"""Set-2 adjudication: (a) total secrecy parameter rescaled to 1e-9 (eps_sec = 8e-10 so that 5 eps_sec/4 = 1e-9),
(b) post-selection-charged collective min-ent at b=11 and 15, (c) c_phi argmax boundary in D for the per-probe
information (symmetric family). Output data/panel_variants2.csv and data/cphi_argmax.csv"""
import os, sys, csv, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from skl import skl_qct_ad, threshold_qber, gw_deltas, tally_info, _CPHI_GRID
rows = []; t0 = time.time()
def rec(model, N, b, fun):
    q, deg, P = threshold_qber(fun, N, b); rows.append(dict(model=model, N=N, b=b, qber_thr=q)); print(rows[-1], "%.0fs" % (time.time() - t0), flush=True)
for b in (7,):
    rec("QCT_joint_shannon_bd_total1e-9", 1e14, b, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="shannon", attack="joint", bell="general", eps_sec=8e-10))
    rec("QCT_joint_minent_bd_total1e-9", 1e14, 11, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="minent", attack="joint", bell="general", eps_sec=8e-10))
for b in (11, 15):
    rec("QCT_joint_minent_bd_postsel", 1e14, b, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="minent", attack="joint", bell="general", postsel=True))
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "panel_variants2.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# (c) argmax boundary
am = []
grid = np.linspace(-1, 1, 801)
for b in (2, 3, 5, 9, 15):
    first = None
    for D in np.arange(0.15, 0.2495, 0.001):
        pa = (1 - D) ** b + D ** b; pu = (1 - D) ** b / pa; best = (-1, 1.0)
        for c in grid:
            r = gw_deltas(D, c)
            if r is None: continue
            d0, d1 = r; I = pu * tally_info(d0, b) + (1 - pu) * tally_info(d1, b)
            if I > best[0]: best = (I, c)
        if best[1] < 1 - 1e-9 and first is None: first = D
    am.append(dict(b=b, first_D_with_argmax_below_1=first)); print(am[-1], flush=True)
with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "cphi_argmax.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["b", "first_D_with_argmax_below_1"]); w.writeheader(); w.writerows(am)
print("done")
