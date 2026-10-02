"""Import the 2020 Chinese two-volume edition of Global History into VitePress.

Usage: python scripts/import-global-history.py path/to/global-history.pdf

Requires PyMuPDF (`python -m pip install pymupdf`). The source PDF is deliberately
kept outside the repository; generated Markdown and figure assets are the site input.
Run scripts/extract-global-history-images.py with the same PDF before building.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
import html
import json
from pathlib import Path
import re
import subprocess
import sys

import pymupdf


ROOT = Path(__file__).resolve().parent.parent
VOLUME = 83
VOLUME_DIR = ROOT / "docs" / "library" / f"volume-{VOLUME:02d}"
BOOK_TITLE = "全球通史：从史前到21世纪（第7版新校本）"
AUTHOR = "〔美〕斯塔夫里阿诺斯"
TRANSLATORS = "吴象婴、梁赤民"
PART_PAGES = {46, 112, 340, 490, 548, 655, 762, 996}
OMITTED_PAGES = set(range(641, 655))  # Lower-volume cover, copyright and repeated TOC.
FRONT = [
    (16, "《全球通史》第7版推荐序"),
    (29, "斯塔夫里阿诺斯的乐观与踌躇"),
    (36, "致读者：为什么需要一部21世纪的全球通史？"),
]
LAST_ESSAY_PAGE = 1207
INDEX_PAGE = 1231
AFTERWORD_PAGE = 1255
NOTE_MARKER = re.compile(r"\[(\d+)\]")


@dataclass
class Section:
    start: int
    kind: str
    title: str
    part: str = ""
    number: int = 0
    end: int = 0

    @property
    def route(self) -> str:
        return f"/library/volume-{VOLUME:02d}/chapter-{self.number:03d}"


@dataclass
class Event:
    kind: str
    text: str
    page: int
    x: float
    y: float
    bottom: float
    size: float = 0
    width: int = 0
    height: int = 0


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def heading_from_page(page: pymupdf.Page, threshold: float) -> str:
    result = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            if line["bbox"][1] > 245:
                continue
            if max(span["size"] for span in line["spans"]) >= threshold:
                result.append("".join(span["text"] for span in line["spans"]).strip())
    return compact("".join(result).replace("　", " "))


def sections_from_pdf(pdf: pymupdf.Document) -> list[Section]:
    sections = [Section(start, "front", title) for start, title in FRONT]
    chapter_count = 0
    essay_count = 0
    for level, _, page1 in pdf.get_toc():
        page = page1 - 1
        if page in PART_PAGES and level == 2:
            title = heading_from_page(pdf[page], 29)
            if not re.match(r"^第.+编", title):
                raise ValueError(f"Cannot read part title at PDF page {page1}: {title!r}")
            title = re.sub(r"^(第.+?编)(?=\S)", r"\1 ", title, count=1)
            sections.append(Section(page, "part", title))
        elif level == 3 and 47 <= page <= LAST_ESSAY_PAGE:
            title = heading_from_page(pdf[page], 23)
            if title.startswith("历史对今天的启示"):
                essay_count += 1
                if title != "历史对今天的启示":
                    title = title.replace("历史对今天的启示", "历史对今天的启示：", 1)
                sections.append(Section(page, "essay", title))
            elif re.match(r"^第.+章", title):
                chapter_count += 1
                sections.append(Section(page, "chapter", title))
            else:
                raise ValueError(f"Cannot read chapter title at PDF page {page1}: {title!r}")
    if (chapter_count, essay_count, len(PART_PAGES)) != (44, 8, 8):
        raise ValueError(f"Unexpected contents: {chapter_count} chapters, {essay_count} essays")
    sections += [
        Section(INDEX_PAGE, "index", "索引"),
        Section(AFTERWORD_PAGE, "back", "新校本编后记"),
    ]
    sections.sort(key=lambda section: section.start)
    for number, section in enumerate(sections, 1):
        section.number = number
        section.end = sections[number].start if number < len(sections) else len(pdf)
    part = ""
    for section in sections:
        if section.kind == "part":
            part = section.title
        section.part = part
    if len(sections) != 65 or sections[0].start != 16 or sections[-1].end != len(pdf):
        raise ValueError("Unexpected section ranges; check the PDF edition")
    return sections


def line_text(spans: list[dict]) -> str:
    pieces = []
    for span in spans:
        content = span["text"]
        if span["size"] < 13 and NOTE_MARKER.fullmatch(content.strip()):
            content = f"@@FNREF:{NOTE_MARKER.fullmatch(content.strip()).group(1)}@@"
        pieces.append(content)
    value = "".join(pieces).strip()
    return re.sub(r"([，,][”’])([A-Za-z])", r"\1 \2", value)


def needs_latin_space(left: str, right: str) -> bool:
    if not left or not right:
        return False
    if left[-1].isascii() and left[-1].isalnum() and right[0].isascii() and right[0].isalnum():
        return True
    if left[-1] in ".,:;!?，。’”" and right[0].isascii() and right[0].isalpha():
        return True
    if left[-1] in ".,:;!?" and right[0] in "“‘\"":
        return True
    return False


def events_for_page(page: pymupdf.Page, page0: int) -> list[Event]:
    events = []
    image_index = 0
    for block in page.get_text("dict")["blocks"]:
        if block["type"] == 1:
            image_index += 1
            width, height = block.get("width", 0), block.get("height", 0)
            if min(block["bbox"][2] - block["bbox"][0], block["bbox"][3] - block["bbox"][1]) < 50:
                continue
            name = f"p{page0 + 1:04d}-{image_index:02d}.webp"
            events.append(Event("image", name, page0, block["bbox"][0], block["bbox"][1], block["bbox"][3], width=width, height=height))
            continue
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            text = line_text(line["spans"])
            if not text:
                continue
            size = max(span["size"] for span in line["spans"])
            kind = "title" if size >= 23 else "heading" if size >= 18 else "caption" if size < 14 else "body"
            events.append(Event(kind, text, page0, line["bbox"][0], line["bbox"][1], line["bbox"][3], size))
    # Italic/roman font changes often create several PDF line objects on the
    # same printed baseline (e.g. "[3]Cited by E. Leacock"). Merge those line
    # fragments before paragraph detection, without moving figures.
    text_events = sorted((event for event in events if event.kind != "image"), key=lambda event: ((event.y + event.bottom) / 2, event.x))
    merged: list[Event] = []
    groups: list[list[Event]] = []
    for event in text_events:
        center = (event.y + event.bottom) / 2
        if groups and abs(center - sum((part.y + part.bottom) / 2 for part in groups[-1]) / len(groups[-1])) <= 6:
            groups[-1].append(event)
        else:
            groups.append([event])
    for parts in groups:
        parts.sort(key=lambda part: part.x)
        combined = ""
        for part in parts:
            if needs_latin_space(combined, part.text):
                combined += " "
            combined += part.text
        first = parts[0]
        size = max(part.size for part in parts)
        kind = "title" if size >= 23 else "heading" if size >= 18 else "caption" if size < 14 else "body"
        merged.append(Event(kind, combined, page0, min(part.x for part in parts), min(part.y for part in parts), max(part.bottom for part in parts), size))
    return sorted([*merged, *(event for event in events if event.kind == "image")], key=lambda event: (event.y, event.x))


def join_lines(left: str, right: str) -> str:
    if not left:
        return right
    if not right:
        return left
    if needs_latin_space(left, right):
        return f"{left} {right}"
    return left + right


def escape_leading_markdown(text: str) -> str:
    if re.match(r"^(?:[#>*+\-]|\d+[.)]\s)", text):
        return "\\" + text
    return text


def render_paragraphs(pdf: pymupdf.Document, section: Section) -> tuple[str, int, set[str]]:
    nodes: list[tuple[str, str]] = []
    paragraph = ""
    paragraph_kind = ""
    previous: Event | None = None
    image_names: set[str] = set()
    source_characters = 0

    def flush() -> None:
        nonlocal paragraph, paragraph_kind
        if paragraph:
            nodes.append((paragraph_kind, paragraph))
        paragraph = ""
        paragraph_kind = ""

    for page0 in range(section.start, section.end):
        if page0 in OMITTED_PAGES:
            continue
        events = events_for_page(pdf[page0], page0)
        source_characters += len(re.sub(r"\s", "", pdf[page0].get_text()))
        for event in events:
            if section.start == 29 and page0 == 35 and event.kind == "body" and event.text.startswith("[1]"):
                # The second recommendation essay has a numbered reference list
                # without the usual printed ［注释］ heading.
                flush()
                nodes.append(("heading", "注释"))
            if event.kind == "title" and page0 == section.start:
                continue  # H1 above replaces the original typeset chapter/part title.
            if event.kind == "image":
                flush()
                image_names.add(event.text)
                # VitePress rewrites Markdown image URLs for VITEPRESS_BASE and
                # adds lazy loading. Raw HTML with a relative src is resolved by
                # Vite as a missing source-tree asset in production builds.
                nodes.append(("image", f'![原书插图（PDF 第{page0 + 1}页）](/library/volume-{VOLUME:02d}/images/{event.text})'))
                previous = event
                continue
            if event.kind == "title":
                flush()
                nodes.append(("heading", event.text))
                previous = event
                continue
            if event.kind == "heading":
                flush()
                heading = event.text.strip("［］[] ") if "注释" in event.text and len(event.text) < 12 else event.text
                if nodes and nodes[-1][0] == "heading" and previous and previous.kind == "heading" and previous.page == page0 and event.y - previous.bottom < 18:
                    nodes[-1] = ("heading", join_lines(nodes[-1][1], heading))
                else:
                    nodes.append(("heading", heading))
                previous = event
                continue
            start_new = (
                not paragraph
                or paragraph_kind != event.kind
                or previous is None
                or previous.kind not in ("body", "caption")
                or event.x >= 95 and event.kind == "body"
                or previous.page == page0 and event.y - previous.bottom > 16
                or event.kind == "caption" and event.text.startswith(("图", "地图", "表"))
                or paragraph_kind == "note" and NOTE_MARKER.match(event.text)
            )
            if start_new:
                flush()
                paragraph_kind = event.kind
                paragraph = event.text
            else:
                paragraph = join_lines(paragraph, event.text)
            previous = event
    flush()

    # Endnotes are numbered anew for each chapter in the source edition. Convert the
    # superscript markers in prose into local, bidirectional links where a definition
    # is present; retain unmatched source markers as plain text.
    note_section = False
    definitions: dict[str, str] = {}
    for kind, content in nodes:
        if kind == "heading" and content == "注释":
            note_section = True
        elif note_section and kind in ("body", "caption"):
            match = NOTE_MARKER.match(content)
            if match:
                if match.group(1) in definitions:
                    raise ValueError(f"Duplicate note {match.group(1)} in {section.title}")
                definitions[match.group(1)] = content[match.end():].strip()

    references: defaultdict[str, list[str]] = defaultdict(list)

    def link_reference(match: re.Match[str]) -> str:
        number = match.group(1)
        if number not in definitions:
            return f"[{number}]"
        ref_id = f"note-ref-{number}-{len(references[number]) + 1}"
        references[number].append(ref_id)
        return f'<sup class="footnote-ref" id="{ref_id}"><a href="#note-{number}" aria-label="查看本页注释 {number}">[{number}]</a></sup>'

    output = []
    note_section = False
    for kind, content in nodes:
        if kind == "heading":
            output.append(f"## {escape_leading_markdown(content)}")
            if content == "注释":
                note_section = True
        elif kind == "image":
            output.append(content)
        elif note_section and kind in ("body", "caption") and NOTE_MARKER.match(content):
            match = NOTE_MARKER.match(content)
            number = match.group(1)
            note_text = html.escape(content[match.end():].strip())
            output.append(("note", number, note_text))
        elif kind == "caption":
            output.append(f"*{escape_leading_markdown(content)}*")
        else:
            linked = re.sub(r"@@FNREF:(\d+)@@", link_reference, content)
            output.append(escape_leading_markdown(linked))

    final = []
    for node in output:
        if isinstance(node, tuple):
            _, number, content = node
            backrefs = " ".join(
                f'<a class="footnote-backref" href="#{ref_id}" aria-label="返回注释 {number} 的第 {i} 处引用">↩</a>'
                for i, ref_id in enumerate(references[number], 1)
            )
            if backrefs:
                backrefs = f' <span class="footnote-backrefs">{backrefs}</span>'
            final.append(f'<p class="footnote-definition footnote-local" id="note-{number}"><a class="footnote-number" href="#note-{number}">[{number}]</a>{content}{backrefs}</p>')
        else:
            final.append(node)
    return "\n\n".join(final), source_characters, image_names


def write_markdown(pdf: pymupdf.Document, sections: list[Section]) -> tuple[int, set[str]]:
    VOLUME_DIR.mkdir(parents=True, exist_ok=True)
    for old in VOLUME_DIR.glob("chapter-*.md"):
        old.unlink()
    total_characters = 0
    images = set()
    for section in sections:
        body, count, names = render_paragraphs(pdf, section)
        total_characters += count
        images.update(names)
        if not body:
            raise ValueError(f"No content for {section.title}")
        meta = BOOK_TITLE + (f" · {section.part}" if section.part else "")
        page = (
            f'---\ntitle: "{section.title}"\ndescription: "{meta} · {section.title}"\n---\n\n'
            f'<p class="reading-meta"><a href="./">{BOOK_TITLE}</a>'
            f'{" · " + section.part if section.part else ""}</p>\n\n'
            f'# {section.title}\n\n{body}\n'
        )
        (VOLUME_DIR / f"chapter-{section.number:03d}.md").write_text(page, encoding="utf-8")
    return total_characters, images


def grouped_sections(sections: list[Section]) -> list[tuple[str, list[Section]]]:
    groups: list[tuple[str, list[Section]]] = []
    group_name = "前置内容"
    current: list[Section] = []
    for section in sections:
        if section.kind == "part":
            if current:
                groups.append((group_name, current))
            group_name = section.title
            current = []
        elif section.kind == "index":
            if current:
                groups.append((group_name, current))
            group_name = "附录"
            current = []
        current.append(section)
    if current:
        groups.append((group_name, current))
    return groups


def write_index_and_nav(sections: list[Section], character_count: int) -> None:
    groups = grouped_sections(sections)
    index_lines = [
        "---",
        f'title: "{BOOK_TITLE}"',
        f'description: "{AUTHOR}著；{TRANSLATORS}译。上、下册正文与插图。"',
        "---", "", f"# {BOOK_TITLE}", "",
        f"{AUTHOR}著，{TRANSLATORS}译。", "",
        f"[开始阅读 →]({sections[0].route})", "",
        "## 目录", "",
    ]
    for group_name, items in groups:
        index_lines.append(f"### {group_name}")
        index_lines.extend(f"- [{item.title}]({item.route})" for item in items)
        index_lines.append("")
    (VOLUME_DIR / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

    sidebar = [{
        "text": BOOK_TITLE,
        "collapsed": True,
        "items": [
            {"text": "本卷首页", "link": f"/library/volume-{VOLUME:02d}/"},
            *({"text": name, "collapsed": name != "前置内容", "items": [
                {"text": item.title, "link": item.route} for item in items
            ]} for name, items in groups),
        ],
    }]
    catalog = [{
        "title": BOOK_TITLE,
        "fullTitle": BOOK_TITLE,
        "volumeLabel": "新增卷",
        "author": AUTHOR,
        "translator": TRANSLATORS,
        "isbn": "978-7-301-26938-1 / 978-7-301-27027-1",
        "link": f"/library/volume-{VOLUME:02d}/",
        "firstPage": sections[0].route,
        "pageCount": len(sections),
    }]
    stats = {"volumeCount": 1, "pageCount": len(sections), "characterCount": character_count}
    module = ROOT / "docs" / ".vitepress" / "library.additional.mjs"
    module.write_text(
        "// 此文件由 scripts/import-global-history.py 生成。\n"
        f"export const additionalLibrarySidebar = {json.dumps(sidebar, ensure_ascii=False, indent=2)}\n\n"
        f"export const additionalLibraryCatalog = {json.dumps(catalog, ensure_ascii=False, indent=2)}\n\n"
        f"export const additionalLibraryStats = {json.dumps(stats, ensure_ascii=False, indent=2)}\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    pdf = pymupdf.open(args.pdf)
    if len(pdf) != 1259:
        raise ValueError(f"Expected the 1259-page edition, found {len(pdf)} pages")
    sections = sections_from_pdf(pdf)
    count, images = write_markdown(pdf, sections)
    write_index_and_nav(sections, count)
    subprocess.run(["node", str(ROOT / "scripts" / "rebuild-library-index.mjs")], check=True)
    asset_dir = ROOT / "docs" / "public" / "library" / f"volume-{VOLUME:02d}" / "images"
    missing = [name for name in images if not (asset_dir / name).exists()]
    print(f"Imported {len(sections)} reading pages, {count:,} source characters, {len(images)} images")
    if missing:
        print(f"Image assets still missing: {len(missing)} (run extract-global-history-images.py)", file=sys.stderr)


if __name__ == "__main__":
    main()
