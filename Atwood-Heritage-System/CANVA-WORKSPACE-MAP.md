# Canva Workspace Map — Atwood Heritage (LIVE)

**Canva access:** ✅ Available & authenticated (Canva MCP server).
**Created:** 2026-07-25. **Status:** Brand-level structure live. ASIN folders + designs pending source materials.

---

## Live folders (created directly in Canva)

| Folder | Canva ID | URL |
|---|---|---|
| **Atwood Heritage – Amazon.ca Optimization** (main) | `FAHQXWyNXg4` | https://www.canva.com/folder/FAHQXWyNXg4 |
| 00 – Brand Master Assets | `FAHQXa8FjJU` | https://www.canva.com/folder/FAHQXa8FjJU |
| 01 – Brand Guidelines | `FAHQXYqdbMw` | https://www.canva.com/folder/FAHQXYqdbMw |
| 02 – Amazon Brand Store | `FAHQXRHq5nQ` | https://www.canva.com/folder/FAHQXRHq5nQ |
| 03 – A+ Content Master Templates | `FAHQXWgSvPQ` | https://www.canva.com/folder/FAHQXWgSvPQ |
| 04 – Listing Image Master Templates | `FAHQXXZBmYY` | https://www.canva.com/folder/FAHQXXZBmYY |
| 05 – Client Presentation | `FAHQXWqFtL0` | https://www.canva.com/folder/FAHQXWqFtL0 |
| ASIN Projects | `FAHQXW4Q6bQ` | https://www.canva.com/folder/FAHQXW4Q6bQ |

---

## What happens per ASIN (created on intake, not before)
Inside **ASIN Projects** (`FAHQXW4Q6bQ`), one folder per ASIN named:
`[ASIN] – [Product Name] – [Pack Size]`

Each ASIN folder gets 3 Canva designs:
1. `[ASIN] – [Short Name] – Amazon Listing Images` (9 pages, 2000×2000, RGB, JPEG export)
2. `[ASIN] – [Short Name] – A+ Content` (module-matched pixel dimensions)
3. `[ASIN] – [Short Name] – Specification and QA`

## Brand Store (brand-level, NOT per ASIN)
Lives in **02 – Amazon Brand Store** (`FAHQXRHq5nQ`).
Design: `Atwood Heritage – Amazon.ca Brand Store` — created once brand catalogue + assets are confirmed.

---

## Brand asset intake structure (inside `00 – Brand Master Assets` = `FAHQXa8FjJU`)
The drop zone the brand uploads into. One subfolder per asset type:

| Subfolder | Canva ID | For |
|---|---|---|
| 01 – Logos | `FAHQXnEY5r0` | Primary, secondary, transparent PNG, vector logo files |
| 02 – Colours & Fonts | `FAHQXrwqoNE` | Hex/Pantone values, font files or names |
| 03 – Product & Packaging Photos | `FAHQXigBTKU` | Front/back/sides, out-of-pack, range shots |
| 04 – Lifestyle & Brand Story Photos | `FAHQXvMuN1E` | Approved lifestyle, facility/production, heritage |
| 05 – Label, Nutrition & UPC Images | `FAHQXgQKSxU` | Front label, bilingual Nutrition Facts, ingredients/allergens, UPC |
| 06 – Certifications & Badges | `FAHQXmn9mUQ` | Certificates + approved badge logos (with proof) |
| 07 – Icons, Patterns & Textures | `FAHQXlwPMQg` | Brand icons, patterns, textures |
| 08 – Claim Documentation & Approvals | `FAHQXvQtLJU` | Written claim approvals, do-not-say list, source docs |

**Brand-facing intake = SharePoint** (chosen). No SharePoint connector is available in this session, so the brand uploads there, not into Canva directly. A ready-made mirror of these 8 categories (with a brand upload guide + per-folder notes) was delivered as `Brand-Asset-Intake-SharePoint.zip` — upload it to SharePoint once to recreate the structure. Local copy: `../Brand Asset Intake (upload to SharePoint)/`.

**Import path SharePoint → Canva:** once assets are in SharePoint, share them with me. Direct-download links can be imported into the matching Canva folders via `upload-asset-from-url`. Note: default SharePoint share links are auth-gated (not direct-download) — either grant a direct/anonymous download link, or download + hand me the files, and I upload into the Canva subfolders above.

## Output format: EDITABLE Canva designs (client requirement)
All generated listing/A+ images must be **editable Canva designs**, not flat JPEGs. Codex produces
only components (product cutout, backgrounds, ingredient scenes); Canva holds the editable
composition with native text. Full model → [CANVA-EDITABLE-PRODUCTION-MODEL.md](CANVA-EDITABLE-PRODUCTION-MODEL.md).
Preferred path: master Brand Templates in `04`/`03` + autofill per ASIN.

## Gate before any design/image generation
Do NOT create designs or generate images until BOTH are true:
1. **Brand master assets uploaded** to `00 – Brand Master Assets` (logo, palette, fonts, approved photography, certifications, claim docs).
2. **ASIN minimum source materials** reviewed (see ASIN Intake Command): ASIN link, front + back photos, Nutrition Facts, ingredients/allergens, UPC, pack config, official page, written claim approval.

Missing anything → issue a labelled missing-material request; do not invent.

---

## Brand Kit status
- **Real Canva Brand Kit:** NOT created. Blocked on (a) brand assets not ready, (b) Canva Brand Kits require Pro/Teams, (c) Canva API is read-only for Brand Kits (`list-brand-kits` only — no create).
- **Placeholder in place:** editable **"Atwood Heritage — Brand Guidelines (PLACEHOLDER)"** Canva Doc created and filed in `01 – Brand Guidelines`.
  - Edit: https://www.canva.com/d/s2JVI5ZURzIm05Y  · View: https://www.canva.com/d/HpXQ9eqAIdcoGYO · Design ID `DAHQXrILE-I`
  - Action: replace every blank (hex, fonts, logo, heritage facts) with verified brand values → then build the real Brand Kit in the Canva app (Pro/Teams required).

## Project status: `Waiting for Brand Master Assets + first ASIN intake`
- [x] Canva access verified
- [x] Main folder created
- [x] 7 brand-level folders created
- [x] Brand Guidelines placeholder design created (fill when assets arrive)
- [ ] Real Brand Kit created (needs assets + Pro/Teams; done in Canva app)
- [ ] Brand master assets uploaded (brand to supply)
- [ ] First ASIN intake received
- [ ] ASIN folder + 3 designs created
- [ ] Brand Store design created
