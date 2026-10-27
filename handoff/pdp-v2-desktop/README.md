---
title: "MUTO product page: desktop top of page, plus spacing"
subtitle: "27 October 2026, afternoon"
---

One file to replace on the live theme. It updates the product page on both URLs, which share the template:

- <https://muto.co/products/muto-nad-cellular-complex>
- <https://muto.co/products/muto-nad-cellular-complex-2>

This morning's two files (template and cart drawer) are already live. The cart drawer doesn't change.

# Before you start

- **File:** `templates/product.muto-nad-v2.json`, in `MUTO_PDP_Desktop_27Oct2026_PM.zip`. It's also in GitHub at `handoff/pdp-v2-desktop/` (repo drrichiebarclay-rgb/claude, branch `claude/beautiful-bohr-wkhdur`).
- **Preview:** theme **"Clone Of Live | Plan pricing /mo [27-10]"** (ID 203700666715):
  - <https://muto.co/products/muto-nad-cellular-complex?preview_theme_id=203700666715>
  - <https://muto.co/products/muto-nad-cellular-complex-2?preview_theme_id=203700666715>
- **Built from live as it stands now.** It's this morning's template plus the changes below, so nothing on live is lost. If this template has been edited in the theme editor since 10:40 today, tell me before copying.

# Step 1: replace the template

On the live theme (**Clone Of Live | Buy Box Redesign [31-08]**), go to **Edit code**. Open `templates/product.muto-nad-v2.json`, replace everything with the file from the zip, and save.

**The other way to do it:** publish the preview theme, which is live plus this one file.

# What changes

## Desktop (990px and wider)

- **New order in the right-hand column:**
  1. Stars and "4.83 out of 5".
  2. NAD+ Cellular Complex.
  3. The descriptor ("Everything your body needs after 35…").
  4. The offer: "Choose your plan", the Black Friday box, plans, one-time and Add to cart.
  5. The serving line, the description, reviews and folds.
- **"How it helps" is hidden** (the Energy, Recovery, Mind list).
- **More space** between the stars and the title (20px), the title and the descriptor (18px), and the descriptor and "Choose your plan" (36px).

## Phones

- No change to the order. The offer still comes straight after the images and the testing button.
- "How it helps" still shows on phones, below Add to cart.

## How it's done

All of it is CSS and a small script in the Custom Liquid block at the bottom of the template (`easy_read`). Sections, assets and Skio don't change.

# Check after publishing

- [ ] **Desktop, both URLs:** stars, title and descriptor, then "Choose your plan" with the plans and Add to cart right under them. No "How it helps". The description sits below the button.
- [ ] **Desktop, plan switching:** switching plans still works and the sticky bar shows ~~£70~~ £50/mo or ~~£70~~ £60/mo.
- [ ] **Phone:** unchanged from this morning. Stars, title and descriptor sit above the images, then the testing button, then the plans.
