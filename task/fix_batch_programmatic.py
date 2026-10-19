# -*- coding: utf-8 -*-
with open('task/write_batch_1361_1370.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Execute code to get articles
locs = {}
code_to_run = text[:text.find('def generate_markdown')]
exec(code_to_run, locs)
articles = locs.get('articles', [])

for idx, a in enumerate(articles):
    # Fix matrix
    new_matrix = []
    for row in a.get('matrix', []):
        if len(row) == 4:
            # (word, pos, meaning, ex) -> (word, 'frasa', pos, meaning, ex)
            new_matrix.append((row[0], 'frasa', row[1], row[2], row[3]))
        else:
            new_matrix.append(row)
    a['matrix'] = new_matrix

    # Fix details
    new_details = []
    for row in a.get('details', []):
        if len(row) == 8:
            # (word, aff, pos, kana, desc, coloc, id_ex, ja_ex) -> remove aff
            new_details.append((row[0], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            new_details.append(row)
    a['details'] = new_details

# Reconstruct script
import pprint
import io

new_articles_str = pprint.pformat(articles, width=120, sort_dicts=False)

generator_code = text[text.find('def generate_markdown'):]

full_script = f"""# -*- coding: utf-8 -*-
\"\"\"
セクション33 第2バッチ (1361-1370) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾
\"\"\"

import os

articles = {new_articles_str}

{generator_code}
"""

with open('task/write_batch_1361_1370.py', 'w', encoding='utf-8') as f:
    f.write(full_script)

print("Reconstructed write_batch_1361_1370.py successfully.")
