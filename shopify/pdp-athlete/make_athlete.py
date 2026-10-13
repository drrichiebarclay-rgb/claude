"""Build the athlete PDP (product.muto-nad-athlete.json) from the draft creatine-kit page.

Same offer, plans, gifts, images, CTAs and comparison table; copy rewritten for a
30-35-year-old athlete who tracks HRV, resting heart rate, sleep and recovery.
Claims: authorised claims only; wearable metrics are things to *track*, never effects.

Usage: python3 make_athlete.py [base] [out]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import compare_table  # noqa: E402

base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "../pdp-creatine-kit/product.muto-nad-creatine-kit.json")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "product.muto-nad-athlete.json")

raw = open(base).read()
header = re.match(r"^/\*.*?\*/\s*", raw, flags=re.S)
d = json.loads(raw[header.end():] if header else raw)
S = d["sections"]


def s(sec, **kw):
    S[sec]["settings"].update(kw)


def b(sec, blk, **kw):
    S[sec]["blocks"][blk]["settings"].update(kw)


# ---- Buy box ---------------------------------------------------------------
s("buy", text="<p>For people who train hard and read their data. Two capsules a day built around 300mg NR, the NAD+ building block, plus 18 nutrients, including B vitamins that contribute to normal energy-yielding metabolism and vitamin D for normal muscle function. Every dose on the label. Take a baseline on your wearable, run the 90 days, and judge it on your own numbers.</p>")
b("buy", "b1", text="Built around NR 300mg, the dose the research uses")
b("buy", "b2", text="B vitamins for normal energy-yielding metabolism")
b("buy", "b3", text="Vitamin D for normal muscle function")
b("buy", "b4", text="Track it on your wearable for 90 days, or your money back")
b("buy", "a3", text="<p>Two capsules together each morning with your first meal. Fat helps the fat-soluble ingredients absorb, so whatever you already eat first is the right time. Before or after training doesn’t matter; taking it every day does. No cycling, no loading and no rest days.</p>")
b("buy", "a5", text="<p>Take a 7-day baseline, give it ninety days and compare: HRV, resting heart rate, sleep, recovery score or simply how you feel. If you don’t see a difference, you get your money back in full.</p>")
# Athlete testimonials first (quotes unchanged, just reordered)
order = S["buy"]["block_order"]
snips = [k for k in order if k.startswith("snippet_")]
first = ["snippet_4", "snippet_9", "snippet_3", "snippet_6", "snippet_7", "snippet_1"]
new_snips = first + [k for k in snips if k not in first]
it = iter(new_snips)
S["buy"]["block_order"] = [next(it) if k.startswith("snippet_") else k for k in order]

# ---- Problem ---------------------------------------------------------------
s("problem",
  heading="Your training is\nprecise.\nYour stack isn’t.",
  lede="You’ve dialled in sessions, sleep and fuelling, and you track all of it. Then there’s the supplement shelf: five products, unclear doses, and no way to tell which one is doing anything. MUTO is one protocol you can test against your own data.")
b("problem", "c1", quote="“The numbers say I’m recovered. My legs disagree.”",
  text="Readiness scores and felt recovery don’t always line up. You want both.")
b("problem", "c2", quote="“The second session of the week is the hard one.”",
  text="Back-to-back training days are where recovery gets tested.")
b("problem", "c3", quote="“A shelf full of pills.”",
  text="Five products, overlapping doses, no idea which one is pulling its weight.")
b("problem", "c4", quote="“Just trust us.”",
  text="Proprietary blends and big promises, with nothing you can measure.")

# ---- Why MUTO --------------------------------------------------------------
b("why", "w1", text="Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by a board that includes an international rugby performance nutritionist and a sleep doctor. Got a question? Ask him.")
b("why", "w2", text="Nineteen ingredients, each on the label with its dose and why it’s there. No proprietary blends. Made in the UK to GMP standards and third-party tested batch by batch.")
b("why", "w3", title="Built to be measured.",
  text="Take a 7-day baseline of HRV, resting heart rate, sleep and recovery, then compare 30-day averages at day 30 and day 90. Your data, your verdict, with a 90-day guarantee behind it.")

# ---- Board -----------------------------------------------------------------
s("board", note="Our Scientific Advisory Board: performance, sleep, metabolism and longevity, from international rugby to clinical practice.")

# ---- Benefits: feel + track ------------------------------------------------
b("benefits", "pf", label="What you’ll feel", heading="What athletes\nnotice first",
  lede="What customers who train tell us they notice first. Individual experiences, not a promise. Open any of them for more.")
b("benefits", "f1", title="Energy that holds",
  sub="“Energy is up and staying consistent” – Jack",
  text="<p>NAD+ sits at the centre of how your cells turn food into usable energy. Alongside it, B vitamins contribute to normal energy-yielding metabolism and to the reduction of tiredness and fatigue. No stimulant, so nothing to spike and nothing to crash from.</p>")
b("benefits", "f2", title="Ready for the next session",
  sub="“I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often” – Ayo P",
  text="<p>The hard session is rarely the problem; the one after it is. That gap between back-to-back days is what customers who train most often tell us changes first, usually before anything moves in their data.</p>")
b("benefits", "f3", title="Built for training blocks",
  sub="“I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint” – Rebeca",
  text="<p>A protocol, not a pre-workout. Two capsules every day through the block, with vitamin D contributing to normal muscle function and zinc and copper to the protection of cells from oxidative stress.</p>")
b("benefits", "f4", title="Fewer flat days",
  sub="“I didn't realise how flat I'd been feeling until this helped lift me out of it” – Holly P",
  text="<p>Not a higher ceiling, a higher floor. The change people describe is less in how good the best sessions feel and more in how rarely they turn up flat.</p>")

b("benefits", "pt", label="What to track", heading="Four numbers.\nOne feeling.",
  lede="Take a 7-day baseline before your first capsule, then compare 30-day averages at day 30, 60 and 90. Your numbers against your own starting point, nobody else’s.")
b("benefits", "ck1", title="HRV", sub="Heart rate variability",
  text="<p>The most-watched recovery marker, and the noisiest night to night. Read it as a 30-day average against your own baseline, never a single morning.</p>")
b("benefits", "ck2", title="Resting heart rate", sub="Your overnight or morning low",
  text="<p>Slow to move and easy to read. Compare the 30-day average at day 30 and day 90 with your baseline week.</p>")
b("benefits", "ck3", title="Sleep", sub="Duration, consistency, sleep score",
  text="<p>Track what your device already records. Note late sessions, travel and alcohol so you can read around them.</p>")
benefit_tpl = json.loads(json.dumps(S["benefits"]["blocks"]["ck3"]))
for key, title, sub, text in [
    ("ck4", "Recovery or readiness", "WHOOP, Oura, Garmin and more",
     "<p>Your device’s own score, built from the numbers above. Useful as a trend, and best read next to how the session actually felt.</p>"),
    ("ck5", "How you feel", "30 seconds a week, no device needed",
     "<p>Once a week, rate energy, recovery, sleep and mood out of 10. The numbers tell you what changed; this tells you whether it matters.</p>"),
]:
    blk = json.loads(json.dumps(benefit_tpl))
    blk["settings"].update(panel="track", title=title, sub=sub, text=text)
    S["benefits"]["blocks"][key] = blk
    if key not in S["benefits"]["block_order"]:
        S["benefits"]["block_order"].append(key)

# ---- Results -----------------------------------------------------------------
s("results", note="Ninety days, in their own words and their own data")

# ---- Ingredients ---------------------------------------------------------------
s("ingredients", lede="Built around 300mg NR, the NAD+ building block, with 18 nutrients alongside it.\nAlready taking D3, K2, B vitamins, zinc, copper or CoQ10 separately? They’re in here, at the doses shown.")

# ---- Steps ---------------------------------------------------------------------
s("steps", heading="Treat it like", heading_right="a training block.")
b("steps", "s1", chip="Days −7 to 0", title="Baseline week.",
  text="Seven days on your wearable before the first capsule: HRV, resting heart rate, sleep and recovery. Add a 1–10 score for how you feel.")
b("steps", "s2", chip="Weeks 1–4", title="Hold the variables.",
  text="Same training, same routine, so any difference is easier to read. Travel, illness, alcohol and big training blocks all move your numbers; log them and read around them.")
b("steps", "s3", chip="Day 30", title="First read.",
  text="Compare 30-day averages with your baseline week, not single nights. Customers often notice recovery and energy before anything shows in their data.")
b("steps", "s4", chip="Day 60–90", title="Your verdict.",
  text="Put day 90 next to your baseline. If it’s not for you, you’re covered.")

# ---- Two capsules ----------------------------------------------------------------
s("twocaps", heading="Two capsules.\nAny training day.", heading_right="Ninety days.")
b("twocaps", "o1", title="Two, with your first meal",
  text="Both capsules together with food. Fat helps the fat-soluble ingredients absorb. Before or after training doesn’t matter; every day does.")
b("twocaps", "o2", title="Not a pre-workout",
  text="No stimulant, nothing to time around a session. A daily routine, so the only thing that matters is that tomorrow looks like today.")
b("twocaps", "o3", title="Check it where you already look",
  text="Your watch or ring is already recording the numbers. Take your baseline week, then read 30-day averages at day 30 and day 90.")

# ---- Guarantee -------------------------------------------------------------------
s("guarantee",
  text="<p>Take a 7-day baseline, give it 90 days, then compare: HRV, resting heart rate, sleep, recovery score and how you feel. If you don’t see a difference, you’re covered with a full refund. And you’re always free to leave: skip, pause or cancel online.</p>")

# ---- FAQ -------------------------------------------------------------------------
b("faq", "q1", title="How do I track it?",
  text="<p>Take a 7-day baseline before your first capsule: HRV, resting heart rate, sleep and your device’s recovery or readiness score, plus a 1–10 rating for how you feel. Then compare 30-day averages at day 30, 60 and 90. Single nights are noise; months are signal.</p>")
b("faq", "q6", title="Which devices work?",
  text="<p>Any device that records HRV, resting heart rate and sleep: Garmin, WHOOP, Oura, Apple Watch, Polar, Coros and others. Use the same device for the whole 90 days so you’re comparing like with like. No device? The weekly 1–10 check-in works too.</p>")
q7 = json.loads(json.dumps(S["faq"]["blocks"]["q6"]))
q7["settings"].update(
    title="Can I take it if I compete?",
    text="<p>Every batch is third-party tested for identity, potency and contaminants before release, and the certificate of analysis is available on request. If you compete under anti-doping rules, check with your governing body before taking any supplement, MUTO included.</p>")
S["faq"]["blocks"]["q7"] = q7
if "q7" not in S["faq"]["block_order"]:
    S["faq"]["block_order"].append("q7")

# ---- Comparison table (shared copy, kit variant) ------------------------------------
compare_table.apply(d, "normal", kit=True)

with open(out, "w") as f:
    if header:
        f.write(header.group(0))
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
