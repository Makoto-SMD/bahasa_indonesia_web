# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1430. 【実戦模試】UKBI Peringkat Unggul 模擬問題 第2回" = "exam-advanced/30-mock-exam-ukbi-unggul-02.md" },\n'

new_entries = '''      { "1430. 【実戦模試】UKBI Peringkat Unggul 模擬問題 第2回" = "exam-advanced/30-mock-exam-ukbi-unggul-02.md" },
      { "1431. 【難問空所補充】接辞・前置詞・接続詞精密補充 Vol. 1" = "exam-advanced/31-cloze-test-grammar-advanced-01.md" },
      { "1432. 【難問空所補充】接辞・前置詞・接続詞精密補充 Vol. 2" = "exam-advanced/32-cloze-test-grammar-advanced-02.md" },
      { "1433. 【誤文訂正マスター】ハイレベル文法エラー発見特訓 Vol. 1" = "exam-advanced/33-error-identification-mastery-01.md" },
      { "1434. 【誤文訂正マスター】ハイレベル文法エラー発見特訓 Vol. 2" = "exam-advanced/34-error-identification-mastery-02.md" },
      { "1435. 【速読演習】長文斜め読みと設問照合テクニック Vol. 1" = "exam-advanced/35-reading-speed-comprehension-01.md" },
      { "1436. 【速読演習】長文斜め読みと設問照合テクニック Vol. 2" = "exam-advanced/36-reading-speed-comprehension-02.md" },
      { "1437. 検定で狙われる不規則鼻音化・特殊接辞の落とし穴" = "exam-advanced/37-formal-affixation-traps.md" },
      { "1438. 上級試験に登場する文語・古典由来語彙" = "exam-advanced/38-archaic-classical-terms-in-exams.md" },
      { "1439. 検定必須！政治・社会・経済の公式略語・頭字語200選" = "exam-advanced/39-acronyms-abbreviations-mastery.md" },
      { "1440. EYD第5版に基づく句読点の正確な用法" = "exam-advanced/40-punctuation-eyd-mechanics.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added exam-advanced batch 4 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
