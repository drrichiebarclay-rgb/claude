# MUTO theme handover: Black Friday, sticky add to cart, menu, cart, buttons

**For:** Mehul
**Source theme:** "Black Friday | Claim offer + sticky bar | 31 Oct" (ID 203974869339, unpublished). Every file here was pulled from that theme on 2 Nov 2026 and checked against Shopify's checksums (`MANIFEST.md5`).
**Target:** the live theme ("Clone Of Live | Buy Box Redesign"), or whichever theme goes live for Black Friday.

This follows your feedback: the CSS is now split by section, so nothing PDP-specific loads from the header on every page, and the sticky add to cart is its own section.

---

## ⚠️ Status at 2 Nov, ~12:30: live needs the header and footer steps now

- **Live** ("Clone Of Live | Buy Box Redesign [31-08]") already has every file in `theme/`. They were uploaded at 11:53–11:54 and match by checksum. But live's **header and footer groups were not updated**, so live runs the slimmed `muto-bf-head` with no **MUTO — Site styles**, **MUTO — Menu** or **MUTO — Sticky add to cart**. Since then, every page except the two BF product templates has been missing the site fonts, header, cart and button styles, the new menu and the sticky bar.
- **Ready-made fix:** theme **"Clone Of Live | BF menu, buttons, sticky, CSS by section [02-11]"**, a fresh duplicate of live with the header and footer groups done. Everything else is live's own, including today's template edits. All files are checked by checksum.
  - Preview: https://muto.co/?preview_theme_id=204099125595
  - Editor: https://admin.shopify.com/store/c0xuhb-9e/themes/204099125595/editor

**Pick one:**

- **A. Publish the clone** after a quick preview: homepage, bottle page, menu, cart, a BF product page. Any edits made on live after ~12:30 would need copying across first.
- **B. Fix live in place** (about a minute in the theme editor):
  1. Header → add **MUTO — Site styles** and drag it to the **top**.
  2. Header → add **MUTO — Menu**. Settings: Menu *Main Menu New Drawer*; Log in link `https://mutolongevity.com/a/account/login`; Shop item 1 `muto-menu-nad-jar.jpg`; Offer card image `muto-menu-offer.jpg`.
  3. Footer → add **MUTO — Sticky add to cart**. Leave Product blank and untick "Emit product structured data".

  Or upload `reference/header-group.json` and `reference/footer-group.json` to live. They are exactly live's current files plus those three sections.


## Update ~12:15: the header section now holds only the top bar's CSS (done in the clone)

Your note: the section beside the announcement bar should only carry the bar's CSS. Done in the clone:

| File | Change |
|---|---|
| `sections/muto-bf-head.liquid` (now "MUTO — BF head top bar") | Only `muto-bf-bar.css`, the bar itself and `muto-bf-claim.js`, on the BF templates. No page CSS. |
| `sections/muto-bf-style.liquid` ("MUTO — BF page styles") | Holds the page CSS that was in the head: compact, layout, type, copy CSS and the inline rules. Then extra.css, the premium design (automatic on the premium template) and the comparison and fold-copy scripts, as the bar snippet loaded them. The old "extras" setting is kept only so the templates stay valid. |
| `templates/product.muto-nad-bf.json`, `templates/product.muto-nad-bf-premium.json` | Live's own templates with one change: a `bf_style` section (Design Standard, extras off) added **first**, before `head_styles`, so the CSS order matches the old header order exactly. |
| `muto-bf-sticky.css` | No longer loaded by the head; "MUTO — Black Friday offer" (footer) already loads it. |
| `snippets/muto-bf-bar.liquid` | Now only the bar's markup. It used to also load `muto-bf-extra.css`, `muto-bf-premium.css` (premium template), the comparison and the fold-copy scripts; those moved into "MUTO — BF page styles" **in the same order** (after the page CSS). The extras always load, and premium is picked automatically on `product.muto-nad-bf-premium`. |

**Net effect on the BF pages: the same CSS files and rules, in the same order relative to the template's own styles. Other pages: none of it.**

**To bring this to live**, either publish the clone, or upload `theme/sections/muto-bf-style.liquid` first, then both `theme/templates/*.json`, then `theme/sections/muto-bf-head.liquid` and `theme/snippets/muto-bf-bar.liquid` **last**. If the snippet or head go first, the BF pages lose this CSS until the templates are in. On phones the image then drops below the title, because `muto-bf-extra.css` puts the image first only when it loads after `muto-bf-layout.css`. The templates are byte-for-byte live's as of 12:03 plus `bf_style`; if anyone has edited them on live since, add the section in the editor instead (first in the template, Design Standard).

---
The rest of this guide (install order, BF template steps, dev notes, tests) still applies. Steps 1–2 below are already done on live and on the clone.

---

## What's in the zip

| Folder | What | Action |
|---|---|---|
| `theme/` | 13 new or changed files | Upload all of them |
| `dependencies/` | 14 existing files the new ones load (BF CSS/JS, cart CSS, 2 snippets) | Upload only where the target theme's copy is missing or different (compare with `MANIFEST.md5`) |
| `reference/` | `header-group.json`, `footer-group.json` as set up on the BF theme | **Don't upload.** Make the same changes in the theme editor (step 3) so the live header and footer settings are kept |
| `files/` | `muto-menu-offer.jpg`, `muto-menu-nad-jar.jpg` | Already in the store's Files, so nothing to do. Here as a backup only |

### `theme/` files

| File | New / changed | Purpose |
|---|---|---|
| `sections/muto-site-styles.liquid` | New | "MUTO — Site styles". **Site-wide only**: fonts (Neue Haas, Sometype Mono), heading weights, plain header, shorter mobile header, cart CSS (`muto-cart.css` + `muto-cart-empty.css`), site buttons, range-page and science-page CSS (by template suffix), structured data. First in the header group. |
| `sections/muto-menu.liquid` | New | "MUTO — Menu". The menu panel (see below). Header group. |
| `sections/muto-bf-style.liquid` | New | "MUTO — BF page styles". BF buy box and section CSS, the comparison swap, fold copy. **Only on the BF templates**, directly above "MUTO PDP v2 — Buy". Setting: Design = Standard (turquoise) / Premium (loads `muto-bf-premium.css`). |
| `sections/muto-bf-topbar.liquid` | Changed | "MUTO — BF top bar". The black "Claim →" bar as a section with a product picker. Claim adds the plan and opens the side cart. Removes itself if another top bar is on the page. |
| `sections/muto-sbar.liquid` | Changed | "MUTO — Sticky add to cart". Works on any template and in the **footer group** (`enabled_on.groups: ["footer"]`). In the footer it's the site-wide bar: it steps aside for a page's own sticky bar and skips cart, password, gift card and giveaway pages. Hidden on BF templates (they have the BF offer bar). |
| `sections/muto-bf-offer.liquid` | Changed | Footer BF plan bar. Now loads its own `muto-bf-sticky.css` (it used to come from the head). |
| `sections/muto-bf-head.liquid` | Changed (slimmed) | **Being retired.** Only the old BF block is left (suffix-gated) so the BF templates look right until they have the new sections. Delete it from the header after step 4. |
| `snippets/muto-sbar-bar.liquid` | New | The sticky bar markup and JS for one product (plans or variants), shared by the section. Hides the picker when there's only one option (bottle, socks). Add to cart opens the side cart (Dawn `cart-drawer.renderContents`). |
| `snippets/muto-sbar-style.liquid` | New | Sticky bar sizes to match the PDP bar; black button. |
| `snippets/muto-sci-sticky.liquid` | Changed | The NAD⁺ bar for non-product pages. No fixed id any more (`.mc-sbar--site`); steps aside for other bars; side cart. |
| `snippets/muto-bf-bar.liquid` | Changed | BF top bar on the BF templates: screen reader text ("opens the cart"). |
| `assets/muto-bf-claim.js` | Changed | BF page Claim → adds the plan and opens the side cart (falls back to `/cart`). |
| `assets/muto-cart-empty.css` | New | The empty side cart in the same style as the full cart. |

---

## Install, in this order

1. **Dependencies.** For each file in `dependencies/`, if the target theme doesn't have it or its copy differs, upload this one. All are already used by the BF PDP.
2. **Theme files.** Upload `theme/snippets/*` and `theme/assets/*`, then `theme/sections/*`. Leave `muto-bf-head.liquid` to last, and upload it in the same go as step 3.
3. **Header and footer groups** (theme editor):
   - **Header:** add **MUTO — Site styles** and drag it to the **top**. Add **MUTO — Menu** under it. Settings:
     - Menu: *Main Menu New Drawer*
     - Log in link: `https://mutolongevity.com/a/account/login`
     - Shop photos → Shop item 1: `muto-menu-nad-jar.jpg`
     - Offer card → Image: `muto-menu-offer.jpg`. The text defaults are the BF offer; switch the card off after Black Friday.
   - **Footer:** add **MUTO — Sticky add to cart**. Leave Product blank and untick "Emit product structured data".
   - The section `id`s used on the BF theme (`site_styles`, `muto_menu`, `sticky_atc`) are in `reference/` if you'd rather edit the JSON. Don't give a section in a template the id `bf_bar`: `muto-bf-bar.css` hides `[id$="__bf_bar"]`.
4. **BF templates** (`product.muto-nad-bf` and `product.muto-nad-bf-premium`; the NAD⁺ product uses the **premium** one):
   - add **MUTO — BF page styles** directly **above** "MUTO PDP v2 — Buy". Design: *Premium* on the premium template, *Standard* on the other.
   - add **MUTO — BF top bar** (Product blank = the page's product; plan "3-month"; After Claim = side cart).
5. **Check the BF pages, then delete "MUTO — Black Friday head" from the header.**

Steps 2–3 should go in together. Until the slimmed head and the footer sticky section are both in, a page can briefly show two sticky bars or none.

---

## How the pieces work (dev notes)

**CSS by section**
- Site-wide → `muto-site-styles`.
- BF PDP → `muto-bf-style` (template section).
- Top bar → `muto-bf-topbar` (template section, loads `muto-bf-bar.css`).
- BF plan bar → `muto-bf-offer` (footer, suffix-gated, loads `muto-bf-sticky.css`, `muto-bf-layout.js`, `muto-bf-sticky.js`).
- Site sticky → `muto-sbar` (footer).
- Menu → `muto-menu` (header).
- `muto-bf-layout.js` is loaded once, by `muto-bf-offer`; `muto-bf-style` deliberately doesn't load it.

**MUTO — Menu**
- Renders a `<template id="mmd-tpl">`. On load the script builds `.mmd-root` (overlay + `.mmd-panel` dialog) and appends it to `<body>`, the same pattern as the cart drawer.
- A capture-phase click listener on `#Details-menu-drawer-container > summary` opens this panel instead of Dawn's drawer (`preventDefault` + `stopImmediatePropagation`). Dawn's `#menu-drawer` is hidden with `body:has(.mmd-root) #menu-drawer{display:none}`.
- It closes on the ✕, overlay click, Esc or any link. It locks scroll (`html.mmd-lock`), uses `inert`, keeps `aria-expanded` in sync, and returns focus.
- Content comes from the menu:
  - the first top-level link containing "shop" with children → product rows (photo, or the Shop photos override by position);
  - other top-level links with children → labelled groups;
  - links without children → the "Explore" group.
- It re-builds on `shopify:section:load`.
- Fonts are forced with `.mmd-root :where(*){font-family:var(--mc-font)!important}`.
- Removing the section restores Dawn's drawer untouched.

**Sticky add to cart**
- Each bar has its own id (`mc-sbar-<section.id>`) and its own script.
- `auto = section.location != 'template'`. In the footer the bar steps aside on `DOMContentLoaded`/scroll if the page has another bar: `#MainContent [id$="__sticky"], [data-mh-sticky], .mlp-bar, .mc-sbar`.
- Options:
  - Skio products: one option per selling plan (first available variant with that plan, at the plan's price, "Save X%" from `compare_at_price`).
  - Plain products: one option per variant.
- On the NAD⁺ product page the footer bar adds the line "Black Friday · 3 months for £99" unless a line is set.

**Side cart**
- All add/claim buttons do this:
  1. `cart/add.js`;
  2. `?sections=cart-drawer,cart-icon-bubble`;
  3. `document.querySelector('cart-drawer').renderContents(...)`.
- With no drawer they fall back to `/cart`. Checkout is optional on the two sections.

**Buttons** (in `muto-site-styles`)
- Main buttons `.msc__btn, .mrg__btn, .mil__cat-btn, .mtr .mtr__cta, .mtop__btn`: styled as the premium PDP Add to cart. Black `#242223`, white, Neue Haas 500, uppercase, `.04em`, 4px radius, 60px (56px under 750px), hover `#000`.
- `.mtop__btn` (home hero, on a photo) is white.
- Outline `.msc__tbtn, .mtr-btn` get 4px and uppercase, except inside `.mc` (the PDP buy box).

**Empty cart**
- `muto-cart-empty.css` targets Dawn's `cart-drawer .drawer__inner-empty` markup: heading top-left with a hairline, a black uppercase full-width button, and a mono "Have an account?" label.

---

## Test checklist (BF theme preview, then live)

- [ ] Header menu icon opens the menu from the right, full height. ✕, tapping the dim and Esc all close it. Links work. The page doesn't scroll behind it.
- [ ] Menu: NAD⁺ shows the jar photo; photos are sharp; the offer card shows the photo with text above; Log in goes to `/a/account/login`.
- [ ] Bottle and socks pages: the sticky bar shows the product name once (no picker).
- [ ] NAD⁺ (BF premium) PDP: one top bar and one sticky plan bar. Claim and Add to cart open the **side cart** with the 3-month plan.
- [ ] Home, a page and a collection: one sticky bar. Add to cart opens the side cart.
- [ ] Cart, password and giveaway pages: no sticky bar.
- [ ] Empty side cart: heading top-left, black "Continue shopping".
- [ ] Home, science, about, ingredients, standards, FAQs: buttons black, uppercase, 4px. The home hero button is white.
- [ ] Turning off "MUTO — BF page styles" on a BF template changes only that template.

## Rollback

- Every change is a new section or a file swap.
- To undo the menu, remove "MUTO — Menu" (Dawn's drawer comes back).
- To undo the sticky bar, remove "MUTO — Sticky add to cart" from the footer.
- To undo the site styles, restore the previous `muto-bf-head.liquid` and remove "MUTO — Site styles". The previous version is in the repo history: `shopify/bf-sticky-fix/sections/muto-bf-head.liquid` at commit `8114a02`.

Source and full history: `drrichiebarclay-rgb/claude`, branch `claude/gifted-einstein-f7h2e5`, folder `shopify/bf-sticky-fix/`.
