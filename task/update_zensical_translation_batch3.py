# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

target = '      { "1470. 【マーケティング翻訳】広告のトランスクリエーション" = "translation-stylistics/20-marketing-copywriting-transcreation.md" },\n'

new_entries = '''      { "1470. 【マーケティング翻訳】広告のトランスクリエーション" = "translation-stylistics/20-marketing-copywriting-transcreation.md" },
      { "1471. 【産業翻訳】機械操作マニュアル・安全衛生規程" = "translation-stylistics/21-technical-manual-translation-safety.md" },
      { "1472. 【IT翻訳】ソフトウェア・UI文字列のローカライズ" = "translation-stylistics/22-it-localization-ui-strings.md" },
      { "1473. 【メディカル翻訳】治験プロトコル・医薬品添付文書" = "translation-stylistics/23-medical-pharmaceutical-translation.md" },
      { "1474. 【特許翻訳】特許明細書・請求の範囲（Claims）" = "translation-stylistics/24-patent-specification-translation.md" },
      { "1475. 【外交翻訳】首脳会談・国際会議スピーチの翻訳" = "translation-stylistics/25-diplomatic-speech-translation.md" },
      { "1476. 【文学翻訳】登場人物の階層・人柄を表現するセリフ" = "translation-stylistics/26-literary-translation-dialogue-style.md" },
      { "1477. 【文化翻訳】比喩・文化的暗号の翻訳と現地化" = "translation-stylistics/27-literary-translation-metaphor-culture.md" },
      { "1478. 【報道翻訳】時事ニュース・見出しの切れ味とスピード" = "translation-stylistics/28-news-journalism-translation-tempo.md" },
      { "1479. 【学術翻訳】学術論文アブストラクトの格調高き論述体" = "translation-stylistics/29-academic-paper-abstract-translation.md" },
      { "1480. 【通訳技術】逐次通訳のノートテイキング技術" = "translation-stylistics/30-interpreting-note-taking-technique.md" },
'''

if target in text:
    new_text = text.replace(target, new_entries, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully added translation-stylistics batch 3 to zensical.toml")
else:
    print("Target line not found in zensical.toml!")
