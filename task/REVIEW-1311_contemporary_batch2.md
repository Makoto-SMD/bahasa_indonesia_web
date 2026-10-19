# 校正・検証レポート: TASK-1311 (インドネシア現代社会・トレンド深層読解 第2バッチ: 環境・エネルギー・都市・文化 1311〜1320)

## 1. 担当・実施日
- 担当校正者: Reviewer & Engineer
- 実施日: 2026-10-19
- 対象指示書: `task/TASK-1311_contemporary_batch2.md`

## 2. 検証対象記事
1. `docs/contemporary/11-new-capital-nusantara-progress.md` (1311: IKNヌサンタラ建設と投資)
2. `docs/contemporary/12-green-energy-geothermal-power.md` (1312: 地熱エネルギーとベースロード電源)
3. `docs/contemporary/13-palm-oil-b35-biodiesel.md` (1313: B35バイオディーゼルとEUDR環境紛争)
4. `docs/contemporary/14-food-waste-zero-hunger.md` (1314: 食品ロスと余剰食料レスキュー運動)
5. `docs/contemporary/15-mental-health-awareness-urban.md` (1315: 「Healing」ブームと若者の心の健康)
6. `docs/contemporary/16-indonesian-cinema-golden-age.md` (1316: 映画の黄金期：ホラーと芸術映画)
7. `docs/contemporary/17-modern-indie-music-scene.md` (1317: インディーズ音楽の台頭と文学的歌詞)
8. `docs/contemporary/18-gig-economy-workers-rights.md` (1318: ギグワーカーと配車ドライバーの労働権)
9. `docs/contemporary/19-crypto-asset-investment-boom.md` (1319: 若者の暗号資産ブームと金融規制)
10. `docs/contemporary/20-sustainable-tourism-labuan-bajo.md` (1320: コモド島ラブアン・バジョと住民共生)

## 3. 校正・品質チェック項目
- [x] 正書法・綴り: KBBI準拠（Indonesia-sentris, nirawak, panas bumi, beban dasar listrik, mandatori, proteksionisme hijau, sampah makanan, tengkes, mubazir, pemasungan, masa keemasan, menorehkan sejarah, keresahan eksistensial, pekerja manggung, aset kripto, destinasi super prioritas 等、正確な術語と洗練された文体）。
- [x] ルビ構文の禁止: `{単語|読み}` は一切使用されていないことを確認。
- [x] 約物・太字記法: 鉤括弧の外側に太字を配置（「**強調**」）し、クイズ正解欄も Linter 準拠（`Bracket issues found: 0`）。
- [x] 長文読解の構成完全性: 本文長文（各400〜550語）、重要語彙表、段落ごとの対訳日本語全訳、文法・論理構造解説、読解クイズ3問、深掘り背景コラムが全10記事で完璧に完備。
- [x] フッターリンク: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)` で統一。

## 4. 判定
**APPROVED (承認)** - 技術検証（zensical.toml 登録・ビルド）へ移行。
