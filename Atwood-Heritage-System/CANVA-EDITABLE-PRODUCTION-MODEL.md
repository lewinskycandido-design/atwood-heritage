# Canva Editable Production Model — Atwood Heritage

**Requirement (client):** Every generated listing/A+ image must be an **editable Canva design**,
not a flattened JPEG. Text, callouts, product placement, and backgrounds must all remain editable
inside Canva.

This changes *how* Codex and Canva divide the work. Read alongside
`00_System-Docs/06_claude-to-codex-workflow.md` and `CANVA-WORKSPACE-MAP.md`.

---

## Who makes what

### Codex makes COMPONENTS only (never the finished flat image)
- Clean **product cutout** (background removed) from the verified real product photo.
- **Background scenes / textures** (cream paper, rustic wood, warm daylight surfaces).
- **Ingredient / lifestyle compositions** (raw ingredients, in-use scenes) — as placeable elements.
- Supporting visual elements (subtle motifs, dividers).
- One component at a time, saved with the required filename + `_component` suffix.
- **Codex never bakes in:** headlines, benefit text, nutrition numbers, ingredient lists, allergen
  text, logos, badges, prices. Those are added as **editable Canva elements** so they stay correct + adjustable.

### Canva holds the EDITABLE COMPOSITION
- Each of the 9 listing images = **one editable page** in the ASIN's Listing Images design.
- On each page: Codex component(s) placed as elements + **native editable Canva text** for all copy.
- Nutrition Facts (Image 4) = editable text/table in Canva, transcribed exactly from the label
  (or the real label panel placed as a sharp image element) — never AI-generated text.
- Brand colours, fonts, logo pulled from the Brand Kit / master template → consistent + editable.
- Export JPEG from the finished editable page for Amazon upload.

---

## Two ways to create the editable designs (pick per maturity)

**A) Master Brand Template + autofill (preferred, repeatable)**
1. Build a **master editable Listing Images template** (9 pages, 2000×2000) in
   `04 – Listing Image Master Templates`, and an **A+ master template** in
   `03 – A+ Content Master Templates` — using the Brand Kit (needs brand assets first).
2. Per ASIN: `create-design-from-brand-template` with the verified data → a fully editable design
   pre-filled with that ASIN's copy. Then drop in the Codex product components.
3. Result: consistent, on-brand, editable, fast per ASIN.

**B) Duplicate + compose (early, before templates exist)**
1. Create the ASIN's editable design, add 9 pages.
2. Place Codex components + add editable text per page manually.
3. Slower, but works before master templates are built.

> Either way the deliverable is an **editable multi-page Canva design** in the ASIN folder, plus
> exported JPEGs in `10 – Final Amazon Exports` for upload.

---

## Asset flow into Canva
- Codex component images → `upload-asset-from-url` (or upload in Canva) → placed into the design.
- Keep raw + component files in the local ASIN folders (`06 – Generated Images`) with required names.
- Editable design lives in the Canva ASIN folder; flat exports go to `10 – Final Amazon Exports`.

---

## Still gated (unchanged)
Editable or not, nothing gets generated/composed until:
1. **Brand master assets** uploaded (needed for Brand Kit → editable fonts/colours/logo).
2. **ASIN minimum source materials** reviewed (verified facts for the editable text).

Missing → labelled missing-material request. Codex never invents to fill a gap.

---

## Per-image loop (updated)
1. Claude verifies facts + writes the Codex **component** command (cutout/background/scene only).
2. Codex generates the component → save with required filename.
3. QA the component vs. the real product (shape, proportions, logo/label not distorted, quantity).
4. In Canva: place component on the correct editable page + add editable text (verified copy only).
5. QA the composed page (purpose, legibility desktop+mobile, compliance, safe zones).
6. Export JPEG → `10 – Final Amazon Exports`. Record QA + manifest status.
7. Only then move to the next image.
