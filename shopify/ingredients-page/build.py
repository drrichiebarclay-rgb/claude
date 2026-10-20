"""Ingredient library page: builds templates/page.ingredients.json from ingredients.json.

ingredients.json is the copy for each ingredient (n name, d dose, t tags, c powder colour as RGB,
p powder pattern, w what it does, s supports, y why this form & dose, r key references). Edit it, then run
python3 build.py from this folder.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ING = json.load(open(os.path.join(HERE, "ingredients.json")))

CATS = [  # the statement under the filters, one per filter ("All" shows first)
    ("All", "MUTO puts 19 ingredients in two capsules: NR to raise NAD+, CoQ10 and PQQ for your mitochondria, a full B complex in active forms, vitamins D3 and K2, zinc and copper, and plant polyphenols. Every dose is on the label.",
     ["Daily energy", "Cellular health", "Immune function", "Healthy ageing"]),
    ("Energy", "MUTO’s energy ingredients work where energy is made: inside your cells. Your body turns NR into NAD+, CoQ10 and PQQ support the mitochondria, and the active B vitamins help release energy from food.",
     ["Steady energy through the day", "Less tiredness and fatigue", "Cellular energy production"]),
    ("Recovery", "Recovery starts at the cellular level. Vitamin D3 supports normal muscle function, CoQ10 and PQQ support the mitochondria that refill your energy stores, and riboflavin helps reduce tiredness.",
     ["Bouncing back after activity", "Normal muscle function", "Less tiredness and fatigue"]),
    ("Stress", "A demanding week uses up the nutrients your nervous system relies on. MUTO’s B vitamins in their active forms, with zinc, support normal psychological function and mental performance.",
     ["Normal psychological function", "Mental performance", "Focus through the day"]),
    ("Longevity", "NAD+ falls as we get older. MUTO pairs 300mg NR with TMG, then adds trans-resveratrol and grape seed polyphenols, vitamin K2 for your bones and zinc to help protect cells from oxidative stress.",
     ["Healthy ageing", "NAD+ levels", "Normal bones", "Protecting your cells"]),
    ("Immunity", "Vitamin D3, zinc, copper, folate and vitamins B6 and B12 all contribute to the normal function of the immune system, so one jar covers what most people take separately through the winter.",
     ["Immune function", "Winter wellbeing", "Daily nutrient intake"]),
]

blocks, order = {}, []
for i, (n, t, sup) in enumerate(CATS, 1):
    k = f"cat{i}"
    blocks[k] = {"type": "category", "settings": {"name": n, "text": t, "supports": "\n".join(sup)}}
    order.append(k)
for i, g in enumerate(ING, 1):
    k = f"ing{i:02d}"
    blocks[k] = {"type": "ingredient", "settings": {
        "name": g["n"], "dose": g["d"], "tags": ", ".join(g["t"]),
        "colour": "#%02x%02x%02x" % tuple(g["c"]), "pattern": g["p"],
        "description": g["w"], "supports": g["s"], "why": g["y"],
        "refs": "\n".join(g.get("r", []))}}
    order.append(k)

tpl = {"sections": {"library": {"type": "muto-ingredient-library", "blocks": blocks, "block_order": order,
                                "settings": {"cta_label": "Start your 90 days", "cta_link": "/products/muto-nad-cellular-complex"}}},
       "order": ["library"]}
os.makedirs(os.path.join(HERE, "templates"), exist_ok=True)
out = os.path.join(HERE, "templates", "page.ingredients.json")
json.dump(tpl, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(order) - len(CATS), "ingredients,", len(CATS), "filter statements")
