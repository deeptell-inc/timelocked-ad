# timelocked-ad

Code, data and manuscript source for

> H. Wakaura, *Does hiding the post-processing from a memory-limited eavesdropper raise the noise tolerance of QKD? Timelocked advantage distillation and the 20% barrier* (2026).

The paper asks what a quantum computational timelock on the post-processing announcements of decoy-state BB84 with advantage distillation can buy, treating the parities, the block partition and the bases separately. Theorem 1 shows that hiding the parities does not change the adversary's guessing probability; the finite-key thresholds are computed for Bell-diagonal collective attacks in two entropy accountings.

## Layout

| Path | Content |
|---|---|
| `manuscript.md` | Markdown source of the paper (current version; `manuscript-vX.Y.Z.md` are snapshots) |
| `paper/` | `md2tex.py` (Markdown → REVTeX converter), figures, `main.pdf` |
| `impl/qct_ad/` | Deterministic Python implementation (`skl.py` core, reproduction and SDP scripts, `tests/`) |
| `data/` | Every CSV and log that the printed numbers trace to (`data-manifest.md` maps numbers to files) |
| `preprint-bundle/`, `submission-bundle/` | arXiv and journal submission packages |
| `panel/`, `manuscript-REVIEW.md`, `adversarial-review-log.md`, `claims-ledger.md` | Adversarial panel-review records and the claims ledger |

## Reproduction

```
cd impl/qct_ad
python3 -m pytest tests -q
python3 reproduce.py          # ~11 min, symmetric family thresholds
python3 bd_thresholds.py      # ~45 min, Bell-diagonal thresholds (Table I)
python3 joint_block_sdp.py; python3 joint_block_theorem.py     # Table II, Theorem 1 check
python3 perprobe_opt.py; python3 hidden_partition_sdp.py       # Sec. III, Table IV
python3 panel_variants.py; python3 panel_variants2.py          # Table III and sensitivity rows
python3 asymptotic_mp.py; python3 make_figures.py              # asymptotics (60-digit) and figures
```

Requirements: numpy, scipy, matplotlib, mpmath; cvxpy (CLARABEL/SCS) for the SDP scripts.

## Citation

See `CITATION.cff`; cite the tagged release (v2.1).

## License

Code: MIT (`LICENSE`). Data, figures and manuscript: CC BY 4.0 (`LICENSE-DATA`).
