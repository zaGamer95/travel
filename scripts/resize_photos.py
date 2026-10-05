#!/usr/bin/env python3
"""여행 사진을 블로그용 WebP로 줄입니다.

사용법:
    python3 scripts/resize_photos.py raw/2025-tokyo 2025-tokyo

- raw/2025-tokyo/ 안의 사진을 긴 변 1600px WebP로 줄여서
  assets/photos/2025-tokyo/ 에 저장합니다.
- 휴대폰 회전 정보를 반영하고, 위치(GPS) 등 EXIF 정보는 모두 지웁니다.
- 원본은 raw/ 에 두세요. raw/ 는 .gitignore 에 들어 있어 커밋되지 않습니다.

필요한 것: pip install pillow  (아이폰 HEIC 사진은 pip install pillow-heif 도)
"""
import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow가 필요해요: pip install pillow")

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".tif", ".tiff"}
REPO = Path(__file__).resolve().parent.parent


def main():
    p = argparse.ArgumentParser(description="여행 사진을 블로그용 WebP로 리사이즈")
    p.add_argument("src", type=Path, help="원본 사진 폴더 (예: raw/2025-tokyo)")
    p.add_argument("trip", help="여행 slug (예: 2025-tokyo)")
    p.add_argument("--size", type=int, default=1600, help="긴 변 픽셀 (기본 1600)")
    p.add_argument("--quality", type=int, default=80, help="WebP 품질 (기본 80)")
    p.add_argument("--rename", action="store_true",
                   help="찍은 순서대로 01.webp, 02.webp ... 로 이름 바꾸기")
    args = p.parse_args()

    files = sorted(f for f in args.src.iterdir() if f.suffix.lower() in EXTS)
    if not files:
        sys.exit(f"{args.src} 에 사진이 없어요.")

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
            im.save(out, "WEBP", quality=args.quality, method=6)  # EXIF는 저장하지 않음
        kb = out.stat().st_size // 1024
        total += kb
        print(f"{f.name} -> {out.relative_to(REPO)} ({im.width}x{im.height}, {kb}KB)")

    print(f"\n{len(files)}장, 총 {total / 1024:.1f}MB")


if __name__ == "__main__":
    main()
