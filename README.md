# 文学作品阅读站

在线阅读：[https://minsecrus.github.io/tolstoy/](https://minsecrus.github.io/tolstoy/)

数学著作中文 PDF：[统一下载目录](output/pdf/README.md)。

## 使用

```powershell
npm install
npm run docs:dev
```

用 `npm run docs:build` 验证站点。部署在子路径时，可通过
`VITEPRESS_BASE` 设置基础路径，例如 `/russian-literature/`。

正文标号和注释后的返回箭头可以双向跳转；《历史问题》的注释放在对应章节末尾，在同页往返。
`npm run books:check-footnotes` 会检查全部脚注和返回链接；该检查也会在构建前自动运行。

站内搜索由 [Pagefind](https://pagefind.app/) 提供。`npm run docs:build` 在 VitePress 构建完成后读取生成的网页建立索引，配置见 `pagefind.yml`；索引按需分块加载，中文按词切分。索引只收录正文区域，页面元数据为 `search: false` 的页面不进入搜索。`npm run docs:dev` 没有索引，搜索只在构建后的站点（`npm run docs:preview`）中可用。

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
$env:NODE_OPTIONS='--max-old-space-size=12288'
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
$env:NODE_OPTIONS='--max-old-space-size=12288'
npm run docs:build
```

Finalizer 检查原 PDF 校验值、中英正文、核对状态、未决问题、数学排版语法、图像路径和页码锚点，只将完整完成的连续章节入库。阅读界面显示连续正文和章节导航，逐页来源锚点不可见且不占排版空间；制作记录保留在源文件和验证记录中。`scripts/algebra-continuous-reading.mjs` 仅在生成结果中连接同一章节内跨原书页的未完正文段落，去掉重复的章节首标题、目录页眉和明确的出版页脚，不修改经过核对的逐页源稿。卷首出版信息与书后丛书目录保留原稿和旧地址，隐藏于主导航与站内搜索。`--check` 只验证当前生成结果。数学排版语法检查不能替代对原图的内容核对。普通站点构建直接使用已生成的阅读页面，无须原 PDF、Python 或处理中间图片。

整本中文 PDF 使用 Pandoc 和 XeLaTeX，数学公式保留原生 TeX，中文及数学字体嵌入文件。需要本机安装 SimSun 和 Cambria 字体，以及 Python 的 `pymupdf`、`pypdf`。中文正文、标题和强调统一宋体，标题及强调使用宋体加粗。前言、逻辑预备知识、各部分、各章、附录、参考文献和索引各自从新页开始，章内连续排版，原书页边界不触发分页。目录重新生成，覆盖这些主章节与数学小节，标题和译本页码均可点击跳转。各源页首尾的零尺寸标记随实际内容行输出，多遍排版据此在页眉及 PDF 显示页码中记录原书页码范围，页脚显示译本页序。PDF 保留前言至索引的 909 个来源页面，以新目录替换原书目录，省略卷首出版介绍与书后丛书广告。图形裁片尺寸由 `scripts/algebra-diagram-sizes.json` 记录，使用实际采样密度而非不可靠的 PNG DPI 元数据。

```powershell
python scripts/export-algebra-pdf.py
python scripts/check-algebra-pdf.py
```

成品保存在 `output/pdf/Algebra-Zh.pdf`，随仓库保存，不复制到网站公共目录，也不加入网站下载入口。排版中间文件、来源快照、页码映射及验证报告保存在 `tmp/pdfs/algebra-export/`。

## 《基础范畴论》文字层校录与中文译本

第 87 卷依据用户提供的 Tom Leinster《Basic Category Theory》文字层 PDF 制作，来源文件共 192 页，对应 arXiv:1612.09375v2。全书英文校录、中文全译及两轮逐页原图核对已完成，包含前言、正文、全部证明与习题、附录、延伸阅读和索引。正文从原生文字层提取，不运行全文 OCR；数学符号和交换图仍逐页对照原 PDF，并以作者在 [arXiv 发布的匹配版本 TeX 源码](https://arxiv.org/src/1612.09375v2)辅助核对。原 PDF 和下载的辅助 TeX 不放入网站公共目录。

译文把英语语序、长句和生硬措辞处理为自然中文，不添加原文之外的概念讲解、符号定义或证明说明；这一约定也适用于本项目后续数学著作，见根目录 `AGENTS.md` 与 `.cursor/rules/mathematics-translation.mdc`。

原文件 SHA-256 为 `4d817004b83f46233444c2b3233129cef1154e5e96987fa4be029e040987b59a`。`scripts/category-theory-source-manifest.json` 保存逐页文字层摘要与经实际版面核对的原书页码；`scripts/category-theory-reading-plan.json` 保存阅读部分和小节。原 PDF 内的页标签与索引书签存在错位，因此页码与目录使用实际印刷内容。中英逐页正文、主审核对和绑定当前稿件 SHA-256 的独立二审记录保存在 `source/category-theory/`，制作约定见其中的 `WORKFLOW.md`。

网站只生成前言、致读者、导论、六章、附录、延伸阅读和两个索引，共 13 个学术部分的中英文连续阅读页面；卷首、原目录与空白页保留在源稿中。普通公式使用原生 TeX 和本地 MathJax SVG；复杂图示采用原 PDF 裁片，并在逐页记录中保留裁片 SHA-256、原始坐标与物理宽度。网站正文没有逐页页码横栏、语言切换横栏或制作过程说明。

数学卷 86、87、88 的小项编号（如 `(c)`）保留字面形式，避免 Markdown 自动排版将它们变成版权符号；其他作品的自动排版保持原有行为。

本书原图裁片的网页宽度按原书物理尺寸与正文字号换算，随网页正文字号缩放。尺寸映射预先保存在 `scripts/category-theory-diagram-widths.json`，普通网站构建直接读取它，无须访问原 PDF；句内图保留在原段落中。

```powershell
python scripts/prepare-category-theory.py <PDF路径> --render 1 192
python scripts/prepare-category-theory-diagram-widths.py
node scripts/check-category-theory-math.mjs --require-complete
node scripts/check-mathematical-book-typography.mjs
node scripts/check-category-theory-diagram-renderer.mjs
python scripts/check-category-theory-audits.py --require-complete
node scripts/finalize-category-theory.mjs
node scripts/finalize-category-theory.mjs --check
node scripts/rebuild-library-index.mjs
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=12288'
npm run docs:build
python scripts/export-category-theory-pdf.py
python scripts/check-category-theory-pdf.py
```

中文 PDF 保存为 `output/pdf/Basic-Category-Theory-Zh.pdf`，不复制到网站公共目录或添加网站下载入口。PDF 全部汉字使用宋体，标题和强调使用宋体加粗；主要部分另起新页，章内连续排版，以新可点击目录替代原目录，原书页码范围放在页眉，译本页码放在页脚。排版保留 185 个来源内容页，原书无关卷首和空白页不占导出页。中间文件与验证报告保存在忽略跟踪的 `tmp/pdfs/category-theory-export/`。

目录排为一页，符号索引使用三栏，主题索引使用两栏；索引保留全部条目、层级与跨原书页接续。最终导出文件的独立逐页视觉核验记录保存在 `source/category-theory/export-visual-review.json`。

最终构建后的浏览器核验保存在 `source/category-theory/website-render-review.json`，覆盖章节正文、小项编号、公式加载、裁图尺寸及居中、两处句内图、目录和索引接续。网页核验与 PDF 排版核验均不替代来源数学内容的逐页审校。

原书 © Tom Leinster 2014, 2016，作者发布的 arXiv 版本采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)；本中文翻译及其排版改编同样采用该许可。来源与许可说明保留在原书前言译文和本项目制作记录中。

## 《表示论导论》

第 88 卷依据用户提供的 Etingof 等人《Introduction to Representation Theory》2011 年 AMS 版制作。原文件共 238 页，是附有识别文字层的扫描书；现有文字层辅助录入，不重新运行全文 OCR。来源 SHA-256 为 `2dd757632494b71e95e8b70520e3745ae22b6df5632b7352cc465fcaac6a6563`。数学符号、条件和全文逐页与实际扫描图核对，不把识别文字当成准确原文。

来源清单、实际印刷页码、阅读结构分别保存在 `scripts/representation-theory-source-manifest.json` 与 `scripts/representation-theory-reading-plan.json`。作者官网提供的匹配 2011 年高清版、讲义 TeX 和正式勘误仅作辅助；2024 年更新版的增补内容不混入原书译文。原 PDF、辅助文件和中间稿不进入网站公共目录。

全部 238 页均保留逐页英文校录、中文稿及主译记录；独立审校逐页完整比较扫描图与当前双语稿，审校散列绑定实际文件字节。记录保存在 `source/representation-theory/`，制作约定见其 `WORKFLOW.md`。录入错误直接校正；原书数学错误保留在英文校录中，中文修订以紧邻的可见译校注明示依据。句子写成自然中文，不因为表达偏好添加概念讲解。

阅读正文保留 222 个来源内容页，整理为九章、历史参考文献、数学参考文献和索引，共 12 个连续部分；包括 94 个编号小节、全部证明、习题、提示、脚注、六篇历史插曲与 230 条索引。原书封面、版权、旧目录、空白页与丛书广告仍存入来源记录，排除网站正文导航与导出 PDF。书库正文不显示每页来源条或语言切换条。

普通公式、矩阵、特征标表与对应表采用原生数学排版；55 张复杂箭图、Dynkin 图与分解图保留经过核对的 300 dpi 原图裁片。网页与 PDF 的图片字号按匹配高清版正文及扫描比例标定，尺寸映射预存在 `scripts/representation-theory-diagram-widths.json`。网站使用本书限定的原生脚注插件，保留全部脚注正文、公式与双向跳转，不改变其他卷的脚注处理。

```powershell
python scripts/prepare-representation-theory.py <PDF路径> --render 1 238
python scripts/prepare-representation-theory-diagram-widths.py
node scripts/check-representation-theory-math.mjs --require-complete
python scripts/check-representation-theory-audits.py --require-complete
node scripts/check-representation-theory-continuous-reading.mjs
node scripts/check-representation-theory-footnotes.mjs
node scripts/check-representation-theory-diagram-renderer.mjs
node scripts/check-representation-theory-index.mjs
python scripts/check-representation-theory-index.py
node scripts/finalize-representation-theory.mjs
node scripts/finalize-representation-theory.mjs --check
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=12288'
npm run docs:build
python scripts/export-representation-theory-pdf.py
python scripts/check-representation-theory-pdf.py
```

最终中文 PDF 共 134 页，保存于 `output/pdf/Introduction-to-Representation-Theory-Zh.pdf`，单独提供给用户，不放进网站或添加网站下载入口。汉字、标题和强调使用宋体，标题与强调加粗；数学公式使用原生 TeX。九章与三项附属部分各另起一页，章内连续排版；重新生成涵盖全部数学小节的可跳转目录，页眉保留原书页码范围，页脚标示译本实际页码。中间排版与验证报告位于 `tmp/pdfs/representation-theory-export/`。最终输出的分段视觉检查汇总保存在 `source/representation-theory/export-visual-review.json`。

两册逐页 Markdown 均固定采用 UTF-8 与 LF 换行，避免 Git 检出时改变已审校稿件的字节散列。`scripts/normalize-reviewed-book-line-endings.py` 默认只检查；`--apply` 必须先验证全部主译和独审绑定，并证明仅将 CRLF 改为 LF、不改变正文字符。迁移前后散列保存于各书的 `line-ending-normalization.json`，不据此重新声称数学审校，也不改写既有 PDF。

## 重新导入《操作系统导论》

第 89 卷为 Remzi H. Arpaci-Dusseau 与 Andrea C. Arpaci-Dusseau 著《Operating Systems: Three Easy Pieces》（OSTEP）的人民邮电出版社中文版（王海鹏译），依据作者在[本书官方网站](https://pages.cs.wisc.edu/~remzi/OSTEP/)公开的中文版各章 PDF，按原书顺序合并为 498 页的 PDF 后导入。原 PDF 不纳入仓库，`scripts/ostep-source-manifest.json` 记录其来源与 SHA-256（`a9d54f4c79b8b6ef4dd65e6dbac8f7f00644b97d33001dee239572c770b23e24`）。全书拆为前言、第 1—50 章和附录 A—G 共 58 个阅读页面，侧栏按原书三个部分分组；扉页、内容提要、资源与支持、目录及部分页不单独成页。

原 PDF 中宋体与黑体的 ToUnicode 映射在约 600 处有误（例如“在”被提取为“谁”，“们”被提取为“我”），因此导入器按字形编号对照 Windows 自带的 SimSun/SimHei 字体还原这两种字体的汉字，重新运行需要在装有这两种字体的 Windows 上进行。导入器去掉页眉页脚，把灰底方框转为 VitePress 提示框，保留代码清单的缩进与行号，按原书排版裁出插图（WebP），并把规则表格转为 Markdown 表格；脚注按章编号放在章末，与正文双向链接。

文字层无法可靠还原的部分保存在 `scripts/ostep-reviewed-layout.json`，均已对照页面图像核对：`blocks` 按 PDF 页码和区域替换为手写内容（公式改用 LaTeX，由站点已有的 MathJax 渲染器输出 SVG；含行内分式的段落整段重排），`tables` 收录版式复杂、需按页面图像转写的表格，`text` 记录少量逐字修正（如 PDF 以线条绘制的标识符前导下划线），`code_terms` 按章列出正文中应以行内代码显示的普通单词形式标识符（如 `ticket`、`turn`），以及形状规则误判、应保持普通文字的片段。函数调用、带 `->` 或下划线的标识符、文件名、路径、命令与参数等由导入器按形状自动识别；行内代码与相邻文字各隔一个空格，紧邻全角标点时不加。公式中原书的印刷差错（如式 41.1 的结果印作 109.6KB）按原样保留。

需要重新生成时，安装 `pymupdf`、`fontTools` 和 `Pillow`，然后运行：

```powershell
python scripts/import-ostep.py <PDF路径>
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=12288'
npm run docs:build
```

导入器会校验 PDF 散列，重写 `docs/library/volume-89/`、`docs/public/library/volume-89/images/` 与 `docs/.vitepress/library.ostep.mjs`，并汇总总目录。正文字号的文字若落入插图裁切区域，会列在 `tmp/ostep/figure-text-audit.txt` 中以便复查。

## 第 90—93 卷：由 learning-notes 迁入的译本

《信息检索导论》（第 90 卷）、《时空与几何：广义相对论导论》（第 91 卷）、Carroll《广义相对论讲义》（第 92 卷）和《CS 188 人工智能导论》（第 93 卷）原在 [learning-notes](https://github.com/Minsecrus/learning-notes) 仓库中翻译整理，于该仓库提交 `d56c225` 之后迁入本站，此后以本仓库中的 Markdown 为准。各卷的底本、页码对照和翻译说明见本卷首页。

迁移时页面按原顺序改名为 `chapter-NNN.md`，原系列首页成为本卷首页；站内相对链接改为本站路由，插图复制到 `docs/public/library/volume-9X/images/`，Mermaid 流程图预先渲染为 SVG，《时空与几何》的脚注改为本站带双向链接的注释格式。公式沿用本站的 MathJax SVG 渲染器：learning-notes 自定义的 `\pounds`、`\lefteqn` 分别改写为 `\textsterling` 和 `\rlap{\displaystyle …}`。目录与统计信息保存在 `docs/.vitepress/library.translated-books.mjs`，增删页面时需同步修改该文件并运行 `node scripts/rebuild-library-index.mjs`。

## 重新导入《杜甫全集》

第 94 卷依据用户提供的《杜甫全集》PDF（内题《杜甫诗集》，钱谦益笺注、郝润华点校）整理，共 1,224 个阅读页面。每篇独立诗作各用一篇 Markdown，组诗共用一篇，包括《秋兴八首》《前出塞九首》《八哀诗》《江头五咏》等；另保留文赋、序跋、年谱及书后附录。异文小字仍在原处，编号注文与正文同页双向跳转，内嵌生僻字和世系图使用本地图片。

每个诗歌页面默认显示“只读原文”，可切换到“原文与笺注”。纯原文保留诗句、原作自序和组内分章，去掉夹注、注号及注文；组诗共用一个 Markdown 和阅读地址。直接访问注释锚点时自动切到笺注视图。纯原文视图不重复进入搜索索引，笺注版保留全文检索。

原 PDF 不纳入仓库。安装 `pymupdf` 后运行：

```powershell
python -X utf8 scripts/import-du-fu.py <PDF路径>
python -X utf8 scripts/import-du-fu.py <PDF路径> --check
$env:VITEPRESS_BASE='/tolstoy/'
$env:NODE_OPTIONS='--max-old-space-size=12288'
npm run docs:build
```

生成结果、来源页码及字节散列记录在 `scripts/du-fu-source-manifest.json`，导航由 `docs/.vitepress/library.du-fu.mjs` 提供。篇目边界、原书缺篇及注号异常的处理见 `source/du-fu/WORKFLOW.md`。普通网站构建不依赖原 PDF 或 Python。
