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
    # Image overrides (people row and benefit cards)
    if p.get("people_images"):
        photos = [k for k in S["trust"]["block_order"] if S["trust"]["blocks"][k]["type"] == "photo"]
        for key, (url, alt) in zip(photos, p["people_images"]):
            S["trust"]["blocks"][key]["settings"].update(image="", image_fallback=url, alt=alt, position="")
    if p.get("benefit_images"):
        for key, (url, alt) in zip(("b1", "b2", "b3", "b4"), p["benefit_images"]):
            S["benefits"]["blocks"][key]["settings"].update(image="", image_fallback=url, image_alt=alt)
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


# ======================================================================================
# High performer, 30-40: three angles (energy, recovery, stress). Wearable-literate,
# career plus training. Images: the athlete shots. Buttons: the main product page.
# ======================================================================================
IMG = {k: CDN + v for k, v in {
    "feel": "nad-benefits-feel.jpg?v=1791019769", "track": "nad-benefits-track.jpg?v=1791020038",
    "tired": "nad-problem-tired.jpg?v=1791018569", "recovery": "nad-problem-recovery.jpg?v=1791018568",
    "data": "nad-problem-data.jpg?v=1791018568", "bottle": "nad-guarantee-bottle.jpg?v=1791023640",
    "wearable": "nad-check-wearable.jpg?v=1791017018", "baseline": "nad-step-baseline.jpg?v=1791020791",
    "steady": "nad-step-steady.jpg?v=1791020790", "checkin": "nad-step-checkin-close.jpg?v=1791021630",
    "verdict": "nad-step-verdict.jpg?v=1791020808", "harry": "home-athlete-harry.jpg?v=1791021221",
    "yolanda": "home-athlete-yolanda.jpg?v=1791021221", "kaisa": "home-athlete-kaisa.jpg?v=1791025477",
    "cyclist": "home-athlete-cyclist.jpg?v=1790767821"}.items()}
HP_PEOPLE = [(IMG["harry"], "A runner crossing open parkland"), (IMG["yolanda"], "An athlete in front of a row of treadmills"),
             (IMG["kaisa"], "An athlete running between stations at a HYROX event"), (IMG["cyclist"], "A cyclist on the drops in a time trial")]
HP_TRUST = [("award", "Built by a PhD cell biologist"), ("shield", "Made in the UK, every batch third-party tested"),
            ("label", "No caffeine, no stimulants")]
TRACK = ("How do I track it?", "<p>Take a 7-day baseline before your first capsule: HRV, resting heart rate, sleep and your recovery or readiness score, plus a 1–10 rating for how you feel. Then compare 30-day averages at day 30, 60 and 90. Single nights are noise; months are signal.</p>")
DEVICES = ("Which devices work?", "<p>Any device that records HRV, resting heart rate and sleep: Garmin, WHOOP, Oura, Apple Watch, Polar, Coros and others. Use the same one for the whole 90 days. No device? A weekly 1–10 check-in works too.</p>")
HP_ORDER = COMMON_ORDER

PERSONAS += [
    # ------------------------------------------------------------ HP: energy
    {"key": "hp-energy", "link": MAIN,
     "hero": {"image": "", "image_fallback": IMG["feel"],
              "image_alt": "A cyclist pausing mid-ride in the sun, sunglasses pushed up", "image_position": "50% 20%",
              "heading": "Big job.\nHard training.\nEnergy for both.",
              "body": "<p>MUTO is the daily cellular protocol for people running at full output: two capsules with breakfast, 19 ingredients, every dose on the label. Not a stimulant. A better baseline, judged on your own numbers.</p>",
              "strong": "Take a 7-day baseline on your wearable. Then give it 90 days."},
     "trust": HP_TRUST, "people_heading": "Built for people who\nrun at full output.", "people_images": HP_PEOPLE,
     "problem": {"pill": "Sound familiar?",
                 "heading": "Crushing the 6am session. Gone by the 4pm meeting.",
                 "lede": "You’ve optimised the training plan, the sleep and the macros. But the afternoons still fade, the third coffee does less than it used to, and the evening session gets whatever’s left.",
                 "reframe_heading": "Energy you make,\nnot energy you borrow.",
                 "reframe_text": "Your energy is made in your cells. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients, with B vitamins that contribute to normal energy-yielding metabolism and the reduction of tiredness and fatigue."},
     "pains": [("“Start well but fade later in the day.”", "The most common answer in our customer quiz."),
               ("“Tired of feeling tired.”", "However dialled-in the rest of the plan is."),
               ("Your third coffee is a loan.", "It borrows from 4pm, and 4pm always pays it back.")],
     "benefits": {"heading": "Full output, all day.",
                  "lede": "Not a pre-workout and not a buzz. A daily foundation, so the 4pm meeting and the 6pm session both get the version of you that turned up at 6am."},
     "benefit_cards": [
        ("Still sharp at 4pm.", "The pitch, the deadline, the late call. A steadier supply through the afternoon instead of a crash-and-coffee cycle."),
        ("Energy made in your cells.", "Not a stimulant or a quick hit. A daily routine that supports the system your energy actually comes from."),
        ("Something left for the evening session.", "A full workday shouldn’t mean skipping the session you planned. Turn up to it with something in the tank."),
        ("Built for high-output weeks.", "Big work weeks and big training weeks, back to back. One routine with breakfast, every day.")],
     "benefit_images": [(IMG["baseline"], "A cyclist checking the watch on their wrist"), (IMG["wearable"], "A runner checking a sports watch after a session"),
                        (IMG["steady"], "An athlete between sets in the gym"), (IMG["verdict"], "Three athletes laughing together after a session")],
     "reviews_heading": "<p>Energy, focus, training: what customers say about MUTO</p>",
     "faq": [("Is it a stimulant?", "<p>No. No caffeine and no stimulants, so there’s nothing to time around meetings or sessions. It’s a daily routine you judge over weeks, not hours.</p>"),
             ("Can I still drink coffee?", "<p>Yes. Take your two capsules with breakfast, coffee included.</p>"),
             TRACK, DEVICES, WORK, SUB],
     "offer_heading": "Start your 90 days today.", "offer2_heading": "Take your baseline. Start your 90 days.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": HP_ORDER},

    # ------------------------------------------------------------ HP: recovery
    {"key": "hp-recovery", "link": MAIN,
     "hero": {"image": "", "image_fallback": IMG["bottle"],
              "image_alt": "An athlete resting on a log after a session, drinking from a MUTO bottle", "image_position": "50% 10%",
              "heading": "Your readiness score says no.\nYour diary says go.",
              "body": "<p>MUTO is the daily cellular protocol for people who train hard and work harder: two capsules with breakfast, 19 ingredients, every dose on the label. Recovery starts underneath, so that’s where MUTO starts.</p>",
              "strong": "Take your baseline. Read the 30-day trend, not the single night."},
     "trust": HP_TRUST, "people_heading": "Built for people who\ntrain like it matters.", "people_images": HP_PEOPLE,
     "problem": {"pill": "Sound familiar?",
                 "heading": "Tuesday’s intervals. Wednesday’s dead legs.",
                 "lede": "The hard session is fine. It’s the one after it that tells you how you’re recovering. Add a heavy work week and short nights, and the readiness score stays red for days.",
                 "reframe_heading": "Recovery starts\nunderneath.",
                 "reframe_text": "Recovery happens in the cells that make your energy and run their repair work. MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients, with vitamin D, which contributes to the maintenance of normal muscle function."},
     "pains": [("“HRV been trash for months.”", "A real customer, before they started."),
               ("“Struggling with recovery according to Whoop.”", "Another, describing what their data showed."),
               ("Readiness says red. The plan says go.", "So you train anyway, or you skip and fall behind.")],
     "benefits": {"heading": "Ready for the next session.",
                  "lede": "You train to keep progressing, not to spend the week getting over it. Here’s what’s working underneath."},
     "benefit_cards": [
        ("Back for the next session.", "Thursday’s intervals shouldn’t still be in your legs on Sunday. Train, recover, go again."),
        ("Energy made in your cells.", "Your sessions run on the energy your cells make. MUTO supports that system every day, not just on training days."),
        ("Read the trend, not the night.", "Take a 7-day baseline, then compare 30-day averages of HRV, resting heart rate and sleep. Your data, your verdict."),
        ("Built for training blocks.", "Two capsules every day through the block, whatever the plan says. Nothing to time around sessions.")],
     "benefit_claims": {"b1": "Vitamin D contributes to the maintenance of normal muscle function.",
                        "b3": "Vitamins B6, B12 and folate contribute to the reduction of tiredness and fatigue."},
     "benefit_images": [(IMG["recovery"], "A runner catching her breath, hands on knees"), (IMG["tired"], "An athlete head down on a gym bike"),
                        (IMG["checkin"], "A wrist on an ice bath, the watch showing a live heart rate"), (IMG["baseline"], "A cyclist checking the watch on their wrist")],
     "reviews_heading": "<p>Recovery, training, routine: what customers say about MUTO</p>",
     "faq": [("Will it improve my HRV?", "<p>We won’t promise what any number will do. Take a 7-day baseline, read 30-day averages rather than single nights, and judge it yourself over 90 days. If you don’t see a difference, you’re covered.</p>"),
             ("When should I take it around training?", "<p>It doesn’t matter. Two capsules with your first meal, every day, training day or not. Consistency is what counts.</p>"),
             ("Can I take it with creatine and protein?", "<p>Yes. MUTO sits alongside creatine and protein; your first order even includes our Ultrapure Creatine.</p>"),
             TRACK, DEVICES, SUB],
     "offer_heading": "Start your 90 days today.", "offer2_heading": "Your next training block starts here.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": HP_ORDER},

    # ------------------------------------------------------------ HP: stress
    {"key": "hp-stress", "link": MAIN,
     "hero": {"image": "", "image_fallback": IMG["data"],
              "image_alt": "Two athletes at a table reading a recovery score on a phone", "image_position": "50% 60%",
              "heading": "Work stress.\nTraining stress.\nOne recovery budget.",
              "body": "<p>Your body doesn’t keep separate accounts. A deadline week and a threshold session draw from the same place, and your HRV shows it. MUTO is one daily foundation for high-output weeks: two capsules with breakfast, every dose on the label.</p>",
              "strong": "Not a calming pill. A daily foundation you can check."},
     "trust": HP_TRUST, "people_heading": "Built for people who\ncarry a lot, and still train.", "people_images": HP_PEOPLE,
     "problem": {"pill": "Sound familiar?",
                 "heading": "HRV down. Deadline up.",
                 "lede": "Launch week, a sick kid, a red-eye, a race block. You’ve read about cortisol and stress load, and you can see it in your numbers: the heavy weeks land in your sleep score and your morning HRV.",
                 "reframe_heading": "It all lands\nin the same place.",
                 "reframe_text": "Stress, training and short nights all draw on the same reserves. MUTO is one daily foundation: B vitamins that contribute to normal psychological function, pantothenic acid for normal mental performance, and NAD+ support for the cells that make your energy."},
     "pains": [("Always on. Never off.", "Work, home and training, with no gap between them."),
               ("The deadline lands in your sleep score.", "You can see the heavy weeks in your data before you feel them."),
               ("Busy weeks drain more than any session.", "The training isn’t the hard part. Everything around it is.")],
     "benefits": {"heading": "A steadier head in heavy weeks.",
                  "lede": "It won’t make a hard week easy. It’s a daily foundation for the weeks when work, life and training all peak at once."},
     "benefit_cards": [
        ("Steady when it all peaks.", "Launch week, board week, race week: same body. One routine that doesn’t change when everything else does."),
        ("Energy that lasts the week.", "Not a spike to get through Monday. A steadier supply for Thursday and Friday too."),
        ("Clearer thinking under load.", "The decisions still need making at 5pm. Support for normal mental performance, every day."),
        ("Built for high-output weeks.", "Big work weeks and big training weeks, back to back. One routine with breakfast.")],
     "benefit_claims": {"b1": "Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function.",
                        "b2": "Vitamins B6, B12 and folate contribute to the reduction of tiredness and fatigue.",
                        "b3": "Pantothenic acid contributes to normal mental performance."},
     "benefit_images": [(IMG["data"], "Two athletes reading a recovery score on a phone"), (IMG["feel"], "A cyclist pausing mid-ride in the sun"),
                        (IMG["wearable"], "A runner checking a sports watch after a session"), (IMG["verdict"], "Three athletes laughing together after a session")],
     "reviews_heading": "<p>Focus, energy, routine: what customers say about MUTO</p>",
     "faq": [("Does MUTO lower cortisol?", "<p>No, and we won’t claim it does. There’s no authorised claim for that, and you should be wary of anyone who makes one. MUTO contains B vitamins that contribute to normal psychological function, and pantothenic acid for normal mental performance. To see how heavy weeks land, track HRV, resting heart rate and sleep through the 90 days.</p>"),
             ("Is it a calming supplement?", "<p>No. It isn’t a sedative or an adaptogen blend, and it won’t make a hard week easy. It’s a daily foundation you take with breakfast and judge over 90 days.</p>"),
             ("Is it a stimulant?", "<p>No caffeine and no stimulants, so nothing to time around your day.</p>"),
             TRACK, WORK, SUB],
     "offer_heading": "Start your 90 days today.", "offer2_heading": "One foundation for heavy weeks.",
     "bar": "Welcome offer: £122 of value for £60 on your first subscription, and 90 days to decide.",
     "order": HP_ORDER},
]

if __name__ == "__main__":
    for p in PERSONAS:
        build(p)
