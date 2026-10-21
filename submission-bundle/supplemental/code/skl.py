"""Finite-key secure-key-length (SKL) calculator for decoy-state BB84 with
advantage distillation (AD), and its QCT (quantum computational timelock) variant.

Reference formulas (Treplin, Kleinpass, Orsucci, arXiv:2511.21665, "T25"):
  Eq. 6-19   statistical bounds, decoy bounds, S^-_Kbar (18), Phi^+_Xbar (19)
  Eq. 20     expected distilled length / QBER
  Eq. 93     SKL with AD        Eq. 94  SKL without AD (Wiesemann et al.)
  Eq. 95-98  channel / detector model

QCT V-A variant (this work, theory-foundation.md):
  Eve's quantum side information is replaced by the classical side information of
  the optimal *incoherent* (individual, symmetric) attack of Gisin & Wolf
  (quant-ph/9902048, Eq. 1-5, Thm. 1): Eve learns Z1 = X xor Y (whether Bob's bit was
  disturbed) and a guess Z2 of Bob's bit, correct w.p. delta0 on undisturbed bits.
  The AD-worst-case attack maximises delta0 at fixed disturbance D:
      delta0(D) = 1/2 + 1/2*sqrt(1 - c^2),  c = 3 - 2/(1-D)   (c_phi = 1, delta1 = 1/2)
  which reproduces the Gisin-Wolf threshold D < 1/4 for BB84 (checked in tests).

All functions are pure numpy; no randomness anywhere (deterministic).
"""
from __future__ import annotations
import math
from dataclasses import dataclass
import numpy as np
from scipy.optimize import minimize

LN2 = math.log(2.0)


def h2(p: float) -> float:
    p = min(max(p, 0.0), 1.0)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


# ---------------------------------------------------------------- T25 Eq. 7-10
def delta_H(N, eps):            # Hoeffding
    return math.sqrt(max(N, 0.0) / 2.0 * math.log(1.0 / eps))


def delta_Cp(n, eps):           # Chernoff upper
    L = math.log(1.0 / eps)
    return L + math.sqrt(2.0 * max(n, 0.0) * L + L * L)


def delta_Cm(n, eps):           # Chernoff lower
    L = math.log(1.0 / eps)
    return L / 2.0 + math.sqrt(2.0 * max(n, 0.0) * L + L * L / 4.0)


def delta_p(N, n, eps):
    return min(delta_H(N, eps), delta_Cp(n, eps))


def delta_m(N, n, eps):
    return min(delta_H(N, eps), delta_Cm(n, eps))


def nu(n, k, eps):              # Eq. 10 (random sampling without replacement)
    if n <= 0 or k <= 0:
        return 1.0
    return math.sqrt((n + k) * (k + 1) / (2.0 * n * k * k) * math.log(1.0 / eps))


# ---------------------------------------------------------------- protocol
@dataclass
class Params:
    mu1: float
    mu2: float
    mu3: float
    p_mu1: float
    p_mu2: float
    pZ: float
    qT: float          # fraction of Z bits used as test set (AD only)

    @property
    def p_mu3(self):
        return 1.0 - self.p_mu1 - self.p_mu2

    @property
    def pX(self):
        return 1.0 - self.pZ

    def valid(self):
        return (self.mu1 > self.mu2 + self.mu3 and self.mu2 > self.mu3 >= 0 and
                0 < self.p_mu1 and 0 < self.p_mu2 and self.p_mu3 > 0 and
                0 < self.pZ < 1 and 0 <= self.qT < 1)


@dataclass
class Channel:
    eta: float = 1.0        # end-to-end transmission
    p_noise: float = 0.0    # noise-click probability
    delta_mis: float = 0.0  # misalignment angle [rad]


def click_probs(mu, ch: Channel):        # Eq. 95-96
    pc = 1.0 - (1.0 - ch.p_noise) * math.exp(-ch.eta * mu * math.cos(ch.delta_mis) ** 2)
    pw = 1.0 - (1.0 - ch.p_noise) * math.exp(-ch.eta * mu * math.sin(ch.delta_mis) ** 2)
    p_out = pc * (1 - pw) + pw * (1 - pc) + pc * pw
    p_err = pw * (1 - pc) + 0.5 * pc * pw
    return p_out, p_err


def expected_counts(N, P: Params, ch: Channel):   # Eq. 97-98 (expectation values)
    mus = (P.mu1, P.mu2, P.mu3)
    pmus = (P.p_mu1, P.p_mu2, P.p_mu3)
    n = {}
    m = {}
    for f in ("Z", "T", "X"):
        if f == "Z":
            w = P.pZ ** 2 * (1 - P.qT)
        elif f == "T":
            w = P.pZ ** 2 * P.qT
        else:
            w = P.pX ** 2
        for mu, pmu in zip(mus, pmus):
            po, pe = click_probs(mu, ch)
            n[(f, mu)] = N * pmu * po * w
            m[(f, mu)] = N * pmu * pe * w
    return n, m


def tau(k, P: Params, only12=False):
    mus = (P.mu1, P.mu2, P.mu3)
    pmus = (P.p_mu1, P.p_mu2, P.p_mu3)
    if only12:
        mus, pmus = mus[:2], pmus[:2]
    return sum(p * math.exp(-mu) * mu ** k / math.factorial(k) for mu, p in zip(mus, pmus))


# ---------------------------------------------------------------- T25 Eq. 12-19
def decoy_bounds(N, P: Params, ch: Channel, eps_bar):
    n, m = expected_counts(N, P, ch)
    mu1, mu2, mu3 = P.mu1, P.mu2, P.mu3
    pm = {mu1: P.p_mu1, mu2: P.p_mu2, mu3: P.p_mu3}
    t0, t1 = tau(0, P), tau(1, P)
    out = {}
    for f in ("Z", "T", "X"):
        nf = sum(n[(f, mu)] for mu in (mu1, mu2, mu3))
        np_ = {mu: n[(f, mu)] + delta_p(nf, n[(f, mu)], eps_bar) for mu in (mu1, mu2, mu3)}
        nm_ = {mu: max(n[(f, mu)] - delta_m(nf, n[(f, mu)], eps_bar), 0.0) for mu in (mu1, mu2, mu3)}
        o_minus = t0 / (mu2 - mu3) * (mu2 * math.exp(mu3) * nm_[mu3] / pm[mu3]
                                      - mu3 * math.exp(mu2) * np_[mu2] / pm[mu2])          # Eq. 14a
        o_minus = max(o_minus, 0.0)
        s_minus = t1 * mu1 / (mu1 * (mu2 - mu3) - (mu2 ** 2 - mu3 ** 2)) * (
            math.exp(mu2) * nm_[mu2] / pm[mu2] - math.exp(mu3) * np_[mu3] / pm[mu3]
            + (mu2 ** 2 - mu3 ** 2) / mu1 ** 2 * (o_minus / t0 - math.exp(mu1) * np_[mu1] / pm[mu1]))  # Eq. 14b
        s_minus = max(s_minus, 0.0)
        out[f] = dict(n=nf, o_minus=o_minus, s_minus=s_minus)
        if f in ("T", "X"):
            mf = sum(m[(f, mu)] for mu in (mu1, mu2, mu3))
            mp_ = {mu: m[(f, mu)] + delta_p(mf, m[(f, mu)], eps_bar) for mu in (mu1, mu2, mu3)}
            mm_ = {mu: max(m[(f, mu)] - delta_m(mf, m[(f, mu)], eps_bar), 0.0) for mu in (mu1, mu2, mu3)}
            e_plus = t1 / (mu2 - mu3) * (math.exp(mu2) * mp_[mu2] / pm[mu2]
                                         - math.exp(mu3) * mm_[mu3] / pm[mu3])              # Eq. 16
            out[f]["e_plus"] = max(e_plus, 0.0)
    # key-generation set K = Z without vacuum intensity
    nK = n[("Z", mu1)] + n[("Z", mu2)]
    mK = m[("Z", mu1)] + m[("Z", mu2)]
    t1p = tau(1, P, only12=True)
    t0p = tau(0, P, only12=True)
    sK_minus = t1p / t1 * out["Z"]["s_minus"]                                                # Eq. 15/68
    oK_minus = t0p / t0 * out["Z"]["o_minus"]                                                # Eq. 66
    phiZ_plus = out["T"]["e_plus"] / max(out["T"]["s_minus"], 1e-300) + nu(sK_minus, out["T"]["s_minus"], eps_bar)  # 17a
    phiX_plus = out["X"]["e_plus"] / max(out["X"]["s_minus"], 1e-300) + nu(sK_minus, out["X"]["s_minus"], eps_bar)  # 17b
    phiZ_plus = min(phiZ_plus, 0.5)
    phiX_plus = min(phiX_plus, 0.5)
    return dict(nK=nK, mK=mK, phiK=(mK / nK if nK > 0 else 0.5), sK_minus=sK_minus, oK_minus=oK_minus,
                phiZ_plus=phiZ_plus, phiX_plus=phiX_plus, sets=out)


def ad_block_bounds(D, b, eps_bar, stat="mcdiarmid"):
    """T25 Eq. 18-19 ingredients. D = decoy_bounds(...).
    stat='mcdiarmid': T25 Eq. 18 (3*delta_H correction).
    stat='jiang'    : second route - virtual-IID reduction of Jiang et al. 2021 (Result 2.1):
                      the count of accepted all-single-photon blocks is lower-bounded by the
                      Chernoff lower tail of Binomial(nblk, frac*acc) with failure prob. 2x."""
    nK, sK = D["nK"], D["sK_minus"]
    pZ, pX = D["phiZ_plus"], D["phiX_plus"]
    nblk = math.floor(nK / b)
    if nblk <= 0 or sK <= 0:
        return 0.0, 0.5, 0.0
    frac = (sK / nK) ** b
    acc = (1 - pZ) ** b + pZ ** b - b * (b - 1) / sK
    if stat == "jiang":
        mean = nblk * frac * acc
        S_minus = mean - delta_Cm(mean, eps_bar / 2.0)
    else:
        S_minus = nblk * frac * acc - 3 * delta_H(nK, eps_bar)                              # Eq. 18
    dprime = (nK / sK) ** b * 3 * delta_H(nK, eps_bar) / nblk

    def phi_of(z):                              # Eq. 19 evaluated at Z-error z, X-error pX
        accz = (1 - z) ** b + z ** b - b * (b - 1) / sK
        num = 0.5 * ((1 - z) ** b - (1 - z - 2 * pX) ** b) + dprime
        den = accz - dprime
        return num / den if den > 0 else 0.5
    # Eq. 19 is not monotone in z (all-wrong accepted blocks carry no phase error), so the
    # true single-photon Z error z <= phiZ_plus must be maximised over, not replaced by phiZ_plus.
    Phi_plus = max(phi_of(pZ * i / 200.0) for i in range(201))
    Phi_plus = min(max(Phi_plus, 0.0), 0.5)
    return max(S_minus, 0.0), Phi_plus, acc


def _degenerate(D):
    """True if any single-photon estimate is degenerate (no key can be certified)."""
    return (D["sK_minus"] <= 0 or D["sets"]["T"]["s_minus"] <= 0 or D["sets"]["X"]["s_minus"] <= 0
            or D["phiZ_plus"] >= 0.5 or D["phiX_plus"] >= 0.5)


def distilled_stats(phiK, nK, b):                                                           # Eq. 20
    pa = (1 - phiK) ** b + phiK ** b
    NK = math.floor(nK / b) * pa
    PhiK = phiK ** b / pa
    return NK, PhiK, pa


# ---------------------------------------------------------------- SKL formulas
def skl_ad(N, P: Params, ch: Channel, b, eps_sec=1e-9, eps_cor=1e-15, f=1.2):
    """T25 Eq. 93 (acceptance thresholds set equal to the computed bounds)."""
    eps_bar = eps_sec ** 2 / 368.0
    D = decoy_bounds(N, P, ch, eps_bar)
    if _degenerate(D):
        return -math.inf, dict(D=D)
    if D["phiX_plus"] + D["phiZ_plus"] >= 0.5:      # domain of T25 Eq. 19 (Appendix B)
        return -math.inf, dict(D=D)
    S_minus, Phi_plus, _ = ad_block_bounds(D, b, eps_bar)
    NK, PhiK, _ = distilled_stats(D["phiK"], D["nK"], b)
    lam_IR = f * NK * h2(PhiK)
    ell = S_minus * (1 - h2(Phi_plus)) - lam_IR - math.log2(2 / eps_cor) \
        - 4 * math.log2(2 ** (7 / 4) / (eps_sec - eps_sec ** 2 / 8))
    return ell, dict(D=D, S_minus=S_minus, Phi_plus=Phi_plus, NK=NK, PhiK=PhiK, lam_IR=lam_IR)


def skl_bb84(N, P: Params, ch: Channel, eps_sec=1e-9, eps_cor=1e-15, f=1.2):
    """T25 Eq. 94 (Wiesemann et al. form), no AD. qT is ignored (set 0)."""
    P0 = Params(P.mu1, P.mu2, P.mu3, P.p_mu1, P.p_mu2, P.pZ, 0.0)
    eps_bar = eps_sec ** 2 / 368.0
    D = decoy_bounds(N, P0, ch, eps_bar)
    if D["sK_minus"] <= 0 or D["sets"]["X"]["s_minus"] <= 0 or D["phiX_plus"] >= 0.5:
        return -math.inf, dict(D=D)
    ell = D["oK_minus"] + D["sK_minus"] * (1 - h2(D["phiX_plus"])) - f * D["nK"] * h2(D["phiK"]) \
        - math.log2(2 / eps_cor) - 4 * math.log2(17 / (4 * math.sqrt(2) * eps_sec))
    return ell, dict(D=D)


# ---------------------------------------------------------------- QCT V-A (this work)
def gw_deltas(Dq, c_phi=1.0):
    """Gisin-Wolf symmetric incoherent attack family. Given disturbance D and the
    overlap c_phi = <phi_up|phi_dn> of Eve's 'disturbed' probe states, the symmetry
    condition F = (1+c_phi)/(2-c_psi+c_phi) fixes c_psi. Eve's guessing probabilities
    for undisturbed / disturbed bits are 1/2 + 1/2*sqrt(1-c^2) (Helstrom, two pure states).
    Returns (delta0, delta1) or None if the pair is not realisable."""
    F = 1.0 - Dq
    if F <= 0.0:
        return None
    c_psi = 2.0 + c_phi - (1.0 + c_phi) / F
    if c_psi < -1.0 or c_psi > 1.0:
        return None
    d0 = 0.5 + 0.5 * math.sqrt(max(1.0 - c_psi * c_psi, 0.0))
    d1 = 0.5 + 0.5 * math.sqrt(max(1.0 - c_phi * c_phi, 0.0))
    return d0, d1


def gw_delta0(Dq):
    """AD-worst-case value of delta0 (c_phi = 1 maximises delta0 at fixed D)."""
    r = gw_deltas(Dq, 1.0)
    return 1.0 if r is None else r[0]


def majority_error(delta, b):
    """Error prob. of majority vote over b independent votes each correct w.p. delta
    (ties broken by coin flip)."""
    err = 0.0
    for k in range(b + 1):           # k = number of wrong votes
        pk = math.comb(b, k) * (1 - delta) ** k * delta ** (b - k)
        if 2 * k > b:
            err += pk
        elif 2 * k == b:
            err += 0.5 * pk
    return err


def tally_info(delta, b):
    """Exact mutual information (bits) between the distilled bit and the tally of b
    independent per-ancilla Helstrom votes, each correct w.p. delta. The tally k is a
    sufficient statistic; the majority vote is its MAP decision, so 1 - h(majority_error)
    is only a Fano LOWER bound on this quantity and must not be used as Eve's information."""
    HAK = 0.0
    for k in range(b + 1):           # k = number of votes for '0'
        l0 = math.comb(b, k) * delta ** k * (1 - delta) ** (b - k)
        l1 = math.comb(b, k) * (1 - delta) ** k * delta ** (b - k)
        pk = 0.5 * (l0 + l1)
        if pk > 0:
            HAK += pk * h2(l0 / (l0 + l1))
    return 1.0 - HAK


_CPHI_GRID = [i / 40.0 for i in range(-40, 41)]


def eve_info_distilled(Dq, b):
    """Worst case (over Eve's attack parameter c_phi) of Eve's information on the
    distilled bit of an accepted block, V-A model. Eve knows via Z1 whether the block
    was all-undisturbed (prob p_u) or all-disturbed; per-vote correctness delta0 / delta1.
    I_E = exact tally information (Shannon); p_guess = majority vote (MAP). Returns (I_E bits, p_guess, p_u).
    Gisin-Wolf separability: for D >= 1/4 the Alice-Bob state is separable and no key
    exists for any protocol -> I_E = 1."""
    if Dq >= 0.25:
        return 1.0, 1.0, 1.0
    pa = (1 - Dq) ** b + Dq ** b
    p_u = (1 - Dq) ** b / pa
    best_IE, best_pg = -1.0, 0.0            # worst case over c_phi, separately for each accounting
    for c_phi in _CPHI_GRID:
        r = gw_deltas(Dq, c_phi)
        if r is None:
            continue
        d0, d1 = r
        g0, g1 = majority_error(d0, b), majority_error(d1, b)
        IE = p_u * tally_info(d0, b) + (1 - p_u) * tally_info(d1, b)
        pg = p_u * (1 - g0) + (1 - p_u) * (1 - g1)
        best_IE, best_pg = max(best_IE, IE), max(best_pg, pg)
    return best_IE, best_pg, p_u


def helstrom_product(c, b):
    """Optimal success probability for discriminating two product states whose
    single-copy overlap is c (b copies): 1/2 + 1/2*sqrt(1 - c^(2b))."""
    return 0.5 + 0.5 * math.sqrt(max(0.0, 1.0 - abs(c) ** (2 * b)))


def eve_info_distilled_joint(Dq, b):
    """Within-block JOINT measurement (U1, within-block): Eve may apply any measurement to the
    b probes of a block before the parities are announced. The SDP of joint_block_sdp.py shows
    that the best non-adaptive joint measurement attains the adaptive Helstrom value, which in
    any case upper-bounds every within-block strategy. Worst case over the probe family
    parameter c_phi. Returns (I_E bits [Shannon, adaptive], p_guess, p_u)."""
    if Dq >= 0.25:
        return 1.0, 1.0, 1.0
    F = 1.0 - Dq
    pa = (1 - Dq) ** b + Dq ** b
    p_u = (1 - Dq) ** b / pa
    best_IE, best_pg = -1.0, 0.0            # worst case over c_phi, separately for each accounting
    for c_phi in _CPHI_GRID:
        c_psi = 2.0 + c_phi - (1.0 + c_phi) / F
        if c_psi < -1.0 or c_psi > 1.0:
            continue
        P0, P1 = helstrom_product(c_psi, b), helstrom_product(c_phi, b)
        IE = p_u * (1.0 - h2(1 - P0)) + (1 - p_u) * (1.0 - h2(1 - P1))
        pg = p_u * P0 + (1 - p_u) * P1
        best_IE, best_pg = max(best_IE, IE), max(best_pg, pg)
    return best_IE, best_pg, p_u


def _h2v(x):
    x = np.clip(np.asarray(x, dtype=float), 1e-300, 1 - 1e-16)
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)


def _tally_info_v(delta, b):
    """Vectorised tally_info over an array of per-vote correctness delta."""
    delta = np.asarray(delta, dtype=float)[..., None]
    k = np.arange(b + 1)[None, :]
    comb = np.array([math.comb(b, kk) for kk in range(b + 1)])[None, :]
    l0 = comb * delta ** k * (1 - delta) ** (b - k)
    l1 = comb * (1 - delta) ** k * delta ** (b - k)
    pk = 0.5 * (l0 + l1)
    post = np.where(pk > 0, l0 / np.maximum(l0 + l1, 1e-300), 0.5)
    return 1.0 - np.sum(pk * _h2v(post), axis=-1)


def _majority_error_v(delta, b):
    delta = np.asarray(delta, dtype=float)[..., None]
    k = np.arange(b + 1)[None, :]
    comb = np.array([math.comb(b, kk) for kk in range(b + 1)])[None, :]
    pk = comb * (1 - delta) ** k * delta ** (b - k)
    w = np.where(2 * k > b, 1.0, np.where(2 * k == b, 0.5, 0.0))
    return np.sum(pk * w, axis=-1)


def eve_info_bd(Dz, phiX, b, attack="joint", sup=True, ngrid=None):
    """General Bell-diagonal collective attack (after Pauli twirl) with Z-error Dz = phi_Z and
    X-error phiX, NOT assumed equal. Eve's purification: undisturbed probes psi_a with overlap
    c_psi = (l1 - l2)/(1 - Dz), disturbed probes phi_a with c_phi = (l3 - l4)/Dz, where
    (l1,l2,l3,l4) are the Bell weights, l3 + l4 = Dz, l2 + l4 = phiX. Eliminating l4 = Dz(1-c_phi)/2:
        c_psi = (1 - 2 phiX - Dz c_phi) / (1 - Dz),   feasibility: 0 <= l4 <= min(phiX, Dz), l1 >= 0.
    Worst case over c_phi, and (sup=True) over the true errors D' <= Dz, x' <= phiX: I_E is monotone
    in phiX but not in Dz, so a grid over D' in (0, Dz] is taken. attack='joint' uses Theorem 1,
    'individual' per-probe Helstrom + tally decoding. Returns (sup I_E, sup p_guess, p_u at Dz).
    Reduces to eve_info_distilled(_joint)(Dz, b) at phiX == Dz with sup=False."""
    if Dz <= 0:
        return 0.0, 0.5, 1.0
    if Dz >= 0.5:
        return 1.0, 1.0, 1.0
    if ngrid is None:
        ngrid = 33 if attack == "joint" else 9      # the tally sum makes the individual model 30x costlier
    Dgrid = np.linspace(Dz / ngrid, Dz, ngrid) if sup else np.array([Dz])
    cphi = np.array(_CPHI_GRID)
    D = Dgrid[:, None]; C = cphi[None, :]
    l4 = D * (1 - C) / 2
    feas = (l4 <= phiX + 1e-15) & (1 - D - phiX + l4 >= -1e-15)
    cpsi = np.clip((1 - 2 * phiX - D * C) / (1 - D), -1.0, 1.0)
    pa = (1 - D) ** b + D ** b
    pu = (1 - D) ** b / pa
    if attack == "joint":
        P0 = 0.5 + 0.5 * np.sqrt(np.maximum(0.0, 1 - np.abs(cpsi) ** (2 * b)))
        P1 = 0.5 + 0.5 * np.sqrt(np.maximum(0.0, 1 - np.abs(C) ** (2 * b)))
        IE = pu * (1 - _h2v(1 - P0)) + (1 - pu) * (1 - _h2v(1 - P1))
        pg = pu * P0 + (1 - pu) * P1
    else:
        d0 = 0.5 + 0.5 * np.sqrt(np.maximum(0.0, 1 - cpsi ** 2)); d1 = 0.5 + 0.5 * np.sqrt(np.maximum(0.0, 1 - C ** 2))
        d1 = np.broadcast_to(d1, d0.shape)
        IE = pu * _tally_info_v(d0, b) + (1 - pu) * _tally_info_v(d1, b)
        pg = pu * (1 - _majority_error_v(d0, b)) + (1 - pu) * (1 - _majority_error_v(d1, b))
    IE = np.where(feas, IE, -1.0); pg = np.where(feas, pg, 0.0)
    return float(IE.max()), float(pg.max()), float(pu[-1, 0])


def aep_penalty(S, eps):
    """Finite-size AEP correction (Tomamichel-Colbeck-Renner 2009) for binary C with
    H_min >= 0, H_max <= 1:  4*log2(eta)*sqrt(S*log2(2/eps^2)), eta <= 2+sqrt(2)."""
    eta = 2.0 + math.sqrt(2.0)
    log_term = 1.0 - 2.0 * math.log2(eps)          # = log2(2/eps^2), written to avoid underflow of eps^2
    return 4.0 * math.log2(eta) * math.sqrt(max(S, 0.0) * log_term)


def skl_qct_ad(N, P: Params, ch: Channel, b, eps_sec=1e-9, eps_cor=1e-15, f=1.2,
               entropy="shannon", stat="mcdiarmid", attack="individual", bell="symmetric",
               postsel=False, fano=False):
    """QCT V-A key length: same statistics as T25, Eve's EUR term 1-h(Phi_X) replaced by
    the classical incoherent-attack information bound evaluated at phi_Z^+.
    entropy='shannon' uses H(C|Z) with AEP penalty; 'minent' uses -log2 P_guess (no AEP)."""
    # postsel=True charges the post-selection factor (N+1)^15 of CKR09 to the secrecy parameter used in
    # the i.i.d. analysis (AEP smoothing and leftover hash), as required for the coherent-attack extension.
    eps_iid = eps_sec / (N + 1) ** 15 if postsel else eps_sec
    eps_bar = eps_sec ** 2 / 368.0
    D = decoy_bounds(N, P, ch, eps_bar)
    if _degenerate(D) or D["phiZ_plus"] >= 0.25:
        return -math.inf, dict(D=D)
    S_minus, _, _ = ad_block_bounds(D, b, eps_bar, stat)
    NK, PhiK, _ = distilled_stats(D["phiK"], D["nK"], b)
    lam_IR = f * NK * h2(PhiK)
    if bell == "general":            # Bell-diagonal attack with phi_X != phi_Z (Appendix B)
        IE, pg, p_u = eve_info_bd(D["phiZ_plus"], D["phiX_plus"], b, attack)
    elif attack == "joint":
        IE, pg, p_u = eve_info_distilled_joint(D["phiZ_plus"], b)
    else:
        IE, pg, p_u = eve_info_distilled(D["phiZ_plus"], b)
    if fano and attack == "individual":   # superseded Fano/majority-vote accounting, kept for the comparison file only
        Dz = D["phiZ_plus"]; pa = (1 - Dz) ** b + Dz ** b; pu = (1 - Dz) ** b / pa
        best = -1.0
        for c_phi in _CPHI_GRID:
            r = gw_deltas(Dz, c_phi)
            if r is None: continue
            d0, d1 = r
            best = max(best, pu * (1 - h2(majority_error(d0, b))) + (1 - pu) * (1 - h2(majority_error(d1, b))))
        IE = best
    eps_aep = eps_iid / 4.0
    if entropy == "shannon":
        H = S_minus * (1 - IE) - aep_penalty(S_minus, eps_aep)
    else:
        H = S_minus * (-math.log2(pg))
    ell = H - lam_IR - math.log2(2 / eps_cor) \
        - 4 * math.log2(2 ** (7 / 4) / (eps_iid - eps_iid ** 2 / 8))
    return ell, dict(D=D, S_minus=S_minus, NK=NK, PhiK=PhiK, lam_IR=lam_IR, IE=IE, pg=pg, p_u=p_u)


# ---------------------------------------------------------------- optimisation
def _sig(t):
    t = min(max(float(t), -60.0), 60.0)
    return 1.0 / (1.0 + math.exp(-t))


def _unpack(x, with_qT):
    mu1 = 0.05 + 1.5 * _sig(x[0])
    mu2 = mu1 * (0.02 + 0.9 * _sig(x[1]))
    a = np.exp(np.clip(np.array([x[2], x[3], 0.0]), -60, 60))
    a = a / a.sum()
    pZ = 0.5 + 0.49 * _sig(x[4])
    qT = (0.001 + 0.5 * _sig(x[5])) if with_qT else 0.0
    return Params(mu1, mu2, 0.0, float(a[0]), float(a[1]), pZ, qT)


def optimise(fun, N, ch, b=None, x0=None, restarts=((0, 0, 1.5, 0.5, 1.5, -1.0), (0.5, -0.5, 2.0, 1.0, 2.5, -2.0), (-0.5, 0.5, 1.0, 0.0, 1.0, 0.0))):
    """Nelder-Mead over the 6 (or 5) free parameters; returns (best_ell, Params)."""
    with_qT = b is not None
    best = (-math.inf, None)
    starts = list(restarts) + ([tuple(x0)] if x0 is not None else [])
    for s in starts:
        def obj(x):
            P = _unpack(x, with_qT)
            if not P.valid():
                return 1e30
            try:
                ell = fun(N, P, ch, b)[0] if with_qT else fun(N, P, ch)[0]
            except (ValueError, ZeroDivisionError, OverflowError):
                return 1e30
            if not math.isfinite(ell):
                return 1e30
            return -ell / N
        r = minimize(obj, np.array(s, dtype=float), method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-4, fatol=1e-14, adaptive=True))
        if -r.fun * N > best[0]:
            best = (-r.fun * N, _unpack(r.x, with_qT), r.x)
    return best


def qber_of(P: Params, ch: Channel):
    """Sifted-key QBER phi_K = m_K/n_K (signal+decoy intensities)."""
    num = den = 0.0
    for mu, pmu in ((P.mu1, P.p_mu1), (P.mu2, P.p_mu2)):
        po, pe = click_probs(mu, ch)
        num += pmu * pe
        den += pmu * po
    return num / den


def threshold_qber(fun, N, b=None, eta=1.0, p_noise=0.0, lo_deg=0.0, hi_deg=35.0, tol_deg=0.05):
    """Largest misalignment angle (hence QBER) with positive key, by bisection with
    parameter re-optimisation at every point. Returns (qber, delta_deg, Params)."""
    x0 = None
    bestP = None

    def positive(deg):
        nonlocal x0, bestP
        ch = Channel(eta, p_noise, math.radians(deg))
        ell, P, x = optimise(fun, N, ch, b, x0)
        if ell > 0:
            x0, bestP = x, (P, ch)
        return ell > 0

    if not positive(lo_deg):
        return 0.0, 0.0, None
    while hi_deg - lo_deg > tol_deg:
        mid = 0.5 * (lo_deg + hi_deg)
        if positive(mid):
            lo_deg = mid
        else:
            hi_deg = mid
    P, ch = bestP
    return qber_of(P, ch), lo_deg, P
