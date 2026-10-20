# Personal #2 · Building software in the age of agents

- Kanal: LinkedIn, osebni profil
- Naslov ✅ smer (Vladimir, 19. 10.): "Razvoj v dobi agentov" oz. kako je nastal WNA; 📝 delovni naslov "Building software in the age of agents" (alternativa "How WhatsNextAction was built"). LinkedIn objava nima naslova, naslov je za interno in za morebitni prvi stavek.
- Datum: torek, 27. 10. 2026, 8:30. Intervju pon 26. 10. (✅ Vladimir, 9. 10.), osnutek isti dan, potrditev pon zvečer
- Vizual ✅ (Vladimir, 9. 10.): kratek video v slogu Twitch, 4 terminali 2 × 2 s Claude agenti pri pravem delu na WNA, Vladimirjeva kamera spodaj desno; timelapse 10–15 s, 1:1 1080 × 1080, brez zvoka, zanka; rezerva mirujoč kader

## Vizual: snemanje (Vladimir, do pet 23. 10.)
- 4 terminali v mreži 2 × 2 (npr. iTerm split), temna tema, pisava 16–18 pt; v vsakem prava naloga na WNA.
- Zasebnost: brez API ključev, gesel, `.env`, uporabniških podatkov, e-mailov; Do Not Disturb vklopljen.
- Hkrati: zaslon (Cmd + Shift + 5 → Record Entire Screen) in kamera (QuickTime → New Movie Recording), 2–3 min, pravo delo, brez poziranja, zvok ni potreben.
- Datoteki v `personal/video/raw/`.
- Claude: timelapse 10–15 s, kamera v krogu/zaobljenem okvirju spodaj desno, 1:1, brez zvoka, zanka (ffmpeg); rezerva mirujoč kader. Rok: pred intervjujem pon 26. 10.
- Status: ✅ tema (Vladimir, 9. 10.): kako je razvijati v dobi AI, skozi izkušnjo prvega produkta; ⬜ intervju pon 26. 10.; besedilo še ni napisano

Pravila: prva oseba, iskreno, brez samohvale, brez ponavljanja življenjepisa, brez pomišljajev, brez podpisa, ne prodaja WNA (lahko ga omeni kot primer, brez linka in CTA), brez "AI-powered" in "revolutionary".

## Intervju (zapiski, slovensko)

### Krog 1 (vprašanja pripravljena 9. 10.)
1. Kako je WhatsNextAction dejansko nastal? Kdo je kaj delal (ti, AI agenti, orodja), kako je izgledal tipičen dan razvoja?
2. Kaj te je najbolj presenetilo, v dobrem ali slabem, česar po 25 letih nisi pričakoval?
3. Kaj si delal drugače kot pri NiceHashu ali prej z ekipami ljudi? Kaj se je spremenilo in kaj ostalo isto?

## Slika tedna iz Pointeuse (13.–19. 10.; prebral Claude 19. 10., samo za pripravo, nič od tega ni za objavo brez potrditve)

**Številke (Claude Code, en teden; Pointeuse beleži od 13. 10.):**
- 977 promptov, **149 sej**; od tega ~80 sej agentov, ki jih je zagnal orkestrator (vloge platform-user, engineer, designer, tester, architect), ostalo tvoje.
- Največ sočasnih sej v 20 minutah: **15** (tor 13. 10. ob 11:39), običajno 7–8 (sre, čet, pet).
- Projekti: wna_orchestration 261 promptov, Pointeuse 195, wna_deploy 155, wna_web 83, wna_backend 82, pytools (trading bot) 81, wna-ui-tests 50, marketing 37.
- Ure: tor 10:00–23:42 (8,4 h aktivno), **sre 7:54–00:00 (10,7 h)**, čet 00:00–18:24 (6,7 h), pet 12:00–16:20 (4,1 h, dan izida in videa), vikend skoraj nič.

**Dnevi so si res različni:**
- **Tor 13. 10., orodja in stroški.** Dopoldne gradiš orodja zase (Pointeuse, PM plošča za trading bota), vmes popravki WNA prek ui-tests. Popoldne dolga debata o infrastrukturi: "kaj mi sploh k8s prinese, da mi odnese 70 % denarja" → ena VM za 68 EUR. Zvečer: "grem od računalnika, poženi celoten nabor testov".
- **Sre 14. 10., najdaljši dan.** Zjutraj odločitve o backupu (Madrid, urni 7 dni, dnevni 30 dni, alarm na Slack namesto e-pošte), nato načrt migracije kot FEAT za arhitekta, varnost skrivnosti na VM, krčenje CPU na podih, video za Googlovo verifikacijo OAuth. Ob 23h nov produkt od ideje do MVP v eni uri: "tvoje ocene so za ljudi".
- **Čet 15. 10., kakovost.** Varnostni bugi (registracija razkrije obstoječ e-mail, notranje poti dosegljive od zunaj), discipliniranje testnega agenta, pol ure iteracij logotipa za Google z agentom (J1 … J4, G4).
- **Pet 16. 10., izid.** Deploy na prod po korakih, ki jih poganjaš sam, video Capture, odgovor Googlu.
- **Vikend:** osnutek nove AI platforme.

**Vzorci, ki jih vidim (📝 Claude):**
1. **Ne pišeš kode, vodiš ekipo.** Tvoji prompti so odločitve ("daj vsako uro", "Greva v madrid", "J4 je izbran"), potrditve ("restarted, run the tests", "commit je na meni") in usmerjanje.
2. **Si vodilo med agenti.** Pogosto: "give me prompt for web", nato prilepiš v drugo sejo. Backend agent piše naloge za deploy agenta, ti jih preneseš. Del dela je dobesedno prenašanje sporočil.
3. **Agente si organiziral kot ljudi:** vloge, scenariji v uporabnikovih besedah ("zavezujoče"), zagoni s številkami, /slice → /implement → /test-all → /conclude.
4. **Največ trenja je pri zaupanju in obsegu:** "ti delaš samo to, kar te prosim", "tako enostavne naloge ne morejo trajati 2 h", "you didn't answer anything, you are just doing stuff", "vsega ne preberem, vprašanja morajo biti celovita". Testni agent preverja kodo namesto obnašanja.
5. **Hitrost spremeni načrtovanje:** ocene agentov so umerjene na ljudi; feature traja dan, ne teden.
6. **Denar je zdaj v infrastrukturi, ne v razvoju.** Debata o k8s, VM, backupih in cenah je vsak dan.
7. **Gradiš orodja za vodenje agentov** (Pointeuse, PM plošča): meta plast, ki je pri ekipi ljudi ni bilo.
8. **Agenti delajo, ko te ni** (regresije ponoči, "ko nisem za računalnikom").

⬜ Odprto za intervju: ali smeta v objavo nova projekta (restavracijski MVP, AI platforma)? 📝 Predlog: ne, samo WNA in orodja, ker sta druga dva še neobjavljena.

## Vizual: popravek snemanja 📝 (glede na sliko tedna)
- Realno teče 7–8 sej, ne 4. 📝 Predlog: mreža 2 × 2 ostane (berljivost), a izberi trenutek, ko res teče cikel: **orkestrator (arhitekt), backend, web, ui-tests**. Najbolj tipičen prizor je čet ali sre dopoldne, ko poganjaš /implement in teste.
- Posnemi 3–5 min med pravim delom, ne poziraj. Dobro je, če se vidi, ko prilepiš prompt iz ene seje v drugo: to je zgodba.
- 📝 Dodatno (opcija): zadnji kader timelapsa je pogled dneva v Pointeuse (pasovi projektov) za 1 s. Pokaže "cel dan" brez besed. Pred tem preveri, da v naslovih oken ni nič zasebnega.
- Zasebnost (pomembno, ker v sejah včasih prilepiš žetone ali gesla): pred snemanjem `clear` v vseh terminalih, brez `.env`, JWT, gesel, demo računov, e-mailov strank; Slack in Mail zaprta.

## Koncept ✅ (Vladimir, 19. 10.)
Ozek koncept, da ostane material za naslednje mesece. **#2 = prehod iz klasičnega v novodobni razvoj:** kako je nastal WNA, kako sem se učil iz napak, preveliko zaupanje v LLM in kako sem produkt na novi način pripeljal do konca. "En dan z mojo ekipo agentov" gre v nadaljevanje: ✅ personal #3, tor 24. 11. (Vladimir, 19. 10.).

**Časovnica iz gita (Claude, 19. 10.; za iztočnice, ne za objavo brez potrditve):**
- **okt 2025:** prvi commit backenda (1. 10.), klasično: C++ mikrostoritve (drogon, gtest, vcpkg), router in user service.
- **dec 2025:** deploy projekt (GKE).
- **jan–mar 2026:** najbolj intenzivno (backend feb 96 commitov, mar 74); mar prvi UI testi.
- **apr–maj 2026:** upad (33, 17 commitov). ✅ (Vladimir, 19. 10.): faza, ko je sam razbijal naloge in vodil agente, izgubil pregled, kdo kaj dela in kakšno je stanje; maja mu je Saša omenil vrhnji nivo s specifikacijami.
- **14. 6. 2026:** nov projekt wna_orchestration (orkestrator, po Sašinem nasvetu): "Defined all specs and prepared for new development". Začetek dela z vlogami agentov in specifikacijami; jun skok (68 commitov).
- **jul–okt 2026:** stalen ritem, beta 8. 10., zagon 9. 10.

**Lok objave 📝:**
1. Začel sem kot vedno: arhitektura, mikrostoritve, koda, AI kot pomočnik.
2. Napaka: preveliko zaupanje v LLM (kaj točno, kdaj se je pokazalo, koliko je stalo).
3. Obrat junija: najprej specifikacije, agenti v vlogah, jaz preverjam in odločam.
4. Kako sem produkt pripeljal do konca in kaj bi naredil drugače, če bi začel danes.
5. Vprašanje za bralce.

## Zgodba ✅ (Vladimir, 19. 10.; povzetek njegovih besed)
1. **ChatGPT na začetku:** pomagal skreirati projekte. Zasnova klasična: backend z unit testi, frontend samo uporabniški testi, deployment projekt s skriptami. ChatGPT je hitro prerasel, ostal je samo za pisanje testov.
2. **Claude Code:** najprej mali taski, potem vedno večji. Začel mu je prepuščati cele sklope na frontu in backu.
3. **Napaka, preveliko zaupanje:** delo narejeno napol, agent v neki točki zaide, ne razume zahtev.
4. **Kar je navdušilo:** unit testi. V nekaj minutah popolnoma stestiran nov unit. Zato novi nivoji testiranja: integracija, celotna backend platforma, nato nov projekt ui-tests, kjer agent iz specifikacij zapiše in izvaja teste.
5. **Boljše zahteve, nov problem:** sam je razbijal naloge in vodil, kateri agent kaj dela. Postal je zmeden, ni vedel, kdo kaj dela in kakšno je stanje.
6. **Obrat, maj/junij:** Saša mu je omenil vrhnji nivo, kjer pišeš specifikacije, agent pa določa, kdo mora kaj narediti. Uvedel je orkestrator: tam se pišejo zahteve in vodi stanje izvedbe po projektih. Vsak projekt ima natančno zapisane naloge in limite, do kod agent lahko gre. Tako je WNA prišel do releasa.
7. **Danes:** ne piše več kode, je primarno product owner. Daje zahteve za platformo in pregleda narejeno kot prevzem. Ker pozna kodo, ima oko na arhitekturi, obliki baze, poteku in obliki sporočil.
8. **Nauk:** vedno moraš biti zbran, ker agenti radi začnejo početi kaj drugega, kot pričakuješ. Potrebuješ orodja, s katerimi vse preveriš v okvirju.
9. **Zaključek:** "Razvoja, kot je bil, nikoli več ne bo."

## Intervju, krog 2 (19. 10., interaktivno)
**V1 (narejeno napol):** Vladimir: opazil je pri testiranju funkcije na koncu. Iz sej (Claude, samo za pripravo; seje so ohranjene šele od 21. 9., starejše Claude Code briše po 30 dneh, zato primerov iz pomladi ni) so izbruhi novejši in kažejo drug vzorec: agent ne pozabi dela, pozabi dogovor.
- 8. 10., deploy: ukazi za prod so se zanašali na prazne spremenljivke v lupini, nastalo je napačno ime slike; prod je ostal na stari verziji.
- 13. 10., backend: v slice je dal deploy odvisnosti, čeprav je bilo dogovorjeno, da jih ni.
- 13. 10., backend: popravljal nekaj, kar je Vladimir že rekel, da je popravljeno.
- 15. 10., backend: navodilo "/implement all bugs" se je izgubilo ob praznjenju seje; nobeden od BUG-049 do 053 ni bil narejen, čeprav je delo izgledalo končano.
Za objavo: brez citatov s kletvicami. ✅ Primer (Vladimir, 19. 10.): pravila se kršijo pri manjših stvareh (brez dodatnih knjižnic brez privolitve, pravila za komentarje se stalno kršijo). Pravilo testiranja: testi za pozitivni primer in glavne negativne. Pri funkciji **upload referenc** ni napisal niti pozitivnega; pokazalo se je ob ročnem zagonu, ko ni delalo. Agent je priznal, da je napisal trivialne teste, glavnega pa ne.

**V2 (čas za popravke) ✅ (Vladimir, 19. 10.):** na začetku sta pregled dela in testiranje vzela več časa kot na koncu. Popravljanje je bilo vedno hitrejše, kot če bi vse delal sam, zato je vztrajal. Najtežje je opisati spremembe UI: poravnave in barve. Večkrat je skočil v kodo in nekaj px ali hash barve nastavil sam: zanj največ 10 s, za LLM skoraj vedno vsaj 1 min. Dopolnitev: v kodo gre samo, ko LLM ne zadane, kar je vedno redkeje.

**V3 (unit testi) ✅ (Vladimir, 19. 10.):** unit testi so bili vedno stalnica pri resnih produktih, ni ga bilo treba prepričevati. Vedel je, da povečajo effort za ~20 %, zato jih pri manj pomembnih nalogah ni pisal. Z agentom so praktično brez dodatnega časa, zato imajo zdaj teste tudi najmanj pomembne funkcije; to se pozna pri uporabi: zelo malo bugov že v zgodnjih fazah. Dopolnitev: prepričala ga je cena; s ChatGPT je skoraj obupal, ko je projekt zrasel in ni več dohajal.

**V4 (zmeda) ✅ (Vladimir, 19. 10.):** 2 web, 1 backend, 1 deploy agent. Hkrati več taskov, ki so se (ali ne) razširili na več projektov; zaporedja back → web → deploy ali deploy → back → web, vmes web taski, med čakanjem na deploy neodvisen back task, ali vsi trije polni s tremi pipe taski. Na reMarkable si je pisal, kateri agent kaj dela. Vsak agent je spraševal in rabil odgovore; to je bilo ključno, da je produkt šel v njegovo smer. Ni vedel, kateri je končal in kateri čaka, zato je uvedel popup, ki takoj pritegne pozornost ob koncu ali vprašanju.

**V5 (limite) — prebral Claude iz projektov (19. 10.), ⬜ potrditev, kaj gre v objavo:**
- **Vloge v wna_orchestration:** *architect* (opus) edini sme spremeniti pogodbo (contract), piše samo v orkestracijo, "every decision is the owner's": odprte odločitve D1, D2 … predstavi eno po eno s priporočilom. *pm* (sonnet) ne načrtuje in ne piše kode, samo koordinira; feature zapre šele, ko so vsa polja zelena na lokalnih testih.
- **/slice:** za vsak projekt lokalni kos dela s povezavo na parent; legenda polj `[ ]` `[x]` `[~]` `[NA]`; dobesedno prepisana "Hard rules for the implementer": ne odkljukaj polja, ki ga nisi preveril v kodi (cit. file:line); done = vidno vedenje za uporabnika, ne "testi so zeleni"; "Overstating completion is the worst failure"; samo lokalno testiranje.
- **/implement:** vedno vse tri vrste testov (unit, integration, platform), pozitivni primer in vsi očitni negativni; pri bugih TDD obvezen (najprej test, ki pade); ob nejasnosti STOP in vprašaj v enem paketu; pogodbe ne spreminja sam; ureja samo svoj repo; nikoli commit/push brez ukaza; deploy ukazov ne izvede, samo izpiše za dev in prod.
- **Web CLAUDE.md:** brez novih komponent, barv in knjižnic brez vprašanja; nikoli trdo kodirane barve.
- Povezava z V1: pravilo "Overstating completion is the worst failure" je točno odgovor na upload referenc (trivialni testi namesto glavnega).

**V6 (prevzem) ✅ (Vladimir, 19. 10.):** prevzem = pregled funkcije; ob zapisu zahteve še ne veš točno, kako se bo obneslo, zato je ob prvem preizkusu lahko več stvari. Popolne zavrnitve še ni bilo. Po krajši uporabi je enkrat zahteval popoln redesign, ki je izhajal iz njegovih slabih zahtev. Najpogosteje: napačno razumljeni robni pogoji ali malenkost, za katero je LLM sklepal, da je tako najbolje, on pa se ne strinja; takrat odpreta enega ali več bugov in rešita skupaj. Več sprememb pri prevzemu je, ko je naloga zelo obsežna: LLM nekatere dele naredi slabo ali jih zanemari, in tega tudi on ne opazi takoj.

**V5 dopolnitev ✅ (Vladimir, 19. 10.):** preveč podrobnosti o načinu dela: "to je moja skrivnost in moj uspeh". V objavi samo splošno (agent na vrhu načrtuje, odločitve ostanejo pri njem, pravilo "never report done when it is not"); vloge, /slice, /implement, legenda polj ostanejo zunaj. Pravilo "Overstating completion is the worst failure" je v `/slice` od 16. 6. 2026 (commit f33d7c6 "Adding new work", dva dni po začetku orkestracije); povezave z uploadom referenc iz gita ni mogoče potrditi, zato je v objavi ne trdiva.

**V7 (orodja) ✅ (Vladimir, 19. 10.):** več nivojev testiranja, testi neodvisni, ker jih pišejo agenti z različnimi konteksti. Backend 3 nivoji, nad tem ui-tests; backend in ui-tests poznata skill /test-all (triaža testov). Orkestrator je arhitekt in planer naloge in na koncu v kodi preveri, ali je vse narejeno. Na koncu vse sam potestira kot uporabnik in napake takoj opazi. Pointeuse je samo lastna evidenca časa, s tem nima zveze (v objavah lahko z nedoločnim poimenovanjem).

**V5, pravilo ✅ (Vladimir, 19. 10.):** zaradi dramatičnega učinka v objavi rečeva, da je pravilo nastalo po trivialnih testih, čeprav to ne drži popolnoma.

**V8 (kaj pogreša) ✅ (Vladimir, 19. 10.):** všeč mu je bilo, ko je funkcijo naredil elegantno ali unikatno; uporabnik tega nikoli ni vedel, on pa je vedel, da je naredil nekaj posebnega, in to mu je veliko pomenilo. Zdaj LLM naredi, kar naredi; ne poglablja se, ve, da ni optimalno, je pa dovolj dobro, kar potrdijo vsi testi.

**Intervju končan 19. 10.** (namesto pon 26. 10.).

## Vprašanja za intervju pon 26. 10. 📝 (⬜ potrditev; 8 vprašanj; zgodba je že tu, intervju samo še konkretizira)
1. En konkreten primer "narejeno napol": kateri sklop, kaj si dobil nazaj, kako si opazil?
2. Koliko časa ti je vzelo popravljanje takih sklopov? Si kaj zavrgel in naredil znova?
3. Kateri trenutek z unit testi te je prepričal? Kako hitro se je to poznalo pri napakah?
4. Kako je izgledal dan, ko si bil "zmeden"? Koliko agentov hkrati, kje si vodil stanje?
5. Kako so zapisane limite agenta? Primer ene limite, ki jo agent ne sme prestopiti.
6. Kaj pri prevzemu najpogosteje zavrneš?
7. Katera orodja uporabljaš, da agente držiš v okvirju (testi, orkestrator, Pointeuse)? Katera smeva imenovati?
8. Kaj pogrešaš iz razvoja, kot je bil?

## Zaloga tem za kasnejše objave 📝 (⬜ razporeditev)
| Tema | Material | Možna objava |
|---|---|---|
| **En dan z mojo ekipo agentov: kaj delajo oni, kaj ostane meni** | Pointeuse: sre 14. 10. 7:54–00:00, do 15 sočasnih sej, 149 sej na teden, vloge agentov, ti kot vodilo med agenti | ✅ **personal #3 (24. 11.)**, nadaljevanje #2 (Vladimir, 19. 10.) |
| Ocene so za ljudi: hitrost spremeni načrtovanje | feature v dnevu, MVP od ideje do plana v eni uri | personal #4 ali 2027 |
| Denar je v infrastrukturi, ne v ekipi | k8s 70 % stroškov → ena VM, backupi, cene | personal #4 (22. 12.) "Year one, honestly" ali QubForge |
| Orodja za vodenje agentov | Pointeuse, PM plošča | 2027 (lahko z demom) |
| Vodenje agentov proti vodenju ljudi | primerjava z NiceHashem | 2027 |
| Novi projekti (restavracijski MVP, AI platforma) | še neobjavljeno | ob zagonu |

**Lok objave po zgodbi 📝:** razvoj, kot sem ga poznal 25 let → ChatGPT in Claude Code, prepuščanje celih sklopov → napol narejeno delo → testi kot prva prava zmaga → zmeda pri vodenju agentov → orkestrator, specifikacije, limite → danes product owner, ki pozna kodo → "nikoli več" + vprašanje za bralce.

Izogibava se v #2: prodaja WNA; citati s kletvicami; podrobnosti dneva z agenti (to je #3). ✅ Zamika "ships next week" ne omeniva (Vladimir, 19. 10.: WNA je že zunaj). ✅ Saša ostane "a friend" (Vladimir, 19. 10.).

---

## Osnutek v2 ✅ (Vladimir, 20. 10.: potrjen; jutri še en pregled) · 2985 znakov

Development as I knew it for 25 years is not coming back.

A year ago I started building WhatsNextAction the classic way, with every best practice I had learned. Backend services, unit tests, deployment scripts. ChatGPT helped me set it up, but once the project grew, it could not keep up. After that it only wrote tests and small snippets of code.

Then I found Claude Code. I started small and very cautiously, then gave it whole features in the frontend and backend.

That was my mistake. The work came back half done. The rule was simple: test the main case and the obvious failures. With uploading references, I tested it by hand and it failed. The agent admitted it had written a few trivial tests and skipped the main one. We argued many times about what was actually done and what was not. After that, I did not trust it.

Fixing was still faster than doing it all myself, but it was frustrating. It behaves like a teenager. It tries to get away with minimal effort, sometimes by cheating. You need strict boundaries and an eye on everything it does.

Testing still won me over. Unit tests always cost me about 20 percent more effort, so on less important work I skipped them. With an agent they cost almost nothing. Now even the smallest function has tests, and there are very few bugs, even early on.

Then I got lost. Two agents on the web app, one on the backend, one on deployment. Every agent had questions, and my answers kept the product going my way. I tracked on my reMarkable who was doing what and added a popup for every agent that finished or had a question. I still lost track.

In May a friend told me how he set up his projects: one level on top where you write the specs, and an agent that decides who does what. So I built an orchestrator. It holds the requirements and every project's status. Each agent has exact tasks and clear limits. One rule stands above the rest, written after those trivial tests: never report something as done when it is not.

That is how WhatsNextAction reached release.

Today I don't write code. I am the product owner. I give requirements and review what was built. Most often I find an edge case the agent understood differently. Once I asked for a complete redesign; the fault was in my own requirements. For UI I sometimes open the code myself: moving a few pixels takes me ten seconds, an agent at least a minute. Because I know the code, I still watch the architecture, the database and, when it matters, everything else.

Nothing rests on a single check: three levels of backend tests, UI tests written by agents with a different context, the orchestrator checking the code, and finally me, testing as a user.

What I miss is the elegance. Before, I sometimes built a function in an elegant or unique way. No user ever knew. I knew, and it meant a lot to me. Now the agent's code is not optimal, but it is good enough, and every test confirms it.

If you have been building software for years: where are you on this path?
