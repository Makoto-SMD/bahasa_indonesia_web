# 校正・検証タスク: REVIEW-1161 (戦略会話 第2バッチ 1161-1170)

## 1. 対象記事
- 1161: `docs/strategies/11-restatement-paraphrase.md`
- 1162: `docs/strategies/12-spelling-spelling-out.md`
- 1163: `docs/strategies/13-phone-connection-trouble.md`
- 1164: `docs/strategies/14-zoom-online-meeting-trouble.md`
- 1165: `docs/strategies/15-interrupting-politely.md`
- 1166: `docs/strategies/16-resuming-after-interruption.md`
- 1167: `docs/strategies/17-checking-unknown-word.md`
- 1168: `docs/strategies/18-explaining-japanese-concept.md`
- 1169: `docs/strategies/19-negotiating-price-limits.md`
- 1170: `docs/strategies/20-handling-complaints-calmly.md`

## 2. 校正（Reviewer）チェック
- [x] ルビ構文不使用の徹底（アルファベット＋カタカナ発音欄）
- [x] 太字約物記法（`【タグ】「**日本語**」（原語・状況）`）遵守
- [x] 通信トラブル、割り込み、文化説明、クレーム初期対応の実践的妥当性
- [x] 15問サバイバル・ドリル＋3問クイズの構成
- **判定**: `APPROVED`

## 3. エンジニア（Engineer）検証
- [x] `python task/lint_markdown.py` エラー0件
- [x] `zensical.toml` の `nav` 登録確認
- [x] `zensical build` 検証
