# -*- coding: utf-8 -*-
with open('pdca/NOTES.md', 'r', encoding='utf-8') as f:
    text = f.read()

new_note = r'''
### 2026-10-19: セクション34「【資格演習】検定・UKBI直前実戦模試＆徹底解説」第4バッチ（1431〜1440）完遂（累計1,440記事達成）
- **Director**:
  - 検定・UKBIで合否を分ける難問対策（空所補充Vol.1・Vol.2、誤文訂正Vol.1・Vol.2、速読斜め読み技術Vol.1・Vol.2、不規則鼻音化例外、古典文語、必須アクロニム、EYD第5版句読点）の全10記事（1431〜1440）を企画・指示。
- **Writer**:
  - 全10記事において、「出題傾向・評価基準」「攻略フレームワーク・解法セオリー」「本番同等レベルの実戦想定問題（選択肢・正解アコーディオン・詳細論理解説）」「重要語彙・構文対比テーブル」「合格者の着眼点・プロのアドバイス」の最高峰の演習構成を完備。
  - ルビゼロ規約、太字約物記法（`「**...**」`）の完全遵守。
- **Reviewer**:
  - 他動詞（-kan/-i）空所補充、相関接続詞ペア（baik... maupun...）、重複表現（pleonasme: adalah merupakan, demi untuk）の排除、主語欠落文の発見ロジック、二重子音（memproduksi, mengkritik, mentransfer）の脱落例外、古典マレー談話標識（Alkisah, Hatta, Bahwasanya）、必須アクロニム（KPK, OTT, OJK）、EYD第5版の句読点規則の論理的整合性を検証し、全10記事 APPROVED（`task/REVIEW-1431_exam_batch4.md`）。
- **Engineer**:
  - `zensical.toml` の `nav` 登録、`python .\task\lint_markdown.py` 検証（エラー0件・一発合格）、`zensical build`（エラー・警告0件、No issues found）を確認。
- **BOSS**:
  - **第4バッチ（1431〜1440）完結を承認！累計記事数は 1,440 / 1,500 記事（進捗率 96.0% / 残り60記事）に到達。**
  - これにより上級・最上級受験者が最も失点しやすい文法トラップ・速読・特殊語彙領域の完全攻略法が揃った。
  - 自律・連続実行の原則を貫き、直ちに**第5バッチ「1441〜1450: 専門翻訳・面接スピーキング・UKBI Istimewa・特A級栄誉殿堂＆総合実戦模試 10記事」**へ突入し、セクション34を完全完結させよ！
'''

text = text.rstrip() + "\n" + new_note
with open('pdca/NOTES.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("NOTES.md updated successfully with exam batch 4")
