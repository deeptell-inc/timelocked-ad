# Quantum Information Processing 形式要件 × 成果物 照合表（S12 再実行、2026-11-12）

出典: https://link.springer.com/journal/11128/submission-guidelines （2026-11-12 取得）

| # | 要件 | 成果物での充足 | 状態 |
|---|---|---|---|
| 1 | LaTeX ソース一式（スタイル・図を含む）＋コンパイル済み PDF。Springer Nature テンプレートは「推奨」 | `main.tex`（revtex4-2 `preprint,12pt` 単段、文献は thebibliography でインライン）、`figures/` 3 点、`main.pdf`（32 頁）。sn-jnl クラスはローカル未導入のため未使用 | OK（テンプレートは推奨止まり。編集部が求めたら移植） |
| 2 | タイトルページ: 題名、著者、所属、責任著者メール、ORCID（あれば） | 題名 10 語、著者 1 名・所属・メール記載。ORCID 未記入 | ORCID は著者判断 |
| 3 | 要旨 150–250 語、未定義略語・未特定の文献参照なし | 219 語、文献参照なし、略語なし（BB84 はプロトコル名） | OK（注: 同ページの単盲査読の節には「80–100 語」とあり記述が不一致。Title Page 節の 150–250 語に従った） |
| 4 | キーワード 4–6 個 | 5 個（`\keywords`） | OK |
| 5 | 本文に "Statements and Declarations" 見出しで Competing Interests を記載 | Appendix 直前に節を設置（Competing interests、Data availability、Author contributions） | OK |
| 6 | Data Availability Statement 必須、データ引用は文献リストに | 同節に記載、[Wak26]（GitHub release v2.1）。DOI は未付与 | OK（DOI 推奨） |
| 7 | Funding・Author contribution・Competing interest を投稿フォームに入力 | `declarations.md` に文面 | Funding は著者記入 |
| 8 | LLM 利用（コピー編集を超えるもの）は本文に記載 | `declarations.md` に草案、`make_qip_tex.py` の `AI_USE` で本文に挿入可能 | **著者判断** |
| 9 | 文献: 角括弧の番号引用、引用した文献のみ、DOI があれば記載 | 番号引用（revtex）、全件本文で引用。書式は APS 様式のまま、DOI リンクは未付与 | 採択後の組版で調整可 |
| 10 | 見出しは 3 階層以内の十進法 | 節番号は revtex のローマ数字 | 軽微（テンプレート移植時に解消） |
| 11 | 補足情報: 標準形式、各ファイルに論文題名・誌名・著者・所属・メール、本文で "Online Resource" として言及、ファイル名 ESM_n | `ESM_1.zip`（README_anc.md に題名・誌名・著者・所属・メール）、Data availability で "Online Resource 1" に言及 | OK |
| 12 | 推薦査読者: 所属機関メールまたは本人確認リンクを添える | `suggested_referees.md`（6 名、メール未記載） | 著者記入 |
| 13 | 未発表・他誌で審査中でないこと | PRA（AX13009）・J. Phys. A（JPhysA-126466）はいずれも査読前不採択で審査終了。プレプリントは Research Square（旧題名） | OK |
| 14 | 投稿衛生（CLAUDE.md） | `grep -inE "corrected|earlier (revision|draft)|previously reported|referee|phase-1" main.tex` → 0 件；印字数値は v2.1.3 から不変（S17 継承） | OK |
