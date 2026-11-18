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
    "article": True, "news": True,
    "kicker": "Health · Energy",
    "headline": "Why you’re more tired after 35: a cell biologist on the seven nutrients that matter",
    "standfirst": "The way our cells produce energy changes with age. Dr Richie Barclay sets out what changes, "
                  "what the research shows and what to check on a supplement label.",
    "author_name": "By Dr Richie Barclay",
    "author_role": "Cell biologist and founder of MUTO · Updated November 2026 · 6 min read",
    "author_image_url": FOUNDER, "author_image_position": "50% 20%",
    "image_url": CDN + "muto-step-morning.jpg?v=1793455074",
    "image_alt": "A woman drinking coffee at her kitchen table in the morning light",
    "image_caption": "Caffeine blocks the feeling of tiredness. It does not add to the energy cells produce.",
}


def text(body, kicker="", heading=""):
    return {"type": "text", "settings": {"kicker": kicker, "heading": heading, "body": body}}


def quote(words, name="", note="", stars=False):
    return {"type": "quote", "settings": {"stars": stars, "text": words, "name": name, "note": note}}


opening = text(
    "<p>I get asked the same thing most weeks. Someone in their late thirties or forties tells me they’re "
    "tired all the time and can’t work out why. They sleep OK. They exercise. The GP has run bloods and "
    "everything’s normal. And by three in the afternoon they’re making another coffee.</p>"
    "<p>There’s a reason for it. Your cells make energy in mitochondria, and they get worse at it as you get "
    "older. One study took muscle samples from 146 people aged 18 to 89 and found that the ability to produce "
    "ATP, which is what cells actually run on, dropped steadily with age.</p>"
    "<p>Before anyone writes in: sleep, food and exercise matter more than any supplement. But seven nutrients "
    "keep turning up in the research on how cells make energy, and a few of them get harder to make or absorb "
    "as we age. This is my list. I’ve tried to be honest about where the evidence is good and where it isn’t.</p>")

# ------------------------------------------------------------------ the seven
REG = "Regulation (EU) No 432/2012, as retained in UK law: list of permitted health claims."

nad = need(
    "NAD+", "NAD+",
    "300mg of nicotinamide riboside (NR), the maximum permitted in UK supplements",
    "<p>If you’ve heard of one thing on this list, it’s probably NAD+. It’s in every cell, your mitochondria "
    "can’t turn food into energy without it, and you have less of it as you get older.</p>"
    "<p>Annoyingly, you can’t just swallow it. NAD+ is poorly absorbed. What you take instead is something "
    "your body can build it from, usually nicotinamide riboside (NR), which is a form of vitamin B3.</p>",
    ["In samples of human skin, NAD+ levels were lower with age, from newborns to people in their 70s. | 1",
     "In a placebo-controlled trial, 300mg of NR a day raised NAD+ in the blood by about 51% within two weeks. | 2",
     "What we don’t know yet is whether raising NAD+ makes people feel more energetic. The trials so far have measured levels in the body."],
    ["Massudi H, et al. Age-associated changes in oxidative stress and NAD+ metabolism in human tissue. PLoS One. 2012.",
     "Conze D, Brenner C, Kruger CL. Safety and metabolism of long-term administration of NIAGEN (nicotinamide riboside chloride) "
     "in a randomized, double-blind, placebo-controlled clinical trial of healthy overweight adults. Sci Rep. 2019.",
     REG],
    claim="Niacin (vitamin B3) contributes to normal energy-yielding metabolism and to the reduction of tiredness and fatigue.")

coq10 = need(
    "CoQ10", "CoQ10",
    "150mg, taken with food",
    "<p>CoQ10 does one of the jobs in the chain of reactions that makes ATP inside your mitochondria. You make "
    "your own, but less of it after your twenties, and you don’t get much from food.</p>"
    "<p>It has been around for decades and it isn’t fashionable, which is partly why I like it. There’s a "
    "reasonable amount of human data.</p>",
    ["CoQ10 levels in human organs, including the heart, are highest at around age 20 and then decline. | 1",
     "A 2022 analysis of 13 randomised trials involving 1,126 people found that CoQ10 reduced fatigue scores compared with placebo. | 2",
     "CoQ10 is fat-soluble and is absorbed better when taken with food. | 3"],
    ["Kalén A, Appelkvist EL, Dallner G. Age-related changes in the lipid compositions of rat and human tissues. Lipids. 1989.",
     "Tsai IC, et al. Effectiveness of coenzyme Q10 supplementation for reducing fatigue: a systematic review and "
     "meta-analysis of randomized controlled trials. Front Pharmacol. 2022.",
     "Bhagavan HN, Chopra RK. Coenzyme Q10: absorption, tissue uptake, metabolism and pharmacokinetics. Free Radic Res. 2006."])

dark = {"type": "dark", "settings": {
    "label": "Explainer",
    "heading": "Why energy falls with age",
    "text": "<p>Cells run on ATP, which is made in the mitochondria. Three changes that come with age affect "
            "how much of it they produce.</p>",
    "step_1_title": "Mitochondria produce less",
    "step_1_text": "Between the late 30s and the late 60s, the capacity of muscle to make energy roughly halves.",
    "step_2_title": "NAD+ and CoQ10 decline",
    "step_2_text": "Mitochondria depend on both, and levels of both fall with age in human tissue.",
    "step_3_title": "Absorption gets worse",
    "step_3_text": "The stomach makes less acid, which makes vitamin B12 from food harder to absorb. "
                   "Skin makes less vitamin D from the same amount of sunlight.",
    "end": "Caffeine does not reverse any of this. It blocks the signal that tells the brain it is tired, "
           "which is why the tiredness comes back when it wears off.",
    "refs": lines(
        "Conley KE, Jubrias SA, Esselman PC. Oxidative capacity and ageing in human muscle. J Physiol. 2000.",
        "Short KR, et al. Decline in skeletal muscle mitochondrial function with aging in humans. Proc Natl Acad Sci USA. 2005.",
        "Massudi H, et al. PLoS One. 2012. Kalén A, et al. Lipids. 1989.",
        "Baik HW, Russell RM. Vitamin B12 deficiency in the elderly. Annu Rev Nutr. 1999.",
        "MacLaughlin J, Holick MF. Aging decreases the capacity of human skin to produce vitamin D3. J Clin Invest. 1985.")}}

b_vits = need(
    "B vitamins", "B vitamins, in their active forms",
    "all eight B vitamins, with B12 as methylcobalamin, folate as 5-MTHF and B6 as P5P",
    "<p>Nearly every step of getting energy out of food needs a B vitamin, and your body doesn’t keep much "
    "of a store, so you need them every day.</p>"
    "<p>What I check on a label is the form. Many products use folic acid and cyanocobalamin, which your body "
    "has to convert before it can use them. The methylated versions, 5-MTHF and methylcobalamin, don’t need "
    "that step. They cost more to put in a capsule, which is why you don’t always see them.</p>",
    ["Absorbing vitamin B12 from food becomes harder with age, mainly because the stomach makes less acid. | 1",
     "A common variant of the MTHFR gene makes the enzyme that activates folic acid less efficient. | 2",
     "5-MTHF raises folate levels at least as well as folic acid. | 3"],
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
    "Creatine", "Creatine",
    "3 to 5g of creatine monohydrate a day",
    "<p>People are often surprised to see creatine here, because they think of it as something for the gym. "
    "All it does is help your muscles remake ATP quickly when you ask a lot of them, whether that’s a set of "
    "squats or two flights of stairs.</p>"
    "<p>You make about a gram a day and get the rest from meat and fish. And we all start losing muscle from "
    "our thirties unless we use it.</p>",
    ["The International Society of Sports Nutrition describes creatine monohydrate as the most effective "
     "supplement available for high-intensity exercise capacity. | 1",
     "On a normal diet, creatine stores in muscle are around 60 to 80% full. | 1",
     "Adults lose roughly 3 to 8% of their muscle mass each decade after 30. | 2"],
    ["Kreider RB, et al. International Society of Sports Nutrition position stand: safety and efficacy of "
     "creatine supplementation in exercise, sport, and medicine. J Int Soc Sports Nutr. 2017.",
     "Volpi E, Nazemi R, Fujita S. Muscle tissue changes with aging. Curr Opin Clin Nutr Metab Care. 2004.",
     REG],
    claim="Creatine increases physical performance in successive bursts of short-term, high-intensity exercise. "
          "The beneficial effect is obtained with a daily intake of 3g of creatine.")

zinc = need(
    "Zinc and copper", "Zinc and copper, together",
    "15mg of zinc with 1mg of copper, both as bisglycinate",
    "<p>These are two minerals you only need a little of. Zinc helps you process the carbohydrate, fat and "
    "protein you eat. Copper is part of one of the final enzymes in the energy chain in your mitochondria.</p>"
    "<p>The thing to know is that they compete for absorption. It’s easy to take a zinc supplement for months "
    "without realising it can pull your copper down. Take them together.</p>",
    ["Zinc taken long-term without copper can lower the body’s copper levels. | 1",
     "In a crossover study, zinc bisglycinate was absorbed 43% better than zinc gluconate. | 2",
     "Zinc levels tend to fall with age. | 3"],
    ["Fosmire GJ. Zinc toxicity. Am J Clin Nutr. 1990.",
     "Gandia P, et al. A bioavailability study comparing two oral formulations containing zinc (Zn bis-glycinate "
     "vs. Zn gluconate) after a single administration to twelve healthy female volunteers. Int J Vitam Nutr Res. 2007.",
     "Haase H, Rink L. The immune system and the impact of zinc during aging. Immun Ageing. 2009.",
     REG],
    claim="Copper contributes to normal energy-yielding metabolism. Zinc contributes to normal macronutrient "
          "metabolism and to the protection of cells from oxidative stress.")

d3k2 = need(
    "Vitamin D3 and K2", "Vitamin D3 and K2",
    "2,000 IU of vitamin D3 with 100µg of vitamin K2 as MK-7",
    "<p>Your muscles need vitamin D to work normally. You make it in your skin from sunlight, which is a "
    "problem in Britain: from October to March the sun isn’t strong enough, and older skin makes less anyway.</p>"
    "<p>I pair it with K2. Vitamin D helps you absorb calcium, and vitamin K contributes to normal bones.</p>",
    ["Skin from people in their late 70s and 80s produced less than half the vitamin D of skin from young people. | 1",
     "UK health advice is that everyone should consider a daily vitamin D supplement in autumn and winter. | 2",
     "Vitamin D3 raises blood levels of vitamin D more effectively than D2. | 3",
     "MK-7 stays in the body longer than vitamin K1. | 4"],
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
    "PQQ and trans-resveratrol", "PQQ and trans-resveratrol",
    "20mg of PQQ and 50mg of trans-resveratrol",
    "<p>I’ll be upfront: these two are the least proven things on the list. Most of the research is in cells "
    "or in small groups of people.</p>"
    "<p>PQQ is found in tiny amounts in kiwi fruit, parsley and green tea, and resveratrol comes from grape "
    "skins. I include them because both are being studied for what they do in mitochondria, and the early "
    "results are interesting enough for me.</p>",
    ["In cell studies, PQQ activated a pathway that leads cells to build new mitochondria. | 1",
     "In a small human study, PQQ changed markers in blood and urine linked to mitochondrial activity. | 2",
     "Resveratrol has been widely studied in ageing research, including for its effect on cell pathways that depend on NAD+. | 3"],
    ["Chowanadisai W, et al. Pyrroloquinoline quinone stimulates mitochondrial biogenesis through cAMP response "
     "element-binding protein phosphorylation and increased PGC-1α expression. J Biol Chem. 2010.",
     "Harris CB, et al. Dietary pyrroloquinoline quinone (PQQ) alters indicators of inflammation and "
     "mitochondrial-related metabolism in human subjects. J Nutr Biochem. 2013.",
     "Baur JA, Sinclair DA. Therapeutic potential of resveratrol: the in vivo evidence. Nat Rev Drug Discov. 2006."])

reveal = text(
    "<p>If you bought all of that separately you’d have seven or eight pots on the kitchen counter, from "
    "different brands, all running out at different times. Almost nobody keeps that up.</p>"
    "<p>That’s the reason I made MUTO NAD+ Cellular Complex. Six of the seven are in two capsules you take "
    "with breakfast, and every dose is on the label, so you can check it against this article. Creatine "
    "doesn’t fit in a capsule at a useful dose, so it comes as a separate pouch, free with your first "
    "subscription order.</p>",
    heading="Getting all seven")

customer = quote(
    "“Being in my mid 30s, everything has started to slow down. Muto is providing me with a sense of vitality "
    "which I haven’t experienced since my mid 20s”",
    name="Jonathon R", note="MUTO customer. Individual experience; results vary.")

answer = {"type": "answer", "settings": {
    "label": "",
    "heading": "What is in MUTO",
    "text": "",
    "image_url": CDN + "muto-menu-offer.jpg?v=1793615475",
    "image_alt": "A jar of MUTO NAD+ Cellular Complex beside its box, with every ingredient and dose printed on the side",
    "image_position": "50% 70%",
    "rows": lines(
        "NAD+ | 300mg NR",
        "CoQ10 | 150mg",
        "B vitamins | All eight, in active forms",
        "Creatine | Free 250g pouch with a first subscription order",
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
                          science_label="The evidence", sources_label="Sources")}

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
