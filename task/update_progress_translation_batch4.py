# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,480 / 1,500 記事 (98.7% 達成・最終セクション35進行中！残り20記事)',
    '- **進捗状況**: 1,490 / 1,500 記事 (99.3% 達成・最終セクション35進行中！残りあと10記事！)'
)

# 2. Update lines 1572 to 1581
old_block = '''- [ ] `[未着手]` 1481: 通訳者のためのアクティブリスニング：文の終わりを待たずに意味を予測する (`docs/translation-stylistics/31-interpreting-active-listening.md`)
- [ ] `[未着手]` 1482: 通訳におけるリフォーミュレーション：直訳の呪縛を解き放つ要約・再構成 (`docs/translation-stylistics/32-interpreting-reformulation-skills.md`)
- [ ] `[未着手]` 1483: 通訳者の短期記憶（リテンション）トレーニング：シャドーイングとリプロダクション (`docs/translation-stylistics/33-interpreting-memory-retention.md`)
- [ ] `[未着手]` 1484: サイトトランスレーション（視訳）訓練法：英文・イ文を頭から瞬時に日本語化する (`docs/translation-stylistics/34-interpreting-sight-translation.md`)
- [ ] `[未着手]` 1485: 通訳現場のトラブル対処法：聞き逃し・専門用語不明時のスマートなリカバリー (`docs/translation-stylistics/35-interpreting-crisis-management.md`)
- [ ] `[未着手]` 1486: ウィスパリング通訳の作法：小声で明瞭に伝える発声と距離感 (`docs/translation-stylistics/36-interpreting-whispering-techniques.md`)
- [ ] `[未着手]` 1487: リモート同時通訳（RSI）の留意点：音響環境・チャット連携・交代ルール (`docs/translation-stylistics/37-interpreting-remote-rsi-mastery.md`)
- [ ] `[未着手]` 1488: タフな価格交渉・紛争解決の場での通訳：中立性と信頼感の演出 (`docs/translation-stylistics/38-interpreting-business-negotiation.md`)
- [ ] `[未着手]` 1489: 工場見学・製造現場での通訳：騒音対策・安全配慮と専門工具・工程用語 (`docs/translation-stylistics/39-interpreting-factory-site-visit.md`)
- [ ] `[未着手]` 1490: 医療通訳・患者アテンド：問診票・インフォームドコンセントと心理的ケア (`docs/translation-stylistics/40-interpreting-medical-escort.md`)'''

new_block = '''- [x] `[完了]` 1481: 通訳者のためのアクティブリスニング：文の終わりを待たずに意味を予測する (`docs/translation-stylistics/31-interpreting-active-listening.md`)
- [x] `[完了]` 1482: 通訳におけるリフォーミュレーション：直訳の呪縛を解き放つ要約・再構成 (`docs/translation-stylistics/32-interpreting-reformulation-skills.md`)
- [x] `[完了]` 1483: 通訳者の短期記憶（リテンション）トレーニング：シャドーイングとリプロダクション (`docs/translation-stylistics/33-interpreting-memory-retention.md`)
- [x] `[完了]` 1484: サイトトランスレーション（視訳）訓練法：英文・イ文を頭から瞬時に日本語化する (`docs/translation-stylistics/34-interpreting-sight-translation.md`)
- [x] `[完了]` 1485: 通訳現場のトラブル対処法：聞き逃し・専門用語不明時のスマートなリカバリー (`docs/translation-stylistics/35-interpreting-crisis-management.md`)
- [x] `[完了]` 1486: ウィスパリング通訳の作法：小声で明瞭に伝える発声と距離感 (`docs/translation-stylistics/36-interpreting-whispering-techniques.md`)
- [x] `[完了]` 1487: リモート同時通訳（RSI）の留意点：音響環境・チャット連携・交代ルール (`docs/translation-stylistics/37-interpreting-remote-rsi-mastery.md`)
- [x] `[完了]` 1488: タフな価格交渉・紛争解決の場での通訳：中立性と信頼感の演出 (`docs/translation-stylistics/38-interpreting-business-negotiation.md`)
- [x] `[完了]` 1489: 工場見学・製造現場での通訳：騒音対策・安全配慮と専門工具・工程用語 (`docs/translation-stylistics/39-interpreting-factory-site-visit.md`)
- [x] `[完了]` 1490: 医療通訳・患者アテンド：問診票・インフォームドコンセントと心理的ケア (`docs/translation-stylistics/40-interpreting-medical-escort.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with translation batch 4")
else:
    print("Old block not found in PROGRESS.md!")
