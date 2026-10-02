# 文学作品阅读站

在线阅读：[https://minsecrus.github.io/tolstoy/](https://minsecrus.github.io/tolstoy/)

## 使用

```powershell
npm install
npm run docs:dev
```

用 `npm run docs:build` 验证站点。部署在子路径时，可通过
`VITEPRESS_BASE` 设置基础路径，例如 `/russian-literature/`。

正文使用到的注释会添加在对应页面末尾；正文标号和注释后的返回箭头可以在本页内双向跳转。
`npm run books:check-footnotes` 会检查全部脚注和返回链接；该检查也会在构建前自动运行。

## 重新导入《全球通史》

第 83 卷由《全球通史：从史前到21世纪（第7版新校本）》上、下册合订 PDF 生成。原 PDF 不纳入仓库；网站使用已生成的章节 Markdown 和 WebP 插图。需要重新生成时，安装 `pymupdf` 和 `Pillow`，然后依次运行：

```powershell
python scripts/extract-global-history-images.py <PDF路径>
python scripts/import-global-history.py <PDF路径>
npm run docs:build
```

## 重新导入《津巴多普通心理学》

第 84 卷由《津巴多普通心理学（第8版）》中文 PDF 生成，按原书书签拆成章首页、核心概念、关键问题、本章小结和附录。原 PDF 不纳入仓库；网站使用生成的 Markdown 正文和 WebP 图片。需要重新生成时，安装 `pymupdf` 和 `Pillow`，然后运行：

```powershell
python scripts/extract-zimbardo-images.py <PDF路径>
python scripts/import-zimbardo-psychology.py <PDF路径>
$env:VITEPRESS_BASE='/tolstoy/'
npm run docs:build
```

`scripts/rebuild-library-index.mjs` 会汇总各卷的目录和统计信息；两个专用导入脚本会在导入后自动调用它。
