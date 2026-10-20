#!/usr/bin/env python3
"""Generates index.html for WNA #2 Clarify, 9:16 only (persona B: YT Shorts, TikTok, IG).

Variants:
  main    (this folder)           H6 hook 0-2.0 | UI 2.0-15.2 | card 15.2-21.0   -> YT, IG
  tiktok  (../wna-clarify-tiktok) UI intro 0-2.0 | H6 2.0-2.8 | UI 2.8-15.2 | card -> TikTok (A/B hook)

Voice offsets (Julian): j1 0.05, j2 2.05, j3 3.75, j4 4.95, j5 8.2, j6 9.45, j7 11.2, j8 15.35
Music: "One Last Click" from 13.55 s, release (27.55 s of the song) lands on Inbox Zero at 14.0.
UI cut points (CUT) are placeholders until the Thursday recordings; retime them there.
"""
import json
import os
import sys
from string import Template

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 21.0
CARD = 15.2
NEXT = "Next week: what to do right now."

# phrase id, start of each word (s), end of phrase (s), words; "*" marks a teal key word
HOOK = ("p1", [0.05, 0.40, 1.30, 1.55], 2.00, ["*40", "things.", "Now", "what?"])
Q = ("p2", [2.10, 2.35], 3.70, ["One", "*question."])
UI = [
    ("p3", [3.80, 3.95, 4.10], 4.90, ["Is", "it", "*actionable?"]),
    ("p4", [4.95, 5.76, 5.95, 6.39, 6.62, 7.12, 7.45], 8.10, ["No?", "*Park", "it.", "*File", "it.", "*Trash", "it."]),
    ("p5", [8.25, 8.65, 8.85], 9.35, ["Under", "*2", "minutes?"]),
    ("p6", [9.45, 9.75, 10.00, 10.46, 10.65], 11.10, ["Don't", "file", "it.", "*Do", "it."]),
    ("p7", [11.30, 11.89, 12.43, 12.69, 13.00], 14.00, ["Everything", "else:", "one", "*next", "*step."]),
]
CARD_P = ("p8", [15.38, 15.60, 15.85, 16.15], DUR, ["Know", "your", "*next", "*action."])

# counter: N taps 40 -> 37, Do it 36, jump to 1 before the last item, 0 on Inbox Zero
COUNT = [(5.76, 39), (6.39, 38), (7.12, 37), (10.46, 36), (11.20, 1), (13.60, 0)]
KEY_N = [5.70, 6.33, 7.06]
KEY_Y = [8.15, 11.6]

L = dict(
    W=1080, H=1920,
    cap_ui="left:60px;right:60px;top:170px;height:400px;", cap_ui_fs=104,
    cap_full="left:60px;right:60px;top:1240px;height:420px;", cap_full_fs=112,
    phone="left:240px;top:610px;width:600px;height:1267px;", radius=70,
    counter="left:690px;top:560px;", counter_scale=1,
    card_logo=220, card_title_fs=104, card_url_fs=58, card_next_fs=40,
    card_cap="left:70px;right:70px;top:820px;height:300px;",
    card_logo_top=520, card_url_top=1190, card_next_top=1640,
    key=170, keyY="left:36px;top:1180px;", keyN="right:36px;top:1180px;",
    origin_type="50% 30%", origin_drawer="50% 30%",
)


def phrase_html(pid, words):
    spans = ['<span class="w%s">%s</span>' % (" key" if w.startswith("*") else "", w.lstrip("*")) for w in words]
    return '<div class="phrase" id="%s">%s</div>' % (pid, "".join(spans))


def script(variant):
    ui_in = 2.0 if variant == "main" else 2.8
    js = []
    a = js.append
    if variant == "main":
        a('tl.fromTo("#h6", { scale: 1.04 }, { scale: 1.16, duration: 2.0, ease: "power1.in" }, 0);')
        a('tl.set("#shade", { opacity: 1 }, 0); tl.set("#shade", { opacity: 0 }, 2.0);')
    else:
        # UI from frame 0, then a short H6 reaction, then back to the phone
        a('tl.set("#phone-layer", { opacity: 1 }, 0);')
        a('tl.fromTo("#counter-inner", { scale: 0.5, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }, 0.1);')
        a('flash(2.0); tl.set("#phone-layer", { opacity: 0 }, 2.0);')
        a('tl.set("#shade", { opacity: 1 }, 2.0); tl.set("#shade", { opacity: 0 }, 2.8);')
        a('tl.fromTo("#h6", { scale: 1.10 }, { scale: 1.18, duration: 0.8, ease: "none" }, 2.0);')
    a(f'flash({ui_in});')
    a(f'tl.set("#phone-layer", {{ opacity: 1 }}, {ui_in});')
    a(f'tl.fromTo("#phone", {{ y: 220, scale: 1.08 }}, {{ y: 0, scale: 1, duration: 0.35, ease: "power3.out" }}, {ui_in});')
    if variant == "main":
        a(f'tl.fromTo("#counter-inner", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {ui_in + 0.15});')
    # punch-in on the question, back out for the taps
    a('tl.to("#phone", { scale: 1.18, duration: 0.4, ease: "power3.inOut" }, 3.7);')
    a('tl.to("#phone", { scale: 1, duration: 0.35, ease: "power3.inOut" }, 4.9);')
    # keys
    a('tl.fromTo([".key-cap"], { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)", stagger: 0.08 }, 3.9);')
    for t in KEY_N:
        a(f'tl.fromTo("#keyN", {{ y: 0 }}, {{ y: 10, duration: 0.08, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }}, {t});')
        a(f'tl.fromTo("#keyN", {{ boxShadow: "0 10px 0 #9fb3bb, 0 26px 50px rgba(0,0,0,0.45)" }}, {{ boxShadow: "0 0px 0 #9fb3bb, 0 0 60px rgba(34,211,238,0.9)", duration: 0.08, yoyo: true, repeat: 1, immediateRender: false }}, {t});')
    for t in KEY_Y:
        a(f'tl.fromTo("#keyY", {{ y: 0 }}, {{ y: 10, duration: 0.08, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }}, {t});')
        a(f'tl.fromTo("#keyY", {{ boxShadow: "0 10px 0 #9fb3bb, 0 26px 50px rgba(0,0,0,0.45)" }}, {{ boxShadow: "0 0px 0 #9fb3bb, 0 0 60px rgba(34,211,238,0.9)", duration: 0.08, yoyo: true, repeat: 1, immediateRender: false }}, {t});')
    a('tl.to([".key-cap"], { opacity: 0, scale: 0.8, duration: 0.2 }, 12.3);')
    # jump to the last item
    a('flash(11.2);')
    # counter
    a('const countEl = document.getElementById("count");')
    a('tl.call(() => { countEl.textContent = "40"; }, null, 0);')
    for t, n in COUNT:
        a(f'tl.call(() => {{ countEl.textContent = "{n}"; }}, null, {t});')
        a(f'tl.fromTo("#count", {{ scale: 1.22 }}, {{ scale: 1, duration: 0.18, ease: "power2.out", immediateRender: false }}, {t});')
    a('tl.fromTo("#counter-inner", { scale: 1 }, { scale: 1.2, duration: 0.16, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, 13.6);')
    a(f'tl.set("#phone-layer", {{ opacity: 0 }}, {CARD});')
    # end card
    a(f'flash({CARD});')
    a(f'tl.set("#card", {{ opacity: 1 }}, {CARD});')
    a(f'tl.fromTo("#logo", {{ scale: 0.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {CARD});')
    a('tl.fromTo("#url", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25, ease: "back.out(2)" }, 17.18);')
    a('tl.fromTo("#next", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power1.out" }, 18.6);')
    return "\n".join("      " + l for l in js)


def build(variant, out_dir):
    if variant == "main":
        ui_phr, full_phr = [Q] + UI, [HOOK]
        h6 = (0, 2.0)
        intro = ""
        ui = ("ui.mp4", 2.0, CARD - 2.0)
    else:
        ui_phr, full_phr = [HOOK] + UI, [Q]
        h6 = (2.0, 0.8)
        intro = '            <video id="uiintro" class="clip" src="assets/ui-intro.mp4" muted playsinline data-start="0" data-duration="2.0" data-track-index="1"></video>'
        ui = ("ui-tt.mp4", 2.8, CARD - 2.8)
    timing = {pid: {"s": s, "e": e} for pid, s, e, _ in ui_phr + full_phr + [CARD_P]}
    if variant != "main":
        timing["p2"]["e"] = 2.8  # "One question." lives on the short H6 shot only
    tpl = Template(open(os.path.join(HERE, "template.html.tpl")).read())
    html = tpl.substitute(
        DUR=DUR, TIMING=json.dumps(timing), FMT="9x16 " + variant, NEXT=NEXT,
        UI="\n".join(phrase_html(p, w) for p, _, _, w in ui_phr),
        FULL="\n".join(phrase_html(p, w) for p, _, _, w in full_phr),
        CARD=phrase_html(CARD_P[0], CARD_P[3]),
        H6_START=h6[0], H6_DUR=h6[1], INTRO=intro, UI_FILE=ui[0], UI_START=ui[1], UI_DUR=round(ui[2], 2),
        SCRIPT=script(variant), **L,
    )
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "index.html"), "w").write(html)
    print("wrote", os.path.join(out_dir, "index.html"))


if __name__ == "__main__":
    for v in sys.argv[1:] or ["main", "tiktok"]:
        build(v, HERE if v == "main" else os.path.join(HERE, "..", "wna-clarify-tiktok"))
