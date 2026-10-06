# 文学作品阅读站

在线阅读：[https://minsecrus.github.io/tolstoy/](https://minsecrus.github.io/tolstoy/)

## 使用

```powershell
npm install
npm run docs:dev
```

用 `npm run docs:build` 验证站点。部署在子路径时，可通过
`VITEPRESS_BASE` 设置基础路径，例如 `/russian-literature/`。

正文标号和注释后的返回箭头可以双向跳转；《历史问题》的注释放在对应章节末尾，在同页往返。
`npm run books:check-footnotes` 会检查全部脚注和返回链接；该检查也会在构建前自动运行。

## 重新导入《全球通史》

第 83 卷由《全球通史：从史前到21世纪（第7版新校本）》上、下册合订 PDF 生成。原 PDF 不纳入仓库；网站使用已生成的章节 Markdown 和 WebP 插图。需要重新生成时，安装 `pymupdf` 和 `Pillow`，然后依次运行：

```powershell
python scripts/extract-global-history-images.py <PDF路径>
python scripts/import-global-history.py <PDF路径>
npm run docs:build
```

## 重新导入《津巴多普通心理学》

第 84 卷由《津巴多普通心理学（第8版）》中文 PDF 生成，按原书书签拆成章首页、核心概念、关键问题、本章小结和附录。原 PDF 不纳入仓库；网站使用生成的 Markdown 正文和 WebP 图片。导入器会跳过 PDF 中仅作文字背景的空白边框图像，保留框内可提取的正文以及实际图表。

需要重新生成时，安装 `pymupdf` 和 `Pillow`，然后运行：

```powershell
python scripts/extract-zimbardo-images.py <PDF路径>
python scripts/import-zimbardo-psychology.py <PDF路径>
$env:VITEPRESS_BASE='/tolstoy/'
npm run docs:build
```

`scripts/rebuild-library-index.mjs` 会汇总各卷的目录和统计信息；各卷的专用导入脚本会在导入后自动调用它。

## 《历史问题》中文译本与英文原书

第 85 卷为 Hiro Saito 著《The History Problem: The Politics of War Commemoration in East Asia》（中文题名《历史问题：东亚战争纪念的政治》）。中文译本采用 AI 辅助翻译，按序言、导论、六章正文、结论、参考文献、中英对照索引及作者介绍拆为 12 个阅读页面。全部 815 条原书注释合并到对应导论、各章及结论的末尾，正文引用与原注释在同页双向跳转。中文翻译与网站刊载依据网站维护者确认的另行授权；英文原书的 CC BY-NC-ND 4.0 许可及版权页说明载于本卷首页。

未经修改的 293 页英文 PDF 保存在 `docs/public/library/volume-85/the-history-problem.pdf`，来源为[美国国会图书馆](https://www.loc.gov/item/2019666840/)。`scripts/history-problem-source-manifest.json` 保存来源、SHA-256、原书页码和全部 815 个注释编号，供新检出的仓库复核。原书 SHA-256 为 `f2e7d9fb63cbbe45382333d16fe889514d6d22e47eaa3a2314361b306d8f8e00`。

需要重新抽取英文源文件时，安装 `pymupdf` 后运行：

```powershell
python scripts/prepare-history-problem.py docs/public/library/volume-85/the-history-problem.pdf
```

抽取结果写入忽略跟踪的 `tmp/pdfs/history-problem/`，包含逐页正文、注释和来源清单；抽取脚本不会覆盖现有译文。翻译时保留 `[[P:页码]]`、`[[N:分组:编号]]` 与 `[[D:分组:编号]]` 标记，并将 815 条原注释按原分组合并到对应正文页面的末尾，保留每组注释的原书页码范围说明。序言、导论、六章及结论写入 `docs/library/volume-85/chapter-001.md` 至 `chapter-009.md`；参考文献、中英对照索引及作者介绍分别保留 `chapter-018.md`、`chapter-019.md`、`chapter-020.md` 路径，以保持已发布链接有效。正文引用与返回链接分别使用 `href="#note-..."` 和 `href="#note-ref-..."` 同页锚点。参考文献保留原始学术引用资料，索引保留原页码并补充中英对照。

全部 12 个阅读页面及其章末注释就绪后运行：

```powershell
node scripts/finalize-history-problem.mjs
node scripts/finalize-history-problem.mjs --check
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=8192'
npm run docs:build
```

Finalizer 先检查 PDF 校验值、12 个阅读页面、页码及全部 815 条原注释编号，再将标记转为页码锚点和同页双向注释链接，按最终译文及章末注释统计字数，生成本卷导航并汇总总目录。全卷保留 236 个来源页锚点，其中 `page-280` 是无印刷页码的书后作者简介（PDF 第 293 页）内部锚点，公开显示为“书后作者简介（PDF 第 293 页）”。它可重复运行而不重复添加锚点或返回链接；`--check` 只验证，不修改文件。验证以仓库保存的清单为基础；若抽取目录存在，会额外逐项核对抽取结果，也可用 `--source-dir <目录>` 指定抽取目录。普通站点构建使用已完成的 Markdown，无须 Python 或 `tmp/` 源文件。
