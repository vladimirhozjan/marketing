# WNA · Plan rasti do novega leta (16. 11. 2026 – 10. 1. 2027) 📝

- Avtor: Claude (pet 13. 11. 2026), na Vladimirjevo nalogo: "do novega leta spromovirati WNA, povečati doseg, prodaja mora začeti delati".
- Status: 📝 plan; ✅ odločitve D1–D8 sprejete (Vladimir, 13. 11.), glej pogl. 7. Razvoj V1, V3.1 (MCP title), V6 in ocene zagnan pet 13. 11. (prompt arhitektu).
- ✅ Obseg razvoja (Vladimir, 13. 11.): **zdaj samo FEAT-137 merjenje in FEAT-138 `title` orodij MCP**, nato Android (Play do konca novembra); FEAT-139 preizkus, 140 Empty your head, 141 nadgradnja, 142 maili, 143 priporočila, 144 ocene, 145 PH ponudba **šele po 10. 12.** Posledice so vpisane pri V1, V2, V5, V6, ciljih in časovnici.
- 📝 Predlog vrstnega reda po 10. 12. (okno do PH ima ~3 tedne s prazniki): **145 PH ponudba** (trd rok 4. 1.) → **139 preizkus** (nosi novoletni val, cilj v produkciji do 23. 12.) → 141 nadgradnja → 140 Empty your head → 142 maili → 143 priporočila, 144 ocene (januar).
- Velja skupaj z: `marketing-plan.md`, `registri-in-skupine.md`, `../koledar-objav.md`.

---

## 1. Diagnoza: kje smo v resnici

| Kaj | Številka (dan 3 po objavi) |
|---|---|
| Ogledi in prikazi od zagona 9. 10. (5 videov, 4 platforme) | ~3.000 skupaj; TikTok ~800 na video, IG 40–160, YT 7–71, LinkedIn QF 20–50 |
| Povprečen ogled na TikToku | 1,4–1,8 s (večina odide pri 0:01) |
| Novi pravi uporabniki od zagona | **0** (24 računov = beta in testni; pravi uporabnik je samo Vladimir) |
| Plačljivi uporabniki | 0 (beta dobila Pro/Team darilo) |
| Merjenje vira (UTM, "kje si slišal za nas") | **ni** |
| Najmočnejši posamezen kanal | Vladimirjev LinkedIn: 1.000–1.500 prikazov na objavo (QF stran: 20–50) |

**Zaključek (📝):**
1. **Tedenski video ne pripelje uporabnikov.** Doseg na novih računih brez sledilcev raste počasi, gledalci pa odidejo v prvi sekundi. To je trg, ne izvedba: AI video z animiranim 3D je tekmovanje za pozornost, ne za namero.
2. **Nimamo kanalov z namero.** Ljudje, ki *iščejo* orodje (App Store, Google, imeniki AI/MCP, "best GTD app", r/productivity), nas ne najdejo.
3. **Lijak je slep in brez vzvodov.** Ne vemo, od kod pride obisk; nov uporabnik nima razloga, da preizkusi Pro; ni zanke priporočil.
4. **Imamo dva nepoštena aduta, ki ju ne uporabljamo:** (a) *tvoj lastni AI dela s tvojimi seznami* (MCP + vgrajeni asistent), česar Todoist, Things in OmniFocus nimajo tako; (b) razvojni tempo: funkcija za rast stane pol dneva.

**Strategija v enem stavku:** do novega leta prestavimo težo z *oddajanja* (videi) na *namero* (App Store, imeniki AI, iskanje, skupnosti, osebna mreža) in pred tem popravimo lijak, da vsak obiskovalec šteje in ima razlog plačati.

---

## 2. Cilji do 10. 1. 2027 ✅ (Vladimir, 13. 11.: konzervativni)

✅ **150 registracij · 40 aktiviranih · 5 plačljivih · 300 sledilcev.** Spodnja tabela je bil predlog (📝), ostane za primerjavo.

| Merilo | Danes | Cilj | Zakaj ta številka |
|---|---|---|---|
| Registracije (pravi, z virom) | 0 | **300** | App Store + Product Hunt + imeniki; primerljivi indie zagoni 200–1.000 |
| Aktivirani (v 7 dneh ≥10 stvari v Inbox in ≥1 Clarify) | 0 | **90** (30 %) | brez aktivacije ni plačila |
| Plačljivi (Pro/Team) | 0 | **15** | 5 % aktiviranih ob reverse trialu (D2) |
| MRR | 0 € | **~200 €** | 15 × ~11 €; prvi dokaz, da prodaja dela |
| Doseg: sledilci skupaj (TikTok, IG, YT, LinkedIn QF) | ~60 | **500** | mreža ostaja glavni cilj (✅ 28. 10.) |
| Vladimirjev LinkedIn | ~943 | **1.200** | edini kanal z resnim dosegom |

📝 Tveganje (13. 11.): preizkus pride šele po 10. 12., zato prvi preizkusi Pro potečejo konec decembra ali v januarju; cilj 5 plačljivih do 10. 1. je ogrožen, registracije in sledilci ne. Do takrat "začeti preizkusi Pro" ostanejo 0, ne pomeni napake.

Vodilni tedenski kazalniki: obiski strani po viru · registracije po viru · aktivacija · začeti preizkusi Pro · plačila.

---

## 3. Osem vzvodov po učinku

### V1 · Popravi lijak, preden pripeljemo ljudi (teden 1, razvoj S/M): **najprej**
Brez tega bo vsak val kot zagon 9. 10.: ogledi, nič rezultata.
✅ Zdaj samo V1.1 (FEAT-137); V1.2–V1.5 po 10. 12. (Vladimir, 13. 11.). App Store zagon in imeniki (konec nov, začetek dec) zato pripeljejo ljudi v današnji lijak: Free, obstoječi tour, obstoječi Welcome mail. Besedila (V1.3) so že napisana v `besedila-rast.md`.
1. **Merjenje:** UTM na vseh povezavah (bio, opisi, imeniki), kratki `/start?src=…`, (✅ brez vprašanja "Where did you hear about us?", Vladimir 13. 11.: ne težimo z anketami; App Store `ct=` in Play `referrer` kampanjske povezave), vir shranjen pri uporabniku; v adminu tabela *vir → registracija → aktivacija → Pro*. (S)
2. **Prvih 5 minut (aktivacija):** ✅ zadnji diapozitiv obstoječega Welcome Toura postane "Empty your head": 10 vrstic za vse, kar te teži → en klik "Sort it with AI" (asistent razvrsti). Uporabnik takoj doživi glavno obljubo. (M)
3. **E-poštno zaporedje** (dan 0, 1, 3, 7, 14): en korak naenkrat (Inbox, Clarify, Today, Weekly Review, AI), vsak z enim gumbom nazaj v aplikacijo. Pišem jaz. (S)
4. **Reverse trial (✅ D2, 14 dni):** vsak nov račun 14 dni Pro (AI krediti, email to Inbox, sync), nato Free. Najmočnejši znani vzvod za konverzijo pri produktivnostnih aplikacijah; ljudje plačajo za to, kar so že uporabljali. (S)
5. **Trenutki nadgradnje v aplikaciji:** ko zmanjka kreditov, ob 3. projektu nad limito, ob email to Inbox: kratek, prijazen poziv z letno ceno. (S)

### V2 · App Store in Play Store zagon kot glavni dogodek leta (FEAT-108 v delu; Android do konca novembra, Vladimir 13. 11.)
App Store je kanal z namero: ljudje *iščejo* "to do list", "planner", "gtd".
1. ASO: ime ✅ *WhatsNextAction App*, podnaslov ✅ *Know your next action, with AI*, ključne besede, 6 posnetkov zaslona z enim sporočilom vsak (pripravim jaz iz pravih zaslonov), predogledni video 15–30 s iz obstoječih posnetkov.
2. **Ocene v prvem tednu:** ~15 beta uporabnikov osebno prosiš za oceno; v aplikaciji sistemski poziv za oceno po 3. opravljeni Weekly Review ali 20. zaključeni akciji (S). ✅ Poziv (FEAT-144) šele po 10. 12.; ob zagonu nosijo ocene samo osebne prošnje beta uporabnikom.
3. **Zagonski teden:** video "Now on the App Store" (vse štiri), QubForge objava, personal članek na začetku decembra (✅ D4), mail vsem 24 računom, imeniki (V3), Reddit samo tam, kjer pravila dovolijo.
4. ✅ D3: na iOS velja isti 14-dnevni reverse trial (D2), brez Applovega preizkusa; v App Storu "14 days of Pro, free". ⚠️ Preizkusa ob zagonu še ni: opis in posnetki v trgovinah ob zagonu **brez** "14 days of Pro"; dodamo s posodobitvijo, ko je FEAT-139 v produkciji.

### V3 · AI in MCP distribucija: naš klin
Ljudje, ki uporabljajo Claude ali ChatGPT za delo, iščejo, kam priklopiti svoje sezname. Tam smo prvi in edini "GTD sistem, ki ga upravlja tvoj AI".
1. **Registri** (plan s koraki: `registri-in-skupine.md`): uradni MCP Registry, Smithery, Glama, mcp.so v pon 16. 11.; Claude in ChatGPT imenika takoj, ko so dodani `title` orodij (razvoj S).
2. **Vsebina "Claude + WNA":** 3 kratki posnetki zaslona (brez 3D, pravi Claude): "Claude, plan my week from my inbox", "Claude, what am I waiting for?", "Weekly Review with Claude". To je novost, ki jo ljudje delijo; objave v r/ClaudeAI, r/ChatGPT, r/mcp in X ne (✅ ne X).
3. **Članek na strani:** "How to use Claude as your personal assistant for tasks (with MCP)": SEO za rastoče iskanje.

### V4 · Tvoja mreža ✅ D8: osebnega nagovarjanja ni (Vladimir, 13. 11.: mreža ni aktivna); ostane samo točka 2
1. **50 osebnih sporočil** (LinkedIn, mail) ljudem iz tvoje mreže, ki vodijo ljudi ali imajo polno glavo (bivši sodelavci Iskratel, Inova, NiceHash, partnerji): "Zgradil sem orodje zase; ali bi ga 2 tedna preizkusil in mi povedal, kaj manjka? Dobiš Pro za eno leto." Cilj: 20 aktivnih, 5 citatov, 3 Team ekipe. Osnutke sporočil napišem jaz, pošlješ ti.
2. **Personal LinkedIn (✅ D4, Vladimir 13. 11.):** pravilo "personal nikoli ne prodaja WNA" ostane. Personal članek na začetku decembra, ko sta zunaj iOS in **Android (Vladimir: Play Store do konca novembra)**; datum ⬜.
3. **Team paket:** 3 majhne ekipe iz mreže, brezplačno do konca januarja v zameno za študijo primera (QubForge objava januarja).

### V5 · Novoletni val "Systems, not resolutions" (26. 12. – 10. 1.)
Najboljši teden v letu za produktivnost: ljudje *iščejo* sistem.
1. **Product Hunt tor 5. 1. 2027** ✅ (Vladimir, 13. 11.; 31. 12., 1. 1. in sob 2. 1. zavrnjeni: prazniki in vikend pomenijo malo prometa, cilj so registracije, ne značka): priprava od 14. 12., lovec (hunter), 5 slik, prvi komentar, obveščeni beta uporabniki in mreža iz V4.
2. **Ponudba (✅ D5):** letni Pro −50 % samo za Product Hunt (kupon/povezava PH), 5.–12. 1. 2027. Novoletni val brez popusta nosi 14-dnevni preizkus (D2). ⚠️ Oboje pride po 10. 12.: FEAT-145 mora biti v produkciji do 4. 1., FEAT-139 čim prej pred 26. 12.; če preizkus ne pride pravočasno, val nosi samo Free in mail "New year, new system" brez omembe preizkusa.
3. Video #9 in #10 (že v koledarju) dobita CTA na ponudbo; mail vsem registriranim.
4. Skupnosti (iz `registri-in-skupine.md`): po šestih tednih sodelovanja Vladimir omeni WNA tam, kjer pravila dovolijo; Show HN in Indie Hackers v tednu Product Hunta.

### V6 · Zanka priporočil (razvoj S) ✅ po 10. 12., verjetno januar
"Give a month of Pro, get a month of Pro": povezava v Settings in v mailu po 7 dneh uporabe. Edini kanal, ki raste sam od sebe; pomemben za Team (delegiranje že vabi druge).

### V7 · Imeniki in iskanje (enkratno delo, trajne povezave)
1. AlternativeTo (kot alternativa Todoist, Things, OmniFocus, Nirvana), SaaSHub, Capterra/G2 (Team), There's An AI For That, Futurepedia (opis brez "AI-powered").
2. ✅ D6: ena splošna stran na whatsnextaction.com (npr. "Best apps for a calm task list"), samo dejstva; strani "vs" ne delamo.
3. Vsak petkov video dobi kratek članek (✅ že odločeno 26. 10.): bolečina v naslovu ("how to stop forgetting tasks").

### V8 · Petkov video: manj truda, več namena (✅ D7, Vladimir 13. 11.)
Podatki so jasni: TikTok prinese doseg, ne gledanja; YouTube in LinkedIn QF skoraj nič.
1. Ostane **en video na teden**, a brez Higgsfield 3D (dan dela, 19+ kreditov, brez merljivega učinka: #2 proti #4 enaka prva sekunda). Pravi UI + napis od kadra 0 + Julian.
2. Vsak drugi teden **"Claude + WNA"** posnetek namesto funkcije (V3).
3. LinkedIn QF ostane (skoraj brez dela); YouTube ostane zaradi iskanja.
4. Prihranjen čas gre v V1, V3, V4.

---

## 4. Časovnica po tednih

| Teden | Glavno | Ti (Vladimir) | Jaz (Claude) | Razvoj |
|---|---|---|---|---|
| **16.–22. 11.** | merjenje + registri | registri (pon), Reddit račun | analitika #5, besedila registrov, e-poštno zaporedje, #6 | FEAT-137 merjenje, FEAT-138 `title` orodij |
| **23.–29. 11.** | Claude/ChatGPT + Android | Claude/ChatGPT oddaja, Reddit komentarji | App Store posnetki in besedila, članek "Claude + WNA", video "Claude + WNA" #1 | Android (Play do konca nov) |
| **30. 11.–6. 12.** | App Store zagon (če FEAT-108 pride) | ocene beta uporabnikov | zagonski teden (video, QF, personal, mail), imeniki V7 | iOS (FEAT-108) |
| **7.–13. 12.** | revizija + iskanje | revizija pon 7. 12. (prave številke iz V1.1) | primerjalne strani, 2 članka, video #9 | od 10. 12.: FEAT-145 PH ponudba, FEAT-139 preizkus |
| **14.–20. 12.** | priprava PH | izbereš lovca, potrdiš ponudbo | Product Hunt paket, novoletna kampanja, video #10 | FEAT-139 preizkus (do 23. 12.), 141 nadgradnja |
| **21.–27. 12.** | premor objav | personal #4 | načrt januarja, maili v čakalni vrsti | 140 Empty your head, 142 maili (če gre) |
| **28. 12.–3. 1.** | novoletni val | skupnosti (kjer dovoljeno) | mail "New year, new system", objave | |
| **4.–10. 1.** | **Product Hunt tor 5. 1.** | ves dan na PH, Show HN, Indie Hackers | prvi komentar, odgovori, analitika | 145 preverjen v produkciji do 4. 1. |

---

## 5. Merjenje (od tedna 1)

Vsak ponedeljek v `marketing-plan.md` pogl. 11 namesto samo ogledov:

| Teden | Obiski | Registracije (po viru) | Aktivirani | Preizkusi Pro | Plačila | MRR | Sledilci |
|---|---|---|---|---|---|---|---|

Pravilo: kanal, ki v treh tednih ne prinese nobene registracije, dobi minimalen trud.

---

## 6. Česa ne delamo (namenoma)

Plačani oglasi (✅ ne) · X (✅ ne) · nove platforme (Threads, Bluesky, Pinterest) · Android do konca leta (XL, roadmap) · več videov na teden · popusti brez roka.

---

## 7. Odločitve zate ⬜ (priporočilo prvo)

| | Odločitev | Priporočilo | Trud |
|---|---|---|---|
| **D1** ✅ | Cilji do 10. 1. (pogl. 2) | ✅ konzervativni: 150 / 40 / 5 / 300 (Vladimir, 13. 11.) | – |
| **D2** ✅ | Reverse trial: 14 dni Pro za vsak nov račun | ✅ da, 14 dni, brez kartice, nato Free (Vladimir, 13. 11.) | razvoj S |
| **D3** ✅ | Preizkus na iOS | ✅ isti 14-dnevni reverse trial kot na spletu, brez Apple introductory offer (Vladimir, 13. 11.) | razvoj S |
| **D4** ✅ | Personal ob App Store zagonu | ✅ pravilo ostane brez izjeme; namesto tega personal **članek na začetku decembra**, ko sta zunaj iOS in Android (Vladimir, 13. 11.; datum ⬜) | S |
| **D5** ✅ | Novoletna ponudba | ✅ letni Pro −50 % (48 € namesto 96 €) samo za obiskovalce Product Hunta, 5.–12. 1. 2027 (Vladimir, 13. 11.) | razvoj S |
| **D6** ✅ | Primerjave na spletu | ✅ ena splošna stran (npr. "Best apps for a calm task list"), brez strani "vs" (Vladimir, 13. 11.) | S (pišem jaz) |
| **D7** ✅ | Petkov video | ✅ brez 3D, vsak drugi teden "Claude + WNA" (Vladimir, 13. 11.) | prihranek |
| **D8** ✅ | Mreža | ✅ ne: mreža ni aktivna in ne bo (Vladimir, 13. 11.); V4.1 in V4.3 odpadeta | – |

Opomba: `CLAUDE.md` navaja Pro 9 €, `wna_orchestration/contracts/subscription-tiers.md` pa Pro 11 €/mesec ali 96 €/leto in Team 18 €. V vseh besedilih uporabim pogodbo (96 €/leto), dokler ne rečeš drugače.
