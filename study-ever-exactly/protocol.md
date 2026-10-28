# Replication protocol: *whatever* vs *what* with post-head *exactly*
<!-- SUMMARY: Brett's standalone rating study replicating his one-judge plain-what control with a sample; 2x2 within items, 8 lexical sets, ~40 raters; Humber REB route alongside the independent-relative-whose packet · status: draft protocol, not submitted · updated: 2026-10-28 -->

Draft by Brett with Claude, 2026-10-28. Run by Brett alone, separate from
the joint study with Adele Goldberg (`../study-focus-bci/`), which keeps
the backgroundedness test (`../study-focus-bci/design-revision-2026-10.md`).
The squib's main new claim rests on this replication.

## Question

Does post-head *exactly* in a fused relative need what *-ever* adds? In
five attested frames, Brett judged plain *what* + *exactly* worse than
*whatever* + *exactly*, and plain *what* without *exactly* fine (one
judge, the squib's author). This study asks whether naive raters show the
same interaction.

## Design

2 (wh: *whatever* vs *what*) × 2 (modifier: post-head *exactly* vs none),
within items; eight lexical sets; four lists in a Latin square, so each
participant sees each set once and each condition twice. Matrix predicates
take NP complements and not interrogative ones, so plain *what* can only
be a fused relative.

**Estimand:** the wh × modifier interaction, i.e. how much more *exactly*
costs with *what* than with *whatever*.

**Prediction (stated before data):** the interaction is in that direction,
and *whatever exactly* is not reliably worse than *whatever* alone.

**What would count against it:** no interaction, or *exactly* costing as
much with *whatever* as with *what*.

## Items

Constructed. Frames 1-5 are adapted from attested web examples (sources
in the right column; contexts in the project's
`orchestration/lanes/data/` files); 6-8 are new. Braces give the four
conditions.

| # | Frame | Source |
|---|---|---|
| 1 | The new release will still support {whatever / what} {exactly / -} this feature is, but behind a setting. | adapted from HN 34295663 |
| 2 | He went straight to the minister with {whatever / what} {exactly / -} it is that the analyst told him. | adapted from iWeb (bipartisanreport.com) |
| 3 | The introduction then eases into {whatever / what} {exactly / -} the writer is trying to say. | adapted from iWeb (privatewriting.com) |
| 4 | Meaning can't be reduced to {whatever / what} {exactly / -} is allowed in a physical description. | adapted from iWeb (usyd.edu.au) |
| 5 | {Whatever / What} {exactly / -} it was they were doing suddenly stopped. | adapted from iWeb (pompeiana.org) |
| 6 | The landlord blamed the leak on {whatever / what} {exactly / -} the plumber had installed. | new |
| 7 | She gave the museum {whatever / what} {exactly / -} her grandmother had left her. | new |
| 8 | The committee rejected {whatever / what} {exactly / -} the consultant had proposed. | new |

Notes before finalizing: frame 1's plain-*what* baseline was slightly
weaker than the others in Brett's check, so it may need replacing. Frame 5
is the only subject-position frame. On the plain-*what* + *exactly* items,
an in-situ question reading (*rejected what exactly?*) is possible; the
declarative punctuation and the probe should catch it.

**Fillers:** 16, about half clearly good and half clearly bad, matched in
length, anchoring the scale. Two attention checks.

## Task

One sentence per trial, rated 1-7 for naturalness ("1 = very unnatural,
7 = very natural"), as in the April joint design. After each target, an
interpretation probe: "What did [subject] [verb]?" with options (a) a
particular thing the speaker could name, (b) something, whatever it was,
(c) unclear. The probe checks that *whatever* items get the open-identity
reading and plain *what* items the referential one; it's analysed
separately and doesn't gate the rating analysis.

## Participants and sample

Adult native speakers of English on the platform route used for the
*independent-relative-whose* study. The April joint design cites Sprouse
& Almeida (2017) for about 35 participants for a medium effect on a 7-point
scale; target 40 after exclusions. Exclude participants who fail either
attention check or rate the clearly bad fillers above the clearly good
ones on average.

## Analysis

Ordinal mixed model: rating ~ wh × modifier, with random intercepts and
slopes for participants and items as far as they converge (simplify
following Barr et al. 2013, as in the April design). The interaction is
the test; the simple effect of *exactly* within *whatever* is the
secondary check. Report Brett's own judgments separately, not pooled.

## Ethics and platform

Humber REB, as a second small experiment alongside the
*independent-relative-whose* packet (see that project's `STATUS.md` for
the REB and platform route). Anonymous adult ratings of constructed
sentences, minimal risk.

## Open before submission

1. Replace frame 1 if its plain-*what* baseline stays weak in a check by
   another native speaker.
2. Write the fillers and the attention checks.
3. Decide whether *precisely* gets a later replication subset, as the
   April design planned for the joint study.
