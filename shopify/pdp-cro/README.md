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
