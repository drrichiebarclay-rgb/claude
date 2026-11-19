# MUTO main product page: dev handover for two follow-up changes

**Date:** 19 November 2026
**Page:** https://muto.co/products/muto-nad-cellular-complex
**Status:** both changes are on the unpublished duplicate theme and checked there. **Neither is on the live theme yet.**

These follow the main handover (`handoff_19nov_main_pdp.md`). The live theme already has everything from that handover, including the product template: checked on the live page at the time of writing. Only the two files below are newer than live.

## What to copy to live

| File | Change | New on live? |
|---|---|---|
| `snippets/muto-buy-extras.liquid` | Adds a row of payment icons under the "Arrives by … Tracked 24h" line | No, replaces the existing file |
| `snippets/muto-bf-video-reviews.liquid` | New order for the five customer videos in the buy box | No, replaces the existing file |

Both are in `MUTO_PDP_Followup_19Nov.zip` under `theme/snippets/`, and in GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`, folder `shopify/pdp-cro/theme/snippets/`.

Copy both into the live theme at the same paths. Order does not matter, and no template or settings change is needed.

Preview of the result: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595

## 1. Payment icons

**What it shows.** One centred row of nine icons under the delivery line in the buy box, on phone and desktop: American Express, Apple Pay, Google Pay, Klarna, Maestro, Mastercard, PayPal, Shop Pay, Visa.

**How it works.**
- The list is Shopify's own `shop.enabled_payment_types`, so it reflects what the store accepts and changes if a method is switched on or off in Shopify payments.
- Seven enabled types are deliberately left out, in the `mpay_skip` list at the top of the template block: Bancontact, Diners Club, Discover, JCB, UnionPay, MB WAY, Satispay. To show one again, remove it from that list. To hide another, add its Shopify type name.
- Klarna is in Shopify's list today. If it were ever switched off, the snippet would still print a Klarna icon (there is an explicit fallback line, at Richie's request). Remove that line if Klarna stops being offered.
- The row never wraps: icons shrink to fit (38px wide on desktop, 33px at 375px, 27px at 320px).
- It is placed by the snippet's script, straight after `.mpb-x .mpb-del` (the "Arrives by" line). If that line is renamed or removed, the icons will not appear.

**Open point.** Klarna is shown next to a subscription button. Whether Klarna is actually offered at checkout with a subscription in the cart has not been tested.

## 2. Customer video order

**What changed.** In "Real customers, real reviews" in the buy box, the five videos now run: David Mercado, Adam Hamilton, Kate Bright, Adam Facey, Lucy Halliday. (Was: Kate Bright, Lucy Halliday, David Mercado, Adam Facey, Adam Hamilton.)

**How it works.** The order is the order of entries in the `V` list near the top of the snippet (`name|video id|bitrate|age|life stage`, separated by `;`). Only the order changed; no video, poster or name was edited.

**Not changed.** The separate "In their words" section further down the page has its own nine videos, set in the product template. Its order is untouched.

## Checks after copying to live

Run at 375px and 1440px.

1. Under "Arrives by … Tracked 24h": nine payment icons on a single row, no Bancontact, Diners, Discover, JCB, UnionPay, MB WAY or Satispay.
2. "Real customers, real reviews": first video is David Mercado, last is Lucy Halliday; each still plays.
3. No JavaScript errors.
4. "Start your 90-day test" still adds the 3-Month subscription at £99 with the gifts.

On the duplicate theme, checks 1 and 3 passed at both sizes, and the video order in check 2 is correct. Video playback and check 4 were not re-run after these two changes.

## Still open from the main handover

- Klarna test checkout with a subscription in the cart.
- The rotating "Sound like you?" reviews box does not show on phones: not investigated.
- Adding the 1-Month plan to the cart has not been tested.
- The decisions listed for Richie in the main handover (kit worth, subscriber count, HRV and NAD+ figures, "trial" wording, orders-left number).
- `templates/page.zz-survey-test.json` on the duplicate theme is a leftover test file to delete.
