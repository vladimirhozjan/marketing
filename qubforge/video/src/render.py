import asyncio, os, sys, shutil, subprocess
from playwright.async_api import async_playwright

async def main(w, h, fps, dur, out, variant='qubforge', preview_only=False, extra=''):
    base = os.path.dirname(os.path.abspath(__file__))
    frames = os.path.join(base, f'frames_{w}x{h}')
    shutil.rmtree(frames, ignore_errors=True); os.makedirs(frames)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
        await pg.goto(f'file://{base}/logo-sting-source.html?w={w}&h={h}&fps={fps}&dur={dur}&v={variant}{extra}')
        await pg.wait_for_function('window.FONTS_READY===true')
        total = await pg.evaluate('window.TOTAL_FRAMES')
        cv = await pg.query_selector('#c')
        seq = [0, int(total*0.18), int(total*0.5), total-1] if preview_only else range(total)
        for f in seq:
            await pg.evaluate(f'window.render({f})')
            await cv.screenshot(path=os.path.join(frames, f'f{f:04d}.png'))
        await b.close()
    if preview_only:
        print('preview frames in', frames); return
    subprocess.run(['ffmpeg','-y','-framerate',str(fps),'-i',os.path.join(frames,'f%04d.png'),
                    '-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','slow','-movflags','+faststart', out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('wrote', out)

if __name__ == '__main__':
    w, h = int(sys.argv[1]), int(sys.argv[2]); fps = int(sys.argv[3]); dur = float(sys.argv[4]); out = sys.argv[5]
    preview = len(sys.argv) > 6 and sys.argv[6] == 'preview'
    extra = sys.argv[7] if len(sys.argv) > 7 else ''
    asyncio.run(main(w, h, fps, dur, out, preview_only=preview, extra=extra))
