# -*- coding: utf-8 -*-
"""
Generate Section 32 Batch 3 Articles (1321-1330):
Contemporary Indonesian Society & Trends - Deep Reading Series
- 1321: docs/contemporary/21-culinary-heritage-preservation.md
- 1322: docs/contemporary/22-women-empowerment-umkm.md
- 1323: docs/contemporary/23-cybersecurity-data-leaks.md
- 1324: docs/contemporary/24-education-merdeka-belajar.md
- 1325: docs/contemporary/25-indonesian-language-in-unesco.md
- 1326: docs/contemporary/26-artificial-intelligence-adoption.md
- 1327: docs/contemporary/27-smart-farming-young-farmers.md
- 1328: docs/contemporary/28-plastic-ban-single-use.md
- 1329: docs/contemporary/29-fashion-hijab-modest-wear.md
- 1330: docs/contemporary/30-heritage-railway-revival.md
"""

import os

articles = [
    {
        "filename": "docs/contemporary/21-culinary-heritage-preservation.md",
        "title": "伝統料理レシピのデジタル保存：17,000の島に眠る郷土の味を次世代に継承する",
        "category_badge": "現代社会・食文化とデジタル遺産",
        "lead": "17,000を超える島々と300以上の民族が織りなすインドネシアの郷土料理は、文字として記録されず口承でのみ母から子へと受け継がれてきたため、急速な都市化とファストフードの普及により消滅の危機に瀕しています。スカルノ初代大統領の伝説的料理百科事典『Mustika Rasa』の精神を受け継ぎ、各地の古老たちの知恵をクラウドや動画でアーカイブするデジタル文化遺産保存の最前線に迫ります。",
        "text_id": """Keanekaragaman gastronomi Indonesia merupakan salah satu pusaka budaya takbenda yang paling kaya sekaligus paling rentan di muka bumi. Terbentang di lebih dari 17.000 pulau dengan ratusan suku bangsa, tradisi kuliner nusantara memiliki puluhan ribu resep autentik yang sarat akan kearifan lokal mengenai pemanfaatan rempah-rempah hutan tropis dan tanaman obat liar. Kendati demikian, sebagian besar dari khazanah kuliner adiluhung ini tidak pernah terdokumentasikan dalam bentuk teks tertulis, melainkan hanya diwariskan secara lisan (oral tradition) dari generasi ibu ke anak perempuan di dapur-dapur pedesaan.

Ancaman kepunahan resep tradisional semakin nyata seiring dengan laju urbanisasi yang masif, perubahan gaya hidup serba instan, serta dominasi industri makanan cepat saji global di kalangan generasi muda. Banyak bumbu rempah endemik dan teknik fermentasi purba—seperti pengasapan ikan tradisional di Maluku atau fermentasi rebung asam di Sumatra—mulai dilupakan oleh generasi penerus. Mengabaikan warisan gastronomi ini berarti membiarkan sebagian dari identitas kebangsaan dan kekayaan keanekaragaman hayati nusantara lenyap tanpa jejak.

Merespons krisis kultural ini, gerakan penyelamatan gastronomi berbasis digital mulai marak diinisiasi oleh para sejarawan makanan, juru masak profesional, dan aktivis muda. Terinspirasi oleh kitab kuliner legendaris 'Mustika Rasa'—sebuah ensiklopedia 1.600 resep nusantara yang diprakarsai langsung oleh Presiden Sukarno pada era 1960-an—berbagai komunitas kini aktif blusukan ke pelosok pedalaman untuk merekam video tata cara memasak tradisional, memetakan profil nutrisi bahan pangan lokal, serta mengunggahnya ke basis data komputasi awan yang dapat diakses publik secara gratis. Digitalisasi kuliner ini bukan sekadar upaya nostalgia masa lalu, melainkan strategi ketahanan pangan nasional berbasis kedaulatan pangan lokal.""",
        "vocab": [
            ["pusaka takbenda", "名詞句", "無形文化遺産（intangible cultural heritage）", "Kuliner tradisional adalah pusaka takbenda nusantara."],
            ["khazanah adiluhung", "名詞句", "極めて高貴・崇高な宝庫、至高の文化遺産", "Khazanah adiluhung resep kuno terancam punah."],
            ["blusukan", "動詞（ジャワ語由来）", "現場に直接足を運ぶ、草の根視察する", "Peneliti blusukan ke desa mencari resep langka."],
            ["kedaulatan pangan", "名詞句", "食料主権（自前の食料生産・選択の権利）", "Resep lokal memperkuat kedaulatan pangan nasional."],
            ["fermentasi purba", "名詞句", "古代伝承の発酵技術", "Teknik fermentasi purba menghasilkan cita rasa umami unik."],
            ["keanekaragaman hayati", "名詞句", "生物多様性（biodiversity）", "Rempah nusantara cerminan keanekaragaman hayati."]
        ],
        "translation": [
            "インドネシアのガストロノミー（美食文化）の多様性は、地球上で最も豊潤であると同時に、最も脆弱な無形文化遺産の一つです。数百の民族を擁する17,000以上の島々に広がる群島の食文化の伝統は、熱帯林の香辛料や自生の薬用植物の活用に関する地域の知恵が詰まった何万もの真正なレシピを有しています。それにもかかわらず、この至高の食の宝庫（ハザナー・アディルフン）の大部分は、成文化されたテキストの形で記録されたことがなく、地方の村々の台所において母から娘へと口承の伝統（oral tradition）でのみ受け継がれてきました。",
            "伝統レシピの消滅の危機は、急激な都市化、利便性を追求するインスタントなライフスタイルの変化、そして若い世代におけるグローバルなファストフード産業の支配に伴い、ますます現実味を帯びています。マルク諸島の伝統的な魚の燻製やスマトラの酸味ある発酵タケノコなど、多くの固有のスパイスや古代の発酵技術が、後継世代によって忘れ去られつつあります。このガストロノミーの遺産を放置することは、国家のアイデンティティと群島の生物多様性の豊かさの一部が痕跡もなく消え去るのを看過することを意味します。",
            "この文化的危機に応え、デジタル技術に基づいたガストロノミー救済運動が、食の歴史学者、プロのシェフ、そして若きアクティビストたちによって盛んに立ち上げられ始めました。1960年代にスカルノ初代大統領が直接発案した1,600の群島レシピを網羅する伝説的料理大百科『ムスティカ・ラサ（Mustika Rasa）』に触発され、様々なコミュニティが現在、伝統的な調理法の手順を動画に記録し、地元食材の栄養プロファイルをマッピングし、一般市民が無料でアクセスできるクラウドデータベースへとアップロードするために、人里離れた辺境の現場へと積極的に足を運んで（blusukanして）います。この食文化のデジタル化は単なる過去へのノスタルジーではなく、地元の食料主権に基づいた国家の食料安全保障戦略そのものなのです。"
        ],
        "grammar_points": [
            "ジャワ語起源の政治・行動動詞「blusukan」: ジョコウィ前大統領が庶民の市場や農村へアポなしで視察に訪れる行動から国民語となった `blusukan` は、研究者や若者が「人里離れた現場の奥深くまで直接足を運んで調査する」意味で定着しています。",
            "高雅なジャワ語由来形容詞「adiluhung」: adi（高貴な、美しい）+ luhung（崇高な、卓越した）＝至高の、最高峰の文化的価値を持つもの。伝統文化や王宮芸術を修飾する格調高い雅語です。",
            "構文「bukan sekadar upaya nostalgia ... melainkan strategi ...」: 「単なるノスタルジーではなく、むしろ…という戦略である」という、文化保存の今日的・国家的重要性を論証する高級対比構文です。"
        ],
        "quiz": [
            {
                "question": "インドネシアの何万もの伝統郷土料理レシピが現在消滅の危機に瀕している主な原因は何ですか？",
                "options": ["A. レシピの大半が文字で記録されず母娘の口承に依存しており、都市化とファストフード普及で途絶えつつあるため", "B. インドネシア人が料理をしなくなったため", "C. スパイスが法律で禁止されたため", "D. すべてのレシピがすでに英語に翻訳されたため"],
                "answer": "A. レシピの大半が文字で記録されず母娘の口承に依存しており、都市化とファストフード普及で途絶えつつあるため",
                "explanation": "本文第1・第2段落にある通り、口承に頼ってきたレシピが都市化や生活様式の変化で失われつつあります。"
            },
            {
                "question": "1960年代にスカルノ大統領の主導で編纂された、1600の郷土料理レシピを網羅する伝説的料理本の書名は何ですか？",
                "options": ["A. Mustika Rasa", "B. Laskar Pelangi", "C. Bumi Manusia", "D. Subak Bali"],
                "answer": "A. Mustika Rasa",
                "explanation": "本文第3段落にある通り、スカルノ大統領が命じて作らせた国家料理百科事典は『Mustika Rasa』です。"
            },
            {
                "question": "文中の「blusukan」という言葉の意味として最も適切なものはどれですか？",
                "options": ["A. 人里離れた現場や庶民の生活の場へ直接足を運んで調査する", "B. レストランの料理を美味しく食べる", "C. 迷子になって森をさまよう", "D. 高級ホテルに宿泊する"],
                "answer": "A. 人里離れた現場や庶民の生活の場へ直接足を運んで調査する",
                "explanation": "現場の奥深くや庶民の現場へ直接視察・訪問することを意味するポピュラーな表現です。"
            }
        ],
        "column_title": "歴史コラム：スカルノ大統領の料理外交と『Mustika Rasa』の誕生秘話",
        "column_text": "1960年代、反帝国主義と自立経済（Berdikari）を掲げた初代スカルノ大統領は、「料理こそが国家の自立とアイデンティティの根幹である」と喝破しました。大統領は自ら料理人や各州知事に号令をかけ、群島各地の村々に伝わる未知のレシピを徹底調査させました。数年の歳月をかけて完成した1,000ページを超える『Mustika Rasa』は、宮廷料理から庶民の野草料理までを網羅した世界に誇る文化遺産であり、現代のデジタルアーカイブ運動の原点となっています。"
    },
    {
        "filename": "docs/contemporary/22-women-empowerment-umkm.md",
        "title": "女性起業家が牽引する零細・中小企業（UMKM）：マイクロファイナンスの奇跡",
        "category_badge": "現代社会・ジェンダーと経済自立",
        "lead": "インドネシア国内総生産（GDP）の6割以上を支える約6,500万社の零細・中小企業（UMKM）。その経営者の60%以上が女性（Ibu-ibu）です。無担保のグループ連帯融資を提供する国営マイクロファイナンス「Mekaar」などの普及により、家事や育児の傍ら家庭の台所から起業した女性たちが、貧困の連鎖を断ち切り、子供たちに高等教育を受けさせるまでの「静かな経済革命」の軌跡を追います。",
        "text_id": """Sektor Usaha Mikro, Kecil, dan Menengah (UMKM) merupakan tulang punggung sejati perekonomian Indonesia. Menyumbang lebih dari 61 persen terhadap Produk Domestik Bruto (PDB) nasional dan menyerap sekitar 97 persen dari total tenaga kerja domestik, sektor ini memiliki karakteristik sosiologis yang sangat unik: lebih dari 60 persen pelaku usaha mikro di Indonesia dipimpin dan dikelola oleh kaum perempuan (ibu-ibu rumah tangga). Dari dapur rumah yang sederhana, para perempuan tangguh ini memproduksi aneka makanan ringan, kerajinan tangan, hingga fesyen lokal yang menggerakkan roda ekonomi akar rumput.

Salah satu katalisator paling revolusioner yang memicu pemberdayaan ekonomi perempuan pedesaan adalah ekspansi program pembiayaan mikro syariah dan konvensional yang digulirkan oleh pemerintah melalui PT Permodalan Nasional Madani (PNM) Mekaar (Membina Ekonomi Keluarga Sejahtera). Mengadopsi prinsip pinjaman kelompok tanggung renteng (tontine/joint liability)—mirip dengan model Grameen Bank—PNM Mekaar menyalurkan modal usaha tanpa agunan fisik kepada lebih dari 15 juta perempuan prasejahtera di pelosok nusantara. Pertemuan kelompok mingguan tidak hanya menjadi sarana transaksi cicilan, melainkan juga wadah edukasi literasi keuangan dan penguatan kohesi sosial antarwarga.

Dampak dari kemandirian finansial kaum ibu ini sangat transformatif bagi masa depan bangsa. Berbagai riset sosiologis membuktikan bahwa perempuan cenderung mengalokasikan persentase pendapatan yang jauh lebih besar untuk perbaikan nutrisi keluarga, biaya pendidikan anak-anak hingga jenjang perguruan tinggi, serta tabungan kesehatan. Kendati demikian, perjuangan para pengusaha perempuan ini masih dibayangi oleh beban ganda peran domestik (domestic double burden), keterbatasan akses ke pasar digital formal, serta ancaman jeratan rentenir liar di pedesaan. Membuka akses digitalisasi dan pelatihan manajemen modern bagi pelaku UMKM perempuan adalah kunci mempercepat terwujudnya kesetaraan gender yang berkeadilan di tanah air.""",
        "vocab": [
            ["tulang punggung", "名詞句（比喩）", "大黒柱、中核の支え（backbone）", "UMKM adalah tulang punggung perekonomian Indonesia."],
            ["tanggung renteng", "名詞句", "連帯責任、グループ相互保証", "Sistem tanggung renteng menjamin kelancaran cicilan pinjaman."],
            ["prasejahtera", "形容詞", "生活困窮の、低所得層の（pra- 前 + sejahtera 福祉）", "Bantuan menyasar jutaan keluarga prasejahtera."],
            ["beban ganda", "名詞句", "二重の負担（家事育児と仕事の両立苦）", "Perempuan bekerja kerap memikul beban ganda."],
            ["kohesi sosial", "名詞句", "社会的結束、連帯感", "Pertemuan mingguan mempererat kohesi sosial warga."],
            ["rentenir", "名詞", "高利貸し、ヤミ金業者", "Pinjaman resmi membebaskan warga dari jeratan rentenir."]
        ],
        "translation": [
            "零細・中小企業（UMKM）セクターは、インドネシア経済の真の大黒柱（トゥラン・プングン）です。国内総生産（GDP）の61%以上に貢献し、国内の全雇用の約97%を吸収するこのセクターは、極めてユニークな社会学的特徴を持っています。すなわち、インドネシアの零細企業経営者の60%以上が女性（主婦層）によって率いられ、運営されているのです。質素な自宅の台所から、これらの逞しい女性たちは多種多様なスナック菓子、伝統工芸品、地元ファッションを製造し、草の根の経済の車輪を力強く回しています。",
            "農村部女性の経済的エンパワーメントを促した最も革新的な触媒の一つが、国営企業PT Permodalan Nasional Madani（PNM）が展開する「Mekaar（豊かな家庭経済の育成）」プログラムを通じたマイクロファイナンスの拡大です。グラミン銀行のモデルに類似した「グループ連帯責任（タンゴ・レンテン: tanggung renteng）」の融資原則を採用し、PNM Mekaarは群島各地の1,500万人を超える生活困窮層（プラセジャテラ）の女性たちに対し、物理的担保なしで事業資金を供給しています。毎週のグループ会合は単なる返済の場にとどまらず、金融リテラシー教育や住民同士の社会的一体性（コヒージョン）を強化する貴重なプラットフォームとなっています。",
            "母親たちの経済的自立がもたらした影響は、国家の未来にとって極めて変革的です。様々な社会学的研究が証明しているように、女性は自らの収入のはるかに大きな割合を家族の栄養改善、子供たちの大学までの教育費、そして医療のための貯蓄へと配分する強い傾向を持っています。それにもかかわらず、女性起業家たちの闘いは、家事労働との「二重の負担（ダブルバーデン）」、公式なデジタル市場へのアクセスの限界、そして農村部のヤミ金融（レンテニール）の罠という影に依然として覆われています。女性UMKM事業者に対するデジタル化のアクセス開放と近代的な経営トレーニングの提供こそが、公正なジェンダー平等を加速させる決定的な鍵となっています。"
        ],
        "grammar_points": [
            "比喩的成句「tulang punggung」: tulang（骨）+ punggung（背中）＝背骨、大黒柱。国家経済を支える基幹産業を表現する際の絶対的定番比喩です。",
            "制度概念「tanggung renteng」: tanggung（責任を負う）+ renteng（連なる、数珠繋ぎ）で、「グループ全員が互いに連帯保証人となって返済を支え合う」というマイクロファイナンスの連帯保証システムを指す法務・社会用語です。",
            "接頭辞 pra- による婉曲表現「prasejahtera」: pra-（〜の前、未だ〜ない）+ sejahtera（繁栄した、福祉の行き届いた）で、「貧困層（miskin）」という直接的で侮蔑的な表現を避け、尊厳を保つ行政・福祉用語として定着しています。"
        ],
        "quiz": [
            {
                "question": "インドネシアの零細企業（UMKM）の経営者に関して、統計的に際立っている特徴は何ですか？",
                "options": ["A. 経営者の60%以上が女性（主婦層）であり、草の根経済を牽引していること", "B. 経営者の全員が外国人であること", "C. すべての企業が社員を1,000人以上雇っていること", "D. 店舗がすべて空港の中にあること"],
                "answer": "A. 経営者の60%以上が女性（主婦層）であり、草の根経済を牽引していること",
                "explanation": "本文第1段落にある通り、零細企業の60%以上が主婦をはじめとする女性によって経営されています。"
            },
            {
                "question": "PNM Mekaarのマイクロファイナンスが、無担保で1500万人もの困窮女性に融資できる仕組みは何ですか？",
                "options": ["A. 仲間同士が連帯責任で支え合う「tanggung renteng（連帯責任グループ融資）」モデル", "B. 不動産の土地権利書を預かること", "C. 高級車を担保に取ること", "D. 家族全員のパスポートを没収すること"],
                "answer": "A. 仲間同士が連帯責任で支え合う「tanggung renteng（連帯責任グループ融資）」モデル",
                "explanation": "本文第2段落にある通り、グループで支え合う「tanggung renteng」の連帯保証原則を採用しています。"
            },
            {
                "question": "文中の「tulang punggung」という比喩表現の意味として最も適切なものはどれですか？",
                "options": ["A. 背骨、大黒柱、中核の支え", "B. 美しい装飾品", "C. 非常に重い荷物", "D. 壊れやすい骨董品"],
                "answer": "A. 背骨、大黒柱、中核の支え",
                "explanation": "背骨・背骨の柱から転じて「組織や国家経済を支える大黒柱」を意味します。"
            }
        ],
        "column_title": "社会コラム：母たちの集い「Arisan」から生まれた奇跡の金融連帯",
        "column_text": "インドネシアには、近所の女性たちが毎月集まり、お金を出し合ってくじ引きで順番に総取りする伝統的な頼母子講「アリサン（Arisan）」の文化が古くから津々浦々に根付いています。PNM Mekaarの融資システムがこれほど驚異的な返済率（99%以上）を誇る秘密は、実はこの伝統的なアリサンの信頼ネットワークと女性同士の強い絆（Silaturahmi）をそのまま現代のマイクロクレジットの仕組みへと昇華させた点にあります。地道な女性たちの結束が、国家の貧困削減の最大の原動力となっています。"
    },
    {
        "filename": "docs/contemporary/23-cybersecurity-data-leaks.md",
        "title": "頻発する公的個人データ流出事故と個人データ保護法（UU PDP）の実効性",
        "category_badge": "現代社会・情報セキュリティと法",
        "lead": "有権者名簿、保健省の医療記録、パスポート情報に至るまで、政府機関や国営企業からの大規模な公的個人情報流出事故（Kebocoran Data）が相次いだインドネシア。2024年秋に全面施行された「個人データ保護法（UU PDP）」は、EUのGDPRに匹敵する厳しい罰則を設けたものの、相次ぐランサムウェア攻撃や独立したデータ保護監督機関の設置を巡り、国家のサイバーセキュリティ主権の真価が問われています。",
        "text_id": """Keamanan ruang siber (cybersecurity) telah menjadi salah satu isu paling genting yang mengguncang kepercayaan publik di Indonesia dalam beberapa tahun terakhir. Serangkaian insiden kebocoran data pribadi (data breach) berskala masif terus mendera berbagai institusi strategis, mulai dari jutaan data pemilih Komisi Pemilihan Umum (KPU), basis data rekam medis pasien di bawah Kementerian Kesehatan, hingga kebocoran data paspor Direktorat Jenderal Imigrasi yang diperjualbelikan secara bebas di forum peretas (dark web).

Puncak dari krisis keamanan siber nasional ini meletup secara dramatis ketika Pusat Data Nasional Sementara (PDNS) di Surabaya lumpuh total akibat serangan perangkat pemeras (ransomware) jenis Brain Cipher pada pertengahan tahun 2024. Serangan siber ini melumpuhkan ratusan layanan publik digital vital, termasuk sistem perlintasan imigrasi di seluruh bandara internasional, pendaftaran beasiswa pendidikan, hingga integrasi data perizinan daerah. Insiden memalukan ini menelanjangi kelemahan fatal dalam tata kelola keamanan informasi nasional: rendahnya disiplin pencadangan data (data backup), ketiadaan sistem pemulihan bencana (disaster recovery plan) yang andal, serta tumpang-tindih koordinasi antarlembaga negara.

Di tengah situasi darurat siber tersebut, berlakunya Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP) secara penuh per Oktober 2024 menjadi secercah harapan baru. Mengadopsi prinsip ketat General Data Protection Regulation (GDPR) Uni Eropa, UU PDP mengancam korporasi maupun pengelola data publik yang lalai menjaga kerahasiaan data dengan sanksi administratif berupa denda hingga 2 persen dari total pendapatan tahunan, serta ancaman hukuman pidana kurungan bagi individu yang terbukti menyalahgunakan data pribadi secara melawan hukum. Namun demikian, independensi lembaga otoritas pengawas data pribadi yang dibentuk pemerintah menjadi ujian paling krusial untuk memastikan bahwa hukum ini tidak tumpul ke atas ketika berhadapan dengan kelalaian kementerian negara sendiri.""",
        "vocab": [
            ["kebocoran data", "名詞句", "データ流出、情報漏洩（data breach）", "Insiden kebocoran data pribadi terus berulang."],
            ["perangkat pemeras (ransomware)", "名詞句", "ランサムウェア（身代金要求型ウイルス）", "PDNS diserang oleh perangkat pemeras ganas."],
            ["tumpang-tindih", "動詞/形容詞", "重複する、管轄が重なり合う", "Tumpang-tindih kewenangan memperlemah koordinasi siber."],
            ["pelindungan data pribadi", "名詞句", "個人データ保護（PDP）", "UU Pelindungan Data Pribadi mengadopsi standar GDPR."],
            ["sanksi administratif", "名詞句", "行政処分、行政制裁金", "Korporasi yang lalai terancam sanksi administratif berat."],
            ["tumpul ke atas", "イディオム", "権力者・上流層に対して手加減する（法が甘い）", "Hukum tidak boleh tumpul ke atas dan tajam ke bawah."]
        ],
        "translation": [
            "サイバー空間のセキュリティ（サイバーセキュリティ）は、近年インドネシアにおいて市民の信頼を揺るがす最も緊迫した問題の一つとなっています。中央選挙管理委員会（KPU）の何百万人もの有権者データ、保健省管轄下の患者の医療カルテデータベース、さらには入国管理局のパスポート情報に至るまで、戦略的機関を直撃する大規模な個人データ流出事故が相次ぎ、それらのデータがダークウェブのハッカーフォーラムで公然と売買される事態が発生しました。",
            "この国家サイバーセキュリティ危機の頂点は、2024年半ばにスラバヤの仮設国家データセンター（PDNS）が「Brain Cipher」と呼ばれるランサムウェア（身代金要求型不正プログラム）の攻撃を受けて完全麻痺した際に、劇的な形で爆発しました。このサイバー攻撃は、全国際空港の入国審査システム、教育奨学金の申請、地方許認可データの統合に至るまで、何百もの極めて重要な公的デジタルサービスを麻痺させました。この恥ずべきインシデントは、国家の情報セキュリティガバナンスにおける致命的な弱点を白日の下に晒しました。すなわち、データバックアップの規律の低さ、信頼できる災害復旧計画（ディザスタリカバリ）の欠如、そして国家機関間の管轄の重複と調整不全です。",
            "このサイバー非常事態の渦中、個人データ保護に関する2022年法律第27号（UU PDP）が2024年10月から全面施行されたことは、一筋の新たな希望となりました。欧州連合のGDPRの厳格な原則を取り入れたUU PDPは、データの機密性保持を怠った企業や公的データ管理者に対し、年間売上高の最大2%に達する行政罰金を科すと警告し、個人データを違法に悪用した個人に対しては禁錮刑を含む刑事罰を科しています。しかしながら、政府によって設置される個人データ保護監督機関の独立性は、この法律が国家の省庁自身の過失に対峙した際に「上流（権力側）に対して甘く刃が鈍らない（tumpul ke atas）」ことを保証するための、最も決定的な試練となっています。"
        ],
        "grammar_points": [
            "法慣用表現「tumpul ke atas, tajam ke bawah」: tumpul（鈍い）+ ke atas（上に対して）/ tajam（鋭い）+ ke bawah（下に対して）で、「法律が弱者・庶民に対しては厳罰で厳しく、権力者や政府高官に対しては手加減して甘い」という司法不信を痛烈に告発する絶対的定番成句です。",
            "動詞「menelanjangi」の比喩的用法: telanjang（裸の）に接頭辞 me- と接尾辞 -i が付くことで、「〜の服を剥ぎ取る＝隠されていた致命的な欠陥や腐敗の実態を白日の下に晒し出す」というジャーナリズム特有の告発動詞となります。",
            "法律名詞「pelindungan」と「perlindungan」の正書法上の区別: 正統インドネシア語（EYD）において、保護する「プロセス・行為そのもの」は `pelindungan`、保護された「状態や施設」は `perlindungan` と厳格に使い分けられます（UU Pelindungan Data Pribadi）。"
        ],
        "quiz": [
            {
                "question": "2024年半ばに仮設国家データセンター（PDNS）が麻痺し、全国の空港入国審査をストップさせた原因は何ですか？",
                "options": ["A. Brain Cipher型ランサムウェア（身代金要求型ウイルス）によるサイバー攻撃", "B. データセンターの停電", "C. ネズミがケーブルをかじったこと", "D. インターネットの料金未払い"],
                "answer": "A. Brain Cipher型ランサムウェア（身代金要求型ウイルス）によるサイバー攻撃",
                "explanation": "本文第2段落にある通り、悪質なランサムウェア攻撃によって全国の入国審査や公的サービスが麻痺しました。"
            },
            {
                "question": "2024年10月に全面施行された個人データ保護法（UU PDP）が参考にした、ヨーロッパの厳格な国際基準は何ですか？",
                "options": ["A. GDPR (General Data Protection Regulation)", "B. KTP (Kartu Tanda Penduduk)", "C. ASEAN Charter", "D. UNESCO World Heritage"],
                "answer": "A. GDPR (General Data Protection Regulation)",
                "explanation": "本文第3段落にある通り、EUの包括的データ保護規則であるGDPRの原則を強く反映しています。"
            },
            {
                "question": "成句「tumpul ke atas」が批判している司法・法執行の不公平さはどれですか？",
                "options": ["A. 法律が権力者や政府に対して甘く、追及の手が鈍いこと", "B. 裁判官の使うペンの先が丸まっていること", "C. 高齢者に対する法律の適用が厳しいこと", "D. 山の上で法律が通用しないこと"],
                "answer": "A. 法律が権力者や政府に対して甘く、追及の手が鈍いこと",
                "explanation": "権力者（上）には鈍く弱者（下）には鋭いという、不公正な法執行への痛烈な批判フレーズです。"
            }
        ],
        "column_title": "ITコラム：謎のハッカー「Bjorka（ビョルカ）」と国家のプライド",
        "column_text": "2022年、インドネシアのサイバー空間に「Bjorka（ビョルカ）」と名乗る正体不明のハッカーが出現し、大臣や大統領の個人情報（KTP番号、携帯電話番号、ワクチン接種歴など）を次々とTwitterやTelegramで晒し上げる前代未聞の騒動を起こしました。政府は国家サイバー暗号庁（BSSN）や警察を総動員して追跡したものの正体を特定できず、国民の間では「政府のセキュリティのお粗末さを笑い飛ばすダークヒーロー」として妙な人気を博してしまう事態となりました。この苦い教訓が、国家データ保護法（UU PDP）の成立を急がせる最大の推進力となったのです。"
    },
    {
        "filename": "docs/contemporary/24-education-merdeka-belajar.md",
        "title": "「自由な学び（Merdeka Belajar）」教育改革：暗記教育から探究型プロジェクト学習へ",
        "category_badge": "現代社会・教育改革と人材育成",
        "lead": "ゴジェック（Gojek）創業者から35歳の若さで教育文化研究技術大臣へと電撃抜擢されたナディム・マカリムが断行した、インドネシア教育史上最大の構造改革「ムルデカ・ブラジャール（Merdeka Belajar: 自由な学び）」。半世紀続いた全国統一筆記試験（UN）の廃止、大学でのインターンシップ単位化、探究型プロジェクト学習の導入など、詰め込み教育を破壊した大改革の功罪を総括します。",
        "text_id": """Sistem pendidikan nasional di Indonesia telah mengalami perombakan paling radikal dalam sejarah modernnya melalui peluncuran cetak biru kebijakan 'Merdeka Belajar'. Diprakarsai oleh mantan pendiri raksasa teknologi Gojek yang dipercaya menjabat sebagai Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi, Nadiem Makarim, kebijakan terobosan ini bertujuan membongkar belenggu pedagogi tradisional yang selama puluhan tahun memenjarakan daya kritis siswa dalam budaya hafalan pasif dan orientasi nilai angka semata.

Langkah paling berani dalam reformasi ini adalah penghapusan Ujian Nasional (UN)—sebuah instrumen evaluasi akhir massal yang kerap memicu stres ekstrem bagi siswa dan rentan kecurangan sistemik—yang kemudian digantikan dengan Asesmen Nasional (AN). Berbeda dengan UN yang menguji penguasaan materi pelajaran secara kaku, Asesmen Nasional berfokus mengukur kompetensi literasi membaca mendalam, numerasi logis, serta survei karakter Pancasila secara komprehensif. Di tingkat kurikulum sekolah dasar dan menengah, penerapan 'Kurikulum Merdeka' memberikan fleksibilitas otonom bagi guru untuk merancang pembelajaran berbasis proyek (project-based learning) yang kontekstual dengan kearifan lingkungan lokal.

Di tingkat perguruan tinggi, terobosan ini diwujudkan melalui program 'Kampus Merdeka' yang memberikan hak belajar tiga semester di luar program studi, memungkinkan jutaan mahasiswa magang di industri terkemuka, melakukan riset terapan, atau mengabdi di desa-desa 3T (terdepan, terluar, tertinggal). Kendati disambut pujian karena mendekatkan dunia kampus dengan kebutuhan riil pasar kerja global, implementasi Merdeka Belajar tidak luput dari kendala serius di lapangan: kesenjangan infrastruktur digital yang tajam di wilayah pelosok, beban administratif pelaporan guru yang masih tinggi, serta kesiapan mental para pendidik konvensional dalam beradaptasi dengan perubahan kurikulum yang begitu cepat.""",
        "vocab": [
            ["cetak biru (blueprint)", "名詞句", "青写真、基本計画構想", "Cetak biru Merdeka Belajar merombak pendidikan."],
            ["daya kritis", "名詞句", "批判的思考力、クリティカルシンキング", "Siswa didorong mengembangkan daya kritis analitis."],
            ["Ujian Nasional (UN)", "固有名詞", "全国統一国家試験（かつての卒業試験）", "Penghapusan UN mengakhiri era hafalan buta."],
            ["literasi dan numerasi", "名詞句", "読解力と数理的論理思考力", "Asesmen Nasional berfokus pada literasi dan numerasi."],
            ["wilayah 3T", "固有名詞句", "辺境離島・国境最前線の遅れた地域（Terdepan, Terluar, Tertinggal）", "Mahasiswa mengabdi di sekolah-sekolah wilayah 3T."],
            ["pembelajaran berbasis proyek", "名詞句", "プロジェクト型学習（PBL）", "Kurikulum Merdeka menerapkan pembelajaran berbasis proyek."]
        ],
        "translation": [
            "インドネシアの国家教育システムは、「ムルデカ・ブラジャール（Merdeka Belajar: 自由な学び）」政策構想の発表を通じて、その近代史において最も根本的な再編を経験しました。教育文化研究技術大臣に抜擢された元ゴジェック創業者のナディム・マカリムによって主導されたこの画期的な政策は、何十年もの間、生徒の批判的思考力（クリティカルシンキング）を受動的な丸暗記文化とテストの点数至上主義の中に閉じ込めてきた従来のペダゴジー（教育法）の足枷を破壊することを目指しました。",
            "この改革における最も果敢な一手は、「国家試験（UN: Ujian Nasional）」の完全廃止でした。生徒に極度のストレスを与え、組織的な不正行為の温床となっていたこの全国一斉試験は、「国家アセスメント（AN）」へと取って代わられました。教科内容の機械的な記憶を試していたUNとは異なり、国家アセスメントは深い読解力（リテラシー）、数理的論理思考力（ニューメラシー）、そして包括的なパンチャシラ人格調査の測定に焦点を当てています。初中等教育のカリキュラムレベルでは、「ムルデカ・カリキュラム」の導入により、教師が地域の環境の知恵に根ざした「プロジェクト型学習（PBL）」を自律的に設計できる柔軟性が付与されました。",
            "大学・高等教育レベルでは、この大改革は「キャンパス・ムルデカ（Kampus Merdeka）」プログラムを通じて実現されました。学生が学部の外で最大3学期間学ぶ権利を付与し、何百万人もの大学生が有名企業での長期インターンシップ、応用研究、あるいは「3T地域（国境・辺境・立ち遅れた離島地域）」の村々での教育奉仕活動に参加することを可能にしたのです。大学教育をグローバルな労働市場の実践的ニーズに近づけたとして高い評価を受けた反面、現場での実施には深刻なハードルも露呈しました。辺境地域における深刻なデジタルインフラ格差、教師に対する依然として重い行政報告事務の負担、そしてあまりに急速なカリキュラム変更に適応しきれない従来型教員たちの心理的戸惑いです。"
        ],
        "grammar_points": [
            "比喩動詞「membongkar belenggu」: bongkar（解体する、破壊する）+ belenggu（手枷、足枷、束縛）＝「長年の束縛や因習の足枷を打ち砕く」。旧態依然とした詰め込み教育の打破を雄弁に語る名文句です。",
            "公的略語概念「wilayah 3T」: Terdepan（最前線の・国境沿いの）、Terluar（最外郭の・最果ての島々の）、Tertinggal（開発から取り残された）。インドネシアの地域格差是正政策における最重要行政標語です。",
            "接尾辞 -an による評価名詞「hafalan」: hafal（暗記している）+ -an ＝ 暗記、丸暗記。`budaya hafalan`（丸暗記文化）は創造性を阻害する旧来教育の弊害を象徴する言葉として用いられます。"
        ],
        "quiz": [
            {
                "question": "ナディム・マカリム大臣が主導した教育改革「Merdeka Belajar」における最も象徴的な廃止措置は何ですか？",
                "options": ["A. 暗記偏重で生徒に過度なストレスを与えていた「国家統一試験（UN: Ujian Nasional）」の完全廃止", "B. 夏休みの完全廃止", "C. 教科書の利用禁止", "D. すべての学校をオンライン授業のみにすること"],
                "answer": "A. 暗記偏重で生徒に過度なストレスを与えていた「国家統一試験（UN: Ujian Nasional）」の完全廃止",
                "explanation": "本文第2段落にある通り、点数至上主義と不正の温床だった全国統一卒業試験（UN）を全廃しました。"
            },
            {
                "question": "大学教育改革「Kampus Merdeka」が学生に与えた画期的な権利は何ですか？",
                "options": ["A. 最大3学期にわたり、企業インターンシップや辺境教育奉仕を正規の単位として履修できる権利", "B. 授業料を生涯払わなくてよい権利", "C. 授業に出席せずに卒業できる権利", "D. 教授を自由に解雇できる権利"],
                "answer": "A. 最大3学期にわたり、企業インターンシップや辺境教育奉仕を正規の単位として履修できる権利",
                "explanation": "本文第3段落にある通り、最大3学期をインターンや研究、村落ボランティアに充てる制度です。"
            },
            {
                "question": "文中の「wilayah 3T」の「3T」が表す3つの言葉の組み合わせとして正しいものはどれですか？",
                "options": ["A. Terdepan, Terluar, Tertinggal", "B. Tertinggi, Terbesar, Terjauh", "C. Tercepat, Terbaik, Termurah", "D. Terpanas, Terdingin, Terkering"],
                "answer": "A. Terdepan, Terluar, Tertinggal",
                "explanation": "国境最前線（Terdepan）、最果て離島（Terluar）、開発立ち遅れ地域（Tertinggal）の略です。"
            }
        ],
        "column_title": "教育コラム：建国の父キ・ハジャル・デワンタラの「Taman Siswa」精神の復活",
        "column_text": "「Merdeka Belajar（自由な学び）」という言葉は、実はオランダ植民地時代に民族教育の祖キ・ハジャル・デワンタラ（Ki Hadjar Dewantara）が創設した独立学校「タマン・シスワ（Taman Siswa）」の哲学に由来しています。「教育とは子どもを型にはめることではなく、子ども自身の自然な才能を開花させる手助けをすることである（Ing ngarsa sung tuladha, ing madya mangun karsa, tut wuri handayani）」という教育哲学が、テック起業家出身の大臣の手によって21世紀の国家カリキュラムとして息を吹き返したのです。"
    },
    {
        "filename": "docs/contemporary/25-indonesian-language-in-unesco.md",
        "title": "インドネシア語のユネスコ総会公用語採択：国際語化を目指す言語政策のロードマップ",
        "category_badge": "現代社会・言語政策と国際地位",
        "lead": "2023年11月、パリのユネスコ本部で開催された第42回ユネスコ総会において、インドネシア語が正式に総会公用語（Official Language）として承認されました。英語、フランス語、アラビア語、中国語などに並び、東南アジア諸国連合（ASEAN）加盟国の国語として初の歴史的快挙となったこの決定の背景にある緻密な言語外交と、「インドネシア語の国際化（Internasionalisasi Bahasa Indonesia）」の未来図を読み解きます。",
        "text_id": """Sebuah lembaran sejarah diplomasi kebudayaan yang teramat membanggakan berhasil ditorehkan oleh bangsa Indonesia di panggung multilateral dunia. Pada tanggal 20 November 2023, Sidang Umum ke-42 Organisasi Pendidikan, Keilmuan, dan Kebudayaan Perserikatan Bangsa-Bangsa (UNESCO) di Paris secara aklamasi menyetujui adopsi bahasa Indonesia sebagai salah satu bahasa resmi Sidang Umum UNESCO. Dengan pengakuan bergengsi ini, bahasa Indonesia resmi menjadi bahasa ke-10 yang diakui dalam forum musyawarah tertinggi badan dunia tersebut, berdampingan dengan bahasa-bahasa dunia mapan seperti Inggris, Prancis, Arab, Tiongkok, Rusia, dan Spanyol.

Keberhasilan diplomasi linguistik ini bukanlah sebuah kebetulan yang instan, melainkan buah dari strategi jangka panjang yang diamanatkan langsung oleh Undang-Undang Nomor 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara. Pemerintah melalui Badan Pengembangan dan Pembinaan Bahasa (Badan Bahasa) Kementerian Pendidikan telah merancang peta jalan internasionalisasi bahasa Indonesia secara sistematis. Dengan jumlah penutur yang melampaui 300 juta jiwa di seluruh dunia—menjadikannya bahasa dengan penutur terbanyak ke-11 di dunia—bahasa Indonesia dinilai memiliki vitalitas linguistik yang luar biasa kuat, struktur tata bahasa yang egaliter dan mudah dipelajari, serta peran historis sebagai jembatan pemersatu ratusan suku bangsa yang majemuk.

Pengakuan di tingkat UNESCO ini memicu akselerasi program Bahasa Indonesia bagi Penutur Asing (BIPA) yang kini telah diajarkan di lebih dari 50 negara di dunia, mulai dari perguruan tinggi di Australia, Jepang, Jerman, hingga Mesir. Bagi bangsa Indonesia, status bahasa resmi di forum dunia ini bukan sekadar pencapaian simbolis prestise nasional, melainkan instrumen kekuatan lunak (soft power) yang strategis untuk mempromosikan perdamaian global, memperluas pengaruh geopolitik di kawasan Indo-Pasifik, serta memperjuangkan agar bahasa Indonesia dapat diakui secara de jure sebagai bahasa kerja resmi di tingkat sekretariat ASEAN.""",
        "vocab": [
            ["aklamasi", "名詞", "満場一致の拍手喝采（acclamation）", "Resolusi disetujui secara aklamasi oleh delegasi."],
            ["diplomasi linguistik", "名詞句", "言語外交（言語の国際的普及を目指す外交）", "Diplomasi linguistik memperkuat posisi tawar bangsa."],
            ["vitalitas linguistik", "名詞句", "言語の活力、使用頻度と話者数の強靭さ", "Bahasa Indonesia memiliki vitalitas linguistik tinggi."],
            ["kekuatan lunak (soft power)", "名詞句", "ソフトパワー（文化・価値観による影響力）", "Bahasa resmi menjadi instrumen kekuatan lunak global."],
            ["BIPA", "固有名詞", "外国人向けインドネシア語教育プログラム（Bahasa Indonesia bagi Penutur Asing）", "Program BIPA diajarkan di puluhan kampus dunia."],
            ["akselerasi", "名詞", "加速、促進（acceleration）", "Pengakuan dunia memicu akselerasi promosi BIPA."]
        ],
        "translation": [
            "世界の多国間外交の舞台において、極めて誇らしい文化外交の新たな歴史の1ページがインドネシア国民によって刻まれました。2023年11月20日、パリで開催された第42回国連教育科学文化機関（ユネスコ）総会は、インドネシア語をユネスコ総会の公式言語の一つとして採択することを満場一致（アクラマシ: aklamasi）で承認しました。この栄誉ある承認により、インドネシア語は英語、フランス語、アラビア語、中国語、ロシア語、スペイン語といった確立された世界言語と肩を並べ、国連機関の最高審議フォーラムにおいて認められた第10番目の公式言語となったのです。",
            "この言語外交の成功は決して一過性の偶然ではなく、国旗・国語・国章に関する法律（2009年法律第24号）によって直接義務付けられた長期戦略の結実でした。教育省傘下の言語開発育成機構（Badan Bahasa）を中心とする政府は、インドネシア語の国際化ロードマップを体系的に策定してきました。世界中で3億人を超える話者人口（世界第11位の話者数）を誇るインドネシア語は、極めて強靭な言語的活力（バイタリティ）、階級差のない平等主義的で習得しやすい文法構造、そして多様な数百の民族を結びつけてきた歴史的な統合の架け橋としての役割が高く評価されました。",
            "ユネスコでのこの承認は、オーストラリア、日本、ドイツ、エジプトなど世界50カ国以上の高等教育機関で現在教えられている「外国人向けインドネシア語（BIPA）」プログラムの加速の起爆剤となりました。インドネシア国民にとって、世界フォーラムにおける公式言語の地位は、単なる国家的名誉の象徴的達成にとどまらず、地球規模の平和を促進し、インド太平洋地域における地政学的影響力を拡大し、さらには東南アジア諸国連合（ASEAN）事務局レベルでの公式作業言語としての承認を勝ち取るための、戦略的な「ソフトパワー」の武器となっているのです。"
        ],
        "grammar_points": [
            "外交・議会用語「secara aklamasi」: ラテン語起源の aklamasi（異議のない全員一致の拍手承認）に副詞化接置詞 secara が付いたもので、「全会一致で、満場一致で可決された」ことを表す公式記録の定番表現です。",
            "成句「membuka lembaran sejarah」: lembar（紙のページ・枚）+ sejarah（歴史）＝歴史の1ページを開く、新たな歴史を刻む。輝かしい国家の快挙を称える報道の決まり文句です。",
            "同位概念「kekuatan lunak (soft power)」: 国際関係論の soft power の公式定訳で、軍事力や経済力（hard power）に対比される「文化、言語、道徳的魅力による外交的影響力」を指します。"
        ],
        "quiz": [
            {
                "question": "2023年11月にインドネシア語がユネスコ総会で達成した歴史的快挙は何ですか？",
                "options": ["A. 東南アジア諸国（ASEAN）の言語として初めて、ユネスコ総会の第10番目の公式言語として採択された", "B. ユネスコの本部がジャカルタに移転した", "C. 世界中の全人類がインドネシア語を話すことが義務付けられた", "D. パリの全学校でインドネシア語が必修科目になった"],
                "answer": "A. 東南アジア諸国（ASEAN）の言語として初めて、ユネスコ総会の第10番目の公式言語として採択された",
                "explanation": "本文第1段落にある通り、ASEAN加盟国の言語として初めてユネスコ総会公用語（第10の言語）に採択されました。"
            },
            {
                "question": "世界中で3億人以上の話者を持ち、外国人にインドネシア語を教える教育プログラムの公的略称は何ですか？",
                "options": ["A. BIPA (Bahasa Indonesia bagi Penutur Asing)", "B. KTP (Kartu Tanda Penduduk)", "C. OJK (Otoritas Jasa Keuangan)", "D. PHK (Pemutusan Hubungan Kerja)"],
                "answer": "A. BIPA (Bahasa Indonesia bagi Penutur Asing)",
                "explanation": "外国人向けインドネシア語講座・教育プログラムは「BIPA」と呼ばれます。"
            },
            {
                "question": "文中の「secara aklamasi」という言葉の意味として最も適切なものはどれですか？",
                "options": ["A. 満場一致で、全員の拍手喝采によって", "B. 多数決でギリギリ可決されて", "C. 秘密の投票によって", "D. 激しい殴り合いの末に"],
                "answer": "A. 満場一致で、全員の拍手喝采によって",
                "explanation": "aklamasi（満場一致の拍手採択）により異議なく全員一致で承認されたことを意味します。"
            }
        ],
        "column_title": "歴史コラム：1928年「青年の誓い（Sumpah Pemuda）」から世界への飛翔",
        "column_text": "1928年10月28日、オランダ植民地下のジャカルタに集まった若者たちが「一つの祖国、一つの民族、一つの言語＝インドネシア語」を宣言した歴史的な「青年の誓い（Sumpah Pemuda）」。多数派のマジャパヒトの言語であるジャワ語ではなく、群島の商業共通語（リングア・フランカ）であった平易なマレー語を敢えて国語として選定した先人たちの智慧が、95年の時を経てついにパリのユネスコ総会という世界の最高峰へと飛翔したのです。言語の奇跡の歩みは今も続いています。"
    },
    {
        "filename": "docs/contemporary/26-artificial-intelligence-adoption.md",
        "title": "東南アジアのAI導入最前線：行政DX・多言語チャットボット・農業テックの躍進",
        "category_badge": "現代社会・先端技術とAI",
        "lead": "生成AI（Generative AI）の急速な台頭は、東南アジア最大の人口とデジタルエコノミーを誇るインドネシアにも巨大な地殻変動をもたらしています。エヌビディア（NVIDIA）による大規模AIデータセンター投資、地方自治体の行政DX、700を超える地方言語に対応する多言語AIモデルの開発など、開発途上国におけるAIのフロンティアを深層読解します。",
        "text_id": """Kecerdasan Buatan (Artificial Intelligence/AI), khususnya terobosan model kecerdasan buatan generatif, tengah memicu disrupsi teknologi berskala masif di seluruh sektor kehidupan masyarakat Indonesia. Sebagai negara dengan ekonomi digital terbesar di Asia Tenggara yang diproyeksikan menembus valuasi ratusan miliar dolar AS, Indonesia dipandang oleh raksasa teknologi multinasional sebagai episentrum adopsi AI paling strategis. Komitmen investasi bernilai ratusan juta dolar dari Nvidia dan Indosat Ooredoo Hutchison untuk membangun pusat keunggulan AI (AI Centre of Excellence) di Surakarta, Jawa Tengah, menjadi bukti konkret magnet investasi teknologi masa depan ini.

Penerapan kecerdasan buatan di Indonesia memperlihatkan karakteristik solutif yang sangat khas dalam mengatasi kesenjangan struktural di negara kepulauan. Di sektor pelayanan publik, kementerian dan pemerintah daerah mulai mengintegrasikan asisten virtual cerdas berbasis Natural Language Processing (NLP) untuk melayani pengurusan perizinan warga selama 24 jam nonstop. Di sektor pertanian, perusahaan rintisan agritech memanfaatkan algoritma computer vision dan citra satelit guna memprediksi serangan hama wereng dan mengoptimalkan pemupukan presisi bagi petani sawah. Lebih mengesankan lagi, para peneliti kecerdasan buatan lokal tengah giat mengembangkan Large Language Model (LLM) dwibahasa yang mampu menerjemahkan ratusan bahasa daerah nusantara yang terancam punah ke dalam bahasa Indonesia secara akurat.

Kendati menawarkan lompatan produktivitas yang fantastis, penetrasi AI yang begitu agresif membawa sederet tantangan etis dan ketenagakerjaan yang tidak mudah. Laporan dari berbagai lembaga riset tenaga kerja mengingatkan bahwa jutaan pekerjaan administratif tingkat pemula di sektor perbankan, telekomunikasi, dan layanan pelanggan rentan terdisrupsi oleh otomatisasi cerdas. Di samping itu, ketiadaan regulasi etika AI yang mengikat secara hukum—saat ini baru berupa Surat Edaran Menteri Komunikasi dan Informatika—menimbulkan kekhawatiran terkait bias algoritma, pelanggaran hak cipta data pelatihan, serta masifnya peredaran konten disinformasi palsu (deepfake) yang berpotensi mencederai iklim demokrasi bangsa.""",
        "vocab": [
            ["kecerdasan buatan generatif", "名詞句", "生成AI（Generative AI）", "AI generatif memicu disrupsi cara kerja modern."],
            ["episentrum adopsi", "名詞句", "技術導入・普及の震源地、中心地", "Indonesia menjadi episentrum adopsi teknologi digital."],
            ["bahasa daerah nusantara", "名詞句", "群島各地の地方言語（700以上存在）", "Model LLM lokal dikembangkan untuk bahasa daerah."],
            ["terdisrupsi", "動詞（受動態）", "破壊的変革を被る、淘汰される", "Pekerjaan klerikal rentan terdisrupsi otomatisasi AI."],
            ["palsu (deepfake)", "名詞句", "ディープフェイク、高度なAI偽造動画・音声", "Peredaran video deepfake mengancam iklim demokrasi."],
            ["surat edaran", "名詞句", "通達、回状（法的拘束力のないガイドライン）", "Panduan etika AI masih berupa surat edaran menteri."]
        ],
        "translation": [
            "人工知能（AI）、とりわけ生成AIモデルの画期的な進歩は、インドネシア社会のあらゆる生活分野において大規模なテクノロジー・ディスラプション（破壊的変革）を引き起こしています。将来的に数百億ドル規模の評価額に達すると予測されている東南アジア最大のデジタル経済大国として、インドネシアは多国籍メガテック企業から最も戦略的なAI受容の中心地（エピセンター）と見なされています。エヌビディア（NVIDIA）とインドサット（Indosat Ooredoo Hutchison）が中部ジャワ州スラカルタ（ソロ）にAI卓越性センター（AI Centre of Excellence）を建設するための数億ドル規模の投資コミットメントは、この未来のテクノロジー投資の強い引力を示す具体的な証拠です。",
            "インドネシアにおけるAIの適用は、島嶼国家特有の構造的格差を克服するための極めてユニークな解決志向の特徴を示しています。公共サービス分野では、省庁や地方自治体が自然言語処理（NLP）ベースの高度な対話型AIアシスタントを統合し、市民の行政許認可手続きを24時間ノンストップで処理し始めています。農業分野では、アグリテックのスタートアップ企業がコンピュータービジョン・アルゴリズムと衛星画像を組み合わせ、ウンカなどの害虫被害の予測や水田農家のための精密施肥の最適化に役立てています。さらに目覚ましいことに、地元のAI研究者たちは、消滅の危機に瀕している何百もの群島地方言語をインドネシア語へと正確に翻訳・架橋するバイリンガル大規模言語モデル（LLM）の開発を精力的に進めています。",
            "驚異的な生産性の跳躍を提供する一方で、あまりにアグレッシブなAIの浸透は、容易ではない一連の倫理的および雇用上の課題をもたらしています。労働調査機関のレポートは、銀行、通信、カスタマーサービスにおける何百万もの初級事務職が、知的自動化によって淘汰・代替されるリスクが高いと警告しています。さらに、法的拘束力を持つAI倫理規制の不在（現時点では情報通信大臣の『通達（Surat Edaran）』にとどまる）は、アルゴリズムの偏見、学習データの著作権侵害、そして民主主義の気候を傷つけかねない高度な偽造コンテンツ（ディープフェイク: deepfake）の大規模な拡散に対する強い懸念を生み出しています。"
        ],
        "grammar_points": [
            "語根 disrupsi からの派生動詞「terdisrupsi」: 外来語 disruption に受動態接頭辞 ter- が付いたもので、「意図せずして破壊的イノベーションの波に呑み込まれ、淘汰されてしまう」という不可抗力的ニュアンスを表します。",
            "形容詞句「berupa Surat Edaran」: berupa（〜の形をとっている）+ Surat Edaran（大臣通達）。法律（Undang-Undang）のような強制力・罰則がなく、あくまで努力目標やガイドラインにとどまっている規制の弱さを客観的に指摘する定型句です。",
            "専門語彙「dwibahasa」の語構成: サンスクリット語数詞 dwi-（2つの、バイ〜）+ bahasa（言語）＝「二言語の、バイリンガルな」。dwiwarna（二色の＝赤白国旗）、dwifungsi（二重機能）などと同様の伝統的造語法です。"
        ],
        "quiz": [
            {
                "question": "半導体大手エヌビディア（NVIDIA）がインドサットと共同でインドネシアに建設を発表した大型AI投資施設は何ですか？",
                "options": ["A. 中部ジャワ州スラカルタ（ソロ）のAI卓越性センター（AI Centre of Excellence）", "B. バリ島の巨大映画館", "C. ジャカルタの石炭発電所", "D. カリマンタンの紙パルプ工場"],
                "answer": "A. 中部ジャワ州スラカルタ（ソロ）のAI卓越性センター（AI Centre of Excellence）",
                "explanation": "本文第1段落にある通り、NVIDIAはソロにAI卓越性センターを建設する投資を発表しました。"
            },
            {
                "question": "多言語国家インドネシアにおいて、地元AI研究者たちが特に力を入れて開発している独自の大規模言語モデル（LLM）の目的は何ですか？",
                "options": ["A. 700以上ある消滅危機の地方言語（Bahasa Daerah）を正確に翻訳・保存すること", "B. 学校の宿題をすべてAIに代筆させること", "C. テレビのアナウンサーを全員ロボットにすること", "D. 外国語の利用を法律で禁止すること"],
                "answer": "A. 700以上ある消滅危機の地方言語（Bahasa Daerah）を正確に翻訳・保存すること",
                "explanation": "本文第2段落にある通り、何百もの多様な地方言語を保存・翻訳するLLMの開発が進められています。"
            },
            {
                "question": "文中の「terdisrupsi」という言葉の意味として最も適切なものはどれですか？",
                "options": ["A. 破壊的変化によって淘汰される、急変に巻き込まれる", "B. 昇進して給料が上がること", "C. 海外へ旅行に行くこと", "D. 新しいコンピューターを買い換えること"],
                "answer": "A. 破壊的変化によって淘汰される、急変に巻き込まれる",
                "explanation": "disrupsi（破壊的革新）に受動接頭辞 ter- が付いた言葉で、「淘汰される、変革の煽りを食らう」を意味します。"
            }
        ],
        "column_title": "社会コラム：大統領選を揺るがした「ディープフェイク（Deepfake）」AIの衝撃",
        "column_text": "2024年のインドネシア大統領選挙において、世界を驚かせたのはAIテクノロジーの大規模な政治利用でした。かつて軍の強硬派司令官として知られたプラボウォ候補のイメージを、AI生成の愛らしいチビキャラアニメ（Gemoy）に変貌させて若者票を一気に掴んだ戦略や、故スハルト元大統領がAIディープフェイクで蘇り有権者に投票を呼びかける動画など、AIは世論を劇的に動かす諸刃の剣となりました。技術の倫理的リテラシーが今まさに試されています。"
    },
    {
        "filename": "docs/contemporary/27-smart-farming-young-farmers.md",
        "title": "IoTスマート農業に参入する高学歴「ミレニアル農家（Petani Milenial）」の台頭",
        "category_badge": "現代社会・農業革新と若者",
        "lead": "農業従事者の平均年齢が50歳を超え、後継者不足が叫ばれる中、ITや工学を学んだ高学歴の若者たちがスマート農業（Smart Farming）を引っ提げて農村へ帰還する「ミレニアル農家（Petani Milenial）」現象が起きています。スマートフォンによるIoT水やり自動化、ドローン農薬散布、直販Eコマースアプリを駆使し、旧来の「泥臭く儲からない農業」を最先端ビジネスへと変革する若きイノベーターたちに迫ります。",
        "text_id": """Sektor pertanian Indonesia tengah menghadapi krisis regenerasi yang mengkhawatirkan: mayoritas petani di tanah air saat ini telah berusia di atas 50 tahun, sementara generasi muda pedesaan cenderung berbondong-bondong merantau ke kota-kota besar demi memburu pekerjaan formal. Pekerjaan bertani selama ini kerap dicitrakan secara stereotipikal sebagai profesi rendahan yang kotor, melelahkan, dan tidak menjanjikan masa depan finansial yang mapan akibat panjangnya rantai tengkulak yang mempermainkan harga komoditas.

Namun, narasi pesimistis tersebut kini mulai dipatahkan oleh kebangkitan fenomena 'Petani Milenial'. Didukung oleh program inkubasi pemerintah daerah—seperti yang dipelopori secara masif di Provinsi Jawa Barat—ribuan pemuda berpendidikan sarjana dari latar belakang teknik, ilmu komputer, dan manajemen memilih banting stir kembali ke desa. Mereka merevolusi metode budidaya pertanian konvensional menjadi pertanian presisi berbasis Internet of Things (IoT smart farming).

Dengan memanfaatkan sensor tanah nirkabel untuk memantau kelembapan dan keasaman (pH) secara real-time, sistem irigasi tetes otomatis (drip irrigation) yang dikendalikan melalui layar ponsel pintar, serta pemanfaatan armada pesawat nirawak (drone) untuk penyemprotan pupuk organik cair, efisiensi panen melonjak drastis hingga puluhan persen. Selain inovasi teknologi di hulu, para petani milenial ini juga memotong cengkeraman tengkulak di hilir dengan memasarkan sayuran hidroponik dan buah premium mereka secara langsung ke konsumen perkotaan melalui platform e-commerce dan media sosial. Transformasi ini membuktikan bahwa modernisasi pertanian mampu mengembalikan martabat profesi petani sebagai wirausahawan agribisnis modern yang prestisius.""",
        "vocab": [
            ["regenerasi petani", "名詞句", "農家の世代交代、後継者育成", "Regenerasi petani sangat penting bagi ketahanan pangan."],
            ["rantai tengkulak", "名詞句", "中間搾取仲買人（トングラック）の多重流通網", "Petani kerap dirugikan oleh permainan harga rantai tengkulak."],
            ["banting stir", "慣用句", "ハンドルを急転回する、進路・職歴を劇的に変える", "Sarjana teknik banting stir menjadi petani milenial."],
            ["pertanian presisi (precision farming)", "名詞句", "精密農業（IoTデータに基づく農業）", "Pertanian presisi mengoptimalkan penggunaan pupuk dan air."],
            ["irigasi tetes", "名詞句", "点滴灌漑（ドリップイリゲーション）", "Sistem irigasi tetes dikendalikan lewat aplikasi smartphone."],
            ["wirausahawan agribisnis", "名詞句", "アグリビジネス起業家", "Anak muda bangga menjadi wirausahawan agribisnis."]
        ],
        "translation": [
            "インドネシアの農業セクターは、憂慮すべき世代交代（リジェネレーション）の危機に直面しています。現在、国内の農家の過半数は50歳を超えており、農村部の若い世代は正規雇用の仕事を求めて大都市へと大挙して出稼ぎ（ムランタウ: merantau）する傾向にあります。これまで農業という職業は、汚れ、過酷で、農産物価格を牛耳る中間仲買人（トングラック: tengkulak）の長い搾取構造のために安定した経済的未来を約束しない「低層の仕事」としてステレオタイプにイメージされてきました。",
            "しかし、この悲観的な言説は現在、「ミレニアル農家（Petani Milenial）」現象の勃興によって打ち破られ始めています。西ジャワ州などで大規模に先駆けて推進された地方政府のインキュベーションプログラムに後押しされ、工学、情報科学、経営学などの学士号を持つ何千人もの大卒の若者たちが、進路を大きく舵を切って（バンティング・スティール: banting stir）農村へと帰還することを選んだのです。彼らは従来の慣行農業手法を、モノのインターネット（IoT）に基づく「精密スマート農業」へと革命的に変革しています。",
            "土壌の水分量や酸性度（pH）をリアルタイムで監視する無線土壌センサー、スマートフォンの画面から遠隔制御される自動点滴灌漑（ドリップイリゲーション）システム、そして液体有機肥料の散布のためのドローン（無人機）艦隊の配備を活用することで、収穫効率は数十パーセントも跳ね上がりました。上流での技術革新に加え、これらミレニアル農家たちは、自ら生産した水耕栽培野菜や高級果物をEコマースプラットフォームやソーシャルメディアを通じて都市部の消費者へ直接マーケティングすることで、下流における中間仲買人の支配を断ち切りました。この変革は、農業の近代化が農家という職業の尊厳を取り戻し、名誉ある「近代アグリビジネス起業家」へと昇華させ得ることを証明しています。"
        ],
        "grammar_points": [
            "慣用句「banting stir」の比喩的用法: banting（叩きつける、急旋回する）+ stir（車のハンドル・舵）＝ハンドルを急に切る、転じて「これまでのキャリアや専攻から劇的に職業方針を転換する」ことを表す極めてポピュラーな成句です。",
            "社会用語「rantai tengkulak」の告発性: tengkulak（農村の悪質な買い叩き仲買人）が形成する重層的な流通マージンを指し、零細農家がいつまでも貧困から抜け出せない構造的原因として常に槍玉に挙げられます。",
            "造語「wirausahawan」の構造: wira（英雄、勇敢な者）+ usaha（事業、努力）+ -wan（〜の人）＝「起業家、アントレプレナー」。単なる商人（pedagang）ではなく、リスクをとって革新を起こす実業家への敬意が込められています。"
        ],
        "quiz": [
            {
                "question": "「Petani Milenial（ミレニアル農家）」と呼ばれる若者たちが、従来の農業と一線を画している革新的な点は何ですか？",
                "options": ["A. IoT土壌センサー、ドローン散布、スマホ遠隔灌漑などのスマート農業技術と直販Eコマースを活用している点", "B. 農機具を一切使わずに素手だけで耕す点", "C. すべての野菜を外国から輸入して売る点", "D. 畑仕事をすべて外国人にやらせている点"],
                "answer": "A. IoT土壌センサー、ドローン散布、スマホ遠隔灌漑などのスマート農業技術と直販Eコマースを活用している点",
                "explanation": "本文第2・第3段落にある通り、IoTセンサーやドローンなどの精密農業とネット直販を武器にしています。"
            },
            {
                "question": "農村の若者たちが農業を敬遠してきた最大の構造的要因として挙げられているものはどれですか？",
                "options": ["A. 中間仲買人（tengkulak）による買い叩き構造と、過酷で儲からないというステレオタイプ", "B. インドネシアの土壌で野菜が育たないこと", "C. 若者が野菜を食べるのを嫌っていること", "D. 農地でインターネットが法律で禁止されていること"],
                "answer": "A. 中間仲買人（tengkulak）による買い叩き構造と、過酷で儲からないというステレオタイプ",
                "explanation": "本文第1段落にある通り、仲買人による搾取構造と「汚くて儲からない」というイメージが原因でした。"
            },
            {
                "question": "文中の「banting stir」という慣用句の意味として最も適切なものはどれですか？",
                "options": ["A. 進路やキャリアを劇的に転換する、方針を大きく変える", "B. 車のハンドルを壊してしまう", "C. 激しい交通事故を起こす", "D. 自動車の運転を諦める"],
                "answer": "A. 進路やキャリアを劇的に転換する、方針を大きく変える",
                "explanation": "ハンドルを急旋回することから「キャリアや方針を大きく方向転換する」ことを意味します。"
            }
        ],
        "column_title": "経済コラム：西ジャワ州政府の「Petani Milenial」プロジェクトの挑戦と挫折",
        "column_text": "リドワン・カミル前西ジャワ州知事が大々的に打ち出した「Petani Milenial」構想は、遊休州有地を若者に無償貸与し、地方銀行の低利融資と買い取り保証をセットにしたことで全国的な注目を集めました。しかし、一部のプロジェクトでは土壌の不適合やオフテイカー（買い取り企業）の債務不履行により若者が借金を背負うトラブルも発生。「スマート農業の技術だけでなく、作物の販売リスクヘッジと強固なサプライチェーンの構築こそが生死を分ける」という貴重な実務の教訓を残しました。"
    },
    {
        "filename": "docs/contemporary/28-plastic-ban-single-use.md",
        "title": "使い捨てプラスチック禁止令：伝統エコ素材キャッサババッグとリフィル文化の復活",
        "category_badge": "現代社会・環境問題と循環経済",
        "lead": "世界第2位の海洋プラスチック汚染排出国という不名誉なレッテルに直面したインドネシア。ジャカルタやバリ島をはじめとする主要都市が「使い捨てレジ袋の全面禁止」に踏み切る中、キャッサバ（タピオカの原料芋）から作られる100%生分解性バイオプラスチックや、昔ながらのバナナの葉、容器持参リフィルステーションなど、伝統と先端素材が織りなす「脱プラ循環経済」の現在地をレポートします。",
        "text_id": """Krisis polusi sampah plastik telah menempatkan Indonesia di bawah sorotan tajam komunitas lingkungan internasional. Studi ilmiah yang dipublikasikan dalam jurnal Science oleh Jenna Jambeck sempat menempatkan nusantara sebagai penyumbang sampah plastik ke lautan terbesar kedua di dunia setelah Tiongkok. Jutaan ton kantong kresek, sedotan plastik, dan kemasan saset (sachet) sekali pakai yang tidak terkelola mencemari sungai-sungai utama, menyumbat saluran drainase perkotaan hingga memicu banjir menahun, serta meracuni ekosistem terumbu karang laut tropis.

Menyadari ancaman ekologis yang kian tidak terkendali, gelombang aksi kebijakan lingkungan mulai bergulir dari tingkat daerah. Provinsi Bali memelopori terobosan berani melalui Peraturan Gubernur Nomor 97 Tahun 2018 yang melarang total penggunaan kantong plastik, styrofoam, dan sedotan plastik sekali pakai di seluruh pusat perbelanjaan, toko modern, hingga pasar tradisional. Langkah progresif ini segera disusul oleh DKI Jakarta melalui Peraturan Gubernur Nomor 142 Tahun 2019, yang mewajibkan seluruh peritel dan pengelola pasar rakyat beralih ke kantong belanja ramah lingkungan.

Di tengah tekanan regulasi tersebut, muncullah revolusi inovasi material hijau dari para wirausahawan lokal yang menggali kekayaan agrikultur nusantara. Perusahaan rintisan bioplastik seperti Avani Eco sukses menciptakan kantong belanja berbahan dasar pati singkong (cassava starch) yang dapat terurai secara hayati dalam hitungan bulan di dalam tanah, bahkan larut seketika dalam air panas tanpa meninggalkan residu mikroplastik berbahaya. Di tingkat gaya hidup masyarakat perkotaan, toko curah tanpa kemasan (bulk store) dan stasiun isi ulang (refill station) mulai menjamur, menghidupkan kembali kearifan leluhur yang terbiasa membawa wadah sendiri dan membungkus makanan dengan daun pisang alami demi kelestarian bumi pertiwi.""",
        "vocab": [
            ["kantong kresek", "名詞句", "薄手の使い捨てプラスチックレジ袋", "Penggunaan kantong kresek sekali pakai dilarang di Jakarta."],
            ["sampah saset (sachet)", "名詞句", "小分け使い切りパウチ包装ゴミ", "Sampah saset plastik sangat sulit didaur ulang."],
            ["pati singkong (cassava)", "名詞句", "キャッサバ芋デンプン（タピオカ原料）", "Bioplastik dari pati singkong mudah terurai alami."],
            ["terurai secara hayati", "動詞句", "生分解される（biodegradable）", "Kantong nabati terurai secara hayati dalam tanah."],
            ["toko curah (bulk store)", "名詞句", "量り売りゼロウェイストショップ", "Toko curah mendorong gaya hidup bebas sampah."],
            ["bumi pertiwi", "名詞句", "母なる大地、祖国インドネシア", "Mari kita jaga kelestarian alam bumi pertiwi."]
        ],
        "translation": [
            "プラスチックゴミ汚染の危機は、インドネシアを国際環境コミュニティの厳しい監視の視線の下に置くことになりました。ジェンナ・ジャンベック博士らが学術誌『Science』に発表した著名な研究論文は、インドネシアを中国に次ぐ「世界第2位の海洋プラスチックゴミ排出国」として位置付けました。適切に処理されない何百万トンもの使い捨てレジ袋（カントン・クレセック: kantong kresek）、プラスチック製ストロー、小分けパウチ包装（サシェ: sachet）が主要な河川を汚染し、都市の排水路を詰まらせて毎年の洪水を誘発し、熱帯のサンゴ礁生態系を蝕んできました。",
            "制御不能になりつつある生態学的脅威を自覚し、環境政策の行動の波が地方自治体レベルから動き始めました。バリ州は2018年州知事令第97号を通じて、すべてのショッピングモール、近代的小売店、伝統市場に至るまで、使い捨てプラスチック袋、発泡スチロール、プラスチックストローの使用を全面禁止する果敢な先駆けとなりました。この進歩的な一歩には直ちにジャカルタ首都特別州（DKI Jakarta）が2019年州知事令第142号で追随し、すべての小売業者および市民市場の管理者に対して環境配慮型のエコバッグへの切り替えを義務付けました。",
            "この規制強化の圧力のただ中で、群島の豊かな農業資源を掘り起こした地元起業家たちによる「グリーン素材イノベーションの革命」が出現しました。「Avani Eco」などのバイオプラスチック・スタートアップは、キャッサバ芋のデンプン（タピオカ原料）を主原料とし、土壌の中で数ヶ月のうちに完全に生分解され、熱湯の中では有害なマイクロプラスチックの残渣を残さず即座に溶解するショッピングバッグの開発に成功しました。都市市民のライフスタイルレベルでは、容器包装なしの量り売り店（バルクストア）や洗剤のリフィルステーションが急増し、母なる大地の持続可能性のために、自前の容器を持参し自然のバナナの葉で食べ物を包んでいた先祖の知恵をリバイバルさせています。"
        ],
        "grammar_points": [
            "口語名称「kantong kresek」の定着: 薄手のビニール袋が擦れ合う「カサカサ（kresek-kresek）」という擬音語に由来する生活用語で、公的な行政令やニュース報道でも正式な用語として日常的に用いられます。",
            "愛国・詩的表現「bumi pertiwi」: サンスクリット語の地母神プリティヴィーに由来する表現で、「母なる祖国の大地・豊かな国土」を慈しむ情緒的な響きを持ちます。",
            "接頭辞 se- による時間限定「dalam hitungan bulan」: 「ものの数ヶ月のうちに、数ヶ月と経たないうちに」という迅速な自然分解のプロセスを明快に表現するフレーズです。"
        ],
        "quiz": [
            {
                "question": "ジャカルタやバリ島などの地方政府が施行した画期的なプラスチック環境規制の内容は何ですか？",
                "options": ["A. ショッピングモールや市場での使い捨てプラスチックレジ袋（kantong kresek）などの使用全面禁止", "B. プラスチック袋を有料で1枚10万円に値上げしたこと", "C. すべてのプラスチックを燃やすことを義務付けたこと", "D. 買い物をすること自体を禁止したこと"],
                "answer": "A. ショッピングモールや市場での使い捨てプラスチックレジ袋（kantong kresek）などの使用全面禁止",
                "explanation": "本文第2段落にある通り、使い捨てレジ袋、発泡スチロール、ストローなどの使用が条例で禁止されました。"
            },
            {
                "question": "地場スタートアップ「Avani Eco」が開発した、熱湯に溶けて数ヶ月で土に還る生分解性エコバッグの原料は何ですか？",
                "options": ["A. キャッサバ芋のデンプン（pati singkong）", "B. 石油の廃油", "C. アルミニウムの粉末", "D. 牛の皮"],
                "answer": "A. キャッサバ芋のデンプン（pati singkong）",
                "explanation": "本文第3段落にある通り、キャッサバ（タピオカの原料芋）のデンプンから作られています。"
            },
            {
                "question": "文中の「kantong kresek」という言葉の語源として正しいものはどれですか？",
                "options": ["A. ビニール袋が擦れ合う「カサカサ（kresek-kresek）」という音のオノマトペ", "B. 発明したオランダ人科学者の名前", "C. ジャカルタの川の名前", "D. 政府の公認スタンプの名前"],
                "answer": "A. ビニール袋が擦れ合う「カサカサ（kresek-kresek）」という音のオノマトペ",
                "explanation": "薄いレジ袋が擦れる「カサカサ」というオノマトペから名付けられた日常語です。"
            }
        ],
        "column_title": "環境コラム：多国籍消費財メーカーの「Sachet（小分けパウチ）」経済の功罪",
        "column_text": "インドネシアの街角の個人商店（Warung）を覗くと、シャンプーや洗剤、インスタントコーヒーが1回分ずつプラ包装された「Sachet（サシェ）」が所狭しと吊り下げられています。日雇い労働者や低所得層がその日暮らしの小銭で日用品を買えるように多国籍企業が広めたビジネスモデルですが、アルミとプラスチックの複合フィルムであるためリサイクルが不可能で、海洋プラ汚染の最大の元凶となっています。生活の利便性と環境正義のせめぎ合いが続いています。"
    },
    {
        "filename": "docs/contemporary/29-fashion-hijab-modest-wear.md",
        "title": "モデストファッションの世界首都：モダンヒジャブと伝統バティックの融合革命",
        "category_badge": "現代社会・ファッションと宗教",
        "lead": "世界最大のムスリム女性人口を擁するインドネシアは、身体の露出を控えた現代的なイスラム服飾「モデスト・ファッション（Modest Fashion）」の世界的流行発信地（Mecca of Modest Fashion）へと飛翔しました。伝統的なベール（ヒジャブ）にバティックやイカットの幾何学美、パステルカラーの優美さを融合させた女性デザイナーたちの台頭と、数十億ドル規模の巨大ファッション市場の深層を読み解きます。",
        "text_id": """Indonesia tengah mengukir reputasi internasional yang gemilang sebagai episentrum mode busana santun dunia (Mecca of World Modest Fashion). Jika beberapa dekade silam gaya berbusana muslimah kerap dicitrakan secara kaku, monokromatik, dan homogen dalam balutan gamis longgar bergaya Timur Tengah, lanskap tersebut kini telah bertransformasi total menjadi industri kreatif bernilai triliunan rupiah yang sangat dinamis, penuh warna, dan berorientasi pada tren global kontemporer.

Kunci dari revolusi estetika fesyen muslim Indonesia ini terletak pada keberanian para perancang busana perempuan lokal dalam mengawinkan nilai-nilai kepatuhan syariat Islam dengan kekayaan khazanah wastra nusantara. Kain tradisional warisan leluhur—seperti batik tulis Jawa, tenun ikat Nusa Tenggara, dan songket Minangkabau yang anggun—disulap secara kreatif menjadi busana modern berpotongan elegan (chic ready-to-wear), blazer kantor profesional, hingga gaun malam mewah haute couture. Keberagaman warna-warna pastel yang cerah dan material kain katun tropis yang sejuk menjadikan busana muslim Indonesia sangat adaptif dengan iklim khatulistiwa dan digandrungi oleh perempuan muda modern (hijabers).

Perhelatan panggung mode terkemuka seperti Jakarta Muslim Fashion Week (JMFW) dan Indonesia Modest Fashion Week (IMFW) secara konsisten menarik atensi pembeli internasional dari Timur Tengah, Eropa, hingga Amerika Serikat. Desainer papan atas nasional seperti Dian Pelangi dan Ria Miranda telah sukses memamerkan koleksi mereka di panggung bergengsi New York Fashion Week dan Paris Fashion Week. Didukung oleh penetrasi pesat platform niaga elektronik (e-commerce) dan ekosistem pembuat konten fesyen di media sosial, industri modest fashion Indonesia tidak hanya memperkuat identitas budaya bangsa, melainkan juga membuktikan bahwa religiusitas dan modernitas estetika dapat berjalan seiring secara harmonis dan inklusif.""",
        "vocab": [
            ["busana santun (modest fashion)", "名詞句", "モデストファッション（露出を控えた上品な服装）", "Indonesia berambisi menjadi pusat busana santun dunia."],
            ["wastra nusantara", "名詞句", "群島伝統織物（バティック、絣、ソンケット等の総称）", "Desainer memadukan hijab dengan wastra nusantara."],
            ["kepatuhan syariat", "名詞句", "イスラム法の遵守（戒律への敬意）", "Busana dirancang tanpa melanggar kepatuhan syariat."],
            ["hijabers", "名詞（スラング造語）", "おしゃれにヒジャブを着こなす現代ムスリム女性", "Komunitas hijabers menjadi penggerak tren mode."],
            ["digandrungi", "動詞（受動態）", "熱狂的に愛好される、大人気である", "Warna-warna pastel sangat digandrungi anak muda."],
            ["religiusitas", "名詞", "宗教性、信仰心（religius 由来）", "Fesyen membuktikan religiusitas dapat berdampingan dengan tren."]
        ],
        "translation": [
            "インドネシアは、世界の「モデスト・ファッション（Busana Santun: 露出を控えた上品なイスラム服飾）」の中心地（メッカ）として、輝かしい国際的名声を確立しつつあります。数十年前にはムスリム女性の服装スタイルが中東風のゆったりした黒一色の長衣（ガミス）の中に画一的・禁欲的に閉じ込められていたとすれば、その情勢は今や、極めてダイナミックで色彩に満ち、グローバルな現代トレンドを意識した数十兆ルピア規模のクリエイティブ産業へと完全に変貌を遂げました。",
            "インドネシアのムスリム・ファッションの美意識の革命の鍵は、イスラム法の戒律の遵守という宗教的価値観と、群島の伝統織物（ワストラ・ヌサンタラ: wastra nusantara）の至高の豊かさを大胆に融合させた地元女性デザイナーたちの挑戦にありました。ジャワの手描きバティック、東ヌサ・トゥンガラ州のイカット絣、ミナンカバウの優雅なソンケット金糸織物といった先祖伝来の伝統布が、上品な既製服（chic ready-to-wear）、オフィス用プロフェッショナル・ブレザー、高級イブニングドレスへと創造的に一新されたのです。明るいパステルカラーの多様性と熱帯に適した涼しいコットン素材の採用は、インドネシアのムスリム服を赤道直下の気候に完璧に適合させ、現代の若い女性たち（ヒジャバーズ: hijabers）から熱狂的な支持を集めています。",
            "ジャカルタ・ムスリム・ファッション・ウィーク（JMFW）などの有力なファッションの祭典は、中東、欧州、米国からの海外バイヤーの熱い注目を一貫して集めています。ディアン・ペランギ（Dian Pelangi）やリア・ミランダ（Ria Miranda）といった国内トップクラスのデザイナーたちは、ニューヨークやパリの国際ファッションウィークの舞台で自身のコレクションを発表し大成功を収めました。急速に普及するEコマースとSNS上のインフルエンサー網に支えられ、インドネシアのモデストファッション産業は単に国家の文化的アイデンティティを強固にするだけでなく、宗教的信仰心と現代の美意識が調和的かつインクルーシブに両立し得ることを世界に証明しています。"
        ],
        "grammar_points": [
            "高雅な古典文学語「wastra」: サンスクリット語起源で、単なる衣服用の布地（kain）を超えた「歴史的・芸術的価値を持つ伝統織物（バティック、イカット、ソンケットなど）」を総称する格調高い文化財用語です。",
            "ジャワ語起源の愛好動詞「digandrungi」: gandrung（恋い慕う、夢中になる）に受動態接辞 di-...-i が付いたもので、「若者たちの間で熱烈に愛好されている、大ブームとなっている」という熱狂を生き生きと描写します。",
            "現代英語と結合した社会名詞「hijabers」: hijab（イスラムの頭髪覆いベール）に英語の接尾辞 -ers（〜する人々）を結合したインドネシア発祥の造語で、保守的な枠組みを脱してポップにおしゃれを楽しむ新世代のムスリム女性コミュニティを指します。"
        ],
        "quiz": [
            {
                "question": "インドネシアの「モデスト・ファッション（Busana Santun）」が世界的な大人気を集めた美意識の革新は何ですか？",
                "options": ["A. イスラムの戒律の遵守に、バティックやイカットなどの伝統布と涼しいパステルカラーを融合させたこと", "B. 中東の黒い長衣（アバヤ）をそのまま輸入して着ていること", "C. すべての服を紙で作っていること", "D. ヒジャブの着用を禁止したこと"],
                "answer": "A. イスラムの戒律の遵守に、バティックやイカットなどの伝統布と涼しいパステルカラーを融合させたこと",
                "explanation": "本文第2段落にある通り、伝統布（wastra）の美しさと熱帯に適したパステルカラーの融合が強みです。"
            },
            {
                "question": "ニューヨークやパリのファッションウィークでコレクションを発表した、インドネシアを代表する先駆的ムスリム女性デザイナーは誰ですか？",
                "options": ["A. Dian Pelangi", "B. Joko Widodo", "C. Nadiem Makarim", "D. Pramoedya Ananta Toer"],
                "answer": "A. Dian Pelangi",
                "explanation": "本文第3段落にある通り、カラフルなバティック・ヒジャブで世界に進出したのはDian Pelangiです。"
            },
            {
                "question": "文中の「digandrungi」という言葉の意味として最も適切なものはどれですか？",
                "options": ["A. 熱狂的に好まれている、大人気である", "B. 厳しく批判されている", "C. 値段が高すぎて売れない", "D. 法律で禁止されている"],
                "answer": "A. 熱狂的に好まれている、大人気である",
                "explanation": "gandrung（恋焦がれる）から派生した言葉で、「熱烈に愛されている、大人気である」を意味します。"
            }
        ],
        "column_title": "社会コラム：スハルト独裁時代の「ヒジャブ禁止」から市民権獲得への歩み",
        "column_text": "今では大統領夫人から国会議員、女子高生まで当たり前に着用されているヒジャブ（インドネシアでは伝統的にジルバブ: Jilbab）ですが、実はスハルト新体制（Orde Baru）時代の1980年代には「政治的イスラム過激主義の象徴」と見なされ、公立学校での着用が厳格に禁止されていました。女子生徒たちは停学処分に抗議して法廷闘争を繰り広げ、1991年にようやく解禁を勝ち取りました。現代の自由でファッショナブルなヒジャブ文化の根底には、女性たちが信教の自由を求めて闘った現代史のドラマが横たわっています。"
    },
    {
        "filename": "docs/contemporary/30-heritage-railway-revival.md",
        "title": "植民地時代の歴史的鉄道遺産の復活：観光列車アマバラワと山岳SLの旅路",
        "category_badge": "現代社会・歴史遺産と観光鉄道",
        "lead": "オランダ東インド植民地時代にジャワ島のプランテーション（砂糖・コーヒー）輸送のために建設された歴史的な鉄道網。近年、国営鉄道会社PT KAIや鉄道ファン（Railfans）の手により、中部ジャワ州アマバラワの歯軌条（アプト式）蒸気機関車や、スマトラ島西部の鉱山鉄道など、貴重な鉄道遺産の動態保存とヘリテージ・ツーリズムが急速な盛り上がりを見せています。植民地の記憶と産業遺産の保存の最前線を深層読解します。",
        "text_id": """Jejak sejarah kolonialisme Belanda di Indonesia meninggalkan salah satu warisan teknik sipil paling monumental di kawasan Asia: jaringan jalan rel kereta api yang membentang ribuan kilometer melintasi pegunungan terjal dan perkebunan tropis di Pulau Jawa dan Sumatra. Dibangun pada akhir abad ke-19 terutama untuk melayani eksploitasi komoditas ekspor—seperti gula, kopi, tembakau, dan batu bara—jalur-jalur rel bersejarah ini sempat terbengkalai dan mengalami penonaktifan massal (deaktivasi) pada era 1970-1980-an akibat kalah bersaing dengan moda transportasi jalan raya.

Namun, dalam satu dekade terakhir, kesadaran pelestarian sejarah bangsa membangkitkan kembali gairah penyelamatan warisan perkeretaapian (heritage railway revival). Diprakarsai oleh PT Kereta Api Indonesia (KAI) bekerja sama dengan komunitas pencinta kereta api (railfans) dan pemerhati sejarah, berbagai stasiun tua yang megah berarsitektur Art Deco dipugar kembali ke bentuk aslinya. Ikon paling legendaris dari gerakan restorasi ini adalah Museum Kereta Api Ambarawa di Jawa Tengah, yang berhasil menghidupkan kembali lokomotif uap kuno bergerigi (rack railway) buatan Esslingen Jerman tahun 1902 untuk mendaki lereng Gunung Ungaran yang curam.

Keberhasilan menghidupkan kembali lokomotif uap tua dan jalur wisata pegunungan—seperti jalur Sawahlunto di Sumatra Barat yang telah diakui sebagai Situs Warisan Dunia UNESCO (Ombilin Coal Mining Heritage)—tidak hanya mendatangkan berkah devisa pariwisata sejarah (heritage tourism), melainkan juga menjadi sarana edukasi publik mengenai sejarah kelam kerja paksa (rodi) era kolonial. Mengintegrasikan konservasi mesin-mesin uap purba dengan pemberdayaan ekonomi masyarakat di sepanjang lintasan rel menjadi bukti bahwa warisan masa lalu dapat dirawat sebagai aset masa depan yang membanggakan.""",
        "vocab": [
            ["warisan teknik sipil", "名詞句", "土木工学遺産（civil engineering heritage）", "Rel kereta api adalah warisan teknik sipil kolonial."],
            ["terbengkalai", "動詞/形容詞", "放置された、荒れ果てた", "Banyak jalur rel kuno sempat terbengkalai puluhan tahun."],
            ["lokomotif uap bergerigi", "名詞句", "歯軌条（アプト式）蒸気機関車", "Lokomotif uap bergerigi mampu mendaki lereng curam."],
            ["arsitektur Art Deco", "名詞句", "アール・デコ建築様式", "Stasiun kereta tua dipugar dengan gaya arsitektur Art Deco."],
            ["pariwisata sejarah (heritage tourism)", "名詞句", "歴史・産業遺産観光", "Jalur Ambarawa menjadi ikon pariwisata sejarah."],
            ["kerja paksa (rodi)", "名詞句", "強制労働（オランダ植民地時代の過酷な苦役）", "Rel dibangun dengan penderitaan kerja paksa rodi."]
        ],
        "translation": [
            "オランダによるインドネシア植民地支配の歴史的痕跡は、アジア地域において最も記念碑的な土木工学遺産の一つを残しました。ジャワ島とスマトラ島の険しい山岳地帯や熱帯プランテーションを縦横に縫って何千キロメートルにもわたり敷設された鉄道線路網です。19世紀末、主として砂糖、コーヒー、タバコ、石炭といった輸出向け商品作物の搾取輸送に供するために建設されたこれらの歴史的鉄路は、道路交通機関との競争に敗れた結果、1970〜80年代にかけて放置され、大規模な廃線・休止（デアクティバシ）の憂き目に遭いました。",
            "しかし、ここ10年間の自国の歴史保存への意識の高まりは、鉄道産業遺産の救済への熱気（ヘリテージ・レイルウェイ・リバイバル）を力強く蘇らせました。国営鉄道PT KAIが熱心な鉄道愛好家コミュニティ（レイルファンズ: railfans）や歴史研究家と連携して主導し、アール・デコ建築様式を誇る堂々たる数々の古い歴史的駅舎が往時の姿へと美しく復元（修復）されました。この復元運動の最も伝説的なアイコンは、中部ジャワ州のアマバラワ鉄道博物館です。同館は、ウンガラン火山の険しい急勾配を登坂するため、1902年ドイツ・エスリンゲン社製のラック式（歯軌条）蒸気機関車の動態復活に見事に成功したのです。",
            "古い蒸気機関車や山岳観光鉄路の復活の成功（ユネスコ世界文化遺産に登録された西スマトラ州サワルントのオンビリン炭鉱鉄道遺産など）は、単に歴史遺産観光（ヘリテージ・ツーリズム）による観光外貨をもたらすだけでなく、植民地時代の過酷な強制労働（ロディ: rodi）の暗黒の歴史を記憶するための公的教育の場としても機能しています。古代の蒸気機関の動態保存と、線路沿いの住民コミュニティの経済的エンパワーメントを統合することは、過去の遺産が誇るべき未来の資産として大切に守り継がれ得ることを証明しています。"
        ],
        "grammar_points": [
            "語根 bengkalai からの受動状態形容詞「terbengkalai」: 接頭辞 ter- が付くことで、「誰にも顧みられず放置され、荒れ果てたままになっている状態」を表す名詞修飾語です（proyek terbengkalai: 頓挫し放置された事業）。",
            "歴史的借用語「rodi（強制労働）」: オランダ語の herendienst（領主への賦役・夫役）から派生した言葉で、日本占領時代の労務者（Romusha）と並び、過酷な植民地支配の苦役を象徴する歴史用語です。",
            "受動使役動詞「dipugar」: pugar（復元する、修復する）の受動態で、歴史的建造物や遺跡（Candiや古駅舎）を原形を損なわずに美しく修復・リストアする際の公式用語です。"
        ],
        "quiz": [
            {
                "question": "中部ジャワのアマバラワ鉄道博物館（Museum Kereta Api Ambarawa）が世界的に誇る、動態保存に成功した貴重な鉄道技術は何ですか？",
                "options": ["A. ウンガラン火山の急勾配を登るためのドイツ製アプト式（歯軌条）蒸気機関車", "B. 新幹線と同じ最高時速300kmの超高速リニアモーターカー", "C. 水中を走る潜水鉄道", "D. すべて木で作られたレール"],
                "answer": "A. ウンガラン火山の急勾配を登るためのドイツ製アプト式（歯軌条）蒸気機関車",
                "explanation": "本文第2段落にある通り、1902年ドイツ製のアプト式ラックレール蒸気機関車の動態保存で有名です。"
            },
            {
                "question": "オランダ植民地時代の鉄道建設にまつわる暗い歴史として本文に言及されている過酷な使役は何ですか？",
                "options": ["A. 先住民族に対する過酷な強制労働（rodi）の歴史", "B. 鉄道の利用が王族だけに制限されていたこと", "C. 切符がダイヤモンドでしか買えなかったこと", "D. 列車が毎日脱線していたこと"],
                "answer": "A. 先住民族に対する過酷な強制労働（rodi）の歴史",
                "explanation": "本文第3段落にある通り、植民地時代の過酷な強制労働（rodi）の犠牲の上に線路が敷設されました。"
            },
            {
                "question": "文中の「terbengkalai」という言葉の意味として最も適切なものはどれですか？",
                "options": ["A. 放置された、荒れ果てたままになっている", "B. 非常に賑わっている", "C. 厳重に警備されている", "D. 新しく建設されたばかりの"],
                "answer": "A. 放置された、荒れ果てたままになっている",
                "explanation": "bengkalai（中途半端）から派生し、「放置されて荒廃した状態」を意味します。"
            }
        ],
        "column_title": "鉄道コラム：西スマトラの「Mak Itam（黒いお母さん）」SLの奇跡の復活",
        "column_text": "ユネスコ世界文化遺産に登録された西スマトラ州サワルント（Sawahlunto）の炭鉱鉄道には、「Mak Itam（黒いお母さん）」の愛称で住民から親しまれた山岳蒸気機関車（E1060号機）がありました。長年ボイラーが故障し静態保存されていましたが、PT KAIの熟練技術者たちが古い設計図を頼りに部品を一から手作りで削り出し、2022年に再び黒煙を上げて汽笛を轟かせました。かつて石炭と苦役の歴史を運んだ鉄路は今、地域の誇りと希望を乗せて走っています。"
    }
]

def generate_contemporary_article(data):
    md = f"""# {data['title']}

<div class="article-meta">
  <span class="category-badge">{data['category_badge']}</span>
  <span class="read-time">読了目安: 15分</span>
  <span class="level-badge">B2〜C1（中上級〜上級論説）</span>
</div>

## はじめに

{data['lead']}

---

## 1. 本文長文読解（インドネシア語論説文）

{data['text_id']}

---

## 2. 重要語彙・専門用語・必須コロケーション

本記事に登場した重要語彙および論説文特有の専門用語・コロケーション一覧です。

| インドネシア語 | 品詞 | 日本語の語義 | 例文・共起パターン |
| :--- | :--- | :--- | :--- |
"""
    for v in data['vocab']:
        md += f"| **{v[0]}** | {v[1]} | {v[2]} | {v[3]} |\n"

    md += """
---

## 3. 本文の対訳・日本語全訳

段落ごとの対訳です。論理展開と文構造を照らし合わせながら確認してください。

"""
    for idx, trans_para in enumerate(data['translation'], 1):
        md += f"""### 第{idx}段落の日本語訳

{trans_para}

"""

    md += """---

## 4. 文法・論理構造の深層解説

現代の一流紙や専門レポートで用いられる高度な構文・レジスターの特徴を解説します。

"""
    for pt in data['grammar_points']:
        md += f"- **構文ポイント**: {pt}\n"

    md += """
---

## 5. 読解理解度クイズ（全3問）

本文の内容を正確に把握できたか、以下の3択クイズで確認してみましょう。

"""
    for q_idx, q in enumerate(data['quiz'], 1):
        md += f"""### 第{q_idx}問: {q['question']}

"""
        for opt in q['options']:
            md += f"- {opt}\n"
        md += f"""
??? note "正解と解説を確認する"
    **正解**: 「**{q['answer']}**」
    
    **解説**: {q['explanation']}

"""

    md += f"""---

## 6. {data['column_title']}

{data['column_text']}

---

## 7. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return md

def main():
    os.makedirs("docs/contemporary", exist_ok=True)
    for data in articles:
        content = generate_contemporary_article(data)
        with open(data["filename"], "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {data['filename']}")

if __name__ == "__main__":
    main()
