<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=$W, height=$H" />
    <title>WNA Clarify $FMT</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face { font-family: "Inter"; src: url("assets/Inter-Bold.ttf") format("truetype"); font-weight: 700; }
      @font-face { font-family: "Inter"; src: url("assets/Inter-SemiBold.ttf") format("truetype"); font-weight: 600; }
      @font-face { font-family: "Montserrat"; src: url("assets/Montserrat.ttf") format("truetype"); font-weight: 100 900; }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: #0a0e1a; }
      #root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Inter", sans-serif; }
      .layer { position: absolute; inset: 0; }
      #bg {
        background:
          radial-gradient(ellipse 85% 55% at 50% 66%, rgba(14, 116, 144, 0.6), rgba(10, 14, 26, 0) 70%),
          linear-gradient(180deg, #0a0e1a 0%, #0c1824 55%, #0a0e1a 100%);
      }
      .full { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      #shade {
        background: linear-gradient(180deg, rgba(5, 10, 18, 0) 45%, rgba(5, 10, 18, 0.72) 78%, rgba(5, 10, 18, 0.85) 100%);
        opacity: 0;
      }

      /* captions */
      .caps { position: absolute; }
      #cap-ui { $cap_ui }
      #cap-full { $cap_full }
      #cap-card { $card_cap }
      .phrase { position: absolute; inset: 0; display: flex; flex-wrap: wrap; align-content: center; justify-content: center; gap: 0 0.26em; }
      #cap-ui .phrase { font-size: ${cap_ui_fs}px; }
      #cap-full .phrase { font-size: ${cap_full_fs}px; }
      #cap-card .phrase { font-size: ${card_title_fs}px; }
      .w {
        display: block; color: #f4f7fb; font-weight: 700; line-height: 1.08; letter-spacing: -0.035em; opacity: 0;
        text-shadow: 0 6px 30px rgba(0, 0, 0, 0.35);
      }
      .w.key { color: #22d3ee; }
      #cap-card .w.key { color: #a5f3fc; }

      /* phone */
      #phone-layer { opacity: 0; }
      #phone {
        position: absolute; $phone
        border-radius: ${radius}px; padding: 13px;
        background: linear-gradient(145deg, #3a3e48, #1b1d22 42%, #0f1116);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 60px 120px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.25);
        transform-origin: $origin_type;
      }
      #screen { position: relative; width: 100%; height: 100%; border-radius: calc(${radius}px - 13px); overflow: hidden; background: #f3f6f7; }
      #ui { position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 0%; }

      /* counter */
      #counter {
        position: absolute; $counter
        width: 250px; height: 170px; border-radius: 36px; background: #0e7490;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.25);
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        transform: scale($counter_scale); transform-origin: 50% 50%;
      }
      #counter-inner { display: flex; flex-direction: column; align-items: center; }
      #counter-label { color: rgba(255, 255, 255, 0.82); font-weight: 600; font-size: 30px; letter-spacing: 0.14em; }
      #count { color: #fff; font-weight: 700; font-size: 104px; line-height: 1; letter-spacing: -0.04em; font-variant-numeric: tabular-nums; }

      /* end card */
      #card { opacity: 0; background: radial-gradient(ellipse 90% 60% at 30% 20%, rgba(34, 211, 238, 0.18), rgba(0, 0, 0, 0) 60%), linear-gradient(160deg, #164e63 0%, #0e7490 100%); }
      #logo {
        position: absolute; left: 50%; top: ${card_logo_top}px; width: ${card_logo}px; height: ${card_logo}px; margin-left: calc(${card_logo}px / -2);
        /* G4 logo: white circle with its own shadow baked into the png */
      }
      #url { position: absolute; left: 0; right: 0; top: ${card_url_top}px; text-align: center; color: #fff; opacity: 0; }
      #url .small { display: block; font-family: "Inter"; font-weight: 600; font-size: calc(${card_url_fs}px * 0.62); color: rgba(255, 255, 255, 0.8); letter-spacing: 0.02em; margin-bottom: 10px; }
      #url .big { display: block; font-family: "Montserrat"; font-weight: 700; font-size: ${card_url_fs}px; letter-spacing: -0.01em; }
      #next {
        position: absolute; left: 0; right: 0; top: ${card_next_top}px; text-align: center; opacity: 0;
        font-family: "Inter"; font-weight: 600; font-size: ${card_next_fs}px; color: rgba(255, 255, 255, 0.78);
      }
      /* Y / N keys */
      .key-cap {
        position: absolute; width: ${key}px; height: ${key}px; border-radius: 30px; opacity: 0;
        background: linear-gradient(180deg, #ffffff 0%, #e6ecef 100%);
        box-shadow: 0 10px 0 #9fb3bb, 0 26px 50px rgba(0, 0, 0, 0.45);
        display: flex; align-items: center; justify-content: center;
        font-family: "Inter"; font-weight: 700; font-size: calc(${key}px * 0.52); color: #0e7490;
      }
      #keyY { $keyY }
      #keyN { $keyN }
      #flash { background: #fff; opacity: 0; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="$DUR" data-width="$W" data-height="$H">
      <div class="layer" id="bg"></div>

      <video id="h6" class="clip full" src="assets/h6.mp4" muted playsinline data-start="$H6_START" data-duration="$H6_DUR" data-track-index="0"></video>
      <div class="layer" id="shade"></div>

      <div class="layer" id="phone-layer">
        <div id="phone" data-layout-allow-overflow>
          <div id="screen">
$INTRO
            <video id="ui" class="clip" src="assets/$UI_FILE" muted playsinline data-start="$UI_START" data-duration="$UI_DUR" data-track-index="1"></video>
          </div>
        </div>
        <div id="counter">
          <div id="counter-inner">
            <div id="counter-label">INBOX</div>
            <div id="count">40</div>
          </div>
        </div>
        <div class="key-cap" id="keyY">Y</div>
        <div class="key-cap" id="keyN">N</div>
        <div class="caps" id="cap-ui">
$UI
        </div>
      </div>

      <div class="caps" id="cap-full">
$FULL
      </div>

      <div class="layer" id="card">
        <img id="logo" src="assets/logo.png" alt="" />
        <div class="caps" id="cap-card">
$CARD
        </div>
        <div id="url"><span class="small">Start free at</span><span class="big">whatsnextaction.com</span></div>
        <div id="next">$NEXT</div>
      </div>

      <div class="layer" id="flash"></div>

      <audio id="vo" src="assets/vo.wav" data-start="0" data-duration="$DUR" data-track-index="2" data-volume="1"></audio>
      <audio id="music" src="assets/music.wav" data-start="0" data-duration="$DUR" data-track-index="3" data-volume="0.2"></audio>
    </div>
    <script>
      const T = $TIMING;
      const tl = gsap.timeline({ paused: true });
      const flash = (t) => tl.fromTo("#flash", { opacity: 0 }, { opacity: 0.85, duration: 0.06, ease: "none", yoyo: true, repeat: 1, immediateRender: false }, t - 0.06);

$SCRIPT

      // word-by-word captions: pop in on the voice, cut out at phrase end
      Object.keys(T).forEach((id) => {
        const els = document.querySelectorAll("#" + id + " .w");
        T[id].s.forEach((t, i) => {
          tl.fromTo(els[i], { opacity: 0, y: 36, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.16, ease: "back.out(2.2)" }, t);
        });
        if (T[id].e < $DUR) tl.set(els, { opacity: 0 }, T[id].e);
      });

      tl.set({}, {}, $DUR);
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
