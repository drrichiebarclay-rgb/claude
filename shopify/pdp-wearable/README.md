# Wearable PDP (`product.muto-nad-wearable`)

A separate version of the live main product page (`product.muto-nad-bf-premium`) for people who already do the
basics well (sleep, training, food), track on a wearable, and whose HRV, sleep and recovery numbers won't move.
30+, about 60% men. The angle: the biology under energy and recovery (NAD+, mitochondria) as the next layer,
checked on their own device over 90 days.

- **Theme:** Clone Of Live | Wearable PDP [23-11] (ID 205557006683), a copy of the live theme made 23 Nov 2026.
- **Preview** (main product, no product changes needed):
  https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-wearable&preview_theme_id=205557006683
- **To use it for real:** give a product (e.g. a new unlisted copy of NAD+ Cellular Complex for ads) the template
  `muto-nad-wearable`, on whichever theme is live. Templates live per theme, so copy
  `templates/product.muto-nad-wearable.json` to the live theme first.

## Same as live

Design, offer, plans, gifts, photos, Black Friday bar and box, reviews, test results, ingredient library,
comparison, founder and board.

## What changed

| Where | Live | Wearable |
|---|---|---|
| Line above headline | Designed for over 35s | For over-30s who track their recovery |
| Headline | One daily routine for energy, recovery, healthy ageing and strength. | Doing the basics right? Your numbers still won't move. |
| Line under headline | …support your energy, recovery and healthy ageing | The layer under sleep, training and food: NR → NAD+ → mitochondria. 7-day baseline, 30-day averages |
| Ticks | More energy… / Recover in time… / Built for the years ahead | The biology behind your energy / Ready for the next session / Built to be tracked on your wearable |
| Review chips | Next 20 years / Flat by 3pm / Slower to bounce back | Playing the long game / Energy flat despite good sleep / Recovery score stuck (same filters) |
| Benefits, Who it's for folds | Busy-life wording | Layer underneath the basics; "Is it for you?" names the stalled-metrics customer and the devices |
| Dark band | Your life won't fit a perfect routine | The basics are done. Good sleep. Smart training. Same flat line. |
| Survey | Energy first | HRV first; "What 87 customers reported." |
| Why it happens | It's not in your head | You've fixed the basics. Your biology still changed. (same stats and sources) |
| Benefits section | Energy, recovery and healthy ageing | What's underneath your numbers (NAD+ and mitochondria) |
| Timeline | First you feel it. Then you check it. | Run it like an experiment: baseline, read around the noise, your verdict |
| Testimonials | Mixed | Training, sleep and recovery quotes on (all real, unchanged) |
| FAQ | | New first three: What's left if I already do the basics? Will it improve my HRV? Which devices work? |

## Claims

Authorised nutrient claims only, worded exactly. No metric is promised to change ("We won't promise what any number
will do"). The NR study is labelled as a study of NR, not of MUTO. Customer quotes are unchanged.

## How it's built

Template-only. Shared snippets whose words needed to change (buy-box lines, ticks, review chips, dark band) are
rendered into a variable in this template and their strings swapped, so no shared file changes and every other
page is untouched. The template also sets the BF page styles' Design to Premium and adds the
`template-muto-nad-bf-premium` body class, because the premium look switches on by template name.

- `make_wearable.py` builds the template from `base/live__product.muto-nad-bf-premium.json` (live, 23 Nov).
- `make_jq.py` turns the build into `wearable.jq`, a jq edit of the live template, used to create the file on
  Shopify without sending the whole 210 KB file.
- If a swapped string changes in a shared snippet, its replacement silently stops applying: the build script
  checks every string against the snippet copies in `base/`.
