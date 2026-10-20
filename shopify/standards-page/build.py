"""Our standards page: builds templates/page.standards.json from the copy doc
(MUTO_Our_Standards_Page_Copy_Oct26.docx), using only the existing MUTO landing-page
sections (muto-lp-*), so it carries the same design system as the landing pages.

Section map (doc section → theme section):
  1 Hero            → muto-lp-article-hero, then muto-lp-trust as the 5-item proof strip
  2 Why we built it → muto-lp-article + muto-lp-reasons (founder "person" block)
  3 Rules vs MUTO   → muto-lp-article + muto-lp-reasons ("compare" block)
  4 Ten standards   → muto-lp-article + muto-lp-reasons (10 numbered reasons, "How to check" panels)
  5 Five jobs       → muto-lp-article + muto-lp-reasons (compare + callout + button), anchor #ingredients
  6 Scientists      → muto-lp-article + muto-lp-experts
  7 Check us        → muto-lp-article + muto-lp-reasons (5 numbered steps + email button)
  8 Questions       → muto-lp-faq-2
  9 Closing CTA     → muto-lp-article + muto-lp-reasons (button), plus muto-lp-bar
The doc's [Confirm …] notes are left out of the page; they're listed in README.md.

Usage: python3 build.py   (writes templates/page.standards.json)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PDP = "/products/muto-nad-cellular-complex"
CTA = "Start your 90 days"
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"
KIT = CDN + "muto-lp-kit-hero.jpg?v=1791969959"
KIT_ALT = "The MUTO welcome kit: NAD+ Cellular Complex jar and refill pouches, Ultrapure Creatine, the bottle and the presentation box"
FOUNDER = CDN + "about-founder.jpg?v=1790751995"

S, ORDER = {}, []


def add(key, type_, settings=None, blocks=None):
    sec = {"type": type_, "settings": settings or {}}
    if blocks is not None:
        sec["blocks"] = {k: b for k, b in blocks}
        sec["block_order"] = [k for k, _ in blocks]
    S[key] = sec
    ORDER.append(key)


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


# ---- 1. Hero ----
add("hero", "muto-lp-article-hero", {
    "image_fallback": KIT, "image_alt": KIT_ALT, "image_position": "55% 62%",
    "kicker": "Our standards",
    "heading": "You shouldn’t have to take a supplement on trust.",
    "sub": "Supplements don’t have to prove much to go on sale in the UK. So we built MUTO to a higher bar, and we show you all of it.",
    "cta_label": CTA, "cta_link": PDP,
    "jump_label": "See every ingredient and dose", "jump_target": "#ingredients",
}, [])
add("proof", "muto-lp-trust", {"heading": ""}, [
    ("t1", {"type": "item", "settings": {"icon": "label", "text": "Every dose on the label"}}),
    ("t2", {"type": "item", "settings": {"icon": "flask", "text": "Every batch third-party tested"}}),
    ("t3", {"type": "item", "settings": {"icon": "shield", "text": "Made in the UK to GMP"}}),
    ("t4", {"type": "item", "settings": {"icon": "award", "text": "Six scientists on our advisory board"}}),
    ("t5", {"type": "item", "settings": {"icon": "shield", "text": "90-day money-back guarantee"}}),
])

# ---- 2. Why we built it this way ----
add("why", "muto-lp-article", {
    "heading": "Doing everything right, and still buying on a leap of faith.",
    "body": p("Most of the people I’ve worked with in their 40s and 50s were doing everything right. Training, eating well, taking their supplements. And they still felt it: gone by 3pm, nothing left for the people at home, sitting out the things they love.",
              "Most of what they took, they took on trust. Greens, a supermarket multivitamin, collagen, joint capsules. Labels that didn’t show the doses. Nobody checking every batch. No way to know if any of it was doing anything."),
})
add("why_founder", "muto-lp-reasons", {"anchor": "founder"}, [
    ("f1", {"type": "person", "settings": {
        "label": "Why I built MUTO", "image_fallback": FOUNDER, "position": "50% 20%",
        "quote": "I spent years in the lab studying why our bodies get less back from the same food and training as we age. Then years consulting people just like you. So when I built MUTO, I built it the way I’d want it built for my own family: nothing hidden, everything checkable.",
        "name": "Dr Richie Barclay, Founder", "role": "PhD, cell biology and nutrition"}}),
])

# ---- 3. What the rules ask for vs what we chose to do ----
add("rules", "muto-lp-article", {
    "heading": "Nobody made us do any of this. That’s the point.",
    "body": p("Food supplements in the UK are regulated as food. That keeps them safe to eat, but it asks for far less than most people assume. Here’s the gap."),
})
RULES = [
    ("Approval before it goes on sale", "✕ No", "✓ Formulated by a PhD cell biologist and reviewed by a six-member scientific advisory board"),
    ("Every dose on the label", "✕ No: “proprietary blends” are allowed", "✓ Every ingredient, every dose, on the label and on this page"),
    ("Independent testing of every batch", "✕ No", "✓ Every batch third-party tested. Certificates available on request"),
    ("Made in a GMP-certified facility", "✕ No", "✓ Made in the UK to GMP standards, in an ISO-certified facility"),
    ("A scientist involved", "✕ No", "✓ A PhD founder and six named scientists"),
    ("Human research", "✕ No", "✓ Our first human study starts in December 2026, with more university research to follow"),
    ("A guarantee", "✕ No", "✓ 90 days, or your money back"),
]
add("rules_table", "muto-lp-reasons", {"anchor": "the-rules"}, [
    ("c1", {"type": "compare", "settings": {
        "heading": "", "col1": "", "col2": "Required by UK law?", "col3": "What MUTO does",
        "rows": "\n".join(" | ".join(r) for r in RULES), "note": ""}}),
])

# ---- 4. Our ten standards ----
add("standards_head", "muto-lp-article", {
    "heading": "Ten standards. All of them checkable.",
    "body": p("Each one is a plain promise, why it matters, and how you can check it yourself."),
})
STANDARDS = [
    ("Every dose on the label",
     "No proprietary blends. Every one of the 19 ingredients is listed with its exact dose and form, so you know exactly what you’re taking.",
     "Read the full label below, or turn the jar round."),
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
     "Formulated by Dr Richie Barclay, PhD in cell biology and nutrition, with a six-member scientific advisory board across sports nutrition, exercise physiology, public health and lifestyle medicine. The board meets every quarter to guide our research and every new formula.",
     "Meet the board below."),
    ("Research we’ll publish, whatever it shows",
     "MUTO is part of independent university research: a University of Westminster study starts in December 2026, with work at King’s College London, Coventry and Newcastle to follow. There are no results yet, and we’ll never say there are.",
     "We’ll share every update on this page."),
    ("Honest claims only",
     "We only make the health claims UK law authorises, worded exactly. We’ll tell you what MUTO won’t do as clearly as what it will. Every review is genuine and invited from every customer, and every creator we work with is disclosed.",
     "Every claim on our site carries its authorised wording."),
    ("Built to be checked",
     "Note how you feel today: score your afternoons, or check your wearable. Give it 90 days. If you don’t feel the difference, you get every subscription payment back. Skip, pause or cancel online anytime, with a reminder five days before every payment.",
     "Guarantee terms below."),
]
add("standards", "muto-lp-reasons", {"anchor": "standards"}, [
    (f"s{i}", {"type": "reason", "settings": {"title": t, "body": p(b), "answer_label": "How to check", "answer": p(c)}})
    for i, (t, b, c) in enumerate(STANDARDS, 1)
])

# ---- 5. Five jobs, one jar ----
add("jobs_head", "muto-lp-article", {
    "heading": "The foundation your body runs on.",
    "body": p("Built for what you actually need in your 40s and 50s. Five jobs, one jar."),
})
JOBS = [
    ("1. Energy", "Methylated B vitamins", "Help you feel less tired"),
    ("2. Muscles and bones", "Vitamin D3 2,000 IU + K2 100µg", "Normal muscle function and the maintenance of normal bones"),
    ("3. Immunity", "Zinc 15mg + copper 1mg, with D3", "The normal function of your immune system"),
    ("4. NAD+", "NR 300mg", "Your body turns it into NAD+, which runs lower as we get older"),
    ("5. What ties it together", "CoQ10 150mg, trans-resveratrol 50mg, grape seed extract 150mg, PQQ 20mg, TMG 450mg, BioPerine® 5mg", "Every dose on the label"),
]
add("jobs", "muto-lp-reasons", {"anchor": "ingredients"}, [
    ("j1", {"type": "compare", "settings": {
        "heading": "", "col1": "Job", "col2": "What’s in it", "col3": "What it does",
        "rows": "\n".join(" | ".join(r) for r in JOBS),
        "note": "Vitamins B6 and B12 contribute to the reduction of tiredness and fatigue. Vitamin D contributes to normal muscle function. Vitamins D and K contribute to the maintenance of normal bones. Zinc, copper and vitamin D contribute to the normal function of the immune system."}}),
    ("j2", {"type": "callout", "settings": {
        "text": p("<strong>Two capsules with breakfast.</strong> Alongside our creatine, which comes free with your first order, it’s all you need to keep up."),
        "image_fallback": KIT, "image_alt": KIT_ALT, "image_position": "55% 62%"}}),
    ("j3", {"type": "cta", "settings": {"text": "", "label": "See the full label and the science behind each ingredient", "link": "/pages/ingredients"}}),
])

# ---- 6. Meet the scientists ----
add("people_head", "muto-lp-article", {
    "heading": "The people behind the formula.",
    "body": p("A supplement doesn’t need a scientist anywhere near it. Ours has seven.",
              "<em>Our advisory board guides our research and formulation. It doesn’t endorse products, and none of its members are presented as recommending MUTO for any medical purpose.</em>"),
})
BOARD = [  # as on the live landing pages
    ("shopify://shop_images/Dr_James_Cover_Final.png", CDN + "about-board-3.jpg?v=1790751994", "Dr James Morehen", "Performance nutritionist, international rugby · Scientific Advisory Board", "Advises MUTO on performance nutrition for people who still train hard."),
    ("shopify://shop_images/Dr_Alka_Cover_Final.png", CDN + "about-board-1.jpg?v=1790751995", "Dr Alka Patel", "Longevity doctor & global speaker · Scientific Advisory Board", "Advises MUTO on longevity: helping people keep doing what they love for longer."),
    ("shopify://shop_images/Dr_Richard_Cover_Final.png", "", "Dr Richard Mackenzie", "Leading metabolism researcher · Scientific Advisory Board", "Advises MUTO on metabolism: how your cells turn food into energy."),
    ("shopify://shop_images/Dr_Matt.png", "", "Dr Maciej Zatonski", "Performance & sleep doctor · Scientific Advisory Board", "Advises MUTO on sleep and recovery, and on reading them over weeks, not nights."),
    ("shopify://shop_images/Dr-ash-cover-hq.webp", "", "Dr Ash Kapoor", "Longevity & Human Optimisation Doctor & Founder of Levitas One · Scientific Advisory Board", "Advises MUTO on longevity and human optimisation."),
    ("shopify://shop_images/Jamie-Paweleck.jpg", "", "Dr Jamie Paweleck", "Longevity doctor and medical educator · Scientific Advisory Board", "Advises MUTO on longevity medicine and medical education."),
]
add("people", "muto-lp-experts", {"heading": "Our founder and Scientific Advisory Board."}, [
    ("e0", {"type": "person", "settings": {"image_fallback": FOUNDER, "alt": "Dr Richie Barclay holding a jar of MUTO", "position": "50% 20%",
                                           "name": "Dr Richie Barclay, PhD", "role": "Founder · PhD, cell biology and nutrition",
                                           "quote": "“I built MUTO because I was tired of supplements that ask you to take them on trust. So every ingredient and every dose is on the label.”"}}),
] + [
    (f"e{i}", {"type": "person", "settings": {"image": img, "image_fallback": fb, "alt": n, "name": n, "role": r, "quote": q}})
    for i, (img, fb, n, r, q) in enumerate(BOARD, 1)
])

# ---- 7. Check us yourself ----
add("check_head", "muto-lp-article", {"heading": "Don’t take our word for it.", "body": ""})
CHECK = [
    ("Read the full label.", "Every ingredient, every dose."),
    ("Paste it into ChatGPT, or show it to your GP, pharmacist or nutritionist.", ""),
    ("Ask us for a batch certificate.", ""),
    ("Ask Richie anything about the formula.", "He answers formula questions himself."),
    ("Then give it 90 days, and judge it for yourself.", ""),
]
add("check", "muto-lp-reasons", {"anchor": "check"}, [
    (f"k{i}", {"type": "reason", "settings": {"title": t, "body": p(b) if b else "", "answer_label": "", "answer": ""}})
    for i, (t, b) in enumerate(CHECK, 1)
] + [
    ("k_cta", {"type": "cta", "settings": {"text": "Email us", "label": "hello@mutolongevity.com", "link": "mailto:hello@mutolongevity.com"}}),
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
    ("Something else?", "Everything else, from delivery to your subscription, is in our <a href=\"/pages/faqs\">full FAQ</a>."),
]
add("faq", "muto-lp-faq-2", {"heading": "Questions about our standards.", "open_first": True, "schema_on": True}, [
    (f"q{i}", {"type": "q", "settings": {"q": q, "a": p(a)}}) for i, (q, a) in enumerate(FAQ, 1)
])

# ---- 9. Closing CTA ----
add("close_head", "muto-lp-article", {
    "heading": "Above the standard. Beneath the surface.",
    "body": p("Five jobs, one jar. Every dose on the label, every batch tested, and 90 days to judge it for yourself."),
})
add("close", "muto-lp-reasons", {"anchor": "start"}, [
    ("z1", {"type": "cta", "settings": {"text": "90-day money-back guarantee for subscribers · Skip, pause or cancel online · T&Cs apply", "label": CTA, "link": PDP}}),
])
add("bar", "muto-lp-bar", {"text": "Every dose on the label. Every batch tested. 90 days to judge it.", "cta_label": CTA, "cta_sub": "", "cta_link": PDP})

# Page-only CSS: the trust strip takes five items (the section is built for three)
add("page_css", "custom-liquid", {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid": """<style>
.mlp-trust__row{grid-template-columns:repeat(5,minmax(0,1fr))!important;max-width:1320px}
.mlp-trust__item+.mlp-trust__item{border-top:0;border-left:1px solid var(--hair)}
@media (max-width:749px){
  .mlp-trust__row{display:flex!important;flex-wrap:wrap;justify-content:center}
  .mlp-trust__item{flex:0 0 33.333%;border-left:0!important}
  .mlp-trust__item:nth-child(n+4){border-top:1px solid var(--hair)}
}
.mlp-rs__cta p{font-size:14px}
</style>"""})

out = os.path.join(HERE, "templates", "page.standards.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
