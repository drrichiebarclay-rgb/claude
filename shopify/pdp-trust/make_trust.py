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
    "heading": "Not ready to slow down.",
    "sub": "The next-generation multi-nutrient, built for what your body needs in your 40s and 50s.",
    "note": "Got a wearable? Track the shift over 90 days.",
    "space_top": 100, "space_bottom": 100}}

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
        "text": "<p>Richie Barclay is a cell biologist with a PhD in cellular biology and nutrition, a Harley Street nutritionist for the last 13 years, and a former cricketer.</p>"
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

# --- Page backgrounds: no gradient washes, alternating flat grey and white ---
GREY, WHITE = "#f2f2f2", "#ffffff"
BANDS = [  # section key -> ground, in page order. The buy box keeps the live page's own
           # plain #fafafa, and "compare" keeps its live sage (#c8d2cf) band, so neither is listed.
    ("statement", WHITE),
    ("board", WHITE),
    ("standards", WHITE),
    ("results", GREY),
    ("quotes", WHITE),
    ("founder", GREY),
    ("problem", WHITE),
    ("benefits", GREY),
    ("steps", WHITE),
    ("guarantee", GREY),
    ("faq", GREY),
]

# A line straight after the subhead (which the easy_read script adds; this runs after it).
COLLAB = "In collaboration with seven leading scientists from world-leading research institutions."
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
    (93, "bounce back quicker"),
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
    bar.style.width = '0';
    if (still) { bar.style.width = s[0] + '%%'; return; }
    requestAnimationFrame(function () { requestAnimationFrame(function () { bar.style.width = s[0] + '%%'; }); });
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

# Delivery line: "Ready to ship - arrives by Thu 29th Oct", always the next calendar day in UK time,
# rolling over at midnight while the page is open.
SHIP_JS = """<script>
(function () {
  var el = document.querySelector('.mc .mpb-del');
  if (!el || el.dataset.ship) return;
  el.dataset.ship = '1';
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function ord(n) { var t = n % 100; if (t > 10 && t < 14) return 'th'; return ['th', 'st', 'nd', 'rd'][n % 10] || 'th'; }
  function tomorrowUK() {
    var p = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', year: 'numeric', month: 'numeric', day: 'numeric' })
      .formatToParts(new Date());
    var get = function (t) { return +p.filter(function (x) { return x.type === t; })[0].value; };
    var d = new Date(Date.UTC(get('year'), get('month') - 1, get('day') + 1));
    return DAYS[d.getUTCDay()] + ' ' + d.getUTCDate() + ord(d.getUTCDate()) + ' ' + MONTHS[d.getUTCMonth()];
  }
  var last = '';
  function paint() {
    var t = tomorrowUK();
    if (t === last) return;
    last = t;
    el.innerHTML = '<span class="mc-ship__dot" aria-hidden="true"></span><span>Ready to ship — arrives by <b>' + t + '</b></span>';
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
        "custom_liquid": "\n".join(css), "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}
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
        rules.append(f"{w},{w} > .mc,{w} > .mh{{background:{ground}!important}}")
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
                 'html body .mc .mc-collab{margin:10px 0 0;font-size:15px;line-height:1.4;color:rgba(36,34,35,.72)}'
                 '@media (max-width:989px){html body .mc .mc__buy-copy > .mc-collab{text-align:center}}')
    # Rotating stats under Add to cart (built by STATS_JS)
    rules.append('html body .mc .mc-stats{display:grid;grid-template-columns:minmax(64px,1fr) auto;align-items:center;gap:16px;'
                 'margin:14px 0 0;padding:14px 18px;border:1.5px solid rgba(36,34,35,.12);border-radius:14px;background:#fff}'
                 'html body .mc .mc-stats__bar{position:relative;display:block;height:12px;border-radius:6px;background:#ecebe6;overflow:visible}'
                 'html body .mc .mc-stats__bar i{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:6px;'
                 'background:linear-gradient(90deg,#9fe0ad,#6bce7f);box-shadow:0 0 14px rgba(107,206,127,.55);transition:width .9s cubic-bezier(.2,0,.2,1)}'
                 'html body .mc .mc-stats__text{margin:0;font-size:15px;font-weight:500;line-height:1.25;color:#242223;white-space:nowrap;transition:opacity .35s}'
                 'html body .mc .mc-stats__text b{font-weight:700;color:#2f8a46}'
                 'html body .mc .mc-stats.is-fading .mc-stats__text{opacity:0}'
                 '@media (max-width:420px){html body .mc .mc-stats{gap:12px;padding:12px 14px}html body .mc .mc-stats__text{font-size:14px}}'
                 '@media (prefers-reduced-motion:reduce){html body .mc .mc-stats__bar i,html body .mc .mc-stats__text{transition:none}}')
    # "Ready to ship - arrives by <tomorrow>" line under the button (filled in by SHIP_JS)
    rules.append('html body .mc .mpb-del{align-items:center}'
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
    css = "\n".join(rules)
    return {"type": "custom-liquid", "settings": {
        "custom_liquid": "<style>\n/* Flat, alternating band grounds for this page (no gradient washes). Built by make_trust.py. */\n"
                         + css + "\n</style>" + DRAG_JS + SHIP_JS + STATS_JS + COLLAB_JS,
        "color_scheme": "scheme-1", "padding_top": 0, "padding_bottom": 0}}


# --- Existing sections: a slightly more clinical voice ----------------------
def clinical(d):
    S = d["sections"]

    r = S["results"]["settings"]           # the 9:16 customer videos
    r["heading"] = "Don’t take\nour word for it."
    r["note"] = "MUTO customers, in their own words"
    r["foot"] = "Individual experiences. Everyone is different, and we can’t promise results."
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
        S["results"]["block_order"].append(key)   # sits under the standards band, which brings its own space

    b = S["board"]["settings"]
    b["heading"] = "Six scientists put\ntheir name to MUTO."
    b["note"] = "Our Scientific Advisory Board reviews the formula"
    b["field"] = False        # plain #FAFAFA ground, no mint wash
    b["compact"] = True       # the thin one-row strip: all six across on desktop, small swipeable cards on phones
    b["space_top"] = 60       # sits straight under the statement band

    st = S["steps"]
    st["settings"]["heading"] = "Your first 90 days."
    st["settings"]["heading_right"] = "What to expect."
    # Benefits follow the live timeline (muto-nad-v2) and stay within authorised claims
    # (B vitamins: tiredness and fatigue; vitamin D: normal muscle function).
    steps = [
        ("Day 1", "Set your baseline.",
         "Two capsules with breakfast. Score your energy, sleep and recovery out of 10, or note your wearable’s numbers."),
        ("Day 30", "Afternoons that hold.",
         "Usually the first thing people notice: less of a 3pm slump, energy left for the evening. B vitamins help reduce tiredness and fatigue."),
        ("Day 60", "Bouncing back sooner.",
         "Vitamin D supports normal muscle function. A long walk, a game of tennis or a gym session stops costing you the next day."),
        ("Day 90", "Feel it, or your money back.",
         "Compare your scores with day 1. Not feeling the difference? Email us and we’ll refund what you paid, minus delivery."),
    ]
    for k, (chip, title, text) in zip(st["block_order"], steps):
        st["blocks"][k]["settings"].update({"chip": chip, "title": title, "text": text})

    f = S["faq"]
    for blk in f["blocks"].values():
        s = blk["settings"]
        if s["title"] == "Why not just take one vitamin?":
            s["text"] = ("<p>You can. MUTO puts 19 ingredients, each at a declared dose, into 2 capsules: "
                         "300mg NR plus the B vitamins, TMG, CoQ10 and PQQ that work alongside it. One jar instead of several pots.</p>")
    f["blocks"]["q_tested"] = {"type": "q", "settings": {
        "title": "How is it tested?",
        "text": "<p>Every batch is tested by an independent lab for identity, potency, heavy metals and microbes before it’s released. "
                "MUTO is made in the UK to GMP standards, in an ISO-certified facility.</p>"}}
    f["block_order"].insert(4, "q_tested")
    # "Do I need a smartwatch?" removed
    for k in [k for k, b in f["blocks"].items() if b["settings"].get("title") == "Do I need a smartwatch?"]:
        del f["blocks"][k]
        f["block_order"].remove(k)

    # The three "why" cards say what the founder and standards bands now say in full.
    S["why"]["disabled"] = True


def main():
    raw = open(SNAP).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    assert d["sections"]["faq"]["blocks"][d["sections"]["faq"]["block_order"][0]]["type"] == "q", "check FAQ block type"

    raw2 = open(V2).read()
    v2 = json.loads(raw2[raw2.index("{"):])
    for key in FROM_V2:
        d["sections"][key] = v2["sections"][key]

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

    d["sections"].update({
        "statement": STATEMENT,
        "standards": standards(),
        "quotes": reviews(),
        "founder": FOUNDER,
    })
    clinical(d)
    d["sections"]["custom_reviews_KpXTpD"]["settings"]["bg_color"] = WHITE
    d["sections"]["bands"] = bands_css()

    d["order"] = [
        "buy",
        "statement",        # "Not ready to slow down."
        "board_anchor",     # #scientific-board, linked from the buy box
        "board",            # Scientific Advisory Board, compact row
        "standards",
        "tests",            # #test-results: certificate-of-analysis panel (a dialog, opens from links)
        "results",          # customer videos, 9:16
        "quotes",      # up to 20 rotating written reviews
        "founder",
        "problem", "benefits", "steps", "guarantee", "why", "compare", "faq",
        "custom_reviews_KpXTpD", "sticky", "easy_read", "bands",
    ]
    hoist_styles(d)
    assert sorted(d["order"]) == sorted(d["sections"]), set(d["order"]) ^ set(d["sections"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
