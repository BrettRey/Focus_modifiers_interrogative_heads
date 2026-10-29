#!/usr/bin/env python3
"""Design analysis (Gelman & Carlin 2014) for the whatever/what x exactly study.

Reuses the data-generating model in power_simulation.py (cumulative logit,
crossed participant and item random effects, borrowed variance components),
with 16 frames. For each assumed true interaction and sample size it reports
the mean 95% interval half-width of the by-participant difference-of-
differences estimate (rating points), the probability of significance under
the by-participant and by-item tests together, and Type S and Type M among
significant results. Half-widths ignore item variability, so the planned
mixed model's intervals will be somewhat wider.
"""
import importlib.util
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ps", HERE / "power_simulation.py")
ps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ps)

SEED = 20261028
N_ITEMS = 16
N_REPS = 2000
LATENT = (0.3, 0.5, 0.8)
NS = (60, 100, 150)


def rep(n, delta, rng):
    lists = np.arange(n) % 4
    cond = (np.arange(N_ITEMS)[None, :] + lists[:, None]) % 4
    pe = {k: rng.normal(0, v, n) for k, v in ps.P_SD.items()}
    ie = {k: rng.normal(0, v, N_ITEMS) for k, v in ps.I_SD.items()}
    wh, md = ps.WH[cond], ps.MOD[cond]
    lat = (ps.BASE_WHATEVER + pe["intercept"][:, None] + ie["intercept"][None, :]
           + wh * (ps.WHAT_MAIN + pe["wh"][:, None] + ie["wh"][None, :])
           + md * (ps.EXACTLY_MAIN + pe["mod"][:, None] + ie["mod"][None, :])
           - wh * md * (delta + pe["inter"][:, None] + ie["inter"][None, :]))
    y = ps.ordinal(lat, rng).astype(float)
    cm = np.stack([(y * (cond == c)).sum(1) / (cond == c).sum(1) for c in range(4)], 1)
    im = np.stack([(y * (cond == c)).sum(0) / np.maximum((cond == c).sum(0), 1) for c in range(4)], 1)
    dp = (cm[:, 1] - cm[:, 0]) - (cm[:, 3] - cm[:, 2])   # positive = predicted
    di = (im[:, 1] - im[:, 0]) - (im[:, 3] - im[:, 2])
    p1 = 2 * stats.t.sf(abs(dp.mean() / (dp.std(ddof=1) / np.sqrt(n))), n - 1)
    p2 = 2 * stats.t.sf(abs(di.mean() / (di.std(ddof=1) / np.sqrt(N_ITEMS))), N_ITEMS - 1)
    hw = stats.t.ppf(.975, n - 1) * dp.std(ddof=1) / np.sqrt(n)
    return dp.mean(), hw, (p1 < .05) and (p2 < .05)


def main():
    rng = np.random.default_rng(SEED)
    print("latent  n   true_DoD  ci95_halfwidth  P(sig)  TypeS  TypeM")
    for delta in LATENT:
        for n in NS:
            r = np.array([rep(n, delta, rng) for _ in range(N_REPS)])
            est, hw, sig = r[:, 0], r[:, 1], r[:, 2].astype(bool)
            true = est.mean()
            ts = np.mean(est[sig] < 0) if sig.any() else float("nan")
            tm = np.mean(np.abs(est[sig])) / true if sig.any() else float("nan")
            print(f"{delta:5.1f} {n:4d}   {true:5.2f}      {hw.mean():5.2f}        "
                  f"{sig.mean():5.2f}  {ts:5.3f}  {tm:5.2f}")


if __name__ == "__main__":
    main()
