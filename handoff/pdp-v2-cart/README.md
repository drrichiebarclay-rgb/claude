---
title: "MUTO product page and cart drawer: per-month plans, new top of page, new cart"
subtitle: "27 October 2026"
---

New plan pricing, a new top of page and sticky-bar price on the product page, and a rebuilt cart drawer. **It's 2 files to copy into the live theme.** Both URLs use the same template, so one copy covers both:

- <https://muto.co/products/muto-nad-cellular-complex>
- <https://muto.co/products/muto-nad-cellular-complex-2>

No section, asset, app or Skio changes.

# Before you start

- **Files:** `MUTO_PDP_v2_Cart_27Oct2026.zip`. They're also in GitHub at `handoff/pdp-v2-cart/` (repo drrichiebarclay-rgb/claude, branch `claude/beautiful-bohr-wkhdur`).

| File | Replaces |
|---|---|
| `templates/product.muto-nad-v2.json` | the template with the same name |
| `snippets/cart-drawer.liquid` | the snippet with the same name |

- **Preview:** it's all on the theme **"Clone Of Live | Plan pricing /mo [27-10]"** (ID 203700666715):
  - <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203700666715>
  - <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=203700666715>
- **Built from the live files as they were this morning.** On 27 Oct, live still matched them. If either file has been edited on live since, tell me before copying, so those edits aren't lost.

# Step 1: copy the 2 files

On the live theme (**Clone Of Live | Buy Box Redesign [31-08]**), go to **Edit code**:

1. Open `templates/product.muto-nad-v2.json`, replace everything with the file from the zip, and save.
2. Open `snippets/cart-drawer.liquid`, replace everything with the file from the zip, and save.

**The other way to do it:** publish the preview theme instead. It's a full copy of live from this morning with only these 2 files changed.

# What changes

## Product page: plans

- **Quarterly:** **£50/mo**, with ~~£70~~ underneath. A cyan **SAVE 28%** tag sits in the box's top-left corner.
- **Monthly:** **£60/mo**, with ~~£70~~ underneath, and a **SAVE 14%** tag.
- **"Best value" bar:** the dark bar over Quarterly reads "✦ BEST VALUE · New customers: free welcome kit worth £77".
- **Billing lines:** unchanged ("billed £150 every 3 months", "billed £60 every 4 weeks"). **Skio isn't changed.** It still bills £150 every 3 months and £60 every 4 weeks.
- **The button:** reads **Add to cart**, with no price on it.
- **Sticky bar at the bottom:** shows the per-month price for the selected plan, "Add to cart ~~£70~~ £50/mo" or "~~£70~~ £60/mo".

## Product page: top of page

- **On phones, AgeMate-style, from the top:**
  1. Stars and "4.83 out of 5" (bigger stars, Neue Haas, no underline).
  2. **NAD+ Cellular Complex**.
  3. "Everything your body needs after 35 for energy, recovery, stress, immunity and longevity."
  4. The images.
  5. A **View third-party testing results** button.
  6. The offer: Black Friday box, "Choose your plan", plans, one-time and the button.
  7. The description, benefits, reviews and folds.
- **On desktop:** the same parts in the existing two-column layout.
- **Removed:**
  - "MUTO" above the title.
  - The "Ingredients + nutritional information" link.
  - The second testing button lower in the buy box.

## Cart drawer (all pages)

- **Order:** NAD product first, then gifts as **"Your free welcome gifts (n)"**. Each gift is a small row with picture, name, value crossed out and FREE. The order is creatine, socks, bottle, ebook, jar, then the Garmin entry last.
  - With a NAD subscription, the **12-Week Protocol eBook** and **Forever Jar** (£10 each) are listed as gifts even though they aren't cart lines.
- **Removed:** the reviews box and the free-shipping bar.
- **If a subscription is in the cart**, a grey box at the top reads:
  - "Feel the difference in 90 days – or get every payment back."
  - "Skip, pause or cancel online anytime."
  - "★★★★★ 4.8/5"
- **Under the NAD title:**
  - "Replaces 5 supplements · £1.67 a day" on Quarterly, "· £2 a day" on Monthly, and just "Replaces 5 supplements" on one-time.
  - A green ticked line: "You save £60 every 3 months, ongoing" or "You save £10 every month, ongoing".
- **The price under the title is gone.** It's only on the right now.
- **Subtotal:** ~~sum of the crossed-out prices above~~ **total**, then a **Save £x** pill. The confusing "YOU SAVE" badge is gone.
- **Button:** **Checkout · £150**, using the live cart total.
- **Under the payment icons:** "🔒 Secure checkout · ⏸ Cancel anytime · 🛡 90-day guarantee".
- **Fix:** the quantities sent with checkout are now matched to each cart line by its key, not by row order. The new row order can't move a quantity onto the wrong item.

# Worth knowing

- **Typed-in figures:**
  - The per-month prices (£50/mo, £60/mo, £70) are typed into the page's styling, because the theme prints Skio's billed price. If Skio's prices change, update them in the `easy_read` Custom Liquid block at the bottom of the template. Search for `£50/mo`.
  - The cart's per-day cost and "You save" amounts are worked out from Skio's prices automatically.
- **The Black Friday box:** it's still in the template and hides itself after 23:59 on 28 Oct, as before.
- **The editor:** the copied template replaces what's on live. Make any theme-editor tweaks to these pages **after** copying, not before.

# Check after publishing

- [ ] **Both URLs, on a phone:** stars, title and descriptor sit above the images. The testing button opens the test results.
- [ ] **Plans:** Quarterly shows £50/mo, ~~£70~~ and SAVE 28%, and is selected on load. Monthly shows £60/mo, ~~£70~~ and SAVE 14%. Switching plans updates the sticky bar.
- [ ] **Add to cart on Quarterly:**
  - The drawer shows NAD first and the gifts list underneath.
  - "£1.67 a day" and "You save £60 every 3 months, ongoing" appear.
  - The subtotal maths adds up.
  - The button reads "Checkout · £…".
- [ ] **Switch to Monthly in the cart:** the lines change to "£2 a day" and "£10 every month".
- [ ] **One-time purchase:** no subscription box, no per-day or savings lines, and no ebook or jar in the gifts.
- [ ] **Quantity:** change the NAD quantity to 2, then check out. Checkout shows 2 NAD and the gifts at their own quantities.
