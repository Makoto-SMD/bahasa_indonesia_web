"""Writer Script: Articles 1011 - 1020 for docs/output/
"""

articles_data = [
    {
        "slug": "11-conjunction-coordinating",
        "title": "【瞬間作文】等位接続詞（dan, atau, tetapi, melainkan）の論理接続",
        "intro": "単語や文を対等に結ぶ等位接続詞は、会話の展開を支える骨格です。特に「逆接」において、肯定文を受ける tetapi と、否定文を受ける melainkan（〜ではなくて…だ）の決定的な違いを0.5秒で使い分ける反射神経を鍛えます。",
        "rules": [
            ("dan（並列・〜と） / atau（選択・または）", "Saya dan dia（私と彼）、teh atau kopi（お茶またはコーヒー）。"),
            ("tetapi / tapi（逆接・しかし）", "肯定の内容に反する事態を接続。「Dia kaya, tetapi tidak sombong（彼は裕福だが傲慢ではない）」。"),
            ("melainkan（対比逆接・〜ではなくて）", "否定詞 bukan / tidak の後に続き、「AではなくてBだ」と訂正する。「Bukan dia yang salah, melainkan saya（彼が悪いのではなく私が悪い）」。")
        ],
        "drill": [
            ("父と母は市場へ行きました。", "Ayah dan ibu pergi ke pasar.", "アヤ ダン イブ プルギ ク パサール", "並列接続詞 dan。"),
            ("お茶にしますか、それともコーヒーにしますか？", "Anda mau teh atau kopi?", "アンダ マウ テ アタウ コピ", "選択接続詞 atau。"),
            ("この部屋は小さいですが、とても綺麗です。", "Kamar ini kecil, tetapi sangat bersih.", "カマール イニ クチル トゥタピ サンガット ブルシ", "逆接 tetapi。口語では tapi。"),
            ("彼は日本人ではなくて、インドネシア人です。", "Dia bukan orang Jepang, melainkan orang Indonesia.", "ディア ブカン オラン ジュパン ムラインカン オラン インドネシア", "否定対比 bukan ... melainkan。"),
            ("私は行きたいのですが、時間がありません。", "Saya mau pergi, tetapi tidak punya waktu.", "サヤ マウ プルギ トゥタピ ティダッ プニャ ワクトゥ", "逆接 tetapi。"),
            ("今日出発しますか、それとも明日ですか？", "Anda berangkat hari ini atau besok?", "アンダ ブルランカット ハリ イニ アタウ ベソッ", "選択 atau。"),
            ("彼は怠け者なのではなく、疲れているのです。", "Dia bukan malas, melainkan sedang lelah.", "ディア ブカン マラス ムラインカン スダン レラ", "bukan ... melainkan。"),
            ("兄と弟はサッカーをしています。", "Kakak dan adik sedang bermain sepak bola.", "カカッ ダン アディッ スダン ブルマイン スパッ ボラ", "並列 dan。"),
            ("安くて美味しい屋台。", "Warung yang murah dan enak.", "ワルン ヤン ムラ ダン エナッ", "性質の並列 murah dan enak。"),
            ("これは私の責任ではなく、あなたの責任です。", "Ini bukan tanggung jawab saya, melainkan tanggung jawab Anda.", "イニ ブカン タングン ジャワブ サヤ ムラインカン タングン ジャワブ アンダ", "対比 melainkan。"),
            ("彼女は優しいですが、怒ると怖いです。", "Dia ramah, tetapi kalau marah menakutkan.", "ディア ラマ トゥタピ カロウ マラ ムナクッカン", "逆接 tetapi。"),
            ("現金で支払いますか、それともQRISですか？", "Bayar dengan tunai atau QRIS?", "バヤル ドゥンガン トゥナイ アタウ クリス", "選択 atau。"),
            ("私は魚も肉も好きです。", "Saya suka ikan dan daging.", "サヤ スカ イカン ダン ダギン", "並列 dan。"),
            ("彼はお金を求めているのではなく、平和を求めている。", "Dia tidak mencari uang, melainkan mencari kedamaian.", "ディア ティダッ マンチャリ ウアン ムラインカン マンチャリ クダマイアン", "tidak ... melainkan。"),
            ("問題は複雑ですが、解決策はあります。", "Masalahnya rumit, tetapi ada jalan keluarnya.", "マサラニャ ルミット トゥタピ アダ ジャラン クルアルニャ", "逆接 tetapi。")
        ],
        "quiz": [
            ("「AではなくB」の構文で空欄に入るのは？ Bukan dia, ___ saya.", ["melainkan", "tetapi", "dan", "atau"], 1),
            ("「〜または…」を表す接続詞は？", ["atau", "dan", "tetapi", "karena"], 1),
            ("「彼は背が高いが力は弱い」の接続詞は？", ["tetapi", "melainkan", "atau", "sehingga"], 1)
        ]
    },
    {
        "slug": "12-conjunction-subordinating",
        "title": "【瞬間作文】従属接続詞（karena, sehingga, agar, jika, walaupun）の複文組み立て",
        "intro": "理由（karena）、結果（sehingga）、目的（agar / supaya）、条件（jika / kalau）、譲歩（walaupun / meskipun）の従属接続詞を使いこなすと、幼稚な短文から論理的な複文へと表現力が飛躍します。条件と結果を瞬時に繋ぐトレーニングです。",
        "rules": [
            ("karena（理由・〜なので） vs sehingga（結果・その結果〜）", "karena は原因を導き、sehingga はその原因から生じた帰結を導きます。"),
            ("agar / supaya（目的・〜するために）", "望ましい状態を実現させるための目的節を導きます。口語では biar。"),
            ("jika / kalau（条件・もし〜なら）", "仮定・条件節。文頭に置くことも文中に置くことも可能です。"),
            ("walaupun / meskipun（譲歩・〜にもかかわらず）", "反対の事実を提示しながら主節を強調します。")
        ],
        "drill": [
            ("雨が降っているので、私は家にいます。", "Karena hujan, saya tinggal di rumah.", "カルナ フジャン サヤ ティンガル ディ ルマ", "理由節 Karena hujan。"),
            ("彼は一生懸命勉強したので、試験に合格しました。", "Dia belajar keras sehingga lulus ujian.", "ディア ブラジャール クラス スヒンガ ルルス ウジアン", "結果節 sehingga lulus。"),
            ("健康でいられるように、野菜をたくさん食べなさい。", "Makanlah banyak sayur agar tetap sehat.", "マカンラ バニャッ サユール アガル トゥタップ スハット", "目的節 agar tetap sehat。"),
            ("もし時間があれば、映画を見に行きましょう。", "Jika ada waktu, mari kita pergi menonton film.", "ジカ アダ ワクトゥ マリ キタ プルギ ムノントン フィルム", "条件節 Jika ada waktu。"),
            ("疲れていましたが、彼は仕事を続けました。", "Walaupun lelah, dia tetap melanjutkan pekerjaan.", "ワラウプン レラ ディア トゥタップ ムランジュットカン プケルジャアン", "譲歩節 Walaupun lelah。"),
            ("道が混んでいたので、遅刻しました。", "Karena jalanan macet, saya terlambat.", "カルナ ジャラナン マチェット サヤ トゥルランバット", "理由 Karena jalanan macet。"),
            ("風邪を引かないように、温かい服を着てください。", "Pakailah baju hangat supaya tidak masuk angin.", "パカイラ バジュ ハンガット スパヤ ティダッ マスッ アンギン", "目的 supaya tidak..."),
            ("もし明日雨が降ったら、遠足を中止します。", "Kalau besok hujan, piknik akan dibatalkan.", "カロウ ベソッ フジャン ピクニック アカン ディバタルカン", "口語条件 kalau。"),
            ("高いですが、品質は最高です。", "Meskipun mahal, kualitasnya terbaik.", "ムスキプン マハル クアリタスニャ トゥルバイッ", "譲歩 Meskipun mahal。"),
            ("お金が足りなかったので、買いませんでした。", "Karena uangnya tidak cukup, saya tidak membeli.", "カルナ ウアンニャ ティダッ チュクップ サヤ ティダッ ムンブリ", "理由 Karena uangnya..."),
            ("みんなが理解できるように、ゆっくり話してください。", "Tolong bicara pelan-pelan agar semua orang paham.", "トロン ビチャラ プランプラン アガル スムア オラン パハム", "目的 agar semua paham。"),
            ("彼はお金をたくさん持っているけれど、質素に暮らしている。", "Meskipun punya banyak uang, dia hidup sederhana.", "ムスキプン プニャ バニャッ ウアン ディア ヒドゥップ スデルハナ", "譲歩 Meskipun..."),
            ("早く寝れば、明日早く起きられます。", "Jika tidur lebih awal, Anda bisa bangun pagi besok.", "ジカ ティドゥール ルビ アワル アンダ ビサ バングン パギ ベソッ", "条件 Jika..."),
            ("大雨が降って、その結果洪水が起きました。", "Hujan deras turun sehingga terjadi banjir.", "フジャン ドゥラス トゥルン スヒンガ トゥルジャディ バンジール", "結果 sehingga terjadi..."),
            ("あなたが幸せなら、私も嬉しいです。", "Kalau kamu bahagia, saya juga senang.", "カロウ カム バハギア サヤ ジュガ スナン", "条件 Kalau... ")
        ],
        "quiz": [
            ("「〜するために（目的）」を導く接続詞は？", ["agar", "karena", "sehingga", "walaupun"], 1),
            ("「その結果〜（帰結）」を導く接続詞は？", ["sehingga", "karena", "jika", "meskipun"], 1),
            ("「〜にもかかわらず（譲歩）」を導く接続詞は？", ["walaupun", "karena", "supaya", "kalau"], 1)
        ]
    },
    {
        "slug": "13-classifiers-counting",
        "title": "【瞬間作文】助数詞（orang, ekor, buah, batang, lembar）と数量詞の即時産出",
        "intro": "物を数える時、インドネシア語では「数 ＋ 助数詞 ＋ 名詞」の順で並べます。数詞「1」と助数詞が合体して「se-」になる規則（seorang, seekor, sebuah）を反射的に口から出せるようにします。",
        "rules": [
            ("主要助数詞 5選", "orang（人間）、ekor（動物）、buah（一般の物・建物・果物・抽象名詞）、batang（細長い棒状の物・タバコ・木）、lembar（薄い紙・布・チケット）。"),
            ("数詞 1 の接頭辞 se- 化", "satu orang → seorang、satu ekor → seekor、satu buah → sebuah、satu lembar → selembar。2以上は dua orang, tiga buah と通常通り。")
        ],
        "drill": [
            ("1人の医者", "seorang dokter", "スオラン ドクテル", "人間1人 seorang。"),
            ("3人の学生", "tiga orang mahasiswa", "ティガ オラン マハシスワ", "人間複数 tiga orang。"),
            ("1匹の猫", "seekor kucing", "スエコル クチン", "動物1匹 seekor。"),
            ("2羽の鳥", "dua ekor burung", "ドゥア エコル ブルン", "動物複数 dua ekor。"),
            ("1個のリンゴ", "sebuah apel", "スブア アペル", "果物・物体1個 sebuah。"),
            ("5台の車", "lima buah mobil", "リマ ブア モビル", "車両・機械 lima buah。"),
            ("1本の鉛筆", "sebatang pensil", "スバタン ペンシル", "細長い物1本 sebatang。"),
            ("3本のタバコ", "tiga batang rokok", "ティガ バタン ロコッ", "棒状 tiga batang。"),
            ("1枚の紙", "selembar kertas", "スルンバール クルタス", "薄い紙1枚 selembar。"),
            ("2枚の航空券", "dua lembar tiket pesawat", "ドゥア ルンバール ティケット プサワット", "薄いチケット dua lembar。"),
            ("私は昨日、1冊の面白い本を買いました。", "Kemarin saya membeli sebuah buku menarik.", "クマリン サヤ ムンブリ スブア ブク ムナリッ", "本1冊 sebuah buku。"),
            ("庭に2匹の犬がいます。", "Ada dua ekor anjing di halaman.", "アダ ドゥア エコル アンジン ディ ハラマン", "犬2匹 dua ekor anjing。"),
            ("手紙を1枚書いてください。", "Tolong tulis selembar surat.", "トロン トゥリス スルンバール スラット", "手紙1通・1枚 selembar surat。"),
            ("道端に大きな木が1本立っています。", "Sebatang pohon besar berdiri di pinggir jalan.", "スバタン ポホン ブサール ブルディリ ディ ピンギール ジャラン", "木1本 sebatang pohon。"),
            ("会議室には10人の参加者がいます。", "Ada sepuluh orang peserta di ruang rapat.", "アダ スプル オラン プスルタ ディ ルアン ラパット", "10人 sepuluh orang。")
        ],
        "quiz": [
            ("「1匹の犬」の正しいインドネシア語は？", ["seekor anjing", "seorang anjing", "sebuah anjing", "sebatang anjing"], 1),
            ("「紙やチケット」を数える助数詞は？", ["lembar", "batang", "ekor", "buah"], 1),
            ("「鉛筆やタバコ」を数える助数詞は？", ["batang", "buah", "lembar", "orang"], 1)
        ]
    },
    {
        "slug": "14-existential-ada",
        "title": "【瞬間作文】存在表現 ada の多機能構文（所有・存在・強調）の瞬間生成",
        "intro": "インドネシア語の「ada」は、物理的「存在（〜がある/いる）」だけでなく、「所有（〜を持っている）」や「事実の強調（確かに〜である）」など多彩な顔を持ちます。日本語の直訳癖を捨てて ada 構文を自由自在に操るドリルです。",
        "rules": [
            ("存在の ada（場所に〜がある/いる）", "「Ada [物/人] di [場所]」または「Di [場所] ada [物/人]」。Ada kucing di bawah meja（机の下に猫がいる）。"),
            ("所有の ada（主語には〜がある＝持っている）", "「[人] ada [物]」。Saya ada uang（私にはお金がある＝お金を持っている）。punya とほぼ同義ですが、より日常的。"),
            ("有無の確認（〜はありますか？）", "Ada gula?（砂糖はありますか？）"),
            ("否定（ない/いない）", "tidak ada を使用。Tidak ada masalah（問題ありません）。")
        ],
        "drill": [
            ("机の上に本があります。", "Ada buku di atas meja.", "アダ ブク ディ アタス メジャ", "存在 Ada buku..."),
            ("今日、時間ありますか？", "Apakah Anda ada waktu hari ini?", "アカパ アンダ アダ ワクトゥ ハリ イニ", "所有・時間の余裕 ada waktu?"),
            ("質問はありますか？", "Ada pertanyaan?", "アダ プルタニャアン", "有無の確認 Ada pertanyaan?"),
            ("問題ありません。", "Tidak ada masalah.", "ティダッ アダ マサラ", "存在否定 Tidak ada masalah."),
            ("部屋の中に誰もいません。", "Tidak ada siapa-siapa di dalam kamar.", "ティダッ アダ シアパシアパ ディ ダラム カマール", "人物の不在 Tidak ada siapa-siapa."),
            ("何か良いアイデアはありますか？", "Ada ide bagus?", "アダ イデ バグス", "有無の確認 Ada ide bagus?"),
            ("私は今、細かいお金を持っていません。", "Saya tidak ada uang kecil sekarang.", "サヤ ティダッ アダ ウアン クチル スカラン", "所有否定 tidak ada uang kecil。"),
            ("駅の近くに美味しいレストランがあります。", "Ada restoran enak di dekat stasiun.", "アダ レストラン エナッ ディ ドゥカット スタシウン", "場所の存在 Ada restoran..."),
            ("何か手伝えることはありますか？", "Ada yang bisa saya bantu?", "アダ ヤン ビサ サヤ バントゥ", "超頻出サービス表現 Ada yang bisa..."),
            ("明日、重要な会議があります。", "Besok ada rapat penting.", "ベソッ アダ ラパット ポンティン", "予定・イベントの存在 Ada rapat."),
            ("冷蔵庫の中に何もありません。", "Tidak ada apa-apa di dalam kulkas.", "ティダッ アダ アパアパ ディ ダラム クルカス", "完全否定 Tidak ada apa-apa."),
            ("車にガソリンは入っていますか？", "Ada bensin di mobil?", "アダ ベンシン ディ モビル", "有無確認 Ada bensin?"),
            ("あそこに警察官がいます。", "Ada polisi di sana.", "アダ ポリシ ディ サナ", "人物の存在 Ada polisi."),
            ("何か用事がありますか？", "Ada perlu apa?", "アダ プルル アパ", "用件の確認 Ada perlu apa?"),
            ("チャンスはまだあります。", "Masih ada kesempatan.", "マシ アダ クスンパタン", "継続存在 Masih ada kesempatan.")
        ],
        "quiz": [
            ("店員が客に「何かお手伝いしましょうか？」と声をかける定番表現は？", ["Ada yang bisa saya bantu?", "Punya apa Anda?", "Bisa apa di sini?", "Mau apa kamu?"], 1),
            ("「問題ありません」の正しい表現は？", ["Tidak ada masalah.", "Bukan ada masalah.", "Jangan ada masalah.", "Belum ada masalah."], 1),
            ("「誰もいない」を表すフレーズは？", ["tidak ada siapa-siapa", "tidak ada apa-apa", "bukan siapa-siapa", "belum siapa-siapa"], 1)
        ]
    },
    {
        "slug": "15-imperatives-requests",
        "title": "【瞬間作文】依頼・指示・禁止（tolong, silakan, harap, jangan, dilarang）",
        "intro": "人に何かを頼む・促す・禁止する表現は、語気や敬意の度合いを誤ると重大な人間関係トラブルになります。最も丁寧な「tolong / silakan」から、公的指示「harap」、厳格な禁止「dilarang / jangan」までを即時選別します。",
        "rules": [
            ("tolong（〜してください・お願い）", "相手に行動を依頼する最も一般的で丁寧な言葉。Tolong bantu saya（助けてください）。"),
            ("silakan（どうぞ〜してください・勧奨）", "相手に許可や推奨を与える丁寧な表現。Silakan masuk（どうぞお入りください）。"),
            ("harap / mohon（〜してください・公的要請）", "アナウンスや公的掲示、ビジネス文書での強い丁寧要請。Harap tenang（お静かに願います）。"),
            ("jangan（〜しないで・禁止）", "日常会話での禁止。「Jangan lupa（忘れないで）」。"),
            ("dilarang（〜禁止・公的標識）", "公の規則・法律による禁止。「Dilarang merokok（喫煙禁止）」。")
        ],
        "drill": [
            ("手伝ってください。", "Tolong bantu saya.", "トロン バントゥ サヤ", "丁寧な依頼 tolong。"),
            ("どうぞお座りください。", "Silakan duduk.", "シラカン ドゥドゥッ", "丁寧な勧奨 silakan。"),
            ("ドアを閉めてください。", "Tolong tutup pintunya.", "トロン トゥトゥップ ピントゥニャ", "依頼 tolong tutup。"),
            ("忘れないでくださいね。", "Jangan lupa ya.", "ジャンガン ルパ ヤ", "日常禁止 jangan lupa。"),
            ("ここでタバコを吸わないでください（日常）。", "Jangan merokok di sini.", "ジャンガン ムロコッ ディ シニ", "日常禁止 jangan。"),
            ("【看板】喫煙禁止", "Dilarang merokok.", "ディララン ムロコッ", "公的禁止掲示 dilarang。"),
            ("お静かに願います（アナウンス）。", "Harap tenang.", "ハラップ トゥナン", "公的要請 harap tenang。"),
            ("どうぞ召し上がってください。", "Silakan makan.", "シラカン マカン", "食事の勧め silakan。"),
            ("パスポートを見せてください。", "Tolong perlihatkan paspor Anda.", "トロン プルリハッカン パスポル アンダ", "公的依頼 tolong perlihatkan。"),
            ("怒らないでください。", "Jangan marah.", "ジャンガン マラ", "感情の制止 jangan marah。"),
            ("【看板】駐車禁止", "Dilarang parkir di sini.", "ディララン パルキール ディ シニ", "公的禁止 Dilarang parkir。"),
            ("少々お待ちください。", "Tolong tunggu sebentar.", "トロン トゥング スブンタール", "依頼 tolong tunggu sebentar。"),
            ("シートベルトを着用してください（機内）。", "Harap kenakan sabuk pengaman.", "ハラップ クナカン サブッ プンガマン", "安全アナウンス Harap kenakan。"),
            ("遠慮しないでください。", "Jangan sungkan-sungkan.", "ジャンガン スンカンスンカン", "気遣い jangan sungkan。"),
            ("どうぞ先にお通りください。", "Silakan jalan duluan.", "シラカン ジャラン ドゥルアン", "譲り合い Silakan... ")
        ],
        "quiz": [
            ("「どうぞ〜してください（勧奨）」を表す丁寧な言葉は？", ["silakan", "tolong", "jangan", "dilarang"], 1),
            ("公共標識で「立ち入り禁止」を表す語句は？", ["Dilarang masuk", "Jangan masuk", "Silakan masuk", "Harap masuk"], 1),
            ("「忘れないでね」の自然な日常会話フレーズは？", ["Jangan lupa ya.", "Dilarang lupa ya.", "Harap lupa ya.", "Silakan lupa ya."], 1)
        ]
    },
    {
        "slug": "16-passive-prefix-di",
        "title": "【瞬間作文】三人称 di- 受動態の瞬間組み立て（Diperiksa oleh dokter）",
        "intro": "インドネシア語の受動態は、三人称（彼、彼女、彼ら、人名、物）が動作主の場合に接頭辞「di-」を使います。客観的な事実報道やビジネス文書の主役である di- 受動態を反射的に組み立てるドリルです。",
        "rules": [
            ("di- 構文の公式", "【被行為者（主語） ＋ di-動詞 ＋ (oleh) ＋ 動作主（三人称）】。oleh は動作主が動詞の直後に来る場合は省略可能です。"),
            ("動作主の制限", "di- は原則として「三人称」のみに適用されます。一人称（saya）や二人称（kamu）には語幹受動態を使います。"),
            ("アスペクトの位置", "sudah, belum, akan などの副詞は必ず di-動詞の「前」に置きます（Sudah diperbaiki）。")
        ],
        "drill": [
            ("車は修理工によって修理されました。", "Mobil diperbaiki oleh montir.", "モビル ディプルバイキ オレ モンティル", "di- 受動態。"),
            ("その手紙は社長によって署名されました。", "Surat itu ditandatangani oleh direktur.", "スラット イトゥ ディタンダタンガニ オレ ディレクトゥール", "公式文書 di-。"),
            ("患者は医師によって診察されました。", "Pasien diperiksa oleh dokter.", "パシエン ディプルイクサ オレ ドクテル", "診察 di- 受動態。"),
            ("この小説は有名な作家によって書かれました。", "Novel ini ditulis oleh penulis terkenal.", "ノフェル イニ ディトゥリス オレ プヌリス トゥルクナル", "執筆 ditulis oleh..."),
            ("その家はすでに銀行によって売却されました。", "Rumah itu sudah dijual oleh bank.", "ルマ イトゥ スダ ディジュアル オレ バンク", "完了 sudah dijual。"),
            ("この料理はお母さんによって作られました。", "Makanan ini dimasak oleh ibu.", "マカナン イニ ディマサッ オレ イブ", "調理 dimasak oleh ibu。"),
            ("会議は来週に延期されました。", "Rapat ditunda sampai minggu depan.", "ラパット ディトゥンダ サンパイ ミング ドゥパン", "延期 ditunda。"),
            ("その犬は近所の人々に世話されています。", "Anjing itu dirawat oleh warga sekitar.", "アンジン イトゥ ディラワット オレ ワルガ スキタール", "世話 dirawat。"),
            ("新しい法律が政府によって公布されました。", "Undang-undang baru diumumkan oleh pemerintah.", "ウンダンウンダン バル ディウムムカン オレ プムリンタ", "公布 diumumkan。"),
            ("泥棒は警察に逮捕されました。", "Pencuri ditangkap oleh polisi.", "プンチュリ ディタンカップ オレ ポリシ", "逮捕 ditangkap。"),
            ("このビルは地震によって破壊されました。", "Gedung ini dihancurkan oleh gempa bumi.", "グドゥン イニ ディハンチュルカン オレ グムパ ブミ", "破壊 dihancurkan。"),
            ("荷物は昨日、配達員によって届けられました。", "Paket dikirim oleh kurir kemarin.", "パケット ディキリム オレ クリル クマリン", "配達 dikirim。"),
            ("新薬は研究者たちによってテストされています。", "Obat baru sedang diuji oleh para peneliti.", "オバット バル スダン ディウジ オレ パラ プヌリティ", "進行 sedang diuji。"),
            ("その提案は上司によって拒否されました。", "Usulan itu ditolak oleh atasan.", "ウスラン イトゥ ディトラッ オレ アタサン", "拒否 ditolak。"),
            ("この問題は専門家によって議論される予定です。", "Masalah ini akan dibahas oleh para ahli.", "マサラ イニ アカン ディバハス オレ パラ アフリ", "未来 akan dibahas。")
        ],
        "quiz": [
            ("接頭辞 di- を使った受動態の動作主として文法的に正しいのは？", ["三人称（dokter, mereka, dia）", "一人称（saya）", "二人称（kamu, Anda）", "常に省略しなければならない"], 1),
            ("「その本は彼によって読まれた」の正しい文は？", ["Buku itu dibaca oleh dia.", "Buku itu saya dibaca.", "Buku itu kamu dibaca.", "Buku itu membaca dia."], 1),
            ("「会議は延期された」の受動態は？", ["Rapat ditunda.", "Rapat menunda.", "Rapat bertunda.", "Rapat tertunda."], 1)
        ]
    },
    {
        "slug": "17-passive-stem-first-person",
        "title": "【瞬間作文】一人称語幹受動態（Buku ini sudah saya baca）の自動発話化",
        "intro": "日本人学習者が最もつまずきやすく、かつネイティブが日常会話で最も多用するのが「一人称語幹受動態」です。「Saya sudah membaca buku ini（能動態）」よりも「Buku ini sudah saya baca（語幹受動態）」の方が圧倒的に自然です。この語順を無意識に繰り出すドリルです。",
        "rules": [
            ("一人称語幹受動態の鉄則", "【目的物（主語） ＋ (アスペクト/助動詞) ＋ saya / aku ＋ 語幹動詞（接頭辞なし）】。Buku ini saya baca。"),
            ("絶対にやってはいけない誤用", "❌ Buku ini dibaca oleh saya（三人称の di- を一人称に使うのは不自然・誤用）。"),
            ("人称代名詞と語幹の不可分性", "saya と動詞の語幹の間には、原則として副詞を挟みません。「sudah saya baca」であり、「saya sudah baca」も可能ですが、アスペクトを前に置くのが標準的です。")
        ],
        "drill": [
            ("その本は私が読みました。", "Buku itu sudah saya baca.", "ブク イトゥ スダ サヤ バチャ", "語幹 baca（接頭辞 meN- なし）。"),
            ("そのレポートは私が書きました。", "Laporan itu sudah saya tulis.", "ラポラン イトゥ スダ サヤ トゥリス", "語幹 tulis。"),
            ("コーヒーは私が買いました。", "Kopi sudah saya beli.", "コピ スダ サヤ ブリ", "語幹 beli。"),
            ("そのメールは私が送りました。", "Email itu sudah saya kirim.", "イーメール イトゥ スダ サヤ キリム", "語幹 kirim。"),
            ("部屋は私が掃除しました。", "Kamar sudah saya bersihkan.", "カマール スダ サヤ ブルシカン", "語幹 bersihkan。"),
            ("その問題は私が解決します。", "Masalah itu akan saya selesaikan.", "マサラ イトゥ アカン サヤ スルサイカン", "未来 akan saya selesaikan。"),
            ("その提案は私が引き受けます。", "Usulan itu saya terima.", "ウスラン イトゥ サヤ トゥリマ", "語幹 terima。"),
            ("そのお金は私が払いました。", "Uang itu sudah saya bayar.", "ウアン イトゥ スダ サヤ バヤル", "語幹 bayar。"),
            ("書類は私が確認しました。", "Dokumen sudah saya periksa.", "ドクメン スダ サヤ プルイクサ", "語幹 periksa。"),
            ("宿題は私がもう終えました。", "PR sudah saya selesaikan.", "ペーエル スダ サヤ スルサイカン", "語幹 selesaikan。"),
            ("その秘密は私が知っています。", "Rahasia itu saya ketahui.", "ラハシア イトゥ サヤ クタフイ", "語幹 ketahui。"),
            ("荷物は私が持っていきます。", "Barang akan saya bawa.", "バラン アカン サヤ バワ", "未来 akan saya bawa。"),
            ("その知らせは私が伝えました。", "Kabar itu sudah saya sampaikan.", "カバール イトゥ スダ サヤ サンパイカン", "語幹 sampaikan。"),
            ("車は私が洗いました。", "Mobil sudah saya cuci.", "モビル スダ サヤ チュチ", "語幹 cuci。"),
            ("その料理は私が作りました。", "Makanan itu saya buat.", "マカナン イトゥ サヤ ブアット", "語幹 buat。")
        ],
        "quiz": [
            ("「その手紙は私が書いた」の最も自然なインドネシア語は？", ["Surat itu sudah saya tulis.", "Surat itu ditulis oleh saya.", "Saya sudah ditulis surat itu.", "Surat itu menulis saya."], 1),
            ("一人称語幹受動態で使われる動詞の形は？", ["語幹（接頭辞なし）", "di- 動詞", "meN- 動詞", "ber- 動詞"], 1),
            ("「この件は私が処理します」を語幹受動態で言うと？", ["Hal ini akan saya urus.", "Hal ini diurus oleh saya.", "Saya diurus hal ini.", "Hal ini mengurus saya."], 1)
        ]
    },
    {
        "slug": "18-passive-stem-second-person",
        "title": "【瞬間作文】二人称語幹受動態（Tugas ini harus kamu selesaikan）の反射出力",
        "intro": "相手（あなた・君）に対して「あなたが〜する」という行為を、目的語を主語にして優しく促したり確認したりする表現です。「Tugas ini harus kamu kerjakan（この課題は君がやらなきゃ）」のように、二人称でも語幹受動態を用います。",
        "rules": [
            ("二人称語幹受動態の公式", "【目的物（主語） ＋ (助動詞) ＋ kamu / Anda ＋ 語幹動詞】。"),
            ("相手への配慮・依頼のトーン", "命令形「Beli ini!（これ買え）」よりも「Ini bisa kamu beli（これは君が買えるよ）」の方が柔らかく響きます。"),
            ("di- を使わない鉄則", "一人称同様、❌ Ini harus dibeli oleh kamu とは言いません。Ini harus kamu beli とします。")
        ],
        "drill": [
            ("この課題は君が終えなければならない。", "Tugas ini harus kamu selesaikan.", "トゥガス イニ ハルス カム スルサイカン", "二人称語幹 selesaikan。"),
            ("この本はもう読みましたか？", "Apakah buku ini sudah Anda baca?", "アカパ ブク イニ スダ アンダ バチャ", "完了確認 sudah Anda baca。"),
            ("この薬を飲まなければなりません。", "Obat ini harus Anda minum.", "オバット イニ ハルス アンダ ミヌム", "義務 harus Anda minum。"),
            ("この車を運転できますか？", "Mobil ini bisa kamu setir?", "モビル イニ ビサ カム スティル", "可能 bisa kamu setir?"),
            ("この書類にサインしてください。", "Dokumen ini tolong Anda tandatangani.", "ドクメン イニ トロン アンダ タンダタンガニ", "依頼 tolong Anda tandatangani。"),
            ("この料理は君が食べるべきだ。", "Makanan ini harus kamu coba.", "マカナン イニ ハルス カム チョバ", "推奨 harus kamu coba。"),
            ("この問題はあなたが決めてください。", "Masalah ini silakan Anda putuskan.", "マサラ イニ シラカン アンダ プトゥスカン", "決定依頼 silakan Anda putuskan。"),
            ("鍵はどこに置きましたか？", "Kuncinya kamu taruh di mana?", "クンチニャ カム タルー ディ マナ", "疑問 kuncinya kamu taruh..."),
            ("この部屋は君が掃除してね。", "Kamar ini tolong kamu bersihkan ya.", "カマール イニ トロン カム ブルシカン ヤ", "親しい依頼 tolong kamu bersihkan。"),
            ("その荷物はあなたが受け取ってください。", "Paket itu silakan Anda terima.", "パケット イトゥ シラカン アンダ トゥリマ", "受取 silakan Anda terima。"),
            ("このペンを使っていいですよ。", "Pulpen ini boleh kamu pakai.", "プルペン イニ ボレ カム パカイ", "許可 boleh kamu pakai。"),
            ("そのお金は君が保管しておきなさい。", "Uang itu harus kamu simpan.", "ウアン イトゥ ハルス カム シンパン", "保管 harus kamu simpan。"),
            ("その知らせを君はもう聞いた？", "Kabar itu sudah kamu dengar?", "カバール イトゥ スダ カム ドンガル", "確認 sudah kamu dengar?"),
            ("この機会を逃してはならない。", "Peluang ini tidak boleh kamu lewatkan.", "プルアン イニ ティダッ ボレ カム レワットカン", "機会 tidak boleh kamu lewatkan。"),
            ("この服は君が着るのにぴったりだ。", "Baju ini cocok kamu pakai.", "バジュ イニ チョチョッ カム パカイ", "適合 cocok kamu pakai。")
        ],
        "quiz": [
            ("「この本はあなたが読むべきだ」の正しい語幹受動態は？", ["Buku ini harus Anda baca.", "Buku ini harus dibaca oleh Anda.", "Anda harus membaca buku ini.", "Buku ini Anda dibaca."], 1),
            ("二人称語幹受動態の動詞の接頭辞は？", ["接頭辞なし（語幹のみ）", "di-", "meN-", "ter-"], 1),
            ("「鍵は君が持ってる？」の自然な口語語幹受動態は？", ["Kuncinya kamu bawa?", "Kuncinya dibawa oleh kamu?", "Kamu membawa kuncinya?", "Kuncinya membawakan kamu?"], 1)
        ]
    },
    {
        "slug": "19-prefix-men-transitive",
        "title": "【瞬間作文】接頭辞 meN- 他動詞の鼻音化と即時発話（membeli, menulis, melihat）",
        "intro": "インドネシア語の能動他動詞を作る接頭辞「meN-」は、語根の語頭子音によって 6種類（me-, mem-, men-, meng-, meny-, menge-）に鼻音化変化します。頭で規則を計算するのではなく、語根を聞いた瞬間に正しい音で口から飛び出す反射神経を養います。",
        "rules": [
            ("鼻音化の基本4大脱落（K, T, S, P）", "語根の先頭が K, T, S, P の場合、子音が脱落して鼻音に同化します：kirim → mengirim、tulis → menulis、siram → menyiram、pakai → memakai。"),
            ("有声子音の同化（B, D, J, G）", "脱落せずに残ります：beli → membeli、dengar → mendengar、jual → menjual、goreng → menggoreng。"),
            ("母音・H・R・L・W・Y", "meng- または me- に接続：ambil → mengambil、lihat → melihat、rawat → merawat。")
        ],
        "drill": [
            ("母は野菜を買います（語根: beli）。", "Ibu membeli sayur.", "イブ ムンブリ サユール", "beli → membeli（Bは残る）。"),
            ("彼は手紙を書きます（語根: tulis）。", "Dia menulis surat.", "ディア ムヌリス スラット", "tulis → menulis（Tは脱落してNに）。"),
            ("私は友達を見ました（語根: lihat）。", "Saya melihat teman.", "サヤ ムリハット トゥマン", "lihat → melihat。"),
            ("父はコーヒーを飲みます（語根: minum）。", "Ayah meminum kopi.", "アヤ メミヌム コピ", "minum → meminum。"),
            ("彼らは新しい車を洗っています（語根: cuci）。", "Mereka mencuci mobil baru.", "ムレカ ムンチュチ モビル バル", "cuci → mencuci。"),
            ("彼女は新しい服を着ます（語根: pakai）。", "Dia memakai baju baru.", "ディア メマカイ バジュ バル", "pakai → memakai（Pは脱落してMに）。"),
            ("社長は小包を送りました（語根: kirim）。", "Direktur mengirim paket.", "ディレクトゥール ムンギリム パケット", "kirim → mengirim（Kは脱落してNGに）。"),
            ("兄は花に水をやっています（語根: siram）。", "Kakak menyiram bunga.", "カカッ ムニィラム ブンガ", "siram → menyiram（Sは脱落してNYに）。"),
            ("私たちは魚を焼きます（語根: bakar）。", "Kami membakar ikan.", "カミ ムンバカール イカン", "bakar → membakar。"),
            ("彼は私の話をよく聞きます（語根: dengar）。", "Dia mendengar cerita saya.", "ディア ムンドンガル チュリタ サヤ", "dengar → mendengar。"),
            ("彼女はお金を数えています（語根: hitung）。", "Dia menghitung uang.", "ディア ムンヒトウン ウアン", "hitung → menghitung。"),
            ("私たちは問題を議論します（語根: bahas）。", "Kami membahas masalah.", "カミ ムンバハス マサラ", "bahas → membahas。"),
            ("彼は鍵を取りました（語根: ambil）。", "Dia mengambil kunci.", "ディア ムンガンビル クンチ", "ambil → mengambil。"),
            ("先生は質問に答えます（語根: jawab）。", "Guru menjawab pertanyaan.", "グル ムンジャワブ プルタニャアン", "jawab → menjawab。"),
            ("妹はリンゴを切っています（語根: potong）。", "Adik memotong apel.", "アディッ メモトン アペル", "potong → memotong（Pは脱落）。")
        ],
        "quiz": [
            ("語根 tulis（書く）に meN- がついた時の正しい形は？", ["menulis", "mentulis", "metulis", "mengtulis"], 1),
            ("語根 kirim（送る）に meN- がついた時の正しい形は？", ["mengirim", "menkirim", "mekirim", "memkirim"], 1),
            ("語根 pakai（使う・着る）に meN- がついた時の正しい形は？", ["memakai", "mempakai", "mepakai", "menpakai"], 1)
        ]
    },
    {
        "slug": "20-prefix-men-intransitive",
        "title": "【瞬間作文】接頭辞 meN- 自動詞と状態変化（menangis, mendarat, menguning）",
        "intro": "meN- は他動詞だけでなく、目的語をとらない「自動詞」や、自然な「状態変化（〜になる）」、音の発声などを表す重要動詞群を形成します。日常会話で感情や状況を生き生きと描写する自動詞を反射出力します。",
        "rules": [
            ("感情・生理的動作の自動詞", "menangis（泣く）、merintih（うめく）、menguap（あくびをする/蒸発する）。"),
            ("場所・目標への移動・到達", "mendarat（着陸する：darat=陸）、melaut（出漁する：laut=海）、menepi（端に寄る：tepi=端）。"),
            ("状態変化・色彩化（〜になる）", "menguning（黄色くなる：kuning=黄色）、membesar（大きくなる：besar=大きい）、mengecil（小さくなる）。")
        ],
        "drill": [
            ("赤ちゃんがベッドで泣いています。", "Bayi menangis di tempat tidur.", "バイ ムナンギス ディ トゥムパット ティドゥール", "生理動作 menangis。"),
            ("飛行機は時間通りに着陸しました。", "Pesawat mendarat tepat waktu.", "プサワット ムンダラット トゥパット ワクトゥ", "到達 mendarat（darat=陸）。"),
            ("秋になり、葉が黄色くなりました。", "Daun-daun menguning di musim gugur.", "ダウンダウン ムングニン ディ ムシム ググール", "状態変化 menguning。"),
            ("漁師たちは夜に出漁します。", "Para nelayan melaut pada malam hari.", "パラ ヌラヤン ムラウット パダ マラム ハリ", "移動 melaut（laut=海）。"),
            ("タクシーが道端に寄りました。", "Taksi menepi di pinggir jalan.", "タクシ ムヌピ ディ ピンギール ジャラン", "移動 menepi（tepi=端）。"),
            ("彼は眠くてあくびをしました。", "Dia menguap karena mengantuk.", "ディア ムングアップ カルナ ムンガントゥッ", "動作 menguap。"),
            ("山火事の煙が空へ立ち上りました。", "Asap membubung ke angkasa.", "アサップ ムンブブン ク アンカサ", "移動 membubung。"),
            ("会社の規模は年々大きくなっています。", "Ukuran perusahaan membesar setiap tahun.", "ウクラン プルサハアン ムンブサール スティアプ タフン", "状態変化 membesar。"),
            ("雨が降って川の水位が増しました。", "Air sungai meluap karena hujan.", "アイル スンガイ ムルアップ カルナ フジャン", "氾濫 meluap。"),
            ("彼女の顔は怒りで赤くなりました。", "Wajahnya memerah karena marah.", "ワジャニャ ムメラ カルナ マラ", "色彩変化 memerah（merah=赤）。"),
            ("その噂は街中に急速に広がりました。", "Rumor itu meluas dengan cepat di kota.", "ルモール イトゥ ムルアス ドゥンガン チパット ディ コタ", "状態変化 meluas（luas=広い）。"),
            ("船は西へ針路をとって進みました。", "Kapal menuju ke arah barat.", "カパル ムヌジュ ク アラ バラット", "目標方向 menuju（tuju=目標）。"),
            ("彼の病状は徐々に悪化しました。", "Kondisinya memburuk secara perlahan.", "コンディシニャ ムンブルッ スチャラ プルラハン", "状態変化 memburuk（buruk=悪い）。"),
            ("事態は日増しに改善しています。", "Situasi membaik dari hari ke hari.", "シトゥアシ ムンバイッ ダリ ハリ ク ハリ", "状態変化 membaik（baik=良い）。"),
            ("犬が怪しい男に向かって吠えました。", "Anjing menggonggong ke arah pria mencurigakan.", "アンジン ムンゴンゴン ク アラ プリア ムンチュリガカン", "鳴き声 menggonggong。")
        ],
        "quiz": [
            ("飛行機が「着陸する」を表す動詞は？", ["mendarat", "melaut", "menepi", "menangis"], 1),
            ("「黄色くなる」という色の変化を表す動詞は？", ["menguning", "memerah", "membiru", "menghijau"], 1),
            ("「良くなる・改善する」を表す meN- 自動詞は？", ["membaik", "memburuk", "membesar", "mengecil"], 1)
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

print("Batch 1011-1020 generated successfully.")
