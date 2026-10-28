# Replication protocol: *whatever* vs *what* with post-head *exactly*
<!-- SUMMARY: Brett's standalone rating study replicating his one-judge plain-what control with a sample; 2x2 within items, 16 lexical sets, 60 raters (power-simulated); Humber REB route alongside the independent-relative-whose packet · status: draft protocol, not submitted · updated: 2026-10-28 -->

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
within items; sixteen lexical sets; four lists in a Latin square, so each
participant sees each set once and each condition four times. Matrix predicates
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
`orchestration/lanes/data/` files); 6-16 are new. Braces give the four
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
| 9 | The tenant was charged for {whatever / what} {exactly / -} the inspector had found broken. | new |
| 10 | The editor cut {whatever / what} {exactly / -} the reviewer had objected to. | new |
| 11 | They auctioned off {whatever / what} {exactly / -} the estate had left behind. | new |
| 12 | The crew cleared away {whatever / what} {exactly / -} the storm had brought down. | new |
| 13 | Customs confiscated {whatever / what} {exactly / -} the traveller had declared. | new |
| 14 | The chef threw out {whatever / what} {exactly / -} the supplier had delivered that morning. | new |
| 15 | The new manager undid {whatever / what} {exactly / -} her predecessor had set up. | new |
| 16 | The court froze {whatever / what} {exactly / -} the company still owned. | new |

Notes before finalizing: frame 1's plain-*what* baseline was slightly
weaker than the others in Brett's check, so it may need replacing. Frame 5
is the only subject-position frame. On the plain-*what* + *exactly* items,
an in-situ question reading (*rejected what exactly?*) is possible; the
declarative punctuation and the probe should catch it.

**Fillers (draft, constructed):** 16, matched roughly in length to the
targets, none containing a wh word, *exactly* or *precisely*. Eight
clearly good:

1. The bakery on the corner closes early on Sundays in the winter.
2. Most of the guests had already left by the time the band arrived.
3. She folded the letter twice and slipped it into her coat pocket.
4. The committee postponed its decision until the spring meeting.
5. After the storm, the river rose higher than anyone had expected.
6. He keeps his tools in a wooden box under the kitchen sink.
7. The museum lent two of its paintings to a gallery in Montreal.
8. Our neighbours repainted their fence a surprisingly bright green.

Eight clearly bad (agreement, word order, or a missing argument):

9. The bakery on the corner close early on Sundays in the winter.
10. Most of the guests had already leaving by the time the band arrived.
11. She folded twice the letter and it slipped into her coat pocket.
12. The committee postponed until the spring meeting its the decision.
13. After the storm, the river rose more higher than anyone had expected.
14. He keeps in a wooden box his tools under the kitchen sink the.
15. The museum lent two of its paintings to in Montreal a gallery.
16. Our neighbours repainted their fence a surprisingly bright green very.

**Attention checks (2):** "For this sentence, please choose 2 on the
scale." and "For this sentence, please choose 6 on the scale.", placed in
the first and second halves of the list.

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
*independent-relative-whose* study. Target 60 after exclusions.

**Power (2026-10-28, `power_simulation.py`, output in
`power_simulation_output.txt`).** The estimand is an interaction, so the
April design's "about 35 for a medium effect" (Sprouse & Almeida 2017, for
simple contrasts) doesn't carry over. A simulation with cumulative-logit
data, crossed participant and item random effects (variance components
borrowed from the *independent-relative-whose* simulation, so priors, not
estimates), tested conservatively by participant and by item together,
gives:

| Lexical sets | Raters | Power if *exactly* costs plain *what* about 0.8 points more than *whatever* (latent 0.8) | about 1.15 points more (1.2) | about 1.5 points more (1.6) |
|---|---|---|---|---|
| 8 | 40 | 0.30 | 0.60 | 0.88 |
| 8 | 80 | 0.58 | 0.90 | 0.99 |
| 16 | 40 | 0.64 | 0.95 | 1.00 |
| 16 | 60 | 0.85 | 0.99 | 1.00 |

With 8 items the by-item test is the bottleneck, so more items buy more
than more raters. Sixteen sets and 60 raters cover an interaction of about
0.8 rating points (mean cell ratings in the simulation: *whatever* 5.1,
*whatever exactly* 4.9, *what* 4.9, *what exactly* 3.9). Brett's "clearly
worse" suggests at least that, but it's one judge's impression. The simulation approximates the planned ordinal
mixed model and should be rerun on the final items. Exclude participants who fail either
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

1. **Frame 1.** Its plain-*what* baseline was the weakest in Brett's
   check. Candidate replacement (constructed, same NP-complement
   structure): *The update quietly removed {whatever / what} {exactly / -}
   the old menu had offered.* Brett to pick one after a check by another
   native speaker.
2. Fillers and attention checks: drafted above (2026-10-28); Brett to
   review. With 16 targets, 16 fillers keeps the ratio at one to one.
3. Frames 9-16 (added 2026-10-28 after the power check): Brett to review.
4. *Precisely*: not in this round (decided 2026-10-28). The claim being
   replicated is about *exactly*; a *precisely* subset can follow if the
   interaction holds.
