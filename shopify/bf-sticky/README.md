# Black Friday: Claim offer + sticky plan bar + compact phone layout

**Dev handoff:** `handoff/handoff_31oct_bf_pdp.md` (also `handoff/MUTO_Dev_Handoff_BF_PDP_31Oct2026.docx` and the zip `handoff/MUTO_BF_PDP_31Oct.zip`). It is the up-to-date description; the notes below are the earlier build log.

On theme **"Black Friday | Claim offer + sticky bar | 31 Oct 2026"** (ID 203974869339), a duplicate of the live theme taken 31 Oct.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203974869339

## What's on the theme (`theme/`)
Two sections, both only render on the `product.muto-nad-bf` template:

- **Header group: `sections/muto-bf-head.liquid`**. It loads every Black Friday stylesheet before the page is drawn, so the old design never flashes. It also draws the black top bar (`snippets/muto-bf-bar.liquid`). Its **Claim** link adds the 3-month plan and goes straight to checkout (`assets/muto-bf-claim.js`).
  - `muto-bf-bar.css`: the top bar, the hidden old bar, the one-time purchase as a text line.
  - `muto-bf-sticky.css`: the sticky plan bar.
  - `muto-bf-compact.css` and `muto-bf-type.css`: smaller, tighter type. Sections below the buy box are scaled down.
  - `muto-bf-layout.css`: image first on phones, arrows instead of thumbnails, testing button in place of the badges, smaller delivery, guarantee and doctors blocks.
  - `muto-bf-copy.css`: all copy changes, done in CSS so they're right on first paint. That covers the descriptor, the green Black Friday line, "3-Month Supply" and "1-Month Supply", £99 vs £210 and £49.99, the welcome kit heading and the one-time line.
- **Footer group: `sections/muto-bf-offer.liquid`**. The sticky plan bar (`assets/muto-bf-sticky.js`), plus `assets/muto-bf-layout.js` for the gallery arrows, moving the testing button, and plan names in the sticky picker.

`live-snapshot/` holds the live template, buy section and CSS these were built against.

## After Black Friday
In Customize, delete "MUTO — Black Friday head" from the header and "MUTO — Black Friday offer" from the footer.
