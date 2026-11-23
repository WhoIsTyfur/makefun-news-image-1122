"""Draws the front page for Sunday 22 November 2026 into art/entry.png.

Run locally (Pillow + Windows fonts): python art/draw.py [content_module] [out.png]
The repo's main.py only copies the committed PNG, so the grader needs neither.
"""
import importlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icons import ICONS  # noqa: E402

K = 2                      # supersampling factor
W = H = 1024
FONTDIR = "C:/Windows/Fonts/"

PAPER = (250, 247, 240)
INK = (20, 20, 24)
INK2 = (60, 60, 66)
RULE = (150, 144, 132)
ACCENT = (150, 24, 24)
TAGCOL = {"CONFIRMED": (22, 100, 56), "OFFICIAL": (30, 70, 140), "REPORTED": (120, 76, 10), "CLAIM": (150, 24, 24)}
REGCOL = {"Europe": (40, 80, 150), "Middle East": (160, 40, 40), "Africa": (190, 110, 20),
          "Asia": (30, 120, 90), "Americas": (110, 60, 150), "Oceania": (20, 120, 150), "World": (90, 90, 96)}

_fonts = {}


def F(name, size):
    key = (name, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONTDIR + name, int(size * K))
    return _fonts[key]


SERIF_B = "georgiab.ttf"
SERIF_I = "georgiai.ttf"
SERIF = "georgia.ttf"
SANS = "segoeui.ttf"
SANS_B = "segoeuib.ttf"
SANS_SB = "seguisb.ttf" if os.path.exists(FONTDIR + "seguisb.ttf") else "segoeuib.ttf"


class Page:
    def __init__(self):
        self.im = Image.new("RGB", (W * K, H * K), PAPER)
        self.d = ImageDraw.Draw(self.im)

    # all coordinates in 1024-space
    def text(self, x, y, s, font, fill=INK, anchor="la"):
        self.d.text((x * K, y * K), s, font=font, fill=fill, anchor=anchor)

    def tw(self, s, font):
        return self.d.textlength(s, font=font) / K

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1):
        self.d.rectangle([x0 * K, y0 * K, x1 * K, y1 * K], fill=fill, outline=outline,
                         width=int(width * K) if outline else 0)

    def hline(self, x0, x1, y, fill=RULE, width=1):
        self.d.line([x0 * K, y * K, x1 * K, y * K], fill=fill, width=max(1, int(width * K)))

    def vline(self, x, y0, y1, fill=RULE, width=1):
        self.d.line([x * K, y0 * K, x * K, y1 * K], fill=fill, width=max(1, int(width * K)))

    def wrap(self, s, font, width):
        words, lines, cur = s.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.tw(t, font) <= width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w_
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, s, font, width, lh, fill=INK, maxlines=99):
        lines = self.wrap(s, font, width)
        if len(lines) > maxlines:
            raise ValueError("too long (%d lines > %d): %s" % (len(lines), maxlines, s))
        for i, ln in enumerate(lines):
            self.text(x, y + i * lh, ln, font, fill)
        return y + len(lines) * lh

    def fit(self, s, name, size, width, minsize):
        while size > minsize and self.tw(s, F(name, size)) > width:
            size -= 0.5
        if self.tw(s, F(name, size)) > width:
            raise ValueError("does not fit: " + s)
        return F(name, size)

    def icon(self, kind, x0, y0, x1, y1):
        w, h = int(round((x1 - x0) * K)), int(round((y1 - y0) * K))
        sub = Image.new("RGB", (w, h), PAPER)
        ICONS[kind](ImageDraw.Draw(sub), 0, 0, w - 1, h - 1, K)
        self.im.paste(sub, (int(round(x0 * K)), int(round(y0 * K))))

    def badge(self, s, x1, y0, size=20):
        f = F(SANS_B, size)
        w = self.tw(s, f) + 12
        self.rect(x1 - w - 4, y0 + 4, x1 - 4, y0 + 4 + size + 10, fill=(255, 255, 255), outline=INK, width=1)
        self.text(x1 - 4 - w / 2, y0 + 4 + (size + 10) / 2, s, f, INK, anchor="mm")

    def stamp(self, s, x0, y1, size=21):
        f = F(SANS_B, size)
        w = self.tw(s, f) + 12
        h = size + 9
        self.rect(x0 + 4, y1 - h - 4, x0 + 4 + w, y1 - 4, fill=(255, 255, 255), outline=INK, width=1)
        self.text(x0 + 4 + w / 2, y1 - 4 - h / 2, s, f, INK, anchor="mm")

    def tag(self, label, x, y, size=11.5):
        f = F(SANS_B, size)
        col = TAGCOL[label]
        w = self.tw(label, f) + 10
        tint = tuple(int(255 - (255 - v) * 0.18) for v in col)
        self.rect(x, y, x + w, y + size + 7, fill=tint, outline=col, width=1.2)
        self.text(x + 5, y + (size + 7) / 2, label, f, INK, anchor="lm")
        return x + w


# --- map --------------------------------------------------------------
LAND = [
    # North America
    [(-168, 66), (-140, 70), (-95, 72), (-80, 64), (-60, 55), (-66, 45), (-76, 38), (-81, 31),
     (-81, 25), (-90, 29), (-97, 26), (-97, 20), (-87, 21), (-83, 10), (-79, 8), (-92, 15),
     (-105, 20), (-112, 29), (-117, 33), (-124, 40), (-124, 48), (-135, 58), (-150, 60), (-165, 60)],
    [(-73, 78), (-20, 82), (-20, 70), (-45, 60), (-55, 68), (-70, 76)],  # Greenland
    # South America
    [(-80, 8), (-62, 10), (-50, 0), (-35, -6), (-39, -15), (-48, -26), (-58, -38), (-65, -42),
     (-68, -54), (-74, -50), (-72, -30), (-70, -18), (-76, -14), (-81, -5)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 44), (-5, 48), (2, 51), (8, 54), (10, 57), (5, 61), (14, 67),
     (25, 71), (40, 68), (45, 60), (40, 48), (36, 46), (28, 41), (24, 38), (20, 40), (16, 38),
     (12, 44), (8, 44), (3, 42), (-1, 37)],
    [(-6, 50), (2, 51), (0, 58), (-6, 58)],  # Britain
    # Africa
    [(-17, 21), (-6, 35), (10, 37), (20, 31), (32, 31), (35, 28), (43, 12), (51, 12), (42, -2),
     (40, -15), (35, -25), (20, -35), (17, -29), (12, -17), (13, -5), (9, 4), (-8, 4), (-16, 12)],
    [(44, -16), (50, -15), (47, -25), (44, -24)],  # Madagascar
    # Asia
    [(28, 41), (36, 36), (35, 32), (35, 28), (43, 13), (52, 16), (57, 23), (50, 26), (48, 30),
     (57, 26), (62, 25), (68, 24), (73, 20), (77, 8), (80, 15), (88, 22), (92, 21), (98, 16),
     (104, 2), (104, 10), (109, 12), (108, 21), (117, 24), (122, 30), (121, 38), (126, 38),
     (128, 35), (130, 43), (142, 48), (141, 54), (157, 60), (165, 62), (180, 66), (180, 70),
     (140, 72), (110, 77), (80, 73), (68, 70), (55, 70), (45, 68), (40, 66), (40, 48), (36, 46)],
    [(130, 31), (136, 34), (141, 38), (142, 45), (139, 40), (133, 34)],  # Japan
    [(95, 5), (106, -6), (115, -8), (106, -3), (100, 0)],  # Sumatra/Java
    [(110, 0), (117, 7), (119, 1), (116, -4), (110, -3)],  # Borneo
    [(132, -1), (141, -3), (150, -10), (141, -9), (134, -4)],  # New Guinea
    [(120, 18), (122, 18), (126, 8), (122, 7), (120, 13)],  # Philippines
    # Australia
    [(114, -22), (122, -18), (130, -12), (137, -12), (142, -11), (146, -19), (153, -26),
     (151, -34), (146, -39), (138, -35), (131, -31), (116, -35), (114, -28)],
    [(166, -46), (174, -41), (178, -38), (174, -36), (172, -41), (168, -45)],  # New Zealand
]


def draw_map(pg, x0, y0, x1, y1, pins):
    pg.rect(x0, y0, x1, y1, fill=(214, 228, 238))
    lon0, lon1, lat0, lat1 = -170, 180, 78, -50

    def P(lon, lat):
        return (x0 + (lon - lon0) / (lon1 - lon0) * (x1 - x0), y0 + (lat - lat0) / (lat1 - lat0) * (y1 - y0))

    for poly in LAND:
        pts = [(a * K, b * K) for a, b in (P(lo, la) for lo, la in poly)]
        pg.d.polygon(pts, fill=(236, 230, 214), outline=(170, 160, 140))
    f = F(SANS_B, 10.5)
    for n, lon, lat, region in pins:
        cx, cy = P(lon, lat)
        r = 7.5
        pg.d.ellipse([(cx - r) * K, (cy - r) * K, (cx + r) * K, (cy + r) * K],
                     fill=(255, 255, 255), outline=REGCOL[region], width=int(2 * K))
        pg.text(cx, cy + 0.5, str(n), f, INK, anchor="mm")


# --- page -----------------------------------------------------------------
def render(c, out):
    pg = Page()
    L, R = 16, W - 16

    # top line
    f = F(SANS_B, 13.5)
    pg.text(L, 6, c.TOP_LEFT, f, INK)
    pg.text(R, 6, c.TOP_RIGHT, f, INK, anchor="ra")
    pg.hline(L, R, 25, INK, 1.5)

    # masthead
    fm = pg.fit(c.DATE, SERIF_B, 76, R - L, 60)
    pg.text(W / 2, 90, c.DATE, fm, INK, anchor="ms")
    sub = getattr(c, "SUBLINE", "")
    dy = 0 if sub else -22
    if sub:
        fs = pg.fit(sub, SERIF_I, 17, R - L, 13)
        pg.text(W / 2, 115, sub, fs, ACCENT, anchor="ms")
    pg.hline(L, R, 124 + dy, INK, 2)

    # numbers strip
    y = 126 + dy
    n = len(c.NUMBERS)
    cw = (R - L) / n
    for i, (num, lab) in enumerate(c.NUMBERS):
        cx = L + cw * i + cw / 2
        pg.text(cx, y + 30, num, F(SERIF_B, 27), ACCENT, anchor="ms")
        fl = pg.fit(lab, SANS, 12.5, cw - 8, 11)
        pg.text(cx, y + 47, lab, fl, INK, anchor="ms")
        if i:
            pg.vline(L + cw * i, y + 5, y + 50)
    pg.hline(L, R, y + 55)

    # UTC strip
    y = 186 + dy
    pg.text(L, y + 1, "The day", F(SANS_B, 13), INK)
    pg.text(L, y + 18, "in UTC", F(SANS_B, 13), INK)
    n = len(c.UTC)
    x = L + 60
    cw = (R - x) / n
    for i, (t, lab) in enumerate(c.UTC):
        cx = x + cw * i
        pg.text(cx + 5, y + 0, t, F(SANS_B, 14), ACCENT)
        fl = pg.fit(lab, SANS, 13, cw - 9, 11.5)
        pg.text(cx + 5, y + 18, lab, fl, INK)
        pg.vline(cx, y, y + 34)
    pg.hline(L, R, y + 39, INK, 1.5)

    # leads
    y = 232 + dy
    gap = 14
    lw = (R - L - 2 * gap) / 3
    for i, s in enumerate(c.LEADS):
        x0 = L + i * (lw + gap)
        ph = 98
        pg.icon(s["icon"], x0, y, x0 + lw, y + ph)
        if s.get("badge"):
            pg.badge(s["badge"], x0 + lw, y, 22)
        pg.rect(x0, y, x0 + lw, y + ph, outline=INK, width=1)
        yy = y + ph + 6
        xx = pg.tag(s["tag"], x0, yy)
        pg.text(xx + 7, yy + 1, "%d · %s" % (i + 1, s["place"]), F(SANS_B, 13), INK)
        yy += 23
        yy = pg.para(x0, yy, s["head"], F(SERIF_B, 20), lw, 23, INK, maxlines=2)
        yy = pg.para(x0, yy + 3, s["dek"], F(SANS, 14), lw, 17, INK, maxlines=2)
        pg.text(x0, yy + 2, s["src"], F(SANS, 12.5), INK2)
    y_end = 494 + dy - 29
    pg.hline(L, R, y_end, INK, 1.5)

    # tiles: two rows
    y = y_end + 7
    per = (len(c.TILES) + 1) // 2
    gap = 10
    tw = (R - L - (per - 1) * gap) / per
    th = 140 - dy // 2
    for i, s in enumerate(c.TILES):
        r_, col = divmod(i, per)
        x0 = L + col * (tw + gap)
        y0 = y + r_ * (th + 6)
        ph = 47 - dy // 2
        pg.icon(s["icon"], x0, y0, x0 + tw, y0 + ph)
        if s.get("badge"):
            pg.badge(s["badge"], x0 + tw, y0, 15)
        if s.get("fact"):
            pg.stamp(s["fact"], x0, y0 + ph, 19)
        pg.rect(x0, y0, x0 + tw, y0 + ph, outline=INK, width=1)
        yy = y0 + ph + 4
        xx = pg.tag(s["tag"], x0, yy, 10.5)
        lab = "%d · %s" % (i + 4, s["place"])
        pg.text(xx + 5, yy + 0.5, lab, pg.fit(lab, SANS_B, 12, tw - (xx - x0) - 6, 10.5), INK)
        yy += 20
        yy = pg.para(x0, yy, s["head"], F(SERIF_B, 14.5), tw, 17, INK, maxlines=2)
        yy = pg.para(x0, yy + 1, s["dek"], F(SANS, 13.5), tw, 16.5, INK, maxlines=2)
    y = y + 2 * th + 6 + 4
    pg.hline(L, R, y, INK, 1.5)

    # map + also on
    y += 5
    rows = (len(c.ALSO) + 1) // 2
    mw = 300
    pg.text(L, y, "Where it happened · pins = story numbers", F(SANS_B, 12.5), INK)
    my0 = y + 18
    my1 = my0 + 133
    draw_map(pg, L, my0, L + mw, my1, c.PINS)
    pg.rect(L, my0, L + mw, my1, outline=INK, width=1)
    ly = my1 + 3
    lx = L
    fl = F(SANS, 12.5)
    for j, (reg, cnt) in enumerate(c.REGION_COUNTS):
        if j == 4:
            lx, ly = L, ly + 15
        s = "%s %d" % (reg, cnt)
        pg.d.ellipse([lx * K, (ly + 4) * K, (lx + 8) * K, (ly + 12) * K], outline=REGCOL[reg], width=int(2 * K), fill=(255, 255, 255))
        pg.text(lx + 10, ly - 1, s, fl, INK)
        lx += pg.tw(s, fl) + 14

    ax = L + mw + 16
    pg.text(ax, y, c.ALSO_TITLE, F(SANS_B, 14), INK)
    aw = (R - ax - 14) / 2
    fn = F(SANS_B, 13.5)
    for i, (num, reg, txt) in enumerate(c.ALSO):
        col, row = divmod(i, rows)
        xx = ax + col * (aw + 14)
        yy = y + 20 + row * 17
        pg.d.ellipse([xx * K, (yy + 5) * K, (xx + 9) * K, (yy + 14) * K], fill=REGCOL[reg])
        pg.text(xx + 14, yy, str(num), fn, INK)
        tx0 = xx + 14 + pg.tw("00", fn) + 6
        pg.text(tx0, yy, txt, pg.fit(txt, SANS, 13.5, xx + aw - tx0, 12.5), INK)
    y2 = max(ly + 17, y + 20 + rows * 17 + 2)
    # date check box
    pg.rect(L, y2, R, y2 + 44, outline=ACCENT, width=1.5)
    pg.text(L + 7, y2 + 5, "Date", F(SANS_B, 14), ACCENT)
    pg.text(L + 7, y2 + 23, "check", F(SANS_B, 14), ACCENT)
    tx = L + 56
    pg.text(tx, y2 + 4, c.DATECHECK_OUT, pg.fit(c.DATECHECK_OUT, SANS, 13.5, R - tx - 6, 12), INK)
    pg.text(tx, y2 + 23, c.DATECHECK_NOT_YET, pg.fit(c.DATECHECK_NOT_YET, SANS, 13.5, R - tx - 6, 12), INK)
    # footer
    pg.text(L, y2 + 48, c.LEGEND, pg.fit(c.LEGEND, SANS, 12.5, R - L, 11), INK2)
    if y2 + 64 > H:
        raise ValueError("page overflows: %d" % (y2 + 64))

    small = pg.im.resize((W, H), Image.LANCZOS)
    pal = small.quantize(colors=getattr(c, "COLORS", 96), method=Image.MEDIANCUT, dither=Image.NONE)
    pal.save(out, optimize=True)
    return out


if __name__ == "__main__":
    mod = sys.argv[1] if len(sys.argv) > 1 else "content"
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "entry.png")
    c = importlib.import_module(mod)
    render(c, out)
    print(out, os.path.getsize(out))
