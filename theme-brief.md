---
asset: theme-brief
version: 1.0.0
生成元入力: theory-foundation.md v1.0.0, T2_prior_art.md §5（ゴール＋仕様）
依存工程: S3
生成日: 2026-10-08
起点: P4（承認ゲートなし、S5 優先）
---

# 研究テーマ（S4）

## 問い（1文）
Eve の量子メモリ寿命 t_coh より長く古典後処理メッセージ（AD パリティ・IR 情報・任意で基底）を隠す（遅延または計算量時間ロック）だけで、decoy-BB84 の有限鍵許容 QBER は Treplin ら 2025 の 17.3%（N=10¹⁴）をどこまで超えられるか、そしてそれは既存 FPGA 蒸留エンジンの実時間性を保ったまま実装できるか。

## 新規性主張（独立 2 経路で確認予定）
1. QCT 仮定下で後処理メッセージを時間ロックした decoy-BB84+AD の**有限鍵率式**を初めて導出する（確認経路: arXiv 全文検索＋Semantic Scholar 被引用連鎖は済、2 経路目として IEEE Xplore/Optica 検索を S9 で実施）。
2. 利得の機構を「暗号化」から「Eve の測定の非適応化（公開遅延 τ_ann > t_coh）」へ再定義し、PQC 時間ロックを遅延圧縮として位置づける（確認経路: Novak 2025 の無利得定理と P-K 2023 §III の「遅延」言及の 2 経路で整合済 → PARTIALLY→SUPPORTED 候補）。
3. AD 段を含む QKD 後処理の実時間 FPGA 実装は存在しない（確認経路: arXiv 済、IEEE Xplore を S9 で）。

## 貢献（箇条書き）
- C1: 二層の脅威モデル V-A（基底即時公開、後処理のみ遅延）/ V-B（基底も遅延）を定義し、各々で Eve を古典側情報に帰着する条件（A2 の遅延不等式）を明示。
- C2: 標準個別攻撃モデル（i.i.d. 即時測定）で、反復符号 AD と Treplin 統計を合成した有限鍵率計算器を公開実装し、Treplin の数値（8.7→11.3%, 9.5→17.3%）を再現した上で QCT-AD の閾値を数値化。
- C3: 命題 P2（τ_ann ≤ t_coh で Treplin に還元）と P4（もつれ限界を超えない）による整合性検証。
- C4: AD＋遅延/暗号化を既存蒸留パイプラインに 1 段追加する実時間アーキテクチャ案と、レイテンシ予算（τ_ann vs t_comp）の定量化。
- 非貢献（明示）: 一般の結合・非適応測定（U1）に対する厳密定理は与えない。

## スコープと非スコープ
- スコープ: decoy-BB84（3 強度、能動基底）、直接和解、反復符号 AD（b=2…9、非連接）、V-A/V-B、有限鍵 N=10⁸–10¹⁴、FPGA は設計・スループット見積（合成までは S13 で判断）。
- 非スコープ: 6 状態・MDI・TF・CV 変種、連接 AD、Eve の有界記憶 q>0（U2）、PQC 鍵配送プロトコル自体の安全性証明（U3）、実機 QKD 実験。

## 逆算工程計画（S{n} 列）
| 順 | 工程 | 成果物 | ゲート |
|---|---|---|---|
| 1 | S5 理論実装 | impl/（鍵率計算器: Treplin 再現 → QCT-AD V-A）, impl-report.md | S16 |
| 2 | S6 データ収集 | data/（QBER–鍵率曲線、閾値表、b 最適化、τ_ann/t_comp 予算表）, data-manifest.md | S16 |
| 3 | S8 構成 | outline.md, logic-map.md | S16, H4 |
| 4 | S7 執筆 | manuscript.md（PRA/Quantum 想定、revtex4-2） | S16, H4, **S17** |
| 5 | S9 補完 | gap-report.md（U1 の限定表現、IEEE 2 経路目検索） | **S17** |
| 6 | S18 敵対的査読 | manuscript-REVIEW.md 等 | S16/S17 内包 |
| 7 | S10 投稿先 | venue-decision.md | — |
| 8 | S13 パッケージ化 | program-package/（S5/S6 と並行可） | — |
| 9 | S11/S12 | preprint-bundle/, submission-bundle/ | **S17**、投稿直前にユーザー承認 |

## 想定成果物
- impl/qct_ad/: `treplin_skl.py`（Eq. 93/94 再現）, `qct_ad_rate.py`（V-A 個別攻撃＋AD）, `scan.py`, `tests/`
- data/: `threshold_table.csv`, `rate_curves.csv`, `latency_budget.csv`
- manuscript.md → paper/main.tex
