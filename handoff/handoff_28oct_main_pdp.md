---
title: "MUTO main product page: new template for the main URL and -2"
subtitle: "28 October 2026"
---

The main product page and -2 move to a new template, **`muto-nad-trust`**. It is today's `muto-nad-v2` page, with every section kept: buy box, "On this page" menu, "Five jobs. One daily jar.", the ingredient library, comparison, timeline, "How to take it", FAQs. New blocks slot in between: the statement, four problem stats, the science board, standards, customer videos, reviews and the founder. The Black Friday pre-sale box and its MUTO10 code are removed.

That means **7 new files to add**, **template changes on 2 products**, **removing the pre-sale box from 3 live templates** and **2 announcement-bar messages to take down** and **1 cart setting for the new travel vial**. No existing theme file is overwritten.

# Before you start

- **Files:** `MUTO_Main_PDP_28Oct2026.zip`, also in GitHub at `handoff/main-pdp/` (repo drrichiebarclay-rgb/claude, branch `claude/gifted-wozniak-e239h5`).
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Preview:** the page is already on the 3M refill plan theme (ID 202682564955):
  <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955&view=muto-nad-trust>
- **Your edits are kept.** Everything except the new blocks is copied from the **live `muto-nad-v2` template as of 28 October**: the buy box and its `easy_read` block, the menu, benefits, ingredient library, comparison, timeline, "How to take it", the FAQs and the test-results panel. If you've edited `muto-nad-v2` since, tell Richie before copying, and the template will be rebuilt from your latest version.

# Step 1: add the 7 files, in this order

Every file is new; nothing with these names exists on live.

| File | What it is |
|---|---|
| `assets/muto-crea-trust.css` | Styles for the five new blocks |
| `sections/muto-crea-statement.liquid` | "Not ready to slow down." band |
| `sections/muto-crea-stats.liquid` | "The problem": four stat boxes with sources |
| `sections/muto-crea-standards.liquid` | "Checked, not taken on trust." four standards cards |
| `sections/muto-crea-reviews.liquid` | "What our community say." rotating reviews (20) |
| `sections/muto-crea-founder.liquid` | Founder band |
| `templates/product.muto-nad-trust.json` | The page itself |

Add the asset and the sections first. A template that uses a section is rejected if the section isn't there yet.

With the Shopify CLI, from the unzipped folder:

    shopify theme push --theme 200736047451 --nodelete \
      --only "assets/muto-crea-trust.css" --only "sections/muto-crea-*.liquid" \
      --only "templates/product.muto-nad-trust.json"

Or in admin: Online Store → Themes → live theme → … → Edit code. Add a new asset, then each new section, then a new product template named `muto-nad-trust`, and paste each file in.

All the other sections the page uses are already on live and unchanged: `muto-pdp-v2-buy`, `muto-section-nav`, `muto-benefit-cards`, `muto-home-board`, `muto-ingredient-library`, `muto-home-results`, `muto-chapter`, `muto-timeline`, `muto-crea-faq`, `custom-reviews`, `muto-test-results`.

# Step 2: change the product templates

Do this **after** step 1. In Shopify admin, go to Products → product → Theme template.

| URL | Product | Template now | Template after |
|---|---|---|---|
| `/products/muto-nad-cellular-complex` (main) | NAD+ Cellular Complex | `muto-nad-v2` | **`muto-nad-trust`** |
| `/products/muto-nad-cellular-complex-2` | NAD+ Cellular Complex 2 | `muto-nad-v2` | **`muto-nad-trust`** |

Nothing is deleted. `muto-nad-v2` stays in the theme, so either page can be switched back in one click.

# Step 3: remove the Black Friday pre-sale box from live

**MUTO10 was ended on 28 October at 17:19.** It no longer works at checkout. The dark "BLACK FRIDAY PRE-SALE" box still says the code "is applied automatically at checkout", and its script still tries to apply MUTO10 on page load. It's on three live templates:

- `product.muto-nad-v2` (main and -2 until step 2 is done)
- `product.muto-nad-performance` (-3)
- `product.muto-nad-45` (no product uses it now)

In each one, open the `easy_read` Custom Liquid block and delete three things:

1. In the `<style>`: from `/* Black Friday pre-sale box, above the plans */` up to (not including) `/* -2 page only:`.
2. In the `<script>`: from `/* Black Friday pre-sale: real countdown` down to the end of that function, the line `if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();` and the `})();` after it.
3. The line `<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"></div>`.

The new `muto-nad-trust` template already has all three removed.

**Quick stopgap** if step 3 can't be done straight away: Online Store → Customize → Theme settings → Custom CSS, add `.mc-bf:has(.mc-bf__clock){display:none !important}`. That hides the box on every page. The script still runs, but MUTO10 is ended, so nothing is applied.

# Step 4: the travel vial (3-month plan, first order)

A free **travel vial** now comes with the first order on the 3-month plan only, shown with **£10 crossed out**, like the other gifts.

- **Product: already created.** "Travel Vial", handle `muto-travel-vial-free`, SKU `TRAVEL-VIAL`, £0 with a £10 compare-at, unlisted, stock not tracked, published to the Online Store. Its photo is on the product, so it shows in the cart.
- **Cart: one setting to change on the live theme.** Online Store → Customize → Theme settings → the cart giveaway settings → the 3-month free products list (`cart_free_product_3m`). Add **Travel Vial** (`muto-travel-vial-free`) to the list, alongside the bottle, socks, creatine and Garmin entry. The theme's giveaway script then adds it to the cart at £0 whenever the 3-month NAD+ subscription is in it. The cart drawer lists it under "Your free welcome gifts" with £10 struck through and "Free". Subscription renewals don't carry cart gifts, so it only ships with the first order.
- **Page: in the template.** The welcome kit shows a "Travel vial" tile (£10 struck through) and an itemised row on the quarterly plan only. The quarterly kit is now worth **£87** (was £77) in the plan's bullet and the bar above the plans.
- **Also say £87** wherever else the quarterly kit is quoted at £77, e.g. the announcement bar's "£77 OF FREE GIFTS WITH EACH ORDER" if that's meant to be the quarterly figure.

# Step 5: the announcement bar

The scrolling announcement bar at the top of every page (section `muto-announce` in the header group) still advertises the ended offer: **"EXTRA 10% OFF OUR QUARTERLY PLAN"** and **"ENDS ON 28.10.26"**. Remove those two messages (Customize → Header → announcement bar). The other three ("LIMITED NEW CUSTOMER OFFER", "£77 OF FREE GIFTS WITH EACH ORDER", "FREE ULTRAPURE CREATINE, BOTTLE, SOCKS, JAR, EBOOK") can stay.

# What's on the new page

In order, below the buy box. **New** blocks are in bold; the rest is `muto-nad-v2` as it is on live today.

1. "On this page" menu (pins to the top as you scroll, as on live), with four new links: **Problem**, **Standards**, **What people say** (the videos) and **Founder**, 12 links in page order
2. **Statement:** "Not ready to slow down." / "The next-generation multi-nutrient, built for what your body needs in your 40s and 50s." / tag "Got a wearable? Track the shift over 90 days."
3. **The problem:** small mono label "The problem", heading "Your biology shifts. Most supplements don’t." Four cards in the standards style (number, lime topic tag, big figure, cyan rule, one line): **57%** of supplements tested didn’t match their label (Crawford et al., JAMA Network Open 2022) · **3–8%** muscle lost every decade after 30 (Volpi et al., Curr Opin Clin Nutr Metab Care 2004) · **50%** less NAD+ by middle age (Massudi et al., PLoS ONE 2012, analysed in Peluso et al., Nutrients 2022) · **~50%** drop in muscle mitochondrial capacity and energy between your 40s and late 60s (Conley et al., Journal of Physiology 2000). Sources in a small line underneath.
4. **Benefits:** the live five cards, with a new heading: "Benefits built on published science." (small line above: "Five jobs. One daily jar."), and a new line under it: "What you need after 35. Your biology shifts. What you need evolves."
5. **Science board:** "Six scientists put their name to MUTO.", compact row, white background.
6. **Standards:** four cards. Card 1 has the "View third-party testing results" button, which opens the certificate panel (batch 2333).
7. **Customer videos:** "Don't take our word for it.", 8 videos in a row that scrolls: Kate Bright, David Mercado, Lucy Halliday, Harry Insley, Adam Facey, Max Richards, Adam Hamilton, Yolanda King. Ellen Gray's video is removed, and so is the footnote under the row.
8. **Reviews:** "What our community say.", 20 five-star REVIEWS.io reviews that rotate every 6 seconds, with "4.8 from 103 reviews".
9. "Every ingredient has a job." ingredient library
10. **Founder:** Dr Richie Barclay, PhD: cell biologist, Harley Street nutritionist for 13 years, former cricketer and tennis player.
11. Comparison (heading now "See the difference for yourself."), "What you can expect over time." timeline, "How to take it.", FAQs (all 10 from live), REVIEWS.io widget.

Also changed from `muto-nad-v2`:

- **Under the buy button:** the serving line, "Not another multivitamin…" copy and the quote slider are blanked or hidden (not deleted).
- **Buy button** in brand green **#6BCE7F**, charcoal label, with a second line inside it: a shield and "90-day money-back guarantee".
- **Under the subhead:** "In collaboration with seven leading scientists from world-leading research institutions, including four universities in the UK and Australia."
- **Rotating stats** under the button, every 3.5 seconds: "94% reported better recovery", "92% reported improved energy", "88% bounce back quicker", with a black bar that fills left to right to each figure. Set in `STATS` in `make_trust.py`.
- **Delivery line** under the button: "● Ready to ship — arrives by **Thu 29th Oct** | [Royal Mail logo] Tracked 24hr delivery". The date is the next calendar day in UK time, or the day after from the **9pm cut-off**, set by a script that updates while the page is open. Before the script runs it says "arrives tomorrow". The logo is `theme/assets/royal-mail-logo.png`, embedded in the template (nothing to upload).
- **"How it helps" list** in the buy box is hidden on phones as well as desktop.
- **Phones:** the billing line under each plan name is smaller (12px) so it fits, and the delivery line is centred.
- **Phones, whole page:** a smaller, tighter scale below 750px. Headings 28px (the statement 32px), lines under headings 15px, body 14-15px, smaller cards with less padding, benefit cards narrower, problem stats two by two, section spacing 40px. The new bands' sizes are in `muto-crea-trust.css`. The live sections' sizes are in the template's `head_styles` block, so they only change on this page.
- **No sticky add-to-cart bar.** The `sticky` section isn't in this template, so nothing slides in at the top or bottom of the page as you scroll.
- **Backgrounds:** no gradient washes. Almost every band is flat white. Brand sage grey (#C8D2CF) is used only on "What our community say" and the comparison (as on live). "How to take it" and the ingredient library are white too. Set in the `head_styles` block at the top of the template.

## How it's built

- **Template-only** apart from the five new sections and their stylesheet. The page's own styles are in a Custom Liquid block called `head_styles` at the **top** of the template, so the buy box is styled from the first paint (with them at the bottom, the old design flashed on load). Its scripts stay in `easy_read` and `bands` at the bottom. A Custom Liquid block called `early`, straight after the buy box, opens the page on the Quarterly plan and adds the subhead, the testing-results button, the collaboration line, the rotating stats and the delivery line before the first paint, so nothing jumps on load (it used to flip from Monthly to Quarterly once the page had loaded). The same scripts at the bottom stay as a safety net. The `bands` scripts (delivery line, rotating stats, collaboration line, video drag) run again after `shopify:section:load`, so they survive the theme editor re-drawing the buy box.
- **Source:** `shopify/pdp-trust/make_trust.py` builds the template. Change copy there and rebuild rather than editing by hand, or tell Richie about manual edits so they aren't lost on the next rebuild.

# Page speed (theme-wide, for you to do)

The template now does its part: the REVIEWS.io widget loads only when the reader nears it (or once the page is idle), the two Neue Haas weights are preloaded, and nothing in the buy box moves after first paint. What's left is in `layout/theme.liquid` and the app embeds, which every page shares, so it's yours to change and test:

1. **Render-blocking scripts in `<head>`.** `jquery-min.js`, `slick-min.js` and `custom.js` load with no `defer`, so a phone downloads and runs ~130 KB of script before it can draw anything. Add `defer` to all three (they keep their order). First search the theme for inline scripts that call `$(` or `jQuery(` straight away rather than on `DOMContentLoaded`. Those would break, so wrap them first.
2. **The OpenAI pixel** is initialised with `debug: true`. Set it to `false`.
3. **The Usermaven script** sits before `<head>`. Move it inside `<head>` (it already loads deferred).
4. **App embeds** (Online Store → Customize → App embeds). REVIEWS.io core and rating snippet, Klaviyo, Elevar, Triple Whale, Microsoft Clarity, Alia and Pandectes all load on every page. Turn off any that aren't used. Clarity and Alia are the usual candidates to load only on key pages.
5. **Preload the page's stylesheets.** On product pages, add `<link rel="preload" as="style">` in `<head>` for `muto-crea.css` and `muto-home.css`. The buy box links them from the body, so the browser finds them late.
6. **Measure before and after** with PageSpeed Insights (mobile) on the main URL. Watch LCP (the first product photo, already marked high priority) and Total Blocking Time.

# Check after publishing

1. **Main URL and -2:** the buy box and every section from today's page are there (menu, Five jobs, ingredient library, comparison, timeline, How to take it, FAQs), with **no** dark Black Friday box above the plans.
2. **Add to cart** on the Quarterly plan, the Monthly plan and one-time purchase. Each lands in the cart at the full price, with **no MUTO10**.
3. **Clicks:**
   - The stars scroll to the reviews widget.
   - "Scientific board" scrolls to the board.
   - Each "On this page" menu link scrolls to its section.
   - "View third-party testing results" (under the images, and on standards card 1) opens the certificate panel.
4. **Videos:** all 8 play. The row scrolls sideways (trackpad, drag, or swipe on a phone).
5. **Reviews:** the cards move on every 6 seconds, and the arrows work.
6. **On a phone:** nothing runs off the side; the statement tag wraps onto two lines.
7. **No sticky bar** appears as you scroll the page.
8. **-3 and any page on `muto-nad-performance`:** no Black Friday box (step 3).
9. **Travel vial:** add the 3-month plan to the cart. The drawer's gift list shows Travel Vial, £10 struck through, Free. The monthly plan doesn't get it.
10. **Announcement bar:** no "extra 10% off" or "ends on 28.10.26" (step 5).
