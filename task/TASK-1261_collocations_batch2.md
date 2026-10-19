# 執筆指示書: TASK-1261〜1270 【共起連語】最頻出動詞・身体名詞語根コロケーション辞典（第2バッチ）

## 1. 基本情報
- **タスクID**: TASK-1261〜1270
- **担当役職**: 編集長（Director）発行 → 執筆担当（Writer）受領
- **対象セクション**: セクション31「【共起連語】最頻出コア語根＆コロケーション辞典」
- **対象記事数**: 10記事（1261〜1270）
- **ディレクトリ**: `docs/lexicon/`
- **累計目標**: 1,260 → 1,270 / 1,500 記事（進捗率 84.7%）

---

## 2. 記事一覧・スラッグ一覧
1. **1261**: 語根 `turun` の必須コロケーション（turun tangan, turun harga, turun minum, turun ranjang, turun pamor）
   - ファイル名: `docs/lexicon/11-verb-collocations-turun.md`
2. **1262**: 語根 `tahan` の必須コロケーション（tahan banting, tahan lama, tahan uji, tahan lapar, tahan godaan）
   - ファイル名: `docs/lexicon/12-verb-collocations-tahan.md`
3. **1263**: 語根 `pecah` の必須コロケーション（pecah belah, pecah rekor, pecah tangis, pecah kongsi, pecah ketuban）
   - ファイル名: `docs/lexicon/13-verb-collocations-pecah.md`
4. **1264**: 語根 `putar` の必須コロケーション（putar balik, putar otak, putar lidah, putar haluan, putar haluan politik）
   - ファイル名: `docs/lexicon/14-verb-collocations-putar.md`
5. **1265**: 語根 `jalan` の必須コロケーション（jalan keluar, jalan pintas, jalan buntu, jalan tengah, jalan tol）
   - ファイル名: `docs/lexicon/15-verb-collocations-jalan.md`
6. **1266**: 身体名詞 `hati` の連語（rendah hati, besar hati, patah hati, keras hati, hati kecil, jatuh hati）
   - ファイル名: `docs/lexicon/16-noun-collocations-hati.md`
7. **1267**: 身体名詞 `kepala` の連語（kepala dingin, keras kepala, besar kepala, cuci kepala, pusing kepala）
   - ファイル名: `docs/lexicon/17-noun-collocations-kepala.md`
8. **1268**: 身体名詞 `mata` の連語（mata rantai, mata air, mata angin, mata pencaharian, mata-mata）
   - ファイル名: `docs/lexicon/18-noun-collocations-mata.md`
9. **1269**: 身体名詞 `tangan` の連語（tangan kanan, cuci tangan, campur tangan, angkat tangan, buah tangan）
   - ファイル名: `docs/lexicon/19-noun-collocations-tangan.md`
10. **1270**: 身体名詞 `kaki` の連語（kaki lima, kaki tangan, angkat kaki, cuci kaki, mata kaki）
    - ファイル名: `docs/lexicon/20-noun-collocations-kaki.md`

---

## 3. 記事構成・品質基準
- **タイトル**: `# 【共起連語】語根 {語根} の必須コロケーション辞典：{代表表現}`
- **導入部**: コア語根の基本的概念（下降・耐久・分裂・回転・進行、および身体部位メタファー）と、インドネシア語における共起（Collocation）の重要性
- **最頻出コロケーション総覧テーブル**: コロケーション・直訳・実際の意味・文脈レジスター（日常/ビジネス/報道）・典型例文の Markdown テーブル
- **重要コロケーション詳細解説＆例文カード**:
  - 各表現の成り立ち、語義の展開プロセス、接辞付加時の語形（例: turun tangan, campur tangan, mencampurtangani）
  - `.id-example` クラスによる例文ブロック（インドネシア語、カタカナ発音、日本語訳、語法ポイント）
- **実践ダイアログボックス**: `.dialogue-box` による会話形式の活用例
- **誤用注意・ネイティブの語感解説**: 直訳すると不自然になる表現、日本人学習者が混同しやすいポイント
- **定着確認クイズ（全3問）**:
  - 4択形式、正解の太字約物記法（`**正解**: 「**...**」`）
  - 丁寧な解説
- **文化コラム・語源解説**: 身体性（body metaphors）に息づくインドネシア人の人間観や社会哲学
- **フッター**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 4. 厳格遵守ルール
1. ルビ構文（`{単語|読み}`）の完全禁止。
2. 日本語約物の外側に太字を配置（`「**強調内容**」`）。
3. Linter（`lint_markdown.py`）0エラー。
4. `zensical.toml` への nav 追加および `zensical build` でエラーゼロ。
