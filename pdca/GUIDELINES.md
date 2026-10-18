# 組織共通執筆・校正ガイドライン (Editorial Guidelines)

本ガイドラインは、日本人向けインドネシア語学習ナレッジベース（Zensical）を自律的かつ高品質に構築するための品質規約です。
Director、Writer、Reviewer、Engineer、BOSS の全員が本規約を遵守してください。

---

## 1. 記事執筆の基本原則

1. **学習者目線（日本人向け）の解説**:
   - 専門的な言語学用語（文法学術用語）を振り回さず、直感的かつ実用的な解説を心がける。
   - 英語や日本語との対比（例: 「英語の〜に相当」「日本語の助詞とは異なり〜」）を活用して理解を促進する。
2. **例文・用例の充実**:
   - すべての解説には、日常会話やビジネス、旅行でそのまま使える実践的な例文を最低2〜3個付与する。
   - 単語単体ではなく、フレーズや対話（`.dialogue-box`）形式を交える。
3. **視覚的コンポーネントの活用**:
   - インドネシア語例文カード (`.id-example`) を使用する。
   - 接辞の解説では、接頭辞・語根・接尾辞の色分け（`.affix-prefix`, `.affix-root`, `.affix-suffix`）を活用する。

---

## 2. 表記・マークダウン規約

### 2.1 ルビ（カタカナ読み・訳注）
- 発音や意味のルビには `{インドネシア語|カタカナや訳}` を使用する。
  ```markdown
  {Selamat|スラマッ} {pagi|パギ}!
  ```
- **Markdown表（テーブル）内での注意**:
  - 表の中ではパイプ `|` が列の区切りと干渉するため、必ず `\|` とエスケープする。
  ```markdown
  | インドネシア語 | 読み・訳 |
  | --- | --- |
  | {terima\|トゥリマ} {kasih\|カシ} | ありがとう |
  ```

### 2.2 例文カード記法
```markdown
<div class="id-example" markdown>

<div class="id-sentence">
{Saya|サヤ} {mau|マウ} {makan|マカン} {nasi|ナシ} {goreng|ゴレン}.
</div>
<div class="id-reading">
サヤ マウ マカン ナシ ゴレン
</div>
<div class="id-meaning">
私はナシゴレン（インドネシア風炒飯）が食べたいです。
</div>

</div>
```

### 2.3 対話（会話）ブロック記法
```markdown
<div class="dialogue-box" markdown>

<div class="dialogue-item">
  <span class="dialogue-speaker">A</span>
  <span>{Apa|アパ} {ini|イニ}?（これは何ですか？）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker dialogue-speaker--b">B</span>
  <span>{Ini|イニ} {kopi|コピ}.（これはコーヒーです。）</span>
</div>

</div>
```

---

## 3. ナビゲーションとビルド規約

1. **`zensical.toml` への登録**:
   - 新規記事を作成したら、必ず `zensical.toml` の `nav` の適切なセクションに登録する。
2. **ビルド検証**:
   - 記事作成・修正後は以下のコマンドを実行してエラーがないことを確認する。
   ```powershell
   .\.venv\Scripts\zensical.exe build
   powershell -ExecutionPolicy Bypass -File .\format.ps1
   ```
3. **ポート指定**:
   - ローカルサーバーはポート `8001`（`http://localhost:8001`）を使用する。
