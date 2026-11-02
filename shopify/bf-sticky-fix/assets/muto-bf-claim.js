(function () {
  var bar = document.getElementById('mc-bfx');
  if (!bar) return;
  var busy = false;

  /* The Quarterly plan: from the Liquid above, or failing that from the page's Quarterly card
     (the second card, Skio's order), so a renamed selling plan still works. */
  function quarterly() {
    var v = bar.getAttribute('data-variant'), p = bar.getAttribute('data-plan');
    if (v) return { id: v, plan: p };
    var card = document.querySelectorAll('.mc__plans > label.mc__plan')[1];
    if (card && card.getAttribute('data-variant')) return { id: card.getAttribute('data-variant'), plan: card.getAttribute('data-plan') || '' };
    return null;
  }

  /* No script, or the add fails: bring the plans into view instead, clear of the bar */
  function scrollToOffer() {
    var to = document.querySelector('.mc-bf') || document.querySelector('.mc__plans');
    if (!to) return;
    var y = to.getBoundingClientRect().top + window.pageYOffset - bar.offsetHeight - 12;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }

  function done(ok) {
    if (ok) { window.location.href = '/checkout'; return; }
    busy = false;
    bar.classList.remove('is-busy');
    bar.removeAttribute('aria-busy');
    scrollToOffer();
  }

  bar.addEventListener('click', function (e) {
    e.preventDefault();
    if (busy) return;
    var q = quarterly();
    if (!q || !window.fetch) { scrollToOffer(); return; }
    busy = true;
    bar.classList.add('is-busy');
    bar.setAttribute('aria-busy', 'true');
    var root = (window.Shopify && Shopify.routes && Shopify.routes.root) || '/';
    var planId = q.plan ? parseInt(q.plan, 10) : null;
    /* Already in the cart on this plan (a second tap, or back from checkout): don't add a second box */
    fetch(root + 'cart.js', { credentials: 'same-origin' })
      .then(function (r) { return r.ok ? r.json() : { items: [] }; })
      .catch(function () { return { items: [] }; })
      .then(function (cart) {
        var has = (cart.items || []).some(function (it) {
          var sp = it.selling_plan_allocation && it.selling_plan_allocation.selling_plan;
          return String(it.variant_id) === String(q.id) && (sp ? sp.id : null) === planId;
        });
        if (has) return done(true);
        var item = { id: parseInt(q.id, 10), quantity: 1 };
        if (planId) item.selling_plan = planId;
        return fetch(root + 'cart/add.js', {
          method: 'POST',
          credentials: 'same-origin',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ items: [item] })
        }).then(function (r) { done(r.ok); });
      })
      .catch(function () { done(false); });
  });
})();
