# Repository Guidelines

## Project Overview

**Title:** Focus Modifiers with Interrogative Heads (working title)
**Type:** Squib
**Author:** Brett Reynolds
**Status:** Parked after Glossa rejection (2026-07-07). See `STATUS.md` for current state; do not duplicate status here.

## Core Argument (as submitted; see `main.tex` for the authoritative version)

Payne, Huddleston & Pullum (2010) analyze "precisely nothing" as adverbial modification of a determinative in NP structure. This squib addresses a related but distinct construction: focus modifiers with interrogative heads ("precisely who," "exactly what," "just which").

Current analysis in `main.tex`: *exactly/precisely/just/only* are focusing adverbs in peripheral modifier function in NP (CGEL p. 437). Interrogatives license them because interrogatives denote alternative sets requiring exhaustive identification. Relative constructions (integrated and fused alike) block them because relatives background the relative word, clashing with the foregrounding modifier (BCI principle, Goldberg 2006; Cuneo & Goldberg 2023).

Key points:

1. CGEL recognizes interrogatives allow special modifiers (post-head *else*, pre/post-head *exactly/precisely*, stacking *just exactly/precisely*) (CGEL pp. 592, 915-918).
2. The semantic questioned element may be smaller than the syntactic phrase (*whose* in *whose father*).
3. Focusing modifiers attach at the NP periphery, e.g. `[NP [AdvP:Mod precisely] [NP:Head who]]`, parallel to *precisely nothing*, *exactly that*.
4. Plain fused relatives pattern with integrated relatives, not interrogatives: `*Precisely what she built collapsed` (Pullum revision, 2025-12-23). *-ever* fused relatives don't: the October 2026 run found *the hell* and post-head *exactly* after *whatever* in usage. `main.tex` predates that finding. See `STATUS.md` and `DECISIONS.md` (2026-10-27, 2026-10-28).
5. The restriction is semantically natural: interrogatives denote alternatives/variable-values; *precisely/exactly* signals insistence on precise, exhaustive identification.

Key references:

- Huddleston & Pullum 2002 (CGEL): pp. 437, 592, 912, 915-918
- Payne, Huddleston & Pullum 2010 (adjectives/adverbs paper)
- Hamblin 1973; Groenendijk & Stokhof 1984 (alternatives, exhaustivity)
- Theiler, Roelofsen & Aloni 2018 (exactly who; strong exhaustivity)
- Goldberg 2006 (BCI); Cuneo & Goldberg 2023
- Quirk et al. 1985; König 1991 (focus particles)

## Project Structure & Module Organization

- `main.tex` is the primary paper source; `main-glossa.tex` is the Glossa submission version; `main-ja.tex` is an alternate version.
- `references.bib` is the committed project-local bibliography used by `biber`. Do not relink it to the central bibliography: the central file lacks cited keys (`hamblin1973`, `theiler2018`, `cuneo2023`) and the Glossa build breaks. See `DECISIONS.md` (2026-05-27).
- `.house-style/` holds the shared LaTeX preamble and the authoritative style rules (`style-guide.md`, `style-rules.yaml`).
- Notes and planning live in `notes/` (including `draft-notes.md`, `annotated survey.md`, `foregrounding-analysis.md`), plus `STATUS.md`, `DECISIONS.md`, and `SESSION_LOG.md` at the root.
- `study-focus-bci/` holds the Goldberg empirical follow-up (design, stimuli, micro-pilot). Use "free relative" in shared materials for Adele; retain "fused relative" (CGEL term) in the squib. See `DECISIONS.md` (2026-04-01).
- Generated artifacts include `main.pdf`, `main.*`, `main-ja.*`, `main-glossa.*`, and `*.pdf` copies of sources; treat these as build outputs or reference files, not editing targets.

## Build, Test, and Development Commands

- Build the paper PDF:
  ```bash
  xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
  ```
- The same sequence builds `main-glossa.tex`. Don't use LuaLaTeX: it runs words together in the PDF's text layer.
- There is no Makefile in this repo; run the command directly from the project root.

## Coding Style & Naming Conventions

- Follow the house style in `.house-style/style-guide.md` and the macros defined in `.house-style/preamble.tex`.
- Use the provided macros for mentions/quotes and examples (e.g., `\term{}`, `\enquote{}`, `\ea...\z`) rather than ad-hoc formatting.
- Keep LaTeX source clean and readable; avoid editing generated `.aux`, `.bcf`, `.blg`, `.log`, `.out`, `.run.xml`, or `.pdf` files.

## Testing Guidelines

- No automated tests are configured.
- Validation = successful LaTeX build + clean bibliography (`biber`) + spot-check the resulting `main.pdf` for layout or citation issues.

## Commit & Pull Request Guidelines

- This is a Git repository (`master`, remote `origin`). Prefer concise, imperative commit messages (e.g., "Refine section 2 analysis"); recent history also uses `feat:` prefixes for additions. Include the compiled PDF only if required by your workflow.
- For PRs, include a brief summary of changes and note the exact build command used to regenerate the PDF.

## House Style Updates (Optional)

- Updating `.house-style/` affects formatting across the paper; do this only intentionally.
- If you change style files, note the rationale in `STATUS.md` and rebuild the PDF to confirm the effect.

## Model Routing

Choose the models and any redundancy yourself, following the portfolio rule in `LLM-CLI-projects/.claude/rules/multi-model-dispatch.md`; don't ask Brett. Participant data from the rating study stays off external routes once collected.
