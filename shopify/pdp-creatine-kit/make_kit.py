"""Clone a NAD+ product template with creatine added to the welcome kit.

Usage: python3 make_kit.py <base template> <out template> <normal|simple>
Adds a creatine gift as the first welcome-kit tile and updates the first-order reassurance row.
"""
import json
import sys

src, out, tone = sys.argv[1:]
raw = open(src).read()
head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
buy = d["sections"]["buy"]
IMG = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-creatine.jpg?v=1791022787"

buy["blocks"]["k0"] = {"type": "gift", "settings": {
    "value": "£30",
    "name": "Micronised Creatine" if tone == "normal" else "Creatine",
    "image_fallback": IMG,
    "image_alt": "A pouch of MUTO Ultrapure Micronised Creatine Monohydrate, part of the welcome kit",
    "plans": "",
}}
order = buy["block_order"]
assert "k0" not in order
order.insert(order.index("k1"), "k0")

buy["blocks"]["term_3"]["settings"]["text"] = (
    "Free with your first order: Ultrapure Micronised Creatine Monohydrate, performance socks, Forever Jar, 12-week protocol guide"
    if tone == "normal" else
    "Free in your first box: creatine, socks, a jar and a guide"
)
open(out, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("written", out)
