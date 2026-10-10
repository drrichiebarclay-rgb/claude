"""Home page copy update (templates/index.json), 10 Oct 2026.

Usage: python3 apply_copy_oct10.py <current template> <output template>
"""
import json
import sys

src, out = sys.argv[1], sys.argv[2]
raw = open(src).read()
head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
S = d["sections"]
CTA = "Start the protocol"

# --- Hero ------------------------------------------------------------------------
hero = S["hero"]["settings"]
hero["heading"] = "Built for people who aren’t\nready to slow down."
hero["subheading"] = (
    "The daily cellular protocol for people who aren’t ready to slow down. Energy that lasts past 3pm, "
    "recovery that keeps pace with your training, and every dose on the label. 90 days to feel the difference."
)

# --- CTAs: every button that leads to the NAD+ protocol --------------------------------
hero["cta_label"] = CTA
for bid in ("pn", "pe"):
    S["shop"]["blocks"][bid]["settings"]["cta_label"] = CTA
S["founder"]["settings"]["cta_label"] = CTA
S["benefits"]["blocks"]["bpn"]["settings"]["cta_label"] = CTA
for b in S["science_nad"]["blocks"].values():
    b["settings"]["cta_label"] = CTA

# --- Why MUTO (same three pillars as the product page) ---------------------------------
why = S["why"]["blocks"]
why["w1"]["settings"].update({
    "title": "Built by a scientist\nyou can talk to.",
    "text": "Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by our "
            "Scientific Advisory Board. Got a question? Ask him.",
    "image": "shopify://shop_images/Richie_Lab.png",
    "image_fallback": "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/Richie_Lab.png?v=1779261881",
    "image_alt": "Dr Richie Barclay in a lab coat",
    "image_position": "50% 25%",
})
why["w2"]["settings"]["text"] = (
    "Nineteen ingredients, each on the label with its dose and the reason it's there. No proprietary blends. "
    "Made in the UK by a GMP-certified manufacturer. Ask your AI to check the label."
)
why["w3"]["settings"]["text"] = (
    "Note how you feel on day 0. Check in at day 30 and day 90, in how your days feel, your training, or your "
    "wearable if you have one. Your verdict, with a 90-day guarantee behind it."
)

# --- Founder ---------------------------------------------------------------------------
f = S["founder"]
f["blocks"]["p1b"] = {"type": "para", "settings": {"text": (
    "I’m not done yet either. Most of the people who take MUTO are in their 40s and 50s, still training, "
    "still working, and not ready to slow down.")}}
order = f["block_order"]
order.insert(order.index("p1") + 1, "p1b")
# p3 already reads "We're running research programmes ... and we'll publish what we find, whatever it shows."

# --- People like you ---------------------------------------------------------------------
S["athletes"]["settings"]["heading"] = "Still training.\nStill working.\nNot done yet."

# --- Board -------------------------------------------------------------------------------
S["board"]["settings"].update({"note": "Our Scientific Advisory Board", "compact": True, "rail_gap": 40})

# --- Numbers -----------------------------------------------------------------------------
st = S["stats"]["blocks"]
st["n1"]["settings"].update({"label": "University\nresearch partners", "caption": ""})
st["n3"]["settings"]["figure"] = "6"

# --- Benefits ----------------------------------------------------------------------------
ben = S["benefits"]
ben["settings"]["heading"] = "Where you’ll\nfeel it"
ben["blocks"]["bpn"]["settings"]["lede"] = (
    "Nineteen ingredients working beneath the surface, on the 30 trillion cells behind your energy, your "
    "recovery and how you age. Judge it over 90 days, in how your days feel."
)
for bid, title, text in [
    ("bn1", "Energy", "Steady through the afternoon, not a spike and a fade."),
    ("bn2", "Recovery", "Bounce back between sessions like you used to."),
    ("bn3", "Calm", "A steadier baseline through busy weeks."),
    ("bn4", "Healthy ageing", "Ageing shows up first in your energy and recovery. Judge it over 90 days, not one morning."),
]:
    ben["blocks"][bid]["settings"].update({"title": title, "text": text})

open(out, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("ok")
