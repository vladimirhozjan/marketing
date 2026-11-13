# WNA · AI in MCP registri ter skupine 📝

- Namen: novoletni val (✅ smer, Vladimir 26. 10.). Registri prinesejo povezave na stran in uporabnike, ki že uporabljajo
  Claude ali ChatGPT; skupine potrebujejo nekaj tednov sodelovanja, zato začnemo zdaj.
- Status: 📝 predlog Claude (pet 13. 11.), ⬜ potrditev (Vladimir). Pogoje registrov sem preveril 13. 11. na spletu;
  večina virov je tretjih oseb, uradne strani preverim ob oddaji.
- Strežnik: `https://api.whatsnextaction.com/mcp` (FEAT-070: Streamable HTTP, OAuth 2.1 z dinamično registracijo
  klienta, 78 orodij, vsak paket). Vodič: `https://whatsnextaction.com/help/connect-ai`.

## Pregled: kje vse objavimo, da WNA obstaja 📝 (13. 11.; ✅ = odločeno)

| Kdaj | Kje | Stanje |
|---|---|---|
| teče | TikTok, IG Reels, YouTube Shorts, LinkedIn QF (petkov video) · mail What's new · članki na whatsnextaction.com · ena splošna primerjalna stran (D6) | ✅ |
| pon 16. 11. | **Uradni MCP Registry** (→ GitHub MCP Registry, VS Code, PulseMCP) · Smithery · Glama · mcp.so · awesome-mcp-servers (PR) | ⬜ |
| konec nov | **Claude Connectors Directory** · **ChatGPT apps** (po `title` orodij) | ⬜ |
| konec nov / dec | **Google Play** (✅ do konca nov) · **App Store** (FEAT-108) · zagonski teden: video, QF, mail · personal članek začetek dec (✅ D4) | ⬜ |
| december | AlternativeTo · SaaSHub · Capterra · G2 · There's An AI For That · Futurepedia · Toolify | ⬜ |
| od zdaj, vrh okoli novega leta | Reddit: r/ClaudeAI, r/mcp, r/productivity, r/getdisciplined; r/gtd enkrat (prva omemba WNA po reviziji 7. 12.) | ⬜ |
| **tor 5. 1. 2027** | **Product Hunt** ✅ (letni Pro −50 %, D5) · Show HN · Indie Hackers | ✅ datum |
| ne | X ✅ · plačani oglasi ✅ · Facebook GTD skupine · GTD Connect | ✅ |

## Kaj WNA že izpolnjuje in kaj manjka

| Zahteva (imeniki Claude, ChatGPT, Microsoft) | Stanje |
|---|---|
| Javni HTTPS, Streamable HTTP, OAuth | ✅ |
| Vsako orodje ima `readOnlyHint` / `destructiveHint` | ✅ (`wna_backend/backend_common/mcp/tool_catalog.cpp`) |
| Vsako orodje ima `title` (Claude review) | ⬜ manjka; v razvoju FEAT-138 (zagnan 13. 11.) |
| Testni račun za pregled | ✅ demo račun (za pregled ločen, glej ⬜ 3) |
| Politika zasebnosti, pogoji, podpora | ✅ `/legal/privacy`, `/legal/terms`, hello@whatsnextaction.com |
| Logo, kratek in dolg opis | 📝 pripravim jaz (ikone v `brand/icons/`) |

## Ponedeljek 16. 11.: plan

| Ura | Kdo | Kaj | Trajanje |
|---|---|---|---|
| 9:00 | Claude | analitika #5 dan 3; besedila za vse registre (spodaj, "Besedila") | 1 h |
| 10:00 | ti + jaz | **1 Uradni MCP Registry** (DNS + objava) | 30 min |
| 10:30 | ti | **2 Smithery** · **3 mcp.so** · **4 Glama** | 30 min |
| 11:00 | ti | **5 Claude Connectors Directory**: preveri dostop in obrazec (oddaja, ko so `title` dodani) | 15 min |
| 11:15 | ti | **6 ChatGPT apps**: preveri dostop, test v Developer Mode | 30 min |
| 11:45 | ti | **7 Reddit**: račun in prvi komentarji | 20 min |
| popoldne | Claude | taski v WNA marketing; task za razvoj (`title` orodij) | |

Pozneje (ne v ponedeljek): Microsoft Copilot Connectors, imeniki AI orodij, Indie Hackers / Show HN ob native zagonu.
Brez oddaje: **Gemini** (ni javnega imenika, samo partnerstva in Enterprise) in **Mistral** (ni oddaje, uporabnik
doda strežnik z URL; to pokriva vodič "other MCP apps").

---

## 1 · Uradni MCP Registry (registry.modelcontextprotocol.io)

Zakaj prvi: iz njega se napajajo GitHub MCP Registry, galerija v VS Code, PulseMCP (ta trenutno ne sprejema
neposrednih oddaj) in deloma Smithery. Ime strežnika bo `com.whatsnextaction/wna`, lastništvo dokažeš z DNS.
`server.json` pripravim jaz v `whatsnextaction/mcp-registry/`.

1. V terminalu namesti orodje: `brew install mcp-publisher`
2. Ustvari ključ (zasebni ključ ostane pri tebi, nikomur ga ne pošiljaj):
   `openssl genpkey -algorithm Ed25519 -out ~/.wna-mcp-key.pem`
3. Izpiši javni ključ: `echo "v=MCPv1; k=ed25519; p=$(openssl pkey -in ~/.wna-mcp-key.pem -pubout -outform DER | tail -c 32 | base64)"`
4. Pri ponudniku DNS za whatsnextaction.com dodaj **TXT** zapis na `whatsnextaction.com` (ime `@`) z vrednostjo iz 3. koraka.
   Počakaj nekaj minut.
5. Prijava: `mcp-publisher login dns --domain whatsnextaction.com --private-key $(openssl pkey -in ~/.wna-mcp-key.pem -noout -text | grep -A3 "priv:" | tail -n +2 | tr -d ' :\n')`
6. V mapi `whatsnextaction/mcp-registry/` zaženi `mcp-publisher publish`.
7. Preveri: `curl "https://registry.modelcontextprotocol.io/v0/servers?search=whatsnextaction"`; javi mi rezultat.

## 2 · Smithery (smithery.ai)

1. Odpri smithery.ai → **Sign in** (z GitHub računom).
2. **Publish server** (oz. *Add server*) → izberi **Remote / URL**.
3. URL: `https://api.whatsnextaction.com/mcp`; ime **WhatsNextAction**; opis, logo in kategorijo **Productivity** prilepi iz "Besedila".
4. Ko Smithery preveri strežnik, te vpraša za prijavo (OAuth): prijavi se z **demo** računom, ne s svojim.
5. **Publish**; povezavo do strani mi pošlji.

## 3 · mcp.so

1. Odpri mcp.so/submit (prijava z GitHub, če jo zahteva).
2. Tip **Server**, ime **WhatsNextAction**, URL `https://whatsnextaction.com/help/connect-ai` (javnega repozitorija nimamo;
   če polje zahteva GitHub URL, mi javi in odpremo issue po njihovih navodilih).
3. Opis in tagi iz "Besedila" → **Submit**.

## 4 · Glama (glama.ai/mcp)

Glama sama indeksira odprtokodne strežnike z GitHuba; zaprtokodni oddaljeni strežnik dodaš ročno.
1. glama.ai → prijava → **MCP Servers** → **Add server** (oz. *Submit*).
2. Izberi **Remote server**, URL `https://api.whatsnextaction.com/mcp`, ostalo iz "Besedila".
3. Če ponudi samo GitHub repozitorij, se ustavi in mi javi.

## 5 · Claude Connectors Directory (Anthropic)

Največji učinek, a s pregledom. V ponedeljek samo preveriš dostop in pogledaš obrazec; oddamo, ko razvoj doda `title`.
1. Odpri **claude.ai/directory/manage** s svojim računom.
2. Če stran pove, da potrebuješ Team ali Enterprise organizacijo, se ustavi in mi javi (viri si nasprotujejo).
3. Sicer izberi **MCP connector** in poglej polja obrazca (ne oddajaj). Naredi posnetek zaslona in mi ga pošlji;
   besedila prilagodim natanko poljem.
4. Za pregled bodo zahtevali testni račun: ⬜ 3 spodaj.

## 6 · ChatGPT apps (OpenAI)

1. Odpri **platform.openai.com** → v meniju **Apps** (oz. *ChatGPT apps*).
2. Če zahteva preverjanje organizacije (Verify organization), ga začni; traja lahko nekaj dni.
3. V ChatGPT: **Settings → Apps → Advanced → Developer mode** vklopi, dodaj strežnik `https://api.whatsnextaction.com/mcp`,
   prijava z demo računom. Preizkusi dva ukaza: "What's on my Today list?" in "Add 'Call the dentist' to my inbox".
4. Posnetke zaslona **iz ChatGPT** shrani v Downloads (OpenAI zavrne posnetke, ki niso iz ChatGPT).
5. Obrazca še ne oddajaj; javi, kaj zahteva.

## 7 · Reddit (skupine)

Tvoj osebni račun, ne WNA. Prvih nekaj tednov samo pomoč, brez povezav.
1. Prijava na reddit.com (ali nov račun z imenom brez "WNA").
2. Pridruži se: **r/ClaudeAI**, **r/mcp**, **r/productivity**, **r/getdisciplined**.
3. V vsaki preberi pravila (desni stolpec), posebej o samopromociji; zapiši, ali imajo tedensko nit za promocijo.
4. Napiši 2–3 koristne komentarje (npr. kako nehaš pozabljati stvari, kako uporabljaš Claude za opravila), brez omembe WNA.
5. Ritem do novega leta: 2–3 komentarji na teden. Prva omemba WNA ⬜ po reviziji 7. 12.

---

## Besedila 📝 (pripravim v pon dopoldne, vse EN)

- Ime: WhatsNextAction
- Kratek opis (≤ 100 znakov), dolg opis, kategorija Productivity, tagi, logo 512 px, povezave (stran, vodič, zasebnost, podpora).
- Pravila: brez "AI-powered", brez "GTD app" kot imena; "built around the GTD methodology"; brez pomišljajev;
  ne naštevamo infrastrukture.

## Odprto ⬜

1. Potrditev plana (Vladimir).
2. `title` za vseh 78 orodij (razvoj, S) pred oddajo v Claude in ChatGPT.
3. Testni račun za recenzente: demo račun (že ima podatke) ali nov ločen račun, da posnetki ostanejo čisti.
4. Microsoft Copilot Connectors: verjetno Partner Center; preverim po ponedeljku.

Viri (13. 11.): claude.com/docs/connectors/building/submission · openai.com/index/developers-can-now-submit-apps-to-chatgpt ·
modelcontextprotocol registry (mcp-publisher, DNS) · geekflare.com/guides/mcp-server-directories ·
github.com/tangency-labs/solidcraft/issues/8648 (Gemini, Mistral, Microsoft)
