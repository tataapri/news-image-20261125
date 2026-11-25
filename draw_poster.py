#!/usr/bin/env python3
"""Draw the news poster for Wednesday, 25 November 2026.

Flat vector-style newspaper front page, drawn entirely with Pillow
primitives: no photos, no downloaded artwork. Regenerates entry.png
(1024x1024, under 1 MiB).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (24, 24, 24)
RULE = (24, 24, 24)
ACCENT = (158, 28, 28)
MUTED = (90, 84, 72)
CARD = (255, 255, 255)
SKY = (178, 214, 235)
SEA = (46, 110, 158)
SEA_DARK = (28, 78, 120)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, fnt, fill, leading):
    for line in lines:
        d.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_ship(d, x0, y0, x1, y1):
    """Cargo ship on the sea, drone above, smoke plume."""
    d.rectangle([x0, y0, x1, y1], fill=SKY)
    d.rectangle([x0, y1 - 34, x1, y1], fill=SEA)
    d.rectangle([x0, y1 - 30, x1, y1 - 26], fill=SEA_DARK)
    # sun
    d.ellipse([x1 - 52, y0 + 10, x1 - 16, y0 + 46], fill=(246, 196, 69))
    # hull
    d.polygon([(x0 + 60, y1 - 62), (x0 + 330, y1 - 62), (x0 + 310, y1 - 30),
               (x0 + 84, y1 - 30)], fill=(158, 28, 28))
    d.rectangle([x0 + 60, y1 - 62, x0 + 330, y1 - 56], fill=(120, 20, 20))
    # containers
    cols = [(52, 110, 158), (246, 196, 69), (70, 140, 90), (220, 120, 40)]
    for i, c in enumerate(cols):
        d.rectangle([x0 + 78 + i * 62, y1 - 108, x0 + 132 + i * 62, y1 - 62],
                    fill=c, outline=(24, 24, 24), width=2)
    # bridge tower
    d.rectangle([x0 + 330, y1 - 108, x0 + 356, y1 - 62], fill=(240, 240, 240),
                outline=(24, 24, 24), width=2)
    d.rectangle([x0 + 336, y1 - 100, x0 + 350, y1 - 88], fill=(46, 110, 158))
    # drone, high in the sky clear of the ship
    dx, dy = x0 + 392, y0 + 30
    d.ellipse([dx - 22, dy - 4, dx - 8, dy + 4], fill=INK)
    d.ellipse([dx + 8, dy - 4, dx + 22, dy + 4], fill=INK)
    d.rectangle([dx - 10, dy - 3, dx + 10, dy + 3], fill=INK)
    d.line([(dx, dy + 3), (dx + 14, dy + 16)], fill=INK, width=2)
    d.ellipse([dx + 8, dy + 14, dx + 20, dy + 26], fill=ACCENT)
    # waves
    for wx in range(x0 + 10, x1 - 10, 46):
        d.arc([wx, y1 - 20, wx + 34, y1 - 6], 180, 360, fill=(255, 255, 255), width=3)


def draw_tower(d, x0, y0, x1, y1):
    """Skyscraper with a damaged facade, city skyline at dusk."""
    d.rectangle([x0, y0, x1, y1], fill=(250, 196, 110))
    d.ellipse([x0 + 18, y0 + 12, x0 + 58, y0 + 52], fill=(246, 220, 120))
    # distant skyline
    for bx, bh in ((0, 44), (52, 62), (300, 50), (352, 70)):
        d.rectangle([x0 + bx, y1 - bh, x0 + bx + 46, y1], fill=(120, 110, 100))
    # main tower
    tx0, tx1 = x0 + 150, x0 + 250
    d.polygon([(tx0, y1), (tx0, y0 + 8), (tx0 + 50, y0), (tx1, y0 + 8),
               (tx1, y1)], fill=(70, 90, 120))
    for wy in range(y0 + 22, y1 - 8, 16):
        for wx in range(tx0 + 8, tx1 - 14, 16):
            d.rectangle([wx, wy, wx + 8, wy + 8], fill=(246, 220, 120))
    # damage: dark scorch patch mid-facade
    d.ellipse([tx0 + 18, y0 + 52, tx1 - 8, y0 + 92], fill=(40, 36, 32))
    d.ellipse([tx0 + 30, y0 + 60, tx1 - 20, y0 + 84], fill=(90, 60, 40))
    # smoke
    for i, r in enumerate((10, 8, 6)):
        d.ellipse([tx0 + 8 + i * 12, y0 + 40 - i * 8,
                   tx0 + 8 + i * 12 + r * 2, y0 + 40 - i * 8 + r * 2],
                  fill=(110, 110, 110))
    # ground
    d.rectangle([x0, y1 - 10, x1, y1], fill=(90, 80, 70))


def draw_laptop(d, x0, y0, x1, y1):
    """Laptop with a warning shield: a cyber breach."""
    d.rectangle([x0, y0, x1, y1], fill=(52, 68, 92))
    # binary rain
    import random
    rnd = random.Random(7)
    for _ in range(26):
        bx = rnd.randint(x0 + 6, x1 - 16)
        by = rnd.randint(y0 + 6, y1 - 40)
        d.text((bx, by), rnd.choice("01"), font=font(SANS, 11),
               fill=(120, 160, 200))
    # laptop
    lx0, ly0, lx1, ly1 = x0 + 96, y0 + 34, x1 - 96, y1 - 44
    d.rectangle([lx0, ly0, lx1, ly1], fill=(24, 24, 24))
    d.rectangle([lx0 + 8, ly0 + 8, lx1 - 8, ly1 - 8], fill=(178, 214, 235))
    d.polygon([(lx0 - 26, ly1 + 14), (lx1 + 26, ly1 + 14), (lx1, ly1),
               (lx0, ly1)], fill=(60, 60, 60))
    # warning triangle on screen
    cx, cy = (lx0 + lx1) // 2, (ly0 + ly1) // 2
    d.polygon([(cx, cy - 26), (cx + 26, cy + 16), (cx - 26, cy + 16)],
              fill=(246, 196, 69), outline=INK)
    d.rectangle([cx - 2, cy - 14, cx + 2, cy + 2], fill=INK)
    d.ellipse([cx - 2, cy + 7, cx + 2, cy + 11], fill=INK)


def draw_court(d, x0, y0, x1, y1):
    """Courthouse columns with a gavel."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 200, 170))
    # pediment
    d.polygon([(x0 + 60, y0 + 46), (x0 + 190, y0 + 10), (x0 + 320, y0 + 46)],
              fill=(120, 100, 80))
    d.rectangle([x0 + 60, y0 + 46, x0 + 320, y0 + 56], fill=(90, 76, 60))
    # columns
    for cx in (86, 150, 214, 278):
        d.rectangle([x0 + cx, y0 + 56, x0 + cx + 22, y1 - 26], fill=(240, 236, 224))
        d.rectangle([x0 + cx - 4, y0 + 52, x0 + cx + 26, y0 + 60], fill=(240, 236, 224))
        d.rectangle([x0 + cx - 4, y1 - 30, x0 + cx + 26, y1 - 22], fill=(240, 236, 224))
    d.rectangle([x0 + 40, y1 - 22, x0 + 340, y1 - 12], fill=(90, 76, 60))


def draw_clinic(d, x0, y0, x1, y1):
    """Hospital building with a red cross, ambulance leaving."""
    d.rectangle([x0, y0, x1, y1], fill=(190, 220, 190))
    d.ellipse([x0 + 20, y0 + 10, x0 + 66, y0 + 56], fill=(246, 220, 120))
    # hills
    d.pieslice([x0 - 40, y1 - 60, x0 + 180, y1 + 40], 180, 360, fill=(120, 170, 110))
    d.pieslice([x0 + 200, y1 - 70, x0 + 420, y1 + 40], 180, 360, fill=(100, 150, 95))
    # clinic building
    d.rectangle([x0 + 60, y0 + 46, x0 + 240, y1 - 18], fill=(255, 255, 255),
                outline=INK, width=2)
    d.rectangle([x0 + 60, y0 + 46, x0 + 240, y0 + 62], fill=ACCENT)
    for wy in range(y0 + 74, y1 - 26, 22):
        for wx in (x0 + 78, x0 + 112, x0 + 146, x0 + 180):
            d.rectangle([wx, wy, wx + 18, wy + 14], fill=(120, 170, 200))
    # red cross sign
    cx, cy = x0 + 290, y0 + 66
    d.rectangle([cx - 8, cy - 22, cx + 8, cy + 22], fill=ACCENT)
    d.rectangle([cx - 22, cy - 8, cx + 22, cy + 8], fill=ACCENT)
    # ambulance
    ax, ay = x0 + 268, y1 - 44
    d.rectangle([ax, ay, ax + 92, ay + 26], fill=(255, 255, 255), outline=INK, width=2)
    d.rectangle([ax + 62, ay + 4, ax + 92, ay + 26], fill=(178, 214, 235), outline=INK, width=2)
    d.rectangle([ax + 8, ay + 8, ax + 18, ay + 18], fill=ACCENT)
    d.ellipse([ax + 14, ay + 22, ax + 30, ay + 38], fill=INK)
    d.ellipse([ax + 66, ay + 22, ax + 82, ay + 38], fill=INK)


def draw_scales(d, x0, y0, x1, y1):
    """Scales of justice over the French tricolore."""
    d.rectangle([x0, y0, x1, y1], fill=(240, 236, 224))
    # tricolore ribbon across the top
    d.rectangle([x0, y0, x0 + (x1 - x0) // 3, y0 + 18], fill=(0, 85, 164))
    d.rectangle([x0 + (x1 - x0) // 3, y0, x0 + 2 * (x1 - x0) // 3, y0 + 18],
                fill=(255, 255, 255))
    d.rectangle([x0 + 2 * (x1 - x0) // 3, y0, x1, y0 + 18], fill=(239, 65, 53))
    # scales
    cx = (x0 + x1) // 2
    d.rectangle([cx - 3, y0 + 26, cx + 3, y1 - 22], fill=(120, 100, 60))
    d.rectangle([cx - 46, y0 + 30, cx + 46, y0 + 36], fill=(120, 100, 60))
    d.ellipse([cx - 6, y0 + 22, cx + 6, y0 + 34], fill=(196, 164, 90))
    for side in (-1, 1):
        sx = cx + side * 42
        d.line([(cx + side * 44, y0 + 33), (sx - 18, y0 + 66)], fill=INK, width=2)
        d.line([(cx + side * 44, y0 + 33), (sx + 18, y0 + 66)], fill=INK, width=2)
        d.pieslice([sx - 22, y0 + 62, sx + 22, y0 + 86], 0, 180, fill=(196, 164, 90))
    d.rectangle([cx - 34, y1 - 22, cx + 34, y1 - 14], fill=(120, 100, 60))


STORIES = [
    ("UKRAINE · BALTIC SEA", "KYIV OWNS BALTIC SHIP STRIKE",
     "Zelenskyy confirms Ukraine's drone hit the Russian cargo ship "
     "Sparta II in the Gulf of Finland.",
     draw_ship),
    ("SAUDI ARABIA", "RIYADH TOWER HIT AGAIN",
     "A Houthi drone hits Riyadh's tallest tower, the PIF headquarters, "
     "again; 11 people wounded.",
     draw_tower),
    ("WASHINGTON", "CIA AND ODNI HACKED",
     "Intruders breach an unclassified intelligence system; no classified "
     "data was hit, officials say.",
     draw_laptop),
    ("NEW YORK · TECH", "HUAWEI FOUND GUILTY",
     "A Brooklyn jury convicts the Chinese telecom giant on 10 of 12 "
     "counts, including bank fraud.",
     draw_court),
    ("DR CONGO", "WHO FLEES CONGO FIGHTING",
     "Health workers leave an Ituri hospital after three days sheltering "
     "from fighting amid Ebola.",
     draw_clinic),
    ("FRANCE", "SARKOZY TO STAND TRIAL",
     "A corruption case against the ex-president and his wife Carla Bruni "
     "is ordered to trial.",
     draw_scales),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 28  # margin

    # ---- Masthead ----
    d.text((W // 2, 24), "THE WORLD TODAY", font=font(SERIF_B, 78),
           fill=INK, anchor="ma")
    d.rectangle([m, 118, W - m, 122], fill=RULE)
    d.text((W // 2, 130), "WEDNESDAY, 25 NOVEMBER 2026",
           font=font(SANS_B, 40), fill=ACCENT, anchor="ma")
    d.rectangle([m, 180, W - m, 184], fill=RULE)
    d.rectangle([m, 188, W - m, 190], fill=RULE)

    # ---- Story grid: 2 columns x 3 rows ----
    gx, gy = m, 200
    cw = (W - 2 * m - 14) // 2
    ch = 248
    gap = 14
    head_f = font(SANS_B, 25)
    cap_f = font(SANS, 18)
    kick_f = font(SANS_B, 15)

    for i, (kicker, headline, caption, draw_art) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = gx + col * (cw + gap)
        y0 = gy + row * (ch + gap)
        x1, y1 = x0 + cw, y0 + ch
        d.rectangle([x0, y0, x1, y1], fill=CARD, outline=(200, 192, 176), width=2)
        # illustration panel
        art_h = 118
        draw_art(d, x0 + 2, y0 + 2, x1 - 2, y0 + 2 + art_h)
        d.rectangle([x0 + 2, y0 + 2 + art_h, x1 - 2, y0 + 2 + art_h + 2], fill=RULE)
        tx = x0 + 14
        ty = y0 + 2 + art_h + 8
        d.text((tx, ty), kicker, font=kick_f, fill=ACCENT)
        ty += 22
        lines = wrap(d, headline, head_f, cw - 28)
        ty = text_block(d, tx, ty, lines[:2], head_f, INK, 27)
        ty += 4
        lines = wrap(d, caption, cap_f, cw - 28)
        text_block(d, tx, ty, lines[:2], cap_f, MUTED, 20)

    # ---- Footer ----
    fy = gy + 3 * ch + 2 * gap + 10
    d.rectangle([m, fy, W - m, fy + 2], fill=RULE)
    d.text((W // 2, fy + 10),
           "All six stories reported on Wednesday, 25 November 2026  ·  "
           "Sources: Reuters, Bloomberg, CNN, AP",
           font=font(SANS_B, 17), fill=INK, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
