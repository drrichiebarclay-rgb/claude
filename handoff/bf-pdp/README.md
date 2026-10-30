---
title: "MUTO Black Friday: go-live handover"
subtitle: "30 October 2026"
---

The Black Friday page and every cart change are built into a ready-to-publish copy of the live theme. You need to:

- check the Skio and stock items below
- publish the theme
- switch two products to the redirect template

# What's ready

**Theme:** "Black Friday | 30 Oct 2026 | dup of live" (ID **203930960219**), unpublished. It was duplicated from live at about 13:00 on 30 Oct, so it includes:

- your latest `custom.js`, with gifts by SKU and NAD+ moved to the top
- the cart drawer and settings as they were on live at that time
- every new section and template you'd already pushed

**Previews:**

- Black Friday page: <https://muto.co/products/bf-nad-cellular-complex?preview_theme_id=203930960219>
- After Black Friday: <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203930960219&view=muto-nad-trust>

**The Black Friday product** is **BF NAD+ Cellular Complex** (`/products/bf-nad-cellular-complex`). It's unlisted and already set to the `muto-nad-bf` template. Its Skio plans carry the offer prices:

- **3-month:** £99, then £125
- **Monthly:** £49.99, then £60

**Changed in this theme, compared with live:**

| File | Change |
|---|---|
| `templates/product.muto-nad-bf.json` | The Black Friday page (see "What the page does") |
| `templates/product.muto-bf-redirect.json` | New. For the main URL and -2: sends visitors to the BF product, keeping `utm_`, `gclid`, `fbclid` |
| `templates/product.muto-nad-trust.json` | The page without the offer, for main and -2 after Black Friday |
| `snippets/cart-drawer.liquid` | Three cart changes, listed below |
| `config/settings_data.json` | Gift lists in display order, listed below |
| `layout/theme.liquid` | Page speed, listed below |

**Cart drawer changes:**

- **Saving under the product line:**
  - **BF product:** "You save £111 on your first order".
  - **Main product:** "You save £60 every 3 months". "Ongoing" is removed everywhere.
- **Subtotal:** the crossed-out price is the product's compare-at (~~£210~~ £99 · Save £111). The gifts are shown separately as "+ £87 of free gifts" in a lime pill. Before, the gifts' values were added into the crossed-out total, which made ~~£296.99~~ and "Save £197.99".
- **Gift list order:** the travel vial now sorts with the bottle, so creatine comes first.

**Gift lists** (`cart_free_product_3m` and `cart_free_product`, in this order, which is the order they show in the cart and at checkout under NAD+):

| Plan | Products, in order |
|---|---|
| 3-month | creatine, socks, bottle, **travel vial**, **eBook**, **Forever Jar**, Garmin entry |
| Monthly | creatine, socks, **eBook**, **Forever Jar**, Garmin entry |

**Products created:**

| Product | Handle | SKU | Details |
|---|---|---|---|
| Travel Vial | `muto-travel-vial-free` | `TRAVEL-VIAL` | 3-month plan only |
| Forever Jar | `muto-forever-jar-free` | `FOREVER-JAR` | |

Both are £0 with a £10 compare-at, unlisted, stock not tracked, ship with the order, and have their photos. The eBook (`muto-ebook`) already existed.

# Before publishing

1. **Take the Black Friday 3-month plan off the main product in Skio. This is urgent: it affects the live site now.**
   - **The problem:** the BF plan (group `bf-subscription-refills-3-month`, selling plan **694836494683**, **£99**) is attached to the **main** product's 90-day variants as well as the BF product's. On today's live page it shows as an extra, unpriced "3-MONTH SUBSCRIPTION" card that sells at £99.
   - **The fix:** remove the main product's variants from that group.
   - **Already handled:** `muto-nad-trust` hides it on the main product by ID. The BF template doesn't hide it, because there it's the real plan.
2. **The third payment.** The page says "£99 for your first order, £125 on your second, £150 on your third." Skio shows £99, then £125 from the second order. Make sure £150 applies from the third.
3. **Orders left.** The black bar and the offer box read the shop metafield **`muto.bf_orders_left`** (now **481**). Nothing counts it down:
   - **To count it down:** add a Shopify Flow ("order created containing the BF product → decrease by 1"), or update it by hand (Settings → Custom data → Shop).
   - **At 0:** the box says "All 500 have gone."
4. **Live changes made after 13:00 on 30 Oct.** Copy anything changed on live after 13:00 on 30 Oct into this theme. That includes theme settings and app embeds.
5. **Warehouse.** The Forever Jar is now its own £0 line (it used to ship in every kit without one). Make sure each order still gets one jar, not two.

# Going live

1. **Run the checks** at the end of this doc on the preview.
2. **Publish** "Black Friday | 30 Oct 2026 | dup of live".
3. **Switch the templates** (Products → product → Theme template):

| URL | Black Friday | After Black Friday |
|---|---|---|
| `/products/bf-nad-cellular-complex` | `muto-nad-bf` (already set) | set the product to **Draft** |
| `/products/muto-nad-cellular-complex` (main) | **`muto-bf-redirect`** | `muto-nad-trust` |
| `/products/muto-nad-cellular-complex-2` | **`muto-bf-redirect`** | `muto-nad-trust` |

The redirect fires at the very top of `<head>` (in `theme.liquid`), with the template's own script as a back-up. It doesn't fire in the theme editor, so the main product stays editable. Ads and emails can also link to the BF product directly. A Shopify URL redirect won't work here, because those only apply to pages that don't exist.

4. **Announcement bar.** The Black Friday page hides the blue scrolling bar itself. On other pages, remove "EXTRA 10% OFF OUR QUARTERLY PLAN" and "ENDS ON 28.10.26". "£77 OF FREE GIFTS" is now **£87** for the 3-month plan.

`muto-nad-v2` stays in the theme, so any product can be switched back in one click.

# What the page does

The new main page has every `muto-nad-v2` section plus the new trust blocks. The Black Friday page adds the offer on top. In page order:

1. **Black bar** (Custom Liquid `bf_bar`):
   - **Position:** fixed to the top of the screen, 44px. The page, header included, starts 44px lower, so nothing sits under it. The theme pulls product content up under its see-through header, which is why the bar is fixed rather than in the page.
   - **Text:** "● BLACK FRIDAY 53% off your first order plus a welcome kit worth £87 · 481/500 left · Claim offer". Phones show the short version.
   - **Tap:** scrolls to the offer box.
   - **Stock count:** rendered in Liquid, so it's there from the first paint.
2. **Buy box**:
   - Opens on Quarterly before the first paint. The Custom Liquid `early` block runs straight after the buy box, so nothing jumps.
   - **Offer box above the plans:** "BLACK FRIDAY OFFER · 53% off your first order · plus a welcome kit worth £87 · £99 / £125 / £150", and "481 out of 500 remaining".
   - **Plan cards:** "£1.10 a day" (3-month) and "£1.79 a day" (monthly), each in a lime pill.
   - **Welcome kit:** 3-month includes the travel vial (~~£10~~).
   - **Under the button:** green Add to cart button with "90-day money-back guarantee", rotating stats, and the delivery line with the Royal Mail logo and a 9pm cut-off.
3. **"On this page" menu:** pins at 44px, under the bar.
4. **The rest of the page:**
   - The best is still ahead
   - The problem (four stats with sources)
   - Benefits
   - Science board
   - Standards
   - Customer videos
   - Rotating reviews
   - Ingredient library
   - Founder (stage photo)
   - Comparison ("See the difference for yourself.")
   - Timeline
   - How to take it
   - FAQs
   - REVIEWS.io widget

**Phones:** a smaller, tighter scale throughout: 28px headings, problem stats two by two, smaller cards. No sticky add-to-cart bar.

# Page speed

**In `theme.liquid`, on the new product templates only** (`muto-nad-bf`, `muto-nad-trust`, `muto-bf-redirect`; every other page is unchanged):

- `jquery-min.js`, `slick-min.js` and `custom.js` load with `defer`.
  - **Why only these templates:** I checked every section and snippet. Nothing on these pages uses jQuery inline, but other pages' sections do.
  - **Order:** `defer` keeps their order, and `custom.js` still waits for jQuery's ready.
- `slick.css` and `slick-theme.css` aren't loaded, because nothing on these pages uses Slick.
- `muto-crea.css`, `muto-home.css` and the two Neue Haas weights are preloaded.
- The BF redirect runs before anything else loads.

**In `theme.liquid`, on every page:**

- The OpenAI pixel has `debug: false`.
- The Usermaven loader has moved inside `<head>`.

**In the page:**

- The REVIEWS.io widget loads when the reader nears it, or once the page is idle.
- Images below the first screen are lazy and sized. Videos load only when tapped.
- The first product photo has high priority.

**Still open, for you:**

- **App embeds** load on every page: REVIEWS.io (two), Klaviyo, Elevar, Triple Whale, Clarity, Alia, Pandectes. Turn off any that aren't needed.
- **`custom.css`** (192 KB) blocks rendering on every page.
- **The NAD+ superscript code in `custom.js`** rewrites every "NAD+" text node after load, which is slow on long pages. Consider skipping it on these templates.
- **Measure** with PageSpeed Insights (mobile) on the BF product before and after publishing.

# Check before and after publishing

1. **Main URL and -2** land on the BF product, with `?utm_…` kept.
2. **Top of the page, phone and desktop:**
   - the black bar is at the very top, with the full header visible under it and no blue bar
   - the menu row never slides under the bar
   - the page opens on Quarterly and nothing jumps
3. **Only two plan cards** (Monthly, Quarterly) plus "Buy once".
4. **3-month in the cart:**
   - the line says "£1.10 a day" and "You save £111 on your first order"
   - the subtotal reads ~~£210~~ £99 · Save £111 · "+ £87 of free gifts"
   - the gifts read creatine, socks, bottle, travel vial, eBook, Forever Jar, Garmin, under NAD+
   - checkout lists them in the same order, starting with NAD+, and charges £99
5. **Monthly in the cart:**
   - £49.99 at checkout
   - gifts read creatine, socks, eBook, Forever Jar, Garmin
   - no travel vial
6. **Orders left:** change `muto.bf_orders_left` and both the bar and the box follow.
7. **Clicks:**
   - the bar scrolls to the offer box
   - each menu link goes to its section
   - "View third-party testing results" opens the certificates
   - the stars go to the reviews
   - videos play
8. **After Black Friday:** switch main and -2 to `muto-nad-trust` and set the BF product to Draft. There should be no bar, no offer box, normal prices, and "You save £60 every 3 months" in the cart.

# Files and source

- **Every file:** `MUTO_BF_PDP_30Oct2026.zip`, also in GitHub at `handoff/bf-pdp/` (repo drrichiebarclay-rgb/claude, branch `claude/gifted-wozniak-e239h5`).
- **Building the templates:** `shopify/pdp-trust/make_trust.py` and `make_bf.py` build them. Change copy there and rebuild, or tell Richie about manual edits so they aren't lost.
