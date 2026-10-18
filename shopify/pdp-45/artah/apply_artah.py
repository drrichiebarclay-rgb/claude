"""Artah-style buy box for the -2 product page (template product.muto-nad-45).

Template-only: copy goes into the buy section's settings and blocks, styling into
the page's own custom-liquid block (easy_read), which no other template uses.
The shared muto-crea-buy section is not changed.

Usage: python3 apply_artah.py <in template.json> <out template.json>
"""
import json, re, sys

CSS = open(__file__.replace("apply_artah.py", "artah.css")).read()
REST_CSS = open(__file__.replace("apply_artah.py", "artah-rest.css")).read()
JS = open(__file__.replace("apply_artah.py", "artah.js")).read()
BF_CSS = open(__file__.replace("apply_artah.py", "bf.css")).read()  # Black Friday early access box
BF_JS = open(__file__.replace("apply_artah.py", "bf.js")).read()

SETTINGS = {
    "eyebrow": "MUTO",
    "heading": "NAD+ Cellular Complex",
    "serving": "Serving: 30-day supply (60 capsules), 2 a day",
    "text": "<p><strong>Your daily NAD+ formula, made for adults over 35.</strong></p>"
            "<p>NAD+ is the molecule your cells use to make energy. MUTO is built around 300mg NR, a form of vitamin B3 "
            "your body turns into NAD+, with TMG, CoQ10, PQQ, resveratrol, vitamins D3 and K2 and all 8 B vitamins. "
            "19 ingredients in 2 capsules, every dose on the label.</p>"
            "<p><a href=\"#whats-inside\">Ingredients + nutritional information</a></p>",
    "plans_banner": "New customer offer, free welcome kit worth £77",
    "plans_label": "Choose your plan",
    "kit_title": "Welcome kit — arrives with your first box",
    "kit_itemised": False,
    "gifts_label": "Future gifts",
    "onetime_label": "One-time purchase, no gifts – [price]",
    "cta_label": "Subscribe",
    "cta_price": True,
    "rating_link": "#ReviewsWidget",
}
POINTS = [
    "Supports your cells’ NAD+",
    "Helps reduce tiredness + fatigue",
    "Supports energy metabolism",
    "Supports mental performance",
    "Supports normal muscle function",
    "One jar instead of several pots",
]
PLAN = {"name": "Monthly plan", "price_suffix": "", "save": "Save 14% + free gifts",
        "note": "Billed £60 every 4 weeks · £2 a day",
        "detail": "<ul><li>Free welcome kit (£62 in value)</li><li>Free gifts in boxes 2 to 6</li>"
                  "<li>Cancel or pause anytime</li><li>90-day money-back guarantee</li></ul>"}
# Quarterly: the price itself comes from Skio's 3-MONTH SUBSCRIPTION plan (set it to £150 there).
PLAN3 = {"name": "Quarterly plan", "price": "£150", "price_suffix": "", "was": "£210",
         "save": "Save 28% + free gifts",
         "note": "Billed £150 every 3 months · £1.67 a day",
         "detail": "<ul><li>Free welcome kit (£77 in value)</li><li>Free gifts in boxes 2 and 3, then creatine in every box</li>"
                   "<li>Cancel or pause anytime</li><li>90-day money-back guarantee</li></ul>"}

CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"
IMG = {"creatine": CDN + "gift-creatine.jpg?v=1791022787", "socks": CDN + "gift-socks.jpg?v=1791023071",
       "jar": CDN + "gift-forever-jar.jpg?v=1791023224", "bottle": CDN + "gift-bottle.jpg?v=1791022787",
       "icon": CDN + "gift-icon.png?v=1770138065", "credit": CDN + "muto-gift-credit-v2.jpg?v=1791392560",
       "consult": CDN + "muto-gift-consultation-v2.jpg?v=1791392559"}
# Plan positions follow Skio's order: 1 = monthly, 2 = quarterly (the page shows quarterly first visually).
Q_GIFTS = [  # quarterly-only first-box gift; the others are the page's own gifts, shared by both plans
    ("qk3", "£15", "Bottle", "Performance Bottle", IMG["bottle"], "The MUTO Performance Bottle in translucent blue"),
]
SHARED_GIFTS = 5  # the first five existing gifts (creatine, socks, jar, guide, Garmin entry) show on both plans
Q_MONTHS = [  # quarterly later boxes
    ("qm2a", "Box 2", "Socks", "£12", IMG["socks"], "A pouch of MUTO Performance Socks, free with box 2"),
    ("qm2b", "Box 2", "Creatine", "£30", IMG["creatine"], "A pouch of MUTO creatine, free with box 2"),
    ("qm2c", "Box 2", "Store credit", "£10", IMG["credit"], "A black MUTO gift card for £10 store credit"),
    ("qm3a", "Box 3", "Creatine", "£30", IMG["creatine"], "A pouch of MUTO creatine, free with box 3"),
    ("qm3b", "Box 3", "Chat with an expert", "£120", IMG["consult"], "A silver MUTO gift card for a one-to-one consultation"),
    ("qm4", "Box 4 on", "Creatine, every box", "£30", IMG["creatine"], "A pouch of MUTO creatine, free in every box from box 4"),
]


def main(src, dst, include_rest=True):
    raw = open(src).read()
    d = json.loads(re.sub(r"^/\*.*?\*/", "", raw, flags=re.S))
    buy = d["sections"]["buy"]
    buy["settings"].update(SETTINGS)
    # Benefits: replace the point blocks with six, keeping their place in the order
    order = buy["block_order"]
    old = [k for k in order if buy["blocks"][k]["type"] == "point"]
    at = order.index(old[0])
    for k in old:
        order.remove(k); del buy["blocks"][k]
    new = [f"ben{i}" for i in range(1, len(POINTS) + 1)]
    for k, t in zip(new, POINTS):
        buy["blocks"][k] = {"type": "point", "settings": {"text": t}}
    order[at:at] = new
    # The monthly plan card (the first plan block)
    plans = [k for k in order if buy["blocks"][k]["type"] == "plan"]
    p1 = plans[0]
    buy["blocks"][p1]["settings"].update(PLAN)
    if len(plans) > 1:
        buy["blocks"][plans[1]]["settings"].update(PLAN3)
    # Gifts per plan: existing gifts and later-box gifts belong to the monthly plan (1);
    # the quarterly plan (2) gets its own first box and later boxes.
    B = buy["blocks"]
    # Drop earlier quarterly duplicates and the hidden trust pills (the section allows 50 blocks)
    for k in [k for k in order if k in ("qk0", "qk1", "qk2", "qk4", "qk5") or B[k]["type"] == "trust"]:
        order.remove(k); B.pop(k, None)
    own_gifts = [k for k in order if B[k]["type"] == "gift" and not k.startswith("q")]
    for i, k in enumerate(own_gifts):
        B[k]["settings"]["plans"] = "" if i < SHARED_GIFTS else "1"
    for k in order:
        if B[k]["type"] == "month" and not k.startswith("q"):
            B[k]["settings"]["plans"] = "1"
    after = order.index(own_gifts[2])  # bottle sits after the jar
    for j, (k, val, name, row, img, alt) in enumerate(Q_GIFTS):
        B[k] = {"type": "gift", "settings": {"value": val, "name": name, "row_label": row, "row_note": "",
                                             "image_fallback": img, "image_alt": alt, "plans": "2"}}
        if k not in order: order.insert(after + 1 + j, k)
    last_month = max(i for i, k in enumerate(order) if B[k]["type"] == "month")
    for j, (k, label, text, val, img, alt) in enumerate(Q_MONTHS):
        B[k] = {"type": "month", "settings": {"label": label, "text": text, "value": val,
                                              "image_fallback": img, "image_alt": alt, "plans": "2"}}
        if k not in order: order.insert(last_month + 1 + j, k)
    # Show the quarterly plan (live had it hidden)
    buy["settings"]["hidden_plans"] = ""
    # Page CSS + the ingredients link
    if "easy_read" not in d["sections"]:
        d["sections"]["easy_read"] = {"type": "custom-liquid", "settings": {"custom_liquid": "", "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}
        d["order"].append("easy_read")
    css = CSS + "\n" + BF_CSS + ("\n" + REST_CSS if include_rest else "")
    d["sections"]["easy_read"]["settings"]["custom_liquid"] = "<style>\n" + css + "\n</style>\n<script>\n" + JS + "\n" + BF_JS + "\n</script>"
    # Age: "over 40" becomes "over 35" anywhere on the page
    def walk(o):
        if isinstance(o, dict):
            return {k: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        if isinstance(o, str):
            return o.replace("over 40", "over 35").replace("Over 40", "Over 35")
        return o
    d = walk(d)
    json.dump(d, open(dst, "w"), ensure_ascii=False, indent=2)
    print("wrote", dst, "points:", new, "plan:", p1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], include_rest="--buybox-only" not in sys.argv)
