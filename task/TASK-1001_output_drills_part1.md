# 執筆指示書: TASK-1001_output_drills_part1

- **担当**: 編集長（Director）
- **対象記事**: 1001〜1010（瞬間口頭作文＆パターンプラクティス 前半10本）
  - 1001: 基本語順（SVO）と名詞修飾（DM則）の即時産出 (`docs/output/01-svo-word-order.md`)
  - 1002: 否定詞 tidak と bukan の反射的使い分け (`docs/output/02-negation-tidak-bukan.md`)
  - 1003: 親称代名詞（Anda, Bapak, Ibu, Mas, Mbak）の適切な使い分け (`docs/output/03-pronouns-kinship.md`)
  - 1004: 指示詞 ini / itu と場所表現（di sini / ke sana）の瞬発力 (`docs/output/04-demonstratives-ini-itu.md`)
  - 1005: 疑問詞（apa, siapa, di mana, kapan, kenapa, bagaimana）の即座疑問文 (`docs/output/05-question-words-5w1h.md`)
  - 1006: アスペクト副詞（sudah, belum, sedang, akan, pernah）の反射文生成 (`docs/output/06-aspect-markers.md`)
  - 1007: 前置詞（di, ke, dari, pada, kepada）の場所・方向マッピング (`docs/output/07-basic-prepositions.md`)
  - 1008: 抽象前置詞（untuk, bagi, demi, tentang, menurut）の文脈適用 (`docs/output/08-abstract-prepositions.md`)
  - 1009: 助動詞（harus, boleh, bisa, mau, ingin）のニュアンス即座出力 (`docs/output/09-auxiliary-verbs.md`)
  - 1010: 比較級・最上級・同等比較（lebih, paling, ter-, sama...dengan） (`docs/output/10-comparison-patterns.md`)

## 執筆要件
1. **SLA理論（DeKeyser スキル習得理論）の徹底**:
   - 単なる説明ではなく、日本語刺激から1〜2秒でインドネシア語文を脳内生成する「瞬間口頭作文（Pushed Output）」の仕組みを実装する。
   - 各記事に「瞬間作文ドリル 15〜20本ノック（日本語 → インドネシア語正解・語順構造解説・カタカナ発音・解説）」を必ず掲載する。
2. **デザインコンポーネントの活用**:
   - `.id-example`（`.id-sentence`, `.id-reading`, `.id-meaning`）
   - パターン比較用 Markdown テーブル
3. **インバリアント遵守**:
   - ❌ ルビ構文（`{単語|読み}`）は使用禁止。
   - 太字・約物ルール（`「**強調内容**」`）の遵守。
   - 理解度チェッククイズ（3問）の設置。
