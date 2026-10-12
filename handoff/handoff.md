---
title: "MUTO site changes: dev handoff"
subtitle: "12 October 2026"
---

Most of the 10 October handoff is now live. This update covers what's left: **8 files**, all in `shopify/live-ready`. One of them is a new version of the NAD+ product page with creatine in the first-order kit. It changes nothing until you point traffic at it.

# Before you start

- **Copy from:** the folder `shopify/live-ready` in GitHub (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`): <https://github.com/drrichiebarclay-rgb/claude/tree/claude/faq-page-shopify-redesign-hbqcg8/shopify/live-ready>. It now holds only the 8 files still to copy, at their theme paths.
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451). Sections first, then templates, or a template save fails on settings its section doesn't have yet.
- **How the folder was made:** on 12 Oct I compared each live-ready file with the live theme. 8 were identical, so they're done and were removed from the folder. What's left is below.
- **Buy section is built on today's live file.** Live's `sections/muto-crea-buy.liquid` now has your duplicate-option fix (`seen_options`). The live-ready copy is that exact file with the new options merged in, so the fix stays. Don't take this section from the 3M refill plan theme: that copy still carries the unreleased 3M refill plan code.
- **To see the new pages working:** preview the 3M refill plan theme (ID 202682564955): <https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-live-creatine-kit&preview_theme_id=202682564955>. In live the template is named `product.muto-nad-creatine-kit.json`.

# Already live: no action

These match live exactly: `muto-crea-ingredients`, `muto-home-board` and `muto-home-science` sections; home (`index.json`), `page.muto-home`, `page.about-us`, `page.about-muto` and `product.muto-socks` templates; the review card in the buy section; and the NAD+ product description.

# The 8 files to copy

| File | Page | What changed |
|---|---|---|
| `sections/muto-crea-buy.liquid` | NAD+ product pages | Today's live file plus new optional settings for the first-order kit (details below). All are off or blank by default, so the current NAD+ page looks exactly the same. |
| `sections/faq-schema.liquid` | FAQ | "How do I claim?" answer: claim window now "within 14 days after your 90 days end" (was "within 104 days of your first order…"). |
| `templates/page.faq-new.json` | FAQ (/pages/faqs) | Same claim-window wording in the visible answer. |
| `templates/product.muto-nad.json` | NAD+ product page | FAQ "What if it's not for me?": "within 14 days after your 90 days end" (was "within 90 days of your first order"). Nothing else. |
| `templates/product.muto-bottle.json` | Bottle product page | Not shipped last time. "Shop the protocol" NAD+ tab: new subheader, three steps, "What's inside" label (same as socks, which is live). |
| `templates/product.muto-nad-simple.json` | Simple NAD+ page (test) | Live has the 3M refill plan theme's version, which includes the unreleased "3 months £135" plan card (`plan_RAXANa`). This copy is built on the live product page and leaves that card out. Copy it unless the 3-month plan is meant to be on this page. |
| `templates/product.muto-nad-creatine-kit.json` | **New:** NAD+ page with creatine kit | See below. |
| `templates/product.muto-socks.json` | Socks product page | Only change: "Use the product's own images" switched on (see below). |

Every product template in this folder also has "Use the product's own images" switched on.

# Product images come from Shopify admin

New setting in `sections/muto-crea-buy.liquid`: **Use the product's own images** (`gallery_from_product`, off by default).

- When it's on, the gallery and thumbnails show the product's images from Products → Media in Shopify admin, in that order, with each image's alt text (product title if blank). Change, add or reorder images there and the product page updates; no theme edit needed.
- When it's off, or the product has no images, the gallery uses the "Gallery image" blocks as before.
- It's on in every product template in this folder (NAD+, simple NAD+, creatine-kit NAD+, bottle, socks).
- **NAD+ pages will change** when this ships: they'll show the 3 images now in the product's Media (the kit banner, "19 ingredients. Nothing hidden." and the label/jar shot) instead of the old gallery (kit set + two cyclist photos). Bottle and socks look the same, because their Media already matches.
- **Creatine page:** its template isn't in this folder. Turn the setting on in the theme editor (product page → Buy box → "Use the product's own images") after copying the section. Its Media already matches its gallery.
- Images should be 4:3 (1290×968 today) to fit the gallery frame without cropping.

# Kit options

These are also in `sections/muto-crea-buy.liquid`. They only appear when filled in, and today only the creatine-kit template uses them.

- **Wider kit grid:** with more than 4 gifts, the kit images sit on one row (one column per gift) instead of wrapping.
- **Itemised list** (`kit_itemised`, `kit_main`, `kit_main_note`): an "includes" list above the kit images. It shows the main product, then one row per gift with its value struck through and "Free". Each gift block gets `row_label` (row name) and `row_note` (replaces "Free", e.g. "Free entry").
- **Footer points under the list** (`kit_foot_1` to `kit_foot_4`), each with an icon (tick, clock, chevron, cross).
  - Points 1, 3 and 4 can open a pop-up: set `kit_foot_N_pop_title` and `kit_foot_N_pop`. The point then becomes an underlined link that opens a native `<dialog>`. It closes with the × button, the Esc key or a click on the backdrop.
  - **Point 4 shows on phones only** (under 750px). There, the four points form a 2×2 grid. On desktop the first three stay on one line.

# New: NAD+ page with creatine in the kit

**File:** `templates/product.muto-nad-creatine-kit.json`. It's built on today's live NAD+ template: same plans, prices and sections, with only the changes below.

**How to use it:** copying the file in changes nothing on its own. Either send traffic to `https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-creatine-kit`, or switch the product's template to `muto-nad-creatine-kit` in Shopify admin (Products → NAD+ Cellular Complex → Theme template).

**Needs:** the new `sections/muto-crea-buy.liquid` from this folder (copy it first). The creatine image is `gift-creatine.jpg` in Shopify Files (already uploaded).

| Area | Change |
|---|---|
| Kit images | Creatine added as the first gift: "Micronised Creatine", £30, image gift-creatine.jpg. All 5 gifts sit on one row. |
| First-order line | "Free with your first order: Ultrapure Micronised Creatine Monohydrate, performance socks, Forever Jar, 12-week protocol guide" |
| Itemised list | "Your first order includes:" NAD+ Cellular Complex (Included) · Ultrapure Micronised Creatine (~~£30~~ Free) · Performance Socks (Size UK 6-11) (~~£12~~ Free) · Forever Jar (~~£10~~ Free) · 12-Week Protocol Guide (~~£10~~ Free) · Oura Ring 5 prize draw entry (Free entry) |
| Footer points | "90-day money-back guarantee" (pop-up) · "Free next-day delivery" · "Skip or cancel anytime" (pop-up) · "No commitment" (pop-up, phones only) |
| Guarantee pop-up | "No risk. Take MUTO every day for 90 days. If you don't see a difference, we'll refund every subscription payment you made in that time, less delivery costs. Fewer than 0.1% of customers ask for their money back. For first-time subscribers at muto.co. Just email us within 14 days after your 90 days end. Full details" (link to /pages/faqs#guarantee) |
| Skip or cancel pop-up | "Going on holiday or running low? Skip a delivery, delay your next order, or cancel whenever you want, before your next charge. Total control, zero pressure." |
| No commitment pop-up | "You're never locked in. Pause, restart or cancel your MUTO plan at any time, directly from your account. No questions asked." |
| Ticked rows | The 6 ticked reassurance rows under the button are removed; the itemised list carries that message now. |
| FAQ | "What if it's not for me?": claim within 14 days after your 90 days end. |

The 3M refill plan theme also has creatine-kit versions of its own NAD+ page and the simple page (`product.muto-nad-creatine-kit`, `product.muto-nad-simple-creatine-kit`). They aren't in this folder: the first carries the unreleased 3M refill plan, and the simple one can be rebuilt on live if it's wanted.

# Still open

Most of these are copy decisions for Richie, not dev work.

- [ ] **"Fewer than 0.1% ask for their money back"** (guarantee pop-up): confirm it's backed by refund data before going live.
- [ ] **"No commitment" and "Skip or cancel anytime"** say much the same thing on phones. Keep both, or drop one.
- [ ] **"Free gifts worth £249"** (plans banner, same as live) was set before creatine (£30) joined the first-order kit. Check the figure on the creatine-kit page.
- [ ] **Creatine at later orders:** creatine is still the gift at orders 4 and 6 (as on live) and now also in the first-order kit. Confirm that's intended.
- [ ] **Refund policy** (Settings → Policies) still describes a 30-day guarantee with a wearable export. Rewrite it to the FAQ terms: 90 days, first-time subscribers at muto.co, less delivery costs, claim within 14 days after the 90 days end, wearable data optional.
- [ ] **"Full refund" wording** on the NAD+ product page: the "90-Day Money back Guarantee" accordion and the guarantee section say "in full". The FAQ says "less our delivery costs".
- [ ] **"Pre-Order Now - Arrives 15/10"** is hard-coded in the Add to Cart button in `muto-crea-buy.liquid`, not a setting. Remove it after 15 Oct.
- [ ] **Product search description** (SEO) still says "stress resilience".
- [ ] **"300+ supporting studies"** stat on the home page: flagged in the FAQ brief as unsupported.
- [ ] **/pages/muto-home** still has the old buttons ("Start your 90 days", "Start Today", "Coming Soon"), "seven scientists" and the "7 advisors" stat.
- [ ] **CoQ10 form on the home page:** the science Formula tab and "What's inside" say plain "CoQ10"; the FAQ table says Ubiquinone. Confirm whether the home page should say "(as ubiquinone)".
- [ ] **Claims review:** vitamin K2 sits under the immunity and muscle claims in the science Formula tab, product description and FAQ, but has no authorised claim for either.
- [ ] **Plan per-day prices:** live says "£2/day", but £60 every 4 weeks is about £2.14 a day.
- [ ] **Informed Sport:** swap the drug-tested athletes FAQ answer when certification is live (the certified wording is in MUTO_FAQ_Page_Final_Oct26.docx).

# Check after publishing

1. **NAD+ product page:** the gallery shows the 3 images from the product's Media in admin. Everything else looks as it does today: no itemised list, the ticked rows are still there, the review card still rotates, and plan picking still works (the duplicate-option fix is kept).
2. **Creatine-kit page:** open /products/muto-nad-cellular-complex?view=muto-nad-creatine-kit.
   - Five kit images sit on one row, under the itemised list.
   - Each pop-up opens and closes.
   - On a phone, "No commitment" appears as the fourth point in a 2×2 grid. On desktop it's hidden.
3. **Simple page:** /products/muto-nad-cellular-complex?view=muto-nad-simple shows the same plans as the normal page (no "3 months £135" card).
4. **FAQ (/pages/faqs):** "How do I claim?" reads "within 14 days after your 90 days end". Run it through Google's Rich Results Test (<https://search.google.com/test/rich-results>). It should find one FAQPage with 54 questions.
5. **Bottle product page:** the "Shop the protocol" NAD+ tab has the new steps and the "What's inside" label.
