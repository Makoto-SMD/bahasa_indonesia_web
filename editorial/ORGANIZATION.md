# AI編集組織の構造と自律運用マニュアル (Editorial Organization Manual)

本ドキュメントは、日本人向けインドネシア語学習ナレッジベース（Zensical）を自律的かつ高品質に構築・保守するための「AI編集組織」の構造、各役職の責務、およびデータフローを定義したものです。

---

## 🚨 共通運用ルール（組織全員が参照・厳守）
1. **編集対象範囲**:
   - ⭕ **「`docs/`」配下の記事**を編集対象とする。
   - ❌ 開発環境やスクリプトは編集対象外。
2. **フォルダーの役割**:
   - **`task/` フォルダー**: AI組織の各員が作業に必要なファイル（指示書、校正タスク、進捗ツリー等）を入れる。
   - **`pdca/` フォルダー**: 気がついたこと、改善したほうがよいこと、PDCA改善レポート、組織ガイドラインを入れる。
3. **ローカルサーバーポート**:
   - **8001**（`http://localhost:8001`）
4. **定期的なGitコミットの実行 (Git Commits)**:
   - **未コミット記事が10本以上**、または**セクション完了・全体修正時**には、Engineerが必ずGitコミット（`python .\task\check_git_checkpoint.py`）を実行して作業成果を確定させる。

---

## 1. 組織図とデータフロー

```mermaid
flowchart TD
    BOSS["👔 上司 (BOSS)<br/>組織全体の監視 / PDCA / 改善案発行"]
    DIRECTOR["📋 編集長 (Director)<br/>進捗監視 / トピック決定 / 執筆指示書"]
    WRITER["✍️ 執筆担当 (Writer)<br/>記事作成 / ルビ付与 / 修正対応"]
    REVIEWER["🔍 校正 (Reviewer)<br/>正確性・自然さ検証 / 校正FB / 承認"]
    ENGINEER["⚙️ ビルド・検証・Git (Engineer)<br/>HTML崩れ・リンク切れ・nav登録検証・Gitコミット"]

    PROGRESS[("📊 全体進捗ツリー<br/>task/PROGRESS.md")]
    TASKS[("📝 執筆指示書<br/>task/TASK-xxx.md")]
    REVIEWS[("💬 校正フィードバック<br/>task/REVIEW-xxx.md")]
    ARTICLES[("📄 インドネシア語記事<br/>docs/")]
    HTML[("🌐 ビルド成果物<br/>site/")]
    GIT[("📦 Gitリポジトリ<br/>commit checkpoint")]
    PDCA_NOTES[("📝 気づき・メモ<br/>pdca/NOTES.md")]
    PDCA_IMPROVE[("💡 改善案・規約<br/>pdca/IMPROVEMENTS.md<br/>pdca/GUIDELINES.md")]

    %% 作業フロー
    PROGRESS --> DIRECTOR
    DIRECTOR -->|Task Spec 発行| TASKS
    TASKS --> WRITER
    WRITER -->|記事作成| ARTICLES
    WRITER -->|校正タスク起票| REVIEWS
    ARTICLES --> REVIEWER
    REVIEWS <-->|修正指示 / 再提出| WRITER
    REVIEWER -->|承認 (Approve)| ENGINEER
    ENGINEER -->|Zensical ビルド| HTML
    HTML --> ENGINEER
    ENGINEER -->|10記事ごと/セクション完了時| GIT
    ENGINEER -.->|技術的校正FB| REVIEWS
    
    %% 気づきとPDCA
    WRITER -.->|気づき記録| PDCA_NOTES
    REVIEWER -.->|気づき記録| PDCA_NOTES
    ENGINEER -.->|気づき記録| PDCA_NOTES
    TASKS -.->|監視| BOSS
    REVIEWS -.->|監視| BOSS
    PDCA_NOTES -.->|分析| BOSS
    BOSS -->|改善案・規約更新| PDCA_IMPROVE
    PDCA_IMPROVE --> DIRECTOR
    PDCA_IMPROVE --> WRITER
    PDCA_IMPROVE --> REVIEWER
    PDCA_IMPROVE --> ENGINEER
```

---

## 2. 各役職の役割と入出力仕様

### 2.1 編集長（Director）
- **役割**: 全体カリキュラム（`task/PROGRESS.md`）の進捗を監視し、次に執筆すべきトピックを決定して執筆指示書を発行する。
- **入力**: `task/PROGRESS.md`、`docs/` の既存記事、`pdca/GUIDELINES.md`、`pdca/NOTES.md`
- **出力**: `task/TASK-{ID}_{slug}.md`（執筆指示書）、`task/PROGRESS.md` の更新

### 2.2 執筆担当（Writer）
- **役割**: 執筆指示書に従い、記事（`docs/...`）を執筆する。校正フィードバックに応じて修正する。
- **入力**: `task/TASK-xxx.md`、`task/REVIEW-xxx.md`（修正時）、`pdca/GUIDELINES.md`
- **出力**: `docs/...` の記事、`task/REVIEW-xxx.md`（校正タスク起票・修正報告）、`pdca/NOTES.md`（気づき）

### 2.3 校正（Reviewer）
- **役割**: 執筆された記事を精査し、インドネシア語の正しさ、自然な用例、ルビ記法、わかりやすさを検証・判定する。
- **入力**: `docs/...` の記事、`task/REVIEW-xxx.md`、`pdca/GUIDELINES.md`
- **出力**: `task/REVIEW-xxx.md`（修正指示または承認判定）、`pdca/NOTES.md`（気づき）

### 2.4 ビルド・検証・Gitコミット（Engineer）
- **役割**: 新規記事のナビゲーション登録確認、`zensical build`、`format.ps1` によるHTML崩れ・リンク切れ検証、および未コミット記事が10本以上またはセクション完了時の自動Gitコミット（`python .\task\check_git_checkpoint.py`）を行う。
- **入力**: `docs/`、`zensical.toml`、生成 HTML
- **出力**: `site/`、`Gitコミット`、`task/REVIEW-xxx.md` への検証結果記録、`pdca/NOTES.md`（気づき）

### 2.5 上司（BOSS）
- **役割**: `task/` 内の全指示・校正ログおよび `pdca/NOTES.md` の気づきを精査し、根本原因を突き止め、再発防止のPDCA改善案を発行する。
- **入力**: `task/` 配下の全ファイル、`pdca/NOTES.md`、Git差分
- **出力**: `pdca/IMPROVEMENTS.md`、`pdca/GUIDELINES.md` の改訂
