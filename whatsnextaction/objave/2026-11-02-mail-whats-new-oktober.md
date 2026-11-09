# WNA · What's new: oktober (mesečni broadcast)

- Kanal: e-pošta obstoječim uporabnikom, množično pošiljanje iz admina (pošlje Vladimir)
- Pošiljatelj: Vladimir Hozjan <hello@whatsnextaction.com>
- Datum: 📝 pon 2. 11. 2026 (prvi delovni dan po koncu meseca); ⬜ potrditev
- Ritem ✅ (Vladimir, 26. 10.): What's new je broadcast obstoječim uporabnikom, enkrat na mesec, samo večje stvari
- Vsebina: izidi oktobra iz `~/Documents/wna_orchestration/roadmap.md` (FEAT-003, -050, -017, -051, -053, -055, -056, -059, -060, -061, -063, -064, -065, -066; dopolnjeno 2. 11.: FEAT-005, -068, -069, -070, -071/-078/-079, -072, -080); izpuščeno: interno (deploy, testi, admin, cene, logotip, popravki napak, offline sync API za native aplikacije), pristajalna stran, prazna stanja, uvodni ogled
- Status: 📝 osnutek (Claude, 26. 10.; dopolnjen 2. 11. z izidi 27. 10.–1. 11.), ⬜ potrditev; ⬜ preveri, da so vse naštete funkcije na produkciji; žive liste na produkciji ✅ (Vladimir, 2. 11.); navodila za MCP: v mailu samo napotilo na Settings → AI Apps ✅ (Vladimir, 2. 11.) · ✅ **poslano pon 2. 11.** (Vladimir, iz admina, HTML spodaj)

Pravila: brez pomišljajev, brez "GTD app", brez "AI-powered"; admin nima placeholderjev, zato "Hi," brez imena.

---

**Subject:** What's new in WhatsNextAction: October

Hi,

A lot has happened since the launch on October 9. Here are the bigger things.

**An assistant that does the work**

- Tell the AI assistant what you want in plain words, like "move everything about the trip into a new project", and it does it, with a list of every change. Open it with the AI button or Cmd+K. It always asks before it trashes or deletes anything. Every plan gets monthly credits, and the models run in the EU.
- Prefer your own AI app? Connect Claude, ChatGPT or any app that supports MCP, and it can read and update your lists with your permission. Copy the address from Settings, AI Apps and add it as a connector.

**Your calendar and your files, in Google**

- Google Calendar sync. Anything you schedule shows up in Google Calendar, and changes made there come back. WhatsNextAction can also create its own calendar in your Google account, and events you add there become actions. (Pro and Team)
- Google Drive storage. Keep attachments and reference files in your own Google Drive. Switch between Local and Google Drive in Reference.

**Capture from anywhere**

- Photo, voice and file in Quick Add and the Inbox. Snap a receipt, record a thought, drop in a PDF. (Pro and Team)
- Email to Inbox now keeps the attachments.
- On Android, share anything to WhatsNextAction from any app once it is installed on your home screen.
- No signal? Capture still works. Items wait on your device and go out when you are back online.

**Plan a project**

- A brainstorm canvas for every project. Throw in ideas as a mind map, then turn the ones you want into actions in one go.
- Project templates. Save any project as a template and start the next one with all its actions already in place.
- Horizons. Write down your areas of responsibility, goals, vision and purpose on one page, and link each project to the area and goal it serves.

**Always up to date**

- Lists update live. Change something on your phone and it shows up on your laptop right away, no refresh needed.
- Notifications in your browser, next to email. Choose what you get in Settings, Notifications.
- Sign in with Apple, next to Google.

**Find and fix faster**

- Search everything from one box.
- Undo. Completed or trashed something by mistake? Click Undo or press Ctrl+Z.
- On desktop, Cmd+K (Ctrl+K on Windows) opens the command palette. Press ? to see every shortcut.
- On your phone, swipe right to complete, swipe left to trash, and pull down to refresh.

**Weekly Review**

- A progress bar through the six steps, and a look at the last 7 and the next 14 days before you finish.

As always, the feedback bubble in the app goes straight to me.

Vladimir
WhatsNextAction

## HTML za admin

Predloga iz admina (logo `cid:logo`), vsebina zgoraj; kopiraj celoten blok.

```html
<html><head><meta charset="utf-8"></head><body style="margin:0;padding:0;"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f9fafb;padding:40px 16px;"><tr><td align="center"><table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background-color:#ffffff;border:1px solid #e5e7eb;"><tr><td style="padding:28px 32px 16px;"><span style="font-family:'Montserrat',Arial,sans-serif;font-size:20px;font-weight:bold;color:#0e7490;"><img src="cid:logo" alt="" width="24" height="24" style="vertical-align:middle;margin-right:8px;"> WhatsNextAction</span></td></tr><tr><td style="padding:0 32px;"><div style="border-top:1px solid #e5e7eb;"></div></td></tr><tr><td style="padding:28px 32px;font-family:'Montserrat',Arial,sans-serif;font-size:15px;color:#1f2937;line-height:1.7;"><h2 style="font-family:'Montserrat',Arial,sans-serif;font-size:22px;font-weight:bold;color:#1f2937;margin:0 0 8px;">What's new in October</h2><p style="margin:0 0 16px;color:#1f2937;">Hi,</p><p style="margin:0 0 16px;color:#1f2937;">A lot has happened since the launch on October 9. Here are the bigger things.</p><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">An assistant that does the work</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">Tell the AI assistant what you want in plain words, like "move everything about the trip into a new project", and it does it, with a list of every change. Open it with the AI button or Cmd+K. It always asks before it trashes or deletes anything. Every plan gets monthly credits, and the models run in the EU.</li><li style="margin:0 0 8px;">Prefer your own AI app? Connect Claude, ChatGPT or any app that supports MCP, and it can read and update your lists with your permission. Copy the address from Settings, AI Apps and add it as a connector.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Your calendar and your files, in Google</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">Google Calendar sync. Anything you schedule shows up in Google Calendar, and changes made there come back. WhatsNextAction can also create its own calendar in your Google account, and events you add there become actions. (Pro and Team)</li><li style="margin:0 0 8px;">Google Drive storage. Keep attachments and reference files in your own Google Drive. Switch between Local and Google Drive in Reference.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Capture from anywhere</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">Photo, voice and file in Quick Add and the Inbox. Snap a receipt, record a thought, drop in a PDF. (Pro and Team)</li><li style="margin:0 0 8px;">Email to Inbox now keeps the attachments.</li><li style="margin:0 0 8px;">On Android, share anything to WhatsNextAction from any app once it is installed on your home screen.</li><li style="margin:0 0 8px;">No signal? Capture still works. Items wait on your device and go out when you are back online.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Plan a project</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">A brainstorm canvas for every project. Throw in ideas as a mind map, then turn the ones you want into actions in one go.</li><li style="margin:0 0 8px;">Project templates. Save any project as a template and start the next one with all its actions already in place.</li><li style="margin:0 0 8px;">Horizons. Write down your areas of responsibility, goals, vision and purpose on one page, and link each project to the area and goal it serves.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Always up to date</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">Lists update live. Change something on your phone and it shows up on your laptop right away, no refresh needed.</li><li style="margin:0 0 8px;">Notifications in your browser, next to email. Choose what you get in Settings, Notifications.</li><li style="margin:0 0 8px;">Sign in with Apple, next to Google.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Find and fix faster</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">Search everything from one box.</li><li style="margin:0 0 8px;">Undo. Completed or trashed something by mistake? Click Undo or press Ctrl+Z.</li><li style="margin:0 0 8px;">On desktop, Cmd+K (Ctrl+K on Windows) opens the command palette. Press ? to see every shortcut.</li><li style="margin:0 0 8px;">On your phone, swipe right to complete, swipe left to trash, and pull down to refresh.</li></ul><h3 style="font-family:'Montserrat',Arial,sans-serif;font-size:16px;font-weight:bold;color:#0e7490;margin:24px 0 8px;">Weekly Review</h3><ul style="margin:0 0 16px;padding-left:20px;color:#1f2937;"><li style="margin:0 0 8px;">A progress bar through the six steps, and a look at the last 7 and the next 14 days before you finish.</li></ul><p style="margin:24px 0 16px;color:#1f2937;">As always, the feedback bubble in the app goes straight to me.</p><p style="margin:0;color:#1f2937;">Vladimir<br>WhatsNextAction</p></td></tr></table><table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;"><tr><td style="padding:24px 32px;text-align:center;font-family:'Montserrat',Arial,sans-serif;font-size:12px;color:#9CA3AF;line-height:1.6;">&copy; 2026 WhatsNextAction &middot; Your personal productivity companion</td></tr></table></td></tr></table></body></html>
```
