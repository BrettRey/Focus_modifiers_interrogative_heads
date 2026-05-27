# STATUS.md

## Current State

**Status:** SUBMITTED to Glossa; under review, one reviewer outstanding as of 2026-05-20
**Target:** Glossa (squib, ≤5000 words)
**Manuscript ID:** 27281
**Last updated:** 2026-05-27
**Editor:** Agata Renans (Konstanz)
**Expected decision:** within ~one month (by ~2026-06-20) per editor's 2026-05-20 reply to Brett's 2026-05-17 status enquiry

## Progress

- [x] Initial argument sketched
- [x] Target venue identified (Glossa)
- [x] House style added
- [x] Formal write-up polished
- [x] Example sentences collected
- [x] Rhetorical improvements (inclusio, tricolon, epigrammatic close)
- [x] Title revised with empirical hook
- [x] CGEL terminology standardized
- [x] *Only* added to modifier class
- [x] Open questions expanded
- [x] Keywords added
- [x] Posted to LingBuzz
- [x] Pullum revision: fused relatives don't license precision modifiers
- [x] Update LingBuzz
- [x] Glossa submission (Dec 23)

## Session Summary

- **2026-05-27 PM provenance/build cleanup**: Restored `references.bib` from the committed project-local bibliography after the central-bibliography symlink broke the Glossa build. The central bibliography lacks `hamblin1973`, `theiler2018`, and `cuneo2023`, all cited by `main-glossa.tex`; with the symlink, a temp build produced Biber missing-entry warnings and undefined citations. After restoration, a temp XeLaTeX/Biber build of `main-glossa.tex` completed with no missing-entry warnings and no undefined citations in the final log. No manuscript content changed. Added `.DS_Store` to `.gitignore`; the already tracked `study-focus-bci/.DS_Store` remains a separate hygiene issue.
- **2026-04-01**: Rebuilt the stimulus planning around a clean two-study design and produced a shareable discussion draft at `study-focus-bci/stimuli/two-track-stimulus-sets-draft.md`. Study 1 now distinguishes core subject relatives, exploratory subject `that`, integrated object relatives (`which/that/bare`), supplementary `which`, and free-relative / whole-NP families. Study 2 is now a contextual ranking study with a full text version and a smaller audio subset, using stable third-person reference frames instead of dialogue-dependent `I/you` alternations. The backgroundedness diagnostics were also redesigned so their task logic is internally coherent.
- **2026-04-01 (later)**: Tightened the stimulus bank before sharing it with Adele. The clean Study 1 text core is now human `who` only, with nonhuman subject `which` moved into a secondary replication family and the free-relative supplement given explicit interpretation probes. Applied sentence-level reviewer fixes across the exploratory `that` family, the free-relative supplement, the object/supplementary nonhuman families, Study 2 incongruent contexts, and the negation/discourse diagnostics. Exported Adele-facing Dropbox snapshots as `stimulus-redesign-for-adele-2026-04-01.{md,docx}` and drafted `study-focus-bci/email-to-adele-2026-04-01.md`.
- **2026-04-01 (pre-meeting review)**: Reviewed all shared materials in dropbox/Exactly/ and Adele's Feb 3 email. Ran two rounds of simulated review board (8 reviewers total) on `two-track-stimulus-sets-draft.md`. Round 1: design-level review (methodologist, semanticist, syntactician, skeptic). Round 2: stimulus-sentence-level review (same panel plus native-speaker naturalness audit). Consensus: Family B (core `who`) is cleanest; Family T (exploratory `that`) needs most work. Key theoretical finding: redundancy hypothesis (no live alternatives when head noun fixes referent) is a viable alternative to BCI with different predictions for free relatives. Key cross-cutting finding: *exactly* is not semantically uniform across conditions (exhaustivity vs. identity/precision vs. confirmatory emphasis). Concrete fix list produced: 13 priority items including verb replacements, extraction-type standardization, context strengthening, and confound removal. All review outputs in `/tmp/claude-agent-output/`.
- **2025-12-24**: **Goldberg collaboration offer.** Adele willing to collect data (late Jan / early Feb). Brett to create stimuli. Two predictions: (1) *exactly* blocked with relatives (backgroundedness), (2) gradient: better in it-clefts than subject-initial. Adele raises question about cleft prediction - not all clefts focus arguments (e.g., "It was 1972 when..."). Needs clarifying before stimuli.
- **2025-12-23**: **Geoff's critique addressed.** Revised paper to remove all claims about fused relatives patterning with interrogatives. Added Geoff's Frankenstein diagnostic example. Simplified generalization: precision modifiers licensed by interrogatives only. Added acknowledgments to Pullum and Goldberg.
- **2025-12-21**: Adele Goldberg feedback: "Brilliant! I find it totally compelling." Loves *precisify* and BCI terminology. Says it's inspiring her to revisit her 2006 chapter 7 work on scope/topicality.
- **2025-12-20**: Full draft from scratch to LingBuzz in ~9 hours. 4 pages, 4 citations. BCI as pragmatic explanation. XeLaTeX for proper PDF text extraction.
