# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1390. 語根 layan の全派生語図鑑" = "derivations-2/140-root-layan.md" },\n'

new_entries = '''      { "1390. 語根 layan の全派生語図鑑" = "derivations-2/140-root-layan.md" },
      { "1391. 語根 urus の全派生語図鑑" = "derivations-2/141-root-urus.md" },
      { "1392. 語根 kelola の全派生語図鑑" = "derivations-2/142-root-kelola.md" },
      { "1393. 語根 pimpin の全派生語図鑑" = "derivations-2/143-root-pimpin.md" },
      { "1394. 語根 arah の全派生語図鑑" = "derivations-2/144-root-arah.md" },
      { "1395. 語根 bimbing の全派生語図鑑" = "derivations-2/145-root-bimbing.md" },
      { "1396. 語根 didik の全派生語図鑑" = "derivations-2/146-root-didik.md" },
      { "1397. 語根 latih の全派生語図鑑" = "derivations-2/147-root-latih.md" },
      { "1398. 語根 uji の全派生語図鑑" = "derivations-2/148-root-uji.md" },
      { "1399. 語根 nilai の全派生語図鑑" = "derivations-2/149-root-nilai.md" },
      { "1400. 【総括】語根派生語マスター検定 第2弾" = "derivations-2/150-section33-master-exam.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully updated zensical.toml with batch 5")
else:
    print("Target not found in zensical.toml!")
