# 校正レビュー報告書: TASK-1121 (二重言語 Baku ⇄ Gaul 1121-1130)

## 1. 対象記事
- 1121: `docs/diglossia/21-slang-contraction-habits.md` (短縮造語: mager, baper, bucin)
- 1122: `docs/diglossia/22-work-formal-email-to-wa.md` (ビジネス文書 ⇄ 社内チャット)
- 1123: `docs/diglossia/23-boss-report-formal-to-oral.md` (上司への口頭報告ブレンド術)
- 1124: `docs/diglossia/24-customer-cs-chat-register.md` (カスタマーサポート接客: Kak/Min)
- 1125: `docs/diglossia/25-sns-instagram-tiktok-slang.md` (SNSコメント欄: spill, salfok, FYP)
- 1126: `docs/diglossia/26-ordering-cafe-restaurant.md` (飲食店・カフェ注文)
- 1127: `docs/diglossia/27-taxi-ojol-ride-hailing.md` (タクシー・配車ナビ指示)
- 1128: `docs/diglossia/28-market-bargaining-tpo.md` (伝統市場・露店交渉術)
- 1129: `docs/diglossia/29-phone-call-switching.md` (電話応対コードスイッチング)
- 1130: `docs/diglossia/30-small-talk-weekend-gossip.md` (週末雑談・リラックスモード)

## 2. 検証項目
1. **場面別二重言語コードスイッチングの妥当性**:
   - 職場（メール vs チャット、上司報告）、商業（CS接客、カフェ、市場交渉、配車アプリ）、メディア（SNSミーム）、私生活（週末雑談）の各ドメインにおけるTPOレジスターの使い分けが極めて実践的。
   - インドネシア特有のビジネス文化（Pak/Buへの口頭敬意バランス、ECチャットのKak/Min文化）が正確に反映されている。
2. **フォーマット規約**:
   - ルビ構文不使用。
   - 太字約物記法（`【タグ】「**日本語**」（原語）`）遵守。
   - 対比表、15問双方向リライトドリル、3問理解度クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
