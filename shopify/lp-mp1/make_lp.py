"""Build the MP1 (Slowing Competitor) Meta top-of-funnel landing page:
product.lp-mp1.json, viewed at /products/muto-nad-cellular-complex?view=lp-mp1.

Built from the existing MUTO sections (home hero, problem, why, results, founder,
steps, guarantee, FAQ, banner, sticky) so it carries the brand as-is. Copy follows
the Messaging House "Not Done Yet" (10 Oct 2026): MP1 hooks, the six-beat sequence
(recognition → underneath → protocol → proof → check it yourself → offer) and its
claims guardrails (no "faster recovery", "more energy", "improves HRV"; pain is
described, the result is never promised). Easier-reading styles from the 45-55 page.

Usage: python3 make_lp.py [out]
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SH = os.path.join(HERE, "..")
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "product.lp-mp1.json")


def load(p):
    return json.loads(re.sub(r"^/\*.*?\*/", "", open(os.path.join(SH, p)).read(), flags=re.S))


def copy(x):
    return json.loads(json.dumps(x))


home = load("home-3m-refill/templates/index.json")["sections"]
kit = load("pdp-creatine-kit/product.muto-nad-creatine-kit.json")["sections"]

# Where every CTA goes: the 45-55 product page (-2 after the rollout)
PDP = "/products/muto-nad-cellular-complex-2"
CTA = "Start your 90 days"

S = {}

# ---- 1. Recognition (hero) ----------------------------------------------------
S["hero"] = copy(home["hero"])
S["hero"]["settings"].update(
    heading="Same training.\nSlower recovery.",
    subheading="It’s not your discipline. Recovery is where ageing shows up first, and it starts underneath. MUTO is two capsules with breakfast, every dose on the label, and 90 days to judge it yourself.",
    cta_label=CTA, cta_link=PDP, schema_on=False)

# ---- 1b. Recognition, in their words (problem) ---------------------------------
S["problem"] = copy(kit["problem"])
p = S["problem"]
p["settings"].update(
    eyebrow="Sound familiar?",
    heading="When did Sunday\nstart lasting\nuntil Wednesday?",
    lede="You’re fitter than most people your age, and you still turn up. But the session that used to be gone by Monday now hangs around for days, and more rest isn’t fixing it.")
# Card images: c2 runner catching breath, c1 head down on a bike, c3 the box, c4 reading a score
p["blocks"]["c2"]["settings"].update(quote="“I need longer to recover than I used to.”",
                                     text="Same training. Same sleep. Slower bounce-back.")
p["blocks"]["c1"]["settings"].update(quote="“My legs are still heavy on Sunday.”",
                                     text="Thursday’s session hasn’t left yet.")
p["blocks"]["c3"]["settings"].update(quote="“A cupboard full of pots.”",
                                     text="Five supplements, and no idea which one’s working.")
p["blocks"]["c4"]["settings"].update(quote="“No hype. I want science.”",
                                     text="Big promises, and nothing you can check.")
p["block_order"] = ["c2", "c1", "c3", "c4"]

# ---- 2 + 3. Underneath, then the protocol ----------------------------------------
S["protocol"] = copy(kit["twocaps"])
w = S["protocol"]
w["settings"].update(heading="It starts\nunderneath.", heading_right="So start there.")
w["blocks"]["o1"]["settings"].update(
    title="Underneath",
    text="Your cells use NAD+ to make energy, and levels fall with age. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients.")
w["blocks"]["o2"]["settings"].update(
    title="One routine",
    text="Two capsules with breakfast. 19 ingredients, every dose on the label. No caffeine, no stimulants, nothing to time around training.")
w["blocks"]["o3"]["settings"].update(
    title="Nothing hidden",
    text="Built by Dr Richie Barclay, PhD in cell biology. Made in the UK, every batch third-party tested. Ask your AI what’s in it.")
# o1 needs the founder/cells image less than a product shot: swap o1 and o2 images
o1, o2 = w["blocks"]["o1"]["settings"], w["blocks"]["o2"]["settings"]
for k in ("image", "image_fallback", "image_alt", "image_position"):
    o1[k], o2[k] = o2.get(k, ""), o1.get(k, "")

# ---- 4. Proof: people like them, Day 1 to Day 90 -----------------------------------
S["results"] = copy(kit["results"])
S["results"]["settings"].update(heading="People like you.\nDay 1 to Day 90.", note="In their own words",
                                foot="Individual experiences. We won’t promise what MUTO will do for you.")

# ---- 4b. The guide ---------------------------------------------------------------------
S["founder"] = copy(home["founder"])
f = S["founder"]
f["settings"].update(heading="Meet the scientist\nbehind it.", cta_label=CTA, cta_link=PDP)
f["blocks"]["p1"]["settings"]["text"] = "I’m a cell biologist and a former cricketer. I built MUTO because I was tired of supplements that ask you to take them on trust."
f["blocks"]["p1b"]["settings"]["text"] = "I’m not done yet either. Most people who take MUTO are in their 40s and 50s, still training, still working."
f["blocks"]["p2"]["settings"]["text"] = "So every ingredient and every dose is on the label, with the reason it’s there. Got a question about the formula? Ask me."
f["blocks"]["p4"]["settings"]["text"] = "And don’t take my word for it. Note your starting point, give it 90 days, and make your own call."
f["blocks"].pop("p3", None)
f["block_order"] = ["p1", "p1b", "p2", "p4"]

# ---- 5. Check it yourself ----------------------------------------------------------------
S["steps"] = copy(kit["steps"])
st = S["steps"]
st["settings"].update(heading="Don’t take it on trust.", heading_right="Check it yourself.")
st["blocks"]["s1"]["settings"].update(chip="Day 0", title="Note your starting point.",
    text="How your legs feel the day after a hard session, out of 10. Or a 7-day average, if you wear a watch.")
st["blocks"]["s2"]["settings"].update(chip="Weeks 1–4", title="Train as normal.",
    text="Two capsules with breakfast, every day. Keep everything else the same.")
st["blocks"]["s3"]["settings"].update(chip="Day 30", title="First check-in.",
    text="Compare with day 0. How did the days after your hard sessions feel?")
st["blocks"]["s4"]["settings"].update(chip="Day 90", title="Your call.",
    text="If you don’t see a difference, you’re covered.")

S["guarantee"] = copy(kit["guarantee"])
S["guarantee"]["settings"].update(
    heading="90 days.\nYour verdict.",
    aside="If you don’t see a difference, you’re covered.",
    text="<p>Subscribe, take it every day for 90 days, and judge it yourself. If you don’t see a difference, we’ll refund you, minus delivery. Skip, pause or cancel online whenever you like. We remind you 5 days before every payment.</p>")

# ---- 6. Objections, then the offer ----------------------------------------------------------
S["faq"] = copy(kit["faq"])
q = S["faq"]
tpl = copy(q["blocks"]["q1"])
faqs = [
    ("Will it work for me?",
     "<p>We won’t promise what it’ll do for you. Note your starting point, give it 90 days, and judge it yourself. If you don’t see a difference, you’re covered.</p>"),
    ("What’s actually in it?",
     "<p>19 ingredients, every dose on the label: 300mg NR (the most allowed in Great Britain), a full B complex, vitamin D3 and K2, zinc, copper, CoQ10 and more. Ask your AI, your GP, or Richie, who answers formula questions himself.</p>"),
    ("Is it worth the money?",
     "<p>Compare it with your cupboard, not with zero. MUTO is about £2 a day, in one routine instead of several separate pots, and you have 90 days to decide.</p>"),
    ("Am I locked into a subscription?",
     "<p>No. Skip, pause or cancel online, any time. We remind you 5 days before every payment.</p>"),
    ("Is it a stimulant?",
     "<p>No caffeine and no stimulants. This won’t give you energy in an hour. It’s a daily routine you judge over 90 days.</p>"),
    ("Is it safe with what I already take?",
     "<p>Usually, yes. If you take medicine, check with your GP first, and don’t stop anything you take for a medical reason.</p>"),
]
q["blocks"], q["block_order"] = {}, []
for i, (t, a) in enumerate(faqs, 1):
    b = copy(tpl)
    b["settings"].update(title=t, text=a)
    q["blocks"][f"q{i}"] = b
    q["block_order"].append(f"q{i}")
q["settings"]["heading"] = "Fair questions"

# ---- Close ------------------------------------------------------------------------------------
S["banner"] = copy(home["banner"])
S["banner"]["settings"].update(line_a="Not\ndone\nyet.", line_b="Start your\n90 days.")

S["sticky"] = copy(kit["sticky"])
S["sticky"]["settings"].update(sticky_cta_label=CTA, cta_link=PDP, sticky_label="NAD+ Cellular Complex",
                               sticky_sub="90 days to decide. Cancel any time.")

# ---- Easier reading (shared with the 45-55 product page) ---------------------------------------
css = open(os.path.join(SH, "pdp-45/easy-read.css")).read()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = "\n".join(l.strip() for l in css.splitlines() if l.strip())
S["easy_read"] = {"type": "custom-liquid",
                  "settings": {"custom_liquid": "<style>\n" + css + "\n</style>", "color_scheme": "scheme-1",
                               "padding_top": 0, "padding_bottom": 0}}

order = ["hero", "problem", "protocol", "results", "founder", "steps", "guarantee", "faq",
         "banner", "sticky", "easy_read"]
assert set(order) == set(S)
with open(out, "w") as fh:
    json.dump({"sections": S, "order": order}, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("wrote", out)
