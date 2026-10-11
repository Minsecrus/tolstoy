"""Extract the book's text layer and render reference pages, without claiming review.

Extraction does not invoke OCR. Formula transcription, translation, and visual
comparison are separately recorded in source/category-theory/review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = Path("C:/Users/29728/Downloads/Basic Category Theory (Tom Leinster) (z-library.sk, 1lib.sk, z-lib.sk).pdf")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, nargs="?", default=DEFAULT_PDF)
    parser.add_argument("--render", nargs=2, type=int, metavar=("FIRST", "LAST"))
    parser.add_argument("--dpi", type=int, default=145)
    parser.add_argument("--manifest", action="store_true", help="Write a source manifest; leave off when using the reviewed inventory")
    args = parser.parse_args()
    source = args.pdf.resolve()
    work = ROOT / "tmp/pdfs/category-theory"
    text_dir, image_dir = work / "text", work / "pages"
    text_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    pdf = pymupdf.open(source)
    with source.open("rb") as stream:
        sha = hashlib.file_digest(stream, "sha256").hexdigest()
    manifest = {"sourceFileName": source.name, "sourcePath": str(source), "sourceSha256": sha,
                "pdfPageCount": len(pdf), "title": "Basic Category Theory", "author": "Tom Leinster",
                "edition": "Cambridge Studies in Advanced Mathematics 143, 2014",
                "extractionNotice": "Extracted from the embedded text layer without OCR; extraction does not certify formula accuracy or visual review.",
                "pages": []}
    for number, page in enumerate(pdf, 1):
        text = page.get_text(sort=False)
        (text_dir / f"pdf-{number:04d}.txt").write_text(text, encoding="utf-8")
        manifest["pages"].append({"pdfPage": number, "widthPt": round(page.rect.width, 3),
                                  "heightPt": round(page.rect.height, 3), "embeddedTextCharacters": len(text),
                                  "embeddedTextSha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
    if args.manifest:
        target = ROOT / "scripts/category-theory-source-manifest.json"
        if target.exists():
            raise ValueError("A source manifest already exists; preserve its inventoried printed-page labels")
        target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Extracted {len(pdf)} text-layer reference pages; SHA-256 {sha}", flush=True)
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
