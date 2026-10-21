"""Asymptotic six-state AD rates (b=2) under three adversary bounds, from block guessing
probabilities P (class-averaged, accepted blocks):
  known   : adaptive Helstrom (bases and parities known)            -> P_ad
  hidden  : bases hidden, parities known (upper bound on Eve)        -> P_ck   (from sixstate_b2_mixed_cknown.log)
Rate per raw bit: (p_a/b) [ H_E - f h(Phi_K) ],  H_E = h(1-P) (Fano/Shannon) or -log2 P (min-entropy).
Usage: python sixstate_ad_rates.py  (reads data/sixstate_b2_mixed_cknown.log)"""
import os, re, math, sys
sys.path.insert(0, os.path.dirname(__file__))
from skl import h2

log = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sixstate_b2_mixed_cknown.log")
pts = {}
for line in open(log):
    m = re.search(r"c_psi=([\d.]+) D=([\d.]+) parity=\((\d),\) status=(\w+) P_joint\(c known, theta hidden\)=([\d.]+) P_ad=([\d.]+)", line)
    if m:
        c, D, par, st, pj, pad = m.groups()
        pts.setdefault((float(c), float(D)), {})[int(par)] = (float(pj), float(pad), st)
b = 2
for (c, D), d in sorted(pts.items()):
    pa = (1 - D) ** b + D ** b
    PhiK = D ** b / pa
    # classes with parity c=0 and c=1 are equiprobable
    for name, idx in (("hidden(c known)", 0), ("known", 1)):
        P = sum(v[idx] for v in d.values()) / len(d)
        for f in (1.0, 1.2):
            r_sh = pa / b * (h2(1 - P) - f * h2(PhiK))
            r_me = pa / b * (-math.log2(P) - f * h2(PhiK))
            print(f"c_psi={c:.2f} D={D:.3f} {name:16s} P={P:.5f} f={f}: rate_Shannon={r_sh:+.4f} rate_minent={r_me:+.4f}  status={[v[2] for v in d.values()]}")
