# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''      { "L50: 古典パントゥン詩集: 四行詩に宿る群島の知恵と美意識" = "literature/l50-pantun-melayu-klasik-sintesis.md" },
    ] },
    ] },
  ] },
  { "地理・文化探訪" = ['''

new_block = '''      { "L50: 古典パントゥン詩集: 四行詩に宿る群島の知恵と美意識" = "literature/l50-pantun-melayu-klasik-sintesis.md" },
    ] },
    ] },
    { "検定・UKBI直前実戦模試＆徹底解説" = [
      { "1401. 【技能検定B級対策】文法・構造問題の急所" = "exam-advanced/01-inken-b-structure-grammar.md" },
      { "1402. 【技能検定B級対策】類義語・語彙選択テクニック" = "exam-advanced/02-inken-b-vocabulary-synonyms.md" },
      { "1403. 【技能検定B級対策】誤文訂正セクション" = "exam-advanced/03-inken-b-error-correction.md" },
      { "1404. 【技能検定B級対策】長文読解（ビジネス・経済）" = "exam-advanced/04-inken-b-reading-business.md" },
      { "1405. 【技能検定B級対策】日イ翻訳の勘所" = "exam-advanced/05-inken-b-translation-jp-id.md" },
      { "1406. 【技能検定B級対策】イ日翻訳の勘所" = "exam-advanced/06-inken-b-translation-id-jp.md" },
      { "1407. 【技能検定A級対策】超難問構文解析" = "exam-advanced/07-inken-a-complex-syntax.md" },
      { "1408. 【技能検定A級対策】ことわざ・慣用表現50選" = "exam-advanced/08-inken-a-idioms-peribahasa.md" },
      { "1409. 【技能検定A級対策】社説・論説文の超長文読解" = "exam-advanced/09-inken-a-editorial-reading.md" },
      { "1410. 【技能検定A級対策】自由記述・小論文作成法" = "exam-advanced/10-inken-a-high-level-essay.md" },
    ] },
  ] },
  { "地理・文化探訪" = ['''

if target in text:
    new_text = text.replace(target, new_block, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added exam-advanced batch 1 to zensical.toml")
else:
    print("Target block not found in zensical.toml!")
