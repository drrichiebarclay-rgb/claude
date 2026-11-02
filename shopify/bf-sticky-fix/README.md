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
- **MUTO — Black Friday top bar**: pick the product.
- **MUTO — Sticky add to cart**: pick the product. Name it anything but `sticky`.

## Check before publishing

- **Home page**: if the home template's sticky section already has a product set (it was labelled "for structured data"), the bar now sells that product with plan options built from Skio. Before, it showed the hard-coded NAD+ bar ("3-Month Supply (Save 53%) · £1.10 a day · £99"). Check the wording, or clear the product to keep the old bar.
- Test on a page with each bar:
  - the plan added to the cart has the right selling plan
  - Claim goes to checkout
  - only one sticky bar shows
