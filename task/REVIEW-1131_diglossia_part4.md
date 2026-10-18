# 校正・検証タスク: REVIEW-1131 (二重言語 第4バッチ 1131-1140)

## 1. 対象記事
- 1131: `docs/diglossia/31-javanese-colloquial-elements.md`
- 1132: `docs/diglossia/32-sundanese-colloquial-elements.md`
- 1133: `docs/diglossia/33-chinese-indonesian-peranakan.md`
- 1134: `docs/diglossia/34-surabaya-east-java-slang.md`
- 1135: `docs/diglossia/35-medan-north-sumatra-elements.md`
- 1136: `docs/diglossia/36-movie-subtitles-vs-audio.md`
- 1137: `docs/diglossia/37-podcast-talk-show-register.md`
- 1138: `docs/diglossia/38-dating-pdkt-romance-slang.md`
- 1139: `docs/diglossia/39-emotion-exclamations-gokil.md`
- 1140: `docs/diglossia/40-workplace-gossip-character.md`

## 2. 校正（Reviewer）チェック
- [x] ルビ構文（`{...|...}`）不使用の徹底（アルファベット＋カタカナ発音欄）
- [x] 太字約物記法（`【タグ】「**日本語**」（原語）`）遵守
- [x] 方言・プラナカン・若者スラングの語彙・用例の適切性
- [x] 15問ノック＋3問クイズの構成
- **判定**: `APPROVED`

## 3. エンジニア（Engineer）検証
- [x] `python task/lint_markdown.py` エラー0件
- [x] `zensical.toml` の `nav` 登録確認
- [x] `zensical build` 検証
