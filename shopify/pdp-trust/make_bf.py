"""Black Friday clone of the main NAD+ product page.

Takes the trust-band build (theme/templates/product.muto-nad-45.json, made by make_trust.py)
and swaps the dark pre-sale box above the plans for a small white Black Friday box with a
black outline: the offer, and a live count of orders left out of 500.

Usage (from shopify/pdp-trust/):  python3 make_trust.py && python3 make_bf.py
Out: theme/templates/product.muto-nad-bf.json
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "theme", "templates", "product.muto-nad-trust.json")
OUT = os.path.join(HERE, "theme", "templates", "product.muto-nad-bf.json")

# --- Offer ----------------------------------------------------------------------------------
TOTAL = 500
CODE = ""   # the 53%-off discount code once it exists in Shopify; blank = nothing applied
HEADLINE = "53% off your first order"
KIT = "plus a welcome kit worth £77"
SCHEDULE = "£99 for your first order, £125 on your second, £150 on your third."
# Quarterly card while the offer runs: £99 first box = £33/mo, £1.10 a day (90 days)
Q_SAVE = "Save 53%"
Q_NOTE = "3 months’ supply: £99 for your first box, then £125, then £150 · £1.10 a day"
Q_PER_MONTH = "£33/mo"
# Monthly card while the offer runs: £49.99 first month, then £60 every 4 weeks (49.99 / 28 = £1.79 a day)
M_SAVE = "Save 28%"   # £49.99 vs £70 is 28.6%, rounded down
M_NOTE = "£49.99 for your first month, then £60 every 4 weeks · £1.79 a day"
M_PER_MONTH = "£49.99/mo"
# Subhead under the title (set by the easy_read script)
SUBHEAD = "Our lowest price yet, while stocks last. Been waiting to try MUTO? Now’s the time to run the 90-day test."
# Orders left: shop metafield muto.bf_orders_left (integer). Blank hides the count.
DATA = ('<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"'
        ' data-orders="{{ shop.metafields.muto.bf_orders_left.value }}"></div>')

CSS = """/* Black Friday box, above the plans: white, black outline. Offer on the left, orders left out
   of 500 on the right (under it on phones), a bar along the foot. */
html body .mc .mc-bf{margin:18px 0 0;padding:16px 18px 16px;border:1.5px solid #242223;border-radius:12px;background:#fff;color:#242223;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 16px;align-items:start}
html body .mc .mc-bf[hidden]{display:none}
/* Plan bar: "Black Friday offer · Limited stock" on the left, "Best value" on the right as a filled turquoise pill */
html body .mc .mc__plans-banner::before{order:2;content:"Best value"!important;padding:6px 12px;border-radius:999px;background:#5efaff;color:#242223!important;font-size:12px;line-height:1;letter-spacing:.1em}
/* Black Friday subhead: fill each line before breaking (no balancing), a touch heavier */
html body .mc .mc-subhead,html body .mc .mc__buy-copy > .mc-subhead{text-wrap:wrap!important;font-weight:500!important}
html body .mc .mc-bf__tag{grid-column:1/-1;display:flex;align-items:center;gap:8px;margin:0 0 4px;font-family:var(--mc-mono,monospace);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}
html body .mc .mc-bf__dot{width:8px;height:8px;border-radius:50%;background:#242223;animation:mcBfPulse 1.6s ease-in-out infinite}
@keyframes mcBfPulse{50%{opacity:.25}}
html body .mc .mc-bf__main{grid-column:1;min-width:0}
html body .mc .mc-bf__offer{margin:0;font-size:clamp(24px,2.4vw,30px);font-weight:600;line-height:1.05;letter-spacing:-.01em}
html body .mc .mc-bf__kit{margin:4px 0 0;font-size:16px;font-weight:600;line-height:1.25}
html body .mc .mc-bf__sched{margin:8px 0 0;font-size:14px;line-height:1.4;color:rgba(36,34,35,.75)}
html body .mc .mc-bf__count{grid-column:2;grid-row:2;margin:0;min-width:96px;max-width:130px;padding:10px 12px 8px;border:1.5px solid #242223;border-radius:10px;text-align:center}
html body .mc .mc-bf__count b{display:block;font-size:30px;font-weight:600;line-height:1;font-variant-numeric:tabular-nums}
html body .mc .mc-bf__count small{display:block;margin-top:4px;font-family:var(--mc-mono,monospace);font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase}
html body .mc .mc-bf__foot{grid-column:1/-1;display:flex;align-items:center;gap:12px;margin-top:10px}
html body .mc .mc-bf__bar{flex:1;display:block;height:6px;border-radius:3px;background:rgba(36,34,35,.12);overflow:hidden}
html body .mc .mc-bf__bar i{display:block;height:100%;background:#242223;border-radius:3px}
html body .mc .mc-bf__note{flex:0 0 auto;margin:0;font-size:12px;line-height:1.35;color:rgba(36,34,35,.7)}
html body .mc .mc-bf__note b{font-family:var(--mc-mono,monospace);letter-spacing:.06em;color:#242223}
@media (max-width:480px){
  html body .mc .mc-bf{grid-template-columns:1fr}
  html body .mc .mc-bf__count{grid-column:1;grid-row:auto;display:flex;align-items:baseline;justify-content:center;gap:8px;margin-top:10px;max-width:none;width:100%;text-align:left}
  html body .mc .mc-bf__count small{white-space:nowrap;font-family:var(--mc-font);font-size:17px;font-weight:500;letter-spacing:0;text-transform:none}
  html body .mc .mc-bf__count b{display:inline;font-size:28px}
  html body .mc .mc-bf__count small{display:inline;margin:0}
  html body .mc .mc-bf__foot{flex-wrap:wrap}
}

"""

JS = """/* Black Friday: 53%% off the first order plus the welcome kit, limited to TOTAL orders.
   Orders left comes from the shop metafield muto.bf_orders_left (printed into #mc-bf-data by the
   template); it must be the real number left. Blank hides the count. CODE, once set, is applied
   automatically so it is on the cart and checkout. */
(function () {
  var CODE = %(code)s;
  var TOTAL = %(total)d;
  if (CODE) {
    try {
      if (!sessionStorage.getItem('mcBf' + CODE)) {
        fetch('/discount/' + encodeURIComponent(CODE), { credentials: 'same-origin' })
          .then(function () { try { sessionStorage.setItem('mcBf' + CODE, '1'); } catch (e) {} });
      }
    } catch (e) {
      fetch('/discount/' + encodeURIComponent(CODE), { credentials: 'same-origin' });
    }
  }
  function mount() {
    var plans = document.querySelector('.mc .mc__plans');
    if (!plans || document.querySelector('.mc-bf')) return;
    var data = document.getElementById('mc-bf-data');
    var left = data ? parseInt(data.getAttribute('data-orders'), 10) : NaN;
    var box = document.createElement('div');
    box.className = 'mc-bf';
    box.setAttribute('role', 'note');
    var html =
      '<p class="mc-bf__tag"><span class="mc-bf__dot"></span>Black Friday offer</p>' +
      '<div class="mc-bf__main"><p class="mc-bf__offer">%(headline)s</p>' +
      '<p class="mc-bf__kit">%(kit)s</p>' +
      '<p class="mc-bf__sched">%(schedule)s</p></div>';
    var hasCount = left >= 0 && left <= TOTAL;
    if (hasCount) {
      html += '<p class="mc-bf__count" aria-label="' + left + ' out of ' + TOTAL + ' remaining"><b>' + left +
        '</b><small>out of ' + TOTAL + ' remaining</small></p>';
    }
    html += '<div class="mc-bf__foot">' +
      (hasCount ? '<span class="mc-bf__bar" aria-hidden="true"><i style="width:' + Math.round(left / TOTAL * 100) + '%%"></i></span>' : '') +
      '<p class="mc-bf__note">' + (hasCount && left === 0 ? 'All ' + TOTAL + ' have gone.' : 'Limited to ' + TOTAL + ' orders.') +
      (CODE ? ' Code <b>' + CODE + '</b> is applied at checkout.' : '') + '</p></div>';
    box.innerHTML = html;
    plans.parentNode.insertBefore(box, plans);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
""" % {"code": json.dumps(CODE), "total": TOTAL, "headline": HEADLINE, "kit": KIT, "schedule": SCHEDULE}


def cut(text, start, end_marker):
    """Return (before, after) around the span that starts at `start` and runs up to `end_marker`."""
    i = text.index(start)
    j = text.index(end_marker, i)
    return text[:i], text[j:]


def main():
    raw = open(SRC).read()
    head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
    er = d["sections"]["easy_read"]["settings"]
    t = er["custom_liquid"]
    hs = d["sections"]["head_styles"]["settings"]   # the page's styles, at the top (see make_trust.hoist_styles)

    # 1. styles: the white Black Friday box (the trust build has already removed the pre-sale box)
    h = hs["custom_liquid"]
    k = h.index("/* -2 page only:")
    h = h[:k] + CSS + h[k:]
    # 2. script, before the subhead script
    k = t.index("/* Subhead under the title")
    t = t[:k] + JS + "\n" + t[k:]
    # 3. data: the orders-left count
    t = DATA + "\n" + t
    # 4. quarterly card: per-month price drawn by the stylesheet, and the sticky bar's copy of it
    old_q = 'label.mc__plan:nth-of-type(2) .mc__plan-prices::before{content:"£50/mo"}'
    assert old_q in h
    h = h.replace(old_q, 'label.mc__plan:nth-of-type(2) .mc__plan-prices::before{content:"%s"}' % Q_PER_MONTH)
    old_m = 'label.mc__plan:nth-of-type(1) .mc__plan-prices::before{content:"£60/mo"}'
    assert old_m in h
    h = h.replace(old_m, 'label.mc__plan:nth-of-type(1) .mc__plan-prices::before{content:"%s"}' % M_PER_MONTH)
    old_s = "var PER_MONTH = { 1: ['£60/mo', '£70'], 2: ['£50/mo', '£70'] };"
    assert old_s in t
    t = t.replace(old_s, "var PER_MONTH = { 1: ['%s', '£70'], 2: ['%s', '£70'] };" % (M_PER_MONTH, Q_PER_MONTH))
    # 5. subhead: kept as on the main page (the Black Friday subhead was dropped on 28 Oct)
    assert "pre-sale" not in t.lower() and "MUTO10" not in t
    er["custom_liquid"] = t
    hs["custom_liquid"] = h

    q = next(b for b in d["sections"]["buy"]["blocks"].values()
             if b["type"] == "plan" and b["settings"].get("name") == "Quarterly plan")
    q["settings"]["save"] = Q_SAVE
    q["settings"]["note"] = Q_NOTE
    m = next(b for b in d["sections"]["buy"]["blocks"].values()
             if b["type"] == "plan" and b["settings"].get("name") == "Monthly plan")
    m["settings"]["save"] = M_SAVE
    m["settings"]["note"] = M_NOTE

    # Black bar over the plans: "Black Friday offer" (the "✦ Best value" label stays on its left)
    d["sections"]["buy"]["settings"]["plans_banner"] = "Black Friday offer · Limited stock"
    # Ticks: the welcome-kit line first, on both plans
    import re as _re
    for plan in (q, m):
        items = _re.findall(r"<li>.*?</li>", plan["settings"]["detail"])
        kit = [i for i in items if "welcome kit" in i.lower()]
        assert len(kit) == 1, items
        plan["settings"]["detail"] = "<ul>" + "".join(kit + [i for i in items if i not in kit]) + "</ul>"

    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
