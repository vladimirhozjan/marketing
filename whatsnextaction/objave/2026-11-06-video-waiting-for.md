# WNA · Video #4 Waiting For

- Kanal: persona A (koledar) → **Instagram Reels (9:16)** in **LinkedIn QubForge (1:1)**; ✅ pet 6. 11. (Vladimir) dodana še **TikTok** in **YouTube Shorts** zaradi dosega (#3: TikTok 786 ogledov).
- Datum: **pet 6. 11. 2026**; LinkedIn QF 9:00–10:00, Instagram 17:00–18:00 (ritem ✅ 23. 10.).
- Cikel: pon 2. 11. scenarij (jaz) → **tor 3. 11. potrditev (ti)** → tor Higgsfield H8, Julian, glasba, predloga brez UI (jaz) → **sre 4. 11. UI posnetki (ti)**, montaža isti dan (jaz) → čet 5. 11. pregled (ti) → pet 6. 11. objava (ti).
- Vizual: 📝 en 3D prizor za hook (H8), nato pravi UI čez dobro polovico videa (dodajanje v Waiting For, seznam z imeni, podrobnosti "koliko časa", Got it), zaključna kartica.
- Sporočilo: 3 "sistem, ne disciplina" → tagline *Stress-Free Productivity. With a system you can trust.*; hook iz koledarja *"Waiting on someone? Park it. Forget it. The app remembers."*
- Dolžina: 📝 okoli 21 s (naracija ~14 s)
- Status: ✅ scenarij potrjen (Vladimir, pon 2. 11.), hook "Three people" · Julian, glasba, predloga brez UI narejeni pon 2. 11. (dan prej)

Pravila: brez "GTD" v govoru; brez "AI-powered"; brez pomišljajev; vsak stavek naracije ima napis na zaslonu; oznaka AI ✅ samo Instagram; samodejni podnapisi nikjer (LinkedIn: ob nalaganju izklopi, sicer ⋯ → Edit captions → Remove captions); brez primerjave z drugimi aplikacijami. Mirna verzija UI ✅ (od Clarify): brez tipk, bliskov in približkov, UI 1,5–2×, rezi samo na mirujočih zaslonih.

## Nit s #3 📝

Kartica #3 je napovedala *"Next week: waiting on someone?"*. #3 je skrajšal seznam na danes; #4 vzame iz glave še zadnjo stvar, ki jo nosimo s sabo: kdo nam kaj dolguje. Persona A to pozna iz službe in doma hkrati (sodelavec, banka, mojster). Kdor ni videl prejšnjih, dobi samostojen video.

## Kaj potrebujem od tebe

**Do tor 3. 11. (potrditev; brez nje ne začnem s prizorom)**
- [x] 1. ✅ Scenarij kot celota (Vladimir, 2. 11.).
- [x] 2. ✅ Hook "Three people owe you an answer…" (Vladimir, 2. 11.); bil je predlog: *"Three people owe you an answer. Can you name all three?"* ali R1 *"Waiting on someone? And keeping it in your head?"* (bližje napovedi s kartice #3).
- [x] 3. ✅ Hook prizor H8 (Vladimir, 2. 11.): ključni kader H8-3d-3, video H8-video-2.
- [ ] 4. Glasba: 📝 ista "One Last Click", drug izrez.
- [ ] 5. Napoved na kartici: 📝 *Next week: already out? Do what fits.* (#5 Context tags, pet 13. 11.)
- [x] 6. Demo račun pripravljen (Claude, 2. 11.; ponovno čet 5. 11., ker je bil račun 2. 11. popoldne ponastavljen): Waiting For od zgoraj *Feedback on the design* · Mark, od 1. 10. ("1mo") · *Confirmation of the transfer* · Bank, od 30. 10. · *Sales summary from Luka* · Luka · *Quote for the new cabinets* · Contractor. Next Actions ima 4 stvari. *Signed contract* ne obstaja.

**Sre 4. 11.: UI posnetki** v `whatsnextaction/video/raw/` (navodila spodaj)
- [x] 7. `wait-01-add`, `wait-02-list`, `wait-03-detail`, `wait-04-gotit` (Vladimir, čet 5. 11., 10:53–10:57). *Signed contract* se doda na dno seznama (ne na vrh), *Confirmation of the transfer* pride v Next Actions kot zadnja vrstica; podrobnosti kažejo "Mark · for 1 month".

**Montaža ✅ narejena (čet 5. 11.), ✅ pregled potrjen (Vladimir, čet 5. 11.)**
- `whatsnextaction/video/wna-waiting-for-9x16.mp4` (IG) in `wna-waiting-for-1x1.mp4` (LinkedIn QF), 22,0 s, −14 LUFS, Whisper potrdi celoten govor.
- Naslovnica `wna-waiting-for-cover-9x16.jpg` in sličica `wna-waiting-for-thumbnail-1x1.jpg` (kader "Park it.", 4,6 s).
- UI rez: `video/wna-waiting-for/cut_ui.py`; tipkanje skrajšano (posnetek se začne pri vpisu "Sarah"), med prizori pretopi 0,3 s; j2 "Park it." premaknjen na 3,85 s, da pade na tap Add.

**Pet 6. 11. (objavljaš ti)**
- [x] 8. Opisi po platformah (spodaj); objavljeno na vseh štirih (6.–7. 11.).

---

## Scenarij (naracija EN, kadri) 📝

| s | Kader | Naracija (Julian) | Napis na zaslonu |
|---|---|---|---|
| 0–2,8 | **H8** (3D): ista oseba za pisalno mizo v pisarni, pozno popoldne, prenosnik odprt (zaslon obrnjen stran). Nasloni se nazaj, pogled odtava v stran, kot da šteje v glavi, nato rahlo nelagoden pogled v kamero: "kdo je že bil?". Od kadra 0. | "Three people owe you an answer. Can you name all three?" | ***3 people owe you an answer. Can you name all three?*** |
| 2,8–5,6 | **Pravi UI** (`wait-01`, ~1,7×): stran **Waiting For**, obrazec: *Signed contract* + *Sarah* → Add; vrstica se pojavi na vrhu s čipom **Sarah** | "Park it." | ***Park it.*** |
| 5,6–8,0 | **Pravi UI** (`wait-02`): seznam Waiting For, štiri vrstice z imeni (Sarah, Contractor, Mark, Bank); miren kader, nič se ne premika | "Forget it." | ***Forget it.*** |
| 8,0–11,0 | **Pravi UI** (`wait-03`): tap na *Feedback on the design* → podrobnosti: **Waiting for Mark · 1mo**; počakaj na tem zaslonu | "The app remembers who. And for how long." | ***The app remembers who. And for how long.*** |
| 11,0–14,0 | **Pravi UI** (`wait-04`): *Confirmation of the transfer* → **Got it** → vrstica izgine iz Waiting For; (pretop) vrstica na vrhu Next Actions | "When it arrives, it's back on your list." | ***When it arrives, it's back on your list.*** |
| 14,0–21 | Zaključna kartica: logotip G4 na teal gradientu | "Stress-free productivity. With a system you can trust. Start free at whatsnextaction.com." | ***A system you can trust.*** → *whatsnextaction.com*; spodaj manjše: *Next week: already out? Do what fits.* |

**Delež pravega UI:** 2,8–14,0 s = 11,2 s od ~21 s (53 %). En 3D prizor.

**Dejstvo iz aplikacije (preverjeno v kodi, 2. 11.):** vrstica v seznamu Waiting For pokaže samo ime (čip), ne koliko časa; trajanje ("today", "3d", "1mo") je v podrobnostih akcije. Zato kader 8–11 s odpre podrobnosti.

**1:1 (LinkedIn QF):** ista časovnica, telefon manjši in na sredini, napisi zgoraj, kot pri #3 (`build.py` izdela obe razmerji).

### Merjenje naracije

Ocena po Julianovem tempu (izmerjeno na #1–#3):

| # | Stavek | s |
|---|---|---|
| 1 | Three people owe you an answer. Can you name all three? | 2,8 |
| 2 | Park it. | 0,7 |
| 3 | Forget it. | 0,8 |
| 4 | The app remembers who. And for how long. | 2,2 |
| 5 | When it arrives, it's back on your list. | 2,0 |
| 6 | Stress-free productivity. With a system you can trust. Start free at whatsnextaction.com. | 5,6 |
| | **Skupaj govor** | **14,1** |

**Rezerve:**
- R1 "Waiting on someone? And keeping it in your head?" (namesto 1)
- R2 "Not in your head. Here." (namesto 3, če bi "Forget it." zvenelo preveč brezbrižno)
- R3 "A month? Maybe it's time to ask." (dodatek po 4; pokaže, čemu trajanje služi, video +2 s)

### Zakaj tako (kratko)
- Bolečina persone A ni sama naloga, ampak spominjanje: kdo mi še dolguje odgovor. Vprašanje "Can you name all three?" gledalec preizkusi na sebi in redko uspe.
- "Park it. Forget it." sta kratka udarca na mirnih kadrih; olajšanje nosi to, da se na zaslonu nič ne zgodi.
- "1mo" pri Marku je edini trenutek, ko aplikacija pokaže nekaj, česar si sam ne bi zapomnil.
- Got it zaključi krog: čakanje ni slepa ulica, stvar se vrne na seznam.
- Sporočilo 3 (sistem, ne disciplina) dobi svoj tagline na kartici.

## Higgsfield prizor (izvedem jaz prek MCP)

Slog ✅ kot #1–#3: stilizirano 3D, teal v senci, jantarna v lučeh, brez berljivega besedila, zaslon obrnjen stran. Oseba ✅ ista, referenca `video/higgsfield/3d/H2b-3d-2.png`.

Postopek kot pri H7: ključni kader (`gpt_image_2_5`, 9:16, referenca H2b-3d-2) 3 različice → izbereš → video (`kling3_0`, pro, 9:16, 5 s, brez zvoka, cfg 0,7) 2 različici → izbereš. Iz H7 naučeno: čim manj gibanja rok, nič ne pride iz naprav, brez pare in dima.

**Poziv (EN):**
- **H8 (0–2,8 s), hook:** *Stylized 3D animation look, soft clay-like materials, gentle global illumination, saturated teal in the shadows and warm amber late-afternoon light through an office window, not cartoonish. The same man as in the reference, about 40, mid-level manager in a business casual shirt, sits at his office desk with an open laptop whose screen faces away from the camera. He leans back in his chair, his eyes drift to the side as if counting something in his head, then he looks straight into the camera with a slightly uneasy "who was it again?" expression. Hands stay still on the armrests. Slow push-in toward his face. No smoke, no steam, nothing comes out of any device. No readable text.*

**Ključni kadri (pon 2. 11.)** v `video/higgsfield/3d/`: `H8-3d-1/2/3.png`, pregled `H8-pregled.jpg` (prvi na levi je referenca H2b; referenca na Higgsfield 9bfb9911). Job ID: abb2d006, ee44d31e, 4ffdefa8. H8-3d-1: naslonjen, pogled v stran, roke mirne · H8-3d-2: naslonjen, nelagoden pogled v kamero · H8-3d-3: roka na bradi, pogled gor. ⬜ izbira.

✅ izbran **H8-3d-3** (Vladimir, 2. 11.).

**Videi (pon 2. 11.)** (Kling 3.0 pro, 5 s, brez zvoka, 9:16, začetni kader H8-3d-3) v `video/higgsfield/3d/`, pregled `H8-video-pregled.jpg` (zgoraj 1, spodaj 2, kader na ~0,8 s):
- `H8-video-1.mp4` (51aeabfb): roka ves čas na bradi, pogled gor, nato počasi v kamero, zaskrbljen.
- `H8-video-2.mp4` (c9171646): pogled gor, spusti roko na mizo, konča z nelagodnim pogledom v kamero.
- ✅ izbran **H8-video-2** (Vladimir, 2. 11.), izrez 2,0–5,0 s → `video/wna-waiting-for/assets/h8.mp4`.

Rezerva, če H8 ne uspe: `H6-video-2.mp4` iz Clarify (pogled v kamero) z napisom čez.

**Strošek:** 3 ključni kadri × 0,25 + 2 videa × ~9 ≈ 19 kreditov.

## Snemanje UI (navodila za Vladimirja)

Nastavitve kot pri #1–#3: iPhone, snemanje zaslona iz Nadzornega centra, pokončno, mikrofon izklopljen, Do Not Disturb, svetla tema, English, demo račun. 1 s mirovanja na začetku in koncu vsakega posnetka. Tapaj mirno, med koraki pol sekunde premora; pospešim v montaži.

**Priprava demo računa (naredim jaz prek MCP po potrditvi, ni v kadru):** v Waiting For že sta *Feedback on the design* (Mark) in *Confirmation of the transfer* (Bank), oba od 24. 9. (podrobnosti kažejo "1mo"). Dodam *Quote for the new windows* (Contractor). *Signed contract* (Sarah) dodaš ti na posnetku 1. Next Actions ostane, kot je po #3 (17 stvari).

**Posnetek 1, `wait-01-add.MP4` (~10 s):** začni na **Engage**, končaj na Waiting For
1. Odpri **Waiting For**. Miruj 1 s.
2. Odpri obrazec za dodajanje. Naslov *Signed contract*, Waiting for *Sarah*, potrdi. Miruj 2 s, ko se vrstica pojavi.

**Posnetek 2, `wait-02-list.MP4` (~5 s):** začni in končaj na **Waiting For**
1. Seznam Waiting For s štirimi vrsticami, ne dotikaj se zaslona 4 s.

**Posnetek 3, `wait-03-detail.MP4` (~6 s):** začni in končaj na **Waiting For**
1. Tapni *Feedback on the design*. Na podrobnostih miruj 3 s (vidno "Mark" in "1mo").
2. Nazaj na seznam.

**Posnetek 4, `wait-04-gotit.MP4` (~10 s):** začni na **Waiting For**, končaj na Next Actions
1. Tapni *Confirmation of the transfer* → **Got it**. Miruj 1 s na seznamu brez nje.
2. Odpri **Next Actions**. Miruj 2 s (vrstica naj bo vidna na vrhu; če ni, jo poiščem v montaži ali uredim vrstni red prek MCP).

Po snemanju: demo račun pusti; za #5 Context tags dodam oznake prek MCP.

## Julian ✅ narejen (pon 2. 11.)

`video/waiting-for/julian/` (mp3 + wav 48 kHz), vsi dobesedno potrjeni z Whisper (large-v3-turbo). Dolžine: j1 3,04 · j2 0,88 · j3 0,72 · j4 2,80 · j5 2,40 · j6 7,20 s = 17,0 s govora (ocena 14,1; j6 je za 1,6 s daljši, ker Julian "whatsnextaction.com" izgovori počasi). Rezerve r1 2,64 · r2 1,68 · r3 2,56 s.

Odmiki v videu: j1 0,05 · j2 3,30 · j3 6,00 · j4 8,40 · j5 11,60 · j6 14,50 (konča 21,5). **Video je zato 22,0 s** (ocena ~21): H8 0–3,0 · UI 3,0–14,2 (wait-01 3,0–5,8 · wait-02 5,8–8,2 · wait-03 8,2–11,4 · wait-04 11,4–14,2) · kartica 14,2–22,0.

## Glasba 📝 `raw/One Last Click.wav` (ista kot #1–#3)

Sprostitev pesmi poravnam na kader "Forget it." (miren seznam, ~6 s videa).

📝 Sprememba (pon 2. 11.): pesem je dolga samo 39,8 s; če bi sprostitev (27,55 s pesmi) padla na "Forget it." pri 6,0 s, bi glasba utihnila pri 18,3 s, sredi kartice. Zato izrez od 17,8 s: sprostitev pade na **9,75 s, na podrobnosti "Mark · 1mo"** (trenutek, ko aplikacija pokaže nekaj, česar si sam ne bi zapomnil), glasba zveni do konca s pojemanjem. ⬜ potrditev

## Predloga ✅ narejena (pon 2. 11.), brez UI

`video/wna-waiting-for/` (9:16, IG) in `video/wna-waiting-for-1x1/` (LinkedIn QF); `build.py` izdela obe, `hyperframes check` brez napak. Poskusna rendra v `renders/`: časovnica, napisi beseda za besedo in kartica delujejo; namesto UI je siv nadomestek z imenom posnetka. Brez števca (ta je bil samo pri #3). Glasnost −17,3 LUFS → končni normaliziram na −14. V sre 4. 11. po posnetkih napišem `cut_ui.py` in zamenjam nadomestek.

## Objave po platformah (pet 6. 11., objavljaš ti) 📝

Vrstni red: 1 LinkedIn QubForge (9:00–10:00) → 2 Instagram Reels (17:00–18:00).

### 1 · LinkedIn QubForge (1:1) ✅ objavljeno pet 6. 11.: https://www.linkedin.com/posts/qubforge_park-it-forget-it-activity-7524374444711157760-qavR
- Besedilo:
```
Three people owe you an answer. A colleague, the bank, someone fixing your windows. Can you name all three without checking?

Most of us keep that list in our head, and it never stops running.

In WhatsNextAction you park it in Waiting For: what you are waiting for and from whom. The app remembers how long it has been. When it arrives, one tap and it is back on your list.

Stress-free productivity. With a system you can trust.

Start free: https://whatsnextaction.com

#WhatsNextAction #productivity #focus
```
- Nastavitve: sličica `wna-waiting-for-thumbnail-1x1.jpg` · samodejni podnapisi izklopi ob nalaganju · naslov videa "Park it. Forget it." · LinkedIn nima oznake AI.

### 2 · Instagram Reels (9:16) ✅ objavljeno sob 7. 11.: https://www.instagram.com/p/DfbrcM6KDKU/
- Opis:
```
Three people owe you an answer. Can you name all three?

Park it.
Forget it.
The app remembers who, and for how long.
When it arrives, it's back on your list.

Start free, link in bio.

#productivity #mentalload #focus #worklife #whatsnextaction
```
- Nastavitve: **AI label** vklopi · samodejni podnapisi izklopi · Cover: kader "Park it." · *Also share to Facebook* izklopi · glasbe ne dodajaj · po objavi deli v Story.

### 3 · YouTube Shorts (9:16) ✅ objavljeno sob 7. 11.: https://youtube.com/shorts/LzATV1bxRXU · dodano pet 6. 11. (✅ Vladimir: tudi TikTok in Shorts, zaradi dosega)
- Video `wna-waiting-for-9x16.mp4`, naslovnica `wna-waiting-for-cover-9x16.jpg`.
- Naslov:
```
Three people owe you an answer. Can you name them?
```
- Opis:
```
A colleague, the bank, someone who still owes you feedback. Most of us keep that list in our head. Park it in Waiting For: the app remembers who, and for how long. When it arrives, it's back on your list.

Start free: https://whatsnextaction.com

Built around the GTD methodology, made for people who have never heard of it. A new short every week, one feature at a time.

#productivity #mentalload #focus #worklife #whatsnextaction
```
- Nastavitve: *Uporaba umetne inteligence* **Ne** · Audience: **No, it's not made for kids** · Visibility: Public · Category *Howto & Style* · samodejni podnapisi izklopljeni.

### 4 · TikTok (9:16) ✅ objavljeno sob 7. 11.: https://www.tiktok.com/@whatsnextaction/video/7705333168898854166 · dodano pet 6. 11.
- Video `wna-waiting-for-9x16.mp4` (brez posebne TikTok različice).
- Opis:
```
Three people owe you an answer. Can you name all three? Park it. Forget it. The app remembers. #productivity #mentalload #focus #worklife
```
- Nastavitve: **AI-generated content** izklopljeno · **Your brand** ✅ · Cover: kader "Park it." · glasbe iz TikTok knjižnice ne dodajaj.
