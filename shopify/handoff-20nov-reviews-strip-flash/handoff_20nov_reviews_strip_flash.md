# MUTO main product page: reviews strip flashing at the top on phones — dev handover

**Date:** 20 November 2026
**Page:** https://muto.co/products/muto-nad-cellular-complex
**Status:** fixed on the unpublished duplicate theme and checked there. **Not on the live theme yet.**

## What to copy to live

One file, replacing the existing one at the same path:

| File | Change |
|---|---|
| `sections/muto-survey.liquid` | The scrolling reviews strip no longer shows above the product photo while the phone page loads |

It is in `MUTO_PDP_Reviews_Strip_Flash_20Nov.zip` under `theme/sections/`, and in GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`, at `shopify/pdp-cro/theme/sections/`.

No template or settings change is needed. This replaces the version of the same file that went live at 17:00 on 19 November.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595

## The problem

On phones, the strip of scrolling customer quotes appeared at the top of the page, above the product photo, for several seconds while the page loaded, then disappeared and reappeared lower down above "As seen in".

**Cause.** Two scripts act on the same strip:
1. An older script (part of the phone layout) lifts the strip into the photo area at the top of the page.
2. The script added on 19 November moves it back down, directly above "As seen in". It only ran once the "As seen in" strip existed, and that strip is itself added late by another script.

In between, the strip was visible in the top position. On a throttled connection that gap measured about 7.5 seconds.

## The fix

Two changes, both in `sections/muto-survey.liquid`:

1. **A style rule hides the strip whenever it is in the top position:**
   `#MainContent .mc__buy-media [id$="__reviews_ticker"]{display:none!important}`
   So even if the older script puts it there, it is never seen.
2. **The move no longer waits for "As seen in".** The script is split into two functions:
   - `liftSeen()` lifts the "As seen in" strip above the trial results section, as before.
   - `placeTicker()` puts the reviews strip directly above the "As seen in" wrapper, or above the trial results section if that wrapper does not exist yet.
   Both run straight away, then every 150ms for about 12 seconds, and once more on window load, so the strip is put back if the older script moves it again.

## Things a developer needs to know

- **The hide rule lives in this section's stylesheet.** If the trial results section is removed from the product template, the rule goes with it and the strip returns to the top of the page on phones, as it was before 19 November.
- **The rule is not limited to phones.** On desktop the strip is never placed in the photo area, so the rule has no effect there.
- **The older lifting script is untouched.** The cleaner long-term fix is to remove that behaviour from the phone layout so nothing needs hiding or moving back. This was not done because that script also arranges other parts of the phone layout.
- **The polling is cheap:** two DOM lookups per pass, about 80 passes, then it stops.

## Checks after copying to live

1. On a phone, load the page (ideally on mobile data, or with throttling in browser dev tools): no scrolling quotes strip appears above the product photo at any point.
2. On a phone, scroll past the buy box: the scrolling strip sits directly above "As seen in", followed by the trial results section.
3. On desktop: order unchanged (scrolling strip, "As seen in", trial results).
4. No JavaScript errors.

On the duplicate theme:
- Check 1: two recorded loads on a simulated phone with a throttled connection and 4x slower processor. Before the fix the strip sat at the top from about 4.6s to 12.2s. After the fix it never appeared there in either recording; it first shows already in its final area.
- Checks 2 to 4 passed at 375px and 1440px.
- This was tested in Chromium's phone emulation, **not on a real iPhone in Safari**. It should be confirmed on a real device.

## State of the earlier handovers

Checked against the live theme at the time of writing:

- Main product page, payment icons and video order, welcome kit £72 and button labels, hero wearable lines: on live.
- Reviews strip position and "High demand" pill removal (two files, 19 Nov): on live, updated 17:00 on 19 November.
- This file: **not on live.** Live has the 19 November version, which still shows the flash.
