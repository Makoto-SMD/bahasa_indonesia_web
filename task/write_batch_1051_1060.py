"""Writer Script: Articles 1051 - 1060 for docs/clinic/
"""

articles_data = [
    {
        "slug": "01-sudah-tense-overuse",
        "title": "【誤用克服】「〜した＝sudah」の呪縛！過去テンスとアスペクト完了の混同を直す",
        "intro": "日本語話者が最も頻繁に犯す誤用が「過去の出来事なら何でも sudah をつけてしまう」現象です。インドネシア語には動詞の過去形が存在せず、文脈や時制副詞（kemarin, tadi）で過去を表します。sudah は「すでに完了していること（現在の視点）」を強調する場合にのみ使うという根本原則を体得します。",
        "cases": [
            ("昨日、映画を見ました。", "Saya kemarin sudah menonton film.", "Kemarin saya menonton film.", "kemarin（昨日）という過去の時を表す語がある場合、sudah を入れると「すでに観終えていた」という不自然な完了強調になり、ネイティブにはくどく聞こえます。単に動詞をそのまま置くだけで十分です。"),
            ("さっき彼と話しました。", "Tadi saya sudah berbicara dengan dia.", "Tadi saya berbicara dengan dia.", "tadi（さっき）が過去を示しているため、sudah は原則不要です。")
        ],
        "drill": [
            ("昨日、日本から友達が来ました。", "Kemarin teman dari Jepang datang.", "クマリン トゥマン ダリ ジュパン ダタン", "kemarin があるので sudah は不要。"),
            ("先週、新しいパソコンを買いました。", "Minggu lalu saya membeli komputer baru.", "ミング ラル サヤ ムンブリ コンピューテル バル", "minggu lalu だけで過去を表す。"),
            ("今朝、コーヒーを飲みました。", "Pagi tadi saya minum kopi.", "パギ タディ サヤ ミヌム コピ", "pagi tadi で過去明示。"),
            ("彼は2年前に大学を卒業しました。", "Dia lulus universitas dua tahun lalu.", "ディア ルルス ユニヴェルシタス ドゥア タフン ラル", "dua tahun lalu があるため sudah 不要。"),
            ("もう宿題を終えました（完了の強調）。", "Saya sudah menyelesaikan PR.", "サヤ スダ ムンユルサイカン ペーエル", "過去時を表す言葉がなく「すでに終えた」状態を強調するので sudah が必須！"),
            ("さっき電話がありました。", "Tadi ada telepon.", "タディ アダ テレポン", "tadi ada telepon で十分。"),
            ("昨夜、激しい雨が降りました。", "Tadi malam hujan deras turun.", "タディ マラム フジャン ドゥラス トゥルン", "tadi malam で過去明示。"),
            ("子供の頃、よく川で泳ぎました。", "Waktu kecil saya sering berenang di sungai.", "ワクトゥ クチル サヤ スリン ブルナン ディ スンガイ", "waktu kecil で十分。"),
            ("会議は午後3時に終わりました。", "Rapat selesai pada pukul tiga sore.", "ラパット スルサイ パダ プクル ティガ ソレ", "時刻指定があるため sudah 不要。"),
            ("もう昼食を食べましたか？（未済・完了の確認）", "Apakah Anda sudah makan siang?", "アカパ アンダ スダ マカン シアン", "未完了か完了かを問う典型的な sudah。"),
            ("私は昨日、その本を読みました。", "Kemarin saya membaca buku itu.", "クマリン サヤ ムンバチャ ブク イトゥ", "kemarin のみで過去。"),
            ("彼は先月、会社を辞めました。", "Bulan lalu dia mengundurkan diri dari kantor.", "ブラン ラル ディア ムングンドゥルカン ディリ ダリ カントール", "bulan lalu で十分。"),
            ("そのニュースはさっき聞きました。", "Berita itu tadi saya dengar.", "ブリタ イトゥ タディ サヤ ドンガル", "tadi で十分。"),
            ("もう準備ができました（完了状態）。", "Sudah siap.", "スダ シアップ", "状態の実現を表す sudah。"),
            ("私たちは去年、バリ島へ旅行しました。", "Tahun lalu kami berlibur ke Bali.", "タフン ラル カミ ブルリブール ク バリ", "tahun lalu があるため sudah 不要。")
        ],
        "quiz": [
            ("「昨日ナシゴレンを食べた」の最も自然な表現は？", ["Kemarin saya makan nasi goreng.", "Kemarin saya sudah makan nasi goreng.", "Saya sudah kemarin makan nasi goreng.", "Kemarin sudah saya makan nasi goreng."], 1),
            ("sudah を必ず使うべき状況は？", ["「すでに完了している/もう済んだ」というアスペクト状態を強調したい時", "過去の出来事には文脈に関係なく常に", "文末に置く時", "疑問文の時"], 1),
            ("「さっき彼に会った」の自然な文は？", ["Tadi saya bertemu dengan dia.", "Tadi saya sudah bertemu dengan dia.", "Sudah tadi saya bertemu dengan dia.", "Saya sudah tadi bertemu dia."], 1)
        ]
    },
    {
        "slug": "02-memberi-giving-receiving",
        "title": "【誤用克服】「〜てあげる/もらう」を memberi で直訳しない！-kan と受動態の処方箋",
        "intro": "日本語の「〜てあげる」「〜てもらう」「〜てくれる」という授受表現を、そのまま memberi（与える）で直訳した【Dia memberi saya pergi】のような壊れた文は日本人学習者の典型的な誤用です。インドネシア語では接尾辞「-kan」の受益構文や「受動態」を使って表現します。",
        "cases": [
            ("彼は私にコーヒーを淹れてくれた。", "Dia memberi membuat saya kopi.", "Dia membuatkan saya kopi.", "英語の give me や日本語の「作ってくれる」を直訳せず、動詞 membuat に受益の接尾辞 -kan をつけて membuatkan saya kopi とします。"),
            ("私は先生に推薦状を書いてもらった。", "Saya menerima guru menulis surat.", "Surat rekomendasi saya dituliskan oleh guru.", "「〜してもらう」は受益の受動態（dituliskan）で表現するのが自然です。")
        ],
        "drill": [
            ("母は私に新しい服を買ってくれた。", "Ibu membelikan saya baju baru.", "イブ ムンブリカン サヤ バジュ バル", "membelikan saya...（買ってくれた）。"),
            ("父に車を洗ってもらいました。", "Mobil saya dicucikan oleh ayah.", "モビル サヤ ディチュチカン オレ アヤ", "受動態 dicucikan oleh..."),
            ("温かい紅茶を淹れてあげましょうか？", "Mau saya buatkan teh hangat?", "マウ サヤ ブアットカン テ ハンガット", "buatkan（淹れてあげる）。"),
            ("タクシーを呼んで差し上げましょうか？", "Boleh saya carikan taksi?", "ボレ サヤ チャリカン タクシ", "carikan（探してあげる）。"),
            ("彼はお客さんにドアを開けてあげた。", "Dia membukakan pintu untuk tamu.", "ディア ムンブカカン ピントゥ ウントゥッ タム", "membukakan（開けてあげる）。"),
            ("先生に発音を直してもらいました。", "Pengucapan saya dibetulkan oleh guru.", "プングチャパン サヤ ディベトゥルカン オレ グル", "受動態 dibetulkan oleh..."),
            ("妹におもちゃを選んであげました。", "Saya memilihkan mainan untuk adik.", "サヤ メミリカン マイナン ウントゥッ アディッ", "memilihkan（選んであげる）。"),
            ("お水を一杯取ってきてくれますか？", "Bisa ambilkan saya segelas air?", "ビサ アンビルカン サヤ スグラス アイル", "ambilkan saya...（取ってくれる？）。"),
            ("彼は私に部屋を借りてくれた。", "Dia menyewakan kamar untuk saya.", "ディア ムニェワカン カマール ウントゥッ サヤ", "menyewakan（借りてくれた）。"),
            ("荷物を持ってあげましょうか？", "Biar saya bawakan barangnya?", "ビアル サヤ バワカン バランニャ", "bawakan（持ってあげる）。"),
            ("医者に診てもらいました。", "Saya diperiksa oleh dokter.", "サヤ ディプルイクサ オレ ドクテル", "診察してもらう＝diperiksa oleh..."),
            ("友達にバリ島の写真を送ってもらった。", "Saya dikirimi foto Bali oleh teman.", "サヤ ディキリミ フォト バリ オレ トゥマン", "受動態 dikirimi..."),
            ("彼女は私にインドネシア料理を作ってくれた。", "Dia memasakkan saya masakan Indonesia.", "ディア メマサッカン サヤ マサカン インドネシア", "memasakkan saya..."),
            ("ホテルを予約してあげましょうか？", "Mau saya pesankan hotel?", "マウ サヤ プサンカン ホテル", "pesankan（予約してあげる）。"),
            ("彼にお金を貸してあげなさい。", "Pinjamkan uang kepadanya.", "ピンジャムカン ウアン クパダニャ", "pinjamkan（貸してあげる）。")
        ],
        "quiz": [
            ("「彼は私に本を買ってくれた」の正しいインドネシア語は？", ["Dia membelikan saya buku.", "Dia memberi saya membeli buku.", "Dia membeli buku memberi saya.", "Dia dapat buku dari saya."], 1),
            ("日本語の「〜してもらう」をインドネシア語で表現する最も自然な方法は？", ["受動態（di- / di-...-kan）を使う", "memberi を直前に置く", "dapat を動詞の前に置く", "menerima を動詞の前に置く"], 1),
            ("「ドアを開けてあげてください」は？", ["Tolong bukakan pintunya.", "Tolong memberi buka pintu.", "Tolong buka memberi pintu.", "Tolong dibukakan memberi."], 1)
        ]
    },
    {
        "slug": "03-inanimate-subject-avoidance",
        "title": "【誤用克服】無生物主語の壁！「この薬を飲めば治る」をインドネシア語の語順で表現する",
        "intro": "日本語は人間を主語にして「この薬を飲んだら治りますよ」「この道をまっすぐ行けば駅に着きますよ」と条件節（〜たら/〜れば）で迂回して表現する傾向が強いです。一方、インドネシア語は英語と同様に「無生物（薬・道・ニュース）を主語にして直接述語を置く」方が圧倒的に簡潔で自然です。",
        "cases": [
            ("この薬を飲めば頭痛が治るよ。", "Kalau kamu minum obat ini, sakit kepala kamu sembuh.", "Obat ini menyembuhkan sakit kepala.", "人間を主語にして「Kalau kamu...」と長く回りくどく言うより、「Obat ini（この薬が）menyembuhkan sakit kepala（頭痛を治す）」と無生物主語にする方がネイティブらしく知的です。"),
            ("この道を行けば駅に着きます。", "Kalau lewat jalan ini, kamu tiba di stasiun.", "Jalan ini menuju ke stasiun.", "「Jalan ini menuju ke stasiun（この道が駅に通じている）」と表現するのが最も簡潔です。")
        ],
        "drill": [
            ("この薬は痛みを和らげます（この薬を飲めば痛みが和らぐ）。", "Obat ini meredakan rasa sakit.", "オバット イニ ムルダカン ラサ サキッ", "無生物主語 Obat ini..."),
            ("この道は直接空港へ通じています。", "Jalan ini langsung menuju ke bandara.", "ジャラン イニ ラングスン ムヌジュ ク バンダラ", "無生物主語 Jalan ini..."),
            ("そのニュースは私たち全員を驚かせた。", "Berita itu mengejutkan kita semua.", "ブリタ イトゥ ムンゲジュットカン キタ スムア", "無生物主語 Berita itu..."),
            ("この数字は経済の回復を示しています。", "Angka ini menunjukkan pemulihan ekonomi.", "アンカ イニ メヌンジュッカン プムリハン エコノミ", "無生物主語 Angka ini..."),
            ("この技術は私たちの生活を便利にします。", "Teknologi ini mempermudah hidup kita.", "テクノロジ イニ メムプルムダ ヒドゥップ キタ", "無生物主語 Teknologi ini..."),
            ("その雨が空気を涼しくした。", "Hujan itu menyejukkan udara.", "フジャン イトゥ ムニェジュッカン ウダラ", "無生物主語 Hujan itu..."),
            ("この手紙が彼の無実を証明している。", "Surat ini membuktikan bahwa dia tidak bersalah.", "スラット イニ メムブクティカン バフワ ディア ティダッ ブルサラ", "無生物主語 Surat ini..."),
            ("この規則はトラブルを防ぐためのものです。", "Aturan ini mencegah timbulnya masalah.", "アトゥラン イニ ムンチェガ ティムブルニャ マサラ", "無生物主語 Aturan ini..."),
            ("その経験が彼を強い人間に育てた。", "Pengalaman itu membentuknya menjadi pribadi yang kuat.", "プンガラマン イトゥ メムベントゥッニャ ムンジャディ プリバディ ヤン クアット", "無生物主語 Pengalaman itu..."),
            ("この看板は道順を示しています。", "Papan petunjuk ini mengarahkan jalan.", "パパン プトゥンジュッ イニ ムンガラッカン ジャラン", "無生物主語 Papan petunjuk ini..."),
            ("この本は多くの知識を与えてくれる。", "Buku ini memberikan banyak wawasan.", "ブク イニ ムンブリカン バニャッ ワワサン", "無生物主語 Buku ini..."),
            ("昨日の地震が多くの建物を破壊した。", "Gempa kemarin menghancurkan banyak bangunan.", "グムパ クマリン ムンハンチュルカン バニャッ バングナン", "無生物主語 Gempa kemarin..."),
            ("その笑顔が私の疲れを吹き飛ばしてくれた。", "Senyumannya menghilangkan rasa lelah saya.", "スニュマンニャ ムンヒランカン ラサ レラ サヤ", "無生物主語 Senyumannya..."),
            ("このアプリは時間を大幅に節約できる。", "Aplikasi ini sangat menghemat waktu.", "アプリカシ イニ サンガット ムンヘマット ワクトゥ", "無生物主語 Aplikasi ini..."),
            ("その決定が会社の未来を変えた。", "Keputusan itu mengubah masa depan perusahaan.", "クプトゥサン イトゥ ムングバ マサ ドゥパン プルサハアン", "無生物主語 Keputusan itu...")
        ],
        "quiz": [
            ("「この薬を飲めば風邪が治る」を最も自然かつ簡潔に言うと？", ["Obat ini menyembuhkan flu.", "Kalau minum obat ini kamu sembuh flu.", "Obat ini kamu minum maka flu sembuh.", "Flu sembuh jika kamu minum obat ini."], 1),
            ("「この道を行けば駅に着く」のスマートな表現は？", ["Jalan ini menuju ke stasiun.", "Kalau kamu jalan di jalan ini sampai stasiun.", "Kamu tiba di stasiun jika jalan ini.", "Jalan ini kamu pakai ke stasiun."], 1),
            ("無生物主語構文の大きなメリットは？", ["「もし〜なら」と仮定節を重ねず、主語と動詞で簡潔・明快に表現できる", "必ず受動態にできる", "主語を省略できる", "文末詞を増やせる"], 1)
        ]
    },
    {
        "slug": "04-passive-voice-overuse",
        "title": "【誤用克服】日本語の受身「〜される」の過剰直訳を排し、自然な能動態に直す",
        "intro": "日本語では「雨に降られる」「先生に褒められる」「友達に来られる」のように受身表現（特に被害受動）が極めて日常的です。しかしこれをインドネシア語で機械的に受動態に直訳すると、非常に不自然な文になります。自然な能動態 meN- や周囲辞 ke-...-an へのパラダイムシフトを行います。",
        "cases": [
            ("私は先生に褒められました。", "Saya dipuji oleh guru.", "Guru memuji saya. / Saya mendapat pujian dari guru.", "日本語では「私が褒められた」と言いますが、インドネシア語では「Guru memuji saya（先生が私を褒めた）」と能動態で言う方が圧倒的に活き活きとして自然です。"),
            ("昨夜、友達に来られて勉強できなかった。", "Tadi malam saya didatangi teman sehingga tidak bisa belajar.", "Tadi malam teman datang ke rumah sehingga saya tidak bisa belajar.", "「友達に来られる」は単に「Teman datang（友達が来た）」と能動態で言えば足ります。")
        ],
        "drill": [
            ("社長が私を新しいリーダーに選んだ（選ばれた）。", "Direktur memilih saya sebagai pemimpin baru.", "ディレクトゥール メミリ サヤ スバガイ プミンピン バル", "能動態 memilih saya。"),
            ("昨日、突然友達が私の家に来ました。", "Kemarin teman tiba-tiba datang ke rumah saya.", "クマリン トゥマン ティバティバ ダタン ク ルマ サヤ", "能動態 datang。"),
            ("母は私を厳しく叱りました（叱られた）。", "Ibu memarahi saya dengan tegas.", "イブ メマラヒ サヤ ドゥンガン トゥガス", "能動態 memarahi saya。"),
            ("上司が私の提案を承認してくれた（承認された）。", "Atasan menyetujui usulan saya.", "アタサン ムニュツジュイ ウスラン サヤ", "能動態 menyetujui。"),
            ("昨日雨に降られてずぶ濡れになった。", "Kemarin saya kehujanan sampai basah kuyup.", "クマリン サヤ クフジャナン サンパイ バサ クユップ", "自然な被災受動 kehujanan。"),
            ("近所の人たちが私を親切に歓迎してくれた。", "Warga menyambut saya dengan hangat.", "ワルガ メニャンブット サヤ ドゥンガン ハンガット", "能動態 menyambut saya。"),
            ("警察官が彼に職務質問をした。", "Polisi menanyai dia di jalan.", "ポリシ メナニャイ ディア ディ ジャラン", "能動態 menanyai。"),
            ("医者は私に十分休むよう忠告した。", "Dokter menasihati saya untuk istirahat cukup.", "ドクテル メナシハティ サヤ ウントゥッ イスティラハット チュクップ", "能動態 menasihati。"),
            ("犬が突然私に吠えかかってきた。", "Anjing tiba-tiba menggonggong ke arah saya.", "アンジン ティバティバ ムンゴンゴン ク アラ サヤ", "能動態 menggonggong。"),
            ("先生は私の質問に丁寧に答えてくれた。", "Guru menjawab pertanyaan saya dengan ramah.", "グル ムンジャワブ プルタニャアン サヤ ドゥンガン ラマ", "能動態 menjawab。"),
            ("観客は彼の素晴らしい演技に拍手を送った。", "Penonton bertepuk tangan untuk penampilannya.", "プノントン ブルテプッ タンガン ウントゥッ プナンピランニャ", "能動態 bertepuk tangan。"),
            ("泥棒が隣の家に侵入した（入られた）。", "Pencuri masuk ke rumah tetangga.", "プンチュリ マスッ ク ルマ トゥタンガ", "能動態 masuk / kemalingan。"),
            ("彼らは私を温かく励ましてくれた。", "Mereka menyemangati saya dengan tulus.", "ムレカ ムニェマンガティ サヤ ドゥンガン トゥルス", "能動態 menyemangati。"),
            ("審査員は彼女に最高得点を与えた。", "Juri memberikan nilai tertinggi kepadanya.", "ジュリ ムンブリカン ニライ トゥルティンギ クパダニャ", "能動態 memberikan。"),
            ("子供たちが私の周りに集まってきた。", "Anak-anak berkumpul di sekitar saya.", "アナッアナッ ブルクンプル ディ スキタール サヤ", "能動態 berkumpul。")
        ],
        "quiz": [
            ("「先生に褒められた」を最も自然に表現する能動文は？", ["Guru memuji saya.", "Saya dipuji oleh guru.", "Pujian guru kepada saya.", "Saya ada pujian guru."], 1),
            ("日本語の「雨に降られた（被害）」に最も適したインドネシア語は？", ["Saya kehujanan.", "Saya dihujani.", "Hujan memukul saya.", "Saya tertabrak hujan."], 1),
            ("日本語の受身をインドネシア語に移す際の重要な原則は？", ["動作主を主語にした能動文（meN-）に変換できないかまず検討する", "常に di- を使う", "常に ter- を使う", "受動態は禁止されている"], 1)
        ]
    },
    {
        "slug": "05-te-oku-preparatory",
        "title": "【誤用克服】「〜しておく（準備・放置）」の直訳ミスを防ぐ（siapkan, biarkan, dulu）",
        "intro": "日本語の「〜ておく」には、①事前準備（切符を買っておく）、②状態の放置（そのままにしておく）、③とりあえず・先行動作（先に食べておく）の3つの異なる意味があります。これらをすべて同一の単語で直訳しようとする誤用を是正し、siapkan, biarkan, dulu を使い分けます。",
        "cases": [
            ("切符を事前に買っておきます。", "Saya membeli tiket menaruh.", "Saya membeli tiket terlebih dahulu. / Saya siapkan tiketnya.", "「〜ておく」の「おく」を物理的な「置く（menaruh）」と直訳するのは致命的な誤用です。準備なら menyiapkan、事前に先行するなら terlebih dahulu / dulu を使います。"),
            ("ドアを開けたままにしておいてください。", "Tolong simpan pintu terbuka.", "Biarkan pintunya terbuka.", "状態の放置は biarkan（そのままにさせておく）を用います。")
        ],
        "drill": [
            ("出かける前に部屋を掃除しておきます。", "Saya membersihkan kamar dulu sebelum pergi.", "サヤ ムンブルシカン カマール ドゥル スブルム プルギ", "先行 dulu。"),
            ("会議の前に資料を準備しておいてください。", "Tolong siapkan dokumen sebelum rapat.", "トロン シアプカン ドクメン スブルム ラパット", "事前準備 siapkan。"),
            ("窓を開けたままにしておいてください（放置）。", "Biarkan jendelanya terbuka.", "ビアルカン ジュンデラニャ トゥルブカ", "放置 biarkan。"),
            ("先に食べておいてね（私は後で行くから）。", "Makanlah duluan ya.", "マカンラ ドゥルアン ヤ", "先行 duluan。"),
            ("忘れないようにメモ帳に書いておきました。", "Saya catat dulu di buku agar tidak lupa.", "サヤ チャタット ドゥル ディ ブク アガル ティダッ ルパ", "先行 dulu。"),
            ("荷物はそのまま置いておいてください。", "Biarkan barangnya di situ.", "ビアルカン バランニャ ディ シトゥ", "放置 biarkan。"),
            ("出かける前に電気を消しておきなさい。", "Matikan lampu dulu sebelum keluar.", "マティカン ランプ ドゥル スブルム クルアール", "先行 dulu。"),
            ("緊急時のために現金を少し用意しておきます。", "Saya siapkan sedikit uang tunai untuk darurat.", "サヤ シアプカン スディキッ ウアン トゥナイ ウントゥッ ダルラット", "事前準備 siapkan。"),
            ("その件はしばらくそのままにしておきましょう。", "Biarkan masalah itu untuk sementara.", "ビアルカン マサラ イトゥ ウントゥッ スムンタラ", "放置 biarkan。"),
            ("彼に前もって伝えておきました。", "Saya sudah mengabarinya terlebih dahulu.", "サヤ スダ ムンガバリニャ トゥルルビ ダフル", "事前 terlebih dahulu。"),
            ("ホテルをあらかじめ予約しておきます。", "Saya memesan hotel terlebih dahulu.", "サヤ メメサン ホテル トゥルルビ ダフル", "事前予約 terlebih dahulu。"),
            ("エアコンをつけたままにしておいて。", "Biarkan AC-nya tetap menyala.", "ビアルカン アーセーニャ トゥタップ メニャラ", "放置 biarkan tetap..."),
            ("出発前にトイレに行っておきなさい。", "Pergi ke toilet dulu sebelum berangkat.", "プルギ ク トイレット ドゥル スブルム ブルランカット", "先行 dulu。"),
            ("パスポートのコピーを取っておいた方がいい。", "Sebaiknya siapkan salinan paspor.", "スバイッニャ シアプカン サリナン パスポル", "事前準備 siapkan。"),
            ("料理を少し冷ましておきましょう。", "Biarkan makanannya agak dingin dulu.", "ビアルカン マカナンニャ アガッ ディンギン ドゥル", "放置・先行 biarkan... dulu。")
        ],
        "quiz": [
            ("「ドアを開けたままにしておいて（放置）」の自然な表現は？", ["Biarkan pintunya terbuka.", "Tolong taruh pintu buka.", "Simpan pintu buka.", "Bikin pintu terbuka."], 1),
            ("「先に食べておいて（先行）」を表す日常語は？", ["Makan duluan ya.", "Makan menaruh ya.", "Makan simpan ya.", "Makan buat ya."], 1),
            ("「事前に資料を準備しておく」を表す動詞は？", ["menyiapkan dokumen", "menaruh dokumen", "menyimpan dokumen", "membiarkan dokumen"], 1)
        ]
    },
    {
        "slug": "06-te-shimau-regret-accident",
        "title": "【誤用克服】「〜てしまう（後悔・完了）」の直訳ミス（terlanjur, keburu, sampai）",
        "intro": "日本語の「〜てしまう」は、①取り返しのつかない後悔（言ってしまった、買っちゃった）、②時間切れ・先を越される（バスが行ってしまった）、③完了（全部食べてしまった）を含みます。これらを terlanjur, keburu, habis で鮮やかに外科手術します。",
        "cases": [
            ("秘密をつい言ってしまった（取り返しがつかない）。", "Saya sudah bicara rahasia.", "Saya terlanjur membocorkan rahasianya.", "取り返しのつかない後悔には副詞 terlanjur（後の祭り・時すでに遅し）を使います。"),
            ("間に合わなくて電車が行ってしまった。", "Kereta pergi tidak sempat.", "Keretanya keburu berangkat.", "時間切れで手遅れになる「〜てしまう」は keburu を使います。")
        ],
        "drill": [
            ("もう買っちゃったよ（取り返しがつかない）。", "Sudah terlanjur saya beli.", "スダ トゥルランジュール サヤ ブリ", "後悔 terlanjur。"),
            ("急がないと、店が閉まっちゃうよ（時間切れ）。", "Cepat, nanti keburu tokonya tutup.", "チパット ナンティ クブル トコニャ トゥトゥップ", "時間切れ keburu。"),
            ("雨が降り出しちゃった（間に合わなかった）。", "Keburu hujan turun.", "クブル フジャン トゥルン", "先を越される keburu。"),
            ("ケーキを全部食べちゃった（完了）。", "Kuenya habis saya makan.", "クエニャ ハビス サヤ マカン", "食べ尽くす habis dimakan。"),
            ("言ってはいけないことをつい口走ってしまった。", "Saya terlanjur mengucapkan hal yang tidak boleh.", "サヤ トゥルランジュール ムングチャップカン ハル ヤン ティダッ ボレ", "失言 terlanjur。"),
            ("バスがもう出ちゃったよ。", "Busnya sudah keburu jalan.", "ブスニャ スダ クブル ジャラン", "先を越される keburu jalan。"),
            ("契約書にサインしちゃった後だった。", "Sudah terlanjur menandatangani kontrak.", "スダ トゥルランジュール ムナンダタンガニ コントラッ", "既成事実 terlanjur。"),
            ("夜更かしして朝になっちゃった。", "Begadang sampai tahu-tahu sudah pagi.", "ブガダン サンパイ タフタフ スダ パギ", "いつの間にか sampai..."),
            ("スマホを床に落としちゃった。", "Ponsel saya terjatuh ke lantai.", "ポンセル サヤ トゥルジャトゥ ク ランタイ", "不慮の事故 terjatuh。"),
            ("お金を使い果たしちゃった。", "Uang saya habis terpakai.", "ウアン サヤ ハビス トゥルパカイ", "使い果たす habis terpakai。"),
            ("映画がもう始まっちゃったよ。", "Filmnya sudah keburu mulai.", "フィルムニャ スダ クブル ムライ", "始まってしまった keburu mulai。"),
            ("怒りに任せて手紙を破っちゃった。", "Karena marah, terlanjur merobek surat itu.", "カルナ マラ トゥルランジュール メロベッ スラット イトゥ", "後悔 terlanjur merobek。"),
            ("スープを全部飲み干しちゃった。", "Supnya habis saya minum.", "スプニャ ハビス サヤ ミヌム", "完飲 habis。"),
            ("彼を好きになっちゃった。", "Saya terlanjur jatuh cinta kepadanya.", "サヤ トゥルランジュール ジャトゥ チンタ クパダニャ", "不可逆 terlanjur jatuh cinta。"),
            ("電車の中で居眠りしちゃった。", "Saya tertidur di dalam kereta.", "サヤ トゥルティドゥール ディ ダラム クレタ", "うっかり tertidur。")
        ],
        "quiz": [
            ("「取り返しがつかないことをしてしまった（後悔）」を表す副詞は？", ["terlanjur", "keburu", "habis", "sudah"], 1),
            ("「急がないとバスが出ちゃうよ（時間切れ手遅れ）」を表す副詞は？", ["keburu", "terlanjur", "terlalu", "belum"], 1),
            ("「全部食べ尽くしてしまった」を表す自然な形は？", ["Habis saya makan.", "Makan saya selesai.", "Sudah makan habis.", "Saya makan terlanjur."], 1)
        ]
    },
    {
        "slug": "07-indirect-politeness-clash",
        "title": "【誤用克服】「遠慮・遠回しな断り」が招く誤解と、インドネシア流の温かい断り方",
        "intro": "日本人の「行けたら行きます」「ちょっと都合が悪くて…」という曖昧・遠回しな断り文句は、インドネシアでは「本当は来るのか？」「失礼な嘘つき」と解釈され、重大な人間関係の摩擦を引き起こします。角を立てずに温かく断るインドネシア流の処方箋を伝授します。",
        "cases": [
            ("（パーティーに誘われて）行けたら行きます（本当は行かない）。", "Mungkin saya pergi kalau bisa.", "Maaf sekali, kali ini saya tidak bisa ikut karena ada acara lain.", "「行けたら行く」を直訳すると、相手は「来る」と期待して料理を用意してしまいます。断る時は最初に「Maaf sekali（本当にごめん）」と謝意を示し、行けない理由を添えるのが礼儀です。"),
            ("（商談の提案を断る時）検討させていただきます。", "Saya akan mempertimbangkannya.", "Usulannya sangat bagus, namun untuk saat ini kami belum bisa melanjutkan.", "ただ検討すると言うだけでなく、提案を一度褒めてから「現時点では見送る」と明確に伝えます。")
        ],
        "drill": [
            ("本当に申し訳ないのですが、今回は参加できません。", "Maaf sekali, kali ini saya tidak bisa ikut.", "マアフ スカリ カリ イニ サヤ ティダッ ビサ イクット", "温かい断り Maaf sekali..."),
            ("お誘いありがとうございます。ただ、あいにく先約がありまして。", "Terima kasih atas ajakannya, tapi sayang saya sudah ada janji lain.", "トゥリマ カシ アタス アジャカンニャ タピ サヤン サヤ スダ アダ ジャンジ ライン", "感謝＋理由 tapi sayang..."),
            ("素晴らしいご提案ですが、現時点では予算が足りません。", "Usulannya sangat menarik, tapi saat ini anggaran belum mencukupi.", "ウスランニャ サンガット ムナリッ タピ サアット イニ アンガラン ブロン ムンチュクピ", "褒めてから断る。"),
            ("ぜひ行きたかったのですが、体調が優れず残念です。", "Pengin banget ikut, tapi sayang badan lagi kurang fit.", "プンギン バンゲット イクット タピ サヤン バダン ラギ クラン フィット", "口語の温かい断り。"),
            ("お力になりたいのですが、私には権限がありません。", "Saya ingin sekali membantu, namun hal ini di luar wewenang saya.", "サヤ インギン スカリ メムバントゥ ナムン ハル イニ ディ ルアール ウェウェナン サヤ", "丁寧な辞退。"),
            ("また次の機会にぜひ誘ってくださいね。", "Lain kali ajak saya lagi ya.", "ライン カリ アジャッ サヤ ラギ ヤ", "前向きな結び Lain kali..."),
            ("せっかくのお心遣いですが、お腹がいっぱいです。", "Terima kasih banyak, tapi saya sudah sangat kenyang.", "トゥリマ カシ バニャッ タピ サヤ スダ サンガット クニャン", "食事の断り。"),
            ("今日はどうしても外せない用事があります。", "Hari ini ada keperluan mendesak yang tidak bisa ditinggal.", "ハリ イニ アダ クプルルアン ムンデサッ ヤン ティダッ ビサ ディティンガル", "明確な理由。"),
            ("ご期待に添えず、心苦しい限りです。", "Mohon maaf kami belum bisa memenuhi harapan Anda.", "モホン マアフ カミ ブロン ビサ メムヌヒ ハラパン アンダ", "ビジネス丁重。"),
            ("お気持ちだけありがたく頂戴いたします。", "Terima kasih atas niat baiknya, saya hargai sekali.", "トゥリマ カシ アタス ニカット バイッニャ サヤ ハルガイ スカリ", "好意への感謝。"),
            ("あいにく明日は一日中出張に出ております。", "Sayang sekali besok saya dinas luar seharian.", "サヤン スカリ ベソッ サヤ ディナス ルアール スハリアン", "不在の明示。"),
            ("今週は締め切りに追われていて時間が取れません。", "Minggu ini lagi dikejar tenggat waktu jadi belum sempat.", "ミング イニ ラギ ディクジャル トゥンガット ワクトゥ ジャディ ブロン スムパット", "多忙の理由。"),
            ("お話しできて光栄でしたが、そろそろ失礼しなければなりません。", "Senang mengobrol dengan Anda, tapi saya harus pamit sekarang.", "スナン ムンゴブロール ドゥンガン アンダ タピ サヤ ハルス パミット スカラン", "お暇の挨拶 pamit。"),
            ("私の一存では決めかねますので、持ち帰らせてください。", "Saya perlu mendiskusikannya dulu dengan tim.", "サヤ プルル ムンディスクシカンニャ ドゥル ドゥンガン ティム", "社内相談。"),
            ("また近いうちにランチでも行きましょう。", "Kapan-kapan kita makan siang bareng ya.", "カパンカパン キタ マカン シアン バレン ヤ", "親しい次回約束。")
        ],
        "quiz": [
            ("インドネシアで誘いを断る際の鉄則は？", ["「行けたら行く」と曖昧に濁す", "最初に感謝とお詫び（Maaf sekali）を述べ、理由を添えて温かく断る", "返事をせず無視する", "怒った顔で断る"], 2),
            ("「また別の機会に誘ってね」の定番フレーズは？", ["Lain kali ajak saya lagi ya.", "Jangan ajak saya lagi.", "Mungkin saya mau nanti.", "Tolak ajakan Anda."], 1),
            ("「お気持ちだけいただきます」を表す上品な表現は？", ["Terima kasih atas niat baiknya.", "Saya tidak mau barangnya.", "Ambil saja kembali.", "Jangan kasih saya."], 1)
        ]
    },
    {
        "slug": "08-ada-punya-confusion",
        "title": "【誤用克服】「持っている/ある」の混乱（Ada buku vs Punya buku vs Memiliki）",
        "intro": "日本語の「ある・いる・持っている」に対応する ada, punya, memiliki の混同は、初中級者の大定番です。「Ada mobil」と「Punya mobil」はどう違うのか？「Saya ada uang」と「Saya punya uang」の微妙な使い分けを整理します。",
        "cases": [
            ("私は車を持っています。", "Saya ada mobil.", "Saya punya mobil.", "法的な所有権や自分の所有物であることを述べる場合は punya を使います。「Saya ada mobil」と言うと「（今日使える）車がある・手元にある」という一時的ニュアンスになります。"),
            ("机の上にペンがあります。", "Punya pulpen di atas meja.", "Ada pulpen di atas meja.", "場所における物理的存在には ada を使い、punya は絶対に使えません。")
        ],
        "drill": [
            ("机の上に鍵があります（場所の存在）。", "Ada kunci di atas meja.", "アダ クンチ ディ アタス メジャ", "存在 ada。"),
            ("彼は高級車を2台持っています（所有）。", "Dia punya dua mobil mewah.", "ディア プニャ ドゥア モビル メワ", "所有 punya。"),
            ("今日、細かいお金持ってる？（手元にあるか）", "Ada uang kecil hari ini?", "アダ ウアン クチル ハリ イニ", "手元の有無 ada。"),
            ("私はまだパスポートを持っていません（未所持）。", "Saya belum punya paspor.", "サヤ ブロン プニャ パスポル", "所有 punya。"),
            ("会社は多数の特許を保有しています（公式所有）。", "Perusahaan memiliki banyak hak paten.", "プルサハアン メミリキ バニャッ ハッ パテン", "格調高い保有 memiliki。"),
            ("何か良い質問はありますか？", "Ada pertanyaan bagus?", "アダ プルタニャアン バグス", "存在 ada。"),
            ("彼はまだ子供がいません。", "Dia belum punya anak.", "ディア ブロン プニャ アナッ", "親族 punya。"),
            ("この部屋にはエアコンがありません。", "Tidak ada AC di kamar ini.", "ティダッ アダ アーセー ディ カマール イニ", "存在否定 tidak ada。"),
            ("彼女は広い人脈を持っています。", "Dia memiliki jaringan relasi yang luas.", "ディア メミリキ ジャリンガン レラシ ヤン ルアス", "保有 memiliki。"),
            ("時間ありますか？", "Ada waktu?", "アダ ワクトゥ", "余裕 ada waktu。"),
            ("私は自分の家を持っていません（借家暮らし）。", "Saya tidak punya rumah sendiri.", "サヤ ティダッ プニャ ルマ スンディリ", "所有 tidak punya。"),
            ("庭に大きな木があります。", "Ada pohon besar di halaman.", "アダ ポホン ブサール ディ ハラマン", "存在 ada。"),
            ("彼は豊かな経験を持っています。", "Dia memiliki pengalaman yang kaya.", "ディア メミリキ プンガラマン ヤン カヤ", "抽象保有 memiliki。"),
            ("何か手伝えることはありますか？", "Ada yang bisa saya bantu?", "アダ ヤン ビサ サヤ バントゥ", "存在 ada。"),
            ("兄は新しいバイクを持っています。", "Kakak punya motor baru.", "カカッ プニャ モトル バル", "所有 punya。")
        ],
        "quiz": [
            ("「机の上に本がある」の正しい文は？", ["Ada buku di atas meja.", "Punya buku di atas meja.", "Memiliki buku di atas meja.", "Adanya buku di atas meja."], 1),
            ("「彼は車を所有している」を表す最も適切な語は？", ["Dia punya mobil.", "Dia ada mobil di jalan.", "Dia tempat mobil.", "Dia menjadi mobil."], 1),
            ("公的文書・論文で「権利や資産を保有する」を表す格式高い動詞は？", ["memiliki", "punya", "ada", "dapat"], 1)
        ]
    },
    {
        "slug": "09-bisa-dapat-mampu-misuse",
        "title": "【誤用克服】「できる」の使い分けミス（能力の mampu, 状況の bisa, 許可の dapat）",
        "intro": "日本語の「できる」には、①個人の肉体的・経済的能力（mampu / sanggup）、②一般的な状況可能（bisa）、③公的・法的許可（dapat / boleh）の異なる次元があります。何でも bisa で済ませる癖を脱却し、正確なニュアンスを身につけます。",
        "cases": [
            ("彼は家を買う経済的余裕がない（買えない）。", "Dia tidak bisa beli rumah.", "Dia tidak mampu membeli rumah.", "お金や体力の限界で「〜できない」場合は mampu を使います。tidak bisa だと「買い方を知らない」「物理的に禁止されている」ようにも聞こえます。"),
            ("ここは駐車可能です（法・規則の許可）。", "Bisa parkir di sini.", "Dapat parkir di sini. / Boleh parkir di sini.", "公的な案内や許可には dapat / boleh が格調高く適合します。")
        ],
        "drill": [
            ("彼は車を買う経済的余裕があります。", "Dia mampu membeli mobil baru.", "ディア マンプ ムンブリ モビル バル", "経済的能力 mampu。"),
            ("私はインドネシア語を少し話せます。", "Saya bisa berbicara bahasa Indonesia sedikit.", "サヤ ビサ ブルビチャラ バハサ インドネシア スディキッ", "一般的習得能力 bisa。"),
            ("旅行者はビザなしで入国できます（制度的許可）。", "Wisatawan dapat masuk tanpa visa.", "ウィサタワン ダパット マスッ タンパ フィサ", "制度的可能 dapat。"),
            ("私は重い荷物を持ち上げられません（体力不足）。", "Saya tidak sanggup mengangkat beban berat ini.", "サヤ ティダッ サングップ ムナンカット ブバン プラット イニ", "体力限界 sanggup。"),
            ("明日、オフィスに来られますか？（スケジュール可能）", "Apakah Anda bisa datang ke kantor besok?", "アカパ アンダ ビサ ダタン ク カントール ベソッ", "状況可能 bisa。"),
            ("貧しい人々にも教育を受ける権利がある。", "Masyarakat kurang mampu berhak mendapat pendidikan.", "マシャラカット クラン マンプ ブルハッ ムンダパット プンディディカン", "経済階層 kurang mampu。"),
            ("このボタンを押せば、画面が起動します。", "Dengan menekan tombol ini, layar dapat menyala.", "ドゥンガン ムヌカン トンボル イニ ラヤール ダパット メニャラ", "機能可能 dapat。"),
            ("彼はその精神的プレッシャーに耐えきれなかった。", "Dia tidak sanggup menahan tekanan mental itu.", "ディア ティダッ サングップ メナハン トゥカナン メンタル イトゥ", "精神的限界 sanggup。"),
            ("彼女はピアノをとても上手に弾けます。", "Dia bisa bermain piano dengan sangat mahir.", "ディア ビサ ブルマイン ピアノ ドゥンガン サンガット マヒール", "技術可能 bisa。"),
            ("詳細情報はウェブサイトでご確認いただけます。", "Informasi lengkap dapat diakses di situs web.", "インフォルマシ ルンカップ ダパット ディアクセ ディ シトゥス ウェブ", "公的案内 dapat。"),
            ("私たちはこの危機を克服する能力がある。", "Kita mampu mengatasi krisis ini.", "キタ マンプ ムンガタシ クリシス イニ", "組織能力 mampu。"),
            ("ここでタバコを吸ってもいいですか？（許可）", "Boleh saya merokok di sini?", "ボレ サヤ ムロコッ ディ シニ", "許可 boleh。"),
            ("彼は泳ぐことができます（泳ぎ方を知っている）。", "Dia bisa berenang.", "ディア ビサ ブルナン", "一般的可能 bisa。"),
            ("学生は割引料金を利用できます。", "Mahasiswa dapat menikmati tarif diskon.", "マハシスワ ダパット メニクマティ タリフ ディスコン", "制度的特典 dapat。"),
            ("私はもうこれ以上走れません（体力限界）。", "Saya tidak sanggup berlari lagi.", "サヤ ティダッ サングップ ブルラリ ラギ", "体力限界 sanggup。")
        ],
        "quiz": [
            ("「家を買う金銭的余裕がある」を表す最適な助動詞は？", ["mampu", "bisa", "boleh", "boleh jadi"], 1),
            ("「体力・気力的に耐えきれない」を表す言葉は？", ["tidak sanggup", "tidak bisa", "tidak boleh", "tidak dapat"], 1),
            ("公式文書で「〜することが可能です」を表す格調高い語は？", ["dapat", "bisa", "sanggup", "sempat"], 1)
        ]
    },
    {
        "slug": "10-mau-akan-distinction",
        "title": "【誤用克服】「〜するつもり/〜だろう」の mau と akan の意志と未来の混同矯正",
        "intro": "日本語の「〜する」「〜でしょう」に対して、インドネシア語の「mau」は強い主観的意志・欲望（〜したい、〜する気だ）を含み、「akan」は客観的未来・予定（〜する予定だ、〜だろう）を示します。天候や客観的予測に mau を使ってしまう不自然さを矯正します。",
        "cases": [
            ("明日は雨が降るでしょう（天気予報）。", "Besok mau hujan.", "Besok akan hujan.", "雨自身に「降りたい」という意志はないため、客観的未来には akan を使います（ただし口語で「雨が降りそうだ」と空模様を見て言う mau hujan は例外的に使われますが、公式予測は akan です）。"),
            ("私は来年結婚するつもりです（強い意志）。", "Saya akan menikah tahun depan.", "Saya mau menikah tahun depan. / Saya berencana menikah.", "本人の意志・決意を強調する場合は mau または berencana を用います。")
        ],
        "drill": [
            ("明日の午後、雨が降るでしょう（客観的気象予測）。", "Besok sore akan turun hujan.", "ベソッ ソレ アカン トゥルン フジャン", "客観的未来 akan。"),
            ("私は新しい車を買うつもりです（本人の購入意志）。", "Saya mau membeli mobil baru.", "サヤ マウ ムンブリ モビル バル", "強い意志 mau。"),
            ("大統領は明日、日本を訪問する予定です（公式行事）。", "Presiden akan mengunjungi Jepang besok.", "プレシデン アカン ムングンジュンギ ジュパン ベソッ", "公式予定 akan。"),
            ("今夜、何が食べたい？（相手の欲求）", "Kamu mau makan apa malam ini?", "カム マウ マカン アパ マラム イニ", "欲求 mau。"),
            ("会議は間もなく開始されます（客観的時間経過）。", "Rapat akan segera dimulai.", "ラパット アカン スグラ ディムライ", "客観未来 akan。"),
            ("彼は仕事を辞めたがっている（本人の希望）。", "Dia mau berhenti dari pekerjaannya.", "ディア マウ ブルヘンティ ダリ プケルジャアンニャ", "主観意志 mau。"),
            ("新薬の効果は間もなく証明されるでしょう。", "Khasiat obat baru akan segera terbukti.", "カシアット オバット バル アカン スグラ トゥルブクティ", "客観的帰結 akan。"),
            ("コーヒーを飲みますか、紅茶にしますか？", "Mau minum kopi atau teh?", "マウ ミヌム コピ アタウ テ", "意志選択 mau。"),
            ("物価は来月さらに上昇する見込みです。", "Harga barang akan naik lagi bulan depan.", "ハルガ バラン アカン ナイク ラギ ブラン ドゥパン", "経済予測 akan。"),
            ("私たちは全力を尽くすつもりです。", "Kami mau berusaha sekuat tenaga.", "カミ マウ ブルウサハ スクアット トゥナガ", "決意 mau。"),
            ("結果は明日発表される予定です。", "Hasilnya akan diumumkan besok.", "ハシルニャ アカン ディウムムカン ベソッ", "公式予定 akan。"),
            ("もう帰るの？（相手の意志）", "Kamu sudah mau pulang?", "カム スダ マウ プラン", "意志確認 mau pulang?"),
            ("地球の気温は上昇し続けるだろう。", "Suhu bumi akan terus meningkat.", "スフ ブミ アカン トゥルス メニンカット", "科学的予測 akan。"),
            ("手伝ってくれる？（意志の確認）", "Kamu mau bantu saya?", "カム マウ バントゥ サヤ", "依頼意志 mau bantu?"),
            ("この法案は来週可決される見通しだ。", "RUU ini akan disahkan minggu depan.", "エルウーウー イニ アカン ディサハカン ミング ドゥパン", "公的未来 akan。")
        ],
        "quiz": [
            ("客観的な天気予報で「明日は晴れるでしょう」と言う時の助動詞は？", ["akan", "mau", "ingin", "hendak"], 1),
            ("相手に「何が飲みたい？」と希望を尋ねる時の助動詞は？", ["mau", "akan", "boleh", "harus"], 1),
            ("mau と akan の根本的な違いは？", ["mau は主観的意志・欲求、akan は客観的未来・予定", "mau は過去、akan は未来", "mau は否定文専用、akan は肯定文専用", "全く同じで違いはない"], 1)
        ]
    }
]

import os

for a in articles_data:
    filepath = os.path.join("docs/clinic", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. 症例カルテ（日本人特有の不自然な発話例）\n")
    for idx, (jp, bad, good, explanation) in enumerate(a['cases'], 1):
        lines.append(f"### 症例 {idx}: 「**{jp}**」")
        lines.append(f"- ❌ **不自然な直訳**: `{bad}`")
        lines.append(f"- ⭕ **自然なネイティブ表現**: `{good}`")
        lines.append(f"- **病因分析**: {explanation}\n")
    
    lines.append("## 2. 処方箋とパラダイムシフト\n")
    lines.append("日本語の発想（テンス・アスペクトの混同や授受表現の直訳）から脱却し、インドネシア語本来の語彙体系と構文を自然にマッピングするための思考ルールを身につけます。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 矯正リライトドリル（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語の文を見て、直訳の罠を避けて**自然なインドネシア語**を1〜2秒以内に口頭で発声してください。\n")
    
    for idx, (jp, id_sent, kana, exp) in enumerate(a['drill'], 1):
        lines.append(f"### 第{idx}問")
        lines.append(f"**日本語**: 「**{jp}**」\n")
        lines.append('<div class="id-example" markdown>\n')
        lines.append(f'<div class="id-sentence">\n{id_sent}\n</div>')
        lines.append(f'<div class="id-reading">\n{kana}\n</div>')
        lines.append(f'<div class="id-meaning">\n{jp}\n</div>')
        lines.append('</div>\n')
        lines.append(f"- **処方ポイント**: {exp}\n")
        lines.append("---\n")
        
    lines.append("## 4. 理解度チェッククイズ\n")
    for q_idx, (q_text, opts, ans_idx) in enumerate(a['quiz'], 1):
        lines.append(f"**Q{q_idx}. {q_text}**\n")
        for opt_idx, opt in enumerate(opts, 1):
            mark = " (正解)" if opt_idx == ans_idx else ""
            lines.append(f"- {opt_idx}. {opt}{mark}")
        lines.append("")
        
    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filepath}")

print("Batch 1051-1060 generated successfully.")
