# 墨线 Beamer 模板

用于中文学术组会、课程展示与技术分享的 Beamer 模板。采用白底、思源宋体粗标题、思源黑体正文、蓝色细横线及简洁页码；封面主标题使用淡灰圆角背景。

项目提供大小两种 16:9 版式，共用一份 `main.tex` 与同一套正文。随附按功能组织的语法示例，可查找并复制所需页面。

## 快速开始

1. 在 `config/metadata.tex` 中设置标题、作者、单位与日期。未填写的作者和单位不显示。
2. 在 `main.tex` 的“选择版式”处选择 `style-small` 或 `style-large`。
3. 从 `sections/` 复制需要的 `frame`，替换正文、图片与文献。
4. 在 `00-Template` 目录运行：

```sh
tectonic main.tex
```

输出为 `main.pdf`。`main-small.pdf` 和 `main-large.pdf` 是两种版式的预览快照；普通编译只更新 `main.pdf`。

### 编译环境

- 推荐 Tectonic，首次编译或新增宏包时需要联网下载依赖。
- 支持包含 ctex、Beamer、fontspec、biblatex、csquotes 与 Fandol 的 TeX Live / MiKTeX，使用 XeLaTeX 编译。
- 使用当前 BibTeX 文献后端时，XeLaTeX 的编译顺序为：

```sh
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

文件使用 UTF-8 编码；不支持 pdfLaTeX。不需要安装随附字体到操作系统，也不依赖外部主题或代码高亮程序。

## 版式与字体

在 `main.tex` 的 `documentclass` 之前选择一种版式：

```latex
\input{config/style-small} % 或 config/style-large
```

| 项目 | 小版（默认） | 大版 |
| --- | --- | --- |
| 页面尺寸 | 16 × 9 cm | 24 × 13.5 cm |
| 文档字号 | 11pt | 14pt |
| 左右边距 | 0.9 cm | 1.2 cm |
| 页脚 | 当前页 / 总页数 | 当前页 / 总页数 |

中文标题和表格使用思源宋体，正文使用思源黑体；四个随附 OTF 文件中任意一个缺失时，整套中文字体回退到 TeX 发行版提供的 Fandol。西文正文使用 Latin Modern，参考文献、引文环境与脚注使用 Times 风格的 TeX Gyre Termes。字体来源及许可证见 [fonts/README.md](fonts/README.md)。

目录采用淡蓝底章节编号、直立宋体粗标题与较轻的黑体小节。默认单栏；放不下时测量不同章节分界，选择两栏高度较均衡的位置。两栏顶部对齐，长条目换行后对齐标题文字。双栏仍超出容量时以单栏续页显示全部条目，不自动缩小字号。

章节、小节自动生成居中过渡页；星号形式不进入目录，也不生成过渡页。正文页码采用“当前 / 总数”，`\appendix` 之后采用独立的“A-当前 / A-总数”。

## 示例索引

| 文件 | 内容 |
| --- | --- |
| [01-text.tex](sections/01-text.tex) | 页面与章节、文字强调、嵌套列表、术语列表、链接、代码 |
| [02-blocks.tex](sections/02-blocks.tex) | 三色 Block、分栏组合、段落注释 |
| [03-figures.tex](sections/03-figures.tex) | 分栏、插图、并排图片、图题与交叉引用 |
| [04-tables.tex](sections/04-tables.tex) | 三线表、粗体表头、自动列宽、合并表头与表格引用 |
| [05-math-overlays.tex](sections/05-math-overlays.tex) | 公式、矩阵、分段函数、定理证明、动画与内部链接 |
| [06-references.tex](sections/06-references.tex) | 引文、普通脚注、文献引用与文献表语法 |
| [90-appendix.tex](sections/90-appendix.tex) | 文献表、术语表、长内容续页与特殊页面 |

删除 `main.tex` 中对应的 `\input` 可以移除一个示例章节。使用自己的章节时，按需要保留配置与附录即可。

## 自定义命令与环境

以下是模板提供的写作接口。标准的 `frame`、`columns`、`block`、`\alert`、`\caption` 与文献引用命令仍可直接使用。

### 重点文字：`\keypoint`

```latex
\keypoint{核心结论}
```

使用主题蓝与粗体，适合段落或列表中的重点短语。

### 独立段落注释：`\slideNote`

```latex
这是正文。
\slideNote{补充解释、假设或阅读提示。可以包含 $n>0$ 和\textbf{重点}。

这里是注释的第二段。}
这里继续正文。
```

无标题栏、无阴影的淡灰圆角背景，使用 `\small` 灰色直立文字。自动适应当前栏宽，支持多段文字，结束后恢复正文样式。适合短说明；较长内容应分段或拆页。

### 来源说明：`\sourceNote`

```latex
\sourceNote{来源：\parencite{example2026}。}
```

使用小字号、辅助灰和 Times 风格西文字体，不添加脚注编号。图表专属出处紧随对应图表或题注，置于相同栏内；整页共有出处可放在分栏之后。

### 插图：`\slideimage`

```latex
\centering
\slideimage{result.png}
% 或指定高度上限：
\slideimage[0.45\textheight]{result.png}
```

参数为 `\slideimage[高度上限]{文件名}`，默认高度上限 `0.58\textheight`，宽度上限为当前 `\linewidth`。图片保持比例，同时满足宽、高限制；命令本身不添加居中、图题或编号。

图片放在 `figures/` 后可只写文件名。需要图题时使用标准 `figure`、`\caption` 和 `\label`。素材约定见 [figures/README.md](figures/README.md)。

### 表头：`\tablehead` 与列类型 `Y`

```latex
\begin{tabularx}{\linewidth}{@{}lY@{}}
  \toprule
  \tablehead{方法} & \tablehead{说明} \\
  \midrule
  示例 & 自动分配宽度，长文字自然换行。 \\
  \bottomrule
\end{tabularx}
```

`\tablehead{列名}` 将当前单元格加粗；每个表头单元格分别标记，合并单元格可写 `\multicolumn{2}{c}{\tablehead{分组标题}}`。表格使用衬线体、1.2 倍行距。`Y` 是自定义的左对齐 `X` 列，配合 `tabularx` 自动分配宽度。

### 宽松要点：`keypoints`

```latex
\begin{keypoints}
  \item 第一个核心观点。
  \item 第二个核心观点。
\end{keypoints}
```

内容写法与 `enumerate` 相同，增加顶部留白与条目间距。适合短要点；密集列表仍可使用标准 `enumerate` 或 `itemize`。

### 自适应目录：`\InkAutoToc`

```latex
\begin{frame}[plain,allowframebreaks,noframenumbering]{目录}
  \InkAutoToc
\end{frame}
```

自动选择单栏、双栏或续页；`allowframebreaks` 支持超长目录分页。由 `config/toc.tex` 实现，不必手工填写章节范围。

### 引用字体：`\TimesCite`

```latex
{\TimesCite Times-style reference text.}
```

切换到模板配置的 Times 风格西文字体；局部分组结束后恢复。中文仍由中文字体配置决定。`quote`、`quotation`、文献表和脚注已应用对应设置，普通写作无需手动切换。

### 三色 Block

`block`、`alertblock` 和 `exampleblock` 是 Beamer 原生环境，模板只定制其外观：分别采用墨蓝、砖红与灰绿，圆角、无阴影，并提供内边距。

```latex
\begin{alertblock}{适用条件}
  这里写限制或需要关注的内容。
\end{alertblock}
```

## 配置文件

| 文件 | 职责 |
| --- | --- |
| `main.tex` | 唯一编译入口与章节顺序 |
| `config/metadata.tex` | 标题、作者、单位与日期 |
| `config/style-small.tex`、`config/style-large.tex` | 页面尺寸、字号、边距和页脚 |
| `config/base.tex` | 字体、宏包、文献和常用写作命令 |
| `config/colors.tex` | 主题色、Block 色与注释背景 |
| `config/layout.tex` | 页标题、封面、页码、过渡页与列表 |
| `config/toc.tex` | 目录模板、分栏测量与续页 |
| `config/blocks.tex` | Block 布局与内边距 |
| `config/commands.tex` | 目录与脚注的字体设置 |

版式文件通过 `\SlideGeometry` 设置页面，使用 `\ApplySlideStyle` 应用字号和页脚；这两个初始化宏已由 `main.tex` 调用。常用参数包括 `\InkMargin`（左右边距）、`\SourceNoteSize`（来源字号）、`\InkTopRule`（标题横线粗细）和 `\InkBlockPadding`（Block 内边距）。其余 `Ink...` 命令主要用于内部实现。

## 文献与附录

文献写在 `references/references.bib`，正文使用 `\textcite{键}`、`\parencite{键}` 或 `\footcite{键}`。`example2026` 是虚构排版示例，正式汇报时替换为真实条目。

默认使用 `biblatex + BibTeX`，适配 Tectonic；Tectonic 不提供 Biber。需要 Biber 时使用配备该程序的 XeLaTeX 工具链，并修改 `backend`。文献表字体通过 `\bibfont` 设置。

`\appendix` 切换到附录页码。移除附录时同时删除该命令和 `\input{sections/90-appendix}`。

## 编译排查

```sh
tectonic --keep-logs main.tex
```

检查日志中的 `Missing character`、`Overfull` 和 `undefined`，并查看实际 PDF。目录与交叉引用需要多轮编译，Tectonic 会自动完成。

中文斜体回退到 Fandol 楷体；在当前 XeTeX/Tectonic 链路中，这部分文字可能缺少正确的 ToUnicode 映射，显示正常但搜索、复制不可靠。普通正文、标题和目录使用随附思源字体。
