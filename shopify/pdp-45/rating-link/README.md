# -2 product page: rating links to the reviews

The "★★★★★ Rated 4.83 out of 5" line in the buy box on /products/muto-nad-cellular-complex-2 now links to the reviews section further down the page (the reviews.io widget, `#ReviewsWidget`), with a smooth scroll.

## Files for the live theme (`live/`)

Built from the live theme's own copies, taken on 17 October 2026, so your latest edits are kept.

| File | Change |
|---|---|
| `sections/muto-crea-buy.liquid` | New optional setting **Rating link**. When it has a value, the star row and rating text become a link. Without a value, nothing changes, so the other product pages that use this section are unaffected. |
| `templates/product.muto-nad-45.json` | Sets Rating link to `#ReviewsWidget` on the -2 page. Nothing else changed. |

Copy the section first, then the template. Or, after copying the section, set it in the theme editor instead: -2 page → buy box → Rating link → `#ReviewsWidget`.

To do the same on another product page, set its Rating link to `#ReviewsWidget`, as long as that page has the reviews.io section.

`preview/` holds the same change applied to the preview theme's (older) copies; it's already uploaded there.
