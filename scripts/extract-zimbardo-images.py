"""Extract the illustrations from the Chinese eighth edition of Zimbardo Psychology.

Usage:
    python scripts/extract-zimbardo-images.py path/to/zimbardo-psychology.pdf

Requires PyMuPDF and Pillow. The PDF stays outside the repository; WebP assets go
to docs/public/library/volume-84/images. Filenames use the one-based PDF page
number and the one-based order of image blocks on that page. Read image blocks
from ``get_text("dict")``: ``get_images()`` omits many inline charts in this PDF.
"""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

import pymupdf
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "public" / "library" / "volume-84" / "images"
FIRST_PAGE = 19
LAST_PAGE = 1556
EXPECTED_IMAGE_COUNT = 633
WEBP_QUALITY = 90


def extract(pdf_path: Path) -> dict[str, object]:
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    written: list[Path] = []
    with pymupdf.open(pdf_path) as document:
        if document.page_count != LAST_PAGE:
            raise ValueError(
                f"Expected the {LAST_PAGE}-page edition, found {document.page_count} pages"
            )

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for page_number in range(FIRST_PAGE, LAST_PAGE + 1):
            page = document[page_number - 1]
            image_index = 0
            for block in page.get_text("dict")["blocks"]:
                if block["type"] != 1:
                    continue

                image_index += 1
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

    if len(written) != EXPECTED_IMAGE_COUNT:
        raise ValueError(
            f"Expected {EXPECTED_IMAGE_COUNT} image blocks, found {len(written)}; "
            "check that this is the same PDF edition"
        )

    return {
        "outputDirectory": str(OUTPUT_DIR),
        "pageRange": [FIRST_PAGE, LAST_PAGE],
        "quality": WEBP_QUALITY,
        "imageCount": len(written),
        "totalBytes": sum(path.stat().st_size for path in written),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Zimbardo Psychology PDF")
    args = parser.parse_args()
    print(json.dumps(extract(args.pdf), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
