"""Thresholds under the within-block joint-measurement bound (attack='joint').
Outputs data/joint_thresholds.csv (asymptotic + finite-key)."""
import os, sys, csv, math
sys.path.insert(0, os.path.dirname(__file__))
from skl import eve_info_distilled_joint, h2, skl_qct_ad, threshold_qber
from asymptotic import rate_eur, thr


def rate_joint(D, b, f, acc="shannon"):
    pa = (1 - D) ** b + D ** b
    IE, pg, _ = eve_info_distilled_joint(D, b)
    PhiK = D ** b / pa
    H = (1 - IE) if acc == "shannon" else -math.log2(pg)
    return pa / b * (H - f * h2(PhiK))


rows = []
for f in (1.2, 1.0):
    for b in (1, 2, 3, 5, 7, 9, 11, 15, 21, 31):
        rows.append(dict(kind="asymptotic", f=f, b=b, N="inf",
                         thr_EUR=thr(rate_eur, b, f),
                         thr_joint_shannon=thr(lambda D, b, f: rate_joint(D, b, f, "shannon"), b, f),
                         thr_joint_minent=thr(lambda D, b, f: rate_joint(D, b, f, "minent"), b, f)))
        print(rows[-1], flush=True)
quick = len(sys.argv) > 1 and sys.argv[1] == "quick"
cases = [(1e14, [9])] if quick else [(1e8, [2, 3, 4]), (1e14, [5, 7, 9, 11, 15])]
for N, bs in cases:
    for b in bs:
        r = dict(kind="finite", f=1.2, b=b, N=N, thr_EUR=float("nan"))
        for ent in ("shannon", "minent"):
            fun = lambda N_, P_, ch_, b_, e=ent: skl_qct_ad(N_, P_, ch_, b_, entropy=e, attack="joint")
            q, deg, P = threshold_qber(fun, N, b)
            r["thr_joint_" + ent] = q
        rows.append(r); print(r, flush=True)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "joint_thresholds%s.csv" % ("_quick" if quick else ""))
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
