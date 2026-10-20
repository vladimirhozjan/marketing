#!/usr/bin/env python3
"""Generates index.html for WNA #1 Capture in 9:16 (this folder) and 1:1 (../wna-capture-1x1).

Timeline (s): H4 0-1.8 | UI 1.8-11.5 | H5 11.5-14.65 | card 14.65-19.8
Voice offsets (Julian): j1 0.05, j2 1.85, j3 2.85, j4 6.65, j5 9.35, j6 11.7, j7 14.75
"""
import json
import os
import sys
from string import Template

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 19.8

# phrase id, start of each word (s), end of phrase (s), words; "*" marks a teal key word
PHRASES = {
    "hook": [
        ("p1", [0.10, 0.45, 0.75, 0.90, 1.05], 1.80, ["*40", "things", "in", "your", "head?"]),
    ],
    "ui": [
        ("p2", [1.95, 2.20], 2.85, ["*Type", "them."]),
        ("p3", [2.93, 3.25], 3.90, ["Don't", "*sort."]),
        ("p4", [3.95, 4.25], 4.85, ["Don't", "*plan."]),
        ("p5", [4.90, 5.15], 6.55, ["Just", "*type."]),
        ("p6", [6.65, 6.90, 7.60], 9.25, ["One", "*tap.", "Anywhere."]),
        ("p7", [9.35, 9.60, 10.46, 10.60, 10.72, 10.90], 11.50, ["All", "*40.", "Out", "of", "your", "head."]),
    ],
    "calm": [
        ("p8", [12.43, 12.80], 13.25, ["Having", "*ideas."]),
        ("p9", [13.30, 13.50, 13.85], 14.60, ["Not", "holding", "*them."]),
    ],
    "card": [
        ("p10", [14.82, 14.97, 15.10, 15.25, 15.35, 15.50], DUR, ["Get", "it", "out", "of", "your", "*head."]),
    ],
}

# layout per format
L = {
    "9x16": dict(
        W=1080, H=1920,
        cap_ui="left:60px;right:60px;top:170px;height:400px;", cap_ui_fs=112,
        cap_full="left:60px;right:60px;top:1240px;height:420px;", cap_full_fs=112,
        phone="left:240px;top:610px;width:600px;height:1267px;", radius=70,
        counter="left:690px;top:560px;", counter_scale=1,
        card_logo=220, card_title_fs=104, card_url_fs=58, card_next_fs=40,
        card_cap="left:70px;right:70px;top:820px;height:300px;",
        card_logo_top=520, card_url_top=1190, card_next_top=1640,
        zoom_type=1.22, zoom_drawer=1.35, origin_type="50% 12%", origin_drawer="28% 0%",
    ),
    "1x1": dict(
        W=1080, H=1080,
        cap_ui="left:40px;width:520px;top:300px;height:480px;", cap_ui_fs=88,
        cap_full="left:50px;right:50px;top:690px;height:300px;", cap_full_fs=92,
        phone="left:585px;top:50px;width:460px;height:971px;", radius=56,
        counter="left:420px;top:780px;", counter_scale=0.85,
        card_logo=170, card_title_fs=88, card_url_fs=50, card_next_fs=34,
        card_cap="left:60px;right:60px;top:410px;height:220px;",
        card_logo_top=190, card_url_top=680, card_next_top=930,
        zoom_type=1.1, zoom_drawer=1.0, origin_type="90% 0%", origin_drawer="90% 0%",
    ),
}


def phrase_html(pid, words):
    spans = []
    for w in words:
        key = w.startswith("*")
        spans.append('<span class="w%s">%s</span>' % (" key" if key else "", w.lstrip("*")))
    return '<div class="phrase" id="%s">%s</div>' % (pid, "".join(spans))


def build(fmt, out_dir):
    c = L[fmt]
    groups = {}
    timing = {}
    for g, items in PHRASES.items():
        groups[g] = "\n".join(phrase_html(pid, words) for pid, _, _, words in items)
        for pid, starts, end, words in items:
            timing[pid] = {"s": starts, "e": end}
    tpl = Template(open(os.path.join(HERE, "template.html.tpl")).read())
    html = tpl.substitute(
        DUR=DUR, TIMING=json.dumps(timing), FMT=fmt,
        HOOK=groups["hook"], UI=groups["ui"], CALM=groups["calm"], CARD=groups["card"],
        **{k: v for k, v in c.items()},
    )
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "index.html"), "w").write(html)
    print("wrote", os.path.join(out_dir, "index.html"))


if __name__ == "__main__":
    which = sys.argv[1:] or ["9x16", "1x1"]
    for fmt in which:
        build(fmt, HERE if fmt == "9x16" else os.path.join(HERE, "..", "wna-capture-1x1"))
