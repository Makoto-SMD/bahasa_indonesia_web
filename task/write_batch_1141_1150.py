# -*- coding: utf-8 -*-
import os
import re

articles_data = [
    {
        "slug": "41-anger-formal-to-informal",
        "title": "【二重言語】怒り・不満のレジスター：Kami sangat menyayangkan ⇄ Parah banget sih / Kesel gue",
        "intro": "不満や怒りを表す際、ビジネスや公の場での「冷静かつ客観的な抗議（Bahasa Baku）」と、親しい間柄での「感情を露わにする憤慨（Bahasa Gaul）」では使われる構文が劇的に異なります。「Kami sangat menyayangkan（遺憾に思う）」から「Kesel gue（超むかつく）」まで、レジスターの適切な切り替えを体得します。",
        "pairs": [
            ("Kami sangat menyayangkan hal ini.", "Parah bgt sih ini, kesel gue!", "遺憾の意 ⇄ 強い怒りと苛立ち"),
            ("Mohon pertanggungjawabannya.", "Gimana sih lu, kok lepas tanggung jawab?!", "責任追及の公式表現 ⇄ 口語の問い詰め"),
            ("Hal ini tidak dapat kami toleransi.", "Gak bisa dibiarin nih kelakuan kayak gini!", "不容認の宣言 ⇄ 口語の制裁感情"),
            ("Tindakan ini sangat mengecewakan.", "Kecewa berat gue liat hasilnya.", "失望の公式表明 ⇄ 率直な口語失望")
        ],
        "drill": [
            ("【Baku→Gaul】このような事態が生じたことを非常に遺憾に思います。（Kami sangat menyayangkan terjadinya insiden seperti ini.）", "Parah bgt sumpah, kesel abis gue kejadiannya begini!", "パラ バンゲット スンパ、クセル アビス グエ クジャディアンニャ ブギニ", "遺憾 ⇄ 強い怒り。"),
            ("【Gaul→Baku】いい加減にしてよ、責任取って！（Gausah kabur lu, tanggung jawab dong!）", "Mohon jangan melarikan diri dari kewajiban dan tanggung jawab Anda.", "モホン ジャンガン ムラリカン ディリ ダリ クワジバン ダン タングン ジャワブ アンダ", "公式責任催促。"),
            ("【Baku→Gaul】このような無礼な対応は許容できません。（Perlakuan kasar semacam ini tidak dapat kami toleransi.）", "Gak ada adab bgt, gak bisa ditolerir nih kelakuannya!", "ガッ アダ アダブ バンゲット、ガッ ビサ ディトレリル ニ クラクアンニャ", "無礼への抗議。"),
            ("【Gaul→Baku】本当に呆れて言葉が出ない。（Gila ya, gak habis pikir gue sama kelakuan lu!）", "Saya sungguh merasa sangat heran dan kecewa atas tindakan Anda.", "サヤ スング ムラサ サンガット ヘラン ダン クチェワ アタス ティンダカン アンダ", "呆れ ⇄ 公式失望。"),
            ("【Baku→Gaul】約束が守られず失望しました。（Saya merasa sangat kecewa janji tersebut tidak dipenuhi.）", "Kecewa berat gue, omdo doang ternyata dari kemarin!", "クチェワ ブラット グエ、オムド ドアン トゥルニャタ ダリ クマレン", "失望と口先批判。"),
            ("【Gaul→Baku】怒りで頭に血が上ってる。（Emosi jiwa gue, naik darah liat tingkahnya!）", "Saya merasa sangat marah dan tersinggung oleh sikapnya.", "サヤ ムラサ サンガット マラ ダン トゥルスィングン オレ スィカップニャ", "激怒 ⇄ 公式憤慨。"),
            ("【Baku→Gaul】二度と同じ過ちを繰り返さないでください。（Jangan sampai mengulangi kesalahan fatal semacam ini lagi.）", "Jangan diulangin lagi ya, awas aja kalo kejadian lagi!", "ジャンガン ディウランイン ラギ ヤ、アワス アジャ カロ クジャディアン ラギ", "警告 ⇄ 口語脅し。"),
            ("【Gaul→Baku】人の努力を台無しにするな！（Jangan ngerusak rencana orang napa!）", "Tolong jangan merusak perencanaan kerja yang telah disusun bersama.", "トロン ジャンガン ムルサッ プレンチナナアン クルジャ ヤン トゥラ ディススン ブルサマ", "妨害抗議。"),
            ("【Baku→Gaul】これ以上の遅延は認められません。（Keterlambatan lebih lanjut tidak dapat kami terima.）", "Gak ada toleransi lagi buat yang ngaret!", "ガッ アダ トレランスィ ラギ ブアット ヤン ンガレット", "遅延不容認。"),
            ("【Gaul→Baku】勝手なことばかりするな。（Enak bgt lu tinggal lempar masalah ke orang!）", "Tolong jangan melimpahkan permasalahan pribadi kepada pihak lain.", "トロン ジャンガン ムリンパカン プルマサラハン プリバディ クパダ ピハッ ライン", "身勝手批判。"),
            ("【Baku→Gaul】契約条件が著しく違反されています。（Syarat dan ketentuan kontrak telah dilanggar secara sepihak.）", "Ngelanggar perjanjian sepihak nih, main-main dia!", "ンゲランガル プルジャンジアン スピハッ ニ、マイン マイン ディア", "契約違反。"),
            ("【Gaul→Baku】口先ばかりで誠意がない。（Cuma manis di bibir doang, gak ada ikhlasnya!）", "Orang tersebut hanya pandai berjanji tanpa menunjukkan niat baik nyata.", "オラン トゥルスブット ハニャ パンダイ ブルジャンジ タンパ ムヌンジュッカンニアット バイッ ニャタ", "不誠実批判。"),
            ("【Baku→Gaul】至急改善策を提示してください。（Segera sampaikan langkah korektif dan solusi konkret.）", "Buruan kasih solusi napa, jangan cuma diem doang!", "ブルアン カスィ ソルスィ ナパ、ジャンガン チュマ ディエム ドアン", "解決策要求。"),
            ("【Gaul→Baku】怒鳴りつけないでよ。（Jangan ngegas dong, santai aja ngomongnya!）", "Mohon turunkan nada suara Anda dan berbicaralah dengan tenang.", "モホン トゥルンカン ナダ スアラ アンダ ダン ブルビチャララ ドゥンガン トゥナン", "トーン鎮静化。"),
            ("【Baku→Gaul】正式に抗議の意を表明いたします。（Kami menyampaikan nota protes resmi atas perlakuan ini.）", "Gue layangkan komplain resmi ke manajemen sekarang juga!", "グエ ラヤンカン コンプレイン レスミ ク マナジェメン スカラン ジュガ", "公式クレーム。")
        ],
        "quiz": [
            ("公式文書で「遺憾に思う」を表す「Kami sangat menyayangkan...」を、若者が日常会話で感情を込めて言う時の表現は？", ["Parah banget sih, kesel gue!", "Terima kasih banyak ya!", "Selamat atas hasilnya!", "Silakan masuk!"], 1),
            ("話し相手がカッカして声を荒らげている時に「声を荒らげないで、落ち着いて話して」とたしなめる口語表現は？", ["Jangan ngegas dong!", "Jangan makan dong!", "Jangan tidur dong!", "Jangan jalan dong!"], 1),
            ("口語で「激怒して血圧が上がる・頭に血が上る」を表す慣用表現は？", ["emosi jiwa / naik darah", "turun berat", "cuci mata", "naik kelas"], 1)
        ]
    },
    {
        "slug": "42-praise-formal-to-informal",
        "title": "【二重言語】賞賛・感激のレジスター：Prestasi yang luar biasa ⇄ Keren abis / Gila sih",
        "intro": "相手の成果や作品を褒め称えるとき、式典や公の場での「品格ある賛辞（Bahasa Baku）」と、同僚や友人同士の「テンションの高い絶賛（Bahasa Gaul）」を使い分けることで、人間関係の距離感にぴったり合ったコミュニケーションが実現します。",
        "pairs": [
            ("Pencapaian yang sangat membanggakan.", "Keren abis bro, gokil gak ada lawan!", "誇らしい業績 ⇄ 口語の最高絶賛"),
            ("Karya ini memiliki nilai estetika tinggi.", "Aesthetic bgt parah, cakep visualnya!", "芸術的価値の評価 ⇄ 若者のセンス絶賛"),
            ("Anda telah menunjukkan dedikasi luar biasa.", "Emang lu doang yang paling niat, mantap!", "献身の評価 ⇄ 誠意・努力の口語評価"),
            ("Hasil evaluasi menunjukkan kinerja sempurna.", "Kinerjanya dapet bintang lima, GG abis!", "完璧な成績評価 ⇄ 満点評価スラング")
        ],
        "drill": [
            ("【Baku→Gaul】大変誇らしい素晴らしい成果です。（Ini adalah pencapaian yang sungguh sangat membanggakan.）", "Keren abis bro, gokil parah prestasinya!", "クレン アビス ブロ、ゴキル パラ プレスタスィニャ", "賞賛のレジスター変換。"),
            ("【Gaul→Baku】この企画、まじで神がかってる！（Gila sih, out of the box bgt idenya!）", "Gagasan konsep ini sungguh sangat luar biasa inovatif.", "ガガサン コンセプ イニ スング サンガット ルアル ビアサ イノヴァティフ", "口語絶賛 ⇄ 公式賞賛。"),
            ("【Baku→Gaul】素晴らしいプレゼンテーションでした。（Presentasi yang Anda sampaikan sangat memukau hadirin.）", "Pecah bgt presentasinya tadi, semua orang tepuk tangan!", "プチャ バンゲット プレゼンタスィニャ タディ、スムア オラン トゥプッ タンガン", "プレゼン成功。"),
            ("【Gaul→Baku】あなたの仕事は本当に手際が良い。（Gercep bgt kerjanya, rapi pula!）", "Kinerja Anda terbukti sangat cepat tanggap dan terstruktur rapi.", "キネルジャ アンダ トゥルブクティ サンガット チパット タングアップ ダン トゥルストルクトゥール ラピ", "手際・迅速性の賞賛。"),
            ("【Baku→Gaul】あなたの献身に心より敬意を表します。（Kami sangat mengapresiasi dedikasi dan kerja keras Anda.）", "Salute bgt gue sama kerja keras lu selama ini!", "サリュート バンゲット グエ サマ クルジャ クラス ル スラマ イニ", "敬意と感謝。"),
            ("【Gaul→Baku】本当に頼りになる相棒だよ！（Andalan gue bgt lu mah, selalu ada solusinya!）", "Anda adalah mitra kerja yang senantiasa dapat diandalkan.", "アンダ アダラ ミトラ クルジャ ヤン スナンティアサ ダパット ディアンダルカン", "頼れる相棒。"),
            ("【Baku→Gaul】デザインが非常に洗練されています。（Desain visual ini tampak begitu elegan dan berkelas.）", "Aesthetic pol desainnya, clean dan elegan bgt!", "エステティック ポル デザインニャ、クリーン ダン エレガン バンゲット", "デザイン絶賛。"),
            ("【Gaul→Baku】この料理、星5つの美味しさ！（Enak parah makanannya, bintang lima no debat!）", "Cita rasa kuliner ini sungguh berada pada tingkat kelezatan sempurna.", "チタ ラサ クリネル イニ スング ブラダ パダ ティンカット クルザタン スンププルナ", "料理絶賛。"),
            ("【Baku→Gaul】期待を遥かに上回る素晴らしい結果です。（Hasil ini melampaui seluruh target yang ditetapkan.）", "Jauh ngelampaui ekspektasi bro, juara emang lu!", "ジャウ ンエランプイ エクスペクタスィ ブロ、ジュアラ エマン ル", "期待超え。"),
            ("【Gaul→Baku】歌声が上手すぎて鳥肌立った！（Merinding disko gue denger vokalnya, top tier!）", "Kualitas olah vokal tersebut sungguh sangat memukau kalbu.", "クアリタス オラ ヴォカル トゥルスブット スング サンガット ムムカウ カルブ", "歌声絶賛。"),
            ("【Baku→Gaul】誠に模範的なリーダーシップです。（Kepemimpinan Anda merupakan teladan bagi kami semua.）", "Leader panutan bgt ini mah, humble tapi tegas!", "リーダー パヌタン バンゲット イニ マ、ハンブル タピ トゥガス", "リーダーシップ賞賛。"),
            ("【Gaul→Baku】あいつのセンスは別格だよ。（Emang beda kelas dia mah, taste-nya mahal!）", "Selera dan kepekaan artistik beliau berada di atas rata-rata.", "スレラ ダン クプカアン アルティスティック ブリアウ ブラダ ディ アタス ラタ ラタ", "センスの格差。"),
            ("【Baku→Gaul】粘り強くやり遂げましたね。（Anda telah berhasil menuntaskannya dengan ketekunan luar biasa.）", "Mental baja emang lu, kelar juga akhirnya!", "ムンタル バジャ エマン ル、クラル ジュガ アキールニャ", "完遂賞賛。"),
            ("【Gaul→Baku】お見事な勝利！（Auto win bro, GG parah permainannya!）", "Sebuah kemenangan telak yang diraih secara mutlak dan sempurna.", "スブア クムナンガン トゥラッ ヤン ディライ スチャラ ムトラッ ダン スンププルナ", "勝利賞賛。"),
            ("【Baku→Gaul】これからも更なる飛躍を期待しています。（Semoga prestasi cemerlang ini terus berlanjut ke depan.）", "Makin menyala abangku, sukses terus kedepannya ya!", "マキン ムニャラ アバンクー、スクセス トゥルス クドゥパンニャ ヤ", "若者の激励（Makin menyala）。")
        ],
        "quiz": [
            ("若者やSNSで相手の圧倒的な活躍や勢いを「ますます輝いてるぞ！」と称える最新流行フレーズは？", ["Makin menyala abangku!", "Makin padam abangku!", "Makin tidur abangku!", "Makin mager abangku!"], 1),
            ("動きが素早く機敏で仕事が早い人を「gerak cepat」の短縮語で褒めるスラングは？", ["gercep", "mager", "baper", "kepo"], 1),
            ("相手の成果や才能に対して「規格外にイカれてる・すげえ！」と絶賛する口語形容詞は？", ["gokil", "lebay", "omdo", "cringe"], 1)
        ]
    },
    {
        "slug": "43-advice-formal-to-informal",
        "title": "【二重言語】助言・忠告のレジスター：Sebaiknya Saudara... ⇄ Mendingan lu... / Saran gue sih",
        "intro": "他人にアドバイスや忠告を与える際、上司や顧客向けの「角を立てない客観的な提案（Bahasa Baku）」と、同僚や友人向けの「率直で親身な助言（Bahasa Gaul）」を使い分ける技術は、対人関係の信頼構築において極めて重要です。",
        "pairs": [
            ("Sebaiknya Saudara mempertimbangkannya.", "Mendingan lu pikir-pikir lagi deh.", "再考の勧め ⇄ 口語の親身な助言"),
            ("Saran kami adalah melakukan konsultasi.", "Saran gue sih, mending lu konsul dulu.", "専門家相談の提案 ⇄ 口語の気軽な勧め"),
            ("Alangkah baiknya bila dipersiapkan sejak dini.", "Enakan disiapin dari sekarang biar gak ribet.", "事前準備の推奨 ⇄ 口語の手間削減提案"),
            ("Hindarilah mengambil keputusan tergesa-gesa.", "Jangan grasak-grusuk ambil keputusan, santai aja.", "性急な判断の戒め ⇄ 口語の落ち着き促し")
        ],
        "drill": [
            ("【Baku→Gaul】再検討されることをお勧めいたします。（Sebaiknya Saudara mempertimbangkan kembali hal ini.）", "Mendingan lu pikir mateng-mateng lagi deh bro.", "メンディンガン ル ピキール マトゥン マトゥン ラギ デ ブロ", "再考推奨。"),
            ("【Gaul→Baku】休んだほうがいいよ、顔色が悪い。（Mending lu istirahat dulu, pucet bgt muka lu.）", "Alangkah baiknya bila Anda beristirahat sejenak karena tampak kurang sehat.", "アランカ バイッニャ ビラ アンダ ブルイスティラハット スジュナッ カレナ タンパッ クラン セハット", "健康助言。"),
            ("【Baku→Gaul】専門家へのご相談をお勧めします。（Kami menyarankan agar berkonsultasi dengan tenaga ahli.）", "Saran gue sih, mending tanya expert-nya langsung.", "サラン グエ スィ、メンディンタニャ エキスパートニャ ランスン", "専門家相談。"),
            ("【Gaul→Baku】焦って決めないで。（Gausah buru-buru, pertimbangin baek-baek.）", "Hindarilah mengambil keputusan secara tergesa-gesa tanpa perhitungan.", "ヒンダリラ ムナンビル クプトゥサン スチャラ トゥルグサ グサ タンパ プルヒトゥンガン", "焦り戒め。"),
            ("【Baku→Gaul】バックアップを取っておいた方が安全です。（Langkah antisipasi sebaiknya disiapkan terlebih dahulu.）", "Mending lu siapin Plan B dari sekarang buat jaga-jaga.", "メンディン ル スィアピン プラン ビー ダリ スカラン ブアット ジャガ ジャガ", "備えの推奨。"),
            ("【Gaul→Baku】関わらない方が身のためだよ。（Mending lu gak usah ikut campur, ribet ntar!）", "Sebaiknya Anda tidak mencampuri perkara tersebut demi kenyamanan bersama.", "スバイッニャ アンダ ティダッ ムンチャンプリ プルカラ トゥルスブット ドゥミ クニャマナン ブルサマ", "不干渉忠告。"),
            ("【Baku→Gaul】正直に打ち明けた方が賢明です。（Akan lebih bijaksana apabila berterus terang sejak awal.）", "Jujur aja dari awal, daripada bohong ketauan makin runyam.", "ジュジュール アジャ ダリ アワル、ダルィパダ ボホン クタウアン マキン ルニャム", "正直さの推奨。"),
            ("【Gaul→Baku】お金の無駄遣いはやめなよ。（Jangan boros-boros amat napa, tabung dikit!）", "Disarankan untuk lebih bijak mengelola pengeluaran dan menabung.", "ディサランカン ウントゥッ ルビ バイッ ムンゲロラ プングルアラン ダン ムナブン", "浪費戒め。"),
            ("【Baku→Gaul】念のため確認された方が確実です。（Sebaiknya Saudara melakukan konfirmasi ulang secara tertulis.）", "Double check lagi ya bro, biar gak ada miskom.", "ダブル チェック ラギ ヤ ブロ、ビアル ガッ アダ ミスコム", "確認推奨。"),
            ("【Gaul→Baku】他人の意見に流されないで。（Jangan gampang kemakan omongan orang lain.）", "Hendaknya Anda tidak mudah terpengaruh oleh opini yang belum terbukti.", "フンダッニャ アンダ ティダッ ムダ トゥルプンガル オレ オピニ ヤン ブルム トゥルブクティ", "主体性の推奨。"),
            ("【Baku→Gaul】弁護士への相談を強く推奨します。（Sangat kami sarankan untuk meminta bantuan hukum resmi.）", "Mending langsung sewa lawyer aja deh kalo udah seberat ini.", "メンディン ランスン セワ ローヤー アジャ デ カロ ウダ スブラット イニ", "法的助言。"),
            ("【Gaul→Baku】自分を追い詰めすぎないで。（Jangan terlalu keras sama diri sendiri napa.）", "Mohon jangan terlalu membebani pikiran Anda secara berlebihan.", "モホン ジャンガン トゥルラル ムンベバニ ピキラン アンダ スチャラ ブルレビハン", "自己肯定・休息。"),
            ("【Baku→Gaul】早めの退社をお勧めします。（Sebaiknya Anda pulang lebih awal untuk beristirahat.）", "Balik gih dari sekarang, jangan maksain lembur mulu.", "バリッ ギー ダリ スカラン、ジャンガン マクサイン レンブール ムル", "早帰り推奨。"),
            ("【Gaul→Baku】一度話し合ってみたら？（Coba ajak ngobrol baik-baik dulu deh empat mata.）", "Alangkah bijaknya bila dilakukan dialog secara terbuka empat mata.", "アランカ ビジャッニャ ビラ ディラクカン ディアログ スチャラ トゥルブカ エンパット マタ", "対話推奨。"),
            ("【Baku→Gaul】健康第一でお過ごしください。（Utamakanlah kesehatan fisik dan mental Anda.）", "Kesehatan nomor satu bro, kerjaan mah gak ada habisnya!", "クセハタン ノモール サトゥ ブロ、クルジャアン マ ガッ アダ ハビスニャ", "健康第一。")
        ],
        "quiz": [
            ("口語で相手に「〜した方がいいよ（〜のほうがマシだよ）」と気軽に助言する定番の語は？", ["mending / mendingan", "pasti", "harus", "jangan"], 1),
            ("事前準備やトラブル予防のために「念のため、用心のために」を口語で表す表現は？", ["buat jaga-jaga", "buat main-main", "buat buang-buang", "buat pamer"], 1),
            ("「焦ってバタバタと行動するな」を意味する口語オノマトペ表現は？", ["jangan grasak-grusuk", "jangan enak-enak", "jangan manis-manis", "jangan makan-makan"], 1)
        ]
    },
    {
        "slug": "44-opinion-formal-to-informal",
        "title": "【二重言語】意見表明のレジスター：Menurut pandangan kami ⇄ Kalo menurut gue sih / Gue rasa",
        "intro": "自らの見解や判断を相手に伝えるとき、会議や論文での「客観性を担保した謙虚な論述（Bahasa Baku）」と、ディスカッションでの「切れ味の良い直感的な主張（Bahasa Gaul）」を使いこなすことで、説得力と親しみやすさの両立が可能になります。",
        "pairs": [
            ("Menurut pandangan kami... (弊社の見解では)", "Kalo menurut kacamata gue sih...", "見解提示のレジスター差"),
            ("Kami berpendapat bahwa... (〜であると考えます)", "Gue rasa kayaknya...", "推量・意見のトーン差"),
            ("Dapat disimpulkan bahwa... (と結論づけられます)", "Intinya mah gini...", "結論要約のレジスター差"),
            ("Dari perspektif yang berbeda... (別の視点では)", "Kalo diliat dari sisi laen ya...", "視点転換の表現差")
        ],
        "drill": [
            ("【Baku→Gaul】私たちの見解では、この計画は実現困難です。（Menurut pandangan kami, rencana ini sulit direalisasikan.）", "Kalo menurut gue sih, agak mustahil ya rencana begini.", "カロ ムヌルット グエ スィ、アガッ ムスタヒル ヤ レンチャナ ブギニ", "実現性の私見。"),
            ("【Gaul→Baku】正直、これは時間の無駄だと思う。（Jujurly gue rasa buang-buang waktu doang ini mah.）", "Secara jujur kami berpendapat kegiatan ini kurang efisien dari segi waktu.", "スチャラ ジュジュール カミ ブルプンダパット クギアタン イニ クラン エフィスィエン ダリ スギ ワクトゥ", "非効率の指摘。"),
            ("【Baku→Gaul】別の角度から検討してみる必要があります。（Perlu ditinjau dari sudut pandang yang lebih luas.）", "Coba liat dari sudut pandang laen deh, biar gak sempit.", "チョバ リアット ダリ スドゥット パンダン ライン デ、ビアル ガッ スンピット", "多角的検討。"),
            ("【Gaul→Baku】要するに、予算が足りないんでしょ？（Ujung-ujungnya soal duit kan ya, ngaku aja!）", "Pada hakikatnya kendala mendasar terletak pada keterbatasan anggaran belanja.", "パダ ハキカットニャ クンダラ ムンダサール トゥルレタック パダ クトゥルバタサン アンガラン ブランジャ", "予算不足の指摘。"),
            ("【Baku→Gaul】この提案には賛同いたしかねます。（Kami merasa keberatan untuk menyepakati usulan tersebut.）", "Gue kurang sreg sih sama usulan ini, agak riskan.", "グエ クラン スレッ スィ サマ ウスラン イニ、アガッ リスカン", "難色表明。"),
            ("【Gaul→Baku】私は全然気にならないよ。（Kalo gue mah santai aja, gak ada masalah sama sekali.）", "Bagi diri saya pribadi, hal tersebut tidak menjadi suatu permasalahan.", "バギ ディリ サヤ プリバディ、ハル トゥルスブット ティダッ ムンジャディ スアトゥ プルマサラハン", "寛容の表明。"),
            ("【Baku→Gaul】市場の需要は依然として高いと考えられます。（Kami meyakini permintaan pasar masih sangat menjanjikan.）", "Market-nya masih gurih bgt ini mah sebenernya!", "マーケットニャ マスィ グリ バンゲット イニ マ スブヌルニャ", "市場需要の評価。"),
            ("【Gaul→Baku】話が都合良すぎる。（Terlalu mulus ceritanya, pasti ada udang di balik batu.）", "Skenario tersebut tampak terlalu ideal sehingga patut dicurigai motif di baliknya.", "スケナリオ トゥルスブット タンパッ トゥルラル イデアル スヒンガ パトゥット ディチュリガイ モティフ ディバリッニャ", "不信感・疑念。"),
            ("【Baku→Gaul】長期的な影響を考慮すべきです。（Dampak jangka panjang seyogianya dipertimbangkan matang.）", "Mikirin long term-nya dong, jangan cuma liat sekarang!", "ミキリン ロング タームニャ ドン、ジャンガン チュマ リアット スカラン", "長期視点。"),
            ("【Gaul→Baku】それが一番無難な選択肢だよ。（Itu mah opsi paling aman, gak bakal salah!）", "Pilihan tersebut merupakan opsi yang paling minim risiko.", "ピリハン トゥルスブット ムルパカン オプスィ ヤン パリン ミニム リスィコ", "安全策の推奨。"),
            ("【Baku→Gaul】私個人の意見としては賛成です。（Secara pribadi, saya mendukung penuh inisiatif ini.）", "Kalo dari gue pribadi sih yes bgt ya buat proyek ini.", "カロ ダリ グエ プリバディ スィ イエス バンゲット ヤ ブアット プロイェッ イニ", "個人的賛成。"),
            ("【Gaul→Baku】根拠が薄弱すぎる。（Gak ada dasar ilmiahnya sama sekali, cuma asumsi!）", "Argumen tersebut tidak didukung oleh data empiris yang sahih.", "アルグメン トゥルスブット ティダッ ディドゥクン オレ データ エンピリス ヤン サヒ", "論拠薄弱。"),
            ("【Baku→Gaul】状況を見守るのが賢明です。（Akan lebih bijak bila kita mengamati perkembangan situasi.）", "Wait and see dulu aja, liat sikonnya gimana ntar.", "ウェイト アンド シー ドゥル アジャ、リアット スィコンニャ ギマナ エンタール", "様子見。"),
            ("【Gaul→Baku】これ、絶対ヒットするよ！（Gue yakin seribu persen ini bakal viral!）", "Saya memiliki keyakinan penuh produk ini akan menuai sukses besar.", "サヤ ムミリキ クヤキナン プヌ プロドゥッ イニ アカン ムヌアイ スクセス ブサール", "ヒット予測。"),
            ("【Baku→Gaul】優先順位を見直すべきです。（Prioritas kerja hendaknya dievaluasi kembali secara menyeluruh.）", "Sortir lagi prioritasnya, jangan semua mau digarap!", "ソルティール ラギ プリオリタスニャ、ジャンガン スムア マウ ディガラッ", "優先順位整理。")
        ],
        "quiz": [
            ("日常会話で自分の意見を「私の見立て・視点から言えばね」とカジュアルに切り出す表現は？", ["Kalo menurut kacamata gue sih...", "Berdasarkan pasal 1 undang-undang...", "Mungkin Anda salah paham...", "Tolong diam sebentar..."], 1),
            ("提案などに対して「いまいちしっくりこない・腑に落ちない」という微妙な難色を表す口語は？", ["kurang sreg", "kurang garam", "kurang tidur", "kurang makan"], 1),
            ("市場やビジネスチャンスが「非常に魅力的・旨味がある」ことを表す口語形容詞は？", ["gurih", "asin", "pahit", "hambar"], 1)
        ]
    },
    {
        "slug": "45-hesitation-fillers-register",
        "title": "【二重言語】躊躇・フィラーのレジスター：Kira-kira... ⇄ Gimana ya, anu, kayak, apa tuh namanya",
        "intro": "言葉に詰まった時や考えをまとめる間の「フィラー（つなぎ言葉）」は、公式スピーチでの「Kira-kira...（おおよそ）」「Bisa dikatakan...（言わば）」と、日常会話での「Gimana ya...（なんて言うか）」「Anu...（あのー）」「Kayak...（なんか〜みたいな）」で大きく異なります。流暢さを演出する必須フィラーを学びます。",
        "pairs": [
            ("Bagaimana menjelaskannya ya... (どう説明したものか)", "Gimana ya ngomongnya...", "言葉を探す時のフィラー"),
            ("Kurang lebih semacam itu... (おおよそそのような)", "Kayak... apa ya, semacem gitu lah...", "曖昧に例示する時のフィラー"),
            ("Hal yang ingin saya maksud adalah...", "Maksud gue tuh yang... itu lho...", "意図を補足する時のフィラー"),
            ("Sebentar, saya sedang mengingatnya...", "Bentar-bentar, apa tuh namanya...", "名前を思い出せない時のフィラー")
        ],
        "drill": [
            ("【Baku→Gaul】どう表現すれば伝わるでしょうか。（Bagaimana sebaiknya saya menjelaskannya ya?）", "Gimana ya jelasinnya, agak rumit sebenernya.", "ギマナ ヤ ジュラスィンニャ、アガッ ルミット スブヌルニャ", "説明に迷うフィラー。"),
            ("【Gaul→Baku】あのー、名前なんだっけ？（Anu... siapa tuh namanya, kok gue lupa ya?）", "Mohon maaf, saya sedang berusaha mengingat nama beliau.", "モホン マアフ、サヤ スダン ブルウサハ ムニンガット ナマ ブリアウ", "名前忘れ ⇄ 公式弁明。"),
            ("【Baku→Gaul】いわば、一種の触媒のようなものです。（Dapat dianalogikan semacam katalisator proses.）", "Kayak semacem pemicu gitu lho, paham kan?", "カヤッ スマチェム プミチュ ギトゥ ロ、パハム カン", "例示フィラー。"),
            ("【Gaul→Baku】なんていうか、ちょっと変な感じ。（Kayak gimanaaa gitu rasanya, aneh pokoknya!）", "Nuansanya terasa agak janggal dan sulit dideskripsikan secara tepat.", "ヌアンサニャ トゥラサ アガッ ジャンガル ダン スリット ディデスクリプスィカン スチャラ トゥパット", "曖昧な違和感。"),
            ("【Baku→Gaul】少し待ってください、確認します。（Mohon tunggu sejenak, saya periksa datanya.）", "Bentar-bentar, tadi naruhnya di mana ya...", "ブンタル ブンタル、タディ ナルーニャ ディ マナ ヤ", "確認フィラー。"),
            ("【Gaul→Baku】要するにそういうこと！（Pokoknya intinya mah kayak gitu lah ya!）", "Secara garis besar kesimpulannya adalah seperti demikian.", "スチャラ ガリス ブサール クスィンプルアンニャ アダラ スプルティ ドゥミキアン", "大まかな締め。"),
            ("【Baku→Gaul】確か、先週の火曜日だったと思います。（Seingat saya, peristiwanya terjadi pada hari Selasa lalu.）", "Kalo gak salah mah hari Selasa deh ya, cmiiw.", "カロ ガッ サラ マ ハリ スラサ デ ヤ、シーエムアイアイダブリュー", "記憶の不確かさ。"),
            ("【Gaul→Baku】あの件、あれはどうなった？（Itu tuh... yang itu gimana kelanjutannya?）", "Perihal agenda yang sebelumnya telah kita bahas, bagaimana perkembangannya?", "プリハル アジェンダ ヤン スブルムニャ トゥラ キタ バハス、バガイマナ プルクンバンガンニャ", "遠回しな質問。"),
            ("【Baku→Gaul】ええと、次の議題は何でしょうか。（Baiklah, agenda apakah yang perlu kita bahas selanjutnya?）", "Terus apa lagi ya abis ini? Ada lagi gak?", "トゥルス アパ ラギ ヤ アビス イニ？ アダ ラギ ガッ", "進行フィラー。"),
            ("【Gaul→Baku】言葉に詰まっちゃった。（Aduh blepotan nih gue ngomongnya, grogi bgt!）", "Mohon maaf penyampaian saya agak terbata-bata karena merasa gugup.", "モホン マアフ プンニャムパイアン サヤ アガッ トゥルバタ バタ カレナ ムラサ ググップ", "緊張フィラー。"),
            ("【Baku→Gaul】大体1時間程度要する見込みです。（Diperkirakan membutuhkan durasi sekitar satu jam.）", "Kira-kira sejam-an lah ya, kurang lebih.", "キラ キラ スジャムアン ラ ヤ、クラン ルビ", "概算時間。"),
            ("【Gaul→Baku】急に思い出せなくなった！（Udah di ujung lidah nih, tapi gak keluar!）", "Istilah tersebut sebenarnya sudah saya ketahui namun luput dari ingatan.", "イスティラ トゥルスブット スブヌルニャ スダ サヤ クタフイ ナムン ルプット ダリ インガタン", "喉元まで出かかっている。"),
            ("【Baku→Gaul】結論から申し上げますとですね。（Apabila ditarik kesimpulan secara langsung...）", "Gini lho gampangnya...", "ギニ ロ ガンパンニャ", "噛み砕きフィラー。"),
            ("【Gaul→Baku】え、私ですか？（Hah, gue? Masa gue sih?）", "Apakah yang Anda maksudkan adalah diri saya?", "アパカ ヤン アンダ マクスッドカン アダラ ディリ サヤ", "聞き返しフィラー。"),
            ("【Baku→Gaul】本日は以上とさせていただきます。（Demikian hal-hal yang dapat kami sampaikan.）", "Udah sih itu aja paling dari gue.", "ウダ スィ イトゥ アジャ パリン ダリ グエ", "発言締めフィラー。")
        ],
        "quiz": [
            ("日常会話で言葉に詰まった時、「なんて言うかさ…どう説明したものか」と時間を稼ぐ定番フィラーは？", ["Gimana ya ngomongnya...", "Siapa nama Anda...", "Berapa harganya...", "Di mana rumahnya..."], 1),
            ("話の途中で「あのー…ええと」と間をつなぐインドネシア語の最も一般的なフィラー詞は？", ["anu", "kucing", "piring", "kursi"], 1),
            ("記憶があやふやな時に「私の記憶が正しければ（間違ってたら訂正して）」と添える略語は？", ["cmiiw (correct me if I'm wrong)", "otw", "gpp", "baper"], 1)
        ]
    },
    {
        "slug": "46-jaksel-slang-code-mixing",
        "title": "【二重言語】南ジャカルタ言葉（Bahasa Jaksel）：which is, literally, basically, prefer, even のコードミキシング",
        "intro": "ジャカルタ南部（Jaksel）の若者やスタートアップ界隈で爆発的に定着した「Bahasa Jaksel（南ジャカルタ言葉）」は、インドネシア語の日常口語の中に英語の接続詞や副詞（which is, literally, basically, prefer, even）を巧みに挟み込む高度なコードミキシング現象です。文化現象としての理解と適切な距離感を学びます。",
        "pairs": [
            ("yang mana / yang berarti (つまり・それは)", "which is...", "文を関係代名詞的につなぐJaksel定番"),
            ("secara harfiah / sungguh-sungguh (文字通り・まじで)", "literally...", "誇張や事実強調の副詞"),
            ("pada dasarnya (基本的には・要するに)", "basically...", "論点をまとめる接続詞"),
            ("lebih memilih (〜のほうを好む)", "prefer...", "選択や好みの表明")
        ],
        "drill": [
            ("【Baku→Gaul】基本的に私は在宅勤務を好みます。（Pada dasarnya saya lebih memilih bekerja dari rumah.）", "Basically gue lebih prefer WFH sih ya, which is lebih fleksibel.", "ベーシックリー グエ ルビ プリファー ダブリューエフエイチ スィ ヤ、ウィッチ イズ ルビ フレクスィベル", "Jaksel構文。"),
            ("【Gaul→Baku】まじで昨日は一睡もできなかった。（Literally gue gak bisa tidur semaleman, overthinking parah!）", "Secara sungguh-sungguh saya sama sekali tidak dapat terlelap sepanjang malam.", "スチャラ スング スング サヤ サマ スカリ ティダッ ダパット トゥルルラップ スパンジャン マラム", "literally ⇄ secara sungguh-sungguh。"),
            ("【Baku→Gaul】彼らでさえその事実を知りません。（Bahkan pihak mereka pun tidak mengetahui fakta tersebut.）", "Even mereka aja gak aware sama isu ini, bayangin deh!", "イーヴン ムレカ アジャ ガッ アウェア サマ イス イニ、バヤンイン デ", "even ⇄ bahkan。"),
            ("【Gaul→Baku】その企画、正直まったく共感できない。（Jujurly gue gak relate sama konsep campaign-nya.）", "Sejujurnya gagasan kampanye tersebut terasa kurang memiliki keterhubungan bagi saya.", "スジュジュルニャ ガガサン カンパニエ トゥルスブット トゥラサ クラン ムミリキ クトゥルフブンガン バギ サヤ", "gak relate ⇄ tidak berhubungan。"),
            ("【Baku→Gaul】それは私にとって大きな精神的負担です。（Hal tersebut menimbulkan beban mental yang cukup berat bagi saya.）", "Itu bikin gue mental breakdown sih, which is gak sehat bgt.", "イトゥ ビキン グエ メンタル ブレイクダウン スィ、ウィッチ イズ ガッ セハット バンゲット", "メンタル負担のJaksel表現。"),
            ("【Gaul→Baku】私の価値観とは合わない。（Gak align sama personal value gue.）", "Gagasan tersebut tidak selaras dengan prinsip moral pribadi saya.", "ガガサン トゥルスブット ティダッ スララス ドゥンガン プリンスィプ モラル プリバディ サヤ", "gak align ⇄ tidak selaras。"),
            ("【Baku→Gaul】結局のところ、すべてはお金次第です。（Pada akhirnya segala sesuatunya ditentukan oleh ketersediaan dana.）", "At the end of the day, tetep ujungnya budget juga kan ya.", "アット ジ エンド オブ ザ デイ、トゥタップ ウジュンニャ バジェット ジュガ カン ヤ", "at the end of the day ⇄ pada akhirnya。"),
            ("【Gaul→Baku】まずは優先順位を整理しよう。（Mesti make sense dulu timeline-nya, baru eksekusi.）", "Jadwal kerja hendaknya disusun secara logis dan masuk akal sebelum dilaksanakan.", "ジャドワル クルジャ フンダッニャ ディススン スチャラ ロギス ダン マスッ アカル スブルム ディラクサナカン", "make sense ⇄ masuk akal。"),
            ("【Baku→Gaul】話が本題から逸れてしまっています。（Pembahasan ini tampaknya telah keluar dari topik utama.）", "Pembahasannya udah agak out of topic ya guys, back to topic yuk!", "プンバハサンニャ ウダ アガッ アウト オブ トピック ヤ ガイズ、バック トゥ トピック ユッ", "out of topic ⇄ keluar topik。"),
            ("【Gaul→Baku】その意見には一理ある。（Make sense sih argumen lu, gak kepikiran sebelumnya.）", "Argumentasi Anda sungguh logis dan memiliki dasar pemikiran yang tepat.", "アルグメンタスィ アンダ スング ロギス ダン ムミリキ ダサール プミキラン ヤン トゥパット", "make sense ⇄ logis。"),
            ("【Baku→Gaul】率直にフィードバックを共有してください。（Mohon sampaikan tanggapan Anda secara terbuka dan jujur.）", "Drop your honest feedback dong guys, no hard feelings ya!", "ドロップ ユア オーネスト フィードバック ドン ガイズ、ノー ハード フィーリングス ヤ", "no hard feelings ⇄ tanpa dendam。"),
            ("【Gaul→Baku】急な変更でパニックになった。（Gue shock bgt mendadak pivoting strategi gini!）", "Saya merasa sangat terkejut atas perubahan arah strategi yang begitu mendadak.", "サヤ ムラサ サンガット トゥルクジュット アタス プルバハン アラ ストラテギ ヤン ブギトゥ ムンダダッ", "pivoting ⇄ ubah haluan。"),
            ("【Baku→Gaul】ワークライフバランスを重視しています。（Saya sangat memprioritaskan keseimbangan antara kerja dan kehidupan pribadi.）", "Gue concern bgt sama work-life balance, biar gak burnout.", "グエ コンサーン バンゲット サマ ワークライフ バランス、ビアル ガッ バーンアウト", "burnout ⇄ lelah mental。"),
            ("【Gaul→Baku】彼女の美的センスは素晴らしい。（Visual feed Instagram-nya aesthetic bgt, suka deh!）", "Tampilan tata letak media sosial miliknya memiliki nilai seni yang sangat memikat.", "タンピラン タタ ルタック メディア ソスィアル ミリクニャ ムミリキ ニライ スニ ヤン サンガット ムミカット", "aesthetic ⇄ indah berseni。"),
            ("【Baku→Gaul】要約しますと、本日の決定事項は以下の通りです。（Sebagai rangkuman, berikut adalah poin-poin keputusan hari ini.）", "So basically, key takeaway meeting hari ini tuh ada tiga ya.", "ソー ベーシックリー、キー テイクアウェイ ミーティング ハリ イニ トゥ アダ ティガ ヤ", "会議のJakselまとめ。")
        ],
        "quiz": [
            ("南ジャカルタ言葉（Bahasa Jaksel）の代名詞的接続詞で「つまり・それは〜なんだけど」と文をつなぐ英語は？", ["which is", "although", "despite", "nevertheless"], 1),
            ("「文字通り・本当に誇張なしでまじで」を意味して会話に頻出するJaksel副詞は？", ["literally", "slowly", "hardly", "rarely"], 1),
            ("「〜のほうを好む、〜のほうが好き」をインドネシア語の会話で英語借用して言う動詞は？", ["prefer", "hate", "cancel", "delay"], 1)
        ]
    },
    {
        "slug": "47-gen-z-millennial-slang-drift",
        "title": "【二重言語】世代間ギャップ口語（Gen Z vs ミレニアル）：fomo, yolo, salty, spill, salfok, cuaks",
        "intro": "インドネシアの言葉の進化は凄まじく、ミレニアル世代（Gen Y）が使っていたスラングと、現在のGen Z（Z世代）がTikTokやXで生み出す最新スラングでは語彙の交代が起きています。「fomo（取り残される恐怖）」「spill（秘密の暴露）」「salfok（誤爆・注目ズレ）」「cuaks（皮肉の吐き捨て感嘆詞）」など、世代間ギャップを埋める最前線語彙を学びます。",
        "pairs": [
            ("takut ketinggalan tren (流行に乗り遅れる恐怖)", "FOMO (fear of missing out)", "イベント・新商品の買い煽り"),
            ("bocorkan rahasianya (秘密を暴露して)", "spill the tea / spill dong", "ウワサ・暴露を催促する"),
            ("salah fokus (注目する場所がズレる)", "salfok", "本題より背景や服装に目が行く"),
            ("ungkapan sindiran sinis (皮肉の吐き捨て)", "... cuaks!", "痛烈な皮肉を言った後の決め台詞")
        ],
        "drill": [
            ("【Baku→Gaul】流行に乗り遅れるのが怖くて買ってしまいました。（Saya membelinya karena takut tertinggal oleh tren terkini.）", "Kena FOMO gue anjir, langsung checkout tanpa mikir!", "クナ フォーモ グエ アンジール、ランスン チェックアウト タンパ ミキール", "FOMO ⇄ takut ketinggalan。"),
            ("【Gaul→Baku】その秘密を詳しく教えて！（Spill dong ceritanya, kepo bgt nih gue!）", "Tolong ceritakan rahasia atau informasi perihal masalah tersebut.", "トロン チュリタカン ラハスィア アタウ インフォルマスィ プリハル マサラ トゥルスブット", "spill ⇄ bocorkan cerita。"),
            ("【Baku→Gaul】本題と違う点に目が行ってしまいました。（Perhatian saya justru teralihkan pada hal yang tidak utama.）", "Gue malah salfok sama kucing di belakangnya, gemoy bgt!", "グエ マラ サルフォッ サマ クチン ディ ブラカンニャ、グモイ バンゲット", "salfok ⇄ salah fokus。"),
            ("【Gaul→Baku】負け惜しみを言わないで。（Gausah salty gitu lah liat orang lain menang!）", "Hindarilah bersikap dengki dan merasa iri hati atas keberhasilan orang lain.", "ヒンダリラ ブルスィカップ ドゥンキ ダン ムラサ イリ ハティ アタス クブルハスィラン オラン ライン", "salty ⇄ iri / dengki。"),
            ("【Baku→Gaul】人生は一度きりなのだから楽しもう。（Hidup ini hanya sekali, maka nikmatilah sebaik mungkin.）", "YOLO lah bro, kapan lagi bisa liburan bareng kayak gini!", "ヨーロー ラ ブロ、カパン ラギ ビサ リブラン バレン カヤッ ブギニ", "YOLO (you only live once)。"),
            ("【Gaul→Baku】口先では正義を語るくせに裏では不正ばかり。（Ngomongnya anti korupsi tapi demen gratifikasi, cuaks!）", "Sangat ironis ketika perkataan moral tidak selaras dengan perbuatan nyata.", "サンガット イロニス クティカ プルカタアン モラル ティダッ スララス ドゥンガン プルブアタン ニャタ", "cuaks ⇄ sindiran sinis。"),
            ("【Baku→Gaul】その意見には全面的に同意します。（Saya sepenuhnya sependapat dengan pernyataan tersebut.）", "Valid no debat sih ini mah, real bgt!", "ヴァリッド ノー デバット スィ イニ マ、リアル バンゲット", "Gen Z同調。"),
            ("【Gaul→Baku】嘘ばっかりついてる。（Cap cap doang, red flag parah kelakuannya!）", "Seluruh perkataannya terindikasi bohong dan perilakunya sangat meragukan.", "スルルー プルカタアンニャ トゥリンディカスィ ボホン ダン プリラクニャ サンガット ムラグカン", "red flag批判。"),
            ("【Baku→Gaul】とても愛らしくて可愛いですね。（Makhluk ini tampak begitu menggemaskan sekali.）", "Kiyowo / gemoy bgt sih bayinya, pengen cubit!", "キヨウォ / グモイ バンゲット スィ バイニャ、ペンゲン チュビット", "gemoy ⇄ menggemaskan。"),
            ("【Gaul→Baku】彼には完全に冷めてしまった。（Udah ilfeel dan gak respect lagi gue sama dia.）", "Saya telah kehilangan seluruh rasa hormat dan simpati terhadap dirinya.", "サヤ トゥラ クヒランガン スルルー ラサ ホルマット ダン スィンパティ トゥルハダップ ディリニャ", "ilfeel ⇄ hilang simpati。"),
            ("【Baku→Gaul】精神的な疲労から回復する必要があります。（Saya perlu memulihkan energi psikis dan ketenangan jiwa.）", "Butuh healing bgt gue, pen liburan ke pantai!", "ブトゥ ヒーリング バンゲット グエ、ペン リブラン ク パンタイ", "healing ⇄ pulihkan mental。"),
            ("【Gaul→Baku】あいつ、本当に自己顕示欲が強い。（Pansos mulu kerjaannya, numpang tenar!）", "Orang tersebut selalu berusaha memanfaatkan ketenaran pihak lain demi popularitas.", "オラン トゥルスブット スラル ブルウサハ ムマンファアットカン クトゥナラン ピハッ ライン ドゥミ ポプラリタス", "pansos ⇄ panjat sosial。"),
            ("【Baku→Gaul】大げさな態度を取るのはおやめください。（Mohon jangan bereaksi secara berlebihan terhadap perkara ini.）", "Gausah lebay deh lu, hal sepele juga!", "ガウサ レバイ デ ル、ハル スペレ ジュガ", "lebay ⇄ berlebihan。"),
            ("【Gaul→Baku】彼は完全に恋人に言いなりだ。（Bucin abis cowoknya, gak boleh kemana-mana!）", "Pria tersebut sepenuhnya tunduk di bawah kendali kekasihnya.", "プリア トゥルスブット スプヌフニャ トゥンドゥッ ディ バワ クンダリ クカスィフニャ", "bucin ⇄ budak cinta。"),
            ("【Baku→Gaul】何気ない日常の美しさを記録しましょう。（Mari mengabadikan momen keseharian yang sederhana namun bermakna.）", "Dump foto bulan ini aesthetic bgt vibe-nya!", "ダンプ フォト ブラン イニ エステティック バンゲット ヴァイブニャ", "photo dump ⇄ dokumentasi momen。")
        ],
        "quiz": [
            ("SNSなどで「秘密や裏話を暴露して！教えて！」と催促する英語由来のスラングは？", ["spill (spill the tea)", "drink", "cook", "wash"], 1),
            ("動画や写真で、本題の主役よりも背景の面白いものに目が行ってしまう現象を表す略語は？", ["salfok (salah fokus)", "fomo", "yolo", "mager"], 1),
            ("政治家や社会の矛盾を痛烈に皮肉った漫才・投稿の末尾に吐き捨てるように叫ぶ流行語は？", ["Cuaks!", "Monggo!", "Punten!", "Tengkyu!"], 1)
        ]
    },
    {
        "slug": "48-code-switching-etiquette",
        "title": "【二重言語】コードスイッチング作法：相手・場面・関係性に応じた切り替え境界と失礼回避術",
        "intro": "インドネシア語の二重言語（Baku vs Gaul）において最も重要なのは、「どちらか一方だけを話すこと」ではなく、「相手の立場・年齢・場面に応じて適切なレジスターを選択し、失礼にならず親愛を示す切り替え（Code-Switching）ができること」です。失礼を回避し、好感度を高める大人の切り替え作法を訓練します。",
        "pairs": [
            ("Kepada atasan / klien (上司・顧客向け)", "Bahasa Baku / Santun", "敬意とプロ意識の維持"),
            ("Kepada rekan sebaya (同僚・友人向け)", "Bahasa Santai / Gaul Halus", "親近感と円滑なチームワーク"),
            ("Di forum rapat resmi (公式会議の場)", "Register Formal Tertib", "正確な議論と記録の担保"),
            ("Di sesi makan siang santai (ランチの雑談)", "Register Kasual Akrab", "本音の交流と心理的安全性")
        ],
        "drill": [
            ("【会議(Baku)→雑談(Gaul)】先ほどの会議の決定に従いましょう。（Mari kita patuhi keputusan rapat resmi tadi.）", "Yaudah cus kita gasin aja keputusan rapat td, seru nih!", "ヤウダ チュス キタ ガスィン アジャ クプトゥサン ラパット タディ、スル ニ", "公式決定 ⇄ 雑談の実行宣言。"),
            ("【雑談(Gaul)→上司報告(Baku)】部長、企画書できました！（Pak, proposalnya udah kelar nih, monggo dicek!）", "Selamat pagi Bapak, draf proposal telah selesai kami susun dan siap diperiksa.", "スラマット パギ バパッ、ドラフ プロポサル トゥラ スルサイ カミ ススン ダン スィアップ ディプ リクサ", "同僚口頭 ⇄ 上司公式報告。"),
            ("【顧客(Baku)→同僚(Gaul)】お客様よりご満足の声をいただきました。（Pihak pelanggan menyampaikan rasa puas atas layanan kita.）", "Klien hepi bgt bro, closing deals kita hari ini!", "クライエン ヘピ バンゲット ブロ、クロージング ディールズ キタ ハリ イニ", "公式成果 ⇄ 同僚とのハイタッチ。"),
            ("【同僚(Gaul)→顧客(Baku)】見積もり送っといたよ！（Udah gue lempar invoice-nya ya!）", "Faktur penagihan resmi telah kami kirimkan melalui pos-el untuk ditindaklanjuti.", "ファクトゥール プナギハン レスミ トゥラ カミ キリムカン ムラルイ ポスエル ウントゥッ ディティンダッ ランジュティ", "口語共有 ⇄ 公式送付案内。"),
            ("【公的スピーチ(Baku)→歓談(Gaul)】本日のご来場を歓迎いたします。（Kami menyambut hangat kehadiran seluruh tamu undangan.）", "Wih rame bgt yg dateng, makasih bgt udah nyempetin mampir ya!", "ウィッ ラメ バンゲット ヤン ダトゥン、マカスィ バンゲット ウダ ニェンペッティン マンピール ヤ", "式典歓迎 ⇄ 立食歓談。"),
            ("【歓談(Gaul)→公的スピーチ(Baku)】みなさん、静かにしてください。（Woi diem dulu napa, mau mulai nih acaranya!）", "Hadirin sekalian, dimohon untuk menempati tempat duduk karena acara akan segera dimulai.", "ハディリン スカリアン、ディモホン ウントゥッ ムヌンパティ トゥムパット ドゥドゥッ カレナ アチャラ アカン スグラ ディムライ", "口頭静止 ⇄ 公式着席案内。"),
            ("【社内通達(Baku)→チャット催促(Gaul)】本日期限のアンケートにご回答願います。（Dimohon kesediaan mengisi kuesioner sebelum batas waktu.）", "Guys jangan lupa isi survei hari ini ya, bentar doang kok!", "ガイズ ジャンガン ルパ イシ スルヴェイ ハリ イニ ヤ、ブンタル ドアン コッ", "公式通達 ⇄ チャット声かけ。"),
            ("【チャット催促(Gaul)→社内通達(Baku)】まだの人早く出して！（Yang belom ngumpulin buruan ya!）", "Bagi rekan-rekan yang belum menyerahkan berkas, mohon segera menuntaskannya.", "バギ ルカン ルカン ヤン ブルム ムニュラカン ブルカス、モホン スグラ ムヌンタスカンニャ", "チャット催促 ⇄ 公式リマインド。"),
            ("【病院受付(Baku)→待合室(Gaul)】保険証のご提示をお願いいたします。（Mohon tunjukkan kartu identitas dan kepesertaan BPJS Anda.）", "Minta kartunya bentar ya kak, mau didata dulu.", "ミンタ カルトゥニャ ブンタル ヤ カッ、マウ ディデータ ドゥル", "窓口形式 ⇄ 親切な口頭対応。"),
            ("【待合室(Gaul)→医師問診(Baku)】腹痛がひどくて歩けない。（Sakit perut parah dok, melilit bgt rasanya!）", "Saya mengalami nyeri hebat pada bagian perut bawah sejak tadi pagi.", "サヤ ムンガラミ ニエリ ヘバット パダ バギアン プルット バワ スジャッ タディ パギ", "患者の口語訴え ⇄ 正確な症状申告。"),
            ("【警察事情聴取(Baku)→友人通報(Gaul)】事故の状況を時系列で陳述してください。（Mohon sampaikan kronologi kejadian secara terperinci.）", "Ceritain pelan-pelan bro, kok lu bisa nabrak tadi?", "チュリタイン プラン プラン ブロ、コッ ル ビサ ナブラッ タディ", "公的調書 ⇄ 友人心配。"),
            ("【友人通報(Gaul)→警察事情聴取(Baku)】バイクが急に飛び出してきたんだ。（Motornya nyelonong kenceng bgt tiba-tiba!）", "Kendaraan roda dua tersebut melaju kencang dari arah samping tanpa menyalakan lampu sinyal.", "クンダラアン ロダ ドゥア トゥルスブット ムラジュ クンチャン ダリ アラ サンピン タンパ ムニャラカン ランプ スィニャル", "口語恐怖 ⇄ 正確な目撃証言。"),
            ("【商談終了(Baku)→懇親会(Gaul)】有意義な議論に心より感謝申し上げます。（Terima kasih atas diskusi konstruktif yang telah berlangsung.）", "Seru bgt obrolannya tadi pak, santai sambil ngopi yuk!", "スル バンゲット オブロランニャ タディ パッ、サンタイ サンビル ンオピ ユッ", "商談公式締め ⇄ 懇親カフェ誘い。"),
            ("【懇親会(Gaul)→商談終了(Baku)】また飲みに行きましょう。（Ntar nongkrong lagi ya bro kapan-kapan!）", "Kami menantikan kesempatan berharga untuk dapat bekerja sama kembali di masa mendatang.", "カミ ムナンティカン クスンパタン ブルハルガ ウントゥッ ダパット ブルクルジャ サマ クンバリ ディ マサ ムンダタン", "口語別れ際 ⇄ 公式次回協力挨拶。"),
            ("【日常の原則】場をわきまえた使い分けこそが真の流暢さである。（Kemampuan menempatkan ragam bahasa sesuai konteks adalah bukti kemahiran sejati.）", "Tau kapan harus formal dan kapan harus santai, itu baru jago!", "タウ カパン ハルス フォルマル ダン カパン ハルス サンタイ、イトゥ バル ジャゴ", "二重言語の極意。")
        ],
        "quiz": [
            ("上司や重要クライアントに公式な報告書を提出する際、最も避けるべき口語表現は？", ["Pak, proposalnya udah kelar nih, monggo dicek!", "Selamat pagi Bapak, dokumen telah kami selesaikan.", "Berikut laporan hasil evaluasi kami.", "Mohon arahan dan masukan dari Bapak."], 1),
            ("同僚同士のSlackチャットで、あまりに硬すぎる「Dengan hormat, bersama ini kami sampaikan...」を使うとどう受け取られやすい？", ["よそよそしく距離を感じる（kaku dan berjarak）", "非常に親切でフレンドリーに感じる", "笑いが起きて盛り上がる", "給料が上がる"], 1),
            ("インドネシア語の二重言語（Diglossia）を運用する上で最も大切な大原則は？", ["TPO（時・場所・相手）に応じて自然にレジスターを切り替える", "どんな場面でも若者スラングだけで通す", "親しい友人にも常に公的硬質標準語だけを使う", "外国人は一切口語を使ってはいけない"], 1)
        ]
    },
    {
        "slug": "49-complete-dialogue-baku-gaul-paired",
        "title": "【二重言語】同一シナリオ完全パラレル対比：同一の商談・雑談シーンを Baku と Gaul で演じ分ける",
        "intro": "全く同じ内容の会話（プロジェクトの進捗確認、スケジュールの相談、問題解決、ランチの誘い）を、「完全公式標準語（Bahasa Baku）」と「完全ストリート口語（Bahasa Gaul）」の完全パラレルな2つのスクリプトで対比します。語彙、語順、助詞、代名詞がどう連動して変換されるかの総決算を行います。",
        "pairs": [
            ("Skenario 1: Evaluasi Proyek (進捗確認)", "Baku: Formal terstruktur ⇄ Gaul: Cepat to-the-point", "プロジェクト進捗のレジスター差"),
            ("Skenario 2: Penundaan Rapat (日程延期)", "Baku: Permohonan maaf santun ⇄ Gaul: Chat santai fleksibel", "日程再調整のレジスター差"),
            ("Skenario 3: Penanganan Krisis (トラブル対応)", "Baku: Analisis mitigasi risiko ⇄ Gaul: Gercep gerak cepat", "危機対応のレジスター差"),
            ("Skenario 4: Makan Siang Bersama (ランチ誘い)", "Baku: Ajakan formal terencana ⇄ Gaul: Cus meluncur spontan", "食事の誘いのレジスター差")
        ],
        "drill": [
            ("【Baku】進捗はいかがですか？順調に進んでいますか？（Bagaimanakah perkembangan proyek saat ini, apakah berjalan lancar?）", "Gimana progresnya bro? Aman-aman aja kan ya?", "ギマナ プログレスニャ ブロ？ アマン アマン アジャ カン ヤ", "進捗確認の対比。"),
            ("【Gaul】順調だよ、予定通り今週中に終わる。（Aman terkendali bro, kelar minggu ini sesuai jadwal.）", "Seluruh tahapan pekerjaan berjalan sesuai rencana dan akan tuntas pekan ini.", "スルルー タハパン プクルジャアン ブルジャラン ススアイ レンチャナ ダン アカン トゥンタス プカン イニ", "順調報告の対比。"),
            ("【Baku】急な要件により、会議の時間を変更願えますか？（Berhubung ada keperluan mendesak, apakah rapat dapat dijadwalkan ulang?）", "Bro sori bgt, bisa reschedule rapatnya gak? Lg ada hal urgent nih.", "ブロ ソリ バンゲット、ビサ リスケジュール ラパットニャ ガッ？ ラギ アダ ハル アージェント ニ", "日程延期の対比。"),
            ("【Gaul】全然大丈夫！午後何時なら空いてる？（Gpp santai aja! Lu bisanya jam berapa siang nanti?）", "Tidak ada masalah, pada pukul berapakah Saudara memiliki waktu luang siang nanti?", "ティダッ アダ マサラ、パダ プクル ブラパカ サウダラ ムミリキ ワクトゥ ルアン スィアン ナンティ", "延期承諾の対比。"),
            ("【Baku】重大なシステムエラーが発生いたしました。（Telah terjadi kendala sistematis yang cukup krusial pada peladen.）", "Gawat bro, server-nya down parah nih!", "ガワット ブロ、サーバーニャ ダウン パラ ニ", "障害発生の対比。"),
            ("【Gaul】すぐ修正パッチ当てるから待って！（Skrg juga gue benerin, tunggu bentar ya!）", "Langkah penanganan teknis akan segera kami laksanakan secara intensif.", "ランカ プナンガナン テクニス アカン スグラ カミ ラクサナカン スチャラ インテンスィフ", "復旧作業の対比。"),
            ("【Baku】昼食をご一緒いたしませんか？（Apakah Saudara berkenan untuk bersantap siang bersama kami?）", "Makan siang bareng yuk guys, laper bgt nih!", "マカン スィアン バレン ユッ ガイズ、ラペル バンゲット ニ", "ランチ誘いの対比。"),
            ("【Gaul】いいね！何食べに行く？（Cus meluncur! Mau makan apa kita hari ini?）", "Tentu saja dengan senang hati, hidangan apakah yang hendak kita nikmati bersama?", "トゥントゥ サジャ ドゥンガン スナン ハティ、ヒダンガン アパカ ヤン フンダッ キタ ニクマティ ブルサマ", "ランチ同調の対比。"),
            ("【Baku】近所の日本食レストランはいかがでしょうか。（Bagaimana apabila kita mengunjungi restoran Jepang terdekat?）", "Gimana kalo sushi deket kantor aja? Enak dan gak terlalu rame.", "ギマナ カロ ススィ ドゥクット カントール アジャ？ エナッ ダン ガッ トゥルラル ラメ", "店舗提案の対比。"),
            ("【Gaul】賛成！すぐ行こう！（Setuju parah, kuy berangkat skrg sebelum kehabisan tempat!）", "Pilihan yang sangat tepat, mari segera berangkat sebelum tempat tersebut penuh.", "ピリハン ヤン サンガット トゥパット、マリ スグラ ブルランカット スブルム トゥムパット トゥルスブット プヌ", "即決出発の対比。"),
            ("【Baku】お支払いは各自でよろしいですか？（Apakah pembayaran tagihan hendak dilakukan secara terpisah?）", "Split bill aja ya kita bayarnya biar gampang.", "スプリット ビル アジャ ヤ キタ バヤルニャ ビアル ガンパン", "会計の対比。"),
            ("【Gaul】私がまとめて払っておくよ！（Gue talangin dulu aja, ntar lu transfer via QRIS ya!）", "Perkenankan saya menyelesaikan pembayaran terlebih dahulu melalui transaksi elektronik.", "プルクナンカン サヤ ムンニュレサイカン プンバヤラン トゥルルビ ダフル ムラルイ トランサクスィ エレクトロニック", "立替の対比。"),
            ("【Baku】大変有意義で楽しい時間でした。（Pertemuan dan santap siang kali ini sungguh terasa sangat berkesan.）", "Seru bgt nongkrong siang ini, kenyang bego jadinya!", "スル バンゲット ノンクロン スィアン イニ、クニャン ベゴ ジャディニャ", "食事後の感想の対比。"),
            ("【Gaul】また明日仕事頑張ろう！（Besok gaspol lagi kerjanya, thank you ya bro!）", "Semoga semangat kerja kita semakin terpacu untuk menuntaskan target esok hari.", "スモガ スマンガット クルジャ キタ スマキン トゥルパチュ ウントゥッ ムヌンタスカン ターゲット エソッ ハリ", "激励の対比。"),
            ("【まとめ】同一の意図がこれほど豊かに二重に表現される。（Sebuah niat yang sama dapat terwujud dalam dua ragam bahasa yang begitu kaya.）", "Dua dunia bahasa dalam satu kepala, itulah indahnya bahasa Indonesia!", "ドゥア ドゥニア バハサ ダラム サトゥ クパラ、イトゥラ インダニャ バハサ インドネシア", "二重言語の美学。")
        ],
        "quiz": [
            ("ランチの誘いで「よし、すぐ行こう！」と元気に出発する時の若者スラングは？", ["Cus meluncur!", "Mohon izin permisi...", "Tolong jangan pergi...", "Selamat jalan..."], 1),
            ("食事代を「各自で割り勘にする」ことを表すオフィス英語借用スラングは？", ["split bill", "split second", "split banana", "split screen"], 1),
            ("仲間同士で「とりあえず俺が立て替えておくよ」と親身に申し出る口語動詞は？", ["gue talangin dulu", "gue buang dulu", "gue curi dulu", "gue simpen dulu"], 1)
        ]
    }
]

# 1141-1149の生成
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

# 1150: 総合診断クリニック（50問総合変換診断）の生成
f50_path = "docs/diglossia/50-diglossia-comprehensive-drill.md"
drill50_data = [
    # 1-10: 基本文法・短縮・動詞・受動態
    ("【Baku→Gaul】彼はすでに帰宅しました。（Dia sudah pulang ke rumah.）", "Dia udah balik ke rumah.", "ディア ウダ バリッ ク ルマ", "sudah → udah, pulang → balik。"),
    ("【Gaul→Baku】まだ食べてないよ。（Belom makan nih gue.）", "Saya belum sempat menikmati makanan.", "サヤ ブルム スンパット ムニクマティ マカナン", "belom → belum, gue → saya。"),
    ("【Baku→Gaul】母のために服を買います。（Saya membeli pakaian untuk ibu.）", "Gue beliin baju buat nyokap.", "グエ ベリイン バジュ ブアット ニョカップ", "membeli → beli, untuk → buat, ibu → nyokap。"),
    ("【Gaul→Baku】足を踏まれちゃった。（Kaki gue keinjek orang di KRL!）", "Kaki saya terinjak oleh penumpang di kereta.", "カキ サヤ トゥルインジャッ オレ プヌンパン ディ クレタ", "ke-受動 → ter-。"),
    ("【Baku→Gaul】私は行きたくありません。（Saya tidak ingin pergi ke sana.）", "Gue gak mau cabut kesono.", "グエ ガッ マウ チャブット クソノ", "tidak → gak/nggak, pergi → cabut。"),
    ("【Gaul→Baku】どうして遅刻したの？（Kok telat sih lu?）", "Mengapakah Anda terlambat hadir hari ini?", "ムンアパカ アンダ トゥルランバット ハディール ハリ イニ", "kok ... sih → mengapa。"),
    ("【Baku→Gaul】何を笑っているのですか？（Apa yang sedang Anda tertawakan?）", "Ngetawain apaan sih lu dari tadi?", "ンゲタワイン アパアン スィ ル ダリ タディ", "apa → apaan, meN-kan → nge-in。"),
    ("【Gaul→Baku】ちょっと待ってて！（Bentar ya, otw nih!）", "Mohon tunggu sebentar, saya sedang dalam perjalanan.", "モホン トゥング スブンタル、サヤ スダン ダラム プルジャラナン", "bentar → sebentar, otw → dalam perjalanan。"),
    ("【Baku→Gaul】しかし、予算が足りません。（Tetapi, anggaran tidak mencukupi.）", "Tapi ya gitu, duitnya gak cukup.", "タピ ヤ ギトゥ、ドゥイットニャ ガッチュクップ", "tetapi → tapi, anggaran → duit。"),
    ("【Gaul→Baku】彼が犯人に違いない。（Pasti dia tuh pelakunya, kan ya!）", "Dapat dipastikan bahwa beliaulah pelaku utamanya.", "ダパット ディパスティカン バフワ ブリアウラ プラク ウタマニャ", "kan ya → dapat dipastikan。"),
    
    # 11-20: 助詞（sih, dong, deh, kok, lho, ya）
    ("【Baku→Gaul】もちろん知っていますよ！（Tentu saja saya mengetahuinya dengan baik!）", "Tau dong, masa gak tau sih!", "タウ ドン、マサ ガッ タウ スィ", "dong（当然・親密）。"),
    ("【Gaul→Baku】やってみたら？おすすめだよ！（Coba dulu deh, seru banget lho!）", "Alangkah baiknya bila Anda mencobanya terlebih dahulu.", "アランカ バイッニャ ビラ アンダ ムンチョバニャ トゥルルビ ダフル", "deh（推奨）＋ lho（感嘆・告知）。"),
    ("【Baku→Gaul】どうしてそんなに怒っているの？（Mengapa Anda begitu marah sekali?）", "Kok ngegas bgt sih lu, santai napa!", "コッ ンゲガス バンゲット スィ ル、サンタイ ナパ", "kok ... sih（不審・驚き）。"),
    ("【Gaul→Baku】あれ、雨降ってきたの？（Lho, kok udah ujan aja sih?）", "Wah, sungguh tak disangka hujan telah mulai turun.", "ワ、スング タッ ディサンカ フジャン トゥラ ムライ トゥルン", "lho kok（意外性の重なり）。"),
    ("【Baku→Gaul】明日忘れずに来てくださいね。（Mohon tidak lupa untuk hadir esok hari.）", "Besok dateng ya, jangan sampe lupa lho!", "ベソッ ダトゥン ヤ、ジャンガン サンペ ルパ ロ", "ya（確認・念押し）。"),
    ("【Gaul→Baku】まあ、仕方ないよね。（Yaudah deh, pasrah aja gue mah.）", "Baiklah, saya menerima keputusan ini dengan ikhlas.", "バイッラ、サヤ ムヌリマ クプトゥサン イニ ドゥンガン イクラス", "yaudah deh（妥協・受容）。"),
    ("【Baku→Gaul】私は実際行きたくないのです。（Sebenarnya saya pribadi enggan untuk hadir.）", "Gue sih sebenernya agak mager ya mau dateng.", "グエ スィ スブヌルニャ アガッ マゲル ヤ マウ ダトゥン", "sih sebenernya（控えめな本音）。"),
    ("【Gaul→Baku】君も知ってるでしょ？（Kan lu sendiri yg ngomong kemarin!）", "Bukankah Anda sendiri yang menyatakannya kemarin?", "ブカンカ アンダ スンディリ ヤン ムンニャタカンニャ クマレン", "kan（同意の引き出し）。"),
    ("【Baku→Gaul】絶対に秘密にしておいてください。（Mohon jaga kerahasiaan ini sebaik-baiknya.）", "Awas ya, jangan bocor kemana-mana lho!", "アワス ヤ、ジャンガン ボチョール クマナ マナ ロ", "念押し警告。"),
    ("【Gaul→Baku】いい加減にして！（Udah dong, jangan ribut mulu napa!）", "Cukuplah, dimohon untuk menghentikan perdebatan ini.", "チュクップラ、ディモホン ウントゥッ ムンヘンティカン プルデバタン イニ", "dong（促し・制止）。"),

    # 21-30: チャット略語・スラング造語・プロケム
    ("【Baku→Gaul】了解、すぐに向かいます。（Baik, saya akan segera meluncur ke lokasi.）", "Sip otw skrg ya bro, gpp telat dkit.", "スィップ オーテーウェー スカラン ヤ ブロ、ジーペーペー トゥラット ディキット", "otw, gpp, skrg。"),
    ("【Gaul→Baku】（笑）（Wkwk, ngakak abis liat fotonya!）", "Tertawa terbahak-bahak melihat gambar tersebut.", "トゥルタワ トゥルバハッ バハッ ムリハット ガンバール トゥルスブット", "wkwk / ngakak ⇄ tertawa。"),
    ("【Baku→Gaul】外に出るのが億劫です。（Saya merasa malas untuk beranjak keluar.）", "Lagi mager parah nih di kasur.", "ラギ マゲル パラ ニ ディ カスール", "mager ⇄ malas gerak。"),
    ("【Gaul→Baku】そんなに感情的にならないで。（Gausah baper gitu dong, cuma guyon!）", "Mohon jangan memasukkan gurauan ini ke dalam hati.", "モホン ジャンガン ムマスッカン グラウアン イニ ク ダラム ハティ", "baper ⇄ bawa perasaan。"),
    ("【Baku→Gaul】行こう、映画見に行こう！（Ayo kita pergi menonton bioskop bersama!）", "Kuy nonton bioskop bareng!", "クイ ノントン ビオスコップ バレン", "kuy ⇄ yuk (Prokem)。"),
    ("【Gaul→Baku】明日会える？（Besok sabi gak ketemuan?）", "Apakah besok Anda bisa meluangkan waktu bertemu?", "アパカ ベソッ アンダ ビサ ムルアンカン ワクトゥ ブルトゥム", "sabi ⇄ bisa (Prokem)。"),
    ("【Baku→Gaul】ただの売名行為に過ぎません。（Hal itu hanyalah tindakan panjat sosial semata.）", "Cuma pansos doang tuh caper!", "チュマ パンソス ドアン トゥ チャペル", "pansos ⇄ panjat sosial。"),
    ("【Gaul→Baku】彼は恋に盲目だ。（Bucin parah dia sama pacarnya.）", "Ia sangat terikat dan diperbudak oleh cinta kekasihnya.", "イア サンガット トゥリカット ダン ディプルブダッ オレ チンタ クカスィフニャ", "bucin ⇄ budak cinta。"),
    ("【Baku→Gaul】暇で何もすることがありません。（Saya memiliki banyak waktu luang tanpa kegiatan.）", "Lagi gabut bgt nih, scroll TikTok mulu.", "ラギ ガブット バンゲット ニ、スクロール ティックトック ムル", "gabut ⇄ tidak ada kegiatan。"),
    ("【Gaul→Baku】かっこつけすぎだよ。（Jangan sok jaim deh lu di depan orang!）", "Jangan terlalu berusaha menjaga citra diri secara berlebihan.", "ジャンガン トゥルラル ブルウサハ ムンジャガ チトラ ディリ スチャラ ブルレビハン", "jaim ⇄ jaga image。"),

    # 31-40: 方言借用（ジャワ、スンダ、プラナカン、スラバヤ、メダン）
    ("【Baku→Gaul】どうぞ、先にお召し上がりください。（Silakan makan hidangan ini lebih dahulu.）", "Monggo mas, dicicipi dulu hidangannya.", "モンゴ マス、ディチチピ ドゥル ヒダンガンニャ", "monggo（ジャワ語どうぞ）。"),
    ("【Gaul→Baku】本当にありがとうございました！（Hatur nuhun pisan ya kang!）", "Terima kasih banyak atas segala bantuannya saudara.", "トゥリマ カシ バニャッ アタス スガラ バントゥアンニャ サウダラ", "hatur nuhun pisan（スンダ語感謝）。"),
    ("【Baku→Gaul】今回の取引で大きな利益が出ました。（Transaksi bisnis ini menghasilkan keuntungan melimpah.）", "Wih mantap, cuan gede nih dari bisnis!", "ウィッ マンタップ、チュアン グデ ニ ダリ ビスニス", "cuan（中華系利益）。"),
    ("【Gaul→Baku】兄貴、これいくら？（Cak, piro regane iki?）", "Berapakah harga barang ini wahai saudara penjual?", "ブラパカ ハルガ バラン イニ ワハイ サウダラ プンジュアル", "cak / piro（スラバヤ口語）。"),
    ("【Baku→Gaul】今日は信じられないほど暑い！（Hari ini cuaca terasa sangat panas luar biasa.）", "Panas kali bah hari ini lae, gersang!", "パナス カリ バー ハリ イニ ラエ、ゲルサン", "kali / bah / lae（メダン口語）。"),
    ("【Gaul→Baku】大げさに怒らないで！（Ojok nesu-nesu ta rek, santai ae!）", "Mohon jangan lekas marah wahai kawan-kawan sekalian.", "モホン ジャンガン ルカス マラ ワハイ カワン カワン スカリアン", "ojok / ta / rek（東ジャワ口語）。"),
    ("【Baku→Gaul】適当に柔軟に安くしておいてよ。（Tolong beri kelonggaran harga yang fleksibel.）", "Udah cincai lah ya harganya sama temen sendiri.", "ウダ チンチャイ ラ ヤ ハルガニャ サマ トゥムン スンディリ", "cincai（プラナカン柔軟性）。"),
    ("【Gaul→Baku】道を通してください。（Punten nya mang, numpang lewat sakedap.）", "Permisi, perkenankan saya untuk lewat sejenak.", "プルミスィ、プルクナンカン サヤ ウントゥッ レワット スジュナッ", "punten / sakedap（スンダ語）。"),
    ("【Baku→Gaul】調子はどうですか？元気ですか？（Bagaimana kabarmu kawan, apakah baik-baik saja?）", "Piye kabare rek, sehat-sehat kabeh kan?", "ピエ カバレ レッ、セハット セハット カベ カン", "piye / kabeh（ジャワ語近況）。"),
    ("【Gaul→Baku】頭が痛くて割れそうだ。（Pening kali kepala awak mikirin kerjaan.）", "Kepala saya terasa sangat pening memikirkan beban pekerjaan.", "プパラ サヤ トゥラサ サンガット プニン ムミキルカン ブバン プクルジャアン", "pening kali / awak（スマトラ口語）。"),

    # 41-50: Jaksel、世代スラング、感情爆発、総合レジスター
    ("【Baku→Gaul】基本的に私はこの案を支持します。（Pada dasarnya saya lebih menyukai alternatif ini.）", "Basically gue lebih prefer opsi ini sih, which is lebih make sense.", "ベーシックリー グエ ルビ プリファー オプスィ イニ スィ、ウィッチ イズ ルビ メイク センス", "Jaksel構文。"),
    ("【Gaul→Baku】その秘密を詳しく教えて！（Spill dong ceritanya, penasaran bgt nih!）", "Tolong bocorkan informasi rahasia perihal peristiwa tersebut.", "トロン ボチョルカン インフォルマスィ ラハスィア プリハル プリスティワ トゥルスブット", "spill ⇄ bocorkan cerita。"),
    ("【Baku→Gaul】うわっ、本当にびっくりした！（Astaga, saya sungguh merasa sangat terkejut!）", "Anjir, kaget setengah mati gue barusan!", "アンジール、カゲット ス トゥンガ マティ グエ バルサン", "anjir（感嘆詞）。"),
    ("【Gaul→Baku】この企画、まじでイカれてる！（Gokil abis idenya bro, GG parah!）", "Gagasan konsep ini sungguh sangat luar biasa inovatif.", "ガガサン コンセプ イニ スング サンガット ルアル ビアサ イノヴァティフ", "gokil abis / GG ⇄ luar biasa。"),
    ("【Baku→Gaul】他人の私生活を詮索しないで。（Jangan mencampuri urusan pribadi orang lain.）", "Gausah kepo deh lu sama privasi orang!", "ガウサ ケポ デ ル サマ プリヴァスィ オラン", "kepo ⇄ ingin tahu urusan orang。"),
    ("【Gaul→Baku】他人の成功に嫉妬しないで。（Jangan suka julid liat temen sukses!）", "Hindarilah bersikap dengki dan sinis terhadap pencapaian rekan Anda.", "ヒンダリラ ブルスィカップ ドゥンキ ダン スィニス トゥルハダップ プンチャパイアン ルカン アンダ", "julid ⇄ dengki dan sinis。"),
    ("【Baku→Gaul】お勧めの選択肢は何ですか？（Opsi manakah yang sebaiknya dipilih?）", "Mendingan pilih yang mana nih bro menurut lu?", "メンディンガン ピリ ヤン マナ ニ ブロ ムヌルット ル", "mendingan ⇄ sebaiknya。"),
    ("【Gaul→Baku】会議の決定に従ってすぐ動こう！（Cus kita gasin hasil meeting tadi!）", "Mari segera kita tindak lanjuti hasil keputusan rapat secara cepat.", "マリ スグラ キタ ティンダッ ランジュティ ハシル クプトゥサン ラパット スチャラ チパット", "cus gasin ⇄ segera tindak lanjuti。"),
    ("【Baku→Gaul】ご多忙のところお時間をいただき心より感謝申し上げます。（Terima kasih sebesar-besarnya atas waktu yang telah diluangkan.）", "Tengkyu bgt ya udah nyempetin waktu buat ngobrol santai!", "テンキュー バンゲット ヤ ウダ ニェンペッティン ワクトゥ ブアット ンオブロル サンタイ", "感謝のレジスター変換。"),
    ("【総合総括】Baku と Gaul の二重言語を自在に行き来する。（Menguasai dwibahasa Baku dan Gaul secara lincah dan beretika.）", "Lancar Baku, jago Gaul, paham etika: itulah bahasa Indonesia sejati!", "ランチャール バク、ジャゴ ガウル、パハム エティカ：イトゥラ バハサ インドネシア スジャティ", "二重言語の到達点。")
]

lines50 = []
lines50.append("# 【二重言語総括】標準語（Baku）⇄ 街角口語（Gaul）50問総合変換診断クリニック\n")
lines50.append("セクション27で学んだ「日常動作、動詞meN-脱落、ke-受動態、代名詞、否定詞、アスペクト、疑問詞、助詞連打、WA略語、プロケム、方言借用（ジャワ・スンダ・プラナカン・スラバヤ・メダン）、南ジャカルタ言葉（Jaksel）、若者世代スラング、感情表出」の全領域を総括する、50問の完全双方向リライト総合診断クリニックです。\n")

lines50.append("## 1. 総合レベル判定基準\n")
lines50.append("| スコア（正答数） | レベル称号 | 診断結果と学習アドバイス |")
lines50.append("|---|---|---|")
lines50.append("| **45 〜 50 問** | **ネイティブ・バイリンガル級 (Master)** | 公式スピーチから街角の砕けたスラングまで完璧に制御。TPO判断も万全です。 |")
lines50.append("| **35 〜 44 問** | **上級ストリートマスター (Advanced)** | 日常の会話やチャット、方言借用にも柔軟に対応可能。更なる洗練を目指しましょう。 |")
lines50.append("| **25 〜 34 問** | **中級口語実践者 (Intermediate)** | 基本的な短縮形や助詞は理解できているが、スラングや方言の即応に課題があります。 |")
lines50.append("| **0 〜 24 問** | **教科書固定化レジスター (Beginner)** | 標準語（Baku）に偏りすぎており、口語の聞き取りや砕けた会話に壁を感じる段階です。 |")
lines50.append("")

lines50.append("## 2. 50問総合変換診断ドリル\n")
lines50.append("> [!IMPORTANT]")
lines50.append("> **診断ルール**: 各問題を声に出して1〜2秒以内に即答してください。直感的に適切なレジスターへ言い換えられるかをテストします。\n")

for idx, (prompt, target_sent, kana, exp) in enumerate(drill50_data, 1):
    m = re.match(r'^(【.+?】)(.+?)（(.+?)）$', prompt)
    if m:
        tag, jp, orig = m.group(1), m.group(2), m.group(3)
        lines50.append(f"### 第{idx}問: {tag}「**{jp}**」（{orig}）\n")
    else:
        lines50.append(f"### 第{idx}問: 「**{prompt}**」\n")
    lines50.append('<div class="id-example">')
    lines50.append(f'<div class="id-sentence"><strong>{target_sent}</strong></div>')
    lines50.append(f'<div class="id-pronunciation">発音: {kana}</div>')
    lines50.append(f'<div class="id-translation">解説: {exp}</div>')
    lines50.append('</div>\n')

lines50.append("## 3. セクション27修了チェッククイズ\n")
quiz50 = [
    ("インドネシア語の「Baku（標準語）」と「Gaul（口語）」の使い分けにおいて最も肝要なことは？", ["相手の立場や場面（TPO）に応じて自然にレジスターを切り替えること", "外国人は常に教科書調のBakuだけを使うこと", "どんな公的な場でも最新スラングを連発すること", "ルビを振って発音すること"], 1),
    ("ジャカルタの若者・ビジネス層で使われる「which is」「literally」「basically」などの混交を何と呼ぶ？", ["南ジャカルタ言葉（Bahasa Jaksel）", "スラバヤ弁", "メダン方言", "古マレー語"], 1),
    ("ジャワ語・スンダ語・中国語など多文化が融合した口語表現を学ぶ最大の学習メリットは？", ["心理的距離を一気に縮め、本音のコミュニケーションと現地社会への融合が実現すること", "試験の点数だけが上がること", "日本語を忘れること", "文法を無視できるようになること"], 1)
]

for q_idx, (q_text, opts, ans_idx) in enumerate(quiz50, 1):
    lines50.append(f"### 問{q_idx}: {q_text}\n")
    for o_idx, opt in enumerate(opts, 1):
        mark = " (正解)" if o_idx == ans_idx else ""
        lines50.append(f"- [{ 'x' if o_idx == ans_idx else ' ' }] {o_idx}. {opt}{mark}")
    lines50.append("")

with open(f50_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines50))
print(f"Generated: {f50_path}")

print("Batch 1141-1150 generated successfully. Section 27 completed!")
