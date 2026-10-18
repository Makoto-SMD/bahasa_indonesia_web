"""Writer Script: Articles 1061 - 1070 for docs/clinic/
"""

articles_data = [
    {
        "slug": "11-bukan-tidak-with-adjectives",
        "title": "【誤用克服】形容詞や動詞に bukan を使ってしまう誤用パターンの徹底診断",
        "intro": "日本語の「〜ではない」という否定の統一感に引っ張られ、形容詞や動詞に bukan を誤用してしまう症例（❌ Ini bukan enak / ❌ Dia bukan tahu）は初中級者の大定番です。bukan が許される唯一の例外（対比構文 bukan A melainkan B）も含めて完全診断します。",
        "cases": [
            ("この料理は美味しくない。", "Makanan ini bukan enak.", "Makanan ini tidak enak.", "形容詞 enak の否定は必ず tidak です。bukan を単体で形容詞につけることはできません。"),
            ("私はそのことを知らない。", "Saya bukan tahu hal itu.", "Saya tidak tahu hal itu.", "動詞 tahu の否定は tidak です。")
        ],
        "drill": [
            ("この部屋は広くありません。", "Kamar ini tidak luas.", "カマール イニ ティダッ ルアス", "形容詞 luas の否定は tidak。"),
            ("彼は怠け者なのではなく、疲れているのです。", "Dia bukan malas, melainkan lelah.", "ディア ブカン マラス ムラインカン レラ", "対比構文 bukan ... melainkan なら形容詞でも bukan が可能！"),
            ("私は魚を食べません。", "Saya tidak makan ikan.", "サヤ ティダッ マカン イカン", "動詞 makan の否定は tidak。"),
            ("これは私の車ではありません。", "Ini bukan mobil saya.", "イニ ブカン モビル サヤ", "名詞句 mobil saya の否定は bukan。"),
            ("その服は高くない。", "Baju itu tidak mahal.", "バジュ イトゥ ティダッ マハル", "形容詞 mahal の否定は tidak。"),
            ("彼が悪いのではなく、私のミスです。", "Bukan dia yang salah, melainkan saya.", "ブカン ディア ヤン サラ ムラインカン サヤ", "人称の対比否定 bukan dia..."),
            ("今日は寒くありません。", "Hari ini tidak dingin.", "ハリ イニ ティダッ ディンギン", "形容詞 dingin の否定は tidak。"),
            ("彼女はまだ結婚していません。", "Dia belum menikah.", "ディア ブロン メニカ", "未完了 belum。"),
            ("私が求めているのはお金ではなく時間です。", "Bukan uang yang saya cari, melainkan waktu.", "ブカン ウアン ヤン サヤ チャリ ムラインカン ワクトゥ", "名詞対比 bukan uang..."),
            ("この道は安全ではありません。", "Jalan ini tidak aman.", "ジャラン イニ ティダッ アマン", "形容詞 aman の否定は tidak。"),
            ("彼は英語が話せません。", "Dia tidak bisa berbicara bahasa Inggris.", "ディア ティダッ ビサ ブルビチャラ バハサ イングリス", "助動詞 bisa の否定は tidak。"),
            ("それは解決策ではなく、新たな問題だ。", "Itu bukan solusi, melainkan masalah baru.", "イトゥ ブカン ソルシ ムラインカン マサラ バル", "名詞 bukan solusi..."),
            ("スープが辛すぎないようにしてください。", "Supnya jangan terlalu pedas ya.", "スプニャ ジャンガン トゥルラル プダス ヤ", "依頼・禁止 jangan。"),
            ("私はその意見に同意しません。", "Saya tidak setuju dengan pendapat itu.", "サヤ ティダッ スツジュ ドゥンガン プンダパット イトゥ", "動詞 setuju の否定は tidak。"),
            ("彼が遅刻したのは故意ではない。", "Dia terlambat bukan karena sengaja.", "ディア トゥルランバット ブカン カルナ スンガジャ", "理由節の対比 bukan karena... ")
        ],
        "quiz": [
            ("「このホテルは高くない」の正しい文は？", ["Hotel ini tidak mahal.", "Hotel ini bukan mahal.", "Hotel ini jangan mahal.", "Hotel ini belum mahal."], 1),
            ("形容詞の直前に bukan が文法的に使える唯一の条件は？", ["「〜ではなく…だ」という melainkan との対比構文の時", "過去形の時", "疑問文の時", "丁寧語の時"], 1),
            ("「私は知らない」の正しいインドネシア語は？", ["Saya tidak tahu.", "Saya bukan tahu.", "Saya jangan tahu.", "Saya tanpa tahu."], 1)
        ]
    },
    {
        "slug": "12-oleh-agent-overuse",
        "title": "【誤用克服】受動態で oleh を常に挿入してしまう「英語直訳・日本語直訳」癖の矯正",
        "intro": "英語の受動態「by」や日本語の「〜によって」に引きずられ、受動態 di- の後ろに機械的にすべて「oleh」を挿入してしまう日本人学習者が後を絶ちません。インドネシア語では、動作主が動詞の直後に隣接する場合、oleh は省略するのがはるかに自然で流暢です。",
        "cases": [
            ("そのケーキは母が作りました（母によって作られた）。", "Kue itu dibuat oleh ibu.", "Kue itu dibuat ibu.", "動作主 ibu が動詞 dibuat の直後に密着しているため、oleh は入れない方がすっきりして自然です。"),
            ("その車は修理工によって昨日修理された。", "Mobil itu diperbaiki kemarin oleh montir.", "Mobil itu diperbaiki kemarin oleh montir.", "動詞と動作主の間に kemarin などの副詞が割り込む場合は、oleh が脱落すると意味が崩れるため oleh が必須です。")
        ],
        "drill": [
            ("その手紙は社長が署名しました（署名された）。", "Surat itu ditandatangani direktur.", "スラット イトゥ ディタンダタンガニ ディレクトゥール", "直後密着のため oleh なしが自然！"),
            ("部屋は妹が掃除しました。", "Kamar dibersihkan adik.", "カマール ディブルシカン アディッ", "oleh なし。"),
            ("その本は彼によって昨日読まれた。", "Buku itu dibaca kemarin oleh dia.", "ブク イトゥ ディバチャ クマリン オレ ディア", "副詞 kemarin が挟まるため oleh 必須。"),
            ("ご飯はお母さんが炊きました。", "Nasi dimasak ibu.", "ナシ ディマサッ イブ", "oleh なし。"),
            ("泥棒は警察に逮捕されました。", "Pencuri ditangkap polisi.", "プンチュリ ディタンカップ ポリシ", "oleh なし。"),
            ("その絵は有名な画家によって描かれた。", "Lukisan itu dilukis pelukis terkenal.", "ルキサン イトゥ ディルキス プルキス トゥルクナル", "oleh なしで十分。"),
            ("新薬は研究者によってテストされている。", "Obat baru sedang diuji para peneliti.", "オバット バル スダン ディウジ パラ プヌリティ", "oleh なし。"),
            ("規則は政府によって来週公布される。", "Aturan akan diumumkan minggu depan oleh pemerintah.", "アトゥラン アカン ディウムムカン ミング ドゥパン オレ プムリンタ", "副詞句が挟まるため oleh 必須。"),
            ("荷物は配達員が届けました。", "Paket diantar kurir.", "パケット ディアンタール クリル", "oleh なし。"),
            ("窓は風で開いてしまった。", "Jendela terbuka oleh angin kencang.", "ジュンデラ トゥルブカ オレ アンギン クンチャン", "無生物・原因 oleh。"),
            ("車は修理工が直しました。", "Mobil diperbaiki montir.", "モビル ディプルバイキ モンティル", "oleh なし。"),
            ("その知らせは彼が伝えました。", "Kabar itu disampaikan dia.", "カバール イトゥ ディサンパイカン ディア", "oleh なし。"),
            ("宿題は先生が確認しました。", "PR diperiksa guru.", "ペーエル ディプルイクサ グル", "oleh なし。"),
            ("木は嵐によって倒された。", "Pohon ditumbangkan oleh badai kemarin.", "ポホン ディトゥムバンカン オレ バダイ クマリン", "副詞挟み込み oleh。"),
            ("コーヒーは彼が飲みました。", "Kopi diminum dia.", "コピ ディミヌム ディア", "oleh なし。")
        ],
        "quiz": [
            ("受動態で動作主が動詞の直後に来る場合の oleh の扱いは？", ["省略するのが最も自然ですっきりしている", "絶対に省略してはならない", "必ず文頭に置く", "名詞には使えない"], 1),
            ("oleh が必須となる条件は？", ["動詞と動作主の間に副詞（kemarin, tadi など）が挟まる時", "主語が人間の時", "動詞が現在形の時", "受動態の時常に"], 1),
            ("「その料理は母が作った（作られた）」の最も簡潔で自然な文は？", ["Makanan dimasak ibu.", "Makanan dimasak oleh karena ibu.", "Makanan memasak oleh ibu.", "Makanan dibuat oleh pada ibu."], 1)
        ]
    },
    {
        "slug": "13-jam-waktu-pukul-clash",
        "title": "【誤用克服】時間表現 jam, waktu, pukul の混同と不自然なコロケーションの是正",
        "intro": "日本語ではすべて「時間・時」と一括りにできる jam, waktu, pukul ですが、インドネシア語では①時刻（pukul / jam）、②時間の長さ・時間帯（jam）、③抽象的な「とき・時間・機会」（waktu）を厳格に区別します。混同を根治する処方箋です。",
        "cases": [
            ("今、時間ありますか？", "Apakah Anda ada jam sekarang?", "Apakah Anda ada waktu sekarang?", "「（都合としての）時間・暇」は waktu です。jam は物理的な時計や時刻・時間数を指すため、ada jam だと「時計を持っていますか？」と誤解されます。"),
            ("会議は午前8時に始まります（公式文書）。", "Rapat dimulai jam delapan pagi.", "Rapat dimulai pada pukul 08.00 pagi.", "ニュースや公式文書での時刻指定には pukul を用いるのが正式な正書法（EYD）です。")
        ],
        "drill": [
            ("今、時間ありますか？（都合の確認）", "Ada waktu sekarang?", "アダ ワクトゥ スカラン", "都合 waktu。"),
            ("今何時ですか？（時刻の質問）", "Jam berapa sekarang?", "ジャム ブラパ スカラン", "時刻質問 jam berapa。"),
            ("列車は午前9時ちょうどに出発します（公的時刻）。", "Kereta berangkat pada pukul 09.00 tepat.", "クレタ ブルランカット パダ プクル スンビラン トゥパット", "公的時刻 pukul。"),
            ("ジャカルタまで飛行機で2時間かかります（所要時間）。", "Perjalanan ke Jakarta memakan waktu dua jam.", "プルジャラナン ク ジャカルタ メマカン ワクトゥ ドゥア ジャム", "所要時間 dua jam。"),
            ("子供の時、私はバリ島に住んでいました（〜の時）。", "Pada waktu kecil, saya tinggal di Bali.", "パダ ワクトゥ クチル サヤ ティンガル ディ バリ", "時期・時代 waktu。"),
            ("私の腕時計が壊れました（時計そのもの）。", "Jam tangan saya rusak.", "ジャム タンガン サヤ ルサッ", "時計 jam。"),
            ("時間を無駄にしてはいけません。", "Jangan membuang-buang waktu.", "ジャンガン メムブアンブアン ワクトゥ", "抽象時間 waktu。"),
            ("会議は3時間続きました（継続時間）。", "Rapat berlangsung selama tiga jam.", "ラパット ブルラングスン スラマ ティガ ジャム", "時間数 tiga jam。"),
            ("食事の時間ですよ。", "Waktunya makan.", "ワクトゥニャ マカン", "好機・時間帯 Waktunya..."),
            ("毎朝6時に起きます（日常会話の時刻）。", "Saya bangun jam enam setiap pagi.", "サヤ バングン ジャム エナム スティアプ パギ", "口語時刻 jam enam。"),
            ("時が経つのは本当に早い。", "Waktu berlalu begitu cepat.", "ワクトゥ ブルラル ブギトゥ チパット", "時の流れ waktu。"),
            ("壁掛け時計が止まっています。", "Jam dinding mati.", "ジャム ディンディン マティ", "時計 jam dinding。"),
            ("時間通りに到着してください。", "Tolong tiba tepat waktu.", "トロン ティバ トゥパット ワクトゥ", "時間通り tepat waktu。"),
            ("彼は1日8時間働きます。", "Dia bekerja delapan jam sehari.", "ディア ブケルジャ ドラパン ジャム スハリ", "労働時間 delapan jam。"),
            ("いつかまた会える時間が来ると信じています。", "Saya percaya akan ada waktu untuk bertemu lagi.", "サヤ プルチャヤ アカン アダ ワクトゥ ウントゥッ ブルトゥム ラギ", "機会 waktu。")
        ],
        "quiz": [
            ("「今、時間（暇）ありますか？」の正しい文は？", ["Ada waktu sekarang?", "Ada jam sekarang?", "Ada pukul sekarang?", "Ada saatnya sekarang?"], 1),
            ("ニュース報道や公式文書で「午前8時に」を表す正式な表現は？", ["pada pukul 08.00", "pada jam 08.00", "pada waktu 08.00", "pada arloji 08.00"], 1),
            ("「2時間かかる」の「2時間（継続時間数）」を表すのは？", ["dua jam", "dua pukul", "dua waktu", "kedua jam"], 1)
        ]
    },
    {
        "slug": "14-banyak-orang-word-order",
        "title": "【誤用克服】banyak orang と orang banyak（群衆）の意味差と語順ミス",
        "intro": "「たくさんの人」を表現したい時、banyak orang と言うべきか、orang banyak と言うべきか？後置修飾のルール（名詞＋形容詞）を機械的に適用して orang banyak と言ってしまうと、「大衆・群衆・一般庶民」という全く別の意味になります。語順による意味変化を徹底解剖します。",
        "cases": [
            ("通りにはたくさんの人がいます（多数の個人）。", "Ada orang banyak di jalan raya.", "Ada banyak orang di jalan raya.", "「たくさんの人」という不特定多数の個人を指す場合は数量詞 banyak を名詞の前に置きます。後ろに置くと「群衆・大衆」という集合名詞的ニュアンスになります。"),
            ("大勢の人の前で話すのは緊張します（公衆の面前）。", "Gugup berbicara di depan banyak orang.", "Gugup berbicara di depan orang banyak.", "「公衆の面前・人前」という定型的な表現では、後置修飾の orang banyak（群衆・大衆）を用いるのが極めて自然です。")
        ],
        "drill": [
            ("通りにはたくさんの人がいます（多数の人々）。", "Ada banyak orang di jalan raya.", "アダ バニャッ オラン ディ ジャラン ラヤ", "多数の人 banyak orang。"),
            ("彼は大勢の人の前で演説した（公衆の面前）。", "Dia berpidato di depan orang banyak.", "ディア ブルピダト ディ ドゥパン オラン バニャッ", "公衆・群衆 orang banyak。"),
            ("多くの人々がその提案に反対した。", "Banyak orang menolak usulan itu.", "バニャッ オラン メノラッ ウスラン イトゥ", "主語 Banyak orang。"),
            ("人前で大声を出すのは恥ずかしい。", "Malu berteriak di depan orang banyak.", "マル ブルトリアッ ディ ドゥパン オラン バニャッ", "人前 orang banyak。"),
            ("昨日、たくさんの観光客がバリ島に到着した。", "Kemarin banyak turis tiba di Bali.", "クマリン バニャッ トゥリス ティバ ディ バリ", "数量詞 banyak turis。"),
            ("一般大衆の利益を守らなければならない。", "Harus menjaga kepentingan orang banyak.", "ハルス メンジャガ クポンティンガン オラン バニャッ", "大衆の利益 orang banyak。"),
            ("多くの子供たちが公園で遊んでいる。", "Banyak anak bermain di taman.", "バニャッ アナッ ブルマイン ディ タマン", "数量詞 Banyak anak。"),
            ("彼は大衆に好かれるリーダーだ。", "Dia pemimpin yang disukai orang banyak.", "ディア プミンピン ヤン ディスカイ オラン バニャッ", "大衆 orang banyak。"),
            ("多くの学生が試験に合格した。", "Banyak siswa lulus ujian.", "バニャッ シスワ ルルス ウジアン", "数量詞 Banyak siswa。"),
            ("公衆の面前で喧嘩をしてはいけない。", "Jangan bertengkar di depan orang banyak.", "ジャンガン ブルトゥンカル ディ ドゥパン オラン バニャッ", "公衆 orang banyak。"),
            ("たくさんの車が渋滞に巻き込まれている。", "Banyak mobil terjebak macet.", "バニャッ モビル トゥルジェバッ マチェット", "数量詞 Banyak mobil。"),
            ("多くの人が健康の重要性に気づいている。", "Banyak orang menyadari pentingnya kesehatan.", "バニャッ オラン ムニャダリ ポンティンニャ クセハタン", "主語 Banyak orang。"),
            ("彼は人前で話すのが苦手です。", "Dia tidak percaya diri bicara di depan orang banyak.", "ディア ティダッ プルチャヤ ディリ ビチャラ ディ ドゥパン オラン バニャッ", "人前 orang banyak。"),
            ("市場にはたくさんの果物が売られている。", "Banyak buah dijual di pasar.", "バニャッ ブア ディジュアル ディ パサール", "数量詞 Banyak buah。"),
            ("公共の福祉、大勢の人の幸福を祈る。", "Mendoakan kebahagiaan orang banyak.", "メンドアカアン クバハギアアン オラン バニャッ", "大衆・万民 orang banyak。")
        ],
        "quiz": [
            ("「通りにたくさんの人がいる」の正しい語順は？", ["Ada banyak orang di jalan.", "Ada orang banyak di jalan.", "Ada banyaknya orang di jalan.", "Ada perorangan banyak di jalan."], 1),
            ("「人前で（公衆の面前で）」を表す決まり文句は？", ["di depan orang banyak", "di depan banyak orang", "di depan terbanyak orang", "di depan orang-orang banyak"], 1),
            ("banyak orang と orang banyak の違いは？", ["banyak orang は「多数の人々」、orang banyak は「群衆・大衆」", "全く同じ意味", "banyak orang はスラング", "orang banyak は誤用"], 1)
        ]
    },
    {
        "slug": "15-sangat-sekali-redundancy",
        "title": "【誤用克服】sangat ... sekali の二重修飾の違和感と自然な強調表現",
        "intro": "「とても」を強調したいあまり、前置強調の sangat と後置強調の sekali を同時に使って【❌ sangat bagus sekali】と重ねてしまう誤用が非常に目立ちます。文法的には許容される場面もありますが、スマートな文章では「どちらか一方」を使うのが洗練された大人のインドネシア語です。",
        "cases": [
            ("このホテルはとても綺麗です。", "Hotel ini sangat bersih sekali.", "Hotel ini sangat bersih. / Hotel ini bersih sekali.", "sangat と sekali を両方重ねると「馬から落ちて落馬する」のような二重強調のくどさが出ます。どちらか片方だけに絞るのがエレガントです。"),
            ("富士山はとても高い。", "Gunung Fuji amat sangat tinggi sekali.", "Gunung Fuji sangat tinggi. / Gunung Fuji tinggi sekali.", "強調語を過剰に乱立させる癖を矯正します。")
        ],
        "drill": [
            ("この料理はとても美味しいです（sangat パターン）。", "Makanan ini sangat enak.", "マカナン イニ サンガット エナッ", "前置強調 sangat。"),
            ("この景色はとても美しいですね（sekali パターン）。", "Pemandangan ini indah sekali ya.", "プマンダンガン イニ インダ スカリ ヤ", "後置強調 sekali。"),
            ("社長はとても忙しいです。", "Direktur sangat sibuk.", "ディレクトゥール サンガット シブッ", "スマートな単一強調。"),
            ("彼の家はものすごく大きいです。", "Rumahnya besar sekali.", "ルマニャ ブサール スカリ", "sekali による強調。"),
            ("今日の気温はとても暑い。", "Suhu hari ini sangat panas.", "スフ ハリ イニ サンガット パナス", "sangat panas。"),
            ("その問題は極めて複雑です。", "Masalah itu sangat rumit.", "マサラ イトゥ サンガット ルミット", "sangat rumit。"),
            ("その子犬はとても可愛い。", "Anak anjing itu lucu sekali.", "アナッ アンジン イトゥ ルチュ スカリ", "lucu sekali。"),
            ("彼の説明はとても分かりやすい。", "Penjelasannya sangat jelas.", "プンジュラサンニャ サンガット ジュラス", "sangat jelas。"),
            ("昨夜の地震はとても揺れが強かった。", "Gempa tadi malam kuat sekali.", "グムパ タディ マラム クアット スカリ", "kuat sekali。"),
            ("その知らせを聞いてとても嬉しいです。", "Saya sangat senang mendengar kabar itu.", "サヤ サンガット スナン ムンドンガル カバール イトゥ", "sangat senang。"),
            ("スープがとても熱いので気をつけて。", "Supnya panas sekali, hati-hati.", "スプニャ パナス スカリ ハティハティ", "panas sekali。"),
            ("この靴はとても履き心地が良い。", "Sepatu ini sangat nyaman dipakai.", "スパトゥ イニ サンガット ニャマン ディパカイ", "sangat nyaman。"),
            ("彼女の歌声はとても素晴らしい。", "Suaranya merdu sekali.", "スアラニャ ムルドゥ スカリ", "merdu sekali。"),
            ("この道は夜とても暗いです。", "Jalan ini sangat gelap pada malam hari.", "ジャラン イニ サンガット グラップ パダ マラム ハリ", "sangat gelap。"),
            ("試験はとても難しかったです。", "Ujiannya sulit sekali.", "ウジアンニャ スリット スカリ", "sulit sekali。")
        ],
        "quiz": [
            ("「とても美味しい」を表現する最も洗練された方法は？", ["sangat enak または enak sekali", "sangat enak sekali", "amat sangat lezat sekali", "paling sangat enak"], 1),
            ("sangat の正しい配置位置は？", ["形容詞の直前（sangat indah）", "形容詞の直後", "文末", "主語の直前"], 1),
            ("sekali の正しい配置位置は？", ["形容詞の直後（indah sekali）", "形容詞の直前", "文頭", "主語の直後"], 1)
        ]
    },
    {
        "slug": "16-untuk-preposition-overuse",
        "title": "【誤用克服】日本語の「〜のために」を機械的に untuk と訳す病の克服",
        "intro": "日本語の「〜のために」は、①目的（〜するために）、②理由・原因（大雨のために）、③受益（あなたのために）、④対象（子供にとって）など多岐にわたります。これをすべて untuk で直訳すると、原因を表したいのに目的になってしまう重大な意味逆転が起こります。",
        "cases": [
            ("大雨のために、電車が止まりました（理由）。", "Untuk hujan deras, kereta berhenti.", "Karena hujan deras, kereta berhenti.", "日本語の「大雨のために」は理由・原因なので karena です。untuk だと「大雨を降らせるために電車を止めた」という不気味な意味になってしまいます！"),
            ("子供たちにとって、睡眠は大切です（対象者）。", "Untuk anak-anak, tidur itu penting.", "Bagi anak-anak, tidur itu penting.", "評価の対象者を示す場合は untuk ではなく bagi を使います。")
        ],
        "drill": [
            ("病気のために、彼は学校を休みました（理由）。", "Karena sakit, dia tidak masuk sekolah.", "カルナ サキッ ディア ティダッ マスッ スコラ", "理由は karena！"),
            ("健康のために、毎日野菜を食べます（目的）。", "Saya makan sayur setiap hari demi kesehatan.", "サヤ マカン サユール スティアプ ハリ ドミ クセハタン", "目的・大義は demi / untuk。"),
            ("私にとって、あなたが一番大切です（対象者）。", "Bagi saya, Anda yang paling berharga.", "バギ サヤ アンダ ヤン パリン ブルハルガ", "対象者は Bagi saya。"),
            ("大渋滞のために、飛行機に乗り遅れた（理由）。", "Karena macet parah, saya ketinggalan pesawat.", "カルナ マチェット パラ サヤ クティンガラン プサワット", "理由は karena。"),
            ("これは子供たちのための本です（用途・対象）。", "Ini buku untuk anak-anak.", "イニ ブク ウントゥッ アナッアナッ", "用途は untuk。"),
            ("台風のために、試合は延期された（理由）。", "Karena badai, pertandingan ditunda.", "カルナ バダイ プルタンディンガン ディトゥンダ", "理由は karena。"),
            ("彼らにとって、この決定は不利です（対象）。", "Bagi mereka, keputusan ini merugikan.", "バギ ムレカ クプトゥサン イニ メルギカン", "対象者は bagi。"),
            ("家を買うためにお金を貯めています（目的）。", "Saya menabung uang untuk membeli rumah.", "サヤ メナブン ウアン ウントゥッ ムンブリ ルマ", "目的は untuk。"),
            ("地震のために、停電が発生しました（理由）。", "Karena gempa, terjadi pemadaman listrik.", "カルナ グムパ トゥルジャディ プマダマン リストリッ", "理由は karena。"),
            ("外国人にとって、漢字は難しい（対象）。", "Bagi orang asing, kanji itu sulit.", "バギ オラン アシン カンジ イトゥ スリット", "対象者は bagi。"),
            ("将来のために一生懸命勉強する（目的）。", "Belajar giat demi masa depan.", "ブラジャール ギアット ドミ マサ ドゥパン", "目的・大義 demi。"),
            ("事故のために、道路が通行止めになった（理由）。", "Karena kecelakaan, jalan ditutup.", "カルナ クチュラカアン ジャラン ディトゥトゥップ", "理由は karena。"),
            ("初心者向け（初心者用）の辞書（用途）。", "Kamus untuk pemula.", "カムス ウントゥッ プムラ", "用途 untuk。"),
            ("学生にとって、休日は楽しい（対象）。", "Bagi mahasiswa, hari libur menyenangkan.", "バギ マハシスワ ハリ リブール メニュナンカン", "対象 bagi。"),
            ("寝坊したために、遅刻してしまった（理由）。", "Karena bangun kesiangan, saya terlambat.", "カルナ バングン クシアンガン サヤ トゥルランバット", "理由は karena。")
        ],
        "quiz": [
            ("「大雨のために電車が遅れた（原因）」の正しい前置詞は？", ["Karena hujan deras", "Untuk hujan deras", "Bagi hujan deras", "Demi hujan deras"], 1),
            ("「私にとって（評価）」を表す正しい前置詞は？", ["Bagi saya", "Untuk saya", "Karena saya", "Atas saya"], 1),
            ("「将来のために（大義・目的）」を表す前置詞は？", ["demi masa depan", "karena masa depan", "akibat masa depan", "oleh masa depan"], 1)
        ]
    },
    {
        "slug": "17-dengan-preposition-misuse",
        "title": "【誤用克服】手段・同伴・様態の dengan の過剰使用と適切な省略",
        "intro": "日本語の助詞「〜で（手段）」「〜と（同伴）」を何でも dengan と直訳してしまう病を治します。乗り物（naik mobil / naik kereta）や言語（pakai bahasa Indonesia / berbahasa Indonesia）において dengan を乱用する不自然さを排し、ネイティブの引き締まった表現を身につけます。",
        "cases": [
            ("私は電車で行きます（手段）。", "Saya pergi dengan kereta.", "Saya pergi naik kereta.", "乗り物に乗って移動する場合、dengan kereta よりも「naik kereta（電車に乗って行く）」と言うのが圧倒的に自然です。"),
            ("インドネシア語で話してください。", "Tolong bicara dengan bahasa Indonesia.", "Tolong bicara bahasa Indonesia. / Tolong pakai bahasa Indonesia.", "言語名には dengan は不要で、直接目的語にするか pakai を使います。")
        ],
        "drill": [
            ("私たちはバスで行きます（乗り物）。", "Kami pergi naik bus.", "カミ プルギ ナイク ブス", "naik bus。"),
            ("ペンで名前を書いてください（道具）。", "Tolong tulis nama dengan pulpen.", "トロン トゥリス ナマ ドゥンガン プルペン", "道具は dengan pulpen。"),
            ("私は父と一緒に市場へ行きました（同伴）。", "Saya pergi ke pasar bersama ayah.", "サヤ プルギ ク パサール ブルサマ アヤ", "同伴 bersama ayah。"),
            ("笑顔で挨拶しましょう（様態）。", "Mari menyapa dengan senyuman.", "マリ メニャパ ドゥンガン スニュマン", "様態 dengan senyuman。"),
            ("彼は飛行機でスラバヤへ向かった。", "Dia pergi ke Surabaya naik pesawat.", "ディア プルギ ク スラバヤ ナイク プサワット", "naik pesawat。"),
            ("英語でメールを書いてください。", "Tolong tulis email dalam bahasa Inggris.", "トロン トゥリス イーメール ダラム バハサ イングリス", "dalam / pakai bahasa Inggris。"),
            ("熱心に勉強しなさい（様態）。", "Belajarlah dengan giat.", "ブラジャールラ ドゥンガン ギアット", "様態 dengan giat。"),
            ("スプーンを使って食べてください（道具）。", "Makanlah dengan sendok.", "マカンラ ドゥンガン スンドッ", "道具 dengan sendok。"),
            ("彼はバイクで仕事に通っています。", "Dia berangkat kerja naik motor.", "ディア ブルランカット クルジャ ナイク モトル", "naik motor。"),
            ("喜んでお手伝いします（様態）。", "Dengan senang hati saya bantu.", "ドゥンガン スナン ハティ サヤ バントゥ", "様態 Dengan senang hati。"),
            ("友達と一緒に昼食を食べました。", "Saya makan siang bersama teman.", "サヤ マカン シアン ブルサマ トゥマン", "同伴 bersama teman。"),
            ("礼儀正しく話しなさい（様態）。", "Bicaralah dengan sopan.", "ビチャララ ドゥンガン ソパン", "様態 dengan sopan。"),
            ("車で行きましょうか？", "Mau pergi naik mobil?", "マウ プルギ ナイク モビル", "naik mobil。"),
            ("インドネシア語で話しましょう。", "Mari kita bicara bahasa Indonesia.", "マリ キタ ビチャラ バハサ インドネシア", "言語名は直接 bicara bahasa Indonesia。"),
            ("慎重に運転してください（様態）。", "Menyetirlah dengan hati-hati.", "メニョティルラ ドゥンガン ハティハティ", "様態 dengan hati-hati。")
        ],
        "quiz": [
            ("「電車で行く」の最も自然な日常表現は？", ["pergi naik kereta", "pergi dengan kereta", "pergi pakai kereta", "pergi untuk kereta"], 1),
            ("「インドネシア語で話す」の自然な言い方は？", ["bicara bahasa Indonesia", "bicara dengan bahasa Indonesia", "bicara dari bahasa Indonesia", "bicara kepada bahasa Indonesia"], 1),
            ("「友達と一緒に」を表す最も明確な同伴表現は？", ["bersama teman", "dengan kereta", "pada teman", "ke teman"], 1)
        ]
    },
    {
        "slug": "18-dari-daripada-confusion",
        "title": "【誤用克服】起点 dari と比較 daripada の混同（誤った daripada の使用）",
        "intro": "マレー語や古いインドネシア語の用法、あるいは英語の than と from の混同から、「dari」と「daripada」を取り違えるミスが頻発します。「dari」は場所・時間の起点（〜から）および出所、「daripada」は比較（〜よりも）専用です。daripada を起点に使ってしまう誤用を徹底根絶します。",
        "cases": [
            ("私は日本から来ました。", "Saya datang daripada Jepang.", "Saya datang dari Jepang.", "場所や起点は 100%「dari」です。daripada は比較以外では使えません。"),
            ("健康は富よりも大切です。", "Kesehatan lebih penting dari kekayaan.", "Kesehatan lebih penting daripada kekayaan.", "比較には正式には daripada を使います（口語では dari に略されることもありますが、公式な文章では daripada が正確です）。")
        ],
        "drill": [
            ("彼はスラバヤから到着しました（場所起点）。", "Dia tiba dari Surabaya.", "ディア ティバ ダリ スラバヤ", "起点は dari。"),
            ("兄は私より背が高い（比較）。", "Kakak lebih tinggi daripada saya.", "カカッ ルビ ティンギ ダリパダ サヤ", "比較は daripada。"),
            ("会議は午前9時から始まります（時間起点）。", "Rapat dimulai dari jam sembilan.", "ラパット ディムライ ダリ ジャム スンビラン", "起点は dari。"),
            ("飛行機は電車よりも速い（比較）。", "Pesawat lebih cepat daripada kereta.", "プサワット ルビ チパット ダリパダ クレタ", "比較は daripada。"),
            ("この小包は母から送られてきました（出所）。", "Paket ini dikirim dari ibu.", "パケット イニ ディキリム ダリ イブ", "出所は dari。"),
            ("行動することは口先だけで言うことよりも大切だ。", "Bertindak lebih penting daripada sekadar bicara.", "ブルティンダッ ルビ ポンティン ダリパダ スカダール ビチャラ", "比較 daripada。"),
            ("駅からオフィスまで歩きます（起点）。", "Berjalan dari stasiun ke kantor.", "ブルジャラン ダリ スタシウン ク カントール", "起点 dari。"),
            ("このホテルはあのホテルより安い（比較）。", "Hotel ini lebih murah daripada hotel itu.", "ホテル イニ ルビ ムラ ダリパダ ホテル イトゥ", "比較 daripada。"),
            ("彼女は部屋から出て行きました（空間起点）。", "Dia keluar dari kamar.", "ディア クルアール ダリ カマール", "起点 dari。"),
            ("失敗を恐れるよりも、挑戦する方が良い（比較）。", "Lebih baik mencoba daripada takut gagal.", "ルビ バイッ ムンチョバ ダリパダ タクット ガガル", "比較 daripada。"),
            ("木から熟したマンゴーが落ちました（起点）。", "Mangga matang jatuh dari pohon.", "マンガ マタン ジャトゥ ダリ ポホン", "起点 dari。"),
            ("今日の気温は昨日より涼しい（比較）。", "Suhu hari ini lebih sejuk daripada kemarin.", "スフ ハリ イニ ルビ スジュッ ダリパダ クマリン", "比較 daripada。"),
            ("最初から最後まで全部読みました（起点）。", "Membaca semua dari awal sampai akhir.", "ムンバチャ スムア ダリ アワル サンパイ アヒール", "起点 dari。"),
            ("品質は量よりも大切です（比較）。", "Kualitas lebih berharga daripada kuantitas.", "クアリタス ルビ ブルハルガ ダリパダ クアンティタス", "比較 daripada。"),
            ("このニュースはどこから手に入れましたか？（出所）", "Dari mana Anda mendapat berita ini?", "ダリ マナ アンダ ムンダパット ブリタ イニ", "出所 dari mana。")
        ],
        "quiz": [
            ("「日本から来ました（起点）」の正しい文は？", ["Saya datang dari Jepang.", "Saya datang daripada Jepang.", "Saya datang kepada Jepang.", "Saya datang di Jepang."], 1),
            ("「AはBより大きい（比較）」の正式な接続詞は？", ["A lebih besar daripada B.", "A lebih besar dari pada B.", "A lebih besar kepada B.", "A lebih besar untuk B."], 1),
            ("daripada の文法的な唯一の機能は？", ["2つの物事を比べる（〜よりも）", "場所の出発点を表す（〜から）", "時間の起点を表す（〜から）", "理由を表す（〜なので）"], 1)
        ]
    },
    {
        "slug": "19-tentang-mengenai-overuse",
        "title": "【誤用克服】「〜について」を何でも tentang にしてしまう論文・ビジネス文の矯正",
        "intro": "日本語の「〜について（議論する、報告する、考える）」を何でもかんでも前置詞 tentang で直訳する癖は、文章を幼稚で冗長にします。接尾辞「-i」や「-kan」の他動詞を活用することで、前置詞を使わずに直接目的語をとる洗練されたビジネス文体へとリライトします。",
        "cases": [
            ("私たちは新しいプロジェクトについて議論した。", "Kami berdiskusi tentang proyek baru.", "Kami membahas proyek baru.", "「berdiskusi tentang...」も文法的には正しいですが、ビジネスや論文では他動詞 membahas（〜を討議する）を使って直接目的語を取る方が圧倒的に簡潔で知性的です。"),
            ("彼はその規則について知っている。", "Dia tahu tentang aturan itu.", "Dia mengetahui aturan itu.", "tahu tentang ではなく、他動詞 mengetahui を使います。")
        ],
        "drill": [
            ("私たちは予算について議論しました。", "Kami membahas anggaran belanja.", "カミ ムンバハス アンガラン ブランジャ", "他動詞 membahas [目的語]。"),
            ("社長はその問題について調査を指示した。", "Direktur meneliti masalah tersebut.", "ディレクトゥール ムヌリティ マサラ トゥルスブット", "他動詞 meneliti。"),
            ("彼は社内規則を熟知している（規則について知っている）。", "Dia mengetahui peraturan kantor.", "ディア ムングタフイ プラトゥラン カントール", "他動詞 mengetahui。"),
            ("私たちは新しい技術を研究しています（技術について研究）。", "Kami mempelajari teknologi baru.", "カミ メムプラジャリ テクノロジ バル", "他動詞 mempelajari。"),
            ("その小説は愛の物語を描いている。", "Novel itu menceritakan kisah cinta.", "ノフェル イトゥ ムンチュリタカン キサ チンタ", "他動詞 menceritakan。"),
            ("委員会は報告書の内容を審査した。", "Komite memeriksa isi laporan.", "コミテ ムムリクサ イシ ラポラン", "他動詞 memeriksa。"),
            ("彼らは気候変動の影響を分析している。", "Mereka menganalisis dampak perubahan iklim.", "ムレカ ムンアナリシス ダンパッ プルバハン イクリム", "他動詞 menganalisis。"),
            ("私たちは契約条件を交渉した。", "Kami merundingkan syarat kontrak.", "カミ ムルンディンカン シャラット コントラッ", "他動詞 merundingkan。"),
            ("この本はインドネシアの歴史を扱っている。", "Buku ini mengulas sejarah Indonesia.", "ブク イニ ムングラス スジャラ インドネシア", "他動詞 mengulas。"),
            ("医師は患者の容態を説明した。", "Dokter menjelaskan kondisi pasien.", "ドクテル ムンジュラスカン コンディシ パシエン", "他動詞 menjelaskan。"),
            ("私たちは新しい法律の施行について合意した。", "Kami menyepakati pemberlakuan hukum baru.", "カミ ムニェパカティ プムブルラクアン フクム バル", "他動詞 menyepakati。"),
            ("彼は自分の過ちを認めた（過ちについて認めた）。", "Dia mengakui kesalahannya.", "ディア ムンガクイ クサラハンニャ", "他動詞 mengakui。"),
            ("政府は貧困削減策を推進している。", "Pemerintah mengupayakan pengentasan kemiskinan.", "プムリンタ ムングパヤカン プンゲンタサン クミスキナン", "他動詞 mengupayakan。"),
            ("警察は事故の原因を究明している。", "Polisi menyelidiki penyebab kecelakaan.", "ポリシ ムンユリディキ プニェバブ クチュラカアン", "他動詞 menyelidiki。"),
            ("私たちは今後の計画を話し合った。", "Kami membicarakan rencana ke depan.", "カミ ムムビチャラカン レンチャナ ク ドゥパン", "他動詞 membicarakan。")
        ],
        "quiz": [
            ("「新しいプロジェクトについて議論する」を最も簡潔・知的に言うと？", ["membahas proyek baru", "berdiskusi tentang proyek baru", "bicara tentang proyek baru", "omong-omong tentang proyek baru"], 1),
            ("「規則について知っている」を1単語の他動詞で表現すると？", ["mengetahui aturan", "tahu tentang aturan", "kenal aturan", "paham tentang aturan"], 1),
            ("tentang の乱用を避けて文章を引き締めるための秘訣は？", ["接尾辞 -kan や -i を伴う他動詞（meN-）に置き換えて直接目的語を取る", "前置詞を全部消す", "受動態にする", "英語の単語を混ぜる"], 1)
        ]
    },
    {
        "slug": "20-sebagai-position-misuse",
        "title": "【誤用克服】日本語の「〜として」を何でも sebagai と直訳する不自然さの解消",
        "intro": "日本語の「〜として」は、①身分・資格（医者として働く）、②代表（日本代表として）、③機能（部屋をオフィスとして使う）、④時（最初として）など極めて多機能です。これを何でも sebagai と機械直訳する癖を排し、menjadi や untuk などを使い分ける技術を伝授します。",
        "cases": [
            ("この部屋を寝室として使っています。", "Kamar ini digunakan sebagai kamar tidur.", "Kamar ini dijadikan kamar tidur. / Kamar ini untuk kamar tidur.", "sebagai は「身分・身分資格（sebagai dokter, sebagai guru）」に最も適合します。物の用途や機能転換には dijadikan（〜にされる）や untuk を使う方が自然です。"),
            ("お土産としてこのお菓子を買いました。", "Saya membeli kue ini sebagai oleh-oleh.", "Saya membeli kue ini untuk oleh-oleh.", "目的・用途なので untuk oleh-oleh が自然です。")
        ],
        "drill": [
            ("兄は病院で医者として働いています（身分・職業）。", "Kakak bekerja sebagai dokter di rumah sakit.", "カカッ ブケルジャ スバガイ ドクテル ディ ルマ サキッ", "資格・身分 sebagai dokter。"),
            ("お土産としてこの伝統工芸品を買いました（用途）。", "Saya membeli kerajinan ini untuk oleh-oleh.", "サヤ ムンブリ クラジナン イニ ウントゥッ オレオレ", "用途 untuk oleh-oleh。"),
            ("この古い建物を博物館に改装した（機能転換）。", "Bangunan tua ini dijadikan museum.", "バングナン トゥア イニ ディジャディカン ムセウム", "機能転換 dijadikan..."),
            ("彼はインドネシア代表として大会に出場した（立場）。", "Dia bertanding sebagai wakil Indonesia.", "ディア ブルタンディン スバガイ ワキル インドネシア", "立場 sebagai wakil。"),
            ("朝食としてバナナを1本食べました（用途）。", "Saya makan sebutir pisang untuk sarapan.", "サヤ マカン スブティル ピサン ウントゥッ サラパン", "用途 untuk sarapan。"),
            ("彼女は通訳として会議に同行した（役割）。", "Dia mendampingi delegasi sebagai penerjemah.", "ディア ムンダンピンギ デレガシ スバガイ プヌルジュマ", "役割 sebagai penerjemah。"),
            ("プレゼントとして本を贈りました（用途）。", "Memberikan buku untuk hadiah ulang tahun.", "ムンブリカン ブク ウントゥッ ハディア ウラン タフン", "用途 untuk hadiah。"),
            ("彼は私の親友であり、兄のような存在です。", "Dia sahabat saya dan sudah dianggap seperti kakak.", "ディア サハバット サヤ ダン スダ ディアンガップ スペルティ カカッ", "見なし dianggap seperti..."),
            ("この部屋を倉庫として使ってください（機能）。", "Jadikan ruangan ini gudang penyimpanan.", "ジャディカン ルアンガン イニ グダン プンシンパナン", "機能 jadikan..."),
            ("私個人の意見として申し上げます（立場）。", "Saya berbicara sebagai pribadi.", "サヤ ブルビチャラ スバガイ プリバディ", "立場 sebagai pribadi。"),
            ("参考資料としてこの本をお読みください（用途）。", "Bacalah buku ini untuk referensi.", "バチャラ ブク イニ ウントゥッ レフェレンシ", "用途 untuk referensi。"),
            ("彼はリーダーとして優れた資質を持っている（資格）。", "Dia punya bakat luar biasa sebagai pemimpin.", "ディア プニャ バカット ルアール ビアサ スバガイ プミンピン", "資格 sebagai pemimpin。"),
            ("記念品としてバティックの布をいただいた（用途）。", "Menerima kain batik untuk kenang-kenangan.", "メネリマ カイン バティッ ウントゥッ クナンクナンガン", "用途 untuk kenang-kenangan。"),
            ("彼は証人として法廷に召喚された（身分）。", "Dia dipanggil ke pengadilan sebagai saksi.", "ディア ディパンギル ク プンガディラン スバガイ サクシ", "法的身分 sebagai saksi。"),
            ("これを教訓として次に生かそう（教訓）。", "Jadikan ini pelajaran untuk masa depan.", "ジャディカン イニ プラジャラン ウントゥッ マサ ドゥパン", "教訓 jadikan... pelajaran。")
        ],
        "quiz": [
            ("「医者として働く（身分・職業）」を表す自然な表現は？", ["bekerja sebagai dokter", "bekerja untuk dokter", "bekerja menjadi dokter", "bekerja dengan dokter"], 1),
            ("「お土産としてお菓子を買う（用途）」の最も自然な前置詞は？", ["untuk oleh-oleh", "sebagai oleh-oleh", "dengan oleh-oleh", "menjadi oleh-oleh"], 1),
            ("部屋をオフィスに転換する時の動詞は？", ["dijadikan kantor", "disebagaikan kantor", "diuntukkan kantor", "dimenjadikan kantor"], 1)
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
    lines.append("母語（日本語）の思考フレームを解体し、インドネシア語の品詞分類・前置詞の本来の役割に即した構文パターンを確立します。\n")
    
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

print("Batch 1061-1070 generated successfully.")
