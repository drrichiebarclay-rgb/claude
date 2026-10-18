/* Black Friday early access: real countdown to the offer's end, code applied automatically.
   Change END and CODE here. After END the box disappears and the code is no longer applied. */
(function () {
  var CODE = 'MUTO10';
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
      '<p class="mc-bf__tag"><span class="mc-bf__dot"></span>Black Friday early access</p>' +
      '<p class="mc-bf__offer">Extra 10% off your first order</p>' +
      '<p class="mc-bf__note">Code <b>' + CODE + '</b> is applied automatically at checkout</p>' +
      '<div class="mc-bf__clock" aria-live="off">' +
        '<span data-u="d">00<small>days</small></span><span data-u="h">00<small>hrs</small></span>' +
        '<span data-u="m">00<small>min</small></span><span data-u="s">00<small>sec</small></span></div>' +
      '<p class="mc-bf__ends">Early access ends 23:59, Wednesday 28 October.</p>';
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
