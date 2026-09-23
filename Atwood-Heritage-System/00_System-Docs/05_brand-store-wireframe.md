# 05 — Amazon Brand Store Wireframe (Atwood Heritage)

Multi-page Amazon Store built in the Store Builder. Premium heritage feel, rustic-clean, mobile-first.
Store images/tiles follow the brand system in `01_image-system-guidelines.md`.

**Builder note:** Amazon Stores use tiles/sections on a responsive grid. Design assets for both
desktop and mobile. Full-width hero ~ 3000 px wide recommended; keep critical content centered.

---

## Site map
```
Home
├─ Shop All (product grid)
├─ Collections / By Category  (e.g. Breakfast · Pantry · Gifting — match real range)
├─ Our Story (heritage)
└─ (optional) Recipes / How to Enjoy
```

---

## Page 1 — HOME (wireframe, top → bottom)

```
┌──────────────────────────────────────────────────────────┐
│ [ NAV: Atwood Heritage logo | Shop All | Collections |   │
│        Our Story | Recipes ]                             │
├──────────────────────────────────────────────────────────┤
│ HERO (full-width lifestyle)                              │
│   Brand logo + one-line positioning                     │
│   [ Shop All ]  button                                  │
├──────────────────────────────────────────────────────────┤
│ VALUE STRIP  ( 3–4 icons + labels )                     │
│   Small-batch · Canadian · Quality ingredients · ...    │
│   (only verified attributes)                            │
├──────────────────────────────────────────────────────────┤
│ FEATURED / BESTSELLERS  (product tile row, 3–4 ASINs)   │
├──────────────────────────────────────────────────────────┤
│ HERITAGE STORY BAND                                      │
│   Image + short founding/quality story  [ Our Story ]   │
├──────────────────────────────────────────────────────────┤
│ SHOP BY CATEGORY  (tiles link to collection pages)      │
├──────────────────────────────────────────────────────────┤
│ LIFESTYLE / RECIPE band  (optional)                     │
├──────────────────────────────────────────────────────────┤
│ FOOTER: brand line + full product grid                  │
└──────────────────────────────────────────────────────────┘
```

## Page 2 — SHOP ALL
- Full product grid (auto-populated product tiles), sortable by Amazon.
- Optional short banner at top with brand lockup.

## Page 3 — COLLECTIONS / BY CATEGORY
- One section per real category. Each: category banner + product subset grid.
- Only create categories that map to actual SKUs.

## Page 4 — OUR STORY (heritage)
```
┌──────────────────────────────────────────────────────────┐
│ HERO: heritage image + headline                          │
│ STORY BLOCKS (image + text, alternating L/R):            │
│   • Roots / founding (verified facts only)               │
│   • Craft / small-batch process                          │
│   • Ingredients / sourcing                                │
│   • Values / Canadian identity                            │
│ CLOSING: brand mark + [ Shop All ]                       │
└──────────────────────────────────────────────────────────┘
```

## Page 5 — RECIPES / HOW TO ENJOY (optional)
- Serving ideas / simple recipes using the products. Factual, on-brand, links back to ASINs.

---

## Store design rules
- Consistent nav on every page; logo → Home.
- Reuse gallery palette, fonts, badge/icon style.
- Every claim on Store tiles sourced (same discipline as listings).
- Mobile: check tile text legibility; keep hero text centered and large.
- Bilingual consideration for `.ca` where practical.
- No pricing/promo claims baked into images (prices change; Amazon shows live price).
