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

- **Product template:** the offer's button needs the product in scope to find the 3-month plan, so the page
  is the main product shown through a second template (`?view=`). No product's template assignment changes.
- **The name** is kept so the address already shared keeps working.

## The trust section

Under the offer: six icon tiles (third-party tested, scientific board, made in the UK, GMP, ISO,
filler-free), the scientific board strip, and two buttons.

- **View nutrition table** opens the product page's nutrition label image in a pop-up.
- **View third-party test results** opens the product page's test-results panel. That panel is the
  `tests` section on the template, copied unchanged from the live product page, so update it there and
  rebuild when a new batch is tested.

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

1. Open the address on a phone. No black bar at the top, no store header, no sticky add to cart.
2. Seven numbered cards, the black panel, the timeline.
3. Every green button scrolls to "Today's special offer".
4. The countdown is running.
5. "Claim today's offer" opens the side cart with the 3-Month Supply at £99 and the welcome gifts.
6. Reviews load under the offer.
