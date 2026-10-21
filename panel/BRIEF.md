# Panel brief (self-contained; the panellist cannot see the conversation)

## Target
- Manuscript: /Users/deeptell01/Documents/alterego/personal/qcrypt/manuscript.md (v1.3.0, Markdown source; the compiled PDF is paper/main.pdf, LaTeX paper/main.tex). Title: "Does hiding the post-processing from a memory-limited eavesdropper raise the noise tolerance of QKD? Timelocked advantage distillation and the 20% barrier". Single author. Target venue: Physical Review A (Regular Article); the review standard requested is Nature/PRX-level.
- Code: /Users/deeptell01/Documents/alterego/personal/qcrypt/impl/qct_ad/ (deterministic Python; `skl.py` core; `tests/test_skl.py`; drivers `reproduce.py [quick]`, `bd_thresholds.py [quick]`, `joint_thresholds.py [quick]`, `asymptotic.py`, `joint_block_sdp.py`, `joint_block_theorem.py`, `joint_block_ansatz.py`, `hidden_basis_sdp.py`, `sixstate_mixed_lb.py`, `sixstate_b3_lb.py`, `scan.py`, `make_figures.py`). Requirements: numpy, scipy, cvxpy (CLARABEL/SCS), matplotlib. `quick` modes run in minutes; full runs take 10–45 min each (do NOT run full `scan.py`/`reproduce.py`/`bd_thresholds.py`; use `quick`).
- Data every printed number traces to: /Users/deeptell01/Documents/alterego/personal/qcrypt/data/ (CSV + logs). Mapping of numbers to files: claims-ledger.md and fact-check-report.md in the project root; impl-report.md and data-manifest.md describe the pipeline.
- Primary sources (full text, Markdown with page breaks "---" = page boundaries) in /Users/deeptell01/research/notes/: Bae–Acín 2007 `arxivquant-ph0610048v1-9-oct-2006.md`; Acín et al. 2006 `arxivquant-ph0411092v1-12-nov-2004.md`; Gisin–Wolf 1999 `arxivquant-ph9902048v1-11-feb-1999.md`; Treplin–Kleinpaß–Orsucci 2025 (T25) `finite-size-analysis-of-decoy-state-bb84.md`; Bocquet–Alléaume–Leverrier `optimal-eavesdropping-on-qkd-without-quantum-memory.md`; Tomamichel–Colbeck–Renner 2009 `arxiv08111221v3-quant-ph-12-may-2009.md`; Vyas–Alléaume 2020 `everlasting-secure-key-agreement-with-performance-beyond-qkd.md`; Novak 2025 `security-of-quantum-key-distribution-with-one-time-pad-protected-error-correctio.md`; Pastushenko–Kronberg 2023 `arxiv230612347v1-quant-ph-21-jun-2023.md`; Fuchs thesis 1996 `arxivquant-ph9601020v1-23-jan-1996.md`.

## What the paper claims (so you can attack it)
1. Model: quantum computational timelock (Vyas–Alléaume): adversary must measure her probes before the AD parities / syndrome are announced. Two adversary classes: individual (per-probe) and joint (whole AD block measured jointly, non-adaptively).
2. Theorem 1 (Appendix A): for the parity-conditioned discrimination problem the best non-adaptive joint measurement attains the adaptive Helstrom value ½+½√(1−c^{2b}) for every block size b, via the explicit basis {X^{ỹ} Z^{(0,Ly′)} g±} with L the prefix-XOR map. Hence hiding the parities buys nothing; asymptote 20% (BB84), finite-key thresholds return to 17.3–18.4% (Table I), vs 17.3% unconditional (T25).
3. Per-probe adversary would concede 20.7–20.8% (b=9) with 25% asymptote (the Bae–Acín individual-attack remark), reported as reference point.
4. Hiding the basis as well (six-state) does not compound with AD (numerics b≤3).
5. Finite-key formula = T25 Eq. (93) with the EUR term replaced by an AEP/min-entropy term; adversary term maximised over all Bell-diagonal collective attacks (Appendix C.4); reduction to coherent attacks sketched (Appendix B).
6. By-products: T25 Eq. (19) domain φ_X+φ_Z<1/2; the Fano/majority-vote expression underestimates a per-probe adversary (tally information instead).

## Five axes (score each /10)
新規性 (novelty vs Bae–Acín 2007, Acín et al. 2006, BAL11, T25), データ分量 (amount of evidence: tables, SDP, theorem verification, six-state numerics), データ質 (correctness and reproducibility of numbers; separate "reproducibility" = numbers match files from "soundness" = the computed quantity is the right one), ストーリー (framing, honesty of negative result, abstract/intro/conclusion alignment), 論理展開 (proof of Theorem 1, Appendix B/C, monotonicity/supremum argument, composability claims).

## Output (STRICT format; write to the file named in your task; also return it)
```markdown
# 総合スコア（Nature 級査読者ペルソナ採点）
| 評価軸 | スコア | コメント（長所／問題を深刻度順に） |
|---|---|---|
| **新規性** | <0-10>/10 | … |
| **データ分量** | <0-10>/10 | … |
| **データ質** | <0-10>/10 | … |
| **ストーリー** | <0-10>/10 | … |
| **論理展開** | <0-10>/10 | … |
| **総合** | <0-10>/10 | 総評 |

推奨: <ACCEPT / MINOR_REVISION / MAJOR_REVISION / REJECT>
```
Then: `## 長所` (list) and `## 問題（深刻度順）` — each item: location (section/equation), the problem, **確度 0–100**, and a **具体的な反証条件** (what observation/computation would show the criticism wrong). Separate facts (what you checked) from inferences. Do not invent citations; if you cite a source, give the page/section from the files above. Do not modify any project file. Write in Japanese (quotes from the manuscript may stay in English).
