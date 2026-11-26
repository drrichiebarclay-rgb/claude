---
title: "MUTO PDP + cart drawer: dev handover"
subtitle: "25 November 2026"
---

All changes are on the duplicate theme **Clone Of Live | Wearable PDP [23-11]** (ID 205557006683), not published. Preview: <https://c0xuhb-9e.myshopify.com/products/muto-nad-cellular-complex?preview_theme_id=205557006683>

**The priority is a full check of the cart on mobile, on real devices, before anyone publishes.**

# Mobile cart test checklist

Please run every check below on real phones: iPhone Safari, Android Chrome, and the Instagram and Facebook in-app browsers (that's where most of the traffic lands). The cart drawer was rebuilt in many small rounds, and it was only checked in a desktop test browser and one iPhone screenshot. Note the device, browser and result against each line, with a screenshot of anything wrong.

## Adding to cart

- [ ] 3-month plan: tap Add to cart on the product page. The drawer opens, and the line shows £89.10, the 3-month plan, and "Then £125 every 3 months / Skip or cancel anytime".
- [ ] 1-month plan: same check. Expect "Then £60 every month".
- [ ] One-time purchase: no terms line, and the quantity control works normally.
- [ ] Sticky bar at the bottom of the product page: "Add to cart" adds the 3-month plan when that plan is selected. With any other plan selected, it scrolls to the plan cards.
- [ ] At checkout, the selling plan is still attached and BF63 is applied (3-month first order £89.10).

## Inside the drawer

- [ ] Banner under the header reads "✓ BF63 APPLIED · SAVINGS + WELCOME KIT" on one line.
- [ ] Product block: "NAD+ Cellular Complex" lines up with the top of the image, with no big gaps. Price column: £89.10 and "every 3 months" in green, £210 crossed out in grey.
- [ ] Quantity buttons (− 1 +) and the bin sit under the price column. Plus and minus change the quantity and the totals update; the bin removes the line.
- [ ] Gifts row "6 welcome gifts, worth £72 · Free" opens and closes, and the open list doesn't break the layout.
- [ ] Totals: the gold "Black Friday savings" pill with the red saving, then Subtotal with the crossed-out and new totals.
- [ ] The checkout button looks like the product page's Add to cart: same font, "Checkout · £89.10" in sentence case, 4px corners.
- [ ] Express buttons (Shop Pay, Apple Pay, PayPal, Google Pay) sit in one compact row under Checkout, and Checkout stays the most prominent button.
- [ ] Trust block under the express buttons: "Arrives Fri 27th Nov · Royal Mail Tracked 24" on one line, then the guarantee line, then the Informed Sport and reviews line.
- [ ] On a 390×844 screen (iPhone 14) with one item, the checkout and express buttons are visible without scrolling.
- [ ] The drawer scrolls smoothly as one page, with no inner scroll box and no sideways scroll.

## Edge cases

- [ ] Two different products in the cart.
- [ ] Change the quantity, then check the drawer re-draws correctly (gifts, totals, banner).
- [ ] Empty cart: the empty state still shows Continue shopping.
- [ ] Open the drawer after 9pm UK time: the date moves on a day.
- [ ] Express checkout from the cart completes with a subscription (Shop Pay, and Apple Pay on iPhone), with the selling plan intact and BF63 applied (£89.10). Try it after adding from the top bar, the sticky bar and the product page.
- [ ] The full cart page (/cart) still works: it shows the plain jar image and a matching checkout button.
- [ ] In the Microsoft Clarity live view, these events fire: drawer_checkout_click, drawer_express_checkout_click, cart_gifts_expand, drawer_remove_item, drawer_continue_shopping, sticky_bar_click, tap_bf_offer, tap_announcement_bar.

# Cart drawer: what changed

Nearly all of it is in `snippets/cart-drawer.liquid`. The markup changes are marked with "(25 Nov)" comments, and the styles are in dated style blocks at the end of the file (rounds 1–18, later rounds override earlier ones). No prices or discount logic were changed.

| Area | Change | Where |
| --- | --- | --- |
| Product line | Name, supply, and terms over two lines ("Then £X every 3 months / Skip or cancel anytime"). The renewal price and interval come from the line's selling plan. | cart-drawer.liquid |
| Price column | Discounted price and "every 3 months" in the Add to cart green (#1e8f4e). The plan's full price (Shopify's compare-at price for the plan) is crossed out in grey. | cart-drawer.liquid |
| Quantity | The theme's own − / + buttons and bin, moved under the price column. Behaviour is unchanged from the original theme (no cap on subscriptions). | cart-drawer.liquid |
| Image | The NAD+ line shows a plain jar photo (gift-sq-forever-jar.jpg) in the drawer and on /cart. | cart-drawer.liquid, sections/main-cart-items.liquid |
| Gifts | Collapsed to one line, "N welcome gifts, worth £X · Free". The count and value come from the gift lines. Tap to expand. | cart-drawer.liquid |
| Banner | "✓ [code] applied · Savings + welcome kit" under the header. From 1 Dec it reads "Welcome kit included". | cart-drawer.liquid |
| Totals | Gold "Black Friday savings" pill with the saving in red, then Subtotal with the crossed-out and new totals. The old "Save" pill and the Cart/Delivery/Payment step tracker are gone. | cart-drawer.liquid |
| Checkout button | Same type as the product page's Add to cart: Neue Haas, weight 500, 17px, sentence case, 4px corners. | cart-drawer.liquid |
| Express checkout | Shopify's native accelerated-checkout buttons, in one compact row (44px, 4px corners). | cart-drawer.liquid |
| Trust block | Under the express buttons: the delivery date (same 9pm rule as the product page), the guarantee with its refund rate, and Informed Sport with the review count from REVIEWS.io. The old checklist (drawn by assets/muto-cart.css) is switched off in the drawer only. | cart-drawer.liquid, snippets/muto-royal-mail.liquid (new) |
| Layout | The whole drawer scrolls as one, so the checkout button shows without scrolling. | cart-drawer.liquid |
| Clarity | Click and expand events (see the checklist). | cart-drawer.liquid |

The drawer never had express checkout buttons before; nothing in the theme or Skio was hiding them. Shopify renders them in a closed shadow DOM and only offers a row or a full-width stack, so a 2×2 grid isn't possible.

# Product page: what changed

All on the main product template `product.muto-nad-bf-premium`. No separate v2 template was built; Richie asked for the changes to go on the main page.

| Area | Change | Where |
| --- | --- | --- |
| Hero copy | Eyebrow "NAD+ Cellular Complex · Two capsules a day". H1 "The daily energy and recovery formula for over-35s" (lowercase s via a small script). New subhead and supporting paragraph. | templates/product.muto-nad-bf-premium.json, snippets/muto-bf-buybox-copy.liquid, snippets/muto-buy-extras.liquid |
| Benefit bullets | Four bullets with fine-line icons, including "Got a wearable? Track the shift yourself." | snippets/muto-bf-mars.liquid, snippets/muto-buy-extras.liquid |
| Offer button | "Black Friday – extra 10% off" with a Copy code button (copies and applies BF63). Phase 1 only. | snippets/muto-buy-extras.liquid |
| Proof row | Under Add to cart: Informed Sport certified · Every batch tested · 90-day money-back guarantee · Subscriptions. The guarantee line was taken off the button and the "Give it 90 days" pill removed. | snippets/muto-buy-extras.liquid |
| Gifts | All gifts on one line. Tapping one opens its details full width underneath. | snippets/muto-buy-extras.liquid |
| Plan banner | "Black Friday offer – ends 30 November" ("Best value" from 1 Dec). | snippets/muto-bf-ag1-plans.liquid |
| "Simplify your routine" box | New copy listing NR, CoQ10, resveratrol, vitamin D3 and K2, zinc and copper, and a B complex. The per-day price line was removed. | snippets/muto-buy-extras.liquid |
| Benefits fold | Science-led copy (forms, doses, NR study). Informed Sport added to the Quality fold. | templates/product.muto-nad-bf-premium.json |
| What to expect | "No wearable?" paragraph and full guarantee terms moved here. Clinical trial now "January 2027". | templates/product.muto-nad-bf-premium.json |
| Reviews | The "Sound like you?" review box is removed. The rotating review strip stays. | templates/product.muto-nad-bf-premium.json |
| Sticky bar (mobile) | Product name, "Black Friday: 63% off + £72 free gifts", and a green Add to cart button. | sections/muto-bf-offer.liquid |

# Offer bars and the 1 December switch

The top bar and sticky bar copy for both phases lives in **Theme settings → Black Friday offer bars**. A new snippet, `snippets/muto-offer-phase.liquid`, rendered in the head of `layout/theme.liquid`, picks the phase in the visitor's browser. So Shopify's page cache can't hold the old copy, and nobody has to switch anything at midnight.

- **Which offer to show:** Automatic (default) switches to phase 2 at 2026-12-01T00:00:00Z. It can also be forced to Phase 1 or Phase 2.
- **Phase 1:** applies BF63 once per visit, and writes it onto the cart itself after every add or quantity change (top bar, sticky bar and product page alike). So checkout and express checkout from the cart both charge £89.10 for the 3-month plan. Any other code already on the cart is kept. If a setting is ever blank, the bars fall back to built-in wording. Copy: "Extra 10% off ends midnight Mon 30 Nov · 3 months for £89.10".
- **Phase 2:** "3 months for £125, then £150" copy and an Add to cart button. No code is applied. The offer button and the Black Friday labels hide themselves.
- **Top bar** (`snippets/muto-bf-bar.liquid`) is site-wide, so its copy shows on every page.
- `sections/muto-bf-head.liquid` and `sections/muto-bf-offer.liquid` also render on a `v2` template suffix. That's harmless if unused.

# Before publishing

Nothing is published, and nothing should go live until the mobile checklist passes and Richie signs off.

- [ ] **This theme also carries the wearable PDP work** from 23 Nov. Confirm that's meant to go live with it, or move these files onto a fresh copy of live (the store is at Shopify's 20-theme limit, so delete an old copy first).
- [ ] **BF63 ends at 23:30 UK on 30 Nov**, not 23:59, while the copy says midnight. Change the end time in Discounts.
- [ ] **Skio repricing on 1 Dec:** the 3-month plan is £99 then £125 today. The phase 2 copy says £125 then £150. Someone must change the Skio plan at midnight, or the bars will promise prices checkout doesn't charge.
- [ ] **"63% off"** on the sticky bar: the checkout maths gives about 58% (£89.10 against £210). Richie approved the wording; keep it only if that's still the call.
- [ ] **BF63 also applies** to the 1-month plan (£44.99 first month) and one-time purchase (£63). Confirm that's intended.
- [ ] **The plan cards** still show "£33/mo", "Save 53%" and "£1.10 a day", which conflict with £89.10 in the bars and cart.
- [ ] **Subscription quantity** can go above 1 again (an earlier brief asked to cap it at 1). Confirm that's intended.
- [ ] **Apple Pay** shows in Safari. Confirm all four express buttons fit one row on a 360px Android screen.
- [ ] **Compliance:** the Benefits fold has no authorised-claim line, and the paragraph under the H1 says "restore your energy, recovery". Run both past compliance.
