---
asset: venue-decision
version: 1.1.0
生成元入力: theme-brief.md v1.0.0, manuscript.md v0.9.0, manuscript-REVIEW.md v1.0.0
依存工程: S10（S4, S9, S18 後）
生成日: 2026-10-09
---

# 投稿先決定

原稿の性格: 負の結果（タイムロック AD は無条件限界を超えない）＋ 先行研究（Bae–Acín 2007）の限定条件の明確化 ＋ 有限鍵数値 ＋ T25 実装上の注意。理論・数値中心、実験なし、約 6,500 語・図 3・表 2・参照 31。組版は revtex4-2（paper/main.tex）。

| 候補 | 適合度 | スコープ一致 | 形式要件 | 締切 | 判断 |
|---|---|---|---|---|---|
| Phys. Rev. A（Regular Article） | 高 | QKD 安全性解析・攻撃モデル・有限鍵数値は PRA の中心領域。Bae–Acín 2007、Acín et al. 2006、Lim et al. 2014、Fung et al. 2012 など本稿の主要参照が PRA 掲載 | revtex4-2（現状のまま）、長さ制限なし、図は PDF/EPS、要旨 ≤ 600 字相当、補足資料可。査読は単盲 | 随時 | **第 1 候補** |
| Quantum | 中〜高 | 理論的に明快な負の結果と予想（Conjecture 1）は Quantum の読者に合う。arXiv 公開が前提で S11 と整合 | quantumarticle クラスへの変換が必要（revtex からの移植は軽微）、長さ制限なし、要旨 ≤ 250 語目安、オープンアクセス（APC は任意、投稿時に確認） | 随時 | 第 2 候補（PRA で不採択時、または Conjecture 1 を証明できた場合は第 1 候補に昇格） |
| Phys. Rev. Applied | 中 | 実装（FPGA）が主眼なら適合だが、本稿では §6 を縮約し負の結果が主眼のため応用誌の期待と合わない | revtex4-2、長さ制限なし | 随時 | 見送り |
| New J. Phys. | 中 | BAL11 の掲載誌系列（J. Phys. A）に近いが、負の結果の受容性は PRA と同程度でオープンアクセス費用が必要 | IOP テンプレート、APC 必要（投稿時に確認） | 随時 | 予備候補 |
| npj Quantum Information | 低〜中 | 「新しい正の結果」志向が強く、負の結果・予想中心の本稿には不利 | Nature 系テンプレート、APC 必要 | 随時 | 見送り |

## 決定と理由
- **決定: Phys. Rev. A（Regular Article）に投稿。** 理由: (i) 本稿の対話相手である Bae–Acín 2007 と Acín et al. 2006 が PRA 掲載であり、同誌での応答が最も自然。(ii) 現在の revtex4-2 組版をそのまま使え、長さ制限がない。(iii) 負の結果でも数値・モデルが明確なら PRA の査読基準で評価される。
- **プレプリント: S11 で arXiv（quant-ph）に公開する**（PRA は arXiv 事前公開を認める）。arXiv 公開は投稿前に行い、投稿時に arXiv 番号を記載する。
- **S11/S12 の要否: 両方必要。** S11（arXiv バンドル: main.tex, figures/, bib 相当の参照, データ・コードの参照先）→ S12（PRA 投稿バンドル: 同一ソース＋カバーレター＋提案査読者）。**いずれも実行前にユーザー承認が必要（progress.md 保留中の承認）。**
- 補足: Conjecture 1 の一般 b 証明が得られた場合は Quantum を第 1 候補に再検討する（S10 再実行）。

確度: 80 / 根拠: 各誌の形式要件は公開投稿ガイドの一般知識に基づく（2026-10-09 時点の料金・字数は投稿時に再確認。未照合）。適合度判断は主要参照の掲載誌（一次出典の書誌）に基づく。

## 決定の確定（2026-10-15）
- ユーザー決定: **Physical Review A（Regular Article）**。定理 1 を得た後も PRA を維持（Bae–Acín / Acín et al. への応答という位置付けを優先）。不採択時の第 2 候補は Quantum。
- S12 実施: submission-bundle/（main.tex、figures/、supplemental_material.zip、cover_letter.md、suggested_referees.md、declarations.md、requirements.md）。
