# -*- coding: utf-8 -*-
import os

articles_data = [
    {
        "slug": "31-lucu-menarik-funny-interesting",
        "title": "【誤用克服】「面白い」の lucu（お笑い・滑稽・可愛い）と menarik（興味深い）の取り違え",
        "intro": "日本語の「おもしろい」は、ゲラゲラ笑えるユーモアと、知的好奇心を刺激する興味深さの両方を指しますが、インドネシア語では完全に別単語です。学術書や歴史映画について buku ini lucu と言うと「ギャグ本・お笑い」になり、知的評価を伝えるなら menarik を使わなければなりません。",
        "cases": [
            ("歴史の授業や講演会が「とても面白かった（知的好奇心）」と言う時。", "Kuliah sejarah tadi sangat lucu.", "Kuliah sejarah tadi sangat menarik.", "lucu は「笑える・滑稽・可愛らしい（子供や動物）」という意味です。知的好奇心や関心を引く「面白さ」には必ず menarik を使います。lucu を使うと「講師がピエロのようでおかしかった」という意味になってしまいます。"),
            ("コメディアンの冗談を聞いて「本当に面白い（笑える）」と言う時。", "Lelucon komedian itu sangat menarik.", "Lelucon komedian itu sangat lucu.", "腹を抱えて笑うようなユーモア・冗談には lucu を用います。menarik だと「興味深い社会風刺だ」という冷静な分析のように響きます。")
        ],
        "drill": [
            ("この小説のストーリー展開はとても面白い（興味深い）。", "Alur cerita novel ini sangat menarik.", "アルール チュリタ ノベル イニ サンガット ムナリッ", "興味深い menarik。"),
            ("彼のジョークはいつも面白い（笑える）。", "Lelucon dia selalu lucu.", "ルルチョン ディア スラル ルチュ", "笑える lucu。"),
            ("子供の仕草がとても可愛い（愛らしい・お茶目）。", "Tingkah laku anak itu sangat lucu.", "ティンカ ラク アナッ イトゥ サンガット ルチュ", "愛らしい・お茶目 lucu。"),
            ("インドネシアの歴史についての興味深い記事を読んだ。", "Membaca artikel yang menarik tentang sejarah Indonesia.", "ムンバチャ アルティケル ヤン ムナリッ トンタン スジャラ インドネシア", "興味深い記事 artikel menarik。"),
            ("そのコメディ映画は本当に面白くて大爆笑した。", "Film komedi itu lucu sekali sampai tertawa terbahak-bahak.", "フィルム コメディ イトゥ ルチュ スカリ サンパイ トゥルタワ トゥルバハッバハッ", "爆笑 lucu sekali。"),
            ("この新製品のコンセプトは非常に魅力的だ（興味をそそる）。", "Konsep produk baru ini sangat menarik.", "コンセプト プロドゥッ バル イニ サンガット ムナリッ", "魅力的・興味深い menarik。"),
            ("子猫が毛糸玉で遊ぶ姿が面白い（可愛い）。", "Lucu sekali melihat anak kucing bermain bola benang.", "ルチュ スカリ ムリハット アナッ クチン ブルマイン ボラ ブナン", "愛らしい lucu。"),
            ("観光地としてバリ島には多くの魅力的なスポットがある。", "Sebagai daerah wisata, Bali punya banyak tempat menarik.", "スバガイ ダエラ ウィサタ、バリ プニャ バニャッ トゥムパット ムナリッ", "魅力的な場所 tempat menarik。"),
            ("変な顔をして人を笑わせる（おどけた仕草）。", "Membuat wajah lucu untuk membuat orang tertawa.", "ムンブアット ワジャ ルチュ ウントゥッ ムンブアット オラン トゥルタワ", "変顔 wajah lucu。"),
            ("セミナーでとても興味深いプレゼンテーションを聞いた。", "Mendengar presentasi yang sangat menarik di seminar.", "ムンダンガル プレゼンタスィ ヤン サンガット ムナリッ ディ セミナル", "興味深い発表 presentasi menarik。"),
            ("あの芸人のコントは何度見ても面白い（笑える）。", "Sketsa pelawak itu ditonton berkali-kali tetap lucu.", "スケチャ プラワッ イトゥ ディトントン ブルカリカリ トゥタップ ルチュ", "お笑い lucu。"),
            ("他人の文化を学ぶことは非常に興味深い体験です。", "Mempelajari budaya lain adalah pengalaman yang menarik.", "ムンペラジャリ ブダヤ ライン アダラ プンガラマン ヤン ムナリッ", "興味深い体験 pengalaman menarik。"),
            ("彼の話し方はユーモアがあって面白い。", "Cara bicaranya lucu dan menghibur.", "チャラ ビチャラニャ ルチュ ダン ムンヒブル", "ユーモラス lucu。"),
            ("提案書にとても興味深いデータが含まれている。", "Proposal itu memuat data yang sangat menarik.", "プロポサル イトゥ ムムアット データ ヤン サンガット ムナリッ", "興味深いデータ data menarik。"),
            ("おもしろおかしい話をして場を和ませた。", "Menceritakan kisah lucu untuk mencairkan suasana.", "ムンチュリタカン キサ ルチュ ウントゥッ ムンチャイルカン スアサナ", "面白い話 kisah lucu。")
        ],
        "quiz": [
            ("学術書やドキュメンタリーが「内容的に面白い」と褒める単語は？", ["menarik", "lucu", "aneh", "enak"], 1),
            ("お笑い芸人のコントや冗談が「ゲラゲラ笑える」時の単語は？", ["lucu", "menarik", "bosan", "indah"], 1),
            ("「観光名所・魅力的な場所」を意味する表現は？", ["tempat menarik", "tempat lucu", "tempat ramai", "tempat sepi"], 1)
        ]
    },
    {
        "slug": "32-aneh-lucu-strange-clash",
        "title": "【誤用克服】「おかしい」の aneh（奇妙・異常・不審）と lucu（笑える）の混同是正",
        "intro": "日本語の「おかしい」は、「笑える（funny）」と「奇妙だ・変だ・異常だ（strange/abnormal）」の両方に使われますが、インドネシア語では完全に区別されます。機械の故障や人の不審な行動に対して lucu と言うと「面白がっている」と受け取られ、重大なトラブルを招きます。",
        "cases": [
            ("パソコンの画面が急に点滅して「これ、何かおかしい（変だ）」と言う時。", "Komputer ini agak lucu layarnya.", "Komputer ini agak aneh layarnya. / Ada yang tidak beres.", "機械の不具合、動作異常、怪しい現象には aneh（奇妙・異様）や tidak beres（正常でない）を用います。lucu を使うと「画面がコミカルに踊っていて笑える」という呑気な感想になってしまいます。"),
            ("彼の服の着方が「おどけていて笑える」と言う時。", "Gaya pakaiannya aneh sekali (membuat tertawa).", "Gaya pakaiannya lucu sekali.", "意図的におどけた格好やマスコットのような可愛らしさには lucu を使います。aneh を使うと「不気味だ・頭がおかしい」という侮蔑や不審感のニュアンスになります。")
        ],
        "drill": [
            ("このエンジンから何か変な音がする（異音・異常）。", "Ada suara aneh dari mesin ini.", "アダ スアラ アネ ダリ メシン イニ", "異音 suara aneh。"),
            ("彼の冗談はおかしくてみんな笑った（笑える）。", "Leluconnya lucu dan semua orang tertawa.", "ルルチョンニャ ルチュ ダン スムア オラン トゥルタワ", "笑える lucu。"),
            ("夜中に外から奇妙な物音が聞こえた（不審・怪奇）。", "Terdengar suara aneh dari luar tengah malam.", "トゥルダンガル スアラ アネ ダリ ルアル トゥンガ マラム", "奇妙な音 suara aneh。"),
            ("そんな言い訳をするなんて、どう考えてもおかしい（不条理）。", "Aneh sekali kalau memberi alasan seperti itu.", "アネ スカリ カラウ ムンブリ アラサン スペルティ イトゥ", "不自然・変 aneh。"),
            ("着ぐるみを着たスタッフが歩き回ってて面白い（コミカル）。", "Staf yang memakai kostum boneka itu lucu sekali.", "スタフ ヤン ムマカイ コストゥム ボネカ イトゥ ルチュ スカリ", "コミカル lucu。"),
            ("このスープ、何だか変な味がする（異味）。", "Sup ini rasanya agak aneh.", "スップ イニ ラサニャ アガッ アネ", "変な味 rasa aneh。"),
            ("急に彼が優しくなったのはどこか怪しい（不審）。", "Tiba-tiba dia jadi baik, agak aneh rasanya.", "ティバティバ ディア ジャディ バイッ、アガッ アネ ラサニャ", "怪しい・不自然 aneh。"),
            ("彼のリアクションがいちいち面白くて笑える。", "Reaksinya selalu lucu membuat kita tertawa.", "レアクスィニャ スラル ルチュ ムンブアット キタ トゥルタワ", "笑える lucu。"),
            ("パソコンがフリーズして動かない、おかしいな。", "Komputernya macet tidak bisa jalan, aneh ya.", "コンピュテルニャ マチェット ティダッ ビサ ジャラン、アネ ヤ", "機械の異常 aneh。"),
            ("彼がそんなミスをするなんて信じられない、変だな。", "Aneh sekali dia bisa membuat kesalahan fatal seperti itu.", "アネ スカリ ディア ビサ ムンブアット クサラハン ファタル スペルティ イトゥ", "不可解 aneh sekali。"),
            ("アニメのキャラクターがドタバタ動いて面白い。", "Karakter animasinya bergerak lucu.", "カラクテル アニマスィニャ ブルグラッ ルチュ", "コミカル lucu。"),
            ("この契約書の文面、どこかおかしいところはないか？", "Apakah ada pasal yang aneh dalam kontrak ini?", "アパカ アダ パサル ヤン アネ ダラム コントラッ イニ", "条文の不備・不審 aneh。"),
            ("誰もいないはずの部屋から足音がする、不気味だ。", "Ada suara langkah kaki di kamar kosong, aneh banget.", "アダ スアラ ランカ カキ ディ カマル コソン、アネ バンゲット", "不気味 aneh banget。"),
            ("変な夢を見て目が覚めた（悪夢・奇妙な夢）。", "Terbangun karena mimpi yang sangat aneh.", "トゥルバングン カレナ ミンピ ヤン サンガット アネ", "奇妙な夢 mimpi aneh。"),
            ("赤ちゃんが変顔をして笑わせてくれた。", "Bayinya membuat wajah lucu dan tertawa.", "バイニャ ムンブアット ワジャ ルチュ ダン トゥルタワ", "変顔・愛嬌 wajah lucu。")
        ],
        "quiz": [
            ("車のブレーキから異音がして「何かおかしい」と言う時の単語は？", ["aneh", "lucu", "senang", "cantik"], 1),
            ("芸人のギャグが「おかしくて笑える」と言う時の単語は？", ["lucu", "aneh", "rusak", "gelap"], 1),
            ("「このスープは変な味がする」の表現は？", ["Sup ini rasanya aneh.", "Sup ini rasanya lucu.", "Sup ini rasanya manis.", "Sup ini rasanya gurih."], 1)
        ]
    },
    {
        "slug": "33-mudah-gampang-susah-sulit",
        "title": "【誤用克服】「〜しやすい/にくい」の mudah / susah と gampang / sulit のレジスター使い分け",
        "intro": "インドネシア語で「簡単・容易」を表す mudah と gampang、「困難・難しい」を表す sulit と susah は、意味は似ていますが文脈とレジスター（改まり度）が異なります。公式ビジネス文書で gampang/susah を多用すると幼く響き、動詞への接続パターンにも注意が必要です。",
        "cases": [
            ("ビジネスの契約書や公式報告書で「解決が極めて困難である」と書く時。", "Masalah ini susah sekali diselesaikan.", "Masalah ini sangat sulit diselesaikan.", "公式文書・学術論文・フォーマルスピーチでは sulit（困難）および mudah（平易）を用います。susah や gampang は日常口語（bahasa percakapan）の響きが強くなります。"),
            ("「このペンは書きやすい（使いやすい）」と言う時。", "Pulpen ini mudah untuk tulis.", "Pulpen ini enak / mudah dipakai untuk menulis.", "インドネシア語で「〜しやすい」は mudah dipakai / enak digunakan など動詞の受動的適性を表す形を用います。直訳で mudah untuk menulis とすると構文が崩れます。")
        ],
        "drill": [
            ("この試験問題はとても簡単だ（公式・客観評価）。", "Soal ujian ini sangat mudah.", "ソアル ウジアン イニ サンガット ムダ", "平易 mudah。"),
            ("そんなの簡単だよ！すぐできる（口語）。", "Itu sih gampang! Cepat selesai.", "イトゥ シ ガンパン！ チパット スルサイ", "口語の簡単 gampang。"),
            ("この経済問題の解決は極めて困難だ（公式・文語）。", "Penyelesaian masalah ekonomi ini sangat sulit.", "プニェレサイアン マサラ エコノミ イニ サンガット スリット", "困難 sulit。"),
            ("最近、生活が苦しくてお金に困っている（生計・苦難）。", "Akhir-akhir ini hidup susah cari uang.", "アキールアキール イニ ヒドゥップ スサ チャリ ウアン", "生計の苦難 susah。"),
            ("このスマホは操作がしやすくて便利だ。", "Ponsel ini mudah dioperasikan dan praktis.", "ポンセル イニ ムダ ディオペラスィカン ダン プラクティス", "操作容易 mudah dioperasikan。"),
            ("彼の性格は理解しにくい（頑固・気難しい）。", "Sifatnya susah ditebak / sulit dimengerti.", "スィファットニャ スサ ディトゥバッ / スリット ディムンゲルティ", "理解困難 sulit dimengerti。"),
            ("初心者でも簡単に学べるインドネシア語。", "Bahasa Indonesia yang mudah dipelajari oleh pemula.", "バハサ インドネシア ヤン ムダ ディペラジャリ オレ プムラ", "習得容易 mudah dipelajari。"),
            ("口で言うのは簡単だが、実行するのは難しい。", "Ngomongnya gampang, tapi praktiknya susah.", "ンゴモンニャ ガンパン、タピ プラクティッニャ スサ", "口語対比 gampang vs susah。"),
            ("この部屋は風通しが良くて過ごしやすい。", "Ruangan ini nyaman ditinggali karena sejuk.", "ルアンガン イニ ニャマン ディティンガリ カレナ スジュッ", "快適・過ごしやすい nyaman。"),
            ("ビザの申請手続きが複雑で手こずった。", "Prosedur pengajuan visa cukup rumit dan sulit.", "プロセドゥル プンガジュアン ヴィサ チュクップ ルミット ダン スリット", "複雑困難 rumit dan sulit。"),
            ("簡単に諦めないで、もう少し頑張って！", "Jangan gampang menyerah, berjuanglah sedikit lagi!", "ジャンガン ガンパン ムニェラ、ブルジュアンラ スディキット ラギ", "安易に jangan gampang。"),
            ("割れやすいので取り扱い注意（注意書き）。", "Mudah pecah, harap berhati-hati.", "ムダ プチャ、ハラップ ブルハティハティ", "破損容易 mudah pecah。"),
            ("彼を説得するのは至難の業だ。", "Sangat sulit untuk membujuk dia.", "サンガット スリット ウントゥッ ムンブジュッ ディア", "説得困難 sangat sulit membujuk。"),
            ("ジャカルタの渋滞時はタクシーを捕まえにくい。", "Susah dapat taksi saat jam macet di Jakarta.", "スサ ダパット タクスィ サアット ジャム マチェット ディ ジャカルタ", "確保困難 susah dapat...。"),
            ("このアプリは使いやすくて初心者向けだ。", "Aplikasi ini ramah pengguna dan mudah digunakan.", "アプリカスィ イニ ラマ プングナ ダン ムダ ディグナカン", "使いやすい mudah digunakan。")
        ],
        "quiz": [
            ("公式ビジネス文書で「困難な課題」と書く場合の適切な表現は？", ["tantangan yang sulit", "tantangan yang susah", "tantangan yang gampang", "tantangan yang payah"], 1),
            ("「言うのは易く行うは難し」の口語的な対比表現は？", ["gampang / susah", "mudah / enak", "sulit / rumit", "gampang / lancar"], 1),
            ("荷物の「ワレモノ注意（壊れやすい）」の定型表記は？", ["Mudah Pecah", "Gampang Hancur", "Susah Pecah", "Sulit Rusak"], 1)
        ]
    },
    {
        "slug": "34-apa-apakah-indirect-question",
        "title": "【誤用克服】疑問詞 apa と apakah の混同（Yes/No疑問文と間接疑問・名詞節）",
        "intro": "何でも「ですか？」を apa で済ませていませんか？apa は「何（what）」を問う疑問代名詞であり、文全体を Yes/No 疑問文にする標識、および間接疑問「〜かどうか（whether）」には apakah を用いるのが標準的です。両者の文法的役割を完全峻別します。",
        "cases": [
            ("初対面で「あなたは日本人ですか？（Yes/No疑問）」と尋ねる時。", "Apa Anda orang Jepang?", "Apakah Anda orang Jepang?", "文頭に apa のみを置くのは口語では許容されますが、標準文法および丁寧な会話では Yes/No 疑問詞の apakah を用いるのが正確です。apa だと「あなたは何日本人ですか？」のような奇妙な響きを孕みます。"),
            ("「彼が来るかどうか分かりません（間接疑問）」と言う時。", "Saya tidak tahu apa dia datang.", "Saya tidak tahu apakah dia akan datang atau tidak.", "「〜かどうか」という名詞節・間接疑問には必ず apakah（または apakah ... atau tidak）を用います。apa 単体だと「彼が何を持ってくるか分からない」と誤解される恐れがあります。")
        ],
        "drill": [
            ("これは何ですか？（what）", "Apa ini? / Ini apa?", "アパ イニ / イニ アパ", "何 apa。"),
            ("明日の会議に出席されますか？（Yes/No疑問）", "Apakah Anda akan menghadiri rapat besok?", "アパカ アンダ アカン ムンハディリ ラパット ブソッ", "Yes/No疑問 Apakah...。"),
            ("彼が賛成するかどうか確認してください（間接疑問）。", "Tolong pastikan apakah dia setuju atau tidak.", "トロン パスティカン アパカ ディア ス トゥジュ アタウ ティダッ", "〜かどうか apakah... atau tidak。"),
            ("何を食べているのですか？", "Apa yang sedang Anda makan?", "アパ ヤン スダン アンダ マカン", "何を apa yang...。"),
            ("この部屋でタバコを吸ってもいいですか？（許可Yes/No）", "Apakah boleh merokok di ruangan ini?", "アパカ ボレ ムロコッ ディ ルアンガン イニ", "許可尋ね Apakah boleh...。"),
            ("プロジェクトが成功するかどうかはチームワーク次第だ。", "Apakah proyek ini berhasil atau tidak bergantung pada kerja sama tim.", "アパカ プロイェッ イニ ブルハスィル アタウ ティダッ ブルガントゥン パダ クルジャ サマ ティム", "成否主語節 Apakah...。"),
            ("何時ですか？（何・時刻）", "Jam berapa sekarang?", "ジャム ブラパ スカラン", "何時 jam berapa。"),
            ("あなたが言っている意味が分かりません（what節）。", "Saya tidak mengerti apa yang Anda maksud.", "サヤ ティダッ ムンゲルティ アパ ヤン アンダ マクスッド", "意味するもの apa yang dimaksud。"),
            ("本当にそれで大丈夫ですか？（確認Yes/No）", "Apakah Anda benar-benar yakin dengan itu?", "アパカ アンダ ブナルブナル ヤキン ドゥンガン イトゥ", "確信尋ね Apakah... yakin。"),
            ("彼らがどこに住んでいるか知っていますか？", "Apakah Anda tahu di mana mereka tinggal?", "アパカ アンダ タフ ディ マナ ムレカ ティンガル", "間接疑問 Apakah Anda tahu...。"),
            ("昨夜、何があったのですか？（何が起きたか）", "Apa yang terjadi tadi malam?", "アパ ヤン トゥルジャディ タディ マラム", "出来事 apa yang terjadi。"),
            ("今日、雨が降るかどうか天気予報を見よう。", "Mari cek ramalan cuaca apakah hari ini akan hujan.", "マリ チェッ ラマラン チュアチャ アパカ ハリ イニ アカン フジャン", "降雨の有無 apakah hujan。"),
            ("何か質問はありますか？", "Apakah ada pertanyaan?", "アパカ アダ プルタニャアン", "質問の有無 Apakah ada...。"),
            ("どうしてそんなことを言ったのか理解できない。", "Saya tidak paham apa alasan dia berkata begitu.", "サヤ ティダッ パハム アパ アラサン ディア ブルカタ ブギトゥ", "何の理由 apa alasan。"),
            ("準備はすべて整いましたか？", "Apakah semua persiapan sudah selesai?", "アパカ スムア プルスィアパン スダ スルサイ", "完了確認 Apakah... sudah selesai。")
        ],
        "quiz": [
            ("「彼が来るかどうか知っていますか？」の間接疑問接続詞は？", ["apakah", "apa", "siapa", "mengapa"], 1),
            ("フォーマルなYes/No疑問文の文頭に置くべき語は？", ["Apakah", "Apa sih", "Berapa", "Bagaimana"], 1),
            ("「あなたは何を求めていますか？」の疑問詞は？", ["Apa yang", "Apakah yang", "Siapakah", "Kapan"], 1)
        ]
    },
    {
        "slug": "35-setelah-sesudah-sejak-timeline",
        "title": "【誤用克服】「〜してから」の setelah / sesudah と sejak（〜以来）の時間軸整理",
        "intro": "日本語の「〜してから」には、単なる動作の前後関係（〜した後に）と、過去の起点を表す（〜して以来ずっと）の2つの意味があります。これを混同して「日本に来てからずっと勉強している」を setelah datang と言うと、継続アスペクトが崩れて不自然になります。",
        "cases": [
            ("「インドネシアに来て以来、ずっとバリ島に住んでいます」と言う時。", "Setelah datang ke Indonesia, saya tinggal di Bali.", "Sejak datang ke Indonesia, saya terus tinggal di Bali.", "過去の時点を起点として現在まで状態が継続している場合は必ず sejak（〜以来）を用います。setelah だと単なる一回限りの前後関係（〜した後に）になり、継続のニュアンスが消えてしまいます。"),
            ("「ご飯を食べてから薬を飲みなさい（順序）」と言う時。", "Sejak makan nasi, minumlah obat.", "Setelah / Sesudah makan nasi, minumlah obat.", "動作の単なる時間的前後関係（Aを完了した後にBをする）には setelah または sesudah を用います。sejak を使うと「ご飯を食べて以来ずっと薬を飲み続けなさい」という奇妙な指示になります。")
        ],
        "drill": [
            ("朝食を食べた後にコーヒーを飲む（前後順序）。", "Setelah sarapan pagi, saya minum kopi.", "ストゥラ サラパン パギ、サヤ ミヌム コピ", "順序 setelah。"),
            ("子供の頃からずっとサッカーが好きです（過去からの継続起点）。", "Sejak kecil saya selalu suka sepak bola.", "スジャッ クチル サヤ スラル スカ スパッ ボラ", "継続起点 sejak。"),
            ("卒業してから5年間この会社で働いています。", "Sejak lulus kuliah, sudah lima tahun bekerja di sini.", "スジャッ ルルス クリア、スダ リマ タフン ブルクルジャ ディ シニ", "継続 sejak lulus。"),
            ("手を洗ってから食事を始めてください（順序）。", "Cucilah tangan sebelum dan setelah makan.", "チュチラ タンガン スブルム ダン ストゥラ マカン", "順序 setelah makan。"),
            ("彼と出会って以来、私の人生は変わった。", "Sejak bertemu dia, hidup saya berubah.", "スジャッ ブルトゥム ディア、ヒドゥップ サヤ ブルバ", "起点 sejak bertemu。"),
            ("会議が終わった後ですぐにご連絡します。", "Saya akan segera menghubungi Anda setelah rapat selesai.", "サヤ アカン スグラ ムンフブンギ アンダ ストゥラ ラパット スルサイ", "事後 setelah rapat。"),
            ("先週からずっと熱が下がらない（継続）。", "Sejak minggu lalu demamnya tidak turun-turun.", "スジャッミング ラル ドゥマムニャ ティダッ トゥルントゥルン", "起点 sejak minggu lalu。"),
            ("映画を見終わってからカフェでおしゃべりした。", "Setelah menonton film, kami mengobrol di kafe.", "ストゥラ メノントン フィルム、カミ ムンオブロル ディ カフェ", "事後 setelah menonton。"),
            ("独立以来、この国は目覚ましい発展を遂げた。", "Sejak kemerdekaan, negara ini berkembang pesat.", "スジャッ クムルデカアン、ヌガラ イニ ブルクンバン プサット", "歴史的起点 sejak。"),
            ("よく検討した上で決定を下します。", "Akan mengambil keputusan setelah mempertimbangkan dengan matang.", "アカン メンガンビル クプトゥサン ストゥラ ムンプルティンバンカン ドゥンガン マタン", "検討後 setelah...。"),
            ("今朝からずっと雨が降り続いている。", "Hujan terus turun sejak pagi tadi.", "フジャン トゥルス トゥルン スジャッ パギ タディ", "継続 sejak pagi tadi。"),
            ("パスポートを受け取ってから航空券を予約する。", "Memesan tiket pesawat setelah menerima paspor.", "ムメサン ティケット プサワット ストゥラ メネリマ パスポル", "順序 setelah menerima。"),
            ("あの事故以来、彼は車を運転しなくなった。", "Sejak kecelakaan itu, dia tidak mau menyetir mobil lagi.", "スジャッ クチュラカアン イトゥ、ディア ティダッ マウ メニョティル モビル ラギ", "心理的起点 sejak。"),
            ("夕立が止んだ後、綺麗な虹が出た。", "Setelah hujan reda, muncul pelangi yang indah.", "ストゥラ フジャン レダ、ムンチュル プランギ ヤン インダ", "事後 setelah hujan reda。"),
            ("入社以来、無遅刻無欠勤を貫いている。", "Sejak masuk kerja, tidak pernah terlambat atau absen.", "スジャッ マスッ クルジャ、ティダッ プルナ トゥルランバット アタウ アブセン", "継続 sejak masuk kerja。")
        ],
        "quiz": [
            ("「子供の時から（以来）ずっと」を表す正しい前置詞は？", ["sejak kecil", "setelah kecil", "sesudah kecil", "sampai kecil"], 1),
            ("「会議が終わった後に電話する」の順序を表す接続詞は？", ["setelah / sesudah", "sejak", "selama", "sebelum"], 1),
            ("「インドネシアに来て以来ずっと働いている」の適切な表現は？", ["Sejak datang terus bekerja", "Setelah datang pernah kerja", "Sesudah datang tidak kerja", "Sebelum datang sedang kerja"], 1)
        ]
    },
    {
        "slug": "36-frequency-adverbs-placement",
        "title": "【誤用克服】頻度副詞 selalu, sering, kadang-kadang, jarang の語順と誤用防止",
        "intro": "頻度副詞（いつも・しばしば・時々・めったに〜ない）の位置は文の意味や自然さに直結します。特に jarang はそれ自体に「めったに〜ない（否定）」のニュアンスが含まれるため、日本語の「めったに食べない」を tidak jarang makan と直訳すると「しばしば食べる」という二重否定の逆の意味になります。",
        "cases": [
            ("「私はドリアンをめったに食べません」と言う時。", "Saya tidak jarang makan durian.", "Saya jarang makan durian.", "jarang は単体で「めったに〜しない（rarely/seldom）」を表す準否定副詞です。tidak jarang と言うと「めったに〜しないわけではない＝頻繁に食べる（quite often）」という肯定強調になってしまいます。"),
            ("「彼はいつも朝遅刻してくる」と述語を修飾する時。", "Dia datang terlambat selalu.", "Dia selalu datang terlambat.", "selalu（いつも）や sering（しばしば）などの頻度副詞は、基本的に修飾する動詞・述語の直前に置くのが標準的です。英語のように文末に放り出すと不自然になります。")
        ],
        "drill": [
            ("彼は毎朝いつもジョギングをしている（100%）。", "Dia selalu joging setiap pagi.", "ディア スラル ジョギン スティアッ パギ", "常に selalu。"),
            ("私は週末によくモールへ行きます（頻繁）。", "Saya sering pergi ke mal saat akhir pekan.", "サヤ スリン プルギ ク マル サアット アキール プカン", "頻繁 sering。"),
            ("時々、昔の友達と電話で話す（時々）。", "Kadang-kadang saya mengobrol lewat telepon dengan teman lama.", "カダンカダン サヤ ムンオブロル ルワット テレポン ドゥンガン トゥマン ラマ", "時々 kadang-kadang。"),
            ("彼は外食をめったにしない（めったに〜ない）。", "Dia jarang makan di luar.", "ディア ジャラン マカン ディ ルアル", "めったに〜ない jarang。"),
            ("決して諦めてはいけません（完全否定）。", "Jangan pernah menyerah sama sekali.", "ジャンガン プルナ ムニェラ サマ スカリ", "決して〜ない jangan pernah。"),
            ("彼女はいつも笑顔で挨拶してくれる。", "Dia selalu menyapa dengan senyuman.", "ディア スラル メニャパ ドゥンガン スニュマン", "常に selalu menyapa。"),
            ("雨季にはよく洪水が起こる（頻出）。", "Sering terjadi banjir saat musim hujan.", "スリン トゥルジャディ バンジル サアット ムスィム フジャン", "頻発 sering terjadi。"),
            ("たまには一人でゆっくりカフェで過ごしたい。", "Kadang-kadang ingin santai sendirian di kafe.", "カダンカダン インギン サンタイ スンディリアン ディ カフェ", "たまには kadang-kadang。"),
            ("私はお酒をめったに飲みません。", "Saya jarang sekali minum minuman keras.", "サヤ ジャラン スカリ ミヌム ミヌマン クラス", "めったに飲まない jarang sekali。"),
            ("約束の時間は必ず守らなければならない。", "Harus selalu menepati janji waktu.", "ハルス スラル ムヌパティ ジャンジ ワクトゥ", "常に守る selalu menepati。"),
            ("彼女は滅多に怒らない温厚な人だ。", "Dia orang yang sabar dan jarang marah.", "ディア オラン ヤン サバル ダン ジャラン マラ", "めったに怒らない jarang marah。"),
            ("彼はしょっちゅう忘れ物をする。", "Dia sering sekali ketinggalan barang.", "ディア スリン スカリ クティンガラン バラン", "しょっちゅう sering sekali。"),
            ("時には立ち止まって自分を見つめ直すことも必要だ。", "Kadang-kadang perlu berhenti sejenak untuk refleksi diri.", "カダンカダン プルル ブルヘンティ スブンタル ウントゥッ レフレクスィ ディリ", "時には kadang-kadang。"),
            ("父は日曜日にいつも洗車をしている。", "Ayah selalu mencuci mobil pada hari Minggu.", "アヤ スラル ムンチュチ モビル パダ ハリミング", "いつも selalu mencuci。"),
            ("最近、彼とはめったに会えていない。", "Akhir-akhir ini saya jarang bertemu dengan dia.", "アキールアキール イニ サヤ ジャラン ブルトゥム ドゥンガン ディア", "めったに会わない jarang bertemu。")
        ],
        "quiz": [
            ("「彼はめったに遅刻しない」の最も自然な表現は？", ["Dia jarang terlambat.", "Dia tidak jarang terlambat.", "Dia selalu tidak terlambat.", "Dia terlambat jarang."], 1),
            ("tidak jarang が表す本当の意味は？", ["頻繁にある（めったにないわけではない）", "全くない", "時々ある", "常にない"], 1),
            ("「いつも・常に」を表す副詞 selalu の標準的な位置は？", ["動詞・述語の直前", "文の最後尾", "名詞と形容詞の間", "前置詞の直後"], 1)
        ]
    },
    {
        "slug": "37-mungkin-barangkali-bisa-jadi",
        "title": "【誤用克服】「〜かもしれない」の mungkin, barangkali, bisa jadi の確信度グラデーション",
        "intro": "日本語の「〜かもしれない」「たぶん」に当たる表現には mungkin, barangkali, bisa jadi があります。これらは話者の確信度や口語／文語のレジスターによって使い分けられます。また、単なる可能（bisa）と推量（bisa jadi）の混同も頻発するエラーです。",
        "cases": [
            ("「彼は明日来られないかもしれない」と推測を述べる時。", "Dia tidak bisa datang besok (mungkin).", "Mungkin dia tidak bisa datang besok.", "mungkin（たぶん・かもしれない）は推量の助動詞／副詞として文頭または述語の前に置きます。文末に置いたり bisa と混同すると推量の焦点がぼやけます。"),
            ("噂話などで「それ、あり得るかもね！（そうかも）」と相槌を打つ時。", "Mungkin saja bisa.", "Bisa jadi! / Bisa saja.", "会話の中で「あり得る！」「そうかもしれない」と口語で相槌を打つ際は Bisa jadi! が最も生き生きとした表現です。単に Mungkin と言うよりも可能性への納得感が伝わります。")
        ],
        "drill": [
            ("たぶん明日は雨が降るでしょう（一般的な推量）。", "Mungkin besok akan turun hujan.", "ムンキン ブソッ アカン トゥルン フジャン", "たぶん mungkin。"),
            ("もしかしたら彼は道に迷ったのかもしれない（控えめな推測）。", "Barangkali dia tersesat di jalan.", "バランカリ ディア トゥルスサット ディ ジャラン", "もしかしたら barangkali。"),
            ("それ、本当かもしれないね！（あり得る・口語相槌）", "Bisa jadi kabar itu benar!", "ビサ ジャディ カバル イトゥ ブナル", "あり得る bisa jadi。"),
            ("彼はまだオフィスにいるかもしれません。", "Mungkin dia masih ada di kantor.", "ムンキン ディア マシ アダ ディ カントール", "推量 mungkin masih ada。"),
            ("ご迷惑でなければ、明日お伺いしてもよろしいでしょうか？（丁寧な前置き）", "Barangkali Bapak berkenan, saya ingin berkunjung besok.", "バランカリ バパッ ブルクナン、サヤ インギン ブルクンジュン ブソッ", "控えめな打診 barangkali。"),
            ("計画の変更もあり得ます（可能性の示唆）。", "Bisa jadi rencana ini akan berubah.", "ビサ ジャディ レンチャナ イニ アカン ブルバ", "変更の可能性 bisa jadi。"),
            ("彼女は病気で休んでいるのかもしれない。", "Mungkin dia tidak masuk kerja karena sakit.", "ムンキン ディア ティダッ マスッ クルジャ カレナ サキッ", "推量 mungkin sakit。"),
            ("彼が犯人である可能性も十分にある（推論）。", "Bisa jadi dialah pelakunya.", "ビサ ジャディ ディアラ プラクニャ", "可能性 bisa jadi。"),
            ("おそらく彼らはもう合意に達したはずだ。", "Kemungkinan besar mereka sudah mencapai kesepakatan.", "クムンキナン ブサル ムレカ スダ ムンチャパイ クスパカタン", "高い可能性 kemungkinan besar。"),
            ("もしかしたら私の勘違いかもしれません（謙遜）。", "Barangkali saya yang salah paham.", "バランカリ サヤ ヤン サラ パハム", "もしかして barangkali。"),
            ("明日のフライトは遅延するかもしれない。", "Penerbangan besok mungkin akan mengalami keterlambatan.", "プネルバンガン ブソッ ムンキン アカン ムンガラミ クトゥルランバタン", "遅延推量 mungkin tertunda。"),
            ("価格が上がる可能性は否定できない。", "Bisa jadi harganya akan naik lagi.", "ビサ ジャディ ハルガニャ アカン ナイス ラギ", "価格上昇の可能性 bisa jadi。"),
            ("彼らはすでにそのニュースを知っているかもしれない。", "Mungkin mereka sudah tahu berita tersebut.", "ムンキン ムレカ スダ タフ ブリタ トゥルスブット", "推量 mungkin sudah tahu。"),
            ("何事も不可能なことはない（ことわざ）。", "Tidak ada yang tidak mungkin di dunia ini.", "ティダッ アダ ヤン ティダッ ムンキン ディ ドゥニア イニ", "不可能はない tidak mungkin。"),
            ("それもありだね、一理あるよ（同意）。", "Bisa jadi begitu, ada benarnya juga.", "ビサ ジャディ ブギトゥ、アダ ブナルニャ ジュガ", "あり得る bisa jadi begitu。")
        ],
        "quiz": [
            ("会話で「あり得るね！その可能性はある」と相槌を打つ口語表現は？", ["Bisa jadi!", "Mungkin tidak!", "Pasti bukan!", "Harus jadi!"], 1),
            ("手紙や目上への発話で「もしよろしければ」と控えめに切り出す語は？", ["Barangkali", "Pasti", "Wajib", "Bisa saja"], 1),
            ("「極めて高い可能性で（十中文八九）」を意味する名詞句は？", ["kemungkinan besar", "mungkin kecil", "bisa jadi banyak", "barangkali tinggi"], 1)
        ]
    },
    {
        "slug": "38-baru-saja-pas-tepat-timing",
        "title": "【誤用克服】「ちょうど〜したところ」の baru saja と pas / tepat（合致）の使い分け",
        "intro": "日本語の「ちょうど」には、直前に動作を終えたばかりの時制（ちょうど食べたところ）と、時間や寸法・状況がピタリと一致している状態（ちょうど3時、ちょうど良いサイズ）があります。これを混同して「ちょうど着いた」に tepat sampai と言うと不自然になります。",
        "cases": [
            ("「今ちょうど空港に着いたところです（直前完了）」と連絡する時。", "Saya tepat sampai di bandara sekarang.", "Saya baru saja sampai di bandara sekarang.", "動作が「たった今完了したばかり」という直前完了には baru saja（口語では baru）を用います。tepat は「正確な時刻・地点への合致（tepat waktu = 定刻）」を表すため、tepat sampai だと「狂いなく到着した」という不自然な表現になります。"),
            ("「ちょうど3時ちょうどです（時刻の一致）」と言う時。", "Sekarang baru saja jam 3.", "Sekarang tepat pukul 3. / Pas jam 3.", "時刻や数値がピッタリ一致している場合は tepat や口語の pas を使います。baru saja jam 3 と言うと「3時になったばかり」という時間経過の強調になります。")
        ],
        "drill": [
            ("たった今、家に着いたところです（直前完了）。", "Saya baru saja sampai di rumah.", "サヤ バル サジャ サンパイ ディ ルマ", "直前完了 baru saja。"),
            ("ちょうど3時ぴったりに会議が始まった（時刻合致）。", "Rapat dimulai tepat pukul tiga.", "ラパット ディムライ トゥパット プクル ティガ", "時刻一致 tepat pukul...。"),
            ("この靴のサイズ、私の足にちょうどピッタリだ（サイズ合致）。", "Ukuran sepatu ini pas sekali di kaki saya.", "ウクラン スパトゥ イニ パス スカリ ディ カキ サヤ", "サイズ合致 pas sekali。"),
            ("彼はいま出かけたばかりです（直前）。", "Dia baru saja berangkat beberapa menit lalu.", "ディア バル サジャ ブランカット ブブラパ メニット ラル", "直前出発 baru saja berangkat。"),
            ("ちょうど良いタイミングで雨が止んだ。", "Pas banget, hujannya berhenti tepat waktu.", "パス バンゲット、フジャンニャ ブルヘンティ トゥパット ワクトゥ", "好タイミング pas banget。"),
            ("お風呂から上がったばかりで髪が濡れている。", "Baru saja selesai mandi, rambut masih basah.", "バル サジャ スルサイ マンディ、ラムブット マシ バサ", "直前入浴 baru saja mandi。"),
            ("お釣りのないよう、ちょうど1万ルピアお支払いします（金額一致）。", "Membayar dengan uang pas sepuluh ribu rupiah.", "ムンバヤル ドゥンガン ウアン パス スプル リブ ルピア", "ぴったりのお金 uang pas。"),
            ("いま昼食を食べ終えたところです。", "Saya baru saja selesai makan siang.", "サヤ バル サジャ スルサイ マカン スィアン", "食後直後 baru saja selesai。"),
            ("電車が定刻通り正確に到着した（定刻）。", "Kereta tiba tepat waktu sesuai jadwal.", "クレタ ティバ トゥパット ワクトゥ ススアイ ジャドワル", "定刻 tepat waktu。"),
            ("噂をすれば影、ちょうど彼から電話がかかってきた！", "Panjang umur, pas banget dia telepon!", "パンジャン ウムル、パス バンゲット ディア テレポン", "グッドタイミング pas banget。"),
            ("大学を卒業したばかりのフレッシュマンです。", "Dia baru saja lulus dari universitas.", "ディア バル サジャ ルルス ダリ ユニヴェルシタス", "新卒 baru saja lulus。"),
            ("的の真ん中に正確に命中した（地点合致）。", "Mengenai tepat di tengah sasaran.", "ムンゲナイ トゥパット ディ トゥンガ ササラン", "中心合致 tepat di tengah。"),
            ("いま起きたばかりでまだ頭がぼーっとしている。", "Baru saja bangun tidur, kepala masih terasa berat.", "バル サジャ バングン ティドゥール、クラパ マシ トゥラサ ブラット", "起床直後 baru saja bangun。"),
            ("この服、値段もデザインもちょうど求めていたものだ。", "Baju ini pas sekali dengan selera dan anggaran saya.", "バジュ イニ パス スカリ ドゥンガン スレラ ダン アンガラン サヤ", "好みに合致 pas sekali。"),
            ("先ほど社長がオフィスを出られたところです。", "Direktur baru saja meninggalkan kantor.", "ディレクトゥル バル サジャ メニンガルカン カントール", "直前退出 baru saja。")
        ],
        "quiz": [
            ("「今しがたオフィスに着いたばかりです」の適切な表現は？", ["baru saja sampai", "tepat waktu sampai", "pas jam sampai", "mungkin sampai"], 1),
            ("「お釣りのないピッタリの金額」を意味する表現は？", ["uang pas", "uang baru", "uang tepat", "uang cocok"], 1),
            ("「定刻通りに」を表す正しいコロケーションは？", ["tepat waktu", "baru waktu", "pas sampai", "tepat saja"], 1)
        ]
    },
    {
        "slug": "39-harus-wajib-mesti-perlu",
        "title": "【誤用克服】「〜しなければならない」の harus, wajib, mesti, perlu の強制力比較",
        "intro": "日本語の「〜しなければならない」「必要だ」には様々な段階があります。法律上の法的義務（wajib）、状況的な必然・義務（harus/mesti）、必要性や推奨（perlu）を正しく使い分けないと、ただの提案が威圧的な命令になったり、法的義務が軽視されたりします。",
        "cases": [
            ("入国時に「ビザを取得しなければならない（法的義務）」と説明する時。", "Anda perlu membuat visa.", "Anda wajib memiliki visa untuk masuk.", "法律、公の規則、宗教上の厳格な義務には wajib（義務的・必須）を用います。perlu（〜する必要がある）だと「取ったほうが便利」程度の任意性に聞こえてしまい危険です。"),
            ("「野菜をもっと食べるべきですよ（健康上の助言）」と同僚に言う時。", "Kamu wajib makan sayur banyak-banyak.", "Kamu harus / perlu makan lebih banyak sayur.", "日常の個人的な助言や健康上の推奨に wajib を使うと「国家の命令」のように過剰に重くなります。親しいアドバイスには harus（〜すべき）や perlu（〜したほうがいい）を用います。")
        ],
        "drill": [
            ("すべての国民は税金を納める義務がある（法的義務）。", "Semua warga negara wajib membayar pajak.", "スムア ワルガ ヌガラ ワジッブ ムンバヤル パジャッ", "法的義務 wajib。"),
            ("私たちは今すぐ出発しなければならない（必然・急務）。", "Kita harus berangkat sekarang juga.", "キタ ハルス ブランカット スカラン ジュガ", "必須 harus。"),
            ("この書類はサインする前に確認する必要があります（必要性）。", "Dokumen ini perlu diperiksa sebelum ditandatangani.", "ドクメン イニ プルル ディプ リクサ スブルム ディタンダタンガニ", "必要性 perlu。"),
            ("バイクに乗る時はヘルメットの着用が義務付けられている。", "Pengendara motor wajib memakai helm standar.", "プンゲンダラ モトール ワジッブ ムマカイ ヘルム スタンダール", "着用義務 wajib memakai helm。"),
            ("そんなに心配する必要はありませんよ（不要）。", "Tidak perlu khawatir sampai seperti itu.", "ティダッ プルル クワティル サンパイ スペルティ イトゥ", "不要 tidak perlu。"),
            ("明日の朝一番でレポートを提出しなければならない。", "Mesti mengumpulkan laporan besok pagi-pagi.", "メスティ ムングンプルカン ラポラン ブソッ パギパギ", "義務 mesti。"),
            ("この薬は食後に服用しなければなりません（指示）。", "Obat ini harus diminum setelah makan.", "オバット イニ ハルス ディミヌム ストゥラ マカン", "服用指示 harus diminum。"),
            ("イスラム教徒は断食月に断食を行う義務がある（宗教義務）。", "Umat Muslim wajib berpuasa di bulan Ramadan.", "ウマット ムスリム ワジッブ ブルプアサ ディ ブラン ラマダン", "宗教義務 wajib berpuasa。"),
            ("この件についてはもう一度話し合う必要がある。", "Kita perlu mendiskusikan hal ini sekali lagi.", "キタ プルル ムンディスクスィカン ハル イニ スカリ ラギ", "話し合いの必要性 perlu mendiskusikan。"),
            ("失敗から学ばなければならない（教訓）。", "Kita harus belajar dari kesalahan masa lalu.", "キタ ハルス ブラジャル ダリ クサラハン マサ ラル", "教訓 harus belajar。"),
            ("入室前に靴を脱ぐ義務がある（ルール）。", "Wajib melepas sepatu sebelum masuk ke ruangan.", "ワジッブ ムレパス スパトゥ スブルム マスッ ク ルアンガン", "規則 wajib melepas。"),
            ("急ぐ必要はない、時間はたっぷりある（不要）。", "Tidak usah / tidak perlu buru-buru, waktu masih banyak.", "ティダッ ウサ / ティダッ プルル ブルブル、ワクトゥ マシ バニャッ", "急ぐ必要なし tidak perlu。"),
            ("成功するためには一生懸命努力しなければならない。", "Harus berusaha keras untuk mencapai kesuksesan.", "ハルス ブルウサハ クラス ウントゥッ ムンチャパイ クスクセサン", "努力の義務 harus berusaha。"),
            ("このソフトウェアはアップデートが必要だ。", "Perangkat lunak ini perlu diperbarui segera.", "プランカット ルナッ イニ プルル ディプルバルイ スグラ", "更新必要 perlu diperbarui。"),
            ("約束は守らなければならない（道徳）。", "Janji mesti ditepati dengan penuh tanggung jawab.", "ジャンジ メスティ ディトゥパティ ドゥンガン プヌ タングン ジャワブ", "約束厳守 mesti ditepati。")
        ],
        "quiz": [
            ("「国民の納税義務」のように法的に強制される義務を表す語は？", ["wajib", "perlu", "boleh", "bisa"], 1),
            ("「心配する必要はない（心配無用）」を表すフレーズは？", ["Tidak perlu khawatir", "Wajib tidak khawatir", "Harus jangan khawatir", "Mesti khawatir"], 1),
            ("日常会話で「〜しなければならない」を表す最も一般的で汎用的な助動詞は？", ["harus", "wajib", "sah", "izin"], 1)
        ]
    },
    {
        "slug": "40-boleh-bisa-permission-ability",
        "title": "【誤用克服】「〜してもよい」の boleh（許可）と bisa（能力・可能）の混同矯正",
        "intro": "日本語の「〜できる」「〜していい」を英語の can に引きずられて何でも bisa と訳していませんか？bisa は能力や物理的可能（able to）を表し、対人関係での「許可（may/allowed to）」を求める際は boleh を用いるのが鉄則です。",
        "cases": [
            ("他人の部屋に入る時に「入ってもいいですか？（許可）」と尋ねる時。", "Bisa saya masuk?", "Boleh saya masuk?", "許可を求める時は必ず boleh（〜してもよい）を使います。Bisa saya masuk? と言うと「私の身体はドアの隙間を通ることができますか？（物理的可能性）」という奇妙なニュアンスになります。"),
            ("「私はインドネシア語が話せます（語学能力）」と言う時。", "Saya boleh bicara bahasa Indonesia.", "Saya bisa bicara bahasa Indonesia.", "個人の後天的スキルや能力には必ず bisa を使います。boleh を使うと「私はインドネシア語を話す許可を当局から与えられています」という意味になってしまいます。")
        ],
        "drill": [
            ("ここに入ってもよろしいですか？（許可）", "Boleh saya masuk ke sini?", "ボレ サヤ マスッ ク シニ", "許可尋ね Boleh saya...。"),
            ("私はピアノを弾くことができます（能力）。", "Saya bisa bermain piano.", "サヤ ビサ ブルマイン ピアノ", "能力 bisa。"),
            ("写真を撮ってもいいですか？（撮影許可）", "Boleh saya mengambil foto di sini?", "ボレ サヤ ムンガンビル フォト ディ シニ", "撮影許可 Boleh...。"),
            ("彼は英語とインドネシア語が流暢に話せます（語学能力）。", "Dia bisa berbahasa Inggris dan Indonesia dengan lancar.", "ディア ビサ ブルバハサ イングリス ダン インドネシア ドゥンガン ランチャール", "語学能力 bisa。"),
            ("一口味見してもいい？（友人への軽い許可）", "Boleh coba sedikit makanannya?", "ボレ チョバ スディキット マカナンニャ", "味見許可 Boleh coba...。"),
            ("今夜、私の家に泊まることができるよ（状況可能）。", "Kamu bisa menginap di rumah saya malam ini.", "カム ビサ ムンギナップ ディ ルマ サヤ マラム イニ", "状況可能 bisa。"),
            ("子供はここで遊んではいけません（禁止）。", "Anak-anak tidak boleh bermain di area ini.", "アナッアナッ ティダッ ボレ ブルマイン ディ エリア イニ", "禁止 tidak boleh。"),
            ("このパソコンを借りてもいいですか？（借用許可）", "Bolehkah saya meminjam laptop ini?", "ボレカ サヤ ムミンジャム ラップトップ イニ", "丁寧な許可 Bolehkah...。"),
            ("怪我をして歩くことができない（身体的不能）。", "Kakinya cedera sehingga tidak bisa berjalan.", "カキニャ チェデラ スヒンガ ティダッ ビサ ブルジャラン", "不能 tidak bisa。"),
            ("会議で発言してもよろしいでしょうか？（発言許可）", "Bolehkah saya menyampaikan pendapat?", "ボレカ サヤ ムニャンパイカン プンダパット", "発言許可 Bolehkah menyampaikan...。"),
            ("彼は辛い食べ物をたくさん食べることができる（耐性）。", "Dia bisa makan makanan yang sangat pedas.", "ディア ビサ マカン マカナン ヤン サンガット プダス", "可能 bisa makan。"),
            ("ここでタバコを吸ってはいけません（禁煙）。", "Dilarang merokok, tidak boleh merokok di sini.", "ディララン ムロコッ、ティダッ ボレ ムロコッ ディ シニ", "禁止 tidak boleh。"),
            ("明日のスケジュールを変更できますか？（状況可能の打診）", "Apakah bisa mengubah jadwal pertemuan besok?", "アパカ ビサ ムングバ ジャドワル プルトゥムアン ブソッ", "状況可能の打診 Apakah bisa...。"),
            ("電話番号を教えてもらってもいいですか？（丁寧な依頼）", "Boleh minta nomor teleponnya?", "ボレ ミンタ ノモール テレポンニャ", "連絡先許可 Boleh minta...。"),
            ("努力すれば誰でも夢を叶えることができる。", "Siapa pun bisa meraih impian jika berusaha.", "シアパ プン ビサ ムライ インピアン ジカ ブルウサハ", "一般的可能 bisa。")
        ],
        "quiz": [
            ("美術館で「写真を撮ってもいいですか（許可）？」と尋ねる語は？", ["Boleh", "Bisa", "Harus", "Mesti"], 1),
            ("「私はバイクの運転ができる（技能・能力）」を表す助動詞は？", ["bisa", "boleh", "wajib", "perlu"], 1),
            ("「ここでは駐車禁止（してはいけない）」を表す表現は？", ["tidak boleh parkir", "tidak bisa parkir", "belum parkir", "kurang parkir"], 1)
        ]
    }
]

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
    lines.append("母語（日本語）の思考フレームを解体し、インドネシア語の語彙の守備範囲・対人関係のレジスターに即した自然な表現パターンを身体化します。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 矯正リライトドリル（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語の文を見て、直訳の罠を避けて**自然なインドネシア語**を1〜2秒以内に口頭で発声してください。\n")
    
    for idx, (jp, id_sent, kana, exp) in enumerate(a['drill'], 1):
        lines.append(f"### 第{idx}問: 「**{jp}**」\n")
        lines.append('<div class="id-example">')
        lines.append(f'<div class="id-sentence"><strong>{id_sent}</strong></div>')
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

print("Batch 1081-1090 generated successfully.")
