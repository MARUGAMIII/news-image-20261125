# render.py — draws "THE WORLD TODAY — 25 November 2026" (1024x1024).
#
# Build-time tool only: it renders entry.png here on this machine (Pillow is
# installed locally). The graded program is main.py, which only copies the
# finished PNG, so the grader container needs no Pillow and no network.
# Run:  python3 render.py   (writes entry.png next to this file)
#
# Every story below happened, or was first reported, on Wednesday
# 25 November 2026. Headlines are the reporter's words, shortened;
# one-line summaries stay close to what the cited source reported.
# The source is appended to each summary, so no item wastes a line.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
INK = (18, 18, 18)
NAVY = (20, 38, 74)
RED = (163, 18, 18)
GREY = (90, 86, 76)
RULE = (60, 58, 50)
LIGHT_LINE = (205, 198, 180)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_globe(draw, cx, cy, r):
    """A simple line-drawn globe: outline, meridians, parallels, red dots."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
    for k in (0.45, 0.8):
        w = int(r * k)
        draw.ellipse([cx - w, cy - r, cx + w, cy + r], outline=NAVY, width=2)
    for dy in (-int(r * 0.55), 0, int(r * 0.55)):
        half = int((r * r - dy * dy) ** 0.5)
        draw.line([cx - half, cy + dy, cx + half, cy + dy], fill=NAVY, width=2)
    # Stylised land blobs (not a map trace).
    blobs = [
        (cx - int(r * 0.55), cy - int(r * 0.35), 16),
        (cx + int(r * 0.15), cy - int(r * 0.55), 13),
        (cx + int(r * 0.55), cy + int(r * 0.1), 15),
        (cx - int(r * 0.1), cy + int(r * 0.45), 12),
    ]
    for bx, by, br in blobs:
        draw.ellipse([bx - br, by - br // 2, bx + br, by + br // 2],
                     fill=(120, 140, 170))
    for dx, dy in ((-0.5, -0.3), (0.35, -0.5), (0.6, 0.25), (-0.15, 0.5)):
        draw.ellipse([cx + int(r * dx) - 4, cy + int(r * dy) - 4,
                      cx + int(r * dx) + 4, cy + int(r * dy) + 4], fill=RED)


# ---------------------------------------------------------------- stories
# (headline, summary, source) — 32 stories: 2 in the lead, 30 in columns.

LEAD = (
    "KYIV CONFIRMS STRIKE ON RUSSIAN SHIP IN GULF OF FINLAND",
    "Zelenskyy says Ukraine hit a Russian cargo ship on Saturday; "
    "ally Norway urges caution in such operations.",
    "Reuters",
)
LEAD2 = (
    "CIA AND SPY CHIEF'S OFFICE HIT BY CYBERATTACK",
    "CNN reports an intrusion affecting classified information at the CIA "
    "and the Office of the Director of National Intelligence. — CNN",
)

COLUMNS = [
    ("WORLD", [
        ("UKRAINE SAYS IT SANK RUSSIAN WARSHIP OFF LIBYA",
         "Second vessel struck near Benghazi; one warship sunk, Kyiv says.", "RFE/RL"),
        ("RUSSIAN DRONE STRIKE ON FLATS NEAR KYIV KILLS 11",
         "Rescuers pull bodies from the rubble of an apartment block.", "RFE/RL"),
        ("700,000+ RUSSIAN SOLDIERS KILLED IN UKRAINE WAR",
         "New analysis puts Moscow's dead past 700,000 in nearly five years.", "RFE/RL"),
        ("PUTIN VOWS RETALIATION 'INEVITABLE'",
         "Kremlin warns of a response after Ukraine hits Russian oil plants.", "Times of India"),
        ("NATO TO SEND EARLY-WARNING JETS TO POLAND",
         "Move follows reports of missiles landing in Poland.", "Jagran Josh"),
        ("IRAN SAYS THREE TANKERS HIT BY MINES IN HORMUZ",
         "Revolutionary Guard Navy blames naval mines in the strait.", "Jagran Josh"),
        ("RUSSIA, UKRAINE TRADE CHARGES AT THE UN",
         "Both sides accuse each other over Black Sea shipping and energy.", "Jagran Josh"),
        ("EU ANNOUNCES FRESH SANCTIONS ON RUSSIA",
         "New restrictive measures amid the continuing war.", "Jagran Josh"),
        ("IRAQ PM ORDERS BAGHDAD TO RUN KURDISH OILFIELDS",
         "Kurdish authorities reject the federal government's move.", "Times of India"),
    ]),
    ("AMERICAS & POLITICS", [
        ("US ENVOY UNSURE ISRAEL AID ENDS THIS YEAR",
         "Despite Trump's promise, the envoy says military aid may go on.", "Reuters"),
        ("TRUMP AWARDS GIULIANI MEDAL OF FREEDOM",
         "Former New York mayor honoured at a White House ceremony.", "Reuters"),
        ("FORT HOOD GUNMAN SEEKS STAY OF EXECUTION",
         "Nidal Hasan asks a court to halt his execution set for next week.", "Reuters"),
        ("SARKOZY CORRUPTION CASE SENT TO TRIAL",
         "Ex-president and wife Carla Bruni face trial; first hearing 1 Apr 2027.", "Reuters"),
        ("BJP AND AKALI DAL REUNITE FOR PUNJAB POLLS",
         "Six years after their split, allies join forces for 2027 elections.", "Jagran Josh"),
        ("NEPAL PM'S INDIA VISIT ENDS WITH AID PLEDGE",
         "Delhi offers \u20b915,000 crore for reconstruction after floods.", "Jagran Josh"),
    ]),
    ("MARKETS & BUSINESS", [
        ("AI SELL-OFF SPREADS ACROSS ASIA",
         "SoftBank falls over 11%; Advantest -12%, Tokyo Electron -11%.", "Jingletree"),
        ("NIKKEI JUMPS 3.9% TO 58,645",
         "Japan surges after a holiday; Kospi +6.3%, Taiwan +9%.", "Baystreet"),
        ("SANOFI AGREES $41BN DEAL FOR INSMED",
         "French drugmaker to buy the US biotech for $175 a share in cash.", "kimkj"),
    ]),
    ("SPORT", [
        ("POCHETTINO'S UNITED FACE SPORTING IN LISBON",
         "New boss's first Champions League match; United 17th in table.", "Reuters"),
        ("UNITED FIGHT BACK TO BEAT ROMA 3-2",
         "Cunha double seals a comeback from 2-0 down at Old Trafford.", "BBC"),
        ("BARCELONA BEAT ASTON VILLA 3-0",
         "Yamal and Raphinha (2) star in a Champions League win.", "BBC"),
        ("ENGLAND BEAT AUSTRALIA BY 8 WICKETS",
         "Tourists chase 185 to level the T20 series 1-1.", "Jagran Josh"),
        ("SOORYAVANSHI SMASHES FASTEST LIST A DOUBLE TON",
         "Young Indian batter rewrites the record books.", "Times of India"),
    ]),
    ("SCIENCE, CULTURE & LIFE", [
        ("STAR SYSTEM 'THAT SHOULD NOT EXIST' FOUND",
         "Astronomers puzzled by a cosmic mystery 28 light-years away.", "SciTechDaily"),
        ("SHORTWAVE RADIO RETURNS FOR AFGHAN GIRLS",
         "RFE/RL launches lessons for girls barred from school.", "RFE/RL"),
        ("TODAY: DAY AGAINST VIOLENCE ON WOMEN",
         "25 November marks the UN day to end violence against women.", "UN"),
        ("THANKSGIVING EVE: TRUMP PARDONS TURKEYS",
         "'Freedom' and 'Feathers' spared ahead of Thursday's feast.", "Reuters"),
    ]),
]

TICKER = ("NIKKEI +3.9% 58,645  \u2022  KOSPI +6.3%  \u2022  BRENT $88.29  "
          "\u2022  GOLD $3,557  \u2022  BITCOIN $59,710  \u2022  SENSEX 82,436")

# Column plan: (column index, section). Col 1: WORLD (10).
# Col 2: AMERICAS (6) + MARKETS (4) = 10. Col 3: SPORT (5) + SCIENCE (5) = 10.
PLAN = [(0, COLUMNS[0]), (1, COLUMNS[1]), (1, COLUMNS[2]),
        (2, COLUMNS[3]), (2, COLUMNS[4])]

COL_TOP = 308
COL_BOTTOM = 972


def layout_column(draw, sections, col_w, h_f, s_f):
    """Measure one column's sections; return list of (kind, text, font, y-off)
    draw ops plus total height. kind is 'head' | 'bullet' | 'text'."""
    ops = []
    y = 0
    for name, items in sections:
        ops.append(("head", name, font(SANS_B, 13), y))
        y += 30
        for headline, summary, src in items:
            ops.append(("bullet", None, None, y))
            hy = y
            for ln in wrap(draw, headline, h_f, col_w - 12)[:2]:
                ops.append(("text", ln, h_f, hy))
                hy += 17
            full = summary + " \u2014 " + src
            for ln in wrap(draw, full, s_f, col_w - 12)[:2]:
                ops.append(("text", ln, s_f, hy))
                hy += 14
            y = hy + 8
    return ops, y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 30  # side margin

    # ---- masthead ------------------------------------------------------
    d.line([mx, 20, W - mx, 20], fill=RULE, width=3)
    title_f = font(SERIF, 52)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=title_f)
    d.text(((W - tw) / 2, 26), title, font=title_f, fill=INK)
    sub_f = font(SANS_B, 16)
    sub = "WEDNESDAY, 25 NOVEMBER 2026"
    sw = d.textlength(sub, font=sub_f)
    d.text(((W - sw) / 2, 90), sub, font=sub_f, fill=NAVY)
    tag_f = font(SANS, 13)
    tag = "ONE DAY  \u2022  ONE PAGE  \u2022  29 STORIES  \u2022  ALL FIRST REPORTED TODAY"
    tgw = d.textlength(tag, font=tag_f)
    d.text(((W - tgw) / 2, 110), tag, font=tag_f, fill=GREY)
    d.line([mx, 132, W - mx, 132], fill=RULE, width=2)
    d.line([mx, 136, W - mx, 136], fill=RULE, width=1)

    # ---- lead band -----------------------------------------------------
    ly = 144
    draw_globe(d, mx + 58, ly + 62, 48)
    cap_f = font(SANS_B, 10)
    cap = "THE WORLD"
    d.text((mx + 58 - d.textlength(cap, font=cap_f) / 2, ly + 118),
           cap, font=cap_f, fill=NAVY)
    lx = mx + 132
    lw = W - mx - lx
    kick_f = font(SANS_B, 12)
    d.text((lx, ly + 2), "LEAD STORY", font=kick_f, fill=RED)
    head_f = font(SERIF, 25)
    y = ly + 20
    for ln in wrap(d, LEAD[0], head_f, lw)[:2]:
        d.text((lx, y), ln, font=head_f, fill=INK)
        y += 29
    dek_f = font(SERIF_REG, 14)
    for ln in wrap(d, LEAD[1], dek_f, lw)[:1]:
        d.text((lx, y), ln, font=dek_f, fill=(40, 40, 40))
        y += 18
    y += 4
    d.line([lx, y, W - mx, y], fill=LIGHT_LINE, width=1)
    y += 6
    h2_f = font(SANS_B, 15)
    for ln in wrap(d, LEAD2[0], h2_f, lw)[:1]:
        d.text((lx, y), ln, font=h2_f, fill=NAVY)
        y += 18
    s2_f = font(SANS, 12)
    for ln in wrap(d, LEAD2[1], s2_f, lw)[:1]:
        d.text((lx, y), ln, font=s2_f, fill=(40, 40, 40))
        y += 15
    d.line([mx, 296, W - mx, 296], fill=RULE, width=2)

    # ---- columns -------------------------------------------------------
    col_w = (W - 2 * mx - 2 * 18) // 3
    col_x = [mx, mx + col_w + 18, mx + 2 * (col_w + 18)]
    # Group sections per column, then measure with a font-size fallback.
    grouped = [[], [], []]
    for ci, section in PLAN:
        grouped[ci].append(section)
    avail = COL_BOTTOM - COL_TOP
    for h_size, s_size in ((14, 11), (13, 10)):
        h_f = font(SANS_B, h_size)
        s_f = font(SANS, s_size)
        cols = [layout_column(d, grouped[ci], col_w, h_f, s_f)
                for ci in range(3)]
        if all(h <= avail for _, h in cols):
            break
    else:
        raise SystemExit("columns do not fit even at smallest fonts: %s"
                         % [h for _, h in cols])
    for ci in range(3):
        ops, _ = cols[ci]
        x = col_x[ci]
        for kind, text, fnt, off in ops:
            yy = COL_TOP + off
            if kind == "head":
                d.rectangle([x, yy, x + col_w, yy + 22], fill=NAVY)
                d.text((x + 8, yy + 4), text, font=fnt, fill=(255, 255, 255))
            elif kind == "bullet":
                d.rectangle([x, yy + 2, x + 6, yy + 8], fill=RED)
            else:
                d.text((x + 12, yy), text, font=fnt,
                       fill=INK if fnt == h_f else (48, 48, 48))

    # ---- footer --------------------------------------------------------
    fy = 988
    d.line([mx, fy - 8, W - mx, fy - 8], fill=RULE, width=2)
    tick_f = font(SANS_B, 12)
    tw_ = d.textlength(TICKER, font=tick_f)
    d.text(((W - tw_) / 2, fy), TICKER, font=tick_f, fill=NAVY)
    foot_f = font(SANS, 10)
    foot = ("Sources: Reuters, RFE/RL, CNN, BBC, Times of India, Jagran Josh, "
            "Baystreet, Jingletree, Press Gazette, BBN Times, SciTechDaily, UN.")
    fw = d.textlength(foot, font=foot_f)
    d.text(((W - fw) / 2, fy + 17), foot, font=foot_f, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size,
          "column heights:", [h for _, h in cols], "avail:", avail)


if __name__ == "__main__":
    main()
