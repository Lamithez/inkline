# 学术组会 Beamer 模板

用于学术组会汇报的 Beamer 模板：16:9 页面，「墨线」样式（白底、深墨色宋体粗标题、黑体正文、标题下蓝色细横线、简洁页码），支持中英文混排。编译后生成 `main.pdf`。

## 使用方法

1. 在 `config/metadata.tex` 里填写标题和日期。
2. 编辑 `sections/01`–`04` 的内容；需要插图就放进 `figures/`，文献条目写进 `references/references.bib`。
3. 在项目根目录编译：

```sh
tectonic main.tex
```

编译需要 Tectonic，首次运行或新增宏包时需联网。也可用带 ctex、Beamer、biblatex、Fandol 的 TeX Live / MiKTeX，以 XeLaTeX 编译（有引文时依次运行 XeLaTeX → BibTeX → XeLaTeX → XeLaTeX）。**不支持 pdfLaTeX**。所有文件保存为 UTF-8。

## 文件说明

| 文件或目录 | 用途 |
| --- | --- |
| `main.tex` | 唯一编译入口，控制章节顺序 |
| `config/style-small.tex` | 小版：16 × 9 cm、11pt，页脚只有页码（默认） |
| `config/style-large.tex` | 大版：24 × 13.5 cm、14pt，页脚只有页码 |
| `config/base.tex` | 宏包、中文字体、表格、文献、`\keypoint` 等命令 |
| `config/colors.tex` | 墨线配色与三色 Block 语义色 |
| `config/layout.tex` | 页标题、边距、页脚与页码、过渡页、目录模板 |
| `config/blocks.tex` | 三色圆角 Block |
| `config/commands.tex` | 目录与脚注字体 |
| `config/metadata.tex` | 标题与日期 |
| `sections/01`–`04` | 研究背景、调研结果、分析与讨论、结论 |
| `sections/05-examples.tex` | 可复制的示例页（Block、分栏、图文、表格、公式、分步显示） |
| `sections/90-appendix.tex` | 参考文献、术语表与补充材料 |
| `references/references.bib` | 文献库 |
| `figures/` | 图片资源（含占位图与说明） |
| `fonts/` | 随附思源宋体、思源黑体及许可证，无需安装到系统 |

## 切换版式

只改 `main.tex` 中「选择版式」下的这一行即可，两版共用正文、字体、配色与图片：

```latex
\input{config/style-small}   % 改成 style-large 即切换到大版
```

| 项目 | small 小版 | large 大版 |
| --- | --- | --- |
| 页面 / 字号 | 16 × 9 cm，11pt | 24 × 13.5 cm，14pt |
| 左右边距 | 0.9cm | 1.2cm |
| 页脚 | 仅「当前 / 总」 | 仅「当前 / 总」 |

仓库中的 `main-small.pdf` 与 `main-large.pdf` 是两版预览；切换样式并编译后，
`main.pdf` 对应当前选择的样式，默认与小版一致。

## 版式微调

- 封面主标题使用淡灰色圆角背景，无阴影；背景色在 `config/colors.tex` 的 `title panel` 中设置。
  封面、章节与小节过渡页不显示短横线；章节编号用主题蓝，标题保持深墨色。
- 圆角 Block 外边缘与标题横线、正文边界对齐，保留三色、字号及内边距。
- 表格保持衬线体与三线表，行距为 `1.2`（`config/base.tex` 的 `\InkTableStyle`），表头使用 `\textbf`。
- 单栏短列表可使用 `\begin{keypoints} ... \end{keypoints}`，内容写法与 `enumerate` 相同。
  它增加少量顶部留白与条目间距；双栏或 Block 内仍可使用普通列表。
- 两版字号、目录和正文内容保持原有设置。

## 常用写法

| 功能 | 写法 |
| --- | --- |
| 新建页面 | `\begin{frame}{标题} ... \end{frame}` |
| 突出重点 | `\keypoint{重点}` 或 `\alert{强调}` |
| 插入图片 | `\slideimage{result.png}`，限高用 `\slideimage[0.45\textheight]{result.png}` |
| 来源说明 | `\sourceNote{来源：……}` |
| 行内引文 | `\enquote{引文}` |
| 整段引文 | `\begin{quote}...\end{quote}` 或 `\blockquote{...}` |
| 文献引用 | `\textcite{键}` / `\parencite{键}` / `\footcite{键}` |
| 网址与路径 | `\url{网址}`、`\path{路径}` |

## 引用类文字的字体

参考文献、正文引用、引文块（`quote` / `quotation` / `\blockquote`）与脚注统一使用
**Times 风格衬线体**，由 `config/base.tex` 的 `\TimesCite` 提供；正文西文仍是 Latin Modern，
中文仍是思源宋体/黑体。字体族使用 TeX Gyre Termes（Times New Roman 的度量兼容替代品，
随 Tectonic / TeX Live 分发）。要整体更换，只改 `\TimesCite` 一处即可。

`config/base.tex` 中另有 `\renewcommand{\bibfont}{\TimesCite}` —— 文献表字体必须通过
biblatex 的 `\bibfont` 钩子设置，在 frame 里写 `\TimesCite` 会被 biblatex 重置。

## 附录与页码

正文页码是「当前 / 总」；`main.tex` 中 `\appendix` 之后自动切换为附录独立编号 **A-1 / A-3**（附录内重新计数）。参考文献、术语表等附录内容都在 `sections/90-appendix.tex`。

不需要附录时，删除 `main.tex` 中的 `\appendix` 与 `\input{sections/90-appendix}` 两行；不需要示例页时删除 `\input{sections/05-examples}` 一行。

## 参考文献

使用 `biblatex + BibTeX`（作者年份制），文献表自动列出已引用条目并支持分页。`references.bib` 中的 `example2026` 是虚构示例，正式使用前请替换。

**Tectonic 不带 biber**：把 `config/base.tex` 的后端改成 `biber` 会以 `error: program not found` 失败。若需要 biber 的完整多语种（中文作者名、排序）支持，请改用带 biber 的 XeLaTeX 工具链编译，或在 Overleaf 上选择 XeLaTeX + Biber。

## 编译排查

需要排查问题时保留日志：

```sh
tectonic --keep-logs main.tex
```

重点检查 `Missing character`（缺字）、`Overfull`（内容溢出）、`undefined`（未定义引用）与 `Invalid UTF`（编码问题），并以编译退出状态和生成的 PDF 为准。内容过多时优先精简或拆页，不要靠缩小字号硬塞。

**已知限制**：中文斜体/倾斜字形（正文的 `\textit`、目录里的小节标题）使用 Fandol 楷体，该字体在当前 XeTeX + Tectonic 链路下未能生成 ToUnicode 映射，因此这些文字在 PDF 里**显示正常但无法被搜索或复制**。这是模板沿用已久的字体映射问题，不影响排版效果；如需彻底解决需更换中文斜体字体。
