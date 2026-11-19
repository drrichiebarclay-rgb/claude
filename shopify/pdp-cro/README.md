# MUTO main PDP fixes (19 Nov 2026)

Brief: "MUTO PDP fixes". Product page `/products/muto-nad-cellular-complex`, template `product.muto-nad-bf-premium`.

- `live/` the files as they were on the live theme on 19 Nov.
- `theme/` the edited files. These are on "Clone Of Live | PDP CRO audit [19-11]" (ID 205307445595), a duplicate of the live theme made on 19 Nov. Nothing is on the live theme. An earlier version (before the audit copy pass) is on draft 204807176539.
- `apply.py` rebuilds `theme/` from `live/` with exact find and replace; it stops if a string is not found the expected number of times.
- `screenshots/` 375px and 1440px captures from the preview.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=205307445595 (the wearable line is now the default; add `&hero=a` to see the hero without it).

## Single source of truth

`snippets/muto-offer.liquid` holds the kit worth (3-month £72, 1-month £62) and the button label ("Start your 90-day test"). Change them there only.
`snippets/muto-rating.liquid` prints the rating and review count from the product's review metafields.
Hero test: theme editor > product template > "MUTO BF style" section > `hero_variant` (B default: "Designed to be tracked on your wearable"; A: without it).

## Files changed

| File | Why |
|---|---|
| snippets/muto-offer.liquid (new) | One place for kit worth and button label |
| snippets/muto-rating.liquid (new) | Rating and count from review metafields |
| sections/muto-bf-style.liquid | Loads the shared values, hero A/B setting, keeps rating in step with the widget |
| snippets/muto-bf-buybox-copy.liquid | Hero B lines; "£33/mo for your first 3 months" |
| snippets/muto-bf-mars.liquid | Phone buy block: button label, rating, first-3-months wording, Klarna icon removed |
| snippets/muto-bf-ag1-plans.liquid | Desktop plan cards: "£1.10 a day for your first 3 months", kit worth |
| snippets/muto-bf-kit-grid.liquid | Kit worth from the shared value |
| snippets/muto-bf-bar.liquid | Top bar (sitewide): first-3-months wording, kit £72, button label |
| snippets/muto-bf-compare-main.liquid | Cost row: "£33 for your first 3 months, then £41.67–£50" |
| sections/muto-bf-offer.liquid | Sticky bar button label |
| assets/muto-bf-sticky.js | Sticky bar: "£99 for your first 3 months" |
| sections/muto-menu.liquid | Menu offer card: £87 to shared £72, button label |
| sections/muto-bf-topbar.liquid | Unused defaults £87 to £72 |
| assets/muto-bf-extra.css, assets/muto-bf-premium.css | Hard-coded £87/£72 text now reads the shared value |
| assets/muto-bf-copy.css | One-time line: "(no gifts, no money-back guarantee)" |
| sections/muto-pdp-v2-buy.liquid, sections/muto-loved.liquid | Rating text from metafields |
| snippets/cart-drawer.liquid | "Money-back policy" labels to "guarantee on subscriptions" |
| assets/muto-cart.css | Reassurance line under the checkout button |
| templates/product.muto-nad-bf-premium.json | "What to expect" copy, energy panel, FAQ, one-time label, button label, review AI summary off |

To go live, copy the files in `theme/` to the live theme.

## Audit copy pass (MLO Growth CRO audit, 19 Nov)

- Hero: "Designed to be tracked on your wearable, so you don't have to take our word for it." No promise that any wearable metric improves.
- "What to expect": first signs moved to weeks 1-2, each step tied to checking your own wearable or scores.
- FAQ: new "How do I know this isn't a £99 placebo?"; "When will I notice something?" leads with two to four weeks.
- Cart: a five-line checklist panel under checkout, including "Fewer than 1 in 1,000 people ask for a refund".
- Not built: wearable screenshots (needs real customer data), Klarna/instalments, persona pages.

## Timeline and Informed Sport (19 Nov, later)

- `sections/muto-expect.liquid` rewritten as an interactive timeline: the dots are tabs and one card shows the selected step. New setting "Open at" (the template opens at step 2, "Weeks 1-2"). Source in `src/`.
- `snippets/muto-informed-sport.liquid` (new) and `assets/muto-informed-sport.png` (new): the Informed Sport badge, placed in the buy box under the testing and nutrition links and in the test results panel's overview. Rendered from `sections/muto-bf-style.liquid`.
- `sections/muto-test-results.liquid`: a fifth tab, "Informed Sport", with the certificate details (LMS-PSRM-09495, 18 Nov 2026) and a link to the PDF (`assets/muto-informed-sport-certificate.pdf`). The buy box badge opens the panel at this tab.

## Third pass (19 Nov): survey block, Black Friday widget, notes, cart steps

- `sections/muto-survey.liquid` (new): the dark "wearable style" survey card under the buy box. Results are blocks; the NAD+ study figure is a separate setting with its own source.
- `snippets/muto-buy-extras.liquid` (new): "High demand" pill (reads shop metafield `muto.bf_orders_left`, never writes it), "Black Friday is live" banner with a countdown to the "Black Friday ends" setting on the "MUTO BF style" section (default 2026-11-30T23:59:59, UK time: confirm it), the "Replaces 5 supplements" value note and the subscription flexibility note.
- `snippets/muto-offer.liquid`: adds the "Over 2,000 loyal subscribers" line used beside the stars.
- 1-Month plan now shown in plain pounds (no percentage, no kit value) so the page has one discount figure and one kit value.
- `snippets/cart-drawer.liquid` + `assets/muto-cart.css`: Cart > Delivery > Payment steps above the checkout button.
- "What to expect": each step now has a tinted "On your wearable" line (block setting "Wearable line").
- Template: the disabled "statement" section was removed, because Shopify allows 25 sections per template and the survey block was the 26th.
- A test file `templates/page.zz-survey-test.json` is on the duplicate theme and can be deleted in the code editor.

## Fourth pass (19 Nov): brief v2 and survey band

- Survey band: now a white, clinical, full-width band about 365px tall on desktop, placed after the press and reviews ticker. Eyebrow "12-week customer trial results", heading "Studied in real people.", Recovery 87%.
- Countdown: runs to 9pm UK time each day, the next-day delivery cut-off, and is labelled as that (not as the end of the offer).
- Buy box: "Designed for over 35s" sub-header; bullet "Built for the years ahead" (P0.12); value line "One jar instead of five…" above the plans; control line "You're in charge…" under them and above the button.
- `snippets/muto-bf-review-box.liquid`: chip "Thinking about the next 20 years" first, replacing "Too many pots on the shelf" (option 2 of 4.5); Kevin, 36 moved from third to sixth slide (4.6; the order is set in the theme).
- Hero variant analytics (4.1): `data-hero-variant` on the buy box and sticky bar; dataLayer events `muto_hero_view` and `muto_add_to_cart` carry `hero_variant`.
- One-time line is back to "(no gifts)".
