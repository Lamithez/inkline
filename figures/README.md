# 示例图片

本目录是示例手册的素材，不属于 Inkline 库。库不会自动设置图片路径。

## 使用

```latex
\includegraphics[
  width=\linewidth,
  height=0.45\textheight,
  keepaspectratio
]{figures/result.pdf}
```

也可在主文件中设置 `\graphicspath{{figures/}}`，之后只写文件名。支持 PNG、JPG 和 PDF；图表、流程图等矢量内容优先使用 PDF。保留原图比例，裁去截图中的无关区域，文件名建议使用英文和连字符。

## 图题与出处

需要编号时使用标准 `figure`、`\caption` 与 `\label`。专属来源通过 `\inksource{...}` 放在对应图片或题注之后，并保持在同一栏内；整页共有来源放在分栏之后。

## 占位图

`example-figure.png` 是 1280 × 720 的占位图，供 [图片示例](../sections/03-figures.tex) 演示。正式使用时替换为自己的素材。
