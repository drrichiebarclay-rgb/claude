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
