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
# Three pillars: energy, recovery, stress. Felt benefits are framed as what customers
# report; effect claims are the authorised ones only (B vitamins, vitamin D, zinc, copper).
s("buy", text="<p>Energy for the evening session after a full workday. Legs back for the next morning. A steadier head when work and training both pile on. Two capsules a day built around 300mg NR, the NAD+ building block, with B vitamins that contribute to normal energy-yielding metabolism and normal psychological function, and vitamin D for normal muscle function. Take a baseline on your wearable and judge it on your own numbers.</p>")
b("buy", "b1", text="Energy that lasts to the evening session")
b("buy", "b2", text="Ready for the next session, not the one after")
b("buy", "b3", text="Built for weeks when work and training both peak")
b("buy", "b4", text="Track it on your wearable for 90 days, or your money back")
b("buy", "a3", text="<p>Two capsules together each morning with your first meal. Fat helps the fat-soluble ingredients absorb, so whatever you already eat first is the right time. Before or after training doesn’t matter; taking it every day does. No caffeine, no cycling, no loading and no rest days.</p>")
b("buy", "a5", text="<p>Take a 7-day baseline, give it ninety days and compare: HRV, resting heart rate, sleep, your recovery or stress score, or simply how you feel. If you don’t see a difference, you get your money back in full.</p>")
# Training and energy testimonials first (quotes unchanged, just reordered)
order = S["buy"]["block_order"]
snips = [k for k in order if k.startswith("snippet_")]
first = ["snippet_4", "snippet_6", "snippet_9", "snippet_3", "snippet_2", "snippet_1"]
new_snips = first + [k for k in snips if k not in first]
it = iter(new_snips)
S["buy"]["block_order"] = [next(it) if k.startswith("snippet_") else k for k in order]

# ---- Problem: one card per pillar, then the stack ----------------------------
s("problem",
  heading="Training stress.\nWork stress.\nOne recovery budget.",
  lede="Your body doesn’t keep separate accounts. A deadline week and a threshold session draw from the same place, and your HRV shows it. Most supplements ask you to trust them. MUTO is one protocol you can test against your own data.")
b("problem", "c1", quote="“Nothing left for the 6pm session.”",
  text="Sharp at 9am. Running on empty by the time you change for training.")
b("problem", "c2", quote="“Tuesday’s intervals. Wednesday’s dead legs.”",
  text="The hard session is fine. The one after it is where recovery shows.")
b("problem", "c4", quote="“HRV down. Deadline up.”",
  text="Work stress and training stress land in the same numbers. Your watch can’t tell them apart.")
b("problem", "c3", quote="“A shelf full of pills.”",
  text="Five products, overlapping doses, no idea which one is pulling its weight.")
S["problem"]["block_order"] = ["c1", "c2", "c4", "c3"]

# ---- Why MUTO --------------------------------------------------------------
b("why", "w1", text="Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by a board that includes an international rugby performance nutritionist and a sleep doctor. Got a question? Ask him.")
b("why", "w2", text="Nineteen ingredients, each on the label with its dose and why it’s there. No proprietary blends. Made in the UK to GMP standards and third-party tested batch by batch.")
b("why", "w3", title="Built to be measured.",
  text="Take a 7-day baseline of HRV, resting heart rate, sleep, recovery and stress, then compare 30-day averages at day 30 and day 90. Your data, your verdict, with a 90-day guarantee behind it.")

# ---- Board -----------------------------------------------------------------
s("board", note="Our Scientific Advisory Board: performance, sleep, metabolism and longevity, from international rugby to clinical practice.")

# ---- Benefits: feel (energy, recovery, stress, the block) + track ------------
b("benefits", "pf", label="What you’ll feel", heading="Energy. Recovery.\nStress.",
  lede="What customers who train tell us changes first. Individual experiences, not a promise. Open any of them for more.")
b("benefits", "f1", title="Energy at 6pm, not just 9am",
  sub="“I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore” – Danny S",
  text="<p>The real test isn’t the first hour. It’s whether there’s anything left for the evening session after a full day. NAD+ sits at the centre of how your cells turn food into usable energy, and B vitamins contribute to normal energy-yielding metabolism and the reduction of tiredness and fatigue. No caffeine, so no 4pm crash.</p>")
b("benefits", "f2", title="Legs back for the next session",
  sub="“I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often” – Ayo P",
  text="<p>Back-to-back days are the test: Tuesday’s intervals, then Wednesday’s run. That gap is what customers who train most often tell us changes first, often before anything moves in their data. Vitamin D contributes to normal muscle function.</p>")
b("benefits", "f3", title="A steadier head in heavy weeks",
  sub="“More focused during the day” – Alexandra",
  text="<p>Big work week, big training week, same body. Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function, and pantothenic acid to normal mental performance. Customers describe the heavy weeks feeling less heavy.</p>")
b("benefits", "f4", title="Through a full training block",
  sub="“I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint” – Rebeca",
  text="<p>Not a pre-workout for the big days. Two capsules every day through the block, with zinc and copper contributing to the protection of cells from oxidative stress, the kind hard training produces.</p>")

b("benefits", "pt", label="What to track", heading="Four numbers.\nOne feeling.",
  lede="Energy, recovery and stress all show up on your wearable. Take a 7-day baseline, then compare 30-day averages at day 30, 60 and 90, against your own starting point.")
b("benefits", "ck1", title="HRV", sub="Recovery and stress load",
  text="<p>The number that reacts to everything: hard sessions, deadlines, short nights. Read it as a 30-day average against your baseline, never a single morning. If your device shows a stress score, track it alongside.</p>")
b("benefits", "ck2", title="Resting heart rate", sub="Recovery and training load",
  text="<p>Slow to move and easy to read. Creeping up usually means load is outrunning recovery. Compare the 30-day average at day 30 and day 90 with your baseline week.</p>")
b("benefits", "ck3", title="Sleep", sub="Where recovery happens",
  text="<p>Duration, consistency and your sleep score, as your device records them. Note late sessions, travel and alcohol so you can read around them.</p>")
benefit_tpl = json.loads(json.dumps(S["benefits"]["blocks"]["ck3"]))
for key, title, sub, text in [
    ("ck4", "Readiness or Body Battery", "Your energy for the day",
     "<p>WHOOP Recovery, Oura Readiness, Garmin Body Battery or Training Readiness. Read the trend, next to how the session actually felt.</p>"),
    ("ck5", "How you feel", "Energy, recovery, stress: 1–10",
     "<p>Once a week, rate energy, recovery, stress and sleep out of 10. Thirty seconds. The numbers show what changed; this shows whether you noticed.</p>"),
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
  text="Seven days on your wearable before the first capsule: HRV, resting heart rate, sleep and recovery. Add a 1–10 score for energy, recovery and stress.")
b("steps", "s2", chip="Weeks 1–4", title="Hold the variables.",
  text="Same training, same routine, so any difference is easier to read. Travel, illness, alcohol and big training blocks all move your numbers; log them and read around them.")
b("steps", "s3", chip="Day 30", title="First read.",
  text="Compare 30-day averages with your baseline week, not single nights. Customers often notice energy and recovery before anything shows in their data.")
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
  text="<p>Take a 7-day baseline, give it 90 days, then compare: HRV, resting heart rate, sleep, your recovery or stress score, and how you feel. If you don’t see a difference, you’re covered with a full refund. And you’re always free to leave: skip, pause or cancel online.</p>")

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
q8 = json.loads(json.dumps(S["faq"]["blocks"]["q6"]))
q8["settings"].update(
    title="Will it help with stress?",
    text="<p>It isn’t a calming supplement, and it won’t make a hard week easy. Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function, and pantothenic acid to normal mental performance. To see how heavy weeks land, track HRV and your device’s stress score through the 90 days and compare them with your baseline.</p>")
S["faq"]["blocks"]["q8"] = q8
fo = S["faq"]["block_order"]
if "q8" not in fo:
    fo.insert(fo.index("q6") + 1, "q8")

# ---- Comparison table (shared copy, kit variant) ------------------------------------
compare_table.apply(d, "normal", kit=True)

with open(out, "w") as f:
    if header:
        f.write(header.group(0))
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
