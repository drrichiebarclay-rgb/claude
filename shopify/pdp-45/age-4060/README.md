# Main PDP buy box for 40-60 year olds (20 Oct 2026)

`/products/muto-nad-cellular-complex` uses template `product.muto-nad-45`. This changes that template's buy box so it speaks to 40-60 year olds who aren't sport focused.

- **What to copy:** `product.muto-nad-45.json` → live theme `templates/product.muto-nad-45.json`. One file, template-only. The `muto-crea-buy` section doesn't change.
- **Built from live:** the source is the live template as of 20 Oct (`live-snapshot-20oct/`, last edited on live 19 Oct). If live is edited again before this is copied, refresh the snapshot and run `python3 age-4060/apply_4060.py` from `shopify/pdp-45/`.
- **Unchanged:** prices, plans, gifts and their plan tags, the Black Friday pre-sale box, the gallery, and everything below the buy box.

## What changes, top to bottom

| Part | Before | After |
|---|---|---|
| Serving line | 30-day supply, third-party tested, 90-day guarantee | 2 capsules with breakfast · 30-day supply (60 capsules) |
| Headline line | For adults 35+ who aren't ready to slow down | A daily formula to help you feel less tired, made for your 40s, 50s and 60s |
| Paragraph | 30 trillion cells, track recovery and readiness on your wearable | Afternoons feel harder, 19 nutrients in two capsules, no gym, no gadgets, no powders |
| Benefits ("How it helps") | NAD+, fatigue, energy metabolism, protect cells, five bottles in one, track it on your wearable | Tiredness + fatigue, energy from food, cognitive function, immune system, normal bones, one jar instead of five pots |
| Reassurance row (new) | none | 90-day money-back guarantee · Skip, pause or cancel online · Made in the UK, every batch lab tested |
| Plan ticks | Gifts first | Guarantee, cancel online with no phone calls, free UK delivery, then the welcome kit |
| Quarterly note | Billed £150 every 3 months | 3 months' supply, billed £150 every 3 months |
| Welcome kit tiles | Creatine, Socks, Jar, Bottle, Guide, Garmin | Jar, Guide, Bottle, Socks, Creatine, Garmin (same gifts, everyday items first) |
| Future gifts label | Future gifts | Thank-you gifts in later boxes |
| One-time row | One-time purchase, no gifts | Prefer to try one jar first? Buy once (no gifts) |
| Review quotes | Includes "Has actually changed my recovery" | That quote is removed. Afternoon slump, focus and "replaces multiple products" stay |
| "Who it's for" fold | 35+, recovery takes longer | 40s, 50s and 60s, keeping up with work and family, no need to be sporty |
| Type | | Larger body, benefit, plan and button text, and darker greys, for easier reading |

The benefit lines use the UK authorised claims for the formula's B vitamins, zinc, and vitamins D and K. Have them checked before going live if you have a regulatory reviewer.

## Check before publishing

- [ ] **Quarterly delivery:** the note says "3 months' supply". If the quarterly box isn't a full 3 months of capsules, change that wording.
- [ ] **On a phone:** the reassurance ticks stack, the benefits show in one column, and the plan boxes fit the width.
- [ ] **Block count:** 42 of the section's 50.
- **Not covered here: photos.** The carousel comes from the product's Media (10 images), not the template. If any of the first few are sport shots, lead instead with the jar and an everyday shot (morning routine, walking). Don't use Files → Replace, because other products share those images.
