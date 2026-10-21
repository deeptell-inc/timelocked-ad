"""Explicit non-adaptive measurement attaining the adaptive Helstrom value (manuscript Sec. 3, Conjecture 1 evidence).
Projective measurement with fixed decision rule  a1_hat = y1 xor (y' . c)  (y in {0,1}^b outcome label).
Maximise P(O) = 2^-b sum_y <m_y|G_y|m_y> over orthonormal bases {m_y} by Riemannian gradient ascent on O(2^b)."""
import numpy as np, itertools, math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from joint_block_sdp import probe_states

def G_mats(D, b):
    c = 3 - 2 / (1 - D); psi0, psi1 = probe_states(c); dim = 2 ** b
    vec = {}
    for a in itertools.product((0, 1), repeat=b):
        v = np.array([1.0])
        for ai in a: v = np.kron(v, psi1 if ai else psi0)
        vec[a] = v
    cs = list(itertools.product((0, 1), repeat=b - 1))
    G = []
    for y in itertools.product((0, 1), repeat=b):
        g = np.zeros((dim, dim))
        for cc in cs:
            a1 = (y[0] + sum(yi * ci for yi, ci in zip(y[1:], cc))) % 2
            a = (a1,) + tuple((a1 + ci) % 2 for ci in cc)
            g += np.outer(vec[a], vec[a])
        G.append(g)
    pad = 0.5 + 0.5 * math.sqrt(1 - c ** (2 * b))
    return G, dim, pad

def ascend(G, dim, iters=4000, seed=0, O=None):
    rng = np.random.default_rng(seed)
    if O is None:
        O, _ = np.linalg.qr(rng.normal(size=(dim, dim)))
    def val(O): return sum(O[:, y] @ G[y] @ O[:, y] for y in range(dim)) / dim
    eta = 0.5; v = val(O)
    for it in range(iters):
        Gam = np.column_stack([2 * G[y] @ O[:, y] for y in range(dim)]) / dim
        grad = Gam - O @ Gam.T @ O
        while True:
            On, _ = np.linalg.qr(O + eta * grad)
            On = On * np.sign(np.sum(On * (O + eta * grad), axis=0))   # keep orientation
            vn = val(On)
            if vn >= v: break
            eta *= 0.5
            if eta < 1e-12: return O, v
        O, v = On, vn; eta = min(eta * 1.5, 5.0)
        if np.linalg.norm(grad) < 1e-11: break
    return O, v

if __name__ == "__main__":
    for b in [int(x) for x in sys.argv[1:]]:
        for D in (0.10, 0.20):
            G, dim, pad = G_mats(D, b)
            best = 0
            for s in range(3):
                O, v = ascend(G, dim, seed=s); best = max(best, v)
            print(f"b={b} D={D}: ansatz best {best:.9f}  P_ad {pad:.9f}  gap {pad-best:.2e}", flush=True)
