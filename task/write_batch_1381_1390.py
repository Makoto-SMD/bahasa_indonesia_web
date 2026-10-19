# -*- coding: utf-8 -*-
"""
セクション33 第4バッチ (1381-1390) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾
"""

import os

articles = [
    {
        "filename": "131-root-cegah.md",
        "title": "1381. 語根 cegah の全派生語図鑑（mencegah, pencegahan, tercegah, pencegah）",
        "root": "cegah",
        "core_meaning": "防ぐ、予防する、阻止する、食い止める、妨げる",
        "explanation": "語根 cegah は、病気、犯罪、事故、腐敗などの好ましくない事態が「発生する前に先手を打って食い止める」予防・阻止のコアを持ちます。日常の健康管理（mencegah penyakit）から警察・法務による犯罪抑止（pencegahan korupsi）、予防薬や抑止剤（pencegah）まで、社会防衛の必須語根です。",
        "matrix": [
            ("cegah", "語根", "動詞・命令", "防ぐ、阻止せよ（通常は接辞を伴う）", "Cegah penularan virus dengan selalu mencuci tangan pakai sabun."),
            ("mencegah", "meN-", "他動詞", "防ぐ、予防する、阻止する、食い止める", "Olahraga rutin efektif mencegah risiko serangan jantung."),
            ("pencegahan", "peN- -an", "名詞", "予防、防止、阻止策、抑止プロセス", "Pencegahan tindak pidana korupsi memerlukan transparansi anggaran."),
            ("tercegah", "ter-", "受動・可能動詞", "阻止される、防ぎ止められる", "Konflik komunal akhirnya tercegah berkat mediasi tokoh adat."),
            ("pencegah", "peN-", "名詞", "予防薬、防止器具、阻止するもの", "Vaksin ini berfungsi sebagai pencegah infeksi saluran pernapasan."),
            ("mencegah lebih baik", "frasa", "成句・格言", "予防は治療に勝る", "Mencegah lebih baik daripada mengobati adalah prinsip hidup sehat.")
        ],
        "details": [
            ("mencegah", "他動詞", "ムンチュガハ",
             "病気、災害、不正、事故などを未然に「防ぐ・食い止める」最も一般的な動詞です。",
             "mencegah korupsi（汚職を防止する）, mencegah banjir（洪水を防ぐ）, mencegah penyebaran hoaks（デマの拡散を阻止する）",
             "Pemerintah memasang rambu lalu lintas baru untuk mencegah kecelakaan di tikungan tajam.",
             "政府は急カーブでの事故を防止するため、新たな道路標識を設置した。"),
            ("pencegahan", "名詞", "プンチュガハン",
             "医療・警察・防災における「予防策、防止活動、抑止メカニズム」を指す公的用語です。",
             "Komisi Pemberantasan Korupsi / KPK（汚職撲滅委員会での予防部門）, langkah pencegahan（予防措置）, pencegahan dini（早期予防）",
             "Langkah pencegahan kebakaran hutan melibatkan patroli terpadu dan pemadaman titik api.",
             "森林火災の予防措置には、合同パトロールと熱源スポットの消火活動が含まれる。"),
            ("pencegah", "名詞", "プンチュガハ",
             "病原菌や害虫、錆びなどを「防ぐための薬剤・道具・要因」を指します。",
             "obat pencegah mabuk perjalanan（乗り物酔い止め薬）, cat pencegah karat（防錆塗料）",
             "Krim ini mengandung formula khusus pencegah gigitan nyamuk demam berdarah.",
             "このクリームはデング熱の蚊の刺傷を防止する特殊成分を含んでいる。"),
            ("tercegah", "動詞", "トゥルチュガハ",
             "周囲の努力や早期対応によって、大惨事や衝突が「未然に防がれた・食い止められた」状態です。",
             "bencana tercegah（大惨事が防がれる）, krisis tercegah（危機が回避される）",
             "Tawuran antarpelajar berhasil tercegah berkat kesigapan aparat kepolisian berpatroli.",
             "警察官によるパトロールの迅速さのおかげで、学生同士の集団乱闘は未然に防がれた。")
        ],
        "dialogue": {
            "title": "企業のコンプライアンスと情報漏洩防止ミーティング",
            "lines": [
                ("Budi", "Bagaimana sistem keamanan siber kita dalam mencegah upaya peretasan data nasabah?"),
                ("Rian", "Kami telah memperbarui firewall dan menerapkan autentikasi dua faktor untuk pencegahan kebocoran data."),
                ("Budi", "Bagus. Kebocoran data harus tercegah sejak dini agar reputasi perusahaan tetap terjaga."),
                ("Rian", "Siap, Pak. Langkah pencegahan ini akan terus dievaluasi secara berkala.")
            ]
        },
        "grammar_points": [
            ("cegah vs hindar", "cegah（mencegah）は事態そのものを「発生させないよう未然に食い止める・阻止する（prevent）」。hindar（menghindari）は既に存在する危険から「身をかわして避ける（avoid）」。"),
            ("語根頭文字 c と meN- の鼻音化", "語根頭文字 c は接頭辞 meN- が付いても脱落せず、men-cegah となる規則（c は k, p, s, t と違って脱落しない）。")
        ],
        "quizzes": [
            {
                "q": "「予防は治療に勝る」に相当する有名なインドネシア語の格言はどれか？",
                "options": ["A. Mencegah lebih baik daripada mengobati", "B. Menghindari lebih baik daripada berobat", "C. Tercegah lebih baik daripada sakit", "D. Pencegahan lebih baik daripada sehat"],
                "ans": "A. Mencegah lebih baik daripada mengobati",
                "expl": "医学・健康の黄金格言として「Mencegah lebih baik daripada mengobati（防ぐことは治すことより良い）」と言います。"
            },
            {
                "q": "「早期の予防措置をとる」をインドネシア語で表現したものはどれか？",
                "options": ["A. mengambil langkah pencegahan dini", "B. membuat pencegah dini", "C. mencegah awal langkah", "D. tercegah langkah cepat"],
                "ans": "A. mengambil langkah pencegahan dini",
                "expl": "「langkah pencegahan dini（早期予防措置）」に動詞 mengambil（取る）を結びつけた定型コロケーションです。"
            },
            {
                "q": "「防錆塗料（サビを防ぐペンキ）」を表す表現はどれか？",
                "options": ["A. cat tercegah karat", "B. cat pencegah karat", "C. cat mencegah karat", "D. cat pencegahan karat"],
                "ans": "B. cat pencegah karat",
                "expl": "〜を防ぐための器具・薬剤・薬品には道具名詞の pencegah を使い「cat pencegah karat」と表現します。"
            }
        ],
        "peribahasa": {
            "quote": "Sedia payung sebelum hujan.",
            "meaning": "雨が降る前に傘を用意せよ＝転ばぬ先の杖。災難や困難が訪れる前に、万全の予防・準備をしておくべきであるという教訓。"
        }
    },
    {
        "filename": "132-root-lindung.md",
        "title": "1382. 語根 lindung の全派生語図鑑（melindungi, perlindungan, pelindung, terlindung）",
        "root": "lindung",
        "core_meaning": "守る、保護する、庇護する、隠れる、覆い隠す",
        "explanation": "語根 lindung は、外敵や風雨、危険から身を「覆い守る・庇護する」原義を持ちます。法的な人権擁護（perlindungan HAM）から希少動植物の保護（melindungi satwa langka）、ヘルメットなどの防具（alat pelindung diri）、守られた安全な環境（terlindung）まで、人道と安全を支える基本語根です。",
        "matrix": [
            ("lindung", "語根", "自動詞", "身を隠す、保護される（通常接辞付き）", "Kucing itu mencari tempat lindung saat hujan badai melanda."),
            ("melindungi", "meN- -i", "他動詞", "守る、保護する、庇護する、防御する", "Undang-undang dibuat untuk melindungi hak-hak seluruh warga negara."),
            ("perlindungan", "per- -an", "名詞", "保護、庇護、防護体制、保障", "Saksi kunci dalam kasus korupsi mendapat perlindungan khusus dari LPSK."),
            ("pelindung", "peN-", "名詞", "保護者、後援者、防具、盾", "Helm standar SNI berfungsi sebagai pelindung kepala pengendara motor."),
            ("terlindung", "ter-", "受動・状態動詞", "守られている、遮蔽されている、安全な", "Kawasan teluk ini terlindung dari deburan ombak besar samudra."),
            ("melindungkan", "meN- -kan", "他動詞", "〜を庇う、〜を避難させる、隠す", "Ibu itu melindungkan anaknya di balik tubuhnya saat terjadi kerusuhan."),
            ("alat pelindung diri", "frasa", "名詞句・略語APD", "個人防護具（PPE）", "Tenaga medis wajib mengenakan alat pelindung diri saat menangani wabah.")
        ],
        "details": [
            ("melindungi", "他動詞", "ムリンドゥンギ",
             "危険、攻撃、寒さ、風雨から対象を「守る・保護する」最も代表的な他動詞です。",
             "melindungi hak cipta（著作権を保護する）, melindungi konsumen（消費者を保護する）, melindungi lingkungan（環境を保護する）",
             "Hutan bakau memiliki peran ekologis krusial untuk melindungi pesisir dari ancaman abrasi laut.",
             "マングローブ林は、海岸を波の浸食の脅威から守る上で極めて重要な生態学的役割を果たしている。"),
            ("perlindungan", "名詞", "プルリンドゥンガン",
             "法律、制度、施設による「保護、救済、保障制度」を指す最重要法務・行政名詞です。",
             "perlindungan anak（児童保護）, perlindungan data pribadi（個人データ保護）, LPSK（証人被害者保護庁）",
             "Pemerintah mengesahkan regulasi baru mengenai perlindungan data pribadi di ruang siber.",
             "政府はサイバー空間における個人データ保護に関する新たな規制を成立させた。"),
            ("pelindung", "名詞", "プリンズン",
             "人を危険から守る「防具、守護者、パトロン、保護膜」を指します。",
             "malaikat pelindung（守護天使）, pelindung layar / screen protector（画面保護フィルム）",
             "Pekerja konstruksi diwajibなく menggunakan rompi pelindung dan sepatu keselamatan di area proyek.",
             "建設作業員はプロジェクト現場において保護ベストと安全靴の着用が義務付けられている。"),
            ("terlindung", "状態動詞", "トゥルリンドゥン",
             "屋根や壁、法律の庇護のもとにあって「守られている、危害が及ばない」安全な状態です。",
             "terlindung dari sinar matahari（日光から遮られている）, hidup terlindung（温室育ちの生活）",
             "Koleksi naskah kuno disimpan di ruang berpendingin agar terlindung dari kerusakan cuaca.",
             "古写本のコレクションは、天候による劣化から保護されるよう温度管理された部屋に保管されている。")
        ],
        "dialogue": {
            "title": "個人情報保護法（UU PDP）の社内遵守に関する対話",
            "lines": [
                ("Hana", "Pak Doni, bagaimana kesiapan perusahaan kita memenuhi regulasi perlindungan data pribadi nasabah?"),
                ("Doni", "Tim legal dan IT sudah menyusun protokol enkripsi baru untuk melindungi data transaksi dari kebocoran."),
                ("Hana", "Bagus sekali. Kepercayaan publik akan runtuh jika data mereka tidak terlindung dengan baik."),
                ("Doni", "Tepat. Kita harus menjadi institusi yang mampu memberikan rasa aman dan perlindungan maksimal.")
            ]
        },
        "grammar_points": [
            ("接頭辞 per-...-an vs peN-...-an", "lindung から派生する名詞は perlindungan（保護制度・状態）であり、pelindungan ではない点に注意。名詞 pelindung は人や防具を表す。"),
            ("LPSK（Lembaga Perlindungan Saksi dan Korban）", "インドネシアの司法ニュースで頻出する「証人被害者保護庁」。裁判で証言する重要証人の身辺警護を行う国家機関。")
        ],
        "quizzes": [
            {
                "q": "医療現場や建設現場で用いられる「個人防護具（PPE）」のインドネシア語略称（APD）の正式名称はどれか？",
                "options": ["A. Alat Pelindung Diri", "B. Asosiasi Perlindungan Dokter", "C. Alat Pengaman Daerah", "D. Aset Penjaga Darurat"],
                "ans": "A. Alat Pelindung Diri",
                "expl": "個人防護具は「Alat Pelindung Diri（略称 APD）」と言います。"
            },
            {
                "q": "インドネシアの「個人データ保護法」を正しく表現したものはどれか？",
                "options": ["A. UU Perlindungan Data Pribadi", "B. UU Melindungi Data Pribadi", "C. UU Pelindung Data Pribadi", "D. UU Terlindung Data Pribadi"],
                "ans": "A. UU Perlindungan Data Pribadi",
                "expl": "制度・保護法規には名詞 perlindungan を用いて「UU Perlindungan Data Pribadi（UU PDP）」と呼びます。"
            },
            {
                "q": "「このサンゴ礁の海域は外洋の荒波から守られている」の空欄に入る語は？\nKawasan terumbu karang ini [...] dari hantaman ombak laut lepas.",
                "options": ["A. melindungi", "B. terlindung", "C. perlindungan", "D. pelindung"],
                "ans": "B. terlindung",
                "expl": "主語が荒波から「守られている・遮蔽されている」受動・完了状態を表すため、terlindung が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Tempat berlindung di waktu hujan, tempat berteduh di waktu panas.",
            "meaning": "雨の時の避難場所、暑い時の日陰＝国民や家族をあらゆる災難から温かく包み守ってくれる頼もしい指導者や親の存在。"
        }
    },
    {
        "filename": "133-root-bela.md",
        "title": "1383. 語根 bela の全派生語図鑑（membela, pembelaan, pembela, terbela）",
        "root": "bela",
        "core_meaning": "擁護する、弁護する、かばう、味方する、尽くす",
        "explanation": "語根 bela は、弱者、正義、祖国、名誉のために「自らを顧みず立ち上がって擁護・弁護・防衛する」利他的で力強いコアを持ちます。裁判での弁護活動（membela terdakwa）から祖国防衛（bela negara）、弁護士や支援者（pembela）、弁護側最終陳述（pledoi / nota pembelaan）まで、正義と献身の基幹語根です。",
        "matrix": [
            ("bela", "語根", "動詞・概念", "擁護する、尽くす、防衛する", "Semangat bela negara wajib ditanamkan kepada generasi muda."),
            ("membela", "meN-", "他動詞", "擁護する、弁護する、味方する、防衛する", "Pengacara ternama itu bersedia membela hak masyarakat adat tanpa bayaran."),
            ("pembelaan", "peN- -an", "名詞", "弁護、擁護、弁明、自衛陳述", "Terdakwa membacakan nota pembelaan pribadi di hadapan majelis hakim."),
            ("pembela", "peN-", "名詞", "弁護士、擁護者、ディフェンダー（守備選手）", "Dia dikenal sebagai pembela gigih hak-hak kaum buruh perempuan."),
            ("terbela", "ter-", "受動・可能動詞", "擁護される、救われる、守られ得る", "Hak-hak korban kekerasan seksual akhirnya terbela dengan adanya undang-undang baru."),
            ("bela diri", "frasa", "名詞句", "護身術、武道（Pencak Silat等）", "Seni bela diri tradisional Pencak Silat diakui sebagai warisan budaya dunia."),
            ("bela negara", "frasa", "名詞句", "祖国防衛、国防の義務・精神", "Pendidikan bela negara bertujuan memperkuat integrasi nasional.")
        ],
        "details": [
            ("membela", "他動詞", "ムンブラ",
             "弱者や友人、被告人を「擁護・弁護する」、祖国を「防衛する」能動動作です。",
             "membela kebenaran（真理・正義を擁護する）, membela tanah air（祖国を防衛する）, membela martabat（尊厳を守る）",
             "Para pahlawan kemerdekaan rela mengorbankan jiwa dan raga demi membela kehormatan bangsa.",
             "独立の英雄たちは民族の尊厳を守るために自らの命と体を惜しみなく捧げた。"),
            ("pembelaan", "名詞", "プンブラアン",
             "裁判での「弁護、弁論、意見陳述」、あるいは批判に対する「自己正当化・釈明」を指します。",
             "nota pembelaan（弁論趣意書・Pledoi）, pembelaan diri（正当防衛・自己弁護）",
             "Tim penasihat hukum mengajukan nota pembelaan setebal seratus halaman dalam sidang pamungkas.",
             "弁護団は最終公判において100ページに及ぶ弁論趣意書を提出した。"),
            ("pembela", "名詞", "プンブラ",
             "正義の「擁護者、弁護士」、またはサッカーなどでゴールを守る「ディフェンダー（bek）」を指します。",
             "pembela HAM（人権擁護活動家）, pembela keadilan（正義の擁護者）",
             "Aktivis lingkungan itu dinobatkan sebagai pembela kelestarian hutan hujan tropis.",
             "その環境活動家は熱帯雨林の生態系保全の擁護者として表彰された。"),
            ("bela negara", "名詞句", "ブラ・ヌガラ",
             "憲法に規定された国民の「国防への参加・愛国奉仕」を表すインドネシアの重要国是です。",
             "kesadaran bela negara（国防意識）, program bela negara（愛国国防研修）",
             "Setiap warga negara memiliki hak dan kewajiban yang sama dalam upaya bela negara.",
             "すべての国民は祖国防衛の取り組みにおいて平等な権利と義務を有している。")
        ],
        "dialogue": {
            "title": "法廷での最終弁論と被告人の権利擁護",
            "lines": [
                ("Farid", "Apakah tim pengacara sudah menyelesaikan berkas nota pembelaan untuk sidang besok?"),
                ("Maya", "Sudah selesai. Kami telah menyusun argumen yuridis yang kuat untuk membela klien kita."),
                ("Farid", "Pastikan semua bukti saksi meringankan tercantum dalam pembelaan tersebut."),
                ("Maya", "Tentu. Sebagai pembela keadilan, kita harus memperjuangkan hak-haknya secara maksimal.")
            ]
        },
        "grammar_points": [
            ("bela と belah の識別", "bela（擁護する・防衛する）と belah（割る・半分にする）はスペルも意味も全く異なる単語なので混同に厳重注意（membela＝かばう、membelah＝切り割る）。"),
            ("Pledoi と nota pembelaan", "オランダ法由来の裁判用語 Pledoi（プレドイ＝最終弁論）のインドネシア語標準名詞が nota pembelaan。ニュース報道で同義として用いられる。")
        ],
        "quizzes": [
            {
                "q": "インドネシアの伝統的な武道・護身術（Pencak Silat等）を総称する言葉はどれか？",
                "options": ["A. bela diri", "B. bela negara", "C. pembelaan", "D. membela raga"],
                "ans": "A. bela diri",
                "expl": "護身術・武道は「bela diri（自己を守る）」と言います。bela negara は「祖国防衛」です。"
            },
            {
                "q": "「人権擁護活動家」を意味する標準的なインドネシア語はどれか？",
                "options": ["A. pembela HAM", "B. pelindung hukum", "C. penjaga hak", "D. pahlawan rakyat"],
                "ans": "A. pembela HAM",
                "expl": "人権（HAM＝Hak Asasi Manusia）の擁護者は「pembela HAM」と呼びます。"
            },
            {
                "q": "「弁護側が裁判官の前で読み上げる最終弁論書」を何と呼ぶか？",
                "options": ["A. nota pembelaan", "B. surat tuntutan", "C. berkas gugatan", "D. vonis hakim"],
                "ans": "A. nota pembelaan",
                "expl": "弁護側の最終弁論書は「nota pembelaan（Pledoi）」と言います。検察側の求刑書は surat tuntutan です。"
            }
        ],
        "peribahasa": {
            "quote": "Hancur badan dikandung tanah, budi baik terkenang jua.",
            "meaning": "肉体は土に還り朽ち果てようとも、善行と正義を尽くした名声は永遠に記憶され続ける。"
        }
    },
    {
        "filename": "134-root-tuntut.md",
        "title": "1384. 語根 tuntut の全派生語図鑑（menuntut, tuntutan, penuntutan, penuntut）",
        "root": "tuntut",
        "core_meaning": "要求する、請求する、起訴する、研鑽する、追究する",
        "explanation": "語根 tuntut は、あるべき正当な権利や知識を「強い意志をもって強く求める・追究する」コアを持ちます。裁判での検察による起訴・求刑（menuntut hukuman）から労働者の権利要求（tuntutan gaji）、学問を修めること（menuntut ilmu）、検察官（penuntut umum）まで、法務と向学心を象徴する重要語根です。",
        "matrix": [
            ("tuntut", "語根", "動詞・命令", "要求せよ、追究する（接辞付きが通例）", "Tuntutlah hakmu secara sah dan beradab sesuai hukum yang berlaku."),
            ("menuntut", "meN-", "他動詞", "要求する、起訴・求刑する、学問を修める", "Jaksa penuntut umum menuntut terdakwa dengan hukuman seumur hidup."),
            ("tuntutan", "-an", "名詞", "要求、請求、求刑、時代の要請", "Ribuan buruh menggelar demonstrasi damai menyampaikan tuntutan upah."),
            ("penuntutan", "peN- -an", "名詞", "起訴、訴追手続き、追究プロセス", "Proses penuntutan perkara korupsi itu dipimpin oleh jaksa senior."),
            ("penuntut", "peN-", "名詞", "起訴者、検察官（Jaksa Penuntut Umum）", "Penuntut umum membacakan berkas dakwaan di depan sidang pengadilan."),
            ("menuntut ilmu", "frasa", "成句・動詞句", "学問を修める、知識を深める", "Menuntut ilmu adalah kewajiban moral setiap manusia sepanjang hayat.")
        ],
        "details": [
            ("menuntut", "他動詞", "ムヌントゥット",
             "権利や賠償を「強く要求する」、法廷で「求刑する」、知識を「修得する」多面的な他動詞です。",
             "menuntut ganti rugi（損害賠償を請求する）, menuntut keadilan（正義を要求する）, menuntut ilmu（学問を修める）",
             "Para korban bencana menuntut transparansi dalam penyaluran dana bantuan kemanusiaan.",
             "被災者たちは人道支援金の配分における透明性を要求している。"),
            ("tuntutan", "名詞", "トゥントゥタン",
             "労働争議での「要求項目」、裁判での検察官の「求刑内容」、または時代の「ニーズ・要請」を指します。",
             "tuntutan hukum（法的要求・告訴）, tuntutan zaman（時代の要請）, tuntutan jaksa（検察官の求刑）",
             "Perusahaan akhirnya menyetujui sebagian tuntutan serikat pekerja terkait tunjangan kesehatan.",
             "会社側は最終的に、健康手当に関する労働組合の要求の一部を受け入れた。"),
            ("penuntutan", "名詞", "プヌントゥタン",
             "検察当局が容疑者を裁判所へ引き渡して責任を追及する「刑事訴追・起訴手続き」を指します。",
             "surat ketetapan penghentian penuntutan / SKP2（起訴猶予・不起訴決定書）, penuntutan pidana（刑事訴追）",
             "Kejaksaan Negeri melimpahkan berkas penuntutan kasus penyelundupan narkoba ke pengadilan.",
             "地方検察庁は麻薬密輸事件の起訴書類を裁判所に送致した。"),
            ("penuntut umum", "名詞", "プヌントゥット・ウムム",
             "公訴を提起し裁判で求刑を行う「公設検察官（JPU: Jaksa Penuntut Umum）」の公的呼称です。",
             "jaksa penuntut（公判検事）, penuntut hak（権利の請求者）",
             "Jaksa Penuntut Umum menghadirkan lima orang saksi ahli dalam sidang pembuktian.",
             "公設検察官は立証公判において5名の専門家証人を出廷させた。")
        ],
        "dialogue": {
            "title": "法廷での検察官の求刑と弁護士の対応",
            "lines": [
                ("Wawan", "Berapa lama vonis yang dituntut oleh Jaksa Penuntut Umum terhadap terdakwa?"),
                ("Ratih", "Penuntut umum menuntut hukuman penjara selama delapan tahun dan denda satu miliar rupiah."),
                ("Wawan", "Tuntutan itu cukup berat. Apakah tim kuasa hukum akan membantahnya dalam pledoi?"),
                ("Ratih", "Tentu. Kami menilai tuntutan jaksa tidak berdasar karena bukti materialnya sangat lemah.")
            ]
        },
        "grammar_points": [
            ("tuntut vs gugat の決定的区別", "tuntut（menuntut）は「要求する、刑事事件で検察が起訴・求刑する」。gugat（menggugat）は「民事裁判で訴訟を起こす（提訴する）、異議を申し立てる」。"),
            ("menuntut ilmu という文化的成句", "学問・教養を身につけることを「menuntut ilmu（知識を求める）」と表現する。預言者の格言「中国に至るとも知識を求めよ（Tuntutlah ilmu walau ke negeri Cina）」など広く定着。")
        ],
        "quizzes": [
            {
                "q": "インドネシアの法廷で「公設検察官（JPU）」を表す正式名称はどれか？",
                "options": ["A. Jaksa Penuntut Umum", "B. Hakim Penuntut Perkara", "C. Pengacara Penuntut Hukum", "D. Polisi Penuntut Umum"],
                "ans": "A. Jaksa Penuntut Umum",
                "expl": "検察官は「Jaksa Penuntut Umum（JPU）」と呼ばれます。"
            },
            {
                "q": "「労働組合は基本給の引き上げを要求している」の空欄に入る動詞は？\nSerikat buruh [...] kenaikan upah pokok sebesar sepuluh persen.",
                "options": ["A. menuntut", "B. penuntut", "C. penuntutan", "D. tertuntut"],
                "ans": "A. menuntut",
                "expl": "要求するという能動動作なので他動詞 menuntut が正解です。"
            },
            {
                "q": "「学問を修める、知識を追究する」という意味の定型成句はどれか？",
                "options": ["A. menuntut ilmu", "B. menuntut buku", "C. mencari sekolah", "D. menuntut akal"],
                "ans": "A. menuntut ilmu",
                "expl": "知識・学問の修得は慣用句として「menuntut ilmu」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Tuntutlah ilmu dari buaian hingga ke liang lahat.",
            "meaning": "揺りかごから墓場まで学問を求めよ＝生涯学習の重要性を説いた格言。"
        }
    },
    {
        "filename": "135-root-gugat.md",
        "title": "1385. 語根 gugat の全派生語図鑑（menggugat, gugatan, penggugat, tergugat）",
        "root": "gugat",
        "core_meaning": "提訴する、民事訴訟を起こす、告発する、異議を唱える",
        "explanation": "語根 gugat は、不当な権利侵害や契約違反に対して裁判所に「民事訴訟を提起する」、あるいは社会の通念や権威に「果敢に異議を申し立てる・疑問を突きつける」法務・論争のコアを持ちます。原告（penggugat）から被告（tergugat）、訴状・訴訟（gugatan）、既成概念への挑戦（menggugat tradisi）まで、法治社会と批判的思考の中核語根です。",
        "matrix": [
            ("gugat", "語根", "動詞・概念", "提訴する、訴え出る（通常接辞付き）", "Warga sepakat gugat pihak pengembang atas pencemaran limbah."),
            ("menggugat", "meN-", "他動詞", "提訴する、民事訴訟を起こす、異議を唱える", "Masyarakat adat menggugat perusahaan tambang yang merusak hutan ulayat."),
            ("gugatan", "-an", "名詞", "訴状、民事訴訟、告発、提訴案件", "Pengadilan negeri menerima berkas gugatan sengketa kepemilikan tanah."),
            ("penggugat", "peN-", "名詞", "原告、提訴者、異議申立人", "Pihak penggugat menghadirkan bukti sertifikat tanah yang sah."),
            ("tergugat", "ter-", "名詞・受動動詞", "被告（民事）、訴えられた側", "Tergugat membantah telah melakukan wanprestasi dalam perjanjian bisnis."),
            ("gugatan perdata", "frasa", "名詞句", "民事訴訟", "Penyelesaian sengketa bisnis biasanya ditempuh melalui gugatan perdata."),
            ("gugatan cerai", "frasa", "名詞句", "離婚訴訟・離婚申し立て", "Pengadilan Agama mencatat peningkatan jumlah gugatan cerai tahun ini.")
        ],
        "details": [
            ("menggugat", "他動詞", "ムングガット",
             "民事裁判で損害や権利回復を求めて「提訴する」、または古い慣習や権力に「異議を突きつける」動作です。",
             "menggugat ke pengadilan（裁判所に提訴する）, menggugat status quo（現状維持に異議を唱える）",
             "Kelompok konsumen menggugat maskapai penerbangan karena pembatalan sepihak tanpa kompensasi.",
             "消費者グループは、補償なしの一方的な欠航を理由に航空会社を提訴した。"),
            ("gugatan", "名詞", "グガタン",
             "裁判所に提出される「訴状・提訴アクション・請求」を指す民事訴訟の基本用語です。",
             "gugatan perdata（民事訴訟）, gugatan kelompok / class action（集団代表訴訟）, memenangkan gugatan（勝訴する）",
             "Majelis hakim memutuskan menolak seluruh gugatan yang diajukan oleh pihak pengusaha.",
             "裁判長団は、事業者側から提起されたすべての訴え（請求）を棄却することを決定した。"),
            ("penggugat", "名詞", "プングガット",
             "民事訴訟において訴えを起こした側である「原告」を指す法廷用語です（対義語は tergugat）。",
             "kuasa hukum penggugat（原告代理人弁護士）, dalil penggugat（原告の主張）",
             "Penggugat menuntut ganti rugi materiil sebesar sepuluh miliar rupiah atas pencemaran nama baik.",
             "原告は名誉毀損に対する100億ルピアの物質的損害賠償を請求した。"),
            ("tergugat", "名詞", "トゥルグガット",
             "民事訴訟において訴えを起こされた側である「被告」を指します（刑事裁判の被告人は terdakwa）。",
             "pihak tergugat（被告側）, replik dan duplik（原告の再反論と被告の再答弁）",
             "Pihak tergugat diberi waktu dua pekan untuk menyusun berkas jawaban atas gugatan tersebut.",
             "被告側には、その訴状に対する答弁書を作成するために2週間の猶予が与えられた。")
        ],
        "dialogue": {
            "title": "企業の契約不履行と民事訴訟の検討",
            "lines": [
                ("Hendra", "Mitra bisnis kita belum juga melunasi pembayaran proyek padahal sudah lewat enam bulan."),
                ("Sinta", "Tim hukum menyarankan agar kita segera melayangkan gugatan perdata atas tuduhan wanprestasi."),
                ("Hendra", "Apakah posisi kita sebagai penggugat cukup kuat dengan bukti-bukti kontrak yang ada?"),
                ("Sinta", "Sangat kuat. Dokumen perjanjian kerja sama dan bukti penagihan kita lengkap dan sah.")
            ]
        },
        "grammar_points": [
            ("民事の「被告（tergugat）」vs 刑事の「被告人（terdakwa）」の厳格な使い分け", "民事裁判で訴えられた側は「tergugat（被告）」、刑事裁判で罪に問われている側は「terdakwa（被告人）」。検定や実務で極めて厳密に区別される。"),
            ("class action のインドネシア語訳", "集団代表訴訟はインドネシア法上「gugatan perwakilan kelompok」と呼ばれる。公害訴訟などで頻出。")
        ],
        "quizzes": [
            {
                "q": "民事訴訟における「原告」と「被告」の正しい組み合わせはどれか？",
                "options": ["A. penggugat dan tergugat", "B. penuntut dan terdakwa", "C. hakim dan jaksa", "D. pembela dan penuduh"],
                "ans": "A. penggugat dan tergugat",
                "expl": "民事訴訟の原告は penggugat、被告は tergugat です。刑事の検察・被告人は penuntut (jaksa) と terdakwa です。"
            },
            {
                "q": "「民事訴訟を提起する」をインドネシア語で表現したものはどれか？",
                "options": ["A. mengajukan gugatan perdata", "B. membuat tuntutan pidana", "C. menuduh perkara", "D. memvonis gugatan"],
                "ans": "A. mengajukan gugatan perdata",
                "expl": "訴訟を提起することは「mengajukan gugatan（訴状を提出する）」と表現します。"
            },
            {
                "q": "裁判所が「訴えを退ける・棄却する」ことを意味する表現はどれか？",
                "options": ["A. menolak gugatan", "B. menerima gugatan", "C. mencabut gugatan", "D. menggugat balik"],
                "ans": "A. menolak gugatan",
                "expl": "裁判所が原告の請求を認めず退けることは「menolak gugatan（請求棄却）」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Kalah jadi abu, menang jadi arang dalam bersengketa.",
            "meaning": "法廷闘争で争えば、負ければ灰になり勝っても炭になる（共倒れ）＝徒に訴訟を長引かせるより、和解（perdamaian）を模索するのが賢明であるという戒め。"
        }
    },
    {
        "filename": "136-root-tolak.md",
        "title": "1386. 語根 tolak の全派生語図鑑（menolak, penolakan, tertolak, tolak ukur）",
        "root": "tolak",
        "core_meaning": "拒絶する、断る、却下する、押し返す、押し出す",
        "explanation": "語根 tolak は、迫り来るものを「手で押し返す・跳ね除ける」原義から、提案や要求を「拒絶・却下する（menolak tawaran）」、船を岸から「押し出す（bertolak）」、基準・尺度（tolak ukur）、そして魔除け（tolak bala）まで、物理的斥力と意思決定の境界線を司る重要語根です。",
        "matrix": [
            ("tolak", "語根", "動詞・命令", "断れ、拒絶せよ、押し返せ", "Tolak segala bentuk suap demi integritas profesi Anda."),
            ("menolak", "meN-", "他動詞", "拒絶する、断る、却下する、拒否する", "Dewan Direksi dengan tegas menolak tawaran akuisisi hostile tersebut."),
            ("penolakan", "peN- -an", "名詞", "拒絶、却下、拒絶反応、不承認", "Keputusan itu memicu gelombang penolakan dari serikat pekerja."),
            ("tertolak", "ter-", "受動・可能動詞", "拒絶された、却下された、弾かれた", "Pengajuan visa turisnya tertolak karena paspor masa berlakunya kurang."),
            ("bertolak", "ber-", "自動詞", "出発する、（〜に）基づく、立脚する", "Kapal pesiar itu dijadwalkan bertolak dari pelabuhan besok pagi."),
            ("tolak ukur", "frasa", "名詞句", "尺度、基準、ベンチマーク（tolok ukur）", "Indeks kepuasan pelanggan menjadi tolak ukur keberhasilan layanan kami."),
            ("tolak bala", "frasa", "名詞句・民俗", "厄除け、魔除けの儀礼", "Warga desa menggelar ritual tolak bala untuk memohon keselamatan dari wabah.")
        ],
        "details": [
            ("menolak", "他動詞", "ムノラック",
             "誘い、提案、ビザ申請、判決請求などを明確に「拒絶する・断る・却下する」動詞です。",
             "menolak permohonan（申請を却下する）, menolak ajakan（誘いを断る）, menolak gratifikasi（賄賂・謝礼の受け取りを拒否する）",
             "Pegawai negeri sipil wajib menolak segala bentuk gratifikasi yang berkaitan dengan jabatannya.",
             "公務員はその職務に関連するいかなる形の贈答・謝礼も拒否する義務がある。"),
            ("penolakan", "名詞", "プノラカン",
             "社会的な「反対運動」、医学的な「拒絶反応」、公的手続きの「却下」を指します。",
             "penolakan warga（住民の反対）, penolakan cangkok organ（臓器移植の拒絶反応）, surat penolakan（却下通知書）",
             "Rancangan undang-undang itu menuai gelombang penolakan luas dari kalangan akademisi.",
             "その法案は学術界から広範な反対の波を巻き起こした。"),
            ("bertolak", "自動詞", "ブルトラック",
             "船や飛行機が港・空港から「旅立つ・出発する」、または議論が特定の前提に「立脚する」ことを表します。",
             "bertolak dari pelabuhan（港を出発する）, bertolak dari fakta（事実に基づいている）",
             "Analisis ekonomi ini bertolak dari asumsi bahwa inflasi akan tetap terkendali.",
             "この経済分析は、インフレが依然として制御下に置かれるという前提に基づいている。"),
            ("tolak ukur", "名詞句", "トラック・ウクール",
             "成果や品質を客観的に評価するための「基準、尺度、物差し（ベンチマーク）」です。",
             "menjadi tolak ukur（基準となる）, tolak ukur keberhasilan（成功の物差し）",
             "Tingkat literasi digital generasi muda menjadi tolak ukur kemajuan pendidikan modern.",
             "若者のデジタルリテラシーの度合いが、現代教育の進歩を測る尺度となっている。")
        ],
        "dialogue": {
            "title": "ビジネス提案の辞退と角を立てない断り方",
            "lines": [
                ("Sinta", "Bagaimana kita menyampaikan penolakan kerja sama ini kepada calon vendor tanpa merusak hubungan baik?"),
                ("Rudy", "Kita harus menolak secara sopan dengan menjelaskan bahwa fokus anggaran tahun ini dialihkan ke proyek lain."),
                ("Sinta", "Baik. Apakah penolakan ini perlu disertai surat resmi perusahaan?"),
                ("Rudy", "Iya, kirimkan surat resmi bernada apresiatif agar mereka tetap terbuka untuk peluang di masa depan.")
            ]
        },
        "grammar_points": [
            ("bertolak dari の構文用法", "「〜に立脚する、〜を出発点とする」という抽象的論理接続表現として論説文で多用される（英語の based on / starting from）。"),
            ("tolak ukur と tolok ukur の正書法", "KBBI（大辞典）では元来「tolok ukur（tolok＝秤・標準）」が標準とされたが、現在では慣用的に「tolak ukur」も広く流通している。")
        ],
        "quizzes": [
            {
                "q": "「評価基準・尺度（ベンチマーク）」を意味するインドネシア語の表現はどれか？",
                "options": ["A. tolak ukur", "B. tolak bala", "C. penolakan nilai", "D. bertolak ukur"],
                "ans": "A. tolak ukur",
                "expl": "物差し・評価基準は「tolak ukur（または tolok ukur）」と言います。"
            },
            {
                "q": "「その船はジャカルタのタンジュン・プリオク港からシンガポールへ向けて出航した」の空欄に入る動詞は？\nKapal kargo itu [...] dari Pelabuhan Tanjung Priok menuju Singapura.",
                "options": ["A. bertolak", "B. menolak", "C. tertolak", "D. penolakan"],
                "ans": "A. bertolak",
                "expl": "船や乗り物が港を出港・出発する自動詞は「bertolak」を用います。"
            },
            {
                "q": "「インドネシアの伝統的な厄除け・魔除けの儀礼」を指す表現はどれか？",
                "options": ["A. tolak ukur", "B. tolak bala", "C. menolak angin", "D. tolak rugi"],
                "ans": "B. tolak bala",
                "expl": "厄除け・災難除けは「tolak bala（bala＝災難・天災）」と呼びます。"
            }
        ],
        "peribahasa": {
            "quote": "Menolak tuah, merangkul celaka.",
            "meaning": "幸運（tuah）を拒絶して災難を抱きしめる＝目の前にある良縁や幸福を無碍に断り、かえって破滅を招く愚かさを戒めることわざ。"
        }
    },
    {
        "filename": "137-root-terima.md",
        "title": "1387. 語根 terima の全派生語図鑑（menerima, penerimaan, keterbukaan, terima kasih）",
        "root": "terima",
        "core_meaning": "受ける、受け取る、受け入れる、受諾する、感謝する",
        "explanation": "語根 terima は、手渡された物体を「受領する」物理的動作から、意見や運命を「受け入れる・受諾する（menerima takdir/kenyataan）」、学生や新入社員を「採用・合格させる（diterima）」、そして世界中で知られる感謝の言葉「ありがとう（terima kasih＝愛を受け取る）」まで、受容と温かい人間関係を象徴する語根です。",
        "matrix": [
            ("terima", "語根", "動詞", "受ける、受領する（通常接辞付き）", "Terima apa adanya adalah kunci kedamaian batin."),
            ("menerima", "meN-", "他動詞", "受け取る、受領する、受け入れる、採用する", "Dia dengan gembira menerima tawaran beasiswa studi ke luar negeri."),
            ("penerimaan", "peN- -an", "名詞", "受領、受け入れ、採用、歳入・収入", "Penerimaan pajak negara melampaui target pada akhir tahun anggaran."),
            ("diterima", "di-", "受動態動詞", "受け取られる、合格する、採用される", "Adik saya sangat bersyukur diterima di universitas negeri ternama."),
            ("keterimaan", "ke- -an", "名詞・専門", "受容性、アクセプタビリティ", "Tingkat keterimaan teknologi baru dipengaruhi oleh kemudahan penggunaannya."),
            ("berterima kasih", "ber-", "自動詞", "感謝する、お礼を言う", "Kami ingin berterima kasih atas dukungan tulus seluruh masyarakat."),
            ("terima bersih", "frasa", "成句・経済", "手取りで受け取る（控除後）", "Gaji yang ia peroleh setiap bulan adalah lima juta rupiah terima bersih.")
        ],
        "details": [
            ("menerima", "他動詞", "ムヌリマ",
             "手紙や贈り物を受け取る、提案を受け入れる、運命を甘受する、新人を採用する万能動詞です。",
             "menerima kenyataan（現実を受け入れる）, menerima tamu（来客をもてなす・迎える）, menerima suap（賄賂を受け取る）",
             "Kita harus belajar menerima perbedaan pendapat demi menjaga keharmonisan bersama.",
             "私たちは共同体の調和を保つために、意見の相違を受け入れることを学ばねばならない。"),
            ("penerimaan", "名詞", "プヌリマアン",
             "国家の税収や企業の「歳入・売上」、あるいは新入生・新入社員の「受け入れ・採用プロセス」を指します。",
             "penerimaan negara bukan pajak / PNBP（非税収歳入）, penerimaan mahasiswa baru（新入生受け入れ）",
             "Kementerian Keuangan melaporkan bahwa penerimaan kas negara tumbuh positif.",
             "財務省は国家財政の歳入がプラス成長を遂げたと報告した。"),
            ("diterima", "受動態動詞", "ディトゥリマ",
             "入試に「合格する」、面接を通過して「採用される」際に最もよく使われるお祝いの言葉です。",
             "diterima kerja（就職が決まる）, diterima di perguruan tinggi（大学に合格する）",
             "Selamat atas keberhasilanmu diterima bekerja di perusahaan multinasional itu!",
             "その多国籍企業への採用（就職決定）、本当におめでとう！"),
            ("berterima kasih", "動詞", "ブルトゥリマ・カシヒ",
             "「terima kasih（ありがとう）」を動詞化して、公式に「〜に感謝の意を表する」表現です。",
             "berterima kasih kepada donor（寄付者に感謝する）, ucapan terima kasih（謝辞・感謝の言葉）",
             "Panitia ingin berterima kasih yang sebesar-besarnya kepada seluruh sponsor pendukung acara.",
             "実行委員会は、イベントを支援してくださったすべてのスポンサーの皆様に心より感謝申し上げます。")
        ],
        "dialogue": {
            "title": "就職活動の合格通知と感謝の報告",
            "lines": [
                ("Nadia", "Ibu, kabar gembira! Saya baru saja menerima email pengumuman dari kementerian."),
                ("Ibu", "Alhamdulillah! Apakah kamu diterima sebagai pegawai negeri, Nak?"),
                ("Nadia", "Iya, Bu! Saya diterima di divisi hubungan internasional. Saya sangat berterima kasih atas doa Ibu."),
                ("Ibu", "Selamat, sayang. Semoga penerimaan ini menjadi awal berkah bagi pengabdianmu pada negara.")
            ]
        },
        "grammar_points": [
            ("terima kasih の語源的成り立ち", "terima（受け取る）+ kasih（愛・慈しみ）＝「あなたの愛（好意）を受け取りました」という温かい心情が凝縮された感謝の挨拶。"),
            ("diterima の慣用用法（合格・採用）", "インドネシア語では「試験に合格した」を「lulus ujian」というだけでなく、組織側から「受け入れられた」という意味で「Saya diterima di UI（東大/インドネシア大学に合格した）」と極めて自然に表現する。")
        ],
        "quizzes": [
            {
                "q": "大学の入試に「合格した」、企業に「採用された」ことを表す最も自然な日常表現はどれか？",
                "options": ["A. diterima", "B. penerimaan", "C. berterima", "D. keterimaan"],
                "ans": "A. diterima",
                "expl": "学校や企業に合格・採用されることは「diterima di...」と受動態で表現します。"
            },
            {
                "q": "国家の「税収・歳入」を意味する財政用語はどれか？",
                "options": ["A. pengeluaran pajak", "B. penerimaan pajak", "C. penerima kas", "D. tarikan pajak"],
                "ans": "B. penerimaan pajak",
                "expl": "税金による歳入は「penerimaan pajak」と言います。支出は pengeluaran です。"
            },
            {
                "q": "手取り額（控除後の純受取額）を意味するビジネス成句はどれか？",
                "options": ["A. terima bersih", "B. terima kasih", "C. terima kotor", "D. terima jadi"],
                "ans": "A. terima bersih",
                "expl": "税金や保険料が引かれた後の手取り受取額は「terima bersih（綺麗に受け取る）」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Budi baik orang kenang selalu, air susu dibalas air tuba jangan ditiru.",
            "meaning": "人の恩義や親切は常に感謝して記憶せよ。母乳（善意）に毒水（悪意）で返すような恩知らずの振る舞いをしてはならない。"
        }
    },
    {
        "filename": "138-root-tolong.md",
        "title": "1388. 語根 tolong の全派生語図鑑（menolong, pertolongan, penolong, tertolong）",
        "root": "tolong",
        "core_meaning": "助ける、救助する、手助けする、〜してください（依頼）",
        "explanation": "語根 tolong は、生命の危機や重大な困難に直面した者を「救い出す・助命する」人道救助のコアを持ちます。緊急時の「助けて！（Tolong!）」から日常の丁寧な依頼（tolong bantu saya）、応急処置（pertolongan pertama / P3K）、救世主・恩人（penolong）まで、人間社会の絆を象徴する最頻出語根です。",
        "matrix": [
            ("tolong", "語根", "感動詞・助詞", "助けて！、どうか〜してください（依頼詞）", "Tolong jangan merokok di dalam ruangan ber-AC ini."),
            ("menolong", "meN-", "他動詞", "助ける、救助する、手助けする、救う", "Warga bahu-membahu menolong korban kecelakaan bus tersebut."),
            ("pertolongan", "per- -an", "名詞", "援助、救助、救済、手当", "Korban tenggelam itu segera mendapat pertolongan pertama dari penjaga pantai."),
            ("penolong", "peN-", "名詞", "救助者、恩人、助け手、救世主", "Dia menganggap dokter bedah itu sebagai malaikat penolong hidupnya."),
            ("tertolong", "ter-", "受動・可能動詞", "助かる、命拾いする、救命され得る", "Beruntung pasien kritis itu masih tertolong setelah operasi darurat."),
            ("minta tolong", "frasa", "成句・動詞", "助けを求める、依頼する", "Jangan ragu minta tolong jika Anda mengalami kesulitan teknis."),
            ("pertolongan pertama", "frasa", "名詞句・略語P3K", "応急手当、ファーストエイド", "Setiap kendaraan wajib menyediakan kotak pertolongan pertama pada kecelakaan.")
        ],
        "details": [
            ("tolong", "助詞・間投詞", "トロン",
             "人に依頼するときの丁寧なクッション言葉（〜してください）、または叫び声「助けて！」です。",
             "Tolong ambilkan dokumen itu.（その書類を取ってください）, Tolong! Ada pencuri!（助けて！泥棒だ！）",
             "Tolong kirimkan laporan keuangan kuartal ini ke alamat email saya sebelum sore.",
             "夕方までに私のメールアドレスに今期の財務報告書を送ってください。"),
            ("menolong", "他動詞", "ムノロン",
             "事故や溺水、貧困、病気の他者を「救う・手助けする」人道的動詞です。",
             "menolong sesama（同胞を助ける）, menolong jiwa manusia（人命を救う）",
             "Relawan kemanusiaan bekerja tanpa lelah menolong warga yang terisolasi banjir.",
             "人道ボランティアたちは洪水で孤立した住民を救助するために休むことなく働いた。"),
            ("pertolongan", "名詞", "プルトロンガン",
             "救護、救命処置、神や人からの「助け・恩恵」を指す名詞です。",
             "Pertolongan Pertama pada Kecelakaan / P3K（応急手当ボックス）, memohon pertolongan（救いを乞う）",
             "Berkat pertolongan cepat dari tim paramedis, pendarahan korban dapat dihentikan.",
             "救急救命士チームの迅速な手当てのおかげで、被害者の出血を止めることができた。"),
            ("tertolong", "可能動詞", "トゥルトロン",
             "処置が間に合って「助かった・救命された」（否定形 tidak tertolong＝手遅れで死亡した）を表します。",
             "nyawanya tertolong（一命を取り留めた）, tidak tertolong lagi（もはや助からなかった）",
             "Meskipun dokter telah berupaya maksimal, nyawa korban tabrakan itu tidak tertolong.",
             "医師たちは全力を尽くしたものの、その衝突事故被害者の命は助からなかった。")
        ],
        "dialogue": {
            "title": "オフィスでの急病人と救急対応",
            "lines": [
                ("Rina", "Pak Hendra tiba-tiba pingsan di ruang rapat! Tolong panggilkan tim medis gedung!"),
                ("Andi", "Tenang, saya sudah menghubungi dokter. Mari kita berikan pertolongan pertama."),
                ("Rina", "Ambilkan kotak P3K di dekat resepsionis untuk memeriksa denyut nadi beliau."),
                ("Andi", "Syukurlah, napasnya masih teratur. Semoga beliau segera tertolong dan pulih kembali.")
            ]
        },
        "grammar_points": [
            ("tolong vs bantu の違い", "tolong は主に「生命の危機、重大なトラブルからの救助（rescue/help in crisis）」。bantu は日常業務や作業の「補助・手伝い・アシスト（assist/support）」。依頼詞としても tolong はよりフォーマルかつ丁寧。"),
            ("P3K（Pertolongan Pertama Pada Kecelakaan）", "救急箱や応急手当を指すインドネシアで最も有名な略語。家庭やオフィス、車内に常備される。")
        ],
        "quizzes": [
            {
                "q": "インドネシア語で「救急箱（ファーストエイドキット）」を表す略称はどれか？",
                "options": ["A. APD", "B. P3K", "C. KPK", "D. BUMN"],
                "ans": "B. P3K",
                "expl": "Pertolongan Pertama Pada Kecelakaan の頭文字をとって「P3K」と言います。"
            },
            {
                "q": "医師の手当てが間に合わず「一命を取り留めることができなかった（亡くなった）」を表す定型句はどれか？",
                "options": ["A. nyawanya tidak tertolong", "B. pertolongan ditolak", "C. menolong jiwa", "D. tidak bertolong"],
                "ans": "A. nyawanya tidak tertolong",
                "expl": "命が助からなかったことは「nyawanya tidak tertolong」と表現します。"
            },
            {
                "q": "「ドアを閉めてください」と丁寧に頼むときの正しい依頼文はどれか？",
                "options": ["A. Tolong tutup pintunya.", "B. Pertolongan tutup pintu.", "C. Menolong pintu tutup.", "D. Tertolong tutup pintunya."],
                "ans": "A. Tolong tutup pintunya.",
                "expl": "依頼のクッション言葉として文頭に tolong を置き「Tolong tutup pintunya」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Tolong-menolong adalah sendi kehidupan bermasyarakat.",
            "meaning": "相互扶助（助け合い）こそが共同体社会生活の礎石（基本原理・ゴトンロヨン精神）である。"
        }
    },
    {
        "filename": "139-root-bantu.md",
        "title": "1389. 語根 bantu の全派生語図鑑（membantu, bantuan, pembantu, terbantu）",
        "root": "bantu",
        "core_meaning": "手伝う、支援する、補助する、役に立つ、家政婦",
        "explanation": "語根 bantu は、誰かの作業、負担、経済的苦境を「横から支えて負担を軽くする」支援・アシストのコアを持ちます。日常の手伝い（membantu ibu）から国際人道支援（bantuan internasional）、政府の社会保障給付金（bansos / bantuan sosial）、大いに助かること（sangat terbantu）まで、共生社会の土台となる語根です。",
        "matrix": [
            ("bantu", "語根", "動詞・命令", "手伝え、支援せよ（通常接辞付き）", "Bantu sesama tanpa memandang latar belakang suku dan agama."),
            ("membantu", "meN-", "他動詞", "手伝う、支援する、助けとなる、促進する", "Teknologi kecerdasan buatan dapat membantu mempercepat analisis data."),
            ("bantuan", "-an", "名詞", "支援、援助、補助金、救援物資", "Pemerintah menyalurkan bantuan sosial tunai bagi keluarga pra-sejahtera."),
            ("pembantu", "peN-", "名詞", "お手伝いさん、家政婦（ART）、補助具、助手", "Asisten rumah tangga dahulu sering disebut sebagai pembantu rumah tangga."),
            ("terbantu", "ter-", "受動・可能動詞", "助かる、支援を受ける、負担が軽くなる", "Para pelaku UMKM merasa sangat terbantu dengan adanya pinjaman bunga rendah."),
            ("membantukan", "meN- -kan", "他動詞", "〜を応援に回す、応援派遣する", "Polda membantukan ratusan personel pengamanan ke daerah rawan."),
            ("bantuan hukum", "frasa", "名詞句", "法律扶助、無料弁護支援", "Lembaga Bantuan Hukum (LBH) memberikan advokasi cuma-cuma bagi warga miskin.")
        ],
        "details": [
            ("membantu", "他動詞", "ムンバントゥ",
             "誰かの仕事を手伝う、生活を支援する、あるいは道具が作業の「助けになる」万能動詞です。",
             "membantu korban bencana（被災者を支援する）, sangat membantu（とても役に立つ）, membantu menyelesaikan tugas（課題の解決を手伝う）",
             "Aplikasi navigasi digital ini sangat membantu pengemudi menemukan rute tercepat.",
             "このデジタルナビアプリは、運転手が最短ルートを見つける上で大いに役立っている。"),
            ("bantuan", "名詞", "バントゥアン",
             "金銭、物資、ボランティアによる「援助、支援金、救援」全般を指します。",
             "bantuan sosial / Bansos（社会保障給付金）, bantuan kemanusiaan（人道支援）, bantuan modal usaha（創業資金支援）",
             "Penyaluran bantuan pangan beras disalurkan merata ke daerah-daerah terpencil.",
             "米の食糧支援の配給は、孤立した辺境地域へと公平に行われた。"),
            ("pembantu", "名詞", "プンバントゥ",
             "かつて「お手伝いさん（家政婦）」を指した言葉ですが、現在はより丁寧な「ART（Asisten Rumah Tangga）」が推奨されます。",
             "pembantu rumah tangga / PRT（家政婦・お手伝いさん）, pembantu rektor（副学長＝現在はWakil Rektor）",
             "Saat ini istilah Asisten Rumah Tangga lebih disukai untuk menghormati profesi pekerja domestik.",
             "現在では家事労働者の職業を尊重するため、ART（家事アシスタント）という呼称が好まれる。"),
            ("terbantu", "動詞", "トゥルバントゥ",
             "他者の支援や便利なツールのおかげで「大いに助かった、負担が軽減された」心理・状態を表します。",
             "sangat terbantu（大変助かる）, merasa terbantu（助かったと感じる）",
             "Kami merasa sangat terbantu oleh bantuan sukarelawan selama proses evakuasi.",
             "私たちは避難プロセスの間、ボランティアたちの支援によって大いに助けられた。")
        ],
        "dialogue": {
            "title": "零細企業（UMKM）向け補助金とデジタル化支援",
            "lines": [
                ("Wati", "Pak Joko, apakah warung kelontong Bapak sudah menerima bantuan modal dari pemerintah?"),
                ("Joko", "Alhamdulillah sudah, Bu. Dana bantuan itu sangat membantu kami menambah stok barang dagangan."),
                ("Wati", "Baguslah. Selain modal, pemerintah daerah juga membuka pelatihan untuk membantu digitalisasi pembayaran."),
                ("Joko", "Wah, saya pasti ikut. Saya ingin belajar memakai QRIS agar pembeli lebih mudah bertransaksi.")
            ]
        },
        "grammar_points": [
            ("Bansos（Bantuan Sosial）の重要性", "インドネシアの時事ニュースで毎日登場する「社会扶助・給付金」の略語。貧困層支援の米や現金の直接給付（BLT）を指す。"),
            ("PRT から ART へのポリティカル・コレクトネス", "「pembantu rumah tangga」という言葉には伝統的な主従関係の響きがあるため、現代の公的文書や都市部では「Asisten Rumah Tangga (ART)」と言い換えるのが社会通念・エチケット。")
        ],
        "quizzes": [
            {
                "q": "インドネシアのニュースで頻出する「社会扶助・困窮層向け給付金（Bantuan Sosial）」の略称はどれか？",
                "options": ["A. Bansos", "B. BUMN", "C. BLT", "D. BPJS"],
                "ans": "A. Bansos",
                "expl": "Bantuan Sosial は一般に「Bansos（バンソス）」と略されます。"
            },
            {
                "q": "現代インドネシアにおいて「お手伝いさん・家政婦」を尊重して呼ぶ際に好まれる表現（ART）の正式名称はどれか？",
                "options": ["A. Asosiasi Rumah Tangga", "B. Asisten Rumah Tangga", "C. Ahli Rancang Taman", "D. Agen Rumah Tangga"],
                "ans": "B. Asisten Rumah Tangga",
                "expl": "家事労働者の尊厳に配慮した標準的表現は「Asisten Rumah Tangga（略称 ART）」です。"
            },
            {
                "q": "「新機能のおかげで、私たちの作業効率は大いに助けられた（向上した）」の空欄に入る動詞は？\nKami merasa sangat [...] dengan kehadiran fitur otomatisasi terbaru ini.",
                "options": ["A. terbantu", "B. membantu", "C. bantuan", "D. pembantu"],
                "ans": "A. terbantu",
                "expl": "助けられた・負担が軽くなった状態を表すため、terbantu が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Berat sama dipikul, ringan sama dijinjing.",
            "meaning": "重いものは共に担ぎ、軽いものは共に手提げで運ぶ＝苦楽を分かち合い、互いに助け合うインドネシアの相互扶助の最高精神。"
        }
    },
    {
        "filename": "140-root-layan.md",
        "title": "1390. 語根 layan の全派生語図鑑（melayani, pelayanan, pelayan, terlayani）",
        "root": "layan",
        "core_meaning": "仕える、給仕する、もてなす、サービスを提供する、応対する",
        "explanation": "語根 layan は、他者の要求や福祉のために「真心をもって応対しサービスを提供する」ホスピタリティと奉仕のコアを持ちます。レストランの給仕（pelayan restoran）から行政の公共サービス（pelayanan publik）、顧客対応（melayani pelanggan）、隅々まで行き届いた医療（terlayani）まで、近代サービス産業と公共倫理の屋台骨となる語根です。",
        "matrix": [
            ("layan", "語根", "動詞", "仕える、応対する（通常接辞付き）", "Jiwa melayani adalah esensi dasar seorang abdi negara."),
            ("melayani", "meN- -i", "他動詞", "仕える、給仕する、サービスを提供する、応対する", "Petugas bank melayani setiap nasabah dengan ramah dan profesional."),
            ("pelayanan", "peN- -an", "名詞", "サービス、接客、給仕、公共サービス", "Peningkatan kualitas pelayanan publik menjadi prioritas utama reformasi birokrasi."),
            ("pelayan", "peN-", "名詞", "ウェイター、給仕人、奉仕者、召使い", "Pelayan restoran membawakan menu istimewa ke meja tamu."),
            ("terlayani", "ter-", "受動・可能動詞", "サービスを受けられる、対応される", "Masyarakat di pulau terpencil kini terlayani oleh kapal puskesmas keliling."),
            ("pelayanan publik", "frasa", "名詞句", "公共サービス、住民行政サービス", "Mal Pelayanan Publik mengintegrasikan puluhan izin dalam satu gedung."),
            ("melayani sepenuh hati", "frasa", "成句・スローガン", "真心を込めておもてなし・奉仕する", "Rumah sakit ini berkomitmen melayani pasien sepenuh hati tanpa diskriminasi.")
        ],
        "details": [
            ("melayani", "他動詞", "ムラヤニ",
             "客、患者、住民の要望に対して「サービスを提供する・応対する・給仕する」動作です。",
             "melayani pembeli（買い手に応対する）, melayani kebutuhan masyarakat（住民のニーズに応える）",
             "Apotek ini buka dua puluh empat jam untuk melayani kebutuhan obat darurat warga.",
             "この薬局は住民の緊急の医薬品ニーズに対応するため24時間営業している。"),
            ("pelayanan", "名詞", "プラヤナン",
             "接客、カスタマーサポート、行政手続きなどの「サービス全般」を指す最重要ビジネス・社会名詞です。",
             "pelayanan konsumen / customer service（顧客対応）, standar pelayanan minimal（最低サービス基準）, pelayanan prima（最高品質のサービス・エクセレントサービス）",
             "Bank swasta itu meraih penghargaan bergengsi berkat standar pelayanan prima kepada nasabahnya.",
             "その民間銀行は、預金者に対する最高水準のエクセレントサービスの提供により名誉ある賞を受賞した。"),
            ("pelayan", "名詞", "プラヤン",
             "飲食店などの「ウェイター、給仕係」、あるいは宗教・社会における「奉仕者」を指します。",
             "pelayan toko（店員・ショップ店員）, pelayan masyarakat（公僕・国民の奉仕者）",
             "Seorang pelayan yang ramah dapat meningkatkan kenyamanan pengunjung restoran.",
             "愛想の良い給仕係は、レストランの客の快適度を向上させることができる。"),
            ("terlayani", "可能動詞", "トゥルラヤニ",
             "すべての住民や顧客が「サービスを漏れなく受けられる・対応が行き届く」状態を表します。",
             "belum terlayani listrik（まだ電気が通っていない・未電化の）, seluruh warga terlayani（全住民に行き届いた）",
             "Pemerintah menargetkan seluruh desa di kawasan perbatasan terlayani akses internet cepat.",
             "政府は国境地帯のすべての村が高速インターネットのサービスを享受できるよう目標を掲げている。")
        ],
        "dialogue": {
            "title": "統合行政窓口（Mal Pelayanan Publik）での住民サービス体験",
            "lines": [
                ("Fitri", "Saya sangat kagum dengan Mal Pelayanan Publik kota kita sekarang."),
                ("Eko", "Iya, betul. Dulu mengurus KTP dan paspor butuh waktu berhari-hari di kantor terpisah."),
                ("Fitri", "Sekarang semua terintegrasi di satu tempat dan petugasnya melayani dengan cepat serta transparan."),
                ("Eko", "Inilah bukti nyata peningkatan kualitas pelayanan publik bagi kemaslahatan warga.")
            ]
        },
        "grammar_points": [
            ("Pelayanan Prima（エクセレントサービス）", "インドネシアの公務員研修や民間サービス業で合言葉となっている概念。迅速、親切、透明、的確なハイレベルサービスを指す。"),
            ("pelayan masyarakat という表現", "公務員（PNS/ASN）の誇りある自称として「abdi negara（国家の僕）」とともに「pelayan masyarakat（国民への奉仕者）」という表現が好まれる。")
        ],
        "quizzes": [
            {
                "q": "自治体が住民票、パスポート、営業許可などの窓口を一元化した統合行政施設の名称はどれか？",
                "options": ["A. Mal Pelayanan Publik", "B. Kantor Pelayan Daerah", "C. Gedung Terlayani Bersama", "D. Balai Layan Warga"],
                "ans": "A. Mal Pelayanan Publik",
                "expl": "窓口を一元化した施設は「Mal Pelayanan Publik（MPP）」と呼ばれます。"
            },
            {
                "q": "「最高品質の顧客サービス、エクセレントサービス」を意味する定型ビジネス用語はどれか？",
                "options": ["A. pelayanan prima", "B. pelayan utama", "C. layanan pertama", "D. terlayani cepat"],
                "ans": "A. pelayanan prima",
                "expl": "最高水準のサービスは「pelayanan prima」と言います。"
            },
            {
                "q": "「離島の住民たちも巡回医療船のサービスを受けられるようになった」の空欄に入る動詞は？\nWarga pulau terpencil kini [...] layanan kesehatan kapal puskesmas keliling.",
                "options": ["A. melayani", "B. terlayani", "C. pelayan", "D. melayankan"],
                "ans": "B. terlayani",
                "expl": "住民たちがサービスを受けられる・行き届いた状態を表すため、terlayani が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Pemimpin yang sejati adalah pelayan bagi kaumnya.",
            "meaning": "真の指導者とは、自らの民・共同体に誠心誠意仕える奉仕者（サーヴァント・リーダー）であるという教え。"
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
