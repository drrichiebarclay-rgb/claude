"""Trust bands + a slightly more clinical voice for the main NAD+ product page
(template product.muto-nad-45).

Built on the LIVE template snapshot (live-snapshot-28oct/), so edits made on live
are kept. Adds four new sections (theme/sections/muto-crea-*.liquid) and changes
copy only in the sections listed below; the buy box is not touched.

Usage (from shopify/pdp-trust/):  python3 make_trust.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "live-snapshot-28oct", "templates__product.muto-nad-45.json")
# The main product moved to template muto-nad-v2 on 27 Oct. Its buy box (section muto-pdp-v2-buy),
# the easy_read block that styles it (incl. the Black Friday box), the sticky bar, the
# #scientific-board anchor and the #test-results certificate panel are taken from it verbatim.
V2 = os.path.join(HERE, "live-snapshot-28oct", "templates__product.muto-nad-v2.json")
FROM_V2 = ["buy", "easy_read", "sticky", "board_anchor", "tests", "compare"]  # compare = "MUTO vs the usual"
OUT = os.path.join(HERE, "theme", "templates", "product.muto-nad-trust.json")
CDN = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/"

# --- New: statement ----------------------------------------------------------
STATEMENT = {"type": "muto-crea-statement", "settings": {
    "label": "",
    "heading": "The best is still ahead.",
    "sub": "Built for your energy, recovery and sleep in your 40s and 50s. Five supplements in one daily jar.",
    "note": "Track it on your wearable for 90 days, or your money back.",
    "space_top": 100, "space_bottom": 100}}

# --- New: problem stats (straight after the statement, before the benefits) ---
PROBLEM_STATS = [  # tag, figure, line, source. Updated 30 Oct.
    ("Energy", "~50%", "drop in your muscles’ energy-making capacity between your 40s and late 60s",
     "Conley et al., Journal of Physiology (2000)"),
    # Moore: older men (~71) needed 0.40 g/kg protein in one meal to max out muscle protein synthesis,
    # young men (~22) 0.24 g/kg, i.e. ~67% more. Proposed for the anabolic-resistance card; swap for
    # Richie's own figure if he has one.
    ("Recovery", "~65%", "more protein per meal needed to switch on muscle repair as you age",
     "Moore et al., Journals of Gerontology Series A (2015)"),
    ("Longevity", "3–8%", "of muscle lost every decade after 30",
     "Volpi et al., Current Opinion in Clinical Nutrition and Metabolic Care (2004)"),
    ("Trust", "57%", "of immune supplements tested didn’t match their label",
     "Crawford et al., JAMA Network Open (2022): 17 of 30 products"),
]


def problem():
    blocks = {"p%d" % (i + 1): {"type": "stat", "settings": {"tag": g, "figure": f, "text": x}}
              for i, (g, f, x, _) in enumerate(PROBLEM_STATS)}
    sources = " ".join("%02d. %s." % (i + 1, s) for i, (_, _, _, s) in enumerate(PROBLEM_STATS))
    return {"type": "muto-crea-stats", "blocks": blocks, "block_order": list(blocks), "settings": {
        "label": "The problem",
        "heading": "Your biology shifts.\nMost supplements don’t.",
        "sources": "<p>" + sources + "</p>",
        "space_top": 70, "space_bottom": 150}}


# --- New: standards ----------------------------------------------------------
STANDARDS_ITEMS = [
    ("tested", "Every batch", "Third-party tested",
     "<p>Every batch is tested by an independent lab for identity, potency, heavy metals and microbes before it’s released.</p>",
     # Set CERTS_URL to the page where the certificates are published.
     "View third-party testing results", "", "Certificates of analysis on request"),
    ("dose", "300mg NR", "Full, declared doses",
     "<p>Nicotinamide riboside at 300mg, the maximum daily amount authorised in Great Britain. All 19 ingredients are on the label with their doses. No proprietary blends.</p>",
     "", "", ""),
    ("board", "6 experts", "Scientific Advisory Board",
     "<p>Doctors and scientists in longevity, metabolism, sleep and performance nutrition review the formula.</p>",
     "", "", ""),
    ("made", "GMP · ISO", "Made in the UK",
     "<p>Manufactured in the UK to GMP standards, in an ISO-certified facility.</p>",
     "", "", ""),
]
CERTS_URL = "#test-results"  # opens the certificate-of-analysis panel (section muto-test-results)

def standards():
    blocks, order = {}, []
    for key, stat, title, text, link_label, link, note in STANDARDS_ITEMS:
        if key == "tested":
            link = CERTS_URL
        blocks[key] = {"type": "standard", "settings": {
            "stat": stat, "title": title, "text": text,
            "link_label": link_label, "link": link, "no_link_note": note}}
        order.append(key)
    return {"type": "muto-crea-standards", "blocks": blocks, "block_order": order, "settings": {
        "heading": "Checked, not\ntaken on trust.",
        "lede": "The four things we hold every jar to",
        "foot": "",
        "space_top": 100, "space_bottom": 100}}

# --- New: rotating reviews ---------------------------------------------------
# Real customer words only, copied from REVIEWS.io. Add up to 20; fill in ages
# (with the customer's OK) and set require_age to True once every card has one.
REVIEWS = [
    # topic (ours), quote (theirs: the whole review or one unbroken passage of it,
    # copied exactly from REVIEWS.io), name, age. All 5-star.
    ("Mid-30s", "Being in my mid 30s, everything has started to slow down. Muto is providing me with a sense of vitality which I haven’t experienced since my mid 20s", "Jonathon R", ""),
    ("Healthy ageing", "bought it to support healthy ageing and have been genuinely surprised at how quickly I felt a difference. My recovery and sleep have noticeably improved.", "K R", ""),
    ("Afternoon energy", "No afternoon slump and in general feeling great", "Lynda", ""),
    ("Feeling like yourself", "I didn't realise how flat I'd been feeling until this helped lift me out of it", "Holly P", ""),
    ("A month in", "I have been using for almost a month and can honestly say I have felt such a difference", "Michelle F", ""),
    ("From a sceptic", "I am usually sceptical to new supplements but this has been highly recommended by my friend so gave it a shot. It has exceeded my expectations, which is not easy as I am well-versed in nutrition and supplements.", "Aleks", ""),
    ("Sustained energy", "I have sustained energy, I sleep better, perform better in workouts, and don’t crash anymore.", "Danny S", ""),
    ("Tracked on Oura", "I track the effectiveness of my supplements using my Oura ring, and all my key biometrics are improving: recovery, sleep, HRV and RHR", "Hugh K", ""),
    ("Mornings", "I predominantly struggle with mornings but already feel myself finding these easier", "Becca", ""),
    ("Recovery", "Has actually changed my recovery", "Adam H", ""),
    ("All-day energy", "The cellular energy boost it gives you really enables me to power through my day.", "Max", ""),
    ("Energy and sleep", "Since starting taking Muto my energy levels and my sleep has improved drastically (even within the first month)", "Matteo M", ""),
    ("Fewer pots", "I love that this replaces multiple products", "Amy C", ""),
    ("Keeping up", "Started using muto because I felt like my body couldn’t keep up with the amount of exercise I wanted to do. After taking muto, I felt more energised and ready for my next session!", "Brendan", ""),
    ("Marathon training", "I started taking Muto for my Boston Marathon training hoping to have better recovery; and it did not disappoint", "Rebeca", ""),
    ("Training more often", "As a keen runner, I’ve noticed how Muto has helped me recover faster meaning I can train harder, more often.", "Ayo P", ""),
    ("Focus", "I’ve been taking MUTO every day for just under 2 months now and definitely feel more focused during the day", "Alexandra", ""),
    ("Consistent energy", "Energy is up and staying consistent.", "Jack", ""),
    ("Clearer mind", "I feel like I have more energy and a clearer mind.", "Sam", ""),
    ("A scientist who picks up the phone", "Richie from the team gave me a call just to chat about my background and goals", "Mathew H", ""),
]

def reviews():
    blocks, order = {}, []
    for i, (topic, quote, name, age) in enumerate(REVIEWS, 1):
        k = f"rv{i}"
        blocks[k] = {"type": "review", "settings": {
            "topic": topic, "quote": quote, "name": name, "age": age, "verified": True}}
        order.append(k)
    return {"type": "muto-crea-reviews", "blocks": blocks, "block_order": order, "settings": {
        "eyebrow": "Verified customers",
        "heading": "What our\ncommunity say.",
        "summary": "4.8 from 103 reviews",  # REVIEWS.io, 28 Oct 2026 (4.83 average): update as it moves
        "interval": 6, "min_age": 30, "require_age": False,
        "foot": "Real reviews from verified customers, in their own words. Everyone is different.",
        "space_top": 100, "space_bottom": 100}}

# --- New: founder ------------------------------------------------------------
FOUNDER = {"type": "muto-crea-founder",
    "blocks": {},
    "block_order": [],
    "settings": {
        "eyebrow": "Our founder",
        "heading": "Built by a doctor\nwho wanted proof.",
        "text": "<p>Richie Barclay is a cell biologist with a PhD in cellular biology and nutrition, a Harley Street nutritionist for the last 13 years, and a former cricketer and tennis player.</p>"
                "<p>He started MUTO after years of watching supplements sell on claims nobody had checked, with the doses hidden in blends. "
                "So MUTO does it the other way: every dose is on the label, every batch goes to an outside lab, "
                "and six doctors and scientists review the formula.</p>",
        "quote": "I built MUTO because I was tired of supplements that ask you to take them on trust.",
        "quote_by": "Dr Richie Barclay, PhD, founder",
        "link_label": "Got a question? Email Richie",
        "link": "mailto:hello@mutolongevity.com",
        "image": "shopify://shop_images/about-founder.jpg",
        "image_fallback": CDN + "about-founder.jpg?v=1790751995",
        "image_alt": "Dr Richie Barclay holding a jar of NAD+ Cellular Complex",
        "image_position": "50% 20%",
        "caption": "",
        "space_top": 100, "space_bottom": 100}}

# --- Page backgrounds: no gradient washes; flat white, with the sage grey used rarely ---
GREY, WHITE = "#c8d2cf", "#ffffff"   # grey = brand sage #C8D2CF
BANDS = [  # section key -> ground, in page order. The buy box and the nav keep the live page's own
           # #fafafa and "compare" keeps its live sage band. Mostly white; grey used rarely (28 Oct).
    ("statement", WHITE),
    ("problem", WHITE),
    ("benefits", WHITE),
    ("board", WHITE),
    ("standards", WHITE),
    ("results", WHITE),
    ("quotes", GREY),
    ("library", WHITE),
    ("founder", WHITE),
    ("timeline", WHITE),
    ("howto", WHITE),
    ("faq", WHITE),
]
REVIEWS_GROUND = WHITE  # the REVIEWS.io widget band (its own colour setting)

# A line straight after the subhead (which the easy_read script adds; this runs after it).
COLLAB = "In collaboration with seven leading scientists from world-leading research institutions, including four universities in the UK and Australia."
COLLAB_JS = """<script>
(function () {
  var sub = document.querySelector('.mc .mc-subhead');
  if (!sub || document.querySelector('.mc-collab')) return;
  var p = document.createElement('p');
  p.className = 'mc-collab';
  p.textContent = %s;
  sub.insertAdjacentElement('afterend', p);
})();
</script>""" % json.dumps(COLLAB, ensure_ascii=False)

# Rotating stats under Add to cart. Placed right after the button, inside the same wrapper, so the
# buy column's ordering keeps it directly under the button.
STATS = [
    (94, "reported better recovery"),
    (92, "reported improved energy"),
    (88, "bounce back quicker"),
]
STATS_JS = """<script>
(function () {
  var STATS = %s;
  var btn = document.querySelector('.mc .mc__buy-cta');
  if (!btn || document.querySelector('.mc-stats')) return;
  var box = document.createElement('div');
  box.className = 'mc-stats';
  box.innerHTML = '<span class="mc-stats__bar" aria-hidden="true"><i></i></span><p class="mc-stats__text" aria-live="polite"></p>';
  btn.insertAdjacentElement('afterend', box);
  var bar = box.querySelector('i'), text = box.querySelector('.mc-stats__text');
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var n = 0;
  function show(i) {
    var s = STATS[i];
    text.innerHTML = '<b>' + s[0] + '%%</b> ' + s[1];
    /* Snap back to empty with no transition, then fill left to right */
    bar.style.transition = 'none';
    bar.style.width = '0';
    void bar.offsetWidth;
    bar.style.transition = '';
    if (still) { bar.style.width = s[0] + '%%'; return; }
    requestAnimationFrame(function () { bar.style.width = s[0] + '%%'; });
  }
  show(0);
  setInterval(function () {
    if (document.hidden) return;
    n = (n + 1) %% STATS.length;
    if (still) { show(n); return; }
    box.classList.add('is-fading');
    setTimeout(function () { show(n); box.classList.remove('is-fading'); }, 350);
  }, 3500);
})();
</script>""" % json.dumps(STATS)

# Delivery line: "Ready to ship - arrives by Thu 29th Oct": the next calendar day in UK time, or the day after
# from the 9pm cut-off, updating while the page is open.
SHIP_JS = """<script>
(function () {
  var el = document.querySelector('.mc .mpb-del');
  if (!el || el.dataset.ship) return;
  el.dataset.ship = '1';
  /* Royal Mail logo (theme/assets/royal-mail-logo.png), inline so it needs no upload */
  var RM_LOGO = 'data:image/png;base64,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';
  var CUTOFF = 21;
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function ord(n) { var t = n % 100; if (t > 10 && t < 14) return 'th'; return ['th', 'st', 'nd', 'rd'][n % 10] || 'th'; }
  function tomorrowUK() {
    var p = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', year: 'numeric', month: 'numeric', day: 'numeric',
      hour: 'numeric', hourCycle: 'h23' }).formatToParts(new Date());
    var get = function (t) { return +p.filter(function (x) { return x.type === t; })[0].value; };
    /* Next-day cut-off is 9pm UK time: from 21:00 it arrives the day after tomorrow */
    var days = get('hour') >= CUTOFF ? 2 : 1;
    var d = new Date(Date.UTC(get('year'), get('month') - 1, get('day') + days));
    return DAYS[d.getUTCDay()] + ' ' + d.getUTCDate() + ord(d.getUTCDate()) + ' ' + MONTHS[d.getUTCMonth()];
  }
  var last = '';
  function paint() {
    var t = tomorrowUK();
    if (t === last) return;
    last = t;
    el.innerHTML = '<span class="mc-ship__dot" aria-hidden="true"></span><span>Ready to ship — arrives by <b>' + t + '</b></span>' +
      '<span class="mc-ship__rm"><img src="' + RM_LOGO + '" alt="Royal Mail" width="32" height="22">Tracked 24hr delivery</span>';
  }
  paint();
  setInterval(paint, 60000);
})();
</script>"""

# Mouse drag-to-scroll for the customer-video row on desktop (touch and trackpads scroll natively).
DRAG_JS = """<script>
(function () {
  var rail = document.querySelector('[id$="__results"] .mh__res-rail');
  if (!rail || rail.dataset.drag) return;
  rail.dataset.drag = '1';
  var down = false, moved = false, x0 = 0, s0 = 0;
  rail.addEventListener('mousedown', function (e) { down = true; moved = false; x0 = e.pageX; s0 = rail.scrollLeft; });
  window.addEventListener('mousemove', function (e) {
    if (!down) return;
    var dx = e.pageX - x0;
    if (Math.abs(dx) > 4) { moved = true; rail.classList.add('is-dragging'); }
    if (moved) { e.preventDefault(); rail.scrollLeft = s0 - dx; }
  });
  window.addEventListener('mouseup', function () { down = false; rail.classList.remove('is-dragging'); });
  /* A drag must not also count as a click on a video's play button */
  rail.addEventListener('click', function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
})();
</script>"""


def rerunnable(js):
    """Wrap an injector so it runs again whenever Shopify re-draws a section. The theme editor
    replaces the buy box's markup each time it is selected or edited, which wiped the delivery
    line, the stats and the collaboration line; each injector is guarded, so re-running is safe."""
    head, tail = "<script>\n(function () {", "})();\n</script>"
    assert js.startswith(head) and js.endswith(tail), js[:40]
    body = js[len(head):-len(tail)]
    return (head + "\n  function run() {" + body + "  }\n  run();\n"
            "  document.addEventListener('shopify:section:load', function () { setTimeout(run, 60); });\n"
            + tail)


def hoist_styles(d, keys=("easy_read", "bands")):
    """Move the <style> of the page's Custom Liquid blocks into one block at the top of the page.

    easy_read restyles the buy box and sits at the end of the template, so the browser painted the
    buy box with the section's own defaults first and restyled it once it reached the bottom: the old
    design flashed on load. Styles now arrive before the buy box; the scripts stay at the end, because
    they work on elements that have to exist first."""
    css = []
    for key in keys:
        st = d["sections"][key]["settings"]
        t = st["custom_liquid"]
        i, j = t.index("<style>"), t.index("</style>") + len("</style>")
        css.append(t[i:j])
        st["custom_liquid"] = t[:i] + t[j:]
    d["sections"]["head_styles"] = {"type": "custom-liquid", "settings": {
        "custom_liquid": FONT_PRELOAD + "\n" + "\n".join(css), "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}
    d["order"].insert(0, "head_styles")


def strip_presale(t):
    i = t.index("/* Black Friday pre-sale box, above the plans */")
    j = t.index("/* -2 page only:", i)
    t = t[:i] + t[j:]
    i = t.index("/* Black Friday pre-sale: real countdown")
    end = "if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();\n})();\n"
    j = t.index(end, i) + len(end)
    t = t[:i] + t[j:]
    t = t.replace('<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"></div>', "")
    assert "MUTO10" not in t and "pre-sale" not in t.lower() and "mc-bf-data" not in t
    return t


def bands_css():
    """A template-only style block. Each section is matched by the end of its
    Shopify wrapper id (shopify-section-template--…__<key>), so it reaches only
    this page and only these sections. !important because the washes are set on
    the bands' own root classes in muto-crea.css / muto-home.css."""
    rules = []
    for key, ground in BANDS:
        w = f'[id$="__{key}"]'
        rules.append(f"{w},{w} > .mc,{w} > .mh,{w} > .mil{{background:{ground}!important}}")
        # Masks that use the page ground (e.g. the timeline dots) follow the band
        rules.append(f"{w}{{--mc-ground:{ground}}}{w} .mc{{--mc-ground:{ground}}}")
        if ground == GREY:
            # On the sage band the sage glass cards (reviews) turn white so they don't vanish into it
            rules.append(f"{w} .mc{{--mt-sage:rgba(255,255,255,.6)}}")
    # Small line above "Benefits built on published science." in caps, like the other bands' labels
    rules.append('[id$="__benefits"] .mbc__eyebrow{text-transform:uppercase!important;letter-spacing:.12em!important;line-height:1.2!important;margin-bottom:-8px!important}')  # grid row gap 24 - 8 = 16px to the heading, as the problem band
    # Subhead under the title: fill each line before breaking (the live rule balances it into two short
    # lines), medium weight.
    rules.append('html body .mc .mc-subhead,html body .mc .mc__buy-copy > .mc-subhead{text-wrap:wrap!important;font-weight:500!important}')
    # Buy button (and the sticky bar's) in brand green #6bce7f, charcoal label
    rules.append('html body .mc .mc__buy-cta,html body .mh__sticky .mh__sticky-btn{background:#6bce7f!important;color:#242223!important}')
    # Add to cart: a second line inside the button, shield + "90-day money-back guarantee"
    rules.append('html body .mc .mc__buy-cta{height:auto!important;min-height:68px;padding-top:12px!important;padding-bottom:12px!important;'
                 'flex-direction:column;align-items:center;justify-content:center;text-align:center}'
                 'html body .mc .mc__buy-cta .btn-label-wrapper{padding-bottom:0}'
                 'html body .mc .mc__buy-cta::after{content:"90-day money-back guarantee";display:block;width:fit-content;margin:5px auto 0;'
                 'padding-left:22px;font-size:14px;font-weight:500;line-height:18px;letter-spacing:0;'
                 """background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23242223' stroke-width='1.8' stroke-linejoin='round' stroke-linecap='round'%3E%3Cpath d='M12 2.8 4.5 5.8v5.6c0 4.9 3.2 8.6 7.5 10 4.3-1.4 7.5-5.1 7.5-10V5.8z'/%3E%3Cpath d='m8.6 12 2.4 2.4 4.4-4.8'/%3E%3C/svg%3E") left center/16px 16px no-repeat}""")
    # Line under the subhead (added by COLLAB_JS): ordered with the title group, centred on phones like it
    rules.append('html body .mc .mc__buy-copy > .mc-collab{order:0}'
                 'html body .mc .mc-collab{margin:12px 0 0;font-size:17px;font-weight:400;line-height:1.4;color:#242223}'
                 '@media (max-width:989px){html body .mc .mc__buy-copy > .mc-collab{text-align:center}}')
    # Rotating stats under Add to cart (built by STATS_JS)
    rules.append('html body .mc .mc-stats{display:grid;grid-template-columns:minmax(64px,1fr) auto;align-items:center;gap:16px;'
                 'margin:14px 0 0;padding:14px 18px;border:1.5px solid rgba(36,34,35,.12);border-radius:14px;background:#fff}'
                 'html body .mc .mc-stats__bar{position:relative;display:block;height:12px;border-radius:6px;background:#ecebe6;overflow:visible}'
                 'html body .mc .mc-stats__bar i{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:6px;'
                 'background:#242223;transition:width .9s cubic-bezier(.2,0,.2,1)}'
                 'html body .mc .mc-stats__text{margin:0;font-size:15px;font-weight:500;line-height:1.25;color:#242223;white-space:nowrap;transition:opacity .35s}'
                 'html body .mc .mc-stats__text b{font-weight:700;color:#242223}'
                 'html body .mc .mc-stats.is-fading .mc-stats__text{opacity:0}'
                 '@media (max-width:420px){html body .mc .mc-stats{gap:12px;padding:12px 14px}html body .mc .mc-stats__text{font-size:14px}}'
                 '@media (prefers-reduced-motion:reduce){html body .mc .mc-stats__bar i,html body .mc .mc-stats__text{transition:none}}')
    # Plan cards: the billing line under each plan name much smaller on phones, so it fits
    rules.append('@media (max-width:749px){html body .mc .mc__plan-note{font-size:12px!important;line-height:1.35}}')
    # "How it helps" list in the buy box: hidden on phones too (desktop already hides it)
    rules.append('html body .mc .mc__buy-points{display:none!important}')
    # "Ready to ship - arrives by <tomorrow>" line under the button (filled in by SHIP_JS)
    rules.append('html body .mc .mpb-del{align-items:center;flex-wrap:wrap;row-gap:6px}'
                 'html body .mc .mpb-del .mc-ship__rm{display:inline-flex;align-items:center;gap:7px;margin-left:4px;padding-left:12px;border-left:1px solid rgba(36,34,35,.18);white-space:nowrap}'
                 'html body .mc .mpb-del .mc-ship__rm img{display:block;width:32px;height:auto}'
                 '@media (max-width:520px){html body .mc .mpb-del .mc-ship__rm{flex-basis:100%;justify-content:center;margin-left:0;padding-left:0;border-left:0}}'
                 '@media (max-width:749px){html body .mc .mpb-del{justify-content:center;text-align:center}}'
                 'html body .mc .mpb-del .mc-ship__dot{flex:0 0 10px;width:10px;height:10px;border-radius:50%;background:#6bce7f;'
                 'box-shadow:0 0 0 0 rgba(107,206,127,.6);animation:mcShip 2s ease-out infinite}'
                 '@keyframes mcShip{70%{box-shadow:0 0 0 7px rgba(107,206,127,0)}100%{box-shadow:0 0 0 0 rgba(107,206,127,0)}}'
                 'html body .mc .mpb-del b{font-weight:600;text-decoration:underline;text-decoration-color:#6bce7f;'
                 'text-decoration-thickness:2px;text-underline-offset:3px}'
                 '@media (prefers-reduced-motion:reduce){html body .mc .mpb-del .mc-ship__dot{animation:none}}')
    # Customer videos: a scrolling row on desktop too (the section's own desktop layout is a fixed
    # 6-across grid that wraps a 7th card). ~5.5 cards show so the cut-off one says "scroll".
    rules.append('@media screen and (min-width:990px){[id$="__results"] .mh__res-rail{display:flex!important;'
                 'overflow-x:auto!important;scroll-snap-type:x proximity;scrollbar-width:thin;padding-bottom:12px!important;cursor:grab}'
                 '[id$="__results"] .mh__res-rail::-webkit-scrollbar{display:block;height:6px}'
                 '[id$="__results"] .mh__res-rail::-webkit-scrollbar-thumb{background:rgba(36,34,35,.3);border-radius:3px}'
                 '[id$="__results"] .mh__res-card{flex:0 0 calc((100% - 60px)/5.5)!important;scroll-snap-align:start}'
                 '[id$="__results"] .mh__res-rail.is-dragging{cursor:grabbing;scroll-snap-type:none;user-select:none}}')
    # Phones: one smaller, tighter scale for the live sections too, matching the new bands
    # (muto-crea-trust.css). Headings 28px, ledes 15px, body 14px, card titles 17-20px, smaller cards.
    rules.append('@media screen and (max-width:749px){'
                 'html body .mc__h2,html body .mh__h2,html body .mch__h{font-size:28px!important;line-height:.95!important}'
                 'html body .mc .mc__stm-head{font-size:32px!important}'
                 'html body .mbc__lede,html body .mtl__lede,html body .mil__lede,html body .mh__lede,html body .mch__intro{font-size:15px!important;line-height:1.4!important}'
                 'html body .mbc__eyebrow,html body .mtl__eyebrow,html body .mil__eyebrow,html body .mh__board-note,html body .mh__res-note,html body .mh__mono{font-size:11px!important}'
                 # benefit cards: narrower, shorter, smaller type on the glass panel
                 'html body .mbc__card{flex-basis:66%!important;aspect-ratio:4/5!important}'
                 'html body .mbc__panel{padding:16px 18px 18px!important}'
                 'html body .mbc__t{font-size:20px!important}html body .mbc__x{font-size:13.5px!important;line-height:1.35!important}'
                 'html body .mbc__btn{height:46px!important;padding:0 20px!important;font-size:14px!important}'
                 'html body .mbc__arrow{width:46px!important;height:46px!important}'
                 # ingredient library
                 'html body .mil__filter{padding:10px 16px!important;font-size:14px!important}'
                 'html body .mil__name{font-size:17px!important}html body .mil__dose{font-size:13px!important}'
                 'html body .mil__cat-text{font-size:20px!important}html body .mil__cat-btn{min-height:46px!important;font-size:15px!important}'
                 'html body .mil__tag{font-size:10px!important;padding:7px 9px!important}'
                 # timeline
                 'html body .mtl__t{font-size:18px!important}html body .mtl__x{font-size:14px!important;line-height:1.4!important}'
                 'html body .mtl__pill{height:28px!important;font-size:11.5px!important}'
                 # comparison and how to take it (muto-chapter)
                 'html body .mch__bt{font-size:18px!important}html body .mch__bx{font-size:14.5px!important}'
                 'html body .mch__q{font-size:18px!important}html body .mch__table-h{font-size:18px!important}'
                 'html body .mch__t{font-size:13.5px!important}html body .mch th{font-size:13px!important}'
                 # board and videos (muto-home)
                 'html body .mh__member-name{font-size:16px!important}html body .mh__member-role{font-size:12px!important}'
                 'html body .mh__res-name{font-size:15px!important}'
                 # FAQs, section menu
                 'html body .mc__faq{padding-top:40px!important;padding-bottom:40px!important}'
                 'html body .mc__faq-list{margin-top:20px!important}html body .mc__faq-body{font-size:14.5px!important}'
                 'html body .msn__nav ol a{font-size:13px!important}'
                 '}')
    css = "\n".join(rules)
    return {"type": "custom-liquid", "settings": {
        "custom_liquid": "<style>\n/* Flat, alternating band grounds for this page (no gradient washes). Built by make_trust.py. */\n"
                         + css + "\n</style>" + "".join(rerunnable(j) for j in (DRAG_JS, SHIP_JS, STATS_JS, COLLAB_JS)),
        "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}


# --- Existing sections: a slightly more clinical voice ----------------------
def clinical(d):
    S = d["sections"]

    S["compare"]["settings"]["heading"] = "See the difference\nfor yourself."
    S["howto"]["settings"]["band"] = "ground"   # white band (bands_css), not the live sage
    S["library"]["settings"]["bg"] = "#ffffff"
    b = S["benefits"]["settings"]          # the live "Five jobs" cards, reframed for 40s and 50s
    b["eyebrow"] = "Five jobs. One daily jar."
    b["heading"] = "Benefits built on\npublished science."
    b["lede"] = "What you need after 35. Your biology shifts. What you need evolves."

    r = S["results"]["settings"]           # the 9:16 customer videos
    r["heading"] = "Don’t take\nour word for it."
    r["note"] = "MUTO customers, in their own words"
    r["foot"] = ""   # footnote under the videos removed (28 Oct)
    S["results"]["settings"]["space_top"] = 70
    # Ellen Gray's video is removed.
    S["results"]["blocks"].pop("r4", None)
    S["results"]["block_order"].remove("r4")
    # Three more customer videos (Richie's Google Drive). Kate's is already in Shopify Files; David's and
    # "testimonial.mp4" have to be uploaded in Content -> Files first. Until then their tiles keep the
    # placeholder video named below. Set the file name (as Shopify shows it) to switch a tile over.
    PREVIEW = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/preview_images/"
    NEW_VIDEOS = [
        # key, name, video file in Shopify, cover (fallback URL; Shopify's own thumbnail of the video)
        ("r7", "Kate Bright", "kate v4.mp4", PREVIEW + "ae14f3b1ff0f4ef09ae55be1fd8cfadd.thumbnail.0000000000.jpg?v=1773314771", ""),
        ("r8", "David Mercado", "✅Copy of David Chat.mp4", PREVIEW + "cd1132a29bdc4f5081bfd9e6b008339b.thumbnail.0000000000.jpg?v=1793207168", ""),
        # Lucy: the Drive file is "testimonial.mp4"; "Lucy Short.mp4" (already in Files, Dec 2025) is used meanwhile
        ("r9", "Lucy Halliday", "Lucy Short.mp4", PREVIEW + "3dcc774e01284c63ab3f6eaf40bc5fb7.thumbnail.0000000000.jpg?v=1766048998", ""),
    ]
    PLACEHOLDER = {"r8": "Muto 1.mp4", "r9": "Muto 2.mp4"}
    for key, name, video, fallback, cover in NEW_VIDEOS:
        if video is None:
            video, name = PLACEHOLDER[key], ""
        S["results"]["blocks"][key] = {"type": "result", "settings": {
            "image": cover, "image_fallback": fallback, "image_alt": "A MUTO customer talking to camera",
            "image_position": "", "video": "shopify://files/videos/" + video, "video_url": "", "video_link": "",
            "show_play": True, "result": "", "quote": "", "name": name, "tag": "", "detail": ""}}
        S["results"]["block_order"].append(key)
    # Kate, David and Lucy lead the row
    lead = ["r7", "r8", "r9"]
    S["results"]["block_order"] = lead + [k for k in S["results"]["block_order"] if k not in lead]
    # Yolanda King ends it
    S["results"]["block_order"].remove("r2")
    S["results"]["block_order"].append("r2")   # sits under the standards band, which brings its own space

    b = S["board"]["settings"]
    b["heading"] = "Six scientists put\ntheir name to MUTO."
    b["note"] = "Our Scientific Advisory Board reviews the formula"
    b["field"] = False        # plain #FAFAFA ground, no mint wash
    b["compact"] = True       # the thin one-row strip: all six across on desktop, small swipeable cards on phones
    b["space_top"] = 60       # sits straight under the statement band

    # The timeline, FAQ and comparison are the live page's own and stay exactly as they are.

# --- Travel vial: a first-order gift on the 3-month (quarterly) plan only -------------------------
# The cart adds it from the theme setting cart_free_product_3m (product muto-travel-vial-free, £0 with a
# £10 compare-at, so the cart's gift list strikes through £10). Here it is the kit tile and the
# itemised row, scoped to the quarterly card (plan 2), and the quarterly kit is now worth £87.
VIAL_IMAGE = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-travel-vial.jpg?v=1793355262"
KIT_Q_OLD, KIT_Q_NEW = "£77", "£87"


def travel_vial(buy):
    buy["blocks"]["qk_vial"] = {"type": "gift", "settings": {
        "value": "£10", "name": "Travel vial", "row_label": "Travel vial", "row_note": "",
        "image": "shopify://shop_images/gift-travel-vial.jpg", "image_fallback": VIAL_IMAGE,
        "image_alt": "The MUTO travel vial, a frosted glass tube of capsules with a silver cap", "plans": "2"}}
    order = buy["block_order"]
    first_gift = next(i for i, k in enumerate(order) if buy["blocks"][k]["type"] == "gift")
    order.insert(first_gift, "qk_vial")
    q = next(b for b in buy["blocks"].values()
             if b["type"] == "plan" and b["settings"].get("name") == "Quarterly plan")
    assert KIT_Q_OLD in q["settings"]["detail"]
    q["settings"]["detail"] = q["settings"]["detail"].replace(KIT_Q_OLD, KIT_Q_NEW)
    assert KIT_Q_OLD in buy["settings"]["plans_banner"]
    buy["settings"]["plans_banner"] = buy["settings"]["plans_banner"].replace(KIT_Q_OLD, KIT_Q_NEW)


# --- No jumping on load ----------------------------------------------------------------------------
# Everything the page adds to the buy box used to run from the bottom of the page, so a phone painted
# the buy box first and then shifted it: the plan flipped from Monthly to Quarterly after the whole page
# had loaded, and the subhead, the testing button, the collaboration line, the stats and the delivery
# line popped in. They now run from a block straight after the buy box, before the first paint. The
# copies at the bottom stay as a safety net and do nothing once these have run (each is guarded).
PRESELECT_JS = """<script>
/* Open on the Quarterly plan (the second card) before first paint: the same switch muto-home.js makes
   on a click, so its own start-up then announces Quarterly and nothing changes on screen. */
(function () {
  var cards = [].slice.call(document.querySelectorAll('.mc__plans > label.mc__plan'));
  var q = cards[1];
  if (!q || q.classList.contains('is-selected') || q.classList.contains('is-unavailable')) return;
  var qi = q.querySelector('.mc__plan-input');
  if (qi && qi.disabled) return;
  cards.forEach(function (c) {
    var on = c === q;
    c.classList.toggle('is-selected', on);
    var r = c.querySelector('input[type="radio"]');
    if (r && !r.disabled) r.checked = on;
  });
  var idx = q.getAttribute('data-index');
  [].forEach.call(document.querySelectorAll('[data-mc-plan-for]'), function (el) {
    var list = (el.getAttribute('data-mc-plan-for') || '').split(/\\s+/);
    el.classList.toggle('is-plan-off', list.indexOf(idx) === -1);
  });
  var price = q.getAttribute('data-price-full') || q.getAttribute('data-price') || '';
  if (price) [].forEach.call(document.querySelectorAll('[data-mh-cta-price]'), function (s) { s.textContent = price; });
  var v = q.getAttribute('data-variant');
  if (v) {
    var plan = q.getAttribute('data-plan') || '';
    [].forEach.call(document.querySelectorAll('[data-mh-cart-id]'), function (f) { f.value = v; });
    [].forEach.call(document.querySelectorAll('[data-mh-cart-plan]'), function (f) { f.value = plan; f.disabled = !plan; });
  }
})();
</script>"""


def early_scripts(d):
    er = d["sections"]["easy_read"]["settings"]["custom_liquid"]
    i = er.index("/* Subhead under the title")
    j = er.index("})();", i) + len("})();")
    sub = er[i:j]
    # The testing button waited for the test-results panel (at the bottom) to exist; it only needs the
    # panel when clicked, so it goes in now with everything else.
    old = " && document.querySelector('[data-mtr]')"
    assert old in sub
    sub = sub.replace(old, "")
    html = (PRESELECT_JS + "\n<script>\n" + sub + "\n</script>\n" + COLLAB_JS + "\n" + STATS_JS + "\n" + SHIP_JS)
    d["sections"]["early"] = {"type": "custom-liquid", "settings": {
        "custom_liquid": html, "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}
    d["order"].insert(d["order"].index("buy") + 1, "early")


# --- Page speed ------------------------------------------------------------------------------------
# The REVIEWS.io widget at the foot of the page loaded its script the blocking way, mid-page: the
# browser stopped building the page until it had downloaded and run, and the page's load event waited
# on it. It now loads when the reader comes within ~1200px of it, or when the browser is idle after
# the page has loaded (so it is always there for search engines and the rich snippets), or on a click
# on a link to it. The widget's own settings are untouched.
REVIEWS_SRC = '<script src="https://widget.reviews.io/polaris/build.js"></script>'
REVIEWS_LOADER = """
(function () {
  var el = document.getElementById('ReviewsWidget'), started = false;
  function go() {
    if (started) return;
    started = true;
    var s = document.createElement('script');
    s.src = 'https://widget.reviews.io/polaris/build.js';
    s.async = true;
    s.onload = function () { window.__mutoReviews(); };
    document.head.appendChild(s);
  }
  if (el && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries, obs) {
      if (entries[0].isIntersecting) { obs.disconnect(); go(); }
    }, { rootMargin: '1200px 0px' }).observe(el);
  } else {
    go();
  }
  window.addEventListener('load', function () {
    (window.requestIdleCallback || function (f) { setTimeout(f, 2500); })(go, { timeout: 4000 });
  });
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('a[href*="ReviewsWidget"], a[href*="#reviews"], [data-reviews-jump]')) go();
  }, true);
})();
"""


def lazy_reviews(st):
    c = st["review_content"]
    assert c.count(REVIEWS_SRC) == 1 and c.count("new ReviewsWidget(") == 1
    c = c.replace(REVIEWS_SRC, "")
    c = c.replace("new ReviewsWidget(", "window.__mutoReviews = function () {\nnew ReviewsWidget(")
    end = c.rindex("</script>")
    c = c[:end].rstrip() + "\n};\n" + REVIEWS_LOADER + "</script>" + c[end + len("</script>"):]
    st["review_content"] = c


# The two weights the buy box opens with, fetched straight away rather than once muto-crea.css arrives
FONT_PRELOAD = "".join(
    '<link rel="preload" as="font" type="font/woff2" crossorigin href="%s">' % u for u in (
        "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/NeueHaasDisplay-Roman.woff2?v=1788216240",
        "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/NeueHaasDisplay-Mediu.woff2?v=1788216243"))


def nav_links(d):
    """'On this page' menu: the live links plus the new bands, in page order (targets are section keys)."""
    nav = d["sections"]["nav"]
    links = {b["settings"]["target"]: b["settings"]["label"] for b in nav["blocks"].values()}
    links.update({"problem": "Problem", "standards": "Standards", "results": "What people say", "founder": "Founder"})
    order = [k for k in d["order"] if k in links]
    assert len(order) == len(links), set(links) - set(order)
    nav["blocks"] = {"n%d" % (i + 1): {"type": "link", "settings": {"label": links[k], "target": k}}
                     for i, k in enumerate(order)}
    nav["block_order"] = list(nav["blocks"])


def main():
    # Base: the LIVE main page (muto-nad-v2) exactly as it is, so its own sections stay: the
    # "On this page" nav, "Five jobs. One daily jar.", the ingredient library, the comparison,
    # the timeline, "How to take it", the FAQs, reviews and the test-results panel.
    raw = open(V2).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    # The 9:16 customer videos come from the earlier main page (muto-nad-45 snapshot).
    raw45 = open(SNAP).read()
    old = json.loads(raw45[raw45.index("{"):])
    d["sections"]["results"] = old["sections"]["results"]

    # The Black Friday pre-sale box (and its automatic MUTO10 code) is removed: MUTO10 was ended
    # on 28 Oct. Its styles, its script and its data div all come out of easy_read.
    er = d["sections"]["easy_read"]["settings"]
    er["custom_liquid"] = strip_presale(er["custom_liquid"])

    # Under the buy button: drop the serving line, the "Not another multivitamin" copy and the
    # review-quote slider (the rotating reviews band further down does that job). Blanked and
    # hidden, not deleted, so they can be switched back in the theme editor.
    buy = d["sections"]["buy"]
    # Delivery line: "Ready to ship - arrives by <next calendar day>", the date filled in by SHIP_JS.
    # "tomorrow" is what shows before the script runs.
    buy["blocks"]["x_delivery"]["settings"]["text"] = "Ready to ship — arrives <strong>tomorrow</strong>"
    buy["settings"]["serving"] = ""
    buy["settings"]["text"] = ""
    for k, blk in buy["blocks"].items():
        if blk["type"] == "snippet":
            blk["disabled"] = True
    travel_vial(buy)

    d["sections"].update({
        "statement": STATEMENT,
        "problem": problem(),
        "standards": standards(),
        "quotes": reviews(),
        "founder": FOUNDER,
    })
    clinical(d)
    d["sections"]["reviews"]["settings"]["bg_color"] = REVIEWS_GROUND
    lazy_reviews(d["sections"]["reviews"]["settings"])
    d["sections"]["bands"] = bands_css()

    # Page order follows the nav (Benefits, The experts, Ingredients, Comparison, What to expect,
    # How to take it, FAQs, Reviews), with the new bands slotted in.
    d["order"] = [
        "buy",
        "nav",              # "On this page" (live)
        "statement",        # "Not ready to slow down."
        "problem",          # four problem stats, with sources
        "benefits",         # "Five jobs. One daily jar." (live)
        "board_anchor",     # #scientific-board, linked from the buy box
        "board",            # "Six scientists put their name to MUTO.", compact row
        "standards",        # "Checked, not taken on trust."
        "results",          # customer videos, 9:16 (above the ingredients, 28 Oct)
        "quotes",           # 20 rotating written reviews
        "library",          # "Every ingredient has a job." (live)
        "founder",
        "compare",          # "MUTO vs the usual" (live)
        "timeline",         # "What you can expect over time." (live)
        "howto",            # "How to take it." (live)
        "faq",              # live, 10 questions
        "reviews",          # REVIEWS.io widget (live)
        "tests",            # #test-results: certificate-of-analysis panel (a dialog, opens from links)
        "easy_read", "bands",
    ]
    # No sticky add-to-cart bar on this page (removed 28 Oct)
    d["sections"].pop("sticky", None)
    nav_links(d)
    hoist_styles(d)
    early_scripts(d)
    assert sorted(d["order"]) == sorted(d["sections"]), set(d["order"]) ^ set(d["sections"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
