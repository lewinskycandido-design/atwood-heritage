# 01 — Amazon.ca Image System Guidelines

The technical and visual rules every Atwood Heritage listing image must follow. Applies to all 9
slots. Slot-specific direction lives in `02_nine-image-layout-plan.md`.

---

## 1. Technical specs (Amazon.ca requirements)

| Attribute | Rule |
|-----------|------|
| **File format** | JPEG (`.jpg`) preferred for listing; PNG/TIFF accepted. Use JPEG for final upload. |
| **Color mode** | sRGB (not CMYK). |
| **Recommended size** | **2000 × 2000 px** (square). Enables hover-zoom. Never below 1600 px on the longest side; 1000 px is the hard floor for zoom. |
| **Aspect ratio** | 1:1 square for all 9 gallery slots. |
| **Max file size** | Keep under 10 MB; target 1–3 MB with quality ≥ 85. |
| **Resolution** | 72 dpi+ (pixel dimensions are what matter, not dpi). |
| **Frame fill** | Product fills **~85%** of the frame on the main image. |
| **File naming** | `ASIN_slotNN_shortdesc.jpg` — e.g. `B0XXXXX_01_main.jpg` |

### Main image (Slot 1) — strict Amazon rules
- Pure **RGB white background** (255,255,255).
- **Product only.** No text, logos, watermarks, badges, borders, props, or graphics.
- No packaging that isn't part of the actual product being sold.
- No inset/secondary images, no "collage."
- Fills ~85% of the frame, centered, in focus, professionally lit.
- Must be a real representation of the product (a photo, or a photoreal render of the actual pack).

> Slots 2–9 may include text, graphics, lifestyle scenes, and infographics.

---

## 2. Brand visual system — "rustic but clean"

### Palette (define real hex values in `01_Brand-Assets/brand-guide.md`)
- **Base / paper:** warm off-white / cream (background for infographic slots).
- **Ink / heritage dark:** deep charcoal or espresso brown for headlines.
- **Primary heritage accent:** a single brand color (e.g. forest green, oxblood, or barn red — confirm from brand assets).
- **Secondary accent:** muted gold / wheat / natural kraft.
- Keep to **2 accent colors max** per image. Rustic ≠ busy.

### Typography
- **Headline:** a characterful serif or slab-serif (heritage feel). One typeface, 2–3 weights.
- **Body / labels:** a clean humanist sans-serif for legibility at thumbnail size.
- Never more than **2 type families** per image.
- Minimum on-image text size: readable when the image is scaled to a 300 px thumbnail.

### Texture & finish (the "rustic" without the mess)
- Subtle paper/linen grain, soft natural shadows, warm daylight.
- Natural props only on lifestyle/story slots: wood, linen, stone, wheat, kraft paper, cast iron.
- **Avoid:** heavy filters, plastic-looking gradients, neon, clip-art icons, drop-shadow overload.

### Layout grid
- Work on a consistent invisible grid (e.g. 12-col with generous margins ≥ 8% of frame).
- Reserve a consistent zone for the badge/label style so all 9 feel like a set.
- Same corner for the small brand logo lockup on infographic slots (e.g. top-left or bottom-center).

---

## 3. Legibility & mobile-first rules
- Design every non-main image to survive a **300 × 300 px** thumbnail.
- Max ~6–8 words per headline. One core message per image.
- High contrast text over image (add a scrim/overlay behind text on lifestyle shots).
- Icons paired with 1–3 word labels, not paragraphs.
- Numbers and facts big; supporting text small.

---

## 4. Claim & text rules on images (compliance-first)
- Only text that maps to a **verified source** (spec sheet / label / official site / live listing).
- **Prohibited on images:** "cures," "treats," "prevents," "clinically proven," disease references,
  "#1," "best," unverifiable superlatives, unearned certification logos.
- If claiming a certification (organic, non-GMO, gluten-free, kosher, etc.), the product must
  actually hold it and you must have the logo rights. Otherwise **omit**.
- Nutrition callouts must match the label's Nutrition Facts table exactly (e.g. "Xg protein per serving").
- Country-of-origin / "Made in Canada" style claims must meet CFIA thresholds — see `07_compliance-canada-food.md`.

---

## 5. Consistency across ASINs
- Reuse the same badge template, icon set, font pairing, and color tokens for every ASIN.
- Keep the same photographic light direction and background tone across the catalog.
- The set of 9 should look unmistakably "Atwood Heritage" next to any other product in the brand.

---

## 6. Output & export
- Export final at 2000×2000, sRGB, JPEG quality 90.
- Keep an editable/source version (PNG or layered) in `02_Working/`.
- Final delivery lands in `03_Final-Images/` named per the convention above.
- Log every image's claims + source in `06_QA/qa-checklist.md`.
