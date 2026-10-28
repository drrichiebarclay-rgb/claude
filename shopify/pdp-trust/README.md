# Main product page: trust bands and a more clinical voice (28 Oct 2026)

Template `product.muto-nad-45` (the main NAD+ page, `/products/muto-nad-cellular-complex`).
Built on the **live** template as of 28 Oct (`live-snapshot-28oct/`, last edited on live 19 Oct), so live edits are kept.
The buy box is not touched. Rebuild with `python3 make_trust.py`.

## Files to copy into the live theme (in this order)

1. `theme/assets/muto-crea-trust.css`
2. `theme/sections/muto-crea-standards.liquid`, `muto-crea-reviews.liquid`, `muto-crea-founder.liquid`, `muto-crea-statement.liquid`
3. `theme/templates/product.muto-nad-45.json`

All four sections are new names, so nothing on live is overwritten except the template.

## New page order

| # | Band | Status |
|---|---|---|
| 1 | Buy box | unchanged |
| 2 | **Our standards**: third-party tested, 300mg NR + declared doses, Scientific Advisory Board, UK made GMP · ISO | new |
| 3 | Customer videos, 9:16 (existing "results" band) | retitled "Customer reports." |
| 4 | **Rotating reviews** ("Selected reviews."): up to 20 hand-picked written reviews, name + age, auto-advance every 6s | new |
| 5 | **Founder**: Dr Richie Barclay, PhD | new |
| 6 | Scientific Advisory Board | retitled |
| 7 | **Statement**: "A daily supplement." / "Built for your biology after 35 years old." | new |
| 8+ | Problem, benefits, 90-day steps, guarantee, compare, FAQ, REVIEWS.io widget | copy tightened |

The old "Why people trust MUTO" three-card band is **hidden, not deleted** (founder and standards now cover it).

## More clinical copy (light touch)

- Videos: "Real people. Real stories." → "Customer reports."
- Board: "Our experts." → "Scientific Advisory Board." / "Six doctors and scientists who review the formula."
- Steps: "Give it 90 days. See how you feel." → "A 90-day protocol. Measured by you." Steps: Record a baseline / 2 capsules, with breakfast / First check-in / Compare with day 1.
- Compare: "The easy way to get NAD⁺." → "One formula. Every dose declared." Rows: "300mg NR…", "Every dose declared on the label".
- FAQ: new "How is it tested?"; "Why not just take one vitamin?" now names the doses.

## Before it goes live

- [ ] **Reviews: fill to 20.** 8 real quotes are in (from the landing pages). Pick 12 more from REVIEWS.io, 5-star, over-30s, on-message (energy, recovery, feeling like yourself, one jar, the science). Copy the words exactly.
- [ ] **Ages.** Add each reviewer's age (with their OK). Reviews with an age under 30 are hidden automatically. Once every card has an age, tick "Only reviews with an age" to enforce over-30s only.
- [ ] **Rating summary** (e.g. "4.8 from 412 reviews"): add the live REVIEWS.io figure, or leave blank.
- [ ] **Certificates link.** The copy says "Certificates of analysis on request" until a URL is set. Once the certificates are published, set the link on standard 01 (or `CERTS_URL` in `make_trust.py`) and the card shows "View the certificates →".
