# インドネシア語学習ナレッジベース (Bahasa Indonesia Knowledge Base)

MkDocs Materialの後継である超高速静的サイトジェネレーター **[Zensical](https://zensical.org)** で構築した、日本人のための体系的なインドネシア語学習ナレッジベースです。

Antigravity（AI組織: Director, Writer, Reviewer, Engineer, BOSS）による自律編集・執筆・校正・ビルド・PDCAサイクルに対応しています。

---

## 📂 ディレクトリ構成

```text
bahasa_indonesia/
├── zensical.toml                # サイト全体の設定ファイル（メタデータ、テーマ、ナビゲーション）
├── AGENTS.md                    # Antigravity AI組織 運用ルール（行動原則・インバリアント）
├── README.md                    # 本ドキュメント
├── requirements.txt             # Python依存パッケージ（zensical, djlint）
├── ruby_extension.py            # ルビ（カタカナ読み・注釈）およびツールチップ用拡張
├── .djlintrc                    # HTMLフォーマッター設定
├── format.bat                   # HTML一括整形バッチ
├── format.ps1                   # PowerShell用HTML整形スクリプト
├── run_server.bat               # ローカルサーバー起動バッチ（ポート 8001）
├── run_server.ps1               # PowerShell用起動スクリプト（ポート 8001）
├── .gitignore                   # Git除外設定
├── .agents/                     # Antigravity エージェント・スキル定義
│   ├── agents/                  # 5役職（director, writer, reviewer, engineer, boss）
│   └── skills/                  # 自律編集スキル（autonomous-editorial）
├── task/                        # 作業用フォルダー
│   └── PROGRESS.md              # カリキュラム進捗ツリー（指示書・校正タスクをここに配置）
├── pdca/                        # 改善・気づきフォルダー
│   ├── GUIDELINES.md            # 組織共通執筆・校正ガイドライン
│   ├── NOTES.md                 # 各員の気づき・改善メモ
│   └── IMPROVEMENTS.md          # 上司（BOSS）によるPDCA改善レポート
├── editorial/                   # AI組織構造・運用マニュアル
└── docs/                        # ナレッジ記事のMarkdown格納場所
    ├── index.md                 # サイトトップページ
    └── stylesheets/
        └── extra.css            # カスタムCSS（アイボリーノート風デザイン、例文カード等）
```

---

## 🚀 使い方

### 1. ローカルプレビューサーバーの起動
ファイルを編集するとブラウザが即座に自動リロード（ホットリロード）されます。

> [!NOTE]
> 日本語学習サイト（ポート8000）と重複しないよう、本サイトは **ポート 8001** で起動します。

- **方法 A (簡単)**: `run_server.bat` をダブルクリック
- **方法 B (CLI)**:
  ```powershell
  .\.venv\Scripts\zensical.exe serve -a localhost:8001
  ```
  起動後、ブラウザで [http://localhost:8001](http://localhost:8001) を開きます。

### 2. 静的サイトのビルド
```powershell
.\.venv\Scripts\zensical.exe build
```
`site/` ディレクトリにHTML/CSS/JS一式が出力されます。

### 3. HTMLのフォーマット（コード自動整形）
ビルド後のHTMLから無駄な空行やインデント崩れを一括除去・整形します。
```powershell
powershell -ExecutionPolicy Bypass -File .\format.ps1
```

---

## 🤖 Antigravity による自律編集サイクル

Antigravity に向かって「**自律編集サイクルを回して**」「**次の記事を執筆して**」と指示するだけで、以下のフローが自律的に実行されます。

1. **Director（編集長）**: `task/PROGRESS.md` から未着手トピックを選定し、`task/TASK-xxx.md` を発行。
2. **Writer（執筆担当）**: 指示書に基づき `docs/...` に記事を作成、`task/REVIEW-xxx.md` を起票。
3. **Reviewer（校正担当）**: インドネシア語の正しさ・用例・ルビを検証し承認。
4. **Engineer（エンジニア）**: `zensical.toml` へのナビ登録、ビルドおよびHTMLフォーマットを検証。
5. **BOSS（上司）**: サイクルを振り返り、`pdca/NOTES.md` から改善点を抽出して `pdca/GUIDELINES.md` を更新。
