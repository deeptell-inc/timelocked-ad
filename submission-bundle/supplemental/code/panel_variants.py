"""Panel adjudication: (a) post-selection-charged thresholds, (b) Fano/majority-vote variant (superseded accounting),
(c) no-timelock Holevo baseline. Output data/panel_variants.csv"""
import os, sys, csv, math, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import skl
from skl import skl_qct_ad, threshold_qber, _CPHI_GRID, _h2v
rows = []; t0 = time.time()
def rec(model, N, b, fun):
    q, deg, P = threshold_qber(fun, N, b)
    rows.append(dict(model=model, N=N, b=b, qber_thr=q)); print(rows[-1], "%.0fs" % (time.time() - t0), flush=True)
for b in (7, 9):
    for att in ("joint", "individual"):
        for ent in ("shannon", "minent"):
            rec(f"QCT_{att}_{ent}_bd_postsel", 1e14, b, lambda N_, P_, ch_, b_, a=att, e=ent: skl_qct_ad(N_, P_, ch_, b_, entropy=e, attack=a, bell="general", postsel=True))
rec("QCT_individual_shannon_sym_fano", 1e14, 9, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="shannon", attack="individual", fano=True))
rec("QCT_individual_shannon_sym_fano", 1e8, 3, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="shannon", attack="individual", fano=True))
# Holevo baseline: replace I_acc by chi = h((1+|c|^b)/2) per block type (no timelock), Bell-diagonal, sup over D'
_orig = skl.eve_info_bd
def eve_info_holevo(Dz, phiX, b, attack="joint", sup=True, ngrid=33):
    if Dz <= 0: return 0.0, 0.5, 1.0
    if Dz >= 0.5: return 1.0, 1.0, 1.0
    Dgrid = np.linspace(Dz / ngrid, Dz, ngrid); C = np.array(_CPHI_GRID)[None, :]; D = Dgrid[:, None]
    l4 = D * (1 - C) / 2; feas = (l4 <= phiX + 1e-15) & (1 - D - phiX + l4 >= -1e-15)
    cpsi = np.clip((1 - 2 * phiX - D * C) / (1 - D), -1, 1); pa = (1 - D) ** b + D ** b; pu = (1 - D) ** b / pa
    chi0 = _h2v((1 + np.abs(cpsi) ** b) / 2); chi1 = _h2v((1 + np.abs(C) ** b) / 2)
    IE = pu * chi0 + (1 - pu) * chi1; IE = np.where(feas, IE, -1.0)
    return float(IE.max()), 0.5, float(pu[-1, 0])
skl.eve_info_bd = eve_info_holevo
for b in (5, 7, 9):
    rec("holevo_no_timelock_shannon_bd", 1e14, b, lambda N_, P_, ch_, b_: skl_qct_ad(N_, P_, ch_, b_, entropy="shannon", attack="joint", bell="general"))
skl.eve_info_bd = _orig
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "panel_variants.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote", out)
