# Our standards page (draft, 20 Oct 2026)

Built from `MUTO_Our_Standards_Page_Copy_Oct26.docx`, laid out after the AG1 quality-standards page in MUTO's own styles (`muto-crea.css`: teal ink, sage, cyan buttons, Neue Haas Grotesk, Sometype Mono).

| Part | Section |
|---|---|
| Headline, intro, ten standards (list left, selected fills teal; promise, "how to check" and two photos right) | `sections/muto-standards.liquid` (new) |
| Customer videos | `muto-home-results`, copied from the product page |
| Start your 90 days: photo left, teal panel itemising the first order | `sections/muto-get-started.liquid` (new) |
| Five questions | `muto-crea-faq` |

Photos on the standards reuse existing site images as stand-ins; swap them in each standard's Photo 1 / Photo 2. Prices in the panel are typed (monthly plan, £60 and the £62 kit), so keep them in step with Skio.

- **Template:** `templates/page.standards.json` (run `python3 build.py` to rebuild after copy edits).
- **Theme:** on the 3M refill plan draft theme (ID 202682564955) only.
- **Page:** "Our standards", handle `standards`, hidden, with the doc's SEO title and meta description.
- **New sections:** copy `sections/muto-standards.liquid` and `sections/muto-get-started.liquid` before the template.

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
- **Going live:** copy the two sections, then `templates/page.standards.json`, to the live theme, then set the page to Visible.
