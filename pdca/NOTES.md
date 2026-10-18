# 気づき・改善メモ (Editorial Notes)

組織の全メンバー（Director, Writer, Reviewer, Engineer, BOSS）が、作業中に「気がついたこと」「改善したほうがよいこと」「学習者のつまずきポイント」を自由に書き留めるファイルです。
上司（BOSS）が本ファイルを定期的に精査し、根本原因を分析して `pdca/IMPROVEMENTS.md` や `pdca/GUIDELINES.md` に反映します。

---

## 📝 ログ一覧

### 2026-10-18: プロジェクト初期立ち上げ
- **Engineer**: 
  - サイトプレビューサーバーのポートを日本語学習サイト（8000）と重複しないよう `8001` に設定完了。
  - ルビ拡張 `ruby_extension.py` を配置し、`.venv\Lib\site-packages\local_project.pth` により確実なモジュール参照を確立。
  - PowerShell環境での文字化けや実行ポリシーに対応するため、`powershell -ExecutionPolicy Bypass -File .\format.ps1` を標準検証コマンドに設定。
- **Director**: 
  - 日本人学習者向けの体系的なカリキュラム進捗ツリー（文字・発音、文法、接辞、日常会話、語彙、スラング・文化、検定対策）を `task/PROGRESS.md` に策定。
- **BOSS**: 
  - 自律編集体制の土台を確立。今後は指示書発行（Director）から執筆・校正・ビルドの自律サイクルを回す準備が整った。
