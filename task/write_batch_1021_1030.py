"""Writer Script: Articles 1021 - 1030 for docs/output/
"""

articles_data = [
    {
        "slug": "21-prefix-ber-intransitive",
        "title": "【瞬間作文】接頭辞 ber- 自動詞・状態動詞の即時産出（berjalan, berbicara）",
        "intro": "接頭辞「ber-」は、主語自身が主体となって行う自動詞（berjalan: 歩く、berbicara: 話す）や、所有・身につける状態（berbaju: 服を着ている、berambut panjang: 髪が長い）を瞬時に形成します。能動他動詞 meN- と混同せず、目的語をとらない自律した動作を0.5秒で出力します。",
        "rules": [
            ("自発的動作の自動詞", "berjalan（歩く）、berlari（走る）、berenang（泳ぐ）、berhenti（止まる）。目的語を後ろに直接とりません。"),
            ("所有・装着の状態", "berbaju merah（赤い服を着ている）、bersepatu（靴を履いている）、beruang（金持ちだ：お金を持っている）。"),
            ("相互行為（互いに〜する）", "bertemu（会う）、berpisah（別れる）、bersalaman（握手し合う）。")
        ],
        "drill": [
            ("私たちは毎朝公園を歩きます。", "Kami berjalan di taman setiap pagi.", "カミ ブルジャラン ディ タマン スティアプ パギ", "自動詞 berjalan。"),
            ("彼は英語をとても上手に話します。", "Dia berbicara bahasa Inggris dengan sangat lancar.", "ディア ブルビチャラ バハサ イングリス ドゥンガン サンガット ランチャール", "自動詞 berbicara。"),
            ("子供たちはプールで泳いでいます。", "Anak-anak sedang berenang di kolam renang.", "アナッアナッ スダン ブルナン ディ コラム ルナン", "動作 berenang。"),
            ("その車は赤信号で止まりました。", "Mobil itu berhenti di lampu merah.", "モビル イトゥ ブルヘンティ ディ ランプ メラ", "停止 berhenti。"),
            ("彼女は白いドレスを着ています。", "Dia berbaju gaun putih.", "ディア ブルバジュ ガウン プティ", "装着 berbaju。"),
            ("彼らは昨日、駅で会いました。", "Mereka bertemu di stasiun kemarin.", "ムレカ ブルトゥム ディ スタシウン クマリン", "相互行為 bertemu。"),
            ("兄は病院で医者として働いています。", "Kakak bekerja sebagai dokter di rumah sakit.", "カカッ ブケルジャ スバガイ ドクテル ディ ルマ サキッ", "職業行動 bekerja。"),
            ("友達同士、固く握手しました。", "Sesama teman saling bersalaman dengan erat.", "スサマ トゥマン サリン ブルサラマン ドゥンガン エラット", "相互 bersalaman。"),
            ("彼女は長い黒髪をしています。", "Dia berambut hitam panjang.", "ディア ブルラムブット ヒタム パンジャン", "状態・特徴 berambut。"),
            ("私たちは来週バリ島で休暇を過ごします。", "Kami akan berlibur di Bali minggu depan.", "カミ アカン ブルリブール ディ バリ ミング ドゥパン", "休暇 berlibur。"),
            ("彼らは夜遅くまで議論しました。", "Mereka berdiskusi sampai larut malam.", "ムレカ ブルディスクシ サンパイ ラルット マラム", "議論 berdiskusi。"),
            ("学生たちは熱心に勉強しています。", "Para siswa sedang belajar dengan giat.", "パラ シスワ スダン ブラジャール ドゥンガン ギアット", "学習 belajar（ber-+ajar）。"),
            ("彼のバイクは黒い色をしています。", "Motornya berwarna hitam.", "モトルニャ ブルワルナ ヒタム", "色彩状態 berwarna。"),
            ("あの老人はとても裕福です（金を持っている）。", "Kakek itu sangat beruang.", "カケッ イトゥ サンガット ブルウアン", "所有 beruang。"),
            ("私たちは明日、空港で別れます。", "Kami akan berpisah di bandara besok.", "カミ アカン ブルピサ ディ バンダラ ベソッ", "別れ berpisah。")
        ],
        "quiz": [
            ("接頭辞 ber- 動詞の最大の特徴は？", ["直接の目的語をとらない自動詞になる", "必ず目的語が必要な他動詞になる", "受動態専用の動詞になる", "過去形専用の動詞になる"], 1),
            ("「赤い服を着ている」を表す動詞句は？", ["berbaju merah", "membaju merah", "terbaju merah", "dibaju merah"], 1),
            ("「駅で会う」を表す自然な表現は？", ["bertemu di stasiun", "menemukan di stasiun", "ditemu di stasiun", "tertemu di stasiun"], 1)
        ]
    },
    {
        "slug": "22-ber-vs-men-contrast",
        "title": "【瞬間作文】ber- と meN- の使い分け対比ドリル（berubah vs mengubah）",
        "intro": "同一の語根から ber-（自動詞・状態・自発）と meN-（他動詞・意図的行為）が派生するペアは、インドネシア語の最もダイナミックな語彙体系です。「何かが自然に変わる（berubah）」のか、「誰かが何かを変える（mengubah）」のかを瞬時に切り替えるドリルです。",
        "rules": [
            ("ber- は自動詞（主語自身が変わる）", "Situasi berubah（状況が変わる）、Dia bercukur（彼は髭を剃る：自分自身の髭）。"),
            ("meN- は他動詞（対象・目的語に働きかける）", "Dia mengubah rencana（彼は計画を変える）、Tukang cukur mencukur rambutnya（理髪師が彼の髪を刈る）。")
        ],
        "drill": [
            ("気候が急速に変化しています。", "Iklim berubah dengan cepat.", "イクリム ブルウバ ドゥンガン チパット", "自動詞 berubah。"),
            ("政府は新しい規則を変更しました。", "Pemerintah mengubah peraturan baru.", "プムリンタ ムングバ プラトゥラン バル", "他動詞 mengubah。"),
            ("私たちは新しい家に引っ越しました。", "Kami pindah ke rumah baru.", "カミ ピンダ ク ルマ バル", "自動詞 pindah / berpindah。"),
            ("彼は机を窓の近くに移動させました。", "Dia memindahkan meja ke dekat jendela.", "ディア メミンダカン メジャ ク ドゥカット ジュンデラ", "他動詞 memindahkan。"),
            ("木の枝が折れました。", "Ranting pohon patah.", "ランティン ポホン パタ", "自動詞 patah / berpatah。"),
            ("彼は定規を折ってしまいました。", "Dia mematahkan penggaris.", "ディア メマタカン プンガリス", "他動詞 mematahkan。"),
            ("彼女は鏡の前で髪を整えています。", "Dia berhias di depan cermin.", "ディア ブルヒアス ディ ドゥパン チュルミン", "再帰・自分 berhias。"),
            ("彼らは教室を花で飾り付けました。", "Mereka menghias ruang kelas dengan bunga.", "ムレカ ムンヒアス ルアン クラス ドゥンガン ブンガ", "他動詞 menghias。"),
            ("私たちは駅の前で集まりました。", "Kami berkumpul di depan stasiun.", "カミ ブルクンプル ディ ドゥパン スタシウン", "自動詞 berkumpul。"),
            ("先生は生徒たちを校庭に集めました。", "Guru mengumpulkan para siswa di lapangan.", "グル ムングンプルカン パラ シスワ ディ ラパンガン", "他動詞 mengumpulkan。"),
            ("空の色が青からオレンジに変わった。", "Warna langit berubah dari biru menjadi jingga.", "ワルナ ランギット ブルウバ ダリ ビル ムンジャディ ジンガ", "自動詞 berubah。"),
            ("社長は会社の戦略を変更した。", "Direktur mengubah strategi perusahaan.", "ディレクトゥール ムングバ ストラテギ プルサハアン", "他動詞 mengubah。"),
            ("二つの道路がここで交わります。", "Dua jalan ini bertemu di sini.", "ドゥア ジャラン イニ ブルトゥム ディ シニ", "自動詞 bertemu。"),
            ("私は昨日、古い手紙を発見しました。", "Saya kemarin menemukan surat lama.", "サヤ クマリン ムヌムカン スラット ラマ", "他動詞 menemukan。"),
            ("彼は毎朝髭を剃ります。", "Dia bercukur setiap pagi.", "ディア ブルチュクール スティアプ パギ", "自動詞（再帰）bercukur。")
        ],
        "quiz": [
            ("「状況が変わる」に適切な動詞は？ Situasi ___.", ["berubah", "mengubah", "diubah", "terubah"], 1),
            ("「計画を変更する」に適切な動詞は？ ___ rencana.", ["mengubah", "berubah", "terubah", "seubah"], 1),
            ("「生徒を集める」に適切な動詞は？ ___ siswa.", ["mengumpulkan", "berkumpul", "terkumpul", "kumpulan"], 1)
        ]
    },
    {
        "slug": "23-prefix-ter-accidental",
        "title": "【瞬間作文】接頭辞 ter- の無意識・偶発用法の瞬間作文（terbawa, tertidur）",
        "intro": "接頭辞「ter-」の代表的機能の一つが「無意識・偶発（うっかり〜してしまう、意図せず〜になる）」です。自分の意志ではなく事故や不可抗力で発生した事態を言い表す、インドネシア語特有の心理描写を瞬時に発話します。",
        "rules": [
            ("無意識・偶発の ter-", "tertidur（寝落ちする・うっかり眠る）、terbangun（ふと目が覚める）、terlupa（うっかり忘れる）、terbawa（うっかり持っていってしまう）。"),
            ("事故・突発の受動", "tertabrak（車に撥ねられる）、terinjak（踏まれる）、terjatuh（転ぶ・落ちる）。意志的受動 di- と違い「不慮の事故」のニュアンス。")
        ],
        "drill": [
            ("私はテレビを見ながら寝落ちしてしまいました。", "Saya tertidur saat menonton televisi.", "サヤ トゥルティドゥール サアット ムノントン テレフィシ", "無意識の寝落ち tertidur。"),
            ("夜中にふと目が覚めました。", "Saya terbangun di tengah malam.", "サヤ トゥルバングン ディ トゥンガ マラム", "突発的覚醒 terbangun。"),
            ("他人の傘をうっかり持ってきてしまいました。", "Payung orang lain terbawa oleh saya.", "パユン オラン ライン トゥルバワ オレ サヤ", "偶発の持参 terbawa。"),
            ("彼の名前をど忘れしてしまいました。", "Saya terlupa nama dia.", "サヤ トゥルルパ ナマ ディア", "うっかり忘却 terlupa。"),
            ("私の足が満員電車で踏まれました。", "Kaki saya terinjak di kereta yang penuh.", "カキ サヤ トゥルインジャッ ディ クレタ ヤン プヌ", "不慮の受難 terinjak。"),
            ("彼女は階段で足を滑らせて転びました。", "Dia terpeleset dan terjatuh di tangga.", "ディア トゥルプレセット ダン トゥルジャトゥ ディ タンガ", "偶発の転倒 terjatuh。"),
            ("スマホを家に置き忘れてきてしまいました。", "Ponsel saya tertinggal di rumah.", "ポンセル サヤ トゥルティンガル ディ ルマ", "うっかり放置 tertinggal。"),
            ("彼の秘密がつい口から漏れてしまった。", "Rahasianya terucap begitu saja.", "ラハシアニャ トゥルウチャップ ブギトゥ サジャ", "つい言ってしまう terucap。"),
            ("秘密の書類が風で飛ばされてしまった。", "Dokumen rahasia terbang terbawa angin.", "ドクメン ラハシア トゥルバン トゥルバワ アンギン", "不可抗力 terbawa angin。"),
            ("バイクがトラックに追突されてしまった。", "Motor tertabrak oleh truk.", "モトル トゥルタブラッ オレ トルック", "突発事故 tertabrak。"),
            ("私は彼の冗談につい笑ってしまった。", "Saya tertawa mendengar leluconnya.", "サヤ トゥルタワ ムンドンガル ルルチョンニャ", "思わず笑う tertawa。"),
            ("熱いお茶で舌をやけどしてしまった。", "Lidah saya terbakar teh panas.", "リダ サヤ トゥルバカール テ パナス", "不慮のやけど terbakar。"),
            ("指を包丁で切ってしまいました。", "Jari saya teriris pisau.", "ジャリ サヤ トゥルイリス ピサウ", "怪我 teriris。"),
            ("重要なメールをつい削除してしまった。", "Email penting terhapus oleh saya.", "イーメール ポンティン トゥルハプス オレ サヤ", "誤削除 terhapus。"),
            ("会議中に居眠りしてしまった。", "Saya terkantuk-kantuk dalam rapat.", "サヤ トゥルカントゥッカントゥッ ダラム ラパット", "うとうとする terkantuk。")
        ],
        "quiz": [
            ("「うっかり眠ってしまう（寝落ち）」を表す動詞は？", ["tertidur", "meniduri", "ditidurkan", "bertidur"], 1),
            ("「車に撥ねられる（不慮の事故）」を表す受動態は？", ["tertabrak", "menabrak", "ditabrakkan", "bertabrak"], 1),
            ("「傘をうっかり持ってきてしまった」を表す語句は？", ["terbawa", "membawa", "dibawakan", "berbawa"], 1)
        ]
    },
    {
        "slug": "24-prefix-ter-potential",
        "title": "【瞬間作文】接頭辞 ter- の可能・不可能否定（tidak terhitung, terjangkau）",
        "intro": "接頭辞「ter-」のもう一つの極めて重要な機能は「可能（〜できる）」、特に否定詞 tidak とセットになった「不可能（〜しきれない）」の表現です。tidak terhitung（数え切れない）、terjangkau（手が届く・手頃な）などの必須語句を反射生成します。",
        "rules": [
            ("肯定の可能（〜できる・〜の手が届く）", "terjangkau（手が届く・購入できる）、terbaca（読める・判読できる）。"),
            ("否定の不可能（tidak / tak ter- ＝ 〜しきれない）", "tidak terhitung（数え切れない）、tidak tertahankan（耐えられない）、tidak ternilai（値段がつけられないほど貴重な）、tidak terduga（予期できない）。")
        ],
        "drill": [
            ("このホテルの宿泊費はとても手頃です（手が届く）。", "Tarif hotel ini sangat terjangkau.", "タリフ ホテル イニ サンガット トゥルジャンカウ", "可能 terjangkau（jangkau=届く）。"),
            ("夜空には数え切れない星があります。", "Ada bintang yang tidak terhitung di langit malam.", "アダ ビンタン ヤン ティダッ トゥルヒトゥン ディ ランギット マラム", "不可能 tidak terhitung（数え切れない）。"),
            ("彼の字は汚くて読めません。", "Tulisannya tidak terbaca karena jelek.", "トゥリサンニャ ティダッ トゥルバチャ カルナ ジュレッ", "不可能 tidak terbaca（読めない）。"),
            ("歯の痛みが耐えられません。", "Sakit gigi ini tidak tertahankan.", "サキッ ギギ イニ ティダッ トゥルタハンカン", "不可能 tidak tertahankan（耐えられない）。"),
            ("この絵画は計り知れない価値があります（値がつかない）。", "Lukisan ini bernilai tak ternilai.", "ルキサン イニ ブルニライ タッ トゥルニライ", "最高評価 tak ternilai。"),
            ("昨日の地震は全く予期していませんでした。", "Gempa kemarin terjadi secara tidak terduga.", "グムパ クマリン トゥルジャディ スチャラ ティダッ トゥルドゥガ", "想定外 tidak terduga。"),
            ("この本は子供でも理解できます。", "Buku ini terpahami bahkan oleh anak-anak.", "ブク イニ トゥルパハミ バッカン オレ アナッアナッ", "可能 terpahami。"),
            ("彼の悲しみは言葉では言い表せません。", "Kesedihannya tidak terkatakan dengan kata-kata.", "クセディハンニャ ティダッ トゥルカタカン ドゥンガン カタカタ", "不可能 tidak terkatakan。"),
            ("スマートフォンの値段が安くて手が届きやすい。", "Harga ponselnya murah dan terjangkau.", "ハルガ ポンセルニャ ムラ ダン トゥルジャンカウ", "手頃 terjangkau。"),
            ("その噂の真偽は証明できません。", "Kebenaran rumor itu tidak terbukti.", "クブナラン ルモール イトゥ ティダッ トゥルブクティ", "証明不能 tidak terbukti。"),
            ("富士山の頂上からの景色は息を呑む美しさでした。", "Pemandangan dari puncak tidak terlukiskan indahnya.", "プマンダンガン ダリ プンチャッ ティダッ トゥルルキスカン インダニャ", "描写不能 tidak terlukiskan。"),
            ("彼の親切には感謝してもしきれません。", "Kebaikannya tidak terbalaskan.", "クバイカンニャ ティダッ トゥルバラスカン", "報いきれない tidak terbalaskan。"),
            ("その目標は私たちの能力で達成可能です。", "Target itu tercapai dengan kemampuan kita.", "ターゲット イトゥ トゥルチャパイ ドゥンガン クマンプアン キタ", "達成可能 tercapai。"),
            ("彼の声は小さすぎて聞こえませんでした。", "Suaranya terlalu pelan sehingga tidak terdengar.", "スアラニャ トゥルラル プラン スヒンガ ティダッ トゥルドンガル", "不可聴 tidak terdengar。"),
            ("この課題は今日中に解決可能です。", "Tugas ini terselesaikan hari ini.", "トゥガス イニ トゥルスルサイカン ハリ イニ", "完了可能 terselesaikan。")
        ],
        "quiz": [
            ("価格が「手頃である（手が届く）」を表す頻出語は？", ["terjangkau", "terhitung", "terbaca", "terdengar"], 1),
            ("「数え切れないほど多い」を表す表現は？", ["tidak terhitung", "tidak terbaca", "tidak terduga", "tidak tercapai"], 1),
            ("「言葉では言い表せない」を表すフレーズは？", ["tidak terkatakan", "tidak tertulis", "tidak terdengar", "tidak tercium"], 1)
        ]
    },
    {
        "slug": "25-prefix-ter-superlative",
        "title": "【瞬間作文】接頭辞 ter- の最上級表現の瞬間生成（terbaik, terbesar）",
        "intro": "形容詞の語頭に接頭辞「ter-」をつけると、「最も〜（最上級）」を1単語でエレガントに表現できます。paling besar よりも簡潔で格調高い terbaik, terbesar, tertinggi などを反射出力します。",
        "rules": [
            ("ter- ＋ 形容詞 ＝ 最上級", "terbaik（最高・一番良い）、terbesar（最大）、terkecil（最小）、tertinggi（最高度・最高峰）、termahal（最も高価な）、termurah（最も安価な）。"),
            ("修飾位置の原則", "名詞の「後ろ」に置きます。produk terbaik（最高の製品）、gunung tertinggi（最も高い山）。")
        ],
        "drill": [
            ("これはこの店で一番美味しい料理です。", "Ini makanan terlezat di restoran ini.", "イニ マカナン トゥルルザット ディ レストラン イニ", "最上級 terlezat。"),
            ("彼がクラスで一番背が高い少年です。", "Dia anak laki-laki tertinggi di kelas.", "ディア アナッ ラキラキ トゥルティンギ ディ クラス", "最上級 tertinggi。"),
            ("世界最大の島国インドネシア。", "Indonesia adalah negara kepulauan terbesar di dunia.", "インドネシア アダラ ネガラ クプラウアン トゥルブサール ディ ドゥニア", "最大 terbesar。"),
            ("最善を尽くしてください。", "Lakukan yang terbaik.", "ラクカン ヤン トゥルバイッ", "最善 yang terbaik。"),
            ("これが市場で最も安い果物です。", "Ini buah termurah di pasar.", "イニ ブア トゥルムラ ディ パサール", "最安 termurah。"),
            ("最も重要なことは諦めないことです。", "Hal terpenting adalah tidak menyerah.", "ハル トゥルポンティン アダラ ティダッ ムニェラ", "最重要 hal terpenting。"),
            ("ジャカルタで最も古い建物のひとつ。", "Salah satu gedung tertua di Jakarta.", "サラ サトゥ グドゥン トゥルトゥア ディ ジャカルタ", "最古 tertua。"),
            ("この大学で最も優秀な学生。", "Mahasiswa terpandai di universitas ini.", "マハシスワ トゥルパンダイ ディ ユニヴェルシタス イニ", "最優秀 terpandai。"),
            ("最新のニュースをお伝えします。", "Kami sampaikan berita terkini.", "カミ サンパイカン ブリタ トゥルキニ", "最新 terkini。"),
            ("最も近い病院はどこですか？", "Di mana rumah sakit terdekat?", "ディ マナ ルマ サキッ トゥルドゥカット", "最近 terdekat。"),
            ("人生で最も幸せな瞬間。", "Momen terbahagia dalam hidup.", "モメン トゥルバハギア ダラム ヒドゥップ", "最幸 terbahagia。"),
            ("世界で最も高価なコーヒー、ルワックコーヒー。", "Kopi termahal di dunia, kopi luwak.", "コピ トゥルマハル ディ ドゥニア コピ ルワック", "最高価 termahal。"),
            ("世界で最も速い新幹線。", "Kereta peluru tercepat di dunia.", "クレタ プルル トゥルチパット ディ ドゥニア", "最速 tercepat。"),
            ("彼が家族の中で一番若い末っ子です。", "Dia anak termuda dalam keluarga.", "ディア アナッ トゥルムダ ダラム クルアルガ", "最年少 termuda。"),
            ("最も愛する人への贈り物。", "Hadiah untuk orang tercinta.", "ハディア ウントゥッ オラン トゥルチンタ", "最愛 tercinta。")
        ],
        "quiz": [
            ("「最高の、最も良い」を表す接頭辞 ter- の単語は？", ["terbaik", "terbagus", "terindah", "tercocok"], 1),
            ("「最も近い病院」の語順は？", ["rumah sakit terdekat", "terdekat rumah sakit", "rumah terdekat sakit", "sakit terdekat rumah"], 1),
            ("「最新のニュース」の表現は？", ["berita terkini", "berita terlama", "berita termurah", "berita terluas"], 1)
        ]
    },
    {
        "slug": "26-suffix-kan-causative-base",
        "title": "【瞬間作文】接尾辞 -kan の使役構文（membersihkan, membesarkan）",
        "intro": "接尾辞「-kan」の最も中心的な機能が「使役（〜に…させる、〜を…の状態にする）」です。形容詞や動詞の語根に -kan をつけることで、他動詞として対象をその状態へ導く表現を瞬時に組み立てます。",
        "rules": [
            ("形容詞語根 ＋ -kan（〜の状態にする）", "bersih（清潔な）→ membersihkan（掃除する・清潔にする）、besar（大きい）→ membesarkan（大きくする・育てる）、panas（熱い）→ memanaskan（温める）。"),
            ("自動詞語根 ＋ -kan（〜を行動させる・行かせる）", "masuk（入る）→ memasukkan（中に入れる）、bangun（起きる）→ membangunkan（起こす）、turun（下りる）→ menurunkan（降ろす）。")
        ],
        "drill": [
            ("母は部屋を掃除しています。", "Ibu sedang membersihkan kamar.", "イブ スダン ムンブルシカン カマール", "使役 membersihkan（bersih=綺麗）。"),
            ("彼はスープを温め直しました。", "Dia memanaskan kembali supnya.", "ディア メマナスカン クンバリ スプニャ", "使役 memanaskan（panas=熱い）。"),
            ("朝7時に私を起こしてください。", "Tolong bangunkan saya jam tujuh pagi.", "トロン バングンカン サヤ ジャム トゥジュ パギ", "使役 bangunkan（bangun=起きる）。"),
            ("荷物を車の中に入れてください。", "Tolong masukkan barang ke dalam mobil.", "トロン マスッカン バラン ク ダラム モビル", "使役 masukkan（masuk=入る）。"),
            ("運転手さん、あの角で私を降ろしてください。", "Pak sopir, tolong turunkan saya di tikungan itu.", "パッ ソピル トロン トゥルンカン サヤ ディ ティクンガン イトゥ", "使役 turunkan（turun=下りる）。"),
            ("両親は私たちを愛情を込めて育ててくれた。", "Orang tua membesarkan kami dengan penuh kasih sayang.", "オラン トゥア ムンブサールカン カミ ドゥンガン プヌ カシ サヤン", "使役 membesarkan（besar=大きい）。"),
            ("彼はパソコンの音量を小さくしました。", "Dia mengecilkan volume komputer.", "ディア ムンゲチルカン フォルメ コンピューテル", "使役 mengecilkan（kecil=小さい）。"),
            ("先生は生徒たちに規則を明確に説明しました。", "Guru menjelaskan aturan kepada para siswa.", "グル ムンジュラスカン アトゥラン クパダ パラ シスワ", "使役 menjelaskan（jelas=明確な）。"),
            ("彼女は部屋を暗くするために電気を消した。", "Dia mematikan lampu untuk menggelapkan ruangan.", "ディア メマティカン ランプ ウントゥッ ムンゲラップカン ルアンガン", "使役 menggelapkan（gelap=暗い）。"),
            ("社長は新しいプロジェクトを立ち上げた。", "Direktur menjalankan proyek baru.", "ディレクトゥール ムンジャランカン プロイェッ バル", "使役 menjalankan（jalan=進む）。"),
            ("彼は壊れた椅子を直しました。", "Dia membetulkan kursi yang rusak.", "ディア ムンベトゥルカン クルシ ヤン ルサッ", "使役 membetulkan（betul=正しい）。"),
            ("スピードを落としてください（速度を遅くする）。", "Tolong lambatkan kecepatan kendaraan.", "トロン ランバットカン クチパタン クンダラアン", "使役 lambatkan（lambat=遅い）。"),
            ("政府は市民の生活を豊かにするために努めています。", "Pemerintah berupaya memakmurkan rakyat.", "プムリンタ ブルウパヤ メマクムルカン ラクヤット", "使役 memakmurkan（makmur=繁栄）。"),
            ("彼はスーツケースを上に持ち上げました。", "Dia menaikkan koper ke atas.", "ディア メナイッカン コペル ク アタス", "使役 menaikkan（naik=上がる）。"),
            ("深呼吸をして、心を落ち着かせなさい。", "Tarik napas dalam dan tenangkan pikiranmu.", "タリッ ナパス ダラム ダン トゥナンカン ピキランム", "使役 tenangkan（tenang=落ち着いた）。")
        ],
        "quiz": [
            ("形容詞 bersih（清潔な）に -kan をつけて「掃除する」にする動詞は？", ["membersihkan", "berbersih", "terbersih", "kebersihan"], 1),
            ("「私を降ろしてください」の命令形動詞は？", ["Turunkan saya", "Naikkan saya", "Masukkkan saya", "Bangunkan saya"], 1),
            ("「音量を小さくする」を表す動詞は？", ["mengecilkan", "membesarkan", "memanaskan", "menjauhkkan"], 1)
        ]
    },
    {
        "slug": "27-suffix-kan-benefactive",
        "title": "【瞬間作文】接尾辞 -kan の受益構文（membuatkan, membelikan kopi）",
        "intro": "接尾辞「-kan」のもう一つの極めて重要で温かい機能が「受益（〜のために…してあげる・してくれる）」です。日本語の「買ってあげる」「作ってあげる」を memberi で直訳せず、membuatkan kopi（コーヒーを淹れてあげる）とサラリと言える構文力を鍛えます。",
        "rules": [
            ("受益構文の語順公式", "【主語 ＋ 動詞-kan ＋ 受益者（人） ＋ 目的物】。Saya membelikan adik buku（私は妹に本を買ってあげた）。"),
            ("前置詞 untuk を使う言い換え", "【主語 ＋ 動詞 ＋ 目的物 ＋ untuk ＋ 受益者】。Saya membeli buku untuk adik。-kan 構文の方が口語でスマートです。")
        ],
        "drill": [
            ("父は私に新しい自転車を買ってくれました。", "Ayah membelikan saya sepeda baru.", "アヤ ムンブリカン サヤ スペダ バル", "受益 membelikan [人] [物]。"),
            ("母は私たちに美味しいケーキを作ってくれました。", "Ibu membuatkan kami kue yang lezat.", "イブ ムンブアットカン カミ クエ ヤン ルザット", "受益 membuatkan [人] [物]。"),
            ("温かい紅茶を淹れてあげましょうか？", "Mau saya buatkan teh hangat?", "マウ サヤ ブアットカン テ ハンガット", "親切の申し出 Mau saya buatkan...?"),
            ("彼はお客さんにドアを開けてあげました。", "Dia membukakan pintu untuk tamu.", "ディア ムンブカカン ピントゥ ウントゥッ タム", "受益 membukakan。"),
            ("タクシーを呼んで差し上げましょうか？", "Boleh saya carikan taksi?", "ボレ サヤ チャリカン タクシ", "親切 carikan taksi。"),
            ("彼は友達に部屋を借りてあげた。", "Dia menyewakan kamar untuk temannya.", "ディア ムニェワカン カマール ウントゥッ トゥマンニャ", "受益 menyewakan。"),
            ("彼女は妹にお気に入りの服を選んであげた。", "Dia memilihkan baju favorit untuk adiknya.", "ディア メミリカン バジュ ファフォリット ウントゥッ アディッニャ", "受益 memilihkan。"),
            ("私にお水を一杯取ってきていただけますか？", "Bisa ambilkan saya segelas air?", "ビサ アンビルカン サヤ スグラス アイル", "依頼 Bisa ambilkan saya...?"),
            ("祖父は私たちに昔話を聞かせてくれました。", "Kakek menceritakan kami dongeng lama.", "カケッ ムンチュリタカン カミ ドンゲン ラマ", "伝達・受益 menceritakan。"),
            ("先生は学生に推薦状を書いてあげた。", "Guru menuliskan surat rekomendasi untuk siswa.", "グル ムヌリスカン スラット レコメンダシ ウントゥッ シスワ", "受益 menuliskan。"),
            ("彼は病気の同僚にお粥を煮てあげた。", "Dia memasakkan bubur untuk rekannya yang sakit.", "ディア メマサッカン ブブール ウントゥッ レカンニャ ヤン サキッ", "受益 memasakkan。"),
            ("荷物を持ってあげましょうか？", "Biar saya bawakan barangnya?", "ビアル サヤ バワカン バランニャ", "親切の申し出 Biar saya bawakan...?"),
            ("彼らは子供たちに新しい服を縫ってあげた。", "Mereka menjahitkan baju baru untuk anak-anak.", "ムレカ ムンジャヒッカン バジュ バル ウントゥッ アナッアナッ", "受益 menjahitkan。"),
            ("ホテルを予約してあげましょうか？", "Mau saya pesankan hotel?", "マウ サヤ プサンカン ホテル", "手配 pesankan。"),
            ("彼にお金を貸してあげなさい。", "Pinjamkan uang kepadanya.", "ピンジャムカン ウアン クパダニャ", "貸与 pinjamkan。")
        ],
        "quiz": [
            ("「私にコーヒーを淹れてくれる？」の最も自然な表現は？", ["Bisa buatkan saya kopi?", "Bisa memberi saya kopi buat?", "Bisa membuat kopi saya?", "Bisa berikan saya kopi?"], 1),
            ("動詞 beli（買う）に受益の -kan がついた形は？", ["membelikan", "membeli-beli", "terbeli", "berbeli"], 1),
            ("「荷物を持ってあげましょうか？」のフレーズは？", ["Biar saya bawakan barangnya?", "Biar saya dibawakan barangnya?", "Barangnya bawa saya?", "Bawa saya barangnya?"], 1)
        ]
    },
    {
        "slug": "28-suffix-kan-instrumental",
        "title": "【瞬間作文】接尾辞 -kan の道具・対象移動構文（melemparkan batu）",
        "intro": "接尾辞「-kan」の3番目の機能は「道具・対象の移動（目的語そのものをどこかへ移動・投擲・接触させる）」です。「石を投げる（melemparkan batu）」や「荷物を車に積む（memasukkan barang）」など、空間的な運動を表す表現を瞬時に出力します。",
        "rules": [
            ("移動・投擲の -kan", "melemparkan batu（石を投げる：batuが移動する）、menerbangkan layang-layang（凧を飛ばす）。"),
            ("-i との決定的対比", "melemparkan batu ke anjing（石を犬に向かって投げる：移動するのは石） vs melempari anjing dengan batu（犬に石を投げつける：動作の対象・場所は犬）。")
        ],
        "drill": [
            ("少年は川に石を投げ入れました。", "Anak laki-laki itu melemparkan batu ke sungai.", "アナッ ラキラキ イトゥ ムルンパルカン バトゥ ク スンガイ", "移動 melemparkan batu（石を投げる）。"),
            ("子供たちは広場で凧を飛ばしています。", "Anak-anak menerbangkan layang-layang di lapangan.", "アナッアナッ ムヌルバンカン ラヤンラヤン ディ ラパンガン", "移動 menerbangkan（飛ばす）。"),
            ("彼はコートをベッドの上に放り出しました。", "Dia mencampakkan mantel ke atas ranjang.", "ディア ムンチャンパッカン マンテル ク アタス ランジャン", "投擲 mencampakkan。"),
            ("兵士たちは国旗をポールに掲揚しました。", "Para prajurit menaikkan bendera di tiang.", "パラ プラジュリット メナイッカン ブンデラ ディ ティアン", "移動・掲揚 menaikkan bendera。"),
            ("船員たちは救命ボートを海に降ろしました。", "Para pelaut menurunkan sekoci ke laut.", "パラ プラウット ムヌルンカン スコチ ク ラウット", "移動 menurunkan。"),
            ("彼は視線を窓の外に向けました。", "Dia mengarahkan pandangannya ke luar jendela.", "ディア ムンガラッカン パンダンガンニャ ク ルアール ジュンデラ", "移動・指向 mengarahkan。"),
            ("鳥は空高く翼を羽ばたかせました。", "Burung mengepakkan sayapnya tinggi di angkasa.", "ブルン ムンゲパッカン サヤップニャ ティンギ ディ アンカサ", "運動 mengepakkan。"),
            ("彼はボールをゴールに向かって蹴り込みました。", "Dia menendangkan bola ke arah gawang.", "ディア ムヌンダンカン ボラ ク アラ ガワン", "移動 menendangkan bola。"),
            ("彼女は花束を客席に投げました。", "Dia melemparkan buket bunga ke arah penonton.", "ディア ムルンパルカン ブケット ブンガ ク アラ プノントン", "投擲 melemparkan。"),
            ("彼はタバコの灰を灰皿に落としました。", "Dia menjatuhkan abu rokok ke asbak.", "ディア ムンジャトゥカン アブ ロコッ ク アスバッ", "落下 menjatuhkan。"),
            ("彼らは重い荷物をトラックの荷台に載せました。", "Dia menaikkan barang berat ke bak truk.", "ディア メナイッカン バラン プラット ク バッ トルック", "積載 menaikkan。"),
            ("彼は書類を机の引き出しに押し込みました。", "Dia memasukkan dokumen ke dalam laci meja.", "ディア マスッカン ドクメン ク ダラム ラチ メジャ", "挿入 memasukkan。"),
            ("彼はナイフを床に落としてしまいました。", "Dia menjatuhkan pisau ke lantai.", "ディア ムンジャトゥカン ピサウ ク ランタイ", "落下 menjatuhkan。"),
            ("風が落ち葉を遠くへ吹き飛ばしました。", "Angin menerbangkan dedaunan kering ke kejauhan.", "アンギン ムヌルバンカン デダウナン クリン ク クジャウハン", "飛散 menerbangkan。"),
            ("彼はロープを対岸に向かって投げ渡しました。", "Dia melemparkan tali ke seberang sungai.", "ディア ムルンパルカン タリ ク スブラン スンガイ", "投擲 melemparkan tali。")
        ],
        "quiz": [
            ("「石を投げる（石が移動する）」を表す文は？", ["Dia melemparkan batu.", "Dia melempari batu.", "Dia berlempar batu.", "Dia terlempar batu."], 1),
            ("「凧を空へ飛ばす」の正しい動詞は？", ["menerbangkan", "menerbangi", "berterbang", "deterbangkan"], 1),
            ("「荷物を車に積み込む（移動させる）」の動詞は？", ["memasukkan", "memasuki", "bermasuk", "termasuk"], 1)
        ]
    },
    {
        "slug": "29-suffix-i-locative",
        "title": "【瞬間作文】接尾辞 -i の場所・方向への作用構文（mendatangi, menaiki）",
        "intro": "接尾辞「-i」は、前置詞（di, ke）の機能を動詞の中に内包し、「ある場所・対象に向かって直接働きかける（場所性・対象性）」他動詞を作ります。「datang ke（〜へ来る）」を「mendatangi（〜を訪れる）」へと洗練させるドリルです。",
        "rules": [
            ("前置詞内包の -i", "datang ke rumah → mendatangi rumah（家を訪れる）、duduk di kursi → menduduki kursi（椅子に座る・占領する）、naik ke tangga → menaiki tangga（階段を登る）。"),
            ("目的語が「静止した場所・対象」", "動作が向かう場所や人が直接の目的語になります。Buku ini dia kirimi surat（彼に手紙を送る）。")
        ],
        "drill": [
            ("社長は支店を訪問しました。", "Direktur mendatangi kantor cabang.", "ディレクトゥール ムンダタンギ カントール チャバン", "場所 mendatangi（datang ke）。"),
            ("彼は馬に跨って山を登りました。", "Dia menaiki kuda dan mendaki gunung.", "ディア メナイキ クダ ダン ムンダキ グヌン", "対象 menaiki（naik ke）。"),
            ("学生たちは会議室に入りました。", "Para mahasiswa memasuki ruang rapat.", "パラ マハシスワ メマスキ ルアン ラパット", "場所 memasuki（masuk ke）。"),
            ("彼らは敵の陣地を占領しました。", "Mereka menduduki markas musuh.", "ムレカ ムンドゥドゥキ マルカス ムスフ", "場所 menduduki（duduk di）。"),
            ("彼女は毎朝庭の花に水をやります。", "Dia menyirami bunga-bunga di taman setiap pagi.", "ディア ムニィラミ ブンガブンガ ディ タマン スティアプ パギ", "対象 menyirami（siram ke）。"),
            ("私は病院へ行って友人を訪ねました。", "Saya mendatangi rumah sakit untuk menjenguk teman.", "サヤ ムンダタンギ ルマ サキッ ウントゥッ ムンジェングッ トゥマン", "訪問 mendatangi。"),
            ("警察は事故現場に駆けつけました。", "Polisi mendatangi lokasi kecelakaan.", "ポリシ ムンダタンギ ロカシ クチュラカアン", "急行 mendatangi。"),
            ("彼は古い城の階段を一歩一歩登りました。", "Dia menaiki tangga kastil tua selangkah demi selangkah.", "ディア メナイキ タンガ カスティル トゥア スランカ ドゥミ スランカ", "昇降 menaiki。"),
            ("鳥たちが庭の木に留まりました。", "Burung-burung menghinggapi pohon di halaman.", "ブルンブルン ムンヒンガピ ポホン ディ ハラマン", "着地 menghinggapi。"),
            ("大雨が街を水浸しにしました。", "Hujan lebat menggenangi jalanan kota.", "フジャン ルバット ムンゲナンギ ジャラナン コタ", "冠水 menggenangi。"),
            ("私たちは神の恵みに浴しています。", "Kita melimpahi rasa syukur atas berkah Tuhan.", "キタ ムリンパヒ ラサ シュクール アタス ブルカ トゥハン", "付与 melimpahi。"),
            ("彼は手紙にサインをして印鑑を押しました。", "Dia menandatangani dan mencapi surat itu.", "ディア ムナンダタンガニ ダン ムンチャピ スラット イトゥ", "署名 menandatangani。"),
            ("彼はお母さんの額にキスをしました。", "Dia menciumi kening ibunya.", "ディア ムンチュウミ クニン イブニャ", "対象 menciumi。"),
            ("太陽の光が部屋を明るく照らしました。", "Sinar matahari menyinari seluruh kamar.", "シナル マタハリ ムニィナリ スルルー カマール", "照射 menyinari。"),
            ("その噂が彼の心を不安で満たしました。", "Rumor itu menghantui pikirannya.", "ルモール イトゥ ムンハントゥイ ピキランニャ", "憑依 menghantui。")
        ],
        "quiz": [
            ("「場所を訪れる（datang ke）」を -i 動詞にすると？", ["mendatangi", "mendatangkan", "berdatang", "terdatang"], 1),
            ("「階段を登る（naik ke tangga）」を -i 動詞にすると？", ["menaiki tangga", "menaikkan tangga", "bernaik tangga", "ternaik tangga"], 1),
            ("「花に水をやる（水をかける）」を表す動詞は？", ["menyirami bunga", "menyiramkan bunga", "tersiram bunga", "bersiram bunga"], 1)
        ]
    },
    {
        "slug": "30-suffix-i-repetitive",
        "title": "【瞬間作文】接尾辞 -i の反復・複数対象構文（memukuli, menciumi）",
        "intro": "接尾辞「-i」のもう一つの極めて特徴的な用法が「動作の反復（何度も繰り返す）」および「複数の対象への連続的適用」です。1回の動作 memukul（殴る）に対して、何度もボコボコに殴る memukuli のような生々しい動作描写を反射出力します。",
        "rules": [
            ("反復・継続の -i（何度も繰り返す）", "memukul（1回殴る）→ memukuli（何度も殴り続ける）、mencium（1回キスする）→ menciumi（何度もキスしまくる）、melempar（1回投げる）→ melempari（何度も投げつける）。"),
            ("複数対象への動作（あちこちに〜する）", "mengambil（取る）→ mengambili（あちこちから次々と拾い集める）、mencabuti（草を何本も抜きまくる）。")
        ],
        "drill": [
            ("彼は怒って机を何度も叩いた。", "Dia memukuli meja karena marah.", "ディア メムクリ メジャ カルナ マラ", "反復 memukuli。"),
            ("母は愛おしそうに赤ちゃんの頬に何度もキスをした。", "Ibu menciumi pipi bayinya dengan penuh kasih sayang.", "イブ ムンチュウミ ピピ バイニャ ドゥンガン プヌ カシ サヤン", "反復 menciumi。"),
            ("群衆は泥棒に石を何度も投げつけた。", "Massa melempari pencuri dengan batu.", "マッサ ムルンパリ プンチュリ ドゥンガン バトゥ", "反復・対象 melempari。"),
            ("彼は庭の雑草を次から次へと引き抜いた。", "Dia mencabuti rumput liar di taman.", "ディア ムンチャブティ ルムプット リアール ディ タマン", "複数対象 mencabuti。"),
            ("彼女は床に散らばったコインを拾い集めた。", "Dia mengambili koin yang berserakan di lantai.", "ディア ムンガンビリ コイン ヤン ブルセラカン ディ ランタイ", "複数対象 mengambili。"),
            ("雨が屋根を激しく叩き続けた。", "Hujan memukuli atap rumah dengan deras.", "フジャン メムクリ アタップ ルマ ドゥンガン ドゥラス", "反復 memukuli。"),
            ("彼は痛む傷口を何度も触った。", "Dia memegangi lukanya yang sakit.", "ディア メメガンギ ルカニャ ヤン サキッ", "反復 memegangi。"),
            ("警察は容疑者に何度も質問を浴びせた。", "Polisi menanyai tersangka berulang kali.", "ポリシ メナニャイ トゥルスンカ ブルウラン カリ", "反復質問 menanyai。"),
            ("子供たちは壁に落書きをしまくった。", "Anak-anak mencoreti dinding dengan krayon.", "アナッアナッ ムンチョレティ ディンディン ドゥンガン クライヨン", "反復・複数箇所 mencoreti。"),
            ("彼は熟したマンゴーを木から次々に摘み取った。", "Dia memetiki mangga matang dari pohon.", "ディア メムティキ マンガ マタン ダリ ポホン", "複数摘み取り memetiki。"),
            ("波が海岸の岩を絶え間なく打ち付けた。", "Ombak menepuk-nepuki batu karang di pantai.", "オムバッ メヌプッヌプキ バトゥ カラン ディ パンタイ", "反復 menepuki。"),
            ("彼女は涙をハンカチで何度も拭った。", "Dia mengusapi air matanya dengan saputangan.", "ディア ムングサピ アイル マタニャ ドゥンガン サプタンガン", "反復 mengusapi。"),
            ("医者は患者の全身をくまなく触診した。", "Dokter merabai tubuh pasien untuk pemeriksaan.", "ドクテル メラバイ トゥブ パシエン ウントゥッ プムリクサアン", "連続触診 merabai。"),
            ("観客はステージに向かって花束を投げ入れ続けた。", "Penonton melempari panggung dengan karangan bunga.", "プノントン ムルンパリ パングン ドゥンガン カランガン ブンガ", "反復 melempari。"),
            ("彼は届いた荷物の箱を次々と開けていった。", "Dia membukai kotak paket yang tiba.", "ディア ムンブカイ コタッ パケット ヤン ティバ", "複数開封 membukai。")
        ],
        "quiz": [
            ("「何度も机を叩き続ける（反復）」を表す動詞は？", ["memukuli", "memukulkan", "berpukul", "terpukul"], 1),
            ("「石を何度も相手に投げつける」を表す動詞は？", ["melempari", "melemparkan", "berlempar", "terlempar"], 1),
            ("「草を何本も次々に引き抜く」を表す動詞は？", ["mencabuti", "mencabutkan", "bercabut", "tercabut"], 1)
        ]
    }
]

import os

for a in articles_data:
    filepath = os.path.join("docs/output", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. 産出メカニズムと文法公式\n")
    for r_title, r_desc in a['rules']:
        lines.append(f"### {r_title}")
        lines.append(f"{r_desc}\n")
    
    lines.append("## 2. 瞬間口頭作文トレーニング（15本ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語の文を見て、**1〜2秒以内**に声に出してインドネシア語を発話してください。その後、正解の文と解説を確認して口頭で3回リピートします。\n")
    
    for idx, (jp, id_sent, kana, exp) in enumerate(a['drill'], 1):
        lines.append(f"### 第{idx}問")
        lines.append(f"**日本語**: 「**{jp}**」\n")
        lines.append('<div class="id-example" markdown>\n')
        lines.append(f'<div class="id-sentence">\n{id_sent}\n</div>')
        lines.append(f'<div class="id-reading">\n{kana}\n</div>')
        lines.append(f'<div class="id-meaning">\n{jp}\n</div>')
        lines.append('</div>\n')
        lines.append(f"- **構造解説**: {exp}\n")
        lines.append("---\n")
        
    lines.append("## 3. 理解度チェッククイズ\n")
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

print("Batch 1021-1030 generated successfully.")
