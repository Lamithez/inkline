# 图片目录

正文中的插图统一放在本目录。`config/base.tex` 已设置 `\graphicspath{{figures/}}`，
因此在 frame 里只写文件名即可，无需带路径。

## 用法

```latex
\slideimage{result.png}                    % 按当前栏宽等比缩放
\slideimage[0.45\textheight]{result.png}   % 同时限制高度上限
```

## 约定

- 支持 PNG、JPG、PDF。**矢量图优先导出 PDF**（折线图、流程图），位图分辨率建议 ≥ 200 dpi。
- 横纵比建议 16:9 或 4:3，与页面比例接近时留白最少。
- 文件名避免空格与中文，例如用 `arch-overview.pdf` 而不是 `架构 总览.pdf`。
- 截图尽量裁掉窗口边框与无关界面，只保留要说明的区域。
- 图片过多时先精简或拆页，不要靠缩小字号来塞内容。

## 占位图

`example-figure.png` 是 1280 × 720（16:9）的程序生成占位图，供
`sections/03-analysis.tex` 与 `sections/05-examples.tex` 演示图片用法。
正式使用时直接用同名文件覆盖，或改名后同步修改正文中的文件名。
