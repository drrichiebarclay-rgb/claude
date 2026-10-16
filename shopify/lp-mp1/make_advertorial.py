"""Build the broad-persona advertorial landing page (page.lp-stack.json).

Structure follows the "7 reasons your supplement stack isn't working" listicle
format, in MUTO's design: announcement line, article hero with author, real
customer review cards, intro, seven numbered reasons with the MUTO answer in
each, then MP1's offer, FAQ, second offer and sticky bar.
Claims guardrails as the other pages: authorised nutrient claims worded exactly,
real customer words only in quote marks, Richie is a PhD scientist (not a
medical doctor), results never promised.

Run make_lp.py first, then: python3 make_advertorial.py
"""
import copy, json, os
from build_personas import BASE, MAIN, CDN, CTA, faq, SAFE, SUB, WORK, INSIDE

HERE = os.path.dirname(os.path.abspath(__file__))
d = copy.deepcopy(BASE)
S = d["sections"]
for k in ("offer", "offer2", "bar"):
    S[k]["settings"]["cta_link"] = MAIN

FOUNDER = CDN + "about-founder.jpg?v=1790751995"


def blocks(items):
    return ({f"b{i}": b for i, b in enumerate(items, 1)}, [f"b{i}" for i in range(1, len(items) + 1)])


# ---------------------------------------------------------------- hero
hb, ho = blocks([{"type": "stat", "settings": {"figure": "4.83★", "label": "150+ reviews"}},
                 {"type": "stat", "settings": {"figure": "19", "label": "Doses on the label"}},
                 {"type": "stat", "settings": {"figure": "90", "label": "Days to decide"}}])
S["art_hero"] = {"type": "muto-lp-article-hero", "blocks": hb, "block_order": ho, "settings": {
    "announcement": "Taking five or more supplements and still can’t tell if any of them work? Here’s why.",
    "image_fallback": FOUNDER, "image_alt": "Richie Barclay, PhD cell biologist and MUTO founder, holding a jar of NAD+ Cellular Complex",
    "image_position": "50% 22%",
    "kicker": "For active 40–60s",
    "heading": "7 reasons your supplement stack isn’t adding up, and the one protocol built to replace it.",
    "sub": "For anyone taking five or more supplements who still can’t say which one is doing anything.",
    "cta_label": CTA, "cta_link": MAIN,
    "jump_label": "See the 7 reasons", "jump_target": "#reasons",
    "author_image_fallback": FOUNDER, "author_label": "Written by",
    "author_name": "Richie Barclay, PhD", "author_title": "Cell biologist and founder, MUTO"}}

# ---------------------------------------------------------------- real reviews
REVIEWS = [
    ("Replacing several pots", "“I love that this replaces multiple products”", "Amy C"),
    ("Afternoons", "“No afternoon slump and in general feeling great”", "Lynda"),
    ("A scientist who picks up the phone", "“Richie from the team gave me a call just to chat about my background and goals”", "Mathew H"),
    ("Feeling like yourself", "“I didn't realise how flat I'd been feeling until this helped lift me out of it”", "Holly P"),
    ("Recovery", "“Has actually changed my recovery”", "Adam H"),
    ("Marathon training", "“I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint”", "Rebeca"),
    ("Focus", "“More focused during the day”", "Alexandra"),
]
rb, ro = blocks([{"type": "review", "settings": {"topic": t, "quote": q, "name": n}} for t, q, n in REVIEWS])
S["review_cards"] = {"type": "muto-lp-review-cards", "blocks": rb, "block_order": ro, "settings": {
    "label": "What customers say about MUTO", "foot": "Customer reviews, in their own words. Individual experiences; results vary."}}

# ---------------------------------------------------------------- intro
S["intro"] = {"type": "muto-lp-article", "settings": {
    "body": "<p>You read the labels and listened to the podcasts. You ended up with the names that keep coming up: NR, CoQ10, vitamin D3 with K2, a B complex, maybe zinc and resveratrol. <strong>You’ve been consistent for months.</strong> And you still can’t point at one pot and say “this is the one that’s working.”</p>"
            "<p>That isn’t a discipline problem. It’s a design problem: doses you can’t see, ingredients sold one at a time, and no way to check any of it.</p>"
            "<p>Here are seven reasons a cupboard of pots does less than it should, and why one daily protocol, two capsules with breakfast, can replace a good part of it.</p>",
    "band_main": "Rated 4.83 from 150+ reviews",
    "band_sub": "Made in the UK · Every batch third-party tested · 90 days to decide"}}

# ---------------------------------------------------------------- the 7 reasons
PRODUCT = CDN + "nad-gallery-1.jpg?v=1790879783"


def reason(title, body, answer=""):
    return {"type": "reason", "settings": {"title": title, "body": body, "answer": answer, "answer_label": "The MUTO way"}}


items = [
    reason("You’ve been taking it for months. You still can’t tell what’s working. Here’s why.",
           "<p>A pot can list an ingredient without giving you a meaningful amount of it, and an all-in-one can list thirty ingredients at amounts too small to matter. The label has the name. You get a trace.</p>"
           "<p>To take MUTO’s doses as separate products you’d need eleven pots on the kitchen side, every day. Nobody keeps that up for long, so the routine drifts, and then you blame yourself.</p>"
           "<p><strong>You’re not inconsistent. The routine was never built to be checked.</strong></p>",
           "<p>MUTO runs <strong>300mg NR</strong>, the most allowed in Great Britain, and <strong>150mg CoQ10</strong>, with every other dose printed on the label. Two capsules with breakfast.</p>"),
    reason("Your body doesn’t use nutrients one at a time.",
           "<p>Vitamin D3 and K2 belong together: both contribute to the maintenance of normal bones. The B vitamins work as a group: thiamin, riboflavin, niacin, B6 and B12 contribute to normal energy-yielding metabolism. Zinc and copper are balanced against each other.</p>"
           "<p>Seven pots from seven brands were never designed to sit together. Nobody checked how they fit.</p>",
           "<p>MUTO was built as one formula: NR alongside TMG, D3 alongside K2, a full B complex in active forms, and BioPerine® in the same two capsules. One design, one label, chosen by a PhD cell biologist.</p>"),
    {"type": "doses", "settings": {
        "figure": "19", "label": "Ingredients built to work together",
        "sub": "Every dose on the label, no blends",
        "items": "NR | 300mg\nCoQ10 | 150mg\nTMG | 450mg\nGrapeseed extract | 150mg\nTrans-resveratrol | 50mg\nPQQ | 20mg\nVitamin D3 | 2,000 IU\nVitamin K2 (MK-7) | 100µg\nZinc | 15mg bisglycinate\nCopper | 1mg bisglycinate\nB complex | All 8, active forms\nBioPerine® | 5mg",
        "foot": "Plus thiamin, riboflavin, niacin, pantothenic acid, B6 (P5P), folate, B12 and biotin: the full label is on the product page."}},
    {"type": "review", "settings": {
        "lead": "<p>That’s the point. <strong>Not a longer ingredient list. A clearer one.</strong></p>",
        "quote": "“I love that this replaces multiple products”", "name": "Amy C",
        "cta_label": "Compare the labels yourself", "cta_link": MAIN}},
    reason("You’re paying more than you think, and you’ve lost the overview.",
           "<p>Separate pots look cheap until you add them up. NR, CoQ10, PQQ, resveratrol, D3 and K2, a B complex, zinc: bought at MUTO’s doses, that’s about <strong>£5.25 a day</strong>, roughly £158 a month.</p>"
           "<p>Then eleven reorders, eleven delivery charges, eleven chances to run out on a Wednesday. <strong>The worst part isn’t the money. It’s suspecting you’re paying for a result you can’t see.</strong></p>",
           "<p>19 ingredients in two capsules for <strong>£2 a day</strong> on subscription, £60 a month. Less than a coffee.</p>"),
    {"type": "stat", "settings": {
        "figure": "£1,170 a year",
        "text": "Roughly the gap between buying MUTO’s main ingredients as separate products (about £158 a month) and MUTO on subscription (£60 a month).",
        "source": "UK retail prices at similar doses, checked October 2026."}},
    reason("“Fine” isn’t the same as feeling like yourself.",
           "<p>The check-up comes back fine. On paper, nothing to see. In real life, the afternoons are slower, Sunday’s run is still in your legs on Wednesday, and your morning leans on coffee it didn’t used to.</p>"
           "<p>Reference ranges exist to rule out deficiency, not to describe you at your best.</p>"
           "<p><strong>You’re not done yet. You just don’t want to settle for fine.</strong></p>"),
    {"type": "callout", "settings": {
        "text": "<p>MUTO is one daily routine for people who aren’t ready to settle for fine: two capsules with breakfast, every dose on the label, and 90 days to judge it on how your days feel.</p>",
        "image_fallback": PRODUCT, "image_alt": "The MUTO NAD+ Cellular Complex jar, pouch, sachets and bottle together"}},
    reason("“Pixie dusting” is the industry’s open secret. Plenty of stacks are built on it.",
           "<p>Pixie dusting means listing an impressive ingredient at a dose too small to do anything. The ingredient is on the label. The dose is a trace. The label looks powerful; the formula is theatre.</p>"
           "<p>It shows up in two main forms:</p>"
           "<p><strong>1. The proprietary blend.</strong> “Longevity blend: 2,500mg”, with no individual amounts. You can’t tell what’s doing the work, and neither can your GP or your AI. If a brand won’t show the milligrams, ask why.</p>"
           "<p><strong>2. The big-percentage multivitamin.</strong> 1,000% of a cheap water-soluble vitamin makes the label look generous. The ingredients that cost something are missing, or there in a pinch.</p>",
           "<p>No blends and no pixie dust. All 19 ingredients and their doses are on the label, with the forms named: 300mg NR, 150mg CoQ10, zinc and copper as bisglycinate, B6 as P5P, B12 as methylcobalamin. Paste it into your AI, or ask Richie: he answers formula questions himself.</p>"),
    reason("Bought separately, the same ingredients cost about £158 a month. Here’s the maths.",
           "<p>If you take your supplements seriously, you’re probably buying several already: several brands, several deliveries, several reorder dates. MUTO puts all 19 ingredients in two capsules for £60 a month on subscription. About £2 a day.</p>"),
    {"type": "table", "settings": {
        "heading": "What’s inside, and what it would cost separately",
        "col1": "Ingredient", "col2": "Cost a month*",
        "rows": "NR (300mg) | £56.10\nCoQ10 (150mg) | £28.50\nGrapeseed extract (150mg) | £21.30\nPQQ (20mg) | £21.00\nTrans-resveratrol (50mg) | £10.80\nVitamin D3 and K2 | £9.90\nTMG (450mg) | £2.70\nBioPerine® (5mg) | £2.70\nZinc (15mg) | £1.80\nCopper (1mg) | £1.50\nB complex | £1.20",
        "total_label": "Total a month", "ours": "£60", "theirs": "£157.50",
        "note": "*UK retail prices for each ingredient as a separate product, at or near MUTO’s dose, checked 14 October 2026 (Superdrug, Holland & Barrett and other UK retailers). Roughly £1,170 a year more than MUTO on subscription, before delivery charges."}},
    reason("At what point does this become ridiculous?",
           "<p>You know the moment. Sunday evening, refilling the pill organiser. NR, CoQ10, PQQ, D3 and K2, a B complex, zinc, resveratrol. Eleven pots. Ten minutes every morning. <strong>And a growing suspicion that you’ve become the supplement industry’s favourite customer.</strong></p>"
           "<p><strong>It’s not your fault. It’s how the industry is set up.</strong></p>"
           "<p>The best-designed routine does nothing if you give up on it in month three because the ritual wore you down. <strong>Don’t abandon it. Replace it.</strong> The routine that counts is the one you keep every day, for years, without thinking.</p>",
           "<p>Two capsules with breakfast, nothing to sort or time. Rate how you feel at 3pm today and, if you wear a watch, note a week of HRV, resting heart rate and sleep. Judge it at day 30 and day 90. If you don’t see a difference, you’re covered.</p>"),
    {"type": "replaces", "settings": {
        "label": "Two capsules replace", "figure": "Up to 11 separate pots*",
        "items": "NR | bolt\nCoQ10 | heart\nPQQ | sparkle\nResveratrol | leaf\nGrapeseed | drop\nVitamin D3 + K2 | sun\nB complex | capsule\nZinc | shield\nCopper | shield\nTMG | flask\nBioPerine® | leaf",
        "cta_label": "Two capsules of MUTO", "cta_link": MAIN,
        "note": "*The 11 single-ingredient products in the price comparison above. Never stop anything you take for a medical reason."}},
    {"type": "compare", "settings": {
        "heading": "MUTO vs the stack you built yourself",
        "col1": "What you actually want", "col2": "Self-built stack", "col3": "MUTO",
        "rows": "Every dose printed on the label | Depends on the brand | All 19 listed\n"
                "NR, CoQ10, PQQ and resveratrol at real doses | 4 pots, 4 reorders | All four, two capsules\n"
                "Forms named on the label | Varies wildly | Every form named\n"
                "Independent testing | Varies brand to brand | Every batch third-party tested\n"
                "Morning routine | 10 minutes, 11 pots | Two capsules with breakfast\n"
                "Monthly cost at these doses | About £158 | £60\n"
                "Time to judge it | Often 30 days | 90 days, or your money back",
        "note": "Self-built stack: the 11 single-ingredient products in our October 2026 UK price check."}},
    {"type": "person", "settings": {
        "label": "From the scientist who built it",
        "image_fallback": FOUNDER, "position": "50% 20%",
        "quote": "“The interesting question isn’t which supplement is best. It’s why ten separate products so often add up to less than their labels. It usually comes down to dose, form and fit. So I built one formula, put every dose on the label, and gave people 90 days to check it for themselves.”",
        "name": "Richie Barclay, PhD", "role": "Cell biologist and MUTO founder"}},
]
xb, xo = blocks(items)
S["reasons"] = {"type": "muto-lp-reasons", "blocks": xb, "block_order": xo, "settings": {"anchor": "reasons"}}

# ---------------------------------------------------------------- close
S["offer"]["settings"]["heading"] = "Swap the guesswork for a 90-day test."
S["offer2"]["settings"]["heading"] = "One protocol. 90 days. Your call."
S["bar"]["settings"]["text"] = "One routine. Every dose on the label. £122 of value for £60 on your first subscription."
S["reviews"]["settings"]["heading"] = "<p>What customers say</p>"
S["experts"]["settings"]["heading"] = "Who built it.\nOur Scientific Advisory Board."
keep = [k for k in S["experts"]["block_order"] if S["experts"]["blocks"][k]["settings"]["role"] != "Athlete"]
S["experts"]["blocks"] = {k: S["experts"]["blocks"][k] for k in keep}
S["experts"]["block_order"] = keep
S["lp_faq"]["blocks"], S["lp_faq"]["block_order"] = faq([
    ("What does MUTO replace?", "<p>For many customers, several separate pots: NR, CoQ10, PQQ, B vitamins, vitamin D3, K2, zinc and resveratrol are all in here, at the doses shown. Never stop anything you take for a medical reason, and check with your GP if you take medicine.</p>"),
    INSIDE,
    ("Is it worth the money?", "<p>Bought separately at similar doses, the main ingredients cost about £5.25 a day at UK retail. MUTO is £2 a day on subscription, and you have 90 days to decide.</p>"),
    ("Who is Richie Barclay?", "<p>MUTO’s founder: a PhD cell biologist and former cricketer. He isn’t a medical doctor; our Scientific Advisory Board includes doctors and scientists who review the formula.</p>"),
    SAFE, WORK, SUB])

d["order"] = ["art_hero", "review_cards", "intro", "reasons", "reviews", "experts", "offer", "lp_faq", "offer2", "bar"]
for k in [k for k in S if k not in d["order"]]:
    del S[k]
out = os.path.join(HERE, "page.lp-stack.json")
json.dump(d, open(out, "w"), ensure_ascii=False, indent=2)
open(out, "a").write("\n")
print("wrote", out)
