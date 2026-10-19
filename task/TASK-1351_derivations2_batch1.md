# 執筆指示書: TASK-1351（セクション33 第1バッチ 1351〜1360）

## 基本情報
- **担当役職**: 編集長（Director）
- **対象セクション**: セクション33「【語彙拡張】語根別派生語マスター図鑑 第2弾」
- **対象記事ID**: 1351 〜 1360（計10記事）
- **記事ディレクトリ**: `docs/derivations-2/`
- **想定CEFRレベル**: A2 〜 B2（初中級〜中上級）
- **読了目安**: 各12分

---

## 記事一覧と対象語根

1. **1351**: 語根 atur（整理・配置・規則）の全派生語図鑑 (`101-root-atur.md`)
   - 派生語: mengatur, diatur, pengaturan, peraturan, teratur, keteraturan, pengatur
2. **1352**: 語根 hubung（繋ぐ・関係・通信）の全派生語図鑑 (`102-root-hubung.md`)
   - 派生語: menghubungkan, dihubungkan, berhubungan, hubungan, perhubungan, penghubung, terhubung
3. **1353**: 語根 susun（積み重ねる・並べる・編纂）の全派生語図鑑 (`103-root-susun.md`)
   - 派生語: menyusun, disusun, susunan, penyusun, penyusunan, bersusun, tersusun
4. **1354**: 語根 pecah（割れる・分裂・解決）の全派生語図鑑 (`104-root-pecah.md`)
   - 派生語: memecahkan, dipecahkan, perpecahan, pecahan, terpecah, pemecahan, berpecah
5. **1355**: 語根 ikat（縛る・結ぶ・連帯・契約）の全派生語図鑑 (`105-root-ikat.md`)
   - 派生語: mengikat, diikat, ikatan, perikatan, terikat, keterikatan, pengikat
6. **1356**: 語根 lepas（放す・脱ぐ・解放・免除）の全派生語図鑑 (`106-root-lepas.md`)
   - 派生語: melepaskan, dilepaskan, terlepas, pelepasan, berlepas, selepas
7. **1357**: 語根 pasang（設置する・取り付ける・対・満潮）の全派生語図鑑 (`107-root-pasang.md`)
   - 派生語: memasang, dipasang, pemasangan, pasangan, berpasangan, terpasang, pemasang
8. **1358**: 語根 ganti（替える・交替・補償）の全派生語図鑑 (`108-root-ganti.md`)
   - 派生語: mengganti, diganti, berganti, pergantian, pengganti, ganti rugi
9. **1359**: 語根 ubah（変える・改変・変更）の全派生語図鑑 (`109-root-ubah.md`)
   - 派生語: mengubah, diubah, berubah, perubahan, pengubahan, terubah, peubah
10. **1360**: 語根 pindah（移る・移住・転勤・感染）の全派生語図鑑 (`110-root-pindah.md`)
    - 派生語: memindahkan, dipindahkan, berpindah, perpindahan, pemindahan, kepindahan, terpidana

---

## 必須構成要素（語根派生語図鑑フォーマット）

全記事に以下の要素を完全網羅すること：
1. **メタヘッダー**: 記事タイトル、バッジ（語根派生語、語彙拡張、中級文法）、レベル、読了目安時間
2. **語根のコアミーニング解説**: 原義、語源的ニュアンス、接辞による意味展開の鳥瞰
3. **派生語マトリックス（Markdownテーブル）**: 派生語、接辞形態、品詞、日本語義、基本例文
4. **各主要派生語の詳細解説と例文カード**:
   - カタカナ発音表記（※ルビではなく別行のカタカナ発音欄）
   - 文法・ニュアンスの着眼点、典型コロケーション
5. **実践会話ダイアログ（`.dialogue-box`）**: 派生語が文脈の中で自然に使い分けられるリアルな対話
6. **接辞の使い分け・文法比較のポイント**: 学習者が混同しやすい派生語対比（例: per- -an と peN- -an の違いなど）
7. **定着確認クイズ3問**: 選択肢、正解・解説（`<details>` による折りたたみ）
8. **語源・文化コラム**: 語根にまつわる文化的背景やことわざ（Peribahasa）
9. **フッターリンク**: `[総合サイトマップ](../sitemap.md) | [トップページ](../index.md)`

---

## 執筆・検証インバリアント
- **ルビ構文（`{単語|読み}`）の完全禁止**。
- **太字約物記法（`「**強調**」`）の厳格遵守**。
- **Linter（`python .\task\lint_markdown.py`）エラー0件の維持**。
