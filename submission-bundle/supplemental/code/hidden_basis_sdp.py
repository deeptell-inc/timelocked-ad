"""P1'': both-basis keying with delayed sifting (basis AND parities hidden until after t_coh).

Attack: Gisin-Wolf symmetric collective attack with probe overlaps (c_psi, c_phi); the isometry
  V|up>  = sqrt(F)|up>psi_up + sqrt(D)|dn>phi_up,   V|dn> = sqrt(F)|dn>psi_dn + sqrt(D)|up>phi_dn
is built explicitly on a 4-dimensional probe (e1=psi_up, e2 in span(psi), e3=phi_up, e4 in span(phi)).
For an input |a_theta> (theta in {Z,X}) and Bob's outcome y (in basis theta), Eve's conditional
probe state rho_{theta,a,y} = Tr_B[(|y><y| x 1) V|a_theta><a_theta|V^dag] / p(y|a,theta).
AD block (size b): Alice bits a, Bob bits y with y=a (prob (1-D)^b) or y=a_bar (prob D^b) when accepted.
Eve's state for class (theta^b, parity c): rho^{acc}_{theta,a} = [(1-D)^b rho_{theta,a,a} + D^b rho_{theta,a,abar}] / p_a.
Hidden information at measurement time: (theta^b, c). Non-adaptive POVM indexed by functions
f: (theta^b, c) -> guess of a1. SDP value P_joint vs adaptive Helstrom per class P_ad.
"""
import os, sys, csv, itertools, math
import numpy as np
import cvxpy as cp

ket = {0: np.array([1.0, 0.0]), 1: np.array([0.0, 1.0])}
X0 = np.array([1.0, 1.0]) / math.sqrt(2)
X1 = np.array([1.0, -1.0]) / math.sqrt(2)
Y0 = np.array([1.0, 1j]) / math.sqrt(2)
Y1 = np.array([1.0, -1j]) / math.sqrt(2)
BASIS = {"Z": (ket[0], ket[1]), "X": (X0, X1), "Y": (Y0, Y1)}


def probes(c_psi, c_phi):
    e = np.eye(4)
    psi_up = e[0]; psi_dn = c_psi * e[0] + math.sqrt(max(0, 1 - c_psi ** 2)) * e[1]
    phi_up = e[2]; phi_dn = c_phi * e[2] + math.sqrt(max(0, 1 - c_phi ** 2)) * e[3]
    F = (1 + c_phi) / (2 - c_psi + c_phi)
    D = 1 - F
    return psi_up, psi_dn, phi_up, phi_dn, F, D


def isometry(c_psi, c_phi):
    psi_up, psi_dn, phi_up, phi_dn, F, D = probes(c_psi, c_phi)
    V = np.zeros((8, 2))            # (bob 2) x (probe 4) <- qubit
    V[:, 0] = math.sqrt(F) * np.kron(ket[0], psi_up) + math.sqrt(D) * np.kron(ket[1], phi_up)
    V[:, 1] = math.sqrt(F) * np.kron(ket[1], psi_dn) + math.sqrt(D) * np.kron(ket[0], phi_dn)
    assert np.allclose(V.T @ V, np.eye(2), atol=1e-12)
    return V, D


def cond_probe(V, theta, a, y):
    """Eve's probe state given input a in basis theta and Bob's outcome y (same basis).
    Returns (rho (4x4), p(y|a,theta))."""
    inp = BASIS[theta][a]
    out = V.astype(complex) @ inp                   # 8-vector, index = bob*4 + probe
    out = out.reshape(2, 4)                         # [bob, probe]
    yb = BASIS[theta][y]
    amp = yb.conj() @ out                           # projection of Bob onto |y>: 4-vector (probe)
    p = float(np.real(amp.conj() @ amp))
    rho = np.outer(amp, amp.conj()) / p if p > 1e-15 else np.zeros((4, 4), dtype=complex)
    return rho, p


def block_states(c_psi, c_phi, b, thetas):
    """Return dict {(theta_tuple, a_tuple): rho_acc (4^b x 4^b)} and D."""
    V, D = isometry(c_psi, c_phi)
    pa = (1 - D) ** b + D ** b
    out = {}
    for th in thetas:
        for a in itertools.product((0, 1), repeat=b):
            rho_same = np.array([[1.0]]); rho_flip = np.array([[1.0]])
            for i in range(b):
                r_s, p_s = cond_probe(V, th[i], a[i], a[i])
                r_f, p_f = cond_probe(V, th[i], a[i], 1 - a[i])
                rho_same = np.kron(rho_same, r_s); rho_flip = np.kron(rho_flip, r_f)
            out[(th, a)] = ((1 - D) ** b * rho_same + D ** b * rho_flip) / pa
    return out, D


def parity(a):
    return tuple(a[i] ^ a[i + 1] for i in range(len(a) - 1))


def helstrom(r0, r1):
    w = np.linalg.eigvalsh((r0 - r1 + (r0 - r1).conj().T) / 2)
    return 0.5 + 0.25 * float(np.sum(np.abs(w)))


def solve(c_psi, c_phi, b, mode="mixed", solver="CLARABEL", bases="ZX"):
    """mode: 'mixed' -> theta^b uniform over bases^b ; 'same' -> theta^b in {t^b : t in bases}.
    bases='ZX' (BB84) or 'ZXY' (six-state; symmetric attack needs c_phi=0)."""
    thetas = list(itertools.product(bases, repeat=b)) if mode == "mixed" else [tuple(t * b) for t in bases]
    states, D = block_states(c_psi, c_phi, b, thetas)
    classes = [(th, c) for th in thetas for c in itertools.product((0, 1), repeat=b - 1)]
    cidx = {k: i for i, k in enumerate(classes)}
    dim = 4 ** b
    fs = list(itertools.product((0, 1), repeat=len(classes)))
    M = [cp.Variable((dim, dim), hermitian=True) for _ in fs]
    cons = [m >> 0 for m in M] + [sum(M) == np.eye(dim)]
    obj = 0
    prior = 1.0 / (len(thetas) * 2 ** b)
    for (th, a), rho in states.items():
        j = cidx[(th, parity(a))]
        S = sum(M[k] for k, f in enumerate(fs) if f[j] == a[0])
        obj = obj + prior * cp.real(cp.trace(rho @ S))
    prob = cp.Problem(cp.Maximize(obj), cons)
    prob.solve(solver=solver)
    # adaptive value: Helstrom within each class, averaged
    pad = 0.0
    for (th, c) in classes:
        a0 = [a for (t, a) in states if t == th and parity(a) == c and a[0] == 0][0]
        a1 = [a for (t, a) in states if t == th and parity(a) == c and a[0] == 1][0]
        pad += helstrom(states[(th, a0)], states[(th, a1)]) / len(classes)
    return float(prob.value), pad, D


if __name__ == "__main__":
    rows = []
    for b in (1, 2):
        for c_phi in (1.0, 0.0, -1.0):
            for c_psi in (0.9, 0.8, 0.7, 0.6, 0.5, 0.4):
                for mode in (("mixed", "same") if b > 1 else ("mixed",)):
                    try:
                        pj, pad, D = solve(c_psi, c_phi, b, mode)
                    except Exception as e:
                        print("fail", b, c_phi, c_psi, mode, e); continue
                    rows.append(dict(b=b, mode=mode, c_phi=c_phi, c_psi=c_psi, D=D, P_joint=pj, P_adaptive=pad))
                    print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in rows[-1].items()}, flush=True)
    out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "hidden_basis_sdp.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("wrote", out)
