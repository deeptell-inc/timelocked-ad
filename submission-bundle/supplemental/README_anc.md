Title: timelocked-ad code and data
Description: Deterministic Python code, result files and Markdown source behind every table and figure of the manuscript; run tests/test_skl.py and reproduce.py to regenerate the thresholds.

# Preprint bundle (S11) — arXiv quant-ph

Generated 2026-10-09 from manuscript.md v1.1.0 via `anc/code/md2tex.py` (revtex4-2).

## Contents
- `main.tex` — the manuscript (revtex4-2, two-column, 10 pages, bibliography inline as `thebibliography`). Compiles with pdflatex alone; no .bib needed.
- `figures/fig2_eve_info.pdf`, `fig3_rate_vs_qber.pdf`, `fig4_threshold_vs_b.pdf` — Figures 1–3 of the paper (file names keep the internal numbering; captions and references are consistent).
- `anc/` — ancillary files (arXiv keeps the `anc/` directory of the source tarball as downloadable supplementary material):
  - `anc/code/` — deterministic Python implementation (`skl.py` core; `reproduce.py`, `bd_thresholds.py`, `joint_thresholds.py`, `scan.py`, `asymptotic.py`, `joint_block_sdp.py`, `joint_block_theorem.py`, `joint_block_ansatz.py`, `joint_block_quad_search.py`, `hidden_basis_sdp.py`, `sixstate_*.py`, `make_figures.py`; `tests/test_skl.py`, 7 tests). Requirements: numpy, scipy, matplotlib, cvxpy (CLARABEL/SCS) for the SDP scripts.
  - `anc/data/` — every CSV and log the printed numbers trace to (see `anc/manuscript.md` and the verification below).
  - `anc/manuscript.md` — Markdown source of the paper.
- `arxiv-src.tar.gz` — what to upload to arXiv (`main.tex`, `figures/`, `anc/`).

## Pre-upload checklist (status)
- [x] Compiles standalone with pdflatex (2 passes), no undefined references/citations, no overfull boxes > 30 pt.
- [x] Submission hygiene (CLAUDE.md rule): no "corrected / earlier revision / previously reported / referee / conjectur*" in `main.tex`.
- [x] Every printed number traced to a file in `anc/data/` (S17 gate, `claims-ledger.md` v1.3): Tables I–IV, T25 reproduction, asymptotic and finite-key thresholds, six-state and hidden-basis values, Theorem 1 verification log.
- [x] Abstract 1773 characters (< arXiv limit 1920).
- [ ] **Author name(s) and affiliation(s)**: `\author{Author}` / `\affiliation{Affiliation}` are placeholders — must be filled before upload.
- [ ] arXiv metadata (see `arxiv-metadata.txt`): title, abstract (plain text), primary category quant-ph, comments, license (arXiv non-exclusive licence recommended for later PRA submission).
- [ ] Optional: ORCID, funding acknowledgement, data/code statement (currently "ancillary files").

## Reproduction
```
cd anc/code
python3 -m pytest tests -q
python3 reproduce.py          # ~11 min, data/threshold_table.csv (symmetric family)
python3 bd_thresholds.py      # ~45 min, data/bd_thresholds.csv (Table I)
python3 joint_thresholds.py   # ~15 min
python3 asymptotic.py; python3 joint_block_sdp.py; python3 joint_block_theorem.py
python3 scan.py; python3 make_figures.py
```
