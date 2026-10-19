# -*- coding: utf-8 -*-
"""
Batch generation script for Section 31: Collocations Batch 2 (Articles 1261-1270)
Directory: docs/lexicon/
"""

import os

articles = [
    {
        "filename": "docs/lexicon/11-verb-collocations-turun.md",
        "title": "【共起連語】語根 turun の必須コロケーション辞典：turun tangan / turun harga / turun minum / turun ranjang",
        "root": "turun",
        "meaning": "降りる、下がる、下落する、介入する",
        "core_concept": "「高い位置から低い位置へ物理的に移動する」基本語義から、「指導者自らが現場へ介入する」「物価や気温が低下する」「サッカー等のハーフタイムで休息に入る」「亡き配偶者の兄弟姉妹と再婚する（民俗慣習）」という、現場介入・経済変動・身体儀礼の多層的メタファーを展開します。",
        "table_rows": [
            ("turun tangan", "手を降ろす", "自ら介入する、自ら乗り出す、腕を振るう", "政治/指導力", "Presiden akhirnya turun tangan menyelesaikan sengketa lahan yang berlarut-larut."),
            ("turun harga", "価格が下がる", "値下がりする、値下げされる、デフレ傾向", "経済/商用", "Harga cabai dan bawang merah mulai turun harga menjelang panen raya."),
            ("turun minum", "飲み物に降りる", "ハーフタイムに入る、中入り休憩をとる", "スポーツ/競技", "Skor sementara masih imbang tanpa gol hingga wasit meniup peluit tanda turun minum."),
            ("turun ranjang", "寝台に降りる", "妻の死後にその姉妹と再婚する（義妹・義姉との婚姻慣習）", "文化/民俗", "Tradisi perkawinan turun ranjang masih dijumpai di beberapa komunitas adat."),
            ("turun pamor", "名声・威光が下がる", "人気が衰える、落ち目になる、権威を失墜する", "社会/芸能", "Politisi senior itu mulai turun pamor setelah terbukti terlibat skandal suap."),
            ("turun temurun", "降りて降りる", "代々受け継がれた、代々の、世襲の", "歴史/伝統", "Resep bumbu rendang ini diwariskan secara turun temurun dari nenek moyang."),
            ("turun ke jalan", "通りに降りる", "路上デモを行う、抗議デモに参加する", "政治/市民社会", "Ribuan mahasiswa turun ke jalan menuntut pembatalan kenaikan tarif listrik.")
        ],
        "details": [
            {
                "term": "turun tangan (ikut campur menyelesaikan masalah)",
                "trans": "自ら直接介入する、乗り出す、ひと肌脱ぐ",
                "nuance": "単なる部外者の干渉ではなく、最高権力者や上司が、膠着・泥沼化した現場の問題を自らの威信と決断力で収束させるために「上座から降りて直接現場で手を動かす」という称賛的な文脈で多用されます。",
                "ex_id": "Melihat perselisihan internal partai yang kian meruncing, ketua umum terpaksa turun tangan mendamaikan kedua kubu.",
                "ex_kana": "ムリハット プルスリシハン インテルナル パルタイ ヤン キアン メルンチン、クトゥア ウムム トゥルパクサ トゥルン タンガン ムンダマイカン クドゥア クブ",
                "ex_ja": "党内の内部対立がますます先鋭化するのを見て、党首は自ら直接仲裁に乗り出さ（turun tangan）ざるを得ませんでした。",
                "note": "国家指導者や大企業のCEOの果断な行動に冠される代表的フレーズです。"
            },
            {
                "term": "turun minum (istirahat babak pertama)",
                "trans": "ハーフタイムに入る、前半終了の給水休憩",
                "nuance": "サッカー中継やスポーツ報道で「前半終了の笛が鳴る」場面の定番の慣用表現です。熱帯気候の中で選手が水分補給（minum）のためにピッチ脇に降りる光景に由来します。",
                "ex_id": "Kedua tim masih bermain imbang satu-satu hingga waktu turun minum tiba.",
                "ex_kana": "クドゥア ティム マシー ブルマイン インバン サトゥサトゥ ヒンガ ワクトゥ トゥルン ミヌム ティバ",
                "ex_ja": "両チームはハーフタイム（turun minum）に入るまで、1対1の同点で互角の戦いを繰り広げました。",
                "note": "スポーツニュースの見出しで日常的に目にします。"
            },
            {
                "term": "turun temurun (warisan generasi ke generasi)",
                "trans": "代々受け継がれた、代々の、祖父から孫へ伝わる",
                "nuance": "家族の秘伝の味、伝統工芸バティックの染色技法、地域の口承文学など、何世代にもわたり大切に継承されてきた文化的正統性を称える語彙です。",
                "ex_id": "Keahlian membatik tulis ini diajarkan secara turun temurun dari ibu kepada anak gadisnya.",
                "ex_kana": "ケアリアン ムンバティッ トゥリス イニ ディアジャルカン スチャラ トゥルン トゥムルン ダリ イブ クパダ アナッ ガディスニャ",
                "ex_ja": "この手描きバティックの高度な技術は、母から娘へと代々受け継がれて（turun temurun）教え込まれてきました。",
                "note": "`diwariskan turun-temurun`（代々受け継がれる）のセットで頻出します。"
            },
            {
                "term": "turun ke jalan (berdemonstrasi)",
                "trans": "路上デモを行う、街頭に出て抗議の声を上げる",
                "nuance": "法改正や物価高騰、汚職事件に対し、大学生（mahasiswa）や労働組合（buruh）がキャンパスや工場を出て大通りを行進・占拠する市民蜂起を描写します。",
                "ex_id": "Serikat buruh mengancam akan turun ke jalan jika upah minimum sektoral tidak disesuaikan dengan inflasi.",
                "ex_kana": "スリカット ブルフ ムンガンチャム アカン トゥルン ケ ジャラン ジュカ ウパ ミニマム セクトラル ティダッ ディススアイカン ドゥンガン インフラシ",
                "ex_ja": "労働組合は、産業別最低賃金がインフレ率に合わせて改定されない場合、街頭デモに打って出る（turun ke jalan）と警告しました。",
                "note": "インドネシア現代政治の力学を象徴する表現です。"
            },
            {
                "term": "turun pamor (merosot wibawanya)",
                "trans": "人気が落ちる、威光が衰える、凋落する",
                "nuance": "`pamor` は元々クリス（短剣）の刀身に浮き出る神秘的な波紋・霊力を指し、転じて政治家やタレントの放つオーラやカリスマ性を意味します。",
                "ex_id": "Klub raksasa Eropa itu perlahan turun pamor setelah ditinggalkan oleh para bintang andalannya.",
                "ex_kana": "クルブ ラクササ エロパ イトゥ プルラハン トゥルン パモール ステラ ディティンガルカン オレ パラ ビンタン アンダランニャ",
                "ex_ja": "その欧州の名門メガクラブは、主力スター選手たちが去った後、次第に名声と存在感が衰えて（turun pamor）いきました。",
                "note": "栄枯盛衰の文脈で重宝されます。"
            }
        ],
        "dialogue": {
            "title": "労働争議の泥沼化と市長の直接介入",
            "lines": [
                ("Prasetyo", "Aksi buruh yang turun ke jalan sejak kemarin tampaknya belum menunjukkan tanda-tanda akan mereda."),
                ("Nurul", "Benar, Pak. Mediasi antara serikat pekerja dan pemilik pabrik masih menemui jalan buntu."),
                ("Prasetyo", "Kalau dibiarkan berlarut-larut, perekonomian kota kita bisa lumpuh. Wali kota harus segera turun tangan."),
                ("Nurul", "Kabar terakhir, beliau sudah memanggil kedua belah pihak ke balai kota siang ini untuk mencari jalan tengah.")
            ],
            "trans": [
                ("プラセティヨ", "昨日から街頭デモに出ている（turun ke jalan）労働者たちの抗議行動、収束する気配が一向に見えないね。"),
                ("ヌルル", "はい。労働組合と工場経営者の協議は依然として行き詰まりを見せています。"),
                ("プラセティヨ", "このまま放置すれば市の経済が麻痺しかねない。市長が直ちに自ら直接介入する（turun tangan）べきだ。"),
                ("ヌルル", "最新の情報では、市長は妥協点（jalan tengah）を見出すべく、今昼両陣営を市庁舎に召集されたそうです。")
            ]
        },
        "grammar_points": [
            "**自動詞としての turun**: `turun` は物理的・状態的な下降を表す自動詞です。目的語を直接取る他動詞（〜を下ろす、〜を値下げする）にする場合は、使役接尾辞 `-kan` を付加して `menurunkan`（ムヌルンカン）とします（例: `menurunkan harga`＝値下げする、`menurunkan penumpang`＝乗客を降ろす）。",
            "**名詞化 penurunan**: 接頭辞 `pe-` と接尾辞 `-an` による `penurunan` は、「減少・下落・低下」を意味する主要経済・学術名詞となります（例: `penurunan inflasi`＝インフレ率の低下）。"
        ],
        "quizzes": [
            {
                "q": "「国家元首やトップ指導者が、混迷を極める現場の対立を仲裁するために自ら直接乗り出す・介入する」を意味する成句はどれか。",
                "choices": ["turun tangan", "turun ranjang", "turun minum", "turun pamor"],
                "ans": "turun tangan",
                "expl": "自ら直接介入して問題解決に乗り出す表現は `turun tangan` です。"
            },
            {
                "q": "サッカーなどの試合中継で「前半終了のハーフタイムに入る」を意味する定番の慣用句はどれか。",
                "choices": ["turun minum", "turun temurun", "turun ke jalan", "turun harga"],
                "ans": "turun minum",
                "expl": "スポーツ中継でハーフタイムの休憩に入る表現は `turun minum` です。"
            },
            {
                "q": "「何世代にもわたって代々祖先から継承されてきた伝統技術」を表す副詞的連語はどれか。",
                "choices": ["turun temurun", "pasang surut", "tarik ulur", "jatuh bangun"],
                "ans": "turun temurun",
                "expl": "代々受け継がれた、世代を超えて伝承される連語は `turun temurun` です。"
            }
        ],
        "culture_column": {
            "title": "「Turun Ranjang」にみる伝統婚姻と家族扶養の互助精神",
            "body": "直訳すると「寝台に降りる」という意味の `turun ranjang` は、妻に先立たれた夫が、残された幼い子どもたちの養育のために亡き妻の未婚の妹（義妹）と再婚する伝統的慣習法（Hukum Adat）の婚姻制度を指します。一見すると奇異に思えるかもしれませんが、共同体の財産の流出を防ぎ、孤児となった甥や姪を他人の手に委ねず実の叔母が母親代わりとなって慈しむという、伝統社会の深い家族互助（gotong royong）の知恵から生まれた制度なのです。"
        }
    },
    {
        "filename": "docs/lexicon/12-verb-collocations-tahan.md",
        "title": "【共起連語】語根 tahan の必須コロケーション辞典：tahan banting / tahan lama / tahan uji / tahan lapar",
        "root": "tahan",
        "meaning": "耐える、持ちこたえる、拘束する、長持ちする",
        "core_concept": "「外からの強い衝撃や苦痛に屈せず耐え忍ぶ」基本概念から、「打たれ強く過酷な試練に耐える」「長持ちして耐久性がある」「試練を乗り越えて実証されている」「空腹や誘惑を自制する」という、強靭な物理的・精神的耐久力を表す連語を形成します。",
        "table_rows": [
            ("tahan banting", "叩きつけに耐える", "打たれ強い、へこたれない、強靭な耐性がある", "性格/ビジネス", "Seorang wirausahawan sejati harus bermental tahan banting menghadapi kegagalan."),
            ("tahan lama", "長さに耐える", "長持ちする、耐久性がある、賞味期限が長い", "製品/実用", "Baterai ponsel pintar model terbaru ini diklaim tahan lama hingga dua hari penuh."),
            ("tahan uji", "テストに耐える", "実証済みの、試練に耐えた、信頼性が高い", "品質/道徳", "Kesetiaan dan integritas diplomat itu sudah terbukti tahan uji dalam berbagai krisis."),
            ("tahan lapar / tahan haus", "空腹・渇きに耐える", "飢えに耐える、空腹を我慢する", "健康/断食", "Selama menjalankan ibadah puasa, umat muslim dilatih untuk tahan lapar dan haus."),
            ("tahan godaan", "誘惑に耐える", "誘惑に負けない、自制心がある、意志が堅い", "倫理/宗教", "Pejabat yang berintegritas tinggi tidak akan goyah dan selalu tahan godaan suap."),
            ("tahan api / tahan air", "火・水に耐える", "耐火の、難燃性の / 完全防水の", "工業/技術", "Kubah brankas bank dirancang menggunakan material khusus yang tahan api dan tahan air."),
            ("tahan rasa sakit", "痛みに耐える", "痛みに強い、我慢強い", "医療/日常", "Atlet bela diri itu memiliki fisik yang luar biasa tahan rasa sakit saat bertanding.")
        ],
        "details": [
            {
                "term": "tahan banting (tangguh / ulet luar biasa)",
                "trans": "打たれ強い、過酷な逆境に屈しない、へこたれない",
                "nuance": "直訳は「激しく地面に叩きつけられても壊れないこと」。過酷な環境で揉まれても決して音を上げず、立ち直る不屈のタフネスを備えた人物やビジネスモデルを絶賛する定番の誉め言葉です。",
                "ex_id": "Generasi muda saat ini harus dididik agar memiliki kepribadian tahan banting di dunia kerja yang kompetitif.",
                "ex_kana": "ゲネラシ ムダ サアット イニ ハルス ディディディッ アガル ムミリキ クプリバディアン タハン バンティン ディ ドゥニア クルジャ ヤン コンペティティフ",
                "ex_ja": "現代の若者たちは、競争の激しい実社会において打たれ強く強靭な人格（tahan banting）を備えるよう育成されねばなりません。",
                "note": "採用面接や自己PRで極めて好まれる資質表現です。"
            },
            {
                "term": "tahan lama (awet / berdaya tahan tinggi)",
                "trans": "長持ちする、耐久性がある、寿命が長い",
                "nuance": "家電製品、建材、バッテリー、化粧品の持ち（makeup tahan lama）など、時間的経過に対して劣化せず性能を維持することを指す万能形容表現です。",
                "ex_id": "Peralatan rumah tangga berbahan baja antikarat ini terkenal sangat awet dan tahan lama.",
                "ex_kana": "プララタン ルマー タンガ ブルバハン バジャ アンティカラット イニ トゥルクナル サンガット アウェット ダン タハン ラマ",
                "ex_ja": "このステンレス鋼製の家庭用品は、非常に丈夫で長持ちする（tahan lama）ことで知られています。",
                "note": "同義語のジャワ語由来語 `awet`（アウェット）とよく併用されます。"
            },
            {
                "term": "tahan uji (teruji keandalannya)",
                "trans": "試練を乗り越えた、実証済みの、信頼に足る",
                "nuance": "単に新品の状態で頑丈なだけでなく、幾多の嵐や困難な実戦環境に晒された結果、その優秀さや誠実さが客観的に証明されている状態を指します。",
                "ex_id": "Persahabatan mereka berdua telah terbukti tahan uji melewati berbagai cobaan hidup.",
                "ex_kana": "プルサハバタン ムレカ ブルドゥア トゥラー トゥルブクティ タハン ウジ ムレワティ ブルバガイ ジョバアン ヒドゥップ",
                "ex_ja": "彼ら二人の友情は、人生の様々な試練を乗り越えて実証済み（tahan uji）であることが証明されました。",
                "note": "友情、愛、技術、制度の堅牢さを讃える表現です。"
            },
            {
                "term": "tahan godaan (mampu mengendalikan hawa nafsu)",
                "trans": "誘惑に負けない、自制心を保つ",
                "nuance": "金銭（賄賂）、権力、異性、怠惰などの誘惑に直面しても、倫理的規範や信仰心を崩さず踏みとどまる高潔な精神力を描写します。",
                "ex_id": "Sebagai penegak hukum, keberanian untuk tahan godaan adalah harga mati yang tidak bisa ditawar.",
                "ex_kana": "スバガイ プヌガッ フクム、クブルアニアン ウントゥッ タハン ゴダアン アダラー ハルガ マティ ヤン ティダッ ビサ ディタワール",
                "ex_ja": "法執行官として、誘惑に屈しない（tahan godaan）毅然とした勇気は何事にも代えがたい絶対条件です。",
                "note": "`harga mati`（譲れない一線）とよく結びつきます。"
            },
            {
                "term": "tahan api / tahan air",
                "trans": "耐火の / 完全防水の",
                "nuance": "産業規格や製品スペック（仕様）で頻出する技術複合語です。時計の防水機能（jam tangan tahan air）や防護服の難燃機能（baju tahan api）など実用度抜群です。",
                "ex_id": "Bangunan arsip nasional ini menggunakan pintu kedap udara yang tahan api hingga suhu seribu derajat.",
                "ex_kana": "バングナン アルシプ ナシオナル イニ ムングナカン ピントゥ クダップ ウダラ ヤン タハン アピ ヒンガ スフ スリブ ドラジャット",
                "ex_ja": "この国立公文書館の建物は、摂氏千度の高温に耐えうる耐火仕様（tahan api）の気密扉を採用しています。",
                "note": "名詞の直後に置かれて修飾形容詞として機能します。"
            }
        ],
        "dialogue": {
            "title": "スタートアップの起業環境と創業者の資質",
            "lines": [
                ("Satria", "Banyak sekali startup baru yang gulung tikar hanya dalam hitungan bulan ya, Gita."),
                ("Gita", "Iya, iklim ekonomi sedang sulit. Hanya pendiri yang bermental tahan banting yang mampu bertahan."),
                ("Satria", "Betul sekali. Selain produknya harus tahan uji di pasar, manajemen keuangannya juga harus tahan lama menghadapi masa paceklik."),
                ("Gita", "Dan yang terpenting, pimpinannya harus tahan godaan untuk tidak menghamburkan dana investor demi gengsi semata.")
            ],
            "trans": [
                ("サトリア", "ほんの数ヶ月で倒産（gulung tikar）してしまう新規スタートアップが本当に多いね、ギタさん。"),
                ("ギタ", "ええ、経済情勢が厳しいですから。打たれ強く強靭なメンタル（tahan banting）を持つ創業者だけが生き残れます。"),
                ("サトリア", "まったくその通りだ。製品が市場の試練に耐えうる（tahan uji）だけでなく、財務管理も不況期に耐えて長持ち（tahan lama）しなければならない。"),
                ("ギタ", "そして何より、見栄のためだけに投資家の資金を浪費しないよう、指導者が誘惑に負けない（tahan godaan）自制心を持つことが不可欠です。")
            ]
        },
        "grammar_points": [
            "**接辞 menahan による他動詞化**: 語根 `tahan` は無声音 `t` で始まるため、他動詞接頭辞 `meN-` で `t` が `n` に変化して `menahan`（ムナハン）となります。意味は「〜を耐え忍ぶ」「〜を抑える（menahan emosi）」「〜を身柄拘束・勾留する（menahan tersangka）」と法務・心理分野に発展します。",
            "**名詞化 ketahanan**: 周囲辞 `ke-...-an` を伴う `ketahanan` は、「耐性・耐久力・安全保障」を意味し、国家政策の要語である `ketahanan pangan`（食料安全保障）、`ketahanan energi`（エネルギー安全保障）を形成します。"
        ],
        "quizzes": [
            {
                "q": "「逆境や失敗に直面してもへこたれず、立ち直る打たれ強い強靭なメンタル」を表す慣用句はどれか。",
                "choices": ["tahan banting", "tahan lapar", "tahan air", "pasang badan"],
                "ans": "tahan banting",
                "expl": "打たれ強く逆境に強い資質を表す慣用句は `tahan banting` です。"
            },
            {
                "q": "「幾多の困難な試練を乗り越え、その真価や誠実さが実証されている」を意味する連語はどれか。",
                "choices": ["tahan uji", "tahan lama", "tahan api", "tutup buku"],
                "ans": "tahan uji",
                "expl": "試練に耐えて実証済みの状態は `tahan uji` と言います。"
            },
            {
                "q": "国家の最重要政策課題である「食料安全保障」を意味する正式なインドネシア語はどれか。",
                "choices": ["ketahanan pangan", "pertahanan pangan", "penahanan pangan", "tahan lapar pangan"],
                "ans": "ketahanan pangan",
                "expl": "食料安全保障は `ketahanan pangan`（エネルギー安全保障は `ketahanan energi`）です。"
            }
        ],
        "culture_column": {
            "title": "「Tahan Banting」とインドネシア庶民のたくましさ",
            "body": "インドネシア語で「叩きつけられても平気」を意味する `tahan banting`。路地裏で古タイヤを巧みに再利用したサンダルや、何度故障しても直して乗り続ける旧式バイクのように、どんなに貧しく過酷な環境であっても創意工夫（akal-akalan）と朗らかな笑顔を絶やさずに生き抜く庶民のたくましさ（daya lentur / レジリエンス）を象徴する、最も愛着のこもった人生賛歌の表現です。"
        }
    },
    {
        "filename": "docs/lexicon/13-verb-collocations-pecah.md",
        "title": "【共起連語】語根 pecah の必須コロケーション辞典：pecah belah / pecah rekor / pecah tangis / pecah kongsi",
        "root": "pecah",
        "meaning": "割れる、破れる、分裂する、勃発する",
        "core_concept": "「ガラスや陶器が粉々に砕け散る」物理現象から、「国家や組織が内部分裂する」「最高新記録が更新される（記録を破る）」「感情が堰を切って号泣する」「共同事業や連立政権がパートナーシップを解消する」という、崩壊と突破の劇的メタファーを形成します。",
        "table_rows": [
            ("pecah belah", "割れて砕ける", "分裂する、仲違いする、団結が崩壊する", "国家/政治", "Politik adu domba kolonial Belanda berhasil memecah belah persatuan suku-suku Nusantara."),
            ("pecah rekor", "記録を割る", "新記録を樹立する、記録を塗り替える、記録更新する", "スポーツ/経済", "Penjualan album musik tersebut sukses memecah rekor tercepat di platform digital."),
            ("pecah tangis", "泣き声が割れる", "号泣する、堰を切ったように泣き崩れる", "感情/追悼", "Pecah tangis keluarga tak terbendung saat menyambut jenazah korban kecelakaan."),
            ("pecah kongsi", "共同・組合が割れる", "提携を解消する、パートナーシップが決裂する、共同出資から手を引く", "ビジネス/政界", "Kedua konglomerat itu akhirnya pecah kongsi setelah berselisih soal visi perusahaan."),
            ("pecah perang", "戦争が割れる", "戦争が勃発する、武力衝突が火を噴く", "国際/軍事", "Kekhawatiran global kian memuncak bahwa ketegangan regional akan memicu pecah perang."),
            ("pecah ketuban", "羊水が割れる", "破水する（出産時の生理現象）", "医療/出産", "Ibu hamil itu segera dilarikan ke rumah sakit setelah mengalami pecah ketuban."),
            ("pecah suara", "声が割れる", "声変わりする（男子の第二次性徴）", "思春期/生理", "Remaja laki-laki biasanya mulai mengalami pecah suara pada usia tiga belas tahun.")
        ],
        "details": [
            {
                "term": "pecah belah (terpecah / disintegrasi)",
                "trans": "分裂する、仲違いする、バラバラになる",
                "nuance": "国家、民族、政党、家族などの共同体の結束（persatuan）が、外部の謀略や内部の対立によって修復不能なまでに崩壊する危機的状態を表します。",
                "ex_id": "Jangan sampai bangsa yang majemuk ini pecah belah hanya karena perbedaan pilihan politik dalam pemilu.",
                "ex_kana": "ジャンガン サンパイ バンサ ヤン マジュムッ イニ プチャ ブラ ハニャ カレナ プルベダアン ピリハン ポリティッ ダラム プミル",
                "ex_ja": "この多様な国家が、選挙での支持政党の違いだけで分裂し仲違いする（pecah belah）ようなことがあってはなりません。",
                "note": "オランダ植民地時代の分断統治策は `politik pecah belah`（分割統治）と呼ばれます。"
            },
            {
                "term": "pecah rekor (memecahkan rekor)",
                "trans": "新記録を樹立する、記録を塗り替える",
                "nuance": "陸上競技のタイム、映画の興行収入、株式市場の取引高など、従来の最高水準を大幅に突破して歴史的快挙を達成した瞬間に使われます。",
                "ex_id": "Sprinter muda asal Nusa Tenggara Barat itu berhasil memecah rekor nasional lari 100 meter putra.",
                "ex_kana": "スプリンテル ムダ アサル ヌサ トゥンガラ バラット イトゥ ブルハシル ムムチャ レコール ナシオナル ラリ スラトゥス メテル プトラ",
                "ex_ja": "西ヌサ・トゥンガラ出身の若きスプリンターは、男子100メートル走の国内新記録を見事に塗り替え（memecah rekor）ました。",
                "note": "他動詞 `memecahkan rekor`（記録を破る）としても頻出します。"
            },
            {
                "term": "pecah tangis (tangis histeris meledak)",
                "trans": "号泣する、堰を切ったように涙があふれる",
                "nuance": "耐え忍んでいた悲嘆や感動が限界を超え、大声を上げて泣き崩れる劇的な情動の爆発を描写します。",
                "ex_id": "Pecah tangis haru menyelimuti ruang sidang ketika hakim memvonis bebas terdakwa yang tak bersalah.",
                "ex_kana": "プチャ タンギス ハル ムニェリムティ ルアン シダン クティカ ハキム ムムヴォニス ベバス トゥルダクワ ヤン タッ ブルサラー",
                "ex_ja": "裁判官が無実の被告人に無罪を言い渡した瞬間、法廷内は感動の号泣（pecah tangis haru）に包まれました。",
                "note": "悲哀だけでなく感動の涙（tangis haru）にも使われます。"
            },
            {
                "term": "pecah kongsi (bubar kemitraan bisnis/politik)",
                "trans": "共同事業を解消する、パートナーシップが決裂する",
                "nuance": "`kongsi` は中国語（福建語「公司」）由来で共同出資・組合を意味します。共同経営者同士の仲違いによる企業解散や、大統領候補と副大統領候補の政治的決裂に用いられます。",
                "ex_id": "Setelah bermitra selama dua dekade membangun jaringan ritel, kedua sahabat karib itu resmi pecah kongsi.",
                "ex_kana": "ステラ ブルミトラ スラマ ドゥア デカデ ムンバングン ジャリンガン リテル、クドゥア サハバット カリブ イトゥ レスミ プチャ コンシ",
                "ex_ja": "小売チェーンの構築で20年間にわたりパートナーを組んできた親友同士の二人は、正式に提携解消（pecah kongsi）しました。",
                "note": "ビジネス界や政界のゴシップ記事で頻繁に見出しになります。"
            },
            {
                "term": "pecah perang (meletus pertempuran)",
                "trans": "戦争が勃発する、武力衝突が起きる",
                "nuance": "平和状態が暴力的に破壊され、国家間や地域間で全面的な軍事衝突が火を噴く事態を表現します。",
                "ex_id": "Masyarakat internasional mendesak Dewan Keamanan PBB bertindak cepat sebelum pecah perang terbuka.",
                "ex_kana": "マシャラカット インテルナシオナル ムンデスッ デワン クアマナン ペベベ ブルティンダッ チパット スブルム プチャ プラン トゥルブカ",
                "ex_ja": "国際社会は、公然たる全面戦争が勃発する（pecah perang）前に国連安保理が迅速に行動するよう求めました。",
                "note": "「Meletus perang（戦争が爆発する）」とも表現されます。"
            }
        ],
        "dialogue": {
            "title": "創業パートナーの決裂と新記録の達成",
            "lines": [
                ("Rian", "Apakah benar rumor bahwa kedua pendiri platform fintech unicorn itu sudah resmi pecah kongsi?"),
                ("Dina", "Iya, sangat disayangkan. Perbedaan visi mengenai ekspansi global membuat hubungan mereka pecah belah."),
                ("Rian", "Padahal produk baru mereka kemarin baru saja memecah rekor volume transaksi harian tertinggi."),
                ("Dina", "Benar sekali. Kesuksesan finansial ternyata tidak selalu menjamin keharmonisan kemitraan.")
            ],
            "trans": [
                ("リアン", "あのユニコーンFintechプラットフォームの共同創業者二人が正式に提携解消（pecah kongsi）したという噂は本当かい？"),
                ("ディナ", "ええ、本当に残念だわ。海外展開をめぐるビジョンの食い違いで、二人の関係は修復不能に分裂して（pecah belah）しまったの。"),
                ("リアン", "昨日の新製品なんて、過去最高の1日あたり取引量の新記録を塗り替えた（memecah rekor）ばかりだったのに。"),
                ("ディナ", "まさにその通りよ。経済的成功がパートナーシップの調和を必ずしも保証するとは限らないわね。")
            ]
        },
        "grammar_points": [
            "**meN- 変化時の有声音 p 保持と脱落**: `pecah` の語頭は無声音 `p` です。したがって接頭辞 `meN-` が付加されると `p` が鼻音 `m` に変化して `memecah`（ムムチャ）となります（例: `memecahkan rekor`＝記録を破る、`memecahkan masalah`＝問題を解決する）。",
            "**他動詞接尾辞 -kan**: `memecahkan` は「割る・砕く」という物理的意味だけでなく、`memecahkan masalah`（問題を解決する・ブレイクスルーする）という極めて知的な意味領域へ展開します。"
        ],
        "quizzes": [
            {
                "q": "「共同出資者やビジネスパートナー同士の対立により、提携が決裂・解散すること」を表す成句はどれか。",
                "choices": ["pecah kongsi", "pecah rekor", "pecah tangis", "pecah suara"],
                "ans": "pecah kongsi",
                "expl": "共同事業やパートナーシップの決裂・解散を表す表現は `pecah kongsi` です。"
            },
            {
                "q": "オランダ植民地政府が群島の諸民族の団結を阻害するために用いた「分割統治策」を指す歴史用語はどれか。",
                "choices": ["politik pecah belah", "politik pintu terbuka", "politik balas budi", "politik pasang badan"],
                "ans": "politik pecah belah",
                "expl": "分割統治（分断して統治せよ）は `politik pecah belah`（別名 `devide et impera`）と呼ばれます。"
            },
            {
                "q": "「スポーツ選手が大会の歴代最高スコアを塗り替えて新記録を樹立した」を表す動詞句はどれか。",
                "choices": ["memecahkan rekor", "memecahkan masalah", "memecahkan ombak", "memecahkan cermin"],
                "ans": "memecahkan rekor",
                "expl": "新記録を樹立する・破るは `memecahkan rekor`（または `pecah rekor`）です。"
            }
        ],
        "culture_column": {
            "title": "「Kongsi」にみる華人文化とインドネシア商業史",
            "body": "慣用句 `pecah kongsi` に登場する `kongsi`（公司）は、18〜19世紀にカリマンタンの金鉱やジャワの砂糖産業で台頭した華人商人の合資組合組織に由来します。血縁や同郷の絆で結ばれた強固な企業共同体も、利害の対立や世代交代によってひとたび不和が生じると劇的な解散を迎える歴史の教訓が、現代インドネシアのビジネス語彙として深く定着しているのです。"
        }
    },
    {
        "filename": "docs/lexicon/14-verb-collocations-putar.md",
        "title": "【共起連語】語根 putar の必須コロケーション辞典：putar balik / putar otak / putar lidah / putar haluan",
        "root": "putar",
        "meaning": "回す、回転する、曲がる、向きを変える",
        "core_concept": "「軸を中心にぐるりと回転させる」物理動作から、「車椅子や車がUターンする」「頭をフル回転させて知恵を絞る」「言葉を巧みにすり替えて言い逃れる」「政治方針や進路を180度転換する」という、方向転換・知力発揮・詭弁のダイナミックなメタファーを生み出します。",
        "table_rows": [
            ("putar balik", "後ろへ回る", "Uターンする、引き返す、事実を歪曲・捏造する", "交通/論理", "Pengemudi dilarang putar balik di jalan tol karena sangat membahayakan."),
            ("putar otak", "脳を回す", "頭を絞る、知恵を絞る、打開策を必死に考える", "ビジネス/思考", "Manajemen harus putar otak mencari sumber pendapatan baru di tengah pandemi."),
            ("putar lidah", "舌を回す", "言葉を巧みにすり替える、詭弁を弄する、二枚舌を使う", "道徳/弁舌", "Politisi licik itu pandai memutar lidah untuk memutarbalikkan fakta di hadapan publik."),
            ("putar haluan", "船首を回す", "進路を変更する、方針を大転換する、宗旨変えする", "海事/政治", "Pemerintah memutuskan putar haluan ekonomi dari impor konsumtif ke produksi domestik."),
            ("putar roda", "車輪を回す", "経済を回す、活動を継続させる、循環させる", "経済/比喩", "Bantuan modal kerja ini ditujukan untuk memutar roda perekonomian sektor UMKM."),
            ("putar balik fakta", "事実を後ろへ回す", "事実を歪曲する、黒を白と言いくるめる、捏造する", "司法/メディア", "Kuasa hukum menuduh saksi telah memutarbalikkan fakta kejadian sebenarnya."),
            ("putar uang", "お金を回す", "資金を回転させる、投資で利益を回す", "金融/生活", "Pedagang pasar tradisional memutar uang harian untuk belanja stok dagangan esok hari.")
        ],
        "details": [
            {
                "term": "putar balik (berbalik arah / U-turn)",
                "trans": "Uターンする、引き返す / 事実を歪曲する",
                "nuance": "第一の意味は道路交通での「Uターン（putar balik arah）」。第二の意味（比喩）では、`putar balik fakta` のように「事実を正反対にねじ曲げて嘘をつく」という批判的文脈で多用されます。",
                "ex_id": "Setelah menyadari salah jalan, sopir taksi itu segera putar balik di persimpangan berikutnya.",
                "ex_kana": "ステラ ムニャダリ サラー ジャラン、ソピル タクシ イトゥ スグラ プタール バリッ ディ プルスィムパンガン ブルイクットニャ",
                "ex_ja": "道を間違えたことに気づいた後、そのタクシー運転手は次の交差点ですぐにUターン（putar balik）しました。",
                "note": "ジャカルタ名物のUターン手助け屋は `polisi cepek` と呼ばれます。"
            },
            {
                "term": "putar otak (berpikir keras mencari solusi)",
                "trans": "知恵を絞る、頭をフル回転させる",
                "nuance": "資金繰り難、厳しい納期、技術的障害などの窮地に追い込まれた際、生き残りをかけて必死にアイデアをひねり出す人間の知的奮闘を生き生きと描写します。",
                "ex_id": "Para perancang produk harus putar otak agar biaya produksi bisa ditekan tanpa menurunkan kualitas.",
                "ex_kana": "パラ プランチャン プロドゥッ ハルス プタール オタッ アガル ビアヤ プロドゥクシ ビサ ディトゥカン タンパ ムヌルンカン クアリタス",
                "ex_ja": "製品設計者たちは、品質を落とさずに製造コストを削減できるよう知恵を絞ら（putar otak）ねばなりません。",
                "note": "起業家やエンジニアの日常会話で多用されます。"
            },
            {
                "term": "putar haluan (mengubah orientasi / kebijakan)",
                "trans": "船首の向きを変える、方針を180度転換する",
                "nuance": "航海用語の「船首（haluan）を回す」から転じ、政権の外交方針の転換、企業の経営多角化、個人のキャリア転換などをドラマチックに表現します。",
                "ex_id": "Menghadapi era transisi energi, perusahaan minyak multinasional itu mulai putar haluan ke energi surya.",
                "ex_kana": "ムンハダピ エラ トランシシ エネルギ、プルサハアン ミニャッ ムルティナシオナル イトゥ ムライ プタール ハルアン ケ エネルギ スルヤ",
                "ex_ja": "エネルギー転換期に直面し、その多国籍石油企業は太陽光発電へと方針の大転換（putar haluan）を図り始めました。",
                "note": "`mengubah haluan` とも言います。"
            },
            {
                "term": "putar lidah / memutar lidah (bersilat lidah)",
                "trans": "言葉巧みにすり替える、二枚舌を使う、詭弁を弄する",
                "nuance": "自分の失言や悪事を追及された際、都合よく解釈を変えたり詭弁を弄したりして責任を煙に巻く不誠実な弁舌を糾弾する成句です。",
                "ex_id": "Terdakwa berulang kali mencoba memutar lidah untuk mengelabui pertanyaan jaksa penuntut umum.",
                "ex_kana": "トゥルダクワ ブルウラン カリ ムンチョバ ムムタール リダー ウントゥッ ムンゲラブイ プルタニャアン ジャクサ プヌントゥッ ウムム",
                "ex_ja": "被告人は検察官の追及の質問を煙に巻こうと、何度も言葉を巧みにすり替え（memutar lidah）ようと試みました。",
                "note": "`bersilat lidah`（舌先で立ち回る）と同義です。"
            },
            {
                "term": "memutar roda perekonomian",
                "trans": "経済の歯車を回す、活動を循環させる",
                "nuance": "国家のマクロ経済政策、景気刺激策、消費喚起キャンペーンにおいて、停滞したマネーや産業活動を再び活性化させる大義名分として語られます。",
                "ex_id": "Penyaluran bantuan sosial menjelang hari raya terbukti efektif memutar roda perekonomian di daerah pedesaan.",
                "ex_kana": "プニャルラン バントゥアン ソシアル ムンジュラン ハリ ラヤ トゥルブクティ エフェクティフ ムムタール ロダ プルエコノミアン ディ ダエラ プデサアン",
                "ex_ja": "祝日を前にした社会保障給付の支給は、農村地域の経済の歯車を回す（memutar roda perekonomian）上で効果的であることが証明されました。",
                "note": "中央銀行総裁や財務大臣の演説で多用される定型表現です。"
            }
        ],
        "dialogue": {
            "title": "工場の原材料高騰と経営陣の打開策",
            "lines": [
                ("Bagus", "Harga bahan baku impor melonjak drastis akibat pelemahan nilai tukar rupiah, Bu Nia."),
                ("Nia", "Situasi ini sangat kritis. Kita benar-benar harus putar otak agar arus kas perusahaan tetap lancar."),
                ("Bagus", "Apakah sudah saatnya pabrik kita putar haluan mencari pemasok lokal alternatif di dalam negeri?"),
                ("Nia", "Tepat. Jangan sampai kita kehabisan modal kerja untuk memutar roda operasional pabrik bulan depan.")
            ],
            "trans": [
                ("バグス", "ルピア安の影響で輸入原材料の価格が劇的に高騰しています、ニアさん。"),
                ("ニア", "極めて危機的な状況ね。会社のキャッシュフローを維持するために、私たちは本気で知恵を絞ら（putar otak）なければならないわ。"),
                ("バグス", "工場の方針を転換して（putar haluan）、国内の代替サプライヤーを開拓すべき時でしょうか？"),
                ("ニア", "その通りよ。来月の工場の操業の歯車を回す（memutar roda operasional）ための運転資金を切らすような事態だけは避けなければ。")
            ]
        },
        "grammar_points": [
            "**meN- 変化時の無声音 p 鼻音化**: `putar` の頭文字は無声音 `p` です。接頭辞 `meN-` で `p` が脱落して鼻音 `m` に同化し、`memutar`（ムムタール）となります（例: `memutar musik`＝音楽を再生する、`memutarbalikkan`＝ねじ曲げる）。",
            "**両分接辞 memutarbalikkan**: `putar balik` に他動詞接頭辞 `meN-` と使役接尾辞 `-kan` が付加されると、2語が結合して `memutarbalikkan`（事実等を歪曲・捏造する）という1語の強力な他動詞を形成します。"
        ],
        "quizzes": [
            {
                "q": "「危機的状況を打開するため、必死になって知恵を絞る・頭をフル回転させる」を意味する慣用表現はどれか。",
                "choices": ["putar otak", "putar haluan", "putar balik", "tahan banting"],
                "ans": "putar otak",
                "expl": "知恵を絞って必死に考える表現は `putar otak` です。"
            },
            {
                "q": "「道路上で自動車が進行方向を180度反転させてUターンする」ことを表す交通用語はどれか。",
                "choices": ["putar balik", "turun tangan", "lepas landas", "naik kelas"],
                "ans": "putar balik",
                "expl": "Uターンする、引き返す表現は `putar balik` です。"
            },
            {
                "q": "法廷で「証拠を都合よくねじ曲げ、事実を白昼堂々捏造・歪曲する」を意味する高度な他動詞はどれか。",
                "choices": ["memutarbalikkan fakta", "memecahkan masalah", "mengambil alih kuasa", "membuka rahasia"],
                "ans": "memutarbalikkan fakta",
                "expl": "事実を歪曲・捏造することは `memutarbalikkan fakta` と言います。"
            }
        ],
        "culture_column": {
            "title": "「Polisi Cepek」とジャカルタ名物プタール・バリック",
            "body": "ジャカルタの幹線道路を車で走ると、Uターン禁止でない中央分離帯の切れ目（putaran balik）に必ずといっていいほど「手招きで車を誘導する一般人」が立っています。彼らは「ポリスィ・チェペッ（Polisi Cepek / 100ルピア警官）」と呼ばれ、激しい渋滞の中で強引に車列を止めてUターンを支援し、運転手から2,000ルピア程度の小銭（uang receh）を受け取る非公式なギグワーカーです。街の構造的渋滞が生んだインドネシアの逞しいストリートカルチャーです。"
        }
    },
    {
        "filename": "docs/lexicon/15-verb-collocations-jalan.md",
        "title": "【共起連語】語根 jalan の必須コロケーション辞典：jalan keluar / jalan pintas / jalan buntu / jalan tengah",
        "root": "jalan",
        "meaning": "道、道路、歩く、進む、機能する",
        "core_concept": "「人や車が通る物理的な道路、前に進む歩行動作」から、「難問を解決する出口・方策」「危険な抜け道や近道」「議論や交渉の行き詰まり（袋小路）」「対立双方を調停する妥協点・中道」という、問題解決と意思決定の道筋を表す最重要語彙群を構成します。",
        "table_rows": [
            ("jalan keluar", "出る道", "解決策、打開策、出口、脱出口", "ビジネス/一般", "Para pakar berkumpul untuk mencari jalan keluar dari krisis pangan global."),
            ("jalan pintas", "切断する道", "近道、抜け道、手っ取り早い安易な手段", "道徳/比喩", "Meraih kesuksesan sejati membutuhkan proses panjang, bukan lewat jalan pintas."),
            ("jalan buntu", "塞がった道", "行き詰まり、袋小路、暗礁、デッドロック", "交渉/政治", "Negosiasi sengketa batas wilayah terancam jalan buntu akibat klaim sepihak."),
            ("jalan tengah", "真ん中の道", "妥協案、中道、折衷案、和解の着地点", "調停/哲学", "Kedua belah pihak sepakat mengambil jalan tengah demi menghindari konflik berkepanjangan."),
            ("jalan tol", "有料の道", "高速道路、有料自動車専用道路", "交通/土木", "Pembangunan jalan tol Trans-Jawa telah memangkas waktu tempuh antarprovinsi secara drastis."),
            ("jalan pikiran", "思考の道", "思考回路、考えの道筋、ロジック", "哲学/心理", "Sulit memahami jalan pikiran orang yang tega mengkhianati sahabatnya sendiri."),
            ("jalan lurus", "まっすぐな道", "正道、正しい生き方、真理の道", "宗教/倫理", "Doa setiap insan beriman adalah agar senantiasa dibimbing di jalan yang lurus.")
        ],
        "details": [
            {
                "term": "jalan keluar (solusi / pemecahan masalah)",
                "trans": "解決策、打開策、解決の糸口、出口",
                "nuance": "複雑に絡み合った危機や対立から脱出するための現実的・実行可能な解決策（solusi）を指す、最も頻出するポジティブなコロケーションです。",
                "ex_id": "Diskusi meja bundar ini diselenggarakan demi menemukan jalan keluar yang menguntungkan semua pihak.",
                "ex_kana": "ディスクシ メジャ ブンダル イニ ディスレンガラカン デミ ムヌムカン ジャラン クルアル ヤン ムングントゥンカン スムア ピハッ",
                "ex_ja": "この円卓会議は、すべての当事者に利益をもたらす解決策（jalan keluar）を見出すために開催されました。",
                "note": "`menemukan jalan keluar`（解決策を見出す）のセットで頻出します。"
            },
            {
                "term": "jalan buntu (kebuntuan / dead-lock)",
                "trans": "行き詰まり、暗礁に乗り上げる、袋小路",
                "nuance": "物理的な行き止まりの道だけでなく、双方が一歩も譲らない外交交渉、捜査が行き詰まった刑事事件など、前進が完全に阻まれた絶望的状況を表します。",
                "ex_id": "Proses mediasi perceraian itu menemui jalan buntu karena tidak ada kesepakatan hak asuh anak.",
                "ex_kana": "プロセス メディアシ プルチェライアン イトゥ ムヌムイ ジャラン ブントゥ カレナ ティダッ アダ クセパカタン ハッ アスー アナッ",
                "ex_ja": "子どもの養育権に関する合意が得られなかったため、その離婚調停の手続きは行き詰まり（jalan buntu）を迎えました。",
                "note": "`menemui jalan buntu`（暗礁に乗り上げる）という連語が定石です。"
            },
            {
                "term": "jalan pintas (cara instan yang berisiko)",
                "trans": "近道 / 安易な抜け道（安直な手）",
                "nuance": "物理的なショートカット（近道）の意味に加え、「地道な努力を怠って、不正やインスタントな方法で手っ取り早く結果を得ようとする危うい態度」を戒める比喩として多用されます。",
                "ex_id": "Jangan mengambil jalan pintas dengan menggunakan joki skripsi jika ingin menjadi sarjana yang berintegritas.",
                "ex_kana": "ジャンガン ムンガンビル ジャラン ピンタス ドゥンガン ムングナカン ジョキ スクリプシ ジュカ インギン ムンジャディ サルジャナ ヤン ブルインテグリタス",
                "ex_ja": "高潔な学士になりたいのであれば、卒論代行（joki）を使って安易な抜け道（jalan pintas）を選んではなりません。",
                "note": "`mengambil jalan pintas`（近道をする・安直な手を使う）と共起します。"
            },
            {
                "term": "jalan tengah (kompromi / titik temu)",
                "trans": "妥協点、折衷案、中道",
                "nuance": "双方が極端な要求を取り下げ、互いに譲歩し合って見出す合意点（kompromi）です。インドネシアの国是であるパンチャシラ（Pancasila）精神そのものと深く結びついています。",
                "ex_id": "Hakim mediator berhasil merumuskan jalan tengah yang dapat diterima oleh buruh dan pengusaha.",
                "ex_kana": "ハキム メディアトール ブルハシル ムルムスカン ジャラン トゥンガ ヤン ダパット ディトゥリマ オレ ブルフ ダン プングサハ",
                "ex_ja": "調停裁判官は、労働者と経営者の双方が受け入れ可能な妥協案（jalan tengah）を見事にまとめ上げました。",
                "note": "`mengambil jalan tengah`（中道・妥協案を採用する）と共起します。"
            },
            {
                "term": "jalan pikiran (pola pikir / logika)",
                "trans": "思考回路、物事の考え方の道筋、ロジック",
                "nuance": "ある結論に至るまでの内面的な論理展開や信念の構造を指し、「理解に苦しむ論理」を論評する際によく用いられます。",
                "ex_id": "Karya esai ilmiah yang baik harus memiliki jalan pikiran yang runtut, logis, dan mudah dipahami pembaca.",
                "ex_kana": "カルヤ エサイ イルミア ヤン バイク ハルス ムミリキ ジャラン ピキラン ヤン ルントゥット、ロギス、ダン ムダー ディパハミ プムバチャ",
                "ex_ja": "優れた学術エッセイは、理路整然とし論理的で、読者に理解しやすい思考の道筋（jalan pikiran）を持たねばなりません。",
                "note": "`runtut`（整然とした）という形容詞と相性抜群です。"
            }
        ],
        "dialogue": {
            "title": "労使紛争の長期化と和解の糸口模索",
            "lines": [
                ("Wawan", "Negosiasi upah minimum antara dewan pengupahan dan perwakilan buruh kemarin kabarnya menemui jalan buntu ya?"),
                ("Ratih", "Benar, Pak. Masing-masing pihak bersikeras pada angka tuntutan mereka tanpa mau mengalah."),
                ("Wawan", "Tidak boleh ada yang mengambil jalan pintas dengan aksi anarkis. Kita harus segera mencari jalan keluar yang damai."),
                ("Ratih", "Syukurlah pemerintah provinsi turun tangan menawarkan jalan tengah berupa subsidi transportasi.")
            ],
            "trans": [
                ("ワワン", "賃金審議会と労働者代表の間の最低賃金交渉、昨日暗礁に乗り上げた（menemui jalan buntu）らしいね？"),
                ("ラティ", "その通りです、部長。双方が一歩も譲らず、自らの要求額に固執しています。"),
                ("ワワン", "暴動のような安易な暴挙（jalan pintas）に出る者がいてはならない。平和的な打開策（jalan keluar）を至急探らねば。"),
                ("ラティ", "ありがたいことに、州政府が直接乗り出して（turun tangan）交通費補助という形の妥協案（jalan tengah）を提示してくれました。")
            ]
        },
        "grammar_points": [
            "**meN- 変化と自動詞・他動詞**: 語根 `jalan` は流音 `j` で始まります。接頭辞 `meN-` が付加されると `menjalani`（経験する・服役する）、`menjalankan`（動かす・実行する・職務を遂行する）となり、子音脱落は起きません（例: `menjalankan tugas`＝任務を遂行する）。",
            "**名詞化 perjalanan**: 接頭辞 `per-` と接尾辞 `-an` による `perjalanan` は、「旅・道程・プロセス」を意味し、`perjalanan dinas`（出張）、`perjalanan hidup`（人生の歩み）などを形成します。"
        ],
        "quizzes": [
            {
                "q": "「複雑な危機や紛争から脱出するための現実的な解決策・打開策」を意味する最も自然な表現はどれか。",
                "choices": ["jalan keluar", "jalan buntu", "jalan pintas", "jalan tol"],
                "ans": "jalan keluar",
                "expl": "解決策・打開策を表す連語は `jalan keluar` です。"
            },
            {
                "q": "「議論や交渉が双方の譲歩なしに進展せず、暗礁に乗り上げる・行き詰まる」を表す成句はどれか。",
                "choices": ["menemui jalan buntu", "mengambil jalan pintas", "mencari jalan keluar", "membuat jalan tol"],
                "ans": "menemui jalan buntu",
                "expl": "暗礁に乗り上げる、行き詰まりを迎えるは `menemui jalan buntu` です。"
            },
            {
                "q": "「対立する双方が極端な要求を引っ込め、中道・妥協案で合意すること」を表す表現はどれか。",
                "choices": ["mengambil jalan tengah", "mengambil alih kuasa", "pasang badan", "tutup usia"],
                "ans": "mengambil jalan tengah",
                "expl": "中道・妥協案を採用する表現は `mengambil jalan tengah` です。"
            }
        ],
        "culture_column": {
            "title": "「Jalan Tengah」とパンチャシラ中道精神の真髄",
            "body": "インドネシア国家の礎である「パンチャシラ（Pancasila）」は、西洋的個人主義（資本主義）と共産主義（全体主義）、あるいは世俗主義と宗教国家論の二項対立に陥ることなく、多様な民族・宗教が共存できるよう創出された究極の「Jalan Tengah（中道・妥協の道）」でした。この「調和を目指して極端を排する中道精神」は、政治だけでなくビジネス交渉や日常の近所付き合い（rukun tetangga）に至るまで、社会のあらゆるレベルで生きています。"
        }
    },
    {
        "filename": "docs/lexicon/16-noun-collocations-hati.md",
        "title": "【共起連語】身体名詞 hati の連語辞典：rendah hati / besar hati / patah hati / keras hati / hati kecil",
        "root": "hati",
        "meaning": "肝臓、心、感情、胸の内",
        "core_concept": "解剖学的な「肝臓（liver）」を指すと同時に、インドネシア語文化圏において情動・道徳・良心の座（中心）とみなされる最重要の身体メタファーです。謙虚さ、プライド、失恋、頑固さ、良心の呵責など、人間の内面世界の機微を余すところなく描写します。",
        "table_rows": [
            ("rendah hati", "低い心", "謙虚な、腰が低い、傲慢でない", "美徳/性格", "Meskipun sudah sukses dan kaya raya, pengusaha itu tetap rendah hati kepada siapa saja."),
            ("besar hati", "大きい心", "誇らしい、胸を張る、誇りに思う、（文脈により）潔く受け入れる", "感情/態度", "Orang tua itu sangat besar hati melihat putrinya berhasil meraih gelar doktor."),
            ("patah hati", "折れた心", "失恋する、傷心する、失意に沈む", "恋愛/心情", "Lagu balada melankolis ini mengisahkan kepedihan seseorang yang sedang patah hati."),
            ("keras hati", "硬い心", "頑固な、意志が固い、頑として譲らない", "性格/意志", "Sifatnya yang keras hati membuatnya sulit menerima kritik dan masukan dari orang lain."),
            ("hati kecil", "小さい心", "本心、良心、胸の奥底の微かな声", "内省/道徳", "Hati kecilnya selalu merasa bersalah setiap kali ia terpaksa berkata bohong."),
            ("jatuh hati", "心に落ちる", "心を奪われる、好意を寄せる、一目惚れする", "感情/好意", "Sejak pertama kali bertemu di perpustakaan, ia sudah jatuh hati kepada gadis itu."),
            ("lapang hati", "広い心", "寛大な、度量が広い、晴れやかな心持ち", "寛容/精神", "Kita harus menerima keputusan juri lomba ini dengan lapang hati dan jiwa ksatria.")
        ],
        "details": [
            {
                "term": "rendah hati (tawaduk / tidak sombong)",
                "trans": "謙虚な、腰が低い、慎み深い",
                "nuance": "社会的地位や富を得ても決していばり散らさず、他者に対して礼儀正しく敬意を払う人間の最高の美徳（kebajikan）を称える言葉です（※対義語の `tinggi hati`＝傲慢な、思い上がった）。",
                "ex_id": "Seorang ilmuwan sejati selalu bersikap rendah hati karena menyadari betapa luasnya samudra ilmu pengetahuan.",
                "ex_kana": "スオラン イルムワン スジャティ スラル ブルシカップ ルンダー ハティ カレナ ムニャダリ ベタパ ルアスニャ サムドラ イルム プンゲタフアン",
                "ex_ja": "真の科学者は、知識の大海原がいかに広大であるかを自覚しているため、常に謙虚な態度（rendah hati）を保ちます。",
                "note": "名詞形は `kerendahan hati`（謙虚さ）です。"
            },
            {
                "term": "besar hati (bangga / lapang dada menerima)",
                "trans": "誇らしい、胸を張る / 潔く受け入れる",
                "nuance": "第一義は親や指導者が仲間の偉業を見て「誇らしく思う（bangga）」感情。第二義では、敗北や挫折を恨まず「度量広く潔く受け止める（berlapang dada）」潔さを表します。",
                "ex_id": "Seluruh rakyat merasa besar hati ketika atlet bulu tangkis kita berhasil merebut medali emas Olimpiade.",
                "ex_kana": "スルルフ ラクヤット ムラサ ブサール ハティ クティカ アトレット ブル タンキス キタ ブルハシル ムルブット メダリ エマス オリンピアデ",
                "ex_ja": "バドミントン選手がオリンピックで金メダルを獲得した時、全国民が誇らしい気持ち（besar hati）で胸を満たしました。",
                "note": "文脈によって「誇り」と「潔い受容」の両方で機能します。"
            },
            {
                "term": "patah hati (kecewa berat dalam asmara)",
                "trans": "失恋する、恋に破れて傷心する",
                "nuance": "英語の「heartbroken」に直結し、ポップソング（lagu galau）の歌詞の9割に登場する大衆的かつ叙情的な表現です。",
                "ex_id": "Butuh waktu berbulan-bulan baginya untuk pulih dari rasa sakit akibat patah hati.",
                "ex_kana": "ブトゥ ワクトゥ ブルブランブラン バギニャ ウントゥッ プリッ ダリ ラサ サキット アクバット パター ハティ",
                "ex_ja": "失恋（patah hati）の痛みから彼が立ち直るには、何ヶ月もの時間が必要でした。",
                "note": "若者文化・ポピュラー音楽の超頻出キーワードです。"
            },
            {
                "term": "hati kecil (suara hati nurani)",
                "trans": "良心、本心、胸の奥底の真実の声",
                "nuance": "世間体や利害関係で取り繕った表層の言葉とは裏腹に、自分自身だけが知っている純粋な道徳的良心（nurani）を指します。",
                "ex_id": "Meskipun bibirnya tersenyum menyetujui, hati kecilnya berteriak menolak keputusan yang curang itu.",
                "ex_kana": "ムスキプン ビビルニャ トゥルスニュム ムニュトゥジュイ、ハティ クチルニャ ブルトゥリアッ ムノラッ クプトゥサン ヤン チュラン イトゥ",
                "ex_ja": "唇は笑って同意を示していたものの、彼の良心（hati kecil）はその不正な決定に対して拒絶の叫びを上げていました。",
                "note": "`suara hati kecil`（良心の声）という成句が定番です。"
            },
            {
                "term": "lapang hati / lapang dada (berjiwa besar)",
                "trans": "度量が広い、寛大な、心を開いて受け入れる",
                "nuance": "理不尽な批判や競技の敗北に直面しても、怒りや恨みを募らせず、清々しく寛容な精神で全てを受け止める大人の精神的成熟を表します。",
                "ex_id": "Kandidat yang kalah dalam pemilu tersebut mengucapkan selamat kepada pemenang dengan penuh lapang hati.",
                "ex_kana": "カンディダット ヤン カラー ダラム プミル トゥルスブット ムンウチャプカン スラマット クパダ プムナン ドゥンガン プヌー ラパン ハティ",
                "ex_ja": "選挙で敗れた候補者は、勝者に対して極めて寛大な心（lapang hati）をもって祝意を述べました。",
                "note": "民主主義の成熟を測る重要な態度表現です。"
            }
        ],
        "dialogue": {
            "title": "若手研究者の国際学会受賞と恩師の教え",
            "lines": [
                ("Prof. Anton", "Selamat atas penghargaan internasional yang kamu raih di Tokyo, Aris! Kami semua sangat besar hati."),
                ("Aris", "Terima kasih banyak, Prof. Penghargaan ini berkat bimbingan dan doa restu Prof Anton."),
                ("Prof. Anton", "Tetaplah rendah hati, Aris. Jangan biarkan pujian membuatmu sombong dan keras hati."),
                ("Aris", "Pasti, Prof. Hati kecil saya selalu mengingatkan bahwa ilmu ini adalah amanah untuk kemaslahatan umat.")
            ],
            "trans": [
                ("アントン教授", "東京での国際学会賞受賞、おめでとうアリス君！私たち研究室全員が本当に誇らしい気持ち（besar hati）だよ。"),
                ("アリス", "教授、本当にありがとうございます。この受賞は偏にアントン教授のご指導と温かいご支援のおかげです。"),
                ("アントン教授", "常に謙虚な心（rendah hati）を忘れぬことだ、アリス君。称賛の言葉で傲慢になったり頑固（keras hati）になったりしてはならんよ。"),
                ("アリス", "肝に銘じます、教授。この知識は人々の幸福のための預かり物（アマーナ）であると、私の良心（hati kecil）が常に戒めてくれています。")
            ]
        },
        "grammar_points": [
            "**hati と jantung の解剖学的・比喩的差異**: 解剖学的に `hati` は「肝臓（liver）」であり、「心臓（heart）」は `jantung` です。しかし感情・心情・良心の比喩には一貫して `hati` が用いられます（例: `sakit hati`＝心が痛む、悔しい）。物理的な心臓病は `penyakit jantung` と明確に区別されます。",
            "**接尾辞 -kan による使役動詞化**: `memperhatikan` は「注意する・配慮する」、`menghidupkan hati` は「心を生き返らせる」など、hati は派生動詞の基底としても豊富に機能します。"
        ],
        "quizzes": [
            {
                "q": "「大成功を収めても決して傲慢にならず、誰に対しても腰が低く礼儀正しい性格」を表す美徳の連語はどれか。",
                "choices": ["rendah hati", "tinggi hati", "keras hati", "patah hati"],
                "ans": "rendah hati",
                "expl": "謙虚な、腰が低い美徳を表す連語は `rendah hati` です。`tinggi hati` は傲慢な、思い上がったです。"
            },
            {
                "q": "インドネシア語で「失恋する、恋に敗れて傷心する」を意味するポピュラーな成句はどれか。",
                "choices": ["patah hati", "jatuh hati", "besar hati", "lapang hati"],
                "ans": "patah hati",
                "expl": "失恋するは `patah hati`（心が折れる）です。`jatuh hati` は好意を寄せるです。"
            },
            {
                "q": "「世間体を取り繕う言葉の裏にある、自分自身の偽らざる純粋な良心・本心」を指す表現はどれか。",
                "choices": ["hati kecil", "kaki lima", "tangan kanan", "mata angin"],
                "ans": "hati kecil",
                "expl": "良心や胸の奥底の微かな本心は `hati kecil` と言います。"
            }
        ],
        "culture_column": {
            "title": "なぜ「Heart」ではなく「Liver（肝臓）」が心の座なのか？",
            "body": "英語では愛や感情の中心は心臓（Heart）ですが、マレー・オーストロネシア語族の文化圏では古来、情動や精神の宿る器官は「肝臓（Hati）」と捉えられてきました。家畜を屠殺した際に最も大きく温かく血肉に富む肝臓こそが生命エネルギーの源泉であるという古代の身体観が反映されています。そのため「心が痛む」は `sakit hati`、「親切な人」は `baik hati` と、感情表現のほぼ全てが `hati` で紡がれるのです。"
        }
    },
    {
        "filename": "docs/lexicon/17-noun-collocations-kepala.md",
        "title": "【共起連語】身体名詞 kepala の連語辞典：kepala dingin / keras kepala / besar kepala / cuci kepala",
        "root": "kepala",
        "meaning": "頭、首脳、指導者、長、トップ",
        "core_concept": "人体の最上部に位置する「頭部」から、「組織の最高指導者（Kepala Negara, Kepala Sekolah）」「冷静沈着な理性」「頑固な強情さ」「思い上がったうぬぼれ」「洗脳・思想転向」という、理性・知性・プライド・権力構造の多角的メタファーを形成します。",
        "table_rows": [
            ("kepala dingin", "冷たい頭", "冷静な理性、沈着な判断、頭を冷やして", "理性/紛争解決", "Setiap permasalahan keluarga sebaiknya diselesaikan dengan kepala dingin tanpa emosi."),
            ("keras kepala", "硬い頭", "頑固な、強情な、人の忠告を聞かない", "性格/短所", "Anak itu sangat keras kepala dan selalu menolak jika disuruh minum obat."),
            ("besar kepala", "大きい頭", "うぬぼれた、天狗になった、高慢な", "性格/批判", "Pujian yang berlebihan dari media sosial justru membuatnya besar kepala dan lupa diri."),
            ("cuci kepala", "頭を洗う", "洗脳する、マインドコントロールする、思想改造する", "心理/社会問題", "Kelompok teroris menggunakan doktrin ekstrem untuk mencuci kepala para rekrutan baru."),
            ("sakit kepala / pusing kepala", "頭痛・めまいの頭", "頭痛がする、頭を悩ませる厄介な問題", "身体/比喩", "Kenaikan harga sewa toko yang mendadak membuat pedagang kecil sakit kepala."),
            ("kepala keluarga", "家族の頭", "世帯主、家長、家族を養う責任者", "社会/戸籍", "Sebagai kepala keluarga, ayah bekerja keras membanting tulang demi pendidikan anak-anaknya."),
            ("kepala batu", "石の頭", "救いようのない頑固者、石頭、石頭の頑迷さ", "口語/非難", "Sulit berdiskusi dengan orang kepala batu yang sama sekali tidak mau menerima fakta baru.")
        ],
        "details": [
            {
                "term": "kepala dingin (dengan tenang dan rasional)",
                "trans": "冷静沈着な理性、頭を冷やして、理性的態度",
                "nuance": "激高した感情や怒りに任せて衝動的な行動を取るのではなく、冷静に客観的事実を見つめて理性的に判断する大人の態度を促す最重要フレーズです。",
                "ex_id": "Mari kita duduk bersama dan membicarakan sengketa bisnis ini dengan kepala dingin.",
                "ex_kana": "マリ キタ ドゥドゥッ ブルサマ ダン ムンビチャラカン スンケタ ビスニス イニ ドゥンガン クパラ ディンギン",
                "ex_ja": "席を同じくして、このビジネス紛争について頭を冷やして冷静に（kepala dingin）話し合いましょう。",
                "note": "`dengan kepala dingin`（冷静に）という副詞句で頻出します。"
            },
            {
                "term": "keras kepala (bebal / membangkang)",
                "trans": "頑固な、強情な、融通が利かない",
                "nuance": "他者の善意の忠告や客観的なアドバイスに頑なに耳を塞ぎ、自らの誤った主張や行動に固執する頑迷さを批判的に描写します。",
                "ex_id": "Sikapnya yang keras kepala akhirnya merugikan diri sendiri ketika investasinya terbukti bodong.",
                "ex_kana": "シカップニャ ヤン クラス クパラ アヒルニャ メルギカン ディリ スンディリ クティカ インヴェスタシニャ トゥルブクティ ボドン",
                "ex_ja": "彼の頑固な（keras kepala）態度は、投資話が詐欺であると証明された時に結局自分自身の損失となって跳ね返ってきました。",
                "note": "さらに強調した罵倒表現に `kepala batu`（石頭）があります。"
            },
            {
                "term": "besar kepala (sombong / tinggi hati)",
                "trans": "うぬぼれた、天狗になった、思い上がった",
                "nuance": "称賛や一時的な成功によって自惚れ、周囲を見下して傲慢な態度を取るようになった人間を戒める表現です（※先述の `besar hati`＝誇らしい、と混同注意）。",
                "ex_id": "Jangan lekas besar kepala hanya karena memenangkan kejuaraan tingkat kota sekali saja.",
                "ex_kana": "ジャンガン ルカス ブサール クパラ ハニャ カレナ ムムナンカン クジュアラアン ティンカット コタ スカリ サジャ",
                "ex_ja": "市大会で一度優勝したくらいで、すぐに天狗になってうぬぼれる（besar kepala）な。",
                "note": "`besar hati`（誇りに思う）との対比・識別が学習者の最重要ポイントです。"
            },
            {
                "term": "cuci kepala (cuci otak / indoktrinasi)",
                "trans": "洗脳する、マインドコントロールを施す",
                "nuance": "カルト宗教、過激派組織、悪質なマルチ商法などが、巧妙な心理的誘導を用いて個人の批判的思考力を奪い、特定のドグマを植え付ける犯罪的行為を指します。",
                "ex_id": "Badan Intelijen Negara memperingatkan orang tua agar waspada terhadap upaya cuci kepala pada remaja.",
                "ex_kana": "バダン インテリジェン ネガラ ムムプルインガットカン オラン トゥア アガル ワスパダ トゥルハダップ ウパヤ チュチ クパラ パダ ルマジャ",
                "ex_ja": "国家情報庁は保護者に対し、若者たちに対する洗脳（cuci kepala / cuci otak）の企てに警戒するよう呼びかけました。",
                "note": "`cuci otak`（洗脳）と互換的に使われます。"
            },
            {
                "term": "kepala keluarga (penanggung jawab rumah tangga)",
                "trans": "世帯主、家長、一家の責任者",
                "nuance": "公的文書（住民登録証 KTP、家族カード Kartu Keluarga）の公式用語であると同時に、家族全員の衣食住と教育を一身に背負って支える大黒柱への敬意を含む言葉です。",
                "ex_id": "Di masa krisis, para kepala keluarga dituntut lebih kreatif dalam mencari nafkah tambahan.",
                "ex_kana": "ディ マサ クリシス、パラ クパラ クルアルガ ディトゥントゥット レビ クレアティフ ダラム ムンチャリ ナフカ タンバハン",
                "ex_ja": "危機の時代において、世帯主（kepala keluarga）たちは副収入の糧を模索するためにより創造的であることが求められています。",
                "note": "行政・社会保障の必須公的用語です。"
            }
        ],
        "dialogue": {
            "title": "若手スター選手の傲慢と監督の指導",
            "lines": [
                ("Pelatih Joko", "Romi, kamu bermain bagus semalam, tetapi saya perhatikan kamu mulai besar kepala di hadapan rekan setim."),
                ("Romi", "Maaf, Coach. Saya tidak bermaksud sombong, saya hanya percaya diri."),
                ("Pelatih Joko", "Percaya diri itu baik, tetapi kalau terlalu keras kepala dan mengabaikan taktik tim, kamu justru akan merusak permainan."),
                ("Romi", "Baik, Coach. Saya akan dinginkan kepala dan kembali fokus bermain demi kemenangan tim.")
            ],
            "trans": [
                ("ジョコ監督", "ロミ、昨夜のプレーは見事だったが、チームメイトの前で少し天狗になって（besar kepala）いないか。"),
                ("ロミ", "すみません、監督。傲慢になるつもりは決してなく、ただ自信があっただけなんです。"),
                ("ジョコ監督", "自信を持つのは良いことだ。だが頑固（keras kepala）になってチーム戦術を軽視すれば、試合を壊してしまうぞ。"),
                ("ロミ", "わかりました、監督。頭を冷やし（dinginkan kepala）、チームの勝利のために再び集中してプレーします。")
            ]
        },
        "grammar_points": [
            "**besar hati vs besar kepala の超重要識別**: \n- `besar hati`: 心（hati）が大きい ＝「誇らしい、胸を張る（bangga）」「潔く受け止める（berlapang dada）」（ポジティブ）\n- `besar kepala`: 頭（kepala）が大きい ＝「天狗になる、うぬぼれる（sombong）」（ネガティブ批判）\n検定試験や日常会話で最も引っかかりやすい最頻出トラップです。",
            "**kepala による組織の長**: `kepala sekolah`（校長）、`kepala kantor`（所長）、`kepala daerah`（地方首長）、`kepala desa`（村長）のように、名詞修飾で「組織・地域のトップ」を形成します。"
        ],
        "quizzes": [
            {
                "q": "「称賛や成功に酔いしれて天狗になり、思い上がって傲慢になる」を意味する身体連語はどれか。",
                "choices": ["besar kepala", "besar hati", "rendah hati", "kepala dingin"],
                "ans": "besar kepala",
                "expl": "天狗になる、うぬぼれる意味の表現は `besar kepala` です。`besar hati` は誇りに思う、です。"
            },
            {
                "q": "「激高した感情を抑え、冷静沈着な理性をもって対立を解決する」を意味する成句はどれか。",
                "choices": ["dengan kepala dingin", "dengan keras kepala", "dengan kepala batu", "dengan sakit kepala"],
                "ans": "dengan kepala dingin",
                "expl": "冷静沈着に、頭を冷やして物事を解決する態度は `dengan kepala dingin` です。"
            },
            {
                "q": "公的文書（Kartu Keluarga等）において「世帯主、一家の大黒柱」を表す正式な用語はどれか。",
                "choices": ["kepala keluarga", "kepala batu", "kepala dingin", "tangan kanan"],
                "ans": "kepala keluarga",
                "expl": "世帯主・家長を意味する公的用語は `kepala keluarga` です。"
            }
        ],
        "culture_column": {
            "title": "頭部（Kepala）の神聖性と東南アジアのマナー",
            "body": "インドネシアをはじめとする東南アジア社会において、頭部（kepala）は人間の霊魂（semangat）が宿る最も神聖な部位とみなされています。そのため、いくら親しい間柄や愛らしい子どもであっても、他人の頭を気軽に手で触ったり撫でたりすることは重大な無礼（kurang ajar）とみなされます。身体的にも象徴的にも「最上位の不可侵領域」である頭部の神聖観が、言語表現の敬意や威厳の基盤となっているのです。"
        }
    },
    {
        "filename": "docs/lexicon/18-noun-collocations-mata.md",
        "title": "【共起連語】身体名詞 mata の連語辞典：mata rantai / mata air / mata angin / mata pencaharian / mata-mata",
        "root": "mata",
        "meaning": "目、視力、中心点、源泉、要所",
        "core_concept": "光を捉える感覚器官「目」から、「環状構造の結び目（リンク）」「清らかな湧き水（水脈の目）」「方位（風の目）」「生計を立てる手段（生計の目）」「密かに潜入するスパイ」という、連結点・中心源泉・方位観の豊かなメタファーを構築します。",
        "table_rows": [
            ("mata rantai", "鎖の目", "連鎖、輪、リンク、連結環", "科学/歴史", "Fosil manusia purba ini menjadi mata rantai penting dalam evolusi kepulauan Nusantara."),
            ("mata air", "水の目", "湧き水、水源、泉、源泉", "自然/環境", "Masyarakat desa menjaga kelestarian hutan lindung demi melindungi mata air bersih."),
            ("mata angin", "風の目", "方位、方角、羅針盤（東・西・南・北）", "航海/地理", "Pelaut tradisional Bugis mahir membaca arah mata angin menggunakan rasi bintang."),
            ("mata pencaharian", "稼ぎの目", "生計、生業、職業、日々の稼ぎの手立て", "経済/社会", "Sebagian besar penduduk pesisir menggantungkan mata pencaharian pada sektor perikanan."),
            ("mata-mata", "目・目", "スパイ、秘密諜報員、密偵、工作員", "治安/国際", "Aparat intelijen berhasil membongkar jaringan mata-mata asing di ibu kota."),
            ("mata pelajaran / mata kuliah", "学びの目", "教科、科目 / 大学の講義科目", "教育/学術", "Matematika dan Bahasa Indonesia merupakan mata pelajaran wajib di sekolah dasar."),
            ("mata uang", "お金の目", "通貨、貨幣（Rupiah, Yen, Dolar）", "金融/経済", "Nilai tukar mata uang rupiah terhadap dolar AS mengalami penguatan tipis pagi ini.")
        ],
        "details": [
            {
                "term": "mata rantai (unsur penghubung yang tak terputus)",
                "trans": "連鎖、連結環、リンク、重要な結び目",
                "nuance": "歴史の因果関係、サプライチェーン（rantai pasok）、食物連鎖（rantai makanan）、生物進化の「ミッシングリンク（mata rantai yang hilang）」など、全体をつなぐ欠かせない環を指します。",
                "ex_id": "Usaha mikro merupakan mata rantai yang sangat penting dalam rantai pasok industri nasional.",
                "ex_kana": "ウサハ ミクロ ムルパカン マタ ランタイ ヤン サンガット プンティン ダラム ランタイ パソッ インドゥストリ ナシオナル",
                "ex_ja": "零細企業は、国家産業のサプライチェーンにおいて極めて重要な連結環（mata rantai）となっています。",
                "note": "論理的一貫性や因果関係の鎖を描写する際にも用いられます。"
            },
            {
                "term": "mata air (sumber air alami)",
                "trans": "湧き水、水源、泉、源泉",
                "nuance": "大地から滾々と湧き出る清らかな清水の湧出口を指します。比喩として「インスピレーションの源泉」「知識の泉」としても美しく詩的に用いられます。",
                "ex_id": "Kearifan lokal masyarakat adat melarang penebangan pohon di radius seratus meter dari mata air.",
                "ex_kana": "ケアリファン ロカル マシャラカット アダット ムララン プヌバンガン ポホン ディ ラディウス スラトゥス メテル ダリ マタ アイル",
                "ex_ja": "先住民族の伝統的知恵は、水源（mata air）から半径100メートルの樹木の伐採を禁じています。",
                "note": "環境保全の文脈で極めて重要な語彙です。"
            },
            {
                "term": "mata angin (arah kompas)",
                "trans": "方位、方角（timur, barat, selatan, utara）",
                "nuance": "直訳は「風の目」。航海民族であるインドネシア諸民族が、モンスーンの風向と星の運行を読み解いて海洋交易路を切り拓いてきた歴史を物語る方位表現です。",
                "ex_id": "Kompas navigasi ini memuat penunjuk delapan arah mata angin utama secara akurat.",
                "ex_kana": "コンパス ナヴィガシ イニ ムムアット プヌンジュッ ドゥラパン アラー マタ アンギン ウタマ スチャラ アクラット",
                "ex_ja": "この航法コンパスには、主要な8方位の方角（mata angin）が正確に表示されています。",
                "note": "`delapan arah mata angin`（主要8方位）は学校教育の必須基礎知識です。"
            },
            {
                "term": "mata pencaharian (pekerjaan utama untuk hidup)",
                "trans": "生計、生業、職業、生計の手段",
                "nuance": "単なる一時的なアルバイトではなく、自らと家族の命を養い存続させるための主たる生計の手立てを表す、社会学・人類学の格調高い基本語彙です。",
                "ex_id": "Alih fungsi lahan pertanian menjadi kawasan industri telah mengancam mata pencaharian para petani gurem.",
                "ex_kana": "アリフ フンシ ラハン プルタニアン ムンジャディ カワサン インドゥストリ トゥラー ムンガンチャム マタ プンチャハリアン パラ プタニ グレム",
                "ex_ja": "農地の工業団地への転用は、零細農民たちの生計（mata pencaharian）を直接的に脅かしています。",
                "note": "`sumber mata pencaharian`（生計の源泉）の形で多用されます。"
            },
            {
                "term": "mata-mata (spionase / agen rahasia)",
                "trans": "スパイ、秘密工作員、密偵",
                "nuance": "畳語によって「常に四方八方に目を光らせて情報を収集する者」を表す、スパイ・諜報機関の定番の呼称です。",
                "ex_id": "Film thriller ini menceritakan petualangan seorang mata-mata yang menyamar sebagai jurnalis asing.",
                "ex_kana": "フィルム スリラー イニ ムンチュリタカン プトゥアランガン スオラン マタマタ ヤン ムニャマル スバガイ ジュルナリス アシン",
                "ex_ja": "そのサスペンス映画は、外国人ジャーナリストに偽装したスパイ（mata-mata）の冒険を描いています。",
                "note": "動詞形は `memata-matai`（密かに監視・偵察する）となります。"
            }
        ],
        "dialogue": {
            "title": "水源保全プロジェクトと村人の生計",
            "lines": [
                ("Pak Kades", "Kita harus memperketat aturan desa agar hutan lindung di bukit utara tidak dirusak oleh penambang liar."),
                ("Ibu Sekdes", "Benar, Pak Kades. Hutan itu menyimpan mata air utama yang mengaliri sawah dan air minum warga."),
                ("Pak Kades", "Jika mata air itu kering, seluruh mata pencaharian petani di lima dusun akan hancur seketika."),
                ("Ibu Sekdes", "Mari kita pasang pos jaga dan tugaskan pemuda untuk memata-matai gerak-gerik pihak luar yang mencurigakan.")
            ],
            "trans": [
                ("村長", "北の丘にある保護林が不法採掘業者に荒らされないよう、村の規則を厳格化せねばならない。"),
                ("副村長", "その通りです、村長。あの森林には、水田と住民の飲料水を潤す主要な水源（mata air）が眠っています。"),
                ("村長", "もしあの水源が枯れてしまえば、5つの集落の農民たちの生計（mata pencaharian）は一瞬で壊滅してしまう。"),
                ("副村長", "監視所を設置し、青年団に怪しい外部の動きを偵察・監視（memata-matai）させましょう。")
            ]
        },
        "grammar_points": [
            "**mata による複合名詞の形成力**: `mata` は単体で「目」ですが、他の名詞と結びついて「核心・源泉・要所」を指す複合語を無限に生み出します（例: `mata pisau`＝刃先、`mata panah`＝矢じり、`mata kuliah`＝大学の履修科目）。",
            "**他動詞 memata-matai**: 畳語名詞 `mata-mata`（スパイ）に他動詞接尾辞 `-i` が付いた `memata-matai` は、「〜を密かに偵察・監視する」という正式な他動詞となります。"
        ],
        "quizzes": [
            {
                "q": "「自然の大地から滾々と湧き出る清らかな水源・湧き水」を意味する複合名詞はどれか。",
                "choices": ["mata air", "mata angin", "mata rantai", "mata uang"],
                "ans": "mata air",
                "expl": "水源・湧き水は `mata air` です。`mata angin` は方位、`mata rantai` は連鎖、`mata uang` は通貨です。"
            },
            {
                "q": "社会学や経済の文脈で「人間が日々生活を営み家族を養うための主たる生計・生業」を意味する専門語彙はどれか。",
                "choices": ["mata pencaharian", "mata pelajaran", "mata-mata", "mata kaki"],
                "ans": "mata pencaharian",
                "expl": "生計・生業は `mata pencaharian` です。"
            },
            {
                "q": "歴史や進化論において「全体をつなぐ欠くことのできない重要な連結環・連鎖」を意味する成句はどれか。",
                "choices": ["mata rantai", "jalan keluar", "pasang badan", "buah tangan"],
                "ans": "mata rantai",
                "expl": "連結環、鎖の輪、ミッシングリンクなどの比喩は `mata rantai` です。"
            }
        ],
        "culture_column": {
            "title": "「Mata Angin」とブギス族の星辰航海術",
            "body": "スラウェシ島の誇り高き海洋民族ブギス族（Suku Bugis）は、近代的な羅針盤が登場する遥か以前から、伝統的な帆船ピニシ（Pinisi）を駆ってインド洋からオーストラリア北岸に至る広大な海域を踏破しました。彼らにとって `mata angin`（風の目）は単なる東西南北の方位記号ではなく、モンスーンの湿り気、波のうねり、夜空の南十字星（Salib Selatan）の輝きと一体化した、生と死を分かつ神聖な海洋知の結晶だったのです。"
        }
    },
    {
        "filename": "docs/lexicon/19-noun-collocations-tangan.md",
        "title": "【共起連語】身体名詞 tangan の連語辞典：tangan kanan / cuci tangan / campur tangan / angkat tangan / buah tangan",
        "root": "tangan",
        "meaning": "手、腕、権力、介入、関与",
        "core_concept": "物を掴み作業を行う最も能動的な身体器官「手」から、「最も信頼する右腕・懐刀」「自らの責任を回避する（手を洗う）」「他者の領域に介入・干渉する」「降伏・お手上げになる」「旅の土産（手が生み出した果実）」という、権力関係・責任・社交の多彩なメタファーを形成します。",
        "table_rows": [
            ("tangan kanan", "右手", "右腕、腹心、懐刀、最も信頼する補佐役", "人事/ビジネス", "Manajer itu sangat mempercayai sekretarisnya sebagai tangan kanan dalam mengelola divisi."),
            ("cuci tangan", "手を洗う", "責任逃れをする、自分は無関係だと主張する、手を引く", "非難/慣用", "Tersangka korupsi itu mencoba cuci tangan dan melemparkan kesalahan kepada bawahannya."),
            ("campur tangan", "手が混ざる", "干渉する、介入する、おせっかいを焼く", "政治/外交", "Pemerintah menolak keras segala bentuk campur tangan asing dalam urusan dalam negeri."),
            ("angkat tangan", "手を挙げる", "降伏する、お手上げになる、ギブアップする", "日常/比喩", "Setelah mencoba berbagai metode perbaikan, teknisi itu akhirnya angkat tangan dan menyerah."),
            ("buah tangan", "手の果実", "お土産、手土産、旅の贈り物", "社交/文化", "Jangan lupa membawa buah tangan khas Yogyakarta berupa bakpia untuk teman-teman kantor."),
            ("turun tangan", "手を降ろす", "自ら直接乗り出す、直接介入して収拾を図る", "指導力/政治", "Melihat mediasi buntu, menteri tenaga kerja memutuskan turun tangan langsung."),
            ("lepas tangan", "手を放す", "無責任に職務を放棄する、知らぬ顔をする", "道徳/批判", "Pihak rumah sakit tidak boleh lepas tangan atas insiden malapraktik tersebut.")
        ],
        "details": [
            {
                "term": "tangan kanan (orang kepercayaan utama)",
                "trans": "右腕、腹心、懐刀、最も頼りになる側近",
                "nuance": "大統領の首席補佐官、企業オーナーの専務など、意思決定を補佐し機密を共有する絶対的信頼を置かれたナンバーツーを指す定番表現です。",
                "ex_id": "Sejak awal merintis perusahaan, Budi selalu menjadi tangan kanan yang paling setia bagi sang direktur utama.",
                "ex_kana": "スジャッ アワル ムリンティス プルサハアン、ブディ スラル ムンジャディ タンガン カナン ヤン パリン スティア バギ サン ディレクトゥル ウタマ",
                "ex_ja": "会社創業の当初から、ブディは常に代表取締役にとって最も忠実な右腕（tangan kanan）であり続けました。",
                "note": "英語の「right-hand man」と完全に一致します。"
            },
            {
                "term": "cuci tangan (berlepas diri dari tanggung jawab)",
                "trans": "責任逃れをする、知らぬ顔をする、手を洗う",
                "nuance": "聖書でイエスを処刑に引き渡したピラトが群衆の前で手を洗った故事にも通じる、「自分には過失も責任もない」と都合よく逃走を図る態度への厳しい糾弾です。",
                "ex_id": "Masyarakat mengecam pejabat yang mencoba cuci tangan atas kegagalan proyek infrastruktur mangkrak tersebut.",
                "ex_kana": "マシャラカット ムンゲチャム プジャバット ヤン ムンチョバ チュチ タンガン アタス クガガラン プロイェッ インフラストルクトゥル マンクラッ トゥルスブット",
                "ex_ja": "世間は、放置されたインフラプロジェクトの失敗について責任逃れ（cuci tangan）を図ろうとする高官を激しく非難しました。",
                "note": "`lepas tangan` とほぼ同義ですが、より「潔白を装う狡猾さ」が強調されます。"
            },
            {
                "term": "campur tangan (mengintervensi urusan orang lain)",
                "trans": "内政干渉する、介入する、口出しする",
                "nuance": "外交関係における「内政干渉（campur tangan urusan internal）」から、親戚が他人の家庭問題に不当に口を出すことまで、不要な干渉を排斥する文脈で使われます。",
                "ex_id": "Setiap negara berdaulat berhak menentukan nasibnya sendiri tanpa campur tangan kekuatan militer asing.",
                "ex_kana": "スティアップ ネガラ ブルダウラット ブルハッ ムヌントゥカン ナシブニャ スンディリ タンパ チャンプル タンガン ククアタン ミリテル アシン",
                "ex_ja": "すべての主権国家は、外国の軍事力の干渉（campur tangan）を受けることなく自らの運命を決定する権利を有しています。",
                "note": "動詞形は `mencampurtangani` と一語化されます。"
            },
            {
                "term": "angkat tangan (menyerah kalah / pasrah)",
                "trans": "降伏する、お手上げになる、ギブアップする",
                "nuance": "犯人が警察に包囲されて「両手を挙げる」物理動作から転じ、難問の解決や病気の治療が不可能で「万策尽きて白旗を上げる」無力感を表します。",
                "ex_id": "Dokter spesialis terbaik pun sudah angkat tangan menghadapi penyakit komplikasi langka tersebut.",
                "ex_kana": "ドクテル スペシアリス トゥルバイク プン スダ アンカット タンガン ムンハダピ プニャキット コンプリカシ ランカ トゥルスブット",
                "ex_ja": "最高の専門医たちでさえ、その希少な合併症を前にお手上げ（angkat tangan / 匙を投げる）状態でした。",
                "note": "「匙を投げる」に相当するニュアンスです。"
            },
            {
                "term": "buah tangan (oleh-oleh / cenderamata)",
                "trans": "お土産、手土産、旅のギフト",
                "nuance": "`oleh-oleh` の少し改まった文学的・社交的な表現で、旅先や出張先から親しい同僚や家族のために選んできた手土産を温かく指します。",
                "ex_id": "Kepulangan paman dari lawatan ke luar negeri selalu dinanti anak-anak karena membawa banyak buah tangan.",
                "ex_kana": "クプランガン パマン ダリ ラワタン ケ ルアル ネグリ スラル ディナンティ アナッアナッ カレナ ムンバワ バニャッ ブア タンガン",
                "ex_ja": "叔父の海外訪問からの帰国は、たくさんのお土産（buah tangan）を持ち帰ってくれるため、子どもたちにいつも心待ちにされています。",
                "note": "社交マナーとして好まれる美しい語彙です。"
            }
        ],
        "dialogue": {
            "title": "海外出張の帰還と社内の権力抗争",
            "lines": [
                ("Wira", "Selamat datang kembali dari dinas ke Jerman, Pak Harto! Bagaimana hasil perundingannya?"),
                ("Pak Harto", "Lancar, Wira. Ini ada sedikit buah tangan cokelat khas Berlin untuk dinikmati tim."),
                ("Wira", "Wah, terima kasih banyak, Pak! Oya, selama Bapak pergi, manajer divisi lain sempat mencoba campur tangan dalam proyek kita."),
                ("Pak Harto", "Tenang saja. Sebagai tangan kanan saya, kamu sudah menangani semuanya dengan tepat. Mereka tidak bisa cuci tangan begitu saja nanti.")
            ],
            "trans": [
                ("ウィラ", "ハルト部長、ドイツ出張からのご帰国お疲れ様でした！交渉の結果はいかがでしたか？"),
                ("ハルト部長", "順調だったよ、ウィラ君。これはチームの皆で食べてほしいベルリン特産のお土産（buah tangan）のチョコレートだよ。"),
                ("ウィラ", "わあ、ありがとうございます！ところで部長のご不在中、他部署のマネージャーが私たちのプロジェクトに不当に干渉（campur tangan）しようとしてきました。"),
                ("ハルト部長", "心配いらないよ。私の頼れる右腕（tangan kanan）として、君が的確に対処してくれた。彼らも後から知らぬ顔で責任逃れ（cuci tangan）することはできないさ。")
            ]
        },
        "grammar_points": [
            "**campur tangan の派生複合動詞**: `campur tangan` に他動詞接頭辞 `meN-` と接尾辞 `-i` が付加されると、全体が連結して `mencampurtangani`（〜に不当に干渉する）という1語の他動詞になります（※EYD規則により分かち書きが解消されます）。",
            "**buah を冠する比喩表現群**: `buah tangan`（お土産）と同様に、`buah bibir`（噂の種・話題の的）、`buah hati`（愛児・最愛の恋人）、`buah pikiran`（アイデア・所思）など、`buah`＋身体部位はインドネシア語の詩的造語の宝庫です。"
        ],
        "quizzes": [
            {
                "q": "「リーダーや経営者にとって最も信頼のおけるナンバーツーの腹心・懐刀」を意味する身体連語はどれか。",
                "choices": ["tangan kanan", "kaki lima", "kepala dingin", "mata air"],
                "ans": "tangan kanan",
                "expl": "最も信頼する右腕・腹心は `tangan kanan` です。"
            },
            {
                "q": "「不祥事や失敗が発生した際、自分は潔白で無関係であると主張して責任逃れをする」態度を表す成句はどれか。",
                "choices": ["cuci tangan", "angkat tangan", "buah tangan", "campur tangan"],
                "ans": "cuci tangan",
                "expl": "責任逃れをして知らぬ顔をすることは `cuci tangan` です。"
            },
            {
                "q": "旅先や出張先から家族や同僚に持ち帰る「お土産・手土産」を表す丁寧で格調高い表現はどれか。",
                "choices": ["buah tangan", "buah bibir", "buah hati", "buah dada"],
                "ans": "buah tangan",
                "expl": "お土産・手土産は `buah tangan`（または日常語で `oleh-oleh`）です。"
            }
        ],
        "culture_column": {
            "title": "「Oleh-oleh」と「Buah Tangan」にみるインドネシアの分かち合い精神",
            "body": "インドネシア人が旅行や出張に出かける際、最も強い社会的プレッシャーであり同時に喜びでもあるのが `oleh-oleh`（buah tangan）の調達です。帰国や帰省時に手土産を持たずに戻ることは「情の薄いケチな人間」とみなされかねません。旅の果実（buah）を共同体のみんなで分かち合い、無事に帰還できた感謝を神と仲間に捧げる「バギ・バギ（bagi-bagi / 分配）」の温かな精神文化がここに息づいています。"
        }
    },
    {
        "filename": "docs/lexicon/20-noun-collocations-kaki.md",
        "title": "【共起連語】身体名詞 kaki の連語辞典：kaki lima / kaki tangan / angkat kaki / cuci kaki / mata kaki",
        "root": "kaki",
        "meaning": "足、脚、歩行、土台、手先",
        "core_concept": "大地を踏みしめ移動を支える最下部の器官「足」から、「歩道の屋台商人（5フィートの歩道空間）」「悪事の手先・手下」「その場から立ち退く・逃亡する」「足を洗って就寝する」「くるぶし」という、都市空間・手下・退去の独特な語彙世界を構成します。",
        "table_rows": [
            ("kaki lima (PKL)", "5つの足", "歩道の屋台、露店商、歩道スペース（5フィート）", "大衆文化/都市", "Pemerintah kota menata pedagang kaki lima agar tidak mengganggu pejalan kaki."),
            ("kaki tangan", "足と手", "手下、手先、配下、手先となって悪事を働く者", "犯罪/批判", "Polisi berhasil meringkus gembong narkoba beserta lima orang kaki tangannya."),
            ("angkat kaki", "足を持ち上げる", "立ち去る、立ち退く、退去する、逃亡する", "行動/退去", "Penyewa rumah yang menunggak sewa itu akhirnya dipaksa angkat kaki oleh pemilik."),
            ("cuci kaki", "足を洗う", "足を洗って清潔にする、（民俗的に）身を清めて休む", "衛生/習慣", "Ibu selalu mengingatkan kami untuk cuci kaki dan cuci tangan sebelum tidur."),
            ("mata kaki", "足の目", "くるぶし（足首の内側・外側の骨の突起）", "解剖/身体", "Pemain sepak bola itu mengalami cedera pada bagian mata kaki setelah ditekel lawan."),
            ("kaki langit", "空の足", "地平線、水平線、空と大地の境界", "自然/詩的", "Matahari terbenam perlahan di balik kaki langit barat memancarkan warna jingga keemasan."),
            ("kaki bukit / kaki gunung", "丘・山の足", "麓（ふもと）、山麓、丘陵の下部", "地理/地形", "Sebuah desa wisata yang asri terletak tepat di kaki bukit Gunung Merapi.")
        ],
        "details": [
            {
                "term": "kaki lima / Pedagang Kaki Lima (PKL)",
                "trans": "屋台、露店商、歩道の屋台街",
                "nuance": "英領マラッカ海峡植民地時代、ラッフルズが定めた「建物の前の歩道幅は5フィート（約1.5メートル）確保せよ」という都市計画令に由来し、現代では歩道を埋め尽くす屋台商人全般を指します。",
                "ex_id": "Kawasan Malioboro di Yogyakarta terkenal dengan kuliner kaki lima yang menyajikan gudeg lezat.",
                "ex_kana": "カワサン マリオボロ ディ ジョグジャカルタ トゥルクナル ドゥンガン クリネル カキ リマ ヤン ムニャジカン グデグ レザット",
                "ex_ja": "ジョグジャカルタのマリオボロ通りは、美味しいグドゥグを提供する屋台グルメ（kaki lima）で有名です。",
                "note": "露店商人は略称 `PKL`（ペー・カー・エル）として公的文書でも定着しています。"
            },
            {
                "term": "kaki tangan (antek / anak buah pelaku kejahatan)",
                "trans": "手下、手先、配下、悪事の実行犯たち",
                "nuance": "犯罪組織のボス（gembong）の命令に従って汚い仕事を現場で実行する配下のチンピラや手下を指す、強い軽蔑を込めた言葉です。",
                "ex_id": "Bos mafia perjudian itu melarikan diri ke luar negeri sementara kaki tangannya ditangkap polisi.",
                "ex_kana": "ボス マフィア プルジュディアン イトゥ ムラリカン ディリ ケ ルアル ネグリ スマンタラ カキ タンガンニャ ディタンカップ ポリシ",
                "ex_ja": "賭博マフィアの首領は海外へ逃亡したものの、彼の手下たち（kaki tangan）は警察に逮捕されました。",
                "note": "否定的な文脈（犯罪・汚職・不正）に限定して用いられます。"
            },
            {
                "term": "angkat kaki (pergi meninggalkan tempat / minggat)",
                "trans": "立ち退く、退去する、去る、逃げ出す",
                "nuance": "不満、強制立ち退き、契約終了などの理由で、その土地や家、職場から荷物をまとめて立ち去る行動を表します。",
                "ex_id": "Investor asing mengancam akan angkat kaki dari negara ini jika regulasi ketenagakerjaan tidak memberikan kepastian hukum.",
                "ex_kana": "インヴェストール アシン ムンガンチャム アカン アンカット カキ ダリ ネガラ イニ ジュカ レグラシ クテナガケルジャアン ティダッ ムンブリカン クパスティアン フクム",
                "ex_ja": "外国人投資家たちは、労働法規制が法的確実性を提供しない場合、この国から資本を引き揚げて立ち去る（angkat kaki）と威嚇しました。",
                "note": "企業の撤退やテナントの退去で多用されます。"
            },
            {
                "term": "mata kaki (mata buku lali)",
                "trans": "くるぶし（踝）",
                "nuance": "解剖学的な「くるぶし」を指す標準語です。イスラム法において男性が裾の長いズボンを着用する際「くるぶしの上まで裾を上げる（isbal の回避）」という宗教的議論でも頻出します。",
                "ex_id": "Celana panjang yang dikenakannya sedikit menggantung di atas mata kaki.",
                "ex_kana": "チェラナ パンジャン ヤン ディクナカンニャ スディキット ムングントゥン ディ アタス マタ カキ",
                "ex_ja": "彼が穿いている長ズボンは、くるぶし（mata kaki）の少し上の位置で短めに丈がとられています。",
                "note": "日常の怪我やファッションでも使われる基礎解剖語彙です。"
            },
            {
                "term": "kaki bukit / kaki gunung",
                "trans": "麓（ふもと）、山麓",
                "nuance": "地形の最下部を表す自然表現です。「Kaki langit（地平線・空の足）」と並び、自然景観を生き物のように捉える豊かな比喩です。",
                "ex_id": "Resor peristirahatan ini dibangun di kaki gunung dengan pemandangan kebun teh yang menyejukkan mata.",
                "ex_kana": "レソール プリスティラハタン イニ ディバングン ディ カキ グヌン ドゥンガン プマンダンガン クブン テ ヤン ムニェジュッカン マタ",
                "ex_ja": "この保養リゾートホテルは山麓（kaki gunung）に建設され、目を休ませてくれる茶畑の絶景が広がっています。",
                "note": "観光案内や地理解説で頻出します。"
            }
        ],
        "dialogue": {
            "title": "繁華街の歩道整備と露店商の移転問題",
            "lines": [
                ("Satpol PP", "Bapak-bapak pedagang kaki lima, sesuai instruksi wali kota, area trotoar ini harus steril dari lapak jualan."),
                ("Pak Joko", "Tolong beri kami waktu, Pak. Kalau kami dipaksa angkat kaki sekarang, anak istri kami mau makan apa?"),
                ("Satpol PP", "Pemerintah tidak mengusir tanpa solusi, Pak. Semua PKL sudah disediakan kios gratis di pasar relokasi."),
                ("Pak Joko", "Syukurlah kalau begitu. Kami khawatir ada oknum preman yang menjadi kaki tangan mafia pasar gelap.")
            ],
            "trans": [
                ("治安維持隊員", "露店商（pedagang kaki lima）の皆さん、市長の指示に基づき、この歩道エリアは屋台を撤去して歩行者専用としなければなりません。"),
                ("ジョコさん", "どうか猶予をください。今すぐ立ち退く（angkat kaki）よう強制されたら、妻子は何を食べていけばいいのですか？"),
                ("治安維持隊員", "打開策なしに追い出すわけではありませんよ。全PKL向けに移転先市場の無料屋台ブースが用意されています。"),
                ("ジョコさん", "それなら安心しました。闇市場マフィアの手下（kaki tangan）である暴力団員に騙されるのではないかと不安だったのです。")
            ]
        },
        "grammar_points": [
            "**PKL という略語の文法性**: `pedagang kaki lima` は日常会話や新聞報道でほぼ100% `PKL`（ペー・カー・エル）と略称されます。複数形にする場合は `para PKL`（露店商たち）と冠詞 `para` を付けます。",
            "**身体部位メタファーの体系性**: \n- `kaki langit`: 空の足 ＝ 地平線\n- `kaki gunung`: 山の足 ＝ 山麓・麓\n- `kaki meja`: 机の足 ＝ テーブルの脚\n足（kaki）は「大地に接する土台」として極めて一貫したメタファーを形成しています。"
        ],
        "quizzes": [
            {
                "q": "歩道で営業する屋台や露店商人（PKL）の語源となった「5フィート幅の歩道」に由来するインドネシア語はどれか。",
                "choices": ["kaki lima", "kaki tangan", "kaki langit", "kaki bukit"],
                "ans": "kaki lima",
                "expl": "歩道の屋台・露店商人は `kaki lima`（略称 PKL）です。"
            },
            {
                "q": "犯罪組織のボスなどに仕え、「悪事の手先・下っ端となって命令を実行する者たち」を表す成句はどれか。",
                "choices": ["kaki tangan", "tangan kanan", "kaki lima", "angkat kaki"],
                "ans": "kaki tangan",
                "expl": "悪事の手先・手下は `kaki tangan` です。`tangan kanan` は信頼する右腕・懐刀です。"
            },
            {
                "q": "立ち退きを命じられたり資本を引き揚げたりして「その場から去る・立ち退く・逃げ出す」を意味する慣用句はどれか。",
                "choices": ["angkat kaki", "angkat tangan", "cuci kaki", "cuci tangan"],
                "ans": "angkat kaki",
                "expl": "立ち退く、その場を立ち去る表現は `angkat kaki` です。`angkat tangan` は降伏する・お手上げになるです。"
            }
        ],
        "culture_column": {
            "title": "「Kaki Lima」の語源をめぐるラッフルズの遺産",
            "body": "なぜ屋台を「5本の足（Kaki Lima）」と呼ぶのでしょうか。通説では「車輪2つ＋支え1つ＋店主の足2本＝計5本」という民間語源（folk etymology）が親しまれていますが、歴史学的な定説は1819年に英領東インド総督トーマス・ラッフルズがシンガポールとマラッカで発布した「建物の前面には歩行者のための5フィート幅の屋根付き通路（Five-foot way）を設けよ」という都市条例にあります。この5フィート（kaki lima）の空間に商人が自然発生的に店を出したことから、東南アジア屈指の豊かな屋台文化の代名詞となったのです。"
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
> **文化・語根コラム：{col["title"]}**
> 
> {col["body"]}
"""

    full_text = f"""# {art["title"]}

インドネシア語の語根 **`{art["root"]}`** は、原義として「**{art["meaning"]}**」を表します。{art["core_concept"]}

本稿では、日常会話からビジネス、司法・時事報道に至るまでネイティブスピーカーが自然に使いこなす必須の共起表現（コロケーション）を体系的に解説します。

---

## 1. 語根 `{art["root"]}` の最頻出コロケーション総覧

まずは、頻繁に用いられる主要な連語表現の全体像を把握しましょう。

{table_md}

---

## 2. 重要コロケーションの詳細解説と実践例文

それぞれの共起表現が持つ語感、文脈のニュアンス、および構文上のポイントを詳しく見ていきます。

{details_md}

---

## 3. 実践会話ダイアログ

日常や職場の現場でこれらのコロケーションがどのように自然に組み合わされて使われるか、会話の流れで確認しましょう。

{dialogue_md}

---

## 4. 文法・構文上の注意点（接辞変化と語形）

{gp_md}

---

## 5. 定着確認クイズ（全3問）

本記事で学んだ重要コロケーションの理解度をチェックしましょう。

{quizzes_md}

---

## 6. コア語根の文化的背景

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
