# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,440 / 1,500 記事 (96.0% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,450 / 1,500 記事 (96.7% 達成・セクション34完結！残り50記事)'
)

# 2. Update lines 1530 to 1539
old_block = '''- [ ] `[未着手]` 1441: 【翻訳演習】公式ビジネスレター・案内状の日イ相互翻訳 (`docs/exam-advanced/41-translation-clinic-business-letters.md`)
- [ ] `[未着手]` 1442: 【翻訳演習】中央銀行レポート・経済白書の日イ相互翻訳 (`docs/exam-advanced/42-translation-clinic-economic-reports.md`)
- [ ] `[未着手]` 1443: 【翻訳演習】法務通知・コンプライアンス規程の日イ相互翻訳 (`docs/exam-advanced/43-translation-clinic-legal-notices.md`)
- [ ] `[未着手]` 1444: リスニング試験で引っかかりやすい同音異義語・似た発音の対策 (`docs/exam-advanced/44-listening-comprehension-traps.md`)
- [ ] `[未着手]` 1445: 面接・スピーキング試験で沈黙を作らず高得点を獲得するテクニック (`docs/exam-advanced/45-interview-speaking-strategies.md`)
- [ ] `[未着手]` 1446: 検定本番で時間が足りなくなる人のための時間配分ストラテジー (`docs/exam-advanced/46-exam-time-management-skills.md`)
- [ ] `[未着手]` 1447: 試験当日のメンタルコントロールと直前1時間の最終チェックリスト (`docs/exam-advanced/47-psychological-prep-exam-day.md`)
- [ ] `[未着手]` 1448: 最高峰 UKBI Istimewa（特等）を目指すための超絶技巧研究 (`docs/exam-advanced/48-ukbi-istimewa-masterclass.md`)
- [ ] `[未着手]` 1449: 技能検定 特A級合格者の学習法とノート作成術の徹底分析 (`docs/exam-advanced/49-inken-special-a-hall-of-fame.md`)
- [ ] `[未着手]` 1450: グランドフィナーレ：全形式統合型インドネシア語究極の実戦模試 (`docs/exam-advanced/50-comprehensive-grand-mock-exam.md`)'''

new_block = '''- [x] `[完了]` 1441: 【翻訳演習】公式ビジネスレター・案内状の日イ相互翻訳 (`docs/exam-advanced/41-translation-clinic-business-letters.md`)
- [x] `[完了]` 1442: 【翻訳演習】中央銀行レポート・経済白書の日イ相互翻訳 (`docs/exam-advanced/42-translation-clinic-economic-reports.md`)
- [x] `[完了]` 1443: 【翻訳演習】法務通知・コンプライアンス規程の日イ相互翻訳 (`docs/exam-advanced/43-translation-clinic-legal-notices.md`)
- [x] `[完了]` 1444: リスニング試験で引っかかりやすい同音異義語・似た発音の対策 (`docs/exam-advanced/44-listening-comprehension-traps.md`)
- [x] `[完了]` 1445: 面接・スピーキング試験で沈黙を作らず高得点を獲得するテクニック (`docs/exam-advanced/45-interview-speaking-strategies.md`)
- [x] `[完了]` 1446: 検定本番で時間が足りなくなる人のための時間配分ストラテジー (`docs/exam-advanced/46-exam-time-management-skills.md`)
- [x] `[完了]` 1447: 試験当日のメンタルコントロールと直前1時間の最終チェックリスト (`docs/exam-advanced/47-psychological-prep-exam-day.md`)
- [x] `[完了]` 1448: 最高峰 UKBI Istimewa（特等）を目指すための超絶技巧研究 (`docs/exam-advanced/48-ukbi-istimewa-masterclass.md`)
- [x] `[完了]` 1449: 技能検定 特A級合格者の学習法とノート作成術の徹底分析 (`docs/exam-advanced/49-inken-special-a-hall-of-fame.md`)
- [x] `[完了]` 1450: グランドフィナーレ：全形式統合型インドネシア語究極の実戦模試 (`docs/exam-advanced/50-comprehensive-grand-mock-exam.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with exam batch 5")
else:
    print("Old block not found in PROGRESS.md!")
