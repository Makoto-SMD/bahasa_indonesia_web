# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_idx = -1
for i, line in enumerate(lines):
    if 'derivations/root-ukur.md' in line:
        target_idx = i
        break

assert target_idx != -1, "Target line not found"

# target_idx is line 170 (0-indexed 169)
# target_idx + 1 is '    ] },\n'
insert_idx = target_idx + 2

new_block = [
    '    { "語根別派生語マスター図鑑 第2弾" = [\n',
    '      { "1351. 語根 atur の全派生語図鑑" = "derivations-2/101-root-atur.md" },\n',
    '      { "1352. 語根 hubung の全派生語図鑑" = "derivations-2/102-root-hubung.md" },\n',
    '      { "1353. 語根 susun の全派生語図鑑" = "derivations-2/103-root-susun.md" },\n',
    '      { "1354. 語根 pecah の全派生語図鑑" = "derivations-2/104-root-pecah.md" },\n',
    '      { "1355. 語根 ikat の全派生語図鑑" = "derivations-2/105-root-ikat.md" },\n',
    '      { "1356. 語根 lepas の全派生語図鑑" = "derivations-2/106-root-lepas.md" },\n',
    '      { "1357. 語根 pasang の全派生語図鑑" = "derivations-2/107-root-pasang.md" },\n',
    '      { "1358. 語根 ganti の全派生語図鑑" = "derivations-2/108-root-ganti.md" },\n',
    '      { "1359. 語根 ubah の全派生語図鑑" = "derivations-2/109-root-ubah.md" },\n',
    '      { "1360. 語根 pindah の全派生語図鑑" = "derivations-2/110-root-pindah.md" },\n',
    '    ] },\n',
]

lines[insert_idx:insert_idx] = new_block

with open('zensical.toml', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated zensical.toml with Section 33 Batch 1 successfully.")
