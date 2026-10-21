---
asset: fact-check-report
version: 1.1.0
生成元入力: manuscript.md v1.1.0 / submission-bundle/main.tex、vault 全文ノート 14 件、書誌のみ 18 件
依存工程: S17（主張別ラベリング、ユーザー指定形式）
生成日: 2026-10-15
---

# 主張別ファクトチェック（原稿 v1.1.0）

**判定ラベル**: SS = Strongly Supported / PS = Partially Supported / C = Contradicted / NF = Not Found in Uploaded Sources。
**資料の範囲**: vault に全文があるもの（T25, GW99, TCR09, VA20, Novak25, PK23, WMU06, Jiang21, BAL11, BA07, ABBMM06, BMB26, FGGNP97=抄録, IACR 2026/1359）と、書誌・抄録のみで本文未取得のもの（Lim14, Maurer93, GL03, Chau02, ABBMM05, DFSS05, WST08, TL17, FMCC12, MBBA25, BWW08, GW10, Levitin95, Fuchs96, CKR09, KGR05, Walenta14, Constantin17, Cheng25）。後者に依拠する主張は本文で確認できないため、内容が標準的でも **PS 以下**に留めた。頁番号は vault ノートのページ区切り（arXiv 版 PDF）に基づく。本研究自身の数値・定理は「データ」欄で結果ファイルに紐付け、文献判定とは区別した。

## A. 先行研究・背景に関する主張

| # | 主張（原稿の箇所） | 判定 | 支持する資料（頁/節） | 挑戦・限定する資料 | フラグ |
|---|---|---|---|---|---|
| A1 | decoy-BB84 の一方向閾値は「9–11% depending on the source model」（§1） | PS | T25 p.1「around 11% using ideal single-photon sources」; T25 p.29: decoy で 9.5%（N=10¹⁴）; 本実装 9.53%/8.67% | Lim14 は書誌のみ（本文未確認） | Lim14 の引用は本文未照合。T25 単独でも支持できるが、「9–11%」の下端 9% は N=10⁸ の 8.7% とも整合せず（8.7–11% が正確）。 |
| A2 | 「Daylight free-space links, fibres shared with bright classical traffic, and long satellite passes routinely approach or exceed this level」（§1） | **NF** | なし（引用なし） | — | **未支持の一般化**。出典がない経験的主張。具体的な実験報告を 1–2 件引用するか、「can approach」に弱めるべき。 |
| A3 | AD は Maurer が古典鍵合意で導入し、Gottesman–Lo が QKD に導入（§1） | PS | BA07 p.4「standard two-way communication protocol introduced by Maurer in [20], also known as CAD」; T25 p.1 | Maurer93, GL03 は書誌のみ | 二次資料経由。標準的な帰属なので実害は小。 |
| A4 | Chau: BB84 20.0%、六状態 27.6%（§1, §3, §7, §8） | SS | BA07 p.5–6「Chau has improved these bounds up to 20.0% and 27.6%」; ABBMM06 p.4 Eq.(23) 0.2764「the same value as obtained by Chau」 | Chau02 原典は書誌のみ | 2 つの独立全文が一致。原典未読だが十分。 |
| A5 | Gottesman–Lo の値 18.9% / 26.4%（Appendix・ledger 背景） | SS | BA07 p.5, p.6 | — | — |
| A6 | Acín et al. / Bae–Acín は反復符号 AD の集団攻撃下での閾値 20%/27.6% が tight であることを示し、Eve の最適攻撃はパリティ公開後に 2 つの積状態を識別する（§1, §3） | SS | ABBMM06 p.1（iff 条件）, p.2 Eq.(5), p.3「she first waits until step (ii) is completed」, p.4 Eq.(23); BA07 p.2「tight for (d+1)- and 2-bases protocol」, p.6, p.9, p.17 Eq.(68) | — | 原稿 v0.4 以前はこれが欠落していた（修正済）。 |
| A7 | Bae–Acín: 遅延で Eve を個別攻撃に強制でき、CAD2 ではもつれ条件（BB84 で 25%）が安全条件になり、CAD1 では 20% のまま（§1, §3, §7） | SS | BA07 p.4「they can introduce a delay … Eve is then forced to measure her states before the reconciliation, as for an individual attack」; p.9–10 §IV C「the security condition using CAD2 is the entanglement condition λ₁>1/2 … CAD1 … the corresponding security condition is the same as for collective attacks」 | — | 本稿の主結果はこの remark を「per-copy 測定に限る」と限定する。原稿はその旨を明示している（§7）。 |
| A8 | 多コピー 2 状態識別の最適値は個別測定の適応列で達成可能（ABBMM05）（§3, §7） | PS | BA07 p.9「there exists an adaptative sequence of individual measurements which achieves the optimal error probability (30) [36]」（[36]=ABBMM05） | ABBMM05 は書誌のみ | 二次資料経由。 |
| A9 | Jiang et al.: SNS-TF QKD の二方向後処理の有限鍵解析、仮想 IID 帰着（§1, §2 A5, 表 1 注） | SS | Jiang21 p.1「imagining a virtual set of bits where every bit is independent and identical」 | — | — |
| A10 | Bhavsar–Moon–Bae: 仮説検定による二方向蒸留の有限ブロック長界（§1） | SS | BMB26 p.1 抄録・序論 | — | 2026 年 2 月の arXiv 原稿であり査読未了。注記不要だが認識しておく。 |
| A11 | T25: b ビット反復符号 AD で有限鍵閾値 9.5%→17.3%（N=10¹⁴）、EUR による min-entropy 界、Eve は最後のメッセージまで純粋化を保持できる（§1） | SS | T25 p.1, p.29（9.5→17.3、8.7→11.3）; p.15「we use the entropic uncertainty relation … coherent attack scenario」 | — | 本実装でも再現（8.67/11.37/9.53/17.30%）。 |
| A12 | T25 Eq.(19) の単調性は φ_X+φ_Z<1/2 の領域でのみ証明されている（§1, §7, Appendix） | SS | T25 p.33 Appendix B「under the conditions 0<ϕx,ϕz<1/2 and ϕx+ϕz<1/2」; p.25 | — | 領域外の非単調性（0.499→0.25）は本研究の計算（impl-report §4）。T25 の誤りではなく適用条件であることを原稿は明記している。 |
| A13 | Watanabe–Matsumoto–Uyematsu: 事前共有 OTP でパリティを暗号化し、Shor–Preskill 枠組みで純鍵率が向上（§1） | SS | WMU06 p.1「the net key rate of the QKD with proposed preprocessing exceeds the key rate of the QKD without it」「guaranteed in the same way as Shor and Preskill's arguments」 | Novak25 p.1 は事前共有鍵の出所を問題視（「they require an initial pre-shared key」） | 原稿は反論点（事前共有鍵の必要）に触れていない。1 文の追加を推奨。 |
| A14 | Pastushenko–Kronberg: 量子メモリが脱コヒーレンスすれば Eve の情報は Holevo ではなく加法的アクセス可能情報で抑えられる；合成可能安全性は主張していない（§1） | SS | PK23 p.1 §III, p.4（decoherence time の仮定）, p.6「the method does not provide composable security [31] … provides everlasting security [35] in a narrow sense」 | — | — |
| A15 | Novak: 同一セッションの鍵で一方向 EC データを OTP 保護しても、固定安全性レベルで鍵率は不変（§1, §2） | SS | Novak25 p.1「the OTP keys originate from the same QKD session」「equivalence holds for a fixed security level, defined via the diamond distance」 | — | 原稿の「leaves the key rate exactly unchanged」は Novak の「equivalence」と整合。 |
| A16 | Fung–Ma–Chau–Cai: PA の遅延は安全性と鍵率を変えない（§1） | PS | ledger: arXiv:1111.4411 抄録 | FMCC12 本文未取得 | 抄録ベース。本文の条件（遅延の定義）を確認して引用箇所を付けると強くなる。 |
| A17 | Vyas–Alléaume: QCH モデル（t_coh<t_comp）、Eve の最適戦略は即時測定＋事後復号（Prop. 1）、光量子メモリの t_coh は 1 秒未満、MUB-QCT は d+1 MUB を用い QKD を超える鍵率（§1, §2 A1, §3, §7） | SS | VA20 p.2「significantly below one second」「Eve is forced to measure ρ before tcoh」; p.9 Proposition 1; p.1「O(√d) multiplication of key rates」「d+1 mutually unbiased bases」 | — | 「rates beyond QKD」は O(√d) の意味で正確。「everlasting」の定義は VA20 のアクセス可能情報基準（§4 で基準一致を 1 文で説明済）。 |
| A18 | Mazzoncini et al. 2025: 通信複雑性に基づくハイブリッド量子暗号（§1） | PS | 書誌のみ（Quantum 9, 1862） | 本文未取得 | 内容の要約はしていないので実害は小。 |
| A19 | bounded / noisy-storage model（DFSS05, WST08）（§1） | PS | 書誌（FOCS 2005; PRL 100, 220502）を arXiv API で確認 | 本文未取得 | 標準的引用。König–Wehner–Wullschleger 2012 の追加で強化可。 |
| A20 | 対称攻撃のユニタリ U、F=(1+c_φ)/(2−c_ψ+c_φ)、ψ/φ 部分空間の直交性、六状態では c_φ=0（§3） | SS | GW99 p.1 Eqs.(1)–(2); p.2 Eq.(3)「F = (1+⟨φ↑\|φ↓⟩)/(2−⟨ψ↑\|ψ↓⟩+⟨φ↑\|φ↓⟩)」; p.2「for the 6-state protocol ⟨φ↑\|φ↓⟩=0」「δ₁=1」; p.3 Eq.(7) | — | 原稿 §3 の「whose symmetric attack has c_φ=0」は GW99 p.2 で明示的に支持される（引用を [GW99] に付けると良い）。 |
| A21 | GW99 定理 1: AD による鍵合意 iff D/(1−D)<2√(δ₀(1−δ₀))、4 状態で 1/4、6 状態で 1/3；「incoherent」測定の仮定（§3, §7） | SS | GW99 p.3 Theorem 1 Eq.(11), Eqs.(8)–(9); p.1「Under the assumption of incoherent eavesdropping」 | — | 原稿の「the 25% limit of Ref. [GW99] is the limit for an adversary whose memory is shorter than the spacing between pulses」は本稿の解釈。GW99 自身は「incoherent」を仮定しただけで、メモリ時間の議論はしていない（§7 の表現は妥当）。 |
| A22 | FGGNP97: 最適個別盗聴（§2 A4） | PS | FGGNP97 抄録 p.1「optimal eavesdropping probe, consisting of two qubits」 | 本文未取得 | GW99 が同じ攻撃族を Eq.(1)–(3) で与えるため、本文数式は GW99 に帰属させてある。 |
| A23 | TCR09 定理 9: δ(ε,η)=4 log η √(log(2/ε²))、n ≥ (8/5) log(2/ε²)；二値で η ≤ 2+√2（§4） | SS（η の上界は本稿の評価） | TCR09 p.6 Eq.(30)「for n ≥ 8/5 log 2/ε², δ(ε,η) := 4 log η √(log 2/ε²)」 | — | η ≤ 2+√2 は η=√2^{−H_min}+√2^{H_max}+1 に二値（H_min≥0, H_max≤1）を代入した本稿の評価。原稿は「for a binary variable」と明記しており妥当。 |
| A24 | BAL11: メモリなし敵対者の閾値 BB84 15.4%（個別 14.6%）、SARG04 17.6%、六状態 20.4%（個別 15.6%）（§3） | SS | BAL11 p.2, p.5「less than one point more than the 14.6%」, p.6「20.4% and 17.6%」「compared to 12.6% and 15.6%」 | — | — |
| A25 | 「the gain is confined to protocols with more than two bases, in line with the result of Ref. [BWW08] that two bases admit a common optimal measurement」（§3） | **PS（過度な一般化）** | BWW08 は抄録のみ。BAL11 p.5: BB84 でも 14.6%→15.4% の利得がある | **BAL11 p.5 が挑戦**: BB84（2 基底）でも Shannon 閾値で +0.8 pt の利得が報告されている | 本稿の推測確率基準では BB84 に差がない（hidden_basis_sdp.csv）が、文は一般に読める。「in guessing probability the gain is confined …; in Shannon information Ref. [BAL11] finds 0.8 points for BB84」と限定すべき。BWW08 の主張も抄録ベース。 |
| A26 | KGR05: Pauli ツワールにより集団攻撃は観測誤り率を持つ Bell 対角攻撃に帰着（§3, Appendix B） | PS | 書誌（PRL 95, 080501）を arXiv API で確認 | 本文未取得 | 標準的結果だが本文箇所を確認して引用節を付けるべき。Renner の博士論文（2005）を併記すると強くなる。 |
| A27 | CKR09 post-selection: i.i.d. 安全性 ε → 任意攻撃 ε(n+1)^{d²−1}、純粋化系上の CP 写像で成功確率 ≥ (n+1)^{−(d²−1)}（Appendix B） | PS | 書誌のみ; T25 p.15 が同技法 [48] に言及 | 本文未取得 | 命題の内容は標準的だが、「タイムロック制約下でも通る」という本稿の拡張は本稿の論証（Appendix B）であり文献支持はない。**本稿の新しい主張として明示することを推奨**（現状「carries over … because」と書かれているが、証明は 1 段落のスケッチ）。 |
| A28 | Levitin95 / Fuchs96: 2 等確率純粋状態のアクセス可能情報は Helstrom 測定で達成（§3） | **SS（v1.1 で更新）** | Fuchs96（vault 全文）p.89–90: 「in the cases where the optimal information gathering measurement can be written explicitly, it coincides with the optimal error probability measurement … Levitin [110] has shown that in this case the optimal orthogonal projection-valued measurement is indeed the actual optimal measurement」; p.90 Eq.(3.263)（q=\|⟨ψ₀\|ψ₁⟩\|² の関数としてのアクセス可能情報）, p.96 Eq.(3.307) | — | 原稿 v1.2.0 で引用箇所（Chapter 3, Eq. (3.263)）を明記。 |
| A29 | BWW08 / GW10: 事後測定情報付き状態識別の定式化（§1, §3, §7） | PS | BAL11 p.7 が BWW08 [21] を引用; GW10 は arXiv API で書誌確認 | 本文未取得 | 定式化自体は本稿で自己完結しているため依存は弱い。 |
| A30 | FPGA 鍵蒸留エンジン（Walenta14, Constantin17, Cheng25）は復号器律速で、BP-LDPC 復号は「several hundred operations per bit」（§6） | **NF** | IACR 2026/1359 ノートに演算数の記載なし；3 文献は書誌のみ | — | **未支持の数値主張**。「数百演算/ビット」は本稿の桁推定（latency_budget.py）であり文献値ではない。「of order 10²–10³ operations per bit for typical iteration counts [cite a BP-LDPC implementation paper]」に改めるか、数値を落とす。 |

## B. 本研究の主張（データ・証明に紐付け）

| # | 主張 | 判定 | 根拠（ファイル） | フラグ |
|---|---|---|---|---|
| B1 | T25 の 4 公表値の再現（8.67/11.37/9.53/17.30%） | SS | data/threshold_table.csv; T25 p.29 | 0.1 pt 以内。 |
| B2 | 定理 1（非適応結合測定が全 b で適応値に到達、明示的基底） | SS | Appendix A の証明; data/joint_block_theorem.log（b=2–9, 差 ≤5×10⁻¹⁵）; data/joint_block_sdp.csv（b≤4, SDP） | 証明と 2 系統の数値。第三者検証なし（投稿で得られる）。 |
| B3 | 有限鍵閾値（表 I、Bell 対角族で最大化；結合モデル最良 17.66/18.35%） | SS（自前データ） | data/bd_thresholds.csv, joint_thresholds.csv | 対称族との差 ≤0.15 pt も同ファイルで確認。 |
| B4 | 個別モデル 20.7–20.8%（b=9）、漸近 21.9/23.8% | SS（自前） | data/bd_thresholds.csv, asymptotic_thresholds.csv | 参考値であることを §3/§5 に明記済。 |
| B5 | Fano 式 1−h(γ_b) は Eve の情報の下界で、tally 置換で 1.0 pt 低下 | SS | 情報理論（Fano 不等式）; threshold_table.csv（旧 21.89→20.86%） | 旧値 21.89% は原稿に残っていない（投稿衛生規則）。 |
| B6 | 基底隠蔽: BB84 は c_φ=1 で P_joint=P_ad（b=1,2）；六状態 b=1 で 0.751 vs 0.835（D=0.168） | SS（自前） | data/hidden_basis_sdp.csv; sixstate_hidden_basis_b1.csv（D=0.1683: 0.7508/0.8350） | — |
| B7 | 六状態 b=2 同一基底 0.888644 vs 0.888642；混合ブロックの挟み込み [0.8826, 0.8878]、[0.9395, 0.9556]；b=3 で誤り率比 ≤1.04 | PS | data/sixstate_b2_same_verify.log, sixstate_b2_mixed_cknown.log, sixstate_mixed_lb.log, sixstate_b3_lb.log | 下界は一次最適化（収束保証なし）。D=0.259 の比 1.46/1.43 は緩い。原稿はそう明記済。 |
| B8 | 「a bounded error ratio leaves the 27.6% limit unchanged」（§3） | PS | 指数の議論（本稿） | **因果主張に注意**: 比が有界であること自体が未証明。原稿は「evidence, not a proof」と書いており妥当だが、「bounded ratio ⇒ threshold unchanged」の論理は誤り率の指数が閾値を決めるという標準的事実に依存する（Bae–Acín の条件 (68) が指数条件であることを根拠に挙げると良い）。 |
| B9 | 「The cipher compresses latency; it does not create the gain」（§2） | PS | Novak25 p.1（暗号化単独は無利得）; A2 の構成 | 因果主張だが根拠は明示されている。PK23 p.4 の「遅延」言及を併記すると強い。 |
| B10 | Bell 対角族の c_ψ=(1−2φ_X−φ_Z c_φ)/(1−φ_Z)、φ_Z 非単調性 | SS | theory-foundation.md J11（導出）; skl.eve_info_bd（φ_X=φ_Z で旧関数と一致） | GW99 p.3 Eq.(7) の Bell 対角形と整合。 |
| B11 | 「with the post-selection step of Appendix B the formula is a security statement against every timelock-restricted adversary in the model」（§4） | PS | Appendix B（スケッチ） | 証明は 1 段落のスケッチであり、(i) ツワールの公開タイミングと A2 の整合、(ii) 制限された識別器クラスに対する post-selection 不等式の形式的な再証明、は省略されている。「up to the standard post-selection argument, which we sketch」程度に弱めるか、スケッチを Appendix で定理の形にすることを推奨。 |

## C. 横断フラグ

**過度な一般化**
- A2（free-space / satellite の QBER 水準）: 出典なし。
- A25（「2 基底では利得がない」）: BAL11 自身が BB84 で +0.8 pt を報告しており、推測確率基準での主張であることを限定すべき。
- §8「unconditional security already achieves essentially the same」: 「essentially」= ≤1.05 pt は表 I で支持。問題なし。

**未支持または弱い因果主張**
- A30: 「several hundred operations per bit」（文献なし）。
- B8: 「bounded ratio ⇒ 27.6% 不変」（指数論法は正しいが比の有界性は未証明。原稿は明記済）。
- B11: Appendix B の帰着は命題として証明されていない（スケッチ）。

**欠落している反論・留保**
- WMU06 の事前共有鍵問題（Novak25 p.1 が指摘）: §1 に 1 文追加を推奨。
- Levitin/Fuchs の結果（A28）は結合モデル Shannon 列の正当性の要であり、本文照合が必要。
- 本稿の攻撃族の限定（ツワール後の Bell 対角）は Appendix B にあるが、§5 の数値が「対称族」から「Bell 対角族」に変わった経緯は本文に不要（投稿衛生）。現状問題なし。

**複数引用で強化できる箇所**
- A1: Lim14 に加え T25 p.1 を併記。
- A19: König–Wehner–Wullschleger IEEE TIT 58, 1962 (2012)。
- A26: Renner 博士論文（2005）または Renner–Gisin–Kraus PRA 72, 012332 (2005)（arXiv API で書誌確認済）。
- A28: Fuchs–Caves PRL 73, 3047 (1994)。
- A20/A21: 六状態の c_φ=0 に [GW99] を明示的に付ける（現在は文脈引用のみ）。

## D. 集計
- 文献主張 30 件: SS 17 / PS 10 / NF 3（A2, A28, A30）/ C 0。
- 本研究主張 11 件: SS 7 / PS 4。
- **投稿前に対応を推奨する項目**: A2（出典追加または表現緩和）、A25（限定表現）、A28（本文照合）、A30（数値の根拠または削除）、B11（帰着の位置付けを「スケッチ」と明示）。いずれも事実性の誤り（Contradicted）ではなく、表現・引用の強化。

## E. 反映状況（原稿 v1.2.0, 2026-10-15）
- A2: 「routinely approach or exceed」→「can approach」に緩和（出典なしの一般化を除去）。
- A25: 「in guessing probability the gain is confined …, while in Shannon information Ref. [BAL11] still finds a gain of 0.8 percentage points for BB84」に限定。
- A28: Fuchs 学位論文を vault に取得して本文照合（p.89–90, Eq. (3.263)）→ SS。原稿に章・式番号を明記。
- A30: 「several hundred operations per bit」→「orders of magnitude below the per-bit cost of iterative LDPC decoding」（数値を撤去）。
- B11: §4 と §7 で Appendix B を「sketch」と明示、Appendix B の題名と冒頭を変更。
- WMU06 の反論点: Novak25 の「事前共有鍵の出所」指摘を §1 に追加。
- 追加引用: 六状態 c_φ=0 に [GW99]；[KWW12]（König–Wehner–Wullschleger, IEEE TIT 58, 1962, arXiv 書誌確認）；[RGK05]（Renner–Gisin–Kraus, PRA 72, 012332, arXiv 書誌確認）。Fuchs–Caves 1994 は Crossref で確認したが本文未読のため追加せず。
- 再検証: 3 か所の main.tex 再コンパイル（10 頁、未定義参照 0）、投稿衛生 grep 0 件、要旨 1773 字。バンドル（arxiv-src.tar.gz, supplemental_material.zip）更新。
