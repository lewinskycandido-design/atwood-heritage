# ASIN Workspace — <ASIN>_<short-name>

Copy this whole folder for each new ASIN, rename it `ASINs/<ASIN>_<short-name>/`, then work top-down.

## Folder map
```
01_Inputs/
  raw-photos/        ← front, back, contents, ingredient, lifestyle, range shots (≥2000px)
  label-nutrition/   ← front-of-pack, Nutrition Facts (bilingual), ingredients, allergens
  brand-assets/      ← logo (vector+PNG), colors, fonts, brand story doc
02_Working/
  codex-prompts/     ← the 9 filled Codex prompts (from 02_Templates/04)
  imgNN_vX.png       ← working renders
03_Final-Images/     ← ASIN_slotNN_shortdesc.jpg (2000×2000, sRGB, q90) ×9
04_Listing-Copy/
  product-spec.md    ← SINGLE SOURCE OF TRUTH (fill first)
  listing-copy.md    ← title/bullets/description/keywords
05_A-Plus/
  a-plus-copy.md     ← A+ module copy
06_QA/
  qa-checklist.md    ← final gate + claim→source log
```

## Run order
1. Request materials → `02_Templates/00_material-request-checklist.md`
2. Fill `04_Listing-Copy/product-spec.md`
3. Fill `02_Working/codex-prompts/` → generate 9 images (skill: `codex-image`)
4. Write `04_Listing-Copy/listing-copy.md` + `05_A-Plus/a-plus-copy.md`
5. Run `06_QA/qa-checklist.md` → brand sign-off → upload

See `../00_System-Docs/` for all rules.
