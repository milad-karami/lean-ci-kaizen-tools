#!/usr/bin/env python3
"""Übernimmt eine (Codex-)Illustration für ein Tool in beide benötigten Größen.

Usage:  python3 build/add_art.py <tool-id> <bild.png|jpg|webp>
        z. B. python3 build/add_art.py prozess-analyse ~/Downloads/prozess-analyse.png

Schreibt
  assets/illustrations/<tool-id>.webp   960 × 600  (Startseite, README)
  build/art/<tool-id>.webp              560 × 350  (im Tool eingebettet)
Das Bild wird mittig auf das Seitenverhältnis 16:10 zugeschnitten. Danach build.py, hub.py und readme.py ausführen.
"""
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SIZES = [(ROOT / "assets" / "illustrations", (960, 600), 84), (ROOT / "build" / "art", (560, 350), 80)]


def crop_16_10(im):
    w, h = im.size
    target = 16 / 10
    if w / h > target:            # zu breit -> links/rechts kürzen
        nw = round(h * target)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = round(w / target)        # zu hoch -> oben/unten kürzen
    y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    tool_id, src = sys.argv[1], Path(sys.argv[2]).expanduser()
    ids = [t["id"] for t in json.loads((ROOT / "build" / "toolkit.json").read_text(encoding="utf-8"))["tools"]]
    if tool_id not in ids:
        raise SystemExit(f"Unbekannte Tool-ID „{tool_id}“. Bekannt: {', '.join(ids)}")
    im = crop_16_10(Image.open(src).convert("RGB"))
    for folder, size, quality in SIZES:
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / f"{tool_id}.webp"
        im.resize(size, Image.LANCZOS).save(out, "WEBP", quality=quality, method=6)
        print(f"geschrieben: {out.relative_to(ROOT)}  {size[0]}×{size[1]}  ({out.stat().st_size // 1024} KB)")
    print("Jetzt: python3 build/build.py && python3 build/hub.py && python3 build/readme.py")


if __name__ == "__main__":
    main()
