# Black Friday: Claim offer + sticky plan bar + compact phone layout

On theme **"Black Friday | Claim offer + sticky bar | 31 Oct 2026"** (ID 203974869339), a duplicate of the live theme taken 31 Oct.

Preview: https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203974869339

## What's on the theme (`theme/`)
- `sections/muto-bf-offer.liquid`: added to the **footer group**. It only renders on the `product.muto-nad-bf` template. It loads the files below and hides the template's old `bf_bar`.
- `snippets/muto-bf-bar.liquid` + `assets/muto-bf-bar.css` + `assets/muto-bf-claim.js`: the black top bar. **Claim offer** adds the Quarterly plan (the variant on the product's 3-month Skio selling plan, read from the product) to the cart and goes straight to `/checkout`. If that plan is already in the cart it doesn't add it again. On phones it shows as a green pill.
- `assets/muto-bf-sticky.css` + `assets/muto-bf-sticky.js`: the sticky bar at the foot of the screen. It has the product image and name (desktop only), a plan picker and **Add to cart | £price**. The picker stays in step with the plan cards. The button submits the page's own cart form, the same way as the main button. The bar hides while the main Add to cart button is on screen.
- `assets/muto-bf-compact.css`: phones only (≤749px). The buy box is smaller and tighter: title, BF box, plan cards, gifts, one-time line and button.

- `assets/muto-bf-layout.css` + `assets/muto-bf-layout.js` (loaded by the bar snippet): Black Friday box at about half size, badges replaced by the testing-results button, image at the top on phones and tablets with arrows and swipe in place of thumbnails, no divider in the sticky button.

`live-snapshot/` holds the live template, buy section and CSS these were built against.

## After Black Friday
In Customize, delete "MUTO — Black Friday offer" from the footer.
