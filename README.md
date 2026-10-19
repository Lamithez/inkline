# 墨线 Inkline

面向中文学术汇报的 Beamer 文档类。白底、思源宋体粗标题、思源黑体正文、蓝色细横线与圆角信息块，提供大小两种 16:9 页面。项目自带按功能组织的示例手册，可复制所需页面用于自己的汇报。

## 安装与最小用法

把 **`inkline.cls` 和整个 `inkline/` 目录**一并复制到新项目的根目录，与主文件放在同一级。`sections/`、`figures/`、`references/` 和示例 PDF 都不是库运行所必需的。

```latex
\documentclass{inkline}
\title{汇报标题}
\author{作者}
\institute{单位}
\date{\today}

\begin{document}
\begin{frame}[plain,noframenumbering]
  \titlepage
\end{frame}

\begin{frame}{研究问题}
  这里写正文，使用 \alert{重点文字}。
  \inknote{这里写补充说明或适用条件。}
\end{frame}
\end{document}
```

在主文件所在目录编译：

```sh
tectonic main.tex
```

也支持完整 TeX Live / MiKTeX 中的 XeLaTeX；不支持 pdfLaTeX 或 LuaLaTeX。Tectonic 首次编译或获取新宏包时需要联网。文件使用 UTF-8，不需要安装随附字体到系统。

库自动初始化字体、页面、主题和页脚；不读取用户的标题文件、示例正文、图片目录或文献库。复制库后，直接使用标准的标题、分栏、插图、图题和数学命令即可。

## 文档类选项

```latex
\documentclass[size=large,bibliography]{inkline}
```

| 选项 | 默认值 | 作用 |
| --- | --- | --- |
| `size=small` | 是 | 16 × 9 cm，11pt，左右边距 0.9 cm |
| `size=large` | 否 | 24 × 13.5 cm，14pt，左右边距 1.2 cm |
| `bibliography` | 否 | 加载 BibLaTeX，使用 BibTeX 后端 |

其他 Beamer 选项可以直接传入，例如 `handout`。页面尺寸和文档字号统一由 `size` 控制，不要再同时传入其他字号或纵横比选项。

## 公开写作接口

标准命令优先；模板仅提供五项有明确排版作用的接口：

| 接口 | 用途 |
| --- | --- |
| `\inknote{内容}` | 无标题的段落注释 |
| `\inksource{出处}` | 图表来源与简短出处 |
| `\inkcontents` | 自适应目录 |
| `inkpoints` 环境 | 间距较宽松的有序要点 |
| `Y` 列类型 | `tabularx` 中左对齐、自动分配宽度的列 |

### 段落注释

```latex
这是正文。
\inknote{补充条件：$n>0$，可包含\textbf{重点}与链接。

空行可分隔注释内部的多个段落。}
这里继续正文。
```

注释使用浅灰直角背景，深蓝细竖线贴齐背景左缘，无标题栏、无阴影；文字为 `\small` 深墨灰色直立衬线体，上下内边距为 `0.45em`，自动适应当前栏宽，结束后恢复正文样式。适合补充解释和短提示，较长内容应拆页。`\note` 仍是 Beamer 原生的演讲者备注命令，与此接口无关。

### 来源说明

```latex
\inksource{来源：公开数据集或参考文献。}
```

使用小字号、辅助灰和 Times 风格西文字体，不添加脚注编号。图表专属来源放在对应图表或题注后，并保持在同一栏内；整页共有来源放在分栏之后。

### 目录与宽松列表

```latex
\begin{frame}[plain,allowframebreaks,noframenumbering]{目录}
  \inkcontents
\end{frame}

\begin{frame}{核心观点}
  \begin{inkpoints}
    \item 第一个观点。
    \item 第二个观点。
  \end{inkpoints}
\end{frame}
```

目录默认单栏；超出高度后选择章节分界，形成顶部对齐、较均衡的双栏。双栏仍超高时按单栏续页，不缩小字号或隐藏条目。长条目采用悬挂缩进。`allowframebreaks` 是目录续页所必需的。

`inkpoints` 的写法与 `enumerate` 相同，提供顶部留白和较宽的条目间距；密集列表使用标准 `enumerate` 或 `itemize` 即可。

## Block：有标题与无标题

`block`、`alertblock`、`exampleblock` 是 Beamer 原生环境。Inkline 分别使用墨蓝、砖红与灰绿，提供圆角、内边距，并关闭阴影。

```latex
\begin{block}{核心问题}
  有标题时显示标题栏。
\end{block}

\begin{alertblock}{}
  空标题时只显示正文区域。
\end{alertblock}

\begin{exampleblock}{   }
  纯空格标题同样不显示标题栏。
\end{exampleblock}
```

无标题时不保留空白标题高度；字体、背景色和内边距仍按块类型生效。仍需提供标题参数 `{}`，因为这是 Beamer 环境的标准语法。

## 图片、表格与强调

使用原生图片命令指定宽、高上限和保持比例：

```latex
\includegraphics[
  width=\linewidth,
  height=0.45\textheight,
  keepaspectratio
]{figures/result.pdf}
```

库不设置 `\graphicspath`。可在自己的导言区添加 `\graphicspath{{figures/}}`，也可始终写出图片路径。`figure`、`\caption`、`\label` 和 `\ref` 用于编号图题与交叉引用。图片约定见 [figures/README.md](figures/README.md)。

表格采用衬线字体和 1.2 倍行距，表头直接用标准粗体：

```latex
\begin{tabularx}{\linewidth}{@{}lY@{}}
  \toprule
  \textbf{方法} & \textbf{说明} \\
  \midrule
  示例 & 自动分配宽度，长文字自然换行。 \\
  \bottomrule
\end{tabularx}
```

强调使用 `\alert{文字}`，分步强调使用 `\alert<2>{文字}`；不需要额外封装。`\pause`、`\only`、`\uncover`、`columns` 和定理环境均沿用 Beamer 原生语法。

## 文献、字体与页码

需要文献时启用选项，并自行指定文献库：

```latex
\documentclass[bibliography]{inkline}
\addbibresource{references.bib}
```

正文使用 `\textcite{键}`、`\parencite{键}`、`\footcite{键}`。文献表使用 `\printbibliography[heading=none]`；长文献表放在带 `allowframebreaks` 的 frame 中。默认不启用时，库不会加载 BibLaTeX，也不会尝试查找任何 `.bib` 文件。

Tectonic 自动完成多轮排版与 BibTeX。XeLaTeX 启用文献后的编译顺序为 XeLaTeX → BibTeX → XeLaTeX → XeLaTeX。当前内置后端为 BibTeX，不要求 Biber。示例条目 `example2026` 为虚构内容，正式使用时替换。

`inkline/fonts/` 随附四个思源 OTF，全部存在时使用思源；任何一个缺失时整套中文字体回退到 Fandol。字体与许可证说明见 [inkline/fonts/README.md](inkline/fonts/README.md)。西文正文为 Latin Modern，引用环境、来源与脚注采用 Times 风格的 TeX Gyre Termes。

正文页码显示“当前 / 总数”，`\appendix` 之后显示独立的“A-当前 / A-总数”。章节、小节自动生成过渡页；星号形式不进入目录，也不触发过渡页。

## 项目与示例索引

| 文件或目录 | 用途 |
| --- | --- |
| `inkline.cls` | 唯一公共加载入口 |
| `inkline/` | 内部模块与可选字体；和文档类一起复制 |
| `main.tex` | 示例手册唯一编译入口，选择版式并指定示例资源 |
| [01-text.tex](sections/01-text.tex) | 类选项、页面、文字、列表、链接、代码 |
| [02-blocks.tex](sections/02-blocks.tex) | 三类有标题和无标题 Block、注释与来源 |
| [03-figures.tex](sections/03-figures.tex) | 分栏、插图、图题与交叉引用 |
| [04-tables.tex](sections/04-tables.tex) | 表格、粗体表头、合并单元格 |
| [05-math-overlays.tex](sections/05-math-overlays.tex) | 公式、定理、逐步展示与内部链接 |
| [06-references.tex](sections/06-references.tex) | 引文、脚注与文献表 |
| [90-appendix.tex](sections/90-appendix.tex) | 附录、参考文献、术语与续页 |

`main-small.pdf` 和 `main-large.pdf` 是两种版式的预览快照；普通编译只更新 `main.pdf`。改动配色可编辑 `inkline/colors.tex`；其他内部模块不需要用户手工加载。`\ink@...` 名称为内部实现，不属于稳定写作接口。

## 旧写法迁移

不提供旧名称别名，使用旧模板的汇报按下表替换：

| 旧写法 | 新写法 |
| --- | --- |
| 手动输入配置文件并初始化 | `\documentclass[size=small]{inkline}` |
| `\slideimage` | `\includegraphics`，显式填写所需尺寸选项 |
| `\tablehead` | `\textbf` |
| `\keypoint` | `\alert` |
| `\slideNote` | `\inknote` |
| `\sourceNote` | `\inksource` |
| `\InkAutoToc` | `\inkcontents` |
| `keypoints` 环境 | `inkpoints` 环境 |

## 编译排查

```sh
tectonic --keep-logs main.tex
```

检查 `Missing character`、`Overfull`、未解析引用与实际 PDF。所有文件使用 UTF-8，保留完整库目录，并从主文件所在目录编译。中文斜体使用 Fandol 楷体；在部分 XeTeX/Tectonic 环境中，这部分文字的 PDF 搜索、复制可能不可靠。
