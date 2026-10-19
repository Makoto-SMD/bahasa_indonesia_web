# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,420 / 1,500 記事 (94.7% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,430 / 1,500 記事 (95.3% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update lines 1510 to 1519
old_block = '''- [ ] `[未着手]` 1421: 【UKBI第4セクション】記述式（Menulis）：学術論文アブストラクト執筆 (`docs/exam-advanced/21-ukbi-seksi-4-writing-academic.md`)
- [ ] `[未着手]` 1422: 【UKBI第4セクション】記述式（Menulis）：賛否両論の意見論述文 (`docs/exam-advanced/22-ukbi-seksi-4-writing-argument.md`)
- [ ] `[未着手]` 1423: 【UKBI第5セクション】口頭表現（Berbicara）：3分間プレゼンテーション (`docs/exam-advanced/23-ukbi-seksi-5-speaking-presentation.md`)
- [ ] `[未着手]` 1424: 【UKBI第5セクション】口頭表現（Berbicara）：質問への即座の論理的応答 (`docs/exam-advanced/24-ukbi-seksi-5-speaking-rebuttal.md`)
- [ ] `[未着手]` 1425: 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第1回（解答・解説付） (`docs/exam-advanced/25-mock-exam-inken-b-01.md`)
- [ ] `[未着手]` 1426: 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第2回（解答・解説付） (`docs/exam-advanced/26-mock-exam-inken-b-02.md`)
- [ ] `[未着手]` 1427: 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第1回（解答・解説付） (`docs/exam-advanced/27-mock-exam-inken-a-01.md`)
- [ ] `[未着手]` 1428: 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第2回（解答・解説付） (`docs/exam-advanced/28-mock-exam-inken-a-02.md`)
- [ ] `[未着手]` 1429: 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第1回 (`docs/exam-advanced/29-mock-exam-ukbi-unggul-01.md`)
- [ ] `[未着手]` 1430: 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第2回 (`docs/exam-advanced/30-mock-exam-ukbi-unggul-02.md`)'''

new_block = '''- [x] `[完了]` 1421: 【UKBI第4セクション】記述式（Menulis）：学術論文アブストラクト執筆 (`docs/exam-advanced/21-ukbi-seksi-4-writing-academic.md`)
- [x] `[完了]` 1422: 【UKBI第4セクション】記述式（Menulis）：賛否両論の意見論述文 (`docs/exam-advanced/22-ukbi-seksi-4-writing-argument.md`)
- [x] `[完了]` 1423: 【UKBI第5セクション】口頭表現（Berbicara）：3分間プレゼンテーション (`docs/exam-advanced/23-ukbi-seksi-5-speaking-presentation.md`)
- [x] `[完了]` 1424: 【UKBI第5セクション】口頭表現（Berbicara）：質問への即座の論理的応答 (`docs/exam-advanced/24-ukbi-seksi-5-speaking-rebuttal.md`)
- [x] `[完了]` 1425: 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第1回（解答・解説付） (`docs/exam-advanced/25-mock-exam-inken-b-01.md`)
- [x] `[完了]` 1426: 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第2回（解答・解説付） (`docs/exam-advanced/26-mock-exam-inken-b-02.md`)
- [x] `[完了]` 1427: 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第1回（解答・解説付） (`docs/exam-advanced/27-mock-exam-inken-a-01.md`)
- [x] `[完了]` 1428: 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第2回（解答・解説付） (`docs/exam-advanced/28-mock-exam-inken-a-02.md`)
- [x] `[完了]` 1429: 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第1回 (`docs/exam-advanced/29-mock-exam-ukbi-unggul-01.md`)
- [x] `[完了]` 1430: 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第2回 (`docs/exam-advanced/30-mock-exam-ukbi-unggul-02.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with exam batch 3")
else:
    print("Old block not found in PROGRESS.md!")
