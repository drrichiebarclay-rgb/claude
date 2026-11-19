"""MUTO main PDP: CRO fixes of 19 November 2026 (brief: "MUTO PDP fixes").

Reads the live theme's files from live/ (fetched 19 Nov 2026) and writes the changed files to theme/.
Every edit is an exact find-and-replace that must match the expected number of times, so if the live
file has moved on, the script stops instead of guessing. Run: python3 apply.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CHANGED = {}


def edit(path, pairs):
    src = open(os.path.join(HERE, "live", path), encoding="utf-8", newline="").read()
    crlf = "\r\n" in src
    text = src.replace("\r\n", "\n")
    for old, new, *count in pairs:
        want = count[0] if count else 1
        got = text.count(old)
        if got != want:
            raise SystemExit(f"{path}: expected {want} of {old[:70]!r}, found {got}")
        text = text.replace(old, new)
    if crlf:
        text = text.replace("\n", "\r\n")
    out = os.path.join(HERE, "theme", path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8", newline="").write(text)
    CHANGED[path] = len(pairs)


def new(path, text):
    out = os.path.join(HERE, "theme", path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8", newline="").write(text)
    CHANGED[path] = "new"


shutil.rmtree(os.path.join(HERE, "theme"), ignore_errors=True)

KIT3 = "{% render 'muto-offer', key: 'kit3' %}"
KIT1 = "{% render 'muto-offer', key: 'kit1' %}"
CTA = "{% render 'muto-offer', key: 'cta' %}"

# ---------------------------------------------------------------- one place for the offer's words and numbers
new("snippets/muto-offer.liquid", """{%- comment -%}
  MUTO — offer values (muto-offer). ONE place for the numbers and the button label that used to be typed
  into many files. Change a value here and every bar, card, tile, menu card and script that shows it changes.

    {%- render 'muto-offer', key: 'kit3' -%}   what the 3-Month Supply's welcome kit is worth
    {%- render 'muto-offer', key: 'kit1' -%}   what the 1-Month Supply's welcome kit is worth
    {%- render 'muto-offer', key: 'cta' -%}    the one button label
    {%- render 'muto-offer', key: 'vars' -%}   the same values for stylesheets and scripts: CSS variables
                                               (--muto-kit3, --muto-kit1) and window.MUTO_OFFER

  The 3-Month kit is creatine £30, socks £12, travel vial £10, Forever Jar £10 and the 12-week guide £10: £72.
  The Performance Bottle (£15) comes with box 2, so it is not in this figure. The 1-Month kit has no vial: £62.
{%- endcomment -%}
{%- liquid
  assign mo_kit3 = '£72'
  assign mo_kit1 = '£62'
  assign mo_cta = 'Start your 90-day test'
  case key
    when 'kit3'
      echo mo_kit3
    when 'kit1'
      echo mo_kit1
    when 'cta'
      echo mo_cta
  endcase
-%}
{%- if key == 'vars' -%}
  <style>:root{--muto-kit3:"{{ mo_kit3 }}";--muto-kit1:"{{ mo_kit1 }}"}</style>
  <script>window.MUTO_OFFER = { kit3: {{ mo_kit3 | json }}, kit1: {{ mo_kit1 | json }}, cta: {{ mo_cta | json }} };</script>
{%- endif -%}
""")

# ---------------------------------------------------------------- one place for the star-rating line
new("snippets/muto-rating.liquid", """{%- comment -%}
  MUTO — rating line (muto-rating). Prints "4.8 from 106 reviews" from the numbers REVIEWS.io saves on the
  product (metafields reviews.rating and reviews.rating_count), so the line under the stars is never typed.
  `fallback` is printed if the product has no numbers yet.

    <span data-muto-rating>{%- render 'muto-rating', fallback: '4.8 from 103 reviews' -%}</span>

  The data-muto-rating attribute lets the page bring the line into step with the reviews widget once the
  widget has loaded (script in sections/muto-bf-style.liquid): the widget counts reviews of every product in
  its list, so it can be one or two ahead of this product's own count.
{%- endcomment -%}
{%- liquid
  assign mr_product = product
  if mr_product == blank
    assign mr_product = all_products['muto-nad-cellular-complex']
  endif
  assign mr_rating = mr_product.metafields.reviews.rating.value
  assign mr_count = mr_product.metafields.reviews.rating_count.value
  if mr_rating != blank and mr_count != blank and mr_count > 0
    assign mr_score = mr_rating.rating | default: mr_rating | times: 1.0 | round: 1
    echo mr_score | append: ' from ' | append: mr_count | append: ' reviews'
  else
    echo fallback
  endif
-%}
""")

# ---------------------------------------------------------------- page styles section: hero test, shared values, rating sync
edit("sections/muto-bf-style.liquid", [
    ("{{ 'muto-bf-compact.css' | asset_url | stylesheet_tag }}",
     """{%- comment -%} The offer's numbers for the stylesheets and scripts below (one place: snippets/muto-offer.liquid) {%- endcomment -%}
{%- render 'muto-offer', key: 'vars' -%}
{%- render 'muto-informed-sport' -%}
{%- comment -%}
  Hero test. "Hero version" below picks A (as live) or B (adds "Track it on the wearable you already wear." and a
  support line under the headline). An A/B tool, or anyone previewing, can force one with ?hero=a or ?hero=b on
  the address. Set before the buy box is drawn, so there is no flash of the other version.
{%- endcomment -%}
<script>
  (function () {
    var v = {{ section.settings.hero_variant | default: 'B' | downcase | json }};
    var m = /[?&]hero=([ab])\\b/i.exec(location.search);
    if (m) v = m[1].toLowerCase();
    document.documentElement.setAttribute('data-hero', v === 'b' ? 'b' : 'a');
  })();
</script>
<style>html:not([data-hero="b"]) [data-hero-b]{display:none!important}</style>
{{ 'muto-bf-compact.css' | asset_url | stylesheet_tag }}"""),
    ("""{%- render 'muto-bf-compare' -%}
<script>""",
     """{%- render 'muto-bf-compare' -%}
<script>
/* The rating lines ("4.8 from 106 reviews") come from the product's saved review numbers. The reviews widget
   further down counts every product in its list, so once it has loaded, copy its figures into those lines and
   the two always agree. */
(function () {
  function sync() {
    var w = document.getElementById('ReviewsWidget');
    if (!w) return false;
    var m = /Based on\\s+([\\d,]+)\\s+reviews?/i.exec(w.textContent || '');
    var h = w.querySelector('.R-TextHeading');
    var score = h ? parseFloat(h.textContent) : NaN;
    if (!m || !(score > 0)) return false;
    var line = (Math.round(score * 10) / 10).toFixed(1) + ' from ' + m[1] + ' reviews';
    [].forEach.call(document.querySelectorAll('[data-muto-rating]'), function (el) { el.textContent = line; });
    return true;
  }
  function watch() {
    var w = document.getElementById('ReviewsWidget');
    if (!w || sync() || !window.MutationObserver) return;
    var mo = new MutationObserver(function () { if (sync()) mo.disconnect(); });
    mo.observe(w, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', watch); else watch();
})();
</script>
<script>"""),
    ("""    { "type": "checkbox", "id": "extras",""",
     """    { "type": "select", "id": "hero_variant", "label": "Hero version", "default": "B", "info": "B (default): the designed-to-be-tracked line and a support line under the headline. A: without them. Add ?hero=a or ?hero=b to the page address to force one.", "options": [
      { "value": "A", "label": "A (no wearable line)" },
      { "value": "B", "label": "B (designed to be tracked)" }
    ] },
    { "type": "checkbox", "id": "extras","""),
])

# ---------------------------------------------------------------- hero copy (subhead, hero test B, flag on the photo)
edit("snippets/muto-bf-buybox-copy.liquid", [
    ("""created by scientists to support your energy, recovery and healthy ageing.</p>""",
     """created by scientists to support your energy, recovery and healthy ageing.<span data-hero-b> <b>Designed to be tracked on your wearable, so you don’t have to take our word for it.</b></span><span class="mc-sub__support" data-hero-b>No wearable? A 30-second weekly score works just as well. And if it isn’t for you by day 90, you get every subscription payment back.</span></p>"""),
    ("""<span class="mc-heroflag__price"><b>£33/mo</b> Save 53%</span>
  <span class="mc-heroflag__line">+ Free welcome kit worth £72</span>""",
     """<span class="mc-heroflag__price"><b>£33/mo</b> for your first 3 months</span>
  <span class="mc-heroflag__line">Save 53% + free welcome kit worth """ + KIT3 + """</span>"""),
    ("""  html body #MainContent .mc .mc-sub .mc-sub__note{display:block;margin:12px 0 0;font-weight:500;color:#242223}""",
     """  html body #MainContent .mc .mc-sub .mc-sub__note{display:block;margin:12px 0 0;font-weight:500;color:#242223}
  /* Hero test, version B: the support line under the intro */
  html body #MainContent .mc .mc-sub .mc-sub__support{display:block;margin:10px 0 0;font-size:.84em;line-height:1.45;color:rgba(36,34,35,.72)}"""),
])

# ---------------------------------------------------------------- phone buy block
edit("snippets/muto-bf-mars.liquid", [
    ("""<span aria-hidden="true">★★★★★</span> 4.8 from 103 reviews</a>""",
     """<span aria-hidden="true">★★★★★</span> <span data-muto-rating>{%- render 'muto-rating', fallback: '4.8 from 103 reviews' -%}</span></a>"""),
    ("""<span data-mm-gifts>+ £72 free gifts</span><small>No code required</small>""",
     """<span data-mm-gifts>+ """ + KIT3 + """ free gifts</span><small>For your first 3 months</small>"""),
    ("""<button type="button" class="mm-o__btn" data-mm-go>Try it now <svg""",
     """<button type="button" class="mm-o__btn" data-mm-go aria-label="Add 3-Month Supply to cart">""" + CTA + """ <svg"""),
    ("""'american_express,apple_pay,google_pay,klarna,master,paypal,shopify_pay,visa'""",
     """'american_express,apple_pay,google_pay,master,paypal,shopify_pay,visa'"""),
    (""""Try it now" presses it""", """the big button presses it"""),
    ("""save: '53% off', gifts: '+ £72 free gifts',""", """save: '53% off', gifts: '+ """ + KIT3 + """ free gifts',"""),
    ("""save: '28% off', gifts: '+ £62 free gifts',""", """save: '28% off', gifts: '+ """ + KIT1 + """ free gifts',"""),
])

# ---------------------------------------------------------------- plan cards (desktop)
edit("snippets/muto-bf-ag1-plans.liquid", [
    ("""    £1.10 a day, less than half a coffee""", """    £1.10 a day for your first 3 months"""),
    ("""band: 'Best value: £111 off + £72 free gifts',""", """band: 'Best value: £111 off + """ + KIT3 + """ free gifts',"""),
    ("""line: '', per: '£1.10 a day', cup: 'less than half a coffee',""", """line: '', per: '£1.10 a day', cup: ' for your first 3 months',"""),
    ("""line: '', per: '£1.79 a day', cup: 'less than a coffee',""", """line: '', per: '£1.79 a day', cup: ', less than a coffee',"""),
    ("""'<b>' + p.per + '</b>' + (p.cup ? ', ' + p.cup : '')""", """'<b>' + p.per + '</b>' + (p.cup || '')"""),
])

# ---------------------------------------------------------------- welcome-kit tiles
edit("snippets/muto-bf-kit-grid.liquid", [
    ("""  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-worth="£72"] .mc__inc::after{content:"Free gifts worth £72"!important}
  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-worth="£62"] .mc__inc::after{content:"Free gifts worth £62"!important}""",
     """  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-plan="three"] .mc__inc::after{content:"Free gifts worth " var(--muto-kit3)!important}
  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-plan="one"] .mc__inc::after{content:"Free gifts worth " var(--muto-kit1)!important}"""),
    ("""  var WORTH = { three: '£72', one: '£62' };""",
     """  var WORTH = { three: '""" + KIT3 + """', one: '""" + KIT1 + """' };"""),
    ("""    kit.setAttribute('data-kt-worth', one ? WORTH.one : WORTH.three);""",
     """    kit.setAttribute('data-kt-worth', one ? WORTH.one : WORTH.three);
    kit.setAttribute('data-kt-plan', one ? 'one' : 'three');"""),
])

# ---------------------------------------------------------------- top bar (every page)
edit("snippets/muto-bf-bar.liquid", [
    ("""aria-label="Black Friday: 3-Month Supply for £33 a month, save 53%, £1.10 a day, plus a free welcome kit worth £72, while stock lasts. Claim: adds the 3-month plan and opens the cart.">""",
     """aria-label="Black Friday: 3-Month Supply for £33 a month for your first 3 months, save 53%, plus a free welcome kit worth """ + KIT3 + """, while stock lasts. """ + CTA + """: adds the 3-Month Supply to the cart and opens it.">"""),
    ("""<span class="mc-bfx__d"><b>£33/mo (save 53%)</b> · £1.10 a day + free welcome kit worth £72</span>""",
     """<span class="mc-bfx__d"><b>£33/mo for your first 3 months (save 53%)</b> + free welcome kit worth """ + KIT3 + """</span>"""),
    ("""<span class="mc-bfx__m"><b>£33/mo</b> · Save 53% + free kit</span>""",
     """<span class="mc-bfx__m"><b>£33/mo</b> first 3 months</span>"""),
    ("""<span class="mc-bfx__cta">Claim&nbsp;&rarr;</span>""",
     """<span class="mc-bfx__cta">""" + CTA + """&nbsp;&rarr;</span>"""),
])

# ---------------------------------------------------------------- comparison table
edit("snippets/muto-bf-compare-main.liquid", [
    ("""<span class="mc-vs__c mc-vs__c--m" role="cell"><b>£33*</b></span>""",
     """<span class="mc-vs__c mc-vs__c--m" role="cell"><b>£33<small>for your first 3 months, then £41.67–£50</small></b></span>"""),
    ("""? depends on the brand. *Your first 3-Month Supply is £99, about £33 a month; then £125 for the next 3 months and £150 every 3 months after that.""",
     """? depends on the brand. Your first 3-Month Supply is £99, about £33 a month; then £125 for the next 3 months (£41.67 a month) and £150 every 3 months after that (£50 a month)."""),
    ("""<style>
  .mc-vs{""",
     """<style>
  /* MUTO's monthly cost: the intro price, with what it becomes written under it */
  .mc-vs__r--cost .mc-vs__c--m b small{display:block;margin-top:4px;font-size:11.5px;font-weight:400;line-height:1.25;letter-spacing:0;text-transform:none}
  .mc-vs{"""),
])

# ---------------------------------------------------------------- sticky plan bar (product pages)
edit("sections/muto-bf-offer.liquid", [
    ("""<button type="button" class="mc-sbar__btn" data-sbar-add>
        <span class="mc-sbar__btn-full">Add to cart</span><span class="mc-sbar__btn-short">Add</span>""",
     """<button type="button" class="mc-sbar__btn" data-sbar-add aria-label="Add the chosen plan to cart">
        <span class="mc-sbar__btn-full">""" + CTA + """</span><span class="mc-sbar__btn-short">""" + CTA + """</span>"""),
])
edit("assets/muto-bf-sticky.js", [
    ("""  function sub(i) { return [i.day, i.month].filter(Boolean).join(' · '); }""",
     """  /* The 3-Month Supply's £33/mo is an introductory price, so it is never shown without "for your first 3 months" */
  function intro(i) { return /3.?month/i.test(i.name) && i.month ? i.month + ' for your first 3 months' : ''; }
  function sub(i) { return intro(i) || [i.day, i.month].filter(Boolean).join(' · '); }"""),
    ("""    subEl.innerHTML = '';
    if (i.day) {""",
     """    subEl.innerHTML = '';
    if (intro(i)) { subEl.appendChild(document.createTextNode(intro(i))); i = { name: i.name, save: i.save, day: '', month: '' }; }
    if (i.day) {"""),
])

# ---------------------------------------------------------------- menu offer card (every page)
edit("sections/muto-menu.liquid", [
    ("""{%- if s.promo_sub != blank -%}<span class="mmd__promo-sub" style="display:block">{{ s.promo_sub }}</span>{%- endif -%}""",
     """{%- capture promo_kit -%}""" + KIT3 + """{%- endcapture -%}
          {%- if s.promo_sub != blank -%}<span class="mmd__promo-sub" style="display:block">{{ s.promo_sub | replace: '[kit]', promo_kit }}</span>{%- endif -%}"""),
    ("""<span class="mmd__promo-cta">{{ s.promo_cta | default: 'Claim offer' }}<svg""",
     """{%- capture promo_cta -%}""" + CTA + """{%- endcapture -%}
          <span class="mmd__promo-cta">{{ s.promo_cta | default: promo_cta }}<svg"""),
    ("""{ "type": "text", "id": "promo_cta", "label": "Button", "default": "Claim offer" },""",
     """{ "type": "text", "id": "promo_cta", "label": "Button", "info": "Blank: the shared button label, from snippets/muto-offer.liquid" },"""),
    (""""default": "Save 53% + a welcome kit worth £87" },""",
     """"default": "Save 53% + a welcome kit worth [kit]", "info": "[kit] becomes the welcome kit's value, from snippets/muto-offer.liquid" },"""),
])

# ---------------------------------------------------------------- unused top-bar section: defaults brought into line
edit("sections/muto-bf-topbar.liquid", [
    ("""3 months for £99 (save 53%) + welcome kit worth £87" },""", """3 months for £99 (save 53%) + welcome kit worth £72" },"""),
    ("""plus a welcome kit worth £87, while stock lasts.""", """plus a welcome kit worth £72, while stock lasts."""),
])

# ---------------------------------------------------------------- stylesheets: no typed kit value
edit("assets/muto-bf-extra.css", [
    ("""(3-Month: £87 incl. the bottle; 1-Month: £72) */""", """(the values are set once, in snippets/muto-offer.liquid) */"""),
    (""".mc__inc::after{content:"Free gifts worth £87"}""", """.mc__inc::after{content:"Free gifts worth " var(--muto-kit3)}"""),
    (""".mc__inc::after{content:"Free gifts worth £72"}""", """.mc__inc::after{content:"Free gifts worth " var(--muto-kit1)}"""),
])
edit("assets/muto-bf-premium.css", [
    ("""content:"Best value \\00b7  Save 53% + free gifts worth £87";""", """content:"Best value \\00b7  Save 53% + free gifts worth " var(--muto-kit3);"""),
])
edit("assets/muto-bf-copy.css", [
    ("""content:"One-Time Purchase - £70 (no gifts)";""", """content:"One-Time Purchase - £70 (no gifts, no money-back guarantee)";"""),
])

# ---------------------------------------------------------------- rating lines printed by sections
edit("sections/muto-pdp-v2-buy.liquid", [
    ("""<span class="mc__rating-text">{{ section.settings.rating_score }}{% if""",
     """<span class="mc__rating-text"><span data-muto-rating>{%- render 'muto-rating', fallback: section.settings.rating_score -%}</span>{% if"""),
])
edit("sections/muto-loved.liquid", [
    ("""{% endunless %}{{ s.rating }}</p>""",
     """{% endunless %}<span data-muto-rating>{%- render 'muto-rating', fallback: s.rating -%}</span></p>"""),
])

# ---------------------------------------------------------------- cart drawer
# The line under the checkout button is drawn by assets/muto-cart.css (cart drawer and cart page). The icon rows in
# the cart template are hidden by the theme's CSS; their wording is corrected too, in case they are shown again.
edit("assets/muto-cart.css", [
    ("""content:"Free UK delivery on subscriptions  \\00b7  90-day money-back guarantee\\AOrder before 9pm and receive it next day.";""",
     """content:"\\2713\\2002 90-day money-back guarantee on subscriptions\\A\\2713\\2002 Fewer than 1 in 1,000 people ask for a refund\\A\\2713\\2002 Skip, pause or cancel online, anytime\\A\\2713\\2002 A reminder email 5 days before every payment\\A\\2713\\2002 Free next-day UK delivery, order by 9pm";"""),
    # a tidy tinted panel with one reassurance per line, instead of a centred paragraph
    ("""white-space:pre-line;display:block;width:100%;margin-top:14px;text-align:center;font-family:var(--mc-font);font-size:14px;line-height:1.4;color:#242223}""",
     """white-space:pre-line;display:block;width:100%;box-sizing:border-box;margin-top:14px;padding:12px 14px;border-radius:10px;background:#f4f2ef;text-align:left;font-family:var(--mc-font);font-size:13.5px;line-height:1.75;letter-spacing:-.01em;color:#242223}
@media (max-width:480px){:is(#main-cart-footer,cart-drawer) .cart__ctas::after{padding:11px 12px;font-size:12.5px}}"""),
])
edit("snippets/cart-drawer.liquid", [
    ("""<p>90 DAY MONEY-BACK POLICY</p>""", """<p>90-DAY MONEY-BACK GUARANTEE ON SUBSCRIPTIONS</p>""", 2),
    ("""# shown as "+ £87 of free gifts" underneath.""", """# shown as "+ £72 of free gifts" underneath."""),
])

# ---------------------------------------------------------------- the product template: copy and settings only
T = "templates/product.muto-nad-bf-premium.json"
edit(T, [
    # P0.3 / P0.4 / §3.2 "What to expect"
    ("""Most people tell us they notice more energy within days. Everyone’s different, so score yourself on day 1 and compare. Got a wearable? Track the shift yourself.""",
     """You’ll usually feel it before you can measure it, and afternoons tend to come first, often within the first couple of weeks. MUTO is designed to be tracked on your wearable, so take a baseline on day 1 and check it for yourself."""),
    (""""heading": "What people tell us they notice.",""", """"heading": "First you feel it.\\nThen you check it.","""),
    ("""People tell us they notice it around day 60.""", """Many people tell us they start to notice it within the first month."""),
    ("""<p>Give it 60 to 90 days. Many people notice their afternoons first, sometimes within a few weeks. For others it takes longer.</p>""",
     """<p>Most people who feel a difference notice it within the first two to four weeks, and afternoons usually come first: fewer 3pm crashes, and more left for the evening. Some people take longer, which is completely normal, so give it the full 90 days before you decide. That’s exactly why our guarantee runs for 90 days.</p>"""),
    ("""        "q6": {
          "type": "q",""",
     """        "q16": {
          "type": "q",
          "settings": {
            "title": "How do I know this isn’t a £99 placebo?",
            "text": "<p>It’s a fair question, and it’s the one we’d ask too. You can’t tell from a product page, which is why we built MUTO to be checked rather than believed.</p><p>Every dose is on the label, every batch is tested by an independent lab, and MUTO is designed to be tracked on your wearable. Take a baseline on day 1, compare at day 30 and day 90, and judge it on your own afternoons and your own data. If you’re not convinced by day 90, you get every subscription payment back, less delivery. Fewer than 1 in 1,000 people ask for a refund.</p>"
          }
        },
        "q6": {
          "type": "q","""),
    ("""        "q5",
        "q6",
        "q14",""", """        "q5",
        "q16",
        "q6",
        "q14","""),
    (""""title": "Your starting point",
            "text": "<p>Score your afternoons, sleep and recovery out of 10, or note your wearable’s 30-day averages. Then two capsules with breakfast: CoQ10, vitamins D3 and K2 dissolve in fat, so food helps your body take them in.</p>\"""",
     """"title": "Your baseline",
            "text": "<p>Open your wearable and note your 7-day averages for HRV, resting heart rate and recovery. No wearable? Score your afternoons, sleep and recovery out of 10, which takes about thirty seconds. Then take two capsules with breakfast, because CoQ10 and vitamins D3 and K2 dissolve in fat, so food helps your body take them in.</p>\""""),
    (""""label": "Days 3–7",
            "title": "More energy, within days",
            "text": "<p>The first thing most people notice: less of the 3pm wall, and energy left for the evening. B vitamins contribute to the reduction of tiredness and fatigue.</p>\"""",
     """"label": "Weeks 1–2",
            "title": "The first signs",
            "text": "<p>For most people it starts with the 3pm wall: you reach the end of the afternoon and realise you never went looking for that second coffee. B vitamins contribute to the reduction of tiredness and fatigue. If you haven’t noticed anything yet, that’s normal, because every body runs on its own clock.</p>\""""),
    (""""title": "Afternoons that hold",
            "text": "<p>The lift stops being a good day and becomes your normal. Compare your afternoon score with day 1.</p>\"""",
     """"title": "First check-in",
            "text": "<p>Compare your wearable’s 30-day averages with your baseline, and look at the trend rather than any single night. This is where you put what you’ve been feeling next to what your own data shows.</p>\""""),
    (""""title": "Bouncing back sooner",
            "text": "<p>A walk, a round of golf or a gym session stops hanging around for days. Vitamin D contributes to normal muscle function.</p>\"""",
     """"title": "Read the whole picture",
            "text": "<p>Sleep, training, alcohol, travel and illness all move your numbers, so check those before you judge. By now, many people tell us they’re bouncing back sooner after a hard session or a long week. Vitamin D contributes to normal muscle function.</p>\""""),
    (""""title": "Feeling like yourself",
            "text": "<p>Compare your scores with day 1. Many people say they hadn’t realised how flat they’d been. Not for you? Every subscription payment back, less delivery.</p>\"""",
     """"title": "Your verdict",
            "text": "<p>Put day 90 next to day 1, in your own scores and on your own wearable. If you’re glad you did it, keep going. If it isn’t for you, email us within 14 days and you get every subscription payment back, less delivery.</p>\""""),
    # P0.5 energy panel
    ("""Usually the first thing people notice, around day 30.""", """It’s often the first thing people notice, and for many it comes within the first couple of weeks."""),
    # P0.8 one-time line
    ("""Prefer to try one jar first? Buy once – [price] (no gifts)""", """Prefer to try one jar first? Buy once – [price] (no gifts, no money-back guarantee)"""),
    # §3.3 FAQ
    ("""<p>Before you start, score your energy, sleep and recovery out of 10. Do it again at day 30 and day 90, then compare. A pen and paper is fine. Got a wearable? Track the shift yourself, on 30-day averages.</p>""",
     """<p>MUTO is designed to be tracked on your wearable, so you don’t have to take our word for it. Before you start, note your wearable’s 7-day averages, or score your energy, sleep and recovery out of 10 if you don’t wear one: that’s your baseline. Do it again at day 30 and day 90, then compare. A pen and paper is fine. Got a wearable? Compare your 30-day averages with your baseline, and look at the trend, not single nights.</p>"""),
    # §3.4 one button label (the desktop buy button; its price follows it)
    (""""cta_label": "Add to cart",""", """"cta_label": "Start your 90-day test","""),
    # P0.11 the reviews widget's AI summary ("Our customers say…")
    # the timeline opens at "Weeks 1–2: the first signs"
    (""""anchor": "what-to-expect",""", """"anchor": "what-to-expect",
        "open": 2,"""),
    ("""enable_sentiment_analysis: true,""", """enable_sentiment_analysis: false,"""),
    # the hidden in-page bar and the offer box, kept in step with the rest
    ("""plus a welcome kit worth £72. See the offer.""", """plus a welcome kit worth {% render 'muto-offer', key: 'kit3' %}. See the offer."""),
    ("""<span class=\\"mc-bfbar__more\\"> plus a welcome kit worth £72</span>""", """<span class=\\"mc-bfbar__more\\"> plus a welcome kit worth {% render 'muto-offer', key: 'kit3' %}</span>"""),
    ("""<span class=\\"mc-bfbar__cta\\">Claim offer</span>""", """<span class=\\"mc-bfbar__cta\\">{% render 'muto-offer', key: 'cta' %}</span>"""),
    ("""'<p class=\\"mc-bf__kit\\">plus a welcome kit worth £72</p>' +""", """'<p class=\\"mc-bf__kit\\">plus a welcome kit worth {% render 'muto-offer', key: 'kit3' %}</p>' +"""),
])

# ---------------------------------------------------------------- whole files kept in src/ (rewritten or new)
# "What to expect" as an interactive timeline (dots as tabs, one card), and the Informed Sport badge.
for rel in ("sections/muto-expect.liquid", "snippets/muto-informed-sport.liquid", "assets/muto-informed-sport.png"):
    out = os.path.join(HERE, "theme", rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "src", rel), out)
    CHANGED[rel] = "from src/"

for path, n in sorted(CHANGED.items()):
    print(f"{path}: {n}")
