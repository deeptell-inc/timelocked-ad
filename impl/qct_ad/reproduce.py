"""Reproduce T25 headline thresholds and compute the QCT V-A thresholds.
Usage: python reproduce.py [quick]
Outputs data/threshold_table.csv (deterministic)."""
import sys, csv, math, os, time
sys.path.insert(0, os.path.dirname(__file__))
from skl import skl_ad, skl_bb84, skl_qct_ad, threshold_qber, gw_delta0, majority_error

quick = len(sys.argv) > 1 and sys.argv[1] == "quick"
cases = ([(1e8, [1, 2, 3, 4, 5]), (1e10, [3, 5, 7]), (1e12, [3, 5, 7, 9]),
          (1e14, [1, 3, 5, 7, 9, 11, 15, 21])] if not quick else [(1e8, [3]), (1e14, [9])])

rows = []
t0 = time.time()
for N, bs in cases:
    q, deg, P = threshold_qber(skl_bb84, N)
    rows.append(dict(model="BB84_T25_eq94", N=N, b=1, qber_thr=q, delta_deg=deg)); print(rows[-1], flush=True)
    for b in bs:
        q, deg, P = threshold_qber(skl_ad, N, b)
        rows.append(dict(model="AD_T25_eq93", N=N, b=b, qber_thr=q, delta_deg=deg)); print(rows[-1], flush=True)
        for ent in ("shannon", "minent"):
            fun = lambda N_, P_, ch_, b_, e=ent: skl_qct_ad(N_, P_, ch_, b_, entropy=e)
            q, deg, P = threshold_qber(fun, N, b)
            rows.append(dict(model=f"QCT_VA_{ent}", N=N, b=b, qber_thr=q, delta_deg=deg)); print(rows[-1], flush=True)

os.makedirs(os.path.join(os.path.dirname(__file__), "..", "..", "data"), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "threshold_table%s.csv" % ("_quick" if quick else ""))
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out, "in %.0f s" % (time.time() - t0))

# asymptotic sanity: Gisin-Wolf threshold for the V-A model (P4)
print("GW check: delta0(0.25)=%.4f  D/(1-D)=%.4f  2sqrt(d0(1-d0))=%.4f" % (
    gw_delta0(0.25), 0.25 / 0.75, 2 * math.sqrt(gw_delta0(0.25) * (1 - gw_delta0(0.25)))))
