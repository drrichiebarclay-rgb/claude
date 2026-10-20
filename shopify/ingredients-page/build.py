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

# Test results panel, from the batch certificate of analysis (test-results.json)
TR = json.load(open(os.path.join(HERE, "test-results.json")))
assert len(TR["formula"]) == len(ING) == 19
tb, to = {}, []
for i, (g, n, lim, res, note) in enumerate(TR["tests"], 1):
    tb[f"t{i:02d}"] = {"type": "test", "settings": {"group": g, "name": n, "spec": lim, "result": res, "note": note, "pass": True}}
    to.append(f"t{i:02d}")
for i, (g, n, form, amt) in enumerate(TR["formula"], 1):
    tb[f"f{i:02d}"] = {"type": "item", "settings": {"group": g, "name": n, "form": form, "amount": amt}}
    to.append(f"f{i:02d}")
tests = {"type": "muto-test-results", "blocks": tb, "block_order": to, "settings": {
    "show_button": False, "product": TR["product"], "batch": TR["batch"], "doc_label": "Certificate of analysis",
    "made": TR["made"], "bbe": TR["bbe"], "issued": TR["issued"],
    "heading": "Every result came in within its limit.", "stat_value": "300×", "stat_label": "Under the lead limit",
    "chip": "No salmonella detected",
    "note": f"Results from the certificate of analysis for batch {TR['batch']}, issued {TR['issued']}. Ask us for the certificate for your batch: hello@mutolongevity.com",
    "formula_sub": "What went into each capsule of this batch, per two-capsule serving, heaviest first. Vitamins are made with a small overage so the label dose holds right up to the best-before date.",
    "capsule": "Capsule: hypromellose (HPMC), made from plant cellulose. Allergen and intolerance free.",
    "why_1_h": "Heavy metals",
    "why_1": "<p>Lead, cadmium and mercury can build up in the body over time, and they can come in through plant extracts and minerals. Every batch is checked against strict limits, and this one came in well under each: lead at 0.010 ppm against a limit of 3.</p>",
    "why_2_h": "Microbes",
    "why_2": "<p>Bacteria, yeasts and moulds can grow in ingredients that are stored or handled badly. This batch was screened for six, including salmonella and E. coli, and every result was far inside its limit: no salmonella detected, and every other count under 100 per gram.</p>",
    "why_3_h": "Capsule quality",
    "why_3": "<p>Weight uniformity checks every capsule holds the same fill, so every serving gets the dose on the label. Disintegration checks the capsule breaks down within 30 minutes, so the ingredients are released in time to be absorbed.</p>",
    "why_4_h": "Every batch, not just the first",
    "why_4": "<p>A new batch gets a new certificate. We’ll update these results each time, and your batch number is on the jar.</p>"}}
tpl = {"sections": {"library": {"type": "muto-ingredient-library", "blocks": blocks, "block_order": order,
                                "settings": {"cta_label": "Start your 90 days", "cta_link": "/products/muto-nad-cellular-complex",
                                             "tests_label": "View third-party testing results"}},
                    "tests": tests},
       "order": ["library", "tests"]}
os.makedirs(os.path.join(HERE, "templates"), exist_ok=True)
out = os.path.join(HERE, "templates", "page.ingredients.json")
json.dump(tpl, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(order) - len(CATS), "ingredients,", len(CATS), "filter statements")
