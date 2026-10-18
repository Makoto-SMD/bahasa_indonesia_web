# -*- coding: utf-8 -*-
import os

articles_data = [
    {
        "slug": "41-mengajak-mengundang-invite",
        "title": "【誤用克服】「誘う」の mengajak（一緒に行動）と mengundang（招待状・公式招致）の混同是正",
        "intro": "日本語の「誘う」「招待する」を区別せずに mengundang を連発していませんか？mengundang は結婚式や公式晩餐会など「招待状を出して公式に招く（invite）」動詞です。同僚を「一緒にランチに行こう」と気軽に誘う行為は必ず mengajak（一緒に〜しようと誘う）を用います。",
        "cases": [
            ("同僚に「今日のお昼、一緒に食べに行かない？」と誘う時。", "Saya mau mengundang kamu makan siang hari ini.", "Saya mau mengajak kamu makan siang hari ini. / Yuk makan siang bareng.", "日常会話で mengundang を使うと「私が主催する公式ランチ会にご招待申し上げます」という極めて大げさでよそよそしい響きになります。一緒に行動することを提案する日常の「誘い」は mengajak です。"),
            ("友人の結婚式に「ご招待を受けました」と言う時。", "Saya diajak ke pernikahan teman.", "Saya diundang ke acara pernikahan teman.", "冠婚葬祭、公式セミナー、パーティーなどの「招待」には mengundang（受動態 diundang）を用います。diajak だと「友人が行くついでにフラッと連れて行かれた」ような非公式な印象を与えます。")
        ],
        "drill": [
            ("彼を映画に誘った（一緒に行動）。", "Saya mengajak dia menonton film bioskop.", "サヤ ムンガジャッ ディア メノントン フィルム ビオスコップ", "一緒に行動を誘う mengajak。"),
            ("結婚披露宴に招待された（公式招待）。", "Diundang ke pesta resepsi pernikahan.", "ディウンダン ク ペスタ レセプスィ プルニカハン", "公式招待 diundang。"),
            ("今週末、ドライブに行かない？（気軽な誘い）", "Mau ajak kamu jalan-jalan akhir pekan ini.", "マウ アジャッ カム ジャランジャラン アキール プカン イニ", "気軽な誘い ajak。"),
            ("セミナーの基調講演者として著名な教授をお招きした。", "Mengundang profesor ternama sebagai pembicara kunci.", "ムングンダン プロフェソル トゥルナマ スバガイ プムビチャラ クンチ", "招致 mengundang。"),
            ("彼は友達を誘ってサッカーの試合を見に行った。", "Dia mengajak teman-temannya nonton pertandingan sepak bola.", "ディア ムンガジャッ トゥマントゥマンニャ ノントン プルタンディンガン スパッ ボラ", "仲間を誘う mengajak。"),
            ("誕生パーティーの招待状を送付した（招待状）。", "Mengirim kartu undangan untuk pesta ulang tahun.", "ムンギリム カルトゥ ウンダンガン ウントゥッ ペスタ ウラン タフン", "招待状 kartu undangan。"),
            ("カフェでお茶でもしようよ（誘い文句）。", "Ajak ngopi santai di kafe yuk.", "アジャッ ンゴピ サンタイ ディ カフェ ユッ", "お茶に誘う ajak ngopi。"),
            ("来賓をVIP席へご案内する（公式）。", "Mengundang tamu kehormatan ke kursi VIP.", "ムングンダン タム クホルマタン ク クルスィ ヴィアイピー", "公式案内 mengundang。"),
            ("先生から研究プロジェクトに誘われた。", "Diajak oleh guru untuk ikut proyek penelitian.", "ディアジャッ オレ グル ウントゥッ イクット プロイェッ プネリティアン", "勧誘 diajak ikut。"),
            ("式典へのご招待をいただき誠にありがとうございます。", "Terima kasih atas undangan untuk menghadiri upacara.", "トゥリマ カスィ アタス ウンダンガン ウントゥッ ムンハディリ ウパチャラ", "名詞 招待 undangan。"),
            ("誰か一緒に旅行へ行く人を誘おう。", "Ayo ajak seseorang untuk jalan-jalan bersama.", "アヨ アジャッ スソオラン ウントゥッ ジャランジャラン ブルサマ", "旅行に誘う ajak jalan-jalan。"),
            ("大使館のレセプションに招待された。", "Diundang ke acara resepsi kedutaan besar.", "ディウンダン ク アチャラ レセプスィ クドゥタアン ブサル", "大使館招待 diundang。"),
            ("彼は妹を誘って買い物に出かけた。", "Dia mengajak adik perempuannya pergi berbelanja.", "ディア ムンガジャッ アディッ プルンプアンニャ プルギ ブルブランジャ", "誘い出す mengajak pergi。"),
            ("国際シンポジウムのスピーカーとして招致する。", "Mengundang pakar internasional untuk simposium.", "ムングンダン パカル インテルナシオナル ウントゥッ シンポスィウム", "招致 mengundang pakar。"),
            ("誘ってくれてありがとう！（お礼）", "Terima kasih sudah mengajak saya!", "トゥリマ カスィ スダ ムンガジャッ サヤ", "誘いへの感謝 mengajak saya。")
        ],
        "quiz": [
            ("同僚を「一緒にコーヒー飲みに行かない？」と誘う時の動詞は？", ["mengajak", "mengundang", "menyuruh", "memerintah"], 1),
            ("結婚式や記念パーティーの「招待状」を表すインドネシア語は？", ["surat undangan", "surat ajakan", "kartu ajak", "tiket undangan"], 1),
            ("「食事に誘ってくれてありがとう」とお礼を言う時の自然な表現は？", ["Terima kasih sudah mengajak saya makan.", "Terima kasih sudah mengundang saya makan.", "Terima kasih menyuruh saya makan.", "Terima kasih memaksa saya makan."], 1)
        ]
    },
    {
        "slug": "42-bicara-ngomong-bilang-berkata",
        "title": "【誤用克服】「話す」の bicara, ngomong, bilang, berkata のレジスターと文法機能",
        "intro": "インドネシア語の「話す・言う」には、能力や会話行為を表す bicara、日常口語の ngomong、引用動詞「〜と言った」の bilang、文学的・格調高い berkata があります。公の場やビジネスで bilang を連発したり、会話で berkata を使って時代劇のようになったりするミスを是正します。",
        "cases": [
            ("会議で「社長は明日発表するとおっしゃいました」と報告する時。", "Direktur bilang besok mau umumkan.", "Direktur menyampaikan / menyatakan bahwa beliau akan mengumumkan besok.", "公式な会議や目上の発言の引用に口語の bilang（言った）を使うと極めて不躾に聞こえます。ビジネスでは menyampaikan（伝える・述べる）や menyatakan（表明する）を用います。"),
            ("「インドネシア語を話すことができます」と語学能力を述べる時。", "Saya bisa ngomong / bilang bahasa Indonesia.", "Saya bisa berbicara bahasa Indonesia.", "言語を話す能力や対話行為には必ず berbicara（口語では bicara）を用います。ngomong だと「おしゃべりできる」、bilang だと「発言できる」という意味になり能力の表現になりません。")
        ],
        "drill": [
            ("私はインドネシア語を上手に話すことができます（語学能力）。", "Saya bisa berbicara bahasa Indonesia dengan baik.", "サヤ ビサ ブルビチャラ バハサ インドネシア ドゥンガン バイッ", "言語能力 berbicara。"),
            ("彼が「もう帰る」と言っていたよ（日常会話の引用）。", "Dia bilang mau pulang duluan tadi.", "ディア ビラン マウ プラン ドゥルアン タディ", "口語引用 bilang。"),
            ("無駄なおしゃべりをやめて仕事に集中しなさい（おしゃべり）。", "Jangan banyak ngomong, fokus saja pada pekerjaan.", "ジャンガン バニャッ ンゴモン、フォクス サジャ パダ プクルジャアン", "おしゃべり jangan ngomong。"),
            ("大統領は平和の重要性を力説した（公式表明）。", "Presiden menyatakan pentingnya perdamaian dunia.", "プレシデン メニャタカン プンティンニャ プルダマイアン ドゥニア", "公式表明 menyatakan。"),
            ("静かにしてください、先生がお話しになります。", "Harap tenang, guru akan berbicara.", "ハラップ トゥナン、グル アカン ブルビチャラ", "発話行為 berbicara。"),
            ("彼は私に真実を言わなかった（告げる）。", "Dia tidak mengatakan yang sebenarnya kepada saya.", "ディア ティダッ ムンガタカン ヤン スブナルニャ クパダ サヤ", "告げる mengatakan。"),
            ("神は「光あれ」と言われた（聖書・文学）。", "Tuhan berkata: Jadilah terang.", "トゥハン ブルカタ: ジャディラ トゥラン", "神・文学 berkata。"),
            ("彼とは電話で直接話しました。", "Saya sudah berbicara langsung dengan dia lewat telepon.", "サヤ スダ ブルビチャラ ランスン ドゥンガン ディア ルワット テレポン", "直接対話 berbicara langsung。"),
            ("何て言ったの？もう一回言って（口語）。", "Tadi ngomong apa? Coba bilang sekali lagi.", "タディ ンゴモン アパ？ チョバ ビラン スカリ ラギ", "口語発話 ngomong / bilang。"),
            ("上司は今回の提案を歓迎すると述べられた（伝達）。", "Atasan menyampaikan bahwa beliau menyambut baik usulan ini.", "アタサン ムニャンパイカン バワ ベリアウ メニャンブット バイッ ウスラン イニ", "公式伝達 menyampaikan。"),
            ("そんな失礼な言い方をしてはいけない。", "Jangan berkata kasar seperti itu kepada orang tua.", "ジャンガン ブルカタ カサル スペルティ イトゥ クパダ オラン トゥア", "言葉遣い berkata kasar。"),
            ("彼女はおしゃべりが大好きでいつも明るい。", "Dia suka sekali ngobrol dan selalu ceria.", "ディア スカ スカリ ンオブロル ダン スラル チュリア", "雑談 ngobrol。"),
            ("はっきりと言いたいことを言いなさい。", "Katakan apa yang ingin kamu sampaikan secara jelas.", "カタカン アパ ヤン インギン カム ムニャンパイカン スチャラ ジュラス", "明言 katakan。"),
            ("正直に言うと、私はあまり自信がありません。", "Sejujurnya saya katakan, saya kurang percaya diri.", "スジュジュルニャ サヤ カタカン、サヤ クラン プルチャヤ ディリ", "率直に言うと katakan。"),
            ("本音を語り合う深い対話を持った。", "Melakukan pembicaraan mendalam dari hati ke hati.", "ムラクカン プムビチャラアン ムンダラム ダリ ハティ ク ハティ", "対話 pembicaraan。")
        ],
        "quiz": [
            ("履歴書や面接で「英語を話すことができます」と書く・言う際の適切な表現は？", ["bisa berbicara bahasa Inggris", "bisa ngomong bahasa Inggris", "bisa bilang bahasa Inggris", "bisa berkata bahasa Inggris"], 1),
            ("友人間で「彼は何て言ってた？」と気軽に尋ねる時の動詞は？", ["Dia bilang apa?", "Dia menyatakan apa?", "Dia berkata apa?", "Dia berpidato apa?"], 1),
            ("ビジネスの公式報告で「クライアントが〜と述べられた」と丁寧に伝える語は？", ["Klien menyampaikan bahwa...", "Klien bilang kalau...", "Klien ngomong bahwa...", "Klien berkata-kata..."], 1)
        ]
    },
    {
        "slug": "43-lupa-ketinggalan-forgot-left",
        "title": "【誤用克服】「忘れる」の lupa（記憶の喪失）と ketinggalan（置き忘れ）の過失責任と表現差",
        "intro": "日本語の「わすれた」には、約束や知識を頭から失念した（forget）と、物理的な持ち物を特定の場所に置き忘れてきた（leave behind）の両方があります。インドネシア語で「傘を電車に忘れた」を lupa payung di kereta と言うと構文が破綻します。",
        "cases": [
            ("「電車の中に傘を置き忘れてしまいました」と言う時。", "Saya lupa payung di dalam kereta.", "Payung saya ketinggalan di dalam kereta.", "物理的な物をどこかに「置き忘れる・置いてきてしまう」時は必ず ketinggalan（受動・自発）を用います。lupa は「記憶から消える（失念する）」なので、物を目的語にして lupa barang di... と言うと極めて不自然です。"),
            ("「彼の名前を忘れてしまった」と言う時。", "Namanya ketinggalan.", "Saya lupa namanya.", "記憶や約束、タスクを「忘れる」時は lupa を用います。人の名前を ketinggalan と言うと「名前だけ物理的にどこかに落としてきた」ような意味不明な文になります。")
        ],
        "drill": [
            ("スマホを家に置き忘れてきた（置き忘れ）。", "Ponsel saya ketinggalan di rumah.", "ポンセル サヤ クティンガラン ディ ルマ", "置き忘れ ketinggalan。"),
            ("パスワードを完全に忘れてしまった（失念）。", "Saya benar-benar lupa kata sandi saya.", "サヤ ブナルブナル ルパ カタ サンディ サヤ", "記憶喪失 lupa。"),
            ("タクシーの中に財布を忘れてしまった（置き忘れ）。", "Dompet saya ketinggalan di dalam taksi.", "ドンペット サヤ クティンガラン ディ ダラム タクスィ", "置き忘れ ketinggalan。"),
            ("彼との約束の時間を忘れていた（失念）。", "Saya lupa jam janji temu dengan dia.", "サヤ ルパ ジャム ジャンジ トゥム ドゥンガン ディア", "失念 lupa janji。"),
            ("鍵をオフィスに忘れたので家に入れない。", "Kunci kantor ketinggalan, jadi tidak bisa masuk rumah.", "クンチ カントール クティンガラン、ジャディ ティダッ ビサ マスッ ルマ", "置き忘れ ketinggalan。"),
            ("宿題を提出するのを忘れないでね（念押し）。", "Jangan lupa mengumpulkan PR ya.", "ジャンガン ルパ ムングンプルカン ピーアール ヤ", "失念防止 jangan lupa。"),
            ("飛行機にパスポートを忘れたら大変なことになる。", "Bisa gawat kalau paspor sampai ketinggalan di pesawat.", "ビサ ガワット カラウ パスポル サンパイ クティンガラン ディ プサワット", "置き忘れ ketinggalan。"),
            ("うっかりドアの施錠を忘れてしまった。", "Lupa mengunci pintu karena terburu-buru.", "ルパ ムングンチ ピントゥ カレナ トゥルブルブル", "動作の失念 lupa mengunci。"),
            ("何か忘れ物はありませんか？（確認）", "Apakah ada barang yang ketinggalan?", "アパカ アダ バラン ヤン クティンガラン", "忘れ物 barang ketinggalan。"),
            ("過去の嫌な思い出は早く忘れてしまおう。", "Mari segera melupakan kenangan buruk masa lalu.", "マリ スグラ ムルパカン クナンガン ブルッ マサ ラル", "忘れ去る melupakan。"),
            ("メガネをカフェのテーブルに置き忘れた。", "Kacamata saya ketinggalan di meja kafe.", "カチャマタ サヤ クティンガラン ディ メジャ カフェ", "置き忘れ ketinggalan。"),
            ("彼の誕生日をうっかり忘れてしまった。", "Saya terlupa hari ulang tahunnya.", "サヤ トゥルルパ ハリ ウラン タフンニャ", "うっかり失念 terlupa。"),
            ("充電器をホテルに忘れてきてしまった。", "Pengisi daya saya ketinggalan di kamar hotel.", "プンギスィ ダヤ サヤ クティンガラン ディ カマル ホテル", "置き忘れ ketinggalan。"),
            ("名前は覚えているが、顔を忘れてしまった。", "Ingat namanya tapi lupa wajahnya.", "インガット ナマニャ タピ ルパ ワジャニャ", "失念 lupa wajah。"),
            ("忘れっぽい性格を直したい（健忘）。", "Ingin memperbaiki sifat pelupa ini.", "インギン ムムプルバイキ スィファット プルパ イニ", "忘れっぽい人 pelupa。")
        ],
        "quiz": [
            ("「レストランに傘を置き忘れてきた」の自然な表現は？", ["Payung saya ketinggalan di restoran.", "Saya lupa payung di restoran.", "Payung saya melupakan restoran.", "Restoran ketinggalan payung saya."], 1),
            ("「宿題をするのを忘れた」の自然な表現は？", ["Saya lupa mengerjakan PR.", "PR saya ketinggalan mengerjakan.", "Saya ketinggalan PR lupa.", "PR lupa saya kerjakan."], 1),
            ("「忘れ物はありませんか？」とホテル退出時に聞く定番フレーズは？", ["Ada barang yang ketinggalan?", "Ada barang yang lupa?", "Ada barang yang hilang?", "Ada barang yang lewat?"], 1)
        ]
    },
    {
        "slug": "44-hilang-kehilangan-kalah-loss",
        "title": "【誤用克服】「失う」の hilang, kehilangan, kalah（敗北）の他動詞・自動詞混同",
        "intro": "日本語の「なくす」「うしなう」「まける」の混同により、財布を無くした時に saya hilang（私自身が行方不明になった）と言ってしまったり、試合で負ける（kalah）と物を紛失する（kehilangan）を取り違えるトラブルを解決します。",
        "cases": [
            ("「財布を無くしてしまいました」と警察に届ける時。", "Saya hilang dompet.", "Saya kehilangan dompet. / Dompet saya hilang.", "hilang は自動詞で「消える・紛失する」です。主語に人を置いて Saya hilang と言うと「私自身が行方不明になりました・遭難しました」という意味になります。人が主語なら被害構文の kehilangan（〜を失う）、または Dompet saya hilang（財布が紛失した）とします。"),
            ("「昨日のサッカーの試合で負けてしまった」と言う時。", "Tim kami hilang dalam pertandingan kemarin.", "Tim kami kalah dalam pertandingan kemarin.", "勝負や試合に「負ける」のは kalah です。hilang を使うと「試合中にチーム全員が神隠しに遭って行方不明になった」ような意味不明な文になってしまいます。")
        ],
        "drill": [
            ("駅で財布を無くしてしまった（主語: 人の被害）。", "Saya kehilangan dompet di stasiun.", "サヤ クヒランガン ドンペット ディ スタシウン", "被害 kehilangan。"),
            ("私のスーツケースが空港で見当たらない（主語: 物が消えた）。", "Koper saya hilang di bandara.", "コペル サヤ ヒラン ディ バンダラ", "物が消える hilang。"),
            ("決勝戦で相手チームに惜しくも負けた（勝負の敗北）。", "Kalah tipis dari tim lawan di babak final.", "カラ ティピス ダリ ティム ラワン ディ ババッ フィナル", "敗北 kalah。"),
            ("彼は火災で全財産を失った（甚大な喪失）。", "Dia kehilangan seluruh hartanya akibat kebakaran.", "ディア クヒランガン スルルー ハルタニャ アキバット クバカラン", "財産喪失 kehilangan harta。"),
            ("痛みが次第に消えていった（痛みの消失）。", "Rasa sakitnya perlahan-lahan hilang.", "ラサ サキッニャ プルラハンラハン ヒラン", "消失 hilang。"),
            ("大切な友人を亡くして深い悲しみに暮れている。", "Kehilangan sahabat terbaik dan sangat berduka.", "クヒランガン サハバット トゥルバイッ ダン サンガット ブルドゥカ", "死別 kehilangan。"),
            ("やる気と自信を失ってしまった。", "Kehilangan motivasi dan rasa percaya diri.", "クヒランガン モティヴァスィ ダン ラサ プルチャヤ ディリ", "自信喪失 kehilangan motivasi。"),
            ("じゃんけんで負けた人がジュースをおごる（敗北）。", "Yang kalah suit harus mentraktir jus.", "ヤン カラ スイット ハルス ムントラクティル ジュス", "じゃんけん敗北 yang kalah。"),
            ("濃い霧が晴れて太陽が見えてきた。", "Kabut tebal hilang dan matahari mulai terlihat.", "カブット トゥバル ヒラン ダン マタハリ ムライ トゥルリハット", "霧が消える kabut hilang。"),
            ("森の中で道を見失って迷子になった（遭難）。", "Tersesat dan hilang arah di dalam hutan.", "トゥルスサット ダン ヒラン アラ ディ ダラム フタン", "見失う hilang arah。"),
            ("愛車を盗難で失って警察に通報した。", "Kehilangan mobil karena dicuri dan lapor ke polisi.", "クヒランガン モビル カレナ ディチュリ ダン ラポル ク ポリシスィ", "盗難被害 kehilangan mobil。"),
            ("一度失った信頼を取り戻すのは難しい。", "Sulit mengembalikan kepercayaan yang sudah hilang.", "スリット ムンガンバリカン クプルチャヤアン ヤン スダ ヒラン", "失われた信頼 yang sudah hilang。"),
            ("どんなに強くても負けることを恐れてはならない。", "Jangan takut kalah meski menghadapi lawan kuat.", "ジャンガン タクット カラ ムスキ ムンハダピ ラワン クアット", "負けを恐れない takut kalah。"),
            ("記憶を一時的に喪失した（記憶喪失）。", "Kehilangan ingatan untuk sementara waktu.", "クヒランガン インガタン ウントゥッ スムンタラ ワクトゥ", "記憶喪失 kehilangan ingatan。"),
            ("紛失したクレジットカードの利用停止を依頼した。", "Meminta pemblokiran kartu kredit yang hilang.", "ムミンタ プムブロキラン カルトゥ クレディット ヤン ヒラン", "紛失カード kartu yang hilang。")
        ],
        "quiz": [
            ("「私はパスポートを無くした（紛失した）」の正しい表現は？", ["Saya kehilangan paspor.", "Saya hilang paspor.", "Saya kalah paspor.", "Paspor saya kalah."], 1),
            ("「試合に負けた」を表す正しい単語は？", ["kalah", "hilang", "kehilangan", "rusak"], 1),
            ("「私の自転車が盗まれてなくなった（物が主語）」は？", ["Sepeda saya hilang dicuri.", "Saya hilang sepeda dicuri.", "Sepeda saya kalah dicuri.", "Saya kalah sepeda hilang."], 1)
        ]
    },
    {
        "slug": "45-menang-kalah-mengalahkan",
        "title": "【誤用克服】「勝つ・負ける」の menang と kalah、mengalahkan（打ち負かす）の使役関係",
        "intro": "勝敗を述べる際、「AがBに勝った」を直訳して A menang B と言ったり、「AがBを負かした」に A kalah B と言ってしまう文法破壊が多発します。他動詞 mengalahkan（打ち負かす）と前置詞 atas / dari の正しい構文パターンを確立します。",
        "cases": [
            ("「日本チームが相手チームを破った（打ち負かした）」と言う時。", "Tim Jepang menang tim lawan. / kalah tim lawan.", "Tim Jepang mengalahkan tim lawan. / Tim Jepang menang atas tim lawan.", "menang や kalah は基本的に自動詞です。目的語を取って「〜を負かす」とする場合は、接辞 meN-...-kan を付けた他動詞 mengalahkan を用いるか、menang atas...（〜に勝利する）とする必要があります。"),
            ("「私たちはライバルに負けた」と言う時。", "Kami kalah saingan kami.", "Kami kalah dari saingan kami.", "kalah も自動詞であるため、直接目的語を置くことはできません。「〜に負ける」の「〜に」は起点・比較の前置詞 dari を用いて kalah dari... と表現します。")
        ],
        "drill": [
            ("インドネシア代表が試合に勝利した（自動詞）。", "Tim nasional Indonesia berhasil menang dalam pertandingan.", "ティム ナスィオナル インドネシア ブルハスィル ムナン ダラム プルタンディンガン", "勝利 menang。"),
            ("強豪チームを3対1で打ち負かした（他動詞）。", "Mengalahkan tim unggulan dengan skor tiga-satu.", "ムンガラカン ティム ウングルラン ドゥンガン スコル ティガ サトゥ", "打ち負かす mengalahkan。"),
            ("前回のチャンピオンに惜しくも敗れた（敗北）。", "Kalah tipis dari juara bertahan sebelumnya.", "カラ ティピス ダリ ジュアラ ブルタハン スブルムニャ", "〜に敗れる kalah dari...。"),
            ("選挙で圧倒的多数の票を得て勝利した。", "Menang telak dalam pemilihan umum.", "ムナン トゥラッ ダラム プミリハン ウムム", "圧勝 menang telak。"),
            ("自分自身の弱さに打ち勝たなければならない（克服）。", "Harus bisa mengalahkan kelemahan diri sendiri.", "ハルス ビサ ムンガラカン クレマハン ディリ スンディリ", "弱点克服 mengalahkan kelemahan。"),
            ("勝っても負けてもスポーツマンシップが大切だ。", "Menang atau kalah, sportivitas tetap yang utama.", "ムナン アタウ カラ、スポルティヴィタス トゥタップ ヤン ウタマ", "勝敗 menang atau kalah。"),
            ("彼らは宿敵に対して見事な勝利を収めた。", "Mereka meraih kemenangan gemilang atas musuh bebuyutan.", "ムレカ ムライ クムナンガン グミラン アタス ムス ブブユタン", "〜への勝利 kemenangan atas...。"),
            ("価格競争で競合他社に負けてしまった。", "Kalah bersaing dalam perang harga dengan kompetitor.", "カラ ブルサイン ダラム プラン ハルガ ドゥンガン コンペティトル", "競争敗北 kalah bersaing。"),
            ("困難を乗り越えてチャンピオンになった。", "Mengalahkan segala rintangan dan menjadi juara.", "ムンガラカン スガラ リンタンガン ダン ムンジャディ ジュアラ", "困難を打破 mengalahkan rintangan。"),
            ("宝くじで1億ルピアが当選した（当選）。", "Menang undian berhadiah seratus juta rupiah.", "ムナン ウンディアン ブルハディア スラトゥス ジュタ ルピア", "当選 menang undian。"),
            ("彼はどんな勝負でも負けず嫌いだ。", "Dia tidak pernah mau kalah dalam hal apa pun.", "ディア ティダッ プルナ マウ カラ ダラム ハル アパ プン", "負けず嫌い tidak mau kalah。"),
            ("世界王者を倒して新チャンピオンに輝いた。", "Mengalahkan juara dunia dan menjadi juara baru.", "ムンガラカン ジュアラ ドゥニア ダン ムンジャディ ジュアラ バル", "王座奪取 mengalahkan juara。"),
            ("不戦勝で次のラウンドに進出した。", "Menang tanpa bertanding dan maju ke babak berikutnya.", "ムナン タンパ ブルタンディン ダン マジュ ク ババッ ブルイクットニャ", "不戦勝 menang tanpa bertanding。"),
            ("経験の差で相手に敵わなかった（実力差）。", "Kalah pengalaman dibanding lawan.", "カラ プンガラマン ディバンディン ラワン", "経験不足 kalah pengalaman。"),
            ("チームの一致団結が勝利をもたらした。", "Kekompakan tim membuahkan kemenangan manis.", "クコンパカン ティム ムンブアカン クムナンガン マニス", "名詞 勝利 kemenangan。")
        ],
        "quiz": [
            ("「相手チームを負かした（打ち負かす）」を表す他動詞は？", ["mengalahkan", "memenangkan", "kalahkan", "terkalahkan"], 1),
            ("「ライバルチームに負けた」の前置詞として適切なのは？", ["Kalah dari rival", "Kalah ke rival", "Kalah untuk rival", "Kalah pada rival"], 1),
            ("「大差で圧勝した」を表す慣用表現は？", ["menang telak", "menang besar sekali", "menang hancur", "menang rusak"], 1)
        ]
    },
    {
        "slug": "46-rusak-patah-hancur-pecah",
        "title": "【誤用克服】「壊れる」の rusak, patah, hancur, pecah の損傷形態別使い分け",
        "intro": "日本語の「こわれる」「われる」「おれる」「くだける」をすべて rusak で済ませていませんか？インドネシア語では、ガラスや陶器の「粉砕・割れ（pecah）」、棒や骨の「折損（patah）」、建物や組織の「崩壊・壊滅（hancur）」、機能的「故障（rusak）」が物理的に厳密に区別されます。",
        "cases": [
            ("「ガラスのコップが床に落ちて割れた」と言う時。", "Gelas kaca jatuh dan rusak.", "Gelas kaca jatuh dan pecah.", "ガラス、陶器、卵、風船などが割れる・破裂するのは pecah です。rusak を使うと「コップの機能が故障した」という意味になり、物理的破壊の状態が全く伝わりません。"),
            ("「転んで腕の骨を折ってしまった（骨折）」と言う時。", "Tangan saya rusak karena jatuh.", "Tulang tangan saya patah karena jatuh.", "骨、木の枝、鉛筆などの棒状のものがポキッと「折れる」のは patah です。rusak だと「腕が機械のように作動しなくなった」ような奇怪な表現になります。")
        ],
        "drill": [
            ("エアコンが故障して冷たい風が出ない（機能的故障）。", "AC-nya rusak sehingga tidak keluar udara dingin.", "アーセーニャ ルサッ スヒンガ ティダッ クルアル ウダラ ディンギン", "機能故障 rusak。"),
            ("お皿が床に落ちて粉々に割れてしまった（陶器の割れ）。", "Piring jatuh ke lantai dan pecah berkeping-keping.", "ピリン ジャトゥ ク ランタイ ダン プチャ ブルクピンクピン", "割れる pecah。"),
            ("強風で大きな木の枝がポキリと折れた（棒状の折損）。", "Dahan pohon yang besar patah karena angin kencang.", "ダハン ポホン ヤン ブサル パタ カレナ アンギン クンチャン", "折れる patah。"),
            ("大地震で多くの建物が倒壊し瓦礫となった（壊滅・粉砕）。", "Banyak gedung hancur akibat gempa bumi dahsyat.", "バニャッ グドゥン ハンチュル アキバット グムパ ブミ ダーシャット", "壊滅 hancur。"),
            ("パソコンのキーボードが反応しない、壊れたようだ。", "Papan ketik komputer rusak tidak merespons.", "パパン クティッ コンピューテル ルサッ ティダッ ムレスポンス", "電子機器故障 rusak。"),
            ("転んで足の骨を折って入院した（骨折）。", "Jatuh dan tulang kakinya patah hingga dirawat di RS.", "ジャトゥ ダン トゥラン カキニャ パタ ヒンガ ディラワット ディ エルエス", "骨折 tulang patah。"),
            ("窓ガラスがボールに当たって割れた。", "Kaca jendela pecah terkena lemparan bola.", "カチャ ジュンデラ プチャ トゥルクナ レンパラン ボラ", "ガラス割れ kaca pecah。"),
            ("失望で私の心は粉々に打ち砕かれた（比喩的失意）。", "Hati saya hancur berkeping-keping karena kecewa.", "ハティ サヤ ハンチュル ブルクピンクピン カレナ クチェワ", "失意 hancur。"),
            ("車のブレーキが壊れて事故を起こしかけた。", "Rem mobil rusak dan hampir menyebabkan kecelakaan.", "レム モビル ルサッ ダン ハンピル ムニェバブカン クチュラカアン", "機能不全 rem rusak。"),
            ("彼女に振られて失恋した（失恋・心が折れる）。", "Dia sedang patah hati karena diputuskan pacarnya.", "ディア スダン パタ ハティ カレナ ディプトゥスカン パチャルニャ", "失恋 patah hati。"),
            ("風船が針に触れてパンと破裂した（破裂）。", "Balonnya pecah saat terkena jarum.", "バロンニャ プチャ サアット トゥルクナ ジャルム", "破裂 pecah。"),
            ("台風で屋根が吹き飛ばされて家が半壊した。", "Rumahnya hancur sebagian akibat diterjang angin puting beliung.", "ルマニャ ハンチュル スバギアン アキバット ディトゥルジャン アンギン プティン ブリアウン", "半壊 hancur。"),
            ("眼鏡のフレームが踏まれて折れてしまった。", "Bingkai kacamata patah karena terinjak.", "ビンカイ カチャマタ パタ カレナ トゥリンジャッ", "フレーム折損 bingkai patah。"),
            ("スマホの画面にヒビが入って割れてしまった。", "Layar ponselnya retak dan pecah.", "ラヤール ポンセルニャ ルタッ ダン プチャ", "画面割れ layar pecah。"),
            ("腐った卵からひどい悪臭が漂っている（腐敗・損傷）。", "Telur yang rusak menimbulkan bau busuk.", "トゥルール ヤン ルサッ メニムブルカン バウ ブスッ", "品質劣化 rusak。")
        ],
        "quiz": [
            ("ガラスのコップやお皿が「割れる」を表す正しい単語は？", ["pecah", "patah", "hancur", "rusak"], 1),
            ("骨や木の枝がポキリと「折れる」を表す正しい単語は？", ["patah", "pecah", "bocor", "lepas"], 1),
            ("エアコンや冷蔵庫などの機械が「作動せず故障している」状態は？", ["rusak", "pecah", "patah", "hancur"], 1)
        ]
    },
    {
        "slug": "47-jatuh-gugur-turun-fall",
        "title": "【誤用克服】「落ちる」の jatuh, gugur（殉職・落葉・中絶）, turun（下降・降雨）の峻別",
        "intro": "日本語の「おちる」「さがる」「ふる」は、重力による落下（jatuh）、名誉ある戦死や落葉・失格（gugur）、物理的・数値的な下降や雨の降下（turun）に厳格に分かれます。試験に落ちるのを jatuh と直訳する典型的なミスを根絶します。",
        "cases": [
            ("「大学の入学試験に落ちてしまった」と言う時。", "Saya jatuh dalam ujian masuk universitas.", "Saya tidak lulus / gagal dalam ujian masuk universitas.", "試験や選考に「落ちる（不合格になる）」時は tidak lulus や gagal を用います。jatuh は「物理的に高所からドスンと落下する」ことなので、jatuh ujian だと試験会場の床に転落した意味になります。"),
            ("「戦場で勇敢に戦って命を落とした（戦死・殉職）」と言う時。", "Tentara itu jatuh di medan perang.", "Prajurit itu gugur di medan perang.", "軍人・英雄が国家のために戦死・殉職すること、および葉が散ることには極めて格調高い語である gugur を用います。jatuh だと単に足元が滑って転んだだけのように聞こえます。")
        ],
        "drill": [
            ("木からリンゴが地面に落ちた（重力落下）。", "Buah apel jatuh dari pohon ke tanah.", "ブア アペル ジャトゥ ダリ ポホン ク タナ", "落下 jatuh。"),
            ("国家を守るために戦場で殉職した英雄（殉職）。", "Pahlawan yang gugur di medan pertempuran demi negara.", "パフラワン ヤン ググル ディ メダン プルトゥムプラン デミ ヌガラ", "殉職 gugur。"),
            ("午後になって急に大雨が降ってきた（降雨）。", "Hujan deras turun tiba-tiba pada siang hari.", "フジャン ドゥラス トゥルン ティバティバ パダ スィアン ハリ", "降雨 turun hujan。"),
            ("資格試験に不合格になって落ち込んだ（不合格）。", "Sedih karena gagal / tidak lulus dalam ujian sertifikasi.", "スディ カレナ ガガル / ティダッ ルルス ダラム ウジアン スルティフィカスィ", "不合格 gagal / tidak lulus。"),
            ("階段から足を踏み外して転落した（転落）。", "Jatuh terpeleset dari tangga.", "ジャトゥ トゥルプレセット ダリ タンガ", "転落 jatuh。"),
            ("秋になって枯れ葉がハラハラと散る（落葉）。", "Daun-daun kering gugur saat musim gugur.", "ダウンダウン クリン ググル サアット ムスィム ググル", "落葉 gugur。"),
            ("ガソリンの価格が10%下がった（価格下落）。", "Harga bensin turun sebesar sepuluh persen.", "ハルガ ベンシン トゥルン スブサル スプル プルセン", "下落 turun。"),
            ("彼は彼女に一目惚れして恋に落ちた（比喩的落下）。", "Dia langsung jatuh cinta pada pandangan pertama.", "ディア ランスン ジャトゥ チンタ パダ パンダンガン プルタマ", "恋に落ちる jatuh cinta。"),
            ("トーナメントの1回戦で早くも敗退した（敗退）。", "Sudah gugur di babak pertama turnamen.", "スダ ググル ディ ババッ プルタマ トゥルナメン", "敗退 gugur。"),
            ("体温が正常値まで下がって安心した。", "Suhu tubuh sudah turun ke batas normal.", "スフ トゥブ スダ トゥルン ク バタス ノルマル", "体温下降 turun。"),
            ("財布をポケットから落としてしまった。", "Dompetnya jatuh dari saku celana.", "ドンペットニャ ジャトゥ ダリ サク チュラナ", "落とす jatuh。"),
            ("飛行機からパラシュートで飛び降りる（降下）。", "Turun menggunakan parasut dari pesawat.", "トゥルン ムングナカン パラスット ダリ プサワット", "降下 turun。"),
            ("赤字続きで会社が倒産に追い込まれた（破産）。", "Perusahaan jatuh bangkrut karena terus merugi.", "プルサハアン ジャトゥ バンクルト カレナ トゥルス ムルギ", "倒産 jatuh bangkrut。"),
            ("葉巻の灰が絨毯の上に落ちた。", "Abu rokok jatuh ke atas karpet.", "アブ ロコッ ジャトゥ ク アタス カルペット", "灰が落ちる abu jatuh。"),
            ("血圧が急激に下がってめまいがした。", "Tekanan darah turun drastis hingga merasa pusing.", "トゥカナン ダラ トゥルン ドラスティス ヒンガ ムラサ プシン", "血圧降下 turun。")
        ],
        "quiz": [
            ("「試験に落ちた（不合格）」を意味する正しい表現は？", ["gagal / tidak lulus ujian", "jatuh ujian", "turun ujian", "gugur ujian"], 1),
            ("兵士が戦場で名誉の戦死を遂げた場合の動詞は？", ["gugur", "jatuh", "turun", "kalah"], 1),
            ("「物価や気温が下がる」を表す動詞は？", ["turun", "jatuh", "gugur", "hilang"], 1)
        ]
    },
    {
        "slug": "48-naik-turun-menumpang-transit",
        "title": "【誤用克服】「乗る・降りる」の naik と turun、menumpang（便乗）の交通コロケーション",
        "intro": "交通機関の利用で最も基本的な naik（乗る）と turun（降りる）ですが、乗り換え（transit/transfer）や、他人の車・バイクに「便乗させてもらう（numpang / menumpang）」の表現を混同すると、運賃トラブルや意思疎通の齟齬が発生します。",
        "cases": [
            ("「駅で電車を乗り換える」と言いたい時。", "Saya naik ganti kereta di stasiun.", "Saya pindah / ganti kereta di stasiun transit.", "電車の「乗り換え」には pindah kereta（電車を移る）や ganti kereta（電車を変える）を用います。naik ganti のように動詞を直結させるのは不自然な文法破綻です。"),
            ("友人の車に「ちょっと乗せていってくれない？（便乗）」と頼む時。", "Boleh saya naik mobilmu gratis?", "Boleh numpang mobilmu sampai depan jalan?", "知人や友人の乗り物に無料で「便乗させてもらう」「同乗する」行為には numpang（文語: menumpang）を用います。naik mobilmu gratis などと直訳すると極めて不躾に聞こえます。")
        ],
        "drill": [
            ("毎朝MRTに乗って通勤しています（乗車）。", "Setiap pagi naik MRT untuk berangkat kerja.", "スティアッ パギ ナイス エムアールティー ウントゥッ ブランカット クルジャ", "乗車 naik。"),
            ("次のバス停で降ります（降車）。", "Saya akan turun di halte berikutnya.", "サヤ アカン トゥルン ディ ハルテ ブルイクットニャ", "降車 turun。"),
            ("マンガライ駅で別の路線に乗り換える（乗換）。", "Pindah kereta di Stasiun Manggarai.", "ピンダ クレタ ディ スタシウン マンガライ", "乗換 pindah kereta。"),
            ("駅まで車に乗せてもらってもいい？（便乗）", "Boleh numpang sampai stasiun?", "ボレ ヌンパン サンパイ スタシウン", "便乗 numpang。"),
            ("飛行機に搭乗する時間になりました（搭乗）。", "Sudah waktunya naik ke pesawat.", "スダ ワクトゥニャ ナイス ク プサワット", "搭乗 naik pesawat。"),
            ("バイクの後ろに乗る（二人乗り）。", "Naik motor berboncengan di belakang.", "ナイス モトール ブルボンチェンガン ディ ブラカン", "同乗 berboncengan。"),
            ("バスが満員で乗ることができなかった。", "Busetnya penuh sesak sehingga tidak bisa naik.", "バスニャ プヌ ササッ スヒンガ ティダッ ビサ ナイス", "乗車不能 tidak bisa naik。"),
            ("タクシーから降りる時にお忘れ物のないように。", "Hati-hati jangan sampai ada barang tertinggal saat turun dari taksi.", "ハティハティ ジャンガン サンパイ アダ バラン トゥルティンガル サアット トゥルン ダリ タクスィ", "降車 turun dari taksi。"),
            ("ガソリン代を割り勘にして同乗する（カープール）。", "Menumpang mobil teman dengan patungan bensin.", "ムヌンパン モビル トゥマン ドゥンガン パトゥンガン ベンシン", "同乗 menumpang mobil。"),
            ("エレベーターに乗って最上階へ上がる。", "Naik lift menuju ke lantai paling atas.", "ナイス リフト メヌジュ ク ランタイ パリン アタス", "昇降機 naik lift。"),
            ("階段をゆっくり降りる。", "Turun tangga dengan hati-hati perlahan.", "トゥルン タンガ ドゥンガン ハティハティ プルラハン", "階段を降りる turun tangga。"),
            ("船に乗って離島へ渡る。", "Menyeberang ke pulau terpencil naik kapal feri.", "メニェブラン ク プラウ トゥルプンチル ナイス カパル フェリ", "船に乗る naik kapal。"),
            ("乗り過ごして終点まで行ってしまった。", "Kebablasan naik kereta sampai stasiun terakhir.", "クバブラサン ナイス クレタ サンパイ スタシウン トゥラキール", "乗り過ごし kebablasan。"),
            ("トイレをお借りしてもよろしいですか？（場所の拝借）", "Boleh numpang ke kamar mandi sebentar?", "ボレ ヌンパン ク カマル マンディ スブンタル", "場所借用 numpang ke kamar mandi。"),
            ("乗客全員が無事に下船した。", "Semua penumpang kapal sudah turun dengan selamat.", "スムア プヌンパン カパル スダ トゥルン ドゥンガン スラマット", "下船 turun kapal。")
        ],
        "quiz": [
            ("電車の「乗り換え（別の車両・路線へ移る）」を表す表現は？", ["pindah kereta", "naik ganti kereta", "turun naik kereta", "transit jalan kereta"], 1),
            ("友人の車に「乗せてって！」と便乗をお願いする口語単語は？", ["numpang", "pinjam", "sewa", "ambil"], 1),
            ("「次のバス停で降ります」の動詞は？", ["turun", "naik", "jatuh", "lelah"], 1)
        ]
    },
    {
        "slug": "49-buka-tutup-membukakan-doors",
        "title": "【誤用克服】「開ける・閉める」の buka と tutup、membukakan（開けてあげる）の使役",
        "intro": "ドアや窓を「開ける／閉める」基本動詞 buka / tutup ですが、他人のために「開けてあげる（benefactive）」という相手への配慮を表す際は、受益接辞 -kan を伴う membukakan / menutupkan を用いるのが美しいインドネシア語の作法です。",
        "cases": [
            ("荷物を抱えた同僚のために「ドアを開けてあげるよ」と言う時。", "Saya buka pintu untukmu.", "Biar saya bukakan pintunya ya.", "他人のために親切に動作を行う（受益使役）際は、接辞 -kan を使って membukakan pintunya と表現するのが極めて自然でスマートです。buka pintu untukmu は直訳的で硬い響きになります。"),
            ("「お店は何時に開きますか／閉まりますか？」と営業時間を尋ねる時。", "Jam berapa toko ini membukakan?", "Jam berapa tokonya buka / tutup?", "店舗の営業開始・終了という自動詞的・状態的表現には、単純語の buka / tutup を用います。membukakan を使うと「誰のために店を開けてあげるのか」という不自然な文になります。")
        ],
        "drill": [
            ("荷物で両手が塞がっているから、ドアを開けてくれる？", "Tanganku penuh, bisa tolong bukakan pintunya?", "タンガンク プヌ、ビサ トロン ブカカン ピントゥニャ", "開けてあげる bukakan pintu。"),
            ("銀行の営業時間は午前8時から午後3時までです（営業）。", "Bank buka dari jam 8 pagi sampai jam 3 sore.", "バンク ブカ ダリ ジャム デラパン パギ サンパイ ジャム ティガ ソレ", "開店 buka。"),
            ("寒気が入ってくるので窓を閉めてください（閉める）。", "Tolong tutup jendelanya karena udaranya dingin.", "トロン トゥトゥップ ジュンデラニャ カレナ ウダラニャ ディンギン", "窓を閉める tutup jendela。"),
            ("お母さんのためにビンのフタを開けてあげる（親切）。", "Membukakan tutup botol untuk ibu.", "ムンブカカン トゥトゥップ ボトル ウントゥッ イブ", "開けてあげる membukakan。"),
            ("新しく銀行口座を開設した（口座開設）。", "Membuka rekening tabungan baru di bank.", "ムンブカ ルクニン タブンガン バル ディ バンク", "開設 membuka rekening。"),
            ("祝日のため本日は休業いたします（閉店・休業）。", "Toko tutup hari ini karena libur nasional.", "トコ トゥトゥップ ハリ イニ カレナ リブル ナスィオナル", "休業 tutup。"),
            ("心を開いて率直に話し合いましょう（比喩）。", "Mari buka hati dan bicara secara jujur.", "マリ ブカ ハティ ダン ビチャラ スチャラ ジュジュル", "心を開く buka hati。"),
            ("風でバタンとドアが勝手に閉まった（自発）。", "Pintunya tertutup sendiri karena hembusan angin.", "ピントゥニャ トゥルトゥトゥップ スンディリ カレナ フムブサン アンギン", "閉まる tertutup。"),
            ("彼は紳士的に車のドアを開けて彼女を乗せた。", "Dengan sopan membukakan pintu mobil untuknya.", "ドゥンガン ソパン ムンブカカン ピントゥ モビル ウントゥッニャ", "ドアを開けてあげる membukakan。"),
            ("本を50ページまで開きなさい（指示）。", "Buka bukumu sampai halaman lima puluh.", "ブカ ブクム サンパイ ハラマン リマ プル", "本を開く buka buku。"),
            ("道路が冠水したため通行止めになった（閉鎖）。", "Jalan ditutup total karena tergenang banjir.", "ジャラン ディトゥトゥップ トタル カレナ トゥルゲナン バンジル", "道路閉鎖 jalan ditutup。"),
            ("箱の封を開ける（開封）。", "Membuka segel kotak paket.", "ムンブカ セゲル コタッ パケット", "開封 membuka segel。"),
            ("カーテンを閉めて日差しを遮る。", "Menutup gorden untuk menghalau sinar matahari.", "ムヌトゥップ ゴルデン ウントゥッ ムンハラウ スィナル マタハリ", "カーテンを閉める menutup gorden。"),
            ("新規ビジネスの機会を切り拓く（機会創出）。", "Membuka peluang bisnis yang baru.", "ムンブカ プルアン ビスニス ヤン バル", "機会を開く membuka peluang。"),
            ("会議を閉会いたします（閉会）。", "Menutup acara rapat dengan doa bersama.", "ムヌトゥップ アチャラ ラパット ドゥンガン ドア ブルサマ", "閉会 menutup acara。")
        ],
        "quiz": [
            ("両手に荷物を持つ人のために「ドアを開けてあげます」と言うスマートな表現は？", ["Biar saya bukakan pintunya.", "Saya buka pintu kepadamu.", "Saya membukakan untuk pintu.", "Pintu dibuka untukmu."], 1),
            ("「スーパーは何時に閉まりますか？」の正しい表現は？", ["Supermarket tutup jam berapa?", "Supermarket menutupkan jam berapa?", "Supermarket ditutupkan jam berapa?", "Supermarket kancing jam berapa."], 1),
            ("「銀行口座を開設する」の正しい表現は？", ["membuka rekening", "menutup rekening", "membukakan rekening", "terbuka rekening"], 1)
        ]
    },
    {
        "slug": "50-clinic-comprehensive-drill",
        "title": "【誤用克服総括】日本人特有の不自然なインドネシア語・誤用克服50問総合診断",
        "intro": "セクション26「日本人特有の不自然な表現・矯正クリニック」で学んだ全50テーマの処方箋を総動員する、究極の実戦診断テストです。直訳の罠、レジスターの不一致、助動詞・前置詞の混同を完全に克服し、ネイティブが唸る洗練された自然なインドネシア語を反射的に発声できるかチェックします。",
        "cases": [
            ("「薬を飲めば頭痛が治る（無生物主語の直訳）」の克服。", "Obat ini menyembuhkan sakit kepala saya.", "Kalau minum obat ini, sakit kepala saya akan sembuh.", "無生物主語を避けて条件節（Kalau...）にし、人間または症状を主語にして語順を自然に組み替えます。"),
            ("「財布を無くしてしまいました（主語の混乱）」の克服。", "Saya hilang dompet di kereta.", "Dompet saya ketinggalan / hilang di kereta. / Saya kehilangan dompet.", "自動詞 hilang と被害構文 kehilangan を正しく使い分け、行方不明者と誤解されるのを防ぎます。")
        ],
        "drill": [
            ("【テンス】私は昨日すでに宿題を終えました（完了）。", "Kemarin saya sudah menyelesaikan PR saya.", "クマリン サヤ スダ ムニェレサイカン ピーアール サヤ", "アスペクト sudah。"),
            ("【恩恵】母が美味しいスープを作ってくれた（受益）。", "Ibu membuatkan sup yang lezat untuk saya.", "イブ ムムブアットカン スップ ヤン ルザット ウントゥッ サヤ", "受益接辞 -kan。"),
            ("【語順】通りにはたくさんの人々がいます（数量詞）。", "Ada banyak orang di jalan raya.", "アダ バニャッ オラン ディ ジャラン ラヤ", "数量詞 banyak orang。"),
            ("【強調】このバリ島の景色は本当に素晴らしい（単一強調）。", "Pemandangan Bali ini sangat indah / indah sekali.", "プマンダンガン バリ イニ サンガット インダ / インダ スカリ", "二重修飾の回避。"),
            ("【依頼】同僚に「ちょっと手伝ってくれる？」と頼む（自然な依頼）。", "Bisa minta tolong sebentar?", "ビサ ミンタ トロン スブンタル", "日常の依頼 Bisa minta tolong...。"),
            ("【思考】彼が怒っているのかと思い込んでいた（思い違い）。", "Saya kira dia tadi marah.", "サヤ キラ ディア タディ マラ", "思い違い・推測 kira。"),
            ("【知得】山田さんのことは個人的によく知っています（面識）。", "Saya kenal baik dengan Pak Yamada secara pribadi.", "サヤ クナル バイッ ドゥンガン パッ ヤマダ スチャラ プリバディ", "面識 kenal。"),
            ("【居住】私は現在ジャカルタに住んでいます（居住）。", "Saya tinggal di Jakarta sekarang.", "サヤ ティンガル ディ ジャカルタ スカラン", "居住 tinggal。"),
            ("【復帰】昼食を終えてすぐにオフィスに戻ります（職場復帰）。", "Selesai makan siang segera kembali ke kantor.", "スルサイ マカン スィアン スグラ クンバリ ク カントール", "復帰 kembali。"),
            ("【移動】友人を車で空港まで送り届ける（人を送る）。", "Mengantar teman ke bandara naik mobil.", "ムンガンタル トゥマン ク バンダラ ナイス モビル", "人を送る mengantar。"),
            ("【賃貸】旅行のためにレンタカーを1日借りる（有料）。", "Menyewa mobil selama satu hari untuk jalan-jalan.", "メニェワ モビル スラマ サトゥ ハリ ウントゥッ ジャランジャラン", "有料賃貸 menyewa。"),
            ("【土産】バリ島旅行のお土産に名物のお菓子を買った（旅土産）。", "Membeli makanan khas untuk oleh-oleh dari Bali.", "ムンブリ マカナン カス ウントゥッ オレホレ ダリ バリ", "旅土産 oleh-oleh。"),
            ("【感情】食べ残して捨てるのは本当にもったいない（機会損失）。", "Sayang sekali kalau makanan ini dibuang.", "サヤン スカリ カラウ マカナン イニ ディブアン", "もったいない sayang。"),
            ("【レジスター】あ〜疲れた！少し休憩しよう（口語）。", "Aduh capek banget! Istirahat dulu yuk.", "アドゥ チャペッ バンゲット！ イスティラハット ドゥル ユッ", "口語疲労 capek banget。"),
            ("【評価】この歴史映画は内容がとても面白くて興味深い（知的好奇心）。", "Film sejarah ini sangat menarik untuk ditonton.", "フィルム スジャラ イニ サンガット ムナリッ ウントゥッ ディトントン", "興味深い menarik。")
        ],
        "quiz": [
            ("「駅で財布を無くした」の最も自然な表現は？", ["Saya kehilangan dompet di stasiun.", "Saya hilang dompet di stasiun.", "Dompet kalah di stasiun.", "Saya lupa dompet hilang."], 1),
            ("「友人を車で空港まで送る」の正しい動詞は？", ["mengantar", "mengirim", "membawa", "mengambil"], 1),
            ("「この本はとても面白い（興味深い）」の適切な単語は？", ["menarik", "lucu", "aneh", "rusak"], 1)
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

print("Batch 1091-1100 generated successfully.")
