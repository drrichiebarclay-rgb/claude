"""MUTO FAQ page content (October 2026 rewrite).

Single source of truth for the /pages/faqs page. build.py turns this into the
theme template (visible accordions) and the FAQPage JSON-LD, so the schema
wording always matches the visible answers.

Answers are Shopify richtext HTML: <p>, <ul>, <ol>, <li>, <a>, <strong>, <em> only.
"""

PRODUCT_URL = "/products/muto-nad-cellular-complex"
SCIENCE_URL = "/pages/science"
SHIPPING_URL = "/pages/shipping-and-return"
CONTACT_URL = "/pages/contact"
EMAIL = "hello@mutolongevity.com"
MAILTO = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

LAST_UPDATED = "8 October 2026"

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
    ("Coenzyme Q10", "—", "150mg", "†"),
    ("Trans-resveratrol", "—", "50mg", "†"),
    ("PQQ", "Pyrroloquinoline quinone", "20mg", "†"),
    ("BioPerine®", "Piper nigrum L., fruit, 95% piperine", "5mg", "†"),
]
INGREDIENTS_FOOTNOTE = "NRV = nutrient reference value. † No reference intake established."

# Each category: (anchor id, jump-link label, H2 heading, [(question, answer_html), ...])
CATEGORIES = [
    ("about", "About MUTO", "About MUTO", [
        ("What is MUTO NAD+ Cellular Complex?",
         f'<p><a href="{PRODUCT_URL}">MUTO NAD+ Cellular Complex</a> is a daily supplement that supports the 30 trillion cells in your body through NAD+ and other nutrients. It’s two capsules with your first meal: 19 ingredients, every dose on the label, made in the UK. And it’s built to be checked. Take a baseline, track the difference on your wearable or in how your days feel, and make your own call, with a <a href="#guarantee">90-day money-back guarantee</a> behind it.</p>'),
        ("How is MUTO different from other NAD+ supplements?",
         f'<p>MUTO is built to be checked, not taken on trust. Most supplements ask you to believe they’re working. We give you a way to find out: every dose declared, a baseline to start from, help reading your own data, and a <a href="#guarantee">90-day guarantee</a> if you don’t see a difference. It’s also a complete daily formula rather than a single ingredient, with nicotinamide riboside (NR) alongside CoQ10, TMG, resveratrol, PQQ, methylated B vitamins, zinc, copper, D3 and K2. <a href="{SCIENCE_URL}">Read the science behind the formula</a>.</p>'),
        ("Who is MUTO for?",
         "<p>MUTO is for people already doing the work to age well — training, sleeping, eating properly — who want to know it’s paying off. Many of our customers track HRV, recovery or readiness on a WHOOP, Garmin, Oura or Apple Watch. Others don’t track at all and simply notice how their afternoons and mornings feel. MUTO is for adults over 18 only.</p>"),
        ("Who makes MUTO?",
         f"<p>MUTO was founded by Dr Richie Barclay, a PhD scientist in cellular biology and nutrition (not a medical doctor), and is formulated with a seven-member Scientific Advisory Board. It’s manufactured in the UK to GMP standards in an ISO-certified facility. You can ask us anything about the formula: {MAILTO}.</p>"),
        ("Is MUTO being clinically studied?",
         "<p>Yes. MUTO is part of independent university research programmes, starting with a University of Westminster study in December 2026, followed by work with King’s College London in early 2027 and Coventry and Newcastle universities later in 2027. These studies are underway or starting, so there are no results to report yet. We’ll publish them, whatever they show.</p>"),
        ("How do you pronounce MUTO?",
         "<p>MUTO is pronounced “MEW-toe”. It’s Latin for “transform”.</p>"),
    ]),
    ("ingredients", "Ingredients", "Ingredients and formula", [
        ("What ingredients are in MUTO?",
         "<p>MUTO contains 19 ingredients, every one declared at its full dose, with no proprietary blend. Per daily serving of two capsules:</p>"),
        ("Why does MUTO use nicotinamide riboside (NR)?",
         "<p>MUTO uses NR because it’s one of the most studied NAD+ precursors and is authorised for use in food supplements in Great Britain, at up to 300mg a day for adults. MUTO contains exactly 300mg. In a published clinical study, 300mg of NR a day raised blood NAD+ by 51% after 14 days (Conze et al., <em>Scientific Reports</em>, 2019). That study tested NR on its own, not MUTO.</p>"),
        ("What’s the difference between NR and NMN?",
         "<p>NR and NMN are both NAD+ precursors: compounds your body converts into NAD+ by slightly different routes. NR is authorised for food supplements in Great Britain; NMN is currently under novel food assessment. MUTO uses NR so every ingredient in the core formula is on the right side of UK rules.</p>"),
        ("Why not just take NR on its own?",
         "<p>You can, but NR alone covers one input. MUTO pairs it with nutrients that have authorised roles in how your body makes and uses energy — B vitamins and copper for normal energy-yielding metabolism, zinc for protecting cells from oxidative stress — plus CoQ10, TMG, resveratrol and PQQ. One routine instead of several separate products.</p>"),
        ("Can MUTO replace some of my other supplements?",
         "<p>Possibly. MUTO contains full doses of nutrients many people already buy separately: a methylated B complex, zinc, copper, vitamin D3 (2,000 IU), vitamin K2, CoQ10 and an NR product. Compare your current labels against ours before stopping anything, and check with your GP before changing anything you take for a medical reason.</p>"),
        ("Does MUTO contain caffeine or stimulants?",
         "<p>No. MUTO contains no caffeine and no stimulants. It isn’t designed to give you a buzz. It supplies nutrients your cells use every day, which is why it works alongside your morning coffee rather than replacing it.</p>"),
        ("Is MUTO vegan?",
         "<p>Yes. MUTO is vegan: the capsules are made from HPMC, a plant cellulose, and the vitamin D3 comes from algae. It contains no major allergens and no fillers.</p>"),
    ]),
    ("results", "Results & tracking", "Results and tracking", [
        ("How long does MUTO take to work?",
         '<p>Give MUTO 60 to 90 days, taken daily, before you judge it. Some customers say they notice a difference in their energy or recovery within the first few weeks; others notice nothing early on. Wearable data is best read as 30-day averages, not single nights. That’s why our <a href="#guarantee">guarantee</a> runs for 90 days.</p>'),
        ("How do I track whether MUTO is working?",
         "<p>Take a baseline before your first dose, track a few measures for 60–90 days, then compare. Step by step:</p>"
         "<ol>"
         "<li><strong>Baseline.</strong> Note your 7-day averages for HRV, resting heart rate and recovery or readiness. No wearable? Rate your energy, sleep and afternoons out of 10.</li>"
         "<li><strong>Keep everything else steady.</strong> Same training, sleep and other supplements, so the difference is easier to read.</li>"
         "<li><strong>Track the basket, not one number.</strong> HRV moves with travel, alcohol, illness and training load, so look at several measures together.</li>"
         "<li><strong>Check in on days 30, 60 and 90.</strong> Compare 30-day averages with your baseline.</li>"
         "<li><strong>Your call.</strong> If you don’t see a difference, the 90-day guarantee covers you.</li>"
         "</ol>"),
        ("Will MUTO improve my HRV?",
         "<p>We don’t promise what any number will do — bodies vary, and HRV is affected by sleep, stress, training and illness. What we offer is a fair way to find out for yourself: baseline it, track the trend for 90 days, and if you don’t see a difference, we’ll refund you.</p>"),
        ("Do I need a wearable to take MUTO?",
         "<p>No. A wearable makes tracking easier, but a 30-second weekly check-in — energy, sleep, afternoons, mood, each out of 10 — works too. Felt changes are easy to forget, so writing them down is what turns a feeling into a record you can look back on.</p>"),
        ("Which wearables work best for tracking?",
         "<p>Any device that records HRV and resting heart rate overnight works. Garmin, WHOOP and Oura measure through the night, which gives steadier averages. Apple Watch takes fewer HRV readings, so wear it overnight with sleep tracking on and judge it on longer averages.</p>"),
        ("What if I don’t notice a difference?",
         '<p>Then you’re covered. Around day 45 we’ll send a short guide to reading your data and offer a call to check consistency, timing and anything else that might be masking a change. If you still don’t see a difference by day 90, email us and we’ll refund you under the <a href="#guarantee">90-day guarantee</a>.</p>'),
        ("Will MUTO give me an energy boost?",
         "<p>No, not the kind you feel within an hour. Caffeine and energy drinks borrow energy and it resets every morning. MUTO supplies nutrients your body uses to make energy, including vitamins B6, B12 and folate, which contribute to the reduction of tiredness and fatigue.</p>"),
    ]),
    ("guarantee", "90-day guarantee", "The 90-day money-back guarantee", [
        ("What is MUTO’s 90-day money-back guarantee?",
         "<p>If you subscribe, take MUTO daily and don’t see a difference within 90 days, we’ll refund every subscription payment you’ve made in that time, less our delivery costs. We won’t ask you to take MUTO on trust, so we don’t ask you to risk your money on it either.</p>"),
        ("How do I claim the guarantee?",
         f"<p>Email {MAILTO} within 90 days of your first order with your name, order number and a line on your experience. We’ll refund your original payment method within 7 working days of your request. Sharing your wearable data helps us learn but is optional.</p>"),
        ("Who is covered by the guarantee?",
         "<p>The guarantee covers first-time MUTO subscribers buying at muto.co, one claim per customer. One-time purchases aren’t covered, and neither are orders through Amazon or other retailers — contact them directly.</p>"),
        ("Do I need to send my wearable data to get a refund?",
         "<p>No. Your verdict is yours. If you’d like help reading your data before deciding, send it over and we’ll go through it with you.</p>"),
    ]),
    ("safety", "Safety", "Safety", [
        ("Is MUTO safe?",
         "<p>MUTO is made in the UK to GMP standards and every batch is third-party tested; certificates are available on request. Like any supplement, it isn’t right for everyone. Speak to your GP or pharmacist first if you’re on medication, have a medical condition, or are pregnant or breastfeeding.</p>"),
        ("Does MUTO have side effects?",
         f'<p>Most people take MUTO without any problems. A few notice mild stomach discomfort in the first days, which taking it with food usually avoids. Stop taking it and <a href="{CONTACT_URL}">contact us</a> if anything feels wrong.</p>'),
        ("Can I take MUTO with medication?",
         "<p>Check with your GP or pharmacist first if you take any prescription medicine. In particular, MUTO contains vitamin K2 (100µg), which can affect blood thinners such as warfarin. Resveratrol and grape seed extract may also interact with anticoagulant and antiplatelet medicines. We’re happy to send the full label to share with your doctor.</p>"),
        ("Can I take MUTO if I’m on HRT or hormonal contraception?",
         "<p>Talk to your GP or pharmacist before starting. If you take any medication, including HRT or hormonal contraception, please check with your doctor first. We’re happy to send the full label to share with them.</p>"),
        ("Can I take MUTO if I’m pregnant or breastfeeding?",
         "<p>No. MUTO isn’t for use during pregnancy or breastfeeding, or for anyone under 18. Nicotinamide riboside is authorised in Great Britain for adults only, excluding pregnant and breastfeeding women.</p>"),
        ("Is MUTO suitable for drug-tested athletes?",
         "<p>MUTO isn’t yet certified by a banned-substance testing programme such as Informed Sport. If you’re tested under WADA or UKAD rules, speak to your sport’s medical team before taking any supplement.</p>"),
        ("Can I take MUTO with other supplements or coffee?",
         "<p>Yes, in most cases, and coffee is fine. Watch for doubling up: a separate B complex, zinc, vitamin D, K2 or NAD+ product will overlap with what’s already in MUTO. Check your other labels against ours.</p>"),
    ]),
    ("how-to-take", "How to take", "How to take MUTO", [
        ("How do I take MUTO?",
         "<p>Take two capsules once a day with your first meal. Food helps absorb the fat-soluble ingredients (CoQ10, vitamins D3 and K2), and pairing it with breakfast makes it easy to remember. Consistency matters more than exact timing.</p>"),
        ("Do I need to cycle MUTO?",
         "<p>No. MUTO contains no stimulants, so there’s nothing to build tolerance to. It’s designed for daily use.</p>"),
        ("What if I miss a day?",
         "<p>Just take your normal two capsules the next day. Don’t double up.</p>"),
    ]),
    ("orders", "Orders", "Orders and subscriptions", [
        ("How much does MUTO cost?",
         '<p>MUTO is £60 a month on a monthly subscription, £150 every three months on the three-month plan (about £1.67 a day), or £70 as a one-time purchase. Every subscription includes free UK next-day delivery and the <a href="#guarantee">90-day money-back guarantee</a>.</p>'),
        ("Which plan should I choose?",
         f'<p>Choose the three-month plan if you want a proper test: it’s the lowest daily price and lines up with the 90-day window we recommend for judging MUTO. The monthly plan spreads the cost. Both subscriptions are covered by the 90-day guarantee; a one-time purchase isn’t. <a href="{PRODUCT_URL}">Compare plans</a>.</p>'),
        ("Can I skip, pause or cancel my subscription?",
         "<p>Yes, anytime, online. Log in to your account to skip a delivery, pause, change your plan or cancel, with no phone call and no fees. We email you a reminder 5 days before every payment.</p>"),
        ("How fast is delivery?",
         f'<p>UK delivery is free and next-day for orders placed before 9pm, arriving within 1–2 working days. International shipping is calculated at checkout. You’ll get a tracking link by email when your order ships. See <a href="{SHIPPING_URL}">Shipping &amp; Returns</a> for details.</p>'),
        ("Where can I buy MUTO?",
         f'<p>Buy MUTO direct at <a href="{PRODUCT_URL}">muto.co</a>, where subscriptions and the 90-day guarantee apply. It’s also available on Amazon, though Amazon orders aren’t covered by our guarantee.</p>'),
        ("Do I get MUTO Creatine with my order?",
         "<p>From 14 October 2026, three-month subscribers receive MUTO Ultrapure Micronised Creatine with their first two orders, and monthly subscribers with their third order. One serving is 5g. Creatine increases physical performance in successive bursts of short-term, high-intensity exercise; the beneficial effect is obtained with a daily intake of 3g.</p>"),
    ]),
    ("nad-explained", "NAD+ explained", "NAD+ and cellular health explained", [
        ("What is NAD+?",
         "<p>NAD+ (nicotinamide adenine dinucleotide) is a coenzyme found in every cell, which cells use to turn food into usable energy and to run maintenance processes such as DNA repair. Your body makes it continuously from precursors like vitamin B3 and nicotinamide riboside, and recycles it as it’s used.</p>"),
        ("Does NAD+ decline with age?",
         "<p>Research suggests NAD+ levels in some tissues fall with age, as demand rises and production and recycling slow. The size of the decline varies between people and tissues, and blood levels don’t track it neatly, so treat any single headline figure with caution.</p>"),
        ("What’s the difference between NAD+ and NADH?",
         "<p>They’re two forms of the same molecule. NAD+ accepts electrons during energy production and becomes NADH; NADH hands them on and becomes NAD+ again. Cells cycle between the two constantly.</p>"),
        ("How do NAD+ supplements work?",
         "<p>Most NAD+ supplements provide precursors such as NR, which your body converts into NAD+, rather than NAD+ itself, which is poorly absorbed whole. Oral NR at 300mg a day has been shown to raise blood NAD+ in human studies.</p>"),
        ("Can you raise NAD+ naturally?",
         "<p>Exercise, regular sleep and a diet with enough vitamin B3 — from foods such as fish, poultry, mushrooms and whole grains — all support the body’s own NAD+ production. A supplement adds precursors on top of that foundation; it doesn’t replace it.</p>"),
        ("What are sirtuins?",
         "<p>Sirtuins are a family of enzymes involved in cell maintenance, including DNA repair and energy regulation. They need NAD+ to work, which is one reason NAD+ is studied in ageing research.</p>"),
        ("What is HRV and why does it matter?",
         "<p>Heart rate variability (HRV) is the variation in time between heartbeats, and a widely used signal of how your nervous system is handling stress and recovery. It’s personal — never compare yours with someone else’s — and noisy night to night, so the 30-day trend against your own baseline is what’s worth watching.</p>"),
        ("What’s the difference between healthspan and lifespan?",
         "<p>Lifespan is how long you live; healthspan is how long you live well, with the energy, strength and capacity to do what you care about. Our aim at MUTO is simple: live better for longer.</p>"),
        ("Does caffeine affect NAD+?",
         "<p>Caffeine doesn’t raise NAD+. It blocks adenosine, the chemical signal behind sleepiness, so you feel more alert without changing how your cells make energy. That’s why the effect fades and resets each day.</p>"),
    ]),
]

INTRO = "Everything worth checking before you start: what’s in it, how to track it, and how the 90-day guarantee works. Don’t take it on trust. Check."
BYLINE = f"Scientifically reviewed by Dr Richie Barclay, PhD (Cellular Biology &amp; Nutrition) · Last updated {LAST_UPDATED}"

CLOSING_HTML = (
    f"<p><em>Have a question we haven’t answered? Email {MAILTO} — Richie and the team read every message.</em></p>"
    "<p><em>Food supplements should not replace a varied, balanced diet and healthy lifestyle. Do not exceed the recommended daily dose. Not for use by children, or during pregnancy or breastfeeding.</em></p>"
)
