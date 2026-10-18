---
title: "MUTO product pages: Black Friday pre-sale box"
subtitle: "18 October 2026"
---

A new box above the plan boxes on the product pages. **It's one paste on each of 2 product templates, plus a Shopify Flow.** Nothing else on the pages changes.

# Before you start

- **File:** `black-friday-presale-box.liquid`, in `MUTO_BF_Presale_Box.zip` and also in GitHub at `handoff/bf-presale/` (repo drrichiebarclay-rgb/claude, branch `claude/faq-page-shopify-redesign-hbqcg8`).
- **Preview:** it's already on the 3M refill plan theme (ID 202682564955):
  - <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=202682564955>
  - <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=202682564955>

# Step 1: paste the box into both templates

On the live theme, open **Customize**. Then for **each** of the templates `product.muto-nad-45` and `product.muto-nad-performance`:

1. Open a product that uses the template.
2. Select the **Custom Liquid** section at the bottom of the page, the one called `easy_read`.
3. Paste the whole of `black-friday-presale-box.liquid` at the **end** of what's already there. Don't replace the existing code.
4. Save.

# Step 2: the Shopify Flow

The "kits left" number comes from a shop metafield, `muto.bf_boxes_left`. **It's already created and set to 92**, the real pre-Black Friday allocation. To edit it: Settings → Custom data → Shop → "Black Friday welcome kits left". If the field is blank, the line is hidden.

To lower the number by 1 for each new customer:

1. Flow → Create workflow → Trigger: **Order created**.
2. Condition, all of:
   - the customer's number of orders is equal to 1 (welcome kits only go out with first orders, so Skio renewals don't count);
   - `muto.bf_boxes_left` is greater than 0.
3. Action: **Update shop metafield**:
   - namespace `muto`, key `bf_boxes_left`, type Integer;
   - value = the current value minus 1, e.g. `{{ … bf_boxes_left.value | minus: 1 }}`, using Flow's variable picker for the shop metafield.
4. Turn it on before the box goes live.

# Step 3: MUTO10 end date

In Discounts, give **MUTO10** an end date of **28 Oct 2026, 23:59**. Today it has none.

# What the box does

- **What it shows:**
  - "BLACK FRIDAY PRE-SALE".
  - "Extra 10% off the Quarterly plan, plus a free welcome kit worth £77".
  - "£135 for your first box instead of £150. Code MUTO10 is applied automatically at checkout".
  - A live countdown in days, hours, minutes and seconds.
  - "Pre-sale ends 23:59, Wednesday 28 October."
  - "92 of 500 free welcome kits left at this price", with a progress bar.
- **The code:** the page calls `/discount/MUTO10` when it loads, so Shopify applies the code at checkout. MUTO10 gives 10% off, applies to subscriptions and one-time purchases, and can be used once per customer. It works on both plans, even though the box only promotes Quarterly.
- **After 23:59 on 28 October:** the box hides itself and stops applying the code.
- **What you can change:** the end date, the code and the total of 500 are at the top of the script in the pasted code.

# Check after publishing

- [ ] The box appears above "New customer offer" on the main page and on -2, and the countdown is running.
- [ ] Place test orders on Quarterly, Monthly and one-time purchase. Check MUTO10 applies **and** the welcome-kit gifts still arrive. MUTO10 doesn't combine with product discounts, so if the gifts use a product discount, one will cancel the other.
- [ ] After one test order, the count drops from 92 to 91.
- [ ] On a phone, the countdown sits under the text and fits the width.
- [ ] **When the count reaches 0:** the free kit or the price must change, because the box says "at this price". Tell Richie.
