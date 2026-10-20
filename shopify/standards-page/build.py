"""Our standards page: builds templates/page.standards.json from the copy doc
(MUTO_Our_Standards_Page_Copy_Oct26.docx) using the main site's own sections, the
ones the About page, home page and product page are built from (muto-about-*,
muto-home-*, muto-crea-*). Hero, board and banner settings are copied from the
About template (theme-ref/templates__page.about-muto.json) so imagery and
behaviour match it exactly.

Doc section → theme section:
  1 Hero            → muto-about-hero (poster, two actions, plan strip + sticky bar)
                      + muto-about-statement (subhead and the "regulated as food" intro)
                      + muto-about-made (the proof strip as the three evidence cards)
  2 Why we built it → muto-about-founder (portrait + letter card)
  3 Rules vs MUTO   → muto-crea-compare (MUTO vs UK law; the two unused columns hidden)
  4 Ten standards   → muto-crea-faq (ten open-able rows, no FAQ schema)
  5 Five jobs       → muto-crea-benefits (one panel: label photo + five rows)
  6 Scientists      → muto-home-board (the About page's board, with videos)
  7 Check us        → muto-about-proof (five steps)
  8 Questions       → muto-crea-faq
  9 Closing         → muto-about-banner ("Above the standard. Beneath the surface.")
The doc's [Confirm …] notes are left off the page; they're listed in README.md.

Usage: python3 build.py   (writes templates/page.standards.json)
"""
import copy, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ABOUT = json.loads(re.sub(r"^/\*.*?\*/", "", open(os.path.join(HERE, "theme-ref", "templates__page.about-muto.json")).read(), flags=re.S))["sections"]
PDP = "/products/muto-nad-cellular-complex"
CTA = "Start your 90 days"
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"

S, ORDER = {}, []


def add(key, type_, settings, blocks=None):
    sec = {"type": type_, "settings": settings}
    if blocks is not None:
        sec["blocks"] = dict(blocks)
        sec["block_order"] = [k for k, _ in blocks]
    S[key] = sec
    ORDER.append(key)


def from_about(key, **changes):
    sec = copy.deepcopy(ABOUT[key])
    sec["settings"].update(changes)
    return sec


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


# ---- 1. Hero, subhead, proof ----
hero = from_about("hero", heading="Our standards",
                  subheading="You shouldn’t have to take a supplement on trust.",
                  cta_label=CTA, cta_link=PDP,
                  ghost_label="See every ingredient and dose", ghost_link="/pages/ingredients",
                  plan_cta_label=CTA, sticky_cta_label=CTA,
                  schema_on=False)  # the About page already carries the organisation schema
S["hero"] = hero; ORDER.append("hero")

add("intro", "muto-about-statement", {
    "layout": "split", "field": "tail", "eyebrow": "Our standards",
    "head": "Supplements don’t\nhave to prove much\nto go on sale.",
    "tail": "",
    "body": "Food supplements in the UK are regulated as food. That keeps them safe to eat, but it asks for far less than most people assume. So we built MUTO to a higher bar, and we show you all of it.",
    "space_top": 100, "space_bottom": 60})

made = copy.deepcopy(ABOUT["made"])
made["settings"]["heading"] = "Built to a higher bar"
mb = made["blocks"]
order = made["block_order"]
mb[order[0]]["settings"].update(title="Six scientists, named",
                                text="Formulated by a PhD cell biologist and reviewed by a six-member scientific advisory board.")
mb[order[1]]["settings"].update(title="Every dose on the label",
                                text="No proprietary blends. Every ingredient, form and dose on the label, and on this page.")
mb[order[2]]["settings"].update(title="Every batch tested, made in the UK",
                                text="Made in the UK to GMP standards, in an ISO-certified facility. Every batch third-party tested, with a 90-day money-back guarantee.")
S["proof"] = made; ORDER.append("proof")

# ---- 2. Why we built it this way ----
add("founder", "muto-about-founder", {
    "image_fallback": CDN + "about-founder.jpg?v=1790751995",
    "image_alt": ABOUT["founder"]["settings"]["image_alt"],
    "heading": "Doing everything right,\nand still buying on\na leap of faith.",
    "name": "Dr Richie Barclay, Founder · PhD, cell biology and nutrition",
    "cta_label": CTA, "cta_link": PDP, "space_top": 100, "space_bottom": 100}, [
    ("p1", {"type": "para", "settings": {"text": "Most of the people I’ve worked with in their 40s and 50s were doing everything right. Training, eating well, taking their supplements. And they still felt it: gone by 3pm, nothing left for the people at home, sitting out the things they love."}}),
    ("p2", {"type": "para", "settings": {"text": "Most of what they took, they took on trust. Greens, a supermarket multivitamin, collagen, joint capsules. Labels that didn’t show the doses. Nobody checking every batch. No way to know if any of it was doing anything."}}),
    ("p3", {"type": "para", "settings": {"text": "I spent years in the lab studying why our bodies get less back from the same food and training as we age. Then years consulting people just like you. So when I built MUTO, I built it the way I’d want it built for my own family: nothing hidden, everything checkable."}}),
])

# ---- 3. What the rules ask for vs what we chose to do ----
RULES = [
    "Approval before it goes on sale",
    "Every dose on the label",
    "Independent testing of every batch",
    "Made in a GMP-certified facility",
    "A scientist involved",
    "Human research",
    "A money-back guarantee",
]
add("rules", "muto-crea-compare", {
    "heading": "Nobody made us do any\nof this. That’s the point.",
    "table_caption": "What UK law requires, and what MUTO does",
    "claim_label": "",
    "density": "compact", "head_gap": 40, "claim_width": 562, "col_pitch": 160, "panel_width": 120,
    "col_1": "MUTO", "col_1_logo": True, "col_2": "Required by UK law", "col_3": "", "col_4": "",
    "fit": "nad", "space_top": 70, "space_bottom": 70}, [
    (f"r{i}", {"type": "row", "settings": {"claim": c, "m1": "yes", "m2": "no", "m3": "dash", "m4": "dash"}})
    for i, c in enumerate(RULES, 1)
])

# ---- 4. Our ten standards ----
STANDARDS = [
    ("Every dose on the label",
     "No proprietary blends. Every one of the 19 ingredients is listed with its exact dose and form, so you know exactly what you’re taking.",
     "Read the full label, or turn the jar round."),
    ("Doses chosen for a reason",
     "NR at 300mg, the most allowed in Great Britain. Vitamin D3 at 2,000 IU. B vitamins in their active, methylated forms. Zinc and copper dosed as a pair, because they compete for absorption. Nothing added just to make the list longer.",
     "Every dose and form is in the ingredient table."),
    ("Only ingredients authorised in the UK",
     "Every ingredient in MUTO is authorised for use in UK food supplements. That’s why we use NR rather than NMN, which is still under assessment.",
     "Ask us about any ingredient’s status."),
    ("Every batch third-party tested",
     "Not just the first batch. Every batch is tested by an independent lab before it’s released.",
     "Certificates are available on request: <a href=\"mailto:hello@mutolongevity.com\">hello@mutolongevity.com</a>"),
    ("Made in the UK, to GMP",
     "Manufactured in the UK to GMP (Good Manufacturing Practice) standards, in an ISO-certified facility.",
     "Ask us for our manufacturing standards."),
    ("Nothing you don’t need",
     "Vegan capsules made from plant cellulose (HPMC). Vitamin D3 from algae. No major allergens, no fillers, no caffeine and no stimulants.",
     "It’s all on the label."),
    ("Scientists with names",
     "Formulated by Dr Richie Barclay, PhD in cell biology and nutrition, with a six-member scientific advisory board across sports nutrition, exercise physiology, public health and lifestyle medicine. The board meets every quarter to guide our research and every new formula. It doesn’t endorse products, and none of its members are presented as recommending MUTO for any medical purpose.",
     "Meet the board below."),
    ("Research we’ll publish, whatever it shows",
     "MUTO is part of independent university research: a University of Westminster study starts in December 2026, with work at King’s College London, Coventry and Newcastle to follow. There are no results yet, and we’ll never say there are.",
     "We’ll share every update on this page."),
    ("Honest claims only",
     "We only make the health claims UK law authorises, worded exactly. We’ll tell you what MUTO won’t do as clearly as what it will. Every review is genuine and invited from every customer, and every creator we work with is disclosed.",
     "Every claim on our site carries its authorised wording."),
    ("Built to be checked",
     "Note how you feel today: score your afternoons, or check your wearable. Give it 90 days. If you don’t feel the difference, you get every subscription payment back. Skip, pause or cancel online anytime, with a reminder five days before every payment.",
     "Guarantee terms are in our <a href=\"/pages/faqs#guarantee\">FAQs</a>."),
]
add("standards", "muto-crea-faq", {"heading": "Ten standards.\nAll of them checkable.", "schema_on": False, "space_top": 100, "space_bottom": 100}, [
    (f"s{i}", {"type": "q", "settings": {"title": f"{i}. {t}", "text": p(b, f"<strong>How to check:</strong> {c}")}})
    for i, (t, b, c) in enumerate(STANDARDS, 1)
])

# ---- 5. Five jobs, one jar ----
JOBS = [
    ("Energy", "Methylated B vitamins", "Help you feel less tired. Vitamins B6 and B12 contribute to the reduction of tiredness and fatigue."),
    ("Muscles and bones", "Vitamin D3 2,000 IU + K2 100µg", "Vitamin D contributes to normal muscle function. Vitamins D and K contribute to the maintenance of normal bones."),
    ("Immunity", "Zinc 15mg + copper 1mg, with D3", "Zinc, copper and vitamin D contribute to the normal function of the immune system."),
    ("NAD+", "NR 300mg", "Your body turns it into NAD+, which runs lower as we get older."),
    ("What ties it together", "CoQ10, resveratrol, grape seed, PQQ, TMG, BioPerine®", "CoQ10 150mg, trans-resveratrol 50mg, grape seed extract 150mg, PQQ 20mg, TMG 450mg and BioPerine® 5mg. Every dose on the label."),
]
add("jobs", "muto-crea-benefits", {"eyebrow": "Five jobs, one jar", "tablist_label": "Choose a view", "space_top": 96, "space_bottom": 100}, [
    ("panel", {"type": "panel", "settings": {
        "label": "Five jobs", "key": "jobs",
        "heading": "The foundation your\nbody runs on.",
        "lede": "Built for what you actually need in your 40s and 50s. Two capsules with breakfast. Alongside our creatine, free with your first order, it’s all you need to keep up.",
        "image_fallback": CDN + "about-made-declared.jpg?v=1790752124",
        "image_alt": "A close-up of the MUTO NAD+ Cellular Complex label showing every ingredient and dose",
        "cta_label": "See the full label", "cta_link": "/pages/ingredients"}}),
] + [
    (f"j{i}", {"type": "benefit", "settings": {"panel": "jobs", "title": t, "sub": s, "text": p(x)}})
    for i, (t, s, x) in enumerate(JOBS, 1)
])

# ---- 6. Meet the scientists ----
board = copy.deepcopy(ABOUT["board"])
board["settings"].update(heading="The people behind\nthe formula.",
                         note="A supplement doesn’t need a scientist anywhere near it. Ours has seven.")
S["board"] = board; ORDER.append("board")

# ---- 7. Check us yourself ----
add("check", "muto-about-proof", {
    "image_fallback": ABOUT["proof"]["settings"]["image_fallback"], "image_alt": ABOUT["proof"]["settings"]["image_alt"],
    "line_a": "Don’t take our\nword for it.", "line_b": "Check us\nyourself.", "space_top": 100, "space_bottom": 100}, [
    ("c1", {"type": "step", "settings": {"icon": "target", "title": "Read the Label", "text": "Every ingredient, every dose, on the jar and on our ingredients page."}}),
    ("c2", {"type": "step", "settings": {"icon": "infinity", "title": "Ask Someone Else", "text": "Paste it into ChatGPT, or show it to your GP, pharmacist or nutritionist."}}),
    ("c3", {"type": "step", "settings": {"icon": "orbit", "title": "Ask for a Certificate", "text": "Batch certificates on request: hello@mutolongevity.com"}}),
    ("c4", {"type": "step", "settings": {"icon": "heart", "title": "Ask Richie", "text": "Anything about the formula. He answers formula questions himself."}}),
    ("c5", {"type": "step", "settings": {"icon": "gauge", "title": "Give it 90 Days", "text": "Then judge it for yourself. Not for you? Get every subscription payment back."}}),
])

# ---- 8. Questions about our standards ----
FAQ = [
    ("Is MUTO tested for banned substances?", "Every batch of MUTO is third-party tested. We don’t currently make a banned-substance certification claim, and we’ll update this page if that changes."),
    ("Can I see your test results?", "Yes. Batch certificates are available on request: <a href=\"mailto:hello@mutolongevity.com\">hello@mutolongevity.com</a>."),
    ("Why NR and not NMN?", "NR is authorised for food supplements in Great Britain, at up to 300mg a day for adults. NMN is still under novel food assessment. We only use ingredients that are authorised in the UK."),
    ("Why 19 ingredients?", "Because the five jobs need them, and each one has its dose on the label. Nothing is there to make the list longer."),
    ("Has MUTO been clinically proven?", "No, and we won’t say it has. Our first human study starts in December 2026 at the University of Westminster. We’ll publish the results, whatever they show."),
    ("What won’t MUTO do?", "It won’t make you 25 again, replace sleep, training or a decent diet, or work overnight. It isn’t a stimulant. It’s a daily foundation, and most people give it 60 to 90 days."),
    ("Is it safe with medication?", "Check with your GP or pharmacist first if you take any prescription medicine. MUTO contains vitamin K2, which can affect blood thinners such as warfarin. We’re happy to send the full label to share with your doctor."),
    ("Anything else?", "Everything else, from delivery to your subscription, is in our <a href=\"/pages/faqs\">full FAQs</a>."),
]
add("faq", "muto-crea-faq", {"heading": "Questions about\nour standards.", "schema_on": True, "space_top": 100, "space_bottom": 100}, [
    (f"q{i}", {"type": "q", "settings": {"title": q, "text": p(a)}}) for i, (q, a) in enumerate(FAQ, 1)
])

# ---- 9. Closing ----
S["banner"] = from_about("banner", cta_label=CTA, cta_link=PDP); ORDER.append("banner")

# The comparison table has four columns; this page uses two
add("page_css", "custom-liquid", {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid": """<style>
[id$="__rules"] .mc__cmp th:nth-child(n+4),[id$="__rules"] .mc__cmp td:nth-child(n+4){display:none}
</style>"""})

out = os.path.join(HERE, "templates", "page.standards.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
