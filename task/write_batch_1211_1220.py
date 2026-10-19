# -*- coding: utf-8 -*-
import os
import re

stories = [
    {
        "id": "1211",
        "slug": "level-2-01-travel-to-jogja",
        "title": "【Level 2 (A2)】Petualangan ke Yogyakarta（夜行列車で行く古都ジョグジャカルタ旅）",
        "level": "CEFR A2（初級レベル・想定語彙数 600〜1,000語）",
        "desc": "夜行列車での移動、マリオボロ通りの活気、クラトン王宮、伝統料理グドゥグの体験を通じて、旅と移動の初級A2表現を習得する。",
        "text": """Liburan semester kali ini menjadi petualangan yang sangat istimewa bagiku. Ayah mengajak kami sekeluarga berlibur ke Yogyakarta, kota budaya yang penuh dengan pesona sejarah. Kami memilih untuk naik kereta api eksekutif malam dari Stasiun Gambir di Jakarta.

Kereta api mulai melaju tepat pada jam sembilan malam. Di dalam gerbong, suasananya sangat tenang, sejuk, dan nyaman dengan kursi yang empuk. Aku duduk di dekat jendela, memandangi lampu-lampu kota yang perlahan menjauh dan berganti menjadi kegelapan pedesaan. Sebelum tertidur lelap, kami menikmati makan malam berupa nasi goreng hangat yang disediakan oleh petugas kereta api.

Keesokan paginya, tepat saat matahari terbit di ufuk timur, kereta kami tiba di Stasiun Tugu Yogyakarta. Udara pagi kota Jogja menyambut kami dengan kehangatan khas masyarakat Jawa. Kami segera naik becak tradisional menuju hotel di kawasan Jalan Malioboro. Di sepanjang Malioboro, deretan toko suvenir, pedagang batik, dan seniman jalanan mulai bersiap membuka lapak mereka.

Siang harinya, kami mengunjungi Keraton Yogyakarta, istana megah tempat tinggal Sultan. Kami mengagumi arsitektur Jawa klasik yang anggun sambil mendengarkan alunan musik gamelan yang lembut. Sebelum kembali ke hotel, kami mampir ke sebuah warung lesehan untuk mencicipi Gudeg Jogja yang manis dan gurih. Perjalanan ini membuatku semakin mencintai kekayaan budaya Indonesia.""",
        "paragraphs": [
            ("Liburan semester kali ini menjadi petualangan yang sangat istimewa bagiku. Ayah mengajak kami sekeluarga berlibur ke Yogyakarta, kota budaya yang penuh dengan pesona sejarah. Kami memilih untuk naik kereta api eksekutif malam dari Stasiun Gambir di Jakarta.",
             "今回の学期休みは、僕にとってとても特別な冒険となりました。父は僕たち家族全員を連れて、歴史の魅力に満ちた文化の街ジョグジャカルタへ旅行に出かけました。僕たちはジャカルタのガンビル駅からエグゼクティブ夜行列車に乗ることを選びました。",
             "petualangan（冒険）、istimewa（特別な）、kota budaya（文化都市）、pesona sejarah（歴史の魅力）。"),
            ("Kereta api mulai melaju tepat pada jam sembilan malam. Di dalam gerbong, suasananya sangat tenang, sejuk, dan nyaman dengan kursi yang empuk. Aku duduk di dekat jendela, memandangi lampu-lampu kota yang perlahan menjauh dan berganti menjadi kegelapan pedesaan. Sebelum tertidur lelap, kami menikmati makan malam berupa nasi goreng hangat yang disediakan oleh petugas kereta api.",
             "列車は夜の9時ちょうどに出発しました。車両の中はふかふかの座席で、とても静かで涼しく、快適でした。僕は窓の近くに座り、ゆっくりと遠ざかって田舎の暗闇へと変わっていく街の明かりを眺めていました。ぐっすり眠りに落ちる前に、僕たちは乗務員から提供された温かいナシゴレンの夕食を楽しみました。",
             "melaju（スピードに乗って走る）、gerbong（客車車両）、tertidur lelap（ぐっすり眠る）。"),
            ("Keesokan paginya, tepat saat matahari terbit di ufuk timur, kereta kami tiba di Stasiun Tugu Yogyakarta. Udara pagi kota Jogja menyambut kami dengan kehangatan khas masyarakat Jawa. Kami segera naik becak tradisional menuju hotel di kawasan Jalan Malioboro. Di sepanjang Malioboro, deretan toko suvenir, pedagang batik, dan seniman jalanan mulai bersiap membuka lapak mereka.",
             "翌朝、ちょうど東の地平線に太陽が昇る頃、僕たちの列車はジョグジャカルタのトゥグ駅に到着しました。ジョグジャの朝の空気は、ジャワの人々特有の温かさで僕たちを出迎えてくれました。僕たちはすぐに伝統的なベチャ（輪タク）に乗って、マリオボロ通り地区のホテルへ向かいました。マリオボロ通り沿いには、お土産屋の並び、バティック商人、ストリートアーティストたちが露店を開く準備を始めていました。",
             "keesokan paginya（翌朝）、becak（輪タク・三輪自転車）、lapak（露店・屋台）。"),
            ("Siang harinya, kami mengunjungi Keraton Yogyakarta, istana megah tempat tinggal Sultan. Kami mengagumi arsitektur Jawa klasik yang anggun sambil mendengarkan alunan musik gamelan yang lembut. Sebelum kembali ke hotel, kami mampir ke sebuah warung lesehan untuk mencicipi Gudeg Jogja yang manis dan gurih. Perjalanan ini membuatku semakin mencintai kekayaan budaya Indonesia.",
             "昼には、僕たちはスルタン（王）が暮らす壮大な宮殿であるジョグジャカルタ王宮（クラトン）を訪れました。僕たちは柔らかなガムラン音楽の調べを聴きながら、優美な古典ジャワ建築に見とれました。ホテルに戻る前に、甘くて旨味のある名物ジョグジャ・グドゥグを味わうために、レセハン（床座敷）の屋台に立ち寄りました。この旅によって、僕はインドネシアの豊かな文化をますます愛するようになりました。",
             "Keraton（王宮）、gamelan（伝統青銅打楽器合奏）、warung lesehan（ゴザに座る床座敷食堂）、Gudeg（若ジャックフルーツの甘辛煮込み）。")
        ],
        "vocab": [
            ("petualangan", "名詞", "ualang", "冒険、アドベンチャー", "Mendaki gunung adalah petualangan seru."),
            ("istimewa", "形容詞", "-", "特別な、特異な", "Yogyakarta adalah daerah istimewa."),
            ("melaju", "動詞", "laju", "疾走する、速度を上げて進む", "Kereta cepat melaju kencang di rel."),
            ("tertidur lelap", "動詞句", "tidur", "ぐっすり眠る、熟睡する", "Bayi itu tertidur lelap dalam buaian."),
            ("keesokan paginya", "副詞句", "esok", "翌朝、次の日の朝", "Keesokan paginya kami mulai menjelajah kota."),
            ("becak", "名詞", "-", "ベチャ（前部に座席がある三輪自転車・輪タク）", "Naik becak menyusuri jalan Malioboro."),
            ("seniman", "名詞", "seni", "芸術家、アーティスト", "Banyak seniman berkumpul di Jogja."),
            ("keraton", "名詞", "ratu", "王宮、宮殿（ジャワのスルタン宮殿）", "Keraton Yogyakarta dijaga oleh abdi dalem."),
            ("alunan musik", "名詞句", "alun", "音楽の調べ、心地よい音色", "Alunan gamelan terdengar syahdu."),
            ("warung lesehan", "名詞句", "leseh", "床座敷形式の屋台食堂", "Makan gudeg di warung lesehan Malioboro.")
        ],
        "grammar_points": """1. **時の推移を表す接続表現**:
   - *tepat pada jam sembilan*（9時ちょうどに）
   - *sebelum tertidur lelap*（熟睡する前に）
   - *keesokan paginya*（翌朝）
   - *siang harinya*（その日の昼には）
2. **比較・変化を表す副詞 `semakin ...`（ますます〜）**:
   - *semakin mencintai*（ますます愛するようになる）
   - *semakin besar*（ますます大きくなる）
   - *semakin lama semakin dingin*（時間が経つにつれてますます寒くなる）
3. **場所の広がりを表す前置詞句 `di sepanjang ...`（〜沿いに）**:
   - *di sepanjang jalan*（通り沿いに）
   - *di sepanjang pantai*（海岸沿いに）""",
        "quizzes": [
            ("ブディ君一家がジョグジャカルタへ行くために利用した交通機関は何ですか？",
             ["スカルノハッタ空港からの飛行機", "ガンビル駅からのエグゼクティブ夜行列車（kereta api eksekutif malam）", "高速道路を走る自家用車"],
             "ガンビル駅からのエグゼクティブ夜行列車（kereta api eksekutif malam）",
             "第1段落に「Kami memilih untuk naik kereta api eksekutif malam dari Stasiun Gambir di Jakarta.」とあります。"),
            ("トゥグ駅に到着後、マリオボロ通りのホテルへ向かうために乗った乗り物は何ですか？",
             ["地下鉄（MRT）", "伝統的な三輪自転車ベチャ（becak tradisional）", "オートバイタクシー（ojek）"],
             "伝統的な三輪自転車ベチャ（becak tradisional）",
             "第3段落に「Kami segera naik becak tradisional menuju hotel...」とあります。"),
            ("ジョグジャカルタ王宮（クラトン）を見学した後に食べた、甘く煮込んだ名物郷土料理は何ですか？",
             ["ルンダン（Rendang）", "グドゥグ（Gudeg Jogja）", "バソ（Bakso）"],
             "グドゥグ（Gudeg Jogja）",
             "第4段落に「...mencicipi Gudeg Jogja yang manis dan gurih.」とあります。")
        ],
        "culture": """### ジョグジャカルタ特別州（DIY）と古都の魅力
ジョグジャカルタ（Yogyakarta）は、インドネシアで唯一、伝統的なスルタン（イスラム王族・ハメンクブウォノ家）が州知事を世襲する「特別州（Daerah Istimewa）」です。
街の中心にある「マリオボロ通り（Jalan Malioboro）」は夜になると歩道にゴザを敷いた「Lesehan（レセハン）」と呼ばれる屋台がずらりと並び、甘辛い郷土料理「Gudeg（グドゥグ: 若いジャックフルーツをココナッツミルクとパームシュガーで煮込んだ料理）」や、ストリートミュージシャンの生演奏を楽しむ人々で深夜までにぎわいます。"""
    },
    {
        "id": "1212",
        "slug": "level-2-02-school-holiday-village",
        "title": "【Level 2 (A2)】Liburan di Desa Kakek（祖父の村での田植え体験と川遊び）",
        "desc": "農村でのリアルな田植え（menanam padi）体験と、清流での水遊び。農業語彙と自然との触れ合いを描く初級A2ストーリー。",
        "text": """Liburan sekolah semester ini kuputuskan untuk tinggal lebih lama di desa kakek di Garut. Aku ingin merasakan secara langsung bagaimana kehidupan para petani yang bekerja keras menghasilkan beras untuk masyarakat.

Pagi-pagi sekali, saat ayam jantan berkokok bersahut-sahutan, kakek sudah mengajakku pergi ke sawah. Tanah sawah sudah selesai dibajak dan sekarang dipenuhi oleh lumpur basah yang gembur. Kakek memberiku caping, yaitu topi anyaman bambu berbentuk kerucut untuk melindungi kepala dari terik sinar matahari.

Bersama para petani desa, aku belajar cara menanam bibit padi. Kami berjalan mundur perlahan sambil menancapkan beberapa helai bibit padi ke dalam lumpur sedalam beberapa sentimeter. Pada awalnya, aku merasa kesulitan menjaga keseimbangan dan kakiku sering terperosok ke dalam lumpur. Namun, kakek dengan sabar mengajariku hingga aku bisa menanam bibit padi dengan rapi dan lurus.

Menjelang siang, udara mulai terasa panas. Kakek mengajakku membersihkan badan di sungai berbatu yang airnya sangat jernih dan segar. Kami duduk di atas batu besar sambil menikmati makan siang berupa nasi liwet hangat, ikan asin gurih, dan sambal terasi pedas. Petualangan di sawah mengajariku untuk selalu menghargai setiap butir nasi yang kita makan.""",
        "paragraphs": [
            ("Liburan sekolah semester ini kuputuskan untuk tinggal lebih lama di desa kakek di Garut. Aku ingin merasakan secara langsung bagaimana kehidupan para petani yang bekerja keras menghasilkan beras untuk masyarakat.",
             "今学期の学校休みは、ガルットにある祖父の村により長く滞在することに決めました。僕は、人々のために米を生産しようと懸命に働く農民たちの生活を直接体験してみたかったのです。",
             "kuputuskan（私が決心した・語幹受動態）、secara langsung（直接に）、menghasilkan beras（米を生産する）。"),
            ("Pagi-pagi sekali, saat ayam jantan berkokok bersahut-sahutan, kakek sudah mengajakku pergi ke sawah. Tanah sawah sudah selesai dibajak dan sekarang dipenuhi oleh lumpur basah yang gembur. Kakek memberiku caping, yaitu topi anyaman bambu berbentuk kerucut untuk melindungi kepala dari terik sinar matahari.",
             "朝とても早く、雄鶏が競い合って鳴く頃、祖父はすでに僕を連れて田んぼへ向かいました。田んぼの土はすでに耕し終えており、今は柔らかい湿った泥で満たされています。祖父は僕に、照りつける日差しから頭を守るための円錐形の竹編み帽子であるチャーピン（caping）をくれました。",
             "ayam jantan berkokok（雄鶏が鳴く）、lumpur basah（湿った泥）、caping（伝統スゲ笠・農帽）。"),
            ("Bersama para petani desa, aku belajar cara menanam bibit padi. Kami berjalan mundur perlahan sambil menancapkan beberapa helai bibit padi ke dalam lumpur sedalam beberapa sentimeter. Pada awalnya, aku merasa kesulitan menjaga keseimbangan dan kakiku sering terperosok ke dalam lumpur. Namun, kakek dengan sabar mengajariku hingga aku bisa menanam bibit padi dengan rapi dan lurus.",
             "村の農民たちと一緒に、僕は稲の苗の植え方を学びました。僕たちは数センチの深さの泥の中に数本の稲の苗を差し込みながら、ゆっくりと後ろ向きに歩きました。最初はバランスを保つのが難しく、僕の足は泥の中に何度も足を取られました。しかし、祖父が根気よく教えてくれたおかげで、まっすぐ綺麗に苗を植えられるようになりました。",
             "menanam bibit padi（田植えをする）、berjalan mundur（後ろ歩きする・田植え特有の動き）、menancapkan（突き刺す）。"),
            ("Menjelang siang, udara mulai terasa panas. Kakek mengajakku membersihkan badan di sungai berbatu yang airnya sangat jernih dan segar. Kami duduk di atas batu besar sambil menikmati makan siang berupa nasi liwet hangat, ikan asin gurih, dan sambal terasi pedas. Petualangan di sawah mengajariku untuk selalu menghargai setiap butir nasi yang kita makan.",
             "昼が近づくにつれ、空気は暑く感じられ始めました。祖父は僕を連れて、水がとても清らかで爽やかな岩の多い小川で体を洗いました。僕たちは大きな岩の上に座りながら、温かいナシ・リウェット、塩気の効いた魚の干物、ピリ辛の海老発酵味噌サンバル（サンバル・トラシ）の昼食を楽しみました。田んぼでの冒険は、僕たちが口にする米のひと粒ひと粒を常に感謝して大切にすることを教えてくれました。",
             "menjelang（〜に近づく頃）、nasi liwet（香草やスパイスで炊き込んだご飯）、menghargai setiap butir nasi（一粒の米を大切にする）。")
        ],
        "vocab": [
            ("ayam jantan", "名詞句", "ayam", "雄鶏（おんどり）", "Ayam jantan berkokok di pagi hari."),
            ("berkokok", "動詞", "kokok", "（鶏が）コケコッコーと鳴く", "Suara ayam berkokok membangunkan warga."),
            ("caping", "名詞", "-", "農作業用の円錐形スゲ笠・竹編み笠", "Petani memakai caping di terik matahari."),
            ("bibit padi", "名詞句", "bibit", "稲の苗（幼植物）", "Bibit padi hijau siap ditanam di sawah."),
            ("menancapkan", "動詞", "tancap", "突き刺す、植え込む", "Petani menancapkan bibit ke dalam lumpur."),
            ("keseimbangan", "名詞", "timbang", "バランス、平衡感覚", "Sulit menjaga keseimbangan di lumpur licin."),
            ("menjelang", "前置詞/動詞", "jelang", "（時が）〜に近づいて、〜の手前に", "Udara dingin menjelang fajar."),
            ("nasi liwet", "名詞句", "liwet", "ナシ・リウェット（スンダ風炊き込みご飯）", "Nasi liwet Sunda disajikan di atas daun pisang."),
            ("ikan asin", "名詞句", "ikan", "魚の干物、塩魚", "Ikan asin sangat gurih dimakan dengan sambal."),
            ("setiap butir nasi", "名詞句", "butir", "一粒一粒の米", "Kita harus menghargai setiap butir nasi.")
        ],
        "grammar_points": """1. **動作の様態を表す `sambil + 動詞`（〜しながら）**:
   - *berjalan mundur sambil menancapkan bibit*（苗を刺しながら後ろ歩きする）
   - *duduk di batu sambil menikmati makan siang*（昼食を楽しみながら岩に座る）
2. **助数詞 `butir`（小さな粒状のものを数える）**:
   - *sebutir telur*（卵1個）
   - *sebutir beras / butir nasi*（米1粒）
   - *sebutir mutiara*（真珠1粒）
3. **助数詞 `helai`（薄いもの・布・紙・葉・毛髪を数える）**:
   - *sehelai daun*（葉っぱ1枚）
   - *beberapa helai bibit padi*（稲の苗数本）""",
        "quizzes": [
            ("おじいちゃんが強い日差しから頭を守るためにブディ君にくれた伝統的な帽子は何ですか？",
             ["ヘルメット", "チャーピン（caping: 円錐形の竹編み笠）", "野球帽"],
             "チャーピン（caping: 円錐形の竹編み笠）",
             "第2段落に「Kakek memberiku caping, yaitu topi anyaman bambu berbentuk kerucut...」とあります。"),
            ("田んぼに苗を植える際、農民たちはどのような歩き方で作業しますか？",
             ["前向きに小走りで進む", "ゆっくりと後ろ向きに歩く（berjalan mundur）", "横跳びで進む"],
             "ゆっくりと後ろ向きに歩く（berjalan mundur）",
             "第3段落に「Kami berjalan mundur perlahan sambil menancapkan beberapa helai bibit padi...」とあります。"),
            ("田植えの冒険を通じて、ブディ君が学んだ最も大切な教訓は何ですか？",
             ["川の魚を捕まえる技術", "食べる米のひと粒ひと粒を常に大切にし感謝する心（menghargai setiap butir nasi）", "泥んこ遊びの楽しさ"],
             "食べる米のひと粒ひと粒を常に大切にし感謝する心（menghargai setiap butir nasi）",
             "第4段落末尾に「Petualangan di sawah mengajariku untuk selalu menghargai setiap butir nasi yang kita makan.」とあります。")
        ],
        "culture": """### インドネシアの稲作文化と「Dewi Sri（稲の女神）」
インドネシアは世界有数の米消費国であり、主食である米（Padi / Beras / Nasi）は命の源として神聖視されています。
ジャワ島やバリ島では古くから「デウィ・スリ（Dewi Sri: 豊穣と稲の女神）」が信仰されており、田植えの前や収穫祭（Panen Raya）には神への感謝の儀式が執り行われます。子供たちは幼い頃から「Makan nasi sampai bersih, jangan ada yang tersisa（お米は一粒も残さず綺麗に食べなさい）」と厳しくしつけられます。"""
    },
    {
        "id": "1213",
        "slug": "level-2-03-cooking-rendang",
        "title": "【Level 2 (A2)】Belajar Memasak Rendang Padang（本場パダン料理ルンダン作りに挑戦）",
        "desc": "世界で最も美味しい料理に選ばれた「ルンダン（Rendang）」の伝統的調理プロセス。料理用語、スパイス、長時間の煮込み工程を学ぶ。",
        "text": """Menjelang hari raya Idulfitri, suasana di rumah nenek di Padang terasa sangat sibuk. Semua anggota keluarga berkumpul untuk mempersiapkan hidangan istimewa. Masakan utama yang wajib ada di meja makan adalah Rendang Daging Sapi, masakan tradisional khas Minangkabau yang terkenal di seluruh dunia.

Bibi Fatimah mengajariku langkah-langkah memasak rendang secara tradisional menggunakan kuali besi besar di atas tungku kayu bakar. Pertama-tama, kami menyiapkan bumbu rempah-rempah yang melimpah, seperti bawang merah, bawang putih, jahe, lengkuas, kunyit, serai, daun jeruk, dan cabai merah giling. Semua bumbu tersebut dihaluskan dengan cobek batu hingga mengeluarkan aroma wangi yang khas.

Langkah kedua adalah merebus santan kelapa kental bersama bumbu halus dan rempah aromatik. Santan tersebut harus terus diaduk perlahan tanpa henti agar tidak pecah. Setelah santan mendidih dan mengeluarkan minyak kemerahan (tahap gulai), potongan daging sapi segar dimasukkan ke dalam kuali.

Proses memasak rendang membutuhkan kesabaran yang luar biasa. Selama lebih dari empat jam, api dijaga tetap stabil sambil daging terus diaduk hingga cairan santan mengering dan berubah warna menjadi cokelat tua kehitaman (tahap kalio, lalu menjadi rendang kering). Dagingnya terasa sangat empuk dan bumbu rempahnya meresap sempurna hingga ke serat terdalam. Memasak rendang mengajariku arti ketabahan dan kerja keras.""",
        "paragraphs": [
            ("Menjelang hari raya Idulfitri, suasana di rumah nenek di Padang terasa sangat sibuk. Semua anggota keluarga berkumpul untuk mempersiapkan hidangan istimewa. Masakan utama yang wajib ada di meja makan adalah Rendang Daging Sapi, masakan tradisional khas Minangkabau yang terkenal di seluruh dunia.",
             "イスラム教の断食明け大祭（イード・アル＝フィトル）を控え、パダンにある祖母の家の雰囲気はとても慌ただしくなっています。特別なごちそうを準備するために、家族全員が集まりました。食卓に欠かせない主菜は、世界中で有名なミナンカバウ伝統の牛肉のルンダンです。",
             "hari raya Idulfitri（断食明け大祭・レバラン）、hidangan istimewa（特別なごちそう）、khas Minangkabau（ミナンカバウ特有の）。"),
            ("Bibi Fatimah mengajariku langkah-langkah memasak rendang secara tradisional menggunakan kuali besi besar di atas tungku kayu bakar. Pertama-tama, kami menyiapkan bumbu rempah-rempah yang melimpah, seperti bawang merah, bawang putih, jahe, lengkuas, kunyit, serai, daun jeruk, dan cabai merah giling. Semua bumbu tersebut dihaluskan dengan cobek batu hingga mengeluarkan aroma wangi yang khas.",
             "ファティマ叔母さんは、薪のかまどの上に置かれた大きな鉄鍋を使って、伝統的なルンダンの作り方の手順を僕に教えてくれました。まず最初に、僕たちはシャロット、ニンニク、生姜、ガランガル（ナンキョウ）、ターメリック（ウコン）、レモングラス、こぶみかんの葉、挽き唐辛子といった豊かな香辛料を用意しました。それらすべての調味料は、特有の良い香りを放つまで石臼（チョベッ）ですり潰されました。",
             "kuali besar（大鍋）、tungku kayu bakar（薪のかまど）、cobek batu（石臼）、dihaluskan（細かくすり潰される）。"),
            ("Langkah kedua adalah merebus santan kelapa kental bersama bumbu halus dan rempah aromatik. Santan tersebut harus terus diaduk perlahan tanpa henti agar tidak pecah. Setelah santan mendidih dan mengeluarkan minyak kemerahan (tahap gulai), potongan daging sapi segar dimasukkan ke dalam kuali.",
             "第2のステップは、濃厚なココナッツミルクをすり潰した調味料や芳香ハーブと一緒に煮込むことです。そのココナッツミルクは、油分が分離しないように休むことなくゆっくりとかき混ぜ続けなければなりません。ココナッツミルクが沸騰して赤みがかった油が染み出た後（グライの段階）、新鮮な牛肉の切り身が鍋の中に投入されました。",
             "santan kental（濃いココナッツミルク）、diaduk tanpa henti（休まず混ぜられる）、santan pecah（ココナッツミルクの油分が分離してダマになる失敗）。"),
            ("Proses memasak rendang membutuhkan kesabaran yang luar biasa. Selama lebih dari empat jam, api dijaga tetap stabil sambil daging terus diaduk hingga cairan santan mengering dan berubah warna menjadi cokelat tua kehitaman (tahap kalio, lalu menjadi rendang kering). Dagingnya terasa sangat empuk dan bumbu rempahnya meresap sempurna hingga ke serat terdalam. Memasak rendang mengajariku arti ketabahan dan kerja keras.",
             "ルンダンを調理する工程には並外れた忍耐力が必要です。4時間以上もの間、ココナッツミルクの水分が蒸発して焦げ茶色（カリオの段階、そして乾燥したルンダンへ）に色が変わるまで、肉をかき混ぜ続けながら火力を安定して保ちます。肉は驚くほど柔らかく、スパイスの旨味が繊維の最も深い部分まで完璧に染み込んでいます。ルンダン作りは僕に不屈の忍耐と勤勉の意味を教えてくれました。",
             "tahap gulai → kalio → rendang（ルンダンの3大進化プロセス）、empuk（柔らかい）、meresap sempurna（完全に味が染み込む）。")
        ],
        "vocab": [
            ("hidangan istimewa", "名詞句", "hidang", "特別なごちそう、特別料理", "Ibu menyiapkan hidangan istimewa untuk tamu."),
            ("tungku kayu bakar", "名詞句", "tungku", "薪のかまど", "Memasak di tungku kayu bakar menghasilkan aroma sedap."),
            ("lengkuas", "名詞", "-", "ガランガル（生姜に似た東南アジアの芳香根菜）", "Lengkuas dimemarkan sebelum dimasukkan ke sup."),
            ("kunyit", "名詞", "-", "ターメリック、ウコン", "Kunyit memberi warna kuning alami."),
            ("serai", "名詞", "-", "レモングラス", "Batang serai memberi aroma segar pada gulai."),
            ("cobek batu", "名詞句", "cobek", "石臼とすり棒（スパイス磨砕器具）", "Bumbu diulek halus menggunakan cobek batu."),
            ("santan kelapa", "名詞句", "santan", "ココナッツミルク", "Santan kelapa membuat masakan menjadi gurih dan kental."),
            ("diaduk", "動詞", "aduk", "かき混ぜられる", "Sup harus diaduk perlahan agar bumbu merata."),
            ("kalio", "名詞", "-", "カリオ（ルンダンの一歩手前の中間段階・茶色い濃厚シチュー）", "Kalio masih berkuah kental cokelat."),
            ("meresap", "動詞", "resap", "（味が）染み込む、浸透する", "Bumbu rempah meresap sempurna ke dalam daging.")
        ],
        "grammar_points": """1. **調理手順を表す順序標識（Sequential Connectors）**:
   - *Pertama-tama*（まず最初に）
   - *Langkah kedua adalah ...*（第2のステップは〜）
   - *Setelah santan mendidih ...*（ココナッツミルクが沸騰した後〜）
   - *Selama lebih dari empat jam ...*（4時間以上の間〜）
2. **目的と予防を表す接続詞 `agar tidak ...`（〜しないように）**:
   - *diaduk terus agar tidak pecah*（分離しないように混ぜ続ける）
   - *ditutup rapat agar tidak dihinggapi lalat*（ハエが止まらないようにしっかり蓋をする）
3. **結果・変化を表す前置詞句 `berubah menjadi ...`（〜に変わる）**:
   - *berubah menjadi cokelat kehitaman*（黒褐色に変化する）
   - *berubah menjadi lebih baik*（より良くなる）""",
        "quizzes": [
            ("世界的に有名な郷土料理「ルンダン（Rendang）」の発祥の地・民族はどこですか？",
             ["バリ島（Bali）", "西スマトラ州ミナンカバウ民族（Minangkabau, Sumatra Barat）", "西ジャワ州スンダ民族（Sunda）"],
             "西スマトラ州ミナンカバウ民族（Minangkabau, Sumatra Barat）",
             "第1段落に「...masakan tradisional khas Minangkabau yang terkenal di seluruh dunia.」とあります。"),
            ("ルンダンを調理する際、ココナッツミルクの水分が煮詰まる3つの段階の正しい順番は？",
             ["rendang → kalio → gulai", "gulai（黄赤色スープ） → kalio（茶色シチュー） → rendang（黒褐色ドライ）", "kalio → gulai → rendang"],
             "gulai（黄赤色スープ） → kalio（茶色シチュー） → rendang（黒褐色ドライ）",
             "第3・第4段落で解説されている通り、最初はシャバシャバの gulai、煮詰まって茶色の kalio、最終的に水分が飛んで黒褐色の乾いた rendang になります。"),
            ("本物の伝統的ルンダンを作るために必要な調理時間はどのくらいですか？",
             ["約15分間", "約1時間", "4時間以上（lebih dari empat jam）"],
             "4時間以上（lebih dari empat jam）",
             "第4段落に「Selama lebih dari empat jam, api dijaga tetap stabil sambil daging terus diaduk...」と明記されています。")
        ],
        "culture": """### ルンダン（Rendang）の哲学とミナンカバウ社会
アメリカのCNNによる「世界で最も美味しい料理（World's 50 Most Delicious Foods）」で堂々1位に輝いたルンダンは、単なる肉料理ではありません。西スマトラのミナンカバウ社会において、ルンダンを構成する4大要素は社会の柱を象徴しています：
1. **Dagiang（牛肉）**: 社会の指導者（Niniak Mamak）
2. **Karambia（ココナッツ）**: 思想家・学者（Cadiak Pandai）
3. **Lado（唐辛子）**: 戒律を守る宗教指導者（Alim Ulama）
4. **Pemasak（香辛料調味料）**: 一般社会全体（Masyarakat Minangkabau）
何時間も火の前に立ち、じっくりとかき混ぜ続ける作業は、人生における「Patience（忍耐）」「Wisdom（知恵）」「Perseverance（不屈の努力）」を養う神聖な修行とされています。"""
    }
]

# Write stories 1214 to 1220 to complete all 10 articles in Level 2
more_level2_stories = [
    {
        "id": "1214",
        "slug": "level-2-04-football-match",
        "title": "【Level 2 (A2)】Pertandingan Sepak Bola Antar-Desa（白熱する村対抗サッカー決勝戦）",
        "desc": "村対抗サッカー大会の決勝戦。白熱の攻防、同点で迎えたPK戦、団結とスポーツマンシップを描く初級A2ストーリー。",
        "text": """Bulan Agustus selalu menjadi bulan yang paling meriah di desaku. Dalam rangka merayakan Hari Kemerdekaan Republik Indonesia, desa kami mengadakan turnamen sepak bola antar-kampung yang sangat bergengsi. Tim desaku, Garuda Muda, berhasil lolos ke babak final melawan tim tangguh dari desa tetangga, Rajawali FC.

Pertandingan final berlangsung di lapangan sepak bola desa yang dipadati oleh ratusan penonton. Sorak-sorai warga yang meniup terompet dan memukul drum menciptakan atmosfer yang sangat bergemuruh. Aku duduk di bangku penonton bersama ayah dan teman-temanku, membawa bendera merah putih kecil untuk memberi semangat kepada tim desa kami.

Babak pertama berjalan sangat ketat. Kedua tim saling melancarkan serangan berbahaya, namun pertahanan masing-masing tim sangat kokoh. Pada babak kedua, kapten tim Garuda Muda berhasil mencetak gol spektakuler melalui tendangan bebas melengkung. Namun, lima menit sebelum pertandingan berakhir, tim lawan berhasil menyamakan kedudukan menjadi satu sama melalui sundulan kepala.

Karena skor imbang bertahan hingga peluit panjang dibunyikan, pertandingan harus diselesaikan melalui drama adu penalti. Ketegangan memuncak di seluruh penjuru lapangan. Penjaga gawang Garuda Muda melakukan penyelamatan gemilang dengan menepis tendangan penalti penentu lawan. Lapangan seketika meledak dengan sorak kegembiraan. Kami semua berlari ke tengah lapangan untuk merayakan kemenangan bersama. Pertandingan ini mempererat rasa persaudaraan dan persatuan di antara warga.""",
        "paragraphs": [
            ("Bulan Agustus selalu menjadi bulan yang paling meriah di desaku. Dalam rangka merayakan Hari Kemerdekaan Republik Indonesia, desa kami mengadakan turnamen sepak bola antar-kampung yang sangat bergengsi. Tim desaku, Garuda Muda, berhasil lolos ke babak final melawan tim tangguh dari desa tetangga, Rajawali FC.",
             "8月は僕の村でいつも最も賑やかな月です。インドネシア共和国の独立記念日を祝う一環として、僕たちの村は非常に名誉ある村対抗サッカー大会を開催しました。僕の村のチーム「ガルーダ・ムーダ」は見事、隣村の強豪チーム「ラジャワリFC」と戦う決勝戦に進出しました。",
             "dalam rangka（〜の一環として）、turnamen antar-kampung（村対抗トーナメント）、lolos ke babak final（決勝に進出する）。"),
            ("Pertandingan final berlangsung di lapangan sepak bola desa yang dipadati oleh ratusan penonton. Sorak-sorai warga yang meniup terompet dan memukul drum menciptakan atmosfer yang sangat bergemuruh. Aku duduk di bangku penonton bersama ayah dan teman-temanku, membawa bendera merah putih kecil untuk memberi semangat kepada tim desa kami.",
             "決勝戦は何百人もの観客で埋め尽くされた村のサッカーグラウンドで行われました。ラッパを吹き太鼓を叩く住民たちの歓声が、非常に轟く熱気ある雰囲気を作り出していました。僕は父や友達と一緒に観客席に座り、村のチームを応援するために小さな赤白国旗を持っていました。",
             "dipadati ratusan penonton（数百人の観客で満員）、sorak-sorai（歓声）、memberi semangat（声援を送る・励ます）。"),
            ("Babak pertama berjalan sangat ketat. Kedua tim saling melancarkan serangan berbahaya, namun pertahanan masing-masing tim sangat kokoh. Pada babak kedua, kapten tim Garuda Muda berhasil mencetak gol spektakuler melalui tendangan bebas melengkung. Namun, lima menit sebelum pertandingan berakhir, tim lawan berhasil menyamakan kedudukan menjadi satu sama melalui sundulan kepala.",
             "前半戦は非常に緊迫した展開となりました。両チームは互いに危険な攻撃を繰り出しましたが、それぞれの守備は非常に堅固でした。後半戦、ガルーダ・ムーダのキャプテンが曲がるフリーキックで見事なスーパーゴールを決めました。しかし、試合終了の5分前、相手チームがヘディングシュートによって1対1の同点に追いつきました。",
             "babak pertama / kedua（前半 / 後半）、mencetak gol（ゴールを決める）、tendangan bebas（フリーキック）、sundulan kepala（ヘディング）。"),
            ("Karena skor imbang bertahan hingga peluit panjang dibunyikan, pertandingan harus diselesaikan melalui drama adu penalti. Ketegangan memuncak di seluruh penjuru lapangan. Penjaga gawang Garuda Muda melakukan penyelamatan gemilang dengan menepis tendangan penalti penentu lawan. Lapangan seketika meledak dengan sorak kegembiraan. Kami semua berlari ke tengah lapangan untuk merayakan kemenangan bersama. Pertandingan ini mempererat rasa persaudaraan dan persatuan di antara warga.",
             "同点スコアが長い笛（試合終了のホイッスル）が鳴るまで維持されたため、試合はドラマチックなPK戦によって決着をつけなければなりませんでした。グラウンドの至る所で緊張が頂点に達しました。ガルーダ・ムーダのゴールキーパーは、相手の決定的なPKシュートを弾き出す素晴らしいファインセーブを見せました。グラウンドは一瞬にして歓喜の雄叫びで爆発しました。僕たちは皆、勝利を一緒に祝うためにピッチの中央へと駆け出しました。この試合は住民たちの間の兄弟愛と団結の絆をより強固なものにしました。",
             "skor imbang（引き分けスコア）、adu penalti（PK戦）、penjaga gawang（ゴールキーパー）、penyelamatan gemilang（素晴らしいセーブ）。")
        ],
        "vocab": [
            ("turnamen", "名詞", "-", "トーナメント大会", "Turnamen sepak bola diadakan setiap tahun."),
            ("babak final", "名詞句", "babak", "決勝ラウンド、決勝戦", "Dua tim terbaik bertanding di babak final."),
            ("penonton", "名詞", "tonton", "観客、見物人", "Stadion dipenuhi oleh ribuan penonton setia."),
            ("sorak-sorai", "名詞", "-", "歓声、喝采の叫び", "Sorak-sorai penonton mengguncang stadion."),
            ("pertahanan kokoh", "名詞句", "tahan", "強固な守備、頑丈なディフェンス", "Pertahanan kokoh sulit ditembus lawan."),
            ("tendangan bebas", "名詞句", "tendang", "フリーキック", "Pemain mencetak gol lewat tendangan bebas."),
            ("sundulan kepala", "名詞句", "sundul", "ヘディングシュート", "Gol tercipta melalui sundulan kepala tajam."),
            ("adu penalti", "名詞句", "-", "PK合戦（ペナルティキック戦）", "Pertandingan berakhir dengan adu penalti."),
            ("penjaga gawang", "名詞句", "jaga", "ゴールキーパー", "Penjaga gawang berhasil menepis bola."),
            ("persaudaraan", "名詞", "saudara", "兄弟愛、同胞の絆", "Olahraga mempererat rasa persaudaraan bangsa.")
        ],
        "grammar_points": """1. **相互動作を表す `saling + 動詞`（お互いに〜する）**:
   - *saling melancarkan serangan*（お互いに攻撃を繰り出す）
   - *saling membantu*（お互いに助け合う）
   - *saling menghormati*（お互いに尊重し合う）
2. **時間を表す名詞 ＋ 前置詞句 `sebelum ... berakhir`**:
   - *lima menit sebelum pertandingan berakhir*（試合が終わる5分前に）
   - *tiga hari sebelum hari raya*（祝日の3日前に）
3. **周囲辞 `antar-...`（〜間の・対抗の）**:
   - *antar-kampung*（村対抗の）
   - *antar-desa*（集落間の）
   - *antar-negara*（国家間の・国際的な）""",
        "quizzes": [
            ("この村対抗サッカー大会は何の記念行事の一環として8月に開催されましたか？",
             ["新年の祝賀", "インドネシア共和国の独立記念日（Hari Kemerdekaan RI）", "収穫祭"],
             "インドネシア共和国の独立記念日（Hari Kemerdekaan RI）",
             "第1段落に「Dalam rangka merayakan Hari Kemerdekaan Republik Indonesia...」とあります。"),
            ("後半戦の試合終了5分前、相手チームはどのようなプレーで1対1の同点に追いつきましたか？",
             ["オウンゴール", "ヘディングシュート（sundulan kepala）", "長距離ロングシュート"],
             "ヘディングシュート（sundulan kepala）",
             "第3段落に「...berhasil menyamakan kedudukan menjadi satu sama melalui sundulan kepala.」とあります。"),
            ("引き分けの末に行われたPK戦（adu penalti）で勝利の立役者となったのは誰ですか？",
             ["相手のシュートをファインセーブしたゴールキーパー（penjaga gawang）", "監督", "主審（審判）"],
             "相手のシュートをファインセーブしたゴールキーパー（penjaga gawang）",
             "第4段落に「Penjaga gawang Garuda Muda melakukan penyelamatan gemilang dengan menepis tendangan penalti penentu lawan.」とあります。")
        ],
        "culture": """### インドネシアの8月17日「Tujuhbelasan」とサッカー熱
8月17日のインドネシア独立記念日（Hari Kemerdekaan）前後は、全国津々浦々で「Tujuhbelasan（17日祭）」と呼ばれる祝祭イベントが繰り広げられます。
麻袋競走（Balap Karung）や油を塗ったビンロウ樹によじ登る競技（Panjat Pinang）と並んで最も熱狂するのが「村対抗サッカー（Sepak Bola Antar-Kampung: Tarkam）」です。インドネシア人のサッカー熱は世界でも屈指であり、普段は大人しい村人たちが声をからして応援し、地域の結束を確かめ合います。"""
    },
    {
        "id": "1215",
        "slug": "level-2-05-visiting-zoo",
        "title": "【Level 2 (A2)】Melihat Komodo di Ragunan（ラグナン動物園のコモドオオトカゲ）",
        "desc": "南ジャカルタのラグナン動物園を訪問。世界最大のトカゲ「コモドドラゴン」やオランウータンを通じ、動物と環境保護の初級A2語彙を学ぶ。",
        "text": """Pada hari Sabtu pagi, sekolah kami mengadakan kegiatan karyawisata ke Kebun Binatang Ragunan di Jakarta Selatan. Kebun binatang ini sangat luas dan menjadi habitat bagi ribuan satwa liar dari seluruh pelosok nusantara dan mancanegara. Kami pergi bersama rombongan guru dan teman-teman sekelas naik bus sekolah.

Tujuan utama yang paling membuat kami penasaran adalah melihat Komodo secara langsung. Komodo adalah kadal purba raksasa asli Indonesia yang hidup di Pulau Komodo, Nusa Tenggara Timur. Saat kami tiba di kandang khusus komodo, hewan tersebut sedang berjemur dengan tenang di bawah terik sinar matahari. Tubuhnya sangat besar, panjangnya mencapai hampir tiga meter, dengan kulit bersisik kasar berwarna abu-abu gelap.

Pemandu kebun binatang menjelaskan bahwa komodo adalah hewan karnivora pemangsa puncak. Lidahnya yang panjang berwarna kuning bercabang dua selalu menjulur keluar untuk mencium bau mangsa dari jarak beberapa kilometer. Kami mendengarkan penjelasan tersebut dengan penuh kagum dan rasa hormat pada keajaiban alam Indonesia.

Setelah melihat komodo, kami mengunjungi area primata untuk melihat orangutan Kalimantan yang berbulu lebat kemerahan. Orangutan tersebut berayun lincah dari satu pohon ke pohon lainnya menggunakan kedua tangannya yang kuat. Kunjungan edukatif ini membuka mata kami tentang betapa pentingnya menjaga kelestarian satwa langka agar tidak punah dari muka bumi.""",
        "paragraphs": [
            ("Pada hari Sabtu pagi, sekolah kami mengadakan kegiatan karyawisata ke Kebun Binatang Ragunan di Jakarta Selatan. Kebun binatang ini sangat luas dan menjadi habitat bagi ribuan satwa liar dari seluruh pelosok nusantara dan mancanegara. Kami pergi bersama rombongan guru dan teman-teman sekelas naik bus sekolah.",
             "土曜日の朝、僕たちの学校は南ジャカルタにあるラグナン動物園への遠足（校外学習）を実施しました。この動物園は非常に広大で、群島の隅々や世界中から集まった何千頭もの野生動物の生息地となっています。僕たちは先生方やクラスメイトの一行と一緒にスクールバスに乗って行きました。",
             "kegiatan karyawisata（校外学習・修学旅行）、satwa liar（野生動物）、pelosok nusantara（群島の津々浦々）。"),
            ("Tujuan utama yang paling membuat kami penasaran adalah melihat Komodo secara langsung. Komodo adalah kadal purba raksasa asli Indonesia yang hidup di Pulau Komodo, Nusa Tenggara Timur. Saat kami tiba di kandang khusus komodo, hewan tersebut sedang berjemur dengan tenang di bawah terik sinar matahari. Tubuhnya sangat besar, panjangnya mencapai hampir tiga meter, dengan kulit bersisik kasar berwarna abu-abu gelap.",
             "僕たちの好奇心を最もかき立てていた主要な目的地は、コモドオオトカゲを直接見ることでした。コモドは東ヌサトゥンガラ州のコモド島に生息する、インドネシア固有の巨大な古代トカゲです。コモド専用の飼育場に到着した時、その動物は照りつける日差しの下で穏やかに日光浴をしていました。体は非常に巨大で、体長は3メートル近くに達し、暗灰色の粗い鱗の皮膚を持っています。",
             "penasaran（好奇心・気になる）、kadal purba raksasa（巨大な古代トカゲ）、berjemur（日光浴する）。"),
            ("Pemandu kebun binatang menjelaskan bahwa komodo adalah hewan karnivora pemangsa puncak. Lidahnya yang panjang berwarna kuning bercabang dua selalu menjulur keluar untuk mencium bau mangsa dari jarak beberapa kilometer. Kami mendengarkan penjelasan tersebut dengan penuh kagum dan rasa hormat pada keajaiban alam Indonesia.",
             "動物園のガイドは、コモドが頂点捕食者である肉食動物であると説明してくれました。二股に分かれた黄色い長い舌は、数キロ離れた場所から獲物の匂いを嗅ぎ分けるために常に外へ突き出されています。僕たちは畏敬の念とインドネシアの自然の神秘への敬意を胸に、その説明に聞き入りました。",
             "hewan karnivora（肉食動物）、pemangsa puncak（頂点捕食者）、lidah bercabang dua（二股の舌）、menjulur keluar（突き出る・伸びる）。"),
            ("Setelah melihat komodo, kami mengunjungi area primata untuk melihat orangutan Kalimantan yang berbulu lebat kemerahan. Orangutan tersebut berayun lincah dari satu pohon ke pohon lainnya menggunakan kedua tangannya yang kuat. Kunjungan edukatif ini membuka mata kami tentang betapa pentingnya menjaga kelestarian satwa langka agar tidak punah dari muka bumi.",
             "コモドを見た後、僕たちは赤みがかった豊かな毛を持つカリマンタン・オランウータンを見るために霊長類エリアを訪れました。そのオランウータンは力強い両手を使って、ある木から別の木へと身軽にぶら下がりながら移動していました。この教育的な訪問は、希少動物が地球上から絶滅しないように保護することの重要性について、僕たちの目を開かせてくれました。",
             "berayun lincah（身軽にぶら下がる・揺れる）、kelestarian satwa langka（希少動物の保護・持続性）、punah（絶滅する）。")
        ],
        "vocab": [
            ("karyawisata", "名詞", "wisata", "校外学習、遠足、修学旅行", "Murid-murid gembira mengikuti karyawisata."),
            ("kebun binatang", "名詞句", "kebun", "動物園", "Kebun binatang Ragunan sangat luas dan rindang."),
            ("satwa liar", "名詞句", "satwa", "野生動物、野生生物", "Hutan lindung melindungi habitat satwa liar."),
            ("kadal purba", "名詞句", "kadal", "古代トカゲ", "Komodo adalah spesies kadal purba purba."),
            ("berjemur", "動詞", "jemur", "日光浴をする、日に当たる", "Reptil suka berjemur untuk menghangatkan tubuh."),
            ("kulit bersisik", "名詞句", "sisik", "鱗（うろこ）に覆われた皮膚", "Ular dan kadal memiliki kulit bersisik."),
            ("pemangsa puncak", "名詞句", "mangsa", "頂点捕食者、生態系の頂点", "Harimau dan komodo adalah pemangsa puncak."),
            ("menjulur", "動詞", "julur", "（舌などが）外へ長く突き出る", "Lidah komodo menjulur mencium mangsa."),
            ("satwa langka", "名詞句", "langka", "希少野生動物、絶滅危惧種", "Orangutan dan badak adalah satwa langka."),
            ("punah", "形容詞/動詞", "-", "絶滅した、死に絶えた", "Banyak satwa terancam punah akibat deforestasi.")
        ],
        "grammar_points": """1. **形容詞の前に置く感嘆詞 `betapa ...`（なんと〜だろう）**:
   - *betapa pentingnya menjaga alam*（自然を守ることがなんと重要なことか）
   - *betapa indahnya pemandangan ini*（なんと美しい景色だろう）
2. **目的を表す接続詞 `agar tidak ...`（〜しないように）**:
   - *agar tidak punah dari muka bumi*（地球上から絶滅しないように）
   - *agar tidak terlambat*（遅刻しないように）
3. **身体部位を表す形容詞修飾**:
   - *berbulu lebat*（毛が濃い）
   - *bercabang dua*（二股に分かれた）
   - *bersisik kasar*（粗い鱗のある）""",
        "quizzes": [
            ("世界最大のトカゲであるコモドドラゴン（Komodo）の本来の生息地はどこですか？",
             ["ジャワ島（Pulau Jawa）", "東ヌサトゥンガラ州のコモド島（Pulau Komodo, NTT）", "カリマンタン島（Pulau Kalimantan）"],
             "東ヌサトゥンガラ州のコモド島（Pulau Komodo, NTT）",
             "第2段落に「...kadal purba raksasa asli Indonesia yang hidup di Pulau Komodo, Nusa Tenggara Timur.」とあります。"),
            ("コモドが数キロ離れた場所から獲物の匂いを嗅ぎ分けるために使っている身体部位は何ですか？",
             ["大きな耳", "黄色く二股に分かれた長い舌（lidah bercabang dua）", "長い尻尾"],
             "黄色く二股に分かれた長い舌（lidah bercabang dua）",
             "第3段落に「Lidahnya yang panjang berwarna kuning bercabang dua selalu menjulur keluar untuk mencium bau mangsa...」とあります。"),
            ("ラグナン動物園への校外学習を通じて、生徒たちが学んだ最も大切な環境的気づきは何ですか？",
             ["動物に餌をあげる方法", "希少動物（satwa langka）が絶滅しないよう自然環境を保護することの大切さ", "動物園の入場料の安さ"],
             "希少動物（satwa langka）が絶滅しないよう自然環境を保護することの大切さ",
             "第4段落末尾に「...tentang betapa pentingnya menjaga kelestarian satwa langka agar tidak punah dari muka bumi.」とあります。")
        ],
        "culture": """### インドネシアの国宝動物「コモドドラゴン」と自然遺産
コモドオオトカゲ（Varanus komodoensis: 通称 Komodo）は、体長最大3メートル、体重70キロ以上にも達する現生最大のトカゲであり、恐竜の生きた化石とも呼ばれます。生息地であるコモド国立公園（東ヌサトゥンガラ州）はユネスコ世界自然遺産に登録されています。
ジャカルタ市民に愛される「ラグナン動物園（Taman Margasatwa Ragunan）」は、1864年に設立された東南アジア最古級の巨大動物園で、140ヘクタールもの熱帯雨林のような広大な敷地でインドネシア固有の貴重な野生生物を低価格で観察できます。"""
    },
    {
        "id": "1216",
        "slug": "level-2-06-rainy-season-flood",
        "title": "【Level 2 (A2)】Hujan Deras dan Gotong Royong（大雨の冠水と近所の助け合い清掃）",
        "desc": "雨季の大雨で道路が冠水した際、地域住民が一致団結して排水溝を掃除し土嚢を積む。インドネシアの相互扶助精神（Gotong Royong）を描くA2ストーリー。",
        "text": """Musim hujan telah mencapai puncaknya pada bulan Januari. Sejak dini hari, awan mendung tebal menyelimuti langit kota, dan hujan deras mengguyur pemukiman kami tanpa henti selama lebih dari lima jam. Air di selokan utama mulai meluap karena tersumbat oleh tumpukan sampah dan lumpur tebal.

Air setinggi mata kaki mulai menggenangi jalanan di depan rumah warga. Pak RT (Ketua Rukun Tetangga) segera membunyikan tiang listrik dengan potongan besi sebagai tanda bahaya dan memanggil seluruh warga untuk berkumpul. Tanpa menunda waktu, para warga laki-laki, tua maupun muda, segera keluar rumah dengan membawa cangkul, sekop, dan karung pasir.

Kami melakukan aksi gotong royong untuk membersihkan saluran air. Ayah dan tetangga-tetangga bahu-membahu mengeruk lumpur dan sampah plastik yang menyumbat gorong-gorong. Aku dan anak-anak lainnya membantu mengangkut karung pasir untuk diletakkan di depan pintu rumah warga yang posisinya rendah agar air tidak masuk ke dalam rumah.

Sementara para pria bekerja keras di tengah guyuran gerimis, para ibu di pos ronda sibuk menyeduh teh manis panas dan menggoreng pisang goreng renyah untuk para warga yang bekerja. Setelah dua jam bekerja keras bersama-sama, air di selokan akhirnya mengalir lancar dan genangan air di jalan perlahan surut. Semangat gotong royong membuat masalah yang berat terasa jauh lebih ringan.""",
        "paragraphs": [
            ("Musim hujan telah mencapai puncaknya pada bulan Januari. Sejak dini hari, awan mendung tebal menyelimuti langit kota, dan hujan deras mengguyur pemukiman kami tanpa henti selama lebih dari lima jam. Air di selokan utama mulai meluap karena tersumbat oleh tumpukan sampah dan lumpur tebal.",
             "雨季は1月にピークを迎えました。未明から分厚い暗雲が街の空を覆い、激しい雨が5時間以上も途切れることなく僕たちの住宅街に降り注ぎました。幹線排水溝の水は、ゴミの山と分厚い泥によって詰まり、溢れ始めました。",
             "musim hujan（雨季）、mengguyur（激しく浴びせかける・降り注ぐ）、meluap（氾濫する・溢れ出る）、tersumbat（詰まる）。"),
            ("Air setinggi mata kaki mulai menggenangi jalanan di depan rumah warga. Pak RT (Ketua Rukun Tetangga) segera membunyikan tiang listrik dengan potongan besi sebagai tanda bahaya dan memanggil seluruh warga untuk berkumpul. Tanpa menunda waktu, para warga laki-laki, tua maupun muda, segera keluar rumah dengan membawa cangkul, sekop, dan karung pasir.",
             "くるぶしの高さの水が、住民の家の前の道路を浸水させ始めました。町内会長（Pak RT）は即座に鉄の棒で電柱を叩いて警報を鳴らし、住民全員に集まるよう呼びかけました。時間を無駄にすることなく、老いも若きも男性住民たちはクワ、シャベル、土嚢を持ってすぐに家を出ました。",
             "setinggi mata kaki（くるぶしの高さ）、Pak RT（町内会長）、karung pasir（土嚢）。電柱を叩いて合図する伝統的警報。"),
            ("Kami melakukan aksi gotong royong untuk membersihkan saluran air. Ayah dan tetangga-tetangga bahu-membahu mengeruk lumpur dan sampah plastik yang menyumbat gorong-gorong. Aku dan anak-anak lainnya membantu mengangkut karung pasir untuk diletakkan di depan pintu rumah warga yang posisinya rendah agar air tidak masuk ke dalam rumah.",
             "僕たちは水路を掃除するためにゴトン・ロヨン（相互扶助の共同作業）のアクションを行いました。父と近所の人々は肩を寄せ合い協力して、暗渠（排水管）を詰まらせている泥やプラスチックゴミをかき出しました。僕や他の子供たちは、水が家の中に入らないように、地面の低い位置にある住民の家の玄関前に置くための土嚢を運ぶのを手伝いました。",
             "gotong royong（相互扶助・共同作業）、bahu-membahu（肩を並べて協力する）、gorong-gorong（排水暗渠）。"),
            ("Sementara para pria bekerja keras di tengah guyuran gerimis, para ibu di pos ronda sibuk menyeduh teh manis panas dan menggoreng pisang goreng renyah untuk para warga yang bekerja. Setelah dua jam bekerja keras bersama-sama, air di selokan akhirnya mengalir lancar dan genangan air di jalan perlahan surut. Semangat gotong royong membuat masalah yang berat terasa jauh lebih ringan.",
             "男性たちが小雨の降り注ぐ中で懸命に働く一方で、女性陣（お母さんたち）は警備詰所（ポス・ロンダ）で、作業する住民たちのために温かい甘いお茶を淹れたり、サクサクの揚げバナナを揚げたりするのに大忙しでした。2時間一緒に懸命に働いた後、排水溝の水はついに滑らかに流れ、道路の冠水はゆっくりと引いていきました。ゴトン・ロヨンの精神は、重い困難をずっと軽く感じさせてくれました。",
             "pos ronda（地域の警備詰所）、menyeduh teh（お茶を淹れる）、air surut（水が引く・減水する）。")
        ],
        "vocab": [
            ("musim hujan", "名詞句", "hujan", "雨季", "Musim hujan di Indonesia berlangsung Oktober hingga April."),
            ("tersumbat", "動詞", "sumbat", "（偶発的に）詰まる、塞がる", "Saluran air tersumbat oleh sampah plastik."),
            ("menggenangi", "動詞", "genang", "〜を浸水させる、冠水させる", "Air banjir menggenangi permukiman warga."),
            ("Rukun Tetangga (RT)", "名詞句", "-", "町内会、隣組（最小地域自治組織）", "Pak RT memimpin rapat warga malam ini."),
            ("cangkul", "名詞", "-", "クワ（土を掘る農具）", "Petani mencangkul tanah di kebun."),
            ("gotong royong", "名詞/動詞", "-", "相互扶助、共同奉仕作業", "Warga desa menjunjung tinggi tradisi gotong royong."),
            ("bahu-membahu", "副詞句", "bahu", "肩を並べて、一致協力して", "Masyarakat bahu-membahu membangun jembatan rusak."),
            ("gorong-gorong", "名詞", "-", "排水暗渠、地下水路、土管", "Sampah menyumbat gorong-gorong jalan utama."),
            ("pos ronda", "名詞句", "ronda", "夜警詰所、地域の集会小屋", "Bapak-bapak berkumpul di pos ronda untuk ronda malam."),
            ("surut", "動詞/形容詞", "-", "（水が）引く、減水する", "Banjir mulai surut menjelang sore hari.")
        ],
        "grammar_points": """1. **高さを表す接頭辞 `se-` ＋ 名詞**:
   - *setinggi mata kaki*（くるぶしの高さ）
   - *setinggi lutut*（膝の高さ）
   - *setinggi dada*（胸の高さ）
2. **対照的な同時進行を表す接続詞 `sementara`（〜する一方で）**:
   - *Sementara para pria bekerja, para ibu sibuk menyeduh teh.*（男性陣が働く一方で、女性陣はお茶を淹れるのに忙しかった）
3. **偶発受動態 `ter-`（意図せず〜してしまう・〜された状態）**:
   - *tersumbat*（意図せず詰まってしまった）
   - *terperosok*（うっかり足を取られて落ちた）
   - *terbuka*（開いたままになっている）""",
        "quizzes": [
            ("排水路が詰まり大雨で水が溢れた際、町内会長（Pak RT）が住民を呼ぶために取った伝統的な行動は何ですか？",
             ["メガホンで大声を上げた", "鉄の棒で電柱を叩いてカンカンと音を鳴らした", "警察に通報した"],
             "鉄の棒で電柱を叩いてカンカンと音を鳴らした",
             "第2段落に「Pak RT... segera membunyikan tiang listrik dengan potongan besi sebagai tanda bahaya...」とあります。"),
            ("男性陣が排水溝の掃除や土嚢積みに奮闘している間、地域の女性陣（お母さんたち）は何をして支えていましたか？",
             ["家でテレビを見ていた", "地域の詰所で温かい甘いお茶を淹れ、揚げバナナを作っていた", "スーパーへ買い物に行っていた"],
             "地域の詰所で温かい甘いお茶を淹れ、揚げバナナを作っていた",
             "第4段落に「...para ibu di pos ronda sibuk menyeduh teh manis panas dan menggoreng pisang goreng renyah...」とあります。"),
            ("このストーリーで描かれている、困難に直面した地域社会が一致団結して助け合う伝統精神は何と呼ばれますか？",
             ["Bhinneka Tunggal Ika", "Gotong Royong（ゴトン・ロヨン）", "Pancasila"],
             "Gotong Royong（ゴトン・ロヨン）",
             "第3段落・第4段落で強調されている、インドネシア社会の根幹を成す相互扶助精神「Gotong Royong」です。")
        ],
        "culture": """### インドネシアの地域組織「RT/RW」と「Gotong Royong（相互扶助）」
インドネシアの地域コミュニティには、「RT（Rukun Tetangga: 約20〜50世帯の隣組）」と、それを束ねる「RW（Rukun Warga: 町内会）」という強固な住民自治組織が存在します。
電柱を叩いて合図を送る「Tanda Bahaya」や、冠水・冠雪（熱帯では冠水や倒木）時に住民総出で掃除を行う「Kerja Bakti / Gotong Royong」は、法律ではなく地域の人々の助け合いのモラルとして今なお脈々と息づいています。"""
    },
    {
        "id": "1217",
        "slug": "level-2-07-buying-smartphone",
        "title": "【Level 2 (A2)】Membeli Ponsel Pertama dengan Uang Sendiri（アルバイト代で買ったスマホ）",
        "desc": "自力でお金を貯めて初めてスマートフォンを購入する達成感。電化製品の売買、スペック比較、デジタル用語のA2語彙を学ぶ。",
        "text": """Sudah hampir satu tahun Dimas, kakak laki-lakiku, menyisihkan sebagian uang sakunya dan bekerja paruh waktu membantu paman di warung fotokopi. Cita-citanya adalah membeli sebuah ponsel pintar (smartphone) baru dengan uang hasil keringatnya sendiri untuk mendukung kegiatan belajarnya di SMA.

Pada hari Sabtu siang, setelah tabungannya di celengan ayam genap mencapai tiga juta rupiah, Kak Dimas mengajakku pergi ke pusat perbelanjaan elektronik ITC Roxy Mas. Pusat perbelanjaan itu sangat ramai, dipenuhi oleh puluhan toko gawai yang memajang berbagai merek ponsel pintar terbaru dengan lampu warna-warni yang berkilauan.

Kami mendatangi salah satu gerai resmi terpercaya. Seorang staf penjualan yang ramah menyapa kami dan menjelaskan spesifikasi beberapa model ponsel. Kak Dimas sangat teliti; dia membandingkan kapasitas baterai, kejernihan kamera, serta kecepatan prosesor dan kapasitas penyimpanan internal. Kak Dimas akhirnya memilih ponsel pintar berwarna abu-abu metalik dengan kapasitas memori 128 gigabita dan baterai berdaya tahan lima ribu miliampere.

Setelah membayar di kasir dan menerima struk pembayaran resmi, petugas toko membantu memasang kartu SIM serta pelindung layar antigores. Senyum bangga terpancar jelas di wajah Kak Dimas saat memegang ponsel pertamanya. Sebelum pulang, panggilan video pertama yang dilakukan Kak Dimas adalah menelepon ayah dan ibu di rumah untuk memamerkan hasil kerja kerasnya. Peristiwa ini memberiku pelajaran berharga tentang kemandirian dan pentingnya menabung.""",
        "paragraphs": [
            ("Sudah hampir satu tahun Dimas, kakak laki-lakiku, menyisihkan sebagian uang sakunya dan bekerja paruh waktu membantu paman di warung fotokopi. Cita-citanya adalah membeli sebuah ponsel pintar (smartphone) baru dengan uang hasil keringatnya sendiri untuk mendukung kegiatan belajarnya di SMA.",
             "僕の兄のディマスは、高校での勉強活動を支えるために、自分自身の汗の結晶のお金で新しいスマートフォンを買うことを目指して、お小遣いの一部を取り分け、コピー屋の叔父さんを手伝うアルバイトをほぼ1年間続けてきました。",
             "menyisihkan uang（お金を取り分ける・貯金する）、bekerja paruh waktu（アルバイトをする）、hasil keringat sendiri（自分の汗の結晶）。"),
            ("Pada hari Sabtu siang, setelah tabungannya di celengan ayam genap mencapai tiga juta rupiah, Kak Dimas mengajakku pergi ke pusat perbelanjaan elektronik ITC Roxy Mas. Pusat perbelanjaan itu sangat ramai, dipenuhi oleh puluhan toko gawai yang memajang berbagai merek ponsel pintar terbaru dengan lampu warna-warni yang berkilauan.",
             "土曜日の昼、ニワトリの貯金箱の貯金がきっかり300万ルピアに達した時、ディマス兄さんは僕を連れて電化製品ショッピングモールのITCロキシー・マスへ行きました。そのモールは非常に賑やかで、色とりどりの輝くライトとともに最新の様々なブランドのスマホを展示する何十ものガジェット店で溢れていました。",
             "celengan ayam（ニワトリの貯金箱・インドネシアの定番貯金箱）、toko gawai（ガジェット機器店）、memajang（陳列する・展示する）。"),
            ("Kami mendatangi salah satu gerai resmi terpercaya. Seorang staf penjualan yang ramah menyapa kami dan menjelaskan spesifikasi beberapa model ponsel. Kak Dimas sangat teliti; dia membandingkan kapasitas baterai, kejernihan kamera, serta kecepatan prosesor dan kapasitas penyimpanan internal. Kak Dimas akhirnya memilih ponsel pintar berwarna abu-abu metalik dengan kapasitas memori 128 gigabita dan baterai berdaya tahan lima ribu miliampere.",
             "僕たちは信頼できる正規代理店の一つを訪れました。親切な店員が僕たちに挨拶し、いくつかのスマホモデルのスペックを説明してくれました。ディマス兄さんはとても慎重でした。兄はバッテリー容量、カメラの鮮明度、プロセッサの速度、そして内蔵ストレージ容量を比較しました。ディマス兄さんは最終的に、128ギガバイトのメモリ容量と5000ミリアンペアの持続バッテリーを備えた、メタリックグレー色のスマホを選びました。",
             "gerai resmi（公式店舗・正規店）、teliti（入念な・慎重な）、kapasitas penyimpanan（ストレージ容量）。"),
            ("Setelah membayar di kasir dan menerima struk pembayaran resmi, petugas toko membantu memasang kartu SIM serta pelindung layar antigores. Senyum bangga terpancar jelas di wajah Kak Dimas saat memegang ponsel pertamanya. Sebelum pulang, panggilan video pertama yang dilakukan Kak Dimas adalah menelepon ayah dan ibu di rumah untuk memamerkan hasil kerja kerasnya. Peristiwa ini memberiku pelajaran berharga tentang kemandirian dan pentingnya menabung.",
             "レジで代金を支払い、正式な領収書を受け取った後、店員はSIMカードと画面保護ガラスフィルムの装着を手伝ってくれました。初めてのスマホを手にしたディマス兄さんの顔には、誇らしげな笑顔がはっきりと輝いていました。帰宅する前、ディマス兄さんがかけた最初のビデオ通話は、自分の努力の成果を誇らしく見せるために家にいる両親へ電話することでした。この出来事は、僕に自立と貯金の大切さについての貴重な教訓を与えてくれました。",
             "struk pembayaran（レシート・領収書）、pelindung layar antigores（画面保護フィルム）、panggilan video（ビデオ通話）、kemandirian（自立心）。")
        ],
        "vocab": [
            ("menyisihkan", "動詞", "sisih", "（お金などを）取り分ける、貯金する", "Ibu menyisihkan sebagian gaji untuk tabungan."),
            ("bekerja paruh waktu", "動詞句", "kerja", "アルバイトをする、パートタイムで働く", "Mahasiswa sering bekerja paruh waktu di kafe."),
            ("uang saku", "名詞句", "uang", "お小遣い", "Ayah memberi uang saku harian kepada kami."),
            ("celengan", "名詞", "-", "貯金箱", "Celengan ayam plastik sudah terisi penuh koin."),
            ("gawai", "名詞", "-", "ガジェット、電子機器、デバイス", "Gawai memudahkan komunikasi jarak jauh."),
            ("memajang", "動詞", "pajang", "展示する、陳列する", "Toko memajang pakaian model terbaru di etalase."),
            ("spesifikasi", "名詞", "-", "仕様、スペック", "Periksa spesifikasi laptop sebelum membeli."),
            ("antigores", "名詞/形容詞", "gores", "傷防止の、画面保護フィルム", "Pasang antigores agar layar ponsel tidak lecet."),
            ("panggilan video", "名詞句", "panggil", "ビデオ通話", "Kami melakukan panggilan video dengan kakek."),
            ("kemandirian", "名詞", "mandiri", "自立、独立心", "Kemandirian adalah kunci kesuksesan hidup.")
        ],
        "grammar_points": """1. **目的・動機を表す前置詞句 `untuk mendukung ...`（〜を支援するために）**:
   - *untuk mendukung kegiatan belajar*（勉強活動を支えるために）
   - *untuk memenuhi kebutuhan sehari-hari*（日常のニーズを満たすために）
2. **完了・数値の達成を表す動詞 `mencapai ...`（〜に達する）**:
   - *mencapai tiga juta rupiah*（300万ルピアに達する）
   - *mencapai puncak gunung*（山の頂上に到達する）
3. **手段を表す前置詞句 `dengan uang hasil keringat sendiri`（自力のお金で）**:
   - 汗（keringat）は「自力で努力して稼いだ労働の対価」を象徴する美しい慣用表現です。""",
        "quizzes": [
            ("ディマス兄さんが自分のスマートフォンを買うために貯めたお金はいくらでしたか？",
             ["100万ルピア", "300万ルピア（tiga juta rupiah）", "1000万ルピア"],
             "300万ルピア（tiga juta rupiah）",
             "第2段落に「...setelah tabungannya di celengan ayam genap mencapai tiga juta rupiah...」とあります。"),
            ("ディマス兄さんがスマホを選ぶ際に慎重に比較検討したスペックに含まれないものはどれですか？",
             ["バッテリー容量とカメラの鮮明度", "プロセッサの速度と内蔵メモリ容量", "スマホケースのストラップの色"],
             "スマホケースのストラップの色",
             "第3段落で比較したのは「kapasitas baterai, kejernihan kamera, serta kecepatan prosesor dan kapasitas penyimpanan internal」です。"),
            ("買ったばかりのスマホで、ディマス兄さんが最初に行ったアクションは何ですか？",
             ["オンラインゲームで遊ぶ", "家のお父さんとお母さんに誇らしくビデオ通話をかける（menelepon panggilan video）", "SNSに写真を投稿する"],
             "家のお父さんとお母さんに誇らしくビデオ通話をかける（menelepon panggilan video）",
             "第4段落に「...panggilan video pertama yang dilakukan Kak Dimas adalah menelepon ayah dan ibu di rumah...」とあります。")
        ],
        "culture": """### インドネシアの若者とデジタル経済・「Celengan（貯金箱）」
インドネシアは世界でも有数のスマートフォン利用大国であり、東南アジア最大のデジタル経済を誇ります。配車アプリ（GoTo / Grab）や電子決済（QRIS）は日常不可欠です。
一方で、幼い頃からお小遣いを「Celengan（貯金箱）」にコツコツ貯める習慣は伝統的に根強く、豚を持たないイスラム圏であるため「ニワトリ（Celengan Ayam）」や「牛」の形をした素焼きやプラスチックの貯金箱が子供たちの自立教育のシンボルとなっています。"""
    },
    {
        "id": "1218",
        "slug": "level-2-08-batik-making-class",
        "title": "【Level 2 (A2)】Belajar Membatik di Sanggar Seni（伝統バティック染色のワークショップ）",
        "desc": "世界無形文化遺産「バティック（Batik）」の制作工程。チャンティン、熱い蝋（ろう）、藍染めを通じて、伝統工芸と文化のA2語彙を学ぶ。",
        "text": """Batik adalah salah satu warisan budaya Indonesia yang telah diakui oleh UNESCO sebagai Warisan Budaya Takbenda Dunia. Saat berlibur di Yogyakarta, ibu mendaftarkan kami mengikuti kelas lokakarya membatik tulis di sebuah sanggar seni tradisional dekat kawasan Taman Sari.

Sanggar seni itu berlokasi di sebuah rumah joglo kuno dengan halaman rindang. Udara di dalam ruangan dipenuhi aroma khas malam, yaitu lilin khusus untuk membatik yang sedang dicairkan di atas wajan kecil di atas kompor minyak. Seorang pengrajin batik senior bernama Mbok Minah menyambut kami dengan senyuman ramah dan membagikan sehelai kain mori putih polos.

Langkah pertama adalah menggambar pola dasar motif batik tradisional menggunakan pensil tipis pada kain mori. Aku memilih motif Parang Rusak yang melambangkan semangat pantang menyerah. Langkah berikutnya adalah proses yang paling mendebarkan, yaitu mencanting. Kami menggunakan alat berbentuk corong kecil dari tembaga bergagang bambu yang disebut canting untuk mengambil lilin malam panas, lalu meniupnya perlahan dan menggoreskannya mengikuti garis pola pensil. Tangan kami harus sangat tenang agar lilin tidak menetes sembarangan.

Setelah proses mencanting selesai, kain tersebut dicelupkan ke dalam bak pewarna alami berwarna biru nila. Bagian kain yang tertutup lilin malam tidak akan terkena zat pewarna, sehingga motif yang digambar akan tetap berwarna putih. Tahap terakhir adalah merebus kain di dalam air mendidih untuk meluruhkan seluruh lilin (proses nglorod). Saat kain dijemur kering di bawah sinar matahari, selembar kain batik tulis buatan tanganku sendiri berkilau indah mempesona. Pengalaman ini memberiku rasa bangga yang luar biasa atas keagungan warisan leluhur nusantara.""",
        "paragraphs": [
            ("Batik adalah salah satu warisan budaya Indonesia yang telah diakui oleh UNESCO sebagai Warisan Budaya Takbenda Dunia. Saat berlibur di Yogyakarta, ibu mendaftarkan kami mengikuti kelas lokakarya membatik tulis di sebuah sanggar seni tradisional dekat kawasan Taman Sari.",
             "バティックは、ユネスコによって世界無形文化遺産として認定されたインドネシアの文化遺産の一つです。ジョグジャカルタでの休暇中、母はタマン・サリ地区の近くにある伝統芸術工房で、手描きバティック制作のワークショップ教室に僕たちを登録してくれました。",
             "warisan budaya（文化遺産）、lokakarya（ワークショップ）、membatik tulis（手描きバティックを制作する）、sanggar seni（芸術工房）。"),
            ("Sanggar seni itu berlokasi di sebuah rumah joglo kuno dengan halaman rindang. Udara di dalam ruangan dipenuhi aroma khas malam, yaitu lilin khusus untuk membatik yang sedang dicairkan di atas wajan kecil di atas kompor minyak. Seorang pengrajin batik senior bernama Mbok Minah menyambut kami dengan senyuman ramah dan membagikan sehelai kain mori putih polos.",
             "その芸術工房は、木陰のある庭を持つ古い伝統ジョグロ家屋に位置していました。室内の空気は「マラム（malam）」特有の良い香りで満ちていました。マラムとは、石油コンロの上の小鍋で溶かされているバティック専用の特別な蝋（ろう）のことです。ンボッ・ミナという名前のベテランのバティック職人が笑顔で僕たちを出迎え、無地の白いモーリ布（木綿布）を1枚ずつ配ってくれました。",
             "rumah joglo（ジャワ伝統のジョグロ様式建築）、lilin malam（バティック用防染蝋）、pengrajin（職人・工芸家）、kain mori（バティック用の白木綿布）。"),
            ("Langkah pertama adalah menggambar pola dasar motif batik tradisional menggunakan pensil tipis pada kain mori. Aku memilih motif Parang Rusak yang melambangkan semangat pantang menyerah. Langkah berikutnya adalah proses yang paling mendebarkan, yaitu mencanting. Kami menggunakan alat berbentuk corong kecil dari tembaga bergagang bambu yang disebut canting untuk mengambil lilin malam panas, lalu meniupnya perlahan dan menggoreskannya mengikuti garis pola pensil. Tangan kami harus sangat tenang agar lilin tidak menetes sembarangan.",
             "第1のステップは、白木綿布の上に細い鉛筆を使って伝統バティックの幾何学模様の下絵を描くことです。僕は「不屈の諦めない精神」を象徴するパラン・ルサック（Parang Rusak）文様を選びました。次のステップは最もドキドキする工程である「チャンティング（蝋置き）」です。僕たちは熱い蝋をすくうために、竹の柄がついた銅製の小さな漏斗状の道具「チャンティン（canting）」を使い、息を優しく吹きかけて冷まし、鉛筆の下絵の線に沿って蝋をなぞっていきました。蝋が余計な場所に垂れないように、僕たちの手は非常に落ち着いていなければなりませんでした。",
             "motif Parang Rusak（名高い王室バティック文様）、mencanting（チャンティンで蝋を描く）、menetes sembarangan（勝手にぽたぽた垂れる）。"),
            ("Setelah proses mencanting selesai, kain tersebut dicelupkan ke dalam bak pewarna alami berwarna biru nila. Bagian kain yang tertutup lilin malam tidak akan terkena zat pewarna, sehingga motif yang digambar akan tetap berwarna putih. Tahap terakhir adalah merebus kain di dalam air mendidih untuk meluruhkan seluruh lilin (proses nglorod). Saat kain dijemur kering di bawah sinar matahari, selembar kain batik tulis buatan tanganku sendiri berkilau indah mempesona. Pengalaman ini memberiku rasa bangga yang luar biasa atas keagungan warisan leluhur nusantara.",
             "蝋置きの工程が終わった後、その布は藍色の天然染料の槽に浸されました。蝋で覆われた布の部分には染料がつかないため、描かれた文様は白く残ります。最終段階は、すべての蝋を溶かし落とすために布を沸騰したお湯の中で煮沸する工程（ンロロッ工程）です。布が太陽の光の下で干されて乾いた時、僕自身のこの手で作られた手描きバティック布が息をのむほど美しく輝きました。この体験は、群島の先祖の遺産の偉大さに対する並外れた誇りを僕に与えてくれました。",
             "dicelupkan（浸される）、pewarna alami（天然染料）、nglorod（煮沸して蝋を落とすジャワ語の専門工程用語）、warisan leluhur（先祖の遺産）。")
        ],
        "vocab": [
            ("warisan budaya", "名詞句", "waris", "文化遺産", "Batik dan keris adalah warisan budaya leluhur."),
            ("sanggar seni", "名詞句", "sanggar", "芸術工房、アトリエ", "Anak-anak belajar menari di sanggar seni."),
            ("malam", "名詞", "-", "バティック専用の防染蝋（ろう）", "Lilin malam dipanaskan hingga cair."),
            ("kain mori", "名詞句", "-", "バティック染色用の白木綿布", "Kain mori halus digunakan untuk batik tulis."),
            ("pengrajin", "名詞", "rajin", "工芸職人、伝統職人", "Pengrajin batik bekerja dengan penuh ketelitian."),
            ("canting", "名詞", "-", "チャンティン（竹の柄がついた小さな銅製蝋描き筆）", "Canting digunakan untuk menorehkan cairan lilin malam."),
            ("mencelupkan", "動詞", "celup", "浸す、浸漬する、染める", "Kain dicelupkan ke dalam cairan pewarna biru."),
            ("mendidih", "動詞", "didih", "（湯や液体が）沸騰する", "Air mendidih digunakan untuk meluruhkan lilin."),
            ("meluruhkan", "動詞", "luruh", "溶かし落とす、脱落させる", "Proses nglorod meluruhkan malam dari kain."),
            ("keagungan", "名詞", "agung", "偉大さ、威厳、崇高さ", "Keagungan candi Borobudur memikat turis dunia.")
        ],
        "grammar_points": """1. **動作の器具を表す `menggunakan ...`（〜を使って）**:
   - *menggambar pola menggunakan pensil*（鉛筆を使って文様を描く）
   - *mengambil lilin menggunakan canting*（チャンティンを使って蝋をすくう）
2. **目的・結果を表す接続詞 `sehingga ...`（その結果〜となる）**:
   - *tertutup lilin malam sehingga motif tetap putih*（蝋で覆われているため、その結果文様が白いまま残る）
3. **名詞を修飾する過去分詞的表現 `buatan ...`（〜製・〜作の）**:
   - *kain batik buatan tanganku sendiri*（僕自身の手作りのバティック布）
   - *mobil buatan Jepang*（日本製の車）""",
        "quizzes": [
            ("手描きバティック（Batik Tulis）を制作する際、熱い液体蝋（malam）をすくって布に描くための専用の銅製道具は何ですか？",
             ["ハサミ", "チャンティン（canting）", "ペンキ用ローラー"],
             "チャンティン（canting）",
             "第3段落に「Kami menggunakan alat berbentuk corong kecil dari tembaga bergagang bambu yang disebut canting...」とあります。"),
            ("布を藍染料に浸した後、布に付着している蝋をすべて溶かし落とすための伝統工程（Nglorod）では何を使用しますか？",
             ["沸騰した熱湯（air mendidih）で煮る", "氷水で凍らせる", "油で揚げる"],
             "沸騰した熱湯（air mendidih）で煮る",
             "第4段落に「...merebus kain di dalam air mendidih untuk meluruhkan seluruh lilin (proses nglorod).」と明記されています。"),
            ("インドネシアのバティックは、国際的にどの機関によって世界無形文化遺産に認定されていますか？",
             ["国際通貨基金（IMF）", "ユネスコ（UNESCO）", "世界保健機関（WHO）"],
             "ユネスコ（UNESCO）",
             "第1段落に「...telah diakui oleh UNESCO sebagai Warisan Budaya Takbenda Dunia.」とあります。")
        ],
        "culture": """### バティック（Batik）の歴史と「Hari Batik Nasional」
2009年10月2日、ユネスコ（UNESCO）はインドネシアのバティックを「世界無形文化遺産（Intangible Cultural Heritage）」に正式認定しました。これを記念して、毎年**10月2日**は「国家バティックの日（Hari Batik Nasional）」と定められています。
この日には、大統領から公務員、民間企業のビジネスマン、学校の子供たちまで全国民が一斉にお気に入りのバティックを着て出勤・登校します。幾何学模様の「Parang（刀剣・波）」や「Kawung（ヤシの実）」など、各文様には王室の哲学や繁栄の祈りが込められています。"""
    },
    {
        "id": "1219",
        "slug": "level-2-09-library-mystery",
        "title": "【Level 2 (A2)】Buku Misterius di Perpustakaan Lama（古い図書館で見つけた手帳の秘密）",
        "desc": "旧市街の古い図書館で発見された1冊の革表紙の手帳。100年前の古地図と白黒写真から街の歴史を解き明かすA2ミステリー探究ストーリー。",
        "text": """Di sudut kawasan Kota Tua yang tenang, berdiri sebuah gedung tua peninggalan zaman kolonial Belanda yang sekarang difungsikan sebagai perpustakaan arsip sejarah kota. Suatu sore saat hujan rintik-rintik, aku mengunjungi perpustakaan itu untuk mencari bahan tugas sejarah sekolah.

Ruangan perpustakaan itu dipenuhi oleh rak-rak kayu jati raksasa yang menampung ribuan buku kuno berdebu. Saat aku menelusuri lorong paling belakang di bagian sejarah lokal, pandanganku tertuju pada sebuah buku kecil bersampul kulit cokelat tebal yang tergeletak di antara buku-buku tebal. Di sampulnya tertera tulisan tangan pudar bertuliskan 'Catatan Harian Kota, 1924'.

Dengan hati-hati, aku membuka lembaran kertas kekuningan yang rapuh tersebut. Betapa terkejutnya aku ketika menemukan sebuah peta tua yang digambar tangan dengan tinta hitam, disertai beberapa foto hitam-putih berukuran saku. Foto-foto tersebut memperlihatkan jalan raya di depan rumahku seratus tahun yang lalu, di mana belum ada gedung bertingkat maupun mobil modern, melainkan hanya delman yang ditarik kuda dan kanal-kanal air jernih yang tenang.

Di lembaran terakhir buku tersebut, terselip sebuah surat cinta singkat yang belum sempat terkirim dari seorang pemuda pejuang kemerdekaan kepada kekasihnya. Membaca buku misterius itu membuatku merasa seolah-olah sedang melintasi lorong waktu. Aku menyerahkan buku berharga tersebut kepada kepala pustakawan agar dapat dirawat dan dipamerkan dalam pameran arsip kota. Pengalaman tak terduga ini menyadarkanku bahwa setiap sudut kota kita menyimpan cerita masa lalu yang berharga.""",
        "paragraphs": [
            ("Di sudut kawasan Kota Tua yang tenang, berdiri sebuah gedung tua peninggalan zaman kolonial Belanda yang sekarang difungsikan sebagai perpustakaan arsip sejarah kota. Suatu sore saat hujan rintik-rintik, aku mengunjungi perpustakaan itu untuk mencari bahan tugas sejarah sekolah.",
             "旧市街（コタ・トゥア）の静かな一角に、現在は市の歴史公文書図書館として機能している、オランダ植民地時代遺産の古い建物が建っています。ある小雨の降る夕方、僕は学校の歴史の宿題の資料を探すためにその図書館を訪れました。",
             "kawasan Kota Tua（旧市街地区）、peninggalan zaman kolonial（植民地時代の遺産）、arsip sejarah（歴史公文書・アーカイブ）。"),
            ("Ruangan perpustakaan itu dipenuhi oleh rak-rak kayu jati raksasa yang menampung ribuan buku kuno berdebu. Saat aku menelusuri lorong paling belakang di bagian sejarah lokal, pandanganku tertuju pada sebuah buku kecil bersampul kulit cokelat tebal yang tergeletak di antara buku-buku tebal. Di sampulnya tertera tulisan tangan pudar bertuliskan 'Catatan Harian Kota, 1924'.",
             "図書館の室内は、何千冊もの埃っぽい古書を収めた巨大なチーク材の棚で満ちていました。郷土史コーナーの一番奥の通路を歩いていた時、僕の視線は分厚い本たちの間に横たわっている分厚い茶色の革表紙の小さな本に釘付けになりました。その表紙には「1924年・都市の日記」と書かれた色あせた手書きの文字が刻まれていました。",
             "kayu jati（チーク材・高級木材）、menelusuri lorong（通路を歩き回る・探索する）、tulisan tangan pudar（色あせた手書き文字）。"),
            ("Dengan hati-hati, aku membuka lembaran kertas kekuningan yang rapuh tersebut. Betapa terkejutnya aku ketika menemukan sebuah peta tua yang digambar tangan dengan tinta hitam, disertai beberapa foto hitam-putih berukuran saku. Foto-foto tersebut memperlihatkan jalan raya di depan rumahku seratus tahun yang lalu, di mana belum ada gedung bertingkat maupun mobil modern, melainkan hanya delman yang ditarik kuda dan kanal-kanal air jernih yang tenang.",
             "慎重に、僕はその脆い黄色味を帯びた紙のページを開きました。黒インクで手描きされた古い地図と、ポケットサイズの何枚かの白黒写真を発見した時、僕はなんと驚いたことでしょう。それらの写真は100年前の僕の家の前の大通りを写し出しており、そこには高層ビルも現代の車もなく、ただ馬に引かれた馬車（デルマン）と穏やかな清らかな運河だけがありました。",
             "kertas kekuningan rapuh（黄ばんだ脆い紙）、foto hitam-putih（白黒写真）、delman yang ditarik kuda（馬に引かれる馬車）、kanal air（運河）。"),
            ("Di lembaran terakhir buku tersebut, terselip sebuah surat cinta singkat yang belum sempat terkirim dari seorang pemuda pejuang kemerdekaan kepada kekasihnya. Membaca buku misterius itu membuatku merasa seolah-olah sedang melintasi lorong waktu. Aku menyerahkan buku berharga tersebut kepada kepala pustakawan agar dapat dirawat dan dipamerkan dalam pameran arsip kota. Pengalaman tak terduga ini menyadarkanku bahwa setiap sudut kota kita menyimpan cerita masa lalu yang berharga.",
             "その本の最後のページには、独立闘争の青年から恋人へ宛てた、まだ送られる機会のなかった短いラブレターが挟まっていました。その神秘的な本を読むことは、僕にまるでタイムトンネルを通り抜けているかのような感覚を抱かせました。僕はその貴重な本が適切に保存され、市の公文書展で展示されるように、館長に引き渡しました。この思いがけない体験は、僕たちの街のあらゆる街角が貴重な過去の物語を秘めているのだと気づかせてくれました。",
             "pejuang kemerdekaan（独立闘争の戦士）、melintasi lorong waktu（タイムトンネルを通り抜ける）、pengalaman tak terduga（予期せぬ思いがけない体験）。")
        ],
        "vocab": [
            ("Kota Tua", "固有名詞", "-", "コタ・トゥア（ジャカルタ等の旧市街・オランダ植民地時代の歴史遺産地区）", "Kawasan Kota Tua ramai dikunjungi turis."),
            ("kayu jati", "名詞句", "-", "チーク材（硬質で耐久性の高い高級木材）", "Meja kuno ini terbuat dari kayu jati asli."),
            ("menelusuri", "動詞", "telusur", "（道・通路・歴史を）たどる、探索する", "Polisi menelusuri jejak pelaku kejahatan."),
            ("pudar", "形容詞", "-", "色あせた、薄れた、かすれた", "Warna cat dinding mulai pudar termakan usia."),
            ("rapuh", "形容詞", "-", "もろい、壊れやすい、破れやすい", "Kertas dokumen kuno itu sangat rapuh."),
            ("delman", "名詞", "-", "デルマン（2輪または4輪の伝統的乗用馬車）", "Wisatawan naik delman berkeliling alun-alun."),
            ("terselip", "動詞", "selip", "（何かの間に）挟まっている、滑り込んでいる", "Surat rahasia terselip di balik sampul buku."),
            ("seolah-olah", "接続詞/副詞", "-", "まるで〜であるかのように", "Dia berbicara seolah-olah tahu segalanya."),
            ("pustakawan", "名詞", "pustaka", "司書、図書館員", "Pustakawan membantu merestorasi naskah kuno."),
            ("tak terduga", "形容詞句", "duga", "思いがけない、予期せぬ、サプライズの", "Kami mendapat kejutan yang tak terduga.")
        ],
        "grammar_points": """1. **まるで〜かのようを表す比喩接続詞 `seolah-olah`**:
   - *seolah-olah sedang melintasi lorong waktu*（まるでタイムトンネルをくぐっているかのように）
   - *Dia tersenyum seolah-olah tidak terjadi apa-apa.*（彼はまるで何もなかったかのように微笑んだ）
2. **打消しと対比 `bukan ... melainkan ...`（〜ではなく、むしろ〜）**:
   - *belum ada mobil, melainkan hanya delman*（車はなく、むしろ馬車だけであった）
   - *bukan uang yang kucari, melainkan pengalaman*（私が探しているのはお金ではなく、むしろ経験である）
3. **無意識・偶発の接頭辞 `ter-`**:
   - *tertuju*（視線が引きつけられる・向けられる）
   - *tergeletak*（無造作に置かれている・転がっている）
   - *tertera*（印刷されている・記されている）
   - *terselip*（挟まっている）""",
        "quizzes": [
            ("ブディ君が訪れた公文書図書館の建物は、元々いつの時代の遺産（peninggalan）ですか？",
             ["古代マタラム王国時代", "オランダ植民地時代（zaman kolonial Belanda）", "日本の占領時代"],
             "オランダ植民地時代（zaman kolonial Belanda）",
             "第1段落に「...sebuah gedung tua peninggalan zaman kolonial Belanda...」とあります。"),
            ("古い革表紙の手帳の中に挟まっていた100年前の写真には、現代の自動車の代わりに何が写っていましたか？",
             ["電車（kereta listrik）", "馬に引かれた馬車（delman yang ditarik kuda）", "飛行機（pesawat）"],
             "馬に引かれた馬車（delman yang ditarik kuda）",
             "第3段落に「...belum ada gedung bertingkat maupun mobil modern, melainkan hanya delman yang ditarik kuda...」とあります。"),
            ("本の最後のページに挟まっていた、まだ送られていなかった手紙の送り主は誰でしたか？",
             ["オランダの総督", "独立闘争の青年戦士（pemuda pejuang kemerdekaan）", "図書館の初代館長"],
             "独立闘争の青年戦士（pemuda pejuang kemerdekaan）",
             "第4段落に「...sebuah surat cinta singkat yang belum sempat terkirim dari seorang pemuda pejuang kemerdekaan kepada kekasihnya.」とあります。")
        ],
        "culture": """### ジャカルタの「Kota Tua（旧市街・バタヴィア）」と歴史的建造物
ジャカルタ北部に位置する「コタ・トゥア（Kota Tua: 旧バタヴィア）」は、17世紀にオランダ東インド会社（VOC）がアジア支配の拠点として築いた城塞都市の遺構です。
運河（Kanal）沿いに立ち並ぶ重厚なオランダ建築（ファタヒラ広場や旧市庁舎）は、現在では博物館や公文書館、カフェ（Café Batavia）として保存活用されています。古い街並みを歩き、歴史の層を感じる散策（Heritage Walk）は、若者や歴史愛好家の間で絶大な人気を誇ります。"""
    },
    {
        "id": "1220",
        "slug": "level-2-10-level2-review-quiz",
        "title": "【Level 2 (A2) 総括】Petualangan Menjelajah Nusantara & 総合読解診断テスト",
        "desc": "Level 2（A2初級編）の全10テーマの集大成。群島横断の総括ストーリー「プトゥアランガン・ヌサンタラ」の読解と、A2総合実力判定テスト。",
        "text": """Namaku Budi. Tahun ini adalah tahun yang penuh dengan petualangan luar biasa dalam menjelajahi keindahan nusantara. Dari kota asalku di Bandung, aku telah menempuh berbagai perjalanan yang membuka wawasanku tentang kekayaan budaya dan alam Indonesia yang menakjubkan.

Aku masih ingat betapa serunya naik kereta api malam menuju Yogyakarta. Di sana, aku mengagumi kemegahan Keraton, belajar teknik membatik tulis yang sarat makna, dan mencicipi manisnya Gudeg Malioboro. Di desa kakek di Garut, aku belajar menghargai perjuangan para petani dengan menanam padi di sawah berlumpur, serta merasakan kehangatan semangat gotong royong saat warga bersatu membersihkan saluran air akibat hujan deras.

Tak kalah berkesan, saat berkunjung ke rumah nenek di Padang, aku menyaksikan kesabaran bibiku memasak rendang daging sapi selama empat jam di atas tungku kayu bakar. Di kebun binatang, aku menyaksikan keagungan komodo dan lincahnya orangutan yang harus kita lindungi dari kepunahan. Kak Dimas pun telah membuktikan arti kemandirian dengan membeli ponsel pintar pertamanya dari tabungan hasil kerja kerasnya sendiri.

Semua pengalaman ini terekam abadi dalam ingatanku, bagaikan lembaran buku harian kuno yang kutemukan di perpustakaan Kota Tua. Menjelajahi Indonesia bukan hanya tentang melihat tempat-tempat baru yang indah, melainkan tentang memahami nilai persaudaraan, kerja keras, dan keharmonisan hidup bersama alam. Aku bangga menjadi anak Indonesia yang cinta tanah air.""",
        "paragraphs": [
            ("Namaku Budi. Tahun ini adalah tahun yang penuh dengan petualangan luar biasa dalam menjelajahi keindahan nusantara. Dari kota asalku di Bandung, aku telah menempuh berbagai perjalanan yang membuka wawasanku tentang kekayaan budaya dan alam Indonesia yang menakjubkan.",
             "僕の名前はブディです。今年は、群島（ヌサンタラ）の美しさを探索する並外れた冒険に満ちた1年でした。僕の故郷であるバンドン市から、僕はインドネシアの息をのむほど素晴らしい自然と文化の豊かさについての視野を広げてくれる様々な旅を経験しました。",
             "menjelajahi nusantara（群島を探検する）、membuka wawasan（視野を広げる）、menakjubkan（息をのむほど素晴らしい）。"),
            ("Aku masih ingat betapa serunya naik kereta api malam menuju Yogyakarta. Di sana, aku mengagumi kemegahan Keraton, belajar teknik membatik tulis yang sarat makna, dan mencicipi manisnya Gudeg Malioboro. Di desa kakek di Garut, aku belajar menghargai perjuangan para petani dengan menanam padi di sawah berlumpur, serta merasakan kehangatan semangat gotong royong saat warga bersatu membersihkan saluran air akibat hujan deras.",
             "僕はジョグジャカルタへ向かう夜行列車に乗ったのがどれほどエキサイティングだったかを今でも覚えています。そこで僕は王宮の壮大さに見とれ、深い意味を持つ手描きバティックの技法を学び、マリオボロ・グドゥグの甘さを味わいました。ガルットの祖父の村では、泥だらけの田んぼで稲を植えることで農民たちの奮闘に感謝することを学び、激しい雨による水路の掃除で住民が一致団結した時のゴトン・ロヨンの精神の温かさを実感しました。",
             "Level 2 の各ストーリー（ジョグジャ夜行列車、バティック、ガルットの田植え、豪雨のゴトンロヨン）が鮮やかに連結。"),
            ("Tak kalah berkesan, saat berkunjung ke rumah nenek di Padang, aku menyaksikan kesabaran bibiku memasak rendang daging sapi selama empat jam di atas tungku kayu bakar. Di kebun binatang, aku menyaksikan keagungan komodo dan lincahnya orangutan yang harus kita lindungi dari kepunahan. Kak Dimas pun telah membuktikan arti kemandirian dengan membeli ponsel pintar pertamanya dari tabungan hasil kerja kerasnya sendiri.",
             "それに劣らず印象的だったのは、パダンの祖母の家を訪れた時、叔母さんが薪のかまどの上で4時間かけて牛肉のルンダンを作る忍耐を目撃したことです。動物園では、僕たちが絶滅から守らなければならないコモドオオトカゲの威厳とオランウータンの身軽さを目の当たりにしました。ディマス兄さんもまた、自分自身の努力の結晶である貯金から初めてのスマートフォンを購入することで自立の意味を証明しました。",
             "パダン・ルンダン、ラグナン動物園のコモド、兄の自立スマホ購入のエピソードが総括される。"),
            ("Semua pengalaman ini terekam abadi dalam ingatanku, bagaikan lembaran buku harian kuno yang kutemukan di perpustakaan Kota Tua. Menjelajahi Indonesia bukan hanya tentang melihat tempat-tempat baru yang indah, melainkan tentang memahami nilai persaudaraan, kerja keras, dan keharmonisan hidup bersama alam. Aku bangga menjadi anak Indonesia yang cinta tanah air.",
             "これらすべての経験は、旧市街の図書館で見つけた古い日記のページのように、僕の記憶の中に永遠に刻まれています。インドネシアを探検することは、単に美しい新しい場所を見ることだけでなく、同胞の絆、勤勉、そして自然とともに生きる調和の価値を理解することです。僕は祖国を愛するインドネシアの子どもであることを誇りに思います。",
             "Level 2 全編を貫くテーマ（persaudaraan, kerja keras, keharmonisan）の堂々たる総括。")
        ],
        "vocab": [
            ("menjelajahi", "動詞", "jelajah", "探索する、踏破する、旅して回る", "Penjelajah menjelajahi hutan rimba."),
            ("membuka wawasan", "動詞句", "wawas", "視野を広げる、見聞を広める", "Membaca buku membuka wawasan kita."),
            ("menakjubkan", "形容詞", "takjub", "息をのむほど素晴らしい、驚嘆すべき", "Pemandangan bawah laut sangat menakjubkan."),
            ("sarat makna", "形容詞句", "sarat", "深い意味に満ちた、含蓄のある", "Motif batik tradisional sarat makna filosofis."),
            ("perjuangan", "名詞", "juang", "奮闘、戦い、努力", "Perjuangan pahlawan membuahkan kemerdekaan."),
            ("tak kalah berkesan", "慣用句", "kalah", "それに劣らず印象的な", "Pengalaman kedua tak kalah berkesan."),
            ("menyaksikan", "動詞", "saksi", "目撃する、目の当たりにする", "Ribuan warga menyaksikan pesta kembang api."),
            ("kepunahan", "名詞", "punah", "絶滅、死滅", "Lindungi satwa liar dari ancaman kepunahan."),
            ("terekam abadi", "形容詞句", "rekam", "永遠に記録された、不滅の記憶となった", "Kenangan indah terekam abadi di hati."),
            ("tanah air", "名詞句", "tanah", "祖国（直訳: 土地と水＝群島国家）", "Rakyat membela kedaulatan tanah air.")
        ],
        "grammar_points": """### Level 2 (CEFR A2) 文法マスターチェックリスト
1. **動詞接頭辞 `meN-` の他動詞活用体系**:
   - 目的語を伴う能動動作の基本形（*menjelajahi*, *menyaksikan*, *mencicipi*, *mengagumi*）。
2. **動詞接頭辞 `ber-` の自動詞・状態表現**:
   - 所有、状態、相互関係（*berlibur*, *berkumpul*, *bersatu*, *berkesan*）。
3. **無意志・偶発・状態の `ter-`**:
   - *terekam*（刻まれている）、*terbuka*（開かれている）、*terkenal*（有名な）。
4. **論理的複文を構築する重要接続詞**:
   - 原因・理由: *karena*, *sebab*, *akibat*
   - 結果: *sehingga*, *akibatnya*
   - 逆接・対比: *tetapi*, *namun*, *sedangkan*, *bukan... melainkan...*
   - 時間・条件: *saat*, *ketika*, *sebelum*, *sesudah*, *jika*""",
        "quizzes": [
            ("総括ストーリーにおいて、ブディ君の出身都市（kota asal）はどこですか？",
             ["ジャカルタ（Jakarta）", "バンドン（Bandung）", "スラバヤ（Surabaya）"],
             "バンドン（Bandung）",
             "第1段落に「Dari kota asalku di Bandung...」とあります。"),
            ("パダンの祖母の家で、叔母さんが薪のかまどで牛肉のルンダンを作るのにかかった時間は？",
             ["30分間", "4時間（selama empat jam）", "一昼夜（24時間）"],
             "4時間（selama empat jam）",
             "第3段落に「...memasak rendang daging sapi selama empat jam di atas tungku kayu bakar.」とあります。"),
            ("ブディ君がこの1年間の様々な旅（ヌサンタラ探索）を通じて学んだ、最も重要な価値観は何ですか？",
             ["お金持ちになる方法", "同胞の絆、勤勉、そして自然と調和して生きることの尊さ（nilai persaudaraan, kerja keras, dan keharmonisan）", "都会の高層ビルの素晴らしさ"],
             "同胞の絆、勤勉、そして自然と調和して生きることの尊さ（nilai persaudaraan, kerja keras, dan keharmonisan）",
             "第4段落に「...melainkan tentang memahami nilai persaudaraan, kerja keras, dan keharmonisan hidup bersama alam.」と明記されています。")
        ],
        "culture": """### CEFR A2 レベル修了おめでとうございます！
本記事をもって、セクション30の「Level 2 (CEFR A2 初級編: 1211〜1220)」全10記事をすべて完結しました！
A2レベルを修了したあなたは、インドネシアの主要な文化・地域（ジョグジャカルタの王宮とバティック、農村の田植えとゴトンロヨン、パダンのルンダン、国立動物園の固有種、旧市街の歴史遺産）を舞台にした、複文を含むまとまった物語を自然に読み解く読解力を手に入れました。
次の「Level 3 (CEFR B1 中級編: 1221〜1230)」では、伝統儀礼、環境問題、地域社会の変革など、より深層的なインドネシアのリアリティに迫る中級長文読解へと挑みます！"""
    }
]

all_level2 = stories + more_level2_stories

output_dir = "docs/graded-reading"
os.makedirs(output_dir, exist_ok=True)

for st in all_level2:
    filename = f"{st['slug']}.md"
    filepath = os.path.join(output_dir, filename)
    
    lines = []
    lines.append(f"# {st['title']}")
    lines.append("")
    lines.append(f"> [!NOTE]")
    lvl = st.get('level', 'CEFR A2（初級レベル・想定語彙数 600〜1,000語）')
    lines.append(f"> **難易度**: {lvl} | **読解目標**: {st['desc']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. 本文ストーリー（Teks Bacaan）")
    lines.append("")
    lines.append(st["text"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. 段落ごとの対訳と読解ポイント（Terjemahan & Analisis）")
    lines.append("")
    
    for p_idx, para in enumerate(st["paragraphs"], 1):
        ind_p, jp_p, point_p = para
        lines.append(f"### 第{p_idx}段落")
        lines.append("")
        lines.append('<div class="id-example">')
        lines.append("")
        lines.append(f"**インドネシア語本文**:\n{ind_p}")
        lines.append("")
        lines.append(f"**日本語対訳**:\n{jp_p}")
        lines.append("")
        lines.append(f"**読解・文法の着眼点**: {point_p}")
        lines.append("")
        lines.append("</div>")
        lines.append("")
        
    lines.append("---")
    lines.append("")
    lines.append("## 3. 重要語彙・表現10選（Kosakata Kunci）")
    lines.append("")
    lines.append("| 単語・表現 | 品詞 | 語根 | 日本語の意味 | 例文 |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for v in st["vocab"]:
        w, pos, root, mean, ex = v
        lines.append(f"| **{w}** | {pos} | `{root}` | {mean} | `{ex}` |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. 文法・構文の徹底解説（Tata Bahasa）")
    lines.append("")
    lines.append(st["grammar_points"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. 読解力チェッククイズ（Latihan Pemahaman）")
    lines.append("")
    lines.append("ストーリーの内容を正確に読み取れているか、以下の3問で確認しましょう。")
    lines.append("")
    
    for q_idx, quiz in enumerate(st["quizzes"], 1):
        q_text, options, correct, explanation = quiz
        lines.append(f"### クイズ第{q_idx}問: {q_text}")
        lines.append("")
        for opt in options:
            lines.append(f"- [ ] {opt}")
        lines.append("")
        lines.append("<details>")
        lines.append(f"<summary>正解と解説を確認する</summary>")
        lines.append("")
        # Safe bracket formatting in correct answer:
        m_ans = re.match(r'^(「.+?」)(.+?)$', correct)
        if m_ans:
            c_tag = m_ans.group(1)
            c_rest = m_ans.group(2)
            lines.append(f"**正解**: {c_tag}**{c_rest}**")
        else:
            lines.append(f"**正解**: **{correct}**")
        lines.append("")
        lines.append(f"**解説**: {explanation}")
        lines.append("")
        lines.append("</details>")
        lines.append("")
        
    lines.append("---")
    lines.append("")
    lines.append("## 6. 背景知識・文化コラム（Wawasan Budaya）")
    lines.append("")
    lines.append(st["culture"])
    lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated {filepath}")

print("All 10 Graded Reading Level 2 articles generated successfully.")
