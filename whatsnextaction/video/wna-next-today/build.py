#!/usr/bin/env python3
"""Generates index.html for WNA #3 Next Actions + Today, 9:16 (YT Shorts, IG), TikTok 9:16 and 1:1 for LinkedIn.

Variants:
  main    (this folder)               H7 hook 0-2.6 | UI 2.6-14.0 | card 14.0-20.5          -> YT, IG
  tiktok  (../wna-next-today-tiktok)  hand + POV 0-3.0 | UI 3.0-14.4 | card 14.4-20.9 (+0.4) -> TikTok
                                      (Vladimir, 26. 10.: native opening, no 3D, no logo until the card)
  li      (../wna-next-today-1x1)     main timeline in 1:1                                  -> LinkedIn QubForge

Voice offsets (Julian, ../next-today/julian): j1 0.05, j2 2.75, j3 4.40, j4 8.80, j5 11.40, j6 14.20 (TikTok: no j1, +0.4)
Music: "One Last Click" from 18.95 s (TikTok 18.55 s), release (27.55 s of the song) lands on the Today page at 8.6 (9.0).
UI track from the 29. 10. recordings: cut_ui.py (run it before build.py); COUNT follows the real taps.
The hand clip must be SDR (cut_ui.py converts the HLG iPhone shot), or the HDR render path hides the DOM layers.
"""
import json
import os
import sys
from string import Template

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 20.5
HOOK_END = 2.6
CARD = 14.0
NEXT = "Next week: waiting on someone?"
POV = "POV: 20 things on your list and no idea where to start"
TT = 0.4  # TikTok shift after the opening (hand 0-3.0 instead of H7 0-2.6)

# phrase id, start of each word (s), end of phrase (s), words; "*" marks a teal key word (Whisper word times + offsets)
HOOK = ("p1", [0.14, 0.49, 0.77, 1.71, 1.78, 1.84, 2.04], HOOK_END, ["*20", "next", "steps.", "Where", "do", "you", "start?"])
UI = [
    ("p2", [2.95, 3.02, 3.38, 3.67], 4.30, ["Not", "with", "all", "*20."]),
    ("p3", [4.48, 4.75, 5.10, 5.71], 8.60, ["Pick", "what", "matters", "*today."]),
    ("p4", [9.01, 9.15, 10.21, 10.30], 11.30, ["Not", "everything.", "Just", "*today."]),
    ("p5", [11.53, 11.95, 12.58, 12.78, 13.06], 13.90, ["Finish", "*one.", "Then", "the", "next."]),
]
CARD_P = ("p6", [14.20, 14.48, 14.76, 15.07], DUR, ["Know", "your", "*next", "*action."])
URL_AT, NEXT_AT = 16.08, 17.60

# counter: "NEXT 20" on the list, switches to "TODAY 0" on "Pick what matters today", then follows the taps
SWITCH = 4.40
COUNT = [(5.70, 1), (6.75, 2), (7.75, 3), (12.10, 2)]  # on the taps in cut_ui.py

L9 = dict(
    W=1080, H=1920,
    cap_ui="left:60px;right:60px;top:170px;height:400px;", cap_ui_fs=104,
    cap_full="left:60px;right:60px;top:1240px;height:420px;", cap_full_fs=112,
    phone="left:240px;top:610px;width:600px;height:1267px;", radius=70,
    counter="left:690px;top:560px;", counter_scale=1,
    card_logo=220, card_title_fs=104, card_url_fs=58, card_next_fs=40,
    card_cap="left:70px;right:70px;top:820px;height:300px;",
    card_logo_top=520, card_url_top=1190, card_next_top=1640,
    origin_type="50% 30%", origin_drawer="50% 30%",
)
# 1:1 follows the Capture 1x1 layout: captions left, phone right
L1 = dict(
    W=1080, H=1080,
    cap_ui="left:40px;width:520px;top:250px;height:480px;", cap_ui_fs=88,
    cap_full="left:50px;right:50px;top:690px;height:300px;", cap_full_fs=92,
    phone="left:585px;top:50px;width:460px;height:971px;", radius=56,
    counter="left:420px;top:790px;", counter_scale=0.85,
    card_logo=170, card_title_fs=88, card_url_fs=50, card_next_fs=34,
    card_cap="left:60px;right:60px;top:410px;height:220px;",
    card_logo_top=190, card_url_top=680, card_next_top=930,
    origin_type="70% 30%", origin_drawer="70% 30%",
)


def phrase_html(pid, words):
    spans = ['<span class="w%s">%s</span>' % (" key" if w.startswith("*") else "", w.lstrip("*")) for w in words]
    return '<div class="phrase" id="%s">%s</div>' % (pid, "".join(spans))


def shift(ph, d):
    pid, ws, e, words = ph
    return (pid, [round(t + d, 2) for t in ws], round(e + d, 2) if e < DUR else e + d, words)


def script(variant, d, ui_in):
    # calm style (Vladimir, 22. 10.): no punch-ins or flashes, soft fades between the hook, UI and the card
    js = []
    a = js.append
    if variant != "tiktok":
        a(f'tl.fromTo("#h7", {{ scale: 1.04 }}, {{ scale: 1.10, duration: {HOOK_END}, ease: "none" }}, 0);')
        a(f'tl.set("#shade", {{ opacity: 1 }}, 0); tl.set("#shade", {{ opacity: 0 }}, {HOOK_END});')
    else:
        a('tl.fromTo("#pov", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, 0.1);')
        a(f'tl.set("#pov", {{ opacity: 0 }}, {ui_in});')
    a(f'tl.fromTo("#phone-layer", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "power1.out", immediateRender: false }}, {ui_in - 0.1});')
    a(f'tl.fromTo("#counter-inner", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power1.out" }}, {ui_in + 0.1});')
    a('const countEl = document.getElementById("count"), labelEl = document.getElementById("counter-label");')
    a('tl.call(() => { labelEl.textContent = "NEXT"; countEl.textContent = "20"; }, null, 0);')
    a(f'tl.to("#counter-inner", {{ opacity: 0, duration: 0.15, ease: "none" }}, {SWITCH + d - 0.15});')
    a(f'tl.call(() => {{ labelEl.textContent = "TODAY"; countEl.textContent = "0"; }}, null, {SWITCH + d});')
    a(f'tl.to("#counter-inner", {{ opacity: 1, duration: 0.2, ease: "none" }}, {SWITCH + d});')
    for t, n in COUNT:
        a(f'tl.call(() => {{ countEl.textContent = "{n}"; }}, null, {round(t + d, 2)});')
    card = CARD + d
    a(f'tl.fromTo("#card", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power1.out" }}, {card - 0.15});')
    a(f'tl.set("#phone-layer", {{ opacity: 0 }}, {card + 0.2});')
    a(f'tl.fromTo("#logo", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "power2.out" }}, {card});')
    a(f'tl.fromTo("#url", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power1.out" }}, {URL_AT + d});')
    a(f'tl.fromTo("#next", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power1.out" }}, {NEXT_AT + d});')
    return "\n".join("      " + l for l in js)


def build(variant, out_dir):
    if variant != "tiktok":
        d, dur, ui_in = 0.0, DUR, HOOK_END
        ui_phr, full_phr = UI, [HOOK]
        hook = f'<video id="h7" class="clip full" src="assets/h7.mp4" muted playsinline data-start="0" data-duration="{HOOK_END}" data-track-index="0"></video>'
        pov = ""
    else:
        d, dur, ui_in = TT, DUR + TT, HOOK_END + TT
        ui_phr, full_phr = [shift(p, d) for p in UI], []
        hook = f'<video id="hand" class="clip full" src="assets/hand.mp4" muted playsinline data-start="0" data-duration="{ui_in}" data-track-index="0"></video>'
        pov = f'      <div id="pov">{POV}</div>'
    card_p = shift(CARD_P, d)
    timing = {pid: {"s": s, "e": e} for pid, s, e, _ in ui_phr + full_phr + [card_p]}
    tpl = Template(open(os.path.join(HERE, "template.html.tpl")).read())
    html = tpl.substitute(
        DUR=dur, TIMING=json.dumps(timing), FMT=("1x1 " if variant == "li" else "9x16 ") + variant, NEXT=NEXT,
        UI="\n".join(phrase_html(p, w) for p, _, _, w in ui_phr),
        FULL="\n".join(phrase_html(p, w) for p, _, _, w in full_phr),
        CARD=phrase_html(card_p[0], card_p[3]),
        HOOKCLIP=hook, POV=pov, INTRO="", UI_FILE="ui.mp4", UI_START=ui_in, UI_DUR=round(CARD + d - ui_in + 0.3, 2),
        SCRIPT=script(variant, d, ui_in), **(L1 if variant == "li" else L9),
    )
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "index.html"), "w").write(html)
    print("wrote", os.path.join(out_dir, "index.html"))


if __name__ == "__main__":
    dirs = {"main": HERE, "tiktok": os.path.join(HERE, "..", "wna-next-today-tiktok"), "li": os.path.join(HERE, "..", "wna-next-today-1x1")}
    for v in sys.argv[1:] or ["main", "tiktok", "li"]:
        build(v, dirs[v])
