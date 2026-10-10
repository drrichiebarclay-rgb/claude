"""Copy update for the NAD+ PDP (templates/product.muto-nad.json), 10 Oct 2026.

Usage: python3 apply_copy_oct10.py <current template> <output template>
"""
import json
import sys

src, out = sys.argv[1], sys.argv[2]
raw = open(src).read()
head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
S = d["sections"]

EMAIL = '<a href="mailto:hello@mutolongevity.com">hello@mutolongevity.com</a>'


def set_blocks(sec, btype, items, make):
    """Replace every block of btype with new ones, keeping their slot in block_order."""
    order = sec["block_order"]
    old = [b for b in order if sec["blocks"][b]["type"] == btype]
    pos = order.index(old[0]) if old else len(order)
    for b in old:
        del sec["blocks"][b]
    order[:] = [b for b in order if b not in old]
    new_ids = []
    for n, item in enumerate(items, 1):
        bid = f"{btype}_{n}"
        sec["blocks"][bid] = {"type": btype, "settings": make(item)}
        new_ids.append(bid)
    order[pos:pos] = new_ids


# --- Buy box -------------------------------------------------------------------
buy = S["buy"]
for bid, text in zip(["b1", "b2", "b3", "b4"], [
    "Keep your energy all day, not just the morning",
    "Bounce back from hard sessions like you used to",
    "Stay the strong, capable one for longer",
    "Feel the difference in 90 days, or your money back",
]):
    buy["blocks"][bid]["settings"]["text"] = text

buy["settings"]["text"] = (
    "<p>For people who aren’t ready to slow down. Two capsules a day supporting the 30 trillion cells "
    "beneath your energy, recovery and how you age, built around NAD+ and 18 other nutrients. "
    "Every dose on the label. 90 days to decide for yourself.</p>"
)

set_blocks(buy, "term", [
    "90-day money-back guarantee",
    "Free next-day delivery",
    "With your first order: performance socks, Forever Jar, 12-week protocol guide",
    "A thank-you gift with each order up to month 6",
    'Entry to our Oura Ring 5 prize draw (<a href="/pages/better-baseline-giveaway">T&amp;Cs</a>)',
    "Skip, pause or cancel online, with a reminder 5 days before each payment",
], lambda t: {"text": t, "plans": ""})

# Review snippets go straight after the terms block group (rendered under the button).
set_blocks(buy, "snippet", [
    ("“No afternoon slump and in general feeling great”", "Lynda"),
    ("“More focused during the day”", "Alexandra"),
    ("“Has actually changed my recovery”", "Adam H"),
], lambda q: {"quote": q[0], "name": q[1]})

buy["blocks"]["a3"]["settings"]["title"] = "How to take it"

# --- The problem ---------------------------------------------------------------
S["problem"]["settings"]["heading"] = "You’re not done yet.\nSo why does it\nfeel harder?"
S["problem"]["settings"]["lede"] = (
    "The training, the long days, the cupboard of supplements. But the afternoons fade sooner and "
    "sessions take longer to bounce back from. Most supplements ask you to trust they’re working. "
    "We’d rather you check."
)

# --- Why MUTO ------------------------------------------------------------------
why = S["why"]["blocks"]
why["w1"]["settings"].update({
    "title": "Built by a scientist\nyou can talk to.",
    "text": "Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by our "
            "Scientific Advisory Board. Got a question? Ask him.",
    "image": "shopify://shop_images/about-founder.jpg",
    "image_fallback": "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/about-founder.jpg?v=1790751995",
    "image_alt": "Dr Richie Barclay holding a jar of NAD+ Cellular Complex",
    "image_position": "50% 20%",
})
why["w2"]["settings"].update({
    "title": "Nothing hidden.",
    "text": "Nineteen ingredients, each on the label with its dose and why it’s there. No proprietary "
            "blends. Made in the UK to GMP standards. Ask your AI to check it.",
})
why["w3"]["settings"].update({
    "title": "Built to be checked.",
    "text": "Note how you feel on day 0, then check in at day 30 and day 90, in how your days feel, "
            "your training or your wearable. Your verdict, with a 90-day guarantee behind it.",
})

# --- Scientific board / Real results -----------------------------------------------
S["board"]["settings"]["note"] = (
    "Our Scientific Advisory Board: scientists and clinicians in performance, metabolism and longevity."
)
S["results"]["settings"]["note"] = "Ninety days, in their own words"

# --- Benefits --------------------------------------------------------------------
ben = S["benefits"]
ben["blocks"]["pf"]["settings"].update({
    "heading": "What people\nnotice first",
    "lede": "What customers tell us they notice first. Individual experiences, not a promise. "
            "Open any of them for more.",
})
ben["blocks"]["f1"]["settings"]["sub"] = "“No afternoon slump and in general feeling great” – Lynda"
ben["blocks"]["f2"]["settings"]["sub"] = "“Has actually changed my recovery” – Adam H"

ben["blocks"]["pt"]["settings"].update({
    "label": "Ways to check",
    "heading": "Three ways\nto check it",
    "lede": "Use whichever suits you, or all three. Compare against your own starting point at day 30, 60 and 90.",
})
track = [b for b in ben["block_order"] if ben["blocks"][b]["type"] == "benefit"
         and ben["blocks"][b]["settings"]["panel"] == "track"]
pos = ben["block_order"].index(track[0])
for b in track:
    del ben["blocks"][b]
ben["block_order"] = [b for b in ben["block_order"] if b not in track]
new_track = [
    ("ck1", "A weekly how-I-feel check-in", "30 seconds, no device needed",
     "<p>Once a week, rate your energy, sleep, afternoons and mood out of 10. Felt changes are easy to "
     "forget, so writing them down turns a feeling into a record you can look back on.</p>"),
    ("ck2", "Your training log", "What your sessions tell you",
     "<p>Note how hard sessions felt and how ready you were for the next one. Compare a similar week at "
     "day 0, day 30 and day 90.</p>"),
    ("ck3", "Your wearable’s 30-day averages", "HRV, resting heart rate, recovery",
     "<p>Single nights are noisy. Compare 30-day averages for HRV, resting heart rate and recovery or "
     "readiness against your own baseline, not anyone else’s number.</p>"),
]
for bid, title, sub, text in new_track:
    ben["blocks"][bid] = {"type": "benefit", "settings": {"panel": "track", "title": title, "sub": sub, "text": text}}
ben["block_order"][pos:pos] = [t[0] for t in new_track]

# --- Ingredients -----------------------------------------------------------------
ing = S["ingredients"]
ing["settings"].update({
    "heading": "Nineteen ingredients.\nEvery dose on the label.",
    "heading_right": "",
    "lede": "MUTO supports the 30 trillion cells in your body through NAD+ and other nutrients.\n"
            "Already taking D3, K2, B vitamins, zinc, copper or CoQ10 separately? They’re in here, at the doses shown.",
})
for b in ing["blocks"].values():  # retire the Produce / Protect / Put to work filter
    b["settings"]["group"] = ""

# --- 90-day test -----------------------------------------------------------------
steps = S["steps"]
steps["settings"].update({"heading": "Not a quick fix.", "heading_right": "A 90-day test."})
steps["blocks"]["s1"]["settings"].update({
    "chip": "Day 0",
    "text": "Note your starting point: a 30-second how-I-feel check-in, or a 7-day average if you wear a device.",
})
steps["blocks"]["s4"]["settings"].update({"title": "Your verdict.", "text": "If it’s not for you, you’re covered."})

# --- FAQs ------------------------------------------------------------------------
faq = S["faq"]
faq_items = [
    ("q1", None, None),  # "How will I know if it's working?" stays as is
    ("q6", "Do I need a wearable?",
     "<p>No. A wearable makes tracking easier, but a 30-second weekly check-in (energy, sleep, afternoons, "
     "mood, each out of 10) works too. Writing it down is what turns a feeling into a record you can look back on.</p>"),
    ("q2", "When might I notice something?",
     "<p>Give it 60 to 90 days, taken daily, before you judge it. Some people notice a difference in their "
     "energy or recovery within the first few weeks; others notice nothing early on. Read wearable data as "
     "30-day averages, not single nights. That’s why the guarantee runs for 90 days.</p>"),
    ("q3", "Is it safe with my other supplements?",
     "<p>In most cases, yes, and coffee is fine. Watch for doubling up: a separate B complex, zinc, vitamin D, "
     "K2 or NAD+ product will overlap with what’s already in MUTO, so check your other labels against ours. "
     "If you take prescription medicine, check with your GP or pharmacist first: MUTO contains vitamin K2 "
     "(100µg), which can affect blood thinners such as warfarin. Not for use during pregnancy or "
     "breastfeeding, or for anyone under 18.</p>"),
    ("q4", "What if it’s not for me?",
     "<p>If you subscribe, take MUTO daily and don’t see a difference within 90 days, we’ll refund every "
     "subscription payment you’ve made in that time, less our delivery costs. Email " + EMAIL + " within 90 "
     "days of your first order with your name, order number and a line on your experience, and we’ll refund "
     "your original payment method within 7 working days. You don’t need to send any wearable data.</p>"
     "<p>The guarantee covers first-time subscribers buying at muto.co, one claim per customer. One-time "
     "purchases and orders through Amazon or other retailers aren’t covered. You can skip, pause or cancel "
     "online at any time.</p>"),
    ("q5", "Why not just take NR on its own?",
     "<p>You can, but NR alone covers one input. MUTO pairs it with nutrients that have authorised roles in "
     "how your body makes and uses energy (B vitamins and copper for normal energy-yielding metabolism, zinc "
     "for protecting cells from oxidative stress), plus CoQ10, TMG, resveratrol and PQQ. One routine instead "
     "of several separate products.</p>"),
]
for bid, title, text in faq_items:
    if title is None:
        continue
    faq["blocks"][bid] = {"type": "q", "settings": {"title": title, "text": text}}
faq["block_order"] = [b for b, _, _ in faq_items]

open(out, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("buy blocks:", len(buy["block_order"]), "faq:", faq["block_order"])
