#!/usr/bin/env python3
"""Render the 19 November 2026 world-news front page (1024x1024 PNG).

A newspaper-style infographic drawn entirely with PIL: masthead naming the
day, one lead story, six more stories in a grid, and a briefs strip.
Everything is our own drawn work; no photos or copied artwork.

Run: python3 render.py  -> writes entry.png next to this script.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (250, 246, 238)      # warm off-white
CARD = (255, 255, 255)
INK = (20, 20, 20)
MUTED = (90, 86, 78)
NAVY = (22, 40, 63)
RED = (178, 34, 34)
TEAL = (18, 105, 105)
GOLD = (176, 124, 22)
RULE = (210, 203, 188)

FONT_DIR = "/usr/share/fonts/truetype/noto"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF_BLACK = lambda s: font("NotoSerif-Black.ttf", s)
F_SERIF_BOLD = lambda s: font("NotoSerif-Bold.ttf", s)
F_SERIF = lambda s: font("NotoSerif-Regular.ttf", s)
F_SANS_BOLD = lambda s: font("NotoSans-Bold.ttf", s)
F_SANS_SEMI = lambda s: font("NotoSans-SemiBold.ttf", s)
F_SANS = lambda s: font("NotoSans-Regular.ttf", s)
F_SANS_BLACK = lambda s: font("NotoSans-Black.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, text, fnt, color, max_w, line_h, max_lines=None,
                    label=""):
    lines = wrap(draw, text, fnt, max_w)
    if max_lines and len(lines) > max_lines:
        print(f"WARNING: {label!r} truncated: {len(lines)} lines > {max_lines}")
        lines = lines[:max_lines]
    for i, line in enumerate(lines):
        draw.text((x, y + i * line_h), line, font=fnt, fill=color)
    return y + len(lines) * line_h


def kicker(draw, x, y, text, color):
    f = F_SANS_BLACK(17)
    draw.text((x, y), text, font=f, fill=color)
    return y + 24


def card(draw, x, y, w, h, kicker_text, kicker_color, headline, body):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                           outline=RULE, width=2)
    pad = 18
    cx, cy = x + pad, y + 14
    cy = kicker(draw, cx, cy, kicker_text, kicker_color)
    cy = draw_text_block(draw, cx, cy + 2, headline, F_SERIF_BOLD(26), INK,
                         w - 2 * pad, 31, max_lines=2, label=headline)
    draw_text_block(draw, cx, cy + 8, body, F_SANS(18), (52, 52, 52),
                    w - 2 * pad, 24, max_lines=5, label=headline)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=RED)
    d.text((512, 18), "THE WORLD IN ONE PAGE",
           font=F_SANS_BOLD(20), fill=(196, 205, 216), anchor="ma")
    d.text((512, 44), "THURSDAY 19 NOVEMBER 2026",
           font=F_SERIF_BLACK(54), fill=(255, 255, 255), anchor="ma")
    d.text((512, 112), "The day's world news, summed up in one image",
           font=F_SERIF(22), fill=(196, 205, 216), anchor="ma")

    # ---- Lead story: Shenzhen trilateral -------------------------------
    lx, ly, lw, lh = 24, 172, 976, 208
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=10, fill=CARD,
                        outline=RULE, width=2)
    d.rounded_rectangle([lx, ly, lx + 10, ly + lh], radius=5, fill=RED)
    tx = lx + 28
    ty = ly + 16
    ty = kicker(d, tx, ty, "SHENZHEN  ·  APEC SUMMIT  ·  LEAD STORY", RED)
    ty = draw_text_block(d, tx, ty + 4,
                         "Trump, Xi and Putin issue four-point 'Declaration Towards Peace'",
                         F_SERIF_BOLD(32), INK, 640, 38, max_lines=2,
                         label="lead headline")
    draw_text_block(d, tx, ty + 8,
                    "The first-ever trilateral pledges UN reform, oil supply, "
                    "ICC limits and nuclear-risk talks — Ukraine goes "
                    "unmentioned.",
                    F_SANS(20), (52, 52, 52), 640, 26, max_lines=2,
                    label="lead body")
    # Three discs: USA / CHINA / RUSSIA
    discs = [("USA", NAVY, 0), ("CHINA", RED, 1), ("RUSSIA", TEAL, 2)]
    cx0, cy0, r = 753, ly + 58, 42
    for label, color, i in discs:
        cx = cx0 + i * 92
        d.ellipse([cx - r, cy0 - r, cx + r, cy0 + r], fill=color)
        d.text((cx, cy0 - 2), label, font=F_SANS_BLACK(18),
               fill=(255, 255, 255), anchor="mm")
    d.text((cx0 + 92, ly + 124), "Three nuclear powers, one table",
           font=F_SANS_SEMI(17), fill=MUTED, anchor="ma")
    d.text((cx0 + 92, ly + 148), "A declaration, not a deal",
           font=F_SANS(16), fill=MUTED, anchor="ma")

    # ---- Grid: six stories ----------------------------------------------
    gx, gy = 24, 394
    cw, ch, gap = 312, 236, 20
    stories = [
        ("THE GULF  ·  WAR", RED,
         "Hormuz attacks hit a record pace",
         "Iran has struck about 14 ships near the Strait of Hormuz this "
         "month, the fastest pace of the war. Three US carrier groups "
         "are in the region."),
        ("TECH  ·  MARKETS", TEAL,
         "Anthropic closes up 17% on day one",
         "The AI lab's shares open at $111.50 on Nasdaq, peak at $115.10, "
         "then fade to close at $97.17 — 17% above the $83 IPO price."),
        ("THE HAGUE  ·  LAW", GOLD,
         "Myanmar guilty of genocide",
         "The UN court finds Myanmar committed state-sponsored genocide "
         "against the Rohingya — the first state ever held responsible. "
         "Final and binding."),
        ("UKRAINE  ·  WAR", RED,
         "Crimean Bridge hit a third time",
         "An overnight strike halts traffic on the bridge to Crimea, days "
         "after attacks brought down part of its road span. Damage is "
         "being assessed."),
        ("WASHINGTON  ·  POLITICS", NAVY,
         "Jeffries set to be first Black Speaker",
         "House Democrats nominate Hakeem Jeffries 251-11. He is expected "
         "to take the gavel when the new Congress votes on 3 January."),
        ("CULTURE  ·  GAMES", TEAL,
         "Grand Theft Auto VI is out",
         "The global rollout begins at midnight local time, starting in "
         "New Zealand. Players return to Vice City on PS5 and Xbox."),
    ]
    for i, (kick, color, head, body) in enumerate(stories):
        x = gx + (i % 3) * (cw + gap)
        y = gy + (i // 3) * (ch + gap)
        card(d, x, y, cw, ch, kick, color, head, body)

    # ---- Briefs strip ----------------------------------------------------
    by = gy + 2 * ch + gap + 14
    d.rounded_rectangle([24, by, 1000, by + 90], radius=10, fill=(238, 232, 219),
                        outline=RULE, width=2)
    d.text((44, by + 12), "ALSO TODAY", font=F_SANS_BLACK(17), fill=RED)
    draw_text_block(d, 44, by + 38,
                    "Cyclone Akvan nears India's east coast; ~50,000 evacuated "
                    "in Odisha, landfall expected Friday.",
                    F_SANS(19), INK, 440, 25, max_lines=2)
    draw_text_block(d, 536, by + 38,
                    "Van Gogh's Blossoming Chestnut Trees sells for a record "
                    "$190.4m at Sotheby's in New York.",
                    F_SANS(19), INK, 440, 25, max_lines=2)

    # ---- Footer ----------------------------------------------------------
    d.text((512, 1002), "Rendered from news reported on 19 November 2026  ·  "
           "Sources: Reuters, AP, CNN, BBC, IMD",
           font=F_SANS(15), fill=MUTED, anchor="ma")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
