"""Per-probe adversary with hidden block partition: identical, non-adaptive single-probe POVMs (rank-1, up to 4
outcomes, real; Naimark parametrisation E_k = V^T |m_k><m_k| V with {m_k} an orthonormal basis of R^4), followed by
parity disclosure and optimal classical decoding of a_1. Maximises the block information J and the guessing
probability separately over the POVM and compares with Helstrom + tally (the model used in the manuscript).
Output: data/perprobe_opt.csv"""
import os, sys, csv, math, itertools, time
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm
from math import lgamma
sys.path.insert(0, os.path.dirname(__file__))
from skl import gw_delta0, tally_info, majority_error

def histograms(b, K):
    # all compositions of b into K parts
    for cuts in itertools.combinations(range(b + K - 1), K - 1):
        prev = -1; h = []
        for c in cuts: h.append(c - prev - 1); prev = c
        h.append(b + K - 2 - prev); yield tuple(h)

def block_stats(p0, p1, b):
    """p0[k], p1[k]: outcome probabilities for a_i = 0 / 1. Categories (k, c) with c uniform:
    P(k,c | a1) = 1/2 * p_{a1 xor c}[k]. Returns (J bits, p_guess) over b i.i.d. probes."""
    K = len(p0)
    q0 = np.concatenate([0.5 * p0, 0.5 * p1])      # a1 = 0: c=0 -> p0, c=1 -> p1
    q1 = np.concatenate([0.5 * p1, 0.5 * p0])      # a1 = 1
    H = np.array(list(histograms(b, 2 * K)))
    logmult = lgamma(b + 1) - np.sum([np.vectorize(lgamma)(H[:, j] + 1) for j in range(2 * K)], axis=0)
    with np.errstate(divide='ignore'):
        l0 = logmult + H @ np.log(np.maximum(q0, 1e-300)); l1 = logmult + H @ np.log(np.maximum(q1, 1e-300))
    P0 = np.exp(l0); P1 = np.exp(l1); Pm = 0.5 * (P0 + P1)
    post = np.where(Pm > 0, P0 / np.maximum(P0 + P1, 1e-300), 0.5)
    hb = lambda x: -np.where(x > 0, x * np.log2(np.maximum(x, 1e-300)), 0) - np.where(x < 1, (1 - x) * np.log2(np.maximum(1 - x, 1e-300)), 0)
    J = 1 - np.sum(Pm * hb(post)); pg = np.sum(np.maximum(P0, P1)) / 2
    return float(J), float(pg)

def povm_probs(x, c):
    th = 0.5 * math.acos(c); psi0 = np.array([math.cos(th), math.sin(th), 0, 0]); psi1 = np.array([math.cos(th), -math.sin(th), 0, 0])
    A = np.zeros((4, 4)); A[np.triu_indices(4, 1)] = x; O = expm(A - A.T)
    p0 = (O.T @ psi0) ** 2; p1 = (O.T @ psi1) ** 2
    return p0, p1

def optimise(c, b, target, restarts=12, seed=0):
    rng = np.random.default_rng(seed); best = -1; bx = None
    def obj(x):
        p0, p1 = povm_probs(x, c); J, pg = block_stats(p0, p1, b)
        return -(J if target == "info" else pg)
    for r in range(restarts):
        x0 = rng.normal(size=6) * (0.3 if r else 0.0)
        res = minimize(obj, x0, method="Nelder-Mead", options=dict(maxiter=4000, xatol=1e-9, fatol=1e-12))
        if -res.fun > best: best, bx = -res.fun, res.x
    return best

if __name__ == "__main__":
    rows = []
    for b in (2, 3, 4, 5, 7, 9):
        for D in (0.10, 0.17, 0.20, 0.23):
            t0 = time.time(); c = 3 - 2 / (1 - D); d0 = gw_delta0(D)
            J_h = tally_info(d0, b); pg_h = 1 - majority_error(d0, b)
            J_opt = optimise(c, b, "info"); pg_opt = optimise(c, b, "guess")
            rows.append(dict(b=b, D=D, J_helstrom=J_h, J_opt=J_opt, pg_helstrom=pg_h, pg_opt=pg_opt))
            print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in rows[-1].items()}, "%.0fs" % (time.time() - t0), flush=True)
    out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "perprobe_opt.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("wrote", out)
