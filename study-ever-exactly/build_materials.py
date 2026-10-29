#!/usr/bin/env python3
"""Build the item table and per-participant decks for the -ever replication (v2).

Single source of truth for item wording: FRAMES, FILLERS, ATTENTION and
PRACTICE below. Running this writes items/all_items.csv and one deck per
participant in items/decks/ (P001.csv ...), then validates them.

v2 (2026-10-28, after the Astra and Wonder Full reviews): 24 frames (the 16
of v1 plus five alternates for the structurally unusual frames plus three
new ones); 24 distinct fillers, some containing wh-words or exactly outside
the target construction; a separate constrained random order per
participant; an interpretation block with two questions (statement or
question; does the speaker know which <noun>), rotated so every
frame x condition cell is probed equally often across participants; a
non-relative intermediate practice item; explicit attention-check wording.
"""
import collections
import csv
import random
from pathlib import Path

SEED = 20261028
N_PARTICIPANTS = 160          # decks to generate (40 per list); target sample is 100-150
OUT = Path(__file__).resolve().parent / "items"

# {wh} whatever/what ({Wh} sentence-initial); {mod} " exactly" or "".
# Each frame: (template, noun for the interpretation question, source)
FRAMES = {
    "F01": ("The new release will still support {wh}{mod} this feature is, but behind a setting.", "feature", "adapted from HN 34295663"),
    "F02": ("He went straight to the minister with {wh}{mod} it is that the analyst told him.", "information", "adapted from iWeb (bipartisanreport.com)"),
    "F03": ("The introduction then eases into {wh}{mod} the writer is trying to say.", "point", "adapted from iWeb (privatewriting.com)"),
    "F04": ("Meaning can't be reduced to {wh}{mod} is allowed in a physical description.", "property", "adapted from iWeb (usyd.edu.au)"),
    "F05": ("{Wh}{mod} it was they were doing suddenly stopped.", "activity", "adapted from iWeb (pompeiana.org)"),
    "F06": ("The landlord blamed the leak on {wh}{mod} the plumber had installed.", "part", "new"),
    "F07": ("She gave the museum {wh}{mod} her grandmother had left her.", "items", "new"),
    "F08": ("The committee rejected {wh}{mod} the consultant had proposed.", "proposal", "new"),
    "F09": ("The tenant was charged for {wh}{mod} the inspector had found broken.", "items", "new"),
    "F10": ("The editor cut {wh}{mod} the reviewer had objected to.", "passage", "new"),
    "F11": ("They auctioned off {wh}{mod} the estate had left behind.", "items", "new"),
    "F12": ("The crew cleared away {wh}{mod} the storm had brought down.", "debris", "new"),
    "F13": ("Customs confiscated {wh}{mod} the traveller had failed to declare.", "goods", "new"),
    "F14": ("The chef threw out {wh}{mod} the supplier had delivered.", "food", "new"),
    "F15": ("The new manager undid {wh}{mod} her predecessor had set up.", "arrangements", "new"),
    "F16": ("The court froze {wh}{mod} the company owned.", "assets", "new"),
    # variants of F02, F05, F07, F09, F10 (kept alongside the originals)
    "F17": ("He went straight to the minister with {wh}{mod} the analyst had told him.", "information", "new (variant of F02)"),
    "F18": ("The janitor repaired {wh}{mod} the students had damaged.", "things", "new (object frame added alongside subject frame F05)"),
    "F19": ("The movers packed {wh}{mod} the family had stored in the garage.", "things", "new (alternative to F07)"),
    "F20": ("The tenant paid for {wh}{mod} the inspector had flagged.", "damage", "new (variant of F09)"),
    "F21": ("The editor deleted {wh}{mod} the reviewer had marked.", "passage", "new (variant of F10)"),
    # three new frames
    "F22": ("The insurer refused to cover {wh}{mod} the flood had destroyed.", "property", "new"),
    "F23": ("The volunteers sorted {wh}{mod} the donors had dropped off.", "donations", "new"),
    "F24": ("The archivist catalogued {wh}{mod} the professor had kept in his office.", "papers", "new"),
    "F25": ("The mechanic replaced {wh}{mod} the previous owner had fitted.", "parts", "new"),
    "F26": ("The school banned {wh}{mod} the children had been bringing to class.", "things", "new"),
    "F27": ("The collector returned {wh}{mod} the artist had sent him.", "works", "new"),
}
# Near-twin frames: each rater sees exactly one member of each pair (version group).
TWINS = [("F02", "F17"), ("F09", "F20"), ("F10", "F21")]

# Conditions: A whatever, B whatever+exactly, C what, D what+exactly
CONDITIONS = {"A": ("whatever", ""), "B": ("whatever", " exactly"),
              "C": ("what", ""), "D": ("what", " exactly")}

# Distinct contents; none is a variant of another. Second field = noun for the
# interpretation question (natural fillers only; None = not probed).
FILLERS_GOOD = [
    ("The bakery on the corner closes early on Sundays in the winter.", "bakery"),
    ("She folded the letter twice and slipped it into her coat pocket.", "letter"),
    ("The council postponed its decision until the spring meeting.", "meeting"),
    ("He keeps his old camera in a box under the kitchen sink.", "camera"),
    ("The recipe calls for exactly two eggs and a cup of flour.", None),
    ("Nobody on the platform knew what time the last train left.", None),
    ("Whatever the forecast says, we're having the picnic on Saturday.", None),
    ("The orchestra performed its best-known symphony at a festival in Montreal.", "symphony"),
    ("Our neighbours repainted their front door a surprisingly bright green.", "door"),
    ("The coach asked the players what they had eaten before the match.", None),
    ("The library extended its hours during the week before exams.", "library"),
    ("After the heavy rain, the river rose higher than anyone had expected.", "river"),
]
FILLERS_BAD = [
    "The farmer have sold most of his sheep at the autumn market.",
    "Most of the guests had already leaving by the time the band arrived.",
    "The nurses finished the shift an hour early the.",
    "She put on the table the flowers that her friend had brought her yesterday the.",
    "The tailor shortened two exactly centimetres the trousers.",
    "The tourists asked the guide where the station is it.",
    "He gave to his brother for his birthday it.",
    "The bus driver were stopped for speeding on the highway last night.",
    "The puppies is sleeping in the basket by the stove.",
    "Whatever says the doctor, I'm going to finish the race.",
    "The lecture went on longer more than the audience had planned for.",
    "The gardener a fence painted brown new around the vegetables.",
]
ATTENTION = [
    "To show you're reading carefully, please choose 2 for this sentence.",
    "To show you're reading carefully, please choose 6 for this sentence.",
]
PRACTICE = [
    ("P1", "natural", "The children planted tomatoes along the back wall of the garden."),
    ("P2", "unnatural", "The children planted along the back wall tomatoes of garden the."),
    ("P3", "intermediate", "The children planted along the back wall the tomatoes."),
]
RATE_Q = "How natural is this sentence? 1 = very unnatural, 7 = very natural"
RATE_OPTS = "1|2|3|4|5|6|7"
PARSE_Q = "Is this sentence a statement or a question?"
PARSE_OPTS = "A statement|A question|Can't tell"
KNOW_Q = "Does the speaker seem to know which {noun} {be}?"
KNOW_OPTS = "Yes, they know which|No, they don't know which|Can't tell"
# Plural probe nouns take "they were" (*which items it was).
PLURAL_NOUNS = {"items", "goods", "arrangements", "assets", "things", "donations", "papers", "parts", "works"}


def know_q(noun):
    assert noun.endswith("s") == (noun in PLURAL_NOUNS) or noun in {"debris"}, noun
    return KNOW_Q.format(noun=noun, be="they were" if noun in PLURAL_NOUNS else "it was")


def realise(template, cond):
    wh, mod = CONDITIONS[cond]
    return template.replace("{wh}", wh).replace("{Wh}", wh.capitalize()).replace("{mod}", mod)


def item_table():
    rows = []
    for fid, (tpl, noun, src) in FRAMES.items():
        for cond, (wh, mod) in CONDITIONS.items():
            rows.append(dict(item_id=f"{fid}{cond}", item_type="experimental", frame=fid, wh=wh,
                             modifier="exactly" if mod else "none", condition=cond,
                             text=realise(tpl, cond), probe_noun=noun, source=src))
    for i, (t, noun) in enumerate(FILLERS_GOOD, 1):
        rows.append(dict(item_id=f"FG{i:02d}", item_type="filler_good", frame="", wh="", modifier="",
                         condition="", text=t, probe_noun=noun or "", source="new"))
    for i, t in enumerate(FILLERS_BAD, 1):
        rows.append(dict(item_id=f"FB{i:02d}", item_type="filler_bad", frame="", wh="", modifier="",
                         condition="", text=t, probe_noun="", source="new"))
    for i, t in enumerate(ATTENTION, 1):
        rows.append(dict(item_id=f"AC{i}", item_type="attention", frame="", wh="", modifier="",
                         condition="", text=t, probe_noun="", source="new"))
    for pid, kind, t in PRACTICE:
        rows.append(dict(item_id=pid, item_type=f"practice_{kind}", frame="", wh="", modifier="",
                         condition="", text=t, probe_noun="", source="new"))
    return rows


def main_order(trials, rng):
    """At most two experimental trials in a row; never two adjacent experimental
    trials in the same condition; one attention check in each half, not in the
    first three positions."""
    half = len(trials) // 2
    for _ in range(200000):
        seq = trials[:]
        rng.shuffle(seq)
        run, ok = 0, True
        for k, r in enumerate(seq):
            run = run + 1 if r["item_type"] == "experimental" else 0
            if run > 2 or (k and r["item_type"] == "experimental" and seq[k - 1]["item_type"] == "experimental"
                           and r["condition"] == seq[k - 1]["condition"]):
                ok = False
                break
        att = [k for k, r in enumerate(seq) if r["item_type"] == "attention"]
        if ok and att[0] >= 3 and att[0] < half <= att[1]:
            return seq
    raise RuntimeError("no valid order")


def build():
    rng = random.Random(SEED)
    rows = item_table()
    OUT.mkdir(exist_ok=True)
    decks = OUT / "decks"
    decks.mkdir(exist_ok=True)
    for old in decks.glob("*.csv"):
        old.unlink()
    with open(OUT / "all_items.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    by_id = {r["item_id"]: r for r in rows}
    twin_members = {f for pair in TWINS for f in pair}
    singles = [f for f in FRAMES if f not in twin_members]
    fillers = [by_id[f"FG{i:02d}"] for i in range(1, 13)] + [by_id[f"FB{i:02d}"] for i in range(1, 13)]
    attn = [by_id["AC1"], by_id["AC2"]]
    probe_fillers = [r for r in fillers if r["item_type"] == "filler_good" and r["probe_noun"]]
    for p in range(N_PARTICIPANTS):
        lst = p % 4
        version = (p // 4) % 2                     # which member of each twin pair
        fids = singles + [pair[version] for pair in TWINS]
        assert len(fids) == 24
        exp = [by_id[f"{fid}{'ABCD'[(k + lst) % 4]}"] for k, fid in enumerate(fids)]
        main = main_order(exp + fillers + attn, rng)
        # interpretation: 8 experimental trials (2 per condition), rotated by participant
        # so frame x condition cells are probed about equally; plus the probe-able fillers
        rot = (p // 4) % 3
        chosen = []
        for c in "ABCD":
            pool = sorted([r for r in exp if r["condition"] == c], key=lambda r: r["frame"])
            chosen += [pool[(rot * 2) % len(pool)], pool[(rot * 2 + 1) % len(pool)]]
        interp = chosen + rng.sample(probe_fillers, min(8, len(probe_fillers)))
        rng.shuffle(interp)
        out = []
        practice = [by_id["P1"], by_id["P3"], by_id["P2"]]
        for block, seq in (("practice", practice), ("main", main), ("interpretation", interp)):
            for pos, r in enumerate(seq, 1):
                base = dict(participant=f"P{p + 1:03d}", list=lst + 1, block=block, position=pos,
                            item_id=r["item_id"], item_type=r["item_type"], frame=r["frame"], wh=r["wh"],
                            modifier=r["modifier"], condition=r["condition"], text=r["text"])
                if block == "interpretation":
                    opts1 = PARSE_OPTS.split("|")
                    opts2 = KNOW_OPTS.split("|")
                    if rng.random() < 0.5:   # randomize order of the two substantive options
                        opts1[0], opts1[1] = opts1[1], opts1[0]
                        opts2[0], opts2[1] = opts2[1], opts2[0]
                    out.append(dict(base, trial_id=f"P{p + 1:03d}-int-{pos:02d}a", question=PARSE_Q,
                                    options="|".join(opts1)))
                    out.append(dict(base, trial_id=f"P{p + 1:03d}-int-{pos:02d}b",
                                    question=know_q(r["probe_noun"]), options="|".join(opts2)))
                else:
                    out.append(dict(base, trial_id=f"P{p + 1:03d}-{block[:3]}-{pos:02d}",
                                    question=RATE_Q, options=RATE_OPTS))
        with open(decks / f"P{p + 1:03d}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
            w.writeheader()
            w.writerows(out)
    validate()


def validate():
    cells = collections.Counter()
    probed = collections.Counter()
    for f in sorted((OUT / "decks").glob("P*.csv")):
        rows = list(csv.DictReader(open(f)))
        main = [r for r in rows if r["block"] == "main"]
        exp = [r for r in main if r["item_type"] == "experimental"]
        assert len([r for r in rows if r["block"] == "practice"]) == 3
        assert len(main) == 50, len(main)
        frames_here = {r["frame"] for r in exp}
        assert len(exp) == 24 and len(frames_here) == 24
        for a, b in TWINS:
            assert len(frames_here & {a, b}) == 1, f"{f.name} sees both or neither of {a}/{b}"
        assert collections.Counter(r["condition"] for r in exp) == {c: 6 for c in "ABCD"}
        assert sum(r["item_type"] == "filler_good" for r in main) == 12
        assert sum(r["item_type"] == "filler_bad" for r in main) == 12
        assert sum(r["item_type"] == "attention" for r in main) == 2
        run = 0
        for k, r in enumerate(main):
            run = run + 1 if r["item_type"] == "experimental" else 0
            assert run <= 2
            if k and r["item_type"] == "experimental" and main[k - 1]["item_type"] == "experimental":
                assert r["condition"] != main[k - 1]["condition"]
        att = [k for k, r in enumerate(main) if r["item_type"] == "attention"]
        assert att[0] >= 3 and att[0] < 25 <= att[1]
        interp = [r for r in rows if r["block"] == "interpretation"]
        assert len(interp) == 32                       # 16 sentences x 2 questions
        ie = [r for r in interp if r["item_type"] == "experimental" and r["trial_id"].endswith("a")]
        assert collections.Counter(r["condition"] for r in ie) == {c: 2 for c in "ABCD"}
        assert {r["item_id"] for r in interp} <= {r["item_id"] for r in main}
        for r in interp:
            assert "whatever" not in (r["question"] + r["options"]).lower()
            assert "exactly" not in (r["question"] + r["options"]).lower()
        assert len({r["trial_id"] for r in rows}) == len(rows)
        for r in exp:
            cells[(r["frame"], r["condition"])] += 1
        for r in ie:
            probed[(r["frame"], r["condition"])] += 1
    n = len(list((OUT / "decks").glob("P*.csv")))
    twin_members = {f for pair in TWINS for f in pair}
    for fid in FRAMES:
        want = n // 8 if fid in twin_members else n // 4
        assert all(cells[(fid, c)] == want for c in "ABCD"), f"unbalanced {fid}"
    print(f"validated {n} decks: 3 practice + 50 main (24 experimental, 24 fillers, 2 checks) "
          f"+ 16 interpretation sentences x 2 questions; each frame x condition rated in {n // 4} decks ({n // 8} for twin frames); "
          f"probed frame x condition cells: {len(probed)} of {4 * len(FRAMES)}, per cell min {min(probed.values())} max {max(probed.values())}")


if __name__ == "__main__":
    build()
