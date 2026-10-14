"""Build the MP2, MP3 and MP5 landing pages from the MP1 page (page.lp-mp1.json).

Same sections and design; each persona gets its own way in, per the Messaging House
"Not Done Yet" (10 Oct 2026): hero, problem in their words, reframe, benefit framing,
section order, trust signals, FAQ objections, images, close and product link.
Claims guardrails unchanged: pain described, results never promised, nutrient claims
worded exactly; invented lines are never shown as customer quotes.

Run make_lp.py first, then: python3 build_personas.py
"""
import copy, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = json.load(open(os.path.join(HERE, "page.lp-mp1.json")))
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"
MAIN = "/products/muto-nad-cellular-complex"
PDP_45 = "/products/muto-nad-cellular-complex-2"
CTA = "Start your 90 days"


def faq(items):
    return {f"q{i}": {"type": "q", "settings": {"q": q, "a": a}} for i, (q, a) in enumerate(items, 1)}, \
           [f"q{i}" for i in range(1, len(items) + 1)]


def build(p):
    d = copy.deepcopy(BASE)
    S = d["sections"]
    link = p["link"]
    # Product link everywhere
    for k in ("lp_hero", "value", "offer", "offer2", "bar"):
        S[k]["settings"]["cta_link"] = link
    S["lp_hero"]["settings"]["schema_product"] = link.rsplit("/", 1)[-1]
    # Hero
    S["lp_hero"]["settings"].update(p["hero"])
    # Trust strip + people heading
    for key, (icon, text) in zip(("t1", "t2", "t3"), p["trust"]):
        S["trust"]["blocks"][key]["settings"].update(icon=icon, text=text)
    S["trust"]["settings"]["heading"] = p["people_heading"]
    # Problem
    S["problem"]["settings"].update(p["problem"])
    for key, (q, t) in zip(("x1", "x2", "x3"), p["pains"]):
        S["problem"]["blocks"][key]["settings"].update(quote=q, text=t)
    # Benefits: titles and lines (claims and photos stay)
    S["benefits"]["settings"].update(p["benefits"])
    for key, (title, line) in zip(("b1", "b2", "b3", "b4"), p["benefit_cards"]):
        S["benefits"]["blocks"][key]["settings"].update(title=title, line=line)
    if p.get("benefit_claims"):
        for key, claim in p["benefit_claims"].items():
            S["benefits"]["blocks"][key]["settings"]["text"] = claim
    # Value
    S["value"]["settings"].update(p.get("value", {}))
    # Experts: optionally drop the athletes
    if p.get("experts_heading"):
        S["experts"]["settings"]["heading"] = p["experts_heading"]
    if p.get("drop_athletes"):
        keep = [k for k in S["experts"]["block_order"]
                if S["experts"]["blocks"][k]["settings"]["role"] != "Athlete"]
        S["experts"]["blocks"] = {k: S["experts"]["blocks"][k] for k in keep}
        S["experts"]["block_order"] = keep
    # Reviews heading
    S["reviews"]["settings"]["heading"] = p["reviews_heading"]
    # FAQ
    S["lp_faq"]["blocks"], S["lp_faq"]["block_order"] = faq(p["faq"])
    # Offers and bar
    S["offer"]["settings"]["heading"] = p["offer_heading"]
    S["offer2"]["settings"]["heading"] = p["offer2_heading"]
    S["bar"]["settings"]["text"] = p["bar"]
    # Order
    d["order"] = p["order"]
    assert set(d["order"]) == set(S), set(S) ^ set(d["order"])
    out = os.path.join(HERE, f"page.lp-{p['key']}.json")
    json.dump(d, open(out, "w"), ensure_ascii=False, indent=2)
    open(out, "a").write("\n")
    print("wrote", out)


COMMON_ORDER = ["lp_hero", "trust", "problem", "benefits", "value", "offer",
                "formula", "reviews", "experts", "lp_faq", "offer2", "bar"]

SAFE = ("Is it safe with what I already take?",
        "<p>Usually, yes. If you take medicine, check with your GP first, and don’t stop anything you take for a medical reason.</p>")
SUB = ("Am I locked into a subscription?",
       "<p>No. Skip, pause or cancel online, any time. We remind you 5 days before every payment.</p>")
WORK = ("Will it work for me?",
        "<p>We won’t promise what it’ll do for you. Note your starting point, give it 90 days, and judge it yourself. If you don’t see a difference, you’re covered.</p>")
INSIDE = ("What’s actually in it?",
          "<p>19 ingredients, every dose on the label: 300mg NR (the most allowed in Great Britain), a full B complex, vitamin D3 and K2, zinc, copper, CoQ10, PQQ, TMG, grapeseed, trans-resveratrol and BioPerine®. Ask your AI, your GP, or Richie, who answers formula questions himself.</p>")

PERSONAS = [
    # ---------------------------------------------------------------- MP2
    {"key": "mp2", "link": PDP_45,
     "hero": {
        "image": "", "image_fallback": CDN + "nad-take-two.jpg?v=1791017315",
        "image_alt": "Two MUTO capsules in an open palm beside the jar, a glass of water and breakfast",
        "image_position": "50% 45%",
        "heading": "Sharp at 8am.\nGone by 3pm.\nIt’s not your willpower.",
        "body": "<p>MUTO is one daily routine for busy lives: two capsules with breakfast, 19 ingredients, every dose on the label. Not a boost or a buzz. A better baseline, so there’s still something left for the people who need you at 6pm.</p>",
        "strong": "Note how you feel at 3pm today. Then give it 90 days."},
     "trust": [("label", "No caffeine, no stimulants"), ("shield", "Made in the UK, every batch third-party tested"),
               ("award", "Built by a PhD cell biologist")],
     "people_heading": "Built for the people\neveryone else relies on.",
     "problem": {
        "pill": "Sound familiar?",
        "heading": "It’s 3:12pm. You’ve read the same email four times.",
        "lede": "The morning goes fine. Then the afternoon drags, the third coffee does less than it used to, and by the 6pm handover the people who need you most get what’s left.",
        "reframe_heading": "It isn’t willpower.\nIt starts underneath.",
        "reframe_text": "Your energy is made in your cells. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients, with B vitamins that contribute to the reduction of tiredness and fatigue. One routine with breakfast, judged by your afternoons."},
     "pains": [("“Tired of feeling tired.”", "However well you slept."),
               ("“Flagging by mid-afternoon.”", "Sharp in the morning, running on fumes by 3."),
               ("“More mentally drained than physically sore.”", "Work, family and everything in between.")],
     "benefits": {"heading": "Be all there, all day.",
                  "lede": "Not superpowers. Just being the person you want to be at 3pm and at 6pm, for work and for the people at home."},
     "benefit_cards": [
        ("Still all there at 6pm.", "The late meeting, the school run, bath time. Fully present for all of it, not running on fumes by the end of the day."),
        ("Not a boost. A better baseline.", "No caffeine and no quick hit. A daily routine that supports the system your energy actually comes from, deep in your cells."),
        ("Your third coffee is a loan.", "Coffee borrows from later in the day. MUTO is a routine with breakfast, not another hit to time around your diary."),
        ("Look after yourself, too.", "You look after everyone else. Two capsules with breakfast is ten seconds a day for you.")],
     "benefit_claims": {"b3": "Vitamins B6 and B12 contribute to normal psychological function.",
                        "b4": "Zinc, copper and riboflavin contribute to the protection of cells from oxidative stress."},
     "reviews_heading": "<p>Afternoons, focus, routine: what customers say about MUTO</p>",
     "faq": [("Is it a stimulant?", "<p>No. No caffeine and no stimulants, so there’s nothing to time around your day. It’s a daily routine you judge over weeks, not hours.</p>"),
             ("Can I still drink coffee?", "<p>Yes. Take your two capsules with breakfast, coffee included.</p>"),
             ("Is it suitable for women?", "<p>Yes. MUTO is made for adults, and about a third of our customers are women. It’s not for anyone pregnant or breastfeeding, and if you take medicine, check with your GP first.</p>"),
             ("How will I know if it’s working?", "<p>Note how you feel at 3pm today, out of 10. Do the same once a week. At day 30 and day 90, compare. If you wear a watch, its 30-day averages work too.</p>"),
             WORK, SUB],
     "offer_heading": "Start your 90 days today.", "offer2_heading": "Note how you feel at 3pm today.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": COMMON_ORDER},

    # ---------------------------------------------------------------- MP3
    {"key": "mp3", "link": PDP_45,
     "hero": {
        "image": "shopify://shop_images/Frame_2147230149.png", "image_fallback": "",
        "image_alt": "A jar of MUTO NAD+ Cellular Complex on a shelf among separate supplement pots",
        "image_position": "50% 50%",
        "heading": "Five supplements.\nNo idea which one’s working.",
        "body": "<p>MUTO is one daily protocol instead of a cupboard of guesses: 19 ingredients, every dose on the label, built by a PhD cell biologist. Ask your AI what’s in it. Then give it 90 days and judge it yourself.</p>",
        "strong": "£5.25 a day bought separately. £2 a day in two capsules."},
     "trust": [("label", "Every dose on the label, no proprietary blends"), ("shield", "Made in the UK, every batch third-party tested"),
               ("award", "Built by a PhD cell biologist")],
     "people_heading": "Built for people who\nread the label first.",
     "problem": {
        "pill": "Sound familiar?",
        "heading": "Count the pots on your kitchen side.",
        "lede": "You do your research. You spend £100 or more a month on your health. And you still can’t say which of those pots is doing anything, because none of them can be checked.",
        "reframe_heading": "Stop guessing.\nStart checking.",
        "reframe_text": "One protocol, every dose on the label, and 90 days to judge it against your own starting point. If you don’t see a difference, you’re covered."},
     "pains": [("“Several supplements, unsure what’s working.”", "The reorder emails keep coming. The answers don’t."),
               ("“Looking at all my pill bottles…”", "Five products, overlapping doses, one cluttered routine."),
               ("“No hype. I want science.”", "Proprietary blends and big promises, with nothing you can check.")],
     "benefits": {"heading": "One routine. Nothing hidden.",
                  "lede": "The point isn’t more pills. It’s knowing exactly what you take, why it’s there, and whether it’s doing anything."},
     "benefit_cards": [
        ("Energy, accounted for.", "Every B vitamin at a declared dose, in the active forms, instead of a guess spread across three pots."),
        ("One label to read.", "19 ingredients, each with its dose and the reason it’s there. Paste it into your AI and ask what it thinks."),
        ("Built for people who train.", "Vitamin D3 at a daily dose rather than a token one, with K2 alongside it, in the same two capsules."),
        ("Less on the kitchen side.", "One jar with breakfast. Fewer reorders, fewer overlapping doses, one routine you can actually judge.")],
     "value": {"heading": "Eleven pots.\nTwo capsules.",
               "body": "Bought separately at similar doses, MUTO’s ingredients cost about £5.25 a day and fill a shelf. In MUTO they’re £2 a day in two capsules, every dose on the label."},
     "reviews_heading": "<p>One routine instead of many: what customers say about MUTO</p>",
     "faq": [("What does MUTO replace?", "<p>For many customers, several separate pots: B vitamins, vitamin D3, K2, zinc and CoQ10 are all in here, at the doses shown. Never stop anything you take for a medical reason, and check with your GP if you take medicine.</p>"),
             INSIDE,
             ("Is it worth the money?", "<p>Bought separately at similar doses, the ingredients cost about £5.25 a day. MUTO is £2 a day on subscription, and you have 90 days to decide.</p>"),
             ("Why no proprietary blend?", "<p>Because you can’t check a blend. Every ingredient and every dose is on the label, so you, your GP or your AI can see exactly what you’re taking.</p>"),
             WORK, SUB],
     "offer_heading": "Swap the guesswork for a 90-day test.", "offer2_heading": "One protocol. 90 days. Your call.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": ["lp_hero", "trust", "problem", "value", "benefits", "offer",
               "formula", "reviews", "experts", "lp_faq", "offer2", "bar"]},

    # ---------------------------------------------------------------- MP5 (the Wake-Up Call)
    {"key": "mp5", "link": PDP_45,
     "hero": {
        "image": "shopify://shop_images/42FB6D71-CEAF-4B0A-962A-E043F6098596.png", "image_fallback": "",
        "image_alt": "A man in his fifties packing his bag after a ride",
        "image_position": "40% 35%",
        "heading": "Live better\nfor longer.",
        "body": "<p>Some moments make you think about the years ahead: a birthday, a check-up, a friend’s news. MUTO is one small daily habit for the long game, built by a PhD cell biologist and reviewed by doctors: two capsules with breakfast, every dose on the label.</p>",
        "strong": "No promises to turn back the clock. Just a habit you can check, with 90 days to decide."},
     "trust": [("award", "Built by a PhD cell biologist"), ("shield", "Reviewed by our Scientific Advisory Board of doctors and scientists"),
               ("flask", "Research underway with 4 UK universities")],
     "people_heading": "Built for people with\nplenty still to do.",
     "problem": {
        "pill": "The moment it clicks",
        "heading": "The day you decide the next twenty years matter.",
        "lede": "It might be a milestone birthday, a scare, or watching someone you love slow down. Whatever it was, you want to keep doing what you love, for longer, and you want something you can trust to help you start.",
        "reframe_heading": "Biology sets limits.\nWe intend to move them.",
        "reframe_text": "Ageing shows up first in the cells that make your energy and run their repair work. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients, in one routine you can check yourself."},
     "pains": [("“My health has begun deteriorating.”", "A real customer, describing the moment they started."),
               ("“Heading towards 60, I’m taking longer to recover from hard training sessions.”", "Another, on what changed first."),
               ("A cupboard of supplements and no plan.", "Plenty of products. No idea which ones matter.")],
     "benefits": {"heading": "For the years ahead.",
                  "lede": "Not a cure and not a miracle. A daily habit that supports how your body makes energy and protects its cells, so you can keep doing what you love."},
     "benefit_cards": [
        ("Keep up with the people you love.", "The walk with the grandchildren, the round of golf, the long weekend away. The things that make the years worth having."),
        ("Energy made in your cells.", "Not a stimulant or a quick hit. A daily routine that supports the system your energy actually comes from."),
        ("Stay strong and steady.", "Vitamin D at a daily dose, with K2 beside it, for the muscles and bones that keep you moving."),
        ("A habit for the long game.", "Two capsules with breakfast, every day. Small enough to keep for years, clear enough to check.")],
     "benefit_claims": {"b3": "Vitamin D contributes to the maintenance of normal muscle function and normal bones."},
     "experts_heading": "Built by a scientist.\nReviewed by doctors.",
     "drop_athletes": True,
     "reviews_heading": "<p>In their own words: what customers say about MUTO</p>",
     "faq": [("I take medication. Can I take MUTO?", "<p>Check with your GP first, especially if you take a blood thinner such as warfarin. Never stop anything you take for a medical reason. MUTO is a food supplement, not a medicine.</p>"),
             ("Is this anti-ageing?", "<p>No. MUTO won’t reverse ageing, and nothing you swallow will. It supports the cells beneath your energy and recovery through NAD+ and other nutrients, and you get 90 days to judge it yourself.</p>"),
             ("Who is behind it?", "<p>Dr Richie Barclay, PhD in cellular biology and nutrition, with a Scientific Advisory Board of doctors and scientists. MUTO is being studied with four UK universities, and we’ll publish what we find.</p>"),
             INSIDE, WORK, SUB],
     "offer_heading": "Start the habit today.", "offer2_heading": "Your next decade starts with one small habit.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": ["lp_hero", "trust", "problem", "benefits", "formula", "experts", "reviews",
               "value", "offer", "lp_faq", "offer2", "bar"]},
]

if __name__ == "__main__":
    for p in PERSONAS:
        build(p)
