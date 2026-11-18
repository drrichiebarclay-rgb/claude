---
title: "MUTO landing pages: energy after 35 (two versions)"
subtitle: "18 November 2026"
---

Two new advertorial landing pages for paid traffic. **Both pages already exist in Shopify**: published, hidden from search, each assigned its template. What's left is **copying 3 new files onto the live theme**. Nothing existing is edited.

# Before you start

- **Files:** `MUTO_Energy_After_35_Pages.zip`, also in GitHub at `shopify/lp-energy-35/theme/` (repo drrichiebarclay-rgb/claude, branch `claude/determined-mccarthy-8b759h`).
- **Copy to:** the live theme, Clone Of Live | sticky bar [12-11] (ID 204801016155).
- **Preview first:** the 3 files are already on the unpublished theme Clone Of Live | load flash fix [12-11] (ID 204807176539). Add `?preview_theme_id=204807176539` to either address below.
- **Until the files are on live, the public addresses show an empty page.** The pages point at templates the live theme doesn't have yet, so Shopify falls back to the default page template. Don't run ads to them before step 1.

# The two pages

| | Version A: the science | Version B: the feeling |
|---|---|---|
| Address | `/pages/running-on-empty-after-35` | `/pages/not-lazy-running-on-empty` |
| Template | `page.lp-energy-35` | `page.lp-energy-35-feel` |
| Headline | "You're doing everything right. So why are you still running on empty after 35?" | "You're not lazy, you're running on empty, and it isn't your fault." |
| Middle of the page | Bar chart, seven nutrient cards with research notes and sources | Five "sound familiar?" cards, three customer reviews, what's inside in plain English, the guarantee |
| Both end with | "Today's special offer" with a countdown, a trust section, the reviews widget | Same |

Preview links:

- A: <https://muto.co/pages/running-on-empty-after-35?preview_theme_id=204807176539>
- B: <https://muto.co/pages/not-lazy-running-on-empty?preview_theme_id=204807176539>

# Step 1: copy the 3 files, in this order

| File | What it is |
|---|---|
| `sections/muto-lst-needs.liquid` | New section, "MUTO listicle essentials". The whole article, the offer and the trust section are blocks in this one section. |
| `templates/page.lp-energy-35.json` | Version A |
| `templates/page.lp-energy-35-feel.json` | Version B |

Copy the section first. A template that names a section, or a setting, the theme doesn't have yet is rejected.

**Shopify CLI** (from the `theme` folder):

    shopify theme push --theme 204801016155 --nodelete \
      --only "sections/muto-lst-needs.liquid" --only "templates/page.lp-energy-35.json" \
      --only "templates/page.lp-energy-35-feel.json"

**Or Shopify admin:** Online Store → Themes → live theme → … → Edit code. Add the section, then the two page templates (Add a new template → page → `lp-energy-35`, then `lp-energy-35-feel`), paste and save.

There is no step 2. The pages are already created and assigned.

# What the pages rely on, already on the live theme

Nothing here needs copying, but the pages break if any of it is removed or renamed.

| Depends on | Used for |
|---|---|
| `assets/muto-lst.css` | Base styles and fonts. It also hides the store header on any page that loads it. |
| `sections/custom-reviews.liquid` | The REVIEWS.io widget. Its settings are copied from `page.lp-stack`. |
| `sections/muto-test-results.liquid` | The panel that "View third-party test results" opens. Its settings and blocks are copied from `product.muto-nad-bf-premium`. |
| `snippets/muto-bf-bar.liquid`, rendered by `sections/muto-bf-head.liquid` in the header group | **The Claim button.** See below. |
| Product `muto-nad-cellular-complex` with a 3-month selling plan | The plan the Claim button adds. |
| Shopify Files | Every image is referenced by its CDN URL. Nothing to upload. |

# How the Claim button works

The pages have no buy box. "Claim today's offer" adds the 3-Month Supply and opens the side cart.

- It hands the tap to the Black Friday bar's own script: `#mc-bfx`, which the header group renders on every page. That script adds the plan with one request, opens the cart drawer and fires the theme's cart-update event, which is what adds the free welcome gifts.
- **The bar is hidden on these pages, not removed.** The section's "Hide the Black Friday bars" setting hides `#mc-bfx` and `#mc-sbar` with CSS and resets the 44px body padding the bar adds.
- A page template has no product in scope, so the section has a **Product for the offer button** setting, set to `muto-nad-cellular-complex`. The button's `href` is a plain `/cart/add?id=…&selling_plan=…` link built from that product's 3-month plan.
- **When the Black Friday bar is taken out of the header:** the button falls back to that plain link. It still adds the plan, but it goes to the cart page instead of opening the drawer. Check the welcome gifts are still added on that route, or tell me and I'll give the button its own add-to-cart script.

# The offer is typed, not live

Price, crossed-out price, billing lines and the list of free gifts are text settings on the Offer block, copied from the over-35 listicle's offer card on 18 November: £33/mo, was £70, Save 53%, £99 today then £125 then £150, £72 of free gifts. **When the offer changes, both templates need editing by hand** (theme editor → the page template → MUTO listicle essentials → Offer).

# The countdown

Set on the Offer block.

- **Offer end date blank (as shipped):** counts down to midnight tonight on the visitor's own clock, and starts again the next day.
- **Offer end date set (`YYYY-MM-DD`):** counts down to midnight at the end of that day, shows a days box when more than a day is left, and hides itself afterwards.
- **Show a countdown unticked:** no timer.

See "Before ads go live": as shipped, this needs a decision from Richie.

# Trust section

Under the offer: six icon tiles, the scientific board strip and two buttons.

- **View nutrition table** opens the nutrition label image (`muto-nad-nutrition-label-desktop.png`, or `-phone.png` under 750px) in an overlay. It is a plain fixed `div` moved to `<body>` on first open, not a `<dialog>`.
- **View third-party test results** is a link to `#test-results`, which `muto-test-results` listens for. The section also opens the panel itself if it hasn't opened 250ms after the tap.
- **Known report:** Richie said the nutrition label "didn't open on click" once, on the earlier `<dialog>` version. I couldn't reproduce it and have no Safari to test with; the overlay above is the rewrite. **Please test both buttons in Safari on a Mac and on an iPhone.**

# Editing in the theme editor

Everything is blocks in one section, so order and copy can be changed without code.

- **Layout:** "Direct layout" is ticked on both pages. Wrap a phrase in `<em>…</em>` in any heading to turn it green.
- **Blocks:** Essential (the numbered cards), Text, Image, Bar chart, Timeline, Button, Quote, Panel (the grey "why it happens" block; tick "Black background" for the dark version), Answer (the checklist), Offer, Trust.
- **Essentials number themselves** in block order.
- **Line formats** are in each setting's help text, for example research findings are one per line with `| 1` to cite source 1.
- **Image focus** on an Image block controls the crop: `50% 0%` keeps the top, `50% 100%` the bottom.

The source of truth is two scripts in `shopify/lp-energy-35`: `build.py` (version A) and `build_feel.py` (version B). If you edit a page in the editor, tell me, and I'll pull the change into the scripts so it isn't lost on the next rebuild.

# Things to know

- **Section name limit.** Shopify rejects a section whose schema name is over 25 characters. This one is "MUTO listicle essentials" (24).
- **No store header on these pages.** That comes from `muto-lst.css`, as on the over-35 listicle. The footer stays.
- **Body class** is `template-page template-lp-energy-35` (or `-feel`) plus the page handle, if you need a hook.
- **SEO.** Both pages have `seo.hidden` set and their own title and description. They output `noindex,nofollow`.
- **Old files on the preview theme.** `templates/product.muto-nad-bf-lp-energy-35.json` and `…-feel.json` are earlier product-template versions of the same pages. They are only on theme 204807176539, nothing links to them, and they can be deleted. Don't copy them to live.
- **The GitHub repo is public.** The files were put on the preview theme by URL from it.

# Before ads go live (for Richie)

- [ ] **The countdown must be true.** As shipped it resets every night. If the bundle is the same price the next day, that is a false time limit, which UK consumer law (the DMCC Act 2024) and the ASA treat as a banned practice. Give the offer's real last day, or untick the countdown. The same goes for the wording "Today's special offer" and "Offer ends at midnight".
- [ ] **Claims read-through** by your regulatory adviser. On version A: the NAD+, CoQ10 and PQQ cards and the "why it happens" panel cite studies for ingredients with no authorised claim. On version B: the five "sound familiar?" cards, and "everyday wear and tear inside your cells" as the plain-English gloss on oxidative stress.
- [ ] **It's in your voice.** Approve or reword the first-person lines on version A ("People often tell me…", "That is the reason I made MUTO NAD+ Cellular Complex").
- [ ] **"Thousands of them have switched"** in version B's sub-headline: confirm it's true.
- [ ] **Customer reviews** quoted on the pages are Jonathon R, Lynda, Danny S and Holly P, word for word from the product page.
- [ ] **Page addresses** were my choice. Change them before ads point at them if you want different ones.

# Check after publishing

Do this on both pages, on a phone and on desktop, without `preview_theme_id`.

1. The article shows (not an empty page). No store header, no black bar at the top, no sticky add to cart.
2. The countdown is running.
3. Every green "See today's Black Friday offer" button scrolls to the offer.
4. "Claim today's offer" opens the side cart with **NAD+ Cellular Complex, 3-month subscription, £99** and the six free gifts at £0: creatine, socks, travel vial, Forever Jar, 12-week eBook, Apple Watch entry.
5. "View nutrition table" opens the label, and closes on the cross, on a tap outside it and on Escape.
6. "View third-party test results" opens the panel showing 10 of 10 tests passed.
7. Reviews load under the trust section.
8. Version A: seven numbered cards, the bar chart and the grey "Why energy falls with age" panel. Version B: five numbered cards, three starred customer quotes and the grey panel.
9. Safari on a Mac and an iPhone: repeat 4, 5 and 6.

# What was tested, and what wasn't

Tested on the preview theme on 18 November, in a Chromium browser at 390px, on both pages: everything in the checklist above passed, including the cart contents in step 4. Desktop width was tested for layout and the nutrition label on the earlier product-template version.

Not tested: Safari and Firefox; checkout beyond the cart; the pages on the live theme; the Claim button's fallback route with the Black Friday bar removed.
