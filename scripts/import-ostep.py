"""Import the Chinese edition of Operating Systems: Three Easy Pieces.

Usage: python scripts/import-ostep.py path/to/OSTEP-中文版.pdf [--pages A-B --debug]

The source is the 498-page Chinese edition (王海鹏 译, 人民邮电出版社) as
merged from the chapter PDFs the authors host at
https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/. The PDF stays outside the
repository; scripts/ostep-source-manifest.json records its checksum.

Requires PyMuPDF, fontTools and Pillow, plus the Windows SimSun/SimHei fonts:
the PDF's ToUnicode maps for those fonts are wrong in about 600 places (for
example 在 extracts as 谁, 们 as 我), so their text is rebuilt from glyph IDs,
which match the installed fonts.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import hashlib
import html
import io
import json
from pathlib import Path
import re
import subprocess

import pymupdf
from fontTools.ttLib import TTCollection, TTFont
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VOLUME = 89
VOLUME_DIR = ROOT / "docs" / "library" / f"volume-{VOLUME:02d}"
IMAGE_DIR = ROOT / "docs" / "public" / "library" / f"volume-{VOLUME:02d}" / "images"
IMAGE_ROUTE = f"/library/volume-{VOLUME:02d}/images"
MANIFEST = ROOT / "scripts" / "ostep-source-manifest.json"
REVIEWED_LAYOUT = ROOT / "scripts" / "ostep-reviewed-layout.json"
TITLE = "操作系统导论"
AUTHOR = "〔美〕雷姆兹·H. 阿帕希-杜塞尔、安德莉亚·C. 阿帕希-杜塞尔"
TRANSLATOR = "王海鹏"
SOURCE_URL = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
PAGE_COUNT = 498
SKIPPED = {"扉页", "内容提要", "资源与支持", "目录"}

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩"
CAPTION_RE = re.compile(r"^(图|表)\s*([0-9A-G]+\.\d+)")
CJK_RE = re.compile(r"[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]")
CODE_FONT = "CourierNew"
BOLD_FONTS = ("FZHTJW", "SimHei")
CALLOUT_GRAY = 0.85
# Body-size text that ends up inside a figure crop, for review.
AUDIT: list[str] = []


# --------------------------------------------------------------------------
# Glyph repair


def _reverse_cmap(font) -> dict[int, str]:
    reverse: dict[int, set[str]] = defaultdict(set)
    for codepoint, glyph in font.getBestCmap().items():
        reverse[font.getGlyphID(glyph)].add(chr(codepoint))
    return {gid: min(chars) for gid, chars in reverse.items()}


class GlyphRepair:
    """Map SimSun/SimHei glyph IDs back to characters via the system fonts."""

    def __init__(self) -> None:
        fonts = Path("C:/Windows/Fonts")
        self.maps = {
            "SimSun": _reverse_cmap(TTCollection(str(fonts / "simsun.ttc")).fonts[0]),
            "SimHei": _reverse_cmap(TTFont(str(fonts / "simhei.ttf"))),
        }
        self.repaired = 0

    def page_fixes(self, page: pymupdf.Page) -> dict[tuple[float, float], str]:
        fixes: dict[tuple[float, float], str] = {}
        for span in page.get_texttrace():
            table = self.maps.get(span["font"])
            if not table:
                continue
            for codepoint, gid, origin, _bbox in span["chars"]:
                char = chr(codepoint)
                fixed = table.get(gid)
                # Only CJK glyphs are wrong; Latin glyph IDs differ between
                # SimSun versions and their ToUnicode entries are correct.
                if fixed and fixed != char and CJK_RE.match(char) and CJK_RE.match(fixed):
                    fixes[(round(origin[0], 2), round(origin[1], 2))] = fixed
        return fixes


# --------------------------------------------------------------------------
# Page model


@dataclass
class Span:
    text: str
    font: str
    size: float
    flags: int
    bbox: tuple[float, float, float, float]
    chars: list[tuple[str, float]]  # (char, x0) for code layout

    @property
    def is_code(self) -> bool:
        return self.font.startswith(CODE_FONT)


@dataclass
class Line:
    page: int
    bbox: tuple[float, float, float, float]
    spans: list[Span]

    @property
    def text(self) -> str:
        return "".join(span.text for span in self.spans)

    @property
    def x0(self) -> float:
        return self.bbox[0]

    @property
    def y0(self) -> float:
        return self.bbox[1]

    @property
    def x1(self) -> float:
        return self.bbox[2]

    @property
    def y1(self) -> float:
        return self.bbox[3]

    @property
    def visible(self) -> list[Span]:
        return [span for span in self.spans if span.text.strip()]

    @property
    def size(self) -> float:
        # Subscripts and note marks never set the line's size, even when they
        # outnumber the characters they hang from (as in "Tc1").
        largest = max((span.size for span in self.visible), default=0)
        sizes = Counter()
        for span in self.visible:
            if span.size >= largest * 0.8:
                sizes[round(span.size, 1)] += len(span.text.strip())
        return sizes.most_common(1)[0][0] if sizes else 0

    @property
    def first(self) -> Span:
        return self.visible[0]

    @property
    def is_code(self) -> bool:
        # SimSun supplies the caret in "ˆC" inside otherwise Courier listings.
        chars = [(span.is_code or span.text.strip() == "ˆ", len(span.text.strip())) for span in self.visible]
        code = sum(n for is_code, n in chars if is_code)
        return code > 0 and code * 2 >= sum(n for _, n in chars) and chars[0][0]


@dataclass
class Graphic:
    rect: pymupdf.Rect


@dataclass
class Figure:
    page: int
    rect: pymupdf.Rect
    caption: str = ""
    kind: str = "图"  # 图, 表 or 插图
    caption_above: bool = False
    full_width: bool = True
    image: str = ""
    table: list[list[str]] | None = None
    markdown: str = ""
    caption_rect: pymupdf.Rect | None = None

    @property
    def extent(self) -> pymupdf.Rect:
        """The area body text wraps around: the figure and its caption."""
        return self.rect | self.caption_rect if self.caption_rect else self.rect

    @property
    def y(self) -> float:
        return self.rect.y0


@dataclass
class Callout:
    rect: pymupdf.Rect
    page: int


@dataclass
class PageModel:
    number: int
    lines: list[Line]
    figures: list[Figure]
    callouts: list[Callout]
    notes: list[Line]
    left: float


def rect_of(bbox) -> pymupdf.Rect:
    return pymupdf.Rect(bbox)


def overlaps(a: pymupdf.Rect, b: pymupdf.Rect, pad: float = 0) -> bool:
    return (a.x0 - pad < b.x1 and b.x0 - pad < a.x1 and
            a.y0 - pad < b.y1 and b.y0 - pad < a.y1)


def inside(line: Line, rect: pymupdf.Rect, pad: float = 2) -> bool:
    cx = (line.x0 + line.x1) / 2
    cy = (line.y0 + line.y1) / 2
    return rect.x0 - pad <= cx <= rect.x1 + pad and rect.y0 - pad <= cy <= rect.y1 + pad


def merge_rects(rects: list[pymupdf.Rect], gap: float) -> list[pymupdf.Rect]:
    groups = [pymupdf.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        result: list[pymupdf.Rect] = []
        for rect in groups:
            for index, other in enumerate(result):
                if overlaps(rect, other, gap):
                    result[index] = other | rect
                    changed = True
                    break
            else:
                result.append(pymupdf.Rect(rect))
        groups = result
    return groups


def read_lines(page: pymupdf.Page, number: int, repair: GlyphRepair) -> list[Line]:
    fixes = repair.page_fixes(page)
    lines: list[Line] = []
    raw = page.get_text("rawdict", flags=pymupdf.TEXT_PRESERVE_WHITESPACE)
    for block in raw["blocks"]:
        if block["type"] != 0:
            continue
        for raw_line in block["lines"]:
            if abs(raw_line["dir"][1]) > 0.1:
                continue  # Rotated axis labels live inside figures.
            spans = []
            for raw_span in raw_line["spans"]:
                chars = []
                for char in raw_span["chars"]:
                    key = (round(char["origin"][0], 2), round(char["origin"][1], 2))
                    value = fixes.get(key, char["c"])
                    if value != char["c"]:
                        repair.repaired += 1
                    chars.append((value, char["bbox"][0]))
                text = "".join(c for c, _ in chars)
                if not text:
                    continue
                spans.append(Span(text, raw_span["font"].split("+")[-1], raw_span["size"],
                                  raw_span["flags"], tuple(raw_span["bbox"]), chars))
            visible = "".join(s.text for s in spans).strip()
            width = raw_line["bbox"][2] - raw_line["bbox"][0]
            # Hidden text (a 1pt-wide copy of the running head) is not content.
            if visible and width >= 0.3 * len(visible) * min(s.size for s in spans):
                lines.append(Line(number, tuple(raw_line["bbox"]), spans))
    # Word's PDF export splits one visual line into several pieces and puts
    # footnote marks on their own, higher baseline. Group pieces that overlap
    # vertically into rows, then rejoin the horizontally adjacent pieces.
    rows: list[list[Line]] = []
    for line in sorted(lines, key=lambda piece: (piece.y0 + piece.y1) / 2):
        for row in reversed(rows[-4:]):
            main = max(row, key=lambda piece: piece.size)
            overlap = min(main.y1, line.y1) - max(main.y0, line.y0)
            if overlap >= 0.5 * min(main.y1 - main.y0, line.y1 - line.y0):
                row.append(line)
                break
        else:
            rows.append([line])
    merged: list[Line] = []
    for row in rows:
        row.sort(key=lambda piece: piece.x0)
        current = row[0]
        for line in row[1:]:
            # Side-by-side captions and captions beside wrapped text share the
            # body row but stand apart from it; table captions put the number
            # and the title far apart on purpose.
            adjacent = line.x0 - current.x1 < 15 or re.fullmatch(r"\s*表\s*[0-9A-G]+\.\d+\s*", current.text)
            # Footnote marks are tiny superscripts; anything else must match
            # the type size, which keeps 9pt captions out of 10.5pt body text.
            similar = abs(current.size - line.size) < 1.5 or min(current.size, line.size) < 7.5
            # Code keeps its trailing comments, which sit in a column far right.
            code = current.is_code and line.is_code
            # Full-width punctuation boxes can overlap the next piece a little.
            if (adjacent or code) and similar and line.x0 >= current.x1 - 10 and current.is_code == line.is_code:
                current.spans.extend(line.spans)
                current.bbox = (current.x0, min(current.y0, line.y0), max(current.x1, line.x1),
                                max(current.y1, line.y1))
            else:
                merged.append(current)
                current = line
        merged.append(current)
    merged.sort(key=lambda line: (round(line.y1), line.x0))
    return [piece for line in merged for piece in split_captions(line)]


def split_captions(line: Line) -> list[Line]:
    """Side-by-side figures can share one text line for both captions."""
    text = line.text
    starts = [m.start() for m in re.finditer(r"(?<=\s)(图|表)\s*[0-9A-G]+\.\d+", text)]
    if not starts or not CAPTION_RE.match(text.strip()) or line.size > 9.6:
        return [line]
    pieces: list[list[Span]] = [[] for _ in range(len(starts) + 1)]
    offset = 0
    for span in line.spans:
        for index, (char, x0) in enumerate(span.chars):
            piece = sum(1 for start in starts if offset >= start)
            end = span.chars[index + 1][1] if index + 1 < len(span.chars) else span.bbox[2]
            target = pieces[piece]
            if target and getattr(target[-1], "_source", None) is span:
                last = target[-1]
                last.text += char
                last.chars.append((char, x0))
                last.bbox = (last.bbox[0], last.bbox[1], end, last.bbox[3])
            else:
                piece_span = Span(char, span.font, span.size, span.flags,
                                  (x0, span.bbox[1], end, span.bbox[3]), [(char, x0)])
                piece_span._source = span
                target.append(piece_span)
            offset += 1
    result = []
    for spans in pieces:
        if spans and "".join(s.text for s in spans).strip():
            visible = [s for s in spans if s.text.strip()]
            bbox = (visible[0].bbox[0], line.y0, visible[-1].bbox[2], line.y1)
            result.append(Line(line.page, bbox, spans))
    return result


def is_caption(line: Line) -> bool:
    return bool(CAPTION_RE.match(line.text.strip())) and line.size <= 9.6


def is_small(line: Line) -> bool:
    return line.size <= 9.6 and not line.is_code


def build_page(pdf: pymupdf.Document, number: int, repair: GlyphRepair,
               overrides: dict) -> PageModel:
    page = pdf[number]
    lines = [line for line in read_lines(page, number, repair) if line.y1 > 60]

    note_top = None
    separators: list[pymupdf.Rect] = []
    callout_rects = []
    graphics: list[pymupdf.Rect] = []
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"])
        fill = drawing.get("fill")
        if rect.y1 <= 60:
            continue
        if fill and min(fill) > 0.98 and not drawing.get("color"):
            continue  # White page backgrounds.
        if (fill and max(fill) < 0.2 and rect.height <= 1.5 and 60 <= rect.width <= 120 and
                rect.x0 < 60 and rect.y0 > 300):
            separators.append(rect)
        if fill and abs(fill[0] - CALLOUT_GRAY) < 0.02 and rect.width > 380:
            callout_rects.append(rect)
            continue
        if rect.width < 0.3 and rect.height < 0.3:
            continue
        graphics.append(rect)
    for rect in separators:
        # The footnote rule stands alone; table rules continue to the right.
        alone = not any(abs(other.y0 - rect.y0) < 3 and other.x0 > rect.x1 - 1 for other in graphics)
        starts_note = any(line.y0 > rect.y0 and line.text.strip()[:1] in CIRCLED for line in lines
                          if line.y0 < rect.y0 + 20)
        if alone and starts_note:
            note_top = rect.y0
        else:
            graphics.append(rect)
    for info in page.get_image_info():
        rect = pymupdf.Rect(info["bbox"])
        if rect.y1 > 60 and rect.width * rect.height > 0:
            graphics.append(rect)

    notes: list[Line] = []
    if note_top is not None:
        notes = [line for line in lines if line.y0 >= note_top - 1]
        lines = [line for line in lines if line.y0 < note_top - 1]
        graphics = [rect for rect in graphics if rect.y0 < note_top - 1]

    callouts = [Callout(rect, number) for rect in merge_rects(callout_rects, 1)]
    # Figures drawn inside a callout keep their own graphics; the callout's
    # gray fill never counts as a figure.
    clusters = merge_rects(graphics, 10)

    figures: list[Figure] = []
    claimed: set[int] = set()
    # Reviewed formulas replace whatever the text layer and drawings hold.
    for item in overrides.get("blocks", {}).get(str(number + 1), []):
        rect = pymupdf.Rect(item["rect"])
        figures.append(Figure(number, rect, kind="markdown", markdown=item["markdown"]))
        claimed |= {index for index, cluster in enumerate(clusters) if overlaps(cluster, rect)}
    # Figure captions claim their drawings before tables grow downwards.
    captions = sorted((line for line in lines if is_caption(line)),
                      key=lambda line: line.text.strip().startswith("表"))
    caption_ids = {id(line) for line in captions}

    def bounds(caption: Line, kind: str) -> tuple[float, float]:
        """A figure never reaches past the neighbouring caption."""
        others = [other for other in captions if other is not caption]
        if kind == "图":
            return max((o.y1 for o in others if o.y1 <= caption.y0 + 1), default=0), caption.y0
        return caption.y1, min((o.y0 for o in others if o.y0 >= caption.y1 - 1), default=page.rect.y1)

    def grow(region: pymupdf.Rect, direction: str, lo: float = 0, hi: float = 10_000,
             band: tuple[float, float] = (0, 10_000)) -> pymupdf.Rect:
        changed = True
        while changed:
            changed = False
            for index, cluster in enumerate(clusters):
                if index in claimed or cluster.y0 < lo - 1 or cluster.y1 > hi + 1:
                    continue
                if cluster.x0 < band[0] or cluster.x1 > band[1]:
                    continue  # a narrow chart never swallows a full-width table
                horizontal = cluster.x0 < region.x1 + 10 and region.x0 - 10 < cluster.x1
                near = (region.y0 - 25 <= cluster.y1 <= region.y1 + 2 if direction == "up"
                        else region.y0 - 2 <= cluster.y0 <= region.y1 + 25)
                if horizontal and (near or overlaps(cluster, region, 2)):
                    region |= cluster
                    claimed.add(index)
                    changed = True
        return region

    def absorb_labels(region: pymupdf.Rect, lo: float = 0, hi: float = 10_000) -> pymupdf.Rect:
        changed = True
        while changed:
            changed = False
            for line in lines:
                if id(line) in caption_ids or inside(line, region, 0):
                    continue
                if not is_small(line) or line.y0 < lo - 1 or line.y1 > hi + 1:
                    continue
                if overlaps(rect_of(line.bbox), region, 6):
                    region |= rect_of(line.bbox)
                    changed = True
        return region

    for caption in captions:
        # A caption beside wrapped text can run onto a second, centred line.
        # (Table captions sit above the table, whose header row comes next.)
        if caption.text.strip().startswith("表"):
            continue
        follower = next((line for line in lines if line is not caption and not is_caption(line) and
                         is_small(line) and 0 <= line.y0 - caption.y1 < 6 and
                         line.x0 >= caption.x0 - 30 and line.x1 <= caption.x1 + 30), None)
        if follower is not None:
            if CJK_RE.match(follower.text.strip()[:1]):
                caption.spans[-1].text = caption.spans[-1].text.rstrip()
            caption.spans.extend(follower.spans)
            caption.bbox = (min(caption.x0, follower.x0), caption.y0, max(caption.x1, follower.x1), follower.y1)
            lines.remove(follower)

    for caption in captions:
        kind = CAPTION_RE.match(caption.text.strip()).group(1)
        crect = rect_of(caption.bbox)
        lo, hi = bounds(caption, kind)
        best = None
        for index, cluster in enumerate(clusters):
            if index in claimed or cluster.y0 < lo - 1 or cluster.y1 > hi + 1:
                continue
            cx = (crect.x0 + crect.x1) / 2
            if not (cluster.x0 - 20 <= cx <= cluster.x1 + 20):
                continue
            if kind == "图":
                distance = crect.y0 - cluster.y1
            else:
                distance = cluster.y0 - crect.y1
            if -4 <= distance <= 40 and (best is None or distance < best[0]):
                best = (distance, index)
        if best is None:
            continue  # Code listings and text-only figures stay as text.
        claimed.add(best[1])
        direction = "up" if kind == "图" else "down"
        start = clusters[best[1]]
        band = (min(start.x0, crect.x0) - 60, max(start.x1, crect.x1) + 60)
        region = grow(pymupdf.Rect(start), direction, lo, hi, band)
        region = absorb_labels(region, lo, hi)
        region = grow(region, direction, lo, hi, band)
        figures.append(Figure(number, region, caption.text.strip(), kind,
                              caption_above=kind == "表",
                              full_width=region.x0 < 200 and region.x1 > 330,
                              caption_rect=pymupdf.Rect(crect)))
        caption_ids.discard(id(caption))
        caption.spans = [Span("\0caption", "", 0, 0, caption.bbox, [])]

    for index, cluster in enumerate(clusters):
        if index in claimed:
            continue
        if cluster.width < 15 or cluster.height < 6:
            continue  # Rules and underlines.
        claimed.add(index)
        region = absorb_labels(grow(pymupdf.Rect(cluster), "down"))
        figures.append(Figure(number, region, "", "插图", full_width=region.x0 < 200 and region.x1 > 330))

    # Tables whose layout defeats extraction (merged cells, two-level headers,
    # struck-out values) were transcribed by hand from the page images.
    reviewed_tables = overrides.get("tables", {})
    for figure in figures:
        label = re.sub(r"\s+", "", CAPTION_RE.match(figure.caption).group(0)) if figure.caption else ""
        if label in reviewed_tables:
            figure.markdown = f"*{caption_markup(figure.caption)}*\n\n{mark_markdown_code(reviewed_tables[label])}"
        elif figure.kind in ("表", "插图"):
            figure.table = extract_table(page, figure.rect, lines)

    kept = []
    for line in lines:
        if line.spans and line.spans[0].text == "\0caption":
            continue
        holder = next((figure for figure in figures if inside(line, figure.rect)), None)
        if holder is not None:
            if line.size >= 10 and holder.table is None and not holder.markdown:
                AUDIT.append(f"PDF p{number + 1} {holder.kind} {[round(v) for v in holder.rect]}: {line.text.strip()[:60]}")
            continue
        kept.append(line)
    body = [line for line in kept if line.size >= 10]
    left = Counter(round(line.x0) for line in body).most_common(1)[0][0] if body else 55
    left = min(left, 56)
    return PageModel(number, kept, figures, callouts, notes, left)


def extract_table(page: pymupdf.Page, region: pymupdf.Rect, lines: list[Line]) -> list[list[str]] | None:
    """Rebuild a ruled grid as text; merged cells or stray text keep the image."""
    # Many tables draw column rules only in the header, so also try those
    # rules extended over every row, then columns aligned on the text.
    candidates = [
        lambda: found_grid(page, region, {"strategy": "lines"}),
        lambda: header_rule_grid(page, region),
        lambda: found_grid(page, region, {"vertical_strategy": "text", "horizontal_strategy": "lines"}),
    ]
    for candidate in candidates:
        rows = candidate()
        table = fill_table(rows, region, lines) if rows else None
        if table:
            return table
    return None


def found_grid(page: pymupdf.Page, region: pymupdf.Rect, options: dict) -> list[list[tuple]] | None:
    try:
        found = page.find_tables(clip=region + (-2, -2, 2, 2), **options)
    except Exception:
        return None
    if len(found.tables) != 1:
        return None
    return [row.cells for row in found.tables[0].rows]


def header_rule_grid(page: pymupdf.Page, region: pymupdf.Rect) -> list[list[tuple]] | None:
    xs: set[float] = set()
    ys: set[float] = set()
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"])
        if not region.intersects(rect + (-2, -2, 2, 2)):
            continue
        if rect.width <= 1.5 and rect.height > 5:
            xs.add(round((rect.x0 + rect.x1) / 2))
        elif rect.height <= 1.5 and rect.width > 20:
            ys.add(round((rect.y0 + rect.y1) / 2))
    xs |= {round(region.x0), round(region.x1)}
    xs_sorted = [x for x in sorted(xs) if region.x0 - 3 <= x <= region.x1 + 3]
    xs_sorted = [x for i, x in enumerate(xs_sorted) if i == 0 or x - xs_sorted[i - 1] > 4]
    ys_sorted = [y for y in sorted(ys) if region.y0 - 3 <= y <= region.y1 + 3]
    ys_sorted = [y for i, y in enumerate(ys_sorted) if i == 0 or y - ys_sorted[i - 1] > 4]
    if len(xs_sorted) < 3 or len(ys_sorted) < 3:
        return None
    return [[(x0, y0, x1, y1) for x0, x1 in zip(xs_sorted, xs_sorted[1:])]
            for y0, y1 in zip(ys_sorted, ys_sorted[1:])]


def fill_table(rows: list[list[tuple]], region: pymupdf.Rect, lines: list[Line]) -> list[list[str]] | None:
    if (len(rows) < 2 or any(cell is None for row in rows for cell in row) or
            len({len(row) for row in rows}) != 1 or len(rows[0]) < 2):
        return None
    cells: list[list[list[tuple[Line, Span]]]] = [[[] for _ in row] for row in rows]
    for line in lines:
        if not inside(line, region, 2):
            continue
        for span in line.visible:
            cx = (span.bbox[0] + span.bbox[2]) / 2
            cy = (span.bbox[1] + span.bbox[3]) / 2
            target = next(((r, c) for r, row in enumerate(rows) for c, cell in enumerate(row)
                           if cell[0] - 1 <= cx <= cell[2] + 1 and cell[1] - 1 <= cy <= cell[3] + 1), None)
            if target is None:
                return None
            cells[target[0]][target[1]].append((line, span))
    if not any(cells_row for row in cells for cells_row in row):
        return None
    if any(not cell for cell in cells[0]):
        return None  # every column in this book has a heading
    for row in cells:
        for cell in row:
            # A missed column rule leaves two columns' text in one cell.
            by_line: dict[int, list] = defaultdict(list)
            for line, span in cell:
                by_line[id(line)].append(span.bbox)
            for boxes in by_line.values():
                boxes.sort(key=lambda box: box[0])
                if any(right[0] - left[2] > 12 for left, right in zip(boxes, boxes[1:])):
                    return None
    table = []
    for r, row in enumerate(cells):
        texts = []
        for c, cell in enumerate(row):
            right = rows[r][c][2]
            segments: list[list[Token]] = [[]]
            previous_line = None
            for line, span in sorted(cell, key=lambda item: (round(item[0].y1), item[1].bbox[0])):
                token = line_tokens(Line(line.page, line.bbox, [span]))
                token[0].style = span_style(span, line.size)
                if token[0].style == "small":
                    token[0].sub = (span.bbox[1] + span.bbox[3]) / 2 > (line.y0 + line.y1) / 2
                if previous_line is not None and previous_line is not line:
                    # Short lines in a cell are separate steps; full ones wrap.
                    ended = max(s.bbox[2] for l, s in cell if l is previous_line)
                    if ended < right - 2 * previous_line.size:
                        segments.append(token)
                    else:
                        segments[-1] = join_tokens(segments[-1], token)
                else:
                    segments[-1].extend(token)
                previous_line = line
            texts.append("<br>".join(render_tokens(segment) for segment in segments).replace("|", "\\|"))
        table.append(texts)
    return table


# --------------------------------------------------------------------------
# Markdown rendering


def escape_text(text: str) -> str:
    text = text.replace("\\", "\\\\")
    for char in "*_`$~":
        text = text.replace(char, "\\" + char)
    text = text.replace("<", "&lt;").replace("{{", "&#123;&#123;")
    return text


def escape_block_start(text: str) -> str:
    if re.match(r"^(#|>|[-+] |\d+[.)] |=+$|-+$|\|)", text):
        return "\\" + text
    return text


def span_style(span: Span, line_size: float, mixed: bool = False) -> str:
    font = span.font
    if span.is_code:
        return "code"
    if span.size < line_size * 0.8 and span.text.strip() in CIRCLED:
        return "noteref"
    if span.size < line_size * 0.8 and line_size >= 9:
        return "small"
    # 黑体 marks emphasis in body text; inside boxes it is 9pt like the box
    # titles, so there it only counts when mixed into a line of other fonts.
    if "Bold" in font or (font.startswith(BOLD_FONTS) and (span.size >= 10 or mixed)) or font.startswith("FZXBSJW"):
        return "bold"
    if "Italic" in font:
        return "italic"
    return ""


@dataclass
class Token:
    text: str
    style: str
    sub: bool = False


@dataclass
class Block:
    kind: str  # p, h2, h3, li, code, figure, callout-start, callout-end, break
    tokens: list[Token] = field(default_factory=list)
    text: str = ""
    figure: Figure | None = None
    lang: str = ""
    last_line: Line | None = None
    limit: float = 0
    code: bool = True  # mark inline code (not in reference lists)


def line_tokens(line: Line, notes: dict[str, int] | None = None) -> list[Token]:
    size = line.size
    mixed = any(not span.font.startswith(BOLD_FONTS + ("Webdings", "Wingdings")) and span.text.strip()
                for span in line.spans)
    tokens = []
    for span in line.spans:
        style = span_style(span, size, mixed)
        sub = False
        if style == "small":
            line_mid = (line.y0 + line.y1) / 2
            sub = (span.bbox[1] + span.bbox[3]) / 2 > line_mid
        if style == "noteref":
            for mark in span.text.strip():
                if notes is not None and mark in notes:
                    tokens.append(Token(str(notes[mark]), "noteref"))
                else:
                    tokens.append(Token(mark, ""))
            continue
        tokens.append(Token(span.text, style, sub))
    return tokens


def join_tokens(previous: list[Token], following: list[Token]) -> list[Token]:
    if not previous:
        return list(following)
    if not following:
        return previous
    left = previous[-1]
    right = following[0]
    left_text = left.text.rstrip()
    right_text = right.text.lstrip()
    tail = left_text[-1:] if left_text else ""
    head = right_text[:1]
    spaced = (left.text != left_text) and tail and head and not CJK_RE.match(tail) and not CJK_RE.match(head)
    need_space = (spaced and tail not in "_/-") or (tail.isascii() and tail.isalnum() and head.isascii() and head.isalnum())
    left.text = left_text + (" " if need_space else "")
    right.text = right_text
    return previous + list(following)


def render_tokens(tokens: list[Token], mark_code: bool = True, html_code: bool = False,
                  block_start: bool = True) -> str:
    merged: list[Token] = []
    for token in tokens:
        if not token.text:
            continue
        if merged and merged[-1].style == token.style and merged[-1].sub == token.sub and token.style != "noteref":
            merged[-1].text += token.text
        else:
            merged.append(Token(token.text, token.style, token.sub))

    def code_markup(core: str) -> str:
        if html_code:
            return f"<code>{html.escape(core)}</code>"
        ticks = "``" if "`" in core else "`"
        return f"{ticks}{core}{ticks}"

    pieces: list[tuple[str, bool]] = []  # (markup, is inline code)
    for token in merged:
        text = token.text
        if token.style == "noteref":
            number = token.text
            pieces.append((f'<sup class="footnote-ref" id="note-ref-{number}-1">'
                           f'<a href="#note-{number}" aria-label="查看本页注释 {number}">[{number}]</a></sup>', False))
            continue
        core = text.strip()
        if not core:
            pieces.append((" " if pieces else "", False))
            continue
        lead = " " if text[:1].isspace() else ""
        trail = " " if text[-1:].isspace() else ""
        if token.style == "code":
            pieces += [(lead, False), (code_markup(core), True), (trail, False)]
            continue
        if token.style == "bold":
            body = f"**{escape_text(core)}**"
        elif token.style == "italic" and re.search(r"\w", core):
            body = f"*{escape_text(core)}*"
        elif token.style == "small":
            tag = "sub" if token.sub else "sup"
            body = f"<{tag}>{html.escape(core)}</{tag}>"
        else:
            pieces.append((lead, False))
            for segment, is_code in split_code(core) if mark_code else [(core, False)]:
                pieces.append((code_markup(segment) if is_code else escape_text(segment), is_code))
            pieces.append((trail, False))
            continue
        pieces.append((lead + body + trail, False))

    # Inline code stands one space apart from the words around it; the
    # punctuation rules below then pull full-width punctuation back against it.
    out = ""
    after_code = False
    for markup, is_code in pieces:
        if not markup:
            continue
        if (is_code and out and SPACED_RE.match(out[-1])) or (after_code and SPACED_RE.match(markup[0])):
            out += " "
        out += markup
        after_code = is_code
    text = re.sub(r"[  ]{2,}", " ", out).strip()
    text = text.replace("I /O", "I/O")  # a stray space in the source text
    # Word inserts spaces around full-width punctuation at span joins.
    text = re.sub(r" +([，。；：、！？）」』”’])", r"\1", text)
    text = re.sub(r"([（「『“‘]) +", r"\1", text)
    # Bold/italic markers must hug their content for markdown-it.
    text = re.sub(r"\*\*\*\*", "", text)
    text = re.sub(r"(?<=[^\s*])\*\* \*\*(?=[^\s*])", " ", text)  # one bold run, not two
    return escape_block_start(text) if block_start else text


# Inline code in prose. The PDF sets identifiers in prose in the same Times
# face as English words, so code is recognised by its shape, plus per-chapter
# lists of plain-word identifiers (such as ticket or turn) found by reading
# each chapter.

SPACED_RE = re.compile(r"[A-Za-z0-9一-鿿]")
_PROSE = "　-〿一-鿿＀-￯“”‘’"
CODE_SHAPES = [
    # ./program -flag value …, or a run of flags and their values
    rf"(?:\./|(?<![A-Za-z0-9_/.\-])--?(?=[A-Za-z]))[^\s{_PROSE}]+(?: [^\s{_PROSE}]+)*",
    # calls: wait(), TestAndSet(flag, 1), malloc(strlen(s) + 1)
    rf"(?<![A-Za-z0-9_.>])[A-Za-z_]\w*(?:->[A-Za-z_]\w*)*\((?:[^()\n{_PROSE}]|\([^()\n{_PROSE}]*\))*\)",
    r"(?<![A-Za-z0-9_])[A-Za-z_]\w*(?:->[A-Za-z_]\w*)+",  # lock->turn
    r"(?<![A-Za-z0-9_])_*[A-Za-z][A-Za-z0-9]*(?:_+[A-Za-z0-9]+)+_?(?![A-Za-z0-9_])",  # O_CREAT
    r"(?<![A-Za-z0-9_./-])[A-Za-z0-9][\w.-]*\.(?:c|h|py|txt|o|out|sh|S|s|tmp)(?![A-Za-z0-9_])",  # cpu.c
    r"(?<![A-Za-z0-9_>)/])/(?=[A-Za-z0-9_./-]*[A-Za-z][A-Za-z0-9_./-]*[A-Za-z0-9_.-])"
    r"(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+/?",  # /tmp/file, not N/2 or a split I /O
    r"(?<![A-Za-z0-9_])%[a-z]{2,3}(?![A-Za-z0-9_])",  # %eax
    r"(?<![A-Za-z0-9_])\$?0x[0-9a-fA-F]+(?![A-Za-z0-9_])",  # 0x8049a1c, $0x1
]
_code_pattern = re.compile("|".join(f"(?:{shape})" for shape in CODE_SHAPES), re.ASCII)
_not_code: set[str] = set()
_code_contexts: list[tuple[str, str]] = []
UNMATCHED_CONTEXTS: set[tuple[str, str]] = set()


def set_code_terms(terms: list[str], not_code: list[str] | None = None,
                   contexts: list[dict] | None = None) -> None:
    """Use this chapter's reviewed identifiers.

    terms are code wherever they occur in the chapter's prose; not_code lists
    shape matches that are ordinary text; contexts mark a word as code only
    inside the given phrase, for words that are also used as plain English.
    """
    global _code_pattern, _not_code, _code_contexts
    _not_code = set(not_code or [])
    _code_contexts = [(re.sub(r"\\(.)", r"\1", item["context"]).replace("`", ""), item["term"])
                      for item in contexts or []]
    UNMATCHED_CONTEXTS.update(_code_contexts)
    shapes = CODE_SHAPES[:2]
    if terms:
        words = "|".join(re.escape(term) for term in sorted(set(terms), key=len, reverse=True))
        # A listed word never stops short of a file extension (hw in hw.o).
        shapes.append(rf"(?<![A-Za-z0-9_])(?:{words})(?![A-Za-z0-9_]|\.[A-Za-z0-9])")
    shapes += CODE_SHAPES[2:]
    _code_pattern = re.compile("|".join(f"(?:{shape})" for shape in shapes), re.ASCII)


def split_code(text: str) -> list[tuple[str, bool]]:
    spans: list[tuple[int, int]] = []
    for context, term in _code_contexts:
        for found in re.finditer(re.escape(context), text):
            inner = re.search(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", context)
            if inner:
                spans.append((found.start() + inner.start(), found.start() + inner.end()))
                UNMATCHED_CONTEXTS.discard((context, term))
    for match in _code_pattern.finditer(text):
        start, end = match.span()
        code = match.group(0)
        # Sentence punctuation and an unmatched closing parenthesis stay prose.
        while code and (code[-1] in ".,;:!?" or (code[-1] == ")" and code.count(")") > code.count("("))):
            code = code[:-1]
            end -= 1
        if not code.strip("-./_") or code in _not_code:
            continue
        if not any(start < b and a < end for a, b in spans):
            spans.append((start, end))
    # Pieces of one command or name separated by a single space ("gcc" and
    # "-o hw hw.o") are one piece of code.
    joined: list[tuple[int, int]] = []
    for start, end in sorted(spans):
        if joined and start >= joined[-1][1] and text[joined[-1][1]:start] == " ":
            joined[-1] = (joined[-1][0], end)
        else:
            joined.append((start, end))
    parts: list[tuple[str, bool]] = []
    position = 0
    for start, end in joined:
        if start < position:
            continue
        code = text[start:end]
        if start > position:
            parts.append((text[position:start], False))
        parts.append((code, True))
        position = end
    if position < len(text):
        parts.append((text[position:], False))
    return parts


def mark_markdown_code(markdown: str) -> str:
    """Mark inline code in hand-written table markdown, cell by cell."""
    markup = re.compile(r"(<[^>]+>|`[^`]*`|~~.*?~~|\*[^*|]+\*|\|)")
    out = []
    for piece in markup.split(markdown):
        if not piece or markup.fullmatch(piece) or set(piece.strip()) <= set("- "):
            out.append(piece)
            continue
        plain = re.sub(r"\\(.)", r"\1", piece)
        if not any(is_code for _, is_code in split_code(plain)):
            out.append(piece)
            continue
        lead = piece[:len(piece) - len(piece.lstrip())]
        trail = piece[len(piece.rstrip()):]
        out.append(lead + render_tokens([Token(plain.strip(), "")], block_start=False) + trail)
    return "".join(out)


def ends_sentence(tokens: list[Token]) -> bool:
    text = "".join(token.text for token in tokens if token.style != "noteref" and token.text != "\0br").rstrip()
    if text[-1:] in "”’）)」』" and len(text) > 1:
        return text[-2] in "。！？!?…"
    return text[-1:] in "。！？：；…!?:;" or not text


def code_text(lines: list[Line]) -> str:
    chars = [(c, x) for line in lines for span in line.spans if span.is_code for c, x in span.chars]
    if not chars:
        return ""
    base = min(x for c, x in chars if c.strip())
    # Courier's advance, measured rather than derived from the font size.
    advances = sorted(b[1] - a[1] for line in lines for span in line.spans if span.is_code
                      for a, b in zip(span.chars, span.chars[1:]) if b[1] > a[1])
    width = advances[len(advances) // 2] if advances else 4.5
    out = []
    previous = None
    spacing = None
    for line in lines:
        if previous is not None:
            gap = line.y0 - previous.y0
            if previous.page == line.page:
                if spacing is None or gap < spacing:
                    spacing = gap if gap > 3 else spacing
                if spacing and gap > spacing * 1.6:
                    out.extend([""] * (round(gap / spacing) - 1))
        # Keep the listing's own spaces; positions only add the indentation
        # and the padding that aligns trailing comments in a column.
        row: list[str] = []
        for span in line.spans:
            for c, x in span.chars:
                if not c.strip():
                    if row:
                        row.append(" ")
                    continue
                col = round((x - base) / width)
                if col > len(row):
                    row.extend(" " * (col - len(row)))
                row.append(c)
                if CJK_RE.match(c):
                    row.append("")  # full-width glyphs take two columns
        out.append("".join(row).rstrip().replace("ˆ", "^"))
        previous = line
    while out and not out[0]:
        out.pop(0)
    return "\n".join(out)


def code_language(text: str) -> str:
    if re.search(r"^\s*(\d+\s+)?#include|;\s*$|^\s*(\d+\s+)?(int|void|char|struct|typedef)\b", text, re.M):
        return "c"
    return "text"


# --------------------------------------------------------------------------
# Sections


@dataclass
class Section:
    title: str
    start: int
    end: int
    group: str
    number: int = 0
    notes: list[str] = field(default_factory=list)

    @property
    def route(self) -> str:
        return f"/library/volume-{VOLUME:02d}/chapter-{self.number:03d}"


def sections_from_pdf(pdf: pymupdf.Document) -> list[Section]:
    toc = pdf.get_toc()
    entries = []
    for index, (_level, title, page1) in enumerate(toc):
        end = toc[index + 1][2] - 1 if index + 1 < len(toc) else len(pdf)
        entries.append((re.sub(r"\s+", " ", title).replace("CPU 虚", "CPU 虚"), page1 - 1, end))
    sections = []
    group = ""
    for title, start, end in entries:
        if title in SKIPPED:
            continue
        if re.match(r"^第\d部分", title):
            group = title.replace("部分 ", "部分　")
            continue
        if title.startswith("附录"):
            group = "附录"
        elif title in ("前言",) or re.match(r"^第[12]章", title):
            group = ""
        title = re.sub(r"^(第\d+章|附录[A-G]) ", r"\1　", title)
        sections.append(Section(title, start, end, group))
    for number, section in enumerate(sections, start=1):
        section.number = number
    if len(sections) != 58:
        raise ValueError(f"Unexpected outline: {len(sections)} reading pages")
    return sections


class SectionWriter:
    def __init__(self, section: Section) -> None:
        self.section = section
        self.blocks: list[Block] = []
        self.paragraph: Block | None = None
        self.code: list[Line] = []
        self.pending: list[Figure] = []
        self.interrupted: list[Block] = []  # figures moved after a resumed paragraph
        self.callout: Callout | None = None
        self.note_numbers: dict[str, int] = {}
        self.notes: list[list[Token]] = []
        self.in_references = False
        self.title_line: Line | None = None

    # Paragraph state ------------------------------------------------------

    def close_paragraph(self) -> None:
        if self.paragraph is not None:
            self.blocks.append(self.paragraph)
            self.paragraph = None
            for figure in self.pending:
                self.blocks.append(Block("figure", figure=figure))
            self.pending = []
            self.blocks.extend(self.interrupted)
            self.interrupted = []

    def close_code(self) -> None:
        if self.code:
            text = code_text(self.code)
            if text.strip():
                self.blocks.append(Block("code", text=text, lang=code_language(text)))
            self.code = []

    def set_callout(self, callout: Callout | None) -> None:
        if callout is self.callout:
            return
        if self.callout is not None and callout is not None and callout.page > self.callout.page:
            self.callout = callout  # the box continues on the next page
            return
        self.close_code()
        self.close_paragraph()
        if self.callout is not None and callout is None:
            self.blocks.append(Block("callout-end"))
        self.callout = callout

    def resume_paragraph(self) -> bool:
        """Rejoin a sentence that a figure or listing interrupted mid-way."""
        index = len(self.blocks)
        while index > 0 and self.blocks[index - 1].kind in ("figure", "code", "caption"):
            index -= 1
        if index == len(self.blocks) or index == 0:
            return False
        block = self.blocks[index - 1]
        if block.kind != "p" or ends_sentence(block.tokens):
            return False
        self.interrupted = self.blocks[index:]
        del self.blocks[index - 1:]
        self.paragraph = block
        return True

    def add_figure(self, figure: Figure) -> None:
        if figure.full_width or self.paragraph is None:
            self.close_code()
            self.close_paragraph()
            self.blocks.append(Block("figure", figure=figure))
        else:
            self.pending.append(figure)

    def add_line(self, line: Line, model: PageModel, limit: float, notes: dict[str, int]) -> None:
        text = line.text.strip()
        size = line.size
        first = line.first
        if line.is_code:
            self.close_paragraph()
            self.code.append(line)
            return
        self.close_code()

        if size >= 20:
            return  # Chapter titles repeat the H1.
        if first.font.startswith("FZLBJW") and size >= 15:
            self.close_paragraph()
            self.blocks.append(Block("h2", text=re.sub(r"\s+", " ", text)))
            self.in_references = "参考资料" in text
            return
        if first.font.startswith("FZZDXJW") and size >= 11:
            self.close_paragraph()
            self.blocks.append(Block("h3", text=re.sub(r"\s+", " ", text)))
            return
        if self.callout is not None and first.font.startswith("FZHTJW") and size < 10:
            title = re.sub(r"\s+", " ", text)
            if self.blocks and self.blocks[-1].kind == "callout-start" and self.paragraph is None:
                wrapped = self.title_line is not None and self.title_line.x1 - self.title_line.x0 > 0.7 * self.callout.rect.width
                self.blocks[-1].text += title if wrapped else "　" + title
                self.title_line = line
            else:
                self.close_paragraph()
                self.blocks.append(Block("callout-start", text=title))
                self.title_line = line
            return

        if is_caption(line):
            self.close_paragraph()
            self.blocks.append(Block("caption", text=text))
            return
        if (re.fullmatch(r"[（(]\s*[0-9A-G]+\.\d+\s*[)）]", text) and self.paragraph is not None and
                self.paragraph.last_line.page == line.page and abs(self.paragraph.last_line.y1 - line.y1) < 3):
            self.paragraph.tokens.append(Token(" " + text, ""))  # equation number
            return

        tokens = line_tokens(line, notes)
        column_left = model.left + (6 if self.callout else 0)
        for figure in model.figures:
            area = figure.extent
            if (not figure.full_width and area.x1 < line.x0 and
                    area.y0 - 8 < line.y1 and line.y0 < area.y1 + 8):
                beside = [other.x0 for other in model.lines if other.x0 > area.x1 and
                          area.y0 - 8 < other.y1 and other.y0 < area.y1 + 8]
                column_left = max(column_left, min(beside))
        indented = line.x0 > column_left + 8
        bullet = text[:1] in "●•◆■�" or first.font.startswith(("Webdings", "Wingdings"))
        if bullet:
            while tokens and not tokens[0].text.strip():
                tokens.pop(0)
            tokens[0].text = tokens[0].text.lstrip()[1:]
        speaker = bool(re.match(r"^(教授|学生)[（(：:]", text)) and first.font.startswith(BOLD_FONTS)
        reference = self.in_references and bool(re.match(r"^\[[A-Za-z0-9+&.\-]+\d{2}[a-z]?\]", text))
        new_paragraph = bullet or speaker or reference or indented or self.paragraph is None
        if self.paragraph is not None and self.paragraph.kind == "li" and not bullet and line.x0 > column_left + 28:
            new_paragraph = False  # hanging indent of a bullet item (paragraphs indent only 21pt)
        plain = not bullet and not speaker and not reference
        if (self.paragraph is not None and self.paragraph.last_line is not None and
                self.paragraph.last_line.page != line.page and plain and
                (not indented or not ends_sentence(self.paragraph.tokens))):
            # The paragraph continues on the next page (chapters were typeset
            # separately, so a continuation is sometimes indented).
            new_paragraph = False
        if self.paragraph is None and plain and not indented and self.resume_paragraph():
            new_paragraph = False
        if new_paragraph:
            self.close_paragraph()
            self.paragraph = Block("li" if bullet else "p", tokens=tokens, last_line=line, limit=limit,
                                   code=not self.in_references)
            return
        previous = self.paragraph.last_line
        beside_figure = any(not figure.full_width and
                            (figure.extent.x0 > previous.x1 - 2 or figure.extent.x1 < previous.x0 + 2) and
                            figure.extent.y0 - 8 < previous.y1 and previous.y0 < figure.extent.y1 + 8
                            for figure in model.figures)
        short = (previous.page == line.page and not beside_figure and
                 previous.x1 < self.paragraph.limit - previous.size * 1.5)
        if self.in_references and not short:
            # Each reference prints its title, its source and the Chinese
            # comment on separate lines, even when a line runs full width.
            tail = previous.text.rstrip()[-1:]
            head = text[:1]
            short = bool(tail and head) and (
                (not CJK_RE.match(tail) and bool(CJK_RE.match(head))) or (tail == "”" and head.isascii() and head.isalpha()))
        if short:
            self.paragraph.tokens.append(Token("\0br", ""))
            self.paragraph.tokens.extend(tokens)
        else:
            self.paragraph.tokens = join_tokens(self.paragraph.tokens, tokens)
        self.paragraph.last_line = line
        self.paragraph.limit = limit

    # Notes ----------------------------------------------------------------

    def register_notes(self, model: PageModel) -> dict[str, int]:
        mapping: dict[str, int] = {}
        current: list[Token] | None = None
        for line in model.notes:
            text = line.text.strip()
            tokens = line_tokens(line)
            if text[:1] in CIRCLED:
                mark = text[0]
                number = len(self.notes) + 1
                mapping[mark] = number
                stripped = tokens[0].text.lstrip()
                tokens[0].text = stripped[1:]
                current = tokens
                self.notes.append(current)
            elif current is not None:
                current[:] = join_tokens(current, tokens)
            elif self.notes:
                self.notes[-1][:] = join_tokens(self.notes[-1], tokens)
        return mapping

    def render(self) -> tuple[str, int]:
        self.close_code()
        self.close_paragraph()
        if self.callout is not None:
            self.blocks.append(Block("callout-end"))
            self.callout = None
        out: list[str] = []
        characters = 0
        open_callout = False
        for block in self.blocks:
            if block.kind in ("p", "li"):
                parts = []
                segment: list[Token] = []
                for token in block.tokens:
                    if token.text == "\0br":
                        parts.append(render_tokens(segment, mark_code=block.code))
                        segment = []
                    else:
                        segment.append(token)
                parts.append(render_tokens(segment, mark_code=block.code))
                text = "<br>\n".join(part for part in parts if part)
                if not text:
                    continue
                characters += len(re.sub(r"<[^>]+>|\s", "", text))
                out.append(("- " + text.lstrip("\\")) if block.kind == "li" else text)
            elif block.kind in ("h2", "h3"):
                marker = "##" if block.kind == "h2" else "###"
                out.append(f"{marker} {render_tokens([Token(block.text, '')], block_start=False)}")
                characters += len(block.text)
            elif block.kind == "code":
                fence = "````" if "```" in block.text else "```"
                out.append(f"{fence}{block.lang}\n{block.text}\n{fence}")
                characters += len(re.sub(r"\s", "", block.text))
            elif block.kind == "figure":
                out.extend(figure_markdown(block.figure))
            elif block.kind == "caption":
                out.append(f"*{caption_markup(block.text)}*")
            elif block.kind == "callout-start":
                if open_callout:
                    out.append(":::")
                title = block.text
                kind = "warning" if title.startswith("关键问题") else "tip" if title.startswith("提示") else "info"
                out.append(f"::: {kind} {render_tokens([Token(title, '')], block_start=False)}")
                open_callout = True
                characters += len(title)
            elif block.kind == "callout-end":
                if open_callout:
                    out.append(":::")
                    open_callout = False
        if open_callout:
            out.append(":::")
        return "\n\n".join(out), characters


def format_caption(text: str) -> str:
    caption = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"^(图|表) ?([0-9A-G]+\.\d+) *", r"\1 \2　", caption)


def caption_markup(text: str) -> str:
    return render_tokens([Token(format_caption(text), "")], block_start=False)


def figure_markdown(figure: Figure) -> list[str]:
    if figure.markdown:
        return [figure.markdown]
    caption = format_caption(figure.caption)
    if figure.table:
        header, *body = figure.table
        lines = ["| " + " | ".join(cell or " " for cell in header) + " |",
                 "|" + "|".join(" --- " for _ in header) + "|"]
        lines += ["| " + " | ".join(row) + " |" for row in body]
        table = "\n".join(lines)
        return [f"*{escape_text(caption)}*", table] if caption else [table]
    alt = caption or f"插图（原书 PDF 第 {figure.page + 1} 页）"
    image = f"![{alt.replace('[', '［').replace(']', '］')}]({IMAGE_ROUTE}/{figure.image})"
    if not caption:
        return [image]
    label = f"*{caption_markup(figure.caption)}*"
    return [label, image] if figure.caption_above else [image, label]


def render_figure(pdf: pymupdf.Document, figure: Figure, name: str) -> None:
    clip = pymupdf.Rect(figure.rect) + (-3, -3, 3, 3)
    clip &= pdf[figure.page].rect
    pixmap = pdf[figure.page].get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=clip, alpha=False)
    image = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGB")
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    image.save(IMAGE_DIR / name, "WEBP", lossless=True, quality=100, method=6)


# --------------------------------------------------------------------------
# Driver


def section_markdown(pdf, section: Section, repair: GlyphRepair, overrides: dict,
                     images: list[str], debug: bool = False) -> tuple[str, int]:
    reviewed = overrides.get("code_terms", {}).get(str(section.number), {})
    set_code_terms(reviewed.get("code", []), reviewed.get("not_code", []), reviewed.get("contexts", []))
    writer = SectionWriter(section)
    figure_count = Counter()
    for number in range(section.start, section.end):
        model = build_page(pdf, number, repair, overrides)
        mapping = writer.register_notes(model)
        events: list[tuple[float, int, object]] = []
        for line in model.lines:
            events.append((line.y0, 1, line))
        for figure in model.figures:
            figure_count[number] += 1
            if figure.table is None and not figure.markdown:
                figure.image = f"p{number + 1:03d}-{figure_count[number]:02d}.webp"
                images.append(figure.image)
                if not debug:
                    render_figure(pdf, figure, figure.image)
            row_top = min(other.rect.y0 for other in model.figures
                          if other.rect.y0 < figure.rect.y1 and figure.rect.y0 < other.rect.y1)
            events.append((row_top, 0, figure))
        events.sort(key=lambda item: (item[0], item[1], item[2].x0 if isinstance(item[2], Line) else item[2].rect.x0))
        body_lines = [line for line in model.lines if not line.is_code]
        for _y, _order, item in events:
            if isinstance(item, Figure):
                centre = pymupdf.Point((item.rect.x0 + item.rect.x1) / 2, (item.rect.y0 + item.rect.y1) / 2)
                writer.set_callout(next((c for c in model.callouts if centre in c.rect), None))
                writer.add_figure(item)
                continue
            line = item
            callout = next((c for c in model.callouts if inside(line, c.rect, 1)), None)
            writer.set_callout(callout)
            neighbours = [other.x1 for other in body_lines if abs(other.y0 - line.y0) < 40
                          and (inside(other, callout.rect, 1) if callout else not any(
                              inside(other, c.rect, 1) for c in model.callouts))]
            limit = max(neighbours) if neighbours else line.x1
            writer.add_line(line, model, limit, mapping)
        if debug:
            print(f"--- page {number + 1}: {len(model.lines)} lines, {len(model.figures)} figures, "
                  f"{len(model.callouts)} callouts, {len(model.notes)} note lines, left {model.left}")
            for figure in model.figures:
                print("   FIG", figure.kind, [round(v) for v in figure.rect], figure.caption[:30], "TABLE" if figure.table else "")
    body, characters = writer.render()
    if writer.notes:
        definitions = ["## 注释"]
        for number, tokens in enumerate(writer.notes, start=1):
            text = render_tokens(tokens, html_code=True)
            definitions.append(
                f'<p class="footnote-definition footnote-source" id="note-{number}">'
                f'<a class="footnote-number" href="#note-{number}">[{number}]</a>{text} '
                f'<span class="footnote-backrefs"><a class="footnote-backref" href="#note-ref-{number}-1" '
                f'aria-label="返回注释 {number} 的第 1 处引用">↩</a></span></p>')
            characters += len(re.sub(r"<[^>]+>|\s", "", text))
        body += "\n\n" + "\n\n".join(definitions)
    section.notes = [str(n) for n in range(1, len(writer.notes) + 1)]
    return body, characters


def apply_reviewed_layout(markdown: str, section: Section, overrides: dict) -> str:
    """Apply text fixes checked against the rendered PDF pages."""
    for index, fix in enumerate(overrides.get("text", {}).get(str(section.number), []), start=1):
        matches = markdown.count(fix["original"])
        if matches != fix.get("count", 1):
            raise ValueError(f"Reviewed fix {section.number}:{index} matches {matches} times")
        markdown = markdown.replace(fix["original"], fix["revised"])
    return markdown


def write_site_metadata(sections: list[Section], character_count: int) -> None:
    groups: list[tuple[str, list[Section]]] = []
    for section in sections:
        if groups and groups[-1][0] == section.group:
            groups[-1][1].append(section)
        else:
            groups.append((section.group, [section]))
    lines = ["---", f"title: {json.dumps(TITLE, ensure_ascii=False)}",
             f"description: {json.dumps(f'{AUTHOR}著，{TRANSLATOR}译。Operating Systems: Three Easy Pieces 中文版。', ensure_ascii=False)}",
             "---", "", f"# {TITLE}", "",
             f"{AUTHOR}著，{TRANSLATOR}译，人民邮电出版社 2019 年出版。英文书名 *Operating Systems: Three Easy Pieces*，简称 OSTEP。", "",
             "全书围绕虚拟化、并发和持久性三个主题展开，介绍现代操作系统的主要组件，包括调度、虚拟内存管理、磁盘和 I/O 子系统以及文件系统。"
             "大部分章节先提出一个关键问题，再通过书中介绍的技术、算法和思想解决它；各部分以师生对话引入。", "",
             f"本卷依据作者在[本书官方网站]({SOURCE_URL})公开提供的中文版各章 PDF 整理。插图保留原书排版的图片，"
             "代码、公式和大部分表格转为可检索的文本；原书注释放在各章末尾，与正文双向链接。", "",
             f"[开始阅读 →]({sections[0].route})", "", "## 目录", ""]
    for group, items in groups:
        if group:
            lines += [f"### {group}", ""]
        lines += [f"- [{item.title}]({item.route})" for item in items]
        lines.append("")
    (VOLUME_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")

    sidebar_items: list[dict] = [{"text": "本卷首页", "link": f"/library/volume-{VOLUME:02d}/"}]
    for group, items in groups:
        links = [{"text": item.title, "link": item.route} for item in items]
        if group:
            sidebar_items.append({"text": group, "collapsed": True, "items": links})
        else:
            sidebar_items.extend(links)
    sidebar = [{"text": TITLE, "collapsed": True, "items": sidebar_items}]
    catalog = [{"title": TITLE, "fullTitle": f"{TITLE}（Operating Systems: Three Easy Pieces）",
                "volumeLabel": "新增卷", "author": AUTHOR, "translator": TRANSLATOR,
                "link": f"/library/volume-{VOLUME:02d}/", "firstPage": sections[0].route,
                "pageCount": len(sections)}]
    stats = {"volumeCount": 1, "pageCount": len(sections), "characterCount": character_count}
    module = ROOT / "docs" / ".vitepress" / "library.ostep.mjs"
    module.write_text(
        "// 此文件由 scripts/import-ostep.py 生成。\n"
        f"export const ostepLibrarySidebar = {json.dumps(sidebar, ensure_ascii=False, indent=2)}\n\n"
        f"export const ostepLibraryCatalog = {json.dumps(catalog, ensure_ascii=False, indent=2)}\n\n"
        f"export const ostepLibraryStats = {json.dumps(stats, ensure_ascii=False, indent=2)}\n",
        encoding="utf-8")
    subprocess.run(["node", "scripts/rebuild-library-index.mjs"], cwd=ROOT, check=True)


def verify_source(path: Path) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != manifest["sha256"]:
        raise ValueError(f"Unexpected PDF checksum {digest}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", help="debug a 1-based PDF page range, e.g. 35-43")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    verify_source(args.pdf)
    pdf = pymupdf.open(args.pdf)
    if len(pdf) != PAGE_COUNT:
        raise ValueError(f"Expected {PAGE_COUNT} pages, found {len(pdf)}")
    repair = GlyphRepair()
    overrides = json.loads(REVIEWED_LAYOUT.read_text(encoding="utf-8")) if REVIEWED_LAYOUT.exists() else {}
    sections = sections_from_pdf(pdf)

    if args.pages:
        first, _, last = args.pages.partition("-")
        debug_section = Section("调试", int(first) - 1, int(last or first), "", 0)
        body, _ = section_markdown(pdf, debug_section, repair, overrides, [], debug=args.debug)
        out = ROOT / "tmp" / "ostep" / f"debug-{args.pages}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        print(f"Wrote {out} ({repair.repaired} glyphs repaired)")
        return

    VOLUME_DIR.mkdir(parents=True, exist_ok=True)
    if IMAGE_DIR.exists():
        for old in IMAGE_DIR.glob("*.webp"):
            old.unlink()
    images: list[str] = []
    rendered: dict[str, str] = {}
    character_count = 0
    note_count = 0
    for section in sections:
        body, characters = section_markdown(pdf, section, repair, overrides, images)
        character_count += characters
        note_count += len(section.notes)
        context = f"{TITLE} · {section.group}" if section.group else TITLE
        markdown = (f"---\ntitle: {json.dumps(section.title, ensure_ascii=False)}\n"
                    f"description: {json.dumps(f'{context} · {section.title}', ensure_ascii=False)}\n---\n\n"
                    f'<p class="reading-meta"><a href="./">{TITLE}</a>'
                    f'{" · " + section.group if section.group else ""}</p>\n\n'
                    f"# {section.title}\n\n{body}\n")
        rendered[f"chapter-{section.number:03d}.md"] = apply_reviewed_layout(markdown, section, overrides)
    for old in VOLUME_DIR.glob("chapter-*.md"):
        if old.name not in rendered:
            old.unlink()
    for name, markdown in rendered.items():
        (VOLUME_DIR / name).write_text(markdown, encoding="utf-8")
    write_site_metadata(sections, character_count)
    audit = ROOT / "tmp" / "ostep" / "figure-text-audit.txt"
    audit.parent.mkdir(parents=True, exist_ok=True)
    audit.write_text("\n".join(AUDIT) + "\n", encoding="utf-8")
    for context, term in sorted(UNMATCHED_CONTEXTS):
        print(f"Code context not found: {term!r} in {context!r}")
    print(f"Imported {len(sections)} pages, {character_count:,} characters, {len(images)} images, "
          f"{note_count} notes, {repair.repaired} glyphs repaired")


if __name__ == "__main__":
    main()
