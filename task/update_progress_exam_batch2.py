# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,410 / 1,500 記事 (94.0% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,420 / 1,500 記事 (94.7% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update lines 1500 to 1509
old_block = '''- [ ] `[未着手]` 1411: 【技能検定特A級対策】国際条約・法律条文の翻訳：格調高き定型表現の処理 (`docs/exam-advanced/11-inken-special-a-legal-treaty.md`)
- [ ] `[未着手]` 1412: 【技能検定特A級対策】通訳・即時要約の技術：情報の取捨選択と瞬発力 (`docs/exam-advanced/12-inken-special-a-simultaneous.md`)
- [ ] `[未着手]` 1413: 【UKBI能力評価試験】試験構成・評価基準（Peringkat）とスコアアップ戦略 (`docs/exam-advanced/13-ukbi-overview-scoring-bands.md`)
- [ ] `[未着手]` 1414: 【UKBI第1セクション】リスニング攻略：日常会話・インタビューの聞き取り (`docs/exam-advanced/14-ukbi-seksi-1-listening-social.md`)
- [ ] `[未着手]` 1415: 【UKBI第1セクション】リスニング攻略：学術講義・公式スピーチの論理把握 (`docs/exam-advanced/15-ukbi-seksi-1-listening-academic.md`)
- [ ] `[未着手]` 1416: 【UKBI第2セクション】文法・正書法（EYD第5版）完全対応ドリル (`docs/exam-advanced/16-ukbi-seksi-2-grammar-mechanics.md`)
- [ ] `[未着手]` 1417: 【UKBI第2セクション】接辞・造語法・派生語の正誤判定トレーニング (`docs/exam-advanced/17-ukbi-seksi-2-word-formation.md`)
- [ ] `[未着手]` 1418: 【UKBI第3セクション】図表・インフォグラフィックス読み取り読解法 (`docs/exam-advanced/18-ukbi-seksi-3-reading-charts-tables.md`)
- [ ] `[未着手]` 1419: 【UKBI第3セクション】自然科学・テクノロジー学術論文の読解演習 (`docs/exam-advanced/19-ukbi-seksi-3-reading-scientific.md`)
- [ ] `[未着手]` 1420: 【UKBI第3セクション】現代文学・エッセイの行間を読む高度読解 (`docs/exam-advanced/20-ukbi-seksi-3-reading-literature.md`)'''

new_block = '''- [x] `[完了]` 1411: 【技能検定特A級対策】国際条約・法律条文の翻訳：格調高き定型表現の処理 (`docs/exam-advanced/11-inken-special-a-legal-treaty.md`)
- [x] `[完了]` 1412: 【技能検定特A級対策】通訳・即時要約の技術：情報の取捨選択と瞬発力 (`docs/exam-advanced/12-inken-special-a-simultaneous.md`)
- [x] `[完了]` 1413: 【UKBI能力評価試験】試験構成・評価基準（Peringkat）とスコアアップ戦略 (`docs/exam-advanced/13-ukbi-overview-scoring-bands.md`)
- [x] `[完了]` 1414: 【UKBI第1セクション】リスニング攻略：日常会話・インタビューの聞き取り (`docs/exam-advanced/14-ukbi-seksi-1-listening-social.md`)
- [x] `[完了]` 1415: 【UKBI第1セクション】リスニング攻略：学術講義・公式スピーチの論理把握 (`docs/exam-advanced/15-ukbi-seksi-1-listening-academic.md`)
- [x] `[完了]` 1416: 【UKBI第2セクション】文法・正書法（EYD第5版）完全対応ドリル (`docs/exam-advanced/16-ukbi-seksi-2-grammar-mechanics.md`)
- [x] `[完了]` 1417: 【UKBI第2セクション】接辞・造語法・派生語の正誤判定トレーニング (`docs/exam-advanced/17-ukbi-seksi-2-word-formation.md`)
- [x] `[完了]` 1418: 【UKBI第3セクション】図表・インフォグラフィックス読み取り読解法 (`docs/exam-advanced/18-ukbi-seksi-3-reading-charts-tables.md`)
- [x] `[完了]` 1419: 【UKBI第3セクション】自然科学・テクノロジー学術論文の読解演習 (`docs/exam-advanced/19-ukbi-seksi-3-reading-scientific.md`)
- [x] `[完了]` 1420: 【UKBI第3セクション】現代文学・エッセイの行間を読む高度読解 (`docs/exam-advanced/20-ukbi-seksi-3-reading-literature.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with exam batch 2")
else:
    print("Old block not found in PROGRESS.md!")
