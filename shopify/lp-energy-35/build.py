"""Build the "energy after 35" advertorial (templates/product.muto-nad-bf-lp-energy-35.json).

An article in the founder's voice: headline, standfirst and byline, a short opening story, seven numbered
essentials with the research for each, a black "why it happens" band, then MUTO as what he built, the live
buy box and the reviews.

A product template, like the over-35 listicle, so the page has the product in scope and the buy box is the
real one. The name starts with muto-nad-bf because the header and footer switch the Black Friday top bar and
sticky add to cart on for any template whose name contains it.

Everything from the buy box down is copied, unchanged, from the live main product page's template
(live-snapshot/product.muto-nad-bf-premium.json, taken from the live theme on 18 November 2026): the buy box
and the styles and scripts that draw it, the reviews widget and the test-results panel its button opens.
Above it: one section, sections/muto-lst-needs.liquid, which carries the article header, the story text,
the essentials, the quotes and the answer.

Voice: first person, Dr Richie Barclay. Nothing is put in his mouth that the site doesn't already say about
him (cell biologist, formulated MUTO because he couldn't find a product he'd take); the opening anecdote is
for him to approve. Customer quotes are real reviews from the live product page, word for word.

Claims guardrails, as on the other pages: authorised nutrient claims worded exactly and kept in the claims
note; research described as what a study measured, with its source, never as a promised result; no claim that
MUTO treats tiredness. NAD+, CoQ10, PQQ and resveratrol have no authorised claims, so their copy says what
they are and what was studied only.

Refresh the snapshot from the live theme before rebuilding, so the buy box stays the live one.
Run: python3 build.py
"""
import copy
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"
NAME = "product.muto-nad-bf-lp-energy-35.json"


def load(path):
    raw = open(os.path.join(HERE, path), encoding="utf-8").read()
    return json.loads(raw[raw.index("{"):])  # Shopify prefixes saved templates with a comment


PDP = load("live-snapshot/product.muto-nad-bf-premium.json")
P = PDP["sections"]


def lines(*items):
    return "\n".join(items)


def need(short, title, dose, body, science, refs, claim="", dose_label="What to look for"):
    return {"type": "need", "settings": {
        "short": short, "title": title, "dose_label": dose_label, "dose": dose, "body": body,
        "science": lines(*science), "claim": claim, "refs": lines(*refs)}}


# ------------------------------------------------------------------ article header and opening
FOUNDER = CDN + "about-founder.jpg?v=1790751995"
header = {
    "article": True,
    "kicker": "Energy and healthy ageing",
    "headline": "I’m a cell biologist. These are the 7 things I’d take for energy after 35.",
    "standfirst": "Most people over 35 blame themselves for the 3pm slump. The real cause is in your cells, "
                  "and the research on what they need is clearer than the supplement aisle makes it look.",
    "author_name": "By Dr Richie Barclay",
    "author_role": "PhD cell biologist · Founder of MUTO · 6 min read",
    "author_image_url": FOUNDER, "author_image_position": "50% 20%",
    "image_url": CDN + "muto-step-morning.jpg?v=1793455074",
    "image_alt": "A woman drinking coffee at her kitchen table in the morning light",
    "image_caption": "",
}


def text(body, kicker="", heading=""):
    return {"type": "text", "settings": {"kicker": kicker, "heading": heading, "body": body}}


def quote(words, name="", note="", stars=False):
    return {"type": "quote", "settings": {"stars": stars, "text": words, "name": name, "note": note}}


opening = text(
    "<p>There’s a question I hear more than any other. It usually comes from someone in their late 30s or 40s "
    "who is doing most things right. <strong>“Why am I so tired? Nothing’s actually wrong with me.”</strong></p>"
    "<p>They sleep reasonably well. They exercise. Their blood tests come back fine. And yet by mid-afternoon "
    "they’re running on coffee and willpower, and a hard week takes longer to shake off than it used to.</p>"
    "<p>I’m a cell biologist, so I’ll tell you what I tell them. You’re not lazy, and "
    "you’re not imagining it. The way your cells make energy changes as you get older.</p>"
    "<p>Here are the seven things I’d look at, in order. For each one I’ll tell you what it does, what to look "
    "for on a label, and what the research actually shows, including where it’s still thin.</p>")

# ------------------------------------------------------------------ the seven
REG = "Regulation (EU) No 432/2012, as retained in UK law: list of permitted health claims."

nad = need(
    "NAD+", "NAD+: the molecule every cell needs to make energy",
    "300mg of nicotinamide riboside (NR), the most the UK allows",
    "<p>If I had to pick one molecule to explain why 45 feels different from 25, it would be this one. NAD+ is "
    "in every cell you have. Your mitochondria, the parts of each cell that turn food into energy, can’t do "
    "their job without it. <strong>And you have less of it with every decade.</strong></p>"
    "<p>NAD+ itself isn’t well absorbed when you swallow it, which is why I’d skip products that list it as an "
    "ingredient. The practical route is nicotinamide riboside (NR): a form of vitamin B3 that your body turns "
    "into NAD+.</p>",
    ["NAD+ levels measured in human skin fall steadily with age, from newborns to people in their 70s. | 1",
     "In a placebo-controlled trial, 300mg of NR a day raised NAD+ in the blood by about 51% within two weeks. | 2",
     "Still being studied: whether more NAD+ changes how energetic people feel. The trials so far measure levels in the body."],
    ["Massudi H, et al. Age-associated changes in oxidative stress and NAD+ metabolism in human tissue. PLoS One. 2012.",
     "Conze D, Brenner C, Kruger CL. Safety and metabolism of long-term administration of NIAGEN (nicotinamide riboside chloride) "
     "in a randomized, double-blind, placebo-controlled clinical trial of healthy overweight adults. Sci Rep. 2019.",
     REG],
    claim="Niacin (vitamin B3) contributes to normal energy-yielding metabolism and to the reduction of tiredness and fatigue.")

coq10 = need(
    "CoQ10", "CoQ10: the spark inside your mitochondria",
    "150mg, taken with food",
    "<p>CoQ10 is the one I’m most surprised people haven’t heard of. It sits inside your mitochondria and "
    "carries electrons along the chain that makes ATP, the energy your cells actually spend. It’s part of the "
    "machinery itself.</p>"
    "<p>Your body makes its own, but production peaks in your twenties and falls from there, and food provides "
    "very little.</p>",
    ["CoQ10 levels in human organs, including the heart, are highest at around age 20 and then decline. | 1",
     "A 2022 analysis that pooled 13 randomised trials and 1,126 people found CoQ10 reduced fatigue scores compared with placebo. | 2",
     "CoQ10 is fat-soluble, so it’s absorbed better with food. Take it with breakfast, not on an empty stomach. | 3"],
    ["Kalén A, Appelkvist EL, Dallner G. Age-related changes in the lipid compositions of rat and human tissues. Lipids. 1989.",
     "Tsai IC, et al. Effectiveness of coenzyme Q10 supplementation for reducing fatigue: a systematic review and "
     "meta-analysis of randomized controlled trials. Front Pharmacol. 2022.",
     "Bhagavan HN, Chopra RK. Coenzyme Q10: absorption, tissue uptake, metabolism and pharmacokinetics. Free Radic Res. 2006."])

dark = {"type": "dark", "settings": {
    "label": "Why it happens",
    "heading": "You’re not getting lazy. Your cells are making less energy.",
    "text": "<p>Every cell in your body runs on a fuel called ATP, made by tiny power stations called "
            "mitochondria. As the years go by, three things quietly change.</p>",
    "step_1_title": "Your power stations slow down",
    "step_1_text": "In a study of 146 adults aged 18 to 89, the muscles’ ability to produce ATP fell steadily "
                   "with age. Between your late 30s and late 60s, your muscles’ capacity to make energy roughly halves.",
    "step_2_title": "They run short of what they run on",
    "step_2_text": "NAD+ and CoQ10, two molecules your mitochondria can’t work without, both decline with age in human tissue.",
    "step_3_title": "You absorb and make less",
    "step_3_text": "Your stomach makes less acid, so vitamin B12 from food gets harder to absorb. "
                   "Your skin makes less vitamin D from the same sunshine.",
    "end": "The result is the feeling you know: fine at 9am, flat by 3pm, slower to bounce back. And it’s why "
           "another coffee doesn’t fix it. Caffeine masks tiredness. It doesn’t make energy.",
    "refs": lines(
        "Short KR, et al. Decline in skeletal muscle mitochondrial function with aging in humans. Proc Natl Acad Sci USA. 2005.",
        "Conley KE, Jubrias SA, Esselman PC. Oxidative capacity and ageing in human muscle. J Physiol. 2000.",
        "Massudi H, et al. PLoS One. 2012. Kalén A, et al. Lipids. 1989.",
        "Baik HW, Russell RM. Vitamin B12 deficiency in the elderly. Annu Rev Nutr. 1999.",
        "MacLaughlin J, Holick MF. Aging decreases the capacity of human skin to produce vitamin D3. J Clin Invest. 1985.")}}

b_vits = need(
    "Methylated B vitamins", "Methylated B vitamins: the form your body can use straight away",
    "All 8 B vitamins, with B12 as methylcobalamin, folate as 5-MTHF and B6 as P5P",
    "<p>Most people have taken a B complex at some point. Far fewer have checked which form was in it, and "
    "that’s the part I care about.</p>"
    "<p>B vitamins are the workers on your energy production line. Almost every step that releases energy from "
    "food needs one of them, and your body can’t store most of them for long.</p>"
    "<p>Ordinary B vitamins have to be converted before your body can use them. Methylated, or “active”, forms "
    "skip that step. That matters more as you get older, and for the many people whose genes make the "
    "conversion less efficient.</p>",
    ["Absorbing vitamin B12 from food gets harder with age, mainly because the stomach makes less acid. | 1",
     "A common variant of the MTHFR gene makes the enzyme that activates folic acid less efficient. | 2",
     "5-MTHF, the active form of folate, raises folate levels at least as well as folic acid. | 3"],
    ["Baik HW, Russell RM. Vitamin B12 deficiency in the elderly. Annu Rev Nutr. 1999.",
     "Frosst P, et al. A candidate genetic risk factor for vascular disease: a common mutation in "
     "methylenetetrahydrofolate reductase. Nat Genet. 1995.",
     "Pietrzik K, Bailey L, Shane B. Folic acid and L-5-methyltetrahydrofolate: comparison of clinical "
     "pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2010.",
     REG],
    claim="Vitamins B2, B3, B5, B6, B12 and folate contribute to the reduction of tiredness and fatigue. "
          "Thiamin, riboflavin, niacin, pantothenic acid, vitamin B6, vitamin B12 and biotin contribute to "
          "normal energy-yielding metabolism.")

creatine = need(
    "Creatine", "Creatine: your muscles’ fastest energy reserve",
    "3 to 5g of creatine monohydrate a day. Nothing fancier",
    "<p>This is the one that surprises people, because they think of it as a gym supplement. Creatine isn’t "
    "only for bodybuilders. Your muscles store it as a rapid reserve that recharges ATP in "
    "seconds whenever demand spikes: the stairs, a run for the train, the last few reps.</p>"
    "<p>You make about a gram a day and get the rest from meat and fish. And from your 30s, muscle itself "
    "starts to slip unless you keep using it.</p>",
    ["It’s one of the most studied supplements there is. Sports scientists rate creatine monohydrate the most "
     "effective supplement for high-intensity exercise. | 1",
     "On a normal diet, your muscles’ creatine stores are only around 60 to 80% full. | 1",
     "Adults lose roughly 3 to 8% of their muscle each decade after 30. | 2"],
    ["Kreider RB, et al. International Society of Sports Nutrition position stand: safety and efficacy of "
     "creatine supplementation in exercise, sport, and medicine. J Int Soc Sports Nutr. 2017.",
     "Volpi E, Nazemi R, Fujita S. Muscle tissue changes with aging. Curr Opin Clin Nutr Metab Care. 2004.",
     REG],
    claim="Creatine increases physical performance in successive bursts of short-term, high-intensity exercise. "
          "The beneficial effect is obtained with a daily intake of 3g of creatine.")

zinc = need(
    "Zinc and copper", "Zinc and copper: small doses, big jobs, and they have to be balanced",
    "15mg of zinc with 1mg of copper, both as bisglycinate",
    "<p>Zinc helps your body process the carbohydrate, fat and protein you eat. Copper is part of the final "
    "step of energy production inside your mitochondria. You only need a little of each, but you do need both.</p>"
    "<p>Here’s the catch, and it’s the mistake I see most often: they compete. Take zinc on its own for months "
    "and your copper can drop. If a product gives you one without the other, put it back on the shelf.</p>",
    ["Zinc taken long-term without copper can lower the body’s copper levels. | 1",
     "In a crossover study, zinc bisglycinate was absorbed 43% better than zinc gluconate, a common form. | 2",
     "Zinc levels tend to fall as we get older. | 3"],
    ["Fosmire GJ. Zinc toxicity. Am J Clin Nutr. 1990.",
     "Gandia P, et al. A bioavailability study comparing two oral formulations containing zinc (Zn bis-glycinate "
     "vs. Zn gluconate) after a single administration to twelve healthy female volunteers. Int J Vitam Nutr Res. 2007.",
     "Haase H, Rink L. The immune system and the impact of zinc during aging. Immun Ageing. 2009.",
     REG],
    claim="Copper contributes to normal energy-yielding metabolism. Zinc contributes to normal macronutrient "
          "metabolism and to the protection of cells from oxidative stress.")

d3k2 = need(
    "Vitamin D3 and K2", "Vitamin D3 and K2: the sunshine pair your muscles rely on",
    "2,000 IU of vitamin D3 with 100µg of vitamin K2 as MK-7",
    "<p>Your muscles need vitamin D to work normally, and how strong you feel is a big part of how energetic "
    "you feel. Your skin makes it from sunlight, but from October to March the UK sun isn’t strong enough.</p>"
    "<p>K2 is its partner. Vitamin D helps your body absorb calcium, and K2 works alongside it for your bones.</p>",
    ["Skin from people in their late 70s and 80s made less than half the vitamin D that young skin did. | 1",
     "UK health advice is for everyone to consider a daily vitamin D supplement in autumn and winter. | 2",
     "D3 raises vitamin D levels in the blood more effectively than D2. | 3",
     "MK-7 stays in the body longer than vitamin K1, so once a day is enough. | 4"],
    ["MacLaughlin J, Holick MF. Aging decreases the capacity of human skin to produce vitamin D3. J Clin Invest. 1985.",
     "Scientific Advisory Committee on Nutrition. Vitamin D and Health. 2016.",
     "Tripkovic L, et al. Comparison of vitamin D2 and vitamin D3 supplementation in raising serum "
     "25-hydroxyvitamin D status: a systematic review and meta-analysis. Am J Clin Nutr. 2012.",
     "Schurgers LJ, et al. Vitamin K-containing dietary supplements: comparison of synthetic vitamin K1 and "
     "natto-derived menaquinone-7. Blood. 2007.",
     REG],
    claim="Vitamin D contributes to the maintenance of normal muscle function and normal bones. "
          "Vitamin K contributes to the maintenance of normal bones.")

pqq = need(
    "PQQ and trans-resveratrol", "PQQ and trans-resveratrol: the two that mitochondria researchers are watching",
    "20mg of PQQ and 50mg of trans-resveratrol, the stable form",
    "<p>These are the newest names on my list, and I’ll be straight with you: the research is at an earlier "
    "stage than for the vitamins above. I include them because of where that research is pointing.</p>"
    "<p>PQQ is found in tiny amounts in kiwi, parsley and green tea. Resveratrol comes from grape skins. Both "
    "are studied for the same reason: what they do in the mitochondria, the power stations this whole article is about.</p>",
    ["In cell studies, PQQ switched on the signal that tells cells to build new mitochondria. | 1",
     "In a small human study, PQQ changed markers in blood and urine that are linked to mitochondrial activity. | 2",
     "Resveratrol is one of the most studied plant compounds in healthy-ageing research, including the cell "
     "pathways that depend on NAD+. | 3"],
    ["Chowanadisai W, et al. Pyrroloquinoline quinone stimulates mitochondrial biogenesis through cAMP response "
     "element-binding protein phosphorylation and increased PGC-1α expression. J Biol Chem. 2010.",
     "Harris CB, et al. Dietary pyrroloquinoline quinone (PQQ) alters indicators of inflammation and "
     "mitochondrial-related metabolism in human subjects. J Nutr Biochem. 2013.",
     "Baur JA, Sinclair DA. Therapeutic potential of resveratrol: the in vivo evidence. Nat Rev Drug Discov. 2006."])

reveal = text(
    "<p>Seven essentials means seven or more separate pots, each from a different brand, each with its own "
    "dose and its own reorder date. Most people manage it for a month. Then the routine quietly falls apart.</p>"
    "<p>The best formula in the world does nothing if you stop taking it. So the real question isn’t only what "
    "to take. It’s what you’ll still be taking in six months.</p>",
    kicker="The problem with a list like this",
    heading="Knowing what to take is the easy part.")

customer = quote(
    "“Being in my mid 30s, everything has started to slow down. Muto is providing me with a sense of vitality "
    "which I haven’t experienced since my mid 20s”",
    name="Jonathon R", note="MUTO customer. Individual experience; results vary.", stars=True)

answer = {"type": "answer", "settings": {
    "label": "What I built",
    "heading": "So I put all seven into one daily routine.",
    "text": "<p>I couldn’t find one product that covered this list at these doses, with every dose printed on "
            "the label. So I formulated it. <strong>MUTO NAD+ Cellular Complex puts six of the seven into two "
            "capsules with breakfast.</strong> The seventh, creatine, comes free in your welcome kit.</p>",
    "image_url": CDN + "muto-menu-offer.jpg?v=1793615475",
    "image_alt": "A jar of MUTO NAD+ Cellular Complex beside its box, with every ingredient and dose printed on the side",
    "image_position": "50% 70%",
    "rows": lines(
        "NAD+ | 300mg NR, the most the UK allows",
        "CoQ10 | 150mg",
        "Methylated B vitamins | All 8, in active forms",
        "Creatine | Free 250g pouch with your first subscription order",
        "Zinc and copper | 15mg and 1mg, as bisglycinate",
        "Vitamin D3 and K2 | 2,000 IU and 100µg",
        "PQQ and trans-resveratrol | 20mg and 50mg"),
    "ticks": lines("19 ingredients, no blends", "Every batch independently tested", "Made in the UK",
                   "90-day money-back guarantee"),
    "cta": "See today’s offer", "cta_link": "",
    "foot": "Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle. "
            "If your tiredness is new, severe or doesn’t lift, speak to your GP. If you take medication, "
            "or are pregnant or breastfeeding, check with your doctor before taking supplements."}}

order_blocks = [("opening", opening), ("nad", nad), ("coq10", coq10), ("why", dark), ("bvits", b_vits),
                ("creatine", creatine), ("zinc", zinc), ("d3k2", d3k2), ("pqq", pqq), ("reveal", reveal),
                ("customer", customer), ("answer", answer)]
needs = {"type": "muto-lst-needs",
         "blocks": {k: v for k, v in order_blocks},
         "block_order": [k for k, _ in order_blocks],
         "settings": dict(header, index_label="", count_label="Essential",
                          science_label="What the research says", sources_label="Sources")}

# ------------------------------------------------------------------ the template
# From the live product page, unchanged: the styles that draw the buy box (bf_style, head_styles), the Black
# Friday top bar (bf_bar), the buy box, its scripts (early, easy_read, bands), the reviews widget and the
# test-results panel that the buy box's "View third-party testing results" button opens.
# Left out: ag1_plans. Despite the name it is the "As seen in" row and the dark "Your life won't fit a perfect
# routine" band under the product page's buy box, not part of the buy box.
bf_style = copy.deepcopy(P["bf_style"])
# The premium look is automatic on the product page's own template name; here it is asked for by setting.
bf_style["settings"]["design"] = "premium"

sections = {
    "bf_style": bf_style,
    "head_styles": P["head_styles"],
    "bf_bar": P["bf_bar"],
    "needs": needs,
    "buy": P["buy"],
    "early": P["early"],
    "reviews": P["reviews"],
    "tests": P["tests"],
    "easy_read": P["easy_read"],
    "bands": P["bands"],
}
out = {"sections": sections, "order": list(sections)}

path = os.path.join(HERE, "theme", "templates", NAME)
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", path, os.path.getsize(path), "bytes")
