# Ikone G4 (WhatsNextAction)

Generator `wna-icons.html` z logotipom G4 ("wn" + puščica; geometrija iz `../logo/logo-G4.svg`). Na teal ozadju je logotip obrnjen (bel krog, teal črke, puščica #0891b2), enako kot `../og-image`. Pisave prek povezave `fonts` → `../og-image/fonts`.

| Datoteka | Za kaj |
|---|---|
| `wna-avatar-G4-1024.png` | profilna slika YouTube, TikTok, Instagram, X (platforme obrežejo v krog) |
| `wna-youtube-banner-G4-2560x1440.png` | YouTube banner (vse v varnem območju 1546 × 423) |
| `wna-watermark-G4-150.png` | YouTube video watermark (prosojni robovi) |
| `wna-intro-G4-1080.png` | kvadratna predstavitvena slika |
| `wna-logo-card-G4-512.png` | logotip na zaključni kartici videov (HyperFrames `assets/logo.png`, od Clarify naprej) |

Ponoven izris (iz te mape; watermark se izriše v 600 in pomanjša):
```
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
r(){ "$C" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --default-background-color=00000000 \
  --window-size=$2,$3 --virtual-time-budget=3000 --allow-file-access-from-files --screenshot=$4 "file://$PWD/wna-icons.html?kind=$1&w=$2&h=$3"; }
r avatar 1024 1024 wna-avatar-G4-1024.png
r watermark 600 600 wm600.png && ffmpeg -y -i wm600.png -vf scale=150:150:flags=lanczos wna-watermark-G4-150.png && rm wm600.png
r card 512 512 wna-logo-card-G4-512.png
r banner 2560 1440 wna-youtube-banner-G4-2560x1440.png
r intro 1080 1080 wna-intro-G4-1080.png
```
Stare datoteke s strelo (`../wna-avatar-1024.png` …) ostanejo kot arhiv.

Dodatno: `wna-logo-wide-G4-1460x300.png` (ležeč logotip za svetla ozadja, prosojen: Stripe *Logo*, Paywiser). Izris: `r wide 1600 300 wide.png`, nato `ffmpeg -i wide.png -vf crop=1460:300:0:0 wna-logo-wide-G4-1460x300.png`.

## Kam kaj (zamenjava ikon, okt 2026)
| Mesto | Datoteka |
|---|---|
| Gravatar | `wna-avatar-G4-1024.png` |
| Stripe → Settings → Branding: *Icon* | `wna-avatar-G4-1024.png` (kvadrat, < 512 KB) |
| Stripe → Settings → Branding: *Logo* | `wna-logo-wide-G4-1460x300.png` |
| Stripe: *Brand color* / *Accent color* | `#0e7490` / `#22d3ee` |
| Paywiser → Brands: *Brand logo* | `wna-logo-wide-G4-1000x205.png` (Paywiser sprejme največ 1000 × 1000; izris: `ffmpeg -i wna-logo-wide-G4-1460x300.png -vf scale=1000:-1:flags=lanczos wna-logo-wide-G4-1000x205.png`) |
