# 图片目录

正文中的插图统一放在本目录。`config/base.tex` 已设置 `\graphicspath{{figures/}}`，
因此在 frame 里只写文件名即可，无需带路径。

## 用法

```latex
\slideimage{result.png}                    % 宽度不超过当前栏宽，保持比例
\slideimage[0.45\textheight]{result.png}   % 同时限制高度上限
```

## 约定

- 支持 PNG、JPG、PDF。**矢量图优先导出 PDF**（折线图、流程图），位图分辨率建议 ≥ 200 dpi。
- 保留原图比例，按单栏或双栏所需的宽高选择素材。
- 为便于跨环境引用，文件名建议使用英文和连字符，例如用 `arch-overview.pdf` 而不是 `架构 总览.pdf`。
- 截图尽量裁掉窗口边框与无关界面，只保留要说明的区域。
- 图片过多时先精简或拆页，不要靠缩小字号来塞内容。

## 图题与出处

需要编号时使用标准 `figure`、`\caption` 与 `\label`。图片专属来源通过 `\sourceNote{...}` 放在图片或题注之后，并保持在同一栏内；整页共有来源放在分栏之后。

## 占位图

`example-figure.png` 是 1280 × 720（16:9）的程序生成占位图，供
`sections/03-figures.tex` 演示图文分栏、并排图片、图题与交叉引用。
正式使用时直接用同名文件覆盖，或改名后同步修改正文中的文件名。
