"""Secure key rate (ell/N) versus QBER for T25-AD and QCT V-A models.
Channel: eta=1, p_noise=0, QBER from misalignment only (T25 Fig. 5 setting).
Output: data/rate_curves.csv (deterministic)."""
import sys, os, csv, math, time
sys.path.insert(0, os.path.dirname(__file__))
from skl import skl_ad, skl_bb84, skl_qct_ad, optimise, Channel, qber_of

N_list = [1e8, 1e14]
b_list = [1, 3, 5, 9]
degs = [float(d) for d in range(0, 31, 1)]
rows = []
t0 = time.time()
for N in N_list:
    for b in b_list:
        x0 = {"AD": None, "QCT_shannon": None, "QCT_minent": None, "BB84": None}
        for deg in degs:
            ch = Channel(1.0, 0.0, math.radians(deg))
            if b == 1:
                ell, P, x = optimise(skl_bb84, N, ch, None, x0["BB84"]); x0["BB84"] = x
                rows.append(dict(model="BB84_T25_eq94", N=N, b=1, delta_deg=deg, qber=qber_of(P, ch), rate=max(ell, 0) / N))
            ell, P, x = optimise(skl_ad, N, ch, b, x0["AD"]); x0["AD"] = x
            rows.append(dict(model="AD_T25_eq93", N=N, b=b, delta_deg=deg, qber=qber_of(P, ch), rate=max(ell, 0) / N))
            for ent in ("shannon", "minent"):
                fun = lambda N_, P_, ch_, b_, e=ent: skl_qct_ad(N_, P_, ch_, b_, entropy=e)
                ell, P, x = optimise(fun, N, ch, b, x0["QCT_" + ent]); x0["QCT_" + ent] = x
                rows.append(dict(model="QCT_VA_" + ent, N=N, b=b, delta_deg=deg, qber=qber_of(P, ch), rate=max(ell, 0) / N))
            print(N, b, deg, "%.0fs" % (time.time() - t0), flush=True)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "rate_curves.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
