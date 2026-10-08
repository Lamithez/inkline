# 随附字体

使用 Adobe 官方的简体中文地区子集 OTF，未修改字体文件。随模板携带，无需安装到操作系统。

- [思源宋体 Source Han Serif](https://github.com/adobe-fonts/source-han-serif)：`SourceHanSerifCN-Regular.otf`、`SourceHanSerifCN-Bold.otf`。来源提交 `7889f11bf31170b5d092a083b357c8c8130f89e0`，目录 `SubsetOTF/CN/`。
- [思源黑体 Source Han Sans](https://github.com/adobe-fonts/source-han-sans)：`SourceHanSansCN-Regular.otf`、`SourceHanSansCN-Bold.otf`。来源提交 `a4f7cf94edfb9d7ffbdfc4841de276358bd7e0f2`，目录 `SubsetOTF/CN/`。

字体总计约 39 MiB；分别附带原始 SIL Open Font License 1.1 许可证。转发模板时保留许可证。

字体选择集中在 `config/base.tex` 的 `\IfFileExists` 分支中（有思源字体用思源，缺失时整套回退到 Fandol），主字体对应宋体，无衬线字体对应黑体。更换字体时同步修改 Regular 和 Bold 文件名。若不需要思源字体，可整组移除这些 OTF，模板将自动使用原有 Fandol 配置；不要只删除 Bold 文件。
