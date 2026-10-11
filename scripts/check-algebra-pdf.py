"""Validate continuous PDF coverage, source snapshots, labels, fonts, and prose."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

import pymupdf
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "tmp/pdfs/algebra-export"
PDF = ROOT / "output/pdf/Algebra-Zh.pdf"
SOURCE_PAGES = list(range(6, 12)) + list(range(17, 920))
report = json.loads((WORK / "export-page-map.json").read_text(encoding="utf8"))
snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
doc = pymupdf.open(PDF)
reader = PdfReader(PDF)
assert doc.page_count == report["pageCount"]
assert [entry["sourcePdfPage"] for entry in report["pageMap"]] == SOURCE_PAGES
assert len(snapshot["sections"]) == 31
assert snapshot["generatedContents"] is True
assert all(section["key"] not in ["title-pages", "contents", "series-list"] for section in snapshot["sections"])
assert snapshot["counts"]["diagrams"] == 140
assert len(report["physicalPages"]) == doc.page_count
assert {int(n) for n in snapshot["sourceHashes"]} == set(SOURCE_PAGES)
assert {int(n) for n in snapshot["readingBodies"]} == set(SOURCE_PAGES)
assert [entry[1] for entry in doc.get_toc()] == ["目录"] + [s["title"] for s in snapshot["sections"]]
log = (WORK / "algebra.log").read_text(encoding="utf8", errors="replace")
assert not re.search(r"Missing character:|Overfull \\[hv]box|Undefined control sequence", log), "typesetting defects in XeLaTeX log"
source_texts = []
for n in SOURCE_PAGES:
    path = ROOT / f"source/algebra/zh/pdf-{n:04d}.md"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == snapshot["sourceHashes"][str(n)]
    # The exporter may remove a duplicate opening chapter heading. Compare the
    # exact reading body, not a title that was deliberately omitted.
    source_texts.append(f"ALGEbrasource{n:04d}\n\n" + snapshot["readingBodies"][str(n)])
ast = json.loads(subprocess.run(["pandoc", "-f", "markdown-fancy_lists", "-t", "json"], input="\n\n".join(source_texts), text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout)
chunks = collections.defaultdict(list)
prose_chunks = collections.defaultdict(list)
strong_texts = collections.defaultdict(list)
current = 0
counts = {"inlineMath": 0, "displayMath": 0, "diagrams": 0, "mathPunctuation": 0}

def diagram_count(node):
    if isinstance(node, list):
        return sum(diagram_count(child) for child in node)
    if isinstance(node, dict):
        if node.get("t") == "Image":
            assert node["c"][2][0].startswith("/library/volume-86/diagrams/"), node
            return 1
        return sum(diagram_count(child) for child in node.values())
    return 0

def str_text(node):
    if isinstance(node, list):
        return "".join(str_text(child) for child in node)
    if isinstance(node, dict):
        if node.get("t") == "Str":
            return node["c"]
        if node.get("t") in ["Space", "SoftBreak", "LineBreak"]:
            return " "
        if node.get("t") in ["Math", "Image", "Figure"]:
            return ""
        return "".join(str_text(child) for child in node.values())
    return ""

def collect(node):
    global current
    if isinstance(node, list):
        for child in node: collect(child)
    elif isinstance(node, dict):
        if node.get("t") in ["Image", "Figure"]:
            counts["diagrams"] += diagram_count(node)
            return
        if node.get("t") == "Str":
            value = node["c"]
            if re.fullmatch(r"ALGEbrasource\d{4}", value):
                current = int(value[-4:])
            else:
                chunks[current].append(value)
                prose_chunks[current].append(value)
        elif node.get("t") == "Math":
            kind, tex = node["c"]
            counts["displayMath" if kind["t"] == "DisplayMath" else "inlineMath"] += 1
            counts["mathPunctuation"] += tex.count("。")
            # Chinese words within formulas must also survive font embedding.
            chunks[current].append(node["c"][1])
            # Formula labels can use stars too. They are not prose references,
            # and omitting a formula must not concatenate adjacent text tokens.
            prose_chunks[current].append("\ufffc")
        elif node.get("t") in ["Space", "SoftBreak", "LineBreak"]:
            prose_chunks[current].append(" ")
        elif node.get("t") == "Strong":
            strong_texts[current].append(str_text(node["c"]))
            collect(node["c"])
        else:
            for v in node.values(): collect(v)

collect(ast["blocks"])
assert counts == snapshot["counts"], (counts, snapshot["counts"], "formula/diagram counts differ from reading bodies")
assert set(chunks) == set(SOURCE_PAGES)
missing = []
body_bounds = []
embedded_fonts = set()
cjk_fonts = set()
physical_texts = []
physical_body_texts = []
generated_contents_pages = []
page_map = {entry["sourcePdfPage"]: entry for entry in report["pageMap"]}
previous_first = previous_last = 0
for n in SOURCE_PAGES:
    entry = page_map[n]
    first, last = entry["firstExportPage"], entry["lastExportPage"]
    assert 1 <= first <= last <= doc.page_count, (n, "invalid physical interval")
    assert first >= previous_first and last >= previous_last, (n, "source order reversed")
    previous_first, previous_last = first, last
    review = json.loads((ROOT / f"source/algebra/review/pdf-{n:04d}.json").read_text(encoding="utf8"))
    assert entry["printedPage"] == review["printedPage"], (n, "original printed page label changed")
section_starts = []
previous_section_last = 0
for section in snapshot["sections"]:
    first = page_map[section["firstPdfPage"]]["firstExportPage"]
    last = page_map[section["lastPdfPage"]]["lastExportPage"]
    assert first > previous_section_last, (section["key"], first, previous_section_last, "major section did not begin on a new physical page")
    section_starts.append({"key": section["key"], "firstExportPage": first, "lastExportPage": last})
    previous_section_last = last
if "sectionStarts" in report:
    actual_starts = report["sectionStarts"]
    if isinstance(actual_starts, dict):
        actual_starts = [{"key": key, **value} for key, value in actual_starts.items()]
    for expected in section_starts:
        actual = next((value for value in actual_starts if value["key"] == expected["key"]), None)
        assert actual and all(actual.get(key) == value for key, value in expected.items()), (expected, actual, "major section map differs from source intervals")
for physical, entry in enumerate(report["physicalPages"], 1):
    assert entry["exportPage"] == physical, (physical, "physical page sequence mismatch")
    expected_sources = [n for n in SOURCE_PAGES
                        if page_map[n]["firstExportPage"] <= physical <= page_map[n]["lastExportPage"]]
    generated = entry.get("generated", False)
    assert expected_sources or generated, (physical, "empty page inserted into continuous text")
    assert entry["sourcePdfPages"] == expected_sources, (physical, "physical/source mapping mismatch")
    if generated:
        assert expected_sources == [] and entry["sectionTitle"] == "目录" and entry["originalLabel"] == "", (physical, "generated contents page has source-page metadata")
        generated_contents_pages.append(physical)
    page = doc[physical - 1]
    text = page.get_text()
    physical_texts.append(text)
    compact = re.sub(r"\s+", "", text)
    if not generated:
        if any(page_map[n]["printedPage"] is not None for n in expected_sources):
            assert entry["originalLabel"] and re.sub(r"\s+", "", entry["originalLabel"]) in compact, (physical, "original page range missing")
        else:
            assert entry["originalLabel"] == "", (physical, "an original printed page label was invented")
    assert "\ufffd" not in text, (physical, "replacement character")
    spans = [s for b in page.get_text("dict")["blocks"] if "lines" in b for line in b["lines"] for s in line["spans"]]
    page_body = []
    for span in spans:
        x0, y0, x1, y1 = span["bbox"]
        if re.search(r"[\u3400-\u9fff]", span["text"]):
            cjk_fonts.add(span["font"])
            assert "SimSun" in span["font"], (physical, span["font"], "Chinese text is not set in the requested SimSun family")
        # The first body line begins near y=64 pt; exclude only the running
        # header (around y=30) and footer (around y=800), not that first line.
        if 50 < y0 < 790 and span["text"].strip():
            page_body.append(span["text"])
            if x0 < 53 or x1 > page.rect.width - 53:
                body_bounds.append({"exportPage": physical, "sourcePdfPages": expected_sources, "bbox": span["bbox"], "text": span["text"][:80]})
    physical_body_texts.append("" if generated else "".join(page_body))
    for font in page.get_fonts(full=True):
        xref = font[0]
        if xref not in embedded_fonts:
            assert len(doc.extract_font(xref)[3]) > 0, (physical, font, "font not embedded")
            embedded_fonts.add(xref)

assert generated_contents_pages, "native linked table of contents was not generated"
assert doc.get_toc()[0][2] == generated_contents_pages[0], "contents bookmark targets the wrong physical page"
contents_text = re.sub(r"\s+", "", "".join(physical_texts[physical - 1] for physical in generated_contents_pages))
contents_targets = {link["page"] + 1 for physical in generated_contents_pages
                    for link in doc[physical - 1].get_links()
                    if link.get("kind") in [pymupdf.LINK_GOTO, pymupdf.LINK_NAMED] and link.get("page", -1) >= 0}
contents_rows = collections.defaultdict(list)
for physical in generated_contents_pages:
    page = doc[physical - 1]
    spans = [span for block in page.get_text("dict")["blocks"] if "lines" in block
             for line in block["lines"] for span in line["spans"]]
    for link in page.get_links():
        if link.get("kind") not in [pymupdf.LINK_GOTO, pymupdf.LINK_NAMED] or link.get("page", -1) < 0:
            continue
        area = link["from"]
        row = [span for span in spans if area.y0 - 1 <= (span["bbox"][1] + span["bbox"][3]) / 2 <= area.y1 + 1]
        row.sort(key=lambda span: span["bbox"][0])
        contents_rows[link["page"] + 1].append(re.sub(r"\s+", "", "".join(span["text"] for span in row)))
for section, start, bookmark in zip(snapshot["sections"], section_starts, doc.get_toc()[1:]):
    assert re.sub(r"\s+", "", section["title"]) in contents_text, (section["key"], "main section title missing from native contents")
    assert start["firstExportPage"] in contents_targets, (section["key"], start["firstExportPage"], "native contents lacks an internal jump to the main section")
    assert bookmark[2] == start["firstExportPage"], (section["key"], bookmark[2], start["firstExportPage"], "chapter bookmark targets the wrong physical page")
    title = re.sub(r"\s+", "", section["title"])
    assert any(title in row and re.search(r"(?<!\d)" + str(start["firstExportPage"]) + r"(?!\d)", row)
               for row in contents_rows[start["firstExportPage"]]), (section["key"], "contents row does not print its actual translated-PDF page number")
for entry in report["pageMap"]:
    n = entry["sourcePdfPage"]
    actual = "".join(physical_texts[entry["firstExportPage"] - 1:entry["lastExportPage"]])
    expected_chars = collections.Counter(re.findall(r"[\u3400-\u9fff]", "".join(chunks[n])))
    actual_chars = collections.Counter(re.findall(r"[\u3400-\u9fff]", actual))
    lost = expected_chars - actual_chars
    if lost:
        missing.append({"sourcePage": n, "missingCharacters": dict(lost)})
# A whole-body count supplements overlapping source intervals. Otherwise the
# same text could satisfy adjacent source pages merely by being in both spans.
expected_all = collections.Counter(re.findall(r"[\u3400-\u9fff]", "".join("".join(chunks[n]) for n in SOURCE_PAGES)))
actual_all = collections.Counter(re.findall(r"[\u3400-\u9fff]", "".join(physical_body_texts)))
global_missing = dict(expected_all - actual_all)
star_references = []
assert collections.Counter(re.findall(r"\(\*{1,3}\)", "".join(prose_chunks[503]))) == {"(*)": 1, "(**)": 1}, "source 503 prose references were consumed during Markdown parsing"
for n in SOURCE_PAGES:
    # Unescaped (*) / (**) can be consumed as Markdown emphasis. The reading
    # helper escapes them only in prose, so all references survive as Str nodes.
    expected = collections.Counter(re.findall(r"\(\*{1,3}\)", "".join(prose_chunks[n])))
    if not expected:
        continue
    entry = page_map[n]
    actual = re.sub(r"\s+", "", "".join(physical_texts[entry["firstExportPage"] - 1:entry["lastExportPage"]]))
    found = {label: actual.count(label) for label in expected}
    assert all(found[label] >= count for label, count in expected.items()), (n, dict(expected), found, "plain-text star reference lost")
    star_references.append({"sourcePage": n, "expected": dict(expected), "found": found})

# The source page 503 term must keep its Strong AST markup rather than printing
# Markdown delimiters. SimSun fake bold keeps the same font name, so the visual
# review checks its weight; font-family names cannot prove that weight here.
entry = page_map[503]
assert any("真同余式" in value for value in strong_texts[503]), "source 503 term lost its Strong markup"
term_text = re.sub(r"\s+", "", "".join(physical_texts[entry["firstExportPage"] - 1:entry["lastExportPage"]]))
assert "真同余式" in term_text, "source 503 term is missing from the PDF"
assert not re.search(r"\*{2}真同余式|真同余式\*{2}", term_text), "source 503 prints literal bold delimiters"
result = {"pageCount": doc.page_count, "sourcePages": len(SOURCE_PAGES), "bookmarks": len(doc.get_toc()), "mathExpressions": counts["inlineMath"] + counts["displayMath"], "mathCounts": counts, "originalDiagrams": counts["diagrams"], "embeddedFontCount": len(embedded_fonts), "chineseFontFamilies": sorted(cjk_fonts), "sourceHashesCurrent": True, "generatedContentsPages": generated_contents_pages, "contentsMainSectionLinksVerified": len(section_starts), "majorSectionPageBreaksVerified": len(section_starts), "missingProseCharacters": missing, "globalMissingProseCharacters": global_missing, "marginExceptions": body_bounds, "plainTextStarReferences": star_references, "source503BoldMarkupVerified": True, "pdfSha256": hashlib.sha256(PDF.read_bytes()).hexdigest()}
(WORK / "pdf-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf8")
print(json.dumps({k: v if k not in ["missingProseCharacters", "globalMissingProseCharacters", "marginExceptions", "plainTextStarReferences"] else len(v) for k, v in result.items()}, ensure_ascii=False))
assert not missing, "Chinese prose character loss detected; inspect validation report"
assert not global_missing, "whole-book Chinese prose character loss detected; inspect validation report"
assert not body_bounds, "text margin violations detected; inspect validation report"
