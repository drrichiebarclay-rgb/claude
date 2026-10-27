"""Main product page (template product.muto-nad-v2): plans shown per month, AG1-style.

Quarterly £50/mo with £70 struck through, monthly £60/mo with £70 struck through, the % off
as a tag in each box's top-left corner, "Best value" leading the bar over the quarterly box, and
a plain "Add to cart" button with no price on it.
Top of the page (top.css, top.js): on phones the stars, title and a subhead sit above the images,
AgeMate-style, with no "MUTO" over the title; a "View third-party testing results" button sits under
the images (all widths) instead of under the buy box; the
"Ingredients + nutritional information" link is gone from the description.
Template-only: the save copy goes on the plan blocks, the styling (plan-prices.css) into the
page's own custom-liquid block (easy_read). Skio's prices and the section are not changed.

Usage: python3 apply_plan_prices.py <in template.json> <out template.json>
"""
import json, re, sys

CSS = open(__file__.replace("apply_plan_prices.py", "plan-prices.css")).read()
TOP_CSS = open(__file__.replace("apply_plan_prices.py", "top.css")).read()
TOP_JS = open(__file__.replace("apply_plan_prices.py", "top.js")).read()
INGREDIENTS_LINK = re.compile(r"<p><a href=\"#test-results-3\">Ingredients \+ nutritional information</a></p>")
SAVE = {"Monthly plan": "Save 14%",     # £60 against £70
        "Quarterly plan": "Save 28%"}   # £50 against £70
MARK = "/* ---- Plan cards, AG1-style"
CTA = {"cta_label": "Add to cart", "cta_price": False}  # plain button, no price on it


def main(src, dst):
    raw = open(src).read()
    header = re.match(r"^/\*.*?\*/\s*", raw, flags=re.S)
    d = json.loads(raw[header.end():] if header else raw)
    buy = d["sections"]["buy"]
    buy["settings"].update(CTA)
    buy["settings"]["eyebrow"] = ""  # no "MUTO" over the title
    # The testing-results button now sits under the images; drop the one under the buy box
    for k in [k for k in buy["block_order"] if buy["blocks"][k]["type"] == "tests"]:
        buy["block_order"].remove(k); del buy["blocks"][k]
    text, n = INGREDIENTS_LINK.subn("", buy["settings"]["text"])
    assert n == 1, "ingredients link not found"
    buy["settings"]["text"] = text
    for k in buy["block_order"]:
        b = buy["blocks"][k]
        if b["type"] == "plan" and b["settings"].get("name") in SAVE:
            b["settings"]["save"] = SAVE[b["settings"]["name"]]
    s = d["sections"]["easy_read"]["settings"]
    liquid = s["custom_liquid"]
    if MARK in liquid:  # rebuild: drop the earlier copy
        liquid = liquid[:liquid.index(MARK)] + liquid[liquid.index("</style>", liquid.index(MARK)):]
    i = liquid.index("</style>")
    liquid = liquid[:i].rstrip("\n") + "\n\n" + CSS + "\n" + TOP_CSS + liquid[i:]
    j = liquid.rindex("</script>")
    s["custom_liquid"] = liquid[:j].rstrip("\n") + "\n\n" + TOP_JS + liquid[j:]
    json.dump(d, open(dst, "w"), ensure_ascii=False, indent=2)
    print("wrote", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
