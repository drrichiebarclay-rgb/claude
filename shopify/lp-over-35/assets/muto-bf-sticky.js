(function () {
  var bar = document.getElementById('mc-sbar');
  if (!bar || bar.dataset.ready) return;
  bar.dataset.ready = '1';
  var select = bar.querySelector('[data-sbar-select]');
  var nameEl = bar.querySelector('[data-sbar-name]');
  var subEl = bar.querySelector('[data-sbar-sub]');
  var priceEl = bar.querySelector('[data-sbar-price]');
  var addBtn = bar.querySelector('[data-sbar-add]');

  /* Plan cards from the first buy box only. A page can carry the buy box twice (the listicle);
     muto-home.js keeps the copies on the same plan, so one set of options is enough. */
  function cards() {
    var plans = document.querySelector('.mc__plans');
    return plans ? [].slice.call(plans.querySelectorAll(':scope > label.mc__plan')) : [];
  }
  function clean(s) { return (s || '').replace(/^["']|["']$/g, '').replace(/\s+/g, ' ').trim(); }
  /* Text drawn by the page's CSS (the per-day pill and the per-month price), so the bar always says
     what the cards say, and changes when they do. */
  function pseudo(el, which) {
    if (!el) return '';
    var c = getComputedStyle(el, which).content;
    return c && c !== 'none' && c !== 'normal' ? clean(c) : '';
  }
  function info(card) {
    var name = clean((card.querySelector('.mc__plan-name') || {}).textContent) || card.getAttribute('data-name') || '';
    var save = clean((card.querySelector('.mc__plan-save') || {}).textContent);
    var day = pseudo(card.querySelector('.mc__plan-head'), '::after');
    var month = pseudo(card.querySelector('.mc__plan-prices'), '::before') || card.getAttribute('data-price') || '';
    return { name: name, save: save, day: day, month: month };
  }
  function label(i) { return i.name + (i.save ? ' (' + i.save.replace(/^save/i, 'Save') + ')' : ''); }
  function sub(i) { return [i.day, i.month].filter(Boolean).join(' · '); }

  function build() {
    var list = cards();
    if (!list.length) return false;
    /* Same order as on the page: the Quarterly box leads (it is ordered first by the page's CSS) */
    var order = list.map(function (c, n) { return { c: c, n: n, o: parseInt(getComputedStyle(c).order, 10) || 0 }; })
      .sort(function (a, b) { return a.o - b.o || a.n - b.n; });
    select.innerHTML = '';
    order.forEach(function (x) {
      var opt = document.createElement('option');
      var i = info(x.c);
      opt.value = String(x.n);
      opt.textContent = label(i) + (sub(i) ? ' – ' + sub(i) : '');
      if (x.c.classList.contains('is-unavailable')) opt.disabled = true;
      select.appendChild(opt);
    });
    return true;
  }

  function paint() {
    var list = cards();
    var n = list.findIndex(function (c) { return c.classList.contains('is-selected'); });
    if (n < 0) n = 0;
    var card = list[n];
    if (!card) return;
    var i = info(card);
    select.value = String(n);
    nameEl.textContent = label(i);
    subEl.innerHTML = '';
    if (i.day) { var b = document.createElement('b'); b.textContent = i.day; subEl.appendChild(b); }
    if (i.day && i.month) subEl.appendChild(document.createTextNode(' · '));
    if (i.month) subEl.appendChild(document.createTextNode(i.month));
    /* The price on the page's own button (what Skio bills today), so the two buttons agree */
    var p = document.querySelector('.mc__buy-cta [data-mh-cta-price]');
    priceEl.textContent = p ? clean(p.textContent) : '';
  }

  select.addEventListener('change', function () {
    var card = cards()[parseInt(select.value, 10)];
    if (card && !card.classList.contains('is-selected')) card.click();
    setTimeout(paint, 0);
  });

  addBtn.addEventListener('click', function () {
    /* The page's cart form, kept in step with the chosen card by muto-home.js */
    var field = document.querySelector('[data-mh-cart-id]');
    var form = field && field.form;
    var main = document.querySelector('.mc__buy-cta');
    if (form && field.value) {
      if (form.requestSubmit) {
        var btn = document.querySelector('button[form="' + form.id + '"][name="add"]');
        form.requestSubmit(btn || undefined);
      } else form.submit();
    } else if (main) main.click();
  });

  document.addEventListener('muto:home:plan', function () { setTimeout(paint, 0); });
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.mc__plan, .mc__plan-detail')) setTimeout(paint, 30);
  });

  /* Show the bar whenever the page's own Add to cart button is off screen */
  function watch(sel) {
    var mains = [].slice.call(document.querySelectorAll(sel || '.mc__buy-cta'));
    var seen = [];
    function show(on) {
      bar.classList.toggle('is-visible', on);
      bar.setAttribute('aria-hidden', on ? 'false' : 'true');
      if ('inert' in bar) bar.inert = !on;
    }
    /* With more than one buy box, the bar shows only while none of their buttons is on screen */
    if (mains.length && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (e) {
          var k = seen.indexOf(e.target);
          if (e.isIntersecting && k < 0) seen.push(e.target);
          if (!e.isIntersecting && k > -1) seen.splice(k, 1);
        });
        show(!seen.length);
      }, { threshold: 0 });
      mains.forEach(function (m) { io.observe(m); });
    } else {
      show(true);
    }
  }

  /* A page with no buy box (the over-35 listicle's offer cards): the bar offers the 3-month plan and its button
     hands the tap to the Black Friday top bar's Claim, as the cards' own Claim buttons do */
  function offerMode() {
    var claim = document.getElementById('mc-bfx');
    if (!claim || !claim.getAttribute('data-variant') || !document.querySelector('[data-mlst-claim]')) return;
    var pick = select.closest('.mc-sbar__pick');
    select.hidden = true;
    if (pick) pick.style.pointerEvents = 'none';
    nameEl.textContent = '3-Month Supply';
    subEl.textContent = 'Black Friday · welcome kit included';
    priceEl.textContent = '£99';
    addBtn.addEventListener('click', function () { claim.click(); });
    watch('[data-mlst-claim]');
  }

  function start() {
    if (!build()) { offerMode(); return; }
    paint();
    watch();
    /* The price on the main button is repainted by the page after load; follow it */
    var p = document.querySelector('.mc__buy-cta [data-mh-cta-price]');
    if (p && window.MutationObserver) new MutationObserver(paint).observe(p, { childList: true, characterData: true, subtree: true });
    setTimeout(paint, 600);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

