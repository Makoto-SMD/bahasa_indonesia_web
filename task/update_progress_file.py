"""Update task/PROGRESS.md with 500 new articles.
"""

def update_progress():
    with open("task/PROGRESS.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Update summary header
    content = content.replace("Curriculum Progress Tree - 1,000 Articles", "Curriculum Progress Tree - 1,500 Articles")
    content = content.replace("- **総記事数**: 1,000記事（トップページ・総合サイトマップを含め全1,002ファイル）\n- **収録カテゴリ・セクション数**: 24 セクション\n- **進捗状況**: 1,000 / 1,000 記事 (100% 完了・検証済み)",
                              "- **総記事数**: 1,500記事（トップページ・総合サイトマップを含め全1,502ファイル）\n- **収録カテゴリ・セクション数**: 35 セクション\n- **進捗状況**: 1,000 / 1,500 記事 (66.7% 達成・500記事拡充フェーズ進行中)")

    with open("task/plan_500_articles.txt", "r", encoding="utf-8") as f:
        plan_text = f.read()

    new_content = content.rstrip() + "\n\n" + plan_text.strip() + "\n"

    with open("task/PROGRESS.md", "w", encoding="utf-8") as f:
        f.write(new_content)

    print("task/PROGRESS.md successfully updated with 500 new articles!")

if __name__ == "__main__":
    update_progress()
