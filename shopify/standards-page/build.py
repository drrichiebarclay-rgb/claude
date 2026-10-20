"""Our standards page: builds templates/page.standards.json from the copy doc
(MUTO_Our_Standards_Page_Copy_Oct26.docx) using the main site's own sections, the
ones the About page, home page and product page are built from (muto-about-*,
muto-home-*, muto-crea-*). Hero, board and banner settings are copied from the
About template (theme-ref/templates__page.about-muto.json) so imagery and
behaviour match it exactly.

Kept deliberately simple (seven sections), after the AG1 quality-standards style:
  statement → muto-about-statement     numbers → muto-home-stats
  ten standards → muto-about-research  rules vs MUTO → muto-crea-compare
  founder note → muto-about-founder    questions → muto-crea-faq
  close → muto-about-banner
The doc's five jobs, scientists and check-it-yourself sections are left to the
ingredients and About pages, which the page links to.
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


# Simple, calm page: a statement, three numbers, the ten standards as a plain list,
# the rules table, the founder's note, short questions, then the brand banner.

# ---- 1. Opening statement ----
add("intro", "muto-about-statement", {
    "layout": "split", "field": "tail", "eyebrow": "Our standards",
    "head": "You shouldn’t have to\ntake a supplement\non trust.",
    "tail": "",
    "body": "Supplements don’t have to prove much to go on sale in the UK. So we built MUTO to a higher bar, and we show you all of it.",
    "space_top": 140, "space_bottom": 60})

# ---- 2. Three numbers ----
add("numbers", "muto-home-stats", {"heading": "", "space_top": 40, "space_bottom": 80}, [
    ("n1", {"type": "stat", "settings": {"figure": "19", "label": "Doses on\nthe label", "caption": "No proprietary blends"}}),
    ("n2", {"type": "stat", "settings": {"figure": "100%", "label": "Of batches\ntested", "caption": "By an independent lab"}}),
    ("n3", {"type": "stat", "settings": {"figure": "90", "label": "Days to\njudge it", "caption": "Or your money back"}}),
])

# ---- 3. Ten standards, as a plain list ----
STANDARDS = [
    ("Every dose\non the label", "No proprietary blends. All 19 ingredients listed with their exact dose and form."),
    ("Doses chosen\nfor a reason", "NR at 300mg, the most allowed in Great Britain. D3 at 2,000 IU. B vitamins in active forms. Zinc and copper as a pair."),
    ("Only UK-authorised\ningredients", "Every ingredient is authorised for UK food supplements. That’s why we use NR, not NMN."),
    ("Every batch\ntested", "Every batch is tested by an independent lab before it’s released. Certificates on request."),
    ("Made in the UK,\nto GMP", "Manufactured to Good Manufacturing Practice standards, in an ISO-certified facility."),
    ("Nothing you\ndon’t need", "Vegan capsules. No major allergens, no fillers, no caffeine, no stimulants."),
    ("Scientists\nwith names", "Formulated by Dr Richie Barclay, PhD, and reviewed by a six-member scientific advisory board."),
    ("Research we’ll\npublish", "A University of Westminster study starts in December 2026. We’ll share the results, whatever they show."),
    ("Honest claims\nonly", "Only the health claims UK law authorises, worded exactly. Every review is genuine."),
    ("Built to be\nchecked", "Give it 90 days. If you don’t feel the difference, you get every subscription payment back."),
]
add("standards", "muto-about-research", {"field": False, "heading": "Our ten\nstandards", "space_top": 80, "space_bottom": 100}, [
    (f"s{i}", {"type": "item", "settings": {"name": n, "note": t}}) for i, (n, t) in enumerate(STANDARDS, 1)
])

# ---- 4. What the rules ask for vs what we do ----
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
    "fit": "nad", "space_top": 100, "space_bottom": 100}, [
    (f"r{i}", {"type": "row", "settings": {"claim": c, "m1": "yes", "m2": "no", "m3": "dash", "m4": "dash"}})
    for i, c in enumerate(RULES, 1)
])

# ---- 5. Why we built it this way ----
add("founder", "muto-about-founder", {
    "image_fallback": CDN + "about-founder.jpg?v=1790751995",
    "image_alt": ABOUT["founder"]["settings"]["image_alt"],
    "heading": "Nothing hidden.\nEverything checkable.",
    "name": "Dr Richie Barclay, Founder · PhD, cell biology and nutrition",
    "cta_label": CTA, "cta_link": PDP, "space_top": 100, "space_bottom": 100}, [
    ("p1", {"type": "para", "settings": {"text": "Most of the people I’ve worked with in their 40s and 50s were doing everything right, and still buying on a leap of faith. Labels that didn’t show the doses. Nobody checking every batch."}}),
    ("p2", {"type": "para", "settings": {"text": "So when I built MUTO, I built it the way I’d want it built for my own family: nothing hidden, everything checkable."}}),
])

# ---- 6. Questions ----
FAQ = [
    ("Can I see your test results?", "Yes. Batch certificates are available on request: <a href=\"mailto:hello@mutolongevity.com\">hello@mutolongevity.com</a>."),
    ("Why NR and not NMN?", "NR is authorised for food supplements in Great Britain, at up to 300mg a day for adults. NMN is still under novel food assessment."),
    ("Has MUTO been clinically proven?", "No, and we won’t say it has. Our first human study starts in December 2026 at the University of Westminster. We’ll publish the results, whatever they show."),
    ("Is it tested for banned substances?", "Every batch is third-party tested. We don’t currently make a banned-substance certification claim, and we’ll update this page if that changes."),
    ("Is it safe with medication?", "Check with your GP or pharmacist first. MUTO contains vitamin K2, which can affect blood thinners such as warfarin."),
]
add("faq", "muto-crea-faq", {"heading": "Questions", "schema_on": True, "space_top": 100, "space_bottom": 100}, [
    (f"q{i}", {"type": "q", "settings": {"title": q, "text": p(a)}}) for i, (q, a) in enumerate(FAQ, 1)
])

# ---- 7. Close ----
S["banner"] = from_about("banner", cta_label=CTA, cta_link=PDP); ORDER.append("banner")

# The comparison table has four columns; this page uses two
add("page_css", "custom-liquid", {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid": """<style>
[id$="__rules"] .mc__cmp th:nth-child(n+4),[id$="__rules"] .mc__cmp td:nth-child(n+4){display:none}
</style>"""})

out = os.path.join(HERE, "templates", "page.standards.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
