"""Build WNA "It's out" video. Usage: python build.py <real|clone> <9x16|1x1> <out.mp4>"""
import sys, os, subprocess, json, re
sys.path.insert(0, os.path.dirname(__file__))
import gfx

VOICE, FMT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = (1080, 1920) if FMT == "9x16" else (1080, 1080)
FPS = 30
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, f"work_{VOICE}_{FMT}")
os.makedirs(WORK, exist_ok=True)
RAW = "/Users/vladimirhozjan/Documents/marketing/whatsnextaction/video/raw/"
HF = "/Users/vladimirhozjan/Documents/marketing/whatsnextaction/video/higgsfield/3d/"
N2 = RAW + "voice-02-narration 2.m4a"
N3 = RAW + "voice-02-narration v3.m4a"
MUSIC = RAW + "WNA its out bed v3.wav"
REC = {
    "engage": RAW + "ScreenRecording_09-24-2026 15-05-13_1 - engage.MP4",
    "inbox": RAW + "ScreenRecording_09-24-2026 15-08-26_1 - inbox.MP4",
    "clarify": RAW + "ScreenRecording_09-24-2026 15-10-00_1 - clarify.MP4",
    "izero": RAW + "ScreenRecording_09-24-2026 15-11-28_1 - inbox zero.MP4",
}
TOTAL = 32.6
TADA = 24.0           # music hit, IT'S OUT card
SONG_TADA = 30.33     # bass re-entry in WNA its out bed v3.wav


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(map(str, cmd)))
        print(r.stderr[-3000:])
        raise SystemExit(1)
    return r


def dur(p):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout)


def speech_islands(p, noise=-38, d=0.12):
    err = run(["ffmpeg", "-i", p, "-af", f"silencedetect=noise={noise}dB:d={d}", "-f", "null", "-"]).stderr
    ev = [(m.group(1), float(m.group(2))) for m in re.finditer(r"silence_(start|end): ([0-9.]+)", err)]
    total = dur(p)
    isl, cur = [], 0.0
    for kind, t in ev:
        if kind == "start":
            if t - cur > 0.05:
                isl.append([cur, t])
        else:
            cur = t
    if total - cur > 0.05 and (not ev or ev[-1][0] == "end"):
        isl.append([cur, total])
    return isl


# ---------------------------------------------------------------- voice clips
# slot: (start time in video, latest end)
SLOTS = {"L1": (0.30, 2.62), "L2a": (2.72, 3.62), "L2b": (3.70, 4.52), "L2c": (4.60, 5.45), "L2d": (5.52, 6.62),
         "L3": (6.85, 8.35), "L4": (8.62, 12.95), "L5": (13.20, 18.15), "L6": (18.45, 22.40),
         "L7": (24.12, 26.35), "L8": (26.55, 31.70)}
REAL = {"L1": (N2, 11.55, 13.90), "L2a": (N3, 25.58, 26.42), "L2b": (N3, 26.85, 27.63), "L2c": (N3, 28.57, 29.40),
        "L2d": (N3, 14.42, 15.60), "L3": (N2, 34.45, 35.44), "L4": (N2, 46.38, 50.32), "L5": (N2, 60.05, 64.64),
        "L6": (N2, 71.46, 74.99), "L7": (N2, 80.82, 82.50), "L8": (N2, 97.45, 101.84)}
VCHAIN = "highpass=f=75,afftdn=nf=-42,acompressor=threshold=-22dB:ratio=3:attack=5:release=120:makeup=2"


def prep_voice():
    clips = {}
    if VOICE == "real":
        for k, (src, a, b) in REAL.items():
            p = os.path.join(WORK, f"v_{k}.wav")
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(a - 0.13), "-to", str(b + 0.08), "-i", src, "-af",
                 VCHAIN + ",afade=t=in:d=0.02,areverse,afade=t=in:d=0.05,areverse", "-ar", "48000", "-ac", "1", p])
            clips[k] = p
    else:
        cdir = os.path.join(HERE, "clone" if VOICE == "clone" else "julian")
        pre = "c" if VOICE == "clone" else "j"
        for i in [1, 3, 4, 5, 6, 7, 8]:
            src = os.path.join(cdir, f"{pre}{i}.wav")
            p = os.path.join(WORK, f"v_L{i}.wav")
            isl = speech_islands(src, -40, 0.25)
            a, b = isl[0][0], isl[-1][1]
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, a - 0.03)), "-to", str(b + 0.06), "-i", src, "-af",
                 "highpass=f=75,silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-40dB:stop_silence=0.22,"
                 "afade=t=in:d=0.02,areverse,afade=t=in:d=0.05,areverse", "-ar", "48000", "-ac", "1", p])
            clips[f"L{i}"] = p
        # line 2: four separate clone generations, one per fragment
        for k in ["L2a", "L2b", "L2c", "L2d"]:
            src = os.path.join(cdir, pre + "2" + k[-1] + ".wav")
            isl = speech_islands(src, -40, 0.25)
            a, b = isl[0][0], isl[-1][1]
            p = os.path.join(WORK, f"v_{k}.wav")
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, a - 0.03)), "-to", str(b + 0.06), "-i", src, "-af",
                 "highpass=f=75,afade=t=in:d=0.02,areverse,afade=t=in:d=0.05,areverse", "-ar", "48000", "-ac", "1", p])
            clips[k] = p
    # fit into slots
    placed = {}
    for k, p in clips.items():
        s, e = SLOTS[k]
        d = dur(p)
        room = e - s
        if d > room:
            tempo = min(1.18, d / room)
            q = p.replace(".wav", "_t.wav")
            run(["ffmpeg", "-v", "error", "-y", "-i", p, "-af", f"atempo={tempo:.4f}", q])
            p, d = q, dur(q)
        placed[k] = (s, p, d)
    return placed


def voice_track(placed):
    ins, fl = [], []
    for i, (k, (s, p, d)) in enumerate(placed.items()):
        ins += ["-i", p]
        ms = int(s * 1000)
        fl.append(f"[{i}]adelay={ms}|{ms}[a{i}]")
    n = len(placed)
    fl.append("".join(f"[a{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0,apad=whole_dur={TOTAL},atrim=0:{TOTAL}[v]")
    out = os.path.join(WORK, "voice.wav")
    run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fl), "-map", "[v]", "-ar", "48000", "-ac", "1", out])
    # static gain to -16 LUFS integrated
    I = float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", run(["ffmpeg", "-i", out, "-af", "ebur128", "-f", "null", "-"]).stderr)[-1])
    out2 = os.path.join(WORK, "voice_n.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", out, "-af", f"volume={-16 - I:.2f}dB", out2])
    return out2


def phrase_times(p, start, n):
    """Start times (video clock) of the first n phrases inside a placed clip."""
    isl = speech_islands(p, -38, 0.14)
    isl = [x for x in isl if x[1] - x[0] > 0.1]
    while len(isl) > n:
        gaps = [isl[i + 1][0] - isl[i][1] for i in range(len(isl) - 1)]
        j = gaps.index(min(gaps))
        isl[j] = [isl[j][0], isl[j + 1][1]]
        del isl[j + 1]
    return [start + x[0] for x in isl]


# ---------------------------------------------------------------- video
GRADE = "eq=contrast=1.10:saturation=1.22:gamma=0.98"


def scene_filter(zoom=1.0, zx=0.5, zy=0.5):
    """Scale scene to canvas; optional static punch-in (zoom>1) centred at (zx, zy)."""
    if FMT == "9x16":
        f = f"scale={int(W*zoom)}:{int(H*zoom)}:flags=lanczos,crop={W}:{H}:(iw-{W})*{zx}:(ih-{H})*{zy}"
    else:
        f = f"scale={int(1080*zoom)}:{int(1920*zoom)}:flags=lanczos,crop={W}:{H}:(iw-{W})*{zx}:(ih-{H})*{zy}"
    return f + "," + GRADE


def seg_scene(name, src, a, b, length, zoom=1.0, zx=0.5, zy=0.5, extra=""):
    out = os.path.join(WORK, f"s_{name}.mp4")
    speed = (b - a) / length
    vf = f"trim={a}:{b},setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS}," + scene_filter(zoom, zx, zy) + extra
    vf += f",trim=0:{length},setpts=PTS-STARTPTS,format=yuv420p"
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", vf, "-an", "-r", str(FPS), "-c:v", "libx264", "-crf", "14",
         "-preset", "fast", out])
    return out


# UI panel layout
if FMT == "9x16":
    BAND, PX, PW = 600, 90, 900
else:
    BAND, PX, PW = 240, 120, 840
PH = H - BAND
SRC_TOP = 150  # remove iPhone status bar
SRC_H = int(PH * 1180 / PW)


def ui_assets():
    bgp = os.path.join(WORK, "ui_bg.png")
    if True:
        gfx.ui_background(W, H, bgp, panel=(PX, BAND, PW, PH))
        gfx.round_mask(PW, PH, 44 if FMT == "9x16" else 32, os.path.join(WORK, "ui_mask.png"))
    return bgp, os.path.join(WORK, "ui_mask.png")


def seg_ui(name, pieces, fade_white=False):
    """pieces: list of (rec, a, b, out_len). Hard cuts between pieces, composited on the teal panel."""
    bgp, maskp = ui_assets()
    parts = []
    for i, (rec, a, b, ln) in enumerate(pieces):
        p = os.path.join(WORK, f"u_{name}_{i}.mp4")
        speed = (b - a) / ln
        src_h = min(SRC_H, 2556 - SRC_TOP)
        fc = (f"[0:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},crop=1180:{src_h}:0:{SRC_TOP},"
              f"scale={PW}:{PH}:flags=lanczos,format=rgba[ui];[2:v]format=gray[m];"
              f"[ui][m]alphamerge[uim];[1:v][uim]overlay={PX}:{BAND}:shortest=1,trim=0:{ln},setpts=PTS-STARTPTS,format=yuv420p[o]")
        run(["ffmpeg", "-v", "error", "-y", "-i", REC[rec], "-loop", "1", "-framerate", str(FPS), "-i", bgp,
             "-loop", "1", "-framerate", str(FPS), "-i", maskp, "-filter_complex", fc, "-map", "[o]", "-an",
             "-r", str(FPS), "-c:v", "libx264", "-crf", "14", "-preset", "fast", p])
        parts.append(p)
    out = os.path.join(WORK, f"s_{name}.mp4")
    concat(parts, out, reencode=True, vf=("fade=t=in:st=0:d=0.30:color=white" if fade_white else None))
    return out


def seg_still(name, png, length, vf=None):
    out = os.path.join(WORK, f"s_{name}.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", png, "-t", str(length),
         "-vf", (vf + "," if vf else "") + "format=yuv420p", "-r", str(FPS), "-c:v", "libx264", "-crf", "14",
         "-preset", "fast", out])
    return out


def seg_color(name, color, length):
    out = os.path.join(WORK, f"s_{name}.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={color}:s={W}x{H}:r={FPS}:d={length}",
         "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "14", "-preset", "fast", out])
    return out


def seg_itsout(length):
    d = os.path.join(WORK, "itsout")
    os.makedirs(d, exist_ok=True)
    gfx.itsout_frames(d, W, H, n_anim=7)
    out = os.path.join(WORK, "s_itsout.mp4")
    last = os.path.join(d, "itsout_07.png")
    for k in range(8, int(length * FPS) + 1):
        dst = os.path.join(d, f"itsout_{k:02d}.png")
        if not os.path.exists(dst):
            os.link(last, dst)
    run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(d, "itsout_%02d.png"),
         "-t", str(length), "-vf", "fade=t=in:st=0:d=0.22:color=white,format=yuv420p", "-r", str(FPS),
         "-c:v", "libx264", "-crf", "14", "-preset", "fast", out])
    return out


def concat(parts, out, reencode=False, vf=None):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for p in parts:
            f.write(f"file '{p}'\n")
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst]
    if vf:
        cmd += ["-vf", vf]
    if reencode or vf:
        cmd += ["-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", "-r", str(FPS)]
    else:
        cmd += ["-c", "copy"]
    run(cmd + [out])


# ---------------------------------------------------------------- main
placed = prep_voice()
vt = voice_track(placed)
import mlx_whisper


def word_starts(p, start, targets):
    r = mlx_whisper.transcribe(p, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", word_timestamps=True,
                               language="en")
    ws = [w for sg in r["segments"] for w in sg["words"]]
    res = []
    for t in targets:
        hit = [w for w in ws if w["word"].strip().lower().strip(".,?!").startswith(t)]
        res.append(start + (hit[0]["start"] if hit else 0.0))
    return res


open_see_close = word_starts(placed["L6"][1], placed["L6"][0], ["open", "see", "close"])
url_t = word_starts(placed["L8"][1], placed["L8"][0], ["what"])[0]
if url_t <= placed["L8"][0] + 0.01:  # URL not recognised: take the last speech island
    url_t = phrase_times(placed["L8"][1], placed["L8"][0], 2)[-1]
open_see_close = [float(x) for x in open_see_close]
url_t = float(url_t)
print("voice:", {k: (round(s, 2), round(d, 2)) for k, (s, p, d) in placed.items()})
print("open/see/close:", [round(x, 2) for x in open_see_close], "url:", round(url_t, 2))

# timeline of picture (start, end) must cover 0..TOTAL
segs = []
T = {"h1": (0.0, 2.68), "h2a": (2.68, 3.66), "h2b1": (3.66, 4.56), "h2b2": (4.56, 5.49), "h1eyes": (5.49, 6.62),
     "h3": (6.62, 8.45), "ui_inbox": (8.45, 13.05), "ui_clarify": (13.05, 18.25), "ui_engage": (18.25, 22.35),
     "ui_izero": (22.35, 23.25), "black": (23.25, TADA), "itsout": (TADA, 26.40), "end": (26.40, TOTAL)}
L = {k: round(b - a, 3) for k, (a, b) in T.items()}
segs.append(seg_scene("h1", HF + "H1-video-2.mp4", 0.55, 3.05, L["h1"]))
segs.append(seg_scene("h2a", HF + "H2a-video-1.mp4", 1.30, 2.45, L["h2a"]))
segs.append(seg_scene("h2b1", HF + "H2b-video-2.mp4", 0.20, 1.10, L["h2b1"]))
segs.append(seg_scene("h2b2", HF + "H2b-video-2.mp4", 3.95, 5.00, L["h2b2"]))
segs.append(seg_scene("h1eyes", HF + "H1-video-2.mp4", 2.75, 3.90, L["h1eyes"], zoom=1.55, zx=0.5, zy=0.30))
segs.append(seg_scene("h3", HF + "H3-video-2.mp4", 1.25, 5.0, L["h3"]))
segs.append(seg_ui("inbox", [("inbox", 6.0, 66.5, L["ui_inbox"])], fade_white=True))
segs.append(seg_ui("clarify", [("clarify", 4.4, 6.4, 1.05), ("clarify", 8.9, 10.9, 1.0), ("clarify", 15.0, 17.0, 0.9),
                               ("clarify", 22.4, 26.7, L["ui_clarify"] - 2.95)]))
segs.append(seg_ui("engage", [("engage", 1.5, 1.5 + L["ui_engage"] * 1.15, L["ui_engage"])]))
segs.append(seg_ui("izero", [("izero", 15.35, 16.6, L["ui_izero"])]))
segs.append(seg_color("black", "black", L["black"]))
segs.append(seg_itsout(L["itsout"]))
ed = os.path.join(WORK, "end")
os.makedirs(ed, exist_ok=True)
gfx.endcard_states(ed, W, H)
e1 = max(0.5, url_t - T["end"][0])
e2 = 1.0
segs.append(seg_still("end_a", os.path.join(ed, "end_a.png"), round(e1, 3)))
segs.append(seg_still("end_b", os.path.join(ed, "end_b.png"), round(e2, 3)))
segs.append(seg_still("end_c", os.path.join(ed, "end_c.png"), round(TOTAL - T["end"][0] - e1 - e2, 3)))
picture = os.path.join(WORK, "picture.mp4")
concat(segs, picture, reencode=True)

# ---------------------------------------------------------------- text overlays
tx = os.path.join(WORK, "txt")
os.makedirs(tx, exist_ok=True)
scene_y = H * (0.74 if FMT == "9x16" else 0.80)
band_y = BAND * (0.60 if FMT == "9x16" else 0.52)
big = 118 if FMT == "9x16" else 96
mid = 84 if FMT == "9x16" else 64
TXT = [  # (name, text, t0, t1, y, size, max_w)
    ("t1", "That thing|you'll forget.", 0.0, T["h1"][1], scene_y, mid, W * 0.86),
    ("t2a", "Sticky notes.", T["h2a"][0], T["h2a"][1], scene_y, big, None),
    ("t2b", "Notes.", T["h2b1"][0], T["h2b1"][1], scene_y, big, None),
    ("t2c", "Mail.", T["h2b2"][0], T["h2b2"][1], scene_y, big, None),
    ("t2d", "Head.", T["h1eyes"][0], T["h1eyes"][1], scene_y, int(big * 1.25), None),
    ("t4", "Get it out of your head.", T["ui_inbox"][0] + 0.15, T["ui_inbox"][1], band_y, mid, W * 0.9),
    ("t5", "Every thing gets a next action.", T["ui_clarify"][0], T["ui_clarify"][1], band_y, mid, W * 0.9),
]
ov_in, ov_f = [], []
idx = 1


def add_overlay(name, text, t0, t1, y, size, max_w, cx=None):
    global idx
    gfx.overlay_pair(tx, name, text, W, H, y, size, max_w)
    ov_in.extend(["-loop", "1", "-framerate", str(FPS), "-i", os.path.join(tx, name + "_pop.png"),
                  "-loop", "1", "-framerate", str(FPS), "-i", os.path.join(tx, name + ".png")])
    pop_end = t0 + 0.10
    ov_f.append((idx, t0, pop_end))
    ov_f.append((idx + 1, pop_end, t1))
    idx += 2


for n, t, a, b, y, s, mw in TXT:
    add_overlay(n, t, a, b, y, s, mw)
# "Open. See. Close." builds up word by word in the band
words = ["Open.", "Open. See.", "Open. See. Close."]
for i, wtxt in enumerate(words):
    t0 = open_see_close[i]
    t1 = open_see_close[i + 1] if i < 2 else T["ui_engage"][1]
    add_overlay(f"t6_{i}", wtxt, t0, t1, band_y, 100 if FMT == "9x16" else 80, W * 0.96)

chain, last = [], "0:v"
for k, (i, a, b) in enumerate(ov_f):
    o = f"v{k}"
    chain.append(f"[{last}][{i}:v]overlay=0:0:enable='between(t,{a:.3f},{b - 0.001:.3f})':shortest=1[{o}]")
    last = o
chain.append(f"[{last}]format=yuv420p[vout]")

# ---------------------------------------------------------------- music + mix
song_off = SONG_TADA - TADA
mus = os.path.join(WORK, "music.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", MUSIC, "-af",
     "acompressor=threshold=-30dB:ratio=6:attack=20:release=400:makeup=1,dynaudnorm=f=500:g=31:m=4:b=1,"
     f"atrim=start={song_off},asetpts=PTS-STARTPTS,atrim=0:{TOTAL},afade=t=in:d=0.15,afade=t=out:st={TOTAL-1.4}:d=1.4",
     "-ar", "48000", "-ac", "2", mus])
Im = float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", run(["ffmpeg", "-i", mus, "-af", "ebur128", "-f", "null", "-"]).stderr)[-1])
mix = os.path.join(WORK, "mix.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", vt, "-i", mus, "-filter_complex",
     f"[0]aformat=channel_layouts=stereo[v];[1]volume={-30 - Im:.2f}dB[m];[v][m]amix=inputs=2:normalize=0[a]",
     "-map", "[a]", "-ar", "48000", mix])
Ix = float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", run(["ffmpeg", "-i", mix, "-af", "ebur128", "-f", "null", "-"]).stderr)[-1])
mix2 = os.path.join(WORK, "mix_n.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", mix, "-af", f"volume={-14.3 - Ix:.2f}dB,alimiter=limit=0.79:level=false", mix2])

run(["ffmpeg", "-v", "error", "-y", "-i", picture, *ov_in, "-i", mix2, "-filter_complex", ";".join(chain),
     "-map", "[vout]", "-map", f"{idx}:a", "-t", str(TOTAL), "-c:v", "libx264", "-crf", "16", "-preset", "slow",
     "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k",
     "-movflags", "+faststart", OUT])
print("done", OUT, dur(OUT))
