# Session Log: Focus Modifiers with Interrogative Heads

## Project Timeline
- **Folder created**: 2025-12-20, ~12:00 EST
- **Draft complete**: 2025-12-20, ~14:20 EST
- **Polish complete**: 2025-12-20, ~17:00 EST
- **Posted to LingBuzz**: 2025-12-20, ~21:00 EST
- **Pullum revision**: 2025-12-23, ~13:00 EST
- **Elapsed time**: ~9 hours (including gym and dinner break)
- **Actual working time**: ~5-6 hours

## Session: 2025-12-23 — Pullum Revision

### Geoff's critical feedback (received Dec 23)

> I am not at all sure that you're right about fused relatives allowing the precisification adverbs... To secure my own intuitions on the matter, I generally use examples like these:
>
> (2) a. What Frankenstein created that night still isn't clear. [subordinate interrogative]
>     b. What Frankenstein created that night would later murder his wife. [fused relative]
>
> In (2b), the use of the fused relative as the subject of the verb murder completely rules out interpreting it as implicitly some kind of question... Now notice what happens under the precisification adverbs:
>
> (3) a. Exactly what Frankenstein created that night still isn't clear. [interrogative] ✓
>     b. *Exactly what Frankenstein created that night would later murder his wife. [fused relative] ✗
>
> I'm pretty sure (3b) is disastrously bad. So (faute de mieux) I think in (1) you must have a disguised interrogative.

**Verdict**: Geoff is right. The generalization simplifies.

### Changes made

| Section | Change |
|---------|--------|
| **Abstract** | Removed "fused relatives" — now says precision modifiers apply to interrogatives but not relatives "fused or otherwise" |
| **Example paradigm** | Added Geoff's Frankenstein diagnostic: `*Exactly what F. created would murder his wife` |
| **Section 1** | Added explanatory note on subordinate interrogative vs. fused relative disambiguation |
| **Section 2** | "Interrogatives but excludes all relative constructions" |
| **Section 3** | Removed the "fused relatives escape" explanation — all relatives background |
| **Conclusion** | Updated to reflect simpler generalization |
| **Open questions** | Removed free-choice disambiguation question (no longer relevant) |

### Theoretical upshot

The revised generalization is **simpler**: precision modifiers are licensed by **interrogatives only**. All relatives — fused and integrated alike — background the wh-word, so the BCI clash applies uniformly.

The earlier claim that "fused relatives pattern with interrogatives" was based on examples like *I saw exactly what you did*, which are actually **subordinate interrogatives**, not fused relatives. Geoff's Frankenstein test disambiguates: use a predicate that forces a referential reading.

### HPC table update

| Property | Deixis (*today*) | Anaphor (rel. *who*) | Interrogative (*who?*) |
|----------|------------------|----------------------|------------------------|
| Determiner resistance | ✓ | ✓ | ✓ |
| Focus-modifier licensing | ✗ | ✗ | ✓ |
| Morphological paradigm | ✗ | partial | partial |

(Removed the "fused ✓" note — fused relatives pattern with other relatives, not with interrogatives.)

### Methodological concern: motivated reasoning?

The BCI explanation worked equally well for opposite empirical claims:

- **Original (wrong)**: Fused relatives foreground the wh-word (because it's the head), so precision modifiers work.
- **Revised (correct)**: Fused relatives background the wh-word (because they're still relatives), so precision modifiers fail.

Both stories *feel* principled. That's suspicious.

**What saves it (maybe):**

1. **The data came first.** Geoff provided the diagnostic; we adjusted the categorization. We didn't shop for data to fit the theory.

2. **The modifier itself is the test.** We're using the precision-modifier distribution to *diagnose* foregrounding status, then unifying it with other BCI phenomena (islands, etc.). That's not circular if the goal is unification, not independent prediction.

3. **It makes further predictions.** If this analysis is right, other foregrounding devices (focus particles, clefts) should pattern similarly with relatives. That's checkable.

**Lesson for the paper:** Don't overclaim. Say: "The BCI principle provides a unified account. The data confirm that fused relatives pattern with other relatives in backgrounding the wh-element." That's descriptively accurate without pretending we predicted it.

### Alternative test cases discussed

- **\*Exactly whoever he met helped him** — morphologically unambiguous fused relative (*-ever*). Also bad. But conflates the two explananda (semantic vs. pragmatic), so not used in paper.
- **\*Exactly what hair he had left was gray** — partitive fused relative. Unambiguous without special predicate. Used in paper.

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
