"""News image for Tuesday 24 November 2026.

Draws a 1024x1024 newspaper front page with Python's standard
library only: a hand-written PNG encoder (zlib + CRC), rectangle /
circle / triangle primitives, and a 5x7 bitmap font scaled up so
every label stays legible at 300 pixels across. No network, no
randomness, no wall clock: two runs write identical bytes.

Stories (all first reported on 24 Nov 2026, cross-checked this
morning): South Korea scrambles jets as Russian planes enter its
air-defence zone near Ulleung Island; Gukesh defends the world
chess title against Sindarov, Game 1 in Geneva; Modi and Nepal's
PM flag off the Saryu-Kamala Express; the US blacklists Alibaba's
Singapore unit Apex; Fiji shuts all schools for five days as the
El Nino drought deepens; Brazil's lower house backs Lula's
fiscal plan (footer ticker).
"""

import os
import struct
import zlib

W = 1024
H = 1024

CREAM = (247, 242, 230)
NAVY = (16, 36, 62)
NAVY2 = (24, 52, 88)
GOLD = (212, 164, 32)
WHITE = (255, 255, 255)
INK = (18, 22, 30)
GREY = (92, 98, 110)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
ORANGE = (224, 110, 30)
SKY = (176, 214, 235)
GREEN = (34, 120, 70)

FONT = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("01110", "00100", "00100", "00100", "00100", "00100", "01110"),
    "J": ("00111", "00010", "00010", "00010", "00010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "11011", "10001"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00110", "01000", "10000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    "6": ("01110", "10000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00001", "01110"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
    "-": ("00000", "00000", "00000", "01110", "00000", "00000", "00000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    ",": ("00000", "00000", "00000", "00000", "01100", "00100", "01000"),
    ":": ("00000", "01100", "01100", "00000", "01100", "01100", "00000"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    "'": ("00100", "00100", "01000", "00000", "00000", "00000", "00000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    "%": ("11001", "11010", "00010", "00100", "01000", "01011", "10011"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "!": ("00100", "00100", "00100", "00100", "00100", "00000", "00100"),
    "?": ("01110", "10001", "00001", "00110", "00100", "00000", "00100"),
    "&": ("01100", "10010", "10100", "01000", "10101", "10010", "01101"),
}

BUF = bytearray(W * H * 3)


def px(x, y, color):
    if 0 <= x < W and 0 <= y < H:
        i = (y * W + x) * 3
        BUF[i], BUF[i + 1], BUF[i + 2] = color


def rect(x, y, w, h, color):
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            px(xx, yy, color)


def circle(cx, cy, r, color):
    for yy in range(cy - r, cy + r + 1):
        for xx in range(cx - r, cx + r + 1):
            if (xx - cx) * (xx - cx) + (yy - cy) * (yy - cy) <= r * r:
                px(xx, yy, color)


def line(x0, y0, x1, y1, color, thick=1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy), 1)
    for s in range(steps + 1):
        x = x0 + dx * s // steps
        y = y0 + dy * s // steps
        for ty in range(thick):
            for tx in range(thick):
                px(x + tx, y + ty, color)


def tri(x0, y0, x1, y1, x2, y2, color):
    lo = min(y0, y1, y2)
    hi = max(y0, y1, y2)
    for y in range(lo, hi + 1):
        xs = []
        for (ax, ay, bx, by) in ((x0, y0, x1, y1), (x1, y1, x2, y2), (x2, y2, x0, y0)):
            if ay == by:
                continue
            if min(ay, by) <= y < max(ay, by):
                xs.append(ax + (bx - ax) * (y - ay) // (by - ay))
        if len(xs) >= 2:
            for x in range(min(xs), max(xs) + 1):
                px(x, y, color)


def text(x, y, s, scale, color):
    cx = x
    for ch in s:
        glyph = FONT.get(ch, FONT["?"])
        for r in range(7):
            row = glyph[r]
            for c in range(5):
                if row[c] == "1":
                    rect(cx + c * scale, y + r * scale, scale, scale, color)
        cx += 6 * scale
    return cx


def text_w(s, scale):
    return len(s) * 6 * scale


def chunk(name, data):
    out = struct.pack(">I", len(data)) + name + data
    out += struct.pack(">I", zlib.crc32(name + data) & 0xFFFFFFFF)
    return out


def write_png(path):
    raw = bytearray()
    for y in range(H):
        raw.append(0)
        raw += BUF[y * W * 3:(y + 1) * W * 3]
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 6))
    png += chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


def icon_jet(x, y):
    circle(x + 55, y + 55, 52, SKY)
    tri(x + 82, y + 55, x + 52, y + 40, x + 52, y + 70, NAVY)
    rect(x + 16, y + 48, 42, 14, NAVY)
    tri(x + 28, y + 48, x + 48, y + 24, x + 48, y + 48, NAVY)
    tri(x + 28, y + 62, x + 48, y + 86, x + 48, y + 62, NAVY)
    rect(x + 12, y + 50, 10, 10, RED)


def icon_chess(x, y):
    rect(x + 6, y + 6, 100, 100, NAVY)
    for r in range(4):
        for c in range(4):
            if (r + c) % 2 == 0:
                rect(x + 8 + c * 24, y + 8 + r * 24, 24, 24, INK)
            else:
                rect(x + 8 + c * 24, y + 8 + r * 24, 24, 24, WHITE)
    circle(x + 56, y + 42, 16, GOLD)
    rect(x + 48, y + 20, 16, 14, GOLD)
    rect(x + 40, y + 58, 32, 8, GOLD)
    rect(x + 34, y + 68, 44, 8, GOLD)


def icon_train(x, y):
    rect(x + 12, y + 30, 86, 46, TEAL)
    rect(x + 22, y + 40, 20, 16, WHITE)
    rect(x + 50, y + 40, 20, 16, WHITE)
    rect(x + 12, y + 76, 86, 8, INK)
    circle(x + 30, y + 88, 10, INK)
    circle(x + 80, y + 88, 10, INK)
    line(x + 6, y + 100, x + 104, y + 100, GOLD, 4)
    tri(x + 98, y + 30, x + 98, y + 76, x + 78, y + 53, TEAL)


def icon_chip(x, y):
    rect(x + 30, y + 30, 50, 50, INK)
    rect(x + 42, y + 42, 26, 26, GOLD)
    for i in range(4):
        rect(x + 18, y + 38 + i * 12, 12, 5, GREY)
        rect(x + 80, y + 38 + i * 12, 12, 5, GREY)
        rect(x + 38 + i * 12, y + 18, 5, 12, GREY)
        rect(x + 38 + i * 12, y + 80, 5, 12, GREY)


def icon_sun(x, y):
    line(x + 55, y + 4, x + 55, y + 12, ORANGE, 4)
    line(x + 22, y + 14, x + 30, y + 20, ORANGE, 4)
    line(x + 88, y + 14, x + 80, y + 20, ORANGE, 4)
    circle(x + 55, y + 45, 30, ORANGE)
    rect(x + 14, y + 82, 82, 6, (40, 120, 190))
    rect(x + 22, y + 94, 66, 6, (40, 120, 190))


def panel(y, bar, title, line1, line2, icon):
    rect(20, y, 984, 150, WHITE)
    rect(20, y, 14, 150, bar)
    rect(20, y, 984, 4, bar)
    rect(20, y + 146, 984, 4, (210, 204, 188))
    text(52, y + 16, title, 4, NAVY)
    text(52, y + 62, line1, 3, INK)
    text(52, y + 96, line2, 3, GREY)
    icon(872, y + 20)


def main():
    rect(0, 0, W, H, CREAM)
    rect(0, 0, W, 158, NAVY)
    rect(0, 154, W, 4, GOLD)
    text(32, 18, "TUESDAY - THE WORLD IN ONE PICTURE", 3, GOLD)
    text(32, 52, "24 NOVEMBER 2026", 8, WHITE)
    text(32, 122, "FIVE STORIES FROM FIVE REGIONS", 3, (200, 214, 230))
    panel(172, RED, "KOREA SCRAMBLES JETS", "RUSSIAN PLANES ENTER AIR DEFENCE ZONE", "NEAR ULLEUNG ISLAND. JETS UP. ALERT LIFTED.", icon_jet)
    panel(332, NAVY2, "CHESS CROWN GAME 1", "GUKESH DEFENDS TITLE V SINDAROV IN GENEVA", "GAME 1 TODAY. BOTH 20. YOUNGEST FINAL EVER.", icon_chess)
    panel(492, GREEN, "NEW TRAIN LINKS INDIA AND NEPAL", "MODI AND NEPAL PM FLAG OFF SARYU-KAMALA", "EXPRESS. AYODHYA TO JANAKPUR DHAM.", icon_train)
    panel(652, TEAL, "US BLACKLISTS ALIBABA UNIT", "SINGAPORE UNIT APEX ACCUSED OVER CHIP", "DIVERSION. ALIBABA DENIES WRONGDOING.", icon_chip)
    panel(812, ORANGE, "FIJI SHUTS SCHOOLS IN DROUGHT", "ALL SCHOOLS SHUT FOR FIVE DAYS FROM NOV 30", "AS EL NINO DROUGHT DEEPENS IN PACIFIC.", icon_sun)
    rect(0, 976, W, 48, NAVY)
    text(32, 990, "ALSO TODAY: BRAZIL LOWER HOUSE BACKS LULA FISCAL PLAN", 3, WHITE)
    out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    write_png(out)


if __name__ == "__main__":
    main()
