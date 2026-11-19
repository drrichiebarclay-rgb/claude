# Welcome kit worth £72, not £87, on every page (19 Nov 2026)

The main product page was corrected earlier (see `../pdp-cro`). This fixes the same figure everywhere else.

- `live/` the live theme's files as fetched on 19 Nov: every template, the header and footer groups, and the two sections involved.
- `theme/` the 16 files that said £87, with only that figure changed. On the duplicate theme "Clone Of Live | PDP CRO audit [19-11]" (ID 205307445595). Not on live.
- `apply.py` rebuilds `theme/` from `live/`; it stops if it meets an £87 that is not the kit worth.

| File | Where the figure shows |
|---|---|
| `templates/index.json` | Home page: the Black Friday bar in the header (text and screen-reader label) and the offer card |
| `sections/muto-sci.liquid` | The offer card's "£1.10 a day · free welcome kit worth…" line on every page that has the card. Now reads the shared value in `snippets/muto-offer.liquid` |
| `sections/faq-schema.liquid` | FAQ page: the question-and-answer data search engines read |
| `templates/page.faq-new.json` | FAQ page: the pricing answer and the offer card |
| `templates/page.about-us.json`, `page.ingredients.json`, `page.science-simple.json`, `page.standards.json` | Offer card |
| `templates/product.muto-bottle.json`, `product.muto-creatine.json`, `product.muto-socks.json` | Offer card on those product pages |
| `templates/product.muto-nad-bf.json`, `product.muto-nad-bf-premium-2.json`, `product.muto-nad-bf-lsttesta.json`, `product.muto-nad-bf-lsttestb.json`, `product.muto-nad-trust.json` | Other NAD+ product page versions: plan details, offer box and in-page bar |

`sections/muto-sci.liquid` needs `snippets/muto-offer.liquid`, which is already on live.

Not covered: sections and snippets outside the ~120 fetched for the product page work plus the files above were not searched.
