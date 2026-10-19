# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1420. 【UKBI第3セクション】現代文学・エッセイ行間読解" = "exam-advanced/20-ukbi-seksi-3-reading-literature.md" },\n'

new_entries = '''      { "1420. 【UKBI第3セクション】現代文学・エッセイ行間読解" = "exam-advanced/20-ukbi-seksi-3-reading-literature.md" },
      { "1421. 【UKBI第4セクション】記述式：学術論文要旨執筆" = "exam-advanced/21-ukbi-seksi-4-writing-academic.md" },
      { "1422. 【UKBI第4セクション】記述式：賛否両論の意見論述文" = "exam-advanced/22-ukbi-seksi-4-writing-argument.md" },
      { "1423. 【UKBI第5セクション】口頭表現：3分間プレゼン" = "exam-advanced/23-ukbi-seksi-5-speaking-presentation.md" },
      { "1424. 【UKBI第5セクション】口頭表現：質問への即座の応答" = "exam-advanced/24-ukbi-seksi-5-speaking-rebuttal.md" },
      { "1425. 【実戦模試】技能検定B級 完全想定問題 第1回" = "exam-advanced/25-mock-exam-inken-b-01.md" },
      { "1426. 【実戦模試】技能検定B級 完全想定問題 第2回" = "exam-advanced/26-mock-exam-inken-b-02.md" },
      { "1427. 【実戦模試】技能検定A級 完全想定問題 第1回" = "exam-advanced/27-mock-exam-inken-a-01.md" },
      { "1428. 【実戦模試】技能検定A級 完全想定問題 第2回" = "exam-advanced/28-mock-exam-inken-a-02.md" },
      { "1429. 【実戦模試】UKBI Peringkat Unggul 模擬問題 第1回" = "exam-advanced/29-mock-exam-ukbi-unggul-01.md" },
      { "1430. 【実戦模試】UKBI Peringkat Unggul 模擬問題 第2回" = "exam-advanced/30-mock-exam-ukbi-unggul-02.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added exam-advanced batch 3 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
