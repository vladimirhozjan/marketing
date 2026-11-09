# WNA · Landing hero: AI asistent (FEAT-081)

- Namen: animacija na heroju landing strani (FEAT-081 D3/D4, `wna_orchestration/features/FEAT-081-ai-landing-pricing-help.md`).
  Kaže samo vgrajenega asistenta; "ali uporabi svoj AI" je vrstica pod njo (to ni del posnetka).
- Sporočilo: AI je orodje, ki ti prihrani delo. Ti se odločiš, AI pretipka in razvrsti.
- Brez glasu, brez napisov v posnetku (besedilo ob animaciji določi designer). Kratke zanke, ki se ponavljajo.
- Snemanje: **prod**, račun `demo@whatsnextaction.com` (Pro, 10.000 kreditov ≈ 110 zahtev), **desktop**:
  asistent je zasidran desno, seznam levo se osvežuje sam (FEAT-080), zato se v enem kadru vidita oba.
  Na telefonu panel prekrije zaslon, zato mobilni posnetek ne pride v poštev.
- Status: 📝 račun pripravljen (Claude, 2. 11.), čaka na snemanje (ti). ✅ Ponovno snemanje ta teden (Vladimir, 9. 11.): izboljšana izkušnja asistenta, stvari se na seznamu pojavljajo in izginjajo.

## Priprava pred snemanjem (ti)

- [ ] Svetla tema, okno 1440 × 900, zoom 100 %, brez zaznamkov in razširitev v vrstici, obvestila sistema izklopljena.
- [ ] Settings → AI Assistant: preizkusi en ukaz na privzetem modelu (DeepSeek V4 Flash) in na najhitrejšem; vzemi
  tistega, ki ukaz naredi pravilno v najmanj korakih. Čakanje bo v montaži pospešeno.
- [ ] Pred vsakim ponovnim posnetkom mi reci **"reset demo"** in vrnem račun v začetno stanje (spodaj).

## Začetno stanje računa (pripravljeno 2. 11.)

| Seznam | Vsebina |
|---|---|
| Inbox (8) | flights to Lisbon in May? · Luka wants the Q4 slides by Friday · gift for Ana · kitchen - ask when the cabinets get delivered · car insurance expires 30 Nov · fix the leaking tap · idea: monthly newsletter for clients · return the library books |
| Projekti (3) | **Q4 client report** (Work) · **Kitchen renovation** (Home) · **Ana's 40th birthday** (Family, **prazen canvas, brez akcij**) |
| Next | Pull the Q4 numbers from the dashboard · Choose tiles at the showroom · Renew passport · Back up the laptop · Book a dentist check-up · Water the plants |
| Today | Pay the electricity bill · Call mum back |
| Waiting For | Sales summary from Luka (Luka) · Quote for the new cabinets (Contractor) |
| Someday | Learn Spanish |
| Horizons | Areas: Work · Family · Home · Health |
| Tagi | @computer · @phone · @errands · @home |

## Kader A: canvas se napolni (glavni, najbolj dinamičen) 📝

1. Odpri projekt **Ana's 40th birthday** → **Brainstorm** (prazen canvas). Odpri asistenta (sparkles zgoraj).
2. Začni snemati. Vpiši in pošlji:
   > Brainstorm Ana's 40th birthday on the canvas: guests, venue, food, music and the gift.
3. Na canvasu se pojavljajo veje in ideje. Ko se ustavi, počakaj 2 s na mirnem canvasu in ustavi snemanje.
4. (Neobvezno, A2) Na canvasu **Convert with AI** → predlog akcij → potrdi → akcije v projektu.

Dolžina v montaži: 6–8 s (pospešeno). Posnetek: `raw/hero-a-canvas`.

## Kader B: Inbox se izprazni, seznami se napolnijo 📝

1. Odpri **Inbox** (8 stvari). Asistent odprt.
2. Začni snemati. Vpiši in pošlji:
   > Sort my inbox. Turn each item into a next step with a context, put anything that belongs to a project into it,
   > and send ideas to Someday.
3. Vrstice izginjajo iz Inboxa, števec pada proti 0, števci Next / Projects / Someday v stranski vrstici rastejo.
4. Ko je Inbox prazen, počakaj 2 s, nato (pretop) klik na **Next Actions**, kjer so nove akcije s tagi. Ustavi.

Pričakovano: "gift for Ana" → projekt Ana's 40th birthday · "Luka … Q4 slides" → Q4 client report ·
"kitchen …" → Kitchen renovation · "newsletter" → Someday · "flights to Lisbon" → Someday ali nov projekt.
Če asistent kaj razvrsti čudno, posnetek ponovi (reset demo).

Dolžina v montaži: 6–8 s. Posnetek: `raw/hero-b-inbox`.

## Kader C: dan se splanira (rezerva) 📝

1. Odpri **Today** (2 akciji). Asistent odprt.
2. Pošlji:
   > Plan my Friday: put the three most urgent things on Today.
3. Today se napolni. Ustavi po 2 s mirnega zaslona.

Posnetek: `raw/hero-c-today`. Uporabi le, če A ali B ne uspe.

## Montaža (jaz)

- Vrstni red zanke: **A → B** (rez na mirnem zaslonu), skupaj ≈ 12–15 s; brez tipk, bliskov in približkov
  (mirna verzija UI kot pri #3/#4); čakanje asistenta pospešeno, tipkanje ukaza pustiš berljivo.
- Oddaja (FEAT-081 je izšel, hero ga samo prebere — drop-in, brez spremembe kode):
  `wna_web/main/src/main-app/assets/landing/landing-hero.mp4` — H.264, **brez zvočne sledi**, 16:10, **1600 × 1000**,
  **≤ 4 MB** (igra inline na iOS Safari) + `landing-hero-poster.jpg` (prvi kader, ista velikost).
  Ena datoteka za obe širini; pri 500 px se pomanjša, besedilo ni nujno berljivo, nosi ga gibanje.
- Dokler datoteke ni, hero kaže današnjo `landing-engage.png`.

## Reset demo (Claude prek MCP `wna-demo`)

Vse, kar je asistent ustvaril v posnetku, v koš; Inbox znova 8 stvari iz tabele; canvas projekta Ana's 40th
birthday prazen (ideje se brišejo trajno); ostale sezname vrnem na tabelo zgoraj.
