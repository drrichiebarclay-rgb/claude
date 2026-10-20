"""Science page: builds templates/page.science-simple.json from
MUTO_Science_Page_Copy_Oct26.docx, in the same styles as the standards page.

  muto-science-hero  eyebrow, headline, subhead, byline and pinned chapter links (new section)
  muto-chapter       one per chapter: pinned number on the left, content on the right (new section)
  muto-home-board    the scientific board rail, the home page's slim cards, under chapter 5

Six chapters: what changes (with the science), how it shows up (charcoal band),
what's in it (stats, five job cards, the teams table folded), MUTO vs the usual,
the experts, your 90 days (a timeline), then the offer and reviews. Bands
alternate #fafafa and mint #c8d2cf. Ingredient lists are built from
../ingredients-page/ingredients.json, so all 19 appear with their doses.

Preview on the existing Science page with ?view=science-simple, so the live
/pages/science template is untouched. The doc's [Confirm …] notes are left off
the page; they're in README.md.

Usage: python3 build.py
"""
import copy, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ABOUT = json.loads(re.sub(r"^/\*.*?\*/", "", open(os.path.join(HERE, "..", "standards-page", "theme-ref", "templates__page.about-muto.json")).read(), flags=re.S))["sections"]
PDP = "/products/muto-nad-cellular-complex"
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"

S, ORDER = {}, []
ING = json.load(open(os.path.join(HERE, "..", "ingredients-page", "ingredients.json")))
SHORT = {"Nicotinamide Riboside (NR)": "NR", "Vitamin B12 (Methylcobalamin)": "B12 (methylcobalamin)", "Vitamin D3 (Vegan)": "D3",
         "TMG (Trimethylglycine)": "TMG", "Vitamin B2 (Riboflavin)": "B2 (riboflavin)", "Vitamin K2 (MK-7)": "K2 (MK-7)",
         "Zinc (Bisglycinate)": "Zinc bisglycinate", "Folate (5-MTHF)": "Folate (5-MTHF)", "Trans-Resveratrol": "Trans-resveratrol",
         "Grape Seed Extract": "Grape seed extract", "Vitamin B6 (P5P)": "B6 (P5P)", "Vitamin B1 (Thiamine)": "B1 (thiamine)",
         "Vitamin B3 (Niacin)": "B3 (niacin)", "Vitamin B5 (Pantothenic Acid)": "B5 (pantothenic acid)",
         "Copper (Bisglycinate)": "Copper bisglycinate", "BioPerine® (Black Pepper)": "BioPerine® (black pepper)"}
DOSE = {i["n"]: f"{SHORT.get(i['n'], i['n'])} {i['d'].replace(' mg', 'mg').replace(' mcg', 'mcg').replace('50mcg', '50mcg (2,000 IU)') if i['n'].startswith('Vitamin D3') else i['d'].replace(' mg', 'mg').replace(' mcg', 'mcg')}" for i in ING}


def having(tag):
    """Every ingredient on the ingredients page tagged with this job, with its dose."""
    return ", ".join(DOSE[i["n"]] for i in ING if tag in i["t"])


def named(*keys):
    """Ingredients by the start of their name, with doses."""
    out = []
    for k in keys:
        out += [DOSE[i["n"]] for i in ING if i["n"] == k or i["n"].startswith(k + " ")]
    return ", ".join(out)


def add(key, type_, settings, blocks=None):
    sec = {"type": type_, "settings": settings}
    if blocks is not None:
        sec["blocks"] = dict(blocks)
        sec["block_order"] = [k for k, _ in blocks]
    S[key] = sec
    ORDER.append(key)


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


def chapter(key, anchor, number, label, heading, intro="", art="none", blocks=(), takeaway="", line="", small="",
            cta_label="", cta_link="", tint=False):
    add(key, "muto-chapter", {"anchor": anchor, "number": number, "label": label, "heading": heading, "intro": intro,
                              "art": art, "takeaway": takeaway, "line": line, "small": small,
                              "cta_label": cta_label, "cta_link": cta_link, "tint": tint,
                              "space_top": 96, "space_bottom": 96}, list(blocks))


def point(k, title, text):
    return (k, {"type": "point", "settings": {"title": title, "text": p(text)}})


def table(k, heading, rows, highlight=0, note=""):
    return (k, {"type": "table", "settings": {"heading": heading, "rows": "\n".join(" | ".join(r) for r in rows),
                                             "highlight": highlight, "note": note}})


CHAPTERS = [  # anchor, chapter-link label
    ("what-changes", "What changes after 35"),
    ("how-it-shows-up", "How it shows up"),
    ("whats-in-it", "What’s in it"),
    ("muto-vs-the-usual", "MUTO vs the usual"),
    ("the-experts", "The experts"),
    ("your-90-days", "Your 90 days"),
]

# ---- Hero ----
add("hero", "muto-science-hero", {
    "eyebrow": "The science, made simple",
    "heading": "What changes in your body after 35, and what to do about it.",
    "sub": "No jargon. No hype. What happens inside you, how it shows up in your day, and why we built MUTO the way we did. In five minutes.",
    "author_image_fallback": CDN + "about-founder.jpg?v=1790751995",
    "author_label": "Explained by",
    "author_name": "Dr Richie Barclay, Founder · PhD, cell biology and nutrition",
    "nav_label": "Chapters", "nav_top": 0, "space_top": 120}, [
    (f"l{i}", {"type": "link", "settings": {"label": lab, "anchor": a}}) for i, (a, lab) in enumerate(CHAPTERS, 1)
])

# ---- 1: what changes, and the science behind it (one chapter) ----
chapter("c1", "what-changes", "01", "What changes after 35",
        "Somewhere after 35, your body starts working a little differently.",
        intro=p("Nothing dramatic happens overnight. But three quiet shifts start inside your 30 trillion cells, and they build through your 40s and 50s."),
        art="decline",
        blocks=[point("a", "You make less NAD+", "Every cell makes its own energy, in tiny power stations called mitochondria. NAD+ is the courier that carries energy from your food to them, over and over, all day. From your mid-30s, your body makes less of it. Fewer couriers, the same amount of work."),
                point("b", "You get less back", "Your body responds less to the same food and the same training. It’s called anabolic resistance, and it’s what I spent years studying in the lab. Same effort, smaller return."),
                point("c", "Your cells’ maintenance slows", "Making energy creates a little “exhaust”. The crews that clean it up, a family of enzymes called sirtuins, also run on NAD+. Fewer couriers means more competition for the same supply.")],
        takeaway="It’s not you doing anything wrong. It’s biology, and the basics you took at 30 weren’t built for it.")
S["c1"]["settings"]["art_beside"] = True  # bands alternate: page background, then mint

# ---- 2: how it shows up (charcoal band) ----
QUOTES = ["Sharp at 8am. Gone by 3pm.", "Hard sessions hang around for days.", "I’m doing everything right, and I still feel it."]
chapter("c2", "how-it-shows-up", "02", "How it shows up",
        "You don’t feel your cells. You feel your day.",
        blocks=[(f"q{i}", {"type": "quote", "settings": {"text": q}}) for i, q in enumerate(QUOTES, 1)],
        line=p("It’s like your body has switched to low power mode. Still working, still getting through the day, but running on less than it used to."))
S["c2"]["settings"]["band"] = "mint"

# ---- 3: what's in it ----
STATS = [("19", "ingredients, every dose on the label"), ("300mg", "NR, the most allowed in Great Britain"),
         ("2", "capsules with breakfast"), ("0", "proprietary blends")]
# The same five as the ingredients page filters: each card's line is the short form of that filter's
# statement (../ingredients-page/jobs.json) and lists every ingredient tagged with the job
JOBLINES = json.load(open(os.path.join(HERE, "..", "ingredients-page", "jobs.json")))
JOBS = [(j, JOBLINES[j], having(j)) for j in ("Energy", "Recovery", "Stress", "Longevity", "Immunity")]
TEAMS = [("Team", "Who’s on it", "What happens"),  # all 19, each once
         ("The energy team", named("Nicotinamide", "CoQ10", "PQQ", "Vitamin B2"), "NR becomes NAD+, the courier. CoQ10 is the relay runner that passes energy along inside the power station, and PQQ is studied for its role in the power stations themselves. B2 is part of the enzymes that release energy from food."),
         ("The B team", named("Vitamin B1", "Vitamin B3", "Vitamin B5", "Biotin"), "Each one is a working part in the steps that turn food into energy, and B1, B3 and B5 also support normal psychological function and mental performance."),
         ("The recycling team", named("Folate", "Vitamin B12", "Vitamin B6", "TMG"), "Your cells constantly reuse one of their most important building blocks. Folate and B12 keep that recycling loop turning, TMG runs a second loop alongside it, and B6 handles the exit. We use the active forms, the ones the cell actually uses."),
         ("The clean-up crew", named("Zinc", "Copper"), "Zinc and copper build the enzyme that cleans up the exhaust from making energy. One enzyme, two metals, so we pair them, both as bisglycinate."),
         ("The grape pair", named("Trans-Resveratrol", "Grape Seed Extract"), "Plant polyphenols from grapes. Trans-resveratrol is widely studied in healthy-ageing research, and grape seed extract is standardised to 95% polyphenols."),
         ("The bone relay", named("Vitamin D3", "Vitamin K2"), "D3 tells your cells to make a bone protein. K2 switches that protein on. D3 makes it, K2 activates it."),
         ("The helper", named("BioPerine®"), "Black pepper extract, added to help your body take in the other ingredients. No taste, no heat.")]
assert sorted(x for r in TEAMS[1:] for x in r[1].split(", ") if not x[0].isdigit()) == sorted(DOSE.values()), "every ingredient once"
t2 = table("t2", "How the 19 ingredients work together", TEAMS)
t2[1]["settings"]["fold"] = True
chapter("c3", "whats-in-it", "03", "What’s in it",
        "Five jobs, one jar.",
        intro=p("MUTO is built for what you actually need after 35: one daily formula covering five jobs, so you’re not guessing across five separate pots."),
        blocks=[(f"n{i}", {"type": "stat", "settings": {"value": v, "label": l}}) for i, (v, l) in enumerate(STATS, 1)]
               + [(f"j{i}", {"type": "card", "settings": {"kicker": f"0{i}", "title": t, "text": x, "detail_label": "What’s in it", "detail": d}})
                  for i, (t, x, d) in enumerate(JOBS, 1)]
               + [t2],
        line=p("Plus BioPerine® (black pepper) 5mg in every serve, to help your body take in the rest. That’s all 19."),
        cta_label="See every ingredient", cta_link="/pages/ingredients",
        small=p("Vitamins B6 and B12 contribute to the reduction of tiredness and fatigue. Vitamin D contributes to normal muscle function. Vitamins D and K contribute to the maintenance of normal bones. Zinc, copper and vitamin D contribute to the normal function of the immune system. In a study of adults aged 40 to 60, 300mg of NR a day raised NAD+ by 51% in two weeks. That study tested NR on its own, not MUTO."))

# ---- 4 ----
VS = [("", "MUTO", "Multivitamin", "Greens powder", "Collagen or joint capsules"),
      ("Built for", "What you need after 35: five jobs", "The basics", "The basics", "One area"),
      ("NR, for NAD+", "✓ 300mg", "Not usually included", "Not usually included", "Not usually included"),
      ("Active (methylated) B vitamins", "✓", "Varies: check the label", "Varies: check the label", "Not usually included"),
      ("Vitamin D3 with K2", "✓ 2,000 IU + 100µg", "Varies: check the label", "Varies: check the label", "Not usually included"),
      ("Zinc and copper, dosed as a pair", "✓ 15mg + 1mg", "Varies: check the label", "Varies: check the label", "Not usually included"),
      ("Every dose on the label", "✓ All 19", "Varies: blends are allowed", "Varies: blends are allowed", "Varies"),
      ("Every batch third-party tested", "✓", "Not required by law", "Not required by law", "Not required by law"),
      ("Scientists with names", "✓ PhD founder + six-member board", "Varies", "Varies", "Varies"),
      ("90-day money-back guarantee", "✓", "Varies", "Varies", "Varies"),
      ("How many pots", "One jar", "One of several", "One of several", "One of several")]
chapter("c4", "muto-vs-the-usual", "04", "MUTO vs the usual",
        "What you’ve been taking vs what you actually need.",
        intro=p("Most people in their 40s and 50s are taking some mix of these. Here’s how they compare."),
        blocks=[table("t1", "", VS, highlight=2,
                      note="Comparisons are by category, not brand, and products vary. Hold any label up against ours. Multivitamins, greens and collagen do the job they were built for; MUTO was built for a different one.")])

S["c4"]["settings"]["band"] = "mint"

# ---- 5: the experts, one heading, then the board ----
chapter("c5", "the-experts", "05", "The experts",
        "The scientists behind the formula.",
        intro=p("A supplement doesn’t need a scientist anywhere near it. Ours has seven. Our scientific advisory board meets every quarter to guide our research and every new formula."))
S["c5"]["settings"]["space_bottom"] = 40  # the board follows straight on
board = copy.deepcopy(ABOUT["board"])
board["settings"].update(heading="", note="", field=False, compact=True, rail_gap=40, space_top=0, space_bottom=48)  # the home page's slim cards
S["board"] = board; ORDER.append("board")
# The board band on the page's own ground colour, no mint wash
add("board_css", "custom-liquid", {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0,
                                   "custom_liquid": "<style>[id$=\"__board\"] .mh{background:var(--mc-ground,#f9f9f9)}[id$=\"__board_css\"]{display:none}#MainContent,[id$=\"__board\"]{background:var(--mc-ground,#f9f9f9)}</style>"})  # no white between sections
add("research", "muto-chapter", {"anchor": "our-research", "number": "", "label": "Our research (follows the board)", "heading": "",
                                 "line": p("<strong>Our research.</strong> Our first human study starts in December 2026 at the University of Westminster, with work at King’s College London, Coventry and Newcastle to follow. There are no results yet, and we’ll never say there are. We’ll publish them, whatever they show."),
                                 "small": p("Our advisory board guides our research and formulation. Its members don’t endorse products, and none of them is presented as recommending MUTO for any medical purpose."),
                                 "art": "none", "takeaway": "", "intro": "", "cta_label": "", "cta_link": "",
                                 "tint": False, "space_top": 0, "space_bottom": 96}, [])

# ---- 6: your 90 days, straight into the offer ----
STEPS = [("Day 1", "Your baseline", "Score your afternoons, sleep and recovery out of 10, or note your wearable’s numbers. It takes 30 seconds."),
         ("Day 30", "Afternoons that hold", "Usually the first thing people notice. Less of a 3pm slump, easier mornings, and energy left for the evening."),
         ("Day 60", "Bouncing back sooner", "A walk, a round of golf or a gym session stops hanging around for days. Busy weeks cost you less."),
         ("Day 90", "Feeling like yourself", "Compare your scores with day 1. Many people say they hadn’t realised how flat they’d been feeling.")]
chapter("c6", "your-90-days", "06", "Your 90 days",
        "Test it on yourself.",
        intro=p("What people tell us they notice, and roughly when. Everyone’s different, so score yourself on day 1 and compare."),
        blocks=[(f"s{i}", {"type": "step", "settings": {"kicker": k, "title": t, "text": p(x)}}) for i, (k, t, x) in enumerate(STEPS, 1)],
        line=p("If you don’t feel the difference in 90 days, you get every subscription payment back. Skip, pause or cancel online anytime."))
S["c6"]["settings"].update(band="mint", space_bottom=96)

# Offer and reviews, the same sections as the standards page
STD = json.load(open(os.path.join(HERE, "..", "standards-page", "templates", "page.standards.json")))["sections"]
S["start"] = copy.deepcopy(STD["start"]); ORDER.append("start")
S["start"]["settings"]["space_top"] = 0  # straight on from the mint timeline
S["reviews"] = copy.deepcopy(STD["reviews"]); ORDER.append("reviews")

out = os.path.join(HERE, "templates", "page.science-simple.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
