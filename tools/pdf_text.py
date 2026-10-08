"""Extract per-page text from a XeLaTeX/Tectonic PDF (no third-party PDF libs).

Why this exists: this machine has no pypdfium2 / pypdf / LibreOffice / pdftoppm,
and Pillow 12 cannot open PDFs, so the only way to check what actually landed on
each page is to parse the PDF by hand:
  1. expand object streams (ObjStm) into a {objnum: object-body} map
  2. read the page tree (/Type /Page -> /Contents), in document order
  3. for each page, resolve /Fn -> font object -> /BaseFont subset prefix
  4. decode the content stream's hex strings through that font's ToUnicode CMap

Usage:  python pdf_text.py <file.pdf>
"""

import re
import sys
import zlib


def inflate(raw):
    try:
        return zlib.decompress(raw)
    except Exception:
        return raw


def build_objects(data):
    """Return {objnum: body_bytes} with object streams expanded."""
    objects = {}
    objstm_bodies = []

    for m in re.finditer(rb"(\d+)\s+0\s+obj\b(.*?)endobj", data, re.S):
        num, body = int(m.group(1)), m.group(2)
        if b"/ObjStm" in body:
            sm = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
            if sm:
                objstm_bodies.append((body, inflate(sm.group(1).rstrip(b"\r\n"))))
        objects[num] = body

    for header, inner in objstm_bodies:
        n = re.search(rb"/N\s+(\d+)", header)
        first = re.search(rb"/First\s+(\d+)", header)
        if not n or not first:
            continue
        n, first = int(n.group(1)), int(first.group(1))
        pairs = re.findall(rb"(\d+)\s+(\d+)", inner[:first])
        for i in range(min(n, len(pairs))):
            onum = int(pairs[i][0])
            start = first + int(pairs[i][1])
            end = (
                first + int(pairs[i + 1][1])
                if i + 1 < len(pairs)
                else len(inner)
            )
            objects.setdefault(onum, inner[start:end])
    return objects


def parse_cmaps(objects):
    """subset-prefix -> {code:int -> character}, resolved via each font's /ToUnicode."""
    cmaps = {}
    # Map ToUnicode stream object -> CMap table
    stream_tables = {}
    for num, body in objects.items():
        sm = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
        if not sm:
            continue
        # NB: the CMap marker lives *inside* the deflated stream, so the stream
        # must be inflated before it can be recognised.
        inflated = inflate(sm.group(1).rstrip(b"\r\n"))
        if b"beginbfchar" not in inflated and b"beginbfrange" not in inflated:
            continue
        text = inflated.decode("latin-1", "replace")
        table = {}
        for src, dst in re.findall(r"<([0-9A-Fa-f]{2,4})>\s*<([0-9A-Fa-f]{2,8})>", text):
            try:
                table[int(src, 16)] = bytes.fromhex(dst).decode("utf-16-be", "replace")
            except Exception:
                pass
        if table:
            stream_tables[num] = table

    # Font objects point at their CMap through /ToUnicode
    for num, body in objects.items():
        bf = re.search(rb"/BaseFont\s*/([A-Z]{6})\+", body)
        tu = re.search(rb"/ToUnicode\s+(\d+)\s+0\s+R", body)
        if not bf or not tu:
            continue
        table = stream_tables.get(int(tu.group(1)))
        if table:
            cmaps[bf.group(1).decode()] = table
    return cmaps


def content_of(objects, body):
    """Return decompressed stream bytes of an object body, or None."""
    sm = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
    if not sm:
        return None
    return inflate(sm.group(1).rstrip(b"\r\n"))


def page_objects(objects, refs_body):
    """Collect object bodies for /Fn -> N 0 R font resources in a resource dict."""
    font_res = {}
    body = refs_body
    # /Resources may itself be an indirect reference
    rm = re.search(rb"/Resources\s+(\d+)\s+0\s+R", body)
    if rm:
        body = objects.get(int(rm.group(1)), b"")
    # font entries may be inline (/F1 12 0 R) or listed in a /Font << ... >> dict
    fm = re.search(rb"/Font\s*(\d+)\s+0\s+R", body)
    if fm:
        body = objects.get(int(fm.group(1)), b"") + body
    for m in re.finditer(rb"/(F\d+)\s+(\d+)\s+0\s+R", body):
        font_res[m.group(1).decode()] = int(m.group(2))
    return font_res


def content_streams(objects, page_body):
    """Return the concatenated decompressed content stream(s) of a page.

    dvipdfmx writes either /Contents N 0 R or the array form /Contents[N 0 R ...].
    """
    refs = []
    m = re.search(rb"/Contents\s*\[([^\]]*)\]", page_body)
    if m:
        refs = [int(x) for x in re.findall(rb"(\d+)\s+0\s+R", m.group(1))]
    else:
        m = re.search(rb"/Contents\s+(\d+)\s+0\s+R", page_body)
        if m:
            refs = [int(m.group(1))]
    parts = []
    for r in refs:
        c = content_of(objects, objects.get(r, b""))
        if c:
            parts.append(c)
    return b"\n".join(parts) if parts else None


def decode_page(objects, cmaps, page_body):
    """Decode one page object's text."""
    font_res = page_objects(objects, page_body)
    prefix_of = {}
    for rname, onum in font_res.items():
        fbody = objects.get(onum, b"")
        bf = re.search(rb"/BaseFont\s*/([A-Z]{6})\+", fbody)
        if bf:
            prefix_of[rname] = bf.group(1).decode()

    content = content_streams(objects, page_body)
    if content is None:
        return None

    pieces = []
    for m in re.finditer(
        rb"/(F\d+)\s+[\d.]+\s+Tf(.*?)(?=/(?:F\d+)\s+[\d.]+\s+Tf|\Z)", content, re.S
    ):
        rname, chunk = m.group(1)[-4:].decode().lstrip("/"), m.group(2)
        table = cmaps.get(prefix_of.get(rname, ""), None)
        # TJ takes an array of strings and kerning numbers: [<hex> -333 <hex>]TJ
        for hexstr in re.findall(rb"<([0-9A-Fa-f]+)>", chunk):
            codes = [int(hexstr[i : i + 4], 16) for i in range(0, len(hexstr), 4)]
            if table and all(c in table for c in codes):
                pieces.append("".join(table[c] for c in codes))
            else:
                pieces.append("<%s>" % hexstr.decode())
        for lit in re.findall(rb"\(((?:[^()\\]|\\.)*)\)\s*Tj", chunk):
            pieces.append(lit.decode("latin-1"))
    return " ".join(pieces)


def page_texts(path):
    objects = build_objects(open(path, "rb").read())
    cmaps = parse_cmaps(objects)
    pages = [
        (num, body)
        for num, body in objects.items()
        if re.search(rb"/Type\s*/Page[^s]", body)
    ]
    pages.sort(key=lambda kv: kv[0])
    out = []
    for num, body in pages:
        out.append((num, decode_page(objects, cmaps, body) or ""))
    return out


def main():
    # Make output UTF-8 regardless of the Windows console codepage.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 2

    pages = page_texts(args[0])
    if "--footers" in flags:
        # The footline is emitted last in each page's content stream, so the final
        # text chunk is the page number. Used to verify main vs appendix numbering.
        for i, (_num, text) in enumerate(pages, 1):
            print(f"page {i:>2}: {text.split()[-1] if text.split() else '(none)'}")
        return 0

    print(f"{len(pages)} pages")
    for i, (num, text) in enumerate(pages, 1):
        print(f"--- page {i} (obj {num}) ---")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
