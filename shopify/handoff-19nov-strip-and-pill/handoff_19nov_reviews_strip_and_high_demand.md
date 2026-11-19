# MUTO main product page: reviews strip position and "High demand" pill — dev handover

**Date:** 19 November 2026
**Page:** https://muto.co/products/muto-nad-cellular-complex
**Status:** both changes are on the unpublished duplicate theme and checked there. **Neither is on the live theme yet.**

## What to copy to live

Two files, each replacing the existing one at the same path. Order does not matter, and no template or settings change is needed.

| File | Change |
|---|---|
| `sections/muto-survey.liquid` | On phones, the scrolling reviews strip moves to sit directly above "As seen in" |
| `snippets/muto-buy-extras.liquid` | The red "High demand: only N welcome kits left" pill is removed |

Both are in `MUTO_PDP_Strip_and_Pill_19Nov.zip` under `theme/`, and in GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`, folder `shopify/pdp-cro/theme/`.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595

## 1. Scrolling reviews strip on phones

**What changed.** On phones the strip of scrolling customer quotes used to sit at the very top of the page, above the product photo. It now sits lower down, directly above the "As seen in" strip (Men's Fitness, Women's Fitness), which is where it already was on desktop.

Order on a phone is now: buy box, scrolling reviews strip, "As seen in", trial results section.

**How it works.**
- The strip is its own section (`reviews_ticker`) placed after the buy box in the template. An existing script lifts it to the top of the page on phones.
- The trial results section already had a script that lifts the "As seen in" strip to sit above it. That same script now also puts the reviews strip back directly above the "As seen in" wrapper, and gives it the same grey background.
- The code is in the `lift()` function near the bottom of `sections/muto-survey.liquid`, in the lines commented "Phones: another script lifts the moving reviews strip…". Remove those lines to send the strip back to the top of the page on phones.

**Things to know.**
- Desktop is unaffected: the strip was already in this position, so the script leaves it where it is.
- Because it is moved after the page loads, on a slow connection the strip may show briefly at the top before moving down.
- It depends on the trial results section being on the page. If that section is removed from the template, the strip goes back to the top on phones.
- The strip no longer appears above the photo on phones at all.

## 2. "High demand" pill removed

**What changed.** The red pill above the "Black Friday is live" banner ("High demand: only N welcome kits left") is gone, on phone and desktop. The banner and its countdown are unchanged and now sit directly under the star rating.

**How it works.** The pill's markup was deleted from the banner template in `snippets/muto-buy-extras.liquid`. Its CSS (`.mbx__hot`, `.mbx__dot`) is left in the file and is now unused.

**Things to know.**
- The snippet still reads the shop metafield `muto.bf_orders_left` into a variable, but nothing prints it any more. The metafield itself is untouched and still used elsewhere in the theme.
- Nothing else in the snippet changed: the banner, the delivery cut-off countdown, the "Replaces 5 supplements" line, the "You're in charge" line and the payment icons are as they were.

## Checks after copying to live

Run at 375px and 1440px.

1. Phone: the top of the page goes from the header straight to the product photo, with no scrolling quotes above it.
2. Phone: scrolling down past the buy box, the scrolling quotes strip appears directly above "As seen in", followed by the trial results section.
3. Desktop: the order is unchanged (scrolling strip, "As seen in", trial results).
4. Under the star rating, the "Black Friday is live" banner shows with its countdown and no red pill above it.
5. No JavaScript errors.

On the duplicate theme, all five passed at both sizes. Adding to cart was not re-tested after these two changes.

## State of the earlier handovers

Checked against the live theme at the time of writing:

- Main product page (29 files): on live.
- Payment icons and customer video order (2 files): on live.
- Welcome kit £72 and button labels (22 files): on live.
- Hero wearable lines (`snippets/muto-bf-buybox-copy.liquid`): on live, updated 14:37 today.
- These two files: **not on live.** The live page still shows the "High demand" pill.

## Still open

- Klarna test checkout with a subscription in the cart.
- The rotating "Sound like you?" reviews box does not show on phones: not investigated.
- Adding the 1-Month plan to the cart has not been tested.
- `templates/page.zz-survey-test.json` on the duplicate theme is a leftover test file to delete.
- Richie's open decisions from the main handover, less the orders-left figure, which no longer shows.
