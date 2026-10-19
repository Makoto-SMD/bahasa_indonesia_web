# 執筆指示書: TASK-1361（セクション33 第2バッチ 1361〜1370）

## 基本情報
- **担当役職**: 編集長（Director）
- **対象セクション**: セクション33「【語彙拡張】語根別派生語マスター図鑑 第2弾」
- **対象記事ID**: 1361 〜 1370（計10記事）
- **記事ディレクトリ**: `docs/derivations-2/`
- **想定CEFRレベル**: A2 〜 B2（初中級〜中上級）
- **読了目安**: 各12分

---

## 記事一覧と対象語根

1. **1361**: 語根 tambah（増える・添加・補足）の全派生語図鑑 (`111-root-tambah.md`)
   - 派生語: menambah, bertambah, tambahan, penambahan, pertambahan, tertambah
2. **1362**: 語根 kurang（減る・不足・欠点・控えめ）の全派生語図鑑 (`112-root-kurang.md`)
   - 派生語: mengurangi, berkurang, kekurangan, pengurangan, sekurang-kurangnya
3. **1363**: 語根 bagi（分ける・分配・割り算・〜にとって）の全派生語図鑑 (`113-root-bagi.md`)
   - 派生語: membagi, berbagi, pembagian, sebagian, sebagian besar, bagaimanapun
4. **1364**: 語根 gabung（結合する・合併・一体化）の全派生語図鑑 (`114-root-gabung.md`)
   - 派生語: menggabungkan, bergabung, penggabungan, gabungan, tergabung
5. **1365**: 語根 kumpul（集まる・収集・蓄積・結集）の全派生語図鑑 (`115-root-kumpul.md`)
   - 派生語: mengumpulkan, berkumpul, perkumpulan, pengumpulan, kumpulan, terkumpul
6. **1366**: 語根 pisah（分かれる・隔離・分離・別離）の全派生語図鑑 (`116-root-pisah.md`)
   - 派生語: memisahkan, berpisah, pemisahan, perpisahan, terpisah, pemisah
7. **1367**: 語根 tarik（引く・引き出す・惹きつける・撤退）の全派生語図鑑 (`117-root-tarik.md`)
   - 派生語: menarik, ditarik, tertarik, ketertarikan, penarikan, tarikan
8. **1368**: 語根 dorong（押す・推進する・促す・動機）の全派生語図鑑 (`118-root-dorong.md`)
   - 派生語: mendorong, didorong, dorongan, pendorong, terdorong
9. **1369**: 語根 angkat（持ち上げる・引き上げる・任命・世代・軍隊）の全派生語図鑑 (`119-root-angkat.md`)
   - 派生語: mengangkat, diangkat, pengangkatan, angkatan, terangkat, berangkat
10. **1370**: 語根 turun（下りる・低下する・下落・子孫・伝統）の全派生語図鑑 (`120-root-turun.md`)
    - 派生語: menurunkan, diturunkan, penurunan, keturunan, menurun, turun-temurun

---

## 必須構成要素（語根派生語図鑑フォーマット）

全記事に以下の要素を完全網羅すること：
1. **メタヘッダー**: 記事タイトル、バッジ（語根派生語、語彙拡張、中級文法）、レベル、読了目安時間
2. **語根のコアミーニング解説**: 原義、語源的ニュアンス、接辞による意味展開の鳥瞰
3. **派生語マトリックス（Markdownテーブル）**: 派生語、接辞形態、品詞、日本語義、基本例文（5列を厳守）
4. **各主要派生語の詳細解説と例文カード**:
   - カタカナ発音表記（※独立した行のカタカナ発音欄）
   - 文法・ニュアンスの着眼点、典型コロケーション
5. **実践会話ダイアログ（`.dialogue-box`）**: 派生語が文脈の中で自然に使い分けられるリアルな対話
6. **接辞の使い分け・文法比較のポイント**: 学習者が混同しやすい派生語対比（例: bertambah vs menambah, berkurang vs mengurangi 等）
7. **定着確認クイズ3問**: 選択肢、正解・解説（`<details>` による折りたたみ）
8. **語源・文化コラム**: 語根にまつわる文化的背景やことわざ（Peribahasa）
9. **フッターリンク**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 執筆・検証インバリアント
- **ルビ構文（`{単語|読み}`）の完全禁止**。
- **太字約物記法（`「**強調**」`）の厳格遵守**。
- **Linter（`python .\task\lint_markdown.py`）エラー0件の維持**。
