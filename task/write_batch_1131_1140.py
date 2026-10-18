# -*- coding: utf-8 -*-
import os
import re

articles_data = [
    {
        "slug": "31-javanese-colloquial-elements",
        "title": "【二重言語】ジャワ語借用語の日常混入：monggo, suwun, piye, opo, rek の親密会話",
        "intro": "ジャカルタや全国の口語会話では、人口の最大派閥であるジャワ人の文化的影響により、ジャワ語（Bahasa Jawa）の単語が挨拶や相槌、感嘆詞として自然に混入します。「monggo（どうぞ）」「suwun（ありがとう）」「piye（どう？）」「opo（何？）」など、耳にした瞬間に距離をグッと縮める日常語彙を学びます。",
        "pairs": [
            ("silakan (どうぞ)", "monggo", "お先にどうぞ、召し上がれ"),
            ("terima kasih (ありがとう)", "matur nuwun / suwun", "ジャワ風の温かい感謝"),
            ("bagaimana (どうですか)", "piye / kepiye", "近況確認・相談のどう？"),
            ("apa (何ですか)", "opo / opoan", "何それ？どんな用事？")
        ],
        "drill": [
            ("【Baku→Gaul】どうぞ、先にお召し上がりください。（Silakan makan lebih dulu.）", "Monggo mas, dicicipi dulu hidangannya.", "モンゴ マス、ディチチピ ドゥル ヒダンガンニャ", "monggo ⇄ silakan。"),
            ("【Gaul→Baku】本当にありがとうね！（Matur nuwun sanget ya mas!）", "Terima kasih banyak atas segala bantuannya.", "トゥリマ カシ バニャッ アタス スガラ バントゥアンニャ", "matur nuwun ⇄ terima kasih。"),
            ("【Baku→Gaul】今日の調子はどう？（Bagaimana kabarmu hari ini?）", "Piye kabare bro? Sehat-sehat kan?", "ピエ カバレ ブロ？ セハット セハット カン", "piye ⇄ bagaimana。"),
            ("【Gaul→Baku】これ何？（Opo iki rek?）", "Apa maksud dari benda atau hal ini kawan?", "アパ マクスッド ダリ ブンダ アタウ ハル イニ カワン", "opo iki ⇄ apa ini。"),
            ("【Baku→Gaul】もう帰るの？（Kamu sudah mau pulang sekarang?）", "Udah mau mulih mas?", "ウダ マウ ムリッ マス", "mulih ⇄ pulang。"),
            ("【Gaul→Baku】全然大丈夫だよ！（Ora popo, santai aja rek!）", "Tidak apa-apa, semuanya baik-baik saja kawan.", "ティダッ アパ アパ、スムアニャ バイッ バイッ サジャ カワン", "ora popo ⇄ tidak apa-apa。"),
            ("【Baku→Gaul】少し待ってください。（Mohon tunggu sebentar.）", "Sek yo, nunggu sedelok.", "セッ ヨ、ヌング スドロッ", "sedelok ⇄ sebentar。"),
            ("【Gaul→Baku】本当に疲れたよ。（Boyokku pegel kabeh rek.）", "Pinggang saya terasa sangat pegal kawan-kawan.", "ピンガン サヤ トゥラサ サンガット プガル カワン カワン", "boyok ⇄ pinggang, kabeh ⇄ semua。"),
            ("【Baku→Gaul】本当にすごいね！（Wah hebat sekali kamu.）", "Jan jos tenan kowe mas!", "ジャン ジョス トゥナン コウェ マス", "jos tenan ⇄ hebat / mantap sekali。"),
            ("【Gaul→Baku】どこに行くの？（Mau nandi kowe?）", "Hendak pergi ke manakah Anda?", "フンダッ プルギ ク マナカ アンダ", "nandi ⇄ ke mana, kowe ⇄ kamu。"),
            ("【Baku→Gaul】嘘でしょう、ありえない。（Masa sih? Tidak mungkin.）", "Mosok sih? Ora percoyo aku.", "モソッ スィ？ オラ プルチョヨ アク", "mosok ⇄ masa sih。"),
            ("【Gaul→Baku】もったいない！（Eman-eman banget makanannya.）", "Sangat sayang sekali bila makanan ini terbuang.", "サンガット サヤン スカリ ビラ マカナン イニ トゥルブアン", "eman ⇄ sayang / mubazir。"),
            ("【Baku→Gaul】眠くてたまらない。（Saya merasa sangat mengantuk sekali.）", "Ngantuk pol rek, ra kuat melek.", "ンアントゥッ ポル レッ、ラ クアット ムレッ", "pol ⇄ sangat, melek ⇄ bangun。"),
            ("【Gaul→Baku】どうしてそんなことするの？（Ngopo kok koyo ngono?）", "Mengapa Anda berbuat hal seperti demikian?", "ムンアパ アンダ ブルブアット ハル スプルティ ドゥミキアン", "ngopo ⇄ kenapa, koyo ngono ⇄ seperti itu。"),
            ("【Baku→Gaul】みんなで一緒に食べよう。（Mari kita makan bersama teman-teman.）", "Ayo mangan bareng rek!", "アヨ マンガン バレン レッ", "mangan ⇄ makan, bareng ⇄ bersama。")
        ],
        "quiz": [
            ("ジャワ語由来で、全国的にも「どうぞお入りください/どうぞお食べください」と勧める挨拶は？", ["monggo", "suwun", "piye", "opo"], 1),
            ("「全然気にしないで、大丈夫だよ」をジャワ語混じりで親密に言う定番フレーズは？", ["ora popo", "koyo ngono", "jos tenan", "eman-eman"], 1),
            ("友人たちを「みんな、仲間たち」と呼びかける東ジャワ・ジャワ方言特有の呼びかけ詞は？", ["rek (arek)", "kelen", "lae", "cuy"], 1)
        ]
    },
    {
        "slug": "32-sundanese-colloquial-elements",
        "title": "【二重言語】スンダ語借用語の西ジャワ口語：teh, mah, atuh, euy, punten, nuhun",
        "intro": "バンドンをはじめとする西ジャワ州（スンダ地方）のインドネシア語には、独特の柔らかなイントネーションとともに、スンダ語（Bahasa Sunda）の小詞や挨拶が濃厚に混じります。「punten（すみません）」「nuhun（ありがとう）」「atuh（〜だよ）」「mah（〜はね）」など、会話に柔らかさと愛嬌を添えるスンダ要素を学びます。",
        "pairs": [
            ("permisi / maaf (すみません)", "punten", "道を通る時・声かけの丁寧な前置き"),
            ("terima kasih (ありがとう)", "hatur nuhun / nuhun", "スンダ式の心温まる感謝"),
            ("dong / tentu saja (〜ですよ)", "atuh", "柔らかく念を押す文末小詞"),
            ("ya ampun / kawan (おい/まあ)", "euy", "親しい呼びかけ・感嘆の文末詞")
        ],
        "drill": [
            ("【Baku→Gaul】すみません、通してください。（Permisi, boleh minta jalan?）", "Punten nya, numpang lewat.", "プンテン ニャ、ヌンパン レワット", "punten ⇄ permisi。"),
            ("【Gaul→Baku】本当にありがとうございました！（Hatur nuhun pisan kang!）", "Terima kasih banyak atas segala bantuannya saudara.", "トゥリマ カシ バニャッ アタス スガラ バントゥアンニャ サウダラ", "hatur nuhun pisan ⇄ terima kasih banyak。"),
            ("【Baku→Gaul】私について言えば、行きたくないです。（Kalau saya sendiri, tidak mau pergi.）", "Abdi mah alim angkat atuh.", "アブディ マ アリム アンカット アトゥ", "mah ⇄ kalau / topik marker。"),
            ("【Gaul→Baku】もちろん一緒に行こうよ！（Ikut atuh euy, masa nggak ikut!）", "Tentu saja mari ikut bersama kami kawan.", "トゥントゥ サジャ マリ イクット ブルサマ カミ カワン", "atuh euy ⇄ dong / tentu saja。"),
            ("【Baku→Gaul】お兄さん、この服はいくらですか？（Berapa harga baju ini, mas?）", "Sabaraha ieu teh mang?", "サバラハ イエウ テ マン", "sabaraha ⇄ berapa, ieu teh ⇄ ini。"),
            ("【Gaul→Baku】美味しい、たまらない！（Geulis pisan euy pemandangannya!）", "Pemandangan ini sungguh sangat indah sekali kawan.", "プマンダンアン イニ スング サンガット インダ スカリ カワン", "geulis / endah pisan ⇄ indah sekali。"),
            ("【Baku→Gaul】もう帰ったの？（Apakah dia sudah pulang?）", "Udah mulih kitu manehna teh?", "ウダ ムリッ キトゥ マネナ テ", "teh ⇄ 強調・特定小詞。"),
            ("【Gaul→Baku】美味しくて止まらない！（Raos pisan ieu baso teh.）", "Bakso ini terasa sangat lezat sekali.", "バッソ イニ トゥラサ サンガット ルザット スカリ", "raos pisan ⇄ enak sekali。"),
            ("【Baku→Gaul】急がないで、ゆっくり行こう。（Jangan terburu-buru, santai saja.）", "Tong rusuh atuh, lalaunan weh.", "トン ルスッ アトゥ、ララウナン ウェ", "tong ⇄ jangan, lalaunan ⇄ pelan-pelan。"),
            ("【Gaul→Baku】どうしてそんなに怒ってるの？（Naha ambek-ambekan kitu atuh?）", "Mengapa Anda tampak begitu marah sekali?", "ムンアパ アンダ タンパッ ブギトゥ マラ スカリ", "naha ⇄ kenapa, ambek ⇄ marah。"),
            ("【Baku→Gaul】本当に暑いですね！（Wah hawanya terasa sangat panas sekali.）", "Hareudang pisan euy poe ieu!", "ハレウダン ピサン エウイ ポエ イエウ", "hareudang ⇄ panas gerah。"),
            ("【Gaul→Baku】もうお腹いっぱい！（Kasep pisan euy bajunya.）", "Pakaian tersebut tampak sangat rapi dan tampan kawan.", "パカイアン トゥルスブット タンパッ サンガット ラピ ダン タンパン カワン", "kasep ⇄ tampan / keren。"),
            ("【Baku→Gaul】ちょっと待ってください。（Tunggu sebentar ya.）", "Sakedap nya, antosan sakedik.", "サクダップ ニャ、アントサン サクディッ", "sakedap ⇄ sebentar。"),
            ("【Gaul→Baku】どこに行くの？（Bade kamana atuh kang?）", "Hendak bepergian ke manakah Anda saudara?", "フンダッ ブプルギアン ク マナカ アンダ サウダラ", "bade kamana ⇄ mau ke mana。"),
            ("【Baku→Gaul】雨がすごく降ってきた。（Hujan turun sangat deras sekali di luar.）", "Hujan ageung pisan euy di luar!", "フジャン アグン ピサン エウイ ディ ルアル", "ageung ⇄ besar, pisan ⇄ sekali。")
        ],
        "quiz": [
            ("スンダ語由来で、道を通る時や会話の切り出しに使う丁寧な「すみません」は？", ["punten", "nuhun", "atuh", "euy"], 1),
            ("感謝を伝える「ありがとう」のスンダ語表現は？", ["hatur nuhun", "punten", "hareudang", "sabaraha"], 1),
            ("文末で「〜だよ」「もちろん〜しよう」と柔らかく相手を促すスンダ語特有の小詞は？", ["atuh", "dong", "sih", "kok"], 1)
        ]
    },
    {
        "slug": "33-chinese-indonesian-peranakan",
        "title": "【二重言語】中華系インドネシア語（プラナカン語彙）：cuan, hoki, cincai, cici, koko",
        "intro": "インドネシアの商業都市やビジネス界、若者カルチャーには、閩南語（ホッケン語）などの中華系方言にルーツを持つ語彙（プラナカン語彙）が深く定着しています。「cuan（利益・儲け）」「hoki（幸運）」「cincai（適当に・お任せで）」「koko / cici（お兄さん・お姉さん）」など、商談や投資、日常会話で頻出する必須語彙を学びます。",
        "pairs": [
            ("keuntungan (利益・儲け)", "cuan", "株・ビジネス・副業の利益"),
            ("keberuntungan (幸運・ラッキー)", "hoki", "運の良さ・ツキ"),
            ("mudah / fleksibel (柔軟に・適当に)", "cincai", "細かいことは気にせず融通を利かせる"),
            ("kakak laki-laki / perempuan", "koko / cici", "親愛を込めた呼称")
        ],
        "drill": [
            ("【Baku→Gaul】今回の投資で大きな利益が出ました。（Investasi ini menghasilkan keuntungan besar.）", "Wih mantap, cuan gede nih dari kripto!", "ウィッ マンタップ、チュアン グデ ニ ダリ クリプト", "cuan ⇄ keuntungan。"),
            ("【Gaul→Baku】今日は本当に運が良かった！（Hoki banget gue hari ini, dapet tiket murah.）", "Saya merasa sangat beruntung sekali hari ini.", "サヤ ムラサ サンガット ブルウントゥン スカリ ハリ イニ", "hoki ⇄ beruntung。"),
            ("【Baku→Gaul】値段は適当に安くしておいてよ。（Tolong beri kelonggaran harga yang fleksibel.）", "Udah cincai lah harganya sama kawan sendiri.", "ウダ チンチャイ ラ ハルガニャ サマ カワン スンディリ", "cincai ⇄ fleksibel / santai。"),
            ("【Gaul→Baku】お姉さん、この服を見せてください。（Ci, mau liat model baju yang ini dong.）", "Permisi kakak, saya ingin melihat contoh pakaian ini.", "プルミスィ カカッ、サヤ インギン ムリハット チョント パカイアン イニ", "cici (ci) ⇄ kakak perempuan。"),
            ("【Baku→Gaul】損をしてしまいました。（Kami mengalami kerugian modal yang cukup besar.）", "Yah boncos deh, rugi banyak bulan ini.", "ヤー ボンチョス デ、ルギ バニャッ ブラン イニ", "boncos ⇄ rugi / pengeluaran jebol。"),
            ("【Gaul→Baku】本当にケチなおじさんだな。（Pelit amat tuh engkoh, pelici.）", "Pria paruh baya tersebut sangat berhati-hati dan kikir dengan uang.", "プリア パル バーヤ トゥルスブット サンガット ブルハティ ハティ ダン キキル ドゥンガン ウアン", "engkoh ⇄ paman / om Tionghoa。"),
            ("【Baku→Gaul】お兄さん、コーヒーのおかわりをください。（Mas, tolong tambah satu kopi lagi.）", "Ko, nambah es kopi satu lagi ya.", "コ、ナンバ エス コピ サトゥ ラギ ヤ", "koko (ko) ⇄ kakak laki-laki。"),
            ("【Gaul→Baku】元が取れたよ！（Udah balik modal nih, BP.）", "Modal usaha kami sudah berhasil kembali secara utuh.", "モダル ウサハ カミ スダ ブルハシル クンバリ スチャラ ウトゥ", "balik modal ⇄ BEP。"),
            ("【Baku→Gaul】彼はお金持ちの御曹司だ。（Dia adalah anak orang yang sangat berada.）", "Crazy rich dia mah, tajir melintir abis.", "クレイジー リッチ ディア マ、タジール ムリンティール アビス", "tajir melintir ⇄ kaya raya。"),
            ("【Gaul→Baku】領収書をください。（Minta bon pembeliannya dong ci.）", "Tolong berikan kuitansi atau nota resmi dari transaksi ini.", "トロン ブリカン クイタンシ アタウ ノタ レスミ ダリ トランサクスィ イニ", "bon ⇄ kuitansi / nota。"),
            ("【Baku→Gaul】嘘をつかないで正直に言って。（Tolong jangan berbohong kepada saya.）", "Jangan suka culas dong, harus jujur.", "ジャンガン スカ チュラス ドン、ハルス ジュジュール", "culas ⇄ curang / tidak jujur。"),
            ("【Gaul→Baku】ただのくだらないおしゃべり。（Cuma omong kosong doang, cap cai.）", "Percakapan tersebut hanya berupa pembicaraan tanpa arti.", "プルチャカパン トゥルスブット ハニャ ブルパ プンビチャラアン タンパ アルティ", "cap cai ⇄ campur aduk / omong kosong。"),
            ("【Baku→Gaul】彼のビジネスはとても繁盛している。（Usaha miliknya berkembang sangat pesat sekali.）", "Tokonya laris manis tanjung kimpul, hoki terus!", "トコニャ ラリス マニス タンジュン キンプル、ホキ トゥルス", "laris manis ⇄ laris sekali。"),
            ("【Gaul→Baku】割り勘にしよう。（Kita patungan aja ya ci makannya.）", "Mari kita membagi biaya makanan ini secara merata.", "マリ キタ ムンバギ ビアヤ マカナン イニ スチャラ ムラタ", "patungan ⇄ bagi rata。"),
            ("【Baku→Gaul】もうこれ以上損を拡大させたくない。（Kita harus membatasi kerugian saat ini juga.）", "Harus cut loss sekarang sebelum makin boncos!", "ハルス カット ロス スカラン スブルム マキン ボンチョス", "cut loss ⇄ batasi rugi。")
        ],
        "quiz": [
            ("ビジネスや投資で「儲け・利益」を意味する最も一般的な中華系スラングは？", ["cuan", "hoki", "cincai", "boncos"], 1),
            ("商談や価格交渉で「細かいことは言わず適当に安くして・柔軟にやって」を意味する語は？", ["cincai", "cuan", "hoki", "koko"], 1),
            ("中華系女性に対して親愛を込めて呼ぶ「お姉さん」の呼称は？", ["cici (ci)", "koko (ko)", "engkoh", "tante"], 1)
        ]
    },
    {
        "slug": "34-surabaya-east-java-slang",
        "title": "【二重言語】スラバヤ・東ジャワの熱い口語：arek, cak, rek, ta, ojok の親密構文",
        "intro": "インドネシア第2の都市スラバヤを中心とする東ジャワ口語（Bahasa Jawa Suroboyoan / Malangan）は、歯切れの良いテンポと強い直球の親密さが魅力です。「arek（若者・子ども）」「cak（兄貴・お兄さん）」「rek（みんな）」「ta（〜なの？疑問）」「ojok（〜するな）」など、ジャカルタ口語とは一味違う熱い表現を体得します。",
        "pairs": [
            ("anak-anak / pemuda (若者・子ども)", "arek-arek", "スラバヤっ子・仲間たち"),
            ("jangan (〜するな・やめて)", "ojok", "禁止を表す東ジャワ方言"),
            ("apakah ya? (〜なの？)", "... ta?", "文末の疑問詞（〜か？）"),
            ("kakak laki-laki (お兄さん)", "cak", "スラバヤでの男性敬称・呼びかけ")
        ],
        "drill": [
            ("【Baku→Gaul】みんな、どこにご飯食べに行く？（Kalian mau pergi makan di mana kawan?）", "Mangan nandi rek awan-awan ngene?", "マンガン ナンディ レッ アワン アワン ンゲネ", "rek ⇄ kawan-kawan, mangan ⇄ makan。"),
            ("【Gaul→Baku】兄貴、これいくら？（Cak, piro regane iki?）", "Berapakah harga barang ini wahai saudara penjual?", "ブラパカ ハルガ バラン イニ ワハイ サウダラ プンジュアル", "cak ⇄ mas / abang, piro ⇄ berapa。"),
            ("【Baku→Gaul】そんなことしないで！（Tolong jangan lakukan hal itu!）", "Ojok ngono ta rek, sing genah sitik!", "オジョッ ンオノ タ レッ、シン グナ スィティッ", "ojok ⇄ jangan, ngono ⇄ begitu。"),
            ("【Gaul→Baku】本当に行くの？（Sido melu ta koen?）", "Apakah Anda jadi ikut bersama rombongan kami?", "アパカ アンダ ジャディ イクット ブルサマ ロンボンガン カミ", "sido ⇄ jadi, ta ⇄ kah, koen ⇄ kamu。"),
            ("【Baku→Gaul】スラバヤの若者たちは元気いっぱいだ。（Pemuda Surabaya sangat bersemangat.）", "Arek Suroboyo ancen wani tenan!", "アレック スロボヨ アンチェン ワニ トゥナン", "arek ⇄ anak muda, wani ⇄ berani。"),
            ("【Gaul→Baku】めちゃくちゃ暑い！（Panas pol rek hawane dino iki.）", "Suhu udara hari ini terasa luar biasa panas sekali.", "スフ ウダラ ハリ イニ トゥラサ ルアル ビアサ パナス スカリ", "panas pol ⇄ panas sekali。"),
            ("【Baku→Gaul】冗談はやめてくれ。（Jangan berbicara sembarangan tanpa bukti.）", "Ojok ngguyu ta, aku iki tenanan!", "オジョッ ンギュユ タ、アク イキ トゥナナアン", "ojok ngguyu ⇄ jangan tertawa, tenanan ⇄ serius。"),
            ("【Gaul→Baku】全部嘘ばっかり！（Nggedebus kabeh omongane!）", "Semua perkataannya hanyalah bualan belaka.", "スムア プルカタアンニャ ハニャラ ブアラン ブラカ", "nggedebus ⇄ omong kosong, kabeh ⇄ semua。"),
            ("【Baku→Gaul】美味しくてたまらない。（Rasanya sungguh sangat nikmat sekali.）", "Uenak pol rawon iki cak!", "ウエナッ ポル ラウォン イキ チャッ", "uenak pol ⇄ enak sekali。"),
            ("【Gaul→Baku】そんなの当たり前だよ。（Iyo lah, pancen koyo ngono ancene.）", "Tentu saja, hal tersebut sudah semestinya demikian.", "トゥントゥ サジャ、ハル トゥルスブット スダ スムスティニャ ドゥミキアン", "ancen / pancen ⇄ memang。"),
            ("【Baku→Gaul】これ誰の財布？（Dompet siapakah ini gerangan?）", "Dompete sopo iki rek?", "ドンペテ ソポ イキ レッ", "sopo ⇄ siapa。"),
            ("【Gaul→Baku】もう帰りたい。（Wis kape mulih aku rek, ngantuk.）", "Saya sudah bersiap-siap untuk pulang karena mengantuk.", "サヤ スダ ブルスィアップ スィアップ ウントゥッ プラン カレナ ムンアントゥッ", "wis ⇄ sudah, kape ⇄ mau, mulih ⇄ pulang。"),
            ("【Baku→Gaul】急がないで、落ち着いて。（Tolong tenang dan jangan panik.）", "Ojok kesusu ta, kalem ae napa.", "オジョッ クスス タ、カレム アエ ナパ", "kesusu ⇄ terburu-buru。"),
            ("【Gaul→Baku】本当にひどい！（Jancuk, apes pol dino iki!）", "Aduh, sungguh malang sekali nasib saya hari ini.", "アドゥ、スング マラン スカリ ナスィブ サヤ ハリ イニ", "apes pol ⇄ sial sekali。"),
            ("【Baku→Gaul】明日また会おう。（Sampai berjumpa kembali besok hari kawan.）", "Ketemu maneh sesuk yo rek!", "クトゥム マネ ススッ ヨ レッ", "maneh ⇄ lagi, sesuk ⇄ besok。")
        ],
        "quiz": [
            ("東ジャワ口語で「〜するな（禁止）」を表す代表的な単語は？", ["ojok", "jangan", "tong", "ora"], 1),
            ("スラバヤで疑問文の末尾につけて「〜なの？/〜か？」と確認する小詞は？", ["ta", "kah", "sih", "kan"], 1),
            ("スラバヤや東ジャワで男性に対して使う親密な敬称・呼びかけは？", ["cak", "mas", "bang", "kang"], 1)
        ]
    },
    {
        "slug": "35-medan-north-sumatra-elements",
        "title": "【二重言語】メダン・北スマトラの直球口語：kali, kelen, awak, cemmana, lae",
        "intro": "北スマトラ州メダンを中心とするスマトラ口語（Bahasa Medan）は、バタク文化やマレー語、中国語が融合した力強いイントネーションと、極めてダイレクトな語彙が特徴です。「kali（とても）」「kelen（君たち）」「awak（私/私たち）」「cemmana（どうやって/どうなの）」「lae（義兄弟・親友）」など、メダン独特の語彙を学びます。",
        "pairs": [
            ("sangat / sekali (とても・すごく)", "... kali", "形容詞の後に置いて強調"),
            ("kalian (君たち・お前ら)", "kelen", "2人称複数のメダン方言"),
            ("saya / kita (私・俺たち)", "awak", "親密な自称"),
            ("bagaimana (どうやって・どうなの)", "cemmana", "疑問詞のメダン短縮形")
        ],
        "drill": [
            ("【Baku→Gaul】今日は本当に暑い！（Hari ini sangat panas sekali rasanya.）", "Panas kali bah hari ini, gersang!", "パナス カリ バー ハリ イニ、ゲルサン", "panas kali ⇄ sangat panas。"),
            ("【Gaul→Baku】君たち、どこ行くの？（Mau kemana kelen woi?）", "Hendak bepergian ke manakah kalian semua?", "フンダッ ブプルギアン ク マナカ カリアン スムア", "kelen ⇄ kalian。"),
            ("【Baku→Gaul】どうやって解決すればいい？（Bagaimana cara kita menyelesaikannya?）", "Cemmana ini lae, pening awak!", "チュンマナ イニ ラエ、プニン アワッ", "cemmana ⇄ bagaimana, lae ⇄ kawan。"),
            ("【Gaul→Baku】私は全然知らないよ。（Awak mana tau soal masalah itu!）", "Saya sama sekali tidak mengetahui perihal masalah tersebut.", "サヤ サマ スカリ ティダッ ムンゲタフイ プリハル マサラ トゥルスブット", "awak ⇄ saya / aku。"),
            ("【Baku→Gaul】本当に美味しい！（Masakan ini sungguh sangat lezat sekali.）", "Sedap kali kuahnya bah, paten!", "スダップ カリ クアニャ バー、パテン", "sedap kali ⇄ sangat lezat, paten ⇄ mantap。"),
            ("【Gaul→Baku】大げさに騒ぐな！（Jangan ribut-ribut kali lah kelen!）", "Dimohon untuk tidak menimbulkan kegaduhan berlebihan.", "ディモホン ウントゥッ ティダッ ムニンブルカン クガドゥハン ブルレビハン", "ribut-ribut kali ⇄ terlalu ribut。"),
            ("【Baku→Gaul】とても遠い場所にある。（Tempat itu letaknya sangat jauh sekali.）", "Jauh kali lokasinya lae, payah kali kesana.", "ジャウ カリ ロカスィニャ ラエ、パヤ カリ クサナ", "jauh kali ⇄ sangat jauh, payah ⇄ sulit。"),
            ("【Gaul→Baku】かっこいい服だね！（Paten kali kutengok gayamu bro!）", "Gaya penampilan Anda tampak sangat rapi dan menarik.", "ガヤ プナンピラン アンダ タンパッ サンガット ラピ ダン ムナリッ", "paten ⇄ keren / mantap, kutengok ⇄ kulihat。"),
            ("【Baku→Gaul】嘘ばかりついている。（Orang tersebut selalu berbicara bohong.）", "Kombur doang kerjanya, cakap besar!", "コンブール ドアン クルジャニャ、チャカップ ブサール", "kombur ⇄ omong kosong / gosip。"),
            ("【Gaul→Baku】頭が痛くて割れそうだ。（Pening kali kepala awak mikirin utang.）", "Kepala saya terasa sangat pusing memikirkan tanggungan utang.", "プパラ サヤ トゥラサ サンガット プスィン ムミキルカン タングンガン ウタン", "pening kali ⇄ sangat pusing。"),
            ("【Baku→Gaul】さっさと歩きなさい。（Berjalanlah dengan lebih cepat sedikit.）", "Cepat sikit jalannya, lambat kali kelen!", "チュパット スィキット ジャランニャ、ランバット カリ クレン", "sikit ⇄ sedikit, lambat kali ⇄ sangat lambat。"),
            ("【Gaul→Baku】どうして急に怒るの？（Ngapain kau mendadak emosi gitu lae?）", "Mengapa Anda tiba-tiba menjadi sangat emosional kawan?", "ムンアパ アンダ ティバ ティバ ムンジャディ サンガット エモシオナル カワン", "ngapain kau ⇄ mengapa kamu。"),
            ("【Baku→Gaul】信じられないほど安い。（Harga barang ini murah sekali di luar nalar.）", "Murah kali harganya bah, borong yok!", "ムラ カリ ハルガニャ バー、ボロン ヨッ", "murah kali ⇄ sangat murah, yok ⇄ yuk。"),
            ("【Gaul→Baku】そんなの朝飯前だよ。（Cincai itu, hal kecil gampang kali!）", "Perkara tersebut sangat mudah untuk diselesaikan.", "プルカラ トゥルスブット サンガット ムダ ウントゥッ ディスルサイカン", "gampang kali ⇄ sangat mudah。"),
            ("【Baku→Gaul】元気だったか相棒！（Bagaimana kabarmu kawan lamaku?）", "Sehat kau kan lae? Lama tak sua!", "セハット カウ カン ラエ？ ラマ タッ スア", "lae ⇄ kawan / ipar, tak sua ⇄ tak jumpa。")
        ],
        "quiz": [
            ("メダン口語で形容詞の後につけて「とても・すごく」を強調する代表語は？", ["kali", "banget", "pisan", "pol"], 1),
            ("メダン弁で「君たち（2人称複数）」を指す方言は？", ["kelen", "kalian", "rek", "lu pada"], 1),
            ("疑問詞「bagaimana（どうやって・どうなの）」のメダン口語の短縮形は？", ["cemmana", "gimana", "piye", "kumaha"], 1)
        ]
    },
    {
        "slug": "36-movie-subtitles-vs-audio",
        "title": "【二重言語】映画・ドラマ字幕の二重性：文字字幕（Baku）⇄ 実際の発話（Gaul）の徹底比較",
        "intro": "Netflixや映画のインドネシア語作品を見るとき、画面に表示される公式字幕（Subtitles）は端正な「Bahasa Baku（標準語）」に要約されますが、俳優が実際に話している台詞（Audio）は超リアルな「Bahasa Gaul（口語スラング）」です。この二重性を対比して聴き取る力を鍛えます。",
        "pairs": [
            ("Apakah kamu sedang bercanda?", "Lu lagi ngelawak apa gimana sih?", "字幕の形式 ⇄ 実際の発話の苛立ち"),
            ("Saya tidak peduli dengan hal itu.", "Bodo amat lah, emang gue pikirin!", "字幕の無関心 ⇄ 実際の冷酷な突き放し"),
            ("Mari kita bicarakan secara baik-baik.", "Ngobrol santai dulu napa, jangan ngegas!", "字幕の理性的対話 ⇄ 実際の喧嘩腰抑制"),
            ("Dia sengaja menyembunyikan kebenaran.", "Dia sengaja nutup-nutupin faktanya tuh.", "字幕の客観叙述 ⇄ 実際の口語動詞")
        ],
        "drill": [
            ("【字幕(Baku)→発話(Gaul)】何を考えているのですか？（Apa yang sedang Anda pikirkan?）", "Mikir apaan sih lu dari tadi melamun mulu?", "ミキール アパアン スィ ル ダリ タディ ムラムン ムル", "字幕標準語 ⇄ リアル口語ツッコミ。"),
            ("【発話(Gaul)→字幕(Baku)】勝手にすれば！（Terserah lu dah, males gue ngurusinnya!）", "Saya menyerahkan keputusan sepenuhnya kepada Anda.", "サヤ ムニュラカン クプトゥサン スプヌフニャ クパダ アンダ", "激怒突き放し ⇄ 字幕公式表現。"),
            ("【字幕(Baku)→発話(Gaul)】私は彼を全く信用していません。（Saya sama sekali tidak mempercayai dirinya.）", "Nggak percaya sama sekali gue sama tuh bocah.", "ンガッ プルチャヤ サマ スカリ グエ サマ トゥ ボチャ", "否定前置口語。"),
            ("【発話(Gaul)→字幕(Baku)】煽るのやめてくれない？（Gausah mancing-mancing emosi gue napa!）", "Mohon jangan memprovokasi kemarahan saya.", "モホン ジャンガン ムンプロヴォカスィ クマラハン サヤ", "口語怒り ⇄ 字幕標準要約。"),
            ("【字幕(Baku)→発話(Gaul)】私たちは罠にはめられたのだ。（Kita telah dijebak oleh mereka.）", "Kena jebak kita rek, kena tipu mentah-mentah!", "クナ ジュバッ キタ レッ、クナ ティプ ムンタ ムンタ", "ke-受動＋口語強調。"),
            ("【発話(Gaul)→字幕(Baku)】そんなはずないだろ！（Mana mungkin anjir, jangan ngarang lu!）", "Hal tersebut sangat tidak masuk akal sekali.", "ハル トゥルスブット サンガット ティダッ マスッ アカル スカリ", "口語否定 ⇄ 字幕論理表現。"),
            ("【字幕(Baku)→発話(Gaul)】彼らはすでに立ち去りました。（Mereka telah meninggalkan tempat ini.）", "Udah pada kabur orang-orangnya dari tadi.", "ウダ パダ カブール オラン オランニャ ダリ タディ", "kabur ⇄ pergi / meninggalkan。"),
            ("【発話(Gaul)→字幕(Baku)】勘違いしないでよね。（Jangan geer dulu lu, gue cuma nolongin!）", "Tolong jangan berprasangka bahwa saya menyukai Anda.", "トロン ジャンガン ブルプラサンカ バフワ サヤ ムニュカイ アンダ", "geer (gede rasa) ⇄ salah sangka。"),
            ("【字幕(Baku)→発話(Gaul)】すぐに警察に通報してください。（Segera hubungi pihak kepolisian.）", "Buruan lapor polisi skrg juga!", "ブルアン ラポル ポリシスィ スカラン ジュガ", "buruan ⇄ segera。"),
            ("【発話(Gaul)→字幕(Baku)】頭がおかしいんじゃないの？（Gila lu ya, gak ada otak apa gimana?）", "Apakah tindakan Anda ini masih terbilang waras?", "アパカ ティンダカン アンダ イニ マスィ トゥルビラン ワラス", "口語罵倒 ⇄ 字幕婉曲批判。"),
            ("【字幕(Baku)→発話(Gaul)】私は約束を守ります。（Saya pasti akan menepati janji saya.）", "Janji gue gak bakal gue ingkarin kok.", "ジャンジ グエ ガッ バカル グエ インカリン コッ", "口語約束。"),
            ("【発話(Gaul)→字幕(Baku)】さっさと白状しろよ！（Ngaku aja lu buruan, jangan muter-muter!）", "Akuilah perbuatan Anda tanpa berbelit-belit.", "アクイラ プルブアタン アンダ タンパ ブルブリット ブリット", "口語尋問 ⇄ 字幕公式命令。"),
            ("【字幕(Baku)→発話(Gaul)】彼にはまだ未練がある。（Tampaknya ia masih menyimpan perasaan.）", "Keliatan bgt masih gamon tuh orang.", "クリアタン バンゲット マスィ ガモン トゥ オラン", "gamon (gagal move on) ⇄ belum lupa。"),
            ("【発話(Gaul)→字幕(Baku)】もううんざりだ。（Enek gue lama-lama liat drama lu!）", "Saya sudah merasa sangat jenuh dengan semua kepalsuan ini.", "サヤ スダ ムラサ サンガット ジュヌ ドゥンガン スムア クパルスアン イニ", "enek ⇄ muak / jenuh。"),
            ("【字幕(Baku)→発話(Gaul)】さようなら、二度と会うことはない。（Selamat tinggal, kita takkan pernah bertemu lagi.）", "Dadah, jangan pernah nongol lagi di depan gue!", "ダダ、ジャンガン プルナ ノンオル ラギ ディ ドゥパン グエ", "nongol ⇄ muncul / bertemu。")
        ],
        "quiz": [
            ("映画字幕では「Saya tidak peduli」と書かれる台詞を、若者が実際に激しく言い放つ時の口語は？", ["Bodo amat lah!", "Terima kasih ya!", "Mohon maaf!", "Silakan saja!"], 1),
            ("字幕で「masih menyimpan perasaan（元恋人に未練がある）」を、現代ドラマの若者が言うスラングは？", ["masih gamon (gagal move on)", "masih baper", "masih mager", "masih bucin"], 1),
            ("映画字幕の「segera（すぐに・急いで）」に対応する、話し言葉の代表的語彙は？", ["buruan", "perlahan", "nanti", "kemarin"], 1)
        ]
    },
    {
        "slug": "37-podcast-talk-show-register",
        "title": "【二重言語】YouTube/ポッドキャストの対談口語：相槌、間、切り返し、テンポ感",
        "intro": "Deddy CorbuzierやRaditya Dikaなどの人気YouTube対談・ポッドキャストでは、完全なインフォーマルと一定の敬意が絶妙にブレンドされた「洗練されたGaul（対談口語）」が話されます。「Gini lho（こういうことだよ）」「Bisa dibilang（言ってみれば）」「Intinya（要するに）」などの相槌や文脈展開を身につけます。",
        "pairs": [
            ("Pada intinya adalah... (要するに)", "Intinya gini sih bro...", "論点を整理して切り出す相槌"),
            ("Dapat dikatakan bahwa... (言ってみれば)", "Bisa dibilang kayak gitu...", "相手の意見に同調・要約"),
            ("Menurut pandangan saya (私の見解では)", "Kalau menurut kacamata gue ya...", "私見を述べるイントロ"),
            ("Maksud saya begini (私の意図はこういうことです)", "Maksud gue tuh gini lho...", "誤解を解く・掘り下げる説明")
        ],
        "drill": [
            ("【Baku→Gaul】要するに、それは個人の選択次第です。（Intinya hal tersebut bergantung pada pilihan pribadi.）", "Intinya balik lagi ke preferensi masing-masing sih ya.", "インティニャ バリッ ラギ ク プレフェレンスィ マスィン マスィン スィ ヤ", "対談のまとめ切り返し。"),
            ("【Gaul→Baku】言ってみれば、一種の投資だよね。（Bisa dibilang ini semacam investasi jangka panjang kan?）", "Hal ini dapat dianalogikan sebagai bentuk investasi masa depan.", "ハル イニ ダパット ディ アナロギカン スバガイ ブントゥッ インヴェスタスィ マサ ドゥパン", "口語同調 ⇄ 公式解説。"),
            ("【Baku→Gaul】私の視点から言えば、それは間違っています。（Dari sudut pandang saya, tindakan itu keliru.）", "Kalo dari kacamata gue sih agak blunder ya langkah itu.", "カロ ダリ カチャマタ グエ スィ アガッ ブランダー ヤ ランカ イトゥ", "blunder ⇄ kesalahan fatal。"),
            ("【Gaul→Baku】言いたいのはそういうことじゃないの！（Bukan gitu maksud gue bro, dengerin dulu napa!）", "Bukan maksud saya untuk menyampaikan hal seperti demikian.", "ブカン マクスッド サヤ ウントゥッ ムンニャムパイカン ハル スプルティ ドゥミキアン", "口語釈明 ⇄ 公式弁明。"),
            ("【Baku→Gaul】興味深い指摘ですね。（Itu adalah poin argumen yang sangat menarik.）", "Menarik nih poinnya, jarang ada yang notice soal ini.", "ムナリッ ニ ポインニャ、ジャラン アダ ヤン ノーティス ソアル イニ", "notice ⇄ memperhatikan。"),
            ("【Gaul→Baku】それは完全に事実だよ。（Valid no debat itu mah, emang faktanya gitu!）", "Argumen tersebut sepenuhnya sahih dan tidak terbantahkan lagi.", "アルグメン トゥルスブット スプヌフニャ サヒ ダン ティダッ トゥルバンタカン ラギ", "valid no debat ⇄ fakta tak terbantahkan。"),
            ("【Baku→Gaul】どうしてそう思ったのですか？（Mengapa Anda memiliki pemikiran seperti itu?）", "Kok lu bisa kepikiran ke arah sana sih awalnya?", "コッ ル ビサ クピキラン ク アラ サナ スィ アワルニャ", "対談の深掘り質問。"),
            ("【Gaul→Baku】正直に告白するとね。（Jujurly gue waktu itu sempet ngerasa insecure.）", "Sejujurnya pada saat itu saya merasa kurang percaya diri.", "スジュジュルニャ パダ サアット イトゥ サヤ ムラサ クラン プルチャヤ ディリ", "jujurly ⇄ sejujurnya, insecure ⇄ minder。"),
            ("【Baku→Gaul】別の角度から見てみましょう。（Mari kita tinjau dari sudut pandang yang berbeda.）", "Coba kita liat dari angle yang beda deh ya.", "チョバ キタ リアット ダリ アングル ヤン ベダ デ ヤ", "angle ⇄ sudut pandang。"),
            ("【Gaul→Baku】これ、めちゃくちゃ刺さる話だな！（Daging semua ini pembicaraannya, gokil!）", "Seluruh percakapan ini mengandung wawasan yang sangat bermutu tinggi.", "スルルー プルチャカパン イニ ムンガンドゥン ワワサン ヤン サンガット ブルムトゥ ティンギ", "daging semua ⇄ bermutu / bergizi tinggi。"),
            ("【Baku→Gaul】本質的な問題はそこではありません。（Masalah mendasarnya bukan berada di situ.）", "Root problem-nya bukan di situ sebenernya.", "ルート プロブレムニャ ブカン ディ スィトゥ スブヌルニャ", "root problem ⇄ masalah mendasar。"),
            ("【Gaul→Baku】まさにその通り！（Setuju parah gue sama lu bro!）", "Saya sepenuhnya sependapat dengan apa yang Anda kemukakan.", "サヤ スプヌフニャ スプンダパット ドゥンガン アパ ヤン アンダ クムカカン", "setuju parah ⇄ sangat setuju。"),
            ("【Baku→Gaul】次の話題に進みましょう。（Mari kita lanjutkan ke topik pembicaraan berikutnya.）", "Next topic nih ya, ini gak kalah seru nih.", "ネクスト トピック ニ ヤ、イニ ガッ カラ スル ニ", "対談進行。"),
            ("【Gaul→Baku】話の辻褄が合わないよ。（Gak nyambung bro argumen lu barusan.）", "Argumen yang baru saja Anda kemukakan tidak relevan.", "アルグメン ヤン バル サジャ アンダ クムカカン ティダッ レレヴァン", "gak nyambung ⇄ tidak nyambung / tidak relevan。"),
            ("【Baku→Gaul】本日の対談の結論を申し上げます。（Berikut adalah kesimpulan dari sesi dialog hari ini.）", "Takeaway pentingnya hari ini tuh simpel ya temen-temen.", "テイクアウェイ プンティンニャ ハリ イニ トゥ スィンペル ヤ トゥムン トゥムン", "takeaway ⇄ kesimpulan petikan。")
        ],
        "quiz": [
            ("ポッドキャストや対談で「要するにこういうことだよ」と論点をまとめる定番の切り出しは？", ["Intinya gini sih...", "Menurut undang-undang...", "Mungkin salah ya...", "Diam saja kamu..."], 1),
            ("対談の内容が「非常に有益で中身が濃い（中身が詰まっている）」ことを絶賛するスラング表現は？", ["Daging semua!", "Tulang semua!", "Sayur semua!", "Air semua!"], 1),
            ("相手の意見に「激しく同意する！反論の余地がないほど正しい！」と同調するネット・対談スラングは？", ["Valid no debat!", "Hoaks parah!", "Gak jelas!", "Bodo amat!"], 1)
        ]
    },
    {
        "slug": "38-dating-pdkt-romance-slang",
        "title": "【二重言語】恋愛・デート・若者の人間関係スラング：PDKT, nembak, jadian, ghosting",
        "intro": "インドネシアの若者カルチャーにおいて、恋愛や交際に関する語彙は非常に豊かです。「PDKT（アプローチ・付き合う前のお試し期間）」「nembak（告白する）」「jadian（交際成立）」「ghosting（音信不通で逃げる）」「bucin（恋の奴隷）」など、SNSや日常会話に溢れる恋愛特有のレジスターをマスターします。",
        "pairs": [
            ("pendekatan (アプローチ・交際前期間)", "PDKT", "付き合う前の距離を縮める段階"),
            ("menyatakan cinta (愛を告白する)", "nembak", "ズバッと告白すること"),
            ("resmi berpacaran (正式に付き合い始める)", "jadian", "カップル成立"),
            ("menghilang tanpa kabar (音信不通になる)", "ghosting", "急に連絡を絶ってフェードアウト")
        ],
        "drill": [
            ("【Baku→Gaul】彼らは交際前のアプローチ期間中です。（Mereka berdua sedang dalam tahap pendekatan.）", "Mereka berdua lagi masa-masa PDKT nih.", "ムレカ ブルドゥア ラギ マサ マサ ペーデーカーテー ニ", "PDKT ⇄ pendekatan。"),
            ("【Gaul→Baku】昨日、彼女に告白しちゃった！（Kemarin malem gue akhirnya nembak dia!）", "Kemarin malam saya akhirnya memberanikan diri menyatakan cinta padanya.", "クマレン マラム サヤ アキールニャ ムンブラニカン ディリ ムンニャタカン チンタ パダニャ", "nembak ⇄ menyatakan cinta。"),
            ("【Baku→Gaul】私たちは正式に付き合うことになりました。（Kami berdua telah resmi berpacaran saat ini.）", "Akhirnya kita resmi jadian juga guys!", "アキールニャ キタ レスミ ジャディアン ジュガ ガイズ", "jadian ⇄ resmi berpacaran。"),
            ("【Gaul→Baku】急に音信不通にされちゃった。（Sialan, gue dighosting sama gebetan gue.）", "Sangat disayangkan, orang yang saya dekati tiba-tiba menghilang tanpa kabar.", "サンガット ディサヤンカン、オラン ヤン サヤ ドゥカティ ティバ ティバ ムンヒラン タンパ カバル", "dighosting ⇄ diputus kontak tiba-tiba。"),
            ("【Baku→Gaul】あの人は私の片思いの相手です。（Orang tersebut adalah sosok yang sedang saya sukai.）", "Dia tuh gebetan baru gue, manis bgt kan?", "ディア トゥ グベタン バル グエ、マニス バンゲット カン", "gebetan ⇄ orang yang disukai。"),
            ("【Gaul→Baku】彼は完全に恋の奴隷になっている。（Bucin parah dia, disuruh apa aja mau!）", "Ia sangat diperbudak oleh perasaan cinta terhadap kekasihnya.", "イア サンガット ディプルブダッ オレ プラサアン チンタ トゥルハダップ クカスィフニャ", "bucin (budak cinta) ⇄ terikat cinta。"),
            ("【Baku→Gaul】元恋人との関係を清算できましたか？（Apakah Anda sudah melupakan mantan kekasih Anda?）", "Udah move on belum lu dari mantan?", "ウダ ムーヴ オン ブルム ル ダリ マンタン", "move on ⇄ melupakan masa lalu。"),
            ("【Gaul→Baku】元カノにまだ未練があるんだ。（Jujur gue masih gamon bgt sama mantan.）", "Sejujurnya saya masih belum bisa melupakan kenangan bersama mantan kekasih.", "スジュジュルニャ サヤ マスィ ブルム ビサ ムルパカン クナンガン ブルサマ マンタン クカスィ", "gamon ⇄ gagal move on。"),
            ("【Baku→Gaul】相思相愛ですか？（Apakah perasaan cinta Anda berbalas olehnya?）", "Cintanya bertepuk sebelah tangan apa gayung bersambut?", "チンタニャ ブルテプッ スブラ タンガン アパ ガユン ブルサンブット", "gayung bersambut ⇄ saling suka。"),
            ("【Gaul→Baku】ただの友達関係に留まっちゃった。（Kena friendzone gue jadinya, sedih amat.）", "Hubungan kami pada akhirnya hanya terjebak sebatas pertemanan belaka.", "フブンガン カミ パダ アキールニャ ハニャ トゥルジェバッ スバタス プルトゥマナン ブラカ", "friendzone ⇄ sebatas teman。"),
            ("【Baku→Gaul】私たちは破局しました。（Hubungan percintaan kami telah resmi berakhir.）", "Kita udah putus dari minggu lalu.", "キタ ウダ プトゥス ダリミング ラル", "putus ⇄ berakhir hubungan pacaran。"),
            ("【Gaul→Baku】あいつ、思わせぶりな態度ばかり取る。（Suka tebar pesona dan kasih harapan palsu (PHP).）", "Orang tersebut gemar memberikan harapan palsu yang tidak pasti.", "オラン トゥルスブット グマル ムンブリカン ハラパン パルス ヤン ティダッ パスティ", "PHP (pemberi harapan palsu)。"),
            ("【Baku→Gaul】二股をかけられていた。（Ternyata saya telah diduakan oleh kekasih saya.）", "Gue diselingkuhin anjir, sakit hati bgt!", "グエ ディスリンクイイン アンジール、サキット ハティ バンゲット", "selingkuh ⇄ mendua / selingkuh。"),
            ("【Gaul→Baku】理想の恋人タイプだよ。（Tipe idaman gue bgt tuh orang, spek bidadari!）", "Sosok tersebut sangat memenuhi kriteria pasangan ideal saya.", "ソソッ トゥルスブット サンガット ムムヌヒ クリテリア パサンガン イデアル サヤ", "tipe idaman / spek idaman。"),
            ("【Baku→Gaul】結婚の約束を交わしました。（Kami telah merencanakan jenjang pernikahan resmi.）", "Tahun depan kita rencana mau naik pelaminan nih.", "タフン ドゥパン キタ レンチャナ マウ ナイッ プラミナン ニ", "naik pelaminan ⇄ menikah。")
        ],
        "quiz": [
            ("若者が付き合う前に仲を深める「アプローチ・交際前期間」を意味する略語は？", ["PDKT (pendekatan)", "PHP", "BPPT", "BUMN"], 1),
            ("好きな人に「愛を告白する（ズバッと気持ちを伝える）」を意味する口語動詞は？", ["nembak", "lempar", "tangkap", "pukul"], 1),
            ("デート相手や恋人候補が急にメッセージの返信をやめて音信不通になる行為は？", ["ghosting", "gamon", "bucin", "flexing"], 1)
        ]
    },
    {
        "slug": "39-emotion-exclamations-gokil",
        "title": "【二重言語】感情爆発の感嘆詞スラング：anjir, anjay, gokil, mantul, parah の度合いとTPO",
        "intro": "インドネシアの街角で若者が驚いた時やテンションが上がった時に飛び交う感嘆詞（interjeksi）には、激しいニュアンスからユーモラスな表現まで幅広いグラデーションがあります。「anjir / anjay（うわっ！やばっ！）」「gokil（イカれてる・すごい！）」「mantul（超最高！）」「parah（ひどい・やばい）」など、感情の強さと使うべきTPOを学びます。",
        "pairs": [
            ("Luar biasa mengejutkan! (うわっ！やばい！)", "Anjir / Anjay!", "驚き・呆れ・感嘆の若者スラング"),
            ("Luar biasa hebat / gila! (イカれてる・すげえ！)", "Gokil abis!", "規格外の凄さや面白さを賞賛"),
            ("Mantap betul! (超最高・ドンピシャ！)", "Mantul bgt!", "「mantap betul」の短縮語"),
            ("Sangat parah / keterlaluan! (ひどすぎる・ヤバい！)", "Parah sih ini!", "呆れ返るほどの度を超えた状況")
        ],
        "drill": [
            ("【Baku→Gaul】うわっ、本当にびっくりした！（Aduh, saya sungguh sangat terkejut sekali!）", "Anjir, kaget setengah mati gue barusan!", "アンジール、カゲット ス トゥンガ マティ グエ バルサン", "anjir ⇄ seruan terkejut。"),
            ("【Gaul→Baku】この企画、まじでイカれてるよ！（Gokil abis ide konsep lu bro!）", "Gagasan konsep Anda sungguh luar biasa inovatif dan cemerlang.", "ガガサン コンセプ アンダ スング ルアル ビアサ イノヴァティフ ダン チュムルラン", "gokil abis ⇄ luar biasa hebat。"),
            ("【Baku→Gaul】素晴らしい味ですね！（Kelezatan hidangan ini sungguh sangat mantap sekali.）", "Mantul bgt rasanya, nagih parah!", "マントゥル バンゲット ラサニャ、ナギ パラ", "mantul ⇄ mantap betul。"),
            ("【Gaul→Baku】あいつの態度はひどすぎる。（Parah bgt sih perilakunya, gak punya etika!）", "Perilaku orang tersebut sungguh sudah sangat keterlaluan.", "プリラク オラン トゥルスブット スング スダ サンガット クトゥルラルアン", "parah bgt ⇄ sangat keterlaluan。"),
            ("【Baku→Gaul】信じられないほど素晴らしい！（Wah, sungguh pemandangan yang sangat memukau.）", "Anjay, keren parah fotonya, aesthetic bgt!", "アンジャイ、クレン パラ フォトニャ、エステティック バンゲット", "anjay ⇄ ungkapan kagum。"),
            ("【Gaul→Baku】本当に呆れて言葉も出ない。（Hadeuh, tepuk jidat gue liat kelakuan lu.）", "Saya sungguh merasa sangat heran dan tidak habis pikir.", "サヤ スング ムラサ サンガット ヘラン ダン ティダッ ハビス ピキール", "hadeuh ⇄ helaan napas heran。"),
            ("【Baku→Gaul】なんと愚かなことでしょう。（Betapa cerobohnya tindakan semacam itu.）", "Bego parah sih itu mah, ngapain dilakuin!", "ベゴ パラ スィ イトゥ マ、ンガパイン ディラクイン", "bego ⇄ bodoh / ceroboh。"),
            ("【Gaul→Baku】めちゃくちゃ楽しかった！（Pecah abis konsernya semalem, seru pol!）", "Suasana konser kemarin malam sungguh sangat meriah sekali.", "スアサナ コンセル クマレン マラム スング サンガット ムリア スカリ", "pecah ⇄ sangat meriah / sukses besar。"),
            ("【Baku→Gaul】とんでもない価格設定だ。（Harga yang ditawarkan sangat tidak masuk akal.）", "Gila kali ya, mahal amat harganya selangit!", "ギラ カリ ヤ、マハル アマット ハルガニャ スランギット", "mahal selangit ⇄ mahal sekali。"),
            ("【Gaul→Baku】冗談でしょ？（Buset dah, lu seriusan mau beli mobil sport?）", "Astaga, apakah Anda benar-benar bersungguh-sungguh?", "アスタガ、アパカ アンダ ブナル ブナル ブルスング スング", "buset dah ⇄ seruan kaget。"),
            ("【Baku→Gaul】お見事な勝利でした。（Kemenangan tersebut diraih dengan sangat sempurna.）", "GG parah lu mainnya bro, auto menang!", "ジージー パラ ル マインニャ ブロ、オート ムナン", "GG (good game) ⇄ hebat sekali。"),
            ("【Gaul→Baku】うわ、最悪の展開だ。（Apes bgt, malah kena tilang di lampu merah.）", "Sungguh malang nasib saya karena terkena sanksi tilang.", "スング マラン ナスィブ サヤ カレナ トゥルクナ サンクスィ ティラン", "apes ⇄ sial / malang。"),
            ("【Baku→Gaul】鳥肌が立ちました。（Saya merasa merinding karena sangat terharu.）", "Merinding disko gue denger suaranya, gokil!", "ムリンディン ディスコ グエ ドゥンゲル スアラニャ、ゴキル", "merinding ⇄ bulu kuduk berdiri。"),
            ("【Gaul→Baku】本当に神対応だね！（The best emang pelayanan lu, bintang lima!）", "Kualitas pelayanan yang Anda berikan sungguh luar biasa memuaskan.", "クアリタス プラヤナン ヤン アンダ ブリカン スング ルアル ビアサ ムムアスカン", "the best ⇄ sangat memuaskan。"),
            ("【Baku→Gaul】呆然として動けなくなりました。（Saya terpaku tak mampu berkata-kata.）", "Bengong gue saking shock-nya liat kejadian itu.", "ブンゴン グエ サキン ショックニャ リアット クジャディアン イトゥ", "bengong ⇄ melamun terpana。")
        ],
        "quiz": [
            ("「mantap betul（素晴らしい・最高）」をギュッと縮めた若者の流行語は？", ["mantul", "mager", "baper", "pansos"], 1),
            ("常識外れに面白かったり凄かったりする状況を「イカれてる・最高！」と褒めるスラングは？", ["gokil", "lebay", "omdo", "kepo"], 1),
            ("若者が驚いた時や呆れた時に「うわっ！やばっ！」と発するスラング感嘆詞は？", ["anjir / anjay", "punten", "monggo", "nuhun"], 1)
        ]
    },
    {
        "slug": "40-workplace-gossip-character",
        "title": "【二重言語】ウワサ話・人物批評スラング：kepo, julid, nyinyir, toxic, red flag",
        "intro": "オフィスやSNSでの雑談・人物評では、他人の性格や行動パターンを的確（かつ皮肉たっぷり）に形容するスラングが多用されます。「kepo（詮索好き・おせっかい）」「julid（嫉妬混じりの意地悪・皮肉）」「nyinyir（ネチネチ愚痴る）」「toxic（有害な人・環境）」「red flag（危険信号な性格）」など、現代の人間関係を見抜く必須ボキャブラリーを学びます。",
        "pairs": [
            ("ingin tahu urusan orang lain (詮索好き・首を突っ込む)", "kepo", "他人の秘密や私生活を知りたがる"),
            ("iri hati / dengki dan bersikap sinis (嫉妬や皮肉)", "julid", "他人の成功や幸せを素直に喜ばない"),
            ("mengeluh / mencibir terus-menerus (ネチネチ批判する)", "nyinyir", "小言や文句をしつこく言い続ける"),
            ("berdampak buruk bagi mental (有害な・毒な)", "toxic", "周囲に悪影響を与える人や職場")
        ],
        "drill": [
            ("【Baku→Gaul】他人の私生活を詮索しないでください。（Jangan mencampuri urusan pribadi orang lain.）", "Gausah kepo deh lu sama urusan orang!", "ガウサ ケポ デ ル サマ ウルサン オラン", "kepo ⇄ ingin tahu urusan orang。"),
            ("【Gaul→Baku】他人の幸せに皮肉を言わないで。（Jangan suka julid liat temen sukses.）", "Hindarilah bersikap sinis dan dengki atas keberhasilan orang lain.", "ヒンダリラ ブルスィカップ スィニス ダン ドゥンキ アタス クブルハスィラン オラン ライン", "julid ⇄ iri dan sinis。"),
            ("【Baku→Gaul】ネチネチと文句を言い続けるのはやめて。（Hentikan kebiasaan mencibir secara terus-menerus.）", "Stop nyinyir mulu napa, kerjain aja tugas lu!", "ストップ ニンニール ムル ナパ、クルジャイン アジャ トゥガス ル", "nyinyir ⇄ mencibir terus。"),
            ("【Gaul→Baku】あの職場は環境が有害すぎる。（Toxic bgt lingkungan kantornya, gak sehat.）", "Suasana lingkungan kerja tersebut sangat beracun bagi kesehatan mental.", "スアサナ リンカンガン クルジャ トゥルスブット サンガット ブラチュン バギ クセハタン ムンタル", "toxic ⇄ merugikan mental。"),
            ("【Baku→Gaul】あの人には危険な兆候が見られます。（Terdapat indikasi perilaku yang patut diwaspadai dari dirinya.）", "Red flag parah sih sifatnya, mending lu hindari deh.", "レッド フラッグ パラ スィ スィファットニャ、メンディン ル ヒンダリ デ", "red flag ⇄ tanda bahaya sifat。"),
            ("【Gaul→Baku】あいつは二枚舌だ。（Muka dua tuh orang, di depan baik di belakang nusuk!）", "Orang tersebut bersikap munafik dan berkhianat di belakang.", "オラン トゥルスブット ブルスィカップ ムナフィッ ダン ブルキアナット ディ ブラカン", "muka dua ⇄ munafik。"),
            ("【Baku→Gaul】嘘の情報を流すのはやめてください。（Jangan menyebarkan kabar angin yang tidak terbukti.）", "Jangan suka nyebar hoaks sama fitnah dong!", "ジャンガン スカ ニェバール ホアクス サマ フィットナ ドン", "nyebar hoaks ⇄ menyebar rumor palsu。"),
            ("【Gaul→Baku】被害者ぶるのはやめて。（Gausah playing victim deh lu, jelas-jelas lu yg salah!）", "Jangan berlagak seolah diri Anda adalah korban dalam masalah ini.", "ジャンガン ブルラガッ スオラ ディリ アンダ アダラ コルバン ダラム マサラ イニ", "playing victim ⇄ bersikap seolah korban。"),
            ("【Baku→Gaul】他人の足を引っ張る行為は慎むべきです。（Sebaiknya hindari upaya saling menjatuhkan sesama rekan.）", "Jangan suka saling sikut di tempat kerja.", "ジャンガン スカ サリン スィクット ディ トゥムパット クルジャ", "saling sikut ⇄ saling menjatuhkan。"),
            ("【Gaul→Baku】自己中心的な人だ。（Egois bgt orangnya, cuma mikirin diri sendiri.）", "Sosok tersebut memiliki kepribadian yang sangat mementingkan diri sendiri.", "ソソッ トゥルスブット ムミリキ クプリバディアン ヤン サンガット ムムンティンカン ディリ スンディリ", "egois ⇄ mementingkan diri sendiri。"),
            ("【Baku→Gaul】裏表のない正直な人です。（Dia adalah sosok yang sangat tulus tanpa kepalsuan.）", "Orangnya asik dan humble bgt, gak neko-neko.", "オランニャ アスィッ ダン ハンブル バンゲット、ガッ ネコネコ", "gak neko-neko ⇄ tulus / apa adanya。"),
            ("【Gaul→Baku】話に尾ひれをつけないで。（Jangan suka ngegoreng isu yg gak jelas!）", "Tolong jangan membesar-besarkan permasalahan kecil ini.", "トロン ジャンガン ムンブサール ブサールカン プルマサラハン クチル イニ", "ngegoreng isu ⇄ membesar-besarkan berita。"),
            ("【Baku→Gaul】ただの根拠のない噂話です。（Hal tersebut hanyalah gosip burung yang belum tentu benar.）", "Cuma kabar burung doang, gausah dimasukin hati.", "チュマ カバル ブルン ドアン、ガウサ ディマスッカン ハティ", "kabar burung ⇄ kabar tanpa dasar。"),
            ("【Gaul→Baku】あいつ、本当に態度が大きい。（Sok jagoan tuh orang, sok berkuasa!）", "Orang tersebut bersikap sangat angkuh dan sombong.", "オラン トゥルスブット ブルスィカップ サンガット アンク ダン ソンボン", "sok jagoan ⇄ angkuh / sombong。"),
            ("【Baku→Gaul】彼と関わると面倒なことになりますよ。（Berurusan dengan dirinya hanya akan mendatangkan kerumitan.）", "Ribet urusannya kalo berurusan sama tuh orang, mending skip!", "リベット ウルサンニャ カロ ブルウルサン サマ トゥ オラン、メンディン スキップ", "skip ⇄ hindari / lewati。")
        ],
        "quiz": [
            ("他人の私生活や秘密を「根掘り葉掘り知りたがる詮索好き」を意味する最も代表的なスラングは？", ["kepo", "julid", "nyinyir", "bucin"], 1),
            ("他人の成功や幸せに対して「嫉妬混じりの意地悪な皮肉を言う」ことを表すスラング動詞は？", ["julid", "mager", "pansos", "flexing"], 1),
            ("周囲の精神衛生を悪化させるような「有害な人・有害な環境」を英語借用で何と呼ぶ？", ["toxic", "cincai", "hoki", "gokil"], 1)
        ]
    }
]

for a in articles_data:
    filepath = os.path.join("docs/diglossia", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. コードスイッチング対比表（公式標準表現 ⇄ 口語・スラング）\n")
    lines.append("| No | 公式標準表現 (Bahasa Baku) | 口語・スラング (Bahasa Gaul) | 意味・ニュアンス |")
    lines.append("|---|---|---|---|")
    for idx, (baku, gaul, meaning) in enumerate(a['pairs'], 1):
        lines.append(f"| {idx} | `{baku}` | **{gaul}** | {meaning} |")
    lines.append("")
    
    lines.append("## 2. 構文・文脈心理メカニズム\n")
    lines.append("公式標準語の文法構造が、口語においてどのように短縮・脱落・母音変容（音韻融合）を起こしているかを理解することで、リスニングの「聞き取れない壁」を突破し、自然な発話が可能になります。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 双方向コード変換ドリル（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語と提示された文を見て、指定されたレジスター（Baku → Gaul または Gaul → Baku）へ1〜2秒以内に口頭で言い換えてください。\n")
    
    for idx, (prompt, target_sent, kana, exp) in enumerate(a['drill'], 1):
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

print("Batch 1131-1140 generated successfully.")
