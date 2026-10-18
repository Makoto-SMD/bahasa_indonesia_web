# 執筆指示書: TASK-1011_output_drills_part2

- **担当**: 編集長（Director）
- **対象記事**: 1011〜1020（瞬間口頭作文＆パターンプラクティス 第2バッチ 10本）
  - 1011: 等位接続詞（dan, atau, tetapi, melainkan）の論理接続 (`docs/output/11-conjunction-coordinating.md`)
  - 1012: 従属接続詞（karena, sehingga, agar, jika, walaupun）の複文組み立て (`docs/output/12-conjunction-subordinating.md`)
  - 1013: 助数詞（orang, ekor, buah, batang, lembar）と数量詞の即時産出 (`docs/output/13-classifiers-counting.md`)
  - 1014: 存在表現 ada の多機能構文（所有・存在・強調）の瞬間生成 (`docs/output/14-existential-ada.md`)
  - 1015: 依頼・指示・禁止（tolong, silakan, harap, jangan, dilarang） (`docs/output/15-imperatives-requests.md`)
  - 1016: 三人称 di- 受動態の瞬間組み立て（Diperiksa oleh dokter） (`docs/output/16-passive-prefix-di.md`)
  - 1017: 一人称語幹受動態（Buku ini sudah saya baca）の自動発話化 (`docs/output/17-passive-stem-first-person.md`)
  - 1018: 二人称語幹受動態（Tugas ini harus kamu selesaikan）の反射出力 (`docs/output/18-passive-stem-second-person.md`)
  - 1019: 接頭辞 meN- 他動詞の鼻音化と即時発話（membeli, menulis, melihat） (`docs/output/19-prefix-men-transitive.md`)
  - 1020: 接頭辞 meN- 自動詞と状態変化（menangis, mendarat, menguning） (`docs/output/20-prefix-men-intransitive.md`)

## 執筆要件
1. **SLA即時自動化の徹底**:
   - 日本語刺激から1〜2秒以内の産出ドリル各15問。
   - 語幹受動態（Buku ini saya baca）、tetapi vs melainkan、meN-鼻音化の即座判断など、日本人のボトルネックを集中強化。
2. **デザインコンポーネント**:
   - `.id-example`（`.id-sentence`, `.id-reading`, `.id-meaning`）
   - 各記事に理解度チェッククイズ3問。
3. **インバリアント**:
   - ルビ構文（`{単語|読み}`）の完全排除、太字約物ルール（`「**強調**」`）の遵守。
