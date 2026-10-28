"""Black Friday clone of the main NAD+ product page.

Takes the trust-band build (theme/templates/product.muto-nad-45.json, made by make_trust.py)
and swaps the dark pre-sale box above the plans for a small white Black Friday box with a
black outline: the offer, and a live count of orders left out of 500.

Usage (from shopify/pdp-trust/):  python3 make_trust.py && python3 make_bf.py
Out: theme/templates/product.muto-nad-bf.json
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "theme", "templates", "product.muto-nad-45.json")
OUT = os.path.join(HERE, "theme", "templates", "product.muto-nad-bf.json")

# --- Offer ----------------------------------------------------------------------------------
TOTAL = 500
CODE = ""   # the 53%-off discount code once it exists in Shopify; blank = nothing applied
OFFER = "Get 53% off your first order, plus a welcome kit worth £77"
# Orders left: shop metafield muto.bf_orders_left (integer). Blank hides the count.
DATA = ('<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"'
        ' data-orders="{{ shop.metafields.muto.bf_orders_left.value }}"></div>')

CSS = """/* Black Friday box, above the plans: white, black outline, orders left out of 500 */
html body .mc .mc-bf{margin:18px 0 0;padding:14px 16px 16px;border:1.5px solid #242223;border-radius:12px;background:#fff;color:#242223}
html body .mc .mc-bf[hidden]{display:none}
html body .mc .mc-bf__tag{display:flex;align-items:center;gap:8px;margin:0 0 6px;font-family:var(--mc-mono,monospace);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}
html body .mc .mc-bf__dot{width:7px;height:7px;border-radius:50%;background:#242223;animation:mcBfPulse 1.6s ease-in-out infinite}
@keyframes mcBfPulse{50%{opacity:.25}}
html body .mc .mc-bf__offer{margin:0;font-size:17px;font-weight:600;line-height:1.25}
html body .mc .mc-bf__stock{display:flex;align-items:center;gap:12px;margin-top:12px}
html body .mc .mc-bf__count{flex:0 0 auto;margin:0;font-size:13px;line-height:1.2}
html body .mc .mc-bf__count b{font-size:15px;font-variant-numeric:tabular-nums}
html body .mc .mc-bf__bar{flex:1;display:block;height:6px;border-radius:3px;background:rgba(36,34,35,.12);overflow:hidden}
html body .mc .mc-bf__bar i{display:block;height:100%;background:#242223;border-radius:3px}
html body .mc .mc-bf__note{margin:8px 0 0;font-size:12px;line-height:1.35;color:rgba(36,34,35,.7)}
html body .mc .mc-bf__note b{font-family:var(--mc-mono,monospace);letter-spacing:.06em;color:#242223}

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
      '<p class="mc-bf__tag"><span class="mc-bf__dot"></span>Black Friday</p>' +
      '<p class="mc-bf__offer">%(offer)s</p>';
    if (left >= 0 && left <= TOTAL) {
      html += '<div class="mc-bf__stock"><p class="mc-bf__count">' +
        (left > 0 ? '<b>' + left + '</b> of ' + TOTAL + ' left' : '<b>All ' + TOTAL + '</b> have gone') +
        '</p><span class="mc-bf__bar" aria-hidden="true"><i style="width:' + Math.round(left / TOTAL * 100) + '%%"></i></span></div>';
    }
    html += '<p class="mc-bf__note">Limited to ' + TOTAL + ' orders.' +
      (CODE ? ' Code <b>' + CODE + '</b> is applied automatically at checkout.' : '') + '</p>';
    box.innerHTML = html;
    plans.parentNode.insertBefore(box, plans);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
""" % {"code": json.dumps(CODE), "total": TOTAL, "offer": OFFER}


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

    # 1. styles: the dark pre-sale box -> the white Black Friday box
    a, b = cut(t, "/* Black Friday pre-sale box, above the plans */", "/* -2 page only:")
    t = a + CSS + b
    # 2. script: the pre-sale countdown -> the Black Friday box
    start = "/* Black Friday pre-sale: real countdown"
    i = t.index(start)
    end = "if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();\n})();\n"
    j = t.index(end, i) + len(end)
    t = t[:i] + JS + t[j:]
    # 3. data: add the orders-left count
    old = '<div id="mc-bf-data" hidden data-left="{{ shop.metafields.muto.bf_boxes_left.value }}"></div>'
    assert old in t
    t = t.replace(old, DATA)
    assert "pre-sale" not in t.lower() and "MUTO10" not in t, "old pre-sale box left behind"
    er["custom_liquid"] = t

    with open(OUT, "w") as fh:
        fh.write(head)
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
