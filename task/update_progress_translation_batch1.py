# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,450 / 1,500 記事 (96.7% 達成・セクション34完結！残り50記事)',
    '- **進捗状況**: 1,460 / 1,500 記事 (97.3% 達成・最終セクション35進行中！残り40記事)'
)

# 2. Update lines 1542 to 1551
old_block = '''- [ ] `[未着手]` 1451: 日イ翻訳の根本原理：日本語の主語省略とインドネシア語の主語復元の技術 (`docs/translation-stylistics/01-jp-id-translation-core-principles.md`)
- [ ] `[未着手]` 1452: 日本語の「は」と「が」をインドネシア語でどう表現するか（主題提示 vs 焦点化 yang） (`docs/translation-stylistics/02-handling-japanese-wa-and-ga.md`)
- [ ] `[未着手]` 1453: 日本語の抽象名詞（〜性、〜化、〜感）をインドネシア語に変換する技法 (`docs/translation-stylistics/03-abstract-noun-nominalization.md`)
- [ ] `[未着手]` 1454: 日本語の受動態を自然な能動態 meN- に変換する翻訳の定石 (`docs/translation-stylistics/04-passive-to-active-transformation.md`)
- [ ] `[未着手]` 1455: インドネシア語の di- / 語幹受動態を自然な日本語能動文に訳す定石 (`docs/translation-stylistics/05-active-to-passive-transformation.md`)
- [ ] `[未着手]` 1456: 日本語のモダリティ「〜はずだ」「〜わけだ」「〜に違いない」の的確な訳出 (`docs/translation-stylistics/06-modality-translation-hazuda-wake.md`)
- [ ] `[未着手]` 1457: 「〜てくれる」「〜てもらう」の受益表現をめぐる翻訳ストラテジー (`docs/translation-stylistics/07-benefactive-translation-kureru-morau.md`)
- [ ] `[未着手]` 1458: 日本語の使役「〜させる」と接尾辞 -kan のニュアンス適合性 (`docs/translation-stylistics/08-causative-translation-saseru.md`)
- [ ] `[未着手]` 1459: 無生物主語構文の処理法：英語・インドネシア語と日本語の構造転換 (`docs/translation-stylistics/09-inanimate-subject-translation.md`)
- [ ] `[未着手]` 1460: オノマトペ（擬音語・擬態語）の翻訳：生き生きとした描写をどう移すか (`docs/translation-stylistics/10-mimetic-words-translation.md`)'''

new_block = '''- [x] `[完了]` 1451: 日イ翻訳の根本原理：日本語の主語省略とインドネシア語の主語復元の技術 (`docs/translation-stylistics/01-jp-id-translation-core-principles.md`)
- [x] `[完了]` 1452: 日本語の「は」と「が」をインドネシア語でどう表現するか（主題提示 vs 焦点化 yang） (`docs/translation-stylistics/02-handling-japanese-wa-and-ga.md`)
- [x] `[完了]` 1453: 日本語の抽象名詞（〜性、〜化、〜感）をインドネシア語に変換する技法 (`docs/translation-stylistics/03-abstract-noun-nominalization.md`)
- [x] `[完了]` 1454: 日本語の受動態を自然な能動態 meN- に変換する翻訳の定石 (`docs/translation-stylistics/04-passive-to-active-transformation.md`)
- [x] `[完了]` 1455: インドネシア語の di- / 語幹受動態を自然な日本語能動文に訳す定石 (`docs/translation-stylistics/05-active-to-passive-transformation.md`)
- [x] `[完了]` 1456: 日本語のモダリティ「〜はずだ」「〜わけだ」「〜に違いない」の的確な訳出 (`docs/translation-stylistics/06-modality-translation-hazuda-wake.md`)
- [x] `[完了]` 1457: 「〜てくれる」「〜てもらう」の受益表現をめぐる翻訳ストラテジー (`docs/translation-stylistics/07-benefactive-translation-kureru-morau.md`)
- [x] `[完了]` 1458: 日本語の使役「〜させる」と接尾辞 -kan のニュアンス適合性 (`docs/translation-stylistics/08-causative-translation-saseru.md`)
- [x] `[完了]` 1459: 無生物主語構文の処理法：英語・インドネシア語と日本語の構造転換 (`docs/translation-stylistics/09-inanimate-subject-translation.md`)
- [x] `[完了]` 1460: 日本語のオノマトペ・擬音語擬態語のインドネシア語描写技法 (`docs/translation-stylistics/10-onomatopoeia-translation-techniques.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with translation batch 1")
else:
    print("Old block not found in PROGRESS.md!")
