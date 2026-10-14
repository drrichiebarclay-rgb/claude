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

# Images reused from the creatine-kit product page and the home page
B = kit["buy"]["blocks"]
img = lambda k: B[k]["settings"].get("image_fallback", "")
SHOP_NAD = home["shop"]["blocks"]["pn"]["settings"].get("image_fallback", "")

# ---- 1. Hero: product photo | offer copy ---------------------------------------
S["lp_hero"] = {"type": "muto-lp-hero", "settings": {
    "image_fallback": img("g1"),
    "image_alt": B["g1"]["settings"].get("image_alt", "The MUTO NAD+ Cellular Complex set"),
    "rating_text": "Rated 4.83 from 150+ reviews",
    "heading": "Same training.\nSlower recovery.\nIt’s not your discipline.",
    "body": "<p>MUTO is the daily cellular protocol for people who still train: two capsules with breakfast, 19 ingredients, every dose on the label. Start now and your first order includes a free welcome kit, with Ultrapure Creatine.</p>",
    "strong": "Two capsules. One routine. 90 days to judge it yourself.",
    "cta_label": CTA, "cta_link": PDP,
    "ticks": "Free next-day delivery\n90-day money-back guarantee"}}

# ---- 2. Trust strip + the people it's for -----------------------------------------
S["trust"] = {"type": "muto-lp-trust", "settings": {
    "heading": "Built for people who still train,\nstill work, and aren’t done yet."},
    "blocks": {}, "block_order": []}
for i, (icon, text) in enumerate([("award", "Built by a PhD cell biologist"),
                                  ("shield", "Made in the UK, every batch third-party tested"),
                                  ("flask", "Research underway with 4 UK universities")], 1):
    S["trust"]["blocks"][f"t{i}"] = {"type": "item", "settings": {"icon": icon, "text": text}}
    S["trust"]["block_order"].append(f"t{i}")
for k in ("w1", "w2", "w3", "w4"):
    st_ = B[k]["settings"]
    S["trust"]["blocks"][f"p{k}"] = {"type": "photo", "settings": {
        "image_fallback": st_.get("image_fallback", ""), "alt": st_.get("image_alt", ""),
        "position": st_.get("image_position", "")}}
    S["trust"]["block_order"].append(f"p{k}")

# ---- 3. Problem framing (added above benefits) ---------------------------------------
S["problem"] = {"type": "muto-lp-problem", "settings": {
    "pill": "Sound familiar?",
    "heading": "When did Sunday start lasting until Wednesday?",
    "lede": "You’re fitter than most people your age, and you still turn up. But the session that used to be gone by Monday now hangs around for days. More rest isn’t fixing it, and neither is the cupboard of supplements.",
    "reframe_heading": "It’s not your discipline.\nIt starts underneath.",
    "reframe_text": "Recovery is where ageing tends to show up first, in the cells that make your energy. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients, in one daily routine you can check yourself."},
    "blocks": {}, "block_order": []}
for i, (q_, t_) in enumerate([
        ("“I need longer to recover than I used to.”", "Same training. Same sleep. Slower bounce-back."),
        ("“My legs are still heavy on Sunday.”", "Thursday’s session hasn’t left yet."),
        ("“A cupboard full of pots.”", "Five supplements, and no idea which one’s working.")], 1):
    S["problem"]["blocks"][f"x{i}"] = {"type": "pain", "settings": {"quote": q_, "text": t_}}
    S["problem"]["block_order"].append(f"x{i}")

# ---- 4. Benefits: plain-English benefit + the authorised claim, worded exactly -------
S["benefits"] = {"type": "muto-lp-benefits", "settings": {
    "heading": "What’s working underneath.", "foot": ""}, "blocks": {}, "block_order": []}
for i, (title, claim) in enumerate([
        ("Steadier energy, all day.", "Vitamins B6, B12 and folate contribute to the reduction of tiredness and fatigue."),
        ("Energy made in your cells.", "Thiamin, riboflavin, niacin, vitamins B6 and B12, and copper contribute to normal energy-yielding metabolism."),
        ("Built for people who train.", "Vitamin D contributes to the maintenance of normal muscle function."),
        ("Protection from everyday wear.", "Zinc, copper and riboflavin contribute to the protection of cells from oxidative stress.")], 1):
    S["benefits"]["blocks"][f"b{i}"] = {"type": "benefit", "settings": {"title": title, "text": claim}}
    S["benefits"]["block_order"].append(f"b{i}")

# ---- 5. Value: a cupboard of pots vs two capsules ----------------------------------------
S["value"] = {"type": "muto-lp-value", "settings": {
    "heading": "19 ingredients.\nTwo capsules.",
    "body": "Most supplements cover one thing. Add more and the cupboard fills up fast, with no way to tell what’s working. MUTO puts 19 ingredients in one daily routine, every dose on the label.",
    "more_label": "See every dose",
    "more_list": "\n".join([
        "Nicotinamide riboside (NR) | 300mg", "Trimethylglycine (TMG) | 450mg", "Coenzyme Q10 | 150mg",
        "Grapeseed extract | 150mg", "Trans-resveratrol | 50mg", "PQQ | 20mg", "Vitamin D3 | 2000IU",
        "Vitamin K2 (MK-7) | 100µg", "Thiamin (B1) | 5mg", "Riboflavin (B2) | 5mg", "Niacin (B3) | 16mg NE",
        "Pantothenic acid (B5) | 10mg", "Vitamin B6 (P5P) | 5mg", "Folate | 400µg", "Vitamin B12 | 100µg",
        "Biotin | 300µg", "Zinc bisglycinate | 15mg", "Copper bisglycinate | 1mg", "BioPerine® | 5mg"]),
    "without_placeholder": "Photo needed: a cupboard of supplement pots",
    "without_label": "Without MUTO: a cupboard of separate pots",
    "without_price": "£3.30+",
    "with_image_fallback": SHOP_NAD, "with_image_alt": "A jar of MUTO NAD+ Cellular Complex",
    "with_label": "With MUTO: two capsules a day",
    "with_price": "£2",
    "cta_label": CTA, "cta_link": PDP,
    "foot": "£3.30+ a day is the £100+ a month buyers told us they spent on supplements before MUTO. MUTO is £60 a month on subscription."}}

# ---- 6. The offer, itemised ------------------------------------------------------------------
S["offer"] = {"type": "muto-lp-offer", "settings": {
    "image_fallback": img("g1"), "image_alt": B["g1"]["settings"].get("image_alt", ""),
    "heading": "Start your 90 days today.",
    "product_name": "NAD+ Cellular Complex (30 days)", "product_price": "£60",
    "product_sub": "£2 a day on subscription. Usually £70.",
    "includes_label": "First order includes:",
    "total_was": "£132", "total_now": "£60",
    "cta_label": CTA, "cta_link": PDP,
    "ticks": "Free next-day delivery\nSkip, pause or cancel online\n90-day money-back guarantee"},
    "blocks": {}, "block_order": []}
for i, (name, desc, was) in enumerate([
        ("Ultrapure Creatine", "Micronised creatine monohydrate, every batch tested", "£30"),
        ("Performance Socks", "Size UK 6–11", "£12"),
        ("Forever Jar", "Refill it from the pouch every month", "£10"),
        ("12-Week Protocol Guide", "How to run your 90 days and check it yourself", "£10"),
        ("Garmin watch prize draw", "Entry into our quarterly draw", "")], 1):
    S["offer"]["blocks"][f"i{i}"] = {"type": "item", "settings": {"name": name, "desc": desc, "was": was,
                                                                  "now": "free" if was else "included"}}
    S["offer"]["block_order"].append(f"i{i}")

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

order = ["lp_hero", "trust", "problem", "benefits", "value", "offer",
         "results", "founder", "steps", "guarantee", "faq", "banner", "bar", "easy_read"]
assert set(order) == set(S)
with open(out, "w") as fh:
    json.dump({"sections": S, "order": order}, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("wrote", out)
