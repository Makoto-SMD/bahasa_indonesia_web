# -*- coding: utf-8 -*-
"""
セクション33 第5バッチ (1391-1400) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾（セクション完結編）
"""

import os

articles = [
    {
        "filename": "141-root-urus.md",
        "title": "1391. 語根 urus の全派生語図鑑（mengurus, pengurusan, pengurus, urusan）",
        "root": "urus",
        "core_meaning": "処理する、世話をする、片付ける、用事、手続き、役員",
        "explanation": "語根 urus は、散らかった物事や雑多なタスクを「順序立てて整頓・処理する、面倒を見る」コアを持ちます。日常の用事・ビジネス（urusan）から行政手続き（pengurusan visa）、組織の幹部・役員（pengurus）、他人の干渉（ikut campur urusan）まで、日常・実務に不可欠な基幹語根です。",
        "matrix": [
            ("urus", "語根", "動詞・命令", "処理せよ、片付けろ（通常接辞付き）", "Urus dulu dokumen ini sebelum jam kantor berakhir."),
            ("mengurus", "meN-", "他動詞", "処理する、手続きする、世話をする、管理する", "Dia sedang mengurus perpanjangan izin tinggal di kantor imigrasi."),
            ("pengurusan", "peN- -an", "名詞", "手続き、処理プロセス、管理業務", "Proses pengurusan paspor kini jauh lebih cepat lewat aplikasi daring."),
            ("pengurus", "peN-", "名詞", "役員、幹部、管理者、世話人", "Rapat pengurus yayasan membahas program beasiswa tahun ajaran baru."),
            ("urusan", "-an", "名詞", "用事、用件、問題、管轄事項、関心事", "Saya datang ke Jakarta untuk menyelesaikan beberapa urusan bisnis."),
            ("terurus", "ter-", "受動・可能動詞", "きちんと手入れされている、管理が行き届いた", "Taman kota itu tampak asri dan terurus dengan sangat baik."),
            ("bukan urusan", "frasa", "慣用語・成句", "関係ない、余計なお世話", "Masalah pribadi orang lain bukan urusan kita untuk mencampurinya.")
        ],
        "details": [
            ("mengurus", "他動詞", "ムングルス",
             "行政手続きを行う、病人の世話をする、組織を経営する万能動詞です。",
             "mengurus anak（子どもの世話をする）, mengurus izin usaha（営業許可の手続きをする）, mengurus jenazah（葬儀を執り行う）",
             "Sebagai orang tua tunggal, ia bekerja keras mencari nafkah sekaligus mengurus kedua anaknya.",
             "ひとり親として、彼女は生計を立てるために懸命に働きながら、同時に2人の子どもの面倒を見ている。"),
            ("pengurusan", "名詞", "プングルサン",
             "ビザ、免許証、登記などの「公的手続き・申請・処理作業」を指します。",
             "biaya pengurusan（手続き費用）, pengurusan sertifikat tanah（土地権利証の手続き）",
             "Pemerintah memangkas birokrasi berbelit demi mempermudah pengurusan izin investasi.",
             "政府は投資許可手続きを簡素化するため、煩雑な官僚機構（たらい回し）を削減した。"),
            ("pengurus", "名詞", "プングルス",
             "組合、財団、アパート管理組合などの「役員・理事・執行部」を指します。",
             "pengurus harian（常任理事）, dewan pengurus（理事会）, pengurus RT（住民組織役員）",
             "Pemilihan ketua dan pengurus koperasi baru akan diselenggarakan akhir pekan ini.",
             "新しい協同組合の組合長および役員の選挙が今週末に開催される。"),
            ("urusan", "名詞", "ウルサン",
             "日々の「用事、関心事、管轄、案件」を指す最頻出名詞です。",
             "urusan pribadi（私事）, urusan luar negeri（外交・外務）, urusan administrasi（事務手続き）",
             "Kementerian Luar Negeri bertanggung jawab atas segala urusan diplomasi internasional.",
             "外務省はあらゆる国際外交案件に対する責任を担っている。")
        ],
        "dialogue": {
            "title": "役所での各種証明書手続きに関する相談",
            "lines": [
                ("Bayu", "Apakah kamu sudah selesai mengurus surat keterangan domisili di kelurahan?"),
                ("Lestari", "Sudah, Mas. Sekarang sistem pengurusan surat sudah terdigitalisasi sehingga sangat praktis."),
                ("Bayu", "Baguslah. Ada urusan lain yang perlu kita selesaikan sebelum kantor tutup?"),
                ("Lestari", "Tinggal urusan legalisasi dokumen di kantor notaris saja, setelah itu semuanya beres.")
            ]
        },
        "grammar_points": [
            ("urus と kurus の音韻的差異", "urus（処理する・用事）と kurus（痩せている）は全く無関係の語根。発音と綴りの混同に注意。"),
            ("tak terurus の慣用表現", "接頭辞 ter- の否定形「tak terurus」は「放置されて荒れ放題の、手入れされていない（neglected）」状態を表す頻出フレーズ。")
        ],
        "quizzes": [
            {
                "q": "「ビザの更新手続きを行う」をインドネシア語で表現したものはどれか？",
                "options": ["A. mengurus perpanjangan visa", "B. pengurus visa panjang", "C. urusan perpanjangan visa", "D. terurus visa baru"],
                "ans": "A. mengurus perpanjangan visa",
                "expl": "手続きを能動的に行う動作なので、他動詞 mengurus を用いて「mengurus perpanjangan visa」と言います。"
            },
            {
                "q": "「それは私の知ったことではない（私には関係ない用事だ）」を意味する成句はどれか？",
                "options": ["A. Itu bukan urusan saya", "B. Itu tak terurus saya", "C. Itu pengurus saya", "D. Itu urus sendiri"],
                "ans": "A. Itu bukan urusan saya",
                "expl": "「Itu bukan urusan saya」は「私の管轄・関心事ではない＝余計なお世話だ」を表す定番フレーズです。"
            },
            {
                "q": "財団や組合の「役員・幹部」を指す名詞はどれか？",
                "options": ["A. urusan", "B. pengurusan", "C. pengurus", "D. terurus"],
                "ans": "C. pengurus",
                "expl": "組織の管理・運営を担う役員は「pengurus」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Lain ladang lain belalang, lain lubuk lain ikannya.",
            "meaning": "畑が違えばバッタも違い、淵が違えば魚も違う＝地域や組織が異なれば、それぞれの風習や事務処理のルール（urusan）も異なる。"
        }
    },
    {
        "filename": "142-root-kelola.md",
        "title": "1392. 語根 kelola の全派生語図鑑（mengelola, pengelolaan, pengelola, terkelola）",
        "root": "kelola",
        "core_meaning": "管理する、運営する、マネジメントする、統括する",
        "explanation": "語根 kelola は、企業、資産、天然資源、データなどの複雑な対象を「専門的・戦略的にマネジメント（管理・運営）する」高次の統御コアを持ちます。企業経営（mengelola bisnis）から廃棄物処理管理（pengelolaan sampah）、ファンドマネージャー・管理者（pengelola）、適切に統御された状態（terkelola）まで、現代マネジメントの最重要語根です。",
        "matrix": [
            ("kelola", "語根", "動詞・概念", "管理する、運営する（接辞付きが基本）", "Kelola keuangan pribadi dengan bijak sejak usia muda."),
            ("mengelola", "meN-", "他動詞", "管理する、運営する、マネジメントする、経営する", "Manajer berpengalaman itu dipercaya mengelola cabang baru perusahaan."),
            ("pengelolaan", "peN- -an", "名詞", "管理、運営、マネジメント、処理プロセス", "Tata kelola perusahaan yang baik (GCG) mencegah penyalahgunaan wewenang."),
            ("pengelola", "peN-", "名詞", "管理者、運営者、経営母体、運用担当者", "Pemerintah bekerja sama dengan pihak swasta sebagai pengelola jalan tol."),
            ("terkelola", "ter-", "受動・可能動詞", "管理されている、うまく統御された", "Limbah industri harus terkelola secara aman agar tidak mencemari sungai."),
            ("tata kelola", "frasa", "名詞句", "ガバナンス、統治体制", "Penerapan tata kelola yang transparan dan akuntabel sangat penting bagi BUMN.")
        ],
        "details": [
            ("mengelola", "他動詞", "ムンクロラ",
             "資金、プロジェクト、農地、天然資源を「体系的に経営・運営・管理する」プロフェッショナルな動詞です。",
             "mengelola stres（ストレスをコントロールする）, mengelola keuangan（家計・財務を管理する）, mengelola waktu（時間管理する）",
             "Kemampuan mengelola waktu dan prioritas kerja merupakan kunci sukses para profesional.",
             "時間と業務の優先順位を管理する能力は、プロフェッショナルたちの成功の鍵である。"),
            ("pengelolaan", "名詞", "プンクロラアン",
             "資源や廃棄物、資産の「運用・管理手法・ガバナンス」を指す公的・ビジネス基本名詞です。",
             "pengelolaan sampah（ゴミ処理・廃棄物管理）, pengelolaan sumber daya alam（天然資源管理）",
             "Pemerintah daerah memperketat regulasi pengelolaan limbah bagi kawasan industri.",
             "地方政府は工業団地に対する廃棄物管理の規制を強化した。"),
            ("pengelola", "名詞", "プンクロラ",
             "施設やファンド、Webサイトの「運営母体・管理人・ディレクター」を指します。",
             "badan pengelola（管理機構）, manajer investasi pengelola dana（資産運用マネージャー）",
             "Badan Pengelola Keuangan Haji bertugas menginvestasikan dana jamaah secara syariah.",
             "巡礼基金管理機構は、巡礼者の基金をイスラム法（シャリア）に則って運用する責務を負っている。"),
            ("tata kelola", "名詞句", "タタ・クロラ",
             "「ガバナンス（統治構造）」を表す定型名詞句で、企業の健全経営に必須の概念です。",
             "Good Corporate Governance / GCG（優良企業統治）, tata kelola pemerintahan（行政ガバナンス）",
             "Penerapan prinsip tata kelola yang baik mendorong kepercayaan investor global.",
             "良好なガバナンス原則の適用が、グローバル投資家の信頼を後押ししている。")
        ],
        "dialogue": {
            "title": "企業の廃棄物管理とESG投資に関する役員会議",
            "lines": [
                ("Irfan", "Bagaimana sistem pengelolaan limbah di pabrik baru kita, Bu Dewi?"),
                ("Dewi", "Semua limbah cair sudah terkelola melalui instalasi pengolahan modern sebelum dialirkan ke luar."),
                ("Irfan", "Sangat bagus. Pengelola kawasan industri juga menuntut standar ramah lingkungan yang ketat."),
                ("Dewi", "Betul, Pak. Tata kelola lingkungan yang baik adalah komitmen utama kita terhadap prinsip ESG.")
            ]
        },
        "grammar_points": [
            ("urus vs kelola の使い分け", "urus（mengurus）は日常的な「雑務の処理、世話、行政手続き」。kelola（mengelola）は「戦略的マネジメント、企業経営、資源運用、ガバナンス」という組織的・高度な次元で用いられる。"),
            ("tata kelola（ガバナンス）", "tata（秩序・配列）+ kelola（管理）からなる合成名詞で、英語の governance の定訳。新聞の経済面・政治面で最頻出。")
        ],
        "quizzes": [
            {
                "q": "「コーポレート・ガバナンス（企業統治）」を意味するインドネシア語の標準的表現はどれか？",
                "options": ["A. tata urus perusahaan", "B. tata kelola perusahaan", "C. pengurus korporasi", "D. aturan kelola modal"],
                "ans": "B. tata kelola perusahaan",
                "expl": "ガバナンスは「tata kelola」と訳されるため、企業統治は「tata kelola perusahaan（Good Corporate Governance）」と言います。"
            },
            {
                "q": "「廃棄物・ゴミ管理」を意味する公的用語はどれか？",
                "options": ["A. pengelolaan sampah", "B. pengurusan sampah", "C. kelola kotoran", "D. buangan urus"],
                "ans": "A. pengelolaan sampah",
                "expl": "廃棄物の処理・運用管理は「pengelolaan sampah / limbah」と表現します。"
            },
            {
                "q": "「高速道路の運営事業者」を表す名詞はどれか？",
                "options": ["A. pengurus jalan tol", "B. pengelola jalan tol", "C. pekelola jalan", "D. penata tol"],
                "ans": "B. pengelola jalan tol",
                "expl": "商業インフラや施設の運営者は「pengelola」を用います。"
            }
        ],
        "peribahasa": {
            "quote": "Hemat pangkal kaya, rajin pangkal pandai, tertib pangkal damai.",
            "meaning": "倹約は富の基、勤勉は知恵の基、規律（適切な管理統制）は平和の基である。"
        }
    },
    {
        "filename": "143-root-pimpin.md",
        "title": "1393. 語根 pimpin の全派生語図鑑（memimpin, pimpinan, kepemimpinan, pemimpin）",
        "root": "pimpin",
        "core_meaning": "率いる、指導する、指揮する、手を引いて案内する、リーダーシップ",
        "explanation": "語根 pimpin は、手を引いて目的地へ案内する動作から、集団や組織、国家の先頭に立って「指揮・統率する」リーダーシップのコアを持ちます。大統領や指導者（pemimpin）、会議の司会進行・統率（memimpin rapat）、リーダーシップの資質（kepemimpinan）、上層部・首脳陣（pimpinan）まで、指導者層の語彙を支配する語根です。",
        "matrix": [
            ("pimpin", "語根", "動詞・命令", "率いよ、導け（通常接辞付き）", "Pimpin dengan keteladanan, bukan dengan ancaman kekuasaan."),
            ("memimpin", "meN-", "他動詞", "率いる、指導する、指揮する、司会進行する、首位に立つ", "Kapten tim memimpin rekan-rekannya dengan penuh semangat juang."),
            ("pemimpin", "peN-", "名詞", "指導者、リーダー、首領、トップ", "Seorang pemimpin visioner mampu membaca arah perubahan zaman."),
            ("pimpinan", "-an", "名詞", "首脳陣、上層部、経営幹部、指導体制", "Keputusan strategis itu disepakati dalam rapat pimpinan tingkat tinggi."),
            ("kepemimpinan", "ke- -an", "名詞", "リーダーシップ、統率力、指導者精神・任期", "Gaya kepemimpinan transformasional sangat cocok di era keterbukaan."),
            ("terpimpin", "ter-", "受動・状態動詞", "指導された、誘導された（Demokrasi Terpimpin等）", "Demokrasi Terpimpin pernah diterapkan di Indonesia pada era Presiden Sukarno.")
        ],
        "details": [
            ("memimpin", "他動詞", "ムミンピン",
             "国家、軍隊、プロジェクト、会議を「率いる・統率する」、またはレースで「首位を走る」動作です。",
             "memimpin rapat（会議を司会進行する）, memimpin doa（お祈りを先導する）, memimpin klasemen（順位表の首位に立つ）",
             "Presiden memimpin upacara peringatan Hari Kemerdekaan di Istana Merdeka.",
             "大統領はムルデカ宮殿において独立記念日の式典を主宰（先導）した。"),
            ("pemimpin", "名詞", "プミンピン",
             "組織や国家、チームの「指導者・リーダー個人」を指します。",
             "pemimpin redaksi（編集長）, pemimpin daerah（地方首長）, pemimpin spiritual（宗教的指導者）",
             "Integritas moral adalah syarat mutlak yang harus dimiliki oleh setiap calon pemimpin bangsa.",
             "道徳的誠実さは、すべての国家指導者候補が備えていなければならない絶対条件である。"),
            ("pimpinan", "名詞", "ピンピナン",
             "組織の「上層部、首脳陣、幹部会」、あるいは指導・統率そのものを指します。",
             "rapat pimpinan / Rapim（幹部会・首脳会議）, unsur pimpinan（指導層）",
             "Pimpinan perusahaan memberikan apresiasi tinggi kepada karyawan berprestasi luar biasa.",
             "会社首脳陣は、極めて顕著な功績を挙げた従業員に対して高い評価を贈った。"),
            ("kepemimpinan", "名詞", "クピンピナン",
             "人を動かし組織を牽引する「リーダーシップ、統率力、指導方針」を指す抽象名詞です。",
             "jiwa kepemimpinan（リーダーシップ精神）, tongkat kepemimpinan（指導者のバトン）",
             "Pelatihan bela negara ini diadakan untuk mengasah karakter dan kapasitas kepemimpinan pemuda.",
             "この愛国国防研修は、青年の人格とリーダーシップ能力を磨くために開催された。")
        ],
        "dialogue": {
            "title": "新プロジェクトのリーダーシップと組織運営方針",
            "lines": [
                ("Galih", "Selamat atas terpilihnya kamu untuk memimpin proyek transformasi digital kantor kita, Dina."),
                ("Dina", "Terima kasih, Mas. Ini amanah besar dari jajaran pimpinan yang harus saya jalankan sungguh-sungguh."),
                ("Galih", "Saya yakin dengan gaya kepemimpinanmu yang kolaboratif, tim akan bekerja sangat solid."),
                ("Dina", "Mohon dukungan dan masukannya selalu. Pemimpin yang baik harus mau mendengar suara timnya.")
            ]
        },
        "grammar_points": [
            ("pemimpin vs pimpinan の厳密な識別", "pemimpin はリーダーという「人（指導者個人）」を表す（agent noun）。pimpinan は「首脳陣、経営層、リーダーシップ体制」という集合的組織・概念を表す。試験・ビジネスの最重要識別点。"),
            ("Demokrasi Terpimpin（指導民主主義）", "1959年〜1965年のスカルノ大統領時代に導入されたインドネシア現代史の重要政治体制名。接頭辞 ter- を用いた代表的歴史用語。")
        ],
        "quizzes": [
            {
                "q": "新聞社や雑誌社の「編集長」を表すインドネシア語はどれか？",
                "options": ["A. pemimpin redaksi", "B. pimpinan koran", "C. ketua berita", "D. kepala jurnal"],
                "ans": "A. pemimpin redaksi",
                "expl": "編集長は「pemimpin redaksi（略称 Pemred）」と言います。"
            },
            {
                "q": "組織の「首脳陣、経営幹部会」を表す名詞はどれか？",
                "options": ["A. pemimpin", "B. pimpinan", "C. kepemimpinan", "D. memimpin"],
                "ans": "B. pimpinan",
                "expl": "上層部・首脳陣の集合体は「pimpinan」を用います。"
            },
            {
                "q": "スカルノ大統領時代の「指導民主主義」を表す歴史用語はどれか？",
                "options": ["A. Demokrasi Pemimpin", "B. Demokrasi Pimpinan", "C. Demokrasi Terpimpin", "D. Demokrasi Memimpin"],
                "ans": "C. Demokrasi Terpimpin",
                "expl": "指導民主主義は「Demokrasi Terpimpin」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Ing ngarsa sung tuladha, ing madya mangun karsa, tut wuri handayani.",
            "meaning": "前に立っては模範を示し、中にあっては志を鼓舞し、後ろにあっては後押しをする＝インドネシア教育の父キ・ハジャル・デワンタラが説いた理想のリーダーシップ論。"
        }
    },
    {
        "filename": "144-root-arah.md",
        "title": "1394. 語根 arah の全派生語図鑑（mengarahkan, pengarahan, arahan, terarah）",
        "root": "arah",
        "core_meaning": "方向、方角、志向、指針、指示・指示を与える",
        "explanation": "語根 arah は、方位磁針が指す物理的な「方角」から、政策や人生の「方向性・志向」、指導者が下す「指針・訓示（arahan）」、焦点を合わせる使役（mengarahkan）、目標に向かって計画された状態（terarah）まで、ベクトルと指針を司る基本語根です。",
        "matrix": [
            ("arah", "語根", "名詞", "方向、方角、目標、趣向", "Angin berhembus kencang ke arah timur laut."),
            ("searah", "se-", "前置詞・形容詞", "同じ方向の、一方通行の、一致した", "Jalan ini diberlakukan sistem satu arah selama jam sibuk pagi."),
            ("mengarahkan", "meN- -kan", "他動詞", "向ける、指導する、誘導する、焦点を当てる", "Dosen pembimbing mengarahkan mahasiswa memilih topik riset yang orisinal."),
            ("pengarahan", "peN- -an", "名詞", "ブリーフィング、オリエンテーション、訓示、指示説明", "Panglima memberikan pengarahan taktis kepada para prajurit sebelum bertugas."),
            ("arahan", "-an", "名詞", "指針、指示、助言、指導ガイドライン", "Kami bekerja sesuai arahan dan instruksi langsung dari direktur utama."),
            ("terarah", "ter-", "受動・状態動詞", "方向付けられた、目標が定まった、秩序ある", "Program pelatihan ini membantu generasi muda memiliki rencana karier yang terarah.")
        ],
        "details": [
            ("arah", "名詞", "アラハ",
             "空間的な方角、政策の向かう先、人生の針路を表す基本名詞です。",
             "arah jarum jam（時計回り）, arah kebijakan（政策方針・ガイドライン）, kehilangan arah（方向性を見失う）",
             "Pemerintah menetapkan arah kebijakan hilirisasi industri untuk meningkatkan nilai tambah komoditas.",
             "政府はコモディティの付加価値を高めるため、産業川下化の政策方針を定めた。"),
            ("mengarahkan", "他動詞", "ムンアラハカン",
             "視線や武器、関心を「向ける」、あるいは人を正しい方向へ「誘導・指導する」動作です。",
             "mengarahkan kamera（カメラを向ける）, mengarahkan pandangan（視線を注ぐ）, mengarahkan siswa（生徒を導く）",
             "Pelatih mengarahkan fokus pemain pada strategi bertahan di babak kedua pertandingan.",
             "監督は試合の後半、守備戦術に選手の集中を向けさせた。"),
            ("arahan", "名詞", "アラハン",
             "上司、首長、指導者が部下に与える「指示、指針、アドバイス」を指す公的実務用語です。",
             "mendapat arahan（指示を受ける）, memberi arahan（指針を授ける）, menindaklanjuti arahan（指示をフォローアップ・実行する）",
             "Seluruh staf dinas wajib menindaklanjuti arahan gubernur terkait penanganan banjir.",
             "すべての局員は、洪水対策に関する知事の指示をフォローアップし実行しなければならない。"),
            ("pengarahan", "名詞", "プンアラハン",
             "任務の前に全員を集めて行う「事前オリエンテーション、説明会、ブリーフィング」です。",
             "sesi pengarahan（説明会セッション）, pengarahan teknis / briefing teknis（技術的ブリーフィング）",
             "Ketua panitia memberikan pengarahan singkat kepada seluruh relawan sebelum acara dimulai.",
             "実行委員長はイベント開始前に、すべてのボランティアに対して簡潔な事前説明を行った。")
        ],
        "dialogue": {
            "title": "新規プロジェクト開始前のキックオフと指針説明",
            "lines": [
                ("Satria", "Apakah semua anggota tim sudah berkumpul di ruang rapat untuk sesi pengarahan?"),
                ("Novi", "Sudah lengkap, Mas. Kita menunggu arahan dari Bapak Direktur mengenai target kuartal ini."),
                ("Satria", "Bagus. Arahan beliau sangat penting agar langkah kerja kita terarah dan efisien."),
                ("Novi", "Betul. Dengan panduan yang jelas, kita bisa mengarahkan seluruh sumber daya tepat sasaran.")
            ]
        },
        "grammar_points": [
            ("arahan vs instruksi", "instruksi は命令的・強制的な「指図・指令（order）」。arahan は大所高所からの「指導方針・指針・助言（guidance/directive）」というニュアンスを持ち、ビジネスや公務で好まれる。"),
            ("searah jarum jam", "時計回りは「searah jarum jam（時計の針と同じ方向）」、反時計回りは「berlawanan arah jarum jam（時計の針と逆方向）」。")
        ],
        "quizzes": [
            {
                "q": "上司や指導者が示す「指導方針・指針・助言」を表す最も標準的な実務用語はどれか？",
                "options": ["A. arahan", "B. searah", "C. terarah", "D. penyearah"],
                "ans": "A. arahan",
                "expl": "上司からの指針・ガイダンスは「arahan」と言います。"
            },
            {
                "q": "「時計回り」をインドネシア語で正しく表現したものはどれか？",
                "options": ["A. searah jarum jam", "B. berarah jam", "C. pengarahan jam", "D. terarah jam"],
                "ans": "A. searah jarum jam",
                "expl": "時計回りは「searah jarum jam」と言います。"
            },
            {
                "q": "任務やプロジェクトの開始前に行われる「事前説明・ブリーフィング」を表す名詞はどれか？",
                "options": ["A. pengarahan", "B. arahan", "C. searah", "D. berarah"],
                "ans": "A. pengarahan",
                "expl": "説明会・オリエンテーションの手続き・セッションは「pengarahan」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Malu bertanya sesat di jalan, enggan berdayung hanyut serantau.",
            "meaning": "尋ねるのを恥ずかしがれば道に迷い、漕ぐのを怠れば遠く流される＝分からないときは素直に教えや指針（arahan）を請うべきである。"
        }
    },
    {
        "filename": "145-root-bimbing.md",
        "title": "1395. 語根 bimbing の全派生語図鑑（membimbing, bimbingan, pembimbing, terbimbing）",
        "root": "bimbing",
        "core_meaning": "導く、手を引く、指導する、助言する、メンタリングする",
        "explanation": "語根 bimbing は、迷ったり未熟な者の手を優しく取って「正しい道へと寄り添い導く」メンターシップのコアを持ちます。卒論指導教員（dosen pembimbing）からカウンセリング・進路指導（bimbingan konseling / BK）、親による徳育（membimbing anak）、導かれた状態（terbimbing）まで、教育と人間的成長の根幹を支える語根です。",
        "matrix": [
            ("bimbing", "語根", "動詞・命令", "導け、手を引け（通常接辞付き）", "Bimbinglah langkah generasi penerus menuju masa depan yang gemilang."),
            ("membimbing", "meN-", "他動詞", "導く、指導する、手引きする、カウンセリングする", "Guru dengan penuh kesabaran membimbing murid yang mengalami kesulitan belajar."),
            ("bimbingan", "-an", "名詞", "指導、助言、メンタリング、カウンセリング、学習塾", "Mahasiswa akhir wajib mengikuti bimbingan skripsi secara intensif."),
            ("pembimbing", "peN-", "名詞", "指導教員、メンター、ガイド、指導役", "Dosen pembimbing memberikan catatan kritis untuk menyempurnakan tesisnya."),
            ("terbimbing", "ter-", "受動・可能動詞", "指導を受ける、導かれた、チュートリアル形式の", "Siswa melakukan eksperimen sains melalui metode diskusi terbimbing."),
            ("bimbingan belajar", "frasa", "名詞句・略語Bimbel", "学習塾、補習スクール", "Banyak pelajar mendaftar bimbingan belajar untuk persiapan ujian masuk PTN.")
        ],
        "details": [
            ("membimbing", "他動詞", "ムンビンビン",
             "知識や精神の未熟な者を「丁寧に指導する・メンターとして導く」温かい動詞です。",
             "membimbing rohani（魂・信仰を導く）, membimbing skripsi（卒論を指導する）, membimbing langkah awal（最初の一歩を導く）",
             "Para mentor bisnis siap membimbing pelaku UMKM dalam memperluas pasar ekspor.",
             "ビジネスメンターたちが、零細起業家が輸出市場を拡大できるよう指導する準備を整えている。"),
            ("bimbingan", "名詞", "ビンビンガン",
             "学校や職場での「個別指導、カウンセリング、アドバイス」を指します。",
             "bimbingan konseling / BK（進路・生活相談窓口）, di bawah bimbingan（〜の指導のもとで）",
             "Di bawah bimbingan profesor ahli bioteknologi, penelitian itu berhasil meraih paten internasional.",
             "バイオテクノロジーの専門教授の指導のもと、その研究は国際特許の取得に成功した。"),
            ("pembimbing", "名詞", "プンビンビン",
             "大学の「指導教員」、精神的「メンター」、あるいは巡礼の「案内役」を指します。",
             "dosen pembimbing utama（主指導教員）, pembimbing ibadah haji（ハッジ巡礼指導員）",
             "Mahasiswa harus berkonsultasi secara rutin dengan dosen pembimbing agar lulus tepat waktu.",
             "学生は予定通りに卒業できるよう、指導教員と定期的に面談・相談しなければならない。"),
            ("bimbingan belajar", "名詞句", "ビンビンガン・ブラジャール",
             "インドネシア全国に普及している「民間学習塾（通称 Bimbel）」を指す教育用語です。",
             "lembaga bimbel（学習塾機関）, kelas intensif bimbel（塾の特訓クラス）",
             "Menjelang ujian seleksi nasional masuk perguruan tinggi, lembaga bimbingan belajar dipadati siswa.",
             "国立大学入学選抜試験を控え、民間学習塾は多くの生徒たちで混雑している。")
        ],
        "dialogue": {
            "title": "大学での卒業論文指導と進捗相談",
            "lines": [
                ("Rangga", "Bagaimana jadwal bimbingan skripsimu dengan Dosen Pembimbing minggu ini, Citra?"),
                ("Citra", "Alhamdulillah, beliau sudah membaca draf bab empat dan meminta saya datang besok pagi."),
                ("Rangga", "Bagus sekali. Beliau memang sangat teliti dan sabar dalam membimbing metode penelitian."),
                ("Citra", "Iya, saya sangat bersyukur. Berkat bimbingan beliau, analisis data saya menjadi jauh lebih tajam.")
            ]
        },
        "grammar_points": [
            ("Bimbel（Bimbingan Belajar）という国民的略語", "日本の「学習塾・予備校」に相当し、インドネシアの受験生（高校3年生など）のほぼ全員が通う施設。"),
            ("pembimbing vs pendidik", "pendidik は教師・教育者全般（educator）。pembimbing は論文指導や生活相談など、特定の個人に寄り添って導く「メンター・指導教官（advisor/mentor）」。")
        ],
        "quizzes": [
            {
                "q": "大学の卒業論文を指導する「指導教官」をインドネシア語で何と呼ぶか？",
                "options": ["A. Dosen Pembimbing", "B. Dosen Pendidik", "C. Dosen Pengarah", "D. Dosen Pemimpin"],
                "ans": "A. Dosen Pembimbing",
                "expl": "大学の指導教員は「Dosen Pembimbing（略称 Dosbing）」と呼ばれます。"
            },
            {
                "q": "インドネシアで民間学習塾を指す通称（略語）はどれか？",
                "options": ["A. Bimbel", "B. Bansos", "C. BUMN", "D. Pemred"],
                "ans": "A. Bimbel",
                "expl": "Bimbingan Belajar の略称は「Bimbel（ビンベル）」です。"
            },
            {
                "q": "学校の「生活指導・カウンセリング室」を表す略語（BK）の正式名称はどれか？",
                "options": ["A. Bimbingan Konseling", "B. Bantuan Komunal", "C. Balai Kesehatan", "D. Badan Kepegawaian"],
                "ans": "A. Bimbingan Konseling",
                "expl": "スクールカウンセリング・進路指導窓口は「Bimbingan Konseling（BK）」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Guru kencing berdiri, murid kencing berlari.",
            "meaning": "教師が立ち小便をすれば、生徒は走りながら小便をする＝指導者の悪癖や不手際は、生徒たちに倍加して悪影響を与えるので、指導的立場にある者は常に身を律しなければならない。"
        }
    },
    {
        "filename": "146-root-didik.md",
        "title": "1396. 語根 didik の全派生語図鑑（mendidik, pendidikan, pendidik, terdidik）",
        "root": "didik",
        "core_meaning": "教え育てる、教育する、薫陶を与える、教養を授ける",
        "explanation": "語根 didik は、知識の伝達のみならず道徳、人格、生活規範を「包括的に教え育てる（教育する）」国家・文明の最重要語根です。学校教育・国家教育制度（pendidikan nasional）から教師・教育者（pendidik）、高学歴層・インテリ（kaum terdidik）、家庭教育（mendidik anak）まで、人間の人格形成を司ります。",
        "matrix": [
            ("didik", "語根", "動詞・命令", "教育せよ、育てよ（通常接辞付き）", "Didiklah anak dengan teladan cinta kasih dan kejujuran."),
            ("mendidik", "meN-", "他動詞", "教育する、教え育てる、薫陶する、啓発する", "Tugas orang tua dan guru adalah mendidik generasi yang berakhlak mulia."),
            ("pendidikan", "peN- -an", "名詞", "教育、教育制度、学歴、養成課程", "Pendidikan karakter memegang peranan krusial dalam kurikulum merdeka."),
            ("pendidik", "peN-", "名詞", "教育者、教師、指導員、教職者", "Pemerintah berupaya meningkatkan kesejahteraan para tenaga pendidik di daerah terpencil."),
            ("terdidik", "ter-", "形容詞・状態動詞", "教育を受けた、教養のある、インテリの", "Masyarakat terdidik diharapkan menjadi pelopor perubahan sosial yang positif."),
            ("peserta didik", "frasa", "名詞句", "児童・生徒・受講生（公的教育用語）", "Setiap peserta didik memiliki potensi unik yang perlu dikembangkan."),
            ("pendidikan tinggi", "frasa", "名詞句", "高等教育（大学・大学院）", "Akses terhadap pendidikan tinggi semakin terbuka melalui berbagai program beasiswa.")
        ],
        "details": [
            ("mendidik", "他動詞", "ムンディディック",
             "単なる技術訓練を超えて、知性と倫理観を備えた人間として「育てる」包括的動詞です。",
             "mendidik anak usia dini（幼児を教育する）, mendidik kedisiplinan（規律を教え込む）",
             "Sekolah tidak hanya mengajar ilmu pengetahuan, tetapi juga mendidik budi pekerti luhur.",
             "学校は知識を教授するだけでなく、高潔な人格と徳育を教え育てる場でもある。"),
            ("pendidikan", "名詞", "プンディディカン",
             "国家の「教育制度、学校、学位・学歴」を指す最重要社会用語です。",
             "Hari Pendidikan Nasional / Hardiknas（国民教育の日・5月2日）, sistem pendidikan nasional（国家教育システム）",
             "Anggaran pendidikan nasional dialokasikan minimal dua puluh persen dari APBN.",
             "国家教育予算は国家財政支出（APBN）の最低20パーセントが配分されている。"),
            ("pendidik", "名詞", "プンディディック",
             "教員、大学教授、インストラクターなど「教育に携わる専門職」の総称です。",
             "tenaga pendidik dan kependidikan（教員および教育事務職員）, sosok pendidik sejati（真の教育者の姿）",
             "Dedikasi para pendidik di pulau terluar patut mendapat penghargaan setinggi-tingginya.",
             "国境の離島で尽力する教育者たちの献身は、最高峰の敬意と表彰に値する。"),
            ("terdidik", "形容詞", "トゥルディディック",
             "十分な教育を受けて「教養がある、知的な（educated）」人物・階層を指します。",
             "kaum terdidik（知識階層・インテリ）, pengangguran terdidik（大卒・高学歴失業者）",
             "Masalah pengangguran terdidik menjadi tantangan serius bagi penyerapan tenaga kerja saat ini.",
             "高学歴失業者の問題は、現代の雇用吸収における深刻な課題となっている。")
        ],
        "dialogue": {
            "title": "「国民教育の日」と未来を担う人材育成に関する対話",
            "lines": [
                ("Budi", "Selamat Hari Pendidikan Nasional! Semangat Ki Hadjar Dewantara harus selalu kita hidupkan."),
                ("Siti", "Betul sekali. Mendidik generasi muda bukan hanya tugas guru di kelas, melainkan tanggung jawab seluruh masyarakat."),
                ("Budi", "Tantangan kita ke depan adalah mencetak lulusan terdidik yang memiliki kecakapan digital sekaligus etika kuat."),
                ("Siti", "Setuju. Sistem pendidikan kita harus terus beradaptasi dengan perubahan zaman tanpa meninggalkan nilai luhur bangsa.")
            ]
        },
        "grammar_points": [
            ("peserta didik（児童生徒）という公的用語", "インドネシアの教育法令や公的文書では、murid（児童生徒）や siswa（生徒）の包括的公用語として「peserta didik（教育参加者＝学習者）」が標準使用される。"),
            ("Hardiknas（Hari Pendidikan Nasional）", "毎年5月2日はインドネシア教育の父キ・ハジャル・デワンタラの生誕を記念する「国民教育の日」。祝典や記念行事が行われる。")
        ],
        "quizzes": [
            {
                "q": "インドネシアで毎年5月2日に祝われる教育記念日の名称はどれか？",
                "options": ["A. Hari Pahlawan Nasional", "B. Hari Pendidikan Nasional", "C. Hari Guru Sedunia", "D. Hari Kebangkitan Belajar"],
                "ans": "B. Hari Pendidikan Nasional",
                "expl": "5月2日は「Hari Pendidikan Nasional（Hardiknas）」です。"
            },
            {
                "q": "「大卒者などの高学歴失業」を表す社会問題用語はどれか？",
                "options": ["A. pengangguran terdidik", "B. pendidik miskin", "C. kemunduran pendidikan", "D. peserta didik nganggur"],
                "ans": "A. pengangguran terdidik",
                "expl": "学歴があるにもかかわらず就職難にある人々は「pengangguran terdidik（高学歴失業）」と呼ばれます。"
            },
            {
                "q": "現代インドネシアの教育法規において児童・生徒・学習者を指す公的用語はどれか？",
                "options": ["A. peserta didik", "B. anak didik", "C. kaum terdidik", "D. pendidik muda"],
                "ans": "A. peserta didik",
                "expl": "法令上の学習者の公式呼称は「peserta didik」です。"
            }
        ],
        "peribahasa": {
            "quote": "Bila anak tidak diajar di rumah, dunia akan mengajarnya dengan cara yang keras.",
            "meaning": "子どもを家庭でしっかり教え育てなければ、世間が過酷な方法でその子に思い知らせることになる＝家庭教育（徳育）の重要性。"
        }
    },
    {
        "filename": "147-root-latih.md",
        "title": "1397. 語根 latih の全派生語図鑑（melatih, pelatihan, pelatih, terlatih）",
        "root": "latih",
        "core_meaning": "訓練する、練習する、鍛える、コーチする、トレーニング",
        "explanation": "語根 latih は、反復練習や実技トレーニングによって特定の「技能や身体能力を習熟・熟練させる」動作を表します。スポーツの監督・コーチ（pelatih）から職業訓練・企業研修（pelatihan kerja / Diklat）、熟練した専門職（tenaga terlatih）、反復練習（berlatih）まで、プロフェッショナルなスキルアップの基幹語根です。",
        "matrix": [
            ("latih", "語根", "動詞・命令", "鍛えよ、練習せよ（通常接辞付き）", "Latihlah kemampuan berkomunikasi di depan umum setiap hari."),
            ("melatih", "meN-", "他動詞", "訓練する、鍛える、指導する、教え込む", "Instruktur berpengalaman itu melatih teknik bertahan hidup di hutan."),
            ("berlatih", "ber-", "自動詞", "練習する、トレーニングする、鍛錬する", "Para atlet bulu tangkis berlatih keras enam jam sehari di pelatnas."),
            ("pelatihan", "peN- -an", "名詞", "研修、トレーニング、講習会、訓練プロセス", "Kementerian Ketenagakerjaan menyelenggarakan pelatihan vokasi gratis."),
            ("pelatih", "peN-", "名詞", "コーチ、監督、トレーナー、訓練教官", "Pelatih kepala tim nasional sepak bola menyusun strategi baru."),
            ("terlatih", "ter-", "形容詞・受動動詞", "熟練した、訓練された、百戦錬磨の", "Operasi penyelamatan darurat hanya boleh dilakukan oleh personel terlatih."),
            ("latihan", "-an", "名詞", "練習、演習、ドリル、トレーニングメニュー", "Latihan soal secara berkala sangat efektif meningkatkan nilai ujian.")
        ],
        "details": [
            ("melatih", "他動詞", "ムラティヒ",
             "人や動物に対して特定の技能や規律を「反復して教え込む・訓練する」動作です。",
             "melatih anjing pelacak（警察犬を訓練する）, melatih kesabaran（忍耐力を鍛える）, melatih otot（筋肉を鍛える）",
             "Bermain catur secara rutin dapat membantu melatih daya konsentrasi dan strategi anak.",
             "チェスを定期的にプレイすることは、子どもの集中力と戦略的思考を鍛えるのに役立つ。"),
            ("berlatih", "自動詞", "ブルラティヒ",
             "学習者やアスリート自身が自発的に「練習・稽古に励む」動作です。",
             "berlatih keras（猛特訓する）, berlatih vokal（声楽のボイストレーニングをする）",
             "Tim paduan suara sekolah giat berlatih setiap sore untuk persiapan kompetisi internasional.",
             "学校の合唱団チームは、国際コンクールの準備のため毎夕熱心に練習に励んでいる。"),
            ("pelatihan", "名詞", "プラティハン",
             "企業や公的機関が主催する「研修プログラム、スキルアップセミナー、職業訓練」です。",
             "Balai Latihan Kerja / BLK（職業訓練所）, pelatihan kepemimpinan（リーダーシップ研修）, modul pelatihan（研修テキスト）",
             "Program pelatihan kewirausahaan ini ditujukan untuk memberdayakan ibu-ibu rumah tangga.",
             "この起業家育成研修プログラムは、主婦たちのエンパワーメントを目的としている。"),
            ("terlatih", "形容詞", "トゥルラティヒ",
             "長年の練習や訓練を経て「高度な技能が身についている、熟練した」状態を表します。",
             "tenaga kerja terlatih（熟練労働者・技能工）, mata yang terlatih（訓練された眼識・鑑識眼）",
             "Mata terlatih seorang kurator seni mampu membedakan lukisan asli dengan lukisan tiruan.",
             "美術キュレーターの研ぎ澄まされた鑑識眼は、本物の絵画と贋作を見分けることができる。")
        ],
        "dialogue": {
            "title": "バドミントン代表合宿とコーチの指導方針",
            "lines": [
                ("Kevin", "Bagaimana program latihan fisik kita di bawah arahan pelatih baru, Marcus?"),
                ("Marcus", "Sangat intensif. Pelatih melatih daya tahan dan kelincahan kaki kita dengan metode modern."),
                ("Kevin", "Iya, saya merasa stamina saya meningkat drastis setelah rutin berlatih dua pekan ini."),
                ("Marcus", "Bagus. Hanya atlet yang terlatih dan berdisiplin tinggi yang mampu meraih medali emas dunia.")
            ]
        },
        "grammar_points": [
            ("pelatihan vs latihan", "pelatihan は研修制度・組織的トレーニングプログラム（training program/course）。latihan は具体的な反復練習・演習ドリル・問題集（exercise/practice/drill）。"),
            ("BLK（Balai Latihan Kerja）", "労働省が全国で運営する「公的職業訓練校」。溶接、IT、服飾、自動車整備などの実務技能を無償で学べる施設。")
        ],
        "quizzes": [
            {
                "q": "スポーツチームの「監督・ヘッドコーチ」を表すインドネシア語はどれか？",
                "options": ["A. pelatih kepala", "B. pemimpin lapangan", "C. pendidik bola", "D. guru olahraga"],
                "ans": "A. pelatih kepala",
                "expl": "ヘッドコーチ・監督は「pelatih kepala」と言います。"
            },
            {
                "q": "インドネシアの公的「職業訓練所（BLK）」の正式名称はどれか？",
                "options": ["A. Balai Latihan Kerja", "B. Badan Lembaga Ketenagakerjaan", "C. Balai Latih Karyawan", "D. Biro Latihan Keterampilan"],
                "ans": "A. Balai Latihan Kerja",
                "expl": "公的職業訓練施設は「Balai Latihan Kerja（BLK）」です。"
            },
            {
                "q": "「熟練労働者（スキルのある労働力）」を意味する経済用語はどれか？",
                "options": ["A. tenaga kerja terlatih", "B. buruh pelatihan", "C. pekerja pelatih", "D. karyawan berlatih"],
                "ans": "A. tenaga kerja terlatih",
                "expl": "熟練工・訓練を受けた労働者は「tenaga kerja terlatih（または tenaga terdidik）」と言います。"
            }
        ],
        "peribahasa": {
            "quote": "Alah bisa karena biasa.",
            "meaning": "慣れれば困難も乗り越えられる＝「習うより慣れよ」「継続は力なり」。反復練習によってどんな難事も容易になるという教え。"
        }
    },
    {
        "filename": "148-root-uji.md",
        "title": "1398. 語根 uji の全派生語図鑑（menguji, pengujian, ujian, teruji）",
        "root": "uji",
        "core_meaning": "試験する、試す、検査する、テストする、試練",
        "explanation": "語根 uji は、品質、強度、能力、あるいは信仰・忍耐の真偽を「試して検証する」コアを持ちます。学校の試験（ujian sekolah）から臨床試験（uji klinis）、実証実験（pengujian laboratorium）、試練を乗り越えて実証された（teruji）まで、科学的客観性と人生の試練を包括する語根です。",
        "matrix": [
            ("uji", "語根", "名詞・動詞", "テスト、試験、試せ", "Uji coba sistem pembayaran baru akan dilakukan pekan depan."),
            ("menguji", "meN-", "他動詞", "試験する、試す、検査・検証する、審査する", "Dosen senior ditugaskan menguji sidang skripsi para mahasiswa."),
            ("ujian", "-an", "名詞", "試験、テスト、試練、艱難辛苦", "Ujian Tulis Berbasis Komputer (UTBK) adalah syarat masuk universitas negeri."),
            ("pengujian", "peN- -an", "名詞", "検査、検定、実証実験、試験プロセス", "Pengujian sampel air tanah dilakukan di laboratorium bersertifikat."),
            ("teruji", "ter-", "形容詞・受動動詞", "実証された、試練を耐え抜いた、信頼のおける", "Keahliannya dalam memimpin krisis sudah teruji selama bertahun-tahun."),
            ("uji coba", "frasa", "名詞句", "実証実験、トライアル、試行運転", "Uji coba kereta cepat Whoosh berlangsung sukses tanpa kendala teknis."),
            ("uji klinis", "frasa", "名詞句", "臨床試験、治験", "Vaksin baru harus melewati tiga tahap uji klinis sebelum diproduksi massal.")
        ],
        "details": [
            ("menguji", "他動詞", "ムングジ",
             "性能をテストする、学生の学力を審査する、あるいは神が人の信仰を試す動作です。",
             "menguji ketahanan（耐久性をテストする）, menguji teori（理論を検証する）, menguji kesabaran（忍耐力を試す）",
             "Kondisi krisis moneter ini benar-benar menguji ketangguhan manajemen perbankan nasional.",
             "この通貨危機の状況は、国内銀行経営の強靱さを真に試している。"),
            ("ujian", "名詞", "ウジアン",
             "学校や検定のペーパーテスト、あるいは人生における「過酷な試練・災難」を指します。",
             "ujian nasional / UN（全国統一試験）, menghadapi ujian hidup（人生の試練に立ち向かう）",
             "Bagi orang beriman, musibah bencana alam dipandang sebagai ujian keimanan dan kesabaran.",
             "信仰者にとって、自然災害の災難は信仰と忍耐の試練と見なされる。"),
            ("pengujian", "名詞", "プングジアン",
             "研究機関や工場で行われる「科学的検査、安全性検定、実証プロセス」です。",
             "uji laboratorium（実験室テスト）, pengujian emisi kendaraan（車両排ガス検査）",
             "Pemerintah mewajibkan pengujian kelaikan jalan secara berkala bagi angkutan umum.",
             "政府は公共交通機関に対し、定期的な車両走行適格性検査（車検）を義務付けている。"),
            ("teruji", "形容詞", "トゥルウジ",
             "実験や幾多の危機を経て「性能・実績が実証された、本物であると証明された」状態です。",
             "kualitas teruji（実証された品質）, metode yang teruji（確立された手法）",
             "Obat herbal tradisional ini memiliki khasiat yang teruji secara empiris oleh masyarakat lokal.",
             "この伝統ハーブ薬は、地元住民によって経験的に実証された効能を備えている。")
        ],
        "dialogue": {
            "title": "新薬開発の臨床試験と安全性承認ミーティング",
            "lines": [
                ("dr. Farhan", "Bagaimana hasil tahap akhir pengujian klinis obat herbal baru kita?"),
                ("dr. Ratna", "Sangat menggembirakan. Efektivitasnya menguji daya tahan sel imun menunjukkan respons positif."),
                ("dr. Farhan", "Apakah keamanannya sudah teruji bebas dari efek samping berbahaya?"),
                ("dr. Ratna", "Sudah teruji aman pada ribuan sukarelawan. Kita siap mengajukan izin edar ke BPOM.")
            ]
        },
        "grammar_points": [
            ("uji coba（トライアル）という頻出成句", "uji（試す）+ coba（試みる）の同義的合成語で、新製品のテスト販売、新路線の試運転、新システムのパイロット運用などを指す。"),
            ("BPOM（Badan Pengawas Obat dan Makanan）", "医薬品や食品の安全性試験・認可を管轄するインドネシアの国家機関（米FDAに相当）。ニュースで必須。")
        ],
        "quizzes": [
            {
                "q": "新システムや乗り物の「実証実験・試行運転（トライアル）」を表す定型成句はどれか？",
                "options": ["A. uji coba", "B. ujian coba", "C. pengujian rasa", "D. teruji coba"],
                "ans": "A. uji coba",
                "expl": "トライアル・試行運転は「uji coba」と言います。"
            },
            {
                "q": "医学における「治験・臨床試験」を表す専門用語はどれか？",
                "options": ["A. uji klinis", "B. ujian medis", "C. pengujian dokter", "D. coba sakit"],
                "ans": "A. uji klinis",
                "expl": "臨床試験は「uji klinis」と言います。"
            },
            {
                "q": "「実績と品質が試練を経てすでに実証されている」ことを表す形容詞はどれか？",
                "options": ["A. teruji", "B. diuji", "C. penguji", "D. ujian"],
                "ans": "A. teruji",
                "expl": "実証された・信頼の置ける状態を表すため、接頭辞 ter- を伴う teruji が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Emas tahan uji, besi tahan tempa.",
            "meaning": "黄金は酸の鑑定（試験）に耐え、鉄は鍛冶の打撃に耐える＝真に有能で誠実な人間は、どんな過酷な試練や困難に遭っても本物の輝きを失わない。"
        }
    },
    {
        "filename": "149-root-nilai.md",
        "title": "1399. 語根 nilai の全派生語図鑑（menilai, penilaian, penilai, nilai）",
        "root": "nilai",
        "core_meaning": "評価する、採点する、見積もる、価値、点数、価格、理念",
        "explanation": "語根 nilai は、物や行為の「客観的価値、価格」から、テストの「点数・成績」、憲法や宗教の「理念・価値観（nilai-nilai Pancasila）」、主観的な「評価・品定め（menilai）」まで、人間の価値判断を全方位で司る最重要語根です。",
        "matrix": [
            ("nilai", "語根", "名詞", "価値、点数、価格、数値、理念", "Pancasila memuat nilai-nilai luhur kepribadian bangsa Indonesia."),
            ("menilai", "meN-", "他動詞", "評価する、採点する、鑑定する、見積もる、判断する", "Juri menilai penampilan peserta berdasarkan kreativitas dan teknik."),
            ("penilaian", "peN- -an", "名詞", "評価、査定、採点、アセスメント、鑑定評価", "Penilaian kinerja pegawai dilakukan setiap akhir semester secara objektif."),
            ("penilai", "peN-", "名詞", "鑑定士、評価員、審査員、アプレイザー", "Penilai publik menaksir harga pasar tanah yang akan dibebaskan."),
            ("bernilai", "ber-", "自動詞・形容詞", "価値がある、貴重な、高価な", "Museum nasional menyimpan ribuan artefak bernilai sejarah tinggi."),
            ("ternilai", "ter-", "受動・可能動詞", "評価される、値がつけられる（tak ternilai＝計り知れない）", "Kasih sayang orang tua adalah anugerah tak ternilai harganya."),
            ("nilai tambah", "frasa", "名詞句・経済", "付加価値（value-added）", "Hilirisasi tambang bertujuan memberikan nilai tambah bagi ekonomi nasional.")
        ],
        "details": [
            ("menilai", "他動詞", "ムニライ",
             "作品を審査する、生徒を採点する、不動産を鑑定する、人を「品定め・評価する」動作です。",
             "menilai karya seni（芸術作品を評価する）, jangan menilai dari luar（外見で判断するな）",
             "Jangan cepat menilai seseorang hanya berdasarkan penampilan fisiknya semata.",
             "外見の風貌だけに基づいて軽々しく人を判断・評価してはならない。"),
            ("penilaian", "名詞", "プニライアン",
             "学校の成績評価、人事考課、不動産鑑定などの「アセスメント手続き」を指します。",
             "penilaian kinerja karyawan / KPI（社員業績評価）, kriteria penilaian（審査基準）",
             "Hasil penilaian audit independen menunjukkan tata kelola keuangan yang sangat transparan.",
             "独立監査の評価結果は、極めて透明性の高い財務ガバナンスを示している。"),
            ("bernilai", "形容詞", "ブルニライ",
             "歴史的、金銭的、文化的に「高い価値を持っている」状態を修飾します。",
             "bernilai tinggi（高価値の）, bernilai miliaran rupiah（数十億ルピアの価値がある）",
             "Arkeolog menemukan guci keramik kuno bernilai sejarah sangat tinggi di situs candi.",
             "考古学者たちは寺院遺跡において歴史的価値の極めて高い古代陶磁器の壺を発見した。"),
            ("tak ternilai", "形容詞句", "タック・トゥルニライ",
             "金銭では換算できないほど「計り知れない、プライスレスな（priceless）」尊さを表します。",
             "tak ternilai harganya（値段がつけられないほど貴重な）, jasa tak ternilai（計り知れない功績）",
             "Pengorbanan para tenaga medis saat pandemi adalah jasa yang tak ternilai bagi kemanusiaan.",
             "パンデミック下での医療従事者たちの犠牲は、人類に対する計り知れない功績である。")
        ],
        "dialogue": {
            "title": "年末の人事考課と社員パフォーマンス評価面談",
            "lines": [
                ("Rian", "Bagaimana sistem penilaian kinerja karyawan tahun ini, Bu Maya?"),
                ("Maya", "Kita menggunakan indikator penilaian yang lebih komprehensif, mencakup pencapaian target dan kerja sama tim."),
                ("Rian", "Bagus sekali. Penilai harus bersikap objektif agar memotivasi seluruh staf."),
                ("Maya", "Pasti. Karyawan yang menciptakan nilai tambah luar biasa bagi perusahaan akan mendapat promosi.")
            ]
        },
        "grammar_points": [
            ("nilai tambah（付加価値）という現代最重要経済語", "インドネシアの国家経済政策「Hilirisasi（川下化政策）」の核心概念。未加工鉱石ではなく加工して「nilai tambah」を生み出す。"),
            ("tak ternilai harganya", "英語の priceless（値段が付けられないほど尊い）に相当する格調高い成句。感謝や家族愛を語る定番。")
        ],
        "quizzes": [
            {
                "q": "経済学やビジネスで用いられる「付加価値（バリューアッド）」のインドネシア語訳はどれか？",
                "options": ["A. nilai tambah", "B. harga lebih", "C. penilaian untung", "D. penilai pasar"],
                "ans": "A. nilai tambah",
                "expl": "付加価値は「nilai tambah」と言います。"
            },
            {
                "q": "「プライスレスな、金銭には代えられないほど貴重な」を意味する表現はどれか？",
                "options": ["A. bernilai murah", "B. tak ternilai harganya", "C. nilai sedang", "D. tanpa penilaian"],
                "ans": "B. tak ternilai harganya",
                "expl": "計り知れない価値は「tak ternilai harganya」と表現します。"
            },
            {
                "q": "「外見だけで人を判断・評価してはならない」の空欄に入る動詞は？\nJangan mudah [...] orang dari penampilannya saja.",
                "options": ["A. menilai", "B. ternilai", "C. bernilai", "D. penilai"],
                "ans": "A. menilai",
                "expl": "能動的に人を評価・品定めする動作なので、他動詞 menilai が正解です。"
            }
        ],
        "peribahasa": {
            "quote": "Bunga dipetik baunya hilang, kencana dicanai nilainya bertambah.",
            "meaning": "花は摘めば香りが失せるが、黄金は磨き鍛えるほど価値（nilai）が増す＝真の美徳や能力は鍛錬を経てこそ本物の輝きを放つ。"
        }
    }
]

# Article 150: Section 33 Master Exam
exam_content = """---
title: "1400. 【セクション33総括】語根別派生語マスター図鑑 第2弾 50問総合マスター検定"
description: "セクション33で学んだ全50語根（数量・動作・社会・権利・法務・管理・教育・評価）の派生語ネットワークを完全総括する全50問の本格総合診断検定テスト。"
---

<div class="category-badge">語根別派生語マスター図鑑 総括検定</div>

# 1400. 【セクション33総括】語根別派生語マスター図鑑 第2弾 50問総合マスター検定

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 制限時間目安: 60分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 中級〜最上級（CEFR A2〜C1）</span>
  <span class="meta-item"><i class="fas fa-list-check"></i> 全50問（各2点 / 100点満点）</span>
</div>

---

## 1. 総合マスター検定の概要と出題基準

本検定は、**セクション33「【語彙拡張】語根別派生語マスター図鑑 第2弾（記事1351〜1399）」**で体系化した全50語根の派生語ネットワークを網羅的・多角的に測定する集大成テストです。

単なる単語の意味記憶にとどまらず、以下の4大領域から出題されます：
1. **接辞と語根の形態音韻変化**（meN-の鼻音化、ber-とmeN-の自他動詞対比、peN-...-anとper-...-anの区別）
2. **語用論的コロケーションと文脈適合性**（成句、ビジネス・法律・行政実務用語）
3. **類義語根・対義語根の精密な意味境界**（cegah vs hindar, tuntut vs gugat, tolong vs bantu, tumbuh vs kembang）
4. **ことわざ（Peribahasa）と文化的文脈**

---

## 2. 50問総合マスター検定 本番問題

各問の4つの選択肢（A〜D）から最も適切なものを1つ選んでください。全問回答後、各アコーディオンを開いて正解と詳細解説を確認してください。

"""

# 50 comprehensive questions
questions_data = [
    # 1-10: 1351-1360 (atur, hubung, susun, pecah, ikat, lepas, pasang, ganti, ubah, pindah)
    ("交通整理や法規制の「規則・法令」を表す法律用語は？", ["A. pengaturan", "B. peraturan", "C. teratur", "D. pengatur"], "B. peraturan", "国家や自治体が定める規則・法令は peraturan（例: Peraturan Pemerintah）です。pengaturan は調整・手配プロセスです。"),
    ("「関係省庁・関連部署」を表す行政成句は？", ["A. instansi terkait", "B. instansi perhubungan", "C. instansi berhubung", "D. instansi ikatan"], "A. instansi terkait", "関連する機関は terkait（語根 ikat ＝結びついた）を用いて「instansi terkait」と言います。"),
    ("書籍や辞書を「編纂・執筆・構成する」能動動作を表す動詞は？", ["A. menyusun", "B. susunan", "C. penyusun", "D. tersusun"], "A. menyusun", "本や計画を整理・編纂する他動詞は menyusun です。"),
    ("民族や国家組織の「内部対立による分裂・解体」を表す名詞は？", ["A. pecahan", "B. perpecahan", "C. memecahkan", "D. terpecah"], "B. perpecahan", "集団内の亀裂・分裂事象は名詞 perpecahan と言います。"),
    ("「雇用契約、法的な債権債務関係」を表す法務用語は？", ["A. ikatan dinas", "B. perikatan", "C. mengikat", "D. terikat"], "B. perikatan", "民法上の債権・債務関係（契約の拘束関係）は perikatan と言います。"),
    ("鳥や被疑者を「檻・拘束から解き放つ・釈放する」他動詞は？", ["A. melepaskan", "B. berlepas", "C. pelepasan", "D. terlepas"], "A. melepaskan", "対象を解放する使役他動詞は melepaskan です。"),
    ("機器の「取り付け・設置工事」を表す名詞は？", ["A. pasangan", "B. pemasangan", "C. terpasang", "D. mempasang"], "B. pemasangan", "工事や作業プロセスは名詞 pemasangan です。"),
    ("政権や世代の「交代・交替」を表す名詞は？", ["A. ganti rugi", "B. pergantian", "C. pengganti", "D. berganti"], "B. pergantian", "体制や世代の交代現象は pergantian（例: pergantian generasi）です。"),
    ("社会構造や気候の「劇的な変動・変化」を表す名詞は？", ["A. pengubahan", "B. perubahan", "C. terubah", "D. mengubah"], "B. perubahan", "自然・自発的な変化や社会変動は名詞 perubahan（例: perubahan iklim）です。"),
    ("人口の都市への「移動・移住」を表す名詞は？", ["A. perpindahan", "B. pemindahan", "C. berpindah", "D. memindahkan"], "A. perpindahan", "自発的な移動現象は perpindahan（例: perpindahan penduduk）です。"),

    # 11-20: 1361-1370 (tambah, kurang, bagi, gabung, kumpul, pisah, tarik, dorong, angkat, turun)
    ("「従業員の時間外労働手当（割増賃金）」を意味する表現は？", ["A. upah tambahan", "B. upah bertambah", "C. penambahan upah", "D. tambah upah"], "A. upah tambahan", "追加の手当・給与は形容詞的用法で「upah tambahan」と言います。"),
    ("「およそ、約（kira-kira）」を意味する成句副詞は？", ["A. kurang lebih", "B. sedikit kurang", "C. kekurangan", "D. mengurangi"], "A. kurang lebih", "大体・およそは成句で「kurang lebih」と言います。"),
    ("「知識や経験を互いに共有・分かち合う」動詞句は？", ["A. membagi rata", "B. berbagi pengalaman", "C. sebagian jalan", "D. pembagian tugas"], "B. berbagi pengalaman", "自発的な共有・分かち合いは自動詞 berbagi を用いて「berbagi pengalaman」と言います。"),
    ("「多国籍企業同士が対等合併する」ことを表す名詞は？", ["A. penggabungan", "B. gabungan", "C. bergabung", "D. tergabung"], "A. penggabungan", "企業の合併・統合プロセスは名詞 penggabungan（マージャー）です。"),
    ("「市民団体、有志のサークル集会組織」を表す名詞は？", ["A. pengumpulan", "B. perkumpulan", "C. kumpulan", "D. terkumpul"], "B. perkumpulan", "人々が集まる結社・団体は名詞 perkumpulan と言います。"),
    ("「夫婦の正式な離婚・別離」を表す動詞は？", ["A. memisahkan", "B. berpisah", "C. pemisahan", "D. terpisah"], "B. berpisah", "互いに分かれる相互動作は自動詞 berpisah を用います。"),
    ("観光地が持つ「人を惹きつける魅力・アピール力」を表す成句は？", ["A. daya tarik", "B. penarikan dana", "C. menarik hati", "D. tertarik wisata"], "A. daya tarik", "魅力・求心力は定型成句で「daya tarik」と言います。"),
    ("経済成長を牽引する「主たる推進力・原動力」を表す名詞は？", ["A. dorongan", "B. pendorong utama", "C. mendorong", "D. terdorong"], "B. pendorong utama", "推進役・原動力は名詞 pendorong を用いて「pendorong utama」と言います。"),
    ("公的な不祥事に対して要人が「口を開いて意見表明する」慣用表現は？", ["A. angkat tangan", "B. angkat bicara", "C. angkat kaki", "D. angkat topi"], "B. angkat bicara", "公に発言・コメントすることは「angkat bicara」と言います。angkat tangan は降参、angkat kaki は逃亡です。"),
    ("大統領や警察トップが自ら現場へ「介入し直接手を差し伸べる」慣用動詞は？", ["A. turun tangan", "B. turun harga", "C. penurunan", "D. menurunkan"], "A. turun tangan", "自ら直接介入して解決を図ることは「turun tangan」と言います。"),

    # 21-30: 1371-1380 (naik, jatuh, bangkit, runtuh, roboh, tumbuh, kembang, maju, mundur, hindar)
    ("タレントや商品が「脚光を浴びて人気絶頂にある」ことを表す慣用句は？", ["A. naik pitam", "B. naik daun", "C. naik kelas", "D. naik banding"], "B. naik daun", "人気急上昇・脚光を浴びている状態は「naik daun」と言います。"),
    ("請求書や契約の「支払期日が到来する（満期になる）」成句は？", ["A. jatuh hati", "B. jatuh tempo", "C. jatuh miskin", "D. jatuh bangun"], "B. jatuh tempo", "期日満了・支払い期限は「jatuh tempo」と言います。"),
    ("毎年5月20日に記念されるインドネシアの歴史的記念日は？", ["A. Hari Kebangkitan Nasional", "B. Hari Pahlawan", "C. Hari Sumpah Pemuda", "D. Hari Kesaktian Pancasila"], "A. Hari Kebangkitan Nasional", "民族的覚醒を祝う日は「Hari Kebangkitan Nasional」です。"),
    ("古代寺院の崩壊した「石造遺跡・瓦礫の残骸」を表す集合名詞は？", ["A. keruntuhan", "B. reruntuhan", "C. runtuhan", "D. peruntuhan"], "B. reruntuhan", "散乱する瓦礫や遺跡群は部分重複名詞「reruntuhan（例: reruntuhan candi）」です。"),
    ("強風で倒れてきた電柱の「下敷きになって被災する」動詞構文は？", ["A. merobohkan tiang", "B. kerobohan tiang", "C. perobohan tiang", "D. teroboh tiang"], "B. kerobohan tiang", "倒壊物に直撃される被災動詞は ke-...-an を伴う「kerobohan」です。"),
    ("子どもの「心身の発育と発達」を一括して指す小児医学の慣用句は？", ["A. tumbuh kembang", "B. tumbuhan anak", "C. pertumbuhan saja", "D. berkembang biak"], "A. tumbuh kembang", "子どもの成育・発達は連語で「tumbuh kembang」と言います。"),
    ("国の省庁や公的機関における「研究開発（R&D）」の公的略称は？", ["A. Litbang", "B. Balitbang", "C. Ristek", "D. Puslit"], "A. Litbang", "Penelitian dan Pengembangan の頭文字をとって「Litbang」と言います。"),
    ("急用のため会議の予定を「繰り上げる（前倒しにする）」動詞は？", ["A. memundurkan", "B. memajukan", "C. memajukan jadwal", "D. kemajuan jadwal"], "C. memajukan jadwal", "日程を早める使役表現は「memajukan jadwal」です。"),
    ("役員が責任を取って「辞職届・退職願を提出する」動詞句は？", ["A. mengundurkan diri", "B. memundurkan diri", "C. kemunduran jabatan", "D. mundur kerja"], "A. mengundurkan diri", "自発的に辞任することは「mengundurkan diri」と言います。"),
    ("健康的な生活により生活習慣病の罹患を「免れる・助かる」動詞は？", ["A. menghindari", "B. terhindar", "C. penghindaran", "D. menghindarkan"], "B. terhindar", "前置詞 dari と結びつき難を逃れる状態は「terhindar」を用います。"),

    # 31-40: 1381-1390 (cegah, lindung, bela, tuntut, gugat, tolak, terima, tolong, bantu, layan)
    ("「予防は治療に勝る」に相当する医学格言の空欄に入る語は？\n[...] lebih baik daripada mengobati.", ["A. Menghindari", "B. Mencegah", "C. Tercegah", "D. Pencegahan"], "B. Mencegah", "格言は「Mencegah lebih baik daripada mengobati」です。"),
    ("医療従事者や建設作業員が身につける「個人防護具（PPE）」の略称は？", ["A. APD", "B. P3K", "C. KPK", "D. KTP"], "A. APD", "Alat Pelindung Diri の略称は「APD」です。"),
    ("裁判の最終公判で弁護側が読み上げる「弁論趣意書（Pledoi）」の標準名は？", ["A. surat gugatan", "B. nota pembelaan", "C. berkas tuntutan", "D. putusan vonis"], "B. nota pembelaan", "弁護側の最終弁論書は「nota pembelaan」です。"),
    ("裁判で公訴を提起し求刑を行う「公設検察官」の略称（JPU）の正式名は？", ["A. Jaksa Penuntut Umum", "B. Juri Pengadilan Umum", "C. Jaksa Pemutus Utama", "D. Jajaran Penegak Undang"], "A. Jaksa Penuntut Umum", "検察官は「Jaksa Penuntut Umum（JPU）」です。"),
    ("民事訴訟において訴訟を起こした「原告」を表す法廷用語は？", ["A. terdakwa", "B. penggugat", "C. tergugat", "D. penuntut"], "B. penggugat", "民事の原告は「penggugat」です。被告は tergugat、刑事の被告人は terdakwa です。"),
    ("業績や品質を測る客観的な「評価基準・尺度（ベンチマーク）」を表す成句は？", ["A. tolak ukur", "B. tolak bala", "C. bertolak ukur", "D. penolakan nilai"], "A. tolak ukur", "基準・尺度は「tolak ukur（tolok ukur）」と言います。"),
    ("各種税金による「国家歳入」を表す財政用語は？", ["A. penerimaan pajak", "B. pengeluaran pajak", "C. terima bersih", "D. keterimaan kas"], "A. penerimaan pajak", "税収歳入は「penerimaan pajak」です。"),
    ("家庭やオフィスに常備される「応急救急箱」を表す略語（P3K）の正式名は？", ["A. Pertolongan Pertama Pada Kecelakaan", "B. Perlindungan Pasien Pasca Krisis", "C. Pusat Pengobatan Penyakit Kronis", "D. Penyelamatan Pertama Petugas Medis"], "A. Pertolongan Pertama Pada Kecelakaan", "P3K の正式名称は「Pertolongan Pertama Pada Kecelakaan」です。"),
    ("低所得者層へ直接配分される「社会保障給付金」の通称略語は？", ["A. Bansos", "B. BUMN", "C. BPJS", "D. BLT"], "A. Bansos", "Bantuan Sosial の略称は「Bansos（バンソス）」です。"),
    ("公務員や民間サービスが目指す「最高品質のエクセレントサービス」は？", ["A. pelayanan prima", "B. pelayan utama", "C. layanan pertama", "D. terlayani unggul"], "A. pelayanan prima", "エクセレントサービスは定型語で「pelayanan prima」と言います。"),

    # 41-50: 1391-1399 (urus, kelola, pimpin, arah, bimbing, didik, latih, uji, nilai)
    ("「それは私の知ったことではない（余計なお世話だ）」を表す成句は？", ["A. Itu bukan urusan saya", "B. Itu tak terurus saya", "C. Itu pengurus saya", "D. Itu urus sendiri"], "A. Itu bukan urusan saya", "関係ない・私事ではないは「Itu bukan urusan saya」と言います。"),
    ("企業の健全経営に不可欠な「コーポレート・ガバナンス（企業統治）」は？", ["A. tata urus perusahaan", "B. tata kelola perusahaan", "C. pengurus bisnis", "D. aturan kelola"], "B. tata kelola perusahaan", "ガバナンスは「tata kelola」と言います。"),
    ("新聞社や雑誌社のトップである「編集長」を表す役職名は？", ["A. pemimpin redaksi", "B. pimpinan redaksi", "C. ketua berita", "D. kepala jurnalistik"], "A. pemimpin redaksi", "編集長個人は「pemimpin redaksi（Pemred）」と言います。"),
    ("上司や首長が部下に示す「指導方針・助言ガイドライン」を表す実務語は？", ["A. arahan", "B. pengarahan", "C. terarah", "D. searah"], "A. arahan", "指針・ガイダンスは名詞「arahan」です。"),
    ("大学で卒業論文を個別指導する「論文指導教員」の呼称は？", ["A. Dosen Pembimbing", "B. Dosen Pendidik", "C. Dosen Pengarah", "D. Dosen Pengurus"], "A. Dosen Pembimbing", "指導教員は「Dosen Pembimbing（Dosbing）」です。"),
    ("インドネシアの教育法令で児童・生徒・受講生を指す包括的公用語は？", ["A. anak didik", "B. peserta didik", "C. murid sekolah", "D. kaum terdidik"], "A. peserta didik", "公的呼称は「peserta didik」です。"),
    ("労働省が運営する公的「職業訓練所（BLK）」の正式名称は？", ["A. Balai Latihan Kerja", "B. Badan Lembaga Kerja", "C. Biro Latih Kejuruan", "D. Balai Latih Karyawan"], "A. Balai Latihan Kerja", "公的職業訓練所は「Balai Latihan Kerja（BLK）」です。"),
    ("新車両や新システムの「実証実験・試行運転（トライアル）」を表す成句は？", ["A. uji coba", "B. ujian coba", "C. pengujian rasa", "D. teruji coba"], "A. uji coba", "トライアルは「uji coba」と言います。"),
    ("産業川下化（Hilirisasi）の主目的である「付加価値」のインドネシア語は？", ["A. nilai lebih", "B. nilai tambah", "C. penilai laba", "D. bertambah nilai"], "B. nilai tambah", "付加価値は「nilai tambah」です。"),
    ("金銭では換算できないほど「計り知れない、尊い」価値を表す成句は？", ["A. tak bernilai", "B. tak ternilai harganya", "C. tanpa nilai", "D. harga ternilai"], "B. tak ternilai harganya", "計り知れない尊さは「tak ternilai harganya」と言います。")
]

for idx, (q, opts, ans, expl) in enumerate(questions_data, 1):
    opts_str = "\n".join([f"- {opt}" for opt in opts])
    exam_content += f"""### 第{idx}問
**{q}**
{opts_str}

<details>
<summary>正解と解説を見る</summary>

**正解**: 「**{ans}**」

**解説**:
{expl}
</details>

---

"""

exam_content += """## 3. スコア判定基準とマスターレベル判定表

全50問の正解数に応じて、現在のあなたの派生語ネットワークの習熟度を判定します。

| 正解数 / 得点 | 判定レベル | 評価と推奨学習アドバイス |
| :---: | :---: | :--- |
| **46〜50問 (92〜100点)** | **C2: ネイティブ最上級マスター** | 完璧です！法律・行政・ビジネス・日常会話からことわざに至る全50語根の派生語体系を完全にマスターしています。プロの通訳・翻訳者や高度ビジネス交渉者として申し分ない語彙運用力です。 |
| **40〜45問 (80〜90点)** | **C1: 上級エキスパート** | 非常に優秀です！ほとんどの派生語と接辞の使い分けを正しく理解できています。間違えた数問の専門用語（法務・行政・略語）を復習すれば完全無欠になります。 |
| **32〜39問 (64〜78点)** | **B2: 実践中上級レベル** | 合格水準です！日常会話や一般ニュースは問題なく読みこなせます。類義語根の使い分け（cegah vs hindar, tuntut vs gugat等）や名詞化の接辞パターンを再確認しましょう。 |
| **25〜31問 (50〜62点)** | **B1: 成長中級レベル** | 基礎的な派生語は定着していますが、接辞による微妙な品詞転換や成句で迷いが見られます。各語根の5列マトリックス表と例文カードを重点的に音読復習してください。 |
| **24問以下 (48点以下)** | **A2: 基礎再強化推奨** | 語根のコアミーニングと接辞の基本規則（meN-, ber-, di-, peN-...-an, per-...-an）に戻り、1記事ずつ例文カードを反復練習することをお勧めします。 |

---

## 4. セクション33完結記念メッセージ

おめでとうございます！**セクション33「語根別派生語マスター図鑑 第2弾（全50記事）」**を完全走破しました。
第1弾（50語根）と合わせた**計100大語根**の派生語ネットワークを習得したことにより、あなたのインドネシア語語彙力は**数千語規模へと爆発的に拡大**しました。

未知の単語に出会っても、その「語根」と「接辞」を瞬時に分解し、文脈から正確な意味を推理できる**真の言語的直観**が完成しています。
誇りを持って、次のステージへと進んでください！

---

## 5. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""

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

    # Generate 150-section33-master-exam.md
    exam_path = os.path.join(target_dir, "150-section33-master-exam.md")
    with open(exam_path, "w", encoding="utf-8") as f:
        f.write(exam_content)
    print(f"Generated: {exam_path}")

if __name__ == "__main__":
    main()
