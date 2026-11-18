"""Build version B of the "energy after 35" advertorial (templates/product.muto-nad-bf-lp-energy-35-feel.json).

Same page furniture as version A (build.py): the direct layout, the offer with its countdown, the trust
section, the reviews widget and the test-results panel. What changes is the argument. Version A explains
seven nutrients with research notes; this one is for a reader who doesn't want the science. It leads with
how the problem feels (in customers' own words from the jobs-to-be-done research), says in two plain
paragraphs why it happens, then shows what customers say they got back and how simple the routine is.

Guardrails as version A, and tighter because there is less evidence on the page: every outcome is either a
real customer's words (public reviews, quoted exactly, "results vary") or an authorised claim worded
exactly. Nothing says MUTO treats tiredness. Research participants are not quoted or named.

Run: python3 build_feel.py   (it imports build.py, which rebuilds version A first)
"""
import json
import os

import build as A
from build import CDN, lines, text, quote, cta, need

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "product.muto-nad-bf-lp-energy-35-feel.json"
RV = "MUTO customer. Individual experience; results vary."

header = dict(
    A.header,
    headline="You’re not lazy, you’re <em>running on empty</em>, and it isn’t your fault.",
    standfirst="A gentle explanation of why so many people over 35 feel flat by the middle of the afternoon, "
               "and the simple two-capsule morning habit that thousands of them have switched to.",
)

opening = text(
    "<p>There was probably a time when you had a little more in the tank than you do now, and when a busy day "
    "didn’t leave you feeling quite so flat by the end of it.</p>"
    "<p>These days you might feel fine until around three in the afternoon, when everything starts to feel a "
    "little heavier than it should.</p>"
    "<p><strong>So you make another coffee and push through a slower afternoon, and by the time you get home "
    "there isn’t very much left for the people you love.</strong></p>"
    "<p>What makes it harder is that you’re already doing most things right, because you eat well, you keep "
    "moving and you get to bed at a sensible time.</p>"
    "<p>And still, somehow, you don’t quite feel like yourself, which can be a lonely thing to carry around "
    "when nobody else can see it.</p>",
    heading="Do you remember when you could <em>just go again?</em>")

familiar = text(
    "<p>If you’re over 35, there’s a good chance you’ll recognise at least a couple of these, and if you do, "
    "please know that you’re far from the only one.</p>",
    heading="Does any of this <em>sound familiar?</em>")

moments = [
    need("", "The 3pm crash", "",
         "<p>You feel fine all morning, and then the middle of the afternoon arrives and you find yourself "
         "reaching for a coffee that you know you’ll regret at bedtime.</p>", [], []),
    need("", "Brain fog when you need to be sharp", "",
         "<p>Your thinking slows down in the one meeting where you most need to be sharp, and you can feel "
         "yourself searching for words that used to come easily.</p>", [], []),
    need("", "Heavy legs the next day", "",
         "<p>A walk, a run or a gym session that you once shook off overnight is still sitting in your legs "
         "when you climb the stairs two days later.</p>", [], []),
    need("", "Nothing left for the evening", "",
         "<p>You get through the working day, but by the evening there’s very little left in the tank for the "
         "people at home, even though you’d love nothing more than to give them your best.</p>", [], []),
    need("", "Waking up groggy", "",
         "<p>You spend a full night in bed and still wake up feeling as though you haven’t quite recharged "
         "for the day ahead.</p>", [], []),
]

why = {"type": "dark", "settings": {
    "label": "Why it happens",
    "heading": "It isn’t in your head, and it isn’t your fault.",
    "text": "<p>From around your mid-30s, your body gradually becomes less efficient at turning the food you eat "
            "into energy, and scientists have measured it: between your late 30s and your late 60s, your "
            "muscles’ capacity to make energy falls by roughly half.</p>"
            "<p>That is simply biology doing what biology does, and it has nothing to do with willpower or "
            "with being lazy.</p>",
    "step_1_title": "", "step_1_text": "", "step_2_title": "", "step_2_text": "",
    "step_3_title": "", "step_3_text": "",
    "end": "It also explains why another coffee never really fixes it, because caffeine only hides the "
           "tiredness for a while and lets it come back once it has worn off.",
    "refs": "Conley KE, Jubrias SA, Esselman PC. Oxidative capacity and ageing in human muscle. J Physiol. 2000."}}

life = text(
    "<p>The difficulty is that life doesn’t pause while you work all of this out, because there is still work "
    "to do, children to look after, journeys to make and people who are relying on you.</p>"
    "<p>And very few of us are 25-year-old personal trainers who can build a whole life around a perfect "
    "routine.</p>"
    "<p><strong>What most of us need is something gentle and simple that fits into the life we actually "
    "have.</strong></p>",
    heading="Life doesn’t <em>wait for you to catch up</em>")

photo = {"type": "image", "settings": {
    "image_url": CDN + "Golden_Hour_Family_Beach_Walk.png?v=1792566215",
    "image_alt": "A family walking along a beach at sunset with their dog", "image_position": "50% 0%", "caption": ""}}

back = text(
    "<p>We asked the people who take it what had changed for them, and these are their own words and not ours.</p>",
    heading="What people say they <em>got back</em>")

q1 = quote("“No afternoon slump and in general feeling great”", "Lynda", RV, stars=True)
q2 = quote("“I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore.”",
           "Danny S", RV, stars=True)
q3 = quote("“I didn't realise how flat I'd been feeling until this helped lift me out of it”", "Holly P", RV, stars=True)

simple = text(
    "<p><strong>MUTO NAD+ Cellular Complex</strong> is two capsules that you take with your breakfast, and "
    "that really is all there is to it.</p>"
    "<ul><li>There is nothing to mix and nothing to carry around with you</li>"
    "<li>It contains no caffeine and no stimulants, so there is nothing to crash from later</li>"
    "<li>One jar takes the place of a cupboard full of separate pots</li>"
    "<li>It soon becomes a habit as easy as brushing your teeth</li></ul>"
    "<p>It was made by a cell biologist for adults over 35, and you don’t need to be sporty or own a "
    "smartwatch for it to be right for you.</p>",
    heading="Two capsules, <em>every morning</em>")

jar = {"type": "image", "settings": {
    "image_url": CDN + "lp-over-35-hero.jpg?v=1794239299",
    "image_alt": "A woman at her kitchen table in morning light, taking a capsule beside a glass of water and a jar "
                 "of MUTO NAD+ Cellular Complex", "image_position": "50% 100%", "caption": ""}}

inside = {"type": "answer", "settings": {
    "label": "",
    "heading": "What’s inside, <em>in plain English</em>",
    "text": "<p>There are 19 ingredients in the two capsules, and you don’t need to remember any of their names, "
            "so here is what the main ones are there to do.</p>",
    "image_url": "", "image_alt": "", "image_position": "",
    "rows": lines(
        "B vitamins | Help reduce tiredness and fatigue, and all eight are in here in forms your body can use straight away.",
        "Vitamin D | Supports normal muscle function, which matters because most of us in the UK get too little sun from October to March.",
        "Zinc and copper | Help protect your cells from oxidative stress, which is the everyday wear and tear that goes on inside them.",
        "NR (a form of vitamin B3) | Your body turns it into NAD+, which every cell uses to make energy and which you have less of as you get older.",
        "CoQ10 | Plays a part in how your cells make energy, and your body makes less of it after your twenties.",
        "Creatine (free) | Helps with short bursts of hard effort, like the stairs or a sprint, and comes as a separate pouch that is free with your first subscription order."),
    "ticks": "",
    "cta": A.CTA, "cta_link": "",
    "foot": "Vitamins B2, B3, B5, B6, B12 and folate contribute to the reduction of tiredness and fatigue. "
            "Vitamin D contributes to the maintenance of normal muscle function. Zinc and copper contribute to "
            "the protection of cells from oxidative stress. Creatine increases physical performance in "
            "successive bursts of short-term, high-intensity exercise; the beneficial effect is obtained with "
            "a daily intake of 3g of creatine. Food supplements are not a substitute for a varied, balanced "
            "diet and a healthy lifestyle. If your tiredness is new, severe or doesn’t lift, speak to your GP. "
            "If you take medication, or are pregnant or breastfeeding, check with your doctor before taking "
            "supplements."}}

timeline = json.loads(json.dumps(A.timeline))
timeline["settings"]["heading"] = "What to expect, <em>week by week</em>"
timeline["settings"]["intro"] = ("This is a slow and steady change rather than a quick jolt, so it helps to "
                                 "score how your afternoons feel out of 10 on day 1 and then gently compare "
                                 "as the weeks go by.")

risk = text(
    "<p>We would much rather you tried it properly than took our word for it, so we ask you to take it every "
    "day for 90 days.</p>"
    "<p>If you don’t feel a difference in that time, you can email us within 14 days of your 90 days ending "
    "and we will refund every subscription payment, less the cost of delivery.</p>"
    "<p><strong>That way there is very little to lose by finding out whether it helps you feel more like "
    "yourself again.</strong></p>",
    heading="And if it isn’t for you, <em>you get your money back</em>")

blocks = [("opening", opening), ("familiar", familiar)]
blocks += [(f"m{i}", m) for i, m in enumerate(moments, 1)]
blocks += [("why", why), ("life", life), ("cta1", cta()),
           ("back", back), ("q1", q1), ("q2", q2), ("q3", q3), ("photo", photo),
           ("simple", simple), ("jar", jar), ("inside", inside),
           ("timeline", timeline), ("risk", risk),
           ("offer", A.offer), ("trust", A.trust)]

needs = {"type": "muto-lst-needs",
         "blocks": dict(blocks), "block_order": [k for k, _ in blocks],
         "settings": dict(header, hide_bf_bars=True, index_label="", count_label="Essential",
                          science_label="Research notes:", sources_label="Source")}

sections = {"needs": needs, "reviews": A.P["reviews"], "tests": A.P["tests"]}
path = os.path.join(HERE, "theme", "templates", NAME)
with open(path, "w", encoding="utf-8") as f:
    json.dump({"sections": sections, "order": list(sections)}, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", path, os.path.getsize(path), "bytes")
