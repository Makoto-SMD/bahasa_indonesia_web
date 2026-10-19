# -*- coding: utf-8 -*-
"""
セクション34 第1バッチ (1401-1410) 記事生成スクリプト
【資格演習】検定・UKBI直前実戦模試＆徹底解説
"""

import os

articles = [
    {
        "filename": "01-inken-b-structure-grammar.md",
        "title": "1401. 【技能検定B級対策】文法・構造問題の急所：接尾辞-kan/-iと周囲辞の識別",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "インドネシア語技能検定B級の筆記試験において、合否の分かれ目となるのが「接尾辞 -kan と -i の機能的識別」および「周囲辞 ke-...-an, peN-...-an, per-...-an の意味的対比」です。本記事では、過去問の出題パターンを徹底分析し、瞬時に正解を導き出すための構文識別アルゴリズムを伝授します。",
        "theory": [
            ("接尾辞 -kan の三大機能（使役・受益・道具）",
             "1. **使役（kausatif）**: 目的語をある状態にする、または移動させる（例: membersihkan＝清潔にする、menaikkan＝引き上げる）。\n"
             "2. **受益（benefaktif）**: 他者のために動作を行う（例: membelikan ayah kopi＝父のためにコーヒーを買ってあげる）。第1目的語が受益者、第2目的語が対象。\n"
             "3. **道具・手段（instrumental）**: その物を道具として使う（例: melemparkan batu＝石を投げる）。"),
            ("接尾辞 -i の三大機能（場所・反復・状態付与）",
             "1. **場所・対象指向（lokatif）**: 動作が向かう場所や対象そのものを目的語にとる（例: memasuki ruangan＝部屋に入る、menghadiri rapat＝会議に出席する）。前置詞 ke/di を吸収する性質がある。\n"
             "2. **反復・反復動作（iteratif）**: 動作を何度も繰り返す（例: memukuli＝何度も殴りつける）。\n"
             "3. **付与使役**: 目的語に何かを授ける・塗る（例: menggarami masakan＝料理に塩を振る）。"),
            ("周囲辞 peN-...-an と per-...-an の決定的識別法",
             "基底となる動詞の接辞によって決定される：\n"
             "- **meN- 動詞から派生** → **peN-...-an**（能動的・人為的プロセス・行為）：mengembangkan → pengembangan（開発・育成作業）。\n"
             "- **ber- 動詞から派生** → **per-...-an**（自発的状態・集合的現象・制度）：berkembang → perkembangan（発展・進歩・推移現象）。")
        ],
        "problems": [
            {
                "q": "Pemerintah berupaya [...] subsidi bahan bakar minyak secara bertahap agar tidak membebani anggaran negara.",
                "options": ["A. mengurangi", "B. mengurangkan", "C. berkurang", "D. pengurangan"],
                "ans": "A. mengurangi",
                "expl": "目的語「subsidi BBM（燃料補助金）」という数量・負担を人為的に「削減する・減らす」他動詞が必要です。数量を減らす他動詞は接尾辞 -i を伴う mengurangi が標準的です。mengurangkan は通常、引き算（〜から引く）や免除で用いられます。"
            },
            {
                "q": "Direktur Utama meminta sekretaris untuk [...] dokumen kontrak kerja sama ke kantor rekanan di Jakarta Pusat.",
                "options": ["A. mengantarkan", "B. mengantari", "C. perantaran", "D. pengantar"],
                "ans": "A. mengantarkan",
                "expl": "書類（dokumen kontrak）という物を目的の場所へ「送り届ける・持参する」使役・移動動作なので、接尾辞 -kan を伴う mengantarkan が正解です。mengantari は「（人に対して）届けてあげる」という意味になります。"
            },
            {
                "q": "Kawasan wisata alam ini terkenal karena [...] pemandangan danau vulkanik yang sangat memukau.",
                "options": ["A. menyuguhkan", "B. menyuguhi", "C. suguhan", "D. disuguhkan"],
                "ans": "A. menyuguhkan",
                "expl": "目的語が「景色（pemandangan）」という差し出される対象（提供物）であるため、接尾辞 -kan を伴う menyuguhkan が適切です。menyuguhi の場合は「客（tamu）」など提供を受ける側が目的語になります。"
            }
        ],
        "table": [
            ("menduduki", "場所・地位を占める（Kursi, jabatan）", "mendudukkan", "人を座らせる、地位に就かせる（使役）"),
            ("menanami", "土地に作物を植え付ける（Menanami sawah）", "menanamkan", "種や資本・思想を植え込む（Menanamkan modal）"),
            ("mengirimi", "人に物を送る（Mengirimi ibu uang）", "mengirimkan", "物を人に送る（Mengirimkan uang kepada ibu）"),
            ("menemui", "人に面会する・訪ねる（Menemui klien）", "menemukan", "物を発見する・見つけ出す（Menemukan bukti）"),
            ("mengetahui", "事実・知識を知っている（Mengetahui rahasia）", "mengenalkan", "人や物を紹介する（Mengenalkan teman）")
        ],
        "pro_tip": "B級の文法問題では、「目的語が＜人/場所＞なのか＜物/情報＞なのか」を判別することが最速の解法です。-i は目的語に場所・相手が来やすく、-kan は動かされる物・使役対象が来ます。"
    },
    {
        "filename": "02-inken-b-vocabulary-synonyms.md",
        "title": "1402. 【技能検定B級対策】類義語・語彙選択：文脈に最適な語彙を見抜くテクニック",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "B級の語彙セクションでは、辞書的な日本語訳が同じ（「減る」「見る」「知る」など）複数の選択肢から、文脈のレジスター（公的度・文章語・日常語）や共起関係（コロケーション）に最も合致する1語を選び出す能力が厳格に問われます。",
        "theory": [
            ("視覚動词のレジスターと使い分け（melihat, memandang, meninjau, menyaksikan）",
             "- **melihat**: 最も一般的な「見る・視界に入る」。\n"
             "- **memandang**: 遠くや風景を「じっと見つめる」、または抽象的に「〜とみなす・評価する」。\n"
             "- **meninjau**: 政策や現場を「視察する・再検討する・レビューする」（公的・政策実務語）。\n"
             "- **menyaksikan**: 事件や式典を「目撃する・立ち会う」（証人・公的目撃）。"),
            ("知得・理解動詞のグラデーション（tahu, kenal, paham, mengerti, menyadari）",
             "- **tahu**: 事実や情報を客観的に「知っている」。\n"
             "- **kenal**: 人や場所と「面識がある・親しい」。\n"
             "- **paham / mengerti**: 理由や仕組み、言語のロジックを「理解・把握している」。\n"
             "- **menyadari**: 自らの過ちや状況の重大性を「自覚する・認識する」心境の変化。"),
            ("減少・衰退を表す類義語（berkurang, menurun, menyusut, merosot）",
             "- **berkurang**: 数量や痛みが一般的に「減る」。\n"
             "- **menurun**: グラフや健康状態、気温が「下降する・低下する」。\n"
             "- **menyusut**: 面積や体積、布が「縮小する・縮む」。\n"
             "- **merosot**: 通貨や業績、道徳が「暴落する・急激に悪化する」。")
        ],
        "problems": [
            {
                "q": "Presiden didampingi Menteri PUPR dijadwalkan [...] progres pembangunan bendungan raksasa di Jawa Barat.",
                "options": ["A. melihat", "B. meninjau", "C. menyaksikan", "D. memandang"],
                "ans": "B. meninjau",
                "expl": "大統領が大臣を伴って国家プロジェクトの進捗を「視察・現場査察する」公的文脈であるため、meninjau が最も適切です。"
            },
            {
                "q": "Nilai tukar rupiah terhadap dolar AS mengalami [...] tajam akibat ketidakpastian pasar finansial global.",
                "options": ["A. kemerosotan", "B. penurunan", "C. penyusutan", "D. pengurangan"],
                "ans": "A. kemerosotan",
                "expl": "通貨価値や市場価格の急激な「下落・暴落（slump）」には、形容詞 tajam（急激な）と共起して kemerosotan tajam が最も自然な経済表現です。"
            },
            {
                "q": "Meskipun mereka bekerja di gedung yang sama, saya belum [...] secara akrab dengan manajer pemasaran baru itu.",
                "options": ["A. mengenal", "B. mengetahui", "C. menyadari", "D. memahami"],
                "ans": "A. mengenal",
                "expl": "新任マネージャーという「人物」と面識を持ち親しく知り合っているかどうかなので、人称対象をとる mengenal（kenal）が正解です。"
            }
        ],
        "table": [
            ("taraf", "生活水準・発展段階（taraf hidup, taraf internasional）", "tingkat", "階級・度合い・レベル（tingkat suku bunga, tingkat pendidikan）"),
            ("dampak", "政策や事件の強い影響・余波（dampak negatif）", "pengaruh", "文化・思想・人物の浸透的影響（pengaruh globalisasi）"),
            ("syarat", "資格や契約の必要条件（syarat pendaftaran）", "ketentuan", "法令や規程の条項・定め（ketentuan hukum）"),
            ("peluang", "ビジネスや将来の好機・チャンス（peluang usaha）", "kesempatan", "時間的・偶発的な機会（kesempatan emas）"),
            ("hambatan", "進行を妨げる障害・ハードル（hambatan perdagangan）", "rintangan", "物理的・人生の険しい障壁（rintangan alam）")
        ],
        "pro_tip": "類義語問題では、直前直後の名詞との「定型コロケーション」を記憶しているかが勝負です。例: taraf hidup（生活水準）であって tingkat hidup とは言いません。"
    },
    {
        "filename": "03-inken-b-error-correction.md",
        "title": "1403. 【技能検定B級対策】誤文訂正セクション：文法的な不整合を即座に発見する法",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "技能検定B級の筆記試験で多くの受験者が時間を浪費してしまうのが「下線部A〜Dのうち文法的に誤っているものを1つ選ぶ」誤文訂正問題です。出題される誤りのパターンは限定されており、5つの典型トラップを頭に叩き込んでおけば、5秒で正解を見抜くことが可能です。",
        "theory": [
            ("誤文訂正の5大頻出パターン",
             "1. **受動態の主語・動詞・行為者の不整合**: 一人称・二人称の語幹受動態（buku ini saya baca）と三人称の di-...-nya/oleh（buku ini dibaca oleh mereka）の混同。\n"
             "2. **前置詞の二重使用・欠落**: tentang, terhadap, kepada, untuk などの前置詞が他動詞の直後に不要に挿入されているケース（例: membicarakan tentang masalah → membicarakan masalah）。\n"
             "3. **重複強調の不自然さ**: sangat...sekali, amat...sekali, para...sekalian などの重複誤用。\n"
             "4. **接辞の誤用**: 自動詞に不要な -kan が付いている、または名詞化接辞の取り違え（peN-...-an vs per-...-an）。\n"
             "5. **時間詞・アスペクトの衝突**: sudah と belum の矛盾、kemarin と akan の時制不一致。")
        ],
        "problems": [
            {
                "q": "次の文の下線部(A)〜(D)のうち、文法的に誤っているものはどれか？\n\nKomite pengawas (A) [sedang mendiskusikan] (B) [tentang] langkah strategis (C) [untuk mengatasi] defisit anggaran yang (D) [semakin membengkak].",
                "options": ["A. sedang mendiskusikan", "B. tentang", "C. untuk mengatasi", "D. semakin membengkak"],
                "ans": "B. tentang",
                "expl": "他動詞 mendiskusikan は直接目的語をとるため、前置詞 tentang を直後に置くことはできません（mendiskusikan tentang は典型的な誤用）。正しくは「mendiskusikan langkah strategis」とするか、自動詞を用いて「berdiskusi tentang langkah strategis」とします。"
            },
            {
                "q": "次の文の下線部(A)〜(D)のうち、文法的に誤っているものはどれか？\n\nLaporan keuangan tahunan (A) [tersebut] (B) [sudah diselesaikan oleh saya] (C) [sebelum] rapat umum pemegang saham (D) [dimulai].",
                "options": ["A. tersebut", "B. sudah diselesaikan oleh saya", "C. sebelum", "D. dimulai"],
                "ans": "B. sudah diselesaikan oleh saya",
                "expl": "行為者が一人称代名詞「saya」の場合、di- 動詞受動態（diselesaikan oleh saya）ではなく、語幹受動態を用いて「sudah saya selesaikan」とするのが標準語法（bahasa baku）の厳格な規則です。"
            },
            {
                "q": "次の文の下線部(A)〜(D)のうち、文法的に誤っているものはどれか？\n\n(A) [Para peserta-peserta seminar] (B) [sangat antusias sekali] (C) [mendengarkan paparan] dari (D) [pakar ekonomi terkemuka] tersebut.",
                "options": ["A. Para peserta-peserta seminar", "B. sangat antusias sekali", "C. mendengarkan paparan", "D. pakar ekonomi terkemuka"],
                "ans": "A. Para peserta-peserta seminar",
                "expl": "複数の人称を表す「para」の直後に重複名詞「peserta-peserta」を重ねることは二重複数（redundansi）の重大な誤用です。正しくは「Para peserta seminar」または「Peserta-peserta seminar」のいずれかに統一しなければなりません。"
            }
        ],
        "table": [
            ("誤: membicarakan tentang...", "正: membicarakan... / berbicara tentang...", "他動詞は前置詞不要"),
            ("誤: surat ini ditulis oleh saya", "正: surat ini saya tulis", "一人称行為者の語幹受動態"),
            ("誤: sangat indah sekali", "正: sangat indah / indah sekali", "二重強調の回避"),
            ("誤: demi untuk kepentingan bersama", "正: demi kepentingan / untuk kepentingan", "目的接続詞の重複禁止"),
            ("誤: bertujuan untuk memajukan", "正: bertujuan memajukan", "bertujuan の直後は動詞直接接続")
        ],
        "pro_tip": "誤文訂正では、まず「動詞の直後に前置詞（tentang, akan, dengan）がないか」「di-... oleh saya/kami になっていないか」「para + 重複形になっていないか」の3点を真っ先にスキャンしてください。"
    },
    {
        "filename": "04-inken-b-reading-business.md",
        "title": "1404. 【技能検定B級対策】長文読解（ビジネス・経済）：パラグラフ要約と設問解法",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "B級の長文読解は、現代インドネシアの経済、デジタル化、環境政策、企業活動をテーマとする約400〜600語の本格的な論説パッセージが出題されます。設問の意図を正確に見抜き、パラグラフごとのトピック文（kalimat utama）を素早く特定して解答する直読直解ストラテジーを解説します。",
        "theory": [
            ("B級長文読解を制する3ステップ",
             "1. **設問の先読み（Pre-reading questions）**: 本文を読む前に設問と選択肢のキーワード（年号、固有名詞、理由・原因）に目を通し、探索目標をセットする。\n"
             "2. **第1文スキャン法（Top-down scanning）**: 各パラグラフの第1文（主題文）を読み、文章全体の論理展開（問題提起 → 現状分析 → 課題 → 解決策）を把握する。\n"
             "3. **同義言い換え（Paraphrasing）の見極め**: 正解選択肢は本文の語句そのままでなく、類義語や受動構文で言い換えられている（例: meningkatkan ekspor → mendorong penjualan ke luar negeri）。")
        ],
        "problems": [
            {
                "q": "【読解パッセージ】\nSektor usaha mikro, kecil, dan menengah (UMKM) memegang peranan krusial sebagai tulang punggung perekonomian Indonesia. Berdasarkan data Kementerian Koperasi dan UKM, sektor ini menyerap lebih dari 97 persen total tenaga kerja nasional dan berkontribusi sekitar 61 persen terhadap Produk Domestik Bruto (PDB). Namun, tantangan utama yang dihadapi pelaku UMKM saat ini adalah rendahnya tingkat literasi digital dan keterbatasan akses pembiayaan formal dari perbankan.\n\nUntuk mengatasi hambatan tersebut, pemerintah meluncurkan Gerakan Nasional Bangga Buatan Indonesia (Gernas BBI) yang berfokus pada percepatan transformasi digital. Melalui program ini, jutaan pelaku usaha didorong untuk melakukan onboarding ke platform niaga elektronik (e-commerce). Selain itu, penyaluran Kredit Usaha Rakyat (KUR) berbunga rendah terus dioptimalkan guna memperkuat modal kerja dan meningkatkan daya saing produk lokal di pasar domestik maupun regional.\n\n**設問: Berdasarkan teks di atas, apa kendala utama yang menghambat perkembangan UMKM di Indonesia?**",
                "options": [
                    "A. Kurangnya tenaga kerja yang berminat bekerja di sektor UMKM.",
                    "B. Tingginya bunga pinjaman kredit usaha yang ditetapkan pemerintah.",
                    "C. Rendahnya pemahaman teknologi digital dan sulitnya akses permodalan perbankan.",
                    "D. Ketidakmampuan produk UMKM bersaing di platform e-commerce."
                ],
                "ans": "C. Rendahnya pemahaman teknologi digital dan sulitnya akses permodalan perbankan.",
                "expl": "第1段落末尾の「tantangan utama yang dihadapi pelaku UMKM saat ini adalah rendahnya tingkat literasi digital dan keterbatasan akses pembiayaan formal dari perbankan（デジタルリテラシーの低さと銀行からの公的融資アクセスの限界）」が、選択肢Cで同義に言い換えられています。"
            },
            {
                "q": "**設問: Apa tujuan utama diluncurkannya Gerakan Nasional Bangga Buatan Indonesia (Gernas BBI)?**",
                "options": [
                    "A. Menggantikan seluruh peran perbankan komersial dalam pembiayaan UMKM.",
                    "B. Mempercepat proses digitalisasi pelaku UMKM agar masuk ke ekosistem e-commerce.",
                    "C. Membatasi masuknya produk-produk impor di pasar swalayan modern.",
                    "D. Mengurangi ketergantungan tenaga kerja nasional pada sektor informal."
                ],
                "ans": "B. Mempercepat proses digitalisasi pelaku UMKM agar masuk ke ekosistem e-commerce.",
                "expl": "第2段落冒頭「pemerintah meluncurkan Gernas BBI yang berfokus pada percepatan transformasi digital... didorong untuk melakukan onboarding ke platform niaga elektronik」に合致するため、Bが正解です。"
            }
        ],
        "table": [
            ("tulang punggung perekonomian", "経済の屋台骨・バックボーン"),
            ("menyerap tenaga kerja", "労働力を吸収・雇用する"),
            ("Produk Domestik Bruto (PDB)", "国内総生産（GDP）"),
            ("pembiayaan formal", "公的金融機関からの融資"),
            ("niaga elektronik (e-commerce)", "電子商取引"),
            ("daya saing pasar", "市場競争力")
        ],
        "pro_tip": "設問の選択肢で「seluruh（すべて）」「hanya（〜のみ）」「selalu（常に）」などの極端な限定詞が含まれる選択肢は誤り（トラップ）である確率が高いので注意してください。"
    },
    {
        "filename": "05-inken-b-translation-jp-id.md",
        "title": "1405. 【技能検定B級対策】日イ翻訳：日本語特有の表現を自然なインドネシア語に移す",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "B級の記述試験（日イ翻訳）では、直訳すると意味不明になる日本語特有の「配慮・意図・受身・無生物主語」を、インドネシア語の自然な統語構造（S-V-O）へと転換する構文変換力が採点の決定打となります。",
        "theory": [
            ("日イ翻訳の3大処方箋",
             "1. **「〜ておく」「〜てしまう」の処理**: 事前準備の「ておく」は事前を表す副詞 terlebih dahulu / sebelumnya で処理。望ましくない「てしまう」は無意志接頭辞 ter- または不幸を表す副詞 sayangnya で表現。\n"
             "2. **日本語の受動文を能動文に再構築する**: 「新制度が導入された」→「Pemerintah memperkenalkan sistem baru（政府が新制度を導入した）」のように明確な能動態に直す方が自然な場合が多い。\n"
             "3. **「〜することになっている」などの制度表現**: sudah disepakati / dijadwalkan / diwajibkan を用いて、規程・合意事項として表現する。")
        ],
        "problems": [
            {
                "q": "【課題文1】来週の会議で使用する資料を、明日までに印刷しておいてください。",
                "options": [
                    "A. Tolong cetak dokumen yang akan digunakan dalam rapat minggu depan sebelum besok.",
                    "B. Harap mencetakkan terlebih dahulu dokumen untuk rapat minggu depan paling lambat besok.",
                    "C. Silakan Anda sudah mencetak materi rapat depan sebelum besok tiba.",
                    "D. Dokumen rapat minggu depan harus dicetak disimpan besok hari."
                ],
                "ans": "B. Harap mencetakkan terlebih dahulu dokumen untuk rapat minggu depan paling lambat besok.",
                "expl": "「印刷しておいてください」という事前準備のニュアンスは mencetakkan terlebih dahulu、期限の「明日までに」は paling lambat besok（遅くとも明日まで）と表現するのが最も格調高く自然なビジネス表現です。Aも通じますが「〜ておく」のニュアンスが弱く、Bが満点答案です。"
            },
            {
                "q": "【課題文2】技術革新の進展に伴い、人々の生活様式は急速に変化しつつある。",
                "options": [
                    "A. Seiring dengan kemajuan inovasi teknologi, pola hidup masyarakat sedang berubah secara pesat.",
                    "B. Bersama inovasi teknologi maju, hidup orang berubah banyak sekali.",
                    "C. Mengikuti teknologi baru, gaya masyarakat menjadi lain cepat.",
                    "D. Karena kemajuan inovasi teknologi membuat orang berganti hidup."
                ],
                "ans": "A. Seiring dengan kemajuan inovasi teknologi, pola hidup masyarakat sedang berubah secara pesat.",
                "expl": "「〜に伴い」は Seiring dengan...、「生活様式」は pola hidup、「急速に」は secara pesat と表現するのが定型です。"
            }
        ],
        "table": [
            ("〜に伴い、〜とともに", "seiring dengan / sejalan dengan"),
            ("〜に基づいて、〜に準拠して", "berdasarkan pada / sesuai dengan"),
            ("〜を目的として、〜のために", "bertujuan untuk / demi"),
            ("遅くとも〜までに", "paling lambat / selambat-lambatnya"),
            ("〜という点において", "dalam hal / dari segi")
        ],
        "pro_tip": "日本語の「〜をお願いします」をすべて tolong で訳すのではなく、ビジネス文書や公式な依頼では「Kami mohon agar...」「Harap...」を使い分けると加点対象になります。"
    },
    {
        "filename": "06-inken-b-translation-id-jp.md",
        "title": "1406. 【技能検定B級対策】イ日翻訳：抽象名詞と受動態を読みやすい日本語に翻訳する",
        "level": "技能検定B級（CEFR B1〜B2）",
        "intro": "B級のイ日翻訳セクションでは、インドネシア語特有の長い抽象名詞句（ke-...-an, peN-...-an）や受動態構文を、ぎこちない直訳（〜されることの増加、など）を脱して、自然でこなれた日本語のビジネス文章へ意訳・再構成する力が試されます。",
        "theory": [
            ("イ日翻訳のブラッシュアップ技法",
             "1. **抽象名詞を動詞として訳出する**: 「keberhasilan penerapan kebijakan ini（この政策の適用の成功）」→「この政策の適用が成功したこと / 政策が功を奏したこと」。\n"
             "2. **受動態を能動態や自発表現に変換する**: 「Langkah ini diambil oleh manajemen（この措置は経営陣によって取られた）」→「経営陣はこの措置を講じた」。\n"
             "3. **接続詞チャンクの論理関係を明確にする**: bahwa（〜ということ）、sehingga（その結果、〜）、meskipun demikian（それにもかかわらず）の流れを自然な日本語の接続詞で繋ぐ。")
        ],
        "problems": [
            {
                "q": "【課題文1】Peningkatan kualitas sumber daya manusia dipandang sebagai faktor penentu dalam mewujudkan visi Indonesia Emas 2045.",
                "options": [
                    "A. 人材の質の向上は、「黄金のインドネシア2045」ビジョンを実現する上での決定的な要因と見なされている。",
                    "B. 人間資源の品質が増加することは、黄金インドネシア2045の夢を現実に見る要因である。",
                    "C. 2045年の黄金のインドネシアを見るために、人材の質が高まることが決め手として見られている。",
                    "D. 人材品質のアップが、インドネシアゴールド2045年のビジョン現実に決定要因と見なされた。"
                ],
                "ans": "A. 人材の質の向上は、「黄金のインドネシア2045」ビジョンを実現する上での決定的な要因と見なされている。",
                "expl": "sumber daya manusia（人材）、faktor penentu（決定要因）、mewujudkan visi（ビジョンを実現する）という公式訳語を的確に配し、文末の dipandang sebagai（〜と見なされている）を自然に結んだAが完全な解答です。"
            },
            {
                "q": "【課題文2】Meskipun menghadapi ketidakpastian pasar global, kinerja ekspor nonmigas nasional tetap menunjukkan pertumbuhan yang menjanjikan.",
                "options": [
                    "A. 世界市場の不透明感に直面しているものの、国の非石油ガス輸出実績は依然として有望な成長を示している。",
                    "B. グローバル市場の不確かさに遭ったけれど、石油ガス以外の輸出の働きは前途有望に伸びている。",
                    "C. 不確実な市場のせいで、全国のノンミガス輸出は成長を約束された状態を保った。",
                    "D. 世界の市場が不確かでも、国内の輸出は石油以外も全部成長することが見せられている。"
                ],
                "ans": "A. 世界市場の不透明感に直面しているものの、国の非石油ガス輸出実績は依然として有望な成長を示している。",
                "expl": "ketidakpastian pasar global（世界市場の不透明感）、kinerja ekspor nonmigas（非石油ガス輸出実績）、pertumbuhan yang menjanjikan（有望な・期待できる成長）の専門用語が的確に日本語化されています。"
            }
        ],
        "table": [
            ("sumber daya manusia (SDM)", "人材・人的資源"),
            ("kinerja perusahaan", "企業業績・パフォーマンス"),
            ("ketidakpastian", "不透明感・不確実性"),
            ("menjanjikan", "前途有望な・期待が持てる"),
            ("faktor penentu", "決定打・決定要因"),
            ("tindak lanjut", "フォローアップ・事後措置")
        ],
        "pro_tip": "翻訳問題では、直訳のまま残すと不自然な「kata nomina（名詞句）」を、「〜すること」「〜する際」と動詞的にほぐして訳出すると、日本語の文章として格段に読みやすくなります。"
    },
    {
        "filename": "07-inken-a-complex-syntax.md",
        "title": "1407. 【技能検定A級対策】超難問構文解析：複々文・挿入句・倒置構文の骨格把握",
        "level": "技能検定A級（CEFR C1）",
        "intro": "最高峰の技能検定A級では、1文の中に3つ以上の従属節、挿入句、倒置構文（inversi）、関係代名詞 yang の多重修飾が組み込まれた100語以上の重文が出題されます。文構造を見失わずに「主語（S）と述語（P）の骨格」を瞬時に抽出する高度な統語分析スキルを伝授します。",
        "theory": [
            ("A級超難問構文を解剖する3つの視点",
             "1. **多重 yang の階層構造**: 先行詞がどれであるかを意味と文脈から階層化して見抜く。\n"
             "2. **倒置構文（Inversi: P-S構文）**: 強調のために述語や場所副詞句が文頭に置かれ、主語が後置される構造（例: Terletak di pusat kota adalah gedung megah itu）。\n"
             "3. **挿入句（Aposisi）の括弧外し**: カンマで挟まれた同格挿入句（— ... —）を一旦無視し、大骨格の S-P を把握する。")
        ],
        "problems": [
            {
                "q": "【難問構文解析】次の文の主幹となる「主語（S）」と「述語動詞（P）」の正しい組み合わせはどれか？\n\nKeberanian moral para tokoh pergerakan kemerdekaan yang tanpa pamrih mengorbankan kepentingan pribadi demi masa depan bangsa yang merdeka dan berdaulat, tercermin secara nyata dalam naskah historis ini.",
                "options": [
                    "A. S: para tokoh, P: mengorbankan",
                    "B. S: kepentingan pribadi, P: merdeka",
                    "C. S: Keberanian moral, P: tercermin",
                    "D. S: masa depan bangsa, P: berdaulat"
                ],
                "ans": "C. S: Keberanian moral, P: tercermin",
                "expl": "文頭の「Keberanian moral（道徳的勇気）」が文全体の主語（S）です。その後ろの「para tokoh... berdaulat」まではすべて yang 節を含む修飾部であり、文全体の述語（P）は末尾の「tercermin（反映されている・表れている）」です。"
            },
            {
                "q": "次の倒置構文（Inversi）において、意味上の真の「主語」はどれか？\n\nTak kalah pentingnya dalam merumuskan kebijakan fiskal berkelanjutan adalah komitmen bersama untuk memberantas kebocoran anggaran.",
                "options": [
                    "A. kebijakan fiskal", "B. kebocoran anggaran", "C. komitmen bersama", "D. pentingnya"
                ],
                "ans": "C. komitmen bersama",
                "expl": "文頭の「Tak kalah pentingnya dalam merumuskan...」は述語（P）としての形容詞句の強調倒置です。真の主語（S）は後置された「komitmen bersama untuk memberantas kebocoran anggaran（予算漏洩を撲滅するための共通のコミットメント）」です。"
            }
        ],
        "table": [
            ("Inversi（倒置構文）", "P - S（述語が文頭、主語が後置される）", "Penting untuk dicatat bahwa..."),
            ("Aposisi（同格句）", "S, [同格説明], P", "Presiden, selaku kepala negara, menyatakan..."),
            ("Yang 多重修飾", "先行詞 + yang (1) + yang (2)", "Kebijakan yang diambil yang berdampak..."),
            ("Klausa Adverbial", "接続詞 + S + P, S + P", "Meskipun sempat terkendala, proyek itu tetap...")
        ],
        "pro_tip": "A級の読解では、1文が4〜5行に及ぶ長文に出会ったら、まず接続詞とカンマ、yang に印をつけ、「誰が・何を・どうした」という骨格（S-P-O）だけを抜き出して読む訓練を重ねてください。"
    },
    {
        "filename": "08-inken-a-idioms-peribahasa.md",
        "title": "1408. 【技能検定A級対策】ことわざ（Peribahasa）と慣用表現：頻出50選の文脈運用",
        "level": "技能検定A級（CEFR C1）",
        "intro": "技能検定A級の筆記試験および面接試験において、合否の決定打となるのが伝統的なことわざ（Peribahasa）や高度なイディオム（Ungkapan Idiomatis）の正確な理解と運用です。単なる暗記ではなく、社説や政治スピーチでどのような論証文脈で引用されるかを詳説します。",
        "theory": [
            ("A級頻出 Peribahasa の4大テーマ",
             "1. **協調・団結・相互扶助**: Berat sama dipikul, ringan sama dijinjing / Bersatu kita teguh, bercerai kita runtuh.\n"
             "2. **因果応報・身から出た錆**: Menepuk air di dulang, terpercik muka sendiri / Lempar batu sembunyi tangan.\n"
             "3. **危機管理・先見の明**: Sedia payung sebelum hujan / Air tenang menghanyutkan.\n"
             "4. **適応・郷に入っては郷に従え**: Di mana bumi dipijak, di situ langit dijunjung.")
        ],
        "problems": [
            {
                "q": "Seorang pejabat publik yang bersikap manis di hadapan media namun diam-diam menyalahgunakan wewenang diibaratkan seperti [...].",
                "options": [
                    "A. musang berbulu domba",
                    "B. kancil yang cerdik",
                    "C. kerbau dicucuk hidung",
                    "D. burung dalam sangkar"
                ],
                "ans": "A. musang berbulu domba",
                "expl": "外面は親切そうに見せかけて心に悪意を秘めている人物（羊の皮を被った狼）を、インドネシア語では「musang berbulu domba（羊の毛皮を着たジャコウネコ）」と表現します。"
            },
            {
                "q": "Para pendiri bangsa selalu mengingatkan agar kita senantiasa menjaga persatuan, karena [...].",
                "options": [
                    "A. nasi sudah menjadi bubur",
                    "B. bersatu kita teguh, bercerai kita runtuh",
                    "C. ada asap ada api",
                    "D. pagar makan tanaman"
                ],
                "ans": "B. bersatu kita teguh, bercerai kita runtuh",
                "expl": "「団結すれば強固となり、分裂すれば崩壊する」という民族団結の最も有名な国是ことわざです。"
            },
            {
                "q": "Orang yang tampak pendiam namun ternyata menyimpan kecerdasan luar biasa dan pemikiran mendalam sering digambarkan dengan pepatah [...].",
                "options": [
                    "A. tong kosong nyaring bunyinya",
                    "B. air tenang menghanyutkan",
                    "C. bagai api dalam sekam",
                    "D. menangguk di air keruh"
                ],
                "ans": "B. air tenang menghanyutkan",
                "expl": "物静かだが奥底に計り知れない力量を秘めている人物（能ある鷹は爪を隠す）は「air tenang menghanyutkan（静かな水は人を押し流す）」と表現します。"
            }
        ],
        "table": [
            ("Lempar batu sembunyi tangan", "自ら悪事を働きながら犯行を隠蔽する（卑劣な責任逃れ）"),
            ("Pagar makan tanaman", "信頼して守りを任せた身内が裏切って横領・侵害する"),
            ("Tong kosong nyaring bunyinya", "中身のない空っぽの人間ほど大声で自慢し騒ぎ立てる"),
            ("Bagai air di daun talas", "定見がなく日和見主義で信念がコロコロ変わる人物"),
            ("Gali lubang tutup lubang", "借金を返すために別の借金を重ねる（自転車操業）")
        ],
        "pro_tip": "ことわざ問題は、選択肢を字面通りに直訳するのではなく、「教訓・比喩される人間類型」とセットで脳内データベース化しておくことが得点の秘訣です。"
    },
    {
        "filename": "09-inken-a-editorial-reading.md",
        "title": "1409. 【技能検定A級対策】社説・論説文の超長文読解：筆者の主張と論理の展開",
        "level": "技能検定A級（CEFR C1）",
        "intro": "A級の読解試験では、Kompas紙やTempo誌の社説（Tajuk Rencana / Opini）から、800〜1,000語規模の最高峰の論説文が出題されます。高度な政治経済・憲法論争・地政学的対立を論じた文章から、筆者の隠されたスタンス（アティチュード）を的確に読み取るクリティカル・リーディングの手法を伝授します。",
        "theory": [
            ("社説（Tajuk Rencana）読解の論理フレームワーク",
             "1. **導入（Tesis / Premis Awal）**: 最近の時事ニュースや法改正の事実提示。\n"
             "2. **対立視点（Antitesis）**: 政府見解に対する野党・NGO・市民社会からの批判や副作用の指摘。\n"
             "3. **論拠の補強（Argumentasi）**: 統計データ、憲法裁判所判例、歴史的先例の引用。\n"
             "4. **結論・提言（Sintesis / Rekomendasi）**: 社説特有の提言動詞（sepatutnya, seyogianya, mutlak diperlukan）に着目する。")
        ],
        "problems": [
            {
                "q": "【社説抜粋】\nKebijakan hilirisasi mineral yang digadang-gadang sebagai lokomotif pertumbuhan ekonomi baru patut diapresiasi dari sisi peningkatan penerimaan ekspor olahan. Kendati demikian, euforia angka-angka makroekonomi tidak boleh membutakan mata pembuat kebijakan terhadap dampak sosial-ekologis yang kian menganga di daerah lingkar tambang. Konflik agraria dengan masyarakat adat, kerusakan ekosistem laut akibat pembuangan tailing, serta minimnya serapan tenaga kerja lokal merupakan noktah hitam yang menodai narasi keberhasilan tersebut. Sudah seyogianya pemerintah melakukan evaluasi menyeluruh dan menegakkan hukum lingkungan secara tanpa pandang bulu.\n\n**設問: Berdasarkan petikan tajuk rencana di atas, bagaimana sikap utama penulis terhadap kebijakan hilirisasi mineral?**",
                "options": [
                    "A. Menolak secara mutlak seluruh proyek hilirisasi tambang karena merusak lingkungan.",
                    "B. Mendukung penuh tanpa catatan karena berhasil mendongkrak penerimaan ekspor negara.",
                    "C. Mengapresiasi capaian ekonominya namun mendesak evaluasi ketat atas dampak sosial dan lingkungan.",
                    "D. Menyalahkan masyarakat adat yang menentang pembangunan fasilitas pengolahan mineral."
                ],
                "ans": "C. Mengapresiasi capaian ekonominya namun mendesak evaluasi ketat atas dampak sosial dan lingkungan.",
                "expl": "筆者は冒頭で輸出増加の経済成果を評価（patut diapresiasi）しつつも、「Kendati demikian（しかしながら）」以下で環境汚染や先住民族との衝突などの黒点（noktah hitam）を挙げ、包括的評価と法執行（evaluasi menyeluruh dan penegakan hukum）を提言しているため、Cが完全に合致する客観的要約です。"
            }
        ],
        "table": [
            ("digadang-gadang", "大いに期待・嘱望されている"),
            ("tanpa pandang bulu", "えこひいきなく・公平無私に"),
            ("noktah hitam", "汚点・黒点・汚名"),
            ("seyogianya / sepatutnya", "〜するのが至当・当然である（提言詞）"),
            ("menganga", "口を開けている・深刻化している（dampak menganga）")
        ],
        "pro_tip": "社説の核心的メッセージは、逆接接続詞（kendati demikian, namun, akan tetapi）の後ろ、および提言副詞（seyogianya, hendaknya, patut）を含む文に集約されています。"
    },
    {
        "filename": "10-inken-a-high-level-essay.md",
        "title": "1410. 【技能検定A級対策】自由記述・エッセイ作成：説得力ある小論文の構成法",
        "level": "技能検定A級（CEFR C1）",
        "intro": "技能検定A級の二次試験（記述・面接）では、与えられた時事テーマ（少子高齢化、脱炭素、AI倫理、民主主義の課題など）について、200〜300語の説得力ある論述エッセイを即座に構築する力が求められます。論理的破綻を防ぎ高得点を叩き出す「PREP法＋論理標識（Signpost words）」のテンプレートを完全公開します。",
        "theory": [
            ("インドネシア語エッセイの黄金構成（PREP法）",
             "1. **Point（主張・テーゼ）**: 文頭で自らの立場を明快に宣言（Menurut pandangan saya, ... merupakan...）。\n"
             "2. **Reason（理由・根拠）**: 主張を裏付ける論理的理由（Hal ini didasarkan pada dua alasan fundamental...）。\n"
             "3. **Example / Evidence（具体例・データ）**: 政策、実例、統計の提示（Sebagai contoh konkret,...）。\n"
             "4. **Point Restatement（結論・提言）**: 主張の再確認と今後の提言（Oleh karena itu, langkah mitigasi yang komprehensif mutlak diperlukan...）。"),
            ("格調を高める論理標識（Wacana Penanda）",
             "- **並列・列挙**: Pertama-tama, di samping itu, lebih lanjut lagi.\n"
             "- **逆接・対比**: Di sisi lain, sebaliknya, bertolak belakang dengan hal tersebut.\n"
             "- **因果・帰結**: Akibatnya, dengan demikian, sebagai konsekuensi logis.")
        ],
        "problems": [
            {
                "q": "【小論文模範解答モデル】テーマ: 「Transisi Energi Hijau di Indonesia（インドネシアにおけるグリーンエネルギー転換）」",
                "options": [
                    "A. 模範エッセイ構成の確認",
                    "B. 模範エッセイの論理展開の分析",
                    "C. 模範エッセイの接続語句の確認",
                    "D. 模範エッセイの語彙レベルの確認"
                ],
                "ans": "A. 模範エッセイ構成の確認",
                "expl": "以下のモデルエッセイ（約220語）は、A級満点基準を満たす格調高い文章構成の見本です。\n\n**[Transisi Energi Hijau: Antara Peluang dan Tantangan]**\nTransisi menuju energi hijau merupakan keniscayaan historis yang mutlak dihadapi Indonesia guna mencapai target Net Zero Emission pada tahun 2060. Kebijakan ini tidak hanya krusial untuk memitigasi dampak krisis iklim global, tetapi juga membuka peluang emas bagi terciptanya lapangan kerja hijau (green jobs) baru.\n\nNamun demikian, proses dekarbonisasi ini menghadapi tantangan struktural yang tidak mudah. Di satu sisi, ketergantungan ekonomi pada industri batu bara masih sangat tinggi, baik sebagai sumber penerimaan devisa maupun penopang ketahanan listrik domestik. Di sisi lain, pembangunan infrastruktur energi terbarukan—seperti pembangkit listrik tenaga surya dan panas bumi—memerlukan investasi awal yang sangat masif serta transfer teknologi mutakhir.\n\nOleh sebab itu, transisi energi tidak boleh dilakukan secara tergesa-gesa tanpa memperhatikan keadilan sosial bagi para pekerja di sektor fosil. Pemerintah seyogianya menerapkan strategi 'transisi yang berkeadilan' (just transition) melalui pemberian insentif fiskal bagi investor hijau sekaligus program pelatihan vokasi bagi tenaga kerja lokal. Dengan peta jalan yang komprehensif, Indonesia dapat melangkah maju menjadi pelopor ekonomi hijau di kawasan Asia Tenggara."
            }
        ],
        "table": [
            ("keniscayaan historis", "歴史的必然（避けて通れない運命）"),
            ("dekarbonisasi", "脱炭素化"),
            ("just transition", "公正な移行（労働者に配慮した転換）"),
            ("insentif fiskal", "財政・税制上の優遇措置"),
            ("peta jalan (roadmap)", "工程表・ロードマップ")
        ],
        "pro_tip": "エッセイを書く際は、主観的な感情論（Saya rasa, Menurut saya saja）を避け、「Fakta menunjukkan bahwa...」「Data empiris membuktikan bahwa...」のように客観的な論証文体を維持することが合格の秘訣です。"
    }
]

def generate_markdown(a):
    theory_content = ""
    for title, desc in a["theory"]:
        theory_content += f"""### {title}
{desc}

"""

    problem_items = ""
    for idx, p in enumerate(a["problems"], 1):
        opts_str = "\n".join([f"- {opt}" for opt in p["options"]])
        problem_items += f"""#### 第{idx}問
{p['q']}

{opts_str}

<details>
<summary>正解と解説を見る</summary>

**正解**: 「**{p['ans']}**」

**解説**:
{p['expl']}
</details>

---

"""

    table_rows = ""
    table_header = "| 項目・表現 | 解説・ニュアンス・共起表現 |\n| :--- | :--- |\n"
    if a["table"] and len(a["table"][0]) == 4:
        table_header = "| 表現A（接尾辞-i等） | 意味・用法 | 表現B（接尾辞-kan等） | 意味・用法 |\n| :--- | :--- | :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} | **{row[2]}** | {row[3]} |\n"
    elif a["table"] and len(a["table"][0]) == 3:
        table_header = "| 誤用例 | 正用例 | 文法解説 |\n| :--- | :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | **{row[1]}** | {row[2]} |\n"
    else:
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "インドネシア語技能検定・UKBI対策シリーズ。{a['title']}の出題傾向、解法セオリー、実戦想定問題、詳細解説まで徹底指導。"
---

<div class="category-badge">検定・UKBI実戦対策</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 試験の傾向と出題意図

{a['intro']}

---

## 2. 攻略フレームワーク・解法セオリー

{theory_content}

---

## 3. 実戦想定問題と詳細解説

本番試験と同等レベルのオリジナル想定問題です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}

---

## 4. 重要語彙・構文対比テーブル

本セクションのテーマに関連する最重要語彙・成句の対比一覧です。

{table_header}{table_rows}

---

## 5. 合格者の着眼点・プロのアドバイス

> [!TIP]
> **合格のためのワンポイント・アドバイス**:
> {a['pro_tip']}

---

## 6. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "exam-advanced")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
