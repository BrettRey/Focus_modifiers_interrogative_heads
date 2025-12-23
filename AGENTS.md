# Repository Guidelines

## Project Structure & Module Organization
- `main.tex` is the primary paper source; `main-ja.tex` is an alternate version.
- `references.bib` contains the bibliography used by `biber`.
- `.house-style/` holds the shared LaTeX preamble and the authoritative style rules (`style-guide.md`, `style-rules.yaml`).
- Notes and planning live in `draft-notes.md`, `annotated survey.md`, `foregrounding-analysis.md`, `STATUS.md`, and `SESSION_LOG.md`.
- Generated artifacts include `main.pdf`, `main.*`, `main-ja.*`, and `*.pdf` copies of sources; treat these as build outputs or reference files, not editing targets.

## Build, Test, and Development Commands
- Build the paper PDF (recommended workflow from `CLAUDE.md`):
  ```bash
  lualatex main.tex && biber main && lualatex main.tex && lualatex main.tex
  ```
- If you prefer XeLaTeX (hinted by the `% !TEX` directive), swap `lualatex` for `xelatex`, but keep the same `biber` pass sequence.
- There is no Makefile in this repo; run the command directly from the project root.

## Coding Style & Naming Conventions
- Follow the house style in `.house-style/style-guide.md` and the macros defined in `.house-style/preamble.tex`.
- Use the provided macros for mentions/quotes and examples (e.g., `\term{}`, `\enquote{}`, `\ea...\z`) rather than ad‑hoc formatting.
- Keep LaTeX source clean and readable; avoid editing generated `.aux`, `.bcf`, `.blg`, `.log`, `.out`, `.run.xml`, or `.pdf` files.

## Testing Guidelines
- No automated tests are configured.
- Validation = successful LaTeX build + clean bibliography (`biber`) + spot‑check the resulting `main.pdf` for layout or citation issues.

## Commit & Pull Request Guidelines
- This directory is not a Git repository, so there is no commit history to infer conventions.
- If you initialize Git, prefer concise, imperative messages (e.g., “Refine section 2 analysis”) and include the compiled PDF only if required by your workflow.
- For PRs, include a brief summary of changes and note the exact build command used to regenerate the PDF.

## House Style Updates (Optional)
- Updating `.house-style/` affects formatting across the paper; do this only intentionally.
- If you change style files, note the rationale in `STATUS.md` and rebuild the PDF to confirm the effect.
