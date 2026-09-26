"""Extract the substantive images from the combined Global History PDF.

Usage:
    python scripts/extract-global-history-images.py path/to/global-history.pdf

Requires PyMuPDF and Pillow. Install with ``python -m pip install pymupdf pillow``.

The output directory is docs/public/library/volume-83/images. PDF page numbers and
image-block numbers in filenames are one-based. Image-block numbering includes
blocks that are skipped, so another importer can reproduce the same references.
"""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

import pymupdf
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "public" / "library" / "volume-83" / "images"
FIRST_PAGE = 17
LAST_PAGE = 1255
LOWER_VOLUME_FRONT_MATTER = range(642, 656)
MIN_DISPLAY_SIDE_PT = 50
WEBP_QUALITY = 90


def extract(pdf_path: Path) -> dict[str, object]:
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    document = pymupdf.open(pdf_path)
    if document.page_count < LAST_PAGE:
        raise ValueError(
            f"Expected at least {LAST_PAGE} pages, found {document.page_count}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    skipped: list[dict[str, object]] = []

    try:
        for page_number in range(FIRST_PAGE, LAST_PAGE + 1):
            if page_number in LOWER_VOLUME_FRONT_MATTER:
                continue

            page = document[page_number - 1]
            image_index = 0
            for block in page.get_text("dict")["blocks"]:
                if block["type"] != 1:
                    continue

                image_index += 1
                x0, y0, x1, y1 = block["bbox"]
                if min(x1 - x0, y1 - y0) < MIN_DISPLAY_SIDE_PT:
                    skipped.append({"page": page_number, "imageBlock": image_index})
                    continue

                filename = f"p{page_number:04d}-{image_index:02d}.webp"
                destination = OUTPUT_DIR / filename
                with Image.open(io.BytesIO(block["image"])) as source:
                    image = source.convert("RGB")
                    image.save(
                        destination,
                        format="WEBP",
                        quality=WEBP_QUALITY,
                        method=6,
                    )
                written.append(destination)
    finally:
        document.close()

    return {
        "outputDirectory": str(OUTPUT_DIR),
        "pageRange": [FIRST_PAGE, LAST_PAGE],
        "excludedLowerFrontMatter": [
            LOWER_VOLUME_FRONT_MATTER.start,
            LOWER_VOLUME_FRONT_MATTER.stop - 1,
        ],
        "quality": WEBP_QUALITY,
        "imageCount": len(written),
        "totalBytes": sum(path.stat().st_size for path in written),
        "skippedSmallBlocks": skipped,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Combined upper/lower volume PDF")
    args = parser.parse_args()
    print(json.dumps(extract(args.pdf), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
