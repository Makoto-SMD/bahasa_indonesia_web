# 執筆指示書: TASK-1281〜1290 【共起連語】時事専門領域コロケーション辞典（第4バッチ）

## 1. 基本情報
- **タスクID**: TASK-1281〜1290
- **担当役職**: 編集長（Director）発行 → 執筆担当（Writer）受領
- **対象セクション**: セクション31「【共起連語】最頻出コア語根＆コロケーション辞典」
- **対象記事数**: 10記事（1281〜1290）
- **ディレクトリ**: `docs/lexicon/`
- **累計目標**: 1,280 → 1,290 / 1,500 記事（進捗率 86.0%）

---

## 2. 記事一覧・スラッグ一覧
1. **1281**: 【政治時事連語：選挙】pemilihan umum, perolehan suara, hak pilih, kampanye akbar, kotak suara
   - ファイル名: `docs/lexicon/31-politics-collocations-election.md`
2. **1282**: 【政治時事連語：外交】hubungan bilateral, nota kesepahaman, kunjungan kenegaraan, duta besar
   - ファイル名: `docs/lexicon/32-politics-collocations-diplomacy.md`
3. **1283**: 【法律連語：法廷】mengajukan gugatan, vonis hakim, saksi kunci, bukti otentik, praduga tak bersalah
   - ファイル名: `docs/lexicon/33-legal-collocations-court.md`
4. **1284**: 【経済時事連語：マクロ】laju inflasi, pertumbuhan ekonomi, daya beli masyarakat, neraca perdagangan
   - ファイル名: `docs/lexicon/34-economics-collocations-inflation.md`
5. **1285**: 【環境時事連語：気候】pemanasan global, energi terbarukan, emisi karbon, deforestasi, efek rumah kaca
   - ファイル名: `docs/lexicon/35-environment-collocations-climate.md`
6. **1286**: 【IT技術連語：デジタル】keamanan siber, kecerdasan buatan, komputasi awan, basis data, serangan siber
   - ファイル名: `docs/lexicon/36-tech-collocations-digital.md`
7. **1287**: 【医療健康連語：診察】tekanan darah, resep dokter, rawat inap, efek samping, rekam medis
   - ファイル名: `docs/lexicon/37-health-collocations-medical.md`
8. **1288**: 【学術論文連語：研究】metodologi penelitian, kerangka berpikir, uji hipotesis, tinjauan pustaka
   - ファイル名: `docs/lexicon/38-academic-collocations-research.md`
9. **1289**: 【伝統文化連語：儀礼】upacara adat, warisan leluhur, nilai luhur, norma masyarakat, kearifan lokal
   - ファイル名: `docs/lexicon/39-culture-collocations-tradition.md`
10. **1290**: 【家庭生活連語：家事】membersihkan rumah, memasak makanan, mencuci pakaian, belanja bulanan
    - ファイル名: `docs/lexicon/40-daily-collocations-home.md`

---

## 3. 記事構成・品質基準
- **タイトル**: `# 【共起連語】{分野} の必須コロケーション辞典：{代表表現}`
- **導入部**: 各専門ドメインにおける共起（Collocation）の重要性と、新聞・論文・日常での自然な言い回し
- **最頻出コロケーション総覧テーブル**: コロケーション・直訳・実際の意味・文脈レジスター・典型例文の Markdown テーブル
- **重要コロケーション詳細解説＆例文カード**:
  - 各表現の成り立ち、語義展開、派生語形（例: mengajukan gugatan, menguji hipotesis）
  - `.id-example` クラスによる例文ブロック（インドネシア語、カタカナ発音、日本語訳、語法ポイント）
- **実践ダイアログボックス**: `.dialogue-box` による会話形式の活用例
- **誤用注意・ネイティブの語感解説**: 専門用語の正確な使い分け（例: pemilu vs pilkada, rawat inap vs rawat jalan）
- **定着確認クイズ（全3問）**:
  - 4択形式、正解の太字約物記法（`**正解**: 「**...**」`）
  - 丁寧な解説
- **文化・専門コラム**: 各ドメインの背景知識（選挙フェスティバル、公的医療保険BPJS、慣習法と現代法の共存等）
- **フッター**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 4. 厳格遵守ルール
1. ルビ構文（`{単語|読み}`）の完全禁止。
2. 日本語約物の外側に太字を配置（`「**強調内容**」`）。
3. Linter（`lint_markdown.py`）0エラー。
4. `zensical.toml` への nav 追加および `zensical build` でエラーゼロ。
