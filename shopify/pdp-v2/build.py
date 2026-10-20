"""New product page: builds templates/product.muto-nad-v2.json.

Starts from the 40-60 buy box (../pdp-45/age-4060/product.muto-nad-45.json, the draft's
product.muto-nad-4060) and lays out, top to bottom:

  buy        muto-pdp-buy: the buy box, with a delivery line, a guarantee panel, the test
             results button and the doctors block under the button; accordions rewritten
  benefits   muto-benefit-cards: the five jobs as photo cards (AG1 style)
  reviews    REVIEWS.io widget, as on the current product page
  board      the home page's slim scientific board
  library    muto-ingredient-library: the 19 ingredients, filterable (h2 here)
  compare    muto-chapter: MUTO vs the usual, the science page's table
  howto      muto-chapter: three steps
  faq        muto-crea-faq: rewritten
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
buy["settings"]["text"] = buy["settings"]["text"].replace('href="#whats-inside"', 'href="#test-results-3"')

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
EXTRAS = [
    ("x_delivery", {"type": "delivery", "settings": {"text": "Free <strong>next-day delivery</strong> in the UK"}}),
    ("x_promise", {"type": "promise", "settings": {"title": "No-risk 90-day guarantee",
                                                    "text": "Feel the difference in 90 days, or get every subscription payment back. Skip, pause or cancel online anytime."}}),
    ("x_tests", {"type": "tests", "settings": {"label": "View third-party testing results"}}),
    ("x_doctors", {"type": "doctors", "settings": {**{f"face_{i}": f for i, f in enumerate(faces, 1) if f},
                                                   "title": "Formulated with leading doctors and scientists",
                                                   "text": "Meet our scientific advisory board",
                                                   "link": "#scientific-board"}}),
]
for k, b in EXTRAS:
    buy["blocks"][k] = b
    buy["block_order"].append(k)
assert len(buy["block_order"]) <= 50, len(buy["block_order"])
put("buy", buy)

# ---- Benefit cards ----
CARDS = [
    ("Energy", "Vitamins B6 and B12 help reduce tiredness and fatigue, and help your body release energy from food.", "shopify://shop_images/nad-step-baseline.jpg"),
    ("Recovery", "Vitamin D supports normal muscle function, and riboflavin helps reduce tiredness after a long day.", "shopify://shop_images/nad-guarantee-runner.jpg"),
    ("Stress", "B vitamins support normal psychological function, and B5 supports mental performance through a demanding week.", "shopify://shop_images/MUTO0296.png"),
    ("Longevity", "300mg NR, which your body turns into NAD+. Zinc helps protect your cells from oxidative stress.", "shopify://shop_images/MUTO0266.png"),
    ("Immunity", "Vitamin D3, zinc, copper, folate, B6 and B12 all support the normal function of your immune system.", "shopify://shop_images/nad-jar.jpg"),
]
put("benefits", {"type": "muto-benefit-cards", "settings": {
    "heading": "Five jobs.\nOne daily jar.",
    "lede": "19 nutrients in two capsules, built for what your body needs after 35. So you can keep up with work, family and everything else.",
    "button_label": "View supplement facts", "button_link": "", "button_tab": "3",
    "space_top": 96, "space_bottom": 96},
    "blocks": {f"b{i}": {"type": "card", "settings": {"image": img, "title": t, "text": x}} for i, (t, x, img) in enumerate(CARDS, 1)},
    "block_order": [f"b{i}" for i in range(1, len(CARDS) + 1)]})

# ---- Reviews, below the fold ----
put("reviews", copy.deepcopy(BASE["custom_reviews_KpXTpD"]))

# ---- Slim scientific board, with the anchor the doctors block links to ----
put("board_anchor", {"type": "custom-liquid", "settings": {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid":
    "<style>[id$=\"__board_anchor\"]{height:0;overflow:hidden;margin:0!important;padding:0!important}[id$=\"__board\"] .mh{background:var(--mc-ground,#f9f9f9)}</style>"
    "<span id=\"scientific-board\" style=\"display:block;position:relative;top:-80px\"></span>"}})
board["settings"].update(heading="Meet our\nscientific board.", note="Our Scientific Advisory Board", field=False, compact=True,
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

# ---- How to take it: three steps ----
STEPS = [("Step 1", "Two capsules with breakfast", "CoQ10, vitamin D3 and K2 dissolve in fat, so your body takes them in best with food."),
         ("Step 2", "Every morning", "It works best as a daily habit. Keep the jar by the kettle so you don’t forget."),
         ("Step 3", "Check in at day 30 and 90", "Score your energy and sleep out of 10 on day 1, then compare. Not for you after 90 days? Get every subscription payment back.")]
put("howto", {"type": "muto-chapter", "settings": {
    "anchor": "how-to-take-it", "number": "", "label": "How to take it", "heading": "How to take it.",
    "intro": p("Three steps. Two capsules. About ten seconds a day."), "art": "none", "takeaway": "", "line": "", "small": "",
    "cta_label": "", "cta_link": "", "tint": False, "band": "ground", "space_top": 96, "space_bottom": 96},
    "blocks": {f"s{i}": {"type": "step", "settings": {"kicker": k, "title": t, "text": p(x)}} for i, (k, t, x) in enumerate(STEPS, 1)},
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

# ---- The test results panel, opened from the buy box, the cards and the FAQ ----
put("tests", copy.deepcopy(ING_T["tests"]))

put("sticky", copy.deepcopy(BASE["sticky"]))
put("easy_read", copy.deepcopy(BASE["easy_read"]))

out = os.path.join(HERE, "templates", "product.muto-nad-v2.json")
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections;", len(buy["block_order"]), "buy blocks")
