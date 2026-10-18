"""Git Checkpoint Helper for Autonomous Editorial Organization

未コミットの記事（docs/配下）の数を数え、指定のしきい値（デフォルト10本）以上、
または全体修正・強制コミット（--force）時に、zensical buildを検証した上で自動コミットします。
"""

import sys
import subprocess
from pathlib import Path

THRESHOLD = 10

def run_command(cmd, shell=True, check=True):
    res = subprocess.run(cmd, shell=shell, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and res.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}\n{res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)
    return res

def get_uncommitted_files():
    res = run_command("git status --porcelain", check=False)
    lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    return lines

def get_uncommitted_docs(all_lines):
    # docs/ 配下の未コミットファイル（新規または変更）
    docs = [l for l in all_lines if "docs/" in l]
    return docs

def main():
    force = "--force" in sys.argv
    threshold = THRESHOLD
    for arg in sys.argv:
        if arg.startswith("--threshold="):
            threshold = int(arg.split("=")[1])

    all_uncommitted = get_uncommitted_files()
    total_count = len(all_uncommitted)
    doc_uncommitted = get_uncommitted_docs(all_uncommitted)
    doc_count = len(doc_uncommitted)

    print(f"[INFO] Uncommitted status: docs={doc_count} (threshold: {threshold}), total={total_count}")

    # トリガー判定:
    # 1. docs記事数がしきい値(10本)以上
    # 2. --force 指定かつ未コミット変更が存在する
    should_commit = (doc_count >= threshold) or (force and total_count > 0)

    if should_commit:
        print(f"[INFO] Triggering automatic Git checkpoint (docs={doc_count}, total={total_count}, force={force})...")
        
        # 1. Build validation
        print("[INFO] Running zensical build verification...")
        build_res = subprocess.run(r".\.venv\Scripts\zensical.exe build", shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if build_res.returncode != 0:
            print(f"[ERROR] Build failed! Aborting commit:\n{build_res.stderr}\n{build_res.stdout}", file=sys.stderr)
            sys.exit(1)
        print("[INFO] Zensical build passed.")

        # 2. Stage changes (docs, nav, tasks, pdca, rules)
        print("[INFO] Staging project changes...")
        run_command("git add docs/ zensical.toml task/ pdca/ .agents/ AGENTS.md editorial/")

        # 3. Create commit message
        custom_msg = None
        for i, arg in enumerate(sys.argv):
            if arg == "-m" and i + 1 < len(sys.argv):
                custom_msg = sys.argv[i + 1]

        if not custom_msg:
            if doc_count > 0:
                custom_msg = f"feat: add/update {doc_count} articles and curriculum updates (auto-checkpoint)"
            else:
                custom_msg = f"chore: organization rules and task updates (auto-checkpoint)"

        commit_res = subprocess.run(["git", "commit", "-m", custom_msg], capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(commit_res.stdout)
        if commit_res.returncode == 0:
            print(f"[SUCCESS] Committed successfully ({total_count} files).")
        else:
            print(f"[WARNING] Commit returned code {commit_res.returncode}:\n{commit_res.stderr}")
    else:
        print(f"[INFO] Condition not met (docs: {doc_count} < {threshold}). No commit needed at this step.")

if __name__ == "__main__":
    main()
