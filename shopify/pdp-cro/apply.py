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
    {%- render 'muto-offer', key: 'subs' -%}   the line beside the star rating ("Over 2,000 loyal subscribers")
    {%- render 'muto-offer', key: 'vars' -%}   the same values for stylesheets and scripts: CSS variables
                                               (--muto-kit3, --muto-kit1) and window.MUTO_OFFER

  The 3-Month kit is creatine £30, socks £12, travel vial £10, Forever Jar £10 and the 12-week guide £10: £72.
  The Performance Bottle (£15) comes with box 2, so it is not in this figure. The 1-Month kit has no vial: £62.
{%- endcomment -%}
{%- liquid
  assign mo_kit3 = '£72'
  assign mo_kit1 = '£62'
  assign mo_cta = 'Start your 90-day test'
  assign mo_subs = 'Over 2,000 loyal subscribers'
  case key
    when 'kit3'
      echo mo_kit3
    when 'kit1'
      echo mo_kit1
    when 'cta'
      echo mo_cta
    when 'subs'
      echo mo_subs
  endcase
-%}
{%- if key == 'vars' -%}
  <style>:root{--muto-kit3:"{{ mo_kit3 }}";--muto-kit1:"{{ mo_kit1 }}"}</style>
  <script>window.MUTO_OFFER = { kit3: {{ mo_kit3 | json }}, kit1: {{ mo_kit1 | json }}, cta: {{ mo_cta | json }}, subs: {{ mo_subs | json }} };</script>
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
    echo mr_score | append: ' · '
  else
    echo '4.8 · '
  endif
  render 'muto-offer', key: 'subs'
-%}
""")

# ---------------------------------------------------------------- page styles section: hero test, shared values, rating sync
edit("sections/muto-bf-style.liquid", [
    ("{{ 'muto-bf-compact.css' | asset_url | stylesheet_tag }}",
     """{%- comment -%} The offer's numbers for the stylesheets and scripts below (one place: snippets/muto-offer.liquid) {%- endcomment -%}
{%- render 'muto-offer', key: 'vars' -%}
{%- render 'muto-informed-sport' -%}
{%- render 'muto-buy-extras' -%}
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
    /* The variant is exposed for analytics: data-hero-variant on the buy box, and a dataLayer event on page
       view and on every tap of an add-to-cart button, so add-to-cart can be split by variant. */
    var V = v === 'b' ? 'B' : 'A';
    window.MUTO_HERO_VARIANT = V;
    function send(name) {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: name, hero_variant: V });
      try { if (window.Shopify && Shopify.analytics && Shopify.analytics.publish) Shopify.analytics.publish(name, { hero_variant: V }); } catch (e) {}
    }
    send('muto_hero_view');
    document.addEventListener('DOMContentLoaded', function () {
      [].forEach.call(document.querySelectorAll('#MainContent .mc, #mc-sbar'), function (el) { el.setAttribute('data-hero-variant', V); });
    });
    document.addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('.mm-o__btn, .mc__buy-cta, #mc-sbar button, #mc-bfx a, form[action*="/cart/add"] [type="submit"]');
      if (b && /90-day test|add to cart/i.test((b.textContent || '') + ' ' + (b.getAttribute('aria-label') || ''))) send('muto_add_to_cart');
    }, true);
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
    var line = (Math.round(score * 10) / 10).toFixed(1) + ' \u00b7 ' + ((window.MUTO_OFFER && window.MUTO_OFFER.subs) || '');
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
    # the second line inside the buy button (Richie, 19 Nov): the control line above the button now covers cancelling
    (""".mc__buy-cta::after{content:"Skip, pause or cancel online · cancel in 2 clicks"!important;""", """.mc__buy-cta::after{content:"90-day money-back guarantee"!important;"""),
    ("""<p class="mc-for" data-mc-for hidden>Now with free creatine</p>""", """<p class="mc-for" data-mc-for hidden>Designed for over 35s</p>"""),
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
    # P0.12: the bullet loosened the authorised claim
    ("""Protect your cells as you age""", """Built for the years ahead"""),
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
    ("""save: '28% off', gifts: '+ £62 free gifts',""", """save: 'First month', gifts: '+ free welcome kit',"""),
])

# ---------------------------------------------------------------- plan cards (desktop)
edit("snippets/muto-bf-ag1-plans.liquid", [
    ("""    £1.10 a day, less than half a coffee""", """    £1.10 a day for your first 3 months"""),
    ("""band: 'Best value: £111 off + £72 free gifts',""", """band: 'Best value: £111 off + """ + KIT3 + """ free gifts',"""),
    ("""line: '', per: '£1.10 a day', cup: 'less than half a coffee',""", """line: '', per: '£1.10 a day', cup: ' for your first 3 months',"""),
    ("""line: '', per: '£1.79 a day', cup: 'less than a coffee',""", """line: '', per: '£1.79 a day', cup: ' for your first month',"""),
    ("""name: '1-Month Supply', save: 'Save 28%',""", """name: '1-Month Supply', save: '',"""),
    ("""'<b>' + p.per + '</b>' + (p.cup ? ', ' + p.cup : '')""", """'<b>' + p.per + '</b>' + (p.cup || '')"""),
])

# ---------------------------------------------------------------- welcome-kit tiles
edit("snippets/muto-bf-kit-grid.liquid", [
    ("""  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-worth="£72"] .mc__inc::after{content:"Free gifts worth £72"!important}
  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-worth="£62"] .mc__inc::after{content:"Free gifts worth £62"!important}""",
     """  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-plan="three"] .mc__inc::after{content:"Free gifts worth " var(--muto-kit3)!important}
  html:root body #MainContent [id$="__buy"] .mc__kit[data-kt-plan="one"] .mc__inc::after{content:"Free welcome kit included"!important}"""),
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
    (""".mc__inc::after{content:"Free gifts worth £72"}""", """.mc__inc::after{content:"Free welcome kit included"}"""),
])
edit("assets/muto-bf-premium.css", [
    ("""content:"£1.79 a day  \\00b7  Save 28%"}""", """content:"£1.79 a day for your first month"}"""),
    ("""content:"£1.79 per day  \\00b7  Save 28%"!important}""", """content:"£1.79 a day for your first month"!important}"""),
    ("""content:"Best value \\00b7  Save 53% + free gifts worth £87";""", """content:"Best value \\00b7  Save 53% + free gifts worth " var(--muto-kit3);"""),
])
# (The one-time line stays "(no gifts)": the "no money-back guarantee" wording was added, then removed at Richie's request.)

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
@media (max-width:480px){:is(#main-cart-footer,cart-drawer) .cart__ctas::after{padding:11px 12px;font-size:12.5px}}
/* Checkout steps above the checkout button: numbered dots on a line, the first one filled */
.mcs{display:flex;align-items:center;gap:0;margin:14px 0 12px;padding:0;list-style:none;font-family:var(--mc-font);font-size:12.5px;line-height:1;color:rgba(36,34,35,.55)}
.mcs__s{display:flex;align-items:center;gap:7px;margin:0;padding:0;white-space:nowrap}
.mcs__s + .mcs__s{flex:1 1 0;justify-content:flex-end}
.mcs__s + .mcs__s::before{content:"";flex:1 1 auto;height:1px;margin:0 10px;background:rgba(36,34,35,.2)}
.mcs__n{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;border:1px solid rgba(36,34,35,.3);font-size:11px;font-weight:500}
.mcs__s.is-on{color:#242223;font-weight:500}
.mcs__s.is-on .mcs__n{border-color:#242223;background:#242223;color:#fff}"""),
])
edit("snippets/cart-drawer.liquid", [
    ("""        <div class="cart__ctas" {{ block.shopify_attributes }}>""",
     """        {%- comment -%} Where you are in the checkout: Cart, Delivery, Payment {%- endcomment -%}
        {%- if cart != empty -%}
          <ol class="mcs" aria-label="Checkout steps">
            <li class="mcs__s is-on" aria-current="step"><span class="mcs__n">1</span>Cart</li>
            <li class="mcs__s"><span class="mcs__n">2</span>Delivery</li>
            <li class="mcs__s"><span class="mcs__n">3</span>Payment</li>
          </ol>
        {%- endif -%}
        <div class="cart__ctas" {{ block.shopify_attributes }}>"""),
    ("""<p>90 DAY MONEY-BACK POLICY</p>""", """<p>90-DAY MONEY-BACK GUARANTEE ON SUBSCRIPTIONS</p>""", 2),
    ("""# shown as "+ £87 of free gifts" underneath.""", """# shown as "+ £72 of free gifts" underneath."""),
])

# ---------------------------------------------------------------- the product template: copy and settings only
T = "templates/product.muto-nad-bf-premium.json"
# The survey block under the buy box (sections/muto-survey.liquid). Figures from MUTO's customer survey
# (87 men and women aged 30-50); the NAD+ figure is from a published study of NR, so it is shown apart.
SURVEY = """    "survey": {
      "type": "muto-survey",
      "blocks": {
        "r1": { "type": "result", "settings": { "label": "Energy", "value": 92, "text": "report improved energy", "detail": "The thing people mention most is that their afternoons stop fading, so there is still something left for the evening." } },
        "r2": { "type": "result", "settings": { "label": "Recovery", "value": 87, "text": "report better recovery", "detail": "People told us they felt ready to go again sooner, whether that was after training or after a long week." } },
        "r3": { "type": "result", "settings": { "label": "Strain", "value": 93, "text": "bounce back quicker from strain", "detail": "After a hard session, a late night or a heavy week, most said they were back to themselves faster." } },
        "r4": { "type": "result", "settings": { "label": "HRV", "value": 89, "text": "report improved HRV", "detail": "Most said their HRV had improved on their own wearable. This is what customers told us, not a clinical measurement, and your own numbers may differ." } }
      },
      "block_order": ["r1", "r2", "r3", "r4"],
      "settings": {
        "anchor": "survey",
        "eyebrow": "12-week customer trial results",
        "heading": "Studied in real people.",
        "lede": "We asked 87 men and women aged 30 to 50 who take MUTO what had changed for them. Tap a result to see it.",
        "extra_value": "51%",
        "extra_text": "rise in blood NAD+ after two weeks of 300mg NR a day, the amount in MUTO, in a published clinical study.",
        "extra_source": "Conze et al., Scientific Reports, 2019. A study of NR, not of MUTO.",
        "foot": "Survey of 87 men and women taking MUTO between the ages of 30 and 50. Self-reported by customers, not a clinical study. Individual results may vary."
      }
    },
"""
edit(T, [
    # P0.3 / P0.4 / §3.2 "What to expect"
    ("""Most people tell us they notice more energy within days. Everyone’s different, so score yourself on day 1 and compare. Got a wearable? Track the shift yourself.""",
     """You’ll usually feel it before you can measure it: energy that lasts the afternoon comes first, and a body that’s ready to go again follows. MUTO is designed to be tracked on your wearable, so you can check what you feel against your own data."""),
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
     """"title": "Know where you’re starting",
            "text": "<p>Notice how today actually feels: how your afternoons go, how your legs feel on the stairs the morning after training, and how long a hard week takes to shake off. Score each out of 10, which takes about thirty seconds. Then take two capsules with breakfast, because CoQ10 and vitamins D3 and K2 dissolve in fat, so food helps your body take them in.</p>",
            "proof": "Note your 7-day averages for HRV, resting heart rate and recovery. That’s your baseline.\""""),
    (""""label": "Days 3–7",
            "title": "More energy, within days",
            "text": "<p>The first thing most people notice: less of the 3pm wall, and energy left for the evening. B vitamins contribute to the reduction of tiredness and fatigue.</p>\"""",
     """"label": "Weeks 1–2",
            "title": "Your afternoons come back",
            "text": "<p>Energy is usually the first thing people feel. The 3pm wall softens, you stop going looking for that second coffee, and there’s something left for the evening and the people in it. B vitamins contribute to the reduction of tiredness and fatigue. If you haven’t noticed anything yet, that’s normal, because every body runs on its own clock.</p>",
            "proof": "Keep wearing it. It’s too early to read a trend, so go by how your afternoons feel.\""""),
    (""""title": "Afternoons that hold",
            "text": "<p>The lift stops being a good day and becomes your normal. Compare your afternoon score with day 1.</p>\"""",
     """"title": "Ready to go again",
            "text": "<p>By now, many people tell us their legs feel less heavy the morning after a session, and that they’re ready to train, play or simply get on with the week sooner than they used to be. The steadier afternoons tend to have stopped feeling like a lucky day.</p>",
            "proof": "Your first check-in. Compare your 30-day averages with your baseline, and look at the trend rather than any single night.\""""),
    (""""title": "Bouncing back sooner",
            "text": "<p>A walk, a round of golf or a gym session stops hanging around for days. Vitamin D contributes to normal muscle function.</p>\"""",
     """"title": "It becomes your normal",
            "text": "<p>Energy that holds from morning to evening, and bouncing back from a hard session or a long week, stop being things you notice and become how you feel. People often tell us this is when they say yes to more: the extra session, the late dinner, the weekend plans. Vitamin D contributes to normal muscle function.</p>",
            "proof": "Read the whole picture. Sleep, training, alcohol, travel and illness all move your numbers, so check those before you judge.\""""),
    (""""title": "Feeling like yourself",
            "text": "<p>Compare your scores with day 1. Many people say they hadn’t realised how flat they’d been. Not for you? Every subscription payment back, less delivery.</p>\"""",
     """"title": "Feeling like yourself again",
            "text": "<p>Many people tell us they hadn’t realised how flat they’d been until it lifted. This is your verdict: if you’re glad you did it, keep going. If it isn’t for you, email us within 14 days and you get every subscription payment back, less delivery.</p>",
            "proof": "Put day 90 next to day 1, in your own scores and in your own data, and judge it for yourself.\""""),
    # P0.5 energy panel
    ("""Usually the first thing people notice, around day 30.""", """It’s often the first thing people notice, and for many it comes within the first couple of weeks."""),
    # P0.8 one-time line
    # §3.3 FAQ
    ("""<p>Before you start, score your energy, sleep and recovery out of 10. Do it again at day 30 and day 90, then compare. A pen and paper is fine. Got a wearable? Track the shift yourself, on 30-day averages.</p>""",
     """<p>MUTO is designed to be tracked on your wearable, so you don’t have to take our word for it. Before you start, note your wearable’s 7-day averages, or score your energy, sleep and recovery out of 10 if you don’t wear one: that’s your baseline. Do it again at day 30 and day 90, then compare. A pen and paper is fine. Got a wearable? Compare your 30-day averages with your baseline, and look at the trend, not single nights.</p>"""),
    # §3.4 one button label (the desktop buy button; its price follows it)
    (""""cta_label": "Add to cart",""", """"cta_label": "Start your 90-day test","""),
    # P0.11 the reviews widget's AI summary ("Our customers say…")
    (""""save": "Save 28%",""", """"save": "","""),
    ("""Free welcome kit worth £62, then thank-you gifts""", """Free welcome kit, then thank-you gifts"""),
    ("""    "reviews_ticker": {""", SURVEY + """    "reviews_ticker": {"""),
    ("""    "reviews_ticker",
""", """    "reviews_ticker",
    "survey",
"""),
    # future gifts (Richie, 19 Nov): 3-Month plan's "Box 4 on" reads "Box 4"; on the 1-Month plan the bottle comes with box 3
    (""""label": "Box 4 on",""", """"label": "Box 4","""),
    ("""        "mg2": {
          "type": "month",
          "settings": {
            "label": "Box 2",""", """        "mg2": {
          "type": "month",
          "settings": {
            "label": "Box 3","""),
    ("""The MUTO Performance Bottle, free with order 2""", """The MUTO Performance Bottle, free with order 3"""),
    # one message for simplicity (Richie, 19 Nov): "Replaces 5 supplements in one"
    ("""<strong>One jar, not ten.</strong> 19 ingredients at full dose, every one on the label.""", """<strong>Replaces 5 supplements in one.</strong> 19 ingredients at full dose, every one on the label."""),
    (""""title": "One jar replaces five""", """"title": "Replaces 5 supplements in one"""),
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

# ---------------------------------------------------------------- test results panel: an Informed Sport tab
edit("sections/muto-test-results.liquid", [
    ("""'Overview,Full results,Formula,Why it matters' | split: ','""", """'Overview,Full results,Formula,Why it matters,Informed Sport' | split: ','"""),
    ("""  html.mtr-lock{overflow:hidden}""",
     """  html.mtr-lock{overflow:hidden}
  /* Tab 5: the Informed Sport certificate */
  .mtr__is{display:flex;align-items:center;gap:20px;margin-top:32px}
  .mtr__is img{flex:0 0 auto;display:block;width:auto;height:72px;border-radius:6px}
  .mtr__is p{margin:0;max-width:44ch;font-size:15.5px;line-height:1.55;color:var(--mtr-muted)}
  @media (max-width:749px){.mtr__is{align-items:flex-start;gap:14px}.mtr__is img{height:52px}.mtr__is p{font-size:14.5px}}"""),
    ("""        {%- if s.certificate != blank -%}<a class="mtr__cert" href="{{ s.certificate }}" target="_blank" rel="noopener">Download the certificate (PDF) →</a>{%- endif -%}
      </section>""",
     """        {%- if s.certificate != blank -%}<a class="mtr__cert" href="{{ s.certificate }}" target="_blank" rel="noopener">Download the certificate (PDF) →</a>{%- endif -%}
      </section>

      {%- comment -%} 5 Informed Sport. Details typed from the certificate (assets/muto-informed-sport-certificate.pdf). {%- endcomment -%}
      <section class="mtr__panel" role="tabpanel" id="mtr-p-{{ sid }}-5" aria-labelledby="mtr-tab-{{ sid }}-5" hidden>
        <h3 class="mtr__h">Informed Sport certified.</h3>
        <p class="mtr__sub">Informed Sport is the independent programme, run by LGC, that tests supplements for substances banned in sport. NAD<sup>+</sup> Cellular Complex meets its standards, and every batch is tested before it is released.</p>
        <div class="mtr__is">
          <img src="{{ 'muto-informed-sport.png' | asset_url }}" alt="Informed Sport: banned substance tested, every batch" width="148" height="72" loading="lazy">
          <p>That matters if you compete, and it is one more outside check on what is in the jar if you don’t.</p>
        </div>
        <div class="mtr__list">
          <p class="mtr__lh"><span>Certificate</span><span>Details</span></p>
          <p class="mtr__row"><span>Product</span><span><em style="font-style:normal">MUTO NAD+ Cellular Complex</em></span></p>
          <p class="mtr__row"><span>Member</span><span>MUTO Longevity Ltd</span></p>
          <p class="mtr__row"><span>Certification number</span><span>LMS-PSRM-09495</span></p>
          <p class="mtr__row"><span>Date of certification</span><span>18 Nov 2026</span></p>
          <p class="mtr__row"><span>Certified by</span><span>LGC Limited, Cambridgeshire, UK</span></p>
        </div>
        <a class="mtr__cert" href="{{ 'muto-informed-sport-certificate.pdf' | asset_url }}" target="_blank" rel="noopener">View the certificate (PDF) →</a>
        <p class="mtr__note">You can confirm the certification, and check that your batch is listed, at <a href="https://www.informed-sport.com/" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline">informed-sport.com</a>.</p>
      </section>"""),
])

# Shopify allows 25 sections in a template. The survey block is the 26th, so the "statement" section, which
# was switched off (disabled) and not shown on the page, is taken out of the template to make room.
_p = os.path.join(HERE, "theme", T)
_t = open(_p, encoding="utf-8", newline="").read()
_a = _t.index('    "statement": {')
_b = _t.index('\n    },\n', _a) + len('\n    },\n')
assert '"disabled": true' in _t[_a:_b] and _t.count('    "statement",\n') == 1
_t = (_t[:_a] + _t[_b:]).replace('    "statement",\n', '')
open(_p, "w", encoding="utf-8", newline="").write(_t)

# ---------------------------------------------------------------- brief v2 (Fairing): bullet, persona chip, review order
edit("snippets/muto-bf-review-box.liquid", [
    # 4.5: the longevity persona first; it takes the place of "Too many pots on the shelf" (four chips wrap
    # to a second row in the box, and the value line in the buy box now covers that point)
    ("""    <button type="button" class="mc-rv__chip" data-f="Energy" aria-pressed="false">Flat by 3pm</button>""",
     """    <button type="button" class="mc-rv__chip" data-f="Ageing" aria-pressed="false">Thinking about the next 20 years</button>
    <button type="button" class="mc-rv__chip" data-f="Energy" aria-pressed="false">Flat by 3pm</button>"""),
    ("""    <button type="button" class="mc-rv__chip" data-f="Pots" aria-pressed="false">Too many pots on the shelf</button>
""", """"""),
    ("""Slower to bounce back, Too many pots on the shelf;""", """Slower to bounce back; Thinking about the next 20 years comes first;"""),
])
# the reviews that speak to the longevity persona get its tag, so the new chip filters to them
_p = os.path.join(HERE, "theme", "snippets/muto-bf-review-box.liquid")
_t = open(_p, encoding="utf-8", newline="").read()
import re as _re
_figs = _re.findall(r'    <figure class="mc-rv__slide".*?</figure>\n', _t, flags=_re.S)
assert len(_figs) >= 6
_new = []
for _f in _figs:
    if _re.search(r'healthy ageing|age well|Mid 30s|as resilient as my 20s|since my mid 20s', _f):
        _f = _re.sub(r'data-tags="\|', 'data-tags="|Ageing|', _f, count=1)
    _new.append(_f)
assert sum('|Ageing|' in _f for _f in _new) >= 2
# 4.6: the first five slides show an age of 40 or over where an age is shown, so Kevin, 36 moves to sixth
_k = [i for i, _f in enumerate(_new) if '<b>Kevin, 36</b>' in _f]
assert _k == [2]
_new.insert(5, _new.pop(2))
_a = _t.index(_figs[0]); _b = _t.index(_figs[-1]) + len(_figs[-1])
assert _t[_a:_b] == "".join(_figs)
_first = _new[0]
_t = _t[:_a] + "".join(_new) + _t[_b:]
open(_p, "w", encoding="utf-8", newline="").write(_t)

# ---------------------------------------------------------------- phones: back to the plan cards with the gifts
# (Richie, 19 Nov) On phones the compact price-and-button block (.mm-o) had replaced the plan cards. It is
# switched off, and the phone-only rules that hid the plan cards, the kit inside the card, the Add to cart
# button and the one-time link are removed, so phones show the same buy box as desktop. The review quotes,
# rating, ticks and links at the top of the phone layout stay.
_p = os.path.join(HERE, "theme", "snippets/muto-bf-mars.liquid")
_t = open(_p, encoding="utf-8", newline="").read()
_a = _t.index("    /* The welcome kit: its own block under the two plan cards, the gifts in one row to swipe */")
_b = _t.index("    /* The moving reviews strip: above the photo, slim */")
assert 0 < _a < _b and _t[_a:_b].count("mc__plans > label.mc__plan{display:none!important}") == 1
_t = _t[:_a] + "    /* The compact price-and-button block is off: phones show the plan cards with the gifts, as desktop does */\n    html body #MainContent .mc .mm-o{display:none!important}\n" + _t[_b:]
open(_p, "w", encoding="utf-8", newline="").write(_t)

# ---------------------------------------------------------------- "Your life won't fit a perfect routine" block
edit("snippets/muto-bf-jobs.liquid", [
    # one message for simplicity (Richie, 19 Nov)
    ("""        <h3>One jar, not ten</h3>""", """        <h3>Replaces 5 supplements in one</h3>"""),
])

# ---------------------------------------------------------------- whole files kept in src/ (rewritten or new)
# "What to expect" as an interactive timeline (dots as tabs, one card), and the Informed Sport badge.
for rel in ("sections/muto-expect.liquid", "snippets/muto-informed-sport.liquid", "snippets/muto-buy-extras.liquid", "sections/muto-survey.liquid", "assets/muto-informed-sport.png", "assets/muto-informed-sport-certificate.pdf"):
    out = os.path.join(HERE, "theme", rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "src", rel), out)
    CHANGED[rel] = "from src/"

for path, n in sorted(CHANGED.items()):
    print(f"{path}: {n}")
