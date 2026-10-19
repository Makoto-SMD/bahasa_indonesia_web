# -*- coding: utf-8 -*-
with open('task/PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update summary
text = text.replace(
    '- **進捗状況**: 1,380 / 1,500 記事 (92.0% 達成・500記事拡充フェーズ進行中)',
    '- **進捗状況**: 1,390 / 1,500 記事 (92.7% 達成・500記事拡充フェーズ進行中)'
)

# 2. Replace lines 1468 to 1478
old_block = '''- [ ] `[未着手]` 1381: 語根 cegah（防ぐ・予防）の全派生語図鑑：mencegah, pencegahan, tercegah, pencegah (`docs/derivations-2/131-root-cegah.md`)
- [ ] `[未着手]` 1382: 語根 lindung（守る・保護）の全派生語図鑑：melindungi, perlindungan, pelindung, terlindung (`docs/derivations-2/132-root-lindung.md`)
- [ ] `[未着手]` 1383: 語根 bela（擁護・弁護）の全派生語図鑑：membela, pembelaan, pembela, terbela (`docs/derivations-2/133-root-bela.md`)
- [ ] `[未着手]` 1384: 語根 serang（攻撃・襲撃）の全派生語図鑑：menyerang, serangan, penyerangan, penyerang (`docs/derivations-2/134-root-serang.md`)
- [ ] `[未着手]` 1385: 語根 lawan（戦う・反対）の全派生語図鑑：melawan, perlawanan, lawan, berlawanan (`docs/derivations-2/135-root-lawan.md`)
- [ ] `[未着手]` 1386: 語根 tolak（拒絶・突き放す）の全派生語図鑑：menolak, penolakan, tertolak, bertolak (`docs/derivations-2/136-root-tolak.md`)
- [ ] `[未着手]` 1387: 語根 terima（受け取る・承認）の全派生語図鑑：menerima, penerimaan, penerima, diterima (`docs/derivations-2/137-root-terima.md`)
- [ ] `[未着手]` 1388: 語根 aku（認める・自白）の全派生語図鑑：mengakui, pengakuan, terakui, memperlakukan (`docs/derivations-2/138-root-akui.md`)
- [ ] `[未着手]` 1389: 語根 tolong（助ける・救助）の全派生語図鑑：menolong, pertolongan, penolong, tertolong (`docs/derivations-2/139-root-tolong.md`)
- [ ] `[未着手]` 1390: 語根 bantu（手伝う・支援）の全派生語図鑑：membantu, bantuan, pembantu, berbantuan (`docs/derivations-2/140-root-bantu.md`)'''

new_block = '''- [x] `[完了]` 1381: 語根 cegah（防ぐ・予防）の全派生語図鑑：mencegah, pencegahan, tercegah, pencegah (`docs/derivations-2/131-root-cegah.md`)
- [x] `[完了]` 1382: 語根 lindung（守る・保護）の全派生語図鑑：melindungi, perlindungan, pelindung, terlindung (`docs/derivations-2/132-root-lindung.md`)
- [x] `[完了]` 1383: 語根 bela（擁護・弁護）の全派生語図鑑：membela, pembelaan, pembela, terbela (`docs/derivations-2/133-root-bela.md`)
- [x] `[完了]` 1384: 語根 tuntut（要求・訴追）の全派生語図鑑：menuntut, tuntutan, penuntutan, penuntut (`docs/derivations-2/134-root-tuntut.md`)
- [x] `[完了]` 1385: 語根 gugat（提訴・告発）の全派生語図鑑：menggugat, gugatan, penggugat, tergugat (`docs/derivations-2/135-root-gugat.md`)
- [x] `[完了]` 1386: 語根 tolak（拒絶・却下）の全派生語図鑑：menolak, penolakan, tertolak, tolak ukur (`docs/derivations-2/136-root-tolak.md`)
- [x] `[完了]` 1387: 語根 terima（受ける・受諾）の全派生語図鑑：menerima, penerimaan, keterbukaan, terima kasih (`docs/derivations-2/137-root-terima.md`)
- [x] `[完了]` 1388: 語根 tolong（助ける・救助）の全派生語図鑑：menolong, pertolongan, penolong, tertolong (`docs/derivations-2/138-root-tolong.md`)
- [x] `[完了]` 1389: 語根 bantu（手伝う・支援）の全派生語図鑑：membantu, bantuan, pembantu, terbantu (`docs/derivations-2/139-root-bantu.md`)
- [x] `[完了]` 1390: 語根 layan（仕える・給仕）の全派生語図鑑：melayani, pelayanan, pelayan, terlayani (`docs/derivations-2/140-root-layan.md`)'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open('task/PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("PROGRESS.md updated successfully with batch 4")
else:
    print("Old block not found!")
