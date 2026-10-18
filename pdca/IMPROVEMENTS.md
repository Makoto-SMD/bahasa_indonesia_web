# PDCA 改善レポート集 (Continuous Improvement Reports)

上司（BOSS）が日々の執筆・校正・ビルドログおよび `pdca/NOTES.md` を分析し、再発防止策と組織改善案をまとめる台帳です。

---

## 📌 改善記録一覧

### [IMP-001] プロジェクト初期立ち上げとポート競合防止
- **発生状況 / 課題**:
  - 日本語学習ナレッジベース（ポート8000）と同時並行で稼働させる必要がある。
  - ルビ拡張の読み込みエラーやPowerShellスクリプトの実行ポリシー制限をあらかじめ防ぐ必要がある。
- **根本原因**:
  - デフォルトポート（8000）の重複による起動失敗リスク。
  - Python仮想環境のPYTHONPATH未解決。
- **再発防止策・改善内容**:
  1. `run_server.ps1` および `run_server.bat` のデフォルト引数を `-a localhost:8001` に固定。
  2. `.venv/Lib/site-packages/local_project.pth` を作成し、プロジェクトルートのモジュールを常にロード可能にした。
  3. `format.ps1` をASCIIベースの安全なスクリプト構造にし、`-ExecutionPolicy Bypass` で安定動作する手順を確立。
- **反映先**:
  - `run_server.ps1`, `run_server.bat`, `AGENTS.md`, `pdca/GUIDELINES.md`

### [IMP-002] インドネシア語記事におけるルビ（カタカナ読み等）の完全撤廃
- **発生状況 / 課題**:
  - 執筆記事内のインドネシア語文章に `{単語|カタカナ}` 構文でルビを振っていたが、読みにくく不自然であるため不要との改善提案（ユーザーFB）を受領。
- **根本原因**:
  - 日本語学習サイト向けに構築された初期テンプレート・ルビ機能がそのまま引き継がれていたこと。インドネシア語はアルファベット表記であり、文章全体にカタカナのルビを振る必要性がそもそもない。
- **再発防止策・改善内容**:
  1. **全既存記事（13記事・374箇所）のルビを完全削除**: アルファベット本来のすっきりした文章に一括置換。
  2. **組織規約・ガイドラインの改定**:
     - `AGENTS.md`: ルビ構文規約を削除し、ルビ付与を禁止・不要と明記。
     - `pdca/GUIDELINES.md`: 「2.1 ルビの廃止方針」としてルビ不要ルールを明記。
     - `.agents/skills/autonomous-editorial/SKILL.md`: Writer/Reviewerの工程からルビ要件を排除。
     - `.agents/agents/writer.md`, `reviewer.md`: 執筆時・校正時のチェック項目からルビを排除し、混入防止を義務付け。
  3. **今後のタスク指示書**: ルビ付与指示は一切行わない。
- **反映先**:
  - `AGENTS.md`, `pdca/GUIDELINES.md`, `.agents/skills/autonomous-editorial/SKILL.md`, `.agents/agents/writer.md`, `.agents/agents/reviewer.md`, `docs/` 配下全記事

