# MUTO FAQ page (/pages/faqs) — October 2026 rewrite

Source: `MUTO_FAQ_Rewrite_Oct2026.docx` (49 questions, 8 categories).

- `faq_content.py` — all page copy (questions, answers, ingredients table, intro, byline, closing notes).
- `build.py` — generates the theme files below from `faq_content.py`, so the FAQPage JSON-LD always matches the visible answers.
- `theme/templates/page.faq.json` — the page template: banner (H1 + intro), byline, sticky category jump links, one Custom FAQs section per category (H2 with anchor id, H3 questions in `<details>` accordions rendered server-side), JSON-LD section.
- `theme/sections/custom-faqs.liquid` — existing section plus an `anchor_id` setting and an optional `content_html` block field (used for the real HTML ingredients table).
- `theme/sections/faq-schema.liquid` — one FAQPage JSON-LD block.
- `live-snapshot/page.faq.json` — the live template before this rewrite, for rollback/reference.

Category anchors: `#about`, `#ingredients`, `#results`, `#guarantee`, `#safety`, `#how-to-take`, `#orders`, `#nad-explained`.

Rebuild after editing copy: `python3 build.py`, then upload the three `theme/` files to the theme.
