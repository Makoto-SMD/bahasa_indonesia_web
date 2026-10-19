# -*- coding: utf-8 -*-
"""
Batch generation script for Section 31: Collocations Batch 4 (Articles 1281-1290)
Directory: docs/lexicon/
"""

import os

articles = [
    {
        "filename": "docs/lexicon/31-politics-collocations-election.md",
        "title": "【共起連語】政治時事・選挙の必須コロケーション辞典：pemilihan umum / perolehan suara / hak pilih",
        "root": "pemilu",
        "meaning": "選挙、民主的投票、民意の集計、政治キャンペーン",
        "core_concept": "世界第3位の民主主義国家インドネシアの政治生命線である「選挙（Pemilihan Umum / Pemilu）」において、投票権、得票率、大規模集会、投票箱など、選挙報道や政治対話で必須となる共起表現を体系化します。",
        "table_rows": [
            ("pemilihan umum (pemilu)", "一般的な選択", "総選挙、大統領・議会選挙、国民投票", "政治/国制", "Indonesia sukses menyelenggarakan pemilihan umum serentak terbesar di dunia secara damai."),
            ("perolehan suara", "声の獲得", "得票数、得票率、票の獲得状況", "報道/統計", "Berdasarkan hasil hitung cepat, pasangan calon nomor urut dua memimpin perolehan suara."),
            ("hak pilih", "選ぶ権利", "選挙権、投票権、参政権", "憲法/市民権", "Setiap warga negara yang telah berusia tujuh belas tahun berhak menggunakan hak pilihnya."),
            ("kampanye akbar", "壮大なキャンペーン", "大規模合同選挙集会、メガ集会、総決起集会", "選挙/大衆", "Ratusan ribu simpatisan memadati stadion utama untuk menghadiri kampanye akbar pasangan capres."),
            ("kotak suara", "声の箱", "投票箱（かつてはアルミ製、現在は強化紙製）", "選挙管理/実務", "Petugas KPU mendistribusikan kotak suara ke pulau-pulau terpencil menggunakan perahu tradisional."),
            ("politik uang", "お金の政治", "金権政治、票の買収、ばらまき選挙（money politics）", "批判/法執行", "Bawaslu berkomitmen menindak tegas segala bentuk politik uang selama masa tenang pemilu."),
            ("golongan putih (golput)", "白い集団", "棄権、白票、投票ボイコット層", "社会現象/政治", "Tingkat partisipasi pemilih meningkat signifikan seiring menurunnya persentase golput.")
        ],
        "details": [
            {
                "term": "perolehan suara (hasil rekapitulasi suara pemilu)",
                "trans": "得票数、得票率、票の獲得状況",
                "nuance": "開票速報（hitung cepat / quick count）や中央選挙管理委員会（KPU）の公式集計（rekapitulasi resmi）において、各候補者や政党が獲得した票の集計結果を指します。",
                "ex_id": "Komisi Pemilihan Umum (KPU) mengumumkan perolehan suara nasional pemilihan presiden secara transparan.",
                "ex_kana": "コミスィ プミリハン ウムム ムンウムムカン プロレハン スアラ ナシオナル プミリハン プレシデン スチャラ トランスパラン",
                "ex_ja": "中央選挙管理委員会（KPU）は、大統領選挙の全国得票集計（perolehan suara）を透明性をもって公表しました。",
                "note": "`memimpin perolehan suara`（得票数でリードする）と頻出します。"
            },
            {
                "term": "menggunakan hak pilih (mencoblos di TPS)",
                "trans": "選挙権（投票権）を行使する、投票所に足を運ぶ",
                "nuance": "市民が主権者として投票所（TPS）に向かい、投票用紙に釘で穴を開けて（mencoblos）自らの意思を表明する民主的権利の行使を指します。",
                "ex_id": "Pemerintah menetapkan hari pemungutan suara sebagai hari libur nasional agar warga leluasa menggunakan hak pilih.",
                "ex_kana": "プムリンター ムヌタップカン ハリ プムングタン スアラ スバガイ ハリ リブール ナシオナル アガル ワルガ レルアサ ムングナカン ハッ ピリフ",
                "ex_ja": "政府は市民が自由に選挙権を行使（menggunakan hak pilih）できるよう、投票日を国民の祝日に指定しました。",
                "note": "`kehilangan hak pilih`（選挙権を剥奪される）も法廷用語です。"
            },
            {
                "term": "kampanye akbar (rapat umum terbuka pemilu)",
                "trans": "大規模総決起集会、メガ選挙ラリー",
                "nuance": "選挙戦終盤の法定キャンペーン期間（masa kampanye）に、スタジアムや大広場に十数万人規模の支持者（massa simpatisan）を結集して党勢を誇示する巨大政治イベントです。",
                "ex_id": "Lalu lintas ibu kota dialihkan demi mengantisipasi kepadatan massa yang menghadiri kampanye akbar di Senayan.",
                "ex_kana": "ラル リンタス イブ コタ ディアンリカン デミ ムンガンティシパシ クパダタン マッサ ヤン ムンハディリ カンパニェ アクバール ディ スナヤン",
                "ex_ja": "スナヤンでの大規模総決起集会（kampanye akbar）に詰めかける群衆の混雑を想定し、首都の交通が迂回誘導されました。",
                "note": "アラビア語 `akbar`（偉大な・最大規模の）が冠されます。"
            },
            {
                "term": "politik uang (praktik bagi-bagi uang / serangan fajar)",
                "trans": "金権政治、票の買収、買収ばらまき",
                "nuance": "投票直前の夜明けに有権者へ現金を配って買収する「暁の急襲（serangan fajar）」など、公正な民主主義を歪める不正な金銭供与を指す政治・司法用語です。",
                "ex_id": "Pendidikan politik bagi generasi muda sangat penting untuk membendung godaan politik uang di akar rumput.",
                "ex_kana": "プンディディカン ポリティッ バギ ゲネラシ ムダ サンガット プンティン ウントゥッ ムンベンドゥン ゴダアン ポリティッ ウアン ディ アカル ルムプット",
                "ex_ja": "草の根での金権買収（politik uang）の誘惑を食い止めるため、若い世代に対する政治教育が極めて重要です。",
                "note": "選挙監視委員会（Bawaslu）の摘発対象です。"
            },
            {
                "term": "golongan putih / golput (absen memilih secara sadar)",
                "trans": "白票、棄権、意図的投票ボイコット",
                "nuance": "1971年にスハルト独裁体制の不公正な選挙に抗議して若者や知識人が提唱した歴史的社会運動に由来し、現代でも既成政党に失望して棄権する層を指します。",
                "ex_id": "Tokoh lintas agama mengajak seluruh umat untuk tidak golput dan datang ke TPS demi masa depan bangsa.",
                "ex_kana": "トコー リンタス アガマ ムンガジャッ スルルフ ウマット ウントゥッ ティダッ ゴルプット ダン ダタン ケ テーペーエス デミ マサ ドゥパン バンサ",
                "ex_ja": "宗教宗派を超えた指導者たちは、国家の未来のために棄権（golput）せず投票所に足を運ぶようすべての信徒に呼びかけました。",
                "note": "現代インドネシア政治史の象徴的略語です。"
            }
        ],
        "dialogue": {
            "title": "大統領選挙の投票日と開票速報の熱気",
            "lines": [
                ("Rian", "Pagi tadi saya sudah mencoblos di TPS dekat rumah untuk menggunakan hak pilih saya."),
                ("Siti", "Bagus sekali, Rian. Jangan sampai kita jadi bagian dari golput yang merugikan proses demokrasi."),
                ("Rian", "Bagaimana hasil hitung cepat televisi siang ini, apakah perolehan suara sudah mulai stabil?"),
                ("Siti", "Sudah masuk sekitar 80 persen suara sampel, dan antusiasme masyarakat pemilu kali ini luar biasa tinggi.")
            ],
            "trans": [
                ("リアン", "今朝、近所の投票所（TPS）で投票権を行使（menggunakan hak pilih）するために一票を投じてきたよ。"),
                ("シティ", "素晴らしいわ、リアン。民主主義プロセスを損なう白票・棄権（golput）の側になってはだめよね。"),
                ("リアン", "昼のテレビの開票速報（hitung cepat）はどう？得票率（perolehan suara）はもう安定してきたかい？"),
                ("シティ", "サンプルの約80％が開票されていて、今回の総選挙に対する市民の熱気は驚くほど高いわよ。")
            ]
        },
        "grammar_points": [
            "**pemilu と pilkada の区別**: \n- `pemilu` (pemilihan umum): 国レベルの総選挙（大統領・副大統領選、国会議員 DPR、地方代表議員 DPD）\n- `pilkada` (pemilihan kepala daerah): 地方自治体の首長選挙（州知事 Gubernur、市長 Walikota、県知事 Bupati）\n政治報道を正確に読み解くための基本分類です。",
            "**suara の換喩**: `suara` は本来「声・音声」ですが、選挙では「投票・票（votes）」を意味します（例: `suara sah`＝有効票、`perolehan suara`＝得票数、`hitung suara`＝開票）。"
        ],
        "quizzes": [
            {
                "q": "国民や市民が「主権者として選挙で投票権を行使する」を表す正しい動詞句はどれか。",
                "choices": ["menggunakan hak pilih", "menandatangani kontrak", "mengajukan gugatan", "memutarbalikkan fakta"],
                "ans": "menggunakan hak pilih",
                "expl": "選挙権・投票権を行使するは `menggunakan hak pilih` です。"
            },
            {
                "q": "選挙管理委員会や開票速報で「各候補者が獲得した得票数・得票率の集計」を意味する専門語はどれか。",
                "choices": ["perolehan suara", "arus kas", "pangsa pasar", "suku bunga"],
                "ans": "perolehan suara",
                "expl": "得票数・得票率は `perolehan suara` です。"
            },
            {
                "q": "選挙戦の終盤にスタジアムなどに十数万人の支持者を結集して行われる「大規模総決起集会」の呼称はどれか。",
                "choices": ["kampanye akbar", "kampanye promosi", "upacara adat", "evaluasi kinerja"],
                "ans": "kampanye akbar",
                "expl": "大規模な選挙集会・総決起ラリーは `kampanye akbar` です。"
            }
        ],
        "culture_column": {
            "title": "「Pesta Demokrasi」とお祭りのような選挙文化",
            "body": "インドネシアにおいて総選挙（Pemilu）は、堅苦しい義務ではなく「民主主義のお祭り（Pesta Demokrasi）」と呼ばれます。投票日には近所の投票所（TPS）にテントが張られ、民族衣装を着た係員が笑顔で迎え、投票を終えた指を紫色のインク（tinta pemilu）に浸してSNSで誇らしげにセルフィーを投稿します。政治的対立を超えて、全国民が祝祭として民主主義を楽しむ独自の明るいカルチャーが存在します。"
        }
    },
    {
        "filename": "docs/lexicon/32-politics-collocations-diplomacy.md",
        "title": "【共起連語】政治時事・外交の必須コロケーション辞典：hubungan bilateral / nota kesepahaman / kunjungan kenegaraan",
        "root": "diplomasi",
        "meaning": "外交、二国間関係、国際条約、首脳会談、使節",
        "core_concept": "「独立積極（Bebas Aktif）」を国是とし国際秩序の架け橋となるインドネシアの「外交関係（Diplomasi Internasional）」において、二国間関係、覚書締結、公式国家訪問、大使館実務など、国際ニュースを読み解く必須の外交コロケーションを網羅します。",
        "table_rows": [
            ("hubungan bilateral", "二国間の関係", "二国間関係、二国間友好親善", "外交/国際", "Indonesia dan Jepang sepakat mempererat hubungan bilateral di bidang transisi energi hijau."),
            ("nota kesepahaman (MoU)", "合意了解の覚え書き", "覚書、了解覚書（Memorandum of Understanding）", "条約/公式", "Kedua kementerian menandatangani nota kesepahaman kerja sama perlindungan tenaga kerja migran."),
            ("kunjungan kenegaraan", "国家の訪問", "公式国家訪問、国賓訪問（state visit）", "儀礼/首脳", "Presiden bertolak ke Washington untuk memenuhi undangan kunjungan kenegaraan."),
            ("duta besar luar biasa", "並外れた特命大使", "特命全権大使（Duta Besar Luar Biasa dan Berkuasa Penuh）", "外交官/使節", "Duta besar baru menyerahkan surat-surat kepercayaan kepada kepala negara di istana merdeka."),
            ("menjaga perdamaian dunia", "世界平和を守る", "国際平和を維持する、平和維持活動（PKO）", "国連/憲法", "Sesuai amanat konstitusi 1945, Indonesia aktif mengirim pasukan perdamaian PBB."),
            ("perjanjian ekstradisi", "引き渡しの協定", "犯罪人引き渡し条約（extradition treaty）", "司法/国際法", "Pemerintah meratifikasi perjanjian ekstradisi buronan korupsi dengan negara tetangga."),
            ("kedaulatan wilayah", "領域の主権", "領土主権、領海領空の不可侵性", "国防/安全保障", "TNI Angkatan Laut berpatroli rutin guna menjaga kedaulatan wilayah laut di perbatasan.")
        ],
        "details": [
            {
                "term": "hubungan bilateral (kerja sama antardua negara)",
                "trans": "二国間関係、二国間の外交・経済協力",
                "nuance": "ASEANや国連のような多国間外交（multilateral）と対比され、特定の2国間における友好条約、貿易協定、安全保障対話の枠組みを指します。",
                "ex_id": "Peringatan 65 tahun hubungan bilateral Indonesia-Jepang menjadi momentum memperkuat kemitraan strategis komprehensif.",
                "ex_kana": "プリンガタン アナムプル リマ タフン フブンガン ビラテラル インドネシア ジャパン ムンジャディ モメントゥム ムムプルクアット クミトラアン ストラテギス コンプレヘンシフ",
                "ex_ja": "インドネシアと日本の二国間関係（hubungan bilateral）樹立65周年は、包括的・戦略的パートナーシップを強化する契機となりました。",
                "note": "`mempererat hubungan bilateral`（二国間関係を緊密化する）が定石です。"
            },
            {
                "term": "nota kesepahaman / MoU (dokumen kesepakatan awal)",
                "trans": "了解覚書、覚書（MoU）",
                "nuance": "本格的な国際条約（perjanjian internasional）や正式契約の前段階として、協力の基本方針や合意枠組みを定めた文書です。",
                "ex_id": "Kedua menteri menandatangani nota kesepahaman tentang pengembangan ekosistem baterai kendaraan listrik.",
                "ex_kana": "クドゥア ムンテリ ムナンダタンガニ ノタ クセパハマン トゥンタン プンゲムバンガン エコシステム バテライ クンダラアン リストリッ",
                "ex_ja": "両大臣は、電気自動車用バッテリーのエコシステム開発に関する了解覚書（nota kesepahaman）に署名しました。",
                "note": "ニュースやビジネス実務では `MoU` と略されます。"
            },
            {
                "term": "kunjungan kenegaraan (kunjungan resmi kepala negara)",
                "trans": "国賓訪問、公式国家訪問（State Visit）",
                "nuance": "国家元首（大統領や国王）が他国を公式に訪問する最高格式の外交儀礼であり、21発の礼砲や大統領府での首脳会談を伴います。",
                "ex_id": "Dalam kunjungan kenegaraan ke Tokyo, Presiden dijadwalkan bertemu dengan Kaisar dan Perdana Menteri.",
                "ex_kana": "ダラム クンジュンガン クネガラアン ケ トウキョウ、プレシデン ディジャドワルカン ブルトゥム ドゥンガン カイサル ダン プルダナ ムンテリ",
                "ex_ja": "東京への国賓公式訪問（kunjungan kenegaraan）において、大統領は天皇陛下および首相と会談する予定です。",
                "note": "非公式実務訪問（kunjungan kerja）と格式が明確に区別されます。"
            },
            {
                "term": "duta besar luar biasa dan berkuasa penuh (Dubes LBBP)",
                "trans": "特命全権大使（Ambassador Extraordinary and Plenipotentiary）",
                "nuance": "外交使節団の最高責任者であり、派遣国の元首を直接代表して駐在国での全権外交権を行使する公式称号です。",
                "ex_id": "Duta Besar Luar Biasa Republik Indonesia untuk PBB menyampaikan pidato pembelaan atas hak-hak bangsa Palestina.",
                "ex_kana": "ドゥタ ブサール ルアル ビアサ レプブリッ インドネシア ウントゥッ ペーベーベー ムンニャンパイカン ピダト プムベラアン アタス ハッハッ バンサ パレスティナ",
                "ex_ja": "国連駐在インドネシア特命全権大使（duta besar luar biasa）は、パレスチナ人民の権利を擁護する力強い演説を行いました。",
                "note": "略称は `Dubes`（ドゥベス）です。"
            },
            {
                "term": "menjaga kedaulatan wilayah (integritas teritorial)",
                "trans": "領域主権を維持・防衛する、領土保全",
                "nuance": "17,000を超える島々からなる群島国家（negara kepulauan）インドネシアが、排他的経済水域（ZEE）や国境離島の主権を他国の不法侵入から守る安全保障の絶対命題です。",
                "ex_id": "TNI berkomitmen penuh menjaga kedaulatan wilayah kedaulatan NKRI dari ancaman separatis maupun agresi luar.",
                "ex_kana": "テーエヌイー ブルコミットメン プヌー ムンジャガ クダウラタン ウィラヤ クダウラタン エヌカーエルイー ダリ アンチャマン セパラティス マウプン アグレシ ルアル",
                "ex_ja": "国軍（TNI）は、分離主義の脅威や外部からの侵略からインドネシア共和国統一国家（NKRI）の領域主権（kedaulatan wilayah）を死守することに全力を傾注しています。",
                "note": "国防政策の最高基本概念です。"
            }
        ],
        "dialogue": {
            "title": "二国間首脳会談と投資覚書の締結",
            "lines": [
                ("Diplomat Senior", "Bagaimana persiapan penyambutan kunjungan kenegaraan Perdana Menteri besok pagi?"),
                ("Staf Protokol", "Semua sudah siap, Pak. Upacara jajar kehormatan dan pertemuan bilateral akan digelar di Istana Bogor."),
                ("Diplomat Senior", "Pastikan draf nota kesepahaman investasi energi terbarukan sudah diverifikasi kementerian hukum."),
                ("Staf Protokol", "Sudah tuntas, Pak. Duta besar kedua negara juga telah mengonfirmasi kehadiran dalam upacara penandatanganan.")
            ],
            "trans": [
                ("上席外交官", "明朝の首相の公式国家訪問（kunjungan kenegaraan）の出迎え準備はどうなっているかね？"),
                ("儀典スタッフ", "すべて整いました。栄誉礼儀仗式と二国間首脳会談（pertemuan bilateral）はボゴール宮殿で執り行われます。"),
                ("上席外交官", "再生可能エネルギー投資に関する了解覚書（nota kesepahaman）のドラフトが法務省の確認を終えているか再確認してくれ。"),
                ("儀典スタッフ", "完了しております。両国の特命全権大使（duta besar）も調印式への出席を確認済みです。")
            ]
        },
        "grammar_points": [
            "**接辞による kedaulatan の形成**: 語根 `daulat`（主権・権能）に周囲辞 `ke-...-an` が付加されて抽象名詞 `kedaulatan`（主権・統治権）を形成します（例: `kedaulatan rakyat`＝国民主権、`kedaulatan pangan`＝食料主権）。",
            "**kenegaraan の形容詞的機能**: `negara`（国家）に `ke-...-an` が付いた `kenegaraan` は「国家の、国家的な」という形容詞として、`upacara kenegaraan`（国家式典）、`kunjungan kenegaraan`（国賓訪問）などを形成します。"
        ],
        "quizzes": [
            {
                "q": "国際外交において「特定の2つの国家の間で結ばれる友好・通商・政治関係」を表す専門語はどれか。",
                "choices": ["hubungan bilateral", "hubungan multilateral", "kunjungan kenegaraan", "nota kesepahaman"],
                "ans": "hubungan bilateral",
                "expl": "二国間関係は `hubungan bilateral` です（多国間関係は `multilateral`）。"
            },
            {
                "q": "政府間や企業間で「協力の基本方針を定めて署名する了解覚書（MoU）」のインドネシア語正式名称はどれか。",
                "choices": ["nota kesepahaman", "surat peringatan", "kotak suara", "laporan laba rugi"],
                "ans": "nota kesepahaman",
                "expl": "覚書（MoU）の正式名称は `nota kesepahaman` です。"
            },
            {
                "q": "国家元首が他国を最高格式で公式訪問する「国賓訪問（State Visit）」を表す連語はどれか。",
                "choices": ["kunjungan kenegaraan", "kunjungan kerja", "kunjungan keluarga", "kunjungan wisata"],
                "ans": "kunjungan kenegaraan",
                "expl": "国賓訪問・国家公式訪問は `kunjungan kenegaraan` です。"
            }
        ],
        "culture_column": {
            "title": "「Bebas Aktif」とアジア・アフリカ会議の外交精神",
            "body": "インドネシア外交の神髄は、冷戦初期の1948年に初代副大統領モハマッド・ハッタが提唱した「Bebas Aktif（独立積極）」ドクトリンにあります。東西どちらの軍事同盟ブロックにも盲従せず（Bebas＝自由・非同盟）、世界平和と反植民地主義のために主導的に行動する（Aktif＝積極的）という理念は、1955年のバンドン・アジア・アフリカ会議（KAA）で結実し、現代のASEAN外交に至るまで国家の揺るぎない誇りとなっています。"
        }
    },
    {
        "filename": "docs/lexicon/33-legal-collocations-court.md",
        "title": "【共起連語】法律時事・法廷の必須コロケーション辞典：mengajukan gugatan / vonis hakim / saksi kunci / praduga tak bersalah",
        "root": "hukum",
        "meaning": "法律、司法、裁判、訴訟、法理",
        "core_concept": "法治国家（Negara Hukum）の正義と秩序を担保する「法廷・司法実務（Pengadilan & Peradilan）」において、訴訟提起、判決言い渡し、重要証人、無罪推定の原則など、法廷劇や事件報道を深く理解するための必須コロケーションを体系化します。",
        "table_rows": [
            ("mengajukan gugatan", "訴えを提出する", "提訴する、訴訟を提起する、民事裁判を起こす", "民事/法務", "Warga korban pencemaran limbah mengajukan gugatan perdata ganti rugi terhadap pabrik."),
            ("vonis hakim", "裁判官の判決", "裁判所の判決、言渡し、有罪・無罪判決", "刑事/司法", "Majelis hakim menjatuhkan vonis dua puluh tahun penjara kepada terdakwa kasus pembunuhan."),
            ("saksi kunci", "鍵の証人", "重要証人、キーパーソンとなる証人、決め手となる証言者", "事件/公判", "LPSK memberikan perlindungan fisik ketat kepada saksi kunci pembongkaran mafia pajak."),
            ("bukti otentik", "本物の証拠", "確実な証拠、真正な書証、動かぬ物証", "証拠法/法廷", "Jaksa penuntut umum membeberkan rekaman kamera pengawas sebagai bukti otentik di persidangan."),
            ("praduga tak bersalah", "無罪の推定", "無罪推定の原則（presumption of innocence）", "憲法/人権", "Media massa diwajibkan mematuhi asas praduga tak bersalah sebelum adanya putusan hukum tetap."),
            ("kekuatan hukum tetap (inkrah)", "確定した法的効力", "判決確定、法的効力の確定（オランダ語 in kracht van gewijsde）", "司法/終局", "Eksekusi hukuman mati baru dapat dilaksanakan setelah perkara berkekuatan hukum tetap."),
            ("alat bukti", "証拠の道具", "法定証拠手段（目撃証言、鑑定、書証、自白等）", "刑事訴訟法", "Penyidik telah mengantongi minimal dua alat bukti sah sebelum menetapkan status tersangka.")
        ],
        "details": [
            {
                "term": "mengajukan gugatan perdata (melayangkan tuntutan hukum)",
                "trans": "民事訴訟を提起する、提訴する",
                "nuance": "契約違反や不法行為（perbuatan melawan hukum）によって損害を被った原告（penggugat）が、地方裁判所に正式な訴状を提出して裁判の審理を求める行為です。",
                "ex_id": "Masyarakat adat mengajukan gugatan terhadap izin konsesi tambang yang menyerobot hutan ulayat.",
                "ex_kana": "マシャラカット アダット ムンガジュカン グガタン トゥルハダップ イジン コンセシ タンバン ヤン ムニェロボット フタン ウラヤット",
                "ex_ja": "先住慣習法共同体は、慣習林を侵害した鉱山採掘コンセッション許可に対して訴訟を提起（mengajukan gugatan）しました。",
                "note": "刑事の「起訴」は `melimpahkan berkas perkara / menuntut` です。"
            },
            {
                "term": "vonis hakim (putusan majelis hakim)",
                "trans": "裁判官（合議体）の判決、言い渡し",
                "nuance": "審理を終えた裁判長（Ketua Majelis Hakim）が、法廷で朗読して宣告する終局判決です。動詞 `menjatuhkan vonis`（判決を下す）と強固に共起します。",
                "ex_id": "Terdakwa tampak tertunduk lesu saat mendengarkan vonis hakim yang menjatuhkan hukuman seumur hidup.",
                "ex_kana": "トゥルダクワ タンパック トゥルトゥンドゥッ レス サアット ムンデンガルカン ヴォニス ハキム ヤン ムンジャトゥフカン フクマン スウムル ヒドゥップ",
                "ex_ja": "被告人は、終身刑を言い渡す裁判官の判決（vonis hakim）を聞きながら力なくうなだれていました。",
                "note": "無罪判決は `vonis bebas` と呼ばれます。"
            },
            {
                "term": "saksi kunci (saksi mahkota / saksi penentu)",
                "trans": "重要証人、キーパーソンとなる証人",
                "nuance": "事件の真相や首謀者を特定する上で決定的な証言（kesaksian）を持ち、身の危険に晒されやすい証人を指します。証人保護庁（LPSK）が警護にあたります。",
                "ex_id": "Kehadiran saksi kunci di persidangan berhasil membongkar skandal korupsi yang melibatkan pejabat tinggi.",
                "ex_kana": "クハディラン サクシ クンチ ディ プルスィダンガン ブルハシル ムムボンカル スカンダル コルプスィ ヤン ムリバットカン プジャバット ティンギ",
                "ex_ja": "法廷への重要証人（saksi kunci）の出廷は、高官が関与した汚職スキャンダルを白日の下に晒す決定打となりました。",
                "note": "`kunci`（鍵）という比喩が効いています。"
            },
            {
                "term": "asas praduga tak bersalah (presumption of innocence)",
                "trans": "無罪推定の原則",
                "nuance": "裁判所による確定判決が下されるまでは、いかなる被疑者・被告人も無実として扱われねばならないという近代刑事法規の至上原則です。",
                "ex_id": "Polisi dan jurnalis harus tetap menghormati asas praduga tak bersalah saat merilis penangkapan tersangka.",
                "ex_kana": "ポリシ ダン ジュルナリス ハルス トゥタップ ムンホルマティ アサス プラドゥガ タッ ブルサラー サアット メリリース プナンカパン トゥルサンカ",
                "ex_ja": "警察およびジャーナリストは、容疑者逮捕を発表する際にも無罪推定の原則（asas praduga tak bersalah）を厳格に尊重しなければなりません。",
                "note": "法制・人権報道の必須語彙です。"
            },
            {
                "term": "berkekuatan hukum tetap / inkrah (in kracht van gewijsde)",
                "trans": "判決が確定した、法的効力が最終確定した（インクラ）",
                "nuance": "控訴（banding）や上告（kasasi）の期限が切れるか最高裁で棄却され、これ以上通常の上訴手段で争えなくなった最終確定判決を指すオランダ法由来の最重要語です。",
                "ex_id": "Eksekusi penyitaan aset koruptor baru dapat dilakukan setelah putusan perkara berkekuatan hukum tetap.",
                "ex_kana": "エクセクスィ プニィタアン アセット コルプトール バル ダパット ディラクカン ステラ プトゥサン プルカラ ブルククアタン フクム トゥタップ",
                "ex_ja": "汚職犯の資産差し押さえ執行は、事件の判決が法的に確定（berkekuatan hukum tetap / inkrah）した後に初めて実施可能となります。",
                "note": "実務ではオランダ語由来の俗称 `inkrah`（インクラ）が飛び交います。"
            }
        ],
        "dialogue": {
            "title": "大型汚職裁判の結審と判決言い渡し",
            "lines": [
                ("Wartawan Hukum", "Bagaimana suasana di ruang sidang pembacaan vonis mantan menteri tadi, Bu Jaksa?"),
                ("Jaksa Penuntut", "Sangat tegang. Berkat keterangan saksi kunci dan bukti otentik aliran dana, dakwaan kami terbukti."),
                ("Wartawan Hukum", "Berapa lama vonis hakim yang dijatuhkan? Apakah terdakwa langsung menerima?"),
                ("Jaksa Penuntut", "Divonis dua belas tahun penjara. Kuasa hukumnya masih pikir-pikir dan belum inkrah karena ada rencana banding.")
            ],
            "trans": [
                ("司法記者", "先ほどの元大臣への判決言い渡し（pembacaan vonis）の法廷の雰囲気はどうでしたか、検事さん？"),
                ("検察官", "極めて緊迫していました。重要証人（saksi kunci）の証言と資金移動の動かぬ証拠（bukti otentik）のおかげで、私たちの起訴事実は立証されました。"),
                ("司法記者", "裁判官の判決（vonis hakim）の刑期はどれくらいでしたか？被告側は即座に受け入れましたか？"),
                ("検察官", "懲役12年の判決でした。弁護団は熟慮期間に入っており、控訴の意向があるためまだ判決確定（inkrah）ではありません。")
            ]
        },
        "grammar_points": [
            "**gugat から gugatan への名詞化**: 動詞語根 `gugat`（訴える・告発する）に接尾辞 `-an` が付いて `gugatan`（訴訟・訴状・要求）となります。動詞句は `mengajukan gugatan`（提訴する）と共起します。",
            "**オランダ語由来の司法隠語 inkrah**: 正式な法令用語は `berkekuatan hukum tetap`（恒久的な法的効力を有する）ですが、弁護士、検察官、裁判官、事件記者は全員一致してオランダ語 `in kracht van gewijsde` を短縮した `inkrah`（インクラ）を口語・日常実務で用います。"
        ],
        "quizzes": [
            {
                "q": "裁判において「損害賠償を求めて地方裁判所に正式に民事訴訟を起こす・提訴する」を表す動詞句はどれか。",
                "choices": ["mengajukan gugatan", "menjatuhkan vonis", "memutus kontrak", "mengambil alih"],
                "ans": "mengajukan gugatan",
                "expl": "提訴する、民事訴訟を起こすは `mengajukan gugatan` です。"
            },
            {
                "q": "事件の真相を解明する上で決定的な証言を行い、法廷の鍵を握る「重要証人」の呼称はどれか。",
                "choices": ["saksi kunci", "saksi bisu", "kaki tangan", "tangan kanan"],
                "ans": "saksi kunci",
                "expl": "重要証人、キーマンとなる証人は `saksi kunci` です。"
            },
            {
                "q": "これ以上上訴できず、判決が最終的に法的効力を持って確定した状態（インクラ）を表す正式な法律用語はどれか。",
                "choices": ["berkekuatan hukum tetap", "praduga tak bersalah", "alat bukti sah", "tutup usia"],
                "ans": "berkekuatan hukum tetap",
                "expl": "判決確定は `berkekuatan hukum tetap`（通称 inkrah）です。"
            }
        ],
        "culture_column": {
            "title": "「LPSK」と内部告発者を守る正義の砦",
            "body": "権力者やマフィアが絡む巨大汚職裁判において、重要証人（saksi kunci）や内部告発者（whistleblower）は常に暗殺や脅迫の危機に晒されます。そこでインドネシアでは2006年に独立国家機関として「証人被害者保護庁（LPSK: Lembaga Perlindungan Saksi dan Korban）」が設立されました。安全な隠れ家（safe house）の提供や法廷での厳重な武装警護を通じて、弱者が恐れることなく真実を証言できる司法環境を支えています。"
        }
    },
    {
        "filename": "docs/lexicon/34-economics-collocations-inflation.md",
        "title": "【共起連語】マクロ経済時事の必須コロケーション辞典：laju inflasi / pertumbuhan ekonomi / daya beli masyarakat",
        "root": "ekonomi",
        "meaning": "経済、景気、インフレ、購買力、貿易収支",
        "core_concept": "2億8千万の人口を擁し東南アジア最大の経済規模を誇るインドネシアの「マクロ経済（Ekonomi Makro）」において、物価上昇率、経済成長率、国民の購買力、貿易収支など、経済ニュースや市場分析を精読するための必須コロケーションを整理します。",
        "table_rows": [
            ("laju inflasi", "インフレの速度", "インフレ率、物価上昇率、物価騰貴のペース", "マクロ/物価", "Bank Indonesia menargetkan laju inflasi tahunan berada di kisaran 2,5 plus minus 1 persen."),
            ("pertumbuhan ekonomi", "経済の成長", "経済成長、経済成長率、GDP成長", "国家/統計", "Pertumbuhan ekonomi Indonesia pada kuartal kedua tercatat solid sebesar 5,05 persen."),
            ("daya beli masyarakat", "社会の買う力", "国民の購買力、消費意欲、実質消費能力", "消費/福祉", "Bantuan sosial pangan disalurkan secara berkala untuk menjaga daya beli masyarakat miskin."),
            ("neraca perdagangan", "貿易の天秤", "貿易収支（黒字: surplus, 赤字: defisit）", "貿易/為替", "Indonesia mencatatkan surplus neraca perdagangan selama 40 bulan berturut-turut berkat ekspor komoditas."),
            ("cadangan devisa", "外貨の蓄え", "外貨準備高、外貨保有額", "中央銀行/通貨", "Cadangan devisa nasional dinilai memadai untuk membiayai kebutuhan impor dan pembayaran utang luar negeri."),
            ("pendapatan domestik bruto (PDB)", "国内総所得", "国内総生産（GDP）", "経済統計/国力", "Sektor konsumsi rumah tangga masih menjadi kontributor terbesar terhadap PDB nasional."),
            ("gejolak pasar", "市場の動揺・波乱", "市場のボラティリティ、相場の混乱、金融不安", "市場/証券", "Otoritas Jasa Keuangan (OJK) terus memantau gejolak pasar keuangan global secara intensif.")
        ],
        "details": [
            {
                "term": "laju inflasi (tingkat kenaikan harga barang dan jasa)",
                "trans": "インフレ率、物価上昇ペース",
                "nuance": "食品価格の季節変動（volatile food）や燃料価格など、生活必需品の物価上昇スピードを指す中央銀行や統計局（BPS）の最重要指標です。",
                "ex_id": "Pemerintah daerah mengawasi rantai pasokan bahan pokok untuk meredam laju inflasi menjelang bulan suci Ramadhan.",
                "ex_kana": "プムリンター ダエラ ムンガワスィ ランタイ パソカン バハン ポコッ ウントゥッ ムルダム ラジュ インフラシ ムンジュラン ブラン スチ ラマダン",
                "ex_ja": "地方自治体は、聖なる断食月を前に物価上昇率（laju inflasi）を抑制するため、生活必需品のサプライチェーンを監視しています。",
                "note": "`meredam laju inflasi`（インフレ率を抑え込む）と共起します。"
            },
            {
                "term": "daya beli masyarakat (kemampuan belanja konsumen)",
                "trans": "国民の購買力、実質消費能力",
                "nuance": "物価高や雇用情勢によって左右される一般市民の財布事情（消費購買力）を表し、内需主導型経済であるインドネシアの景気回復を左右する決定打です。",
                "ex_id": "Pelemahan daya beli masyarakat di kelas menengah menjadi sorotan para ekonom dalam beberapa kuartal terakhir.",
                "ex_kana": "プルマハン ダヤ ベリ マシャラカット ディ クラス ムネンガ ムンジャディ ソロタン パラ エコノム ダラム ブルブラパ クアルタル トゥルアヒル",
                "ex_ja": "中間層における国民の購買力の低下（pelemahan daya beli）は、ここ数四半期にわたりエコノミストたちの注目の的となっています。",
                "note": "`menjaga daya beli`（購買力を維持する）が頻出します。"
            },
            {
                "term": "pertumbuhan ekonomi berkualitas",
                "trans": "質の高い経済成長（格差是正・雇用創出を伴う成長）",
                "nuance": "単なるGDPの数字の上昇だけでなく、貧困削減（pengentasan kemiskinan）や広範な雇用創出を伴う持続可能な成長を希求する政策用語です。",
                "ex_id": "Pemerintah menargetkan pertumbuhan ekonomi berkualitas yang mampu menyerap jutaan tenaga kerja baru.",
                "ex_kana": "プムリンター ムナルゲッカン プルトゥムブハン エコノミ ブルクアリタス ヤン マムプ ムニェラップ ジュタアン トゥナガ クルジャ バル",
                "ex_ja": "政府は、何百万人もの新規労働力を吸収しうる質の高い経済成長（pertumbuhan ekonomi berkualitas）を目指しています。",
                "note": "開発経済学の重要キーワードです。"
            },
            {
                "term": "surplus neraca perdagangan (ekspor melebihi impor)",
                "trans": "貿易収支の黒字、貿易黒字",
                "nuance": "石炭、パーム油（CPO）、ニッケルなどの天然資源加工品輸出が好調で、輸出総額が輸入総額を上回り外貨を獲得している健全な状態を指します。",
                "ex_id": "Surplus neraca perdagangan yang berlanjut menjadi bantalan kokoh bagi stabilitas nilai tukar rupiah.",
                "ex_kana": "スルプルス ネラチャ プルダガンガン ヤン ブルランジュット ムンジャディ バンタラン ココー バギ スタビリタス ニライ トゥカール ルピア",
                "ex_ja": "継続する貿易収支の黒字（surplus neraca perdagangan）は、ルピア為替レートの安定にとって強固なクッション（防壁）となっています。",
                "note": "対義語は `defisit neraca perdagangan`（貿易赤字）です。"
            },
            {
                "term": "cadangan devisa (foreign exchange reserves)",
                "trans": "外貨準備高、公式外貨準備保有額",
                "nuance": "通貨危機の防衛、輸入代金の決済、政府の対外債務返済に充当するため、中央銀行が保有する米ドルや金（emas）などの国際準備資産です。",
                "ex_id": "Posisi cadangan devisa Indonesia pada akhir bulan lalu setara dengan pembiayaan 6,5 bulan impor.",
                "ex_kana": "ポジスィ チャダンガン デヴィサ インドネシア パダ アヒル ブラン ラル スタラ ドゥンガン プムビアヤアン エナム コマ リマ ブラン エクスポール",
                "ex_ja": "先月末時点のインドネシアの外貨準備高（cadangan devisa）は、輸入6.5ヶ月分の支払いに相当する規模を維持しています。",
                "note": "国際通貨基金（IMF）の安全基準（3ヶ月分）を大きく上回ります。"
            }
        ],
        "dialogue": {
            "title": "中央銀行の景気見通しと物価安定化対策",
            "lines": [
                ("Ekonom", "Bagaimana penilaian Anda mengenai rilis data laju inflasi dari Badan Pusat Statistik kemarin?"),
                ("Analis Pasar", "Sangat terkendali, berada di level 2,1 persen. Namun tantangannya adalah menjaga daya beli masyarakat di pedesaan."),
                ("Ekonom", "Betul sekali. Konsumsi domestik adalah motor utama agar pertumbuhan ekonomi kita bisa mencapai lima persen tahun ini."),
                ("Analis Pasar", "Apalagi surplus neraca perdagangan kita masih kuat, sehingga cadangan devisa kita cukup aman meredam gejolak global.")
            ],
            "trans": [
                ("エコノミスト", "昨日の中央統計庁（BPS）によるインフレ率（laju inflasi）の発表データをどう評価されますか？"),
                ("市場アナリスト", "極めてよく抑制されており、2.1％の水準に収まっています。しかし課題は農村部の国民の購買力（daya beli masyarakat）をどう維持するかですね。"),
                ("エコノミスト", "その通りです。今年の経済成長（pertumbuhan ekonomi）5％を達成するには、国内消費が最大のエンジンですから。"),
                ("市場アナリスト", "幸い貿易収支の黒字（surplus neraca perdagangan）も依然堅調で、外貨準備高（cadangan devisa）も世界的な波乱を吸収するのに十分な安全圏にあります。")
            ]
        },
        "grammar_points": [
            "**laju の速度・ペースメタファー**: `laju` は船や車の「走航・前進速度」を意味しますが、マクロ経済では `laju inflasi`（インフレ率）、`laju pertumbuhan`（成長ペース）のように、変動率の推移スピードを表す抽象名詞として定着しています。",
            "**neraca のバランス・天秤**: `neraca`（天秤ばかり）は、`neraca perdagangan`（貿易収支）、`neraca pembayaran`（国際収支）、`neraca keuangan`（貸借対照表）のように、左右の入出金バランスを計測する用語の基底となります。"
        ],
        "quizzes": [
            {
                "q": "中央銀行や政府が生活必需品の価格安定を図るために常に注視する「インフレ率・物価上昇率」を表す連語はどれか。",
                "choices": ["laju inflasi", "daya beli masyarakat", "suku bunga acuan", "arus kas operasional"],
                "ans": "laju inflasi",
                "expl": "インフレ率・物価上昇ペースは `laju inflasi` です。"
            },
            {
                "q": "内需主導型経済において極めて重視される「一般庶民や国民の実質的な消費購買力」を意味する用語はどれか。",
                "choices": ["daya beli masyarakat", "pertumbuhan ekonomi", "pangsa pasar", "suntikan modal"],
                "ans": "daya beli masyarakat",
                "expl": "国民の購買力は `daya beli masyarakat` です。"
            },
            {
                "q": "輸出総額が輸入総額を上回り、外貨の流入が健全に維持されている「貿易収支の黒字」を表す表現はどれか。",
                "choices": ["surplus neraca perdagangan", "defisit neraca perdagangan", "cadangan devisa", "laporan laba rugi"],
                "ans": "surplus neraca perdagangan",
                "expl": "貿易黒字は `surplus neraca perdagangan` です。"
            }
        ],
        "culture_column": {
            "title": "「Bansos」とインドネシアの社会的セーフティネット",
            "body": "生活必需品や米の価格が高騰した際、インドネシア政府が機動的に発動するのが社会扶助「バンソス（Bansos: Bantuan Sosial）」の配布です。米の現物配給（bansos beras）や直接現金給付（BLT: Bantuan Langsung Tunai）を通じて、最貧困層の食卓を守り、国民の購買力（daya beli masyarakat）の底割れを防ぎます。社会の安定（stabilitas nasional）を保つための最重要の政治経済ツールです。"
        }
    },
    {
        "filename": "docs/lexicon/35-environment-collocations-climate.md",
        "title": "【共起連語】環境時事・気候変動の必須コロケーション辞典：pemanasan global / energi terbarukan / emisi karbon",
        "root": "lingkungan",
        "meaning": "環境、生態系、気候変動、脱炭素、森林保全",
        "core_concept": "熱帯雨林とメガ・バイオダイバーシティを抱える環境大国インドネシアの「地球環境＆気候変動（Lingkungan & Perubahan Iklim）」において、地球温暖化、再生可能エネルギー、炭素排出量、森林破壊、温室効果ガスなど、COP国際気候サミットや環境報道の必須コロケーションを体系化します。",
        "table_rows": [
            ("pemanasan global", "地球の温暖化", "地球温暖化、グローバル・ウォーミング", "気候/科学", "Pemanasan global telah memicu anomali cuaca ekstrem dan mempercepat kenaikan permukaan air laut."),
            ("energi terbarukan (EBT)", "更新されうるエネルギー", "再生可能エネルギー（太陽光、地熱、水力、バイオマス）", "エネルギー/政策", "Pemerintah berkomitmen meningkatkan bauran energi terbarukan hingga 23 persen pada tahun 2025."),
            ("emisi karbon", "炭素の放出", "炭素排出量、CO2排出、温室効果ガス排出", "環境/産業", "Pemberlakuan pajak karbon dirancang untuk mendorong industri menurunkan emisi karbon secara bertahap."),
            ("deforestasi hutan", "森林の脱森林化", "森林伐採、森林破壊、乱伐", "保全/林業", "Teknologi satelit digunakan secara aktif untuk memantau titik deforestasi di pedalaman Kalimantan."),
            ("efek rumah kaca", "温室の効果", "温室効果（greenhouse effect）、温暖化メカニズム", "理科/環境", "Peningkatan konsentrasi gas metana dan CO2 di atmosfer kian memperparah efek rumah kaca."),
            ("lahan gambut", "泥炭の土地", "泥炭地、ピートランド（巨大な炭素貯留層）", "湿地/保全", "Restorasi lahan gambut sangat krusial untuk mencegah kebakaran hutan dan bencana kabut asap."),
            ("transisi energi", "エネルギーの移行", "エネルギー転換、脱石炭・クリーンエネルギーシフト", "国際/開発", "Transisi energi yang adil (Just Energy Transition) membutuhkan pendanaan iklim dari negara-negara maju.")
        ],
        "details": [
            {
                "term": "energi baru terbarukan / EBT (renewable energy)",
                "trans": "新・再生可能エネルギー（地熱、太陽光、水力等）",
                "nuance": "インドネシア国家エネルギー政策の核心用語で、世界最大の地熱資源（geotermal）や豊富な太陽光を活用したクリーンエネルギーへの転換を目指す包括的概念です。",
                "ex_id": "Pembangkit Listrik Tenaga Surya (PLTS) Terapung Cirata merupakan bukti nyata pemanfaatan energi terbarukan di tanah air.",
                "ex_kana": "プムバンキット リストリッ トゥナガ スルヤ トゥラプン チラタ ムルパカン ブクティ ニャタ プマンファアタン エネルギ トゥルバルカン ディ タナ アイル",
                "ex_ja": "チラタ水上太陽光発電所（PLTS）は、国内における再生可能エネルギー（energi terbarukan）活用の具体的な証左です。",
                "note": "公的文書では略称 `EBT` が標準的に用いられます。"
            },
            {
                "term": "menekan emisi karbon (dekarbonisasi industri)",
                "trans": "炭素排出量を削減する、脱炭素化を進める",
                "nuance": "2060年までのネットゼロエミッション（Net-Zero Emission）達成に向け、石炭火力発電所の早期退役や電気自動車普及を通じてCO2排出を削減する国家戦略です。",
                "ex_id": "Pabrik semen ramah lingkungan ini mengadopsi teknologi penangkapan karbon untuk menekan emisi karbon pabrik.",
                "ex_kana": "パブリック セメン ラマー リングクンガン イニ ムンガドプスィ テクノロギ プナンカパン カルーボン ウントゥッ ムヌカン エミスィ カルーボン パブリック",
                "ex_ja": "この環境配慮型セメント工場は、工場の炭素排出量（emisi karbon）を削減するために炭素回収技術を導入しました。",
                "note": "`perdagangan karbon`（炭素排出量取引 / カーボンクレジット）と直結します。"
            },
            {
                "term": "deforestasi hutan tropis (penggundulan hutan liar)",
                "trans": "熱帯雨林の森林伐採・森林破壊",
                "nuance": "アブラヤシ農園開発や鉱山採掘による原生林の伐採を指し、オランウータン等の固有種の絶滅危機や地球規模の炭素放出を引き起こす世界的な環境論争の的です。",
                "ex_id": "Pemberian moratorium izin baru perkebunan sawit berhasil menekan laju deforestasi hutan primer secara signifikan.",
                "ex_kana": "プンベリアン モラトリウム イジン バル プルクブナン サウィット ブルハシル ムヌカン ラジュ デフォレスタスィ フタン プリメル スチャラ スィグニフィカン",
                "ex_ja": "パーム油農園の新規開発許可の凍結（モラトリアム）措置は、原生林の森林破壊（deforestasi）のペースを大幅に抑制しました。",
                "note": "国際環境NGOの報告書で最頻出する重要単語です。"
            },
            {
                "term": "restorasi lahan gambut (pemulihan ekosistem gambut)",
                "trans": "泥炭湿原の再生、ピートランドの復元・保水",
                "nuance": "炭素を膨大に貯蔵している泥炭地（lahan gambut）が乾燥して山火事（kebakaran hutan）を起こし、有毒な煙霧（kabut asap / haze）が隣国シンガポールまで覆うのを防ぐための湿潤化・再緑化事業です。",
                "ex_id": "Badan Restorasi Gambut dan Mangrove (BRGM) bertugas membasahi kembali lahan gambut yang mengering demi mencegah karhutla.",
                "ex_kana": "バダン レストラスィ ガンブット ダン マングローフ ブルトゥガス ムンバサヒ クンバリ ラハン ガンブット ヤン ムンゲリン デミ ムンチェガ カルフトラ",
                "ex_ja": "泥炭マングローブ再生庁（BRGM）は、森林火災（karhutla）を防ぐため乾燥した泥炭地（lahan gambut）を再湿潤化する任務を担っています。",
                "note": "`karhutla`（森林泥炭火災）の対策に不可欠です。"
            },
            {
                "term": "dampak pemanasan global terhadap pesisir",
                "trans": "地球温暖化が沿岸部に及ぼす影響（海面上昇と浸水）",
                "nuance": "ジャカルタ北部や北中部ジャワ沿岸（スモラン等）で頻発する高潮冠水（banjir rob）や地盤沈下、島嶼部の水没危機を描写する喫緊の気候正義の課題です。",
                "ex_id": "Warga pulau-pulau kecil mulai merasakan dampak nyata pemanasan global akibat naiknya permukaan laut.",
                "ex_kana": "ワルガ プラウプラウ クチル ムライ ムラサカン ダンパック ニャタ プマナサン グロバル アクバット ナイッニャ プルムカアン ラウト",
                "ex_ja": "小さな島々の住民たちは、海面上昇による地球温暖化（pemanasan global）の現実の脅威を身をもって感じ始めています。",
                "note": "首都移転の主要動機の一つでもあります。"
            }
        ],
        "dialogue": {
            "title": "国際気候サミットと脱炭素エネルギー転換",
            "lines": [
                ("Aktivis Lingkungan", "Pemerintah harus lebih ambisius dalam menekan emisi karbon dari pembangkit listrik tenaga batu bara."),
                ("Pejabat ESDM", "Tentu, kami sedang mempercepat transisi energi dengan meningkatkan porsi energi terbarukan seperti panas bumi dan surya."),
                ("Aktivis Lingkungan", "Bagaimana dengan perlindungan hutan hujan tropis dan lahan gambut di luar Jawa?"),
                ("Pejabat ESDM", "Laju deforestasi sudah turun drastis dalam tiga tahun terakhir berkat penegakan hukum dan restorasi lahan gambut berkelanjutan.")
            ],
            "trans": [
                ("環境活動家", "政府は石炭火力発電所からの炭素排出量（emisi karbon）の削減に対してもっと野心的であるべきです。"),
                ("エネルギー鉱物資源省官僚", "もちろんです。私たちは地熱や太陽光といった再生可能エネルギー（energi terbarukan）の比率を高め、エネルギー転換（transisi energi）を加速させています。"),
                ("環境活動家", "ジャワ島以外の熱帯雨林や泥炭地（lahan gambut）の保全はどうなっていますか？"),
                ("エネルギー鉱物資源省官僚", "森林破壊（deforestasi）のペースは、厳格な法執行と持続可能な泥炭地再生によって過去3年間で劇的に低下していますよ。")
            ]
        },
        "grammar_points": [
            "**接尾辞 -kan による terbarukan**: `baru`（新しい）に受動接頭辞 `ter-` と使役接尾辞 `-kan` が付加された `terbarukan` は、「更新可能な、再生可能な（renewable）」という環境科学の専門形容詞として定着しています。",
            "**略語 karhutla の浸透**: `kebakaran hutan dan lahan`（森林および土地の火災）は、気象庁（BMKG）や防災庁（BNPB）の公的発表で常に `karhutla`（カルフトラ）と略称されます。"
        ],
        "quizzes": [
            {
                "q": "太陽光、風力、地熱、水力など、枯渇せず自然に更新される「再生可能エネルギー」の正式なインドネシア語はどれか。",
                "choices": ["energi terbarukan (EBT)", "emisi karbon", "lahan gambut", "deforestasi hutan"],
                "ans": "energi terbarukan (EBT)",
                "expl": "再生可能エネルギーは `energi terbarukan`（略称 EBT）です。"
            },
            {
                "q": "森林伐採や開発により「広大な熱帯雨林が失われ破壊されること」を意味する国際環境用語はどれか。",
                "choices": ["deforestasi hutan", "pemanasan global", "transisi energi", "efek rumah kaca"],
                "ans": "deforestasi hutan",
                "expl": "森林破壊・森林伐採は `deforestasi` です。"
            },
            {
                "q": "膨大な炭素を貯蔵し、乾燥すると激しい煙霧火災を引き起こす「泥炭湿地」を意味する語はどれか。",
                "choices": ["lahan gambut", "hutan ulayat", "mata air", "kaki bukit"],
                "ans": "lahan gambut",
                "expl": "泥炭地は `lahan gambut` です。"
            }
        ],
        "culture_column": {
            "title": "「Hutan Adat」と先住民族の知恵を守った憲法判決（MK 35）",
            "body": "インドネシアの森林保全における金字塔が、2012年の憲法裁判所判決（Putusan MK No. 35/PUU-X/2012）です。それまで「国有林」とみなされ企業に伐採権が乱発されていた熱帯林に対し、「先住慣習林（Hutan Adat）は国有林ではない」と宣言し、何百年も自然と共生してきた先住民族（Masyarakat Adat）の土地主権を認めました。環境保全の最前線には、常に先住民族の伝統知（kearifan lokal）が存在しているのです。"
        }
    },
    {
        "filename": "docs/lexicon/36-tech-collocations-digital.md",
        "title": "【共起連語】IT技術・デジタルの必須コロケーション辞典：keamanan siber / kecerdasan buatan / komputasi awan",
        "root": "digital",
        "meaning": "デジタル、IT技術、人工知能、サイバー空間、クラウド",
        "core_concept": "世界屈指のデジタル人口とユニコーン企業を誇るインドネシアの「IT・テクノロジー産業（Teknologi Informasi）」において、サイバーセキュリティ、人工知能（AI）、クラウドコンピューティング、データベース、サイバー攻撃など、最先端のデジタル経済を牽引する必須コロケーションを整理します。",
        "table_rows": [
            ("keamanan siber", "サイバーの安全", "サイバーセキュリティ、情報セキュリティ", "IT/防衛", "Pemerintah memperkuat sistem keamanan siber nasional untuk melindungi pusat data strategis."),
            ("kecerdasan buatan (AI)", "人工の知能", "人工知能（Artificial Intelligence）、AI技術", "先端技術/産業", "Pemanfaatan kecerdasan buatan mampu meningkatkan efisiensi diagnosis medis di rumah sakit modern."),
            ("komputasi awan", "雲の計算", "クラウドコンピューティング（Cloud Computing）", "インフラ/IT", "Banyak perusahaan bermigrasi ke komputasi awan demi menghemat biaya pemeliharaan server fisik."),
            ("basis data (database)", "データの基地", "データベース、データ基盤、データバンク", "システム/開発", "Perlindungan privasi pengguna dalam basis data kependudukan harus diatur secara ketat oleh hukum."),
            ("serangan siber", "サイバーの攻撃", "サイバー攻撃、ハッキング、ランサムウェア攻撃", "犯罪/セキュリティ", "Layanan perbankan sempat terganggu selama beberapa jam akibat serangan siber berbahaya."),
            ("transformasi digital", "デジタルの変容", "デジタルトランスフォーメーション（DX）、IT化", "企業改革/国家", "Sektor perbankan memimpin transformasi digital dengan meluncurkan aplikasi perbankan serba bisa."),
            ("pusat data nasional (PDN)", "国家のデータセンター", "国家データセンター、政府共通クラウド基盤", "行政DX/インフラ", "Pembangunan Pusat Data Nasional bertujuan mengintegrasikan ribuan aplikasi layanan publik pemerintah.")
        ],
        "details": [
            {
                "term": "keamanan siber nasional (Badan Siber dan Sandi Negara / BSSN)",
                "trans": "国家サイバーセキュリティ、情報防衛体制",
                "nuance": "国家暗号庁（BSSN）や重要インフラ、金融機関が、重要データ流出やハッキングからサイバー空間を防衛する安全保障の最前線です。",
                "ex_id": "Undang-Undang Perlindungan Data Pribadi (UU PDP) mewajibkan pengendali data memperkuat arsitektur keamanan siber.",
                "ex_kana": "ウンダンウンダン プルリンドゥンガン ダタ プリバディ ムワジブカン プンゲンダリ ダタ ムムプルクアット アルシテクトゥル クアマナン スィベル",
                "ex_ja": "個人データ保護法（UU PDP）は、データ管理者に対してサイバーセキュリティ（keamanan siber）のアーキテクチャ強化を義務付けています。",
                "note": "法制化された最重要コンプライアンス分野です。"
            },
            {
                "term": "kecerdasan buatan generatif (Generative AI)",
                "trans": "生成AI、人工知能テクノロジー",
                "nuance": "文章作成、翻訳、プログラミング、デザインなどを自動生成する先端AI技術を指し、教育や産業界での活用と倫理的規制（etika AI）が議論されています。",
                "ex_id": "Adopsi kecerdasan buatan dalam kurikulum universitas bertujuan membekali mahasiswa dengan keterampilan masa depan.",
                "ex_kana": "アドプスィ クチェルダサン ブアタン ダラム クリクルム ウニヴェルシタス ブルトゥジュアン ムムブカリ マハシスワ ドゥンガン クトゥランピラン マサ ドゥパン",
                "ex_ja": "大学カリキュラムへの人工知能（kecerdasan buatan）の導入は、学生たちに未来のスキルを身につけさせることを目的としています。",
                "note": "技術・教育記事の最先端バズワードです。"
            },
            {
                "term": "komputasi awan terdistribusi (Cloud computing)",
                "trans": "クラウドコンピューティング、分散クラウド基盤",
                "nuance": "自前で高価なオンプレミスサーバーを保有せず、Google CloudやAWSなどの堅牢なクラウドインフラを利用してスケーラブルに開発・運用する現代ITの標準方式です。",
                "ex_id": "Startup e-commerce ini mengandalkan komputasi awan elastis untuk menangani lonjakan transaksi pesta belanja online.",
                "ex_kana": "スタートアップ エコマース イニ ムンガンダルカン コンプタスィ アワン エラスティス ウントゥッ ムナンガニ ロンジャカン トランサクスィ ペスタ ブランジャ オンライン",
                "ex_ja": "そのECスタートアップは、オンラインショッピング祭の取引急増に対応するため、柔軟なクラウドコンピューティング（komputasi awan）に依拠しています。",
                "note": "英語の直訳「雲（awan）の計算（komputasi）」として定着しました。"
            },
            {
                "term": "serangan siber ransomware",
                "trans": "ランサムウェアによるサイバー攻撃（身代金要求型攻撃）",
                "nuance": "国家データセンター（PDN）や大手銀行の基幹システムを暗号化して人質に取る悪質なサイバーテロ事件を指し、社会問題化しています。",
                "ex_id": "Insiden serangan siber terhadap infrastruktur vital pemerintah memicu evaluasi menyeluruh atas prosedur enkripsi data.",
                "ex_kana": "インスィデン スランガン スィベル トゥルハダップ インフラストルクトゥル ヴィタル プムリンター ムミチュ エヴァルアスィ ムニュルルー アタス プロセドゥル エンクリプスィ ダタ",
                "ex_ja": "政府重要インフラに対するサイバー攻撃（serangan siber）インシデントは、データ暗号化手順の全面的な見直しを引き起こしました。",
                "note": "危機管理報道の最頻出語彙です。"
            },
            {
                "term": "transformasi digital layanan publik",
                "trans": "公共行政サービスのデジタルトランスフォーメーション（DX）",
                "nuance": "窓口での手書き申請や住民票取得を廃止し、アプリ一つで行政手続きが完結するスマートシティ（kota pintar）や電子政府（e-Government）化の潮流です。",
                "ex_id": "Transformasi digital perizinan usaha terbukti memangkas birokrasi dan menutup celah pungutan liar.",
                "ex_kana": "トランストルマスィ ディジタール プリジナナン ウサハ トゥルブクティ ムマンカス ビロクラシ ダン ムヌトゥップ チェラー プングタン リアル",
                "ex_ja": "事業許認可のデジタルトランスフォーメーション（transformasi digital）は、官僚的手続きを削減し不当な不法徴収（pungli）の温床を塞いだことが証明されました。",
                "note": "行政改革の重要スローガンです。"
            }
        ],
        "dialogue": {
            "title": "銀行の基幹システム刷新とサイバー防御",
            "lines": [
                ("CTO", "Bagaimana progres migrasi sistem perbankan inti kita ke komputasi awan, Arya?"),
                ("IT Security Lead", "Berjalan lancar, Pak. Kami telah mengimplementasikan arsitektur keamanan siber berlapis untuk melindungi basis data nasabah."),
                ("CTO", "Pastikan sistem kecerdasan buatan pendeteksi fraud juga terintegrasi secara real-time."),
                ("IT Security Lead", "Tentu, Pak. Sistem otomatis ini dirancang agar mampu memitigasi serangan siber seketika sebelum merusak jaringan.")
            ],
            "trans": [
                ("CTO（最高技術責任者）", "勘定系基幹システムのクラウドコンピューティング（komputasi awan）への移行進捗はどうだい、アルヤ君？"),
                ("セキュリティ責任者", "順調です。顧客データベース（basis data）を防護するため、多層防御のサイバーセキュリティ（keamanan siber）アーキテクチャを実装いたしました。"),
                ("CTO", "不正検知のための人工知能（kecerdasan buatan）システムもリアルタイムで統合されているか確認してくれ。"),
                ("セキュリティ責任者", "もちろんです。ネットワークに被害が出る前にサイバー攻撃（serangan siber）を即座に緩和できるよう自動設計されております。")
            ]
        },
        "grammar_points": [
            "**siber の定着と接頭辞的用法**: 英語の `cyber` はオランダ語風綴りではなく英語直輸入の `siber`（スィベル）としてインドネシア語正書法に組み込まれ、`keamanan siber`（サイバーセキュリティ）、`ruang siber`（サイバー空間）、`kejahatan siber`（サイバー犯罪）と強固に共起します。",
            "**komputasi awan の直訳造語**: 英語の `Cloud Computing` を「komputasi（計算）」＋「awan（雲）」と直訳して借用した、インドネシア語の標準化言語政策（Badan Bahasa）の成功例の一つです。"
        ],
        "quizzes": [
            {
                "q": "現代のIT産業や国家防衛において「情報セキュリティ・サイバーセキュリティ」を表す正式な用語はどれか。",
                "choices": ["keamanan siber", "komputasi awan", "kecerdasan buatan", "basis data"],
                "ans": "keamanan siber",
                "expl": "サイバーセキュリティは `keamanan siber` です。"
            },
            {
                "q": "英語の Artificial Intelligence (AI) に相当する正式なインドネシア語はどれか。",
                "choices": ["kecerdasan buatan", "komputasi awan", "transformasi digital", "serangan siber"],
                "ans": "kecerdasan buatan",
                "expl": "人工知能は `kecerdasan buatan`（人工の知能）です。"
            },
            {
                "q": "物理サーバーを自前で保有せず、インターネット経由でリソースを利用する「クラウドコンピューティング」はどれか。",
                "choices": ["komputasi awan", "basis data", "pusat data", "jaringan lokal"],
                "ans": "komputasi awan",
                "expl": "クラウドコンピューティングは `komputasi awan` です。"
            }
        ],
        "culture_column": {
            "title": "「QRIS」と世界をリードするインドネシアのフィンテック革命",
            "body": "インドネシアの日常を劇的に変えたのが、中央銀行が主導した全国統一QRコード決済規格「QRIS（クリス: Quick Response Code Indonesian Standard）」です。高級ショッピングモールから道端の屋台（kaki lima）や寺院のお賽銭に至るまで、誰もがスマホ一つで即座にキャッシュレス決済を行います。銀行口座を持たない層（unbanked）を一気にデジタル経済圏へ包摂した、東南アジア随一のフィンテックの奇跡です。"
        }
    },
    {
        "filename": "docs/lexicon/37-health-collocations-medical.md",
        "title": "【共起連語】医療健康・診察の必須コロケーション辞典：tekanan darah / resep dokter / rawat inap / efek samping",
        "root": "kesehatan",
        "meaning": "健康、医療、病院、診察、投薬、保険",
        "core_concept": "病の治療と国民のウェルビーイングを支える「医療・ヘルスケア（Kesehatan & Medis）」において、血圧測定、医師の処方箋、入院治療、薬の副作用、カルテ管理など、病院受診や健康管理で欠かせない必須コロケーションを網羅します。",
        "table_rows": [
            ("tekanan darah", "血の圧力", "血圧（tekanan darah tinggi: 高血圧 / hipertensi）", "診察/生理", "Perawat mengukur tekanan darah dan suhu tubuh pasien sebelum pemeriksaan dokter."),
            ("resep dokter", "医師のレシピ", "処方箋、医師の処方薬指示書", "薬局/調剤", "Obat antibiotik keras ini hanya dapat dibeli di apotek dengan menggunakan resep dokter."),
            ("rawat inap", "宿泊の看護", "入院治療、入院（対義語: rawat jalan 通院外来）", "病院/治療", "Pasien demam berdarah tersebut memerlukan rawat inap intensif selama beberapa hari."),
            ("efek samping", "横の効果", "副作用、副次的悪影響（adverse effect）", "薬学/安全性", "Dokter menjelaskan kemungkinan efek samping obat seperti rasa kantuk dan mual."),
            ("rekam medis", "医療の記録", "カルテ、診療録、医療記録（medical record）", "病院/情報", "Kerahasiaan isi rekam medis pasien dijamin dan dilindungi secara ketat oleh undang-undang."),
            ("rujuk ke rumah sakit", "病院へ照会する", "専門病院へ紹介する、転院搬送する（surat rujukan）", "医療制度/BPJS", "Puskesmas memberikan surat rujukan agar pasien dapat diperiksa di rumah sakit umum daerah."),
            ("jaminan kesehatan nasional (BPJS Kesehatan)", "国民健康保障", "国民健康保険（BPJS健康保険システム）", "社会保障/皆保険", "Program BPJS Kesehatan menjamin akses pengobatan gratis bagi jutaan warga prasejahtera.")
        ],
        "details": [
            {
                "term": "rawat inap vs rawat jalan (inpatient vs outpatient)",
                "trans": "入院（入院治療） vs 通院（外来診療）",
                "nuance": "病院医療の基本区分です。ベッドに宿泊して24時間看護を受けるのが `rawat inap`（inap＝宿泊）、診察後に帰宅するのが `rawat jalan`（jalan＝歩く/通う）です。",
                "ex_id": "Fasilitas kamar rawat inap kelas satu di rumah sakit rujukan ini sudah penuh terisi pasien flu.",
                "ex_kana": "ファスィリタス カマル ラワット イナップ クラス サトゥ ディ ルマー サキット ルジュカン イニ スダ プヌー トゥルスィ パスィエン フル",
                "ex_ja": "この紹介先総合病院の一等入院病室（rawat inap）施設は、インフルエンザ患者ですでに満室となっています。",
                "note": "医療保険請求の最重要区分項目です。"
            },
            {
                "term": "menebus resep dokter di apotek",
                "trans": "薬局で医師の処方箋の薬を受け取る（調剤してもらう）",
                "nuance": "医師から渡された処方箋（resep）を街の薬局（apotek）に持ち込み、代金を払って調剤された薬を受け取る一連の行為を動詞 `menebus`（買い戻す・清算する）で表します。",
                "ex_id": "Setelah berkonsultasi dengan dokter spesialis anak, ayah bergegas menebus resep obat di apotek 24 jam.",
                "ex_kana": "ステラ ブルコンスルタスィ ドゥンガン ドクテル スペシアリス アナッ、アヤフ ブルゲガス ムヌブス レセップ オバット ディ アポテック ドゥアプルウンパット ジャム",
                "ex_ja": "小児科専門医との診察を終えた後、父親は24時間営業の薬局で処方箋の薬を受け取りに（menebus resep）急ぎました。",
                "note": "`menebus resep`（処方薬を引き取る）は決まり文句です。"
            },
            {
                "term": "efek samping yang merugikan",
                "trans": "有害な副作用、好ましくない薬の副反応",
                "nuance": "主たる薬効（khasiat utama）の裏で生じる眠気、吐き気、アレルギー反応など、服用にあたって注意を要する身体的リスクを指します。",
                "ex_id": "Ibu hamil dilarang mengonsumsi sembarang jamu herbal tanpa petunjuk medis karena risiko efek samping.",
                "ex_kana": "イブ ハミル ディララン ムンゴンソゥムスィ スムバラン ジャム ヘルバル タンパ プトゥンジュッ メディス カレナ リスィコ エフェッ サンピン",
                "ex_ja": "妊婦は副作用（efek samping）のリスクがあるため、医師の指示なしに生薬ジャムーをむやみに服用してはなりません。",
                "note": "`tanpa efek samping`（副作用なし）は健康食品の惹句です。"
            },
            {
                "term": "surat rujukan BPJS (sistem rujukan berjenjang)",
                "trans": "BPJS健康保険の診療紹介状（階層的紹介システム）",
                "nuance": "国民皆保険（BPJS Kesehatan）において、まず地域の診療所（Puskesmas / Klinik Faskes 1）を受診し、そこから大病院へ紹介してもらうための必須書類です。",
                "ex_id": "Pasien harus membawa kartu BPJS aktif dan surat rujukan dari faskes pertama untuk berobat ke rumah sakit.",
                "ex_kana": "パスィエン ハルス ムンバワ カルトゥ ベーページェーエス アクティフ ダン スラット ルジュカン ダリ ファスケス プルタマ ウントゥッ ブルオバット ケ ルマー サキット",
                "ex_ja": "患者は総合病院で受診するため、有効なBPJSカードと一次医療機関からの紹介状（surat rujukan）を持参しなければなりません。",
                "note": "インドネシアの公的医療受診の必須ルールです。"
            },
            {
                "term": "menjaga tekanan darah tetap stabil",
                "trans": "血圧を正常かつ安定した状態に保つ",
                "nuance": "食生活の改善、減塩、定期的な運動を通じて高血圧症（hipertensi）や脳卒中を予防する日常ヘルスケアの基本目標です。",
                "ex_id": "Pola makan rendah garam dan olahraga teratur sangat dianjurkan untuk menjaga tekanan darah penderita jantung.",
                "ex_kana": "ポラ マカン ルンダー ガラム ダン オラフラガ トゥラトゥル サンガット ディアンジュルカン ウントゥッ ムンジャガ トゥカナン ダラー プンドゥリタ ジャンツン",
                "ex_ja": "心臓病患者の血圧（tekanan darah）を安定維持するため、減塩食と適度な運動が強く推奨されています。",
                "note": "`tekanan darah tinggi`（高血圧）は国民病の一つです。"
            }
        ],
        "dialogue": {
            "title": "クリニックでの問診と大病院への紹介",
            "lines": [
                ("Dokter", "Hasil pemeriksaan menunjukkan tekanan darah Ibu cukup tinggi dan ada gejala tifus."),
                ("Ibu Rina", "Aduh, apakah kondisi saya cukup parah, Dok? Apakah harus rawat inap?"),
                ("Dokter", "Iya, untuk menghindari dehidrasi, saya terbitkan surat rujukan rawat inap ke rumah sakit umum."),
                ("Ibu Rina", "Baik, Dok. Apakah obat yang dokter resepkan ini aman dan tidak menimbulkan efek samping mual?")
            ],
            "trans": [
                ("医師", "検査の結果、奥様の血圧（tekanan darah）がかなり高く、腸チフスの症状が見られます。"),
                ("リナさん", "まあ、そんなに重い状態なのでしょうか、先生？入院治療（rawat inap）が必要ですか？"),
                ("医師", "ええ、脱水を防ぐため、公立総合病院への入院紹介状（surat rujukan rawat inap）を発行いたします。"),
                ("リナさん", "わかりました、先生。処方していただくこの薬は安全で、吐き気の副作用（efek samping）はありませんか？")
            ]
        },
        "grammar_points": [
            "**inap と jalan の対立**: `menginap`（宿泊する）から派生した `rawat inap`（入院）と、歩いて帰る `rawat jalan`（通院外来）という、身体の動作動詞を基にした名詞連語の対比が明快です。",
            "**menebus resep の語義**: `tebus`（身代金を払う・質受けする・買い戻す）という動詞が、処方箋を出して調剤薬を受け取る行為に特化して使われるのは、インドネシア語独特の商習慣コロケーションです。"
        ],
        "quizzes": [
            {
                "q": "病院で患者がベッドに宿泊して24時間の医療看護を受ける「入院治療」の正式なインドネシア語はどれか。",
                "choices": ["rawat inap", "rawat jalan", "resep dokter", "rekam medis"],
                "ans": "rawat inap",
                "expl": "入院は `rawat inap` です（通院外来は `rawat jalan`）。"
            },
            {
                "q": "薬を服用した際に現れる、主たる薬効以外の望ましくない「副作用」を表す連語はどれか。",
                "choices": ["efek samping", "tekanan darah", "surat rujukan", "badan hukum"],
                "ans": "efek samping",
                "expl": "副作用は `efek samping` です。"
            },
            {
                "q": "診察後に薬局（Apotek）に処方箋を持ち込み、「調剤薬を正式に買い受ける・引き取る」を表す動詞句はどれか。",
                "choices": ["menebus resep dokter", "membuat janji temu", "mengajukan gugatan", "mencari jalan keluar"],
                "ans": "menebus resep dokter",
                "expl": "処方箋の薬を受け取る・引き取るは `menebus resep dokter` です。"
            }
        ],
        "culture_column": {
            "title": "「Jamu」と近代西洋医学のハイブリッド共生",
            "body": "インドネシアでは近代病院の西洋医学（medis barat）が普及した現代でも、ウコン（kunyit）やショウガ（jahe）、ジャワショウガ（temulawak）などの薬草を煎じた伝統生薬「ジャムー（Jamu）」が国民の健康維持に深く浸透しています。ちょっとした風邪や体調不良なら、病院へ行く前に屋台のジャムー売り（tukang jamu gendong）で苦いハーブを飲み干して身体を温めるという、伝統と科学の豊かな共存文化が息づいています。"
        }
    },
    {
        "filename": "docs/lexicon/38-academic-collocations-research.md",
        "title": "【共起連語】学術論文・研究の必須コロケーション辞典：metodologi penelitian / kerangka berpikir / uji hipotesis",
        "root": "akademik",
        "meaning": "学術、論文執筆、研究調査、仮説検証、先行研究",
        "core_concept": "大学院や研究所における知の探求「学術研究＆論文執筆（Penelitian Ilmiah & Skripsi）」において、研究方法論、論理的思考の枠組み、仮説検定、先行研究レビュー、データ分析など、格調高いアカデミック・ライティングに不可欠な必須コロケーションを整理します。",
        "table_rows": [
            ("metodologi penelitian", "研究の方法論", "研究方法論、リサーチ・メソドロジー（定量・定性）", "学術/手法", "Bab tiga skripsi ini menguraikan metodologi penelitian kuantitatif yang digunakan."),
            ("kerangka berpikir", "思考の骨組み", "理論的枠組み、思考フレームワーク、概念図", "理論/論文", "Penulis menyusun kerangka berpikir yang menghubungkan variabel bebas dan terikat."),
            ("uji hipotesis", "仮説のテスト", "仮説検定、仮説の検証（t-test, ANOVA等）", "統計/分析", "Hasil uji hipotesis menunjukkan adanya pengaruh signifikan antara kedua variabel."),
            ("tinjauan pustaka", "文献の展望", "先行研究レビュー、文献検討、文献考証（literature review）", "論文/基礎", "Tinjauan pustaka yang komprehensif diperlukan untuk memetakan kebaruan riset (novelty)."),
            ("analisis data", "データの分析", "データ分析、統計解析、質的分析", "手法/解釈", "Proses analisis data dibantu menggunakan perangkat lunak statistik versi terbaru."),
            ("daftar pustaka", "文献の目録", "参考文献一覧、文献リスト（bibliografi）", "体裁/引用", "Semua sumber kutipan harus dicantumkan secara konsisten dalam daftar pustaka."),
            ("kebaruan penelitian (novelty)", "研究の新しさ", "研究の新規性、独創性、オリジナリティ", "査読/学術", "Dewan penguji mempertanyakan kebaruan penelitian ini dibanding disertasi terdahulu.")
        ],
        "details": [
            {
                "term": "metodologi penelitian kualitatif / kuantitatif",
                "trans": "質的 / 量的研究方法論",
                "nuance": "学術論文（skripsi / tesis / disertasi）の第3章（Bab III）で必ず詳述される、データ収集法、標本抽出（sampling）、妥当性信頼性検証の科学的プロトコルです。",
                "ex_id": "Penelitian ini menerapkan metodologi penelitian kualitatif dengan pendekatan studi kasus mendalam.",
                "ex_kana": "プヌリティアン イニ ムヌラップカン メトドロギ プヌリティアン クアリタティフ ドゥンガン プンデカタン スツディ カスス ムンダラム",
                "ex_ja": "本研究は、詳細なケーススタディ（事例研究）アプローチによる質的研究方法論（metodologi penelitian kualitatif）を適用しています。",
                "note": "学位論文の成否を分ける基幹章です。"
            },
            {
                "term": "kerangka berpikir teoritis (conceptual framework)",
                "trans": "理論的思考の枠組み、概念フレームワーク",
                "nuance": "先行研究や確立された学説に基づいて、研究対象となる複数の変数（variabel）がどのような因果関係や相関関係で結びついているかを明示した論理構造図です。",
                "ex_id": "Berdasarkan kerangka berpikir yang dibangun, kepemimpinan transformasional dihipotesiskan mempengaruhi kinerja guru.",
                "ex_kana": "ブルダサルカン クランカ ブルピキル ヤン ディバングン、クプミンピナン トランスフォルマシオナル ディヒポテスィスカン ムムパンガルヒ キネルジャ グル",
                "ex_ja": "構築された思考の枠組み（kerangka berpikir）に基づき、変革的リーダーシップは教師の業績に影響を与えると仮説立てられます。",
                "note": "論文第2章の総括としてダイアグラム化されます。"
            },
            {
                "term": "menguji hipotesis secara statistik",
                "trans": "仮説を統計学的に検証・検定する",
                "nuance": "収集した実証データに対し、回帰分析や検定手法を適用して、帰無仮説（H0）を棄却し対立仮説（H1）を有意水準（p < 0.05）で採択する実証プロセスの核心です。",
                "ex_id": "Uji hipotesis dilakukan dengan uji regresi linear berganda untuk mengukur tingkat signifikansi.",
                "ex_kana": "ウジ ヒポテスィス ディラクカン ドゥンガン ウジ レグレシ リネアル ブルガンダ ウントゥッ ムングクル ティンカット スィグニフィカンシ",
                "ex_ja": "有意水準を測定するため、重回帰分析によって仮説検定（uji hipotesis）が実施されました。",
                "note": "動詞句 `menguji hipotesis` としても頻出します。"
            },
            {
                "term": "tinjauan pustaka / kajian pustaka (literature review)",
                "trans": "先行研究検討、文献レビュー、先行研究考証",
                "nuance": "自らの研究が車輪の再発明（reinventing the wheel）にならないよう、国内外の最新学術誌（jurnal terakreditasi）の論文を批判的に精読・整理する論文第2章の根幹です。",
                "ex_id": "Dalam tinjauan pustaka, peneliti merangkum perkembangan teori keadilan distributif dari masa ke masa.",
                "ex_kana": "ダラム ティンジャウアン プスタカ、プヌリティ ムランゴム プンゲムバンガン テオリ クアディラン ディストリブティフ ダリ マサ ケ マサ",
                "ex_ja": "先行研究レビュー（tinjauan pustaka）において、研究者は配分的正義論の時代ごとの理論的変遷を要約しました。",
                "note": "`kajian literatur` とも呼ばれます。"
            },
            {
                "term": "menemukan kebaruan penelitian (novelty)",
                "trans": "研究の新規性（独創性・オリジナリティ）を提示する",
                "nuance": "修士論文（tesis）や博士論文（disertasi）の学術審査（sidang ujian）において、これまでの学界に存在しなかった新たな発見や視点を示せているかを問う最重要の評価基準です。",
                "ex_id": "Kebaruan penelitian ini terletak pada integrasi kearifan lokal suku Sasak ke dalam kurikulum sains modern.",
                "ex_kana": "クバルアン プヌリティアン イニ トゥルレタッ パダ インテグラシ ケアリファン ロカル スク ササッ ケ ダラム クリクルム サインス モデルン",
                "ex_ja": "本研究の新規性（kebaruan penelitian）は、ササク族の伝統的知恵を現代科学教育カリキュラムへと統合した点にあります。",
                "note": "査読付き学術誌掲載の必須要件です。"
            }
        ],
        "dialogue": {
            "title": "修士論文の口頭試問（Sidang Skripsi/Tesis）前の指導",
            "lines": [
                ("Dosen Pembimbing", "Tinjauan pustakamu sudah sangat kaya, Rudi, tetapi bagaimana dengan kerangka berpikirnya?"),
                ("Rudi", "Sudah saya perjelas dalam diagram di bab dua, Prof. Hubungan antarvariabelnya kini lebih logis."),
                ("Dosen Pembimbing", "Bagus. Pastikan dalam sidang besok kamu bisa mempertahankan kebaruan penelitianmu di hadapan dewan penguji."),
                ("Rudi", "Siap, Prof. Saya juga telah menyiapkan bukti komputasi dari seluruh uji hipotesis statistik saya.")
            ],
            "trans": [
                ("指導教授", "先行研究レビュー（tinjauan pustaka）は極めて充実しているよルディ君、しかし思考の枠組み（kerangka berpikir）の整理はどうかな？"),
                ("ルディ", "第2章のダイアグラムで明確に整理いたしました、教授。変数間の関係性がより論理的になりました。"),
                ("指導教授", "結構。明日の口頭試問では、審査委員会の前で君の研究の新規性（kebaruan penelitian）をしっかり主張・論証できるようにしたまえ。"),
                ("ルディ", "承知いたしました、教授。全統計的仮説検定（uji hipotesis）の計算ログも完全に準備しております。")
            ]
        },
        "grammar_points": [
            "**pustaka による学術複合語**: サンスクリット語由来の `pustaka`（書物・典籍）は、`perpustakaan`（図書館）、`daftar pustaka`（参考文献リスト）、`tinjauan pustaka`（先行研究レビュー）など、学術文献に関わる最高位の用語を形成します。",
            "**tinjauan の接辞構造**: 動詞語根 `tinjau`（見渡す・展望する）に名詞接尾辞 `-an` が付いた `tinjauan` は、「鳥瞰的展望・包括的考察」を意味し、学術論文の標題で多用されます。"
        ],
        "quizzes": [
            {
                "q": "学術論文で、データ収集法や標本抽出プロトコルを科学的に体系化した「研究方法論」を意味する用語はどれか。",
                "choices": ["metodologi penelitian", "kerangka berpikir", "daftar pustaka", "uji hipotesis"],
                "ans": "metodologi penelitian",
                "expl": "研究方法論は `metodologi penelitian` です。"
            },
            {
                "q": "論文第2章で、先行研究を網羅的にレビュー・考証する「先行研究検討」を表す正式な用語はどれか。",
                "choices": ["tinjauan pustaka", "arus kas operasional", "tanda tangan kontrak", "saksi kunci"],
                "ans": "tinjauan pustaka",
                "expl": "先行研究レビューは `tinjauan pustaka`（または `kajian pustaka`）です。"
            },
            {
                "q": "統計データ分析を用いて「設定した理論的仮説を検証・検定する」プロセスを表す連語はどれか。",
                "choices": ["uji hipotesis", "uji coba", "tahan uji", "uji nyali"],
                "ans": "uji hipotesis",
                "expl": "仮説検定・検証は `uji hipotesis` です。"
            }
        ],
        "culture_column": {
            "title": "「Sidang Skripsi」とインドネシアの卒業試問儀礼",
            "body": "インドネシアの大学を卒業する上で、学生にとって人生最大の試練であり通過儀礼となるのが「スィダン・スクリプスィ（Sidang Skripsi: 卒業論文口頭試問）」です。黒いスーツにネクタイを締め、複数の厳格な審査教授（dosen penguji）の鋭い質問攻めを何時間も耐え抜いて合格を勝ち取った瞬間、キャンパスの中庭で友人たちから花束やタスキ（selempang gelar）を贈られて祝福される光景は、家族全員の誇りとなる感動的な風物詩です。"
        }
    },
    {
        "filename": "docs/lexicon/39-culture-collocations-tradition.md",
        "title": "【共起連語】伝統文化・儀礼の必須コロケーション辞典：upacara adat / warisan leluhur / nilai luhur / kearifan lokal",
        "root": "budaya",
        "meaning": "文化、伝統儀礼、先祖の遺産、土着の知恵、高貴な価値観",
        "core_concept": "300を超える民族が織りなす「インドネシアの伝統文化＆慣習（Kebudayaan & Adat Istiadat）」において、伝統儀式、祖先の遺産、高貴な道徳的価値観、地域に伝わる土着の知恵（kearifan lokal）など、文化論や民俗紀行を深く味わうための必須コロケーションを整理します。",
        "table_rows": [
            ("upacara adat", "慣習の式典", "伝統儀礼、慣習儀式、伝統的祭礼", "民俗/宗教", "Upacara adat Rambu Solo di Toraja menarik ribuan wisatawan mancanegara setiap tahun."),
            ("warisan leluhur", "先祖の遺産", "祖先の遺産、先祖伝来の文化遺産", "歴史/アイデンティティ", "Kain tenun ikat bernilai seni tinggi ini merupakan warisan leluhur yang harus dilestarikan."),
            ("nilai luhur", "気高い価値", "高尚な精神的価値観、崇高な徳目、道徳規範", "哲学/教育", "Nilai luhur gotong royong terbukti menjadi perekat persatuan bangsa dalam menghadapi krisis."),
            ("kearifan lokal", "地域の知恵", "伝統的土着の知恵、地域社会の知恵（local wisdom）", "環境/文化人類学", "Masyarakat adat Baduy menerapkan kearifan lokal dalam menjaga kelestarian hutan mata air."),
            ("norma masyarakat", "社会の規範", "社会規範、世間の道徳的ルール、良識", "社会学/倫理", "Tindakan amoral tersebut dikecam keras karena bertentangan dengan norma masyarakat setempat."),
            ("warisan budaya takbenda", "無形の文化遺産", "無形文化遺産（UNESCO Intangible Cultural Heritage）", "国際/文化財", "Wayang kulit dan keris telah diakui oleh UNESCO sebagai warisan budaya takbenda dunia."),
            ("hukum adat", "慣習の法", "慣習法（Adat Law）、伝統的法規範", "法制/人類学", "Di beberapa wilayah kepulauan, sengketa tanah warisan masih diselesaikan melalui hukum adat.")
        ],
        "details": [
            {
                "term": "upacara adat (ritual kebudayaan tradisional)",
                "trans": "伝統儀礼、伝統的慣習儀式",
                "nuance": "誕生、成人、婚姻、葬儀（Rambu Soloなど）、収穫祭（Sedekah Bumi）など、人生の節目や季節の循環に神仏や先祖の霊を祀り、共同体の絆を確かめ合う神聖な儀礼です。",
                "ex_id": "Upacara adat Seren Taun digelar oleh masyarakat agraris Sunda sebagai wujud rasa syukur atas hasil panen padi.",
                "ex_kana": "ウパチャラ アダット スレン タウン ディゲラール オレ マシャラカット アグラリス スンダ スバガイ ウジュッド ラサ シュクル アタス ハシル パネン パディ",
                "ex_ja": "スンダの農耕共同体によって開催される伝統儀礼「スレン・タウン（Seren Taun）」は、稲の収穫に対する感謝の表れです。",
                "note": "民族ごとに固有の名称と儀礼手順を持ちます。"
            },
            {
                "term": "warisan leluhur yang tak ternilai harganya",
                "trans": "計り知れない価値を持つ祖先伝来の遺産",
                "nuance": "古代寺院建築（ボロブドゥールやプランバナン）、伝統舞踊、影絵芝居、バティック染色の手仕事など、何百年も前に先祖たちが創造した比類なき文化遺産への崇敬を表します。",
                "ex_id": "Generasi muda memiliki tanggung jawab moral untuk merawat warisan leluhur agar tidak punah ditelan zaman.",
                "ex_kana": "ゲネラシ ムダ ムミリキ タングン ジャワブ モラル ウントゥッ ムラワット ワリサン ルルフール アガル ティダッ プナー ディトゥラン ザマン",
                "ex_ja": "若い世代は、祖先の遺産（warisan leluhur）が時代の波に呑まれて絶滅してしまわないよう保護する道徳的責任を負っています。",
                "note": "`melestarikan warisan leluhur`（祖先の遺産を保存継承する）が定石です。"
            },
            {
                "term": "kearifan lokal dalam mitigasi bencana (local wisdom)",
                "trans": "災害軽減や環境共生における土着の知恵",
                "nuance": "シムル島（Simeulue）住民に伝わる津波伝承「Smong」のように、近代科学機器が存在しない時代から自然の異変を読み解き、持続可能な共生を可能にしてきた先住民の叡智です。",
                "ex_id": "Pakar kebencanaan mempelajari kearifan lokal rumah adat panggung yang terbukti tahan guncangan gempa bumi.",
                "ex_kana": "パカール クベンチャナアン ムムパラジャリ ケアリファン ロカル ルマー アダット パングン ヤン トゥルブクティ タハン グンチャカン グムパ ブミ",
                "ex_ja": "防災の専門家たちは、地震の激しい揺れに耐えうることが実証されている高床式伝統家屋の土着の知恵（kearifan lokal）を研究しています。",
                "note": "環境・防災政策の最重要キーワードです。"
            },
            {
                "term": "nilai luhur gotong royong",
                "trans": "相互扶助（ゴトン・ロヨン）の高尚な精神的徳目",
                "nuance": "個人の利己的利益を超えて、村の道路普請や冠婚葬祭、災害復興において全員が無償で力を合わせる、インドネシア国民統合の魂と称される至高の価値観です。",
                "ex_id": "Pancasila mengkristalisasikan nilai-nilai luhur yang telah hidup dalam peradaban Nusantara ribuan tahun silam.",
                "ex_kana": "パンチャスィラ ムンクリスタリサスィカン ニライニライ ルルフール ヤン トゥラー ヒドゥップ ダラム プルアダバン ヌサンタラ リブアン タフン スラム",
                "ex_ja": "パンチャシラは、数千年前から群島文明の中に息づいてきた崇高な価値観（nilai luhur）を結晶化させたものです。",
                "note": "国家哲学教育の要語です。"
            },
            {
                "term": "warisan budaya takbenda UNESCO",
                "trans": "ユネスコ無形文化遺産（世界遺産）",
                "nuance": "バティック（Batik）、クリス（Keris）、ワヤン（Wayang）、アンクルン（Angklung）、ガムラン（Gamelan）など、ユネスコによって世界人類の宝として認定された伝統芸能・工芸です。",
                "ex_id": "Penetapan jamu sebagai warisan budaya takbenda dunia mempertegas posisi Indonesia sebagai episentrum herbal dunia.",
                "ex_kana": "プヌタパン ジャムー スバガイ ワリサン ブダヤ タッベンダ ドゥニア ムムプルトゥガス ポスィスィ インドネシア スバガイ エピセントルム ヘルバル ドゥニア",
                "ex_ja": "伝統生薬ジャムーのユネスコ無形文化遺産（warisan budaya takbenda）認定は、世界のハーブの中心地としてのインドネシアの地位を確立しました。",
                "note": "`takbenda` は「無形の」を意味します。"
            }
        ],
        "dialogue": {
            "title": "トラジャの伝統葬儀と文化遺産の継承",
            "lines": [
                ("Wisatawan", "Luar biasa megah dan sakral ya prosesi upacara adat Rambu Solo ini, Bli."),
                ("Pemandu Budaya", "Iya, upacara kematian ini adalah warisan leluhur suku Toraja yang sarat dengan nilai luhur penghormatan kepada orang tua."),
                ("Wisatawan", "Bagaimana masyarakat bisa mempertahankan tradisi yang begitu rumit di era modern?"),
                ("Pemandu Budaya", "Kuncinya adalah kearifan lokal dan hukum adat yang tetap ditaati secara gotong royong oleh seluruh rumpun keluarga.")
            ],
            "trans": [
                ("旅行者", "このトラジャの伝統葬儀「ランブ・ソロ（Rambu Solo）」の儀式行列（upacara adat）、息を呑むほど壮大で神聖ですね。"),
                ("文化ガイド", "ええ、この葬送儀礼は両親への敬愛という高貴な徳目（nilai luhur）に満ちた、トラジャ族の祖先の遺産（warisan leluhur）です。"),
                ("旅行者", "現代社会において、これほど複雑で壮大な伝統をどうやって維持できているのですか？"),
                ("文化ガイド", "鍵となるのは、一族全員が相互扶助（gotong royong）で遵守し続ける土着の知恵（kearifan lokal）と慣習法（hukum adat）ですよ。")
            ]
        },
        "grammar_points": [
            "**luhur による道徳的修飾**: `luhur`（気高い・高貴な）は、`nilai luhur`（高潔な徳目）、`budi pekerti luhur`（気品ある高潔な人格）、`leluhur`（祖先・先祖）と、道徳的・血統的高貴さを表す語彙群を形成します。",
            "**takbenda の接頭的否定**: `tak`（〜ない）＋ `benda`（物体・形ある物）＝ `takbenda`（無形の / intangible）。ユネスコ関連の文化行政用語として完全に定着しています。"
        ],
        "quizzes": [
            {
                "q": "各民族共同体で古くから執り行われている神聖な「伝統儀礼・慣習儀式」を表す連語はどれか。",
                "choices": ["upacara adat", "upacara bendera", "kampanye akbar", "tinjauan pustaka"],
                "ans": "upacara adat",
                "expl": "伝統儀礼は `upacara adat` です（`upacara bendera` は学校等の国旗掲揚式）。"
            },
            {
                "q": "何世代にもわたり地域社会に受け継がれてきた「土着の知恵・伝統的知恵（Local Wisdom）」を表す専門語はどれか。",
                "choices": ["kearifan lokal", "nilai luhur", "warisan leluhur", "hukum adat"],
                "ans": "kearifan lokal",
                "expl": "土着の知恵・伝統的叡智は `kearifan lokal` です。"
            },
            {
                "q": "バティックやワヤン、ガムランなど、ユネスコに認定された「無形文化遺産」の正式なインドネシア語名称はどれか。",
                "choices": ["warisan budaya takbenda", "cagar budaya fisik", "hukum adat ulayat", "adat istiadat"],
                "ans": "warisan budaya takbenda",
                "expl": "無形文化遺産は `warisan budaya takbenda` です。"
            }
        ],
        "culture_column": {
            "title": "「Gotong Royong」にみる群島文明の連帯哲学",
            "body": "独立宣言者スカルノが「パンチャシラの5つの原則をただ一つの言葉に要約するならば、それこそがゴトン・ロヨン（Gotong Royong）である」と演説したように、この相互扶助精神はインドネシア人の精神的背骨です。重い木造家屋を数百人で丸ごと持ち上げて引っ越す南スラウェシの「Mappalette Bola」や、水路を共同清掃するバリの「Subak」など、助け合いの連帯は今も生き生きと脈動しています。"
        }
    },
    {
        "filename": "docs/lexicon/40-daily-collocations-home.md",
        "title": "【共起連語】家庭生活・家事の必須コロケーション辞典：membersihkan rumah / memasak makanan / mencuci pakaian",
        "root": "rumahtangga",
        "meaning": "家庭生活、家事、掃除、炊事、洗濯、日用品買い出し",
        "core_concept": "人々の温かい生活の拠点である「家庭・家事（Kehidupan Rumah Tangga）」において、部屋の掃除、食事の調理、衣服の洗濯、月々の生活必需品買い出しなど、日々の暮らしを生き生きと語り合うための必須コロケーションを網羅します。",
        "table_rows": [
            ("membersihkan rumah", "家を清める", "家を掃除する、部屋を片付ける、大掃除する", "家事/生活", "Setiap akhir pekan, seluruh anggota keluarga bekerja bakti membersihkan rumah bersama."),
            ("memasak makanan", "食べ物を煮炊きする", "料理を作る、食事を自炊する、調理する", "台所/料理", "Ibu bangun pagi-pagi sekali untuk memasak makanan bergizi sebelum anak-anak berangkat sekolah."),
            ("mencuci pakaian", "衣服を洗う", "洗濯をする、服を手洗い・洗濯機で洗う", "洗濯/家事", "Mencuci pakaian berbahan sutra sebaiknya dilakukan secara manual tanpa mesin cuci."),
            ("belanja bulanan", "月ごとの買い物", "月々の買い出し、日用品・食料品のまとめ買い", "家計/消費", "Ibu rumah tangga berburu diskon di supermarket saat jadwal belanja bulanan tiba."),
            ("menyetrika baju", "服にアイロンをかける", "服にアイロンをかける、衣服のしわを伸ばす", "家事/身だしなみ", "Ia menyetel musik favorit agar tidak bosan saat menyetrika baju tumpukan cucian."),
            ("membuang sampah", "ゴミを捨てる", "ゴミ出しをする、ゴミを分別して捨てる", "衛生/環境", "Anak-anak dibiasakan sejak dini untuk membuang sampah pada tempatnya."),
            ("merapikan tempat tidur", "寝床を整える", "ベッドメイキングをする、布団を整える", "生活習慣/朝", "Langkah pertama untuk memulai hari yang produktif adalah merapikan tempat tidur sendiri.")
        ],
        "details": [
            {
                "term": "membersihkan rumah (bersih-bersih rumah secara menyeluruh)",
                "trans": "家を掃除する、部屋の片付けをする",
                "nuance": "床のモップ掛け（mengepel lantai）、埃払い（mengelap debu）、庭の手入れ（merawat halaman）を含め、家全体を清潔で快適な状態に保つ日常家事全般を指します。",
                "ex_id": "Menjelang hari raya Idulfitri, tradisi mengecat dinding dan membersihkan rumah selalu dilakukan warga.",
                "ex_kana": "ムンジュラン ハリ ラヤ イドゥルフィトリ、トラディスィ ムンゲチャット ディンディン ダン ムムブルスィフカン ルマー スラル ディラクカン ワルガ",
                "ex_ja": "レバラン大祭を前に、壁をペンキで塗り直し家を大掃除する（membersihkan rumah）習慣が常に住民によって行われます。",
                "note": "口語では `bersih-bersih rumah` とも言われます。"
            },
            {
                "term": "memasak makanan sehari-hari",
                "trans": "毎日の食事（料理）を作る、自炊する",
                "nuance": "台所（dapur）で食材を切り、ブンブ（調味料ペースト）を石臼（cobek）で擦り潰して炒め煮にする、東南アジアの香り豊かな手料理の営みです。",
                "ex_id": "Memasak makanan sendiri di rumah terbukti jauh lebih hemat dan terjamin kebersihannya dibanding jajan di luar.",
                "ex_kana": "ムマサッ マカナン スンディリ ディ ルマー トゥルブクティ ジャウ レビ ヘマット ダン トゥルジャミン クブルスィハンニャ ディバンディン ジャジャン ディ ルアル",
                "ex_ja": "家で自分で料理を作る（memasak makanan sendiri）ことは、外食をするよりも遥かに経済的で衛生面も保証されていることが証明されています。",
                "note": "`masakan rumah`（お袋の味・家庭料理）と共起します。"
            },
            {
                "term": "mencuci pakaian dan menjemur cucian",
                "trans": "洗濯をして洗濯物を天日干しする",
                "nuance": "南国の強い日差しの下で物干し竿（jemuran）に洗濯物を干す光景は、インドネシアの住宅街の典型的な日常風景です。",
                "ex_id": "Jangan mencuci pakaian saat langit mendung agar cucian tidak berbau apek akibat terlambat kering.",
                "ex_kana": "ジャンガン ムンチュチ パカイアン サアット ランギット ムンドゥン アガル チュチアン ティダッ ブルバウ アペッ アクバット トゥルランバット クリン",
                "ex_ja": "洗濯物が乾くのが遅れて生乾きの嫌な臭い（bau apek）がしないよう、曇り空の時には洗濯をして（mencuci pakaian）はなりません。",
                "note": "`bau apek`（生乾き臭）は日常頻出語です。"
            },
            {
                "term": "belanja bulanan kebutuhan pokok",
                "trans": "月々のまとめ買い、日用品・基礎食料品の買い出し",
                "nuance": "毎月の給料日（hari gajian）直後に、米、食用油、砂糖、洗剤、トイレットペーパーなどの生活必需品（sembako）をスーパーで一括購入する家計管理イベントです。",
                "ex_id": "Ibu mencatat daftar belanja bulanan secara rinci agar tidak tergoda membeli barang diskon yang tidak diperlukan.",
                "ex_kana": "イブ ムンチャタット ダフタル ブランジャ ブランナン スチャラ リンチ アガル ティダッ トゥルゴダ ムンベリ バラン ディスコン ヤン ティダッ ディプルルカン",
                "ex_ja": "母親は、必要のないセール品を買う誘惑に負けないよう、月々の買い出しリスト（belanja bulanan）を詳細にメモしました。",
                "note": "家計簿（anggaran belanja）と直結します。"
            },
            {
                "term": "merapikan tempat tidur setiap pagi",
                "trans": "毎朝ベッドメイキングをする、布団を整える",
                "nuance": "シーツのしわを伸ばし、枕（bantal）と抱き枕（guling）を所定の位置に美しく並べる、規律ある生活習慣の第一歩です。",
                "ex_id": "Kebiasaan sederhana seperti merapikan tempat tidur setelah bangun tidur melatih kedisiplinan mental anak.",
                "ex_kana": "クビアサアン スデルハナ スプルティ ムラピカン トゥムパット ティドゥル ステラ バングン ティドゥル ムラティ クディスィプリナン メンタル アナッ",
                "ex_ja": "起床後にベッドを整える（merapikan tempat tidur）ような些細な習慣が、子どもの精神的規律を育みます。",
                "note": "しつけ（disiplin）の基本動作です。"
            }
        ],
        "dialogue": {
            "title": "休日の家族での大掃除と買い出し計画",
            "lines": [
                ("Ayah", "Mumpung hari Minggu cerah, bagaimana kalau kita bagi tugas membersihkan rumah pagi ini?"),
                ("Ibu", "Setuju, Ayah! Saya dan anak-anak akan mencuci pakaian dan merapikan kamar tidur."),
                ("Ayah", "Bagus, saya yang akan menyapu halaman dan membuang sampah ke tempat penampungan sementara."),
                ("Ibu", "Setelah semua bersih dan rapi, siang nanti kita pergi ke supermarket untuk belanja bulanan ya.")
            ],
            "trans": [
                ("お父さん", "せっかくの日曜の晴天だし、今朝は分担して家の大掃除（membersihkan rumah）をしないかい？"),
                ("お母さん", "大賛成よ、お父さん！私と子どもたちで洗濯（mencuci pakaian）と寝室の片付けをするわ。"),
                ("お父さん", "よし、私は庭を掃いてゴミ出し（membuang sampah）を集積所までしてくるよ。"),
                ("お母さん", "全部綺麗に片付いたら、昼からスーパーへ月々の買い出し（belanja bulanan）に行きましょうね。")
            ]
        },
        "grammar_points": [
            "**meN- による家事動詞の規則変化**: \n- `bersih`（清い） → `membersihkan`（掃除する）\n- `masak`（煮炊きする） → `memasak`（料理する）\n- `cuci`（洗う） → `mencuci`（洗濯する・洗う）\n- `rapi`（整った） → `merapikan`（整頓する）\n形容詞や語根が接尾辞 `-kan` や接頭辞 `meN-` で見事に使役他動詞化されています。",
            "**名詞化 cucian と jemuran**: 接尾辞 `-an` が付いた `cucian` は「洗濯物」、`jemuran` は「天日干し物 / 物干し竿」となり、日常の家事名詞として不可欠です。"
        ],
        "quizzes": [
            {
                "q": "休日に家族で協力して「家を大掃除する、部屋をきれいに片付ける」を表す最も標準的な表現はどれか。",
                "choices": ["membersihkan rumah", "menandatangani kontrak", "mengajukan penawaran", "turun tangan"],
                "ans": "membersihkan rumah",
                "expl": "家を掃除する・片付けるは `membersihkan rumah` です。"
            },
            {
                "q": "給料日後などにスーパーで食料品や日用品をまとめて購入する「月々の買い出し」を表す連語はどれか。",
                "choices": ["belanja bulanan", "laporan laba rugi", "kampanye promosi", "kaki lima"],
                "ans": "belanja bulanan",
                "expl": "月々の買い出しは `belanja bulanan` です。"
            },
            {
                "q": "起床後にシーツや枕を整える「ベッドメイキングをする・布団を整頓する」を表す動詞句はどれか。",
                "choices": ["merapikan tempat tidur", "mencuci pakaian", "memasak makanan", "membuang muka"],
                "ans": "merapikan tempat tidur",
                "expl": "ベッドメイキングをする・寝床を整えるは `merapikan tempat tidur` です。"
            }
        ],
        "culture_column": {
            "title": "「Guling」とインドネシアの抱き枕文化",
            "body": "インドネシアの家庭のベッド（tempat tidur）に欠かせないのが、細長い円筒形の抱き枕「グリン（Guling）」です。植民地時代にオランダ人が熱帯の寝苦しい夜を涼しく快適に過ごすために考案したとされ、当時は「オランダの妻（Dutch wife）」とも呼ばれました。今では老若男女問わず、グリンをぎゅっと抱きしめて眠らなければ安眠できないというほど、国民の生活文化に深く溶け込んでいます。"
        }
    }
]

def generate_markdown(art):
    table_lines = [
        "| コロケーション（連語） | 直訳 | 実際の意味・用例 | 文脈・レジスター | 典型例文 |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for row in art["table_rows"]:
        table_lines.append(f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} | *{row[4]}* |")
    table_md = "\n".join(table_lines)

    details_md_list = []
    for d in art["details"]:
        d_md = f"""### {d["term"]}
- **直訳と意味**: 「**{d["trans"]}**」
- **語感と文脈解説**: {d["nuance"]}

<div class="id-example">
<div class="id-sentence"><strong>{d["ex_id"]}</strong></div>
<div class="id-pronunciation">（{d["ex_kana"]}）</div>
<div class="id-translation">「{d["ex_ja"]}」</div>
</div>

> [!NOTE]
> **語法・派生ポイント**: {d["note"]}
"""
        details_md_list.append(d_md)
    details_md = "\n".join(details_md_list)

    dlg = art["dialogue"]
    dlg_lines = []
    for l in dlg["lines"]:
        dlg_lines.append(f"**{l[0]}**: {l[1]}<br>")
    dlg_trans = []
    for t in dlg["trans"]:
        dlg_trans.append(f"- **{t[0]}**: 「{t[1]}」")
    
    dialogue_md = f"""<div class="dialogue-box">
<div class="dialogue-title">会話ダイアログ：{dlg["title"]}</div>

{"".join(dlg_lines)}
</div>

#### 日本語対訳
{"\n".join(dlg_trans)}
"""

    gp_md = "\n".join([f"- {p}" for p in art["grammar_points"]])

    quizzes_md_list = []
    for idx, q in enumerate(art["quizzes"], 1):
        choices_str = "\n".join([f"{chr(65+c_idx)}. {choice}" for c_idx, choice in enumerate(q["choices"])])
        q_md = f"""#### 問{idx}: {q["q"]}

{choices_str}

<details>
<summary>正解と解説を確認する</summary>

**正解**: 「**{q["ans"]}**」

**解説**:
{q["expl"]}
</details>
"""
        quizzes_md_list.append(q_md)
    quizzes_md = "\n".join(quizzes_md_list)

    col = art["culture_column"]
    culture_md = f"""> [!TIP]
> **文化・専門コラム：{col["title"]}**
> 
> {col["body"]}
"""

    full_text = f"""# {art["title"]}

インドネシア語における **`{art["root"]}`** 分野は、原義として「**{art["meaning"]}**」に関わる領域を表します。{art["core_concept"]}

本稿では、ニュース報道や論文、公式声明、日常会話に至るまでネイティブスピーカーが自然に使いこなす必須の共起表現（コロケーション）を体系的に解説します。

---

## 1. `{art["root"]}` の最頻出コロケーション総覧

まずは、頻繁に用いられる主要な連語表現の全体像を把握しましょう。

{table_md}

---

## 2. 重要コロケーションの詳細解説と実践例文

それぞれの共起表現が持つ語感、文脈のニュアンス、および構文上のポイントを詳しく見ていきます。

{details_md}

---

## 3. 実践会話ダイアログ

現場でこれらのコロケーションがどのように自然に組み合わされて使われるか、会話の流れで確認しましょう。

{dialogue_md}

---

## 4. 文法・構文上の注意点（接辞変化と語形）

{gp_md}

---

## 5. 定着確認クイズ（全3問）

本記事で学んだ重要コロケーションの理解度をチェックしましょう。

{quizzes_md}

---

## 6. コア概念の文化的・専門的背景

{culture_md}

---

## 7. 次のステップ・関連リンク
- [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return full_text

def main():
    os.makedirs("docs/lexicon", exist_ok=True)
    for art in articles:
        content = generate_markdown(art)
        with open(art["filename"], "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {art['filename']}")

if __name__ == "__main__":
    main()
