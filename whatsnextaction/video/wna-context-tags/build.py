#!/usr/bin/env python3
"""Generates index.html for WNA #5 Context tags: 9:16 only (TikTok, YouTube Shorts, Instagram).

No 3D hook (Vladimir, 9. 11.): the real UI carries the video from frame 0.
  UI 0-12.2 (ctx-01-list 0-3.2 | ctx-02-computer 3.2-8.4 | ctx-03-home 8.4-12.2) | card 12.2-19.5
Voice (Julian, ../context-tags/julian, all lines Whisper-verified 9. 11.):
  j1 0.05, j2 3.30, j3 5.30, j4 8.60 (the switch to @home), j5 12.60 (ends 17.64)
Music: "One Last Click" from 18.95 s, release (27.55 in the song) lands at 8.6 on @home; fade out 18.0-19.5.
UI track: cut_ui.py after the thu 12. 11. recordings. Until assets/ui.mp4 exists the phone shows a grey placeholder.
"""
import json
import os
from string import Template

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 19.5
CARD = 12.2
NEXT = "Next week: 15 minutes that keep it all true."
SCENES = [(0.0, "ctx-01-list<br>Next Actions, mixed"), (3.2, "ctx-02-computer<br>@computer · 6 rows"),
          (8.4, "ctx-03-home<br>@home · 4 rows<br>trash on top")]


def at(offset, starts):
    return [round(offset + s, 2) for s in starts]


# phrase id, start of each word (s), end of phrase (s), words; "*" marks a teal key word (Whisper word times + offsets)
UI = [
    ("p1", at(0.05, [0.08, 0.20, 0.33, 0.60, 0.80, 1.00, 1.36, 1.52, 1.83, 2.14, 2.30]), 3.2,
     ["Why", "is", "“take", "out", "the", "*trash”", "on", "your", "list", "at", "*work?"]),
    ("p2", at(3.30, [0.09, 0.28, 0.42, 0.77, 0.91]), 5.2, ["Tell", "it", "*where", "you", "are."]),
    ("p3", at(5.30, [0.10, 0.15, 0.45, 1.13, 1.28, 1.56, 1.77, 1.98, 2.12]), 8.4,
     ["At", "your", "*desk:", "only", "what", "you", "can", "do", "there."]),
    ("p4", at(8.60, [0.06, 0.13, 0.54, 0.79, 1.21, 1.38, 2.22, 2.28, 2.40]), CARD,
     ["At", "*home:", "the", "trash", "is", "back.", "Right", "on", "*time."]),
]
CARD_P = ("p5", at(12.60, [0.0, 0.27, 0.57, 0.81]), DUR, ["Know", "your", "*next", "*action."])
URL_AT, NEXT_AT = round(12.60 + 2.06, 2), 16.2

L9 = dict(
    W=1080, H=1920,
    cap_ui="left:60px;right:60px;top:170px;height:400px;", cap_ui_fs=96,
    cap_full="left:60px;right:60px;top:1240px;height:420px;", cap_full_fs=104,
    phone="left:240px;top:610px;width:600px;height:1267px;", radius=70,
    card_logo=220, card_title_fs=104, card_url_fs=58, card_next_fs=40,
    card_cap="left:70px;right:70px;top:820px;height:300px;",
    card_logo_top=520, card_url_top=1190, card_next_top=1640,
    origin_type="50% 30%", origin_drawer="50% 30%",
)

# 1:1 for LinkedIn QubForge (Vladimir, 13. 11.), as #3/#4: captions left, phone right
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
    # calm style (Vladimir, 22. 10.): no punch-ins or flashes; phone visible from frame 0
    js = []
    a = js.append
    a('tl.set("#phone-layer", { opacity: 1 }, 0);')
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
    if has_ui:
        uivideo = (f'            <video id="ui" class="clip" src="assets/ui.mp4" muted playsinline data-start="0" '
                   f'data-duration="{round(CARD + 0.3, 2)}" data-track-index="1"></video>')
        intro = ""
    else:
        uivideo, intro = "", f'            <div id="ph">{SCENES[0][1]}</div>'
    timing = {pid: {"s": s, "e": e} for pid, s, e, _ in UI + [CARD_P]}
    tpl = Template(open(os.path.join(HERE, "template.html.tpl")).read())
    html = tpl.substitute(
        DUR=DUR, TIMING=json.dumps(timing), FMT=("1x1" if variant == "li" else "9x16"), NEXT=NEXT,
        UI="\n".join(phrase_html(p, w) for p, _, _, w in UI),
        FULL="", CARD=phrase_html(CARD_P[0], CARD_P[3]),
        HOOKCLIP="", INTRO=intro, UIVIDEO=uivideo, SCRIPT=script(has_ui), **(L1 if variant == "li" else L9),
    )
    open(os.path.join(out_dir, "index.html"), "w").write(html)
    print("wrote", os.path.join(out_dir, "index.html"), "(ui.mp4)" if has_ui else "(placeholder)")


if __name__ == "__main__":
    build("main", HERE)
    li = os.path.join(HERE, "..", "wna-context-tags-1x1")
    if os.path.isdir(li):
        build("li", li)
