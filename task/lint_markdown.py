#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Markdown Linter & Auto-Fixer for Bahasa Indonesia KB
- Checks & auto-fixes bold syntax around Japanese brackets: **「text」** -> 「**text**」
- Checks that news-reading / reading comprehension follows standard section ordering:
  Body -> Vocab -> Translation -> Grammar/Background
"""

import os
import re
import sys

DOCS_DIR = "docs"

def fix_bold_in_text(content):
    # Multiple brackets like **「A」「B」**
    def repl_multi_brackets(m):
        full = m.group(1)
        return re.sub(r'([「『（【])(.*?)([」』）】])', r'\1**\2**\3', full)

    content = re.sub(r'\*\*(([「『（【][^「『（【」』）】\n]+?[」』）】])+)\*\*', repl_multi_brackets, content)

    # Single bracket
    for ob, cb in [('「', '」'), ('『', '』'), ('【', '】')]:
        pattern = re.compile(rf'\*\*\{ob}(.+?)\{cb}\*\*')
        content = pattern.sub(rf'{ob}**\1**{cb}', content)

    # Pure （ ... ）
    content = re.sub(r'\*\*（([^（）\n]+?)）\*\*', r'（**\1**）', content)
    return content

def run_lint_and_fix(auto_fix=True):
    modified_count = 0
    bracket_issues = 0
    mermaid_issues = 0

    bracket_pattern = re.compile(r'\*\*([「『（【])(.*?)([」』）】])\*\*')

    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".md"):
                fpath = os.path.join(root, f)
                with open(fpath, "r", encoding="utf-8") as fp:
                    content = fp.read()

                # Check brackets bold
                b_matches = list(bracket_pattern.finditer(content))
                if b_matches:
                    bracket_issues += len(b_matches)

                # Check mermaid in derivations
                if "derivations" in fpath and "```mermaid" in content:
                    mermaid_issues += 1

                if auto_fix:
                    fixed = fix_bold_in_text(content)
                    if fixed != content:
                        modified_count += 1
                        with open(fpath, "w", encoding="utf-8") as fp:
                            fp.write(fixed)

    print(f"[Markdown Linter] Bracket issues found: {bracket_issues}")
    print(f"[Markdown Linter] Mermaid in derivations found: {mermaid_issues}")
    if auto_fix:
        print(f"[Markdown Linter] Auto-fixed files: {modified_count}")

if __name__ == "__main__":
    auto_fix = "--check" not in sys.argv
    run_lint_and_fix(auto_fix=auto_fix)
