# Main product page: trust bands and a more clinical voice (28 Oct 2026)

**Dev handover (28 Oct): `handoff/MUTO_Dev_Handoff_Main_PDP_28Oct2026.docx`.** MUTO10 was ended on 28 Oct 17:19 and the pre-sale box is removed from this template.

Template `product.muto-nad-trust` (the main NAD+ page, `/products/muto-nad-cellular-complex`).
Built on the **live** template as of 28 Oct (`live-snapshot-28oct/`, last edited on live 19 Oct), so live edits are kept.
The buy box is not touched. Rebuild with `python3 make_trust.py`.

## The main page is now `muto-nad-v2` (27 Oct)

The main product moved to template `product.muto-nad-v2` on 27 Oct. The buy box in this build is taken **verbatim from that live template**: the `buy` section (`muto-pdp-v2-buy`), its `easy_read` styling block (incl. the Black Friday box), the sticky bar, the `#scientific-board` anchor, the `#test-results` certificate panel (`muto-test-results`) and the "MUTO vs the usual" comparison (`compare`, section `muto-chapter`). `make_trust.py` copies them from `live-snapshot-28oct/templates__product.muto-nad-v2.json`.

## Files to copy into the live theme (in this order)

1. `theme/assets/muto-crea-trust.css`
2. `theme/sections/muto-crea-standards.liquid`, `muto-crea-reviews.liquid`, `muto-crea-founder.liquid`, `muto-crea-statement.liquid`
3. `theme/templates/product.muto-nad-trust.json`

All four sections are new names, so nothing on live is overwritten except the template.

## New page order

| # | Band | Status |
|---|---|---|
| 1 | Buy box | unchanged |
| 2 | **Statement**: "Not ready to slow down." / "The next-generation multi-nutrient, built for what your body needs in your 40s and 50s." | new |
| 3 | Scientific Advisory Board, now the **compact row** (all six across on desktop) | retitled |
| 4 | **Our standards**: four sage cards (third-party tested, 300mg NR + declared doses, advisory board, UK made GMP · ISO) | new |
| 5 | Customer videos, 9:16 (existing "results" band), **8 videos in a scrolling row** (2 added from page.borrowed-energy: Muto 1 and Muto 2; names to fill in) | retitled "Don’t take our word for it." |
| 6 | **Rotating reviews** ("What our community say."): up to 20 hand-picked reviews, name + age, auto-advance every 6s | new |
| 7 | **Founder**: Dr Richie Barclay, PhD | new |
| 8+ | Problem, benefits, 90-day steps, guarantee, compare, FAQ, REVIEWS.io widget | copy tightened |

The old "Why people trust MUTO" three-card band is **hidden, not deleted** (founder and standards now cover it).

**Backgrounds:** no gradient washes anywhere on the page. Bands alternate flat grey (#F2F2F2) and white, set in a template-only `bands` style block at the end of the template (built by `make_trust.py`).

The new bands use the page's own patterns (sage glass cards, mono notes opposite the heading, sparkle tag pills) in the brand palette: #FAFAFA, #C8D2CF, #5EFAFF, #C9FFB7, #F0FF84, #242223.

## More clinical copy (light touch)

- Videos: "Real people. Real stories." → "Customer reports."
- Board: "Our experts." → "Scientific Advisory Board." / "Six doctors and scientists who review the formula."
- Timeline: "Your first 90 days. What to expect." Day 1 set your baseline / Day 30 afternoons that hold / Day 60 bouncing back sooner / Day 90 feel it, or your money back.
- Compare: "The easy way to get NAD⁺." → "One formula. Every dose declared." Rows: "300mg NR…", "Every dose declared on the label".
- FAQ: new "How is it tested?"; "Why not just take one vitamin?" now names the doses.

## Before it goes live

- **Reviews: 20 in.** 5-star REVIEWS.io reviews, copied word for word (whole or one unbroken passage). Rating line "4.8 from 103 reviews" is typed in: update it as the count grows.
- [ ] **Ages.** Add each reviewer's age (with their OK). Reviews with an age under 30 are hidden automatically. Once every card has an age, tick "Only reviews with an age" to enforce over-30s only.
- [ ] **Certificates link.** The copy says "Certificates of analysis on request" until a URL is set. Once the certificates are published, set the link on standard 01 (or `CERTS_URL` in `make_trust.py`) and the card shows "View the certificates →".

## Black Friday clone: `product.muto-nad-bf`

Same page as above, built from it by `make_bf.py`. Changes:

- **Box above the plans** (white, black outline): "BLACK FRIDAY OFFER" / "53% off your first order" / "plus a welcome kit worth £77" / "£99 for your first order, £125 on your second, £150 on your third." On the right, a counter tile "500 of 500 left", a bar along the foot and "Limited to 500 orders."
- **Quarterly card:** "Save 53%", **£33/mo** with £70 struck through, "3 months’ supply: £99 for your first box, then £125, then £150 · £1.10 a day". The sticky bar shows £33/mo too.
- **Subhead:** "Our lowest price yet, while stocks last. Been waiting to try MUTO? Now’s the time to run the 90-day test."
- **Monthly card:** "Save 28%", **£49.99/mo** with £70 struck through, "£49.99 for your first month, then £60 every 4 weeks · £1.79 a day", welcome kit worth £62.
- The orders-left count is the shop metafield **`muto.bf_orders_left`** (created 28 Oct, set to 500; Settings → Custom data → Shop → "Black Friday orders left (53% offer)"). Blank hides the count; 0 shows "All 500 have gone."

Before it goes live:

- [ ] **Discounts:** Quarterly £99 first box, £125 second, £150 third (Skio bills £150); Monthly £49.99 first, then £60 (Skio bills £60). These need to exist in Shopify / Skio. Then set `CODE` at the top of `make_bf.py` and rebuild so the page applies the code automatically, as MUTO10 was.
- [ ] **Add-to-cart button** still shows Skio’s billed price (£150) until the discount applies; check it reads right in the cart.
- [ ] **Flow:** Order created + uses the Black Friday code → `muto.bf_orders_left` minus 1 (same pattern as the welcome-kit Flow in `handoff/handoff_17oct_pdp_buybox.md`).
- [ ] **At 0:** turn the discount off. The box will say "All 500 have gone."
