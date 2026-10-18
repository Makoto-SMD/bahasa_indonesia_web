# 校正レビュー報告書: TASK-1081 (クリニック 1081-1090)

## 1. 対象記事
- 1081: `docs/clinic/31-lucu-menarik-funny-interesting.md` (lucu vs menarik)
- 1082: `docs/clinic/32-aneh-lucu-strange-clash.md` (aneh vs lucu)
- 1083: `docs/clinic/33-mudah-gampang-susah-sulit.md` (mudah/gampang vs susah/sulit)
- 1084: `docs/clinic/34-apa-apakah-indirect-question.md` (apa vs apakah)
- 1085: `docs/clinic/35-setelah-sesudah-sejak-timeline.md` (setelah/sesudah vs sejak)
- 1086: `docs/clinic/36-frequency-adverbs-placement.md` (selalu, sering, jarang placement)
- 1087: `docs/clinic/37-mungkin-barangkali-bisa-jadi.md` (mungkin vs barangkali vs bisa jadi)
- 1088: `docs/clinic/38-baru-saja-pas-tepat-timing.md` (baru saja vs pas/tepat)
- 1089: `docs/clinic/39-harus-wajib-mesti-perlu.md` (harus vs wajib vs mesti vs perlu)
- 1090: `docs/clinic/40-boleh-bisa-permission-ability.md` (boleh vs bisa)

## 2. 検証項目
1. **語法・正書法**:
   - ユーモア（lucu）と知的好奇心（menarik）の厳格な峻別。
   - 異常・奇妙（aneh）と滑稽（lucu）の混同防止。
   - 口語（gampang/susah）と公用・文語（mudah/sulit）の使い分け。
   - 疑問代名詞 apa と Yes/No・間接疑問 apakah の構文機能。
   - 前後順序（setelah）と過去起点の継続（sejak）の時間軸。
   - 頻度副詞（特に準否定 jarang の位置と二重否定の回避）。
   - 推量表現の確信度と相槌（bisa jadi, barangkali）。
   - 直前完了（baru saja）と時空合致（pas/tepat）の区分。
   - 強制力グラデーション（法・宗教義務 wajib, 必然 harus, 推奨 perlu）。
   - 許可（boleh）と能力・物理的可能（bisa）の混同是正。
2. **フォーマット規約**:
   - ルビ構文不使用、太字約物記法（`「**強調**」`）遵守。
   - 15問ドリル＋3問クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
