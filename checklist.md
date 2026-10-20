# Checklista (stanje: torek 20. 10. 2026)

## Danes, tor 20. 10.
- [x] Personal #2 v2 ✅ (Vladimir, 20. 10.), 2.985 znakov; sre 21. 10. še en pregled
- [x] LinkedIn Capture: podnapisi odstranjeni (Vladimir, 20. 10.; meni ⋯ → Edit captions → Remove captions)
- [x] What's new ta teden ne (Vladimir): Google Calendar Sync in BYOS Google Drive naslednji teden kot **dve objavi**; 📝 Calendar Sync pon 26. 10., BYOS ✅ zamaknjen za teden → 📝 pon 2. 11.
- [x] Ikone G4 (Claude): `whatsnextaction/brand/icons/` (avatar, YouTube banner, watermark, intro, logotip kartice); Clarify kartica že z G4
- [ ] **Ta teden, Vladimir: zamenjava ikon** na YouTube (slika, banner, watermark), TikTok, Instagram, X; backend in frontend že urejena (Vladimir), Zoho ni potrebe; Vladimir preveri Gravatar, Stripe in Paywiser
- [x] Scenarij WNA #3 Next Actions + Today 📝: `whatsnextaction/objave/2026-10-29-video-next-today.md` (~19 s, pravi UI 60 %, H7 hook "20 next steps. Where do you start?", 9:16 + 1:1); ⬜ potrditev do pon 26. 10.; UI posnetki sre 28. 10.

## Danes, pon 19. 10.
- [x] Scenarij #2 Clarify 📝: `whatsnextaction/objave/2026-10-23-video-clarify.md` (~20 s, pravi UI 66 %, hook "40 things. Now what?" nadaljuje Capture, en 3D prizor H6, Inbox Zero kot olajšanje; samo 9:16 za YT, TikTok, IG)
- [x] Številke Capture dan 3 → `whatsnextaction/marketing-plan.md` pogl. 11 (prek Chrome):
  - TikTok 232 (povp. **1,78 s**, odhod pri 0:01) · YouTube 65 (povp. 0:53, vrtijo ga; +1 naročnik) · Instagram 40 (prej 7)
  - LinkedIn QF 1 reakcija, stran 21 sledilcev · ⚠️ samodejni podnapisi na LinkedInu spet vklopljeni (izklopi: *Edit captions*)
  - Admin: 24 uporabnikov (+2 od 12. 10.), DAU 1
- [x] Higgsfield H6: ✅ izbran H6-3 (Vladimir); videa v izdelavi → ti izbereš
- [x] ✅ WNA #3 Next Actions + Today: **čet 29. 10.** namesto pet 30. 10. (koledar popravljen)
- [x] ✅ TikTok dobi svojo različico hooka (pravi UI od kadra 0), YT in IG potrjeno (A/B test)
- [x] Scenarij Clarify ✅ potrjen (Vladimir, pon 19. 10.), vse štiri točke

## Danes, pet 16. 10.: Capture izdelan
- [x] UI posnetki `capture-01/02/03` v `whatsnextaction/video/raw/` (Vladimir, 12:52–13:00)
- [x] Julian: 7 stavkov + rezerve R1–R3 v `whatsnextaction/video/capture/julian/`, vsi dobesedno potrjeni z Whisper
- [x] Montaža HyperFrames: `whatsnextaction/video/wna-capture-9x16.mp4`, `wna-capture-1x1.mp4` (19,8 s, −14 LUFS), sličica `wna-capture-thumbnail-1x1.jpg`; projekt `video/wna-capture/` (`build.py` + `template.html.tpl` izdela 9:16 in 1:1)
- [x] Vladimir: pregled videov ✅ potrjen ("boljše kot prejšnjič")
- [x] **Objava #1 Capture pet 16. 10. popoldne** na vseh štirih (TikTok: Your brand ✅; IG: AI label)
  - [x] YouTube https://www.youtube.com/shorts/5KG95jjlsEk
  - [x] TikTok https://www.tiktok.com/@whatsnextaction/video/7697234880144395542
  - [x] Instagram https://www.instagram.com/p/Dejf17nKGVj/
  - [x] LinkedIn QubForge https://www.linkedin.com/posts/qubforge_40-things-in-your-head-get-them-out-in-two-activity-7516833496145960960-MDOt (naslov "40 things in your head? Get them out in two minutes.")

## Pon 12. 10.: Capture v produkciji
- [x] Scenarij #1 Capture ✅ potrjen: `whatsnextaction/objave/2026-10-16-video-capture.md` (~19 s, naracija ~15,7 s, pravi UI 52 %, hook "40 things in your head?" od kadra 0; opisi za YT, TikTok, IG in LinkedIn QF v datoteki)
- [x] Glasba ✅ `whatsnextaction/video/raw/One Last Click.wav` (Suno, chill techno brez basa in kitare; podlaga "It's out" zavrnjena); sprostitev pri 27,55 s pesmi poravnana na 11,5 s videa, video začne pri 16,05 s pesmi
- [x] Higgsfield prizori ✅: ključna kadra H4-3d-2 (vrtinec listkov) in H5-3d-2 (olajšanje); videa **H4-video-1** in **H5-video-2** v `whatsnextaction/video/higgsfield/3d/` (~38 kreditov)
- [x] Številke dan 3 → `whatsnextaction/marketing-plan.md`, konec pogl. 11:
  - TikTok 254 (povp. 6,6 s, do konca 0,8 %, še vedno odhod pri 0:01) · YouTube 56 (0 v zadnjih 48 h) · Instagram 7
  - LinkedIn osebno 363 prikazov / 9 reakcij · QubForge 3 / 1 repost, stran 20 sledilcev
  - Admin: 22 uporabnikov, **0 novih registracij od petka**, DAU 2
  - Ugotovitev: zagonski val izzvenel; video ni prinesel nobenega uporabnika → krajši video, hook v prvem kadru, krajša pot do registracije
- [x] HyperFrames (HeyGen, odprtokodno, Apache-2.0, brezplačno, izris lokalno) nameščen: skills v `~/.claude/skills/hyperframes*`, testna scena `whatsnextaction/video/hf-capture-test-9x16.mp4` (7,5 s, izris 11 s), projekt `whatsnextaction/video/hf-capture-test/` kot vzor

## Odločitve ✅ (Vladimir, pet 16. 10.)
- Video Capture potrjen; HyperFrames predloga `video/wna-capture/` je vzor za naslednje videe
- TikTok: *Your brand* obkljukano pri vsakem videu; YouTube: občinstvo "ni za otroke" (zapisano v `social-guidelines.md`)

## Odločitve ✅ (Vladimir, 12. 10.)
- Scenarij Capture potrjen, vključno s hookom H4 in napovedjo "Next Friday" na zaključni kartici
- Glasba: chill techno, zelo moderno, brez basa in kitare → "One Last Click"
- Prizora: H4-video-1, H5-video-2
- Montaža odslej v **HyperFrames** (lepši gradienti in prehodi), začenši s Capture; ffmpeg pot ostane rezerva

## Naslednje
### Ti
- [x] ~~Sre 14. 10.~~ pet 16. 10.: UI posnetki za Capture v `whatsnextaction/video/raw/`: najprej 24 vnosov v demo račun, nato `capture-01-quickadd`, `capture-02-anywhere`, `capture-03-inbox40` (navodila v scenariju, "Snemanje UI")
- [x] **Pet 16. 10. popoldne (namesto 9:00): objava #1 Capture** (YT, TikTok, IG, LinkedIn QF); oznaka AI samo IG, samodejni podnapisi nikjer
- [ ] Odgovori na komentarje in maile beta uporabnikov; kdor omeni ekipo → Team v adminu
- [x] ~~Tor 20. 10.~~ pon 19. 10.: potrditev scenarija Clarify ✅
- [ ] **Čet 22. 10.: UI posnetki Clarify** (`clarify-01/02/03`, navodila v scenariju); montažo naredim isti dan
- [ ] Pet 23. 10.: objava #2 Clarify (YT, TikTok, IG)
- [ ] Do pet 23. 10. (ne tor 20. 10., Vladimir): posnetka za personal #2 (zaslon 4 terminali 2 × 2 + kamera, 2–3 min) v `personal/video/raw/`
- [x] Intervju za personal #2 opravljen pon 19. 10. (namesto 26. 10.)
- [x] Osnutek v1 personal #2 potrjen pon 19. 10. (Vladimir)
- [ ] Vladimir: podrobni popravki besedila v1 (bere se skokovito), nato gladilni prehod
- [ ] **Tor 27. 10. 8:30: objava personal #2**

### Jaz
- [x] ~~Čet 15. 10.~~ pet 16. 10.: Julian (7 stavkov + rezerve, preverjeno z Whisper), montaža Capture v HyperFrames 9:16 in 1:1 z "One Last Click" (okvir iPhona, približki, napisi beseda za besedo, pravi števec 24 → 40, −14 LUFS), sličica `wna-capture-thumbnail-1x1.jpg`; oba videa tebi v čet popoldne
- [x] Pon 19. 10.: scenarij #2 Clarify (objava pet 23. 10.)
- [x] Pon 19. 10.: številke Capture dan 3
- [x] Pon 19. 10.: Higgsfield H6 ✅ H6-video-2 (Vladimir); kartica ✅ "Next week: what to do right now."
- [x] Pon 19. 10.: Julian (8 stavkov, Whisper ✅), glasba, predloga Clarify obe različici (`video/wna-clarify/`, `wna-clarify-tiktok/`) z Y/N tipkama, H6 in kartico; v četrtek manjkajo samo UI posnetki
- [ ] Čet 22. 10.: montaža Clarify YT/IG + TikTok različica, naslovnica → tebi isti dan
- [ ] Do pon 26. 10.: montaža vizuala personal #2 (1:1 timelapse, kamera spodaj desno, brez zvoka)
- [x] Pon 19. 10.: zgodba personal #2 zapisana (Vladimir) + osnutek v0 📝 + 9 dopolnilnih vprašanj
- [x] Pon 19. 10.: osnutek v1 personal #2 iz intervjuja, 2.762 znakov (`personal/objave/2026-10-27-objava-linkedin.md`)

## Odprto, ni nujno
- [ ] Produkt: kratek URL `/start`, prvi zaslon strani za novince (po dnevu 3 bolj pomembno: 0 registracij iz videa)
- [ ] Merjenje: UTM + "kje si slišal za nas" ob registraciji (admin izvora registracij ne prikazuje)
- [ ] YouTube telefonsko preverjanje: 9. 10. SMS na 040 286 764 ne pride; poskusi z glasovnim klicem ali drugo številko (brez tega povezava v opisu ni klikljiva)
- [ ] TikTok 2FA: 18. 9. zavrnjeno (nov račun); poskusi znova
- [ ] www.whatsnextaction.com: TLS certifikat
- [x] Personal #3 (tor 24. 11.): "A day with my team of agents" ✅ (Vladimir, 19. 10.), nadaljevanje #2
- [ ] Datum native aplikacij → Product Hunt

## Narejeno
- [x] Tor 13. 10.: Stripe preverjen (ni novih nakupov Pro); LinkedIn QubForge "It's out" samodejni podnapisi urejeni; Instagram Reel auto captions izklopljeni in Reel deljen v Story
- [x] **Pet 9. 10.: zagon WNA.** Beta mail + registracija čet 8. 10. (darilo Pro/Team 1 leto, Pro nakup preverjen). Video "It's out": YouTube https://youtube.com/shorts/M44Vqth8NWs · TikTok https://www.tiktok.com/@whatsnextaction/video/7694578854131698966 · Instagram https://www.instagram.com/p/DeRFOxcKidy/ · QubForge #1 https://www.linkedin.com/posts/qubforge_whatsnextaction-productivity-startup-activity-7514242821130993666-FnAK · Vladimir delil z "First product out. If you keep everything in your head, this one is for you."
- [x] Odločitve 9. 10.: ves koledar zamaknjen za dva tedna; LinkedIn ob torkih 8:30; oznaka AI samo Instagram; samodejni podnapisi nikjer; Reddit ne (revizija 7. 12.); personal #2 "Building my first product in the AI era"
- [x] Marketinški plani (WNA, personal, QubForge), launch-sequence, koledar objav, analiza, social-guidelines
- [x] QubForge logo sting (1:1 in 9:16), og-image in OG oznake na qubforge.com
- [x] LinkedIn profil urejen; **personal #1 "Became an entrepreneur"** tor 15. 9. (12. 10.: 1.497 prikazov, 49 reakcij, 12 komentarjev)
- [x] Računi: YouTube, Instagram, TikTok (Verified Business), X (samo rezervacija)
- [x] Glas Julian (ElevenLabs prek Higgsfielda); video "It's out" 9:16 in 1:1
