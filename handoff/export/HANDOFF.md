# MUTO site refresh: developer handoff (31 Oct 2026)

All work is on the unpublished preview theme **"Black Friday | Claim offer + sticky bar | 31 Oct"**
(`gid://shopify/OnlineStoreTheme/203974869339`). Preview: https://muto.co/?preview_theme_id=203974869339

Nothing has been published. `theme/` in this folder holds every file that differs from the live theme,
in the theme's own folder layout, and each one matches the preview theme byte for byte (all 61 checked against
Shopify's checksums at handover, 31 Oct). Simplest route to go live: **publish the preview theme**. If you merge
into another theme instead, copy `theme/` over it and see "Files in the Files area" below.

## Pages changed

| Page | Template |
| --- | --- |
| Home | `templates/index.json` |
| NAD+ Cellular Complex (Black Friday PDP) | `templates/product.muto-nad-bf.json` |
| Creatine / Socks / Bottle | `templates/product.muto-creatine.json`, `product.muto-socks.json`, `product.muto-bottle.json` |
| Science | `templates/page.science-simple.json` (page handle `science`) |
| About | `templates/page.about-us.json` (page handle `about`) |
| Ingredients | `templates/page.ingredients.json` |
| Quality standards | `templates/page.standards.json` |
| FAQs | `templates/page.faq-new.json` (page handle `faqs`) + `sections/faq-schema.liquid` |
| Other templates with copy updates only | `product.muto-nad-trust.json`, `product.muto-nad-v2.json` (test results), `page.about-muto.json`, `page.muto-home.json`, `page.lp-*.json` x8 (King's College London removed) |

## Site-wide behaviour: `sections/muto-bf-head.liquid` (first section in the header group)

One section, loaded on every page before the page is drawn. It holds:
- **Fonts**: `@font-face` for Neue Haas Grotesk Display (400/500/700) and Sometype Mono; `--mc-font` / `--mc-mono`.
- **Header**: plain on every page (no navy band, no glass pills; black logo/nav/icons on white).
  On the home page it overlays the first photo in white (`muto-home-top` prints `allow-transparent-header`).
  Menu drawer sits above all sticky bars on a solid panel.
- **Type rules**: heading weight 500 site-wide; Sometype Mono always uppercase (list of classes);
  superscripts don't change line height; footer headings weight 500; one button style.
- **"On this page" bar** (`sections/muto-section-nav.liquid`): hidden until it pins to the top on scroll.
  It measures whole section wrappers, so the highlighted chip matches the section on screen even where
  the page scales its sections with CSS `zoom` (the Black Friday PDP does: .93 desktop, .84 mobile).
- **Sticky add to cart on every page** except product pages, home, cart, accounts, password
  (`snippets/muto-sci-sticky.liquid`, NAD+ 3-month / 1-month, adds to cart then opens `/cart`).
- **Black Friday PDP only** (`template.suffix == 'muto-nad-bf'`): all BF styles (`assets/muto-bf-*.css`),
  the top bar + Claim, comparison swap.
- **Creatine/socks/bottle only**: `assets/muto-range-buy.css` (buy box in the PDP type scale, white plan boxes).
- **Structured data**: Organization + WebSite on home, Article on the science page.

## New sections (all in `sections/`, all editable in Customize)

| Section | Used on | What it is |
| --- | --- | --- |
| `muto-home-top` | Home | Header photo with words, mobile photo URL, review ticker |
| `muto-story` | About, Home | Layouts: who / mission / numbers / value / split / gallery / team |
| `muto-sci` | Science, Ingredients, Standards, About, FAQ, Home, range pages | Layouts incl. hero cards, shifts cards, statement, **banner (photo + Black Friday buy box)** |
| `muto-benefits` | PDP, Science, Creatine | Benefit tabs with photo, doses, claim, ingredient list |
| `muto-range` | Home, Socks, Bottle, Creatine | Shop the range: tabs, product, points, key doses |
| `muto-loved` | Home, PDP | "Loved by our community": 8 customer videos (Kate, David, Lucy, Adam Hamilton, Harry, Adam Facey, Max, Yolanda) between 10 written reviews; "Read all reviews" goes to the reviews section |
| `muto-howto` | PDP, Creatine | Step cards with photo |
| `muto-expect` | PDP, Creatine | Timeline (Day 1 → 90 / Week labels) |
| `muto-compare` | Home | Renders the "MUTO vs the usual" table straight into the page |
| `muto-cmp2` | Creatine | Two-way comparison (MUTO vs standard creatine), same look |
| `muto-sbar` | Home, Creatine, Socks, Bottle | Sticky add to cart: product's own variants, or NAD+ on home |
| `muto-section-nav` | PDP, Science | "On this page" chips: appear when the first linked section reaches the top, light up the section on screen |
| `muto-test-results` | PDP, Science, Ingredients, Standards, About | Certificates pop-up (real certificate data) |

The comparison table markup lives in `snippets/muto-bf-compare.liquid`, styles in `assets/muto-bf-compare.css`.

## Files in the Files area (Settings > Files), referenced as `shopify://shop_images/...`

Uploaded for this work: `muto-science-ride.jpg` (offer banner), `muto-science-bottle.jpg`, `muto-step-morning.jpg`,
`muto-about-runclub.jpg`, `muto-about-microscope.jpg`, `muto-creatine-scoop.jpg`.
These already exist on the store, so they don't need re-uploading if you publish this theme.

## Things to check before going live

1. **Selling plans**: the BF buy box, sticky bars and offer banners find the Skio plans by name
   (`3-month` / `1-month` in the plan name). Currently 3-MONTH SUBSCRIPTION (694836494683) and
   1-MONTH SUBSCRIPTION (694836461915). Test add to cart on each page.
2. **Black Friday copy to remove after 30 Nov**: top bar, "Black Friday: 3 months for £99" lines, offer banner
   (`muto-sci` banner sections), the FAQ price answer (faq_q21) and `faq-schema.liquid`.
3. **Open copy questions for the owner**: six vs seven advisers; welcome kit contents; monthly price
   (£60 in FAQ vs £49.99 on PDP); "no major allergens".
4. **Speed**: run PageSpeed Insights on mobile before and after publishing. Videos load on tap,
   images are sized per screen. Sometype Mono is a TTF; a WOFF2 copy would be smaller.
5. Three section presets (`muto-about-founder`, `muto-home-founder`, `muto-about-research`) still
   mention King's College London in their default text only. No live page shows it.
