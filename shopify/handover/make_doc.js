// Builds MUTO_Home_and_PDP_dev_handover.docx: node make_doc.js
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, LevelFormat, AlignmentType, ExternalHyperlink,
} = require("docx");

const INK = "162F31", MUTED = "5C6B6C", MINT = "E6ECEA", HAIR = "C8D2CF";
const FONT = "Arial";
const W = 9638; // A4 text width at 2cm margins (11906 - 2*1134)

const t = (text, o = {}) => new TextRun({ text, font: FONT, size: 21, color: INK, ...o });
const code = (text) => new TextRun({ text, font: "Consolas", size: 19, color: INK });
const P = (runs, o = {}) => new Paragraph({ spacing: { after: 120, line: 300 }, children: Array.isArray(runs) ? runs : [t(runs)], ...o });
const H1 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 160 }, children: [new TextRun({ text: s, font: FONT, size: 32, bold: true, color: INK })] });
const H2 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 }, children: [new TextRun({ text: s, font: FONT, size: 25, bold: true, color: INK })] });
const B = (runs, level = 0) => new Paragraph({ numbering: { reference: "bul", level }, spacing: { after: 80, line: 290 }, children: Array.isArray(runs) ? runs : [t(runs)] });
const N = (runs, ref = "num") => new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 100, line: 290 }, children: Array.isArray(runs) ? runs : [t(runs)] });
const link = (text, url) => new ExternalHyperlink({ link: url, children: [new TextRun({ text, font: FONT, size: 21, color: "1F6F7C", underline: {} })] });
const note = (runs) => new Paragraph({
  spacing: { before: 120, after: 160, line: 290 },
  shading: { type: ShadingType.CLEAR, fill: MINT, color: "auto" },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: INK, space: 8 } },
  indent: { left: 160, right: 160 },
  children: Array.isArray(runs) ? runs : [t(runs)],
});

const border = { style: BorderStyle.SINGLE, size: 4, color: HAIR };
const borders = { top: border, bottom: border, left: border, right: border };
function table(widths, head, rows) {
  const cell = (content, w, isHead) => new TableCell({
    width: { size: w, type: WidthType.DXA }, borders,
    shading: isHead ? { type: ShadingType.CLEAR, fill: INK, color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: [new Paragraph({ children: (Array.isArray(content) ? content : [content]).map(c =>
      typeof c === "string" ? (isHead ? new TextRun({ text: c, font: FONT, size: 18, bold: true, color: "FFFFFF" }) : t(c, { size: 18 })) : c) })],
  });
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: head.map((h, i) => cell(h, widths[i], true)) }),
           ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, widths[i], false)) }))],
  });
}
const c = (s) => [new TextRun({ text: s, font: "Consolas", size: 17, color: INK })];

const DRAFT = "Clone Of Live | 3M refill plan (theme ID 202682564955)";
const LIVE = "Clone Of Live | Buy Box Redesign [31-08] (theme ID 200736047451, the published theme)";

const children = [
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "MUTO", font: FONT, size: 20, bold: true, color: MUTED, characterSpacing: 40 })] }),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "Home page and new product page: developer handover", font: FONT, size: 44, bold: true, color: INK })] }),
  P([t("21 October 2026. Everything below is built and reviewed on the draft theme. This document covers what to copy to the live theme, in what order, and how to check it.", { color: MUTED })]),

  H1("1. Summary"),
  B([t("New product page", { bold: true }), t(" for NAD+ Cellular Complex becomes the main page at "), code("/products/muto-nad-cellular-complex"), t(".")]),
  B([t("The current product page", { bold: true }), t(" stays available as a second URL: "), code("/products/muto-nad-cellular-complex?view=2"), t(".")]),
  B([t("Home page", { bold: true }), t(" copy updated to match the new product, science and ingredients pages. Template-only change.")]),
  note([t("Both changes are made by copying files from the draft theme to the live theme, then switching the product's template. No app, checkout or Skio changes. Prices, plans, gifts and selling plans all come from the existing product and are unchanged.")]),

  H2("Themes"),
  table([2200, 7438], ["Theme", "Name"], [["Draft (source)", DRAFT], ["Live (target)", LIVE]]),
  P(""),
  H2("Preview links"),
  B([t("New product page: "), link("muto.co/products/muto-nad-cellular-complex?view=muto-nad-v2&preview_theme_id=202682564955", "https://muto.co/products/muto-nad-cellular-complex?view=muto-nad-v2&preview_theme_id=202682564955")]),
  B([t("Home page: "), link("muto.co/?preview_theme_id=202682564955", "https://muto.co/?preview_theme_id=202682564955")]),

  H1("2. New product page"),
  H2("What's on the page, top to bottom"),
  table([2600, 2700, 4338], ["Section", "File", "Notes"], [
    ["Buy box", c("muto-pdp-v2-buy"), "Copy of the live buy box (muto-crea-buy) with new intro copy, a 'How it helps' list, a delivery line, three badges, a guarantee panel, a test results button, a doctors link, rewritten accordions and two short lists. Same product form, plans and Skio behaviour."],
    ["Section links", c("muto-section-nav"), "Pinned row of chips under the buy box. Highlights the section on screen; tapping jumps to it."],
    ["Benefits", c("muto-benefit-cards"), "Five photo cards (Energy, Recovery, Stress, Longevity, Immunity). 'View supplement facts' opens the test results panel on its Formula tab."],
    ["Meet the experts", c("muto-home-board"), "Existing section, slim cards."],
    ["Ingredients", c("muto-ingredient-library"), "Filterable 19 ingredients with a click-to-open drawer."],
    ["Comparison", c("muto-chapter"), "MUTO vs multivitamin, greens and collagen."],
    ["What to expect", c("muto-timeline"), "Day 1, 30, 60, 90 with a pinned photo."],
    ["How to take it", c("muto-chapter"), "Three photo steps."],
    ["FAQs", c("muto-crea-faq"), "Existing section, ten rewritten questions."],
    ["Reviews", c("custom-reviews"), "Existing REVIEWS.io widget, at the bottom."],
    ["Test results panel", c("muto-test-results"), "Hidden until opened. Batch 2333 certificate: tests, results, formula."],
    ["Sticky bar, easy read", c("muto-home-sticky, custom-liquid"), "As on the current product page."],
  ]),

  H2("Files to copy from the draft theme to the live theme"),
  P("Copy each file's full contents from the draft theme (Online Store, Themes, ... , Edit code) into the live theme. Then check the MD5 matches, if your tooling shows it."),
  table([4100, 1500, 4038], ["File", "Status on live", "Draft MD5"], [
    [c("sections/muto-pdp-v2-buy.liquid"), "New", c("fda18a2a3fe8257933d58615d621c6ca")],
    [c("sections/muto-section-nav.liquid"), "New", c("d5ee3ad05304552f85f0f851c2db21d9")],
    [c("sections/muto-benefit-cards.liquid"), "Replace (older)", c("612ba8b6308cdb1810431444fcbb43f1")],
    [c("sections/muto-timeline.liquid"), "Replace (older)", c("fb2bbb18c3df0f6f561dc8b46a3d5e07")],
    [c("sections/muto-chapter.liquid"), "Replace (older)", c("91874848ee7bf36fed8057612c9b9fe6")],
    [c("sections/muto-test-results.liquid"), "Replace (older)", c("13ffbb9cdd2f83d3f8587dad0f596544")],
    [c("sections/muto-ingredient-library.liquid"), "Replace (older)", c("1ce354bd17bc9a8747985346dcbea923")],
    [c("templates/product.muto-nad-v2.json"), "New", c("d00581eb00a23646187e73db8b63b2dc")],
  ]),
  P(""),
  note([t("Do not touch ", { bold: true }), code("sections/muto-pdp-buy.liquid"), t(" on the live theme. It is an older landing-page buy box that other templates use. The new buy box was named "), code("muto-pdp-v2-buy"), t(" so the two can't collide.")]),
  P([t("Already on live and identical, so nothing to copy: "), code("muto-crea-faq"), t(", "), code("muto-home-board"), t(", "), code("custom-reviews"), t(", "), code("muto-crea.js"), t(", "), code("muto-home.js"), t(", "), code("snippets/muto-image"), t(", "), code("snippets/muto-crea-faq-schema"), t(".")]),

  H2("Pages the shared sections also feed"),
  P([t("Four of the sections above are shared with the science, ingredients and standards pages, which were copied to live this morning in older versions. Replacing those sections without the matching templates can leave those pages out of step. Copy these too, at the same time:")]),
  table([4100, 5538], ["File", "Draft MD5"], [
    [c("templates/page.science-simple.json"), c("740efaea150f6e13cde14a42922bdbc3")],
    [c("templates/page.ingredients.json"), c("6c231a032a2f3ef70c8c57c14d21cc75")],
    [c("templates/page.standards.json"), c("75a7233bc799a949fc3ffb7890d9cb86")],
    [c("sections/muto-science-hero.liquid"), c("f3fd54bf5316623b2f4a5e4737e8a97e")],
    [c("sections/muto-get-started.liquid"), c("7851d48b70f9bdd3c9ebb98e6dc7a35e")],
    [c("sections/muto-standards.liquid"), c("0e2fa8d3beab87a7a2057da91c8d3f25")],
  ]),

  H2("Make it the main page, and keep the current one at URL 2"),
  P([t("The product "), t("NAD+ Cellular Complex", { bold: true }), t(" ("), code("muto-nad-cellular-complex"), t(") currently uses template "), code("product.muto-nad-45"), t(".")]),
  N([t("On the live theme, create "), code("templates/product.2.json"), t(" as an exact copy of "), code("templates/product.muto-nad-45.json"), t(". The current page is then always reachable at "), code("?view=2"), t(".")]),
  N([t("Check "), code("/products/muto-nad-cellular-complex?view=2"), t(" shows the current page, buy box included, and add one item to cart.")]),
  N([t("Check "), code("/products/muto-nad-cellular-complex?view=muto-nad-v2"), t(" shows the new page on live, and add one item to cart on each plan.")]),
  N([t("In Shopify admin, Products, NAD+ Cellular Complex, Theme template: change "), code("muto-nad-45"), t(" to "), code("muto-nad-v2"), t(" and save.")]),
  N([t("Check "), code("/products/muto-nad-cellular-complex"), t(" now shows the new page.")]),
  note([t("To roll back, set the product's template back to "), code("muto-nad-45"), t(". Nothing else needs undoing.")]),
  P([t("Ads, emails or tests that should keep sending traffic to the current page can link to "), code("?view=2"), t(". Leave "), code("product.muto-nad-45.json"), t(" in place; don't rename or delete it.")]),

  H1("3. Home page"),
  P([t("One file: "), code("templates/index.json"), t(" (draft MD5 "), code("98a32f166c4f50cdd426fe38083f7d59"), t("). No section code changes. The live "), code("index.json"), t(" is identical to the draft's before these edits (MD5 "), code("9d6337adb7c69d352f746b8cbb254bdd"), t("), so the draft version can replace it as is. If live has been edited since, merge the changes listed below instead.")]),
  H2("What changed"),
  table([2500, 7138], ["Section", "Change"], [
    ["Hero", "Subheading: 'Not another multivitamin. The next generation of one: 19 ingredients for energy, recovery, a clearer head, ageing well and immunity, in two capsules a day. 90 days to feel the difference.'"],
    ["Shop the protocol (NAD+ tab)", "Lede: 'Not another multivitamin. The next generation of one.' Three steps rewritten (Built for life after 35; One jar, nothing hidden; 90 days to decide), with links to /pages/science and /pages/ingredients."],
    ["Founder", "One paragraph: 'still working, keeping up with family' in place of 'still training'."],
    ["Scientific board", "Heading: 'Meet the experts behind MUTO.'"],
    ["Where you'll feel it (NAD+ tab)", "Six rows, matching the product page: Energy, Recovery, Mind, Ageing well, Immunity, Simplicity. Lede links to /pages/ingredients."],
    ["Benefits photo", "New style-only section benefits_css pins the photo while the rows scroll (desktop, 990px and up)."],
    ["The science: NAD+ (all five tabs)", "What it does, How it works, Formula, Who it's for, Protocol rewritten to match the science and ingredients pages, with links to /pages/science, /pages/ingredients and /pages/standards."],
    ["Unchanged", "Creatine and essentials tabs, athletes, banner, stats, sticky bar."],
  ]),
  P(""),
  note([t("The links go to "), code("/pages/science"), t(", "), code("/pages/ingredients"), t(" and "), code("/pages/standards"), t(". Ingredients and standards are hidden pages and the science page uses the "), code("science-simple"), t(" view. Before the home page goes live, publish those pages and point each one at its new template, or the links will 404 or show the old science page.")]),

  H1("4. QA checklist"),
  B("Desktop (1440px) and phone (390px), Chrome and Safari."),
  B("Product page: add to cart on the monthly plan, the 3-month plan and one-time. The cart drawer opens with the right variant and selling plan."),
  B("Sticky add-to-cart bar appears after the buy box and adds the selected plan."),
  B("Section links pin under the header, highlight the right chip and jump to each section."),
  B("'View third-party testing results', 'View supplement facts' and 'Ingredients + nutritional information' open the test results panel (the last two on its Formula tab)."),
  B("Ingredient cards open the drawer; filters work; Escape closes it."),
  B("FAQ answers open; reviews widget loads at the bottom."),
  B("?view=2 still shows and sells the current page."),
  B("Home page: tabs switch on Shop the protocol, Where you'll feel it and The science; every new link resolves."),

  H1("5. Before going live: content checks"),
  B([t("'Third-party tested'.", { bold: true }), t(" The test results come from the manufacturer's certificate of analysis for batch 2333, signed by its technical team. Confirm an independent lab ran the tests before the button and copy say 'third-party'.")]),
  B([t("Benefit lines.", { bold: true }), t(" The 'How it helps' and benefit card lines are written for tone, not in UK-authorised claim wording. Have them reviewed if you have a claims reviewer.")]),
  B([t("Scientific board.", { bold: true }), t(" The board shows six members, including Dr Jamie Paweleck; the science copy doc lists Mitch Naughton. Confirm who should appear.")]),

  H1("6. Source"),
  P([t("Built from scripts in the repository "), code("drrichiebarclay-rgb/claude"), t(", branch "), code("claude/dazzling-darwin-ng8dx0"), t(": "), code("shopify/pdp-v2/build.py"), t(" (product page) and "), code("shopify/home-page/build.py"), t(" (home page). Changes made in the theme editor were merged into these scripts, so rebuilding keeps them.")]),
];

const doc = new Document({
  creator: "MUTO", title: "Home page and new product page: developer handover",
  styles: { default: { document: { run: { font: FONT, size: 21, color: INK } } } },
  numbering: { config: [
    { reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
    { reference: "num", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
  ] },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } }, children }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(__dirname + "/MUTO_Home_and_PDP_dev_handover.docx", b); console.log("ok"); });
