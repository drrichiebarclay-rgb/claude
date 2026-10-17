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

/* Start on the quarterly plan (the second card in Skio's order), once the section script is ready */
window.addEventListener('load', function () {
  setTimeout(function () {
    var cards = document.querySelectorAll('.mc__plans > label.mc__plan');
    var q = cards[1] && cards[1].querySelector('.mc__plan-input');
    if (q && !q.checked && !q.disabled) q.click();
  }, 50);
});

/* The button shows the selected plan's old price struck through before its price */
(function () {
  function syncWas() {
    var price = document.querySelector('.mc__buy-cta [data-mh-cta-price]');
    if (!price) return;
    var input = document.querySelector('.mc__plans .mc__plan-input:checked');
    var card = input && input.closest('.mc__plan');
    var was = card && card.querySelector('.mc__plan-was');
    var s = price.parentNode.querySelector('.mc-art__cta-was');
    if (!s) {
      s = document.createElement('s');
      s.className = 'mc-art__cta-was';
      price.parentNode.insertBefore(s, price);
    }
    s.textContent = was ? was.textContent.trim() : '';
  }
  document.addEventListener('change', function (e) {
    if (e.target.classList && e.target.classList.contains('mc__plan-input')) setTimeout(syncWas, 0);
  });
  window.addEventListener('load', function () { setTimeout(syncWas, 120); });
  document.addEventListener('DOMContentLoaded', syncWas);
})();
