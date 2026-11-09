---
title: "MUTO product pages: Black Friday top bar, welcome kit and url-2"
subtitle: "9 November 2026"
---

Fixes for the three Black Friday product pages. **The theme changes are already built in a duplicate of live: publish it, then switch url-2's template.** Nothing else on the site changes.

| Page | Template today | Template after this handover |
|---|---|---|
| Main: `/products/muto-nad-cellular-complex` | `product.muto-nad-bf-premium` | no change |
| url-2: `/products/muto-nad-cellular-complex-2` | `product.muto-nad-bf` | **`product.muto-nad-bf-premium`** (same as main) |
| url-3: `/products/muto-nad-cellular-complex-3` | `product.muto-nad-bf-v3` | no change |

# Before you start

- **Theme:** **Clone Of Live | BF top bar fix [09-11]** (ID 204572492123), a duplicate of live made on 9 Nov with the changes below loaded in. Unpublished.
- **Previews:**
  - <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=204572492123>
  - <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=204572492123>
  - <https://muto.co/products/muto-nad-cellular-complex-3?preview_theme_id=204572492123>
- **Files:** GitHub, repo `drrichiebarclay-rgb/claude`, branch `claude/exciting-allen-d0oqpz`, folder `shopify/bf-topbar-fix/`. The same files are in the duplicate theme.
- **Not yet tested on the real store.** It was built without access to muto.co and tested on a mock page only. Do the checks at the end on the previews before publishing.

# Step 1: check live hasn't changed since 9 Nov

The duplicate was made from live on 9 Nov, about 12:00 UK. If anyone has edited the live theme since then, those edits are not in the duplicate. Either copy them across or tell us before publishing.

# Step 2: test the previews (checklist at the end), then publish

Online Store → Themes → **Clone Of Live | BF top bar fix [09-11]** → Publish.

# Step 3: give url-2 the main page's design

After publishing:

1. Products → **NAD+ Cellular Complex** with the handle `muto-nad-cellular-complex-2`. There are several products with this title, so check the handle.
2. Theme template: change `muto-nad-bf` to **`muto-nad-bf-premium`**. Save.
3. Open url-2 and check it now looks exactly like the main page.

This is a product setting, so it changes the live page as soon as you save. Do it straight after publishing so url-2 never shows the old design on the new theme.

# Step 4: retire the old url-2 design

Once Step 3 is done and checked, the template `product.muto-nad-bf` is no longer used by any product.

1. Products: filter by theme template `muto-nad-bf` and confirm nothing is left on it.
2. Then delete `templates/product.muto-nad-bf.json` from the live theme, in Edit code. Keep a copy first; it's in the GitHub folder above.

Two side effects of retiring it, both expected:

- `layout/theme.liquid` loads jQuery, Slick and custom.js deferred only on the `muto-nad-bf`, `muto-nad-trust` and `muto-bf-redirect` templates. url-2 on the premium template loads them the normal way, exactly as the main page does today.
- The `muto-bf-style` section uses the premium design whenever the template suffix is `muto-nad-bf-premium`, so url-2 gets it automatically. No setting to change.

# What changed in the theme

All on the three Black Friday templates only. The header section `muto-bf-head` only renders on templates whose suffix contains `muto-nad-bf`.

## 1. "Claim →" top bar works from the first tap

**Why it was dead.** It was tapped 205 times on url-3 and 33 times on main with no response. There were three causes:

- The bar was a link to `#MainContent`. It only became a Claim button once `assets/muto-bf-claim.js` loaded, and that is deferred behind everything else, so early taps did nothing visible.
- Once loaded, each tap waited on three requests in a row: check the cart, add, then fetch the side cart.
- The premium designs hide the spinner (`.mc-bfx__spin{display:none!important}` in `muto-bf-premium.css` and `-v3.css`), so nothing changed on screen. Repeat taps were ignored as "busy".

**Fix:**

- `snippets/muto-bf-bar.liquid`:
  - **Real link.** The bar's link is now `/cart/add?id=<90-day variant>&quantity=1&selling_plan=<3-MONTH SUBSCRIPTION>`, so it works before any script has run.
  - **Which plan.** The variant is the first available one with a selling plan whose name contains "3-month". On all three products that is SKU `NAD-3M-Month1`.
  - **Inline script.** The Claim script is now inline, straight after the bar.
  - **One request per tap.** The cart is checked in the background as the page loads. The add (`/cart/add.js` with `sections`) returns the side cart in the same response.
  - **Instant feedback.** On tap the bar changes at once to "Adding your Black Friday offer…" with a spinner.
  - **Fallback.** If nothing has happened after 6 seconds, it falls back to the plain link.
- `assets/muto-bf-bar.css`: styles for the tapped state, written to override the premium CSS.
- `sections/muto-bf-head.liquid`: no longer loads `muto-bf-claim.js`. The file is still in the theme but unused; delete it later if you like.

## 2. Side cart shows the item and the full welcome kit

Two bugs found while testing, both fixed in the snippet above. The Claim now opens the cart exactly as the theme's own Add to cart does (`assets/product-form.js`):

- **Blank item list.** It removes `is-empty` from `<cart-drawer>` and `<cart-drawer-items>` before rendering. Before this, a cart that started empty opened with no items showing.
- **Missing gifts.** It publishes `PUB_SUB_EVENTS.cartUpdate`. That is what makes `custom.js` (`checkManualGiveAway`) add the free gifts:
  - The 3-month kit is creatine, socks, bottle, travel vial and the Garmin entry, per theme settings `cart_free_product_3m`.
  - The guide and Forever Jar are drawn by `snippets/cart-drawer.liquid` itself.
  - `PUB_SUB_EVENTS` and `publish` are top-level `const`/function declarations, so the code checks them with `typeof`, not `window.`.
  - If `custom.js` hasn't subscribed yet (a very early tap), it publishes on `load`.

## 3. Buy box: socks label

All three templates: "Performance socks (UK 6–11)" → **"Performance socks (one size fits all)"**. This is the `row_label` of the gift block `k1` in the `buy` section.

## 4. Buy box: each welcome-kit item opens into a box

`snippets/muto-bf-kit-box.liquid`, new and rendered by `muto-bf-head`.

- **What opens a box:** tapping a kit image tile, an itemised row ("… £12 Free") or a later-delivery tile.
- **What's in it:**
  - the photo at 900px wide;
  - the name;
  - the value, struck through, with "Free" or the row's own note, e.g. "Free entry";
  - a description, which is the image's alt text from the theme editor.
- **Closing:** with ×, a tap outside or Esc.
- **No side effects:** it doesn't change the selected plan.
- **Keyboard:** items get `role="button"` and `tabindex="0"`; Enter or Space opens.
- **Content:** nothing is typed in the snippet. It reads what the buy box drew, so editing a gift in the theme editor updates its box. To improve a box's description, edit that gift's **Alt text**.

# Files

| File | Change |
|---|---|
| `snippets/muto-bf-bar.liquid` | Rewritten: real link, inline Claim, side cart and gifts |
| `snippets/muto-bf-kit-box.liquid` | New |
| `sections/muto-bf-head.liquid` | Renders the kit box; no longer loads `muto-bf-claim.js` |
| `assets/muto-bf-bar.css` | Tapped state added at the end |
| `templates/product.muto-nad-bf.json` | Socks label (retired in Step 4) |
| `templates/product.muto-nad-bf-premium.json` | Socks label |
| `templates/product.muto-nad-bf-v3.json` | Socks label |

# Checks before and after publishing

On a phone, with an **empty cart** each time, on main, url-2 and url-3:

- [ ] Tap "Claim →" as soon as the page appears. It changes to "Adding your Black Friday offer…" immediately.
- [ ] The side cart opens with NAD+ Cellular Complex on the 90-day plan at £99.
- [ ] After the theme's loading spinner, it lists the full welcome kit: creatine, socks, bottle, travel vial, Garmin entry, 12-Week Protocol eBook and Forever Jar.
- [ ] Tap "Claim →" again. It doesn't add a second NAD+ line; it just opens the cart.
- [ ] With JavaScript off, or with a slow connection simulated, tapping the bar lands on the cart page with the 90-day plan in it. This is the plain `/cart/add` link with `selling_plan`. Shopify accepts it, but confirm Skio picks up the plan.
- [ ] Buy box: the socks row reads "Performance socks (one size fits all)".
- [ ] Tap each kit tile and each itemised row. A box opens with the right photo, name and value. The plan selection doesn't change.
- [ ] Desktop: the same checks, plus Esc closes the box.
- [ ] After Step 3: url-2 looks identical to main, and the checks above still pass on url-2.
- [ ] Place one test order through checkout from the Claim bar. Confirm the gifts and the £99 price carry through.
