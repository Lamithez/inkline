# 学术组会 Beamer 模板

用于学术组会汇报的 Beamer 模板：16:9 页面，「墨线」样式（白底、深墨色宋体粗标题、黑体正文、标题下蓝色细横线、简洁页码），支持中英文混排。正文是一份按功能组织的语法示例手册，编译后生成 `main.pdf`。

## 使用方法

1. 在 `config/metadata.tex` 里填写标题和日期。
2. 从 `sections/01`–`06` 按功能查找并复制所需页面，替换成自己的内容；图片放进 `figures/`，文献条目写进 `references/references.bib`。
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
| `sections/01-text.tex` | 页面与章节、文字强调、嵌套列表、术语列表、网址、代码 |
| `sections/02-blocks.tex` | 三色 Block、分栏组合、独立段落注释 |
| `sections/03-figures.tex` | 等宽与不等宽分栏、插图、并排图片、图题与交叉引用 |
| `sections/04-tables.tex` | 粗体表头、三线表、自动列宽、合并表头、表格引用 |
| `sections/05-math-overlays.tex` | 公式、矩阵、分段函数、定理证明、分步显示、内部链接 |
| `sections/06-references.tex` | 引文、脚注、文献引用与文献表语法 |
| `sections/90-appendix.tex` | 实际文献表、术语表、续页与特殊页面 |
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
- 表格保持衬线体与三线表，行距为 `1.2`（`config/base.tex` 的 `\InkTableStyle`），表头每个单元格使用 `\tablehead{文字}`。
- 单栏短列表可使用 `\begin{keypoints} ... \end{keypoints}`，内容写法与 `enumerate` 相同。
  它增加少量顶部留白与条目间距；双栏或 Block 内仍可使用普通列表。
- 两版字号保持原有设置；目录含 section 与 subsection，默认单栏。
  `\InkAutoToc` 按实际排版高度判断，超出可用高度时自动按完整章节拆成两栏；
  两栏顶部对齐，并保留标题横线下方的留白。

## 常用写法

| 功能 | 写法 |
| --- | --- |
| 新建页面 | `\begin{frame}{标题} ... \end{frame}` |
| 突出重点 | `\keypoint{重点}` 或 `\alert{强调}` |
| 独立段落注释 | `\slideNote{补充解释或阅读提示。}` |
| 表头加粗 | `\tablehead{列名}`，每个表头单元格分别标记 |
| 插入图片 | `\slideimage{result.png}`，限高用 `\slideimage[0.45\textheight]{result.png}` |
| 来源说明 | `\sourceNote{来源：……}` |
| 行内引文 | `\enquote{引文}` |
| 整段引文 | `\begin{quote}...\end{quote}` 或 `\blockquote{...}` |
| 文献引用 | `\textcite{键}` / `\parencite{键}` / `\footcite{键}` |
| 网址与路径 | `\url{网址}`、`\path{路径}` |

## 注释与表头

`\slideNote` 是本模板自定义的独立段落宏：淡灰圆角背景、无标题栏、无阴影，
文字使用比默认正文小一档的 `\small` 字号和灰色直立字形。它自动适应单栏或分栏宽度，
可包含公式、加粗、链接以及用空行分隔的多个段落，结束后恢复正文样式。
颜色集中在 `config/colors.tex` 的 `annotation` 中，内边距在 `config/base.tex` 中设置。
简短出处仍使用 `\sourceNote`；需要带语义标题的内容使用三类 Block。

```latex
这是正文。
\slideNote{这里说明一个假设或补充条件。}
这里继续正文。
```

`\tablehead` 是 `\textbf` 的语义封装，沿用表格的衬线字体。
表头需显式标记，不会把数据的第一行误当成表头；合并表头同样适用：

```latex
\tablehead{方法} & \tablehead{准确率} \\
\multicolumn{2}{c}{\tablehead{分组标题}} \\
```

## 引用类文字的字体

参考文献、正文引用、引文块（`quote` / `quotation` / `\blockquote`）与脚注统一使用
**Times 风格衬线体**，由 `config/base.tex` 的 `\TimesCite` 提供；正文西文仍是 Latin Modern，
中文仍是思源宋体/黑体。字体族使用 TeX Gyre Termes（Times New Roman 的度量兼容替代品，
随 Tectonic / TeX Live 分发）。要整体更换，只改 `\TimesCite` 一处即可。

`config/base.tex` 中另有 `\renewcommand{\bibfont}{\TimesCite}` —— 文献表字体必须通过
biblatex 的 `\bibfont` 钩子设置，在 frame 里写 `\TimesCite` 会被 biblatex 重置。

## 附录与页码

正文页码是「当前 / 总」；`main.tex` 中 `\appendix` 之后自动切换为附录独立编号 **A-当前 / A-总数**（附录内重新计数）。参考文献、术语表等附录内容都在 `sections/90-appendix.tex`。

不需要附录时，删除 `main.tex` 中的 `\appendix` 与 `\input{sections/90-appendix}` 两行。
各功能章节可通过删除对应的 `\input` 独立移除，目录和页码自动更新。

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
