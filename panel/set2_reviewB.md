# 総合スコア（Nature 級査読者ペルソナ採点）

| 評価軸 | スコア | コメント（長所／問題を深刻度順に） |
|---|---|---|
| **新規性** | 6/10 | 任意ブロック長の明示的な事後情報付き識別測定は残る。CHT18 への位置づけも改善。ただし、窓制限から per-probe 安全性への帰着は新しい成果として未成立。 |
| **データ分量** | 7/10 | Holevo、post-selection 感度、偶数 b の改善、n=6 の分割隠蔽を追加した点を評価。窓付き大規模問題を直接解くデータではない。 |
| **データ質** | 5/10 | 保存 CSV と本文の対応は改善したが、計算対象の攻撃クラスと保証するクラスが一致しない。撤去を宣言した b=2 行も残存。本査読では数値計算・テストを再実行していない。 |
| **ストーリー** | 4/10 | 三種類の隠蔽の分離は前進。一方、要旨・結論・カバーレターでは未証明の帰着を再び結果として提示し、小さな非零利得を「加算しない」と表現している。 |
| **論理展開** | 4/10 | 定理1の核を否定する理由は見つからない。しかし §VII の境界条件、min-entropy と鍵率上限の混同、Pinsker の向き、post-selection の扱いに重大な不整合が残る。 |
| **総合** | 5/10 | 修正の方向は正しいが、科学的較正もパッケージ整合も未収束。定理中心の限定論文として再構成できるため、棄却ではなく大幅改訂。 |

推奨: MAJOR_REVISION

Reviewer B — Set 2、論理・新規性担当。対象は `manuscript.md` v2.0.0。指定順で統合裁定、13項目の修正宣言、本文全文、指定の周辺文書を読んだ。図キャプションは Markdown 本文にないため `paper/main.tex` と `preprint-bundle/main.tex` も参照した。数値計算、テスト、再ビルドは未実行。保存データの閲覧は再現実験とは区別する。本レビュー以外のファイルは変更していない。

## 長所

- T25 Protocol 1 の事後ランダム分割を A2 に取り込み、パリティ、分割、基底を分離したことは Set 1 の核心への応答である。原典 p.4、steps 3/5 と整合する方向に変わった。citeturn2view5
- 定理1は既知の分割・基底の下で、パリティ公開前の測定が公開後の guessing probability に達するという限定命題として価値がある。CHT18 の一般的な「最適測定の両立可能性」と、今回の具体的な構成との関係も本文に加わった。citeturn3view2
- §IV は collective min-entropy 列が時間ロック不要であること、Shannon 列がブロック間積測定に限定されることを明記した。これは単なる語調変更ではない。
- 不利なデータを実際に追加している。Table 3 の Holevo/PS、Table 4 の n=5,6、§III の偶数 b の改善、六状態の大 b 未解決という記述を評価する。

## 問題（深刻度順）

### B1［重大］W → role-blind per-probe は証明ではなく、未閉鎖のモデル仮定

**場所:** A4、§I contribution (iv)、Abstract、§V、§VII、§VIII、cover letter の項目2、arXiv abstract。

**確認事実:** A4 は窓内の任意の結合測定を許した直後に “the measurement record factorises into a per-probe instrument” と述べ、“Up to the feed-forward on unrelated probes, which we neglect” を付けて per-probe クラスへ移る。したがって、仮定と結果が混在している。単に「feed-forward を無視した仮定モデルを解析する」とは書かれていない。

**論理上の問題:** 同一の対象ブロックのプローブが別窓にあることは、そのブロックについて全公開情報に条件づけた記録が i.i.d. になることを意味しない。各窓の結合測定は他ブロックにもまたがり、後から公開されるそれらのパリティ・採否・測定履歴を利用できる。未知の他プローブを公開情報に条件づける前に平均化し、単一プローブの POVM に置き換えるには別の定理が必要である。衝突しない割合が大きいことだけでも、同一 POVM 最適化でも、この穴は埋まらない。

feed-forward の省略は **A4 と §VII には明示、Abstract・§V の数値説明・§VIII には明示されていない**。後三者は限定クラスのベンチマークを W 全体の結論として読ませる。cover letter と arXiv metadata にも同じ問題が伝播している。

これは W が必ず安全性を破るという反例報告ではなく、**W に対する保証がまだ導かれていない**という指摘である。衝突ブロックや最後の記憶窓を無視するなら、その処理をエントロピー損失として会計する必要もある。

**確度: 99/100。具体的な反証条件:** 全公開 transcript と他ブロックの情報を含め、任意の許容窓内測定・古典的 feed-forward を role-blind 積測定へ安全側に還元する定理を提示すること。または W についての保証を撤回し、非適応・同一単一プローブ POVM を独立の仮定として全該当箇所に明記すること。

### B2［重大］Open question の「既知の端点」が誤りで、問題そのものも未定義部分を残す

**場所:** §VII Open question、Table 4、定理1。

**確認事実:** “At $w=1$ the answer is the per-probe benchmark for odd $b$; at $w\ge n_K$ it is the adaptive value of Theorem 1” とある。しかし定理1は**測定前にブロック所属が分かる**問題であり、全プローブを保持できても測定時に分割が隠れている問題ではない。さらにこの open question は基底も後から与える。

本文自身の Table 4 は、全 n プローブを保持しても、n=6、b=2、D=0.10 で 0.8884、adaptive で 0.8981 とする。これは「全保持なら同じ」という根拠にならず、その方向の端点主張に反する証拠である。また Table 4 は対象プローブの相手が保持した n 個の中から選ばれる問題であり、大きな $n_K$ の一部分だけを保持する $w=6$ の窓問題ではない。

$w=1$ についても、確認されたのは実4出力・同一 POVM の有限数値探索であり、古典適応を含む全窓戦略の最適性ではない。guessing probability と accessible information は別々の最適化量であり、一つの「adaptive value」を両方の答えにはできない。

最低限必要なのは $n_K$、保持対象（全送信パルスか sifted single-photon probes か）、到着時刻分布、固定窓か rolling lifetime か、基底・ブロック内順序・採否・他ブロックのパリティをいつ与えるか、許容測定 instrument、Bell-diagonal パラメータの最大化範囲である。D だけでは一般 Bell-diagonal 攻撃を指定できない。

**確度: 100/100。具体的な反証条件:** 分割も基底も測定後情報のままで、全保持の場合に定理1と同じ値が得られる別の定理を与え、Table 4 との違いを解消すること。さらに $w=1$ の最適性証明またはベンチマークへの格下げと、完全な operational definition を提示すること。

### B3［重大］min-entropy の厳密値を「どの解析でも越えられない鍵率」に戻している

**場所:** §IV、§V、§VII 冒頭、§I、§VIII。

**確認事実:** §IV の積 cq 状態に対する min-entropy の加法性と、測定をブロック間で結合してもこの bound が成立するという説明は、固定した collective/product モデルと適切な条件づけの下では正しい。ここは Set 1 の修正を認める。量子 side information に対する guessing probability の operational meaning も適切である。citeturn3view0

しかし §VII は 17.66% を “what any analysis within the model can certify” と呼ぶ。厳密な **unsmoothed min-entropy** はそのまま最適抽出鍵長の上限ではない。本文自身が同じブロック局所モデルで Shannon 18.35% を示しており、文言を文字通りには維持できない。

比較基準も混線する。§V は joint Shannon 18.35% と Holevo Shannon 16.76% を挙げてから “at most 0.7 percentage points” と結論するが、同じ b=7 の両値の差は **1.59 pt**。0.69 pt は 18.35−17.66、すなわち異なる accounting と最良 b を使った比較である。0.7 pt を「表示した候補の中で最良の no-timelock certificate からの改善」と呼ぶなら説明可能だが、$1-I_E^{joint}$ と $1-\chi$ の差そのもの、または時間ロック利得の普遍上限とは呼べない。

さらに §IV の “if A2 fails … the entropic-uncertainty term … must be restored” は、直前に時間ロック不要とした min-entropy 列にも適用されるように読める。少なくとも「Shannon の特定の置換が使えない」と限定すべきで、EUR に戻すことが唯一の選択でもない。

**確度: 99/100。具体的な反証条件:** smooth min-entropy または抽出鍵長の converse を示すこと。あるいは “any analysis” を削除し、同一 b・同一 accounting・同一安全性を揃えた差と、最良 certificate 同士の差を別々に表示すること。

### B4［重大］PS 列は coherent-security certificate ではない。ε の統一も条件付き

**場所:** §IV、Table 3 と直前段落、Appendix B、Appendix C.5、Abstract、§VIII。

**確認事実:** §IV は Table 3 で “every $\epsilon$ it affects” に係数を課したとする。一方、§V は parameter-estimation intervals を **“we do not shrink”** と明記し、Appendix B は post-selection を “more than a comment” として適用できない理由を挙げる。この三つは同じ保証の説明ではない。

Table 3 は smoothing/hash にだけ係数を課した**感度分析**として有用だが、PE 予算と攻撃クラスの不変性を解決していない以上、一般 coherent attacks に対する 20.61% の保証ではない。要旨・結論の “20.6% with the post-selection factor charged” はこの限定を落としている。Appendix B のブロック次元に関する議論自体も、適用可能な reduction を与えた証明にはなっていない。

$5\epsilon_{sec}/4$ は、原典の予算に追加 smoothing を単純加算するという宣言として理解できる。T25 Lemma 4、Eq.(29) は smoothing が加算される形なので、ここに独立の係数2誤りがあるとは判定しない。min-entropy 版だけが $\epsilon_{sec}$ を満たすなら、より緩い共通上限 $5\epsilon_{sec}/4$ で表示しても矛盾ではない。ただし C.5 の最後の文が Shannon 版まで含むかは明確化が必要で、量子 side information 版の説明も §IV に追随していない。citeturn3view3

“the difference is worth less than one bit of key” も、表示式の係数4の hash 項を同一総 ε に調整すれば、主要差だけで $4\log_2(5/4)\simeq1.29$ bits となる。AEP・PE まで同一予算で再配分する場合を、単なる一ビット未満の差と断定できない。

**確度: 99/100。具体的な反証条件:** PE を含む全予算と攻撃クラス保存を追った coherent reduction を提示すること。または PS を sensitivity-only と全箇所で明示し、同一総 ε の再会計により一ビット未満という主張を実証すること。

### B5［重大］Pinsker の修正は向きが逆。C.5 に旧「coincides」が残る

**場所:** §IV 最終文、Appendix C.5 最終文。

**確認事実:** §IV は trace distance が accessible-information criterion を “through Pinsker's inequality” で抑えるとする。C.5 はなお “coincides with the accessible-information criterion” とする。

Pinsker が直接与えるのは相対エントロピーから距離への上界であり、$\delta\le\sqrt{(\ln2)D_{KL}/2}$ という向きである。小さな距離から小さな mutual information を導くなら、鍵長等を含むエントロピー連続性評価を別途使う必要がある。「同じ criterion／同じ ε」でもない。citeturn3academia12turn3view1

**確度: 100/100。具体的な反証条件:** 使用する距離・相対エントロピー・鍵長を定義し、必要方向の不等式と最終情報量予算を明示すること。C.5 の “coincides” を維持するなら、その同値性を同じパラメータで証明すること。

### B6［重大］「偶数 b の撤去」が実装されていない。奇数 b の最適性も過大表現

**場所:** Table 1、同キャプション、§III per-probe optimization、Abstract、§VIII。

**確認事実:** 修正ログ#4は Table 1 の b=2 per-probe 値の撤去を宣言した。キャプションも “reported for odd $b$ only” になった。しかし実表には **N=10^8、b=2、12.75%／13.89%** がそのまま残る。§III は “We therefore use the Helstrom benchmark for odd $b$ only” とするため、本文内でも直接矛盾する。

偶数の guessing probability 改善は §III に数値付きで開示され、Table 2 の注記も改善した。しかし Table 4 の比較対象は 0.8143 の H のままで、同じ D=0.10、b=2 の最良候補 0.8454 を併記しない。この差は隠蔽効果・結合測定効果の大きさの印象を変える。

また、実4出力同一 POVM を有限個の b・D で最適化して一致したことは、全奇数 b・全許容 POVM・全攻撃の最適性定理ではない。実際に本文が挙げる探索範囲は b=3,5,7,9、D∈[0.10,0.23]。Table 1 の b=11,15 や「odd block sizes」一般を覆う証明はない。数値最大化は敵の情報の下界を与えるので、見つけた最大値を安全性用の上界にするには追加の証明・証明書が要る。

**確度: 100/100（表の残存）、98/100（最適性の過大表現）。具体的な反証条件:** b=2 行を実際に撤去または H-only の非安全性ベンチマークとして分離すること。奇数一般の最適性については網羅性と大域上界の証明を提示するか、探索範囲内の数値的観察と書き直すこと。

### B7［高］六状態の「加算しない」は、本文の非零差と整合しない

**場所:** §III hidden bases、Abstract、§I contribution (v)、§VIII、cover letter 項目3、arXiv abstract。

**確認事実:** §III は独立に隠れた基底について、D=0.167、b=2 で guessing probability の低下を **0.0008–0.006**、D=0.259 で **0.003–0.019** と記す。それでも “Hiding the basis and hiding the parities therefore do not compound” と結論する。要旨・結論・周辺文書の “does not add … at small blocks” も、縮小したが非零の効果をゼロと表現している。

大 b の閾値を未解決とした修正は評価する。しかし「同一隠れ基底の b=2 問題で等しい」「独立基底では残余差がある」「漸近閾値は不明」を分離すべきである。最大 0.03 bits という表現も、計算した b・D・状態族の範囲を明記しなければ一様上界に見える。

BB84 についても示された equality は、記載上は $c_\varphi=1$、b=1,2 の SDP 結果である。要旨の “does not help BB84 in guessing probability” は、その範囲を越えた全 b の定理と読める。

**確度: 99/100。具体的な反証条件:** 独立基底での非零区間を撤回する検証結果、または全 b の no-gain theorem を示すこと。そうでなければ「検討した小ブロックでは利得が縮小するが残る」に統一すること。

### B8［高］時刻・窓のモデルが混在し、4×10^-4 は限定条件付きの概算

**場所:** A1/A2/A4、§VII。

**確認事実と手計算:** $\binom92(10^9)(1)/10^{14}=3.6\times10^{-4}$ なので、**書かれた式を一桁に丸めて 4×10^-4 とする算術は正しい**。これを新たな計算ミスとして非難すべきではない。

ただし、固定された互いに素な窓に各 w 個のプローブが入る模型なら、二つの異なる到着位置が同じ窓に入る確率は $(w-1)/(N-1)$ であり、上記はペア union bound の先頭次数である。一方、A1 の「各プローブの寿命が $t_{coh}$」という rolling lifetime なら、二つの一様到着時刻の差が $t_{coh}$ 未満となる確率は $2r-r^2$、$r=t_{coh}/T_{run}$。小 r の先頭次数は約2倍で、b=9 のペア和は約 $7.2\times10^{-4}$ となる。どちらも厳密な accepted/single-photon block の比率ではなく、その条件づけと高確率評価がさらに必要である。

A2 の「$t_{coh}\ll T_{run}$ なら every probe を全告知前に測定する」も厳密には誤りで、run 終了前 $t_{coh}$ のプローブは告知時に残り得る。A1 が $t_{comp}$ を暗号の使用からの時間と定義しているのに、A2 が encryption delay を $t_{comp}-t_m$ とする点にも時刻原点の不整合がある。

T25 がランダムに分割する対象は送信 N 個そのものではなく、sifting・test・vacuum removal 後の $n_K$ 個である。送信レート f と sifted rate の違いを、§VII の $w=ft_{coh}$ と $w\ge n_K$ にも反映する必要がある。原典 p.4 step 5 の定義が基準となる。citeturn2view5

**確度: 100/100（算術）、98/100（モデル不整合）。具体的な反証条件:** 固定窓か rolling lifetime かを一意に指定し、実際の sifted/accepted 標本への条件づけと末尾窓の処理を含む有限標本 bound を示すこと。時刻原点も統一すること。

### B9［高］不利な数値は隠されてはいないが、要旨・結論で対称に提示されない

**場所:** Abstract、§V、§VIII、Tables 1/3/4、cover letter。

- **PS:** 本文には b=9 の H Shannon **20.81→19.39%** があるのに、要旨・結論は **20.7–20.8% (20.6% PS)** と異なる accounting をまとめる。20.6% は H min-entropy 20.61% であり、両方の値がほぼ保たれるわけではない。
- **Holevo:** 16.40/16.76/15.59% は Table 3 と本文に出た。これは改善。ただし要旨・結論の0.7 ptは、同一 Shannon accounting の差ではない（B3）。
- **偶数 b:** 改善値は §III にあるが、Table 1 の未撤去行と Table 4 の H 比較だけでは不十分（B6）。
- **n=6:** 0.8884 は本文・Table 4 にあり、要旨も結合測定が adaptive の大半を回収すると述べる。この点に隠蔽を認定しない。ただし n≤6 の結果から “protects only through locality” という一般命題は導けない。大 n の挙動は open とすべきである。
- **同一 b:** §V には b=9 と最良 b の両方が書かれたが、要旨・結論には b=9 の指定がない。17.66% は b=11、20.66/20.81% は b=9 で、H min-entropy の表示範囲内最良値は b=15 の21.83%。条件の非対称性は解消しきっていない。

**確度: 99/100。具体的な反証条件:** 要旨・結論にも accounting、b、総 ε、PS が感度分析であることを付し、19.39% を含む対応関係を示すこと。全保持小 n と大標本窓模型を明確に分離すること。

### B10［中］新規性の帰属は改善したが、BA07 の個別攻撃を W の定理に読み替えないこと

**場所:** §I、§III、§VII、cover letter。

BA07 §III A は、同じ相互作用を各信号に施し、その直後に測定する individual attack を定義する。§IV C はこの制限下で CAD1 と CAD2 が非同値になると論じる。原典の25%を、窓内の任意の結合測定を許す W にそのまま帰属できない。本稿の定理は、より強い測定クラスでは「パリティ非公開だけ」では十分でないと示す拡張であって、BA07 の明示した個別攻撃の結論を否定するものではない。citeturn2view3turn2view4

CHT18 は、事前・事後情報で最適 guessing probability が等しいことと、各部分問題に両立可能な最適測定があることの同値性を既に与える。本稿の独自性はこの一般論自体でなく、対象のパリティ ensemble の任意 b に対する明示的な共通測定構成にある。今回この区別を本文に書いた点は適切である。citeturn3view2

**確度: 96/100。具体的な反証条件:** BA07 が現在の W を明示的に許した一次資料箇所を示すこと。CHT18 と同一の具体的構成が既出である証拠が出れば、新規性の肯定評価も下げる。

### B11［中］周辺文書の更新は実在するが、投稿可能な一貫したパッケージには未到達

**場所:** cover letter、README、arxiv-metadata、declarations、図キャプション。

確認した cover letter と README は既に v2 系の内容であり、「周辺文書が全部旧版のまま」とは判定しない。しかし cover letter と arXiv abstract は B1/B7 の過大主張を引き継ぐ。arXiv abstract には引用除去でできた **“Ref. .”** が複数あり、独立した要旨として読めない。文字数は末尾改行込み1790で、1789文字という表示自体を問題とはしない。

README は高精度 `asymptotic_mp.py` を列挙する一方、再現コマンド欄は `asymptotic.py` のままで、新規 PS、per-probe、hidden-partition の実行経路もない。検証済み一覧も “Tables I–II” のまま、現在の4表と同期していない。これは本査読で再実行した結果ではなく、案内の欠落である。

declarations に旧科学的強主張はない。ただし funding、prior posting、日付等のプレースホルダーが残り、最終投稿書類としては未完成。元の blanket no-go 文言が消えたことと、投稿一式の完了は別である。

**確度: 100/100（文面）、95/100（再現案内の不足）。具体的な反証条件:** 引用の欠落、過大主張、旧再現案内、プレースホルダーを修正し、実際の投稿対象一式に同じ変更が反映された確認記録を示すこと。

### B12［低］Appendix A の「iff」は c=0 で偽だが、定理本体の反例ではない

**場所:** Appendix A、Lemma 1 の前の積期待値の説明。

**確認事実:** $\langle\Psi|X^wZ^s|\Psi\rangle=0$ であることを、w と s が共通位置を持つことと “if and only if” で結んでいる。しかし許容範囲 $|c|<1$ は c=0 を含む。w=0、s に一つの1がある場合にも $\langle\psi_0|Z|\psi_0\rangle=c=0$ で、共通位置なしに積がゼロになる。

Lemma 1 が必要とするのは共通位置があればゼロという十分条件なので、これは局所的な記述修正で済み、定理1を破るとは判定しない。

**確度: 100/100。具体的な反証条件:** c=0 が除外されているか、当該文が十分条件だけを主張していることを示すこと。現在の定理文は c=0 を許す。

## 13項目の「宣言対実装」照合

「実装済み」はここでは文面・保存ファイルへの反映を意味し、新たな数値的再現保証ではない。

| # | 判定と確認した証拠 | 確度 | 具体的な反証条件／閉じる条件 |
|---|---|---|---|
| 1 | **部分実装。** A2 の “random partition”、A4 の J/W/H、§VII open question、n≤6 の Table 4 はある。しかし W の帰着を要旨で断定し、open question の端点も誤る（B1/B2）。 | 99 | W 還元と端点の定理、または仮定・未解決への一貫した格下げ。 |
| 2 | **部分実装。** §IV の “does not use the timelock at all”、Shannon の積測定限定、Table 3 の Holevo 16.40/16.76/15.59 は存在。§VII の “what any analysis … can certify” と0.7 ptの比較混線が残る。 | 100 | B3 の converse か比較表の修正。 |
| 3 | **部分実装。** 60 log₂(N+1)、AEP 約4.8倍、Table 3、Appendix B の16^b−1は存在。PE未計上なのに “every ε” とする。PS数値は保証でなく感度分析。 | 100 | 全 ε の実会計と適用可能な reduction、または sensitivity-only 表示。 |
| 4 | **宣言と不一致。** §III の0.8454/0.9246、Table 2注、C.2の一般POVM記述はあるが、撤去宣言した Table 1 の b=2、12.75/13.89% が残る。 | 100 | 実表からの撤去または明確な別枠化。 |
| 5 | **文面反映済み。** §V に “at most 0.16 … at N=10^14” と “up to 0.8 … at N=10^8”。旧≤0.15の一律主張ではない。 | 100 | 指定版でこの訂正が存在しない、または対象表と違うとの具体的証拠。 |
| 6 | **文面・保存CSV反映済み、図再生成は未検証。** §V/図キャプションに60桁、b=41,61。CSVのf=1.2、b=31はEUR 19.1776%、joint Shannon 19.7301%。通常CSVの該当EUR値も高精度CSVと一致。 | 98 | 提出図が旧値を描く証拠、または生成 provenance の不一致。再ビルドは本査読対象外。 |
| 7 | **本文と保存データは反映。** §VII は対称族の21.89%対20.86%を明記。`data/panel_variants.csv` に21.8858%と16.1977%がある。quick再実行・全quickファイル同値は未検証。 | 98 | 対応する保存行が別条件、または現行quick出力が一致しない検証。 |
| 8 | **反映済み。** §III は “close to D=1/4 the maximiser moves”、b=2でD≥0.206、b=9でD≥0.239と明記。C.1も “at the error rates of interest” に限定。 | 99 | 「全 b≥2 で常に最大」とする未限定の対象版記述を示すこと。 |
| 9 | **未完了／誤修正。** §IV と C.5途中に5ε/4はあるが、C.5末尾の “coincides” が残り、§IVのPinskerは逆向き。 | 100 | B4/B5 の正しい予算と情報量不等式。 |
| 10 | **帰属修正は実装。** BWW08へのBB84 no-gainの誤帰属は外れ、本人のSDPとBAL11のShannon +0.8 ptを区別。ただしb=1,2の結果の一般化は残る。 | 98 | 全bへの定理、または要旨等への範囲明記。 |
| 11 | **部分実装。** §III/§VIIに大b未解決がある。しかし “do not compound” と、小ブロックでも “does not add” が本文・周辺文書に残る。 | 100 | B7の非零区間と整合する表現への統一。 |
| 12 | **撤回は実装。** “every timelock-restricted adversary” はなく、Appendix B末尾は coherent extension を open とする。ただし§IV/Table 3の読み方が追随しない。 | 99 | PS列がcoherent保証ではないことの全箇所での明記。 |
| 13 | **部分実装。** 定理の\|c\|<1、A4置換、CHT18本文引用、11個のtest関数は確認。§Vはb=9と最良bを分離。しかし要旨はb=9を明記せず、比較非対称とW帰着の問題を残す。テスト成功は再検証していない。 | 99 | 要旨まで条件を統一し、テスト実行が必要なら別途結果を提示。 |

## 較正の伝播監査：見出し・キャプション・付録・周辺文書

以下は確認した対象版における一覧。図内文字・PDFの視覚的再検証、配布zip内部の同一性までは認証しない。

| 対象 | 旧強主張の残存／限定の不足 |
|---|---|
| タイトル | “Does hiding the post-processing … ? … the 20% barrier” のまま。疑問形なのでそれ自体は偽のno-goではないが、三種類の隠蔽と推測確率への限定を表さない。 |
| Abstract | Wへの帰着、奇数一般の最適性、PS 20.6%、BB84全般no-gain、六状態small-block no-add。feed-forward省略なし。B1/B4/B6/B7/B9。 |
| §I Introduction | contribution (iv) の “reduction” と (v) の基底no-add。数値探索と定理を分ける必要。 |
| §II Model assumptions | 見出し自体は中立。A4の条件付き仮定と還元の断定が混在。A2のevery probe、時刻原点の誤り。 |
| §III The adversary's information on the distilled bit | 主見出しは中立。小見出し “Is the Helstrom benchmark the best per-probe measurement?” への答えは数値探索に限定すべき。“Hiding … therefore do not compound” は残存。 |
| §IV Finite-key secure key length | 見出しが保証を示すため、W未証明・collective限定・PS非保証を明示すべき。本文に “must be restored”、逆向きPinskerが残る。 |
| §V Numerical results | 見出しは中立。HをWの数値に読む問題、0.7 ptの比較混線、feed-forward省略なし。 |
| §VI Implementation considerations | 見出しは中立。“neither is worth paying for in order to hide the parities” はguessing probability/min-entropyへの限定がない。本文が認めるShannon利得とも緊張する。実装費用と利得の比較を実証していない。 |
| §VII Discussion | 見出しは中立。“what any analysis … can certify”、Wの断定、誤ったopen-question端点が残る。feed-forward但し書きはある。 |
| §VIII Conclusion | Abstractと同じ過大主張。feed-forward省略なし。 |
| Table 1 caption | collective/J-Shannon/Hのラベル改善。ただし “odd b only” と実表b=2が矛盾。 |
| Table 2 caption | 偶数bでH非最適と明記済み。ここは修正が届いている。 |
| Table 3 caption | smoothing/hashに限定する語はあるが、PE未計上・coherent証明ではないことをキャプションだけでは十分伝えない。 |
| Table 4 caption | n個全保持・probe 1の相手を事後開示という設定は明記。真のw窓問題とは違う。比較は最適per-probeでなくH。 |
| 図1（内部Fig.2）caption | “individual measurement” はHのベンチマークであることを明記した方がよい。20/25%線をWの保証として読ませないこと。 |
| 図2（内部Fig.3）caption | “Secure key rate” とper-probe benchmarkを併記。H条件・安全性範囲・feed-forward制限がキャプションにない。 |
| 図3（内部Fig.4）caption | 60-digit arithmeticへ更新済み。per-probe/jointの範囲と各accountingの違いの明記は不足。 |
| Appendix A | 見出しは正確。既知分割の定理であり、未知分割への拡張はない。c=0で偽の “iff” を修正。 |
| Appendix B | 見出しは “Twirling, post-selection and block locality” に更新。blanket coherent-security claimは撤回済み。本文/PSの読み方との統一が必要。 |
| Appendix C.1–C.4 | C.1のworst-case限定、C.2の一般POVM、C.3のH/J別漸近条件、C.4のBell-diagonal式はある。C.3の25%をW全体に外挿してはいけない。 |
| Appendix C.5 | 古典side-informationのみの説明、旧 “coincides”、εの適用範囲が残る。§IVの量子min-entropy列と分けて整理する必要。 |
| cover letter | 三分法へ更新済み。しかし項目2のW帰着と項目3のsmall-block no-addは未較正。Shannon残余利得も説明しない。 |
| README | 旧 blanket no-go の科学的説明は見当たらない。v2化は実在。高精度・新規表の再現案内、検証済み表番号が未同期。 |
| arXiv metadata | 要旨の過大主張を継承。“Ref. .” が残存。 |
| declarations | 旧科学的強主張はない。資金・投稿情報の未入力欄が残る。 |

確度は文面の存在について **99–100/100**。この一覧の反証条件は、指定した対象版に当該文が存在しない、または同じ表示箇所に十分な限定が既に存在することの提示である。見出しだけを「旧強主張」として数えず、一般的な見出しと実際の断定を区別した。

検索例に挙げられた **“buys nothing beyond unconditional security”, “returns to 17.3–18.4%”, “within 10^-3”, “every timelock-restricted adversary”, “memory of block length”, “microseconds”** は、今回確認した指定本文・周辺文書・TeXキャプションでは旧結論として見つからなかった。近い旧論理が **“what any analysis … can certify”** と **“do not compound”** に残っていることが問題である。定理検証の10^-7等や、n=6で「1 percentage point以内」という別の正しい限定数値を、旧10^-3主張と混同しない。

## Open question を回答可能にする最小の修正文針

まず基底既知の単一光子・固定Bell-diagonal状態族に限定し、全 $n_K$ プローブの時刻とランダム分割Π、採否A、パリティCを定義する。その上で、許容される窓付き instrument の集合 $\mathcal W$ と、その全古典記録Rに対し、例えば

$$P^{\mathcal W}_{\rm guess}(n_K,w,b,D,c_\varphi)
=\sup_{\mathcal I\in\mathcal W}P_{\rm guess}(K_j\mid R,\Pi,C,A),$$

を、対象ブロックjの選び方・採択条件を含めて定義する。accessible information は同じ制約下の別の supremum として定義する。鍵全体の安全性には、単一bitの量だけでなく全鍵の conditional smooth min-entropy またはその有効な下界が必要である。

- w=1：H は明示的な実現可能ベンチマーク。制限された同一POVM数値探索との一致は既知だが、全戦略の最適性とは書かない。
- 全保持・分割事後：独立の事後情報識別問題。adaptive値は上界であり、定理1だけから等号とは書かない。
- 全保持・分割事前・パリティ事後：ここが定理1の解く端点。
- Table 4：全保持・対象ペアの相手だけが事後に分かる小n問題として位置づけ、窓問題のw≤6の解とは呼ばない。

この修正は問題を解いたことではなく、何を解くべきかの明確化である。**確度: 98/100。反証条件:** 現稿のモデルからこれらの区別が不要と分かる一意な定義と還元が提示されること。

## 収束判定

**科学的較正のループ: 未収束。** パリティの限定定理、量子min-entropy列の独立性、既知の文献関係は改善した。しかし W の帰着と open question の端点を誤ったまま、Abstract/Conclusion が数値的保証を約束している。B1–B9を解消しない限り、Set 1の核心が別の形で再発している。**確度: 99/100。反証条件:** 上記の未証明な帰着・誤端点・会計・情報量変換を解消した一貫した版と根拠を提示すること。

**パッケージ整合のループ: 未収束。** v2への実際の更新は認めるが、Table 1の撤去不履行、C.5の旧文、要旨/結論/cover letterの同じ過大主張、arXivの空引用、READMEの再現案内に不整合が残る。**確度: 100/100。反証条件:** 同一原稿から生成された投稿一式について、13項目の差分照合と本文・図表・要旨・周辺書類の同期を確認できること。

**最終勧告:** 定理1を中心成果、Hの閾値を明示した制限モデルのベンチマーク、分割隠蔽と一般窓攻撃を未解決問題として提示するなら論文は救える。現版を「窓付き敵に20.6%を保証した較正済み論文」として投稿することは支持しない。
