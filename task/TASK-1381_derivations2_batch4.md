# 執筆指示書 (Task Specification)

## タスク情報
- **タスクID**: TASK-1381_derivations2_batch4
- **対象セクション**: セクション33「【語彙拡張】語根別派生語マスター図鑑 第2弾」（1381〜1390 / 全50記事中 第4バッチ）
- **対象記事（10本）**:
  1. `docs/derivations-2/131-root-cegah.md` (1381. 語根 cegah の全派生語図鑑：mencegah, pencegahan, tercegah, pencegah)
  2. `docs/derivations-2/132-root-lindung.md` (1382. 語根 lindung の全派生語図鑑：melindungi, perlindungan, pelindung, terlindung)
  3. `docs/derivations-2/133-root-bela.md` (1383. 語根 bela の全派生語図鑑：membela, pembelaan, pembela, terbela)
  4. `docs/derivations-2/134-root-tuntut.md` (1384. 語根 tuntut の全派生語図鑑：menuntut, tuntutan, penuntutan, penuntut)
  5. `docs/derivations-2/135-root-gugat.md` (1385. 語根 gugat の全派生語図鑑：menggugat, gugatan, penggugat, tergugat)
  6. `docs/derivations-2/136-root-tolak.md` (1386. 語根 tolak の全派生語図鑑：menolak, penolakan, tertolak, tolak ukur)
  7. `docs/derivations-2/137-root-terima.md` (1387. 語根 terima の全派生語図鑑：menerima, penerimaan, keterbukaan, terima kasih)
  8. `docs/derivations-2/138-root-tolong.md` (1388. 語根 tolong の全派生語図鑑：menolong, pertolongan, penolong, tertolong)
  9. `docs/derivations-2/139-root-bantu.md` (1389. 語根 bantu の全派生語図鑑：membantu, bantuan, pembantu, terbantu)
  10. `docs/derivations-2/140-root-layan.md` (1390. 語根 layan の全派生語図鑑：melayani, pelayanan, pelayan, terlayani)

---

## 執筆方針・構成レギュレーション

各記事は以下の黄金構成を厳格に保持すること：
1. **メタデータ・ヘッダー**: タイトル、カテゴリバッジ、読了目安時間（12分）、レベル（初中級〜上級 A2〜B2）
2. **語根のコア概念と派生展開**: 語根の根源的意味、物理的意味から心理・社会・比喩的意味への展開
3. **派生語一覧マトリックス（5列テーブル）**: 派生語、接辞パターン、品詞、日本語義、基本例文
4. **主要派生語の精密解説と例文カード（最低4語）**:
   - カタカナ発音、語法ニュアンス、重要コロケーション、インドネシア語例文、自然な日本語訳
5. **実践会話ダイアログ（`.dialogue-box` クラス）**: 2名のリアルなビジネス・日常・法務会話
6. **接辞の使い分け・文法比較のポイント**:
   - cegah vs lindung、tuntut vs gugat、tolak vs terima、tolong vs bantu、melayani vs pelayanan 等の決定的相違点
7. **定着確認クイズ（3問）**: 選択肢、アコーディオン式解答（`details/summary`）、詳細な解説
8. **語源・文化コラム（Peribahasa・社会的背景）**: ことわざや成句
9. **フッターナビゲーション**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

### チェックインバリアント
- ❌ ルビ構文（`{単語|読み}`）の完全禁止
- 太字約物記法（`「**強調内容**」`）の厳格遵守
- マトリックスのタプルは厳密に5要素 `(word, aff, pos, meaning, ex)`
- 詳細カードのタプルは厳密に7要素 `(word, pos, kana, desc, coloc, id_ex, ja_ex)`
