"""Figures from data/*.csv (one message per figure). Output: paper/figures/*.pdf,png"""
import os, csv, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = os.path.join(os.path.dirname(__file__), "..", "..")
data = os.path.join(root, "data")
figdir = os.path.join(root, "paper", "figures")
os.makedirs(figdir, exist_ok=True)


def read(name):
    with open(os.path.join(data, name)) as fh:
        return list(csv.DictReader(fh))


# Fig 2: Eve's information on the distilled bit vs QBER, several b (V-A worst case)
import sys
sys.path.insert(0, os.path.dirname(__file__))
from skl import eve_info_distilled, eve_info_distilled_joint, h2
fig, ax = plt.subplots(figsize=(4.2, 3.2))
Ds = [i / 400 for i in range(1, 100)]
for b in (1, 3, 5, 9, 15):
    ax.plot([100 * D for D in Ds], [1 - eve_info_distilled(D, b)[0] for D in Ds], label=f"b={b}")
    col = ax.lines[-1].get_color()
    ax.plot([100 * D for D in Ds], [1 - eve_info_distilled_joint(D, b)[0] for D in Ds], ls="-.", color=col, alpha=0.9)
    pa = lambda D: (1 - D) ** b + D ** b
    ax.plot([100 * D for D in Ds], [1 - h2(min(max(0.5 * ((1 - D) ** b - (1 - 3 * D) ** b) / pa(D), 0), 0.5)) for D in Ds],
            ls="--", color=col, alpha=0.6)
ax.set_xlabel("QBER (%)"); ax.set_ylabel(r"$1-I_E$ per distilled bit (bits)")
ax.set_yscale("log"); ax.set_ylim(1e-4, 1); ax.axvline(25, color="k", lw=0.8, ls=":"); ax.axvline(20, color="k", lw=0.8, ls="-.")
ax.legend(fontsize=6, ncol=2); ax.set_title("solid: per-probe H; dash-dot: joint block; dashed: EUR (T25)", fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(figdir, "fig2_eve_info.pdf")); fig.savefig(os.path.join(figdir, "fig2_eve_info.png"), dpi=200)

# Fig 3: key rate vs QBER
if os.path.exists(os.path.join(data, "rate_curves.csv")):
    rows = read("rate_curves.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2), sharey=True)
    for ax, N in zip(axes, ("100000000.0", "100000000000000.0")):
        for model, ls in (("AD_T25_eq93", "--"), ("QCT_VA_minent", "-"), ("QCT_VA_shannon", ":")):
            for b in ("1", "3", "5", "9"):
                pts = [(100 * float(r["qber"]), float(r["rate"])) for r in rows if r["N"] == N and r["b"] == b and r["model"] == model and float(r["rate"]) > 0]
                if pts:
                    ax.plot(*zip(*sorted(pts)), ls=ls, label=f"{model.replace('AD_T25_eq93','AD (T25)').replace('QCT_VA_minent','per-probe H, min-ent').replace('QCT_VA_shannon','per-probe H, Shannon')} b={b}")
        pts = [(100 * float(r["qber"]), float(r["rate"])) for r in rows if r["N"] == N and r["model"] == "BB84_T25_eq94" and float(r["rate"]) > 0]
        if pts:
            ax.plot(*zip(*sorted(pts)), color="k", lw=0.8, label="BB84 (no AD)")
        ax.set_yscale("log"); ax.set_ylim(1e-8, 1); ax.set_xlabel("QBER (%)"); ax.set_title(f"N = 1e{int(math.log10(float(N)))}", fontsize=9)
        ax.axvline(17.3, color="gray", lw=0.6, ls=":"); ax.axvline(25, color="k", lw=0.6, ls=":")
    axes[0].set_ylabel(r"secure key rate $\ell/N$"); axes[1].legend(fontsize=5, ncol=2)
    fig.tight_layout(); fig.savefig(os.path.join(figdir, "fig3_rate_vs_qber.pdf")); fig.savefig(os.path.join(figdir, "fig3_rate_vs_qber.png"), dpi=200)

# Fig 4: thresholds vs b (asymptotic + finite)
rows = read("asymptotic_thresholds.csv")
fig, ax = plt.subplots(figsize=(4.2, 3.2))
for f, mk in (("1.2", "o"), ("1.0", "s")):
    rr = [r for r in rows if r["f"] == f]
    ax.plot([int(r["b"]) for r in rr], [100 * float(r["thr_QCT_VA"]) for r in rr], marker=mk, label=f"per-probe H, f={f}")
    ax.plot([int(r["b"]) for r in rr], [100 * float(r["thr_EUR_T25"]) for r in rr], marker=mk, ls="--", label=f"EUR (T25), f={f}")
if os.path.exists(os.path.join(data, "threshold_table.csv")):
    tt = read("threshold_table.csv")
    for model, mk in (("QCT_VA_minent", "^"), ("AD_T25_eq93", "v")):
        rr = [r for r in tt if r["N"] == "100000000000000.0" and r["model"] == model]
        ax.scatter([int(r["b"]) for r in rr], [100 * float(r["qber_thr"]) for r in rr], marker=mk, s=18, label=f"{model.replace('QCT_VA_minent','per-probe H, min-ent').replace('AD_T25_eq93','AD (T25)')}, finite N=1e14")
jt = os.path.join(data, "joint_thresholds.csv")
if not os.path.exists(jt):
    jt = os.path.join(data, "joint_thresholds_quick.csv")
if os.path.exists(jt):
    jr = [r for r in read(jt) if r["kind"] == "asymptotic" and r["f"] == "1.2" ]
    ax.plot([int(r["b"]) for r in jr], [100 * float(r["thr_joint_shannon"]) for r in jr], marker="D", color="k", lw=1.2,
            label="joint block measurement, f=1.2")
    jf = [r for r in read(jt) if r["kind"] == "finite" and r["N"] == "100000000000000.0"]
    if jf:
        ax.scatter([int(r["b"]) for r in jf], [100 * float(r["thr_joint_minent"]) for r in jf], marker="x", color="k", s=22,
                   label="joint, finite N=1e14 (min-ent)")
ax.axhline(25, color="k", lw=0.8, ls=":"); ax.axhline(20, color="k", lw=0.8, ls="-."); ax.axhline(27.6, color="gray", lw=0.6, ls=":")
ax.set_xlabel("AD block size b"); ax.set_ylabel("threshold QBER (%)"); ax.set_xscale("log"); ax.legend(fontsize=5)
fig.tight_layout(); fig.savefig(os.path.join(figdir, "fig4_threshold_vs_b.pdf")); fig.savefig(os.path.join(figdir, "fig4_threshold_vs_b.png"), dpi=200)
print("figures written to", figdir)
