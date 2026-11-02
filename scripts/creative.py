#!/usr/bin/env python3
"""Branded social cards from a client's identity values. Writes self-contained HTML (one .slide per card, Adobe Express importable)
and a PNG per card via headless Edge.

  python scripts/creative.py <slug> <cards.json> <name>     cards.json = {"brand": {...}, "cards": [{"kind": "story|title", "lines": [...], "small": "..."}]}
                                                            → clients/<slug>/content/<YYYY-MM>/creative/<name>.html + <name>-<n>.png

Photos and Reels stay real (shot by the team); this makes only text cards: story greetings, Reel title cards, Google post images.
"""
import json, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CLIENTS = REPO / "clients"
EDGE = [Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"), Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe")]
W, H = 1080, 1920


def card_html(brand: dict, card: dict) -> str:
    bg = card.get("bg") or brand["bg"]
    fg = card.get("fg") or brand["fg"]
    accent = card.get("rule") or (fg if bg.lower() == brand["accent"].lower() else brand["accent"])
    lines = "".join(f"<div class='l'>{l}</div>" for l in card["lines"])
    small = card.get("small", "")
    size = card.get("size", 96 if card.get("kind") == "title" else 72)
    return f"""<div class='slide' style='background:{bg};color:{fg}'>
  <div class='mark' style='color:{fg}'>{brand['mark']}</div>
  <div class='rule' style='background:{accent}'></div>
  <div class='txt' style='font-size:{size}px'>{lines}</div>
  <div class='small'>{small}</div>
</div>"""


def build(slug: str, spec_path: str, name: str) -> Path:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    brand, cards = spec["brand"], spec["cards"]
    month = spec.get("month")
    out_dir = CLIENTS / slug / "content" / month / "creative"
    out_dir.mkdir(parents=True, exist_ok=True)
    css = f"""
@import url('https://fonts.googleapis.com/css2?family={brand['head_font'].replace(' ', '+')}:ital,wght@0,400;0,600;1,400&family={brand['text_font'].replace(' ', '+')}:wght@400;500&display=swap');
html, body {{ margin: 0; padding: 0; background: #ddd; }}
.slide {{ width: {W}px; height: {H}px; position: relative; box-sizing: border-box; padding: 140px 110px; font-family: '{brand['head_font']}', Georgia, serif; overflow: hidden; }}
.mark {{ position: absolute; top: 120px; left: 110px; font-family: '{brand['head_font']}', serif; font-size: 64px; letter-spacing: 0.22em; font-weight: 600; }}
.rule {{ position: absolute; top: 230px; left: 110px; width: 160px; height: 6px; }}
.txt {{ position: absolute; left: 110px; right: 110px; top: 50%; transform: translateY(-50%); line-height: 1.18; font-weight: 400; }}
.txt .l {{ margin-bottom: 28px; }}
.small {{ position: absolute; left: 110px; right: 110px; bottom: 140px; font-family: '{brand['text_font']}', Arial, sans-serif; font-size: 34px; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.85; }}
"""
    slides = "\n".join(card_html(brand, c) for c in cards)
    html = f"""<!doctype html><html lang='bg'><head><meta charset='utf-8'>
<meta name='viewport' content='width={W}'>
<meta name='hz:canvas-width' content='{W}'><meta name='hz:canvas-height' content='{H}'><meta name='hz:slide-selector' content='.slide'>
<title>{name}</title><style>{css}</style></head><body>{slides}</body></html>"""
    html_path = out_dir / f"{name}.html"
    html_path.write_text(html, encoding="utf-8")
    edge = next((e for e in EDGE if e.exists()), None)
    if edge:
        for i, c in enumerate(cards, 1):
            one = out_dir / f"{name}-{i}.html"
            one.write_text(html.replace(slides, card_html(brand, c)), encoding="utf-8")
            png = out_dir / f"{name}-{i}.png"
            subprocess.run([str(edge), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}", "--virtual-time-budget=6000", f"--screenshot={png}", one.resolve().as_uri()], check=True, capture_output=True, timeout=120)
            one.unlink()
            print(png)
    print(html_path)
    return html_path


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3])
