---
asset: outline
version: 1.0.0
生成元入力: theme-brief.md v1.0.0, theory-foundation.md v1.0.0, impl-report.md v0.2.0
依存工程: S4
生成日: 2026-10-08
---

# 構成（S8）— 原稿アウトライン

想定媒体: Physical Review A / Quantum（revtex4-2）。Nature 型 7 要素アブストラクト、大→小→大の導入、1 図 1 メッセージ。

## タイトル案
Timelocked advantage distillation: finite-key decoy-state BB84 beyond the entropic-uncertainty threshold under a quantum computational timelock

## Abstract（7 要素）
1. 背景: QKD の許容 QBER は後処理で決まり、AD で 17.3%（有限鍵）まで到達。
2. 問題: それ以上は Eve の量子メモリに対する EUR 界が律速。
3. 着想: Eve の量子メモリ寿命 t_coh より長く後処理メッセージを隠せば、Eve は測定を後処理に適応できず古典化される（QCT）。
4. 方法: Treplin 統計 ＋ Gisin–Wolf 個別攻撃族の最悪化 ＋ 反復符号 AD の有限鍵式。
5. 結果: N=10¹⁴, b=9 で 20.7–21.9%、漸近で 25% に近づく。
6. 含意: PQC は「遅延圧縮」であり、暗号化自体は無利得（Novak）。
7. 展望: 結合測定への一般化（U1）と実時間 FPGA。

## 1. Introduction（大→小→大）
- 大: QKD の実用限界は雑音耐性。
- 中: AD の歴史（Gottesman–Lo, Chau）と有限鍵化（Jiang 2021, Treplin 2025）。EUR 界の壁。
- 小: 後処理暗号化の系譜（Watanabe 2006, P-K 2023）と Novak 2025 の無利得定理。
- 大: 本研究の主張と貢献 C1–C4。

## 2. Model and assumptions
- A1–A5、V-A/V-B、遅延不等式。PQC の役割（遅延圧縮）。
- 図 1: タイムライン（傍受 t_rx、t_coh、公開 t_m+Δ_m、t_comp）。

## 3. Reduction of Eve to classical side information
- Vyas–Alléaume 命題 1 の適用。V-A では Gisin–Wolf 対称個別攻撃族に帰着。
- 最悪化パラメータ c_φ、δ0, δ1。
- 図 2: δ0(D) と Eve の蒸留ビット情報 I_E(D,b)。

## 4. Finite-key secure key length
- Protocol（Treplin Protocol 1 ＋ 遅延/暗号化）。
- 式: ℓ_QCT = S⁻_K̄[1 − I_E(φ⁺_Z,b)] − AEP − λ_IR − log 項。
- 命題 P2（還元）、P4（もつれ限界）。
- 合成可能性の範囲限定（QCT 内）と ε の配分。

## 5. Numerical results
- 図 3: 鍵率 vs QBER（N=10⁸,10¹⁴; b=1,3,5,9; T25 vs QCT）。
- 表 1: 閾値表（有限鍵・漸近）。
- 図 4: 閾値 vs b（漸近、25% への収束）。

## 6. Implementation considerations
- AD 段の演算量、遅延予算表、既存 FPGA エンジンへの統合案。

## 7. Discussion
- U1（結合測定）、U2（有界記憶 q>0）、U3（PQC 鍵配送）。
- Novak との関係、P-K との関係、MUB-QCT との比較（基底ロック vs 後処理ロック）。

## 8. Conclusion

## References（claims-ledger と突合）
T25; Jiang 2021; Novak 2025; P-K 2023; Watanabe 2006; Vyas–Alléaume 2020; Mazzoncini 2025; Gisin–Wolf 1999; Fuchs 1997; Tomamichel–Leverrier 2017; Gottesman–Lo 2003; Chau 2002; Maurer 1993; Csiszár–Körner 1978; Walenta 2014; Constantin 2017; Cheng 2025; Ballester–Wehner–Winter 2008; TFKW 2013; Grilo 2025.
