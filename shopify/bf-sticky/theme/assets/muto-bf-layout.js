/* Black Friday page: gallery arrows (and swipe) in place of the thumbnails, and the testing-results
   button moved to where the badges were. Loaded by snippets/muto-bf-bar.liquid. */
(function () {
  var ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9 5l7 7-7 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  function gallery() {
    var main = document.querySelector('.mc .mc__gallery-main');
    if (!main || main.dataset.bfArrows) return;
    var slides = [].slice.call(main.querySelectorAll('[data-mc-slide]'));
    if (slides.length < 2) return;
    main.dataset.bfArrows = '1';
    var thumbs = [].slice.call(document.querySelectorAll('.mc [data-mc-thumb]'));

    function cur() { var i = slides.findIndex(function (s) { return !s.hidden; }); return i < 0 ? 0 : i; }
    function mk(dir, label) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'mc-garrow mc-garrow--' + dir;
      b.setAttribute('aria-label', label);
      b.innerHTML = dir === 'prev' ? ICON.replace('M9 5l7 7-7 7', 'M15 5l-7 7 7 7') : ICON;
      main.appendChild(b);
      return b;
    }
    var prev = mk('prev', 'Previous image');
    var next = mk('next', 'Next image');
    function sync() { prev.hidden = cur() === 0; }
    function go(i) {
      i = (i + slides.length) % slides.length;
      /* The thumbnail's own click keeps the theme's gallery script in step; then make sure */
      if (thumbs[i]) thumbs[i].click();
      slides.forEach(function (s, n) { s.hidden = n !== i; });
      thumbs.forEach(function (t, n) { t.setAttribute('aria-current', n === i ? 'true' : 'false'); });
      sync();
    }
    next.addEventListener('click', function () { go(cur() + 1); });
    prev.addEventListener('click', function () { go(cur() - 1); });
    thumbs.forEach(function (t) { t.addEventListener('click', function () { setTimeout(sync, 0); }); });

    var x0 = null, y0 = 0;
    main.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
    main.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
      x0 = null;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) go(cur() + (dx < 0 ? 1 : -1));
    }, { passive: true });
    sync();
  }

  function tests() {
    var bad = document.querySelector('.mc .mpb-bad');
    var btn = document.querySelector('.mc .mc-tests-btn');
    if (bad && btn && btn.nextElementSibling !== bad) bad.parentNode.insertBefore(btn, bad);
  }

  /* The cards show their new names in CSS; the text itself is renamed too, for the sticky bar's picker */
  function names() {
    [].forEach.call(document.querySelectorAll('.mc .mc__plans > label.mc__plan'), function (c) {
      var n = c.querySelector('.mc__plan-name');
      if (!n) return;
      var t = n.textContent;
      var r = /quarter|3.?month/i.test(t) ? '3-Month Supply' : /month/i.test(t) ? '1-Month Supply' : '';
      if (r && t !== r) { n.textContent = r; c.setAttribute('data-name', r); }
    });
  }

  function run() { names(); gallery(); tests(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
  document.addEventListener('shopify:section:load', function () { setTimeout(run, 60); });
})();
