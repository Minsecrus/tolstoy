import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..')

const headingPattern = /^(?:第[一二三四五六七八九十百千万0-9]+(?:部|卷|章|幕|场|篇|辑|节)(?:\s|　|$)|[0-9]{1,3}(?:\s|　|$)|[一二三四五六七八九十百千万]+(?:\s|　|$)|上卷$|下卷$|序诗$|序言$|献词$|前言$|引言$|尾声$|终场$|人物$|抒情诗$|叙事诗$|故事诗集$|戏剧$|散文$)/
const containerPattern = /^(?:第[一二三四五六七八九十百千万0-9]+(?:部|卷)(?:\s|　|$)|上卷$|下卷$|故事诗集$|抒情诗$|叙事诗$|戏剧$|散文$)/
const fallbackPattern = /^正文\s*\d+$/

function pageNumber(link) {
  const match = link?.match(/chapter-(\d+)$/)
  return match ? Number(match[1]) : null
}

function pageFile(volumeNo, chapterNo) {
  return path.join(
    rootDir,
    'docs',
    'library',
    `volume-${String(volumeNo).padStart(2, '0')}`,
    `chapter-${String(chapterNo).padStart(3, '0')}.md`,
  )
}

function pageSource(volumeNo, chapterNo) {
  const file = pageFile(volumeNo, chapterNo)
  if (!fs.existsSync(file)) return null
  const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/)
  const h1Index = lines.findIndex((line) => line.startsWith('# '))
  if (h1Index < 0) return null
  return {
    title: lines[h1Index].slice(2).trim(),
    lines: lines.slice(h1Index + 1),
  }
}

function firstContentHeading(volumeNo, chapterNo) {
  const source = pageSource(volumeNo, chapterNo)
  if (!source) return null
  for (const line of source.lines) {
    const text = line.trim()
    if (!text || text.length > 80 || containerPattern.test(text)) continue
    if (headingPattern.test(text)) return text
  }
  return null
}

function sourceTitle(volumeNo, chapterNo) {
  return pageSource(volumeNo, chapterNo)?.title ?? null
}

function pageLabel(volumeNo, chapterNo, original, groupText = '') {
  const title = sourceTitle(volumeNo, chapterNo) ?? original
  const marker = firstContentHeading(volumeNo, chapterNo)
  const isGroupStart = groupText && (
    title === groupText ||
    title.startsWith(`${groupText}　`) ||
    title.startsWith(groupText) ||
    containerPattern.test(title)
  )
  if (isGroupStart && marker === groupText) return `第${chapterNo}页`
  if (fallbackPattern.test(title) || isGroupStart) {
    return marker ?? `第${chapterNo}页`
  }
  return title
}

function contentLabel(volumeNo, chapterNo) {
  const title = sourceTitle(volumeNo, chapterNo)
  return firstContentHeading(volumeNo, chapterNo) ?? (title && !fallbackPattern.test(title) ? title : `第${chapterNo}页`)
}

function page(volumeNo, chapterNo, text) {
  return {
    text,
    link: `/library/volume-${String(volumeNo).padStart(2, '0')}/chapter-${String(chapterNo).padStart(3, '0')}`,
  }
}

function section(text, items, collapsed = true) {
  return { text, collapsed, items }
}

function rangeSection(volumeNo, text, start, end) {
  const items = []
  for (let chapterNo = start; chapterNo <= end; chapterNo += 1) {
    items.push(page(volumeNo, chapterNo, contentLabel(volumeNo, chapterNo)))
  }
  return section(text, items)
}

function rangeWithLabels(volumeNo, text, entries, collapsed = true) {
  return section(text, entries.map(([chapterNo, label]) => page(volumeNo, chapterNo, label)), collapsed)
}

function specialSections(volumeNo) {
  if (volumeNo === 58) {
    return [
      rangeSection(volumeNo, '第一卷　三个妇人', 1, 5),
      rangeSection(volumeNo, '第二卷　归来', 6, 8),
      rangeSection(volumeNo, '第三卷　诱惑', 9, 12),
      rangeSection(volumeNo, '第四卷　闭门羹', 13, 15),
      rangeSection(volumeNo, '第五卷　发现', 16, 19),
      rangeSection(volumeNo, '第六卷　后事', 20, 21),
    ]
  }

  if (volumeNo === 61) {
    return [
      rangeSection(volumeNo, '第一部　妙龄少女', 1, 6),
      rangeSection(volumeNo, '第二部　失身女子', 7, 8),
      rangeSection(volumeNo, '第三部　振作精神', 9, 14),
      rangeSection(volumeNo, '第四部　终身大事', 15, 20),
      rangeSection(volumeNo, '第五部　女人总是吃亏', 21, 27),
      rangeSection(volumeNo, '第六部　皈依宗教者', 28, 33),
      rangeSection(volumeNo, '第七部　完结', 34, 37),
    ]
  }

  if (volumeNo === 68) {
    return [
      rangeWithLabels(volumeNo, '第一部', [[1, '第一章'], [2, '第二章—第三章'], [3, '第四章—第六章']]),
      rangeWithLabels(volumeNo, '第二部', [[4, '第一章'], [5, '第二章'], [6, '第三章']]),
      rangeWithLabels(volumeNo, '第三部', [
        [7, '开篇'], [8, '第一章—第七章'], [9, '第二章'], [10, '第三章'],
        [11, '第四章'], [12, '第五章'], [13, '第六章—第七章'], [14, '第八章'],
        [15, '第九章'], [16, '第十章'], [17, '第十一章'],
      ]),
    ]
  }

  if (volumeNo === 70) {
    return [
      rangeWithLabels(volumeNo, '前置内容', [
        [1, '前言'], [2, '第2页'], [3, '第3页'], [4, '第4页'],
      ]),
      rangeWithLabels(volumeNo, '第一章　昂蒂姆·阿尔芒—迪布瓦', [[5, '一'], [6, '三'], [7, '五']]),
      rangeWithLabels(volumeNo, '第二章　朱利尤斯·德·巴拉格利乌尔', [[8, '一'], [9, '三'], [10, '五'], [11, '七']]),
      rangeWithLabels(volumeNo, '第三章　阿梅代·弗勒里苏瓦尔', [[12, '一'], [13, '二']]),
      rangeWithLabels(volumeNo, '第四章　蜈蚣', [[14, '四'], [15, '二'], [16, '四'], [17, '六'], [18, '七']]),
      rangeWithLabels(volumeNo, '第五章　拉夫卡迪奥', [[19, '一'], [20, '二'], [21, '四'], [22, '六']]),
      rangeWithLabels(volumeNo, '忒修斯', [[23, '一'], [24, '五'], [25, '八'], [26, '十一']]),
    ]
  }

  if (volumeNo === 73) {
    return [rangeWithLabels(volumeNo, '正文', Array.from({ length: 13 }, (_, index) => {
      const chapterNo = index + 1
      return [chapterNo, pageLabel(volumeNo, chapterNo, `正文 ${String(chapterNo).padStart(2, '0')}`)]
    }), false)]
  }

  if (volumeNo === 80) {
    return [rangeWithLabels(volumeNo, '正文', [
      [1, '第一章—第二章'], [2, '第三章—第四章'], [3, '第五章—第六章'],
      [4, '第七章—第九章'], [5, '第十章—第十一章'], [6, '第十二章—第十三章'],
      [7, '第十四章—第十五章'], [8, '第十六章—第十七章'], [9, '第十八章'],
      [10, '第十九章'], [11, '第二十章—第二十一章'],
    ], false)]
  }

  if (volumeNo === 81) {
    return [rangeWithLabels(volumeNo, '正文', [
      [1, '序、第一场—第二场'], [2, '第三场—第四场'], [3, '第五场—第六场'],
      [4, '第七场—第八场'], [5, '第九场—第十一场'], [6, '第十二场—第十四场'],
      [7, '第十五场—第十七场'], [8, '第十八场—第十九场'], [9, '第二十场—第二十三场'],
      [10, '第二十四场—第二十六场'], [11, '第二十七场—第三十一场'],
      [12, '第三十二场—第三十三场'], [13, '第三十四场—第三十六场'],
    ], false)]
  }

  if (volumeNo === 82) {
    return [rangeWithLabels(volumeNo, '正文', [
      [1, '前置内容、第一章'], [2, '第一章续、第二章、第三章'],
      [3, '第三章续、第四章、第五章'], [4, '第五章续、第六章—第九章'],
      [5, '第九章续、第十章—第十一章'], [6, '第十一章续、第十二章—第十四章'],
      [7, '第十四章续、第十五章—第十七章'], [8, '第十七章续、第十八章—第二十一章'],
      [9, '第二十一章续、第二十二章—第二十三章'],
      [10, '第二十三章续、第二十四章—第二十五章'],
      [11, '第二十五章续、第二十六章—第二十七章'],
    ], false)]
  }

  return null
}

function normalizeNode(volumeNo, node, groupText = '') {
  if (node.items) {
    const items = []
    if (node.link) {
      const chapterNo = pageNumber(node.link)
      if (chapterNo) items.push(page(volumeNo, chapterNo, pageLabel(volumeNo, chapterNo, node.text, node.text)))
    }
    items.push(...node.items.map((child) => normalizeNode(volumeNo, child, node.text)))
    return { text: node.text, collapsed: node.collapsed ?? true, items }
  }

  if (!node.link) return { ...node }
  const chapterNo = pageNumber(node.link)
  return chapterNo
    ? page(volumeNo, chapterNo, pageLabel(volumeNo, chapterNo, node.text, groupText))
    : { ...node }
}

export function curateLibrarySidebar(sidebar) {
  return sidebar.map((volume, index) => {
    const volumeNo = index + 1
    const special = specialSections(volumeNo)
    if (special) return { ...volume, items: [volume.items[0], ...special] }
    return {
      ...volume,
      items: [volume.items[0], ...volume.items.slice(1).map((node) => normalizeNode(volumeNo, node))],
    }
  })
}
