# J. Phys. A 形式要件 × 成果物 照合表（S12 再実行、2026-10-29）

出典: IOP Publishing 投稿ガイド（format-free submission）、https://publishingsupport.iopscience.iop.org/journals/journal-of-physics-a-mathematical-and-theoretical/ （2026-10-29 取得）

| # | 要件 | 成果物での充足 | 状態 |
|---|---|---|---|
| 1 | 初回投稿は format-free: 単一 PDF、図表は本文に埋め込み、12 pt 以上の読みやすいフォント | `main.pdf`（revtex4-2 `preprint,12pt` 単段、31 頁、図表埋め込み）。`main.tex` は改訂時用 | OK |
| 2 | 題名: 簡潔・検索語を含む・非標準略語なし | 11 語の名詞句、"advantage distillation"・"quantum key distribution" を含む | OK |
| 3 | 要旨 ≤ 300 語、略語定義、図表・式・文献への参照なし | 229 語、引用なし、QBER を展開（"quantum bit error rate"）、BB84 は標準名 | OK |
| 4 | 本文はローマ字のみ、行番号は自動付与 | 該当 | OK |
| 5 | 単盲査読: 著者・所属を冒頭に記載 | 著者 1 名・所属・メール記載 | OK |
| 6 | 補足データ: 各ファイル ≤ 50 MB、合計 ≤ 150 MB、題名 ≤ 30 字・説明 ≤ 30 語をファイル内に | `supplemental_material.zip`（72 KB）、`supplemental/README_anc.md` に題名・説明 | OK |
| 7 | 研究データ・コードの公開を推奨 | GitHub release v2.1（MIT / CC BY 4.0）、原稿 Data availability 段落と [Wak26] | OK |
| 8 | プレプリント方針: 著作権移転前なら可 | Research Square 10.21203/rs.3.rs-11453979/v1（旧題名）を宣言・カバーレターに記載 | OK |
| 9 | 投稿先: ScholarOne（https://iopscience.iop.org/journal/1751-8121/page/submission-options） | ユーザー作業 | 未 |
| 10 | 投稿衛生（CLAUDE.md）: 改訂経緯・査読者言及・撤回数値なし | `grep -inE "corrected|earlier (revision|draft)|previously reported|referee|phase-1" main.tex` → 0 件；印字数値は v2.1.3 から不変（S17 継承） | OK |
| 11 | 過去投稿歴 | PRA AX13009 は査読前不採択（技術的指摘なし）。IOP は開示を要求しない；APS 再投稿時のみ開示義務 | 記録のみ |
