"""High-precision (mpmath, 60 digits) asymptotic thresholds for large b, where double precision underflows
(1 - I_E and 1 - h(Phi_X) reach 1e-16 near the threshold for b >= 31). Recomputes data/asymptotic_thresholds.csv
and the asymptotic rows of data/joint_thresholds.csv. Output: data/asymptotic_thresholds_mp.csv"""
import os, sys, csv
import mpmath as mp
mp.mp.dps = 60
sys.path.insert(0, os.path.dirname(__file__))
from skl import _CPHI_GRID
def h(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1: return mp.mpf(0)
    return -x * mp.log(x, 2) - (1 - x) * mp.log(1 - x, 2)
def tally(delta, b):
    delta = mp.mpf(delta); H = mp.mpf(0)
    for k in range(b + 1):
        l0 = mp.binomial(b, k) * delta ** k * (1 - delta) ** (b - k); l1 = mp.binomial(b, k) * (1 - delta) ** k * delta ** (b - k)
        pk = (l0 + l1) / 2
        if pk > 0: H += pk * h(l0 / (l0 + l1))
    return 1 - H
def rate_eur(D, b, f):
    D = mp.mpf(D); pa = (1 - D) ** b + D ** b
    PhiX = ((1 - D) ** b - (1 - 3 * D) ** b) / (2 * pa); PhiX = min(max(PhiX, 0), mp.mpf(1) / 2)
    PhiK = D ** b / pa
    return pa / b * ((1 - h(PhiX)) - f * h(PhiK))
def eve_terms(D, b, joint):
    D = mp.mpf(D); pa = (1 - D) ** b + D ** b; pu = (1 - D) ** b / pa; F = 1 - D
    bestI = mp.mpf(-1); bestpg = mp.mpf(0)
    for c_phi in _CPHI_GRID:
        c_phi = mp.mpf(c_phi); c_psi = 2 + c_phi - (1 + c_phi) / F
        if c_psi < -1 or c_psi > 1: continue
        if joint:
            P0 = mp.mpf(1) / 2 + mp.sqrt(1 - abs(c_psi) ** (2 * b)) / 2; P1 = mp.mpf(1) / 2 + mp.sqrt(1 - abs(c_phi) ** (2 * b)) / 2
            I = pu * (1 - h(1 - P0)) + (1 - pu) * (1 - h(1 - P1)); pg = pu * P0 + (1 - pu) * P1
        else:
            d0 = mp.mpf(1) / 2 + mp.sqrt(1 - c_psi ** 2) / 2; d1 = mp.mpf(1) / 2 + mp.sqrt(1 - c_phi ** 2) / 2
            I = pu * tally(d0, b) + (1 - pu) * tally(d1, b); pg = mp.mpf(0)
        bestI = max(bestI, I); bestpg = max(bestpg, pg)
    return bestI, bestpg
def rate_ind(D, b, f):
    D = mp.mpf(D); pa = (1 - D) ** b + D ** b; I, _ = eve_terms(D, b, False); return pa / b * ((1 - I) - f * h(D ** b / pa))
def rate_joint(D, b, f, acc):
    D = mp.mpf(D); pa = (1 - D) ** b + D ** b; I, pg = eve_terms(D, b, True)
    H = (1 - I) if acc == "shannon" else -mp.log(pg, 2)
    return pa / b * (H - f * h(D ** b / pa))
def thr(fun, b, f, lo=mp.mpf("0.001"), hi=mp.mpf("0.2499")):
    if fun(lo, b, f) <= 0: return mp.mpf(0)
    for _ in range(45):
        mid = (lo + hi) / 2
        if fun(mid, b, f) > 0: lo = mid
        else: hi = mid
    return lo
rows = []
for f in (1.2, 1.0):
    for b in (1, 2, 3, 5, 7, 9, 11, 15, 21, 31, 41, 61):
        r = dict(f=f, b=b, thr_EUR_T25=float(thr(rate_eur, b, f)), thr_individual=float(thr(rate_ind, b, f)),
                 thr_joint_shannon=float(thr(lambda D, b_, f_: rate_joint(D, b_, f_, "shannon"), b, f)),
                 thr_joint_minent=float(thr(lambda D, b_, f_: rate_joint(D, b_, f_, "minent"), b, f)))
        rows.append(r); print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "asymptotic_thresholds_mp.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
