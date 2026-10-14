# MUTO landing pages: files for the live theme

19 files. Copy them into the live theme (Clone Of Live | Buy Box Redesign [31-08], ID 200736047451),
sections and the stylesheet first, then the 7 templates.

Pages already created in Shopify (published, hidden from search), each set to its template:

| Page | Template | Persona |
|---|---|---|
| /pages/not-done-yet | page.lp-mp1 | MP1 Slowing Competitor |
| /pages/sharp-all-day | page.lp-mp2 | MP2 Afternoon Fader |
| /pages/one-protocol | page.lp-mp3 | MP3 Stack Doubter |
| /pages/live-better-for-longer | page.lp-mp5 | MP5 Wake-Up Call |
| /pages/full-output | page.lp-hp-energy | High performer 30-40: energy |
| /pages/ready-for-the-next-session | page.lp-hp-recovery | High performer 30-40: recovery |
| /pages/one-recovery-budget | page.lp-hp-stress | High performer 30-40: stress |

MP1, MP2, MP3 and MP5 buttons link to /products/muto-nad-cellular-complex-2; the three high-performer pages link to /products/muto-nad-cellular-complex.

## Option A: Shopify CLI (one command, from this folder)

    shopify theme push --theme 200736047451 --nodelete \
      --only "sections/muto-lp-*.liquid" --only "assets/muto-lp.css" --only "templates/page.lp-*.json"

## Option B: Shopify admin

Online Store → Themes → live theme → … → Edit code.
1. Sections → Add a new section, for each muto-lp-*.liquid (11 files), paste the contents, save.
2. Assets → Add a new asset → muto-lp.css, paste, save.
3. Templates → Add a new template → page → name lp-mp1 (then lp-mp2, lp-mp3, lp-mp5, lp-hp-energy, lp-hp-recovery, lp-hp-stress), paste the JSON, save.

The three high-performer pages also use `muto-home-results` (the customer videos), which is already on the live theme; nothing to copy for it.

Check each page on mobile and desktop once live.
