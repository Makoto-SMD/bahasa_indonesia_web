# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1410. 【技能検定A級対策】自由記述・小論文作成法" = "exam-advanced/10-inken-a-high-level-essay.md" },\n'

new_entries = '''      { "1410. 【技能検定A級対策】自由記述・小論文作成法" = "exam-advanced/10-inken-a-high-level-essay.md" },
      { "1411. 【技能検定特A級対策】国際条約・法律条文の翻訳" = "exam-advanced/11-inken-special-a-legal-treaty.md" },
      { "1412. 【技能検定特A級対策】通訳・即時要約の技術" = "exam-advanced/12-inken-special-a-simultaneous.md" },
      { "1413. 【UKBI能力評価試験】試験構成とスコア戦略" = "exam-advanced/13-ukbi-overview-scoring-bands.md" },
      { "1414. 【UKBI第1セクション】日常会話リスニング攻略" = "exam-advanced/14-ukbi-seksi-1-listening-social.md" },
      { "1415. 【UKBI第1セクション】学術講義リスニング攻略" = "exam-advanced/15-ukbi-seksi-1-listening-academic.md" },
      { "1416. 【UKBI第2セクション】文法・EYD第5版正書法" = "exam-advanced/16-ukbi-seksi-2-grammar-mechanics.md" },
      { "1417. 【UKBI第2セクション】接辞・造語法判定トレーニング" = "exam-advanced/17-ukbi-seksi-2-word-formation.md" },
      { "1418. 【UKBI第3セクション】図表・インフォグラフィックス読解" = "exam-advanced/18-ukbi-seksi-3-reading-charts-tables.md" },
      { "1419. 【UKBI第3セクション】自然科学・学術論文読解" = "exam-advanced/19-ukbi-seksi-3-reading-scientific.md" },
      { "1420. 【UKBI第3セクション】現代文学・エッセイ行間読解" = "exam-advanced/20-ukbi-seksi-3-reading-literature.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added exam-advanced batch 2 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
