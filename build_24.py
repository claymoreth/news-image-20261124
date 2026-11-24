#!/usr/bin/env python3
"""Build the news-image-20261124 newspaper entry (one image, 1024x1024).

Source: Mana's own 35-story summary (stories-mana-24nov.md), translated to
English newspaper style. All 35 stories present: 3 heroes + 10 cards + 22 list.
Deterministic: no time/randomness except PRESS_TIME, set once to the real
UTC time at build.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
THUMBS = os.path.join(HERE, "thumbs2d")

PRESS_TIME = "07:26"  # UTC, set at build time

W = H = 1024
NAVY = (16, 28, 58)
RED = (207, 31, 38)
CREAM = (247, 242, 234)
INK = (25, 25, 25)
GREY = (96, 96, 96)
GREEN = (46, 139, 87)
GOLD = (176, 132, 24)
OLIVE = (148, 138, 88)
RULE = (200, 190, 175)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

TICKER = ("HORMUZ: three ships ablaze  \u00b7  ZAPORIZHZHIA: 2 killed  \u00b7  "
          "SHENZHOU-24: launch tomorrow  \u00b7  COP31: no deal  \u00b7  "
          "NVIDIA: Huang restored")

STATS = [("3", "ships ablaze in Hormuz"),
         ("22", "hurt in Zaporizhzhia strike"),
         ("11", "dead from bootleg liquor"),
         ("10,000+", "migrants reach Canaries"),
         ("1,000+", "US flights delayed"),
         ("90", "experiments on Shenzhou-24")]

TAB_COLORS = [(34, 120, 74), (176, 132, 24), (207, 31, 38), (36, 84, 160),
              (20, 130, 138), (110, 62, 150), (16, 28, 58)]
TABS = ["E & SE ASIA 5", "S & C ASIA 5", "MID EAST 5", "EUROPE 5",
        "AFRICA 5", "N AMERICA 5", "S AMERICA 5"]

HEROES = [
    {"bar": "HORMUZ: THREE SHIPS ABLAZE", "badge": "3 SHIPS", "badge_color": GREEN,
     "tag": "AT SEA", "img": "flat01_hormuz.png",
     "caption": "Ships ablaze in the Strait of Hormuz",
     "loc": "1 HORMUZ \u00b7 MIDDLE EAST \u00b7 WAR",
     "head": "Three ships burn as Hormuz tension peaks",
     "deck": "Three vessels are ablaze in the strategic strait as maritime security in the Gulf worsens."},
    {"bar": "UKRAINE: STRIKE KILLS 2", "badge": "2 KILLED", "badge_color": GREEN,
     "tag": "OVERNIGHT", "img": "flat02_zaporizhzhia.png",
     "caption": "Apartment block hit in Zaporizhzhia",
     "loc": "2 ZAPORIZHZHIA \u00b7 EUROPE \u00b7 WAR",
     "head": "Russian missiles hit Zaporizhzhia, 2 killed, 22 hurt",
     "deck": "Overnight strikes damage an apartment block and transport links in south-east Ukraine; two children among the hurt."},
    {"bar": "SPACE: SHENZHOU-24 READY", "badge": "90 TESTS", "badge_color": GOLD,
     "tag": "TOMORROW", "img": "flat03_shenzhou.png",
     "caption": "Shenzhou-24 prepares for launch",
     "loc": "3 JIUQUAN \u00b7 EAST ASIA \u00b7 SPACE",
     "head": "China to launch Shenzhou-24 with Pakistani astronaut",
     "deck": "The spacecraft lifts off tomorrow morning for Tiangong, carrying the first foreign astronaut on a mission of 90 science experiments."},
]

CARDS = [
    {"bar": "ANTALYA: COP31 FALLOUT", "img": "flat04_cop31.png",
     "loc": "ANTALYA, WORLD \u00b7 CLIMATE",
     "head": "COP31 ends with no fossil-fuel deal",
     "deck": "Talks closed on Sunday with no deal on fossil fuels or adaptation funding; Ethiopia, next host, faces pressure to secure climate cash."},
    {"bar": "WASHINGTON: IRAN DELAY", "img": "flat05_trump.png",
     "loc": "WASHINGTON, AMERICAS \u00b7 WAR",
     "head": "Trump delays new Iran strike past New Year",
     "deck": "Despite Netanyahu urging a strike now, the White House holds off action past the New Year, keeping the blockade and Qatar mediation."},
    {"bar": "WASHINGTON: IRAN SANCTIONS", "img": "flat06_sanctions.png",
     "loc": "WASHINGTON, AMERICAS \u00b7 WAR",
     "head": "US sanctions Iran shadow banks",
     "deck": "Treasury targets more than 20 currency exchanges and shell firms to cut Tehran's cross-border funding."},
    {"bar": "THE HAGUE: ICJ BACKING", "img": "flat07_icj.png",
     "loc": "THE HAGUE, WORLD \u00b7 JUSTICE",
     "head": "14 nations back ICJ Rohingya verdict",
     "deck": "Fourteen nations from Europe, Africa and Oceania recognise the verdict on Myanmar, as Britain sanctions top military figures."},
    {"bar": "NVIDIA: HUANG RESTORED", "img": "flat08_nvidia.png",
     "loc": "NEW YORK, AMERICAS \u00b7 MARKETS",
     "head": "Nvidia restores Huang as chief executive",
     "deck": "The board restores Jensen Huang after national-security talks with Washington; shares jump sharply."},
    {"bar": "SEOUL: JETS INTRUDE", "img": "flat09_jets.png",
     "loc": "SEOUL, EAST ASIA \u00b7 DEFENCE",
     "head": "Russian jets enter South Korea air zone",
     "deck": "Seoul reports Russian military aircraft breaching its air defence zone, after an early warning wrongly named North Korean planes."},
    {"bar": "JAKARTA: MSCI REVIEW", "img": "flat10_msci.png",
     "loc": "JAKARTA, SE ASIA \u00b7 MARKETS",
     "head": "MSCI: Indonesia status still in review",
     "deck": "MSCI denies reports it cancelled the downgrade to Standalone Market, saying consultation runs to 30 April 2027."},
    {"bar": "GAZA: DRONE STRIKE", "img": "flat11_gaza.png",
     "loc": "GAZA, MIDDLE EAST \u00b7 WAR",
     "head": "Israeli drone strike kills 3 Gaza police",
     "deck": "A strike kills three police officers as reports say over 80% of Gaza's water and farm infrastructure is destroyed."},
    {"bar": "BENGHAZI: WARSHIP HIT", "img": "flat12_benghazi.png",
     "loc": "BENGHAZI, AFRICA \u00b7 WAR",
     "head": "Ukraine sea drone hits Russian warship",
     "deck": "Zelenskyy confirms a long-range strike on a Russian corvette at Benghazi naval base; fire rages, 10 hurt."},
    {"bar": "CANARY: MIGRANT RECORD", "img": "flat13_canary.png",
     "loc": "CANARY ISLANDS, EUROPE \u00b7 MIGRATION",
     "head": "Record migrant wave hits Canary Islands",
     "deck": "More than 10,000 migrants reach the islands in November; shelters on El Hierro are full."},
]

ALSO = [
    (14, "Singapore, Australia deepen AI and energy ties", "AP"),
    (15, "11 die from bootleg liquor in India", "Reuters"),
    (16, "Pakistani astronaut makes history on China mission", "Reuters"),
    (17, "Rohingya refugees in Bangladesh welcome ICJ verdict", "AP"),
    (18, "World oil prices fall more than 3%", "Reuters"),
    (19, "UN warns of gender violence crisis in Asia; only 16% seek help", "AP"),
    (20, "Iran court seeks Rp5.29 quadrillion from US", "Reuters"),
    (21, "Zelenskyy urges four-party peace talks now", "Reuters"),
    (22, "EU debates seven-year budget tied to Ukraine aid", "Reuters"),
    (23, "Libya demands UN probe into Benghazi attack", "Reuters"),
    (24, "Libya oil pipeline restart presses oil prices down", "Reuters"),
    (25, "Zambia, Turkey agree water and climate deal", "AP"),
    (26, "Ethiopia readies to host COP32", "Reuters"),
    (27, "Trump: China may buy 250 more Boeing jets", "Reuters"),
    (28, "UN chief urges global AI oversight deal in a year", "AP"),
    (29, "Thousands of US flights delayed by system failure", "AP"),
    (30, "Mexico to try cartel boss at home", "Reuters"),
    (31, "Car bomb hits governor's office in Meta, Colombia", "AP"),
    (32, "WHO chief visits Cuba amid health crisis", "AP"),
    (33, "Ex-Ecuador candidate Gonzalez speaks from detention", "Reuters"),
    (34, "Australia under fire after COP31 energy draft fails", "Reuters"),
    (35, "Australian music legend Molly Meldrum dies", "AP"),
]

PINS = [(56.5, 26.5, 10, -12), (35.2, 47.8, 14, -2), (98.5, 39.8, 0, 0),
        (30.7, 36.9, 0, 0), (-77.0, 38.9, 0, -4), (-77.0, 38.9, -18, 14),
        (4.3, 52.1, -16, -12), (-74.0, 40.7, 14, 10), (127.0, 37.5, 14, -2),
        (106.8, -6.2, 0, 10), (34.5, 31.5, -10, 10), (20.1, 32.1, 12, -12),
        (-16.6, 28.3, -14, 8)]

DATE_CHECK = ("Every main story on this page happened, or was first reported, on "
              "Tuesday 24 November 2026 (UTC). Developments from earlier days appear "
              "only as follow-ups, dated in their decks. Figures are as reported at "
              "press time; developing stories may since have moved on.")

CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 68), (-95, 80), (-85, 70),
     (-75, 62), (-65, 60), (-55, 47), (-70, 42), (-75, 35), (-80, 25),
     (-85, 20), (-90, 15), (-95, 18), (-105, 20), (-110, 23), (-120, 32),
     (-125, 40), (-130, 55), (-150, 60)],
    [(-80, 10), (-75, 5), (-60, 0), (-50, 0), (-40, -5), (-35, -10),
     (-40, -20), (-48, -28), (-55, -35), (-65, -40), (-70, -50), (-73, -40),
     (-72, -20), (-78, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 59), (28, 60), (30, 70), (40, 68), (45, 60),
     (40, 50), (35, 45), (30, 42), (28, 40), (23, 36), (19, 40), (15, 38),
     (12, 44), (8, 44), (3, 43), (-2, 37)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (30, 31), (35, 28),
     (43, 12), (51, 11), (48, 0), (40, -10), (35, -20), (32, -28), (25, -34),
     (18, -35), (15, -27), (12, -18), (9, -1), (9, 4), (-8, 4), (-13, 8)],
    [(30, 70), (40, 68), (55, 70), (70, 72), (90, 75), (110, 74), (130, 72),
     (150, 70), (170, 66), (178, 65), (162, 60), (158, 52), (142, 50),
     (140, 40), (135, 35), (127, 33), (122, 38), (120, 30), (110, 20),
     (105, 10), (100, 8), (95, 15), (90, 22), (85, 20), (80, 8), (77, 8),
     (72, 20), (66, 25), (60, 25), (55, 28), (50, 30), (48, 30), (43, 35),
     (36, 36), (30, 42)],
    [(95, 5), (105, 0), (110, -5), (115, -8), (120, -10), (130, -5),
     (135, 0), (140, -5), (140, 2), (130, 5), (120, 8), (105, 10)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32), (137, -35),
     (140, -38), (145, -38), (150, -37), (153, -27), (150, -22), (146, -19),
     (142, -11), (136, -12), (132, -11), (126, -14), (122, -17), (118, -20)],
    [(167, -45), (170, -42), (174, -39), (178, -38), (175, -41), (172, -43),
     (168, -47)],
]


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(path, int(size))


def wrap(draw, text, fnt, max_w):
    lines = []
    cur = ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, path, size, max_w, max_lines, min_size=8):
    s = size
    while s >= min_size:
        fnt = font(path, s)
        lines = wrap(draw, text, fnt, max_w)
        if len(lines) <= max_lines:
            return lines, fnt
        s -= 0.5
    fnt = font(path, min_size)
    return wrap(draw, text, fnt, max_w)[:max_lines], fnt


def fit_single(draw, text, path, size, max_w, min_size=7):
    s = size
    while s > min_size and draw.textlength(text, font=font(path, s)) > max_w:
        s -= 0.5
    return font(path, s)


def cover(img, w, h):
    iw, ih = img.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    x = (nw - w) // 2
    y = (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def point_in_poly(lon, lat, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > lat) != (yj > lat):
            xinters = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < xinters:
                inside = not inside
        j = i
    return inside


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Top navy bar
    d.rectangle([0, 0, W, 27], fill=NAVY)
    d.text((14, 6), "THE WORLD IN ONE DAY", font=font(SANS_B, 13), fill=WHITE)
    d.text((W - 14, 8),
           "35 STORIES \u00b7 7 REGIONS \u00b7 ALL FROM THIS ONE DAY \u00b7 PRESS TIME "
           + PRESS_TIME + " UTC",
           font=font(SANS_B, 9), fill=WHITE, anchor="ra")

    # Masthead
    d.text((W // 2, 30), "Tuesday 24 November 2026", font=font(SERIF_B, 54),
           fill=NAVY, anchor="ma")

    # Ticker
    tick_f = fit_single(d, TICKER, SERIF_I, 15, W - 28)
    d.text((W // 2, 88), TICKER, font=tick_f, fill=RED, anchor="ma")

    # Stats row
    d.line([(14, 106), (1010, 106)], fill=RULE, width=1)
    d.line([(14, 140), (1010, 140)], fill=RULE, width=1)
    cw = 996 / 6
    for i, (num, label) in enumerate(STATS):
        cx = 14 + i * cw + cw / 2
        d.text((cx, 108), num, font=font(SERIF_B, 23), fill=RED, anchor="ma")
        d.text((cx, 131), label, font=font(SANS_R, 9), fill=GREY, anchor="ma")
    for i in range(1, 6):
        x = 14 + i * cw
        d.line([(x, 108), (x, 138)], fill=RULE, width=1)

    # Region tabs
    tab_w = 996 / 7
    for i, (tab, color) in enumerate(zip(TABS, TAB_COLORS)):
        x0 = 14 + i * tab_w
        d.rectangle([x0, 142, x0 + tab_w - 2, 158], fill=color)
        d.text((x0 + (tab_w - 2) / 2, 144), tab, font=font(SANS_B, 10),
               fill=WHITE, anchor="ma")

    # Heroes
    for hi, hero in enumerate(HEROES):
        x = (14, 350, 686)[hi]
        HW = 324
        d.rectangle([x, 160, x + HW, 176], fill=RED)
        bar_f = fit_single(d, hero["bar"], SANS_B, 11, HW - 16)
        d.text((x + 8, 163), hero["bar"], font=bar_f, fill=WHITE)
        thumb = Image.open(os.path.join(THUMBS, hero["img"])).convert("RGB")
        img.paste(cover(thumb, HW, 130), (x, 176))
        # Badge + tag pills, top-right stacked
        pill_f = font(SANS_B, 9)
        for j, (txt, color) in enumerate(
                [(hero["badge"], hero["badge_color"]), (hero["tag"], NAVY)]):
            pw = d.textlength(txt, font=pill_f) + 12
            px = x + HW - 6 - pw
            py = 180 + j * 20
            d.rounded_rectangle([px, py, px + pw, py + 18], radius=7, fill=color)
            d.text((px + pw / 2, py + 3), txt, font=pill_f, fill=WHITE, anchor="ma")
        d.text((x, 308), hero["caption"], font=font(SERIF_I, 11), fill=GREY)
        d.text((x, 322), hero["loc"], font=font(SANS_B, 10), fill=RED)
        head_lines, head_f = fit_lines(d, hero["head"], SERIF_B, 19, HW, 3)
        lead = 19 * 1.08
        for k, line in enumerate(head_lines):
            d.text((x, 336 + k * lead), line, font=head_f, fill=INK)
        deck_y = max(336 + len(head_lines) * lead + 2, 372)
        deck_lines, deck_f = fit_lines(d, hero["deck"], SANS_R, 11, HW, 3)
        for k, line in enumerate(deck_lines):
            d.text((x, deck_y + k * 13), line, font=deck_f, fill=INK)
        print("hero", hi + 1, "head lines", len(head_lines),
              "deck lines", len(deck_lines), "deck bottom", deck_y + len(deck_lines) * 13)

    # Cards
    for ci, card in enumerate(CARDS):
        row, col = divmod(ci, 5)
        y0 = 408 if row == 0 else 578
        x = 14 + col * 201
        CW = 192
        thumb = Image.open(os.path.join(THUMBS, card["img"])).convert("RGB")
        img.paste(cover(thumb, CW, 56), (x, y0))
        d.rectangle([x, y0 + 56, x + CW, y0 + 71], fill=RED)
        bar_f = fit_single(d, card["bar"], SANS_B, 8.5, CW - 8)
        d.text((x + 4, y0 + 59), card["bar"], font=bar_f, fill=WHITE)
        loc_f = fit_single(d, card["loc"], SANS_B, 7.5, CW)
        d.text((x, y0 + 74), card["loc"], font=loc_f, fill=RED)
        head_lines, head_f = fit_lines(d, card["head"], SERIF_B, 13, CW, 3)
        for k, line in enumerate(head_lines):
            d.text((x, y0 + 86 + k * 15), line, font=head_f, fill=INK)
        max_deck = 3 if len(head_lines) <= 2 else 2
        deck_lines, deck_f = fit_lines(d, card["deck"], SANS_R, 9.5, CW, max_deck)
        deck_y = y0 + 86 + len(head_lines) * 15 + 2
        for k, line in enumerate(deck_lines):
            d.text((x, deck_y + k * 12), line, font=deck_f, fill=INK)
        bottom = deck_y + len(deck_lines) * 12
        assert bottom <= y0 + 165, (ci, bottom, y0)
        print("card", ci + 1, "head lines", len(head_lines),
              "deck lines", len(deck_lines), "bottom", bottom)

    # Bottom headers
    d.text((14, 748), "WHERE IT HAPPENED", font=font(SANS_B, 11), fill=INK)
    d.text((150, 750), "pins match story numbers", font=font(SERIF_I, 9), fill=GREY)
    d.text((340, 748), "22 MORE STORIES \u00b7 TUESDAY 24 NOVEMBER",
           font=font(SANS_B, 12), fill=INK)
    d.line([(14, 764), (1010, 764)], fill=INK, width=1)

    # Dotted map
    for gy in range(768, 921, 6):
        for gx in range(14, 331, 6):
            lon = (gx - 14) / 316 * 360 - 180
            lat = 84 - (gy - 768) / 152 * 142
            if any(point_in_poly(lon, lat, poly) for poly in CONTINENTS):
                d.ellipse([gx - 1.6, gy - 1.6, gx + 1.6, gy + 1.6], fill=OLIVE)

    # Pins
    for idx, (lon, lat, dx, dy) in enumerate(PINS, start=1):
        gx = 14 + (lon + 180) / 360 * 316
        gy = 768 + (84 - lat) / 142 * 152
        px = min(max(gx + dx, 14 + 8), 330 - 8)
        py = min(max(gy + dy, 768 + 8), 920 - 8)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=WHITE, width=1)
        d.text((px, py), str(idx), font=font(SANS_B, 8), fill=WHITE, anchor="mm")

    # ALSO list: two columns of 11
    for i, (n, text, src) in enumerate(ALSO):
        col, row = divmod(i, 11)
        x = 340 + col * 340
        y = 768 + row * 13.8
        size = 9
        while size > 7:
            num_f = font(SANS_B, size)
            txt_f = font(SANS_R, size)
            total = (d.textlength(str(n) + ". ", font=num_f)
                     + d.textlength(text, font=txt_f) + 4
                     + d.textlength(src, font=txt_f))
            if total <= 330:
                break
            size -= 0.5
        num_f = font(SANS_B, size)
        txt_f = font(SANS_R, size)
        num_w = d.textlength(str(n) + ". ", font=num_f)
        d.text((x, y), str(n) + ". ", font=num_f, fill=RED)
        d.text((x + num_w, y), text, font=txt_f, fill=INK)
        d.text((x + num_w + d.textlength(text, font=txt_f) + 4, y), src,
               font=txt_f, fill=GREY)

    # DATE CHECK box
    d.rectangle([14, 926, 1010, 968], outline=RED, width=2)
    d.text((24, 936), "DATE CHECK", font=font(SANS_B, 13), fill=RED)
    dc_lines = wrap(d, DATE_CHECK, font(SANS_R, 10.5), W - 14 - 150)
    for k, line in enumerate(dc_lines):
        d.text((150, 930 + k * 13), line, font=font(SANS_R, 10.5), fill=INK)

    # Sources line
    d.text((14, 972), "Sources: Reuters, AP, AFP.", font=font(SANS_R, 9), fill=GREY)
    d.text((1010, 972),
           "Scenes are drawn illustrations \u00b7 wires read to " + PRESS_TIME + " UTC",
           font=font(SANS_R, 9), fill=GREY, anchor="ra")

    # Footer bar
    d.rectangle([0, 992, W, H], fill=NAVY)
    d.text((14, 1002), "THE WORLD IN ONE DAY", font=font(SANS_B, 11), fill=WHITE)
    d.text((1010, 1004), "TUESDAY 24 NOVEMBER 2026 \u00b7 ONE PAGE",
           font=font(SANS_B, 9), fill=WHITE, anchor="ra")

    png_path = os.path.join(HERE, "entry.png")
    jpg_path = os.path.join(HERE, "entry.jpg")
    img.save(png_path, optimize=True, compress_level=9)
    img.convert("RGB").save(jpg_path, quality=88)
    print("entry.png", os.path.getsize(png_path), "bytes")
    print("entry.jpg", os.path.getsize(jpg_path), "bytes")


if __name__ == "__main__":
    main()
