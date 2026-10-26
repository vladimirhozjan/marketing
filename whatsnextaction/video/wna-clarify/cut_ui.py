#!/usr/bin/env python3
"""Cuts the Clarify UI recordings (22. 10.) into the continuous UI tracks.

File names do not match their content (recorded out of order):
  clarify-03-inboxzero.MP4  Inbox scroll, Clarify, 3x No (Someday, Reference, Trash), Reply to Ana
  clarify-02-twominutes.MP4 Reply to Ana: Yes, Single, under 2 min Yes, Do it now (clean take, used)
  clarify-01-no.MP4         Book flight for March: Yes, Single, No, Create Next Action, Inbox Zero

Each segment: (file, src_in, src_out, video_in, video_out); speed follows from the lengths.
Taps land on: Someday 5.76, Reference 6.39, Trash 7.12, Do it now 10.46, Inbox Zero 13.60 (video s).
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
NO, TWO, ZERO = "clarify-03-inboxzero.MP4", "clarify-02-twominutes.MP4", "clarify-01-no.MP4"

# Calm version (Vladimir, 22. 10.: "preveč skače"): taps run at 1.5-2x, cuts only between identical
# still screens, static screens absorb the timing, one cross-fade on the jump to the last item.
XF = 0.3  # cross-fade from "Do it now" to the last item, centred on 11.2
A_TAIL = [
    # 3x No: No taps 13.85 / 17.25 / 24.37, destination taps 14.69 / 18.69 / 25.14 -> 5.68 / 6.62 / 7.20
    (NO, 13.60, 14.85, 4.95, 5.78),
    (NO, 17.00, 18.85, 5.78, 6.705),
    (NO, 24.15, 25.60, 6.705, 7.43),
    # Reply to Ana: Yes 1.08, Single 2.73, Yes do it now 5.50 -> 10.40
    (TWO, 0.60, 2.97, 7.43, 8.615),
    (TWO, 2.97, 5.50, 8.615, 10.40),
    (TWO, 5.50, 6.45, 10.40, 11.35),
]
B = [
    # Book flight: Clarify 4.0, Yes 6.29, Single 7.33, No 8.79, keyboard away 10.65, Create 12.70, Inbox Zero 12.85
    (ZERO, 3.10, 4.60, 11.05, 11.80),
    (ZERO, 5.60, 6.60, 11.80, 12.30),
    (ZERO, 7.00, 7.60, 12.30, 12.60),
    (ZERO, 8.40, 9.20, 12.60, 13.00),
    (ZERO, 10.45, 10.85, 13.00, 13.20),
    (ZERO, 12.05, 12.85, 13.20, 13.60),
    (ZERO, 12.85, 14.45, 13.60, 15.20),
]
MAIN = ([(NO, 8.65, 13.60, 2.00, 4.95)] + A_TAIL, B)   # Inbox, Clarify tap 9.65, Is it actionable?
TIKTOK = ([(NO, 9.30, 13.60, 2.80, 4.95)] + A_TAIL, B)
INTRO = ([(NO, 3.50, 8.90, 0.00, 2.00)], None)  # scroll to the bottom and back, from frame 0


def cut(parts, out):
    groups = [g for g in parts if g]
    segs = [s for g in groups for s in g]
    files = sorted({s[0] for s in segs})
    args = ["ffmpeg", "-v", "error", "-y"]
    for f in files:
        args += ["-i", os.path.join(RAW, f)]
    fc, k = [], 0
    for gi, g in enumerate(groups):
        for (f, a, b, va, vb) in g:
            speed = (b - a) / (vb - va)
            fc.append(f"[{files.index(f)}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{speed:.5f},fps=30,scale=720:-2,settb=1/30[s{k}]")
            k += 1
        first = k - len(g)
        fc.append("".join(f"[s{i}]" for i in range(first, k)) + f"concat=n={len(g)}:v=1:a=0[g{gi}]")
    if len(groups) == 2:
        a_len = groups[0][-1][4] - groups[0][0][3]
        fc.append(f"[g0][g1]xfade=transition=fade:duration={XF}:offset={a_len - XF:.3f},format=yuv420p[out]")
    else:
        fc.append("[g0]format=yuv420p[out]")
    args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-an", "-c:v", "libx264", "-crf", "17", out]
    subprocess.run(args, check=True)
    print("wrote", out)


if __name__ == "__main__":
    tt = os.path.join(HERE, "..", "wna-clarify-tiktok", "assets")
    cut(MAIN, os.path.join(HERE, "assets", "ui.mp4"))
    cut(TIKTOK, os.path.join(tt, "ui-tt.mp4"))
    cut(INTRO, os.path.join(tt, "ui-intro.mp4"))
