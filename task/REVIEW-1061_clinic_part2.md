# 校正レビュー報告書: TASK-1061 (クリニック 1061-1070)

## 1. 対象記事
- 1061: `docs/clinic/11-bukan-tidak-with-adjectives.md` (bukan/tidak with adjectives)
- 1062: `docs/clinic/12-oleh-agent-overuse.md` (oleh agent overuse)
- 1063: `docs/clinic/13-jam-waktu-pukul-clash.md` (jam, waktu, pukul clash)
- 1064: `docs/clinic/14-banyak-orang-word-order.md` (banyak orang vs orang banyak)
- 1065: `docs/clinic/15-sangat-sekali-redundancy.md` (sangat... sekali redundancy)
- 1066: `docs/clinic/16-untuk-preposition-overuse.md` (untuk preposition overuse)
- 1067: `docs/clinic/17-dengan-preposition-misuse.md` (dengan preposition misuse)
- 1068: `docs/clinic/18-dari-daripada-confusion.md` (dari vs daripada)
- 1069: `docs/clinic/19-tentang-mengenai-overuse.md` (tentang/mengenai overuse)
- 1070: `docs/clinic/20-sebagai-position-misuse.md` (sebagai position misuse)

## 2. 検証項目
1. **語法・正書法**:
   - `bukan` と `tidak` の否定対象（名詞句 vs 述語・形容詞・動詞）の明確な対比。
   - `oleh` の省略規則（動詞直後の行為者は不要、離れる場合のみ必須）の解説。
   - `jam`（時刻・時間数・時計）、`waktu`（時・時期・接続詞）、`pukul`（公式時刻点）の区分。
   - `banyak orang`（不特定多数の個人）と `orang banyak`（群衆・大衆）の語順によるニュアンス変化の解説。
   - `sangat ... sekali` 二重強調の不自然さと自然な代替表現（`sangat bagus` または `bagus sekali`）。
   - 前置詞 `untuk`, `dengan`, `dari/daripada`, `tentang`, `sebagai` の過剰使用・直訳癖への的確な処方箋。
2. **フォーマット規約**:
   - ルビ構文不使用（アルファベット＋カタカナ発音欄）。
   - 太字約物記法（`「**強調**」`）遵守。
   - 各記事15問の瞬間口頭作文ドリル＋3問の選択式クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
