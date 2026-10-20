"""Main product page (template product.muto-nad-45): buy box restructured for 40-60 year olds
who aren't sport focused.

Template-only, built on the live template (live-snapshot-20oct/), so edits made on live are kept.
The shared muto-crea-buy section is not changed. Gifts, prices, plans and the Black Friday box are
unchanged; only the copy, the order of what's shown and the type sizes change.

Health claims stay within the UK authorised wording for the formula's vitamins and minerals
(B vitamins: tiredness, energy metabolism; zinc: cognitive function; vitamin D, zinc, B6, B12:
immune system; vitamins D and K: bones).

Usage (from shopify/pdp-45/): python3 age-4060/apply_4060.py
  writes age-4060/product.muto-nad-45.json
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "live-snapshot-20oct", "templates__product.muto-nad-45.json")
DST = os.path.join(HERE, "product.muto-nad-45.json")
AGE_CSS = open(os.path.join(HERE, "age.css")).read()

SETTINGS = {
    "serving": "2 capsules with breakfast · 30-day supply (60 capsules)",
    "text": "<p><strong>A daily formula to help you feel less tired, made for your 40s, 50s and 60s.</strong></p>"
            "<p>If afternoons feel harder than they used to, you’re not alone. Two capsules with breakfast give your body "
            "19 nutrients in one go: NR, a form of vitamin B3 your body turns into NAD+, plus CoQ10, vitamins D3 and K2 "
            "and all 8 B vitamins. No gym, no gadgets, no powders to mix.</p>"
            "<p><a href=\"#whats-inside\">Ingredients + nutritional information</a></p>",
    "plans_banner": "New customers: free welcome kit worth £77",
    "gifts_label": "Thank-you gifts in later boxes",
    "onetime_label": "Prefer to try one jar first? Buy once – [price] (no gifts)",
}
POINTS = [  # "How it helps", two columns on desktop
    "Helps reduce tiredness + fatigue",
    "Helps release energy from food",
    "Supports normal cognitive function",
    "Supports your immune system",
    "Helps maintain normal bones",
    "One jar instead of five pots",
]
TRUST = [  # reassurance, straight above "Choose your plan"
    "90-day money-back guarantee",
    "Skip, pause or cancel online",
    "Made in the UK, every batch lab tested",
]
TICKS = "<li>90-day money-back guarantee</li><li>Skip, pause or cancel online, no phone calls</li><li>Free UK delivery</li>"
PLANS = {  # by block id
    "plan_RAXANa": {  # quarterly, shown first
        "note": "3 months’ supply, billed £150 every 3 months · £1.67 a day",
        "detail": "<ul>" + TICKS + "<li>Free welcome kit worth £77, then thank-you gifts in later boxes</li></ul>",
    },
    "p1": {  # monthly
        "note": "Billed £60 every 4 weeks · £2 a day",
        "detail": "<ul>" + TICKS + "<li>Free welcome kit worth £62, then thank-you gifts in boxes 2 to 6</li></ul>",
    },
}
# Welcome kit tiles: everyday items first, the sport-led ones after (same gifts, same plan tags)
GIFT_ORDER = ["k2", "k3", "qk3", "k1", "k0", "k4"]  # jar, guide, bottle, socks, creatine, Garmin entry
RENAME = {("qk3", "row_label"): "Water bottle", ("mg3", "text"): "Socks"}
# Review quotes: everyday energy and focus; the recovery quote is dropped
SNIPPETS = ["snippet_1", "snippet_2", "snippet_7"]
WHO = ("<p><strong>Made for adults in their 40s, 50s and 60s.</strong>&nbsp;Most of our customers are in their 40s and 50s.</p>"
       "<p><strong>It’s for you if:</strong></p><ul>"
       "<li>Afternoons feel harder than they used to</li>"
       "<li>You want to keep up with work, family and the things you enjoy</li>"
       "<li>Your supplement shelf is full and you’re not sure what works</li>"
       "<li>You’d rather take one simple thing every morning</li></ul>"
       "<p><strong>You don’t need to be sporty</strong>, or own a smartwatch. Walkers and gardeners take it, as well as gym-goers.</p>"
       "<p><strong>Not for</strong>&nbsp;under-18s, or if you’re pregnant or breastfeeding. On medication? Check with your doctor first.</p>")


def main():
    d = json.loads(re.sub(r"^/\*.*?\*/", "", open(SRC).read(), flags=re.S))
    buy = d["sections"]["buy"]
    B, order = buy["blocks"], buy["block_order"]
    buy["settings"].update(SETTINGS)

    # Benefits: same six slots, new wording
    pts = [k for k in order if B[k]["type"] == "point"]
    assert len(pts) == len(POINTS), pts
    for k, t in zip(pts, POINTS):
        B[k]["settings"]["text"] = t

    # Trust row after the benefits (the section draws it between the benefits and the plans)
    for k in [k for k in order if B[k]["type"] == "trust"]:
        order.remove(k); del B[k]
    at = order.index(pts[-1]) + 1
    for i, t in enumerate(TRUST, 1):
        B[f"tr{i}"] = {"type": "trust", "settings": {"text": t}}
    order[at:at] = [f"tr{i}" for i in range(1, len(TRUST) + 1)]

    for k, s in PLANS.items():
        assert B[k]["type"] == "plan", k
        B[k]["settings"].update(s)

    # Reorder the kit tiles in the slots the gifts already occupy
    slots = [i for i, k in enumerate(order) if B[k]["type"] == "gift"]
    assert sorted(order[i] for i in slots) == sorted(GIFT_ORDER), [order[i] for i in slots]
    for i, k in zip(slots, GIFT_ORDER):
        order[i] = k

    for (k, f), v in RENAME.items():
        B[k]["settings"][f] = v

    # Review quotes
    snips = [k for k in order if B[k]["type"] == "snippet"]
    at = order.index(snips[0])
    for k in snips:
        order.remove(k)
        if k not in SNIPPETS:
            del B[k]
    order[at:at] = SNIPPETS

    # "Who it's for" first among the folds, rewritten
    who = next(k for k in order if B[k]["type"] == "fold" and "Who it" in B[k]["settings"]["title"])
    B[who]["settings"]["text"] = WHO
    folds = [i for i, k in enumerate(order) if B[k]["type"] == "fold"]
    order.remove(who); order.insert(folds[0], who)

    assert len(order) <= 50, len(order)  # the section's block limit
    assert set(order) == set(B), set(order) ^ set(B)

    # Page CSS: the age overrides go after the existing styles in easy_read
    er = d["sections"]["easy_read"]["settings"]
    marker = "/* ---- 40-60 buy box ---- */"
    liquid = er["custom_liquid"]
    if marker in liquid:
        liquid = re.sub(re.escape(marker) + r".*?(?=</style>)", "", liquid, flags=re.S)
    er["custom_liquid"] = liquid.replace("</style>", marker + "\n" + AGE_CSS + "</style>", 1)

    json.dump(d, open(DST, "w"), ensure_ascii=False, indent=2)
    print("wrote", DST, "blocks:", len(order))


if __name__ == "__main__":
    main()
