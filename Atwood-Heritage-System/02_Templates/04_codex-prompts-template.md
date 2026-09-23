# Codex Image Prompts — 9 Slots (Template, per ASIN)

Copy this file into each ASIN's `02_Working/codex-prompts/`. Replace every `<...>` with **verified
facts from product-spec.md**. Run each with the `codex-image` skill (see
`00_System-Docs/06_claude-to-codex-workflow.md`). Slots showing the real pack/label = **edit the
real photo/label image**, don't invent packaging.

Fill once, reuse across the ASIN:
- `<PRODUCT>` = official product name
- `<NETQTY>` = metric net quantity (e.g. 500 g)
- `<PALETTE>` = brand hex values (cream base, heritage dark, accent1, accent2)
- `<HEADLINE_FONT_FEEL>` = heritage serif / slab
- `<BODY_FONT_FEEL>` = clean humanist sans

Global negatives (append to every prompt):
`no watermark, no logos you weren't given, no distorted or garbled text, no lorem ipsum, no extra
text beyond what is specified, no plastic gradients, no neon, no fake certification badges, no
promotional text, no borders, sRGB, sharp focus, legible at 300px thumbnail.`

---

## IMG 1 — Main Image (pure product on white) — EDIT REAL PHOTO
```
Using the provided real product photo of <PRODUCT>, place the exact pack on a pure white background
(RGB 255,255,255), centered, product filling ~85% of a square 2000x2000 frame. Professional studio
lighting, soft natural contact shadow, crisp focus, true-to-life colors and label.
ABSOLUTELY NO text, no graphics, no badges, no props, no borders. Product only.
Keep the real label, brand mark, and all packaging text exactly as in the source photo — do not
alter or regenerate any label text.
[+ global negatives]
```

## IMG 2 — Key Benefit / Product Overview
```
Premium Canadian heritage food product image, rustic but clean. Square 2000x2000.
SUBJECT: <PRODUCT> (<NETQTY>) hero shot, slightly angled, on a warm cream (<PALETTE base>) backdrop
with subtle paper texture and soft daylight.
LAYOUT: product centered/left; 3–4 short benefit callouts arranged cleanly (icon + 1–3 word label each).
CALLOUTS (verified only): "<benefit1>", "<benefit2>", "<benefit3>", "<benefit4>".
HEADLINE (≤6 words, <HEADLINE_FONT_FEEL>): "<overview headline>".
Labels in <BODY_FONT_FEEL>. Accent colors: <PALETTE accent1/accent2>, max 2.
Simple line icons, heritage feel, no clip-art.
[+ global negatives]
```

## IMG 3 — Ingredient / Source / Quality Story
```
Premium Canadian heritage food image, rustic but clean. Square 2000x2000.
SCENE: raw source ingredients of <PRODUCT> (<verified key ingredients>) arranged on natural wood /
linen with the pack beside them, warm daylight, subtle steam/texture as fitting.
HEADLINE (≤6 words): "<sourcing/quality line, e.g. Made with whole grain oats>".
Sub-line (short, verified): "<origin or craft note>".
Palette <PALETTE>, heritage serif headline + clean sans sub-line, max 2 accents.
No health/superfood claims. Ingredients shown must be actual ingredients only.
[+ global negatives]
```

## IMG 4 — Nutrition / Product Facts — USE REAL LABEL
```
Clean premium infographic, square 2000x2000, warm cream background, rustic-clean.
Reproduce the product's ACTUAL bilingual (EN/FR) Nutrition Facts panel from the provided label
image, placed legibly on the right. On the left, present key verified facts as tidy rows:
"Net quantity: <NETQTY>", "Servings per pack: <servings>", "Serving size: <serving size>",
"Contains: <allergens>".
Do NOT invent or alter any nutrition numbers, ingredients, or allergen text — mirror the label
exactly. Heritage serif headline "<Product Facts / Nutrition>", clean sans body. Palette <PALETTE>.
[+ global negatives]
```

## IMG 5 — Pack Size / Serving / Use Case
```
Premium heritage product infographic, square 2000x2000, cream background, rustic-clean.
LEFT: <PRODUCT> pack with dimension/size callout lines showing <NETQTY> and pack size.
RIGHT: a simple 1–3 step "How to enjoy" strip (small icons + short labels): "<step1>", "<step2>", "<step3>".
Callout: "<servings> servings per pack".
Heritage serif headline "<Size & Serving / How to Enjoy>", clean sans labels. Palette <PALETTE>.
All numbers/steps from spec/label only.
[+ global negatives]
```

## IMG 6 — Lifestyle — PREFER EDITING A REAL PRODUCT PHOTO INTO SCENE
```
Warm lifestyle photo, square 2000x2000, premium Canadian heritage mood, rustic but clean.
SCENE: <PRODUCT> in a real home setting — <e.g. sunlit wooden kitchen table, linen napkin, morning
light>, product clearly visible and unaltered (use the real pack from the provided photo).
Natural props only: wood, linen, ceramic, <fitting food context>. Human hands optional.
Optional short evocative line (≤5 words): "<lifestyle line>" — or no text.
No health/medical implication. Product must remain true to the real item.
[+ global negatives]
```

## IMG 7 — Brand Trust / Heritage Story
```
Premium brand-story image, square 2000x2000, rustic-clean, warm cream/heritage-dark palette <PALETTE>.
CONTENT: Atwood Heritage logo (use provided logo file), a short heritage narrative, and 2–3 verified
proof points as small badges/labels: "<est. year>", "<family-owned/region>", "<craft/values>".
HEADLINE (heritage serif): "<heritage headline>". Body (clean sans): "<1–2 line brand story>".
Subtle texture, rustic props minimal (e.g. faint wheat/wood motif). Only brand-confirmed facts.
[+ global negatives]
```

## IMG 8 — Comparison / Product Range
```
Clean premium line-up / comparison image, square 2000x2000, cream background, rustic-clean.
OPTION A (range): consistent renders of the Atwood Heritage <line> variants in a row, each labeled
with name + <NETQTY>/format.
OPTION B (attribute grid): a simple table comparing own variants across factual rows
(<format>, <net qty>, <key ingredient>, <verified dietary flag>).
Heritage serif headline "<Explore the Range / Find your fit>", clean sans labels. Palette <PALETTE>.
Own products / objective attributes only — no competitor references, no "better than" claims.
[+ global negatives]
```

## IMG 9 — Final Conversion / Why Choose Atwood Heritage
```
Premium closing image, square 2000x2000, rustic-clean, palette <PALETTE>.
CONTENT: <PRODUCT> hero shot + a tight recap of 3–5 verified selling points as a clean checklist:
"<point1>", "<point2>", "<point3>", "<point4>". Atwood Heritage logo sign-off at bottom.
HEADLINE (heritage serif, ≤6 words): "Why choose Atwood Heritage".
Optional truthful line: "<e.g. Small-batch, made in Canada>". Clean sans body.
Recap only claims already shown in images 1–8. Warm, confident, uncluttered.
[+ global negatives]
```

---

### After generating each image
1. Save working PNG → `02_Working/imgNN_vX.png`.
2. QA vs `08_qa-checklist-master.md` (brand + compliance + legibility).
3. Iterate prompt if needed.
4. Export final 2000×2000 sRGB JPEG q90 → `03_Final-Images/ASIN_slotNN_shortdesc.jpg`.
5. Log on-image claims + sources in `06_QA/qa-checklist.md`.
