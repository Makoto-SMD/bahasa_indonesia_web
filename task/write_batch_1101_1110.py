# -*- coding: utf-8 -*-
import os

articles_data = [
    {
        "slug": "01-daily-actions-baku-gaul",
        "title": "【二重言語】日常動作動詞（makan, tidur, pergi, pulang）の標準語（Baku）⇄ 街角口語（Gaul）変換",
        "intro": "インドネシア語は、教科書に載っている公式標準語（Bahasa Baku）と、若者や街中で日常的に使われるストリート口語（Bahasa Gaul）が大きく乖離する「二重言語社会（Diglossia）」です。日常の基本動作動詞がどのように口語化されるかを完全マスターします。",
        "pairs": [
            ("Saya mau makan pagi.", "Gue mau nyarap dulu nih.", "朝食を食べる（makan pagi ⇄ nyarap）"),
            ("Dia sudah tidur pulas.", "Dia udah bobo pules.", "ぐっすり眠る（tidur ⇄ bobo/tidur）"),
            ("Ayo kita pergi sekarang.", "Yuk cabut sekarang / OTW yuk.", "出発する・移動する（pergi ⇄ cabut / OTW）"),
            ("Saya mau pulang ke rumah.", "Gue mau balik duluan ya.", "帰宅する（pulang ⇄ balik）")
        ],
        "drill": [
            ("【Baku→Gaul】私は先に帰ります。（Saya pulang duluan ya.）", "Gue balik duluan ya.", "グエ バリッ ドゥルアン ヤ", "pulang は会話で balik に変換されます。"),
            ("【Gaul→Baku】もう出発しようぜ！（Yuk cabut sekarang!）", "Mari kita pergi sekarang.", "マリ キタ プルギ スカラン", "cabut は標準語の pergi / berangkat に対応します。"),
            ("【Baku→Gaul】屋台で朝ごはんを食べよう。（Mari sarapan di warung.）", "Yuk nyarap di warung.", "ユッ ニャラップ ディ ワルン", "朝食 sarapan は口語で nyarap と言います。"),
            ("【Gaul→Baku】彼、まだ寝てるよ。（Dia masih molor / bobo tuh.）", "Dia masih tidur.", "ディア マシ ティドゥール", "molor や bobo は標準語の tidur です。"),
            ("【Baku→Gaul】ちょっとお菓子をつまもう。（Ayo kita makan camilan.）", "Yuk ngemil-ngemil santai.", "ユッ ンゲミルンゲミル サンタイ", "間食するは口語で ngemil です。"),
            ("【Gaul→Baku】今向かってる途中！（Gue lagi OTW nih!）", "Saya sedang dalam perjalanan menuju ke sana.", "サヤ スダン ダラム プルジャラナン メヌジュ ク サナ", "OTW は公式には dalam perjalanan です。"),
            ("【Baku→Gaul】今夜飲みに行かない？（Mau minum-minum malam ini?）", "Mau nongkrong sambil ngopi ntar malam?", "マウ ノンクロン サンビル ンゴピ エンタール マラム", "たむろして飲む・カフェに行くは nongkrong。"),
            ("【Gaul→Baku】昨夜、夜更かししちゃった。（Semalem begadang sampe pagi.）", "Tadi malam saya tidak tidur semalaman.", "タディ マラム サヤ ティダッ ティドゥール スマラマン", "begadang は夜更かしする。"),
            ("【Baku→Gaul】ちょっと散歩しよう。（Ayo kita jalan-jalan sebentar.）", "Yuk jalan-jalan bentar.", "ユッ ジャランジャラン ブンタル", "sebentar は bentar に短縮されます。"),
            ("【Gaul→Baku】彼はもう退社したよ。（Dia udah balik dari kantor.）", "Dia sudah pulang dari kantor.", "ディア スダ プラン ダリ カントール", "udah balik ⇄ sudah pulang。"),
            ("【Baku→Gaul】お腹がすいて死にそう。（Saya sangat lapar sekali.）", "Laper banget nih, perut keroncongan.", "ラペル バンゲット ニ、プルット クロンチョンガン", "lapar → laper, sangat... sekali → banget。"),
            ("【Gaul→Baku】映画見に行こう！（Yuk nonton bioskop!）", "Mari kita menonton film di bioskop.", "マリ キタ メノントン フィルム ディ ビオスコップ", "nonton ⇄ menonton。"),
            ("【Baku→Gaul】部屋でゴロゴロ休んでいる。（Beristirahat santai di kamar.）", "Lagi rebahan santai di kamar.", "ラギ ルバハン サンタイ ディ カマル", "横になってダラダラするは rebahan。"),
            ("【Gaul→Baku】ご飯食べに行こう！（Yuk makan bareng!）", "Mari kita makan bersama-sama.", "マリ キタ マカン ブルサマサマ", "bareng ⇄ bersama-sama。"),
            ("【Baku→Gaul】急いで！もう時間がない。（Cepatlah, sudah tidak ada waktu.）", "Buruan dong, udah mepet nih waktunya!", "ブルアン ドン、ウダ メペット ニ ワクトゥニャ", "buruan ⇄ cepatlah, mepet ⇄ sempit/terbatas。")
        ],
        "quiz": [
            ("親しい友人に「先に帰るね！」と言う最もこなれたGaul口語は？", ["Gue balik duluan ya!", "Saya pulang lebih awal.", "Saya akan kembali sekarang.", "Baku pulang duluan."], 1),
            ("若者が「今向かっている途中！」と言う定番スラングは？", ["Lagi OTW!", "Lagi cabut!", "Lagi nyarap!", "Lagi molor!"], 1),
            ("カフェなどで仲間と「まったり集まる・たむろする」を表す口語動詞は？", ["nongkrong", "begadang", "rebahan", "cabut"], 1)
        ]
    },
    {
        "slug": "02-verbs-prefix-men-dropping",
        "title": "【二重言語】動詞接頭辞 meN- 脱落の会話文法規則と自然な発音（membeli → beli, membawa → bawa）",
        "intro": "日常会話で教科書通りに Saya membeli buku と話すと、まるでアナウンサーの原稿読みのように聞こえます。口語では meN- 接頭辞が脱落して語幹のみ（beli, bawa）になるか、頭文字が鼻音化（ng- / ny- / n- / m-）した形で発話されるのが自然な鉄則です。",
        "pairs": [
            ("Saya mau membeli kopi.", "Gue mau beli kopi.", "買う（membeli ⇄ beli）"),
            ("Dia sedang membaca koran.", "Dia lagi baca koran.", "読む（membaca ⇄ baca）"),
            ("Tolong bantu menolong dia.", "Tolong bantuin nolong dia.", "助ける（menolong ⇄ nolong）"),
            ("Saya memikirkan hal itu.", "Gue lagi mikirin hal itu.", "考える（memikirkan ⇄ mikirin）")
        ],
        "drill": [
            ("【Baku→Gaul】私は明日車を運転します。（Saya akan mengendarai mobil besok.）", "Besok gue nyetir mobil.", "ブソッ グエ ニョティル モビル", "menyetir は口語で nyetir。"),
            ("【Gaul→Baku】ペン取ってくれる？（Bisa ambilin pulpen?）", "Dapatkah Anda mengambilkan pulpen untuk saya?", "ダパッカ アンダ ムンガンビルカン プルペン ウントゥッ サヤ", "ambilin ⇄ mengambilkan。"),
            ("【Baku→Gaul】彼らは昨夜映画を見た。（Mereka menonton film tadi malam.）", "Mereka nonton film semalem.", "ムレカ ノントン フィルム スマレム", "menonton ⇄ nonton。"),
            ("【Gaul→Baku】彼を待ってるの。（Lagi nungguin dia nih.）", "Saya sedang menunggu dia.", "サヤ スダン ムヌング ディア", "nungguin ⇄ menunggu。"),
            ("【Baku→Gaul】質問に答えてください。（Tolong menjawab pertanyaan ini.）", "Tolong jawab pertanyaannya ya.", "トロン ジャワブ プルタニャアンニャ ヤ", "menjawab ⇄ jawab。"),
            ("【Gaul→Baku】手伝ってよ！（Bantuin dong!）", "Tolong bantu saya.", "トロン バントゥ サヤ", "bantuin ⇄ bantu。"),
            ("【Baku→Gaul】荷物を持ってあげる。（Saya akan membawakan barangmu.）", "Sini gue bawain barangnya.", "スィニ グエ バワイン バランニャ", "membawakan ⇄ bawain。"),
            ("【Gaul→Baku】何見てるの？（Lagi ngeliat apa sih?）", "Apa yang sedang Anda lihat?", "アパ ヤン スダン アンダ リハット", "ngeliat ⇄ melihat。"),
            ("【Baku→Gaul】先生が彼を叱った。（Guru memarahi dia.）", "Guru marahin dia.", "グル マラヒン ディア", "memarahi ⇄ marahin。"),
            ("【Gaul→Baku】噂話を聞いたよ。（Udah denger gosipnya.）", "Saya sudah mendengar kabar burung tersebut.", "サヤ スダ ムンダンガル カバル ブルン トゥルスブット", "denger ⇄ mendengar。"),
            ("【Baku→Gaul】手紙を書いている。（Saya sedang menulis surat.）", "Lagi nulis surat nih.", "ラギ ヌリス スラット ニ", "menulis ⇄ nulis。"),
            ("【Gaul→Baku】お金を数える。（Lagi ngitung duit.）", "Sedang menghitung uang.", "スダン ムンヒト芳ン ウアン", "ngitung ⇄ menghitung, duit ⇄ uang。"),
            ("【Baku→Gaul】部屋を掃除する。（Membersihkan kamar tidur.）", "Bersihin kamar dulu ya.", "ブルスィヒン カマル ドゥル ヤ", "membersihkan ⇄ bersihin。"),
            ("【Gaul→Baku】靴を脱いで。（Lepas sepatunya dong.）", "Harap melepas sepatu Anda.", "ハラップ ムレパス スパトゥ アンダ", "lepas ⇄ melepas。"),
            ("【Baku→Gaul】夜空を見上げる。（Memandangi langit malam.）", "Mandang langit malam yang indah.", "マンダン ランギット マラム ヤン インダ", "memandangi ⇄ mandang。")
        ],
        "quiz": [
            ("口語会話で「待っている」と言う時の最も自然な動詞形は？", ["lagi nunggu", "sedang menunggu", "tengah menanti", "sudah tunggu"], 1),
            ("標準語の接尾辞 -kan（使役・受益）は口語で何に変化するか？", ["-in (contoh: ambilin, bawain)", "-kanlah", "-an", "-ken"], 1),
            ("「お金を数える」の口語的表現は？", ["ngitung duit", "menghitung uang", "bilang rupiah", "baca fulus"], 1)
        ]
    },
    {
        "slug": "03-passive-di-vs-ke-an",
        "title": "【二重言語】受動態の変換規則：フォーマル di- / ter- ⇄ 口語 ke- / ke-...-an",
        "intro": "標準語では受動態に di-（意図的）や ter-（偶発・自発）を用いますが、口語ジャカルタ方言では ke-（偶発受動: ketabrak, keinjak）や ke-...-an（被害受動: kehujanan, kemalaman）が圧倒的な主役となります。文脈に応じた受動態のスイッチングを学びます。",
        "pairs": [
            ("Dia tertabrak sepeda motor.", "Dia ketabrak motor kemarin.", "事故に遭う（tertabrak ⇄ ketabrak）"),
            ("Rumah itu terlihat dari sini.", "Rumahnya kelihatan dari sini.", "見える（terlihat ⇄ kelihatan）"),
            ("Saya terkena air hujan.", "Gue kehujanan basah kuyup.", "雨に降られる（terkena hujan ⇄ kehujanan）"),
            ("Kakinya terinjak orang.", "Kakinya keinjek orang di kereta.", "踏まれる（terinjak ⇄ keinjek）")
        ],
        "drill": [
            ("【Baku→Gaul】階段で足が滑って転んだ。（Saya terpeleset di tangga.）", "Gue kepeleset di tangga tadi.", "グエ クプレセット ディ タンガ タディ", "terpeleset ⇄ kepeleset。"),
            ("【Gaul→Baku】うっかり寝過ごしちゃった！（Aduh ketiduran gue!）", "Aduh, saya tidak sengaja tertidur pulas.", "アドゥ、サヤ ティダッ スンガジャ トゥルティドゥール プラス", "ketiduran ⇄ tidak sengaja tertidur。"),
            ("【Baku→Gaul】鍵が部屋の中に閉じ込められた。（Kunci terkunci di dalam.）", "Kuncinya kekunci di dalam kamar.", "クンチニャ ククンチ ディ ダラム カマル", "terkunci ⇄ kekunci。"),
            ("【Gaul→Baku】寒気で風邪引いちゃった。（Kedinginan sampe masuk angin.）", "Saya kedinginan hingga jatuh sakit.", "サヤ クディンギナン ヒンガ ジャトゥ サキッ", "被害受動 kedinginan。"),
            ("【Baku→Gaul】彼の嘘がバレた。（Kebohongannya terbongkar.）", "Bohongnya ketahuan deh.", "ボホンニャ クタフアン デ", "terbongkar ⇄ ketahuan。"),
            ("【Gaul→Baku】足を踏まれちゃった。（Kaki gue keinjek nih.）", "Kaki saya terinjak oleh seseorang.", "カキ サヤ トゥリンジャッ オレ スソオラン", "keinjek ⇄ terinjak。"),
            ("【Baku→Gaul】夜遅くなってしまった。（Kami kemalaman di jalan.）", "Kemaleman kita di jalan macet.", "クマルマン キタ ディ ジャラン マチェット", "kemalaman ⇄ kemaleman。"),
            ("【Gaul→Baku】料理がしょっぱすぎる！（Makanannya keasinan!）", "Masakan ini terlalu asin.", "マサカン イニ トゥルラル アスィン", "過剰 keasinan ⇄ terlalu asin。"),
            ("【Baku→Gaul】うっかり飲み物をこぼした。（Minumannya tertumpah.）", "Minumannya ketumpahan di baju.", "ミヌマンニャ クトゥムパハン ディ バジュ", "tertumpah ⇄ ketumpahan。"),
            ("【Gaul→Baku】警察に捕まっちゃった。（Ketangkep polisi tadi.）", "Ditangkap oleh pihak kepolisian.", "ディタンカップ オレ ピハッ クポリシアン", "ketangkep ⇄ ditangkap。"),
            ("【Baku→Gaul】急な用事で邪魔された。（Terganggu oleh urusan mendadak.）", "Keganggu sama urusan mendadak.", "クガング サマ ウルサン ムンダダッ", "terganggu ⇄ keganggu。"),
            ("【Gaul→Baku】コーヒーが甘すぎるよ。（Kopinya kemanisan nih.）", "Kopi ini terlalu manis rasanya.", "コピ イニ トゥルラル マニス ラサニャ", "過剰 kemanisan ⇄ terlalu manis。"),
            ("【Baku→Gaul】スマホが床に落っこちた。（Ponsel terjatuh ke lantai.）", "HP gue kejatuhan barang.", "ハーペー グエ クジャトゥハン バラン", "terjatuh ⇄ kejatuhan。"),
            ("【Gaul→Baku】熱々のスープで舌を火傷した。（Lidah gue kepanasan.）", "Lidah saya terbakar panas.", "リダ サヤ トゥルバカル パナス", "kepanasan ⇄ terlalu panas。"),
            ("【Baku→Gaul】彼の声がここまではっきり聞こえる。（Suaranya terdengar jelas.）", "Suaranya kedengeran jelas banget.", "スアラニャ クドゥンゲラン ジュラス バンゲット", "terdengar ⇄ kedengeran。")
        ],
        "quiz": [
            ("口語で「車に轢かれそうになった（偶発）」を表す動詞は？", ["hampir ketabrak", "hampir ditabrakkan", "hampir tertabrakkan", "hampir menabrak"], 1),
            ("「雨に降られてずぶ濡れになった（被害）」を表す口語フレーズは？", ["kehujanan basah kuyup", "dihujani air", "hujan deras turun", "hujan-hujanan enak"], 1),
            ("口語の ke-...-an で味覚が「過剰（〜すぎる）」を表す例として正しいのは？", ["keasinan (しょっぱすぎる)", "asinan (漬物)", "mengasini (塩をつける)", "terasinkan (塩漬けされた)"], 1)
        ]
    },
    {
        "slug": "04-pronouns-saya-aku-gue",
        "title": "【二重言語】人称代名詞の3大レジスター（Baku: saya/Anda ⇄ Akrab: aku/kamu ⇄ Gaul: gue/lu）の境界線",
        "intro": "インドネシア語の人称代名詞は、話し手と聞き手の社会的距離・心理的親密さ・地域性を如実に表します。目上に gue/lu を使うと致命的な無礼になり、親友に saya/Anda を使い続けると冷たい壁を作ります。3大レジスターの境界線を整理します。",
        "pairs": [
            ("Saya ingin bertanya kepada Anda.", "Gue mau nanya dong sama lu.", "私とあなた（saya/Anda ⇄ gue/lu）"),
            ("Aku sangat menyayangi kamu.", "Gue sayang banget sama lu.", "恋人・友人（aku/kamu ⇄ gue/lu）"),
            ("Nama saya Budi, senang bertemu.", "Kenalin, gue Budi nih.", "自己紹介のレジスター差"),
            ("Silakan Anda masuk duluan.", "Lu masuk duluan aja santai.", "相手への呼びかけ（Anda ⇄ lu）")
        ],
        "drill": [
            ("【Baku→Gaul】私はジャカルタ出身です。（Saya berasal dari Jakarta.）", "Gue anak Jakarta asli.", "グエ アナッ ジャカルタ アスリ", "若者口語 gue。"),
            ("【Gaul→Baku】お前、どこ行くの？（Lu mau ke mana?）", "Anda hendak pergi ke mana?", "アンダ ヘンダッ プルギ ク マナ", "改まった Anda。"),
            ("【Baku→Akrab】君の意見はどう？（Bagaimana pendapat Anda?）", "Gimana menurut kamu?", "ギマナ ムヌルット カム", "親しい対等 aku/kamu。"),
            ("【Gaul→Baku】私には分からないよ。（Gue nggak tahu apa-apa.）", "Saya sama sekali tidak mengetahui hal tersebut.", "サヤ サマ スカリ ティダッ ムンゲタフイ ハル トゥルスブット", "公式 saya。"),
            ("【Baku→Gaul】君の携帯番号を教えて。（Boleh saya minta nomor telepon Anda?）", "Boleh minta nomor WA lu nggak?", "ボレ ミンタ ノモール ワー ル ンガッ", "口語の連絡先交換 lu。"),
            ("【Gaul→Baku】俺たちのチームが勝った！（Tim gue yang menang!）", "Tim kami yang berhasil meraih kemenangan.", "ティム カミ ヤン ブルハスィル ムライ クムナンガン", "公の場 kami。"),
            ("【Baku→Akrab】君と一緒に映画を見たい。（Saya ingin menonton dengan Anda.）", "Aku pengen nonton bareng kamu.", "アク プンゲン ノントン バレン カム", "親密 aku/kamu。"),
            ("【Gaul→Baku】お前、マジで言ってんの？（Lu seriusan nih?）", "Apakah Anda sungguh-sungguh dengan pernyataan itu?", "アパカ アンダ スングスング ドゥンガン プルニャタアン イトゥ", "公式確認。"),
            ("【Baku→Gaul】私は今日暇です。（Saya senggang hari ini.）", "Gue lagi gabut nih hari ini.", "グエ ラギ ガブット ニ ハリ イニ", "暇・退屈 gabut。"),
            ("【Gaul→Baku】私がおごるよ。（Tenang, gue yang traktir.）", "Jangan khawatir, saya yang akan mentraktir Anda.", "ジャンガン クワティル、サヤ ヤン アカン ムントラクティル アンダ", "公式歓待。"),
            ("【Baku→Akrab】君を信じているよ。（Saya percaya kepada Anda.）", "Aku percaya sama kamu kok.", "アク プルチャヤ サマ カム コッ", "親密信頼。"),
            ("【Gaul→Baku】お前ん家、どこ？（Rumah lu di mana sih?）", "Di manakah letak kediaman Anda?", "ディ マナカ ルタッ クディアマン アンダ", "丁寧な住居尋ね。"),
            ("【Baku→Gaul】私は怒っていませんよ。（Saya tidak marah kepada Anda.）", "Gue nggak kesel kok sama lu.", "グエ ンガッ クサル コッ サマ ル", "口語の感情吐露。"),
            ("【Gaul→Baku】俺たち、親友だろ！（Kita kan sahabat dekat!）", "Bukankah kita adalah sahabat sejati?", "ブカンカ キタ アダラ サハバット スジャティ", "公の友情確認。"),
            ("【Baku→Gaul】君の服、かっこいいね。（Pakaian Anda tampak sangat bagus.）", "Outfit lu kece badai bro!", "アウトフィット ル クチェ バダイ ブロ", "若者スラング kece badai。")
        ],
        "quiz": [
            ("ジャカルタのストリート口語「gue / lu」を使って良い相手は？", ["同年代の親しい友人・仲間", "初対面の取引先クライアント", "大学の教授や上司", "警察官や入国審査官"], 1),
            ("恋人同士や親しい友人同士で最も自然で温かみのある代名詞ペアは？", ["aku / kamu", "saya / Anda", "gue / lu", "kami / kalian"], 1),
            ("ビジネスの公式なメールや初対面で使うべき確実な代名詞は？", ["saya / Bapak (Ibu) / Anda", "gue / lu", "aku / kamu", "kita / ente"], 1)
        ]
    },
    {
        "slug": "05-negation-tidak-nggak-ndak",
        "title": "【二重言語】否定詞の変換：tidak ⇄ nggak / ndak / kagak の使い分け",
        "intro": "教科書では否定詞といえば tidak ですが、生きた口語会話では 90% 以上 nggak（または地域方言の ndak, 下町の kagak）が使われます。公式スピーチで nggak を言うと教養を疑われ、友達に tidak と言うとロボットのように聞こえる、この二重性を攻略します。",
        "pairs": [
            ("Saya tidak mau pergi.", "Gue nggak mau pergi.", "行きたくない（tidak ⇄ nggak）"),
            ("Dia tidak tahu apa-apa.", "Dia kagak tahu apa-apaan.", "何も知らない（tidak ⇄ kagak: 下町ベタウィ）"),
            ("Saya tidak punya uang.", "Ndak punya duit mas.", "お金がない（tidak ⇄ ndak: ジャワ口語）"),
            ("Ini bukan urusan saya.", "Ini bukan urusan gue kok.", "私の知ったことではない（名詞否定 bukan）")
        ],
        "drill": [
            ("【Baku→Gaul】美味しくない。（Makanannya tidak enak.）", "Makanannya nggak enak.", "マカナンニャ ンガッ エナッ", "口語否定 nggak。"),
            ("【Gaul→Baku】全然問題ないよ！（Nggak apa-apa kok!）", "Sama sekali tidak ada masalah.", "サマ スカリ ティダッ アダ マサラ", "公式 tidak ada masalah。"),
            ("【Baku→Gaul】彼は今日来られない。（Dia tidak bisa datang hari ini.）", "Dia nggak bisa dateng hari ini.", "ディア ンガッ ビサ ダテン ハリ イニ", "tidak bisa ⇄ nggak bisa。"),
            ("【Gaul→Baku】知らないよ！（Kagak tahu gue!）", "Saya benar-benar tidak mengetahuinya.", "サヤ ブナルブナル ティダッ ムンゲタフイニャ", "kagak tahu ⇄ tidak tahu。"),
            ("【Baku→Gaul】嘘ではありません。（Ini bukan sebuah kebohongan.）", "Bukan bohong kok ini suwer.", "ブカン ボホン コッ イニ スウェル", "bukan は口語でも bukan。"),
            ("【Gaul→Baku】気にしないで。（Nggak usah dipikirin.）", "Anda tidak perlu memikirkannya.", "アンダ ティダッ プルル ムミキルカンニャ", "nggak usah ⇄ tidak perlu。"),
            ("【Baku→Gaul】私は辛いものが好きではない。（Saya tidak suka pedas.）", "Gue nggak doyan pedes.", "グエ ンガッ ドヤン プデス", "suka makan ⇄ doyan。"),
            ("【Gaul→Baku】時間がもうない！（Udah nggak sempet lagi!）", "Sudah tidak ada waktu yang cukup.", "スダ ティダッ アダ ワクトゥ ヤン チュクップ", "nggak sempet ⇄ tidak sempat。"),
            ("【Baku→Gaul】冗談ではないよ。（Saya tidak sedang bercanda.）", "Gue nggak lagi bercanda nih.", "グエ ンガッ ラギ ブルチャンダ ニ", "tidak bercanda ⇄ nggak bercanda。"),
            ("【Gaul→Baku】そんなの無理！（Nggak mungkin banget!）", "Hal itu sangat mustahil untuk terjadi.", "ハル イトゥ サンガット ムスタヒル ウントゥッ トゥルジャディ", "nggak mungkin ⇄ mustahil。"),
            ("【Baku→Gaul】高価ではない。（Harganya tidak terlalu mahal.）", "Harganya nggak gitu mahal kok.", "ハルガニャ ンガッ ギトゥ マハル コッ", "tidak terlalu ⇄ nggak gitu。"),
            ("【Gaul→Baku】あいつは来ないよ。（Dia ndak bakal dateng.）", "Dia tidak akan hadir.", "ディア ティダッ アカン ハディル", "ndak bakal ⇄ tidak akan。"),
            ("【Baku→Gaul】私はまだお腹が空いていない。（Saya belum merasa lapar.）", "Gue belom laper nih.", "グエ ブロム ラペル ニ", "belum ⇄ belom。"),
            ("【Gaul→Baku】気に食わないな。（Kagak demen gue liatnya.）", "Saya kurang menyukai hal tersebut.", "サヤ クラン メニュカイ ハル トゥルスブット", "kagak demen ⇄ tidak suka。"),
            ("【Baku→Gaul】恐れることはない。（Jangan merasa takut.）", "Nggak usah takut, sans aja.", "ンガッ ウサ タクット、サンス アジャ", "sans = santai。")
        ],
        "quiz": [
            ("インドネシアの日常会話で最も標準的に使われる口語否定詞は？", ["nggak", "tidak", "bukan", "tanpa"], 1),
            ("ジャカルタの下町ベタウィ言葉で独特の荒っぽい否定詞は？", ["kagak", "ndak", "ora", "mohon"], 1),
            ("「〜する必要はない（〜しなくていい）」の最もこなれた口語表現は？", ["nggak usah", "tidak wajib", "belum perlu", "bukan boleh"], 1)
        ]
    },
    {
        "slug": "06-aspect-sudah-udah-belum-belom",
        "title": "【二重言語】アスペクト副詞の口語短縮（sudah → udah, belum → belom, sedang → lagi）",
        "intro": "時間の流れや動作の進行を表すアスペクト詞は、会話の中で極めて高い頻度で音韻縮約・母音変化を起こします。sudah は udah、belum は belom、sedang は lagi に置き換わります。この口語アスペクトの反射的聞き取りと産出を訓練します。",
        "pairs": [
            ("Saya sudah menyelesaikan tugas.", "Gue udah kelar ngerjain tugas.", "完了（sudah ⇄ udah / kelar）"),
            ("Dia belum datang ke kantor.", "Dia belom nyampe kantor.", "未完了（belum ⇄ belom）"),
            ("Saya sedang makan siang.", "Gue lagi makan siang nih.", "進行（sedang ⇄ lagi）"),
            ("Apakah Anda sudah pernah ke sana?", "Udah pernah ke sana belom?", "経験確認（sudah... belum ⇄ udah... belom）")
        ],
        "drill": [
            ("【Baku→Gaul】私はすでにチケットを購入しました。（Saya sudah membeli tiket.）", "Gue udah beli tiketnya.", "グエ ウダ ブリ ティケットニャ", "sudah membeli ⇄ udah beli。"),
            ("【Gaul→Baku】宿題、もう終わった？（Tugasnya udah kelar belom?）", "Apakah Anda sudah menyelesaikan tugas tersebut?", "アパカ アンダ スダ ムニェレサイカン トゥガス トゥルスブット", "udah kelar belom ⇄ sudah selesai belum。"),
            ("【Baku→Gaul】彼は今、会議中です。（Dia sedang menghadiri rapat.）", "Dia lagi rapat sekarang.", "ディア ラギ ラパット スカラン", "sedang ⇄ lagi。"),
            ("【Gaul→Baku】まだご飯食べてない。（Belom makan nih dari pagi.）", "Saya belum sarapan sejak pagi tadi.", "サヤ ブルム サラパン スジャッ パギ タディ", "belom ⇄ belum。"),
            ("【Baku→Gaul】もう帰る時間ですよ。（Sudah waktunya untuk pulang.）", "Udah jamnya balik nih.", "ウダ ジャムニャ バリッ ニ", "udah jamnya ⇄ sudah waktunya。"),
            ("【Gaul→Baku】今、運転してるから後でね。（Lagi nyetir nih, ntar ya.）", "Saya sedang mengemudi mobil, nanti saya hubungi lagi.", "サヤ スダン ムングムディ モビル、ナンティ サヤ フブンギ ラギ", "lagi nyetir ⇄ sedang mengemudi。"),
            ("【Baku→Gaul】バリ島に行ったことがありますか？（Pernahkah Anda ke Bali?）", "Udah pernah ke Bali belom?", "ウダ プルナ ク バリ ブロム", "経験尋ね udah pernah... belom。"),
            ("【Gaul→Baku】仕事が全部片付いた！（Udah beres semua kerjaan!）", "Semua pekerjaan telah selesai dikerjakan.", "スムア プクルジャアン トゥラ スルサイ ディクルジャカン", "udah beres ⇄ telah selesai。"),
            ("【Baku→Gaul】雨がまだ降っている。（Hujan masih sedang turun.）", "Hujannya masih awet nih.", "フジャンニャ マシ アウェット ニ", "長引く雨 masih awet。"),
            ("【Gaul→Baku】さっき起きたばかり。（Barusan banget bangun tidur.）", "Saya baru saja terbangun dari tidur.", "サヤ バル サジャ トゥルバングン ダリ ティドゥール", "barusan banget ⇄ baru saja。"),
            ("【Baku→Gaul】準備はすべて整いました。（Semua persiapan sudah selesai.）", "Semuanya udah siap beres.", "スムアニャ ウダ スィアップ ベレス", "udah siap ⇄ sudah selesai。"),
            ("【Gaul→Baku】今、考え中！（Lagi mikir keras nih!）", "Saya sedang berpikir dengan sungguh-sungguh.", "サヤ スダン ブルピキル ドゥンガン スングスング", "lagi mikir ⇄ sedang berpikir。"),
            ("【Baku→Gaul】まだ返事が来ていない。（Belum ada balasan pesan.）", "Belom dibales chat-nya.", "ブロム ディバレス チャットニャ", "belom dibales ⇄ belum dibalas。"),
            ("【Gaul→Baku】映画はもう始まっちゃった。（Filmnya udah keburu mulai.）", "Pemutaran film sudah terlanjur dimulai.", "プムトゥラン フィルム スダ トゥルランジュール ディムライ", "udah keburu ⇄ sudah terlanjur。"),
            ("【Baku→Gaul】今まさに家を出るところです。（Saya baru saja mau berangkat.）", "Lagi mau cabut nih.", "ラギ マウ チャブット ニ", "lagi mau cabut ⇄ baru saja mau berangkat。")
        ],
        "quiz": [
            ("日常会話で sedang（〜している最中）の代わりに最も使われる語は？", ["lagi", "udah", "belom", "akan"], 1),
            ("「すでに終わった・片付いた」を表す最もポピュラーな口語形容詞は？", ["kelar / beres", "lulus", "sempurna", "mati"], 1),
            ("「もう昼ご飯食べた？」と友達に聞く自然な口語表現は？", ["Udah makan siang belom?", "Apakah Anda sudah makan siang?", "Sudahkah makan siang Anda?", "Baku makan siang kamu?"], 1)
        ]
    },
    {
        "slug": "07-question-apakah-apaan-gimana",
        "title": "【二重言語】疑問詞の口語変換：bagaimana → gimana, mengapa → kenapa, apakah → apa / apaan",
        "intro": "標準語の疑問詞 bagaimana, mengapa, di mana は、日常会話では gimana, kenapa, mana に短縮・変容します。さらに「何それ？」と驚く apaan tuh? などの感情表現も豊富です。口語疑問詞のバリエーションを使いこなしましょう。",
        "pairs": [
            ("Bagaimana kabar Anda?", "Gimana kabarnya? / Gimana kabarmu?", "調子はどう？（bagaimana ⇄ gimana）"),
            ("Mengapa Anda terlambat datang?", "Kenapa telat dateng?", "なぜ遅刻した？（mengapa ⇄ kenapa）"),
            ("Apakah ini milik Anda?", "Ini punya lu bukan? / Apa ini?", "これは君の？（apakah ⇄ apa / apaan）"),
            ("Di mana Anda tinggal?", "Tinggal di mana sih?", "どこに住んでるの？（di mana ⇄ di mana / mana）")
        ],
        "drill": [
            ("【Baku→Gaul】どうやって行くの？（Bagaimana cara perginya?）", "Gimana naiknya ke sana?", "ギマナ ナイスニャ ク サナ", "bagaimana cara ⇄ gimana。"),
            ("【Gaul→Baku】なんで泣いてるの？（Kenapa lu nangis?）", "Mengapa Anda menangis?", "ムンガパ アンダ ムナンギス", "kenapa ⇄ mengapa, nangis ⇄ menangis。"),
            ("【Baku→Gaul】何があったのですか？（Apa yang telah terjadi?）", "Ada apaan sih rame-rame?", "アダ アパアン スィ ラメラメ", "apaan sih ⇄ apa yang terjadi。"),
            ("【Gaul→Baku】調子はどう？（Gimana kabarnya bro?）", "Bagaimanakah kabar Anda hari ini?", "バガイマナカ カバル アンダ ハリ イニ", "gimana kabar ⇄ bagaimana kabar。"),
            ("【Baku→Gaul】どこで買ったの？（Di mana Anda membelinya?）", "Beli di mana tuh barang?", "ブリ ディ マナ トゥ バラン", "di mana ⇄ di mana tuh。"),
            ("【Gaul→Baku】何これ、変な味！（Apaan nih, aneh banget rasanya!）", "Benda apakah ini, rasanya sangat ganjil.", "ブンダ アパカ イニ、ラサニャ サンガット ガンジル", "apaan nih ⇄ benda apakah ini。"),
            ("【Baku→Gaul】どうして来なかったの？（Mengapa tidak hadir kemarin?）", "Kenapa kemarin nggak dateng?", "クナパ クマリン ンガッ ダテン", "mengapa tidak hadir ⇄ kenapa nggak dateng。"),
            ("【Gaul→Baku】いくらだった？（Berapaan harganya tadi?）", "Berapakah harga barang tersebut?", "ブラパカ ハルガ バラン トゥルスブット", "berapaan ⇄ berapakah harga。"),
            ("【Baku→Gaul】どっちがいいと思う？（Yang mana yang lebih baik?）", "Mending yang mana menurut lu?", "ムンディン ヤン マナ ムヌルット ル", "mending ⇄ lebih baik。"),
            ("【Gaul→Baku】誰がそんなこと言ったの？（Siapa yang ngomong gitu?）", "Siapakah yang mengatakan hal tersebut?", "スィアパカ ヤン ムンガタカン ハル トゥルスブット", "ngomong gitu ⇄ mengatakan hal tersebut。"),
            ("【Baku→Gaul】いつ出発しますか？（Kapan Anda akan berangkat?）", "Kapan cabutnya nih?", "カパン チャブットニャ ニ", "kapan berangkat ⇄ kapan cabut。"),
            ("【Gaul→Baku】どうすればいいか分からない。（Bingung gimana caranya.）", "Saya bingung bagaimana cara melakukannya.", "サヤ ビングン バガイマナ チャラ ムラクカンニャ", "gimana caranya ⇄ bagaimana caranya。"),
            ("【Baku→Gaul】何を見ているの？（Apa yang sedang Anda perhatikan?）", "Ngaso sambil liat apaan tuh?", "ンガソ サンビル リハット アパアン トゥ", "apaan tuh ⇄ apa yang diperhatikan。"),
            ("【Gaul→Baku】どうしてそんなに怒るの？（Kenapa marah-marah melulu?）", "Mengapa Anda selalu meluapkan amarah?", "ムンガパ アンダ スラル ムルアプカン アマラ", "kenapa marah-marah ⇄ mengapa marah。"),
            ("【Baku→Gaul】次はどこへ行く？（Ke mana tujuan kita berikutnya?）", "Abis ini mau ke mana lagi kita?", "アビス イニ マウ ク マナ ラギ キタ", "abis ini ⇄ setelah ini。")
        ],
        "quiz": [
            ("日常会話で「どうして？（why）」を尋ねる最も一般的な語は？", ["kenapa", "mengapa", "sebab apa", "alasan"], 1),
            ("「何だよそれ！」とくだけた調子でツッコミを入れる定番疑問詞は？", ["Apaan tuh?!", "Apakah gerangan?", "Bagaimanakah itu?", "Mengapa begitu?"], 1),
            ("「どう？（how）」を気軽に尋ねる口語疑問詞は？", ["gimana", "bagaimana", "macam mana", "apa kabar"], 1)
        ]
    },
    {
        "slug": "08-time-sekarang-skrg-ntar",
        "title": "【二重言語】時間表現の口語短縮：sekarang → skrg / bentar, nanti → ntar, kemarin → kemaren",
        "intro": "日常の会話やテキストチャット（WhatsApp）では、時間表現が驚くほど短縮されます。sebentar は bentar、nanti は ntar、kemarin は kemaren、tadi malam は semalem と音が縮まり、テンポの良い会話が生まれます。",
        "pairs": [
            ("Tunggu sebentar ya.", "Tunggu bentar ya. / Bentar ya.", "ちょっと待って（sebentar ⇄ bentar）"),
            ("Nanti kita bicarakan lagi.", "Ntar kita omongin lagi.", "あとで話そう（nanti ⇄ ntar）"),
            ("Kemarin saya pergi ke mall.", "Kemaren gue cabut ke mal.", "昨日（kemarin ⇄ kemaren）"),
            ("Tadi malam hujan sangat deras.", "Semalem hujannya deres parah.", "昨夜（tadi malam ⇄ semalem）")
        ],
        "drill": [
            ("【Baku→Gaul】ちょっと待ってください。（Tolong tunggu sebentar.）", "Bentar ya, tunggu semenit.", "ブンタル ヤ、トゥング スムニット", "sebentar ⇄ bentar。"),
            ("【Gaul→Baku】あとで連絡するね。（Ntar gue kabarin ya.）", "Nanti saya akan memberi kabar kepada Anda.", "ナンティ サヤ アカン ムンブリ カバル クパダ アンダ", "ntar kabarin ⇄ nanti beri kabar。"),
            ("【Baku→Gaul】昨日の夜、何してた？（Tadi malam sedang melakukan apa?）", "Semalem lu lagi ngapain?", "スマレム ル ラギ ンガパイン", "tadi malam ⇄ semalem, ngapain ⇄ melakukan apa。"),
            ("【Gaul→Baku】さっき彼に会ったよ。（Barusan ketemu dia di lobi.）", "Saya baru saja berpapasan dengan beliau di lobi.", "サヤ バル サジャ ブルパパサン ドゥンガン ベリアウ ディ ロビ", "barusan ⇄ baru saja。"),
            ("【Baku→Gaul】明日の朝一番で会いましょう。（Mari bertemu besok pagi-pagi.）", "Besok pagi-pagi kita kumpul ya.", "ブソッ パギパギ キタ クンプル ヤ", "besok ⇄ bsk (チャット)。"),
            ("【Gaul→Baku】今すぐ出発！（Sekarang juga cabut!）", "Kita harus berangkat sekarang juga.", "キタ ハルス ブランカット スカラン ジュガ", "cabut ⇄ berangkat。"),
            ("【Baku→Gaul】最近、とても忙しい。（Akhir-akhir ini saya sangat sibuk.）", "Akhir-akhir ini lagi hectic bgt gue.", "アキールアキール イニ ラギ ヘクティック バンゲット グエ", "hectic bgt = sibuk sekali。"),
            ("【Gaul→Baku】昔はよくここで遊んだ。（Dulu sering maen di sini.）", "Dahulu kala kami sering bermain di tempat ini.", "ダフル カラ カミ スリン ブルマイン ディ トゥムパット イニ", "dulu sering maen ⇄ dahulu sering bermain。"),
            ("【Baku→Gaul】今何時ですか？（Pukul berapa sekarang?）", "Jam berapa nih sekarang?", "ジャム ブラパ ニ スカラン", "pukul berapa ⇄ jam berapa。"),
            ("【Gaul→Baku】一瞬で終わるよ！（Cuma sebentar doang kok!）", "Ini hanya memerlukan waktu yang sangat singkat.", "イニ ハニャ ムムルルカン ワクトゥ ヤン サンガット スィンカット", "sebentar doang ⇄ waktu singkat。"),
            ("【Baku→Gaul】午後2時ちょうどに会いましょう。（Tepat pukul dua siang.）", "Pas jam dua siang ya ntar.", "パス ジャム ドゥア スィアン ヤ エンタール", "tepat pukul ⇄ pas jam。"),
            ("【Gaul→Baku】昨日の昼ご飯美味しかった。（Kemaren makan siangnya enak.）", "Makan siang kemarin terasa sangat lezat.", "マカン スィアン クマリン トゥラサ サンガット ルザット", "kemaren ⇄ kemarin。"),
            ("【Baku→Gaul】ずっと以前からの知り合いです。（Kenal sejak lama.）", "Udah kenal dari jaman baheula.", "ウダ クナル ダリ ジャマン バヘウラ", "jaman baheula = 大昔。"),
            ("【Gaul→Baku】今夜空いてる？（Ntar malem free nggak?）", "Apakah Anda ada waktu luang nanti malam?", "アパカ アンダ アダ ワクトゥ ルアン ナンティ マラム", "ntar malem free ⇄ nanti malam ada waktu。"),
            ("【Baku→Gaul】もうすぐ着きます。（Sebentar lagi saya akan tiba.）", "Bentar lagi nyampe nih, otw.", "ブンタル ラギ ニャンペ ニ、オーテーウェー", "bentar lagi nyampe ⇄ sebentar lagi tiba。")
        ],
        "quiz": [
            ("口語で「あとでね（later）」と軽く言う定番単語は？", ["ntar ya", "segera ya", "lekas ya", "nanti sekali"], 1),
            ("会話で「ちょっと待って」と言う時の最も短い表現は？", ["Bentar!", "Menunggu!", "Sabar sebentar!", "Tunggu dulu sebentar!"], 1),
            ("「昨夜」を口語で一言で表す単語は？", ["semalem", "kemarin malam hari", "tadi gelap", "malam lewat"], 1)
        ]
    },
    {
        "slug": "09-conjunction-kalau-kalo-tapi",
        "title": "【二重言語】接続詞の口語変換：tetapi → tapi, kalau → kalo, karena → soalnya / abisnya",
        "intro": "文と文をつなぐ接続詞は、会話のリズムを作る心臓部です。標準語の tetapi, jikalau, oleh karena itu は、口語では tapi, kalo, soalnya, abisnya, makanya に様変わりします。因果関係や条件の口語スイッチングを身につけます。",
        "pairs": [
            ("Saya ingin pergi, tetapi hujan deras.", "Pengen pergi, tapi ujan deres.", "逆接（tetapi ⇄ tapi）"),
            ("Kalau Anda ada waktu, mari mengobrol.", "Kalo ada waktu, ngobrol yuk.", "条件（kalau ⇄ kalo）"),
            ("Saya terlambat karena macet.", "Telat, soalnya macet parah di jalan.", "理由（karena ⇄ soalnya）"),
            ("Oleh karena itu, berhati-hatilah.", "Makanya, hati-hati dong.", "結果（oleh karena itu ⇄ makanya）")
        ],
        "drill": [
            ("【Baku→Gaul】行きたいけれど、お金がない。（Mau pergi tetapi tidak ada uang.）", "Pengen pergi tapi bokek nih.", "プンゲン プルギ タピ ボケッ ニ", "tetapi ⇄ tapi, tidak ada uang ⇄ bokek。"),
            ("【Gaul→Baku】だから言ったでしょ！（Makanya, gue kan udah bilang!）", "Oleh sebab itu, bukankah saya telah memperingatkan Anda?", "オレ スバッブ イトゥ、ブカンカ サヤ トゥラ ムンプリンガッカン アンダ", "makanya ⇄ oleh sebab itu。"),
            ("【Baku→Gaul】もし暇なら遊びに来て。（Jikalau senggang, silakan mampir.）", "Kalo lagi santai, mampir sini dong.", "カロ ラギ サンタイ、マンピル スィニ ドン", "jikalau ⇄ kalo。"),
            ("【Gaul→Baku】だって彼が怒るんだもん。（Abisnya dia marah-marah terus sih.）", "Hal itu dikarenakan beliau terus meluapkan emosi.", "ハル イトゥ ディカレナカン ベリアウ トゥルス ムルアプカン エモスィ", "理由言い訳 abisnya ⇄ dikarenakan。"),
            ("【Baku→Gaul】疲れた、なぜなら残業したから。（Lelah karena lembur kerja.）", "Capek, soalnya lembur semaleman.", "チャペッ、ソアルニャ レンブール スマラマン", "karena ⇄ soalnya。"),
            ("【Gaul→Baku】それどころか逆効果だよ。（Malahan jadi tambah ancur.）", "Bahkan hal itu justru memperburuk situasi.", "バカン ハル イトゥ ジュストゥル ムムプルブルッ スィトゥアスィ", "malahan ⇄ bahkan justru。"),
            ("【Baku→Gaul】安いけれども品質が良い。（Murah tetapi kualitasnya bagus.）", "Murah tapi barangnya oke punya.", "ムラ タピ バランニャ オケ プニャ", "tetapi ⇄ tapi。"),
            ("【Gaul→Baku】じゃあ、どうする？（Terus, mau gimana sekarang?）", "Lalu, apakah langkah kita selanjutnya?", "ラル、アパカ ランカ キタ スランジュットニャ", "terus ⇄ lalu。"),
            ("【Baku→Gaul】雨が降ったら中止です。（Kalau hujan, dibatalkan.）", "Kalo ujan, batal acaranya.", "カロ ウジャン、バタル アチャラニャ", "kalau ⇄ kalo, dibatalkan ⇄ batal。"),
            ("【Gaul→Baku】彼のせいで遅刻した。（Gara-gara dia jadi telat nih.）", "Akibat perbuatan dia, kami mengalami keterlambatan.", "アキバット プルブアタン ディア、カミ ムンガラミ クトゥルランバタン", "gara-gara ⇄ akibat。"),
            ("【Baku→Gaul】ただし条件があります。（Namun ada syarat tertentu.）", "Cuma ada syaratnya ya bro.", "チュマ アダ シャラットニャ ヤ ブロ", "namun ⇄ cuma / tapi。"),
            ("【Gaul→Baku】そうしないと後悔するよ。（Kalo nggak, nyesel lu ntar.）", "Jika tidak, Anda pasti akan menyesal di kemudian hari.", "ジカ ティダッ、アンダ パスティ アカン メニェサル ディ クムディアン ハリ", "kalo nggak ⇄ jika tidak。"),
            ("【Baku→Gaul】仕事中なので電話に出られない。（Tidak bisa angkat telepon karena sedang kerja.）", "Nggak bisa angkat telp, soalnya lagi repot.", "ンガッ ビサ アンカット テルプ、ソアルニャ ラギ レポット", "soalnya ⇄ karena。"),
            ("【Gaul→Baku】とにかくやってみよう。（Pokoknya kita coba dulu aja.）", "Bagaimanapun juga, mari kita berusaha terlebih dahulu.", "バガイマナプン ジュガ、マリ キタ ブルウサハ トゥルレビ ダフル", "pokoknya ⇄ bagaimanapun juga。"),
            ("【Baku→Gaul】彼だけでなく私も行く。（Bukan hanya dia, melainkan saya juga.）", "Nggak cuma dia doang, gue juga ikut.", "ンガッ チュマ ディア ドアン、グエ ジュガ イクット", "melainkan ⇄ juga ikut。")
        ],
        "quiz": [
            ("会話で「なぜなら〜だから（理由の説明）」を切り出す最も定番の語は？", ["soalnya", "karena sesungguhnya", "oleh karena itu", "dikarenakan"], 1),
            ("「だから〜でしょ！（ほら見たことか）」と促す接続詞は？", ["Makanya!", "Tetapi!", "Walaupun!", "Jikalau!"], 1),
            ("「〜のせいで（ネガティブな原因）」を表す口語接続表現は？", ["gara-gara", "berkat", "demi", "karena kemuliaan"], 1)
        ]
    },
    {
        "slug": "10-particle-sih-in-action",
        "title": "【二重言語】魔法の文末詞「sih」完全攻略：疑問の和らげ、控えめな主張、意外性のトーン",
        "intro": "インドネシア語の口語会話で最も耳にする文末詞の一つが「sih」です。直接的で角が立つ言い方を和らげたり（クッション）、「そうは言うけどね…」と前置きしたり、不審・意外性を表したりと、ネイティブ会話のニュアンスの要となります。",
        "pairs": [
            ("Apa itu?", "Apaan sih itu?", "疑問の和らげ・苛立ち（何それ？ ⇄ なんだよそれ〜）"),
            ("Saya setuju.", "Setuju sih, tapi agak mahal.", "控えめな同意（賛成ではあるけれど…）"),
            ("Kenapa Anda menangis?", "Kenapa sih lu nangis?", "親しい詮索（どうしたの、なんで泣いてるの？）"),
            ("Bukan saya yang melakukan.", "Bukan gue sih pelakunya.", "控えめな否定（私じゃないと思うけどね）")
        ],
        "drill": [
            ("【Baku→Gaul】何を見てるの？（Apa yang sedang Anda lihat?）", "Liatin apaan sih?", "リアティン アパアン スィ", "疑問の和らげ apaan sih。"),
            ("【Gaul→Baku】美味しかったけど、ちょっと高かったね。（Enak sih, tapi mahal.）", "Makanannya lezat, akan tetapi harganya cukup mahal.", "マカナンニャ ルザット、アカン トゥタピ ハルガニャ チュクップ マハル", "控えめな留保 〜 sih, tapi...。"),
            ("【Baku→Gaul】本当に知らないの？（Apakah Anda sungguh-sungguh tidak tahu?）", "Beneran nggak tahu sih lu?", "ブネラン ンガッ タフ スィ ル", "意外性 sih。"),
            ("【Gaul→Baku】実は私も行きたいんだ。（Sebenernya gue pengen ikut sih.）", "Sejujurnya saya berkeinginan untuk ikut serta.", "スジュジュルニャ サヤ ブルクインギナン ウントゥッ イクット スルタ", "前置き sebenernya... sih。"),
            ("【Baku→Gaul】誰が言ったの？（Siapakah yang mengatakannya?）", "Siapa sih yang ngomong gitu?", "スィアパ スィ ヤン ンゴモン ギトゥ", "詮索 siapa sih。"),
            ("【Gaul→Baku】そうだけど、でもね。（Iya sih, tapi kan nggak gitu juga.）", "Hal tersebut memang benar, namun kenyataannya tidak demikian.", "ハル トゥルスブット メマン ブナル、ナムン クニャタアンニャ ティダッ ドゥミキアン", "受容と反論 Iya sih, tapi...。"),
            ("【Baku→Gaul】どうしてそんなに怒るの？（Mengapa Anda sangat marah?）", "Kenapa sih marah-marah mulu?", "クナパ スィ マラマラ ムル", "苛立ち・疑問 kenapa sih。"),
            ("【Gaul→Baku】私個人の意見としてはね。（Kalo menurut gue pribadi sih ya.）", "Apabila ditinjau dari sudut pandang pribadi saya.", "アパビラ ディティンジャウ ダリ スドゥット パンダン プリバディ サヤ", "私見表明 menurut gue sih。"),
            ("【Baku→Gaul】どこに置いてあったの？（Di manakah barang itu diletakkan?）", "Ditaruh di mana sih barangnya?", "ディタル ディ マナ スィ バランニャ", "疑問 di mana sih。"),
            ("【Gaul→Baku】変だなあ、さっきまであったのに。（Aneh sih, tadi ada di sini.）", "Sungguh aneh, padahal tadi masih ada di tempat ini.", "スング アネ、パダハル タディ マシ アダ ディ トゥムパット イニ", "違和感・意外性 aneh sih。"),
            ("【Baku→Gaul】何て言えばいいかな。（Apa yang sebaiknya saya katakan ya?）", "Gimana ya ngomongnya sih...", "ギマナ ヤ ンゴモンニャ スィ", "ためらい・思案。"),
            ("【Gaul→Baku】嫌いじゃないけど、あんまり好きでもない。（Bukannya nggak suka sih, cuma...）", "Bukan berarti saya membenci, hanya saja...", "ブカン ブルアルティ サヤ ムムベンチ、ハニャ サジャ", "遠回しな婉曲表現。"),
            ("【Baku→Gaul】いくらだった？（Berapakah harganya?）", "Berapaan sih harganya?", "ブラパアン スィ ハルガニャ", "疑問 berapaan sih。"),
            ("【Gaul→Baku】まあ、大丈夫だと思うよ。（Bakal aman-aman aja sih kayaknya.）", "Sepertinya semua akan baik-baik saja.", "スペルティニャ スムア アカン バイッバイッ サジャ", "控えめな見立て 〜 sih kayaknya。"),
            ("【Baku→Gaul】君の言う通りだね。（Perkataan Anda memang benar.）", "Bener juga sih kata lu.", "ブネル ジュガ スィ カタ ル", "納得 bener juga sih。")
        ],
        "quiz": [
            ("文末詞「sih」が「Iya sih, tapi...」という文脈で果たす役割は？", ["相手の意見を一旦受け止めつつ、留保・反論を柔らかく添える", "相手を激しく罵倒する", "文を疑問文に変える", "過去の完了を表す"], 1),
            ("「Kenapa sih lu?」というフレーズの持つニュアンスは？", ["「どうしたの？（親しい心配や軽い呆れ）」", "「何時刻に出発ですか？」", "「お名前は何ですか？」", "「お会計はいくらですか？」"], 1),
            ("「Bener juga sih」が表す意味は？", ["「言われてみれば確かにそうだね（納得）」", "「絶対に間違いだ」", "「信じられない」", "「嘘をつくな」"], 1)
        ]
    }
]

# docs/diglossia ディレクトリの存在確認
os.makedirs("docs/diglossia", exist_ok=True)

for a in articles_data:
    filepath = os.path.join("docs/diglossia", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. コードスイッチング対比表（Baku標準語 ⇄ Gaul口語）\n")
    lines.append("| No | 公式標準語 (Bahasa Baku) | 街角口語 (Bahasa Gaul) | 意味・ニュアンス |")
    lines.append("|---|---|---|---|")
    for idx, (baku, gaul, meaning) in enumerate(a['pairs'], 1):
        lines.append(f"| {idx} | `{baku}` | **{gaul}** | {meaning} |")
    lines.append("")
    
    lines.append("## 2. 構文・音韻変化のメカニズム\n")
    lines.append("公式標準語の文法構造が、口語においてどのように短縮・脱落・母音変容（音韻融合）を起こしているかを理解することで、リスニングの「聞き取れない壁」を突破し、自然な発話が可能になります。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 双方向コード変換ドリル（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語と提示された文を見て、指定されたレジスター（Baku → Gaul または Gaul → Baku）へ1〜2秒以内に口頭で言い換えてください。\n")
    
    for idx, (prompt, target_sent, kana, exp) in enumerate(a['drill'], 1):
        import re
        m = re.match(r'^(【.+?】)(.+?)（(.+?)）$', prompt)
        if m:
            tag, jp, orig = m.group(1), m.group(2), m.group(3)
            lines.append(f"### 第{idx}問: {tag}「**{jp}**」（{orig}）\n")
        else:
            lines.append(f"### 第{idx}問: 「**{prompt}**」\n")
        lines.append('<div class="id-example">')
        lines.append(f'<div class="id-sentence"><strong>{target_sent}</strong></div>')
        lines.append(f'<div class="id-pronunciation">発音: {kana}</div>')
        lines.append(f'<div class="id-translation">解説: {exp}</div>')
        lines.append('</div>\n')
    
    lines.append("## 4. 理解度チェッククイズ\n")
    for q_idx, (q_text, opts, ans_idx) in enumerate(a['quiz'], 1):
        lines.append(f"### 問{q_idx}: {q_text}\n")
        for o_idx, opt in enumerate(opts, 1):
            mark = " (正解)" if o_idx == ans_idx else ""
            lines.append(f"- [{ 'x' if o_idx == ans_idx else ' ' }] {o_idx}. {opt}{mark}")
        lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated: {filepath}")

print("Batch 1101-1110 generated successfully.")
