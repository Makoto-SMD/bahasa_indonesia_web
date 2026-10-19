# 執筆指示書: TASK-1251〜1260 【共起連語】最頻出コア動詞語根コロケーション辞典（第1バッチ）

## 1. 基本情報
- **タスクID**: TASK-1251〜1260
- **担当役職**: 編集長（Director）発行 → 執筆担当（Writer）受領
- **対象セクション**: セクション31「【共起連語】最頻出コア語根＆コロケーション辞典」
- **対象記事数**: 10記事（1251〜1260）
- **ディレクトリ**: `docs/lexicon/`
- **累計目標**: 1,250 → 1,260 / 1,500 記事（進捗率 84.0%）

---

## 2. 記事一覧・スラッグ一覧
1. **1251**: 語根 `ambil` の必須コロケーション（ambil bagian, ambil alih, ambil keputusan, ambil hati, ambil pusing）
   - ファイル名: `docs/lexicon/01-verb-collocations-ambil.md`
2. **1252**: 語根 `buat` の必須コロケーション（buat janji, buat keputusan, buat gara-gara, buat onar, buat salah）
   - ファイル名: `docs/lexicon/02-verb-collocations-buat.md`
3. **1253**: 語根 `buka` の必須コロケーション（buka usaha, buka suara, buka puasa, buka jalan, buka pintu）
   - ファイル名: `docs/lexicon/03-verb-collocations-buka.md`
4. **1254**: 語根 `tutup` の必須コロケーション（tutup mata, tutup mulut, tutup usia, tutup buku, tutup telinga）
   - ファイル名: `docs/lexicon/04-verb-collocations-tutup.md`
5. **1255**: 語根 `tarik` の必須コロケーション（tarik perhatian, tarik kesimpulan, tarik napas, tarik diri, tarik ulur）
   - ファイル名: `docs/lexicon/05-verb-collocations-tarik.md`
6. **1256**: 語根 `pasang` の必須コロケーション（pasang mata, pasang telinga, pasang aksi, pasang badan, pasang surut）
   - ファイル名: `docs/lexicon/06-verb-collocations-pasang.md`
7. **1257**: 語根 `buang` の必須コロケーション（buang waktu, buang muka, buang air, buang sial, buang hajat）
   - ファイル名: `docs/lexicon/07-verb-collocations-buang.md`
8. **1258**: 語根 `lepas` の必須コロケーション（lepas tangan, lepas tanggung jawab, lepas pandang, lepas kendali, lepas landas）
   - ファイル名: `docs/lexicon/08-verb-collocations-lepas.md`
9. **1259**: 語根 `jatuh` の必須コロケーション（jatuh tempo, jatuh sakit, jatuh cinta, jatuh miskin, jatuh bangun）
   - ファイル名: `docs/lexicon/09-verb-collocations-jatuh.md`
10. **1260**: 語根 `naik` の必須コロケーション（naik daun, naik pangkat, naik darah, naik banding, naik pitam）
    - ファイル名: `docs/lexicon/10-verb-collocations-naik.md`

---

## 3. 記事構成・品質基準
- **タイトル**: `# 【共起連語】語根 {語根} の必須コロケーション辞典：{代表表現}`
- **導入部**: コア語根の基本的概念（多義的展開のメタファー）と、インドネシア語における共起（Collocation）の重要性
- **最頻出コロケーション総覧テーブル**: コロケーション・直訳・実際の意味・使用レジスター（日常/ビジネス/報道）・典型例文の Markdown テーブル
- **重要コロケーション詳細解説＆例文カード**:
  - 各表現の成り立ち、語義の展開プロセス、接辞付加時の語形（例: mengambil alih, pengambilalihan）
  - `.id-example` クラスによる例文ブロック（インドネシア語、カタカナ発音、日本語訳、語法ポイント）
- **実践ダイアログボックス**: `.dialogue-box` による会話形式の活用例
- **誤用注意・ネイティブの語感解説**: 直訳すると不自然になる表現、日本人学習者が混同しやすいポイント
- **定着確認クイズ（全3問）**:
  - 4択形式、正解の太字約物記法（`**正解**: 「**...**」`）
  - 丁寧な解説
- **文化コラム・語源解説**: 慣用表現に息づくインドネシア人の生活感覚や価値観
- **フッター**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 4. 厳格遵守ルール
1. ルビ構文（`{単語|読み}`）の完全禁止。
2. 日本語約物の外側に太字を配置（`「**強調内容**」`）。
3. Linter（`lint_markdown.py`）0エラー。
4. `zensical.toml` への nav 追加および `zensical build` でエラーゼロ。
