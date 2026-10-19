# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,430 / 1,500 記事 (95.3% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,440 / 1,500 記事 (96.0% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update lines 1520 to 1529
old_block = '''- [ ] `[未着手]` 1431: 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選（Vol. 1） (`docs/exam-advanced/31-cloze-test-grammar-advanced-01.md`)
- [ ] `[未着手]` 1432: 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選（Vol. 2） (`docs/exam-advanced/32-cloze-test-grammar-advanced-02.md`)
- [ ] `[未着手]` 1433: 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問（Vol. 1） (`docs/exam-advanced/33-error-identification-mastery-01.md`)
- [ ] `[未着手]` 1434: 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問（Vol. 2） (`docs/exam-advanced/34-error-identification-mastery-02.md`)
- [ ] `[未着手]` 1435: 【速読演習】制限時間内での長文斜め読みと設問照合テクニック（Vol. 1） (`docs/exam-advanced/35-reading-speed-comprehension-01.md`)
- [ ] `[未着手]` 1436: 【速読演習】制限時間内での長文斜め読みと設問照合テクニック（Vol. 2） (`docs/exam-advanced/36-reading-speed-comprehension-02.md`)
- [ ] `[未着手]` 1437: 検定で狙われる「不規則鼻音化・特殊接辞」の落とし穴完全網羅 (`docs/exam-advanced/37-formal-affixation-traps.md`)
- [ ] `[未着手]` 1438: 上級試験に登場する文語・古典由来語彙（syahdan, alkisah, bahwasanya） (`docs/exam-advanced/38-archaic-classical-terms-in-exams.md`)
- [ ] `[未着手]` 1439: 検定必須！政治・社会・経済の公式略語・頭字語200選 (`docs/exam-advanced/39-acronyms-abbreviations-mastery.md`)
- [ ] `[未着手]` 1440: EYD第5版に基づく句読点（コンマ、セミコロン、コロン）の正確な用法 (`docs/exam-advanced/40-punctuation-eyd-mechanics.md`)'''

new_block = '''- [x] `[完了]` 1431: 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選（Vol. 1） (`docs/exam-advanced/31-cloze-test-grammar-advanced-01.md`)
- [x] `[完了]` 1432: 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選（Vol. 2） (`docs/exam-advanced/32-cloze-test-grammar-advanced-02.md`)
- [x] `[完了]` 1433: 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問（Vol. 1） (`docs/exam-advanced/33-error-identification-mastery-01.md`)
- [x] `[完了]` 1434: 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問（Vol. 2） (`docs/exam-advanced/34-error-identification-mastery-02.md`)
- [x] `[完了]` 1435: 【速読演習】制限時間内での長文斜め読みと設問照合テクニック（Vol. 1） (`docs/exam-advanced/35-reading-speed-comprehension-01.md`)
- [x] `[完了]` 1436: 【速読演習】制限時間内での長文斜め読みと設問照合テクニック（Vol. 2） (`docs/exam-advanced/36-reading-speed-comprehension-02.md`)
- [x] `[完了]` 1437: 検定で狙われる「不規則鼻音化・特殊接辞」の落とし穴完全網羅 (`docs/exam-advanced/37-formal-affixation-traps.md`)
- [x] `[完了]` 1438: 上級試験に登場する文語・古典由来語彙（syahdan, alkisah, bahwasanya） (`docs/exam-advanced/38-archaic-classical-terms-in-exams.md`)
- [x] `[完了]` 1439: 検定必須！政治・社会・経済の公式略語・頭字語200選 (`docs/exam-advanced/39-acronyms-abbreviations-mastery.md`)
- [x] `[完了]` 1440: EYD第5版に基づく句読点（コンマ、セミコロン、コロン）の正確な用法 (`docs/exam-advanced/40-punctuation-eyd-mechanics.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with exam batch 4")
else:
    print("Old block not found in PROGRESS.md!")
