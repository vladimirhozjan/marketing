#!/usr/bin/env python3
"""Cuts the Context tags recordings (pet 13. 11., PWA on iPhone) into the UI track assets/ui.mp4 (video 0-12.5 s).

Recordings (1180x2556, 60 fps, SDR):
  ctx-01-list      Engage 0-1.3, menu 1.5-2.75, Next Actions 3.0 (trash 4th row), scroll down 4.0-8.5, up to 11.3
  ctx-02-computer  Next 0-1.7, menu 2.0, Context filter sheet 3.0-4.0, tap @computer 4.0, menu 4.25-5.5,
                   6 rows from 6.25 (a "Load more" flashes 5.75-6.0), still to 10.4
  ctx-03-home      @computer 0-1.7, menu 2.0, sheet 3.25-4.5, tap @home 4.75, menu 5.0-6.25, 4 rows from 7.25
Groups are joined with a 0.3 s cross-fade at 3.2 / 5.3 / 7.9 / 8.7 (tap @home on the music release 8.6); inside a group
only straight speed changes (calm style, Vladimir 22. 10.). Each group but the last runs 0.3 s past its boundary.
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
UI_IN, XF = 0.0, 0.3
C1, C2, C3 = "ctx-01-list.MP4", "ctx-02-computer.MP4", "ctx-03-home.MP4"

# (file, src_in, src_out, video_in, video_out)
GROUPS = [
    [(C1, 3.0, 3.95, 0.0, 1.3),      # Next Actions, trash on row 4 ("Why is take out the trash")
     (C1, 3.95, 8.0, 1.3, 3.5)],     # scroll down the long list ("on your list at work?")
    [(C2, 1.6, 5.7, 3.2, 5.6)],      # menu -> Context filter -> @computer ("Tell it where you are.")
    [(C2, 6.25, 8.85, 5.3, 8.2)],    # 6 rows, still ("At your desk ..."); skips the "Load more" flash
    [(C3, 4.2, 4.95, 7.9, 8.9)],     # Context filter, tap @home at 8.63 (music release 8.6)
    [(C3, 7.25, 9.6, 8.7, 12.5)],    # 4 rows, trash on top ("At home: the trash is back.")
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
    cut(os.path.join(HERE, "assets", "ui.mp4"))
