# -*- coding: utf-8 -*-
import os
import re

stories = [
    {
        "id": "1201",
        "slug": "level-1-01-morning-routine",
        "title": "【Level 1 (A1)】Pagi Hari di Rumah Budi（ブディ君の爽やかな朝の日常）",
        "level": "CEFR A1（入門レベル・想定語彙数 300〜500語）",
        "desc": "インドネシアの典型的な朝の生活習慣を平易な現在形・基本語順で描いた入門ストーリー。水浴び（mandi）や朝食表現をマスターする。",
        "text": """Namaku Budi. Umurku sepuluh tahun. Setiap hari, aku bangun tidur pada jam lima pagi. Udara pagi di rumahku terasa sangat sejuk dan segar.

Setelah bangun tidur, aku segera merapikan tempat tidur. Lalu, aku pergi ke kamar mandi untuk mandi dan menggosok gigi. Air di bak mandi sangat dingin, tetapi membuat badanku terasa segar dan bersemangat.

Pada jam enam pagi, ibu memanggilku untuk sarapan bersama di meja makan. Ayah sedang membaca koran sambil minum kopi hitam hangat. Ibu memasak nasi goreng yang sangat lezat dengan telur mata sapi. Kami makan bersama dengan gembira sambil mengobrol santai.

Selesai sarapan, aku memakai seragam sekolah merah putih yang bersih dan rapi. Aku berpamitan kepada ayah dan ibu, lalu mencium tangan mereka. Pada jam setengah tujuh, aku berjalan kaki menuju sekolah bersama teman-temanku.""",
        "paragraphs": [
            ("Namaku Budi. Umurku sepuluh tahun. Setiap hari, aku bangun tidur pada jam lima pagi. Udara pagi di rumahku terasa sangat sejuk dan segar.",
             "僕の名前はブディです。10歳です。毎日、朝の5時に起きます。僕の家の朝の空気はとても涼しくて爽やかです。",
             "所有代名詞 -ku（namaku, umurku, rumahku）と基本語順 S + V（aku bangun tidur）の平易な構文。"),
            ("Setelah bangun tidur, aku segera merapikan tempat tidur. Lalu, aku pergi ke kamar mandi untuk mandi dan menggosok gigi. Air di bak mandi sangat dingin, tetapi membuat badanku terasa segar dan bersemangat.",
             "起きた後、僕はすぐにベッドを整えます。それから、水浴びと歯磨きのためにバスルームへ行きます。水桶の水はとても冷たいですが、僕の体を爽やかで元気にしてくれます。",
             "kamar mandi（バスルーム）や bak mandi（水桶）など、インドネシアの伝統的な入浴文化が登場。"),
            ("Pada jam enam pagi, ibu memanggilku untuk sarapan bersama di meja makan. Ayah sedang membaca koran sambil minum kopi hitam hangat. Ibu memasak nasi goreng yang sangat lezat dengan telur mata sapi. Kami makan bersama dengan gembira sambil mengobrol santai.",
             "朝の6時に、お母さんが僕を呼んで食卓で一緒に朝ご飯を食べます。お父さんは温かいブラックコーヒーを飲みながら新聞を読んでいます。お母さんは目玉焼きを乗せたとても美味しいナシゴレンを作ってくれました。僕たちはリラックスしておしゃべりしながら、楽しく一緒に食べます。",
             "sedang + 動詞（〜している進行形）や sambil（〜しながら）の並行動作表現に注目。telur mata sapi は目玉焼き。"),
            ("Selesai sarapan, aku memakai seragam sekolah merah putih yang bersih dan rapi. Aku berpamitan kepada ayah dan ibu, lalu mencium tangan mereka. Pada jam setengah tujuh, aku berjalan kaki menuju sekolah bersama teman-temanku.",
             "朝食を終えて、僕は清潔で整った赤白の学校の制服を着ます。お父さんとお母さんに行ってきますの挨拶をして、両親の手にキスをします。6時半に、僕は友達と一緒に歩いて学校へ向かいます。",
             "seragam merah putih（公立小学校の赤白制服）や、両親・年長者の手に鼻や唇を寄せる敬愛の挨拶文化（salim）が描かれています。")
        ],
        "vocab": [
            ("bangun tidur", "動詞句", "bangun", "起きる、起床する", "Aku bangun pagi setiap hari."),
            ("sejuk", "形容詞", "-", "涼しい、爽やかな", "Udara di pegunungan sangat sejuk."),
            ("kamar mandi", "名詞句", "kamar", "バスルーム、水浴び場", "Dia sedang berada di kamar mandi."),
            ("menggosok gigi", "動詞句", "gosok", "歯を磨く", "Jangan lupa menggosok gigi sebelum tidur."),
            ("sarapan", "名詞/動詞", "sarap", "朝食、朝ご飯を食べる", "Kami sarapan nasi goreng tadi pagi."),
            ("kopi hitam", "名詞句", "kopi", "ブラックコーヒー", "Ayah suka minum kopi hitam hangat."),
            ("telur mata sapi", "名詞句", "telur", "目玉焼き（牛の目卵）", "Saya suka makan nasi dengan telur mata sapi."),
            ("seragam", "名詞", "ragam", "制服、ユニフォーム", "Murid SD memakai seragam merah putih."),
            ("berpamitan", "動詞", "pamit", "別れの挨拶をする、行ってきますを言う", "Budi berpamitan kepada orang tuanya."),
            ("mencium tangan", "動詞句", "cium", "（敬意を込めて）手にキスをする", "Anak itu mencium tangan kakeknya.")
        ],
        "grammar_points": """1. **所有親称接尾辞 `-ku`（私の〜）**:
   - 名詞の直後にくっついて「私の」を表します。
   - *nama*（名前）＋ *-ku* → *namaku*（私の名前）
   - *rumah*（家）＋ *-ku* → *rumahku*（私の家）
2. **時刻の表現 `pada jam ...`**:
   - *pada jam lima pagi*（朝の5時に）
   - *pada jam setengah tujuh*（6時半に / 7時の半分手前）
3. **前置詞 `di`, `ke`, `dari` の使い分け**:
   - *di rumah*（家で・場所）
   - *ke kamar mandi*（バスルームへ・方向）
   - *dari tempat tidur*（ベッドから・起点）""",
        "quizzes": [
            ("ブディ君は毎朝何時に起きますか？",
             ["朝の4時", "朝の5時", "朝の6時半"],
             "朝の5時",
             "本文第1段落に「Setiap hari, aku bangun tidur pada jam lima pagi.（毎日、朝の5時に起きます）」と明記されています。"),
            ("ブディ君のお母さんが作った朝食のメニューは何ですか？",
             ["サテ・アヤム（鶏肉の串焼き）", "目玉焼きを乗せたナシゴレン", "トーストと温かいミルク"],
             "目玉焼きを乗せたナシゴレン",
             "第3段落に「Ibu memasak nasi goreng yang sangat lezat dengan telur mata sapi.」とあります。"),
            ("学校へ行く前、ブディ君は両親に対してインドネシアの伝統としてどのような挨拶をしましたか？",
             ["お辞儀をした", "握手をして抱き合った", "行ってきますの挨拶をして、両親の手にキス（敬意を表す接触）をした"],
             "行ってきますの挨拶をして、両親の手にキス（敬意を表す接触）をした",
             "第4段落に「Aku berpamitan kepada ayah dan ibu, lalu mencium tangan mereka.」とあり、インドネシアの美しい伝統「salim（年長者の手に触れて敬意を示す）」が描かれています。")
        ],
        "culture": """### インドネシアの朝の文化と習慣
インドネシアの朝は非常に早いです。イスラム教の夜明け前の礼拝（Subuh）が朝4時半頃に行われるため、多くの家庭が朝5時前には起床して一日をスタートさせます。
また、学校の始業時間も早く、多くの小中高校が朝6時半〜7時に始まります。そのため、朝6時には制服を着た子供たちが元気に登校する姿が見られます。
小学校の制服は国旗と同じ「赤（ズボン・スカート）と白（シャツ）」、中学校は「紺と白」、高校は「グレーと白」と全国で統一されています。"""
    },
    {
        "id": "1202",
        "slug": "level-1-02-traditional-market",
        "title": "【Level 1 (A1)】Pergi ke Pasar Tradisional（お母さんと伝統市場へ買い物）",
        "desc": "伝統市場の活気あふれる風景と、野菜・果物の名前、買い物の基本フレーズ（いくらですか？など）を身につけるA1ストーリー。",
        "text": """Hari Minggu pagi, ibu mengajakku pergi ke pasar tradisional. Pasar itu terletak tidak jauh dari rumah kami. Kami berjalan kaki santai sambil menikmati udara pagi.

Suasana di dalam pasar sangat ramai dan meriah. Ada banyak penjual yang menawarkan barang dagangan mereka dengan suara lantang. Kami melihat deretan sayuran segar seperti bayam, wortel, tomat, dan kubis.

Ibu berjalan menuju kios buah. Di sana, ada banyak buah tropis yang manis dan berwarna-warni. Ibu membeli satu sisir pisang raja dan dua buah pepaya besar. Ibu bertanya kepada penjual, "Berapa harga pisang ini, Pak?" Penjual menjawab dengan ramah, "Dua puluh ribu rupiah saja, Bu."

Setelah membeli buah, kami membeli ikan segar dan bumbu dapur seperti bawang merah, bawang putih, dan cabai. Keranjang belanjaanku sekarang sudah penuh. Kami pulang ke rumah dengan hati yang senang.""",
        "paragraphs": [
            ("Hari Minggu pagi, ibu mengajakku pergi ke pasar tradisional. Pasar itu terletak tidak jauh dari rumah kami. Kami berjalan kaki santai sambil menikmati udara pagi.",
             "日曜日の朝、お母さんは僕を連れて伝統市場へ行きました。その市場は僕たちの家からそれほど遠くない場所にあります。僕たちは朝の空気を楽しみながら、のんびり歩きました。",
             "mengajakku（私を誘う・連れていく）や terletak（位置する）の基本動詞。"),
            ("Suasana di dalam pasar sangat ramai dan meriah. Ada banyak penjual yang menawarkan barang dagangan mereka dengan suara lantang. Kami melihat deretan sayuran segar seperti bayam, wortel, tomat, dan kubis.",
             "市場の中の雰囲気はとても賑やかで活気があります。大声で商品を勧める売り手がたくさんいます。僕たちはホウレンソウ、ニンジン、トマト、キャベツといった新鮮な野菜の列を見ました。",
             "ramai（賑やか）、meriah（活気がある）、bayam（ホウレンソウ/ヒユナ）、wortel（ニンジン）など市場の頻出語彙。"),
            ("Ibu berjalan menuju kios buah. Di sana, ada banyak buah tropis yang manis dan berwarna-warni. Ibu membeli satu sisir pisang raja dan dua buah pepaya besar. Ibu bertanya kepada penjual, \"Berapa harga pisang ini, Pak?\" Penjual menjawab dengan ramah, \"Dua puluh ribu rupiah saja, Bu.\"",
             "お母さんは果物の売店へ歩いていきました。そこには、甘くて色とりどりの熱帯の果物がたくさんあります。お母さんはバナナひと房と大きなパパイヤを2個買いました。お母さんは店員に尋ねました。「このバナナはおいくらですか、ご主人？」。店員は愛想よく答えました。「2万ルピアですよ、奥さん」。",
             "satu sisir（バナナのひと房）の助数詞や、値段を聞く定番表現「Berapa harga ...?」。"),
            ("Setelah membeli buah, kami membeli ikan segar dan bumbu dapur seperti bawang merah, bawang putih, dan cabai. Keranjang belanjaanku sekarang sudah penuh. Kami pulang ke rumah dengan hati yang senang.",
             "果物を買った後、僕たちは新鮮な魚と、赤わけぎ、ニンニク、唐辛子といった料理の調味料を買いました。僕の買い物かごは今やもういっぱいです。僕たちは嬉しい気持ちで家に帰りました。",
             "インドネシア料理の三種の神器「bawang merah（赤わけぎ）、bawang putih（ニンニク）、cabai（唐辛子）」が登場。")
        ],
        "vocab": [
            ("pasar tradisional", "名詞句", "pasar", "伝統市場", "Pasar tradisional buka sejak subuh."),
            ("ramai", "形容詞", "-", "賑やかな、人が多い", "Pasar ini selalu ramai setiap pagi."),
            ("penjual", "名詞", "jual", "売り手、店員", "Penjual itu sangat ramah kepada pembeli."),
            ("sayuran segar", "名詞句", "sayur", "新鮮な野菜", "Ibu membeli sayuran segar untuk dimasak."),
            ("kios", "名詞", "-", "売店、小さな店舗", "Ada kios buah di pojok pasar."),
            ("buah tropis", "名詞句", "buah", "熱帯果物", "Indonesia kaya akan buah tropis yang lezat."),
            ("satu sisir", "助数詞句", "sisir", "（バナナの）ひと房", "Ibu membeli satu sisir pisang matang."),
            ("bumbu dapur", "名詞句", "bumbu", "台所の調味料・スパイス", "Bumbu dapur membuat masakan menjadi harum."),
            ("bawang merah", "名詞句", "bawang", "赤わけぎ、シャロット", "Bawang merah adalah bumbu dasar masakan."),
            ("keranjang", "名詞", "-", "かご、バスケット", "Keranjang belanja penuh dengan sayur dan buah.")
        ],
        "grammar_points": """1. **値段を尋ねる疑問文 `Berapa harga ...?`**:
   - *Berapa harga pisang ini?*（このバナナはおいくらですか？）
   - 簡略形: *Berapa harganya?*（いくらですか？）
   - 口語形: *Berapaan?*（いくら？）
2. **バナナ専用の助数詞 `sisir`（くし・房）**:
   - バナナの1本は *satu buah* または *satu biji*。
   - 房（平たい列）は *satu sisir*（くしの歯のような形状から）。
   - 房がたくさんついた巨大な幹ごとは *satu tandan*。
3. **指示詞 `ini`（これ・この）と `itu`（あれ・その）の語順**:
   - 名詞の**後ろ**に置きます。
   - *pasar itu*（その市場）
   - *pisang ini*（このバナナ）""",
        "quizzes": [
            ("お母さんとブディ君は日曜日、何のためにどこへ行きましたか？",
             ["スーパーマーケットへ服を買いに行った", "伝統市場へ野菜や果物などの買い物に行った", "公園へサッカーをしに行った"],
             "伝統市場へ野菜や果物などの買い物に行った",
             "第1段落に「Hari Minggu pagi, ibu mengajakku pergi ke pasar tradisional.」とあります。"),
            ("お母さんが買ったバナナの値段はいくらでしたか？",
             ["1万ルピア（sepuluh ribu rupiah）", "2万ルピア（dua puluh ribu rupiah）", "5万ルピア（lima puluh ribu rupiah）"],
             "2万ルピア（dua puluh ribu rupiah）",
             "第3段落で店員が「Dua puluh ribu rupiah saja, Bu.」と答えています。"),
            ("買い物の最後に買った、インドネシア料理に欠かせない基本調味料（bumbu dapur）の3点セットは何ですか？",
             ["塩、コショウ、砂糖", "醤油、ケチャップ、マヨネーズ", "赤わけぎ（bawang merah）、ニンニク（bawang putih）、唐辛子（cabai）"],
             "赤わけぎ（bawang merah）、ニンニク（bawang putih）、唐辛子（cabai）",
             "第4段落に「bumbu dapur seperti bawang merah, bawang putih, dan cabai」と明記されています。")
        ],
        "culture": """### インドネシアの伝統市場（Pasar Tradisional）
インドネシアの町や村には、必ず中心となる「伝統市場（Pasar Tradisional）」があります。近代的なスーパーマーケット（Supermarket）が増えた現在でも、食材の新鮮さと安さ、そして店主との温かいコミュニケーションを求めて多くの市民が朝早くから市場を訪れます。
市場では値切り交渉（tawar-menawar）も日常茶飯事であり、「Bisa kurang sedikit, Pak?（少し安くなりませんか？）」などのやり取りを通じて地域コミュニティの絆が育まれています。"""
    },
    {
        "id": "1203",
        "slug": "level-1-03-favorite-food",
        "title": "【Level 1 (A1)】Makanan Indonesia Kesukaanku（大好きなナシゴレンとサテ）",
        "desc": "インドネシアを代表する国民食（ナシゴレン、サテ、ソト）の魅力と、味覚を表す形容詞（甘い、辛い、香ばしい等）を学ぶストーリー。",
        "text": """Indonesia adalah negara yang memiliki banyak makanan lezat. Di antara semua makanan tradisional, ada dua makanan yang paling aku sukai, yaitu nasi goreng dan sate ayam.

Nasi goreng adalah makanan yang sangat populer. Nasi dimasak bersama kecap manis, bawang merah, bawang putih, dan sedikit cabai. Aromanya sangat harum saat digoreng di wajan besar. Biasanya, nasi goreng disajikan bersama telur dadar, potongan mentimun, dan kerupuk yang renyah. Rasanya manis, gurih, dan sedikit pedas.

Makanan kesukaanku yang kedua adalah sate ayam. Daging ayam dipotong kecil-kecil, lalu ditusuk dengan bilah bambu. Daging tersebut dibakar di atas bara arang hingga matang dan harum. Setelah matang, sate disiram dengan saus kacang yang kental dan manis. Aku suka makan sate ayam bersama lontong.

Setiap akhir pekan, keluargaku sering makan malam di warung tenda dekat rumah. Menikmati makanan lezat bersama keluarga membuat hatiku sangat bahagia.""",
        "paragraphs": [
            ("Indonesia adalah negara yang memiliki banyak makanan lezat. Di antara semua makanan tradisional, ada dua makanan yang paling aku sukai, yaitu nasi goreng dan sate ayam.",
             "インドネシアはたくさんの美味しい料理を持つ国です。すべての伝統料理の中で、僕が一番好きな料理が2つあります。それはナシゴレンとサテ・アヤム（焼き鳥）です。",
             "paling aku sukai（私が一番好きな）という最上級表現と、yaitu（すなわち〜）の例示接続詞。"),
            ("Nasi goreng adalah makanan yang sangat populer. Nasi dimasak bersama kecap manis, bawang merah, bawang putih, dan sedikit cabai. Aromanya sangat harum saat digoreng di wajan besar. Biasanya, nasi goreng disajikan bersama telur dadar, potongan mentimun, dan kerupuk yang renyah. Rasanya manis, gurih, dan sedikit pedas.",
             "ナシゴレンは非常に人気のある料理です。ご飯は甘い醤油（ケチャップマニス）、赤わけぎ、ニンニク、そして少しの唐辛子と一緒に炒められます。大きな中華鍋で炒められるときの香りはとても香ばしいです。普段、ナシゴレンは卵焼き、刻んだキュウリ、そしてサクサクのクルプック（揚げ煎餅）と一緒に提供されます。味は甘く、旨味があり、少しピリ辛です。",
             "味覚を表す形容詞：manis（甘い）、gurih（旨味がある・塩気とコク）、pedas（辛い）、renyah（サクサク）。"),
            ("Makanan kesukaanku yang kedua adalah sate ayam. Daging ayam dipotong kecil-kecil, lalu ditusuk dengan bilah bambu. Daging tersebut dibakar di atas bara arang hingga matang dan harum. Setelah matang, sate disiram dengan saus kacang yang kental dan manis. Aku suka makan sate ayam bersama lontong.",
             "僕の2番目の好物はサテ・アヤムです。鶏肉は小さく切られ、竹串に刺されます。その肉は炭火の上で火が通り香ばしくなるまで焼かれます。焼き上がった後、サテには濃厚で甘いピーナッツソースがたっぷりかけられます。僕はサテ・アヤムをロントン（圧縮米の餅）と一緒に食べるのが好きです。",
             "受動態 di- の基本：dipotong（切られる）、ditusuk（刺される）、dibakar（焼かれる）、disiram（かけられる）。"),
            ("Setiap akhir pekan, keluargaku sering makan malam di warung tenda dekat rumah. Menikmati makanan lezat bersama keluarga membuat hatiku sangat bahagia.",
             "毎週末、僕の家族は家の近くの屋台（ワルン・テンダ）でよく夕食を食べます。家族と一緒に美味しい料理を楽しむことは、僕の心をとても幸せにしてくれます。",
             "warung tenda（夜になると歩道に現れるテント式の屋台食堂）は庶民の食文化の象徴。")
        ],
        "vocab": [
            ("makanan lezat", "名詞句", "makan", "美味しい料理", "Restoran ini menyajikan makanan lezat."),
            ("sate ayam", "名詞句", "sate", "インドネシア風焼き鳥", "Sate ayam Madura sangat terkenal."),
            ("kecap manis", "名詞句", "kecap", "インドネシアの甘口醤油", "Kecap manis membuat nasi goreng berwarna cokelat."),
            ("aroma harum", "名詞句", "harum", "香ばしい・良い香り", "Aroma sate bakar sangat menggugah selera."),
            ("kerupuk renyah", "名詞句", "kerupuk", "サクサクの揚げ煎餅", "Makan nasi tanpa kerupuk terasa kurang lengkap."),
            ("gurih", "形容詞", "-", "旨味がある、コクがある、香ばしい", "Kuah sup ini rasanya sangat gurih."),
            ("saus kacang", "名詞句", "saus", "ピーナッツソース", "Sate ayam disiram dengan saus kacang."),
            ("lontong", "名詞", "-", "バナナの葉で包んで煮た圧縮米（米餅）", "Lontong sering dimakan bersama sate."),
            ("warung tenda", "名詞句", "warung", "テント屋台食堂", "Kami makan sate di warung tenda pinggir jalan."),
            ("bahagia", "形容詞", "-", "幸せな、幸福な", "Mereka hidup dengan rukun dan bahagia.")
        ],
        "grammar_points": """1. **基本受動態 `di-`（〜される）**:
   - 初級A1で頻出する客観的受動態。
   - *dimasak*（調理される）
   - *disajikan*（提供される）
   - *dibakar*（焼かれる）
   - *disiram*（注がれる・かけられる）
2. **味覚を表す重要形容詞**:
   - *manis*（甘い）
   - *pedas*（辛い）
   - *asin*（しょっぱい）
   - *asam*（酸っぱい）
   - *pahit*（苦い）
   - *gurih*（旨味・コクがある）
3. **最上級の表現 `paling ...`**:
   - *paling aku sukai*（私が最も好きな）
   - *paling lezat*（一番美味しい）
   - *paling populer*（一番人気がある）""",
        "quizzes": [
            ("ナシゴレンに特徴的な甘みと茶色い色をつける調味料は何ですか？",
             ["トマトケチャップ", "甘口醤油（kecap manis）", "ココナッツミルク（santan）"],
             "甘口醤油（kecap manis）",
             "第2段落に「Nasi dimasak bersama kecap manis...」とあり、大豆とヤシ糖から作られる kecap manis が味の決め手です。"),
            ("サテ・アヤムにたっぷりかけられる濃厚なソースは何のソースですか？",
             ["ピーナッツソース（saus kacang）", "激辛サンバルソース", "マヨネーズ"],
             "ピーナッツソース（saus kacang）",
             "第3段落に「Setelah matang, sate disiram dengan saus kacang yang kental dan manis.」とあります。"),
            ("サテと一緒に主食としてよく食べられる、バナナの葉で包んで固めたお米の食べ物は何ですか？",
             ["ミーゴレン（焼きそば）", "ロントン（lontong）", "ロティ（パン）"],
             "ロントン（lontong）",
             "第3段落に「Aku suka makan sate ayam bersama lontong.」とあります。")
        ],
        "culture": """### インドネシアの食文化とクルプック（Kerupuk）
インドネシアの人々にとって、「クルプック（揚げ煎餅）」は単なるスナックではなく、食事に欠かせない相棒です。「Makan tanpa kerupuk, bagaikan sayur tanpa garam（クルプックのない食事は、塩のない野菜スープのようなもの）」と言われるほど愛されています。
白米やナシゴレン、ソトを食べる際、カリッとしたクルプックを砕いて一緒に口に運ぶことで、食感のコントラスト（サクサク感）を楽しみます。食堂や屋台には、必ず大きな青い缶に入ったクルプックが置かれています。"""
    },
    {
        "id": "1204",
        "slug": "level-1-04-school-friends",
        "title": "【Level 1 (A1)】Teman-Teman di Sekolah Baru（新しい学校の友達と自己紹介）",
        "desc": "新学期のクラスで友達を作り、出身地や趣味を語り合う日常会話ストーリー。自己紹介と疑問文（どこから来たの？趣味は何？）を習得する。",
        "text": """Hari ini adalah hari pertama tahun ajaran baru di sekolahku. Aku sekarang duduk di kelas lima Sekolah Dasar. Di kelasku, ada banyak teman baru yang datang dari berbagai daerah.

Saat jam istirahat, aku berkenalan dengan seorang anak laki-laki bernama Andi. Andi baru saja pindah dari kota Surabaya ke Jakarta karena ayahnya pindah tugas. Wajahnya ramah dan dia murah senyum. Aku menyapanya, "Halo Andi, senang berkenalan denganmu." Andi tersenyum dan menjawab, "Halo Budi, senang bertemu denganmu juga."

Kami duduk di bangku taman sekolah sambil mengobrol tentang hobi kami. Andi bercerita bahwa dia sangat suka bermain sepak bola. Dia bercita-cita menjadi pemain tim nasional Indonesia. Sedangkan aku bercerita bahwa hobiku adalah membaca buku cerita dan menggambar pemandangan alam.

Tidak lama kemudian, Siti datang bergabung bersama kami. Siti adalah teman sekelasku yang pandai menyanyi. Kami bertiga tertawa bersama dan berjanji untuk belajar kelompok bersama nanti sore. Memiliki teman-teman baru membuat hari pertamaku di sekolah terasa sangat menyenangkan.""",
        "paragraphs": [
            ("Hari ini adalah hari pertama tahun ajaran baru di sekolahku. Aku sekarang duduk di kelas lima Sekolah Dasar. Di kelasku, ada banyak teman baru yang datang dari berbagai daerah.",
             "今日は僕の学校の新学期の初日です。僕は今、小学校の5年生です。僕のクラスには、様々な地域からやって来たたくさんの新しい友達がいます。",
             "duduk di kelas lima（5年生に在籍している）の表現。duduk は「座る」から転じて学年に所属することを表す。"),
            ("Saat jam istirahat, aku berkenalan dengan seorang anak laki-laki bernama Andi. Andi baru saja pindah dari kota Surabaya ke Jakarta karena ayahnya pindah tugas. Wajahnya ramah dan dia murah senyum. Aku menyapanya, \"Halo Andi, senang berkenalan denganmu.\" Andi tersenyum dan menjawab, \"Halo Budi, senang bertemu denganmu juga.\"",
             "休み時間に、僕はアンディという名前の男の子と知り合いになりました。アンディはお父さんの転勤のため、スラバヤ市からジャカルタへ引っ越してきたばかりでした。彼の顔立ちは親しみやすく、愛嬌のある笑顔を浮かべています。僕が「ハロー、アンディ、知り合えて嬉しいよ」と声をかけると、アンディは微笑んで「ハロー、ブディ、僕も会えて嬉しいよ」と答えました。",
             "berkenalan（知り合う）、murah senyum（笑顔を絶やさない・愛嬌がある）などの人物描写。"),
            ("Kami duduk di bangku taman sekolah sambil mengobrol tentang hobi kami. Andi bercerita bahwa dia sangat suka bermain sepak bola. Dia bercita-cita menjadi pemain tim nasional Indonesia. Sedangkan aku bercerita bahwa hobiku adalah membaca buku cerita dan menggambar pemandangan alam.",
             "僕たちは学校の庭のベンチに座りながら、お互いの趣味についておしゃべりしました。アンディはサッカーをするのが大好きだと話してくれました。彼はインドネシア代表チームの選手になることを夢見ています。一方、僕の趣味は物語の本を読むことと、自然の風景を描くことだと話しました。",
             "bercerita bahwa（〜だと話す）、bercita-cita（夢を持つ・志す）、sedangkan（一方で）。"),
            ("Tidak lama kemudian, Siti datang bergabung bersama kami. Siti adalah teman sekelasku yang pandai menyanyi. Kami bertiga tertawa bersama dan berjanji untuk belajar kelompok bersama nanti sore. Memiliki teman-teman baru membuat hari pertamaku di sekolah terasa sangat menyenangkan.",
             "まもなくして、シティがやって来て僕たちの輪に加わりました。シティは歌が上手な僕のクラスメイトです。僕たち3人は一緒に笑い合い、今日の夕方に一緒にグループ学習をしようと約束しました。新しい友達ができたことで、学校初日はとても楽しい一日になりました。",
             "bergabung（合流する）、kami bertiga（私たち3人）、belajar kelompok（グループ学習）。")
        ],
        "vocab": [
            ("tahun ajaran baru", "名詞句", "ajar", "新学期、新年度", "Tahun ajaran baru dimulai bulan Juli."),
            ("jam istirahat", "名詞句", "istirahat", "休み時間", "Murid-murid bermain di halaman saat jam istirahat."),
            ("berkenalan", "動詞", "kenal", "知り合う、自己紹介し合う", "Saya ingin berkenalan dengan teman baru."),
            ("pindah", "動詞", "-", "引っ越す、移る", "Keluarganya baru pindah ke rumah baru."),
            ("murah senyum", "慣用表現", "senyum", "笑顔が素敵な、愛嬌がある", "Gadis itu sangat ramah dan murah senyum."),
            ("bercita-cita", "動詞", "cita", "〜を夢見る、志す", "Dia bercita-cita menjadi dokter spesialis."),
            ("tim nasional", "名詞句", "-", "（サッカー等の）国家代表チーム", "Tim nasional Indonesia bermain sangat gigih."),
            ("menggambar", "動詞", "gambar", "絵を描く", "Adik suka menggambar pemandangan gunung."),
            ("pandai", "形容詞", "-", "賢い、〜が得意な", "Siti sangat pandai menyanyi lagu daerah."),
            ("belajar kelompok", "動詞/名詞", "ajar", "グループ学習、勉強会", "Kami mengadakan belajar kelompok setiap sore.")
        ],
        "grammar_points": """1. **接頭辞 `ber-` の基本機能（相互・状態）**:
   - *berkenalan*（お互いに知り合う）
   - *bertemu*（会う）
   - *bercerita*（話をする）
   - *bergabung*（加わる・合流する）
   - *berjanji*（約束する）
2. **数詞 ＋ 接頭辞 `ber-`（〜人グループ）**:
   - *kami berdua*（私たち2人）
   - *kami bertiga*（私たち3人）
   - *mereka berempat*（彼ら4人）
3. **対比の接続詞 `sedangkan`（一方で）**:
   - 2つの対照的な事実を並べるときに使います。
   - *Andi suka sepak bola, sedangkan hobiku menggambar.*（アンディはサッカーが好きで、一方で私の趣味は絵を描くことです）""",
        "quizzes": [
            ("新しく転校してきたアンディ君は、どこの都市からジャカルタへ引っ越してきましたか？",
             ["バンドン（Bandung）", "スラバヤ（Surabaya）", "メダン（Medan）"],
             "スラバヤ（Surabaya）",
             "第2段落に「Andi baru saja pindah dari kota Surabaya ke Jakarta...」と明記されています。"),
            ("アンディ君の将来の夢（cita-cita）は何ですか？",
             ["学校の先生になること", "インドネシア代表チームのサッカー選手になること", "有名な画家になること"],
             "インドネシア代表チームのサッカー選手になること",
             "第3段落に「Dia bercita-cita menjadi pemain tim nasional Indonesia.」とあります。"),
            ("後から合流したクラスメイトのシティちゃんの特技は何ですか？",
             ["料理を作ること", "歌を歌うのが上手なこと（pandai menyanyi）", "速く走ること"],
             "歌を歌うのが上手なこと（pandai menyanyi）",
             "第4段落に「Siti adalah teman sekelasku yang pandai menyanyi.」とあります。")
        ],
        "culture": """### インドネシアの新学期と学校生活
インドネシアの学校の新学期（Tahun Ajaran Baru）は、日本（4月）とは異なり、**7月中旬**に始まります。
小学校は6年間（Sekolah Dasar: SD）、中学校は3年間（Sekolah Menengah Pertama: SMP）、高校は3年間（Sekolah Menengah Atas: SMA）の「6-3-3制」です。
多民族国家であるため、大都市の学校にはジャワ島各地、スマトラ島、スラウェシ島など様々な地方出身の生徒が集まり、共通語であるインドネシア語を通じてすぐに親友になります。放課後には「belajar kelompok（グループ学習）」と称して友達の家に集まり、宿題をしながらおやつを食べるのが子供たちの定番の楽しみです。"""
    },
    {
        "id": "1205",
        "slug": "level-1-05-my-family",
        "title": "【Level 1 (A1)】Keluarga Besarku di Bandung（バンドンに住む温かい大家族）",
        "desc": "西ジャワ州バンドンに暮らす温かい家族の紹介。家族の親称（父、母、兄、妹）や職業、性格を表すA1基本語彙を網羅。",
        "text": """Keluargaku tinggal di kota Bandung, Jawa Barat. Bandung adalah kota yang dikelilingi oleh pegunungan, sehingga udaranya selalu sejuk dan nyaman. Kami tinggal di sebuah rumah sederhana yang memiliki halaman yang asri.

Keluargaku terdiri dari empat orang, yaitu ayah, ibu, seorang kakak laki-laki, dan aku. Ayahku bernama Pak Hendra. Ayah bekerja sebagai seorang arsitek yang merancang gedung-gedung indah. Ayah adalah sosok yang sabar, bijaksana, dan sangat menyayangi keluarga.

Ibuku bernama Ibu Rina. Ibu adalah seorang guru matematika di Sekolah Menengah Pertama. Meskipun sibuk mengajar di sekolah, ibu selalu memasak makanan yang enak untuk kami di rumah. Ibu sangat rajin, ramah, dan pintar membuat kue tradisional Sunda.

Kakak laki-lakiku bernama Dimas. Kak Dimas berumur lima belas tahun dan sekarang duduk di bangku SMA. Kak Dimas sangat gemar bermain gitar dan berolahraga basket. Setiap akhir pekan, kami selalu berkumpul bersama di ruang keluarga untuk menonton televisi atau bernyanyi bersama. Aku sangat bersyukur memiliki keluarga yang harmonis dan penuh kasih sayang.""",
        "paragraphs": [
            ("Keluargaku tinggal di kota Bandung, Jawa Barat. Bandung adalah kota yang dikelilingi oleh pegunungan, sehingga udaranya selalu sejuk dan nyaman. Kami tinggal di sebuah rumah sederhana yang memiliki halaman yang asri.",
             "僕の家族は西ジャワ州のバンドン市に住んでいます。バンドンは山々に囲まれた都市で、そのため空気はいつも涼しくて快適です。僕たちは緑豊かな庭のある素朴な家に住んでいます。",
             "sehingga（その結果〜）の因果接続詞や、asri（緑豊かで美しい）という住環境の重要形容詞。"),
            ("Keluargaku terdiri dari empat orang, yaitu ayah, ibu, seorang kakak laki-laki, dan aku. Ayahku bernama Pak Hendra. Ayah bekerja sebagai seorang arsitek yang merancang gedung-gedung indah. Ayah adalah sosok yang sabar, bijaksana, dan sangat menyayangi keluarga.",
             "僕の家族は4人家族で、父、母、兄、そして僕です。父の名前はヘンドラさんです。父は美しい建物を設計する建築家として働いています。父は忍耐強く、思慮深く、家族を深く愛してくれる存在です。",
             "terdiri dari（〜から成る）、bekerja sebagai（〜として働く）、sosok（人物像）。"),
            ("Ibuku bernama Ibu Rina. Ibu adalah seorang guru matematika di Sekolah Menengah Pertama. Meskipun sibuk mengajar di sekolah, ibu selalu memasak makanan yang enak untuk kami di rumah. Ibu sangat rajin, ramah, dan pintar membuat kue tradisional Sunda.",
             "母の名前はリナさんです。母は中学校の数学の教師です。学校で教えるのに忙しいにもかかわらず、母は家でいつも僕たちのために美味しい料理を作ってくれます。母はとても勤勉で、親しみやすく、スンダの伝統的なお菓子を作るのが上手です。",
             "meskipun（〜にもかかわらず）、guru matematika（数学教師）、pintar membuat（〜を作るのが上手）。"),
            ("Kakak laki-lakiku bernama Dimas. Kak Dimas berumur lima belas tahun dan sekarang duduk di bangku SMA. Kak Dimas sangat gemar bermain gitar dan berolahraga basket. Setiap akhir pekan, kami selalu berkumpul bersama di ruang keluarga untuk menonton televisi atau bernyanyi bersama. Aku sangat bersyukur memiliki keluarga yang harmonis dan penuh kasih sayang.",
             "僕の兄の名前はディマスです。ディマス兄さんは15歳で、今は高校に通っています。ディマス兄さんはギターを弾くこととバスケットボールをするのが大好きです。毎週末、僕たちはいつもリビングに集まってテレビを見たり一緒に歌ったりします。僕は調和のとれた愛情あふれる家族を持てたことを心から感謝しています。",
             "kakak laki-laki（兄 / 略して Kak）、penuh kasih sayang（愛情に満ちた）。")
        ],
        "vocab": [
            ("pegunungan", "名詞", "gunung", "山々、山岳地帯", "Kota Bandung dikelilingi pegunungan hijau."),
            ("rumah sederhana", "名詞句", "rumah", "質素な家、素朴な家", "Mereka tinggal di rumah sederhana yang bersih."),
            ("asri", "形容詞", "-", "（自然が）緑豊かで美しい、清々しい", "Lingkungan desa itu sangat asri dan sejuk."),
            ("terdiri dari", "動詞句", "diri", "〜から成る、構成される", "Keluargaku terdiri dari empat anggota."),
            ("arsitek", "名詞", "-", "建築家", "Ayah adalah arsitek yang berpengalaman."),
            ("merancang", "動詞", "rancang", "設計する、デザインする", "Arsitek bertugas merancang denah bangunan."),
            ("sabar", "形容詞", "-", "辛抱強い、寛容な", "Guru harus sabar menghadapi murid-murid."),
            ("bijaksana", "形容詞", "-", "賢明な、思慮深い", "Kakek memberikan nasihat yang sangat bijaksana."),
            ("ruang keluarga", "名詞句", "ruang", "居間、リビングルーム", "Kami mengobrol santai di ruang keluarga."),
            ("kasih sayang", "名詞句", "kasih", "愛情、いつくしみ", "Ibu merawat kami dengan penuh kasih sayang.")
        ],
        "grammar_points": """1. **構成を表す表現 `terdiri dari ...`**:
   - *Keluarga saya terdiri dari lima orang.*（私の家族は5人家族です）
   - *Buku ini terdiri dari sepuluh bab.*（この本は10章から成ります）
2. **職業を表す前置詞 `bekerja sebagai ...`**:
   - *bekerja sebagai guru*（教師として働く）
   - *bekerja sebagai dokter*（医師として働く）
   - *bekerja sebagai arsitek*（建築家として働く）
3. **兄・姉・弟・妹の親称体系**:
   - *kakak laki-laki*（兄）
   - *kakak perempuan*（姉）
   - *adik laki-laki*（弟）
   - *adik perempuan*（妹）
   - 日常の呼びかけでは親しみを込めて *Kak*（兄・姉）や *Dik*（弟・妹）と呼びます。""",
        "quizzes": [
            ("ブディ君のお父さん（Pak Hendra）の職業は何ですか？",
             ["高校の数学の先生", "建物を設計する建築家（arsitek）", "伝統市場の商人"],
             "建物を設計する建築家（arsitek）",
             "第2段落に「Ayah bekerja sebagai seorang arsitek yang merancang gedung-gedung indah.」とあります。"),
            ("ブディ君のお母さんは中学校で何の科目を教えていますか？",
             ["英語（Bahasa Inggris）", "数学（matematika）", "歴史（sejarah）"],
             "数学（matematika）",
             "第3段落に「Ibu adalah seorang guru matematika di Sekolah Menengah Pertama.」とあります。"),
            ("ブディ君の兄（Dimas）の趣味は何ですか？",
             ["ギターを弾くこととバスケットボールをすること", "テレビゲームと漫画を読むこと", "料理を作ること"],
             "ギターを弾くこととバスケットボールをすること",
             "第4段落に「Kak Dimas sangat gemar bermain gitar dan berolahraga basket.」とあります。")
        ],
        "culture": """### バンドン（Kota Bandung）とスンダ文化の温もり
西ジャワ州の州都バンドン（Bandung）は、標高約700メートル以上の高地に位置し、年間を通じて冷涼な気候からオランダ植民地時代には「ジャワのパリ（Parijs van Java）」と称されました。
先住民族であるスンダ族（Suku Sunda）は、非常に穏やかで礼儀正しく、ユーモアを好む気質で知られています。家族の絆（Keluarga）を極めて大切にし、親戚一同が集まる週末の団らんはインドネシア全土で最も尊ばれる文化的な時間です。"""
    }
]

# Write a loop for the remaining 5 stories in the batch (1206-1210) to make all 10 stories complete
more_stories = [
    {
        "id": "1206",
        "slug": "level-1-06-cat-pet-story",
        "title": "【Level 1 (A1)】Kucingku Si Belang（我が家の愛猫ブランのお散歩）",
        "desc": "ペットの三毛猫「ブラン」の可愛い日常。動物に関する語彙や、感情・日常の動きを表現するA1ストーリー。",
        "text": """Aku memiliki seekor kucing peliharaan yang sangat lucu. Namanya adalah Si Belang. Dinamakan Si Belang karena bulunya memiliki tiga warna yang indah, yaitu putih, oranye, dan hitam. Matanya bulat bersinar dan ekornya sangat panjang.

Setiap pagi, Si Belang selalu membangunkanku dengan suara mengeong yang lembut. Dia suka menggesekkan badannya ke kakiku untuk meminta makan. Makanan kesukaan Si Belang adalah ikan tongkol rebus. Saat aku meletakkan mangkuk makanannya, dia makan dengan sangat lahap hingga mangkuknya bersih.

Pada siang hari yang hangat, Si Belang suka tidur siang di atas sofa empuk di ruang tamu. Kadang-kadang, dia berjalan-jalan di halaman rumah untuk mengejar kupu-kupu yang beterbangan di antara bunga-bunga. Gerakannya sangat lincah dan menggemaskan.

Saat aku pulang dari sekolah, Si Belang selalu menunggu di dekat pintu pagar. Dia menyambutku dengan gembira sambil melompat kecil. Memiliki Si Belang membuat hari-hariku di rumah selalu ceria dan penuh tawa.""",
        "paragraphs": [
            ("Aku memiliki seekor kucing peliharaan yang sangat lucu. Namanya adalah Si Belang. Dinamakan Si Belang karena bulunya memiliki tiga warna yang indah, yaitu putih, oranye, dan hitam. Matanya bulat bersinar dan ekornya sangat panjang.",
             "僕はとても可愛いペットの猫を1匹飼っています。名前はブランです。白、オレンジ、黒の3つの美しい色の毛を持っていることから、シ・ブラン（まだらちゃん）と名付けられました。目は丸くて輝いており、尻尾はとても長いです。",
             "助数詞 seekor（動物1匹）や、色の名前（putih, oranye, hitam）。"),
            ("Setiap pagi, Si Belang selalu membangunkanku dengan suara mengeong yang lembut. Dia suka menggesekkan badannya ke kakiku untuk meminta makan. Makanan kesukaan Si Belang adalah ikan tongkol rebus. Saat aku meletakkan mangkuk makanannya, dia makan dengan sangat lahap hingga mangkuknya bersih.",
             "毎朝、ブランは優しい鳴き声で僕を起こしてくれます。ご飯をねだるために、僕の足に体をすり寄せてきます。ブランの大好物は茹でたカツオです。僕がご飯のお皿を置くと、お皿がピカピカになるまでとても美味しそうにモリモリ食べます。",
             "mengeong（ニャーと鳴く）、makan dengan lahap（ガツガツ美味しそうに食べる）。"),
            ("Pada siang hari yang hangat, Si Belang suka tidur siang di atas sofa empuk di ruang tamu. Kadang-kadang, dia berjalan-jalan di halaman rumah untuk mengejar kupu-kupu yang beterbangan di antara bunga-bunga. Gerakannya sangat lincah dan menggemaskan.",
             "暖かい昼下がり、ブランはリビングのふかふかのソファの上で昼寝をするのが好きです。時々、花々の間を飛び交う蝶々を追いかけるために、家の庭を散歩します。その動きはとても敏捷で可愛らしいです。",
             "sofa empuk（ふかふかのソファ）、mengejar（追いかける）、lincah（敏捷な）、menggemaskan（愛くるしい）。"),
            ("Saat aku pulang dari sekolah, Si Belang selalu menunggu di dekat pintu pagar. Dia menyambutku dengan gembira sambil melompat kecil. Memiliki Si Belang membuat hari-hariku di rumah selalu ceria dan penuh tawa.",
             "僕が学校から帰る時、ブランはいつも門の近くで待っています。小さく飛び跳ねながら、嬉しそうに僕を出迎えてくれます。ブランがいることで、僕の家での毎日はいつも明るく笑顔に満ちています。",
             "pintu pagar（門扉）、menyambut（出迎える）、ceria（陽気な・明るい）。")
        ],
        "vocab": [
            ("seekor kucing", "助数詞句", "ekor", "猫1匹", "Ada seekor kucing tidur di teras."),
            ("hewan peliharaan", "名詞句", "pelihara", "ペット、飼育動物", "Kucing adalah hewan peliharaan populer."),
            ("bulu", "名詞", "-", "体毛、毛並み、羽", "Bulu kucing itu sangat halus."),
            ("mengeong", "動詞", "meong", "ニャーと鳴く", "Anak kucing mengeong mencari induknya."),
            ("lahap", "副詞/形容詞", "-", "ガツガツと、美味しそうに", "Anak itu makan dengan sangat lahap."),
            ("sofa empuk", "名詞句", "empuk", "ふかふかのソファ", "Kakek duduk santai di sofa empuk."),
            ("mengejar", "動詞", "kejar", "追いかける", "Kucing suka mengejar tikus dan burung."),
            ("kupu-kupu", "名詞", "-", "蝶々（昆虫）", "Banyak kupu-kupu hinggap di bunga taman."),
            ("lincah", "形容詞", "-", "身のこなしが軽い、敏捷な", "Gerakan penari itu sangat lincah."),
            ("menggemaskan", "形容詞", "gemas", "愛くるしい、抱きしめたくなる", "Tingkah laku bayi itu sangat menggemaskan.")
        ],
        "grammar_points": """1. **動物を数える助数詞 `ekor`（〜匹・〜頭）**:
   - インドネシア語で動物を数える際は *ekor*（尾）を使います。
   - *seekor kucing*（1匹の猫）
   - *dua ekor burung*（2羽の鳥）
   - *lima ekor sapi*（5頭の牛）
2. **人物やペットの名前に付ける親称冠詞 `Si`**:
   - 親しみやすさや愛嬌を込めて名前に付けます。
   - *Si Belang*（まだらちゃん）
   - *Si Kancil*（マメジカ君・民話の主人公）
3. **継続・習慣を表す副詞 `selalu`, `sering`, `kadang-kadang`**:
   - *selalu*（いつも・100%）
   - *sering*（よく・頻繁に・70%）
   - *kadang-kadang*（時々・たまに・30%）""",
        "quizzes": [
            ("ブディ君の飼い猫の名前「Si Belang」の由来は何ですか？",
             ["体がとても大きくて力強いから", "毛に白・オレンジ・黒の3色の斑（まだら）模様があるから", "足がとても速いから"],
             "毛に白・オレンジ・黒の3色の斑（まだら）模様があるから",
             "第1段落に「Dinamakan Si Belang karena bulunya memiliki tiga warna yang indah...」とあります。"),
            ("シ・ブランの大好物のご飯は何ですか？",
             ["茹でたカツオ（ikan tongkol rebus）", "鶏肉のソーセージ", "乾燥したキャットフード"],
             "茹でたカツオ（ikan tongkol rebus）",
             "第2段落に「Makanan kesukaan Si Belang adalah ikan tongkol rebus.」と明記されています。"),
            ("シ・ブランが昼間に庭に出て追いかけるのが好きな生き物は何ですか？",
             ["トカゲ", "蝶々（kupu-kupu）", "ネズミ"],
             "蝶々（kupu-kupu）",
             "第3段落に「...mengejar kupu-kupu yang beterbangan di antara bunga-bunga.」とあります。")
        ],
        "culture": """### インドネシア人と猫（Kucing）の特別な絆
インドネシアでは、猫（Kucing）は最も親しまれている動物です。人口の約87%を占めるイスラム教において、預言者ムハンマドが「ムエザ（Muezza）」という愛猫を深く可愛がったという伝承があるため、猫を慈しみ大切に扱う文化が社会全体に根付いています。
街角のワルン（屋台）や住宅街の軒先には、人懐っこい地域猫がたくさんおり、人々が余った魚やご飯を分け与える心温まる風景が日常的に見られます。"""
    },
    {
        "id": "1207",
        "slug": "level-1-07-weekend-park",
        "title": "【Level 1 (A1)】Hari Minggu di Taman Kota（日曜日の緑あふれる公園でピクニック）",
        "desc": "週末の市民公園での家族ピクニック。自転車乗り、遊具、自然観察、ピクニックの持ち物を描くA1ストーリー。",
        "text": """Hari Minggu adalah hari yang paling ditunggu-tunggu oleh seluruh anggota keluarga. Pada hari libur ini, ayah dan ibu mengajak kami berekreasi ke Taman Kota Bandung. Taman kota itu sangat luas, bersih, dan dipenuhi oleh pepohonan rindang.

Kami tiba di taman pada jam delapan pagi. Udara masih terasa sejuk dan matahari bersinar cerah. Ayah menggelar tikar piknik di bawah pohon beringin yang besar. Ibu mengeluarkan bekal makanan dari keranjang, seperti roti isi, buah potong, dan jus jeruk dingin.

Aku dan Kak Dimas menyewa sepeda tandem untuk berkeliling taman. Kami mengayuh sepeda bersama sambil tertawa gembira. Di sepanjang jalan taman, kami melihat banyak keluarga yang sedang bermain layang-layang, berolahraga lari pagi, atau sekadar duduk santai membaca buku.

Setelah lelah bersepeda, kami kembali ke tikar piknik untuk menikmati bekal bersama. Makanan terasa jauh lebih lezat saat disantap di alam terbuka. Sebelum pulang, ayah membelikan kami es krim cokelat. Hari Minggu di taman kota adalah momen indah yang selalu membuat kami bahagia.""",
        "paragraphs": [
            ("Hari Minggu adalah hari yang paling ditunggu-tunggu oleh seluruh anggota keluarga. Pada hari libur ini, ayah dan ibu mengajak kami berekreasi ke Taman Kota Bandung. Taman kota itu sangat luas, bersih, dan dipenuhi oleh pepohonan rindang.",
             "日曜日はいちばん家族全員が心待ちにしている日です。この休日に、お父さんとお母さんは僕たちを連れてバンドン市立公園へレクリエーションに出かけました。その市民公園はとても広くて清潔で、緑豊かな木々で満ちています。",
             "paling ditunggu-tunggu（最も待望の）、pepohonan rindang（木陰を作る生い茂った木々）。"),
            ("Kami tiba di taman pada jam delapan pagi. Udara masih terasa sejuk dan matahari bersinar cerah. Ayah menggelar tikar piknik di bawah pohon beringin yang besar. Ibu mengeluarkan bekal makanan dari keranjang, seperti roti isi, buah potong, dan jus jeruk dingin.",
             "僕たちは朝の8時に公園に到着しました。空気はまだ涼しく、太陽は明るく輝いています。お父さんは大きなガジュマルの木の下にピクニック用のゴザを敷きました。お母さんはかごからサンドイッチ、カットフルーツ、冷たいオレンジジュースといったお弁当を取り出しました。",
             "menggelar tikar（ゴザ・シートを敷く）、bekal makanan（持参したお弁当）。"),
            ("Aku dan Kak Dimas menyewa sepeda tandem untuk berkeliling taman. Kami mengayuh sepeda bersama sambil tertawa gembira. Di sepanjang jalan taman, kami melihat banyak keluarga yang sedang bermain layang-layang, berolahraga lari pagi, atau sekadar duduk santai membaca buku.",
             "僕とディマス兄さんは公園を一周するためにタンデム自転車（2人乗り自転車）を借りました。僕たちは楽しそうに笑いながら一緒にペダルを漕ぎました。公園の道沿いには、凧揚げをしたり、朝のジョギングをしたり、あるいは単にのんびり座って本を読んだりしているたくさんの家族が見えました。",
             "sepeda tandem（2人乗り自転車）、bermain layang-layang（凧揚げをする）。"),
            ("Setelah lelah bersepeda, kami kembali ke tikar piknik untuk menikmati bekal bersama. Makanan terasa jauh lebih lezat saat disantap di alam terbuka. Sebelum pulang, ayah membelikan kami es krim cokelat. Hari Minggu di taman kota adalah momen indah yang selalu membuat kami bahagia.",
             "自転車に疲れた後、僕たちはピクニックシートに戻って一緒にお弁当を楽しみました。屋外で食べる食事はずっと美味しく感じられます。帰る前に、お父さんは僕たちにチョコレートアイスクリームを買ってくれました。市民公園での日曜日は、僕たちをいつも幸せにしてくれる素敵なひとときです。",
             "disantap（平らげられる・召し上がられる）、alam terbuka（大自然・屋外）。")
        ],
        "vocab": [
            ("hari libur", "名詞句", "libur", "休日、祝日", "Hari Minggu adalah hari libur sekolah."),
            ("taman kota", "名詞句", "taman", "市民公園、都市公園", "Taman kota menjadi tempat rekreasi murah."),
            ("pohon rindang", "名詞句", "rindang", "生い茂った木陰の木", "Kami berteduh di bawah pohon rindang."),
            ("tikar piknik", "名詞句", "tikar", "ピクニック用のゴザ・敷物", "Ibu menggelar tikar di atas rumput hijau."),
            ("bekal", "名詞", "-", "弁当、持参の食料", "Adik membawa bekal nasi goreng ke sekolah."),
            ("sepeda tandem", "名詞句", "sepeda", "タンデム自転車（2人乗り自転車）", "Kami menyewa sepeda tandem di taman."),
            ("mengayuh", "動詞", "kayuh", "（自転車のペダルを）漕ぐ", "Anak itu mengayuh sepedanya dengan cepat."),
            ("layang-layang", "名詞", "-", "凧（たこ）", "Anak-anak bermain layang-layang di lapangan luas."),
            ("alam terbuka", "名詞句", "alam", "自然の中、屋外、アウトドア", "Berpiknik di alam terbuka sangat menyenangkan."),
            ("es krim", "名詞", "-", "アイスクリーム", "Ayah membelikan es krim rasa cokelat.")
        ],
        "grammar_points": """1. **接頭辞 `ber-` を持つ乗り物・スポーツ動詞**:
   - *bersepeda*（自転車に乗る）
   - *berolahraga*（スポーツをする）
   - *berekreasi*（レクリエーションする）
2. **畳語による「生い茂る・たくさんの」意味派生**:
   - *pohon*（木）→ *pepohonan*（木々・木立）
   - *daun*（葉）→ *dedaunan*（葉っぱの茂み）
3. **比較級の強調 `jauh lebih ...`（はるかに〜）**:
   - *jauh lebih lezat*（はるかに美味しい）
   - *jauh lebih besar*（はるかに大きい）
   - *jauh lebih murah*（はるかに安い）""",
        "quizzes": [
            ("ブディ君一家がバンドン市民公園に到着したのは何時ですか？",
             ["朝の6時", "朝の8時（jam delapan pagi）", "昼の12時"],
             "朝の8時（jam delapan pagi）",
             "第2段落に「Kami tiba di taman pada jam delapan pagi.」とあります。"),
            ("ブディ君とお兄ちゃん（Dimas）が公園を一周するために借りた乗り物は何ですか？",
             ["スクーター", "タンデム自転車（sepeda tandem: 2人乗り自転車）", "足漕ぎボート"],
             "タンデム自転車（sepeda tandem: 2人乗り自転車）",
             "第3段落に「Aku dan Kak Dimas menyewa sepeda tandem untuk berkeliling taman.」とあります。"),
            ("公園から帰る直前に、お父さんが子供たちに買ってくれたおやつは何ですか？",
             ["チョコレートアイスクリーム（es krim cokelat）", "焼きトウモロコシ", "綿菓子"],
             "チョコレートアイスクリーム（es krim cokelat）",
             "第4段落に「Sebelum pulang, ayah membelikan kami es krim cokelat.」と明記されています。")
        ],
        "culture": """### インドネシアの市民公園と「Tikar（ゴザ）」の文化
インドネシアの大都市（ジャカルタ、バンドン、スラバヤなど）では、近年、市民の憩いの場として美しく整備された「Taman Kota（市民公園）」や、日曜朝の「Car Free Day（歩行者天国）」が大人気です。
公園に行くと、芝生の上に「Tikar（伝統的な編みゴザやレジャーシート）」を敷いて、家族連れや若者たちが何時間ものんびりと語り合います。敷物を持参していなくても、公園内には「Sewa tikar（ゴザの貸し出し）」を行う露天商がいて、数千ルピアで手軽にピクニックを楽しむことができます。"""
    },
    {
        "id": "1208",
        "slug": "level-1-08-lost-umbrella",
        "title": "【Level 1 (A1)】Payung Merah yang Hilang（雨の日に置き忘れた赤い傘を探して）",
        "desc": "雨の日の図書館での出来事と、忘れ物を探す心温まるストーリー。位置関係を表す前置詞（上、下、中、近く）を習得する。",
        "text": """Kemarin sore, langit di atas kota mendung sangat gelap. Angin kencang mulai berhembus, dan tidak lama kemudian hujan turun dengan sangat lebat. Aku membawa payung merah kesayanganku saat pergi ke perpustakaan daerah untuk membaca buku.

Perpustakaan itu sangat tenang dan nyaman. Aku membaca beberapa buku cerita bergambar yang sangat menarik. Tanpa terasa, dua jam telah berlalu. Ketika aku melihat ke luar jendela, hujan sudah mulai reda. Aku segera mengembalikan buku ke rak buku dan bersiap untuk pulang ke rumah.

Namun, ketika aku tiba di pintu depan perpustakaan, aku terkejut. Payung merahku tidak ada di tempat payung! Aku merasa cemas dan panik. Aku mencari di bawah meja baca, di dekat rak buku, dan di sudut ruangan, tetapi payung itu tetap tidak ditemukan.

Aku kemudian memberanikan diri bertanya kepada petugas perpustakaan bernama Ibu Dewi. Sambil tersenyum ramah, Ibu Dewi berkata, "Apakah ini payung merahmu, Nak? Tadi ada pengunjung yang menyerahkannya ke meja informasi karena tertinggal." Aku merasa sangat lega dan bahagia. Aku mengucapkan terima kasih banyak kepada Ibu Dewi sebelum berjalan pulang di bawah udara sore yang sejuk.""",
        "paragraphs": [
            ("Kemarin sore, langit di atas kota mendung sangat gelap. Angin kencang mulai berhembus, dan tidak lama kemudian hujan turun dengan sangat lebat. Aku membawa payung merah kesayanganku saat pergi ke perpustakaan daerah untuk membaca buku.",
             "昨日の夕方、街の上の空は暗く曇っていました。強い風が吹き始め、まもなく雨が激しく降り出しました。僕は本を読むために地域の図書館へ行く際、お気に入りの赤い傘を持っていきました。",
             "mendung（曇り）、hujan lebat（大雨・土砂降り）、payung kesayangan（お気に入りの傘）。"),
            ("Perpustakaan itu sangat tenang dan nyaman. Aku membaca beberapa buku cerita bergambar yang sangat menarik. Tanpa terasa, dua jam telah berlalu. Ketika aku melihat ke luar jendela, hujan sudah mulai reda. Aku segera mengembalikan buku ke rak buku dan bersiap untuk pulang ke rumah.",
             "その図書館はとても静かで快適でした。僕はとても面白い絵本の物語を何冊か読みました。気づかないうちに、2時間が過ぎ去っていました。窓の外を見ると、雨はすでに小降りになり始めていました。僕はすぐに本を書棚に戻し、家へ帰る準備をしました。",
             "tanpa terasa（知らぬ間に・あっという間に）、hujan reda（雨が止む・小降りになる）。"),
            ("Namun, ketika aku tiba di pintu depan perpustakaan, aku terkejut. Payung merahku tidak ada di tempat payung! Aku merasa cemas dan panik. Aku mencari di bawah meja baca, di dekat rak buku, dan di sudut ruangan, tetapi payung itu tetap tidak ditemukan.",
             "しかし、図書館の玄関に到着した時、僕は驚きました。僕の赤い傘が傘立てになかったのです！僕は不安でパニックになりました。僕は読書机の下、本棚の近く、そして部屋の隅を探しましたが、傘はどうしても見つかりませんでした。",
             "位置の前置詞：di bawah meja（机の下）、di dekat rak（棚の近く）、di sudut（隅に）。"),
            ("Aku kemudian memberanikan diri bertanya kepada petugas perpustakaan bernama Ibu Dewi. Sambil tersenyum ramah, Ibu Dewi berkata, \"Apakah ini payung merahmu, Nak? Tadi ada pengunjung yang menyerahkannya ke meja informasi karena tertinggal.\" Aku merasa sangat lega dan bahagia. Aku mengucapkan terima kasih banyak kepada Ibu Dewi sebelum berjalan pulang di bawah udara sore yang sejuk.",
             "僕はそれから勇気を出して、デウィさんという名前の図書館員に尋ねました。優しく微笑みながら、デウィさんは言いました。「これはあなたの赤い傘かい、坊や？さっき置き忘れてあったからと、案内カウンターに届けてくれた利用者がいたのよ」。僕はとても安心し、嬉しくなりました。僕はデウィさんに心からお礼を言って、涼しい夕方の空気の中を歩いて帰りました。",
             "memberanikan diri（勇気を出す）、lega（ほっと安心した）、menyerahkan（手渡す・届ける）。")
        ],
        "vocab": [
            ("hujan lebat", "名詞句", "hujan", "激しい雨、大雨、豪雨", "Hujan lebat disertai angin kencang."),
            ("payung", "名詞", "-", "傘", "Bawalah payung sebelum hujan turun."),
            ("perpustakaan", "名詞", "pustaka", "図書館", "Murid-murid membaca buku di perpustakaan."),
            ("reda", "形容詞/動詞", "-", "（雨や嵐が）小降りになる、収まる", "Kita jalan setelah hujan mulai reda."),
            ("rak buku", "名詞句", "rak", "本棚、書棚", "Buku disusun rapi di rak buku."),
            ("cemas", "形容詞", "-", "不安な、心配な", "Ibu merasa cemas saat adik belum pulang."),
            ("di sudut", "前置詞句", "sudut", "〜の隅に、コーナーに", "Ada tempat sampah di sudut ruangan."),
            ("petugas", "名詞", "tugas", "係員、職員、担当者", "Petugas perpustakaan melayani dengan ramah."),
            ("tertinggal", "動詞", "tinggal", "置き忘れた、取り残された", "Dompetnya tertinggal di atas meja kasir."),
            ("merasa lega", "動詞句", "lega", "ほっと安心する、胸をなでおろす", "Saya merasa lega setelah ujian selesai.")
        ],
        "grammar_points": """1. **位置・空間を表す前置詞表現**:
   - *di atas meja*（机の上に）
   - *di bawah meja*（机の下に）
   - *di dalam ruangan*（部屋の中に）
   - *di luar jendela*（窓の外に）
   - *di dekat pintu*（ドアの近くに）
   - *di sudut ruangan*（部屋の隅に）
2. **偶発・無意志を表す接頭辞 `ter-`**:
   - *terkejut*（びっくりする・驚かされる）
   - *tertinggal*（うっかり置き忘れる）
   - *ditemukan*（見つかる / *tidak ditemukan* 見つからない）
3. **成句表現 `tanpa terasa`（いつの間にか）**:
   - 時間の経過が非常に早かったことを表す定型表現。
   - *Tanpa terasa, hari sudah sore.*（いつの間にか、もう夕方になっていた）""",
        "quizzes": [
            ("ブディ君が図書館に行った日の夕方の天気はどうでしたか？",
             ["青空が広がる快晴だった", "暗い雲が立ち込め、激しい雨（hujan lebat）が降った", "雪が降っていた"],
             "暗い雲が立ち込め、激しい雨（hujan lebat）が降った",
             "第1段落に「...langit di atas kota mendung sangat gelap... hujan turun dengan sangat lebat.」とあります。"),
            ("傘が見当たらずパニックになったブディ君が探した場所に含まれないものはどれですか？",
             ["読書机の下（di bawah meja baca）", "本棚の近く（di dekat rak buku）", "トイレの中（di dalam toilet）"],
             "トイレの中（di dalam toilet）",
             "第3段落で探した場所は「di bawah meja baca, di dekat rak buku, dan di sudut ruangan」であり、トイレは探していません。"),
            ("ブディ君の赤い傘はどこにありましたか？",
             ["図書館の案内カウンター（他の利用者が届けてくれていた）", "泥棒に盗まれていた", "最初から家に置いてあった"],
             "図書館の案内カウンター（他の利用者が届けてくれていた）",
             "第4段落に「Tadi ada pengunjung yang menyerahkannya ke meja informasi karena tertinggal.」とあります。")
        ],
        "culture": """### インドネシアの雨季（Musim Hujan）と助け合いの精神
熱帯気候のインドネシアには、雨季（10月〜4月頃）と乾季（5月〜9月頃）の2つの季節があります。雨季には突然バケツをひっくり返したような豪雨（スコール / Hujan Lebat）が降るため、「Sedia payung sebelum hujan（雨が降る前に傘を用意せよ＝転ばぬ先の杖）」という有名なことわざがあります。
また、忘れ物を案内所に届けてくれた利用者のように、インドネシア社会には「Gotong Royong（相互扶助・助け合い）」と他者への思いやり（Tolong-menolong）の精神が深く根付いています。"""
    },
    {
        "id": "1209",
        "slug": "level-1-09-visiting-grandparents",
        "title": "【Level 1 (A1)】Berkunjung ke Rumah Kakek di Desa（村のおじいちゃんの家を訪ねて）",
        "desc": "田舎の村（Desa）を訪れる体験記。広大な田園（Sawah）、清らかな川、果物狩りを通じて、自然描写と移動の表現を学ぶ。",
        "text": """Saat liburan sekolah tiba, keluargaku pergi berkunjung ke rumah kakek dan nenek di sebuah desa kecil dekat kota Garut. Kami berangkat dari kota Bandung dengan mengendarai mobil pada pagi hari. Perjalanan memakan waktu sekitar dua jam.

Sepanjang perjalanan, pemandangan alam terlihat sangat indah mempesona. Kami melihat hamparan sawah hijau yang bertingkat-tingkat dan pegunungan tinggi yang diselimuti kabut putih tipis. Udara di desa kakek terasa sangat bersih, sejuk, dan bebas dari polusi kendaraan.

Kakek dan nenek menyambut kedatangan kami di halaman rumah dengan senyum bahagia dan pelukan hangat. Rumah kakek adalah rumah panggung kayu tradisional khas Sunda. Di belakang rumah kakek, terbentang kebun buah yang sangat luas dengan pohon rambutan, mangga, dan durian.

Keesokan paginya, kakek mengajakku berjalan-jalan ke sawah. Aku melihat para petani sedang membajak sawah bersama kerbau mereka. Di dekat sawah, ada sungai kecil dengan air yang jernih dan mengalir tenang. Aku bermain air bersama anak-anak desa dengan penuh kegembiraan. Mengunjungi desa kakek selalu menjadi pengalaman liburan yang paling berkesan bagiku.""",
        "paragraphs": [
            ("Saat liburan sekolah tiba, keluargaku pergi berkunjung ke rumah kakek dan nenek di sebuah desa kecil dekat kota Garut. Kami berangkat dari kota Bandung dengan mengendarai mobil pada pagi hari. Perjalanan memakan waktu sekitar dua jam.",
             "学校の休みがやって来た時、僕の家族はガルット市の近くの小さな村にあるおじいちゃんとおばあちゃんの家を訪ねに行きました。僕たちは朝、バンドン市から車を運転して出発しました。所要時間は約2時間でした。",
             "berkunjung ke（〜を訪れる）、mengendarai mobil（車を運転する）、memakan waktu（時間を要する）。"),
            ("Sepanjang perjalanan, pemandangan alam terlihat sangat indah mempesona. Kami melihat hamparan sawah hijau yang bertingkat-tingkat dan pegunungan tinggi yang diselimuti kabut putih tipis. Udara di desa kakek terasa sangat bersih, sejuk, dan bebas dari polusi kendaraan.",
             "道中ずっと、自然の風景は息をのむほど美しく見えました。僕たちは一面に広がる緑の段々畑（棚田）と、薄い白い霧に覆われた高い山々を見ました。おじいちゃんの村の空気はとても澄んでいて涼しく、車の排気ガス汚染がありません。",
             "sawah bertingkat-tingkat（段々畑・棚田）、diselimuti kabut（霧に包まれた）、bebas dari polusi（公害のない）。"),
            ("Kakek dan nenek menyambut kedatangan kami di halaman rumah dengan senyum bahagia dan pelukan hangat. Rumah kakek adalah rumah panggung kayu tradisional khas Sunda. Di belakang rumah kakek, terbentang kebun buah yang sangat luas dengan pohon rambutan, mangga, dan durian.",
             "おじいちゃんとおばあちゃんは、幸せな笑顔と温かい抱擁で庭で僕たちの到着を出迎えてくれました。おじいちゃんの家は伝統的なスンダ特有の高床式の木造家屋です。おじいちゃんの家の裏には、ランブータン、マンゴー、ドリアンの木があるとても広い果樹園が広がっています。",
             "rumah panggung（高床式家屋）、pelukan hangat（温かいハグ）、kebun buah（果樹園）。"),
            ("Keesokan paginya, kakek mengajakku berjalan-jalan ke sawah. Aku melihat para petani sedang membajak sawah bersama kerbau mereka. Di dekat sawah, ada sungai kecil dengan air yang jernih dan mengalir tenang. Aku bermain air bersama anak-anak desa dengan penuh kegembiraan. Mengunjungi desa kakek selalu menjadi pengalaman liburan yang paling berkesan bagiku.",
             "翌朝、おじいちゃんは僕を連れて田んぼへ散歩に行きました。僕は農民たちが水牛と一緒に田んぼを耕しているのを見ました。田んぼの近くには、澄んだ水が穏やかに流れる小川がありました。僕は村の子供たちと一緒に喜びにあふれて水遊びをしました。おじいちゃんの村を訪ねることは、僕にとっていつも一番心に残る休日の体験です。",
             "membajak sawah（田んぼを耕す）、kerbau（水牛）、paling berkesan（最も印象深い・思い出に残る）。")
        ],
        "vocab": [
            ("liburan sekolah", "名詞句", "libur", "学校の長期休み、休暇", "Murid-murid senang saat liburan sekolah tiba."),
            ("berkunjung", "動詞", "kunjung", "訪問する、訪ねる", "Kami berkunjung ke rumah kerabat di desa."),
            ("sawah", "名詞", "-", "水田、田んぼ", "Padi menguning siap dipanen di sawah."),
            ("diselimuti kabut", "動詞句", "selimut", "霧に覆われた、包まれた", "Puncak gunung diselimuti kabut tebal pagi ini."),
            ("rumah panggung", "名詞句", "panggung", "高床式家屋", "Rumah panggung aman dari banjir dan binatang."),
            ("kebun buah", "名詞句", "kebun", "果樹園、果物畑", "Kakek memetik mangga manis di kebun buah."),
            ("membajak", "動詞", "bajak", "（畑・田んぼを）耕す", "Petani membajak sawah sebelum menanam padi."),
            ("kerbau", "名詞", "-", "水牛", "Kerbau membantu petani membajak lumpur."),
            ("air jernih", "名詞句", "jernih", "清らかな水、透明な水", "Sungai pegunungan memiliki air jernih dan dingin."),
            ("berkesan", "動詞/形容詞", "kesan", "印象深い、心に残る", "Liburan ke Bali sangat berkesan bagi saya.")
        ],
        "grammar_points": """1. **時の表現 `saat ... tiba`（〜がやって来た時）**:
   - *Saat liburan tiba*（休暇がやって来た時）
   - *Saat hari raya tiba*（祝日がやって来た時）
2. **交通手段を表す `dengan mengendarai ...`（〜を運転して）**:
   - *dengan mengendarai mobil*（車を運転して）
   - *dengan mengendarai sepeda motor*（バイクを運転して）
   - 公共交通機関の場合は *naik bus*（バスに乗って）や *naik kereta*（列車に乗って）。
3. **最上級の感情表現 `paling berkesan`（最も心に残る）**:
   - *pengalaman yang paling berkesan*（最も印象的な経験）
   - *kenangan yang paling indah*（一番美しい思い出）""",
        "quizzes": [
            ("おじいちゃんとおばあちゃんが住んでいる村は、どの都市の近くにありますか？",
             ["ジャカルタ市（Jakarta）", "ガルット市（Garut）", "スラバヤ市（Surabaya）"],
             "ガルット市（Garut）",
             "第1段落に「...di sebuah desa kecil dekat kota Garut.」と明記されています。"),
            ("おじいちゃんの家の裏にある果樹園に植えられている果物に含まれないものはどれですか？",
             ["ランブータン（rambutan）", "マンゴー（mangga）", "リンゴ（apel）"],
             "リンゴ（apel）",
             "第3段落に「...pohon rambutan, mangga, dan durian.」とあり、温帯性のリンゴは植えられていません。"),
            ("田んぼで農民たちと一緒に田を耕していた動物は何ですか？",
             ["馬（kuda）", "水牛（kerbau）", "象（gajah）"],
             "水牛（kerbau）",
             "第4段落に「...para petani sedang membajak sawah bersama kerbau mereka.」とあります。")
        ],
        "culture": """### インドネシアの「Mudik（里帰り）」と農村（Desa）の原風景
インドネシアでは、大都市に住む人々が長期休暇（特にレバラン断食明け大祭）に一斉に故郷の村へ帰省する「Mudik（ムディック）」という巨大な文化的移動現象があります。
大都市の渋滞や喧騒を離れ、緑豊かな棚田（Sawah Bertingkat）、親切な村人たち、そして澄んだ小川が流れる農村（Desa）の風景は、すべてのインドネシア人の心の故郷（Kampung Halaman）として大切にされています。"""
    },
    {
        "id": "1210",
        "slug": "level-1-10-level1-review-quiz",
        "title": "【Level 1 (A1) 総括】Cerita Liburan Seru & 総合読解力診断テスト",
        "desc": "Level 1（A1入門編）の集大成。まとめストーリー「楽しい休日の思い出」の読解と、基礎語彙・文法・読解力を完全測定する総合診断テスト。",
        "text": """Namaku Budi. Minggu lalu adalah hari libur yang paling menyenangkan bagiku. Pagi-pagi sekali pada jam lima, aku sudah bangun tidur dan mandi dengan air yang segar. Ibu membuatkan sarapan nasi goreng telur yang lezat.

Setelah sarapan, aku, ayah, ibu, dan Kak Dimas pergi ke taman kota. Di sana, udaranya sangat sejuk karena banyak pepohonan rindang. Kak Dimas dan aku menyewa sepeda untuk berkeliling taman. Kami melihat banyak orang sedang berolahraga dan bermain layang-layang. Kami juga duduk santai di atas tikar sambil makan buah pisang dan pepaya yang dibeli dari pasar tradisional.

Siang harinya, kami mampir ke sebuah warung tenda untuk makan sate ayam dengan saus kacang yang gurih. Saat hujan mulai turun lebat, kami berteduh dengan tenang di dalam mobil. Sore harinya, ketika kami tiba di rumah, kucingku Si Belang sudah menunggu di depan pintu pagar sambil mengeong gembira.

Aku merasa sangat bersyukur memiliki keluarga yang hangat dan teman-teman yang baik hati. Belajar bahasa Indonesia membuatku bisa menceritakan semua kebahagiaan ini kepada dunia.""",
        "paragraphs": [
            ("Namaku Budi. Minggu lalu adalah hari libur yang paling menyenangkan bagiku. Pagi-pagi sekali pada jam lima, aku sudah bangun tidur dan mandi dengan air yang segar. Ibu membuatkan sarapan nasi goreng telur yang lezat.",
             "僕の名前はブディです。先週は僕にとって最も楽しい休日でした。朝早くの5時に、僕はすでに起きて爽やかな水で水浴びをしました。お母さんは美味しい卵入りナシゴレンの朝ご飯を作ってくれました。",
             "過去の時代表現 Minggu lalu（先週）と、pagi-pagi sekali（朝とても早くに）。"),
            ("Setelah sarapan, aku, ayah, ibu, dan Kak Dimas pergi ke taman kota. Di sana, udaranya sangat sejuk karena banyak pepohonan rindang. Kak Dimas dan aku menyewa sepeda untuk berkeliling taman. Kami melihat banyak orang sedang berolahraga dan bermain layang-layang. Kami juga duduk santai di atas tikar sambil makan buah pisang dan pepaya yang dibeli dari pasar tradisional.",
             "朝食の後、僕、父、母、ディマス兄さんは市民公園へ行きました。そこは緑が生い茂る木々がたくさんあるため、空気はとても涼しかったです。ディマス兄さんと僕は公園を一周するために自転車を借りました。僕たちはたくさんの人々が運動したり凧揚げをしたりしているのを見ました。僕たちはまた、伝統市場で買ったバナナとパパイヤを食べながら、ゴザの上にリラックスして座りました。",
             "Level 1 で登場した重要語彙（taman kota, sepeda, layang-layang, tikar, pasar tradisional）が総動員。"),
            ("Siang harinya, kami mampir ke sebuah warung tenda untuk makan sate ayam dengan saus kacang yang gurih. Saat hujan mulai turun lebat, kami berteduh dengan tenang di dalam mobil. Sore harinya, ketika kami tiba di rumah, kucingku Si Belang sudah menunggu di depan pintu pagar sambil mengeong gembira.",
             "昼には、僕たちはコクのあるピーナッツソースのサテ・アヤムを食べるために、ある屋台食堂に立ち寄りました。雨が激しく降り始めた時、僕たちは車の中で落ち着いて雨宿りをしました。夕方、僕たちが家に到着した時、愛猫のシ・ブランが嬉しそうにニャーと鳴きながらすでに門の前で待っていました。",
             "mampir（立ち寄る）、berteduh（雨宿りする）、Si Belang の再登場。"),
            ("Aku merasa sangat bersyukur memiliki keluarga yang hangat dan teman-teman yang baik hati. Belajar bahasa Indonesia membuatku bisa menceritakan semua kebahagiaan ini kepada dunia.",
             "僕は温かい家族と親切な友達を持てて、とてもありがたく感じています。インドネシア語を学ぶことで、僕はこれらすべての幸せを世界に向けて語ることができます。",
             "Level 1 の締めくくりに相応しい前向きな結び。")
        ],
        "vocab": [
            ("minggu lalu", "名詞句", "lalu", "先週", "Minggu lalu kami pergi berlibur ke pantai."),
            ("paling menyenangkan", "形容詞句", "senang", "最も楽しい", "Ini adalah liburan yang paling menyenangkan."),
            ("pagi-pagi sekali", "副詞句", "pagi", "朝とても早くに", "Petani berangkat ke sawah pagi-pagi sekali."),
            ("berkeliling", "動詞", "keliling", "一周する、あちこち回る", "Kami berkeliling kota naik bus wisata."),
            ("mampir", "動詞", "-", "（途中で）立ち寄る、寄り道する", "Mari kita mampir sebentar ke toko buku."),
            ("berteduh", "動詞", "teduh", "雨宿りする、木陰で休む", "Mereka berteduh di halte bus saat hujan."),
            ("baik hati", "形容詞句", "hati", "親切な、優しい", "Orang itu sangat ramah dan baik hati."),
            ("kebahagiaan", "名詞", "bahagia", "幸福、幸せ", "Keluarga adalah sumber kebahagiaan utama."),
            ("menceritakan", "動詞", "cerita", "〜を語る、物語る", "Kakek menceritakan dongeng masa lalu."),
            ("kepada dunia", "前置詞句", "dunia", "世界に向けて、世の中に", "Kita perkenalkan budaya Indonesia kepada dunia.")
        ],
        "grammar_points": """### Level 1 (CEFR A1) 文法チェックリスト完全制覇
1. **語順の絶対ルール**:
   - 主語（S）＋ 動詞（V）＋ 目的語（O）
   - 名詞 ＋ 修飾語（形容詞・所有代名詞・指示詞）: *rumah besar ini*（この大きな家）
2. **代名詞と親称体系**:
   - 一人称: *aku*（親しい）、*saya*（丁寧）
   - 二人称: *kamu*（親しい）、*Anda*（丁寧）、*Bapak/Ibu*（目上への敬称）
   - 三人称: *dia*（彼・彼女）、*mereka*（彼ら）
3. **時制・アスペクトの標識**:
   - 完了: *sudah*（すでに）
   - 未完了: *belum*（まだ）
   - 進行: *sedang*（〜している最中）
   - 未来: *akan*（〜する予定）
4. **否定詞の峻別**:
   - *bukan* ＋ 名詞句: *Bukan orang Jepang*（日本人ではない）
   - *tidak* ＋ 動詞・形容詞: *Tidak mahal*（高くない）、*Tidak makan*（食べない）""",
        "quizzes": [
            ("本文の総合ストーリーにおいて、ブディ君一家が昼食を食べた場所はどこですか？",
             ["高級ホテルのレストラン", "サテ・アヤムの屋台食堂（warung tenda）", "おじいちゃんの家の庭"],
             "サテ・アヤムの屋台食堂（warung tenda）",
             "第3段落に「Siang harinya, kami mampir ke sebuah warung tenda untuk makan sate ayam...」とあります。"),
            ("大雨が激しく降ってきた時、ブディ君一家はどこで雨宿りをしましたか？",
             ["公園の大きな木の下", "車の中（di dalam mobil）", "図書館のロビー"],
             "車の中（di dalam mobil）",
             "第3段落に「Saat hujan mulai turun lebat, kami berteduh dengan tenang di dalam mobil.」とあります。"),
            ("夕方に家へ帰り着いた時、門の前で嬉しそうに出迎えてくれたのは誰（何）ですか？",
             ["学校の友達のアンディ", "隣の家のおばあさん", "愛猫のシ・ブラン（Si Belang）"],
             "愛猫のシ・ブラン（Si Belang）",
             "第3段落末尾に「...kucingku Si Belang sudah menunggu di depan pintu pagar sambil mengeong gembira.」とあります。")
        ],
        "culture": """### CEFR A1 レベル修了おめでとうございます！
本記事をもって、セクション30の「Level 1 (CEFR A1 入門物語編)」全10記事をすべて完読しました。
A1レベルをマスターしたあなたは、身近な日常生活（朝の習慣、買い物、食事、学校の友達、家族、ペット、公園、忘れ物、田舎の村）に関する基本的な語彙と文章を、辞書なしで左から右へ語順通りに直読直解できる盤石の読解基礎力を身につけました。
次の「Level 2 (CEFR A2 初級編: 1211〜1220)」では、より豊かな文脈と語彙で描かれる本格的な冒険と発見のストーリーへステップアップします！"""
    }
]

all_stories = stories + more_stories

output_dir = "docs/graded-reading"
os.makedirs(output_dir, exist_ok=True)

for st in all_stories:
    filename = f"{st['slug']}.md"
    filepath = os.path.join(output_dir, filename)
    
    lines = []
    lines.append(f"# {st['title']}")
    lines.append("")
    lines.append(f"> [!NOTE]")
    lvl = st.get('level', 'CEFR A1（入門レベル・想定語彙数 300〜500語）')
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

print("All 10 Graded Reading Level 1 articles generated successfully.")
