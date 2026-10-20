"""Our standards page: builds templates/page.standards.json from the copy doc
(MUTO_Our_Standards_Page_Copy_Oct26.docx) using the main site's own sections, the
ones the About page, home page and product page are built from (muto-about-*,
muto-home-*, muto-crea-*). Hero, board and banner settings are copied from the
About template (theme-ref/templates__page.about-muto.json) so imagery and
behaviour match it exactly.

Laid out after the AG1 quality-standards page, in MUTO's own styles (muto-crea.css):
  muto-standards     headline, intro, the ten standards as a list with photos (new section)
  muto-home-board    the scientific board, as on the About page
  muto-get-started   photo + charcoal panel itemising the first order (new section)
  custom-reviews     REVIEWS.io widget, copied from the product page
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


# After the AG1 quality-standards page, in MUTO's own styles: headline and intro with the
# ten standards as a list (selected one fills teal, its promise and two photos on the right),
# the customer video rail from the product page, a "get started" panel, then short questions.
PDPT = json.load(open(os.path.join(HERE, "..", "pdp-45", "age-4060", "product.muto-nad-45.json")))["sections"]
IMG = {
    "declared": CDN + "about-made-declared.jpg?v=1790752124",
    "tested": CDN + "about-made-tested.jpg?v=1790752123",
    "scientists": CDN + "about-made-scientists.jpg?v=1790752123",
    "founder": CDN + "about-founder.jpg?v=1790751995",
    "kit": CDN + "muto-lp-kit-hero.jpg?v=1791969959",
    "factory": CDN + "home-why-manufacturing.jpg?v=1790767821",
    "jar": CDN + "nad-gallery-1.jpg?v=1790879783",
    "board1": CDN + "about-board-1.jpg?v=1790751995",
    "board3": CDN + "about-board-3.jpg?v=1790751994",
    "guide": CDN + "muto-gift-guide-v2.jpg?v=1791392560",
    "checkin": CDN + "nad-step-checkin-close.jpg?v=1791021630",
}
MAIL = "<a href=\"mailto:hello@mutolongevity.com\">hello@mutolongevity.com</a>"
STANDARDS = [
    ("Every dose on the label", "No proprietary blends. Every one of the 19 ingredients is listed with its exact dose and form, so you know exactly what you’re taking.",
     "Read the full label on our <a href=\"/pages/ingredients\">ingredients page</a>, or turn the jar round.", "declared", "jar"),
    ("Doses chosen for a reason", "NR at 300mg, the most allowed in Great Britain. Vitamin D3 at 2,000 IU. B vitamins in their active, methylated forms. Zinc and copper dosed as a pair, because they compete for absorption. Nothing added just to make the list longer.",
     "Every dose and form is in the ingredient table.", "guide", "kit"),
    ("Only UK-authorised ingredients", "Every ingredient in MUTO is authorised for use in UK food supplements. That’s why we use NR rather than NMN, which is still under assessment.",
     "Ask us about any ingredient’s status: " + MAIL, "jar", "factory"),
    ("Every batch third-party tested", "Not just the first batch. Every batch is tested by an independent lab before it’s released.",
     "Certificates are available on request: " + MAIL, "tested", "factory"),
    ("Made in the UK, to GMP", "Manufactured in the UK to GMP (Good Manufacturing Practice) standards, in an ISO-certified facility.",
     "Ask us for our manufacturing standards.", "factory", "tested"),
    ("Nothing you don’t need", "Vegan capsules made from plant cellulose (HPMC). Vitamin D3 from algae. No major allergens, no fillers, no caffeine and no stimulants.",
     "It’s all on the label.", "tested", "kit"),
    ("Scientists with names", "Formulated by Dr Richie Barclay, PhD in cell biology and nutrition, with a six-member scientific advisory board. The board meets every quarter to guide our research and every new formula. It doesn’t endorse products.",
     "Meet the board on our <a href=\"/pages/about\">About page</a>.", "scientists", "board1"),
    ("Research we’ll publish", "A University of Westminster study starts in December 2026, with work at King’s College London, Coventry and Newcastle to follow. There are no results yet, and we’ll never say there are.",
     "We’ll share every update on this page.", "board3", "scientists"),
    ("Honest claims only", "We only make the health claims UK law authorises, worded exactly. We’ll tell you what MUTO won’t do as clearly as what it will. Every review is genuine, and every creator we work with is disclosed.",
     "Every claim on our site carries its authorised wording.", "declared", "founder"),
    ("Built to be checked", "Note how you feel today. Give it 90 days. If you don’t feel the difference, you get every subscription payment back. Skip, pause or cancel online anytime, with a reminder five days before every payment.",
     "Guarantee terms are in our <a href=\"/pages/faqs#guarantee\">FAQs</a>.", "checkin", "founder"),
]
add("standards", "muto-standards", {
    "heading": "The standards\nbehind MUTO",
    "lede": "Supplements don’t have to prove much to go on sale in the UK. So we built MUTO to a higher bar, and we show you all of it: every dose on the label, every batch tested, made in the UK.",
    "list_label": "Our standards", "space_top": 120, "space_bottom": 100}, [
    (f"s{i}", {"type": "standard", "settings": {"title": t, "text": p(x), "check": p(c),
                                                "image_1_fallback": IMG[a]}})
    for i, (t, x, c, a, b) in enumerate(STANDARDS, 1)
])

# The scientific board, as on the About and home pages (interview videos, tags)
board = copy.deepcopy(ABOUT["board"])
board["settings"].update(heading="Meet our\nscientific board.", note="Our scientific advisory board")
S["board"] = board; ORDER.append("board")

add("start", "muto-get-started", {
    "image_fallback": IMG["kit"], "image_position": "55% 62%",
    "image_alt": "The MUTO first order: NAD+ Cellular Complex jar and refill pouches, Ultrapure Creatine, the bottle and the presentation box",
    "heading": "Start your\n90 days",
    "product_name": "NAD+ Cellular Complex (30 days)", "product_price": "£60",
    "product_sub": "£2 a day on the monthly plan",
    "includes_label": "First order includes:",
    "total_label": "Total", "total_was": "£122", "total_now": "£60",
    "cta_label": CTA, "cta_link": PDP,
    "ticks": "Free next-day delivery\nSkip, pause or cancel online\n90-day money-back guarantee",
    "space_top": 40, "space_bottom": 100}, [
    ("i1", {"type": "item", "settings": {"name": "Ultrapure Creatine", "desc": "A 250g pouch of micronised creatine", "was": "£30", "now": "free"}}),
    ("i2", {"type": "item", "settings": {"name": "Forever Jar", "desc": "A glass jar to keep", "was": "£10", "now": "free"}}),
    ("i3", {"type": "item", "settings": {"name": "12-week guide", "desc": "How to run your 90 days and check it yourself", "was": "£10", "now": "free"}}),
    ("i4", {"type": "item", "settings": {"name": "Socks", "desc": "Size UK 6–11", "was": "£12", "now": "free"}}),
])

# Customer reviews (REVIEWS.io widget), copied from the product page
S["reviews"] = copy.deepcopy(PDPT["custom_reviews_KpXTpD"]); ORDER.append("reviews")

out = os.path.join(HERE, "templates", "page.standards.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"sections": S, "order": ORDER}, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out, len(ORDER), "sections")
