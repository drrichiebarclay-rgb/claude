/* "Ingredients + nutritional information" opens the What's inside fold and scrolls to it */
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[href="#whats-inside"]');
  if (!a) return;
  var d = [].find.call(document.querySelectorAll('.mc__acc-item'), function (x) {
    var s = x.querySelector('summary'); return s && /inside/i.test(s.textContent);
  });
  if (!d) return;
  e.preventDefault();
  d.open = true;
  d.scrollIntoView({ behavior: 'smooth', block: 'center' });
});

(function () {
  var norm = function (t) { return (t || '').replace(/\s+/g, '').replace(/\/mo$/, ''); };
  function cards() { return [].slice.call(document.querySelectorAll('.mc__plans > label.mc__plan')); }

  /* The button shows the old price of whichever plan its price belongs to, struck through */
  function syncWas() {
    var price = document.querySelector('.mc__buy-cta [data-mh-cta-price]');
    if (!price) return;
    var now = norm(price.textContent);
    var card = cards().find(function (c) {
      var p = c.querySelector('.mc__plan-price'); return p && norm(p.textContent) === now;
    }) || document.querySelector('.mc__plans > label.mc__plan.is-selected');
    var was = card && card.querySelector('.mc__plan-was');
    var s = price.parentNode.querySelector('.mc-art__cta-was');
    if (!s) {
      s = document.createElement('s');
      s.className = 'mc-art__cta-was';
      price.parentNode.insertBefore(s, price);
    }
    var t = was ? was.textContent.trim() : '';
    if (s.textContent !== t) s.textContent = t;
  }

  /* Start on the quarterly plan (the second card in Skio's order) */
  function selectQuarterly(tries) {
    var c = cards()[1];
    if (!c) return;
    if (c.classList.contains('is-selected')) return;
    var input = c.querySelector('.mc__plan-input');
    if (input && input.disabled) return;
    c.click();
    if (input && !input.checked) { input.checked = true; input.dispatchEvent(new Event('change', { bubbles: true })); }
    if (tries > 0) setTimeout(function () { selectQuarterly(tries - 1); }, 250);
  }

  function start() {
    var price = document.querySelector('.mc__buy-cta [data-mh-cta-price]');
    if (price && window.MutationObserver) {
      new MutationObserver(syncWas).observe(price, { childList: true, characterData: true, subtree: true });
    }
    document.addEventListener('change', function () { setTimeout(syncWas, 0); });
    document.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('.mc__plan')) setTimeout(syncWas, 0);
    });
    syncWas();
    setTimeout(function () { selectQuarterly(4); setTimeout(syncWas, 50); }, 300);
  }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
