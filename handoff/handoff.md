---
title: "MUTO site changes: dev handoff"
subtitle: "10 October 2026"
---

All changes are saved on the unpublished theme **Clone Of Live | 3M refill plan**. To ship them, copy 13 files into the live theme. Two of them are prepared copies that leave out the unreleased 3M refill plan work.

# Before you start

- **Copy from:** the folder `shopify/live-ready` in GitHub (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`): <https://github.com/drrichiebarclay-rgb/claude/tree/claude/faq-page-shopify-redesign-hbqcg8/shopify/live-ready>. It holds all 13 files at their theme paths.
- **Copy to:** the live theme, Clone Of Live | Buy Box Redesign [31-08] (ID 200736047451). Sections first, then templates, or a template save fails on settings its section doesn't have yet.
- **Don't publish the 3M refill plan theme to ship these changes**, and don't copy `templates/product.muto-nad.json` or `sections/muto-crea-buy.liquid` from it. That theme also holds the unreleased 3M refill plan: a "90 Day Protocol £135" plan card, an empty "Hidden plans" setting (live hides the 3-month subscription), a £1.83/day note on the monthly card (live says £2/day) and new plan-picker code.
- **How the folder was made:** I compared every file against live. 11 had no other changes, so the folder has the 3M refill plan theme's versions. The other 2 are the live files with only the changes listed here applied: the buy section is the live file plus 93 added lines, nothing removed.
- **To see everything working together:** preview the 3M refill plan theme (ID 202682564955) at <https://muto.co/?preview_theme_id=202682564955>.

# 11 files taken from the 3M refill plan theme

Copy the four sections first, then the seven templates.

| File | Page | What changed |
|---|---|---|
| `sections/muto-crea-ingredients.liquid` | NAD+ product page | New optional "Subheading" setting under the ingredients heading: line 1 as intro, later lines as a sage note box, with spacing above the tiles. Renders nothing when blank, so the creatine page is unaffected. |
| `sections/muto-home-board.liquid` | Home | New "Compact row" checkbox: all board members in one row on desktop, smaller swipeable cards on mobile. Off by default, so the product page board is unchanged. |
| `sections/muto-home-science.liquid` | Home, Muto Home | Restores the gap between a paragraph and a list in the science tabs (a theme list reset was removing it). |
| `sections/faq-schema.liquid` | FAQ | FAQPage JSON-LD regenerated from the final 54 questions. |
| `templates/index.json` | Home | Hero statement and supporting copy; every button reads "Start the protocol" with links unchanged (four NAD science tabs now link to the NAD+ product explicitly; creatine "Coming Soon" now links to /products/muto-creatine); Why MUTO pillars (founder photo on card 1); founder paragraph added; "Still training. Still working. Not done yet."; board note + compact row; numbers (4 university research partners, 6 advisors); "Where you'll feel it" benefits; NAD science tabs and "Shop the protocol" NAD+ tab rewritten; "What's inside" label. |
| `templates/page.muto-home.json` | /pages/muto-home | NAD science tabs and "Shop the protocol" NAD+ tab, same copy as home. Buttons and other sections not changed. |
| `templates/page.about-us.json` | /pages/about | Hero, plan, sticky, founder and banner buttons read "Start the protocol". "Donate Here" unchanged. |
| `templates/page.about-muto.json` | /pages/muto-about | Same button changes as /pages/about. "See the science" and "Donate Here" unchanged. |
| `templates/product.muto-bottle.json` | Bottle product page | "Shop the protocol" NAD+ tab: new subheader, three steps, "What's inside" label. |
| `templates/product.muto-socks.json` | Socks product page | Same as the bottle page. |
| `templates/page.faq-new.json` | FAQ (/pages/faqs uses template faq-new) | Final FAQ copy: 54 questions in 8 sections, ingredient table (CoQ10 form = Ubiquinone), byline dated 10 October 2026. |

# 2 prepared files: NAD+ product page

Both are the live files with these changes applied, and nothing else.

**`sections/muto-crea-buy.liquid`** (93 lines added, none removed)

- New "Review snippet" block type (quote + name), with an `assign snippets` line.
- Rendered under the Add to Cart button, before the accordions: a frosted-glass card showing one quote at a time, crossfading every 2 seconds, with clickable dots. It pauses on hover, keyboard focus and hidden tabs, and doesn't rotate for reduced-motion visitors. CSS and JS are inline in the block and only output when snippets exist, so the creatine page is unchanged.

**`templates/product.muto-nad.json`**, section by section:

| Section | Change |
|---|---|
| Buy box | Bullets: "Keep your energy all day, not just the morning" / "Bounce back from hard sessions like you used to" / "Stay the strong, capable one for longer" / "Feel the difference in 90 days, or your money back" |
| Buy box | Description: "For people who aren't ready to slow down… 90 days to decide for yourself." |
| Buy box | Reassurance rows replaced with 6: 90-day money-back guarantee · Free next-day delivery · First-order kit (socks, Forever Jar, 12-week guide) · Thank-you gift up to month 6 · Oura Ring 5 prize draw (T&Cs link to /pages/better-baseline-giveaway) · Skip, pause or cancel online with a 5-day reminder |
| Buy box | 9 review snippets added (Lynda, Alexandra, Adam H, Ayo P, Holly P, Danny S, Amy C, Mathew H, Rebeca), verbatim from REVIEWS.io |
| Buy box | "What the research shows" removed (4 stat blocks deleted, title and references cleared) |
| Buy box | "Why this?" note removed (title and text cleared) |
| Buy box | Accordion "How to Enjoy" renamed "How to take it" |
| The problem | Heading "You're not done yet. So why does it feel harder?" and new lede |
| Why MUTO | Card 1 "Built by a scientist you can talk to." with the founder photo (about-founder.jpg); card 2 adds "Ask your AI to check it."; card 3 day 0 / 30 / 90 copy |
| Scientific board | Note: "Our Scientific Advisory Board: scientists and clinicians in performance, metabolism and longevity." |
| Benefits | Heading "What people notice first" with "Individual experiences, not a promise."; all four sub-lines are verbatim review quotes (Lynda, Adam H, Becca, Jack); tab renamed "Ways to check" with 3 new items (weekly check-in, training log, wearable 30-day averages) |
| Real results | Note: "Ninety days, in their own words" |
| Ingredients | Heading "Nineteen ingredients. Every dose on the label."; subheading (30 trillion cells line + "Already taking D3, K2…" note); Produce / Protect / Put to work filter removed (all groups blank) |
| 90-day test | Heading "Not a quick fix. A 90-day test."; step 1 chip "Day 0" with new copy; step 4 "If it's not for you, you're covered." |
| FAQs | Added "Do I need a wearable?"; rewrote "When might I notice something?", "Is it safe with my other supplements?", "What if it's not for me?" (full guarantee terms) and "Why not just take NR on its own?" |

# Already live: no action

- **NAD+ product description** (Shopify admin → Products → NAD+ Cellular Complex) was rewritten on 10 Oct. It drops Produce / Protect / Put to Work and the HRV claim. The old text is in the repo at `shopify/product-description/previous-description.html`.

# Still open

Not in the 13 files. Most are copy decisions for Richie, not dev work.

- [ ] **Refund policy** (Settings → Policies) still describes a 30-day guarantee with a wearable export. Rewrite it to the FAQ terms: 90 days, first-time subscribers at muto.co, less delivery costs, claim within 104 days, wearable data optional.
- [ ] **"Full refund" wording** on the NAD+ product page: the "90-Day Money back Guarantee" accordion and the guarantee section say "in full". The FAQ says "less our delivery costs".
- [ ] **"Pre-Order Now - Arrives 15/10"** is hard-coded in the Add to Cart button in `muto-crea-buy.liquid`, not a setting. Remove it after 15 Oct.
- [ ] **"Feel it in days, your data proves it by day 30"** banner: not found in these templates yet. Align it to 60–90 days.
- [ ] **FAQ byline date** reads "Last updated 10 October 2026". Change it in the FAQ byline section if it goes live on another day.
- [ ] **Product search description** (SEO) still says "stress resilience".
- [ ] **"300+ supporting studies"** stat on the home page: flagged in the FAQ brief as unsupported.
- [ ] **/pages/muto-home** still has the old buttons ("Start your 90 days", "Start Today", "Coming Soon"), "seven scientists" and the "7 advisors" stat.
- [ ] **CoQ10 form on the home page:** the science Formula tab and "What's inside" say plain "CoQ10"; the FAQ table says Ubiquinone. Confirm whether the home page should say "(as ubiquinone)".
- [ ] **Socks and bottle buttons** read "Start the protocol" but link to their own product pages.
- [ ] **Claims review:** vitamin K2 sits under the immunity and muscle claims in the science Formula tab, product description and FAQ, but has no authorised claim for either. The TMG line in the Formula tab is new wording to check.
- [ ] **Informed Sport:** swap the drug-tested athletes FAQ answer when certification is live (the certified wording is in MUTO_FAQ_Page_Final_Oct26.docx).

# Check after publishing

1. **NAD+ product page:** the plan cards match today's live plans (no 90 Day Protocol card). The review card rotates under Add to Cart. No research stats or "Why this?" box.
2. **Home:** every button says "Start the protocol" and lands on the right product. The board is one row on desktop and swipes on mobile.
3. **FAQ (/pages/faqs):** 54 questions in 8 sections, the jump bar sticks, the ingredient table scrolls sideways on mobile, and no "Ubiquinol" anywhere.
4. **Search markup:** run /pages/faqs through Google's Rich Results Test (<https://search.google.com/test/rich-results>). It should find one FAQPage with 54 questions.
5. **About pages (/pages/about, /pages/muto-about):** buttons say "Start the protocol".
