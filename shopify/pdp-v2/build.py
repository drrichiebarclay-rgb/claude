"""New product page: builds templates/product.muto-nad-v2.json.

Starts from the 40-60 buy box (../pdp-45/age-4060/product.muto-nad-45.json, the draft's
product.muto-nad-4060) and lays out, top to bottom:

  buy        muto-pdp-buy: the buy box, with a delivery line, a guarantee panel, the test
             results button and the doctors block under the button; accordions rewritten
  nav        muto-section-nav: chips for the sections below, pinned once scrolled to
  benefits   muto-benefit-cards: the five jobs as photo cards (AG1 style)
  board      the home page's slim scientific board
  library    muto-ingredient-library: the 19 ingredients, filterable (h2 here)
  compare    muto-chapter: MUTO vs the usual, the science page's table
  timeline   muto-timeline: what to expect at day 1, 30, 60 and 90
  howto      muto-chapter: three steps
  faq        muto-crea-faq: rewritten
  reviews    REVIEWS.io widget, as on the current product page
  tests      muto-test-results: the panel the button opens (nothing shows until opened)
  sticky, easy_read  as on the current product page

Copy for ingredients and tests comes from ../ingredients-page (ingredients.json,
test-results.json and its built template), the comparison from ../science-page.
Usage: python3 build.py
"""
import copy, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SH = os.path.dirname(HERE)


def load(path):
    return json.loads(re.sub(r"^/\*.*?\*/", "", open(os.path.join(SH, path)).read(), flags=re.S))


BASE = load("pdp-45/age-4060/product.muto-nad-45.json")["sections"]
ING_T = load("ingredients-page/templates/page.ingredients.json")["sections"]
SCI_T = load("science-page/templates/page.science-simple.json")["sections"]
STD_T = load("standards-page/templates/page.standards.json")["sections"]
TR = load("ingredients-page/test-results.json")
S, ORDER = {}, []


def put(key, sec):
    S[key] = sec
    ORDER.append(key)


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


def ul(*items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


MAIL = '<a href="mailto:hello@mutolongevity.com">hello@mutolongevity.com</a>'

# ---- Buy box ----
buy = copy.deepcopy(BASE["buy"])
buy["type"] = "muto-pdp-buy"
buy["settings"]["text"] = p("<strong>Not another multivitamin. The next generation of one.</strong>",
                            "The active vitamins and minerals you’d want from a good multivitamin, plus the cellular science most leave out: NR for NAD⁺, CoQ10, PQQ and resveratrol. 19 ingredients, every dose on the label, two capsules, one jar.",
                            '<a href="#test-results-3">Ingredients + nutritional information</a>')
# "How it helps": the five jobs, each a title over its line; * refers to the authorised claims in the small print
POINTS = [("Energy", "Afternoons that don’t fade"), ("Recovery", "Bounce back from a busy week"), ("Mind", "A clearer head, all day"),
          ("Ageing well", "Age on your own terms"), ("Immunity", "Stay well through winter"), ("Simplicity", "One jar replaces five")]  # job, then what you feel
old = [k for k in buy["block_order"] if buy["blocks"][k]["type"] == "point"]
at = buy["block_order"].index(old[0])
for k in old:
    del buy["blocks"][k]
    buy["block_order"].remove(k)
for i, (lab, x) in enumerate(POINTS, 1):
    buy["blocks"][f"job{i}"] = {"type": "point", "settings": {"label": lab, "title": x, "text": "", "icon": "", "dark": False}}
    buy["block_order"].insert(at + i - 1, f"job{i}")
buy["settings"]["points_foot"] = ""  # the line and the small print under the cards were removed
buy["settings"]["points_note"] = ""

def form(n, f):
    """The form, when it says more than the name: 'methylcobalamin' yes, 'trimethylglycine' for TMG no."""
    if not f or f.lower() in n.lower():
        return ""
    f = re.sub(r"\s*\(([^)]*)\)", r", \1", f)  # no brackets inside brackets
    return f" · {f[0].lower() + f[1:] if f[1:2].islower() else f}"


FORMULA = ul(*[f"<strong>{n}</strong> {a}{form(n, f)}" for g, n, f, a in TR["formula"]])
FOLDS = [
    ("Who it’s for", p("<strong>Made for adults in their 40s, 50s and 60s.</strong> Most of our customers are in their 40s and 50s. You don’t need to be sporty or own a smartwatch.",
                       "It’s for you if afternoons feel harder than they used to, you get less back from the same effort, or you want to keep up with work, family and the things you love.")),
    ("What it does", p("Five jobs in one daily formula:") + ul(
        "<strong>Energy.</strong> Vitamins B6 and B12 contribute to the reduction of tiredness and fatigue.",
        "<strong>Recovery.</strong> Vitamin D contributes to normal muscle function.",
        "<strong>Stress.</strong> B vitamins contribute to normal psychological function, and B5 to normal mental performance.",
        "<strong>Longevity.</strong> 300mg NR, which your body turns into NAD+, plus zinc, which contributes to the protection of cells from oxidative stress.",
        "<strong>Immunity.</strong> Vitamin D, zinc, copper, folate, B6 and B12 contribute to the normal function of the immune system.")
     + p("One jar instead of five pots: no separate NAD+, CoQ10, resveratrol, D3 + K2 or B-complex.")),
    ("What’s inside", p("19 ingredients in two capsules. Every dose is on the label, per two-capsule serving:") + FORMULA
     + p('Filter them by job on our <a href="/pages/ingredients">ingredients page</a>.')),
    ("How to take it", p("Two capsules every morning with breakfast.",
                         "<strong>Why with food?</strong> CoQ10, vitamin D3 and K2 dissolve in fat, so your body takes them in best with a meal.",
                         "<strong>Why every day?</strong> It works best as a habit. Keep the jar by the kettle.")),
    ("Quality and testing", ul("Every dose on the label, no proprietary blends",
                               "Only UK-authorised ingredients: that’s why we use NR, not NMN",
                               "Made in the UK to GMP standards",
                               "Every batch tested before release for heavy metals, microbes and capsule quality",
                               "Vegan capsules from plant cellulose, vitamin D3 from algae, no major allergens")
     + p('<a href="#test-results">See the results for the current batch</a>')),
    ("Delivery, skipping and cancelling", p("Free next-day delivery in the UK. A new jar arrives every 4 weeks, with gifts on your orders.",
                                            "Skip, pause or cancel online anytime. No phone calls, and we remind you five days before every payment.")),
    ("90-day money-back promise", p("Take it every day for 90 days. If you don’t feel the difference, email " + MAIL + " and you get every subscription payment back.")),
]
folds = [k for k in buy["block_order"] if buy["blocks"][k]["type"] == "fold"]
first = buy["block_order"].index(folds[0])
for k in folds:
    del buy["blocks"][k]
    buy["block_order"].remove(k)
for i, (t, x) in enumerate(FOLDS, 1):
    buy["blocks"][f"fold{i}"] = {"type": "fold", "settings": {"title": t, "text": x}}
    buy["block_order"].insert(first + i - 1, f"fold{i}")

board = copy.deepcopy(BASE["board"])
faces = [board["blocks"][m]["settings"].get("image") for m in board["block_order"]][:4]
# The trust pills above the plans go (one is kept, hidden, because "Choose your plan" hangs off their
# list); their points move under the button as badges, AgeMate style
for k in ("tr2", "tr3"):
    del buy["blocks"][k]
    buy["block_order"].remove(k)
EXTRAS = [
    ("x_delivery", {"type": "delivery", "settings": {"text": "Free <strong>next-day delivery</strong> in the UK"}}),
    ("x_badges", {"type": "badges", "settings": {"mark_1": "UK", "label_1": "Made in the UK", "mark_2": "GMP",
                                                  "label_2": "Made to GMP standards", "mark_3": "shield", "label_3": "Every batch tested"}}),
    ("x_promise", {"type": "promise", "settings": {"title": "No-risk 90-day guarantee",
                                                    "text": "Feel the difference in 90 days, or get every subscription payment back. Skip, pause or cancel online anytime."}}),
    ("x_tests", {"type": "tests", "settings": {"label": "View third-party testing results"}}),
    ("x_doctors", {"type": "doctors", "settings": {**{f"face_{i}": f for i, f in enumerate(faces, 1) if f},
                                                   "title": "Formulated with leading doctors and scientists",
                                                   "text": "Meet our scientific advisory board",
                                                   "link": "#scientific-board"}}),
]
EXTRAS.append(("x_lists", {"type": "lists", "settings": {
    "title_1": "Free from", "items_1": "Proprietary blends\nFillers\nCaffeine and stimulants\nMajor allergens",
    "title_2": "Made with", "items_2": "Vegan capsules\nVitamin D3 from algae\nActive B vitamins\nBisglycinate minerals"}}))
for k, b in EXTRAS:
    buy["blocks"][k] = b
    buy["block_order"].append(k)
assert len(buy["block_order"]) <= 50, len(buy["block_order"])
put("buy", buy)

# ---- Section links: pinned chips for the sections below, as on the science page ----
NAV = [("Benefits", "benefits"), ("The experts", "board"), ("Ingredients", "library"), ("Comparison", "compare"),
       ("What to expect", "timeline"), ("How to take it", "howto"), ("FAQs", "faq"), ("Reviews", "reviews")]
put("nav", {"type": "muto-section-nav", "settings": {"label": "On this page", "nav_top": 0},
            "blocks": {f"n{i}": {"type": "link", "settings": {"label": l, "target": t}} for i, (l, t) in enumerate(NAV, 1)},
            "block_order": [f"n{i}" for i in range(1, len(NAV) + 1)]})

# ---- Benefit cards ----
JOBLINES = load("ingredients-page/jobs.json")  # the same lines as the science page, from the ingredients page statements
PHOTOS = {"Energy": "shopify://shop_images/nad-step-baseline.jpg", "Recovery": "shopify://shop_images/nad-guarantee-runner.jpg",
          "Stress": "shopify://shop_images/MUTO0296.png", "Longevity": "shopify://shop_images/MUTO0266.png", "Immunity": "shopify://shop_images/nad-jar.jpg"}
CARDS = [(j, JOBLINES[j], PHOTOS[j]) for j in ("Energy", "Recovery", "Stress", "Longevity", "Immunity")]
put("benefits", {"type": "muto-benefit-cards", "settings": {
    "heading": "Five jobs.\nOne daily jar.",
    "lede": "19 nutrients in two capsules, built for what your body needs after 35. So you can keep up with work, family and everything else.",
    "button_label": "View supplement facts", "button_link": "", "button_tab": "3",
    "space_top": 96, "space_bottom": 96},
    "blocks": {f"b{i}": {"type": "card", "settings": {"image": img, "title": t, "text": x}} for i, (t, x, img) in enumerate(CARDS, 1)},
    "block_order": [f"b{i}" for i in range(1, len(CARDS) + 1)]})


# ---- Slim scientific board, with the anchor the doctors block links to ----
put("board_anchor", {"type": "custom-liquid", "settings": {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid":
    "<style>[id$=\"__board_anchor\"]{height:0;overflow:hidden;margin:0!important;padding:0!important}[id$=\"__board\"] .mh{background:var(--mc-ground,#f9f9f9)}</style>"
    "<span id=\"scientific-board\" style=\"display:block;position:relative;top:-80px\"></span>"}})
board["settings"].update(heading="Meet the experts\nbehind MUTO.", note="Our Scientific Advisory Board", field=False, compact=True,
                         rail_gap=40, space_top=72, space_bottom=72)
put("board", board)

# ---- Ingredients ----
lib = copy.deepcopy(ING_T["library"])
for k in [k for k in lib["block_order"] if lib["blocks"][k]["type"] == "category"]:
    del lib["blocks"][k]
    lib["block_order"].remove(k)
lib["settings"].update(heading_tag="h2", tests_label="", heading="Every ingredient has a job.",
                       lede="19 ingredients, every dose on the label. Filter by what they support, and tap one to see why it’s there.",
                       pad_top=96, pad_bottom=96)
put("library", lib)

# ---- MUTO vs the usual ----
cmp_ = copy.deepcopy(SCI_T["c4"])
cmp_["settings"].update(anchor="compare", number="", band="mint", space_top=96, space_bottom=96)
put("compare", cmp_)

# ---- What to expect over time (the science page's timeline, AgeMate's layout) ----
TL = load("pdp-v2/timeline.json")  # shared with the science page
MILES = [(x["pill"], x["title"], x["text"]) for x in TL["milestones"]]
put("timeline", {"type": "muto-timeline", "settings": {
    "heading": TL["heading"], "lede": TL["lede"],
    "image": "shopify://shop_images/MUTO0296.png", "image_alt": "",
    "foot": TL["foot"],
    "band": "ground", "sticky_top": 120, "space_top": 96, "space_bottom": 96},
    "blocks": {f"m{i}": {"type": "milestone", "settings": {"pill": d, "title": t, "text": p(x)}} for i, (d, t, x) in enumerate(MILES, 1)},
    "block_order": [f"m{i}" for i in range(1, len(MILES) + 1)]})

# ---- How to take it: three steps ----
STEPS = [("Step 1", "Two capsules with breakfast", "CoQ10, vitamin D3 and K2 dissolve in fat, so your body takes them in best with food.", "shopify://shop_images/nad-jar.jpg"),
         ("Step 2", "Every morning", "It works best as a daily habit. Keep the jar by the kettle so you don’t forget.", "shopify://shop_images/MUTO0266.png"),
         ("Step 3", "Check in at day 30 and 90", "Score your energy and sleep out of 10 on day 1, then compare. Not for you after 90 days? Get every subscription payment back.",
          "shopify://shop_images/1BBE18C7-9CBA-4EA3-BB3F-60C13D1F4F19.png")]
put("howto", {"type": "muto-chapter", "settings": {
    "anchor": "how-to-take-it", "number": "", "label": "How to take it", "heading": "How to take it.",
    "intro": p("Three steps. Two capsules. About ten seconds a day."), "art": "none", "takeaway": "", "line": "", "small": "",
    "cta_label": "", "cta_link": "", "tint": False, "band": "mint", "space_top": 96, "space_bottom": 96},
    "blocks": {f"s{i}": {"type": "step", "settings": {"image": img, "kicker": k, "title": t, "text": p(x)}} for i, (k, t, x, img) in enumerate(STEPS, 1)},
    "block_order": [f"s{i}" for i in range(1, len(STEPS) + 1)]})

# ---- FAQs ----
faq = copy.deepcopy(BASE["faq"])
QS = [
    ("Who is MUTO for?", p("Adults over 35. Most of our customers are in their 40s and 50s. You don’t need to be sporty or own a smartwatch.")),
    ("What is NAD+, and why does it matter?", p("NAD+ is a molecule every cell uses to turn food into energy. Your body makes less of it from your mid-30s. MUTO gives you 300mg of NR, a form of vitamin B3 your body turns into NAD+.")),
    ("Why NR and not NMN?", p("NR is authorised for food supplements in the UK. NMN is still under assessment, so we don’t use it. 300mg of NR is the most allowed in Great Britain.")),
    ("When will I notice something?", p("Give it 60 to 90 days. Many people notice their afternoons first, sometimes within a few weeks. For others it takes longer.")),
    ("How do I know it’s working?", p("Before you start, score your energy, sleep and recovery out of 10. Do it again at day 30 and day 90, then compare. A pen and paper is fine.")),
    ("Is it safe with my other medication?", p("Usually, yes. Coffee is fine too. If you take medicine, ask your doctor first, especially if you take a blood thinner like warfarin.")),
    ("Is it vegan?", p("Yes. The capsules are plant cellulose, vitamin D3 comes from algae, and there are no major allergens, fillers, caffeine or stimulants.")),
    ("How is it tested?", p('Every batch is tested before release for heavy metals, microbes and capsule quality. <a href="#test-results">See the results for the current batch</a>.')),
    ("Can I skip, pause or cancel?", p("Yes, online, anytime. No phone calls. We send a reminder five days before every payment.")),
    ("What if it’s not for me?", p(f"Take it every day for 90 days. If you don’t feel the difference, email {MAIL} and you get every subscription payment back.")),
]
faq["blocks"] = {f"q{i}": {"type": "q", "settings": {"title": t, "text": x}} for i, (t, x) in enumerate(QS, 1)}
faq["block_order"] = [f"q{i}" for i in range(1, len(QS) + 1)]
put("faq", faq)

# ---- Reviews, at the bottom ----
put("reviews", copy.deepcopy(BASE["custom_reviews_KpXTpD"]))

# ---- The test results panel, opened from the buy box, the cards and the FAQ ----
put("tests", copy.deepcopy(ING_T["tests"]))

put("sticky", copy.deepcopy(BASE["sticky"]))
er = copy.deepcopy(BASE["easy_read"])
er["settings"]["custom_liquid"] = er["settings"]["custom_liquid"].replace("</style>", "\n/* New PDP: plain #fafafa behind the buy box, no gradient */\nhtml body .mc.mc--buy,html body .mc.mc--buy.mc--fit-nad{background:#fafafa!important}\n/* New PDP: the pills moved under the button as badges; only the heading stays */\nhtml body .mc .mc__trust li{display:none}\nhtml body .mc .mc__trust::after{margin-top:8px}\n</style>", 1)
put("easy_read", er)

# Photos picked in the theme editor (21 Oct), kept on rebuild
EDITOR_IMAGES = {("benefits", "b1"): "Golden_Hour_Family_Beach_Walk.png", ("benefits", "b2"): "038A80BF-8A59-420A-8CC3-3C5DDFB275B6.png",
                 ("benefits", "b3"): "3E3756BE-4955-4D85-81D7-30B61D5035B0.png", ("benefits", "b4"): "Golden_Hour_Ocean_Portrait.png",
                 ("benefits", "b5"): "D9D67CEB-ADD5-421D-97BD-39141E88C5E9.png",
                 ("howto", "s1"): "nad-take-two.jpg", ("howto", "s2"): "Coffee_MUTO.jpg", ("howto", "s3"): "D2AA08A2-83BB-4249-AC48-A8261A413D04.png"}
for (sec, blk), f in EDITOR_IMAGES.items():
    S[sec]["blocks"][blk]["settings"]["image"] = "shopify://shop_images/" + f
S["timeline"]["settings"]["image"] = "shopify://shop_images/B41838FF-C1C0-41C3-AF29-AE2348CE86A8.png"

out = os.path.join(HERE, "templates", "product.muto-nad-v2.json")
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections;", len(buy["block_order"]), "buy blocks")
