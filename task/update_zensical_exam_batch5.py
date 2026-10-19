# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1440. EYD第5版に基づく句読点の正確な用法" = "exam-advanced/40-punctuation-eyd-mechanics.md" },\n'

new_entries = '''      { "1440. EYD第5版に基づく句読点の正確な用法" = "exam-advanced/40-punctuation-eyd-mechanics.md" },
      { "1441. 【翻訳演習】公式ビジネスレター・案内状" = "exam-advanced/41-translation-clinic-business-letters.md" },
      { "1442. 【翻訳演習】中央銀行レポート・経済白書" = "exam-advanced/42-translation-clinic-economic-reports.md" },
      { "1443. 【翻訳演習】法務通知・コンプライアンス規程" = "exam-advanced/43-translation-clinic-legal-notices.md" },
      { "1444. リスニングで引っかかりやすい同音異義語・似た発音" = "exam-advanced/44-listening-comprehension-traps.md" },
      { "1445. 面接・スピーキングで沈黙を作らず高得点を取る技" = "exam-advanced/45-interview-speaking-strategies.md" },
      { "1446. 検定本番の時間配分ストラテジー" = "exam-advanced/46-exam-time-management-skills.md" },
      { "1447. 当日のメンタル制御と直前1時間チェックリスト" = "exam-advanced/47-psychological-prep-exam-day.md" },
      { "1448. 最高峰 UKBI Istimewa（特等）を目指す超絶技巧" = "exam-advanced/48-ukbi-istimewa-masterclass.md" },
      { "1449. 技能検定 特A級合格者の学習法とノート術" = "exam-advanced/49-inken-special-a-hall-of-fame.md" },
      { "1450. 【総括】全形式統合型究極の実戦模試" = "exam-advanced/50-comprehensive-grand-mock-exam.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added exam-advanced batch 5 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
