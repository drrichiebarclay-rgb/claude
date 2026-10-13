"""Build the high-performer PDP (product.muto-nad-performance.json) from the draft creatine-kit page.

Same offer, plans, gifts, images, CTAs and comparison table; copy rewritten for a
30-35-year-old high performer (work, training, life) who tracks HRV, resting heart
rate, sleep, recovery and stress.
Claims: authorised claims only; wearable metrics are things to *track*, never effects.

Usage: python3 make_performance.py [base] [out]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import compare_table  # noqa: E402

base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "../pdp-creatine-kit/product.muto-nad-creatine-kit.json")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "product.muto-nad-performance.json")

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
s("buy", text="<p>For people who perform at a high level, at work, in training and at home, and track how it’s going. Energy that lasts past the 4pm meeting and into the evening. Recovery that keeps up with your week. A steadier head when everything peaks at once. Two capsules a day built around 300mg NR, the NAD+ building block, with B vitamins that contribute to normal energy-yielding metabolism and normal psychological function, and vitamin D for normal muscle function. Take a baseline on your wearable and judge it on your own numbers.</p>")
b("buy", "b1", text="Energy that lasts past the 4pm meeting")
b("buy", "b2", text="Bounce back from big days and hard sessions")
b("buy", "b3", text="Built for weeks when everything peaks at once")
b("buy", "b4", text="Track it on your wearable for 90 days, or your money back")
b("buy", "a3", text="<p>Two capsules together each morning with your first meal. Fat helps the fat-soluble ingredients absorb, so whatever you already eat first is the right time. Before a meeting or after a session doesn’t matter; taking it every day does. No caffeine, no cycling, no loading and no rest days.</p>")
b("buy", "a5", text="<p>Take a 7-day baseline, give it ninety days and compare: HRV, resting heart rate, sleep, your recovery or stress score, or simply how you feel. If you don’t see a difference, you get your money back in full.</p>")
# Energy, focus and recovery testimonials first (quotes unchanged, just reordered)
order = S["buy"]["block_order"]
snips = [k for k in order if k.startswith("snippet_")]
first = ["snippet_6", "snippet_1", "snippet_2", "snippet_3", "snippet_7", "snippet_4"]
new_snips = first + [k for k in snips if k not in first]
it = iter(new_snips)
S["buy"]["block_order"] = [next(it) if k.startswith("snippet_") else k for k in order]

# ---- Problem: one card per pillar, then the stack ----------------------------
s("problem",
  heading="High output.\nSame body.\nOne recovery budget.",
  lede="Your body doesn’t keep separate accounts. A board meeting, a long-haul flight and a hard session all draw from the same place, and your HRV shows it. Most supplements ask you to trust them. MUTO is one protocol you can test against your own data.")
b("problem", "c1", quote="“Sharp at 9am. Gone by 4pm.”",
  text="The afternoon is where the real work, and the evening, get decided.")
b("problem", "c2", quote="“A big day costs me two.”",
  text="A late night, a long flight or a hard session, and the next day pays for it.")
b("problem", "c4", quote="“HRV down. Deadline up.”",
  text="Work stress and training stress land in the same numbers. Your watch can’t tell them apart.")
b("problem", "c3", quote="“A shelf full of pills.”",
  text="Five products, overlapping doses, no idea which one is pulling its weight.")
S["problem"]["block_order"] = ["c1", "c2", "c4", "c3"]

# ---- Why MUTO --------------------------------------------------------------
b("why", "w1", text="Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by a board of performance, sleep, metabolism and longevity experts. Got a question? Ask him.")
b("why", "w2", text="Nineteen ingredients, each on the label with its dose and why it’s there. No proprietary blends. Made in the UK to GMP standards and third-party tested batch by batch.")
b("why", "w3", title="Built to be measured.",
  text="Take a 7-day baseline of HRV, resting heart rate, sleep, recovery and stress, then compare 30-day averages at day 30 and day 90. Your data, your verdict, with a 90-day guarantee behind it.")

# ---- Board -----------------------------------------------------------------
s("board", note="Our Scientific Advisory Board: performance, sleep, metabolism and longevity, from international rugby to clinical practice.")

# ---- Benefits: feel (energy, recovery, stress, the block) + track ------------
b("benefits", "pf", label="What you’ll feel", heading="Energy. Recovery.\nStress.",
  lede="What customers tell us changes first. Individual experiences, not a promise. Open any of them for more.")
b("benefits", "f1", title="Energy past 4pm",
  sub="“No afternoon slump and in general feeling great” – Lynda",
  text="<p>The real test isn’t the first hour. It’s the 4pm meeting, the evening session, and still being present at home. NAD+ sits at the centre of how your cells turn food into usable energy, and B vitamins contribute to normal energy-yielding metabolism and the reduction of tiredness and fatigue. No caffeine, so no 4pm crash.</p>")
b("benefits", "f2", title="Bounce back from big days",
  sub="“Has actually changed my recovery” – Adam H",
  text="<p>A late night, a long-haul flight, a hard session: the cost shows up the next day. How quickly that next day feels normal is what customers most often tell us changes, often before anything moves in their data. Vitamin D contributes to normal muscle function.</p>")
b("benefits", "f3", title="A steadier head when it all peaks",
  sub="“More focused during the day” – Alexandra",
  text="<p>Launch week, board week, race week: same body. Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function, and pantothenic acid to normal mental performance. Customers describe the heavy weeks feeling less heavy.</p>")
b("benefits", "f4", title="Fewer flat days",
  sub="“I didn't realise how flat I'd been feeling until this helped lift me out of it” – Holly P",
  text="<p>Not a higher ceiling, a higher floor. The change people describe is less in how good the best days feel and more in how rarely they turn up flat. Zinc and copper contribute to the protection of cells from oxidative stress.</p>")

b("benefits", "pt", label="What to track", heading="Four numbers.\nOne feeling.",
  lede="Energy, recovery and stress all show up on your wearable. Take a 7-day baseline, then compare 30-day averages at day 30, 60 and 90, against your own starting point.")
b("benefits", "ck1", title="HRV", sub="Recovery and stress load",
  text="<p>The number that reacts to everything: hard sessions, deadlines, long flights, short nights. Read it as a 30-day average against your baseline, never a single morning. If your device shows a stress score, track it alongside.</p>")
b("benefits", "ck2", title="Resting heart rate", sub="Recovery and overall load",
  text="<p>Slow to move and easy to read. Creeping up usually means your week is outrunning your recovery. Compare the 30-day average at day 30 and day 90 with your baseline week.</p>")
b("benefits", "ck3", title="Sleep", sub="Where recovery happens",
  text="<p>Duration, consistency and your sleep score, as your device records them. Note late nights, travel and alcohol so you can read around them.</p>")
benefit_tpl = json.loads(json.dumps(S["benefits"]["blocks"]["ck3"]))
for key, title, sub, text in [
    ("ck4", "Readiness or Body Battery", "Your energy for the day",
     "<p>WHOOP Recovery, Oura Readiness, Garmin Body Battery or Training Readiness. Read the trend, next to how the day actually felt.</p>"),
    ("ck5", "How you feel", "Energy, recovery, stress: 1–10",
     "<p>Once a week, rate energy, recovery, stress and sleep out of 10. Thirty seconds. The numbers show what changed; this shows whether you noticed.</p>"),
]:
    blk = json.loads(json.dumps(benefit_tpl))
    blk["settings"].update(panel="track", title=title, sub=sub, text=text)
    S["benefits"]["blocks"][key] = blk
    if key not in S["benefits"]["block_order"]:
        S["benefits"]["block_order"].append(key)

# ---- Results -----------------------------------------------------------------
s("results", note="Ninety days, in their own words")

# ---- Ingredients ---------------------------------------------------------------
s("ingredients", lede="Built around 300mg NR, the NAD+ building block, with 18 nutrients alongside it.\nAlready taking D3, K2, B vitamins, zinc, copper or CoQ10 separately? They’re in here, at the doses shown.")

# ---- Steps ---------------------------------------------------------------------
s("steps", heading="Run it like", heading_right="an experiment.")
b("steps", "s1", chip="Days −7 to 0", title="Baseline week.",
  text="Seven days on your wearable before the first capsule: HRV, resting heart rate, sleep and recovery. Add a 1–10 score for energy, recovery and stress.")
b("steps", "s2", chip="Weeks 1–4", title="Hold the variables.",
  text="Same routine, same training, so any difference is easier to read. Travel, illness, alcohol and big weeks all move your numbers; log them and read around them.")
b("steps", "s3", chip="Day 30", title="First read.",
  text="Compare 30-day averages with your baseline week, not single nights. Customers often notice energy and recovery before anything shows in their data.")
b("steps", "s4", chip="Day 60–90", title="Your verdict.",
  text="Put day 90 next to your baseline. If it’s not for you, you’re covered.")

# ---- Two capsules ----------------------------------------------------------------
s("twocaps", heading="Two capsules.\nAny kind of day.", heading_right="Ninety days.")
b("twocaps", "o1", title="Two, with your first meal",
  text="Both capsules together with food. Fat helps the fat-soluble ingredients absorb. Before a meeting or after a session doesn’t matter; every day does.")
b("twocaps", "o2", title="Not a stimulant",
  text="No caffeine, nothing to time around meetings or sessions. A daily routine, so the only thing that matters is that tomorrow looks like today.")
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
    title="Is there caffeine in it?",
    text="<p>No. No caffeine and no stimulants, so there’s nothing to time around meetings, training or bedtime, and your coffee stays as it is. Every batch is third-party tested for identity, potency and contaminants before release.</p>")
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
