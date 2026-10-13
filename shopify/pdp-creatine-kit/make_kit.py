"""Clone a NAD+ product template with creatine added to the welcome kit.

Usage: python3 make_kit.py <base template> <out template> <normal|simple>
Adds a creatine gift as the first welcome-kit tile and updates the first-order reassurance row.
"""
import json
import sys

src, out, tone = sys.argv[1:]
raw = open(src).read()
head, d = raw[: raw.index("{")], json.loads(raw[raw.index("{"):])
buy = d["sections"]["buy"]
IMG = "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-creatine.jpg?v=1791022787"

buy["blocks"]["k0"] = {"type": "gift", "settings": {
    "value": "£30",
    "name": "Micronised Creatine" if tone == "normal" else "Creatine",
    "image_fallback": IMG,
    "image_alt": "A pouch of MUTO Ultrapure Micronised Creatine Monohydrate, part of the welcome kit",
    "plans": "",
}}
order = buy["block_order"]
assert "k0" not in order
order.insert(order.index("k1"), "k0")

buy["blocks"]["term_3"]["settings"]["text"] = (
    "Free with your first order: Ultrapure Micronised Creatine Monohydrate, performance socks, Forever Jar, 12-week protocol guide"
    if tone == "normal" else
    "Free in your first box: creatine, socks, a jar and a guide"
)
# Itemised "includes" list above the kit images
st = buy["settings"]
if tone == "normal":
    st.update({"kit_title": "Your first order includes:", "kit_itemised": True,
               "kit_main": "NAD+ Cellular Complex", "kit_main_note": "Included",
               "kit_foot_1": "90-day money-back guarantee", "kit_foot_2": "Free next-day delivery",
               "kit_foot_3": "Skip or cancel anytime"})
    labels = {"k0": "Ultrapure Micronised Creatine", "k1": "Performance Socks (Size UK 6-11)", "k2": "Forever Jar",
              "k3": "12-Week Protocol Guide", "k4": "Chance to win a Garmin Watch"}
else:
    st.update({"kit_title": "Your first box includes:", "kit_itemised": True,
               "kit_main": "NAD+ Cellular Complex", "kit_main_note": "Included",
               "kit_foot_1": "Money back for 90 days", "kit_foot_2": "Free delivery",
               "kit_foot_3": "Stop any time"})
    labels = {"k0": "Creatine", "k1": "Socks (Size UK 6-11)", "k2": "Jar to keep", "k3": "12-week guide",
              "k4": "Chance to win a Garmin Watch"}
for bid, label in labels.items():
    buy["blocks"][bid]["settings"]["row_label"] = label
buy["blocks"]["k4"]["settings"]["row_note"] = "Free entry"
# Giveaway prize is now a Garmin Watch (caption under the kit image)
buy["blocks"]["k4"]["settings"].update({
    "value": "Garmin Watch", "name": "giveaway entry",
    "image_fallback": "https://cdn.shopify.com/s/files/1/0976/2724/2843/files/gift-garmin.jpg?v=1791883127",
    "image_alt": "A white Garmin watch, the giveaway prize in the welcome kit",
})
buy["blocks"]["k4"]["settings"].pop("image", None)

# The ticked reassurance rows go: the itemised list now carries that message
terms = [b for b in buy["block_order"] if buy["blocks"][b]["type"] == "term"]
for b in terms:
    del buy["blocks"][b]
buy["block_order"] = [b for b in buy["block_order"] if b not in terms]

# "Skip or cancel anytime" opens a pop-up
if tone == "normal":
    st.update({"kit_foot_3_pop_title": "Skip or cancel anytime",
               "kit_foot_3_pop": "<p>Going on holiday or running low? Skip a delivery, delay your next order, or cancel whenever you want, before your next charge. Total control, zero pressure.</p>"})
else:
    st.update({"kit_foot_3_pop_title": "Stop any time",
               "kit_foot_3_pop": "<p>Going on holiday or running low? Skip a box, move your next order, or stop whenever you want, before your next payment. You’re in control.</p>"})

# "90-day money-back guarantee" opens a pop-up
if tone == "normal":
    st.update({"kit_foot_1_pop_title": "90-day money-back guarantee",
               "kit_foot_1_pop": ("<p><strong>No risk.</strong> Take MUTO every day for 90 days. If you don’t see a difference, "
                                  "we’ll refund every subscription payment you made in that time, less delivery costs.</p>"
                                  "<p>Fewer than 0.1% of customers ask for their money back.</p>"
                                  "<p>For first-time subscribers at muto.co. Just email us within 14 days after your 90 days end. "
                                  "<a href=\"/pages/faqs#guarantee\">Full details</a></p>")})
else:
    st.update({"kit_foot_1_pop_title": "Money back for 90 days",
               "kit_foot_1_pop": ("<p><strong>No risk.</strong> Take it every day for 90 days. Not for you? Email us within 14 days after your 90 days end. "
                                  "We’ll give your money back, minus delivery.</p>"
                                  "<p>Fewer than 1 in 1,000 people ask for a refund.</p>"
                                  "<p><a href=\"/pages/faqs#guarantee\">Full details</a></p>")})

# "No commitment" opens a pop-up (phones only, as a fourth footer point)
if tone == "normal":
    st.update({"kit_foot_4": "No commitment", "kit_foot_4_pop_title": "No commitment",
               "kit_foot_4_pop": "<p>You’re never locked in. Pause, restart or cancel your MUTO plan at any time, directly from your account. No questions asked.</p>"})
else:
    st.update({"kit_foot_4": "No contract", "kit_foot_4_pop_title": "No contract",
               "kit_foot_4_pop": "<p>You’re never tied in. Pause, start again or stop your plan whenever you like, from your account. No questions asked.</p>"})

# Gallery follows the product images in Shopify admin
st["gallery_from_product"] = True

# One claim window everywhere: 14 days after the 90 days end
q4 = d["sections"]["faq"]["blocks"]["q4"]["settings"]
for old in ("within 90 days of your first order", "within 104 days of your first order"):
    q4["text"] = q4["text"].replace(old, "within 14 days after your 90 days end")
assert "14 days after your 90 days end" in q4["text"], q4["text"]

open(out, "w").write(head + json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("written", out)
