#!/usr/bin/env python3
"""Shrink trip photos to WebP for the blog.

Usage:
    python3 scripts/resize_photos.py raw/2025-tokyo 2025-tokyo

- Resizes the photos in raw/2025-tokyo/ to WebP, 1600px on the long side,
  and saves them to assets/photos/2025-tokyo/.
- Applies phone rotation and strips all EXIF data, including GPS location.
- Keep originals in raw/. raw/ is in .gitignore, so it is never committed.

Requires: pip install pillow  (plus pip install pillow-heif for iPhone HEIC photos)
"""
import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".tif", ".tiff"}
REPO = Path(__file__).resolve().parent.parent


def main():
    p = argparse.ArgumentParser(description="Resize trip photos to WebP for the blog")
    p.add_argument("src", type=Path, help="folder of original photos (e.g. raw/2025-tokyo)")
    p.add_argument("trip", help="trip slug (e.g. 2025-tokyo)")
    p.add_argument("--size", type=int, default=1600, help="long side in pixels (default 1600)")
    p.add_argument("--quality", type=int, default=80, help="WebP quality (default 80)")
    p.add_argument("--rename", action="store_true",
                   help="rename to 01.webp, 02.webp ... in the order taken")
    args = p.parse_args()

    files = sorted(f for f in args.src.iterdir() if f.suffix.lower() in EXTS)
    if not files:
        sys.exit(f"No photos found in {args.src}.")

    out_dir = REPO / "assets" / "photos" / args.trip
    out_dir.mkdir(parents=True, exist_ok=True)

    total = 0
    for i, f in enumerate(files, 1):
        name = f"{i:02d}.webp" if args.rename else f.stem.lower().replace(" ", "-") + ".webp"
        out = out_dir / name
        with Image.open(f) as im:
            im = ImageOps.exif_transpose(im)
            im.thumbnail((args.size, args.size), Image.LANCZOS)
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGB")
            im.save(out, "WEBP", quality=args.quality, method=6)  # EXIF is not saved
        kb = out.stat().st_size // 1024
        total += kb
        print(f"{f.name} -> {out.relative_to(REPO)} ({im.width}x{im.height}, {kb}KB)")

    print(f"\n{len(files)} photos, {total / 1024:.1f}MB total")


if __name__ == "__main__":
    main()
