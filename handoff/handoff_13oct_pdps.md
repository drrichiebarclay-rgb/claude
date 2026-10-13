---
title: "MUTO NAD+ product pages: new main page and page order"
subtitle: "13 October 2026"
---

Two new NAD+ product page templates are ready. One becomes the **main product page**, the other goes on **-2**, and your existing test pages move to **-3, -4 and -5**. Nothing in the shared sections changes: this is **2 template files to copy** and **template changes on 4 products**.

# Before you start

- **Copy from:** `shopify/pdp-rollout/templates` in GitHub (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`): <https://github.com/drrichiebarclay-rgb/claude/tree/claude/faq-page-shopify-redesign-hbqcg8/shopify/pdp-rollout/templates>.
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Your live edits are kept.** Both files were built from a snapshot of **live taken this afternoon (13 Oct)**, so they keep your edits: the hidden 3-month plan (`hidden_plans`), "£2/day" on the monthly plan note, and the board settings. If you edit live again before copying, tell me and I'll rebuild.
- **No section changes needed.** Both templates only use sections already on live (`muto-crea-buy`, `muto-crea-compare`, `muto-crea-benefits` and the other `muto-crea-*` / `muto-home-*` sections, plus the standard `custom-liquid`). I checked that live `muto-crea-buy.liquid` has every setting they use (`gallery_from_product`, `kit_foot_4`, `hidden_plans`, `kit_itemised`).
- **Preview both on the 3M refill plan theme** (ID 202682564955). The previews don't have your hidden-plan edit, so they show both plans; the files you copy do hide the 3-month plan.
  - Main page: <https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-performance&preview_theme_id=202682564955>
  - 45–55 page: <https://muto.co/products/muto-nad-cellular-complex-3?view=muto-nad-45&preview_theme_id=202682564955>

# The 2 files to copy

| File | What it is |
|---|---|
| `templates/product.muto-nad-performance.json` | **New main page.** Built on today's live `product.muto-nad-creatine-kit.json`. Same offer, plans, gifts, images, buttons and comparison table; copy rewritten for a broad, busy 30–45 audience around energy, recovery and stress, with a weekly check-in or wearable to track it. |
| `templates/product.muto-nad-45.json` | **New -2 page, for 45–55.** Built on today's live `product.muto-nad-simple-creatine-kit.json`. Plain, emotional copy, fewer sections in a simpler order, and easier-reading text sizes. Also brings this page up to date with the Garmin giveaway tile and the new plain-English comparison table (live still shows the Oura tile and the old table here). |

# Product templates after the change

Set each product's **Theme template** in Shopify admin (Products → product → Online store → Theme template), **after** the files above are on live. If you switch a product first, its page falls back to the default product template.

| URL | Product | Template now | Template after |
|---|---|---|---|
| `/products/muto-nad-cellular-complex` (main, active) | NAD+ Cellular Complex | `muto-nad-creatine-kit` | **`muto-nad-performance`** |
| `/products/muto-nad-cellular-complex-2` | NAD+ Cellular Complex 2 | `muto-nad-live-creatine-kit` | **`muto-nad-45`** |
| `/products/muto-nad-cellular-complex-3` | NAD+ Cellular Complex 3 | `muto-nad-simple-creatine-kit` | **`muto-3`** (your page, now on `-old`) |
| `/products/muto-nad-cellular-complex-4` | NAD⁺ Cellular Complex | `muto-6` | `muto-6` (no change) |
| `/products/muto-nad-cellular-complex-5` | NAD⁺ Cellular Complex | `muto-5` | `muto-5` (no change) |

Your three pages (`muto-3`, `muto-6`, `muto-5`) end up on -3, -4 and -5. Only `muto-3` moves, from `-old` to `-3`.

Nothing is deleted. The old templates (`muto-nad-creatine-kit`, `muto-nad-live-creatine-kit`, `muto-nad-simple-creatine-kit`) stay in the theme unused, so you can switch any product back in one click.

# What's on each page

## Main page (`muto-nad-performance`)

- **Buy box intro:** "You're doing more than ever. MUTO lets you see if it's working. NR, which your body turns into NAD+, plus 18 supporting ingredients, every dose on the label. Two capsules with breakfast, then track your energy, recovery and stress on your wearable. 90 days to judge it, or your money back on subscriptions."
- **Banner:** "Welcome kit worth £62, free with your first order" (as on your live creatine-kit page).
- **Bullets:** Energy that lasts through the afternoon / Bounce back from late nights, travel and workouts / Built for busy, stressful weeks / Feel the difference in 90 days, or your money back.
- **Problem:** "Busy life. Same body. One energy budget." with four cards: Sharp at 9am, gone by 4pm / One late night costs me two days / Always on, never off / A shelf full of pills.
- **Benefits:** two tabs. "What you'll feel" (energy past 4pm, bounce back faster, a steadier head in busy weeks, fewer flat days) and "Check it your way" (weekly check-in first, then HRV, resting heart rate, sleep, readiness or Body Battery).
- **FAQ:** adds "Will it help with stress?" and "Is there caffeine in it?".
- **Same as today:** plans, gifts, gallery, comparison table, guarantee, reviews and sticky bar. Section order is unchanged.

## -2 page, 45–55 (`muto-nad-45`)

- **Buy box intro:** "You're not ready to slow down. You just want to feel like yourself again, with energy for the whole day, not just the morning. Two capsules with breakfast. Give it 90 days. Love it, or get your money back."
- **Bullets:** Feel like yourself again / Energy that lasts past lunch / Bounce back after a walk, a round or the gym / 90 days to try it, or your money back.
- **Problem:** "You don't feel old. So why so tired?" Cards: I used to have so much energy / My body takes longer to recover / I just want to feel like me again / Too many pills.
- **Simpler order:** buy → problem → what people notice → real stories → 90 days → guarantee → why trust us → experts → comparison → FAQs → reviews. The "Two capsules" section and the full ingredients list are removed (the "What's inside" fold in the buy box still covers ingredients). Benefits has one view only; the tracking tab is folded into the 90-day steps.
- **FAQ:** adds "Is it right for my age?" first.
- **Easier reading:** a `custom-liquid` section at the end of the template (`easy_read`, zero padding) holds a `<style>` block. It only exists in this template, so no other page is affected. It:
  - raises body text from 16px to 17px, with a looser line height;
  - sets the opening line to 19px, the problem intro to 20px and step titles to 23px;
  - darkens grey secondary text;
  - enlarges the gift labels from 10px to 13px and the plan prices to 20px;
  - makes the buttons 17px and 56px tall;
  - keeps the trust pills at theme size, on one line on desktop;
  - hides the benefits tab switcher.

  The source is `shopify/pdp-45/easy-read.css` if you'd rather move it into a stylesheet later.

# Notes

- [ ] **Product titles in cart and checkout:** the -2 and -3 products are titled "NAD+ Cellular Complex 2" and "NAD+ Cellular Complex 3", and that title shows in the cart, checkout and order emails. Worth renaming both to "NAD+ Cellular Complex" if these pages get traffic.
- [ ] **Hidden 3-month plan:** both new templates keep your `hidden_plans` setting, so only the monthly plan shows. If the 3-month plan should show on the 45–55 page, clear `hidden_plans` on it.
- [ ] **`-old` product:** after the switch, `muto-3` is on both `-old` and `-3`. Leave `-old` as it is, or redirect it to `-3`.
- [ ] **Ads and links:** anything pointing at the main page will show the new copy straight away. Any ad that should keep the old creatine-kit copy needs its own product and URL.

# Check after publishing

1. **Main page:** the intro starts "You're doing more than ever", the banner says £62, only the monthly plan shows, and the benefits tabs read "What you'll feel" and "Check it your way".
2. **-2:** "You don't feel old. So why so tired?" is the problem heading. The Garmin tile and the plain-English comparison table ("The easy way to get NAD⁺.") show, the text is visibly larger, and the trust pills each sit on one line on desktop.
3. **-3, -4, -5:** your own pages, as before.
4. **Add to cart** works on all five, with the welcome kit added.
5. **On a phone:** check -2 for wrapping in the plan cards and gift labels.
