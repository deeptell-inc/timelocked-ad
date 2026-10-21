"""Finite-key thresholds with the general Bell-diagonal Eve term (phi_X != phi_Z), Appendix B.
Models: individual / joint x shannon / minent, bell='general'. Output data/bd_thresholds.csv"""
import os, sys, csv, time
sys.path.insert(0, os.path.dirname(__file__))
from skl import skl_qct_ad, threshold_qber
quick = len(sys.argv) > 1 and sys.argv[1] == "quick"
cases = [(1e14, [9])] if quick else [(1e8, [2, 3]), (1e14, [5, 7, 9, 11, 15])]
rows = []; t0 = time.time()
for N, bs in cases:
    for b in bs:
        for att in ("individual", "joint"):
            for ent in ("shannon", "minent"):
                fun = lambda N_, P_, ch_, b_, a=att, e=ent: skl_qct_ad(N_, P_, ch_, b_, entropy=e, attack=a, bell="general")
                q, deg, P = threshold_qber(fun, N, b)
                rows.append(dict(model=f"QCT_{att}_{ent}_bd", N=N, b=b, qber_thr=q, delta_deg=deg)); print(rows[-1], "%.0fs" % (time.time()-t0), flush=True)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "bd_thresholds%s.csv" % ("_quick" if quick else ""))
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
