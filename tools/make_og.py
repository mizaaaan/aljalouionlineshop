#!/usr/bin/env python3
"""Generate the 1200x630 Open Graph share image for Al Jaloui Mart.

Run from the repo root:  python3 tools/make_og.py
Then commit the updated og-image.png.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NAVY    = (27, 42, 78)
NAVY_D  = (16, 28, 56)
YELLOW  = (247, 225, 0)
GOLD    = (200, 166, 0)
CREAM   = (252, 249, 225)
LINE    = (229, 225, 198)
INK_SOF = (91, 100, 120)
WHITE   = (255, 255, 255)


def find_font(names):
    """First existing font path from a list of candidates."""
    for path in names:
        if os.path.exists(path):
            return path
    raise SystemExit("No usable font found for the OG image.")


FONT_B = find_font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "/opt/freestyle/python/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf",
])
FONT_R = find_font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    "/opt/freestyle/python/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf",
])

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

# --- Soft cream background shapes ---
d.ellipse((650, -320, 1430, 460), fill=CREAM)
d.ellipse((-220, 440, 250, 910), fill=CREAM)

# --- Thin brand frame ---
d.rounded_rectangle((22, 22, W - 22, H - 22), radius=26, outline=LINE, width=3)

# --- Logo mark: yellow bag, navy handle, navy chat bubble ---
# Geometry is authored in the same 120x130 space as the inline SVG logo.
S, OX, OY = 3.0, 110, 130


def T(x, y):
    return (OX + x * S, OY + y * S)


# handle: arch drawn first so the bag covers its feet
d.arc((*T(41, 6), *T(78, 54)), start=180, end=360, fill=NAVY, width=int(9 * S))
for hx in (41, 78):
    d.line((*T(hx, 30), *T(hx, 44)), fill=NAVY, width=int(9 * S))
# bag body
d.rounded_rectangle((*T(8, 37), *T(105, 128)), radius=14 * S, fill=YELLOW)
# the bite: the smooth hook cut out of the bottom-right corner (same
# bezier segments as the inline SVG logo path)

def cubic(p0, c1, c2, p3, n=24):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts

bite = []
bite += cubic((105, 64), (105, 78), (96, 88), (84, 90))
bite += cubic((84, 90), (72, 92), (60, 102), (57, 112))
bite += cubic((57, 112), (56, 120), (62, 127), (72, 128))
d.polygon([T(x, y) for x, y in bite] + [T(105, 128)], fill=WHITE)
# chat bubble (rounded triangle pointing right)
bubble = [T(84, 92), T(119, 107), T(88, 127)]
d.polygon(bubble, fill=NAVY)
d.line(bubble + [bubble[0]], fill=NAVY, width=int(9 * S), joint="curve")
for x, y in bubble:
    r = 5 * S
    d.ellipse((x - r, y - r, x + r, y + r), fill=NAVY)

# --- Wordmark ---
x0 = 640
wm = ImageFont.truetype(FONT_B, 64)
d.text((x0, 168), "Al Jaloui", font=wm, fill=NAVY)

sub = ImageFont.truetype(FONT_B, 21)
x = x0 + 4
for ch in "MART":
    d.text((x, 262), ch, font=sub, fill=NAVY)
    x += d.textbbox((0, 0), ch, font=sub)[2] + 13

# yellow accent bar
d.rounded_rectangle((x0 + 4, 322, x0 + 132, 334), radius=6, fill=YELLOW)

# tagline
d.text((x0 + 4, 362), "To the satisfaction of Almighty.",
       font=ImageFont.truetype(FONT_R, 29), fill=INK_SOF)

# separator
d.line((x0 + 4, 432, x0 + 500, 432), fill=LINE, width=2)


def fit(text, font_path, size, maxw):
    """Largest font size <= size whose rendered text fits maxw."""
    while size > 10:
        f = ImageFont.truetype(font_path, size)
        if d.textbbox((0, 0), text, font=f)[2] - d.textbbox((0, 0), text, font=f)[0] <= maxw:
            return f
        size -= 1
    return ImageFont.truetype(font_path, size)


lines = [
    "Essentials \u00b7 Mother & Baby \u00b7 Personal Care",
    "Health devices \u00b7 Cash on delivery",
    "Doha, Qatar",
]
y = 452
for text in lines:
    f = fit(text, FONT_R, 20, 500)
    d.text((x0 + 4, y), text, font=f, fill=INK_SOF)
    y += 30

order_line = "Order on WhatsApp \u00b7 +974 7473 3400"
d.text((x0 + 4, y + 6), order_line, font=fit(order_line, FONT_B, 22, 500), fill=NAVY)

out = "og-image.png"
img.save(out, "PNG", optimize=True)
print("saved", out, img.size, f"{os.path.getsize(out)/1024:.0f} KB")
