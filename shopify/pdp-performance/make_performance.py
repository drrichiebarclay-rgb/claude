"""Build PDP 4 (product.muto-nad-performance.json) from the draft creatine-kit page.

Same offer, plans, gifts, images, CTAs and comparison table; copy rewritten for a
broad, educated 30-35 audience with full, busy lives, around energy, recovery and
stress. Tracking works with a weekly check-in or a wearable.
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
# Three benefits: energy, recovery, stress, for busy lives in general (work, family,
# workouts, travel). Felt benefits are framed as what customers report; effect claims
# are the authorised ones only (B vitamins, vitamin D, zinc, copper). A wearable is optional.
s("buy", text="<p>You’re doing more than ever. MUTO lets you see if it’s working. NR, which your body turns into NAD+, plus 18 supporting ingredients, every dose on the label. Two capsules with breakfast, then track your energy, recovery and stress on your wearable. 90 days to judge it, or your money back on subscriptions.</p>")
b("buy", "b1", text="Energy that lasts through the afternoon")
b("buy", "b2", text="Bounce back from late nights, travel and workouts")
b("buy", "b3", text="Built for busy, stressful weeks")
b("buy", "b4", text="Feel the difference in 90 days, or your money back")
b("buy", "a3", text="<p>Two capsules together each morning with your first meal. Fat helps the fat-soluble ingredients absorb, so whatever you already eat first is the right time. Taking it every day is what matters. No caffeine, no cycling, no loading and no rest days.</p>")
b("buy", "a5", text="<p>Note your starting point, give it ninety days and compare: how your days feel, or your wearable’s HRV, sleep and recovery. If you don’t see a difference, you get your money back in full.</p>")
# Energy and everyday testimonials first (quotes unchanged, just reordered)
order = S["buy"]["block_order"]
snips = [k for k in order if k.startswith("snippet_")]
first = ["snippet_1", "snippet_6", "snippet_2", "snippet_5", "snippet_7", "snippet_3"]
new_snips = first + [k for k in snips if k not in first]
it = iter(new_snips)
S["buy"]["block_order"] = [next(it) if k.startswith("snippet_") else k for k in order]

# ---- Problem: one card per benefit, then the stack ---------------------------
s("problem",
  heading="Busy life.\nSame body.\nOne energy budget.",
  lede="Your body doesn’t keep separate accounts. Work, workouts, kids, late nights and travel all draw from the same place, and you feel it by mid-afternoon. Most supplements ask you to trust them. MUTO is one protocol you can check for yourself.")
b("problem", "c1", quote="“Sharp at 9am. Gone by 4pm.”",
  text="The afternoon is where the day, and the evening, get decided.")
b("problem", "c2", quote="“One late night costs me two days.”",
  text="A late night, a long trip or a hard workout, and the next day pays for it.")
b("problem", "c4", quote="“Always on. Never off.”",
  text="Work, home, training: it all lands in the same place, and it all adds up.")
b("problem", "c3", quote="“A shelf full of pills.”",
  text="Five products, overlapping doses, no idea which one is pulling its weight.")
S["problem"]["block_order"] = ["c1", "c2", "c4", "c3"]

# ---- Why MUTO --------------------------------------------------------------
b("why", "w1", text="Formulated by Richie Barclay, PhD in cellular biology and nutrition, and reviewed by our Scientific Advisory Board of doctors and scientists. Got a question? Ask him.")
b("why", "w2", text="Nineteen ingredients, each on the label with its dose and why it’s there. No proprietary blends. Made in the UK to GMP standards and third-party tested batch by batch.")
b("why", "w3", title="Built to be checked.",
  text="Note how you feel on day 0, or take a 7-day baseline on your wearable, then check in at day 30 and day 90. Your verdict, with a 90-day guarantee behind it.")

# ---- Benefits: feel (energy, recovery, stress, flat days) + ways to check -----
b("benefits", "pf", label="What you’ll feel", heading="Energy. Recovery.\nStress.",
  lede="What customers tell us changes first. Individual experiences, not a promise. Open any of them for more.")
b("benefits", "f1", title="Energy past 4pm",
  sub="“No afternoon slump and in general feeling great” – Lynda",
  text="<p>The real test isn’t the first hour. It’s the 4pm slump, the evening workout, and still having something left for the people at home. NAD+ sits at the centre of how your cells turn food into usable energy, and B vitamins contribute to normal energy-yielding metabolism and the reduction of tiredness and fatigue. No caffeine, so no crash.</p>")
b("benefits", "f2", title="Bounce back faster",
  sub="“Has actually changed my recovery” – Adam H",
  text="<p>A late night, a long trip, a hard workout: the cost shows up the next day. How quickly that next day feels normal is what customers most often tell us changes. Vitamin D contributes to normal muscle function.</p>")
b("benefits", "f3", title="A steadier head in busy weeks",
  sub="“More focused during the day” – Alexandra",
  text="<p>Deadlines, family, everything at once: same body. Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function, and pantothenic acid to normal mental performance. Customers describe the heavy weeks feeling less heavy.</p>")
b("benefits", "f4", title="Fewer flat days",
  sub="“I didn't realise how flat I'd been feeling until this helped lift me out of it” – Holly P",
  text="<p>Not a higher ceiling, a higher floor. The change people describe is less in how good the best days feel and more in how rarely they turn up flat. Zinc and copper contribute to the protection of cells from oxidative stress.</p>")

b("benefits", "pt", label="Ways to check", heading="Check it\nyour way.",
  lede="With a wearable or without one. Note your starting point, then compare at day 30, 60 and 90.")
b("benefits", "ck1", title="HRV", sub="If you wear a device",
  text="<p>The number that reacts to everything: busy weeks, workouts, short nights. Read it as a 30-day average against your own baseline, never a single morning. If your device shows a stress score, track it alongside.</p>")
b("benefits", "ck2", title="Resting heart rate", sub="Slow to move, easy to read",
  text="<p>Creeping up usually means your week is outrunning your recovery. Compare the 30-day average at day 30 and day 90 with your starting point.</p>")
b("benefits", "ck3", title="Sleep", sub="Where recovery happens",
  text="<p>Duration, consistency and your sleep score, as your device records them. Note late nights, travel and alcohol so you can read around them.</p>")
benefit_tpl = json.loads(json.dumps(S["benefits"]["blocks"]["ck3"]))
for key, title, sub, text in [
    ("ck4", "Readiness or Body Battery", "Your energy for the day",
     "<p>WHOOP Recovery, Oura Readiness, Garmin Body Battery and others. Read the trend, next to how the day actually felt.</p>"),
    ("ck5", "A 30-second weekly check-in", "No device needed",
     "<p>Once a week, rate your energy, recovery, stress and sleep out of 10. Felt changes are easy to forget, so writing them down turns a feeling into a record you can look back on.</p>"),
]:
    blk = json.loads(json.dumps(benefit_tpl))
    blk["settings"].update(panel="track", title=title, sub=sub, text=text)
    S["benefits"]["blocks"][key] = blk
# Weekly check-in first: it works for everyone
S["benefits"]["block_order"] = ["pf", "f1", "f2", "f3", "f4", "pt", "ck5", "ck1", "ck2", "ck3", "ck4"]

# ---- Ingredients ---------------------------------------------------------------
s("ingredients", lede="Built around 300mg NR, the NAD+ building block, with 18 nutrients alongside it.\nAlready taking D3, K2, B vitamins, zinc, copper or CoQ10 separately? They’re in here, at the doses shown.")

# ---- Steps ---------------------------------------------------------------------
s("steps", heading="Not a quick fix.", heading_right="A 90-day check.")
b("steps", "s1", chip="Day 0", title="Note your starting point.",
  text="A 30-second check-in on energy, recovery, stress and sleep, or a 7-day average if you wear a device.")
b("steps", "s2", chip="Weeks 1–4", title="Keep the rest steady.",
  text="Same routine, so any difference is easier to read. Travel, illness, alcohol and big weeks all move how you feel; note them and read around them.")
b("steps", "s3", chip="Day 30", title="First check-in.",
  text="Compare with day 0. Customers often notice energy and recovery in how their days feel before anything shows in their data.")
b("steps", "s4", chip="Day 60–90", title="Your verdict.",
  text="Put day 90 next to day 0. If it’s not for you, you’re covered.")

# ---- Two capsules ----------------------------------------------------------------
s("twocaps", heading="Two capsules.\nAny kind of day.", heading_right="Ninety days.")
b("twocaps", "o1", title="Two, with your first meal",
  text="Both capsules together with food. Fat helps the fat-soluble ingredients absorb. Whatever you eat first is the right time; every day is what matters.")
b("twocaps", "o2", title="Not a stimulant",
  text="No caffeine, nothing to time around your day. A daily routine, so the only thing that matters is that tomorrow looks like today. Most people keep the jar next to the coffee.")
b("twocaps", "o3", title="Check it your way",
  text="A 30-second weekly note, or the watch or ring you already wear. Note your starting point on day 0, then check in at day 30 and day 90.")

# ---- Guarantee -------------------------------------------------------------------
s("guarantee",
  text="<p>Note your starting point, give it 90 days, then compare: how your days feel, or your wearable’s HRV, sleep and recovery. If you don’t see a difference, you’re covered with a full refund. And you’re always free to leave: skip, pause or cancel online.</p>")

# ---- FAQ -------------------------------------------------------------------------
b("faq", "q1", title="How will I know if it’s working?",
  text="<p>Note your starting point before your first capsule: a 30-second check-in (energy, recovery, stress and sleep, each out of 10), or a 7-day average from your wearable. Then compare at day 30, 60 and 90. Single days are noise; months are signal.</p>")
b("faq", "q6", title="Do I need a wearable?",
  text="<p>No. The 30-second weekly check-in works on its own. If you do wear one (Garmin, WHOOP, Oura, Apple Watch and others), use the same device for the whole 90 days and compare 30-day averages of HRV, resting heart rate and sleep.</p>")
q7 = json.loads(json.dumps(S["faq"]["blocks"]["q6"]))
q7["settings"].update(
    title="Is there caffeine in it?",
    text="<p>No. No caffeine and no stimulants, so there’s nothing to time around your day, and your coffee stays as it is. Every batch is third-party tested for identity, potency and contaminants before release.</p>")
S["faq"]["blocks"]["q7"] = q7
q8 = json.loads(json.dumps(S["faq"]["blocks"]["q6"]))
q8["settings"].update(
    title="Will it help with stress?",
    text="<p>It isn’t a calming supplement, and it won’t make a hard week easy. Vitamins B6, B12, thiamin, niacin and biotin contribute to normal psychological function, and pantothenic acid to normal mental performance. To see how busy weeks land, rate stress in your weekly check-in, or track HRV and your device’s stress score, and compare with your starting point.</p>")
S["faq"]["blocks"]["q8"] = q8
S["faq"]["block_order"] = ["q1", "q6", "q8", "q2", "q3", "q4", "q5", "q7"]

# ---- Comparison table (shared copy, kit variant) ------------------------------------
compare_table.apply(d, "normal", kit=True)

with open(out, "w") as f:
    if header:
        f.write(header.group(0))
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
