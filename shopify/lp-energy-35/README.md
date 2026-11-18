# Advertorial: "Why you're more tired after 35: a cell biologist on the seven nutrients that matter"

An advertorial for paid traffic, laid out like a news article and written in Richie's voice: category line,
headline, standfirst, byline, lead photo with a caption, then a single serif reading column. Seven numbered
subheads (NAD+, CoQ10, B vitamins, creatine, zinc and copper, D3 and K2, PQQ and trans-resveratrol), each
with a few plain paragraphs, what to look for on a label, the evidence as a short list and its sources. A
black "Why energy falls with age" explainer sits between 2 and 3. MUTO isn't named until "Getting all seven"
at the end, followed by a customer review, what's in MUTO, the **live main product page's buy box** and the
reviews widget.

Page address once the files are on the live theme:

    https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-bf-lp-energy-35

Previews (the new sections rendered into the live product page's own HTML and CSS, 18 November 2026):
`previews/mobile-390.jpg` and `previews/desktop-1440.jpg`. The reviews widget looks unstyled in them only
because the preview machine can't load REVIEWS.io's stylesheet; the section is the live page's, unchanged.

## Files to copy to the live theme (2)

Copy the section first: a template that names a section the theme doesn't have is rejected.

| File | What it is |
|---|---|
| `theme/sections/muto-lst-needs.liquid` | New section, "MUTO listicle essentials". Nothing existing is changed. |
| `theme/templates/product.muto-nad-bf-lp-energy-35.json` | New product template. |

Nothing else is needed. The template uses sections, snippets and stylesheets already on the live theme
(Clone Of Live | sticky bar [12-11], ID 204801016155), and every image is already in Shopify Files.

To try it on an unpublished theme first, copy both files there and add `&preview_theme_id=<theme id>` to the
address above.

## Why a product template, and why this name

- **Product template:** the buy box only works with a product in scope, so the page is the main product
  shown through a second template (`?view=`), the same way the over-35 listicle is
  (`product.muto-nad-bf-lp-over-35`). No product's template assignment changes.
- **`muto-nad-bf` in the name:** the header and footer switch on the Black Friday top bar and the sticky add
  to cart for any template whose name contains it. Rename the file and they disappear.

## What's on the page, top to bottom

| Section | Source |
|---|---|
| Black Friday styles, buy-box styles, top bar | Live product page, unchanged |
| Article header (headline, standfirst, byline, lead photo), opening story, the 7 essentials, the black band, the customer quote and the answer | `muto-lst-needs` (new) |
| Buy box | Live product page, unchanged |
| Reviews widget | Live product page, unchanged |
| Test-results panel (opened by the buy box's button) and the buy box's scripts | Live product page, unchanged |

Left out on purpose: the "As seen in" row and dark "Your life won't fit a perfect routine" band that follow
the buy box on the product page (`ag1_plans`). They aren't part of the buy box, and the page has its own
black band.

## The buy box is a copy taken on 18 November 2026

It is the live template's buy box, block for block (`live-snapshot/product.muto-nad-bf-premium.json`). It
does **not** follow later edits to the product page. When the product page's offer or buy box changes:

1. Save the live `templates/product.muto-nad-bf-premium.json` over the copy in `live-snapshot/`.
2. Run `python3 build.py`.
3. Copy the rebuilt template to the theme.

The copy on this page lives in `build.py`. Everything is also editable in the theme editor (choose the
template from the menu at the top); tell me about editor changes so the script keeps them.

## Editing in the theme editor

- **Article header:** headline, standfirst, byline, lead photo and caption are in the section's settings.
- **News article layout** (ticked on this page): serif reading column, numbered subheads, plain lists. Untick
  it for the card design with "Essential 1 of 7" badges. "Article style" on its own only sets headings in
  sentence case.
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

1. Open the address on a phone. Black Friday bar at the top, no store header, then the headline and byline.
2. Seven essentials, numbered 1 to 7, with the black band between 2 and 3.
3. "See today's offer" scrolls to the buy box.
4. The buy box matches the main product page: plans, welcome kit, price and button. Add to cart on each plan.
5. "View third-party testing results" opens the panel.
6. Reviews load under the buy box.
7. The sticky add to cart appears at the foot of the screen.
