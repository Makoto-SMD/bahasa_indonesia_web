# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,360 / 1,500 記事 (90.7% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,370 / 1,500 記事 (91.3% 達成・500記事拡充フェーズ進行中)'
)

# 2. Update 1361-1370
old_block = '''- [ ] `[未着手]` 1361: 語根 tambah（増える・添加）の全派生語図鑑：menambah, bertambah, tambahan, penambahan (`docs/derivations-2/111-root-tambah.md`)
- [ ] `[未着手]` 1362: 語根 kurang（減る・不足）の全派生語図鑑：mengurangi, berkurang, kekurangan, pengurangan (`docs/derivations-2/112-root-kurang.md`)
- [ ] `[未着手]` 1363: 語根 bagi（分ける・分配）の全派生語図鑑：membagi, berbagi, pembagian, sebagian (`docs/derivations-2/113-root-bagi.md`)
- [ ] `[未着手]` 1364: 語根 gabung（結合・合併）の全派生語図鑑：menggabungkan, bergabung, penggabungan, gabungan (`docs/derivations-2/114-root-gabung.md`)
- [ ] `[未着手]` 1365: 語根 kumpul（集まる・収集）の全派生語図鑑：mengumpulkan, perkumpulan, pengumpulan, terkumpul (`docs/derivations-2/115-root-kumpul.md`)
- [ ] `[未着手]` 1366: 語根 pisah（分かれる・隔離）の全派生語図鑑：memisahkan, berpisah, pemisahan, terpisah (`docs/derivations-2/116-root-pisah.md`)
- [ ] `[未着手]` 1367: 語根 tarik（引く・魅力）の全派生語図鑑：menarik, tertarik, ketertarikan, penarikan (`docs/derivations-2/117-root-tarik.md`)
- [ ] `[未着手]` 1368: 語根 dorong（押す・推進）の全派生語図鑑：mendorong, dorongan, pendorong, terdorong (`docs/derivations-2/118-root-dorong.md`)
- [ ] `[未着手]` 1369: 語根 angkat（持ち上げる・任命）の全派生語図鑑：mengangkat, pengangkatan, angkatan, terangkat (`docs/derivations-2/119-root-angkat.md`)
- [ ] `[未着手]` 1370: 語根 turun（下りる・低下）の全派生語図鑑：menurunkan, penurunan, keturunan, menurun (`docs/derivations-2/120-root-turun.md`)'''

new_block = '''- [x] `[完了]` 1361: 語根 tambah（増える・添加）の全派生語図鑑：menambah, bertambah, tambahan, penambahan (`docs/derivations-2/111-root-tambah.md`)
- [x] `[完了]` 1362: 語根 kurang（減る・不足）の全派生語図鑑：mengurangi, berkurang, kekurangan, pengurangan (`docs/derivations-2/112-root-kurang.md`)
- [x] `[完了]` 1363: 語根 bagi（分ける・分配）の全派生語図鑑：membagi, berbagi, pembagian, sebagian (`docs/derivations-2/113-root-bagi.md`)
- [x] `[完了]` 1364: 語根 gabung（結合・合併）の全派生語図鑑：menggabungkan, bergabung, penggabungan, gabungan (`docs/derivations-2/114-root-gabung.md`)
- [x] `[完了]` 1365: 語根 kumpul（集まる・収集）の全派生語図鑑：mengumpulkan, perkumpulan, pengumpulan, terkumpul (`docs/derivations-2/115-root-kumpul.md`)
- [x] `[完了]` 1366: 語根 pisah（分かれる・隔離）の全派生語図鑑：memisahkan, berpisah, pemisahan, terpisah (`docs/derivations-2/116-root-pisah.md`)
- [x] `[完了]` 1367: 語根 tarik（引く・魅力）の全派生語図鑑：menarik, tertarik, ketertarikan, penarikan (`docs/derivations-2/117-root-tarik.md`)
- [x] `[完了]` 1368: 語根 dorong（押す・推進）の全派生語図鑑：mendorong, dorongan, pendorong, terdorong (`docs/derivations-2/118-root-dorong.md`)
- [x] `[完了]` 1369: 語根 angkat（持ち上げる・任命）の全派生語図鑑：mengangkat, pengangkatan, angkatan, terangkat (`docs/derivations-2/119-root-angkat.md`)
- [x] `[完了]` 1370: 語根 turun（下りる・低下）の全派生語図鑑：menurunkan, penurunan, keturunan, menurun (`docs/derivations-2/120-root-turun.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully.")
else:
    print("Old block not found!")
