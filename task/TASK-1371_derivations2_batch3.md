# 執筆指示書 (Task Specification)

## タスク情報
- **タスクID**: TASK-1371_derivations2_batch3
- **対象セクション**: セクション33「【語彙拡張】語根別派生語マスター図鑑 第2弾」（1371〜1380 / 全50記事中 第3バッチ）
- **対象記事（10本）**:
  1. `docs/derivations-2/121-root-naik.md` (1371. 語根 naik の全派生語図鑑：menaikkan, kenaikan, menaiki, menaik)
  2. `docs/derivations-2/122-root-jatuh.md` (1372. 語根 jatuh の全派生語図鑑：menjatuhkan, kejatuhan, penjatuhan, terjatuh)
  3. `docs/derivations-2/123-root-bangkit.md` (1373. 語根 bangkit の全派生語図鑑：membangkitkan, kebangkitan, pembangkit, berbangkit)
  4. `docs/derivations-2/124-root-runtuh.md` (1374. 語根 runtuh の全派生語図鑑：meruntuhkan, keruntuhan, reruntuhan, runtuhan)
  5. `docs/derivations-2/125-root-roboh.md` (1375. 語根 roboh の全派生語図鑑：merobohkan, kerobohan, perobohan, teroboh)
  6. `docs/derivations-2/126-root-tumbuh.md` (1376. 語根 tumbuh の全派生語図鑑：menumbuhkan, pertumbuhan, tumbuhan, bertumbuh)
  7. `docs/derivations-2/127-root-kembang.md` (1377. 語根 kembang の全派生語図鑑：mengembangkan, perkembangan, pengembangan, berkembang)
  8. `docs/derivations-2/128-root-maju.md` (1378. 語根 maju の全派生語図鑑：memajukan, kemajuan, pemajuan, termaju)
  9. `docs/derivations-2/129-root-mundur.md` (1379. 語根 mundur の全派生語図鑑：memundurkan, kemunduran, pemunduran, bermundur)
  10. `docs/derivations-2/130-root-hindar.md` (1380. 語根 hindar の全派生語図鑑：menghindari, terhindar, penghindaran, menghindarkan)

---

## 執筆方針・構成レギュレーション

各記事は以下の黄金構成を厳格に保持すること：
1. **メタデータ・ヘッダー**: タイトル、カテゴリバッジ、読了目安時間（12分）、レベル（初中級〜上級 A2〜B2）
2. **語根のコア概念と派生展開**: 語根の根源的意味、物理的意味から心理・社会・比喩的意味への展開
3. **派生語一覧マトリックス（5列テーブル）**: 派生語、接辞パターン、品詞、日本語義、基本例文
4. **主要派生語の精密解説と例文カード（最低4語）**:
   - カタカナ発音、語法ニュアンス、重要コロケーション、インドネシア語例文、自然な日本語訳
5. **実践会話ダイアログ（`.dialogue-box` クラス）**: 2名のリアルなビジネス・日常会話
6. **接辞の使い分け・文法比較のポイント**:
   - naik vs menaikkan vs menaiki、tumbuh vs berkembang、maju vs memajukan 等の決定的相違点
7. **定着確認クイズ（3問）**: 選択肢、アコーディオン式解答（`details/summary`）、詳細な解説
8. **語源・文化コラム（Peribahasa・社会的背景）**: ことわざや成句
9. **フッターナビゲーション**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

### チェックインバリアント
- ❌ ルビ構文（`{単語|読み}`）の完全禁止
- 太字約物記法（`「**強調内容**」`）の厳格遵守
- マトリックスのタプルは厳密に5要素 `(word, aff, pos, meaning, ex)`
- 詳細カードのタプルは厳密に7要素 `(word, pos, kana, desc, coloc, id_ex, ja_ex)`
