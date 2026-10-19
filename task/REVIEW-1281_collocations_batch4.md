# 校正・検証レポート: TASK-1281 (最頻出コア語根＆コロケーション辞典 第4バッチ: 時事・専門領域連語 1281〜1290)

## 1. 担当・実施日
- 担当校正者: Reviewer & Engineer
- 実施日: 2026-10-19
- 対象指示書: `task/TASK-1281_collocations_batch4.md`

## 2. 検証対象記事
1. `docs/lexicon/31-politics-collocations-election.md` (1281: 選挙・政治時事連語)
2. `docs/lexicon/32-politics-collocations-diplomacy.md` (1282: 外交・国際関係連語)
3. `docs/lexicon/33-legal-collocations-court.md` (1283: 司法・法廷連語)
4. `docs/lexicon/34-economics-collocations-inflation.md` (1284: マクロ経済・インフレ連語)
5. `docs/lexicon/35-environment-collocations-climate.md` (1285: 気候変動・環境連語)
6. `docs/lexicon/36-tech-collocations-digital.md` (1286: IT・デジタル先端連語)
7. `docs/lexicon/37-health-collocations-medical.md` (1287: 医療・健康診査連語)
8. `docs/lexicon/38-academic-collocations-research.md` (1288: 学術論文・研究論理連語)
9. `docs/lexicon/39-culture-collocations-tradition.md` (1289: 伝統儀礼・社会規範連語)
10. `docs/lexicon/40-daily-collocations-home.md` (1290: 家庭生活・家事生活連語)

## 3. 校正・品質チェック項目
- [x] 正書法・綴り: KBBI準拠（pemilihan umum, perolehan suara, nota kesepahaman, vonis hakim, laju inflasi, emisi karbon, kecerdasan buatan, resep dokter, kerangka berpikir, warisan leluhur 等、正しい表記）
- [x] ルビ構文の禁止: `{単語|読み}` は一切使用されていないことを確認。
- [x] 約物・太字記法: 鉤括弧の外側に太字を配置（「**強調**」）し、クイズ正解欄も Linter 準拠（`Bracket issues found: 0`）。
- [x] 構成完全性: 表・解説・例文・共起パターン・3択クイズ・専門文化コラムが完備。
- [x] フッターリンク: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)` で統一。

## 4. 判定
**APPROVED (承認)** - 技術検証（zensical.toml 登録・ビルド）へ移行。
