---
asset: claims-ledger
version: 2.0.0
生成元入力: knowledge/claims-ledger.md スキーマ（~/methodology）
依存工程: S17（追記元）
生成日: 2026-10-08
更新責任工程: S17（追記）/ S7・S8（引用整合の突合）
---

# claims-ledger — 主張台帳（T2 プロジェクト）

スキーマ: claim / 種別 / 判定 / 出典URL/DOI / 確認日 / 反証探索。SUPPORTED は一次出典＋反証探索「有」が必須。新規性・主要数値は独立 2 経路まで PARTIALLY。

## 台帳

| claim | 種別 | 判定 | 出典URL/DOI | 確認日 | 反証探索 |
|---|---|---|---|---|---|
| decoy-BB84+AD の有限鍵解析で、N=10¹⁴, b=9 のとき許容 QBER が 9.5% から 17.3% に増加する（ε_sec=10⁻⁹, ε_cor=10⁻¹⁵, η=1, p_noise=0, f=1.2） | 数値/事実 | PARTIALLY | https://arxiv.org/abs/2511.21665 §7.3, §8 | 2026-10-08 | 有（同一出典内の 2 箇所で一致。独立 2 経路目は未取得 → PARTIALLY 固定） |
| 同条件で N=10⁸ のとき最適 b=3 で 8.7% から 11.3% | 数値/事実 | PARTIALLY | 同上 §7.3 | 2026-10-08 | 有（同上） |
| AD において多光子または真空事象を 1 つでも含むブロックは不安全であり、鍵生成から除外する | 因果 | SUPPORTED | 同上 §2.1.1 | 2026-10-08 | 有（Jiang ら 2021 は SNS-TF で untagged ビットのみを数える同型の扱い） |
| Treplin ら以前の decoy-BB84+AD 解析は有限サイズ効果の扱いが不完全である（著者の主張） | 引用帰属 | SUPPORTED | 同上 §1 | 2026-10-08 | 有（Jiang ら 2021 が SNS-TF に限定した有限鍵 AD を与えており、decoy-BB84 には未適用） |
| 同一 QKD セッションの生鍵を OTP 鍵とする一方向誤り訂正データの暗号化は、固定安全性レベル（ダイヤモンド距離）で鍵率を変えない | 数値/事実 | SUPPORTED | https://doi.org/10.3390/e27101032 §6 Eq. 35–36 | 2026-10-08 | 有（Pastushenko–Kronberg 2023 の反対主張は記憶寿命仮定付きであり矛盾しない） |
| Novak 2025 の解析は非対話（一方向）EC に限定され、対話型 EC は範囲外 | 引用帰属 | SUPPORTED | 同上 §3 | 2026-10-08 | 有 |
| 事前共有鍵で OTP 暗号化した双方向前処理により、6 状態・BB84 の純鍵率が一方向 QKD を上回る（漸近、Shor–Preskill 型） | 数値/事実 | SUPPORTED | https://arxiv.org/abs/quant-ph/0608030 §4–5 Eq. (5),(6) | 2026-10-08 | 有（Novak 2025 は事前共有鍵の出所が未解析と批判。主張自体は両立） |
| Eve の量子メモリ・コヒーレンス時間に上界を仮定すると、Eve の情報は Holevo 量ではなく加法的アクセス可能情報で抑えられ、集団攻撃は個別攻撃より有利でなくなる | 因果 | SUPPORTED | https://arxiv.org/abs/2306.12347 §III Eq. (4),(5) | 2026-10-08 | 有（同論文 §IV が PA 後の最適測定変化の反例を示し、無仮定では不成立と自認） |
| Pastushenko–Kronberg の方法は無制限量子資源の Eve に対する合成可能安全性を提供しない（著者明記） | 引用帰属 | SUPPORTED | 同上 §V | 2026-10-08 | 有 |
| QCH モデル: 計算量暗号は t_comp まで破れず、量子メモリは t_coh < t_comp で脱コヒーレンス。この下で Eve の最適戦略は即時測定＋事後復号 | 定義・用語 | SUPPORTED | https://arxiv.org/abs/2004.10173 §II B, §V B 1 命題 1 | 2026-10-08 | 有（Mazzoncini ら 2025 Quantum 9:1862 が同モデルで別プロトコルを証明） |
| QCT の安全性基準はアクセス可能情報／全変動距離であり、トレース距離ではない | 定義・用語 | SUPPORTED | 同上 §III C Eq. (5)–(8) | 2026-10-08 | 有 |
| 光学量子メモリのコヒーレンス時間は 1 秒未満（2020 年時点の技術評価） | 数値/事実 | PARTIALLY | 同上 §II B（付録 A 参照、本文未読） | 2026-10-08 | 無 |
| SNS-TF の双方向誤り棄却で非独立タグ付けを仮想 IID 集合へ帰着すると、Chernoff 界の鍵率は正しく失敗確率が 2 倍になる | 数値/事実 | SUPPORTED | https://arxiv.org/abs/2102.00739 Result 2.1 Eq. (3),(12) | 2026-10-08 | 有（Treplin ら 2025 は McDiarmid による別経路で同種の量を評価） |
| 非コヒーレント盗聴の仮定下で、4 状態・6 状態とも量子的蒸留と古典的鍵合意の限界は一致し、もつれが共有される限り鍵が得られる | 因果 | PARTIALLY | https://arxiv.org/abs/quant-ph/9902048（抄録のみ） | 2026-10-08 | 無（本文未読） |
| BB84 の個別攻撃では 2 量子ビットプローブが情報–擾乱の最適界を同時達成する | 数値/事実 | PARTIALLY | https://arxiv.org/abs/quant-ph/9701039（抄録のみ） | 2026-10-08 | 無（本文未読） |
| 2 基底の事後測定情報付き識別では 1 量子ビットの保存で任意のブール関数が完全計算できる | 数値/事実 | PARTIALLY | https://arxiv.org/abs/quant-ph/0608014（抄録のみ） | 2026-10-08 | 無 |
| **新規性**: QCT 仮定下で AD パリティ・IR 情報を時間ロックした decoy-BB84 の有限鍵率を導出した研究は存在しない | 新規性 | PARTIALLY | T2_prior_art.md（arXiv/S2/OpenAlex/Web 検索, 2026-10-08） | 2026-10-08 | 有（AD 有限鍵: 2511.21665, 2102.00739; 暗号化 EC: e27101032, 2306.12347; QCT: 2004.10173 — いずれも単独要素。IEEE/Optica 会議未索引の可能性は残る） |
| **新規性**: AD の FPGA/実時間実装は存在しない | 新規性 | SUPPORTED | T2_prior_art.md §3（arXiv 検索）＋ Web 検索 2026-10-08（IEEE/IACR/ResearchGate: 2211.17019, JLT 38:3935 CV-QKD FPGA, IACR ePrint 2026/1359 — いずれも AD なし） | 2026-10-08 | 有（2 経路。IEEE Xplore 全文検索は未） |
| PA を一時パッド使用後まで遅延しても QKD の安全性と鍵率は変わらない（Fung–Ma–Chau–Cai 2012） | 引用帰属 | SUPPORTED | arXiv:1111.4411 抄録; PRA 85, 032308 | 2026-10-08 | 有（Novak 2025 と整合: 遅延/暗号化単独は無利得） |
| **新規性**: 利得の機構は暗号化ではなく公開遅延 τ_ann > t_coh と同値であり、PQC は遅延圧縮として働く | 新規性 | PARTIALLY | theory-foundation.md 拡張 1（P-K 2023 §III が「遅延」を同等の手段として言及） | 2026-10-08 | 有（Novak 2025 が暗号化単独の無利得を証明） |

| （更新）decoy-BB84+AD の有限鍵許容 QBER: N=10¹⁴ b=9 で 9.5%→17.3%、N=10⁸ b=3 で 8.7%→11.3% | 数値/事実 | SUPPORTED | T25 §7.3 ＋ 独立再実装 impl/qct_ad（8.67/11.37/9.53/17.30%） | 2026-10-08 | 有（2 経路: 原典本文と独立再計算が 0.1 pt 以内で一致） |
| QCT V-A モデル（i.i.d. 対称個別攻撃、基底公開後にプローブ測定、後処理メッセージは t_coh 後に公開）で、N=10¹⁴, b=9, ε_sec=10⁻⁹, f=1.2 の許容 QBER は min-entropy 版 20.7%、Shannon+AEP 版 21.9% | 数値/事実（主要） | PARTIALLY | impl-report.md §3, data/threshold_table_quick.csv | 2026-10-08 | 有（漸近計算 asymptotic.py で b=9: 22.7% と整合。2 経路目＝独立実装は未） |
| 同モデルの漸近閾値は b→∞ で Gisin–Wolf のもつれ限界 1/4 に下から近づく（b=31, f=1: 24.25%） | 数値/事実 | PARTIALLY | data/asymptotic_thresholds.csv | 2026-10-08 | 有（GW 定理 1 の等号を D=1/4 で数値確認） |
| 全 b スキャン（最終コード）で T25-AD 列は各 N で漸近閾値を下回り N=10¹⁴ では b=9 が最大（17.30%）；QCT min-ent の最大は 21.83%（b=15）、Shannon+AEP の最大は 21.89%（b=9） | 数値/事実 | PARTIALLY | data/threshold_table.csv | 2026-10-08 | 有（漸近表と整合、T25 の「b=9 最適」と一致） |
| QCT V-A 式は Eve 項以外 T25 Eq. 93 と同一であり、A2 不成立時は T25 式に還元する（P2） | 因果 | SUPPORTED | impl/qct_ad/skl.py（skl_qct_ad vs skl_ad） | 2026-10-08 | 有（構成による） |
| AD 段の演算量は原鍵 1 ビットあたり 1 XOR 未満であり、LDPC 復号（数百演算/ビット）に対し 1% 未満 | 数値/事実 | PARTIALLY | impl/qct_ad/latency_budget.py（桁推定） | 2026-10-08 | 無（FPGA 合成未実施） |

| 主要数値 20.7%/21.9%（N=10¹⁴, b=9）は、ブロック計数統計を McDiarmid（T25 Eq.18）から Jiang 仮想 IID＋Chernoff に替えても 0.001 pt 以内で不変；N=10⁸, b=3 では 14.0→14.1%、16.2→16.2% | 数値/事実 | PARTIALLY | data/second_route_jiang.csv | 2026-10-08 | 有（統計経路の独立性は確認。Eve 項・decoy 項は共通のため「独立 2 経路」としては不完全） |

| T25 Eq. 19 の単調性は付録 B で φ_X+φ_Z<1/2 の領域に限って証明されている；領域外（例 φ_X=0.3, φ_Z: 0.3→0.5, b=7 で 0.499→0.25）では非単調で、制約なし最適化はテスト集合を潰して領域外に出る。実装は φ⁺_X+φ⁺_Z<1/2 を受理条件として課す必要がある。T25 の 4 公表値は領域内で不変 | 数値/事実（本研究の指摘） | SUPPORTED | T25 付録 B（note 行 3186–3204: 条件 0<φx,φz<1/2, φx+φz<1/2）; impl-report.md §4 | 2026-10-08 | 有（原文で領域条件を確認。T25 の誤りではなく適用条件の明示） |

| 双方向後処理で BB84 は 18.9%、6 状態は 26.4% の QBER まで安全（Gottesman–Lo）、Chau は 27.6% | 数値/事実（背景引用） | SUPPORTED | コーパス [3] 抄録（IEEE TIT 49, 457）; Watanabe 2006 §1; T25 §1 | 2026-10-08 | 有（3 独立文献で一致） |
| 4 状態プロトコルで Bob と Eve の情報が等しくなる QBER₀=(1−1/√2)/2≈14.6%（個別攻撃、Shannon 最適） | 数値/事実（背景引用） | SUPPORTED | GW 1999 本文（note 行 173–182）; asymptotic.py b=1, f=1 で 14.64% を再現 | 2026-10-08 | 有（2 経路） |
| 個別攻撃下で AD による鍵合意が可能 ⇔ D/(1−D) < 2√(δ₀(1−δ₀))、4 状態で D<1/4、6 状態で 1/3（Gisin–Wolf 定理 1） | 因果 | SUPPORTED | GW 1999 本文 Eq. (8),(9),(11)（note 行 316–365） | 2026-10-08 | 有（skl.py で等号を D=1/4 で数値確認） |
| 有限 AEP（TCR09 定理 9）: (1/n)H_min^ε(Aⁿ|Bⁿ) ≥ H(A|B) − δ(ε,η)/√n、δ = 4 log η √(log(2/ε²))、η = √2^{−H_min}+√2^{H_max}+1、n ≥ (8/5)log(2/ε²)。二値 A では η ≤ 2+√2 | 数値/事実（背景引用） | SUPPORTED | arXiv:0811.1221 本文 Theorem 9, Eq. (30)（note 行 748–764）、η 定義（行 622–625） | 2026-10-08 | 有（実装 aep_penalty と一致を確認） |

| QCT V-A の漸近閾値（単一光子源, f=1）は b=1 で 14.64%、b=9 で 22.87%、b=31 で 24.25%；T25-EUR（反復符号 AD）は b=21 で 18.9% を最大に飽和 | 数値/事実 | PARTIALLY | data/asymptotic_thresholds.csv（asymptotic.py） | 2026-10-08 | 有（b=1 値は GW の QBER₀ と一致） |
| 1−I_E（QCT）は 1−h(Φ_X̄)（EUR）より全域で大きく、比は b=1, 17% で約 1.4、b=9 で約 2 桁 | 数値/事実 | SUPPORTED | impl-report §3 前段の表（D=0.17: b=1 0.5418/0.3423, b=9 0.0089/0.0001）＋ fig2 | 2026-10-08 | 有（同一コードの 2 経路: 漸近表と図） |
| t_comp/t_coh の余裕は t_coh ≤ 100 s, t_comp ≥ 1 年で 3×10⁵ 以上 | 数値/事実 | SUPPORTED | data/latency_budget.csv（算術） | 2026-10-08 | 有 |
| QCT V-A で b≥2, D<1/4 では Eve の最悪攻撃は c_φ=1（δ₁=1/2）で達成され、b=1 のみ c_φ<1 の Shannon 最適攻撃が最悪 | 数値/事実 | SUPPORTED | argmax 格子計算（D∈{0.05,…,0.24}, b∈{1,2,3,5,9,15}）2026-10-08 | 2026-10-08 | 有（格子 81 点） |

| ブロック内の非適応結合測定（事後測定情報＝パリティ）の最適成功確率は、b=2,3 の D∈{0.05,…,0.24} で適応 Helstrom 値 ½+½√(1−c_ψ^{2b}) に一致する（SDP、差<10⁻⁵） | 数値/事実（本研究） | PARTIALLY | impl/qct_ad/joint_block_sdp.py（cvxpy/Clarabel） | 2026-10-08 | 有（P_adaptive は定義上の上界であり、SDP 値はそれを下回らないことを確認） |
| 結合測定下では AD による鍵合意の漸近条件が c_ψ² > D/(1−D) ⇔ D < 0.20 となり、Gisin–Wolf の 1/4 は個別測定に依存する | 因果（本研究） | PARTIALLY | reexamination.md §2（代数）; data/joint_thresholds_quick.csv（b=21: 19.6%） | 2026-10-08 | 有（20% は Chau/GL の無条件二方向 BB84 限界と一致） |
| 結合測定下の有限鍵閾値（N=10¹⁴）は b=9 で 17.3–17.5%、b 最良で 17.7%（min-ent, b=11）/18.4%（Shannon, b=7）であり、T25 最良 17.30% に対する利得は ≤1.1 pt | 数値/事実（本研究） | PARTIALLY | data/joint_thresholds.csv | 2026-10-08 | 有（個別測定版 20.7–21.9% との差は測定クラスのみ） |
| BB84 の無条件二方向後処理の許容 QBER は 20.0%（Chau 2002）、6 状態 27.6% | 数値/事実（背景） | PARTIALLY | Watanabe 2006 §1（引用）; T25 §1 | 2026-10-08 | 無（Chau 原典未読） |

| BB84 で基底とパリティを隠しても、攻撃族の最悪点 c_φ=1 では b=1,2 で P_joint = P_ad（差<10⁻⁸）；基底隠蔽は BB84 に利得を与えない | 数値/事実（本研究） | PARTIALLY | data/hidden_basis_sdp.csv（54 点） | 2026-10-09 | 有（c_φ=0 では差があるが Eve の最悪選択は c_φ=1） |
| 六状態（c_φ=0 対称攻撃）で基底を隠すと b=1 で P_joint < P_ad（D=0.167: 0.750 vs 0.833）；Fano 界による一方向漸近閾値は f=1 で 16.7%→22.7%、f=1.2 で 14.2%→17.6% | 数値/事実（本研究） | PARTIALLY | data/sixstate_hidden_basis_b1.csv, _thresholds.csv | 2026-10-09 | 有（既知基底の 16.7% は Fano 界であり Bruß 型最適攻撃の厳密値とは異なり得る） |

| 量子メモリを持たない Eve（sifting 前に測定、事後測定情報として基底を利用）に対する最適攻撃の閾値: BB84 15.4%（個別攻撃 14.6%、集団 11%）、六状態 20.4%（個別 15.6%、集団 12.6%）、SARG04 17.6%（個別 14.8%） | 数値/事実（背景） | SUPPORTED | arXiv:1106.0329 本文 §V–VII（note 行 540–552, 590–600, 690–712） | 2026-10-09 | 有（BB84 の 15.4% は先行 [17] と一致と著者明記） |
| （修正）本研究の b=1 基底隠蔽結果は BAL11 と整合: BB84 は推測確率で差なし（Shannon では BAL11 の +0.8 pt）、六状態は大きな差（Fano 界で 22.7% は BAL11 の厳密 20.4% を上回る楽観値） | 数値/事実（本研究） | PARTIALLY | data/sixstate_hidden_basis_b1*.csv vs arXiv:1106.0329 | 2026-10-09 | 有 |

| 六状態 b=2 同一基底ブロック（基底・パリティ隠蔽）で P_joint = P_ad（0.888644 vs 0.888642、SCS、POVM 検証済） | 数値/事実（本研究） | PARTIALLY | data/sixstate_b2_same_verify.log | 2026-10-09 | 有（2 ソルバのうち SCS で検証、Clarabel は中断） |
| 六状態 b=2 混合ブロック（独立基底、パリティ既知・基底隠蔽）で P=0.8878 vs P_ad=0.8886（D=0.167）、0.9556 vs 0.9583（D=0.259）；AD 併用時の基底隠蔽の利得は推測確率 ≤0.3 pt | 数値/事実（本研究、主要） | PARTIALLY | data/sixstate_b2_mixed_cknown.log | 2026-10-09 | 有（上界であり真の最悪値はさらに小さい差） |
| 結合測定モデルの反復符号 AD 条件 c_ψ²>D/(1−D) は六状態で D<(5−√5)/10=27.6%、BB84 で D<1/5 を与え、Chau の無条件二方向限界と一致する | 数値/事実（本研究） | PARTIALLY | theory-foundation.md J8（代数） | 2026-10-09 | 有（27.6%/20.0% は Chau 2002 の値と一致；原典未読） |

| Bae–Acín 2007: 集団攻撃下で CAD（反復符号 AD）鍵蒸留の必要十分条件は qubit で \|⟨e_mm\|e_00⟩\|²>D/F（Eq. 68, d=2）；BB84 20%・六状態 27.6% が tight；最適攻撃はパリティ公開後に 2 積状態を識別し、適応的個別測定で達成可能 | 数値/事実（背景・先行） | SUPPORTED | arXiv:quant-ph/0610048 本文 §IV–V, Eq. (25),(30),(68)（vault 全文） | 2026-10-09 | 有（Acín et al. 2006 Eq.(5) と整合；Chau 2002 の値と一致） |
| Bae–Acín 2007 §III A/§IV C: メモリ脱コヒーレンスより長い遅延で Eve を個別攻撃に強制でき、その場合 CAD1 は依然 20% で破れるが CAD2（パリティ公開型）の安全条件はもつれ条件 λ₁>1/2（BB84 で 25%）になる | 引用帰属 | SUPPORTED | 同上 §III A（"forced to measure her states before the reconciliation"）, §IV C | 2026-10-09 | 有（本研究の SDP はこの主張が per-copy 測定に限ることを示す） |
| Acín et al. 2006 (PRA 73, 012327 = quant-ph/0411092): 2 量子ビット状態からの SIMCAP 鍵抽出の iff 条件 (λ₁−λ₂)²>(1−λ₁−λ₂)(λ₁+λ₂)；Chau の 27.6% が tight；最適攻撃はコヒーレント操作不要 | 数値/事実（背景） | SUPPORTED | arXiv:quant-ph/0411092 本文 Eq.(5),(17),(23)（vault 全文） | 2026-10-09 | 有 |
| 個別測定モデルの Shannon 情報に多数決誤り率の Fano 式 1−h(γ_b) を使うと Eve の情報を過小評価する（下界）；tally 相互情報量 J_b に置換すると N=10¹⁴ の個別 Shannon 閾値は b=9 で 21.89%→20.86%、最良 20.91%（b=7）；漸近（f=1.2）は b=9 22.7%→21.9%、b=31 24.2%→23.8% | 数値/事実（本研究・訂正） | SUPPORTED | impl/qct_ad/skl.py tally_info, tests/test_skl.py, data/threshold_table.csv, asymptotic_thresholds.csv | 2026-10-09 | 有（J_b≥1−h(γ_b) を格子で検証；結合モデル・T25 列は不変を確認） |
| 結合測定 SDP: b=4（256 POVM 要素、16 次元）でも P_joint=P_ad（差 ≤2×10⁻⁸、D=0.05–0.24 の 7 点） | 数値/事実（本研究） | PARTIALLY | data/joint_block_sdp.csv（目的関数前計算版） | 2026-10-09 | 有（上界 P_ad との一致を確認；第三者再計算なし） |
| 線形決定則 â₁=y₁⊕y′·c を持つ射影測定の最適基底は適応値に b=2,3 で 10⁻¹¹、b=4 で 5×10⁻⁷、b=5 で 2×10⁻⁶、b=6,7 で 10⁻⁵–10⁻⁴（一次最適化、残差減少中）まで到達する；閉形式は未発見（Conjecture 1） | 数値/事実（本研究） | PARTIALLY | data/joint_block_ansatz.log, impl/qct_ad/joint_block_ansatz.py | 2026-10-09 | 有（b=6,7 の残差は最適化収束に律速され、反例ではない） |
| 六状態 b=2 混合ブロック（基底＋パリティ隠蔽）の Eve 成功確率は [0.8826, 0.8878]（D=0.167）、[0.9395, 0.9556]（D=0.259）；旧記述「<10⁻³ bits」は緩和問題の上界を利得の上界と取り違えていた | 数値/事実（本研究・訂正） | PARTIALLY | data/sixstate_mixed_lb.log（下界）, data/sixstate_b2_mixed_cknown.log（上界） | 2026-10-09 | 有（下界は 16 出力射影測定の一次最適化、64 出力版は収束不良） |
| 2 等確率純粋状態の相互情報量は Helstrom 射影測定で最大化される（Levitin 1995; Fuchs 1996 博士論文） | 数値/事実（背景） | PARTIALLY | 書誌のみ（arXiv:quant-ph/9601020 存在確認）；本文未照合 | 2026-10-09 | 無 |
| bounded/noisy-storage モデル（Damgård et al. FOCS 2005; Wehner–Schaffner–Terhal PRL 100, 220502）、Gopal–Wehner PRA 82, 022326、Acín et al. PRA 71, 032338、Bhavsar–Moon–Bae arXiv:2602.05870 の書誌 | 引用帰属 | SUPPORTED | arXiv API（journal_ref）/ OpenAlex で書誌照合 | 2026-10-09 | 有 |

| 定理 1: 実内積 c の 2 純粋状態の b 重積状態族に対し、パリティ事後情報付き非適応測定の最適成功確率は適応 Helstrom 値 ½+½√(1−c^{2b}) に等しく、明示的基底 {X^{ỹ(y′)}Z^{(0,Ly′)}g±}（L = 接頭 XOR）が達成する（旧 Conjecture 1 を証明） | 数値/事実（本研究・定理） | SUPPORTED | theory-foundation.md J9（証明）; impl/qct_ad/joint_block_theorem.py: b=2–9 で直交誤差 ≤10⁻¹³、P−P_ad ≤5×10⁻¹⁵（data/joint_block_theorem.log） | 2026-10-09 | 有（2 経路: 代数的証明と b≤9 の数値検証; SDP b≤4 とも一致） |
| タイムロック下の集団→コヒーレント帰着: post-selection 写像は Eve の測定前に純粋化系へ作用するため制約クラスを保ち、タグ付け（T25）と Pauli ツワール（KGR05）により Bell 対角集団攻撃へ帰着する；φ_X≠φ_Z の 2 パラメータ族に対する I_E 再最大化は未実施 | 因果（本研究・証明スケッチ） | PARTIALLY | theory-foundation.md P6; manuscript Appendix B; CKR09 / KGR05（書誌確認、本文は抄録レベル） | 2026-10-09 | 有（負の結論は帰着に依存しないことを明記） |
| Kraus–Gisin–Renner 2005 (PRL 95, 080501): 一方向後処理 QKD の鍵率の上下界；対称化（ツワール）により集団攻撃を Bell 対角に帰着 | 引用帰属（背景） | PARTIALLY | arXiv:quant-ph/0410215 書誌（journal_ref 確認）; 本文未読 | 2026-10-09 | 無 |

| 六状態 b=3 混合ブロック（基底＋パリティ隠蔽、64 次元・108 クラス）の達成可能下界: D=0.167 で P≥0.9275 (P_ad 0.9301, 誤り率比 ≤1.04)、D=0.259 で P≥0.9736 (P_ad 0.9816, 比 ≤1.43)；b=1: 1.5, b=2: ≤1.05 (D=0.167) | 数値/事実（本研究） | PARTIALLY | data/sixstate_b3_lb.log, impl/qct_ad/sixstate_b3_lb.py | 2026-10-09 | 有（下界は一次最適化・3 シード；D=0.259 は未収束の可能性。指数の同一性は未証明） |

| Bell 対角集団攻撃（ツワール後）の Eve 条件付き状態は §3 と同じ 2 純粋状態構造を持ち c_ψ=(1−2φ_X−φ_Z c_φ)/(1−φ_Z)、c_φ=(λ₃−λ₄)/φ_Z；I_E は φ_X に単調増加、φ_Z には非単調（sup を格子で評価） | 数値/事実（本研究・導出） | SUPPORTED | theory-foundation.md J11（導出）; skl.eve_info_bd（φ_X=φ_Z で旧関数と一致、単調性格子検証） | 2026-10-09 | 有（2 経路: 代数と数値一致） |

| Bell 対角族で再最大化した有限鍵閾値（N=10¹⁴）: 結合モデル b=9 で 17.30%（min-ent）/17.40%（Shannon）、最良 17.66%（b=11）/18.35%（b=7）；個別モデル b=9 で 20.66/20.81%；対称族との差は後続行（≤0.16 pt at 10¹⁴、最大 0.76 pt at 10⁸）を参照 | 数値/事実（本研究・主要） | PARTIALLY | data/bd_thresholds.csv, threshold_table.csv, joint_thresholds.csv（p_guess の最悪化修正後に再計算） | 2026-10-09 | 有（対称族と一般族の 2 計算が 0.15 pt 以内で整合；第三者再計算なし） |

| 2 等確率純粋状態では相互情報量を最大化する測定が Helstrom（誤り最小）測定と一致する（Levitin; Fuchs 1996 博士論文 Chapter 3, Eq. (3.263)） | 数値/事実（背景・結合モデル Shannon 列の根拠） | SUPPORTED | arXiv:quant-ph/9601020 本文 p.89–90, p.96（vault 全文） | 2026-10-15 | 有（Levitin の原典は書誌のみだが Fuchs が独立に再導出・確認） |

| T25 Eq.(93): ℓ_AD ≤ S⁻[1−h(Φ⁺)] − λ_IR − log₂(2/ε_cor) − 4log₂(2^{7/4}/(ε_sec−ε²_sec/8))、Eq.(21) 同形、Lemma 4（leftover hash）、ε̄ = ε²_sec/368（§6）、S⁻ Eq.(18)、Φ⁺ Eq.(19)、φ⁺ Eq.(17a,b)、N_K̄/Φ_K̄ Eq.(20) | 引用帰属（式番号） | SUPPORTED | T25 ノート p.9, p.11–12, p.26（vault 全文） | 2026-10-15 | 有 |
| TCR09: Definition 4 Eq.(24) Υ=2^{−½H_{3/2}}+2^{½H_{1/2}}+1 ≤ √2^{−Hmin}+√2^{Hmax}+1；Theorem 9 Eq.(30) δ(ε,η)=4 log η √(log 2/ε²)、n ≥ (8/5)log(2/ε²) | 引用帰属（式番号） | SUPPORTED | TCR09 ノート p.5–6 | 2026-10-15 | 有 |
| GW99: Eqs.(1)–(2) 攻撃ユニタリ、Eq.(3) F=(1+c_φ)/(2−c_ψ+c_φ)、p.2 ψ/φ 直交部分空間と Z₁=X⊕Y、六状態 c_φ=0、Eq.(7) Bell 対角形、Eq.(8) 1/4、Eq.(11) 定理 1、p.3 定理 1 の証明（Bob の誤り D^N vs Eve の多数決） | 引用帰属（式番号） | SUPPORTED | GW99 ノート p.1–3 | 2026-10-15 | 有 |
| Helstrom 1976（書籍）、Eldar–Megretski–Verghese IEEE TIT 49, 1007 (2003)（最小誤り識別の SDP 定式化）、König–Renner–Schaffner IEEE TIT 55, 4337 (2009)（H_min = −log p_guess） | 引用帰属（背景） | PARTIALLY | arXiv API で書誌確認（quant-ph/0205178, 0807.1338）；本文未読；Helstrom は Fuchs96 Eq.(3.12) 経由で内容確認 | 2026-10-15 | 無 |

| T25 Protocol 1 は基底・ランダム並べ替え・ランダム分割を量子フェーズ後に公開する（step 3, 5） | 引用帰属 | SUPPORTED | T25 ノート p.4（vault 全文）; パネル A・B が独立確認 | 2026-10-19 | 有 |
| 分割を事後情報とする b=2 の最適非適応測定: n=3: 0.8938、n=4: 0.8913、n=6: 0.8884（D=0.1; P_ad 0.8981, P_ind 0.8143） | 数値/事実（本研究） | PARTIALLY | data/hidden_partition_sdp.csv（CLARABEL/SCS） | 2026-10-19 | 有（P_ind<P<P_ad の挟み込み整合；第三者再計算なし） |
| 同一 4 出力実 POVM の per-probe 最適は奇数 b=3,5,7,9 で Helstrom＋tally に一致（J, p_guess とも 10⁻⁶）、偶数 b で p_guess 改善（b=2, D=0.1: 0.8454 vs 0.8143） | 数値/事実（本研究） | PARTIALLY | data/perprobe_opt.csv; パネル A の役割依存 FF 計算（0.858）と整合 | 2026-10-19 | 有（Nelder–Mead 12 再出発、収束保証なし） |
| post-selection 係数を AEP と LHL に課した N=10¹⁴ 閾値: joint Sh 17.80%（b=7）/15.86%（b=9）、collective min-ent 16.67/17.25%、per-probe H Sh 20.52/19.39%、min-ent 19.70/20.61% | 数値/事実（本研究） | PARTIALLY | data/panel_variants.csv; パネル A の独立計算（17.80/15.86/19.39/20.61）と一致 | 2026-10-19 | 有（2 経路一致；PE 区間未縮小） |
| Holevo（量子メモリ、時間ロックなし）Shannon 閾値 N=10¹⁴: 16.40/16.76/15.59%（b=5/7/9） | 数値/事実（本研究） | PARTIALLY | data/panel_variants.csv; パネル A と一致 | 2026-10-19 | 有（2 経路） |
| 漸近閾値（60 桁）: b=31 EUR 19.18%、joint Shannon 19.73%、b=61 19.53/19.86%、per-probe 24.3%；旧 CSV の b=31 値（18.38/17.99）は倍精度アンダーフロー | 数値/事実（本研究・訂正） | SUPPORTED | data/asymptotic_thresholds_mp.csv; パネル A の mpmath 計算と一致 | 2026-10-19 | 有（2 経路） |
| 対称族と Bell 対角族の閾値差: N=10¹⁴ で ≤0.16 pt、N=10⁸ で最大 0.76 pt（旧「全点 ≤0.15 pt」は訂正） | 数値/事実（本研究・訂正） | SUPPORTED | data/threshold_table.csv vs bd_thresholds.csv | 2026-10-19 | 有 |
| 旧 Fano 会計の閾値 21.89%（N=10¹⁴ b=9）/16.20%（N=10⁸ b=3）が現行結果ファイルに存在 | 数値/事実（出典） | SUPPORTED | data/panel_variants.csv（fano 行） | 2026-10-19 | 有 |
| min-entropy は積 cq 状態で加法的（SDP の可解集合のテンソル化）；よって結合 min-ent 列はブロック間結合測定・量子メモリに対しても有効 | 因果（背景） | SUPPORTED | KRS09（書誌）；パネル B R2 の導出、A の指摘 | 2026-10-19 | 有 |
| Carmeli–Heinosaari–Toigo, PRA 98, 012126 (2018): 事後測定情報付き識別と測定の両立可能性 | 引用帰属 | PARTIALLY | OpenAlex 書誌確認（doi:10.1103/physreva.98.012126）；本文未読 | 2026-10-19 | 無 |
| ε 総量を 1e-9 に揃えても閾値は動かない: joint Shannon b=7 18.348%、collective min-ent b=11 17.659%（差 <1e-6 pt）；鍵長では min-ent 1.3 bit（4 log₂(5/4)）、Shannon ≈1e5 bit | 数値/事実（本研究） | SUPPORTED | data/panel_variants2.csv（eps_sec=8e-10 行）vs bd_thresholds.csv | 2026-10-19 | 有（B4 の「1 bit 未満は誤り」を受け再計算；閾値への影響なしと確認） |
| PS を課した collective min-ent の最良値 17.52%（b=11）；joint Shannon PS 17.80%（b=7）との差 0.3 pt | 数値/事実（本研究） | SUPPORTED | data/panel_variants2.csv（postsel b=11,15 行）、panel_variants.csv | 2026-10-19 | 有（b=15 は 16.02% で b=11 が最良） |
| c_φ 最大点が 1 を離れる D: b=2 0.206、b=3 0.222、b=5 0.232、b=9 0.239、b=15 0.243 | 数値/事実（本研究） | SUPPORTED | data/cphi_argmax.csv | 2026-10-19 | 有（格子 0.001） |
| trace distance δ → 情報量: I(K;E) ≤ 2δℓ+(1+δ)h(δ/(1+δ))（条件付きエントロピーの連続性、Winter 2016 Lemma 2）；Pinsker は逆向きで使えない | 導出/文献 | SUPPORTED | Winter, CMP 347, 291 (2016) Lemma 2 | 2026-10-19 | 有（B5 指摘；古典 A ではさらに係数 2 を落とせるが一般形を引用） |
| 寿命 t_coh のメモリで同一ブロックの 2 プローブが同時保持される確率: 2r−r²（r=t_coh/T_run）、ペア union bound で ≤2·C(b,2)·r = 7.2e-4（b=9, r=1e-5）；sifting・採否で条件づけ未実施 | 導出（本研究） | SUPPORTED | 初等計算（B8 と一致） | 2026-10-19 | 有（固定窓モデルなら 3.6e-4；本文は寿命モデルに統一） |
| 隠れ基底の残余利得（六状態 b=2）: min-ent 0.0013–0.029 bit（log₂(P_ad/P)、D=0.167/0.259） | 数値/事実（本研究） | SUPPORTED | data/hidden_basis_sdp.csv, sixstate_mixed_lb.log | 2026-10-19 | 有（「加算しない」を「小さいが非零」に訂正） |

## S17 サマリ（パネル セット 1 後, manuscript v2.0.0, 2026-10-19）
- 新規 10 行（SUPPORTED 5 / PARTIALLY 5）。撤回: 「メモリがブロック長なら利得なし」（T25 の分割と矛盾）、「≤0.15 pt」、「15 log₂n ビット」、「b≥2 で c_φ=1 最大」、「BWW08: 2 基底は共通最適測定」、Appendix B の「every timelock-restricted adversary」。結合 min-ent 列の位置付けを「集団攻撃値（時間ロック不要）」に訂正。

## S17 サマリ（導出付記, manuscript v1.3.0, 2026-10-15）
- Appendix C（C.1 per-ancilla、C.2 tally、C.3 漸近条件、C.4 Bell 対角、C.5 鍵長式）を追加し、既知の式に原典の式番号を付与（T25 Eqs.17–21,93; TCR09 Def.4/Thm 9; GW99 Eqs.1–3,7,8,11; ABBMM06 Eq.17,23; BA07 Eq.30,68; Fuchs96 Eq.3.12）。新規引用 Hel76/EMV03/KRS09 は書誌確認。数値変更なし。

## S17 サマリ（反映, manuscript v1.2.0, 2026-10-15）
- fact-check-report の要対応 6 件を反映。A28 は本文照合により NF→SUPPORTED。新規引用 KWW12・RGK05 は書誌確認（本文未読、PARTIALLY 扱い）。数値変更なし。差し戻しなし。

## S17 サマリ（主張別ラベリング, fact-check-report.md v1.0.0, 2026-10-15）
- 原稿 v1.1.0 の文献主張 30 件: Strongly Supported 17 / Partially 10 / Not Found 3（A2 free-space QBER 水準、A28 Levitin–Fuchs の本文未照合、A30 LDPC 演算数）/ Contradicted 0。本研究主張 11 件: SS 7 / PS 4。
- 要対応（表現・引用の強化、事実誤りなし）: A2 出典追加、A25「2 基底では利得なし」を推測確率基準に限定（BAL11 p.5 は BB84 で +0.8 pt）、A28 本文照合、A30 数値根拠、B11 Appendix B を「スケッチ」と明示。
- 頁付き照合先: BA07 p.4/p.9–10/p.17、ABBMM06 p.1–4、GW99 p.1–3（Eqs.1–3, 7, 11）、T25 p.15/p.25/p.29/p.33、TCR09 p.6 Eq.(30)、BAL11 p.2/5/6、VA20 p.1/2/9、Novak25 p.1、PK23 p.1/4/6、WMU06 p.1、Jiang21 p.1。

## S17 サマリ（S12 ゲート, submission-bundle, 2026-10-15）
- submission-bundle/main.tex は S11 バンドルと同一（diff なし）。S11 ゲートの数値突合結果をそのまま継承し、修正済みの六状態 b=1 値（0.751/0.835 at D=0.168）が data/sixstate_hidden_basis_b1.csv の格子点（D=0.1683: 0.7508/0.8350）に一致することを再確認。投稿衛生 grep 該当なし。差し戻しなし。
- 未充足（事実性ではなく形式）: 著者名・所属・ORCID・資金・arXiv 番号の記入。

## S17 サマリ（S11 ゲート, preprint-bundle, manuscript v1.1.0, 2026-10-09）
- バンドル main.tex の全印字数値を結果ファイルと突合（scratchpad/s17_verify.py）: T25 再現 4 値、表 I 7 行、表 II 8 行、漸近 21.9/23.8/19.6/18.9%、結合最良 17.66/18.35%、個別 20.7–20.8%、tally−Fano 1.0 pt、BAL11 5 値、基底隠蔽 SDP、六状態 b=2/3 下界・緩和値、定理 1 検証ログ — 全て一致。
- 1 件修正: 六状態 b=1 の「0.750 vs 0.833 at D=0.167」は格子点間の補間値だったため、実在する格子点 D=0.168 の 0.751/0.835 に置換（data/sixstate_hidden_basis_b1.csv）。
- 投稿衛生 grep（corrected / earlier revision / previously reported / referee / phase-1 / conjectur*）: 該当なし。要旨 1773 字（arXiv 上限 1920）。
- 未充足: 著者名・所属がプレースホルダ（ユーザー入力待ち）。

## S17 サマリ（S15→S3 残課題, manuscript v1.0.0, 2026-10-09）
- 定理 1（旧 Conjecture 1）を証明し SUPPORTED（代数的証明＋数値 2 経路）。Bell 対角族の再最大化（J11）を追記、表 1 を一般族の値に更新（旧 17.49/18.39% → 17.40/18.35%）。帰着命題は証明スケッチ（PARTIALLY）。六状態 b=3 の達成可能下界を追記（PARTIALLY）。

## S17 サマリ（S18 ゲート, manuscript v0.9.0, 2026-10-09）
- S18 で生じた新主張 9 件を追記: SUPPORTED 5 / PARTIALLY 4。訂正 2 件（Fano 下界の誤用、六状態混合ブロックの不等式方向）は原稿 v0.5.0→v0.9.0 で修正済。旧数値（個別 Shannon 21.9% 等、「<10⁻³ bits」）は原稿から削除。
- 主要先行研究（Bae–Acín 2007、Acín et al. 2006）を一次本文で照合し、新規性主張を「非適応・ブロック長メモリの Eve でも同条件」「有限鍵版」「基底隠蔽×AD の非併存」に限定（台帳の旧新規性行 1「QCT 下の AD 有限鍵式は存在しない」は維持されるが、閉形式 20%/27.6% の新規性は撤回）。
- 差し戻しなし。H4: References 31 件は全て本文で引用。

## S17 サマリ（S7 ゲート再適用, manuscript v0.4.0, 2026-10-09）
- P1″ 検証の追記 7 件: SUPPORTED 1（BAL11 背景）/ PARTIALLY 6（本研究の SDP 数値、第三者再計算なし）。原稿 §3「Hiding the basis as well」、§7、§8、要旨を改訂し、BAL11 を References に追加。差し戻しなし。

## S17 サマリ（S7 ゲート再適用, manuscript v0.3.0, 2026-10-08）
- S15 差し戻し後の原稿: 主張を「負の結果」に再構成。新規 claim 4 件（結合測定 SDP 一致、20% 条件、有限鍵 17.3–18.4%、Chau 20.0% 背景）を追加、いずれも PARTIALLY（本研究の数値は第三者再計算なし；Chau 原典未読）。
- 旧主要数値（20.7–21.9%、25% 収束）は「個別測定モデル限定」の限定表現に書き換え、台帳の判定は据え置き。
- 差し戻しなし。H4: References に CKR09 を追加し本文 §7 で引用。

## S17 サマリ（S7 ゲート, manuscript v0.2.0, 2026-10-08）
- 原稿の検証可能主張 34 件を台帳と突合: SUPPORTED 22 / PARTIALLY 12 / UNSUPPORTED 0 / CONTRADICTED 0。
- PARTIALLY は (i) 本研究の主要数値（第三者再実装なし）、(ii) 抄録のみの外部文献（Fuchs, BWW, TFKW, Fung）、(iii) t_coh<1 s の技術評価。原稿では「in the standard individual-attack model」「as assessed in Ref. [VA20]」等の限定表現で対応済。
- 差し戻しなし。H4 引用整合: 原稿 References 21 件は全て本文で引用され、台帳行または背景引用として対応付け済。

## S17 サマリ（S5 追記, 2026-10-08）
- 追記 5 件: SUPPORTED 2 / PARTIALLY 3。主要数値（20.7/21.9%）は独立 2 経路目（別実装または別手法）が未達のため PARTIALLY 固定。

## S17 サマリ（S3 ゲート, 2026-10-08）
- 抽出 19 件: SUPPORTED 10 / PARTIALLY 9 / UNSUPPORTED 0 / CONTRADICTED 0 / UNVERIFIABLE 0。
- PARTIALLY の理由: 主要数値（17.3% 等）は単一出典、外部 3 文献は抄録のみ、新規性は定義上 2 経路未達。theory-foundation.md では該当箇所を「未検証」「本文未確認」と限定表現にした。
- 差し戻しなし。S3 通過。

## パネルレビュー セット 2（2026-10-19）
- 構成: A=Claude Opus（再現監査、宣言 13 件の照合＋P1–P10）、B=Codex（論理・新規性、B1–B12）。両者独立。
- 裁定計算: panel_variants2.py（ε 再配分、PS min-ent b=11/15、c_φ argmax 境界）。新規 6 行（SUPPORTED 6）。
- 撤回・訂正: 「差は 1 bit 未満」→ 閾値差 <1e-6 pt（鍵長 1.3 bit）；Pinsker → 連続性（Win16）；「W の帰着」→ 明示仮定；「奇数 b で最適」→ 数値探索で改善なし（b≤9）；「加算しない」→ 小さいが非零；Open question の端点（全保持・分割事後は上界のみ、表 4 で未達）；4e-4 → 7e-4（寿命モデル）；「if and only if」→ 十分条件。
- 原稿 v2.1.0、14 頁。S17 ゲート: main.tex の印字数値を結果ファイルと突合（表 4 は CSV から生成）、投稿衛生 grep 該当なし。
