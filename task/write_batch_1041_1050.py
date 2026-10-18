"""Writer Script: Articles 1041 - 1050 for docs/output/
"""

articles_data = [
    {
        "slug": "41-complex-relative-yang",
        "title": "【瞬間作文】関係詞 yang による長文修飾と焦点化構文の即座組み立て",
        "intro": "インドネシア語の関係詞「yang」は、英語の who, which, that にあたる名詞修飾機能に加え、「〜なのは…だ」という主語の焦点化・分裂文（Cleft Sentence）を形成する最重要構文ツールです。名詞に節を繋ぎ、瞬時に言いたい主語を際立たせるドリルです。",
        "rules": [
            ("関係詞としての yang（〜である…）", "名詞 ＋ yang ＋ [動詞節 / 形容詞節]。orang yang tinggal di Jakarta（ジャカルタに住んでいる人）、mobil yang baru dibeli（新しく買われた車）。"),
            ("焦点化構文（〜なのは誰/何だ）", "「[主語] yang [述語]」。Dia yang memecahkan gelas itu（そのコップを割ったのは彼だ）。Saya yang bertanggung jawab（責任があるのは私だ）。")
        ],
        "drill": [
            ("昨日ここに来た人は私の先生です。", "Orang yang datang ke sini kemarin adalah guru saya.", "オラン ヤン ダタン ク シニ クマリン アダラ グル サヤ", "関係詞 yang datang..."),
            ("机の上にある本を取ってください。", "Tolong ambilkan buku yang ada di atas meja.", "トロン アンビルカン ブク ヤン アダ ディ アタス メジャ", "修飾 yang ada di atas meja。"),
            ("そのコップを割ったのは彼です（彼こそが割った）。", "Dia yang memecahkan gelas itu.", "ディア ヤン メメチャカン グラス イトゥ", "焦点化 Dia yang..."),
            ("このプロジェクトを指揮するのは私です。", "Saya yang memimpin proyek ini.", "サヤ ヤン メミンピン プロイェッ イニ", "焦点化 Saya yang..."),
            ("彼が書いた記事はとても面白い。", "Artikel yang dia tulis sangat menarik.", "アルティケル ヤン ディア トゥリス サンガット ムナリッ", "関係詞節 yang dia tulis。"),
            ("あそこでコーヒーを飲んでいる女性は誰ですか？", "Siapa wanita yang sedang minum kopi di sana?", "シアパ ワニタ ヤン スダン ミヌム コピ ディ サナ", "修飾 yang sedang minum..."),
            ("日本で作られた車はとても頑丈です。", "Mobil yang dibuat di Jepang sangat kuat.", "モビル ヤン ディブアット ディ ジュパン サンガット クアット", "受動修飾 yang dibuat..."),
            ("私たちが昨日泊まったホテル。", "Hotel yang kami inapi kemarin.", "ホテル ヤン カミ イナピ クマリン", "場所関係詞節 yang kami inapi。"),
            ("最初にゴールに到着した走者。", "Pelari yang pertama tiba di garis finis.", "プラリ ヤン プルタマ ティバ ディ ガリス フィニス", "最上 yang pertama tiba。"),
            ("困っている人々を助けるボランティア。", "Relawan yang membantu orang-orang yang kesulitan.", "レラワン ヤン メムバントゥ オランオラン ヤン クスリタン", "二重修飾 yang membantu..."),
            ("私に必要なのはお金ではなく時間です。", "Yang saya butuhkan bukan uang, melainkan waktu.", "ヤン サヤ ブトゥーカン ブカン ウアン ムラインカン ワクトゥ", "名詞化 Yang saya butuhkan..."),
            ("電話をかけてきたのは社長でした。", "Direktur yang menelepon tadi.", "ディレクトゥール ヤン メネレポン タディ", "焦点化 Direktur yang..."),
            ("最も高価な時計を選びなさい。", "Pilihlah jam tangan yang paling mahal.", "ピリラ ジャム タンガン ヤン パリン マハル", "形容詞修飾 yang paling mahal。"),
            ("真実を知っているのは彼女だけです。", "Hanya dia yang tahu kebenarannya.", "ハニャ ディア ヤン タフ クブナランニャ", "焦点化 Hanya dia yang..."),
            ("私たちが直面している問題は深刻です。", "Masalah yang kita hadapi sangat serius.", "マサラ ヤン キタ ハダピ サンガット セリウス", "修飾 yang kita hadapi。")
        ],
        "quiz": [
            ("「昨日来た人」を表す関係詞構文は？", ["orang yang datang kemarin", "orang datang yang kemarin", "yang orang datang kemarin", "orang kemarin yang datang"], 1),
            ("「割ったのは彼だ（彼こそが）」の焦点化文は？", ["Dia yang memecahkan.", "Dia memecahkan yang.", "Yang dia memecahkan.", "Memecahkan yang dia."], 1),
            ("「私が言いたいこと」を表す名詞節は？", ["Yang ingin saya katakan", "Saya ingin yang katakan", "Katakan yang saya ingin", "Ingin yang saya katakan"], 1)
        ]
    },
    {
        "slug": "42-nominal-clause-bahwa",
        "title": "【瞬間作文】名詞節を導く bahwa 構文（Saya tahu bahwa...）の瞬間展開",
        "intro": "英語の「that節」に相当する「bahwa」は、「〜ということ」という事実・意見・伝聞・報告を導く名詞節を作ります。「Saya tahu bahwa...（私は〜であることを知っている）」「Dia mengatakan bahwa...（彼は〜だと言った）」など、知性的な複文を瞬時に口から出すドリルです。",
        "rules": [
            ("伝達・認識動詞 ＋ bahwa ＋ [完全な文]", "tahu bahwa（〜だと知っている）、mengatakan bahwa（〜だと言った）、berpikir bahwa（〜だと思う）、menyadari bahwa（〜だと気づく）、yakin bahwa（〜だと確信している）。"),
            ("主語節としての bahwa", "「Bahwa [文] adalah hal penting（〜ということは重要だ）」のように文頭に置くことも可能。")
        ],
        "drill": [
            ("彼が病気であることを私は知っています。", "Saya tahu bahwa dia sedang sakit.", "サヤ タフ バフワ ディア スダン サキッ", "Saya tahu bahwa..."),
            ("社長は明日来られないと言いました。", "Direktur mengatakan bahwa beliau tidak bisa datang besok.", "ディレクトゥール ムンガタカン バフワ ブリアウ ティダッ ビサ ダタン ベソッ", "mengatakan bahwa..."),
            ("私たちは彼が無実であると確信しています。", "Kami yakin bahwa dia tidak bersalah.", "カミ ヤキン バフワ ディア ティダッ ブルサラ", "yakin bahwa..."),
            ("彼女は自分が間違っていたことに気づいた。", "Dia menyadari bahwa dirinya keliru.", "ディア ムニャダリ バフワ ディリニャ クリルー", "menyadari bahwa..."),
            ("私はこの計画が成功すると信じています。", "Saya percaya bahwa rencana ini akan berhasil.", "サヤ プルチャヤ バフワ レンチャナ イニ アカン ブルハシル", "percaya bahwa..."),
            ("ニュースは明日の天気が晴れだと報じた。", "Berita melaporkan bahwa cuaca besok cerah.", "ブリタ ムラポルカン バフワ チュアチャ ベソッ チラ", "melaporkan bahwa..."),
            ("彼が正直な人間であることは誰もが知っている。", "Semua orang tahu bahwa dia orang jujur.", "スムア オラン タフ バフワ ディア オラン ジュジュル", "tahu bahwa..."),
            ("彼は手紙を受け取ったことを認めた。", "Dia mengakui bahwa dia menerima surat itu.", "ディア ムンガクイ バフワ ディア メネリマ スラット イトゥ", "mengakui bahwa..."),
            ("私はこれが最善の道であると思います。", "Saya merasa bahwa ini jalan terbaik.", "サヤ ムラサ バフワ イニ ジャラン トゥルバイッ", "merasa bahwa..."),
            ("彼らは試合に勝つことを望んでいる。", "Mereka berharap bahwa mereka akan menang.", "ムレカ ブルハラップ バフワ ムレカ アカン ムナン", "berharap bahwa..."),
            ("彼が仕事を辞めたという噂を聞きました。", "Saya mendengar rumor bahwa dia mengundurkan diri.", "サヤ ムンドンガル ルモール バフワ ディア ムングンドゥルカン ディリ", "rumor bahwa..."),
            ("時間が足りないということは明らかだ。", "Jelas bahwa waktunya tidak cukup.", "ジュラス バフワ ワクトゥニャ ティダッ チュクップ", "Jelas bahwa..."),
            ("先生は試験が延期されたと発表した。", "Guru mengumumkan bahwa ujian ditunda.", "グル ムングムムカン バフワ ウジアン ディトゥンダ", "mengumumkan bahwa..."),
            ("私たちは平和を愛する国民であるという事実。", "Fakta bahwa kita adalah bangsa yang cinta damai.", "ファクタ バフワ キタ アダラ バンサ ヤン チンタ ダマイ", "Fakta bahwa..."),
            ("彼が約束を守ることを私は確信している。", "Saya yakin bahwa dia akan menepati janjinya.", "サヤ ヤキン バフワ ディア アカン ムヌパティ ジャンジニャ", "yakin bahwa...")
        ],
        "quiz": [
            ("「〜ということ（that節）」を導く接続詞は？", ["bahwa", "yang", "karena", "sehingga"], 1),
            ("「彼が病気だと知っている」の正しい文は？", ["Saya tahu bahwa dia sakit.", "Saya tahu yang dia sakit.", "Saya tahu karena dia sakit.", "Saya tahu kalau dia sakit."], 1),
            ("「彼が無実であると確信している」は？", ["yakin bahwa dia tidak bersalah", "yakin yang dia tidak bersalah", "yakin agar dia tidak bersalah", "yakin supaya dia tidak bersalah"], 1)
        ]
    },
    {
        "slug": "43-concessive-meskipun",
        "title": "【瞬間作文】譲歩節（meskipun, walaupun, sungguhpun）による複文構築",
        "intro": "「〜にもかかわらず」「たとえ〜だとしても」という譲歩（Concession）は、相手の意見を受け止めつつ自分の主張を通す大人の会話に不可欠です。meskipun, walaupun, kendatipun を使った滑らかな論理展開をトレーニングします。",
        "rules": [
            ("譲歩の主要接続詞", "meskipun（〜だけれども）、walaupun（〜にもかかわらず）、kendatipun（格式高い譲歩：たとえ〜でも）、sungguhpun（文語的譲歩）。"),
            ("主節の namun / tetapi / tetap との呼応", "「Meskipun [譲歩節], [主語] tetap [述語]（〜だけれど、依然として…だ）」。")
        ],
        "drill": [
            ("雨が降っているけれど、私たちは出発します。", "Meskipun hujan, kita tetap berangkat.", "ムスキプン フジャン キタ トゥタップ ブルランカット", "Meskipun..., tetap..."),
            ("疲れていましたが、彼は仕事をやり遂げました。", "Walaupun lelah, dia menyelesaikan tugasnya.", "ワラウプン レラ ディア ムンユルサイカン トゥガスニャ", "Walaupun..."),
            ("値段は高いですが、品質は最高です。", "Meskipun mahal, kualitasnya nomor satu.", "ムスキプン マハル クアリタスニャ ノモル サトゥ", "Meskipun mahal..."),
            ("まだ若いけれど、彼は非常に経験豊富だ。", "Walaupun masih muda, dia sangat berpengalaman.", "ワラウプン マシ ムダ ディア サンガット ブルプンガラマン", "Walaupun masih muda..."),
            ("たとえ困難であっても、私たちは諦めません。", "Kendatipun sulit, kita tidak akan menyerah.", "クンダティプン スリット キタ ティダッ アカン ムニェラ", "Kendatipun sulit..."),
            ("薬を飲んだにもかかわらず、熱が下がりません。", "Meskipun sudah minum obat, demamnya belum turun.", "ムスキプン スダ ミヌム オバット ドマムニャ ブロン トゥルン", "Meskipun sudah..."),
            ("彼女はお金持ちだけれど、とても謙虚です。", "Walaupun kaya, dia sangat rendah hati.", "ワラウプン カヤ ディア サンガット ルンダ ハティ", "Walaupun kaya..."),
            ("道は混んでいましたが、時間通りに着きました。", "Meskipun jalan macet, kami tiba tepat waktu.", "ムスキプン ジャラン マチェット カミ ティバ トゥパット ワクトゥ", "Meskipun macet..."),
            ("夜遅かったけれど、彼は電話に出てくれた。", "Walaupun sudah larut malam, dia mengangkat telepon.", "ワラウプン スダ ラルット マラム ディア ムナンカット テレポン", "Walaupun larut malam..."),
            ("言葉は通じなくても、心は通じ合える。", "Meskipun berbeda bahasa, hati kita saling memahami.", "ムスキプン ブルベダ バハサ ハティ キタ サリン メマハミ", "Meskipun berbeda..."),
            ("何度失敗しても、彼は挑戦し続けた。", "Walaupun gagal berkali-kali, dia terus mencoba.", "ワラウプン ガガル ブルカリカリ ディア トゥルス ムンチョバ", "Walaupun gagal..."),
            ("体が小さくても、力は強い。", "Meskipun bertubuh kecil, tenaganya kuat.", "ムスキプン ブルトゥブ クチル トゥナガニャ クアット", "Meskipun kecil..."),
            ("たとえ嵐になろうとも、船は航海を続ける。", "Kendatipun badai datang, kapal tetap berlayar.", "クンダティプン バダイ ダタン カパル トゥタップ ブルラヤール", "Kendatipun badai..."),
            ("遠く離れていても、私たちは友達です。", "Meskipun tinggal berjauhan, kita tetap berteman.", "ムスキプン ティンガル ブルジャウハン キタ トゥタップ ブルトゥマン", "Meskipun berjauhan..."),
            ("忙しいけれど、運動する時間を作ります。", "Walaupun sibuk, saya meluangkan waktu olahraga.", "ワラウプン シブッ サヤ ムルアンカン ワクトゥ オラフラガ", "Walaupun sibuk...")
        ],
        "quiz": [
            ("「〜にもかかわらず（譲歩）」を表す接続詞ペアは？", ["meskipun / walaupun", "karena / sebab", "sehingga / akibatnya", "supaya / agar"], 1),
            ("「雨だけれど、依然として行く」の呼応副詞は？ Meskipun hujan, kita ___ pergi.", ["tetap", "sudah", "belum", "sedang"], 1),
            ("文語的・格式の高い譲歩接続詞は？", ["kendatipun", "soalnya", "kalo", "abisnya"], 1)
        ]
    },
    {
        "slug": "44-conditional-jika-seandainya",
        "title": "【瞬間作文】条件節・仮定法（jika, kalau, seandainya, asalkan）の瞬時産出",
        "intro": "現実の条件（jika / kalau: もし〜なら）から、事実と異なる仮定（seandainya / sekiranya: もしも〜だったら）、必要条件（asalkan: 〜でありさえすれば）まで、条件表現のレパートリーを瞬時に使い分けるドリルです。",
        "rules": [
            ("jika / kalau（現実的条件・もし〜なら）", "Jika ada waktu, kita pergi（時間があれば行こう）。kalau は日常口語、jika は標準的。"),
            ("seandainya / andaikata（反実仮想・もしも〜だったら）", "現実と異なる願望や仮定。「Seandainya saya punya sayap（もし私に翼があったなら）」。"),
            ("asalkan（条件限定・〜でさえあれば）", "「Asalkan kamu jujur, saya maafkan（君が正直でありさえすれば許す）」。")
        ],
        "drill": [
            ("もし明日晴れたら、海へ行きましょう。", "Jika besok cerah, mari kita pergi ke pantai.", "ジカ ベソッ チラ マリ キタ プルギ ク パンタイ", "現実条件 Jika..."),
            ("もし時間があれば、手伝ってください。", "Kalau ada waktu, tolong bantu saya.", "カロウ アダ ワクトゥ トロン バントゥ サヤ", "口語条件 Kalau..."),
            ("もし私が鳥だったら、空を自由に飛べるのに。", "Seandainya saya seekor burung, saya bisa terbang bebas.", "スアンダイニャ サヤ スエコル ブルン サヤ ビサ トゥルバン ベバス", "仮定法 Seandainya..."),
            ("美味しくさえあれば、安くなくても構いません。", "Asalkan enak, tidak apa-apa walau tidak murah.", "アサルカン エナッ ティダッ アパアパ ワラウ ティダッ ムラ", "限定条件 Asalkan..."),
            ("もし困ったことがあれば、いつでも電話してください。", "Jika ada kesulitan, teleponlah kapan saja.", "ジカ アダ クスリタン テレポンラ カパン サジャ", "条件 Jika ada kesulitan..."),
            ("もし宝くじが当たったら、世界一周旅行をしたい。", "Seandainya menang undian, saya mau keliling dunia.", "スアンダイニャ ムナン ウンディアン サヤ マウ クリリン ドゥニア", "仮定法 Seandainya..."),
            ("健康でありさえすれば、幸せに暮らせます。", "Asalkan sehat, kita bisa hidup bahagia.", "アサルカン スハット キタ ビサ ヒドゥップ バハギア", "限定 Asalkan sehat..."),
            ("もし道に迷ったら、地元の人に尋ねなさい。", "Kalau tersesat, bertanyalah kepada warga lokal.", "カロウ トゥルスサット ブルタニャラ クパダ ワルガ ロカル", "条件 Kalau tersesat..."),
            ("もし彼が生きていたら、きっと喜んだろうに。", "Seandainya dia masih hidup, pasti dia sangat bangga.", "スアンダイニャ ディア マシ ヒドゥップ パスティ ディア サンガット バンガ", "反実仮想 Seandainya..."),
            ("安全でさえあれば、どのルートでも構いません。", "Asalkan aman, rute mana pun tidak masalah.", "アサルカン アマン ルテ マナ プン ティダッ マサラ", "限定 Asalkan aman..."),
            ("もし会議が長引いたら、連絡します。", "Jika rapatnya molor, saya akan mengabari Anda.", "ジカ ラパットニャ モロール サヤ アカン ムンガバリ アンダ", "条件 Jika rapat molor..."),
            ("もし過去に戻れるなら、もっと勉強したい。", "Seandainya bisa kembali ke masa lalu, saya mau belajar lebih giat.", "スアンダイニャ ビサ クンバリ ク マサ ラル サヤ マウ ブラジャール ルビ ギアット", "仮定 Seandainya..."),
            ("君が一緒に行ってくれるなら、私も行きます。", "Asalkan kamu ikut, saya juga mau pergi.", "アサルカン カム イクット サヤ ジュガ マウ プルギ", "限定 Asalkan kamu ikut..."),
            ("もし雨が降らなければ、バーベキューをしよう。", "Jika tidak hujan, mari kita pesta barbekyu.", "ジカ ティダッ フジャン マリ キタ ペスタ バルベキュ", "否定条件 Jika tidak..."),
            ("もしパスポートを失くしたら、大使館に行きなさい。", "Kalau kehilangan paspor, pergilah ke kedutaan.", "カロウ クヒランガン パスポル プルギラ ク クドゥタアン", "条件 Kalau kehilangan...")
        ],
        "quiz": [
            ("事実と異なる「もしも〜だったら（仮定法）」を表す接続詞は？", ["seandainya", "jika", "kalau", "asalkan"], 1),
            ("「〜でありさえすれば」という最低限の必要条件を表す接続詞は？", ["asalkan", "meskipun", "sehingga", "karena"], 1),
            ("「もし時間があれば」の標準的な表現は？", ["Jika ada waktu", "Seandainya ada waktu", "Asalkan ada waktu", "Walaupun ada waktu"], 1)
        ]
    },
    {
        "slug": "45-purpose-agar-supaya",
        "title": "【瞬間作文】目的節（agar, supaya, untuk）による論理的表現の瞬間生成",
        "intro": "「〜するために」「〜になるように」という目的節（Purpose）は、理由と並んで日常・ビジネスの会話で頻出します。agar, supaya, untuk, biar（口語）の自然な配置と動詞句の接続を反射化します。",
        "rules": [
            ("agar / supaya ＋ [文]（主語 ＋ 述語）", "主語を明示して「〜が…できるように」と導く。「Agar anak-anak sehat（子供たちが健康であるように）」。"),
            ("untuk ＋ [動詞/名詞]（目的）", "動詞の原形や名詞に直結して「〜するために」。「Untuk belajar（勉強するために）」。"),
            ("口語の biar（〜するように・〜させるために）", "会話で大人気の「biar cepat（早く済むように）」「biar tahu（知っておくように）」。")
        ],
        "drill": [
            ("試験に合格できるように、熱心に勉強しなさい。", "Belajarlah dengan giat agar lulus ujian.", "ブラジャールラ ドゥンガン ギアット アガル ルルス ウジアン", "agar lulus。"),
            ("風邪を引かないように、温かいお茶を飲みなさい。", "Minumlah teh hangat supaya tidak masuk angin.", "ミヌムラ テ ハンガット スパヤ ティダッ マスッ アンギン", "supaya tidak masuk angin。"),
            ("私はインドネシア語を学ぶためにジャカルタへ来ました。", "Saya datang ke Jakarta untuk belajar bahasa Indonesia.", "サヤ ダタン ク ジャカルタ ウントゥッ ブラジャール バハサ インドネシア", "untuk belajar。"),
            ("早く着くように、高速道路を通りましょう（口語）。", "Lewat jalan tol saja biar cepat sampai.", "レワット ジャラン トル サジャ ビアル チパット サンパイ", "口語 biar cepat sampai。"),
            ("彼らが理解できるように、例を挙げてください。", "Tolong berikan contoh agar mereka paham.", "トロン ブリカン チョント アガル ムレカ パハム", "agar mereka paham。"),
            ("健康を保つために、毎日野菜を食べます。", "Saya makan sayur setiap hari untuk menjaga kesehatan.", "サヤ マカン サユール スティアプ ハリ ウントゥッ メンジャガ クセハタン", "untuk menjaga kesehatan。"),
            ("忘れないように、ノートにメモしなさい。", "Catatlah di buku supaya tidak lupa.", "チャタットラ ディ ブク スパヤ ティダッ ルパ", "supaya tidak lupa。"),
            ("見やすいように、明かりをつけましょう。", "Nyalakan lampu biar terang.", "ニャラカン ランプ ビアル トゥラン", "口語 biar terang。"),
            ("平和を守るために、対話を続けなければならない。", "Kita harus melanjutkan dialog untuk menjaga perdamaian.", "キタ ハルス ムランジュットカン ディアログ ウントゥッ メンジャガ プルダマイアン", "untuk menjaga..."),
            ("誤解が生じないように、はっきりと説明してください。", "Jelaskan dengan jelas agar tidak timbul kesalahpahaman.", "ジュラスカン ドゥンガン ジュラス アガル ティダッ ティムブル クサラパハマン", "agar tidak timbul..."),
            ("子供たちが安全に遊べるように、公園を整備する。", "Menata taman agar anak-anak bisa bermain dengan aman.", "メナタ タマン アガル アナッアナッ ビサ ブルマイン ドゥンガン アマン", "agar anak-anak bisa..."),
            ("お金を節約するために、自炊をしています。", "Saya memasak sendiri untuk menghemat uang.", "サヤ メマサッ スンディリ ウントゥッ ムンヘマット ウアン", "untuk menghemat..."),
            ("みんなが聞こえるように、マイクを使ってください。", "Gunakan mikrofon supaya semua orang bisa mendengar.", "グナカン ミクロフォン スパヤ スムア オラン ビサ ムンドンガル", "supaya semua mendengar。"),
            ("後で困らないように、今準備しておこう。", "Siapkan sekarang biar nanti tidak repot.", "シアプカン スカラン ビアル ナンティ ティダッ レポット", "口語 biar tidak repot。"),
            ("生活費を稼ぐために、朝から晩まで働く。", "Bekerja pagi sampai malam untuk mencari nafkah.", "ブケルジャ パギ サンパイ マラム ウントゥッ マンチャリ ナフカ", "untuk mencari nafkah。")
        ],
        "quiz": [
            ("「〜できるように（目的）」を導く標準的接続詞は？", ["agar", "sehingga", "karena", "sebab"], 1),
            ("日常会話で「〜なように（手っ取り早く）」を意味する口語接続詞は？", ["biar", "agar", "untuk", "oleh"], 1),
            ("「忘れないように」を表すフレーズは？", ["supaya tidak lupa", "karena tidak lupa", "sehingga tidak lupa", "walaupun tidak lupa"], 1)
        ]
    },
    {
        "slug": "46-result-sehingga-makanya",
        "title": "【瞬間作文】結果節（sehingga, akibatnya, sampai-sampai）の即時産出",
        "intro": "原因を受けて「その結果〜になった」「あまりに…なので〜するほどだ」と帰結を導く結果節（Result）のドリルです。sehingga（その結果）、akibatnya（結果として・悪影響）、sampai-sampai（〜するほどだ）、makanya（口語：だから〜なのだ）を反射出力します。",
        "rules": [
            ("sehingga（中立的・論理的結果：その結果〜）", "原因節 ＋ sehingga ＋ 結果節。「Dia belajar keras sehingga lulus（勉強したので合格した）」。"),
            ("akibatnya（否定的な帰結・結果として）", "事故や過失による悪影響を導く。「Dia ceroboh, akibatnya dompetnya hilang（不注意だったので結果として財布を失くした）」。"),
            ("sampai-sampai（度合いの極限・〜するほど）", "「あまりに…で、〜するほどだった」。「Sangat lucu sampai-sampai saya menangis（面白すぎて涙が出るほどだった）」。"),
            ("makanya（口語：だから言ったでしょ・だから〜なのだ）", "Makanya jangan terlambat!（だから遅刻するなと言ったのに！）")
        ],
        "drill": [
            ("大雨が降って、その結果洪水が起きました。", "Hujan deras turun sehingga terjadi banjir.", "フジャン ドゥラス トゥルン スヒンガ トゥルジャディ バンジール", "中立結果 sehingga。"),
            ("彼は夜更かしをした、結果として朝寝坊した。", "Dia begadang semalaman, akibatnya bangun kesiangan.", "ディア ブガダン スマラマン アキバットニャ バングン クシアンガン", "悪影響 akibatnya。"),
            ("とても面白くて、お腹が痛くなるほど笑いました。", "Sangat lucu sampai-sampai perut saya sakit.", "サンガット ルチュ サンパイサンパイ プルット サヤ サキッ", "極限 sampai-sampai。"),
            ("だから言ったでしょ、傘を持って行きなさいって！（口語）", "Makanya, bawa payung kan saya sudah bilang!", "マカニャ バワ パユン カン サヤ スダ ビラン", "口語 makanya。"),
            ("道がひどく渋滞して、その結果フライトに乗り遅れた。", "Jalanan macet parah sehingga saya ketinggalan pesawat.", "ジャラナン マチェット パラ スヒンガ サヤ クティンガラン プサワット", "結果 sehingga ketinggalan。"),
            ("彼は注意を怠った、結果として怪我をしてしまった。", "Dia kurang hati-hati, akibatnya mengalami cedera.", "ディア クラン ハティハティ アキバットニャ ムンガラミ チュデラ", "悪果 akibatnya。"),
            ("疲労が極限に達して、立ったまま寝てしまうほどだった。", "Sangat lelah sampai-sampai tertidur sambil berdiri.", "サンガット レラ サンパイサンパイ トゥルティドゥール サンビル ブルディリ", "極限 sampai-sampai。"),
            ("だから早く起きろって言ったんだよ！（口語）", "Makanya, bangun lebih pagi!", "マカニャ バングン ルビ パギ", "口語 makanya。"),
            ("チーム全員が一致団結し、その結果優勝を果たした。", "Seluruh tim kompak sehingga berhasil menjadi juara.", "スルルー ティム コンパッ スヒンガ ブルハシル ムンジャディ ジュアラ", "好結果 sehingga。"),
            ("新商品の需要が急増し、その結果完売した。", "Permintaan melonjak sehingga produk terjual habis.", "プルミンタアン ムロンジャッ スヒンガ プロドゥッ トゥルジュアル ハビス", "結果 sehingga terjual habis。"),
            ("彼は暴飲暴食した、結果として入院することになった。", "Dia makan sembarangan, akibatnya harus dirawat di rumah sakit.", "ディア マカン スンバラガン アキバットニャ ハルス ディラワット ディ ルマ サキッ", "悪果 akibatnya。"),
            ("声が枯れるほど大声で叫んだ。", "Berteriak kencang sampai-sampai suaranya habis.", "ブルトリアッ クンチャン サンパイサンパイ スアラニャ ハビス", "極限 sampai-sampai。"),
            ("勉強しなかったんでしょ、だからテストの点が悪いの！（口語）", "Gak belajar kan, makanya nilainya jelek!", "ガッ ブラジャール カン マカニャ ニライニャ ジュレッ", "口語 makanya。"),
            ("地震の揺れが強くて、壁にひびが入るほどだった。", "Guncangannya kuat sampai-sampai dinding retak.", "グンチャンガンニャ クアット サンパイサンパイ ディンディン レタッ", "極限 sampai-sampai。"),
            ("台風が直撃し、その結果木々が倒れた。", "Badai menerjang sehingga banyak pohon tumbang.", "バダイ ムヌルジャン スヒンガ バニャッ ポホン トゥムバン", "結果 sehingga。")
        ],
        "quiz": [
            ("「その結果〜になった（標準的）」を導く接続詞は？", ["sehingga", "karena", "agar", "meskipun"], 1),
            ("不注意などによる「悪い結果として〜」を表す副詞は？", ["akibatnya", "untungnya", "akhirnya", "rupanya"], 1),
            ("「〜するほど極端だった」を表す結果構文は？", ["sampai-sampai", "kira-kira", "kadang-kadang", "lama-lama"], 1)
        ]
    },
    {
        "slug": "47-modal-adv-mungkin-pasti",
        "title": "【瞬間作文】様態副詞・確信度（mungkin, pasti, tentu, rupanya, agaknya）",
        "intro": "話者の確信の度合い（100%の確信から50%の推測、外見からの判断）を文に付加する様態副詞（Modal Adverbs）のドリルです。pasti / tentu（確実に）、mungkin（たぶん・おそらく）、rupanya / tampaknya（どうやら〜らしい）を瞬時に差し込みます。",
        "rules": [
            ("確信度 100%: pasti / tentu（必ず・絶対に・もちろん）", "Dia pasti datang（彼は絶対に来る）、Tentu saja（もちろんです）。"),
            ("確信度 50%: mungkin / barangkali（たぶん・おそらく）", "Mungkin dia lupa（たぶん彼は忘れたのだろう）。"),
            ("外見・証拠からの推量: rupanya / tampaknya（どうやら〜のようだ）", "Rupanya hujan sudah reda（どうやら雨は止んだようだ）、Tampaknya dia lelah（どうやら彼は疲れているようだ）。")
        ],
        "drill": [
            ("彼は明日必ずパーティーに来ます。", "Dia pasti datang ke pesta besok.", "ディア パスティ ダタン ク ペスタ ベソッ", "確信 pasti。"),
            ("もちろんです、喜んでお手伝いします。", "Tentu saja, dengan senang hati saya bantu.", "トゥントゥ サジャ ドゥンガン スナン ハティ サヤ バントゥ", "確信 tentu saja。"),
            ("たぶん彼は今日遅刻するでしょう。", "Mungkin dia akan terlambat hari ini.", "ムンキン ディア アカン トゥルランバット ハリ イニ", "推測 mungkin。"),
            ("どうやら雨はもう止んだようです。", "Rupanya hujan sudah reda.", "ルパニャ フジャン スダ レダ", "状況推量 rupanya。"),
            ("どうやら彼はその計画に同意していないようだ。", "Tampaknya dia tidak setuju dengan rencana itu.", "タンパッニャ ディア ティダッ スツジュ ドゥンガン レンチャナ イトゥ", "外見推量 tampaknya。"),
            ("私たちの努力は必ず実を結びます。", "Usaha kita pasti akan membuahkan hasil.", "ウスハ キタ パスティ アカン ムンブアカン ハシル", "確信 pasti membuahkan hasil。"),
            ("おそらく彼はまだ寝ているのだろう。", "Barangkali dia masih tidur.", "バランカリ ディア マシ ティドゥール", "控えめな推量 barangkali。"),
            ("彼が犯人に違いない。", "Pasti dia pelakunya.", "パスティ ディア プラクニャ", "強い確信 pasti。"),
            ("どうやら私は道を間違えたようだ。", "Rupanya saya salah jalan.", "ルパニャ サヤ サラ ジャラン", "気づき rupanya。"),
            ("空が暗い、おそらくもうすぐ雨が降るだろう。", "Langit gelap, agaknya sebentar lagi akan hujan.", "ランギット グラップ アガッニャ スブンタール ラギ アカン フジャン", "気配推量 agaknya。"),
            ("健康が最も貴重な財産であることは確かだ。", "Tentu kesehatan adalah harta yang paling berharga.", "トゥントゥ クセハタン アダラ ハルタ ヤン パリン ブルハルガ", "明白 tentu。"),
            ("たぶん後で電話をかけ直します。", "Mungkin saya akan menelepon kembali nanti.", "ムンキン サヤ アカン ムネレポン クンバリ ナンティ", "推測 mungkin。"),
            ("どうやら事態は改善しつつあるようだ。", "Tampaknya situasi mulai membaik.", "タンパッニャ シトゥアシ ムライ ムンバイッ", "推量 tampaknya。"),
            ("約束は必ず守らなければなりません。", "Janji pasti harus ditepati.", "ジャンジ パスティ ハルス ディトゥパティ", "義務の強調 pasti harus。"),
            ("彼はどうやら本当のことを知っているらしい。", "Rupanya dia tahu yang sebenarnya.", "ルパニャ ディア タフ ヤン スブナルニャ", "判明 rupanya。")
        ],
        "quiz": [
            ("「絶対に、必ず（確信度100%）」を表す副詞は？", ["pasti", "mungkin", "barangkali", "agaknya"], 1),
            ("「どうやら〜のようだ（状況から見て）」を表す副詞は？", ["rupanya", "tentunya", "pastinya", "pastilah"], 1),
            ("「たぶん、おそらく（確信度50%）」を表す最も一般的な語は？", ["mungkin", "pasti", "tentu", "mutlak"], 1)
        ]
    },
    {
        "slug": "48-polite-honorific-softener",
        "title": "【瞬間作文】発話を和らげるクッション言葉（barangkali, mohon maaf, kiranya）",
        "intro": "ビジネスや改まった席で、直接的すぎる物言いを避けて相手への敬意と配慮を示す「クッション言葉（Polite Softeners）」のトレーニングです。mohon maaf（申し訳ありませんが）、sekiranya / kiranya（もしよろしければ）、sudilah kiranya（何卒〜）を反射的に添えられるようにします。",
        "rules": [
            ("mohon maaf（恐れ入りますが・申し訳ありませんが）", "言いにくいことや依頼の冒頭に置く。「Mohon maaf, boleh saya bertanya?（恐れ入りますが、質問しても？）」。"),
            ("kiranya / sekiranya（もしよろしければ・どうか）", "相手に負担をかけない丁寧な条件。「Sekiranya Bapak berkenan（もし部長がお気に召しましたら）」。"),
            ("sudilah kiranya（何卒〜してください・最上級の丁寧）", "公式書簡や演説での最上級の懇請。「Sudilah kiranya Bapak membuka acara ini（何卒開会のご挨拶を賜りたく存じます）」。")
        ],
        "drill": [
            ("恐れ入りますが、もう一度お名前を伺えますか？", "Mohon maaf, boleh tahu nama Anda sekali lagi?", "モホン マアフ ボレ タフ ナマ アンダ スカリ ラギ", "クッション Mohon maaf。"),
            ("もしよろしければ、この書類をご確認いただけますか？", "Sekiranya berkenan, tolong periksa dokumen ini.", "スキラニャ ブルクナン トロン プルイクサ ドクメン イニ", "配慮 Sekiranya berkenan。"),
            ("失礼ですが、ここは立ち入り禁止となっております。", "Mohon maaf, area ini dilarang masuk.", "モホン マアフ アレア イニ ディララン マスッ", "丁寧な制止 Mohon maaf。"),
            ("何卒、本式典の開会宣言をお願い申し上げます。", "Sudilah kiranya Bapak meresmikan acara ini.", "スディラ キラニャ バパッ ムレスミカン アチャラ イニ", "最上級敬礼 Sudilah kiranya。"),
            ("ご不便をおかけして大変申し訳ございません。", "Mohon maaf atas ketidaknyamanan ini.", "モホン マアフ アタス クティダッニャマナン イニ", "公式謝罪 Mohon maaf atas..."),
            ("もし可能でしたら、明日お伺いしてもよろしいでしょうか？", "Sekiranya memungkinkan, bolehkah saya berkunjung besok?", "スキラニャ メムンキンカン ボレカ サヤ ブルクンジュン ベソッ", "丁寧な伺い Sekiranya memungkinkan。"),
            ("お忙しいところ恐縮ですが、少々お時間をいただけますか？", "Mohon maaf mengganggu waktunya, ada waktu sebentar?", "モホン マアフ ムンガング ワクトゥニャ アダ ワクトゥ スブンタール", "切り出し Mohon maaf mengganggu..."),
            ("どうかこの願いをお聞き届けください。", "Kiranya permohonan ini dapat dikabulkan.", "キラニャ プルモホナン イニ ダパット ディカブルカン", "懇請 Kiranya..."),
            ("差し支えなければ、理由をお聞かせ願えますか？", "Jika tidak berkeberatan, bolehkah tahu alasannya?", "ジカ ティダッ ブルクブラタン ボレカ タフ アラサンニャ", "配慮 Jika tidak berkeberatan。"),
            ("失礼とは存じますが、ご意見を伺いたく存じます。", "Mohon maaf, kami ingin meminta pandangan Anda.", "モホン マアフ カミ インギン メミンタ パンダンガン アンダ", "意見聴取 Mohon maaf..."),
            ("ご多忙中恐縮ですが、ご出席賜りますようお願い申し上げます。", "Sudilah kiranya Bapak berkenan hadir.", "スディラ キラニャ バパッ ブルクナン ハディール", "公式招待 Sudilah kiranya..."),
            ("ご迷惑をおかけして申し訳ありません。", "Mohon maaf telah merepotkan Anda.", "モホン マアフ トゥラ メレポットカン アンダ", "お詫び Mohon maaf telah merepotkan。"),
            ("もしお手すきでしたら、お茶でもいかがですか？", "Sekiranya senggang, mau minum teh bersama?", "スキラニャ スンガン マウ ミヌム テ ブルサマ", "軽い誘い Sekiranya senggang。"),
            ("恐れ入りますが、お席をお詰めいただけますか？", "Mohon maaf, bisakah bergeser sedikit?", "モホン マアフ ビサカ ブルゲセル スディキッ", "丁寧な依頼 Mohon maaf, bisakah..."),
            ("どうかご理解とご協力を賜りますようお願い申し上げます。", "Kiranya dapat dimaklumi dan dibantu.", "キラニャ ダパット ディマクルミ ダン ディバントゥ", "結び Kiranya dapat dimaklumi。")
        ],
        "quiz": [
            ("言いにくいことを切り出す際の最も定番のクッション言葉は？", ["Mohon maaf", "Terima kasih", "Sama-sama", "Selamat"], 1),
            ("目上の人に対して「もしよろしければ」と配慮するフレーズは？", ["Sekiranya berkenan", "Asalkan mau", "Pasti bisa", "Harus mau"], 1),
            ("公的書簡で「何卒〜してください」と最上級の丁寧を添える語句は？", ["Sudilah kiranya", "Tolong cepat", "Silakan langsung", "Harap segera"], 1)
        ]
    },
    {
        "slug": "49-idiomatic-fixed-chunks",
        "title": "【瞬間作文】定型チャンク（pada dasarnya, setahu saya, tidak heran jika）の反射発話",
        "intro": "単語を1つずつ組み立てるのではなく、頭にストックした完成された定型表現（Formulaic Chunks）をそのままブロックとして繰り出すことで、発話の流暢性（Fluency）とネイティブらしさが爆発的に高まります。「pada dasarnya（基本的には）」「setahu saya（私の知る限り）」を瞬時に引き出します。",
        "rules": [
            ("視点・前提のチャンク", "pada dasarnya（基本的には・原理的には）、pada kenyataannya（実際には）、setahu saya（私の知る限りでは）、menurut saya（私の考えでは）。"),
            ("評語・接続のチャンク", "tidak heran jika（〜なのも不思議ではない・当然だ）、seperti yang kita ketahui（ご存知の通り）、dengan kata lain（言い換えれば）、mau tidak mau（嫌でも・否応なく）。")
        ],
        "drill": [
            ("基本的には、私はあなたの提案に同意します。", "Pada dasarnya, saya setuju dengan usulan Anda.", "パダ ダサルニャ サヤ スツジュ ドゥンガン ウスラン アンダ", "チャンク Pada dasarnya。"),
            ("私の知る限りでは、彼はまだ独身です。", "Setahu saya, dia masih lajang.", "スタフ サヤ ディア マシ ラジャン", "チャンク Setahu saya。"),
            ("彼が疲れているのも不思議ではありません（当然だ）。", "Tidak heran jika dia merasa lelah.", "ティダッ ヘラン ジカ ディア ムラサ レラ", "チャンク Tidak heran jika..."),
            ("実際には、その問題はそれほど単純ではありません。", "Pada kenyataannya, masalah itu tidak sesederhana itu.", "パダ クニャタアンニャ マサラ イトゥ ティダッ ススデルハナ イトゥ", "チャンク Pada kenyataannya。"),
            ("ご存知の通り、インドネシアは豊かな国です。", "Seperti yang kita ketahui, Indonesia negara yang kaya.", "スペルティ ヤン キタ クタフイ インドネシア ネガラ ヤン カヤ", "チャンク Seperti yang kita ketahui。"),
            ("言い換えれば、私たちはやり直さなければならない。", "Dengan kata lain, kita harus mengulang dari awal.", "ドゥンガン カタ ライン キタ ハルス ムングラン ダリ アワル", "チャンク Dengan kata lain。"),
            ("嫌でも、私たちは現実を受け入れなければならない。", "Mau tidak mau, kita harus menerima kenyataan.", "マウ ティダッ マウ キタ ハルス メネリマ クニャタアン", "チャンク Mau tidak mau。"),
            ("率直に言って、この計画は危険すぎます。", "Terus terang, rencana ini terlalu berisiko.", "トゥルス トゥラン レンチャナ イニ トゥルラル ブルリシコ", "チャンク Terus terang。"),
            ("短く言えば、結論はまだ出ていません。", "Singkat kata, belum ada kesimpulan.", "シンカット カタ ブロン アダ クシムプラン", "チャンク Singkat kata。"),
            ("いずれにせよ、私たちは全力を尽くしました。", "Bagaimanapun juga, kita sudah berusaha maksimal.", "バガイマナプン ジュガ キタ スダ ブルウサハ マクシマル", "チャンク Bagaimanapun juga。"),
            ("私の意見では、品質が最も大切です。", "Menurut hemat saya, kualitas adalah yang terpenting.", "ムヌルット ヘマット サヤ クアリタス アダラ ヤン トゥルポンティン", "格式チャンク Menurut hemat saya。"),
            ("言うまでもなく、健康はかけがえのない宝です。", "Tak perlu dikatakan lagi, kesehatan adalah harta berharga.", "タッ プルル ディカタカン ラギ クセハタン アダラ ハルタ ブルハルガ", "チャンク Tak perlu dikatakan lagi。"),
            ("彼が成功したのも無理はない、努力家だからだ。", "Pantas saja dia sukses, dia orang yang rajin.", "パンタス サジャ ディア スクセス ディア オラン ヤン ラジン", "チャンク Pantas saja。"),
            ("これに関連して、いくつか確認事項があります。", "Sehubungan dengan hal ini, ada beberapa hal yang perlu dicek.", "スフブンガン ドゥンガン ハル イニ アダ ブブラパ ハル ヤン プルル ディチェッ", "チャンク Sehubungan dengan hal ini。"),
            ("要するに、私たちは協力しなければならない。", "Intinya, kita harus bekerja sama.", "インティニャ キタ ハルス ブケルジャ サマ", "チャンク Intinya。")
        ],
        "quiz": [
            ("「基本的には、原理的には」を表す定番チャンクは？", ["Pada dasarnya", "Pada akhirnya", "Pada mulanya", "Pada waktunya"], 1),
            ("「私の知る限りでは」を表す定番チャンクは？", ["Setahu saya", "Sebisa saya", "Semau saya", "Secara saya"], 1),
            ("「〜なのも不思議ではない（当然だ）」を表すチャンクは？", ["Tidak heran jika", "Tidak mau jika", "Tidak boleh jika", "Tidak ada jika"], 1)
        ]
    },
    {
        "slug": "50-comprehensive-rapid-drill",
        "title": "【総合口頭作文】実戦スピード作文テスト：全文法パターン50本連続ノック",
        "intro": "セクション25の集大成として、基本語順から接辞、語幹受動態、複文、クッション言葉、定型チャンクに至るまで、全50の重要構文を網羅した実戦総合ノックです。1問につき1〜2秒以内の即時産出で、頭の中に構築されたインドネシア語の自動化回路を総テストします。",
        "rules": [
            ("テストのルール", "日本語の刺激を見て、**1〜2秒以内**に声に出してインドネシア語を発話してください。ためらわずに口から音を出す反射神経を測定します。"),
            ("合格基準", "全50問中、40問以上が即座に正しく発話できれば「SLA自動化レベル達成（B1/B2実戦運用可能）」と認定されます。")
        ],
        "drill": [
            ("1. 私は熱いコーヒーを飲みます。", "Saya minum kopi panas.", "サヤ ミヌム コピ パナス", "SVO＋後置修飾。"),
            ("2. 彼は学生ではありません、先生です。", "Dia bukan mahasiswa, melainkan guru.", "ディア ブカン マハシスワ ムラインカン グル", "bukan ... melainkan。"),
            ("3. （若い男性店員に）お兄さん、これいくら？", "Mas, berapa harganya ini?", "マス ブラパ ハルガニャ イニ", "親称 Mas。"),
            ("4. あの建物は大きな病院です。", "Gedung itu rumah sakit besar.", "グドゥン イトゥ ルマ サキッ ブサール", "指示詞 itu ＋ 後置修飾。"),
            ("5. 駅へはどうやって行きますか？", "Bagaimana cara pergi ke stasiun?", "バガイマナ チャラ プルギ ク スタシウン", "疑問詞 bagaimana cara。"),
            ("6. 私はもう昼食を食べました。", "Saya sudah makan siang.", "サヤ スダ マカン シアン", "アスペクト sudah。"),
            ("7. 彼はスラバヤからジャカルタへ行きました。", "Dia pergi dari Surabaya ke Jakarta.", "ディア プルギ ダリ スラバヤ ク ジャカルタ", "前置詞 dari ... ke。"),
            ("8. 私にとって健康が一番大切です。", "Bagi saya, kesehatan paling penting.", "バギ サヤ クセハタン パリン ポンティン", "抽象前置詞 Bagi saya。"),
            ("9. ここで写真を撮ってもいいですか？", "Boleh saya mengambil foto di sini?", "ボレ サヤ ムンガンビル フォト ディ シニ", "助動詞許可 Boleh saya..."),
            ("10. このホテルはあのホテルより新しい。", "Hotel ini lebih baru daripada hotel itu.", "ホテル イニ ルビ バル ダリパダ ホテル イトゥ", "比較級 lebih ... daripada。"),
            ("11. 父と母は市場へ出かけました。", "Ayah dan ibu pergi ke pasar.", "アヤ ダン イブ プルギ ク パサール", "等位接続 dan。"),
            ("12. 雨が降っているので、家にいます。", "Karena hujan, saya tinggal di rumah.", "カルナ フジャン サヤ ティンガル ディ ルマ", "従属接続 Karena。"),
            ("13. 庭に3匹の猫がいます。", "Ada tiga ekor kucing di halaman.", "アダ ティガ エコル クチン ディ ハラマン", "助数詞 ekor。"),
            ("14. 何か問題はありますか？", "Ada masalah?", "アダ マサラ", "存在 ada。"),
            ("15. どうぞここにお座りください。", "Silakan duduk di sini.", "シラカン ドゥドゥッ ディ シニ", "丁寧勧奨 Silakan。"),
            ("16. その本は有名な作家によって書かれた。", "Buku itu ditulis oleh penulis terkenal.", "ブク イトゥ ディトゥリス オレ プヌリス トゥルクナル", "di- 受動態。"),
            ("17. その手紙は私がもう書きました。", "Surat itu sudah saya tulis.", "スラット イトゥ スダ サヤ トゥリス", "一人称語幹受動態。"),
            ("18. この課題は君が終えなきゃダメだよ。", "Tugas ini harus kamu selesaikan.", "トゥガス イニ ハルス カム スルサイカン", "二人称語幹受動態。"),
            ("19. 母は新しい服を買いました。", "Ibu membeli baju baru.", "イブ ムンブリ バジュ バル", "meN- 他動詞（beli→membeli）。"),
            ("20. 飛行機が無事に着陸しました。", "Pesawat mendarat dengan selamat.", "プサワット ムンダラット ドゥンガン スラマット", "meN- 自動詞（mendarat）。"),
            ("21. 私たちは毎朝公園を散歩します。", "Kami berjalan-jalan di taman setiap pagi.", "カミ ブルジャランジャラン ディ タマン スティアプ パギ", "ber- 自動詞。"),
            ("22. 状況は日増しに変化しています。", "Situasi berubah dari hari ke hari.", "シトゥアシ ブルウバ ダリ ハリ ク ハリ", "ber- vs meN-（berubah）。"),
            ("23. テレビを見ながら寝落ちしてしまった。", "Saya tertidur saat menonton televisi.", "サヤ トゥルティドゥール サアット ムノントン テレフィシ", "ter- 偶発・寝落ち。"),
            ("24. このホテルの料金はとても手頃です。", "Tarif hotel ini sangat terjangkau.", "タリフ ホテル イニ サンガット トゥルジャンカウ", "ter- 可能。"),
            ("25. 彼が世界で一番足が速い選手です。", "Dia atlet tercepat di dunia.", "ディア アトレット トゥルチパット ディ ドゥニア", "ter- 最上級。"),
            ("26. 妹は自分の部屋を掃除しています。", "Adik sedang membersihkan kamarnya.", "アディッ スダン ムンブルシカン カマールニャ", "-kan 使役。"),
            ("27. 父は私に新しい自転車を買ってくれた。", "Ayah membelikan saya sepeda baru.", "アヤ ムンブリカン サヤ スペダ バル", "-kan 受益。"),
            ("28. 彼は海に石を投げ入れました。", "Dia melemparkan batu ke laut.", "ディア ムルンパルカン バトゥ ク ラウット", "-kan 対象移動。"),
            ("29. 警察はすぐに事故現場に急行した。", "Polisi mendatangi lokasi kecelakaan.", "ポリシ ムンダタンギ ロカシ クチュラカアン", "-i 場所作用。"),
            ("30. 彼は怒って机を何度も叩き続けた。", "Dia memukuli meja karena marah.", "ディア メムクリ メジャ カルナ マラ", "-i 反復動作。"),
            ("31. 彼は犬に石を投げつけました。", "Dia melempari anjing itu dengan batu.", "ディア ムルンパリ アンジン イトゥ ドゥンガン バトゥ", "-kan vs -i。"),
            ("32. 健康は何よりも貴重な財産です。", "Kesehatan adalah harta paling berharga.", "クセハタン アダラ ハルタ パリン ブルハルガ", "ke-...-an 名詞化。"),
            ("33. 私は帰り道に雨に降られてしまった。", "Saya kehujanan dalam perjalanan pulang.", "サヤ クフジャナン ダラム プルジャラナン プラン", "ke-...-an 被災受動。"),
            ("34. このお茶は甘すぎますね。", "Teh ini kemanisan ya.", "テ イニ クマニサン ヤ", "ke-...-an 過度。"),
            ("35. 新しい工場の建設が始まりました。", "Pembangunan pabrik baru telah dimulai.", "プムバングナン パブリッ バル トゥラ ディムライ", "peN-...-an 過程。"),
            ("36. 二つの国は平和条約を結んだ。", "Kedua negara menyepakati perjanjian damai.", "クドゥア ネガラ ムニェパカティ プルジャンジアン ダマイ", "per-...-an 契約。"),
            ("37. 交通規則を厳格に守りなさい。", "Patuhi peraturan lalu lintas dengan ketat.", "パトゥヒ プラトゥラン ラル リンタス ドゥンガン クタット", "peraturan（規則そのもの）。"),
            ("38. 市場には様々な果物が売られている。", "Berbagai buah-buahan dijual di pasar.", "ブルバガイ ブアブアハン ディジュアル ディ パサール", "重複語 多様性。"),
            ("39. 困った時はお互いに助け合いましょう。", "Mari tolong-menolong di saat sulit.", "マリ トロンムノロン ディ サアット スリット", "重複語 相互行為。"),
            ("40. 彼は死に物狂いで必死に走った。", "Dia berlari mati-matian.", "ディア ブルラリ マティマティアン", "重複語 極限強調。"),
            ("41. 昨日ここに来た人は私の叔父です。", "Orang yang datang kemarin adalah paman saya.", "オラン ヤン ダタン クマリン アダラ パマン サヤ", "関係詞 yang。"),
            ("42. 彼は明日来られないと私に伝えた。", "Dia memberi tahu bahwa dia tidak bisa datang.", "ディア ムンブリ タフ バフワ ディア ティダッ ビサ ダタン", "名詞節 bahwa。"),
            ("43. 疲れていたけれど、仕事をやり遂げた。", "Meskipun lelah, dia menyelesaikan tugasnya.", "ムスキプン レラ ディア ムンユルサイカン トゥガスニャ", "譲歩 meskipun。"),
            ("44. もし明日晴れたら、ピクニックに行こう。", "Jika besok cerah, mari kita piknik.", "ジカ ベソッ チラ マリ キタ ピクニック", "条件 jika。"),
            ("45. 風邪を引かないように、薬を飲みなさい。", "Minum obat supaya tidak masuk angin.", "ミヌム オバット スパヤ ティダッ マスッ アンギン", "目的 supaya。"),
            ("46. 大雨が降って、その結果洪水が起きた。", "Hujan lebat sehingga terjadi banjir.", "フジャン ルバット スヒンガ トゥルジャディ バンジール", "結果 sehingga。"),
            ("47. 彼は明日必ず約束の場所に来るはずだ。", "Dia pasti datang ke tempat pertemuan besok.", "ディア パスティ ダタン ク トゥムパット プルトゥムアン ベソッ", "確信 pasti。"),
            ("48. 恐れ入りますが、もう一度言ってくださいますか？", "Mohon maaf, bisakah diulangi sekali lagi?", "モホン マアフ ビサカ ディウランギ スカリ ラギ", "クッション Mohon maaf。"),
            ("49. 基本的には、私はその提案に賛成です。", "Pada dasarnya, saya setuju dengan usulan itu.", "パダ ダサルニャ サヤ スツジュ ドゥンガン ウスラン イトゥ", "チャンク Pada dasarnya。"),
            ("50. 言い換えれば、私たちはやり直さなければならない。", "Dengan kata lain, kita harus mengulanginya.", "ドゥンガン カタ ライン キタ ハルス ムングランギニャ", "チャンク Dengan kata lain。")
        ],
        "quiz": [
            ("瞬間作文で最も重要な学習態度は？", ["文法を紙に書いてからゆっくり話す", "1〜2秒以内に即座に口頭で発声して自動化する", "辞書を引いて珍しい単語を探す", "黙読だけで満足する"], 2),
            ("語幹受動態「その本は私が読んだ」の正解は？", ["Buku itu sudah saya baca.", "Buku itu dibaca oleh saya.", "Saya sudah membaca buku itu.", "Buku itu membaca saya."], 1),
            ("「〜なのも不思議ではない（当然だ）」の定型チャンクは？", ["Tidak heran jika", "Pada dasarnya", "Dengan kata lain", "Setahu saya"], 1)
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
    
    drill_len = len(a['drill'])
    lines.append(f"## 2. 瞬間口頭作文トレーニング（{drill_len}本ノック）\n")
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

print("Batch 1041-1050 generated successfully.")
