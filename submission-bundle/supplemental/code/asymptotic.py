"""Asymptotic (N -> inf, single-photon source, phi_Z = phi_X = D) thresholds for
T25-AD (EUR) and QCT V-A, per block size b and EC efficiency f.
Output: data/asymptotic_thresholds.csv"""
import os, csv, math, sys
sys.path.insert(0, os.path.dirname(__file__))
from skl import eve_info_distilled, h2


def rate_eur(D, b, f):
    pa = (1 - D) ** b + D ** b
    PhiX = min(max(0.5 * ((1 - D) ** b - (1 - 3 * D) ** b) / pa, 0.0), 0.5)
    PhiK = D ** b / pa
    return pa / b * ((1 - h2(PhiX)) - f * h2(PhiK))


def rate_qct(D, b, f):
    pa = (1 - D) ** b + D ** b
    IE, _, _ = eve_info_distilled(D, b)
    PhiK = D ** b / pa
    return pa / b * ((1 - IE) - f * h2(PhiK))


def thr(fun, b, f, lo=0.0, hi=0.2499):
    if fun(lo, b, f) <= 0:
        return 0.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if fun(mid, b, f) > 0:
            lo = mid
        else:
            hi = mid
    return lo


rows = []
for f in (1.2, 1.0):
    for b in (1, 2, 3, 5, 7, 9, 11, 15, 21, 31):
        rows.append(dict(f=f, b=b, thr_EUR_T25=thr(rate_eur, b, f), thr_QCT_VA=thr(rate_qct, b, f)))
        print(rows[-1])
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "asymptotic_thresholds.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
