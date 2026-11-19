# MUTO: welcome kit £72 everywhere, and new button labels — dev handover

**Date:** 19 November 2026
**Status:** both changes are on the unpublished duplicate theme and checked there. **Neither is on the live theme yet.**

Two separate changes, delivered together as one set of 22 files:

1. **Welcome kit worth £72, not £87**, on every page where £87 was found (16 files).
2. **Button labels:** "Add to Cart" on the product page buy button, "Claim now" on the bars (6 files).

No file is in both groups.

## Where everything is

| What | Where |
|---|---|
| Preview | https://muto.co/?preview_theme_id=205307445595 (home) and https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595 (product page) |
| Theme holding the work | "Clone Of Live \| PDP CRO audit [19-11]", ID 205307445595 |
| Files to copy to live | `MUTO_Kit72_Buttons_19Nov.zip`, folder `theme/` (22 files, same paths as the theme) |
| Code | GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`: `shopify/kit-72` and `shopify/pdp-cro` |

## How to put it live

1. Copy the snippets and sections first (7 files).
2. Copy the 15 templates last.
3. Run the checks at the end.

`sections/muto-sci.liquid` and the bars read their values from `snippets/muto-offer.liquid`, which is in this set, so copy that snippet before anything else.

**Before overwriting templates:** the 14 kit-figure templates were taken from live on 19 Nov. If any has been edited in the theme editor since, re-make the change on the current version instead: search the file for `£87` and replace with `£72`.

## Change 1: welcome kit worth £72 (16 files)

Only the figure changes. No layout, pricing logic or settings are touched.

| File | Where the figure shows | £87 replaced |
|---|---|---|
| `templates/index.json` | Home page: the Black Friday bar in the header (visible text and screen-reader label) and the offer card | 3 |
| `sections/muto-sci.liquid` | The offer card's "£1.10 a day · free welcome kit worth…" line, on every page with the card | 1 (now the shared value) |
| `sections/faq-schema.liquid` | FAQ page: the question-and-answer data search engines read | 1 |
| `templates/page.faq-new.json` | FAQ page: the pricing answer and the offer card | 2 |
| `templates/page.about-us.json` | Offer card | 1 |
| `templates/page.ingredients.json` | Offer card | 1 |
| `templates/page.science-simple.json` | Offer card | 1 |
| `templates/page.standards.json` | Offer card | 1 |
| `templates/product.muto-bottle.json` | Offer card | 1 |
| `templates/product.muto-creatine.json` | Offer card | 1 |
| `templates/product.muto-socks.json` | Offer card | 1 |
| `templates/product.muto-nad-bf.json` | Older NAD+ product page: plan details, offer box, in-page bar | 4 |
| `templates/product.muto-nad-bf-premium-2.json` | NAD+ product page version: same three places | 4 |
| `templates/product.muto-nad-bf-lsttesta.json` | NAD+ test page A: plan details, offer box | 3 |
| `templates/product.muto-nad-bf-lsttestb.json` | NAD+ test page B: plan details, offer box | 3 |
| `templates/product.muto-nad-trust.json` | NAD+ "trust" page: plans banner and plan details | 2 |

**Why the home page was missed before.** Most pages draw the Black Friday header bar from `snippets/muto-bf-bar.liquid`, corrected this morning. The home page has its own copy of the bar, typed into a custom-liquid section in `templates/index.json`.

## Change 2: button labels (6 files)

| Where | Was | Now |
|---|---|---|
| Product page buy button | Start your 90-day test | **Add to Cart** |
| Sticky bar | Start your 90-day test | **Claim now** |
| Black Friday top bar (every page except home) | Start your 90-day test → | **Claim now →** |
| Menu offer card | Start your 90-day test | **Claim now** |

The top bar and menu card were not specified in the request; they were set to match the sticky bar.

| File | What changed |
|---|---|
| `snippets/muto-offer.liquid` | The single source. `cta` is now "Add to Cart"; new `cta_bar` is "Claim now" |
| `snippets/muto-bf-bar.liquid` | Top bar uses `cta_bar` (label and screen-reader text) |
| `sections/muto-bf-offer.liquid` | Sticky bar button uses `cta_bar` |
| `sections/muto-menu.liquid` | Menu offer card falls back to `cta_bar` |
| `sections/muto-bf-style.liquid` | The add-to-cart analytics event also recognises "Claim now" |
| `templates/product.muto-nad-bf-premium.json` | Buy button label setting; in-page bar uses `cta_bar` |

To change a label later, edit `snippets/muto-offer.liquid` only. The buy button's own label also sits in the product template setting `cta_label`, so change both for the product page.

## Things a developer needs to know

- **Not searched for £87:** every template, the header and footer groups, and roughly 120 sections, snippets and assets were searched. The remaining sections and snippets were not. A theme-wide search for `£87` in the code editor after go-live will confirm nothing is left.
- **Home page bar is otherwise unchanged.** It still reads "£1.10 a day" without "for your first 3 months" and its button says "Claim". It was not part of either request.
- **Offer card is otherwise unchanged:** it still shows "£1.10 a day" on its own.
- **The five alternate NAD+ product page versions** were changed but not opened, as they are not the template the product currently uses.

## Checks after copying to live

Run at 375px and 1440px.

1. Home page: header bar reads "free welcome kit worth £72".
2. Home, science, FAQs, ingredients, quality standards and the creatine product page: the "3 months for £99" offer card reads £72 in both lines.
3. FAQ page: the pricing answer reads £72; view source and search for `£87`: none.
4. Product page: buy button reads "Add to Cart"; sticky bar reads "Claim now"; top bar reads "Claim now →"; menu offer card reads "Claim now".
5. Press "Add to Cart": the 3-Month subscription is added at £99 with the six gifts.
6. No JavaScript errors.

On the duplicate theme:
- Checks 1 to 3 passed on desktop, across home, science, FAQs, ingredients, quality standards, story, creatine, shop all, cart and the main product page (zero £87 on each). Not re-run at phone width.
- Check 4 passed at both sizes.
- Check 5 passed at phone width; not re-run on desktop after the label change.
- Check 6 passed on the pages above.

## State of the earlier handovers

- Main product page (29 files): on live.
- Payment icons and customer video order (2 files): on live, updated 11:54 today.
- This set (22 files): **not on live.**
