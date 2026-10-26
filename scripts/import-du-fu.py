"""Import the supplied Qian Qianyi annotated Du Fu PDF, one work per Markdown.

Usage: python scripts/import-du-fu.py <PDF path> [--check]
Requires PyMuPDF. The source PDF stays outside the repository.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess

import pymupdf


ROOT = Path(__file__).resolve().parent.parent
VOLUME = ROOT / "docs/library/volume-94"
ASSETS = ROOT / "docs/public/library/volume-94/images"
MANIFEST = ROOT / "scripts/du-fu-source-manifest.json"
MODULE = ROOT / "docs/.vitepress/library.du-fu.mjs"
BOOK = "杜甫全集"
PDF_TITLE = "杜甫诗集"
SOURCE_SHA256 = "08a7bb13a412aa6b727f44e1821e9a813d9f5c33940ff261d433bd0459d37736"
CHINESE = "一二三四五六七八九十百"
NOTE = re.compile(rf"〔([{CHINESE}]+)〕|\[(\d+)\]")
TOKEN = re.compile(r"@@REF:(\d+)@@")
# The printed edition has two sequences whose body and note labels disagree.
# Preserve both printed labels; link according to the words actually explained.
REVIEWED_NOTE_TARGETS = {
    470: {"〔五〕": "〔四〕", "〔六〕": "〔五〕"},
    974: {"〔四〕": "〔三〕", "〔五〕": "〔四〕", "〔六〕": "〔五〕"},
}
REVIEWED_MISSING_REFERENCES = {
    (681, "〔一〕"), (745, "〔十一〕"), (816, "〔一〕"),
}
AUTHOR_PREFACE_PAGES = {398, 404, 416, 421, 445, 456, 457, 542, 543}
# A few passages have ordinary text and readings in the wrong PDF font size.
# These source-local exceptions are for the unannotated view only.
PLAIN_RETAIN_SMALL = {
    328: {"图有二马，"},
    873: {"马，", "重", "到使君滩"},
    998: {"梳。"},
    575: {"一作济潭"},
}
PLAIN_ANNOTATION_IMAGES = {
    "glyph-b3d8b0ea8f4598675cb3.jpg",  # 樊本异文：PDF 第 598 页。
    "glyph-8f9f57990bfa11da2ff8.jpg",  # “一云连……洞”：PDF 第 622 页。
    "glyph-28e3a24c7668aaf61242.jpg",  # 㶉鶒的夹注字形：PDF 第 671 页。
    "glyph-f0a0fa485a382a2ef06f.jpg",  # “陈作……”异文：PDF 第 1307 页。
}
PLAIN_TEXT_REPLACEMENTS = {
    328: {"新一作画": "新"},
    773: {"时一云期": "时"},
    873: {"一云五": "", "晋作当": "", "一作直": ""},
    895: {"北一云南": "北"},
    923: {"汉一云漠": "汉"},
    998: {"堪一云宜": "堪"},
    1153: {"不一作北": "不"},
    1398: {"如陈作为": "如", "辜刊作孤": "辜"},
    575: {"一作济潭": "潭"},
    688: {"立一": "立"},
    702: {"征魂一": "征魂"},
    804: {"行户": "行", "郎切蚁": "蚁"},
    1117: {"南一": "南"},
}
PLAIN_PARAGRAPH_REPLACEMENTS = {
    643: {"只甘似鲁诸生": "只似鲁诸生"},
    1134: {"镜象未离铨一": "镜象未离铨"},
    1139: {"乞去米烦佳客": "乞米烦佳客"},
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


class VisibleText(HTMLParser):
    """Read generated article text without navigation or return-arrow labels."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = dict(attrs).get("class", "") or ""
        if self.skip:
            self.skip += 1
        elif any(name in classes.split() for name in ("reading-meta", "du-fu-source-note", "footnote-backrefs")):
            self.skip = 1

    def handle_endtag(self, tag: str) -> None:
        if self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.parts.append(data)


def cn(number: int) -> str:
    if number < 10:
        return "零一二三四五六七八九"[number]
    if number < 20:
        return "十" + (cn(number % 10) if number % 10 else "")
    if number < 100:
        return cn(number // 10) + "十" + (cn(number % 10) if number % 10 else "")
    raise ValueError(number)


def cn_number(text: str) -> int:
    if "百" in text:
        first, tail = text.split("百")
        return cn_number(first) * 100 + (cn_number(tail) if tail else 0)
    if "十" in text:
        first, tail = text.split("十")
        return (cn_number(first) if first else 1) * 10 + (cn_number(tail) if tail else 0)
    return "零一二三四五六七八九".index(text)


@dataclass
class Fragment:
    text: str
    size: float
    x: float
    y: float
    right: float
    bottom: float
    font: str = ""
    image: str = ""
    width_em: float = 1


@dataclass
class Line:
    page: int
    fragments: list[Fragment]

    @property
    def text(self) -> str:
        return "".join(f.text for f in self.fragments)

    @property
    def size(self) -> float:
        if len(self.fragments) == 1 and self.fragments[0].image and self.fragments[0].size > 40:
            return 0
        return max(f.size for f in self.fragments)

    @property
    def x(self) -> float:
        return min(f.x for f in self.fragments)

    @property
    def y(self) -> float:
        if self.size == 0:
            return self.fragments[0].y
        return max(f.y for f in self.fragments if abs(f.size - self.size) < 0.1)


@dataclass
class Paragraph:
    lines: list[Line] = field(default_factory=list)
    heading: bool = False

    @property
    def text(self) -> str:
        return "".join(line.text for line in self.lines)


@dataclass
class Section:
    title: str
    group: str
    kind: str
    page: int
    y: float = 0
    number: int = 0
    end: tuple[int, float] = (1561, 0)
    paragraphs: list[Paragraph] = field(default_factory=list)
    previous: dict | bool = False
    following: dict | bool = False

    @property
    def route(self) -> str:
        return f"/library/volume-94/chapter-{self.number:04d}"

    @property
    def filename(self) -> Path:
        return VOLUME / f"chapter-{self.number:04d}.md"


class Importer:
    def __init__(self, path: Path):
        self.source_bytes = path.read_bytes()
        self.source_sha256 = sha256(self.source_bytes)
        if SOURCE_SHA256 and self.source_sha256 != SOURCE_SHA256:
            raise ValueError("PDF SHA-256 differs from the inspected edition")
        self.pdf = pymupdf.open(path)
        if len(self.pdf) != 1560:
            raise ValueError("Expected the supplied 1,560-page edition")
        self.assets: dict[str, bytes] = {}
        self.pages: list[dict] = []
        self.reference_count = 0
        self.definition_count = 0
        self.warnings: list[str] = []
        self.resolution_errors: list[dict] = []
        self.group_lines: dict[str, list[Line]] = defaultdict(list)
        self.source_image_count = 0
        self.missing_glyph_count = 0

    def image_fragment(self, page: pymupdf.Page, block: dict) -> Fragment:
        x, top, right, bottom = block["bbox"]
        data = block["image"]
        ext = "jpg" if block["ext"] == "jpeg" else block["ext"]
        name = f"glyph-{sha256(data)[:20]}.{ext}"
        self.assets[name] = data
        self.source_image_count += 1
        size = bottom - top
        return Fragment("", size, x, bottom, right, bottom, image=name,
                        width_em=(right - x) / size)

    def lines_for_page(self, page: pymupdf.Page) -> list[Line]:
        fragments: list[Fragment] = []
        large_images: list[Line] = []
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 1:
                fragment = self.image_fragment(page, block)
                if block["bbox"][3] - block["bbox"][1] > 40:
                    large_images.append(Line(page.number + 1, [fragment]))
                else:
                    fragments.append(fragment)
                continue
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"]
                    x, top, right, bottom = span["bbox"]
                    if "\0" in text:
                        if text != "\0":
                            raise ValueError(f"Mixed missing glyph on page {page.number + 1}")
                        # Preserve the actual printed glyph, rather than guessing a
                        # Unicode replacement for a broken ToUnicode entry.
                        data = page.get_pixmap(matrix=pymupdf.Matrix(4, 4),
                                               clip=pymupdf.Rect(span["bbox"]),
                                               alpha=False).tobytes("png")
                        name = f"unmapped-{sha256(data)[:20]}.png"
                        self.assets[name] = data
                        self.missing_glyph_count += 1
                        fragments.append(Fragment("", span["size"], x,
                                                  span["origin"][1], right, bottom,
                                                  image=name, width_em=(right - x) / span["size"]))
                    else:
                        fragments.append(Fragment(text, span["size"], x,
                                                  span["origin"][1], right, bottom,
                                                  span["font"]))
        # Superscript note numbers are 5.25 pt above their body line; the
        # nearest full-size baseline unifies text split around inline images.
        anchors: list[float] = []
        for fragment in sorted(fragments, key=lambda f: (-f.size, f.y)):
            if fragment.image or fragment.size < 14:
                continue
            if not any(abs(fragment.y - anchor) < 11 for anchor in anchors):
                anchors.append(fragment.y)
        for fragment in fragments:
            if not anchors or min(abs(fragment.y - anchor) for anchor in anchors) >= 11:
                anchors.append(fragment.y)
        buckets: dict[float, list[Fragment]] = defaultdict(list)
        for fragment in fragments:
            anchor = min(anchors, key=lambda y: abs(y - fragment.y))
            buckets[anchor].append(fragment)
        result = [Line(page.number + 1, sorted(items, key=lambda f: f.x))
                  for _, items in sorted(buckets.items())]
        result.extend(large_images)
        result.sort(key=lambda line: line.y)
        return result

    def sections(self, lines: dict[int, list[Line]]) -> list[Section]:
        sections: list[Section] = []
        group = "卷首"
        appendix = ""
        self.groups: list[str] = [group]
        for level, title, page in self.pdf.get_toc():
            if title == "目录":
                continue
            if level == 1 and page < 56:
                sections.append(Section(title, group, "front", page))
            elif level == 2 and page < 1497:
                group = "诗歌补遗" if title == "附录" else title
                self.groups.append(group)
            elif level == 3:
                if 1428 <= page <= 1440:
                    # These bookmarks collect unrelated poems. Their individual
                    # 21.25 pt headings below provide the actual work boundaries.
                    self.group_lines[group].extend(
                        line for line in lines[page] if line.size > 24)
                    continue
                sections.append(Section(NOTE.sub("", title), group, "poem" if page < 1441 else "prose", page))
            elif level == 1 and page >= 1497:
                appendix = title
                self.groups.append(appendix)
                if page == 1509:
                    sections.append(Section("少陵先生年谱", appendix, "chronology", 1510))
            elif level == 2 and page >= 1497 and page != 1510:
                sections.append(Section(title, appendix, "appendix-poem" if page >= 1544 else "appendix", page))
        for page in range(1428, 1441):
            subgroup = next(title for level, title, first in reversed(self.pdf.get_toc())
                            if level == 3 and 1428 <= first <= page)
            for line in lines[page]:
                if 20 <= line.size < 24:
                    title = "".join(f.text for f in line.fragments if f.size >= 20)
                    title = NOTE.sub("", title).strip()
                    sections.append(Section(title, f"诗歌补遗 · {subgroup}", "supplement-poem", page, line.y - 1))
        main_works = sorted((s for s in sections if s.kind == "poem"), key=lambda s: s.page)
        for index, parent in enumerate(main_works):
            last_page = main_works[index + 1].page if index + 1 < len(main_works) else 1427
            for page in range(parent.page, last_page):
                for line in lines.get(page, []):
                    if not 20 <= line.size < 24 or NOTE.match(line.text) or line.text.startswith("卷"):
                        continue
                    if parent.title == "江头五咏" or page == 1256:
                        continue
                    title = "".join(f.text for f in line.fragments if f.size >= 20)
                    title = compact(NOTE.sub("", title))
                    sections.append(Section(title, parent.group, "quoted-poem", page, line.y - 1))
        # Preserve the short editorial introduction to the collected poetics.
        sections.append(Section("诸家诗话引言", "附录三：诸家诗话", "appendix", 1529))
        # The PDF bookmarks put the eight individually named elegies next to
        # their common preamble. They form one cycle, not nine separate works.
        sections = [section for section in sections if not 422 <= section.page < 442]
        sections.sort(key=lambda section: (section.page, section.y))
        for index, section in enumerate(sections):
            section.number = index + 1
            section.previous = ({"text": sections[index - 1].title, "link": sections[index - 1].route}
                                if index else {"text": "本卷首页", "link": "/library/volume-94/"})
            if index + 1 < len(sections):
                following = sections[index + 1]
                # The next section has not received its number in this loop.
                section.following = {"text": following.title, "link": f"/library/volume-94/chapter-{index + 2:04d}"}
                section.end = following.page, following.y
        # Volume divider pages and their short chronological notes belong on
        # the book contents page, rather than the end of the preceding poem.
        dividers = sorted((page, "诗歌补遗" if title == "附录" else title)
                          for level, title, page in self.pdf.get_toc()
                          if level == 2 and page < 1497)
        dividers.extend((page, title) for level, title, page in self.pdf.get_toc()
                        if level == 1 and page >= 1497)
        for index, (page, title) in enumerate(dividers):
            next_work = min((s.page, s.y) for s in sections if (s.page, s.y) > (page, 0))
            for current in range(page, next_work[0] + 1):
                for line in lines.get(current, []):
                    if (line.page, line.y) < next_work:
                        self.group_lines[title].append(line)
            for section in sections:
                if (section.page, section.y) < (page, 0) < section.end:
                    section.end = page, 0
        return sections

    def paragraphs(self, selected: list[Line]) -> list[Paragraph]:
        result: list[Paragraph] = []
        for line in selected:
            heading = line.size >= 20 and not (line.page == 1256 and line.text.startswith("如意"))
            previous = result[-1].lines[-1] if result else None
            new = not previous or heading != result[-1].heading
            if heading:
                new = new or line.page != previous.page or line.y - previous.y > 45
            elif previous:
                # A two-character indent begins a paragraph. Page-top text at
                # the left margin continues the preceding page's paragraph.
                new = new or line.x > 95
                if line.page == previous.page and line.y - previous.y > 27:
                    new = True
                if NOTE.match(line.text.strip()) and line.x > 95:
                    new = True
            if line.size == 0 or previous and previous.size == 0:
                new = True
            if new:
                result.append(Paragraph([line], heading))
            else:
                result[-1].lines.append(line)
        return result

    def fragment_html(self, fragment: Fragment, paragraph: Paragraph,
                      references: list[dict], normal_size: float) -> str:
        if fragment.image:
            if fragment.size > 40:
                return (f'<img class="du-fu-figure" src="/library/volume-94/images/{fragment.image}" '
                        'alt="原书所附杜氏世系图" />')
            return (f'<img class="du-fu-glyph" src="/library/volume-94/images/{fragment.image}" '
                    f'alt="原书用字" style="width: {fragment.width_em:.3f}em" />')
        text = html.escape(fragment.text, quote=False)
        if NOTE.fullmatch(fragment.text.strip()):
            return text
        if fragment.size < normal_size - 1 and text.strip():
            return f'<small class="du-fu-variant">{text}</small>'
        return text

    def render_paragraph(self, paragraph: Paragraph, references: list[dict], title_threshold: float | None = None) -> str:
        # Footnote definitions are set entirely in the smaller type, while
        # readings and authorial notes are smaller fragments of a body line.
        normal_size = max((f.size for line in paragraph.lines for f in line.fragments if not f.image), default=15)
        if not paragraph.heading:
            normal_size = 15 if normal_size > 14 else normal_size
        pieces: list[str] = []
        fragments = [f for line in paragraph.lines for f in line.fragments]
        title_end = -1
        if title_threshold is not None:
            title_end = max(index for index, fragment in enumerate(fragments)
                            if fragment.size >= title_threshold and NOTE.sub("", fragment.text).strip())
            while title_end + 1 < len(fragments) and NOTE.fullmatch(fragments[title_end + 1].text.strip()):
                title_end += 1
        offset = 0
        for line in paragraph.lines:
            for fragment in line.fragments:
                pieces.append(self.fragment_html(fragment, paragraph, references, normal_size))
                if offset == title_end:
                    pieces.append("@@TITLE_END@@")
                offset += 1
        text = "".join(pieces).strip()
        text = re.sub(r'</small><small class="du-fu-variant">', '', text)
        text = re.sub(rf"〔(?:<[^>]+>|[{CHINESE}])+〕",
                      lambda match: re.sub(r"<[^>]+>", "", match.group()), text)
        # Some original note markers use ordinary body-size characters. Their
        # meaning comes from the corresponding note, not from font size.
        definition = self.definition_label(paragraph)
        first_label = True
        def reference(match: re.Match) -> str:
            nonlocal first_label
            if definition and first_label and match.group() == definition.group():
                first_label = False
                return match.group()
            first_label = False
            references.append({"label": match.group(), "paragraph": paragraph})
            return f"@@REF:{len(references) - 1}@@"
        text = NOTE.sub(reference, text)
        return text

    def looks_like_verse(self, paragraph: Paragraph) -> bool:
        plain = "".join(("□" if f.image else f.text)
                        for line in paragraph.lines for f in line.fragments if f.size >= 14)
        if ((paragraph.lines[0].page == 281 and plain.startswith("窦侍御"))
                or (paragraph.lines[0].page == 326 and plain.startswith("江心"))):
            return True
        if paragraph.lines[0].page == 838 and plain.startswith("唐曲"):
            return False
        if NOTE.match(plain) or plain.startswith(("笺曰", "又曰", "按", "右", "《")) or "：" in plain:
            return False
        plain = NOTE.sub("", plain)
        lengths = [len(compact(phrase)) for phrase in re.split(r"[，。？！；]", plain) if compact(phrase)]
        return len(lengths) >= 3 and sum(n in (5, 7, 10, 14, 21) for n in lengths) / len(lengths) >= 0.7

    def definition_label(self, paragraph: Paragraph) -> re.Match | None:
        if paragraph.heading or paragraph.lines[0].x < 95:
            return None
        match = NOTE.match(paragraph.text.strip())
        if match and paragraph.text.strip()[match.end():].startswith(("，", "。", "？", "！", "；")):
            return None
        return match

    def original_paragraph(self, paragraph: Paragraph) -> str:
        main_size = max((f.size for line in paragraph.lines for f in line.fragments if not f.image), default=15)
        threshold = main_size - 1 if paragraph.heading else 14
        pieces: list[str] = []
        discarded = ""
        for line in paragraph.lines:
            for fragment in line.fragments:
                if fragment.image in PLAIN_ANNOTATION_IMAGES:
                    continue
                keep = fragment.size >= threshold or fragment.text in PLAIN_RETAIN_SMALL.get(line.page, set())
                if not keep:
                    discarded += NOTE.sub("", fragment.text)
                    continue
                value = fragment.text
                for before, after in PLAIN_TEXT_REPLACEMENTS.get(line.page, {}).items():
                    value = value.replace(before, after)
                value = NOTE.sub("", value)
                if not value and not fragment.image:
                    continue
                if (discarded and discarded[-1] in "，。？！；" and value
                        and value[0] not in "，。？！；" and pieces):
                    pieces.append(discarded[-1])
                discarded = ""
                if fragment.image:
                    pieces.append(self.fragment_html(fragment, paragraph, [], main_size))
                else:
                    pieces.append(html.escape(value, quote=False))
        if discarded and discarded[-1] in "，。？！；":
            pieces.append(discarded[-1])
        text = "".join(pieces).strip()
        text = re.sub(rf"〔[{CHINESE}]*〕|\[\d*\]", "", text)
        for page in {line.page for line in paragraph.lines}:
            for before, after in PLAIN_PARAGRAPH_REPLACEMENTS.get(page, {}).items():
                text = text.replace(before, after)
        # Font errors occasionally leave a quotation mark from a removed
        # alternative reading. Retain balanced punctuation in original prose.
        for opening, closing in (("“", "”"), ("‘", "’")):
            stack: list[int] = []
            unmatched: set[int] = set()
            for position, character in enumerate(text):
                if character == opening:
                    stack.append(position)
                elif character == closing:
                    if stack:
                        stack.pop()
                    else:
                        unmatched.add(position)
            unmatched.update(stack)
            text = "".join(c for n, c in enumerate(text) if n not in unmatched)
        return text

    def original_view(self, section: Section, verse_indexes: list[int]) -> str:
        paragraphs = section.paragraphs
        parts: list[str] = []
        headings: list[tuple[str, str]] = []
        has_headings = any(p.heading and NOTE.sub("", p.text).strip() for p in paragraphs[1:])
        count_match = re.search(rf"([{CHINESE}]+)(?:首|章)", section.title)
        expected = cn_number(count_match[1]) if count_match else (3 if section.title.startswith("三绝句") else 0)
        numbered = not has_headings and expected > 1 and len(verse_indexes) == expected
        first_verse = min(verse_indexes)
        for index, paragraph in enumerate(paragraphs):
            if index == 0:
                continue
            if paragraph.heading:
                label = self.original_paragraph(paragraph)
                if label:
                    anchor = f"original-part-{len(headings) + 1}"
                    headings.append((anchor, re.sub(r"<[^>]+>", "", label)))
                    parts.append(f'<h2 class="du-fu-original-heading" id="{anchor}">{label}</h2>')
            elif index in verse_indexes:
                if numbered:
                    label = f"其{cn(verse_indexes.index(index) + 1)}"
                    anchor = f"original-part-{len(headings) + 1}"
                    headings.append((anchor, label))
                    parts.append(f'<h2 class="du-fu-original-heading" id="{anchor}">{label}</h2>')
                text = self.original_paragraph(paragraph)
                text = re.sub(r"([。？！])", r"\1<br />", text).removesuffix("<br />")
                parts.append(f'<p class="du-fu-verse">{text}</p>')
            elif index < first_verse and not self.definition_label(paragraph):
                author = (section.kind in ("quoted-poem", "appendix-poem")
                          and len(compact(paragraph.text)) <= 15
                          and not re.search(r"[，。；：]", paragraph.text))
                if section.page in AUTHOR_PREFACE_PAGES or author:
                    text = self.original_paragraph(paragraph)
                    if text:
                        parts.append(f"<p>{text}</p>")
        navigation = ""
        if len(headings) > 1:
            navigation = ('<nav class="du-fu-poem-outline" aria-label="组诗目录">'
                          + "".join(f'<a href="#{anchor}">{label}</a>' for anchor, label in headings) + '</nav>\n\n')
        return f"<h1>{html.escape(section.title)}</h1>\n\n" + navigation + "\n\n".join(parts)

    def render_section(self, section: Section) -> tuple[str, dict]:
        paragraphs = section.paragraphs
        if not paragraphs or not paragraphs[0].heading and section.title != "诸家诗话引言":
            raise ValueError(f"Missing printed title: {section.title} (PDF {section.page})")
        references: list[dict] = []
        rendered: list[str] = []
        heading_html = section.title
        for index, paragraph in enumerate(paragraphs):
            threshold = 20 if section.kind in ("supplement-poem", "quoted-poem") else 24
            value = self.render_paragraph(paragraph, references,
                                          title_threshold=threshold if index == 0 and paragraph.heading else None)
            if index == 0 and paragraph.heading:
                # Keep all title annotations next to the clean navigation title.
                heading_html, value = value.split("@@TITLE_END@@", 1)
                if section.kind == "chronology":
                    value = "## " + heading_html + "\n\n" + value
                    heading_html = section.title
            elif paragraph.heading:
                value = "## " + value
            rendered.append(value)
        definitions: list[dict] = []
        for index, (paragraph, value) in enumerate(zip(paragraphs, rendered)):
            if index == 0 and paragraph.heading:
                continue
            label = self.definition_label(paragraph)
            if label:
                definitions.append({"index": index, "label": label.group(),
                                    "id": f"note-du-fu-{section.number:04d}-{len(definitions) + 1}", "refs": []})
        ref_indexes = {id(paragraph): index for index, paragraph in enumerate(paragraphs)}
        for number, reference in enumerate(references):
            position = ref_indexes[id(reference["paragraph"])]
            target_label = REVIEWED_NOTE_TARGETS.get(section.page, {}).get(reference["label"], reference["label"])
            following = [d for d in definitions if d["label"] == target_label and d["index"] > position]
            if not following:
                self.resolution_errors.append({"title": section.title, "page": section.page,
                                               "label": reference["label"], "paragraph": position})
                reference["html"] = reference["label"]
                continue
            definition = following[0]
            ref_id = f"note-ref-du-fu-{section.number:04d}-{number + 1}"
            definition["refs"].append(ref_id)
            reference["html"] = (f'<sup class="footnote-ref" id="{ref_id}"><a href="#{definition["id"]}">'
                                 f'{reference["label"]}</a></sup>')
        for index, value in enumerate(rendered):
            rendered[index] = TOKEN.sub(lambda match: references[int(match[1])]["html"], value)
        heading_html = TOKEN.sub(lambda match: references[int(match[1])]["html"], heading_html)
        for definition in definitions:
            index = definition["index"]
            value = rendered[index]
            label = definition["label"]
            if not value.startswith(label):
                raise ValueError(f"Styled definition label: {section.title}: {value[:100]}")
            if not definition["refs"]:
                if (section.page, label) not in REVIEWED_MISSING_REFERENCES:
                    raise ValueError(f"Unexpected unreferenced source note: PDF {section.page}: {label}")
                self.warnings.append(f"原书正文缺注号：PDF {section.page}《{section.title}》{label}")
            backrefs = "".join(f'<a class="footnote-backref" href="#{ref_id}" aria-label="返回正文">↩</a>'
                               for ref_id in definition["refs"])
            rendered[index] = (f'<p class="footnote-definition footnote-source" id="{definition["id"]}">'
                               f'<span class="footnote-number">{label}</span>{value[len(label):]}'
                               f'<span class="footnote-backrefs">{backrefs}</span></p>')
        verse_indexes = [index for index, paragraph in enumerate(paragraphs)
                         if index and not paragraph.heading and "poem" in section.kind
                         and self.looks_like_verse(paragraph)]
        expected = re.search(rf"([{CHINESE}]+)首", section.title)
        group_count = cn_number(expected[1]) if expected else (3 if section.title.startswith("三绝句") else 0)
        number_verses = (group_count > 1 and len(verse_indexes) == group_count
                         and not any(p.heading for p in paragraphs[1:]))
        for number, index in enumerate(verse_indexes, 1):
            # Split on punctuation outside HTML tags (annotations and image
            # attributes must not introduce artificial verse boundaries).
            chunks = re.split(r"(<[^>]+>)", rendered[index])
            depth = 0
            for i, chunk in enumerate(chunks):
                if chunk.startswith(("<small", "<sup")):
                    depth += 1
                elif chunk.startswith(("</small", "</sup")):
                    depth -= 1
                elif not chunk.startswith("<") and not depth:
                    chunks[i] = re.sub(r"([。？！])", r"\1<br />", chunk)
            verse = "".join(chunks).removesuffix("<br />")
            rendered[index] = (f"## 其{cn(number)}\n\n" if number_verses else "") + f'<p class="du-fu-verse">{verse}</p>'
        self.reference_count += len(references)
        self.definition_count += len(definitions)
        if paragraphs[0].heading and section.kind != "chronology":
            if (len(paragraphs) > 1 and rendered[0] and not paragraphs[1].heading
                    and paragraphs[1].lines[0].x < 95
                    and paragraphs[0].lines[-1].page == paragraphs[1].lines[0].page
                    and paragraphs[1].lines[0].y - paragraphs[0].lines[-1].y < 28):
                continuation = rendered[1]
                if '<small class="du-fu-variant">' in rendered[0]:
                    continuation = f'<small class="du-fu-variant">{continuation}</small>'
                rendered[0] += continuation
                rendered[0] = rendered[0].replace('</small><small class="du-fu-variant">', '')
                rendered[1] = ""
        frontmatter = ["---", f"title: {json.dumps(section.title, ensure_ascii=False)}",
                       f"description: {json.dumps(f'{BOOK} · {section.group} · {section.title}', ensure_ascii=False)}",
                       "pageClass: du-fu-reading",
                       f"prev: {json.dumps(section.previous, ensure_ascii=False)}",
                       f"next: {json.dumps(section.following, ensure_ascii=False)}", "---", "",
                       f'<p class="reading-meta"><a href="./">{BOOK}</a> · {html.escape(section.group)}</p>',
                       "", f"# {heading_html}", ""]
        body = "\n\n".join(part for part in rendered if part)
        if section.page in REVIEWED_NOTE_TARGETS:
            body = ('<p class="du-fu-source-note">本篇正文与注文的注号沿用原书；跳转按注文所释词语对应。</p>\n\n' + body)
        markdown = "\n".join(frontmatter) + "\n" + body + "\n"
        # A second representation checks every retained source character after
        # formatting, title movement, annotation linking, and stanza splitting.
        article = markdown.split("---", 2)[2]
        article = re.sub(rf"^## 其[{CHINESE}]+\s*$", "", article, flags=re.M)
        if section.kind == "chronology" or section.title == "诸家诗话引言":
            article = re.sub(r"^# .*\n", "", article, count=1, flags=re.M)
        article = re.sub(r"^#{1,3} ", "", article, flags=re.M)
        reader = VisibleText()
        reader.feed(article)
        actual = compact("".join(reader.parts))
        expected_text = compact("".join(p.text for p in paragraphs))
        if actual != expected_text:
            first = next((n for n, (a, b) in enumerate(zip(actual, expected_text)) if a != b),
                         min(len(actual), len(expected_text)))
            raise ValueError(f"Source text changed in {section.title}: "
                             f"expected {expected_text[max(0, first - 20):first + 50]!r}, "
                             f"got {actual[max(0, first - 20):first + 50]!r}")
        original = ""
        if "poem" in section.kind:
            if not verse_indexes:
                raise ValueError(f"No poem text found for original view: {section.title}")
            original = self.original_view(section, verse_indexes)
            before_heading, annotated = markdown.split(f"# {heading_html}", 1)
            annotated = f"# {heading_html}" + annotated
            before_heading = before_heading.replace("pageClass: du-fu-reading\n", "pageClass: du-fu-reading\noutline: false\n")
            markdown = (before_heading + '<DuFuPoem>\n\n<template #original>\n\n' + original
                        + '\n\n</template>\n\n<template #annotated>\n\n' + annotated.rstrip()
                        + '\n\n</template>\n\n</DuFuPoem>\n')
        used_pages = sorted({line.page for p in paragraphs for line in p.lines})
        entry = {"number": section.number, "title": section.title, "group": section.group,
                 "kind": section.kind, "route": section.route, "pdf_pages": used_pages,
                 "source_start": [section.page, round(section.y, 3)],
                 "markdown_sha256": sha256(markdown.encode()), "note_definitions": len(definitions),
                 "note_references": len(references), "verse_paragraphs": len(verse_indexes)}
        if original:
            entry["original_view_sha256"] = sha256(original.encode())
        return markdown, entry

    def generate(self) -> dict[Path, bytes]:
        all_lines: dict[int, list[Line]] = {}
        # Old contents and the three cover images are replaced by the live TOC.
        omitted = set(range(1, 40)) | {55, 750}
        for page in self.pdf:
            if page.number + 1 not in omitted:
                all_lines[page.number + 1] = self.lines_for_page(page)
            self.pages.append({"pdf_page": page.number + 1,
                               "text_sha256": sha256(page.get_text().encode()),
                               "omitted": page.number + 1 in omitted})
        sections = self.sections(all_lines)
        assigned: Counter[tuple[int, int]] = Counter()
        for section in sections:
            selected = []
            for page in range(section.page, min(section.end[0] + 1, len(self.pdf) + 1)):
                for index, line in enumerate(all_lines.get(page, [])):
                    if (section.page, section.y) <= (page, line.y) < section.end:
                        selected.append(line)
                        assigned[(page, index)] += 1
            section.paragraphs = self.paragraphs(selected)
        group_ids = {id(line) for lines in self.group_lines.values() for line in lines}
        unassigned = []
        for page, lines in all_lines.items():
            for index, line in enumerate(lines):
                count = assigned[(page, index)]
                if count > 1:
                    raise ValueError(f"Source line assigned twice on PDF {page}")
                if count == 0 and id(line) not in group_ids:
                    unassigned.append((page, line.text))
        if unassigned:
            raise ValueError(f"Unassigned source lines: {unassigned[:20]}")
        # Editorial footnotes stay with their actual citation when a separately
        # titled quoted poem intervenes before the source page's footnote area.
        arabic_references: dict[str, list[tuple[tuple[int, float], Section]]] = defaultdict(list)
        for section in sections:
            for paragraph in section.paragraphs:
                definition = self.definition_label(paragraph)
                for match in re.finditer(r"\[\d+\]", paragraph.text):
                    if definition and match.start() == 0:
                        continue
                    coordinate = paragraph.lines[0].page, paragraph.lines[0].y
                    arabic_references[match.group()].append((coordinate, section))
        for section in sections:
            for paragraph in list(section.paragraphs):
                label = self.definition_label(paragraph)
                if not label or not label.group().startswith("["):
                    continue
                coordinate = paragraph.lines[0].page, paragraph.lines[0].y
                candidates = [(point, owner) for point, owner in arabic_references[label.group()]
                              if point < coordinate]
                if candidates:
                    _, owner = max(candidates, key=lambda candidate: candidate[0])
                    if owner is not section:
                        section.paragraphs.remove(paragraph)
                        owner.paragraphs.append(paragraph)
        files: dict[Path, bytes] = {}
        manifest_sections = []
        for section in sections:
            markdown, entry = self.render_section(section)
            files[section.filename] = markdown.encode()
            manifest_sections.append(entry)
        if self.resolution_errors:
            raise ValueError(f"Unresolved references: {json.dumps(self.resolution_errors, ensure_ascii=False)}")
        if len(sections) != 1224:
            raise ValueError(f"Unexpected work count: {len(sections)}")
        grouped: dict[str, list[Section]] = defaultdict(list)
        for section in sections:
            grouped[section.group].append(section)
        sidebar_items: list[dict] = [{"text": "本卷首页", "link": "/library/volume-94/"}]
        contents = ["---", f'title: "{BOOK}"', 'description: "杜甫诗文全集，钱谦益笺注"', "---", "",
                    f"# {BOOK}", "", "〔唐〕杜甫 著，〔清〕钱谦益 笺注。", "",
                    "据《杜甫诗集》整理，保留原书二十卷、诗歌补遗及四种附录。单篇诗作各自成页，组诗在同一页连续阅读。诗页默认只读原文，可切换查看完整笺注、异文与校记。", "",
                    f"[开始读诗 →]({next(s.route for s in sections if s.kind == 'poem')})", "", "## 目录", ""]
        for group_number, (group, items) in enumerate(grouped.items(), 1):
            anchor = f"part-{group_number:02d}"
            contents.extend([f"### {group} {{#{anchor}}}", ""])
            base_group = group.split(" · ")[0]
            group_intro = self.group_lines.get(group, []) if group == base_group else []
            for paragraph in self.paragraphs(group_intro):
                if not paragraph.heading:
                    contents.extend([self.render_paragraph(paragraph, []), ""])
            contents.extend(f"- [{s.title}]({s.route})" for s in items)
            contents.append("")
            sidebar_items.append({"text": group, "link": f"/library/volume-94/#{anchor}"})
        files[VOLUME / "index.md"] = ("\n".join(contents).rstrip() + "\n").encode()
        character_count = sum(len(compact(self.pdf[p["pdf_page"] - 1].get_text()))
                              for p in self.pages if not p["omitted"])
        catalog = [{"title": BOOK, "fullTitle": f"{BOOK}（钱谦益笺注《{PDF_TITLE}》）",
                    "volumeLabel": "新增卷", "author": "杜甫（钱谦益笺注）", "link": "/library/volume-94/",
                    "firstPage": next(s.route for s in sections if s.kind == "poem"), "pageCount": len(sections)}]
        stats = {"volumeCount": 1, "pageCount": len(sections), "characterCount": character_count}
        module = "// Generated by scripts/import-du-fu.py.\n"
        for export, value in [("duFuLibrarySidebar", [{"text": BOOK, "collapsed": True, "items": sidebar_items}]),
                              ("duFuLibraryCatalog", catalog), ("duFuLibraryStats", stats)]:
            module += f"export const {export} = {json.dumps(value, ensure_ascii=False, indent=2)}\n\n"
        files[MODULE] = (module.rstrip() + "\n").encode()
        manifest = {"book_title": BOOK, "pdf_title": PDF_TITLE, "source_sha256": self.source_sha256,
                    "pdf_page_count": len(self.pdf), "reading_page_count": len(sections),
                    "original_view_count": sum("poem" in s.kind for s in sections),
                    "section_counts": dict(Counter(s.kind for s in sections)),
                    "note_definitions": self.definition_count, "note_references": self.reference_count,
                    "embedded_image_occurrences": self.source_image_count,
                    "unmapped_glyph_occurrences": self.missing_glyph_count,
                    "reviewed_note_target_discrepancies": REVIEWED_NOTE_TARGETS,
                    "assets": [{"name": name, "sha256": sha256(data)} for name, data in sorted(self.assets.items())],
                    "warnings": self.warnings, "sections": manifest_sections, "pages": self.pages}
        files[MANIFEST] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
        files.update((ASSETS / name, data) for name, data in self.assets.items())
        print(json.dumps({key: value for key, value in manifest.items() if key not in ("sections", "pages", "assets")},
                         ensure_ascii=False, indent=2))
        return files


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    previous = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    importer = Importer(args.pdf)
    files = importer.generate()
    existing = set(VOLUME.glob("*.md")) | set(ASSETS.glob("*"))
    stale = existing - set(files)
    if stale:
        owned = {VOLUME / f'chapter-{s["number"]:04d}.md': s["markdown_sha256"]
                 for s in previous.get("sections", [])}
        owned.update({ASSETS / a["name"]: a["sha256"] for a in previous.get("assets", [])})
        for path in stale:
            if path.parent not in (VOLUME, ASSETS) or sha256(path.read_bytes()) != owned.get(path):
                raise ValueError(f"Unexpected or edited file in generated directory: {path}")
        if args.check:
            raise ValueError(f"Stale generated files: {sorted(map(str, stale))}")
        for path in stale:
            path.unlink()
    changed = []
    for path, data in files.items():
        if not path.exists() or path.read_bytes() != data:
            changed.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if args.check and changed:
        raise ValueError(f"Generated files differ: {changed[:20]}")
    if not args.check:
        subprocess.run(["node", "scripts/rebuild-library-index.mjs"], cwd=ROOT, check=True)
    print(f"{'Checked' if args.check else 'Imported'} {len(files)} files; {len(changed)} changed.")


if __name__ == "__main__":
    main()
