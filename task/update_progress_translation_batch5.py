# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,490 / 1,500 記事 (99.3% 達成・最終セクション35進行中！残りあと10記事！)',
    '- **進捗状況**: 1,500 / 1,500 記事 (100.0% 達成！全35セクション完全完結・偉業達成！)'
)

# 2. Update lines 1582 to 1591
old_block = '''- [ ] `[未着手]` 1491: 高度文体論：公式報告書・論文における端正な学術的文体の構築 (`docs/translation-stylistics/41-stylistics-formal-academic-register.md`)
- [ ] `[未着手]` 1492: 高度文体論：説得力と扇情性を高める修辞的レトリック（反復・対句・誇張） (`docs/translation-stylistics/42-stylistics-persuasive-rhetoric.md`)
- [ ] `[未着手]` 1493: 高度文体論：アイロニーと風刺の解読と産出：行間に潜むユーモアのニュアンス (`docs/translation-stylistics/43-stylistics-irony-satire-humor.md`)
- [ ] `[未着手]` 1494: 高度文体論：婉曲表現（Eufemisme）の美学：死・病・金銭・失敗を品良く語る (`docs/translation-stylistics/44-stylistics-euphemism-taboo.md`)
- [ ] `[未着手]` 1495: 高度文体論：古風・宮廷風文体の活用：格調ある歴史的重みの付与 (`docs/translation-stylistics/45-stylistics-archaisms-court-style.md`)
- [ ] `[未着手]` 1496: AI翻訳（DeepL/ChatGPT）時代におけるポストエディット（MTPE）の実践 (`docs/translation-stylistics/46-ai-translation-post-editing-mtpe.md`)
- [ ] `[未着手]` 1497: プロの翻訳チェック・校正（QA）手順：用語集統一・数字検証・文体一致 (`docs/translation-stylistics/47-translation-quality-assurance-qa.md`)
- [ ] `[未着手]` 1498: 通訳・翻訳者のための個人用語集（Termbase）構築とCATツール活用 (`docs/translation-stylistics/48-building-personal-termbase-glossary.md`)
- [ ] `[未着手]` 1499: 通訳者・翻訳者の職業倫理規定：守秘義務・利益相反・専門的誠実さ (`docs/translation-stylistics/49-professional-code-of-ethics-interpreter.md`)
- [ ] `[未着手]` 1500: 名訳・誤訳から学ぶ最高峰の翻訳批評：プロフェッショナルの境界線 (`docs/translation-stylistics/50-masterclass-translation-critique.md`)'''

new_block = '''- [x] `[完了]` 1491: 高度文体論：公式報告書・論文における端正な学術的文体の構築 (`docs/translation-stylistics/41-stylistics-formal-academic-register.md`)
- [x] `[完了]` 1492: 高度文体論：説得力と扇情性を高める修辞的レトリック（反復・対句・誇張） (`docs/translation-stylistics/42-stylistics-persuasive-rhetoric.md`)
- [x] `[完了]` 1493: 高度文体論：アイロニーと風刺の解読と産出：行間に潜むユーモアのニュアンス (`docs/translation-stylistics/43-stylistics-irony-satire-humor.md`)
- [x] `[完了]` 1494: 高度文体論：婉曲表現（Eufemisme）の美学：死・病・金銭・失敗を品良く語る (`docs/translation-stylistics/44-stylistics-euphemism-taboo.md`)
- [x] `[完了]` 1495: 高度文体論：古風・宮廷風文体の活用：格調ある歴史的重みの付与 (`docs/translation-stylistics/45-stylistics-archaisms-court-style.md`)
- [x] `[完了]` 1496: AI翻訳（DeepL/ChatGPT）時代におけるポストエディット（MTPE）の実践 (`docs/translation-stylistics/46-ai-translation-post-editing-mtpe.md`)
- [x] `[完了]` 1497: プロの翻訳チェック・校正（QA）手順：用語集統一・数字検証・文体一致 (`docs/translation-stylistics/47-translation-quality-assurance-qa.md`)
- [x] `[完了]` 1498: 通訳・翻訳者のための個人用語集（Termbase）構築とCATツール活用 (`docs/translation-stylistics/48-building-personal-termbase-glossary.md`)
- [x] `[完了]` 1499: 通訳者・翻訳者の職業倫理規定：守秘義務・利益相反・専門的誠実さ (`docs/translation-stylistics/49-professional-code-of-ethics-interpreter.md`)
- [x] `[完了]` 1500: 名訳・誤訳から学ぶ最高峰の翻訳批評：プロフェッショナルの境界線 (`docs/translation-stylistics/50-masterclass-translation-critique.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with translation batch 5 - ALL 1500 ARTICLES COMPLETED!")
else:
    print("Old block not found in PROGRESS.md!")
