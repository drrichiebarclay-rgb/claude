# Live-ready theme files (13 Oct 2026)

Copy every file here into the live theme (Clone Of Live | Buy Box Redesign [31-08]) at the same path: **sections first, then templates**.

Every template here was rebuilt from a snapshot of the LIVE theme taken on 13 Oct (`live-snapshot-13oct/`), with only the 13 Oct changes applied, so edits made directly on live are kept. Rebuild with `python3 live-ready/rebuild_from_live.py` (run from `shopify/`) after refreshing the snapshot.

- `sections/muto-crea-compare.liquid`: live file plus an optional **Density: Compact** setting, **Group label** blocks and an inline MUTO wordmark on mobile. Defaults are unchanged.
- `sections/faq-schema.liquid`, `templates/page.faq-new.json`: one FAQ answer now mentions the Garmin watch draw.
- `templates/product.give-away.json`: entry form heading and description for the Garmin watch.
- `templates/product.muto-nad.json`, `product.muto-nad-simple.json`, `product.muto-nad-creatine-kit.json`: Garmin giveaway tile and text, and the new comparison table ("The smarter way to buy NAD⁺").

Full list of changes: see `handoff/MUTO_Dev_Handoff_13Oct2026.docx`.
