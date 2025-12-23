# Implementation Plan: Glossa Squib (Final)

## Clarifications

1. **CGEL and Payne et al. are consistent**: Both analyze *precisely* in *precisely nothing* as a **pre-head peripheral modifier**: `[NP [AdvP:Mod precisely] [NP:Head nothing]]`. Same structure for *precisely who*. No contradiction.

2. **The core question**: Why can precision modifiers peripherally modify interrogative NPs and fused-determinative NPs (*nothing*) but not ordinary noun-headed NPs (*\*precisely cats*)?

3. **BCI is relevant**: The foregrounding/backgrounding mechanism explains the integrated-relative restriction.

---

## Revised Structure (4 sections)

### §1 The puzzle (~600 words)

Lead with the distribution:

| Construction | Example | Status |
|--------------|---------|--------|
| Wh-question (pre-head) | *Exactly who called?* | ✓ |
| Wh-question (post-head) | *Who exactly called?* | ✓ |
| Fused relative | *I did exactly what you asked.* | ✓ |
| Integrated relative | *\*The person exactly who called* | ✗ |

Include:
- CGEL's scattered observations (pp. 592, 912, 916)
- The *else* parallel (same distribution: *who else* but not *\*the person who else*)
- The *just exactly* stack
- Contrast with Payne et al. 2010: they analyze *precisely nothing* as internal post-head; this construction is peripheral pre-head

The scintillating core: **fused relatives pattern with questions, not with integrated relatives—why?**

---

### §2 The syntactic description (~600 words)

**Position**: Peripheral modifiers of interrogative NPs (CGEL pp. 436–438).

CGEL recognizes "precision modifiers" (*exactly, precisely*) as peripheral modifiers occurring with:
- Superlatives (*exactly the right answer*)
- Demonstratives (*exactly that*)
- **Interrogatives and relatives** (*exactly what you asked*)

The distribution:
- Works when the wh-word **heads an NP** (questions, fused relatives)
- Fails when the wh-word is **embedded in a relative clause** (integrated relatives)

Clarify the Payne et al. relationship:
- *Precisely nothing*: internal post-head modifier of the determinative (Payne et al.)
- *Exactly who*: peripheral pre-head modifier of the interrogative NP (this squib)
- **Complementary analyses, not contradictions**

---

### §3 The semantic-pragmatic explanation (~800 words)

Core claim: The distribution reflects a **foregrounding/backgrounding clash** (Cuneo & Goldberg 2023).

**Two-layer account**:

1. **Semantic layer (Theiler et al. 2018)**: Interrogatives and fused relatives denote **alternative sets** (Hamblin 1973). *Exactly/precisely* signals **exhaustive identification**—the answer must pick out the complete set of individuals satisfying the question. This requires alternatives to precisify.

2. **Pragmatic layer (BCI)**: LDD constructions foreground; island constructions background. The same principle applies here:
   - *Exactly* **foregrounds** the wh-element (makes it at-issue, demands precise identification)
   - Integrated relatives **background** their content (presupposed, not at-issue)
   - Combining them = clash

**The parallel with islands**:

| Phenomenon | Foregrounding | Backgrounding | Result |
|------------|---------------|---------------|--------|
| Island effects | LDD fronts wh-phrase | Island construction | Infelicity |
| *\*exactly who* in relatives | *exactly* foregrounds | Integrated relative | Infelicity |

This is the theoretical payoff: **the BCI mechanism generalizes beyond extraction**.

---

### §4 Conclusion (~300 words)

1. The observation: *exactly who* patterns with fused relatives, not integrated relatives
2. Syntactic description: peripheral modifiers of interrogative NPs
3. Explanation: foregrounding/backgrounding clash (same mechanism as islands)
4. Open questions:
   - Cross-linguistic parallels (German *genau wer*, *ausgerechnet*)
   - The *just exactly* ordering constraint
   - The *else* connection (same distribution)

---

## References to Add

```bibtex
@article{cuneo2023,
  author  = {Cuneo, Nicole and Goldberg, Adele E.},
  title   = {The Discourse Functions of Grammatical Constructions Explain an Enduring Syntactic Puzzle},
  journal = {Cognition},
  volume  = {240},
  pages   = {105563},
  year    = {2023}
}

@article{hamblin1973,
  author  = {Hamblin, C. L.},
  title   = {Questions in {Montague} {English}},
  journal = {Foundations of Language},
  volume  = {10},
  pages   = {41--53},
  year    = {1973}
}
```

---

## Word Count Estimate

| Section | Words |
|---------|-------|
| Abstract | 100 |
| §1 The puzzle | 600 |
| §2 Syntactic description | 600 |
| §3 Semantic-pragmatic explanation | 800 |
| §4 Conclusion | 300 |
| **Total** | **~2,400** |

Leaves room for examples and footnotes. Well under 5,000.

---

## Verification Plan

1. **LaTeX compilation**: `lualatex main.tex && biber main && lualatex main.tex`
2. **Word count**: `detex main.tex | wc -w` → verify < 3,500
3. **User review**: Does the BCI argument land?
