# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1370. 語根 turun の全派生語図鑑" = "derivations-2/120-root-turun.md" },\n'

new_entries = '''      { "1370. 語根 turun の全派生語図鑑" = "derivations-2/120-root-turun.md" },
      { "1371. 語根 naik の全派生語図鑑" = "derivations-2/121-root-naik.md" },
      { "1372. 語根 jatuh の全派生語図鑑" = "derivations-2/122-root-jatuh.md" },
      { "1373. 語根 bangkit の全派生語図鑑" = "derivations-2/123-root-bangkit.md" },
      { "1374. 語根 runtuh の全派生語図鑑" = "derivations-2/124-root-runtuh.md" },
      { "1375. 語根 roboh の全派生語図鑑" = "derivations-2/125-root-roboh.md" },
      { "1376. 語根 tumbuh の全派生語図鑑" = "derivations-2/126-root-tumbuh.md" },
      { "1377. 語根 kembang の全派生語図鑑" = "derivations-2/127-root-kembang.md" },
      { "1378. 語根 maju の全派生語図鑑" = "derivations-2/128-root-maju.md" },
      { "1379. 語根 mundur の全派生語図鑑" = "derivations-2/129-root-mundur.md" },
      { "1380. 語根 hindar の全派生語図鑑" = "derivations-2/130-root-hindar.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully updated zensical.toml with batch 3")
else:
    print("Target not found in zensical.toml!")
