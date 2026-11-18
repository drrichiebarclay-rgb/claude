# Advertorial: "Most people over 35 think they're just tired. Here's what may really be happening inside your cells."

A direct-response advertorial for paid traffic, modelled on the format Richie supplied as a reference:
bold headline with one phrase in green, "Sponsored content" label, byline, lead photo and a read-time pill;
one-line paragraphs; a bar chart; a black "Why energy falls with age" panel; seven numbered cards, one per
nutrient, each with research notes, what to look for and its sources (tap "Sources"); MUTO introduced as the
one routine that holds all seven; a customer review; "What's in MUTO"; a timeline of what customers report;
and green buttons that scroll to the offer. It ends with **"Today's special offer"**: the Black Friday
bundle (photo, £33/mo, what's included) with a countdown and a Claim button, then the reviews widget.
There is no buy box, no Black Friday top bar and no sticky add to cart on this page.

Unlike the reference there is no before-and-after photo, no invented narrator and no symptom checklist:
the byline is Richie's, the review is a real one, the timeline is the product page's own, and every figure
has a source.

## Two versions, both Shopify pages

| | Version A: the science | Version B: the feeling |
|---|---|---|
| Page | `/pages/running-on-empty-after-35` | `/pages/not-lazy-running-on-empty` |
| Template | `page.lp-energy-35` | `page.lp-energy-35-feel` |
| Builder | `build.py` | `build_feel.py` (imports `build.py`) |
| Headline | "You're doing everything right. So why are you still running on empty after 35?" | "You're not lazy, you're running on empty, and it isn't your fault." |
| Middle | Chart, seven nutrient cards with research notes and sources | Five "sound familiar?" cards, three customer reviews, "Two capsules, every morning", what's inside in plain English, the guarantee |
| Shared | Offer with countdown, trust section, reviews, test-results panel | Same |

Both pages exist in Shopify (created 18 November 2026): published, hidden from search (`seo.hidden`), each
assigned its template, each with its own SEO title and description. Until the files below are on the live
theme the public addresses show an empty page, because the live theme doesn't have the templates yet.

Preview on the unpublished theme "Clone Of Live | load flash fix [12-11]" (ID 204807176539), where the files
already are: add `?preview_theme_id=204807176539` to either address.

## Files to copy to the live theme (3)

Copy the section first: a template that names a section, or a setting, the theme doesn't have is rejected.

| File | What it is |
|---|---|
| `theme/sections/muto-lst-needs.liquid` | New section, "MUTO listicle essentials". Nothing existing is changed. |
| `theme/templates/page.lp-energy-35.json` | Version A |
| `theme/templates/page.lp-energy-35-feel.json` | Version B |

Everything else the pages use is already on the live theme: `muto-lst.css`, the reviews section
(`custom-reviews`), the test-results section (`muto-test-results`) and the Black Friday bar in the header.

The earlier product-template versions (`product.muto-nad-bf-lp-energy-35*.json`) are still on the preview
theme and can be deleted there; they are no longer in this folder.

## Why these work as pages

A page has no product in scope, so the section has a **Product for the offer button** setting, set to NAD+
Cellular Complex. The Claim button reads that product's 3-month plan from it. The reviews widget is the one
the other landing pages use, which is already set up for a page.

## How the Claim button works

It adds the 3-Month Supply and opens the side cart by handing the tap to the Black Friday bar's own script
(`snippets/muto-bf-bar.liquid`, which the header puts on every page). That is the same route as the bar's
"Claim" and the over-35 listicle's offer card, so the welcome gifts are added by the theme as usual. The bar
itself is hidden on this page ("Hide the Black Friday bars" in the section settings) but must stay in the
header. If the header bar is ever removed, the button falls back to a plain add-to-cart link.

## The offer copy is typed, not live

Price, "was" price, billing lines and the list of gifts are text in the Offer block, taken from the live
over-35 listicle's offer card on 18 November 2026. Update them when the offer changes.

## The countdown

- **Offer end date blank (as built):** counts down to midnight tonight on the visitor's clock and starts
  again the next day.
- **Offer end date set (YYYY-MM-DD):** counts down to midnight at the end of that day, then hides.

## Editing in the theme editor

- **Article header:** headline, standfirst, byline, lead photo and caption are in the section's settings.
- **Direct layout** (ticked on this page) gives the look above. Wrap a phrase in `<em>…</em>` in any heading to
  turn it green. "News article layout" is the earlier serif version; with both unticked you get the card
  design with "Essential 1 of 7" badges.
- **Button**, **Bar chart**, **Image** and **Timeline** are blocks you can add, move or remove. Bars are one
  per line: `Label | number 0-100 | text beside the bar`. Timeline stages are `Stage title | What people report`.
- **Text** blocks carry the story. The first one, above essential 1, opens with a large first letter.
- **Quote** blocks are a pull quote or a customer review (tick "Show five stars").

- Essentials number themselves. Drag to reorder, and "Essential 3 of 7" follows.
- **Research findings:** one per line. To cite a source, end the line with `|` and its number:
  `NAD+ levels fall with age. | 1`
- **Sources:** one per line, in the order they are numbered.
- **Dark panel:** drag it between any two essentials.
- **Answer:** the checklist is one row per line, `Essential | What MUTO provides`. Its button scrolls to the
  buy box.

## Claims: how the copy was written, and what to check

- Authorised health claims are worded exactly and sit in the small print under each essential (B vitamins,
  niacin, copper, zinc, vitamin D, vitamin K, creatine).
- NAD+, CoQ10, PQQ and resveratrol have no authorised claims in Great Britain. Their copy says what they are
  and what a named study measured, with the source. It does not promise a result. Essential 1 says outright
  that trials measure NAD+ levels, not how people feel, and essential 7 says the research is early.
- Sources reuse the references already on the live product page's ingredient library where they exist.
  Figures added for this page were checked against the papers' abstracts on 18 November 2026: Massudi 2012,
  Conze 2019 (51% at 300mg), Tsai 2022 (13 trials, 1,126 people), Short 2005 (146 adults aged 18 to 89),
  MacLaughlin and Holick 1985 (more than twofold) and Gandia 2007 (43.4%).

Before ads go live:

- [ ] **The countdown must be true.** A timer that resets every night on an offer that is still there the
      next day is a false time limit, which UK consumer law (the DMCC Act 2024) and the ASA treat as a
      banned practice. Either the price really changes at midnight each day, or put the offer's real last
      day in "Offer end date", or untick the countdown. Same for the label "Today's special offer" and
      "Offer ends at midnight".

- [ ] **Richie: it's in your voice.** Approve or reword the opening ("I get asked the same thing most
      weeks…"), the opinions ("it isn't fashionable, which is partly why I like it", "the early results are
      interesting enough for me") and "That's the reason I made MUTO NAD+ Cellular Complex."
- [ ] **Two factual asides to confirm:** methylated B vitamins "cost more to put in a capsule", and
      "Creatine doesn't fit in a capsule at a useful dose".
- [ ] **Dateline** in the byline: "Updated November 2026". Change it when the article is revised.
- [ ] **Customer quote:** Jonathon R's review, word for word from the product page.

- [ ] **Regulatory read-through.** Citing studies for ingredients without an authorised claim (the CoQ10
      fatigue analysis, the PQQ studies, NAD+ levels) can still be read as an implied health claim by the
      ASA. Have your adviser check essentials 1, 2 and 7 and the black band.
- [ ] **Conze 2019 used NIAGEN-brand NR.** The page says "300mg of NR a day"; confirm you're happy citing it
      for MUTO's NR.
- [ ] **Creatine wording** in the answer: "comes free in your welcome kit" and "Free 250g pouch with your
      first subscription order". Update if the welcome kit changes.

## Check after copying

1. Open each page on a phone. No black bar at the top, no store header, no sticky add to cart.
2. Seven numbered cards, the black panel, the timeline.
3. Every green button scrolls to "Today's special offer".
4. The countdown is running.
5. "Claim today's offer" opens the side cart with the 3-Month Supply at £99 and the welcome gifts.
6. Reviews load under the offer.
