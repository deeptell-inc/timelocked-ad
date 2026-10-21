"""Worst case over *joint, non-adaptive* measurements on one AD block (U1, within-block).

Setting (QCT tier V-A, collective attack, symmetric probe family of Gisin-Wolf with
c_phi = 1 so that Eve learns nothing from disturbed bits): for an accepted all-undisturbed
block of b bits, Eve holds the product state psi_{a1} x ... x psi_{ab} of pure qubit probe
states with overlap c_psi = <psi_0|psi_1> = 3 - 2/(1-D). She must measure BEFORE learning the
parity string c = (a1^a2, ..., a_{b-1}^a_b) and afterwards guess a1 = the distilled bit.
This is state discrimination with post-measurement information (Ballester-Wehner-Winter):
a POVM {M_f} indexed by functions f : {0,1}^{b-1} -> {0,1}, success probability
    P_joint = 2^-b sum_a Tr[ rho_a sum_{f : f(c(a)) = a1(a)} M_f ].
Compared with
    P_ind  = individual Helstrom per probe + majority vote (skl.majority_error),
    P_ad   = adaptive Helstrom on the two product states of the class c (upper bound,
             = what an adversary who waits for c can do) = 1/2 + 1/2 sqrt(1 - c_psi^(2b)).
Solved as an SDP with cvxpy (deterministic, interior point). Output: data/joint_block_sdp.csv
"""
import os, sys, csv, itertools, math, time
import numpy as np
import cvxpy as cp
sys.path.insert(0, os.path.dirname(__file__))
from skl import gw_delta0, majority_error


def probe_states(c_psi):
    th = 0.5 * math.acos(c_psi)              # <psi0|psi1> = cos(2 th)
    psi0 = np.array([math.cos(th), math.sin(th)])
    psi1 = np.array([math.cos(th), -math.sin(th)])
    return psi0, psi1


def block_state(a, psi0, psi1):
    v = np.array([1.0])
    for ai in a:
        v = np.kron(v, psi1 if ai else psi0)
    return np.outer(v, v)


def parity(a):
    return tuple(a[i] ^ a[i + 1] for i in range(len(a) - 1))


def p_joint(D, b, solver="CLARABEL"):
    c_psi = min(max(3.0 - 2.0 / (1.0 - D), -1.0), 1.0)
    psi0, psi1 = probe_states(c_psi)
    dim = 2 ** b
    cs = list(itertools.product((0, 1), repeat=b - 1))
    fs = list(itertools.product((0, 1), repeat=len(cs)))          # f as tuple over cs
    cidx = {c: i for i, c in enumerate(cs)}
    # all states are real, so an optimal POVM can be taken real symmetric (average M with M*)
    M = [cp.Variable((dim, dim), symmetric=True) for _ in fs]
    cons = [m >> 0 for m in M] + [sum(M) == np.eye(dim)]
    # objective  sum_f Tr[W_f M_f]  with  W_f = 2^-b sum_{a : f(c(a)) = a1} rho_a   (precomputed)
    W = [np.zeros((dim, dim)) for _ in fs]
    for a in itertools.product((0, 1), repeat=b):
        rho = block_state(a, psi0, psi1) / dim
        j = cidx[parity(a)]
        for k, f in enumerate(fs):
            if f[j] == a[0]:
                W[k] += rho
    obj = sum(cp.trace(Wk @ Mk) for Wk, Mk in zip(W, M))
    prob = cp.Problem(cp.Maximize(obj), cons)
    try:
        prob.solve(solver=solver)
    except Exception:
        prob.solve(solver="SCS", eps=1e-9, max_iters=200000)
    return float(prob.value), c_psi


def p_ind(D, b):
    return 1.0 - majority_error(gw_delta0(D), b)


def p_ad(D, b):
    c_psi = min(max(3.0 - 2.0 / (1.0 - D), -1.0), 1.0)
    return 0.5 + 0.5 * math.sqrt(1.0 - c_psi ** (2 * b))


if __name__ == "__main__":
    rows = []
    for b in (2, 3, 4):
        for D in (0.05, 0.10, 0.15, 0.18, 0.20, 0.22, 0.24):
            t0 = time.time()
            pj, cps = p_joint(D, b)
            print("b=%d D=%.2f solved in %.0f s" % (b, D, time.time() - t0), flush=True)
            rows.append(dict(b=b, D=D, c_psi=cps, P_ind=p_ind(D, b), P_joint=pj, P_adaptive=p_ad(D, b)))
            print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in rows[-1].items()}, flush=True)
    out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "joint_block_sdp.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("wrote", out)
