# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,390 / 1,500 記事 (92.7% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,400 / 1,500 記事 (93.3% 達成・大台1,400記事達成！)'
)

# 2. Update lines 1478 to 1487
old_block = '''- [ ] `[未着手]` 1391: 語根 layan（仕える・給仕・サービス）の全派生語図鑑：melayani, pelayanan, pelayan, terlayani (`docs/derivations-2/141-root-layani.md`)
- [ ] `[未着手]` 1392: 語根 urus（処理・世話）の全派生語図鑑：mengurus, pengurusan, pengurus, urusan (`docs/derivations-2/142-root-urus.md`)
- [ ] `[未着手]` 1393: 語根 kelola（管理・運営）の全派生語図鑑：mengelola, pengelolaan, pengelola, terkelola (`docs/derivations-2/143-root-kelola.md`)
- [ ] `[未着手]` 1394: 語根 pimpin（率いる・指導）の全派生語図鑑：memimpin, pimpinan, kepemimpinan, pemimpin (`docs/derivations-2/144-root-pimpin.md`)
- [ ] `[未着手]` 1395: 語根 arah（方向・指導指示）の全派生語図鑑：mengarahkan, pengarahan, arahan, terarah (`docs/derivations-2/145-root-arah.md`)
- [ ] `[未着手]` 1396: 語根 bimbing（導く・指導）の全派生語図鑑：membimbing, bimbingan, pembimbing, terbimbing (`docs/derivations-2/146-root-bimbing.md`)
- [ ] `[未着手]` 1397: 語根 didik（教え育てる・教育）の全派生語図鑑：mendidik, pendidikan, pendidik, terdidik (`docs/derivations-2/147-root-didik.md`)
- [ ] `[未着手]` 1398: 語根 latih（訓練する・練習）の全派生語図鑑：melatih, pelatihan, pelatih, terlatih (`docs/derivations-2/148-root-latih.md`)
- [ ] `[未着手]` 1399: 語根 ajar（学ぶ・教える）の全派生語図鑑：belajar, mengajar, pelajaran, pengajaran, pengajar (`docs/derivations-2/149-root-ajar.md`)
- [ ] `[未着手]` 1400: 語根 uji（試す・試験・検証）の全派生語図鑑：menguji, ujian, pengujian, teruji (`docs/derivations-2/150-root-uji.md`)'''

new_block = '''- [x] `[完了]` 1391: 語根 urus（処理・世話）の全派生語図鑑：mengurus, pengurusan, pengurus, urusan (`docs/derivations-2/141-root-urus.md`)
- [x] `[完了]` 1392: 語根 kelola（管理・運営）の全派生語図鑑：mengelola, pengelolaan, pengelola, terkelola (`docs/derivations-2/142-root-kelola.md`)
- [x] `[完了]` 1393: 語根 pimpin（率いる・指導）の全派生語図鑑：memimpin, pimpinan, kepemimpinan, pemimpin (`docs/derivations-2/143-root-pimpin.md`)
- [x] `[完了]` 1394: 語根 arah（方向・指導指示）の全派生語図鑑：mengarahkan, pengarahan, arahan, terarah (`docs/derivations-2/144-root-arah.md`)
- [x] `[完了]` 1395: 語根 bimbing（導く・指導）の全派生語図鑑：membimbing, bimbingan, pembimbing, terbimbing (`docs/derivations-2/145-root-bimbing.md`)
- [x] `[完了]` 1396: 語根 didik（教え育てる・教育）の全派生語図鑑：mendidik, pendidikan, pendidik, terdidik (`docs/derivations-2/146-root-didik.md`)
- [x] `[完了]` 1397: 語根 latih（訓練する・練習）の全派生語図鑑：melatih, pelatihan, pelatih, terlatih (`docs/derivations-2/147-root-latih.md`)
- [x] `[完了]` 1398: 語根 uji（試す・試験・検証）の全派生語図鑑：menguji, ujian, pengujian, teruji (`docs/derivations-2/148-root-uji.md`)
- [x] `[完了]` 1399: 語根 nilai（評価・採点・価値）の全派生語図鑑：menilai, penilaian, penilai, nilai (`docs/derivations-2/149-root-nilai.md`)
- [x] `[完了]` 1400: 【総括】語根別派生語マスター図鑑 第2弾 50問総合マスター検定 (`docs/derivations-2/150-section33-master-exam.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with batch 5")
else:
    print("Old block not found!")
