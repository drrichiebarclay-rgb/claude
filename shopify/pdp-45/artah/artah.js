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
