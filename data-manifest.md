---
asset: data-manifest
version: 0.7.0
生成元入力: impl/qct_ad/{reproduce,scan,asymptotic,latency_budget}.py（決定的、乱数なし）
依存工程: S4（S5 と並行）
生成日: 2026-10-08
---

# データ台帳（S6）

全ファイルは `data/` 配下。生成コマンドは impl-report.md §5。乱数不使用のため再実行で同一値。

| ファイル | 生成元 | 内容 | 主要列 | 状態 |
|---|---|---|---|---|
| threshold_table_quick.csv | reproduce.py quick | T25 再現 4 点 ＋ QCT V-A（N=10⁸ b=3, N=10¹⁴ b=9） | model, N, b, qber_thr, delta_deg | 完了 |
| threshold_table.csv | reproduce.py | 全 b スキャン（N=10⁸,10¹⁰,10¹²,10¹⁴）、最終コード（Eq.19 領域条件込み） | 同上 | 完了（22 行×3–4 モデル） |
| rate_curves.csv | scan.py | 鍵率 ℓ/N vs QBER（N=10⁸,10¹⁴; b=1,3,5,9; 4 モデル）、最終コード | model, N, b, delta_deg, qber, rate | 完了（806 行） |
| asymptotic_thresholds.csv | asymptotic.py | 漸近閾値 vs b（f=1.2, 1.0） | f, b, thr_EUR_T25, thr_QCT_VA | 完了 |
| second_route_jiang.csv | （impl-report §3 の手順） | McDiarmid vs Jiang 統計の閾値比較 | N, b, entropy, stat, qber_thr | 完了 |
| latency_budget.csv | latency_budget.py | AD 段演算量比・遅延予算 | kind, b, ad_ops_per_bit, ldpc_ops_per_bit, t_coh_s, t_comp_s, … | 完了 |
| joint_block_sdp.csv | joint_block_sdp.py（cvxpy/Clarabel、目的関数を W_f=Σ_a ρ_a 形に前計算） | ブロック内非適応結合測定の最適成功確率 vs 個別投票 vs 適応 Helstrom（b=2,3,4 × D=0.05–0.24 の 21 点; P_joint=P_ad を 2×10⁻⁸ 以内） | b, D, c_psi, P_ind, P_joint, P_adaptive | 確定 |
| joint_block_ansatz.log | joint_block_ansatz.py（Riemannian 勾配上昇） | 線形決定則 â₁=y₁⊕y′·c の射影測定の最適基底: 適応値との差 b=4: 5×10⁻⁷, b=5: 2×10⁻⁶, b=6,7: 10⁻⁵–10⁻⁴（一次最適化、残差減少中で停止） | b, D, best, P_ad, gap | 確定（Conjecture 1 の証拠） |
| sixstate_mixed_lb.log | sixstate_mixed_lb.py | 六状態 b=2 混合ブロック・基底＋パリティ隠蔽の達成可能下界（16 出力射影測定）: D=0.167: P≥0.8826 (P_ad 0.8886), D=0.259: P≥0.9395 (P_ad 0.9583); 64 出力版は収束不良で下回る | c_psi, D, P_achievable, P_ad | 確定（下界） |
| joint_thresholds_quick.csv / joint_thresholds.csv | joint_thresholds.py | 結合測定上界（適応 Helstrom）での漸近・有限鍵閾値 | kind, f, b, N, thr_EUR, thr_joint_shannon, thr_joint_minent | 完了 |
| hidden_basis_sdp.csv | hidden_basis_sdp.py | BB84 基底＋パリティ隠蔽の最適非適応測定（b=1,2; 混合/同一基底; c_φ∈{1,0,−1}; 54 点） | b, mode, c_phi, c_psi, D, P_joint, P_adaptive | 完了 |
| sixstate_hidden_basis_b1.csv / _thresholds.csv | （impl-report §3e の手順） | 六状態 b=1 基底隠蔽 P(D) と一方向漸近閾値（Fano 界） | D, P_joint, P_adaptive / f, thr_* | 完了 |
| sixstate_b2_same_verify.log, sixstate_b2_mixed_cknown.log | （impl-report §3e） | 六状態 b=2 の同一基底／混合ブロック SDP | — | 完了 |
| reproduce_full.log, scan.log, joint_thresholds.log | 上記 | 実行ログ | — | — |

## 図（paper/figures/）
- fig2_eve_info: 1−I_E vs QBER（個別測定 実線、ブロック内結合測定 一点鎖線、EUR 破線、b=1,3,5,9,15）。メッセージ: 結合測定を許すと Eve の項は EUR 項のすぐ上まで落ちる。
- fig3_rate_vs_qber: 鍵率 vs QBER（N=10⁸, 10¹⁴、個別測定モデル）。メッセージ: 個別測定限定では閾値が 17.3%→20.7–21.9% へ移動する。
- fig4_threshold_vs_b: 閾値 vs b（漸近＋有限、個別／結合／EUR）。メッセージ: 個別は 25% へ、結合は 20% へ、EUR は ~19% で飽和。結合と EUR の差は ≤0.7 pt。

## 主要数値の所在（S17 照合用）
- 8.67 / 11.37 / 9.53 / 17.30%: threshold_table_quick.csv（T25 再現）
- 21.89 / 16.20%（Fano 版旧会計、N=10¹⁴ b=9 / N=10⁸ b=3）: panel_variants.csv（fano 行）；threshold_table_quick.csv は現行 tally 会計の quick 出力（20.86% 等）で、Fano 値は含まない
- 14.64 / 22.87 / 24.25%: asymptotic_thresholds.csv（f=1.0, b=1/9/31）


## 更新（2026-10-09, S18）
- threshold_table.csv / rate_curves.csv / asymptotic_thresholds.csv / fig2 / fig4 を tally 情報版 eve_info_distilled で再生成（個別モデル Shannon 列のみ変化; 結合モデル・T25 列は不変）。
- 旧 individual-Shannon 値（21.9% 等, Fano 下界）は無効。
| joint_block_theorem.log | joint_block_theorem.py | 定理 1 の明示的構成の検証: b=2–9、直交誤差・Helstrom 条件・P−P_ad（全て ≤10⁻¹³） | b, D, orth, cond, P, P_ad | 確定（定理の数値検証） |
| sixstate_b3_lb.log | sixstate_b3_lb.py（b=2,3） | 六状態混合ブロック・基底＋パリティ隠蔽の達成可能下界（64 出力射影、3 シード） | b, c_psi, D, P_achievable, P_ad, err_ratio | 確定（下界） |
| bd_thresholds.csv | bd_thresholds.py | φ_X≠φ_Z の Bell 対角集団攻撃に対する有限鍵閾値（individual/joint × Shannon/min-ent、sup over D′） | model, N, b, qber_thr, delta_deg | 確定 |
| panel_variants.csv | panel_variants.py | post-selection 係数を全 ε に課した閾値（b=7,9、4 モデル）、Fano 版個別閾値（旧会計、N=10¹⁴ b=9 / N=10⁸ b=3）、Holevo（量子メモリ、時間ロックなし）Shannon 閾値 b=5,7,9 | model, N, b, qber_thr | 確定 |
| perprobe_opt.csv | perprobe_opt.py | 同一 4 出力実 POVM（Naimark）での per-probe ブロック情報 J と推測確率の最大値 vs Helstrom＋tally、b=2–9、D=0.10–0.23 | b, D, J_helstrom, J_opt, pg_helstrom, pg_opt | 確定（奇数 b で一致、偶数 b で改善） |
| hidden_partition_sdp.csv (+_n5, _n6) | hidden_partition_sdp.py, hidden_partition_n5/6.py | 分割を事後情報とする SDP（b=2、n=3,4,5,6）: P_joint_hidden_partition vs P_ind, P_ad | n, b, D, c_psi, P_ind, P_joint_hidden_partition, P_adaptive, n_povm | 確定（n=3,4,5,6 完了|
| panel_variants2.csv | panel_variants2.py | ε 総量の再配分（ε_sec=8e-10、総 1e-9）での閾値: joint Shannon b=7 18.348%、collective min-ent b=11 17.659%（5ε/4 版と <1e-6 pt 差）；PS を課した collective min-ent b=11 17.52%、b=15 16.02%（§5 の「0.3 pt」の出典） | model, N, b, qber_thr |
| cphi_argmax.csv | panel_variants2.py | I_E^joint の c_φ 最大点が 1 を下回り始める D（b=2: 0.206, 3: 0.222, 5: 0.232, 9: 0.239, 15: 0.243；§3 の出典） | b, first_D_with_argmax_below_1 |
| asymptotic_thresholds_mp.csv | asymptotic_mp.py（mpmath 60 桁） | 漸近閾値（EUR / per-probe / joint Shannon / joint min-ent）b=1–61；asymptotic_thresholds.csv と joint_thresholds.csv の漸近行はこの値で上書き済（b=31 の倍精度アンダーフローを修正） | f, b, thr_* | 確定 |
| threshold_table_quick.csv, bd_thresholds_quick.csv | reproduce.py quick / bd_thresholds.py quick（パネル A の再実行） | quick 実行の現行出力（旧 Fano 版の残骸を置換） | model, N, b, qber_thr | 確定 |
