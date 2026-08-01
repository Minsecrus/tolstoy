import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const scriptDir = path.dirname(fileURLToPath(import.meta.url))
const rootDir = path.resolve(scriptDir, '..')
const sourcePath = process.argv[2]

if (!sourcePath) {
  throw new Error('用法：node scripts/import-world-classics.mjs <合集TXT路径>')
}

const books = [
  ['罪与罚', 542],
  ['白痴', 10099],
  ['群魔', 20640],
  ['卡拉马佐夫兄弟', 34402],
  ['被侮辱与被损害的', 46463],
  ['少年', 52738],
  ['地下室手记：陀思妥耶夫斯基中篇小说选', 62345],
  ['吉檀迦利：泰戈尔诗选', 69719],
  ['饥饿的石头：泰戈尔中短篇小说选', 101322],
  ['沉船', 110698],
  ['纠缠', 116816],
  ['生活的回忆：泰戈尔散文选', 121903],
  ['花钏女：泰戈尔戏剧选', 128280],
  ['套中人：契诃夫短篇小说选', 146476],
  ['樱桃园：契诃夫戏剧选', 152156],
  ['欧也妮·葛朗台', 161716],
  ['高老头', 164772],
  ['贝姨', 169010],
  ['邦斯舅舅', 178476],
  ['农民', 183382],
  ['三十岁的女人', 188032],
  ['幽谷百合', 192753],
  ['夏倍上校：巴尔扎克中短篇小说选', 193814],
  ['还乡', 198396],
  ['无名的裘德', 206700],
  ['卡斯特桥市长', 214929],
  ['苔丝', 220622],
  ['西波利村探险记：哈代中短篇小说选', 227926],
  ['浮士德', 231844],
  ['漫游者的夜歌', 264416],
  ['歌德谈话录', 276807],
  ['少年维特之烦恼', 285156],
  ['亲和力', 286767],
  ['背德者', 289531],
  ['伪币制造者', 294224],
  ['梵蒂冈的地窖', 300369],
  ['人间食粮', 306669],
  ['如果种子不死', 310593],
  ['刚果之行', 313512],
  ['奥勃洛莫夫', 317190],
  ['彼得堡之恋', 330597],
  ['悬崖', 338756],
  ['当代英雄', 360694],
  ['我要生活！我要悲哀……：莱蒙托夫诗选', 363865],
  ['卡尔曼情变断魂录：梅里美中短篇小说选', 372391],
  ['高龙芭智导复仇局', 375149],
  ['雅克团', 378021],
  ['查理第九时代轶事', 383392]
]

const fallbackAuthors = [
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【俄】陀思妥耶夫斯基',
  '【印度】泰戈尔',
  '【印度】泰戈尔',
  '【印度】泰戈尔',
  '【印度】泰戈尔',
  '【印度】泰戈尔',
  '【印度】泰戈尔',
  '【俄】契诃夫',
  '【俄】契诃夫',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【法】巴尔扎克',
  '【英】哈代',
  '【英】哈代',
  '【英】哈代',
  '【英】哈代',
  '【英】哈代',
  '【德】歌德',
  '【德】歌德',
  '【德】歌德',
  '【德】歌德',
  '【德】歌德',
  '【法】安德烈·纪德',
  '【法】安德烈·纪德',
  '【法】安德烈·纪德',
  '【法】安德烈·纪德',
  '【法】安德烈·纪德',
  '【法】安德烈·纪德',
  '【俄】冈察洛夫',
  '【俄】冈察洛夫',
  '【俄】冈察洛夫',
  '【俄】莱蒙托夫',
  '【俄】莱蒙托夫',
  '【法】梅里美',
  '【法】梅里美',
  '【法】梅里美',
  '【法】梅里美',
  '【法】梅里美'
]

const normalizeText = (value) => value
  .replaceAll('\u0000', '')
  .replaceAll('\u000c', '')
  .replace(/\r/g, '')
  .replace(/^\uFEFF/, '')

const source = normalizeText(fs.readFileSync(sourcePath, 'utf8'))
const lines = source.split('\n')
const copyrightMarkers = []
for (let index = 0; index < lines.length; index += 1) {
  if (lines[index].trim() === '版权信息') copyrightMarkers.push(index)
}

if (copyrightMarkers.length !== books.length * 2) {
  throw new Error(`版权信息标记数量异常：期望 ${books.length * 2}，实际 ${copyrightMarkers.length}`)
}

const normalizeMetaValue = (value) => value
  .replace(/^\s*[：:]\s*/, '')
  .replace(/\s+/g, ' ')
  .replace(/^[（(]([^（）()]+)[）)]/, '【$1】')
  .replace(/^\[([^\]]+)\]/, '【$1】')
  .replaceAll('〔', '【')
  .replaceAll('〕', '】')
  .replace(/\s*(?:著者|作者)\s*$/, '')
  .replace(/\s+著\s*$/, '')
  .trim()

function readMetadata(segmentLines, bookIndex) {
  let author = ''
  let translator = ''
  for (const line of segmentLines) {
    const trimmed = line.trim()
    const authorMatch = trimmed.match(/^(?:著者|作者)\s*[：:](.+)$/)
    const translatorMatch = trimmed.match(/^译者\s*[：:](.+)$/)
    if (authorMatch && !author) author = normalizeMetaValue(authorMatch[1])
    if (translatorMatch && !translator) translator = normalizeMetaValue(translatorMatch[1])
  }

  if (author.includes('译')) {
    const authorPart = author.split(/\s*(?:著|译)\s*/)[0].trim()
    const translatorPart = author.match(/\s+([^\s]+)\s*译\s*$/)
    author = authorPart
    if (!translator && translatorPart) translator = translatorPart[1]
  }

  return {
    author: author || fallbackAuthors[bookIndex],
    translator
  }
}

const noteDefinitionPattern = /^\s*[\[［]\s*(\d+)\s*[\]］]/
const metadataLinePattern = /^(?:书名|著者|作者|译者|总策划|策划|责任编辑|特约编辑|装帧设计|监制)\s*[：:]/
const translatorOnlyPattern = /^(?:.{0,40})(?:译|译者|校注|编选|编译|整理)\s*$/

function findBodyEnd(bodyStart, segmentEnd) {
  const tailHeadings = new Set([
    '世界名著名译文库',
    '“世界名著名译文库”总序',
    '附录',
    '注释',
    '译注',
    '译后记',
    '译者后记',
    '编后记',
    '后记',
    '生平及创作年表',
    '生平年表'
  ])
  const isTailHeading = (line) => {
    const trimmed = line.trim()
    if (tailHeadings.has(trimmed)) return true
    return /^(?:附录|注释|译注|译后记|译者后记|编后记|后记|生平及创作年表|生平年表)(?:\s|　|$)/.test(trimmed)
  }
  let end = segmentEnd
  for (let index = bodyStart; index < segmentEnd; index += 1) {
    if (isTailHeading(lines[index])) {
      end = Math.min(end, index)
      break
    }
  }

  for (let index = bodyStart; index < end; index += 1) {
    if (!noteDefinitionPattern.test(lines[index])) continue
    let definitions = 0
    for (let probe = index; probe < Math.min(end, index + 16); probe += 1) {
      if (noteDefinitionPattern.test(lines[probe])) definitions += 1
    }
    if (definitions >= 3) {
      end = index
      break
    }
  }
  return end
}

function cleanBody(rawLines, bodyStart, bodyEnd, noteScanEnd) {
  const noteIds = new Set()
  for (let index = bodyStart; index < noteScanEnd; index += 1) {
    const match = lines[index].match(noteDefinitionPattern)
    if (match) noteIds.add(match[1])
  }

  let bodyLines = rawLines
    .slice(bodyStart, bodyEnd)
    .map((line) => line.trimEnd())

  while (bodyLines.length && !bodyLines[0].trim()) bodyLines.shift()
  while (bodyLines.length && !bodyLines.at(-1).trim()) bodyLines.pop()

  while (bodyLines.length && (metadataLinePattern.test(bodyLines[0].trim()) || translatorOnlyPattern.test(bodyLines[0].trim()))) {
    bodyLines.shift()
    while (bodyLines.length && !bodyLines[0].trim()) bodyLines.shift()
  }

  let nonEmptySeen = 0
  bodyLines = bodyLines.filter((line) => {
    if (!line.trim()) return true
    nonEmptySeen += 1
    if (nonEmptySeen <= 4 && (metadataLinePattern.test(line.trim()) || translatorOnlyPattern.test(line.trim()))) return false
    return !noteDefinitionPattern.test(line)
  })

  const notePattern = [...noteIds]
    .sort((left, right) => right.length - left.length)
    .map((id) => id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
    .join('|')
  if (notePattern) {
    const inlineReference = new RegExp(
      `(?<=[一-龥A-Za-z）】”’])(?:${notePattern})(?=[一-龥，。；：、！？…\\s“”"’）】]|$)`,
      'gu'
    )
    const latinReference = new RegExp(`(^|[\\s（(])(?:${notePattern})(?=\\s+[A-Za-z])`, 'gu')
    bodyLines = bodyLines.map((line) => line.replace(inlineReference, '').replace(latinReference, '$1'))
  }
  bodyLines = bodyLines.map((line) => line.replace(/[\[［]\s*\d+\s*[\]］]/g, ''))
  bodyLines = bodyLines.map((line) => line.trimEnd())

  const normalized = []
  let blankCount = 0
  for (const line of bodyLines) {
    if (line.trim()) {
      normalized.push(line)
      blankCount = 0
    } else if (blankCount < 1) {
      normalized.push('')
      blankCount += 1
    }
  }
  while (normalized.length && !normalized[0].trim()) normalized.shift()
  while (normalized.length && !normalized.at(-1).trim()) normalized.pop()
  return normalized
}

const headingPattern = /^(?:第[一二三四五六七八九十百千万0-9]+(?:部|卷|章|幕|场|篇|辑|节)(?:\s|　|$)|[0-9]{1,3}$|[一二三四五六七八九十百千万]+$|上卷$|下卷$|序诗$|序言$|献词$|前言$|引言$|尾声$|终场$|人物$|抒情诗$|叙事诗$|故事诗集$|戏剧$|散文$)/

function isHeading(block) {
  if (block.includes('\n')) return false
  const text = block.trim()
  if (!text || text.length > 80) return false
  if (headingPattern.test(text)) return true
  return /^(?:第一部|第二部|第三部|第四部|第五部|第一卷|第二卷|第三卷|第四卷|第五卷|第一辑|第二辑|第三辑|第四辑|第五辑)\b/.test(text)
}

function splitPages(bodyLines) {
  const blocks = []
  let current = []
  for (const line of bodyLines) {
    if (!line.trim()) {
      if (current.length) {
        blocks.push(current.join('\n'))
        current = []
      }
    } else {
      current.push(line)
    }
  }
  if (current.length) blocks.push(current.join('\n'))

  const pages = []
  let pageBlocks = []
  let pageChars = 0
  const flush = () => {
    if (!pageBlocks.length) return
    pages.push(pageBlocks)
    pageBlocks = []
    pageChars = 0
  }

  for (const block of blocks) {
    const heading = isHeading(block)
    const headingBreak = heading && pageChars >= 5000
    const hardBreak = pageChars >= 12000
    if ((headingBreak || hardBreak) && pageBlocks.length) flush()
    pageBlocks.push(block)
    pageChars += block.replace(/\s/g, '').length
  }
  flush()

  return pages.map((pageBlocks, index) => {
    const firstBlock = pageBlocks[0]
    const title = isHeading(firstBlock) ? firstBlock.trim() : `正文 ${String(index + 1).padStart(2, '0')}`
    const contentBlocks = isHeading(firstBlock) ? pageBlocks.slice(1) : pageBlocks
    return {
      title,
      content: contentBlocks.join('\n\n').trim()
    }
  })
}

function escapeMarkdownLine(line) {
  if (/^\s*#{1,6}\s/.test(line)) return line.replace(/^\s*(#{1,6})\s/, '$1\\ ')
  if (/^\s*[>*+]\s/.test(line)) return line.replace(/^\s*([>*+])\s/, '$1\\ ')
  if (/^\s*-\s/.test(line)) return line.replace(/^\s*-\s/, '\\- ')
  return line
}

function renderPage(book, volumeNo, page, pageNo) {
  const body = page.content
    .split('\n')
    .map(escapeMarkdownLine)
    .join('\n')
    .trim()
  const fallback = body ? body : '（本页正文为空）'
  return `---\ntitle: ${JSON.stringify(page.title)}\ndescription: ${JSON.stringify(`${book.title} · ${page.title}`)}\n---\n\n<p class="reading-meta"><a href="/library/volume-${String(volumeNo).padStart(2, '0')}/">${book.title}</a></p>\n\n# ${page.title}\n\n${fallback}\n`
}

function renderIndex(book, volumeNo, pages) {
  const volumePath = `/library/volume-${String(volumeNo).padStart(2, '0')}/`
  const items = pages
    .map((page, index) => `- [${page.title}](${volumePath}chapter-${String(index + 1).padStart(3, '0')})`)
    .join('\n')
  return `---\ntitle: ${JSON.stringify(book.title)}\ndescription: ${JSON.stringify(`${book.title}正文`)}\n---\n\n# ${book.title}\n\n[开始阅读 →](${volumePath}chapter-001)\n\n## 目录\n\n${items}\n`
}

function makeSidebarItem(book, volumeNo, pages) {
  const volumePath = `/library/volume-${String(volumeNo).padStart(2, '0')}/`
  return {
    text: book.title,
    collapsed: true,
    items: [
      { text: '本卷首页', link: volumePath },
      {
        text: '正文',
        collapsed: false,
        items: pages.map((page, index) => ({
          text: page.title,
          link: `${volumePath}chapter-${String(index + 1).padStart(3, '0')}`
        }))
      }
    ]
  }
}

const generatedPath = path.join(rootDir, 'docs', '.vitepress', 'library.generated.mjs')
const existing = await import(`${pathToFileURL(generatedPath).href}?import=${Date.now()}`)
// 本站原有 34 卷；导入脚本可能被重复试跑，因此只取原有卷，避免新增卷重复登记。
const existingSidebar = existing.librarySidebar.slice(0, 34)
const existingCatalog = existing.libraryCatalog.slice(0, 34)
const oldStats = {
  volumeCount: 34,
  pageCount: 2276,
  characterCount: 9359569,
  noteCount: 1472,
  noteReferenceCount: 1454,
  orphanNoteCount: 18
}
const newSidebar = []
const newCatalog = []
let newCharacterCount = 0

for (let index = 0; index < books.length; index += 1) {
  const [title, bodyStartLine] = books[index]
  const segmentStart = copyrightMarkers[index * 2]
  const segmentEnd = copyrightMarkers[index * 2 + 2] ?? lines.length
  const bodyStart = bodyStartLine - 1
  if (bodyStart < segmentStart || bodyStart >= segmentEnd) {
    throw new Error(`${title} 正文起点越过本书边界：${bodyStartLine}`)
  }

  const bodyEnd = findBodyEnd(bodyStart, segmentEnd)
  const bodyLines = cleanBody(lines, bodyStart, bodyEnd, segmentEnd)
  const pages = splitPages(bodyLines)
  if (!pages.length) throw new Error(`${title} 没有生成正文页面`)

  const volumeNo = 35 + index
  const volumeDir = path.join(rootDir, 'docs', 'library', `volume-${String(volumeNo).padStart(2, '0')}`)
  fs.mkdirSync(volumeDir, { recursive: true })
  for (const entry of fs.readdirSync(volumeDir)) {
    if (/^chapter-\d+\.md$/.test(entry)) fs.rmSync(path.join(volumeDir, entry))
  }
  fs.writeFileSync(path.join(volumeDir, 'index.md'), renderIndex({ title }, volumeNo, pages))
  for (let pageIndex = 0; pageIndex < pages.length; pageIndex += 1) {
    fs.writeFileSync(
      path.join(volumeDir, `chapter-${String(pageIndex + 1).padStart(3, '0')}.md`),
      renderPage({ title }, volumeNo, pages[pageIndex], pageIndex + 1)
    )
  }

  const metadata = readMetadata(lines.slice(segmentStart, bodyStart), index)
  const volumePath = `/library/volume-${String(volumeNo).padStart(2, '0')}/`
  newSidebar.push(makeSidebarItem({ title }, volumeNo, pages))
  newCatalog.push({
    title,
    fullTitle: `世界名著名译文库 · 第${volumeNo}卷：${title}`,
    volumeLabel: '新增卷',
    author: metadata.author,
    translator: metadata.translator,
    isbn: '',
    link: volumePath,
    firstPage: `${volumePath}chapter-001`,
    pageCount: pages.length
  })
  newCharacterCount += bodyLines.join('').replace(/\s/g, '').length
  console.log(`第${volumeNo}卷 ${title}：${pages.length} 页，正文 ${bodyLines.join('').replace(/\s/g, '').length.toLocaleString('zh-CN')} 字符`)
}

const sidebar = [...existingSidebar, ...newSidebar]
const catalog = [...existingCatalog, ...newCatalog]
const stats = {
  volumeCount: oldStats.volumeCount + newSidebar.length,
  pageCount: oldStats.pageCount + newCatalog.reduce((sum, item) => sum + item.pageCount, 0),
  characterCount: oldStats.characterCount + newCharacterCount,
  noteCount: oldStats.noteCount,
  noteReferenceCount: oldStats.noteReferenceCount,
  orphanNoteCount: oldStats.orphanNoteCount
}

const generated = `// 此文件由 scripts/import-world-classics.mjs 生成，请勿手工编辑。\nexport const librarySidebar = ${JSON.stringify(sidebar, null, 2)}\n\nexport const libraryCatalog = ${JSON.stringify(catalog, null, 2)}\n\nexport const libraryStats = ${JSON.stringify(stats, null, 2)}\n`
fs.writeFileSync(generatedPath, generated)

const indexMarkdown = [
  '---',
  'title: "作品目录"',
  'description: "分卷目录"',
  '---',
  '',
  '# 作品目录',
  '',
  '站内作品已按分卷、分部和章节整理。选择一卷开始阅读。',
  '',
  `共 ${stats.volumeCount} 个分卷、${stats.pageCount} 个阅读页面，正文约 ${Math.round(stats.characterCount / 10000).toLocaleString('zh-CN')} 万字。`,
  '',
  ...catalog.map((item, index) => {
    const volumeNo = index + 1
    const label = item.volumeLabel === '新增卷' ? `第${volumeNo}卷：${item.title}` : `${item.volumeLabel}：${item.title}`
    const author = item.author ? ` — ${item.author}` : ''
    return `- [${label}](${item.link})${author}，${item.pageCount} 个阅读页面`
  }),
  ''
].join('\n')
fs.writeFileSync(path.join(rootDir, 'docs', 'index.md'), indexMarkdown)

console.log(`完成：新增 ${newSidebar.length} 卷、${newCatalog.reduce((sum, item) => sum + item.pageCount, 0)} 个阅读页面。`)
