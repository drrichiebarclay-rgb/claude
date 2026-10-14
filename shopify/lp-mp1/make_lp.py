"""Build the MP1 (Slowing Competitor) Meta top-of-funnel landing page:
page.lp-mp1.json, a page template (the home hero, founder and banner
sections only run on page and home templates). Assign it to a page such as
/pages/not-done-yet; preview on any page with ?view=lp-mp1.

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
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "page.lp-mp1.json")


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

# Images reused from the creatine-kit product page
B = kit["buy"]["blocks"]
img = lambda k: B[k]["settings"].get("image_fallback", "")
FOUNDER = home["founder"]["settings"]["image_fallback"]

# ---- 1. Offer hero (IM8-style split: kit panel + offer copy) ---------------------
S["lp_hero"] = {"type": "muto-lp-hero", "settings": {
    "kit_title": "Your £62 welcome kit.\nOn us.",
    "main_image_fallback": img("g1"),
    "main_image_alt": B["g1"]["settings"].get("image_alt", "The MUTO NAD+ Cellular Complex set"),
    "badge_mark": "<strong>PhD</strong>Formulated",
    "badge_text": "By Dr Richie Barclay, cell biologist. Reviewed by our Scientific Advisory Board.",
    "heading": "The £62 welcome kit.\nFree with your first subscription.",
    "heading_accent": "Start your 90 days.",
    "body": "<p>Same training, slower recovery? It’s not your discipline. It starts underneath. MUTO is one daily protocol for people who aren’t done yet: two capsules with breakfast, every dose on the label, and 90 days to judge it yourself.</p>",
    "rating": "4.83", "reviews": "150+ reviews",
    "proof_image_fallback": FOUNDER,
    "proof_text": "<p><strong>Built by a scientist you can talk to.</strong> Richie answers formula questions himself. <a href=\"#mlp-doses-doses\">See every dose</a></p>",
    "cta_label": CTA, "cta_sub": "Save 14% + free welcome kit", "cta_link": PDP,
    "cta_note": "90-day money-back guarantee · Skip, pause or cancel online"},
    "blocks": {}, "block_order": []}
for key, name, was in [("k0", "Ultrapure Creatine", "£30"), ("k1", "Performance Socks", "£12"),
                       ("k2", "Forever Jar", "£10"), ("k3", "12-Week Protocol Guide", "£10")]:
    S["lp_hero"]["blocks"][key] = {"type": "gift", "settings": {
        "image_fallback": img(key), "image_alt": B[key]["settings"].get("image_alt", name),
        "name": name, "was": was, "now": "Free"}}
    S["lp_hero"]["block_order"].append(key)

# ---- 2. Stats band (press logos row stays hidden until logos are added) -----------
S["stats"] = {"type": "muto-lp-stats", "settings": {"press_label": "As featured in", "stats_label": "MUTO in numbers"},
              "blocks": {}, "block_order": []}
for i, (fig, label) in enumerate([("19", "Ingredients, every dose on the label"),
                                  ("300mg", "NR, the most allowed in Great Britain"),
                                  ("90 days", "To decide, or your money back"),
                                  ("4.83★", "From 150+ reviews")], 1):
    S["stats"]["blocks"][f"st{i}"] = {"type": "stat", "settings": {"figure": fig, "label": label}}
    S["stats"]["block_order"].append(f"st{i}")

# ---- 3. The supplement problem: old way vs the MUTO way -----------------------------
S["compare"] = {"type": "muto-lp-compare", "settings": {
    "pill": "The supplement problem",
    "heading": "Too many pots.", "heading_accent": "Too little proof.",
    "sub": "Most people take a cupboard of supplements and still aren’t sure any of them work. MUTO is built to be checked.",
    "old_title": "The old way",
    "old_items": "5+ separate pots, pills and powders\nProprietary blends with hidden doses\nSingle ingredients at token doses\n£100+ a month and a cupboard full of clutter\nNo way to tell if any of it is working",
    "new_title": "The MUTO way",
    "new_items": "Two capsules with breakfast. That’s it.\nEvery dose on the label. No proprietary blends.\n300mg NR, the most allowed in Great Britain\nOne routine, about £2 a day\n90 days to check it yourself, or your money back",
    "cta_label": CTA, "cta_link": PDP}}

# ---- 4. What people notice (customer words until survey figures are supplied) -------
S["notice"] = {"type": "muto-lp-cards", "settings": {
    "tint": True, "pill": "Real people, real check-ins",
    "heading": "What people notice", "heading_accent": "in their own words",
    "foot": "Individual experiences. We won’t promise what MUTO will do for you."},
    "blocks": {}, "block_order": []}
for i, (title, quote, who) in enumerate([
        ("Afternoons", "“No afternoon slump and in general feeling great”", "Lynda, MUTO customer"),
        ("Recovery", "“Has actually changed my recovery”", "Adam H, MUTO customer"),
        ("Training", "“I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often”", "Ayo P, MUTO customer")], 1):
    S["notice"]["blocks"][f"n{i}"] = {"type": "card", "settings": {"figure": "", "title": title, "text": quote, "cite": who}}
    S["notice"]["block_order"].append(f"n{i}")

# ---- 5. Full transparency: the doses -------------------------------------------------------
S["doses"] = {"type": "muto-lp-doses", "settings": {
    "pill": "Full transparency", "heading": "Every dose.", "heading_accent": "Nothing hidden.",
    "sub": "A few of the 19 ingredients in two capsules, every dose printed on the label.",
    "tags": "Energy-yielding metabolism\nTiredness and fatigue\nMuscle function\nNormal bones\nCell protection",
    "foot": "Ask your AI, your GP or Richie what’s in it."},
    "blocks": {}, "block_order": []}
for i, (amt, name, role) in enumerate([
        ("300mg", "Nicotinamide riboside (NR)", "the NAD+ building block"),
        ("450mg", "TMG", "works alongside NR"),
        ("150mg", "CoQ10", "found in every cell"),
        ("2000IU", "Vitamin D3", "normal muscle function"),
        ("100µg", "Vitamin K2 (MK-7)", "works alongside D3"),
        ("8 B vitamins", "Methylated B complex", "normal energy-yielding metabolism"),
        ("15mg", "Zinc", "protects cells from oxidative stress"),
        ("50mg", "Trans-resveratrol", "a plant polyphenol")], 1):
    S["doses"]["blocks"][f"d{i}"] = {"type": "dose", "settings": {"amount": amt, "name": name, "role": role}}
    S["doses"]["block_order"].append(f"d{i}")

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

S["bar"] = {"type": "muto-lp-bar", "settings": {
    "text": "Welcome offer: a free £62 welcome kit with your first subscription, and 90 days to decide.",
    "cta_label": CTA, "cta_sub": "Save 14%", "cta_link": PDP}}

# ---- Easier reading (shared with the 45-55 product page) ---------------------------------------
css = open(os.path.join(SH, "pdp-45/easy-read.css")).read()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = "\n".join(l.strip() for l in css.splitlines() if l.strip())
S["easy_read"] = {"type": "custom-liquid",
                  "settings": {"custom_liquid": "<style>\n" + css + "\n</style>", "color_scheme": "scheme-1",
                               "padding_top": 0, "padding_bottom": 0}}

order = ["lp_hero", "stats", "compare", "notice", "doses",
         "results", "founder", "steps", "guarantee", "faq", "banner", "bar", "easy_read"]
assert set(order) == set(S)
with open(out, "w") as fh:
    json.dump({"sections": S, "order": order}, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("wrote", out)
