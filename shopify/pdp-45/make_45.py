"""Build the 45-55 PDP (product.muto-nad-45.json) from the draft simple creatine-kit page.

For muto-nad-cellular-complex-3. Same offer, plans, gifts, images, CTA labels and
comparison table. Copy rewritten to speak to 45-55-year-olds in plain, emotional
language; fewer sections in a simpler order; easier-reading styles (easy-read.css)
shipped inside the template's own custom-liquid section, so no shared file changes.

Usage: python3 make_45.py [base] [out]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import compare_table  # noqa: E402
base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "../pdp-creatine-kit/product.muto-nad-simple-creatine-kit.json")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "product.muto-nad-45.json")

raw = open(base).read()
header = re.match(r"^/\*.*?\*/\s*", raw, flags=re.S)
d = json.loads(raw[header.end():] if header else raw)
S = d["sections"]


def s(sec, **kw):
    S[sec]["settings"].update(kw)


def b(sec, blk, **kw):
    S[sec]["blocks"][blk]["settings"].update(kw)


def drop_blocks(sec, keys):
    for k in keys:
        S[sec]["blocks"].pop(k, None)
    S[sec]["block_order"] = [k for k in S[sec]["block_order"] if k not in keys]


# ---- Buy box ---------------------------------------------------------------
s("buy",
  text="<p>You’re not ready to slow down. You just want to feel like yourself again, with energy for the whole day, not just the morning.</p><p>Two capsules with breakfast. Give it 90 days. Love it, or get your money back.</p>",
  plans_banner="Welcome kit worth £62, free with your first order")
b("buy", "b1", text="Feel like yourself again")
b("buy", "b2", text="Energy that lasts past lunch")
b("buy", "b3", text="Bounce back after a walk, a round or the gym")
b("buy", "b4", text="90 days to try it, or your money back")

# Giveaway prize is a Garmin watch (the live simple-kit page still shows Oura)
b("buy", "k4", value="Garmin Watch", name="giveaway entry", row_label="Chance to win a Garmin Watch",
  row_note="Free entry",
  image_fallback="https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-garmin.jpg?v=1791883127",
  image_alt="A white Garmin watch, the giveaway prize in the welcome kit")
S["buy"]["blocks"]["k4"]["settings"].pop("image", None)

# ---- Problem ---------------------------------------------------------------
s("problem",
  heading="You don’t feel old.\nSo why so tired?",
  lede="You still work hard, look after everyone and keep moving. But the afternoons drag, the aches hang around, and the energy you used to take for granted isn’t there. It’s not just you, and it’s not in your head.")
b("problem", "c1", quote="“I used to have so much energy.”",
  text="Now the afternoon slump turns up every day.")
b("problem", "c2", quote="“My body takes longer to recover.”",
  text="A long walk or a game of tennis costs you the next day.")
b("problem", "c4", quote="“I just want to feel like me again.”",
  text="Not younger. Just yourself, with something left at the end of the day.")
b("problem", "c3", quote="“Too many pills.”",
  text="A cupboard full, and no idea which ones work.")
S["problem"]["block_order"] = ["c1", "c2", "c4", "c3"]

# ---- Benefits: one simple view (the tracking tab is folded into the steps) ----
drop_blocks("benefits", ["pt", "ck1", "ck2", "ck3"])
b("benefits", "pf", heading="What people\nnotice first",
  lede="Real customers, in their own words. Everyone is different.")
b("benefits", "f1", title="Energy that lasts past lunch",
  text="<p>Most people notice the afternoons first. No 3pm slump, and energy left for the evening. It’s not a buzz like coffee. It builds steadily, day by day.</p>")
b("benefits", "f2", title="Bouncing back sooner",
  text="<p>Ready for the next walk, round of golf or class sooner, instead of days later.</p>")
b("benefits", "f3", title="Easier mornings",
  text="<p>Getting up feels less like a battle. You don’t need a gadget to notice.</p>")
b("benefits", "f4", title="Feeling like yourself",
  sub="“I didn't realise how flat I'd been feeling until this helped lift me out of it” – Holly P",
  text="<p>Many people say they didn’t realise how flat they’d been feeling until it lifted.</p>")

# ---- Results -----------------------------------------------------------------
s("results", heading="Real people.\nReal stories.", note="In their own words")

# ---- Steps (now also covers how to take it and how to check) ------------------
s("steps", heading="Give it 90 days.", heading_right="See how you feel.")
b("steps", "s1", chip="Day 1", title="Score how you feel.",
  text="Energy and sleep, out of 10. It takes 30 seconds.")
b("steps", "s2", chip="Every day", title="Two with breakfast.",
  text="Keep the jar by the kettle, so you don’t forget.")
b("steps", "s3", chip="Day 30", title="Check in.",
  text="Many people notice the afternoons first.")
b("steps", "s4", chip="Day 90", title="You decide.",
  text="Feel the difference, or get your money back.")

# ---- Why MUTO --------------------------------------------------------------
s("why", heading="Why people trust MUTO")
b("why", "w1", title="Made by a scientist you can talk to.",
  text="Dr Richie Barclay, PhD, made MUTO and checks it with a board of doctors. Got a question? Email him.")

# ---- FAQ -------------------------------------------------------------------------
q0 = json.loads(json.dumps(S["faq"]["blocks"]["q1"]))
q0["settings"].update(
    title="Is it right for my age?",
    text="<p>Yes. MUTO is made for adults over 40, and most of our customers are in their 40s and 50s. You don’t need to be sporty or own a smartwatch.</p>")
S["faq"]["blocks"]["q0"] = q0
S["faq"]["block_order"] = ["q0", "q3", "q1", "q2", "q4", "q6", "q5"]

# ---- Comparison table (shared plain-English copy, kit variant) -----------------------
compare_table.apply(d, "simple", kit=True)

# ---- Easier-reading styles, scoped to this template ---------------------------------
css = open(os.path.join(HERE, "easy-read.css")).read()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = "\n".join(l.strip() for l in css.splitlines() if l.strip())
S["easy_read"] = {
    "type": "custom-liquid",
    "settings": {"custom_liquid": "<style>\n" + css + "\n</style>", "color_scheme": "scheme-1",
                 "padding_top": 0, "padding_bottom": 0},
}

# ---- Simpler order: feel → hope → proof → how → trust → detail ------------------------
for k in ("twocaps", "ingredients"):
    S.pop(k, None)
d["order"] = ["buy", "problem", "benefits", "results", "steps", "guarantee",
              "why", "board", "compare", "faq", "custom_reviews_KpXTpD", "sticky", "easy_read"]
assert set(d["order"]) == set(S), set(S) ^ set(d["order"])

with open(out, "w") as f:
    if header:
        f.write(header.group(0))
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
