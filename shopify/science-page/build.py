"""Science page: builds templates/page.science-simple.json from
MUTO_Science_Page_Copy_Oct26.docx, in the same styles as the standards page.

  muto-science-hero  eyebrow, headline, subhead, byline and pinned chapter links (new section)
  muto-chapter       one per chapter: pinned number on the left, content on the right (new section)
  muto-home-board    the scientific board rail, as on the About page, under chapter 6

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
    ("the-science", "The science behind it"),
    ("how-muto-is-built", "How MUTO is built for it"),
    ("muto-vs-the-usual", "MUTO vs the usual"),
    ("the-experts", "Meet the experts"),
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

# ---- 1 ----
chapter("c1", "what-changes", "01", "What changes after 35",
        "Somewhere after 35, your body starts working a little differently.",
        intro=p("Nothing dramatic happens overnight. But three quiet shifts start inside your cells, and they build through your 40s and 50s."),
        art="decline",
        blocks=[point("a", "You make less NAD+", "A molecule every cell needs to turn food into energy."),
                point("b", "You get less back", "From the same food and the same training."),
                point("c", "Your cells’ maintenance slows", "While the wear and tear of making energy carries on.")],
        takeaway="It’s not you doing anything wrong. It’s biology. And what your body needs changes with it.")

# ---- 2 ----
QUOTES = ["Sharp at 8am. Gone by 3pm.", "The same training just doesn’t land like it used to.",
          "Hard sessions hang around for days.", "I spend Saturdays recovering from the week.",
          "There’s nothing left for the people at home.", "I’m doing everything right, and I still feel it."]
chapter("c2", "how-it-shows-up", "02", "How it shows up",
        "You don’t feel your cells. You feel your day.",
        intro=p("This is what people in their late 30s, 40s and 50s tell us, again and again:"),
        art="battery",
        blocks=[(f"q{i}", {"type": "quote", "settings": {"text": q}}) for i, q in enumerate(QUOTES, 1)],
        line=p("It’s like your body has switched to low power mode. Still working, still getting through the day, but running on less than it used to."),
        tint=True)

# ---- 3 ----
chapter("c3", "the-science", "03", "The science behind it",
        "What’s actually happening inside you.",
        blocks=[point("a", "30 trillion tiny factories", "Every cell makes its own energy, in tiny power stations called mitochondria."),
                point("b", "Fewer couriers", "To make that energy, cells use NAD+ as a courier: it picks up energy from your food and carries it to the power station, over and over, all day. From your mid-30s, your body makes less NAD+. Fewer couriers, the same amount of work."),
                point("c", "Less back from the same input", "As we age, our bodies respond less to the same food and the same training. It’s called anabolic resistance, and it’s what I spent years studying in the lab. Same effort, smaller return."),
                point("d", "More wear, slower maintenance", "Making energy creates a little “exhaust”. Your cells have crews that clean it up and keep everything maintained, and some of those crews, a family of enzymes called sirtuins, also use NAD+ every time they work. Fewer couriers means more competition for the same supply.")],
        takeaway="Three shifts, one root: what your cells need changes, and the basics you took at 30 weren’t built for it.")

# ---- 4 ----
JOBS = [("Job", "What’s in it", "In plain words"),
        ("1. Energy", "B vitamins (B6, B12, folate), in their active forms", "Help you feel less tired"),
        ("2. Muscles and bones", "Vitamin D3 2,000 IU + K2 100µg", "Keep your muscles working and your bones strong"),
        ("3. Immunity", "Zinc 15mg + copper 1mg, with D3", "Support your immune system"),
        ("4. NAD+", "NR 300mg, the most allowed in Great Britain", "Your body turns it into NAD+: more couriers"),
        ("5. What ties it together", "CoQ10, resveratrol, grape seed extract, PQQ, TMG", "The supporting cast, every dose on the label")]
TEAMS = [("Team", "Who’s on it", "What happens"),
         ("The energy team", "NR, CoQ10, copper", "NR becomes NAD+, the courier. CoQ10 is the relay runner that passes energy along inside the power station. Copper sits at the very last step, where the energy gets made."),
         ("The recycling team", "Folate, B12, B6, TMG", "Your cells constantly reuse one of their most important building blocks. Folate and B12 keep that recycling loop turning, TMG runs a second loop alongside it, and B6 handles the exit. We use the active forms, the ones the cell actually uses."),
         ("The clean-up crew", "Zinc + copper", "Zinc and copper build the enzyme that cleans up the exhaust from making energy. One enzyme, two metals, so we pair them."),
         ("The bone relay", "D3 + K2", "D3 tells your cells to make a bone protein. K2 switches that protein on. D3 makes it, K2 activates it.")]
chapter("c4", "how-muto-is-built", "04", "How MUTO is built for it",
        "The foundation your body runs on. Five jobs, one jar.",
        intro=p("MUTO is built for what you actually need after 35: one daily formula covering five jobs, so you’re not guessing across five separate pots."),
        blocks=[table("t1", "The five jobs", JOBS), table("t2", "How the 19 ingredients work together", TEAMS)],
        line=p("<strong>Two capsules with breakfast. Every dose on the label.</strong> Alongside our creatine, it’s all you need to keep up."),
        cta_label="See every ingredient", cta_link="/pages/ingredients",
        small=p("Vitamins B6 and B12 contribute to the reduction of tiredness and fatigue. Vitamin D contributes to normal muscle function. Vitamins D and K contribute to the maintenance of normal bones. Zinc, copper and vitamin D contribute to the normal function of the immune system. In a study of adults aged 40 to 60, 300mg of NR a day raised NAD+ by 51% in two weeks. That study tested NR on its own, not MUTO."),
        tint=True)

# ---- 5 ----
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
chapter("c5", "muto-vs-the-usual", "05", "MUTO vs the usual",
        "What you’ve been taking vs what you actually need.",
        intro=p("Most people in their 40s and 50s are taking some mix of these. Here’s how they compare."),
        blocks=[table("t1", "", VS, highlight=2,
                      note="Comparisons are by category, not brand, and products vary. Hold any label up against ours. Multivitamins, greens and collagen do the job they were built for; MUTO was built for a different one.")])

# ---- 6 ----
chapter("c6", "the-experts", "06", "Meet the experts",
        "The scientists behind the formula.",
        intro=p("A supplement doesn’t need a scientist anywhere near it. Ours has seven. Our scientific advisory board meets every quarter to guide our research and every new formula."),
        line=p("<strong>Our research.</strong> Our first human study starts in December 2026 at the University of Westminster, with work at King’s College London, Coventry and Newcastle to follow. There are no results yet, and we’ll never say there are. We’ll publish them, whatever they show."),
        small=p("Our advisory board guides our research and formulation. Its members don’t endorse products, and none of them is presented as recommending MUTO for any medical purpose."))
S["c6"]["settings"]["space_bottom"] = 40  # the board follows straight on
board = copy.deepcopy(ABOUT["board"])
board["settings"].update(heading="", note="", compact=True, rail_gap=40, space_top=0, space_bottom=96)  # the home page's slim cards
S["board"] = board; ORDER.append("board")

# ---- 7 ----
chapter("c7", "test-it", "07", "Test it yourself",
        "Test it on yourself.",
        blocks=[("s1", {"type": "step", "settings": {"title": "Today", "text": p("Score your afternoons out of 10, or note your wearable’s numbers.")}}),
                ("s2", {"type": "step", "settings": {"title": "Every day", "text": p("Two capsules with breakfast.")}}),
                ("s3", {"type": "step", "settings": {"title": "Days 30, 60 and 90", "text": p("Check in. Look at the trend, not single days.")}}),
                ("s4", {"type": "step", "settings": {"title": "Then", "text": p("Decide for yourself.")}})],
        line=p("If you don’t feel the difference in 90 days, you get every subscription payment back. Skip, pause or cancel online anytime."),
        cta_label="Start your 90 days", cta_link=PDP, tint=True)

# ---- Glossary ----
TERMS = [("Cell", "The tiny unit everything in your body is built from. You have about 30 trillion."),
         ("Mitochondria", "The power stations inside your cells, where energy is made."),
         ("NAD+", "A molecule every cell uses as a courier to carry energy from your food to the power station."),
         ("NR (nicotinamide riboside)", "A form of vitamin B3 that your body turns into NAD+."),
         ("Anabolic resistance", "When your body gets less back from the same food and training as you age."),
         ("CoQ10", "A molecule your body makes, which passes energy along inside the power station."),
         ("Methylated (active) forms", "Versions of B vitamins that are already in the form your cells use."),
         ("Sirtuins", "A family of maintenance enzymes that use NAD+ every time they work.")]
chapter("glossary", "the-words", "", "The words, explained", "The words, explained.",
        blocks=[(f"w{i}", {"type": "term", "settings": {"word": w, "meaning": m}}) for i, (w, m) in enumerate(TERMS, 1)],
        )

out = os.path.join(HERE, "templates", "page.science-simple.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
