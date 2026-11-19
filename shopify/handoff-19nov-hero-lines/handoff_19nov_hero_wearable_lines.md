# MUTO main product page: hero wearable lines — dev handover

**Date:** 19 November 2026
**Page:** https://muto.co/products/muto-nad-cellular-complex
**Status:** on the unpublished duplicate theme and checked there. **Not on the live theme yet.**

## What to copy to live

One file, replacing the existing one at the same path:

| File | Change |
|---|---|
| `snippets/muto-bf-buybox-copy.liquid` | Two lines of hero copy under the headline |

It is in `MUTO_Hero_Lines_19Nov.zip` under `theme/snippets/`, and in GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`, at `shopify/pdp-cro/theme/snippets/`.

No template, section or settings change is needed, and nothing else depends on this file changing.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595

## What changed

Both lines sit in the intro paragraph under the product page headline, on phone and desktop.

| Line | Was | Now |
|---|---|---|
| Bold line ending the intro | Designed to be tracked on your wearable, so you don't have to take our word for it. | **Got a wearable device? Track the shift on your metrics over weeks and months.** |
| Grey line beneath | No wearable? A 30-second weekly score works just as well. And if it isn't for you by day 90, you get every subscription payment back. | **No wearable? Tracking isn't for everyone. A weekly check-in with yourself works too. Set a reminder, notice the difference, and if you don't by day 90, you get every payment back.** |

The first sentence of the intro ("NAD+ Cellular Complex is two capsules a day…") is unchanged.

## How it works

- Both lines are in the `<p class="mc-sub">` element near the top of the snippet, each wrapped in a `data-hero-b` span.
- They show when the hero version is B, which is the default (theme editor: product template > "MUTO BF style" > "Hero version"). Setting it to A, or adding `?hero=a` to the URL, hides both lines.
- To change the wording later, edit the text inside those two spans.

## Two wording points for Richie

These are his words as given; noted so they are a decision rather than an accident.

1. **"You get every payment back."** The guarantee covers subscriptions only, and the previous line said "every subscription payment back". The one-time purchase link is in the same buy box.
2. **"Track the shift on your metrics."** This tells the reader their numbers will move. The original brief asked for wearables to appear only as something to track, with no promised change.

## Checks after copying to live

Run at 375px and 1440px.

1. Under the headline, the bold line reads "Got a wearable device? Track the shift on your metrics over weeks and months."
2. The grey line beneath reads "No wearable? Tracking isn't for everyone…" and ends "you get every payment back."
3. The old line "Designed to be tracked on your wearable, so you don't have to take our word for it" no longer appears.
4. No JavaScript errors.

On the duplicate theme, all four passed at both sizes. Adding to cart was not re-tested after this change, as the file only holds copy.

## State of the earlier handovers

Checked on the live site at the time of writing:

- Main product page (29 files): on live.
- Payment icons and customer video order (2 files): on live.
- Welcome kit £72 and button labels (22 files): on live. The home page, FAQ page and product page show no £87; the bars read "Claim now" and the buy button "Add to Cart".
- This file: **not on live.** The live product page still shows the old "Designed to be tracked…" line.
