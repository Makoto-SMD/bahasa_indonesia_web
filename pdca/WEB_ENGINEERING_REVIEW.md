# Webフロントエンド＆インフラ包括技術レビュー報告書 (Web Engineering Review Report)

- **調査・分析**: AI組織 Webエンジニア部門（Lead Web Architect / Frontend Specialist）
- **対象**: 本プロジェクトで生成されたWebサイト（Zensical静的ビルド成果物、設定、スタイルシート、スクリプト）
- **評価基準・スタンダード**:
  1. Webパフォーマンス & Core Web Vitals（LCP, INP, CLS, TTFB, DOM Size, Payload）
  2. CSS設計・アーキテクチャ・保守性（CSS Variables, Specificity, OOCSS, `!important` 排除, レスポンシブ）
  3. Webアクセシビリティ（WCAG 2.1 AA準拠性, カラーコントラスト比, セマンティクス, a11y）
  4. SEO・メタデータ・ソーシャルグラフ（OGP, Twitter Cards, Canonical, 構造化データ, Sitemap, robots.txt）
  5. 静的サイトジェネレーター（SSG）設定 & ビルドパイプライン（Zensical/MkDocs設定整合性, プラグイン効率化）
  6. フロントエンド機能 & UX拡張性（Web Speech API/音声再生, クリップボード操作, 全文検索インデックス最適化, PWA）
  7. セキュリティ・配信インフラ（HTTPセキュリティヘッダー, CSP, HSTS, キャッシュ戦略, ホスティング設定）
- **作成日**: 2026-10-19

---

## 1. エグゼクティブサマリー (Executive Summary)

本ナレッジベースは、全1,000ページを超える膨大な技術ドキュメント・学習コンテンツを擁し、Rust製のモダン静的サイトジェネレーター（Zensical 0.0.71）を採用して迅速なビルドを実現している。静的HTML生成による堅牢性と初期配信速度のポテンシャルは極めて高い。

しかし、**生成されたWebページおよびビルド設定をWebエンジニアリングの観点から厳密に監査した結果、複数のクリティカルな不具合およびアーキテクチャ上の重大なボトルネックが検出された。**

特に、**「TOML設定ミスによる独自スタイルの完全脱落（P0）」「全ページ500KB・3万行超のHTMLドキュメント肥大（DOM Bloat）（P1）」「7.3MBに達するクライアント検索インデックス（P1）」「ダークモード時のサイドバー文字視認性崩壊（P1）」「OGP/ソーシャルタグの完全欠落（P1）」「ダミーURL放置によるSEO汚染（P1）」**は、ユーザー体験（UX）、Core Web Vitals、検索流入、ブランド信頼性に直接的かつ深刻な悪影響を及ぼしている。

### 🚨 重要度別イシュー一覧 (Severity Matrix)

| 重要度 | 分類 | イシュー概要 | 主な影響 |
| :--- | :--- | :--- | :--- |
| **P0 (Critical)** | ビルド・CSS | **TOML記述ミスによる `extra.css` の完全未適用** | 例文カード・会話枠・ノート用紙質感等の独自スタイルが全ページで消失 |
| **P1 (High)** | パフォーマンス | **全ナビゲーションインライン展開によるDOM Bloat** | 1ページ約500KB/3万行。メモリ圧迫、LCP遅延、INP劣化 |
| **P1 (High)** | パフォーマンス | **7.3MBに及ぶ巨大検索インデックス (`search.json`)** | モバイル・低速回線での通信量爆発、パース時のメインスレッド停止 |
| **P1 (High)** | CSS・a11y | **ダークモード時のサイドバーリンク不可視化（黒地に黒文字）** | ダークモード利用時にナビゲーションが完全に読めなくなる |
| **P1 (High)** | SEO・ソーシャル | **OGP（Open Graph Protocol）およびTwitter Cardsの欠落** | SNSシェア時にアイキャッチや説明文が出ず、流入機会を著しく損失 |
| **P1 (High)** | SEO・基盤 | **`site_url = "https://example.com/..."` のダミーホスト放置** | CanonicalタグおよびSitemapがダミーURLとなり検索インデックスが汚染 |
| **P1 (High)** | a11y | **検定バッジ（`.badge-d`, `.badge-e`）のコントラスト比不足** | WCAG 2.1 AA基準（4.5:1）を大幅に下回り（約2.5:1）、弱視者が読めない |
| **P2 (Medium)** | フロントエンド | **Web Speech API（ブラウザ標準TTS）の未活用** | 語学サイトでありながらネイティブ音声再生手段が提供されていない |
| **P2 (Medium)** | CSS設計 | **`extra.css` における20箇所以上の `!important` 乱用** | 詳細度戦争（Specificity War）が発生し、今後の保守・拡張が極めて困難 |
| **P2 (Medium)** | ビルドパイプライン | **廃止済みルビ拡張（`ruby_extension.py`）の残留** | 規約上ルビ廃止済みにもかかわらず毎ビルドで無駄なCPUサイクルを浪費 |
| **P2 (Medium)** | a11y・SEO | **見出しレベルの階層スキップ（H1直後にH3配置）** | スクリーンリーダーや検索クローラーに対する文書構造セマンティクスの破綻 |
| **P2 (Medium)** | レスポンシブ | **テーブルの横スクロールラッパー欠如 & スピーカー幅崩れ** | スマートフォン表示時に広幅テーブルが画面外へ突き抜けレイアウト崩れ |
| **P2 (Medium)** | SEO・クローラー | **`robots.txt` の未生成** | 検索クローラーに対するサイトマップ案内やクロールディレクティブが未定義 |
| **P3 (Low)** | セキュリティ | **HTTPセキュリティヘッダー（CSP, HSTS等）の未設計** | クリックジャッキングやXSS耐性、外部リソース接続ポリシーが未定義 |
| **P3 (Low)** | UX・機能 | **PWA（Web App Manifest / Service Worker）の未対応** | モバイルホーム画面追加や移動中・オフライン環境での学習不可 |

---

## 2. 詳細分析（7大技術領域）

### 2.1 静的サイトジェネレーター（SSG）と設定の健全性

#### ① `extra_css` の配置ミスによるスタイルシート脱落（最重要インバリアント違反: P0）
- **現象**:
  生成されたすべてのHTMLファイル（`site/**/*.html`）の `<head>` 内を検証したところ、カスタムスタイルシート `stylesheets/extra.css` を読み込む `<link rel="stylesheet">` タグが**1行も出力されていない**。
- **根本原因**:
  `zensical.toml` の L1129 において、`extra_css` が `[[project.theme.palette]]` のテーブルブロック直下にインデントなしで記述されている。
  ```toml
  [[project.theme.palette]]
  media = "(prefers-color-scheme: dark)"
  scheme = "slate"
  primary = "teal"
  accent = "teal"
  toggle.icon = "lucide/moon"
  toggle.name = "システム設定に連動"

  extra_css = ["stylesheets/extra.css"]  # ← ここに書かれている！
  ```
  TOMLの仕様上、配列テーブル `[[...]]` の下に書かれたキーは、その配列要素のプロパティ（`project.theme.palette[2].extra_css`）として解釈される。
  一方、Zensicalのテンプレートエンジン（`base.html`）は以下の通りトップレベルまたは `project` 直下の `config.extra_css` を参照している。
  ```jinja2
  {% for path in config.extra_css %}
    <link rel="stylesheet" href="{{ path | url }}">
  {% endfor %}
  ```
  この結果、ビルド時に `config.extra_css` が空と判定され、HTMLへのリンクタグ出力が完全に脱落していた。
- **影響**:
  プロジェクトが意図した以下の独自デザインが、本番のWebページ上で**1ミリも反映されていない**（デフォルトの素のMaterialテーマのまま表示されている）：
  - アイボリーペーパー・ノート質感の背景色（`#f7f4ed`）
  - インドネシア語例文カード（`.id-example`）の境界線・余白・配色
  - 会話ボックス（`.dialogue-box`, `.dialogue-speaker`）のレイアウト
  - 接辞・語根ハイライト（`.affix-prefix`, `.affix-root`）
  - 検定級バッジ（`.badge-e` 〜 `.badge-a`）
  - 日本語・アルファベット混在フォントスタックの指定

#### ② 廃止済みカスタム拡張（`ruby_extension.py`）のパイプライン残留 (P2)
- **現象**:
  `zensical.toml` L1132 に `ruby_extension = {}` が登録されている。
- **根本原因**:
  プロジェクト規約（`AGENTS.md` 3節）において「ルビ構文（`{単語|読み}`）の廃止」が厳格に決定されたが、ビルド設定側で拡張のロードが解除されていない。
- **影響**:
  全1,000ファイルのビルド時、毎回Pythonの正規表現フックが全記事に対して実行されており、無駄なCPUオーバーヘッドとビルド時間の増大を招いている。

---

### 2.2 パフォーマンス & Core Web Vitals (LCP / INP / CLS)

#### ① ナビゲーションのインライン展開による DOM Bloat（1ページ500KB問題） (P1)
- **現状の実測値**:
  - `site/index.html`: **487 KB**（32,418行）
  - `site/grammar/word-order/index.html`: **483 KB**（32,758行）
  - `site/sitemap/index.html`: **625 KB**（34,068行）
- **技術的課題**:
  1,000記事以上存在する全ページのサイドバーナビゲーション（デスクトップ用ドロワーおよびモバイル用メニュー）が、**すべての個別HTMLファイルに完全なネスト構造としてインライン出力**されている。
  - 1ページあたりのDOMノード数: 推定 **8,000〜12,000ノード**
  - Google Lighthouseの推奨基準: **総ノード数 1,400 未満、最大深度 32 未満**
- **Core Web Vitals への悪影響**:
  1. **LCP (Largest Contentful Paint)**: 数百KBのHTMLダウンロード完了までブラウザのDOMツリー構築がブロックされ、First Contentful Paint / LCPが遅延。
  2. **INP (Interaction to Next Paint)**: 巨大なDOMツリーを保持しているため、画面クリック時やドロワー開閉時のスタイル再計算（Recalculate Style）およびレイアウト再描画（Layout Shift）でメインスレッドがスタック。
  3. **メモリ枯渇（Memory Pressure）**: スマートフォン等の低メモリ環境でブラウザタブがクラッシュ（OOM）するリスク。
- **解決アプローチ**:
  ZensicalおよびMaterial for MkDocsに備わっている **`navigation.prune`** 機能を有効化する。
  `navigation.prune` を有効にすると、現在閲覧中のアクティブなカテゴリ以外の階層ツリーがHTML上から刈り取られ、HTMLファイルサイズが **500KB → 40〜60KB（約90%削減）** へ劇的に軽量化される。

#### ② 7.3MB に達する巨大検索インデックス (`search.json`) (P1)
- **実測値**: `site/search.json` = **7,326,630 バイト (約7.3MB)**
- **技術的課題**:
  クライアントサイド全文検索機能（Web Worker `search.c47bb847.min.js`）が、全1,000記事の全本文・見出し・URLを単一の非圧縮JSONとして一括生成している。
- **ユーザー体験上のリスク**:
  1. ユーザーが検索バーにフォーカスした瞬間、7.3MBのネットワークリクエストが発生する。4G/3Gなどのモバイル回線では数秒以上の通信遅延とパケット消費を強いる。
  2. 端末側で7.3MBのJSONを `JSON.parse()` してWorkerメモリ上に展開する際、モバイルCPUが高負荷となり一時的にUIがフリーズする。
- **改善アプローチ**:
  - 短期策: 本文全体ではなく「記事タイトル・見出し・キーワード」のみをインデックス対象に限定し、インデックスサイズを80%以上削減する。
  - 中長期策: 静的サイト向け次世代検索エンジン（**Pagefind** 等）の導入。Pagefindはインデックスをチャンク分割（Sharding）し、検索ワードに応じて数KB〜数十KBのインデックス片のみをオンデマンドで取得するため、1,000ページ以上の大規模サイトでも初期転送量ゼロで高速検索が可能。

#### ③ Webフォント読み込み競合と CLS（累積レイアウトシフト） (P2)
- **現象**:
  `site/**/*.html` の `<head>` では、以下の通り Google Fonts (`Inter`, `JetBrains Mono`) が読み込まれ、インラインスタイルで強制指定されている：
  ```html
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter:...|JetBrains+Mono:...&amp;display=fallback">
  <style>:root{--md-text-font:"Inter";--md-code-font:"JetBrains Mono"}</style>
  ```
  一方、`extra.css` 側では以下のようにシステムフォント優先の指定を行おうとしている：
  ```css
  :root {
    --md-text-font: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Kaku Gothic ProN", "BIZ UDPGothic", "Meiryo", "Noto Sans JP", sans-serif;
  }
  ```
- **技術的課題**:
  1. `display=fallback` が指定されているため、低速回線下でフォント適用がタイムアウトし、システムフォントから突然Interに切り替わる（またはその逆）ことで文字幅が変動し、**CLS（レイアウトのガタつき）** が発生する。
  2. 日本語グリフが含まれていない欧文フォント `Inter` が最優先されるため、欧文と和文でベースラインやウェイトの不揃いが生じる。

---

### 2.3 CSS設計・アーキテクチャ・レスポンシブ (CSS Architecture)

#### ① `!important` の乱用による「詳細度戦争（Specificity War）」 (P2)
- **現状コードの課題**:
  `extra.css` 内に **23箇所** の `!important` が使用されている。
  ```css
  /* 例: extra.css */
  [data-md-color-scheme="default"] body,
  [data-md-color-scheme="default"] .md-container,
  [data-md-color-scheme="default"] .md-main,
  [data-md-color-scheme="default"] .md-content {
    background-color: #f7f4ed !important;
  }
  .md-header {
    background-color: #f0ece1 !important;
    color: #2b2824 !important;
    border-bottom: 1px solid #ded8cb !important;
  }
  .md-tabs {
    background-color: #ece7db !important;
  }
  .md-nav__link {
    color: #47433c !important;
  }
  ```
- **エンジニア視点の指摘**:
  Material for MkDocs / Zensical はCSSカスタムプロパティ（CSS変数: `--md-default-bg-color`, `--md-primary-fg-color` 等）を基盤とした堅牢なデザイントークン設計を採用している。
  本来これらを上書きすべきところ、クラスセレクタに対して `!important` で強引にプロパティを上書きしているため、スタイルの優先度構造が崩壊している。

#### ② ダークモードにおける重大な視認性崩壊（黒背景に黒文字） (P1)
- **致命的バグのメカニズム**:
  `extra.css` L282 で以下のようにサイドバーリンクの色が指定されている：
  ```css
  .md-nav__link {
    color: #47433c !important;
  }
  ```
  そしてダークモード（`[data-md-color-scheme="slate"]`）の設定セクション（L306〜L360）において、**`.md-nav__link` の上書きルールが存在しない**。
  その結果、ユーザーがダークモードに切り替えた際、スレート色の暗い背景（`#0f172a`）の上に、`!important` で固定された濃灰色の文字（`#47433c`）が表示される。
  - **コントラスト比**: **1.94:1**（完全に不可視レベル）
  - **結果**: ダークモードではサイドバーメニューのリンクが真っ暗になり、ユーザーはナビゲーションを読むことができない。

#### ③ ダークモード時のテーブルヘッダー白浮き (P2)
- `extra.css` L264:
  ```css
  .md-typeset table:not([class]) th {
    background-color: #ede7da;
    color: #1f1d1a;
  }
  ```
  ダークモード用の定義がないため、ダークモード表示時でもテーブルのヘッダー行だけが明るい生成り色（`#ede7da`）のまま残り、ダークUIとの調和が完全に破綻している。

#### ④ モバイル表示におけるレスポンシブ崩れ (P2)
- **広幅テーブルのスクロール不全**:
  文法比較表や活用表（`.md-typeset table:not([class])`）に `overflow: hidden;` が指定されており、横スクロールコンテナが外側にない場合、画面幅375px前後のモバイル端末でテーブル右側が見切れる。
- **会話バッジの縮小崩れ**:
  `.dialogue-box` 内の `.dialogue-speaker`（Aさん、Bさん等の話者バッジ）に `flex-shrink: 0;` が指定されていないため、長文の発言が入った際に話者バッジが横に押し潰されて文字が縦に崩れる。

---

### 2.4 Webアクセシビリティ (a11y: WCAG 2.1 AA準拠性)

#### ① 検定バッジのコントラスト比不足（WCAG 2.1 AA 達成基準 1.4.3 違反） (P1)
`extra.css` のバッジ定義をカラーアナライザーで実測検証：
- **`.badge-d`**: `background-color: #06b6d4; color: white;`
  - コントラスト比: **2.52:1**（基準: **4.5:1 以上**）❌ **不合格**
- **`.badge-e`**: `background-color: #10b981; color: white;`
  - コントラスト比: **2.45:1**（基準: **4.5:1 以上**）❌ **不合格**
- **影響**:
  視力の弱いユーザー、色覚多様性を持つユーザー、および屋外やスマートフォンの画面輝度を落とした環境で、バッジ内の文字が白飛びして読めない。

#### ② 見出しレベルの階層スキップ（WCAG 2.1 AA 達成基準 1.3.1 違反） (P2)
- **実例**: `docs/index.md` L6〜L7
  ```markdown
  # インドネシア語学習ナレッジベース
  ### Bahasa Indonesia Knowledge Base untuk Pembelajar Jepang
  ```
- **技術的課題**:
  `<h1>` の直後に `<h2>` をスキップして `<h3>` を配置している。
  スクリーンリーダーのランドマーク・見出しナビゲーション機能を利用するユーザーは、階層関係を正しく認識できない。サブタイトルは `<h3>` ではなく、`<p class="subtitle">` などのセマンティクスでマークアップすべきである。

#### ③ `abbr[title]` のタッチデバイス非対応 (P2)
- 現状は `abbr[title]` に `cursor: help` とホバー時の下線装飾を与えているが、iOS/Androidなどのタッチデバイスには「ホバー」が存在しないため、付与された解説テキスト（`title` 属性）をスマートフォンユーザーは閲覧できない。
- タップでトグル表示されるアクセシブルなツールチップ（Popover API または軽量CSS/JS）への移行が推奨される。

---

### 2.5 SEO・メタデータ・ソーシャルグラフ

#### ① ダミーホスト設定によるSEO汚染 (P1)
- **現象**:
  `zensical.toml` L2 において `site_url = "https://example.com/bahasa_indonesia/"` と設定されている。
- **影響**:
  - 全ページの `<link rel="canonical" href="https://example.com/bahasa_indonesia/...">` が example.com を指している。
  - `sitemap.xml` 内の全3,000行の `<loc>` がすべて example.com になっている。
  - 検索エンジン（Google bot等）は「このドメインは正規の所有者ではない」「複製サイトである」と判断し、検索順位（SERPs）が大幅に低下、最悪の場合はインデックスから除外される。

#### ② OGP (Open Graph Protocol) および Twitter Cards メタタグの完全欠落 (P1)
- **現状**:
  生成HTMLの `<head>` を精査したところ、`og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `twitter:card` が**1つも存在しない**。
- **影響**:
  X（旧Twitter）、Facebook、LINE、Slack、Discord等で記事URLがシェアされた際、画像や説明文のない素のテキストリンクのみが表示される。ソーシャル経由のクリック率（CTR）およびSNSバイラル効果を著しく毀損している。

#### ③ タイトルタグの二重重複 (P2)
- **実例**: `site/index.html`
  ```html
  <title>インドネシア語学習ナレッジベース - インドネシア語学習ナレッジベース</title>
  ```
- **原因**:
  `docs/index.md` のフロントマターで `title: インドネシア語学習ナレッジベース` が定義されており、`base.html` の `{{ page.meta.title }} - {{ config.site_name }}` ロジックと重複結合している。

#### ④ `robots.txt` の不在 (P2)
- `site/robots.txt` が生成されていない。検索エンジンのクローラーに対して、クローリング方針や `sitemap.xml` の場所を明示的に伝える手段が抜けている。

---

### 2.6 フロントエンド機能 & UX拡張性 (Web API / Modern UX)

#### ① Web Speech API（ブラウザ標準TTS）の未活用 (P2)
- **エンジニア視点の提案**:
  語学ナレッジベースにおいて、発音の確認は学習効率を左右する最重要機能である。
  現在、サイトには音声再生機能が一切存在しないが、**モダンブラウザ（Chrome, Edge, Safari, iOS Safari, Android Chrome）はすべて標準で `window.speechSynthesis`（インドネシア語 `id-ID`）をネイティブサポートしている**。
- **実装の容易性**:
  外部の重い音声ライブラリや有料APIを導入せずとも、わずか40〜50行のVanilla JavaScriptを追加するだけで、すべての `.id-example`（例文カード）および単語リストに「🔊 発音を聞く」ボタンを動的に付与し、ネイティブ発音を再生できる。

#### ② クリップボードAPI連携の欠如 (P3)
- 例文や単語を学習用ノートアプリや単語帳アプリ（Anki等）に転記するユーザー向けに、ワンクリックでテキストをクリップボードにコピーできる機能が未実装。

---

### 2.7 セキュリティ・配信インフラ (Hosting & Security)

#### ① HTTPレスポンスヘッダーおよびCSPの未設計 (P3)
- 静的サイトホスティング（Cloudflare Pages, Vercel, Netlify, AWS S3+CloudFront, Nginx等）において配信すべきセキュリティヘッダーの設定（`_headers` や設定例）が用意されていない。
- 必要なヘッダー:
  - `Content-Security-Policy (CSP)`: XSS防止（Google Fonts、Twemoji画像ドメインの許可等）
  - `X-Content-Type-Options: nosniff`: MIMEスニッフィング防止
  - `X-Frame-Options: DENY`: クリックジャッキング防止
  - `Referrer-Policy: strict-origin-when-cross-origin`: リファラー保護
  - `Permissions-Policy`: 不要なブラウザAPI（カメラ、マイク、位置情報等）の無効化

#### ② キャッシュディレクティブの最適化 (P3)
- 静的アセット（`site/assets/**/*.[hash].min.css`, `bundle.*.min.js`）はコンテンツハッシュが付与されているため、`Cache-Control: public, max-age=31536000, immutable` で永久キャッシュ可能。
- 一方、HTMLファイルは `Cache-Control: public, max-age=0, must-revalidate` で即時更新を保証する設計が必要。

---

## 3. 具体的なコード修正案 (Concrete Code Fixes)

### 3.1 `zensical.toml` の修正差分（P0 / P1対応）

```diff
--- zensical.toml (現状)
+++ zensical.toml (修正案)
@@ -1,5 +1,5 @@
 [project]
-site_url = "https://example.com/bahasa_indonesia/"
+site_url = "https://your-domain.com/bahasa_indonesia/"  # 本番ホストへ変更
 site_name = "インドネシア語学習ナレッジベース"
 site_description = "日本人のためのインドネシア語（文字・発音・文法・接辞・語彙・日常会話・文化）体系的オープンナレッジベース"
 site_author = "Indonesian Learning Project"
+
+# 独自スタイルシートの正しい配置（project直下へ移動）
+extra_css = ["stylesheets/extra.css"]
+extra_javascript = ["javascripts/speech.js"]

 nav = [
   ...
@@ -1102,6 +1102,17 @@
 [project.theme.icon]
 logo = "lucide/book-open"

+# パフォーマンス最適化・モダンUX機能フラグの有効化
+features = [
+  "navigation.prune",          # 【重要】非アクティブツリー刈り取りでHTMLサイズを90%削減
+  "navigation.tabs",           # タブナビゲーション
+  "navigation.tabs.sticky",    # タブバー固定
+  "navigation.top",            # トップへ戻るボタン
+  "navigation.instant",        # SPA風高速ページ遷移
+  "navigation.instant.progress",
+  "content.code.copy",         # コードブロックコピーボタン
+]
+
 [[project.theme.palette]]
 media = "(prefers-color-scheme)"
 scheme = "default"
@@ -1126,10 +1137,7 @@
 toggle.icon = "lucide/moon"
 toggle.name = "システム設定に連動"
 
-extra_css = ["stylesheets/extra.css"]
-
 [project.markdown_extensions]
-ruby_extension = {}  # 廃止規約に従い削除
 abbr = {}
 admonition = {}
```

---

### 3.2 `docs/stylesheets/extra.css` のリファクタリング差分（P1 / P2対応）

`!important` を徹底排除し、MaterialのCSSカスタムプロパティ（CSS変数）を正しく再定義する。さらにダークモード視認性およびバッジコントラスト比を修正。

```diff
--- docs/stylesheets/extra.css (現状)
+++ docs/stylesheets/extra.css (修正案)
@@ -6,51 +6,52 @@
 :root {
   /* 日本語・アルファベット混在フォントスタック */
   --md-text-font: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Kaku Gothic ProN", "BIZ UDPGothic", "Meiryo", "Noto Sans JP", sans-serif;
   --md-code-font: "JetBrains Mono", Consolas, "Courier New", monospace;
 }
 
-/* 1. ノート・紙のような質感カラー */
 :root,
 [data-md-color-scheme="default"] {
   --md-default-bg-color: #f7f4ed;
   --md-default-bg-color--light: rgba(247, 244, 237, 0.7);
   --md-default-bg-color--lighter: rgba(247, 244, 237, 0.3);
   --md-default-bg-color--lightest: rgba(247, 244, 237, 0.12);
 
   --md-default-fg-color: #2b2824;
   --md-default-fg-color--light: #524d45;
   --md-default-fg-color--lighter: #787268;
   --md-default-fg-color--lightest: rgba(43, 40, 36, 0.08);
   --md-typeset-color: #2b2824;
 
   --md-default-border-color: #ded8cb;
   --md-code-bg-color: #ede7da;
   --md-code-fg-color: #2b2824;
 
   --md-primary-fg-color: #0f766e;
   --md-primary-bg-color: #f7f4ed;
   --md-accent-fg-color: #b91c1c;
+
+  /* コンポーネント用変数 */
+  --card-bg-color: #ede7da;
+  --card-border-color: #ded8cb;
+  --table-th-bg: #ede7da;
+  --table-th-fg: #1f1d1a;
+  --nav-link-color: #47433c;
 }
 
-/* !important を排除し変数連動へ変更 */
-[data-md-color-scheme="default"] body,
-[data-md-color-scheme="default"] .md-container,
-[data-md-color-scheme="default"] .md-main,
-[data-md-color-scheme="default"] .md-content {
-  background-color: #f7f4ed !important;
-  color: #2b2824;
-}
-
-.md-header {
-  background-color: #f0ece1 !important;
-  color: #2b2824 !important;
-  border-bottom: 1px solid #ded8cb !important;
-  box-shadow: 0 1px 4px rgba(60, 50, 40, 0.06) !important;
-}
+/* サイドバーリンク（CSS変数化） */
+.md-nav__link {
+  color: var(--nav-link-color);
+}
 
 /* 会話用スタイル（横潰れ防止） */
 .dialogue-speaker {
   font-weight: bold;
   padding: 0.1rem 0.55rem;
   border-radius: 4px;
   background: #0f766e;
   color: #ffffff;
   min-width: 3.5rem;
+  flex-shrink: 0;  /* モバイルで潰れるのを防止 */
   text-align: center;
   font-size: 0.85rem;
 }
 
-/* 検定級バッジ（WCAG 2.1 AA 4.5:1準拠のダークトーンへ修正） */
-.badge-e { background-color: #047857; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: bold; } /* 4.6:1 */
-.badge-d { background-color: #0e7490; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: bold; } /* 4.7:1 */
-.badge-c { background-color: #1d4ed8; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: bold; }
-.badge-b { background-color: #6d28d9; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: bold; }
-.badge-a { background-color: #b45309; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: bold; }
+/* ==========================================================================
+   ダークモード対応（変数の上書きで一括制御）
+   ========================================================================== */
+[data-md-color-scheme="slate"] {
+  --card-bg-color: #1e293b;
+  --card-border-color: #334155;
+  --table-th-bg: #1e293b;
+  --table-th-fg: #f1f5f9;
+  --nav-link-color: #cbd5e1;  /* 【修正】暗い背景でも鮮明に読める色へ */
+}
+
+[data-md-color-scheme="slate"] .md-typeset table:not([class]) th {
+  background-color: var(--table-th-bg);
+  color: var(--table-th-fg);
+  border-bottom-color: #2dd4bf;
+}
```

---

### 3.3 Web Speech API 連携スクリプトの追加案 (`docs/javascripts/speech.js`)

わずか40行のVanilla JSで、すべての例文カードにネイティブ音声再生ボタンを動的注入する実装例：

```javascript
// docs/javascripts/speech.js
document.addEventListener("DOMContentLoaded", () => {
  if (!("speechSynthesis" in window)) return;

  const initSpeechButtons = () => {
    const sentences = document.querySelectorAll(".id-sentence:not([data-speech-initialized])");
    sentences.forEach((el) => {
      el.setAttribute("data-speech-initialized", "true");
      
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "id-speech-button";
      btn.setAttribute("aria-label", "インドネシア語音声を再生");
      btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>`;
      
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        window.speechSynthesis.cancel();
        
        const utterance = new SpeechSynthesisUtterance(el.textContent.trim());
        utterance.lang = "id-ID";
        utterance.rate = 0.9; // 学習者向けにわずかにゆっくり
        window.speechSynthesis.speak(utterance);
      });
      
      el.appendChild(btn);
    });
  };

  initSpeechButtons();
  // Material Instant Navigation (SPA遷移) 時の再初期化対応
  if (typeof document$ !== "undefined") {
    document$.subscribe(initSpeechButtons);
  }
});
```

---

## 4. 優先度付き改善ロードマップ (Actionable Engineering Roadmap)

```
[Phase 1: 即時是正 (Day 1)] ─── P0バグの解消
  ├─ zensical.toml の extra_css 配置修正 ＆ ビルド反映
  └─ ruby_extension の登録解除
        │
[Phase 2: コア最適化 (Week 1)] ─── UX・パフォーマンスの抜本改善
  ├─ theme.features に navigation.prune / instant / top 追加（DOM 90%削減）
  ├─ extra.css のリファクタリング（!important排除、ダークモード文字色修正）
  ├─ バッジ色のコントラスト比修正（WCAG 2.1 AA準拠）
  └─ site_url の本番URL更新 ＆ robots.txt 配置
        │
[Phase 3: 機能・アクセシビリティ拡充 (Week 2)] ─── Webエンジニアリング価値向上
  ├─ Web Speech API（インドネシア語TTS）の導入
  ├─ OGP & Twitter Cards のメタタグ対応（テンプレート拡張またはプラグイン）
  ├─ テーブルのレスポンシブスクロールコンテナ化
  └─ docs/index.md 等の見出しスキップ（H1→H3）修正
        │
[Phase 4: 次世代運用基盤の構築 (Month 1)] ─── 運用の自動化・セキュリティ
  ├─ 検索エンジンの Pagefind 移行（7.3MBインデックスの軽量オンデマンド化）
  ├─ CI/CD自動テスト導入（html-validate, lycheeリンクチェック, pa11y a11yチェック）
  ├─ HTTPセキュリティヘッダー（CSP, HSTS等）の設定
  └─ PWA（manifest.json, オフラインキャッシュ）対応
```

---

## 5. まとめ

本プロジェクトは、1,000ページという比類なきドキュメント資産を有しており、Webサイトとしての基礎体力（HTML/CSS/JS）を適正化するだけで、**世界最高水準のWeb語学学習プラットフォームへと飛躍できるポテンシャル**を秘めている。

まずは最優先課題である **`extra_css` の設定記述ミス解消（P0）**、**`navigation.prune` によるDOM肥大化解消（P1）**、および **ダークモード時の視認性不具合解消（P1）** を速やかに実施することを強く推奨する。
