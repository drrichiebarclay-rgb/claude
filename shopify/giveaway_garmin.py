"""Swap the Oura prize-draw references for the Garmin watch giveaway in product templates.

Usage: python3 giveaway_garmin.py <template.json> [...]
"""
import json
import sys

IMG = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-garmin.jpg?v=1791883127"
TEXT = {
    'Entry to our Oura Ring 5 prize draw (<a href="/pages/better-baseline-giveaway">T&amp;Cs</a>)':
        'Entry to our Garmin watch prize draw (<a href="/pages/better-baseline-giveaway">T&amp;Cs</a>)',
    'A chance to win an Oura Ring (<a href="/pages/better-baseline-giveaway">rules</a>)':
        'A chance to win a Garmin watch (<a href="/pages/better-baseline-giveaway">rules</a>)',
}

for path in sys.argv[1:]:
    raw = open(path).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    buy = d["sections"]["buy"]
    for b in buy["blocks"].values():
        st = b.get("settings", {})
        if b["type"] == "gift" and "oura" in (st.get("value", "") + st.get("image_fallback", "")).lower():
            st.update({"value": "Garmin Watch", "name": "giveaway entry", "image_fallback": IMG,
                       "image_alt": "A white Garmin watch, the giveaway prize in the welcome kit"})
            st.pop("image", None)
        if b["type"] == "term" and st.get("text") in TEXT:
            st["text"] = TEXT[st["text"]]
    out = json.dumps(d, ensure_ascii=False, indent=2)
    assert "oura" not in out.lower(), path
    open(path, "w").write(head + out + "\n")
    print("updated", path)
