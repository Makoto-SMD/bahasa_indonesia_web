# 校正レビュー報告書: TASK-1111 (二重言語 Baku ⇄ Gaul 1111-1120)

## 1. 対象記事
- 1111: `docs/diglossia/11-particle-dong-in-action.md` (文末詞 dong)
- 1112: `docs/diglossia/12-particle-deh-in-action.md` (文末詞 deh)
- 1113: `docs/diglossia/13-particle-kok-in-action.md` (口語助詞 kok)
- 1114: `docs/diglossia/14-particle-kan-in-action.md` (確認詞 kan)
- 1115: `docs/diglossia/15-particle-lho-in-action.md` (感嘆詞 lho)
- 1116: `docs/diglossia/16-particle-ya-in-action.md` (終助詞 ya)
- 1117: `docs/diglossia/17-particle-combination.md` (助詞の連続技)
- 1118: `docs/diglossia/18-wa-chat-abbreviations-01.md` (WhatsApp子音略語)
- 1119: `docs/diglossia/19-wa-chat-abbreviations-02.md` (WhatsAppアクロニム・スラング)
- 1120: `docs/diglossia/20-slang-syllable-inversion-prokem.md` (プロケム音節反転法)

## 2. 検証項目
1. **語法・二重言語分析の精度**:
   - 会話助詞（dong, deh, kok, kan, lho, ya）の文脈別感情色彩（促し・妥協・驚き・同意・告知・軟化）の解説が極めて明快。
   - 助詞の複合用法（dong ya, sih sebenernya, kan ya, deh kayaknya）の実践的分析。
   - 現代インドネシアのデジタルコミュニケーション（WA略語: yg, bgt, tdk, otw, gpp, wkwk, mager, baper）の解読体系。
   - ストリートスラングの音節反転法（Prokem: kuy, sabi）の文化的背景。
2. **フォーマット規約**:
   - ルビ構文不使用。
   - 太字約物記法（`【タグ】「**日本語**」（原語）`）遵守。
   - コードスイッチング対比表、15問双方向リライトドリル、3問理解度クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
