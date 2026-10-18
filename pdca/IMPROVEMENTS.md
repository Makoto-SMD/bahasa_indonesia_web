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
