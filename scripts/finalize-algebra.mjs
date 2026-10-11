import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { rebuildLibraryIndex } from './rebuild-library-index.mjs'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { buildContinuousReadingSections, continuousReadingMarkdown } from './algebra-continuous-reading.mjs'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const volumeDir = path.join(rootDir, 'docs', 'library', 'volume-86')
const modulePath = path.join(rootDir, 'docs', '.vitepress', 'library.algebra.mjs')
const sourceDir = path.join(rootDir, 'source', 'algebra')
const manifestPath = path.join(rootDir, 'scripts', 'algebra-source-manifest.json')
const planPath = path.join(rootDir, 'scripts', 'algebra-reading-plan.json')
const expectedSourceHash = '64caa3209751e16dd570f84ed0c660a5ccaca7e3d5d8aa0b7226fcdc85e5ec3c'
const expectedPdfPages = 923
const bookTitle = '代数'
const fullTitle = 'Algebra — Revised Third Edition'
const reviewFlags = ['visualReviewed', 'englishTranscribed', 'chineseTranslated', 'formulaChecked']
const ancillarySections = new Set(['title-pages', 'series-list'])

function readingSections(sections) {
  return sections.filter((section) => !ancillarySections.has(section.key))
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
  return `/library/volume-86/${language === 'en' ? 'original-' : ''}${section.key}`
}

function translationStatus(progress) {
  return progress.completedPdfPageCount === expectedPdfPages && progress.publishedPdfPageCount === expectedPdfPages &&
    progress.independentReviewedPdfPageCount === expectedPdfPages
    ? 'complete' : 'ongoing'
}

function readIndependentAuditProgress() {
  const result = spawnSync('python', [path.join(rootDir, 'scripts', 'check-algebra-audits.py'), '--json'], {
    cwd: rootDir, encoding: 'utf8', maxBuffer: 4 * 1024 * 1024,
    env: { ...process.env, PYTHONIOENCODING: 'utf-8' }
  })
  if (result.error || result.status !== 0) fail(`独立审校记录验证失败：${result.error?.message ?? result.stdout ?? result.stderr}`)
  let report
  try { report = JSON.parse(result.stdout) } catch { fail('独立审校验证器没有返回有效 JSON') }
  if (report.pdfPageCount !== expectedPdfPages || !Number.isInteger(report.currentSnapshotReviewedPages) ||
      report.currentSnapshotReviewedPages < 0 || report.currentSnapshotReviewedPages > expectedPdfPages ||
      report.invalidRecords.length) fail('独立审校记录或当前稿件快照无效')
  return { independentReviewedPdfPageCount: report.currentSnapshotReviewedPages }
}

function validateSourceManifest(manifest, pdfPath) {
  if (manifest.sourceFileName !== 'Algebra.pdf' || manifest.sourceSha256 !== expectedSourceHash ||
      manifest.pdfPageCount !== expectedPdfPages || manifest.title !== 'Algebra' || manifest.author !== 'Serge Lang') {
    fail('来源清单与指定的 Algebra.pdf 不一致')
  }
  if (!Array.isArray(manifest.pages) || manifest.pages.length !== expectedPdfPages) fail('来源清单须包含全部 923 页')
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
  if (sha256(fs.readFileSync(pdfPath)) !== expectedSourceHash) fail('本地原始 PDF 的 SHA-256 与固定来源清单不一致')
}

function validatePlan(plan) {
  if (plan.sourceSha256 !== expectedSourceHash || plan.pdfPageCount !== expectedPdfPages ||
      !Array.isArray(plan.sections) || !plan.sections.length || typeof plan.inventoryNotice !== 'string') {
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
  if (nextPage !== expectedPdfPages + 1) fail('阅读计划没有完整覆盖 923 页')
}

function validateBody(body, file) {
  if (body === null) return
  if (!body.trim()) fail(`来源正文为空：${file}`)
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
  validateBody(en, enPath)
  validateBody(zh, zhPath)
  const review = fs.existsSync(reviewPath) ? parseJson(reviewPath) : null
  if (review) {
    if (review.pdfPage !== pdfPage ||
        !(review.printedPage === null || (typeof review.printedPage === 'string' && review.printedPage.trim())) ||
        reviewFlags.some((flag) => typeof review[flag] !== 'boolean') ||
        !Array.isArray(review.unresolved) || !review.unresolved.every((item) => typeof item === 'string') ||
        !Array.isArray(review.notes) || !review.notes.every((item) => typeof item === 'string')) {
      fail(`逐页核对记录格式无效：${reviewPath}`)
    }
    if ((review.englishTranscribed && !en?.trim()) || (review.chineseTranslated && !zh?.trim()) ||
        (reviewFlags.every((flag) => review[flag]) && (!en?.trim() || !zh?.trim()))) {
      fail(`逐页核对记录已标记完成，但缺少非空正文：${reviewPath}`)
    }
    if (review.sourceSha256 !== undefined && review.sourceSha256 !== expectedSourceHash) {
      fail(`逐页核对记录的来源 SHA-256 不一致：${reviewPath}`)
    }
  }
  const hasAllFiles = Boolean(en?.trim() && zh?.trim() && review)
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
    config(md) { installMathRenderer(md, { mode: 'inline' }) }
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
      const tokens = markdown.parse(state[language], {})
      const math = countMathTokens(tokens)
      if (math.dollars !== delimiters) fail(`数学公式分隔符没有全部被排版器识别：${file}`)
      mathExpressionCount += math.expressions
      const rendered = markdown.renderer.render(tokens, markdown.options, {})
      if (/data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(rendered)) {
        const message = rendered.match(/data-mjx-error="([^"]+)"/)?.[1] ?? 'MathJax merror'
        fail(`公式无法正确排版：${file}，${message}`)
      }
      for (const match of state[language].matchAll(/!\[[^\]]*\]\((\/library\/volume-86\/[^)]+)\)/g)) {
        const asset = path.resolve(rootDir, 'docs', 'public', `.${match[1]}`)
        const publicRoot = path.join(rootDir, 'docs', 'public', 'library', 'volume-86') + path.sep
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
    `description: ${JSON.stringify(`Serge Lang《Algebra》${language === 'zh' ? '中文译文' : 'English'}。`)}`,
    'pageClass: algebra-reading',
    ...(ancillarySections.has(section.key) ? ['search: false'] : []),
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
    'title: "代数"',
    'description: "Serge Lang《Algebra》中文译本。"',
    '---', '',
    '# 代数', ''
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
  const sidebar = [{ text: '代数', collapsed: true, items: [
    { text: '目录', link: '/library/volume-86/' },
    ...(contents.length ? [
      { text: '中文', collapsed: false, items: contents.map((section) => ({ text: section.title, link: route(section) })) },
      { text: 'English', collapsed: true, items: contents.map((section) => ({ text: section.englishTitle, link: route(section, 'en') })) }
    ] : [])
  ] }]
  const pageCount = published.length * 2
  const catalog = [{
    title: bookTitle, fullTitle, volumeLabel: '新增卷', author: 'Serge Lang',
    description: status === 'ongoing' ? '中文译本（逐章进行）' : '中文译本', edition: manifest.edition,
    source: '用户提供的本地扫描版 Algebra.pdf', sourceSha256: manifest.sourceSha256,
    translationStatus: status, sourcePdfPageCount: expectedPdfPages,
    ...progress, link: '/library/volume-86/', firstPage: contents.length ? route(contents[0]) : '/library/volume-86/', pageCount
  }]
  const stats = { volumeCount: 1, pageCount, characterCount: [...documents.entries()]
    .filter(([file]) => file !== 'index.md').reduce((sum, [, markdown]) => sum + countCharacters(markdown), 0) }
  return '// 此文件由 scripts/finalize-algebra.mjs 生成；完成数仅来自逐页正文与明确核对记录。\n' +
    `export const algebraLibrarySidebar = ${JSON.stringify(sidebar, null, 2)}\n\n` +
    `export const algebraLibraryCatalog = ${JSON.stringify(catalog, null, 2)}\n\n` +
    `export const algebraLibraryStats = ${JSON.stringify(stats, null, 2)}\n`
}

function validateGeneratedPages(documents, published) {
  for (const section of published) {
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
  let pdfPath = 'D:/Download/Algebra.pdf'
  const args = process.argv.slice(2)
  for (let index = 0; index < args.length; index += 1) {
    if (args[index] === '--check') checkOnly = true
    else if (args[index] === '--source-pdf' && args[index + 1]) pdfPath = path.resolve(args[++index])
    else fail(`未知参数 ${args[index]}；用法：node scripts/finalize-algebra.mjs [--source-pdf 路径] [--check]`)
  }
  const manifest = parseJson(manifestPath)
  const plan = parseJson(planPath)
  validateSourceManifest(manifest, pdfPath)
  validatePlan(plan)
  const states = Array.from({ length: expectedPdfPages }, (_, index) => readPageState(index + 1))
  const auditProgress = readIndependentAuditProgress()
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
    if (!states.slice(section.firstPdfPage - 1, section.lastPdfPage).every((state) => state.complete)) break
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
  for (const section of published) {
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
    if (readRequired(modulePath) !== module) fail('代数目录元数据或统计已过期，请重新运行 finalizer')
  } else {
    fs.mkdirSync(volumeDir, { recursive: true })
    for (const [file, markdown] of documents) {
      const target = path.join(volumeDir, file)
      if (readOptional(target) !== markdown) fs.writeFileSync(target, markdown)
    }
    if (readOptional(modulePath) !== module) fs.writeFileSync(modulePath, module)
    await rebuildLibraryIndex()
  }
  console.log(`${checkOnly ? '验证' : '整合'}完成：扫描图核对 ${progress.visualReviewedPdfPageCount}/923 页，四项完成 ${progress.completedPdfPageCount}/923 页；按章入库 ${published.length} 个部分、${progress.publishedPdfPageCount} 个来源页、${published.length * 2} 个中英文阅读页面。原始 PDF SHA-256 一致；全书译本状态为 ${translationStatus(progress)}。`)
}

main().catch((error) => {
  console.error(`《代数》整合失败：${error.message}`)
  process.exitCode = 1
})
