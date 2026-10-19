# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1490. 【通訳技術】医療通訳・問診票とインフォームドコンセント" = "translation-stylistics/40-interpreting-medical-escort.md" },\n'

new_entries = '''      { "1490. 【通訳技術】医療通訳・問診票とインフォームドコンセント" = "translation-stylistics/40-interpreting-medical-escort.md" },
      { "1491. 【高度文体論】公式報告書・論文における端正な文体" = "translation-stylistics/41-stylistics-formal-academic-register.md" },
      { "1492. 【高度文体論】説得力と扇情性を高める修辞レトリック" = "translation-stylistics/42-stylistics-persuasive-rhetoric.md" },
      { "1493. 【高度文体論】アイロニーと風刺の解読とユーモア" = "translation-stylistics/43-stylistics-irony-satire-humor.md" },
      { "1494. 【高度文体論】婉曲表現（Eufemisme）の美学" = "translation-stylistics/44-stylistics-euphemism-taboo.md" },
      { "1495. 【高度文体論】古風・宮廷風文体による歴史的重み" = "translation-stylistics/45-stylistics-archaisms-court-style.md" },
      { "1496. 【AI翻訳時代】機械翻訳ポストエディット（MTPE）" = "translation-stylistics/46-ai-translation-post-editing-mtpe.md" },
      { "1497. 【品質保証】プロの翻訳チェック・校正（QA）手順" = "translation-stylistics/47-translation-quality-assurance-qa.md" },
      { "1498. 【知財管理】個人用語集（Termbase）とCATツール" = "translation-stylistics/48-building-personal-termbase-glossary.md" },
      { "1499. 【職業倫理】通訳者・翻訳者の国際職業倫理規定" = "translation-stylistics/49-professional-code-of-ethics-interpreter.md" },
      { "1500. 【大団円】最高峰の翻訳批評：プロの境界線" = "translation-stylistics/50-masterclass-translation-critique.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added translation-stylistics batch 5 (ALL 1500 ARTICLES!) to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
