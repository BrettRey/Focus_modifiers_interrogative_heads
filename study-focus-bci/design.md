# Experimental Design: BCI and Focus Modification

## Overview

This study tests whether information structure predicts the acceptability of precision modifiers (*exactly*, *precisely*) in the same way it predicts extraction island effects.

## Theoretical Background

Goldberg's (2006) Backgrounded Constituent Infelicity (BCI) principle: foregrounding and backgrounding the same constituent is infelicitous. Long-distance dependencies foreground the fronted phrase; island constructions background it—hence the clash.

**Extension hypothesis:** Precision modifiers foreground the NP they attach to. If the NP is backgrounded, the result is infelicitous, parallel to extraction islands.

## Predictions

### Prediction 1: Relative Clauses Block Modifiers (Negative)

Relative clauses background their head. Therefore, precision modifiers should be blocked:

| Condition | Example | Prediction |
|-----------|---------|------------|
| Interrogative | *Exactly who called?* | ✓ |
| Relative | *The person exactly who called left.* | ✗ |

### Prediction 2: Focus Congruence Predicts Gradience (Positive)

Within the same syntactic frame, discourse-focus status should modulate acceptability:

| Context | Discourse Status | Example | Prediction |
|---------|------------------|---------|------------|
| Focus-congruent | NP is new/contrastive | *A: Which cats?* → *Exactly the cats you mentioned.* | ✓ |
| Focus-incongruent | NP is given/topical | *A: What did they do?* → *Exactly the cats you mentioned were playing.* | ↓ |

## Design

### Factors

1. **Syntactic frame**: Subject position vs. It-cleft
2. **Discourse context**: Focus-congruent vs. Focus-incongruent (manipulated via preceding question)
3. **Modifier presence**: With *exactly* vs. Without

### Dependent Measures

- **Acceptability rating** (7-point Likert or slider)
- Potentially: **Negation task** and **Discourse task** (Cuneo & Goldberg's measures)

## Stimuli Design

### Template Structure

Each item consists of:
1. **Context question** (manipulates focus)
2. **Target sentence** (contains the critical NP ± modifier)

### Example Item Set

**Item 1: Subject position**

| Version | Context | Target |
|---------|---------|--------|
| Focus-congruent, +modifier | *Which cats were playing?* | *Exactly the cats you mentioned were playing.* |
| Focus-congruent, −modifier | *Which cats were playing?* | *The cats you mentioned were playing.* |
| Focus-incongruent, +modifier | *What were the cats doing?* | *Exactly the cats you mentioned were playing.* |
| Focus-incongruent, −modifier | *What were the cats doing?* | *The cats you mentioned were playing.* |

**Item 2: It-cleft**

| Version | Context | Target |
|---------|---------|--------|
| Focus-congruent, +modifier | *Which cats were playing?* | *It was exactly the cats you mentioned that were playing.* |
| Focus-congruent, −modifier | *Which cats were playing?* | *It was the cats you mentioned that were playing.* |
| Focus-incongruent, +modifier | *What about those cats?* | *It was exactly the cats you mentioned that were playing.* |
| Focus-incongruent, −modifier | *What about those cats?* | *It was the cats you mentioned that were playing.* |

## Sample Size and Power

To be determined based on effect size estimates from Cuneo & Goldberg (2023).

## Analysis Plan

- Mixed-effects regression with random slopes for items and participants
- Fixed effects: Frame × Context × Modifier
- Key interaction: Context × Modifier (does focus congruence modulate the modifier effect?)

## Timeline

| Phase | Date | Milestone |
|-------|------|-----------|
| Stimuli development | Jan 2026 | Draft 24 item sets |
| Pilot testing | Late Jan | Small pilot (n~20) |
| Full data collection | Feb 2026 | Target n=100+ |
| Analysis & write-up | Feb–Mar | Submit for publication |
