# Atwood Heritage — Amazon.ca Listing System

A repeatable, compliance-first system for producing Amazon.ca listings for every ASIN:
9 listing images, optimized copy, A+ Content, a Brand Store layout, and a QA gate — all
generated with Claude → Codex image commands and verified against **only** documented product facts.

**Brand direction:** Premium Canadian heritage food brand. Rustic but clean. Amazon-compliant.
**Non-negotiable:** No medical claims. No unsupported nutrition or ingredient claims. Every claim
on an image or in copy must trace to the product spec sheet, the physical label, the official
website, or the live Amazon.ca listing.

---

## How to run a new ASIN (quick start)

1. **Copy the template folder**
   `_ASIN-TEMPLATE/` → `ASINs/<ASIN>_<short-name>/`
2. **Drop inputs** into `01_Inputs/` (raw photos, label/nutrition images, brand assets).
   Use `02_Templates/00_material-request-checklist.md` to request anything missing from the brand.
3. **Fill the spec sheet** `04_Listing-Copy/product-spec.md` from the template. This is the single
   source of truth. If a fact is not in here, it cannot appear on an image.
4. **Generate images** using `00_System-Docs/06_claude-to-codex-workflow.md`. Each of the 9 images
   has its own Codex prompt in `02_Working/codex-prompts/`.
5. **Write copy + A+** using the templates in `02_Templates/`.
6. **Run QA** `06_QA/qa-checklist.md`. Nothing uploads until every box is checked.

---

## System documents (`00_System-Docs/`)

| # | Doc | Purpose |
|---|-----|---------|
| 01 | [Amazon.ca image system guidelines](00_System-Docs/01_image-system-guidelines.md) | Technical + brand rules every image must follow |
| 02 | [9-image layout plan](00_System-Docs/02_nine-image-layout-plan.md) | What each of the 9 slots must communicate |
| 03 | [Listing optimization playbook](00_System-Docs/03_listing-optimization.md) | Title, bullets, description, backend keywords |
| 04 | [A+ Content module plan](00_System-Docs/04_a-plus-content-plan.md) | Module-by-module A+ layout |
| 05 | [Brand Store wireframe](00_System-Docs/05_brand-store-wireframe.md) | Multi-page Store layout |
| 06 | [Claude → Codex command workflow](00_System-Docs/06_claude-to-codex-workflow.md) | How to drive image generation/editing |
| 07 | [Canada food/grocery compliance checklist](00_System-Docs/07_compliance-canada-food.md) | CFIA/Health Canada + Amazon rules |
| 08 | [QA checklist (master)](00_System-Docs/08_qa-checklist-master.md) | Final gate before upload |

## Brand request pack (`03_Brand-Requests/`) — send to the brand
Everything the brand must provide, split into 3 categories:
- `00_cover-sheet.md` — overview + the one rule + how to send files
- `01_request-images.md` — materials for the 9 listing images
- `02_request-a-plus.md` — materials for A+ Content
- `03_request-brand-store.md` — materials for the Brand Store

## Templates (`02_Templates/`)

- `00_material-request-checklist.md` — what to request from the brand per ASIN
- `01_product-spec-template.md` — the single source of truth per ASIN
- `02_listing-copy-template.md` — title/bullets/description/keywords
- `03_a-plus-template.md` — A+ copy blocks
- `04_codex-prompts-template.md` — the 9 image prompts, ready to fill

## Per-ASIN template (`_ASIN-TEMPLATE/`)
Copy this whole folder for each new ASIN. See its internal `README.md` for the folder map.

---

## Golden rules
1. **Facts only.** No claim without a source. When unsure → leave it out and flag on the request checklist.
2. **Main image = pure product on white.** No text, no props, no badges. Ever.
3. **Legibility on mobile.** ~80% of Amazon.ca shoppers are on phones. Test every image as a thumbnail.
4. **One idea per image.** Nine images = nine jobs. Don't crowd.
5. **Consistency across the ASIN and the catalog.** Same fonts, palette, badge style, layout grid.
