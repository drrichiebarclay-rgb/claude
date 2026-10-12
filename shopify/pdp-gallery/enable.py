"""Turn on "Use the product's own images" in every muto-crea-buy section of the given templates.

Usage: python3 enable.py <template.json> [...]
"""
import json
import sys

for path in sys.argv[1:]:
    raw = open(path).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    n = 0
    for sec in d["sections"].values():
        if sec["type"] == "muto-crea-buy":
            sec.setdefault("settings", {})["gallery_from_product"] = True
            n += 1
    open(path, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(path, n)
