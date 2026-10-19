# 校正・検証レポート: TASK-1291 (最頻出コア語根＆コロケーション辞典 第5バッチ: 構文・副詞・慣用連語＆総合検定 1291〜1300)

## 1. 担当・実施日
- 担当校正者: Reviewer & Engineer
- 実施日: 2026-10-19
- 対象指示書: `task/TASK-1291_collocations_batch5.md`

## 2. 検証対象記事
1. `docs/lexicon/41-adjective-collocations-sangat.md` (1291: 強調副詞と形容詞連語)
2. `docs/lexicon/42-adjective-collocations-mutlak.md` (1292: 絶対・確定共起表現)
3. `docs/lexicon/43-frequency-adverbs-collocations.md` (1293: 頻度副詞連語)
4. `docs/lexicon/44-prepositional-chunks-collocations.md` (1294: 前置詞定型チャンク)
5. `docs/lexicon/45-discourse-markers-connectors.md` (1295: 談話標識・論理マーカー)
6. `docs/lexicon/46-idiomatic-pairs-synonyms.md` (1296: 類語重複連語)
7. `docs/lexicon/47-antonymic-pairs-balance.md` (1297: 対義語対比連語)
8. `docs/lexicon/48-rhyming-collocations-sound.md` (1298: 音韻・韻律連語)
9. `docs/lexicon/49-contemporary-slang-collocations.md` (1299: 現代スラング頻出連語)
10. `docs/lexicon/50-comprehensive-collocation-mastery.md` (1300: 総合コロケーション検定50問テスト)

## 3. 校正・品質チェック項目
- [x] 正書法・綴り: KBBI準拠（sangat, amat sangat, syarat mutlak, sering kali, sehubungan dengan, oleh karena itu, hancur lebur, suka duka, seluk beluk, salfok / pansos 等、正確な綴りと語法を検証）。
- [x] ルビ構文の禁止: `{単語|読み}` は一切使用されていないことを確認。
- [x] 約物・太字記法: 鉤括弧の外側に太字を配置（「**強調**」）し、クイズ正解欄も Linter 準拠（`Bracket issues found: 0`）。
- [x] 総合検定の完全性: 第1300記事において、全5分野（動詞・身体・ビジネス・時事・構文）×10問＝計50問の完全テストおよび採点基準表・詳細解説が整っていることを確認。
- [x] フッターリンク: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)` で統一。

## 4. 判定
**APPROVED (承認)** - セクション31完結、技術検証（zensical.toml 登録・ビルド）へ移行。
