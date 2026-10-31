# Science page, simplified (Timeline/AG1-style), Black Friday messaging

`theme/templates/page.science-simple.json` replaces the science page template (page `/pages/science`).
`theme/sections/muto-sci.liquid` is the new section ("MUTO — Science (simple)") with five layouts:
hero with stat cards, photo + story, photo + quote, statement + numbers, offer band.

Page order: hero (NAD+ +51% NR study, Energy, Recovery) · why you feel it · founder quote ·
comparison (the BF page's, swapped in by `muto-bf-head.liquid` into the empty `compare` slot) ·
standards (19 / 300mg / 7 / 4) · scientific board (existing section) · research · Black Friday band ·
reviews (existing section). Every claim is one MUTO already makes: the NR study is labelled as NR
on its own, not MUTO; health claims are the authorised wording.

`live-snapshot/` holds the template it replaced.
