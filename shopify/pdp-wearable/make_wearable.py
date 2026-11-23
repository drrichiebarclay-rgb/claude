"""Build the wearable PDP (product.muto-nad-wearable.json) from the live main PDP (product.muto-nad-bf-premium.json).

Same design, offer, plans, gifts, photos, reviews, tests and ingredient library as the live page; the
messaging is rewritten for people who already do the basics well (sleep, training, food), track on a
wearable, and whose HRV, sleep and recovery numbers have stalled. 30+, around 60% men. The angle is the
biology underneath energy and recovery (NAD+, mitochondria) as the next layer, checked on their own device.

Claims guardrails, as on every MUTO page: authorised nutrient claims worded exactly; wearable metrics are
things to track, never promised effects; customer quotes are real and unchanged; the NR study is labelled
as a study of NR, not of MUTO.

Template-only. Shared snippets whose copy needed changing (the buy box lines, the dark "jobs" band) are
captured in this template and their strings replaced, so no shared file changes and the live page is untouched.

Usage: python3 make_wearable.py [base] [out]
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "base/live__product.muto-nad-bf-premium.json")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "product.muto-nad-wearable.json")

raw = open(base).read()
header = re.match(r"^/\*.*?\*/\s*", raw, flags=re.S)
d = json.loads(raw[header.end():] if header else raw)
S = d["sections"]


def s(sec, **kw):
    S[sec]["settings"].update(kw)


def b(sec, blk, **kw):
    S[sec]["blocks"][blk]["settings"].update(kw)


def add(sec, key, like, **kw):
    blk = json.loads(json.dumps(S[sec]["blocks"][like]))
    blk.pop("disabled", None)
    blk["settings"].update(kw)
    S[sec]["blocks"][key] = blk


def liq(x):
    """A Liquid string literal; single quotes, since the HTML uses double quotes."""
    assert "'" not in x, x
    return "'" + x + "'"


def captured(snippet, pairs, var):
    """Render a shared snippet into a variable and swap strings in it, so the copy changes on this template only."""
    for old, _ in pairs:
        src = open(os.path.join(HERE, "base", "snippets_" + snippet + ".liquid")).read()
        assert src.count(old) >= 1, (snippet, old)
    rep = "".join(" | replace: %s, %s" % (liq(o), liq(n)) for o, n in pairs)
    return "{%%- capture %s -%%}{%%- render '%s' -%%}{%%- endcapture -%%}{{ %s%s }}" % (var, snippet, var, rep)


# ---- Page styles ------------------------------------------------------------------------
# The premium design switches on by template name (muto-nad-bf-premium); this template asks for it by setting.
s("bf_style", design="premium")
# Some styles key off the body class template-muto-nad-bf-premium: give this page the same class, first thing.
hs = S["head_styles"]["settings"]["custom_liquid"]
hs = "<script>document.body.classList.add('template-muto-nad-bf-premium');</script>\n" + hs

# ---- Buy box: lines under the headline (shared snippet, replaced here) ----------------------
BUYBOX = [
    ("Designed for over 35s", "For over-30s who track their recovery"),
    ("is two capsules a day with 19 nutrients at full dose, created by scientists to support your energy, recovery and healthy ageing.",
     "is the layer under sleep, training and food: 300mg NR, which your body turns into NAD<sup>+</sup>, the molecule your mitochondria use to make energy, plus 18 nutrients at full dose. Two capsules a day."),
    ("<b>Got a wearable device? Track the shift on your metrics over weeks and months.</b>",
     "<b>Take a 7-day baseline on your wearable, then read your 30-day averages of HRV, sleep and recovery.</b>"),
    ("No wearable? Tracking isn’t for everyone. A weekly check-in with yourself works too. Set a reminder, notice the difference, and if you don’t by day 90, you get every payment back.",
     "Single nights are noise, months are signal. If you don’t see a difference by day 90, you get every subscription payment back."),
]
old_render = "{%- render 'muto-bf-buybox-copy' -%}"
assert hs.count(old_render) == 1
hs = hs.replace(old_render, captured("muto-bf-buybox-copy", BUYBOX, "mw_bbc"))
# The three ticks under the headline (muto-bf-mars) and the review filter chips (muto-bf-review-box).
# The chips keep their filters (data-f), only the words change.
MARS = [
    ("More energy, fewer afternoon crashes</li>", "The biology behind your energy</li>"),
    ("Recover in time to go again</li>", "Ready for the next session</li>"),
    ("Built for the years ahead</li>", "Built to be tracked on your wearable</li>"),
]
REVIEWS = [
    (">Thinking about the next 20 years</button>", ">Playing the long game</button>"),
    (">Flat by 3pm</button>", ">Energy flat despite good sleep</button>"),
    (">Slower to bounce back</button>", ">Recovery score stuck</button>"),
]
for snip, pairs, var in [("muto-bf-mars", MARS, "mw_mars"), ("muto-bf-review-box", REVIEWS, "mw_rv")]:
    r = "{%%- render '%s' -%%}" % snip
    assert hs.count(r) == 1, snip
    hs = hs.replace(r, captured(snip, pairs, var))
S["head_styles"]["settings"]["custom_liquid"] = hs

s("buy", heading="Doing the basics right? Your numbers still won’t move.")
b("buy", "job1", label="Energy", title="The biology behind your energy")
b("buy", "job2", label="Recovery", title="Ready for the next session")
b("buy", "job4", label="Tracking", title="Built to be checked on your wearable")

b("buy", "fold_benefits", title="Benefits", text=(
    "<p>You already sleep, train and eat with intent. This is the layer underneath: what your cells do with all of it.</p>"
    "<ul>"
    "<li><strong>Energy at the cell level.</strong> 300mg NR, which your body turns into NAD+, the molecule your mitochondria use to make energy, with CoQ10 and PQQ alongside. B vitamins, including 100mcg of active B12, contribute to the reduction of tiredness and fatigue.</li>"
    "<li><strong>Ready for the next session.</strong> 50mcg of vitamin D3 contributes to normal muscle function.</li>"
    "<li><strong>Built to be checked.</strong> Take a 7-day baseline of HRV, resting heart rate, sleep and recovery, then compare 30-day averages at day 30, 60 and 90.</li>"
    "<li><strong>One clean variable.</strong> 19 ingredients at full dose in two capsules, every one on the label, so if your numbers move, you know what changed.</li>"
    "</ul>"
    "<p><strong>Your data. Your verdict. 90 days to decide.</strong></p>"))
# "Who it’s for" is renamed: the page-styles section rewrites any fold whose title contains "who it".
b("buy", "fold1", title="Is it for you?", text=(
    "<p><strong>For people who already do the basics well</strong>: you sleep, train and eat with intent, you track it, "
    "and your HRV, sleep or recovery scores have sat on the same flat line for months anyway.</p>"
    "<p>Most of our customers are in their 30s, 40s and 50s. Works with Garmin, WHOOP, Oura, Apple Watch, Polar and others, "
    "or a weekly 1–10 check-in if you don’t wear one. Adults only; not during pregnancy or breastfeeding.</p>"))

# ---- Dark band under the buy box (shared snippet, replaced here) ---------------------------------
JOBS = [
    ("Not everybody is a 25-year-old PT.", "The basics are done."),
    ("Your life won’t fit a perfect routine.<br class=\"mc-jobs__br\"> Your body still needs one.",
     "Good sleep. Smart training.<br class=\"mc-jobs__br\"> Same flat line."),
    ("You can’t always sleep, train and eat perfectly. MUTO gives your body a daily foundation anyway, so you can keep showing up for work, training and the people who rely on you, now and for years to come.",
     "You’ve done the work: the bedtime, the training plan, the protein, less wine. Your HRV, sleep and recovery scores still sit where they sat months ago. MUTO is the layer underneath the basics, built to be checked on the device you already wear."),
    ("<h3>Afternoons that hold</h3>", "<h3>The cell-level layer</h3>"),
    ("Flat by 3pm? Vitamins B6, B12 and folate help reduce tiredness and fatigue.",
     "300mg NR, which your body turns into NAD<sup>+</sup>. Vitamins B6, B12 and folate contribute to the reduction of tiredness and fatigue."),
    ("For the sessions you care about. Vitamin D supports normal muscle function.",
     "For the sessions you care about. Vitamin D contributes to normal muscle function."),
    ("<h3>Made for a full life</h3>", "<h3>One clean variable</h3>"),
    ("Travel, deadlines, small kids. Two capsules with breakfast. Nothing to mix, nothing to carry.",
     "Change one thing, so if your numbers move, you know why. Two capsules with breakfast."),
]
ag = S["ag1_plans"]["settings"]["custom_liquid"]
old_jobs = "{%- render 'muto-bf-jobs' -%}"
assert ag.count(old_jobs) == 1
S["ag1_plans"]["settings"]["custom_liquid"] = ag.replace(old_jobs, captured("muto-bf-jobs", JOBS, "mw_jobs"))

# ---- Reviews strip: data and recovery quotes first (quotes unchanged) -----------------------------
order = S["reviews_ticker"]["block_order"]
first = ["q11", "q9", "q8", "q10", "q2", "q18", "q13", "q4"]
S["reviews_ticker"]["block_order"] = first + [k for k in order if k not in first]

# ---- Survey: HRV first ----------------------------------------------------------------------
s("survey", heading="What 87 customers reported.",
  lede="We asked 87 men and women aged 30 to 50 who take MUTO what had changed, on their own wearables and in how they feel. Tap a result to see it.")
S["survey"]["block_order"] = ["r4", "r2", "r3", "r1"]

# ---- On this page -----------------------------------------------------------------------------
b("nav", "n1", label="Why it stalls")
b("nav", "n2", label="The biology")
b("nav", "n9", label="The 90-day test")

# ---- Why it happens -------------------------------------------------------------------------------
s("problem", label="Why your numbers stall",
  heading="You’ve fixed the basics.\nYour biology still changed.")
b("problem", "p1", tag="Energy",
  text="<strong class=\"prb-why\">Why the same effort costs more.</strong><span class=\"prb-how\">Your muscles’ capacity to make energy roughly halves between your late 30s and late 60s, however well you train.</span>")
b("problem", "p2", tag="Sleep",
  text="<strong class=\"prb-why\">Why your sleep score plateaus.</strong><span class=\"prb-how\">About 80% less deep sleep in your 40s than at 20, even with a perfect bedtime. Deep sleep is when your body recovers.</span>")
b("problem", "p3", tag="Strength",
  text="<strong class=\"prb-why\">Why you have to work harder to hold it.</strong><span class=\"prb-how\">The muscle adults lose each decade after 30, unless they keep using it.</span>")

# ---- Benefits: the biology ----------------------------------------------------------------------
s("benefits", eyebrow="The biology",
  heading="What’s underneath\nyour numbers.",
  lede="Sleep, training and food are your inputs. Inside every cell, NAD+ and your mitochondria turn them into the energy you train and recover on, and NAD+ levels fall with age. Tap one to see what’s behind it, dose by dose.")
b("benefits", "b1", outcome="Energy at the cell level",
  text="NAD+ sits at the centre of how your mitochondria turn food into usable energy. MUTO gives you 300mg NR, the most allowed in Great Britain, which your body turns into NAD+, with CoQ10 and PQQ alongside. Vitamins B2, B3, B6, B12 and folate contribute to the reduction of tiredness and fatigue.")
b("benefits", "b2", outcome="Ready for the next session",
  text="Your recovery or readiness score is a read-out of how well you’ve bounced back. Vitamin D contributes to normal muscle function, and most of us in the UK get too little sun from October to March. Many customers tell us they notice recovery within the first month.")
b("benefits", "b4", title="The long game", outcome="The trend, not the night",
  text="Zinc, copper and vitamin B2 contribute to the protection of cells from oxidative stress, alongside 300mg NR, TMG, trans-resveratrol and grape seed. This is the baseline you build over months and years, not overnight.")

# ---- Timeline: a 90-day test ---------------------------------------------------------------------------
s("timeline", eyebrow="The 90-day test",
  heading="Run it like\nan experiment.",
  lede="One new variable, a clean baseline and enough time to read a trend. Keep the rest of your routine steady, so your data can tell you something.")
b("timeline", "m1", title="Take your baseline",
  text="<p>Before your first capsule, note your 7-day averages: HRV, resting heart rate, sleep and your recovery or readiness score. Add a 1–10 for how your energy feels. Then take two capsules with breakfast: CoQ10 and vitamins D3 and K2 dissolve in fat, so food helps your body take them in.</p>",
  proof="Same device, same time of day, for the whole 90 days.")
b("timeline", "m1b", title="Feel it before you see it",
  text="<p>Energy is usually what people notice first, before anything shows in their data. B vitamins contribute to the reduction of tiredness and fatigue. If nothing’s obvious yet, that’s normal, because every body runs on its own clock.</p>",
  proof="Too early to read a trend. Keep the rest of your routine steady.")
b("timeline", "m2", title="Your first read",
  text="<p>Compare your 30-day averages with your baseline. Many customers tell us they bounce back from hard sessions sooner by now, and that the steadier days have stopped feeling like a lucky week.</p>",
  proof="Read the 30-day line, never a single morning.")
b("timeline", "m3", title="Read around the noise",
  text="<p>Training blocks, alcohol, travel and illness all move HRV and sleep. Mark them, read around them, and look at whether your baseline itself has shifted. Vitamin D contributes to normal muscle function.</p>",
  proof="Check sleep, training load, alcohol and travel before you judge.")
b("timeline", "m4", title="Your data, your verdict",
  text="<p>Put day 90 next to day 1. If your numbers and your days say keep going, keep going. If it isn’t for you, email us within 14 days and you get every subscription payment back, less delivery.</p>",
  proof="Fewer than 1 in 1,000 people ask for a refund.")

# ---- In their words: training, sleep and recovery quotes (all real, unchanged) ------------------------
for k in ["q3", "q4", "q6"]:
    S["quotes"]["blocks"][k].pop("disabled", None)
for k in ["q8", "q9"]:
    S["quotes"]["blocks"][k]["disabled"] = True

# ---- FAQ -----------------------------------------------------------------------------------------
add("faq", "qb", "q2", title="I already sleep, train and eat well. What’s left?",
    text="<p>That’s exactly who MUTO is for. Good habits set your inputs. NAD+, which falls with age, is part of how your cells turn those inputs into energy, and 300mg of NR a day raised blood NAD+ by about half in a published study (Conze et al., Scientific Reports, 2019, a study of NR, not of MUTO).</p><p>We won’t promise what it does to your numbers. Take a baseline, keep the rest steady, and judge it on your own data over 90 days.</p>")
add("faq", "qh", "q2", title="Will it improve my HRV?",
    text="<p>We won’t promise what any number will do. Take a 7-day baseline, read 30-day averages rather than single nights, and judge it yourself over 90 days. If you don’t see a difference, you’re covered.</p>")
add("faq", "qd", "q2", title="Which devices work?",
    text="<p>Any device that records HRV, resting heart rate and sleep: Garmin, WHOOP, Oura, Apple Watch, Polar, Coros and others. Use the same one for the whole 90 days. No device? A weekly 1–10 check-in works too.</p>")
b("faq", "q5", text="<p>You don’t have to take our word for it. Before your first capsule, note your wearable’s 7-day averages for HRV, resting heart rate, sleep and recovery: that’s your baseline. Compare your 30-day averages at day 30, 60 and 90, and read the trend, not single nights. Training load, alcohol, travel and illness all move the numbers, so mark them as you go.</p>")
S["faq"]["block_order"] = ["qb", "qh", "q5", "qd", "q4", "q16", "q2", "q6", "q14", "q10", "q9", "q15", "q11", "q13", "q12", "q3"] + \
    [k for k in S["faq"]["block_order"] if k in ("q1", "q7", "q8")]

with open(out, "w") as f:
    if header:
        f.write(header.group(0))
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out, os.path.getsize(out))
