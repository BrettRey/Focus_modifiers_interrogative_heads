#!/usr/bin/env python3
"""Design-stage power check for the whatever/what x exactly replication.

Approximation, not the planned analysis: data are generated from a
cumulative-logit model with crossed participant and item random effects,
but tested with aggregated difference-of-differences t-tests by participant
(F1-style) and by item (F2-style), each two-sided at .05. "Both" requires
both, which is conservative relative to the ordinal mixed model the
protocol specifies. Variance components and thresholds are borrowed from
papers/waiting/independent-relative-whose/scripts/power_simulation.py
(participant intercept 0.70, construction slope 0.35, interaction-type
slopes 0.22; item intercept 0.45, item slopes 0.18; thresholds
-2.00 ... 2.10), so they're priors from a sibling design, not estimates.

Design: 8 lexical sets x 4 conditions, 4 Latin-square lists, each
participant rates each set once and each condition twice.
"""
import numpy as np

SEED = 20261028
N_REPS = 2000
N_GRID = (30, 40, 60, 80, 120)
# Interaction on the latent logit scale: extra cost of exactly with plain
# what. Brett's "clearly worse" suggests the upper end.
DELTA_GRID = (0.5, 0.8, 1.2, 1.6)
THRESHOLDS = np.array((-2.00, -1.00, -0.25, 0.50, 1.25, 2.10))
BASE_WHATEVER = 1.2     # whatever, no exactly: good (mean rating about 5.5)
WHAT_MAIN = -0.2        # plain what alone slightly lower
EXACTLY_MAIN = -0.2     # small cost of exactly with whatever
P_SD = dict(intercept=0.70, wh=0.35, mod=0.35, inter=0.22)
I_SD = dict(intercept=0.45, wh=0.18, mod=0.18, inter=0.18)
N_ITEMS = 8  # overridden by main() for the 16-item variant
# Latin square: list l gives item i condition (i + l) % 4.
# Conditions: 0 whatever, 1 whatever+exactly, 2 what, 3 what+exactly.
WH = np.array((0, 0, 1, 1))
MOD = np.array((0, 1, 0, 1))


def ordinal(latent, rng):
    # P(Y <= k) = logistic(theta_k - latent); sample by inverse CDF
    u = rng.random(latent.shape)
    cum = 1 / (1 + np.exp(-(THRESHOLDS[None, :] - latent[..., None])))
    return 1 + (u[..., None] > cum).sum(-1)


def t_p(x):
    n = len(x)
    m, s = x.mean(), x.std(ddof=1)
    if s == 0:
        return 0.0
    from math import erf, sqrt
    t = m / (s / np.sqrt(n))
    # two-sided p via Student t (scipy-free approximation via betainc)
    from scipy import stats
    return 2 * stats.t.sf(abs(t), n - 1)


def one_rep(n, delta, rng):
    lists = np.arange(n) % 4
    cond = (np.arange(N_ITEMS)[None, :] + lists[:, None]) % 4      # n x 8
    pe = {k: rng.normal(0, v, n) for k, v in P_SD.items()}
    ie = {k: rng.normal(0, v, N_ITEMS) for k, v in I_SD.items()}
    wh, md = WH[cond], MOD[cond]
    inter = wh * md
    lat = (BASE_WHATEVER + pe["intercept"][:, None] + ie["intercept"][None, :]
           + wh * (WHAT_MAIN + pe["wh"][:, None] + ie["wh"][None, :])
           + md * (EXACTLY_MAIN + pe["mod"][:, None] + ie["mod"][None, :])
           - inter * (delta + pe["inter"][:, None] + ie["inter"][None, :]))
    y = ordinal(lat, rng).astype(float)
    # by-participant difference of differences on cell means
    cm = np.zeros((n, 4))
    for c in range(4):
        mask = cond == c
        cm[:, c] = (y * mask).sum(1) / mask.sum(1)
    # (whatever+ex - whatever) - (what+ex - what): positive = predicted
    dod_p = (cm[:, 1] - cm[:, 0]) - (cm[:, 3] - cm[:, 2])
    # by-item
    im = np.zeros((N_ITEMS, 4))
    for c in range(4):
        mask = cond == c
        im[:, c] = (y * mask).sum(0) / np.maximum(mask.sum(0), 1)
    dod_i = (im[:, 1] - im[:, 0]) - (im[:, 3] - im[:, 2])
    return t_p(dod_p), t_p(dod_i), dod_p.mean(), cm.mean(0)


def main():
    global N_ITEMS
    rng = np.random.default_rng(SEED)
    for N_ITEMS, deltas, ns in ((8, DELTA_GRID, N_GRID), (16, (0.8, 1.2, 1.6), (40, 60, 80))):
      print(f"\n{N_ITEMS} lexical sets")
      print("delta  n    F1     F2     both   mean_DoD  cell means (whatever, whatever+ex, what, what+ex)")
      for delta in deltas:
        for n in ns:
            r = [one_rep(n, delta, rng) for _ in range(N_REPS)]
            p1 = np.array([x[0] for x in r]); p2 = np.array([x[1] for x in r])
            dod = np.mean([x[2] for x in r]); cells = np.mean([x[3] for x in r], 0)
            print(f"{delta:4.1f} {n:4d}  {np.mean(p1 < .05):.2f}   {np.mean(p2 < .05):.2f}   "
                  f"{np.mean((p1 < .05) & (p2 < .05)):.2f}   {dod:5.2f}    "
                  + " ".join(f"{c:.2f}" for c in cells))


if __name__ == "__main__":
    main()
