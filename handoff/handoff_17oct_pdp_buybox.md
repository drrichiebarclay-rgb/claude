---
title: "MUTO product pages: new buy box, and -2 becomes the main page"
subtitle: "17 October 2026"
---

The -2 page's design (template `muto-nad-45`) becomes the **main product page**. The current main page's template (`muto-nad-performance`) moves to **-3**, and -2 keeps its design. Both templates also have a new buy box.

That means **3 theme files to copy**, **template changes on 2 products**, **photos on 1 product** and a **Shopify Flow** for the Black Friday pre-sale box.

# Before you start

- **Files:** `MUTO_PDPs_buybox_live.zip`, also in GitHub at `shopify/pdp-45/` (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`).
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Your edits are kept.** Both templates were built from the **live copies taken on the morning of 17 October**, so your latest edits (such as the rating wording) are kept. If you've edited either template on live since then, tell me before copying and I'll rebuild.
- **Preview:** both pages work on the 3M refill plan theme (ID 202682564955):
  - -2 design: <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=202682564955>
  - Main design (going to -3): <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955>

# Step 1: copy the 3 files, in this order

| File | What it is |
|---|---|
| `sections/muto-crea-buy.liquid` | The shared buy-box section. One addition: an optional **Rating link** setting that makes the star row a link. Pages that don't fill it in are unchanged. |
| `templates/product.muto-nad-45.json` | The **-2 design**, which becomes the main page. |
| `templates/product.muto-nad-performance.json` | The **current main page**, which moves to -3, with the same new buy box. Everything below the buy box is unchanged. |

Copy the section first. A template that uses the new setting is rejected if the section doesn't have it yet.

# Step 2: change product templates

Do this **after** step 1. In Shopify admin, go to Products → product → Theme template.

| URL | Product | Template now | Template after |
|---|---|---|---|
| `/products/muto-nad-cellular-complex` (main) | NAD+ Cellular Complex | `muto-nad-performance` | **`muto-nad-45`** |
| `/products/muto-nad-cellular-complex-2` | NAD+ Cellular Complex 2 | `muto-nad-45` | `muto-nad-45` (no change) |
| `/products/muto-nad-cellular-complex-3` | NAD+ Cellular Complex 3 | `muto-3` | **`muto-nad-performance`** |

Nothing is deleted. `muto-3` stays in the theme unused, so -3 can be switched back in one click.

# Step 3: product photos

Every page takes its carousel from **its own product's Media**, not from the template. So moving a template doesn't move its photos.

- [ ] **-3 needs photos.** NAD+ Cellular Complex 3 has only 3 images (`newmain.png`, `Frame_2147230140.png`, `Frame_2147230136.png`). Copy the main product's 10 images onto it, in the same order, so -3 looks like today's main page.
- [ ] **Main: optional reorder.** The main product already has the same 10 images as -2, in a different order. To make the main page's carousel match -2 exactly, reorder the main product's Media to:
  1. `Frame_2147230150a`
  2. `Frame_2147230150`
  3. `Frame_2147230153`
  4. `new_eifjwef`
  5. `Frame_2147230151aaa`
  6. `MUTO_-_76`
  7. `Frame_2147230127`
  8. `Frame_2147230152`
  9. `Frame_2147230155`
  10. `Frame_2147230136`
- **Don't use Content → Files → Replace** on these images. Several products share them, so a replace changes every product at once.

# What changed in the buy box (both templates)

- **Title block:**
  - Rating, now linked to the reviews (`#ReviewsWidget`).
  - MUTO, then "NAD+ Cellular Complex" on one line.
  - "Serving: 30-day supply (60 capsules), 2 a day".
  - Descriptor: "Your daily NAD+ formula, made for adults over 35."
  - One paragraph on what it is and what's in it.
  - An "Ingredients + nutritional information" link that opens the ingredients fold.
- **Benefits:** six items in two columns. The trust pills are removed.
- **"Choose your plan"** with two expanding boxes. Quarterly is first and open on load, and clicking a box opens it.
  - Bar on top: "New customer offer, free welcome kit worth £77".
  - **Quarterly plan:** Save 28% + free gifts. £150 with £210 struck through. "Billed £150 every 3 months · £1.67 a day".
    - Ticks: kit worth £77, gifts in boxes 2 and 3 then creatine every box, cancel or pause anytime, 90-day money-back guarantee.
    - Kit tiles: Creatine, Socks, Jar, Bottle, Guide, Garmin entry.
    - Future gifts: box 2 Socks, Creatine and £10 credit; box 3 Creatine and expert chat; from box 4 Creatine every box.
  - **Monthly plan:** Save 14% + free gifts. £60 with £70 struck through. "Billed £60 every 4 weeks · £2 a day".
    - Kit worth £62: Creatine, Socks, Jar, Guide, Garmin entry.
    - Future gifts: box 2 Bottle; box 3 Socks; box 4 Creatine and £10 credit; box 6 Creatine and expert chat.
- **One-time purchase** is its own row, then a button reading "Subscribe · ~~£210~~ £150" or "Subscribe · ~~£70~~ £60". It follows the selected plan.
- **Desktop gallery:** the thumbnails sit in their own column to the left of the main image.
- **"Over 40" is now "over 35"** throughout the -2 design.

## How it's built

- **Template-only.** The copy is in the buy section's settings and blocks. The styling and a small script are in a Custom Liquid block called `easy_read` at the bottom of each template. On `muto-nad-performance` that block is new.
- **The quarterly plan is shown.** `hidden_plans` is now empty. Card prices come from Skio, currently £60 (1-month) and £150 (3-month).
- **Gifts are tagged by plan.** 1 = monthly and 2 = quarterly, in Skio's order; empty means both plans. Only the Bottle is quarterly-only in the first box. The quarterly box shows first because of the page's CSS and opens on load because of its script.
- **Block limit.** The section allows **50 blocks**. `muto-nad-performance` uses 47 and `muto-nad-45` uses 39. Remove a block before adding new ones to the performance template.

# Black Friday pre-sale box (both templates)

A dark box sits above the plan boxes. It runs from page load until **23:59 UK time on Wednesday 28 October**, then hides itself.

- **What it shows:**
  - "BLACK FRIDAY PRE-SALE".
  - "Extra 10% off the Quarterly plan, plus a free welcome kit worth £77".
  - "£135 for your first box instead of £150. Code MUTO10 is applied automatically at checkout".
  - A live countdown in days, hours, minutes and seconds.
  - "Pre-sale ends 23:59, Wednesday 28 October."
  - "92 of 500 free welcome kits left at this price", with a progress bar.
- **How it's built:** template-only, in the same `easy_read` block. The source is `shopify/pdp-45/artah/bf.js` and `bf.css`. The end date, the code and the total of 500 are set at the top of `bf.js`.
- **The code:** the page calls `/discount/MUTO10` when it loads, so Shopify applies the code at checkout. MUTO10 already exists: 10% off, applies to subscriptions and one-time purchases, once per customer. It works on both plans, even though the box only promotes the Quarterly plan.

## Welcome kits left

The number comes from a shop metafield, `muto.bf_boxes_left`. It's set to **92**, the real pre-Black Friday allocation. To edit it: Settings → Custom data → Shop → "Black Friday welcome kits left". If it's blank, the line is hidden.

## Set up: Shopify Flow to lower the count by 1 per new customer

1. Flow → Create workflow → Trigger: **Order created**.
2. Condition, all of:
   - the customer's number of orders is equal to 1 (welcome kits only go out with first orders, so Skio renewals don't count);
   - `muto.bf_boxes_left` is greater than 0.
3. Action: **Update shop metafield**:
   - namespace `muto`, key `bf_boxes_left`, type Integer;
   - value = the current value minus 1, e.g. `{{ … bf_boxes_left.value | minus: 1 }}` using Flow's variable picker for the shop metafield.
4. Turn it on before the box goes live.

## Before launch

- [ ] In Discounts, give **MUTO10 an end date** of 28 Oct 2026, 23:59. Today it has none.
- [ ] **Test orders** on the Quarterly plan, the Monthly plan and one-time purchase. Check MUTO10 applies **and** the welcome-kit gifts still arrive. MUTO10 doesn't combine with product discounts, so if the gifts use a product discount, one will cancel the other.
- [ ] **Check the Flow:** after one test order, the count drops from 92 to 91.
- [ ] **When the count reaches 0:** the free kit or the price must change, because the box says "at this price". Tell Richie so the box can be updated.

# Notes

- [ ] **Product titles in cart and checkout:** -2 and -3 are titled "NAD+ Cellular Complex 2" and "NAD+ Cellular Complex 3", and that title shows in the cart and order emails. Rename both to "NAD+ Cellular Complex" if they get traffic.
- [ ] **-3 is Unlisted.** It works by direct link but won't appear in search or collections. That's fine for ad traffic.
- **Landing pages:** MP1, MP2, MP3 and MP5 link to -2, and the others link to the main URL. After the switch, both URLs show the same design.

# Check after publishing

1. **Main URL:**
   - Shows the -2 design: "made for adults over 35" and the six benefits.
   - Quarterly is open with "New customer offer, free welcome kit worth £77", and the button reads "Subscribe · ~~£210~~ £150".
2. **Click Monthly.** Its box opens and quarterly collapses. The gift tiles and future gifts change, and the button reads "Subscribe · ~~£70~~ £60".
3. **Add to cart** on both plans and on one-time purchase. Each should land in the cart with the right plan and the welcome kit.
4. **Clicks:** the star rating scrolls to the reviews, and "Ingredients + nutritional information" opens the ingredients fold.
5. **-2:** same as the main URL.
6. **-3:** the former main page's content below the buy box, with its own photos once step 3 is done.
7. **On a phone:** the plan boxes, gift tiles and button all fit the width.
