"""Achievable (lower-bound) success probability for the six-state b=2 MIXED-basis block with BOTH the
bases and the parities hidden: projective (rank-1, 16-outcome) measurement + optimal per-outcome decision,
optimised by alternating (decision rule | unitary) ascent. Compared with the adaptive value P_ad."""
import sys, os, itertools, math, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from hidden_basis_sdp import block_states, parity, helstrom

def problem(c_psi, b=2, bases="ZXY"):
    thetas = list(itertools.product(bases, repeat=b))
    states, D = block_states(c_psi, 0.0, b, thetas)
    classes = [(th, c) for th in thetas for c in itertools.product((0, 1), repeat=b - 1)]
    prior = 1.0 / (len(thetas) * 2 ** b)
    R = []   # per class: (rho_{a1=0}, rho_{a1=1})
    for (th, c) in classes:
        a0 = [a for (t, a) in states if t == th and parity(a) == c and a[0] == 0][0]
        a1 = [a for (t, a) in states if t == th and parity(a) == c and a[0] == 1][0]
        R.append((states[(th, a0)], states[(th, a1)]))
    pad = sum(helstrom(r0, r1) for r0, r1 in R) / len(R)
    return R, prior, pad, D

def value(O, R, prior):
    tot = 0.0
    for y in range(O.shape[1]):
        m = O[:, y]
        for r0, r1 in R:
            tot += max(np.real(m.conj() @ r0 @ m), np.real(m.conj() @ r1 @ m))
    return prior * tot

def ascend(R, prior, dim, seed, outer=60, inner=400):
    rng = np.random.default_rng(seed)
    O, _ = np.linalg.qr(rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim)))
    v = value(O, R, prior)
    for _ in range(outer):
        # decision rule given O
        G = []
        for y in range(dim):
            m = O[:, y]; g = np.zeros((dim, dim), dtype=complex)
            for r0, r1 in R:
                g += r0 if np.real(m.conj() @ r0 @ m) >= np.real(m.conj() @ r1 @ m) else r1
            G.append(prior * g)
        eta = 0.5
        for _ in range(inner):
            Gam = np.column_stack([2 * G[y] @ O[:, y] for y in range(dim)])
            grad = Gam - O @ Gam.conj().T @ O
            cur = sum(np.real(O[:, y].conj() @ G[y] @ O[:, y]) for y in range(dim))
            while True:
                On, _ = np.linalg.qr(O + eta * grad)
                vn = sum(np.real(On[:, y].conj() @ G[y] @ On[:, y]) for y in range(dim))
                if vn >= cur: break
                eta *= 0.5
                if eta < 1e-13: break
            if eta < 1e-13: break
            O = On; eta = min(eta * 1.5, 5.0)
        vn = value(O, R, prior)
        if vn - v < 1e-13: v = vn; break
        v = vn
    return O, v

if __name__ == "__main__":
    for c_psi in (0.8, 0.65):
        R, prior, pad, D = problem(c_psi); dim = R[0][0].shape[0]
        best = 0
        for s in range(6):
            O, v = ascend(R, prior, dim, s); best = max(best, v)
            print(f"  seed {s}: {v:.7f}", flush=True)
        print(f"six-state b=2 mixed, bases+parities hidden: c_psi={c_psi} D={D:.3f}  P_achievable>={best:.6f}  P_ad={pad:.6f}  gap<={pad-best:.2e}", flush=True)
