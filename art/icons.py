"""Flat pictograms drawn with Pillow shapes, one per story.

Every function takes (d, x0, y0, x1, y1, k) where d is an ImageDraw on the
2x canvas, the box is in canvas pixels and k is the canvas scale. Drawings
hold no words: at most one big number or place name is stamped on by the
layout code, never here.
"""
import math

NAVY = (24, 33, 58)
NIGHT = (30, 40, 72)
SKY = (196, 222, 238)
SAND = (236, 222, 190)
GRASS = (122, 170, 92)
RED = (190, 40, 40)
ORANGE = (236, 132, 40)
YELLOW = (246, 202, 70)
WHITE = (250, 250, 246)
GREY = (120, 126, 138)
DARK = (40, 40, 46)
BLUE = (52, 104, 170)
SEA = (70, 128, 176)
GREEN = (46, 120, 80)
BROWN = (120, 82, 50)
PURPLE = (110, 80, 150)


def _bg(d, x0, y0, x1, y1, col):
    d.rectangle([x0, y0, x1, y1], fill=col)


def _rel(x0, y0, x1, y1):
    w, h = x1 - x0, y1 - y0
    return lambda fx, fy: (x0 + fx * w, y0 + fy * h)


def city(d, x0, y0, x1, y1, k, col=(20, 26, 46), lit=YELLOW):
    p = _rel(x0, y0, x1, y1)
    blocks = [(0.02, 0.62, 0.12), (0.14, 0.48, 0.24), (0.26, 0.70, 0.34),
              (0.36, 0.55, 0.48), (0.50, 0.66, 0.58), (0.60, 0.44, 0.70),
              (0.72, 0.60, 0.82), (0.84, 0.52, 0.97)]
    for bx0, by, bx1 in blocks:
        a, b = p(bx0, by), p(bx1, 1)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=col)
        wy = a[1] + 6 * k
        while wy < b[1] - 8 * k:
            wx = a[0] + 4 * k
            while wx < b[0] - 6 * k:
                if (int(wx) // 3 + int(wy) // 5) % 3:
                    d.rectangle([wx, wy, wx + 3 * k, wy + 3 * k], fill=lit)
                wx += 8 * k
            wy += 9 * k


def drones(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, NIGHT)
    p = _rel(x0, y0, x1, y1)
    for i in range(9):
        fx = 0.08 + (i * 0.37) % 0.9
        fy = 0.12 + ((i * 0.23) % 0.38)
        cx, cy = p(fx, fy)
        s = 7 * k
        d.polygon([(cx - s, cy), (cx + s, cy - s * 0.35), (cx + s * 0.4, cy), (cx + s, cy + s * 0.35)], fill=WHITE)
        d.line([cx + s, cy, cx + s * 3, cy - s * 0.5], fill=(255, 170, 80), width=int(2 * k))
    city(d, x0, y0, x1, y1, k)
    fx, fy = p(0.33, 0.66)
    d.ellipse([fx - 16 * k, fy - 16 * k, fx + 16 * k, fy + 16 * k], fill=ORANGE)
    d.ellipse([fx - 8 * k, fy - 8 * k, fx + 8 * k, fy + 8 * k], fill=YELLOW)


def summit(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, SKY)
    p = _rel(x0, y0, x1, y1)
    gx, gy = p(0.5, 0.36)
    r = (y1 - y0) * 0.26
    d.ellipse([gx - r, gy - r, gx + r, gy + r], fill=SEA)
    d.polygon([(gx - r * 0.6, gy - r * 0.5), (gx - r * 0.1, gy - r * 0.7), (gx + r * 0.1, gy - r * 0.1),
               (gx - r * 0.3, gy + r * 0.3), (gx - r * 0.7, gy)], fill=GRASS)
    d.polygon([(gx + r * 0.3, gy + r * 0.1), (gx + r * 0.8, gy - r * 0.2), (gx + r * 0.7, gy + r * 0.5),
               (gx + r * 0.4, gy + r * 0.7)], fill=GRASS)
    a, b = p(0.06, 0.70), p(0.94, 0.80)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=BROWN)
    for i in range(7):
        hx, hy = p(0.12 + i * 0.127, 0.70)
        d.ellipse([hx - 9 * k, hy - 26 * k, hx + 9 * k, hy - 8 * k], fill=DARK)
        d.rectangle([hx - 11 * k, hy - 8 * k, hx + 11 * k, hy], fill=DARK)
    a, b = p(0, 0.80), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(210, 196, 168))


def radar(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (238, 214, 170))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.78), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(200, 170, 120))
    cx, cy = p(0.36, 0.52)
    r = (y1 - y0) * 0.30
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 200, 380, fill=GREY)
    d.line([cx, cy, cx, cy + r * 0.9], fill=DARK, width=int(5 * k))
    d.line([cx - r * 0.5, cy + r * 0.9, cx + r * 0.5, cy + r * 0.9], fill=DARK, width=int(6 * k))
    for i, fx in enumerate([0.66, 0.78, 0.9]):
        fx_, fy_ = p(fx, 0.78)
        hgt = (y1 - y0) * (0.34 + 0.08 * (i % 2))
        d.polygon([(fx_ - 14 * k, fy_), (fx_, fy_ - hgt), (fx_ + 14 * k, fy_)], fill=ORANGE)
        d.polygon([(fx_ - 7 * k, fy_), (fx_, fy_ - hgt * 0.55), (fx_ + 7 * k, fy_)], fill=YELLOW)
    qx, qy = p(0.62, 0.22)
    d.ellipse([qx - 20 * k, qy - 20 * k, qx + 20 * k, qy + 20 * k], outline=DARK, width=int(4 * k))


def ballot(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (226, 232, 240))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.30, 0.42), p(0.70, 0.96)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=BLUE)
    s1, s2 = p(0.40, 0.48), p(0.60, 0.53)
    d.rectangle([s1[0], s1[1], s2[0], s2[1]], fill=NAVY)
    c, e = p(0.40, 0.08), p(0.60, 0.50)
    d.rectangle([c[0], c[1], e[0], e[1]], fill=WHITE, outline=DARK, width=int(2 * k))
    m1, m2, m3 = p(0.44, 0.28), p(0.49, 0.38), p(0.57, 0.16)
    d.line([m1, m2, m3], fill=RED, width=int(5 * k))


def cricket(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, GRASS)
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.25, 0.30), p(0.75, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(214, 196, 140))
    for fx in (0.46, 0.5, 0.54):
        t, u = p(fx, 0.42), p(fx, 0.82)
        d.line([t, u], fill=WHITE, width=int(5 * k))
    bx, by = p(0.70, 0.30)
    d.ellipse([bx - 9 * k, by - 9 * k, bx + 9 * k, by + 9 * k], fill=RED)


def racecar(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (34, 34, 44))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.72), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(70, 70, 80))
    for i in range(6):
        u, v = p(0.05 + i * 0.17, 0.85), p(0.13 + i * 0.17, 0.87)
        d.rectangle([u[0], u[1], v[0], v[1]], fill=WHITE)
    a, b = p(0.18, 0.50), p(0.82, 0.68)
    d.rounded_rectangle([a[0], a[1], b[0], b[1]], radius=8 * k, fill=RED)
    c, e = p(0.42, 0.40), p(0.58, 0.52)
    d.rounded_rectangle([c[0], c[1], e[0], e[1]], radius=6 * k, fill=DARK)
    w = p(0.75, 0.40)
    d.rectangle([w[0], w[1], w[0] + 10 * k, w[1] + 20 * k], fill=RED)
    for fx in (0.28, 0.72):
        cx, cy = p(fx, 0.68)
        d.ellipse([cx - 13 * k, cy - 13 * k, cx + 13 * k, cy + 13 * k], fill=(15, 15, 15))
    for i in range(4):
        u = p(0.86 + (i % 2) * 0.04, 0.12 + (i // 2) * 0.08)
        d.rectangle([u[0], u[1], u[0] + 10 * k, u[1] + 10 * k], fill=WHITE)


def ball(d, x0, y0, x1, y1, k, sport="football"):
    _bg(d, x0, y0, x1, y1, GRASS if sport == "football" else (210, 160, 110))
    p = _rel(x0, y0, x1, y1)
    cx, cy = p(0.5, 0.52)
    r = (y1 - y0) * 0.30
    if sport == "football":
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE, outline=DARK, width=int(2 * k))
        pts = [(cx + r * 0.38 * math.cos(math.radians(a - 90)), cy + r * 0.38 * math.sin(math.radians(a - 90))) for a in range(0, 360, 72)]
        d.polygon(pts, fill=DARK)
        a, b = p(0.02, 0.2), p(0.18, 0.9)
        d.rectangle([a[0], a[1], b[0], b[1]], outline=WHITE, width=int(4 * k))
    elif sport == "tennis":
        d.rectangle([x0, y0, x1, y1], fill=(46, 92, 150))
        a, b = p(0.08, 0.12), p(0.92, 0.95)
        d.rectangle([a[0], a[1], b[0], b[1]], outline=WHITE, width=int(3 * k))
        m1, m2 = p(0.5, 0.12), p(0.5, 0.95)
        d.line([m1, m2], fill=WHITE, width=int(4 * k))
        bx, by = p(0.28, 0.45)
        rb = (y1 - y0) * 0.20
        d.ellipse([bx - rb, by - rb, bx + rb, by + rb], fill=(214, 230, 50), outline=DARK, width=int(2 * k))
        d.arc([bx - rb * 1.9, by - rb, bx + rb * 0.1, by + rb], -50, 50, fill=WHITE, width=int(3 * k))
    elif sport == "rugby":
        d.ellipse([cx - r * 1.4, cy - r * 0.8, cx + r * 1.4, cy + r * 0.8], fill=BROWN)
        d.line([cx - r * 0.6, cy, cx + r * 0.6, cy], fill=WHITE, width=int(3 * k))
    else:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ORANGE, outline=DARK, width=int(3 * k))
        d.line([cx - r, cy, cx + r, cy], fill=DARK, width=int(3 * k))
        d.line([cx, cy - r, cx, cy + r], fill=DARK, width=int(3 * k))


def ship(d, x0, y0, x1, y1, k, fire=True):
    _bg(d, x0, y0, x1, y1, (130, 150, 170) if fire else SKY)
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.66), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=SEA)
    d.polygon([p(0.14, 0.58), p(0.86, 0.58), p(0.78, 0.78), p(0.22, 0.78)], fill=DARK)
    c, e = p(0.56, 0.40), p(0.74, 0.58)
    d.rectangle([c[0], c[1], e[0], e[1]], fill=WHITE)
    if fire:
        for fx in (0.30, 0.40):
            fx_, fy_ = p(fx, 0.58)
            hgt = (y1 - y0) * 0.36
            d.polygon([(fx_ - 14 * k, fy_), (fx_, fy_ - hgt), (fx_ + 14 * k, fy_)], fill=ORANGE)
            d.polygon([(fx_ - 7 * k, fy_), (fx_, fy_ - hgt * 0.5), (fx_ + 7 * k, fy_)], fill=YELLOW)
        sx, sy = p(0.36, 0.12)
        d.ellipse([sx - 26 * k, sy - 12 * k, sx + 26 * k, sy + 12 * k], fill=(90, 90, 96))


def power(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, NIGHT)
    p = _rel(x0, y0, x1, y1)
    for fx in (0.22, 0.62):
        t, l, r_ = p(fx, 0.15), p(fx - 0.09, 0.98), p(fx + 0.09, 0.98)
        d.line([l, t, r_], fill=GREY, width=int(4 * k))
        a, b = p(fx - 0.1, 0.32), p(fx + 0.1, 0.32)
        d.line([a, b], fill=GREY, width=int(4 * k))
    d.line([p(0.32, 0.32), p(0.52, 0.32)], fill=GREY, width=int(2 * k))
    d.polygon([p(0.84, 0.10), p(0.74, 0.52), p(0.82, 0.52), p(0.76, 0.92), p(0.94, 0.42), p(0.85, 0.42), p(0.92, 0.10)], fill=YELLOW)


def hospital(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (226, 236, 240))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.10, 0.56), p(0.70, 0.68)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=WHITE, outline=GREY, width=int(2 * k))
    c, e = p(0.10, 0.68), p(0.70, 0.74)
    d.rectangle([c[0], c[1], e[0], e[1]], fill=GREY)
    hx, hy = p(0.18, 0.50)
    d.ellipse([hx - 10 * k, hy - 10 * k, hx + 10 * k, hy + 10 * k], fill=(230, 200, 170))
    cx, cy = p(0.84, 0.40)
    s = (y1 - y0) * 0.22
    d.ellipse([cx - s, cy - s, cx + s, cy + s], fill=WHITE, outline=RED, width=int(3 * k))
    d.rectangle([cx - s * 0.22, cy - s * 0.65, cx + s * 0.22, cy + s * 0.65], fill=RED)
    d.rectangle([cx - s * 0.65, cy - s * 0.22, cx + s * 0.65, cy + s * 0.22], fill=RED)


def magnifier(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (222, 226, 236))
    p = _rel(x0, y0, x1, y1)
    for i in range(4):
        a, b = p(0.08, 0.18 + i * 0.18), p(0.55, 0.26 + i * 0.18)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=GREY if i % 2 else BLUE)
    cx, cy = p(0.70, 0.42)
    r = (y1 - y0) * 0.26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=DARK, width=int(6 * k))
    d.line([cx + r * 0.7, cy + r * 0.7, cx + r * 1.5, cy + r * 1.5], fill=DARK, width=int(9 * k))


def plane(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, SKY)
    p = _rel(x0, y0, x1, y1)
    cx, cy = p(0.5, 0.5)
    L = (x1 - x0) * 0.30
    d.polygon([(cx - L, cy - 4 * k), (cx + L, cy - 6 * k), (cx + L + 12 * k, cy), (cx + L, cy + 6 * k), (cx - L, cy + 4 * k)], fill=WHITE, outline=GREY)
    d.polygon([(cx - 6 * k, cy), (cx + 16 * k, cy), (cx - 14 * k, cy - L * 0.7), (cx - 26 * k, cy - L * 0.7)], fill=GREY)
    d.polygon([(cx - 6 * k, cy), (cx + 16 * k, cy), (cx - 14 * k, cy + L * 0.7), (cx - 26 * k, cy + L * 0.7)], fill=GREY)
    d.line([p(0.06, 0.12), p(0.94, 0.88)], fill=RED, width=int(7 * k))


def fire(d, x0, y0, x1, y1, k, bg=(60, 44, 40)):
    _bg(d, x0, y0, x1, y1, bg)
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.80), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(40, 30, 28))
    for i, fx in enumerate((0.25, 0.45, 0.65, 0.82)):
        fx_, fy_ = p(fx, 0.82)
        hgt = (y1 - y0) * (0.5 + 0.15 * (i % 2))
        d.polygon([(fx_ - 20 * k, fy_), (fx_ - 6 * k, fy_ - hgt * 0.7), (fx_, fy_ - hgt), (fx_ + 20 * k, fy_)], fill=ORANGE)
        d.polygon([(fx_ - 10 * k, fy_), (fx_, fy_ - hgt * 0.5), (fx_ + 10 * k, fy_)], fill=YELLOW)


def quake(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, SKY)
    p = _rel(x0, y0, x1, y1)
    d.polygon([p(0, 1), p(0.30, 0.30), p(0.55, 0.70), p(0.72, 0.40), p(1, 1)], fill=(140, 120, 100))
    d.line([p(0.45, 1.0), p(0.50, 0.85), p(0.44, 0.74), p(0.52, 0.62)], fill=DARK, width=int(5 * k))
    for i in range(3):
        r = (i + 1) * 12 * k
        cx, cy = p(0.82, 0.30)
        d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=RED, width=int(3 * k))


def flood(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (150, 160, 175))
    p = _rel(x0, y0, x1, y1)
    for fx in (0.15, 0.55):
        a, b = p(fx, 0.30), p(fx + 0.25, 0.75)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=(220, 210, 190))
        d.polygon([p(fx - 0.03, 0.32), p(fx + 0.125, 0.12), p(fx + 0.28, 0.32)], fill=RED)
    a, b = p(0, 0.62), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(92, 120, 150))
    for i in range(5):
        u = p(0.05 + i * 0.2, 0.66)
        d.arc([u[0], u[1], u[0] + 30 * k, u[1] + 12 * k], 180, 360, fill=WHITE, width=int(2 * k))
    for i in range(4):
        u = p(0.1 + i * 0.25, 0.0)
        d.line([u[0], u[1] + 4 * k, u[0] - 8 * k, u[1] + 30 * k], fill=(90, 110, 140), width=int(2 * k))


def gavel(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (236, 226, 206))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.15, 0.80), p(0.60, 0.92)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=BROWN)
    c = p(0.55, 0.36)
    d.line([c, p(0.85, 0.75)], fill=BROWN, width=int(9 * k))
    hx, hy = c
    pts = [(hx - 30 * k, hy - 4 * k), (hx - 6 * k, hy - 30 * k), (hx + 18 * k, hy - 6 * k), (hx - 6 * k, hy + 18 * k)]
    d.polygon(pts, fill=(90, 60, 36))
    for i in range(3):
        cx, cy = p(0.82, 0.12 + i * 0.1)
        d.rectangle([cx, cy, cx + 30 * k, cy + 4 * k], fill=GREY)


def rocket(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, NIGHT)
    p = _rel(x0, y0, x1, y1)
    for i in range(14):
        sx, sy = p(((i * 0.37) % 1), ((i * 0.53) % 1) * 0.6)
        d.ellipse([sx - 1.5 * k, sy - 1.5 * k, sx + 1.5 * k, sy + 1.5 * k], fill=WHITE)
    cx, cy = p(0.5, 0.40)
    h = (y1 - y0) * 0.55
    w = 13 * k
    d.polygon([(cx, cy - h * 0.5), (cx + w, cy - h * 0.25), (cx + w, cy + h * 0.4), (cx - w, cy + h * 0.4), (cx - w, cy - h * 0.25)], fill=WHITE)
    d.polygon([(cx - w, cy + h * 0.15), (cx - w * 2, cy + h * 0.45), (cx - w, cy + h * 0.4)], fill=RED)
    d.polygon([(cx + w, cy + h * 0.15), (cx + w * 2, cy + h * 0.45), (cx + w, cy + h * 0.4)], fill=RED)
    d.polygon([(cx - w * 0.7, cy + h * 0.4), (cx, cy + h * 0.95), (cx + w * 0.7, cy + h * 0.4)], fill=ORANGE)


def coin(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (232, 236, 226))
    p = _rel(x0, y0, x1, y1)
    pts = [p(0.04, 0.25), p(0.2, 0.32), p(0.34, 0.30), p(0.48, 0.55), p(0.62, 0.62), p(0.78, 0.80), p(0.96, 0.86)]
    d.line(pts, fill=RED, width=int(5 * k))
    cx, cy = p(0.80, 0.34)
    r = (y1 - y0) * 0.24
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=YELLOW, outline=ORANGE, width=int(4 * k))
    d.ellipse([cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6], outline=ORANGE, width=int(3 * k))


def chart(d, x0, y0, x1, y1, k, up=True):
    _bg(d, x0, y0, x1, y1, (232, 236, 226))
    p = _rel(x0, y0, x1, y1)
    vals = [0.7, 0.6, 0.66, 0.5, 0.45, 0.3, 0.25] if up else [0.25, 0.35, 0.3, 0.5, 0.55, 0.7, 0.8]
    for i, v in enumerate(vals):
        a, b = p(0.06 + i * 0.13, v), p(0.14 + i * 0.13, 0.95)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=GREEN if up else RED)


def crowd(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (226, 220, 210))
    p = _rel(x0, y0, x1, y1)
    for row in range(2):
        for i in range(9):
            hx, hy = p(0.06 + i * 0.11 + row * 0.05, 0.62 + row * 0.18)
            col = [DARK, BROWN, NAVY, GREY][(i + row) % 4]
            d.ellipse([hx - 9 * k, hy - 24 * k, hx + 9 * k, hy - 6 * k], fill=col)
            d.rectangle([hx - 12 * k, hy - 6 * k, hx + 12 * k, hy + 30 * k], fill=col)
    a = p(0.30, 0.08)
    d.rectangle([a[0], a[1], a[0] + 70 * k, a[1] + 36 * k], fill=WHITE, outline=DARK, width=int(2 * k))
    d.line([a[0] + 35 * k, a[1] + 36 * k, a[0] + 35 * k, a[1] + 80 * k], fill=DARK, width=int(3 * k))


def virus(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (230, 238, 232))
    p = _rel(x0, y0, x1, y1)
    for fx, fy, rr in ((0.35, 0.5, 0.3), (0.75, 0.35, 0.16)):
        cx, cy = p(fx, fy)
        r = (y1 - y0) * rr
        for a in range(0, 360, 40):
            ex = cx + r * 1.35 * math.cos(math.radians(a))
            ey = cy + r * 1.35 * math.sin(math.radians(a))
            d.line([cx, cy, ex, ey], fill=GREEN, width=int(3 * k))
            d.ellipse([ex - 4 * k, ey - 4 * k, ex + 4 * k, ey + 4 * k], fill=GREEN)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 160, 110))


def handshake(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (222, 230, 240))
    p = _rel(x0, y0, x1, y1)
    d.polygon([p(0.0, 0.40), p(0.42, 0.40), p(0.55, 0.55), p(0.42, 0.66), p(0.0, 0.66)], fill=NAVY)
    d.polygon([p(1.0, 0.40), p(0.58, 0.40), p(0.45, 0.55), p(0.58, 0.66), p(1.0, 0.66)], fill=BROWN)
    cx, cy = p(0.5, 0.53)
    d.ellipse([cx - 18 * k, cy - 14 * k, cx + 18 * k, cy + 14 * k], fill=(232, 190, 150))
    for fx, col in ((0.12, BLUE), (0.88, RED)):
        a = p(fx, 0.08)
        d.line([a[0], a[1], a[0], a[1] + 50 * k], fill=DARK, width=int(3 * k))
        d.rectangle([a[0], a[1], a[0] + 34 * k, a[1] + 22 * k], fill=col)


def missile(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (200, 184, 160))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.80), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(150, 130, 100))
    d.line([p(0.05, 0.85), p(0.35, 0.25), p(0.65, 0.20), p(0.85, 0.55)], fill=WHITE, width=int(4 * k))
    cx, cy = p(0.85, 0.72)
    d.ellipse([cx - 26 * k, cy - 18 * k, cx + 26 * k, cy + 18 * k], fill=ORANGE)
    d.ellipse([cx - 12 * k, cy - 9 * k, cx + 12 * k, cy + 9 * k], fill=YELLOW)


def ruins(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (190, 176, 160))
    p = _rel(x0, y0, x1, y1)
    d.polygon([p(0.05, 1), p(0.05, 0.40), p(0.20, 0.30), p(0.28, 0.55), p(0.32, 1)], fill=(110, 100, 92))
    d.polygon([p(0.40, 1), p(0.42, 0.22), p(0.60, 0.22), p(0.62, 0.48), p(0.56, 0.60), p(0.66, 1)], fill=(130, 118, 106))
    d.polygon([p(0.72, 1), p(0.74, 0.50), p(0.90, 0.42), p(0.95, 1)], fill=(100, 92, 84))
    sx, sy = p(0.52, 0.10)
    d.ellipse([sx - 40 * k, sy - 14 * k, sx + 40 * k, sy + 14 * k], fill=(120, 120, 124))


def trophy(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (40, 60, 100))
    p = _rel(x0, y0, x1, y1)
    cx, cy = p(0.5, 0.36)
    r = (y1 - y0) * 0.26
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 0, 180, fill=YELLOW)
    d.rectangle([cx - r, cy - r * 0.6, cx + r, cy], fill=YELLOW)
    d.arc([cx - r * 1.5, cy - r * 0.6, cx - r * 0.4, cy + r * 0.4], 90, 270, fill=YELLOW, width=int(4 * k))
    d.arc([cx + r * 0.4, cy - r * 0.6, cx + r * 1.5, cy + r * 0.4], 270, 90, fill=YELLOW, width=int(4 * k))
    d.rectangle([cx - 5 * k, cy + r, cx + 5 * k, cy + r * 1.6], fill=YELLOW)
    d.rectangle([cx - r * 0.6, cy + r * 1.6, cx + r * 0.6, cy + r * 1.9], fill=YELLOW)


def tree(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, SKY)
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.82), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=GRASS)
    for fx in (0.2, 0.5, 0.8):
        tx, ty = p(fx, 0.82)
        d.rectangle([tx - 5 * k, ty - 30 * k, tx + 5 * k, ty], fill=BROWN)
        d.ellipse([tx - 26 * k, ty - 80 * k, tx + 26 * k, ty - 24 * k], fill=GREEN)
    sx, sy = p(0.9, 0.16)
    d.ellipse([sx - 16 * k, sy - 16 * k, sx + 16 * k, sy + 16 * k], fill=YELLOW)


def portrait(d, x0, y0, x1, y1, k, bg=(214, 206, 196)):
    _bg(d, x0, y0, x1, y1, bg)
    p = _rel(x0, y0, x1, y1)
    cx, cy = p(0.5, 0.40)
    r = (y1 - y0) * 0.20
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 110, 104))
    d.pieslice([cx - r * 2.0, cy + r * 1.1, cx + r * 2.0, cy + r * 4.4], 180, 360, fill=(80, 74, 70))
    a = p(0.86, 0.12)
    d.rectangle([a[0] - 20 * k, a[1], a[0] + 20 * k, a[1] + 8 * k], fill=DARK)


def chip(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (226, 230, 240))
    p = _rel(x0, y0, x1, y1)
    cx, cy = p(0.5, 0.5)
    s = (y1 - y0) * 0.28
    for i in range(5):
        o = -s + i * s * 0.5
        d.line([cx + o, cy - s * 1.5, cx + o, cy + s * 1.5], fill=GREY, width=int(3 * k))
        d.line([cx - s * 1.5, cy + o, cx + s * 1.5, cy + o], fill=GREY, width=int(3 * k))
    d.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=6 * k, fill=NAVY)
    d.rectangle([cx - s * 0.5, cy - s * 0.5, cx + s * 0.5, cy + s * 0.5], fill=BLUE)


def tank(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (200, 190, 170))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.82), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(150, 130, 100))
    a, b = p(0.18, 0.60), p(0.78, 0.82)
    d.rounded_rectangle([a[0], a[1], b[0], b[1]], radius=10 * k, fill=(84, 94, 70))
    c, e = p(0.34, 0.44), p(0.60, 0.62)
    d.rounded_rectangle([c[0], c[1], e[0], e[1]], radius=8 * k, fill=(96, 108, 80))
    d.line([p(0.58, 0.50), p(0.94, 0.46)], fill=(70, 80, 60), width=int(7 * k))


def hemicycle(d, x0, y0, x1, y1, k, dem=258, rep=173, open_=4):
    """House seats as a half-circle of dots: blue Democrats, red Republicans, grey undecided."""
    _bg(d, x0, y0, x1, y1, (236, 240, 246))
    cx, cy = (x0 + x1) / 2, y1 - (y1 - y0) * 0.10
    R = min((x1 - x0) * 0.46, (y1 - y0) * 0.82)
    rows = 9
    total = dem + rep + open_
    radii = [R * (0.42 + 0.58 * r / (rows - 1)) for r in range(rows)]
    weights = sum(radii)
    seats = []
    left = total
    for j, r in enumerate(radii):
        n = round(total * r / weights) if j < rows - 1 else left
        left -= n
        for m in range(n):
            a = math.pi * (1 - (m + 0.5) / n)
            seats.append((a, cx + r * math.cos(a), cy - r * math.sin(a)))
    seats.sort(key=lambda t: -t[0])
    dot = R * 0.045
    for idx, (_, sx, sy) in enumerate(seats):
        col = BLUE if idx < dem else ((150, 150, 156) if idx < dem + open_ else RED)
        d.ellipse([sx - dot, sy - dot, sx + dot, sy + dot], fill=col)


def capsized(d, x0, y0, x1, y1, k):
    _bg(d, x0, y0, x1, y1, (176, 196, 214))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.62, 0.20), p(0.98, 0.58)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(206, 200, 188))
    for fx in (0.68, 0.78, 0.88):
        u, v = p(fx, 0.30), p(fx + 0.05, 0.40)
        d.rectangle([u[0], u[1], v[0], v[1]], fill=(150, 146, 138))
    d.polygon([p(0.10, 0.62), p(0.30, 0.22), p(0.40, 0.30), p(0.30, 0.62)], fill=(80, 84, 92))
    d.polygon([p(0.30, 0.22), p(0.40, 0.30), p(0.37, 0.40), p(0.27, 0.32)], fill=(150, 40, 40))
    a, b = p(0, 0.58), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=SEA)
    for j in range(4):
        u = p(0.05 + j * 0.24, 0.66)
        d.arc([u[0], u[1], u[0] + 34 * k, u[1] + 12 * k], 180, 360, fill=WHITE, width=int(2 * k))


def launch(d, x0, y0, x1, y1, k):
    """Rocket lifting off its pad beside a tower, with an exhaust plume."""
    _bg(d, x0, y0, x1, y1, (40, 56, 96))
    p = _rel(x0, y0, x1, y1)
    for j in range(10):
        sx, sy = p(((j * 0.41) % 1), ((j * 0.29) % 1) * 0.4)
        d.ellipse([sx - 1.5 * k, sy - 1.5 * k, sx + 1.5 * k, sy + 1.5 * k], fill=WHITE)
    a, b = p(0.12, 0.12), p(0.18, 0.92)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(120, 120, 128))
    for j in range(6):
        u, v = p(0.12, 0.18 + j * 0.12), p(0.18, 0.24 + j * 0.12)
        d.line([u, v], fill=(80, 80, 88), width=int(2 * k))
    cx = p(0.36, 0)[0]
    top, bot = p(0, 0.06)[1], p(0, 0.60)[1]
    w = 9 * k
    d.rectangle([cx - w, top + 12 * k, cx + w, bot], fill=WHITE)
    d.polygon([(cx - w, top + 12 * k), (cx, top), (cx + w, top + 12 * k)], fill=WHITE)
    d.rectangle([cx - w, top + 30 * k, cx + w, top + 34 * k], fill=(30, 30, 30))
    d.polygon([(cx - w * 0.8, bot), (cx, bot + (y1 - y0) * 0.22), (cx + w * 0.8, bot)], fill=ORANGE)
    d.polygon([(cx - w * 0.4, bot), (cx, bot + (y1 - y0) * 0.12), (cx + w * 0.4, bot)], fill=YELLOW)
    for j, fx in enumerate((0.20, 0.29, 0.38, 0.47, 0.56)):
        u = p(fx, 0.90)
        r = (16 + 6 * (j % 2)) * k
        d.ellipse([u[0] - r, u[1] - r * 0.7, u[0] + r, u[1] + r * 0.7], fill=(226, 226, 230))
    a, b = p(0, 0.94), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(60, 60, 66))


def tent(d, x0, y0, x1, y1, k):
    """Field hospital tent with a red cross, under a grey sky."""
    _bg(d, x0, y0, x1, y1, (210, 216, 222))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0, 0.80), p(1, 1)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(150, 120, 90))
    d.polygon([p(0.10, 0.84), p(0.30, 0.22), p(0.62, 0.22), p(0.82, 0.84)], fill=WHITE, outline=GREY)
    d.polygon([p(0.38, 0.84), p(0.46, 0.50), p(0.54, 0.84)], fill=(70, 70, 76))
    cx, cy = p(0.46, 0.36)
    s = (y1 - y0) * 0.09
    d.rectangle([cx - s * 0.35, cy - s, cx + s * 0.35, cy + s], fill=RED)
    d.rectangle([cx - s, cy - s * 0.35, cx + s, cy + s * 0.35], fill=RED)
    vx, vy = p(0.88, 0.30)
    r = (y1 - y0) * 0.11
    for a_ in range(0, 360, 45):
        ex, ey = vx + r * 1.5 * math.cos(math.radians(a_)), vy + r * 1.5 * math.sin(math.radians(a_))
        d.line([vx, vy, ex, ey], fill=GREEN, width=int(2 * k))
    d.ellipse([vx - r, vy - r, vx + r, vy + r], fill=(90, 160, 110))


def tv(d, x0, y0, x1, y1, k):
    """A TV interview: a screen showing a speaker before a US flag."""
    _bg(d, x0, y0, x1, y1, (226, 222, 214))
    p = _rel(x0, y0, x1, y1)
    a, b = p(0.18, 0.08), p(0.82, 0.86)
    d.rounded_rectangle([a[0], a[1], b[0], b[1]], radius=6 * k, fill=(30, 30, 34))
    a, b = p(0.22, 0.14), p(0.78, 0.78)
    d.rectangle([a[0], a[1], b[0], b[1]], fill=(32, 60, 120))
    for j in range(5):
        u, v = p(0.50, 0.18 + j * 0.10), p(0.76, 0.23 + j * 0.10)
        d.rectangle([u[0], u[1], v[0], v[1]], fill=RED if j % 2 == 0 else WHITE)
    u, v = p(0.24, 0.16), p(0.48, 0.40)
    d.rectangle([u[0], u[1], v[0], v[1]], fill=(40, 70, 140))
    hx, hy = p(0.40, 0.42)
    r = (y1 - y0) * 0.11
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(222, 180, 140))
    d.pieslice([hx - r * 2.2, hy + r * 0.8, hx + r * 2.2, hy + r * 4.6], 180, 360, fill=(30, 36, 60))
    d.rectangle([p(0.46, 0.86)[0], p(0, 0.86)[1], p(0.54, 0)[0], p(0, 0.94)[1]], fill=(30, 30, 34))


ICONS = {
    "drones": drones, "summit": summit, "radar": radar, "ballot": ballot,
    "cricket": cricket, "racecar": racecar, "ship": ship, "power": power,
    "hospital": hospital, "magnifier": magnifier, "plane": plane, "fire": fire,
    "quake": quake, "flood": flood, "gavel": gavel, "rocket": rocket,
    "coin": coin, "chart": chart, "crowd": crowd, "virus": virus,
    "handshake": handshake, "missile": missile, "ruins": ruins, "trophy": trophy,
    "tree": tree, "portrait": portrait, "chip": chip, "tank": tank,
    "football": lambda d, *a: ball(d, *a, sport="football"),
    "tennis": lambda d, *a: ball(d, *a, sport="tennis"),
    "rugby": lambda d, *a: ball(d, *a, sport="rugby"),
    "basketball": lambda d, *a: ball(d, *a, sport="basketball"),
    "boat": lambda d, *a: ship(d, *a, fire=False),
    "launch": launch, "tent": tent, "tv": tv,
    "hemicycle": hemicycle, "capsized": capsized,
    "chart_down": lambda d, *a: chart(d, *a, up=False),
}
