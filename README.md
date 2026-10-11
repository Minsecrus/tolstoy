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

## 《代数》逐页英文校录与中文译本

第 86 卷依据用户提供的 Serge Lang《Algebra》第三版修订版扫描 PDF 制作，共 923 个 PDF 页面。全书英文校录、中文翻译及两轮逐页原图核对已完成，按章节和前后附属部分整理为 34 个中文阅读页面和 34 个英文阅读页面。公式由 MathJax 排版为本地矢量 SVG，按公式内容复用缓存；复杂交换图和矩阵保留经过核对的原图裁片。

原 PDF 保留在用户提供的位置，不复制到公共目录。`scripts/algebra-source-manifest.json` 保存原文件 SHA-256、各页尺寸及未经核对的嵌入文字校验值；`scripts/algebra-reading-plan.json` 保存章节拆分计划。原文件 SHA-256 为 `64caa3209751e16dd570f84ed0c660a5ccaca7e3d5d8aa0b7226fcdc85e5ec3c`。

逐页完整英文校录、中文译稿和明确核对记录分别保存于 `source/algebra/en/`、`source/algebra/zh/`、`source/algebra/review/`。每页必须实际查看扫描原图并核对公式；提取文字、渲染图片或生成草稿都不算完成核对。可明确判断的原书公式笔误在英文中保留原印，中文如作修订，必须同时给出读者可见的译校注及页级记录，不能悄悄更改。独立第二遍审校记录保存在 `source/algebra/math-audit*.json`，包含实际核对范围和稿件 SHA-256；`scripts/check-algebra-audits.py` 检查覆盖和版本匹配，不替代原图审查。`source/algebra/WORKFLOW.md` 描述具体制作约定。

安装 `pymupdf` 后，可重新提取参考文字和渲染指定页段：

```powershell
python scripts/prepare-algebra.py <PDF路径> --render 1 100
```

未经核对的参考文字和原页 PNG 写入忽略跟踪的 `tmp/pdfs/algebra/`；这个步骤不会覆盖中英译稿或填写核对记录。中英全文及对应核对记录完成后运行：

```powershell
node scripts/check-algebra-math.mjs
python scripts/check-algebra-audits.py --require-complete
node scripts/finalize-algebra.mjs --source-pdf <PDF路径>
node scripts/finalize-algebra.mjs --source-pdf <PDF路径> --check
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=8192'
npm run docs:build
```

Finalizer 检查原 PDF 校验值、中英正文、核对状态、未决问题、数学排版语法、图像路径和页码锚点，只将完整完成的连续章节入库。阅读界面显示连续正文和章节导航，逐页来源锚点不可见且不占排版空间；制作记录保留在源文件和验证记录中。`scripts/algebra-continuous-reading.mjs` 仅在生成结果中连接同一章节内跨原书页的未完正文段落，去掉重复的章节首标题、目录页眉和明确的出版页脚，不修改经过核对的逐页源稿。卷首出版信息与书后丛书目录保留原稿和旧地址，隐藏于主导航与站内搜索。`--check` 只验证当前生成结果。数学排版语法检查不能替代对原图的内容核对。普通站点构建直接使用已生成的阅读页面，无须原 PDF、Python 或处理中间图片。

整本中文 PDF 使用 Pandoc 和 XeLaTeX，数学公式保留原生 TeX，中文及数学字体嵌入文件。需要本机安装 SimSun 和 Cambria 字体，以及 Python 的 `pymupdf`、`pypdf`。中文正文、标题和强调统一宋体，标题及强调使用宋体加粗。前言、逻辑预备知识、各部分、各章、附录、参考文献和索引各自从新页开始，章内连续排版，原书页边界不触发分页。目录重新生成，覆盖这些主章节与数学小节，标题和译本页码均可点击跳转。各源页首尾的零尺寸标记随实际内容行输出，多遍排版据此在页眉及 PDF 显示页码中记录原书页码范围，页脚显示译本页序。PDF 保留前言至索引的 909 个来源页面，以新目录替换原书目录，省略卷首出版介绍与书后丛书广告。图形裁片尺寸由 `scripts/algebra-diagram-sizes.json` 记录，使用实际采样密度而非不可靠的 PNG DPI 元数据。

```powershell
python scripts/export-algebra-pdf.py
python scripts/check-algebra-pdf.py
```

成品保存在 `output/pdf/Algebra-Zh.pdf`，随仓库保存，不复制到网站公共目录，也不加入网站下载入口。排版中间文件、来源快照、页码映射及验证报告保存在 `tmp/pdfs/algebra-export/`。
