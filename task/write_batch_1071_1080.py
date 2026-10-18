# -*- coding: utf-8 -*-
import os

articles_data = [
    {
        "slug": "21-minta-tolong-bantu-levels",
        "title": "【誤用克服】お願い表現 minta tolong, tolong, bantu, mohon の丁寧度ミスマッチ防止",
        "intro": "日本語の「〜してください」「手伝ってください」を機械的に訳すと、同僚に堅苦しすぎる mohon を使って距離を作ってしまったり、逆に目上に不躾な命令口調になってしまうことがあります。相手との社会的距離や緊急度に応じた使い分けを徹底解説します。",
        "cases": [
            ("同僚に「ちょっと手伝って」と頼む時。", "Saya mohon Anda membantu saya.", "Bisa minta tolong sebentar?", "日常会話や親しい同僚に mohon（公式・書面での嘆願・申請）を使うと極めて重苦しく不自然です。口語の頼み事では minta tolong（助けを求める）や Bisa tolong... が最も自然です。"),
            ("上司や顧客に「ご確認のほどお願いいたします」と依頼する時。", "Tolong periksa ini ya.", "Mohon bantuannya untuk memeriksa dokumen ini.", "親しい命令や軽い依頼を表す Tolong ... ya は目上や公式ビジネスでは砕けすぎています。文書や公式の場では Mohon kesediaan Bapak... や Mohon bantuannya を用います。")
        ],
        "drill": [
            ("ちょっと手伝ってもらえますか？（同僚への軽い依頼）", "Bisa minta tolong sebentar?", "ビサ ミンタ トロン スブンタル", "同僚への依頼 Bisa minta tolong...。"),
            ("塩を取ってください（食卓での依頼）。", "Tolong ambilkan garam ya.", "トロン アンビルカン ガラム ヤ", "日常動作の依頼 Tolong + 動詞-kan。"),
            ("添付資料をご確認いただけますと幸いです（公式ビジネス）。", "Mohon periksa dokumen terlampir.", "モホン プ リクサ ドクメン トゥルランプィル", "ビジネス文書 Mohon + 動詞。"),
            ("この箱を運ぶのを手伝ってくれませんか？", "Bisa bantu saya angkat kardus ini?", "ビサ バントゥ サヤ アンカット カルドゥス イニ", "手助け Bisa bantu...。"),
            ("ご静粛にお願い申し上げます（アナウンス）。", "Mohon perhatian dan tetap tenang.", "モホン プルハティアン ダン トゥタップ トゥナン", "公のアナウンス Mohon...。"),
            ("ペンを貸していただけますか？", "Boleh pinjam pulpennya sebentar?", "ボレ ピンジャム プルペンニャ スブンタル", "許可・借用 Boleh pinjam...。"),
            ("駅まで車で送ってもらえない？（友人へ）", "Bisa tolong antar saya ke stasiun?", "ビサ トロン アンタル サヤ ク スタシウン", "友人への送迎依頼 Bisa tolong antar...。"),
            ("お手数をおかけして申し訳ありません（クッション言葉）。", "Maaf merepotkan, bisa tolong jelaskan lagi?", "マアフ ムレポットカン、ビサ トロン ジュラスカン ラギ", "配慮表現 Maaf merepotkan。"),
            ("こちらにお名前をご記入ください（窓口・受付）。", "Silakan isi nama Anda di sini.", "シラカン イシ ナマ アンダ ディ シニ", "丁寧な案内・推奨 Silakan...。"),
            ("お時間を少しいただけないでしょうか？（上司へ）", "Bolehkah saya minta waktunya sebentar, Pak?", "ボレカ サヤ ミンタ ワクトゥニャ スブンタル、パッ", "目上への時間依頼 Bolehkah saya minta waktunya...。"),
            ("少々お待ちいただけますようお願いいたします。", "Mohon tunggu sebentar ya, Pak.", "モホン トゥング スブンタル ヤ、パッ", "丁寧な待機依頼 Mohon tunggu sebentar。"),
            ("窓を閉めてくれる？風が強いから。", "Tolong tutup jendelanya dong, angin kencang.", "トロン トゥトゥップ ジュンデラニャ ドン、アンギン クンチャン", "口語の親しい依頼 dong。"),
            ("こちらの利用規約を遵守願います（規約）。", "Dimohon untuk mematuhi aturan ini.", "ディモホン ウントゥッ メマトゥヒ アトゥラン イニ", "受動態での強い要請 Dimohon untuk...。"),
            ("会議室を予約しておいてもらえる？", "Bisa tolong pesankan ruang rapat?", "ビサ トロン プサンカン ルアン ラパット", "予約依頼 pesankan。"),
            ("何か手伝いましょうか？（申し出）", "Ada yang bisa saya bantu?", "アダ ヤン ビサ サヤ バントゥ", "手助けの申し出 Ada yang bisa saya bantu?")
        ],
        "quiz": [
            ("同僚に「ちょっと手伝ってくれる？」と気軽に頼む最も自然な表現は？", ["Bisa minta tolong sebentar?", "Saya mohon bantuan Anda.", "Harap bantu saya sekarang.", "Tolong bantu saya segera."], 1),
            ("ビジネスメールで「添付をご確認ください」と丁寧に書く定型句は？", ["Mohon periksa lampiran ini.", "Tolong periksa lampiran dong.", "Minta tolong periksa berkas.", "Bantu periksa ini ya."], 1),
            ("目上の人に「お時間よろしいでしょうか」と伺う表現は？", ["Bolehkah saya minta waktunya sebentar?", "Saya mau waktu Anda.", "Harus bicara sekarang ya.", "Tolong bicara sama saya."], 1)
        ]
    },
    {
        "slug": "22-pikir-kira-sangka-distinction",
        "title": "【誤用克服】「思う・考える」の pikir, kira, sangka, rasa の致命的なニュアンス差",
        "intro": "日本語の「〜だと思う」「考える」をすべて pikir で済ませていませんか？インドネシア語では、論理的に思考する（pikir）、不確実な推測・思い込み（kira）、予期していなかった思い違い（sangka）、主観的な感覚・所感（rasa/merasa）が明確に区別されます。",
        "cases": [
            ("「明日は雨が降ると思うよ（推測）」と私見を述べる時。", "Saya pikir besok akan hujan.", "Saya rasa besok akan hujan. / Kayaknya besok hujan.", "客観的な推論や思索には pikir を使いますが、個人的な予感や天気の推測には rasa（感覚）や口語の kayaknya（〜みたい）を使うのが極めて自然です。"),
            ("「君が怒っているのかと思った（思い違い・早合点）」と言う時。", "Saya pikir kamu marah.", "Saya kira / sangka kamu marah tadi.", "実際は違っていた推測や「〜かと勘違いしていた」という過去の思い込みには kira や sangka を用います（Saya kira bukan begitu = そうじゃないと思ってた）。")
        ],
        "drill": [
            ("私の感覚では、この計画は少し危険だと思います。", "Menurut rasa saya, rencana ini agak berisiko.", "ムヌルット ラサ サヤ、レンチャナ イニ アガッ ブルリスィコ", "主観的所感 rasa。"),
            ("決断する前によく考えなさい（論理的熟考）。", "Pikirkan baik-baik sebelum mengambil keputusan.", "ピキルカン バイッバイッ スブルム メンガンビル クプトゥサン", "熟考 pikirkan。"),
            ("彼が来ないのかと思ったよ（思い違い）。", "Saya kira dia tidak datang.", "サヤ キラ ディア ティダッ ダタン", "早合点・思い込み kira。"),
            ("まさか君が犯人だとは思わなかった！（予期せぬ疑念）", "Tidak saya sangka kamu pelakunya!", "ティダッ サヤ サンカ カム プラクニャ", "予期せぬ思い sangka。"),
            ("どう思う？（意見を求める）", "Bagaimana menurutmu? / Bagaimana pendapatmu?", "バガイマナ ムヌルットム / バガイマナ プンダパットム", "意見尋ね Menurut...。"),
            ("少し頭が痛い気がする（身体感覚）。", "Saya merasa agak pusing.", "サヤ ムラサ アガッ プシン", "身体的・感情的実感 merasa。"),
            ("深く考えすぎないで、リラックスして。", "Jangan terlalu banyak berpikir, santai saja.", "ジャンガン トゥルラル バニャッ ブルピキル、サンタイ サジャ", "考えすぎ jangan berpikir。"),
            ("彼はもう帰宅したんじゃないかな（推測）。", "Kira-kira dia sudah pulang.", "キラキラ ディア スダ プラン", "およそ・推測 kira-kira。"),
            ("私はこの意見に賛同できないと思います（意見）。", "Saya rasa saya tidak bisa setuju dengan ini.", "サヤ ラサ サヤ ティダッ ビサ ス トゥジュ ドゥンガン イニ", "控えめな所感 saya rasa。"),
            ("誰もそんなこと想像すらしていなかった（想定外）。", "Tidak ada yang menyangka hal itu akan terjadi.", "ティダッ アダ ヤン メニャンカ ハル イトゥ アカン トゥルジャディ", "想定・予期 menyangka。"),
            ("将来について真剣に考えなければならない。", "Harus berpikir serius tentang masa depan.", "ハルス ブルピキル セリウス トンタン マサ ドゥパン", "真剣な思考 berpikir serius。"),
            ("彼は怒っているように感じる（空気感）。", "Rasanya dia sedang kesal.", "ラサニャ ディア スダン クサル", "状況の感覚 rasanya。"),
            ("君の言いたいことはよく考えて理解した。", "Saya sudah memikirkan apa yang kamu katakan.", "サヤ スダ メミキルカン アパ ヤン カム カタカン", "検討・吟味 memikirkan。"),
            ("私が見たところ、この数字はおかしい。", "Sepemikiran saya bukan begitu, angka ini aneh.", "スプミキラン サヤ ブカン ブギトゥ、アンカ イニ アネ", "見解・思考。"),
            ("彼らが合格するとは思わなかった（驚き）。", "Tidak kusangka mereka bisa lulus ujian.", "ティダッ クサンカ ムレカ ビサ ルルス ウジアン", "想定外の驚き tidak kusangka。")
        ],
        "quiz": [
            ("「実際は違ったが〜だと思い込んでいた」を表す最も適切な動詞は？", ["kira / sangka", "pikir", "tahu", "kenal"], 1),
            ("「私の個人的な感覚・所感では」と柔らかく意見を切り出す表現は？", ["Saya rasa...", "Saya berpikir keras...", "Sangka saya...", "Harus saya pikir..."], 1),
            ("「よく考えてから行動しなさい」の動詞は？", ["Pikirkan baik-baik", "Kira-kira saja", "Sangkakan dulu", "Rasakan semuanya"], 1)
        ]
    },
    {
        "slug": "23-kenal-tahu-paham-boundaries",
        "title": "【誤用克服】「知っている」の対象別使い分け（人物 kenal vs 事実 tahu vs 概念 paham）",
        "intro": "日本語の「知っている」は多義的ですが、インドネシア語では目的語の性質によって厳格に単語が分かれます。人を目的語にして tahu を使うと「面識がない（名前や存在を知っているだけ）」になり、失礼になることもあります。3つの境界線を明快に整理します。",
        "cases": [
            ("「山田さんを知っていますか？（面識の有無）」と尋ねる時。", "Apakah Anda tahu Pak Yamada?", "Apakah Anda kenal dengan Pak Yamada?", "人との面識・知り合い関係を尋ねる時は必ず kenal を使います。tahu を使うと「山田という名前の人物が存在することを知っているか」という情報認識の意味になります。"),
            ("「そのニュースの内容をよく理解しています」と言う時。", "Saya tahu sekali berita itu.", "Saya paham betul isi berita itu.", "単に情報として耳に入った（tahu）のではなく、背景や本質を「深く理解・納得している」状態には paham や mengerti を用います。")
        ],
        "drill": [
            ("彼とは大学時代からの知り合いです（面識）。", "Saya kenal dia sejak zaman kuliah.", "サヤ クナル ディア スジャッ ザマン クリア", "面識・友人関係 kenal。"),
            ("明日の会議の時間を知っていますか？（情報・事実）", "Kamu tahu jam berapa rapat besok?", "カム タフ ジャム ブラパ ラパット ブソッ", "事実・情報 tahu。"),
            ("文法のルールをしっかり理解しました（理解）。", "Saya sudah paham aturan tata bahasanya.", "サヤ スダ パハム アトゥラン タタ バハサニャ", "理解・納得 paham。"),
            ("社長の顔は知っているが、直接の面識はない。", "Tahu wajah direktur, tapi tidak kenal pribadi.", "タフ ワジャ ディレクトゥル、タピ ティダッ クナル プリバディ", "情報 tahu vs 面識 kenal。"),
            ("お互いによく知り合っている仲です。", "Kami sudah saling mengenal dengan baik.", "カミ スダ サリン ムンゲナル ドゥンガン バイッ", "相互の知り合い saling mengenal。"),
            ("答えを知っている人は手を挙げてください。", "Yang tahu jawabannya silakan angkat tangan.", "ヤン タフ ジャワバンニャ シラカン アンカット タンガン", "知識・情報 tahu。"),
            ("彼女の気持ちが痛いほどよく分かる（共感・理解）。", "Saya sangat paham perasaan dia.", "サヤ サンガット パハム プラサアン ディア", "心情の理解 paham。"),
            ("初対面ですが、お名前は伺っております。", "Baru pertama kenal, tapi sudah tahu nama Bapak.", "バル プルタマ クナル、タピ スダ タフ ナマ バパッ", "初対面 kenal / 情報 tahu。"),
            ("この単語の意味が分からない（意味把握）。", "Saya tidak mengerti arti kata ini.", "サヤ ティダッ ムンゲルティ アルティ カタ イニ", "語義の理解 mengerti。"),
            ("インドネシアの文化について深く理解したい。", "Ingin memahami budaya Indonesia lebih dalam.", "インギン メマハミ ブダヤ インドネシア レビ ダラム", "深い理解 memahami。"),
            ("この機械の操作方法を知っていますか？", "Apakah tahu cara mengoperasikan mesin ini?", "アパカ タフ チャラ メンオペラシカン メシン イニ", "操作手順 tahu cara...。"),
            ("彼は地元で顔が広い（有名・多くの人が知っている）。", "Dia banyak kenal orang di kampungnya.", "ディア バニャッ クナル オラン ディ カンプンニャ", "顔が広い banyak kenal orang。"),
            ("私にはその事情は知る由もありません（無知）。", "Saya sama sekali tidak tahu urusan itu.", "サヤ サマ スカリ ティダッ タフ ウルサン イトゥ", "全く知らない tidak tahu。"),
            ("先生の意図が十分に理解できました。", "Saya sudah mengerti betul maksud guru.", "サヤ スダ ムンゲルティ ベトゥル マクスッド グル", "意図の理解 mengerti maksud。"),
            ("自己紹介をしてお互いを知り合いましょう。", "Mari berkenalan agar saling mengenal.", "マリ ブルクナラン アガル サリン ムンゲナル", "知り合いになる berkenalan。")
        ],
        "quiz": [
            ("「あの人とは個人的に親しい知り合いだ」を表す単語は？", ["kenal", "tahu", "paham", "mengerti"], 1),
            ("「電車の出発時刻を知っている」を表す単語は？", ["tahu", "kenal", "paham", "maklum"], 1),
            ("複雑な契約内容を「深く理解・把握した」時に最も適切な動詞は？", ["memahami / mengerti", "mengenal", "mengetahui orang", "berkenalan"], 1)
        ]
    },
    {
        "slug": "24-tinggal-hidup-stay-reside",
        "title": "【誤用克服】「住む」の tinggal と hidup（生存・生活）の混同矯正",
        "intro": "日本語の「住む」「生活する」を機械翻訳して、居住地を言うのに hidup di Jakarta と言っていませんか？hidup は「生物学的な生存」や「人生を送る」という意味が強く、住所・住まいを述べる際は tinggal を使います。それぞれの守備範囲を整理します。",
        "cases": [
            ("「私は南ジャカルタに住んでいます」と居住地を述べる時。", "Saya hidup di Jakarta Selatan.", "Saya tinggal di Jakarta Selatan.", "特定の地域や住居に「住所を構えて居住する」のは tinggal です。hidup di... を日常会話で使うと「南ジャカルタで辛うじて生き延びている・生計を立てている」という重い意味に聞こえます。"),
            ("「一人暮らしをする（単身生活）」と言う時。", "Saya tinggal sendiri. / hidup mandiri.", "Saya tinggal sendiri di kos.", "住居の形態として「一人で暮らす（同居人がいない）」は tinggal sendiri です。hidup sendiri だと「天涯孤独で生きていく」という人生観のニュアンスを帯びます。")
        ],
        "drill": [
            ("あなたは今どこに住んでいますか？（居住地）", "Di mana Anda tinggal sekarang?", "ディ マナ アンダ ティンガル スカラン", "居住地 tinggal。"),
            ("健康的な生活を送る（人生・生計）。", "Menjalani hidup yang sehat.", "メンジャラニ ヒドゥップ ヤン セハット", "生活・人生 hidup。"),
            ("私はアパートに住んでいます。", "Saya tinggal di apartemen.", "サヤ ティンガル ディ アパルテメン", "住居 tinggal di apartemen。"),
            ("村の生活はとても穏やかです（暮らし）。", "Kehidupan di desa sangat tenang.", "クヒドゥパン ディ デサ サンガット トゥナン", "名詞 生活 kehidupan。"),
            ("日本にどれくらい住んでいましたか？", "Berapa lama Anda tinggal di Jepang?", "ブラパ ラマ アンダ ティンガル ディ ジュパン", "居住期間 tinggal di...。"),
            ("物価が高くて生活が苦しい（生計）。", "Biaya hidup mahal sehingga hidup susah.", "ビアヤ ヒドゥップ マハル スヒンガ ヒドゥップ スサ", "生活費 biaya hidup。"),
            ("両親と同居しています。", "Saya tinggal bersama orang tua.", "サヤ ティンガル ブルサマ オラン トゥア", "同居 tinggal bersama。"),
            ("植物が元気に生長して生きている（生命）。", "Tanamannya masih hidup dan subur.", "タナマンニャ マシ ヒドゥップ ダン スブル", "生命・生存 hidup。"),
            ("海外に住むのは初めての経験です。", "Tinggal di luar negeri adalah pengalaman pertama.", "ティンガル ディ ルアル ヌグリ アダラ プンガラマン プルタマ", "居住 tinggal di luar negeri。"),
            ("彼は厳しい自然の中で生き抜いた（サバイバル）。", "Dia bertahan hidup di alam yang keras.", "ディア ブルタハン ヒドゥップ ディ アラム ヤン クラス", "生存 bertahan hidup。"),
            ("ホテルに滞在する（一時的居住）。", "Saya tinggal di hotel selama tiga hari.", "サヤ ティンガル ディ ホテル スラマ ティガ ハリ", "滞在 menginap / tinggal。"),
            ("幸せな人生を歩みたい（人生）。", "Ingin menjalani hidup yang bahagia.", "インギン メンジャラニ ヒドゥップ ヤン バハギア", "人生 hidup bahagia。"),
            ("新しい家に引っ越して住み始めた。", "Pindah ke rumah baru dan mulai tinggal di sana.", "ピンダ ク ルマ バル ダン ムライ ティンガル ディ サナ", "居住開始 mulai tinggal。"),
            ("電気がついた（生きている・点灯）。", "Lampunya sudah hidup / menyala.", "ランプニャ スダ ヒドゥップ / ムニャラ", "点灯 hidup / menyala。"),
            ("祖母は田舎で一人暮らしをしています。", "Nenek tinggal sendirian di kampung.", "ネネッ ティンガル スンディリアン ディ カンプン", "一人住まい tinggal sendirian。")
        ],
        "quiz": [
            ("「私はバンドンに住んでいます」の正しい表現は？", ["Saya tinggal di Bandung.", "Saya hidup di Bandung.", "Saya tinggal hidup Bandung.", "Saya menghidup di Bandung."], 1),
            ("「毎月の生活費」を意味する複合名詞は？", ["biaya hidup", "biaya tinggal", "harga hidup", "uang tinggal"], 1),
            ("「一人暮らしをする（単身住まい）」は？", ["tinggal sendiri", "hidup mati", "bertinggal jiwa", "kehidupan sendiri"], 1)
        ]
    },
    {
        "slug": "25-kembali-pulang-lagi-clash",
        "title": "【誤用克服】「戻る・帰る・再び」の kembali, pulang, lagi の使い分け",
        "intro": "日本語の「もどる」「かえる」「また」を混同して、外出先からオフィスに戻るのに pulang と言っていませんか？pulang は「本来の根拠地（家・祖国）へ帰る」意味であり、職場に戻る時は kembali を使わなければ「退勤・帰宅」と勘違いされます。",
        "cases": [
            ("ランチを終えて「オフィスに戻ります」と同僚に言う時。", "Saya mau pulang ke kantor sekarang.", "Saya mau kembali ke kantor sekarang.", "pulang は「帰宅する・母国に帰る」という帰巣動詞です。職場・外出先へ「戻る」のは kembali や balik を使います。pulang ke kantor と言うと「会社が我が家」になってしまいます。"),
            ("「もう一度言ってください」と頼む時。", "Tolong kembali katakan.", "Tolong katakan sekali lagi.", "「再び・もう一度（回数の反復）」には lagi を置きます。kembali は「元の状態への復帰」を表すため、発話を繰り返す際は sekali lagi を文末に添えます。")
        ],
        "drill": [
            ("会議が終わったらすぐにオフィスに戻ります。", "Setelah rapat selesai, saya segera kembali ke kantor.", "ストゥラ ラパット スルサイ、サヤ スグラ クンバリ ク カントール", "職場へ戻る kembali ke kantor。"),
            ("今日は疲れたので早く家に帰りたい。", "Hari ini capek, ingin cepat pulang ke rumah.", "ハリ イニ チャペッ、インギン チパット プラン ク ルマ", "帰宅 pulang ke rumah。"),
            ("もう一度説明していただけますか？（反復）", "Bisa tolong jelaskan sekali lagi?", "ビサ トロン ジュラスカン スカリ ラギ", "もう一度 sekali lagi。"),
            ("元通りの正常な状態に戻った（原状復帰）。", "Sudah kembali ke kondisi normal.", "スダ クンバリ ク コンディスィ ノルマル", "原状復帰 kembali ke...。"),
            ("来年、日本へ本帰国します（帰国）。", "Tahun depan saya akan pulang ke Jepang untuk selamanya.", "タフン ドゥパン サヤ アカン プラン ク ジュパン ウントゥッ スラマニャ", "本帰国 pulang ke Jepang。"),
            ("また明日会いましょう！（再会）", "Sampai jumpa lagi besok!", "サンパイ ジュンパ ラギ ブソッ", "また jumpa lagi。"),
            ("借りていた本を図書館に返却した（戻す）。", "Mengembalikan buku pinjaman ke perpustakaan.", "ムンガンバリカン ブク ピンジャマン ク プルプスタカアン", "返却 mengembalikan。"),
            ("彼は席を外していますが、すぐ戻ります。", "Dia sedang keluar, tapi sebentar lagi kembali.", "ディア スダン クルアル、タピ スブンタル ラギ クンバリ", "席に戻る kembali。"),
            ("故郷に帰省する（レバラン帰省）。", "Pulang kampung saat Lebaran.", "プラン カンプン サアット レバラン", "帰省 pulang kampung。"),
            ("お釣りをお受け取りください（お返し）。", "Ini uang kembalian Anda.", "イニ ウアン クンバリアン アンダ", "お釣り uang kembalian。"),
            ("また同じ間違いを繰り返してしまった。", "Membuat kesalahan yang sama lagi.", "ムンブアット クサラハン ヤン サマ ラギ", "反復 lagi。"),
            ("彼はインドネシアへ再び戻ってきた（再入国）。", "Dia kembali lagi ke Indonesia.", "ディア クンバリ ラギ ク インドネシア", "再訪 kembali lagi。"),
            ("定刻通りに退社する（帰る）。", "Pulang kerja tepat waktu.", "プラン クルジャ トゥパット ワクトゥ", "退社 pulang kerja。"),
            ("記憶が徐々に戻ってきた（回復）。", "Ingatannya perlahan-lahan kembali.", "インガタンニャ プルラハンラハン クンバリ", "回復 kembali。"),
            ("どういたしまして（お礼のお返し）。", "Kembali / Sama-sama.", "クンバリ / サマサマ", "返答 Kembali。")
        ],
        "quiz": [
            ("外回り営業から「会社に戻る」時の正しい表現は？", ["kembali ke kantor", "pulang ke kantor", "lagi ke kantor", "sampai ke kantor"], 1),
            ("「もう一杯コーヒーをください」の「もう〜」は？", ["secangkir kopi lagi", "secangkir kopi kembali", "secangkir kopi pulang", "kopi pulang lagi"], 1),
            ("「本を元の棚に戻す（返却する）」の派生動詞は？", ["mengembalikan", "memulangkan", "melagikan", "kembalian"], 1)
        ]
    },
    {
        "slug": "26-antar-jemput-bawa-directions",
        "title": "【誤用克服】「送る・迎えに行く・持っていく」の移動方向のベクトル錯誤",
        "intro": "日本語の「送る」「連れていく」「持ってくる」は方向性（話者基準か相手基準か）によって語彙が厳格に分かれます。メールを「送る（kirim）」と人を空港へ「送る（antar）」の混同や、迎えに行く（jemput）の使い分けを徹底解説します。",
        "cases": [
            ("友人を車で「空港まで送る」と言う時。", "Saya mau kirim teman saya ke bandara.", "Saya mau antar teman saya ke bandara.", "kirim は荷物・手紙・データを「郵送・送信する」動詞です。生身の人間を車やバイクで目的地まで「送り届ける」のは antar を使います。kirim teman だと友人を小包にして送るような珍妙な表現になります。"),
            ("学校へ子供を「迎えに行く」と言う時。", "Saya mau ambil anak saya di sekolah.", "Saya mau jemput anak saya di sekolah.", "物を取りに行くのは ambil ですが、人間を車などで「出迎える・拾い上げる」のは必ず jemput を用います。ambil anak だと誘拐や物の回収のような不自然さが出ます。")
        ],
        "drill": [
            ("明日、空港まで車でお送りします（人を送る）。", "Besok saya antar Anda ke bandara.", "ブソッ サヤ アンタル アンダ ク バンダラ", "人を送る antar。"),
            ("メールで資料を送付しました（送信）。", "Saya sudah mengirim dokumen lewat email.", "サヤ スダ ムンギリム ドクメン ルワット イーメール", "メール送信 mengirim。"),
            ("駅まで迎えに来てくれる？（人を迎える）", "Bisa jemput saya di stasiun?", "ビサ ジュンプット サヤ ディ スタシウン", "出迎え jemput。"),
            ("傘を持っていきなさい、雨が降りそうだから（持参）。", "Bawa payung ya, sepertinya mau hujan.", "バワ パユン ヤ、スペルティニャ マウ フジャン", "持参 bawa。"),
            ("お土産を日本から持ってきました（持参・運搬）。", "Saya membawa oleh-oleh dari Jepang.", "サヤ ムンバワ オレホレ ダリ ジュパン", "持参 membawa。"),
            ("子供を学校まで送っていく毎日の日課。", "Mengantar anak ke sekolah setiap hari.", "ムンガンタル アナッ ク スコラ スティアッ ハリ", "送迎 mengantar。"),
            ("空港で来賓をお出迎えする（公の送迎）。", "Menjemput tamu penting di bandara.", "ムンジュンプット タム プンティン ディ バンダラ", "出迎え menjemput。"),
            ("郵便局から荷物を発送する（郵送）。", "Mengirim paket lewat kantor pos.", "ムンギリム パケット ルワット カントール ポス", "発送 mengirim paket。"),
            ("これ、あっちへ持っていって（移動）。", "Tolong bawa ini ke sana.", "トロン バワ イニ ク サナ", "運搬 bawa ke sana。"),
            ("ホテルまで送迎サービスがありますか？", "Apakah ada layanan antar-jemput ke hotel?", "アパカ アダ ラヤナン アンタル ジュンプット ク ホテル", "送迎 antar-jemput。"),
            ("料理を自宅まで配達してもらう（デリバリー）。", "Makanannya diantar langsung ke rumah.", "マカナンニャ ディアンタル ランスン ク ルマ", "配達 diantar。"),
            ("忘れ物を家に取りに帰る（物を取りに行く）。", "Pulang untuk mengambil barang yang ketinggalan.", "プラン ウントゥッ ムンガンビル バラン ヤン クティンガラン", "物の回収 mengambil。"),
            ("彼女を家まで無事に送り届けた。", "Mengantar dia sampai ke rumah dengan selamat.", "ムンガンタル ディア サンパイ ク ルマ ドゥンガン スラマット", "送り届ける mengantar。"),
            ("駅前で友達を車で拾った（ピックアップ）。", "Menjemput teman di depan stasiun.", "ムンジュンプット トゥマン ディ ドゥパン スタシウン", "ピックアップ menjemput。"),
            ("メッセージを送信する（チャット）。", "Kirim pesan lewat WhatsApp.", "キリム プサン ルワット ワッツアップ", "送信 kirim pesan。")
        ],
        "quiz": [
            ("空港へ「客人を車で送り届ける」時に使う動詞は？", ["mengantar", "mengirim", "mengambil", "membawa"], 1),
            ("学校へ「子供を車で迎えに行く」時に使う動詞は？", ["menjemput", "mengambil", "mengantar", "mengirim"], 1),
            ("ホテルや空港の「送迎サービス」を指すインドネシア語は？", ["layanan antar-jemput", "layanan kirim-bawa", "layanan ambil-pulang", "layanan jemput-antar"], 1)
        ]
    },
    {
        "slug": "27-pinjam-sewa-lend-borrow",
        "title": "【誤用克服】貸し借りの pinjam（無償借用）と sewa（賃貸・有料）、meminjamkan（貸す）の混乱解消",
        "intro": "日本語の「借りる」「貸す」は無料か有料かを曖昧にしがちですが、インドネシア語では「無償で一時的に借りる（pinjam）」と「代金を支払って賃貸する（sewa）」が明確に峻別されます。さらに「貸す（meminjamkan）」の接辞ミスも頻発します。",
        "cases": [
            ("旅行先で「レンタカーを借りる」と言う時。", "Saya mau pinjam mobil untuk jalan-jalan.", "Saya mau sewa mobil untuk jalan-jalan.", "有料のレンタル・賃貸には必ず sewa を使います。pinjam mobil と言うと「友人の自家用車をタダで拝借する」意味になります。"),
            ("同僚に「ペンを貸してあげるよ」と言う時。", "Saya mau pinjam kamu pulpen.", "Saya pinjamkan pulpen untukmu. / Boleh pakai pulpen saya.", "pinjam は「借りる（主語が受け取る）」です。「貸す（主語が与える）」は使役・与益の接辞 -kan を付けて meminjamkan としなければ意味が逆転します。")
        ],
        "drill": [
            ("レンタカーを1日借りたいのですが（有料）。", "Saya ingin menyewa mobil selama satu hari.", "サヤ インギン メニェワ モビル スラマ サトゥ ハリ", "賃貸 menyewa mobil。"),
            ("ペンを忘れたので貸してください（無償）。", "Boleh saya pinjam pulpennya sebentar?", "ボレ サヤ ピンジャム プルペンニャ スブンタル", "無償借用 pinjam pulpen。"),
            ("彼は私にお金を貸してくれた（貸与）。", "Dia meminjamkan uang kepada saya.", "ディア ムミンジャムカン ウアン クパダ サヤ", "貸す meminjamkan。"),
            ("アパートを1年間契約で賃貸する（家賃）。", "Menyewa apartemen untuk kontrak satu tahun.", "メニェワ アパルテメン ウントゥッ コントラッ サトゥ タフン", "賃貸契約 menyewa apartemen。"),
            ("図書館で本を3冊借りた。", "Meminjam tiga buku di perpustakaan.", "ムミンジャム ティガ ブク ディ プルプスタカアン", "図書借用 meminjam buku。"),
            ("傘をお貸ししましょうか？（親切な申し出）", "Mau saya pinjamkan payung?", "マウ サヤ ピンジャムカン パユン", "貸出の申し出 pinjamkan。"),
            ("バイクのレンタル料金はいくらですか？", "Berapa biaya sewa motor per hari?", "ブラパ ビアヤ セワ モトール プル ハリ", "レンタル料 biaya sewa。"),
            ("銀行から事業資金を融資してもらう（借金）。", "Meminjam uang modal dari bank.", "ムミンジャム ウアン モダル ダリ バンク", "借金 meminjam uang。"),
            ("この部屋は貸し出し中ですか？（賃貸物件）", "Apakah ruangan ini disewakan?", "アパカ ルアンガン イニ ディセワカン", "貸出物件 disewakan。"),
            ("友達からノートを借りてコピーした。", "Meminjam catatan dari teman lalu difotokopi.", "ムミンジャム チャタタン ダリ トゥマン ラル ディフォトコピ", "拝借 meminjam。"),
            ("貸事務所を探しています（オフィス賃貸）。", "Sedang mencari kantor sewaan.", "スダン マンチャリ カントール セワアン", "賃貸オフィス kantor sewaan。"),
            ("借りたものは期限内に返さなければならない。", "Barang yang dipinjam harus dikembalikan tepat waktu.", "バラン ヤン ディピンジャム ハルス ディクンバリカン トゥパット ワクトゥ", "借用物 barang pinjaman。"),
            ("衣装をパーティーのためにレンタルした。", "Menyewa kostum untuk pesta.", "メニェワ コストゥム ウントゥッ ペスタ", "衣装レンタル menyewa kostum。"),
            ("誰にもお金を貸したくない。", "Saya tidak mau meminjamkan uang kepada siapa pun.", "サヤ ティダッ マウ ムミンジャムカン ウアン クパダ シアパ プン", "貸出拒否 meminjamkan uang。"),
            ("大家さんに今月の家賃を支払った。", "Membayar uang sewa bulan ini kepada pemilik rumah.", "ムンバヤル ウアン セワ ブラン イニ クパダ プミリッ ルマ", "家賃 uang sewa。")
        ],
        "quiz": [
            ("レンタカー屋で「車を借りたい」と言う時の動詞は？", ["sewa", "pinjam", "beri", "ambil"], 1),
            ("「本を友達に貸してあげる」の動詞は？", ["meminjamkan", "meminjam", "menyewakan", "meminjami"], 1),
            ("不動産広告で「貸家・貸部屋」と書く時の単語は？", ["Disewakan", "Dipinjamkan", "Dibelikan", "Dibawakan"], 1)
        ]
    },
    {
        "slug": "28-oleh-oleh-hadiah-gift",
        "title": "【誤用克服】「お土産」の oleh-oleh と「プレゼント」の hadiah の混同是正",
        "intro": "日本語では旅行土産も誕生日プレゼントも「おみやげ・贈り物」とひとくくりにしがちですが、インドネシア語では明確に分類されます。旅先から買ってくる名産品は oleh-oleh、記念日・祝い事・賞品として贈る物は hadiah または kado を用います。",
        "cases": [
            ("友人の誕生日パーティーに「プレゼント」を持参する時。", "Saya bawa oleh-oleh untuk ulang tahunmu.", "Saya bawa kado / hadiah untuk ulang tahunmu.", "誕生日・結婚祝いなどの慶事のプレゼントには kado（誕生日等の個人的ギフト）や hadiah（一般的な贈り物・賞品）を使います。oleh-oleh は旅行・帰省先からの「旅のお土産」に限定されます。"),
            ("バリ島旅行から帰ってきて職場で配るお菓子を渡す時。", "Ini hadiah dari Bali untuk teman-teman.", "Ini oleh-oleh dari Bali untuk teman-teman.", "旅先の名物菓子などを配る際は必ず oleh-oleh を使います。hadiah と言うと、何か特別な功績や表彰の賞品を授与するかのようなニュアンスになってしまいます。")
        ],
        "drill": [
            ("バリ島旅行のお土産にクッキーを買いました。", "Membeli kue untuk oleh-oleh dari Bali.", "ムンブリ クエ ウントゥッ オレホレ ダリ バリ", "旅行土産 oleh-oleh。"),
            ("子供の誕生日に自転車をプレゼントした（贈り物）。", "Memberi hadiah sepeda untuk ulang tahun anak.", "ムンブリ ハディア スペダ ウントゥッ ウラン タフン アナッ", "誕生日ギフト hadiah / kado。"),
            ("大会で優勝して豪華な賞品をもらった（賞品）。", "Menang lomba dan mendapat hadiah menarik.", "ムナン ロンバ ダン ムンダパット ハディア ムナリッ", "賞品 hadiah。"),
            ("日本への帰国土産としてバティックを選んだ。", "Memilih batik sebagai oleh-oleh untuk dibawa pulang ke Jepang.", "ムミリッ バティッ スバガイ オレホレ ウントゥッ ディバワ プラン ク ジュパン", "帰国土産 oleh-oleh。"),
            ("クリスマスプレゼントを包装してもらう。", "Minta membungkuskan kado Natal.", "ミンタ ムンブンクスカン カド ナタル", "クリスマスギフト kado。"),
            ("これ、同僚へのちょっとしたお土産です。", "Ini sedikit oleh-oleh untuk rekan kerja.", "イニ スディキット オレホレ ウントゥッ ルカン クルジャ", "手土産 oleh-oleh。"),
            ("結婚祝いに何を贈ればいいか迷っている。", "Bingung mau kasih hadiah pernikahan apa.", "ビングン マウ カシ ハディア プルニカハン アパ", "結婚祝い hadiah pernikahan。"),
            ("お土産屋街でお菓子をたくさん買い込んだ。", "Membeli banyak makanan di pusat oleh-oleh.", "ムンブリ バニャッ マカナン ディ プサット オレホレ", "お土産店 pusat oleh-oleh。"),
            ("勤続10年の記念品を会社から贈呈された。", "Diberi hadiah kenang-kenangan dari kantor.", "ディブリ ハディア クナンクナンガン ダリ カントール", "記念品 hadiah。"),
            ("故郷から果物のお土産を持ってきました。", "Membawa oleh-oleh buah dari kampung halaman.", "ムンバワ オレホレ ブア ダリ カンプン ハラマン", "里帰り土産 oleh-oleh。"),
            ("抽選でスマートテレビが当たった（景品）。", "Menang undian berhadiah smart TV.", "ムナン ウンディアン ブルハディア スマート ティーヴィー", "景品 berhadiah。"),
            ("プレゼントにリボンをかける。", "Memasang pita pada kotak kado.", "ムマサン ピタ パダ コタッ カド", "ギフト箱 kotak kado。"),
            ("旅行に行くならお土産を忘れないでね！", "Kalau jalan-jalan, jangan lupa oleh-oleh ya!", "カラウ ジャランジャラン、ジャンガン ルパ オレホレ ヤ", "旅行土産 oleh-oleh。"),
            ("母の日に花束をプレゼントした。", "Memberikan hadiah buket bunga pada Hari Ibu.", "ムンブリカン ハディア ブケット ブンガ パダ ハリ イブ", "母の日ギフト hadiah。"),
            ("伝統的な手織り布をお土産としていただいた。", "Menerima kain tenun tradisional untuk oleh-oleh.", "メネリマ カイン トゥヌン トラディシオナル ウントゥッ オレホレ", "手土産 oleh-oleh。")
        ],
        "quiz": [
            ("旅行先で買って職場の同僚に配るお菓子の適切な呼称は？", ["oleh-oleh", "hadiah", "upah", "piala"], 1),
            ("友人の誕生日パーティーに贈るプレゼントの呼称は？", ["kado / hadiah", "oleh-oleh", "kenang-kenangan", "ongkos"], 1),
            ("観光地にある「お土産センター・特産品店」の看板表記は？", ["Pusat Oleh-Oleh", "Pusat Hadiah", "Toko Kado", "Pasar Hadiah"], 1)
        ]
    },
    {
        "slug": "29-kasihan-sayang-pity-regret",
        "title": "【誤用克服】「かわいそう」の kasihan と「もったいない・残念」の sayang の使い分け",
        "intro": "日本語の「かわいそう」「もったいない」「残念だ」の感情は、インドネシア語では kasihan（同情・憐憫・気の毒）と sayang（惜しい・もったいない・愛情）に綺麗に分かれます。食べ残しや機会損失に kasihan を使ってしまう誤用を是正します。",
        "cases": [
            ("食べ物を残している人を見て「もったいないよ！」と言う時。", "Kasihan makanannya!", "Sayang sekali makanannya tidak dihabiskan!", "物・お金・時間・機会が「無駄になる・惜しい」時は sayang です。kasihan は「感情や苦痛を持つ生き物に対する同情」なので、Kasihan makanannya と言うと「食べ物が苦しんでいてかわいそう」という奇妙な擬人化になります。"),
            ("怪我をした野良猫を見て「かわいそうに」と同情する時。", "Sayang sekali kucing itu sakit.", "Kasihan sekali kucing itu terluka.", "生き物が被害に遭って「気の毒だ・哀れだ」と感じる純粋な同情には kasihan を使います。sayang を使うと「その猫が惜しい」という変なニュアンスになります。")
        ],
        "drill": [
            ("まだ食べられるのに捨てるのはもったいない（機会損失）。", "Sayang sekali kalau dibuang padahal masih enak.", "サヤン スカリ カラウ ディブアン パダハル マシ エナッ", "もったいない sayang。"),
            ("大雨でずぶ濡れになって、彼が本当にかわいそう（同情）。", "Kasihan sekali dia kehujanan sampai basah kuyup.", "カスィハン スカリ ディア クフジャナン サンパイ バサ クユップ", "かわいそう kasihan。"),
            ("せっかくのチャンスを逃してしまって本当に残念だ。", "Sayang sekali melewatkan kesempatan emas ini.", "サヤン スカリ ムレワットカン クスンパタン エマス イニ", "残念・惜しい sayang sekali。"),
            ("あの小さな子供は一日中働いていて気の毒だ。", "Kasihan anak kecil itu harus bekerja seharian.", "カスィハン アナッ クチル イトゥ ハルス ブルクルジャ スハリアン", "憐憫 kasihan。"),
            ("時間がもったいないから早く始めよう。", "Sayang waktunya, ayo kita mulai sekarang.", "サヤン ワクトゥニャ、アヨ キタ ムライ スカラン", "時間が惜しい sayang waktunya。"),
            ("捨て犬が震えているのを見てかわいそうに思った。", "Merasa kasihan melihat anjing terlantar itu gemetar.", "ムラサ カスィハン ムリハット アンジン トゥルランタル イトゥ グムタール", "同情を感じる merasa kasihan。"),
            ("せっかく買ったチケットが無駄になって残念だ。", "Sayang tiket yang sudah dibeli jadi hangus.", "サヤン ティケット ヤン スダ ディブリ ジャディ ハングス", "チケット失効 sayang。"),
            ("試験にあと1点で落ちたなんて、本当に惜しい！", "Sayang sekali, cuma kurang satu poin untuk lulus!", "サヤン スカリ、チュマ クラン サトゥ ポイン ウントゥッ ルルス", "惜しい sayang sekali。"),
            ("彼をこれ以上いじめないで、かわいそうでしょ。", "Jangan ganggu dia lagi, kasihan kan.", "ジャンガン ガング ディア ラギ、カスィハン カン", "かわいそう kasihan。"),
            ("高い服なのに汚れてしまってもったいない。", "Sayang baju mahal ini jadi kotor.", "サヤン バジュ マハル イニ ジャディ コトール", "服がもったいない sayang baju。"),
            ("親を亡くした孤児たちに同情を寄せる。", "Menaruh rasa kasihan kepada anak-anak yatim itu.", "ムナルッ ラサ カスィハン クパダ アナッアナッ ヤティム イトゥ", "憐憫 rasa kasihan。"),
            ("天気が悪くて観光できなかったのは残念でしたね。", "Sayang sekali cuaca buruk sehingga tidak bisa jalan-jalan.", "サヤン スカリ チュアチャ ブルッ スヒンガ ティダッ ビサ ジャランジャラン", "残念 sayang sekali。"),
            ("怪我をした小鳥の手当てをしてあげた（憐れみ）。", "Mengobati burung yang terluka karena kasihan.", "メンオバティ ブルン ヤン トゥルルカ カレナ カスィハン", "憐憫から karena kasihan。"),
            ("お金を無駄遣いするのは本当にもったいない。", "Sayang sekali membuang-buang uang seperti itu.", "サヤン スカリ ムンブアンブアン ウアン スペルティ イトゥ", "浪費がもったいない sayang。"),
            ("同情するならお金をくれ（ことわざ的表現）。", "Jangan cuma kasihan, beri bantuan nyata.", "ジャンガン チュマ カスィハン、ブリ バントゥアン ニャタ", "同情 kasihan。")
        ],
        "quiz": [
            ("残したご飯を見て「もったいない！」と言う時の自然な単語は？", ["Sayang", "Kasihan", "Sakit", "Rugi"], 1),
            ("雨の中で震えている子犬を見て「かわいそう！」と言う時の単語は？", ["Kasihan", "Sayang", "Benci", "Hemat"], 1),
            ("「あと一歩で勝てたのに惜しい！」の表現は？", ["Sayang sekali!", "Kasihan sekali!", "Cinta sekali!", "Peduli sekali!"], 1)
        ]
    },
    {
        "slug": "30-capek-lelah-register-choice",
        "title": "【誤用克服】「疲れた」の capek（口語）と lelah（文語・心労）の適切なレジスター選択",
        "intro": "日本語の「疲れた」に対応する語として、インドネシア語には口語の capek と文語・公式表現の lelah があります。日常会話で lelah を使うと詩的・大げさに聞こえ、逆に公の場やビジネススピーチで capek を使うと砕けすぎます。TPOに応じたレジスターを習得します。",
        "cases": [
            ("公式の経営会議やスピーチで「スタッフの労苦をねぎらう」時。", "Terima kasih untuk tim yang sudah capek bekerja.", "Terima kasih kepada seluruh tim yang telah bekerja tanpa lelah.", "公式の場や感謝のスピーチでは文語の lelah（または lelah bekerja, tanpa lelah「疲れを知らずに」）を用います。capek は日常口語（bahasa sehari-hari）の響きが強く、公式スピーチには適しません。"),
            ("友達と買い物を歩き回って「あ〜疲れた、休もう」と言う時。", "Saya lelah sekali, mari kita beristirahat sejenak.", "Aduh capek banget, istirahat yuk.", "友人同士のくだけた会話で Saya lelah sekali... と言うと、まるで人生に絶望して精神的に疲れ果てたドラマの台詞のように響きます。日常の肉体的疲労には capek（口語では capek banget）が最も自然です。")
        ],
        "drill": [
            ("あ〜疲れた！ちょっとカフェで休もう（友人との会話）。", "Aduh capek banget! Istirahat dulu di kafe yuk.", "アドゥ チャペッ バンゲット！ イスティラハット ドゥル ディ カフェ ユッ", "日常の疲れ capek banget。"),
            ("スタッフの皆様の献身的なご尽力に心より感謝申し上げます（公式）。", "Terima kasih atas kerja keras bapak ibu yang tidak kenal lelah.", "トゥリマ カスィ アタス クルジャ クラス バパッ イブ ヤン ティダッ クナル レラ", "不眠不休・不撓不屈 tidak kenal lelah。"),
            ("一日中パソコンに向かっていて目が疲れた。", "Mata capek karena seharian menatap layar komputer.", "マタ チャペッ カレナ スハリアン メナタップ ラヤール コンピューテル", "身体の疲労 mata capek。"),
            ("人生に疲れて少し一人になりたい（精神的疲弊・文語）。", "Merasa lelah jiwa dan ingin menyendiri sejenak.", "ムラサ レラ ジワ ダン インギン メニョンディリ スブンタル", "精神的疲弊 lelah jiwa。"),
            ("残業続きで体が本当にクタクタです（口語）。", "Badan benar-benar capek setelah lembur terus.", "バダン ブナルブナル チャペッ ストゥラ レンブール トゥルス", "口語クタクタ badan capek。"),
            ("長い旅路を終えて心地よい疲労感を覚えた（小説・文語的描写）。", "Merasa lelah namun bahagia setelah perjalanan panjang.", "ムラサ レラ ナムン バハギア ストゥラ プルジャラナン パンジャン", "文語描写 lelah namun bahagia。"),
            ("満員電車で通勤するのは本当に疲れる。", "Capek sekali naik kereta yang penuh sesak setiap hari.", "チャペッ スカリ ナイス クレタ ヤン プヌ ササッ スティアッ ハリ", "口語のうんざり capek sekali。"),
            ("激しい運動の後に心地よい疲労感がある。", "Ada rasa lelah yang nyaman setelah olahraga berat.", "アダ ラサ レラ ヤン ニャマン ストゥラ オラフラガ ブラット", "疲労感 rasa lelah。"),
            ("彼らに同じことを何度も説明するのはもう疲れた（うんざり）。", "Capek menjelaskan hal yang sama berulang kali.", "チャペッ ムンジュラスカン ハル ヤン サマ ブルラン カリ", "うんざり capek menjelaskan。"),
            ("長年の闘病生活で体力が限界に達した（重厚な文脈）。", "Tubuhnya lelah setelah bertahun-tahun berjuang melawan sakit.", "トゥブフニャ レラ ストゥラ ブルタフンタフン ブルジュアン メラワン サキッ", "重厚な疲労 tubuhnya lelah。"),
            ("今日はもう歩けないくらい足が疲れた。", "Kaki saya capek sekali sampai tidak bisa jalan lagi.", "カキ サヤ チャペッ スカリ サンパイ ティダッ ビサ ジャラン ラギ", "足の疲労 kaki capek。"),
            ("疲れた時は無理をせず休むのが一番です（一般的なアドバイス）。", "Saat tubuh merasa lelah, istirahat adalah obat terbaik.", "サアット トゥブ ムラサ レラ、イスティラハット アダラ オバット トゥルバイッ", "身体の疲労 tubuh lelah。"),
            ("息つく暇もなく働いた。", "Bekerja terus tanpa henti sampai kelelahan.", "ブルクルジャ トゥルス タンパ ヘンティ サンパイ クレラハン", "過労・疲弊 kelelahan。"),
            ("渋滞に巻き込まれて運転疲れした。", "Capek menyetir karena terjebak macet parah.", "チャペッ メニョティル カレナ トゥルジュバッ マチェット パラ", "運転疲れ capek menyetir。"),
            ("精神的にも肉体的にも限界だった。", "Lelah fisik dan mental sudah mencapai batas.", "レラ フィスィッ ダン メンタル スダ ムンチャパイ バタス", "心身の疲労 lelah fisik dan mental。")
        ],
        "quiz": [
            ("日常会話で友人に「あー疲れた！」と言う時の最も自然な表現は？", ["Capek banget!", "Lelah jiwa!", "Kelelahan sekali!", "Payah badan!"], 1),
            ("ビジネススピーチで「疲れを知らぬ献身」を讃えるフォーマルな表現は？", ["tanpa kenal lelah", "tanpa capek-capek", "tidak ada capeknya", "capek terus"], 1),
            ("「過労・極度の疲労状態」を表す ke-...-an の名詞は？", ["kelelahan", "kecapekan", "melelahkan", "terlelah"], 1)
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

print("Batch 1071-1080 generated successfully.")
