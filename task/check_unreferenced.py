import os
import re

# 1. Read existing zensical.toml nav files
with open('zensical.toml', 'r', encoding='utf-8') as f:
    content = f.read()

# find all .md files referenced in nav
referenced_files = set(re.findall(r'\"([^\"]+\.md)\"', content))

# 2. Get all markdown files in docs
all_docs_files = []
for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(root, file), 'docs').replace('\\', '/')
            all_docs_files.append(rel_path)

print(f"Total files in docs: {len(all_docs_files)}")
print(f"Referenced in nav: {len(referenced_files)}")

unreferenced = [f for f in all_docs_files if f not in referenced_files]
print(f"Unreferenced files: {len(unreferenced)}")

# Print counts by category in unreferenced
from collections import Counter
counts = Counter([f.split('/')[0] if '/' in f else 'root' for f in unreferenced])
for cat, cnt in counts.items():
    print(f"  {cat}: {cnt}")
