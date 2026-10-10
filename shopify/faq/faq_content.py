"""MUTO FAQ page content: final copy, October 2026 (MUTO_FAQ_Page_Final_Oct26.docx).

Single source of truth for the /pages/faqs page. build.py turns this into the
theme template (visible accordions) and the FAQPage JSON-LD, so the schema
wording always matches the visible answers.

Answers are Shopify richtext HTML: <p>, <ul>, <ol>, <li>, <a>, <strong>, <em> only.
"""

PRODUCT_URL = "/products/muto-nad-cellular-complex"
SCIENCE_URL = "/pages/science"
SHIPPING_URL = "/pages/shipping-and-return"
COMPETITION_TERMS_URL = "/pages/better-baseline-giveaway"
EMAIL = "hello@mutolongevity.com"
MAILTO = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

# The doc has "[publish date]" here. Set this to the day the page goes live.
LAST_UPDATED = "10 October 2026"

INGREDIENTS = [
    # (ingredient, form, per 2 capsules, % NRV)
    ("Vitamin D3", "Cholecalciferol, from algae", "50µg (2,000 IU)", "1000%"),
    ("Vitamin K2", "Menaquinone-7 (MK-7)", "100µg", "133%"),
    ("Vitamin B1", "Thiamine", "5mg", "455%"),
    ("Vitamin B2", "Riboflavin", "5mg", "357%"),
    ("Vitamin B3", "Niacin", "16mg NE", "100%"),
    ("Vitamin B5", "Pantothenic acid", "10mg", "167%"),
    ("Vitamin B6", "Pyridoxal-5'-phosphate", "5mg", "357%"),
    ("Folate", "Methyltetrahydrofolate", "400µg", "200%"),
    ("Vitamin B12", "Methylcobalamin", "100µg", "4000%"),
    ("Biotin", "—", "300µg", "600%"),
    ("Zinc", "Bisglycinate", "15mg", "150%"),
    ("Copper", "Bisglycinate", "1mg", "100%"),
    ("Trimethylglycine (TMG)", "Betaine anhydrous", "450mg", "†"),
    ("Nicotinamide riboside (NR)", "—", "300mg", "†"),
    ("Grape seed extract", "Vitis vinifera L., 120:1, 95% polyphenols (equivalent to 18,000mg grape seed)", "150mg", "†"),
    ("Coenzyme Q10", "Ubiquinone", "150mg", "†"),
    ("Trans-resveratrol", "—", "50mg", "†"),
    ("PQQ", "Pyrroloquinoline quinone", "20mg", "†"),
    ("BioPerine®", "Piper nigrum L., fruit, 95% piperine", "5mg", "†"),
]
INGREDIENTS_FOOTNOTE = "NRV = nutrient reference value. † No reference intake established."


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


# Each category: (anchor id, jump-link label, H2 heading, [(question, answer_html), ...])
CATEGORIES = [
    ("about", "About MUTO", "About MUTO", [
        ("What is MUTO NAD+ Cellular Complex?", p(
            "MUTO NAD+ Cellular Complex is a daily supplement that supports the 30 trillion cells in your body through NAD+ and other nutrients. It’s two capsules with your first meal: 19 ingredients, every dose on the label, made in the UK. And it’s built to be checked. Take a baseline, track the difference in how your days feel or on your wearable, and make your own call, with a 90-day money-back guarantee behind it.")),
        ("Who is MUTO for?", p(
            "MUTO is for people who are still training, still working and not ready to slow down. Most of our customers are in their 40s and 50s. If your afternoons fade sooner than they used to, sessions take longer to bounce back from, or you’re taking several supplements and don’t know which one’s working, MUTO is built for you. Some customers track HRV or recovery on a wearable; many simply notice how their days feel. MUTO is for adults over 18 only.")),
        ("Is MUTO for women too?", p(
            "Yes. Plenty of our customers are women, and many tell us the first thing they notice is their afternoons. The formula is the same for everyone. If you take any medication, check with your GP or pharmacist first.")),
        ("How is MUTO different from other NAD+ supplements?", p(
            f'MUTO is built to be checked, not taken on trust. Most supplements ask you to believe they’re working. We give you a way to find out: every dose declared, a baseline to start from, help reading your own data, and a 90-day guarantee if you don’t see a difference. It’s also a complete daily formula rather than a single ingredient, with nicotinamide riboside (NR) alongside CoQ10, TMG, resveratrol, PQQ, methylated B vitamins, zinc, copper, D3 and K2. <a href="{SCIENCE_URL}">Read the science behind the formula.</a>')),
        ("Is NAD+ just hype?", p(
            "There’s a lot of hype around NAD+, which is exactly why we built MUTO to be checked. The science is real: NAD+ is essential to how every cell makes energy, and 300mg of NR a day has been shown to raise blood NAD+ in human studies. What no one can promise is how any supplement will make you feel. So we don’t ask you to believe it. Note your starting point, give it 90 days, and decide for yourself.")),
        ("Can I check your claims?", p(
            "Please do. Every ingredient and dose is on the label and on this page. Paste it into ChatGPT, or show it to your GP, pharmacist or nutritionist. Batch certificates are available on request, and Richie answers formula questions himself.")),
        ("Who makes MUTO?", p(
            f"MUTO was founded by Dr Richie Barclay, a PhD scientist in cellular biology and nutrition (not a medical doctor), and is formulated with a six-member Scientific Advisory Board. It’s manufactured in the UK to GMP standards in an ISO-certified facility. You can ask us anything about the formula: {MAILTO}.")),
        ("Is MUTO being clinically studied?", p(
            "Yes. MUTO is part of independent university research programmes, starting with a University of Westminster study in December 2026, followed by work with King’s College London in early 2027 and Coventry and Newcastle universities later in 2027. These studies are underway or starting, so there are no results to report yet. We’ll publish them, whatever they show.")),
        ("How do you pronounce MUTO?", p(
            "MUTO is pronounced “MEW-toe”. It’s Latin for “transform”.")),
    ]),
    ("what-to-expect", "What to expect", "What to expect", [
        ("How long does MUTO take to work?", p(
            "Give MUTO 60 to 90 days, taken daily, before you judge it. Some customers say they notice a difference in their energy or recovery within the first few weeks; others notice nothing early on. If you track on a wearable, read it as 30-day averages, not single nights. That’s why our guarantee runs for 90 days.")),
        ("Will MUTO give me an energy boost?", p(
            "No, not the kind you feel within an hour. Caffeine and energy drinks borrow energy and it resets every morning. MUTO supplies nutrients your body uses to make energy, including vitamins B6, B12 and folate, which contribute to the reduction of tiredness and fatigue.")),
        ("How do I track whether MUTO is working?", p(
            "Note your starting point before your first dose, give it 90 days, then compare. There are two ways to do it.",
            "<strong>Without a wearable:</strong> once a week, rate your energy, sleep, afternoons and mood out of 10. It takes 30 seconds, and writing it down turns a feeling into a record you can look back on.",
            "<strong>With a wearable:</strong> note your 7-day averages for HRV, resting heart rate and recovery, then compare 30-day averages, not single nights.",
            "Either way, keep the rest of your routine steady and check in on days 30, 60 and 90. Then it’s your call. If you don’t see a difference, you’re covered.")),
        ("Do I need a wearable?", p(
            "No. A wearable makes tracking easier, but a 30-second weekly check-in (energy, sleep, afternoons and mood, each out of 10) works too. Felt changes are easy to forget, so writing them down is what turns a feeling into a record you can look back on.")),
        ("What if I don’t notice a difference?", p(
            "Then you’re covered. Email us and we’ll help you check consistency, timing and anything else that might be masking a change. If you still don’t see a difference by day 90, we’ll refund you under the 90-day guarantee.")),
        ("Will MUTO improve my HRV?", p(
            "We don’t promise what any number will do. Bodies vary, and HRV is affected by sleep, stress, training and illness. What we offer is a fair way to find out for yourself: baseline it, track the trend for 90 days, and if you don’t see a difference, we’ll refund you.")),
        ("Which wearables work best for tracking?", p(
            "Any device that records HRV and resting heart rate overnight works. Garmin, WHOOP and Oura measure through the night, which gives steadier averages. Apple Watch takes fewer HRV readings, so wear it overnight with sleep tracking on and judge it on longer averages.")),
    ]),
    ("guarantee", "90-day guarantee", "The 90-day money-back guarantee", [
        ("What is the 90-day money-back guarantee?", p(
            "If you subscribe, take MUTO daily and don’t see a difference within 90 days, we’ll refund every subscription payment you’ve made in that time, less our delivery costs. We won’t ask you to take MUTO on trust, so we don’t ask you to risk your money on it either.")),
        ("Who is covered?", p(
            "The guarantee covers first-time MUTO subscribers buying at muto.co, one claim per customer. One-time purchases aren’t covered, and neither are orders through Amazon or other retailers. Contact them directly.")),
        ("How do I claim?", p(
            f"Email {MAILTO} with your name, order number and a line on your experience, within 104 days of your first order. That’s your full 90 days, plus 14 days to decide. We’ll refund your original payment method within 7 working days of your request. Sharing your wearable data helps us learn but is optional.")),
        ("Do I need to send my wearable data?", p(
            "No. Your verdict is yours. If you’d like help reading your data before deciding, send it over and we’ll go through it with you.")),
    ]),
    ("orders", "Orders", "Orders and subscriptions", [
        ("How much does MUTO cost?", p(
            "MUTO is £60 a month on a monthly subscription, £150 every three months on the three-month plan (about £1.67 a day), or £70 as a one-time purchase. Every subscription includes free UK next-day delivery and the 90-day money-back guarantee.")),
        ("Why does MUTO cost more than an NR supplement on its own?", p(
            "A single NR product covers one input. MUTO includes NR at the maximum dose authorised in Great Britain (300mg), plus a methylated B complex, D3, K2, zinc, copper, CoQ10 (as ubiquinone), PQQ, resveratrol and TMG. Many people already buy these separately. On the three-month plan it’s about £1.67 a day. Compare it with what’s in your cupboard, and remember you have 90 days to decide.")),
        ("Which plan should I choose?", p(
            f'Choose the three-month plan if you want a proper test: it’s the lowest daily price and lines up with the 90-day window we recommend for judging MUTO. The monthly plan spreads the cost. Both subscriptions are covered by the 90-day guarantee; a one-time purchase isn’t. <a href="{PRODUCT_URL}">Compare plans.</a>')),
        ("What’s in the welcome kit and gifts?", p(
            f'With your first subscription order you get performance socks, a Forever Jar, our 12-week protocol guide and entry into our competition to win an Oura Ring. Subscribers also get a thank-you gift with later orders. Gifts are while stocks last. <a href="{COMPETITION_TERMS_URL}">Competition terms apply.</a>')),
        ("Do subscribers get creatine?", p(
            "Yes. From 14 October 2026, subscribers receive MUTO Ultrapure Micronised Creatine as a gift with later orders. One serving is 5g. Creatine increases physical performance in successive bursts of short-term, high-intensity exercise; the beneficial effect is obtained with a daily intake of 3g.")),
        ("Can I skip, pause or cancel?", p(
            "Yes, anytime, online. Log in to your account to skip a delivery, pause, change your plan or cancel, with no phone call and no fees. We email you a reminder 5 days before every payment.")),
        ("How does delivery work?", p(
            f'UK delivery is free and next-day for orders placed before 9pm, arriving within 1–2 working days. International shipping is calculated at checkout. You’ll get a tracking link by email when your order ships. See <a href="{SHIPPING_URL}">Shipping &amp; Returns</a> for details.')),
        ("Where can I buy MUTO?", p(
            "Buy MUTO direct at muto.co, where subscriptions and the 90-day guarantee apply. It’s also available on Amazon, though Amazon orders aren’t covered by our guarantee.")),
    ]),
    ("ingredients", "Ingredients", "Ingredients and formula", [
        ("What ingredients are in MUTO?", p(
            "MUTO contains 19 ingredients, every one declared at its full dose, with no proprietary blend. Per daily serving of two capsules:")),
        ("Why does MUTO use NR?", p(
            "MUTO uses NR because it’s one of the most studied NAD+ precursors and is authorised for use in food supplements in Great Britain, at up to 300mg a day for adults. MUTO contains exactly 300mg. In a published clinical study, 300mg of NR a day raised blood NAD+ by 51% after 14 days (Conze et al., <em>Scientific Reports</em>, 2019). That study tested NR on its own, not MUTO.")),
        ("What’s the difference between NR and NMN?", p(
            "NR and NMN are both NAD+ precursors: compounds your body converts into NAD+ by slightly different routes. NR is authorised for food supplements in Great Britain; NMN is currently under novel food assessment. MUTO uses NR so every ingredient in the core formula is on the right side of UK rules.")),
        ("Why not just take NR on its own?", p(
            "You can, but NR alone covers one input. MUTO pairs it with nutrients that have authorised roles in how your body makes and uses energy: B vitamins and copper for normal energy-yielding metabolism, and zinc for protecting cells from oxidative stress. It also adds CoQ10, TMG, resveratrol and PQQ. One routine instead of several separate products.")),
        ("Can MUTO replace some of my other supplements?", p(
            "Possibly. MUTO contains full doses of nutrients many people already buy separately: a methylated B complex, zinc, copper, vitamin D3 (2,000 IU), vitamin K2, CoQ10 and an NR product. Compare your current labels against ours before stopping anything, and check with your GP before changing anything you take for a medical reason.")),
        ("Does MUTO contain caffeine or stimulants?", p(
            "No. MUTO contains no caffeine and no stimulants. It isn’t designed to give you a buzz. It supplies nutrients your cells use every day, which is why it works alongside your morning coffee rather than replacing it.")),
        ("Is MUTO vegan?", p(
            "Yes. MUTO is vegan: the capsules are made from HPMC, a plant cellulose, and the vitamin D3 comes from algae. It contains no major allergens and no fillers.")),
    ]),
    ("safety", "Safety", "Safety", [
        ("Is MUTO safe?", p(
            "MUTO is made in the UK to GMP standards and every batch is third-party tested; certificates are available on request. Like any supplement, it isn’t right for everyone. Speak to your GP or pharmacist first if you’re on medication, have a medical condition, or are pregnant or breastfeeding.")),
        ("Are there any side effects?", p(
            "Most people take MUTO without any problems. A few notice mild stomach discomfort in the first days, which taking it with food usually avoids. Stop taking it and contact us if anything feels wrong.")),
        ("Can I take MUTO with medication?", p(
            "Check with your GP or pharmacist first if you take any prescription medicine. In particular, MUTO contains vitamin K2 (100µg), which can affect blood thinners such as warfarin. Resveratrol and grape seed extract may also interact with anticoagulant and antiplatelet medicines. We’re happy to send the full label to share with your doctor.")),
        ("Can I take MUTO if I’m on HRT or hormonal contraception?", p(
            "Talk to your GP or pharmacist before starting. If you take any medication, including HRT or hormonal contraception, please check with your doctor first. We’re happy to send the full label to share with them.")),
        ("Can I take MUTO if I’m pregnant or breastfeeding?", p(
            "No. MUTO isn’t for use during pregnancy or breastfeeding, or for anyone under 18. Nicotinamide riboside is authorised in Great Britain for adults only, excluding pregnant and breastfeeding women.")),
        # Pre-certification version. Swap when Informed Sport certification is live (see the doc).
        ("Is MUTO suitable for drug-tested athletes?", p(
            "MUTO isn’t yet certified by a banned-substance testing programme such as Informed Sport. If you’re tested under WADA or UKAD rules, speak to your sport’s medical team before taking any supplement.")),
        ("Can I take MUTO with other supplements or coffee?", p(
            "Yes, in most cases, and coffee is fine. Watch for doubling up: a separate B complex, zinc, vitamin D, K2 or NAD+ product will overlap with what’s already in MUTO. Check your other labels against ours.")),
    ]),
    ("how-to-take", "How to take", "How to take MUTO", [
        ("How do I take MUTO?", p(
            "Take two capsules once a day with your first meal. Food helps absorb the fat-soluble ingredients (CoQ10, vitamins D3 and K2), and pairing it with breakfast makes it easy to remember. Consistency matters more than exact timing.")),
        ("Do I need to cycle MUTO?", p(
            "No. MUTO contains no stimulants, so there’s nothing to build tolerance to. It’s designed for daily use.")),
        ("What if I miss a day?", p(
            "Just take your normal two capsules the next day. Don’t double up.")),
    ]),
    ("nad-explained", "NAD+ explained", "NAD+ and cellular health explained", [
        ("What is NAD+?", p(
            "NAD+ (nicotinamide adenine dinucleotide) is a coenzyme found in every cell, which cells use to turn food into usable energy and to run maintenance processes such as DNA repair. Your body makes it continuously from precursors like vitamin B3 and nicotinamide riboside, and recycles it as it’s used.")),
        ("Does NAD+ decline with age?", p(
            "Research suggests NAD+ levels in some tissues fall with age, as demand rises and production and recycling slow. The size of the decline varies between people and tissues, and blood levels don’t track it neatly, so treat any single headline figure with caution.")),
        ("What’s the difference between NAD+ and NADH?", p(
            "They’re two forms of the same molecule. When your cells break down food, NAD+ picks up electrons and becomes NADH. NADH then hands them on in your mitochondria to make energy, turning back into NAD+. The balance between the two is part of how your cells manage energy.")),
        ("How do NAD+ supplements work?", p(
            "Most NAD+ supplements provide precursors such as NR, which your body converts into NAD+, rather than NAD+ itself, which is poorly absorbed whole. Oral NR at 300mg a day has been shown to raise blood NAD+ in human studies.")),
        ("Can you raise NAD+ naturally?", p(
            "Regular exercise, enough vitamin B3 in your diet (meat, fish, wholegrains), good sleep and not overdoing alcohol all support how your body makes and recycles NAD+. Precursors like NR are a more direct route. MUTO is designed to sit alongside those habits, not replace them.")),
        ("What are sirtuins?", p(
            "Sirtuins are a family of enzymes involved in cell maintenance, including DNA repair and energy regulation. They need NAD+ to work, which is one reason NAD+ is studied in ageing research.")),
        ("What is HRV?", p(
            "Heart rate variability (HRV) is the variation in time between heartbeats, and a widely used signal of how your nervous system is handling stress and recovery. It’s personal, so never compare yours with someone else’s. It’s also noisy night to night, so the 30-day trend against your own baseline is what’s worth watching.")),
        ("What’s the difference between healthspan and lifespan?", p(
            "Lifespan is how long you live. Healthspan is how long you stay healthy, capable and independent. MUTO is about healthspan: keeping your standard for as long as you can.")),
        ("Does caffeine raise NAD+?", p(
            "Caffeine doesn’t raise NAD+. It blocks adenosine, the chemical signal behind sleepiness, so you feel more alert without changing how your cells make energy. That’s why the effect fades and resets each day.")),
    ]),
]

INTRO = ("Everything worth checking before you start: what’s in it, who it’s for, what to expect, and how the "
         "90-day guarantee works. Don’t take it on trust. Check.")
BYLINE = f"Scientifically reviewed by Dr Richie Barclay, PhD (Cellular Biology &amp; Nutrition) · Last updated {LAST_UPDATED}"

CLOSING_HTML = (
    f"<p><em>Have a question we haven’t answered? Email {MAILTO}. Richie and the team read every message.</em></p>"
    "<p><em>Food supplements should not replace a varied, balanced diet and healthy lifestyle. Do not exceed the recommended daily dose. Not for use by children, or during pregnancy or breastfeeding.</em></p>"
)
