/* Subhead under the title, and the testing-results button under the images. The button opens the
   page's test-results panel (the tests section listens for [data-mtr-open]). */
(function () {
  var SUBHEAD = 'Everything your body needs after 35 for energy, recovery, stress, immunity and longevity.';
  var title = document.querySelector('.mc .mc__buy-title');
  if (title && !document.querySelector('.mc-subhead')) {
    var p = document.createElement('p');
    p.className = 'mc-subhead';
    p.textContent = SUBHEAD;
    title.insertAdjacentElement('afterend', p);
  }
  var media = document.querySelector('.mc .mc__buy-media');
  if (media && !media.querySelector('.mc-tests-btn') && document.querySelector('[data-mtr]')) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'mc-tests-btn';
    b.setAttribute('data-mtr-open', '');
    b.innerHTML = '<span class="mc-tests-btn__tick" aria-hidden="true"><svg viewBox="0 0 12 12" fill="none"><path d="M2.5 6.2 5 8.6l4.5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>View third-party testing results';
    media.appendChild(b);
  }
})();

/* Sticky bar: its button price follows the selected plan as Skio bills it (£150 / £60); show it per
   month like the plan cards (plan-prices.css), old price struck through. Card 1 = monthly, 2 = quarterly. */
(function () {
  var PER_MONTH = { 1: ['£60/mo', '£70'], 2: ['£50/mo', '£70'] };
  function update() {
    var span = document.querySelector('.mh__sticky [data-mh-cta-price]');
    if (!span) return;
    var cards = [].slice.call(document.querySelectorAll('.mc__plans > label.mc__plan'));
    var p = PER_MONTH[cards.findIndex(function (c) { return c.classList.contains('is-selected'); }) + 1];
    if (!p) return;
    var html = '<s class="mc-sticky-was">' + p[1] + '</s> ' + p[0];
    if (span.innerHTML !== html) span.innerHTML = html;
  }
  function start() {
    var span = document.querySelector('.mh__sticky [data-mh-cta-price]');
    if (span && window.MutationObserver) {
      new MutationObserver(update).observe(span, { childList: true, characterData: true, subtree: true });
    }
    document.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('.mc__plan')) { setTimeout(update, 0); setTimeout(update, 60); }
    });
    document.addEventListener('change', function () { setTimeout(update, 0); });
    document.addEventListener('muto:home:plan', update); /* fired by muto-home.js after it paints the price */
    update();
    setTimeout(update, 400);
  }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
