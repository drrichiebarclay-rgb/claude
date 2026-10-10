"""NAD+ science tabs and 'Shop the protocol' NAD+ panel copy, 10 Oct 2026.

Usage: python3 apply_science_shop_oct10.py <template.json> [...]   (edits in place)
"""
import json
import sys

SCIENCE_LEDE = ("What’s happening beneath the surface, and why you feel it in your afternoons, "
                "your recovery and how you age.")
SCIENCE = {
    "What it does": (
        "<p>MUTO NAD+ Cellular Complex supports the 30 trillion cells behind your energy, your recovery and how "
        "you age. It’s built for energy that holds past 3pm, recovery that keeps pace with your training, and the "
        "repair work your cells run overnight. Two capsules, 19 ingredients, and one daily routine instead of a "
        "cupboard of pots.</p>"),
    "How it works": (
        "<p>Your cells run on NAD+. It’s how they turn food into energy, and how they fund the repair work that "
        "keeps you recovering. The harder you train, work and live, the more they use, and supply tends to fall "
        "as you get older.</p>"
        "<p>That’s often where the slowdown starts. Long before you’d call it ageing, you notice it in your "
        "afternoons and in how long sessions take to leave your legs.</p>"
        "<p>MUTO gives your cells the building blocks to make NAD+, plus the nutrients that help them use it: "
        "B vitamins for energy, CoQ10 and PQQ for the mitochondria that produce it, and antioxidants to protect "
        "the cells doing the work.</p>"
        "<p>Not a stimulant. Not a quick hit. A better baseline, built every day.</p>"),
    "Formula": (
        "<p>19 ingredients, every dose on the label. No proprietary blends, no fillers.</p><ul>"
        "<li><strong>NAD+ building blocks:</strong> Nicotinamide Riboside 300mg · TMG 450mg. NR is a form of "
        "vitamin B3 your cells use to make NAD+, and TMG is paired with it to support the methylation your body "
        "uses to process it.</li>"
        "<li><strong>Energy and tiredness:</strong> methylated B vitamins, including methylfolate 400µg, "
        "methylcobalamin 100µg and P5P 5mg. These are the active forms, which contribute to normal "
        "energy-yielding metabolism and the reduction of tiredness and fatigue.</li>"
        "<li><strong>Cell protection, immunity and muscle:</strong> Zinc 15mg · Copper 1mg · Vitamin D3 50µg "
        "(2,000 IU) · Vitamin K2 (MK-7) 100µg. They contribute to the protection of cells from oxidative stress, "
        "normal immune function and normal muscle function.</li>"
        "<li><strong>Mitochondria and plant compounds:</strong> CoQ10 150mg · PQQ 20mg · Grape "
        "seed extract 150mg · Trans-resveratrol 50mg · BioPerine 5mg to help absorption.</li></ul>"
        "<p>Vegan, allergen-free capsules. Made in the UK to GMP standards and third-party tested.</p>"),
    "Who it's for": (
        "<p>People who are still training, still working and not ready to slow down. Most of our customers are "
        "in their 40s and 50s.</p>"
        "<p>If your afternoons fade sooner than they used to, sessions take longer to bounce back from, or "
        "you’re taking five supplements and don’t know which one’s working, MUTO is built for you.</p>"
        "<p>It’s not for anyone chasing a buzz: no caffeine, no stimulants.</p>"),
    "Protocol": (
        "<p>Two capsules with your first meal, every day.</p>"
        "<p>Before you start, note your baseline: how your afternoons, sleep and recovery feel this week, or your "
        "seven-day average if you wear a device. Keep the rest of your routine steady, pick a check-in date, and "
        "judge it over 90 days, not one morning.</p>"
        "<p>Your call. If it’s not for you, you’re covered.</p>"),
}

SHOP_LEDE = "The 19-ingredient daily protocol for people who aren’t ready to slow down."
SHOP_STEPS = [
    "<strong>Built for the slowdown.</strong> Afternoons that fade sooner. Sessions that take longer to leave "
    "your legs. A cupboard of supplements that isn’t fixing it. Beneath the surface, your cells use NAD+ to make "
    "energy and run their repair work, and supply falls as you get older. MUTO supports that system with 19 "
    "ingredients.",
    "<strong>One routine. Nothing hidden.</strong> Two capsules with your first meal. Every dose on the label. "
    "No caffeine, no stimulants, no proprietary blends.",
    "<strong>90 days to decide.</strong> Note how you feel before you start, then check in at day 30 and day 90: "
    "in your days, your training, or on your wearable if you have one. If it’s not for you, you’re covered.",
]

for path in sys.argv[1:]:
    raw = open(path).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    done = []
    for sid, s in d["sections"].items():
        if s["type"] == "muto-home-science" and "NAD+" in s["settings"].get("heading", ""):
            s["settings"]["lede"] = SCIENCE_LEDE
            for b in s["blocks"].values():
                b["settings"]["text"] = SCIENCE[b["settings"]["label"]]
            done.append(sid)
        if s["type"] == "muto-home-shop":
            panel = next(b for b in s["blocks"].values() if b["type"] == "panel" and b["settings"].get("key") == "nad")
            panel["settings"]["lede"] = SHOP_LEDE
            panel["settings"]["actives_label"] = "What’s inside"
            steps = [b for b in s["block_order"] if s["blocks"][b]["type"] == "step"
                     and s["blocks"][b]["settings"].get("panel") == "nad"]
            assert len(steps) == 3, steps
            for bid, text in zip(steps, SHOP_STEPS):
                s["blocks"][bid]["settings"]["text"] = text
            done.append(sid)
    open(path, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(path, done)
