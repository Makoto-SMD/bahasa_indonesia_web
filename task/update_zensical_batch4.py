# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1380. 語根 hindar の全派生語図鑑" = "derivations-2/130-root-hindar.md" },\n'

new_entries = '''      { "1380. 語根 hindar の全派生語図鑑" = "derivations-2/130-root-hindar.md" },
      { "1381. 語根 cegah の全派生語図鑑" = "derivations-2/131-root-cegah.md" },
      { "1382. 語根 lindung の全派生語図鑑" = "derivations-2/132-root-lindung.md" },
      { "1383. 語根 bela の全派生語図鑑" = "derivations-2/133-root-bela.md" },
      { "1384. 語根 tuntut の全派生語図鑑" = "derivations-2/134-root-tuntut.md" },
      { "1385. 語根 gugat の全派生語図鑑" = "derivations-2/135-root-gugat.md" },
      { "1386. 語根 tolak の全派生語図鑑" = "derivations-2/136-root-tolak.md" },
      { "1387. 語根 terima の全派生語図鑑" = "derivations-2/137-root-terima.md" },
      { "1388. 語根 tolong の全派生語図鑑" = "derivations-2/138-root-tolong.md" },
      { "1389. 語根 bantu の全派生語図鑑" = "derivations-2/139-root-bantu.md" },
      { "1390. 語根 layan の全派生語図鑑" = "derivations-2/140-root-layan.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully updated zensical.toml with batch 4")
else:
    print("Target not found in zensical.toml!")
