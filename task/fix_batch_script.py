# -*- coding: utf-8 -*-
with open('task/write_batch_1361_1370.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. kurang lebih
text = text.replace(
    '("kurang lebih", "成句副詞", "およそ、約、大体（kira-kira）", "Jarak dari sini ke bandara kurang lebih lima belas kilometer.")',
    '("kurang lebih", "frasa", "成句副詞", "およそ、約、大体（kira-kira）", "Jarak dari sini ke bandara kurang lebih lima belas kilometer.")'
)

# 2. bagaimanapun
text = text.replace(
    '("bagaimanapun", "接続詞", "いずれにせよ、ともかく、どんなに〜でも", "Bagaimanapun sulitnya situasi ini, kita tidak boleh menyerah.")',
    '("bagaimanapun", "kata sambung", "接続詞", "いずれにせよ、ともかく、どんなに〜でも", "Bagaimanapun sulitnya situasi ini, kita tidak boleh menyerah.")'
)

# 3. bergabung bersama
text = text.replace(
    '("bergabung bersama", "動詞句", "〜とともに合流・参加する", "Mari bergabung bersama kami membangun komunitas literasi digital.")',
    '("bergabung bersama", "frasa verba", "動詞句", "〜とともに合流・参加する", "Mari bergabung bersama kami membangun komunitas literasi digital.")'
)

# 6. daya tarik
text = text.replace(
    '("daya tarik", "名詞句", "魅力、求心力、アピール力、引力", "Keindahan alam bawah laut menjadi daya tarik utama wisata Bali.")',
    '("daya tarik", "frasa nomina", "名詞句", "魅力、求心力、アピール力、引力", "Keindahan alam bawah laut menjadi daya tarik utama wisata Bali.")'
)

# 7. gerobak dorong & mendorong maju
text = text.replace(
    '("gerobak dorong", "名詞句", "手押し車、カート", "Pedagang bakso keliling menjajakan dagangannya dengan gerobak dorong.")',
    '("gerobak dorong", "frasa nomina", "名詞句", "手押し車、カート", "Pedagang bakso keliling menjajakan dagangannya dengan gerobak dorong.")'
)
text = text.replace(
    '("mendorong maju", "動詞句", "前進させる、押し進める", "Inovasi teknologi mendorong maju peradaban manusia.")',
    '("mendorong maju", "frasa verba", "動詞句", "前進させる、押し進める", "Inovasi teknologi mendorong maju peradaban manusia.")'
)

# 7. details[2] pendorong (has extra 'peN-')
old_pendorong = '''            ("pendorong", "peN-", "名詞", "プンドロン",
             "人や出来事を「主たる推進力、後押し、アクセル、駆動力」として形容・比喩する表現です。",
             "faktor pendorong（推進要因・後押し因子）, motor pendorong（推進モーター・原動力）",
             "Sektor konsumsi rumah tangga tetap menjadi pendorong utama ekonomi kuartal ini.",
             "家計消費部門は今期も依然として経済の主要な牽引役であり続けている。")'''

new_pendorong = '''            ("pendorong", "名詞", "プンドロン",
             "人や出来事を「主たる推進力、後押し、アクセル、駆動力」として形容・比喩する表現です。",
             "faktor pendorong（推進要因・後押し因子）, motor pendorong（推進モーター・原動力）",
             "Sektor konsumsi rumah tangga tetap menjadi pendorong utama ekonomi kuartal ini.",
             "家計消費部門は今期も依然として経済の主要な牽引役であり続けている。")'''

text = text.replace(old_pendorong, new_pendorong)

# 8. angkat bicara
text = text.replace(
    '("angkat bicara", "慣用動詞句", "口を開く、公に発言・意見表明する", "Tokoh masyarakat akhirnya angkat bicara mengenai kasus korupsi tersebut.")',
    '("angkat bicara", "idiom", "慣用動詞句", "口を開く、公に発言・意見表明する", "Tokoh masyarakat akhirnya angkat bicara mengenai kasus korupsi tersebut.")'
)

# 9. turun tangan
text = text.replace(
    '("turun tangan", "慣用語・動詞", "介入する、直接手を差し伸べる、自ら出馬する", "Presiden turun tangan langsung menyelesaikan sengketa agraria warga.")',
    '("turun tangan", "idiom", "慣用語・動詞", "介入する、直接手を差し伸べる、自ら出馬する", "Presiden turun tangan langsung menyelesaikan sengketa agraria warga.")'
)

with open('task/write_batch_1361_1370.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement done.")
