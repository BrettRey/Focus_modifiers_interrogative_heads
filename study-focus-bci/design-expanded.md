# Experimental Design: BCI and Focus Modification (Expanded)

**Version:** 2.0  
**Date:** 2026-01-06  
**Status:** Stimuli drafted; awaiting Adele's input

---

## Overview

This study tests whether information structure predicts the acceptability of precision modifiers (*exactly*, *precisely*, *just*) in the same way it predicts extraction island effects.

## Theoretical Background

Goldberg's (2006) Backgrounded Constituent Infelicity (BCI) principle: foregrounding and backgrounding the same constituent is infelicitous. This explains extraction islands—the fronted phrase is foregrounded, but island contexts background it.

**Extension hypothesis:** Precision modifiers foreground the NP they attach to. If the NP is backgrounded, the result is infelicitous, parallel to extraction islands.

---

## Predictions

### Prediction 1: Relative Clauses Block Modifiers (Categorical)

Relative clauses background their head. Therefore, precision modifiers should be blocked:

| Construction | Example | Prediction |
|--------------|---------|------------|
| Interrogative | *Exactly who called?* | ✓ Acceptable |
| Integrated relative | *The person exactly who called left.* | ✗ Unacceptable |
| Fused relative | *Precisely what she built collapsed.* | ✗ Unacceptable |

**Design:** 2 (Construction: interrogative vs. relative) × 2 (Modifier: ±*exactly*)

**Expected:** Main effect of Construction; Modifier × Construction interaction with penalty larger for relatives.

### Prediction 2: Focus Congruence Predicts Gradience (Gradient)

Within the same syntactic frame, discourse-focus status should modulate acceptability:

| Context Type | Discourse Status | Example | Prediction |
|--------------|------------------|---------|------------|
| Focus-congruent | NP is new/contrastive | A: *Which cats?* → B: *Exactly the cats you mentioned.* | Better |
| Focus-incongruent | NP is given/topical | A: *What did they do?* → B: *Exactly the cats you mentioned were playing.* | Worse |

**Design:** 2 (Frame: subject-initial vs. it-cleft) × 2 (Context: focus-congruent vs. incongruent) × 2 (Modifier: ±*exactly*)

**Expected:** Three-way interaction; modifier penalty ameliorated in focus-congruent clefts.

**Adele's concern (Dec 24):** Not all it-clefts focus arguments. Solution: Use specificational clefts with clear argument focus.

---

## Methodology

### Task Selection

Following Schütze & Sprouse (2014):

| Task | Pros | Cons | When to use |
|------|------|------|-------------|
| **Forced-choice** | Most powerful for detecting differences | No gradient info | Categorical contrasts (Pred 1) |
| **7-point Likert** | Intuitive; adequate power at n≥30 | Less sensitive | Gradient effects (Pred 2) |
| **Magnitude estimation** | Continuous scale | High variance; complex | Not recommended here |

**Recommendation:** 7-point Likert throughout for consistency with Cuneo & Goldberg (2023).

### Cuneo & Goldberg's Two-Task Approach

Their innovation: operationalize backgroundedness *independently* of the target construction via:

1. **Negation task:** Does negating the sentence deny the existence of the NP referent, or only the predicate? (If latter: NP is presupposed/backgrounded)
2. **Discourse task:** In dialogue, which construction would be expected first? (More direct = less backgrounded)

**Decision point:** Adopt C&G's approach (more theoretically motivated) or simpler single-task design?

### Stimuli Requirements

- **Multiple lexicalizations:** ≥8 per condition (currently 8 item sets drafted)
- **Latin Square distribution:** Each participant sees one version per item
- **Fillers:** ~50% of trials; anchor scale endpoints; prevent strategy formation
- **Instructions:** "Imagine a friend said this to you. How natural does it sound?"

---

## Sample Size and Power

Based on Sprouse & Almeida's power analyses:

| Effect size | 7-point Likert | Forced-choice |
|-------------|----------------|---------------|
| Large | n ≈ 20 | n ≈ 10 |
| Medium | n ≈ 35 | n ≈ 15 |
| Small | n ≈ 80 | n ≈ 30 |

**Target:** n = 100+ (conservative; allows detection of small-medium effects)

Cuneo & Goldberg (2023) used N = 680 across multiple conditions; our simpler design likely needs n = 100–150.

---

## Analysis Plan

### Pre-processing

1. Exclude participants with <80% accuracy on filler catch trials
2. z-score transform ratings within participant
3. Remove outliers >3 SD from condition mean

### Statistical Models

**Prediction 1:**
```
rating ~ construction * modifier + (1 + construction * modifier | subject) + (1 + construction * modifier | item)
```

**Prediction 2:**
```
rating ~ frame * context * modifier + (1 + frame * context * modifier | subject) + (1 + frame * context * modifier | item)
```

If maximal random structure doesn't converge, simplify following Barr et al. (2013).

### Key Tests

- **Prediction 1:** Significant Construction × Modifier interaction
- **Prediction 2:** Significant Frame × Context × Modifier interaction; simple effects showing modifier penalty reduced in focus-congruent clefts

---

## Stimuli Location

See: `stimuli/draft-stimuli-v1.md`

---

## Timeline

| Phase | Target Date | Milestone |
|-------|-------------|-----------|
| Stimuli draft | ✓ 2026-01-06 | 8 item sets created |
| Adele review | 2026-01-10 | Feedback on design + stimuli |
| Stimuli revision | 2026-01-15 | Final stimuli locked |
| Ethics/IRB | 2026-01-15 | Princeton IRB (Adele's institution) |
| Pilot | Late Jan | Small pilot (n~20) |
| Data collection | Early Feb | Full sample (n=100+) |
| Analysis | Feb 2026 | Results ready |
| Write-up | Mar 2026 | Submit as empirical follow-up |

---

## Open Questions

1. **Task choice:** Single acceptability task, or C&G-style backgroundedness + acceptability?
2. **Modifier variety:** Consistent *exactly*, or vary *exactly/precisely/just*?
3. **NPI angle:** Worth testing negation contexts to probe weak-NPI status?
4. **Fused relatives:** Include as separate condition or just controls?
5. **Platform:** Prolific? MTurk? Lab-based?

---

## References

Cuneo, N., & Goldberg, A. E. (2023). The discourse functions of grammatical constructions explain an enduring syntactic puzzle. *Cognition*, 240, 105563.

Schütze, C. T., & Sprouse, J. (2014). Judgment data. In R. J. Podesva & D. Sharma (Eds.), *Research methods in linguistics* (pp. 27–50). Cambridge University Press.

Sprouse, J., & Almeida, D. (2017). Design sensitivity and statistical power in acceptability judgment experiments. *Glossa*, 2(1), 14.
