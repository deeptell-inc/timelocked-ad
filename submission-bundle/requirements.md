# PRA 形式要件 × 成果物 照合表（S12 手順 1–3）

| # | 要件（APS/PRA 投稿ガイド） | 成果物での充足 | 状態 |
|---|---|---|---|
| 1 | REVTeX 4.2、`pra` オプション、two-column 可 | `main.tex`: `\documentclass[aps,pra,twocolumn,superscriptaddress,nofootinbib]{revtex4-2}` | OK |
| 2 | 題名・著者・所属（superscriptaddress）、責任著者連絡先、ORCID | 著者 1 名・所属・メール記入済（ORCID は任意） | OK |
| 3 | 要旨: 単一段落、数式・引用は最小限、簡潔 | 295 語・単一段落、引用 1 件（[T25]） | OK |
| 4 | 本文: 節構成、式番号、図表番号の参照整合 | hyperref で全参照解決（undefined 0）、図 1–3・表 I–IV | OK |
| 5 | 図: 個別ファイル（PDF/EPS）、印刷で判読可能、カラー可 | `figures/fig2_eve_info.pdf`, `fig3_rate_vs_qber.pdf`, `fig4_threshold_vs_b.pdf`（ベクタ PDF） | OK |
| 6 | 参考文献: 著者・誌名・巻・頁・年（APS 形式、題名任意） | `thebibliography` 39 件、全て本文で引用、arXiv 番号併記 | OK |
| 7 | 補足資料（Supplemental Material）: 別ファイル、本文から参照 | `supplemental_material.zip`（code + data + README）；本文 §V/§VI で「deterministic Python module」として言及、Declarations で明示 | OK |
| 8 | 投稿衛生: 改訂履歴・撤回数値・査読者言及なし（CLAUDE.md 規則） | grep（corrected / earlier revision / previously reported / referee / phase-1 / conjectur*）該当なし | OK |
| 9 | 二重投稿なし、プレプリント方針（arXiv 可） | カバーレターに arXiv 番号欄；APS はプレプリント公開を許容 | **arXiv 番号要記入** |
| 10 | カバーレター（任意だが推奨）: 意義、PRA 適合、推薦査読者 | `cover_letter.md`、`suggested_referees.md` | OK（著者欄要記入） |
| 11 | 宣言: 利益相反、資金、データ可用性、倫理 | `declarations.md` | OK（資金・ORCID 要記入） |
| 12 | 長さ制限 | Regular Article に制限なし（14 頁） | OK |
| 13 | 数値の事実ゲート（S17） | S11 ゲートと同一の `main.tex`（差分なし）を再検証 | OK（下記ログ） |
