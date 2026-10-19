# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1460. 【翻訳技法】日本語オノマトペのインドネシア語描写" = "translation-stylistics/10-onomatopoeia-translation-techniques.md" },\n'

new_entries = '''      { "1460. 【翻訳技法】日本語オノマトペのインドネシア語描写" = "translation-stylistics/10-onomatopoeia-translation-techniques.md" },
      { "1461. 【実務翻訳】ビジネスメール翻訳の定型パターン" = "translation-stylistics/11-business-email-translation-templates.md" },
      { "1462. 【契約書翻訳】契約書翻訳の基本構造と前文定型句" = "translation-stylistics/12-contract-translation-whereas-clause.md" },
      { "1463. 【契約書翻訳】秘密保持契約（NDA）の条文対訳" = "translation-stylistics/13-contract-translation-confidentiality.md" },
      { "1464. 【契約書翻訳】雇用契約書・就業規則と労働法規" = "translation-stylistics/14-contract-translation-employment.md" },
      { "1465. 【契約書翻訳】売買基本契約・販売代理店契約" = "translation-stylistics/15-contract-translation-sales-agency.md" },
      { "1466. 【法務翻訳】法務意見書（Legal Opinion）の翻訳" = "translation-stylistics/16-legal-memorandum-translation.md" },
      { "1467. 【財務翻訳】財務諸表（貸借・損益）の用語対訳" = "translation-stylistics/17-financial-statement-translation.md" },
      { "1468. 【IR翻訳】決算説明会資料・アニュアルレポート" = "translation-stylistics/18-investor-relations-ir-translation.md" },
      { "1469. 【M&A翻訳】デューデリジェンス報告書のリスク評価" = "translation-stylistics/19-m-and-a-due-diligence-translation.md" },
      { "1470. 【マーケティング翻訳】広告のトランスクリエーション" = "translation-stylistics/20-marketing-copywriting-transcreation.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added translation-stylistics batch 2 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
