#!/usr/bin/env python3
"""Generates index.html for WNA #4 Waiting For: 9:16 (Instagram) and 1:1 (LinkedIn QubForge).

Variants:
  main  (this folder)              H8 hook 0-3.0 | UI 3.0-14.2 | card 14.2-22.0 -> IG
  li    (../wna-waiting-for-1x1)   same timeline in 1:1                         -> LinkedIn QubForge

Voice (Julian, ../waiting-for/julian, all lines Whisper-verified 2. 11.):
  j1 0.05, j2 3.85 (on the Add tap), j3 6.00, j4 8.40, j5 11.60, j6 14.50 (j6 ends 21.49)
UI scenes (cut_ui.py after the wed 4. 11. recordings): wait-01 3.0-5.8 | wait-02 5.8-8.2 | wait-03 8.2-11.4 | wait-04 11.4-14.2
Music: "One Last Click" from 17.8 s (the song is only 39.8 s long, so the release at 27.55 lands at 9.75,
  on the detail screen "Mark · 1mo", not on "Forget it." as planned).
UI track: cut_ui.py (run it before build.py). Until assets/ui.mp4 exists the phone shows a grey placeholder with the scene name.
"""
import json
import os
import sys
from string import Template

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 22.0
HOOK_END = 3.0
CARD = 14.2
NEXT = "Next week: already out? Do what fits."
SCENES = [(3.0, "wait-01-add<br>Signed contract · Sarah"), (5.8, "wait-02-list<br>4 rows"),
          (8.2, "wait-03-detail<br>Mark · 1mo"), (11.4, "wait-04-gotit<br>→ Next Actions")]

# phrase id, start of each word (s), end of phrase (s), words; "*" marks a teal key word (Whisper word times + offsets)
HOOK = ("p1", [0.17, 0.41, 0.85, 1.07, 1.29, 1.37, 1.95, 2.18, 2.36, 2.66, 2.78], HOOK_END,
        ["*3", "people", "owe", "you", "an", "answer.", "Can", "you", "name", "all", "*three?"])
UI = [
    ("p2", [3.94, 4.18], 5.80, ["*Park", "it."]),
    ("p3", [6.10, 6.44], 8.20, ["*Forget", "it."]),
    ("p4", [8.52, 8.67, 8.94, 9.40, 10.15, 10.42, 10.65, 10.87], 11.40,
     ["The", "app", "remembers", "*who.", "And", "for", "how", "*long."]),
    ("p5", [11.64, 11.85, 11.97, 12.58, 12.87, 13.18, 13.33, 13.64], 14.15,
     ["When", "it", "arrives,", "it's", "*back", "on", "your", "list."]),
]
CARD_P = ("p6", [16.55, 16.70, 17.00, 17.20, 17.45], DUR, ["A", "system", "you", "can", "*trust."])
URL_AT, NEXT_AT = 18.62, 19.80

L9 = dict(
    W=1080, H=1920,
    cap_ui="left:60px;right:60px;top:170px;height:400px;", cap_ui_fs=104,
    cap_full="left:60px;right:60px;top:1240px;height:420px;", cap_full_fs=104,
    phone="left:240px;top:610px;width:600px;height:1267px;", radius=70,
    card_logo=220, card_title_fs=104, card_url_fs=58, card_next_fs=40,
    card_cap="left:70px;right:70px;top:820px;height:300px;",
    card_logo_top=520, card_url_top=1190, card_next_top=1640,
    origin_type="50% 30%", origin_drawer="50% 30%",
)
# 1:1 as #3: captions left, phone right
L1 = dict(
    W=1080, H=1080,
    cap_ui="left:40px;width:520px;top:250px;height:480px;", cap_ui_fs=88,
    cap_full="left:50px;right:50px;top:690px;height:300px;", cap_full_fs=84,
    phone="left:585px;top:50px;width:460px;height:971px;", radius=56,
    card_logo=170, card_title_fs=88, card_url_fs=50, card_next_fs=34,
    card_cap="left:60px;right:60px;top:410px;height:220px;",
    card_logo_top=190, card_url_top=680, card_next_top=930,
    origin_type="70% 30%", origin_drawer="70% 30%",
)


def phrase_html(pid, words):
    spans = ['<span class="w%s">%s</span>' % (" key" if w.startswith("*") else "", w.lstrip("*")) for w in words]
    return '<div class="phrase" id="%s">%s</div>' % (pid, "".join(spans))


def script(has_ui):
    # calm style (Vladimir, 22. 10.): no punch-ins or flashes, soft fades between the hook, UI and the card
    js = []
    a = js.append
    a(f'tl.fromTo("#h8", {{ scale: 1.04 }}, {{ scale: 1.10, duration: {HOOK_END}, ease: "none" }}, 0);')
    a(f'tl.set("#shade", {{ opacity: 1 }}, 0); tl.set("#shade", {{ opacity: 0 }}, {HOOK_END});')
    a(f'tl.fromTo("#phone-layer", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "power1.out", immediateRender: false }}, {HOOK_END - 0.1});')
    if not has_ui:
        a('const ph = document.getElementById("ph");')
        for t, label in SCENES:
            a(f'tl.call(() => {{ ph.innerHTML = "{label}"; }}, null, {t});')
    a(f'tl.fromTo("#card", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power1.out" }}, {CARD - 0.15});')
    a(f'tl.set("#phone-layer", {{ opacity: 0 }}, {CARD + 0.2});')
    a(f'tl.fromTo("#logo", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "power2.out" }}, {CARD});')
    a(f'tl.fromTo("#url", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power1.out" }}, {URL_AT});')
    a(f'tl.fromTo("#next", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power1.out" }}, {NEXT_AT});')
    return "\n".join("      " + l for l in js)


def build(variant, out_dir):
    has_ui = os.path.exists(os.path.join(out_dir, "assets", "ui.mp4"))
    hook = f'<video id="h8" class="clip full" src="assets/h8.mp4" muted playsinline data-start="0" data-duration="{HOOK_END}" data-track-index="0"></video>'
    if has_ui:
        uivideo = (f'            <video id="ui" class="clip" src="assets/ui.mp4" muted playsinline data-start="{HOOK_END}" '
                   f'data-duration="{round(CARD - HOOK_END + 0.3, 2)}" data-track-index="1"></video>')
        intro = ""
    else:
        uivideo, intro = "", f'            <div id="ph">{SCENES[0][1]}</div>'
    timing = {pid: {"s": s, "e": e} for pid, s, e, _ in UI + [HOOK, CARD_P]}
    tpl = Template(open(os.path.join(HERE, "template.html.tpl")).read())
    html = tpl.substitute(
        DUR=DUR, TIMING=json.dumps(timing), FMT=("1x1" if variant == "li" else "9x16"), NEXT=NEXT,
        UI="\n".join(phrase_html(p, w) for p, _, _, w in UI),
        FULL=phrase_html(HOOK[0], HOOK[3]), CARD=phrase_html(CARD_P[0], CARD_P[3]),
        HOOKCLIP=hook, INTRO=intro, UIVIDEO=uivideo, SCRIPT=script(has_ui), **(L1 if variant == "li" else L9),
    )
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "index.html"), "w").write(html)
    print("wrote", os.path.join(out_dir, "index.html"), "(ui.mp4)" if has_ui else "(placeholder)")


if __name__ == "__main__":
    dirs = {"main": HERE, "li": os.path.join(HERE, "..", "wna-waiting-for-1x1")}
    for v in sys.argv[1:] or ["main", "li"]:
        build(v, dirs[v])
