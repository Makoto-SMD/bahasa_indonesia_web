# 校正レビュー報告書: TASK-1091 (クリニック 1091-1100・セクション26完結)

## 1. 対象記事
- 1091: `docs/clinic/41-mengajak-mengundang-invite.md` (mengajak vs mengundang)
- 1092: `docs/clinic/42-bicara-ngomong-bilang-berkata.md` (bicara, ngomong, bilang, berkata)
- 1093: `docs/clinic/43-lupa-ketinggalan-forgot-left.md` (lupa vs ketinggalan)
- 1094: `docs/clinic/44-hilang-kehilangan-kalah-loss.md` (hilang vs kehilangan vs kalah)
- 1095: `docs/clinic/45-menang-kalah-mengalahkan.md` (menang vs kalah vs mengalahkan)
- 1096: `docs/clinic/46-rusak-patah-hancur-pecah.md` (rusak, patah, hancur, pecah)
- 1097: `docs/clinic/47-jatuh-gugur-turun-fall.md` (jatuh, gugur, turun)
- 1098: `docs/clinic/48-naik-turun-menumpang-transit.md` (naik, turun, menumpang, transit)
- 1099: `docs/clinic/49-buka-tutup-membukakan-doors.md` (buka, tutup, membukakan)
- 1100: `docs/clinic/50-clinic-comprehensive-drill.md` (全50テーマ総合診断)

## 2. 検証項目
1. **語法・正書法**:
   - 行動同行（mengajak）と公式招待（mengundang）の社会的レジスター。
   - 言語能力（berbicara）と日常引用（bilang）、公式言及（menyampaikan）。
   - 記憶失念（lupa）と物理的置き忘れ（ketinggalan）の構文区分。
   - 自動詞消失（hilang）と主語被害（kehilangan）、勝負の敗北（kalah）。
   - 自動詞勝敗（menang/kalah）と他動詞使役（mengalahkan）。
   - 物理損傷形態の峻別（故障 rusak, 折損 patah, 瓦解 hancur, 割れ pecah）。
   - 落下（jatuh）と殉職・落選（gugur）、下降（turun）、試験不合格（gagal）。
   - 乗車（naik）、降車（turun）、便乗（numpang）、乗換（pindah kereta）。
   - 開閉（buka/tutup）と受益使役（membukakan pintu）。
   - 50問総合診断テストによる全クリニック処方箋の定着化。
2. **フォーマット規約**:
   - ルビ構文不使用、太字約物記法（`「**強調**」`）遵守。
   - 15問ドリル＋3問クイズ完備。
3. **エンジニア検証**:
   - `lint_markdown.py`: 0 errors.

## 3. 判定
**APPROVED (承認)**
セクション26【誤用克服】全50記事の完結を承認。即時 `zensical.toml` の nav に登録し、進捗更新および Git コミットを実行可能。
