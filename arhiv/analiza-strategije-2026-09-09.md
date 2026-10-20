# Kritični pregled marketinške strategije — stanje 9. 9. 2026

> Pregled vsega, kar je bilo dogovorjeno do danes (WNA plan pogl. 1–4, 6–8; launch-sequence; letni vsebinski osnutek; brainstorm 9. 9.). Namen: najti luknje, preden se karkoli objavi.

## Sodba v treh stavkih
Strategija je **poceni v denarju in draga v času ter potrpljenju**: socialni marketing brez plačanih oglasov, za publiko, ki jo je treba šele izobraziti (GTD novinci), z ničelno bazo sledilcev na treh od štirih platform. To pomeni počasno, a stabilno rast, ne eksplozije — če to sprejmeš vnaprej, plan zdrži. Največje luknje niso v vsebini, ampak **med videom in plačljivim uporabnikom**: pot od klika do registracije, aktivacija novinca v aplikaciji in merjenje, kaj sploh deluje.

---

## Kaj je dobro (obdrži)

**Ostro ciljanje in iskrena omejitev.** Odločitev "novinci, ne veterani" je najboljša odločitev v celem planu — reši te bitke za funkcije, ki bi jo izgubil, in določa ton vseh vsebin. Anti-persona je zapisana, kar je redko.

**Pozicioniranje "sistem, ki mu zaupaš" namesto "produktivnost".** Kategorija *task manager* je zasedena; *mir* ni. Tri jedrna sporočila z enim na video preprečujejo, da bi videi hoteli povedati vse.

**Ustanovitelj kot glas.** Edini razlikovalnik, ki ga nihče ne more kopirati, in hkrati najcenejši. Zgodba "Why I Built This" na strani je že napisana.

**Ločitev tokov in ritem.** Človek / podjetje / produkt z jasnimi pravili (personal nikoli ne prodaja; What's new gre navzgor, ne navzdol). Vsak drugi ponedeljek LinkedIn, vsak petek video — preprosto, vzdržljivo, predvidljivo.

**Zamik zagona in go/no-go.** Teden dni za račune, glas, posnetke, certifikat in registracijo je bil nujen. Product Hunt tri tedne po zagonu namesto na dan 0 je pravilno.

**Beta darilo Pro/Team za eno leto.** Nič te ne stane, kupi pa 15 ljudi, ki bodo prvi komentirali, delili in dali citate.

**Izpustitev X, Threads, Pinterest.** Manj računov = več pozornosti na tistih, ki štejejo.

**Sezonskost v letnem loku.** Januar in konec avgusta sta vgrajena; večina majhnih produktov to zamudi.

---

## Luknje in šibke točke (po resnosti)

### 1. Pot od videa do registracije ni definirana — 🔴 kritično, poceni popravek
Gledalec na TikToku je na telefonu. Klikne link v biu → pristane na strani, ki govori jezik GTD veteranov → "Start Free" je danes "Coming soon", Pro je "Contact Us". Vsak korak izgubi večino ljudi.
Manjka: (a) samopostrežna registracija, (b) pristajalna stran "novinec-first" (vsaj prvi zaslon), (c) **ali spletna aplikacija na telefonu sploh dobro deluje** (PWA? namestitev na domači zaslon?) — če ne, TikTok/Shorts/Reels promet pade v prazno, ker ti kanali so 95 % mobilni, (d) kratek URL za bio in videe (npr. `whatsnextaction.com/start`) namesto gole domene.
**Strošek:** dev čas (tvoj), 0 €. **Če ni:** ves petkov trud proizvaja oglede, ne uporabnikov.

### 2. Nič se ne meri — 🔴 kritično, skoraj zastonj
Ni dogovora o analitiki, UTM parametrih, niti o vprašanju "kje si slišal za nas" ob registraciji. Oktobrska revizija ("kateri persona/platforma se odziva") je brez tega nemogoča — odločali bi po občutku.
Manjka: analitika na strani (privacy-friendly, EU: Plausible/Umami ~10 €/mes ali GA4 zastonj), UTM na vsakem linku po platformi, eno vprašanje ob registraciji, tedenska tabela v md (ogledi po platformi → kliki → registracije → aktivirani → Pro). Pet številk, en stolpec na teden.
**Strošek:** 0–10 €/mes + 2 uri nastavitve.

### 3. Aktivacija novinca v aplikaciji — 🔴 strateško tveganje, srednje drago
Marketing obljublja "get it out of your head", produkt pa novinca sprejme s praznim Inboxom in besedami Next Actions / Waiting For / Someday. GTD ima znano težavo: ljudje ga opustijo v prvih tednih (tedenski pregled je disciplina). Ciljati novince pomeni **prevzeti nase izobraževanje**, ne le prodajo.
Manjka: prvi zagon, ki uporabnika vodi skozi prvih 5 stvari (capture → clarify ene stvari → prvi Next Action), in **onboarding mail zaporedje** (dan 1, 3, 7) — infrastruktura za mail že obstaja, manjka vsebina. To je najcenejša stvar z največjim učinkom na zadrževanje.
**Strošek:** dev + 3 maili (napišem jih). **Če ni:** registracije brez uporabnikov; social ne more popraviti aktivacije.

### 4. Manjka srednje dolg "kako deluje" video — 🟠 pomembno, poceni
15-sekundni klipi delajo zavedanje, ne razumevanja. Novinec, ki ga hook zanima, potrebuje 2–4 minute "how it works" — en video na YouTubu, na katerega kažejo vsi Shorts, pristajalna stran in beta mail. Brez tega ni mostu med "zanimivo" in "registriram se".
**Strošek:** en video, enkrat, posnetek zaslona + tvoj (pravi) glas. Naredi ga pred zagonom, če se da; sicer do 2. oktobra.

### 5. AI-generiran video kot tveganje, ne le prednost — 🟠 neznano, test pred zagonom
Utrujenost od AI vsebin je leta 2026 realna; TikTok in YouTube AI vsebino označita, del gledalcev jo preskoči. Higgsfieldovi prizori brez pravega produkta so "lep video o ničemer".
Pravilo: **pravi UI aplikacije nosi vsaj polovico vsakega videa**; AI prizori so 2–3-sekundni hook in prehod, ne vsebina. Vizualni stil mora biti enak vsak teden (predloga: barve, tipografija, zaključni kader), sicer račun izgleda kot naključni feed. **Prvi video je test:** če izgleda generično, se pipeline spremeni, preden je javen.
**Strošek:** Higgsfield naročnina (deset do nekaj deset €/mes, odvisno od kreditov; ponovitve stanejo), ElevenLabs (deset do nekaj deset €/mes). Poceni v denarju; tveganje je v kakovosti.

### 6. Tvoj čas je edini pravi strošek — 🟠 podcenjeno
Plan tiho predpostavlja: potrjevanje scenarijev, objavljanje na 4 platformah, odgovarjanje na komentarje (na novem TikTok/IG računu je prva ura po objavi odločilna), LinkedIn objave, What's new, plus razvoj. Realno **4–6 ur na teden** samo za marketing.
Kaj to zniža: orodje za načrtovanje objav (en upload → 4 platforme; Buffer/Metricool/Later imajo zastonj ali poceni pakete) — tvoja vloga postane "potrdi in pritisni". Odgovarjanje na komentarje pa ostane tvoje in ga ne gre delegirati — to je glas ustanovitelja.
**Strošek:** 0–30 €/mes za orodje; prihrani ~1 uro/teden.

### 7. Personal tok je najmočnejši asset in je najmanj izkoriščen — 🟡
600 sledilcev je edina baza, ki jo imaš, in ena objava mesečno na LinkedInu vzdržuje prisotnost, ne gradi občinstva (LinkedIn nagrajuje doslednost). Ne predlagam več objav — predlagam **10 minut tedensko komentiranja pod objavami drugih** (ustanovitelji, produktivnost, slovenski tech). To je zastonj in je edini pravi vzvod rasti na LinkedInu, ki ne zahteva ustvarjanja vsebine. Poleg tega: ni prepovedano, da občasno deliš petkov WNA video z enim stavkom — deljenje ni prodaja.

### 8. Reddit in Facebook skupine — 🟡 precenjeni
r/productivity aktivno odstranjuje promocijo aplikacij; nov račun brez karme je avtomatsko odstranjen. Facebook GTD skupine imajo pravila proti promociji. Realno: **r/gtd** (majhen, toleranten do iskrenih ustanoviteljev) in **r/SideProject** — in to samo, če Reddit račun obstaja in ima nekaj tednov sodelovanja. Če hočeš to na dan zagona, se sodelovanje začne **ta teden**.

### 9. Odvisnost objave 14. 9. od zagona 21. 9. — 🟡
"First product ships next week" v osebni objavi je obljuba z datumom. Če go/no-go v nedeljo 20. 9. pade, obljuba visi. Mitigacija: v objavo "next week" samo, če je v nedeljo 13. 9. vse razen videa pripravljeno; sicer "in the coming weeks".

### 10. Pravne in formalne malenkosti — 🟡 poceni, a obvezne
- GTD® blagovna znamka: stran in vsebine uporabljajo "GTD" opisno — v redu, ampak nikjer "GTD app" kot ime ali kategorija produkta v naslovih.
- Amazon link na strani: če je affiliate, potrebuje razkritje.
- Množični mail: zagonsko sporočilo beta uporabnikom je v redu; vsak nadaljnji marketinški mail potrebuje odjavo in privolitev (GDPR). Onboarding maili so transakcijski — v redu.
- AI oznaka: TikTok in YouTube zahtevata označitev sintetične vsebine — vedno. *(Posodobljeno 9. 10.: pravilo v `CLAUDE.md`; samo Instagram; TikTok in YouTube ne pri animiranih prizorih.)*
- Licence: preveri komercialno rabo pri Higgsfield in ElevenLabs paketu, ki ga vzameš.

### 11. Ni "lastnega" kanala — 🟡
Vse platforme so najete. Edino, kar je tvoje, je e-mail seznam — in imaš infrastrukturo. Ob registraciji opcijska privolitev za "What's new" mail; vsak izid gre tudi po mailu. Zastonj, dolgoročno najvrednejše.

### 12. Cilji odloženi do februarja — 🟢 sprejemljivo, z eno zahtevo
Prav je, da pravih KPI ne ugibaš. Ampak brez **vodilnih kazalnikov** (doslednost objav, ogledi, kliki, registracije/teden, aktivacija) oktobrska revizija nima podlage. Tabela iz točke 2 to reši.

---

## Kaj bo delovalo, kaj je negotovo, kaj ne bo

**Bo delovalo (visoka verjetnost):**
- Doslednost: 50 petkov zapored premaga vsak posamezen "viralen" poskus. Algoritmi nagradijo ritem po 6–10 tednih.
- LinkedIn za Pro/Team: edina platforma, kjer sedi kupec z denarnico in kjer tvoj naziv ter zgodba delata zate.
- Pravi UI + tvoj glas + zgodba ustanovitelja: kombinacija, ki jo veliki produkti ne morejo posnemati.
- Beta darilo → prvi citati in komentarji.
- Sezonski vrhovi (januar, konec avgusta), če je do takrat baza vsebin.

**Negotovo (test, potem odloči):**
- AI vizualije: lahko so prednost (hitrost, cena) ali slabost (generičnost, AI-utrujenost). Prvi video odloči.
- TikTok za persono A (32–45 z družino): manj prisotna kot Luka; verjetno se bo A odzvala na IG in LinkedIn, B na TikTok/Shorts. Oktobrska revizija to pokaže.
- Izobraževanje novincev v 15 sekundah: zavedanje da, razumevanje ne → zato točka 4.
- Kloniran glas z naglasom: avtentično ali moteče — test na 3 ljudeh, ki te ne poznajo.

**Ne bo delovalo (ne pričakuj):**
- Zagonski "pok" na TikTok/IG/YT: računi so stari en teden. Dan zagona je pravi samo na LinkedInu in v mailu.
- Reddit r/productivity in FB skupine kot kanal rasti.
- Mesečni LinkedIn kot rast občinstva — vzdržuje, ne gradi.
- Hitri Pro prihodki: novinci + Free paket + brez oglasov = mesece do smiselnih plačil. Leto 1 meri uporabnike in aktivacijo, ne prihodkov.
- Mobilni promet na spletno aplikacijo, ki na telefonu ni prijetna.

---

## Stroški

### Denar (mesečno, okvirno)
| Postavka | Okvir | Opomba |
|---|---|---|
| Higgsfield AI | deset do nekaj deset € | odvisno od kreditov; ponovitve generacij stanejo |
| ElevenLabs (klon glasu) | deset do nekaj deset € | Creator tier zadošča; professional clone kasneje |
| Orodje za načrtovanje objav | 0–30 € | zastonj paketi obstajajo |
| Analitika (Plausible/Umami ali GA4) | 0–10 € | |
| Link-in-bio / kratek URL | 0 € | lastna domena `/start` |
| Product Hunt, Reddit, vse platforme | 0 € | |
| **Skupaj** | **~30–120 €/mes** | zanemarljivo proti razvoju |

**Česa namenoma ne plačujemo (in kaj bi stalo):** plačani oglasi (Meta/TikTok: smiselno šele z izmerjeno aktivacijo; 300–1000 €/mes za test), vplivneži/produktivnostni YouTuberji (stotine do tisoče € na omembo), agencija ali video produkcija (tisoče €/mes). To je **plan B za Q1 2027**, če organska rast do februarja ne pokaže krivulje.

### Čas (pravi strošek)
| Kdo | Tedensko | Kaj |
|---|---|---|
| Vladimir | 4–6 h | potrjevanje (30 min), objavljanje (1 h, manj z orodjem), komentarji (1–2 h, razpršeno), LinkedIn (30 min + 10 min komentiranja), snemanje posnetkov zaslona ob novih funkcijah |
| Vladimir, enkratno pred zagonom | 15–25 h | računi, glas, posnetki zaslona, pristajalna stran, registracija, SSL, onboarding maili (vsebino dam), "how it works" video |
| Claude | — | scenariji, videi, tekst objav, maili, napotki, tedenska tabela, revizije |

Enkratni strošek pred zagonom je največji in je tudi razlog, da je bil teden zamika pravilen.

---

## Prioritetni popravki pred 21. 9. (poleg že dogovorjenega)
1. Samopostrežna registracija + preverjen mobilni tok registracije na telefonu (točka 1).
2. Analitika + UTM + vprašanje "kje si slišal za nas" (točka 2).
3. Kratek URL `/start` za bio in videe (točka 1).
4. Prvi video kot test AI stila — teden prej, ne na dan zagona (točka 5).
5. Onboarding maili dan 1/3/7 — vsebina od mene, pošiljanje prek obstoječe infrastrukture (točka 3).
6. Reddit račun + sodelovanje, če hočeš r/gtd na dan zagona (točka 8).
7. Pristajalna stran: vsaj prvi zaslon za novince; ostalo lahko po zagonu (točka 1).

Kar lahko počaka na oktober: "how it works" video (točka 4, a bolje prej), newsletter privolitev (11), Product Hunt priprava.

---

## Ena stvar, ki jo je vredno reči naglas
Ta strategija je vzdržljiva samo, če jo meriš proti pravemu cilju. Za leto 1 pravi cilj ni prihodek, ampak **koliko novincev prvi teden res vnese pet stvari in naredi en Weekly Review**. Če je ta številka dobra, bodo Pro plačila prišla; če je slaba, jih noben video ne bo prinesel. Zato sta točki 1 in 3 pred vsem drugim.
