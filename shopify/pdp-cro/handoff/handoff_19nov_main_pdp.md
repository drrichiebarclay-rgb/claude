# MUTO main product page: dev handover

**Date:** 19 November 2026
**Page:** https://muto.co/products/muto-nad-cellular-complex (template `product.muto-nad-bf-premium`)
**Status:** built and checked on an unpublished duplicate of the live theme. **Nothing is on the live theme.**

## Where everything is

| What | Where |
|---|---|
| Preview | https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595 |
| Theme holding the work | "Clone Of Live \| PDP CRO audit [19-11]", ID 205307445595, duplicated from live on 19 Nov |
| Code | GitHub `drrichiebarclay-rgb/claude`, branch `claude/determined-mccarthy-8b759h`, folder `shopify/pdp-cro` |
| Files to copy to live | `shopify/pdp-cro/theme/` (29 files, same paths as the theme). Also in `MUTO_Main_PDP_19Nov.zip` |
| Originals for comparison | `shopify/pdp-cro/live/` (the live files as they were on 19 Nov) |
| Build script | `shopify/pdp-cro/apply.py`: rebuilds `theme/` from `live/` + `src/` by exact find and replace, and stops if a string is not found |
| Screenshots | `shopify/pdp-cro/screenshots/` |

## How to put it live

1. Check the live theme has not changed since 19 Nov (it was last updated 18 Nov). If it has, re-fetch the changed files into `live/`, run `python3 apply.py`, and fix anything it stops on.
2. Either publish the duplicate theme, or copy the 29 files in `theme/` into the live theme at the same paths.
3. If copying files: upload sections, snippets and assets **first**, and `templates/product.muto-nad-bf-premium.json` **last**. The template names two new sections; Shopify rejects it without an error message if they are not there yet.
4. Delete `templates/page.zz-survey-test.json` from the duplicate theme (a leftover test file; it is not in `theme/`).
5. Run the checks at the end of this document.

## What changed, by area

**One source for numbers and labels.** `snippets/muto-offer.liquid` holds the 3-Month kit worth (£72), the button label ("Start your 90-day test") and the line beside the stars ("Over 2,000 loyal subscribers"). Change them there only.

**Pricing wording.** Every £33/mo and £1.10 a day sits next to "for your first 3 months" or the renewal prices. The 1-Month plan is shown in plain pounds, with no percentage and no kit value, so the page has one discount figure (53%) and one kit value (£72). Comparison table cost row reads "£33 for your first 3 months, then £41.67–£50".

**Hero and buy box.**
- Sub-header "Designed for over 35s". Third bullet "Built for the years ahead".
- Subhead ends "Designed to be tracked on your wearable, so you don't have to take our word for it." plus a support line. This is hero variant B, now the default (see settings).
- Red "High demand" pill and dark "Black Friday is live" banner with a countdown, under the star rating.
- Value line above the plan cards ("Replaces 5 supplements in one…"); control line under them ("You're in charge…").
- Informed Sport badge under the testing and nutrition links.
- Button second line: "90-day money-back guarantee".
- Phones now show the same plan cards with gifts as desktop. The compact phone price-and-button block is switched off.
- "Sound like you?" chips: "Thinking about the next 20 years" first, replacing "Too many pots on the shelf". Kevin, 36 moved from third to sixth review.
- Future gifts: 3-Month "Box 4 on" reads "Box 4"; on the 1-Month plan the bottle is labelled Box 3.

**New section: trial results band** (`sections/muto-survey.liquid`), after the reviews ticker. Ring plus four tappable results (Energy 92%, Recovery 87%, Strain 93%, HRV 89%), a separate NAD+ study figure, and a footnote. A script lifts the "As seen in" press strip to sit directly above it.

**"What to expect"** (`sections/muto-expect.liquid`, rewritten). Interactive: five dots are tabs, one card shows the selected step, each with an "On your wearable" line. Opens on step 2.

**Test results pop-up** (`sections/muto-test-results.liquid`). New fifth tab "Informed Sport" with the certificate details and a link to the PDF.

**Cart drawer.** Cart, Delivery, Payment steps above the checkout button; five-line reassurance panel below it.

**FAQ.** New "How do I know this isn't a £99 placebo?"; "When will I notice something?" leads with two to four weeks; "How do I know it's working?" uses 7-day and 30-day averages.

**Sitewide effects.** The top bar, menu offer card and cart are shared, so their changes show on every page.

## Files (29)

New files are marked. Everything else is an edited copy of the live file.

| File | What it does |
|---|---|
| `snippets/muto-offer.liquid` (new) | Kit worth, button label, subscribers line |
| `snippets/muto-rating.liquid` (new) | Star score from review metafields + subscribers line |
| `snippets/muto-buy-extras.liquid` (new) | High demand pill, Black Friday banner and countdown, value line, control line |
| `snippets/muto-informed-sport.liquid` (new) | Informed Sport badge in the buy box and test results overview |
| `sections/muto-survey.liquid` (new) | Trial results band |
| `assets/muto-informed-sport.png` (new) | Informed Sport logo |
| `assets/muto-informed-sport-certificate.pdf` (new) | Informed Sport certificate |
| `sections/muto-expect.liquid` | Interactive timeline (rewritten) |
| `sections/muto-test-results.liquid` | Informed Sport tab |
| `sections/muto-bf-style.liquid` | Loads the new snippets; hero variant setting and analytics; rating sync |
| `sections/muto-bf-offer.liquid`, `assets/muto-bf-sticky.js` | Sticky bar label and "£99 for your first 3 months" |
| `sections/muto-menu.liquid`, `sections/muto-bf-topbar.liquid` | Menu offer card and unused defaults: £87 to shared £72 |
| `sections/muto-pdp-v2-buy.liquid`, `sections/muto-loved.liquid` | Rating line from the shared snippet |
| `snippets/muto-bf-buybox-copy.liquid` | Sub-header, subhead, button second line, photo flag |
| `snippets/muto-bf-mars.liquid` | Phone layout: bullet, rating, compact block switched off, Klarna icon removed |
| `snippets/muto-bf-ag1-plans.liquid`, `snippets/muto-bf-kit-grid.liquid` | Plan cards and kit worth |
| `snippets/muto-bf-bar.liquid` | Top bar wording and label (sitewide) |
| `snippets/muto-bf-compare-main.liquid` | Comparison table cost row |
| `snippets/muto-bf-review-box.liquid` | Chips and review order |
| `snippets/muto-bf-jobs.liquid` | "Replaces 5 supplements in one" card |
| `snippets/cart-drawer.liquid`, `assets/muto-cart.css` | Cart steps and reassurance panel |
| `assets/muto-bf-extra.css`, `assets/muto-bf-premium.css` | Hard-coded kit and saving text |
| `templates/product.muto-nad-bf-premium.json` | Copy, new sections, FAQ, gift labels, reviews AI summary off |

## Settings a non-developer can change

| Where in the theme editor | Setting | Now |
|---|---|---|
| Product template > "MUTO BF style" | Hero version | B (wearable line on). A removes it. `?hero=a` or `?hero=b` on the URL forces one |
| Product template > "MUTO — Survey results" | Eyebrow, heading, intro, results (blocks), study figure, small print, background | Background #FAFAFA |
| Product template > "MUTO — What to expect" | Open at; each step's "Wearable line" | Opens at step 2 |

## Things a developer needs to know

- **25-section limit.** The template had 25 sections. Adding the survey band meant removing the disabled "statement" section. Adding another section needs another removed.
- **Countdown.** Runs to 9pm UK time every day (`CUTOFF_HOUR` in `muto-buy-extras.liquid`), the next-day delivery cut-off, and says so in the banner. It is deliberately not tied to the offer: a nightly-resetting offer timer is false urgency.
- **High demand pill** reads shop metafield `muto.bf_orders_left` and prints the number. Nothing writes to it from this work.
- **Injected elements.** The banner, value line, control line and Informed Sport badge are placed by small scripts because the buy box is arranged by several existing files. The press strip is moved by a script in the survey section and can briefly show in its old place on a slow connection.
- **Hero analytics.** `data-hero-variant` on the buy box and sticky bar; `dataLayer` events `muto_hero_view` and `muto_add_to_cart` with `hero_variant`. The page-view event was seen firing; the add-to-cart event was not observed.
- **Reviews AI summary** is off (`enable_sentiment_analysis: false` on the reviews section).
- **Not touched:** pricing logic, discount functions, the subscription app, the orders-left metafield, the checkout.

## Open items

**Decisions for Richie**
1. Kit worth £72 assumes the Performance Bottle ships with Box 2, not the welcome kit.
2. "Over 2,000 loyal subscribers" sits beside a 4.8 rating that comes from about 107 reviews.
3. "89% report improved HRV" is on the page. The earlier brief said never to say HRV improves.
4. "51% rise in blood NAD+" is attributed to Conze et al., 2019 (a study of NR, not MUTO). Confirm that is the source. NAD+ has no authorised health claim.
5. "Studied in real people" / "12-week customer trial results" sit above a self-reported survey of 87.
6. Timing claims ("first couple of weeks", "within the first month") are worded as what customers say; confirm they can be stood behind.
7. "Fewer than 1 in 1,000 people ask for a refund" is in the cart; the v2 brief said to wait.
8. The 1-Month small print still says "thank-you gifts in boxes 2 to 6" although the bottle is now labelled Box 3.
9. "Only N welcome kits left": confirm the orders-left number is kept current.

**Not done**
- Klarna test checkout with a subscription in the cart.
- Rotating "Sound like you?" reviews box does not show on phones. Not investigated: check whether it shows on the live theme at phone width.
- Wearable screenshots, instalments, persona pages (out of scope).
- Box label changes are labels only; what ships is set in the subscription app.
- The first product photo has offer text and an Informed Sport logo baked into the image.

## Checks before and after go-live

Run at 375px and 1440px.

1. Page loads with no JavaScript errors.
2. Press "Start your 90-day test": cart shows NAD+ 3-Month subscription at £99 plus six gifts at £0.
3. Select 1-Month Supply and add: £49.99 with its gifts.
4. Trial results band: tapping each result moves the ring; Recovery reads 87%.
5. "What to expect": each dot opens its card; "Next" steps forward.
6. Informed Sport badge opens the test results pop-up on its fifth tab; the PDF link opens.
7. Countdown shows hours, minutes and seconds to 9pm UK time.
8. Cart drawer shows the three steps and the five-line panel.
9. Top bar and sticky bar fit without sideways scroll at 375px.
10. Search the theme: no "£87", no "within days".

Last verified on the preview on 19 Nov: items 1, 2, 4 (values), 7, 9 and 10. Items 3, 5 and 6 were verified earlier in the day, before later changes.
