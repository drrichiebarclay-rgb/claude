/* Black Friday pre-sale: real countdown to the offer's end, code applied automatically.
   Change END and CODE here. After END the box disappears and the code is no longer applied.
   Welcome kits left comes from the shop metafield muto.bf_boxes_left (printed into #mc-bf-data by the
   template); it must be the real number left. Blank hides the count. */
(function () {
  var CODE = 'MUTO10';
  var TOTAL = 500;
  var END = new Date('2026-10-28T23:59:00Z'); /* 23:59 UK time, Wed 28 Oct */
  if (Date.now() >= END.getTime()) return;

  /* Apply the code: Shopify keeps it for the cart and checkout */
  try {
    if (!sessionStorage.getItem('mcBf' + CODE)) {
      fetch('/discount/' + encodeURIComponent(CODE), { credentials: 'same-origin' })
        .then(function () { try { sessionStorage.setItem('mcBf' + CODE, '1'); } catch (e) {} });
    }
  } catch (e) {
    fetch('/discount/' + encodeURIComponent(CODE), { credentials: 'same-origin' });
  }

  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function mount() {
    var plans = document.querySelector('.mc .mc__plans');
    if (!plans || document.querySelector('.mc-bf')) return;
    var box = document.createElement('div');
    box.className = 'mc-bf';
    box.setAttribute('role', 'note');
    box.innerHTML =
      '<p class="mc-bf__tag"><span class="mc-bf__dot"></span>Black Friday pre-sale</p>' +
      '<p class="mc-bf__offer">Extra 10% off the Quarterly plan, plus a free welcome kit worth £77</p>' +
      '<p class="mc-bf__note">£135 for your first box instead of £150. Code <b>' + CODE + '</b> is applied automatically at checkout</p>' +
      '<div class="mc-bf__clock" aria-live="off">' +
        '<span data-u="d">00<small>days</small></span><span data-u="h">00<small>hrs</small></span>' +
        '<span data-u="m">00<small>min</small></span><span data-u="s">00<small>sec</small></span></div>' +
      '<p class="mc-bf__ends">Pre-sale ends 23:59, Wednesday 28 October.</p>';
    var data = document.getElementById('mc-bf-data');
    var left = data ? parseInt(data.getAttribute('data-left'), 10) : NaN;
    if (left >= 0 && left <= TOTAL) {
      var stock = document.createElement('div');
      stock.className = 'mc-bf__stock';
      stock.innerHTML = '<p><b>' + left + ' of ' + TOTAL + '</b> free welcome kits left at this price</p>' +
        '<span class="mc-bf__bar"><i style="width:' + Math.max(2, Math.round((TOTAL - left) / TOTAL * 100)) + '%"></i></span>';
      box.appendChild(stock);
    }
    plans.parentNode.insertBefore(box, plans);
    var u = {};
    [].forEach.call(box.querySelectorAll('[data-u]'), function (el) { u[el.getAttribute('data-u')] = el.firstChild; });
    function tick() {
      var t = Math.floor((END.getTime() - Date.now()) / 1000);
      if (t <= 0) { box.hidden = true; clearInterval(iv); return; }
      u.d.nodeValue = pad(Math.floor(t / 86400));
      u.h.nodeValue = pad(Math.floor(t % 86400 / 3600));
      u.m.nodeValue = pad(Math.floor(t % 3600 / 60));
      u.s.nodeValue = pad(t % 60);
    }
    var iv = setInterval(tick, 1000);
    tick();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
