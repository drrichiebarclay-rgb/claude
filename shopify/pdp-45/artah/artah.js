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
