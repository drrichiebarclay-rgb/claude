"""Ingredient library page: builds templates/page.ingredients.json from ingredients.json.

ingredients.json is the copy for each ingredient (n name, d dose, t tags, c powder colour as RGB,
p powder pattern, w what it does, s supports, y why this form & dose). Edit it, then run
python3 build.py from this folder.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ING = json.load(open(os.path.join(HERE, "ingredients.json")))

blocks, order = {}, []
for i, g in enumerate(ING, 1):
    k = f"ing{i:02d}"
    blocks[k] = {"type": "ingredient", "settings": {
        "name": g["n"], "dose": g["d"], "tags": ", ".join(g["t"]),
        "colour": "#%02x%02x%02x" % tuple(g["c"]), "pattern": g["p"],
        "description": g["w"], "supports": g["s"], "why": g["y"]}}
    order.append(k)

tpl = {"sections": {"library": {"type": "muto-ingredient-library", "blocks": blocks, "block_order": order,
                                "settings": {}}},
       "order": ["library"]}
os.makedirs(os.path.join(HERE, "templates"), exist_ok=True)
out = os.path.join(HERE, "templates", "page.ingredients.json")
json.dump(tpl, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(order), "ingredients")
