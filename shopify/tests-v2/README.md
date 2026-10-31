# Third-party testing pop-up: clinical restyle

`theme/sections/muto-test-results.liquid`: the same markup, content and behaviour, with a new style block.
It reads like a lab report: a mono "Certificate of analysis" label in the header, the product name in normal
case, the batch as a mono reference, a white side menu with a thin bar on the open tab (underlined tabs on
phones), normal-case headings, results and limits in tabular mono, PASS as a small teal badge, hairline rules,
a 10px radius and a soft blurred backdrop. The product page's "View third-party testing results" button tick
is quietened to match. Applies everywhere the pop-up opens. `live-snapshot/` holds the original.
