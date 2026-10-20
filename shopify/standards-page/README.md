# Our standards page (draft, 20 Oct 2026)

Built from `MUTO_Our_Standards_Page_Copy_Oct26.docx` with the main site's own sections, the ones the About, home and product pages use (`muto-about-*`, `muto-home-*`, `muto-crea-*`). Hero, board and banner settings are copied from the About template (`theme-ref/`), so imagery and behaviour match. No new section files.

| Doc section | Theme section |
|---|---|
| 1 Hero, subhead, proof strip | About hero (poster, two actions, plan strip and sticky bar), About statement, About "made" cards |
| 2 Why we built it | About founder (portrait and letter card) |
| 3 Rules vs MUTO | Product-page comparison table (MUTO vs required by UK law) |
| 4 Ten standards | Product-page FAQ rows, each with "How to check" |
| 5 Five jobs | Product-page benefits rows beside the label photo |
| 6 Scientists | The board rail with interview videos |
| 7 Check us yourself | About "proof" steps |
| 8 Questions | Product-page FAQ |
| 9 Closing | "Above the standard. Beneath the surface." banner |

- **Template:** `templates/page.standards.json` (run `python3 build.py` to rebuild after copy edits).
- **Theme:** on the 3M refill plan draft theme (ID 202682564955) only.
- **Page:** "Our standards", handle `standards`, hidden, with the doc's SEO title and meta description.
- **New CSS:** a Custom Liquid block hides the comparison table's third and fourth columns, which this page doesn't use.

## Not on the page yet: the doc's [Confirm …] notes

- [ ] Every "Required by UK law? No" line (section 3), with a regulatory adviser.
- [ ] What each batch is tested for (standard 4), so the page can name it.
- [ ] Every form and dose against the live label (section 5), including whether B2 is in the formula.
- [ ] Every ingredient authorised for UK food supplements (standard 3).
- [ ] Board members' names, photos and specialisms, with written sign-off (section 6). The cards reuse the live landing pages' board cards.
- [ ] Research dates: Westminster December 2026; King's, Coventry and Newcastle timings.
- [ ] Certificates on request is still the policy.
- [ ] No Informed Sport until the certificate is live; then add it as standard 11.

## Also before going live

- **URL:** Shopify pages live at `/pages/standards`. For `muto.co/standards`, add a URL redirect `/standards` → `/pages/standards` (Online Store → Navigation → URL redirects).
- **Photos:** the hero uses the About poster. The doc asks for the jar with the label turned to camera; swap it in the hero's Photo setting if you'd rather.
- **Links:** "See the full label…" points to `/pages/ingredients`, which is also still hidden.
- **Going live:** copy `templates/page.standards.json` to the live theme, then set the page to Visible.
