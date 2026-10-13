"""The NAD+ comparison table ("The smarter way to buy NAD+"), shared by every NAD+ product page.

Used by pdp-creatine-kit/make_kit.py and, from the command line, for the pages without the creatine kit:
    python3 compare_table.py <template.json> <normal|simple> <kit|nokit>

Headings use NAD⁺ (U+207A): custom.js wraps an ASCII 'NAD+' plus in <sup>, which breaks the
flex-column heading onto extra lines.
"""
import json
import sys

TABLES = {
    "normal": dict(
        heading="The smarter way\nto buy NAD⁺.",
        cols=("MUTO", "NAD+ alone", "Buying separately", "NAD+ drips"),
        rows=[
            ("NR 300mg, the NAD+ building block", "yes", "yes", "yes", "dash"),
            ("Plus TMG 450mg, alongside the NR", "yes", "no", "yes", "dash"),
            ("Plus 12 vitamins and minerals: B group, D3, K2, zinc and copper", "yes", "no", "yes", "dash"),
            ("Plus CoQ10 150mg and PQQ 20mg", "yes", "no", "yes", "dash"),
            ("Plus grape seed, trans-resveratrol and BioPerine®", "yes", "no", "yes", "dash"),
            ("One routine: two capsules a day", "yes", "yes", "no", "no"),
            ("All 19 ingredients for £2 a day", "yes", "no", "no", "no"),
            ("Every dose on the label, made in the UK", "yes", "dash", "dash", "dash"),
            ("90-day money-back guarantee", "yes", "dash", "dash", "no"),
        ],
        gift={"kit": "Free Ultrapure Creatine (worth £30) with your first order",
              "nokit": "Free welcome kit with your first order"}),
    "simple": dict(
        heading="The easy way\nto get NAD⁺.",
        cols=("MUTO", "NAD+ alone", "Lots of pills", "NAD+ drips"),
        rows=[
            ("NR, the building block for NAD+", "yes", "yes", "yes", "dash"),
            ("Plus TMG, which works alongside NR", "yes", "no", "yes", "dash"),
            ("Plus 12 vitamins and minerals", "yes", "no", "yes", "dash"),
            ("Plus CoQ10 and PQQ", "yes", "no", "yes", "dash"),
            ("Plus 3 plant extracts, like grape seed", "yes", "no", "yes", "dash"),
            ("Just 2 capsules a day", "yes", "yes", "no", "no"),
            ("All 19 ingredients for £2 a day", "yes", "no", "no", "no"),
            ("Every amount on the label", "yes", "dash", "dash", "dash"),
            ("Money back for 90 days", "yes", "dash", "dash", "no"),
        ],
        gift={"kit": "Free creatine (worth £30) in your first box",
              "nokit": "Free gifts in your first box"}),
}


def apply(d, tone, kit):
    """Write the comparison into template dict d. tone: normal|simple; kit: True on creatine-kit pages."""
    t = TABLES[tone]
    rows = t["rows"] + [(t["gift"]["kit" if kit else "nokit"], "yes", "dash", "dash", "dash")]
    cmp = d["sections"]["compare"]
    cmp["settings"].update({
        "heading": t["heading"],
        "col_1": t["cols"][0], "col_2": t["cols"][1], "col_3": t["cols"][2], "col_4": t["cols"][3],
        # Compact layout: short rows, smaller type and hairlines so the table scans in one view
        "density": "compact", "head_gap": 40, "claim_width": 562, "col_pitch": 160,
        "panel_width": 120, "space_top": 70, "space_bottom": 70,
    })
    cmp["blocks"] = {}
    cmp["block_order"] = []
    for n, (claim, m1, m2, m3, m4) in enumerate(rows, 1):
        cmp["blocks"][f"r{n}"] = {"type": "row", "settings": {"claim": claim, "m1": m1, "m2": m2, "m3": m3, "m4": m4}}
        cmp["block_order"].append(f"r{n}")


if __name__ == "__main__":
    path, tone, kit = sys.argv[1:]
    raw = open(path).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    apply(d, tone, kit == "kit")
    open(path, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print("updated", path)
