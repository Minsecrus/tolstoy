import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { installRepresentationTheoryFootnotes } from './representation-theory-footnotes.mjs'
import { buildContinuousReadingSections, continuousReadingMarkdown } from './representation-theory-continuous-reading.mjs'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const volumeDir = path.join(rootDir, 'docs', 'library', 'volume-88')
const modulePath = path.join(rootDir, 'docs', '.vitepress', 'library.representation-theory.mjs')
const sourceDir = path.join(rootDir, 'source', 'representation-theory')
const manifestPath = path.join(rootDir, 'scripts', 'representation-theory-source-manifest.json')
const planPath = path.join(rootDir, 'scripts', 'representation-theory-reading-plan.json')
const sourceInventory = JSON.parse(fs.readFileSync(manifestPath, 'utf8'))
const expectedSourceHash = sourceInventory.sourceSha256
const expectedPdfPages = sourceInventory.pdfPageCount
const bookAuthor = sourceInventory.author ?? sourceInventory.authors?.join(', ')
const bookTitle = '表示论导论'
const fullTitle = 'Introduction to Representation Theory'
const reviewFlags = ['visualReviewed', 'englishTranscribed', 'chineseTranslated', 'formulaChecked']
const ancillarySections = new Set(['title-pages', 'title-page', 'cover', 'copyright', 'blank', 'contents'])
const isAncillary = (section) => section.excludeFromReading === true || ancillarySections.has(section.key) || section.key.startsWith('blank-')

function readingSections(sections) {
  return sections.filter((section) => !isAncillary(section))
}

function fail(message) {
  throw new Error(message)
}

function readRequired(file) {
  if (!fs.existsSync(file)) fail(`缺少文件：${file}`)
  return fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n')
}

function readOptional(file) {
  return fs.existsSync(file) ? readRequired(file) : null
}

function parseJson(file) {
  try {
    return JSON.parse(readRequired(file))
  } catch (error) {
    fail(`${file} 不是有效 JSON：${error.message}`)
  }
}

function sha256(buffer) {
  return crypto.createHash('sha256').update(buffer).digest('hex')
}

function fileStem(pdfPage) {
  return `pdf-${String(pdfPage).padStart(4, '0')}`
}

function route(section, language = 'zh') {
  return `/library/volume-88/${language === 'en' ? 'original-' : ''}${section.key}`
}

function translationStatus(progress) {
  return progress.completedPdfPageCount === expectedPdfPages && progress.publishedPdfPageCount === expectedPdfPages &&
    progress.independentReviewedPdfPageCount === expectedPdfPages
    ? 'complete' : 'ongoing'
}

function readIndependentAuditProgress() {
  const result = spawnSync('python', [path.join(rootDir, 'scripts', 'check-representation-theory-audits.py'), '--json'], {
    cwd: rootDir, encoding: 'utf8', maxBuffer: 4 * 1024 * 1024,
    env: { ...process.env, PYTHONIOENCODING: 'utf-8' }
  })
  if (result.error || result.status !== 0) fail(`独立审校记录验证失败：${result.error?.message ?? result.stdout ?? result.stderr}`)
  let report
  try { report = JSON.parse(result.stdout) } catch { fail('独立审校验证器没有返回有效 JSON') }
  if (report.pdfPageCount !== expectedPdfPages || !Number.isInteger(report.currentSnapshotReviewedPages) ||
      report.currentSnapshotReviewedPages < 0 || report.currentSnapshotReviewedPages > expectedPdfPages ||
      report.invalidRecords.length) fail('独立审校记录或当前稿件快照无效')
  return { independentReviewedPdfPageCount: report.currentSnapshotReviewedPages, currentSnapshotPages: report.currentSnapshotPages }
}

function validateSourceManifest(manifest, pdfPath) {
  if (!/^[0-9a-f]{64}$/.test(expectedSourceHash) || !Number.isInteger(expectedPdfPages) || expectedPdfPages <= 0 ||
      manifest.sourceSha256 !== expectedSourceHash || manifest.pdfPageCount !== expectedPdfPages ||
      manifest.title !== 'Introduction to Representation Theory' ||
      typeof bookAuthor !== 'string' || !bookAuthor.trim()) {
    fail('来源清单与指定的 Introduction to Representation Theory 不一致')
  }
  if (!Array.isArray(manifest.pages) || manifest.pages.length !== expectedPdfPages) fail(`来源清单须包含全部 ${expectedPdfPages} 页`)
  for (let i = 0; i < manifest.pages.length; i += 1) {
    const page = manifest.pages[i]
    if (page.pdfPage !== i + 1 || !Number.isFinite(page.widthPt) || page.widthPt <= 0 ||
        !Number.isFinite(page.heightPt) || page.heightPt <= 0 ||
        !Number.isInteger(page.embeddedTextCharacters) || page.embeddedTextCharacters < 0 ||
        !/^[0-9a-f]{64}$/.test(page.embeddedTextSha256 ?? '')) {
      fail(`来源清单的 PDF 第 ${i + 1} 页记录无效`)
    }
  }
  if (!fs.existsSync(pdfPath)) fail(`缺少本地原始 PDF：${pdfPath}`)
  if (sha256(fs.readFileSync(pdfPath)) !== expectedSourceHash) fail('本地原始 PDF 的 SHA-256 与来源清单不一致')
}

function validatePlan(plan) {
  if (plan.sourceSha256 !== expectedSourceHash || plan.pdfPageCount !== expectedPdfPages ||
      !Array.isArray(plan.sections) || !plan.sections.length) {
    fail('阅读计划与来源清单不一致')
  }
  const seenKeys = new Set()
  const generatedFiles = new Set(['index.md'])
  let nextPage = 1
  for (const section of plan.sections) {
    if (!/^(?:[a-z][a-z0-9]*(?:-[a-z0-9]+)*)$/.test(section.key ?? '') || seenKeys.has(section.key) ||
        typeof section.title !== 'string' || !section.title.trim() ||
        typeof section.englishTitle !== 'string' || !section.englishTitle.trim() ||
        section.firstPdfPage !== nextPage || !Number.isInteger(section.lastPdfPage) ||
        section.lastPdfPage < section.firstPdfPage || section.lastPdfPage > expectedPdfPages) {
      fail(`阅读计划存在重复、缺页或无效分组：${section.key ?? '无 key'}`)
    }
    seenKeys.add(section.key)
    for (const file of [`${section.key}.md`, `original-${section.key}.md`]) {
      if (generatedFiles.has(file)) fail(`阅读计划产生重复文件名：${file}`)
      generatedFiles.add(file)
    }
    nextPage = section.lastPdfPage + 1
  }
  if (nextPage !== expectedPdfPages + 1) fail(`阅读计划没有完整覆盖 ${expectedPdfPages} 页`)
}

function validateBody(body, file, allowEmpty = false) {
  if (body === null) return
  if (!body.trim() && !allowEmpty) fail(`来源正文为空：${file}`)
  if (/^---\n/.test(body)) fail(`逐页来源正文不得包含 frontmatter：${file}`)
  if (/\bid=["']pdf-page-\d+["']/.test(body)) fail(`逐页来源正文不得预置页锚点：${file}`)
  if (/\bTODO\b|\[待翻译\]|\[待核对\]|\[此处省略\]/i.test(body)) fail(`逐页来源正文存在未解决占位内容：${file}`)
}

function readPageState(pdfPage) {
  const stem = fileStem(pdfPage)
  const enPath = path.join(sourceDir, 'en', `${stem}.md`)
  const zhPath = path.join(sourceDir, 'zh', `${stem}.md`)
  const reviewPath = path.join(sourceDir, 'review', `${stem}.json`)
  const en = readOptional(enPath)
  const zh = readOptional(zhPath)
  const blankPage = sourceInventory.pages[pdfPage - 1].pageType === 'blank'
  validateBody(en, enPath, blankPage)
  validateBody(zh, zhPath, blankPage)
  const review = fs.existsSync(reviewPath) ? parseJson(reviewPath) : null
  if (review) {
    if (review.pdfPage !== pdfPage ||
        !(review.printedPage === null || (typeof review.printedPage === 'string' && review.printedPage.trim()) || Number.isInteger(review.printedPage)) ||
        reviewFlags.some((flag) => typeof review[flag] !== 'boolean') ||
        !Array.isArray(review.unresolved) || !review.unresolved.every((item) => typeof item === 'string') ||
        !Array.isArray(review.notes) || !review.notes.every((item) => typeof item === 'string')) {
      fail(`逐页核对记录格式无效：${reviewPath}`)
    }
    const printedLabel = (value) => value === null ? null : String(value)
    if (printedLabel(review.printedPage) !== printedLabel(sourceInventory.pages[pdfPage - 1].printedPage)) {
      fail(`逐页核对记录的原书页码与视觉核实清单不一致：${reviewPath}`)
    }
    if (blankPage && review.blankPage !== true) fail(`空白页须有明确的视觉核对标记：${reviewPath}`)
    if (!blankPage && ((review.englishTranscribed && !en?.trim()) || (review.chineseTranslated && !zh?.trim()) ||
        (reviewFlags.every((flag) => review[flag]) && (!en?.trim() || !zh?.trim())))) {
      fail(`逐页核对记录已标记完成，但缺少非空正文：${reviewPath}`)
    }
    if (typeof review.sourceSha256 === 'string' && review.sourceSha256 !== expectedSourceHash) {
      fail(`逐页核对记录的来源 SHA-256 不一致：${reviewPath}`)
    }
    const currentHashes = { en: en === null ? null : sha256(fs.readFileSync(enPath)), zh: zh === null ? null : sha256(fs.readFileSync(zhPath)) }
    const checkHash = (language, hash, field) => {
      if (typeof hash !== 'string' || !/^[0-9a-f]{64}$/.test(hash) || hash !== currentHashes[language]) {
        fail(`逐页核对记录的当前 ${language} 稿件快照不一致：${reviewPath}，${field}`)
      }
    }
    for (const field of ['sourceSha256', 'markdownSha256', 'sourceHashes', 'sha256']) {
      const hashes = review[field]
      if (hashes === undefined || (field === 'sourceSha256' && typeof hashes === 'string')) continue
      if (!hashes || typeof hashes !== 'object' || Array.isArray(hashes)) fail(`逐页稿件快照须为 en/zh 对象：${reviewPath}，${field}`)
      for (const language of ['en', 'zh']) if (hashes[language] !== undefined) checkHash(language, hashes[language], `${field}.${language}`)
    }
    for (const [language, fields] of Object.entries({ en: ['enSha256', 'englishSha256'], zh: ['zhSha256', 'chineseSha256'] })) {
      for (const field of fields) if (review[field] !== undefined) checkHash(language, review[field], field)
    }
    if (reviewFlags.every((flag) => review[flag]) && review.unresolved.length === 0) {
      for (const language of ['en', 'zh']) {
        const bound = review[`${language}Sha256`] ?? review.sourceSha256?.[language] ??
          review.markdownSha256?.[language] ?? review.sourceHashes?.[language]
        checkHash(language, bound, `${language} completed-review binding`)
      }
    }
    const diagrams = review.diagrams ?? []
    if (!Array.isArray(diagrams)) fail(`图示记录须为数组：${reviewPath}`)
    const imageUrls = (body) => [...(body ?? '').matchAll(/!\[[^\]]*\]\((\/library\/volume-88\/diagrams\/[^)]+)\)/g)].map((match) => match[1])
    const englishImages = imageUrls(en), chineseImages = imageUrls(zh)
    if (JSON.stringify(englishImages) !== JSON.stringify(chineseImages)) fail(`中英文图示次序不一致：${reviewPath}`)
    const recorded = new Set()
    for (const diagram of diagrams) {
      if (typeof diagram.path !== 'string' || !diagram.path.startsWith('/library/volume-88/diagrams/') ||
          !Number.isFinite(diagram.widthPt) || diagram.widthPt <= 0 ||
          !Array.isArray(diagram.clipPt) || diagram.clipPt.length !== 4 || !diagram.clipPt.every(Number.isFinite) ||
          Math.abs(diagram.clipPt[2] - diagram.clipPt[0] - diagram.widthPt) > 0.02 ||
          !/^[0-9a-f]{64}$/.test(diagram.sha256 ?? '')) fail(`原图裁片物理尺寸或快照无效：${reviewPath}`)
      const asset = path.resolve(rootDir, 'docs', 'public', `.${diagram.path}`)
      const publicRoot = path.join(rootDir, 'docs', 'public', 'library', 'volume-88', 'diagrams') + path.sep
      if (!asset.startsWith(publicRoot) || !fs.existsSync(asset) || sha256(fs.readFileSync(asset)) !== diagram.sha256) {
        fail(`原图裁片缺失或已变更：${reviewPath}，${diagram.path}`)
      }
      recorded.add(diagram.path)
    }
    if (englishImages.some((url) => !recorded.has(url))) fail(`正文图示没有已核实的裁片尺寸：${reviewPath}`)
  }
  const hasAllFiles = Boolean(review && en !== null && zh !== null && (blankPage || (en.trim() && zh.trim())))
  const complete = hasAllFiles && reviewFlags.every((flag) => review[flag] === true) && review.unresolved.length === 0
  return { pdfPage, en, zh, review, hasAllFiles, complete }
}

function countCharacters(markdown) {
  const text = markdown.replace(/^---\n[\s\S]*?\n---\n/, '')
    .replace(/<[^>]*>/g, '').replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[\s#*_`>|]/g, '')
  return [...text].length
}

async function validateRenderedMath(states) {
  const markdown = await createMarkdownRenderer(path.join(rootDir, 'docs'), {
    math: true, typographer: true,
    config(md) {
      installMathRenderer(md, { mode: 'inline' })
      installRepresentationTheoryFootnotes(md)
    }
  })
  let mathExpressionCount = 0
  const countMathTokens = (tokens) => tokens.reduce((sum, token) => {
    if (token.type === 'math_inline') return { expressions: sum.expressions + 1, dollars: sum.dollars + 2 }
    if (token.type === 'math_block') return { expressions: sum.expressions + 1, dollars: sum.dollars + 4 }
    const children = token.children ? countMathTokens(token.children) : { expressions: 0, dollars: 0 }
    return { expressions: sum.expressions + children.expressions, dollars: sum.dollars + children.dollars }
  }, { expressions: 0, dollars: 0 })
  const countDelimiters = (source, file) => {
    const prose = source.replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm, '').replace(/`[^`\n]*`/g, '')
    let open = null
    let dollars = 0
    for (let position = 0; position < prose.length; position += 1) {
      if (prose[position] !== '$') continue
      let backslashes = 0
      for (let previous = position - 1; previous >= 0 && prose[previous] === '\\'; previous -= 1) backslashes += 1
      if (backslashes % 2) continue
      const delimiter = prose[position + 1] === '$' ? '$$' : '$'
      dollars += delimiter.length
      if (open && open !== delimiter) fail(`数学公式分隔符交错：${file}`)
      open = open ? null : delimiter
      position += delimiter.length - 1
    }
    if (open) fail(`数学公式分隔符未闭合：${file}，${open}`)
    return dollars
  }
  for (const state of states.filter((item) => item.complete)) {
    for (const language of ['en', 'zh']) {
      const file = `${language}/${fileStem(state.pdfPage)}.md`
      const delimiters = countDelimiters(state[language], file)
      const env = { relativePath: `library/volume-88/${file}` }
      const tokens = markdown.parse(state[language], env)
      const math = countMathTokens(tokens)
      if (math.dollars !== delimiters) fail(`数学公式分隔符没有全部被排版器识别：${file}`)
      mathExpressionCount += math.expressions
      const rendered = markdown.renderer.render(tokens, markdown.options, env)
      if (/data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(rendered)) {
        const message = rendered.match(/data-mjx-error="([^"]+)"/)?.[1] ?? 'MathJax merror'
        fail(`公式无法正确排版：${file}，${message}`)
      }
      for (const match of state[language].matchAll(/!\[[^\]]*\]\((\/library\/volume-88\/[^)]+)\)/g)) {
        const asset = path.resolve(rootDir, 'docs', 'public', `.${match[1]}`)
        const publicRoot = path.join(rootDir, 'docs', 'public', 'library', 'volume-88') + path.sep
        if (!asset.startsWith(publicRoot) || !fs.existsSync(asset)) fail(`缺少来源页图示：${file}，${match[1]}`)
      }
    }
  }
  return { renderedMathCheckedPdfPageCount: states.filter((state) => state.complete).length, mathExpressionCount }
}

function makeReadingDocument(section, language, continuousSection, published) {
  const title = language === 'zh' ? section.title : section.englishTitle
  const sameLanguageSections = readingSections(published)
  const position = sameLanguageSections.findIndex((item) => item.key === section.key)
  const previous = position < 0 ? undefined : sameLanguageSections[position - 1]
  const next = position < 0 ? undefined : sameLanguageSections[position + 1]
  const lines = [
    '---',
    `title: ${JSON.stringify(title)}`,
    `description: ${JSON.stringify(`《Introduction to Representation Theory》${language === 'zh' ? '中文译文' : 'English'}。`)}`,
    'pageClass: algebra-reading representation-theory-reading',
    ...(isAncillary(section) ? ['search: false'] : []),
    `prev: ${previous ? JSON.stringify({ text: language === 'zh' ? previous.title : previous.englishTitle, link: route(previous, language) }) : 'false'}`,
    `next: ${next ? JSON.stringify({ text: language === 'zh' ? next.title : next.englishTitle, link: route(next, language) }) : 'false'}`,
    '---', '',
    `# ${title}`, '',
  ]
  lines.push(continuousReadingMarkdown(continuousSection.pages, { pageAnchors: true }), '')
  return lines.join('\n')
}

function makeHome(published) {
  const contents = readingSections(published)
  const first = contents[0]
  const lines = [
    '---',
    'title: "表示论导论"',
    'description: "《Introduction to Representation Theory》中文译本。"',
    '---', '',
    '# 表示论导论', ''
  ]
  if (first) lines.push(`[开始阅读](${route(first)})`, '')
  lines.push('## 目录', '')
  for (const section of contents) lines.push(`- [${section.title}](${route(section)})`)
  lines.push('')
  return lines.join('\n')
}

function makeModule(manifest, published, documents, progress) {
  const status = translationStatus(progress)
  const contents = readingSections(published)
  const sidebar = [{ text: '表示论导论', collapsed: true, items: [
    { text: '目录', link: '/library/volume-88/' },
    ...(contents.length ? [
      { text: '中文', collapsed: false, items: contents.map((section) => ({ text: section.title, link: route(section) })) },
      { text: 'English', collapsed: true, items: contents.map((section) => ({ text: section.englishTitle, link: route(section, 'en') })) }
    ] : [])
  ] }]
  const pageCount = contents.length * 2
  const catalog = [{
    title: bookTitle, fullTitle, volumeLabel: '新增卷', author: bookAuthor,
    description: status === 'ongoing' ? '中文译本（逐章进行）' : '中文译本', edition: manifest.edition,
    source: '用户提供的含 OCR 文字层扫描 PDF', sourceSha256: manifest.sourceSha256,
    translationStatus: status, sourcePdfPageCount: expectedPdfPages,
    ...progress, link: '/library/volume-88/', firstPage: contents.length ? route(contents[0]) : '/library/volume-88/', pageCount
  }]
  const stats = { volumeCount: 1, pageCount, characterCount: [...documents.entries()]
    .filter(([file]) => file !== 'index.md').reduce((sum, [, markdown]) => sum + countCharacters(markdown), 0) }
  return '// 此文件由 scripts/finalize-representation-theory.mjs 生成；完成数仅来自逐页正文与明确核对记录。\n' +
    `export const representationTheoryLibrarySidebar = ${JSON.stringify(sidebar, null, 2)}\n\n` +
    `export const representationTheoryLibraryCatalog = ${JSON.stringify(catalog, null, 2)}\n\n` +
    `export const representationTheoryLibraryStats = ${JSON.stringify(stats, null, 2)}\n`
}

function validateGeneratedPages(documents, published) {
  for (const section of readingSections(published)) {
    const expected = Array.from({ length: section.lastPdfPage - section.firstPdfPage + 1 }, (_, index) => section.firstPdfPage + index)
    for (const language of ['zh', 'en']) {
      const file = `${language === 'en' ? 'original-' : ''}${section.key}.md`
      const markdown = documents.get(file)
      const actual = [...markdown.matchAll(/\bid="pdf-page-(\d+)"/g)].map((match) => Number(match[1]))
      if (JSON.stringify(actual) !== JSON.stringify(expected)) fail(`${file} 的逐页锚点与来源页序不一致`)
      const ids = [...markdown.matchAll(/\bid="([^"\s]+)"/g)].map((match) => match[1])
      if (new Set(ids).size !== ids.length) fail(`${file} 有重复 HTML 锚点`)
    }
  }
}

async function main() {
  let checkOnly = false
  let checkSourcesOnly = false
  let initializeOnly = false
  let pdfPath = sourceInventory.sourcePath ?? 'C:/Users/29728/Downloads/Introduction to Representation Theory (Pavel Etingof et al.) (z-library.sk, 1lib.sk, z-lib.sk).pdf'
  const args = process.argv.slice(2)
  for (let index = 0; index < args.length; index += 1) {
    if (args[index] === '--check') checkOnly = true
    else if (args[index] === '--check-sources') checkSourcesOnly = true
    else if (args[index] === '--initialize') initializeOnly = true
    else if (args[index] === '--source-pdf' && args[index + 1]) pdfPath = path.resolve(args[++index])
    else fail(`未知参数 ${args[index]}；用法：node scripts/finalize-representation-theory.mjs [--source-pdf 路径] [--check]`)
  }
  const manifest = parseJson(manifestPath)
  const plan = parseJson(planPath)
  validateSourceManifest(manifest, pdfPath)
  validatePlan(plan)
  if (initializeOnly) {
    const progress = {
      visualReviewedPdfPageCount: 0, translatedPdfPageCount: 0, formulaCheckedPdfPageCount: 0,
      completedPdfPageCount: 0, publishedPdfPageCount: 0, independentReviewedPdfPageCount: 0,
      renderedMathCheckedPdfPageCount: 0, mathExpressionCount: 0
    }
    const documents = new Map([['index.md', makeHome([])]])
    const module = makeModule(manifest, [], documents, progress)
    for (const [file, content] of [[modulePath, module], [path.join(volumeDir, 'index.md'), documents.get('index.md')]]) {
      const existing = readOptional(file)
      if (existing !== null && existing !== content) fail('不能以空目录覆盖已有阅读进度，请使用正常 finalizer')
      fs.mkdirSync(path.dirname(file), { recursive: true })
      fs.writeFileSync(file, content)
    }
    console.log('已初始化书目录模块；未发布逐页译文，也未声明主译或独立审校进度。')
    return
  }
  const states = Array.from({ length: expectedPdfPages }, (_, index) => readPageState(index + 1))
  if (checkSourcesOnly) {
    console.log(`逐页文件检查通过：${states.filter((state) => state.complete).length}/${expectedPdfPages} 页；来源 PDF、原书页码、现稿 SHA 及中英文原图裁片均一致。此命令不代替独立内容审校，不发布网站。`)
    return
  }
  const auditResult = readIndependentAuditProgress()
  const auditedPages = new Set(auditResult.currentSnapshotPages)
  const auditProgress = { independentReviewedPdfPageCount: auditResult.independentReviewedPdfPageCount }
  const mathProgress = await validateRenderedMath(states)
  const progress = {
    visualReviewedPdfPageCount: states.filter((state) => state.hasAllFiles && state.review.visualReviewed).length,
    translatedPdfPageCount: states.filter((state) => state.hasAllFiles && state.review.chineseTranslated).length,
    formulaCheckedPdfPageCount: states.filter((state) => state.hasAllFiles && state.review.formulaChecked).length,
    completedPdfPageCount: states.filter((state) => state.complete).length,
    publishedPdfPageCount: 0,
    ...auditProgress,
    ...mathProgress
  }
  const published = []
  for (const section of plan.sections) {
    if (!states.slice(section.firstPdfPage - 1, section.lastPdfPage).every((state) => state.complete && auditedPages.has(state.pdfPage))) break
    published.push(section)
    progress.publishedPdfPageCount += section.lastPdfPage - section.firstPdfPage + 1
  }
  const documents = new Map()
  const continuous = {}
  for (const language of ['zh', 'en']) {
    continuous[language] = new Map((await buildContinuousReadingSections({
      sections: published, states, language, rootDir
    })).map((section) => [section.key, section]))
  }
  for (const section of readingSections(published)) {
    documents.set(`${section.key}.md`, makeReadingDocument(section, 'zh', continuous.zh.get(section.key), published))
    documents.set(`original-${section.key}.md`, makeReadingDocument(section, 'en', continuous.en.get(section.key), published))
  }
  documents.set('index.md', makeHome(published))
  validateGeneratedPages(documents, published)
  const module = makeModule(manifest, published, documents, progress)
  const plannedFiles = new Set(plan.sections.flatMap((section) => [`${section.key}.md`, `original-${section.key}.md`]))
  if (fs.existsSync(volumeDir)) {
    const stale = fs.readdirSync(volumeDir).filter((file) => plannedFiles.has(file) && !documents.has(file))
    if (stale.length) fail(`发现不再满足整章核对条件的已入库页面，须先解决核对记录：${stale.join(', ')}`)
  }
  if (checkOnly) {
    for (const [file, markdown] of documents) {
      if (readRequired(path.join(volumeDir, file)) !== markdown) fail(`${file} 与当前逐页正文和核对记录不一致，请重新运行 finalizer`)
    }
    if (readRequired(modulePath) !== module) fail('表示论导论目录元数据或统计已过期，请重新运行 finalizer')
  } else {
    fs.mkdirSync(volumeDir, { recursive: true })
    for (const [file, markdown] of documents) {
      const target = path.join(volumeDir, file)
      if (readOptional(target) !== markdown) fs.writeFileSync(target, markdown)
    }
    if (readOptional(modulePath) !== module) fs.writeFileSync(modulePath, module)
  }
  const visibleSections = readingSections(published)
  const visibleSourcePages = visibleSections.reduce((sum,section) => sum + section.lastPdfPage - section.firstPdfPage + 1, 0)
  console.log(`${checkOnly ? '验证' : '整合'}完成：原始页面核对 ${progress.visualReviewedPdfPageCount}/${expectedPdfPages} 页，四项完成 ${progress.completedPdfPageCount}/${expectedPdfPages} 页；按章入库 ${visibleSections.length} 个部分、${visibleSourcePages} 个来源页、${visibleSections.length * 2} 个中英文阅读页面。原始 PDF SHA-256 一致；全书译本状态为 ${translationStatus(progress)}。`)
}

main().catch((error) => {
  console.error(`《表示论导论》整合失败：${error.message}`)
  process.exitCode = 1
})
