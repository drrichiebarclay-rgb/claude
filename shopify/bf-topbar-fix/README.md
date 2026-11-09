# Black Friday PDP fixes (9 Nov 2026)

Applies to the three Black Friday product pages, which all draw the top bar from the header section `muto-bf-head`:

| Page | Template |
|---|---|
| /products/muto-nad-cellular-complex | product.muto-nad-bf-premium |
| /products/muto-nad-cellular-complex-2 | product.muto-nad-bf |
| /products/muto-nad-cellular-complex-3 | product.muto-nad-bf-v3 |

Loaded into the unpublished theme **Clone Of Live | BF top bar fix [09-11]** (a duplicate of live, 9 Nov).

## 1. Top bar "Claim →" answers on the first tap
Why taps were dead (205 on url-3, 33 on the main page):
- The bar was a link to `#MainContent` and only became a Claim button once `muto-bf-claim.js` loaded (deferred, after everything else). Taps before that did nothing visible.
- Once loaded, a tap waited on three requests one after another (check cart, add, fetch side cart).
- The premium designs hide the spinner (`.mc-bfx__spin{display:none!important}`), so nothing on screen changed while it waited. Repeat taps were ignored as "busy".

Fix:
- `snippets/muto-bf-bar.liquid`: the link now goes to `/cart/add?id=<3-month variant>&quantity=1&selling_plan=<plan>`, so it works even before any script runs. The Claim script is inline, straight after the bar. The cart check runs in the background as the page loads, and the add returns the side cart's contents in the same request, so a tap needs one request. The bar switches to "Adding your Black Friday offer…" with a spinner the moment it's tapped. If nothing has happened in 6 seconds it falls back to the plain link.
- `assets/muto-bf-bar.css`: the tapped state, written to beat the premium CSS.
- `sections/muto-bf-head.liquid`: no longer loads `muto-bf-claim.js` (left in the theme, unused).

## 2. Buy box: socks label
`templates/*.json`: "Performance socks (UK 6–11)" → "Performance socks (one size fits all)".

## 3. Buy box: every welcome-kit item opens into a box
`snippets/muto-bf-kit-box.liquid` (rendered by `muto-bf-head`): tap an image tile, an itemised row or a later-delivery tile and a box opens with the photo large, the name, the value (struck through, Free) and the description (the image's alt text from the theme editor). Closes with ×, a tap outside or Esc. Keyboard accessible.
