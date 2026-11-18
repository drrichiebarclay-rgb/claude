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
    headline="You’re not lazy. You’re <em>running on empty.</em>",
    standfirst="Why so many people over 35 feel flat by mid-afternoon, and the two-capsule morning habit "
               "thousands of them have switched to.",
)

opening = text(
    "<p>You used to have more in the tank.</p>"
    "<p>Now you’re fine until about 3pm. Then everything gets heavier.</p>"
    "<p><strong>Another coffee. A slow afternoon. Nothing left by the time you get home.</strong></p>"
    "<p>You’re doing most things right. You eat well, you move, you get to bed at a sensible time.</p>"
    "<p>And you still don’t feel like yourself.</p>",
    heading="Remember when you could <em>just go again?</em>")

familiar = text(
    "<p>If you’re over 35, you’ll probably recognise at least a couple of these.</p>",
    heading="Sound <em>familiar?</em>")

moments = [
    need("", "The 3pm crash", "",
         "<p>Fine all morning. Then mid-afternoon arrives and you’re reaching for a coffee you know you "
         "shouldn’t have.</p>", [], []),
    need("", "Brain fog when you need to be sharp", "",
         "<p>Slow thinking in the one meeting where you need to be 100% there.</p>", [], []),
    need("", "Heavy legs the next day", "",
         "<p>A walk, a run or a gym session you used to shake off is still in your legs on the stairs two "
         "days later.</p>", [], []),
    need("", "Nothing left for the evening", "",
         "<p>You get through work. Then there’s nothing in the tank for the people at home, and you can’t "
         "just lie on the sofa.</p>", [], []),
    need("", "Waking up groggy", "",
         "<p>A full night in bed, and you still don’t feel ready for the day.</p>", [], []),
]

why = {"type": "dark", "settings": {
    "label": "Why it happens",
    "heading": "It’s not in your head. Your body has changed.",
    "text": "<p>From your mid-30s, your body gets less efficient at turning food into energy. Scientists have "
            "measured it: between your late 30s and late 60s, your muscles’ capacity to make energy roughly "
            "halves.</p>"
            "<p>That’s biology. It isn’t willpower, and it isn’t laziness.</p>",
    "step_1_title": "", "step_1_text": "", "step_2_title": "", "step_2_text": "",
    "step_3_title": "", "step_3_text": "",
    "end": "And another coffee doesn’t fix it. Caffeine only hides the tiredness. It comes back when the "
           "coffee wears off.",
    "refs": "Conley KE, Jubrias SA, Esselman PC. Oxidative capacity and ageing in human muscle. J Physiol. 2000."}}

life = text(
    "<p>Life doesn’t stop while you sort it out. Work. Kids. Travel. People who rely on you.</p>"
    "<p>And not everybody is a 25-year-old PT who can build their whole life around a perfect routine.</p>"
    "<p><strong>You need something that fits the life you actually have.</strong></p>",
    heading="You can’t just <em>take a week off</em>")

photo = {"type": "image", "settings": {
    "image_url": CDN + "Golden_Hour_Family_Beach_Walk.png?v=1792566215",
    "image_alt": "A family walking along a beach at sunset with their dog", "image_position": "50% 50%", "caption": ""}}

back = text(
    "<p>We asked. These are their words, not ours.</p>",
    heading="What people say they <em>got back</em>")

q1 = quote("“No afternoon slump and in general feeling great”", "Lynda", RV, stars=True)
q2 = quote("“I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore.”",
           "Danny S", RV, stars=True)
q3 = quote("“I didn't realise how flat I'd been feeling until this helped lift me out of it”", "Holly P", RV, stars=True)

simple = text(
    "<p><strong>MUTO NAD+ Cellular Complex</strong> is two capsules with breakfast. That’s it.</p>"
    "<ul><li>Nothing to mix, nothing to carry around</li>"
    "<li>No caffeine and no stimulants, so nothing to crash from</li>"
    "<li>One jar in place of a cupboard full of pots</li>"
    "<li>A habit as easy as brushing your teeth</li></ul>"
    "<p>It was made by a cell biologist for adults over 35. You don’t need to be sporty, and you don’t need "
    "a smartwatch.</p>",
    heading="Two capsules. <em>Every morning.</em>")

jar = {"type": "image", "settings": {
    "image_url": CDN + "lp-over-35-hero.jpg?v=1794239299",
    "image_alt": "A woman at her kitchen table in morning light, taking a capsule beside a glass of water and a jar "
                 "of MUTO NAD+ Cellular Complex", "image_position": "50% 40%", "caption": ""}}

inside = {"type": "answer", "settings": {
    "label": "",
    "heading": "What’s inside, <em>in plain English</em>",
    "text": "<p>19 ingredients in two capsules. You don’t need to remember the names. Here’s what the main "
            "ones do.</p>",
    "image_url": "", "image_alt": "", "image_position": "",
    "rows": lines(
        "B vitamins | Help reduce tiredness and fatigue. All eight are in here, in forms your body can use straight away.",
        "Vitamin D | Supports normal muscle function. Most of us in the UK get too little sun from October to March.",
        "Zinc and copper | Help protect your cells from oxidative stress, which is everyday wear and tear inside your cells.",
        "NR (a form of vitamin B3) | Your body turns it into NAD+, which every cell uses to make energy. You have less NAD+ as you get older.",
        "CoQ10 | Part of how your cells make energy. Your body makes less of it after your twenties.",
        "Creatine (free) | For short bursts of hard effort, like the stairs or a sprint. It comes as a separate pouch, free with your first subscription order."),
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
timeline["settings"]["intro"] = ("It’s a long burn, not a quadruple espresso. Score how your afternoons feel "
                                 "out of 10 on day 1, then compare.")

risk = text(
    "<p>Take it every day for 90 days.</p>"
    "<p>If you don’t feel a difference, email us within 14 days after your 90 days end and we’ll refund every "
    "subscription payment, less delivery.</p>"
    "<p><strong>So what have you got to lose?</strong></p>",
    heading="Not for you? <em>Your money back.</em>")

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
