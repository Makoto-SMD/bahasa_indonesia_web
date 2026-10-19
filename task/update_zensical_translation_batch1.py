# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''      { "1450. 【総括】全形式統合型究極の実戦模試" = "exam-advanced/50-comprehensive-grand-mock-exam.md" },
    ] },
  ] },
'''

new_entries = '''      { "1450. 【総括】全形式統合型究極の実戦模試" = "exam-advanced/50-comprehensive-grand-mock-exam.md" },
    ] },
    { "プロの翻訳・通訳・高度表現テクニック" = [
      { "1451. 【翻訳技法】主語省略と主語復元の技術" = "translation-stylistics/01-jp-id-translation-core-principles.md" },
      { "1452. 【翻訳技法】「は」と「が」の処理（主題 vs 焦点）" = "translation-stylistics/02-handling-japanese-wa-and-ga.md" },
      { "1453. 【翻訳技法】抽象名詞（〜性・〜化・〜感）の変換" = "translation-stylistics/03-abstract-noun-nominalization.md" },
      { "1454. 【翻訳技法】日本語受動態から自然な能動態への転換" = "translation-stylistics/04-passive-to-active-transformation.md" },
      { "1455. 【翻訳技法】被動構文から自然な日本語能動文への転換" = "translation-stylistics/05-active-to-passive-transformation.md" },
      { "1456. 【翻訳技法】モダリティ（はず・わけ・違い）の訳出" = "translation-stylistics/06-modality-translation-hazuda-wake.md" },
      { "1457. 【翻訳技法】「〜てくれる・もらう」受益表現の戦略" = "translation-stylistics/07-benefactive-translation-kureru-morau.md" },
      { "1458. 【翻訳技法】使役「〜させる」と接辞-kanのニュアンス" = "translation-stylistics/08-causative-translation-saseru.md" },
      { "1459. 【翻訳技法】無生物主語構文の主客転換と因果再構成" = "translation-stylistics/09-inanimate-subject-translation.md" },
      { "1460. 【翻訳技法】日本語オノマトペのインドネシア語描写" = "translation-stylistics/10-onomatopoeia-translation-techniques.md" },
    ] },
  ] },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added translation-stylistics batch 1 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
