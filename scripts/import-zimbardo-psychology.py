"""Import the Chinese eighth edition of Zimbardo's psychology textbook.

Usage: python scripts/import-zimbardo-psychology.py path/to/book.pdf

Requires PyMuPDF. The source PDF stays outside the repository. Run
extract-zimbardo-images.py with the same PDF before building the site.
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

import pymupdf


ROOT = Path(__file__).resolve().parents[1]
VOLUME = 84
VOLUME_DIR = ROOT / "docs" / "library" / f"volume-{VOLUME:02d}"
IMAGE_DIR = ROOT / "docs" / "public" / "library" / f"volume-{VOLUME:02d}" / "images"
TITLE = "津巴多普通心理学（第8版）"
AUTHOR = "〔美〕菲利普·津巴多、罗伯特·约翰逊、薇薇安·麦卡恩"
TRANSLATOR = "傅小兰等"
ISBN = "978-7-115-58149-5"
NOTE_RE = re.compile(r"\[(\d+)\]")
CHAPTER_RE = re.compile(r"^第[一二三四五六七八九十]+章")


@dataclass
class Section:
    start: int  # Zero-based PDF page.
    title: str
    kind: str
    chapter: int = 0
    chapter_title: str = ""
    end: int = 0
    number: int = 0

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
    right: float
    bottom: float
    size: float = 0


@dataclass
class ChapterNotes:
    cut_page: int
    cut_y: float
    definitions: dict[str, str]


def compact(value: str) -> str:
    return re.sub(r"\s+", "", value)


def is_decorative_frame(block: dict) -> bool:
    # In this edition, the 1900px grayscale image blocks are empty backgrounds
    # behind separately extractable text. Rendering them alone creates blank,
    # dark-bordered rectangles in the reading view.
    return block["type"] == 1 and block["colorspace"] == 1 and block["width"] == 1900


def sections_from_pdf(pdf: pymupdf.Document) -> list[Section]:
    if len(pdf) != 1556:
        raise ValueError(f"Expected the 1556-page edition, found {len(pdf)} pages")
    sections: list[Section] = []
    chapter = 0
    chapter_title = ""
    for level, title, page1 in pdf.get_toc():
        if level == 1 and 19 <= page1 <= 1554:
            if CHAPTER_RE.match(title):
                chapter += 1
                chapter_title = title
                kind = "chapter"
            elif page1 < 36:
                kind = "front"
            else:
                kind = "back"
                chapter = 0
                chapter_title = ""
            sections.append(Section(page1 - 1, title, kind, chapter, chapter_title))
        elif level == 2 and 36 <= page1 < 1474 and chapter:
            sections.append(Section(page1 - 1, title, "subchapter", chapter, chapter_title))
    sections.sort(key=lambda item: item.start)
    for i, section in enumerate(sections):
        section.number = i + 1
        section.end = sections[i + 1].start if i + 1 < len(sections) else len(pdf)
        if section.end <= section.start:
            raise ValueError(f"Overlapping bookmarks near {section.title}")
    counts = (sum(s.kind == "front" for s in sections),
              sum(s.kind == "chapter" for s in sections),
              sum(s.kind == "subchapter" for s in sections),
              sum(s.kind == "back" for s in sections))
    if counts != (4, 14, 79, 6) or sections[0].start != 18:
        raise ValueError(f"Unexpected book outline: {counts}")
    return sections


def events_for_page(page: pymupdf.Page, page0: int) -> list[Event]:
    events: list[Event] = []
    image_index = 0
    for block in page.get_text("dict")["blocks"]:
        if block["type"] == 1:
            image_index += 1
            if is_decorative_frame(block):
                continue
            x0, y0, x1, y1 = block["bbox"]
            events.append(Event("image", f"p{page0 + 1:04d}-{image_index:02d}.webp",
                                page0, x0, y0, x1, y1))
            continue
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            value = "".join(span["text"] for span in line["spans"]).strip()
            if not value:
                continue
            size = max(span["size"] for span in line["spans"])
            kind = "title" if size >= 24 else "heading" if size >= 18 else "caption" if size < 14 else "body"
            x0, y0, x1, y1 = line["bbox"]
            events.append(Event(kind, value, page0, x0, y0, x1, y1, size))

    # Each chapter introduction begins with a large initial character. It is on
    # the same printed line as the first body line, but appears as a separate PDF
    # text block. Join it before applying paragraph boundaries.
    dropped: set[int] = set()
    for index, event in enumerate(events):
        if event.kind != "title" or len(event.text) != 1 or event.size < 35:
            continue
        choices = [(i, other) for i, other in enumerate(events)
                   if i != index and other.kind == "body" and other.x > event.x
                   and abs(other.y - event.y) <= 10]
        if choices:
            _, other = min(choices, key=lambda item: item[1].x)
            other.text = event.text + other.text
            dropped.add(index)
    return sorted((event for i, event in enumerate(events) if i not in dropped),
                  key=lambda event: (event.y, event.x))


def needs_latin_space(left: str, right: str) -> bool:
    if not left or not right or not right[0].isascii() or not right[0].isalnum():
        return False
    return bool(left[-1].isascii() and left[-1].isalnum()
                or left[-1] in ",.;:!?，。’”)]}©®")


def join_lines(left: str, right: str) -> str:
    return left + (" " if needs_latin_space(left, right) else "") + right


def chapter_notes(pdf: pymupdf.Document, sections: list[Section]) -> dict[int, ChapterNotes]:
    result: dict[int, ChapterNotes] = {}
    chapters = [section for section in sections if section.kind == "chapter"]
    for i, section in enumerate(chapters):
        end = chapters[i + 1].start if i + 1 < len(chapters) else next(
            section.start for section in sections if section.kind == "back")
        tail = [event for page0 in range(max(section.start, end - 4), end)
                for event in events_for_page(pdf[page0], page0) if event.kind != "image"]
        starts = [(index, NOTE_RE.match(event.text)) for index, event in enumerate(tail)
                  if event.x < 110 and NOTE_RE.match(event.text)]
        if not starts:
            continue
        cut_index = starts[0][0]
        definitions: dict[str, str] = {}
        number = ""
        for event in tail[cut_index:]:
            match = NOTE_RE.match(event.text)
            if match and event.x < 110:
                number = match.group(1)
                if number in definitions:
                    raise ValueError(f"Duplicate note {number} in chapter {section.chapter}")
                definitions[number] = event.text[match.end():].strip()
            elif number:
                definitions[number] = join_lines(definitions[number], event.text)
        first = tail[cut_index]
        result[section.chapter] = ChapterNotes(first.page, first.y, definitions)
    return result


def skipped_title_events(events: list[Event], section: Section) -> set[int]:
    skipped: set[int] = set()
    title = compact(section.title)
    pending = ""
    for index, event in enumerate(events):
        if event.kind in ("image", "caption"):
            continue
        if event.kind not in ("title", "heading"):
            break
        candidate = pending + compact(event.text)
        if not title.startswith(candidate):
            break
        skipped.add(index)
        pending = candidate
        if pending == title:
            return skipped
    return set()


def escape_leading_markdown(value: str) -> str:
    if re.match(r"^[#>*+\-]", value):
        return "\\" + value
    return value


def section_body(
    pdf: pymupdf.Document,
    section: Section,
    notes: dict[int, ChapterNotes],
    note_routes: dict[int, str],
    references: defaultdict[tuple[int, str], list[tuple[str, str]]],
) -> tuple[str, set[str], int]:
    nodes: list[tuple[str, str]] = []
    paragraph = ""
    paragraph_kind = ""
    previous: Event | None = None
    images: set[str] = set()
    character_count = 0

    def flush() -> None:
        nonlocal paragraph, paragraph_kind
        if paragraph:
            nodes.append((paragraph_kind, paragraph))
        paragraph = ""
        paragraph_kind = ""

    for page0 in range(section.start, section.end):
        page = pdf[page0]
        character_count += len(re.sub(r"\s", "", page.get_text()))
        events = events_for_page(page, page0)
        skipped = skipped_title_events(events, section) if page0 == section.start else set()
        chapter_note = notes.get(section.chapter)
        for index, event in enumerate(events):
            if chapter_note and (page0 > chapter_note.cut_page or
                                 page0 == chapter_note.cut_page and event.y >= chapter_note.cut_y):
                continue
            if index in skipped:
                continue
            if event.kind == "image":
                flush()
                images.add(event.text)
                nodes.append(("image", f"![原书插图（PDF 第{page0 + 1}页）]"
                              f"(/library/volume-{VOLUME:02d}/images/{event.text})"))
                previous = event
                continue
            if event.kind in ("title", "heading"):
                flush()
                if (nodes and nodes[-1][0] == event.kind and previous
                    and previous.kind == event.kind and previous.page == page0
                    and previous.right > 445 and event.y - previous.bottom < 25):
                    nodes[-1] = (event.kind, join_lines(nodes[-1][1], event.text))
                else:
                    nodes.append((event.kind, event.text))
                previous = event
                continue
            start_new = (
                not paragraph or paragraph_kind != event.kind or previous is None
                or previous.kind not in ("body", "caption")
                or event.kind == "body" and event.x >= 100 and not (
                    previous and previous.kind == "body" and previous.page == page0
                    and previous.right > 500 and event.y - previous.bottom < 12
                    and (previous.x >= 100 and abs(previous.x - event.x) < 5
                         or previous.x >= 125 and 100 <= event.x <= 115))
                or event.kind == "body" and re.match(r"^\d+\.\d+\s", event.text)
                or previous.page == page0 and event.y - previous.bottom > 18
                or event.kind == "caption" and event.text.startswith(("图", "表", "注："))
            )
            if start_new:
                flush()
                paragraph_kind = event.kind
                paragraph = event.text
            else:
                paragraph = join_lines(paragraph, event.text)
            previous = event
    flush()

    def link_reference(match: re.Match[str]) -> str:
        number = match.group(1)
        chapter_note = notes.get(section.chapter)
        if not chapter_note or number not in chapter_note.definitions:
            return match.group(0)
        key = (section.chapter, number)
        ref_id = f"note-ref-{number}-{len(references[key]) + 1}"
        references[key].append((section.route, ref_id))
        target = note_routes[section.chapter]
        href = f"#note-{number}" if target == section.route else f"./chapter-{int(target[-3:]):03d}#note-{number}"
        return (f'<sup class="footnote-ref" id="{ref_id}">'
                f'<a href="{href}" aria-label="查看本章注释 {number}">[{number}]</a></sup>')

    output: list[str] = []
    for index, (kind, value) in enumerate(nodes):
        if kind == "image":
            caption = ""
            for next_kind, text in nodes[index + 1:index + 4]:
                if next_kind not in ("image", "caption"):
                    break
                if next_kind == "caption" and not text.startswith("注："):
                    caption = text
                    break
            if caption:
                caption = caption[:110].replace("[", "［").replace("]", "］")
                value = value.replace("原书插图", caption, 1)
            output.append(value)
        elif kind in ("title", "heading"):
            prefix = "###" if re.match(r"^\d+\.\d+\.\d+\s", value) else "##"
            output.append(f"{prefix} {value}")
        elif kind == "caption":
            output.append(f"*{escape_leading_markdown(NOTE_RE.sub(link_reference, value))}*")
        else:
            output.append(escape_leading_markdown(NOTE_RE.sub(link_reference, value)))

    if section.kind == "subchapter" and section.chapter in notes and section.route == note_routes[section.chapter]:
        output.append("## 注释")
        for number, value in notes[section.chapter].definitions.items():
            backrefs = []
            for origin, ref_id in references[(section.chapter, number)]:
                href = f"#{ref_id}" if origin == section.route else f"./chapter-{int(origin[-3:]):03d}#{ref_id}"
                backrefs.append(f'<a class="footnote-backref" href="{href}" aria-label="返回注释 {number} 的引用">↩</a>')
            backref_html = f' <span class="footnote-backrefs">{" ".join(backrefs)}</span>' if backrefs else ""
            output.append(f'<p class="footnote-definition footnote-source" id="note-{number}">'
                          f'<a class="footnote-number" href="#note-{number}">[{number}]</a>'
                          f'{html.escape(value)}{backref_html}</p>')
    return "\n\n".join(output), images, character_count


def grouped_sections(sections: list[Section]) -> list[tuple[str, list[Section]]]:
    groups: list[tuple[str, list[Section]]] = []
    current_name = "前置内容"
    current: list[Section] = []
    for section in sections:
        if section.kind == "chapter" or section.kind == "back" and current_name != "附录":
            if current:
                groups.append((current_name, current))
            current_name = section.title if section.kind == "chapter" else "附录"
            current = []
        current.append(section)
    if current:
        groups.append((current_name, current))
    return groups


def write_site_metadata(sections: list[Section], character_count: int) -> None:
    groups = grouped_sections(sections)
    lines = ["---", f"title: {json.dumps(TITLE, ensure_ascii=False)}",
             f"description: {json.dumps(f'{AUTHOR}著，{TRANSLATOR}译。正文、图表及术语表。', ensure_ascii=False)}",
             "---", "", f"# {TITLE}", "", f"{AUTHOR}著，{TRANSLATOR}译。", "",
             f"[开始阅读 →]({sections[0].route})", "", "## 目录", ""]
    for group_name, items in groups:
        lines.append(f"### {group_name}")
        lines += [f"- [{item.title}]({item.route})" for item in items]
        lines.append("")
    (VOLUME_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")
    sidebar = [{"text": TITLE, "collapsed": True, "items": [
        {"text": "本卷首页", "link": f"/library/volume-{VOLUME:02d}/"},
        *({"text": group_name, "collapsed": group_name != "前置内容",
           "items": [{"text": item.title, "link": item.route} for item in items]}
          for group_name, items in groups),
    ]}]
    catalog = [{"title": TITLE, "fullTitle": TITLE, "volumeLabel": "新增卷",
                "author": AUTHOR, "translator": TRANSLATOR, "isbn": ISBN,
                "link": f"/library/volume-{VOLUME:02d}/", "firstPage": sections[0].route,
                "pageCount": len(sections)}]
    stats = {"volumeCount": 1, "pageCount": len(sections), "characterCount": character_count}
    module = ROOT / "docs" / ".vitepress" / "library.psychology.mjs"
    module.write_text(
        "// 此文件由 scripts/import-zimbardo-psychology.py 生成。\n"
        f"export const psychologyLibrarySidebar = {json.dumps(sidebar, ensure_ascii=False, indent=2)}\n\n"
        f"export const psychologyLibraryCatalog = {json.dumps(catalog, ensure_ascii=False, indent=2)}\n\n"
        f"export const psychologyLibraryStats = {json.dumps(stats, ensure_ascii=False, indent=2)}\n",
        encoding="utf-8")
    subprocess.run(["node", "scripts/rebuild-library-index.mjs"], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    pdf = pymupdf.open(args.pdf)
    sections = sections_from_pdf(pdf)
    notes = chapter_notes(pdf, sections)
    note_routes = {chapter: next(s.route for s in reversed(sections) if s.chapter == chapter and s.kind == "subchapter")
                   for chapter in notes}
    VOLUME_DIR.mkdir(parents=True, exist_ok=True)
    for old in VOLUME_DIR.glob("chapter-*.md"):
        old.unlink()
    images: set[str] = set()
    references: defaultdict[tuple[int, str], list[tuple[str, str]]] = defaultdict(list)
    character_count = 0
    for section in sections:
        body, names, count = section_body(pdf, section, notes, note_routes, references)
        if not body:
            raise ValueError(f"No content for {section.title}")
        images.update(names)
        character_count += count
        description = f"{TITLE} · {section.chapter_title} · {section.title}" if section.chapter_title and section.chapter_title != section.title else f"{TITLE} · {section.title}"
        markdown = (f"---\ntitle: {json.dumps(section.title, ensure_ascii=False)}\n"
                    f"description: {json.dumps(description, ensure_ascii=False)}\n---\n\n"
                    f'<p class="reading-meta"><a href="./">{TITLE}</a>'
                    f'{" · " + section.chapter_title if section.chapter_title else ""}</p>\n\n'
                    f"# {section.title}\n\n{body}\n")
        (VOLUME_DIR / f"chapter-{section.number:03d}.md").write_text(markdown, encoding="utf-8")
    write_site_metadata(sections, character_count)
    missing = sorted(name for name in images if not (IMAGE_DIR / name).is_file())
    print(f"Imported {len(sections)} pages, {character_count:,} source characters, "
          f"{len(images)} images, {sum(len(n.definitions) for n in notes.values())} notes, "
          f"{sum(map(len, references.values()))} note references")
    if missing:
        print(f"Image assets still missing: {len(missing)} (run extract-zimbardo-images.py)")


if __name__ == "__main__":
    main()
