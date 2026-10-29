# Rating study: *whatever* vs *what* with post-head *exactly* (protocol v2)
<!-- SUMMARY: Brett's standalone rating study of whether -ever reduces the cost of post-head exactly in fused relatives; 24 frames x 4 conditions per rater, per-rater random orders, pilot then 100-150 raters set by a design analysis; Humber REB · status: draft v2 after two independent reviews, not submitted · updated: 2026-10-28 -->

Draft by Brett with Claude, 2026-10-28. Revised after independent reviews
by Astra and Wonder Full (`../orchestration/reviews/2026-10-28/`). Run by
Brett alone; the backgroundedness test is a separate proposal to Adele
Goldberg (`../study-focus-bci/design-revision-2026-10.md`).

## Question

How much more does post-head *exactly* lower the acceptability of a fused
relative headed by plain *what* than one headed by *whatever*? Brett's own
judgments on five attested frames (one judge, the squib's author, so a
go/no-go check, not data) found *whatever* without *exactly* slightly
better than with it, and plain *what* + *exactly* clearly worse than plain
*what*. That is an interaction with a small cost of *exactly* after
*whatever*. This study estimates the interaction from naive raters.

## Design

2 (wh: *whatever* / *what*) × 2 (modifier: post-head *exactly* / none),
within frames. 27 frames in all; each rater sees 24 of them once each
(one member of each near-twin pair), six in each condition, assigned by a
four-list Latin square. Every rater gets a
separate random order (constraints below), so condition and list aren't
tied to position. Matrix predicates take NP complements and not
interrogative ones, except frame F05 (subject position, attested), kept
deliberately.

**Estimand:** the interaction: (*whatever exactly* − *whatever*) −
(*what exactly* − *what*), in rating points and on the model's latent
scale, with its 95% interval.

**Expectation (stated before data):** positive, i.e. *exactly* costs more
after *what*. A small cost after *whatever* is expected too. Nothing here
is a significance test of a point null; the result is the estimate and
its interval.

**What would count against the expectation:** an interaction near zero or
negative, with an interval that excludes effects of the size Brett's
judgments suggest.

## Items

Frames are constructed. F01-F05 are adapted from attested web examples;
F17-F21 were added alongside five structurally unusual frames; the rest
are new. Braces give the four conditions. Wording is generated from
`build_materials.py`, the single source; this table is regenerated from
it.

| # | Frame | Source |
|---|---|---|
| F01 | The new release will still support {whatever / what} {exactly / -} this feature is, but behind a setting. | adapted from HN 34295663 |
| F02 | He went straight to the minister with {whatever / what} {exactly / -} it is that the analyst told him. | adapted from iWeb (bipartisanreport.com) |
| F03 | The introduction then eases into {whatever / what} {exactly / -} the writer is trying to say. | adapted from iWeb (privatewriting.com) |
| F04 | Meaning can't be reduced to {whatever / what} {exactly / -} is allowed in a physical description. | adapted from iWeb (usyd.edu.au) |
| F05 | {Whatever / What} {exactly / -} it was they were doing suddenly stopped. | adapted from iWeb (pompeiana.org) |
| F06 | The landlord blamed the leak on {whatever / what} {exactly / -} the plumber had installed. | new |
| F07 | She gave the museum {whatever / what} {exactly / -} her grandmother had left her. | new |
| F08 | The committee rejected {whatever / what} {exactly / -} the consultant had proposed. | new |
| F09 | The tenant was charged for {whatever / what} {exactly / -} the inspector had found broken. | new |
| F10 | The editor cut {whatever / what} {exactly / -} the reviewer had objected to. | new |
| F11 | They auctioned off {whatever / what} {exactly / -} the estate had left behind. | new |
| F12 | The crew cleared away {whatever / what} {exactly / -} the storm had brought down. | new |
| F13 | Customs confiscated {whatever / what} {exactly / -} the traveller had failed to declare. | new |
| F14 | The chef threw out {whatever / what} {exactly / -} the supplier had delivered. | new |
| F15 | The new manager undid {whatever / what} {exactly / -} her predecessor had set up. | new |
| F16 | The court froze {whatever / what} {exactly / -} the company owned. | new |
| F17 | He went straight to the minister with {whatever / what} {exactly / -} the analyst had told him. | new (variant of F02) |
| F18 | The janitor repaired {whatever / what} {exactly / -} the students had damaged. | new (object frame added alongside subject frame F05) |
| F19 | The movers packed {whatever / what} {exactly / -} the family had stored in the garage. | new (alternative to F07) |
| F20 | The tenant paid for {whatever / what} {exactly / -} the inspector had flagged. | new (variant of F09) |
| F21 | The editor deleted {whatever / what} {exactly / -} the reviewer had marked. | new (variant of F10) |
| F22 | The insurer refused to cover {whatever / what} {exactly / -} the flood had destroyed. | new |
| F23 | The volunteers sorted {whatever / what} {exactly / -} the donors had dropped off. | new |
| F24 | The archivist catalogued {whatever / what} {exactly / -} the professor had kept in his office. | new |
| F25 | The mechanic replaced {whatever / what} {exactly / -} the previous owner had fitted. | new |
| F26 | The school banned {whatever / what} {exactly / -} the children had been bringing to class. | new |
| F27 | The collector returned {whatever / what} {exactly / -} the artist had sent him. | new |

**Near-twins go to different raters.** Three pairs share most of their
wording (F02/F17, F09/F20, F10/F21). Each rater sees one member of each pair (half the
raters get one version, half the other), so nobody meets two sentences
that differ mainly in the manipulated words. With 18 other frames and the
three pairs, every rater still rates 24 frames, six per condition. A
vocabulary check flagged no other co-occurring sentences sharing more
than one common word.

F02 and F05 contain *it is that* / *it was*, which echoes the question
formula *what (exactly) it is that...*; F05 also opens like a question.
That can enlarge the *what* + *exactly* penalty in those frames. It's an
interaction with the frame, not a confound (the feature is in all four
versions), and both frames are reported separately.

**Fillers (24, distinct contents, no minimal pairs).** Twelve natural,
some with *what*, *whatever* or *exactly* outside the target
construction: *The bakery on the corner closes early on Sundays in the winter*; *She folded the letter twice and slipped it into her coat pocket*; *The council postponed its decision until the spring meeting*; *He keeps his old camera in a box under the kitchen sink*; *The recipe calls for exactly two eggs and a cup of flour*; *Nobody on the platform knew what time the last train left*; *Whatever the forecast says, we're having the picnic on Saturday*; *The orchestra performed its best-known symphony at a festival in Montreal*; *Our neighbours repainted their front door a surprisingly bright green*; *The coach asked the players what they had eaten before the match*; *The library extended its hours during the week before exams*; *After the heavy rain, the river rose higher than anyone had expected*. Twelve unnatural (agreement, word order, stray or
misplaced words): *The farmer have sold most of his sheep at the autumn market*; *Most of the guests had already leaving by the time the band arrived*; *The nurses finished the shift an hour early the*; *She put on the table the flowers that her friend had brought her yesterday the*; *The tailor shortened two exactly centimetres the trousers*; *The tourists asked the guide where the station is it*; *He gave to his brother for his birthday it*; *The bus driver were stopped for speeding on the highway last night*; *The puppies is sleeping in the basket by the stove*; *Whatever says the doctor, I'm going to finish the race*; *The lecture went on longer more than the audience had planned for*; *The gardener a fence painted brown new around the vegetables*.

**Practice (3, not analysed):** *The children planted tomatoes along the
back wall of the garden* (natural); *The children planted along the back
wall the tomatoes* (in between); *The children planted along the back
wall tomatoes of garden the* (unnatural).

**Attention checks (2):** "To show you're reading carefully, please
choose 2 for this sentence." and the same with 6, one in each half.

## Task

**Rating block.** 3 practice trials, then 50 trials (24 targets, 24
fillers, 2 checks), one sentence at a time, rated 1-7 for naturalness.
Order is random per rater, with at most two targets in a row, never two
targets of the same condition adjacent, and one check in each half (not in
the first three positions). No questions interrupt the ratings.

**Interpretation block, after all ratings.** Sixteen sentences shown
again: 8 of the rater's targets (two per condition, rotated so all 108
frame × condition cells are probed across raters, the twin frames about half as often) and 8
natural fillers. Two questions each: "Is this sentence a statement or a
question?" (statement / question / can't tell), which catches in-situ or
echo-question readings; and "Does the speaker seem to know which [noun]
it was?" with a frame-specific noun (*they were* for plural nouns; yes /
no / can't tell), which checks
the identity reading. Neither question uses *whatever* or *exactly*; the
order of the two substantive options is randomized.

## Pilot, then main study

**Pilot:** about 30 raters, same materials. Purpose: estimate how much the
interaction varies across frames, check the interpretation questions and
the fillers, and time the session. Pilot data are not pooled with the
main study.

**Decision after the pilot:** if frames vary substantially in the size of
the interaction (pilot estimate of the frame-level SD of the interaction
at about twice the assumed 0.18 on the latent scale or more), write a
second set of 24 frames and split the 48 across raters, 24 each; otherwise
keep 24 frames for everyone. Simulations (2026-10-28): with frames as
similar as assumed, splitting barely changes the interval (±0.28 to ±0.27
points at 100 raters); with frame variability three times the assumption,
48 split frames narrow it from ±0.36 to ±0.31. A 30-rater pilot estimates
that SD only roughly, so the decision should use its interval, not its
point estimate. The REB application describes this branch; a second
frame set goes to the REB as a change request before it's used.

**Main study sample:** 100 raters after exclusions, 150 if the budget
allows. Design analysis (Gelman & Carlin 2014; `design_analysis.py`,
output in `design_analysis_output.txt`, run with 16 frames; 24 frames does
somewhat better): at 100 raters the 95% interval for the interaction is
about ±0.35 points and a significant estimate of a 0.5-point effect is
inflated by about 20%; at 150, ±0.29 and about 10%. With 24 frames, 100
raters gives about ±0.29. Assumptions: variance components borrowed from
the *independent-relative-whose* simulation, replaced by pilot estimates
before the main run.

## Analysis

Cumulative-logit (ordinal) mixed model, fitted with brms in R:
`rating ~ wh * modifier + (1 + wh * modifier | rater) + (1 + wh * modifier | frame)`,
with sum coding (±0.5) so the interaction coefficient is the
difference-of-differences on the latent scale. Weakly informative priors
(normal(0, 1.5) on the population-level effects; defaults otherwise),
written into the preregistration. Report the interaction's posterior
median and 95% interval on the latent scale and as the implied difference
in expected rating. A frequentist check with `ordinal::clmm` (same fixed
effects; random intercepts and the interaction slope) is reported
alongside.

Planned robustness estimates: the five attested frames alone; F02 and
F05 separately; excluding trials whose interpretation answer was
"question"; trial position as a covariate. Brett's own judgments are
reported separately and never pooled.

**Descriptive: number of the free relative's referent.** Coded by frame
from the interpretation noun, fixed before data: singular count (F01,
F03, F04, F05, F06, F08, F10, F21), non-count (F02, F12, F14, F17, F20,
F22), plural (F07, F09, F11, F13, F15, F16, F18, F19, F23, F24, F25,
F26, F27). The main model's frame-level estimates of the interaction are
summarized by class, and the "know which" answers are reported by class.
No current account predicts a difference. Tredinnick (2005), following
von Fintel (2000), gives an *-ever* free relative an ignorance reading
with a plural referent (p. 25, (50)) and finds universal-like behaviour
only on the indifference reading, whether the sortal is singular, plural
or absent (p. 64); Dayal (1997, p. 104) finds plurality neither
necessary nor sufficient for universal-like behaviour. Her earlier paper
tied the don't-know reading to a referent of cardinality one (Tredinnick
1995, pp. 258-261). The summary is descriptive: 13 of the 27 frames are
plural, and number is confounded with source and content (all five
attested frames are singular or non-count). A test of number would need
matched singular and plural versions of the same frames.

**Exclusions** (also in the REB text): raters who fail either attention
check; raters whose mean rating of the unnatural fillers is not at least
one point below their mean rating of the natural fillers; incomplete
sessions. Exclusions are applied before any look at the targets.

## Ethics and platform

Humber REB, on the platform route of the *independent-relative-whose*
study. Minimal risk: ratings of constructed sentences, de-identified for
analysis. Draft REB text: `REB-ADDENDUM.md`.

## Materials

`build_materials.py` holds the wording above and writes
`items/all_items.csv` (96 target versions plus fillers, checks and
practice) and one deck per rater in `items/decks/` (160 decks, 40 per
list), then validates: 3 practice + 50 rating trials + 16 interpretation
sentences × 2 questions per deck; every frame × condition rated in 40
decks (20 for the twin frames); order constraints; no *whatever* or *exactly* in any question.

## Open before submission

1. ~~Brett: check frames F17-F27 and the 24 fillers.~~ Done 2026-10-28: the *whatever* and plain *what* baselines of F17-F27 and the fillers "seem fine" (Brett).
2. Pilot timing; then the main-study sample within 100-150.
3. Write the preregistration from this file.
