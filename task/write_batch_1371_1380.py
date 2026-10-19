# -*- coding: utf-8 -*-
"""
セクション33 第3バッチ (1371-1380) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾
"""

import os

articles = [
    {
        "filename": "121-root-naik.md",
        "title": "1371. 語根 naik の全派生語図鑑（menaikkan, kenaikan, menaiki, menaik）",
        "root": "naik",
        "core_meaning": "上がる、登る、乗る、増大する、昇進する",
        "explanation": "語根 naik は、空間的な上方への移動、乗り物への搭乗、価格・数量・地位の上昇を包括する基本動作語根です。自動詞（naik）から人為的引き上げ（menaikkan）、場所や乗り物への能動的搭乗（menaiki）、名詞化された上昇・値上げ・昇進（kenaikan）まで、極めて高い使用頻度を誇ります。",
        "matrix": [
            ("naik", "語根", "自動詞", "上がる、登る、乗る、昇進する", "Harga bahan pokok biasanya naik menjelang hari raya Idulfitri."),
            ("menaikkan", "meN- -kan", "他動詞", "上げる、引き上げる、高める、搭乗させる", "Bank sentral memutuskan untuk menaikkan suku bunga acuan."),
            ("menaiki", "meN- -i", "他動詞", "〜に登る、〜に乗る（搭乗・登頂する）", "Para wisatawan menaiki tangga curam untuk mencapai puncak candi."),
            ("kenaikan", "ke- -an", "名詞", "上昇、値上げ、昇給、昇格、進級", "Kenaikan gaji karyawan akan disesuaikan dengan tingkat inflasi tahunan."),
            ("menaik", "meN-", "自動詞・形容詞", "上昇傾向にある、上向きの", "Kurva penjualan menunjukkan tren yang menaik pada kuartal ketiga."),
            ("penaikan", "peN- -an", "名詞", "引き上げ作業、値上げプロセス", "Penaikan tarif jalan tol memicu penolakan dari asosiasi logistik."),
            ("naik daun", "frasa", "慣用語・形容詞", "人気急上昇中の、脚光を浴びている", "Aktor muda berbakat itu sedang naik daun di industri perfilman nasional.")
        ],
        "details": [
            ("naik", "自動詞", "ナイック",
             "主語が自力で「上へ移動する」「乗り物に乗る」「数量や数値が増大する」基本自動詞です。",
             "naik kereta api（電車に乗る）, naik pangkat（昇進する）, naik kelas（進級する）, naik pitam（激怒する・カッとなる）",
             "Setiap pagi ribuan komuter naik kereta rel listrik menuju pusat kota Jakarta.",
             "毎朝、何千人もの通勤者がジャカルタ中心部へ向かう近郊電車に乗る。"),
            ("menaikkan", "他動詞", "ムナイッカン",
             "主語が外的な対象を「引き上げる・高める・値上げする」使役動作を表します。",
             "menaikkan harga（値上げする）, menaikkan bendera（国旗を掲揚する）, menaikkan standar（基準を引き上げる）",
             "Perusahaan terpaksa menaikkan harga jual produk akibat lonjakan biaya bahan baku.",
             "企業は原材料費の高騰を受けて、製品の販売価格を引き上げざるを得なかった。"),
            ("menaiki", "他動詞", "ムナイキ",
             "対象となる場所や乗り物に「登る・乗っかる」動作で、目的語に直接場所・対象をとります。",
             "menaiki tangga（階段を登る）, menaiki kuda（馬に乗る）, menaiki bukit（丘を登る）",
             "Wisatawan dilarang menaiki struktur batu candi demi menjaga kelestarian cagar budaya.",
             "観光客は文化財の保護のため、寺院の石造構造物に登ることを禁じられている。"),
            ("kenaikan", "名詞", "クナイカン",
             "物価、気温、給与、地位などが「上昇すること・高まった状態」を指す抽象名詞です。",
             "kenaikan harga beras（米の値上がり）, kenaikan pangkat（昇進・昇格）, kenaikan upah minimum（最低賃金の引き上げ）",
             "Pemerintah berupaya meredam lonjakan kenaikan harga bahan pokok jelang Lebaran.",
             "政府はレバラン（断食明け大祭）を前に、生活必需品価格の急激な上昇を抑えようと努めている。")
        ],
        "dialogue": {
            "title": "物価上昇と生活防衛に関する同僚の会話",
            "lines": [
                ("Rian", "Apakah kamu memperhatikan bahwa harga bahan makanan di pasar tradisional mulai naik lagi?"),
                ("Dewi", "Iya, betul. Kenaikan harga beras dan minyak goreng terasa cukup membebani pengeluaran bulanan."),
                ("Rian", "Pemerintah sebenarnya sudah berupaya menaikkan pasokan beras subsidi untuk menstabilkan pasar."),
                ("Dewi", "Semoga langkah itu berhasil. Jika tidak, biaya transportasi umum juga bisa ikut terdorong menaik.")
            ]
        },
        "grammar_points": [
            ("menaikkan vs menaiki", "menaikkan は使役（〜を上へ引き上げる、値上げする）で目的語は引き上げられる対象（harga, standar）。一方 menaiki は場所・対象指向（〜の上に登る、乗る）で目的語は登られる場所や乗り物（tangga, kuda, perahu）。"),
            ("naik の比喩表現・慣用句", "naik pitam（頭に血が上る＝激怒する）、naik daun（人気がうなぎ登りになる）、naik banding（控訴・上訴する）、naik darah（高血圧・怒る）など感情や社会的手続きの熟語が豊富。")
        ],
        "quizzes": [
            {
                "q": "「中央銀行はインフレを抑制するために金利を引き上げた」の空欄に入る適切な動詞は？\nBank sentral telah [...] suku bunga demi menekan laju inflasi.",
                "options": ["A. menaiki", "B. menaikkan", "C. kenaikan", "D. ternaik"],
                "ans": "B. menaikkan",
                "expl": "金利（suku bunga）という対象を「引き上げる」使役動作なので他動詞 menaikkan が正解です。menaiki は「〜に乗る・登る」、kenaikan は名詞（上昇）です。"
            },
            {
                "q": "次のうち、「人気急上昇中である」ことを意味する慣用表現はどれか？",
                "options": ["A. naik pitam", "B. naik darah", "C. naik daun", "D. naik kelas"],
                "ans": "C. naik daun",
                "expl": "「naik daun」はタレントや商品などが「脚光を浴びて人気絶頂にある」ことを表す慣用句です。naik pitam/naik darah は「激怒する」、naik kelas は「進級する」です。"
            },
            {
                "q": "「観光客は急な階段を登って塔の頂上に達した」の空欄に入る適切な動詞は？\nWisatawan [...] tangga curam untuk mencapai puncak menara.",
                "options": ["A. menaiki", "B. menaikkan", "C. penaikan", "D. berenaik"],
                "ans": "A. menaiki",
                "expl": "階段（tangga）という場所を対象として「登る」動作なので、接尾辞 -i を伴う menaiki が適切です。"
            }
        ],
        "peribahasa": {
            "quote": "Bagaikan naik tangga, setapak demi setapak.",
            "meaning": "階段を一段ずつ登るように、何事も着実に一歩ずつ進めるべきであるという教訓。"
        }
    },
    {
        "filename": "122-root-jatuh.md",
        "title": "1372. 語根 jatuh の全派生語図鑑（menjatuhkan, kejatuhan, penjatuhan, terjatuh）",
        "root": "jatuh",
        "core_meaning": "落ちる、落下する、失脚する、倒れる、〜になる（日付など）",
        "explanation": "語根 jatuh は、重力による物理的な落下や転倒のみならず、政権の失脚、判決の言い渡し（menjatuhkan hukuman）、期限の到来（jatuh tempo）、恋に落ちること（jatuh cinta）まで、劇的な状態変化を司る基本語根です。",
        "matrix": [
            ("jatuh", "語根", "自動詞", "落ちる、転ぶ、失脚する、該当する", "Daun-daun kering jatuh berguguran saat musim kemarau tiba."),
            ("menjatuhkan", "meN- -kan", "他動詞", "落とす、下す、倒す、宣告する", "Hakim menjatuhkan vonis lima tahun penjara kepada terdakwa korupsi."),
            ("kejatuhan", "ke- -an", "名詞・被災動詞", "落下に見舞われる、失脚、政権崩壊", "Kejatuhan rezim Orde Baru pada tahun 1998 menandai era Reformasi."),
            ("penjatuhan", "peN- -an", "名詞", "言い渡し、宣告、処罰執行プロセス", "Penjatuhan sanksi administratif bertujuan memberikan efek jera."),
            ("terjatuh", "ter-", "無意志自動詞", "うっかり転ぶ、誤って落ちる", "Anak kecil itu menangis kencang setelah terjatuh dari sepedanya."),
            ("jatuh tempo", "frasa", "成句・動詞", "期日が到来する、支払期限になる", "Tagihan listrik bulanan akan jatuh tempo pada tanggal dua puluh."),
            ("jatuh cinta", "frasa", "成句・動詞", "恋に落ちる、一目惚れする", "Dia langsung jatuh cinta pada pandangan pertama saat bertemu di kampus.")
        ],
        "details": [
            ("jatuh", "自動詞", "ジャトゥ",
             "重力で下へ落下する、病気になる（jatuh sakit）、期限が来る（jatuh tempo）など多義的な基本動詞です。",
             "jatuh tempo（満期になる・期限が来る）, jatuh bangun（七転び八起き）, jatuh cinta（恋に落ちる）, jatuh miskin（破産して貧乏になる）",
             "Banyak pelaku usaha kecil harus jatuh bangun sebelum meraih kesuksesan.",
             "多くの零細起業家は成功を収める前に何度も七転び八起きの苦難を経験しなければならない。"),
            ("menjatuhkan", "他動詞", "ムンジャトゥッカン",
             "物を故意または不注意で「落とす」、敵や政権を「打倒する」、刑罰を「下す・言い渡す」使役動詞です。",
             "menjatuhkan hukuman（判決を下す）, menjatuhkan mental（精神を挫く）, menjatuhkan pilihan（選択・決定する）",
             "Majelis hakim akhirnya menjatuhkan putusan bersalah kepada pelaku penipuan investasi.",
             "裁判長団は最終的に投資詐欺の犯人に対して有罪判決を下した。"),
            ("kejatuhan", "名詞・動詞", "クジャトゥハン",
             "王朝や政権の「崩壊・失脚」、あるいは「〜が落ちてきて被災する（例: kejatuhan kelapa = ヤシの実が直撃する）」を表します。",
             "kejatuhan pemerintah（政府の失脚・倒閣）, kejatuhan nilai mata uang（通貨価値の暴落）",
             "Krisis moneter hebat mempercepat kejatuhan kekuasaan presiden saat itu.",
             "深刻な通貨危機が当時の大統領権力の失脚を早めた。"),
            ("terjatuh", "無意志動詞", "トゥルジャトゥ",
             "本人の意志に反して足をとられたりバランスを崩して「思わず転倒する・落っこちる」状態です。",
             "terjatuh ke jurang（谷底に転落する）, terpeleset dan terjatuh（滑って転ぶ）",
             "Pengendara motor itu bersyukur tidak mengalami luka parah meski terjatuh di jalan licin.",
             "そのバイク運転手は濡れて滑りやすい道路で転倒したものの、重傷を負わずに済んだことを感謝した。")
        ],
        "dialogue": {
            "title": "支払い期日と資金繰りに関する相談",
            "lines": [
                ("Agus", "Sari, jangan lupa bahwa invoice sewa kantor kita akan jatuh tempo akhir pekan ini."),
                ("Sari", "Tenang saja, Mas. Bagian keuangan sudah menyiapkan dana agar kita tidak terkena denda keterlambatan."),
                ("Agus", "Baguslah. Reputasi bisnis kita bisa jatuh jika sering telat membayar kewajiban."),
                ("Sari", "Betul sekali. Kepercayaan klien adalah aset yang tidak boleh kita jatuhkan begitu saja.")
            ]
        },
        "grammar_points": [
            ("jatuh の慣用句体系", "jatuh hati（心惹かれる）、jatuh nilai（価値が下落する）、menjatuhkan talak（離婚宣告する）、menjatuhkan vonis（判決宣告）など、法律から恋愛まで決定的な動詞句を形成。"),
            ("kejatuhan の二重機能", "名詞「失脚・崩壊」として使われるほか、ke-...-an 被災構文として「Saya kejatuhan mangga（頭にマンゴーが落ちてきた）」のように不意の被害を表す。")
        ],
        "quizzes": [
            {
                "q": "「支払期限が切れる・満期になる」を意味するインドネシア語の成句はどれか？",
                "options": ["A. jatuh hati", "B. jatuh tempo", "C. jatuh cinta", "D. jatuh bangun"],
                "ans": "B. jatuh tempo",
                "expl": "支払いや契約などの満期・期限到来は「jatuh tempo」と言います。jatuh bangun は「浮沈・七転び八起き」、jatuh hati は「惚れ込む」です。"
            },
            {
                "q": "「裁判官は汚職容疑者に対して重い刑罰を下した」の空欄に入る適切な動詞は？\nHakim [...] sanksi berat kepada tersangka kasus korupsi.",
                "options": ["A. terjatuh", "B. kejatuhan", "C. menjatuhkan", "D. berjatuhan"],
                "ans": "C. menjatuhkan",
                "expl": "刑罰や判決を「下す・科す」は使役他動詞 menjatuhkan hukuman / sanksi と表現します。"
            },
            {
                "q": "「床が濡れて滑りやすかったため、彼女は思わず転んでしまった」の空欄に入る動詞は？\nLantai licin membuat dia kehilangan keseimbangan lalu [...].",
                "options": ["A. terjatuh", "B. menjatuhkan", "C. penjatuhan", "D. berjatuh"],
                "ans": "A. terjatuh",
                "expl": "故意ではなく事故や不注意で「うっかり転倒した」無意志動作を表すため、接頭辞 ter- を伴う terjatuh が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Sudah jatuh tertimpa tangga pula.",
            "meaning": "転んだ上に階段が倒れかかってくる＝「泣きっ面に蜂」「一難去ってまた一難」の災難を表す最も有名なことわざ。"
        }
    },
    {
        "filename": "123-root-bangkit.md",
        "title": "1373. 語根 bangkit の全派生語図鑑（membangkitkan, kebangkitan, pembangkit, berbangkit）",
        "root": "bangkit",
        "core_meaning": "立ち上がる、起き上がる、奮起する、覚醒する、発電する",
        "explanation": "語根 bangkit は、横たわった状態や屈服した状態から「力強く身を起こす・復活する」コアを持ちます。精神的な奮起（kebangkitan nasional）、情熱や食欲の喚起（membangkitkan selera）、物理的な電力エネルギーの生成（pembangkit listrik）まで、生命力と再生の息吹を象徴する重要語根です。",
        "matrix": [
            ("bangkit", "語根", "自動詞", "起き上がる、立ち直る、再起する", "Setelah mengalami kegagalan beruntun, atlet itu bangkit dan meraih medali."),
            ("membangkitkan", "meN- -kan", "他動詞", "呼び起こす、奮起させる、発電する、喚起する", "Pidato inspiratif presiden membangkitkan semangat juang rakyat."),
            ("kebangkitan", "ke- -an", "名詞", "復活、復興、覚醒、民族的覚醒", "Hari Kebangkitan Nasional diperingati setiap tanggal dua puluh Mei."),
            ("pembangkit", "peN-", "名詞", "発電機、発電所、動因、誘発装置", "Indonesia sedang memperbanyak pembangunan pembangkit listrik tenaga surya."),
            ("berbangkit", "ber-", "自動詞", "生じる、湧き起こる、再発する", "Perasaan curiga mulai berbangkit di antara rekan kerja."),
            ("terbangkitkan", "ter- -kan", "受動態・可能動詞", "呼び起こされる、奮起させられ得る", "Semangat gotong royong warga kembali terbangkitkan pasca bencana."),
            ("kebangkitan ekonomi", "frasa", "名詞句", "経済復興、景気回復", "Sektor pariwisata menjadi motor penggerak kebangkitan ekonomi pulau Bali.")
        ],
        "details": [
            ("bangkit", "自動詞", "バンキット",
             "病床や挫折から「立ち直る・起き上がる」、情念が「湧き上がる」ことを表す基本動詞です。",
             "bangkit dari keterpurukan（どん底から立ち上がる）, bangkit berdiri（スクッと立ち上がる）, bangkit kembali（再起する）",
             "Masyarakat korban gempa segera bangkit menata kembali kehidupan mereka.",
             "地震被災地の住民たちは速やかに立ち上がり、自分たちの生活を立て直した。"),
            ("membangkitkan", "他動詞", "ムンバンキッカン",
             "人々の意欲や好奇心を「刺激して呼び起こす」、あるいは電気エネルギーを「発生させる」動作です。",
             "membangkitkan selera makan（食欲をそそる）, membangkitkan kenangan lama（昔の記憶を呼び覚ます）, membangkitkan rasa percaya diri（自信を湧き立たせる）",
             "Aroma rempah-rempah yang harum dari dapur berhasil membangkitkan selera makan seluruh keluarga.",
             "台所から漂うスパイスの芳しい香りが、家族全員の食欲をそそった。"),
            ("kebangkitan", "名詞", "クバンキタン",
             "民族や国家の歴史的目覚め、文化・経済の「復興・ルネサンス」を指す格調高い名詞です。",
             "Hari Kebangkitan Nasional（民族覚醒記念日・5月20日）, kebangkitan industri kreatif（クリエイティブ産業の勃興）",
             "Tahun 1908 dicatat dalam sejarah sebagai tonggak awal kebangkitan nasional bangsa Indonesia.",
             "1908年はインドネシア民族の覚醒の初期の里程標として歴史に記録されている。"),
            ("pembangkit", "名詞", "プンバンキット",
             "電気などのエネルギーを生み出す施設・設備（発電所）を指す工業・インフラ用語です。",
             "PLN（国営電力会社）, pembangkit listrik tenaga air / PLTA（水力発電所）, pembangkit listrik tenaga uap / PLTU（石炭火力発電所）",
             "Pemerintah berencana memensiunkan dini beberapa pembangkit listrik berbahan bakar batu bara.",
             "政府は石炭を燃料とするいくつかの火力発電所を早期退役させる計画を立てている。")
        ],
        "dialogue": {
            "title": "再生可能エネルギーへの転換と産業の復興",
            "lines": [
                ("Ilham", "Daerah kita memiliki potensi panas bumi yang besar untuk membangun pembangkit listrik ramah lingkungan."),
                ("Nita", "Betul, Pak. Transisi energi hijau ini sekaligus bisa membangkitkan peluang kerja baru bagi pemuda lokal."),
                ("Ilham", "Kita harus bangkit meninggalkan ketergantungan pada energi fosil yang mencemari lingkungan."),
                ("Nita", "Saya yakin langkah ini akan menjadi momentum kebangkitan ekonomi hijau di wilayah kita.")
            ]
        },
        "grammar_points": [
            ("pembangkit listrik の略語体系", "インドネシアの電力分野では PLTA (air:水力), PLTU (uap:火力), PLTS (surya:太陽光), PLTP (panas bumi:地熱), PLTN (nuklir:原子力) と略語が標準化されている。"),
            ("bangkit vs bangun", "bangun は毎朝「眠りから目を覚ます」「建築する」日常語。bangkit は屈辱や苦境から「再起する」「奮い立つ」強い力感と歴史的・精神的文脈を帯びる。")
        ],
        "quizzes": [
            {
                "q": "毎年5月20日に祝われる、インドネシアの歴史的な祝祭日はどれか？",
                "options": ["A. Hari Pahlawan", "B. Hari Kebangkitan Nasional", "C. Hari Kemerdekaan", "D. Hari Kesaktian Pancasila"],
                "ans": "B. Hari Kebangkitan Nasional",
                "expl": "1908年の初期民族主義団体「ブディ・ウトモ」設立を記念する「Hari Kebangkitan Nasional（民族覚醒記念日）」です。"
            },
            {
                "q": "「太陽光発電所」を意味する略語として正しいものはどれか？",
                "options": ["A. PLTA", "B. PLTU", "C. PLTS", "D. PLTP"],
                "ans": "C. PLTS",
                "expl": "Pembangkit Listrik Tenaga Surya の頭文字をとって「PLTS」と略します。PLTAは水力、PLTUは石炭火力、PLTPは地熱です。"
            },
            {
                "q": "「美しい音楽が彼の幼少期の思い出を呼び起こした」の空欄に入る動詞は？\nAlunan musik merdu itu [...] kenangan indah masa kecilnya.",
                "options": ["A. membangkitkan", "B. kebangkitan", "C. pembangkit", "D. terbangkit"],
                "ans": "A. membangkitkan",
                "expl": "記憶や感情を「呼び覚ます・喚起する」使役動作を表すため、他動詞 membangkitkan が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Kalah jadi abu, menang jadi arang; lebih baik bangkit bersama.",
            "meaning": "争って負ければ灰、勝っても炭（共倒れ）。反目するのではなく共に立ち上がって協力するのが最善であるという教え。"
        }
    },
    {
        "filename": "124-root-runtuh.md",
        "title": "1374. 語根 runtuh の全派生語図鑑（meruntuhkan, keruntuhan, reruntuhan, runtuhan）",
        "root": "runtuh",
        "core_meaning": "崩壊する、崩れ落ちる、瓦解する、失脚する",
        "explanation": "語根 runtuh は、土砂や巨大な建造物、あるいは帝国や体制が「重力や内部の脆さによってガラガラと崩れ落ちる」壊滅的プロセスを表します。天災による山崩れから、独裁政権の打倒（meruntuhkan rezim）、古代遺跡の残骸（reruntuhan candi）まで、劇的な破壊と終焉を語る重要語根です。",
        "matrix": [
            ("runtuh", "語根", "自動詞", "崩れる、崩壊する、失脚する、瓦解する", "Jembatan tua itu akhirnya runtuh setelah dihantam banjir bandang."),
            ("meruntuhkan", "meN- -kan", "他動詞", "崩す、破壊する、打倒する、突き崩す", "Gempa dahsyat meruntuhkan ratusan bangunan permanen di kota itu."),
            ("keruntuhan", "ke- -an", "名詞・被災動詞", "崩壊、瓦解、滅亡、崩落に遭う", "Keruntuhan Uni Soviet mengubah peta geopolitik dunia secara radikal."),
            ("reruntuhan", "reduplikasi", "名詞", "残骸、廃墟、遺跡、瓦礫の山", "Arkeolog menemukan prasasti kuno di antara reruntuhan istana lama."),
            ("runtuhan", "-an", "名詞", "崩落物、崩れた土砂や破片", "Alat berat dikerahkan untuk membersihkan runtuhan tanah longsor."),
            ("meruntuhkan semangat", "frasa", "動詞句", "士気をくじく、心を折る", "Kritik pedas yang tidak membangun dapat meruntuhkan semangat kerja tim.")
        ],
        "details": [
            ("runtuh", "自動詞", "ルントゥ",
             "建物、崖、橋、国家体制などが土台から「ガラガラと崩落・自壊する」動作です。",
             "tebing runtuh（崖崩れ）, tembok runtuh（壁が崩れる）, rezim runtuh（政権が倒れる）",
             "Gedung tua peninggalan zaman kolonial itu runtuh karena termakan usia dan kurang perawatan.",
             "植民地時代のその古い建物は、経年劣化と手入れ不足のため崩壊した。"),
            ("meruntuhkan", "他動詞", "ムルントゥッカン",
             "外力や暴力、論理によって建物や牙城、信念を「破壊する・突き崩す」能動使役です。",
             "meruntuhkan dominasi（支配を突き崩す）, meruntuhkan dinding pembatas（障壁を取り壊す）, meruntuhkan moral（モラルを低下させる）",
             "Strategi serangan balik yang efektif berhasil meruntuhkan pertahanan tim lawan.",
             "効果的なカウンター攻撃の戦術が、相手チームの守備陣を突き崩すことに成功した。"),
            ("keruntuhan", "名詞", "クルントゥハン",
             "国家や文明、巨大企業の「滅亡・終末・破局的崩壊」を指す歴史・経済的専門名詞です。",
             "keruntuhan ekonomi（経済破綻）, keruntuhan moral bangsa（国民的道徳の頽廃）",
             "Banyak faktor internal seperti korupsi sistemik yang mempercepat keruntuhan kerajaan tersebut.",
             "構造的汚職のような多くの内部要因が、その王国の滅亡を加速させた。"),
            ("reruntuhan", "名詞", "ロルントゥハン",
             "崩壊した建物や古代都市の「瓦礫、廃墟、遺跡の遺構」を指す複数・集合名詞です。",
             "reruntuhan candi（寺院遺跡）, di bawah reruntuhan gedung（建物の瓦礫の下で）",
             "Tim penyelamat berjuang tanpa henti mencari korban selamat di balik reruntuhan beton.",
             "救助隊はコンクリートの瓦礫の陰敷から生存者を捜索するため休むことなく奮闘した。")
        ],
        "dialogue": {
            "title": "地震被災地での救援活動と復興計画",
            "lines": [
                ("Bambang", "Laporan terbaru mencatat sejumlah fasilitas umum runtuh akibat gempa dangkal semalam."),
                ("Yuni", "Tim SAR sudah mulai menyisir reruntuhan gedung puskesmas untuk memastikan tidak ada warga terjebak."),
                ("Bambang", "Bencana alam ini meruntuhkan infrastruktur kita, tetapi jangan sampai meruntuhkan harapan hidup para korban."),
                ("Yuni", "Betul, Pak. Kita harus segera mendirikan tenda darurat dan memasok air bersih secepatnya.")
            ]
        },
        "grammar_points": [
            ("reruntuhan の語形成（部分重複）", "語根 runtuh の第1音節の子音に曖昧母音 e を付加した重複形（dwipurwa）+ 接尾辞 -an で形成され、散乱する瓦礫や遺跡群を表す。"),
            ("runtuh vs roboh", "runtuh は建造物や崖が「崩壊して粉々・破片になる」イメージ。roboh は立っていた大木や電柱、建物が根元から「バタリと倒れる・倒壊する」イメージ。")
        ],
        "quizzes": [
            {
                "q": "「地震で倒壊したビルの瓦礫の下から生存者が救出された」の空欄に入る名詞は？\nKorban selamat berhasil dievakuasi dari bawah [...] gedung yang ambruk.",
                "options": ["A. keruntuhan", "B. reruntuhan", "C. peruntuhan", "D. runtuh"],
                "ans": "B. reruntuhan",
                "expl": "物理的な瓦礫や崩れた残骸の山を指すため、集合名詞 reruntuhan が正解です。keruntuhan は崩壊という抽象事象を表します。"
            },
            {
                "q": "「悪意あるデマはチーム内の信頼関係を突き崩す可能性がある」の空欄に入る動詞は？\nKabar bohong itu berpotensi [...] rasa saling percaya di antara kita.",
                "options": ["A. meruntuhkan", "B. mereruntuhkan", "C. keruntuhan", "D. runtuhan"],
                "ans": "A. meruntuhkan",
                "expl": "他動詞として信頼関係を「突き崩す・破壊する」使役動作を表すため、接頭辞 meN- と接尾辞 -kan を伴う meruntuhkan が適切です。"
            },
            {
                "q": "「ソビエト連邦の崩壊」をインドネシア語で表現したものはどれか？",
                "options": ["A. Reruntuhan Uni Soviet", "B. Keruntuhan Uni Soviet", "C. Meruntuhkan Uni Soviet", "D. Runtuhan Uni Soviet"],
                "ans": "B. Keruntuhan Uni Soviet",
                "expl": "国家や帝国の歴史的崩壊・滅亡は抽象名詞 keruntuhan を用いて表現します。"
            }
        ],
        "peribahasa": {
            "quote": "Bumi mana yang tiada ditimpa hujan, gunung mana yang tiada runtuh.",
            "meaning": "雨の降らない地はなく、崩れない山はない＝この世に過ちを犯さない人間や、決して衰退しない強者は存在しない。"
        }
    },
    {
        "filename": "125-root-roboh.md",
        "title": "1375. 語根 roboh の全派生語図鑑（merobohkan, kerobohan, perobohan, teroboh）",
        "root": "roboh",
        "core_meaning": "倒れる、倒壊する、転倒する、なぎ倒す、打ち倒す",
        "explanation": "語根 roboh は、鉛直に直立していた樹木、電柱、壁、建築物が「支えを失ってドサリと倒れ伏す」物理動作を表します。暴風雨による倒木から、老朽建築物の人為的解体（merobohkan gedung）、ボクシングで相手をノックダウンすることまで、直立状態からの転倒・倒壊に特化した語根です。",
        "matrix": [
            ("roboh", "語根", "自動詞", "倒れる、倒壊する、バタリと倒れる", "Pohon beringin tua itu roboh menimpa kabel listrik saat angin kencang."),
            ("merobohkan", "meN- -kan", "他動詞", "倒す、なぎ倒す、解体する、ノックアウトする", "Pemerintah kota mengerahkan buldoser untuk merobohkan bangunan liar."),
            ("kerobohan", "ke- -an", "被災動詞・名詞", "倒壊の下敷きになる、倒壊事故", "Beberapa mobil warga rusak parah akibat kerobohan tiang reklame."),
            ("perobohan", "peN- -an", "名詞", "取り壊し、解体作業、倒壊させるプロセス", "Perobohan stadion lama dilakukan demi membangun arena olahraga modern."),
            ("teroboh", "ter-", "無意志・受動動詞", "倒された、不意に倒れる", "Pagar bambu itu mudah teroboh ketika didorong kerumunan massa."),
            ("roboh total", "frasa", "状態句", "全壊した、跡形もなく倒れた", "Gudang penyimpanan beras itu roboh total diterjang badai siklon.")
        ],
        "details": [
            ("roboh", "自動詞", "ロボホ",
             "直立していた木、建物、塀などが「倒れ伏す」動作です（英語の collapse / fall down）。",
             "rumah roboh（家屋倒壊）, pohon roboh（倒木）, pagar roboh（フェンスが倒れる）",
             "Hujan lebat disertai angin puting beliung menyebabkan puluhan pohon perindang jalan roboh.",
             "激しい突風を伴う大雨により、数十本の街路樹がなぎ倒された。"),
            ("merobohkan", "他動詞", "ムロボホカン",
             "立っている対象を「意図的になぎ倒す・取り壊す・相手をマットに沈める」動作です。",
             "merobohkan lawan（対戦相手をノックダウンする）, merobohkan rumah tua（古い家を取り壊す）",
             "Petinju nasional itu berhasil merobohkan lawannya pada ronde ketiga dengan pukulan telak.",
             "その国内ボクサーは強烈なパンチで見事に対戦相手を第3ラウンドでマットに沈めた。"),
            ("kerobohan", "動詞・名詞", "クロボハン",
             "倒れてきた物の「下敷きになって被害を受ける」被災構文として多用されます。",
             "kerobohan pohon（倒木の下敷きになる）, kerobohan tembok（倒れてきた壁に挟まれる）",
             "Sebuah warung kopi hancur setelah kerobohan pohon kelapa yang tersambar petir.",
             "雷に打たれたヤシの木が倒れて直撃し、1軒のカフェが全壊した。"),
            ("perobohan", "名詞", "プロボハン",
             "再開発や安全確保のために行われる「建造物の計画的解体・撤去工事」を指します。",
             "perobohan gedung bertingkat（高層ビルの解体撤去）, izin perobohan（解体許可証）",
             "Proses perobohan bangunan tanpa izin itu mendapat pengawalan ketat dari petugas keamanan.",
             "その無許可建築物の解体撤去作業は警備当局による厳重な警備のもとで実施された。")
        ],
        "dialogue": {
            "title": "台風被害の現場調査と復旧対策",
            "lines": [
                ("Hendra", "Pak RT, banyak tiang listrik dan pohon roboh di sepanjang jalan utama desa kita."),
                ("Pak RT", "Iya, tim PLN sedang menuju kemari untuk memutus aliran listrik demi keselamatan warga."),
                ("Hendra", "Ada satu rumah warga yang kerobohan batang pohon besar di bagian dapurnya."),
                ("Pak RT", "Mari kita kumpulkan warga untuk bergotong royong memotong dahan dan merobohkan sisa pohon yang rawan tumbang.")
            ]
        },
        "grammar_points": [
            ("roboh vs tumbang", "どちらも「倒れる」だが、tumbang は主に根こそぎ倒れる「植物・樹木」に用いられ（pohon tumbang）、roboh は樹木だけでなく「人工建造物（壁・家屋・橋・電柱）」の倒壊に幅広く用いられる。"),
            ("被災表現としての kerobohan", "「Mobilnya kerobohan pohon」＝「彼の車は倒木の下敷きになった（被災した）」。主語が被害者、kerobohan が被害動詞、後続名詞が加害物を表す典型的構文。")
        ],
        "quizzes": [
            {
                "q": "「強風で倒れてきた電柱の下敷きになり、1台の車が破損した」の空欄に入る語は？\nSebuah mobil rusak parah akibat [...] tiang listrik saat badai.",
                "options": ["A. merobohkan", "B. kerobohan", "C. perobohan", "D. terobohkan"],
                "ans": "B. kerobohan",
                "expl": "物が倒れてきて下敷きになる被害を表すため、被災接辞 ke-...-an を伴う kerobohan が正解です。"
            },
            {
                "q": "「自治体は危険な違法建築物を解体するために重機を投入した」の空欄に入る動詞は？\nPemerintah mengerahkan alat berat untuk [...] bangunan liar yang membahayakan warga.",
                "options": ["A. merobohkan", "B. kerobohan", "C. roboh", "D. berobohan"],
                "ans": "A. merobohkan",
                "expl": "目的語（bangunan liar）を「取り壊す・解体する」能動使役動作なので、他動詞 merobohkan が適切です。"
            },
            {
                "q": "次のうち、主に植物・樹木が根元から倒れる際に特化して好まれる類義語はどれか？",
                "options": ["A. runtuh", "B. gugur", "C. tumbang", "D. patah"],
                "ans": "C. tumbang",
                "expl": "樹木が根元から倒れる現象には「tumbang」が最もよく用いられます。gugur は葉や花が散ること、patah は折れることです。"
            }
        ],
        "peribahasa": {
            "quote": "Pohon yang tinggi roboh, rumput yang lunak tetap bertahan.",
            "meaning": "高木は風で倒れるが、しなやかな草は生き残る＝柔軟で謙虚な姿勢こそが嵐のような危機を乗り越える力であるという教え。"
        }
    },
    {
        "filename": "126-root-tumbuh.md",
        "title": "1376. 語根 tumbuh の全派生語図鑑（menumbuhkan, pertumbuhan, tumbuhan, bertumbuh）",
        "root": "tumbuh",
        "core_meaning": "生える、発芽する、成長する、育つ、生じる",
        "explanation": "語根 tumbuh は、種子から芽が出て生命が「生き生きと育つ」生物学的成長を原義とします。子どもの身体的発達（pertumbuhan anak）、植物界全般（tumbuhan）、愛や信頼が芽生えること（tumbuh rasa cinta）、国家の経済成長率（pertumbuhan ekonomi）まで、プラスの生命力と拡大を表現する最も基本的な語根です。",
        "matrix": [
            ("tumbuh", "語根", "自動詞", "生える、育つ、成長する、芽生える", "Benih cabai yang disemai mulai tumbuh subur di pekarangan."),
            ("menumbuhkan", "meN- -kan", "他動詞", "育てる、芽生えさせる、育む、促進する", "Pendidikan karakter sejak dini bertujuan menumbuhkan rasa empati anak."),
            ("pertumbuhan", "per- -an", "名詞", "成長、発育、伸び、経済成長率", "Pertumbuhan ekonomi nasional ditargetkan mencapai lima persen tahun ini."),
            ("tumbuhan", "-an", "名詞", "植物、草木、植生", "Hutan tropis Indonesia kaya akan berbagai spesies tumbuhan langka."),
            ("bertumbuh", "ber-", "自動詞", "成長しつつある、発達・伸長する", "Komunitas pegiat lingkungan ini bertumbuh sangat pesat di media sosial."),
            ("ketumbuhan", "ke- -an", "名詞・医学", "腫瘍、できもの、ポリープ", "Dokter berhasil mengangkat ketumbuhan jinak di jaringan kulit pasien."),
            ("tumbuh kembang", "frasa", "名詞・成句", "子どもの成育・心身の発達", "Pemenuhan gizi seimbang sangat krusial bagi tumbuh kembang balita.")
        ],
        "details": [
            ("tumbuh", "自動詞", "トゥンブ",
             "植物が生える、子どもが育つ、感情が芽生える動作を表します。",
             "tumbuh gigi（歯が生える）, tumbuh dewasa（成長して大人になる）, tumbuh kesadaran（意識が芽生える）",
             "Rasa saling percaya antara kedua pimpinan negara mulai tumbuh setelah dialog bilateral.",
             "二国間の首脳対話を経て、両国リーダー間の相互信頼が芽生え始めた。"),
            ("menumbuhkan", "他動詞", "ムヌンブッカン",
             "種をまいて育てたり、人材や愛国心、イノベーション意識を「育む・促進する」使役動作です。",
             "menumbuhkan minat baca（読書意欲を育てる）, menumbuhkan optimisme（楽観主義を育む）",
             "Program beasiswa ini dirancang untuk menumbuhkan talenta digital muda berdaya saing global.",
             "この奨学金プログラムは、グローバルな競争力を持つ若いデジタル人材を育成するために設計された。"),
            ("pertumbuhan", "名詞", "プルトゥンブハン",
             "数量、身体、経済などが「拡大・発育するプロセスや指標」を指す最重要統計・社会用語です。",
             "pertumbuhan ekonomi（経済成長）, laju pertumbuhan penduduk（人口増加率）, hormon pertumbuhan（成長ホルモン）",
             "Laju pertumbuhan ekonomi daerah didorong oleh peningkatan konsumsi domestik dan ekspor tambang.",
             "地方の経済成長率は、内需の拡大と鉱物輸出の増加によって牽引された。"),
            ("tumbuhan", "名詞", "トゥンブハン",
             "「植物」全般を指す生物学・日常名詞です（動物は hewan）。",
             "tumbuhan obat（薬用植物）, tumbuhan karnivora（食虫植物）, keanekaragaman tumbuhan（植物の多様性）",
             "Masyarakat adat menggunakan aneka jenis tumbuhan herbal sebagai obat tradisional turun-temurun.",
             "先住民族コミュニティは様々な種類の薬草植物を先祖伝来の伝統薬として用いている。")
        ],
        "dialogue": {
            "title": "乳幼児の栄養改善と子どもの成長に関する対談",
            "lines": [
                ("dr. Farhan", "Ibu Rina, bagaimana pemantauan tumbuh kembang anak Ibu di Posyandu bulan ini?"),
                ("Ibu Rina", "Alhamdulillah, grafik pertumbuhan berat dan tinggi badannya berada pada jalur normal, Dok."),
                ("dr. Farhan", "Bagus sekali. Asupan protein hewani sangat efektif untuk menumbuhkan jaringan otak dan mencegah stunting."),
                ("Ibu Rina", "Terima kasih atas sarannya, Dok. Kami akan terus menjaga pola makan sehat untuknya.")
            ]
        },
        "grammar_points": [
            ("tumbuh vs kembang", "tumbuh は「サイズが大きくなる、生える、身体が伸びる」物理的・量的成長。kembang は「つぼみが開く、能力や知識が開花・多角化・展開する」質的発展。"),
            ("tumbuh kembang という熟語", "小児医学や育児において「心身の発育と発達」を一括して指す決まり文句。Posyandu（地域保健ポスト）で頻出。")
        ],
        "quizzes": [
            {
                "q": "「今年の国の経済成長率は5パーセントに達すると予測されている」の空欄に入る名詞は？\nLaju [...] ekonomi nasional tahun ini diproyeksikan mencapai lima persen.",
                "options": ["A. tumbuhan", "B. penumbuhan", "C. pertumbuhan", "D. bertumbuh"],
                "ans": "C. pertumbuhan",
                "expl": "経済成長は定型表現として「pertumbuhan ekonomi」と言います。"
            },
            {
                "q": "「植物」と「動物」の対比として正しい組み合わせはどれか？",
                "options": ["A. tumbuhan dan hewan", "B. pertumbuhan dan tanaman", "C. tumbuh dan liar", "D. bertumbuh dan binatang"],
                "ans": "A. tumbuhan dan hewan",
                "expl": "植物界全般は「tumbuhan」、動物界全般は「hewan」と呼びます。"
            },
            {
                "q": "「教師は生徒たちの批判的思考力を育むよう努める」の空欄に入る適切な動詞は？\nGuru berusaha [...] daya berpikir kritis pada para siswa.",
                "options": ["A. bertumbuh", "B. tumbuhan", "C. menumbuhkan", "D. ketumbuhan"],
                "ans": "C. menumbuhkan",
                "expl": "能力や精神的態度を「育む・促進する」使役動作を表すため、他動詞 menumbuhkan が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Bumi tidak selebar daun kelor; benih kebaikan akan selalu tumbuh di mana saja.",
            "meaning": "世間は狭いものではない。善意の種はどこであっても必ず芽を出し育つものである。"
        }
    },
    {
        "filename": "127-root-kembang.md",
        "title": "1377. 語根 kembang の全派生語図鑑（mengembangkan, perkembangan, pengembangan, berkembang）",
        "root": "kembang",
        "core_meaning": "咲く、開く、膨らむ、発展する、開発する",
        "explanation": "語根 kembang は、花のつぼみがふっくらと「開花する・膨らむ」原義から、能力・社会・技術が「高度に発展・進化・展開する」意味へと発展した最重要語根です。自発的発展（berkembang）から政策的開発・育成（mengembangkan）、技術開発プロセス（pengembangan）、時代の変遷・動向（perkembangan zaman）まで、進歩とイノベーションを語る中核語です。",
        "matrix": [
            ("kembang", "語根", "名詞・自動詞", "花（ジャワ語由来・bunga）、膨らむ", "Kembang melati putih ditetapkan sebagai puspa bangsa Indonesia."),
            ("berkembang", "ber-", "自動詞", "発展する、進化する、花開く、広まる", "Ekosistem startup di Indonesia berkembang pesat dalam dekade terakhir."),
            ("mengembangkan", "meN- -kan", "他動詞", "発展させる、開発する、育成する、広げる", "Peneliti lokal berhasil mengembangkan vaksin baru untuk penyakit tropis."),
            ("perkembangan", "per- -an", "名詞", "発展、進歩、推移、発達状況、動向", "Kita harus terus memantau perkembangan geopolitik global yang dinamis."),
            ("pengembangan", "peN- -an", "名詞", "開発、育成、研究開発（R&D）活動", "Alokasi anggaran untuk riset dan pengembangan masih perlu ditingkatkan."),
            ("terkembang", "ter-", "受動・状態動詞", "広がっている、翼や帆が張られた", "Layar perahu Phinisi terkembang gagah mengarungi lautan Nusantara."),
            ("negara berkembang", "frasa", "名詞句", "開発途上国（発展途上国）", "Indonesia aktif menyuarakan kepentingan negara berkembang di forum G20.")
        ],
        "details": [
            ("berkembang", "自動詞", "ブルクンバン",
             "都市、産業、生物の機能などが自然に「発展する・進化する・多角化する」状態です。",
             "negara berkembang（発展途上国）, berkembang biak（繁殖する）, berkembang pesat（急速に発展する）",
             "Sektor ekonomi digital di Asia Tenggara terus berkembang membuka banyak lapangan kerja baru.",
             "東南アジアのデジタル経済部門は発展を続け、多くの新たな雇用機会を創出している。"),
            ("mengembangkan", "他動詞", "ムンクンバンカン",
             "新しい商品、技術、ソフトウェア、人材の潜在能力を「開発する・拡大する」能動使役です。",
             "mengembangkan aplikasi（アプリを開発する）, mengembangkan potensi diri（自己の潜在能力を伸ばす）",
             "Perusahaan teknologi itu berinvestasi besar untuk mengembangkan kecerdasan buatan.",
             "そのテクノロジー企業は人工知能を開発するために多額の投資を行っている。"),
            ("perkembangan", "名詞", "プルクンバンガン",
             "情勢、技術、子どもの発達などの「進歩・推移・動向」という現象そのものを指します。",
             "perkembangan teknologi（技術の進歩）, mengikuti perkembangan zaman（時代の変遷に追随する）, perkembangan kasus（事件の進展）",
             "Media massa secara berkala memberitakan perkembangan negosiasi gencatan senjata.",
             "マスメディアは停戦交渉の進展状況を定期的に報道している。"),
            ("pengembangan", "名詞", "プンクンバンガン",
             "人為的な施策としての「研究開発、都市開発、人材育成プログラム」を指す実務用語です。",
             "penelitian dan pengembangan / Litbang（研究開発・R&D）, pengembangan karier（キャリア開発）, pengembangan wilayah（地域開発）",
             "Badan Riset dan Inovasi Nasional memprioritaskan pengembangan energi baru dan terbarukan.",
             "国家研究イノベーション庁（BRIN）は、新再生可能エネルギーの開発を最優先事項としている。")
        ],
        "dialogue": {
            "title": "スタートアップの製品開発と市場展開ミーティング",
            "lines": [
                ("Dimas", "Bagaimana perkembangan pengujian fitur baru di aplikasi kita, Maya?"),
                ("Maya", "Respons dari pengguna awal sangat positif. Komunitas pengguna kita berkembang cukup cepat."),
                ("Dimas", "Bagus. Selanjutnya tim teknis harus mengembangkan integrasi sistem pembayaran digital."),
                ("Maya", "Siap, Mas. Pengembangan modul pembayaran itu ditargetkan selesai akhir bulan ini.")
            ]
        },
        "grammar_points": [
            ("perkembangan vs pengembangan の識別", "perkembangan は自発的・歴史的推移（「技術の進歩」「事件の推移」）。pengembangan は人為的・能動的開発行為（「システム開発」「人材育成プロジェクト」）。試験でも頻出の対比。"),
            ("kembang kempis という成句", "胸が激しく上下すること、または企業経営などが「浮沈を繰り返して青息吐息であること」を表す慣用表現。")
        ],
        "quizzes": [
            {
                "q": "「研究開発（R&D）」に相当するインドネシア語の公的略語（Litbang）の正式名称はどれか？",
                "options": ["A. Penelitian dan Perkembangan", "B. Penelitian dan Pengembangan", "C. Pembelajaran dan Berkembang", "D. Pengujian dan Terkembang"],
                "ans": "B. Penelitian dan Pengembangan",
                "expl": "人為的な開発・育成活動なので「Penelitian dan Pengembangan（Litbang）」が正解です。"
            },
            {
                "q": "「発展途上国」をインドネシア語で表現したものはどれか？",
                "options": ["A. negara maju", "B. negara tertinggal", "C. negara berkembang", "D. negara pengembang"],
                "ans": "C. negara berkembang",
                "expl": "先進国は「negara maju」、発展途上国は現在進行で発展しつつある国という意味で「negara berkembang」と言います。"
            },
            {
                "q": "「事件の最新の進展状況を注視しなければならない」の空欄に入る名詞は？\nKita harus memantau [...] terbaru dari investigasi kasus tersebut.",
                "options": ["A. pengembangan", "B. perkembangan", "C. kembang", "D. mengembangkan"],
                "ans": "B. perkembangan",
                "expl": "事件や情勢の「推移・進展動向」を表すため、現象名詞の perkembangan が適切です。"
            }
        ],
        "peribahasa": {
            "quote": "Bunga bukan sekuntum, kumbang bukan seekor.",
            "meaning": "花は一輪だけではなく、蜂も一匹だけではない＝世の中に異性やチャンスは幾らでもあるので、一つの失恋や失敗に絶望する必要はない。"
        }
    },
    {
        "filename": "128-root-maju.md",
        "title": "1378. 語根 maju の全派生語図鑑（memajukan, kemajuan, pemajuan, termaju）",
        "root": "maju",
        "core_meaning": "前進する、進む、進歩する、立候補する、出馬する",
        "explanation": "語根 maju は、空間的に「前へ進み出る」動作から、文明・技術・教育が「進歩・近代化する」、あるいは選挙に「立候補・出馬する（maju pilkada）」ことまでを表す前向きな基幹語根です。形容詞的用法（negara maju＝先進国）から人為的推進（memajukan）、進歩と発展の結晶（kemajuan）まで幅広く用いられます。",
        "matrix": [
            ("maju", "語根", "自動詞・形容詞", "進む、前進する、進歩した、出馬する", "Langkah kaki prajurit serentak maju menuju garis pertahanan."),
            ("memajukan", "meN- -kan", "他動詞", "前進させる、促進する、進歩させる、日程を繰り上げる", "Pemerintah berkomitmen memajukan industri kreatif lokal."),
            ("kemajuan", "ke- -an", "名詞", "進歩、進展、発達、前進度合い", "Kemajuan teknologi kecerdasan buatan membawa dampak besar bagi kehidupan."),
            ("pemajuan", "peN- -an", "名詞", "促進、推進、振興プロセス（政策用語）", "Undang-Undang Pemajuan Kebudayaan disahkan untuk melindungi warisan leluhur."),
            ("termaju", "ter-", "最上級形容詞", "最も進歩した、最先端の", "Singapura diakui sebagai salah satu negara dengan infrastruktur termaju di Asia."),
            ("negara maju", "frasa", "名詞句", "先進国", "Indonesia memiliki visi jangka panjang untuk menjadi negara maju pada tahun 2045."),
            ("maju tak gentar", "frasa", "成句・スローガン", "恐れることなく前進する（愛国歌の題名）", "Dengan semangat juang tinggi, para pejuang maju tak gentar membela tanah air.")
        ],
        "details": [
            ("maju", "自動詞・形容詞", "マジュ",
             "前へ歩み出る、近代化されている、選挙に立候補するなどの意味を持ちます。",
             "maju ke depan（前へ出る）, berpikir maju（進歩的な考え方をする）, maju dalam pemilihan（選挙に立候補する）",
             "Beberapa tokoh muda berencana maju dalam pemilihan kepala daerah tahun ini.",
             "何人かの若手リーダーたちが今年の地方首長選挙に出馬することを計画している。"),
            ("memajukan", "他動詞", "ムマジュッカン",
             "教育や文化、産業を「振興する・発展させる」、または会議の日程を「前倒しにする」使役動作です。",
             "memajukan pendidikan（教育を振興する）, memajukan jadwal rapat（会議の日程を繰り上げる）",
             "Karena ada tugas mendesak, direktur meminta kita memajukan jadwal pertemuan menjadi besok.",
             "緊急の任務が入ったため、取締役はミーティングの予定を明日へと前倒しにするよう求めた。"),
            ("kemajuan", "名詞", "クマジュアン",
             "科学技術、医療、自己研鑽などの「進歩・進展」という達成状態を指します。",
             "kemajuan teknologi informasi（IT技術の進歩）, kemajuan pesat（長足の進歩）, kemajuan bangsa（国家の近代化）",
             "Kerja keras seluruh tim menunjukkan kemajuan yang sangat signifikan dalam proyek ini.",
             "チーム全体の懸命な努力が、このプロジェクトにおいて極めて顕著な進展を示している。"),
            ("pemajuan", "名詞", "プマジュアン",
             "文化や人権、法制を積極的に推進・振興する「国家・制度的プロセス」を指す格調高い法律・政策用語です。",
             "pemajuan hak asasi manusia（人権の促進・擁護）, pemajuan kebudayaan nasional（国民文化の振興）",
             "Pemerintah membentuk direktorat khusus untuk menangani program pemajuan kebudayaan daerah.",
             "政府は地域の文化振興プログラムを担当する専門局を設立した。")
        ],
        "dialogue": {
            "title": "地方経済の振興と若者のキャリアに関する意見交換",
            "lines": [
                ("Fajar", "Bagaimana cara kita memajukan perekonomian desa agar pemuda tidak semua merantau ke ibu kota?"),
                ("Siti", "Kita bisa memanfaatkan kemajuan internet untuk memasarkan produk kerajinan desa ke mancanegara."),
                ("Fajar", "Ide cemerlang. Pemuda desa harus memiliki pola pikir maju dan melek teknologi digital."),
                ("Siti", "Betul. Dengan begitu, desa kita akan semakin maju tanpa kehilangan kearifan lokalnya.")
            ]
        },
        "grammar_points": [
            ("memajukan jadwal の意味", "時間の文脈で memajukan jadwal と言うと「予定を繰り上げる・前倒しにする（earlier）」という意味になる。逆に「延期する・先送りする」は memundurkan jadwal または menunda。"),
            ("negara maju vs negara berkembang", "「先進国（developed country）」は negara maju、「発展途上国（developing country）」は negara berkembang。対義語としてセットで覚える必須表現。")
        ],
        "quizzes": [
            {
                "q": "「急用のため、会議の時間を2時間前倒し（繰り上げ）にした」の空欄に入る動詞は？\nKarena ada urusan mendesak, kami [...] jadwal pertemuan dua jam lebih awal.",
                "options": ["A. memundurkan", "B. memajukan", "C. kemajuan", "D. termaju"],
                "ans": "B. memajukan",
                "expl": "時間を「早める・繰り上げる」使役動作は memajukan jadwal と表現します。memundurkan は繰り下げ（遅らせる）です。"
            },
            {
                "q": "インドネシア語で「先進国」を意味する表現はどれか？",
                "options": ["A. negara termaju", "B. negara maju", "C. negara kemajuan", "D. negara memajukan"],
                "ans": "B. negara maju",
                "expl": "先進国の標準的な定型表現は「negara maju」です。"
            },
            {
                "q": "インドネシアの文化遺産を保護・振興するために制定された法律名に含まれる単語はどれか？\nUndang-Undang [...] Kebudayaan.",
                "options": ["A. Kemajuan", "B. Pemajuan", "C. Memajukan", "D. Termakmur"],
                "ans": "B. Pemajuan",
                "expl": "国家施策としての促進・振興プロセスを指すため、名詞「Pemajuan（UU Pemajuan Kebudayaan）」が正式名称です。"
            }
        ],
        "peribahasa": {
            "quote": "Maju kena bentur, mundur kena tendang.",
            "meaning": "前へ進めばぶつかり、後ろへ退けば蹴られる＝「進退窮まる」「前門の虎、後門の狼」のジレンマを表すことわざ。"
        }
    },
    {
        "filename": "129-root-mundur.md",
        "title": "1379. 語根 mundur の全派生語図鑑（memundurkan, kemunduran, pemunduran, bermundur）",
        "root": "mundur",
        "core_meaning": "後退する、後ろへ下がる、退陣する、辞任する、衰退する",
        "explanation": "語根 mundur は、空間的に「後ろへ退く・バックする」動作から、役職から「辞任・勇退する（mundur dari jabatan）」、予定を「繰り下げる・延期する（memundurkan jadwal）」、文明や業績が「衰退・後退する（kemunduran）」ことまでを表す対義的基幹語根です。",
        "matrix": [
            ("mundur", "語根", "自動詞", "後退する、下がる、辞任する、延期される", "Mobil itu perlahan mundur keluar dari garasi rumah yang sempit."),
            ("memundurkan", "meN- -kan", "他動詞", "後ろへ下げる、バックさせる、予定を繰り下げる・遅らせる", "Sopir bus berhati-hati memundurkan kendaraannya di terminal."),
            ("kemunduran", "ke- -an", "名詞", "後退、衰退、退行、業績悪化", "Kurangnya inovasi dapat memicu kemunduran daya saing perusahaan."),
            ("pemunduran", "peN- -an", "名詞", "後退させること、繰り下げ・延期プロセス", "Pemunduran tenggat waktu penyerahan tugas disambut lega para mahasiswa."),
            ("mengundurkan diri", "frasa", "成句・動詞", "辞任する、辞職する、棄権する", "Menteri tersebut memutuskan mengundurkan diri setelah skandal terungkap."),
            ("pantang mundur", "frasa", "成句・副詞句", "不退転の、決して屈しない、前進あるのみ", "Dengan semangat pantang mundur, para atlet terus berjuang hingga menit akhir.")
        ],
        "details": [
            ("mundur", "自動詞", "ムンドゥール",
             "物理的に後ろへ下がる、役職から退く、予定が後ろにずれる動作を表します。",
             "mundur beberapa langkah（数歩下がる）, mundur teratur（秩序正しく撤退する）, mundur dari pencalonan（出馬を辞退する）",
             "Melihat ombak besar menerjang pantai, para pengunjung bergegas mundur mencari tempat aman.",
             "大波が海岸に押し寄せるのを見て、観光客たちは急いで後ろへ下がり安全な場所を探した。"),
            ("memundurkan", "他動詞", "ムムンドゥールカン",
             "乗り物をバックさせる、時計の針を遅らせる、期日や時間を「遅らせる・繰り下げる」使役動作です。",
             "memundurkan mobil（車を後退させる）, memundurkan jam keberangkatan（出発時刻を遅らせる）",
             "Panitia memutuskan memundurkan jadwal konser satu jam karena hujan deras belum reda.",
             "豪雨が止まないため、主催者はコンサートの開始予定を1時間遅らせることを決定した。"),
            ("kemunduran", "名詞", "クムンドゥーラン",
             "文明、経済、民主主義、個人の健康状態が「衰退・悪化・退行すること」を指します。",
             "kemunduran ekonomi（景気後退）, kemunduran demokrasi（民主主義の後退）",
             "Banyak pakar menilai pembatasan kebebasan pers merupakan bentuk kemunduran demokrasi.",
             "多くの専門家は報道の自由の制限が民主主義の後退の一形態であると評価している。"),
            ("mengundurkan diri", "動詞句", "ムングンドゥールカン・ディリ",
             "自発的あるいは責任を取って「職・地位・競技から身を引く（辞任・辞職・棄権する）」定型表現です。",
             "surat pengunduran diri（辞表・退職届）, mengundurkan diri dari jabatan direktur（取締役を辞任する）",
             "Setelah menjabat selama satu dekade, CEO tersebut akhirnya memilih mengundurkan diri secara terhormat.",
             "10年間の在任を経て、そのCEOは最終的に名誉ある形で辞任することを選んだ。")
        ],
        "dialogue": {
            "title": "役員の辞任表明と後任人事に関する社内対話",
            "lines": [
                ("Rudy", "Apakah benar kabar bahwa Direktur Keuangan kita telah mengajukan surat pengunduran diri?"),
                ("Anita", "Iya, beliau memilih mundur karena alasan kesehatan keluarga yang membutuhkan perhatian penuh."),
                ("Rudy", "Kehilangan figur berpengalaman seperti beliau tentu menjadi kemunduran bagi manajemen kita."),
                ("Anita", "Kita harus segera mencari pengganti agar roda operasional perusahaan tidak terganggu.")
            ]
        },
        "grammar_points": [
            ("mengundurkan diri の音韻変化", "語根 mundur の頭文字 m に対し接頭辞 meN- が付くと mengundurkan（鼻音 ng の添加）となる点に注意。意味は「自己を後退させる＝辞任する」。"),
            ("memundurkan vs memajukan jadwal の完全対比", "memajukan jadwal＝予定を早める（前倒し）。memundurkan jadwal＝予定を遅らせる（繰り下げ・延期）。ビジネスで毎日のように使われる対義語。")
        ],
        "quizzes": [
            {
                "q": "「退職届・辞表」を意味するインドネシア語の正式な表現はどれか？",
                "options": ["A. surat kemunduran", "B. surat pemunduran", "C. surat pengunduran diri", "D. surat mundur"],
                "ans": "C. surat pengunduran diri",
                "expl": "退職届は「surat pengunduran diri」と言います。"
            },
            {
                "q": "「悪天候のため、フライトの出発時刻が2時間遅らされた（繰り下げられた）」の空欄に入る動詞は？\nJadwal keberangkatan pesawat [...] dua jam akibat cuaca buruk.",
                "options": ["A. dimajukan", "B. dimundurkan", "C. kemunduran", "D. mengundurkan"],
                "ans": "B. dimundurkan",
                "expl": "時刻を「遅らせる・繰り下げる」受動態なので dimundurkan が適切です。dimajukan は繰り上げです。"
            },
            {
                "q": "「不退転の決意で、決して屈しない精神」を表す定型成句はどれか？",
                "options": ["A. pantang mundur", "B. mundur teratur", "C. kemunduran mutlak", "D. mundur diri"],
                "ans": "A. pantang mundur",
                "expl": "「pantang mundur」は「決して引き下がらない、不退転の」という意味の慣用スローガンです。"
            }
        ],
        "peribahasa": {
            "quote": "Esa hilang, dua terbilang; pantang pendekar mundur di gelanggang.",
            "meaning": "一人が倒れても二人が名を残す。真の武士は土俵の上で決して後ろへ退かない＝男児たるもの一度挑んだ勝負で決して退却してはならないという不屈の精神。"
        }
    },
    {
        "filename": "130-root-hindar.md",
        "title": "1380. 語根 hindar の全派生語図鑑（menghindari, terhindar, penghindaran, menghindarkan）",
        "root": "hindar",
        "core_meaning": "避ける、回避する、免れる、遠ざける",
        "explanation": "語根 hindar は、危険、衝突、責任、疾患などの好ましくない事象から身をかわして「回避する・免れる」動作を表します。他動詞（menghindari＝〜を避ける）、可能・無意志受動態（terhindar＝〜から免れる）、危険を遠ざける使役（menghindarkan）、脱税などの行為（penghindaran pajak）まで、リスクマネジメントを語る必須語根です。",
        "matrix": [
            ("hindar", "語根", "自動詞", "避ける、身をかわす（通常は接辞を伴う）", "Hindar dari bahaya adalah naluri dasar setiap makhluk hidup."),
            ("menghindari", "meN- -i", "他動詞", "〜を避ける、回避する、敬遠する", "Pengemudi harus menghindari penggunaan telepon genggam saat berkendara."),
            ("terhindar", "ter-", "受動・可能動詞", "〜を免れる、助かる、〜から逃れられる", "Berkat sabuk pengaman, penumpangnya terhindar dari luka yang fatal."),
            ("menghindarkan", "meN- -kan", "他動詞", "遠ざける、避けるようにする、守る", "Pemberian vaksin bertujuan menghindarkan anak-anak dari ancaman wabah penyakit."),
            ("penghindaran", "peN- -an", "名詞", "回避、忌避行為、免除策", "Penghindaran pajak secara ilegal dapat dikenakan sanksi pidana berat."),
            ("tak terhindarkan", "frasa", "形容詞句", "不可避の、避けられない（inevitable）", "Konflik kepentingan menjadi hal yang tak terhindarkan dalam dunia bisnis.")
        ],
        "details": [
            ("menghindari", "他動詞", "ムンヒンダリ",
             "事故、トラブル、特定の食べ物、対人関係などを能動的に「避ける・回避する」動作です。",
             "menghindari makanan manis（甘い食べ物を控える）, menghindari macet（渋滞を避ける）, menghindari konflik（争いを回避する）",
             "Kita disarankan menghindari konsumsi makanan cepat saji yang mengandung banyak lemak jenuh.",
             "私たちは飽和脂肪酸を多く含むファストフードの摂取を避けるよう推奨されている。"),
            ("terhindar", "動詞", "トゥルヒンダール",
             "運良く、あるいは予防策のおかげで災難や病気から「免れる・助かる」状態です。",
             "terhindar dari bahaya（危険から免れる）, terhindar dari bencana（災難を免れる）, terhindar dari infeksi（感染を免れる）",
             "Desa itu terhindar dari banjir bandang berkat tanggul penahan air yang baru selesai dibangun.",
             "その村は、新しく完成した防水堤防のおかげで鉄砲水の被害を免れた。"),
            ("menghindarkan", "他動詞", "ムンヒンダルカン",
             "主語が人や物を災難・トラブルから「遠ざけて防ぐ・守る」使役動作です。",
             "menghindarkan diri dari narkoba（麻薬から身を遠ざける）, menghindarkan anak dari bahaya（子どもを危険から遠ざける）",
             "Penerapan protokol keselamatan kerja ketat mampu menghindarkan pekerja dari kecelakaan fatal.",
             "厳格な労働安全プロトコルの適用が、作業員たちを致命的な事故から遠ざける（守る）ことができる。"),
            ("penghindaran", "名詞", "プンヒンダラン",
             "リスク、納税、義務などを回避・免脱しようとする「行為・対策プロセス」を指します。",
             "penghindaran pajak / tax avoidance（合法または不透明な租税回避）, penghindaran risiko（リスク回避）",
             "Pemerintah terus memperketat regulasi keuangan guna mencegah praktik penghindaran pajak lintas negara.",
             "政府は国境を越えた租税回避行為を防止するため、金融規制の強化を続けている。")
        ],
        "dialogue": {
            "title": "交通安全と事故回避のための運転マナー",
            "lines": [
                ("Doni", "Kenapa kamu memilih lewat jalan lingkar luar yang jaraknya lebih jauh, Reza?"),
                ("Reza", "Saya ingin menghindari kemacetan parah di pusat kota pada jam pulang kantor ini."),
                ("Doni", "Pilihan bijak. Berkendara santai juga bisa menghindarkan kita dari risiko stres dan kecelakaan."),
                ("Reza", "Betul sekali. Keselamatan adalah hal utama agar kita bisa terhindar dari hal-hal yang tidak diinginkan.")
            ]
        },
        "grammar_points": [
            ("menghindari vs menghindarkan の目的語の違い", "menghindari の目的語は「避けたい対象そのもの（kemacetan, bahaya）」。menghindarkan の目的語は「危険から遠ざけられる守るべき対象（anak, diri, pekerja）」または「menghindarkan A dari B（AをBから遠ざける）」。"),
            ("tak terhindarkan の構文", "英語の inevitable（不可避の）に相当し、新聞論説や学術論文で頻出。「Perubahan adalah hal yang tak terhindarkan（変化は避けられないものである）」。")
        ],
        "quizzes": [
            {
                "q": "「健康的なライフスタイルを維持することで、私たちは様々な生活習慣病を免れることができる」の空欄に入る動詞は？\nDengan pola hidup sehat, kita dapat [...] dari berbagai penyakit kronis.",
                "options": ["A. menghindari", "B. terhindar", "C. menghindarkan", "D. penghindaran"],
                "ans": "B. terhindar",
                "expl": "後続に前置詞 dari（〜から）を伴い、災難や病気から「免れる・逃れられる」状態を表すため、terhindar が正解です。"
            },
            {
                "q": "「租税回避（タックス・アボイダンス）」を意味する経済・法務用語はどれか？",
                "options": ["A. penghindaran pajak", "B. pembebasan pajak", "C. pembayaran pajak", "D. terhindar pajak"],
                "ans": "A. penghindaran pajak",
                "expl": "税金を回避する行為は「penghindaran pajak」と言います。"
            },
            {
                "q": "「渋滞を避けるために朝早く出発した」の空欄に入る適切な動詞は？\nKami berangkat pagi-pagi sekali demi [...] kemacetan lalu lintas.",
                "options": ["A. terhindar", "B. menghindarkan", "C. menghindari", "D. berhindar"],
                "ans": "C. menghindari",
                "expl": "直接目的語（kemacetan）をとって「〜を避ける・回避する」能動動作を表すため、他動詞 menghindari が適切です。"
            }
        ],
        "peribahasa": {
            "quote": "Menghindari lubang, terperosok ke parit.",
            "meaning": "穴を避けようとして溝に落ちる＝一つの小さな災難を避けようとして、かえって別の大きな災難に見舞われること（一難去ってまた一難）。"
        }
    }
]

def generate_markdown(a):
    matrix_rows = ""
    for word, aff, pos, meaning, ex in a["matrix"]:
        matrix_rows += f"| **{word}** | `{aff}` | {pos} | {meaning} | {ex} |\n"

    details_content = ""
    for word, pos, kana, desc, coloc, id_ex, ja_ex in a["details"]:
        details_content += f"""### {word}（{pos}）
- **発音**: `{kana}`
- **意味・語法ニュアンス**: {desc}
- **重要コロケーション**: {coloc}

<div class="id-example">
<div class="id-example-item">
<div class="id-example-id">{id_ex}</div>
<div class="id-example-ja">{ja_ex}</div>
</div>
</div>

"""

    dialogue_lines = ""
    for speaker, line in a["dialogue"]["lines"]:
        dialogue_lines += f"""<div class="dialogue-line">
  <div class="speaker-name">{speaker}</div>
  <div class="speech-bubble">{line}</div>
</div>\n"""

    grammar_items = ""
    for title, desc in a["grammar_points"]:
        grammar_items += f"""#### {title}
{desc}

"""

    quiz_items = ""
    for i, q in enumerate(a["quizzes"], 1):
        options_str = "\n".join([f"- {opt}" for opt in q["options"]])
        quiz_items += f"""**Q{i}. {q['q']}**
{options_str}

<details>
<summary>正解と解説を見る</summary>

**正解**: 「**{q['ans']}**」

**解説**:
{q['expl']}
</details>

"""

    peribahasa_content = f"""<div class="id-example">
<div class="id-example-item">
<div class="id-example-id">{a['peribahasa']['quote']}</div>
<div class="id-example-ja">{a['peribahasa']['meaning']}</div>
</div>
</div>"""

    md = f"""---
title: "{a['title']}"
description: "インドネシア語の重要語根【{a['root']}】のコアミーニングから派生語一覧、詳細例文、実践会話ダイアログ、文法比較、確認クイズまで徹底解説。"
---

<div class="category-badge">語根別派生語マスター図鑑</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 12分</span>
  <span class="meta-item"><i class="fas fa-signal"></i> 中級〜上級（CEFR A2〜B2）</span>
</div>

---

## 1. 語根のコア概念と派生ネットワーク

語根 **{a['root']}** は、基本的に「**{a['core_meaning']}**」というコア概念を持ちます。

{a['explanation']}

---

## 2. 派生語一覧マトリックス

語根 **{a['root']}** から派生する主要な単語と接辞パターンの一覧です。

| 派生語 | 接辞 | 品詞 | 日本語の主な意味 | 典型的な例文 |
| :--- | :--- | :--- | :--- | :--- |
{matrix_rows}

---

## 3. 主要派生語の精密解説と例文カード

{details_content}

---

## 4. 実践会話ダイアログ

語根 **{a['root']}** の派生語が実際のネイティブの会話でどのように使われるかを体験しましょう。

### {a['dialogue']['title']}

<div class="dialogue-box">
{dialogue_lines}
</div>

---

## 5. 接辞の使い分け・文法比較のポイント

{grammar_items}

---

## 6. 定着確認クイズ

学んだ知識を定着させるための3問クイズです。各問題の選択肢を選んだ後、「正解と解説を見る」をクリックして確認してください。

{quiz_items}

---

## 7. 語源・文化コラム（Peribahasa）

インドネシアの伝統的なことわざ（Peribahasa）にも語根 **{a['root']}** を用いた表現が多く見られます。

{peribahasa_content}

---

## 8. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "derivations-2")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
