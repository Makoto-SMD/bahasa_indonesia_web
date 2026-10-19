# -*- coding: utf-8 -*-
with open('task/write_batch_1351_1360.py', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '("lepas tangan", "成句", "無責任に手を引く、責任逃れをする", "Pimpinan proyek tidak boleh lepas tangan atas kegagalan teknis ini.")',
    '("lepas tangan", "-", "成句", "無責任に手を引く、責任逃れをする", "Pimpinan proyek tidak boleh lepas tangan atas kegagalan teknis ini.")'
)

c = c.replace(
    '("pasang surut", "複合名詞", "潮の満ち引き、栄枯盛衰、人生の浮き沈み", "Mereka telah melewati berbagai pasang surut dalam berbisnis.")',
    '("pasang surut", "-", "複合名詞", "潮の満ち引き、栄枯盛衰、人生の浮き沈み", "Mereka telah melewati berbagai pasang surut dalam berbisnis.")'
)

c = c.replace(
    '("ganti rugi", "複合語", "損害賠償、補償金", "Pihak maskapai memberikan uang ganti rugi atas kehilangan bagasi.")',
    '("ganti rugi", "-", "複合語", "損害賠償、補償金", "Pihak maskapai memberikan uang ganti rugi atas kehilangan bagasi.")'
)

c = c.replace(
    '("berpindah tangan", "成句", "（所有権が）人手に渡る、所有者が変わる", "Lukisan bersejarah itu telah berpindah tangan beberapa kali.")',
    '("berpindah tangan", "-", "成句", "（所有権が）人手に渡る、所有者が変わる", "Lukisan bersejarah itu telah berpindah tangan beberapa kali.")'
)

with open('task/write_batch_1351_1360.py', 'w', encoding='utf-8') as f:
    f.write(c)

print('Patched matrix tuples successfully.')
