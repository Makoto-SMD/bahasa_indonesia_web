# -*- coding: utf-8 -*-
import os
import re

articles_data = [
    {
        "slug": "11-particle-dong-in-action",
        "title": "【二重言語】文末詞「dong」の感情色彩：当然の主張、親しい促し、甘えの完全攻略",
        "intro": "インドネシア語の会話で「dong」が付くと、言葉に温かみ、当然のニュアンス、または親しい甘え・おねだりの感情が宿ります。「Tentu saja（もちろん）」と堅苦しく答える代わりに「Iya dong!」と言うだけで、一瞬でネイティブとの距離がゼロになります。",
        "pairs": [
            ("Tentu saja saya bisa.", "Bisa dong!", "もちろんできるよ！（当然の主張）"),
            ("Tolong bantu saya.", "Bantuin dong!", "手伝ってよ〜（親しい促し・甘え）"),
            ("Jangan marah kepada saya.", "Jangan marah dong.", "怒らないでよ〜（宥め）"),
            ("Silakan dicoba makanannya.", "Cobain dong!", "食べてみてよ！（気軽なおすすめ）")
        ],
        "drill": [
            ("【Baku→Gaul】もちろん知ってるよ！（Tentu saja saya tahu.）", "Tahu dong!", "タフ ドン", "当然の肯定 Tahu dong!。"),
            ("【Gaul→Baku】教えてよ〜！（Kasih tahu dong!）", "Tolong beritahukan kepada saya.", "トロン ブリタフカン クパダ サヤ", "親しい依頼 Kasih tahu dong。"),
            ("【Baku→Gaul】笑顔を見せてよ。（Tersenyumlah.）", "Senyum dong!", "スニュム ドン", "促し Senyum dong。"),
            ("【Gaul→Baku】拗ねないでよ。（Jangan ngambek dong.）", "Mohon jangan merajuk lagi.", "モホン ジャンガン ムラジュッ ラギ", "宥め jangan ngambek。"),
            ("【Baku→Gaul】早く来てよ。（Cepatlah datang ke sini.）", "Cepetan dateng dong!", "チュプタン ダテン ドン", "催促 Cepetan dong。"),
            ("【Gaul→Baku】君も行かなきゃ！（Lu juga harus ikut dong!）", "Anda tentu juga harus ikut serta bersama kami.", "アンダ トゥントゥ ジュガ ハルス イクット スルタ ブルサマ カミ", "当然の主張 ikut dong。"),
            ("【Baku→Gaul】一口ちょうだい！（Bolehkah saya minta sedikit?）", "Minta dikit dong!", "ミンタ ディキット ドン", "甘え・おねだり minta dong。"),
            ("【Gaul→Baku】真面目にやってよ。（Yang bener dong kerjanya.）", "Harap bekerja dengan sungguh-sungguh dan benar.", "ハラップ ブルクルジャ ドゥンガン スングスング ダン ブナル", "促し yang bener dong。"),
            ("【Baku→Gaul】私にも見せて。（Tolong perlihatkan kepada saya.）", "Liat dong!", "リアット ドン", "気軽なお願い Liat dong。"),
            ("【Gaul→Baku】割り勘にしてよ。（Bagi dua dong biayanya.）", "Mari kita bagi dua biaya ini secara merata.", "マリ キタ バギ ドゥア ビアヤ イニ スチャラ ムラタ", "提案 bagi dua dong。"),
            ("【Baku→Gaul】座りなよ。（Silakan Anda duduk.）", "Duduk sini dong.", "ドゥドゥッ スィニ ドン", "親しい勧め Duduk dong。"),
            ("【Gaul→Baku】信じてよ！（Percaya dong sama gue!）", "Tolong percayalah kepada perkataan saya.", "トロン プルチャヤラ クパダ プルカタアン サヤ", "強い訴え Percaya dong。"),
            ("【Baku→Gaul】忘れないでね。（Jangan sampai lupa ya.）", "Jangan lupa dong!", "ジャンガン ルパ ドン", "念押し jangan lupa dong。"),
            ("【Gaul→Baku】奢ってよ〜！（Traktir dong bro!）", "Tolong traktir saya makanan kali ini.", "トロン トラクティル サヤ マカナン カリ イニ", "おねだり Traktir dong。"),
            ("【Baku→Gaul】負けるな、頑張れ！（Tetaplah bersemangat!）", "Semangat dong!", "スマンガット ドン", "励まし Semangat dong!。")
        ],
        "quiz": [
            ("相手に「もちろん知ってるよ！（当然でしょ）」と笑顔で答えるフレーズは？", ["Tahu dong!", "Tahu sih.", "Tahu deh.", "Tahu kok."], 1),
            ("友人に甘えて「一口ちょうだいよ〜！」とおねだりする定番口語は？", ["Minta dikit dong!", "Saya memohon sedikit.", "Harap berikan makanan.", "Boleh saya ambil."], 1),
            ("不機嫌な友達を「怒らないでよ〜」と和ませる言葉は？", ["Jangan marah dong.", "Dilarang marah.", "Tidak boleh marah.", "Bukan marah Anda."], 1)
        ]
    },
    {
        "slug": "12-particle-deh-in-action",
        "title": "【二重言語】文末詞「deh」のニュアンス：妥協、決断、おすすめ、確認の表現力",
        "intro": "「deh」は話し手の心の動きを表す繊細な文末詞です。「もういいや、そうしよう（妥協・決断）」、「これ本当におすすめだよ！（推奨）」、「〜だよね？（確認）」など、1文字添えるだけで会話がグッとこなれた印象になります。",
        "pairs": [
            ("Baiklah, saya setuju saja.", "Ya udah deh, gue ikut aja.", "妥協・決断（まあいいや、従うよ）"),
            ("Makanan ini sangat enak sekali.", "Enak banget deh makanannya!", "心からのおすすめ（本当におすすめ！）"),
            ("Saya minta maaf atas kesalahan saya.", "Maaf deh, gue yang salah.", "素直な謝罪・折れる（ごめんね）"),
            ("Terserah Anda saja.", "Terserah lu deh.", "相手に委ねる（君にお任せするよ）")
        ],
        "drill": [
            ("【Baku→Gaul】まあいいか、やってみよう。（Baiklah, mari kita coba.）", "Ya udah deh, kita coba dulu.", "ヤ ウダ デ、キタ チョバ ドゥル", "妥協決断 Ya udah deh。"),
            ("【Gaul→Baku】この映画、本当に面白いよ！（Seru banget deh filmnya!）", "Film ini sungguh sangat menarik untuk ditonton.", "フィルム イニ スング サンガット ムナリッ ウントゥッ ディトントン", "推奨 Seru banget deh。"),
            ("【Baku→Gaul】私が悪かった、ごめんね。（Saya yang bersalah, maafkan.）", "Gue yang salah deh, maaf ya.", "グエ ヤン サラ デ、マアフ ヤ", "折れる・謝罪 salah deh。"),
            ("【Gaul→Baku】君が決めていいよ。（Terserah lu deh mau ke mana.）", "Terserah kepada keputusan Anda hendak ke mana.", "トゥルスラ クパダ クプトゥサン アンダ ヘンダッ ク マナ", "一任 terserah lu deh。"),
            ("【Baku→Gaul】もう帰ろうかな。（Sepertinya saya ingin pulang.）", "Gue balik duluan deh kayaknya.", "グエ バリッ ドゥルアン デ カヤッニャ", "独り言決断 balik deh。"),
            ("【Gaul→Baku】これ買っちゃおう！（Beli yang ini aja deh!）", "Saya memutuskan untuk membeli barang yang ini saja.", "サヤ ムムトゥスカン ウントゥッ ムンブリ バラン ヤン イニ サジャ", "即決 aja deh。"),
            ("【Baku→Gaul】言わない方がよかった。（Sebaiknya saya tidak mengatakannya.）", "Nyesel deh gue ngomong gitu.", "ニェセル デ グエ ンゴモン ギトゥ", "後悔 nyesel deh。"),
            ("【Gaul→Baku】明日また連絡するね。（Besok gue kabarin lagi deh.）", "Besok saya pasti akan memberikan kabar lagi.", "ブソッ サヤ パスティ アカン ムンブリカン カバル ラギ", "確認約束 lagi deh。"),
            ("【Baku→Gaul】これ、君にぴったりだよ！（Ini sangat cocok untuk Anda.）", "Cocok banget deh di lu!", "チョチョッ バンゲット デ ディ ル", "太鼓判 cocok banget deh。"),
            ("【Gaul→Baku】もうこれ以上食べられない。（Udah kenyang banget deh gue.）", "Saya sudah merasa sangat kenyang sekali.", "サヤ スダ ムラサ サンガット クニャン スカリ", "限界 kenyang banget deh。"),
            ("【Baku→Gaul】諦めます。（Saya menyerah saja.）", "Nyerah deh gue, susah amat.", "ニェラ デ グエ、スサ アマット", "諦め nyerah deh。"),
            ("【Gaul→Baku】気をつけて行ってらっしゃい。（Hati-hati di jalan deh ya.）", "Semoga senantiasa berhati-hati dalam perjalanan.", "スモガ スナンティアサ ブルハティハティ ダラム プルジャラナン", "温かい送り出し hati-hati deh ya。"),
            ("【Baku→Gaul】彼を待つのはやめよう。（Mari kita tidak usah menunggu dia.）", "Nggak usah nungguin dia deh.", "ンガッ ウサ ヌングイン ディア デ", "取りやめ nggak usah... deh。"),
            ("【Gaul→Baku】本当に不思議だな。（Aneh banget deh kejadiannya.）", "Kejadian tersebut sungguh terasa sangat ganjil.", "クジャディアン トゥルスブット スング トゥラサ サンガット ガンジル", "実感 aneh banget deh。"),
            ("【Baku→Gaul】明日また考えよう。（Mari kita pikirkan lagi besok.）", "Besok aja deh kita pikirin lagi.", "ブソッ アジャ デ キタ ピキリン ラギ", "先送り besok aja deh。")
        ],
        "quiz": [
            ("迷った末に「まあいいや、そうしよう！」と決断・妥協する口語フレーズは？", ["Ya udah deh!", "Iya dong!", "Bukan sih!", "Kenapa kok!"], 1),
            ("友人に「このカフェ、本当におすすめだよ！」と絶賛する文末詞は？", ["Keren banget deh!", "Keren amat dong?", "Keren kah ya?", "Keren sih bukan."], 1),
            ("自分が折れて「私が悪かったよ、ごめんね」と認める時の言い回しは？", ["Gue yang salah deh, maaf ya.", "Lu yang salah dong.", "Bukan salah gue sih.", "Salah siapa kok."], 1)
        ]
    },
    {
        "slug": "13-particle-kok-in-action",
        "title": "【二重言語】口語助詞「kok」の心理：驚き、不審、「どうして？」の感情表出",
        "intro": "文頭に置く「Kok... ?」は「えっ、どうして？なんで？（驚き・不審）」を表し、文末の「... kok」は「大丈夫だよ、本当に〜だから（安心・弁明）」を表します。置く位置によって役割がダイナミックに変わる口語の最重要ワードです。",
        "pairs": [
            ("Mengapa Anda belum tidur?", "Kok belom tidur sih?", "文頭kok: えっ、なんでまだ寝てないの？（驚き・疑問）"),
            ("Saya tidak apa-apa, jangan khawatir.", "Nggak apa-apa kok, santai aja.", "文末kok: 大丈夫だよ、心配いらないから（安心させる）"),
            ("Mengapa harganya bisa semahal ini?", "Kok mahal banget ya?", "文頭kok: なんでこんなに高いの？（不満・不審）"),
            ("Saya sungguh-sungguh tidak tahu.", "Beneran nggak tahu kok.", "文末kok: 本当に知らないんだってば（弁明）")
        ],
        "drill": [
            ("【Baku→Gaul】えっ、なんで泣いてるの？（Mengapa Anda menangis?）", "Kok nangis sih?", "コッ ナンギス スィ", "驚き疑問 Kok nangis sih?。"),
            ("【Gaul→Baku】痛くないよ、平気。（Nggak sakit kok, tenang aja.）", "Jangan khawatir, ini sama sekali tidak terasa sakit.", "ジャンガン クワティル、イニ サマ スカリ ティダッ トゥラサ サキッ", "安心弁明 Nggak sakit kok。"),
            ("【Baku→Gaul】どうして彼がここにいるの？（Mengapa dia berada di sini?）", "Kok dia ada di sini sih?", "コッ ディア アダ ディ スィニ スィ", "意外・不審 Kok dia ada di sini。"),
            ("【Gaul→Baku】怒ってないよ！（Nggak marah kok gue!）", "Saya sungguh-sungguh tidak merasa marah.", "サヤ スングスング ティダッ ムラサ マラ", "弁明 Nggak marah kok。"),
            ("【Baku→Gaul】えっ、もう帰るの？（Apakah Anda sudah mau pulang?）", "Kok udah mau balik aja?", "コッ ウダ マウ バリッ アジャ", "意外な早さ Kok udah mau balik。"),
            ("【Gaul→Baku】美味しかったよ！（Enak kok makanannya!）", "Masakan tersebut sungguh terasa enak.", "マサカン トゥルスブット スング トゥラサ エナッ", "念押し肯定 Enak kok。"),
            ("【Baku→Gaul】どうして誰もいないの？（Mengapa tidak ada orang?）", "Kok sepi banget, nggak ada orang?", "コッ スピ バンゲット、ンガッ アダ オラン", "不審 Kok sepi。"),
            ("【Gaul→Baku】私が壊したんじゃないよ。（Bukan gue yang ngerusakin kok.）", "Bukan saya yang menyebabkan kerusakan tersebut.", "ブカン サヤ ヤン ムニェバブカン クルサカン トゥルスブット", "潔白主張 Bukan... kok。"),
            ("【Baku→Gaul】なんでそんなこと知ってるの？（Bagaimana bisa tahu?）", "Kok lu bisa tahu sih?", "コッ ル ビサ タフ スィ", "驚き Kok lu bisa tahu。"),
            ("【Gaul→Baku】難しくないよ、簡単。（Gampang kok, nggak susah.）", "Hal ini tidak sulit dan sangat mudah dikerjakan.", "ハル イニ ティダッ スリット ダン サンガット ムダ ディクルジャカン", "励まし Gampang kok。"),
            ("【Baku→Gaul】急に電気が消えた、なんで？（Mengapa lampu padam tiba-tiba?）", "Kok mati lampu tiba-tiba?", "コッ マティ ランプ ティバティバ", "突発事態 Kok mati lampu。"),
            ("【Gaul→Baku】すぐ戻るからね。（Cuma bentar kok, ntar balik lagi.）", "Saya hanya pergi sebentar dan akan segera kembali.", "サヤ ハニャ プルギ スブンタル ダン アカン スグラ クンバリ", "約束 Cuma bentar kok。"),
            ("【Baku→Gaul】どうしてパソコンが動かないの？（Mengapa komputernya macet?）", "Kok komputernya hang ya?", "コッ コンピュテルニャ ハング ヤ", "機械異常 Kok macet。"),
            ("【Gaul→Baku】私、嘘ついてないよ。（Gue nggak bohong kok suwer.）", "Saya bersumpah bahwa saya tidak berbohong.", "サヤ ブルスンパ バワ サヤ ティダッ ブルボホン", "誓い Nggak bohong kok。"),
            ("【Baku→Gaul】えっ、もうこんな時間？（Mengapa waktu cepat sekali berlalu?）", "Kok udah jam segini aja sih?", "コッ ウダ ジャム スギニ アジャ スィ", "時間の早さ Kok udah jam segini。")
        ],
        "quiz": [
            ("相手を安心させて「大丈夫だよ、心配しないで」と言う時の文末詞は？", ["Nggak apa-apa kok.", "Nggak apa-apa dong.", "Nggak apa-apa deh.", "Nggak apa-apa sih."], 1),
            ("思いがけない出来事に「えっ、なんで？（どうしてそんなことが？）」と驚く文頭詞は？", ["Kok bisa?!", "Bisa dong?!", "Bisa deh?!", "Bisa kan?!"], 1),
            ("文頭の「Kok...」と文末の「...kok」の機能差として正しいものは？", ["文頭は「驚き・疑問」、文末は「安心・弁明・念押し」", "文頭は「命令」、文末は「過去形」", "文頭は「禁止」、文末は「願望」", "どちらも全く同じ意味"], 1)
        ]
    },
    {
        "slug": "14-particle-kan-in-action",
        "title": "【二重言語】確認詞「kan」の説得術：「〜でしょ？」「ほらね！」の同意と共感形成",
        "intro": "「kan」は bukan の短縮形から発展した確認詞です。「君も知ってるでしょ？（付加疑問）」「ほら、言った通りでしょ！（ほらね）」と、相手との共通認識を確認し、会話の同調・共感を瞬時に生み出す最強のコミュニケーションツールです。",
        "pairs": [
            ("Anda juga sudah tahu, bukan?", "Lu juga udah tahu kan?", "確認（君も知ってるでしょ？）"),
            ("Bukankah saya sudah memberitahu Anda?", "Tuh kan, gue bilang juga apa!", "ほらね（ほら見たことか！）"),
            ("Hari ini hari Minggu, bukan?", "Sekarang hari Minggu kan ya?", "曜日確認（今日日曜日だよね？）"),
            ("Dia orang yang sangat baik.", "Dia baik banget kan orangnya.", "共感の同意（あの人すごく良い人だよね）")
        ],
        "drill": [
            ("【Baku→Gaul】明日来るよね？（Anda akan datang besok, bukan?）", "Besok dateng kan?", "ブソッ ダテン カン", "予定確認 Besok dateng kan?。"),
            ("【Gaul→Baku】ほらね、私の言った通り！（Tuh kan, bener kata gue!）", "Bukankah apa yang saya katakan terbukti benar?", "ブカンカ アパ ヤン サヤ カタカン トゥルブクティ ブナル", "ほら見たことか Tuh kan。"),
            ("【Baku→Gaul】バリ島って綺麗だよね。（Bali itu sangat indah, bukan?）", "Bali indah banget kan ya.", "バリ インダ バンゲット カン ヤ", "共感求め indah kan ya。"),
            ("【Gaul→Baku】君も映画好きでしょ？（Lu suka nonton film juga kan?）", "Bukankah Anda juga gemar menonton film?", "ブカンカ アンダ ジュガ グマル メノントン フィルム", "好み確認 suka kan。"),
            ("【Baku→Gaul】昨日私に電話したよね？（Anda menelepon saya kemarin, bukan?）", "Kemaren lu nelpon gue kan?", "クマリン ル ネルポン グエ カン", "事実確認 nelpon kan。"),
            ("【Gaul→Baku】私たちは仲間だろ！（Kita kan temen baik!）", "Bukankah kita adalah sahabat karib?", "ブカンカ キタ アダラ サハバット カリッブ", "仲間確認 Kita kan...。"),
            ("【Baku→Gaul】辛いもの食べられるよね？（Anda bisa makan makanan pedas, bukan?）", "Bisa makan pedes kan lu?", "ビサ マカン プデス カン ル", "能力確認 bisa kan。"),
            ("【Gaul→Baku】ほら、雨が降ってきた！（Tuh kan, ujan beneran!）", "Lihatlah, hujan sungguh-sungguh mulai turun.", "リハトラ、フジャン スングスング ムライ トゥルン", "的中 Tuh kan, ujan beneran。"),
            ("【Baku→Gaul】彼はまだ学生ですよね？（Dia masih mahasiswa, bukan?）", "Dia masih kuliah kan ya?", "ディア マシ クリア カン ヤ", "身分確認 masih kuliah kan。"),
            ("【Gaul→Baku】チケットはもう買ったんだよね？（Tiketnya udah dibeli kan?）", "Tiketnya sudah dibeli, bukan?", "ティケットニャ スダ ディブリ、ブカン", "完了確認 udah dibeli kan。"),
            ("【Baku→Gaul】約束守ってくれるよね？（Anda akan menepati janji, bukan?）", "Janji ya, ditepati kan?", "ジャンジ ヤ、ディトゥパティ カン", "念押し ditepati kan。"),
            ("【Gaul→Baku】だって彼がそう言ったんだもん。（Kan dia yang ngomong gitu tadi.）", "Bukankah beliau sendiri yang menyatakannya tadi?", "ブカンカ ベリアウ スンディリ ヤン ムニャタカンニャ タディ", "理由提示 Kan dia...。"),
            ("【Baku→Gaul】この服、似合ってるでしょ？（Pakaian ini cocok untuk saya, bukan?）", "Cocok kan baju ini di gue?", "チョチョッ カン バジュ イニ ディ グエ", "似合ってるでしょ Cocok kan。"),
            ("【Gaul→Baku】ほらね、忘れたでしょ！（Tuh kan, ketinggalan lagi dompetnya!）", "Lihatlah, dompet Anda tertinggal lagi.", "リハトラ、ドンペット アンダ トゥルティンガル ラギ", "ほら見たことか Tuh kan。"),
            ("【Baku→Gaul】前にも会ったことあるよね？（Kita pernah bertemu sebelumnya, bukan?）", "Pernah ketemu sebelumnya kan ya?", "プルナ クトゥム スブルムニャ カン ヤ", "既視感確認 pernah ketemu kan。")
        ],
        "quiz": [
            ("予想が的中した時に「ほらね、言った通りでしょ！」と言う定番スラングは？", ["Tuh kan!", "Iya sih!", "Bisa dong!", "Bukan deh!"], 1),
            ("文末に「kan?」を添える主要な役割は？", ["相手への確認・同調・共感を求める（〜でしょ？）", "強い命令を下す", "過去形にする", "敬語にする"], 1),
            ("「Kan gue udah bilang tadi（だってさっき言ったじゃん）」の文頭 kan の働きは？", ["既知の前提や理由の提示", "未来の推量", "謝罪の言葉", "場所の指定"], 1)
        ]
    },
    {
        "slug": "15-particle-lho-in-action",
        "title": "【二重言語】感嘆詞「lho」の驚きと告知：「あれっ？」「〜なんだよ！」のニュアンス",
        "intro": "「lho（ロ）」は、文頭では「あれっ？おや？（意外・驚き）」、文末では「〜なんだよ！知ってた？（新情報の提供・注意喚起）」を表します。相手がまだ知らない情報を生き生きと伝えたり、思いがけない発見を口にする時の必須表現です。",
        "pairs": [
            ("Lho, mengapa Anda ada di sini?", "Lho, kok lu ada di sini?", "文頭lho: えっ、あれっ？お前なんでここにいるの？"),
            ("Dia sudah menikah, tahukah Anda?", "Dia udah nikah lho!", "文末lho: 彼、もう結婚したんだよ！（新情報の提供）"),
            ("Lho, di mana kacamata saya?", "Lho, kacamata gue mana ya?", "文頭lho: あれっ？メガネどこ置いたっけ？"),
            ("Harganya sangat murah sekali.", "Murah banget lho ini!", "文末lho: これ、すごく安いんだよ！（おすすめ・告知）")
        ],
        "drill": [
            ("【Baku→Gaul】あれっ、鍵がない！（Lho, di mana kuncinya?）", "Lho, kuncinya kok nggak ada?", "ロ、クンチニャ コッ ンガッ アダ", "文頭の驚き Lho, kok...。"),
            ("【Gaul→Baku】彼、日本語話せるんだよ！（Dia bisa bahasa Jepang lho!）", "Tahukah Anda bahwa beliau fasih berbahasa Jepang?", "タフカ アンダ バワ ベリアウ ファスィ ブルバハサ ジュパン", "新情報提供 bisa bahasa Jepang lho。"),
            ("【Baku→Gaul】あれっ、もう雨が降ってきた。（Lho, hujan sudah turun.）", "Lho, udah mulai gerimis nih.", "ロ、ウダ ムライ グリミス ニ", "意外な降雨 Lho, udah mulai...。"),
            ("【Gaul→Baku】これ、限定品なんだよ！（Ini barang langka lho!）", "Barang ini sangat langka dan diproduksi terbatas.", "バラン イニ サンガット ランカ ダン ディプロドゥクスィ トゥルバタス", "アピール barang langka lho。"),
            ("【Baku→Gaul】あれっ、誰も電話に出ない。（Lho, tidak ada yang mengangkat telepon.）", "Lho, kok nggak diangkat telponnya?", "ロ、コッ ンガッ ディアンカット テルポンニャ", "不審 Lho, kok nggak diangkat。"),
            ("【Gaul→Baku】あの店、今日閉まってるよ！（Tokonya tutup lho hari ini!）", "Pemberitahuan bahwa toko tersebut tutup hari ini.", "プムブリタフアン バワ トコ トゥルスブット トゥトゥップ ハリ イニ", "情報提供 tutup lho。"),
            ("【Baku→Gaul】あれっ、財布を忘れた！（Lho, dompet saya ketinggalan!）", "Lho, dompet gue ketinggalan!", "ロ、ドンペット グエ クティンガラン", "気づき Lho, dompet ketinggalan。"),
            ("【Gaul→Baku】私、本気で言ってるんだよ！（Gue serius lho ini!）", "Saya sungguh-sungguh tidak sedang bergurau.", "サヤ スングスング ティダッ スダン ブルグラウ", "真剣さアピール serius lho。"),
            ("【Baku→Gaul】あれっ、昨日言ったよね？（Lho, kemarin sudah saya sampaikan.）", "Lho, kemaren kan udah gue bilang.", "ロ、クマリン カン ウダ グエ ビラン", "Lho と kan のコンボ。"),
            ("【Gaul→Baku】あそこ、美味しいよ！（Enak banget lho makanannya di situ!）", "Makanan di tempat tersebut sangat lezat rasanya.", "マカナン ディ トゥムパット トゥルスブット サンガット ルザット ラサニャ", "おすすめ Enak banget lho。"),
            ("【Baku→Gaul】あれっ、どうしてまだここにいるの？（Lho, mengapa masih di sini?）", "Lho, kok masih nongkrong di sini?", "ロ、コッ マシ ノンクロン ディ スィニ", "意外滞在 Lho, kok masih...。"),
            ("【Gaul→Baku】明日、祝日だよ！（Besok libur lho!）", "Besok adalah hari libur nasional.", "ブソッ アダラ ハリ リブル ナスィオナル", "告知 Besok libur lho。"),
            ("【Baku→Gaul】あれっ、パソコンがフリーズした。（Lho, layarnya mati.）", "Lho, kok mati layarnya?", "ロ、コッ マティ ラヤールニャ", "突発故障 Lho, kok mati。"),
            ("【Gaul→Baku】油断すると危ないよ！（Bisa bahaya lho kalo teledor!）", "Dapat berakibat fatal jika Anda bersikap ceroboh.", "ダパット ブルアキバット ファタル ジカ アンダ ブルスィカップ チュロボ", "注意喚起 bahaya lho。"),
            ("【Baku→Gaul】あれっ、服が汚れてるよ。（Lho, pakaian Anda kotor.）", "Lho, bajunya kotor tuh kena saos.", "ロ、バジュニャ コトール トゥ クナ サオス", "指摘 Lho, bajunya kotor tuh。")
        ],
        "quiz": [
            ("相手がまだ知らない情報を「〜なんだよ！（知ってた？）」と伝える文末詞は？", ["...lho!", "...kan?", "...dong!", "...deh!"], 1),
            ("思いがけない事態に「あれっ？おや？」と声を漏らす文頭の感嘆詞は？", ["Lho...", "Kan...", "Sih...", "Deh..."], 1),
            ("「Lho, kok lu ada di sini?」の全体の意味は？", ["「あれっ、なんでお前がここにいるの？（驚き・意外）」", "「ここへ入ってはいけません」", "「あそこに誰がいますか？」", "「明日ここへ来てください」"], 1)
        ]
    },
    {
        "slug": "16-particle-ya-in-action",
        "title": "【二重言語】万能の終助詞「ya」のトーン調節：命令の軟化、確認、親密さの演出",
        "intro": "文末の「ya（ヤ）」は、日本語の「〜ね」「〜よね」に最も近い万能の終助詞です。硬い命令文を温かい依頼に変えたり（Tolong ya）、同意を求めたり、親しみを込めて別れを告げたりと、コミュニケーションの潤滑油として機能します。",
        "pairs": [
            ("Tolong tutup pintunya.", "Tolong tutup pintunya ya.", "命令の軟化（ドアを閉めてくださいね）"),
            ("Jangan lupa besok ada rapat.", "Jangan lupa besok ya.", "念押し（明日忘れないでね）"),
            ("Terima kasih banyak.", "Makasih ya!", "親密な感謝（ありがとね！）"),
            ("Sampai jumpa lagi besok.", "Dah, sampai ketemu besok ya!", "温かい別れ（じゃあ明日ね！）")
        ],
        "drill": [
            ("【Baku→Gaul】ありがとね！（Terima kasih ya.）", "Makasih banyak ya!", "マカスィ バニャッ ヤ", "感謝 Makasih ya。"),
            ("【Gaul→Baku】待っててね！（Tunggu bentar ya!）", "Mohon bersedia menunggu sebentar.", "モホン ブルスディア ムヌング スブンタル", "依頼 Tunggu ya。"),
            ("【Baku→Gaul】明日、遅刻しないでね。（Jangan terlambat besok.）", "Besok jangan telat ya.", "ブソッ ジャンガン トゥラット ヤ", "念押し jangan telat ya。"),
            ("【Gaul→Baku】また明日ね！（Sampai ketemu besok ya!）", "Sampai berjumpa kembali besok hari.", "サンパイ ブルジュンパ クンバリ ブソッ ハリ", "別れの挨拶 besok ya。"),
            ("【Baku→Gaul】気を付けて帰ってね。（Hati-hatilah di jalan.）", "Hati-hati di jalan ya.", "ハティハティ ディ ジャラン ヤ", "気遣い Hati-hati ya。"),
            ("【Gaul→Baku】手伝ってね！（Bantuin gue ya!）", "Tolong berikan bantuan kepada saya.", "トロン ブリカン バントゥアン クパダ サヤ", "依頼 Bantuin ya。"),
            ("【Baku→Gaul】後で電話するね。（Nanti saya telepon lagi.）", "Ntar gue telpon lagi ya.", "エンタール グエ テルポン ラギ ヤ", "約束 telpon lagi ya。"),
            ("【Gaul→Baku】ごめんね、うっかりしてた。（Maaf ya, khilaf gue.）", "Saya mohon maaf atas kelalaian saya.", "サヤ モホン マアフ アタス クラライアン サヤ", "軽い謝罪 Maaf ya。"),
            ("【Baku→Gaul】これ、美味しいね！（Ini sangat lezat.）", "Enak banget ya makanannya.", "エナッ バンゲット ヤ マカナンニャ", "共感 Enak ya。"),
            ("【Gaul→Baku】忘れないでね。（Ingetin gue ya ntar!）", "Tolong ingatkan saya nanti.", "トロン インガットカン サヤ ナンティ", "依頼 Ingetin ya。"),
            ("【Baku→Gaul】体に気を付けてね。（Jagalah kesehatan Anda.）", "Jaga kesehatan baik-baik ya.", "ジャガ クセハタン バイッバイッ ヤ", "健康気遣い Jaga kesehatan ya。"),
            ("【Gaul→Baku】ゆっくり休んでね。（Istirahat yang cukup ya.）", "Selamat beristirahat dengan tenang.", "スラマット ブルイスティラハット ドゥンガン トゥナン", "ねぎらい Istirahat ya。"),
            ("【Baku→Gaul】塩を取ってくれる？（Ambilkan garam.）", "Tolong ambilin garam ya.", "トロン アンビリン ガラム ヤ", "食卓の依頼 ambilin ya。"),
            ("【Gaul→Baku】そうだよね！（Iya ya, bener banget!）", "Tepat sekali seperti apa yang Anda katakan.", "トゥパット スカリ スペルティ アパ ヤン アンダ カタカン", "共感同意 Iya ya。"),
            ("【Baku→Gaul】じゃあ、またね！（Selamat tinggal.）", "Yuk duluan ya!", "ユッ ドゥルアン ヤ", "親密な退出 Duluan ya。")
        ],
        "quiz": [
            ("命令文「Tolong tutup pintunya」の末尾に「ya」を添える効果は？", ["命令調を和らげ、親しみのある丁寧な依頼にする（〜してね）", "強い威圧感を与える", "過去の出来事にする", "文を名詞化する"], 1),
            ("友人に「ありがとね！」とフランクに感謝を伝える定番フレーズは？", ["Makasih ya!", "Saya ucapkan terima kasih.", "Terima kasih banyak sekali.", "Hormat saya."], 1),
            ("会話の終わりに「じゃあ先に失礼するね！」と温かく告げる言葉は？", ["Duluan ya!", "Saya pulang sekarang.", "Tinggalkan saya.", "Kembali saya."], 1)
        ]
    },
    {
        "slug": "17-particle-combination",
        "title": "【二重言語】助詞の連続技：dong ya, sih sebenernya, kan ya, deh kayaknya の複合感覚",
        "intro": "インドネシア語の達人は、単体の助詞だけでなく「dong ya」「kan ya」「deh kayaknya」「sih sebenernya」と助詞を巧みに組み合わせて、極めて立体的で微妙なニュアンスを表現します。この助詞コンビネーションを解剖します。",
        "pairs": [
            ("Tentu saja Anda mengerti.", "Ngerti dong ya!", "当然わかってるよね！（dong + ya）"),
            ("Sebenarnya saya ingin membantu.", "Pengen bantu sih sebenernya.", "本音の留保（実は〜なんだけどね）"),
            ("Bukankah demikian keadaannya?", "Iya kan ya?", "強い同調確認（だよね〜？ kan + ya）"),
            ("Sepertinya lebih baik kita pergi.", "Cabut aja deh kayaknya.", "控えめな決断（もう行った方がいいかもね）")
        ],
        "drill": [
            ("【Baku→Gaul】もちろん知ってるよね！（Tentu saja Anda tahu.）", "Tahu dong ya pastinya!", "タフ ドン ヤ パスティニャ", "当然確認 dong ya。"),
            ("【Gaul→Baku】実はちょっと行きたくないんだ。（Males pergi sih sebenernya.）", "Sejujurnya saya merasa enggan untuk pergi.", "スジュジュルニャ サヤ ムラサ エンガン ウントゥッ プルギ", "本音の留保 sih sebenernya。"),
            ("【Baku→Gaul】これで合ってるよね？（Ini sudah benar, bukan?）", "Bener kan ya caranya gini?", "ブネル カン ヤ チャラニャ ギニ", "同調確認 kan ya。"),
            ("【Gaul→Baku】もう帰った方がいいかも。（Mending balik aja deh kayaknya.）", "Sepertinya lebih baik saya segera pulang.", "スペルティニャ レビ バイッ サヤ スグラ プラン", "控えめな決断 deh kayaknya。"),
            ("【Baku→Gaul】手伝ってくれるよね？（Anda mau membantu saya, bukan?）", "Bisa bantuin dong ya?", "ビサ バントゥイン ドン ヤ", "親密な念押し dong ya。"),
            ("【Gaul→Baku】美味しかったけど高かったね。（Enak sih sebenernya, tapi mahal.）", "Makanannya memang lezat, akan tetapi harganya mahal.", "マカナンニャ メマン ルザット、アカン トゥタピ ハルガニャ マハル", "評価の留保 sih sebenernya。"),
            ("【Baku→Gaul】彼、来るよね？（Dia akan datang, bukan?）", "Dia dateng kan ya ntar?", "ディア ダテン カン ヤ エンタール", "予定確認 kan ya。"),
            ("【Gaul→Baku】明日にした方がいいかも。（Besok aja deh kayaknya ya.）", "Sepertinya lebih bijak jika ditunda hingga besok.", "スペルティニャ レビ ビジャッ ジカ ディトゥンダ ヒンガ ブソッ", "提案 deh kayaknya。"),
            ("【Baku→Gaul】笑顔でいてね！（Tetaplah tersenyum ya.）", "Senyum dong ya biar manis!", "スニュム ドン ヤ ビアル マニス", "促し dong ya。"),
            ("【Gaul→Baku】本当は知ってたんだ。（Udah tahu sih sebenernya dari awal.）", "Sejujurnya sejak awal saya telah mengetahuinya.", "スジュジュルニャ スジャッ アワル サヤ トゥラ ムンゲタフイニャ", "告白 sih sebenernya。"),
            ("【Baku→Gaul】かっこいいよね？（Tampak sangat keren, bukan?）", "Keren banget kan ya outfit-nya?", "クレン バンゲット カン ヤ アウトフィットニャ", "共感 kan ya。"),
            ("【Gaul→Baku】買わないでおくよ。（Nggak usah beli deh kayaknya.）", "Tampaknya saya memutuskan untuk tidak membelinya.", "タンパッニャ サヤ ムムトゥスカン ウントゥッ ティダッ ムンブリニャ", "見送り deh kayaknya。"),
            ("【Baku→Gaul】許してくれるよね？（Anda memaafkan saya, bukan?）", "Maafin dong ya, jangan ngambek.", "マアフィン ドン ヤ、ジャンガン ンガンベック", "甘え懇願 dong ya。"),
            ("【Gaul→Baku】言いたいことは分かるけどね。（Paham sih sebenernya maksud lu.）", "Sejujurnya saya memahami apa maksud perkataan Anda.", "スジュジュルニャ サヤ メマハミ アパ マクスッド プルカタアン アンダ", "理解の留保 sih sebenernya。"),
            ("【Baku→Gaul】楽しかったよね！（Sangat menyenangkan, bukan?）", "Seru banget kan ya acaranya?", "スル バンゲット カン ヤ アチャラニャ", "思い出共感 kan ya。")
        ],
        "quiz": [
            ("「当然知ってるでしょ〜？」と親しみと確信を込めて念押しする助詞コンビは？", ["dong ya", "sih kan", "deh kok", "lho ya"], 1),
            ("「本音を言えば〜なんだけどね」と控えめに前置きする語順は？", ["...sih sebenernya", "...dong ya", "...kan lho", "...deh kok"], 1),
            ("「もうやめておいた方がいいかもね」と柔らかく決断する表現は？", ["Nggak usah aja deh kayaknya.", "Jangan dong ya pastinya.", "Mesti kok sih.", "Harus kan ya."], 1)
        ]
    },
    {
        "slug": "18-wa-chat-abbreviations-01",
        "title": "【二重言語】WhatsAppチャット略語辞典①：子音短縮形（yg, bgt, tdk, dpt, spy, kpd, bsk）",
        "intro": "インドネシア人の WhatsApp や SNS チャット画面を見ると、母音が極端に省略された暗号のような略語が飛び交っています。これはテキスト入力の高速化から生まれた文化的書法です。頻出の子音短縮形を完璧に解読できるようにします。",
        "pairs": [
            ("yang (関係詞)", "yg", "最も頻出の関係詞短縮形"),
            ("banget (とても)", "bgt", "強調詞 banget の子音短縮"),
            ("tidak (ない)", "tdk / g / gak", "否定詞のチャット表記"),
            ("besok (明日)", "bsk", "時間表現のチャット略語")
        ],
        "drill": [
            ("【Baku→Chat】とても美味しいです。（Enak banget.）", "Enak bgt.", "エナッ バンゲット", "banget ⇄ bgt。"),
            ("【Chat→Baku】明日の会議。（Rapat bsk ya.）", "Rapat besok hari ya.", "ラパット ブソッ ハリ ヤ", "bsk ⇄ besok。"),
            ("【Baku→Chat】購入した商品。（Barang yang dibeli.）", "Brg yg dibeli.", "バラン ヤン ディブリ", "barang ⇄ brg, yang ⇄ yg。"),
            ("【Chat→Baku】参加できません。（Tdk bs hadir.）", "Tidak bisa hadir.", "ティダッ ビサ ハディル", "tdk ⇄ tidak, bs ⇄ bisa。"),
            ("【Baku→Chat】理解できるように。（Supaya bisa paham.）", "Spy bs paham.", "スパヤ ビサ パハム", "supaya ⇄ spy。"),
            ("【Chat→Baku】すでに受領しました。（Sdh dpt info.）", "Sudah dapat informasi.", "スダ ダパット インフォルマスィ", "sdh ⇄ sudah, dpt ⇄ dapat。"),
            ("【Baku→Chat】社長宛ての手紙。（Surat kepada direktur.）", "Srt kpd direktur.", "スラット クパダ ディレクトゥル", "surat ⇄ srt, kepada ⇄ kpd。"),
            ("【Chat→Baku】どこにいますか？（Lg dmn skrg?）", "Sedang di mana sekarang?", "スダン ディ マナ スカラン", "lg ⇄ lagi/sedang, dmn ⇄ di mana, skrg ⇄ sekarang。"),
            ("【Baku→Chat】ちょっと待ってください。（Tunggu sebentar ya.）", "Tggu bntr ya.", "トゥング ブンタル ヤ", "tunggu ⇄ tggu, sebentar ⇄ bntr。"),
            ("【Chat→Baku】昨夜の件。（Mslh tmn smlm.）", "Masalah teman semalam.", "マサラ トゥマン スマラム", "mslh ⇄ masalah, tmn ⇄ teman, smlm ⇄ semalam。"),
            ("【Baku→Chat】何時ですか？（Jam berapa sekarang?）", "Jm brp skrg?", "ジャム ブラパ スカラン", "jam ⇄ jm, berapa ⇄ brp。"),
            ("【Chat→Baku】ありがとう！（Mksih bnyk ya.）", "Terima kasih banyak ya.", "トゥリマ カスィ バニャッ ヤ", "mksih ⇄ terima kasih, bnyk ⇄ banyak。"),
            ("【Baku→Chat】家に着きました。（Sudah sampai rumah.）", "Sdh smpe rmh.", "スダ サンパイ ルマ", "sampai ⇄ smpe, rumah ⇄ rmh。"),
            ("【Chat→Baku】元気ですか？（Gmn kbrnya?）", "Bagaimana kabarnya?", "バガイマナ カバルニャ", "gmn ⇄ gimana, kbrnya ⇄ kabarnya。"),
            ("【Baku→Chat】まだオフィスにいます。（Masih di kantor.）", "Msh di ktr.", "マシ ディ カントール", "masih ⇄ msh, kantor ⇄ ktr。")
        ],
        "quiz": [
            ("チャットで「yg bgt」と書かれていた場合の元の標準語は？", ["yang banget (とても〜な)", "yang bagi", "yang bagus", "yang begitu"], 1),
            ("「bsk jm brp?」というメッセージの解読として正しいのは？", ["Besok jam berapa? (明日何時？)", "Bisa jam berapa?", "Besok jalan berapa?", "Biasa jam berapa?"], 1),
            ("否定の「tidak」をチャットで最も短く表記する記号は？", ["tdk / gak / g", "td", "tk", "ti"], 1)
        ]
    },
    {
        "slug": "19-wa-chat-abbreviations-02",
        "title": "【二重言語】WhatsAppチャット略語辞典②：アクロニムと笑い（otw, gpp, wkwk, mager, baper）",
        "intro": "チャットやSNSで頻出するアクロニム（頭文字語）や若者スラングは、インドネシアのデジタル文化の象徴です。「gpp（大丈夫）」「wkwk（草・笑）」「mager（面倒くさい）」「baper（傷つきやすい）」など、ネイティブチャットの必須スラングを完全解剖します。",
        "pairs": [
            ("gpp", "nggak apa-apa", "大丈夫、何でもない（no problem）"),
            ("wkwk / wkwkwk", "tertawa / tertawa ngakak", "ネットの笑い（日本語の「www」「草」）"),
            ("mager", "malas gerak", "動くのが面倒くさい・ダラダラしたい"),
            ("baper", "bawa perasaan", "感情的になりすぎる・真に受ける")
        ],
        "drill": [
            ("【Baku→Chat】問題ありませんよ。（Tidak ada masalah sama sekali.）", "gpp santai aja.", "ガパパ サンタイ アジャ", "nggak apa-apa ⇄ gpp。"),
            ("【Chat→Baku】大爆笑！（Lucu bgt wkwkwk!）", "Hal itu sangat lucu sekali hingga membuat tertawa terbahak-bahak.", "ハル イトゥ サンガット ルチュ スカリ ヒンガ ムンブアット トゥルタワ トゥルバハッバハッ", "wkwkwk = 笑い。"),
            ("【Baku→Chat】外出するのが面倒くさい。（Malas bergerak untuk keluar.）", "Lagi mager bgt nih.", "ラギ マゲル バンゲット ニ", "malas gerak ⇄ mager。"),
            ("【Chat→Baku】真に受けないでよ。（Jangan baper dong, cuma bercanda.）", "Jangan memasukkan perkataan ini ke dalam hati, saya hanya bergurau.", "ジャンガン ムマスッカン プルカタアン イニ ク ダラム ハティ、サヤ ハニャ ブルグラウ", "bawa perasaan ⇄ baper。"),
            ("【Baku→Chat】今向かっています！（Sedang dalam perjalanan ke sana.）", "OTW bro!", "オーテーウェー ブロ", "on the way ⇄ OTW。"),
            ("【Chat→Baku】承認欲求が強い人。（Orang yang suka pansos di medsos.）", "Orang yang gemar panjat sosial demi popularitas.", "オラン ヤン グマル パンジャット ソスィアル デミ ポプラリタス", "panjat sosial ⇄ pansos。"),
            ("【Baku→Chat】嘘でしょ、本当？（Apakah itu sungguh-sungguh benar?）", "Asli nih? No debat!", "アスリ ニ、ノー デバット", "no debat = 異論なし・確定。"),
            ("【Chat→Baku】彼女、嫉妬してるよ。（Dia lagi bucin parah.）", "Dia sangat diperbudak oleh cinta.", "ディア サンガット ディプルブダッ オレ チンタ", "budak cinta ⇄ bucin（恋の奴隷）。"),
            ("【Baku→Chat】頭が痛い、モヤモヤする。（Merasa bingung dan pusing.）", "Lagi pusing / overthinking bgt.", "ラギ プシン / オーバーシンキング バンゲット", "overthinking = 考えすぎ。"),
            ("【Chat→Baku】適当にやろう。（Santai aja, sans bro.）", "Bersikaplah tenang dan rileks sejenak.", "ブルスィカップラ トゥナン ダン リレクス スブンタル", "sans = santai。"),
            ("【Baku→Chat】すごい、神がかっている！（Sangat hebat luar biasa!）", "Gokil abis!", "ゴキル アビス", "gokil = gila / keren。"),
            ("【Chat→Baku】あの人、偽善者だよ。（Dia itu pansos dan fake bgt.）", "Orang tersebut sangat berpura-pura dan mencari keuntungan.", "オラン トゥルスブット サンガット ブルプラプラ ダン マンチャリ クウントゥンガン", "fake = palsu。"),
            ("【Baku→Chat】ちょっと眠い。（Merasa agak mengantuk.）", "Ngantuk bgt, pen tidur.", "ナントゥッ バンゲット、ペン ティドゥール", "pen = pengen (ingin)。"),
            ("【Chat→Baku】マジで？信じられない！（Demi apa lu?!）", "Demi Tuhan, apakah hal itu benar terjadi?", "デミ トゥハン、アパカ ハル イトゥ ブナル トゥルジャディ", "Demi apa?! = マジで？！。"),
            ("【Baku→Chat】お疲れ様でした！（Terima kasih atas kerja kerasnya.）", "Mantap guys, tengkyu bgt!", "マンタップ ガイズ、テンキュー バンゲット", "tengkyu = thank you。")
        ],
        "quiz": [
            ("インドネシアのネットチャットで「www（笑）」に相当する表記は？", ["wkwk / wkwkwk", "hahaha saja", "lol saja", "5555"], 1),
            ("「面倒くさくて動きたくない（ダラダラしたい）」を意味する略語は？", ["mager (malas gerak)", "baper (bawa perasaan)", "pansos (panjat sosial)", "bucin (budak cinta)"], 1),
            ("チャットの「gpp」の元のフレーズは？", ["nggak apa-apa", "ganteng pisan pisan", "guru paling pintar", "gedung pusat polisi"], 1)
        ]
    },
    {
        "slug": "20-slang-syllable-inversion-prokem",
        "title": "【二重言語】ストリートスラング「プロケム（Prokem）音節反転法」（yuk → kuy, bisa → sabi）",
        "intro": "ジャカルタの若者言葉やストリートカルチャーには、単語の音節や文字を逆さまにして発音する「バハサ・プロケム（Bahasa Prokem / Bahasa Terbalik）」の伝統があります。yuk が kuy、bisa が sabi、balik が libab など、ルールを知ると一瞬で解読できます。",
        "pairs": [
            ("yuk (〜しよう)", "kuy", "音節反転（y-u-k → k-u-y）"),
            ("bisa (できる)", "sabi", "音節入替（bi-sa → sa-bi）"),
            ("balik (帰る)", "kibal / libab", "音節反転（ba-lik → kibal）"),
            ("suka (好き)", "kusa", "音節入替（su-ka → ku-sa）")
        ],
        "drill": [
            ("【Baku→Prokem】行こうぜ！（Ayo kita pergi!）", "Kuy jalan sekarang!", "クイ ジャラン スカラン", "yuk ⇄ kuy。"),
            ("【Prokem→Baku】俺、できるよ！（Gue sabi nih ngerjainnya!）", "Saya mampu menyelesaikan pekerjaan tersebut.", "サヤ マンプ ムニェレサイカン プクルジャアン トゥルスブット", "sabi ⇄ bisa。"),
            ("【Baku→Prokem】帰ろう！（Ayo kita pulang!）", "Kuy balik duluan!", "クイ バリッ ドゥルアン", "kuy balik。"),
            ("【Prokem→Baku】お茶しに行かない？（Ngopi kuy!）", "Mari kita pergi minum kopi bersama.", "マリ キタ プルギ ミヌム コピ ブルサマ", "ngopi kuy ⇄ minum kopi yuk。"),
            ("【Baku→Prokem】これ、いけるね！（Ini bisa dicoba.）", "Sabi lah ini dicoba!", "サビ ラ イニ ディチョバ", "sabi lah ⇄ bisa lah。"),
            ("【Prokem→Baku】映画見よう！（Nonton kuy!）", "Ayo kita menonton film bioskop.", "アヨ キタ メノントン フィルム ビオスコップ", "nonton kuy ⇄ ayo menonton。"),
            ("【Baku→Prokem】すごい！（Hebat sekali!）", "Pecah abis bro!", "プチャ アビス ブロ", "pecah = 爆発的・最高。"),
            ("【Prokem→Baku】これ、マジでいい！（Sabi bgt nih barang!）", "Barang ini sungguh sangat bagus kualitasnya.", "バラン イニ スング サンガット バグス クアリタスニャ", "sabi bgt ⇄ bagus sekali / bisa banget。"),
            ("【Baku→Prokem】昼ごはん食べに行こう！（Ayo makan siang.）", "Makan kuy, laper nih!", "マカン クイ、ラペル ニ", "makan kuy ⇄ ayo makan。"),
            ("【Prokem→Baku】今夜会える？（Ntar malem sabi ketemu?）", "Apakah kita bisa bertemu nanti malam?", "アパカ キタ ビサ ブルトゥム ナンティ マラム", "sabi ketemu ⇄ bisa bertemu。"),
            ("【Baku→Prokem】ちょっと休憩しよう！（Ayo istirahat sebentar.）", "Ngaso kuy bentaran!", "ンガソ クイ ブンタラン", "ngaso kuy ⇄ ayo istirahat。"),
            ("【Prokem→Baku】参加できる人！（Yang sabi ikut angkat tangan!）", "Siapa yang dapat ikut serta, silakan angkat tangan.", "スィアパ ヤン ダパット イクット スルタ、シラカン アンカット タンガン", "yang sabi ⇄ yang bisa。"),
            ("【Baku→Prokem】出発しよう！（Ayo kita berangkat.）", "Cabut kuy!", "チャブット クイ", "cabut kuy ⇄ ayo berangkat。"),
            ("【Prokem→Baku】この企画、いけるよ！（Sabi jalan nih rencana!）", "Rencana ini pasti bisa terlaksana dengan baik.", "レンチャナ イニ パスティ ビサ トゥルラクサナ ドゥンガン バイッ", "sabi jalan ⇄ bisa terlaksana。"),
            ("【Baku→Prokem】散歩しよう！（Ayo kita jalan-jalan.）", "Jalan kuy keliling kota!", "ジャラン クイ クリリン コタ", "jalan kuy ⇄ ayo jalan。")
        ],
        "quiz": [
            ("若者が「Kuy!」と声をかけてきた時、元の単語は何？", ["Yuk! (〜しよう！)", "Kue", "Kucing", "Kuda"], 1),
            ("「Sabi」というプロケムスラングが意味する単語は？", ["Bisa (できる・いける)", "Sapi", "Satu", "Sabtu"], 1),
            ("「Ngopi kuy!」の日本語の意味は？", ["「コーヒー飲みに行こうぜ！」", "「コーヒーをこぼした！」", "「コーヒーが苦い！」", "「コーヒーを買ってきて！」"], 1)
        ]
    }
]

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

print("Batch 1111-1120 generated successfully.")
