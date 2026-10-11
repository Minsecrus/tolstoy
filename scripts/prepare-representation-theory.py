"""Extract the supplied book's existing text layer and render reference pages.

The source is a scanned AMS print edition with an existing recognized text layer.
Extraction and rendering do not assert transcription, translation, or review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = Path("C:/Users/29728/Downloads/Introduction to Representation Theory (Pavel Etingof, Oleg Golberg etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, nargs="?", default=DEFAULT_PDF)
    parser.add_argument("--render", nargs=2, type=int, metavar=("FIRST", "LAST"))
    parser.add_argument("--dpi", type=int, default=145)
    parser.add_argument("--manifest", action="store_true", help="Write an initial manifest; leave off after inventoried page labels are added")
    args = parser.parse_args()
    source = args.pdf.resolve()
    work = ROOT / "tmp/pdfs/representation-theory"
    text_dir, image_dir = work / "text", work / "pages"
    text_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    pdf = pymupdf.open(source)
    with source.open("rb") as stream:
        sha = hashlib.file_digest(stream, "sha256").hexdigest()
    manifest = {"sourceFileName": source.name, "sourcePath": str(source), "sourceSha256": sha,
                "pdfPageCount": len(pdf), "title": "Introduction to Representation Theory",
                "chineseTitle": "表示论导论", "volumeNumber": 88,
                "authors": ["Pavel Etingof", "Oleg Golberg", "Sebastian Hensel", "Tiankai Liu", "Alex Schwendner", "Dmitry Vaintrob", "Elena Yudovina"],
                "historicalInterludesAuthor": "Slava Gerovitch", "edition": "AMS Student Mathematical Library 59, 2011",
                "sourceWorkingPath": "source/representation-theory",
                "extractionMethod": "existing recognized PDF text layer, without full-book OCR",
                "extractionNotice": "The supplied PDF is a scan with an existing recognized text layer. Extracted prose and formula glyphs can contain recognition errors; actual source page images remain authoritative. Extraction or rendering alone does not certify mathematical accuracy or visual review.",
                "metadata": pdf.metadata, "originalBookmarks": pdf.get_toc(),
                "originalPageLabels": pdf.get_page_labels(), "renderDpi": args.dpi, "pages": []}
    for number, page in enumerate(pdf, 1):
        content = page.get_text(sort=False)
        (text_dir / f"pdf-{number:04d}.txt").write_text(content, encoding="utf-8")
        manifest["pages"].append({"pdfPage": number, "widthPt": round(page.rect.width, 3),
                                  "heightPt": round(page.rect.height, 3), "embeddedTextCharacters": len(content),
                                  "embeddedTextSha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                                  "hasTextLayer": bool(content.strip()), "embeddedPageLabel": page.get_label(),
                                  "textPath": f"tmp/pdfs/representation-theory/text/pdf-{number:04d}.txt",
                                  "renderPath": f"tmp/pdfs/representation-theory/pages/pdf-{number:04d}.png"})
    if args.manifest:
        target = ROOT / "scripts/representation-theory-source-manifest.json"
        if target.exists():
            raise ValueError("A source manifest already exists; preserve its inventoried labels")
        target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Extracted {len(pdf)} existing text-layer reference pages; SHA-256 {sha}", flush=True)
    if args.render:
        first, last = args.render
        if not 1 <= first <= last <= len(pdf):
            raise ValueError("Render range is outside the PDF")
        for number in range(first, last + 1):
            target = image_dir / f"pdf-{number:04d}.png"
            if not target.exists():
                pdf[number - 1].get_pixmap(dpi=args.dpi, alpha=False).save(target)
            if number % 10 == 0 or number == last:
                print(f"Rendered PDF page {number}", flush=True)


if __name__ == "__main__":
    main()
