---
title: "MUTO landing pages: handover"
subtitle: "16 October 2026"
---

There are nine Meta landing pages, one for each persona, plus a "7 reasons" advertorial. All nine **pages already exist in Shopify**: published, hidden from search, and each assigned its template. What's left is **copying 25 theme files onto the live theme**. Some of them are already on live, but several are out of date, which is why parts of the live pages look broken today.

# Before you start

- **Files:** `shopify/lp-mp1/live-push` in GitHub (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`): <https://github.com/drrichiebarclay-rgb/claude/tree/claude/faq-page-shopify-redesign-hbqcg8/shopify/lp-mp1/live-push>. The same files are in `MUTO_landing_pages_live_theme.zip`.
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Preview first:** every page works on the 3M refill plan theme (ID 202682564955). Add `?preview_theme_id=202682564955` to any URL below.
- **Order:** sections and the stylesheet first, then the templates. A template that refers to a section the theme doesn't have yet is rejected.

# The nine pages

| URL | Template | Who it's for | Buttons go to |
|---|---|---|---|
| /pages/not-done-yet | `page.lp-mp1` | MP1 Slowing Competitor, 45–60 | -2 |
| /pages/sharp-all-day | `page.lp-mp2` | MP2 Afternoon Fader | -2 |
| /pages/one-protocol | `page.lp-mp3` | MP3 Stack Doubter | -2 |
| /pages/take-your-baseline | `page.lp-mp4` | MP4 Stuck Scorekeeper, 40–60 | main |
| /pages/live-better-for-longer | `page.lp-mp5` | MP5 Wake-Up Call | -2 |
| /pages/why-your-stack-isnt-adding-up | `page.lp-stack` | Broad persona, "7 reasons" advertorial | main |
| /pages/full-output | `page.lp-hp-energy` | High performer 30–40: energy | main |
| /pages/ready-for-the-next-session | `page.lp-hp-recovery` | High performer 30–40: recovery | main |
| /pages/one-recovery-budget | `page.lp-hp-stress` | High performer 30–40: stress | main |

"-2" is `/products/muto-nad-cellular-complex-2`; "main" is `/products/muto-nad-cellular-complex`. The ad links are the page URLs above.

# What's on live today, and what's missing

I compared the live theme with the package on 16 October:

| File | On live? | Action |
|---|---|---|
| `assets/muto-lp.css` | Yes, but an older copy (14 Oct) | **Replace.** This is why the 90-day timeline on take-your-baseline shows as a plain list, and why the store header still appears. |
| `sections/muto-lp-article-hero`, `-article`, `-review-cards`, `-reasons` | No | **Add.** Used by the advertorial only. |
| `sections/muto-lp-hero-2`, `muto-lp-faq-2` | Yes, your copies | **Replace** with the package versions. Same names you chose. |
| `sections/muto-lp-timeline`, `-trust`, `-problem`, `-benefits`, `-value`, `-offer`, `-formula`, `-experts`, `-bar` | Yes, older copies | **Replace.** |
| `templates/page.lp-mp1` … `lp-hp-stress` (8 files) | Yes, older copies | **Replace.** The only differences from live are the new MP4 hero photo and the HP image fixes. I checked: nothing you edited on live is lost, except the "allow transparent header" option on `hero-2`, which isn't needed now that the header is hidden. |
| `templates/page.lp-stack.json` | No | **Add.** |

## Don't touch the older `muto-lp-hero` and `muto-lp-faq`

The live theme has older sections from 5 October called `muto-lp-hero.liquid` and `muto-lp-faq.liquid`, used by earlier pages. Thanks for spotting the clash and renaming mine. The package now uses your names (`muto-lp-hero-2`, `muto-lp-faq-2`) everywhere, so it never writes to the older two. The other old sections (`-comparison`, `-credibility`, `-evidence`, `-statement`, `-testimonials`, `-footer`) aren't in the package either.

# How to copy

**Option A: Shopify CLI** (one command, from the `live-push` folder):

    shopify theme push --theme 200736047451 --nodelete \
      --only "sections/muto-lp-*.liquid" --only "assets/muto-lp.css" --only "templates/page.lp-*.json"

`--nodelete` means nothing on live is removed, and the older `muto-lp-hero` and `muto-lp-faq` aren't in the folder, so they stay as they are.

**Option B: Shopify admin.** Online Store → Themes → live theme → … → Edit code:

1. Sections: add or replace the 15 `muto-lp-*.liquid` files from the package.
2. Assets: replace `muto-lp.css`.
3. Templates: add or replace the 9 `page.lp-*.json` files.

# Things to know

## Header removed on the landing pages

The store header and the cyan announcement bar are hidden on every page that uses a `page.lp-*` template. One rule at the top of `muto-lp.css` does it:

    body[class*="template-lp-"] .shopify-section-group-header-group{display:none !important}

It relies on the class `theme.liquid` already puts on `<body>` (`template-lp-mp4` and so on), so no layout change is needed, and the rest of the site keeps its header. The footer stays. To bring the header back on these pages, delete that line.

## One stylesheet for every page

All 15 sections load `muto-lp.css`. Whenever a section changes, replace the stylesheet with it. An older stylesheet with newer sections is what broke the timeline.

## Images

Every image is already in Shopify Files: the persona photos from the -2 page, the athlete shots, the kit photo (`muto-lp-kit-hero.jpg`) and the new MP4 hero (`muto-lp-mp4-hrv-watch.jpg`). Templates refer to them by file name, so you don't need to upload anything. To change a photo, use the theme editor's image picker on that section; it overrides the built-in one.

## Reviews

The "What customers say" block is the reviews.io widget (`custom-reviews`), so every review in it is real. The quotes in the review cards, the timeline and the featured-review boxes are real customer words from the product page.

## SEO

Each page has its own title and description, set in the page's Search engine listing. All nine are hidden from search (`seo.hidden`), because they're for paid traffic. The hero sections also output WebPage and Product structured data, and the FAQ sections output FAQPage data. The advertorial outputs Article data, with Richie as the author.

## Editing copy

Everything can be edited in the theme editor. The source of truth is the builder scripts in `shopify/lp-mp1`:

- `make_lp.py` builds MP1.
- `build_personas.py` builds MP2–MP5 and the three high-performer pages.
- `make_advertorial.py` builds the advertorial.

If you edit a page in the editor, tell me, and I'll pull the change into the scripts so it isn't lost on the next rebuild.

# Before ads go live (for Richie)

- [ ] **Founder quote on the advertorial**: "The interesting question isn't which supplement is best…", attributed to Richie Barclay, PhD. Written in your voice; approve or reword.
- [ ] **"Every batch third-party tested"** in the advertorial's comparison table and the trust strips: confirm it's accurate. Name the lab if you'd like it shown.
- [ ] **Refund wording** on take-your-baseline ("tell us and we'll refund you" on subscriptions by day 90): confirm it matches the guarantee terms.
- [ ] **Prices** in the advertorial cost table (£157.50 a month bought separately, £1,170 a year) were checked on 14 October; re-check before launch.
- [ ] **Button destination** for MP1, MP2, MP3 and MP5: these still go to -2. Should they go to the main product page like the others?
- [ ] **Claims check** of the new headlines by a regulatory adviser, as the strategy doc recommends.

# Check after publishing

1. Open each page on a phone. There should be no store header or announcement bar. The sticky offer bar sits at the bottom and hides while an offer section is on screen.
2. On **take-your-baseline**: the hero is the HRV watch photo, and "Run a proper 90-day test" shows three cards (Day 0, Day 30, Day 90), not a numbered list.
3. On **why-your-stack-isnt-adding-up**, check these appear:
   - the dark article hero with Richie's photo and the author badge;
   - the swipeable review cards;
   - seven numbered reasons;
   - the dose grid ("19");
   - the cost table (£60 vs £157.50);
   - the icon grid of 11 pots;
   - the comparison table;
   - the advisory board.
4. On the **three high-performer pages**: the "Here's how you'll know" timeline and the customer videos appear.
5. Click a button on each page and check it lands on the right product (table above), with the welcome offer in the buy box.
6. Open any older page built with the 5 October `muto-lp-*` sections and check nothing has changed.
