# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1360. 語根 pindah の全派生語図鑑" = "derivations-2/110-root-pindah.md" },\n'

new_entries = '''      { "1360. 語根 pindah の全派生語図鑑" = "derivations-2/110-root-pindah.md" },
      { "1361. 語根 tambah の全派生語図鑑" = "derivations-2/111-root-tambah.md" },
      { "1362. 語根 kurang の全派生語図鑑" = "derivations-2/112-root-kurang.md" },
      { "1363. 語根 bagi の全派生語図鑑" = "derivations-2/113-root-bagi.md" },
      { "1364. 語根 gabung の全派生語図鑑" = "derivations-2/114-root-gabung.md" },
      { "1365. 語根 kumpul の全派生語図鑑" = "derivations-2/115-root-kumpul.md" },
      { "1366. 語根 pisah の全派生語図鑑" = "derivations-2/116-root-pisah.md" },
      { "1367. 語根 tarik の全派生語図鑑" = "derivations-2/117-root-tarik.md" },
      { "1368. 語根 dorong の全派生語図鑑" = "derivations-2/118-root-dorong.md" },
      { "1369. 語根 angkat の全派生語図鑑" = "derivations-2/119-root-angkat.md" },
      { "1370. 語根 turun の全派生語図鑑" = "derivations-2/120-root-turun.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully updated zensical.toml")
else:
    print("Target not found!")
