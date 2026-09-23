# 06 — Claude → Codex Command Workflow

How to drive image generation/editing for each ASIN. Images are produced with the **Codex image
tool** (via the `codex-image` skill, which runs OpenAI's image model on your ChatGPT/Codex plan —
no API key, no per-image dollar cost). Claude assembles the fact-checked prompt; Codex renders.

---

## Roles
- **Claude** = producer/art director. Reads the spec sheet + label + raw photos, verifies every
  claim, writes the exact Codex prompt, and QA's the output.
- **Codex image tool** = renderer. Generates or edits the PNG from Claude's prompt (optionally using
  a raw product photo as reference/edit input).

---

## The loop (per image, ×9)

```
1. GATHER   → Claude reads product-spec.md + label images + raw photos for this ASIN.
2. VERIFY   → Every word destined for the image is checked against a source. Unverifiable → cut.
3. PROMPT   → Claude fills the slot's Codex prompt from 04_codex-prompts-template.md.
4. GENERATE → Run the codex-image skill with that prompt (+ reference image if editing a real photo).
5. REVIEW   → Claude checks output vs. 08_qa-checklist-master.md (brand + compliance + legibility).
6. ITERATE  → Refine the prompt; regenerate. Repeat until pass.
7. FINALIZE → Export 2000×2000 sRGB JPEG → 03_Final-Images/ ; log claims+sources in QA sheet.
```

---

## How to invoke Codex for images

Use the **`codex-image`** skill. Two modes:

**A) Generate from a text prompt** (infographic/story slots — 2,3,4,5,7,8,9):
> Invoke: `codex-image` with the finalized prompt from `codex-prompts/imgNN_*.md`.
> Save output PNG to `02_Working/`.

**B) Edit / composite a real product photo** (main + lifestyle — 1, 6, and any slot showing the actual pack):
> Provide the raw product photo as the reference/input image, plus the edit instruction
> (e.g. "place this exact pack on pure white, ~85% frame, soft studio shadow, no text").
> This preserves label accuracy — critical for the main image and any real-product shot.

> ⚠️ **Label fidelity:** Do NOT let the model invent or restyle label text, Nutrition Facts, or
> brand marks. For any slot showing the real pack or panel, edit the actual photo/label image rather
> than generating packaging from scratch. Generated packaging is for mood/mockup only, never for the
> live main image.

---

## Standard prompt skeleton (all slots)
Claude fills this from the spec; see per-slot prompts in `02_Templates/04_codex-prompts-template.md`.

```
[ROLE] Premium Canadian heritage food brand product image, rustic but clean.
[SLOT JOB] <what this specific image must communicate>
[SUBJECT] <exact product name + verified format/size>
[LAYOUT] Square 1:1, 2000x2000. <composition, where text/product/props sit>
[BRAND STYLE] Palette: <hex from brand guide>. Fonts feel: heritage serif headline + clean sans labels.
              Warm daylight, subtle paper/linen texture, natural shadows. Max 2 accent colors.
[TEXT ON IMAGE] "<only verified copy, ≤6-word headline + short labels>"  (spell exactly; no other text)
[PROPS] <natural props: wood/linen/wheat — only where allowed by slot>
[CONSTRAINTS] No medical claims, no unverified badges, no competitor refs, no clutter.
              Legible at 300px thumbnail. sRGB.
[NEGATIVE] no watermark, no lorem ipsum, no distorted text, no plastic gradients, no neon,
           no fake certification logos, no extra text beyond specified.
```

> For **Slot 1 (main)** the prompt has NO on-image text and NO props — pure product on white.

---

## Naming & handoff
- Working renders: `02_Working/imgNN_vX.png`
- Final: `03_Final-Images/ASIN_slotNN_shortdesc.jpg` (2000×2000, sRGB, q90)
- Each final image's on-image claims + source logged in `06_QA/qa-checklist.md`.

---

## Batch tip
Generate slots in this order so facts compound cleanly:
`1 (main) → 4 (facts) → 3 (ingredients) → 2 (overview) → 5 (size/use) → 7 (heritage) → 8 (range) → 6 (lifestyle) → 9 (conversion)`.
Facts/ingredients first locks the verified copy you'll reuse in later slots.
