# Decisions Log

Append-only record of project decisions. Agents: add an entry whenever a non-trivial decision is made during a session (structural changes, venue choices, theoretical commitments, scope changes, reviewer feedback acted on). Keep entries short.

Format: `## YYYY-MM-DD` then bullet points with **bold topic** and brief rationale.

---

## 2026-07-07

- **Glossa rejection recorded and paper parked.** Agata Renans declined manuscript 27281 after reviews, saying she saw no viable way to publication in Glossa. The reviews treat the observation as interesting but the squib as underdeveloped: BCI/precisification/alternatives need detail, judgments need contextual grounding, and the syntax/semantics literature base would need expansion. Brett's decision is to leave the paper parked for now rather than rebuild it immediately; Glossa is now available for stronger future submissions.

## 2026-05-27

- **Local bibliography restored for Glossa build reproducibility.** Reverted the `references.bib` symlink back to the committed project-local bibliography because the central bibliography is missing cited keys used by `main-glossa.tex` (`hamblin1973`, `theiler2018`, `cuneo2023`). A temp XeLaTeX/Biber build failed citation resolution before restoration and completed cleanly afterward. Do not relink this project to the central bibliography unless the missing keys are first merged centrally and the Glossa build is rechecked.
- **Artifact hygiene.** Added `.DS_Store` to `.gitignore`; the already tracked `study-focus-bci/.DS_Store` still needs a later hygiene decision.

## 2026-04-01

- **Two-study structure.** Treat the project as two linked studies: Study 1 establishes the distribution of `exactly` across interrogatives, free relatives, and headed relatives; Study 2 tests the focus/backgrounding explanation with definite NPs.
- **Structure as target.** Treat the target of judgment as the intended structure, not the raw string; use audio where prosody is needed to specify that structure.
- **Study 1 coverage.** Split Study 1 into a core subject-relative family, a separate exploratory subject `that` family, an integrated object-relative extension (`which` / `that` / bare), a supplementary `which` benchmark, and a free-relative / whole-NP supplement.
- **Study 2 task.** Make Study 2 a contextual ranking design rather than grammaticality judgment; use a full text study plus a smaller audio subset built on the same response set.
- **Study 2 reference frame.** Remove dialogue-dependent `I/you/we` deictics from Study 2 and use stable third-person descriptions throughout the text and audio materials.
- **Diagnostics redesign.** Keep negation and discourse diagnostics, but use identical negation probes within pairs and givenness-friendly discourse prompts so the diagnostics test backgrounded packaging rather than mismatched answerhood.
- **Clean Study 1 core.** Treat human subject `who` as the first-pass clean text core; move nonhuman subject `which` into a separate replication family interpreted together with the supplementary `which` benchmark.
- **Free-relative interpretation.** Add explicit interpretation probes to the free-relative supplement rather than assuming participants recover the intended free-relative reading.
- **Exploratory diagnostics status.** Mark the backgroundedness diagnostics as exploratory rather than part of the clean first-round demonstration.
- **Stimulus review fixes.** Standardize the exploratory `that` family, tighten weak Study 2 incongruent contexts, replace pragmatic and lexical confounds in the C/G/H families, and make O/S continuations more consequential before sharing the draft.
- **Sharing policy.** Keep the repo markdown file as the canonical source and put ordinary Dropbox snapshot copies there as `.md` and `.docx`; do not use symlinks for Adele-facing materials.
- **Redundancy as alternative hypothesis.** Raised during pre-meeting prep: the headed-relative block on *exactly* may be redundancy (head noun already fixes referent, leaving no live alternatives) rather than BCI (backgrounded content). Makes different predictions for free relatives (fine under redundancy, degraded under BCI), focus manipulation (no help under redundancy, helps under BCI), and appositives (still bad under redundancy, improves under BCI). Study 1 free-relative results will adjudicate.
- **Terminology alignment with Adele.** Use "free relative" in all shared materials; retain "fused relative" (CGEL term) in the squib. Adele objects to "fused" as theory-laden.
- **Review-board findings (round 2, stimulus-focused).** Eight simulated reviewers across two rounds. Consensus: Family B (core `who` subject-relatives) is cleanest; Family T (exploratory `that`) needs most work (mixed extraction types, complement-clause garden path in T4, ambiguous interrogative verbs). Key cross-cutting finding: *exactly* is not semantically uniform — exhaustivity in interrogatives, identity/precision in free relatives, confirmatory emphasis in supplementary relatives. Analysis must not treat acceptability as measuring the same licensing mechanism everywhere.
- **Adele's Feb 3 positions.** She treats *know + what-clause* as free RC (not interrogative); predicts free relatives will allow *exactly*; wants 7-point scale; wants fuller paradigm in Block 1; objects to Block 3 verb choices (decisive). Her prediction that free relatives differ from headed relatives is the key empirical bet.
