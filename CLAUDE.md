# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Marketing — QubForge · WhatsNextAction · Vladimir Hozjan

Ta mapa je marketinški projekt Vladimirja Hozjana (CEO in ustanovitelj QubForge d.o.o., Maribor). Claude tu dela kot marketinški sodelavec, ki izdela vso vsebino; objavlja vedno Vladimir. Do 15. 9. 2026 je delo teklo v Cowork seji; ta datoteka je prenos konteksta.

## Kako delava
- Pogovor v slovenščini. Vsa objavljena vsebina (objave, videi, maili, biografije) **samo v angleščini**. Interni dokumenti v tej mapi v slovenščini.
- Vladimir odloča, Claude predlaga. V dokumentih označuj: ✅ odločeno (Vladimir) · 📝 predlog Claude · ⬜ odprto. Nikoli ne prikazuj predloga kot odločitve.
- Eno po eno. Ko Vladimir reče "ne dodajaj nič novega", povzemi samo to, kar je on rekel.
- Pisanje za Vladimirja: **brez pomišljajev** (nobenih —), brez podpisa pod LinkedIn objavo, brez samohvale, brez ponavljanja življenjepisa v objavah, brez besed "AI-powered", "revolutionary", "GTD app" kot ime produkta. GTD je registrirana znamka: "built around the GTD methodology".
- Datoteke: vse md. V mapi `personal/objave/` je za vsako objavo natanko ena datoteka (brez različic in COPY kopij). Ko urejaš datoteko, ki jo ima Vladimir odprto, mu povej, naj jo v urejevalniku znova naloži.
- Claude nikoli ne klikne "objavi", ne pošilja mailov in ne odpira računov. Prenos datotek s spleta samo z dovoljenjem (Higgsfield: dovoljenje dano).

## Strategija (odločeno)
- Trije ločeni plani: `personal/marketing-plan.md`, `qubforge/marketing-plan.md`, `whatsnextaction/marketing-plan.md`. Skupno zaporedje: `launch-sequence.md`. Koledar: `koledar-objav.md` (do 31. 12. 2026). Analiza: `analiza-strategije-2026-09-09.md`. Checklista: `checklist.md`.
- **WNA**: samo socialni marketing, brez plačanih oglasov. Platforme: YouTube Shorts, TikTok, Instagram Reels, LinkedIn. X ne. Reddit ne (✅ Vladimir, 9. 10.: r/gtd so GTD veterani, promocija se briše, zahteva preveč časa; ponovno pretehtati pri reviziji 7. 12.). Product Hunt samo ob native zagonu.
- **Ciljna skupina WNA**: ljudje, ki GTD **ne poznajo**. Personi A "preobremenjena strokovnjakinja 32–45" in B "ambiciozni mladi profesionalec 22–30" enakovredno; C vodja ekipe (Team) kasneje. GTD veterani namenoma ne. V videih ne vodimo z "GTD", ampak z bolečino; žargon prevajamo v vsakdanji jezik.
- **Pozicioniranje**: "a system you can trust", mir namesto produktivnosti. Tri jedrna sporočila: 1 vse iz glave, 2 vsaka stvar ima naslednji korak, 3 sistem, ne disciplina. Vsak video nosi natanko eno.
- **Tagline**: vodilni *Know your next action.*; izmenično *Get it out of your head.* in *Stress-Free Productivity. With a system you can trust.*
- **Ritem**: WNA en video vsak petek, nabor platform zožan po personi (A → LinkedIn + IG; B → TikTok + Shorts + IG; oba → vse štiri). "What's new" kratka besedilna objava pon/tor samo ob izidu. Personal in QubForge mesečno ob torkih ob 8:30 (✅ 9. 10., prej ponedeljek), QubForge 14 dni za personal. Personal nikoli ne prodaja WNA; QubForge govori o podjetju; WNA o uporabniku.
- **Zagon WNA**: prvotno 21. 9., zamaknjen zaradi Pro nakupa. Beta mail + registracija čet 8. 10. ✅ poslano; video "It's out" + QubForge objava + deljenje pet 9. 10. Prvotno zaporedje: zjutraj beta mail (~15 beta uporabnikov, darilo Pro/Team za 1 leto) → video "It's out" na vseh štirih → QubForge objava → Vladimir deli. Native aplikacije nov–dec 2026 = drugi zagon; Product Hunt takrat ali začetek januarja.
- **Produkcija videov**: Higgsfield AI za prizore (animirano 3D, ne realistično; oseba: moški ~40, srednji management, referenca `whatsnextaction/video/higgsfield/3d/H2b-3d-2.png`), pravi UI aplikacije nosi vsaj polovico videa, glas **Julian** (ElevenLabs preset prek Higgsfield `text2speech_v2`, variant elevenlabs, voice_id `95429266-c0ac-4137-a209-63b8812b0f23`; vsak stavek posebej, preverjen z Whisper). **Vladimirov glas odpade** (24. 9.: posnetek zveni kot telefon, angleščina ni dovolj dobra), tudi klon. Montaža ✅ (Vladimir, 12. 10.) v **HyperFrames** (HeyGen, odprtokodno, HTML → mp4; skills v `~/.claude/skills/hyperframes*`; vzorčni projekt `whatsnextaction/video/hf-capture-test/`): UI v okvirju iPhona, približki, napisi beseda za besedo, števci, prehodi. Prejšnja ffmpeg pot (`whatsnextaction/video/src/build.py` + `gfx.py`) ostane rezerva. Tedenski cikel: pon scenarij → tor potrditev → sre video → čet glas in montaža → pet objava. Oznaka AI ✅ (Vladimir, 9. 10.): samo Instagram (realističen AI glas Julian; Meta izrecno zahteva); TikTok in YouTube brez, dokler so prizori animirani in glas ne posnema resnične osebe; pri realističnih prizorih povsod. Samodejni podnapisi ✅ nikjer, ker ima vsak video ključne stavke kot napis na zaslonu; LinkedIn nima oznake.
- Vsebina videov: `whatsnextaction/feature-list.md` (funkcije, paketi, hooki, vrstni red). Napotki za račune: `whatsnextaction/social-guidelines.md`.

## Kontekst
- Vladimir: 25+ let, DSP doktorat, Iskratel, Inova IT, NiceHash CTO 2018–2024 in CEO 2024–jul 2025. LinkedIn linkedin.com/in/vladimir-hozjan, ~914 sledilcev, večinoma iz NiceHash/kripto sfere. Prva objava #1 "Became an entrepreneur" objavljena tor 15. 9. 2026.
- QubForge: qubforge.com (React/Vite), logotip = izometrična kocka z repom Q, gradient #00D4FF → #8B5CF6, ozadje #0A0E1A, Inter. OG oznake in og-image urejeni.
- WNA: whatsnextaction.com, mobile-first web app, GTD; Free / Pro 9 € / Team 14 €; logotip blisk na teal gradientu (#164e63 → #0e7490), Montserrat. Specifikacije in roadmap v `~/Documents/wna_orchestration` (`roadmap.md`, `specs/features/wna-features.md`, `contracts/limits.md`). Email to Inbox uporablja catch-all na whatsnextaction.com.
- Zoho aliasi za račune: yt@, instagram@, tiktok@, x@ (neobjavljeni), hello@ javni.

## Struktura in konvencije datotek
- Git repozitorij (GitHub `vladimirhozjan/marketing`, od 20. 10. 2026) hrani **samo besedilo, kodo in blagovno znamko** (✅ Vladimir, 20. 10.): vsi mediji (`*.mp4/.mov/.wav/.mp3/.png/.jpg`) in mape `raw/`, `higgsfield/`, `assets/`, `renders/`, `snapshots/` so v `.gitignore`; izjema so slike v `whatsnextaction/brand/` in `qubforge/og-image.png`. Mediji, tudi končni videi, ostanejo samo na disku (objavljeni so na omrežjih). Nove medijske datoteke ne dodajaj v git. Ni build sistema; vse je md + trije HTML/canvas generatorji v `qubforge/video/src/`. Mapa `.idea/` je JetBrains, ignoriraj.
- Objave: `personal/objave/YYYY-MM-DD-objava-<kanal>.md`. Glava z alinejami (Kanal, Datum, Vizual, Status), nato `---` in končno angleško besedilo. Za QubForge in WNA objave enaka oblika v `qubforge/objave/` oz. `whatsnextaction/objave/` (mapi še ne obstajata).
- Vsak razdelek v planih nosi oznako ✅/📝/⬜ v naslovu; pri urejanju oznake ohrani in jih ne spreminjaj brez Vladimirjeve odločitve.
- `checklist.md` je edini "stanje danes" dokument: ob vsakem opravilu ga posodobi (datum v naslovu).
- Končni videi ležijo v `qubforge/video/` (npr. `qubforge-logo-sting-1x1.mp4`, `-9x16.mp4`); vmesne mape `frames_WxH/` v `src/` so izhod renderja in se lahko brišejo.

## Orodja v tej mapi (`qubforge/video/src/`)
Zahteve: `pip install playwright numpy && playwright install chromium`, `brew install ffmpeg`. Vse ukaze zaganjaj iz `qubforge/video/src/`.

- **Logo sting (video)**: `logo-sting-source.html` riše kadre na canvas, `render.py` jih s Playwrightom zajame in z ffmpeg zlepi (libx264, crf 17).
  ```
  python3 render.py <w> <h> <fps> <dur_s> <out.mp4> [preview|no] ["&param=..."]
  python3 render.py 1080 1920 30 5 sting-9x16.mp4 no "&rot=4.2&text=1.9&dir=-1"   # 9:16
  python3 render.py 1080 1080 30 5 sting-1x1.mp4  no "&rot=4.2&text=1.9&dir=-1"   # 1:1
  python3 render.py 1080 1920 30 5 x.mp4 preview   # samo 4 kontrolna kadra v frames_1080x1920/
  ffmpeg -i sting-9x16.mp4 -i higgsfield-audio-5s.wav -c:v copy -c:a aac -shortest final.mp4
  ```
  Parametri v query stringu: `rot` (trajanje enega obrata, privzeto = dur), `text` (sekunda, ko pride napis, privzeto 1.1), `dir` (1/-1 smer vrtenja), `axis`, `v` (varianta napisa, privzeto `qubforge`). Privzeti `dur` v HTML je 8 s; potrjena končna verzija je 5 s z zgornjimi parametri.
- **Zvok**: `higgsfield-audio-5s.wav` je uporabljen (Higgsfield). `audio.py <dur> <out.wav>` je lastni deterministični generator (numpy) → `sting-audio.wav`; ohranjen kot rezerva.
- **Slike (brez render.py)**: `cover-source.html` in `wna-assets.html` sta statična canvasa. Odpri v Chromiumu z ustreznimi query parametri in shrani `#c` (Playwright: počakaj `window.FONTS_READY` pri cover oz. `window.READY` pri wna-assets, nato `screenshot` elementa).
  - `cover-source.html?cover=1&w=&h=&logo=&cx=&cy=`: LinkedIn naslovnica / OG slika QubForge (logo levo, napis "QubForge · Forging intelligent software solutions · qubforge.com" desno). Brez `cover=1` je isti kader kot sting.
  - `wna-assets.html?kind=avatar|banner|square&w=&h=`: avatar 1024×1024, YouTube banner 2560×1440 (varno območje 1546×423 sredinsko), square 1080×1080. Izhodi so že narejeni v `whatsnextaction/brand/` (`wna-avatar-1024.png`, `wna-youtube-banner-2560x1440.png`, `wna-intro-1080.png`); nanje se sklicuje `whatsnextaction/social-guidelines.md`.
- Pisave: samo Inter TTF v `fonts/inter/extras/ttf/` (Regular, Medium, SemiBold, Bold); HTML jih nalaga relativno, zato generatorjev ne premikaj iz `src/`.

## Odprto (15. 9. 2026)
- Je Pro nakup v produkciji živ? (odloči CTA v zagonskem videu)
- Datum native aplikacij.
- YouTube kanal odprt 16. 9. (youtube.com/@WhatsNextAction). Računa TikTok/IG še nista odprta; glas še ni posnet; posnetki zaslona še niso narejeni.
