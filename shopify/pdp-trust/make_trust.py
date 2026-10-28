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
OUT = os.path.join(HERE, "theme", "templates", "product.muto-nad-45.json")
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"

# --- New: statement ----------------------------------------------------------
STATEMENT = {"type": "muto-crea-statement", "settings": {
    "label": "",
    "heading": "A daily supplement.",
    "sub": "Built for your biology after 35 years old.",
    "space_top": 100, "space_bottom": 100}}

# --- New: standards ----------------------------------------------------------
STANDARDS_ITEMS = [
    ("tested", "Every batch", "Third-party tested",
     "<p>Every batch is tested by an independent lab for identity, potency, heavy metals and microbes before it’s released.</p>",
     # Set CERTS_URL to the page where the certificates are published.
     "View the certificates", "", "Certificates of analysis on request"),
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
CERTS_URL = ""  # e.g. "/pages/certificates" once they're published

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
        "eyebrow": "Our standards",
        "heading": "Checked, not\ntaken on trust.",
        "lede": "Most supplements are sold without independent checks, and many hide their doses in blends. These are the four things we hold MUTO to.",
        "foot": "",
        "space_top": 100, "space_bottom": 100}}

# --- New: rotating reviews ---------------------------------------------------
# Real customer words only, copied from REVIEWS.io. Add up to 20; fill in ages
# (with the customer's OK) and set require_age to True once every card has one.
REVIEWS = [
    # topic (ours), quote (theirs, exact), name, age
    ("Afternoon energy", "No afternoon slump and in general feeling great", "Lynda", ""),
    ("Feeling like yourself", "I didn't realise how flat I'd been feeling until this helped lift me out of it", "Holly P", ""),
    ("Recovery", "Has actually changed my recovery", "Adam H", ""),
    ("Mornings", "I predominantly struggle with mornings but already feel myself finding these easier", "Becca", ""),
    ("Marathon training", "I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint", "Rebeca", ""),
    ("Focus", "More focused during the day", "Alexandra", ""),
    ("Fewer pots", "I love that this replaces multiple products", "Amy C", ""),
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
        "eyebrow": "Customer reviews",
        "heading": "Selected\nreviews.",
        "summary": "",  # e.g. "4.8 from 412 reviews": the live REVIEWS.io figure
        "interval": 6, "min_age": 30, "require_age": False,
        "foot": "Real reviews from verified customers, in their own words. Everyone is different.",
        "space_top": 100, "space_bottom": 100}}

# --- New: founder ------------------------------------------------------------
FOUNDER = {"type": "muto-crea-founder",
    "blocks": {
        "f1": {"type": "fact", "settings": {"label": "Founder", "value": "Dr Richie Barclay"}},
        "f2": {"type": "fact", "settings": {"label": "Training", "value": "PhD, cellular biology and nutrition"}},
        "f3": {"type": "fact", "settings": {"label": "Before MUTO", "value": "Cricketer"}},
        "f4": {"type": "fact", "settings": {"label": "Reviewed by", "value": "A Scientific Advisory Board of 6 doctors and scientists"}},
    },
    "block_order": ["f1", "f2", "f3", "f4"],
    "settings": {
        "eyebrow": "Our founder",
        "heading": "Built by a doctor\nwho wanted proof.",
        "text": "<p>Supplements are a loosely policed industry. Doses hide in proprietary blends, and claims often go unchecked.</p>"
                "<p>Dr Richie Barclay, a cell biologist with a PhD in cellular biology and nutrition, built MUTO to bring the rigour of the lab to it: "
                "every dose on the label, every batch tested by an outside lab, and a board of doctors and scientists who review the formula.</p>",
        "quote": "I built MUTO because I was tired of supplements that ask you to take them on trust.",
        "quote_by": "Dr Richie Barclay, PhD · Founder",
        "link_label": "Got a question? Email Richie",
        "link": "mailto:hello@mutolongevity.com",
        "image": "shopify://shop_images/about-founder.jpg",
        "image_fallback": CDN + "about-founder.jpg?v=1790751995",
        "image_alt": "Dr Richie Barclay holding a jar of NAD+ Cellular Complex",
        "image_position": "50% 20%",
        "caption": "",
        "space_top": 100, "space_bottom": 100}}

# --- Existing sections: a slightly more clinical voice ----------------------
def clinical(d):
    S = d["sections"]

    r = S["results"]["settings"]           # the 9:16 customer videos
    r["heading"] = "Customer\nreports."
    r["note"] = "Filmed by customers, in their own words."
    r["foot"] = "Individual experiences. Everyone is different, and we can’t promise results."
    S["results"]["settings"]["space_top"] = 70   # sits under the standards band, which brings its own space

    b = S["board"]["settings"]
    b["heading"] = "Scientific\nAdvisory Board."
    b["note"] = "Six doctors and scientists who review the formula."

    st = S["steps"]
    st["settings"]["heading"] = "A 90-day protocol."
    st["settings"]["heading_right"] = "Measured by you."
    steps = [
        ("Day 1", "Record a baseline.", "Score your energy and sleep out of 10. It takes 30 seconds."),
        ("Daily", "2 capsules, with breakfast.", "Same time each day. Keep the jar by the kettle."),
        ("Day 30", "First check-in.", "Score again. Most people notice the afternoons first."),
        ("Day 90", "Compare with day 1.", "See the difference, or get your money back."),
    ]
    for k, (chip, title, text) in zip(st["block_order"], steps):
        st["blocks"][k]["settings"].update({"chip": chip, "title": title, "text": text})

    c = S["compare"]
    c["settings"]["heading"] = "One formula.\nEvery dose declared."
    for blk in c["blocks"].values():
        if blk["settings"].get("claim") == "Every amount on the label":
            blk["settings"]["claim"] = "Every dose declared on the label"
        if blk["settings"].get("claim") == "NR, the building block for NAD+":
            blk["settings"]["claim"] = "300mg NR, the building block for NAD+"

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

    d["sections"].update({
        "statement": STATEMENT,
        "standards": standards(),
        "reviews_top": reviews(),
        "founder": FOUNDER,
    })
    clinical(d)

    d["order"] = [
        "buy",
        "standards",        # our greatest asset, straight under the buy box
        "results",          # customer videos, 9:16
        "reviews_top",      # 20 rotating written reviews
        "founder",
        "board",
        "statement",        # "A daily supplement. Built for your biology after 35 years old."
        "problem", "benefits", "steps", "guarantee", "why", "compare", "faq",
        "custom_reviews_KpXTpD", "sticky", "easy_read",
    ]
    assert sorted(d["order"]) == sorted(d["sections"]), set(d["order"]) ^ set(d["sections"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
