# 執筆指示書: TASK-1271〜1280 【共起連語】身体名詞＆実践ビジネスコロケーション辞典（第3バッチ）

## 1. 基本情報
- **タスクID**: TASK-1271〜1280
- **担当役職**: 編集長（Director）発行 → 執筆担当（Writer）受領
- **対象セクション**: セクション31「【共起連語】最頻出コア語根＆コロケーション辞典」
- **対象記事数**: 10記事（1271〜1280）
- **ディレクトリ**: `docs/lexicon/`
- **累計目標**: 1,270 → 1,280 / 1,500 記事（進捗率 85.3%）

---

## 2. 記事一覧・スラッグ一覧
1. **1271**: 身体名詞 `mulut` の連語（mulut manis, tutup mulut, banyak mulut, buah mulut, mulut besar）
   - ファイル名: `docs/lexicon/21-noun-collocations-mulut.md`
2. **1272**: 身体名詞 `telinga` の連語（tebal telinga, merah telinga, pasang telinga, masuk telinga kanan keluar telinga kiri）
   - ファイル名: `docs/lexicon/22-noun-collocations-telinga.md`
3. **1273**: 身体名詞 `hidung` の連語（hidung belang, batang hidung, mencium bau busuk, menarik hidung）
   - ファイル名: `docs/lexicon/23-noun-collocations-hidung.md`
4. **1274**: 身体名詞 `muka` の連語（muka masam, cari muka, tebal muka, uang muka, buang muka）
   - ファイル名: `docs/lexicon/24-noun-collocations-muka.md`
5. **1275**: 身体名詞 `darah` の連語（darah daging, darah dingin, darah biru, naik darah, darah muda）
   - ファイル名: `docs/lexicon/25-noun-collocations-darah.md`
6. **1276**: 【ビジネス連語：契約】menandatangani kontrak, membatalkan klausul, wanprestasi, masa berlaku
   - ファイル名: `docs/lexicon/26-business-collocations-contract.md`
7. **1277**: 【ビジネス連語：商談】mencapai kesepakatan, mengajukan penawaran, menekan biaya, daya saing
   - ファイル名: `docs/lexicon/27-business-collocations-negotiation.md`
8. **1278**: 【ビジネス連語：財務】laporan laba rugi, arus kas, suntikan modal, suku bunga, dividen
   - ファイル名: `docs/lexicon/28-business-collocations-finance.md`
9. **1279**: 【ビジネス連語：人事】perekrutan karyawan, pemutusan hubungan kerja (PHK), evaluasi kinerja, jenjang karier
   - ファイル名: `docs/lexicon/29-business-collocations-hr.md`
10. **1280**: 【ビジネス連語：販促】pangsa pasar, target konsumen, kampanye promosi, citra merek, retensi pelanggan
    - ファイル名: `docs/lexicon/30-business-collocations-marketing.md`

---

## 3. 記事構成・品質基準
- **タイトル**: `# 【共起連語】{テーマ} の必須コロケーション辞典：{代表表現}`
- **導入部**: 語根・身体概念およびビジネス機能の基本的概念と、自然な共起（Collocation）の重要性
- **最頻出コロケーション総覧テーブル**: コロケーション・直訳・実際の意味・文脈レジスター（日常/ビジネス/法務）・典型例文の Markdown テーブル
- **重要コロケーション詳細解説＆例文カード**:
  - 各表現の成り立ち、語義展開、派生語形（例: mencairkan dana, memutus hubungan kerja）
  - `.id-example` クラスによる例文ブロック（インドネシア語、カタカナ発音、日本語訳、語法ポイント）
- **実践ダイアログボックス**: `.dialogue-box` による会話形式の活用例
- **誤用注意・ネイティブの語感解説**: 直訳すると不自然になる表現、ビジネス交渉でのタブーや言い換え
- **定着確認クイズ（全3問）**:
  - 4択形式、正解の太字約物記法（`**正解**: 「**...**」`）
  - 丁寧な解説
- **文化・ビジネスコラム**: インドネシアの商習慣・人間関係に息づく文化人類学的知見
- **フッター**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 4. 厳格遵守ルール
1. ルビ構文（`{単語|読み}`）の完全禁止。
2. 日本語約物の外側に太字を配置（`「**強調内容**」`）。
3. Linter（`lint_markdown.py`）0エラー。
4. `zensical.toml` への nav 追加および `zensical build` でエラーゼロ。
