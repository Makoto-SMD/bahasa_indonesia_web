# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,470 / 1,500 記事 (98.0% 達成・最終セクション35進行中！残り30記事)',
    '- **進捗状況**: 1,480 / 1,500 記事 (98.7% 達成・最終セクション35進行中！残り20記事)'
)

# 2. Update lines 1562 to 1571
old_block = '''- [ ] `[未着手]` 1471: 機械操作マニュアル・安全衛生規程の正確かつ明瞭な翻訳 (`docs/translation-stylistics/21-technical-manual-translation-safety.md`)
- [ ] `[未着手]` 1472: ITソフトウェア・UI文字列のローカライズ：文字数制限と直感性 (`docs/translation-stylistics/22-it-localization-ui-strings.md`)
- [ ] `[未着手]` 1473: 治験プロトコル・医薬品添付文書の翻訳：厳密な学術性と安全性 (`docs/translation-stylistics/23-medical-pharmaceutical-translation.md`)
- [ ] `[未着手]` 1474: 特許明細書・請求の範囲（Claims）の翻訳：権利範囲の明確化 (`docs/translation-stylistics/24-patent-specification-translation.md`)
- [ ] `[未着手]` 1475: 首脳会談・国際会議スピーチの翻訳：儀礼的威厳と修辞技法 (`docs/translation-stylistics/25-diplomatic-speech-translation.md`)
- [ ] `[未着手]` 1476: 文学翻訳：登場人物の階層・人柄を表現する文体選択と語末詞 (`docs/translation-stylistics/26-literary-translation-dialogue-style.md`)
- [ ] `[未着手]` 1477: 比喩・文化的暗号の翻訳：注釈をつけずに文脈で溶け込ませる職人技 (`docs/translation-stylistics/27-literary-translation-metaphor-culture.md`)
- [ ] `[未着手]` 1478: 報道・時事ニュースの翻訳：見出しの切れ味と事実伝達のスピード感 (`docs/translation-stylistics/28-news-journalism-translation-tempo.md`)
- [ ] `[未着手]` 1479: 学術論文アブストラクトの翻訳：国際学術水準の格調高き論述体 (`docs/translation-stylistics/29-academic-paper-abstract-translation.md`)
- [ ] `[未着手]` 1480: 逐次通訳のノートテイキング技術：シンボル記号と情報配置の工夫 (`docs/translation-stylistics/30-interpreting-note-taking-technique.md`)'''

new_block = '''- [x] `[完了]` 1471: 機械操作マニュアル・安全衛生規程の正確かつ明瞭な翻訳 (`docs/translation-stylistics/21-technical-manual-translation-safety.md`)
- [x] `[完了]` 1472: ITソフトウェア・UI文字列のローカライズ：文字数制限と直感性 (`docs/translation-stylistics/22-it-localization-ui-strings.md`)
- [x] `[完了]` 1473: 治験プロトコル・医薬品添付文書の翻訳：厳密な学術性と安全性 (`docs/translation-stylistics/23-medical-pharmaceutical-translation.md`)
- [x] `[完了]` 1474: 特許明細書・請求の範囲（Claims）の翻訳：権利範囲の明確化 (`docs/translation-stylistics/24-patent-specification-translation.md`)
- [x] `[完了]` 1475: 首脳会談・国際会議スピーチの翻訳：儀礼的威厳と修辞技法 (`docs/translation-stylistics/25-diplomatic-speech-translation.md`)
- [x] `[完了]` 1476: 文学翻訳：登場人物の階層・人柄を表現する文体選択と語末詞 (`docs/translation-stylistics/26-literary-translation-dialogue-style.md`)
- [x] `[完了]` 1477: 比喩・文化的暗号の翻訳：注釈をつけずに文脈で溶け込ませる職人技 (`docs/translation-stylistics/27-literary-translation-metaphor-culture.md`)
- [x] `[完了]` 1478: 報道・時事ニュースの翻訳：見出しの切れ味と事実伝達のスピード感 (`docs/translation-stylistics/28-news-journalism-translation-tempo.md`)
- [x] `[完了]` 1479: 学術論文アブストラクトの翻訳：国際学術水準の格調高き論述体 (`docs/translation-stylistics/29-academic-paper-abstract-translation.md`)
- [x] `[完了]` 1480: 逐次通訳のノートテイキング技術：シンボル記号と情報配置の工夫 (`docs/translation-stylistics/30-interpreting-note-taking-technique.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with translation batch 3")
else:
    print("Old block not found in PROGRESS.md!")
