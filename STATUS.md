---
slug: focus-modifiers-interrogative-heads
kind: paper
title: Focus modifiers with interrogative heads
stage: complete
external: rejected
blocked_on: []
updated: 2026-07-07
source:
- STATUS.md
- PORTFOLIO.md
parked: true
venue: Glossa (OLH)
external_id: '27281'
notes: 'Rejected after review by Glossa 2026-07-07 (manuscript 27281, editor Agata Renans, Konstanz);
  reviews found the contrast interesting but the squib too compressed (BCI/precisification/alternatives,
  judgment grounding, and syntax/semantics literature all need expansion). Both STATUS.md and PORTFOLIO.md:28
  record Brett''s decision as: leave parked for now rather than rebuild. This is a deliberate deprioritization
  by Brett, not an external block. RESOLVED by ADJUDICATION 2026-07-30: this block is gap 8, and the new
  optional boolean `parked: true` is what it produced. blocked_on stays empty, because nothing external
  prevents Brett resuming work today; `parked: true` carries the deliberate-idleness the old ''parked''
  bucket meant, keeping the axes orthogonal instead of putting a non-blocker in blocked_on. This is the
  clear case of the three (with market-failures-with-nature and varieties-as-conditioning-structure):
  a decision to stop is on the record, not merely a quiet patch. STATUS.md and SESSION_LOG.md both record
  the squib was ''Posted to LingBuzz'' (2025-12-20) but no LingBuzz ID/URL is recorded anywhere in the
  project''s files (checked STATUS.md, DECISIONS.md, SESSION_LOG.md, README.md, AGENTS.md); preprints
  field omitted rather than guessed. The related Goldberg empirical-follow-up collaboration (PORTFOLIO.md:136)
  is a separate tracked project relationship, not part of this squib''s own state.'
claim:
  argues: >-
    Parked after Glossa rejection.
  provenance: drafted-from-map
  claim_updated: 2026-09-04
---

# STATUS.md

## Current State

**Status:** PARKED after Glossa rejection; no immediate revision planned
**Target:** None active; Glossa lane freed for other submissions
**Manuscript ID:** Glossa 27281
**Last updated:** 2026-07-07
**Editor:** Agata Renans (Konstanz)
**Decision:** Rejected after review on 2026-07-07; editor saw no viable way to publication in Glossa on the basis of the reviews.
**Reviews:** Private triage saved in `correspondence/glossa-reviews-2026-07-07.md` (ignored by git).
**October 2026 follow-up:** A three-lane run (semantic derivation, BCI made operational, counterexample hunt) with a two-auditor audit and hand-run COCA searches found G holds in usage for headed, pied-piped and supplementary relatives and fails for *-ever* fused relatives (*the hell*, post-head *exactly*). The December 2025 revision's line that fused relatives don't license precision modifiers holds for plain fused relatives only. Prior art: Tredinnick 1995 and her 2005 Penn dissertation (both read; `literature/tredinnick1995ever-free-relatives.pdf`, `literature/tredinnick2005semantics-free-relatives-ever.pdf`) and Dayal 1997. Results memo: `orchestration/results-memo.md` (gitignored); decisions in `DECISIONS.md`, 2026-10-27 and 2026-10-28.
**Next actions (Brett):** complete the `[TO CONFIRM]` fields in the drafted Humber REB application (`study-ever-exactly/reb/`, gitignored; a separate application from *independent-relative-whose*, due 2 November), after settling the platform's data handling; copy `study-focus-bci/design-revision-2026-10.md` to the shared Dropbox and send `correspondence/2026-10-28-email-to-adele-exactly-ever.md`.

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
- [x] Glossa decision received (rejected after review, 2026-07-07)
- [x] Park rather than rebuild for now; keep Glossa available for stronger submissions

## Session Summary

- **2026-07-07 Glossa decision**: Agata Renans rejected manuscript 27281 after reviews, saying she did not see a viable way to publication at Glossa. Review signal: interesting observation and potentially relevant theoretical issue, but the squib is too compressed; BCI/precisification/alternatives need spelling out; judgment sources and contexts need grounding; and the paper would need stronger engagement with NP/DP structure, degree modification, and wh/relative-clause literature. Brett's decision: this was not a strong enough paper to prioritize now, so park it rather than expand immediately; the useful consequence is that Glossa is free for another submission.
- **2026-07-04 status nudge**: Brett nudged Glossa about the pending squib. Prior state: Brett enquired 2026-05-17; Agata Renans replied 2026-05-20 that one reviewer was still outstanding and expected a decision within about a month.
- **2026-05-27 PM provenance/build cleanup**: Restored `references.bib` from the committed project-local bibliography after the central-bibliography symlink broke the Glossa build. The central bibliography lacks `hamblin1973`, `theiler2018`, and `cuneo2023`, all cited by `main-glossa.tex`; with the symlink, a temp build produced Biber missing-entry warnings and undefined citations. After restoration, a temp XeLaTeX/Biber build of `main-glossa.tex` completed with no missing-entry warnings and no undefined citations in the final log. No manuscript content changed. Added `.DS_Store` to `.gitignore`; the already tracked `study-focus-bci/.DS_Store` remains a separate hygiene issue.
- **2026-04-01**: Rebuilt the stimulus planning around a clean two-study design and produced a shareable discussion draft at `study-focus-bci/stimuli/two-track-stimulus-sets-draft.md`. Study 1 now distinguishes core subject relatives, exploratory subject `that`, integrated object relatives (`which/that/bare`), supplementary `which`, and free-relative / whole-NP families. Study 2 is now a contextual ranking study with a full text version and a smaller audio subset, using stable third-person reference frames instead of dialogue-dependent `I/you` alternations. The backgroundedness diagnostics were also redesigned so their task logic is internally coherent.
- **2026-04-01 (later)**: Tightened the stimulus bank before sharing it with Adele. The clean Study 1 text core is now human `who` only, with nonhuman subject `which` moved into a secondary replication family and the free-relative supplement given explicit interpretation probes. Applied sentence-level reviewer fixes across the exploratory `that` family, the free-relative supplement, the object/supplementary nonhuman families, Study 2 incongruent contexts, and the negation/discourse diagnostics. Exported Adele-facing Dropbox snapshots as `stimulus-redesign-for-adele-2026-04-01.{md,docx}` and drafted `study-focus-bci/email-to-adele-2026-04-01.md`.
- **2026-04-01 (pre-meeting review)**: Reviewed all shared materials in dropbox/Exactly/ and Adele's Feb 3 email. Ran two rounds of simulated review board (8 reviewers total) on `two-track-stimulus-sets-draft.md`. Round 1: design-level review (methodologist, semanticist, syntactician, skeptic). Round 2: stimulus-sentence-level review (same panel plus native-speaker naturalness audit). Consensus: Family B (core `who`) is cleanest; Family T (exploratory `that`) needs most work. Key theoretical finding: redundancy hypothesis (no live alternatives when head noun fixes referent) is a viable alternative to BCI with different predictions for free relatives. Key cross-cutting finding: *exactly* is not semantically uniform across conditions (exhaustivity vs. identity/precision vs. confirmatory emphasis). Concrete fix list produced: 13 priority items including verb replacements, extraction-type standardization, context strengthening, and confound removal. All review outputs in `/tmp/claude-agent-output/`.
- **2025-12-24**: **Goldberg collaboration offer.** Adele willing to collect data (late Jan / early Feb). Brett to create stimuli. Two predictions: (1) *exactly* blocked with relatives (backgroundedness), (2) gradient: better in it-clefts than subject-initial. Adele raises question about cleft prediction - not all clefts focus arguments (e.g., "It was 1972 when..."). Needs clarifying before stimuli.
- **2025-12-23**: **Geoff's critique addressed.** Revised paper to remove all claims about fused relatives patterning with interrogatives. Added Geoff's Frankenstein diagnostic example. Simplified generalization: precision modifiers licensed by interrogatives only. Added acknowledgments to Pullum and Goldberg.
- **2025-12-21**: Adele Goldberg feedback: "Brilliant! I find it totally compelling." Loves *precisify* and BCI terminology. Says it's inspiring her to revisit her 2006 chapter 7 work on scope/topicality.
- **2025-12-20**: Full draft from scratch to LingBuzz in ~9 hours. 4 pages, 4 citations. BCI as pragmatic explanation. XeLaTeX for proper PDF text extraction.
