# -*- coding: utf-8 -*-
from write_batch_1331_1340 import articles

with open('zensical.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_idx = -1
for i, line in enumerate(lines):
    if 'contemporary/30-heritage-railway-revival.md' in line:
        target_idx = i
        break

assert target_idx != -1, "Target line not found"

new_lines = []
for a in articles:
    title = a['title'].replace('"', '\\"')
    filename = a['filename']
    new_lines.append(f'      {{ "{title}" = "contemporary/{filename}" }},\n')

lines[target_idx+1:target_idx+1] = new_lines

with open('zensical.toml', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated zensical.toml successfully from articles list.")
