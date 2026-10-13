# 模板来源与本地适配

来源：https://github.com/billryan/resume

2026-09-11 从 master 分支获取 resume.cls、resume_photo.tex 和 LICENSE。
本目录保留原始照片示例与 MIT 许可证；实际使用的类文件位于上一级 resume.cls。

本地适配：将类文件依赖的外置英文字体改为系统 TeX Gyre Termes；正文使用 Noto Serif CJK SC，标题使用 Noto Sans CJK SC；保留模板的日期对齐结构，调整为右上角照片区与中文单页排版。

照片已插入右上角，使用用户提供的同目录 JPG 文件，在 27 mm × 36 mm 区域内保持原始比例，不裁剪、不修改照片。

编译命令（在上一级目录执行）：

```bash
xelatex -interaction=nonstopmode -halt-on-error resume_zh.tex
```
