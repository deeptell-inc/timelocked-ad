---
asset: progress
version: 0.3.0
生成元入力: research-methodology 起動（T2 再定式化版）
依存工程: なし
生成日: 2026-10-08
---

# 進捗台帳 — T2: QCT 仮定下の PQC 暗号化 AD 付き decoy-BB84 有限鍵率 ＋ FPGA

## 冒頭宣言
- 認識した起点: P4（ゴール＋仕様/課題）。ゴール = 再定式化 T2。仕様 = T2_prior_art.md §5（QCT 仮定、Treplin 2025 を出発点、Jiang 2021 の仮想 IID、Tomamichel–Leverrier 枠組み、FPGA 10⁸ ビット PA）。
- 開始工程: S2（理論素材の一次確認）→ S3★ → S4（簡略計画）→ S5 優先。
- 想定成果物: source-notes.md → theory-foundation.md → theme-brief.md → impl/ + impl-report.md
- ワークスペース: /Users/deeptell01/Documents/alterego/personal/qcrypt/
- 再開/新規: 新規（progress.md なし）。先行調査 T2_prior_art.md と 5×5 レポートは S1 相当の既存成果物として扱う。

## 工程状態
| 工程 | 状態 | 成果物 | 備考 |
|---|---|---|---|
| S1 | 完了（代替） | qcrypt_5x5_analysis.md, T2_prior_art.md | 学術API＋Web検索 |
| S2 | 完了 | source-notes.md v1.1.0 | 一次 6 件（全文/PDF）＋外部 4 件（抄録）。DoD: 全文献ノート有/主張・手法・数値・含意有/claim 候補有 = OK |
| S3★ | 完了 | theory-foundation.md v1.0.0 | S16: 批判レビュー1周（下記）。S17: 19 claim、SUPPORTED 10 / PARTIALLY 9、差し戻しなし。DoD: 依拠/拡張明示・命題 P1–P5・仮定冒頭明記・S17 通過 = OK |
| S4 | 完了 | theme-brief.md v1.0.0 | P4 簡略計画。DoD: 問い1文・新規性3件（2経路予定）・逆算計画 = OK |
| S5 | 完了 | impl/qct_ad/, impl-report.md v0.3.0 | T25 4閾値を再現。QCT V-A: N=10¹⁴ b=9 で 20.7–21.9%、最大 21.8%（b=15, min-ent）。Eq.19 適用領域の制約を実装。DoD: 再現手順・命題結果・主要数値の claim 化 = OK |
| S6 | 完了 | data/, data-manifest.md v0.2.0 | 全 6 CSV ＋ 3 図（paper/figures）。DoD: 台帳に生成元・列・状態 = OK |
| S7★ | 完了（v0.2.0） | manuscript.md v0.2.0, paper/main.tex | S16 1周（4 指摘対応）、S17（34 claim、差し戻しなし）、H4 整合済。revtex4-2 で組版 |
| S9★ | 完了 | gap-report.md v1.0.0 | 12 項目、重 1（U1 限定表現で対応）。S17: Fung 2012 追加・新規性 3 を SUPPORTED |
| S8 | 完了 | outline.md v1.0.0, logic-map.md v1.0.0 | H4 引用整合は S7 完了時に再実施 |
| S18 | 完了 | manuscript-REVIEW.md v1.0.0, adversarial-review-log.md v1.0.0, reference-adequacy.md v1.0.0, manuscript.md v0.9.0（v0.5.0/v0.7.0 スナップショット） | 総合 5/10 MAJOR_REVISION → 重大 2 件（Bae–Acín/Acín 未引用、Fano 下界の誤用）＋敵対 2 セット（計 20 指摘）対応、収束。S17 9 行追記、S16 1 周（PDF 校正）。参照 31 件で充足 |
| S10 | 完了 | venue-decision.md v1.0.0 | PRA Regular Article に決定、arXiv 先行公開（S11）→ PRA 投稿（S12）。承認待ち |

## S5 追記（2026-10-08）
- T25 Eq. 19 の非単調性を発見し、φ_Z∈[0,φ⁺_Z] 最大化で修正。全 b スキャンと鍵率曲線を再実行中（修正前の threshold_table.csv/rate_curves.csv は無効）。

## S16 レビュー記録（theory-foundation.md v1.0.0）
- 指摘 1（論理）: 当初草案は「PQC 暗号化で鍵率向上」と書いていたが、Novak 2025 と矛盾 → 利得の出所を A1/A2（Eve の非適応化）に限定し、PQC を「遅延圧縮」と再定義（拡張 1）。
- 指摘 2（過剰主張）: 「合成可能」を無条件に書いていた → 「QCT モデル内」と限定（拡張 3）。
- 指摘 3（曖昧）: Eve の測定クラスが不明確 → A4 で結合・非適応測定を許す一方、P1 は i.i.d. 個別攻撃に限定し、一般化を U1 として明示。
- 指摘 4（事実）: 25%/14.6% の数値は本文未確認 → S17 で PARTIALLY、本文で「未確認」と明記。

## 生成ログ（MANIFEST 代替: ~/methodology は読み取り専用のためワークスペース側に記録）
| 日付 | 成果物 | version | 生成元入力 |
|---|---|---|---|
| 2026-10-08 | progress.md | 0.1.0 | research-methodology 起動 |
| 2026-10-08 | source-notes.md | 1.1.0 | T2_prior_art.md ＋ hyperresearch 取得一次源 |
| 2026-10-08 | theory-foundation.md | 1.0.0 | source-notes.md v1.1.0 |
| 2026-10-08 | claims-ledger.md | 1.0.0 | S17（S3 ゲート） |

## S15 → S3 差し戻し（2026-10-08, U1 拡張）
- 結合測定 SDP により P1 が個別測定仮定に依存すると判明。reexamination.md v1.0.0 → theory-foundation.md v1.1.0（P1′ 崩壊定理）。
- 下流再生成: impl-report v0.4.0（§3d）、manuscript v0.3.0（題名・要旨・§3・§5・§7 改訂、負の結果として再構成）、ledger 4 行追加。
- joint_thresholds.py 完了（表 1 の結合列を確定、図 2・4 更新）。joint_block_sdp.py の b=4 は実行中（b=2,3 は確定）。
- 結論: 結合測定下では有限鍵最良 18.4%（Shannon, b=7）/17.7%（min-ent, b=11）vs T25 17.3%；漸近 20% 限界。主張は負の結果に再構成（manuscript v0.3.0）。

## P1″ 検証（2026-10-09）
- hidden_basis_sdp.py: BB84 では最悪攻撃 c_φ=1 で利得なし（b=1,2）。六状態では b=1 で基底隠蔽が有効（一方向閾値 16.7%→22.7%, f=1）。
- 実行中: 六状態 b=2 同一基底の検証（SCS/Clarabel）、混合ブロックの基底隠蔽上界、BB84 b=4 SDP。
- theory-foundation v1.2（J4–J8）、ledger 7 行追加。判定: **P1″ 否定**。六状態 b=2 混合ブロックで P=0.8878 vs 0.8886（D=0.167）。結合測定モデルは Chau の 27.6%/20% を再現（J8）。先行 BAL11（arXiv:1106.0329）が b=1 を既に解決済み。
- 原稿 v0.4: §3 に基底隠蔽の段落、§7/§8 を改訂。

## 次工程
- S11 プレプリントバンドル（arXiv quant-ph; paper/main.tex v0.9.0 組版済 8 頁、図 3 点、paper/md2tex.py、データ・コード参照）— **実行前にユーザー承認が必要**（S17 ゲート付き）
- S12 PRA 投稿バンドル — ユーザー承認が必要
- 2026-10-09 残課題の処理（S15→S3）: Conjecture 1 → **定理 1 として証明**（manuscript v1.0.0 Appendix A, theory-foundation v1.3 J9）；集団攻撃への帰着 → Appendix B（証明スケッチ、φ_X≠φ_Z の再最大化は未実施）；六状態大 b → b=3 の達成可能下界を追加（誤り率比 1.5→≤1.05→≤1.04 at D=0.167）、指数の同一性は未証明と明記
- S13 パッケージ化（impl/qct_ad → pyproject、tests、README）
- 未解決 U1（結合測定の厳密界）は本論文の範囲外として明記済

## 保留中の承認
- S11/S12（プレプリント/本投稿）の実行はユーザー承認待ち。

## 生成ログ（追記）
| 2026-10-08 | theme-brief.md | 1.0.0 | theory-foundation.md |
| 2026-10-08 | impl/qct_ad/*, impl-report.md | 0.3.0 | theory-foundation, theme-brief |
| 2026-10-08 | data/*.csv, data-manifest.md | 0.2.0 | impl scripts |
| 2026-10-08 | outline.md, logic-map.md | 1.0.0 | theme-brief, theory-foundation |
| 2026-10-08 | manuscript.md, paper/main.tex, paper/figures/* | 0.2.0 | outline, impl-report, data |
| 2026-10-08 | gap-report.md | 1.0.0 | manuscript v0.1.x |
| 2026-10-08 | vault curation: 10 notes → review, summaries/tags | — | hyperresearch |

## S18 記録（2026-10-09）
- 手順 1: manuscript v0.4.0 を採点（新規性 4/データ量 6/データ質 4/ストーリー 5/論理 6/総合 5 → MAJOR_REVISION）。
- 手順 2: 重大 2 件を修正 → v0.5.0。(a) Bae–Acín 2007 §IV C（CAD2＋個別攻撃＝25%）と Acín et al. 2006 を vault 取得・引用し新規性を再定位。(b) 個別モデル Shannon 情報を tally 相互情報量に置換（N=10¹⁴ b=9: 21.89→20.86%）、表 1・図 2–4・漸近表を再生成。
- 手順 3: セット 1（批判的 5／否定的 5）→ v0.7.0: 明示的測定構成（b≤7）と Conjecture 1、certified/attained の区別、六状態混合ブロックの不等式方向の訂正（[0.8826, 0.8878]）、CKR09 帰着の限定、AEP 非単調の説明。セット 2 → v0.9.0: 要旨の条件付け、個別モデルの測定クラス明示、基準の一致、収束。
- 手順 4: S17 9 行追記（SUPPORTED 5/PARTIALLY 4）、S16: PDF 校正で 4 点修正（太字の生出力、引用符、式 (5) の改行、句読点）。
- 手順 5: reference-adequacy.md — 31 件で足りる（任意追加 3 件）。
- 手順 6: 確度 — REVIEW 80、ログ 80、参照充足 85、venue 80。
- 新規スクリプト: impl/qct_ad/joint_block_ansatz.py, sixstate_mixed_lb.py, paper/md2tex.py；新データ: data/joint_block_sdp.csv（b=4 完了）, joint_block_ansatz.log, sixstate_mixed_lb.log。
- vault: Bae–Acín 2007, Acín et al. 2006, Bhavsar 2026 を取得・キュレーション（lint ok）。

## 生成ログ（追記 2026-10-09）
| 2026-10-09 | manuscript-REVIEW.md | 1.0.0 | manuscript v0.4.0 |
| 2026-10-09 | manuscript.md（-v0.5.0/-v0.7.0/-v0.9.0） | 0.9.0 | REVIEW, adversarial-review-log, 新データ |
| 2026-10-09 | adversarial-review-log.md | 1.0.0 | S18 手順 3 |
| 2026-10-09 | reference-adequacy.md | 1.0.0 | S18 手順 5 |
| 2026-10-09 | venue-decision.md | 1.0.0 | S10 |
| 2026-10-09 | claims-ledger.md | 1.1.0 | S17（S18 ゲート） |
| 2026-10-09 | impl-report.md / data-manifest.md | 0.6.0 / 0.3.0 | S18 データ補完 |
| 2026-10-09 | paper/main.tex, main.pdf, figures/* | 0.9.0 | paper/md2tex.py |

## 残課題処理（2026-10-09, S15→S3→S7）
- 定理 1: 数値解の構造解析 → 二次形式符号の総当たりで指標解を発見 → 明示的基底 {X^{ỹ}Z^{(0,Ly′)}g±}（L=接頭 XOR）の代数的証明。b=2–9 で機械精度の検証。manuscript v1.0.0（要旨・§1・§3・§4・§7・§8・Appendix A）、main.tex 9 頁再組版。
- Appendix B: タイムロック下の post-selection 帰着（タグ付け・ツワール [KGR05] 追加引用）。
- 六状態: b=3 達成可能下界（sixstate_b3_lb.py）。
- 生成ログ: theory-foundation.md 1.3.0 / manuscript.md 1.0.0（-v0.9.0 スナップショット）/ claims-ledger 1.2.0 / impl-report 0.7.0 / data-manifest 0.4.0 / paper/main.tex 1.0.0。
- S11: ユーザー承認（2026-10-09）→ preprint-bundle/ 作成完了（下記）。

## Bell 対角族の再最大化（2026-10-09, S3→S5→S7）
- skl.eve_info_bd（c_ψ=(1−2φ_X−φ_Z c_φ)/(1−φ_Z)、D′≤φ_Z⁺ の sup、φ_X⁺ 直接使用）、bd_thresholds.py。p_guess の最悪化を各会計で独立に取る修正を対称族にも適用し reproduce/joint_thresholds を再実行。
- 結果: 表 1 を一般族の値に更新。対称族との差 ≤0.15 pt。結合モデル最良 17.66%/18.35%、T25 17.30% に対し利得 ≤1.05 pt。
- 原稿 v1.1.0（§3 Bell 対角段落、§4 sup 定義と証明主張の格上げ、§5、Appendix B 更新）、theory-foundation v1.4（J11）、ledger 1.3、impl-report 0.8、manifest 0.5。

## S11 プレプリントバンドル（2026-10-09, 承認済）
- preprint-bundle/: main.tex（v1.1.0、単体コンパイル確認 10 頁）、figures/*.pdf、anc/{code,data,manuscript.md}、README.md、arxiv-metadata.txt、arxiv-src.tar.gz。
- S17 ゲート通過（数値突合スクリプト、1 件を格子点値に修正）。投稿衛生 grep 該当なし。
- **残り（ユーザー作業）**: 著者名・所属の記入、arXiv メタデータの最終確認、アップロード。S12 は 2026-10-15 に PRA で承認・実施（下記）。
- 工程表: S11 完了（著者情報を除く）。

## S12 本投稿バンドル（2026-10-15, 投稿先 PRA 確定）
- submission-bundle/: main.tex（S11 と同一）、figures/ 3 点、supplemental_material.zip（code+data+README、72 KB）、cover_letter.md、suggested_referees.md（6 名候補）、declarations.md、requirements.md（PRA 要件 13 項目の 1 対 1 照合）。
- S17 ゲート通過（S11 と同一本文、六状態 b=1 の修正値を再確認）。投稿衛生 grep 該当なし。
- **残り（ユーザー作業）**: (1) 著者名・所属・ORCID を main.tex とカバーレター・宣言に記入、(2) arXiv へアップロードして番号を取得しカバーレター・宣言に記入、(3) 推薦査読者の確認（利益相反の除外）、(4) APS 投稿システムでアップロード。
- 工程表: S12 完了（著者情報・arXiv 番号を除く）。次は S13（パッケージ化、任意）と S14（査読対応、査読到着後）。

## 著者情報反映（2026-10-15）
- 著者: Hikaru Wakaura（h.wakaura@qiri.co.jp）単著に確定（2026-10-15 訂正）；所属 QIRI（東京）。paper/・preprint-bundle/・submission-bundle/ の main.tex、md2tex.py、カバーレター、宣言、arXiv メタデータに反映し、3 か所とも再コンパイル（10 頁）、arxiv-src.tar.gz 再作成。
- 残り（ユーザー作業）: arXiv アップロード → 番号をカバーレター・宣言に記入、著者貢献文・資金・ORCID（任意）、推薦査読者の確認、APS へ投稿。

## 主張別ファクトチェックと反映（2026-10-15）
- fact-check-report.md v1.1.0: 文献主張 30 件（SS 18 / PS 10 / NF 2 / C 0、A28 を本文照合で SS に更新）、本研究主張 11 件。
- 原稿 v1.2.0（-v1.1.0 スナップショット）: A2・A25・A30・B11 の表現修正、WMU06 への反論追加、GW99/KWW12/RGK05 の引用追加、Appendix B を sketch と明示。paper/・preprint-bundle/・submission-bundle/ の main.tex と両バンドルを更新。

## 導出の明示化（2026-10-15）
- 原稿 v1.3.0（-v1.2.0 スナップショット）: §3・§4 の各式に原典の式番号を付記、Appendix C（5 節）で本稿の導出を読者が追える粒度で記載。引用追加 Hel76, EMV03, KRS09。11 頁。3 か所の main.tex・両バンドル更新。

## パネルレビュー セット 1（2026-10-19）
- 構成: A=Opus（再現監査）、B=Codex（R1）→Sonnet（R2 フォールバック）。統合: manuscript-REVIEW.md v2.0.0（総合 4.5/10, MAJOR_REVISION）。
- 裁定計算: hidden_partition_sdp（n=3,4,6）、perprobe_opt、panel_variants（postsel/Fano/Holevo）、asymptotic_mp。
- 原稿 v2.0.0（-v1.3.0 スナップショット）: 要旨・§2（時刻表・攻撃クラス J/W/H）・§3（per-probe 最適性、分割隠蔽）・§4（会計分離、ε 統一）・§5（表 1 改訂、表 3・4 追加）・§7（Open question）・§8・App. B 書き直し。13 頁。
- 次: セット 2（宣言と実装の照合、較正の伝播、周辺文書）。

## パネルレビュー セット 2（2026-10-19）
- 構成: A=Opus（再現監査, MINOR_REVISION/パッケージ未収束, P1–P10）、B=Codex（論理, MAJOR_REVISION, B1–B12）。統合: manuscript-REVIEW.md v2.1.0。
- 裁定計算: panel_variants2.py（ε 再配分で閾値差 <1e-6 pt、PS min-ent b=11 17.52%、c_φ argmax 境界）。
- 原稿 v2.1.0（-v2.0.0 スナップショット）: 要旨・§1・A2・A4・§3・§4・§5（表 1 b=2 撤去、表 3 キャプション、表 4 列追加）・§6・§7（Open question 書き直し）・§8・App. A・C.5・文献 Win16。14 頁。md2tex 修正（表ループ、table*）。図 3 点再生成（凡例 per-probe H）。
- 両バンドル再作成（main.tex 同一、arXiv 要旨 1913 字、README/カバーレター/requirements/README_anc 更新、tar.gz/zip）。
- 収束宣言: 科学的較正・パッケージ整合の両ループとも収束（adversarial-review-log.md v2.1.0）。
- 残り（ユーザー作業）: arXiv アップロード → 番号記入、資金・ORCID、推薦査読者確認、APS 投稿。

## DAS 更新（2026-10-21）
- GitHub リポジトリ https://github.com/deeptell-inc/timelocked-ad（private、arXiv 投稿時に public 化）を作成。原稿 v2.1.1 に Data availability 段落（Appendix A 直前）、declarations・カバーレター・arXiv メタデータ・README に反映。両バンドル再作成。
- LaTeX ソース（3 か所の main.tex、arxiv-src.tar.gz）は追跡解除し `.gitignore` に追加（ユーザー指示）。ローカルには残存。

## DAS を APS 形式へ、ライセンスと release（2026-10-22）
- 原稿 v2.1.2: DAS 段落を APS 例文形式に統一し、参考文献 [Wak26]（Software and Dataset）を追加。declarations.md に投稿フォーム用文面、requirements.md に DAS 行（14）、CITATION.cff 追加。
- 原稿 v2.1.3（14 頁、エラーなし）: LICENSE（MIT、コード）・LICENSE-DATA（CC BY 4.0、データ・図・原稿）を追加。GitHub release v2.1 を作成し、[Wak26] と declarations の DAS はこの release（DOI なし）を指す。編集部が DOI を要求した場合は Zenodo 連携を有効化して release を再発行する。両バンドル再作成、push 済（最終コミット d311bd6）。
- 残り（ユーザー作業）: arXiv アップロード → 番号をカバーレター・宣言に記入、declarations.md の Funding・ORCID、推薦査読者 6 名の確認、APS 投稿、投稿時にリポジトリを public 化。次工程は S14（査読到着後）。

## プレプリント掲載先の変更（2026-10-29）
- arXiv は投稿制限中のため、プレプリントは Research Square に掲載（https://doi.org/10.21203/rs.3.rs-11453979/v1、2026-10-22、CC BY 4.0；Crossref で確認）。カバーレター・declarations・requirements の arXiv 番号欄を同 DOI に置換。preprint-bundle/ は制限解除後の arXiv 用にそのまま保持。
- リポジトリ deeptell-inc/timelocked-ad は public 化済み（確認 2026-10-29）。
- 残り（ユーザー作業）: declarations.md の Funding・ORCID、推薦査読者の確認、APS 投稿。

## S10 再実行: PRA 不採択（2026-10-29）
- PRA 査読前不採択（AX13009、技術的指摘なし、APS 内に代替誌なし）。venue-decision.md v1.2.0 に診断と次候補を記録。
- 次工程: ユーザーが投稿先を選択 → タイトル・要旨の改稿（S16）→ 選択誌のテンプレートへ移植 → S12 再実行（カバーレター改訂、過去投稿歴の開示）。

## J. Phys. A 向け改稿と S12 再実行（2026-10-29）
- 原稿 v2.2.0（-v2.1.3 スナップショット）: 題名・要旨のみ改稿（要旨 229 語、文献引用なし）。本文・表・図・数値は v2.1.3 と同一（S17 継承、新規 claim なし）。[Wak26] の題名も更新。
- paper/main.tex 再生成・再コンパイル（14 頁、未定義参照 0、投稿衛生 grep 0）。3 か所の main.tex・両バンドルの manuscript.md・arxiv-src.tar.gz・supplemental_material.zip・README.md・CITATION.cff・arxiv-metadata.txt（題名・要旨）を同期。
- submission-bundle-jpa/: IOP format-free 用に `preprint,12pt` 単段で組版した main.pdf（31 頁）、カバーレター（BAL11 への接続を明記）、宣言（Research Square プレプリントは旧題名と注記）、要件表 11 項目。
- 残り（ユーザー作業）: declarations.md の Funding・ORCID、推薦査読者の確認、ScholarOne で PDF＋補足 zip を投稿。
