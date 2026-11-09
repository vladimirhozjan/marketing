#!/usr/bin/env python3
"""Cuts the Waiting For recordings (čet 5. 11.) into the UI track assets/ui.mp4 (video 3.0-14.5 s).

Recordings (1180x2556, 60 fps, SDR):
  wait-01-add     Engage 0-1.3, menu, Waiting For 3.6, + 6.5, typing "Signed contract" 10.6-17.1,
                  "Sarah" 19.2-20.9, Add 21.5 -> row at the bottom + toast, holds to 25.2
  wait-02-list    Waiting For, five rows, still 0-4.7
  wait-03-detail  list 0-2.33, tap Feedback on the design -> detail "Mark for 1 month" 2.5-7.75, back
  wait-04-gotit   list 0-1.37, detail Confirmation of the transfer 1.5-3.65, Got it 3.65 -> list + toast,
                  menu 7.5, Next 8.7, Next page 9.7-12.9 (Confirmation of the transfer as the last row)

Groups are joined with a 0.3 s cross-fade at the scene boundaries 5.8 / 8.2 / 11.4 / 12.8; inside a group
only straight speed changes (calm style, Vladimir 22. 10.). Each group but the last runs 0.3 s past its boundary.
"""
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
UI_IN, XF = 3.0, 0.3
W1, W2, W3, W4 = "wait-01-add.MP4", "wait-02-list.MP4", "wait-03-detail.MP4", "wait-04-gotit.MP4"

# (file, src_in, src_out, video_in, video_out)
GROUPS = [
    [(W1, 19.0, 21.6, 3.0, 4.3),     # Sarah typed, Add at 21.5 -> 4.25 ("Park it.")
     (W1, 21.6, 25.0, 4.3, 6.1)],    # row at the bottom + toast
    [(W2, 0.6, 3.3, 5.8, 8.5)],      # five rows, nothing moves ("Forget it.")
    [(W3, 1.6, 2.6, 8.2, 9.2),       # tap Feedback on the design at 8.93
     (W3, 2.6, 5.1, 9.2, 11.7)],     # Mark, for 1 month
    [(W4, 2.9, 3.9, 11.4, 12.4),     # detail, Got it at 12.15
     (W4, 3.9, 4.75, 12.4, 13.1)],   # list without it
    [(W4, 9.9, 11.6, 12.8, 14.5)],   # Next Actions, the row is back (last row)
]


def cut(out):
    files = sorted({s[0] for g in GROUPS for s in g})
    args = ["ffmpeg", "-v", "error", "-y"]
    for f in files:
        args += ["-i", os.path.join(RAW, f)]
    fc, k = [], 0
    for gi, g in enumerate(GROUPS):
        for (f, a, b, va, vb) in g:
            speed = (b - a) / (vb - va)
            fc.append(f"[{files.index(f)}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{speed:.5f},fps=30,scale=720:-2,setsar=1,settb=1/30[s{k}]")
            k += 1
        first = k - len(g)
        fc.append("".join(f"[s{i}]" for i in range(first, k)) + f"concat=n={len(g)}:v=1:a=0[g{gi}]")
    prev = "g0"
    for gi in range(1, len(GROUPS)):
        off = GROUPS[gi][0][3] - UI_IN
        fc.append(f"[{prev}][g{gi}]xfade=transition=fade:duration={XF}:offset={off:.3f}[x{gi}]")
        prev = f"x{gi}"
    fc.append(f"[{prev}]format=yuv420p[out]")
    args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-an", "-c:v", "libx264", "-crf", "17", out]
    subprocess.run(args, check=True)
    print("wrote", out)


if __name__ == "__main__":
    ui = os.path.join(HERE, "assets", "ui.mp4")
    cut(ui)
    shutil.copy(ui, os.path.join(HERE, "..", "wna-waiting-for-1x1", "assets", "ui.mp4"))
