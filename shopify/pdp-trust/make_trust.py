"""Trust bands + a slightly more clinical voice for the main NAD+ product page
(template product.muto-nad-45).

Built on the LIVE template snapshot (live-snapshot-28oct/), so edits made on live
are kept. Adds four new sections (theme/sections/muto-crea-*.liquid) and changes
copy only in the sections listed below; the buy box is not touched.

Usage (from shopify/pdp-trust/):  python3 make_trust.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "live-snapshot-28oct", "templates__product.muto-nad-45.json")
# The main product moved to template muto-nad-v2 on 27 Oct. Its buy box (section muto-pdp-v2-buy),
# the easy_read block that styles it (incl. the Black Friday box), the sticky bar, the
# #scientific-board anchor and the #test-results certificate panel are taken from it verbatim.
V2 = os.path.join(HERE, "live-snapshot-28oct", "templates__product.muto-nad-v2.json")
FROM_V2 = ["buy", "easy_read", "sticky", "board_anchor", "tests", "compare"]  # compare = "MUTO vs the usual"
OUT = os.path.join(HERE, "theme", "templates", "product.muto-nad-45.json")
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"

# --- New: statement ----------------------------------------------------------
STATEMENT = {"type": "muto-crea-statement", "settings": {
    "label": "",
    "heading": "Not ready to slow down.",
    "sub": "The next-generation multi-nutrient, built for what your body needs in your 40s and 50s.",
    "note": "Got a wearable? Track the shift over 90 days.",
    "space_top": 100, "space_bottom": 100}}

# --- New: standards ----------------------------------------------------------
STANDARDS_ITEMS = [
    ("tested", "Every batch", "Third-party tested",
     "<p>Every batch is tested by an independent lab for identity, potency, heavy metals and microbes before it’s released.</p>",
     # Set CERTS_URL to the page where the certificates are published.
     "View third-party testing results", "", "Certificates of analysis on request"),
    ("dose", "300mg NR", "Full, declared doses",
     "<p>Nicotinamide riboside at 300mg, the maximum daily amount authorised in Great Britain. All 19 ingredients are on the label with their doses. No proprietary blends.</p>",
     "", "", ""),
    ("board", "6 experts", "Scientific Advisory Board",
     "<p>Doctors and scientists in longevity, metabolism, sleep and performance nutrition review the formula.</p>",
     "", "", ""),
    ("made", "GMP · ISO", "Made in the UK",
     "<p>Manufactured in the UK to GMP standards, in an ISO-certified facility.</p>",
     "", "", ""),
]
CERTS_URL = "#test-results"  # opens the certificate-of-analysis panel (section muto-test-results)

def standards():
    blocks, order = {}, []
    for key, stat, title, text, link_label, link, note in STANDARDS_ITEMS:
        if key == "tested":
            link = CERTS_URL
        blocks[key] = {"type": "standard", "settings": {
            "stat": stat, "title": title, "text": text,
            "link_label": link_label, "link": link, "no_link_note": note}}
        order.append(key)
    return {"type": "muto-crea-standards", "blocks": blocks, "block_order": order, "settings": {
        "heading": "Checked, not\ntaken on trust.",
        "lede": "The four things we hold every jar to",
        "foot": "",
        "space_top": 100, "space_bottom": 100}}

# --- New: rotating reviews ---------------------------------------------------
# Real customer words only, copied from REVIEWS.io. Add up to 20; fill in ages
# (with the customer's OK) and set require_age to True once every card has one.
REVIEWS = [
    # topic (ours), quote (theirs: the whole review or one unbroken passage of it,
    # copied exactly from REVIEWS.io), name, age. All 5-star.
    ("Mid-30s", "Being in my mid 30s, everything has started to slow down. Muto is providing me with a sense of vitality which I haven’t experienced since my mid 20s", "Jonathon R", ""),
    ("Healthy ageing", "bought it to support healthy ageing and have been genuinely surprised at how quickly I felt a difference. My recovery and sleep have noticeably improved.", "K R", ""),
    ("Afternoon energy", "No afternoon slump and in general feeling great", "Lynda", ""),
    ("Feeling like yourself", "I didn't realise how flat I'd been feeling until this helped lift me out of it", "Holly P", ""),
    ("A month in", "I have been using for almost a month and can honestly say I have felt such a difference", "Michelle F", ""),
    ("From a sceptic", "I am usually sceptical to new supplements but this has been highly recommended by my friend so gave it a shot. It has exceeded my expectations, which is not easy as I am well-versed in nutrition and supplements.", "Aleks", ""),
    ("Sustained energy", "I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore.", "Danny S", ""),
    ("Tracked on Oura", "I track the effectiveness of my supplements using my Oura ring, and all my key biometrics are improving: recovery, sleep, HRV and RHR", "Hugh K", ""),
    ("Mornings", "I predominantly struggle with mornings but already feel myself finding these easier", "Becca", ""),
    ("Recovery", "Has actually changed my recovery", "Adam H", ""),
    ("All-day energy", "The cellular energy boost it gives you really enables me to power through my day.", "Max", ""),
    ("Energy and sleep", "Since starting taking Muto my energy levels and my sleep has improved drastically (even within the first month)", "Matteo M", ""),
    ("Fewer pots", "I love that this replaces multiple products", "Amy C", ""),
    ("Keeping up", "Started using muto because I felt like my body couldn’t keep up with the amount of exercise I wanted to do. After taking muto, I felt more energised and ready for my next session!", "Brendan", ""),
    ("Marathon training", "I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint", "Rebeca", ""),
    ("Training more often", "As a keen runner, I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often.", "Ayo P", ""),
    ("Focus", "I’ve been taking MUTO every day for just under 2 months now and definitely feel more focused during the day", "Alexandra", ""),
    ("Consistent energy", "Energy is up and staying consistent.", "Jack", ""),
    ("Clearer mind", "I feel like I have more energy and a clearer mind.", "Sam", ""),
    ("A scientist who picks up the phone", "Richie from the team gave me a call just to chat about my background and goals", "Mathew H", ""),
]

def reviews():
    blocks, order = {}, []
    for i, (topic, quote, name, age) in enumerate(REVIEWS, 1):
        k = f"rv{i}"
        blocks[k] = {"type": "review", "settings": {
            "topic": topic, "quote": quote, "name": name, "age": age, "verified": True}}
        order.append(k)
    return {"type": "muto-crea-reviews", "blocks": blocks, "block_order": order, "settings": {
        "eyebrow": "Verified customers",
        "heading": "What our\ncommunity say.",
        "summary": "4.8 from 103 reviews",  # REVIEWS.io, 28 Oct 2026 (4.83 average): update as it moves
        "interval": 6, "min_age": 30, "require_age": False,
        "foot": "Real reviews from verified customers, in their own words. Everyone is different.",
        "space_top": 100, "space_bottom": 100}}

# --- New: founder ------------------------------------------------------------
FOUNDER = {"type": "muto-crea-founder",
    "blocks": {},
    "block_order": [],
    "settings": {
        "eyebrow": "Our founder",
        "heading": "Built by a doctor\nwho wanted proof.",
        "text": "<p>Richie Barclay is a cell biologist with a PhD in cellular biology and nutrition, a Harley Street nutritionist for the last 13 years, and a former cricketer.</p>"
                "<p>He started MUTO after years of watching supplements sell on claims nobody had checked, with the doses hidden in blends. "
                "So MUTO does it the other way: every dose is on the label, every batch goes to an outside lab, "
                "and six doctors and scientists review the formula.</p>",
        "quote": "I built MUTO because I was tired of supplements that ask you to take them on trust.",
        "quote_by": "Dr Richie Barclay, PhD, founder",
        "link_label": "Got a question? Email Richie",
        "link": "mailto:hello@mutolongevity.com",
        "image": "shopify://shop_images/about-founder.jpg",
        "image_fallback": CDN + "about-founder.jpg?v=1790751995",
        "image_alt": "Dr Richie Barclay holding a jar of NAD+ Cellular Complex",
        "image_position": "50% 20%",
        "caption": "",
        "space_top": 100, "space_bottom": 100}}

# --- Page backgrounds: no gradient washes, alternating flat grey and white ---
GREY, WHITE = "#f2f2f2", "#ffffff"
BANDS = [  # section key -> ground, in page order. The buy box keeps the live page's own
           # plain #fafafa, and "compare" keeps its live sage (#c8d2cf) band, so neither is listed.
    ("statement", WHITE),
    ("board", WHITE),
    ("standards", WHITE),
    ("results", GREY),
    ("quotes", WHITE),
    ("founder", GREY),
    ("problem", WHITE),
    ("benefits", GREY),
    ("steps", WHITE),
    ("guarantee", GREY),
    ("faq", GREY),
]

def bands_css():
    """A template-only style block. Each section is matched by the end of its
    Shopify wrapper id (shopify-section-template--…__<key>), so it reaches only
    this page and only these sections. !important because the washes are set on
    the bands' own root classes in muto-crea.css / muto-home.css."""
    rules = []
    for key, ground in BANDS:
        w = f'[id$="__{key}"]'
        rules.append(f"{w},{w} > .mc,{w} > .mh{{background:{ground}!important}}")
    css = "\n".join(rules)
    return {"type": "custom-liquid", "settings": {
        "custom_liquid": "<style>\n/* Flat, alternating band grounds for this page (no gradient washes). Built by make_trust.py. */\n"
                         + css + "\n</style>",
        "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}


# --- Existing sections: a slightly more clinical voice ----------------------
def clinical(d):
    S = d["sections"]

    r = S["results"]["settings"]           # the 9:16 customer videos
    r["heading"] = "Don’t take\nour word for it."
    r["note"] = "MUTO customers, in their own words"
    r["foot"] = "Individual experiences. Everyone is different, and we can’t promise results."
    S["results"]["settings"]["space_top"] = 70   # sits under the standards band, which brings its own space

    b = S["board"]["settings"]
    b["heading"] = "Six scientists put\ntheir name to MUTO."
    b["note"] = "Our Scientific Advisory Board reviews the formula"
    b["field"] = False        # plain #FAFAFA ground, no mint wash
    b["compact"] = True       # the thin one-row strip: all six across on desktop, small swipeable cards on phones
    b["space_top"] = 60       # sits straight under the statement band

    st = S["steps"]
    st["settings"]["heading"] = "Your first 90 days."
    st["settings"]["heading_right"] = "What to expect."
    # Benefits follow the live timeline (muto-nad-v2) and stay within authorised claims
    # (B vitamins: tiredness and fatigue; vitamin D: normal muscle function).
    steps = [
        ("Day 1", "Set your baseline.",
         "Two capsules with breakfast. Score your energy, sleep and recovery out of 10, or note your wearable’s numbers."),
        ("Day 30", "Afternoons that hold.",
         "Usually the first thing people notice: less of a 3pm slump, energy left for the evening. B vitamins help reduce tiredness and fatigue."),
        ("Day 60", "Bouncing back sooner.",
         "Vitamin D supports normal muscle function. A long walk, a game of tennis or a gym session stops costing you the next day."),
        ("Day 90", "Feel it, or your money back.",
         "Compare your scores with day 1. Not feeling the difference? Email us and we’ll refund what you paid, minus delivery."),
    ]
    for k, (chip, title, text) in zip(st["block_order"], steps):
        st["blocks"][k]["settings"].update({"chip": chip, "title": title, "text": text})

    f = S["faq"]
    for blk in f["blocks"].values():
        s = blk["settings"]
        if s["title"] == "Why not just take one vitamin?":
            s["text"] = ("<p>You can. MUTO puts 19 ingredients, each at a declared dose, into 2 capsules: "
                         "300mg NR plus the B vitamins, TMG, CoQ10 and PQQ that work alongside it. One jar instead of several pots.</p>")
    f["blocks"]["q_tested"] = {"type": "q", "settings": {
        "title": "How is it tested?",
        "text": "<p>Every batch is tested by an independent lab for identity, potency, heavy metals and microbes before it’s released. "
                "MUTO is made in the UK to GMP standards, in an ISO-certified facility.</p>"}}
    f["block_order"].insert(4, "q_tested")

    # The three "why" cards say what the founder and standards bands now say in full.
    S["why"]["disabled"] = True


def main():
    raw = open(SNAP).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    assert d["sections"]["faq"]["blocks"][d["sections"]["faq"]["block_order"][0]]["type"] == "q", "check FAQ block type"

    raw2 = open(V2).read()
    v2 = json.loads(raw2[raw2.index("{"):])
    for key in FROM_V2:
        d["sections"][key] = v2["sections"][key]

    # Under the buy button: drop the serving line, the "Not another multivitamin" copy and the
    # review-quote slider (the rotating reviews band further down does that job). Blanked and
    # hidden, not deleted, so they can be switched back in the theme editor.
    buy = d["sections"]["buy"]
    buy["settings"]["serving"] = ""
    buy["settings"]["text"] = ""
    for k, blk in buy["blocks"].items():
        if blk["type"] == "snippet":
            blk["disabled"] = True

    d["sections"].update({
        "statement": STATEMENT,
        "standards": standards(),
        "quotes": reviews(),
        "founder": FOUNDER,
    })
    clinical(d)
    d["sections"]["custom_reviews_KpXTpD"]["settings"]["bg_color"] = WHITE
    d["sections"]["bands"] = bands_css()

    d["order"] = [
        "buy",
        "statement",        # "Not ready to slow down."
        "board_anchor",     # #scientific-board, linked from the buy box
        "board",            # Scientific Advisory Board, compact row
        "standards",
        "tests",            # #test-results: certificate-of-analysis panel (a dialog, opens from links)
        "results",          # customer videos, 9:16
        "quotes",      # up to 20 rotating written reviews
        "founder",
        "problem", "benefits", "steps", "guarantee", "why", "compare", "faq",
        "custom_reviews_KpXTpD", "sticky", "easy_read", "bands",
    ]
    assert sorted(d["order"]) == sorted(d["sections"]), set(d["order"]) ^ set(d["sections"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
