# 校正レビュー報告書: TASK-1071 (クリニック 1071-1080)

## 1. 対象記事
- 1071: `docs/clinic/21-minta-tolong-bantu-levels.md` (minta tolong / tolong / bantu / mohon)
- 1072: `docs/clinic/22-pikir-kira-sangka-distinction.md` (pikir / kira / sangka / rasa)
- 1073: `docs/clinic/23-kenal-tahu-paham-boundaries.md` (kenal / tahu / paham)
- 1074: `docs/clinic/24-tinggal-hidup-stay-reside.md` (tinggal vs hidup)
- 1075: `docs/clinic/25-kembali-pulang-lagi-clash.md` (kembali vs pulang vs lagi)
- 1076: `docs/clinic/26-antar-jemput-bawa-directions.md` (antar vs kirim vs jemput vs bawa)
- 1077: `docs/clinic/27-pinjam-sewa-lend-borrow.md` (pinjam vs sewa vs meminjamkan)
- 1078: `docs/clinic/28-oleh-oleh-hadiah-gift.md` (oleh-oleh vs hadiah vs kado)
- 1079: `docs/clinic/29-kasihan-sayang-pity-regret.md` (kasihan vs sayang)
- 1080: `docs/clinic/30-capek-lelah-register-choice.md` (capek vs lelah)

## 2. 検証項目
1. **語法・正書法**:
   - 依頼表現の社会的距離・レジスター（minta tolong, mohon）の明確な解説。
   - 思考・推測動詞の境界（熟考 pikir, 推測・早合点 kira/sangka, 所感 rasa）。
   - 知得動詞の対象別選定（面識 kenal, 情報 tahu, 概念理解 paham）。
   - 居住（tinggal）と生命・生計（hidup）の混同防止。
   - 帰巣（pulang）と復帰（kembali）、反復（lagi）の峻別。
   - 移動方向ベクトル（人を送る antar, 迎える jemput, 郵送 kirim）。
   - 貸借の有償・無償（sewa vs pinjam）と使役（meminjamkan）。
   - 旅土産（oleh-oleh）と記念祝い品（hadiah/kado）の分類。
   - 同情（kasihan）と損失・惜別（sayang）の使い分け。
   - 口語（capek）と文語・心労（lelah）のTPOレジスター。
2. **フォーマット規約**:
   - ルビ構文不使用（アルファベット＋カタカナ発音欄）。
   - 太字約物記法（`「**強調**」`）遵守。
   - 各記事15問の瞬間口頭作文ドリル＋3問の選択式クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
