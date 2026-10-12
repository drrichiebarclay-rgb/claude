"""Simple-language NAD+ product page: templates/product.muto-nad-simple.json.

Same sections, images, prices and links as product.muto-nad.json; only the words change.
Aim: short words, short sentences, one idea per line, for readers around 50 who want it quick.
Customer quotes stay verbatim (fewer of them). Prices and plan numbers are untouched.

Usage: python3 make_simple.py base-product.muto-nad.json product.muto-nad-simple.json
"""
import json
import sys

src, out = sys.argv[1], sys.argv[2]
raw = open(src).read()
head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
S = d["sections"]
EMAIL = '<a href="mailto:hello@mutolongevity.com">hello@mutolongevity.com</a>'
TRY = "Try it for 90 days"


def setb(sec, bid, **kw):
    S[sec]["blocks"][bid]["settings"].update(kw)


def keep_blocks(sec, btype, keep):
    s = S[sec]
    drop = [b for b in s["block_order"] if s["blocks"][b]["type"] == btype and b not in keep]
    for b in drop:
        del s["blocks"][b]
    s["block_order"] = [b for b in s["block_order"] if b not in drop]


# --- Buy box -----------------------------------------------------------------------
b = S["buy"]["settings"]
b.update({
    "serving": "60 capsules | 30 days | 2 a day",
    "text": ("<p>MUTO is a daily supplement to help you keep your energy as you get older.</p>"
             "<p>Your body needs NAD+ to turn food into energy. Many people make less of it as they age. MUTO gives your body what it needs to make it. It also has B vitamins that help reduce tiredness.</p>"
             "<p>Take 2 capsules with breakfast. Try it for 90 days. Not for you? Get your money back.</p>"),
    "plans_banner": "Free gifts worth £249 with your first order",
    "plans_label": "Pick a plan",
    "kit_title": "Free gifts in your first box",
    "gifts_label": "More free gifts later",
    "onetime_label": "Just want one jar? Buy once – [price]",
    "cta_label": "Add to cart",
    "who_title": "Who takes it",
})
setb("buy", "b1", text="Energy that lasts all day")
setb("buy", "b2", text="Bounce back after exercise")
setb("buy", "b3", text="Stay strong as you get older")
setb("buy", "b4", text="90 days to try it, or your money back")
setb("buy", "t1", text="Money back for 90 days")
setb("buy", "t2", text="Stop any time")
setb("buy", "t3", text="Checked by an outside lab")
setb("buy", "term_1", text="90 days to try it, or your money back")
setb("buy", "term_2", text="Free next-day delivery")
setb("buy", "term_3", text="Free gifts in your first box: socks, a jar and a guide")
setb("buy", "term_4", text="A small gift in each box, up to month 6")
setb("buy", "term_5", text='A chance to win an Oura Ring (<a href="/pages/better-baseline-giveaway">rules</a>)')
setb("buy", "term_6", text="Pause or stop online. We email you before we charge you.")
setb("buy", "p1", name="1 month", note="You pay £60 every 4 weeks.")
if "plan_RAXANa" in S["buy"]["blocks"]:
    setb("buy", "plan_RAXANa", name="3 months", note="You pay £135 every 3 months.")
setb("buy", "k1", name="Socks")
setb("buy", "k2", name="Jar to keep")
setb("buy", "k3", name="12-week guide")
setb("buy", "k4", name="Chance to win")
setb("buy", "mg2", label="Box 2")
setb("buy", "mg3", label="Box 3")
setb("buy", "mg4a", label="Box 4")
setb("buy", "mg4b", label="Box 4")
setb("buy", "mg6a", label="Box 6")
setb("buy", "mg6b", label="Box 6", text="Chat with an expert")
setb("buy", "a1", title="What’s inside", text=(
    "<p>19 ingredients in 2 capsules. Every amount is on the label, so you can check it.</p>"
    "<p><strong>NR (300mg).</strong> The main one. A form of vitamin B3 that your body uses to make NAD+. 300mg is the most allowed in the UK.</p>"
    "<p><strong>8 B vitamins, in their active form.</strong> Your body can use them straight away. They help reduce tiredness and help your body get energy from food.</p>"
    "<p><strong>Vitamin D3 and K2.</strong> Vitamin D helps keep your muscles and bones working normally. K2 works alongside it.</p>"
    "<p><strong>Zinc and copper.</strong> They help protect your cells.</p>"
    "<p><strong>CoQ10 and PQQ.</strong> Found in every cell. Your body makes less CoQ10 as you get older.</p>"
    "<p><strong>Grape seed, resveratrol and BioPerine® (black pepper extract).</strong> Plant extracts. BioPerine helps your body take in the rest.</p>"
    "<p>No caffeine. No fillers. Vegan.</p>"))
setb("buy", "a2", title="Is it safe?", text=(
    "<p>Made in the UK. An outside lab checks every batch.</p>"
    "<p>Take medicine? Ask your doctor first.</p>"))
setb("buy", "a3", title="How to take it", text="<p>Take 2 capsules with breakfast. Every day. That’s it.</p>")
setb("buy", "a4", title="Delivery and stopping", text=(
    "<p>Free next-day delivery in the UK. A new box comes every 4 weeks.</p>"
    "<p>Skip, pause or stop online. No phone calls.</p>"))
setb("buy", "a5", title="Money-back promise", text=(
    "<p>Take it every day for 90 days. Not for you? Email us. We’ll give your money back, minus delivery.</p>"))
# "Who takes it" athlete card out; a plain "Who it's for" dropdown first in the accordions instead
keep_blocks("buy", "athlete", set())
S["buy"]["blocks"]["a0"] = {"type": "fold", "settings": {"title": "Who it’s for", "text": (
    "<p><strong>Made for adults over 40.</strong> Most of our customers are in their 40s and 50s.</p>"
    "<p><strong>It’s for you if:</strong> you still work, exercise or look after a family, and you’re not ready to slow down. "
    "You feel more tired in the afternoon than you used to. Exercise takes longer to get over. "
    "Or you take lots of supplements and don’t know which ones work.</p>"
    "<p><strong>You don’t need</strong> to be sporty, or own a smartwatch. Walkers, gardeners and gym-goers all take it.</p>"
    "<p><strong>It’s not for</strong> anyone under 18, or if you’re pregnant or breastfeeding. Take medicine? Ask your doctor first.</p>")}}
_o = S["buy"]["block_order"]
_o.insert(_o.index("a1"), "a0")
# Fewer, shorter review quotes (verbatim)
keep_blocks("buy", "snippet", {"snippet_1", "snippet_2", "snippet_3", "snippet_7"})

# --- The problem ---------------------------------------------------------------------
S["problem"]["settings"].update({
    "heading": "Getting older\nfeels harder.",
    "lede": "You run out of steam in the afternoon. Exercise takes longer to get over. "
            "You take lots of pills and don’t know which ones work.",
})
setb("problem", "c1", quote="“I’m tired all the time.”", text="Even after a good night’s sleep.")
setb("problem", "c2", quote="“Exercise wipes me out.”", text="It takes days to feel normal again.")
setb("problem", "c3", quote="“Too many pills.”", text="And no idea which ones work.")
setb("problem", "c4", quote="“Just trust us.”", text="Most brands don’t show you what’s inside.")

# --- Why MUTO --------------------------------------------------------------------------
setb("why", "w1", title="Made by a scientist.",
     text="Dr Richie Barclay made MUTO. He’s a scientist. Got a question? Email him.")
setb("why", "w2", title="Nothing hidden.", text="Every amount is on the label. Made in the UK.")
setb("why", "w3", title="Try it for 90 days.", text="See how you feel. Not for you? Get your money back.")

# Short copy: drop the cards' minimum height to the theme's lowest (380px) so the photo sits under the text
S["why"]["settings"]["card_min"] = 380
S["twocaps"]["settings"]["card_min"] = 380

# --- Board / results ------------------------------------------------------------------
S["board"]["settings"].update({"heading": "Our experts.", "note": "Scientists and doctors who check our work."})
S["results"]["settings"].update({
    "heading": "Real people.\nReal stories.",
    "note": "In their own words",
    "foot": "Everyone is different. We can’t promise results.",
})

# --- Benefits ---------------------------------------------------------------------------
S["benefits"]["settings"]["eyebrow"] = "What you may notice"
setb("benefits", "pf", label="What people notice", heading="What people\nnotice first",
     lede="Real customers, in their own words. Everyone is different.", cta_label=TRY)
setb("benefits", "f1", title="More energy in the afternoon",
     text="<p>Your body needs NAD+ to turn food into energy. MUTO gives your body what it needs to make it. It’s not a quick buzz like coffee.</p>")
setb("benefits", "f2", title="Bounce back after exercise",
     text="<p>Many people say they feel ready for the next walk, swim or workout sooner.</p>")
setb("benefits", "f3", title="Easier mornings",
     text="<p>Some people say mornings feel easier. You don’t need a gadget to notice.</p>")
setb("benefits", "f4", title="Steadier days",
     text="<p>People say their days feel more even, with fewer slumps.</p>")
setb("benefits", "pt", label="Is it working?", heading="Is it working?\nHere’s how to tell.",
     lede="Pick one. Check again at day 30 and day 90.", cta_label=TRY)
setb("benefits", "ck1", title="Write down how you feel", sub="Once a week. 30 seconds.",
     text="<p>Score your energy, sleep and mood out of 10.</p>")
setb("benefits", "ck2", title="Notice your exercise", sub="How fast you bounce back",
     text="<p>Do you feel ready again sooner after a walk, a swim or the gym?</p>")
setb("benefits", "ck3", title="Check your watch or ring", sub="Only if you have one",
     text="<p>Look at the monthly average, not one night.</p>")

# --- Ingredients -------------------------------------------------------------------------
S["ingredients"]["settings"].update({
    "heading": "19 good things.\nAll on the label.",
    "lede": "Everything is listed. Nothing is hidden.\n"
            "Already take vitamin D, B vitamins or zinc? They’re in here too.",
})
for bid, text in {
    "i1": "A form of vitamin B3. Your body uses it to make NAD+.",
    "i2": "Works alongside NR.",
    "i3": "The sunshine vitamin. Many people in the UK are low in winter.",
    "i4": "Works with vitamin D.",
    "i5": "8 B vitamins. They help reduce tiredness.",
    "i13": "Helps protect your cells.",
    "i14": "Keeps zinc in balance.",
    "i15": "Comes from grape seeds.",
    "i16": "Found in red grapes.",
    "i17": "Your body makes less of it as you get older.",
    "i18": "Found in foods like kiwi and spinach.",
    "i19": "From black pepper. Helps your body take in the rest.",
}.items():
    setb("ingredients", bid, text=text)
setb("ingredients", "i2", name="TMG")
setb("ingredients", "i5", name="B vitamins")
setb("ingredients", "i13", name="Zinc")
setb("ingredients", "i14", name="Copper")

# --- 90-day test ---------------------------------------------------------------------------
S["steps"]["settings"].update({"heading": "Not a quick fix.", "heading_right": "Give it 90 days."})
setb("steps", "s1", chip="Day 1", title="Write down how you feel.", text="Score your energy and sleep out of 10.")
setb("steps", "s2", chip="Weeks 1–4", title="Take it every day.", text="Keep the rest of your life the same.")
setb("steps", "s3", chip="Day 30", title="Check in.", text="How do you feel now?")
setb("steps", "s4", chip="Day 90", title="You decide.", text="Not for you? Get your money back.")

# --- Compare -------------------------------------------------------------------------------
S["compare"]["settings"].update({
    "heading": "One jar instead\nof lots of pills.",
    "table_caption": "How MUTO compares",
    "col_2": "Healthy habits only",
    "col_3": "Lots of pills",
    "col_4": "Drips and clinics",
})
for bid, claim in {
    "r1": "Works inside your body, every day",
    "r2": "Every amount on the label",
    "r3": "Just 2 capsules a day",
    "r4": "Costs less than a coffee a day",
    "r5": "Help to see if it’s working",
    "r6": "Money back if it’s not for you",
    "r7": "Instant buzz",
}.items():
    setb("compare", bid, claim=claim)

# --- Two capsules -------------------------------------------------------------------------
S["twocaps"]["settings"].update({"heading": "Two capsules.\nWith breakfast.", "heading_right": "Every day."})
setb("twocaps", "o1", title="Take 2 with breakfast", text="Food helps your body take them in.")
setb("twocaps", "o2", title="Make it a habit", text="Keep the jar by the kettle. Then you won’t forget.")
setb("twocaps", "o3", title="Check how you feel", text="Look back at day 30 and day 90.")

# --- Guarantee -----------------------------------------------------------------------------
S["guarantee"]["settings"].update({
    "heading": "Try it.\nNo risk.",
    "aside": "Not for you? Get your money back.",
    "unit": "days to try it",
    "text": "<p>Take it every day for 90 days. Not for you? Email us. We’ll give your money back, minus delivery. You can stop any time.</p>",
})
setb("guarantee", "c1", text="90 days to try")
setb("guarantee", "c2", text="Free delivery")
setb("guarantee", "c3", text="Stop any time")

# --- FAQs ----------------------------------------------------------------------------------
faqs = {
    "q1": ("How do I know it’s working?",
           "<p>Before you start, score your energy and sleep out of 10. Do it again at day 30 and day 90. Then compare.</p>"),
    "q6": ("Do I need a smartwatch?", "<p>No. A pen and paper is fine.</p>"),
    "q2": ("When will I notice something?",
           "<p>Give it 60 to 90 days. Some people notice a change in a few weeks. For others it takes longer.</p>"),
    "q3": ("Is it safe with my other pills?",
           "<p>Usually, yes. Coffee is fine too.</p><p>Take medicine? Ask your doctor first, especially if you take a blood thinner like warfarin.</p>"),
    "q4": ("What if it’s not for me?",
           f"<p>Email {EMAIL} within 14 days after your 90 days end. We’ll give back what you paid, minus delivery.</p>"
           "<p>This is for first-time subscribers who buy at muto.co.</p>"),
    "q5": ("Why not just take one vitamin?",
           "<p>You can. But MUTO puts 19 things in 2 capsules. One jar instead of lots of pots.</p>"),
}
for bid, (title, text) in faqs.items():
    setb("faq", bid, title=title, text=text)

# --- Sticky bar -----------------------------------------------------------------------------
S["sticky"]["settings"].update({"sticky_cta_label": "Add to cart", "sticky_sub": "Pause or stop any time"})

# Gallery follows the product images in Shopify admin
for _sec in d["sections"].values():
    if _sec["type"] == "muto-crea-buy":
        _sec["settings"]["gallery_from_product"] = True

open(out, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("written", out)
