# 随附字体

使用 Adobe 官方的简体中文地区子集 OTF，未修改字体文件。随模板携带，无需安装到操作系统。

- [思源宋体 Source Han Serif](https://github.com/adobe-fonts/source-han-serif)：`SourceHanSerifCN-Regular.otf`、`SourceHanSerifCN-Bold.otf`。来源提交 `7889f11bf31170b5d092a083b357c8c8130f89e0`，目录 `SubsetOTF/CN/`。
- [思源黑体 Source Han Sans](https://github.com/adobe-fonts/source-han-sans)：`SourceHanSansCN-Regular.otf`、`SourceHanSansCN-Bold.otf`。来源提交 `a4f7cf94edfb9d7ffbdfc4841de276358bd7e0f2`，目录 `SubsetOTF/CN/`。

字体总计约 39 MiB；分别附带原始 SIL Open Font License 1.1 许可证。转发模板时保留许可证。

字体配置位于 `config/base.tex`。四个随附 OTF 全部存在时使用思源字体；任意一个缺失时，整套中文字体回退到 TeX 发行版自带的 Fandol，避免 Regular / Bold 字重指向不存在的文件。

更换字体时同步设置 Regular 与 Bold 文件名，并保留相应许可证。中文斜体使用 Fandol 楷体，西文字体由主配置单独设置。
