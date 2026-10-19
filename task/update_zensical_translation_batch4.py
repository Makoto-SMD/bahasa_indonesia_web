# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1480. 【通訳技術】逐次通訳のノートテイキング技術" = "translation-stylistics/30-interpreting-note-taking-technique.md" },\n'

new_entries = '''      { "1480. 【通訳技術】逐次通訳のノートテイキング技術" = "translation-stylistics/30-interpreting-note-taking-technique.md" },
      { "1481. 【通訳技術】アクティブリスニングと意味の先回り予測" = "translation-stylistics/31-interpreting-active-listening.md" },
      { "1482. 【通訳技術】リフォーミュレーション：直訳打破の再構成" = "translation-stylistics/32-interpreting-reformulation-skills.md" },
      { "1483. 【通訳技術】短期記憶（リテンション）トレーニング" = "translation-stylistics/33-interpreting-memory-retention.md" },
      { "1484. 【通訳技術】サイトトランスレーション（視訳）訓練法" = "translation-stylistics/34-interpreting-sight-translation.md" },
      { "1485. 【通訳技術】通訳現場のトラブル対処とスマートリカバリー" = "translation-stylistics/35-interpreting-crisis-management.md" },
      { "1486. 【通訳技術】ウィスパリング通訳の作法と発声" = "translation-stylistics/36-interpreting-whispering-techniques.md" },
      { "1487. 【通訳技術】リモート同時通訳（RSI）の留意点" = "translation-stylistics/37-interpreting-remote-rsi-mastery.md" },
      { "1488. 【通訳技術】タフな価格交渉・紛争解決の場での通訳" = "translation-stylistics/38-interpreting-business-negotiation.md" },
      { "1489. 【通訳技術】工場見学・製造現場での通訳と安全配慮" = "translation-stylistics/39-interpreting-factory-site-visit.md" },
      { "1490. 【通訳技術】医療通訳・問診票とインフォームドコンセント" = "translation-stylistics/40-interpreting-medical-escort.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added translation-stylistics batch 4 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
