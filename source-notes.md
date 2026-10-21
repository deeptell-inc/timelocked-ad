---
asset: source-notes
version: 1.1.0
生成元入力: T2_prior_art.md（S1相当）＋ hyperresearch で取得した一次 PDF/HTML（research/notes/ 配下）
依存工程: S1（代替: T2_prior_art.md, qcrypt_5x5_analysis.md）
生成日: 2026-10-08
---

# 情報源ノート（S2）— T2: QCT 仮定下の暗号化 AD 付き decoy-BB84 有限鍵率

取得は `{{TOOL:web-fetch}}`（hyperresearch fetch、原典 PDF/全文 HTML）。要約経由の孫引きなし。`[i]` は RIS コーパス通し番号。

## Treplin, Kleinpaß, Orsucci (DLR) 2025, "Finite Size Analysis of Decoy-State BB84 with Advantage Distillation" (arXiv:2511.21665, 取得 2026-10-08, vault note `finite-size-analysis-of-decoy-state-bb84`)
- 主張: decoy-BB84 + AD の「初の包括的有限鍵解析」。AD により現実的鍵長で許容 QBER が約 9.5%→約 17.3%。
- 手法: Lim et al. の自己完結 SKL 導出をエントロピー不確定性関係（EUR）で AD 向けに改変。AD = b ビット反復符号（隣接パリティ c_A, c_B を公開、一致ブロックの先頭ビットを採用）。3 強度 decoy（µ1>µ2+µ3, µ3≈0）。Z 基底テスト集合 T（割合 q_T）を新設（AD 後は Z-QBER を直接観測できないため）。統計揺らぎは置換群生成元への McDiarmid 不等式。
- 重要な構造的知見（§2.1.1）: 多光子または真空（ゼロ光子）事象を 1 つでも含むブロックは不安全（Eve がパリティ連鎖から全ビットを決定）。真空パルスは鍵生成から除外し、信号・デコイ強度のみ使用。
- SKL（Eq. 93, 本文 §2.2.2）: ℓ_AD ≤ S⁻_K̄[1 − h(Φ⁺_X̄)] − f·N_K̄·h(Φ_K̄) − log2(2/ε_cor) − 4 log2(·/ε_sec)（S⁻_K̄: 単一光子のみからなる蒸留ブロック数の下界、Φ⁺_X̄: その論理 X 誤り率上界、N_K̄ = ⌊n_K/b⌋[(1−φ_K)^b + φ_K^b]、Φ_K̄ = φ_K^b/[(1−φ_K)^b+φ_K^b]、f=1.2）。非 AD 比較式は Wiesemann et al. の Eq. (94)。
- 数値/結果（§7.3）: ε_sec=10⁻⁹, ε_cor=10⁻¹⁵, η=1, p_noise=0、QBER は misalignment のみ。N=10⁸: 最適 b=3 で 8.7%→11.3%。N=10¹⁴: 最適 b=9 で 9.5%→17.3%。損失耐性 +3.4 dB（p_noise=10⁻⁴）/+2.4 dB（10⁻⁷）、ファイバー約 15 km 延長。
- 本研究への含意: T2 の出発点。パリティ c_A, c_B と IR 情報 λ_IR はいずれも公開。これらを時間ロックした場合の鍵長式が T2 の対象。真空ブロック除外の論法は QCT 下でも必要（Eve が Bob の検出を制御できる点は記憶寿命と無関係）。
- claim候補: [x] 9.5%→17.3%（N=10¹⁴, b=9）、8.7%→11.3%（N=10⁸, b=3）、[x] 真空/多光子含有ブロックは不安全、[x] 既存の decoy+AD 解析 [25][26] は有限サイズ処理が不完全、[x] SNS-TF では成熟した有限鍵 AD 解析が存在 [15]。

## Novak (JSI) 2025, "Security of QKD with One-Time-Pad-Protected Error Correction and Its Performance Benefits", Entropy 27(10):1032 (doi:10.3390/e27101032, PMC12564787, 取得 2026-10-08)
- 主張: 同一 QKD セッションの生鍵の一部を OTP 鍵として誤り訂正データを暗号化しても、固定安全性レベル（ダイヤモンド距離）での鍵率は非保護版と**同一**。利点は計算量（LDPC 符号化問題サイズがシンドローム長の二乗分縮小、PA 圧縮率緩和）。
- 手法: Tomamichel–Leverrier (Quantum 2017) の非漸近証明を拡張。生鍵を X（蒸留用）と O（OTP 用）に分割、Alice と Bob の OTP 鍵は異なる（O ≠ O'）ため、暗号化パリティは「雑音路を通過したパリティ」と等価になり冗長長 r' > r が必要。n−r = n'−r' の調整で鍵率が一致（Eq. 35–36）。min-entropy の鎖律と XOR 構造（Eq. 31–33）で O への依存を消去。**非対話（一方向）EC に限定**、対話型は範囲外と明記。
- 数値/結果: 5G BG1（lifting 224）H 5072×10000、BER 0.09 で成功率 0.99、符号化サイズ比 0.4928。
- 本研究への含意: 「暗号化だけで鍵率は上がらない」の形式的根拠。T2 の利得は暗号化ではなく QCT 仮定（Eve の測定が公開情報に非適応になる）から来る、と主張の構造を変える必要がある。Novak は OTP 鍵の出所を同一セッションに限定しており、計算量鍵（PQC/AES）の場合は対象外。
- claim候補: [x] 同一セッション OTP 保護 EC は鍵率不変、[x] 対話型 EC は未解析、[x] Lo 2003 と Pastushenko–Kronberg 2023 は事前共有鍵/鍵連鎖を要し初期化の安全性が未解析（Novak の批判）。

## Watanabe, Matsumoto, Uyematsu (Tokyo Tech) 2006, "Security of QKD protocol with two-way classical communication assisted by one-time pad encryption" (arXiv:quant-ph/0608030v3, 取得 2026-10-08)
- 主張: 事前共有秘密鍵で OTP 暗号化した双方向前処理（Alice が xMᵀ+s を送り、Bob が差分パリティ t=(x−x̃)Mᵀ を返す）により、消費鍵を差し引いた純鍵率が一方向 QKD を上回り、低誤り率域では Gottesman–Lo の B-step 最適反復をも上回る。
- 手法: 事前共有 EPR 対を補助資源とする双方向 EDP（Vollbrecht–Verstraete の two-way breeding）への帰着。Shor–Preskill 流。6 状態の純鍵率 Eq. (5): 1 − H(q_I,q_X,q_Z,q_Y) + (P_odd/4){H[q_I,q_Z]+H[q_X,q_Y]}。BB84 は α に関する最小化 Eq. (6)。
- 数値/結果: 図 1, 2（脱分極路）。閾値の数値は本文に明記なし（既知値 11%→18.9%/20.0%、12.7%→26.4%/27.6% を引用）。
- 本研究への含意: 「暗号化した双方向前処理」の原型。Alice の生鍵情報が Eve に漏れない点が本質。漸近・鍵連鎖前提・計算量仮定なし。Novak の批判（初期鍵の出所）が同様に適用される。
- claim候補: [x] OTP 支援双方向前処理の純鍵率が一方向を上回る（Shor–Preskill 型漸近証明）、[x] 低誤り率で B-step 最適反復を上回る。

## Pastushenko, Kronberg (Terra Quantum) 2023, "Improving the Performance of Quantum Cryptography by Using the Encryption of the Error Correction Data", Entropy 25:956 (arXiv:2306.12347, 取得 2026-10-08)
- 主張: EC 通信を暗号化し、Eve の量子メモリ・コヒーレンス時間に上界を仮定すると、Eve の情報は Holevo 量 χ ではなく加法的アクセス可能情報 I_acc で抑えられ、鍵率 ≥ I(X:Y) − I_acc(E_E)（Eq. 5）。集団攻撃が個別攻撃より有利でなくなる。
- 手法: Sasaki–Kato–Izutsu–Hirota (1998) の積形式集団のアクセス可能情報加法性定理。EC 開示は符号語集合の開示＝Eve を量子符号化定理の受信者にする（QDL 類似）。PA 通信も遅延または計算量暗号（AES）で保護。
- 限定: 無制限量子資源の Eve に対する合成可能安全性は**提供しない**（著者明記）。PA 後の最適測定が変わりうる例（XOR 後は Bell 測定が最適）を示し、記憶仮定なしの上界は未解決。有限鍵・鍵連鎖の劣化は future work。
- 本研究への含意: T2 の「利得が仮定から来る」構造の原典。QCT（Vyas–Alléaume）と同型の仮定を QKD 後処理に適用した最初の提案だが、証明は漸近的・非合成可能。
- claim候補: [x] 記憶寿命仮定下で χ→I_acc に置換可能、[x] 合成可能安全性は主張しない、[x] PA 通信の OTP 化は鍵率利得を保証しない。

## Vyas, Alléaume (Télécom Paris) 2020, "Everlasting Secure Key Agreement with performance beyond QKD in a Quantum Computational Hybrid security model" (arXiv:2004.10173, 取得 2026-10-08)
- 主張: QCH モデル（計算量暗号は t_comp まで破れない ∧ 量子メモリは t_coh < t_comp で脱コヒーレンス）の下で、MUB-QCT は everlasting 安全な鍵配送を O(√d) 光子まで許容、鍵率 O(√d) 倍、距離 +25 km×log d。
- 手法: 基底 θ を短期安全暗号 E_k で時間ロック。Eve の最適戦略は「即時測定＋事後復号」（命題 1: P_guess(S1) > P_guess(S2)）= 事後測定情報付き状態識別（Ballester–Wehner–Winter）。安全性基準はアクセス可能情報 I_acc ≤ H(X) − H_min(X|Z) と全変動距離 ∆（Alicki–Fannes / Pinsker で結合、Eq. 7–8）。トレース距離ではない。
- 数値/結果: 付録 A で光学量子メモリのコヒーレンス時間は 1 s 未満、AES256 は数十年を想定（t_coh=O(1 s) vs t_comp=O(10⁹ s)）。
- 本研究への含意: T2 の仮定モデルの正典。everlasting 性は「プロトコル実行時に QCH が成立すれば十分」。T2 では時間ロック対象を「AD パリティ＋IR 情報（＋基底公開の遅延 τ_ann）」とし、安全性定義を QCT 型（Eve の事後状態が古典）に合わせる必要がある。
- claim候補: [x] QCH の定義、[x] 最適攻撃は即時測定＋事後復号、[x] 安全性は I_acc/全変動距離基準、[x] t_coh<1 s の技術評価。

## Jiang, Hu, Yu, Wang (Tsinghua) 2021, "Composable security for practical QKD with two way classical communication" (arXiv:2102.00739, 取得 2026-10-08)
- 主張: SNS-TF-QKD の双方向誤り棄却（ランダム 2 ビット対のパリティ比較）において、untagged ビットのタグ付けが非独立である問題を「全ビットが i.i.d. な仮想集合」への帰着で厳密化。Chernoff 界をそのまま使えば鍵率は正しく、失敗確率は定数倍（Result 2.1: 2 倍、Theorem 1: 1/γ_iid 倍）になるだけ。
- 手法: 白玉/黒玉モデル。[k,N] 集合と [p_u=k/N,N]_iid 集合の ww 対数の失敗確率比較（Lemma 1 単調性）。
- 本研究への含意: AD ブロック化後の単一光子ブロック数下界 S⁻_K̄ の有限鍵評価に流用可能（Treplin は McDiarmid を採用、Jiang は仮想 IID＋Chernoff）。被引用 33 で実験系（1002 km TF, 微小衛星）が採用。
- claim候補: [x] 仮想 IID 帰着で失敗確率は 2 倍、[x] 鍵率は Chernoff 直接適用と同一。

## 文献間の一致・矛盾・空白
- 一致: Treplin/Jiang は AD の有限鍵を扱うが EC/AD 通信は公開。Novak/Watanabe/P-K は暗号化を扱うが漸近または一方向限定。Vyas は仮定モデルを与えるが AD も後処理暗号化も扱わない。
- 矛盾: P-K（暗号化で鍵率向上）vs Novak（同一セッション OTP なら不変）。解消: P-K の利得は記憶寿命仮定から、Novak は無仮定・同一セッション鍵。両立する。
- 空白（T2）: QCT 仮定下で AD パリティ・IR 情報を時間ロックした decoy-BB84 の有限鍵率。真空ブロック除外（Treplin）、仮想 IID（Jiang）、即時測定帰着（Vyas）、I_acc 置換（P-K）の 4 部品を合成した証明は存在しない。
## 外部参照（抄録のみ確認、本文未読: 2026-10-08, arXiv API）

### Fuchs, Gisin, Griffiths, Niu, Peres 1997, "Optimal Eavesdropping in Quantum Cryptography. I" (arXiv:quant-ph/9701039; PRA 56, 1163)
- 主張: BB84 に対し、一方の基底の誤り率を固定したときの他方の基底のアクセス可能情報の上界を導出。2 量子ビットプローブで両界を同時達成。信号ごと（個別攻撃）に対する情報–擾乱の最適曲線。
- 本研究への含意: V-A（基底公開後にプローブを測る個別攻撃）における Eve の古典側情報の上界候補。ただし AD 目的関数に対する最適性は未証明（S3 未解決点）。
- claim候補: [ ] 個別攻撃の最適情報–擾乱曲線（本文の式は未確認）。閾値 14.6% は本文未確認 → PARTIALLY。

### Gisin, Wolf 1999, "Quantum cryptography on noisy channels: quantum versus classical key-agreement protocols" (arXiv:quant-ph/9902048; PRL 83, 4200)
- 主張: 非コヒーレント（個別）盗聴の仮定下で、4 状態・6 状態とも、量子的鍵蒸留と古典的鍵合意（AD）の限界は一致し、Alice–Bob が何らかのもつれを共有する限り秘密鍵が得られる。
- 本研究への含意: 個別攻撃＋AD の到達限界は「もつれ存在」で決まる（BB84 で QBER 25% は本文未確認 → PARTIALLY）。T2（Eve を即時測定に帰着）の漸近上限の目安。
- claim候補: [ ] 個別攻撃下で古典 AD の限界＝もつれ限界。

### Ballester, Wehner, Winter 2008, "State Discrimination with Post-Measurement Information" (arXiv:quant-ph/0608014; IEEE TIT 54, 4183) — コーパス [29]
- 主張: 測定後に状態集合の情報（基底）が与えられる識別問題。2 基底では 1 量子ビットの保存で任意のブール関数を完全計算可能、3 基底では全量子ビット保存が必要。AND/XOR の最適成功確率。
- 本研究への含意: V-B（基底公開を τ_ann > t_coh だけ遅延）での Eve の推測確率の定式化。2 基底 BB84 で「1 量子ビット保存で完全」という結果は、t_coh 内に 1 量子ビットでも保持できれば V-B の優位が崩れることを示唆（仮定 A1 を「記憶ゼロ」に強める必要）。
- claim候補: [x] 2 基底では 1 量子ビット保存で任意ブール関数を完全計算可能（抄録）。

### Tomamichel, Fehr, Kaniewski, Wehner 2013, "A monogamy-of-entanglement game with applications to device-independent quantum cryptography" (NJP 15, 103002; 抄録は Culf–Vidick 2022 arXiv:2107.13324 と Broadbent–Culf 2021 arXiv:2111.08081 経由で技術の所在を確認)
- 主張（二次確認）: BB84 状態の単婚ゲームで並列反復の最適勝率を導出、一方向 DI-QKD に応用。Broadbent–Culf は剛性と「擬似乱数関数の一時的仮定のみに依る everlasting 乱数拡張」を示す。
- 本研究への含意: 「計算量仮定は一時的、出力は everlasting」の枠組みの先例。Grilo–Malavolta–Walter–Zhang 2025（arXiv:2510.00791）は秘密が計算量的にのみ隠された単婚ゲームで無視できる勝率を証明。T2 の V-B は「基底が τ_ann の間だけ隠される単婚ゲーム」と読める。
- claim候補: [ ] 単婚ゲームの勝率上界（原論文未読 → UNVERIFIABLE のまま本文で未検証と明記）。

### Fung, Ma, Chau, Cai 2012, "QKD with delayed privacy amplification…" (arXiv:1111.4411; PRA 85, 032308) — 抄録のみ、2026-10-08
- 主張: PA を最終鍵の OTP 使用後まで遅延しても安全性・鍵率は不変。二方向量子チャネル QKD の証明簡略化と信頼中継網に応用。
- 本研究への含意: 「遅延は無利得」の先例（Novak の暗号化版と対）。T2 の利得が A1（記憶寿命）由来であることの補強。
- claim候補: [x] 遅延 PA は安全性・鍵率を変えない。

### IACR ePrint 2026/1359 (Radhakrishnan), "Optimization of Hardware Architecture for QKD" — 2026-10-08
- 主張: パイプライン型 FPGA で QKD 後処理を省エネ加速。AD への言及なし。
- 本研究への含意: 新規性 3（AD の実時間実装は不在）の 2 経路目。

### Bocquet, Alléaume, Leverrier 2011, "Optimal eavesdropping on QKD without quantum memory" (arXiv:1106.0329, 取得 2026-10-09, vault note `optimal-eavesdropping-on-qkd-without-quantum-memory`)
- 主張: 量子メモリのない Eve の最適戦略は、sifting で公開される基底を事後測定情報として使う POVM でアンシラを測ること。相互作用 U と POVM を共に最適化し、鍵が抽出できる最大 QBER を BB84 15.4%（個別攻撃 14.6%、[17] と一致）、六状態 20.4%（集団 12.6%、個別 15.6%）、SARG04 17.6%（個別 14.8%）と算出。
- 手法: 対称攻撃の純化を QBER 条件付きで列挙し、Shannon 相互情報量 I_AE を POVM について最適化。前方和解。
- 本研究への含意: P1″ の b=1 部分は既知。QCT は「メモリなし」を「遅延 > t_coh」で運用的に実現。本研究の未踏部分は AD ブロック（b≥2）との合成と、集団・結合測定下での挙動。
- claim候補: [x] 上記閾値（本文確認済）。

## 文献間の一致・矛盾・空白（改訂）
- 追加の空白: 個別攻撃下の AD（Gisin–Wolf, Maurer）は漸近・i.i.d. 前提。有限鍵・decoy・非 i.i.d. 即時測定への拡張はない。
