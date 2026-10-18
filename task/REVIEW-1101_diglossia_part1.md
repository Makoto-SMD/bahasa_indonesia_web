# 校正レビュー報告書: TASK-1101 (二重言語 Baku ⇄ Gaul 1101-1110)

## 1. 対象記事
- 1101: `docs/diglossia/01-daily-actions-baku-gaul.md` (日常動作動詞)
- 1102: `docs/diglossia/02-verbs-prefix-men-dropping.md` (meN- 接頭辞脱落と鼻音化)
- 1103: `docs/diglossia/03-passive-di-vs-ke-an.md` (受動態 di-/ter- ⇄ ke-/ke-...-an)
- 1104: `docs/diglossia/04-pronouns-saya-aku-gue.md` (代名詞3大レジスター)
- 1105: `docs/diglossia/05-negation-tidak-nggak-ndak.md` (否定詞 tidak ⇄ nggak/ndak/kagak)
- 1106: `docs/diglossia/06-aspect-sudah-udah-belum-belom.md` (アスペクト短縮 udah/belom/lagi)
- 1107: `docs/diglossia/07-question-apakah-apaan-gimana.md` (疑問詞短縮 gimana/kenapa/apaan)
- 1108: `docs/diglossia/08-time-sekarang-skrg-ntar.md` (時間短縮 bentar/ntar/kemaren)
- 1109: `docs/diglossia/09-conjunction-kalau-kalo-tapi.md` (接続詞短縮 tapi/kalo/soalnya)
- 1110: `docs/diglossia/10-particle-sih-in-action.md` (文末詞 sih の機能)

## 2. 検証項目
1. **二重言語（Diglossia）論に基づくコードスイッチングの妥当性**:
   - 公式標準語（Bahasa Baku）と街角口語（Bahasa Gaul / Percakapan）の対照が正確。
   - 単なるくだけた言葉遣いにとどまらず、音韻短縮（縮約・語末母音変容・鼻音化）の規則性が明快。
   - 人称代名詞（saya/Anda vs aku/kamu vs gue/lu）の社会的距離と使用境界が明確。
   - 口語受動態（偶発 ke-, 被害 ke-...-an）の用例が極めて自然。
2. **フォーマット規約**:
   - ルビ構文不使用。
   - 太字約物記法（`【タグ】「**日本語**」（原語）`）遵守。
   - コードスイッチング対比表、15問双方向リライトドリル、3問理解度クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
