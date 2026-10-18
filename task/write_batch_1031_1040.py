"""Writer Script: Articles 1031 - 1040 for docs/output/
"""

articles_data = [
    {
        "slug": "31-suffix-kan-vs-i-contrast",
        "title": "【瞬間作文】接尾辞 -kan と -i の対比瞬間産出（menugaskan vs menugasi）",
        "intro": "接尾辞「-kan」と「-i」は、同一の語根から異なる構文構造を生み出すインドネシア語の最難関ポイントです。目的語が「移動するもの（-kan）」なのか、「作用を受ける対象・場所（-i）」なのかを0.5秒で見極め、正しく使い分けるドリルです。",
        "rules": [
            ("対象移動の -kan vs 場所・対象の -i", "melemparkan batu ke anjing（犬に石を投げる：batuが移動） vs melempari anjing dengan batu（犬に石を投げつける：anjingが対象）。"),
            ("使役の -kan vs 場所付与の -i", "menugaskan pekerjaan kepada staf（仕事をスタッフに割り振る） vs menugasi staf dengan pekerjaan（スタッフに仕事を割り振る）。"),
            ("感情の -kan（使役） vs 感情の -i（直接対象）", "menakutkan（怖がらせる・恐ろしい） vs menakuti（脅す・怖がらせる対象に迫る）。")
        ],
        "drill": [
            ("彼は犬に石を投げました（石が移動）。", "Dia melemparkan batu ke arah anjing.", "ディア ムルンパルカン バトゥ ク アラ アンジン", "-kan（石を投げる）。"),
            ("彼は犬に石を投げつけました（犬が標的）。", "Dia melempari anjing itu dengan batu.", "ディア ムルンパリ アンジン イトゥ ドゥンガン バトゥ", "-i（犬に投げつける）。"),
            ("社長は新しい任務を彼に課しました。", "Direktur menugaskan tugas baru kepadanya.", "ディレクトゥール ムヌガスカン トゥガス バル クパダニャ", "-kan [任務] kepada [人]。"),
            ("社長は彼に新しい任務を与えました。", "Direktur menugasi dia dengan tugas baru.", "ディレクトゥール ムヌガシ ディア ドゥンガン トゥガス バル", "-i [人] dengan [任務]。"),
            ("母は庭に水をまきました（水が移動）。", "Ibu menyiramkan air ke halaman.", "イブ ムニィラムカン アイル ク ハラマン", "-kan [水] ke [場所]。"),
            ("母は庭の花に水をやりました（花が対象）。", "Ibu menyirami bunga-bunga di taman.", "イブ ムニィラミ ブンガブンガ ディ タマン", "-i [花] 直接目的語。"),
            ("彼は壁にペンキを塗りました（ペンキが移動）。", "Dia mengecatkan cat ke dinding.", "ディア ムンゲチャットカン チャット ク ディンディン", "-kan。"),
            ("彼は部屋の壁一面を塗りました（壁が対象）。", "Dia mengecati dinding kamar.", "ディア ムンゲチャティ ディンディン カマール", "-i。"),
            ("彼は友達にプレゼントを贈りました。", "Dia menghadiahkan jam tangan kepada temannya.", "ディア ムンハディアカン ジャム タンガン クパダ トゥマンニャ", "-kan [物] kepada [人]。"),
            ("彼は友達に腕時計をプレゼントしました。", "Dia menghadiahi temannya jam tangan.", "ディア ムンハディアヒ トゥマンニャ ジャム タンガン", "-i [人] [物]。"),
            ("花嫁に指輪をはめてあげてください。", "Tolong pasangkan cincin ke jari pengantin.", "トロン パサンカン チンチン ク ジャリ プンガンティン", "-kan [指輪]。"),
            ("壁に美しい絵を飾り付けなさい。", "Pasangi dinding itu dengan lukisan indah.", "パサンギ ディンディン イトゥ ドゥンガン ルキサン インダ", "-i [壁]。"),
            ("彼は机の上の書類を片付けた（書類を動かした）。", "Dia memindahkan dokumen dari meja.", "ディア メミンダカン ドクメン ダリ メジャ", "-kan。"),
            ("彼は部屋を家具で満たした。", "Dia memenuhit kamar dengan perabotan.", "ディア メムヌヒ カマール ドゥンガン プラボタン", "-i [部屋]。"),
            ("その知らせは彼を安心させた。", "Kabar itu menenangkan hatinya.", "カバール イトゥ ムヌナンカン ハティニャ", "-kan（心を落ち着かせる）。")
        ],
        "quiz": [
            ("「石を投げる（石が移動する）」文は？", ["Dia melemparkan batu.", "Dia melempari batu.", "Dia berlempar batu.", "Dia terlempar batu."], 1),
            ("「犬に石を投げつける（犬が直接目的語）」文は？", ["Dia melempari anjing dengan batu.", "Dia melemparkan anjing dengan batu.", "Dia terlempar anjing.", "Dia berlempar anjing."], 1),
            ("「友達にプレゼントをあげる（友達が直接目的語）」は？", ["menghadiahi teman", "menghadiahkan teman", "berhadiah teman", "terhadiah teman"], 1)
        ]
    },
    {
        "slug": "32-circumfix-ke-an-noun",
        "title": "【瞬間作文】周囲辞 ke-...-an の名詞化の瞬間生成（kesehatan, kebebasan）",
        "intro": "周囲辞「ke-...-an」は、形容詞や動詞を抽象名詞（〜性、〜であること、状態）に転換する最も重要な造語法です。sehat（健康な）→ kesehatan（健康）、bebas（自由な）→ kebebasan（自由）など、抽象概念を瞬時に名詞化して主語や目的語に据えるドリルです。",
        "rules": [
            ("形容詞 ＋ ke-...-an（抽象的性質・状態）", "sehat → kesehatan（健康）、bersih → kebersihan（清潔）、indah → keindahan（美しさ）、adil → keadilan（正義・公平）、nyata → kenyataan（現実）。"),
            ("動詞・名詞 ＋ ke-...-an（領域・概念）", "hidup → kehidupan（生活・生命）、anggota → keanggotaan（会員資格）、pulau → kepulauan（諸島・列島）。")
        ],
        "drill": [
            ("健康は何よりも大切です。", "Kesehatan lebih penting daripada apa pun.", "クセハタン ルビ ポンティン ダリパダ アパ プン", "kesehatan（sehat=健康）。"),
            ("自由はすべての人の権利です。", "Kebebasan adalah hak setiap orang.", "クベバサン アダラ ハッ スティアプ オラン", "kebebasan（bebas=自由）。"),
            ("私たちはバリ島の海の美しさを称賛しました。", "Kami mengagumi keindahan laut Bali.", "カミ ムンガグミ クインダハン ラウット バリ", "keindahan（indah=美しい）。"),
            ("裁判所は正義を守らなければなりません。", "Pengadilan harus menegakkan keadilan.", "プンガディラン ハルス ムヌガッカン クアディラン", "keadilan（adil=公正な）。"),
            ("清潔さは健康の一部です。", "Kebersihan adalah sebagian dari kesehatan.", "クブルシハン アダラ スバギアン ダリ クセハタン", "kebersihan（bersih=清潔な）。"),
            ("これが私たちが直面している厳しい現実です。", "Inilah kenyataan pahit yang kita hadapi.", "イニラ クニャタアン パヒット ヤン キタ ハダピ", "kenyataan（nyata=明白な）。"),
            ("村の人々の温かさに感動しました。", "Saya terharu oleh kehangatan warga desa.", "サヤ トゥルハル オレ クハンガタン ワルガ デサ", "kehangatan（hangat=温かい）。"),
            ("困難を恐れてはならない。", "Jangan takut akan kesulitan.", "ジャンガン タクット アカン クスリタン", "kesulitan（sulit=困難な）。"),
            ("成功は努力によってもたらされる。", "Keberhasilan diraih melalui kerja keras.", "クブルハシラン ディライ ムラルイ クルジャ クラス", "keberhasilan（berhasil=成功する）。"),
            ("インドネシアの文化的多様性。", "Keanekaragaman budaya Indonesia.", "クアネカラガマン ブダヤ インドネシア", "keanekaragaman（多様性）。"),
            ("村の治安と安全を守る。", "Menjaga keamanan dan ketertiban desa.", "メンジャガ クアマナン ダン クトゥルティバン デサ", "keamanan（aman=安全な）。"),
            ("都市部での人々の生活。", "Kehidupan masyarakat di perkotaan.", "クヒドゥパン マシャラカット ディ プルコタアン", "kehidupan（hidup=生きる）。"),
            ("彼の成功の秘密は誠実さです。", "Rahasia suksesnya adalah kejujuran.", "ラハシア スクセスニャ アダラ クジュジュラン", "kejujuran（jujur=正直な）。"),
            ("情報の真実性を確認する。", "Memastikan kebenaran informasi.", "メマスチカン クブナラン インフォルマシ", "kebenaran（benar=正しい）。"),
            ("互いの違いを尊重しなさい。", "Hormatilah perbedaan satu sama lain.", "ホルマティラ クプルベダアン サトゥ サマ ライン", "perbedaan（beda=異なる）。")
        ],
        "quiz": [
            ("形容詞 sehat（健康な）を抽象名詞「健康」にする正しい形は？", ["kesehatan", "pensehatan", "persehatan", "tersehat"], 1),
            ("形容詞 adil（公平な）から作られる名詞「正義・公平」は？", ["keadilan", "pengadilan", "peradilan", "seadil"], 1),
            ("「美しさ」を表す ke-...-an 名詞は？", ["keindahan", "pengindahan", "perindahan", "terindah"], 1)
        ]
    },
    {
        "slug": "33-circumfix-ke-an-adversative",
        "title": "【瞬間作文】周囲辞 ke-...-an の被災・不本意受動（kehujanan, ketinggalan）",
        "intro": "周囲辞「ke-...-an」の2つ目の顔は、意志に反して不本意な災難に遭う「被災受動（〜に遭う、〜されて困る）」です。雨に降られる（kehujanan）、電車に乗り遅れる（ketinggalan kereta）、熱が出る（kemasukan）など、日常の不運を瞬時に発話します。",
        "rules": [
            ("被災・不本意の ke-...-an", "kehujanan（雨に降られる）、kepanasan（暑さにやられる）、kedinginan（寒さに凍える）、ketinggalan（乗り遅れる・置き忘れられる）、kecopetan（スリに遭う）、kemalingan（泥棒に入られる）。"),
            ("主語は「被災者（被害を受けた人）」", "Saya kehujanan（私は雨に降られた）。受身の di- と違い、「自然現象や偶発的な不運」に特化します。")
        ],
        "drill": [
            ("私は帰り道に雨に降られてしまいました。", "Saya kehujanan dalam perjalanan pulang.", "サヤ クフジャナン ダラム プルジャラナン プラン", "被災 kehujanan（hujan=雨）。"),
            ("彼は朝の電車に乗り遅れました。", "Dia ketinggalan kereta pagi.", "ディア クティンガラン クレタ パギ", "不本意 ketinggalan。"),
            ("私の友達は市場でスリに遭いました。", "Teman saya kecopetan di pasar.", "トゥマン サヤ クチョペタン ディ パサール", "被害 kecopetan（copet=スリ）。"),
            ("昨夜、隣の家が泥棒に入られました。", "Tadi malam rumah tetangga kemalingan.", "タディ マラム ルマ トゥタンガ クマリンガン", "被害 kemalingan（maling=泥棒）。"),
            ("子供たちは水泳の後に寒さで震えていました。", "Anak-anak kedinginan setelah berenang.", "アナッアナッ クディンギナン ストゥラ ブルナン", "被災 kedinginan（dingin=寒い）。"),
            ("太陽の下で長時間待たされて暑さにやられた。", "Saya kepanasan karena menunggu lama di bawah matahari.", "サヤ クパナサン カルナ ムヌング ラマ ディ バワ マタハリ", "被災 kepanasan（panas=暑い）。"),
            ("財布をレストランに置き忘れてきてしまった。", "Dompet saya ketinggalan di restoran.", "ドムペット サヤ クティンガラン ディ レストラン", "不本意放置 ketinggalan。"),
            ("私たちは昨夜、停電に見舞われました。", "Kami kegelapan karena mati lampu tadi malam.", "カミ クゲラパン カルナ マティ ランプ タディ マラム", "暗闇に見舞われる kegelapan。"),
            ("彼は夜更かしをして朝寝坊してしまった。", "Dia kesiangan karena begadang semalaman.", "ディア クシアンガン カルナ ブガダン スマラマン", "朝寝坊 kesiangan（siang=昼）。"),
            ("道に迷って途方に暮れてしまいました。", "Saya kesasar di jalan raya.", "サヤ クササール ディ ジャラン ラヤ", "迷子 kesasar / tersesat。"),
            ("会議に遅刻してしまいました（時間が遅くなった）。", "Saya ketelatan datang ke rapat.", "サヤ クトゥラタン ダタン ク ラパット", "遅刻 ketelatan。"),
            ("目の中にゴミが入ってしまいました。", "Mata saya kemasukan debu.", "マタ サヤ クマスッカン ドゥブ", "異物混入 kemasukan。"),
            ("服がスープで汚れてしまった。", "Baju saya kekotoran kuah sup.", "バジュ サヤ クコトラン クア スプ", "汚れ被害 kekotoran。"),
            ("彼らは山で夜になり、暗闇に閉じ込められた。", "Mereka kemalaman di atas gunung.", "ムレカ クマラマン ディ アタス グヌン", "日没に遭う kemalaman。"),
            ("秘密が彼にバレて知られてしまった。", "Rahasia saya ketahuan oleh dia.", "ラハシア サヤ クタフアン オレ ディア", "露見 ketahuan。")
        ],
        "quiz": [
            ("「雨に降られてずぶ濡れになった」を表す動詞は？", ["kehujanan", "menghujani", "dihujankan", "berhujan"], 1),
            ("「電車に乗り遅れる」を表すフレーズは？", ["ketinggalan kereta", "meninggalkan kereta", "ditinggalkan kereta", "bertinggal kereta"], 1),
            ("「市場でスリの被害に遭った」を表す動詞は？", ["kecopetan", "mencopet", "dicopetkan", "bercopet"], 1)
        ]
    },
    {
        "slug": "34-circumfix-ke-an-excessive",
        "title": "【瞬間作文】周囲辞 ke-...-an の過度形容詞用法（kemanisan, kebesaran）",
        "intro": "周囲辞「ke-...-an」の3つ目の機能は、形容詞を挟んで「あまりにも〜すぎる（過度・超過）」を表す用法です。terlalu manis（甘すぎる）を1語で「kemanisan」、terlalu besar（大きすぎる）を「kebesaran」とスマートに表現する口頭反射を鍛えます。",
        "rules": [
            ("形容詞 ＋ ke-...-an ＝ 過度（〜すぎる）", "kemanisan（甘すぎる：manis）、keasinan（塩辛すぎる：asin）、kebesaran（大きすぎる：besar）、kekecilan（小さすぎる：kecil）、kemahalan（高すぎる：mahal）。"),
            ("日常会話での頻度", "レストランでの味の感想や、試着室でのサイズ確認でネイティブが最も好んで使う言い回しです。")
        ],
        "drill": [
            ("このお茶は甘すぎます。", "Teh ini kemanisan.", "テ イニ クマニサン", "過度 kemanisan（manis=甘い）。"),
            ("このスープは塩辛すぎます。", "Sup ini keasinan.", "スプ イニ クアシナン", "過度 keasinan（asin=塩辛い）。"),
            ("この靴は私の足には大きすぎます。", "Sepatu ini kebesaran untuk kaki saya.", "スパトゥ イニ クブサラン ウントゥッ カキ サヤ", "サイズ超過 kebesaran。"),
            ("このシャツは私には小さすぎます。", "Kemeja ini kekecilan untuk saya.", "クメジャ イニ ククチラン ウントゥッ サヤ", "サイズ不足 kekecilan。"),
            ("その服はちょっと高すぎますね。", "Baju itu agak kemahalan ya.", "バジュ イトゥ アガッ クマハラン ヤ", "価格超過 kemahalan。"),
            ("このズボンは長すぎます、裾上げが必要です。", "Celana ini kepanjangan, perlu dipotong.", "チュラナ イニ クパンジャンガン プルル ディポトン", "丈過度 kepanjangan。"),
            ("このスカートは短すぎます。", "Rok ini kependekan.", "ロ环境 イニ クプンデカン", "丈不足 kependekan。"),
            ("エアコンが効きすぎて寒すぎます。", "AC-nya kedinginan.", "アーセーニャ クディンギナン", "温度過度 kedinginan。"),
            ("このサンバルは私には辛すぎます。", "Sambal ini kepedasan untuk saya.", "サンバル イニ クプダサン ウントゥッ サヤ", "辛味超過 kepedasan。"),
            ("部屋が暗すぎて本が読めません。", "Ruangannya kegelapan untuk membaca.", "ルアンガンニャ クゲラパン ウントゥッ ムンバチャ", "暗すぎ kegelapan。"),
            ("コーヒーが苦すぎます。", "Kopinya kepahitan.", "コピニャ クパヒタン", "苦味超過 kepahitan。"),
            ("荷物が重すぎて持ち上げられません。", "Barangnya keberatan untuk diangkat.", "バランニャ クブラタン ウントゥッ ディアンカット", "重量過度 keberatan。"),
            ("時間が早すぎます、もう少し後で行きましょう。", "Waktunya kepagian, mari pergi nanti.", "ワクトゥニャ クパギアン マリ プルギ ナンティ", "早すぎ kepagian。"),
            ("道が狭すぎて車が通れません。", "Jalannya kesempitan untuk mobil.", "ジャランニャ クスンピタン ウントゥッ モビル", "幅過小 kesempitan。"),
            ("スープが熱すぎて舌を火傷しそう。", "Supnya kepanasan, hati-hati.", "スプニャ クパナサン ハティハティ", "熱すぎ kepanasan。")
        ],
        "quiz": [
            ("料理を味見して「甘すぎる」と言う時の1単語は？", ["kemanisan", "memaniskan", "kemanisan-an", "termanis"], 1),
            ("試着して「サイズが大きすぎる」と言う時の表現は？", ["kebesaran", "membesarkan", "terbesar", "sebesar"], 1),
            ("スープが「塩辛すぎる」と言う時の単語は？", ["keasinan", "memasinkan", "asin-asin", "paling asin"], 1)
        ]
    },
    {
        "slug": "35-circumfix-pen-an-process",
        "title": "【瞬間作文】周囲辞 peN-...-an の動作・過程名詞化（pembangunan, pengembangan）",
        "intro": "周囲辞「peN-...-an」は、能動他動詞 meN- に対応し、「動作のプロセス・過程・行為そのもの（〜すること・建設・開発・調査）」を名詞化します。ニュース報道や学術論文で必ず主語・目的語になる重要名詞を反射的に生成します。",
        "rules": [
            ("meN- の鼻音化と完全一致", "語頭変化は meN- と同じ規則をたどります：bangun → membangun → pembangunan（建設）、kembang → mengembangkan → pengembangan（開発）、tulis → menulis → penulisan（執筆）。"),
            ("「動作・過程（Process）」を表す", "pembangunan（建設すること・建設工事）、pemeriksaan（検査すること・検査手続き）。per-...-an が「結果・状態」を表すのと対照的です。")
        ],
        "drill": [
            ("新首都の建設は順調に進んでいます。", "Pembangunan ibu kota baru berjalan lancar.", "プムバングナン イブ コタ バル ブルジャラン ランチャール", "動作・過程 pembangunan。"),
            ("人材の開発は国家の優先事項です。", "Pengembangan sumber daya manusia adalah prioritas negara.", "プンゲムバンガン スンベル ダヤ マヌシア アダラ プリオリタス ネガラ", "開発 pengembangan。"),
            ("論文の執筆には3ヶ月かかりました。", "Penulisan skripsi memakan waktu tiga bulan.", "プヌリサン スクリプシ メマカン ワクトゥ ティガ ブラン", "執筆 penulisan。"),
            ("医師による患者の検査が始まります。", "Pemeriksaan pasien oleh dokter akan dimulai.", "プムリクサアン パシエン オレ ドクテル アカン ディムライ", "検査 pemeriksaan。"),
            ("新商品の販売が好調です。", "Penjualan produk baru sangat bagus.", "プンジュアルアン プロドゥッ バル サンガット バグス", "販売 penjualan。"),
            ("荷物の配送には2日かかります。", "Pengiriman barang memakan waktu dua hari.", "プンギリマン バラン メマカン ワクトゥ ドゥア ハリ", "配送 pengiriman。"),
            ("森林の破壊は地球温暖化を加速させる。", "Penebangan hutan mempercepat pemanasan global.", "プヌバンガン フタン ムムプルチパット プマナサン グローバル", "伐採 penebangan。"),
            ("警察による容疑者の逮捕。", "Penangkapan tersangka oleh pihak kepolisian.", "プナンカパン トゥルスンカ オレ ピハッ クポリシアン", "逮捕 penangkapan。"),
            ("新しい法律の適用が来月から始まります。", "Penerapan hukum baru akan dimulai bulan depan.", "プヌラパン フクム バル アカン ディムライ ブラン ドゥパン", "適用 penerapan。"),
            ("ゴミの処理は都市の深刻な課題です。", "Pengolahan sampah adalah masalah serius perkotaan.", "プンオラハン サンパ アダラ マサラ セリウス プルコタアン", "処理 pengolahan。"),
            ("問題の解決には時間が必要です。", "Penyelesaian masalah membutuhkan waktu.", "プンユルサイアン マサラ メムブトゥーカン ワクトゥ", "解決 penyelesaian。"),
            ("大統領による閣僚の任命。", "Pengangkatan menteri oleh presiden.", "プンアンカタン ムンテリ オレ プレシデン", "任命 pengangkatan。"),
            ("新薬の臨床試験。", "Pengujian klinis untuk obat baru.", "プンウジアン クリニス ウントゥッ オバット バル", "試験・検査 pengujian。"),
            ("教育を通じた国民意識の育成。", "Pembinaan kesadaran warga melalui pendidikan.", "プムビナアン クサダラン ワルガ ムラルイ プンディディカン", "育成 pembinaan。"),
            ("データ分析の結果が発表されました。", "Hasil pengolahan data sudah diumumkan.", "ハシル プンオラハン データ スダ ディウムムカン", "処理・分析 pengolahan。")
        ],
        "quiz": [
            ("動詞 membangun（建設する）に対応する名詞「建設（プロセス）」は？", ["pembangunan", "perbangunan", "kebangunan", "terbangun"], 1),
            ("動詞 mengirim（送る）に対応する名詞「配送・送付」は？", ["pengiriman", "perkiriman", "kekiriman", "kiriman"], 1),
            ("動詞 menyelesaikan（解決する）に対応する名詞「解決プロセス」は？", ["penyelesaian", "perselesaian", "keselesaian", "selesaian"], 1)
        ]
    },
    {
        "slug": "36-circumfix-per-an-result",
        "title": "【瞬間作文】周囲辞 per-...-an の状態・集約名詞化（perjanjian, perjalanan）",
        "intro": "周囲辞「per-...-an」は、自動詞 ber- に対応し、「行為の結果・状態・制度・集約された場所（〜契約、旅路、集合体）」を名詞化します。peN-...-an が動的な「プロセス」であるのに対し、per-...-an は静的な「フレーム・結果」を提示します。",
        "rules": [
            ("ber- 自動詞に対応する名詞化", "berjalan → perjalanan（旅路・道程）、berjanji → perjanjian（約束・条約・契約）、bertemu → pertemuan（会合・面会）。"),
            ("名詞語根 ＋ per-...-an（場所・集合・制度）", "hotel → perhotelan（ホテル業界）、air → perairan（水域・海域）、kota → perkotaan（都市部）、toko → pertokoan（商店街）。")
        ],
        "drill": [
            ("両国は平和条約に署名しました。", "Kedua negara menandatangani perjanjian damai.", "クドゥア ネガラ ムナンダタンガニ プルジャンジアン ダマイ", "契約・条約 perjanjian。"),
            ("ジョグジャカルタへの長い旅路。", "Perjalanan panjang menuju Yogyakarta.", "プルジャラナン パンジャン ムヌジュ ジョグジャカルタ", "旅路 perjalanan。"),
            ("今夜、重要人物たちの会合があります。", "Ada pertemuan tokoh penting malam ini.", "アダ プルトゥムアン トコ ポンティン マラム イニ", "会合 pertemuan。"),
            ("バリ島のホテル業界は回復しつつあります。", "Industri perhotelan di Bali sedang pulih.", "インダストリ プルホテラン ディ バリ スダン プリー", "業界集約 perhotelan。"),
            ("インドネシアの領海警備を強化する。", "Memperkuat pengawasan di perairan Indonesia.", "メムプルクアット プンガワサン ディ プルアイラン インドネシア", "水域 perairan。"),
            ("都市部への人口集中が続いています。", "Konsentrasi penduduk di wilayah perkotaan berlanjut.", "コンセントラシ プンドゥドゥッ ディ ウィラヤ プルコタアン ブルランジュット", "都市部 perkotaan。"),
            ("商店街で火災が発生しました。", "Kebakaran terjadi di kawasan pertokoan.", "クバカラン トゥルジャディ ディ カワサン プルトコアン", "商店街 pertokoan。"),
            ("彼らは熱い議論を交わしました。", "Mereka terlibat dalam perdebatan sengit.", "ムレカ トゥルリバット ダラム プルデバタン スンギット", "論争 perdebatan。"),
            ("二つの会社の間で合意が成立した。", "Tercapai persetujuan antara kedua perusahaan.", "トゥルチャパイ プルスツジュアン アンタラ クドゥア プルサハアン", "合意 persetujuan。"),
            ("伝統舞踊の公演が行われます。", "Pertunjukan tari tradisional akan digelar.", "プルトゥンジュカン タリ クラシッ アカン ディゲラール", "公演 pertunjukan。"),
            ("両者の意見には大きな違いがある。", "Ada perbedaan besar dalam pendapat keduanya.", "アダ プルベダアン ブサール ダラム プンダパット クドゥアニャ", "相違 perbedaan。"),
            ("私たちは友好関係を維持しなければならない。", "Kita harus menjaga persahabatan kita.", "キタ ハルス メンジャガ プルサハバタン キタ", "友情 persahabatan。"),
            ("家族の結婚式に出席しました。", "Saya menghadiri pesta pernikahan keluarga.", "サヤ ムンハディリ ペスタ プルニカハン クルアルガ", "婚姻 pernikahan。"),
            ("農村部の農業経済を発展させる。", "Mengembangkan ekonomi pertanian di pedesaan.", "ムンゲムバンカン エコノミ プルタニアン ディ プデサアン", "農業 pertanian。"),
            ("国際大会での熱戦。", "Pertandingan seru di turnamen internasional.", "プルタンディンガン スル ディ トゥルナメン インテルナシオナル", "試合 pertandingan。")
        ],
        "quiz": [
            ("動詞 berjanji（約束する）に対応する名詞「契約・条約」は？", ["perjanjian", "penjanjian", "keperjanjian", "janjian"], 1),
            ("「ホテル業界全体」を表す集約名詞は？", ["perhotelan", "penghotelan", "kehotelan", "hotel-hotel"], 1),
            ("「旅路・移動の道のり」を表す名詞は？", ["perjalanan", "penjalanan", "kejalanan", "jalannya"], 1)
        ]
    },
    {
        "slug": "37-pen-an-vs-per-an-contrast",
        "title": "【瞬間作文】peN-...-an と per-...-an の使い分け対比ドリル（pemeriksaan vs periksaan）",
        "intro": "同一の語根から peN-...-an（動作・能動プロセス）と per-...-an（結果・制度・場所）の両方が派生するペアは、検定上級や公的文書で最も差がつく領域です。「検査する行為（pemeriksaan）」と「検査結果/尋問調書（periksaan）」のように、文脈に応じた即時選択を鍛えます。",
        "rules": [
            ("動作プロセス（peN-...-an） vs 結果・制度（per-...-an）", "penyatuan（統一する行為・統合プロセス） vs persatuan（団結・統一状態・連合体）。"),
            ("pembentukan（設立する作業） vs perbentukan（形態・体制）", "pengaturan（規則を整理する作業・調整） vs peraturan（定められた規則・ルールそのもの）。")
        ],
        "drill": [
            ("政府は交通規則を制定しました（規則そのもの）。", "Pemerintah menetapkan peraturan lalu lintas.", "プムリンタ ムヌタップカン プラトゥラン ラル リンタス", "peraturan（ルールそのもの）。"),
            ("信号の調整作業が行われています（調整プロセス）。", "Pengaturan lampu lalu lintas sedang dilakukan.", "プンガトゥラン ランプ ラル リンタス スダン ディラクカン", "pengaturan（調整する作業）。"),
            ("国民の団結と統一（団結状態）。", "Persatuan dan kesatuan bangsa.", "プルサトゥアン ダン クサトゥアン バンサ", "persatuan（団結状態）。"),
            ("二つの銀行の統合プロセス（合併作業）。", "Penyatuan dua bank besar sedang berlangsung.", "プンヤトゥアン ドゥア バンク ブサール スダン ブルラングスン", "penyatuan（統合する作業）。"),
            ("医師による患者の検査（検査する行為）。", "Pemeriksaan pasien oleh dokter.", "プムリクサアン パシエン オレ ドクテル", "pemeriksaan（検査作業）。"),
            ("委員会設立の作業が始まりました。", "Pembentukan komite baru telah dimulai.", "プムベントゥカン コミテ バル トゥラ ディムライ", "pembentukan（設立作業）。"),
            ("生物の骨格構造と形態。", "Struktur dan perbentukan tulang makhluk hidup.", "ストルクトゥール ダン プルベントゥカン トゥラン マフルッ ヒドゥップ", "perbentukan（形態・構造）。"),
            ("新しい道路の建設作業（工事プロセス）。", "Pembangunan jalan baru sedang dikerjakan.", "プムバングナン ジャラン バル スダン ディクルジャカン", "pembangunan（建設作業）。"),
            ("古い建築物の保存（保存行為）。", "Pelestarian bangunan tua bersejarah.", "プルスタリアン バングナン トゥア ブルセジャラ", "pelestarian（保存作業）。"),
            ("労働者たちの組合組織（組織そのもの）。", "Persatuan serikat pekerja nasional.", "プルサトゥアン スリカット プケルジャ ナシオナル", "persatuan（組合・連合）。"),
            ("裁判所での尋問手続き。", "Pemeriksaan saksi di ruang sidang pengadilan.", "プムリクサアン サクシ ディ ルアン シダン プンガディラン", "pemeriksaan（尋問行為）。"),
            ("教育制度の改革（制度そのもの）。", "Reformasi peradilan dan pendidikan nasional.", "レフォルマシ プラディラン ダン プンディディカン ナシオナル", "peradilan（司法制度）。"),
            ("裁判官による裁判の審理（審理する作業）。", "Pengadilan perkara oleh majelis hakim.", "プンガディラン プルカラ オレ マジェリス ハキム", "pengadilan（裁判の執行/裁判所）。"),
            ("会社の発展のための戦略（発展プロセス）。", "Strategi untuk perkembangan perusahaan.", "ストラテギ ウントゥッ プルケムバンガン プルサハアン", "perkembangan（発展状態）。"),
            ("新技術の開発プロジェクト（開発プロセス）。", "Proyek pengembangan teknologi baru.", "プロイェッ プンゲムバンガン テクノロジ バル", "pengembangan（開発作業）。")
        ],
        "quiz": [
            ("法律の「規則・ルールそのもの」を表す単語は？", ["peraturan", "pengaturan", "keturanan", "teratur"], 1),
            ("機械やシステムを「調整する作業（プロセス）」を表す単語は？", ["pengaturan", "peraturan", "keteraturan", "aturan"], 1),
            ("「国民の団結（状態）」を表す単語は？", ["persatuan", "penyatuan", "kesatuan", "satuan"], 1)
        ]
    },
    {
        "slug": "38-reduplication-plural",
        "title": "【瞬間作文】重複語（Kata Ulang）の複数・多様性表現（anak-anak, rumah-rumah）",
        "intro": "インドネシア語で名詞を繰り返す「重複語（Kata Ulang）」は、単なる「複数（〜たち）」にとどまらず、「様々な種類の〜（多様性）」を表します。anak-anak（子供たち）、buah-buahan（色々な果物）など、重複による豊かな表現を瞬時に産出します。",
        "rules": [
            ("単純重複（名詞の複数・集合）", "anak → anak-anak（子供たち）、rumah → rumah-rumah（家々）、mobil → mobil-mobil（車輪・車たち）。数詞がある場合は重複させない点に注意（tiga anak ⭕, tiga anak-anak ❌）。"),
            ("重複 ＋ 接尾辞 -an（様々な種類）", "buah → buah-buahan（色々な果物）、sayur → sayur-sayuran（色々な野菜）、obat → obat-obatan（医薬品類）。")
        ],
        "drill": [
            ("子供たちが校庭で遊んでいます。", "Anak-anak sedang bermain di halaman sekolah.", "アナッアナッ スダン ブルマイン ディ ハラマン スコラ", "複数 anak-anak。"),
            ("市場には様々な果物が売られています。", "Berbagai buah-buahan dijual di pasar.", "ブルバガイ ブアブアハン ディジュアル ディ パサール", "多様性 buah-buahan。"),
            ("通りには車がたくさん並んでいます。", "Mobil-mobil berjejer di sepanjang jalan.", "モビルモビル ブルジェジェル ディ スパンジャン ジャラン", "複数 mobil-mobil。"),
            ("新鮮な野菜を毎日食べなさい。", "Makanlah sayur-sayuran segar setiap hari.", "マカンラ サユルサユラン スガル スティアプ ハリ", "多様性 sayur-sayuran。"),
            ("村の家々は木で作られています。", "Rumah-rumah di desa terbuat dari kayu.", "ルマルマ ディ デサ トゥルブアット ダリ カユ", "家々 rumah-rumah。"),
            ("彼らは様々な書類を提出しました。", "Mereka mengumpulkan surat-surat penting.", "ムレカ ムングンプルカン スラットスラット ポンティン", "複数書類 surat-surat。"),
            ("広場には色とりどりの花が咲いています。", "Bunga-bunga berwarna-warni mekar di taman.", "ブンガブンガ ブルワルナワルニ メカール ディ タマン", "複数 bunga-bunga。"),
            ("薬局であらゆる医薬品を購入する。", "Membeli obat-obatan di apotek.", "ムンブリ オバットオバタン ディ アポテック", "医薬品類 obat-obatan。"),
            ("生徒たちは先生の質問に答えた。", "Murid-murid menjawab pertanyaan guru.", "ムリッドムリッド ムンジャワブ プルタニャアン グル", "生徒たち murid-murid。"),
            ("川で魚たちが泳いでいる。", "Ikan-ikan berenang di sungai yang jernih.", "イカンイカン ブルナン ディ スンガイ ヤン ジュルニ", "魚たち ikan-ikan。"),
            ("古い本が棚に並んでいる。", "Buku-buku lama tersusun di rak.", "ブクブク ラマ トゥルススン ディ ラッ", "本類 buku-buku。"),
            ("お母さんは様々なお菓子を作った。", "Ibu membuat aneka kue-kuean tradisional.", "イブ ムンブアット アネカ クエクエアン トラディシオナル", "お菓子類 kue-kuean。"),
            ("木々の葉が風に揺れている。", "Daun-daun pohon bergoyang ditiup angin.", "ダウンダウン ポホン ブルゴヤン ディティウップ アンギン", "木の葉 daun-daun。"),
            ("観光客たちが記念写真を撮っている。", "Turis-turis sedang mengambil foto kenangan.", "トゥリストゥリス スダン ムンガンビル フォト クナンガン", "観光客たち turis-turis。"),
            ("街の明かりが美しく輝いている。", "Lampu-lampu kota menyala dengan indah.", "ランプランプ コタ メニャラ ドゥンガン インダ", "灯り lampu-lampu。")
        ],
        "quiz": [
            ("「様々な種類の果物」を表す重複語は？", ["buah-buahan", "buah-buah", "berbuah-buah", "kebuan-buahan"], 1),
            ("数詞 tiga（3）と名詞 anak（子供）を組み合わせる正しい文法は？", ["tiga anak", "tiga anak-anak", "anak-anak tiga", "tiga beranak"], 1),
            ("「様々な野菜」を表す正しい形は？", ["sayur-sayuran", "sayur-sayur", "bersayur-sayur", "kesayur-sayuran"], 1)
        ]
    },
    {
        "slug": "39-reduplication-reciprocal",
        "title": "【瞬間作文】重複語の相互行為表現（bersalam-salaman, tolong-menolong）",
        "intro": "接頭辞「ber-」や「meN-」と重複語を組み合わせることで、「お互いに〜し合う（相互行為）」を生き生きと表現できます。bersalaman（握手する）→ bersalam-salaman（互いに次々と握手し合う）、tolong-menolong（助け合う）を瞬時に発話します。",
        "rules": [
            ("ber- 語根 -語根 -an（相互行為・和気あいあい）", "bersalam-salaman（互いに握手を交わし合う）、bermaaf-maafan（お互いに許し合う：レバランの定番）、kejar-kejaran / berkejar-kejaran（追いかけっこする）。"),
            ("語根 ＋ meN-語根（相互助け合い・反復的連動）", "tolong-menolong（互いに助け合う）、tarik-menarik（互いに引き合う・綱引きする）、pukul-memukul（殴り合う）。")
        ],
        "drill": [
            ("断食明け大祭で、人々は互いに許し合いました。", "Saat Lebaran, orang-orang saling bermaaf-maafan.", "サアット ルバラン オランオラン サリン ブルマアフマアファン", "相互 bermaaf-maafan。"),
            ("困難な時には互いに助け合いましょう。", "Mari kita tolong-menolong di saat sulit.", "マリ キタ トロンムノロン ディ サアット スリット", "相互扶助 tolong-menolong。"),
            ("客たちは笑顔で次々と握手を交わした。", "Para tamu bersalam-salaman dengan tersenyum.", "パラ タム ブルサラマサラマン ドゥンガン トゥルスニュム", "相互握手 bersalam-salaman。"),
            ("子供たちが校庭で追いかけっこをしています。", "Anak-anak sedang berkejar-kejaran di lapangan.", "アナッアナッ スダン ブルクジャルクジャラン ディ ラパンガン", "追いかけっこ berkejar-kejaran。"),
            ("二つの会社は激しく競い合っている。", "Kedua perusahaan bersaing-saingan dengan ketat.", "クドゥア プルサハアン ブルサインスタインガン ドゥンガン クタット", "競合 bersaing-saingan。"),
            ("彼らは互いに見つめ合って微笑んだ。", "Mereka saling pandang-memandang dan tersenyum.", "ムレカ サリン パンダンメマンダン ダン トゥルスニュム", "見つめ合い pandang-memandang。"),
            ("村人たちは共同作業で互いに協力し合う。", "Warga desa bahu-membahu dalam gotong royong.", "ワルガ デサ バフムンバフ ダラム ゴトン ロヨン", "協力肩を並べる bahu-membahu。"),
            ("彼らは互いに非難し合っている。", "Mereka saling tuduh-menuduh tanpa bukti.", "ムレカ サリン トゥドゥームヌドゥー タンパ ブクティ", "非難し合い tuduh-menuduh。"),
            ("恋人同士、手を繋ぎ合って歩く。", "Sepasang kekasih berjalan sambil berpegang-pegangan tangan.", "スパサン クカシ ブルジャラン サンビル ブルプガンペガンガン タンガン", "手を握り合う berpegang-pegangan。"),
            ("議論の中で双方が激しく反論し合った。", "Kedua pihak bantah-membantah dalam debat.", "クドゥア ピハッ バンタムンバンタ ダラム デバット", "反論の応酬 bantah-membantah。"),
            ("若者たちが互いにからかい合って笑っている。", "Para pemuda bercanda-candaan sambil tertawa.", "パラ プムダ ブルチャンダイチャンダアン サンビル トゥルタワ", "からかい合い bercanda-candaan。"),
            ("綱引き競技で両チームが力強く引き合った。", "Kedua tim tarik-menarik tali dengan sekuat tenaga.", "クドゥア ティム タリッムナリッ タリ ドゥンガン スクアット トゥナガ", "引き合い tarik-menarik。"),
            ("彼らは別れ際に抱き合い抱擁を交わした。", "Mereka berpeluk-pelukan saat berpisah.", "ムレカ ブルプルッペルカン サアット ブルピサ", "抱擁 berpeluk-pelukan。"),
            ("学生同士、ノートを貸し借りし合っている。", "Para siswa saling pinjam-meminjam catatan.", "パラ シスワ サリン ピンジャムメミンジャム チャタタン", "貸し借り pinjam-meminjam。"),
            ("隣人同士、いつでも訪問し合える関係。", "Tetangga yang saling kunjung-mengunjungi.", "トゥタンガ ヤン サリン クンジュンムングンジュンギ", "往来 kunjung-mengunjungi。")
        ],
        "quiz": [
            ("レバランで人々が「お互いに許し合う」伝統行為を表す言葉は？", ["bermaaf-maafan", "memaafkan", "termaafkan", "maaf-maaf"], 1),
            ("「互いに助け合う」を表す頻出成句は？", ["tolong-menolong", "tolong-tolongan", "menolong-nolong", "pertolongan"], 1),
            ("子供たちが「追いかけっこをする」を表す動詞は？", ["berkejar-kejaran", "mengejar-ngejar", "terkejar-kejar", "kejar-mengejar"], 1)
        ]
    },
    {
        "slug": "40-reduplication-intensity",
        "title": "【瞬間作文】重複語の強調・度合い表現（cepat-cepat, pagi-pagi, mati-matian）",
        "intro": "形容詞や副詞を繰り返すことで、「非常に〜」「急いで〜」「徹底的に〜」という強烈な度合いや真剣味を表現できます。cepat-cepat（急いで）、pagi-pagi（朝早くに）、mati-matian（死に物狂いで）など、感情のこもった発話を瞬時に繰り出します。",
        "rules": [
            ("形容詞・副詞の単純重複（度合いの強調）", "cepat-cepat（大急ぎで）、pagi-pagi（朝早くから）、kecil-kecil（小さいくせに・小柄なのに）、diam-diam（こっそりと・密かに）。"),
            ("重複 ＋ 接尾辞 -an（極限・徹底の強調）", "mati-matian（死に物狂いで・必死に）、habis-habisan（徹底的に・全力を尽くして）、gila-gilaan（狂ったように・破天荒に）。")
        ],
        "drill": [
            ("遅刻しないように大急ぎで行きなさい。", "Pergilah cepat-cepat agar tidak terlambat.", "プルギラ チパッチパット アガル ティダッ トゥルランバット", "強調 cepat-cepat。"),
            ("彼は毎朝早くから畑に出て働いている。", "Dia bekerja di ladang pagi-pagi sekali.", "ディア ブケルジャ ディ ラダン パギパギ スカリ", "強調 pagi-pagi。"),
            ("兵士たちは死に物狂いで陣地を守った。", "Para prajurit bertahan mati-matian membela markas.", "パラ プラジュリット ブルタハン マティマティアン ムンベラ マルカス", "徹底 mati-matian。"),
            ("彼らは部屋からこっそり抜け出した。", "Mereka keluar dari kamar diam-diam.", "ムレカ クルアール ダリ カマール ディアムディアム", "密かに diam-diam。"),
            ("彼は全財産を徹底的に使い果たした。", "Dia menghabiskan uangnya habis-habisan.", "ディア ムンハビスカン ウアンニャ ハビスハビサン", "徹底 habis-habisan。"),
            ("よくよく考えてから決めなさい。", "Pikirkan masak-masak sebelum memutuskan.", "ピキルカン マサッマサッ スブルム ムムトゥスカン", "慎重 masak-masak。"),
            ("夜遅くに一人で歩くのは危険です。", "Berbahaya jalan sendirian malam-malam begini.", "ブルバハヤ ジャラン スンディリアン マラムマラム ブギニ", "強調 malam-malam。"),
            ("遠くから見ると、あの山は青く見える。", "Dari jauh-jauh, gunung itu tampak biru.", "ダリ ジャウジャウ グヌン イトゥ タンパッ ビル", "強調 jauh-jauh。"),
            ("彼は大声を上げて助けを求めた。", "Dia berteriak keras-keras meminta tolong.", "ディア ブルトリアッ クラスクラス メミンタ トロン", "強調 keras-keras。"),
            ("子供たちは狂ったように大喜びした。", "Anak-anak bersorak gila-gilaan karena gembira.", "アナッアナッ ブルソラッ ギラギラアン カルナ グムビラ", "極限 gila-gilaan。"),
            ("話す時ははっきりと口を開けなさい。", "Bicaralah jelas-jelas saat berbicara.", "ビチャララ ジュラスジュラス サアット ブルビチャラ", "強調 jelas-jelas。"),
            ("小柄なのに、彼はとても力持ちです。", "Kecil-kecil begitu, dia sangat kuat.", "クチルクチル ブギトゥ ディア サンガット クアット", "逆説的強調 kecil-kecil。"),
            ("彼は密かに彼女の写真を眺めていた。", "Diam-diam dia memandangi fotonya.", "ディアムディアム ディア メマンダンギ フォトニャ", "密かに diam-diam。"),
            ("試験のために必死になって勉強した。", "Saya belajar mati-matian demi ujian.", "サヤ ブラジャール マティマティアン ドミ ウジアン", "死に物狂い mati-matian。"),
            ("スープを熱々のうちに召し上がれ。", "Makanlah sup ini panas-panas.", "マカンラ スプ イニ パナスパナス", "状態 panas-panas。")
        ],
        "quiz": [
            ("「死に物狂いで、必死に」を表す極限強調の重複語は？", ["mati-matian", "mati-mati", "kematian", "mematikan"], 1),
            ("「朝早くから」を表す強調副詞は？", ["pagi-pagi", "siang-siang", "malam-malam", "sore-sore"], 1),
            ("「こっそりと、密かに」を表す表現は？", ["diam-diam", "keras-keras", "cepat-cepat", "jauh-jauh"], 1)
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

print("Batch 1031-1040 generated successfully.")
