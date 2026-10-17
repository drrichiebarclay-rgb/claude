"""Artah-style buy box for the -2 product page (template product.muto-nad-45).

Template-only: copy goes into the buy section's settings and blocks, styling into
the page's own custom-liquid block (easy_read), which no other template uses.
The shared muto-crea-buy section is not changed.

Usage: python3 apply_artah.py <in template.json> <out template.json>
"""
import json, re, sys

CSS = open(__file__.replace("apply_artah.py", "artah.css")).read()
JS = open(__file__.replace("apply_artah.py", "artah.js")).read()

SETTINGS = {
    "eyebrow": "MUTO",
    "heading": "NAD+ Cellular Complex",
    "serving": "Serving: 30-day supply (60 capsules), 2 a day",
    "text": "<p><strong>Your daily NAD+ formula, made for adults over 40.</strong></p>"
            "<p>NAD+ is the molecule your cells use to make energy. MUTO is built around 300mg NR, a form of vitamin B3 "
            "your body turns into NAD+, with TMG, CoQ10, PQQ, resveratrol, vitamins D3 and K2 and all 8 B vitamins. "
            "19 ingredients in 2 capsules, every dose on the label.</p>"
            "<p><a href=\"#whats-inside\" class=\"mc-art__inside\">Ingredients + nutritional information</a></p>",
    "plans_banner": "Welcome kit worth £62, free with your first box",
    "plans_label": "Choose your plan",
    "kit_title": "Free in your first box (worth £62):",
    "gifts_label": "Plus free gifts in boxes 2 to 6",
    "onetime_label": "One-time purchase, no gifts – [price]",
    "cta_label": "Subscribe",
    "cta_price": True,
}
POINTS = [
    "Supports your cells’ NAD+",
    "Helps reduce tiredness + fatigue",
    "Supports energy metabolism",
    "Supports mental performance",
    "Supports normal muscle function",
    "One jar instead of several pots",
]
PLAN = {"name": "Monthly subscription", "price_suffix": "/mo", "save": "Save 14%",
        "note": "£2 a day. £60 every 4 weeks.",
        "detail": "<ul><li>Save 14% on every box, plus free gifts</li><li>Skip, pause or cancel any time</li>"
                  "<li>30-day supply, delivered every 4 weeks</li><li>Free next-day delivery</li></ul>"}


def main(src, dst):
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
    p1 = next(k for k in order if buy["blocks"][k]["type"] == "plan")
    buy["blocks"][p1]["settings"].update(PLAN)
    # Page CSS + the ingredients link
    d["sections"]["easy_read"]["settings"]["custom_liquid"] = "<style>\n" + CSS + "\n</style>\n<script>\n" + JS + "\n</script>"
    json.dump(d, open(dst, "w"), ensure_ascii=False, indent=2)
    print("wrote", dst, "points:", new, "plan:", p1)


if __name__ == "__main__":
    main(*sys.argv[1:3])
