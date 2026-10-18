# -*- coding: utf-8 -*-
import os
import re

os.makedirs("docs/strategies", exist_ok=True)

articles_data = [
    {
        "slug": "11-restatement-paraphrase",
        "title": "【戦略会話】パラフレーズ再陳述：相手の言葉を別の易しい言葉で言い換えて確認する技術",
        "intro": "相手が使った難解な専門用語や慣用句を、自分の知っている平易な単語にパラフレーズ（Paraphrase）して「つまり〜ということですね？」と返す技術は、認識のズレを解消するだけでなく、相手に『この人は話を深く理解している』という絶大な安心感を与えます。",
        "pairs": [
            ("Dengan kata lain, maksudnya adalah...", "Maksudnya sama aja kayak...", "言い換え前置きの差"),
            ("Bisa diistilahkan secara sederhana sebagai...", "Gampangnya tuh kayak...", "平易化の差"),
            ("Apakah ini berarti bahwa...?", "Berarti ini intinya... kan ya?", "帰結確認の差"),
            ("Analoginya menyerupai...", "Mirip-mirip kayak...", "比喩化の差")
        ],
        "drill": [
            ("【ビジネス】別の言葉で言えば、初期投資の回収に3年要するということですね。（Dengan kata lain, BEP baru tercapai dalam tiga tahun?）", "Dengan kata lain, modal awal baru akan kembali utuh dalam kurun waktu tiga tahun, betul?", "ドゥンガン カタ ライン、モダル アワル バル アカン クンバリ ウトゥ ダラム クルン ワクトゥ ティガ タフン、ブトゥル", "ビジネスの言い換え確認。"),
            ("【日常会話】つまり、彼と別れたってこと？（Maksudnya lu udah putus sama dia?）", "Berarti intinya hubungan lu udah resmi berakhir kan, gak pacaran lagi?", "ブラルティ インティニャ フブンガン ル ウダ レスミ ブルアキール カン、ガッ パチャラン ラギ", "恋愛の平易な言い換え。"),
            ("【技術】要するに、アプリの処理速度が劇的に向上したということですね。（Gampangnya kecepatan aplikasinya meningkat drastis?）", "Gampangnya, aplikasi ini jadi jauh lebih enteng dan gak nge-lag lagi kan ya?", "ガンパンニャ、アプリカスィ イニ ジャディ ジャウ ルビ エンテング ダン ガッ ンゲラグ ラギ カン ヤ", "技術用語の平易化。"),
            ("【法律】法令に従わない場合、営業停止の制裁を受けるということでしょうか。（Apakah pelanggaran berakibat pada pembekuan izin usaha?）", "Apakah ini berarti toko kami dilarang beroperasi sementara jika tidak memenuhi syarat?", "アパカ イニ ブラルティ トコ カミ ディララン ブルオペラスィ スムンタラ ジカ ティダッ ムムヌヒ シャラット", "法意の噛み砕き。"),
            ("【人事】昇進に伴い、給与テーブルも改定されるという理解でよろしいですか。（Berarti ada penyesuaian skala gaji seiring promosi?）", "Artinya ada kenaikan gaji pokok yang menyertai tanggung jawab baru ini kan ya?", "アルティニャ アダ クナイカン ガジ ポコッ ヤン ムニェルタイ タングン ジャワブ バル イニ カン ヤ", "人事条件の言い換え。"),
            ("【物流】天候不良により、配達が明日以降にずれ込むということですね。（Pengiriman tertunda akibat cuaca buruk?）", "Maksudnya paket saya baru nyampe paling cepet lusa karena ombak gede di laut ya?", "マクスッドニャ パケット サヤ バル ニャンペ パリン チパット ルサ カレナ オンバッ グデ ディ ラウット ヤ", "物流遅延の確認。"),
            ("【医療】手術ではなく、投薬治療で様子を見るという方針ですね。（Pengobatan rawat jalan dengan obat, bukan operasi?）", "Berarti langkah medisnya cukup minum obat teratur tanpa perlu tindakan bedah ya dok?", "ブラルティ ランカ メディスニャ チュクップ ミヌム オバット トゥラトゥール タンパ プル ティンダカン ブダ ヤ ドッ", "治療方針の確認。"),
            ("【IT】パスワードを忘れたので再発行が必要ということですか？（Perlu reset kata sandi baru?）", "Tinggal bikin password baru lewat tautan email ini saja kan ya?", "ティンガル ビキン パスワード バル レワット タウタン イーメール イニ サジャ カン ヤ", "操作手順の言い換え。"),
            ("【観光】入場料にガイド代もすべて含まれているということですね。（Tiket sudah termasuk jasa pemandu wisata?）", "Harga tiket segini udah 'terima bersih' bareng tour guide-nya kan ya mas?", "ハルガ ティケット スギニ ウダ トゥリマ ブルスィ バレン ツアー ガイドニャ カン ヤ マス", "料金内訳の言い換え。"),
            ("【社内】企画書を一度白紙に戻して最初からやり直せということでしょうか。（Mulai dari nol lagi proposalnya?）", "Apakah arahan Bapak berarti kami harus merancang konsep baru dari titik awal?", "アパカ アラハン バパッ ブラルティ カミ ハルス ムランチャン コンセプ バル ダリ ティティッ アワル", "指示の深刻度確認。"),
            ("【相場】今売ると大損するから我慢して保持せよということですね。（Hold dulu jangan dijual sekarang?）", "Intinya jangan panik sell dulu, tahan asetnya sampe harganya rebound kan ya?", "インティニャ ジャンガン パニック セル ドゥル、タハン アセットニャ サンペ ハルガニャ リバウンド カン ヤ", "投資アドバイスの言い換え。"),
            ("【教育】出席日数が足りないと試験を受けられないということですか？（Kurang presensi tidak boleh ikut ujian?）", "Kalo bolos lebih dari tiga kali, otomatis gak dapet kartu ujian ya pak?", "カロ ボロス ルビ ダリ ティガ カリ、オトマティス ガッ ダペット カルトゥ ウジアン ヤ パッ", "単位条件の言い換え。"),
            ("【住宅】敷金と礼金は退去時に全額返還される性質のものですか？（Apakah uang jaminan dikembalikan penuh saat keluar?）", "Uang deposit ini bakal balik seratus persen kalo gak ada kerusakan kan ya?", "ウアン デポスィット イニ バカル バリッ スラトゥス パーセン カロ ガッ アダ クルサカン カン ヤ", "契約デポジットの確認。"),
            ("【飲食】このスープは豚骨ではなく鶏ガラベースということですね？（Kaldu ayam, bukan kaldu babi kan?）", "Kuahnya murni dari rebusan ayam kan ya mas, halal dan aman buat muslim?", "クアニャ ムルニ ダリ ルブサン アヤム カン ヤ マス、ハラル ダン アマン ブアット ムスリム", "食材ベースの確認。"),
            ("【総括】パラフレーズは知的な理解の証である。（Memparafrasakan adalah cermin kedewasaan intelektual.）", "Ubah kata rumit menjadi sederhana: Anda paham, lawan bicara pun tenang!", "ウバ カタ ルミット ムンジャディ スデルハナ：アンダ パハム、ラワン ビチャラ プン トゥナン", "パラフレーズの黄金則。")
        ],
        "quiz": [
            ("相手の話を「別の言葉で言えば、つまり〜ということですね？」と言い換える定番の接続句は？", ["Dengan kata lain... / Artinya...", "Meskipun demikian...", "Jangan lupa...", "Siapa yang datang..."], 1),
            ("難しい説明を「簡単に言えば、噛み砕くと〜だよ」とカジュアルに平易化する表現は？", ["Gampangnya tuh kayak...", "Susahnya setengah mati...", "Mahal sekali harganya...", "Jauh tempatnya..."], 1),
            ("相手の言葉をパラフレーズ（言い換え）して確認することの最大の心理的効果は？", ["相手に『自分の話を深く正確に理解してくれている』という安心感を与える", "相手を試して恥をかかせる", "会話の時間を引き延ばしてサボる", "相手の語彙力を批判する"], 1)
        ]
    },
    {
        "slug": "12-spelling-spelling-out",
        "title": "【戦略会話】アルファベット綴り確認：人名・地名・メールアドレスを1文字ずつ確実に伝える",
        "intro": "インドネシア語のアルファベット読み（A: アー, B: ベー, C: チェー, D: デー, E: エー, G: ゲー, H: ハー, J: ジェー, K: カー, P: ペー, Q: キー, V: フェー, W: ウェー, Y: イー・グラエック, Z: ゼット）は、英語と母音・子音の読み方が大きく異なります。名前やメールアドレスのスペルを1文字ずつ正確に聞き取り・伝達する技術を磨きます。",
        "pairs": [
            ("Boleh tolong dieja huruf demi huruf?", "Dieja dong satu-satu hurufnya!", "スペル確認要請の差"),
            ("Pakai huruf besar atau kecil?", "Huruf kapital apa bukan?", "大文字・小文字の確認"),
            ("Apakah menggunakan spasi atau tanda hubung?", "Pake strip apa spasi?", "記号・ハイフンの確認"),
            ("Huruf 'C' seperti pada kata 'Cinta'?", "'C' untuk 'Cacing' kan ya?", "フォネティック確認の差")
        ],
        "drill": [
            ("【ビジネス】お名前のアルファベットの綴りを1文字ずつ教えていただけますか？（Boleh tolong eja nama lengkapnya huruf demi huruf?）", "Boleh tolong dieja nama lengkap Bapak satu per satu hurufnya agar tidak keliru?", "ボレ トロン ディエジャ ナマ ルンカップ バパッ サトゥ プル サトゥ フルフニャ アガル ティダッ クリルー", "氏名スペルの公式確認。"),
            ("【日常会話】私の苗字はタカハシです。T-A-K-A-H-A-S-H-I です。（Nama saya Takahashi: T-A-K-A-H-A-S-H-I.）", "Nama keluarga saya Takahashi: Té - Ah - Kah - Ah - Hah - Ah - Es - Hah - I.", "ナマ クルアルガ サヤ タカハシ：テー - アー - カー - アー - ハー - アー - エス - ハー - イ", "日本姓の正確な発音伝達。"),
            ("【メール】メールアドレスのドットの後は「gmail.com」ですか？（Setelah tanda titik adalah 'gmail.com'?）", "Setelah tanda titik itu 'G-mail' kan ya? G-é - Em - Ah - I - El dot com?", "ストゥラ サンダ ティティッ イトゥ ジーメール カン ヤ？ ゲー - エム - アー - イ - エル ドット コム", "メアドの確認。"),
            ("【記号】アンダースコア（下線）ですか、それともハイフンですか？（Tanda garis bawah atau tanda hubung?）", "Pake garis bawah (underscore) atau strip tengah (hyphen) ya mas?", "パケ ガリス バワ（アンダースコア）アタウ ストリップ トゥンガ（ハイフン）ヤ マス", "記号の峻別。"),
            ("【大文字】すべて小文字でよろしいですか？（Semuanya menggunakan huruf kecil ya?）", "Semua hurufnya ditulis huruf kecil kan ya, gak ada yang kapital?", "スムア フルフニャ ディトゥリス フルフ クチル カン ヤ、ガッ アダ ヤン カピタル", "大小文字の確認。"),
            ("【似た文字】B（ベー）ですか、それともD（デー）ですか？（Huruf 'B' atau huruf 'D'?）", "Huruf 'B' untuk Bandung atau 'D' untuk Denpasar ya pak?", "フルフ 'ベー' ウントゥッ バンドン アタウ 'デー' ウントゥッ デンパサール ヤ パッ", "類似音の都市名照合。"),
            ("【似た文字】M（エム）ですか、それともN（エン）ですか？（Huruf 'M' atau huruf 'N'?）", "Huruf 'M' untuk Medan atau 'N' untuk Nabire?", "フルフ 'エム' ウントゥッ メダン アタウ 'エン' ウントゥッ ナビレ", "鼻音字母の照合。"),
            ("【似た文字】V（フェー）ですか、それともF（エフ）ですか？（Huruf 'V' atau huruf 'F'?）", "Pakai huruf 'V' untuk Victor atau 'F' untuk Fajar?", "パケ フルフ 'フェー' ウントゥッ ヴィクター アタウ 'エフ' ウントゥッ ファジャール", "VとFの混同防止。"),
            ("【重複文字】Oが2つ（ダブルO）連続します。（Huruf 'O' ganda berturut-turut.）", "Ada double 'O' ya: Bé - O - O - Kah, seperti pada kata 'Book'.", "アダ ダブル 'オー' ヤ：ベー - オー - オー - カー、スプルティ パダ カタ 'ブック'", "重文字の伝達。"),
            ("【数字と文字】数字のゼロですか、それともアルファベットのOですか？（Angka nol atau huruf 'O'?）", "Itu angka nol atau huruf 'O' kapital ya mas?", "イトゥ アンカ ノル アタウ フルフ 'オー' カピタル ヤ マス", "0とOの混同是正。"),
            ("【地名】スラバヤの綴りは S-U-R-A-B-A-Y-A です。（Ejaan Surabaya adalah S-U-R-A-B-A-Y-A.）", "Surabaya dieja: Es - U - Er - Ah - Bé - Ah - Yé - Ah.", "スロボヨ ディエジャ：エス - ウ - エル - アー - ベー - アー - イェー - アー", "地名のスペリング。"),
            ("【数字と文字】数字の1ですか、小文字のLですか、それとも大文字のIですか？（Angka 1, huruf 'l', atau huruf 'I'?）", "Tolong dipastikan itu angka satu, huruf 'L' kecil, atau huruf 'I' besar?", "トロン ディパスティカン イトゥ アンカ サトゥ、フルフ 'エル' クチル、アタウ フルフ 'イー' ブサール", "1, l, I の厳密確認。"),
            ("【アットマーク】@の記号はインドネシア語で何と呼びますか？（Tanda '@' disebut apa dalam bahasa Indonesia?）", "Tanda '@' biasanya dibaca 'et' atau 'keong' ya kak?", "サンダ アットマーク ビアサニャ ディバチャ 'エット' アタウ 'ケオン' ヤ カッ", "アットマークの呼び方。"),
            ("【領収書】領収書の宛名のために会社名を一文字ずつ言います。（Saya eja nama perusahaan untuk kuitansi.）", "Saya eja nama PT kami pelan-pelan ya mas biar kuitansinya valid.", "サヤ エジャ ナマ ペーテー カミ プラン プラン ヤ マス ビアル クイタンスィニャ ヴァリッド", "領収書発行でのスペル。"),
            ("【総括】アルファベットを正確に発音できる者が、事務トラブルをゼロにする。（Ketelitian mengeja adalah benteng utama akurasi data.）", "Kuasai pelafalan abjad bahasa Indonesia: hindari salah tiket, salah transfer, dan salah surat!", "クアサイ プラファラン アブジャド バハサ インドネシア：ヒンダリ サラ ティケット、サラ トランスファー、ダン サラ スラット", "アルファベットの価値。")
        ],
        "quiz": [
            ("インドネシア語のアルファベットで「C」の正しい読み方は？", ["チェー (Cé)", "シー (See)", "クー (Koo)", "ツァー (Tsa)"], 1),
            ("電話などで字母「B」と「D」の聞き間違いを防ぐために使われる最も一般的な工夫は？", ["「BandungのB」「DenpasarのD」のように有名な都市名とセットで伝える", "大声で怒鳴る", "適当に想像で書く", "アルファベットを廃止する"], 1),
            ("電子メールアドレスの記号「@（アットマーク）」はインドネシアの日常会話で何と呼ばれる？", ["et / tanda keong (カタツムリマーク)", "tanda bintang", "tanda seru", "tanda panah"], 1)
        ]
    },
    {
        "slug": "13-phone-connection-trouble",
        "title": "【戦略会話】電話・電波障害の即応術：「声が途切れています、電波が悪いです」のサバイバル",
        "intro": "島嶼国インドネシアでは、地方への出張や雨季のスコール時、エレベーター内などでスマートフォンの電波が急激に悪化することが日常茶飯事です。通話中に焦らず「電波が悪いです」「声がロボットみたいになっています」「かけ直します」と即座に切り抜ける即応フレーズを体得します。",
        "pairs": [
            ("Sinyal di sini kurang stabil.", "Sinyalnya jelek bgt nih di sini.", "電波不良の報告"),
            ("Suara Anda terputus-putus.", "Suaranya putus-putus bro!", "音声途切れの指摘"),
            ("Perkenankan saya menghubungi kembali.", "Gue telpon balik ya, gue cari sinyal dulu.", "掛け直しの提案"),
            ("Apakah suara saya terdengar sekarang?", "Udah kedengeran belum sekarang?", "通話回復の確認")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、電波が不安定なためお声が途切れております。（Mohon maaf, sinyal kurang stabil sehingga suara terputus-putus.）", "Mohon maaf Bapak, tampaknya sinyal di lokasi kami kurang stabil sehingga suara Bapak terputus-putus.", "モホン マアフ バパッ、タンパッニャ スィニャル ディ ロカスィ カミ クラン スタビル スヒンガ スアラ バパッ トゥルプトゥス プトゥス", "公式な電波不良報告。"),
            ("【日常会話】ごめん、電波悪すぎ！全然聞こえない！（Sori sinyal jelek bgt, gak kedengeran sama sekali!）", "Halo? Bro suaranya kresek-kresek parah nih, sinyal lu apa sinyal gue ya yang bapuk?", "ハロ？ ブロ スアラニャ クレセッ クレセッ パラ ニ、スィニャル ル アパ スィニャル グエ ヤ ヤン バプッ", "友人との雑音ツッコミ。"),
            ("【掛け直し】電波の良い場所に移動して、こちらからかけ直します。（Saya cari sinyal bagus dulu, nanti saya hubungi lagi.）", "Saya bergeser ke area terbuka dulu ya pak, nanti segera saya hubungi kembali.", "サヤ ブルゲセル ク アレア トゥルブカ ドゥル ヤ パッ、ナンティ スグラ サヤ フブンギ クンバリ", "掛け直しの前置き。"),
            ("【雨天障害】大雨のせいで電波が急に落ちました。（Sinyal tiba-tiba drop gara-gara hujan lebat.）", "Di sini lagi hujan badai lebat petir nih, sinyal mendadak hilang timbul.", "ディ スィニ ラギ フジャン バダイ ルバット プティール ニ、スィニャル ムンダダッ ヒラン ティンブル", "天候による電波障害。"),
            ("【音声ロボット化】声が機械みたいに歪んで聞こえます。（Suaranya terdengar seperti robot.）", "Suara Bapak agak terdistorsi kayak robot nih, boleh matikan video sejenak?", "スアラ バパッ アガッ トゥルディストルスィ カヤッ ロボット ニ、ボレ マティカン ヴィデオ スジュナッ", "ロボット声への対処。"),
            ("【切断警告】トンネル・地下に入るので電話が切れるかもしれません。（Bisa terputus karena masuk terowongan.）", "Saya sedang masuk area basement parkir nih, kalau tiba-tiba terputus mohon maklum ya.", "サヤ スダン マスッ アレア ベースメント パルキール ニ、カロ ティバ ティバ トゥルプトゥス モホン マクルム ヤ", "切断の事前予告。"),
            ("【通話回復】もしもし、今私の声はクリアに聞こえますか？（Halo, apakah suara saya sudah terdengar jelas sekarang?）", "Halo tes tes, gimana sekarang pak? Sudah terdengar jernih tanpa gema?", "ハロ テス テス、ギマナ スカラン パッ？ スダ トゥルドゥンガル ジュルニ タンパ グマ", "音声回復チェック。"),
            ("【WhatsApp通話切替】通常の電話回線に切り替えて通話しましょう。（Mari beralih ke panggilan seluler biasa.）", "Panggilan WA-nya macet-macet nih, kita pindah telepon pulsa biasa aja yuk.", "パンギラン ダブリューエーニャ マチェット マチェット ニ、キタ ピンダ テレポン プルサ ビアサ アジャ ユッ", "回線切り替えの提案。"),
            ("【チャット代替】電波が治らないので、要件をWhatsAppで文章で送ります。（Saya kirimkan poinnya lewat teks WhatsApp saja ya.）", "Daripada terputus-putus, rinciannya langsung saya ketik via pesan WhatsApp sekarang ya pak.", "ダルィパダ トゥルプトゥス プトゥス、リンチアンニャ ランスン サヤ クティッ ヴィア プサン ダブリューエー スカラン ヤ パッ", "テキスト送信への切り替え。"),
            ("【保留要請】一瞬ミュートにして電波を確認させてください。（Tolong tunggu sejenak, saya cek koneksi.）", "Tunggu satu menit ya mas, saya restart koneksi internet gawai saya dulu sebentar.", "トゥング サトゥ ムニット ヤ マス、サヤ リスタート コネクスィ インターネット ガワイ サヤ ドゥル スブンタル", "接続再起動の要請。"),
            ("【遅延・ディレイ】音声に数秒のタイムラグが発生しています。（Ada delay suara beberapa detik.）", "Ada jeda delay suara sekitar tiga detik nih, bicaranya gantian ya biar gak tabrakan.", "アダ ジェダ ディレイ スアラ スキタール ティガ ドゥティッ ニ、ビチャラニャ ガンティアン ヤ ビアル ガッ タブラカン", "音声遅延への対処。"),
            ("【無音状態】もしもし？切れた？聞こえてる？（Halo? Putus ya? Masih di situ gak?）", "Halo? Kok mendadak hening ya, masih nyambung gak nih panggilannya?", "ハロ？ コッ ムンダダッ ヘニン ヤ、マスィ ニャンブン ガッ ニ パンギランニャ", "沈黙時の確認。"),
            ("【バッテリー低下】充電が切れそうなので手短に要件をお願いします。（Baterai hampir habis, mohon to-the-point ya.）", "Baterai ponsel saya tinggal 3% nih pak, mohon poin intinya saja sebelum mati mendadak.", "バテライ ポンセル サヤ ティンガル ティガ パーセン ニ パッ、モホン ポイン インティニャ サジャ スブルム マティ ムンダダッ", "バッテリー残量警告。"),
            ("【運転中注意】運転中でスピーカー通話なので少し反響しています。（Sedang menyetir menggunakan handsfree.）", "Saya lagi nyetir pake speaker handsfree nih, agak sedikit bergema suaranya.", "サヤ ラギ ニェティル パケ スピーカー ハンズフリー ニ、アガッ スディキット ブルグマ スアラニャ", "ハンズフリー通話の断り。"),
            ("【総括】電波障害に慌てるな。別の通信手段へ瞬時に誘導せよ。（Jangan panik saat sinyal drop; segera alihkan ke jalur komunikasi lain!）", "Sinyal putus bukan akhir dunia: beralihlah ke teks, voice note, atau telpon reguler seketika!", "スィニャル プトゥス ブカン アキール ドゥニア：ブルアリラ ク テクス、ヴォイス ノート、アタウ テルポン レグレール スクティカ", "通信サバイバルの鉄則。")
        ],
        "quiz": [
            ("電波が悪くて相手の声が途切れている時に伝える定番フレーズ「suara Anda terputus-putus」の意味は？", ["あなたの声が途切れ途切れになっています", "あなたの声が美しすぎます", "あなたの電話番号を忘れました", "新しい携帯を買ってください"], 1),
            ("電話の電波が悪い時に、一度切って自分から掛け直すことを伝える丁寧な表現は？", ["Nanti segera saya hubungi kembali setelah mendapat sinyal bagus", "Jangan pernah telepon saya lagi", "Saya mau lempar HP ini", "Bicaralah dengan orang lain"], 1),
            ("WhatsAppなどのネット通話（VoIP）が不安定な際、最も確実な代替手段は？", ["通常の電話回線（seluler biasa）やテキストメッセージへ切り替える", "画面を激しく叩く", "相手の悪口をSNSに投稿する", "何時間も無言で待ち続ける"], 1)
        ]
    },
    {
        "slug": "14-zoom-online-meeting-trouble",
        "title": "【戦略会話】オンライン会議トラブル：「画面が固まりました、ミュートを解除してください」",
        "intro": "ZoomやGoogle Meet、Microsoft Teamsによるオンライン会議が日常化した現代、画面フリーズ、ミュート忘れ、画面共有トラブル、ハウリングへの即座の対処フレーズはビジネスパーソンの必須サバイバルスキルです。スマートに英語混じりのオンライン用語を使いこなします。",
        "pairs": [
            ("Layar Anda tampak membeku (freeze).", "Layarnya nge-freeze pak!", "画面フリーズの指摘"),
            ("Mohon nyalakan mikrofon (unmute).", "Masih di-mute tuh mik-nya!", "ミュート解除の要請"),
            ("Apakah tayangan presentasi sudah terlihat?", "Udah muncul belum slide-nya?", "画面共有の確認"),
            ("Terdengar suara dengung (feedback).", "Bocor suaranya, agak berdengung.", "ハウリング・雑音の指摘")
        ],
        "drill": [
            ("【ミュート解除】恐れ入ります、マイクがミュートになっています。（Mohon maaf, mikrofon Anda masih termute.）", "Mohon maaf Bapak Direktur, tampaknya mikrofon Bapak masih dalam posisi bisu (mute).", "モホン マアフ バパッ ディレクトゥール、タンパッニャ マイクロフォン バパッ マスィ ダラム ポスィスィ ビス（ミュート）", "公式なミュート解除要請。"),
            ("【画面フリーズ】画面が固まって動かなくなっています。（Layarnya membeku tidak bergerak.）", "Aduh layarnya nge-freeze nih pak, videonya diam dan suara Bapak hilang.", "アドゥ レイヤーニャ ンゲフリーズ ニ パッ、ヴィデオニャ ディアム ダン スアラ バパッ ヒラン", "フリーズの指摘。"),
            ("【画面共有確認】私の共有画面は皆様に見えていますでしょうか？（Apakah layar presentasi saya sudah terlihat?）", "Apakah salindia tayangan presentasi kami sudah tampak jelas di layar rekan-rekan?", "アパカ サリンディア タヤンガン プレゼンタスィ カミ スダ タンパッ ジュラス ディ レイヤー ルカン ルカン", "共有画面の見え具合確認。"),
            ("【カメラOFF提案】通信を安定させるため、カメラをオフにしてみましょう。（Matikan kamera agar koneksi lebih stabil.）", "Koneksinya agak berat nih, gimana kalau kita nonaktifkan kamera video sementara?", "コネクスィニャ アガッ ブラット ニ、ギマナ カロ キタ ノンアクティフカン カメラ ヴィデオ スムンタラ", "帯域節約の提案。"),
            ("【再入室要請】一度退出して、もう一度入り直してもらえますか？（Boleh tolong keluar lalu masuk lagi?）", "Boleh coba leave meeting dulu terus join kembali pak, biasanya langsung lancar.", "ボレ チョバ リーヴ ミーティング ドゥル トゥルス ジョイン クンバリ パッ、ビアサニャ ランスン ランチャール", "再入室の勧め。"),
            ("【画面共有権限】ホストの方、画面共有の権限を付与していただけますか？（Mohon beri izin untuk membagikan layar.）", "Mohon izin Host, apakah bisa mengaktifkan akses 'share screen' untuk akun saya?", "モホン イジン ホスト、アパカ ビサ ムンアクティフカン アクセス 'シェア スクリーン' ウントゥッ アクン サヤ", "共有権限のリクエスト。"),
            ("【全画面表示】スライドを全画面表示（スライドショー）にしていただけますか？（Boleh jadikan layar penuh?）", "Boleh tolong di-klik mode 'slideshow' layar penuh agar tulisannya lebih terbaca?", "ボレ トロン ディ クリック モード 'スライドショー' レイヤー プヌ アガル トゥリスアンニャ ルビ トゥルバチャ", "スライドショー表示要請。"),
            ("【ハウリング】どなたかのマイクから激しい反響音が聞こえています。（Ada gema feedback dari salah satu mikrofon.）", "Ada suara dengung feedback yang cukup kencang, mohon peserta lain mute mik masing-masing ya.", "アダ スアラ ドゥングン フィードバック ヤン チュクップ クンチャン、モホン プスルタ ライン ミュート ミック マスィン マスィン ヤ", "ハウリング沈静化。"),
            ("【チャット誘導】音声が不安定なので、ご意見をチャット欄に書き込んでください。（Tulis pendapat di kolom chat saja.）", "Karena audio agak putus-putus, tanggapannya boleh langsung diketik di kolom obrolan (chat box) ya.", "カレナ オーディオ アガッ プトゥス プトゥス、タングアパンニャ ボレ ランスン ディクティッ ディ コロム オブロラン（チャットボックス）ヤ", "チャット欄活用誘導。"),
            ("【リンク共有】資料のリンクをチャットボックスに貼り付けました。（Tautan materi sudah ditempel di kolom chat.）", "Link dokumen laporan lengkapnya sudah kami sematkan di room chat, silakan diakses.", "リンク ドクメン ラポラン ルンカップニャ スダ カミ スマットカン ディ ルーム チャット、スィラカン ディアクセス", "URL共有アナウンス。"),
            ("【タイムラグ】スライドのページ送りに少し時差があります。（Ada jeda saat pergantian slide.）", "Perpindahan slidenya ada sedikit jeda delay ya, mohon tunggu beberapa detik.", "プルピンダハン スライドニャ アダ スディキット ジェダ ディレイ ヤ、モホン トゥング ブルブラパ ドゥティッ", "スライド遅延の事前案内。"),
            ("【録画確認】本日の会議を録画（レコーディング）してもよろしいでしょうか？（Bolehkah merekam sesi rapat ini?）", "Apakah seluruh hadirin berkenan apabila sesi diskusi hari ini kami rekam (record)?", "アパカ スルルー ハディリン ブルクナン アパビラ ススィ ディスクスィ ハリ イニ カミ レカム（レコード）", "録画の承諾確認。"),
            ("【仮想背景】バーチャル背景のせいで顔が透けてしまっています。（Wajah tembus pandang karena virtual background.）", "Background virtualnya bikin muka Bapak agak hilang timbul nih, boleh diganti latar polos?", "バックグラウンド ヴァーチャルニャ ビキン ムカ バパッ アガッ ヒラン ティンブル ニ、ボレ ディガンティ ラタール ポロス", "仮想背景の調整依頼。"),
            ("【ブレイクアウト】小部屋（ブレイクアウトルーム）に分かれて議論しましょう。（Mari berpencar ke breakout room.）", "Sekarang kita akan bagi peserta ke dalam beberapa breakout room secara acak ya.", "スカラン キタ アカン バギ プスルタ ク ダラム ブルブラパ ブレイクアウトルーム スチャラ アチャッ ヤ", "分科会ルームへの誘導。"),
            ("【総括】トラブルの迅速な言語化が、オンライン会議の知性を決定づける。（Ketangkasan teknis dalam rapat virtual adalah cermin profesionalisme modern.）", "Jangan diam saat layar freeze: sampaikan kendala teknis dengan lugas dan cari solusinya bersama!", "ジャンガン ディアム サアット レイヤー フリーズ：サンパイカン クンダラ テクニス ドゥンガン ルガス ダン チャリ ソルスィニャ ブルサマ", "オンライン会議の掟。")
        ],
        "quiz": [
            ("相手がマイクを消したまま話している時、「ミュートになっていますよ」と伝える表現は？", ["Mikrofon Anda masih dalam posisi bisu / di-mute", "Layar Anda sangat kotor", "Kamera Anda sangat mahal", "Rambut Anda sangat rapi"], 1),
            ("オンライン通話で画面や映像が固まって動かない状態を表す定番の口語動詞は？", ["nge-freeze", "nge-gas", "nge-drop", "nge-print"], 1),
            ("画面共有で「プレゼンのスライドが映っていますか？」と確認する表現は？", ["Apakah salindia / layarnya sudah terlihat?", "Apakah Anda lapar?", "Jam berapa sekarang?", "Di mana rumah Anda?"], 1)
        ]
    },
    {
        "slug": "15-interrupting-politely",
        "title": "【戦略会話】丁寧な割り込み：「一言よろしいですか？」と白熱した議論に割って入る技術",
        "intro": "インドネシア人の会議やディスカッションは時に熱を帯び、発話が重なり合ってなかなか割って入れない状況が生じます。無礼にならず、相手の勢いを止めずに敬意を払ってスッと発言権を獲得する「大人の割り込みストラテジー」を訓練します。",
        "pairs": [
            ("Boleh saya menyela sebentar?", "Boleh potong bentar gak?", "割り込み許可のレジスター差"),
            ("Mohon izin menambahkan satu poin penting.", "Mau nambahin dikit dong!", "補足提案のレジスター差"),
            ("Sebelum beralih ke topik lain...", "Bentar, sebelum ganti topik...", "話題転換阻止の差"),
            ("Perkenankan saya meluruskan hal ini.", "Gue lurusin dikit ya...", "誤解是正の割り込み")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、一言だけ補足させていただいてもよろしいでしょうか。（Mohon maaf, bolehkah saya menambahkan satu poin singkat?）", "Mohon maaf Bapak pimpinan, perkenankan saya menyela sejenak untuk menambahkan satu data penting.", "モホン マアフ バパッ ピンピナン、プルクナンカン サヤ ムニュラ スジュナッ ウントゥッ ムナンバカン サトゥ データ プンティン", "公式会議での丁寧な割り込み。"),
            ("【日常会話】ちょっと待って！一言言わせて！（Bentar bro, boleh motong dikit gak!）", "Eh bentar-bentar, potong dikit dong! Gue punya info penting soal ini!", "エ ブンタル ブンタル、ポトン ディキット ドン！ グエ プニャ インフォ プンティン ソアル イニ", "友人同士の熱い割り込み。"),
            ("【話題転換阻止】次の話題に行く前に、今の件だけ決着させてください。（Sebelum ganti topik, tuntaskan ini dulu.）", "Sebelum kita beralih ke agenda berikutnya, boleh kita pastikan kesepakatan poin ini?", "スブルム キタ ブルアリ ク アジェンダ ブルイクットニャ、ボレ キタ パスティカン クスパカタン ポイン イニ", "議論の置き去り防止。"),
            ("【賛同からの割り込み】その意見に大賛成です、そして実はもう一つありまして。（Sangat setuju, dan ada satu hal lagi.）", "Saya sangat sepakat dengan apa yang disampaikan Pak Budi, dan ingin memperkuat argumen tersebut.", "サヤ サンガット スパカット ドゥンガン アパ ヤン ディサンパイカン パッ ブディ、ダン インギン ムンプルクアット アルグメン トゥルスブット", "同調を足がかりにした発言。"),
            ("【反論の割り込み】失礼ながら、その前提には少し誤解があるようです。（Mohon maaf, tampaknya ada sedikit kekeliruan asumsi.）", "Mohon izin memotong, tampaknya asumsi dasar data yang kita gunakan perlu dikoreksi sedikit.", "モホン イジン ムモトン、タンパッニャ アスムスィ ダサール データ ヤン キタ グナカン プル ディコレクスィ スディキット", "前提の誤り指摘。"),
            ("【緊急の割り込み】緊急の連絡が入りましたので、中断をお許しください。（Mohon maaf ada info darurat mendesak.）", "Mohon maaf sekali memotong jalannya rapat, ada kabar darurat dari kantor pusat yang harus disampaikan.", "モホン マアフ スカリ ムモトン ジャランニャ ラパット、アダ カバル ダルラット ダリ カントール プサット ヤン ハルス ディサンパイカン", "緊急中断。"),
            ("【同僚】ちょっと私の話も聞いてよ！（Dengerin cerita gue juga napa!）", "Gantian dong woi, dari tadi lu mulu yang monolog, dengerin versi gue nih!", "ガンティアン ドン ウォイ、ダリ タディ ル ムル ヤン モノログ、ドゥンゲルイン ヴェルスィ グエ ニ", "発話独占へのツッコミ。"),
            ("【質問の割り込み】今の単語の定義だけ先に確認させてください。（Boleh tahu definisi istilah tadi dulu?）", "Izin memotong sebentar, sebelum melangkah lebih jauh, apa maksud dari istilah 'omnichannel' tadi ya?", "イジン ムモトン スブンタル、スブルム ムランカ ルビ ジャウ、アパ マクスッド ダリ イスティラ 'オムニチャネル' タディ ヤ", "定義確認の即座割り込み。"),
            ("【議事進行】皆様、発言が重複していますので順番にお願いします。（Mohon bergantian karena suara bertumpuk.）", "Bapak dan Ibu sekalian, mohon izin menengahi, agar tertib mari kita beri kesempatan satu per satu.", "バパッ ダン イブ スカリアン、モホン イジン ムヌンガヒ、アガル トゥルティッブ マリ キタ ブリ クスンパタン サトゥ プル サトゥ", "司会者としての仲裁。"),
            ("【雑談】それ私の得意分野だから語らせて！（Itu bidang gue bgt, biar gue jelasin!）", "Wih itu mah makanan sehari-hari gue, sini biar gue beberin faktanya ke kalian!", "ウィッ イトゥ マ マカナン スハリ ハリ グエ、スィニ ビアル グエ ベベリン ファクタニャ ク カリアン", "得意分野へのカットイン。"),
            ("【時間管理】残り時間わずかですので、まとめに入りましょう。（Waktu tersisa sedikit, mari kita simpulkan.）", "Mengingat waktu kita tinggal lima menit lagi, izin memotong untuk merumuskan simpulan akhir.", "ムニンガット ワクトゥ キタ ティンガル リマ ムニット ラギ、イジン ムモトン ウントゥッ ムルムスカン スィンプルアン アキール", "タイムキーパー割り込み。"),
            ("【事実確認】その数字は税別ですか、それとも税込ですか？（Itu sebelum atau sesudah pajak ya?）", "Potong sebentar ya pak, nominal 100 juta tadi sudah include PPN atau belum?", "ポトン スブンタル ヤ パッ、ノミナル スラトゥス ジュタ タディ スダ インクルード ペーペーエン アタウ ブルム", "数値精度の割り込み確認。"),
            ("【感情の鎮静化】白熱しすぎているので、少し落ち着きましょう。（Mari kita turunkan tensi sejenak.）", "Izin menengahi rekan-rekan, mari kita tarik napas sejenak dan kembali fokus pada solusi objektif.", "イジン ムヌンガヒ ルカン ルカン、マリ キタ タリッ ナパス スジュナッ ダン クンバリ フォーカス パダ ソルスィ オブイェクティフ", "過熱議論の冷却。"),
            ("【通訳・翻訳】通訳のために少し文を区切ってください。（Mohon beri jeda untuk penerjemahan.）", "Mohon maaf Bapak pembicara, izin memotong sejenak agar saya dapat menerjemahkan kalimat tadi.", "モホン マアフ バパッ プンビチャラ、イジン ムモトン スジュナッ アガル サヤ ダパット ムヌルジェマカン カリマット タディ", "通訳者の割り込み要請。"),
            ("【総括】礼儀正しい割り込みは、議論を活性化させるアクセルである。（Interupsi santun adalah pelumas dinamika intelektual.）", "Jangan takut memotong: minta izin dengan santun, sampaikan poin bernas, dan kembalikan panggungnya!", "ジャンガン タクット ムモトン：ミンタ イジン ドゥンガン サントゥン、サンパイカン ポイン ブルナス、ダン クンバリカン パングンニャ", "割り込みの美学。")
        ],
        "quiz": [
            ("相手の話の途中で丁寧に割って入る際、最も上品で角の立たない前置きは？", ["Mohon izin menyela sejenak...", "Diam kamu!", "Jangan banyak bacot!", "Saya bosan mendengar Anda!"], 1),
            ("話題が次のテーマに移りそうな時、「その前にこの点だけ決着させて」と引き止める表現は？", ["Sebelum beralih ke topik berikutnya...", "Setelah semuanya selesai...", "Besok saja kita bicarakan...", "Lupakan saja masalah ini..."], 1),
            ("議論に割り込む際、相手の気分を害さないための最も効果的なテクニックは？", ["相手の意見を肯定・賞賛した上で、補足や追加の形で発言する", "相手の意見を全否定して罵倒する", "机を叩いて大声を出す", "相手の弱点を暴露する"], 1)
        ]
    },
    {
        "slug": "16-resuming-after-interruption",
        "title": "【戦略会話】発話の本題復帰：「話が逸れましたが、元の話に戻すと…」の軌道修正",
        "intro": "雑談や割り込み、突発的な電話などで本題から大きく脱線してしまった後、スムーズに会話のレールを元の位置に戻す「発話の本題復帰（Resuming after Interruption）」は、会議を脱線させず時間内にゴールへ導くファシリテーションの最重要スキルです。",
        "pairs": [
            ("Kembali ke topik utama pembahasan...", "Balik lagi ke topik tadi ya...", "本題復帰の前置き"),
            ("Melanjutkan apa yang saya sampaikan tadi...", "Ngelanjutin omongan gue tadi...", "直前の発言継続"),
            ("Sebelum teralihkan, kita sedang membahas...", "Tadi kan kita lagi ngomongin...", "脱線前の話題想起"),
            ("Mari kita fokuskan kembali perhatian pada...", "Fokus ke sini dulu yuk...", "注意集中への誘導")
        ],
        "drill": [
            ("【ビジネス】さて、本題に戻りましょう。（Baiklah, mari kita kembali ke pokok pembahasan semula.）", "Baiklah Bapak dan Ibu, mari kita kembali memfokuskan perhatian pada agenda utama kita hari ini.", "バイッラ バパッ ダン イブ、マリ キタ クンバリ ムムフォーカスカン プルハティアン パダ アジェンダ ウタマ キタ ハリ イニ", "公式な本題復帰。"),
            ("【日常会話】あ、話が逸れちゃったね！元の話に戻すと…（Eh malah ngelantur kemana-mana! Balik ke topik ya...）", "Eh kok jadi ngelantur ngomongin gosip sih! Balik lagi ke cerita yang tadi ya...", "エ コッ ジャディ ンゲラントゥール ンオモンイン ゴスィップ スィ！ バリッ ラギ ク チュリタ ヤン タディ ヤ", "雑談脱線からの復帰。"),
            ("【会議】先ほどの電話で中断されましたが、発言を続けさせていただきます。（Melanjutkan paparan yang sempat terinterupsi.）", "Mohon maaf atas interupsi telepon tadi, perkenankan saya melanjutkan penjelasan terkait anggaran.", "モホン マアフ アタス インテルプスィ テレポン タディ、プルクナンカン サヤ ムンランジュットカン プンジュラサン トゥルカイット アンガラン", "電話中断からの再開。"),
            ("【質問後】ご質問への回答が終わりましたので、元のスライドに戻ります。（Kembali ke tayangan salindia utama.）", "Pertanyaan tadi sudah terjawab tuntas ya, sekarang mari kita kembali ke slide nomor empat.", "プルタニャアン タディ スダ トゥルジャワブ トゥンタス ヤ、スカラン マリ キタ クンバリ ク スライド ノモール エンパット", "質疑後のスライド復帰。"),
            ("【同僚】さっきどこまで話したっけ？（Tadi nyampe mana ya kita ngomongnya?）", "Eh tadi gue ngomong nyampe mana ya? Oh iya, soal tiket pesawat yang promo itu!", "エ タディ グエ ンオモン ニャンペ マナ ヤ？ オー イヤ、ソアル ティケット プサワット ヤン プロモ イトゥ", "失念からの話題復元。"),
            ("【脱線制止】話が本筋から離れすぎているので、一旦整理しましょう。（Pembahasan sudah terlalu jauh melebar.）", "Diskusi ini tampaknya sudah agak melebar dari koridor awal, mari kita tarik mundur ke inti masalah.", "ディスクスィ イニ タンパッニャ スダ アガッ ムルバール ダリ コリドール アワル、マリ キタ タリッ ムンドゥール ク インティ マサラ", "脱線拡大の抑止。"),
            ("【意思決定】雑談はランチの時にして、まず結論を決めましょう。（Ngobrol santainya pas makan siang aja.）", "Nostalgianya kita sambung pas santap siang ya rekan-rekan, sekarang kita ketuk palu keputusan ini dulu.", "ノスタルギアニャ キタ サンブン パス サンタップ スィアン ヤ ルカン ルカン、スカラン キタ クトゥッ パル クプトゥサン イニ ドゥル", "決定優先の復帰。"),
            ("【時間管理】残り時間がありません、本題に集中してください。（Waktu menipis, mohon fokus kembali.）", "Waktu kita hanya tersisa sepuluh menit, mohon tidak membuka topik cabang baru di luar agenda.", "ワクトゥ キタ ハニャ トゥルスィサ スプル ムニット、モホン ティダッ ムンブカ トピック チャバン バル ディ ルアル アジェンダ", "時間制約下での集中。"),
            ("【中断対応】来客対応が完了しましたので、再開いたします。（Tamu sudah selesai dilayani, mari lanjut.）", "Terima kasih atas kesabaran hadirin menunggu, mari kita lanjutkan evaluasi draf kontrak ini.", "トゥリマ カシ アタス クサバラン ハディリン ムヌング、マリ キタ ランジュットカン エヴァルアスィ ドラフ コントラク イニ", "来客中断からの再開。"),
            ("【発話継続】さっき私が言いかけたことなんだけど。（Soal apa yang mau gue omongin tadi.）", "Ngelanjutin kalimat gue yang kepotong barusan, intinya kita mesti gerak cepet sebelum kompetitor tahu.", "ンゲランジュットイン カリマット グエ ヤン クポトン バルサン、インティニャ キタ ムスティ グラッ チパット スブルム コンペティトール タウ", "遮られた発言の完結。"),
            ("【カフェ】店員さんの注文で途切れちゃったね。（Kepotong pas masnya nganter pesanan ya.）", "Tadi seru bgt ceritanya sebelum makanannya dateng, lanjutin dong kelanjutannya gimana!", "タディ スル バンゲット チュリタニャ スブルム マカナンニャ ダトゥン、ランジュッティン ドン クランジュタンニャ ギマナ", "店員中断からの再開。"),
            ("【オンライン通信復帰】ネットが落ちて退出していましたが、復帰しました。（Sempat terlempar keluar meeting, mari lanjut.）", "Mohon maaf sempat terlempar karena koneksi putus, boleh saya lanjutkan penjelasan saya?", "モホン マアフ スンパット トゥルレンパール カレナ コネクスィ プトゥス、ボレ サヤ ランジュットカン プンジュラサン サヤ", "回線切断からの復帰。"),
            ("【感情冷却後】落ち着いたところで、論理的な議論に戻りましょう。（Setelah tenang, mari kembali berdialog rasional.）", "Sekarang setelah suasana lebih tenang, mari kita kaji ulang opsi-opsi yang tersedia secara dingin.", "スカラン ストゥラ スアサナ ルビ トゥナン、マリ キタ カジ ウラン オプスィ オプスィ ヤン トゥルスディア スチャラ ディンギン", "沈静化後の本題復帰。"),
            ("【話の主軸】一番大事な問いは「誰が責任を持つか」です。（Pertanyaan paling krusial adalah siapa penanggung jawabnya.）", "Lepas dari segala perdebatan teknis, mari kembali ke pertanyaan paling mendasar: siapa PIC-nya?", "ルパス ダリ スガラ プルデバタン テクニス、マリ クンバリ ク プルタニャアン パリン ムンダサール：スィアパ ピーアイシーニャ", "最重要論点への回帰。"),
            ("【総括】脱線を楽しんだ後、必ず本線に引き戻すのが一流の対話力である。（Kecakapan mengembalikan jalur percakapan adalah inti kematangan.）", "Boleh saja sesekali melebar; namun pemimpin dialog sejati selalu tahu jalan pulang ke inti masalah!", "ボレ サジャ ススカリ ムルバール；ナムン プミンピン ディアログ スジャティ スラル タウ ジャラン プラン ク インティ マサラ", "本題復帰の極意。")
        ],
        "quiz": [
            ("話が脱線した後に「さて、元の本題に戻りましょう」と軌道修正する定番フレーズは？", ["Mari kita kembali ke pokok pembahasan / topik utama...", "Mari kita tidur sekarang...", "Mari kita lari keliling lapangan...", "Mari kita berkelahi di luar..."], 1),
            ("日常会話で「あ、話があちこち脱線しちゃったね！」と笑いながら自戒する表現は？", ["Eh kok malah ngelantur kemana-mana...", "Eh kok makanannya enak sekali...", "Eh kok bajunya bagus...", "Eh kok hari ini mendung..."], 1),
            ("ファシリテーターが議論を時間内にゴールへ導くために不可欠なスキルは？", ["脱線した話題を適切に打ち切り、アジェンダの本題へ引き戻すこと", "全員に好きなだけ雑談を続けさせること", "怒って途中で会議を放り出すこと", "自分一人だけで喋り続けること"], 1)
        ]
    },
    {
        "slug": "17-checking-unknown-word",
        "title": "【戦略会話】即座の単語質問：「その言葉はどういう意味ですか？」と会話の場で吸収する",
        "intro": "会話の中で知らない単語（Kata yang tidak diketahui）が出てきた時、聞き流して曖昧にするのは語学力向上の最大の機会損失です。相手の話の腰を折らずに「Apa artinya kata itu?（その単語はどういう意味ですか？）」「Bisa kasih contoh?（具体例を教えてもらえますか？）」と、会話そのものを学習の場に変える技術を体得します。",
        "pairs": [
            ("Apa arti dari kata tersebut?", "Maksud kata itu apaan sih?", "単語の意味質問"),
            ("Istilah itu biasa digunakan dalam konteks apa?", "Biasanya dipake buat apa kata itu?", "使用文脈の質問"),
            ("Apakah ada padanan katanya dalam bahasa Inggris?", "Bahasa Inggrisnya apa tuh kira-kira?", "英語の同義語確認"),
            ("Bisakah Anda memberikan contoh kalimatnya?", "Contoh kalimatnya gimana coba?", "例文提示の要請")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、先ほどの単語はどういう意味でしょうか？（Mohon maaf, apa arti dari istilah tadi?）", "Mohon maaf Bapak, istilah yang baru saja Bapak sebutkan artinya apa ya secara konteks bisnis?", "モホン マアフ バパッ、イスティラ ヤン バル サジャ バパッ スブットカン アルティニャ アパ ヤ スチャラ コンテクス ビスニス", "ビジネス用語の質問。"),
            ("【日常会話】その言葉どういう意味？初めて聞いた！（Apaan tuh artinya? Baru denger gue!）", "Eh 'mager' itu apaan sih artinya? Sering denger tapi gak tau kepanjangannya!", "エ 'マゲル' イトゥ アパアン スィ アルティニャ？ スリン ドゥンゲル タピ ガッ タウ クパンジャンガンニャ", "若者スラングの即座質問。"),
            ("【用例依頼】その言葉を使った例文を一つ教えてもらえますか？（Bisa kasih satu contoh kalimatnya?）", "Bisa tolong kasih contoh pemakaiannya dalam kalimat sehari-hari biar lebih kebayang?", "ビサ トロン カスィ チョント プマカイアンニャ ダラム カリマット スハリ ハリ ビアル ルビ クバヤン", "例文による理解の深化。"),
            ("【略語の展開】その略語は何の頭文字を取ったものですか？（Singkatan dari apa istilah itu?）", "Kalo istilah 'PDKT' itu sebenernya singkatan dari kata apa aja ya bro?", "カロ イスティラ 'ペーデーカーテー' イトゥ スブヌルニャ スィンカタン ダリ カタ アパ アジャ ヤ ブロ", "略語のフルスペル確認。"),
            ("【ニュアンスの差異】AとBはどうニュアンスが違うのですか？（Apa beda nuansa antara A dan B?）", "Beda nuansa rasa antara kata 'peduli' sama 'kepo' itu di sebelah mananya ya mas?", "ベダ ヌアンサ ラサ アンタラ カタ 'プドゥリ' サマ 'ケポ' イトゥ ディ スブラ マナニャ ヤ マス", "類義語のニュアンス比較。"),
            ("【英語の対照】英語で言うと何という単語に相当しますか？（Kira-kira apa padanan katanya dalam bahasa Inggris?）", "Kalau dalam bahasa Inggris, padanan kata yang paling pas buat istilah ini apa ya?", "カロ ダラム バハサ イングリス、パダナン カタ ヤン パリン パス ブアット イスティラ イニ アパ ヤ", "英語対訳の確認。"),
            ("【使用の適切性】その言葉は目上の人に対して使っても失礼になりませんか？（Apakah kata itu sopan untuk orang tua?）", "Kata itu tergolong sopan gak ya kalo saya pake pas ngomong ke atasan di kantor?", "カタ イトゥ トゥルゴロン ソパン ガッ ヤ カロ サヤ パケ パス ンオモン ク アタサン ディ カントール", "敬語・レジスターの確認。"),
            ("【方言判定】それはジャカルタの言葉ですか、それとも地方の方言ですか？（Itu bahasa Jakarta atau bahasa daerah?）", "Kata 'monggo' itu serapan dari bahasa Jawa kan ya? Di Jakarta umum dipake gak?", "カタ 'モンゴ' イトゥ スラパン ダリ バハサ ジャワ カン ヤ？ ディ ジャカルタ ウムム ディパケ ガッ", "方言・文化背景の質問。"),
            ("【流行の度合い】その言葉は最近の若者の流行語ですか？（Apakah itu bahasa gaul anak muda zaman sekarang?）", "Itu istilah yang lagi viral di TikTok sekarang ya? Artinya positif atau negatif?", "イトゥ イスティラ ヤン ラギ ヴィラル ディ ティックトック スカラン ヤ？ アルティニャ ポスィティフ アタウ ネガティフ", "流行度とトーンの確認。"),
            ("【メモの許可】とても面白い単語ですね、メモ帳に書き留めてもいいですか？（Kata yang menarik, boleh saya catat?）", "Wah istilah baru nih, menarik bgt! Izin saya catat di HP ya biar gak lupa.", "ワ イスティラ バル ニ、ムナリッ バンゲット！ イジン サヤ チャタット ディ エイチピー ヤ ビアル ガッ ルパ", "積極的な学習意欲の表明。"),
            ("【反意語の確認】反対の意味を表す言葉は何と言いますか？（Apa lawan kata dari istilah tersebut?）", "Kalo lawan katanya apa ya? Kebalikan dari orang yang 'boros' itu apa istilahnya?", "カロ ラワン カタニャ アパ ヤ？ クバリカン ダリ オラン ヤン 'ボロス' イトゥ アパ イスティラニャ", "対義語の引き出し。"),
            ("【発音の再確認】もう一度その単語を発音してもらえますか？（Boleh lafalkan kata itu sekali lagi?）", "Boleh tolong ucapkan sekali lagi? Saya mau tiru intonasi dan tekanan suaranya.", "ボレ トロン ウチャップカン スカリ ラギ？ サヤ マウ ティル イントナスィ ダン トゥカナン スアラニャ", "発音模倣の要請。"),
            ("【漢字や原語の由来】中国語やアラビア語に由来する言葉ですか？（Apakah kata itu berasal dari bahasa Arab atau Hokkien?）", "Kata 'cuan' itu asalnya dari bahasa Tionghoa kan ya mas? Artinya untung ya?", "カタ 'チュアン' イトゥ アサルニャ ダリ バハサ ティオンホア カン ヤ マス？ アルティニャ ウントゥン ヤ", "語源の探求。"),
            ("【即座のフィードバック】私が今その単語を使って文を作ってみてもいいですか？（Boleh saya coba pakai kata itu dalam kalimat sekarang?）", "Boleh saya tes bikin kalimat pake kata itu sekarang? Tolong koreksi kalo aneh ya!", "ボレ サヤ テス ビキン カリマット パケ カタ イトゥ スカラン？ トロン コレクスィ カロ アネ ヤ", "即座のアウトプット実践。"),
            ("【総括】質問する者は一瞬の無知を晒すが、質問せぬ者は一生無知のままである。（Bertanya di saat ragu adalah tanda pembelajar sejati.）", "Setiap kata asing di tengah obrolan adalah tambang emas kosakata baru: bertanyalah dengan antusias!", "スティアップ カタ アスィン ディ トゥンガ オブロラン アダラ タンバン エマス コサカタ バル：ブルタニャラ ドゥンガン アントゥスィアス", "語彙獲得の哲学。")
        ],
        "quiz": [
            ("相手の発言中に出てきた未知語の意味をその場で尋ねる最も基本的なフレーズは？", ["Apa artinya kata itu? / Maksud kata itu apa ya?", "Saya tidak suka kata itu!", "Jangan pakai bahasa Indonesia!", "Berapa harga buku ini?"], 1),
            ("略語（Singkatan）に出会った際、「何の頭文字を取ったものですか？」と尋ねる表現は？", ["Singkatan dari apa istilah itu?", "Siapa yang membuat singkatan itu?", "Kapan singkatan itu dibuat?", "Berapa huruf dalam kata itu?"], 1),
            ("会話の場で未知の単語を教えてもらった後、記憶に定着させるための最高の実践行動は？", ["その場で教えてもらった単語を使って自分で短い例文を作り、相手に確認してもらう", "すぐに忘れて別の話題に行く", "メモを捨てて帰宅する", "単語が難しいと文句を言う"], 1)
        ]
    },
    {
        "slug": "18-explaining-japanese-concept",
        "title": "【戦略会話】日本特有概念の説明：「稟議」「お歳暮」「根回し」を平易に解説する",
        "intro": "日系企業で働くインドネシア人同僚や現地の友人から、「日本の『稟議（Ringi）』って何？」「『お歳暮』と『お中元』は何が違うの？」「『過労死』はどうして起きるの？」と質問された際、直訳に頼らず、現地の文化や制度と対比しながら平易なインドネシア語で説明する文化通訳スキルを養成します。",
        "pairs": [
            ("Konsep budaya khas Jepang... (日本独特の文化概念)", "Tradisi unik di Jepang yang...", "文化前置きのフレーム"),
            ("Tujuannya adalah untuk... (その目的は〜である)", "Tujuannya buat...", "目的説明のフレーム"),
            ("Bisa dibandingkan dengan tradisi... (〜の伝統に比較できる)", "Mirip-mirip kayak tradisi...", "現地文化との対照"),
            ("Proses birokrasi di mana... (〜という官僚的プロセス)", "Alur persetujuan di mana...", "制度・手続きの説明")
        ],
        "drill": [
            ("【稟議（Ringi）】部下が起案し、関係部署の上長全員が順番に印鑑を押して承認するボトムアップの決裁制度。（Sistem persetujuan berjenjang dari bawah ke atas menggunakan stempel cap.）", "Ringi itu sistem persetujuan proposal dari staf bawah yang diedarkan ke semua atasan buat dapet cap stempel berurutan.", "リンギ イトゥ スィステム プルス トゥジュアン プロポサル ダリ スタッフ バワ ヤン ディエダルカン ク スムア アタサン ブアット ダペット チャップ ステンペル ブルウルタン", "稟議制度の解説。"),
            ("【根回し（Nemawashi）】会議で反対されないよう、事前にキーマンと個別に話し合って合意を取り付けておく水面下の調整。（Proses lobi informal sebelum rapat resmi untuk mencapai konsensus.）", "Nemawashi itu semacem lobi-lobi informal di belakang layar sebelum rapat resmi, biar pas rapat langsung disetujui tanpa drama.", "ネマワシ イトゥ スマチェム ロビ ロビ インフォルマル ディ ブラカン レイヤー スブルム ラパット レスミ、ビアル パス ラパット ランスン ディストゥジュイ タンパ ドラマ", "根回しの解説。"),
            ("【お歳暮・お中元】日頃お世話になっている取引先や親戚に、感謝を込めて半期ごとに贈るギフト文化。（Tradisi mengirimkan bingkisan hadiah sebagai wujud terima kasih dua kali setahun.）", "Tradisi ngirimin parcel hadiah resmi kayak kue atau buah ke rekan bisnis sama kerabat buat tanda terima kasih, mirip hampers Lebaran.", "トラディスィ ンギリミン パルセル ハディア レスミ カヤッ クエ アタウ ブア ク ルカン ビスニス サマ クラバット ブアット サンダ トゥリマ カシ、ミリッ ハンパーズ ルバラン", "贈答文化の解説。"),
            ("【過労死（Karoshi）】極端な長時間残業と精神的ストレスにより、突然心不全や脳卒中で亡くなること。（Kematian mendadak akibat kelelahan kerja ekstrem dan tekanan mental.）", "Karoshi itu fenomena meninggal mendadak karena serangan jantung akibat lembur kerja yang gila-gilaan tanpa istirahat.", "カローシ イトゥ フェノメナ ムニンガル ムンダダッ カレナ サランガン ジャンツン アキバット レンブール クルジャ ヤン ギラギラアン タンパ イスティラハット", "過労死の解説。"),
            ("【飲み会（Nomikai）】職場の同僚や上司と居酒屋でお酒を飲みながら、本音でコミュニケーションを深める懇親の場。（Acara minum bersama sepulang kerja untuk mempererat keakraban antar rekan.）", "Tradisi nongkrong minum bareng sepulang kerja di kedai Izakaya, tujuannya buat ngobrol santai dari hati ke hati sama atasan.", "トラディスィ ノンクロン ミヌム バレン スプラン クルジャ ディ クダイ イザカヤ、トゥジュアンニャ ブアット ンオブロル サンタイ ダリ ハティ ク ハティ サマ アタサン", "飲み会文化の解説。"),
            ("【報連相（Ho-Ren-So）】「報告・連絡・相談」の略で、ビジネスにおける情報共有の鉄則。（Singkatan dari Lapor (Hokoku), Hubungi (Renraku), dan Konsultasi (Sodan).）", "Horenso itu pilar komunikasi kerja di Jepang: wajib lapor progres rutin, kabarin info terbaru, dan selalu konsultasi kalo ada kendala.", "ホウレンソウ イトゥ ピラール コムニカスィ クルジャ ディ ジュパン：ワジブ ラポル プログレス ルティン、カバリン インフォ トゥルバル、ダン スラル コンスルタスィ カロ アダ クンダラ", "ホウレンソウの解説。"),
            ("【花見（Hanami）】春に咲く桜の木の下にシートを敷き、皆で飲み食いしながら花を鑑賞するピクニック。（Piknik bersama di bawah pohon sakura yang sedang mekar di musim semi.）", "Piknik bareng keluarga atau teman kantor di bawah pohon sakura mekar sambil makan dan minum, cuma ada setahun sekali pas musim semi.", "ピクニック バレン クルアルガ アタウ トゥムン カントール ディ バワ ポホン サクラ ムカール サンビル マカン ダン ミヌム、チュマ アダ スタフン スカリ パス ムスィム スミ", "花見の解説。"),
            ("【もったいない（Mottainai）】物が無駄に捨てられたり粗末に扱われたりするのを惜しむ心。（Rasa sayang dan penyesalan mendalam apabila sesuatu terbuang sia-sia.）", "Filosofi menghargai barang biar gak mubazir: rasa sayang dan bersalah kalo ada makanan atau benda yang dibuang padahal masih berguna.", "フィロソフィ ムンハルガイ バラン ビアル ガッ ムバジール：ラサ サヤン ダン ブルサラ カロ アダ マカナン アタウ ブンダ ヤン ディブアン パダハル マスィ ブルグナ", "もったいないの解説。"),
            ("【空気を読む（Kuuki wo Yomu）】言葉にされない周囲の雰囲気や人々の意図を、察して適切に行動すること。（Kemampuan membaca suasana dan memahami hal tersirat tanpa diucapkan.）", "Kemampuan peka membaca situasi sosial dan mengerti apa yang diharapkan orang lain tanpa perlu dibilang secara langsung.", "クマンプアン ペカ ムンバチャ スィツアスィ ソスィアル ダン ムンゲルティ アパ ヤン ディハラップカン オラン ライン タンパ プル ディビラン スチャラ ランスン", "空気を読むの解説。"),
            ("【おもてなし（Omotenashi）】見返りを求めず、細部まで心を配って客人を温かくもてなす精神。（Semangat keramahtamahan yang tulus dan penuh perhatian pada detail.）", "Kultur pelayanan tulus yang luar biasa perhatian sampe ke detail kecil, tujuannya bikin tamu ngerasa dihargai sepenuh hati.", "クルトゥール プラヤナン トゥルス ヤン ルアル ビアサ プルハティアン サンペ ク ディテイル クチル、トゥジュアンニャ ビキン タム ンゲラサ ディハルガイ スプヌ ハティ", "おもてなしの解説。"),
            ("【先輩・後輩（Senpai-Kohai）】年齢や入学・入社年次に基づく、厳格かつ面倒見の良い縦の人間関係。（Hierarki hubungan senior-junior yang didasari rasa hormat dan bimbingan.）", "Hierarki senior dan junior di sekolah atau kantor: yang junior wajib hormat, sedangkan yang senior wajib bimbing dan traktir.", "ヒエラルキ セニオル ダン ジュニオル ディ スコラ アタウ カントール：ヤン ジュニオル ワジブ ホルマット、スダンカン ヤン セニオル ワジブ ビンビン ダン トラクティール", "先輩後輩関係の解説。"),
            ("【お盆（Obon）】夏にご先祖様の魂が家に帰ってくると信じられ、迎え火を焚いて供養する仏教行事。（Ritual mengenang arwah leluhur yang diyakini pulang ke rumah pada musim panas.）", "Tradisi di mana orang Jepang percaya arwah leluhur pulang ke rumah, jadi sekeluarga mudik ke kampung halaman buat bersihin kuburan.", "トラディスィ ディ マナ オラン ジュパン プルチャヤ アルワ ルルフール プラン ク ルマ、ジャディ スクルアルガ ムディッ ク カンプン ハラマン ブアット ブルスィヒン クブラン", "お盆の解説。"),
            ("【割り勘（Warikan）】飲食代などの請求額を、参加者全員で均等に頭割りして支払う習慣。（Membagi tagihan pembayaran makanan secara rata kepada setiap orang.）", "Budaya bayar masing-masing dengan membagi total bon makanan secara rata ke semua orang yang ikut makan.", "ブダヤ バヤル マスィン マスィン ドゥンガン ムンバギ トータル ボン マカナン スチャラ ラタ ク スムア オラン ヤン イクット マカン", "割り勘の解説。"),
            ("【弁当（Bento）】栄養バランスや彩り、見た目の美しさを工夫して箱に詰めた手作りご飯。（Kotak bekal makan siang yang disusun secara bergizi, rapi, dan estetik.）", "Kotak bekal nasi yang dihias rapi dan lucu dengan lauk-pauk bergizi seimbang, disiapin penuh cinta dari rumah.", "コタック ブカル ナスィ ヤン ディヒアス ラピ ダン ルチュ ドゥンガン ラウッ パウッ ブルギズィ スインバン、ディスィアピン プヌ チンタ ダリ ルマ", "弁当の解説。"),
            ("【総括】文化を平易に架橋する言葉を持てば、真の相互理解が生まれる。（Menjelaskan budaya sendiri dengan bahasa mereka adalah esensi diplomasi warga.）", "Jangan hanya bilang 'sulit diterjemahkan': temukan analogi budayanya di Indonesia, maka jembatan hati akan terbentang!", "ジャンガン ハニャ ビラン 'スリット ディトゥルジェマカン'：トゥムカン アナロギ ブダヤニャ ディ インドネシア、マカ ジュンバタン ハティ アカン トゥルベンタン", "文化通訳の神髄。")
        ],
        "quiz": [
            ("日本の「稟議（Ringi）」をインドネシア人に最も分かりやすく要約した説明は？", ["sistem persetujuan proposal dari staf bawah yang diedarkan ke semua atasan buat dapat cap stempel", "tradisi minum teh di sore hari", "seni merangkai bunga di vas", "pakaian adat tradisional dari sutra"], 1),
            ("事前に水面下で関係者と話し合って合意を取り付けておく「根回し（Nemawashi）」の的確な比喩は？", ["lobi-lobi informal di belakang layar sebelum rapat resmi", "memotong pohon di hutan belantara", "berlari cepat di jalan raya", "tidur siang di kantor"], 1),
            ("日本の「お中元・お歳暮」のギフト文化をインドネシア人に説明する際、最も親しみやすい現地対照は？", ["Tradisi parcel hampers Idulfitri / Lebaran", "Festival layang-layang", "Upacara bendera 17 Agustus", "Lomba panjat pinang"], 1)
        ]
    },
    {
        "slug": "19-negotiating-price-limits",
        "title": "【戦略会話】予算限界の提示：「これ以上は予算オーバーです」と角を立てずに伝える",
        "intro": "買い物の値引き交渉やビジネスでの価格折衝において、「高すぎる！」「そんな金はない！」と直接的に突き放すと、相手のプライドを傷つけ関係が破綻します。「こちらの予算枠がここまででして…」「上司の承認が下りる上限がこの金額です」と、客観的な限界ラインを示して相手の譲歩を引き出す洗練された交渉術を学びます。",
        "pairs": [
            ("Anggaran yang dialokasikan terbatas pada...", "Budget kami mentok di angka...", "予算上限の提示"),
            ("Jika melebihi nominal ini, persetujuan sulit didapat.", "Kalo lewat dari ini, bos gak bakal acc.", "決裁権限の理由付け"),
            ("Apakah ada opsi penyesuaian spesifikasi?", "Bisa kurangin fiturnya biar masuk budget?", "仕様変更の打診"),
            ("Harga pas untuk kami adalah...", "Harga pasnya mentok berapa nih mas?", "最終価格の探り")
        ],
        "drill": [
            ("【ビジネス】申し訳ありませんが、当社の予算上限は1億ルピアとなっております。（Mohon maaf, plafon anggaran kami terbatas pada 100 juta rupiah.）", "Mohon maaf Bapak, plafon anggaran yang disetujui direksi kami mentok di angka seratus juta rupiah.", "モホン マアフ バパッ、プラフォン アンガラン ヤン ディストゥジュイ ディレクスィ カミ ムントッ ディ アンカ スラトゥス ジュタ ルピア", "ビジネス予算上限の提示。"),
            ("【日常買い物】予算オーバーだからこれ以上は無理！（Over budget nih, gak sanggup kalo segitu!）", "Wah over budget bgt nih mas, dompet saya gak kuat kalo segitu, pasnya berapa nih?", "ワ オーヴァー バジェット バンゲット ニ マス、ドンペット サヤ ガッ クアット カロ スギトゥ、パスニャ ブラパ ニ", "市場での愛嬌ある交渉。"),
            ("【上司決裁】この金額を超えると、本社の承認が下りません。（Jika melebihi nominal ini, kantor pusat tidak akan menyetujui.）", "Jika melampaui angka tersebut, kami pastikan dokumen ini akan ditolak oleh komite anggaran kantor pusat.", "ジカ ムランパウイ アンカ トゥルスブット、カミ パスティカン ドクメン イニ アカン ディトラッ オレ コミテ アンガラン カントール プサット", "決裁権限を盾にした限界提示。"),
            ("【仕様削減】予算内に収めるために、一部の機能を削ることは可能ですか？（Bisa kurangi sebagian fitur agar pas di anggaran?）", "Apakah memungkinkan untuk menurunkan sedikit spesifikasi teknisnya agar angkanya masuk ke pagu anggaran kami?", "アパカ ムンムンキンカン ウントゥッ ムヌルンカン スディキット スペスィフィカスィ テクニスニャ アガル アンカニャ マスッ ク パグ アンガラン カミ", "機能削減による減額提案。"),
            ("【まとめ買い】もし3台まとめて購入するなら、単価を下げてもらえますか？（Bisa diskon per unit kalau beli 3 sekaligus?）", "Seandainya kami menerbitkan PO untuk tiga unit sekaligus hari ini, berapakah diskon maksimal yang bisa Bapak berikan?", "セアンダイニャ カミ ムヌルビットカン ピーオー ウントゥッ ティガ ユニット スカリグス ハリ イニ、ブラパカ ディスコン マクスィマル ヤン ビサ バパッ ブリカン", "ボリュームディスカウント打診。"),
            ("【店頭値引き】キリの良い数字で、50万ルピアちょうどにしてくれませんか？（Bisa dibulatkan jadi 500 ribu pas?）", "Bisa digenapin jadi lima ratus ribu pas gak mas? Biar langsung saya bayar tunai sekarang.", "ビサ ディグナピン ジャディ リマ ラトゥス リブ パス ガッ マス？ ビアル ランスン サヤ バヤル トゥナイ スカラン", "端数切捨て提案。"),
            ("【ホテル延泊】連泊するので、長期滞在レートを適用していただけますか？（Bisa kasih rate khusus long-stay?）", "Berhubung saya menginap selama dua minggu berturut-turut, apakah ada tarif khusus long-stay yang lebih bersahabat?", "ブルフブン サヤ ムンインアップ スラマ ドゥアミング ブルツルット ツルット、アパカ アダ タリフ カス ロングステイ ヤン ルビ ブルサハバット", "長期割引交渉。"),
            ("【納期緩和】急ぎませんので、通常納期で割引をお願いできますか？（Kami tidak buru-buru, boleh diskon untuk tempo reguler?）", "Kami tidak memerlukan pengiriman ekspres kok, kalau pakai jadwal pengiriman reguler apakah biayanya bisa ditekan?", "カミ ティダッ ムムルルカン プンキリマン エクスプレス コッ、カロ パケ ジャドワル プンキリマン レグレール アパカ ビアヤニャ ビサ ディトゥカン", "納期緩和によるコスト減。"),
            ("【競合対照】他社様からこの金額で見積もりをいただいているのですが。（Kami menerima penawaran dari vendor lain sebesar...）", "Sebagai transparansi, pihak kompetitor menawarkan angka 80 juta, apakah Bapak bisa menyamai angka tersebut?", "スバガイ トランスパランスィ、ピハッ コンペティトール ムナワルカン アンカ ドラパンプル ジュタ、アパカ バパッ ビサ ムニャマイ アンカ トゥルスブット", "競合相見積もりの提示。"),
            ("【予算残高】今期の残予算がこれしか残っていないのです。（Sisa anggaran periode ini tinggal segini.）", "Sisa alokasi dana departemen kami untuk kuartal ini benar-benar hanya tersisa nominal tersebut.", "スィサ アロカスィ ダナ デパルテメン カミ ウントゥッ クアルタル イニ ブナル ブナル ハニャ トゥルスィサ ノミナル トゥルスブット", "残予算の客観的提示。"),
            ("【妥協点】お互いの中間を取って、この金額で手を打ちませんか？（Bagaimana kalau kita ambil jalan tengah di angka...）", "Bagaimana bila kita ambil titik temu di tengah-tengah: win-win solution di angka 45 juta?", "バガイマナ ビラ キタ アンビル ティティッ トゥム ディ トゥンガ トゥンガ：ウィン ウィン ソリューション ディ アンカ エンパットプル リマ ジュタ", "中間妥協点の提示。"),
            ("【次回への期待】今回はこの価格でお願いして、次回大型案件で恩返しします。（Tolong beri harga terbaik kali ini, nanti kami repeat order.）", "Bantu kami di proyek perdana ini dulu ya pak, jika performanya memuaskan, kami garansi pesanan berikutnya jauh lebih besar.", "バントゥ カミ ディ プロイェッ プルダナ イニ ドゥル ヤ パッ、ジカ ペルフォルマニャ ムムアスカン、カミ ガランスィ プサナン ブルイクットニャ ジャウ ルビ ブサール", "将来のリピート約束。"),
            ("【おまけ要求】価格が引けないなら、オプション品を無料で付けてくれませんか？（Kalau harga fix, boleh tambah bonus aksesoris?）", "Kalo harga produknya udah nett gak bisa goyang, boleh tolong sertakan bonus casing sama anti-goresnya?", "カロ ハルガ プロドゥッニャ ウダ ネット ガッ ビサ ゴヤン、ボレ トロン スルタカン ボーナス ケーシング サマ アンティ ゴレスニャ", "オマケ・付帯サービスの要求。"),
            ("【最後の切り札】これが私の出せる最終金額です、無理なら諦めます。（Ini penawaran terakhir saya, kalau tidak bisa ya sudah.）", "Ini tawaran terakhir dari saya ya mas, mentok di 200 ribu, kalo gak dapet yaudah belum jodoh berarti.", "イニ タワラン トゥラキール ダリ サヤ ヤ マス、ムントッ ディ ドゥアラトゥス リブ、カロ ガッ ダペット ヤウダ ブルム ジョドッ ブラルティ", "最終通告（belum jodoh）。"),
            ("【総括】交渉とは戦いではなく、双方が納得する着地点を探すダンスである。（Negosiasi bukan pertarungan, melainkan tarian mencari titik temu.）", "Tunjukkan batas kemampuan secara santun: hormati penjual, lindungi dompet sendiri!", "トゥヌジュッカン バタス クマンプアン スチャラ サントゥン：ホルマティ プンジュアル、リンドゥンギ ドンペット スンディリ", "価格交渉の哲学。")
        ],
        "quiz": [
            ("交渉で「こちらの予算の上限は〜で頭打ちです（限界です）」と伝える時の定番語「mentok」の意味は？", ["限界・突き当たり・頭打ち", "まだ余裕がある", "無料である", "倍増する"], 1),
            ("価格がどうしても下げられない時に、実質的にお得にするための優れた交渉アプローチは？", ["価格はそのままで、オマケや付帯サービス（bonus / aksesoris）を付けてもらう", "店員を罵倒する", "警察を呼ぶ", "商品を壊す"], 1),
            ("インドネシアの露店や市場で、これ以上安くならない時に「ご縁がなかったということで諦めます」と笑顔で言う慣用句は？", ["Kalo gak dapet yaudah belum jodoh berarti", "Kamu jahat sekali", "Toko ini jelek", "Saya mau bakar pasar"], 1)
        ]
    },
    {
        "slug": "20-handling-complaints-calmly",
        "title": "【戦略会話】苦情・クレームの初期対応：怒りを鎮め、事実関係を冷静に傾聴する",
        "intro": "顧客や取引先から激しい怒りや苦情（Komplain）をぶつけられた際、即座に言い訳（alasan）をしたり反論したりすると火に油を注ぎます。「まずはご不快な思いをさせた心情に共感して謝罪し、事実関係を冷静に傾聴・確認し、具体的な対応策を約束する」というプロフェッショナルの初期対応フレームワークを身につけます。",
        "pairs": [
            ("Kami mohon maaf atas ketidaknyamanan ini.", "Sori bgt ya atas kejadian ini.", "不快感への一次謝罪"),
            ("Tolong ceritakan kronologi kejadiannya.", "Bisa ceritain detailnya gimana tadi?", "事実関係の傾聴要請"),
            ("Kami akan segera menindaklanjuti keluhan ini.", "Gue urus skrg juga masalah ini ya.", "即時対応の確約"),
            ("Hal ini menjadi evaluasi berharga bagi kami.", "Ini jadi pelajaran penting buat kita.", "改善姿勢の表明")
        ],
        "drill": [
            ("【一次謝罪】ご不便とご迷惑をおかけしましたことを、心よりお詫び申し上げます。（Kami menyampaikan permohonan maaf sebesar-besarnya atas ketidaknyamanan yang terjadi.）", "Kami menyampaikan permohonan maaf yang sedalam-dalamnya atas ketidaknyamanan yang dialami oleh Bapak.", "カミ ムンニャムパイカン プルモホナン マアフ ヤン スダラム ダラムニャ アタス クティダッニャマナン ヤン ディアラミ オレ バパッ", "プロフェッショナルな一次謝罪。"),
            ("【傾聴の姿勢】大変ご立腹されるのもごもっともです、何が起きたか詳しくお聞かせいただけますでしょうか。（Sangat wajar Bapak merasa kecewa, boleh ceritakan kronologinya?）", "Sangat kami pahami kekecewaan Bapak; perkenankan kami mendengarkan kronologi peristiwanya secara lengkap.", "サンガット カミ パハミ ククチェワアン バパッ；プルクナンカン カミ ムンドゥンガルカン クロノロギ プリスティワニャ スチャラ ルンカップ", "共感と傾聴の導入。"),
            ("【反論の抑制】言い訳をするつもりはございません、弊社の落ち度でございます。（Kami tidak bermaksud membela diri, ini murni kekeliruan kami.）", "Kami sama sekali tidak bermaksud mencari pembenaran, kelalaian ini sepenuhnya berada di pihak internal kami.", "カミ サマ スカリ ティダッ ブルマクスッド ムンチャリ プムブナラン、クラライアン イニ スプヌフニャ ブラダ ディ ピハッ インテルナル カミ", "言い訳の徹底排除。"),
            ("【事実確認】商品が破損していた状態の写真を拝見してもよろしいでしょうか？（Bolehkah kami melihat foto kondisi barang yang rusak?）", "Boleh tolong kirimkan dokumentasi foto kondisi barang saat pertama kali diterima agar kami catat ke sistem?", "ボレ トロン キリムカン ドクメンタスィ フォト コンディスィ バラン サアット プルタマ カリ ディトゥリマ アガル カミ チャタット ク スィステム", "事実確認の記録化。"),
            ("【即時交換】直ちに新品の代替品を至急便で再発送いたします。（Kami segera mengirimkan produk pengganti yang baru secara kilat.）", "Hari ini juga kami kirimkan produk pengganti baru melalui kurir instan tanpa biaya sepeser pun.", "ハリ イニ ジュガ カミ キリムカン プロドゥッ プンガンティ バル ムラルイ クーリエ インスタン タンパ ビアヤ スペセル プン", "即時代替品の提供。"),
            ("【返金保証】ご希望であれば、全額返金の手続きを速やかに進めさせていただきます。（Bila berkenan, kami proses pengembalian dana penuh.）", "Apabila Bapak menghendaki pembatalan, dana pembayaran akan kami kembalikan utuh seratus persen dalam tempo 1x24 jam.", "アパビラ バパッ ムンフンダキ プムバタラン、ダナ プンバヤラン アカン カミ クンバリカン ウトゥ スラトゥス パーセン ダラム テンポ サトゥ カリ ドゥアプル エンパット ジャム", "返金の即答。"),
            ("【感情の受け止め】お怒りはごもっともです、私が責任を持って対応いたします。（Amarah Bapak sangat berdasar, saya pribadi yang mengawal solusinya.）", "Saya mengerti sekali rasa jengkel yang timbul; saya pribadi yang akan mengawal investigasi ini hingga tuntas.", "サヤ ムンゲルティ スカリ ラサ ジェンケル ヤン ティンブル；サヤ プリバディ ヤン アカン ムンアワル インヴェスティガスィ イニ ヒンガ トゥンタス", "責任者の特定と安心感付与。"),
            ("【原因調査の約束】なぜこのようなミスが発生したのか、徹底的に原因を究明いたします。（Kami akan mengusut tuntas akar penyebab kesalahan ini.）", "Tim teknis kami sedang mengaudit sistem peladen untuk menemukan akar masalah agar tidak terulang lagi.", "ティム テクニス カミ スダン ムンオウディット スィステム プラデン ウントゥッ ムヌムカン アカール マサラ アガル ティダッ トゥルウラン ラギ", "再発防止の調査約束。"),
            ("【店舗での初期対応】店長をお呼びしますので、涼しいお席でお掛けになってお待ちください。（Silakan duduk di ruangan ber-AC sementara saya panggilkan manajer.）", "Mari Bapak silakan duduk di ruangan yang lebih sejuk dulu, saya panggilkan Manajer Operasional kami segera.", "マリ バパッ スィラカン ドゥドゥッ ディ ルアンガン ヤン ルビ スジュッ ドゥル、サヤ パンギルカン マナジェール オペラシオナル カミ スグラ", "環境変更による怒り鎮静。"),
            ("【進捗連絡の確約】本日夕方17時までに、第一報の調査結果をお電話でご報告いたします。（Kami kabari perkembangan terbarunya sore ini pukul 17.00.）", "Paling lambat pukul lima sore nanti, saya pribadi akan menghubungi Bapak untuk menyampaikan hasil investigasi awal.", "パリン ランバット プクル リマ ソレ ナンティ、サヤ プリバディ アカン ムンフブンギ バパッ ウントゥッ ムンニャムパイカン ハシル インヴェスティガスィ アワル", "タイムリミットの明確化。"),
            ("【社内エスカレーション】経営陣に直ちに本件を重要インシデントとして報告いたします。（Kami eskalasikan perkara ini ke jajaran manajemen direksi.）", "Masalah ini telah kami masukkan ke dalam kategori prioritas merah dan dilaporkan langsung ke meja Direktur Utama.", "マサラ イニ トゥラ カミ マスッカン ク ダラム カテゴリ プリオリタス メラ ダン ディラポルカン ランスン ク メジャ ディレクトゥール ウタマ", "事態の重要性認識の共有。"),
            ("【書面での提出】口頭だけでなく、書面にて正式な始末書と対策書を提出いたします。（Kami sampaikan nota evaluasi resmi secara tertulis.）", "Laporan insiden resmi beserta langkah perbaikan tertulis akan kami serahkan kepada instansi Bapak besok pagi.", "ラポラン インスィデン レスミ ブルスルタ ランカ プルバイカン トゥルトゥリス アカン カミ スラカン クパダ インスタンスィ バパッ ベソッ パギ", "公式書面での対応。"),
            ("【感謝の転換】貴重なご指摘をいただき、心より感謝申し上げます。（Terima kasih banyak atas kritik konstruktif yang telah disampaikan.）", "Kritik tajam dari Bapak merupakan masukan yang sangat berharga bagi kami untuk berbenah lebih baik lagi.", "クリティッ タジャム ダリ バパッ ムルパカン マスカン ヤン サンガット ブルハルガ バギ カミ ウントゥッ ブルブナ ルビ バイッ ラギ", "苦情への感謝転換。"),
            ("【同僚間トラブル】嫌な思いをさせて本当にごめん、二度としない！（Sori bgt udah bikin lu gak nyaman, suer gak bakal gue ulangin!）", "Sori bgt ya bro atas keteledoran gue, bener-bener gak ada maksud jahat, makasih udah mau ngingetin langsung.", "ソリ バンゲット ヤ ブロ アタス クトゥレドラン グエ、ブナル ブナル ガッ アダ マクスッド ジャハット、マカスィ ウダ マウ ンギンゲッティン ランスン", "友人・同僚間の誠実な謝罪。"),
            ("【総括】苦情の初期対応で最も大切なのは、言い訳の速さではなく共感の深さである。（Empati mendahului solusi; dengarkan dengan hati sebelum menawarkan logika.）", "Tahan dorongan untuk membela diri: dengarkan hingga tuntas, akui kelalaian, dan buktikan solusi nyata!", "タハン ドロンガン ウントゥッ ムンベラ ディリ：ドゥンガルカン ヒンガ トゥンタス、アクイ クラライアン、ダン ブクティカン ソルスィ ニャタ", "苦情対応の鉄則。")
        ],
        "quiz": [
            ("クレームを受けた際、初期対応として最も絶対に避けるべきNG行動は？", ["相手の話を遮って「それは弊社のせいではありません」と言い訳（pembenaran）すること", "まずは不快な思いをさせたことに対して真摯に謝罪すること", "相手の言い分を途中で遮らずに最後までメモを取りながら傾聴すること", "調査結果の連絡期限を具体的に伝えること"], 1),
            ("相手の怒りを鎮めるために、事実確認の前にまず示すべき態度は？", ["相手が失望したり怒ったりした感情への共感（Empati）", "警察を呼んで威嚇すること", "笑い飛ばして冗談にすること", "電話を無言で切ること"], 1),
            ("不具合のあった商品を前にして、顧客の信頼を瞬時に回復する最も誠実な初期解決策は？", ["新品の即時無償交換（produk pengganti baru）または全額返金（refund penuh）の提示", "半額だけ客に負担させる", "メーカーに直接文句を言えと突き放す", "自分で直せと工具を渡す"], 1)
        ]
    }
]

for a in articles_data:
    filepath = os.path.join("docs/strategies", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. 戦略的キラーフレーズ対比表（公式・ビジネス ⇄ 日常会話 ⇄ 緊急サバイバル）\n")
    lines.append("| No | 公式・ビジネス表現 | 日常・カジュアル口語 | 状況・ニュアンス |")
    lines.append("|---|---|---|---|")
    for idx, (baku, gaul, meaning) in enumerate(a['pairs'], 1):
        lines.append(f"| {idx} | `{baku}` | **{gaul}** | {meaning} |")
    lines.append("")
    
    lines.append("## 2. 意味交渉（Negotiation of Meaning）のメカニズム\n")
    lines.append("第二言語習得論（SLA）におけるインターアクション仮説（Long）が示す通り、コミュニケーションの破綻を修復し、相手と意味をすり合わせる「意味交渉」のプロセスこそが、言語能力を飛躍的に高める最大の触媒です。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 場面別サバイバル・プラクティス（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 提示されたシチュエーションと日本語を見て、1〜2秒以内に口頭で適切なサバイバルフレーズを声に出してください。\n")
    
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

print("Batch 1161-1170 generated successfully.")
