# Our standards page (draft, 20 Oct 2026)

Built from `MUTO_Our_Standards_Page_Copy_Oct26.docx`, kept deliberately simple (seven sections) with the main site's own sections:

| Part | Theme section |
|---|---|
| Opening statement | About statement band |
| 19 · 100% · 90 | Home page numbers |
| Our ten standards | About "Research in progress" list (name and one line each) |
| Rules vs MUTO | Product-page comparison table |
| Founder's note | About founder portrait and letter card (shortened) |
| Questions | Product-page FAQ (five questions) |
| Close | "Above the standard. Beneath the surface." banner |

The doc's five jobs, scientists and check-it-yourself sections are left out; the ingredients and About pages cover them.

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
- **Links:** "See the full label…" points to `/pages/ingredients`, which is also still hidden.
- **Going live:** copy `templates/page.standards.json` to the live theme, then set the page to Visible.
