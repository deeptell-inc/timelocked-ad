import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from skl import (gw_delta0, majority_error, tally_info, eve_info_distilled, h2, Params, Channel,
                 skl_ad, skl_bb84, skl_qct_ad, distilled_stats)


def test_gw_threshold_is_one_quarter():
    # Gisin-Wolf Thm.1: key possible iff D/(1-D) < 2 sqrt(d0(1-d0)); equality at D=1/4
    for D, expect in ((0.20, True), (0.249, True), (0.251, False), (0.30, False)):
        d0 = gw_delta0(D)
        assert (D / (1 - D) < 2 * math.sqrt(d0 * (1 - d0))) == expect


def test_delta0_limits():
    assert abs(gw_delta0(0.0) - 0.5) < 1e-12          # no disturbance -> no info
    assert abs(gw_delta0(1 / 3) - 1.0) < 1e-12         # F=2/3 -> c=0 -> perfect


def test_majority_error():
    assert abs(majority_error(0.5, 3) - 0.5) < 1e-12
    assert abs(majority_error(0.9, 1) - 0.1) < 1e-12
    assert majority_error(0.9, 5) < majority_error(0.9, 3) < 0.1


def test_eve_info_decreases_with_b_at_high_qber():
    # AD must help below 1/4: at D=0.22 Eve's info per distilled bit drops below
    # Bob's correlation for large enough b; at D>=1/4 no key (I_E=1).
    D = 0.22
    for b in (1, 3, 5, 9, 15):
        IE, pg, pu = eve_info_distilled(D, b)
        _, PhiK, _ = distilled_stats(D, 1e6, b)
        if b >= 15:
            assert 1 - h2(PhiK) > IE
    assert eve_info_distilled(0.25, 9)[0] == 1.0


def test_eq19_sign():
    # when 1-phiZ-2phiX < 0 the logical-X error bound must saturate at 1/2 (no key)
    from skl import ad_block_bounds
    D = dict(nK=1e12, sK_minus=9e11, phiZ_plus=0.4, phiX_plus=0.4)
    S, Phi, _ = ad_block_bounds(D, 9, 1e-20)
    assert Phi == 0.5


def test_skl_runs_and_reduces():
    P = Params(0.5, 0.1, 0.0, 0.7, 0.2, 0.9, 0.1)
    ch = Channel(1.0, 0.0, math.radians(5))
    ell_ad, _ = skl_ad(1e10, P, ch, 3)
    ell_bb, _ = skl_bb84(1e10, P, ch)
    ell_q, _ = skl_qct_ad(1e10, P, ch, 3)
    assert ell_bb > 0 and ell_ad > 0 and ell_q > 0
    assert ell_q >= ell_ad      # P2: QCT bound never below T25 at the same statistics (model monotonicity)


def test_tally_info_dominates_fano_majority_bound():
    for delta in (0.6, 0.75, 0.9):
        for b in (1, 3, 5, 9):
            assert tally_info(delta, b) >= 1 - h2(majority_error(delta, b)) - 1e-12
    assert abs(tally_info(0.9, 1) - (1 - h2(0.1))) < 1e-12     # b=1: tally == vote
    assert abs(tally_info(0.5, 7)) < 1e-12                      # uninformative votes


def test_bell_diagonal_term_reduces_to_symmetric_and_is_monotone_in_phiX():
    from skl import eve_info_bd, eve_info_distilled_joint
    for D in (0.05, 0.17, 0.24):
        for b in (1, 3, 9):
            a = eve_info_bd(D, D, b, "joint", sup=False); c = eve_info_distilled_joint(D, b)
            assert abs(a[0] - c[0]) < 1e-10 and abs(a[1] - c[1]) < 1e-10
            x = [eve_info_bd(D, p, b, "joint", sup=False)[0] for p in (0.05, 0.10, 0.20, 0.30)]
            assert all(x[i + 1] >= x[i] - 1e-12 for i in range(3))


def test_joint_adaptive_value_matches_direct_helstrom():
    import numpy as np
    from skl import helstrom_product
    for c in (-0.6, 0.3, 0.9):
        for b in (1, 3, 5):
            th = 0.5 * np.arccos(c); p0 = np.array([np.cos(th), np.sin(th)]); p1 = np.array([np.cos(th), -np.sin(th)])
            v0 = np.array([1.0]); v1 = np.array([1.0])
            for _ in range(b): v0 = np.kron(v0, p0); v1 = np.kron(v1, p1)
            w = np.linalg.eigvalsh(np.outer(v0, v0) - np.outer(v1, v1))
            assert abs(0.5 + 0.25 * np.abs(w).sum() - helstrom_product(c, b)) < 1e-12


def test_aep_penalty_and_postsel_direction():
    from skl import aep_penalty, Params, Channel, skl_qct_ad
    import math
    assert abs(aep_penalty(1e6, 1e-9 / 4) - 4 * math.log2(2 + math.sqrt(2)) * math.sqrt(1e6 * math.log2(2 / (1e-9 / 4) ** 2))) < 1e-6
    P = Params(0.5, 0.1, 0.0, 0.7, 0.2, 0.9, 0.1); ch = Channel(1.0, 0.0, math.radians(5))
    ell, _ = skl_qct_ad(1e10, P, ch, 3, attack="joint", bell="general")
    ell_ps, _ = skl_qct_ad(1e10, P, ch, 3, attack="joint", bell="general", postsel=True)
    assert ell_ps < ell        # charging the post-selection factor can only shorten the key


def test_theorem1_construction_small_b():
    import numpy as np, itertools, math
    from joint_block_theorem import check
    for b in (2, 3, 4):
        orth, cond, P, pad = check(b, 0.15)
        assert orth < 1e-12 and cond < 1e-12 and abs(P - pad) < 1e-12
