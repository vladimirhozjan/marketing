#!/usr/bin/env python3
"""Cuts the Next Actions + Today recordings (29. 10.) into the UI track and the TikTok hand clip.

File names do not match their content (recorded out of order):
  next-01-list.MP4   Engage, menu, Next list from 3.5, scroll to the bottom and back 4.2-7.5
  next-03-done.MP4   Prepare slides: row 1.2, Move 2.3, Today 3.1 | Pay electricity bill: Move 5.6, Today 6.6 |
                     Call the dentist: Move 8.3, Today 9.4 | menu 12.0, Today 13.2, Today page 13.4
  next-02-today.MP4  Today page, checkmark on Prepare slides 1.75, row gone 2.5
  next-00-hand.MOV   hand with the phone, thumb scrolls the Next list (4K, rotated)

Each segment: (file, src_in, src_out, video_in, video_out) in main video seconds; ui.mp4 starts at 2.6.
Taps land on: Today 5.64 / 6.69 / 7.69, Today page 8.40, checkmark 12.0 (counter in build.py follows them).
"""
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
LIST, MOVE, DONE, HAND = "next-01-list.MP4", "next-03-done.MP4", "next-02-today.MP4", "next-00-hand.MOV"
UI_IN = 2.6

# Calm version (Vladimir, 22. 10.): taps at ~1.7x, cuts only between identical still screens,
# one cross-fade from the Today page after the moves to the clean Today page before the checkmark.
XF = 0.3
A = [
    (LIST, 3.70, 7.70, 2.60, 4.40),     # Next list, scroll down and back to the top
    (MOVE, 1.00, 3.60, 4.40, 5.929),    # Prepare slides -> Move -> Today
    (MOVE, 5.30, 6.90, 5.929, 6.871),   # Pay electricity bill -> Move -> Today
    (MOVE, 8.00, 9.70, 6.871, 7.871),   # Call the dentist -> Move -> Today
    (MOVE, 11.90, 12.40, 7.871, 8.165), # menu opens
    (MOVE, 13.00, 13.50, 8.165, 8.459), # Today tap, Today page
    (MOVE, 13.50, 14.85, 8.459, 10.50), # Today page holds (three things)
]
B = [
    (DONE, 0.00, 4.00, 10.20, 14.30),   # Today page, checkmark, two left
]


def cut(groups, out):
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
    a_len = groups[0][-1][4] - groups[0][0][3]
    fc.append(f"[g0][g1]xfade=transition=fade:duration={XF}:offset={a_len - XF:.3f},format=yuv420p[out]")
    args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-an", "-c:v", "libx264", "-crf", "17", out]
    subprocess.run(args, check=True)
    print("wrote", out)


def hand(out):
    # 3.0 s of the thumb scrolling; ffmpeg applies the rotation, the frame is 2160x3840 (9:16).
    # The iPhone shot is HDR (HLG, BT.2020): convert to SDR BT.709, otherwise HyperFrames switches to its
    # HDR layered composite and draws the videos over every DOM layer (POV caption, counter).
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.0", "-i", os.path.join(RAW, HAND), "-t", "3.0",
                    "-vf", "colorspace=all=bt709:iall=bt2020:itrc=bt2020-10:format=yuv420p,scale=1080:1920,fps=30",
                    "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
                    "-an", "-c:v", "libx264", "-crf", "17", out], check=True)
    print("wrote", out)


if __name__ == "__main__":
    ui = os.path.join(HERE, "assets", "ui.mp4")
    if "hand" not in __import__("sys").argv:
        cut([A, B], ui)
        for d in ("wna-next-today-tiktok", "wna-next-today-1x1"):
            shutil.copy(ui, os.path.join(HERE, "..", d, "assets", "ui.mp4"))
    hand(os.path.join(HERE, "..", "wna-next-today-tiktok", "assets", "hand.mp4"))
