---
title: "MUTO Black Friday: BF product page, with the main URL and -2 pointing to it"
subtitle: "30 October 2026"
---

For Black Friday, the offer lives on its own product, **BF NAD+ Cellular Complex** (`/products/bf-nad-cellular-complex`). It's already created, unlisted, set to the **`muto-nad-bf`** template, and its Skio plans carry the Black Friday prices:
- **3-month:** £99, then £125.
- **Monthly:** £49.99, then £60.

The **main URL and -2 send visitors to it** for the duration, using a small redirect template that keeps tracking parameters. After Black Friday they switch to `muto-nad-trust`, the new page without the offer.

The page itself is the new main page (every live section plus the new trust blocks) with the Black Friday offer on top:
- **Sticky black bar:** "Black Friday · 53% off your first order plus a welcome kit worth £87 · 481/500 left · Claim offer".
- **Offer box above the plans:** white, with a live count of orders left out of 500.
- **Plan cards:** Black Friday pricing, with the daily cost in a lime pill.

# The quick route: publish the Black Friday theme

Everything below is already built into a copy of the live theme, **"Black Friday | 30 Oct 2026 | dup of live" (ID 203930960219)**. It was duplicated from live at about 13:00 on 30 Oct, so it has your latest `custom.js` (with the NAD+-first ordering), cart drawer and settings, plus:

| File | Change |
|---|---|
| `layout/theme.liquid` | Page speed: see "Page speed" below |
| `snippets/cart-drawer.liquid` | The BF product's saving reads "You save £111 on your first order" (no "ongoing" anywhere). The travel vial sorts with the bottle. The subtotal is anchored on the product's compare-at, ~~£210~~ £99 · Save £111, with "+ £87 of free gifts" in a lime pill underneath, where the gifts used to be added into the crossed-out total |
| `config/settings_data.json` | Gift lists in display order. 3-month: creatine, socks, bottle, travel vial, eBook, Forever Jar, Garmin. Monthly: creatine, socks, eBook, Forever Jar, Garmin |
| `templates/product.muto-nad-bf.json` | The Black Friday page |
| `templates/product.muto-bf-redirect.json` | For main and -2: sends visitors to the BF product |
| `templates/product.muto-nad-trust.json` | The page without the offer, for after Black Friday |

Preview: <https://muto.co/products/bf-nad-cellular-complex?preview_theme_id=203930960219>

To go live:
1. **Port newer live changes.** Copy anything changed on live since 13:00 on 30 Oct into this theme.
2. **Publish it.** Run the checks at the end first.
3. **Switch the main URL and -2 to `muto-bf-redirect`** (step 3).
4. **Do the "Must be done" items.**

Steps 1, 2, 4 and 5 below are only needed if you'd rather copy the changes into the current live theme instead.

# Must be done before it goes live

1. **Take the Black Friday 3-month plan off the main product. Urgent: it affects the live site now.** The BF 3-month plan (Skio group `bf-subscription-refills-3-month`, selling plan **694836494683**, **£99** first order) is attached to the **main** product's 90-day variants as well as the BF product's. On today's live page it shows as an extra, unpriced "3-MONTH SUBSCRIPTION" card, and anyone who picks it pays the Black Friday price on the main product. In Skio, remove the main product's variants from that plan group. The new templates hide it on the main product (`muto-nad-trust`, "Hidden plans"). The BF template doesn't hide it, because there it's the real plan.
2. **Check the third payment.** The page says "£99 for your first order, £125 on your second, £150 on your third." Skio has £99, then £125 from the second order. Make sure the £150 from the third order is set (e.g. on the Month 7 variant or a second price step).
3. **Orders left.** The bar and the box read the shop metafield **`muto.bf_orders_left`** (now **481**). Nothing counts it down yet:
   - **To count it down:** use a Shopify Flow ("order created with the BF product → decrease `muto.bf_orders_left` by 1"), or have someone update it by hand (Settings → Custom data → Shop → `bf_orders_left`).
   - **At 0:** the box says "All 500 have gone."
4. **The cart** (step 2):
   - set the two gift lists: vial, eBook and Forever Jar added, in display order
   - change `custom.js` so checkout reads NAD+, creatine … Garmin
   - update the cart drawer so the BF saving says "on your first order"

# Before you start

- **Files:** `MUTO_BF_PDP_30Oct2026.zip`, also in GitHub at `handoff/bf-pdp/` (repo drrichiebarclay-rgb/claude, branch `claude/gifted-wozniak-e239h5`).
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451).
- **Preview:** both pages are on the 3M refill plan theme (ID 202682564955):
  - Black Friday (the BF product): <https://muto.co/products/bf-nad-cellular-complex?preview_theme_id=202682564955>
  - After Black Friday: <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955&view=muto-nad-trust>
- **Your edits are kept.** The buy box, its `easy_read` block, the menu, benefits, ingredient library, comparison, timeline, "How to take it", FAQs and the test-results panel are copied from **live `muto-nad-v2` as of 28 October**. If you've edited `muto-nad-v2` since, tell Richie first, and both templates will be rebuilt from your version.
- **The cart drawer change** is in the zip at `snippets/cart-drawer.liquid` (step 2).
- **Images:** the founder photo (`founder-bf-stage.jpg`) and the travel vial photo (`gift-travel-vial.jpg`) are already in Content → Files, so there is nothing to upload.

# Step 1: add the 9 files, in this order

Every file is new; nothing with these names exists on live.

| File | What it is |
|---|---|
| `assets/muto-crea-trust.css` | Styles for the new blocks |
| `sections/muto-crea-statement.liquid` | "The best is still ahead." band |
| `sections/muto-crea-stats.liquid` | "The problem": four stat cards with sources |
| `sections/muto-crea-standards.liquid` | "Checked, not taken on trust." four standards cards |
| `sections/muto-crea-reviews.liquid` | "What our community say." rotating reviews (20) |
| `sections/muto-crea-founder.liquid` | Founder band |
| `templates/product.muto-nad-bf.json` | **The Black Friday page** (the BF product already points at it) |
| `templates/product.muto-bf-redirect.json` | Sends the main URL and -2 to the BF product, keeping `?utm_…` |
| `templates/product.muto-nad-trust.json` | The page without the offer, for main and -2 after Black Friday |

Add the asset and the sections first. A template that uses a section is rejected if the section isn't there yet.

With the Shopify CLI, from the unzipped folder:

    shopify theme push --theme 200736047451 --nodelete \
      --only "assets/muto-crea-trust.css" --only "sections/muto-crea-*.liquid" \
      --only "templates/product.muto-nad-bf.json" --only "templates/product.muto-bf-redirect.json" \
      --only "templates/product.muto-nad-trust.json"

Or in admin: Online Store → Themes → live theme → … → Edit code. Add a new asset, then each new section, then three new product templates (`muto-nad-bf`, `muto-bf-redirect`, `muto-nad-trust`), and paste each file in.

All the other sections the page uses are already on live and unchanged: `muto-pdp-v2-buy`, `muto-section-nav`, `muto-benefit-cards`, `muto-home-board`, `muto-ingredient-library`, `muto-home-results`, `muto-chapter`, `muto-timeline`, `muto-crea-faq`, `custom-reviews`, `muto-test-results`, `custom-liquid`.

# Step 2: the cart


## Travel vial

A free **travel vial** now comes with the first order on the 3-month plan only, shown with **£10 crossed out**, like the other gifts.

- **Product: already created.** "Travel Vial", handle `muto-travel-vial-free`, SKU `TRAVEL-VIAL`, £0 with a £10 compare-at, unlisted, stock not tracked, published to the Online Store. Its photo is on the product, so it shows in the cart.
- **Cart: one setting to change on the live theme.** Online Store → Customize → Theme settings → the cart giveaway settings → the 3-month free products list (`cart_free_product_3m`). Add **Travel Vial** (`muto-travel-vial-free`) to the list, alongside the bottle, socks, creatine and Garmin entry. The theme's giveaway script then adds it to the cart at £0 whenever the 3-month NAD+ subscription is in it. The cart drawer lists it under "Your free welcome gifts" with £10 struck through and "Free". Subscription renewals don't carry cart gifts, so it only ships with the first order.
- **Page: in the template.** The welcome kit shows a "Travel vial" tile (£10 struck through) and an itemised row on the quarterly plan only. The quarterly kit is now worth **£87** (was £77) in the plan's bullet and the bar above the plans.
- **Also say £87** wherever else the quarterly kit is quoted at £77, e.g. the announcement bar's "£77 OF FREE GIFTS WITH EACH ORDER" if that's meant to be the quarterly figure.

## The 3-month gifts on the BF product

Your 30 Oct change to `custom.js` decides the gifts by SKU (`NAD-3M-Month1` / `NAD-1M-Month1`) rather than product ID. The BF product uses the same SKUs, so its orders get the welcome-kit gifts too. Once the vial is in the 3-month list, they get the vial as well, at checkout as well as in the cart, because the gifts are real £0 lines.

## Gift lists: what's added, and in what order

Two theme settings (Online Store → Customize → Theme settings → cart giveaway) decide which free products are added. Set them to exactly this, **in this order**, which is the order they'll show in the cart and at checkout under NAD+:

| Setting | Products, in order |
|---|---|
| 3-month free products (`cart_free_product_3m`) | `muto-performance-creatine`, `muto-socks-free`, `muto-performance-water-bottle`, **`muto-travel-vial-free`**, **`muto-ebook`**, **`muto-forever-jar-free`**, `chance-to-win-garmin-watch` |
| 1-month free products (`cart_free_product`) | `muto-performance-creatine`, `muto-socks-free`, **`muto-ebook`**, **`muto-forever-jar-free`**, `chance-to-win-garmin-watch` |

- **Forever Jar is new:** "Forever Jar", `muto-forever-jar-free`, SKU `FOREVER-JAR`. It's £0 with a £10 compare-at, unlisted, stock not tracked, ships with the order, and has its photo.
- **The 12-Week Protocol eBook** (`muto-ebook`, £0, compare-at £10, no shipping) already exists. It wasn't in the 3-month list.
- **The cart drawer** already draws the eBook and the jar as listed-only extras when they aren't real lines. Once they are real lines it lists those instead, with no duplicates. They then also appear at checkout.
- **Check with the warehouse:** the jar used to come in every kit without a cart line. Now it's a £0 line, so make sure each order still gets one jar, not two.

## Order in the cart and at checkout: NAD+ first, creatine second, Garmin last

Shopify lists the **newest** cart line first, in the cart and at checkout. The gift script adds the gifts after NAD+ is added, so they end up above it. Change `checkManualGiveAway` in `assets/custom.js` (your 30 Oct version) so that when it adds gifts it:
1. re-adds them one at a time, in reverse of the settings order
2. moves Garmin to the end, because `variantIds` puts `cart_giveaway_product` (Garmin) first
3. re-adds the NAD+ line last, so it sits on top

Replace:

```js
        // 3. Add desired giveaways that are missing
        const missing = desiredIds.filter(
            (id) => !items.some((item) => cusManualGiveawayIsMatch(item, id))
        );
        if (missing.length) await cusManualGwpAddToCart(missing);

        await refreshCartUI();
    };
```

with:

```js
        // 3. Add desired giveaways that are missing, then put the cart in display order.
        //    Shopify shows the newest line first (cart and checkout): re-add every gift one at a
        //    time in reverse of the settings order, Garmin last, then re-add NAD+ so it's on top.
        const missing = desiredIds.filter(
            (id) => !items.some((item) => cusManualGiveawayIsMatch(item, id))
        );
        if (missing.length) {
            const garminId = String(window.cartGiveaway?.variantId || '');
            const ordered = desiredIds.filter((id) => id !== garminId)
                .concat(desiredIds.includes(garminId) ? [garminId] : []);
            const present = items.filter((item) => ordered.some((id) => cusManualGiveawayIsMatch(item, id)));
            if (present.length) await cusManualGiveawayRemoveFromCart(present.map((item) => item.key));
            for (const id of ordered.slice().reverse()) await cusManualGwpAddToCart([id]);
            await moveNadToTop();
        }

        await refreshCartUI();
    };

    // Re-add the NAD+ subscription line(s) so they're the newest, i.e. listed first.
    const moveNadToTop = async () => {
        const cart = await getCartJson();
        const nad = (cart.items || []).filter((item) =>
            /^NAD-/.test(getSku(item)) && !(item.properties || {})[CUS_MANUAL_Giveaway_PROP_KEY]);
        for (const item of nad) {
            await fetch('/cart/change.js', { ...fetchConfig(), body: JSON.stringify({ id: item.key, quantity: 0 }) });
            const line = { id: item.variant_id, quantity: item.quantity, properties: item.properties || {} };
            if (item.selling_plan_allocation) line.selling_plan = item.selling_plan_allocation.selling_plan.id;
            await fetch('/cart/add.js', { ...fetchConfig(), body: JSON.stringify({ items: [line] }) });
        }
    };
```

It only reorders when gifts are being added, so changing a quantity doesn't trigger it. The loader overlay already covers the extra requests, about a second. Test on a real cart, because Shopify's line order has changed between API versions:
- add 3-month NAD+
- check the drawer and checkout read NAD+, creatine, socks, bottle, travel vial, eBook, Forever Jar, Garmin
- try the monthly plan too

## The saving line in the cart drawer

The drawer says "You save £111 every 3 months, ongoing" under the BF product. That's wrong, because the BF price is for the first order only. Replace `snippets/cart-drawer.liquid` with the one in the zip (`snippets/cart-drawer.liquid`). It's the live file from 27 Oct with one change: for products whose handle contains `bf-` (or that are tagged `first-order-offer`), it says **"You save £111 on your first order"**. The main product says "You save £60 every 3 months" ("ongoing" removed). If you've edited the drawer since 27 Oct, copy the change across instead. It's the `mc_first_only` block above the "You save" line.

# Step 3: point the main URL and -2 at the Black Friday product

Do this **after** steps 1 and 2 and the "Must be done" list. In Shopify admin, go to Products → product → Theme template.

| URL | Product | Template now | Black Friday | After Black Friday |
|---|---|---|---|---|
| `/products/bf-nad-cellular-complex` | BF NAD+ Cellular Complex | `muto-nad-bf` (already) | `muto-nad-bf` | set to **Draft** |
| `/products/muto-nad-cellular-complex` (main) | NAD+ Cellular Complex | `muto-nad-v2` | **`muto-bf-redirect`** | `muto-nad-trust` |
| `/products/muto-nad-cellular-complex-2` | NAD+ Cellular Complex 2 | `muto-nad-v2` | **`muto-bf-redirect`** | `muto-nad-trust` |

- **How the redirect works:** `muto-bf-redirect` sends visitors straight to `/products/bf-nad-cellular-complex`, keeping the query string, so `utm_`, `gclid` and `fbclid` survive. A Shopify URL redirect can't do this, because those only apply to pages that don't exist.
- **In the theme editor:** the redirect doesn't fire, so the main product can still be edited.
- **Ads and emails:** they can also link to the BF product directly.

Nothing is deleted. `muto-nad-v2` stays in the theme, so any product can be switched back in one click.

# Step 4: the announcement bar

- **On the Black Friday page:** the page hides the blue scrolling announcement bar itself, so the black Black Friday bar is the only one at the top. Nothing to do.
- **On every other page:** the bar still advertises the ended offer, **"EXTRA 10% OFF OUR QUARTERLY PLAN"** and **"ENDS ON 28.10.26"**. Remove those two messages (Customize → Header → announcement bar). If "£77 OF FREE GIFTS WITH EACH ORDER" is the quarterly figure, it's now **£87** with the travel vial.

# Step 5: remove the old pre-sale box from the other live templates

**MUTO10 was ended on 28 October at 17:19.** It no longer works at checkout. The dark "BLACK FRIDAY PRE-SALE" box still says the code "is applied automatically at checkout", and its script still tries to apply MUTO10 on page load. It's on three live templates:

- `product.muto-nad-v2` (main and -2 until step 3 is done)
- `product.muto-nad-performance` (-3)
- `product.muto-nad-45` (no product uses it now)

In each one, open the `easy_read` Custom Liquid block and delete three things:

1. In the `<style>`: from `/* Black Friday pre-sale box, above the plans */` up to (not including) `/* -2 page only:`.
2. In the `<script>`: from `/* Black Friday pre-sale: real countdown` down to the end of that function, the line `if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();` and the `})();` after it.
3. The line `<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"></div>`.

The new `muto-nad-bf` and `muto-nad-trust` templates already have all three removed.

**Quick stopgap** if this can't be done straight away: Online Store → Customize → Theme settings → Custom CSS, add `.mc-bf:has(.mc-bf__clock){display:none !important}`. That hides the box on every page. The script still runs, but MUTO10 is ended, so nothing is applied.

# The Black Friday additions

On top of everything listed in the next section:

- **Sticky bar** (Custom Liquid block `bf_bar`, before the buy box). Black #242223, white text, 44px tall, fixed to the top of the screen. The page, header included, starts 44px lower so nothing sits under it. The theme pulls product-page content up under its see-through header, which is why the bar is fixed rather than in the page.
  - **Desktop:** "● BLACK FRIDAY **53% off your first order** plus a welcome kit worth £87 · **481**/500 left · Claim offer".
  - **Phones:** "● BLACK FRIDAY **53% off your first order** · **481**/500 left".
  - **Tapping it:** scrolls to the offer box.
  - **Orders left:** comes from `muto.bf_orders_left`, rendered in the page (no script), so it's there from the first paint.
- **The blue announcement bar** is hidden on this page only (`[id$="__muto-announce"]{display:none}` in `bf_bar`).
- **"On this page" menu:** pins 44px from the top, under the bar (its `nav_top` setting).
- **Offer box above the plans:**
  - white with a black outline
  - "BLACK FRIDAY OFFER", "53% off your first order", "plus a welcome kit worth £87", "£99 for your first order, £125 on your second, £150 on your third."
  - "481 out of 500 remaining" with a bar
  - drawn in the `early` block straight after the buy box, so it's there before first paint
- **Bar over the plans:** "Black Friday offer · Limited stock", with "Best value" in a turquoise pill.
- **Quarterly card:** "Save 53%", £33/mo (£70 struck), "3 months' supply: £99 for your first box, then £125, then £150", and a lime **£1.10 a day** pill beside the name. The welcome-kit line is first in its list.
- **Monthly card:** "Save 28%", £49.99/mo (£70 struck), "£49.99 for your first month, then £60 every 4 weeks", and a lime **£1.79 a day** pill.
- **Founder photo:** Richie on stage (`founder-bf-stage.jpg`). The main page keeps the original.

# What's on the page

In order, below the buy box. **New** blocks are in bold; the rest is `muto-nad-v2` as it is on live today.

1. "On this page" menu (pins to the top as you scroll, as on live), with four new links: **Problem**, **Standards**, **What people say** (the videos) and **Founder**, 12 links in page order
2. **Statement:** "The best is still ahead." / "Built for your energy, recovery and sleep in your 40s and 50s. Five supplements in one daily jar." / tag "Track it on your wearable for 90 days, or your money back."
3. **The problem:** small mono label "The problem", heading "Your biology shifts. Most supplements don’t." Four cards in the standards style (number, lime topic tag, big figure, cyan rule, one line): Energy **~50%** drop in your muscles’ energy-making capacity between your 40s and late 60s (Conley et al., 2000) · Recovery **~80%** less deep, restorative sleep by midlife than in your early 20s (Van Cauter et al., JAMA 2000) · Longevity **3–8%** of muscle lost every decade after 30 (Volpi et al., 2004) · Trust **57%** of supplements tested didn’t match their label (Crawford et al., 2022). Sources in a small line underneath.
4. **Benefits:** the live five cards, with a new heading: "Benefits built on published science." (small line above: "Five jobs. One daily jar."), and a new line under it: "What you need after 35. Your biology shifts. What you need evolves."
5. **Science board:** "Six scientists put their name to MUTO.", compact row, white background.
6. **Standards:** four cards. Card 1 has the "View third-party testing results" button, which opens the certificate panel (batch 2333).
7. **Customer videos:** "Don't take our word for it.", 8 videos in a row that scrolls: Kate Bright, David Mercado, Lucy Halliday, Harry Insley, Adam Facey, Max Richards, Adam Hamilton, Yolanda King. Ellen Gray's video is removed, and so is the footnote under the row.
8. **Reviews:** "What our community say.", 20 five-star REVIEWS.io reviews that rotate every 6 seconds, with "4.8 from 103 reviews".
9. "Every ingredient has a job." ingredient library
10. **Founder:** Dr Richie Barclay, PhD: cell biologist, Harley Street nutritionist for 13 years, former cricketer and tennis player.
11. Comparison (heading now "See the difference for yourself."), "What you can expect over time." timeline, "How to take it.", FAQs (all 10 from live), REVIEWS.io widget.

Also changed from `muto-nad-v2`:

- **Under the buy button:** the serving line, "Not another multivitamin…" copy and the quote slider are blanked or hidden (not deleted).
- **Buy button** in brand green **#6BCE7F**, charcoal label, with a second line inside it: a shield and "90-day money-back guarantee".
- **Under the subhead:** "In collaboration with seven leading scientists from world-leading research institutions, including four universities in the UK and Australia."
- **Rotating stats** under the button, every 3.5 seconds: "94% reported better recovery", "92% reported improved energy", "88% bounce back quicker", with a black bar that fills left to right to each figure. Set in `STATS` in `make_trust.py`.
- **Delivery line** under the button: "● Ready to ship — arrives by **Thu 29th Oct** | [Royal Mail logo] Tracked 24hr delivery". The date is the next calendar day in UK time, or the day after from the **9pm cut-off**, set by a script that updates while the page is open. Before the script runs it says "arrives tomorrow". The logo is `theme/assets/royal-mail-logo.png`, embedded in the template (nothing to upload).
- **"How it helps" list** in the buy box is hidden on phones as well as desktop.
- **Phones:** the billing line under each plan name is smaller (12px) so it fits, and the delivery line is centred.
- **Phones, whole page:** a smaller, tighter scale below 750px. Headings 28px (the statement 32px), lines under headings 15px, body 14-15px, smaller cards with less padding, benefit cards narrower, problem stats two by two, section spacing 40px. The new bands' sizes are in `muto-crea-trust.css`. The live sections' sizes are in the template's `head_styles` block, so they only change on this page.
- **No sticky add-to-cart bar.** The `sticky` section isn't in this template, so nothing slides in at the top or bottom of the page as you scroll.
- **Backgrounds:** no gradient washes. Almost every band is flat white. Brand sage grey (#C8D2CF) is used only on "What our community say" and the comparison (as on live). "How to take it" and the ingredient library are white too. Set in the `head_styles` block at the top of the template.

## How it's built

- **Template-only** apart from the five new sections and their stylesheet. The page's own styles are in a Custom Liquid block called `head_styles` at the **top** of the template, so the buy box is styled from the first paint (with them at the bottom, the old design flashed on load). Its scripts stay in `easy_read` and `bands` at the bottom. A Custom Liquid block called `early`, straight after the buy box, opens the page on the Quarterly plan and adds the subhead, the testing-results button, the collaboration line, the rotating stats and the delivery line before the first paint, so nothing jumps on load (it used to flip from Monthly to Quarterly once the page had loaded). The same scripts at the bottom stay as a safety net. The `bands` scripts (delivery line, rotating stats, collaboration line, video drag) run again after `shopify:section:load`, so they survive the theme editor re-drawing the buy box.
- **Source:** `shopify/pdp-trust/make_trust.py` builds the template. Change copy there and rebuild rather than editing by hand, or tell Richie about manual edits so they aren't lost on the next rebuild.

# Page speed

**Done in the Black Friday theme's `layout/theme.liquid`.** Every other page behaves as before:

- **On the new product pages** (`muto-nad-bf`, `muto-nad-trust`, `muto-bf-redirect`):
  - `jquery-min.js`, `slick-min.js` and `custom.js` load with `defer`, so they no longer block the first paint. Nothing on those pages uses jQuery inline. I checked every section and snippet, and only other pages' sections do, which is why it's limited to these templates. `defer` keeps their order, and `custom.js` still waits for jQuery's ready.
  - `slick.css` and `slick-theme.css` aren't loaded. Nothing on those pages uses Slick.
  - `muto-crea.css`, `muto-home.css` and the two Neue Haas weights are preloaded in `<head>`.
- **The redirect from main and -2** fires at the very top of `<head>`, before anything else downloads.
- **The OpenAI pixel** has `debug: false`.
- **The Usermaven loader** has moved inside `<head>`. It was before it.

**Already in the page itself:**
- The REVIEWS.io widget loads only when the reader nears it, or once the page is idle.
- Images below the first screen are lazy and sized. Videos load only when tapped.
- The first product photo has high priority.
- Nothing in the buy box moves after first paint.

**Left for you:**
- **App embeds:** REVIEWS.io core and rating snippet, Klaviyo, Elevar, Triple Whale, Clarity, Alia and Pandectes load on every page. Turn off any that aren't used.
- **Measure:** run PageSpeed Insights (mobile) on the BF product before and after publishing.

# Check after publishing

1. **Main URL and -2** land on `/products/bf-nad-cellular-complex`, with any `?utm_…` kept. **On the BF product, on phone and desktop:**
   - the menu row is never under the black bar while scrolling
   - the black bar is at the very top, with the header fully visible under it and no blue bar
   - the page opens on the **Quarterly** plan
   - nothing jumps as it loads
2. **Prices at checkout match the page:**
   - Quarterly: first box £99
   - Monthly: first month £49.99

   **The main product's own plans no longer offer £99.**
3. **Orders left:** the bar and the box both show the metafield value. Change it and both follow.
4. **Cart and checkout, 3-month BF plan:**
   - The lines read NAD+, creatine, socks, bottle, travel vial, eBook, Forever Jar, Garmin, in that order.
   - The saving line says "You save £111 on your first order".
   - The gift list includes Travel Vial, ~~£10~~ Free, and so does the checkout.
   - The monthly plan doesn't get the vial.
5. **Only two plan cards** (Monthly, Quarterly) plus "Buy once". No empty "3-MONTH SUBSCRIPTION" card.
6. **Clicks:**
   - The bar scrolls to the offer box.
   - Each "On this page" link scrolls to its section, with the menu under the bar.
   - "View third-party testing results" opens the certificate panel.
   - The stars scroll to the reviews widget.
7. **Videos** play, and the **reviews** rotate. The REVIEWS.io widget at the bottom loads as you scroll near it.
8. **After Black Friday:** switch main and -2 to `muto-nad-trust`, and set the BF product to Draft. The main URL should show the page with no bar, no offer box and normal prices.
