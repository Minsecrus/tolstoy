"""Typeset the checked Chinese book continuously, retaining source-page ranges.

Requires Pandoc and XeLaTeX. Intermediate files remain under tmp/pdfs/representation-theory-export.
No book source is edited. Formula AST nodes remain TeX, not raster images.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "tmp/pdfs/representation-theory-export"
OUT = ROOT / "output/pdf/Introduction-to-Representation-Theory-Zh.pdf"

PREAMBLE = r"""\documentclass[UTF8,fontset=windows,11pt]{ctexart}
\usepackage[a4paper,top=22mm,bottom=22mm,left=22mm,right=22mm,headheight=14pt,headsep=7mm,footskip=10mm]{geometry}
\usepackage{amsmath,amssymb,amscd,mathtools,stmaryrd,mathrsfs}
\usepackage{graphicx,adjustbox,enumitem,fancyhdr,xcolor,hyperref,bookmark,multicol,longtable,booktabs,array,calc}
\newcounter{none}
\setCJKmainfont{SimSun}[BoldFont=SimSun,BoldFeatures={FakeBold=1.5},ItalicFont=SimSun,ItalicFeatures={FakeBold=1.5},BoldItalicFont=SimSun,BoldItalicFeatures={FakeBold=1.5}]
\setCJKsansfont{SimSun}[BoldFont=SimSun,BoldFeatures={FakeBold=1.5}]
\setmainfont{Cambria}
\renewcommand{\emph}[1]{\textbf{#1}}
\xeCJKsetup{PunctStyle=plain}
\hypersetup{unicode=true,hidelinks,linktoc=all,pdftitle={表示论导论},pdfauthor={Pavel Etingof et al.},pdfsubject={中文译本},bookmarksdepth=0}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt minus 1pt}
\linespread{1.13}
\setlength{\emergencystretch}{2em}
\sloppy
\setlist{nosep,leftmargin=1.8em,topsep=4pt,parsep=2pt}
\setlength{\columnsep}{16pt}
\setlength{\multicolsep}{4pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\renewcommand{\contentsname}{目录}
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother
\ctexset{section={format=\Large\bfseries,beforeskip=9pt,afterskip=6pt},subsection={format=\large\bfseries,beforeskip=7pt,afterskip=5pt},subsubsection={format=\normalsize\bfseries,beforeskip=6pt,afterskip=4pt}}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\providecommand{\passthrough}[1]{#1}
\InputIfFileExists{representation-theory-page-headers.tex}{}{}
\newcommand{\pageoriginal}{\ifcsname RepresentationTheoryOriginal\thepage\endcsname\csname RepresentationTheoryOriginal\thepage\endcsname\fi}
\newcommand{\pagesection}{\ifcsname RepresentationTheorySection\thepage\endcsname\csname RepresentationTheorySection\thepage\endcsname\fi}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\scriptsize\color{gray}\pagesection}
\fancyhead[R]{\scriptsize\color{gray}\pageoriginal}
\fancyfoot[C]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.2pt}
\renewcommand{\footrulewidth}{0pt}
\newwrite\sourcemap
\immediate\openout\sourcemap=representation-theory-page-map.tsv
\newif\ifRepresentationTheoryBody
\RepresentationTheoryBodyfalse
% These deferred writes travel with the line containing the source boundary.
% Original page boundaries neither start a paragraph nor force a new PDF page.
\DeclareRobustCommand{\sourcebegin}[1]{\ifRepresentationTheoryBody\write\sourcemap{S #1\space\thepage}\fi}
\DeclareRobustCommand{\sourceend}[1]{\ifRepresentationTheoryBody\write\sourcemap{E #1\space\thepage}\fi}
\newcommand{\booksection}[2]{\clearpage\pdfbookmark[0]{#2}{chapter-#1}}
\newcommand{\RepresentationTheoryDisplay}[2]{\begin{equation*}\adjustbox{max width=0.94\linewidth}{$\displaystyle #1$}#2\end{equation*}}
% Preserve TeX's normal relation/operator line breaks for formulas that fit.
% Boxing every short formula prevents those breaks and can overflow prose.
% Only an expression wider than the full measure needs proportional fitting.
\DeclareRobustCommand{\RepresentationTheoryInline}[1]{\leavevmode\begingroup\setbox0=\hbox{$#1$}\allowbreak\hskip0pt\ifdim\wd0>.96\linewidth\adjustbox{max width=.96\linewidth}{$#1$}\else$#1$\fi\nobreak\hskip0pt\endgroup}
\newcommand{\RepresentationTheorySmallDisplay}[2]{{\small\RepresentationTheoryDisplay{#1}{#2}}}
\DeclareRobustCommand{\RepresentationTheorySmallInline}[1]{{\small\RepresentationTheoryInline{#1}}}
\pdfstringdefDisableCommands{\def\RepresentationTheoryInline#1{#1}\def\RepresentationTheorySmallInline#1{#1}\def\sourcebegin#1{}\def\sourceend#1{}}
\begin{document}
\pdfbookmark[0]{目录}{contents}
\begingroup
\setlength{\parskip}{0pt}
\tableofcontents
\endgroup
\clearpage
\RepresentationTheoryBodytrue
"""


def escape_tex(s):
    chars = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(chars.get(c, c) for c in s)


def marker(n, end=False, inline=True):
    # A write at the start of vertical mode can stay on the previous page
    # when the following paragraph moves. Enter its actual text line first.
    prefix = r"\leavevmode" if inline and not end else ""
    return {"t": "RawInline", "c": ["latex", prefix + (r"\sourceend{" if end else r"\sourcebegin{") + str(n) + "}"]}

def attach_boundary(blocks, n, end=False):
    # Put bookkeeping inside the actual first/last typeset line. It has no
    # width, height, visible text, paragraph break, or formula semantics.
    # A heading is a moving argument: never copy source bookkeeping into
    # the generated contents, auxiliary files, or bookmark strings.
    edge = blocks[-1] if end else blocks[0]
    if edge.get("t") == "Header":
        command = marker(n, end, inline=False)["c"][1]
        blocks.insert(len(blocks) if end else 1, {"t": "RawBlock", "c": ["latex", command]})
        return
    def attach(node):
        if isinstance(node, dict):
            kind = node.get("t")
            if kind == "Header":
                return False
            if kind in ["Para", "Plain"]:
                inlines = node["c"]
                edge_inline = inlines[-1] if end else inlines[0]
                if edge_inline.get("t") == "Math" and edge_inline["c"][0]["t"] == "DisplayMath":
                    edge_inline["sourceEnd" if end else "sourceBegin"] = n
                else:
                    inlines.insert(len(inlines) if end else 0, marker(n, end))
                return True
            if kind == "Figure":
                node["sourceEnd" if end else "sourceBegin"] = n
                return True
            children = list(node.values())
        elif isinstance(node, list):
            children = node
        else:
            return False
        return any(attach(child) for child in (reversed(children) if end else children))
    assert attach(blocks), (n, "no content line for source marker")


def merge_index_page(previous, current, body):
    """Continue the source's nested index, without repeating a parent entry.

    Pandoc parses a page's leading indented bullets as root bullets when the
    page is separated by a source sentinel. Restore only the explicit leading
    indentation, then combine adjacent root lists. Source markers already
    attached to the actual item lines travel with those items unchanged.
    """
    assert previous.get("t") == current.get("t") == "BulletList", "index pages must consist of source bullet lists"
    first = re.match(r"^([ \t]*)[-+*][ \t]+", body)
    assert first, "index source does not begin with a bullet"
    indent = len(first.group(1).expandtabs(4))
    if not indent:
        previous["c"].extend(current["c"])
        return
    assert indent % 2 == 0, "source index child indentation must have two-space levels"
    leading = 0
    for line in body.splitlines():
        if not line.strip():
            continue
        bullet = re.match(r"^([ \t]*)[-+*][ \t]+", line)
        assert bullet, "index page has non-list content"
        level = len(bullet.group(1).expandtabs(4))
        if level < indent:
            break
        if level == indent:
            leading += 1
    assert leading and leading <= len(current["c"]), "missing leading child index items"
    parent = previous["c"][-1]
    for _ in range(indent // 2 - 1):
        child = next((block for block in reversed(parent) if block.get("t") == "BulletList"), None)
        assert child and child["c"], "source child has no preceding parent at its explicit depth"
        parent = child["c"][-1]
    child = next((block for block in reversed(parent) if block.get("t") == "BulletList"), None)
    if child is None:
        child = {"t": "BulletList", "c": []}
        parent.append(child)
    child["c"].extend(current["c"][:leading])
    previous["c"].extend(current["c"][leading:])


def convert():
    WORK.mkdir(parents=True, exist_ok=True)
    reading = json.loads(subprocess.run(["node", "scripts/representation-theory-continuous-reading.mjs", "--json", "--language", "zh"], cwd=ROOT, text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout)
    sections = [s for s in reading["sections"] if not s.get("excludeFromPdf") and s["key"] not in ["title-pages", "title-page", "cover", "copyright", "contents"] and not s["key"].startswith("blank-")]
    website_sizes = json.loads((ROOT / "scripts/representation-theory-diagram-widths.json").read_text(encoding="utf8"))
    diagram_sizes = {}
    used_diagram_sizes = {}
    manifest = json.loads((ROOT / "scripts/representation-theory-source-manifest.json").read_text(encoding="utf8"))
    assert website_sizes["sourceSha256"] == manifest["sourceSha256"], "diagram calibration belongs to another source PDF"
    assert not website_sizes["pendingReviewPages"] and website_sizes["reviewRecordCount"] == manifest["pdfPageCount"], "original crop sizing cannot be exported before all source-page reviews are present"
    subprocess.run(["node", "scripts/finalize-representation-theory.mjs", "--check-sources"], cwd=ROOT, check=True)
    subprocess.run(["python", "scripts/check-representation-theory-audits.py", "--require-complete"], cwd=ROOT, check=True)
    pieces = []
    source_hashes = {}
    reading_bodies = {}
    pages = {}
    for section in sections:
        for page in section["pages"]:
            n = page["pdfPage"]
            p = ROOT / f"source/representation-theory/zh/pdf-{n:04d}.md"
            source_hashes[str(n)] = hashlib.sha256(p.read_bytes()).hexdigest()
            review = json.loads((ROOT / f"source/representation-theory/review/pdf-{n:04d}.json").read_text(encoding="utf8"))
            assert all(review[k] for k in ["visualReviewed", "englishTranscribed", "chineseTranslated", "formulaChecked"]) and not review["unresolved"], n
            assert str(review["printedPage"]) == str(manifest["pages"][n - 1].get("printedPage")), (n, "printed-page label differs from source inventory")
            assert review.get("zhSha256", review.get("sourceSha256", {}).get("zh") if isinstance(review.get("sourceSha256"), dict) else None) == source_hashes[str(n)], (n, "primary review is not bound to the exported Chinese snapshot")
            for diagram in review.get("diagrams", []):
                name = Path(diagram["path"]).name
                item = {"widthPt": diagram["widthPt"], "assetSha256": diagram.get("sha256", diagram.get("assetSha256")),
                        "clipPt": diagram.get("clipPt"), "sourcePdfPage": n}
                assert isinstance(item["widthPt"], (int, float)) and item["widthPt"] > 0, (n, diagram)
                if name in diagram_sizes:
                    assert diagram_sizes[name]["widthPt"] == item["widthPt"] and diagram_sizes[name]["assetSha256"] == item["assetSha256"], (n, name, "conflicting measured crop")
                scale = website_sizes["diagrams"].get(diagram["path"])
                assert scale and scale["widthPt"] == item["widthPt"] and scale["sha256"] == item["assetSha256"], (n, name, "original crop font calibration missing or stale")
                item["bodyFontPt"] = scale["bodyFontPt"]
                item["widthEm"] = scale["widthEm"]
                diagram_sizes[name] = item
            pages[n] = page
            complete_body = page["body"] + ("\n\n" + "\n\n".join(page["footnoteDefinitions"]) if page.get("footnoteDefinitions") else "")
            reading_bodies[str(n)] = complete_body
            pieces.append(f"REPresentationSource{n:04d}\n\n" + complete_body + "\n\n")
    md = "".join(pieces)
    ast = json.loads(subprocess.run(["pandoc", "-f", "markdown-fancy_lists", "-t", "json"], input=md, text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout)
    chunks = {}
    current = None
    for block in ast["blocks"]:
        if block.get("t") == "Para" and len(block["c"]) == 1 and block["c"][0].get("t") == "Str" and re.fullmatch(r"REPresentationSource\d{4}", block["c"][0]["c"]):
            current = int(block["c"][0]["c"][-4:])
            chunks[current] = []
        else:
            assert current is not None, block
            # Source heading levels differ between OCR batches. All numbered
            # mathematical sections belong to the same clickable TOC level.
            if block.get("t") == "Header" and block["c"][0] >= 2:
                heading = "".join(item.get("c", " ") for item in block["c"][2] if item.get("t") in ["Str", "Space"])
                if re.match(r"(?:§\s*)?\d+\.\d+\.?(?:\s|$)", heading):
                    block["c"][0] = 2
            chunks[current].append(block)

    joined = []
    joined_pages = []
    for section in sections:
        joined.append({"t": "RawBlock", "c": ["latex", r"\booksection{" + section["key"] + "}{" + escape_tex(section["title"]) + "}"]})
        # The final two lines of Chapter 8 otherwise occupy a separate page.
        # A modest local paragraph-gap reduction keeps its final exercise and
        # Hilbert-theorem caption together without changing text or font size.
        compact_section = section["key"] == "chapter-008"
        if compact_section:
            joined.append({"t": "RawBlock", "c": ["latex", r"\begingroup\setlength{\parskip}{3pt plus 1pt minus 1pt}"]})
        joined.append({"t": "Header", "c": [1, ["section-" + section["key"], [], []], [{"t": "Str", "c": section["title"]}]]})
        columns = {"notation-index": 3, "book-index": 2}.get(section["key"])
        if columns:
            joined.append({"t": "RawBlock", "c": ["latex", r"\begin{multicols}{" + str(columns) + "}"]})
        for page in section["pages"]:
            n = page["pdfPage"]
            blocks = chunks[n]
            attach_boundary(blocks, n)
            attach_boundary(blocks, n, end=True)
            if section["key"] == "book-index" and n != section["firstPdfPage"]:
                assert len(blocks) == 1 and blocks[0]["t"] == "BulletList", (n, "index page contains non-list blocks")
                merge_index_page(joined[-1], blocks[0], page["body"])
            elif page["joinsPrevious"]:
                assert joined[-1]["t"] == "Para" and blocks[0]["t"] == "Para", (n, "joining nonparagraph")
                if page.get("joinSeparator"):
                    joined[-1]["c"].append({"t": "Space"})
                joined[-1]["c"].extend(blocks[0]["c"])
                joined.extend(blocks[1:])
                joined_pages.append(n)
            else:
                joined.extend(blocks)
        if columns:
            joined.append({"t": "RawBlock", "c": ["latex", r"\end{multicols}"]})
        if compact_section:
            joined.append({"t": "RawBlock", "c": ["latex", r"\par\clearpage\endgroup"]})
    def display_paragraph(block):
        if not block or block.get("t") != "Para":
            return False
        displays = [item for item in block["c"] if item.get("t") == "Math" and item["c"][0]["t"] == "DisplayMath"]
        return len(displays) == 1 and all(item in displays or item.get("t") in ["Space", "SoftBreak"] or
                                         item.get("t") == "RawInline" and re.fullmatch(r"(?:\\leavevmode)?\\source(?:begin|end)\{\d+\}", item["c"][1])
                                         for item in block["c"])

    kept_formula_introducers = []
    kept_blocks = []
    for position, block in enumerate(joined):
        next_block = joined[position + 1] if position + 1 < len(joined) else None
        # Even a long paragraph can end with a bare "则" or "若". Protect
        # its last lines with the following display, while allowing TeX to
        # split the paragraph itself and separate consecutive displays.
        keep_with_display = block.get("t") == "Para" and not display_paragraph(block) and display_paragraph(next_block)
        if keep_with_display:
            intro = "".join(item["c"] if item.get("t") == "Str" else " "
                            if item.get("t") in ["Space", "SoftBreak"] else "" for item in block["c"]).strip()
            kept_formula_introducers.append(intro[:80])
        kept_blocks.append(block)
        if keep_with_display:
            # Insert the penalty in vertical mode, after the introductory
            # paragraph. TeX then chooses an earlier legal page boundary from
            # the actual block dimensions rather than reserving spare space.
            kept_blocks.append({"t": "RawBlock", "c": ["latex", r"\nopagebreak[4]"]})
    ast["blocks"] = kept_blocks
    counters = {"inlineMath": 0, "displayMath": 0, "diagrams": 0, "mathPunctuation": 0, "smallMath": 0}

    def image_command(url):
        assert url.startswith("/library/volume-88/diagrams/"), url
        asset = ROOT / "docs/public" / url.lstrip("/")
        assert asset.is_file(), asset
        assert asset.name in diagram_sizes, (asset, "original crop physical width must be recorded in the reviewed page")
        size = diagram_sizes[asset.name]
        assert hashlib.sha256(asset.read_bytes()).hexdigest() == size["assetSha256"], f"Diagram size snapshot stale: {asset}"
        used_diagram_sizes[asset.name] = size
        counters["diagrams"] += 1
        return r"\adjustbox{max width=\linewidth,max totalheight=.65\textheight}{\includegraphics[width=" + f"{size['widthEm']:.6f}em" + "]{" + asset.as_posix() + "}}"

    def walk(node):
        if isinstance(node, list):
            return [walk(v) for v in node]
        if not isinstance(node, dict):
            return node
        if node.get("t") == "Math":
            kind, tex = node["c"]
            small = bool(re.match(r"^\s*\\small\b", tex))
            if small:
                # TeX font-size declarations are text commands. Apply the
                # author's two small character tables before entering math,
                # keeping every mathematical cell unchanged.
                tex = re.sub(r"^\s*\\small\b\s*", "", tex)
                counters["smallMath"] += 1
            # Any Chinese sentence stop written inside $$ needs the CJK text
            # font; math fonts do not contain U+3002.
            counters["mathPunctuation"] += tex.count("。")
            tex = tex.replace("。", r"\text{。}")
            if kind["t"] == "DisplayMath":
                counters["displayMath"] += 1
                tags = re.findall(r"\\tag\*?\{[^}]*\}", tex)
                tex = re.sub(r"\\tag\*?\{[^}]*\}", "", tex)
                macro = r"\RepresentationTheorySmallDisplay{" if small else r"\RepresentationTheoryDisplay{"
                boundaries = "".join((r"\sourcebegin{" if key == "sourceBegin" else r"\sourceend{") + str(node[key]) + "}"
                                     for key in ["sourceBegin", "sourceEnd"] if key in node)
                return {"t": "RawInline", "c": ["latex", macro + tex + "}{" + "".join(tags) + boundaries + "}"]}
            counters["inlineMath"] += 1
            macro = r"\RepresentationTheorySmallInline{" if small else r"\RepresentationTheoryInline{"
            return {"t": "RawInline", "c": ["latex", macro + tex + "}"]}
        if node.get("t") == "Figure":
            images = []
            def find(v):
                if isinstance(v, dict):
                    if v.get("t") == "Image":
                        images.append(v["c"][2][0])
                    else:
                        for z in v.values(): find(z)
                elif isinstance(v, list):
                    for z in v: find(z)
            find(node["c"][2])
            assert images, node
            commands = [image_command(url) for url in images]
            before = r"\leavevmode\sourcebegin{" + str(node["sourceBegin"]) + "}" if "sourceBegin" in node else ""
            after = r"\sourceend{" + str(node["sourceEnd"]) + "}" if "sourceEnd" in node else ""
            return {"t": "RawBlock", "c": ["latex", "\\begin{center}\n" + before + "\n\n".join(commands) + after + "\n\\end{center}"]}
        if node.get("t") == "Image":
            return {"t": "RawInline", "c": ["latex", image_command(node["c"][2][0])]}
        return {k: walk(v) for k, v in node.items()}

    ast = walk(ast)
    body = subprocess.run(["pandoc", "-f", "json", "-t", "latex", "--wrap=none"], input=json.dumps(ast, ensure_ascii=False), text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout
    (WORK / "representation-theory.tex").write_text(PREAMBLE + body + "\n\\clearpage\n\\immediate\\closeout\\sourcemap\n\\end{document}\n", encoding="utf8")
    section_metadata = [{k: v for k, v in s.items() if k != "pages"} for s in sections]
    (WORK / "export-source-check.json").write_text(json.dumps({"pages": len(pages), "sections": section_metadata, "counts": counters, "sourceHashes": source_hashes, "readingBodies": reading_bodies, "joinedSourcePages": joined_pages, "generatedContents": True, "sourceSha256": manifest["sourceSha256"], "diagramSizes": used_diagram_sizes, "keptFormulaIntroducers": kept_formula_introducers}, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({"tex": str(WORK / "representation-theory.tex"), **counters}))


def build_page_mapping(page_count):
    snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
    events = [line.split() for line in (WORK / "representation-theory-page-map.tsv").read_text().splitlines()]
    starts = {int(n): int(physical) for kind, n, physical in events if kind == "S"}
    ends = {int(n): int(physical) for kind, n, physical in events if kind == "E"}
    retained = sorted(int(n) for n in snapshot["sourceHashes"])
    assert len(events) == 2 * len(retained)
    assert sorted(starts) == retained and sorted(ends) == retained
    assert all(1 <= starts[n] <= ends[n] <= page_count for n in retained)
    assert all(starts[a] <= starts[b] and ends[a] <= ends[b] for a, b in zip(retained, retained[1:])), "source boundaries must advance monotonically"
    mapping = []
    for n in retained:
        review = json.loads((ROOT / f"source/representation-theory/review/pdf-{n:04d}.json").read_text(encoding="utf8"))
        mapping.append({"sourcePdfPage": n, "printedPage": review["printedPage"], "firstExportPage": starts[n], "lastExportPage": ends[n]})
    by_source = {entry["sourcePdfPage"]: entry for entry in mapping}
    sections = {n: s for s in snapshot["sections"] for n in range(s["firstPdfPage"], s["lastPdfPage"] + 1)}
    physical_pages = []
    for physical in range(1, page_count + 1):
        sources = [n for n in retained if starts[n] <= physical <= ends[n]]
        if not sources:
            assert physical < starts[retained[0]], (physical, "content page without original source")
            physical_pages.append({"exportPage": physical, "sourcePdfPages": [], "originalLabel": "", "sectionTitle": "目录", "generated": True})
            continue
        printed = [str(by_source[n]["printedPage"]) for n in sources if by_source[n]["printedPage"] is not None]
        label = "原书 " + (printed[0] if printed[0] == printed[-1] else printed[0] + "–" + printed[-1]) if printed else ""
        physical_pages.append({"exportPage": physical, "sourcePdfPages": sources, "originalLabel": label, "sectionTitle": sections[sources[-1]]["title"]})
    return mapping, physical_pages


def write_page_headers(physical_pages):
    header_text = "\n".join(r"\expandafter\def\csname RepresentationTheory" + name + str(page["exportPage"]) + r"\endcsname{" + escape_tex(page[key]) + "}" for page in physical_pages for name, key in [("Original", "originalLabel"), ("Section", "sectionTitle")]) + "\n"
    path = WORK / "representation-theory-page-headers.tex"
    previous = path.read_text(encoding="utf8") if path.exists() else None
    path.write_text(header_text, encoding="utf8")
    return previous == header_text


def compile_pdf():
    from pypdf import PdfReader
    snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
    for number, sha in snapshot["sourceHashes"].items():
        source = ROOT / f"source/representation-theory/zh/pdf-{int(number):04d}.md"
        assert hashlib.sha256(source.read_bytes()).hexdigest() == sha, (number, "prepared source snapshot has changed; regenerate before compiling")
    # The first pass measures source ranges; later passes print those ranges.
    # Header dimensions stay fixed, but verify the map stabilizes before export.
    for cache in ["representation-theory-page-headers.tex", "representation-theory.aux", "representation-theory.toc", "representation-theory.out"]:
        (WORK / cache).unlink(missing_ok=True)
    for run in range(4):
        log = WORK / f"xelatex-pass-{run + 1}.txt"
        with log.open("w", encoding="utf8") as output:
            result = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "representation-theory.tex"], cwd=WORK, stdout=output, stderr=subprocess.STDOUT, text=True, encoding="utf8", errors="replace")
        if result.returncode:
            print(log.read_text(encoding="utf8")[-6000:])
            raise RuntimeError(f"XeLaTeX failed; see {log}")
        print(f"XeLaTeX pass {run + 1} completed", flush=True)
        _, physical_pages = build_page_mapping(len(PdfReader(WORK / "representation-theory.pdf").pages))
        stable = write_page_headers(physical_pages)
        if run >= 1 and stable:
            return
    raise RuntimeError("Original-page header map did not stabilize after four passes")


def finalize():
    from pypdf import PdfReader, PdfWriter
    reader = PdfReader(WORK / "representation-theory.pdf")
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    mapping, physical_pages = build_page_mapping(len(reader.pages))
    for page in physical_pages:
        label = "目录 " + str(page["exportPage"]) if page.get("generated") else page["originalLabel"].removeprefix("原书 ")
        writer.set_page_label(page["exportPage"] - 1, page["exportPage"] - 1, prefix=label)
    writer.add_metadata({"/Title": "表示论导论", "/Author": "Pavel Etingof et al.", "/Subject": "中文译本", "/Language": "zh-CN"})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("wb") as output:
        writer.write(output)
    snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
    by_source = {page["sourcePdfPage"]: page for page in mapping}
    section_starts = [{"key": section["key"], "firstExportPage": by_source[section["firstPdfPage"]]["firstExportPage"], "lastExportPage": by_source[section["lastPdfPage"]]["lastExportPage"]} for section in snapshot["sections"]]
    report = {"pdf": str(OUT), "pageCount": len(reader.pages), "originalPageCount": len(mapping), "excludedSourcePages": sorted(set(range(1, json.loads((ROOT / "scripts/representation-theory-source-manifest.json").read_text(encoding="utf8"))["pdfPageCount"] + 1)) - set(by_source)), "generatedContentsPages": sum(bool(page.get("generated")) for page in physical_pages), "bytes": OUT.stat().st_size, "pageMap": mapping, "physicalPages": physical_pages, "sectionStarts": section_starts}
    (WORK / "export-page-map.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({k: v for k, v in report.items() if k not in ["pageMap", "physicalPages", "sectionStarts"]}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--compile-only", action="store_true")
    args = parser.parse_args()
    if not args.compile_only:
        convert()
    if not args.prepare_only:
        compile_pdf()
        finalize()
