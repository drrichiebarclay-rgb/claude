"""Home page: brings templates/index.json in line with the new pages.

Starts from index-base.json (the draft theme's home template as of 21 Oct) and rewrites the NAD+
copy so it says what the product page, the science page and the ingredients page say:

  - the product: "Not another multivitamin. The next generation of one." 19 ingredients, two capsules,
    five jobs (Energy, Recovery, Mind, Ageing well, Immunity) and one jar instead of five pots
  - who it's for: 40s, 50s and 60s, still working, keeping up with family; no need to be sporty
  - the 90 days: score day 1, check in at day 30 and 90, every subscription payment back
  - links to /pages/science, /pages/ingredients and /pages/standards where each topic goes deeper

Sections changed: hero (sub), shop (NAD+ tab), founder (one line), board (heading), benefits (NAD+ tab,
now the product page's six benefits), science_nad (all five tabs). Creatine, essentials, athletes,
banner, stats and the sticky bar are untouched.
Usage: python3 build.py
"""
import copy, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "index-base.json")))
S = T["sections"]

SCI = '<a href="/pages/science">the science, made simple</a>'
ING = '<a href="/pages/ingredients">all 19 ingredients</a>'
STD = '<a href="/pages/standards">our standards</a>'


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


# ---- Hero ----
S["hero"]["settings"]["subheading"] = ("Not another multivitamin. The next generation of one: 19 ingredients for energy, recovery, "
                                       "a clearer head, ageing well and immunity, in two capsules a day. 90 days to feel the difference.")

# ---- Shop the protocol: NAD+ tab ----
sh = S["shop"]["blocks"]
sh["pn"]["settings"]["lede"] = "Not another multivitamin. The next generation of one."
sh["s1"]["settings"]["text"] = ("<strong>Built for life after 35.</strong> Afternoons that fade sooner. Busy weeks that take longer to "
                                "bounce back from. Your cells use NAD+ to make energy, and you make less of it as you get older. "
                                f"MUTO gives them 19 ingredients to work with. Read {SCI}.")
sh["s2"]["settings"]["text"] = ("<strong>One jar, nothing hidden.</strong> Two capsules with breakfast, in place of up to five pots. "
                                f"Every dose on the label, every batch tested, made in the UK. See {ING}.")
sh["s3"]["settings"]["text"] = ("<strong>90 days to decide.</strong> Score how you feel on day 1, then check in at day 30 and day 90. "
                                "If you don’t feel the difference, you get every subscription payment back.")

# ---- Founder: who takes it, as on the product page ----
S["founder"]["blocks"]["p1b"]["settings"]["text"] = ("I’m not done yet either. Most of the people who take MUTO are in their 40s and 50s: "
                                                     "still working, keeping up with family, and not ready to slow down.")

# ---- Board: the product page's heading ----
S["board"]["settings"]["heading"] = "Meet the experts\nbehind MUTO."

# ---- Where you'll feel it: the product page's six benefits ----
be = S["benefits"]
be["blocks"]["bpn"]["settings"]["lede"] = ("Not another multivitamin. The next generation of one. Five jobs and one jar, "
                                           "built for what your body needs after 35. "
                                           '<a href="/pages/ingredients">See which ingredient does what</a>.')
ROWS = [("Energy", "Afternoons that don’t fade."), ("Recovery", "Bounce back from a busy week."),
        ("Mind", "A clearer head, all day."), ("Ageing well", "Age on your own terms."),
        ("Immunity", "Stay well through winter."), ("Simplicity", "One jar replaces five.")]
old = [k for k in be["block_order"] if be["blocks"][k]["type"] == "benefit" and be["blocks"][k]["settings"]["panel"] == "nad"]
at = be["block_order"].index(old[0])
for k in old:
    del be["blocks"][k]
    be["block_order"].remove(k)
for i, (t, x) in enumerate(ROWS, 1):
    be["blocks"][f"bn{i}"] = {"type": "benefit", "settings": {"panel": "nad", "title": t, "text": x}}
    be["block_order"].insert(at + i - 1, f"bn{i}")

# ---- The science: NAD+ Cellular Complex, all five tabs ----
sc = S["science_nad"]
sc["settings"]["lede"] = "What changes in your body after 35, and why you feel it in your afternoons, your recovery and how you age."
PANELS = {
    "sp1": p("Not another multivitamin. The next generation of one. MUTO gives you the active vitamins and minerals you’d want "
             "from a good multivitamin, plus the cellular science most leave out: NR for NAD⁺, CoQ10, PQQ and resveratrol.",
             "Five jobs in one daily jar: <strong>energy</strong> that holds through the afternoon, <strong>recovery</strong> "
             "from a busy week, a clearer <strong>mind</strong>, <strong>ageing well</strong> and <strong>immunity</strong>. "
             "Two capsules, 19 ingredients, one jar instead of five pots."),
    "sp2": p("Every cell makes its own energy, in tiny power stations called mitochondria. NAD⁺ is the courier that carries "
             "energy from your food to them, all day. From your mid-30s your body makes less of it: fewer couriers, the same work.",
             "You notice it in your day before you’d call it ageing: afternoons that fade, busy weeks that take longer to "
             "bounce back from. It’s like your body has switched to low power mode.",
             "MUTO gives your cells NR, which they turn into NAD⁺, plus what helps them use it: active B vitamins, CoQ10 and "
             "PQQ for your mitochondria, and zinc and copper to help protect your cells. Not a stimulant. A better baseline, "
             "built every day.",
             f"Go deeper: {SCI}."),
    "sp3": p("19 ingredients, every dose on the label. No proprietary blends, no fillers.")
           + "<ul>"
           + "<li><strong>Energy:</strong> NR 300mg, CoQ10 150mg, PQQ 20mg and the active B vitamins.</li>"
           + "<li><strong>Recovery:</strong> vitamin D3 2,000 IU, B2, CoQ10 and PQQ.</li>"
           + "<li><strong>Mind:</strong> B6, B12, folate (5-MTHF) and zinc.</li>"
           + "<li><strong>Ageing well:</strong> NR with TMG 450mg, trans-resveratrol 50mg, grape seed extract 150mg and vitamin K2 100µg.</li>"
           + "<li><strong>Immunity:</strong> vitamin D3, zinc 15mg and copper 1mg (both bisglycinate), folate, B6 and B12.</li>"
           + "</ul>"
           + p(f"Vegan capsules, made in the UK to GMP standards, every batch tested. See {ING} and {STD}."),
    "sp4": p("Adults in their 40s, 50s and 60s. Most of our customers are in their 40s and 50s: still working, keeping up "
             "with family and the things they love, and not ready to slow down.",
             "It’s for you if your afternoons fade sooner than they used to, busy weeks take longer to bounce back from, "
             "or you’re taking five supplements and don’t know which one’s working.",
             "You don’t need to be sporty or own a smartwatch. And it’s not for anyone chasing a buzz: no caffeine, no stimulants."),
    "sp5": p("Two capsules with breakfast, every day.")
           + "<ul>"
           + "<li><strong>Day 1:</strong> score your afternoons, sleep and recovery out of 10.</li>"
           + "<li><strong>Day 30:</strong> afternoons that hold. Usually the first thing people notice.</li>"
           + "<li><strong>Day 60:</strong> bouncing back sooner from busy weeks.</li>"
           + "<li><strong>Day 90:</strong> compare with day 1. Not for you? You get every subscription payment back.</li>"
           + "</ul>",
}
for k, html in PANELS.items():
    sc["blocks"][k]["settings"]["text"] = html

# The benefits photo stays pinned while its rows scroll past (desktop); a style-only section, hidden itself
S["benefits_css"] = {"type": "custom-liquid", "settings": {"color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0, "custom_liquid":
    "<style>[id$=\"__benefits_css\"]{display:none}"
    "@media (min-width:990px){[id$=\"__benefits\"] .mh__benefits-grid{align-items:start}"
    "[id$=\"__benefits\"] .mh__benefits-media{position:sticky;top:110px;align-self:start}}</style>"}}
T["order"].insert(T["order"].index("benefits") + 1, "benefits_css")

out = os.path.join(HERE, "templates", "index.json")
json.dump(T, open(out, "w"), ensure_ascii=False, indent=2)
print("wrote", out)
