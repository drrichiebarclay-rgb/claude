---
title: "MUTO Black Friday: product pages and the over-35 landing page"
subtitle: "10 November 2026 · replaces the 9 November handover"
---

Everything below is already built in one unpublished duplicate of the live theme. **Check it, publish it, then do three admin steps.** Nothing on the live site changes until you publish in Step 2.

This replaces the 9 November handover. It includes everything in that one, plus the changes made on 9–10 November.

| Page | Address | Template after this handover |
|---|---|---|
| Main | `/products/muto-nad-cellular-complex` | `product.muto-nad-bf-premium` (no change) |
| url-2 | `/products/muto-nad-cellular-complex-2` | **`product.muto-nad-bf-premium-2`** (new; switch in Step 3) |
| url-3 | `/products/muto-nad-cellular-complex-3` | `product.muto-nad-bf-v3` (no change) |
| Over-35 landing page | `/products/muto-nad-cellular-complex?view=muto-nad-bf-lp-over-35` | **`product.muto-nad-bf-lp-over-35`** (new) |

# Before you start

- **Theme:** **Clone Of Live | BF top bar fix [09-11]** (ID 204572492123). Unpublished. A duplicate of live made on 9 Nov, about 12:00 UK.
- **Previews:**
  - Main: <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=204572492123>
  - url-2 on its new template: <https://muto.co/products/muto-nad-cellular-complex-2?view=muto-nad-bf-premium-2&preview_theme_id=204572492123>
  - url-3: <https://muto.co/products/muto-nad-cellular-complex-3?preview_theme_id=204572492123>
  - Landing page: <https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-bf-lp-over-35&preview_theme_id=204572492123>
- **Files:** GitHub, repo `drrichiebarclay-rgb/claude`, branch `claude/exciting-allen-d0oqpz`.
  - Product-page files: `shopify/bf-topbar-fix/`.
  - Landing page files and the two shared scripts: `shopify/lp-over-35/`.
  - The duplicate theme holds the same files.
- **Not yet tested on the real store.** Everything was built without access to muto.co and checked on mock pages only. Do the checks at the end on the previews before publishing.

# Step 1: check live hasn't changed since 9 Nov

If anyone has edited the live theme since about 12:00 UK on 9 Nov, those edits are not in the duplicate. Either copy them across or tell us before publishing.

# Step 2: test the previews, then publish

Run the checklist at the end. Then: Online Store → Themes → **Clone Of Live | BF top bar fix [09-11]** → Publish.

# Step 3: move url-2 onto its new template and retire the old design

`templates/product.muto-nad-bf-premium-2.json` is a copy of main's template. Its style section (`bf_style`, "MUTO — BF page styles") has Design set to **Premium**. That setting is needed because premium switches on automatically only for the exact name `muto-nad-bf-premium`.

1. Products → **NAD+ Cellular Complex** with handle `muto-nad-cellular-complex-2`. Several products share this title, so check the handle.
2. Theme template: change `muto-nad-bf` to **`muto-nad-bf-premium-2`**. Save. This changes the live page immediately.
3. Open url-2 next to main. They should look the same.
4. Products: filter by theme template `muto-nad-bf` and confirm nothing is left on it.
5. Edit code: keep a copy of `templates/product.muto-nad-bf.json` (it's in GitHub), then delete it.
   - **Order matters.** Don't delete it before step 2. A product whose template is deleted falls back to the default product page.

From now on, main and url-2 are separate files. Edit both if both should change.

Expected side effect: `layout/theme.liquid` defers jQuery, Slick and custom.js only on the `muto-nad-bf`, `muto-nad-trust` and `muto-bf-redirect` templates. On its new template, url-2 loads them the normal way, exactly as main does today.

# Step 4: the landing page's link

The landing page runs on the main product with a template switch, so no product needs assigning.

Once the theme is published, its live link is:

**<https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-bf-lp-over-35>**

Use that link for ads. Orders and reviews count against the main product.

# Step 5: delete leftover files

In Edit code, delete these. Nothing uses them; Shopify blocks deleting files through the API, so it has to be done here.

- `templates/product.lp-over-35.json`
  - An earlier draft of the landing page.
  - It now shows a "this template is retired" notice in the editor, and on the storefront it redirects to the right template.
- `sections/muto-lst-offer.liquid`: the earlier draft's offer section.
- `templates/product.muto-nad-bf-lsttesta.json` and `templates/product.muto-nad-bf-lsttestb.json`: test templates.
- Optional: `assets/muto-bf-claim.js`. It has been unused since the top bar's Claim script moved inline.

# What changed on the product pages

All of this is on the Black Friday templates only: main, url-2's new template and url-3. The header section `muto-bf-head` only renders on templates whose name contains `muto-nad-bf`.

## 1. Top bar: "Claim →" works from the first tap, new wording

**The fix (from 9 Nov).** It was tapped 205 times on url-3 and 33 on main with no response, because:

- it was a link to `#MainContent` until a deferred script loaded;
- each tap then waited on three requests in a row;
- the premium design hides the spinner.

Now:

- **Real link.** The bar is a real link: `/cart/add?id=<90-day variant>&quantity=1&selling_plan=<3-month plan>`.
  - The variant is the first available one with a selling plan whose name contains "3-month". On all three products that is SKU `NAD-3M-Month1`.
- **Inline script.** The Claim script is inline, straight after the bar.
- **One request per tap.** The cart is checked in the background as the page loads, and the add (`/cart/add.js` with `sections`) returns the side cart in the same response.
- **Instant feedback.** On tap the bar changes at once to "Adding your Black Friday offer…".
- **Fallback.** If nothing has happened after 6 seconds, it falls back to the plain link.

**New wording (10 Nov)**, to match the plan cards:

| Screen | Wording |
|---|---|
| Desktop | Black Friday: £33/mo (save 53%) · £1.10 a day + free welcome kit worth £87 · While stock lasts · Claim → |
| Phone | £33/mo · Save 53% + free kit · Claim → |

Files: `snippets/muto-bf-bar.liquid`, `assets/muto-bf-bar.css`, `sections/muto-bf-head.liquid` (no longer loads `muto-bf-claim.js`).

## 2. Side cart shows the item and the full welcome kit

The Claim opens the cart exactly as the theme's own Add to cart does:

- it removes `is-empty` from `<cart-drawer>` and `<cart-drawer-items>`;
- it publishes `PUB_SUB_EVENTS.cartUpdate`, so `custom.js` (`checkManualGiveAway`) adds the free gifts.

The 3-month kit:

- From theme setting `cart_free_product_3m`: creatine, socks, bottle, travel vial and the Garmin entry.
- From `snippets/cart-drawer.liquid` itself: the guide and the Forever Jar.

`PUB_SUB_EVENTS` and `publish` are top-level declarations, so the code checks them with `typeof`, not `window.`.

## 3. Plan cards: AG1-style pricing (new, 10 Nov)

Each plan card in the buy box now reads like AG1's:

| | 3-Month Supply | 1-Month Supply |
|---|---|---|
| Band | ✦ BLACK FRIDAY OFFER | none |
| Pill (right) | SAVE 53% | SAVE 28% |
| Price | **£33**/mo ~~£70~~ | **£49.99**/mo ~~£70~~ |
| Price a day (outlined pill) | £1.10 a day | £1.79 a day |
| Supply | 90-day supply, delivered every 3 months | 30-day supply, delivered every month |
| First order | £99 on your first order | £49.99 on your first order |
| Then | then £125 for your next 3 months, then £150 every 3 months | then £60 every month |

When the welcome kit hangs off the selected card, the card's bottom joins the kit's panel.

**How it's built:**

- **Where it lives:** new snippet `snippets/muto-bf-ag1-plans.liquid`, rendered by a new custom-liquid section, **"AG1-style plan pricing"** (`ag1_plans`). That section sits straight after the buy box on main, url-2's new template and url-3.
- **What the snippet does:** it rebuilds the copy inside each plan card. Radios, selection, the Add to cart button and its price, the welcome kit and the sticky bar are all still the buy box's own.
- **Figures are typed in the snippet** (`PLANS`), not read from Skio. If prices change in Skio, change them there too.
- **To undo on a page:** delete the "AG1-style plan pricing" section from that template, and the previous cards come back.

**Wording in the buy box itself:** the 1-month plan now says "every month" throughout.

- Plan note: "£49.99 for your first month, then £60 every month".
- Delivery dropdown on main and url-2: "Your next delivery arrives every 3 months on the 3-Month Supply, or every month on the 1-Month Supply, with gifts on your orders."
- url-3's delivery dropdown says the same in its own wording.

## 4. Buy box details (from 9 Nov)

- **Socks label:** "Performance socks (UK 6–11)" → **"Performance socks (one size fits all)"**.
- **Welcome-kit pop-ups.** Each welcome-kit image tile, itemised row and later-delivery tile opens a box. It shows the photo, the name, the value (struck through) with "Free", and the image's alt text as the description.
  - It closes with ×, a tap outside or Esc.
  - It doesn't change the selected plan.
  - Built in `snippets/muto-bf-kit-box.liquid`, rendered by `muto-bf-head`.

## 5. Sean Carroll's video (new, 10 Nov)

Sean's video (`1. Sean HERO Video.mp4`, in Files) is the first card in the "In their words." carousel on main, url-2's new template, url-3 and the landing page.

## 6. Shared scripts now handle more than one buy box

Both files are also used by the product pages. With one buy box they behave as before.

- **`assets/muto-bf-layout.js`.** The gallery arrows and the "View third-party testing results" button are now set up in every buy box on the page, not just the first.
- **`assets/muto-bf-sticky.js`** (the sticky add-to-cart bar):
  - It takes its plan options from the first buy box only.
  - It shows only while no buy button is on screen.
  - On a page with no buy box (the landing page), it offers the 3-month plan at £99 and its button runs the top bar's Claim.

# The over-35 landing page (new)

**"7 reasons why thousands of over 35s are switching to NAD+ Cellular Complex"**, in the product page's branding. It uses the Black Friday templates' top bar, sticky bar and styles, because its template name contains `muto-nad-bf`.

**Order:**

1. **Hero:** photo, headline, stars.
2. **Trust:** Men's Fitness and Women's Fitness logos, plus the "Formulated with leading doctors and scientists" strip.
3. **Reasons 1–4**
   1. What you needed at 20 isn't what you need now
   2. Most supplements don't tell you what's in them
   3. Created by a scientist. Reviewed by our scientific board.
   4. Energy for today. Recovery for tomorrow.
4. **Offer card**
5. **Reasons 5–7**
   5. Healthy ageing, from one daily foundation
   6. Alongside your free creatine, one simple daily routine
   7. Not for you? Every subscription payment back
6. **Timeline:** "What people tell us they notice."
7. **"In their words."**, with "Read all reviews" jumping to this page's reviews.
8. **"Reviewed by our scientific board."**
9. **Offer card** (a second copy).
10. **Customer reviews.**

Hidden sections: url-3's test results panel, plus url-3's style and script blocks.

**On the page:**

- **No site navigation.** The theme header is hidden on this page only. The Black Friday top bar stays.
- **The offer cards** (section "MUTO listicle — kit", used twice) are AG1-style:
  - Black Friday band.
  - 3-Month Supply with Save 53%, £33/mo ~~£70~~ and £1.10 a day.
  - £99 on your first order, then £125, then £150 every 3 months.
  - Product image.
  - Ticks: free welcome kit worth £87, 90-day money-back guarantee, free next-day UK delivery.
  - Each free gift as a dropdown, with photo, ~~value~~ Free and a line about it.
  - **Claim the offer**, which runs the top bar's Claim (adds the 3-month plan, opens the side cart, gifts added). Before scripts load it's a plain `/cart/add` link.
- **There's no full buy box on this page**, so every button adds the 3-month plan.
- **Benefit claims** sit in small print under the reason that names the benefit, as the messaging framework requires.

**Files:**

| File | What it is |
|---|---|
| `templates/product.muto-nad-bf-lp-over-35.json` | The page |
| `sections/muto-lst-article.liquid` | Hero and numbered reasons. Each reason has an image focus setting. |
| `sections/muto-lst-trust.liquid` | Logos and the board strip |
| `sections/muto-lst-kit.liquid` | Offer card with gift dropdowns |
| `assets/muto-lst.css` | The page's styles. Also hides the site header and restyles the reviews widget's buttons on this page. |
| Files: `lp-over-35-hero.jpg`, `lp-over-35-reason-1.jpg`, `lp-over-35-reason-3-panel.jpg`, `lp-over-35-reason-4.jpg`, `lp-over-35-reason-5.jpg` | Photos (copies in GitHub, `shopify/lp-over-35/images/`) |

# All theme files

| File | Change |
|---|---|
| `snippets/muto-bf-bar.liquid` | Top bar: real link, inline Claim, side cart and gifts, new wording |
| `snippets/muto-bf-kit-box.liquid` | New: welcome-kit pop-ups |
| `snippets/muto-bf-ag1-plans.liquid` | **New:** AG1-style plan cards |
| `sections/muto-bf-head.liquid` | Renders the kit box; no longer loads `muto-bf-claim.js` |
| `assets/muto-bf-bar.css` | Tapped state |
| `assets/muto-bf-layout.js` | Every buy box gets arrows and the testing button |
| `assets/muto-bf-sticky.js` | Two buy boxes; offer mode on the landing page |
| `templates/product.muto-nad-bf-premium.json` | Socks label, AG1 plan section, Sean video, "every month" wording |
| `templates/product.muto-nad-bf-premium-2.json` | **New:** url-2's copy of main's, with the same changes, Design set to Premium |
| `templates/product.muto-nad-bf-v3.json` | Socks label, AG1 plan section, Sean video, "every month" wording |
| `templates/product.muto-nad-bf.json` | Socks label; retired and deleted in Step 3 |
| `templates/product.muto-nad-bf-lp-over-35.json` + `sections/muto-lst-*.liquid` + `assets/muto-lst.css` | **New:** landing page |
| `templates/product.lp-over-35.json` | Retired signpost; delete in Step 5 |

# Decisions needed before publishing

- **Crossed-out prices.** £210 (3 months), and £70 a month on both plans, need to be genuine previous prices under UK pricing rules (DMCC Act, CMA guidance). The messaging framework also bans "was" prices and strikethroughs in our own copy. Get sign-off, or remove the crossed-out prices.
- **53% or 52%.** £99 against £210 is 52.9%. Everything new says 53%. Confirm, or change the snippet, the landing page and the top bar to 52%.
- **Auto-renewal wording.** The plan cards no longer carry a "renews automatically until you cancel" line (removed on request). Confirm that wording is clear before purchase elsewhere, e.g. at checkout.
- **1-month billing.** Pages now say "every month". Confirm Skio bills monthly, not every 4 weeks.
- **"Thousands of over 35s"** in the landing page headline needs evidence (more than 2,000 NAD+ buyers). The store doesn't record customers' ages.
- **Hero photo.** The jar label reads "CELLLULAR" (three Ls). Retouch or replace before ads.
- **Sean's surname** is spelt "Carroll". Confirm.

# Checks before and after publishing

On a phone and on desktop, with an **empty cart** each time.

**Main, url-2 (via the `?view=` preview link) and url-3:**

- [ ] Tap the top bar's "Claim →" as soon as the page appears. It changes to "Adding your Black Friday offer…" at once.
- [ ] The side cart opens with NAD+ Cellular Complex on the 3-month plan at £99.
- [ ] After the theme's spinner, the side cart lists the full welcome kit: creatine, socks, bottle, travel vial, Garmin entry, guide and Forever Jar.
- [ ] Tap "Claim →" again. No second NAD+ line; the cart just opens.
- [ ] With JavaScript off, the bar lands on the cart page with the 3-month plan. Confirm Skio picks up the plan.
- [ ] Plan cards look as in section 3. Switch plans: the radio, the kit and the Add to cart price follow, and the kit joins the selected card.
- [ ] Add to cart from the buy box on each plan.
- [ ] Socks row reads "Performance socks (one size fits all)".
- [ ] Each kit tile or row opens its pop-up, and the plan doesn't change.
- [ ] "View third-party testing results" opens the results panel.
- [ ] Sean's video plays first in "In their words."
- [ ] The sticky bar appears once the buy button scrolls away, and adds the selected plan.
- [ ] url-2 on its new template looks the same as main.

**Landing page:**

- [ ] The site header is hidden and the top bar shows.
- [ ] Both offer cards: each gift opens, and **Claim the offer** opens the side cart with the 3-month plan and the gifts.
- [ ] The sticky bar appears between and after the offer cards, and does the same as Claim the offer.
- [ ] "Read all reviews" scrolls to the reviews at the bottom, and the reviews load.
- [ ] The images in reasons 1, 3, 4, 5 and 6 crop well on a phone.

**After publishing:**

- [ ] Step 3 done; no product left on `muto-nad-bf`.
- [ ] Place one test order from the top bar. The gifts and the £99 price carry through.
