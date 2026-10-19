# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,370 / 1,500 記事 (91.3% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,380 / 1,500 記事 (92.0% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update 1371-1380
old_block = '''- [ ] `[未着手]` 1371: 語根 naik（上がる・乗る）の全派生語図鑑：menaikkan, kenaikan, menaiki, menaik (`docs/derivations-2/121-root-naik.md`)
- [ ] `[未着手]` 1372: 語根 jatuh（落ちる・失脚）の全派生語図鑑：menjatuhkan, kejatuhan, penjatuhan, terjatuh (`docs/derivations-2/122-root-jatuh.md`)
- [ ] `[未着手]` 1373: 語根 bangkit（立ち上がる・覚醒）の全派生語図鑑：membangkitkan, kebangkitan, pembangkit (`docs/derivations-2/123-root-bangkit.md`)
- [ ] `[未着手]` 1374: 語根 runtuh（崩壊・崩落）の全派生語図鑑：meruntuhkan, keruntuhan, reruntuhan (`docs/derivations-2/124-root-runtuh.md`)
- [ ] `[未着手]` 1375: 語根 roboh（倒壊・倒れる）の全派生語図鑑：merobohkan, kerobohan, penrobohan (`docs/derivations-2/125-root-roboh.md`)
- [ ] `[未着手]` 1376: 語根 tumbuh（生える・成長）の全派生語図鑑：menumbuhkan, pertumbuhan, tumbuhan (`docs/derivations-2/126-root-tumbuh.md`)
- [ ] `[未着手]` 1377: 語根 kembang（咲く・発展）の全派生語図鑑：mengembangkan, perkembangan, pengembangan (`docs/derivations-2/127-root-kembang.md`)
- [ ] `[未着手]` 1378: 語根 maju（前進・進歩）の全派生語図鑑：memajukan, kemajuan, pemajuan, bermutu (`docs/derivations-2/128-root-maju.md`)
- [ ] `[未着手]` 1379: 語根 mundur（後退・退く）の全派生語図鑑：memundurkan, kemunduran, pemunduran (`docs/derivations-2/129-root-mundur.md`)
- [ ] `[未着手]` 1380: 語根 hindar（避ける・回避）の全派生語図鑑：menghindari, terhindar, penghindaran (`docs/derivations-2/130-root-hindar.md`)'''

new_block = '''- [x] `[完了]` 1371: 語根 naik（上がる・乗る）の全派生語図鑑：menaikkan, kenaikan, menaiki, menaik (`docs/derivations-2/121-root-naik.md`)
- [x] `[完了]` 1372: 語根 jatuh（落ちる・失脚）の全派生語図鑑：menjatuhkan, kejatuhan, penjatuhan, terjatuh (`docs/derivations-2/122-root-jatuh.md`)
- [x] `[完了]` 1373: 語根 bangkit（立ち上がる・覚醒）の全派生語図鑑：membangkitkan, kebangkitan, pembangkit (`docs/derivations-2/123-root-bangkit.md`)
- [x] `[完了]` 1374: 語根 runtuh（崩壊・崩落）の全派生語図鑑：meruntuhkan, keruntuhan, reruntuhan (`docs/derivations-2/124-root-runtuh.md`)
- [x] `[完了]` 1375: 語根 roboh（倒壊・倒れる）の全派生語図鑑：merobohkan, kerobohan, penrobohan (`docs/derivations-2/125-root-roboh.md`)
- [x] `[完了]` 1376: 語根 tumbuh（生える・成長）の全派生語図鑑：menumbuhkan, pertumbuhan, tumbuhan (`docs/derivations-2/126-root-tumbuh.md`)
- [x] `[完了]` 1377: 語根 kembang（咲く・発展）の全派生語図鑑：mengembangkan, perkembangan, pengembangan (`docs/derivations-2/127-root-kembang.md`)
- [x] `[完了]` 1378: 語根 maju（前進・進歩）の全派生語図鑑：memajukan, kemajuan, pemajuan, bermutu (`docs/derivations-2/128-root-maju.md`)
- [x] `[完了]` 1379: 語根 mundur（後退・退く）の全派生語図鑑：memundurkan, kemunduran, pemunduran (`docs/derivations-2/129-root-mundur.md`)
- [x] `[完了]` 1380: 語根 hindar（避ける・回避）の全派生語図鑑：menghindari, terhindar, penghindaran (`docs/derivations-2/130-root-hindar.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with batch 3")
else:
    print("Old block not found in PROGRESS.md!")
