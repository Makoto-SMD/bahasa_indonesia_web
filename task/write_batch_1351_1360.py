# -*- coding: utf-8 -*-
"""
セクション33 第1バッチ (1351-1360) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾
"""

import os

articles = [
    {
        "filename": "101-root-atur.md",
        "title": "1351. 語根 atur の全派生語図鑑（mengatur, peraturan, pengaturan, teratur）",
        "root": "atur",
        "core_meaning": "整理する、整える、秩序づける、手配する、規則を設ける",
        "explanation": "語根 atur は、無秩序な状態にあるものに秩序（tata）を与え、一定のルールや計画に沿って「整える・配置する・取り仕切る」という極めて重要なコアを持ちます。行政規則（peraturan）からスケジュール調整（mengatur jadwal）、日々の規則正しい生活（hidup teratur）に至るまで、社会生活の根幹を支える派生語群を生み出します。",
        "matrix": [
            ("mengatur", "meN-", "他動詞", "整理する、手配・調整する、取り仕切る", "Manajer sedang mengatur jadwal pertemuan penting besok."),
            ("diatur", "di-", "受動態動詞", "調整される、規定される、整理される", "Tata tertib sekolah telah diatur dalam buku panduan ini."),
            ("peraturan", "per- -an", "名詞", "規則、規定、法規、条例", "Kita harus mematuhi peraturan lalu lintas demi keselamatan."),
            ("pengaturan", "peN- -an", "名詞", "設定、調整作業、管理配置のプロセス", "Pengaturan privasi akun media sosial harus diperiksa berkala."),
            ("teratur", "ter-", "形容詞・状態動詞", "規則正しい、整然とした、定期的な", "Olahraga teratur sangat baik untuk menjaga kebugaran tubuh."),
            ("keteraturan", "ke- -an", "名詞", "規則正しさ、秩序、整然性", "Keteraturan sistem transportasi meningkatkan produktivitas."),
            ("pengatur", "peN-", "名詞", "調節器、コントローラー、手配役", "Alat pengatur suhu ruangan ini bekerja secara otomatis.")
        ],
        "details": [
            ("mengatur", "他動詞", "アングトゥール",
             "何かを意図的に整然とした状態にする、あるいは物事の段取りをつける行為全般を表します。",
             "mengatur jadwal（日程を調整する）, mengatur keuangan（家計・財務を管理する）, mengatur strategi（戦略を立てる）",
             "Ibu guru dengan sabar mengatur barisan murid di halaman sekolah.",
             "先生は校庭で辛抱強く生徒たちの列を整えた。"),
            ("peraturan", "名詞", "プラトゥーラン",
             "社会や組織において秩序を保つために制定された「法規・規則・ルール」という成果物・制度そのものを指します。",
             "peraturan pemerintah（政府規制・政令）, peraturan perundang-undangan（法令・規則）, melanggar peraturan（規則に違反する）",
             "Peraturan baru ini mulai berlaku secara efektif per 1 Januari.",
             "この新規則は1月1日より有効に施行される。"),
            ("pengaturan", "名詞", "プンガトゥーラン",
             "規則を策定したり、機器・環境の設定を調整・管理したりする「プロセス・設定作業そのもの」を指します。",
             "pengaturan suhu（温度設定）, pengaturan privasi（プライバシー設定）, pengaturan arus lalu lintas（交通流の整理・管制）",
             "Pengaturan sistem audio ini membutuhkan waktu sekitar tiga puluh menit.",
             "この音響システムの設定作業には約30分の時間を要する。"),
            ("teratur", "形容詞", "トラトゥール",
             "乱れがなく「整然とした、規則正しい」状態を表します。生活習慣や運動の頻度を形容する際によく使われます。",
             "hidup teratur（規則正しい生活を送る）, berolahraga secara teratur（定期的に運動する）, berbaris teratur（整然と並ぶ）",
             "Minumlah obat ini secara teratur tiga kali sehari setelah makan.",
             "この薬を食後に1日3回規則正しく服用してください。")
        ],
        "dialogue": {
            "title": "オフィスでの新プロジェクト進行スケジュールの調整",
            "lines": [
                ("Budi", "Selamat pagi, Bu Rina. Bagaimana kita akan mengatur jadwal rapat untuk proyek baru ini?"),
                ("Rina", "Selamat pagi, Budi. Saya rasa jadwalnya harus diatur secara teratur setiap hari Senin pagi agar tim tetap fokus."),
                ("Budi", "Baik, Bu. Apakah ada peraturan khusus mengenai batas pengumpulan laporan mingguannya?"),
                ("Rina", "Tentu, sesuai peraturan perusahaan, laporan harus dikirim paling lambat hari Jumat sore. Tolong periksa pengaturan kalender tim sekarang ya.")
            ]
        },
        "grammar_point": """### per- -an（peraturan）vs peN- -an（pengaturan）の使い分け

接辞 `per- -an` と `peN- -an` はともに名詞を作りますが、明確なニュアンスの差があります：
- **peraturan**: 調整や規則化の結果として生まれた**「制度・ルール・規範そのもの」**を指します（静的な成果物）。
- **pengaturan**: 実際に調整・設定・整理を行う**「行為・プロセス・設定作業」**を指します（動的なプロセス）。

スマホの画面で「設定」メニューを開くときは、設定作業を行う場所であるため **Pengaturan (Settings)** と表記されます。""",
        "quiz": [
            {
                "q": "Kalimat mana yang menggunakan kata 'peraturan' secara tepat?",
                "options": [
                    "Tolong buka menu peraturan suhu AC di dinding.",
                    "Setiap pengendara motor wajib mematuhi peraturan lalu lintas.",
                    "Dokter menyarankan saya makan secara peraturan tiga kali sehari.",
                    "Dia sedang peraturan buku-buku di rak perpustakaan."
                ],
                "ans": "Setiap pengendara motor wajib mematuhi peraturan lalu lintas.",
                "exp": "交通法規（ルール）を守るという意味では名詞 peraturan が適切です。"
            },
            {
                "q": "Kata yang tepat untuk mendeskripsikan kebiasaan olahraga yang 'disiplin dan rutin' adalah...",
                "options": ["mengatur", "peraturan", "teratur", "pengatur"],
                "ans": "teratur",
                "exp": "「規則正しい、定期的な」という状態・様子を表すには形容詞 teratur を用います（berolahraga secara teratur）。"
            },
            {
                "q": "Apa arti dari 'pengaturan' dalam konteks telepon pintar (smartphone)?",
                "options": ["Surat izin kepemilikan ponsel", "Menu pengaturan/setelan fungsi perangkat (Settings)", "Hukuman denda penggunaan ponsel", "Toko tempat membeli ponsel baru"],
                "ans": "Menu pengaturan/setelan fungsi perangkat (Settings)",
                "exp": "スマホの文脈における pengaturan は、動作環境を調整・設定する機能メニュー（Settings）を意味します。"
            }
        ],
        "column": """### 語源コラム：インドネシア語の「秩序」を司る「Tata」と「Atur」

インドネシア語で秩序や管理を語る際、「Atur」と並んで頻出するのがサンスクリット語由来の「Tata」です。「Tata tertib（校則・規律）」「Tata bahasa（文法）」「Tata ruang（都市空間計画）」のように、複合名詞の先頭に付いて秩序の枠組みを形作ります。

この「Tata」という基盤の上に、人間が能動的に手を入れて秩序を保つ動作が「Atur」です。「Hidup yang teratur membawa ketenangan jiwa（規律正しい生活が魂の平穏をもたらす）」という言葉通り、日々の生活を主体的に整える美徳がこの語根に宿っています。"""
    },
    {
        "filename": "102-root-hubung.md",
        "title": "1352. 語根 hubung の全派生語図鑑（menghubungkan, berhubungan, hubungan, perhubungan）",
        "root": "hubung",
        "core_meaning": "繋ぐ、結びつける、関係する、連絡を取る、接続する",
        "explanation": "語根 hubung は、離れた2つ以上の点、人、概念の間を架橋して「繋ぐ・結びつける・関わりを持つ」というコアを持ちます。人間関係（hubungan）から通信・交通（perhubungan）、因果関係の関連づけ（menghubungkan）まで、ネットワーク社会を表現する最重要語根の一つです。",
        "matrix": [
            ("menghubungkan", "meN- -kan", "他動詞", "結びつける、接続する、連絡させる", "Jembatan baru ini menghubungkan dua pulau yang terpisah."),
            ("dihubungkan", "di- -kan", "受動態動詞", "接続される、関連づけられる", "Komputer harus dihubungkan ke jaringan internet."),
            ("berhubungan", "ber-", "自動詞", "関係がある、関連する、連絡を取り合う", "Masalah kesehatan mental erat berhubungan dengan pola tidur."),
            ("hubungan", "-an", "名詞", "関係、結びつき、人間関係、交際", "Indonesia dan Jepang memiliki hubungan diplomatik yang sangat erat."),
            ("perhubungan", "per- -an", "名詞", "交通・運輸、通信・通信行政", "Kementerian Perhubungan mengawasi kelayakan bus antarkota."),
            ("penghubung", "peN-", "名詞", "媒介者、中継役、連絡通路・接続具", "Jalan tikus ini menjadi jalur penghubung antardesa."),
            ("terhubung", "ter-", "状態動詞", "接続されている、繋がっている", "Ponsel saya sudah terhubung dengan jaringan Wi-Fi kantor.")
        ],
        "details": [
            ("menghubungkan", "他動詞", "ムングフブンカン",
             "AとBの二者を物理的または論理的にリンクさせる、あるいは人に電話や連絡を取り次ぐ際に用います。",
             "menghubungkan jalan（道路を接続する）, menghubungkan fakta（事実を結びつける）, menghubungi（連絡する）",
             "Pemandu wisata menghubungkan wisatawan dengan pengrajin lokal.",
             "ツアーガイドは観光客を地元の職人たちと引き合わせた。"),
            ("berhubungan", "自動詞", "ブルフブンガン",
             "主語が他の要素と「関連している（berhubungan dengan...）」、または「連絡を取り合っている」状態を表します。",
             "tidak berhubungan（無関係である）, berhubungan baik（良好な関係を保っている）, berhubungan langsung（直接関係する）",
             "Gejala demam ini berhubungan langsung dengan infeksi bakteri.",
             "この発熱症状は細菌感染と直接関連している。"),
            ("hubungan", "名詞", "フブンガン",
             "国家間、人と人、事象間の「関係・結びつき」そのものを指す極めて汎用性の高い名詞です。",
             "hubungan internasional（国際関係）, hubungan kerja（雇用関係）, hubungan bilateral（二国間関係）",
             "Komunikasi yang jujur adalah kunci dari hubungan yang harmonis.",
             "誠実なコミュニケーションこそが調和のとれた関係の鍵である。"),
            ("perhubungan", "名詞", "プルフブンガン",
             "社会的な交通、運輸、通信網という大規模なインフラ・行政システムを指す専門的な名詞です。",
             "Kementerian Perhubungan (Kemenhub)（運輸省）, dinas perhubungan（交通局）, alat perhubungan（通信・交通手段）",
             "Dinas Perhubungan mengerahkan ratusan personel untuk mengurai kemacetan.",
             "交通局は渋滞を解消するために数百名の要員を配置した。")
        ],
        "dialogue": {
            "title": "ビジネスパートナーとの提携関係と連絡手段の確認",
            "lines": [
                ("Doni", "Apakah Anda sudah berhasil menghubungi pihak investor dari Tokyo?"),
                ("Sinta", "Sudah, Pak Doni. Saya sudah berbicara langsung dengan manajer perhubungan eksternal mereka."),
                ("Doni", "Bagus. Bagaimana respon mereka terkait hubungan kerja sama jangka panjang kita?"),
                ("Sinta", "Sangat positif. Mereka sepakat bahwa proyek ini akan menghubungkan pasar teknologi kedua negara secara strategis.")
            ]
        },
        "grammar_point": """### hubungi（他動詞）vs berhubungan（自動詞）の違い

語根 hubung から生じる連絡・コンタクトの動詞には重要な文法差があります：
- **menghubungi**（語根+ -i）：前置詞なしで直接目的語を取る他動詞。「〜に連絡する（contact someone）」。
  - 例: *Saya akan menghubungi dokter.*（私は医師に連絡します。）
- **berhubungan dengan...**（接頭辞 ber-）：前置詞 dengan を伴って関連や連絡を表す自動詞。
  - 例: *Saya sedang berhubungan dengan pihak kedutaan.*（私は大使館側と連絡を取り合っています。）""",
        "quiz": [
            {
                "q": "Kata mana yang paling tepat untuk melengkapi: 'Kementerian ... mengumumkan jadwal mudik gratis lebaran.'?",
                "options": ["Hubungan", "Perhubungan", "Menghubungkan", "Terhubung"],
                "ans": "Perhubungan",
                "exp": "交通・運輸行政を担う省庁の公式名称は「Kementerian Perhubungan（運輸省）」です。"
            },
            {
                "q": "Manakah kalimat yang menggunakan 'menghubungkan' dengan benar?",
                "options": [
                    "Dia sedang menghubungkan baik dengan tetangganya.",
                    "Jalan tol ini menghubungkan Kota Jakarta dan Surabaya.",
                    "Ponsel saya sudah menghubungkan dengan internet.",
                    "Mereka memiliki menghubungkan yang harmonis."
                ],
                "ans": "Jalan tol ini menghubungkan Kota Jakarta dan Surabaya.",
                "exp": "「都市Aと都市Bを物理的に繋ぐ」という他動詞用法として正しく用いられています。"
            },
            {
                "q": "Apa lawan kata atau negasi yang umum dari 'berhubungan dengan'?",
                "options": ["tidak berhubungan dengan", "sangat hubungan", "kehilangan perhubungan", "pengait hubungan"],
                "ans": "tidak berhubungan dengan",
                "exp": "「〜と関係がない、無関係である」は否定詞 tidak を用いて「tidak berhubungan dengan」と表現します。"
            }
        ],
        "column": """### 語源コラム：島々を繋ぐ「Poros Maritim」とインドネシアの血脈

1万7千以上の島々からなるインドネシアにおいて、「Hubung（繋ぐ）」は単なる言葉ではなく国家存亡の基本哲学です。島と島が海で隔てられているのではなく、「海によって結ばれている（Laut yang menghubungkan）」という群島国家ドクトリン（Wawasan Nusantara）の根底には、常にこの語根があります。

交通網が未発達な地域では、今でも小型連絡船が「Kapal Penghubung（連絡船）」と呼ばれ、人々の命と生活物資を繋ぎ止める生命線となっています。"""
    },
    {
        "filename": "103-root-susun.md",
        "title": "1353. 語根 susun の全派生語図鑑（menyusun, susunan, penyusun, tersusun）",
        "root": "susun",
        "core_meaning": "積み重ねる、並べる、編纂する、整理して構築する",
        "explanation": "語根 susun は、要素を順序正しく下から上へ積み重ねたり、論理的に並べて一つのまとまりを「編纂・構築する」というコアを持ちます。物理的なレンガの積み重ねから、内閣人事（susunan kabinet）、書籍の編纂（penyusun buku）、計画の立案（menyusun rencana）まで、知的・構造的創造を象徴する語根です。",
        "matrix": [
            ("menyusun", "meN-", "他動詞", "並べる、積み重ねる、編纂・立案する", "Komite sedang menyusun rencana aksi tahunan."),
            ("disusun", "di-", "受動態動詞", "構築される、編纂される、並べられる", "Buku kamus ini disusun oleh para ahli bahasa terkemuka."),
            ("susunan", "-an", "名詞", "構成、配列、編成、構造", "Presiden mengumumkan susunan kabinet baru di istana negara."),
            ("penyusun", "peN-", "名詞", "編纂者、作成者、構成要素", "Tim penyusun kamus bekerja keras selama lima tahun."),
            ("penyusunan", "peN- -an", "名詞", "作成・編纂作業、策定プロセス", "Proses penyusunan anggaran daerah berjalan secara transparan."),
            ("bersusun", "ber-", "自動詞・形容詞", "階層になった、重なり合った、段々になった", "Kue lapis legit memiliki pola warna yang bersusun indah."),
            ("tersusun", "ter-", "状態動詞", "整然と構築された、組み立てられている", "Semua dokumen arsip telah tersusun rapi di lemari.")
        ],
        "details": [
            ("menyusun", "他動詞", "ムニュスン",
             "物や計画、文章を論理的・構造的に順序立てて作り上げる動作です。",
             "menyusun laporan（報告書を作成する）, menyusun anggaran（予算を策定する）, menyusun strategi（戦略を構築する）",
             "Para menteri berkumpul untuk menyusun langkah penyelamatan ekonomi.",
             "閣僚たちは経済救済措置を策定するために集まった。"),
            ("susunan", "名詞", "ススナン",
             "組み合わされて完成した「組織構成、序列、メンバー編成、構造」を指します。",
             "susunan organisasi（組織図・構造）, susunan acara（式次第・プログラム）, susunan kata（語順・統語）",
             "Susunan acara seminar telah difinalisasi oleh panitia pelaksana.",
             "セミナーのプログラム構成は実行委員会によって最終決定された。"),
            ("penyusun", "名詞", "プニュスン",
             "本や辞書、計画書などを執筆・編集した「作成者・編纂者」、あるいは物質を形作る「構成成分」を指します。",
             "tim penyusun（編纂委員会・作成チーム）, unsur penyusun（構成要素・元素）",
             "Nama-nama anggota tim penyusun tercantum di halaman pembuka laporan.",
             "報告書の冒頭ページに作成チームのメンバー名が記載されている。"),
            ("tersusun", "形容詞・状態動詞", "トルススン",
             "すでに完成して「整然と並んでいる・組み立てられている」完了状態を表します。",
             "tersusun rapi（几帳面に整理されている）, tersusun dari...（〜から構成されている）",
             "Koleksi buku kuno itu tersusun rapi berdasarkan abjad dan tahun penerbitan.",
             "その古書コレクションはアルファベットと出版年に基づいて几帳面に整理されている。")
        ],
        "dialogue": {
            "title": "新年度の年間行事計画とイベントプログラムの策定",
            "lines": [
                ("Wawan", "Apakah tim Anda sudah mulai menyusun susunan acara untuk festival budaya bulan depan?"),
                ("Maya", "Sudah, Mas Wawan. Draf awalnya sudah tersusun rapi dan sedang ditinjau oleh ketua panitia."),
                ("Wawan", "Bagus sekali. Pastikan tim penyusun berkoordinasi dengan pengisi acara lokal ya."),
                ("Maya", "Tentu, proses penyusunan jadwal pentas seni akan kami selesaikan akhir pekan ini.")
            ]
        },
        "grammar_point": """### menyusun vs membuat のレジスター（形式度）の違い

「作る」を表す基本動詞 membuat と比べ、menyusun はより高度で知的な作業に使われます：
- **membuat kue / membuat kopi**: 物理的な調理・制作。
- **menyusun skripsi / menyusun anggaran**: 単に形を作るだけでなく、論理や構成を考えて「体系的に編纂・策定する」。

論文の執筆や公的書類の作成では、membuat laporan よりも **menyusun laporan** を用いることで、格調高いビジネス・学術レジスターを表現できます。""",
        "quiz": [
            {
                "q": "Frasa mana yang paling tepat untuk menyebut '式次第・イベントプログラム'?",
                "options": ["susunan acara", "penyusunan acara", "tersusun acara", "bersusun acara"],
                "ans": "susunan acara",
                "exp": "イベントの進行構成やプログラムは名詞句「susunan acara」と言います。"
            },
            {
                "q": "Kata yang tepat untuk orang yang mengompilasi atau mengedit kamus adalah...",
                "options": ["tersusun", "penyusun", "susunan", "menyusunkan"],
                "ans": "penyusun",
                "exp": "編纂者・執筆者を指す行為者名詞は「penyusun（語根 susun に接頭辞 peN-）」です。"
            },
            {
                "q": "Lengkapi kalimat: 'Kamus tebal ini ... dari ribuan halaman kata-kata pilihan.'",
                "options": ["menyusun", "tersusun", "susunan", "penyusunan"],
                "ans": "tersusun",
                "exp": "「〜から構成されている」という受け身・完了状態を表すには「tersusun dari...」を用います。"
            }
        ],
        "column": """### 語源コラム：祝祭の円錐形ご飯「トゥンペンの段重ね（Tumpeng Bersusun）」

ジャワの感謝祭（スラマタン）で欠かせない黄色い円錐形の祝祭飯「Tumpeng（トゥンペン）」。その頂点から裾野にかけて、鶏肉、エビ、卵焼き、野菜の和え物が幾重にも美しく取り囲む様子は「Lauk-pauk yang bersusun（段々に並んだおかず）」と表現されます。

天に向かって高くなる山型の盛り付けは、神聖なマハメル山への畏敬と、人間社会の調和のとれた階層秩序を象徴しています。「Susun」という言葉には、混沌とした世界を美しく秩序ある小宇宙へと組み立て直すという深い文化的感性が宿っているのです。"""
    },
    {
        "filename": "104-root-pecah.md",
        "title": "1354. 語根 pecah の全派生語図鑑（memecahkan, perpecahan, pecahan, terpecah）",
        "root": "pecah",
        "core_meaning": "割れる、砕ける、分裂する、解決する、新記録を破る",
        "explanation": "語根 pecah は、強固な結合が衝撃によって「粉々に砕け散る、亀裂が入る」という破壊的コアを持ちます。しかし抽象的な文脈では、「頭を悩ませる難問を打ち破って解決する（memecahkan masalah）」や「過去の記録を破る（memecahkan rekor）」というポジティブな突破のメタファーとしても極めて頻出します。",
        "matrix": [
            ("memecahkan", "meN- -kan", "他動詞", "割る、粉砕する、解決する、記録を破る", "Polisi berhasil memecahkan teka-teki pembunuhan berencana itu."),
            ("dipecahkan", "di- -kan", "受動態動詞", "割られる、解決される、打破される", "Rekor dunia lari 100 meter berhasil dipecahkan kemarin."),
            ("perpecahan", "per- -an", "名詞", "分裂、不和、内紛、国家解体", "Politik identitas berisiko memicu perpecahan bangsa."),
            ("pecahan", "-an", "名詞", "破片、断片、紙幣の金種、分数", "Uang saku saya berupa pecahan sepuluh ribu rupiah."),
            ("terpecah", "ter-", "状態動詞", "分裂してしまった、細分化された", "Pendapat masyarakat terpecah menjadi dua kubu yang berseberangan."),
            ("pemecahan", "peN- -an", "名詞", "解決、解明、分割・破砕作業", "Musyawarah adalah cara terbaik untuk pemecahan masalah bersama."),
            ("berpecah", "ber-", "自動詞", "分裂する、分かれる（berpecah belah）", "Kita tidak boleh berpecah belah menghadapi musuh bersama.")
        ],
        "details": [
            ("memecahkan", "他動詞", "ムムチャハカン",
             "物理的に物を割る動作のほか、難問を解く（solve）、記録を更新する（break record）際に使われます。",
             "memecahkan masalah（問題を解決する）, memecahkan rekor（記録を破る）, memecahkan kebuntuan（膠着状態を打開する）",
             "Para ilmuwan berusaha memecahkan misteri penyakit langka tersebut.",
             "科学者たちはその難病の謎を解明しようと努めている。"),
            ("perpecahan", "名詞", "プルプチャハン",
             "組織や国家が内部対立によってバラバラに分裂・不和になる状態を指す政治・社会用語です。",
             "mencegah perpecahan（分裂を防ぐ）, memicu perpecahan（内紛を引き起こす）, perpecahan internal（内部崩壊・内紛）",
             "Persatuan nasional harus dijaga agar terhindar dari perpecahan sipil.",
             "市民社会の内紛を避けるため、国民の結束は守られねばならない。"),
            ("pecahan", "名詞", "プチャハン",
             "割れたガラスや陶器の「破片」のほか、通貨の「金種（額面）」や算数の「分数」を指します。",
             "pecahan kaca（ガラスの破片）, uang pecahan kecil（小額紙幣・小銭）, pecahan desimal（小数・分数）",
             "Tolong siapkan uang tunai dalam pecahan lima puluh ribu rupiah.",
             "5万ルピア札の金種で現金を用意してください。"),
            ("terpecah", "形容詞・状態動詞", "トルプチャハ",
             "不本意に割れてしまった状態、あるいは意見や集団が「分かれて対立している」状態を表します。",
             "suara terpecah（票が割れる）, perhatian terpecah（集中力が散漫になる）, terpecah belah（バラバラに分裂する）",
             "Fokus atlet itu terpecah akibat kabar duka dari keluarganya.",
             "家族の訃報により、そのアスリートの集中力は途切れてしまった。")
        ],
        "dialogue": {
            "title": "ビジネス交渉における膠着状態の打開とチームの結束",
            "lines": [
                ("Hendra", "Negosiasi kontrak dengan mitra baru tampak mengalami kebuntuan berat."),
                ("Sari", "Benar, Pak. Kita harus segera mencari solusi kreatif untuk memecahkan masalah ini."),
                ("Hendra", "Jangan sampai perbedaan strategi ini justru memicu perpecahan di dalam tim kita sendiri."),
                ("Sari", "Tentu, Pak. Meskipun suara sempat terpecah, tim sepakat untuk tetap solid di meja perundingan.")
            ]
        },
        "grammar_point": """### 成句 memecahkan kebuntuan（膠着状態を打開する）の威力

語根 pecah を用いた高度な成句表現として必修なのが **memecahkan kebuntuan（ブレークスルー、膠着の打破）** です：
- **kebuntuan**: 語根 buntu（行き止まり・袋小路）の名詞化で「デッドロック、行き詰まり」。
- 行き止まりの壁を木っ端微塵に粉砕して（memecahkan）、前進する突破口を開くというダイナミックな比喩です。政治会談やビジネス交渉の報道で頻出します。""",
        "quiz": [
            {
                "q": "Apa arti dari frasa 'memecahkan rekor' dalam berita olahraga?",
                "options": ["Merusak piala kejuaraan", "Membatalkan perlombaan", "Memperbarui/memecahkan rekor terbaik sebelumnya", "Menolak bertanding di final"],
                "ans": "Memperbarui/memecahkan rekor terbaik sebelumnya",
                "exp": "memecahkan rekor は「過去の最高記録を塗り替える（break the record）」という意味です。"
            },
            {
                "q": "Kata mana yang tepat untuk melengkapi: 'Tolong tukarkan uang ini ke ... yang lebih kecil.'?",
                "options": ["pecahan", "perpecahan", "pemecahan", "memecahkan"],
                "ans": "pecahan",
                "exp": "紙幣の金種や額面は「pecahan uang（小額紙幣＝pecahan kecil）」と言います。"
            },
            {
                "q": "Frasa 'perpecahan bangsa' merujuk pada fenomena sosial berupa...",
                "options": ["Pertumbuhan ekonomi yang merata", "Disintegrasi atau perpecahan persatuan antarwarga negara", "Pembangunan infrastruktur perbatasan", "Pemberantasan korupsi secara tegas"],
                "ans": "Disintegrasi atau perpecahan persatuan antarwarga negara",
                "exp": "perpecahan bangsa は「国民の連帯の分裂・国家の解体危機（disintegrasi）」を意味します。"
            }
        ],
        "column": """### 語源コラム：国是「Bhinneka Tunggal Ika」と対極の「Berpecah Belah」

インドネシア国家の紋章ガルーダの足元に刻まれる国是「Bhinneka Tunggal Ika（多様性の中の統一）」。この聖なる統一の反対概念として、独立闘争期から歴代大統領が最も忌避してきたのが「Berpecah belah（分裂してバラバラになること）」です。

オランダ植民地政府の分断統治（Devide et Impera）によって島々が互いに争わされた痛烈な歴史的記憶から、「Bersatu kita teguh, bercerai kita runtuh（団結すれば我らは固く立ち、分裂すれば我らは崩れ去る）」という格言とともに、「Pecah」の破壊力に対する強い警戒が国民統合の根底に刻まれています。"""
    },
    {
        "filename": "105-root-ikat.md",
        "title": "1355. 語根 ikat の全派生語図鑑（mengikat, ikatan, perikatan, terikat）",
        "root": "ikat",
        "core_meaning": "縛る、結ぶ、連帯する、拘束する、契約する",
        "explanation": "語根 ikat は、紐や縄で物を「縛る・結びつける」という物理的動作から、人と人の情緒的「連帯・絆（ikatan）」、法的な「契約・拘束力（perikatan）」へと意味を展開します。伝統織物（Kain Ikat）から同窓会（ikatan alumni）、法務契約までを網羅する重要語根です。",
        "matrix": [
            ("mengikat", "meN-", "他動詞", "縛る、結ぶ、法的に拘束する、魅了する", "Perjanjian kerja sama ini mengikat kedua belah pihak secara hukum."),
            ("diikat", "di-", "受動態動詞", "縛られる、結ばれる、束ねられる", "Kayu bakar itu diikat dengan tali bambu yang kuat."),
            ("ikatan", "-an", "名詞", "結び目、絆、連帯、同窓会・同業者組合", "Ikatan batin antara ibu dan anak tidak dapat terpisahkan."),
            ("perikatan", "per- -an", "名詞 (法学用語)", "債権債務関係、契約関係 (Obligation/Commitment)", "Hukum perikatan perdata mengatur hak dan kewajiban para pihak."),
            ("terikat", "ter-", "形容詞・状態動詞", "縛られている、拘束された、専属の", "Saya tidak terikat kontrak dengan perusahaan mana pun saat ini."),
            ("keterikatan", "ke- -an", "名詞", "愛着、しがらみ、強い関与・エンゲージメント", "Keterikatan karyawan terhadap visi perusahaan sangat tinggi."),
            ("pengikat", "peN-", "名詞", "結ぶ具、結束バンド、接着剤、絆を強める要素", "Toleransi adalah tali pengikat persatuan di tengah kemajemukan.")
        ],
        "details": [
            ("mengikat", "他動詞", "ムンギカット",
             "紐で縛る動作のほか、契約が人を「法的に拘束する」、あるいは魅力が心を「惹きつける（mengikat hati）」際に使われます。",
             "mengikat tali sepatu（靴紐を結ぶ）, putusan yang mengikat（拘束力のある判決）, mengikat janji（誓いを結ぶ）",
             "Peraturan baru ini bersifat mengikat seluruh anggota asosiasi.",
             "この新規則は協会の全会員を法的に拘束する性質を持つ。"),
            ("ikatan", "名詞", "イカタン",
             "物理的な束（seikat bayam: ほうれん草1束）から、心の絆（ikatan batin）、公的な組織・連盟（Ikatan Dokter Indonesia）を指します。",
             "ikatan alumni（同窓会）, ikatan keluarga（家族の絆）, ikatan dinas（官公庁の服務義務契約）",
             "Ikatan Alumni Universitas Indonesia menggelar reuni akbar tahunan.",
             "インドネシア大学同窓会は年に一度の大規模同窓会を開催した。"),
            ("perikatan", "名詞", "プルイカタン",
             "民法上の債権・債務関係（rechtshandeling）を指す格調高い法律専門用語です。",
             "hukum perikatan（債権法・契約法）, perjanjian perikatan jual beli (PPJB)（不動産売買予約契約）",
             "Akta perikatan jual beli harus ditandatangani di hadapan notaris resmi.",
             "売買予約契約証書は公証人の面前で署名されなければならない。"),
            ("terikat", "形容詞・状態動詞", "トルイカット",
             "何かの義務、規則、契約に「縛られて自由がきかない」状態を表します。",
             "terikat waktu（時間に縛られる）, terikat aturan（規則に縛られる）, tidak terikat（フリーランス・無所属の）",
             "Sebagai pekerja lepas, dia tidak terikat jam kerja kantor yang kaku.",
             "フリーランスとして、彼はオフィスの堅苦しい勤務時間に縛られていない。")
        ],
        "dialogue": {
            "title": "不動産契約における拘束力と売買予約契約（PPJB）の手続き",
            "lines": [
                ("Rian", "Apakah draf perjanjian perikatan jual beli rumah ini sudah final, Bu Notaris?"),
                ("Notaris", "Sudah, Pak Rian. Seluruh klausul di dalamnya bersifat mengikat kedua belah pihak secara sah."),
                ("Rian", "Baik. Apakah setelah penandatanganan ini pembeli langsung terikat kewajiban pelunasan?"),
                ("Notaris", "Tepat sekali. Dokumen perikatan ini menjadi dasar hukum yang kuat sebelum akta jual beli resmi diterbitkan.")
            ]
        },
        "grammar_point": """### 助数詞としての ikat（束）

語根 ikat は、野菜や薪など「束ねられたもの」を数える助数詞（kata bantu bilangan）としても日常会話で頻出します：
- **seikat bayam**: ほうれん草1束
- **dua ikat kayu bakar**: 薪2束
- **seikat bunga**: 花束ひとつ

市場で買い物をするとき、「Beli bayam dua ikat, Bu!（お母さん、ほうれん草2束ちょうだい！）」のように自然に使われます。""",
        "quiz": [
            {
                "q": "Apa arti dari frasa 'putusan pengadilan yang bersifat mengikat'?",
                "options": [
                    "Putusan yang dibatalkan oleh hakim",
                    "Putusan hukum yang wajib dipatuhi oleh para pihak yang bersengketa",
                    "Putusan yang belum selesai ditulis",
                    "Putusan yang hanya berlaku untuk warga negara asing"
                ],
                "ans": "Putusan hukum yang wajib dipatuhi oleh para pihak yang bersengketa",
                "exp": "bersifat mengikat は「法的な拘束力を持つ（binding）」という意味です。"
            },
            {
                "q": "Organisasi profesi dokter resmi di Indonesia dinamakan...",
                "options": ["Ikatan Dokter Indonesia (IDI)", "Penyusun Dokter Nasional", "Perikatan Medis Jakarta", "Pengatur Dokter Praktik"],
                "ans": "Ikatan Dokter Indonesia (IDI)",
                "exp": "インドネシア医師会の公式名称は「Ikatan Dokter Indonesia（IDI）」です。"
            },
            {
                "q": "Kata yang tepat untuk mendeskripsikan pekerja bebas (freelancer) adalah...",
                "options": ["sangat terikat waktu kantor", "tidak terikat jam kerja tetap", "kehilangan ikatan keluarga", "pembuat perikatan sepihak"],
                "ans": "tidak terikat jam kerja tetap",
                "exp": "フリーランスの特徴は「固定の勤務時間に縛られない（tidak terikat jam kerja tetap）」ことです。"
            }
        ],
        "column": """### 語源コラム：世界を魅了する群島の伝統絣「テヌン・イカット（Tenun Ikat）」

「Ikat（結ぶ・括る）」という単語は、今や世界共通の服飾・美術用語（Ikat weave）として英語辞典にも採録されています。

東ヌサ・トゥンガラ（NTT）やスンバ島、カリマンタンに伝わる伝統織物「Kain Tenun Ikat」は、織り上げる前に糸の束を植物の紐で防染のために固く縛り結び（diikat）、天然染料に浸して幾何学模様を染め抜きます。何ヶ月もかけて糸を結び、染め、織り上げる気の遠くなるような手仕事は、部族の祖霊信仰や宇宙観を現代に結びつける神聖な祈りの結晶です。"""
    },
    {
        "filename": "106-root-lepas.md",
        "title": "1356. 語根 lepas の全派生語図鑑（melepaskan, pelepasan, terlepas, selepas）",
        "root": "lepas",
        "core_meaning": "放す、解き放つ、脱ぐ、免れる、〜の後に",
        "explanation": "語根 lepas は、束縛や接続から「自由になる、外れる、離脱する」というコアを持ちます。物理的に衣服を脱ぐ・手を放す動作から、ストレスや責任からの解放（melepaskan tanggung jawab）、何かが終わった直後の時間表現（selepas...）まで、日常・文学・論説に幅広く活用されます。",
        "matrix": [
            ("melepaskan", "meN- -kan", "他動詞", "放す、解き放つ、手放す、脱ぐ、発射する", "Petugas melepaskan burung langka sitaan ke habitat aslinya."),
            ("dilepaskan", "di- -kan", "受動態動詞", "放される、解放される、外される", "Tersangka dilepaskan karena kurangnya bukti yang sah."),
            ("pelepasan", "peN- -an", "名詞", "解放、釈放、送別式、売却・手放し", "Acara pelepasan wisudawan berlangsung secara khidmat di aula."),
            ("terlepas", "ter-", "形容詞・状態動詞", "外れた、解き放たれた、〜とは無関係に", "Kancing bajunya terlepas saat dia berdesakan di kereta."),
            ("berlepas", "ber-", "自動詞 (文語)", "出発する、出港する、責任を放棄する", "Kapal feri berlepas menuju Pelabuhan Bakauheni tepat waktu."),
            ("selepas", "se-", "接続詞・前置詞", "〜の直後に、〜が終わってから（setelah）", "Selepas lulus kuliah, dia langsung bekerja di perusahaan rintisan."),
            ("lepas tangan", "-", "成句", "無責任に手を引く、責任逃れをする", "Pimpinan proyek tidak boleh lepas tangan atas kegagalan teknis ini.")
        ],
        "details": [
            ("melepaskan", "他動詞", "ムルパスカン",
             "握っていた手を放す、衣服を脱ぐ、鳥や捕虜を解き放つ、ストレスを発散させる動作です。",
             "melepaskan lelah（疲れを癒す・休む）, melepaskan kesempatan（好機を逃す）, melepaskan jabatan（辞任する）",
             "Mereka duduk santai di pantai untuk melepaskan penat setelah sepekan bekerja.",
             "彼らは一週間の仕事の後、疲れを癒すためにビーチでゆったり座った。"),
            ("terlepas dari...", "前置詞句", "トルパス ダリ",
             "「〜に関わらず、〜とは別にして（regardless of）」という意味を表す論説文の必須構文です。",
             "terlepas dari kontroversi（論争に関わらず）, terlepas dari perbedaan pendapat（意見の相違は別として）",
             "Terlepas dari kekurangannya, film dokumenter ini menyajikan data yang sangat akurat.",
             "欠点はあるにせよ（欠点とは別にして）、このドキュメンタリー映画は極めて正確なデータを提示している。"),
            ("pelepasan", "名詞", "プルパサン",
             "野生動物の放獣（pelepasan satwa）、退職者や卒業生を送り出す式典（acara pelepasan）を指します。",
             "pelepasan saham（株式の売却・手放し）, pelepasan hak tanah（土地権利の放棄・譲渡）",
             "Upacara pelepasan kontingen atlet SEA Games dipimpin langsung oleh Menteri.",
             "東南アジア競技大会選手団の壮行・出発式は大臣によって直接主導された。"),
            ("selepas", "接続詞", "スルパス",
             "setelah や sesudah と同義の洗練された文語表現。「〜の直後に、〜を終えて」を意味します。",
             "selepas maghrib（日没礼拝の直後）, selepas pandemi（パンデミック終息後）",
             "Selepas menyelesaikan studi master di Tokyo, ia kembali membangun desanya.",
             "東京で修士課程を修了した後、彼は自らの村を発展させるため帰国した。")
        ],
        "dialogue": {
            "title": "保護された野生ウミガメの海への放流イベント",
            "lines": [
                ("Bima", "Kapan acara pelepasan anak penyu (tukik) ke laut akan dimulai, Pak?"),
                ("Rudi", "Selepas matahari terbenam sore nanti, saat ombak laut mulai tenang."),
                ("Bima", "Apakah kita boleh membantu melepaskan tukik tersebut secara langsung ke pantai?"),
                ("Rudi", "Tentu saja, tetapi pastikan tangan Anda bersih agar mereka terlepas dari ancaman bakteri berbahaya.")
            ]
        },
        "grammar_point": """### 成句 lepas tangan（責任逃れをする、知らぬ顔をする）

直訳すると「手を放す（hands off）」ですが、インドネシア語では**「当事者としての責任を放棄し、知らぬ存ぜぬを決め込む（menghindar dari tanggung jawab）」**という強い批判的ニュアンスを持ちます：
- 例: *Jangan lepas tangan begitu saja saat terjadi masalah!*（問題が起きたときにそうやって無責任に逃げるな！）
これと対比されるのが **turun tangan（自ら介入する、手を差し伸べる）** です。""",
        "quiz": [
            {
                "q": "Apa arti dari frasa 'terlepas dari perdebatan yang ada' dalam artikel opini?",
                "options": [
                    "Kalah dalam perdebatan",
                    "Terlepas/terbebas dari penjara",
                    "Terlepas dari/mengesampingkan perdebatan yang ada (regardless of the debate)",
                    "Memulai perdebatan baru yang sengit"
                ],
                "ans": "Terlepas dari/mengesampingkan perdebatan yang ada (regardless of the debate)",
                "exp": "terlepas dari... は「〜は別にして、〜に関わらず（regardless of）」という論説構文です。"
            },
            {
                "q": "Sinonim yang paling tepat untuk kata 'selepas' adalah...",
                "options": ["sebelum", "setelah", "selama", "sewaktu"],
                "ans": "setelah",
                "exp": "selepas は setelah（〜の後）と同義の洗練された時間接続詞です。"
            },
            {
                "q": "Sikap pemimpin yang menolak bertanggung jawab atas kesalahan anak buahnya disebut...",
                "options": ["turun tangan", "lepas tangan", "ringan tangan", "tangan kanan"],
                "ans": "lepas tangan",
                "exp": "責任を放棄して逃げる態度は「lepas tangan」と呼びます。"
            }
        ],
        "column": """### 語源コラム：夕暮れの解き放たれ「Selepas Senja」の詩情

インドネシア文学やポップソングで頻出する美しいフレーズが「Selepas Senja（黄昏の直後）」です。

熱帯の一日は、昼間の燃えるような酷暑から、夕暮れ（Senja）のスコールを経て、涼やかな夜へと一変します。太陽の熱気から大地が「解き放たれる（lepas）」この時間帯は、人々が屋台に集い、温かいコーヒーを飲みながら語り合う最も人間味豊かな黄昏時です。「Lepas」という言葉には、息苦しい日常の重荷からフッと心が軽くなるカタルシスの余韻が込められています。"""
    },
    {
        "filename": "107-root-pasang.md",
        "title": "1357. 語根 pasang の全派生語図鑑（memasang, pemasangan, pasangan, terpasang）",
        "root": "pasang",
        "core_meaning": "取り付ける、設置する、ペアー（対）、満潮、賭ける",
        "explanation": "語根 pasang は、部品や機器を所定の位置に「取り付ける・セットする」という動作と、二つで一つを成す「ペアー・夫婦・カップル（pasangan）」、そして潮が満ちる「満潮（air pasang）」という多彩な意味領域を持ちます。設備工事（pemasangan）から人生の伴侶（pasangan hidup）まで、多角的な表現をカバーします。",
        "matrix": [
            ("memasang", "meN-", "他動詞", "取り付ける、設置する、広告を出す、身につける", "Teknisi sedang memasang panel surya di atap rumah."),
            ("dipasang", "di-", "受動態動詞", "設置される、取り付けられる、掲示される", "Spanduk sosialisasi pemilu dipasang di perempatan jalan."),
            ("pasangan", "-an", "名詞", "ペアー、カップル、夫婦、伴侶、対になるもの", "Pasangan suami istri itu baru saja merayakan ulang tahun pernikahan perak."),
            ("pemasangan", "peN- -an", "名詞", "設置工事、取り付け作業、装着プロセス", "Pemasangan jaringan pipa gas membutuhkan ketelitian tinggi."),
            ("berpasangan", "ber-", "自動詞・形容詞", "ペアーになっている、ペアを組む", "Para penari tampil berpasangan dengan mengenakan busana adat."),
            ("terpasang", "ter-", "状態動詞", "すでに取り付けられている、装着済みである", "Kamera CCTV telah terpasang di setiap sudut gedung."),
            ("pasang surut", "-", "複合名詞", "潮の満ち引き、栄枯盛衰、人生の浮き沈み", "Mereka telah melewati berbagai pasang surut dalam berbisnis.")
        ],
        "details": [
            ("memasang", "他動詞", "ムマサン",
             "機械・器具の設置、看板の掲示、広告の出稿、時計のアラーム設定などに幅広く使われます。",
             "memasang iklan（広告を出す）, memasang target（目標を設定する）, memasang telinga（耳をそばだてる）",
             "Pemerintah memasang rambu-rambu peringatan bahaya longsor di lereng bukit.",
             "政府は丘の斜面に地滑り危険警告標識を設置した。"),
            ("pasangan", "名詞", "パサンガン",
             "靴や手袋の「一組（sepasang sepatu）」から、恋人・配偶者（pasangan hidup）、ペアを指します。",
             "pasangan hidup（人生の伴侶）, sepasang merpati（つがいの鳩）, pasangan calon (paslon)（候補者ペア）",
             "Setiap manusia mendambakan pasangan hidup yang pengertian dan setia.",
             "すべての人間は理解力があり誠実な人生の伴侶を切望している。"),
            ("pemasangan", "名詞", "プマサンガン",
             "設備や部品を取り付ける工事・設置作業のプロセスそのものを指します。",
             "biaya pemasangan（設置工事費）, proses pemasangan（取り付け工程）, pemasangan behel（歯列矯正器具の装着）",
             "Biaya pemasangan sambungan listrik baru telah ditetapkan secara resmi.",
             "新規電力接続の設置工事費は公式に定められている。"),
            ("terpasang", "形容詞・状態動詞", "トルパサン",
             "機器や部品がすでにしっかりと「据え付けられている・作動可能な状態にある」完了状態を表します。",
             "sudah terpasang（すでに設置済みである）, belum terpasang（未設置である）",
             "Sensor gempa bumi sudah terpasang di sepanjang pesisir rawan tsunami.",
             "津波危険沿岸に沿って地震センサーがすでに設置されている。")
        ],
        "dialogue": {
            "title": "新築住宅における太陽光発電パネルの設置工事",
            "lines": [
                ("Agus", "Kapan teknisi akan mulai memasang panel surya di rumah kita?"),
                ("Sari", "Rencananya besok pagi. Seluruh unit peralatan sudah tiba dan siap untuk proses pemasangan."),
                ("Agus", "Baguslah. Berapa lama waktu yang dibutuhkan sampai sistemnya terpasang sempurna?"),
                ("Sari", "Kata mandornya, pemasangan akan selesai dalam satu hari jika cuaca cerah.")
            ]
        },
        "grammar_point": """### 助数詞としての sepasang（一対、1ペア、一組）

2つでセットになっているものを数えるとき、助数詞 **sepasang** を用います：
- **sepasang sepatu**: 一足の靴
- **sepasang anting-anting**: 一対のイヤリング
- **sepasang kekasih**: 一組の恋人同士

また選挙報道で頻出する **Paslon (Pasangan Calon)** は、「大統領・副大統領候補ペア」や「知事・副知事候補ペア」を指す最重要の現代略語です。""",
        "quiz": [
            {
                "q": "Apa arti dari akronim politik 'Paslon' yang sering muncul saat pemilu?",
                "options": ["Pasukan Lapangan", "Pasangan Calon", "Pasar Lokal Online", "Paspor Elektronik"],
                "ans": "Pasangan Calon",
                "exp": "Paslon は Pasangan Calon（正副候補者ペア）の公的略語です。"
            },
            {
                "q": "Kata bantu bilangan yang tepat untuk menyebut '一足の靴' adalah...",
                "options": ["seikat sepatu", "sepasang sepatu", "sebuah sepatu", "sepotong sepatu"],
                "ans": "sepasang sepatu",
                "exp": "対（ペア）になっている靴は「sepasang sepatu」と数えます。"
            },
            {
                "q": "Ungkapan 'pasang surut kehidupan' memiliki makna yang sama dengan...",
                "options": ["kematian yang tenang", "dinamika suka duka dan jatuh bangun kehidupan", "perjalanan liburan ke laut", "pembelian rumah baru"],
                "ans": "dinamika suka duka dan jatuh bangun kehidupan",
                "exp": "潮の満ち引き（pasang surut）は人生の栄枯盛衰・浮き沈み（suka duka）を象徴します。"
            }
        ],
        "column": """### 語源コラム：海の呼吸「Air Pasang」と高潮浸水「Banjir Rob」

海洋国家インドネシアの沿岸部では、語根 pasang は海の潮位と直結しています。「Air pasang」は「満潮」を指し、「Air surut」は「引き潮」を指します。

近年、気候変動による海面上昇と地盤沈下が重なり、満潮時に海水が堤防を越えて市街地へ逆流する高潮浸水が深刻化しています。この現象は現地で「Banjir Rob（ロブ洪水）」と呼ばれ、「Saat air pasang laut naik（高潮の満潮時）」に日常茶飯事の冠水が発生します。自然の潮汐の語根が、現代の都市環境問題の現場で生々しく息づいています。"""
    },
    {
        "filename": "108-root-ganti.md",
        "title": "1358. 語根 ganti の全派生語図鑑（mengganti, berganti, pergantian, pengganti）",
        "root": "ganti",
        "core_meaning": "代わる、替える、交替する、取り替える、代償・補償する",
        "explanation": "語根 ganti は、古いものを取り去って新しいものを「置き換える・交替する・代償を支払う」というコアを持ちます。衣服の着替え（ganti baju）からリーダーの世代交代（pergantian generasi）、部品交換（mengganti suku cadang）、損害賠償（ganti rugi）まで、循環と更新を表現する必須語根です。",
        "matrix": [
            ("mengganti", "meN-", "他動詞", "取り替える、交換する、弁償する、代行する", "Mekanik mengganti oli mesin mobil yang sudah kotor."),
            ("diganti", "di-", "受動態動詞", "交換される、交代させられる、補償される", "Ban sepeda yang bocor ini harus segera diganti."),
            ("berganti", "ber-", "自動詞", "交替する、切り替わる、移り変わる", "Musim kemarau kini telah berganti menjadi musim hujan."),
            ("pergantian", "per- -an", "名詞", "交代、変遷、切り替え、交代期", "Pergantian tahun baru dirayakan dengan pesta kembang api."),
            ("pengganti", "peN-", "名詞", "後継者、代用品、代理役、スペア", "Perusahaan sedang mencari pengganti direktur yang pensiun."),
            ("penggantian", "peN- -an", "名詞", "交換作業、払い戻し・弁済手続き", "Penggantian biaya medis akan diproses oleh pihak asuransi."),
            ("ganti rugi", "-", "複合語", "損害賠償、補償金", "Pihak maskapai memberikan uang ganti rugi atas kehilangan bagasi.")
        ],
        "details": [
            ("mengganti", "他動詞", "ムンガンティ",
             "消耗品や故障品を新しいものに取り替える、あるいは他人の損失を弁償・補填する動作です。",
             "mengganti rugi（損害を弁償する）, mengganti suku cadang（部品を交換する）, mengganti rugi waktu（時間を埋め合わせる）",
             "Pemerintah berjanji akan mengganti tanah warga yang terkena proyek jalan tol.",
             "政府は高速道路プロジェクトの対象となった住民の土地を補償すると約束した。"),
            ("berganti", "自動詞", "ブルガンティ",
             "主語自身が別の状態やものへ自然に「移り変わる、順繰りに交代する」動作です。",
             "berganti pakaian（服を着替える）, berganti musim（季節が移り変わる）, berganti kepemimpinan（指導者が交代する）",
             "Waktu cepat berlalu dan tahun terus berganti tanpa terasa.",
             "時は瞬く間に過ぎ去り、気づかぬうちに年は移り変わっていく。"),
            ("pergantian", "名詞", "プルガンティアン",
             "指導者や体制、シフト、季節が入れ替わる「交代の時期・移行プロセスそのもの」を指します。",
             "pergantian shift（シフト交代）, pergantian zaman（時代の変遷）, pergantian menteri (reshuffle)（内閣改造）",
             "Pergantian kurikulum pendidikan menuai beragam reaksi dari para guru.",
             "教育カリキュラムの変更・刷新は教師たちから多様な反応を呼んだ。"),
            ("pengganti", "名詞", "プンガンティ",
             "退任した人の後を継ぐ「後任者・代役」、または欠けたものの代わりとなる「代用品」を指します。",
             "ban pengganti（スペアタイヤ）, pemain pengganti（控え選手・交代要員）, pengganti gula（人工甘味料・砂糖代替物）",
             "Pelatih memasukkan pemain pengganti pada sepuluh menit terakhir pertandingan.",
             "監督は試合の残り10分で交代要員の選手を投入した。")
        ],
        "dialogue": {
            "title": "オフィスのプリンター故障と部品交換・費用精算",
            "lines": [
                ("Tono", "Printer di ruang administrasi rusak lagi, tampaknya komponen printernya harus diganti."),
                ("Dewi", "Iya, teknisi sudah memeriksa dan menyarankan penggantian suku cadang utama."),
                ("Tono", "Apakah perusahaan akan mengganti biaya perbaikan jika saya bayar terlebih dahulu?"),
                ("Dewi", "Tentu, simpan kuitansinya untuk proses reimbursement atau penggantian biaya di bagian keuangan.")
            ]
        },
        "grammar_point": """### 成句 ganti rugi（損害賠償・補償）の構造

法務・保険・日常トラブルで頻出する **ganti rugi** は、「損失（rugi）を埋め合わせる（ganti）」という直感的な複合語です：
- **uang ganti rugi**: 損害賠償金、補償金
- **tuntutan ganti rugi**: 損害賠償請求
- **mengganti rugi**: 損害を補償する（他動詞句）

事故や納期遅延で「Saya siap mengganti rugi（私が損害を弁償します）」と言えることは、実務会話において極めて重要です。""",
        "quiz": [
            {
                "q": "Kata mana yang paling tepat untuk menyebut 'スペアタイヤ（予備のタイヤ）'?",
                "options": ["ban pergantian", "ban pengganti", "ban berganti", "ban ganti rugi"],
                "ans": "ban pengganti",
                "exp": "代用品・代替のものを指す名詞は「pengganti」です（ban pengganti / ban serep）。"
            },
            {
                "q": "Lengkapi kalimat: 'Setelah seharian bekerja di luar, ayah segera masuk kamar untuk ... pakaian.'",
                "options": ["menggantikan", "berganti", "pergantian", "pengganti"],
                "ans": "berganti",
                "exp": "「服を着替える」という再帰的動作は「berganti pakaian（または ganti baju）」と言います。"
            },
            {
                "q": "Apa arti dari 'uang ganti rugi' yang diberikan maskapai penerbangan?",
                "options": ["Tiket pesawat baru yang lebih mahal", "Kompensasi finansial atas kerugian atau keterlambatan", "Biaya sewa pesawat pribadi", "Hadiah undian bagi penumpang setia"],
                "ans": "Kompensasi finansial atas kerugian atau keterlambatan",
                "exp": "uang ganti rugi は遅延やロストバゲージに対する「金銭的補償（コンペンセーション）」を意味します。"
            }
        ],
        "column": """### 語源コラム：夜警の拍子木と交代番「Gantian（交代でやろう）」

インドネシアの住宅街で夜間警備を行う自警団「Ronda Malam」。住民の男性たちが持ち回りで夜警を担当する際によく交わされる言葉が「Ayo, gantian!（さあ、交代しよう！）」です。

語根 ganti に接尾辞 -an が付いた口語形 **gantian** は、「順番交替で」「代わりばんこに」という意味の超頻出フレーズです。子どものブランコ遊びから大人の当番業務まで、「Gantian ya!」とお互いに譲り合う精神は、相互扶助（Gotong Royong）の温かい潤滑油となっています。"""
    },
    {
        "filename": "109-root-ubah.md",
        "title": "1359. 語根 ubah の全派生語図鑑（mengubah, diubah, berubah, perubahan）",
        "root": "ubah",
        "core_meaning": "変わる、変える、改変する、修正する、転換する",
        "explanation": "語根 ubah は、物事の形態、性質、方針、状態が従前のものから「変化する、変更する」というコアを持ちます。社会の激動（perubahan sosial）からデジタル変革（mengubah cara hidup）、心変わり（berubah pikiran）まで、あらゆる動的プロセスの中核をなす語根です。",
        "matrix": [
            ("mengubah", "meN-", "他動詞", "変える、変更する、改変・修正する", "Teknologi digital telah mengubah cara manusia berkomunikasi."),
            ("diubah", "di-", "受動態動詞", "変更される、改訂される、変えられる", "Jadwal penerbangan terpaksa diubah akibat cuaca buruk."),
            ("berubah", "ber-", "自動詞", "変わる、変化する、変質する", "Sikapnya berubah menjadi sangat ramah setelah berdialog."),
            ("perubahan", "per- -an", "名詞", "変化、変革、変更点、推移", "Perubahan iklim global memicu bencana kekeringan di banyak negara."),
            ("pengubahan", "peN- -an", "名詞", "改変作業、修正行為、変更プロセス", "Pengubahan data kependudukan harus melampirkan surat pengantar."),
            ("terubah", "ter-", "状態動詞", "変更できる（terubahkan）、思わず変わってしまった", "Keputusannya sudah bulat dan tak terubahkan lagi."),
            ("peubah", "peN-", "名詞 (数学・統計)", "変数 (Variable)", "Peneliti menganalisis hubungan antar-peubah bebas dan terikat.")
        ],
        "details": [
            ("mengubah", "他動詞", "ムングバハ",
             "主語が何らかの対象を能動的に別の状態へ作り変える・変更する動作です。",
             "mengubah rencana（計画を変更する）, mengubah dunia（世界を変える）, mengubah pola pikir（マインドセットを変革する）",
             "Pendidikan adalah senjata paling ampuh untuk mengubah nasib keluarga.",
             "教育は家族の運命を変えるための最も強力な武器である。"),
            ("berubah", "自動詞", "ブルバハ",
             "他者からの外力ではなく、主語自身が自発的・自然に「別の状態へと変わる」動作です。",
             "berubah pikiran（気が変わる・考えを改める）, berubah wujud（姿を変える）, tidak pernah berubah（決して変わらない）",
             "Dunia terus berubah dengan sangat cepat seiring kemajuan kecerdasan buatan.",
             "世界は人工知能の進歩に伴い極めて急速に変化し続けている。"),
            ("perubahan", "名詞", "プルバハン",
             "ある状態から別の状態への「移行、変革、差分」という現象そのものを指す名詞です。",
             "perubahan iklim（気候変動）, agen perubahan（変革の担い手・チェンジエージェント）, perubahan signifikan（顕著な変化）",
             "Generasi muda diharapkan menjadi pelopor perubahan sosial yang berkeadilan.",
             "若者世代は公正な社会変革の先駆者となることが期待されている。"),
            ("tak terubahkan", "形容詞句", "タック トルバハカン",
             "ter- + 語根 + -kan に否定の tak/tidak が付いた表現で、「もはや覆すことができない、不変の」を意味します。",
             "takdir yang tak terubahkan（不可逆の運命）, hukum alam yang tak terubahkan（不変の自然法則）",
             "Keputusan vonis hakim Mahkamah Agung bersifat final dan tak terubahkan lagi.",
             "最高裁判所判事の判決は最終的なものであり、もはや覆すことはできない。")
        ],
        "dialogue": {
            "title": "デジタルトランスフォーメーション（DX）と企業風土の変革",
            "lines": [
                ("Bambang", "Bagaimana proses digitalisasi mengubah sistem kerja di kantor cabang kita?"),
                ("Lestari", "Perubahannya sangat drastis, Pak. Sistem manual yang lambat kini diubah menjadi serba otomatis."),
                ("Bambang", "Apakah para karyawan senior sempat menolak ketika pola kerja mereka berubah?"),
                ("Lestari", "Awalnya ada resistensi, tetapi setelah pelatihan rutin, pola pikir mereka berubah menjadi sangat adaptif.")
            ]
        },
        "grammar_point": """### mengubah（他動詞）vs berubah（自動詞）の対比

初中級者が最も混同しやすいペアです：
- **mengubah**（他動詞）：目的語（何を変えるのか）を後ろに取ります。
  - 例: *Dia **mengubah** warna rambutnya.*（彼女は髪の色を変えた。）
- **berubah**（自動詞）：目的語を取らず、主語自身が変化します。
  - 例: *Warna rambutnya **berubah** menjadi pirang.*（彼女の髪の色が金色に変わった。）

「気候が変動する」は *Iklim berubah* であり、環境破壊が「気候を変えてしまう」は *Aktivitas manusia mengubah iklim* となります。""",
        "quiz": [
            {
                "q": "Manakah kalimat yang menggunakan kata 'berubah' secara tepat?",
                "options": [
                    "Pemerintah sedang berubah undang-undang perpajakan.",
                    "Cuaca di pegunungan bisa berubah sewaktu-waktu tanpa peringatan.",
                    "Teknologi baru berhasil berubah gaya hidup masyarakat.",
                    "Tolong berubah kata sandi email Anda sekarang."
                ],
                "ans": "Cuaca di pegunungan bisa berubah sewaktu-waktu tanpa peringatan.",
                "exp": "天候が自然に変化するという自動詞文脈では berubah が正解です。"
            },
            {
                "q": "Istilah resmi dalam bahasa Indonesia untuk 'Climate Change' adalah...",
                "options": ["Pengubahan Iklim", "Perubahan Iklim", "Berubah Iklim", "Ubah Iklim"],
                "ans": "Perubahan Iklim",
                "exp": "「気候変動」の公的用語は名詞化された「Perubahan Iklim」です。"
            },
            {
                "q": "Apa arti dari ungkapan 'berubah pikiran'?",
                "options": ["Mengalami gangguan ingatan", "Mengganti keputusan atau pendapat sebelumnya", "Belajar ilmu filsafat baru", "Marah besar tanpa alasan"],
                "ans": "Mengganti keputusan atau pendapat sebelumnya",
                "exp": "berubah pikiran は「気が変わる、以前の決定・考えを変更する」という意味です。"
            }
        ],
        "column": """### 語源コラム：初代大統領スカルノの叫び「Agen Perubahan（変革の使徒）」

インドネシアの近現代史において、「Perubahan（変革）」は青年の特権と義務を象徴する言葉です。

建国の父スカルノは「1,000人の老人を与えてくれれば山を動かしてみせる。だが、10人の青年を与えてくれれば世界を揺るがしてみせる（Beri aku 1.000 orang tua, niscaya akan kucabut semeru dari akarnya. Beri aku 10 pemuda niscaya akan kuguncangkan dunia）」と叫びました。学生運動や民主化（Reformasi 1998）の歴史においても、若者たちは自らを常に社会を変革する「Agen Perubahan（チェンジエージェント）」と位置づけ、歴史の舵を動かしてきました。"""
    },
    {
        "filename": "110-root-pindah.md",
        "title": "1360. 語根 pindah の全派生語図鑑（memindahkan, berpindah, perpindahan, pemindahan）",
        "root": "pindah",
        "core_meaning": "移る、引っ越す、移転する、移動させる、転勤・転校する",
        "explanation": "語根 pindah は、ある場所・位置から別の場所へ「移動する、移住する、場所を変える」という空間的推移のコアを持ちます。日常の引っ越し（pindah rumah）から、国家的大事業である首都移転（pemindahan ibu kota）、熱の移動（perpindahan panas）まで、あらゆる移動現象を描写します。",
        "matrix": [
            ("memindahkan", "meN- -kan", "他動詞", "移動させる、移す、転送する、移転させる", "Petugas memindahkan kotak suara ke kantor kecamatan."),
            ("dipindahkan", "di- -kan", "受動態動詞", "移動される、転勤させられる、移設される", "Pasien darurat dipindahkan ke rumah sakit rujukan provinsi."),
            ("berpindah", "ber-", "自動詞", "移る、引っ越す、移動する、移住する", "Keluarga kami berpindah dari Surabaya ke Yogyakarta tahun lalu."),
            ("perpindahan", "per- -an", "名詞", "移動、移住、推移、移転現象", "Perpindahan penduduk dari desa ke kota memicu urbanisasi."),
            ("pemindahan", "peN- -an", "名詞", "移転作業、撤去プロセス、移設作業", "Rencana pemindahan ibu kota negara ke IKN terus berjalan."),
            ("kepindahan", "ke- -an", "名詞", "引っ越し、転勤、転校の事実", "Surat keterangan kepindahan diperlukan untuk mendaftar sekolah baru."),
            ("berpindah tangan", "-", "成句", "（所有権が）人手に渡る、所有者が変わる", "Lukisan bersejarah itu telah berpindah tangan beberapa kali.")
        ],
        "details": [
            ("memindahkan", "他動詞", "ムミンダーカン",
             "物を別の場所へ動かす、または人を別の部署・勤務先へ異動させる使役動作です。",
             "memindahkan file（ファイルを移動する）, memindahkan dana（資金を振り替える）, memindahkan narapidana（囚人を移送する）",
             "Silakan memindahkan saldo tabungan ke rekening giro Anda.",
             "預金残高を当座預金口座へ振り替えてください。"),
            ("berpindah", "自動詞", "ブルピンダー",
             "主語自身が住居、場所、所属を別の所へ変える動作です。",
             "berpindah rumah（引っ越す）, berpindah kerja（転職する）, berpindah-pindah（転々とする）",
             "Suku nomaden hidup dengan cara berpindah-pindah tempat mengikuti sumber air.",
             "遊牧民は水源に従って場所を転々と移動しながら暮らしている。"),
            ("pemindahan", "名詞", "プミンダーハン",
             "首都移転や設備移転など、能動的に対象を移す「移転事業・行政プロセス」を指します。",
             "pemindahan ibu kota（首都移転）, pemindahan makam（墓地の移設）, pemindahan tahanan（身柄移送）",
             "Pemindahan kantor pusat bank nasional itu memakan waktu enam bulan.",
             "その国立銀行本店の移転作業には6ヶ月の時間を要した。"),
            ("perpindahan", "名詞", "プルピンダーハン",
             "人口移動や熱伝導など、空間的にものが移動・推移する「現象そのもの」を指す学術・社会用語です。",
             "perpindahan penduduk（人口移動・移住）, perpindahan panas（熱移動・熱伝導）, perpindahan kekuasaan（権力の移行）",
             "Perpindahan panas secara konveksi terjadi pada zat cair dan gas.",
             "対流による熱移動は液体および気体において発生する。")
        ],
        "dialogue": {
            "title": "新首都ヌサンタラ（IKN）への公務員移転計画",
            "lines": [
                ("Fajar", "Bagaimana perkembangan rencana pemindahan kementerian kita ke Ibu Kota Nusantara?"),
                ("Siti", "Tahap pertama pemindahan aparatur sipil negara dijadwalkan mulai pertengahan tahun ini."),
                ("Fajar", "Apakah seluruh staf kementerian wajib berpindah tugas ke sana secara serentak?"),
                ("Siti", "Tidak serentak, Pak. Perpindahan dilakukan secara bertahap dengan memprioritaskan unit-unit strategis.")
            ]
        },
        "grammar_point": """### pemindahan（移転作業）vs perpindahan（移動現象）の違い

ここでも接辞 `peN- -an` と `per- -an` の対比が鮮明に現れます：
- **pemindahan**: 首都を移転したり、囚人を移送したりする**「人為的な移設・移転行為」**（Action/Process）。
  - 例: *pemindahan ibu kota*（首都移転作業）
- **perpindahan**: 人口の移動や季節労働、物理現象としての移動など**「推移・移動という現象そのもの」**（Phenomenon）。
  - 例: *perpindahan penduduk*（人口移動）, *perpindahan panas*（熱移動）""",
        "quiz": [
            {
                "q": "Frasa yang tepat untuk merujuk pada mega-proyek '首都移転' adalah...",
                "options": ["perpindahan ibu kota", "pemindahan ibu kota", "berpindah ibu kota", "kepindahan ibu kota"],
                "ans": "pemindahan ibu kota",
                "exp": "政府が人為的に首都を移転するプロジェクトは「pemindahan ibu kota」と呼びます。"
            },
            {
                "q": "Lengkapi kalimat: 'Keluarga pengungsi itu terpaksa ... tempat tinggal akibat bencana banjir bandang.'",
                "options": ["memindahkan", "berpindah", "pemindahan", "perpindahan"],
                "ans": "berpindah",
                "exp": "主語自身が住まいを移動する自動詞用法なので「berpindah tempat tinggal」が正解です。"
            },
            {
                "q": "Apa arti dari ungkapan 'tanah warisan itu telah berpindah tangan'?",
                "options": [
                    "Tanahnya terbawa longsor",
                    "Kepemilikan tanah tersebut telah beralih/dijual ke orang lain",
                    "Tanahnya dijadikan jalan raya",
                    "Sertifikat tanahnya hilang di jalan"
                ],
                "ans": "Kepemilikan tanah tersebut telah beralih/dijual ke orang lain",
                "exp": "berpindah tangan は「（所有権などが）別の人手に渡る、所有者が変わる」という意味の成句です。"
            }
        ],
        "column": """### 語源コラム：オランダ植民地時代から続く国家移住政策「Transmigrasi」

インドネシアで「Pindah（移る）」という言葉を語る上で避けて通れない歴史的大事業が「Transmigrasi（国内移住政策）」です。

ジャワ島・バリ島・マドゥラ島に偏重した過密人口を、土地の余るスマトラ島やカリマンタン島、スラウェシ島、パプア島へと組織的に移住させる国家政策は、植民地時代の「Kolonisatie」からスハルト政権下まで数十年にわたって強力に推進されました。移住した家族（Transmigran）は新天地で原生林を開墾し、ゴムやアブラヤシ農園を切り拓いてきました。「Pindah」という語根の背後には、国土の均衡ある開発と民族混交の壮大な開拓史が刻まれています。"""
    }
]

def generate_markdown(a):
    md = []
    md.append(f"# {a['title']}\n")
    md.append(f'<span class="badge badge-derivations">語根派生語</span> <span class="badge badge-vocabulary">語彙拡張</span> <span class="badge badge-intermediate">中級文法</span>\n')
    md.append(f"- **対象語根**: `{a['root']}`")
    md.append(f"- **コアの意味**: {a['core_meaning']}")
    md.append(f"- **CEFRレベル**: A2-B2 (初中級〜中上級)")
    md.append(f"- **読了目安**: 12分\n")
    md.append("---\n")
    
    md.append("## 語根のコアミーニングと概念展開\n")
    md.append(f"{a['explanation']}\n")
    
    md.append("## 派生語一覧マトリックス\n")
    md.append("| 派生語 | 接辞パターン | 品詞 | 日本語義 | 基本例文 |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for word, aff, pos, meaning, ex in a["matrix"]:
        md.append(f"| **{word}** | `{aff}` | {pos} | {meaning} | {ex} |")
    md.append("\n")
    
    md.append("## 主要派生語の精密解説と例文カード\n")
    for word, pos, kana, desc, coloc, id_ex, ja_ex in a["details"]:
        md.append(f"### {word}（{pos}）\n")
        md.append(f"**カタカナ発音**: {kana}  \n")
        md.append(f"**語法とニュアンス**: {desc}  \n")
        md.append(f"**重要コロケーション**: `{coloc}`\n")
        md.append(f'<div class="id-example">\n')
        md.append(f"**インドネシア語例文**: {id_ex}  \n")
        md.append(f"**日本語訳**: {ja_ex}\n")
        md.append("</div>\n")
    
    md.append("## 実践会話ダイアログ（Dialogue）\n")
    md.append(f"**シチュエーション**: {a['dialogue']['title']}\n")
    md.append('<div class="dialogue-box">\n')
    for speaker, line in a["dialogue"]["lines"]:
        md.append(f"**{speaker}**: \"{line}\"  \n")
    md.append("</div>\n")
    
    md.append("## 接辞の使い分け・文法比較のポイント\n")
    md.append(f"{a['grammar_point']}\n")
    
    md.append("## 定着確認チェッククイズ（3問）\n")
    for i, q in enumerate(a["quiz"], 1):
        md.append(f"**Q{i}. {q['q']}**\n")
        for opt in q["options"]:
            md.append(f"- {opt}")
        md.append("\n")
        md.append(f'<details>\n<summary>正解と解説を見る</summary>\n<div class="answer-box">\n')
        md.append(f"**正解**: 「**{q['ans']}**」\n")
        md.append(f"**解説**: {q['exp']}\n")
        md.append("</div>\n</details>\n")
    
    md.append("## 語源・文化コラム\n")
    md.append(f"{a['column']}\n")
    
    md.append("---\n")
    md.append("## 次の学習ステップ・関連リンク\n")
    md.append("- [総合サイトマップ](../sitemap.md)")
    md.append("- [トップページ](../index.md)\n")
    
    return "\n".join(md)

def main():
    target_dir = os.path.join("docs", "derivations-2")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        fpath = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {fpath}")

if __name__ == "__main__":
    main()
