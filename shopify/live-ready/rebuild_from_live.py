"""Rebuild the live-ready templates from a snapshot of the LIVE theme, applying only the 13 Oct changes.

The dev edits live directly, so live-ready files are rebuilt on top of live rather than copied from the
draft theme. Usage (from shopify/):  python3 live-ready/rebuild_from_live.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import compare_table  # noqa: E402

SNAP = os.path.join(HERE, "live-snapshot-13oct")
GARMIN_IMG = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-garmin.jpg?v=1791883127"
GARMIN_ALT = "A white Garmin watch, the giveaway prize in the welcome kit"
TERMS = {
    'Entry to our Oura Ring 5 prize draw (<a href="/pages/better-baseline-giveaway">T&amp;Cs</a>)':
        'Entry to our Garmin watch prize draw (<a href="/pages/better-baseline-giveaway">T&amp;Cs</a>)',
    'A chance to win an Oura Ring (<a href="/pages/better-baseline-giveaway">rules</a>)':
        'A chance to win a Garmin watch (<a href="/pages/better-baseline-giveaway">rules</a>)',
}


def load(name):
    raw = open(os.path.join(SNAP, name)).read()
    return raw[: raw.index("{")], json.loads(raw[raw.index("{"):])


def save(path, head, d):
    open(os.path.join(HERE, path), "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print("wrote", path)


def garmin(d, row_label=None):
    for b in d["sections"]["buy"]["blocks"].values():
        st = b.get("settings", {})
        if b["type"] == "gift" and "oura" in (st.get("value", "") + st.get("image_fallback", "")).lower():
            st.update({"value": "Garmin Watch", "name": "giveaway entry", "image_fallback": GARMIN_IMG, "image_alt": GARMIN_ALT})
            st.pop("image", None)
            if row_label:
                st["row_label"] = row_label
        if b["type"] == "term" and st.get("text") in TERMS:
            st["text"] = TERMS[st["text"]]


for name, tone, kit in [("product.muto-nad.json", "normal", False),
                        ("product.muto-nad-simple.json", "simple", False),
                        ("product.muto-nad-creatine-kit.json", "normal", True)]:
    head, d = load("templates__" + name)
    garmin(d, row_label="Chance to win a Garmin Watch" if kit else None)
    compare_table.apply(d, tone, kit)
    out = json.dumps(d, ensure_ascii=False)
    assert "oura" not in out.lower(), name
    save("templates/" + name, head, d)

head, d = load("templates__product.give-away.json")
form = d["sections"]["giveaway_registration_form_ej3c6J"]["settings"]
form["heading"] = "ENTER YOUR EMAIL FOR A CHANCE TO WIN A GARMIN WATCH."
form["description"] = ('<p>Each quarter, one winner chosen at random picks a Garmin watch worth up to £200. See the '
                       '<a href="/pages/better-baseline-giveaway" title="Garmin Watch Giveaway Terms & Conditions">'
                       'terms &amp; conditions</a> for the draw.</p>')
save("templates/product.give-away.json", head, d)

head, d = load("templates__page.faq-new.json")
n = 0
for sec in d["sections"].values():
    for b in sec.get("blocks", {}).values():
        c = b.get("settings", {}).get("content", "")
        if "competition to win an Oura Ring" in c:
            b["settings"]["content"] = c.replace("entry into our competition to win an Oura Ring",
                                                 "entry into our quarterly draw to win a Garmin watch")
            n += 1
assert n == 1
save("templates/page.faq-new.json", head, d)
