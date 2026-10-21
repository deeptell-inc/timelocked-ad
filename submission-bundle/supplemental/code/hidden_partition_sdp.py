"""Hidden block PARTITION as post-measurement information (panel adjudication).
n probes psi_{a_i}; the block containing probe 1 is {1} U J with J a (b-1)-subset of {2..n}, chosen uniformly
AFTER Eve's measurement; the parities c of that block are announced with it. Eve guesses a_1.
Classes (J, c): 2 mixed states each (a_1 = 0/1, other probes averaged). P_joint = SDP over POVMs indexed by
f: classes -> {0,1}. Compare with P_ad (= adaptive Helstrom per class = known-partition Theorem-1 value) and
P_ind (per-probe Helstrom + majority). Output data/hidden_partition_sdp.csv"""
import os, sys, csv, itertools, math, time
import numpy as np, cvxpy as cp
sys.path.insert(0, os.path.dirname(__file__))
from joint_block_sdp import probe_states
from skl import gw_delta0, majority_error

def run(n, b, D, solver="CLARABEL"):
    c = 3 - 2 / (1 - D); psi0, psi1 = probe_states(c); dim = 2 ** n
    vec = {}
    for a in itertools.product((0, 1), repeat=n):
        v = np.array([1.0])
        for ai in a: v = np.kron(v, psi1 if ai else psi0)
        vec[a] = v
    Js = list(itertools.combinations(range(1, n), b - 1))
    cs = list(itertools.product((0, 1), repeat=b - 1))
    classes = [(J, cc) for J in Js for cc in cs]; cidx = {k: i for i, k in enumerate(classes)}
    # class-conditional states rho_{class, a1} = average over all a with a_1 = a1 and parities cc on J
    rho = {}
    for (J, cc) in classes:
        for a1 in (0, 1):
            acc = np.zeros((dim, dim)); m = 0
            for a in itertools.product((0, 1), repeat=n):
                if a[0] != a1: continue
                if tuple((a[0] ^ a[j]) for j in J) != cc: continue
                acc += np.outer(vec[a], vec[a]); m += 1
            rho[(J, cc, a1)] = acc / m
    prior = 1.0 / (len(classes) * 2)
    fs = list(itertools.product((0, 1), repeat=len(classes)))
    W = [np.zeros((dim, dim)) for _ in fs]
    for (J, cc) in classes:
        for a1 in (0, 1):
            k = cidx[(J, cc)]
            for i, f in enumerate(fs):
                if f[k] == a1: W[i] += prior * rho[(J, cc, a1)]
    M = [cp.Variable((dim, dim), symmetric=True) for _ in fs]
    prob = cp.Problem(cp.Maximize(sum(cp.trace(Wk @ Mk) for Wk, Mk in zip(W, M))), [m >> 0 for m in M] + [sum(M) == np.eye(dim)])
    try: prob.solve(solver=solver)
    except Exception: prob.solve(solver="SCS", eps=1e-9, max_iters=200000)
    # adaptive (partition and parities known): Helstrom of the two class states, averaged
    def hel(r0, r1):
        w = np.linalg.eigvalsh((r0 - r1 + (r0 - r1).T) / 2); return 0.5 + 0.25 * np.sum(np.abs(w))
    pad = np.mean([hel(rho[(J, cc, 0)], rho[(J, cc, 1)]) for (J, cc) in classes])
    pind = 1 - majority_error(gw_delta0(D), b)
    return float(prob.value), float(pad), float(pind), c, len(fs)

if __name__ == "__main__":
    rows = []
    for n, b in ((3, 2), (4, 2), (5, 2), (4, 3)):
        for D in (0.10, 0.20):
            t0 = time.time(); pj, pad, pind, c, nf = run(n, b, D)
            rows.append(dict(n=n, b=b, D=D, c_psi=c, P_ind=pind, P_joint_hidden_partition=pj, P_adaptive=pad, n_povm=nf))
            print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in rows[-1].items()}, "%.0fs" % (time.time() - t0), flush=True)
    out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "hidden_partition_sdp.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("wrote", out)
