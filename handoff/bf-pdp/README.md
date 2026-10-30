---
title: "MUTO Black Friday product page: main URL and -2"
subtitle: "30 October 2026"
---

For Black Friday, the main product page and -2 move to a new template, **`muto-nad-bf`**. It's the new main page (`muto-nad-trust`: every live section plus the new trust blocks) with the Black Friday offer on top:

- **Sticky black bar:** "Black Friday · 53% off your first order plus a welcome kit worth £87 · 481/500 left · Claim offer".
- **White offer box above the plans:** a live count of orders left out of 500.
- **Plan cards:** Black Friday pricing, and the daily cost in a lime pill.

After Black Friday, both URLs switch to `muto-nad-trust` (included), the same page without the offer.

# Must be done before it goes live

These are outside the theme. The page **says** the offer, but nothing here **applies** it.

1. **The Black Friday prices at checkout.** The page shows:
   - **Quarterly:** £99 for the first box, then £125, then £150. That's £33/mo, £1.10 a day, "Save 53%".
   - **Monthly:** £49.99 for the first month, then £60 every 4 weeks. That's £1.79 a day, "Save 28%".

   **No discount or Skio offer for this exists yet.** Without one, the cart and checkout charge the normal £150 / £60. Set it up in Skio, or as a Shopify discount, so checkout matches the page.
   - If it's a discount code, tell Richie. The page can apply a code automatically.
   - It's the `CODE` setting in `make_bf.py`, currently blank.
2. **Orders left.** The bar and the box read the shop metafield **`muto.bf_orders_left`** (now **481**). Nothing counts it down yet. Either a Shopify Flow ("order created with the NAD+ subscription → decrease `muto.bf_orders_left` by 1") or a person updating it (Settings → Custom data → Shop → `bf_orders_left`). At 0 the box says "All 500 have gone."
3. **The duplicated 3-month plan in Skio.** On 30 Oct a copy of the 3-month subscription (`copy-of-subscription-refills-3-month`, selling plan **694836494683**) was attached to the 90-day variants. It showed as a third, empty plan card.
   - **On the new templates:** already hidden, via the buy box's "Hidden plans" setting.
   - **On live `muto-nad-v2`:** add the same ID to "Hidden plans" (main and -2 show the extra card until step 3), or delete the copy in Skio if nobody needs it.
   - **If the copy is the Black Friday plan:** tell Richie, as the hidden ID must change.
4. **The travel vial in the cart**, see below.

# Before you start

- **Files:** `MUTO_BF_PDP_30Oct2026.zip`, also in GitHub at `handoff/bf-pdp/` (repo drrichiebarclay-rgb/claude, branch `claude/gifted-wozniak-e239h5`).
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Preview:** both pages are on the 3M refill plan theme (ID 202682564955):
  - Black Friday: <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955&view=muto-nad-bf>
  - After Black Friday: <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955&view=muto-nad-trust>
- **Your edits are kept.** The buy box, its `easy_read` block, the menu, benefits, ingredient library, comparison, timeline, "How to take it", FAQs and the test-results panel are copied from **live `muto-nad-v2` as of 28 October**. If you've edited `muto-nad-v2` since, tell Richie first, and both templates will be rebuilt from your version.
- **Images:** the founder photo (`founder-bf-stage.jpg`) and the travel vial photo (`gift-travel-vial.jpg`) are already in Content → Files, so there is nothing to upload.

# Step 1: add the 8 files, in this order

Every file is new; nothing with these names exists on live.

| File | What it is |
|---|---|
| `assets/muto-crea-trust.css` | Styles for the new blocks |
| `sections/muto-crea-statement.liquid` | "The best is still ahead." band |
| `sections/muto-crea-stats.liquid` | "The problem": four stat cards with sources |
| `sections/muto-crea-standards.liquid` | "Checked, not taken on trust." four standards cards |
| `sections/muto-crea-reviews.liquid` | "What our community say." rotating reviews (20) |
| `sections/muto-crea-founder.liquid` | Founder band |
| `templates/product.muto-nad-bf.json` | **The Black Friday page** |
| `templates/product.muto-nad-trust.json` | The same page without the offer, for after Black Friday |

Add the asset and the sections first. A template that uses a section is rejected if the section isn't there yet.

With the Shopify CLI, from the unzipped folder:

    shopify theme push --theme 200736047451 --nodelete \
      --only "assets/muto-crea-trust.css" --only "sections/muto-crea-*.liquid" \
      --only "templates/product.muto-nad-bf.json" --only "templates/product.muto-nad-trust.json"

Or in admin: Online Store → Themes → live theme → … → Edit code. Add a new asset, then each new section, then two new product templates named `muto-nad-bf` and `muto-nad-trust`, and paste each file in.

All the other sections the page uses are already on live and unchanged: `muto-pdp-v2-buy`, `muto-section-nav`, `muto-benefit-cards`, `muto-home-board`, `muto-ingredient-library`, `muto-home-results`, `muto-chapter`, `muto-timeline`, `muto-crea-faq`, `custom-reviews`, `muto-test-results`, `custom-liquid`.

# Step 2: the travel vial


A free **travel vial** now comes with the first order on the 3-month plan only, shown with **£10 crossed out**, like the other gifts.

- **Product: already created.** "Travel Vial", handle `muto-travel-vial-free`, SKU `TRAVEL-VIAL`, £0 with a £10 compare-at, unlisted, stock not tracked, published to the Online Store. Its photo is on the product, so it shows in the cart.
- **Cart: one setting to change on the live theme.** Online Store → Customize → Theme settings → the cart giveaway settings → the 3-month free products list (`cart_free_product_3m`). Add **Travel Vial** (`muto-travel-vial-free`) to the list, alongside the bottle, socks, creatine and Garmin entry. The theme's giveaway script then adds it to the cart at £0 whenever the 3-month NAD+ subscription is in it. The cart drawer lists it under "Your free welcome gifts" with £10 struck through and "Free". Subscription renewals don't carry cart gifts, so it only ships with the first order.
- **Page: in the template.** The welcome kit shows a "Travel vial" tile (£10 struck through) and an itemised row on the quarterly plan only. The quarterly kit is now worth **£87** (was £77) in the plan's bullet and the bar above the plans.
- **Also say £87** wherever else the quarterly kit is quoted at £77, e.g. the announcement bar's "£77 OF FREE GIFTS WITH EACH ORDER" if that's meant to be the quarterly figure.

# Step 3: switch the product templates

Do this **after** step 1, and once the prices at checkout match (see "Must be done before it goes live"). In Shopify admin, go to Products → product → Theme template.

| URL | Product | Template now | Black Friday | After Black Friday |
|---|---|---|---|---|
| `/products/muto-nad-cellular-complex` (main) | NAD+ Cellular Complex | `muto-nad-v2` | **`muto-nad-bf`** | `muto-nad-trust` |
| `/products/muto-nad-cellular-complex-2` | NAD+ Cellular Complex 2 | `muto-nad-v2` | **`muto-nad-bf`** | `muto-nad-trust` |

Nothing is deleted. `muto-nad-v2` stays in the theme, so either page can be switched back in one click.

# Step 4: the announcement bar

- **On the Black Friday page:** the page hides the blue scrolling announcement bar itself, so the black Black Friday bar is the only one at the top. Nothing to do.
- **On every other page:** the bar still advertises the ended offer, **"EXTRA 10% OFF OUR QUARTERLY PLAN"** and **"ENDS ON 28.10.26"**. Remove those two messages (Customize → Header → announcement bar). If "£77 OF FREE GIFTS WITH EACH ORDER" is the quarterly figure, it's now **£87** with the travel vial.

# Step 5: remove the old pre-sale box from the other live templates

**MUTO10 was ended on 28 October at 17:19.** It no longer works at checkout. The dark "BLACK FRIDAY PRE-SALE" box still says the code "is applied automatically at checkout", and its script still tries to apply MUTO10 on page load. It's on three live templates:

- `product.muto-nad-v2` (main and -2 until step 3 is done; also the page they go back to after Black Friday)
- `product.muto-nad-performance` (-3)
- `product.muto-nad-45` (no product uses it now)

In each one, open the `easy_read` Custom Liquid block and delete three things:

1. In the `<style>`: from `/* Black Friday pre-sale box, above the plans */` up to (not including) `/* -2 page only:`.
2. In the `<script>`: from `/* Black Friday pre-sale: real countdown` down to the end of that function, the line `if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();` and the `})();` after it.
3. The line `<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"></div>`.

The new `muto-nad-bf` and `muto-nad-trust` templates already have all three removed.

**Quick stopgap** if step 3 can't be done straight away: Online Store → Customize → Theme settings → Custom CSS, add `.mc-bf:has(.mc-bf__clock){display:none !important}`. That hides the box on every page. The script still runs, but MUTO10 is ended, so nothing is applied.

# The Black Friday additions

On top of everything listed in the next section:

- **Sticky bar** (Custom Liquid block `bf_bar`, before the buy box). Black #242223, white text, 44px tall, fixed to the top of the screen. The page, header included, starts 44px lower so nothing sits under it. The theme pulls product-page content up under its see-through header, which is why the bar is fixed rather than in the page.
  - **Desktop:** "● BLACK FRIDAY **53% off your first order** plus a welcome kit worth £87 · **481**/500 left · Claim offer".
  - **Phones:** "● BLACK FRIDAY **53% off your first order** · **481**/500 left".
  - **Tapping it:** scrolls to the offer box.
  - **Orders left:** comes from `muto.bf_orders_left`, rendered in the page (no script), so it's there from the first paint.
- **The blue announcement bar** is hidden on this page only (`[id$="__muto-announce"]{display:none}` in `bf_bar`).
- **"On this page" menu:** pins 44px from the top, under the bar (its `nav_top` setting).
- **Offer box above the plans:**
  - white with a black outline
  - "BLACK FRIDAY OFFER", "53% off your first order", "plus a welcome kit worth £87", "£99 for your first order, £125 on your second, £150 on your third."
  - "481 out of 500 remaining" with a bar
  - drawn in the `early` block straight after the buy box, so it's there before first paint
- **Bar over the plans:** "Black Friday offer · Limited stock", with "Best value" in a turquoise pill.
- **Quarterly card:** "Save 53%", £33/mo (£70 struck), "3 months' supply: £99 for your first box, then £125, then £150", and a lime **£1.10 a day** pill beside the name. The welcome-kit line is first in its list.
- **Monthly card:** "Save 28%", £49.99/mo (£70 struck), "£49.99 for your first month, then £60 every 4 weeks", and a lime **£1.79 a day** pill.
- **Founder photo:** Richie on stage (`founder-bf-stage.jpg`). The main page keeps the original.

# What's on the page

In order, below the buy box. **New** blocks are in bold; the rest is `muto-nad-v2` as it is on live today.

1. "On this page" menu (pins to the top as you scroll, as on live), with four new links: **Problem**, **Standards**, **What people say** (the videos) and **Founder**, 12 links in page order
2. **Statement:** "The best is still ahead." / "Built for your energy, recovery and sleep in your 40s and 50s. Five supplements in one daily jar." / tag "Track it on your wearable for 90 days, or your money back."
3. **The problem:** small mono label "The problem", heading "Your biology shifts. Most supplements don’t." Four cards in the standards style (number, lime topic tag, big figure, cyan rule, one line): Energy **~50%** drop in your muscles’ energy-making capacity between your 40s and late 60s (Conley et al., 2000) · Recovery **~80%** less deep, restorative sleep by midlife than in your early 20s (Van Cauter et al., JAMA 2000) · Longevity **3–8%** of muscle lost every decade after 30 (Volpi et al., 2004) · Trust **57%** of supplements tested didn’t match their label (Crawford et al., 2022). Sources in a small line underneath.
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

1. **Main URL and -2 on phone and desktop:**
   - the black bar is at the very top, with the header fully visible under it and no blue bar
   - the page opens on the **Quarterly** plan
   - nothing jumps as it loads
2. **Prices at checkout match the page:**
   - Quarterly: first box £99
   - Monthly: first month £49.99

   This is the "Must be done" item. Check every plan, one-time included.
3. **Orders left:** the bar and the box both show the metafield value. Change it and both follow.
4. **Travel vial:** add the 3-month plan to the cart. The gift list shows Travel Vial, ~~£10~~ Free. The monthly plan doesn't get it.
5. **Only two plan cards** (Monthly, Quarterly) plus "Buy once". No empty "3-MONTH SUBSCRIPTION" card.
6. **Clicks:**
   - The bar scrolls to the offer box.
   - Each "On this page" link scrolls to its section, with the menu under the bar.
   - "View third-party testing results" opens the certificate panel.
   - The stars scroll to the reviews widget.
7. **Videos** play, and the **reviews** rotate. The REVIEWS.io widget at the bottom loads as you scroll near it.
8. **After Black Friday:** switch both products to `muto-nad-trust` and check point 1 again. There should be no bar, no offer box and normal prices.
