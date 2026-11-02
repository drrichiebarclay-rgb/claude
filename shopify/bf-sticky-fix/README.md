# Black Friday: sticky add to cart and top bar on any page

For the theme **Black Friday | Claim offer + sticky bar | 31 Oct** (ID 203974869339). Built on that theme's files as they were on 2 Nov 2026 (muto-sbar and muto-sci-sticky last saved 05:29 UTC).

## The problem

Both bars only worked on the Black Friday product page:

- **Sticky add to cart** (`sections/muto-sbar.liquid`): on a page there is no `product`, so the section went straight to the hard-coded NAD+ bar and ignored the product picked in its settings.
- **Site-wide sticky** (`snippets/muto-sci-sticky.liquid`, drawn by `muto-bf-head` on every page) and the section bar both used `id="mc-sbar"`. Adding the section to a page put two bars with the same id on it, and the section's script picked up the other bar. That broke the section.
- **Top bar**: only drawn by `muto-bf-head` when the template suffix contains `muto-nad-bf`, using the page's own product. Nothing could add it to another page, and `muto-bf-claim.js` looks for one fixed id.

## Files to copy (3)

| File | What changed |
|---|---|
| `sections/muto-sbar.liquid` | **Product** setting now picks what the bar sells, on any template. Blank: the page's own product, or the NAD+ bar on non-product pages. Its own id per section (`mc-sbar-<section id>`), and a script that only touches its own bar. |
| `sections/muto-bf-topbar.liquid` | **New.** The black "Claim →" top bar as a section for any template, with a product picker and plan setting. Own id and own script; doesn't use the template suffix. |
| `snippets/muto-sci-sticky.liquid` | No id any more (class `mc-sbar--site`). Its script finds its own bar, keeps one copy if drawn twice, and removes itself before showing when the page has a sticky section. |

Copy sections first, then the snippet. No template or asset changes needed: both sections use the existing `muto-bf-sticky.css` and `muto-bf-bar.css`.

## Sticky add to cart: settings

- **Product**: what the bar sells.
- **Pre-select the option containing** (default `3-month`).
- Options:
  - For products on Skio plans: one option per selling plan (first available variant with that plan, at the plan's price, with "Save X%" when Shopify has a compare-at price).
  - For plain products: one option per variant.
- **Rename plan 1 / 2**: turns "3-MONTH SUBSCRIPTION" into "3-Month Supply" and similar. Defaults cover NAD+.
- **Add a one-time purchase option** (off by default).
- **After adding**: open the cart (default) or go straight to checkout.
- **Show after scrolling** (default 500px).
- On the Black Friday product template it stays hidden (the Black Friday offer bar already sells that product), unless it's set to a different product.

## Top bar: settings

- **Product**: blank uses the page's own product (product pages only).
- **Plan name contains** (default `3-month`): the Skio plan "Claim" adds. With no match it adds the first available variant, one-time.
- **After Claim**: checkout (default) or cart. A second tap doesn't add a second box.
- **Text**: desktop line, after-the-dot line, phone line, link text, screen reader text.
- Hidden on the Black Friday product template, which draws its own top bar from `muto-bf-head`. If two top bars reach a page, the second removes itself.
- Don't name the section `bf_bar` in a template: `muto-bf-bar.css` hides sections with ids ending in `__bf_bar`.

## How to use on a page

In the theme editor, open the page template, then **Add section**:
- **MUTO — BF top bar**: pick the product.
- **MUTO — Sticky add to cart**: pick the product. Name it anything but `sticky`.

## Check before publishing

- **Home page**: if the home template's sticky section already has a product set (it was labelled "for structured data"), the bar now sells that product with plan options built from Skio. Before, it showed the hard-coded NAD+ bar ("3-Month Supply (Save 53%) · £1.10 a day · £99"). Check the wording, or clear the product to keep the old bar.
- Test on a page with each bar:
  - the plan added to the cart has the right selling plan
  - Claim goes to checkout
  - only one sticky bar shows

## Update, 2 Nov: same design as the product page, and Claim opens the cart

Uploaded to the Black Friday theme (all files checked against the theme's checksums).

- **`snippets/muto-sbar-style.liquid`** (new): the product page's sticky bar sizes (from `muto-bf-type.css` and the desktop step in `muto-bf-extra.css`, which only load on that page), scoped to the site-wide bar and the section bar. Both bars render it, so they look like the product page's bar: 44px photo, 48px picker and button, the same type sizes, price inside the button, turquoise button.
- **`sections/muto-sbar.liquid`** and **`snippets/muto-sci-sticky.liquid`**: render that snippet and show the price in the button. Section prices print without trailing zeros (£99, not £99.00).
- **`assets/muto-bf-claim.js`**: the product page's Claim now opens the cart instead of going straight to checkout. `snippets/muto-bf-bar.liquid` screen reader text updated to match. Both files are committed first as snapshots of the theme, so the diff shows only the change.
- **`sections/muto-bf-topbar.liquid`**: "After Claim" now defaults to "Open the cart".

## Update, 2 Nov: Claim and Add to cart open the side cart

The theme's cart is set to "drawer" (Dawn's cart drawer). Claim on the Black Friday product pages (standard and premium), the BF top bar section, the sticky add to cart section and the site-wide sticky bar now:

1. add the plan to the cart,
2. fetch fresh `cart-drawer` and `cart-icon-bubble` sections (Shopify's Section Rendering API, as Dawn's own Add to cart does),
3. call the drawer's `renderContents`, which updates it and slides it open.

If a page has no drawer, they fall back to the cart page. "Go straight to checkout" is still an option on the two sections. Uploaded and checked against the theme's checksums.

## Update, 2 Nov: sticky add to cart on every page

`sections/muto-bf-head.liquid` (in the header group, so on every page) now draws a sticky add to cart everywhere except the cart, password and gift card pages:

- **Product pages:** a bar for that page's own product (`snippets/muto-sbar-bar.liquid`), with its Skio plans or variants. Skipped on the Black Friday templates (they draw their own plan bar) and the giveaway template.
- **Every other page** (home, pages, collections, blog, search, 404, account): the NAD+ bar (`snippets/muto-sci-sticky.liquid`).
- **No doubles:** either bar removes itself if the page already has its own sticky bar. That covers a "MUTO — Sticky add to cart" section, the home page's "MUTO Home — Sticky cart" (`data-mh-sticky`), a landing page's offer bar (`.mlp-bar`), or any section whose id ends in `__sticky`.

The bar markup moved from `sections/muto-sbar.liquid` into `snippets/muto-sbar-bar.liquid`, so the section and the head use the same bar. The section's settings are unchanged.
