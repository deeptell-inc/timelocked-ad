# セット 2（再採点）— Reviewer A（再現監査）: manuscript v2.0.0

方針: 宣言された 13 件の修正が本文・PDF・データに実際に入っているか、修正によって新しい不整合が生じていないかを検査する。数値はすべて再実行または CSV 突合で確認した。今回の計算はすべて /tmp/panelA/set2 にある。再実行したスクリプト（asymptotic_mp.py、panel_variants.py）が書いた CSV は、実行前のスナップショット（/tmp/panelA/set2/orig）と**バイト単位で同一**であることを確認した。プロジェクトファイルは変更していない。

---

## 1. 宣言と実装の照合（13 件）

判定記号: ✓ = 反映済み、△ = 一部反映、✗ = 未反映または新しい不整合あり。

| # | 宣言内容 | 判定 | 根拠（原稿の文言、または欠落箇所） |
|---|---|---|---|
| 1 | 公開時刻表 A2・攻撃クラス J/W/H・主結論の書き直し・分割 SDP・Open question | ✓ | A2「Protocol 1 of Ref. [T25] runs for a time T_run … and then announces, in this order: the detection record, the bases …, a random reordering …, a random partition …」。A4 で Class J/W/H を定義。§3 に「What hiding the partition is worth…」。§7 に「**Open question.** For a window adversary who holds the w=ft_coh probes…」。要旨も「treating the parities, the block partition and the bases separately」に書き直されている。 |
| 2 | 会計の役割分離・列名変更・Holevo 基準線・「no better analysis」撤回 | △ | §4「First, the two accountings play different roles…」、表 1 の列名「collective (joint), min-ent」、表 3 の「Holevo Shannon, no timelock 16.40/16.76/15.59%」は反映済み。**ただし §7 に「the collective-attack min-entropy bound, 17.66% at N=10^14, is what any analysis within the model can certify」があり、撤回したはずの converse（逆向きの最適性）主張が言い換えで復活している**。最小エントロピーの下界は鍵長の上界ではない。 |
| 3 | post-selection（PS）を全 ε に課した閾値（表 3）、App. B の書き直し | ✓ | 表 3 の PS 4 行と App. B「the leftover-hash term grows by 4 log₂(n+1)^15 bits and … the smoothing parameter of the equipartition term shrinks by the same factor」「exponent 16^b−1」。数値は私の Round 1 の独立計算（17.80/15.86/19.39/20.61）と一致。 |
| 4 | 偶数 b の per-probe の扱い（perprobe_opt、表 1 の b=2 撤去、表 2 注記、§3、C.2） | ✗ | §3 の段落、表 2 の注記、C.2 は反映済み。**表 1 の N=10⁸、b=2 行の per-probe 値 12.75% / 13.89% が md・tex・PDF のいずれにも残っている**。キャプションの「reported for odd b only」と矛盾する。図 3（fig4_threshold_vs_b）も per-probe の漸近曲線を b=2 を含めて描いており、凡例は旧称「individual」のまま。表 4 の比較列も b=2 の Helstrom 値 0.8143 を「per-probe H」としており、本文自身が示す同一 POVM 最適値 0.8454 を使っていない。 |
| 5 | 「≤0.15 pt」を「N=10¹⁴ で ≤0.16、N=10⁸ で最大 0.8」に訂正 | △ | manuscript.md §5 には反映済み。**main.tex / main.pdf では、§V の当該段落（漸近値・0.7/0.3 pt・per-probe の b 最良値・対称族との差）が丸ごと欠落している**（後述 P1）。 |
| 6 | 60 桁精度での再計算、CSV・図の更新、b=41/61 の追加 | △ | data/asymptotic_thresholds_mp.csv、double 精度 CSV の上書き、図の更新は反映済み。本文の値（24.3/19.9/19.5/19.5%）は md にしかなく、PDF にはない（P1）。図キャプションは「finite-key values at N=10⁸ and 10¹⁴」としているが、make_figures.py は N=10¹⁴ の点しか描かない。本文が図を引いて述べる「collective min-entropy threshold to 19.5%」の曲線も図にない。 |
| 7 | Fano 版を panel_variants.csv に出力、quick ファイルの更新 | △ | CSV に 0.21886 / 0.16198 があり、§7 の「21.89% against 20.86%」はたどれる。**data-manifest.md l.37 は今も「13.97 / 16.20 / 20.66 / 21.89%: threshold_table_quick.csv」**で、現行の quick ファイル（15.20 / 20.86%）と食い違う。l.49 の「n=5 は計算中」も古い。 |
| 8 | c_φ=1 の普遍主張の訂正 | ✓ | §3「At the error rates relevant for key generation the maximum is at c_φ=1 … close to D=1/4 the maximiser moves below c_φ=1 (for b=2 at D≥0.206, for b=9 at D≥0.239)」、C.1「(the BB84 worst case at the error rates of interest…)」。ただし 0.206 / 0.239 は私の /tmp の計算から来た値で、プロジェクトのデータファイルには存在しない（§2 参照）。 |
| 9 | 5ε_sec/4 への統一と Pinsker 経由への修正 | ✗ | §4 は「bounded by 5ε_sec/4 … through Pinsker's inequality」で修正済み。**C.5 の末尾（md l.185 / tex l.191）に「yields a key that is ε_sec-secret in the trace-distance sense, which for classical adversary information coincides with the accessible-information criterion of Ref. [VA20]」が残っている**。さらに §4 の新しい文「the difference is worth less than one bit of key」は偽（P4）。 |
| 10 | BWW08 への帰属撤回、BAL11 の +0.8 pt 併記 | ✓ | §3「in guessing probability the gain is confined to protocols with more than two bases for the probe states considered here (our semidefinite programme below), while in Shannon information Ref. [BAL11] still finds a gain of 0.8 percentage points」、§7「that Ref. [BAL11] nevertheless finds 0.8 percentage points in Shannon information」。 |
| 11 | 六状態についての限定 | ✓ | §3「so we make no claim about the six-state threshold with hidden bases」、要旨「does not add to AD for six-state at small blocks」、§7「Whether it vanishes for large b is open」。ただし §3 の「Hiding the basis and hiding the parities therefore do not compound」という一般形の文は残っている（軽微）。 |
| 12 | 「every timelock-restricted adversary」の撤回、App. B の書き直し | ✓ | 該当文は md・tex とも grep で 0 件。App. B「a proof against coherent attacks would need a tool compatible with block locality … and we leave it open」。 |
| 13 | 定理文に \|c\|<1、A4 の置換、要旨の b 明示、[CHT18] の追加、テスト 11 件 | △ | 定理文の「real overlap c, \|c\|<1」、A4、[CHT18]（§1・§3）、テスト 11 件（11 passed）は反映済み。**要旨と結論の「20.7–20.8%」には b=9 の明示がない**。§5 にのみ「at b=9 (its best over b is 21.83% at b=15)」とある。カバーレターも同じ。 |

宣言 13 件のうち、完全に反映されたのは 6 件（#1, 3, 8, 10, 11, 12）、一部反映は 5 件（#2, 5, 6, 7, 13）、未反映または新しい不整合を伴うものは 2 件（#4, 9）。

---

## 2. 新しい数値の再現と、出典をたどれるかの確認

**実行結果（事実）**

| 対象 | 実行 | 結果 |
|---|---|---|
| テスト | `pytest tests -q` | 11 passed（4.2 s、matmul の RuntimeWarning のみ） |
| asymptotic_mp.py | 再実行（150 s） | CSV は既存版とバイト単位で同一。§5 の 24.3%（per-probe b=61: 0.24279）、19.9%（joint Sh b=61: 0.19863）、19.5%（collective min b=61: 0.19466）、19.5%（EUR b=61: 0.19528）、19.6%（joint Sh b=21: 0.19602）、23.8%（b=31: 0.23768）、21.9%（b=9: 0.21882）はすべて一致。Round 1 の私の mpmath の値（b=31 で joint 19.73、EUR 19.18、indiv 23.77）とも一致。 |
| panel_variants.py | 再実行（368 s） | CSV はバイト単位で同一。表 3 の 13 値はすべて一致（17.80/15.86、16.67/17.25、20.52/19.39、19.70/20.61、16.40/16.76/15.59）。 |
| perprobe_opt.py | 新しい点で `optimise` を呼び出し | b=3, D=0.15: J・p_g とも Helstrom と 10⁻¹⁰ まで一致（0.8179216152 / 0.9610256206）。b=9, D=0.22: 一致（0.9997997140 / 0.9999667719）。b=4, D=0.15: p_g 0.97068 > Helstrom 0.96103（偶数 b での改善を再現）。 |
| 6 出力 POVM（2 出力の射影測定 3 つをラベル付きで混合） | 独立テスト（mix.py） | b=3（D=0.10, 0.20）と b=5（D=0.17）で J・p_g とも Helstrom と一致し、4 出力という制限による取りこぼしは見つからなかった。 |
| 表 4 | hidden_partition_sdp.csv（+_n5, _n6）と突合 | 8 行すべて一致（0.89379, 0.982458, 0.891348, 0.981276, 0.889679, 0.980425, 0.888438, 0.979744）。 |
| perprobe_opt.csv | §3「to 10⁻⁶ for b=3,5,7,9 at D∈[0.10,0.23]」の確認 | b=9 も 4 点（0.10, 0.17, 0.20, 0.23）がそろっており、途中打ち切りはない。奇数 b での差は \|ΔJ\| ≤ 1×10⁻¹⁵、\|Δp_g\| ≤ 1.6×10⁻¹³ で、10⁻⁶ という記述は保守的。偶数 b の数値（0.8454 / 0.8143、0.9246 / 0.9093）も一致。 |

**現行ファイルにたどれない数値・誤った数値**

1. **§5「0.3 once the post-selection factor is charged」**: 計算には PS を課した collective min-ent の b 最良値が必要で、どのファイルにもない。私が計算した結果は b=11 で 17.524%、b=15 で 16.02% で、17.80−17.52=0.28 となり値自体は正しいが、panel_variants.csv には b=7 と b=9 しかない。
2. **§3「D≥0.206（b=2）、D≥0.239（b=9）」**: Round 1 の私の計算（/tmp）が出典で、プロジェクトのデータファイルにはない。
3. **§5「≈7×10⁷ bits at the optimum」「60 log₂(N+1)≈2.8×10³」**: 解析式で導けるが、最適点の S⁻ を記録したファイルがない（Round 2 の私の round2.py が出典）。
4. **§4「the difference is worth less than one bit of key」**: 偽（P4）。
5. **表 1 の b=2 per-probe 値 12.75 / 13.89%**: ファイル（bd_thresholds.csv）にはたどれるが、本文の結論（偶数 b では最適でない）と矛盾するため、表に残してはいけない。

それ以外の §III・V・VII・VIII の数値（17.66, 17.30, 18.35, 16.76, 0.7, 20.66/20.81/21.83, 20.61/19.39, 0.16/0.8, 21.89/20.86, 4×10⁻⁴, 0.8938–0.8884, 0.8454/0.9246）は、現行ファイルまたは原稿内の式からたどれる。

---

## 3. 推定量・表記の一貫性

- **ε 表記**:
  - §4 は 5ε_sec/4 で統一されている。
  - C.5 の末尾には「ε_sec-secret … coincides」が残る（#9 ✗）。
  - §4 の三つの remark は「First / Second / Third」の後にもう一度「**Second**, if A2 fails…」が続き、番号が重複している（編集の残骸）。
- **「odd b only」**:
  - 表 1 は b=2 行に per-probe 値を残している（✗）。
  - 図 3 は per-probe の漸近曲線を b=1,2,… で描き、凡例は「individual」。
  - 表 4 の比較列は b=2 の Helstrom 値 0.8143 を「per-probe H」と表示している。§3 自身が b=2 の同一 POVM 最適値を 0.8454 としているので、表 4 の「per-probe との差」は過大に見える。0.8454 を基準にすると、n=6 で回復するのは差の 82%（0.8143 を基準にすると 88%）で、結論は変わらない。
- **Holevo 行**: Holevo は PS なしの値なので、「0.7 pt（PS なし）」との比較は整合する。一方「0.3 pt（PS あり）」は、Holevo の PS 版を計算しないまま collective min-ent の PS 値と比べている。比較の向きは妥当（時間ロックなしの最良値は min-ent）だが、上記のとおり出典ファイルがない。
- **PS 行**: per-probe min-ent の PS 値 b=7 は 0.19704113838591283 で、PS なしの値と**全桁一致**する。閾値の二分探索の刻み（0.05°、QBER にして約 0.05 pt）の内側に収まった結果であり、「barely move」はこの解像度より細かくは言えない。
- **相互参照**: §3 の分割 SDP の段落が「(Table 3)」を参照しているが、正しくは表 4（tex では `\ref{tab:ps}` で、PDF 上は Table III を指してしまう）。

---

## 4. 新しい主張の健全性

**(a) 「min-entropy 列はブロックをまたぐ共同測定に対しても成立する」（§4）**
条件付きで受け入れる。積の cq 状態の H_min は加法的（SDP の主問題・双対問題の可行解をテンソル積にできる）であり、P_ad は量子メモリを持ちパリティを知った Eve の推測確率なので、集団攻撃の下では時間ロックと無関係に成立する。Round 1・2 での私の主張（問題 2）と一致する。条件は二つ。第一に、加法性の根拠として [KRS09] は操作的意味の文献なので、加法性の証明そのものを引くべき。第二に、これはあくまで集団攻撃の値であり、要旨と §7 で T25（コヒーレント攻撃）の 17.30% と並べる箇所には「collective-attack」と毎回書くべき（要旨には書いてあるが、§7 の converse 主張は除くべき）。確度 85。

**(b) A4 の class W への帰着**
- **仮定か定理か**: A4 は「the measurement record factorises into a per-probe instrument …」と導出のように書き、「Up to the feed-forward on unrelated probes, which we neglect」と一つだけ省略を明示している。つまり**仮定込みの帰着**である。ところが要旨と結論は「is reduced to role-blind per-probe measurements」と定理の形で述べており、§7 にしかない但し書き（「feed-forward … was neglected」）が要旨と結論にない。確度 80。
- **見落とされているもう一つの仮定**: window の Eve は 1 窓（w≈10⁹ 個のプローブ、ほとんどが別々のブロック）を共同測定できる。この場合、ブロック間の記録は一般に積にならない。per-probe 列の Shannon/AEP 会計も min-ent 会計（1−γ_b は量子最適ではない）もブロック間の積構造を必要とするので、§4 自身の限定（「valid for adversaries whose measurement is a product over blocks」）を class W にも明示的に課す必要がある。現状の「factorises」はブロックごとの周辺分布については正しいが、ブロック間の相関については何も言っていない。確度 65。
- **分率 C(b,2) f t_coh / N**: オーダーとして正しい。固定窓では 1 対あたりの確率が t_coh/T_run = f t_coh/N で、C(b,2) 対への和集合上界をとると b=9 で 36×10⁹/10¹⁴=3.6×10⁻⁴（本文 4×10⁻⁴）。到着後 t_coh の滑る窓なら係数 2 がつく。**影響は無視できる**: 衝突したブロックを Eve が完全に知っていると仮定しても、失われるのはエントロピー項の割合 q≈4×10⁻⁴ だけである。per-probe min-ent b=9 の閾値点（S⁻=9.2×10⁸、ブロックあたり −log₂p≈1.3×10⁻⁴）では約 40 ビットで、ℓ≈900 ビットに対して小さい。ただし本文が言うとおり、超幾何分布による統計的な上界は未導入。

**(c) 「同一 POVM の最適値は奇数 b で Helstrom」**
支持する。perprobe_opt.csv の 4 点 × b=3,5,7,9 で差は ≤1.6×10⁻¹³。私の新しい 3 点と、6 出力の混合テストも一致した。ただし二点を限定すべき。第一に、最適化は局所探索（Nelder–Mead、12 再出発）で大域最適性の保証はなく、D は 4 点だけなので「D∈[0.10,0.23]」は「four values of D in [0.10,0.23]」と書くべき。第二に、C.2 の「an extremal POVM has at most four rank-one outcomes, … so … four-outcome POVMs」という論法は、ブロック目的関数が POVM について凸でないため厳密ではない（per-probe の混合はブロックのチャネルの混合にならない）。6 出力テストで反例は出なかったので、数値的な支持はある。確度（主張が正しいこと）80。

**(d) その他の新しい主張**
- §4「less than one bit」は偽（P4）。
- §7「is what any analysis within the model can certify」は根拠のない converse 主張（#2 △）。

---

## 5. 検証スクリプトのカバー範囲

tests/test_skl.py は 11 件。新たにカバーされたもの:
- Bell 対角項が対称族に一致し、φ_X について単調であること
- P_ad と Helstrom の直接計算の一致
- AEP の式の値と、PS を課すと鍵長が短くなるという向き
- 定理 1 の構成（b=2,3,4、D=0.15）

**欠けているもの（本文で引用している量）**:
1. PS 閾値の値（表 3）。現在は「ℓ_ps < ℓ」という向きしか検査していない。
2. perprobe_opt（奇数 b での一致、偶数 b での改善）。
3. hidden_partition_sdp（P_ind < P < P_ad の挟み込み、表 4 の値）。
4. asymptotic_mp（b=31 で double 精度版と高精度版が乖離すること、b=61 の値）。
5. Holevo 基準線と Fano 版。
6. T25 の 4 閾値の再現（最も重要な検証なのに quick 実行でしか確認していない）。
7. c_φ の argmax が D≥0.206 で 1 からずれること（B#6 の導関数）。
8. joint_block_theorem.check を import すると、モジュール冒頭のループ（b=2–9 の出力）が走る。テストとしては動くが、副作用がある。

---

## 6. 最終スコア

| 評価軸 | スコア | コメント（長所／問題を深刻度順に） |
|---|---|---|
| **新規性** | 6/10 | 長所: 結論が「パリティの隠蔽は定理で無益、分割の隠蔽は局所性次第、基底は未解決」と明確に分解され、Open question が精密に立てられた。分割を事後情報とする SDP は新しい観点である。問題: 主たる新規性は定理 1（両立性の明示構成）のままで、分割の価値は未解決の問いとして残っている。 |
| **データ分量** | 7/10 | 長所: PS を課した値、Holevo 基準線、同一 POVM の最適化（b≤9）、分割 SDP（n≤6）、60 桁の漸近値が加わった。問題: 分割 SDP は b=2 だけで、PS 版の b 最良値（b=11）と c_φ の argmax 境界がファイル化されていない。 |
| **データ質** | 7/10 | 再現性: 新しい表 3・4、漸近値、perprobe の値はすべて一致し、再実行した CSV はバイト単位で同一。健全性の残課題: 表 1 の b=2 per-probe 値の残存、表 4 の基準値（0.8143 ではなく 0.8454 を使うべき）、「less than one bit」が偽、「0.3」の出典なし、PS 行が二分探索の解像度以下であることの未注記。 |
| **ストーリー** | 6/10 | 長所: 三つのレバーの分離、要旨・§7・結論の整合、六状態の限定が改善された。問題: §7 で converse 主張が復活している。要旨・結論の「reduced to」に仮定（feed-forward の無視、ブロック間の積）が書かれていない。要旨の 20.7–20.8% に b=9 の明示がない。 |
| **論理展開** | 5/10 | 長所: App. B は誠実な現状報告になり、ε も §4 では統一された。問題: class W の帰着はブロック間の積構造を暗黙に仮定している。C.5 に旧来の「ε_sec-secret / coincides」が残る。4 出力で足りるとする論法は凸性がなく厳密でない。 |
| **総合** | 6/10 | 科学的主張はおおむね証拠の範囲に収まった。残っているのは本文の数文の修正（converse、less than one bit、class W の仮定の明示）と、パッケージの不整合（PDF からの段落欠落など）。 |

推奨: MINOR_REVISION（科学的内容について）。ただし、下記の P1–P3 を直すまで投稿パッケージとしては出せない。

### 二つのループの収束判定
- **科学的較正のループ: ほぼ収束（あと 1 周、本文のみ）**。新しいデータは不要。必要なのは、(i) §7 の converse 主張の削除、(ii) §4「less than one bit」の訂正（Shannon 会計では約 9×10⁴ ビット）、(iii) 要旨・結論・A4 での class W の仮定（feed-forward の無視、ブロック間の積）の明示、(iv) 「four values of D」、4 出力論法の限定。
- **パッケージ整合のループ: 未収束**。以下の P1–P10 が残る。

### 残っている必須修正（深刻度順）
- **P1（重）**: main.tex / main.pdf で、§V の漸近値・比較段落（「Asymptotically … 60-digit … 24.3% … 0.7 / 0.3 pt … 0.16 / 0.8 pt」）が丸ごと欠落している。表 IV のキャプションも空（`\caption{}`）。原因は、md で表 4 の直後に空行なしでキャプションが続くため、md2tex が両者を取り込み損ねたことと推定される。fix #5・#6、#2 の一部が投稿版に存在しない。
- **P2（重）**: 表 1 の N=10⁸、b=2 の per-probe 値（12.75 / 13.89%）が残っており、キャプションの「odd b only」と矛盾する（fix #4 未反映）。図 3 も、偶数 b の per-probe 漸近曲線、旧凡例「individual」、キャプションにある N=10⁸ の点の欠如、本文が言及する collective min-ent 漸近曲線の欠如、という点で本文と合っていない。
- **P3（重）**: C.5 の末尾「ε_sec-secret … coincides with the accessible-information criterion」が md・tex 両方に残る（fix #9 未反映）。
- **P4（中）**: §4「the difference is worth less than one bit of key」は偽。ε_sec→0.8ε_sec と置くと、Shannon 会計の AEP 項は S⁻=1.03×10¹¹ で 9.1×10⁴ ビット増え、min-ent でも LHL 項が 4·log₂1.25=1.29 ビット増える。閾値への影響は小さいが、文としては誤り。
- **P5（中）**: §7「is what any analysis within the model can certify」を削除する（#2 で撤回した主張の復活）。
- **P6（中）**: §3 の分割 SDP の段落の「(Table 3)」を「(Table 4)」に直す。表 4 の per-probe 列を b=2 の同一 POVM 最適値 0.8454 に替えるか、別の列として併記する。
- **P7（中）**: 「0.3 pt」（PS を課した collective min-ent の b=11 = 17.52%）と、c_φ の argmax 境界（0.206 / 0.239）を結果ファイルとして出力する。
- **P8（中）**: preprint-bundle/arxiv-metadata.txt の要旨で引用記号が消え、「bound of Ref. .」「the protocol of Ref.  partitions」となっている。Comments の「13 pages」と preprint README の「13 pages」は、PDF の 12 ページと食い違う。
- **P9（中）**: カバーレター §2 の「Their protocol partitions the sifted key at random」は Bae–Acín を指してしまう。正しくは Treplin et al. のプロトコル。要旨・カバーレターの 20.7–20.8% に「at b=9」を付ける。
- **P10（低）**: submission-bundle/supplemental/README_anc.md が v1.1.0 時点のまま（7 tests、10 pages、新スクリプトの記載なし）。supplemental/data に hidden_partition_n6.csv がなく、n6.log の内容も本体と異なる。data-manifest.md l.37・l.49 が古い。claims-ledger.md l.93・l.132 も旧値（「全点で ≤0.15 pt」「18.9%」）のまま。preprint README の Reproduction に新しいスクリプトがない。§4 の remark 番号が重複している（「Second」が 2 回）。
