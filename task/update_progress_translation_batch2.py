# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,460 / 1,500 記事 (97.3% 達成・最終セクション35進行中！残り40記事)',
    '- **進捗状況**: 1,470 / 1,500 記事 (98.0% 達成・最終セクション35進行中！残り30記事)'
)

# 2. Update lines 1552 to 1561
old_block = '''- [ ] `[未着手]` 1461: 日イビジネスメール翻訳の定型パターンと敬語表現の等価性 (`docs/translation-stylistics/11-business-email-translation-templates.md`)
- [ ] `[未着手]` 1462: 契約書翻訳の基本構造：頭書・前文（Whereas条項）・合意条項の定型表現 (`docs/translation-stylistics/12-contract-translation-whereas-clause.md`)
- [ ] `[未着手]` 1463: 【契約書翻訳】秘密保持契約（NDA）の条文対訳と専門用語解説 (`docs/translation-stylistics/13-contract-translation-confidentiality.md`)
- [ ] `[未着手]` 1464: 【契約書翻訳】雇用契約書・就業規則の条文対訳と労働法規語彙 (`docs/translation-stylistics/14-contract-translation-employment.md`)
- [ ] `[未着手]` 1465: 【契約書翻訳】売買基本契約・販売代理店契約の条文対訳 (`docs/translation-stylistics/15-contract-translation-sales-agency.md`)
- [ ] `[未着手]` 1466: 法務意見書（Legal Opinion）の翻訳：論理展開と格調の維持 (`docs/translation-stylistics/16-legal-memorandum-translation.md`)
- [ ] `[未着手]` 1467: 財務諸表（貸借対照表・損益計算書）の用語対訳と注記の翻訳 (`docs/translation-stylistics/17-financial-statement-translation.md`)
- [ ] `[未着手]` 1468: 決算説明会資料・アニュアルレポートの翻訳：投資家向け洗練表現 (`docs/translation-stylistics/18-investor-relations-ir-translation.md`)
- [ ] `[未着手]` 1469: M&Aデューデリジェンス報告書の翻訳：リスク評価と企業価値算定 (`docs/translation-stylistics/19-m-and-a-due-diligence-translation.md`)
- [ ] `[未着手]` 1470: 広告・キャッチコピーのトランスクリエーション：心に響く現地化 (`docs/translation-stylistics/20-marketing-copywriting-transcreation.md`)'''

new_block = '''- [x] `[完了]` 1461: 日イビジネスメール翻訳の定型パターンと敬語表現の等価性 (`docs/translation-stylistics/11-business-email-translation-templates.md`)
- [x] `[完了]` 1462: 契約書翻訳の基本構造：頭書・前文（Whereas条項）・合意条項の定型表現 (`docs/translation-stylistics/12-contract-translation-whereas-clause.md`)
- [x] `[完了]` 1463: 【契約書翻訳】秘密保持契約（NDA）の条文対訳と専門用語解説 (`docs/translation-stylistics/13-contract-translation-confidentiality.md`)
- [x] `[完了]` 1464: 【契約書翻訳】雇用契約書・就業規則の条文対訳と労働法規語彙 (`docs/translation-stylistics/14-contract-translation-employment.md`)
- [x] `[完了]` 1465: 【契約書翻訳】売買基本契約・販売代理店契約の条文対訳 (`docs/translation-stylistics/15-contract-translation-sales-agency.md`)
- [x] `[完了]` 1466: 法務意見書（Legal Opinion）の翻訳：論理展開と格調の維持 (`docs/translation-stylistics/16-legal-memorandum-translation.md`)
- [x] `[完了]` 1467: 財務諸表（貸借対照表・損益計算書）の用語対訳と注記の翻訳 (`docs/translation-stylistics/17-financial-statement-translation.md`)
- [x] `[完了]` 1468: 決算説明会資料・アニュアルレポートの翻訳：投資家向け洗練表現 (`docs/translation-stylistics/18-investor-relations-ir-translation.md`)
- [x] `[完了]` 1469: M&Aデューデリジェンス報告書の翻訳：リスク評価と企業価値算定 (`docs/translation-stylistics/19-m-and-a-due-diligence-translation.md`)
- [x] `[完了]` 1470: 広告・キャッチコピーのトランスクリエーション：心に響く現地化 (`docs/translation-stylistics/20-marketing-copywriting-transcreation.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with translation batch 2")
else:
    print("Old block not found in PROGRESS.md!")
