# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,400 / 1,500 記事 (93.3% 達成・大台1,400記事達成！)',
    '- **進捗状況**: 1,410 / 1,500 記事 (94.0% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update lines 1490 to 1499
old_block = '''- [ ] `[未着手]` 1401: 【技能検定B級対策】文法・構造問題の急所：接尾辞-kan/-iと周囲辞の識別 (`docs/exam-advanced/01-inken-b-structure-grammar.md`)
- [ ] `[未着手]` 1402: 【技能検定B級対策】類義語・語彙選択：文脈に最適な語彙を見抜くテクニック (`docs/exam-advanced/02-inken-b-vocabulary-synonyms.md`)
- [ ] `[未着手]` 1403: 【技能検定B級対策】誤文訂正セクション：文法的な不整合を即座に発見する法 (`docs/exam-advanced/03-inken-b-error-correction.md`)
- [ ] `[未着手]` 1404: 【技能検定B級対策】長文読解（ビジネス・経済）：パラグラフ要約と設問解法 (`docs/exam-advanced/04-inken-b-reading-business.md`)
- [ ] `[未着手]` 1405: 【技能検定B級対策】日イ翻訳：日本語特有の表現を自然なインドネシア語に移す (`docs/exam-advanced/05-inken-b-translation-jp-id.md`)
- [ ] `[未着手]` 1406: 【技能検定B級対策】イ日翻訳：抽象名詞と受動態を読みやすい日本語に翻訳する (`docs/exam-advanced/06-inken-b-translation-id-jp.md`)
- [ ] `[未着手]` 1407: 【技能検定A級対策】超難問構文解析：複々文・挿入句・倒置構文の骨格把握 (`docs/exam-advanced/07-inken-a-complex-syntax.md`)
- [ ] `[未着手]` 1408: 【技能検定A級対策】ことわざ（Peribahasa）と慣用表現：頻出50選の文脈運用 (`docs/exam-advanced/08-inken-a-idioms-peribahasa.md`)
- [ ] `[未着手]` 1409: 【技能検定A級対策】社説・論説文の超長文読解：筆者の主張と論理の展開 (`docs/exam-advanced/09-inken-a-editorial-reading.md`)
- [ ] `[未着手]` 1410: 【技能検定A級対策】自由記述・エッセイ作成：説得力ある小論文の構成法 (`docs/exam-advanced/10-inken-a-high-level-essay.md`)'''

new_block = '''- [x] `[完了]` 1401: 【技能検定B級対策】文法・構造問題の急所：接尾辞-kan/-iと周囲辞の識別 (`docs/exam-advanced/01-inken-b-structure-grammar.md`)
- [x] `[完了]` 1402: 【技能検定B級対策】類義語・語彙選択：文脈に最適な語彙を見抜くテクニック (`docs/exam-advanced/02-inken-b-vocabulary-synonyms.md`)
- [x] `[完了]` 1403: 【技能検定B級対策】誤文訂正セクション：文法的な不整合を即座に発見する法 (`docs/exam-advanced/03-inken-b-error-correction.md`)
- [x] `[完了]` 1404: 【技能検定B級対策】長文読解（ビジネス・経済）：パラグラフ要約と設問解法 (`docs/exam-advanced/04-inken-b-reading-business.md`)
- [x] `[完了]` 1405: 【技能検定B級対策】日イ翻訳：日本語特有の表現を自然なインドネシア語に移す (`docs/exam-advanced/05-inken-b-translation-jp-id.md`)
- [x] `[完了]` 1406: 【技能検定B級対策】イ日翻訳：抽象名詞と受動態を読みやすい日本語に翻訳する (`docs/exam-advanced/06-inken-b-translation-id-jp.md`)
- [x] `[完了]` 1407: 【技能検定A級対策】超難問構文解析：複々文・挿入句・倒置構文の骨格把握 (`docs/exam-advanced/07-inken-a-complex-syntax.md`)
- [x] `[完了]` 1408: 【技能検定A級対策】ことわざ（Peribahasa）と慣用表現：頻出50選の文脈運用 (`docs/exam-advanced/08-inken-a-idioms-peribahasa.md`)
- [x] `[完了]` 1409: 【技能検定A級対策】社説・論説文の超長文読解：筆者の主張と論理の展開 (`docs/exam-advanced/09-inken-a-editorial-reading.md`)
- [x] `[完了]` 1410: 【技能検定A級対策】自由記述・エッセイ作成：説得力ある小論文の構成法 (`docs/exam-advanced/10-inken-a-high-level-essay.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with exam batch 1")
else:
    print("Old block not found in PROGRESS.md!")
