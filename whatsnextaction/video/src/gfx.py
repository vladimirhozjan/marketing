"""Graphics for the WNA "It's out" video: text overlays, backgrounds, end cards (PIL)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT_DIR = "/Users/vladimirhozjan/Documents/marketing/qubforge/video/src/fonts/inter/extras/ttf/"
BOLD = FONT_DIR + "Inter-Bold.ttf"
SEMI = FONT_DIR + "Inter-SemiBold.ttf"
MED = FONT_DIR + "Inter-Medium.ttf"
C1, C2 = (0x16, 0x4E, 0x63), (0x0E, 0x74, 0x90)
BOLT = [(15, 4), (7, 16), (13.5, 16), (13, 24), (21, 12), (14.5, 12)]  # favicon path, viewBox 28


def font(path, size):
    return ImageFont.truetype(path, size)


def gradient(W, H, highlight=True):
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        for x in range(0, W):
            t = (x / W + y / H) / 2
            px[x, y] = tuple(int(C1[i] + (C2[i] - C1[i]) * t) for i in range(3))
    if highlight:
        glow = Image.new("L", (W, H), 0)
        d = ImageDraw.Draw(glow)
        r = int(max(W, H) * 0.55)
        cx, cy = int(W * 0.3), int(H * 0.22)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=40)
        glow = glow.filter(ImageFilter.GaussianBlur(r // 2))
        im = Image.composite(Image.new("RGB", (W, H), (255, 255, 255)), im, glow)
    return im


def bolt(size, color=(255, 255, 255, 255)):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = size / 28
    d.polygon([(x * s, y * s) for x, y in BOLT], fill=color)
    return im


def text_img(text, size, path=BOLD, color=(255, 255, 255, 255), shadow=True, max_w=None, pad=40, line_gap=1.08):
    f = font(path, size)
    if "|" in text:
        lines = [l.strip() for l in text.split("|")]
        words = []
    else:
        words = text.split()
        lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if max_w and f.getlength(test) > max_w and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
    lh = int(size * line_gap)
    tw = int(max(f.getlength(l) for l in lines))
    th = lh * len(lines)
    im = Image.new("RGBA", (tw + 2 * pad, th + 2 * pad), (0, 0, 0, 0))
    if shadow:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ds = ImageDraw.Draw(sh)
        for i, l in enumerate(lines):
            x = pad + (tw - f.getlength(l)) / 2
            ds.text((x, pad + i * lh + size * 0.06), l, font=f, fill=(0, 0, 0, 200))
        sh = sh.filter(ImageFilter.GaussianBlur(size * 0.09))
        im = Image.alpha_composite(im, sh)
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = pad + (tw - f.getlength(l)) / 2
        d.text((x, pad + i * lh), l, font=f, fill=color)
    return im


def place(canvas_size, img, cx, cy, scale=1.0):
    W, H = canvas_size
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if scale != 1.0:
        img = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.LANCZOS)
    out.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))
    return out


def overlay_pair(outdir, name, text, W, H, cy, size, max_w=None, color=(255, 255, 255, 255)):
    """Writes name_pop.png (108%) and name.png (100%) full-canvas overlays."""
    t = text_img(text, size, max_w=max_w, color=color)
    place((W, H), t, W / 2, cy, 1.10).save(os.path.join(outdir, name + "_pop.png"))
    place((W, H), t, W / 2, cy, 1.0).save(os.path.join(outdir, name + ".png"))


def ui_background(W, H, path, panel=None):
    bg = gradient(W, H).convert("RGBA")
    if panel:
        x, y, w, h = panel
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([x - 6, y + 10, x + w + 6, y + h + 80], radius=50, fill=(0, 20, 30, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(28))
        bg = Image.alpha_composite(bg, sh)
    bg.convert("RGB").save(path)


def round_mask(w, h, r, path, round_bottom=False):
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, w - 1, h - 1 + (0 if round_bottom else r)], radius=r, fill=255)
    m.save(path)


def itsout_frames(outdir, W, H, n_anim=7):
    """Slam card: gradient + bolt + IT'S OUT., frames 0..n_anim-1 scale from 1.35 to 1.0, then static."""
    bg = gradient(W, H)
    short = min(W, H)
    b = bolt(int(short * 0.30))
    t = text_img("IT'S OUT.", int(short * 0.165), shadow=False, pad=10)
    group = Image.new("RGBA", (max(b.width, t.width), b.height + t.height + int(short * 0.02)), (0, 0, 0, 0))
    group.alpha_composite(b, ((group.width - b.width) // 2, 0))
    group.alpha_composite(t, ((group.width - t.width) // 2, b.height + int(short * 0.02)))
    for i in range(n_anim + 1):
        k = min(1.0, i / n_anim)
        scale = 1.0 + 0.35 * (1 - k) ** 2
        fr = bg.copy().convert("RGBA")
        fr.alpha_composite(place((W, H), group, W / 2, H / 2, scale))
        fr.convert("RGB").save(os.path.join(outdir, f"itsout_{i:02d}.png"))


def endcard_states(outdir, W, H):
    """End card without the spoken/wordmark name: bolt + URL, then the tagline."""
    bg = gradient(W, H)
    short = min(W, H)
    b = bolt(int(short * 0.30))
    url = text_img("whatsnextaction.com", int(short * 0.070), shadow=False, pad=10)
    tag = text_img("Know your next action.", int(short * 0.060), path=MED, shadow=False, pad=10,
                   color=(255, 255, 255, 215))
    cy = H * 0.42
    states = {"end_a": [], "end_b": [], "end_c": ["tag"]}
    for key, extra in states.items():
        fr = bg.copy().convert("RGBA")
        fr.alpha_composite(place((W, H), b, W / 2, cy - short * 0.14))
        pill_w, pill_h = int(url.width + short * 0.07), int(url.height + short * 0.03)
        pill = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 0))
        ImageDraw.Draw(pill).rounded_rectangle([0, 0, pill_w - 1, pill_h - 1], radius=pill_h // 2,
                                               fill=(255, 255, 255, 40), outline=(255, 255, 255, 150),
                                               width=max(2, short // 360))
        pill.alpha_composite(url, ((pill_w - url.width) // 2, (pill_h - url.height) // 2))
        fr.alpha_composite(place((W, H), pill, W / 2, cy + short * 0.14))
        if "tag" in extra:
            fr.alpha_composite(place((W, H), tag, W / 2, cy + short * 0.30))
        fr.convert("RGB").save(os.path.join(outdir, key + ".png"))
