# Science page, made simple (draft, 20 Oct 2026)

Built from `MUTO_Science_Page_Copy_Oct26.docx` in the same styles as the standards page (`muto-crea.css`).

- **Preview:** on the existing Science page with `?view=science-simple`, on the 3M refill plan draft theme (ID 202682564955). The current `page.science.json` is untouched.
- **Files:** `sections/muto-science-hero.liquid`, `sections/muto-chapter.liquid` (both new), `templates/page.science-simple.json` (run `python3 build.py`).
- **Navigation:** the six chapter links pin to the top once the hero scrolls away and highlight the chapter you're reading. If they slide under the theme's header, raise "Pinned chapter links: distance from top" in the hero.
- **Progress:** a thin cyan line under the chapter links shows how far through the page you are.
- **Board:** the home page's slim six-across cards (compact, 40px gap), straight after chapter 6.
- **Tables on phones:** three-column tables stack into labelled cards; the five-column comparison scrolls sideways with its first column pinned.
- **Chapters:** one "MUTO — Chapter" section each, with point, quote, step, table and glossary-term blocks. Chapter 1 has a simple NAD+-decline diagram and chapter 2 a draining-battery diagram, drawn in code.

## Not on the page yet: the doc's checks

- [ ] Every form and dose against the live label (including which B vitamins are in the formula).
- [ ] One regulatory read of chapters 2, 3 and 6.
- [ ] The NR study line stays word for word ("That study tested NR on its own, not MUTO").
- [ ] Research dates and partners, as on the standards page.
- [ ] Richie signs off every analogy (courier, relay runner, recycling loop, exhaust) and the "from your mid-30s" framing.
- [ ] Every "Not usually included" / "Not required by law" cell in chapter 5, with a regulatory adviser.
- [ ] Board: the rail under chapter 6 is the About page's six (James Morehen, Alka Patel, Richard Mackenzie, Maciej Zatonski, Ash Kapoor, Jamie Paweleck). The doc lists Mitch Naughton and not Jamie Paweleck, and gives different specialisms; confirm who's on it, with written sign-off, and the doc's one-line "what they bring" for each.

## Going live

Copy the two sections, then the template. Either assign `science-simple` to the Science page, or rename the template to `page.science.json` to replace the current one.
