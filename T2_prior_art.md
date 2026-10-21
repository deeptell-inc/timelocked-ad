# T2 先行事例調査: 双方向蒸留 × PQC/OTP暗号化和解 × 有限鍵合成可能証明 × FPGA

調査日: 2026-10-08。情報源: arXiv API、Semantic Scholar API（引用連鎖）、OpenAlex、Web検索。`[i]` は元コーパス（export-ris-33/34）の通し番号、`(arXiv:…)` は新規に見つけた外部文献。

## 0. 結論（先に）

T2 を「4要素の同時統合」として定義した場合、その統合自体は未着手である。ただし T2 の部品のうち 2 つは 2025–2026 年に先行研究が存在し、当初の定式化を修正する必要がある。

| T2 の要素 | 先行状況 | 新規性への影響 |
|---|---|---|
| (A) 双方向蒸留（AD）の有限鍵・合成可能証明 | **既存**。decoy BB84+AD の有限鍵解析で許容QBER 9.5%→17.3% (arXiv:2511.21665, 2025)。SNS-TF の双方向誤り棄却の合成可能有限鍵 (arXiv:2102.00739, 2021)。QCKA+CAD の一般コヒーレント攻撃有限鍵 (Krawec 2025)。 | 「初の有限鍵AD証明」は主張不可。T2 の数値目標（11%→18–27%）は既に 17.3% まで達成済み |
| (B) 和解データの暗号化 | **半分既存、かつ負の結果あり**。OTP 保護誤り訂正は同一セッション鍵を使う限り鍵率が**変わらない**ことが証明済み (Novak, Entropy 2025)。鍵率が上がるのは Eve の量子メモリ寿命を仮定した場合 [193] または計算量タイムロック (QCT, arXiv:2004.10173 / 2311.09164) のみ | 「PQC で和解を暗号化すれば鍵率が上がる」は誤り。利得は**仮定モデル**（QCT 型）から来る。T2 は QCT モデルと明示的に接続する必要がある |
| (C) 双方向通信 + OTP 前処理 | **既存（2006）**。事前共有鍵による OTP 支援の双方向前処理で純鍵率が増加 (Watanabe–Matsumoto–Uyematsu, arXiv:quant-ph/0608030) | 「暗号化した双方向後処理」の原型。ただし漸近・Shor–Preskill 型で、有限鍵でも計算量仮定でもない |
| (D) AD の FPGA/実時間実装 | **不在**。FPGA 蒸留エンジンは全て一方向 (Walenta 2014, Constantin 2017 [93], Li/Yan/Mao 2018–2025, Shingala 2022, [661])。AD の実装論文はゼロ | 実装面の新規性は完全に残っている |
| (E) PQC を和解の搬送に使う | **1件のみ** [299] (Djordjevic 2020、漸近、合成可能性なし)。衛星系ハイブリッド (arXiv:2502.14240 → [868]) は PQC/AES を「命令列」保護に使い、和解には使わない | 合成可能な形での扱いは未着手 |

**再定式化した T2**: 「QCT（量子計算量タイムロック）仮定の下で、PQC 暗号化した双方向蒸留（AD）の通信を持つ decoy-BB84 の有限鍵・合成可能鍵率を導出し、鍵率利得が (i) AD による QBER 耐性拡大と (ii) タイムロックによる和解漏洩の消去の二重効果として現れることを示し、FPGA 実時間エンジンで検証する」。先行研究 (A)(B)(C) はそれぞれ単独の要素であり、三者の合成と (D) はいずれも未着手。

## 1. 要素 A: 双方向蒸留（advantage distillation）の安全性証明

### 1.1 漸近・古典群（コーパス内 + 外部）
- Gottesman–Lo 2003 [3] (arXiv:quant-ph/0105121): B-step/P-step、BB84 18.9%、6状態 26.4%。
- Chau 2002 (arXiv:quant-ph/0205060): 27.6% 閾値。
- Ma–Fung–Dupuis–Chen–Tamaki–Lo 2006 (arXiv:quant-ph/0604094): decoy + 双方向後処理（AD を decoy に適用した原典）。
- Kraus–Branciard–Renner 2007 [24]: 情報理論的手法での双方向鍵率、6状態 0.276。
- Watanabe–Matsumoto–Uyematsu 2007 (arXiv:0705.2904): ハッシュ化双方向通信の鍵率。
- Renner–Gisin–Kraus 2005 [1]: 一方向 + ノイズ前処理。

### 1.2 DI/半DI 群（Lütkenhaus–Tan 系列）
- Tan–Lim–Renner, PRL 2020 (arXiv:1903.10535): DIQKD に AD（repetition code）、IID 集団攻撃。
- Hahn–Tan 2021 (arXiv:2105.03213): 忠実度に基づく十分/必要条件。
- Stasiuk–Lütkenhaus–Tan 2022 (arXiv:2212.06975): 量子 Chernoff ダイバージェンスで十分条件と必要条件を一致させる（IID）。
- Hahn–Tan–Brown 2024 (arXiv:2408.12313): Petz–Rényi 界。
- Bhavsar–Moon–Bae 2026 (arXiv:2602.05870): 仮説検定との厳密な接続。小〜中ブロック長で鍵率改善、「有限ブロック長の正確な条件は未解決」と明記。

### 1.3 有限鍵・合成可能（T2 と最も競合）
- **Jiang–Hu–Yu–Wang 2021 (arXiv:2102.00739)**: SNS-TF-QKD の双方向誤り棄却（2ビット群のタグ付けが非独立）に対し、仮想 IID 集合を介して Chernoff 界で有限鍵を厳密化。被引用 33、TF-QKD 1002 km 実験 (arXiv:2402.00005) や微小衛星 QKD (arXiv:2408.10994) が採用。**合成可能・有限鍵の双方向後処理はここで既に実運用レベル**。
- **Treplin–Kleinpaß–Orsucci 2025 (arXiv:2511.21665)**: decoy-BB84 + AD の「初の包括的有限鍵解析」。現実的鍵長で許容 QBER 約9.5%→約17.3%。被引用 3（2026 の WDM-decoy+AD、S-CAD、Krawec）。
- Krawec 2025 (QCKA + CAD, s44354-025-00005-y / arXiv:2503.24318): 量子サンプリング枠組みで一般コヒーレント攻撃の有限鍵証明。
- Krawec 2026 (arXiv:2601.02565): decoy+CAD の真空事象のエントロピー評価改善（漸近）。
- Thomas–Krawec–Wang 2026 (arXiv:2605.02588): S-CAD（選択的 CAD）、一般コヒーレント攻撃の漸近証明。
- Kawakami ら 2026 (arXiv:2607.04538): QCKA の B/P-step 反復で 20% 超（漸近）。
- Du–Liu–Zhang–Ma 2024 (QST 2025, arXiv:2404.14733): AD の統一枠組み。「OTP を後処理に使わない場合に線形符号で鍵率向上」と述べ、**OTP 使用の有無が鍵率に効く**ことを示唆（要素 B と接続）。
- Sun–Goodenough–Bhatti–Elkouss, PRA 2025 (arXiv:2410.19334): 量子もつれ蒸留 + CAD の二段構成。

### 1.4 変種への展開（漸近）
TF-QKD (arXiv:2202.10059, Quantum 2023: 420→470 km)、MP-QKD (arXiv:2304.03534)、AMDI (arXiv:2407.03980)、INI-QKD (arXiv:2410.00205)、CV-QKD ランダム符号帳 AD で Devetak–Winter と PLOB を超える (Ray–Skoric, arXiv:2402.04770)、DI-QSS (arXiv:2605.21880)。

**判定**: 「AD の有限鍵証明」は 2021 年（SNS-TF）と 2025 年（decoy-BB84）に存在。T2 がこの軸で主張できるのは「PQC 暗号化通信を含む AD」と「QCT 仮定下」の有限鍵のみ。

## 2. 要素 B/C: 和解データ・双方向通信の暗号化

### 2.1 直接の先行
- **Watanabe–Matsumoto–Uyematsu 2006 (arXiv:quant-ph/0608030)**: 事前共有鍵で OTP 支援した双方向前処理。純鍵率が非支援版を上回る。双方向ブリーディング（事前共有 EPR 対）への帰着で Shor–Preskill 流に証明。→ T2 の「暗号化した双方向後処理」の原型。計算量仮定なし、有限鍵なし。
- **Pastushenko–Kronberg 2023 [193]** (arXiv:2306.12347, 被引用 27): 誤り訂正データを暗号化し、Eve の量子メモリ・コヒーレンス時間の仮定下で鍵率改善。QDL との類似を自認。
- **Novak, Entropy 27(10):1032, 2025** (doi:10.3390/e27101032): Tomamichel–Leverrier の非漸近枠組みを OTP 保護 EC に拡張。**同一セッションのエントロピープールから OTP 鍵を取る限り鍵率は非保護版と同一**（ダイヤモンド距離で定義した固定安全性レベルで）。利点は LDPC 符号化問題サイズの縮小（シンドローム長の二乗分）と PA 圧縮率の緩和。→ **鍵率利得は暗号化そのものからは出ない**という明確な負の結果。
- Du ら 2024 (arXiv:2404.14733): 「OTP を後処理に使わない場合」に線形符号で改善、という記述は上と整合。

### 2.2 鍵率利得が出る仮定モデル
- **QCT（量子計算量タイムロック）**: Vyas–Alléaume 2020 (arXiv:2004.10173) が「計算量安全な暗号は量子メモリのコヒーレンス時間より長い時間の後にしか破れない」と仮定する QCH モデルを導入、MUB-QCT で everlasting 鍵配送、O(√d) 光子まで許容。Mazzoncini–Bauer–Brown–Alléaume, Quantum 9:1862 (2025, arXiv:2311.09164) は Hidden Matching 問題に帰着した HM-QCT で IID 攻撃に対する安全性を証明。[724] がこれを HAKE 評価に含める。
- 有界/雑音量子記憶モデル: Damgård–Fehr–Salvail–Schaffner 2005 (arXiv:quant-ph/0508222)、Damgård–Fehr–Renner–Salvail–Schaffner 2007 (arXiv:quant-ph/0612014)、König–Wehner–Wullschleger IEEE TIT 2012 (arXiv:0906.1030)、Schaffner–Terhal–Wehner 2009。DI 版 (arXiv:1211.1402)。
- 量子データロッキング: DiVincenzo ら 2004 (arXiv:quant-ph/0303088)、Lupo–Lloyd PRL 2014 (arXiv:1406.4418)、Lupo 2015 Entropy（時間制限記憶）。
- everlasting / 計算量仮定からの QKD: Malavolta–Walter 2023 (arXiv:2304.02999、2メッセージ QKD、PQ-OWF のみ)、Grilo–Malavolta–Walter–Zhang TCC 2025 (arXiv:2510.00791、計算量的もつれ単婚性)、Metger–Dulek–Coladangelo–Arnon-Friedman [80]、Merkulov–Arnon [325]（EAT を計算量仮定下へ）。

**判定**: T2 が「PQC で和解を暗号化して鍵率を上げる」と言うなら、Novak 2025 により同一セッション鍵版は却下される。生き残る定式化は (i) QCT 仮定下（PQC が量子メモリ寿命内だけ安全であればよい）、または (ii) [193] の記憶寿命仮定、のどちらかを明示し、AD と合成することである。(i) は Alléaume 系列と直接競合するが、同系列は AD も FPGA も扱っていない。

## 3. 要素 D: FPGA / 実時間後処理

- Walenta ら NJP 2014 (arXiv:1309.2583)、Constantin ら 2017 [93]: COW 用、4 Mbps、有限鍵・認証コスト込み。一方向 FEC。
- Zhang ら 2013 (arXiv:1301.2383): FPGA 実時間 QKD。
- Li–Yan–Mao 系列: FFT 型 PA (arXiv:1809.07592, 2018)、大規模高速 PA (arXiv:2107.01013, 2021)、**10⁸ ビット超 PA (Cheng–Mao–Xu–Li, arXiv:2503.09331, 2025, Xilinx XCKU095)** — 有限サイズ効果対策としての大ブロック PA は T2 の有限鍵実証に直接使える。
- Shingala ら 2022 (arXiv:2211.17019): HLS/MapReduce 型の多プロトコル蒸留、動的 EC、サイドチャネル耐性認証。
- [661] 2026: Rudraksh（軽量 PQC）を QKD 後処理に統合した FPGA。「PA の研究は少なく、PQC 連携は未開拓」と自認。
- Kiktenko ら [53]: 認証鍵消費 <1%（UC 枠組み）。
- 衛星向け最小計算 [27]。

**判定**: AD（repetition code、B/P-step、ブロック後選択）の FPGA 実装は検索で 0 件。AD は「ブロック化 → 後選択 → 残りを LDPC」という追加パイプライン段を要し、Jiang ら 2021 が指摘する「タグ付けの非独立性」を有限鍵パラメータ推定にリアルタイムで反映する必要がある。ここは完全に空白。

## 4. 要素 E: PQC を後処理内部で使う既存例

- [299] Djordjevic 2020: PQC で parity を搬送、SC-LDPC を和解と McEliece で共用、TF-QKD 1238 km（漸近、PQC 破壊計算量を鍵率に算入）。
- [868] Gupta ら 2026 と前身 Rani ら 2025 (arXiv:2502.14240): BBM92 + AES の二重保護、「専用誤り和解符号」で安全性/鍵率トレードオフ最適化。PQC/AES は命令列の保護であり和解の暗号化ではない。
- [20][52][824]: PQC は認証のみ。[408][250][443][867]: 信頼ノード保護。
- HAKE: Muckle（Dowling–Hansen–Paterson 2020）、Muckle+（Bruckner–Ramacher–Striecks PQCrypto 2023）、Muckle#（Battarbee–Striecks–Perret–Ramacher, arXiv:2411.04030、KEM 暗黙認証）、MACsec 適用 [422]、評価 [724]。いずれも鍵確立層の結合であり、QKD 後処理内部には入らない。

**判定**: 合成可能枠組みで「PQC 暗号化された和解/AD 通信」を扱った例はない。

## 5. T2 の再設計案

1. **仮定モデルの明示**: QCT 仮定（Alléaume 系列）を採用し、「PQC 暗号化は量子メモリ寿命 τ の間だけ安全」とする。Novak 2025 の等価性定理を回避するには、OTP ではなく計算量暗号で和解・AD 通信を保護し、Eve の攻撃を τ 後の即時測定＋古典事後復号に帰着させる必要がある。
2. **証明の骨格**: Treplin ら 2025 の decoy-BB84+AD 有限鍵解析を出発点に、AD ブロック内の通信（parity, accept/reject）を QCT で隠した場合の Eve の情報を、[193] と同型の「測定後復号」として評価。Jiang ら 2021 の仮想 IID 技法で非独立タグ付けを処理。合成可能性は Tomamichel–Leverrier（Novak が拡張した枠組み）に乗せる。
3. **数値目標の更新**: 一方向 9.5% → AD 17.3%（既存）→ AD+QCT で何%か、が T2 の新しい主張。27.6% (Chau) が漸近上限の目安。
4. **実装**: Cheng ら 2025 の 10⁸ ビット PA FPGA + Constantin/Walenta 型蒸留エンジンに AD 段を追加。PQC 暗号化は [661] の Rudraksh か ML-KEM 派生の軽量 KEM で、τ（ms〜s）内に完了する遅延予算を明示。
5. **差別化の一文**: 「AD の有限鍵証明（2025）、OTP 保護 EC の非利得定理（2025）、QCT モデル（2020–2025）は各々存在するが、三者を合成して『計算量タイムロック下の双方向蒸留』の有限鍵率を導き、実時間 FPGA で検証した研究はない。」

## 6. 参照リスト（外部、arXiv ID 順）

quant-ph/0105121 Gottesman–Lo / quant-ph/0205060 Chau / quant-ph/0303088 DiVincenzo ら / quant-ph/0508222 Damgård ら / quant-ph/0604094 Ma ら / quant-ph/0608030 Watanabe ら / quant-ph/0612014 Damgård ら / 0705.2904 Watanabe ら / 0906.1030 König ら / 1211.1402 / 1301.2383 Zhang ら / 1309.2583 Walenta ら / 1406.4418 Lupo–Lloyd / 1809.07592 Li ら / 1903.10535 Tan–Lim–Renner / 2004.10173 Vyas–Alléaume / 2102.00739 Jiang ら / 2105.03213 Hahn–Tan / 2107.01013 Yan ら / 2202.10059 Li ら / 2211.17019 Shingala ら / 2212.06975 Stasiuk ら / 2304.02999 Malavolta–Walter / 2304.03534 / 2306.12347 Pastushenko–Kronberg / 2311.09164 Mazzoncini ら / 2402.04770 Ray–Skoric / 2404.14733 Du ら / 2407.03980 / 2408.12313 Hahn ら / 2410.00205 / 2410.19334 Sun ら / 2411.04030 Battarbee ら / 2502.14240 Rani ら / 2503.09331 Cheng ら / 2503.24318 Krawec / 2510.00791 Grilo ら / 2511.21665 Treplin ら / 2601.02565 Krawec / 2602.05870 Bhavsar ら / 2605.02588 Thomas ら / 2605.21880 / 2607.04538 Kawakami ら。
非 arXiv: Novak, Entropy 27(10):1032 (2025) doi:10.3390/e27101032; Krawec, s44354-025-00005-y (2025); Dowling–Hansen–Paterson, Muckle (2020); Bruckner–Ramacher–Striecks, Muckle+ (PQCrypto 2023).

## 7. 留保

- Semantic Scholar はレート制限のため被引用連鎖は 2102.00739（33 件）、2511.21665（3 件）、2306.12347（27 件）、2404.14733（8 件）のみ取得。2004.10173 と Novak 2025 の被引用は未取得。
- Novak 2025 は Web 検索の要約と抄録に基づく。等価性定理の正確な前提（OTP 鍵の出所、安全性定義）は本文で確認が必要。
- 「AD の FPGA 実装ゼロ」は arXiv 検索に基づく。IEEE/Optica の会議論文に未索引の実装がある可能性は残る。
