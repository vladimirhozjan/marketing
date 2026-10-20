# WhatsNextAction — kaj vse je v produktu (iz specifikacij, stanje 15. 9. 2026; pogl. 9 in 10 posodobljena 20. 10.)

> Vir: `wna_orchestration/specs/features/wna-features.md` (33 poglavij), `email-to-inbox.md`, `p2-team-collaboration.md`, `contracts/limits.md`, `roadmap.md`.
> Namen: seznam za videe in objave. Stolpec **Video** = ali funkcija nosi samostojen petkov video (★★★ = prva faza, ★★ = kasneje, ★ = omemba, – = ne).

## 1. Capture (vse iz glave)
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Inbox | Vnos "stuff" brez metapodatkov, Enter za vnos, seznam brez omejitev, števec v stranski vrstici | vsi | ★★★ | "40 things in your head? Type them. Don't sort. Just type." |
| Quick Add | Vnos v Inbox z **vsake** strani: gumb v zgornji vrstici (desktop), plavajoči gumb spodaj desno (mobilno); ostane odprt za hitro serijo vnosov | vsi | ★★★ | "Wherever you are in the app, one tap and it's captured." |
| Email to Inbox | Zasebni e-naslov; karkoli pošlješ ali posreduješ, pristane v Inboxu (priponke pridejo kasneje); stikalo on/off, reset naslova, dnevna kvota 50 (Pro) / 100 (Team) | Pro/Team | ★★★ | "Forward the email. Forget the email. It's in your Inbox." |
| Inbox Zero proslava | Ko izprazniš Inbox, kratka animacija "Inbox Zero. You're in control." | vsi | ★★ | "This is what an empty head looks like." |
| Delegirani vnosi | Kar ti delegira sodelavec, pride v tvoj Inbox z oznako "From: ime" | Team | ★ | (skupaj z delegiranjem) |

## 2. Clarify (voden čarovnik)
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Korak 1: Is it actionable? | Y/N s tipkovnico; Ne → Reference / Someday / Trash takoj | vsi | ★★★ | "Is it even a task? One key answers it." |
| Korak 2: Single action or project? | En korak ali več korakov → projekt z obveznim "What does done look like?" | vsi | ★★ | "Most of your 'tasks' are projects. Here's how you tell." |
| Korak 3: Two-minute rule | "Can you do it in under 2 minutes?" → Do It Now zaslon | vsi | ★★★ | "Under two minutes? Don't file it. Do it." |
| Create Action | Naslov, opis, oznake (s predlogi), datumi zloženi (Scheduled / Start after / Due, trajanje) | vsi | ★★ | "Give it a next action, not a deadline." |
| Clarify način | Seznam ob strani, napredek 1/3, samodejno naprej na naslednji element, Escape/Backspace | vsi | ★★ | "Five items, ninety seconds. Watch." |

## 3. Organize (predalčki)
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Next Actions | Seznam pripravljenih naslednjih korakov; filtriranje po oznakah; premikanje z vlečenjem | vsi | ★★★ | "Know your next action." (ime produkta) |
| Today | Kar si izbral za danes; ločeno od vsega ostalega | vsi | ★★★ | "Not everything. Just today." |
| Calendar | Dan / teden / mesec / leto / ponavljajoče; bloki po uri in trajanju; rumeni "start" in rdeči "due" indikatorji; črta trenutnega časa; klik na prazno uro = nov vnos | vsi | ★★ | "Your calendar is for hard landscape only. Everything else lives elsewhere." |
| Projects | Seznam izidov z obveznim izidom; podrobnosti s koraki; premik v Next/Reference/Someday | Free: 7 aktivnih, Pro/Team: neomejeno | ★★ | "A project isn't a task. It's an outcome with steps." |
| Waiting For | Na koga/kaj čakaš + koliko časa že ("3d", "2w"); "Got it" vrne v Next | vsi | ★★★ | "Waiting on someone? Park it. Forget it. The app remembers." |
| Someday / Maybe | Mešan seznam (stuff, akcije, projekti); "Activate" vrne v izvorni predalček; projekt obnovi svoje korake | vsi | ★★ | "Not now doesn't mean never." |
| Reference (file manager) | Mape, iskanje po vseh mapah, seznam/mreža, predogled, prenos, koš, prikaz kvote | Free: samo ogled, 50 MB · Pro 250 MB · Team 1 GB/uporabnika | ★ | "The stuff you'll need later, where you'll find it." |
| Completed | Arhiv opravljenega z Undo | vsi | ★ | – |
| Trash | Mehko brisanje, obnova | vsi | – | – |
| Drag & drop | Preurejanje v seznamih; vlečenje elementa na predalček v stranski vrstici ga premakne (projekt v Next postane akcija); namig ob prvem obisku | vsi | ★★ | "Drag it where it belongs. Done." |
| Context tags | Prosto besedilo z avtodopolnjevanjem; predlogi @computer @phone @errands; filter na strani + **globalni kontekst** v stranski vrstici, ki filtrira vse hkrati | Free: 10 oznak, Pro/Team: neomejeno | ★★★ | "@errands: what can you do while you're already in town?" |
| Attachments | Do 10 datotek na element; velikost 5 / 20 / 50 MB | vsi (po paketu) | ★ | – |
| Comments | Komentarji z zgodovino na vsakem elementu | vsi | ★ | – |
| Overdue označevanje | Rdeč rob in značke "Due"/"Overdue" povsod; rdeči opozorilnik na Engage | vsi | ★ | – |

## 4. Reflect
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Weekly Review | Voden seznam 6 korakov (Inbox, Next, Waiting, Projects, Someday, Calendar) z napredkom "N of 6" in "Last reviewed: N days ago"; predlog ponavljajočega opomnika; posebna značka "Weekly Review" na akciji | vsi (vklop v nastavitvah) | ★★★ | "Friday. Fifteen minutes. Nothing falls through." |
| Recurring actions | Predloge z ravnilom: dnevno/tedensko/mesečno/letno, interval, dnevi v tednu, konec; človeški povzetek ("Every 2 weeks on Mon, Wed"); pogled Recurring v koledarju | Pro/Team | ★★ | "Set it once. It shows up when it should." |

## 5. Engage
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Engage dashboard | Prva stran po prijavi: opozorilo o zapadlih, Today (5), Next (5), Waiting For (5), **nudges** "Keep your system clean"; globalni kontekst filtrira vse | vsi | ★★★ | "Open the app. See exactly what to do. Close the app." |
| GTD tips | Vgrajeni nasveti na straneh, zapreš in si zapomni | vsi | ★ | – |

## 6. Ekipa (Team paket)
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Connections | Povabilo po e-pošti, sprejem/zavrnitev, seznam povezav, značka s številom, rdeča pika za čakajoča povabila | Team (sprejem samo Team) | ★★ | "Invite the people you actually work with." |
| Delegation | Akcijo dodeliš povezavi: pri tebi gre v Waiting For, pri njej v Inbox "From: ti"; ko jo konča, se pri tebi razreši; verige delegiranja | Team | ★★★ | "Delegate it. It leaves your list and lands in theirs. You get notified when it's done." |
| Shared Projects | Deljen projekt z vlogami (owner / write / read-only), backlog z dodeljenimi, zapusti / odstrani člana | Team | ★★ | "One project. Everyone sees the same next actions." |
| In-app notifications | Zvonec z nepreberimi; e-poštna obvestila po dogodkih z izklopom; varnostna vedno | vsi | ★ | – |

## 7. Račun, nastavitve, platforma
| Funkcija | Kaj naredi | Paket | Video | Hook (EN) |
|---|---|---|---|---|
| Registracija + Google SSO | E-pošta/geslo z verifikacijo ali prijava z Googlom; pozabljeno geslo | vsi | ★ | "Start free in under a minute." |
| Settings | Tema (svetla/temna/sistem), časovni pas, začetek tedna, 12/24 h, delovne ure in dnevi, položaj novih elementov, obvestila po dogodkih, seje | vsi | ★ | "Dark mode, your timezone, your week." |
| Mobile web | Predal namesto stranske vrstice, plavajoči gumb za vnos, spodnji listi namesto menijev, gumbi vedno vidni na dotik | vsi | ★★ | "Works in your browser, on any device. Native apps this winter." |
| Keyboard | Y/N v čarovniku, Enter/Escape/Backspace, vejica za oznako | vsi | ★ | – |
| Feedback gumb | Oblaček spodaj desno → e-pošta | vsi | – | – |
| Public pages | Landing, Pricing (Free / Pro 9 € / Team 14 €, letno 3 mesece gratis), Help, Terms, Privacy | – | – | – |

## 8. Omejitve po paketih (za ceno v videih)
| | Free | Pro | Team |
|---|:--:|:--:|:--:|
| Stuff & actions | ∞ | ∞ | ∞ |
| Aktivni projekti | 7 | ∞ | ∞ |
| Oznake | 10 | ∞ | ∞ |
| Ponavljajoče akcije | – | da | da |
| Email to Inbox | – | 50/dan | 100/dan |
| Reference | samo ogled | polno | polno |
| Shramba / priponka | 50 MB / 5 MB | 250 MB / 20 MB | 1 GB/uporabnika / 50 MB |
| Connections, delegiranje, deljeni projekti | – | – | da |

## 9. Kar prihaja (roadmap: Now / Next) — za "What's new" objave, ne za obljube v videih
- Izide okt 2026: **Google Calendar sync** (dvosmerno, Pro/Team; What's new 📝 pon 26. 10.), **BYOS Google Drive** (priponke v lastnem Drivu, tudi za Free; What's new 📝 pon 2. 11.), Google account connection
- V delu: **Apple / Microsoft SSO** (⬜ stanje preveri v orkestratorju)
- Načrtovano: priponke prek Email to Inbox, **globalno iskanje**, Cmd+K paleta, **onboarding ob prvi prijavi**, množične operacije, izboljšave Weekly Review (napredek, praznovanje), mobile-web poliranje (poteze, pull-to-refresh), **streaks**, prazna stanja z ilustracijami, Undo, Notes, USD za ne-EU
- Kasneje: native iOS/Android (offline, push, widget, share extension), Horizons of Focus, Natural Planning Model, checklists, rich capture (foto/zvok), javni API, izvoz podatkov

## 10. Predlog vrstnega reda petkovih videov (faza 1, po ★★★)
1. Capture: Inbox + Quick Add ("get it out of your head") ✅ objavljeno pet 16. 10.
2. Clarify: Is it actionable? + Two-minute rule ✅ pet 23. 10.
3. Next Actions / Today ("know your next action") ✅ čet 29. 10.
4. Waiting For (pet 6. 11.)
5. Context tags (@errands) (pet 13. 11.)
6. Weekly Review
7. Engage dashboard ("open, see, close")
8. Email to Inbox (Pro)
9. Delegation (Team, LinkedIn)
