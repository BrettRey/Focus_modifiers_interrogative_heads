# Session Log: Focus Modifiers with Interrogative Heads

## Project Timeline
- **Folder created**: 2025-12-20, ~12:00 EST
- **Draft complete**: 2025-12-20, ~14:20 EST
- **Polish complete**: 2025-12-20, ~17:00 EST
- **Posted to LingBuzz**: 2025-12-20, ~21:00 EST
- **Elapsed time**: ~9 hours (including gym and dinner break)
- **Actual working time**: ~5-6 hours

## What was accomplished
- Full 4-page Glossa squib drafted from scratch
- Core puzzle: *exactly who* ✓ vs. *the person exactly who* ✗
- CGEL-based syntactic analysis (peripheral modifiers)
- Semantic layer (alternatives + exhaustivity)
- Pragmatic explanation (BCI principle from Cuneo & Goldberg 2023)
- Rhetorical polish: inclusio, tricolon, epigrammatic close
- Title: "*Exactly who* but not *the person exactly who*: Focus modifiers and the foregrounding constraint"
- CGEL terminology standardized ("interrogative word" not "wh-element")
- *Only* added to modifier class
- *else* unified under foregrounding (contrastive focus)
- Open questions expanded (exclamatives, free-choice disambiguation, gradient judgments)
- Keywords added
- XeLaTeX used for proper PDF text extraction (LuaLaTeX had copy-paste issues)

## Key insight (from the human)
Fused relatives pattern with questions; integrated relatives don't—a gap CGEL documents but doesn't explain. The BCI principle (Cuneo & Goldberg 2023) provides the "why": precision modifiers foreground; relatives background; clash.

## On the division of labour
> "I'm the one who knows what questions to ask and notices the interesting issues; LLMs are certainly capable of seeing them once I point them out but are highly unlikely to notice them on their own."

This is accurate. The LLM executed the plan, drafted prose, fixed errors, applied feedback—but the intellectual spark (the puzzle, the BCI connection, the pied-piping test cases, the *else* unification, the open questions about exclamatives and gradient judgments) came from the human.

## Rhetorical improvements applied
- **Inclusio**: Opening/closing echo with the key contrast
- **Tricolon with asyndeton**: "Syntax identifies... Semantics explains... Pragmatics explains..."
- **Epigrammatic close**: "*Exactly who* works because identity is at stake. *The person exactly who* fails because backgrounded content resists foregrounding."
- **Title with empirical hook**: Contrast before colon, theoretical term after

## Files produced
- `main.tex` — LaTeX source (~9.6KB)
- `main.pdf` — Compiled PDF (4 pages)
- `references.bib` — Bibliography (4 entries)
- `cgel-notes.md`, `foregrounding-analysis.md`, `draft-notes.md` — Working notes
- `.house-style/` — Preamble and style rules

## Open questions in squib
- Stacking order (*just exactly* vs. *exactly just*)
- Cross-linguistic parallels (German *genau wer*, *ausgerechnet*)
- Exclamatives (*Exactly what a disaster!*)
- Free-choice vs. fused-relative disambiguation
- Gradient vs. categorical judgments

## External review
ChatGPT provided detailed critique mid-session. Key points addressed:
- Added footnote about DP-level *exactly three cats*
- Confirmed Theiler citation is defensible for exhaustivity
- Added semantic contrast examples (*exactly the cats* vs. *exactly the cats you mentioned*)
- Unified *else* under contrastive-focus foregrounding

## Intellectual origin (Dec 20, evening)

The squib originated from a discussion in the HPC book project about CGEL's classification of *today/tomorrow/tonight/yesterday* as pronouns. The thought process:

1. **Deixis** → *today/tomorrow* resist determiners because their reference is contextually saturated
2. **Anaphor** → relative *who/what* resist determiners because they're bound
3. **But wait** — interrogative *who/what* are *neither* deictic *nor* anaphoric (they're open variables over alternatives), yet they *also* resist determiners
4. **So the resistance isn't from deixis or anaphor per se** — it's from **referential saturation at the DP level**, which all three achieve by different routes
5. **But then** — interrogatives *do* allow these weird AdvP modifiers (*exactly who*) that other relatives don't...
6. **Squib ensues**

The unifying insight is that **determiner resistance** and **focus-modifier licensing** are *different* cluster properties that happen to co-occur in interrogatives but come apart in relatives. The BCI principle explains why: fused relatives keep the wh-word foregrounded (so focus modifiers work), while integrated relatives background it (blocking them).

### HPC connection

This is a concrete example for the HPC book (Chapter 11 or 12): the "pronoun" or "wh-word" category isn't a unified HPC — it's multiple overlapping clusters:

| Property | Deixis (*today*) | Anaphor (rel. *who*) | Interrogative (*who?*) |
|----------|------------------|----------------------|------------------------|
| Determiner resistance | ✓ | ✓ | ✓ |
| Focus-modifier licensing | ✗ | ✗ (integrated) / ✓ (fused) | ✓ |
| Morphological paradigm | ✗ | partial | partial |

The clustering is real but the *mechanisms* are different at each level. Classic HPC situation.
