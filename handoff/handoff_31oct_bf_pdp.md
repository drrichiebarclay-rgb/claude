---
title: "MUTO Black Friday product page: Claim offer, sticky add to cart, compact mobile layout"
subtitle: "31 October 2026"
---

The Black Friday product page has been reworked on a duplicate of the live theme. **Nothing has changed on the live theme yet.** This note covers what changed, how to put it live, and what to check.

# Before you start

- **Preview theme:** "Black Friday | Claim offer + sticky bar | 31 Oct 2026", ID **203974869339**. It's a duplicate of the live theme ("Clone Of Live | Buy Box Redesign [31-08]") taken on 31 October at about 09:40.
  - <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203974869339>
  - <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=203974869339>
- **Files:** in `MUTO_BF_PDP_31Oct.zip`, and in GitHub at `shopify/bf-sticky/theme/` (repo drrichiebarclay-rgb/claude, branch `claude/laughing-bell-el19si`). The zip has the same folders as the theme (`assets/`, `sections/`, `snippets/`).
- **The product template is unchanged.** `templates/product.muto-nad-bf.json` is exactly as on live. Everything is added by two new sections, one in the header group and one in the footer group. Both only render on the `muto-nad-bf` template, except for the compact mobile header (see below).

# What's on the page

**Top bar (black, fixed to the top of the screen)**

- Desktop text: "Black Friday: 3 months for £99 (save 53%) + welcome kit worth £87 · Ends 30 Nov · Claim →".
- Phones: "3 months for £99 · Save 53% · Claim →", on one line down to 320px wide.
- **Claim** adds the 3-month plan to the cart and goes straight to `/checkout`.
  - It adds the first variant that sells on a 3-month Skio selling plan, read from the product, so it works on the main product and on -2.
  - If that plan is already in the cart, it doesn't add a second one.
  - If the add fails, the page scrolls to the plans instead.
- It replaces the template's own `bf_bar` section, which is hidden by CSS.

**Sticky add to cart (fixed to the bottom of the screen)**

- Desktop: product image and name, a plan picker and Add to cart. Phones: the picker and "Add" only.
- The picker and the plan cards stay in step: choosing in one chooses in the other.
- The button submits the page's own cart form, so Skio gets the same `id` + `selling_plan` as the main button and the cart drawer opens.
- The bar hides while the page's own Add to cart button is on screen.

**Buy box (phones and desktop)**

- Phones: the image is right at the top, edge to edge. The thumbnails are replaced by arrows, and swiping also works.
- Under the product name:
  - The descriptor now reads "A daily multi-nutrient with NAD⁺ support, built for 35+. Five supplements in one jar."
  - Under it, a green "Black Friday: 3 months for £99 · Ends 30 Nov" line.
  - The collaboration line, the old Black Friday box and "Choose your plan" are hidden.
- The plans are called "3-Month Supply" (**£99**, £210 crossed out) and "1-Month Supply" (**£49.99**, £70 crossed out).
  - The daily-cost pill lines up with the plan name.
  - The SAVE tags are turquoise, and the "Best value" pill is removed.
- The welcome kit heading reads "Welcome kit with your first box" and "Thank-you gifts in later boxes" reads "Future monthly gifts".
- The Add to cart buttons (page and sticky bar) are turquoise, #5efaff.
- "One-Time Purchase - £70 (no gifts)" is a plain bold text link under the Add to cart button.
- Removed: the stats bar, the Made in the UK / GMP / batch-tested badges (the third-party testing button takes their place) and the grey guarantee box.
- Under the button:
  - The delivery line is shorter and fits on one line on phones: "Arrives by [date] | Royal Mail Tracked 24h".
  - The text and lists are smaller.
- Folds:
  - "Who it's for" and "What it does" (now titled "Science-Backed Benefits") have new copy.
  - "money-back promise" reads "money-back guarantee" and "Major allergens" reads "Allergens".

**Rest of the page**

- Text is smaller on phones. On desktop, it's a little smaller than the site's usual size: the sections below the buy box are scaled to 93% with CSS `zoom`.
- "The best is still ahead." has a new line under it: "Your body changes in mid-life, and NAD+ Cellular Complex is the daily foundation built for it."
- The problem stat figures (~50%, ~80% and so on) are weight 500, the same as the headings.
- **New "MUTO vs the usual" comparison**, replacing the old table:
  - Our column is dark, with the jar photo and lime ticks. Multivitamin, greens powder and buying separately are the other columns.
  - On phones it scrolls sideways, with the feature names pinned on the left.

**Science page (`/pages/science`, template `page.science-simple`), redesigned: all white, science-led**

The template is replaced (`templates/page.science-simple.json`) and uses a new section, `sections/muto-sci.liquid` ("MUTO — Science (simple)"). It uses the same type system as the ingredients page: the site's uppercase weight-500 heading, mono eyebrows, hairline rules, 21px item titles and doses in the teal mono. There are no dark or grey panels.

The story is that what your body needs after 35 is different from what it needed at 20, and MUTO is formulated for that stage. Top to bottom:

1. **Intro:** "Your body after 35 needs something different." with an "At 20 / After 35" table, a turquoise "See the Black Friday offer" button and a link to the ingredients.
2. **Three shifts:** the NAD+ decline chart, marked at 35, then three numbered shifts: less NAD+, anabolic resistance, slower cell maintenance.
3. **Five jobs, one jar:** Energy, Recovery, Stress, Longevity and Immunity, each with its key doses in mono and the authorised claim.
4. **The numbers:** +51% NAD+ (footnoted as the NR study), 19 ingredients, 300mg NR, 0 proprietary blends.
5. **The same comparison** as the product page, on white with the site's heading. It's swapped into the empty `compare` slot by `muto-bf-head.liquid`.
6. **The scientific board:** the existing section, on white.
7. **Our research:** a statement and the four universities.
8. **Black Friday:** an outlined box with "3 months for £99", a turquoise button.
9. **Reviews:** unchanged.

In GitHub at `shopify/science-v2/`. After Black Friday, change the intro button and the offer box in Customize.

**Home page (`templates/index.json`):** the "Still training. Still working. Not done yet." athletes block is replaced, in the same place, by the product page's "Don't take our word for it." customer results videos (all 8). Nothing else on the home page changed. The file is in the zip under `templates/` and in GitHub at `shopify/home-videos/theme/templates/index.json`. If the live home page has been edited since 31 October, re-make this change in Customize instead of copying the file.

**Third-party testing pop-up (`sections/muto-test-results.liquid`), restyled to look clinical.** The markup, content and behaviour are the same; only the styles changed:

- a mono "Certificate of analysis" label and the batch as a mono reference
- a white side menu with a thin bar on the open tab
- normal-case headings
- results in tabular mono
- PASS as small teal badges
- hairline rules

It applies everywhere the pop-up opens. In the zip under `sections/`, and in GitHub at `shopify/tests-v2/`.

**Site-wide (all pages, phones and tablets under 990px):** a shorter header bar.

- About 44px instead of about 76px, with a smaller logo, caption and icons.
- Pages that start under the see-through header move up by the new height.
- This lives in `muto-bf-head.liquid`, outside the Black Friday check, so it applies on every page. See "After Black Friday".

# Files

| File | What it does |
|---|---|
| `sections/muto-bf-head.liquid` | **Header group.** The compact mobile header (site-wide); the science page's comparison and simplifications; on the BF template, loads all BF styles before the page is drawn, the button colour, and the top bar. |
| `sections/muto-bf-offer.liquid` | **Footer group.** The sticky add to cart bar; loads `muto-bf-layout.js` and `muto-bf-sticky.js`. |
| `snippets/muto-bf-bar.liquid` | The top bar markup (finds the 3-month variant + selling plan in Liquid); loads `muto-bf-extra.css`; renders the comparison and swaps it in; new copy for the statement line and the two folds. |
| `snippets/muto-bf-compare.liquid` | The comparison table. Edit rows here. |
| `assets/muto-bf-claim.js` | Claim: add the 3-month plan, go to checkout. |
| `assets/muto-bf-sticky.js` | The sticky bar (picker, sync with the plan cards, add to cart, show and hide). |
| `assets/muto-bf-layout.js` | Gallery arrows and swipe, moves the testing button, renames the plans for the sticky picker, "guarantee" and "Allergens" wording. |
| `assets/muto-bf-bar.css` | Top bar; hides the old bar; one-time purchase as a text line. |
| `assets/muto-bf-sticky.css` | Sticky bar. |
| `assets/muto-bf-compact.css`, `muto-bf-type.css` | Smaller, tighter type (phones and desktop). |
| `assets/muto-bf-layout.css` | Image first on phones, arrows, half-size BF box, badges out, delivery, guarantee and doctors blocks. |
| `assets/muto-bf-copy.css` | Copy done in CSS so it's right on first paint: descriptor, Black Friday line, plan names and prices, welcome kit heading, one-time line, reviews size, delivery line, image spacing. |
| `assets/muto-bf-extra.css` | Latest tweaks: stats bar out, one-time purchase order, "Future monthly gifts", desktop sizes, stat figure weight. |
| `assets/muto-bf-compare.css` | Comparison table styles. |
| `assets/muto-cmp-*.svg` (3) | Placeholder drawings for the comparison (multivitamin, greens tub, several pots). |
| `sections/header-group.json`, `sections/footer-group.json` | For reference: the live theme's groups with the two new sections added. **Don't overwrite live's groups with these** if live's header or footer has changed since 31 October. Add the sections in Customize instead (step 2 below). |

`sections/muto-header-compact.liquid` is on the preview theme but **unused**, left over from an earlier attempt. Don't copy it; delete it from the preview theme.

# Putting it live

**Option A: publish the preview theme.** This is the simplest, but only if nothing has been changed on the live theme since about 09:40 on 31 October. Anything edited on live after that (in Customize or the code editor) isn't in this theme and would be lost. Check the live theme's recent edits first.

**Option B: copy into the live theme.** Do this if live has changed since 31 October.

1. In the live theme's code editor, add the 18 files from the zip: everything in `assets/`, `snippets/`, and `sections/muto-bf-head.liquid` and `sections/muto-bf-offer.liquid`. Don't add the two `-group.json` files.
2. In Customize on live:
   - Open a BF product, e.g. `muto-nad-cellular-complex`.
   - **Header:** Add section → "MUTO — Black Friday head", and drag it to the **top** of the header group, above the announcement bars and the header.
   - **Footer:** Add section → "MUTO — Black Friday offer", below the footer.
   - Save.

# Check after publishing (on a phone and on desktop)

- [ ] **Claim**: tap it. The 3-month plan is added and checkout opens.
  - Check the first box is **£99** (Skio's intro price) and the welcome kit gifts are there.
  - Claim skips the cart drawer. If any gift is added by something in the drawer, it won't be added this way.
- [ ] Place test orders through the main button, the sticky bar (both plans) and the one-time purchase. Check the right variant and plan in each.
- [ ] Do the same on the -2 product.
- [ ] Load the page and check the old design doesn't flash: old text, prices, the BF box or thumbnails.
- [ ] Gallery arrows and swipe on a phone. The image sits right under the header with no gap or overlap; the 46px space is an estimate.
- [ ] Sticky bar: hides while the main button is on screen, and the picker and plan cards stay in step.
- [ ] The comparison appears in place of the old table and scrolls sideways on phones.
- [ ] **Site-wide compact header**: check the home page, other product pages and a content page on a phone, and that nothing is hidden under the header.
- [ ] Doesn't collide with chat or popup widgets at the bottom of the screen.
- [ ] Testing pop-up: open it from the product page and the ingredients page, then check all four tabs on a phone and on desktop.
- [ ] Home page: the results videos play, and the athletes block is gone.
- [ ] Science page: the new layout on phone and desktop, the comparison in place, and the board videos playing.

# Hard-coded in the CSS and scripts (update if the offer changes)

- **Prices** in `muto-bf-copy.css`: £99 / £210 (3-month), £49.99 / £70 (1-month), "One-Time Purchase - £70". The page's own CSS also draws the daily pills (£1.10 and £1.79 a day).
- **Offer wording:**
  - Top bar: `muto-bf-bar.liquid`.
  - Black Friday line ("Ends 30 Nov"): `muto-bf-copy.css`.
  - Sticky bar line ("53% off your first order"): `muto-bf-offer.liquid`.
- **Copy swapped in by script** (statement line, "Who it's for", "Science-Backed Benefits"): `muto-bf-bar.liquid`. To make it permanent, edit the template's settings in Customize.
- **Comparison** rows, prices and footnote: `muto-bf-compare.liquid`.
  - The greens powder price "£40–80" is an estimate. Please confirm it.
  - The three drawings are placeholders until real photos are uploaded to Content → Files. They should show no other brand's logos, and you need the rights to use them.
- **Health claims:** check that the "Science-Backed Benefits" lines are within the UK nutrition and health claims rules, especially "stay well through winter".

# After Black Friday

- Delete "MUTO — Black Friday offer" from the footer group.
- In `muto-bf-head.liquid`, delete the Black Friday part (the `{%- if template.suffix == 'muto-nad-bf' ... -%}` block). Keep the first `<style>` block if you want to keep the compact mobile header site-wide; otherwise delete the section.
- The comparison's footnote ("Your first 3-Month Supply is £99…") also shows on the science page; update or remove it when the offer ends.
- Switch the two products back to `muto-nad-trust`, as noted in `product.muto-bf-redirect.json`.
