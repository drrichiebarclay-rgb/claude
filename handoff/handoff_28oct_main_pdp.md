---
title: "MUTO main product page: new template for the main URL and -2"
subtitle: "28 October 2026"
---

The main product page and -2 move to a new template, **`muto-nad-trust`**. The buy box is the one on the site today. Below it are new blocks: the science board, standards, customer videos, reviews and the founder. The Black Friday pre-sale box and its MUTO10 code are removed.

That means **6 new files to add**, **template changes on 2 products**, and **removing the pre-sale box from 3 live templates**. No existing theme file is overwritten.

# Before you start

- **Files:** `MUTO_Main_PDP_28Oct2026.zip`, also in GitHub at `handoff/main-pdp/` (repo drrichiebarclay-rgb/claude, branch `claude/gifted-wozniak-e239h5`).
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Preview:** the page is already on the 3M refill plan theme (ID 202682564955):
  <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955&view=muto-nad-trust>
- **Your edits are kept.** The buy box, its `easy_read` block, the sticky bar, the comparison table and the test-results panel are copied from the **live `muto-nad-v2` template as of 28 October**. If you've edited `muto-nad-v2` since, tell Richie before copying, and the template will be rebuilt from your latest version.

# Step 1: add the 6 files, in this order

Every file is new; nothing with these names exists on live.

| File | What it is |
|---|---|
| `assets/muto-crea-trust.css` | Styles for the four new blocks |
| `sections/muto-crea-statement.liquid` | "Not ready to slow down." band |
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

All the other sections the page uses are already on live and unchanged: `muto-pdp-v2-buy`, `muto-home-board`, `muto-test-results`, `muto-home-results`, `muto-crea-problem`, `muto-crea-benefits`, `muto-crea-steps`, `muto-crea-guarantee`, `muto-home-why`, `muto-chapter`, `muto-crea-faq`, `custom-reviews`, `muto-home-sticky`.

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

# What's on the new page

In order, below the buy box:

1. **Statement:** "Not ready to slow down." / "The next-generation multi-nutrient, built for what your body needs in your 40s and 50s." / tag "Got a wearable? Track the shift over 90 days."
2. **Science board:** "Six scientists put their name to MUTO.", compact row, white background.
3. **Standards:** four cards. Card 1 has the "View third-party testing results" button, which opens the certificate panel (batch 2333).
4. **Customer videos:** "Don't take our word for it.", 8 videos in a row that scrolls: Kate Bright, David Mercado, Lucy Halliday, Harry Insley, Adam Facey, Max Richards, Adam Hamilton, Yolanda King. Ellen Gray's video is removed.
5. **Reviews:** "What our community say.", 20 five-star REVIEWS.io reviews that rotate every 6 seconds, with "4.8 from 103 reviews".
6. **Founder:** Dr Richie Barclay, PhD.
7. Problem, benefits, **timeline** ("Your first 90 days." day 1 / 30 / 60 / 90), guarantee, **"MUTO vs the usual"** comparison (as on live), FAQs (7; "Do I need a smartwatch?" removed), REVIEWS.io widget.

Also changed from `muto-nad-v2`:

- **Under the buy button:** the serving line, "Not another multivitamin…" copy and the quote slider are blanked or hidden (not deleted).
- **Buy button** (and the sticky bar's) in brand green **#6BCE7F**, charcoal label, with a second line inside it: a shield and "90-day money-back guarantee".
- **Under the subhead:** "In collaboration with seven leading scientists from world-leading research institutions, including four universities in the UK and Australia."
- **Rotating stats** under the button, every 3.5 seconds: "94% reported better recovery", "92% reported improved energy", "88% bounce back quicker", with a black bar that fills left to right to each figure. Set in `STATS` in `make_trust.py`.
- **Delivery line** under the button: "● Ready to ship — arrives by **Thu 29th Oct**". The date is always the next calendar day in UK time, set by a script and rolling over at midnight. Before the script runs it says "arrives tomorrow".
- **Backgrounds:** no gradient washes. The bands alternate flat grey (#F2F2F2) and white, set in the `head_styles` block at the top of the template.
- **Not carried over from `muto-nad-v2`:** the "On this page" menu, "Five jobs. One daily jar.", the ingredient library, the v2 timeline and "How to take it". They stay in `muto-nad-v2` if they're wanted back.

## How it's built

- **Template-only** apart from the four new sections and their stylesheet. The page's own styles are in a Custom Liquid block called `head_styles` at the **top** of the template, so the buy box is styled from the first paint (with them at the bottom, the old design flashed on load). Its scripts stay in `easy_read` and `bands` at the bottom.
- **Source:** `shopify/pdp-trust/make_trust.py` builds the template. Change copy there and rebuild rather than editing by hand, or tell Richie about manual edits so they aren't lost on the next rebuild.

# Check after publishing

1. **Main URL and -2:** the buy box matches today's page, with **no** dark Black Friday box above the plans.
2. **Add to cart** on the Quarterly plan, the Monthly plan and one-time purchase. Each lands in the cart at the full price, with **no MUTO10**.
3. **Clicks:**
   - The stars scroll to the reviews widget.
   - "Scientific board" scrolls to the board.
   - "View third-party testing results" (under the images, and on standards card 1) opens the certificate panel.
4. **Videos:** all 8 play. The row scrolls sideways (trackpad, drag, or swipe on a phone).
5. **Reviews:** the cards move on every 6 seconds, and the arrows work.
6. **On a phone:** nothing runs off the side; the statement tag wraps onto two lines.
7. **-3 and any page on `muto-nad-performance`:** no Black Friday box (step 3).
