# Our standards page (draft, 20 Oct 2026)

Built from `MUTO_Our_Standards_Page_Copy_Oct26.docx` with the existing MUTO landing-page sections (`muto-lp-*`), so it uses the same type, colours and components as the landing pages. No new section files.

- **Template:** `templates/page.standards.json` (run `python3 build.py` to rebuild after copy edits).
- **Theme:** on the 3M refill plan draft theme (ID 202682564955) only.
- **Page:** "Our standards", handle `standards`, hidden, with the doc's SEO title and meta description.
- **New CSS:** a Custom Liquid block at the bottom of the template lets the trust strip hold five items (the section was built for three).

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
- **Photos:** the hero uses the welcome-kit shot. The doc asks for the jar with the label turned to camera; swap it in the hero's Photo setting. The founder card uses the existing founder photo.
- **Links:** "See the full label…" points to `/pages/ingredients`, which is also still hidden.
- **Going live:** copy `templates/page.standards.json` to the live theme, then set the page to Visible.
