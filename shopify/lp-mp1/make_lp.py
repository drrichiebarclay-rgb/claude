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
# Persona images: the 45-55 photos on the live -2 product page (product.muto-nad-45.json,
# snapshot in live-snapshot/) and its lead product image.
P45 = load("lp-mp1/live-snapshot/templates__product.muto-nad-45.json")["sections"]
M2_LEAD = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/newmain.png?v=1791796643"
# The current offer image on the main PDP (Garmin prize draw)
OFFER_IMG = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/new_garmin.png?v=1791890671"
pimg = lambda sec, blk: P45[sec]["blocks"][blk]["settings"].get("image", "") if blk else P45[sec]["settings"].get("image", "")

# ---- 1. Hero: product photo | offer copy ---------------------------------------
S["lp_hero"] = {"type": "muto-lp-hero", "settings": {
    "image_fallback": "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/muto-lp-kit-hero.jpg?v=1791969959",
    "image_alt": "The MUTO welcome kit: NAD+ Cellular Complex jar and refill pouches, Ultrapure Creatine, the bottle and the presentation box",
    "image_position": "55% 62%",
    "schema_on": True, "schema_product": "muto-nad-cellular-complex-2",
    "schema_name": "MUTO NAD+ Cellular Complex",
    "schema_description": "A daily cellular protocol for people who still train: two capsules with breakfast, 19 ingredients including 300mg nicotinamide riboside (NR), every dose on the label. Made in the UK, every batch third-party tested, with a 90-day money-back guarantee for subscribers.",
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
for i, (sec, blk) in enumerate([("problem", "c2"), ("benefits", "pf"), ("problem", "c1"), ("steps", "s4")], 1):
    S["trust"]["blocks"][f"ph{i}"] = {"type": "photo", "settings": {
        "image": pimg(sec, blk), "alt": "A MUTO customer in their 40s or 50s, still training"}}
    S["trust"]["block_order"].append(f"ph{i}")

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
    "without_pots": "Vitamin B complex\nVitamin D3\nVitamin K2\nZinc\nCopper\nCoQ10\nNR\nTMG\nResveratrol\nPQQ\nGrapeseed",
    "without_label": "Without MUTO: separate pots",
    "without_price": "£3.30+",
    "with_image": "", "with_image_fallback": "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/nad-problem-box.jpg?v=1791018999",
    "with_image_alt": "The MUTO NAD+ Cellular Complex box open, with the jar inside",
    "with_label": "With MUTO: two capsules",
    "with_price": "£2",
    "cta_label": CTA, "cta_link": PDP,
    "foot": "£3.30+ a day is the £100+ a month buyers told us they spent on supplements before MUTO. MUTO is £60 a month on subscription."}}

# ---- 6. The offer, itemised ------------------------------------------------------------------
S["offer"] = {"type": "muto-lp-offer", "settings": {
    "image": "", "image_fallback": OFFER_IMG,
    "image_alt": "Everything in your first MUTO order: NAD+ Cellular Complex and Forever Jar, Ultrapure Creatine, socks, the 12-Week Protocol Guide and entry to win a Garmin watch",
    "heading": "Start your 90 days today.",
    "product_name": "NAD+ Cellular Complex and Forever Jar (30 days)", "product_price": "£60",
    "product_sub": "£2 a day on subscription. Usually £70.",
    "includes_label": "First order includes:",
    "total_was": "£122", "total_now": "£60",
    "cta_label": CTA, "cta_link": PDP,
    "ticks": "More free gifts along the way\nFree next-day delivery\nSkip, pause or cancel online\n90-day money-back guarantee"},
    "blocks": {}, "block_order": []}
for i, (name, desc, was) in enumerate([
        ("Ultrapure Creatine", "Micronised creatine monohydrate, every batch tested", "£30"),
        ("Performance Socks", "Size UK 6–11", "£12"),
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
    "text": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
    "cta_label": CTA, "cta_sub": "Save 14%", "cta_link": PDP}}

# ---- 7. Formula proof (honest version: research under way, one cited NR study) -------
WHY = kit["why"]["blocks"]
S["formula"] = {"type": "muto-lp-formula", "settings": {
    "heading": "One formula, built to be checked.",
    "body": "Most supplements never test their formula as a complete product. MUTO is being studied with four UK universities, and we’ll publish what we find, whatever it shows. Until then, every dose is on the label, and you get 90 days to check it yourself.",
    "image_fallback": SHOP_NAD,
    "image_alt": "A jar of MUTO NAD+ Cellular Complex",
    "source": "* Conze et al., 2019. NR taken on its own, not MUTO. MUTO contains 300mg NR, the most allowed in Great Britain."},
    "blocks": {}, "block_order": []}
for i, (fig, unit, text) in enumerate([
        ("51%", "in 14 days*", "300mg of NR a day raised blood NAD+ by 51% in 14 days in a published study."),
        ("4", "universities", "Westminster, King’s College London, Coventry and Newcastle are researching MUTO."),
        ("90", "days", "To judge it yourself. If you don’t see a difference, you’re covered.")], 1):
    S["formula"]["blocks"][f"f{i}"] = {"type": "stat", "settings": {"figure": fig, "unit": unit, "text": text}}
    S["formula"]["block_order"].append(f"f{i}")

# ---- 8. Real customer reviews (the store's Reviews.io widget) -------------------------
S["reviews"] = copy(kit["custom_reviews_KpXTpD"])
rv = S["reviews"]["settings"]
rv["heading"] = "<p>Energy, recovery, routine: what customers say about MUTO</p>"
rv["bg_color"] = "#ffffff"
rv["show_button"] = False
rc = rv["review_content"]
for old, new in [("enable_rich_snippets: true", "enable_rich_snippets: false"),
                 ("per_page: 15", "per_page: 6"),
                 ("enable_sentiment_analysis: true", "enable_sentiment_analysis: false"),
                 ("enable: true, //Show filtering options", "enable: false, //Show filtering options"),
                 ("enable_text_search: true", "enable_text_search: false"),
                 ("enable_sorting: true", "enable_sorting: false"),
                 ("enable_write_review: true", "enable_write_review: false"),
                 ("enable_sub_header: true", "enable_sub_header: false")]:
    assert old in rc, old
    rc = rc.replace(old, new)
rv["review_content"] = rc
rv["padding_top"] = 80
rv["padding_bottom"] = 40
rv["show_review_bar"] = False

# ---- 9. Athletes and experts ------------------------------------------------------------
BOARD = kit["board"]["blocks"]
S["experts"] = {"type": "muto-lp-experts", "settings": {"heading": "Trusted by athletes.\nReviewed by experts."},
                "blocks": {}, "block_order": []}
people = [{"image_fallback": home["founder"]["settings"]["image_fallback"], "alt": "Dr Richie Barclay holding a jar of MUTO",
           "name": "Dr Richie Barclay, PhD", "role": "Founder · cell biologist",
           "quote": "“I built MUTO because I was tired of supplements that ask you to take them on trust. So every ingredient and every dose is on the label.”"}]
for k in ("m1", "m2", "m3", "m4"):
    bs = BOARD[k]["settings"]
    people.append({"image": bs.get("image", ""), "image_fallback": bs.get("image_fallback", ""),
                   "alt": bs["name"], "name": bs["name"],
                   "role": bs["role"].capitalize() + " · Scientific Advisory Board", "quote": ""})
for k in ("w1", "w2", "w3", "w4"):
    bs = B[k]["settings"]
    people.append({"image_fallback": bs.get("image_fallback", ""), "alt": bs.get("image_alt", ""),
                   "position": bs.get("image_position", ""), "name": bs["name"], "role": "MUTO athlete", "quote": ""})
# What each person brings, in MUTO's voice. Not quotes: replace with their own approved
# words when they come back.
ROLE_LINES = {
    "Dr James Morehen": "Advises MUTO on performance nutrition for people who still train hard.",
    "Dr Alka Patel": "Advises MUTO on longevity: helping people keep doing what they love for longer.",
    "Dr Richard Mackenzie": "Advises MUTO on metabolism: how your cells turn food into energy.",
    "Dr Maciej Zatonski": "Advises MUTO on sleep and recovery, and on reading them over weeks, not nights.",
    "Harry Insley": "Runner and MUTO athlete.",
    "Yolanda King": "MUTO athlete.",
    "Kaisa Larkas": "HYROX athlete and MUTO athlete.",
    "Sam Ekstrom": "Time-trial cyclist and MUTO athlete.",
}
for pp in people:
    if not pp.get("quote"):
        pp["quote"] = ROLE_LINES.get(pp["name"], "")
        if pp["role"] == "MUTO athlete":
            pp["role"] = "Athlete"
for i, pp in enumerate(people, 1):
    S["experts"]["blocks"][f"e{i}"] = {"type": "person", "settings": pp}
    S["experts"]["block_order"].append(f"e{i}")

# ---- 10. FAQ ----------------------------------------------------------------------------
S["lp_faq"] = {"type": "muto-lp-faq", "settings": {"heading": "You’ve got questions?\nWe’ve got answers.",
                                                   "open_first": True, "schema_on": True},
               "blocks": {}, "block_order": []}
for i, (q_, a_) in enumerate([
        ("What is MUTO?", "<p>A daily cellular protocol for people who still train and aren’t done yet. Two capsules with breakfast, 19 ingredients, every dose on the label. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients.</p>"),
        ("Which ingredients are in MUTO?", "<p>300mg NR (the most allowed in Great Britain), 450mg TMG, 150mg CoQ10, a methylated B complex, vitamin D3 and K2, zinc, copper, PQQ, grapeseed, trans-resveratrol and BioPerine®. Every dose is on the label. Ask your AI, your GP or Richie, who answers formula questions himself.</p>"),
        ("How do I know if MUTO is right for me?", "<p>Try it. Note how you feel before you start, or take a 7-day average if you wear a watch. Give it 90 days, then compare. If you don’t see a difference, you’re covered.</p>"),
        ("What does MUTO replace?", "<p>For many customers, several separate pots: B vitamins, vitamin D, K2, zinc and CoQ10 are all in here, at the doses shown. Don’t stop anything you take for a medical reason, and check with your GP if you take medicine.</p>"),
        ("How do I take it?", "<p>Two capsules with breakfast, every day. No caffeine and no stimulants, so there’s nothing to time around training.</p>"),
        ("Can I cancel?", "<p>Yes. Skip, pause or cancel online, any time. We remind you 5 days before every payment.</p>")], 1):
    S["lp_faq"]["blocks"][f"q{i}"] = {"type": "q", "settings": {"q": q_, "a": a_}}
    S["lp_faq"]["block_order"].append(f"q{i}")

# ---- 11. Second offer, after the FAQ --------------------------------------------------
S["offer2"] = copy(S["offer"])
S["offer2"]["settings"].update(
    heading="Ready when you are.",
    image="", image_fallback=OFFER_IMG)

# Superseded by the AG1-style sections above
for k in ("results", "founder", "steps", "guarantee", "faq", "banner", "easy_read"):
    S.pop(k, None)

# ---- Easier reading (shared with the 45-55 product page) ---------------------------------------
css = open(os.path.join(SH, "pdp-45/easy-read.css")).read()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = "\n".join(l.strip() for l in css.splitlines() if l.strip())
S["easy_read"] = {"type": "custom-liquid",
                  "settings": {"custom_liquid": "<style>\n" + css + "\n</style>", "color_scheme": "scheme-1",
                               "padding_top": 0, "padding_bottom": 0}}

S.pop("easy_read", None)
order = ["lp_hero", "trust", "problem", "benefits", "value", "offer",
         "formula", "reviews", "experts", "lp_faq", "offer2", "bar"]
assert set(order) == set(S)
with open(out, "w") as fh:
    json.dump({"sections": S, "order": order}, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("wrote", out)
