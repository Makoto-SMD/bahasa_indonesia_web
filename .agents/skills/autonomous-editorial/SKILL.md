---
name: autonomous-editorial
description: >-
  Run autonomous editorial cycles with the AI organization (Director, Writer, Reviewer, Engineer, BOSS).
  Use when asked to autonomously write, review, build-verify, or manage the curriculum of the Indonesian learning knowledge base.
---

# 自律編集組織 運用スキル (Autonomous Editorial Skill)

本スキルは、Director（編集長）、Writer（執筆担当）、Reviewer（校正）、Engineer（ビルド・検証）、BOSS（上司）の5役職からなるAI組織を自律的に連携させ、高品質な日本人向けインドネシア語学習記事制作とPDCA改善を回すための運用手順書です。

---

## 🚨 共通運用ルール（組織全員が参照・厳守）
1. **編集対象範囲**:
   - ⭕ **「`docs/`」配下の記事**を執筆・編集する。
   - ❌ 意図しない設定変更や基盤ファイルの改変は禁止。
2. **フォルダーの役割**:
   - **`task/` フォルダー**: 作業に必要なファイル（進捗ツリー、執筆指示書、校正タスク、フィードバック）を入れる。
   - **`pdca/` フォルダー**: 気がついたこと、改善したほうがよいこと、PDCA改善レポート、組織ガイドラインを入れる。
3. **ローカルサーバー**:
   - ポート番号は **8001**（`http://localhost:8001`）を使用。
4. **定期的なGitコミットの実行 (Git Commits)**:
   - **未コミット記事が10本以上**、または**セクション完了・全体修正時**には、必ずPhase 4でGitコミットを実行する（後回し厳禁）。

---

## 自律サイクルの実行プロトコル

### Phase 1: 編集長（Director）
1. `task/PROGRESS.md` および `zensical.toml` を確認し、未着手のトピックを選定。
2. `pdca/GUIDELINES.md` と `pdca/NOTES.md` を参照し、注意点を把握。
3. 執筆指示書 `task/TASK-{ID}_{slug}.md` を発行。
4. `task/PROGRESS.md` のステータスを `[進行中]` に更新。

### Phase 2: 執筆担当（Writer）
1. `task/TASK-{ID}_{slug}.md` に従い、`docs/...` に記事を作成。
   - ❌ カタカナ等のルビ（`{単語|読み}`）は使用しない（アルファベットそのままの表記）。
   - 例文カード（`.id-example`）、会話カード（`.dialogue-box`）、重要語彙リストを活用。
2. 校正タスク `task/REVIEW-{ID}_{slug}.md` を起票。
3. 気づいたことがあれば `pdca/NOTES.md` に追記。

### Phase 3: 校正担当（Reviewer）
1. `task/REVIEW-{ID}_{slug}.md` と執筆記事を精査。
2. インドネシア語の綴り、文法の正確性、自然な用例、ルビが混入していないかを検証。
3. 指摘があれば修正指示を `task/REVIEW-xxx.md` に記載し Writer に差し戻し。問題なければ `[APPROVED]` を記録。
4. 執筆時のつまずき等に気づいたら `pdca/NOTES.md` に追記。

### Phase 4: ビルド・検証・Gitコミット（Engineer）
1. `zensical.toml` の `nav` に新規記事を登録。
2. ビルドとHTMLフォーマットを実行：
   ```powershell
   .\.venv\Scripts\zensical.exe build
   powershell -ExecutionPolicy Bypass -File .\format.ps1
   ```
3. **Gitコミット自動判定と実行**:
   - 以下のチェックスクリプトを実行し、未コミット記事が10本以上（またはセクション終了時 `--force`）の場合に自動コミットを完了させる：
   ```powershell
   python .\task\check_git_checkpoint.py
   # セクション完了時や即時コミットが必要な場合:
   # python .\task\check_git_checkpoint.py --force -m "feat: <詳細>"
   ```
4. 結果を `task/REVIEW-xxx.md` に記録。

### Phase 5: 上司（BOSS）
1. 今回のサイクルの指示書、校正ログ、差分、`pdca/NOTES.md` を精査。
2. 根本原因を分析し、再発防止策を `pdca/IMPROVEMENTS.md` にまとめる。
3. `pdca/GUIDELINES.md` を改訂。
4. `task/PROGRESS.md` のステータスを `[完了]` に更新。
