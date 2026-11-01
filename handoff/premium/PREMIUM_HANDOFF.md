# MUTO NAD+ PDP, premium version: developer handover (1 Nov 2026)

**Template:** `templates/product.muto-nad-bf-premium.json`
**Theme:** unpublished preview theme "Black Friday | Claim offer + sticky bar | 31 Oct" (`gid://shopify/OnlineStoreTheme/203974869339`)
**Preview:** https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203974869339&view=muto-nad-bf-premium

Nothing is published. The `theme/` folder next to this file holds every file the premium page uses that differs from the
live theme, in the theme's own folder layout. All 34 files were checked byte for byte against the preview theme's checksums
on 1 Nov.

## Going live (pick one)

1. **Publish the preview theme, then assign the template.** Products > NAD+ Cellular Complex > Theme template >
   `muto-nad-bf-premium`. This is the simplest route.
2. **Merge into another theme.** Copy `theme/` over that theme, then assign the template as in option 1.
3. **Make it the standard BF template.** In `snippets/muto-bf-bar.liquid` (line 36), change the condition so that
   `muto-bf-premium.css` loads for `muto-nad-bf` too.

How it loads:
- `sections/muto-bf-head.liquid` is the first section in `header-group.json`. It loads all Black Friday styles when
  `template.suffix contains 'muto-nad-bf'`, so the premium template gets everything the standard one does.
- `snippets/muto-bf-bar.liquid` then adds `assets/muto-bf-premium.css` only when the suffix is `muto-nad-bf-premium`.
- The premium file is loaded last and is append-only: later blocks override earlier ones. Each block is headed with a
  comment ("Reformed pass", "Brand pass", "Timeline pass", and so on). **When editing, change the last block that sets
  a property.**

## Page order (template `order`)

| # | Section key | Type | Notes |
| --- | --- | --- | --- |
| 1 | `head_styles` | custom-liquid | Page styles (existing) |
| 2 | `bf_bar` | custom-liquid | Top bar: "While stock lasts" |
| 3 | `buy` | `muto-pdp-v2-buy` | Title block and buy box (details below) |
| 4 | `reviews_ticker` | `muto-ticker` (**new**) | 20 short customer quotes, scrolling |
| 5 | `early` | custom-liquid | Existing |
| 6 | `nav` | `muto-section-nav` | "On this page" chips; hidden until pinned |
| 7–19 | `statement` … `faq` | existing and new sections | Statement, problem stats, benefits picker (`muto-benefits`), scientific board, standards, `muto-loved` (videos and reviews), ingredient library, founder, comparison, timeline (`muto-expect`), how to take (`muto-howto`), FAQ |
| 20 | `reviews` | custom-reviews | Reviews widget (`#ReviewsWidget`, the target of "Read all reviews") |
| 21 | `tests` | `muto-test-results` | Certificates pop-up |
| 22–23 | `easy_read`, `bands` | custom-liquid | Existing helpers |

There are 23 sections; Shopify's limit is 25 per template. **Adding a third section saves silently without it.**

## Title block (above the buy box)

Settings are in `buy` (type `muto-pdp-v2-buy`). Several lines of copy are CSS `content`, so they are not in Customize.

| Order | What it shows | Source |
| --- | --- | --- |
| Photo | Product gallery; first on mobile | `.mc__buy-media{order:-10}` (`muto-bf-extra.css`) |
| 1 | Headline "MORE ENERGY. FASTER RECOVERY." (uppercase, 500) | `heading` setting |
| 1b | "Built for life after 35." | CSS `.mc__buy-title::after` (`muto-bf-extra.css`) |
| 2 | ★★★★★ "4.8 FROM 103 REVIEWS" (Sometype Mono capitals, underlined) | `rating_score` setting; styled in the premium "Timeline pass" |
| 3 | Grey pill with a badge icon: "90-DAY MONEY-BACK GUARANTEE" | **CSS** `.mc__eyebrow::before` (the hidden product label is reused; the icon is an inline SVG data URI) |
| 4 | Paragraph: "Five supplements in one daily jar for energy, recovery and healthy ageing. Every dose is on the label, so you know exactly what you take and why." | **CSS** `.mc__eyebrow::after` |
| 5 | Three points with short black bar markers: No proprietary blends / Third-party tested / Made in the UK | **CSS** `.mc-subhead::before` (the bars are a repeating gradient sized to the line height: 32px desktop, 30px mobile) |
| 6 | "BLACK FRIDAY: 3 MONTHS FOR £99 · WHILE STOCK LASTS" (mono capitals, one line on mobile) | CSS `.mc-subhead::after` |

To change any CSS copy, search `muto-bf-premium.css` for the text. The last occurrence wins.

## Buy box

- **Plans**:
  - **3-Month plan:**
    - a black band on top reading "BEST VALUE · SAVE 53% + FREE GIFTS WORTH £87" (`.mc__plan-save::before`);
    - a note "£1.10 per day · Save 53%".
  - **1-Month plan:** a note "£1.79 per day · Save 28%".
  - **Both notes:** CSS `.mc__plan-note::before`.
  - **Mobile:** the unselected plan collapses.
- **Includes list**:
  - `kit_itemised: true`; gifts are `gift` blocks in price order. The bottle is 3-Month only (`plans` = "2").
  - First row: "NAD⁺ Cellular Complex (x3)" / "(x1)", set by CSS per selected plan.
  - Gift totals: "Free gifts worth £87" (3-Month) and "£72" (1-Month), CSS `.mc__inc::after` in `muto-bf-extra.css`.
    **If a gift or its value changes, update the block and these totals.**
  - "Future monthly gifts" is kept as a slim row.
- **Add to cart and sticky bar:** black (`#242223`, hover `#000`), text centred.
- **Delivery date:** no background.
- **Drop-downs:** separate outlined boxes 10px apart, 14.5px text, 50px high, with a filled +/− circle.
- **Plan selection:** CSS keys off the selected plan with
  `.mc__plans:has(> label.mc__plan:nth-of-type(2).is-selected)` (Safari 15.4+ and all current browsers).

## Rest of the page (light touch, premium file only)

- **Look:** white backgrounds, hairline cards, mono capitals for tags, outlined review cards, black buttons.
- **Mobile:** body copy below the buy box is 1.5px larger.
- **Section zoom:** sections are scaled with CSS `zoom` (.93 desktop, .84 mobile; `muto-bf-layout.css`). The section
  nav measures whole section wrappers so its highlighting stays correct.
- **Reviews ticker (`sections/muto-ticker.liquid`):**
  - Quotes are `quote` blocks (text, name), editable in Customize, with space above and below set to 36px.
  - Scrolls with a CSS animation, pauses on hover, and stops for reduced motion.
  - Quotes are short extracts from real customer reviews, lightly trimmed (Becca, Jonathon R, Matteo M, Mathew H).
- **Certificates pop-up (`sections/muto-test-results.liquid`):**
  - Restyled in black and greys with an uppercase heading.
  - The laboratory certificate list, batch numbers and test dates are no longer shown. The `cert` blocks remain in the
    template for reference.
  - Shared with the standard PDP and the science, ingredients, standards and about pages.

## Cart (shared site-wide, needed for this page's flow)

- `assets/muto-cart.css` (loaded by `muto-bf-head`) restyles the cart page and drawer.
- `snippets/cart-drawer.liquid` and `sections/main-cart-items.liquid`:
  - add "3-MONTH SUPPLY" / "1-MONTH SUPPLY" under the NAD+ name, from the selling plan name ("3-MONTH" → 3-month;
    anything else, including one-off purchases, → 1-month);
  - the drawer's saving line reads "You save £X".
- `main-cart-items.liquid` is the stock Dawn file plus that one block.
- Under checkout: "Free UK delivery on subscriptions · 90-day money-back guarantee / Order before 9pm and receive it next day."

## Files (`theme/`)

- **Template:** `product.muto-nad-bf-premium.json`
- **Sections:**
  - `muto-bf-head`, `header-group.json`
  - `muto-ticker` (new), `muto-benefits`, `muto-loved`, `muto-expect`, `muto-howto`, `muto-section-nav`
  - `muto-test-results`, `muto-bf-offer`, `main-cart-items`
- **Snippets:** `muto-bf-bar`, `muto-bf-compare`, `cart-drawer`
- **Assets:**
  - `muto-bf-premium.css`
  - `muto-bf-bar/claim/compact/compare/copy/extra/layout/sticky/type` (.css/.js)
  - `muto-cart.css`
  - comparison images `muto-cmp-*.jpg/.svg`

Images uploaded to Settings > Files are referenced as `shopify://shop_images/...` and already exist on the store.

## Test before going live

1. **Add to cart from each plan, the sticky bar and the offer banner.**
   - Plans are found by name: 3-MONTH SUBSCRIPTION (694836494683) and 1-MONTH SUBSCRIPTION (694836461915).
   - Check the cart shows the right supply line and price.
2. **Mobile layout (iPhone width):**
   - photo first;
   - the offer line stays on one line;
   - the guarantee pill and the bar markers line up;
   - the ticker scrolls.
3. **Section nav:** it appears only once pinned, and each chip lands on its section.
4. **Copy to confirm with the owner:**
   - 90-day guarantee wording;
   - "Made in the UK";
   - six vs seven advisers;
   - £60 vs £49.99 monthly;
   - free delivery on all orders or subscriptions only;
   - "(x3)";
   - "no major allergens";
   - welcome kit contents.
5. **When Black Friday ends, remove:**
   - the top bar;
   - the "Black Friday: 3 months for £99" line (`.mc-subhead::after`, in both the desktop and mobile rules);
   - the black band copy;
   - the offer banners;
   - the FAQ price answer.
