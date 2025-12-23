# CLAUDE.md

## Project Overview

**Title:** Focus Modifiers with Interrogative Heads (working title)
**Type:** Squib
**Author:** Brett Reynolds
**Status:** Draft notes

## Core Argument

Payne, Huddleston & Pullum (2010) analyze "precisely nothing" as adverbial modification of a determinative in NP structure. This squib addresses a related but distinct construction: focus modifiers with interrogative heads ("precisely who," "exactly what," "just which").

**Proposal:** Treat *exactly/precisely/just* as focus modifiers licensed specifically by interrogative heads, not as ordinary NP-internal adverbial modifiers. This preserves CGEL's block on pre-head adverbial modifiers of nouns while accounting for the interrogative exception.

## Key Points

1. CGEL recognizes interrogatives allow special modifiers (post-head *else*, pre/post-head *exactly/precisely*, stacking *just exactly/precisely*)
2. The semantic questioned element may be smaller than the syntactic phrase (*whose* in *whose father*)
3. Focus modifiers target the interrogative head itself, not an ordinary noun head
4. *Who* is a pronoun; *which/what* are determinatives - this categorical distinction matters for modification
5. The restriction is semantically natural: interrogatives denote alternatives/variable-values; *precisely/exactly* signals insistence on precise identification

## Proposed Structures (CGEL-style, no DP)

**Pronoun head:**
```
[NP [Mod AdvP precisely] [Head Nom [Head N who]]]
```

**Determinative + noun:**
```
[NP [Det [Mod AdvP exactly] [Head D which]] [Head N person]]
```

**Fused-head:**
```
[NP [Det [Mod AdvP exactly] [Head D which]]]
```

## Key References

- Huddleston & Pullum 2002 (CGEL): pp. 912, 915-918, 592
- Payne, Huddleston & Pullum 2010 (adjectives/adverbs paper)
- Groenendijk & Stokhof 1984 (exhaustivity)
- Theiler, Roelofsen & Aloni 2018 (exactly who; strong exhaustivity)
- Quirk et al. 1985; Konig 1991 (focus particles)

## Build Commands

```bash
# When LaTeX files exist
lualatex main.tex && biber main && lualatex main.tex && lualatex main.tex
```
