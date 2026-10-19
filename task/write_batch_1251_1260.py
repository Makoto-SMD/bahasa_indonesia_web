# -*- coding: utf-8 -*-
"""
Batch generation script for Section 31: Collocations Batch 1 (Articles 1251-1260)
Directory: docs/lexicon/
"""

import os

articles = [
    {
        "filename": "docs/lexicon/01-verb-collocations-ambil.md",
        "title": "【共起連語】語根 ambil の必須コロケーション辞典：ambil bagian / ambil alih / ambil keputusan",
        "root": "ambil",
        "meaning": "取る、手に取る、受け取る、引き受ける",
        "core_concept": "「何かを物理的に手に取る」基本動作から、「責任や役割を引き受ける」「決断を我が物とする」「他者の心や関心を掴み取る」という抽象領域へダイナミックに派生する極めて重要度の高いコア動詞語根です。",
        "table_rows": [
            ("ambil bagian", "部分を取る", "参加する、関与する、一役買う", "フォーマル/報道", "Indonesia siap ambil bagian dalam konferensi tingkat tinggi iklim global."),
            ("ambil alih", "移行を取る", "引き継ぐ、買収する、主導権を握る", "ビジネス/法務", "Perusahaan teknologi raksasa itu sepakat mengambil alih kepemilikan startup lokal."),
            ("ambil keputusan", "決定を取る", "決断を下す、意志決定を行う", "公式/ビジネス", "Dewan direksi harus segera mengambil keputusan strategis demi keberlanjutan bisnis."),
            ("ambil hati", "心を取る", "気に入られるように振る舞う、歓心を買う", "日常/人間関係", "Ia selalu pandai mengambil hati mertuanya dengan tutur kata yang sopan."),
            ("ambil pusing", "頭痛を取る", "気にする、思い悩む、頓着する（通例子どもの否定形）", "口語/慣用表現", "Jangan ambil pusing omongan orang lain yang berniat menjatuhkan mentalmu."),
            ("ambil langkah", "歩み・足取りを取る", "措置を講じる、手を打つ、踏み切る", "報道/行政", "Pemerintah daerah mengambil langkah tegas guna menertibkan pedagang kaki lima."),
            ("ambil tindakan", "行動を取る", "処置・処分を行う、行動を起こす", "公式/法務", "Pihak berwajib tidak ragu mengambil tindakan hukum atas pelanggaran hak cipta.")
        ],
        "details": [
            {
                "term": "ambil bagian (berpartisipasi)",
                "trans": "参加する、関与する、一役買う",
                "nuance": "英語の「take part in」に相当し、国際会議、スポーツ大会、社会運動などに能動的・建設的に加わる場面で多用されます。文語では `mengambil bagian` と接頭辞 `meN-` を伴うのが一般的です。",
                "ex_id": "Seluruh elemen masyarakat diharapkan mengambil bagian dalam program vaksinasi massal.",
                "ex_kana": "スルルフ エレメン マシャラカット ディハラプカン ムンガンビル バギアン ダラム プログラム ワクシナシ マッサル",
                "ex_ja": "社会のあらゆる構成員が、集団接種プログラムに一役買う（参加する）ことが期待されています。",
                "note": "名詞化する場合は `keikutsertaan` や `partisipasi` と同義になります。"
            },
            {
                "term": "ambil alih (mengakuisisi / alih kekuasaan)",
                "trans": "引き継ぐ、買収する、権力を掌握する",
                "nuance": "物理的・組織的な管理権を別の主体から受け渡されて自らの管理下に置くことを指します。企業のM&A（買収）や政権交代の文脈で頻出します。",
                "ex_id": "Setelah restrukturisasi, bank sentral resmi mengambil alih pengawasan terhadap lembaga keuangan bermasalah tersebut.",
                "ex_kana": "ステラ レストルクトゥリサシ、バンク セントラル レスミ ムンガンビル アリフ プンガワサン トゥルハダップ ルンバガ クアンガン ブルマサラー トゥルスブット",
                "ex_ja": "事業再編後、中央銀行はその問題のある金融機関に対する監督権限を正式に引き継ぎ（掌握し）ました。",
                "note": "名詞形は合成名詞として一語化され `pengambilalihan`（買収・掌握）となります。"
            },
            {
                "term": "ambil keputusan (membuat ketetapan)",
                "trans": "決断を下す、意思決定をする",
                "nuance": "不確実な状況下で熟慮の末に一つの結論を選択する行為です。英語の「make a decision」に直結し、組織のトップやリーダーシップの文脈で必須です。",
                "ex_id": "Seorang pemimpin yang tangguh tidak boleh ragu-ragu saat harus mengambil keputusan krusial di masa krisis.",
                "ex_kana": "スオラン プミンピン ヤン タングー ティダッ ボレ ラグラグ サアット ハルス ムンガンビル クプトゥサン クルシアル ディ マサ クリシス",
                "ex_ja": "強靭なリーダーは、危機的状況において極めて重要な決断を下さねばならない時に逡巡してはなりません。",
                "note": "`menetapkan` や `memutuskan` よりも、「重みのある決定プロセス」を連想させます。"
            },
            {
                "term": "ambil pusing (peduli / memikirkan)",
                "trans": "気にする、悩む（通常 tidak / jangan と共に否定で用いる）",
                "nuance": "直訳すると「頭痛を抱え込む」。口語表現で「そんなこと気にするな」「気にする価値もない」と言う際に極めて自然に使われます。",
                "ex_id": "Dia tipe orang yang santai dan tidak mau ambil pusing terhadap kritik yang tidak konstruktif.",
                "ex_kana": "ディア ティペ オラン ヤン サンタイ ダン ティダッ マウ アンビル プシン トゥルハダップ クリティック ヤン ティダッ コンストルクティフ",
                "ex_ja": "彼は呑気な性格で、建設的でない批判に対して思い悩んだり気にしたりしないタイプです。",
                "note": "文頭に `Jangan ambil pusing!`（くよくよするな！）と単独で声をかける励ましの決まり文句です。"
            },
            {
                "term": "ambil langkah / ambil tindakan",
                "trans": "対策を講じる、行動を起こす",
                "nuance": "問題発生時に傍観せず、具体的かつ実効性のある手順を踏み出す官公庁や企業経営者の公式発表で頻出します。",
                "ex_id": "Kementerian Kesehatan segera mengambil langkah antisipatif untuk mencegah penyebaran virus baru.",
                "ex_kana": "クメンテリアン クセハタン スグラ ムンガンビル ランカ アンティシパティフ ウントゥッ ムンチェガ プニェバラン ヴィルス バル",
                "ex_ja": "保健省は新種ウイルスの拡散を未然に防ぐため、直ちに予防的措置を講じました。",
                "note": "`langkah` は「足取り」、`tindakan` は「具体的な行動・処置」を指します。"
            }
        ],
        "dialogue": {
            "title": "新規事業の参入と買収をめぐる役員協議",
            "lines": [
                ("Budi", "Bagaimana tanggapan dewan komisaris mengenai rencana kita untuk mengambil alih anak perusahaan ritel tersebut?"),
                ("Siti", "Secara umum mereka menyetujuinya, asalkan kita tidak tergesa-gesa saat mengambil keputusan akhir sebelum audit selesai."),
                ("Budi", "Tepat sekali. Kita harus mengambil langkah antisipatif agar tidak menanggung beban utang yang berlebihan."),
                ("Siti", "Benar. Banyak kompetitor yang mencoba mengintimidasi kita, tetapi kita tidak usah ambil pusing atas rumor di media sosial.")
            ],
            "trans": [
                ("ブディ", "あの小売子会社を買収（管理権取得）する弊社の計画について、監査役会はどういう反応ですか？"),
                ("シティ", "大筋では賛同していますが、監査が完了する前に拙速に最終決断を下すことのないよう釘を刺されました。"),
                ("ブディ", "まさにその通りです。過剰な負債を抱え込まないよう、事前の予防措置を講じねばなりません。"),
                ("シティ", "同感です。多くの競合が牽制してきていますが、SNS上の噂など気に病む（ambil pusing）必要はありません。")
            ]
        },
        "grammar_points": [
            "**meN- 派生の有無**: 公式な文章やニュース報道では `mengambil alih`, `mengambil bagian` と `meN-` を付加するのが規範的文法ですが、日常会話や口語では語根そのまま `ambil alih`, `ambil pusing` と発話されるのが自然です。",
            "**接辞による複合名詞化**: `ambil alih`（動詞句）を名詞化する場合、接頭辞 `peng-` と接尾辞 `-an` が全体を包み込み、1語に連結して `pengambilalihan`（買収・掌握・接収）という法学・経済学の重要術語になります。"
        ],
        "quizzes": [
            {
                "q": "次の空欄に入る最も自然なコロケーションを選びなさい。\n「Jangan ________ dengan cibiran orang lain, tetaplah fokus mengejar mimpimu.」",
                "choices": ["ambil hati", "ambil alih", "ambil pusing", "ambil bagian"],
                "ans": "ambil pusing",
                "expl": "「他人のあざ笑いなど気にするな（思い悩むな）」という文脈であるため、否定詞 jangan と結びついて「気に病む」を意味する `ambil pusing` が正解です。`ambil hati` は「歓心を買う」、`ambil alih` は「買収する」、`ambil bagian` は「参加する」です。"
            },
            {
                "q": "「政府は不法投棄業者に対して厳しい法的措置を講じた」を意味する適切な表現はどれか。",
                "choices": ["Pemerintah mengambil alih pedagang liar.", "Pemerintah mengambil tindakan tegas terhadap pelaku.", "Pemerintah mengambil hati masyarakat setempat.", "Pemerintah tidak ambil pusing masalah limbah."],
                "ans": "Pemerintah mengambil tindakan tegas terhadap pelaku.",
                "expl": "「厳しい法的措置・処分を講じる」は `mengambil tindakan tegas` と共起します。"
            },
            {
                "q": "動詞句 `ambil alih` を名詞化して「企業買収」を表現する正しい正書法はどれか。",
                "choices": ["pengambil alihan", "pengambilalihan", "pemgambilan alih", "pengalihan ambil"],
                "ans": "pengambilalihan",
                "expl": "接頭辞と接尾辞の両方が付加される「両分接辞（konfiks）peng-...-an」が2語から成る複合語に付く場合、規範文法規則（EYD）により分かち書きを解消して1語に連結表記（`pengambilalihan`）します。"
            }
        ],
        "culture_column": {
            "title": "「Ambil Hati」にみるインドネシアの人間関係の妙技",
            "body": "インドネシア社会において `ambil hati`（直訳：心を取る）は、義理の両親や上司、地域の長老に対して細やかな気配りや丁寧な挨拶（sopan santun）を重ね、愛顧と信頼を勝ち取るポジティブな処世術として語られます。英語の「butter someone up（お世辞を言ってご機嫌を取る）」のような下心のみならず、調和（rukun）を何より尊ぶ東南アジア的共同体への温かい融和行動という文化的含意を持っています。"
        }
    },
    {
        "filename": "docs/lexicon/02-verb-collocations-buat.md",
        "title": "【共起連語】語根 buat の必須コロケーション辞典：buat janji / buat keputusan / buat gara-gara",
        "root": "buat",
        "meaning": "作る、行う、〜のために（前置詞）",
        "core_concept": "「ゼロから形あるものを創出する・作り上げる」意味合いから、「人との約束を取り付ける」「トラブルや騒ぎを引き起こす」「過ちを犯す」など、人間関係や社会的な事象を能動的に生じさせる多面的な共起パターンを形成します。",
        "table_rows": [
            ("buat janji", "約束を作る", "予約をする、アポイントを取る、約束を交わす", "日常/ビジネス", "Saya ingin membuat janji temu dengan dokter spesialis jantung besok pagi."),
            ("buat keputusan", "決定を作る", "決断を下す、意思決定する（ambil keputusanと同義）", "一般/ビジネス", "Kita tidak boleh membuat keputusan secara sepihak tanpa musyawarah."),
            ("buat gara-gara", "口実・口火を作る", "揉め事の種を蒔く、問題を起こす、騒動の口火を切る", "口語/日常", "Anak itu suka sekali membuat gara-gara hingga tetangga merasa terganggu."),
            ("buat onar", "騒乱・騒ぎを作る", "治安を乱す、暴れる、騒ぎを起こす", "報道/警察", "Sekelompok pemuda diamankan polisi karena diduga membuat onar di tempat umum."),
            ("buat salah", "間違いを作る", "誤りを犯す、手落ちをする", "一般/道徳", "Wajar jika manusia pernah berbuat salah, yang terpenting adalah mau memperbaikinya."),
            ("buat kaget", "驚きを作る", "びっくりさせる、驚嘆させる", "口語/日常", "Suara petir yang menggelegar tiba-tiba membuat kaget semua orang di ruangan."),
            ("buat rugi", "損失を作る", "赤字を出す、損をさせる", "商用/ビジネス", "Keputusan investasi yang gegabah itu justru membuat rugi perusahaan ratusan juta.")
        ],
        "details": [
            {
                "term": "buat janji (membuat janji temu)",
                "trans": "予約をする、アポイントを取る",
                "nuance": "病院の診療予約、ビジネスの面談アポ、友人との約束など、時間と場所をすり合わせて合意を形成する場面の万能表現です。",
                "ex_id": "Sebelum datang ke kantor kedutaan, pemohon wajib membuat janji temu secara daring.",
                "ex_kana": "スブルム ダタン ケ カントール クドゥタアン、プモホン ワジブ ムンブアット ジャンジ トゥム スチャラ ダリン",
                "ex_ja": "大使館を訪れる前に、申請者はオンラインで面談予約（アポイント）を取らなければなりません。",
                "note": "親しい間柄なら `janjian`（約束する）というくだけた派生語もよく使われます。"
            },
            {
                "term": "buat gara-gara (memicu masalah)",
                "trans": "揉め事の口火を切る、わざわざ問題を起こす",
                "nuance": "`gara-gara` は「〜のせいで（原因）」を指す名詞で、平和な状態にあえて波風を立てる厄介者に対して苛立ちを込めて用います。",
                "ex_id": "Jangan coba-coba membuat gara-gara di lingkungan ini kalau tidak ingin berurusan dengan warga.",
                "ex_kana": "ジャンガン チョバチョバ ムンブアット ガラガラ ディ リングクンガン イニ カロウ ティダッ インギン ブルウルスサン ドゥンガン ワルガ",
                "ex_ja": "住民たちと揉め事を起こしたくないのなら、この地域で騒ぎの種を蒔くような真似はするな。",
                "note": "非難のニュアンスが強く含まれるイディオムです。"
            },
            {
                "term": "buat onar (membuat keributan)",
                "trans": "騒乱を起こす、暴れる、治安を乱す",
                "nuance": "`onar` は「騒動・混乱・不穏」を意味し、デモ隊の一部暴徒化や繁華街での喧嘩など、警察や治安維持が介入するレベルの社会的不穏を指します。",
                "ex_id": "Pihak kepolisian bertindak cepat membubarkan massa yang mulai membuat onar di depan gedung parlemen.",
                "ex_kana": "ピハッ クポリシアン ブルティンダッ チパット ムンブバルカン マッサ ヤン ムライ ムンブアット オナル ディ ドゥパン グドゥン パルレメン",
                "ex_ja": "警察当局は議会ビルの前で騒乱を起こし始めた群衆を速やかに解散させました。",
                "note": "新聞やテレビニュースで極めて頻繁に見かける報道語彙です。"
            },
            {
                "term": "berbuat salah (melakukan kekeliruan)",
                "trans": "間違いを犯す、悪事に手を染める",
                "nuance": "`buat` に自動詞接頭辞 `ber-` が付いた `berbuat` は「振る舞う、行動する（morally act）」を意味し、倫理的・道徳的な過ちや罪を語る際に用いられます。",
                "ex_id": "Memaafkan orang yang telah berbuat salah kepada kita adalah cermin kematangan budi pekerti.",
                "ex_kana": "ムマアフカン オラン ヤン トゥラー ブルブアット サラー クパダ キタ アダラー チェルミン クマタンガン ブディ プクルティ",
                "ex_ja": "自分に対して過ちを犯した者を許すことは、人格の成熟の表れです。",
                "note": "`berbuat baik`（善行を積む）の対義表現としてペアで覚えられます。"
            },
            {
                "term": "buat rugi / bikin rugi",
                "trans": "損失を被らせる、赤字を生じさせる",
                "nuance": "ビジネスにおける損失だけでなく、「人の親切を無駄にする」「台無しにする」という文脈でも使われます。口語では `bikin rugi` と `bikin` が代替します。",
                "ex_id": "Kerusakan mesin pabrik yang terlambat diperbaiki telah membuat rugi operasional hingga miliaran rupiah.",
                "ex_kana": "クルサカン ムシン パブリック ヤン トゥルランバット ディプルバイキ トゥラー ムンブアット ルギ オペラシオナル ヒンガ ミリアラン ルピア",
                "ex_ja": "修理が遅れた工場の機械故障により、数十億ルピア規模の事業運営損失が生じました。",
                "note": "口語では `bikin` が `buat` の使役（〜させる）用法として圧倒的に普及しています。"
            }
        ],
        "dialogue": {
            "title": "オフィスでの顧客トラブルとアポ調整",
            "lines": [
                ("Rian", "Dewi, apakah klien dari Surabaya sudah membuat janji untuk pertemuan evaluasi proyek minggu depan?"),
                ("Dewi", "Sudah, Pak. Namun ada sedikit insiden, staf magang kita kemarin sempat berbuat salah saat mengirim berkas rahasia."),
                ("Rian", "Aduh, jangan sampai hal sepele itu membuat gara-gara yang merusak kepercayaan mereka."),
                ("Dewi", "Tenang, Pak. Saya sudah langsung mengklarifikasi dan meminta maaf, sehingga tidak sampai membuat rugi kedua belah pihak.")
            ],
            "trans": [
                ("リアン", "デウィさん、スラバヤのクライアントは来週のプロジェクト評価会議のアポ（buat janji）を取りましたか？"),
                ("デウィ", "はい、課長。ただ少しインシデントがありまして、インターン生が昨日機密ファイルの送信で過ちを犯してしまいました。"),
                ("リアン", "おいおい、そんな些細なことで信頼を損なう揉め事（buat gara-gara）に発展させないでくれよ。"),
                ("デウィ", "ご安心ください。私が即座に事情説明と謝罪を行いましたので、双方に損失（buat rugi）が生じる事態は免れました。")
            ]
        },
        "grammar_points": [
            "**buat（動詞） vs buat（前置詞）**: `buat` は連語を作る動詞（作る・引き起こす）だけでなく、口語の前置詞 `untuk`（〜のために、〜向けに）の口語形としても極めて多用されます（例: `Kue ini buat kamu.` ＝ このケーキは君用だよ）。文脈における統語的位置で見極めましょう。",
            "**berbuat（道徳的行為）**: 単なる制作を表す `membuat` と異なり、`berbuat` は `berbuat baik`（善をなす）, `berbuat dosa`（罪を犯す）, `berbuat jahat`（悪事を働く）のように道徳・倫理を帯びた動詞として機能します。"
        ],
        "quizzes": [
            {
                "q": "「警察は路上で暴れていた若者グループを拘束した」の文脈で空欄に入る名詞はどれか。\n「Polisi mengamankan sekelompok pemuda yang membuat ________ di jalan raya.」",
                "choices": ["janji", "onar", "hati", "alih"],
                "ans": "onar",
                "expl": "治安を乱す、暴れる、騒乱を起こすという警察報道の決まり文句は `membuat onar` です。`membuat janji` は予約、`ambil hati` は歓心を買う、`ambil alih` は買収です。"
            },
            {
                "q": "ビジネスで「面談予約（アポイント）を取り付ける」を意味する最も自然な表現はどれか。",
                "choices": ["membuat gara-gara", "membuat janji temu", "membuat onar", "berbuat salah"],
                "ans": "membuat janji temu",
                "expl": "「アポイントを取る、面会予約をする」は `membuat janji temu`（または `membuat janji`）です。"
            },
            {
                "q": "次のうち、道徳的・倫理的な行動を表す自動詞 `berbuat` と正しく共起する組み合わせはどれか。",
                "choices": ["berbuat meja", "berbuat mobil", "berbuat kebajikan", "berbuat kantor"],
                "ans": "berbuat kebajikan",
                "expl": "`berbuat` は物理的な物体制作（meja, mobil, kantor）には使えず、道徳的行動（kebajikan: 善行・徳、dosa: 罪、salah: 過ち）と結びつきます。"
            }
        ],
        "culture_column": {
            "title": "「Bikin」と「Buat」の使い分けにみるジャカルタ口語の浸透",
            "body": "標準語では `membuat` や `menyebabkan`（引き起こす・〜させる）と書かれる場面でも、ジャカルタ方言の影響を受けた口語空間では動詞 `bikin` が圧倒的な存在感を放ちます（`bikin kesal`＝イラつかせる、`bikin pusing`＝頭を悩ませる）。しかし公式文書、論文、格調高いビジネス文書では依然として `membuat keputusan` や `berbuat kesalahan` のように `buat` 系の正則語彙が規範的敬意を担保します。"
        }
    },
    {
        "filename": "docs/lexicon/03-verb-collocations-buka.md",
        "title": "【共起連語】語根 buka の必須コロケーション辞典：buka suara / buka usaha / buka puasa / buka jalan",
        "root": "buka",
        "meaning": "開ける、開く、開始する、公開する",
        "core_concept": "「閉ざされていた扉や蓋を開く」という原初的イメージから、「事業を創業する」「沈黙を破って発言する」「断食を明ける」「可能性を切り拓く」という社会・経済・宗教的転換点を示す連語を豊富に生み出します。",
        "table_rows": [
            ("buka suara", "声を開く", "沈黙を破って証言・発言する、口を開く", "時事/報道", "Mantan pejabat tersebut akhirnya buka suara terkait skandal suap yang menjeratnya."),
            ("buka usaha", "事業を開く", "起業する、店・ビジネスを始める", "経済/ビジネス", "Banyak anak muda di kota besar memilih buka usaha kedai kopi kekinian."),
            ("buka puasa", "断食を開く", "日没後の食事をとる、断食を解く", "宗教/文化", "Keluarga besar berkumpul di rumah nenek untuk merayakan buka puasa bersama."),
            ("buka jalan", "道を開く", "活路を開く、可能性を切り拓く、道を譲る", "比喩/一般", "Inovasi teknologi kecerdasan buatan telah buka jalan bagi efisiensi industri manufaktur."),
            ("buka pintu", "扉を開く", "受け入れる、対話の余地を残す、歓迎する", "外交/政治", "Pemerintah tetap membuka pintu dialog damai dengan kelompok separatis."),
            ("buka rahasia", "秘密を開く", "秘密を暴露する、打ち明ける", "日常/慣用", "Jangan sekali-kali membuka rahasia perusahaan kepada pihak pesaing."),
            ("buka bersama (bukber)", "一緒に開く", "ラマダーン期間中の合同食事会", "大衆文化", "Alumni sekolah kami mengadakan acara buka bersama sekaligus reuni akbar.")
        ],
        "details": [
            {
                "term": "buka suara (angkat bicara)",
                "trans": "沈黙を破って口を開く、真相を語る",
                "nuance": "汚職スキャンダル、事件、論争などでそれまで黙秘していた当事者や目撃者が、公の場や記者会見で初めて証言する劇的瞬間を指す報道の超頻出表現です。",
                "ex_id": "Setelah berminggu-minggu menghilang dari media, sang artis akhirnya buka suara perihal perceraiannya.",
                "ex_kana": "ステラ ブルミングミング クヒランガン ダリ メディア、サン アルティス アヒルニャ ブカ スアラ プリアル プルチェライアンニャ",
                "ex_ja": "数週間にわたりメディアの前から姿を消していたその俳優は、自身の離婚問題についてついに口を開きました。",
                "note": "類語に `angkat bicara`（発言する）があります。"
            },
            {
                "term": "buka usaha (merintis bisnis)",
                "trans": "起業する、商売を始める",
                "nuance": "大企業設立から個人商店、屋台（kaki lima）の開業まで幅広く使われ、雇用創出や自己実現の象徴的フレーズです。",
                "ex_id": "Pemerintah memberikan bantuan modal bergulir bagi UMKM yang ingin membuka usaha mandiri.",
                "ex_kana": "プムリンター ムンブリカン バントゥアン モダル ブルギュリル バギ ウエムカエム ヤン インギン ムンブカ ウサハ マンディリ",
                "ex_ja": "政府は自立した起業を目指す零細・中小企業（UMKM）に対し、回転型支援資金を提供しています。",
                "note": "名詞形は `pembukaan usaha`（開業・創業）です。"
            },
            {
                "term": "buka puasa (ifthar)",
                "trans": "断食明けの食事をとる、断食を解く",
                "nuance": "イスラム教の断食月（ラマダーン）において、日没（マグリブの礼拝）を告げるアザーンとともに水分やナツメヤシ（kurma）を口にする神聖な儀礼です。",
                "ex_id": "Warga memadati pusat jajanan pasar menjelang waktu buka puasa untuk berburu takjil manis.",
                "ex_kana": "ワルガ ムマダティ プサット ジャジャナン パサール ムンジュラン ワクトゥ ブカ プアサ ウントゥッ ブルブル タクジル マニス",
                "ex_ja": "市民たちは日没の断食明けの時刻を前に、甘いおやつ（タクジル）を買い求めるため屋台市場に殺到しました。",
                "note": "友人や同僚と大勢で集まる食事会は `bukber` (buka bersama) と略称されます。"
            },
            {
                "term": "buka jalan (membuka peluang)",
                "trans": "活路を切り拓く、道を拓く",
                "nuance": "物理的な道路開通だけでなく、「新たな可能性や解決策をもたらす先駆的役割を果たす」という抽象的賛辞として使われます。",
                "ex_id": "Penandatanganan perjanjian perdagangan bebas ini diharapkan membuka jalan bagi ekspor produk lokal ke Eropa.",
                "ex_kana": "プナンダタンガナン プルジャンジアン プルダガンガン ベバス イニ ディハラプカン ムンブカ ジャラン バギ エクスポール プロドゥッ ロカル ケ エロパ",
                "ex_ja": "この自由貿易協定の締結は、地元製品の欧州向け輸出への道を切り拓くものと期待されています。",
                "note": "障害を取り除いて進行を促すメタファーです。"
            },
            {
                "term": "buka pintu (terbuka terhadap mediasi)",
                "trans": "対話の門戸を開く、受入れ態勢をとる",
                "nuance": "対立する相手に対して拒絶せず、外交交渉や和解のテーブルに着く用意があることを示す政治・ビジネスの定型句です。",
                "ex_id": "Pihak manajemen pabrik selalu membuka pintu selebar-lebarnya untuk berdiskusi dengan serikat buruh.",
                "ex_kana": "ピハッ マナジェメン パブリック スラル ムンブカ ピントゥ スレバールレバールニャ ウントゥッ ブルディスクシ ドゥンガン スリカット ブルフ",
                "ex_ja": "工場経営陣は労働組合との協議に向け、常に門戸を最大限に広げて（歓迎して）います。",
                "note": "`membuka pintu selebar-lebarnya`（門戸を大きく開く）という強調表現が定石です。"
            }
        ],
        "dialogue": {
            "title": "ラマダーン期のビジネスと若者の起業相談",
            "lines": [
                ("Farhan", "Bulan puasa tahun ini omzet restoranmu bagaimana, Dimas?"),
                ("Dimas", "Alhamdulillah meningkat drastis, apalagi paket buka puasa bersama selalu penuh dipesan sejak sore."),
                ("Farhan", "Hebat! Kesuksesan ini pasti membuka jalan bagimu untuk buka usaha cabang baru di luar kota."),
                ("Dimas", "Insya Allah. Kuncinya adalah mendengarkan saran pelanggan dan tidak ragu buka suara jika ada kendala pasokan.")
            ],
            "trans": [
                ("ファルハン", "今年の断食月、ディマス君のレストランの売上はどうだい？"),
                ("ディマス", "おかげさまで劇的に伸びています。特に合同断食明け（bukber）コースは夕方から常に満席予約ですよ。"),
                ("ファルハン", "素晴らしい！この成功は、君が地方都市に新規店舗を出店する（buka usaha）道を間違いなく切り拓く（buka jalan）ね。"),
                ("ディマス", "そう願っています。お客様の声を聴き、仕入れに問題があれば躊躇なく声を上げる（buka suara）ことが秘訣です。")
            ]
        },
        "grammar_points": [
            "**meN- の鼻音化と保持**: `buka` の語根頭文字は `b` です。接頭辞 `meN-` が付加されると、有声音 `b` は脱落せずそのまま保持され `membuka`（ムンブカ）となります（※無声音 p との対比: `pakai` → `memakai`）。",
            "**複合名詞・略語現象**: `buka puasa bersama` は現代インドネシア語の略語文化（akronim）の典型であり、日常会話やSNS上では `bukber`（ブッベル）というキャッチーな1語として完全に定着しています。"
        ],
        "quizzes": [
            {
                "q": "「汚職容疑者はついに法廷で沈黙を破り、資金の流れを暴露した」の文脈で適切な動詞句はどれか。\n「Tersangka kasus korupsi itu akhirnya ________ di persidangan.」",
                "choices": ["tutup mulut", "buka suara", "ambil alih", "buang waktu"],
                "ans": "buka suara",
                "expl": "沈黙を破って発言・証言する意味のコロケーションは `buka suara` です。`tutup mulut` は逆に口を閉ざす・黙秘する、`ambil alih` は買収する、`buang waktu` は時間を無駄にするです。"
            },
            {
                "q": "断食明けを友人や同僚と祝う合同食事会を指す大衆的な略語（akronim）はどれか。",
                "choices": ["bukber", "mudik", "takjil", "sahur"],
                "ans": "bukber",
                "expl": "`buka bersama`（合同断食明け食事会）の頭文字を合成した略語が `bukber` です。`takjil` は断食明け直後の軽食、`sahur` は夜明け前の食事、`mudik` は帰省です。"
            },
            {
                "q": "「科学技術の革新は、再生可能エネルギー普及への活路を開いた」を表す最も適切な表現はどれか。",
                "choices": ["membuka jalan bagi penyebaran energi terbarukan", "menutup pintu peluang energi hijau", "mengambil hati para peneliti iklim", "membuat onar di sektor ketenagakerjaan"],
                "ans": "membuka jalan bagi penyebaran energi terbarukan",
                "expl": "「〜への活路・可能性を切り拓く」は `membuka jalan bagi...` と共起します。"
            }
        ],
        "culture_column": {
            "title": "ラマダーンを彩る「Bukber」と「Takjil」の社交文化",
            "body": "インドネシアの断食月（Bulan Ramadhan）において、`buka puasa` は単なる禁食の解除にとどまらず、旧友、職場の同僚、親族との絆を再確認する最大のソーシャルイベントとなります。日没の1時間ほど前から街角路地に無数の露店が並び、甘いバナナのココナッツ煮（kolak pisang）や揚げ物（gorengan）といった `takjil` を買い求める人々で賑わう「ngabuburit（日没を待つ散策）」は、インドネシアの温かな風物詩です。"
        }
    },
    {
        "filename": "docs/lexicon/04-verb-collocations-tutup.md",
        "title": "【共起連語】語根 tutup の必須コロケーション辞典：tutup mulut / tutup mata / tutup usia / tutup buku",
        "root": "tutup",
        "meaning": "閉じる、閉める、覆う、塞ぐ、終える",
        "core_concept": "「物理的に空間や隙間を遮断する」動作から、「口を閉ざして黙秘する」「見て見ぬふりをする」「生涯の幕を閉じる（逝去する）」「会計帳簿を締める」という、終焉や遮断に関わる格調高いメタファーを形成します。",
        "table_rows": [
            ("tutup mulut", "口を閉じる", "口をつぐむ、黙秘する、口止めする", "口語/事件", "Saksi kunci itu memilih tutup mulut karena takut mendapat ancaman teror."),
            ("tutup mata", "目を閉じる", "見て見ぬふりをする、無視する、永眠する", "慣用/比喩", "Aparat penegak hukum tidak boleh tutup mata terhadap peredaran narkoba."),
            ("tutup usia", "年齢を閉じる", "逝去する、他界する、息を引き取る", "丁寧/追悼", "Sastrawan legendaris tanah air telah tutup usia pada umur 85 tahun."),
            ("tutup buku", "本・帳簿を閉じる", "決算を行う、帳簿を締め切る、過去を清算する", "会計/ビジネス", "Bagian keuangan perusahaan sedang sibuk menyelesaikan proses tutup buku akhir tahun."),
            ("tutup telinga", "耳を塞ぐ", "耳を貸さない、忠告を頑なに無視する", "慣用句", "Pemimpin yang otoriter cenderung tutup telinga terhadap aspirasi rakyat kecil."),
            ("tutup pintu", "扉を閉ざす", "拒絶する、交渉を打ち切る、締め出す", "外交/交渉", "Pemerintah menutup pintu ekspor bijih mentah demi mendorong hilirisasi."),
            ("tutup aurat", "恥部を覆う", "イスラムの教義に従い肌・髪を覆う（ヒジャブ着用）", "宗教/生活", "Banyak wanita muslim mulai membiasakan diri untuk menutup aurat sejak remaja.")
        ],
        "details": [
            {
                "term": "tutup mulut (membungkam / bungkam)",
                "trans": "口をつぐむ、黙秘する、口封じをする",
                "nuance": "自発的に秘密を守る文脈だけでなく、買収金（uang tutup mulut）を渡されて口封じされる文脈でも頻繁に登場します。",
                "ex_id": "Pelaku menyuap petugas keamanan dengan sejumlah uang tutup mulut agar aksinya tidak dilaporkan.",
                "ex_kana": "プラク ムニュアップ プトゥガス クアマナン ドゥンガン スジュムラー ウアン トゥトゥップ ムルット アガル アクシニャ ティダッ ディラポールカン",
                "ex_ja": "犯人は自らの犯行を通報されないよう、警備員に口止め料（uang tutup mulut）を渡して買収しました。",
                "note": "`uang tutup mulut`（口止め料・賄賂）は警察・司法報道で頻出する成句です。"
            },
            {
                "term": "tutup mata (pura-pura tidak tahu / wafat)",
                "trans": "見て見ぬふりをする、黙認する / 永眠する",
                "nuance": "第一の意味は「目の前で行われている不正や不正義に気づきながら無視を決め込むこと」。第二の意味（文脈次第）では詩的に「永遠の眠りにつく（死ぬ）」を表します。",
                "ex_id": "Kita tidak boleh tutup mata terhadap ketimpangan sosial yang semakin melebar di sekitar kita.",
                "ex_kana": "キタ ティダッ ボレ トゥトゥップ マタ トゥルハダップ クティムパンガン ソシアル ヤン スマキン ムレバール ディ スキタール キタ",
                "ex_ja": "私たちは、身の回りでますます拡大する社会的不平等を見て見ぬふりをしてはなりません。",
                "note": "非難の文脈では圧倒的に「黙認・放置」の意味で用いられます。"
            },
            {
                "term": "tutup usia (meninggal dunia / wafat)",
                "trans": "逝去する、他界する、生涯を閉じる",
                "nuance": "`meninggal dunia`（死去する）や `mati`（死ぬ）よりも遥かに格調高く、敬意を込めた婉曲表現（eufemisme）として、訃報記事（obituari）の公式定型句です。",
                "ex_id": "Mantan presiden yang berjasa besar bagi bangsa itu dikabarkan tutup usia di rumah sakit militer.",
                "ex_kana": "マンタン プレシデン ヤン ブルジャサ ブサール バギ バンサ イトゥ ディカバルカン トゥトゥップ ウシア ディ ルマー サキット ミリテル",
                "ex_ja": "国家に多大な功績を残した元大統領が、軍病院で逝去されたと報じられました。",
                "note": "国家元首や著名文化人の訃報見出しには必ずこの表現が冠されます。"
            },
            {
                "term": "tutup buku (rekonsiliasi keuangan)",
                "trans": "帳簿を締める、期末決算を終える",
                "nuance": "経理・会計の実務用語として、月末や年度末に全ての財務取引を集計・確定させる作業を指します。転じて人生や過去の区切りをつける際にも使われます。",
                "ex_id": "Sebelum tutup buku kuartal keempat, semua divisi diminta menyerahkan laporan pertanggungjawaban anggaran.",
                "ex_kana": "スブルム トゥトゥップ ブク クアルタル クウンパット、スムア ディヴィシ ディミンタ ムニェラカン ラポラン プルタングンジャワバン アンガラン",
                "ex_ja": "第4四半期の帳簿締め（決算）の前に、全事業部は予算執行報告書を提出するよう求められました。",
                "note": "会計ソフトの操作メニューにも `Tutup Buku Akhir Tahun` と表示されます。"
            },
            {
                "term": "tutup telinga (mengabaikan teguran)",
                "trans": "耳を塞ぐ、聞く耳を持たない",
                "nuance": "他者からの忠告、忠言、市民の抗議の声を意図的・頑迷に聞き流す姿勢を厳しく批判する際に用いられます。",
                "ex_id": "Jangan sampai manajemen perusahaan tutup telinga terhadap keluhan para pekerja mengenai upah lembur.",
                "ex_kana": "ジャンガン サンパイ マナジェメン プルサハアン トゥトゥップ トゥリンガ トゥルハダップ クルハン パラ プクルジャ ムンゲナイ ウパ ルンブル",
                "ex_ja": "企業経営陣が、残業代に関する労働者たちの苦情に聞く耳を持たないような事態があってはなりません。",
                "note": "反省や改善を拒否する態度を表す比喩です。"
            }
        ],
        "dialogue": {
            "title": "企業の年度末決算と元役員の訃報",
            "lines": [
                ("Agus", "Wati, apakah proses tutup buku keuangan tahun ini sudah selesai semuanya?"),
                ("Wati", "Hampir selesai, Pak. Hanya tinggal mencocokkan beberapa kuitansi audit eksternal."),
                ("Agus", "Bagus. Oya, tadi saya mendengar kabar duka bahwa pendiri yayasan kita telah tutup usia tadi subuh."),
                ("Wati", "Innalillahi, beliau orang yang sangat dermawan dan tidak pernah tutup mata jika ada karyawan yang kesulitan.")
            ],
            "trans": [
                ("アグス", "ワティさん、今年の財務の帳簿締め（tutup buku）はすべて完了しましたか？"),
                ("ワティ", "ほぼ完了しました、部長。あとは外部監査の領収書を数件照合するだけです。"),
                ("アグス", "良かった。ところで、今朝がた当財団の創設者が逝去された（tutup usia）という訃報を耳にしたよ。"),
                ("ワティ", "ご冥福をお祈りします。あの方は大変慈悲深く、困窮している社員がいれば決して見て見ぬふりをしない（tutup mata）素晴らしい方でした。")
            ]
        },
        "grammar_points": [
            "**meN- 変化時の鼻音化**: `tutup` の語頭子音は無声音 `t` です。接頭辞 `meN-` が付くと、`t` が鼻音 `n` に置換されて `menutup`（ムヌトゥップ）となります（例: `menutup pintu`, `menutup mata`）。",
            "**婉曲表現としての tutup usia**: 人の死を直接的に `mati` と表現することは人間に対して非常に無礼とみなされます。日常では `meninggal dunia`、報道や公式追悼では `tutup usia` や `wafat`、`berpulang ke rahmatullah` を使い分けるのがインドネシア語の教養です。"
        ],
        "quizzes": [
            {
                "q": "新聞の訃報欄で「著名なノーベル賞学者が逝去された」を格調高く伝える表現はどれか。\n「Ilmuwan peraih Nobel itu telah ________ pada usia 90 tahun.」",
                "choices": ["tutup buku", "tutup usia", "tutup mulut", "tutup mata"],
                "ans": "tutup usia",
                "expl": "人の死に対する格調高い婉曲表現（他界・逝去）は `tutup usia` です。`tutup buku` は決算・帳簿締め、`tutup mulut` は口封じ・沈黙です。"
            },
            {
                "q": "「口止め料、秘密を保つための賄賂」を意味するインドネシア語の成句はどれか。",
                "choices": ["uang tutup mulut", "uang tutup mata", "uang buka usaha", "uang buang air"],
                "ans": "uang tutup mulut",
                "expl": "口外しないよう支払う口止め料は `uang tutup mulut` と呼ばれます。"
            },
            {
                "q": "「社会問題や違法行為に気づいていながら、見て見ぬふりをする」を意味するイディオムはどれか。",
                "choices": ["tutup mata", "buka suara", "ambil alih", "tarik napas"],
                "ans": "tutup mata",
                "expl": "不正などを黙認する、見て見ぬふりをする慣用句は `tutup mata` です。"
            }
        ],
        "culture_column": {
            "title": "「Uang Tutup Mulut」と社会正義への戦い",
            "body": "汚職撲滅委員会（KPK）の摘発ニュース等でしばしば耳にする `uang tutup mulut`（口封じマネー）や `tutup mata`（官憲の黙認）は、長年インドネシア社会を苛んできた縁故主義（KKN）の象徴的フレーズでもあります。しかし民主化（Reformasi）以降、告発者（whistleblower）を保護する法整備が進み、SNSの普及によって「見て見ぬふりを許さない市民の監視の目」が不正の隠蔽を次々と暴く力となっています。"
        }
    },
    {
        "filename": "docs/lexicon/05-verb-collocations-tarik.md",
        "title": "【共起連語】語根 tarik の必須コロケーション辞典：tarik perhatian / tarik kesimpulan / tarik napas / tarik diri",
        "root": "tarik",
        "meaning": "引く、引っ張る、引き寄せる、引き出す",
        "core_concept": "「物理的に力を込めて手元へ引き寄せる」動作から、「人々の関心・注意を惹きつける」「議論から論理的結論を引き出す」「息を深く吸い込む」「組織や戦線から身を引く（撤退する）」という求心力と退避のメタファーへと展開します。",
        "table_rows": [
            ("tarik perhatian", "注意を引く", "注目・関心を惹きつける、関心を集める", "マーケ/一般", "Kampanye iklan kreatif itu berhasil menarik perhatian konsumen generasi muda."),
            ("tarik kesimpulan", "結論を引く", "結論を導き出す、総括する、結論づける", "学術/ビジネス", "Kita belum bisa menarik kesimpulan final sebelum seluruh data statistik terkumpul."),
            ("tarik napas", "息を引く", "深呼吸する、息を吸い込む、一息つく", "日常/心理", "Tarik napas dalam-dalam sebelum kamu mulai berbicara di depan panggung."),
            ("tarik diri", "自身を引く", "身を引く、撤退する、辞退する", "政治/ビジネス", "Kandidat itu memutuskan untuk menarik diri dari bursa pemilihan kepala daerah."),
            ("tarik ulur", "引いて緩める", "駆け引きする、綱引きをする、妥協点を探る", "政治/交渉", "Proses negosiasi perjanjian damai masih diwarnai tarik ulur kepentingan politik."),
            ("tarik dana / tarik uang", "資金・お金を引く", "預金を引き出す、出金する", "金融/生活", "Nasabah dapat menarik uang tunai di mesin ATM tanpa kartu menggunakan aplikasi."),
            ("tarik garis batas", "境界線を引く", "線引きをする、一線を画す、境界を定める", "比喩/一般", "Kita harus tegas menarik garis batas antara urusan profesional dan kehidupan pribadi.")
        ],
        "details": [
            {
                "term": "tarik perhatian (menarik minat / sorotan)",
                "trans": "注目を惹きつける、関心を引く",
                "nuance": "広告マーケティング、芸術作品、社会現象が多くの人々の関心や視線を集めるポジティブな状況で使われます。形容詞 `menarik`（魅力的な、面白い）の原点でもあります。",
                "ex_id": "Desain arsitektur gedung baru yang ramah lingkungan itu berhasil menarik perhatian para pakar tata kota.",
                "ex_kana": "デサイン アルシテクトゥル グドゥン バル ヤン ラマー リングクンガン イトゥ ブルハシル ムナリック プルハティアン パラ パカール タタ コタ",
                "ex_ja": "環境に配慮したその新築ビルの建築デザインは、都市計画の専門家たちの注目を大いに惹きつけました。",
                "note": "`menarik perhatian publik`（世間の注目を集める）という成句が定番です。"
            },
            {
                "term": "tarik kesimpulan (menyimpulkan)",
                "trans": "結論を導き出す、総括する",
                "nuance": "実験結果、アンケート分析、長時間の議論などの根拠に基づいて、客観的・論理的な帰結を導き出す学術・ビジネスの必須語彙です。",
                "ex_id": "Berdasarkan hasil uji laboratorium, para peneliti dapat menarik kesimpulan bahwa air sungai tersebut tidak tercemar.",
                "ex_kana": "ブルダサルカン ハシル ウジ ラボラトリウム、パラ プヌリティ ダパット ムナリック クシムプラン バフワ アイル スンガイ トゥルスブット ティダッ トゥルチェマル",
                "ex_ja": "実験室での検査結果に基づき、研究者たちはその川の水は汚染されていないという結論を導き出すことができました。",
                "note": "名詞 `kesimpulan`（結論）と強固にコロケーションします。"
            },
            {
                "term": "tarik napas (menghirup udara)",
                "trans": "息を吸い込む、深呼吸する、安堵する",
                "nuance": "緊張をほぐすための物理的な深呼吸だけでなく、`tarik napas lega`（胸をなでおろす・安堵のため息をつく）という心理的安堵の表現としても重宝されます。",
                "ex_id": "Setelah presentasi selesai dan klien tampak puas, seluruh anggota tim akhirnya bisa menarik napas lega.",
                "ex_kana": "ステラ プレゼンタシ スルサイ ダン クライエン タンパック プアス、スルルフ アンゴタ ティム アヒルニャ ビサ ムナリック ナパス レガ",
                "ex_ja": "プレゼンが終わりクライアントが満足そうに見えたのを見て、チームメンバー全員がついに安堵の息をつく（胸をなでおろす）ことができました。",
                "note": "`menarik napas panjang`（長いため息をつく / 観念する）も頻出です。"
            },
            {
                "term": "tarik ulur (negosiasi alot)",
                "trans": "綱引きをする、激しい駆け引きをする",
                "nuance": "直訳は「凧糸などを引いては緩めること」。利害が激しく対立する労使交渉、政党間の連立協議、領有権交渉などで、双方が一歩も引かず妥協を探る膠着状態を描写します。",
                "ex_id": "Setelah melalui tarik ulur yang alot selama berbulan-bulan, kedua negara akhirnya menyepakati perbatasan laut.",
                "ex_kana": "ステラ ムラルイ タリック ウルル ヤン アロット スラマ ブルブランブラン、クドゥア ネガラ アヒルニャ ムニェパカティ プルバタサン ラウト",
                "ex_ja": "数ヶ月に及ぶ難航した綱引き（激しい駆け引き）を経て、両国はついに海洋境界線で合意に達しました。",
                "note": "「Alot（噛み切れないほど硬い＝難航した）」という形容詞と極めて頻繁に共起します。"
            },
            {
                "term": "tarik diri (mengundurkan diri)",
                "trans": "撤退する、身を引く、出場を辞退する",
                "nuance": "大会、選挙戦、係争中の案件から自発的に降りることを表します。公的な辞任は `mengundurkan diri` ですが、戦略的・状況的な身の引き方は `menarik diri` と表現されます。",
                "ex_id": "Perusahaan multinasional itu memutuskan menarik diri dari proyek tambang demi menjaga reputasi lingkungan.",
                "ex_kana": "プルサハアン ムルティナシオナル イトゥ ムムトゥスカン ムナリック ディリ ダリ プロイェッ タンバン デミ ムンジャガ レプタシ リングクンガン",
                "ex_ja": "その多国籍企業は、環境に関する企業評価（レピュテーション）を守るため鉱山プロジェクトから撤退することを決定しました。",
                "note": "紛争地域からの軍隊の撤収（penarikan pasukan）などにも使われます。"
            }
        ],
        "dialogue": {
            "title": "新商品プロモーションと経営陣の駆け引き",
            "lines": [
                ("Maya", "Bagaimana tanggapan audiens saat peluncuran prototipe aplikasi kita kemarin?"),
                ("Rudi", "Luar biasa! Fitur kecerdasan buatannya benar-benar berhasil menarik perhatian investor dan media."),
                ("Maya", "Syukurlah. Tetapi bagaimana dengan negosiasi pembagian saham dengan pihak pemodal?"),
                ("Rudi", "Masih ada sedikit tarik ulur mengenai persentase bagi hasil, namun kita jangan terburu-buru menarik kesimpulan sebelum kontrak final disusun.")
            ],
            "trans": [
                ("マヤ", "昨日のアプリ試作版の発表会、聴衆の反応はどうだった？"),
                ("ルディ", "凄まじかったよ！AI機能が投資家とメディアの関心を見事に惹きつけた（tarik perhatian）んだ。"),
                ("マヤ", "よかった。でも出資元との株式配分の交渉はどうなっているの？"),
                ("ルディ", "利益分配の比率についてまだ多少の綱引き（tarik ulur）があるけれど、最終契約が作成される前に拙速に結論を出す（tarik kesimpulan）べきではないね。")
            ]
        },
        "grammar_points": [
            "**meN- の鼻音化規則**: `tarik` の頭文字は無声音 `t` のため、接頭辞 `meN-` で `t` が `n` に変化して `menarik`（ムナリック）となります。この `menarik` は動詞「引く」だけでなく、「面白い・魅力的な」という形容詞としても辞書に単独見出しを持つほど発展しました。",
            "**tarik ulur の文法性**: `tarik ulur` は元々動詞の並置ですが、現代語では `tarik-ulur kepentingan`（利害の綱引き）のように、そのまま抽象名詞句として主語や前置詞の目的語に据えられます。"
        ],
        "quizzes": [
            {
                "q": "政治やビジネスの難航する交渉において「双方が譲歩せず駆け引き・綱引きを繰り返す状態」を表す成句はどれか。",
                "choices": ["tarik napas", "tarik ulur", "tarik kesimpulan", "tarik perhatian"],
                "ans": "tarik ulur",
                "expl": "利害をめぐる激しい駆け引きや綱引き状態を表す表現は `tarik ulur` です。"
            },
            {
                "q": "「実験や調査の全データが出揃う前に、早急に結論を下してはならない」を意味する適切な動詞句はどれか。\n「Jangan terburu-buru ________ sebelum seluruh bukti diverifikasi.」",
                "choices": ["menarik kesimpulan", "menarik perhatian", "menarik napas", "menarik uang"],
                "ans": "menarik kesimpulan",
                "expl": "「結論を導き出す」は `menarik kesimpulan` と共起します。"
            },
            {
                "q": "「危機を脱して胸をなでおろす、安堵の息をつく」を意味する成句はどれか。",
                "choices": ["tarik napas lega", "tarik diri", "tutup usia", "buat gara-gara"],
                "ans": "tarik napas lega",
                "expl": "安堵して息をつく、ホッとする表現は `tarik napas lega` です。"
            }
        ],
        "culture_column": {
            "title": "「Tarik Ulur」に見る凧揚げ（Layang-layang）の知恵",
            "body": "インドネシアの乾季の空を舞う伝統的な凧揚げ（main layangan）。強風に煽られた凧を墜落させず高く安定して保つには、糸を力任せに引くだけでも放っておくだけでもダメで、風力に応じて「引いては緩める（tarik ulur）」絶妙なバランス感覚が求められます。この日常の身体感覚が、対立を全面戦争に発展させず妥協の合意（mufakat）を目指すインドネシア特有の粘り強い政治交渉の美学へと昇華されているのです。"
        }
    },
    {
        "filename": "docs/lexicon/06-verb-collocations-pasang.md",
        "title": "【共起連語】語根 pasang の必須コロケーション辞典：pasang badan / pasang telinga / pasang aksi / pasang surut",
        "root": "pasang",
        "meaning": "取り付ける、設置する、構える、満ちる（潮）",
        "core_concept": "「部品や装置を定位置にセットする」「潮が満ちる」という基本語義から、「全身を盾にして立ち塞がる」「耳を澄ませて情報収集する」「気取ったポーズをとる」「栄枯盛衰の波を経験する」という、姿勢の構えや運命の起伏を表す連語へとダイナミックに派生します。",
        "table_rows": [
            ("pasang badan", "身体を据える", "身を挺する、盾になる、矢面に立つ", "政治/防衛", "Sang menteri siap pasang badan demi membela kebijakan subsidi rakyat kecil."),
            ("pasang telinga", "耳を据える", "耳を澄ます、聞き耳を立てる、情報収集に努める", "日常/慣用", "Warga pasang telinga baik-baik untuk mendengarkan pengumuman dari ketua RT."),
            ("pasang mata", "目を据える", "目を凝らす、監視の目を光らせる", "防犯/警戒", "Petugas keamanan tetap pasang mata memantau gerak-gerik orang yang mencurigakan."),
            ("pasang aksi", "演技・格好を据える", "気取る、ポーズをつける、カッコつける", "口語/俗語", "Pemuda itu suka pasang aksi dengan motor gedenya di depan para gadis."),
            ("pasang surut", "満ち潮と引き潮", "栄枯盛衰、波乱万丈、浮き沈み", "歴史/比喩", "Hubungan diplomatik kedua negara tetangga itu telah melewati berbagai pasang surut."),
            ("pasang tarif", "料金を据える", "料金を設定する、強気な相場を要求する", "商取引/口語", "Penyanyi papan atas itu mulai pasang tarif tinggi untuk sekali penampilan panggung."),
            ("pasang target", "目標を据える", "目標を設定する、ノルマを課す", "ビジネス/スポーツ", "Tim nasional sepak bola pasang target lolos ke putaran final Piala Dunia.")
        ],
        "details": [
            {
                "term": "pasang badan (rela berkorban / membela)",
                "trans": "身を挺する、矢面に立つ、責任を一身に背負う",
                "nuance": "批判や攻撃の嵐に晒されている部下や政策を守るため、自らが盾となって防御姿勢をとる政治家や指導者の覚悟を称える（あるいは揶揄する）決まり文句です。",
                "ex_id": "Sebagai kepala proyek, ia berani pasang badan ketika ada komplain keras dari masyarakat sekitar.",
                "ex_kana": "スバガイ クパラ プロイェッ、イア ブルアニ パサン バダン クティカ アダ コンプレイン クラス ダリ マシャラカット スキタール",
                "ex_ja": "プロジェクト責任者として、彼は周辺住民から厳しい苦情が出た際に敢然と身を挺して矢面に立ちました。",
                "note": "比喩的な勇敢さ、自己犠牲精神を表す極めて人気の高いイディオムです。"
            },
            {
                "term": "pasang surut (fluktuasi dinamika)",
                "trans": "栄枯盛衰、浮き沈み、紆余曲折",
                "nuance": "自然現象の「干満（満潮 air pasang と干潮 air surut）」から転じ、国家の歴史、企業の業績、人間関係の波乱万丈な変遷を壮大に語る際に用いられます。",
                "ex_id": "Perjalanan hidup seniman legendaris itu penuh dengan pasang surut sebelum akhirnya diakui dunia.",
                "ex_kana": "プルジャラナン ヒドゥップ スニマン レゲンバリス イトゥ プヌー ドゥンガン パサン スルット スブルム アヒルニャ ディアクイ ドゥニア",
                "ex_ja": "その伝説的芸術家の生涯は、世界に認められるまで紆余曲折（浮き沈み）に満ちたものでした。",
                "note": "`melewati pasang surut`（浮き沈みを乗り越える）という連語が定石です。"
            },
            {
                "term": "pasang telinga / pasang mata",
                "trans": "聞き耳を立てる / 目を光らせる",
                "nuance": "受動的に聞く・見るのではなく、感覚器官を特定の対象に向けて最大限に集中・研ぎ澄ませる意図的動作です。",
                "ex_id": "Pihak kepolisian meminta warga untuk tetap pasang mata dan telinga terhadap ancaman radikalisme.",
                "ex_kana": "ピハッ クポリシアン ムミンタ ワルガ ウントゥッ トゥタップ パサン マタ ダン トゥリンガ トゥルハダップ アンチャマン ラディカリズメ",
                "ex_ja": "警察当局は市民に対し、過激主義の脅威に対して常に目と耳を研ぎ澄ませておくよう要請しました。",
                "note": "警戒態勢（kewaspadaan）を呼びかける文脈でペアで頻出します。"
            },
            {
                "term": "pasang aksi (bergaya / pamer)",
                "trans": "カッコつける、見栄を張る、気取る",
                "nuance": "若者言葉や大衆会話において、周囲の注目を集めようとわざとらしい仕草をしたり、ブランド品や高級車を自慢げに見せびらかしたりする行動を指します。",
                "ex_id": "Jangan cuma bisa pasang aksi di media sosial, buktikan kinerjamu dengan prestasi nyata di lapangan.",
                "ex_kana": "ジャンガン チュマ ビサ パサン アクシ ディ メディア ソシアル、ブクティカン キネルジャム ドゥンガン プレスタシ ニャタ ディ ラパンガン",
                "ex_ja": "SNS上でカッコつけて見栄ばかり張るな、現場での具体的な成果で自分の実力を証明してみせろ。",
                "note": "皮肉や戒めのニュアンスを伴うことが多い表現です。"
            },
            {
                "term": "pasang target (menetapkan sasaran)",
                "trans": "目標を設定する、数値ノルマを掲げる",
                "nuance": "営業成績、工期、スポーツのメダル獲得数など、明確な数値指標を定めて全力を注入するビジネス・競技の定型句です。",
                "ex_id": "Divisi pemasaran pasang target kenaikan penjualan sebesar 20 persen untuk kuartal mendatang.",
                "ex_kana": "ディヴィシ プマサラン パサン ターゲット クナイカン プンジュアラン スブサール ドゥアプル パーセン ウントゥッ クアルタル ムンダタン",
                "ex_ja": "営業マーケティング部門は、次四半期に向けて売上高20％増の目標を設定しました。",
                "note": "口語・ビジネスで `menetapkan target` の簡潔な表現として愛用されます。"
            }
        ],
        "dialogue": {
            "title": "歴史ある老舗企業の再建と新社長の決意",
            "lines": [
                ("Hendra", "Perusahaan keluarga ini telah berdiri lebih dari setengah abad dan melewati banyak pasang surut perekonomian."),
                ("Linda", "Benar, Pak. Namun krisis digital saat ini menuntut kita untuk benar-benar berani pasang badan menghadapi resistensi internal."),
                ("Hendra", "Saya sebagai pimpinan siap pasang badan. Kita juga sudah pasang target agar platform e-commerce kita meluncur bulan depan."),
                ("Linda", "Luar biasa. Karyawan juga mulai pasang telinga dan antusias menyambut rencana transformasi ini.")
            ],
            "trans": [
                ("ヘンドラ", "この同族企業は半世紀以上存続し、経済の幾多の浮き沈み（pasang surut）を乗り越えてきた。"),
                ("リンダ", "その通りです、社長。しかし現在のデジタル危機を乗り越えるには、社内の抵抗に怯まず身を挺して矢面に立つ（pasang badan）覚悟が求められます。"),
                ("ヘンドラ", "私がトップとして矢面に立つ覚悟だ。来月には自社ECプラットフォームを立ち上げるべく目標も掲げた（pasang target）。"),
                ("リンダ", "頼もしいです。社員たちも聞き耳を立てて関心を寄せ（pasang telinga）、この変革プランを熱心に歓迎し始めています。")
            ]
        },
        "grammar_points": [
            "**meN- の無声音 p 鼻音化**: `pasang` の語頭は無声音 `p` です。接頭辞 `meN-` が付加されると `p` が脱落して鼻音 `m` と同化し、`memasang`（ムマサン）となります（例: `memasang iklan`＝広告を出す、`memasang lampu`＝電球を取り付ける）。",
            "**イディオムにおける語幹保持**: `pasang badan`, `pasang aksi`, `pasang surut` 等の慣用句では、文語であっても `meN-` を付けず語根 `pasang` のまま固定連語として扱われるケースが極めて多いのが特徴です。"
        ],
        "quizzes": [
            {
                "q": "「リーダーが批判や攻撃の嵐の中で、部下を守るために自ら矢面に立つ・盾になる」を意味する慣用句はどれか。",
                "choices": ["pasang badan", "pasang aksi", "pasang tarif", "pasang target"],
                "ans": "pasang badan",
                "expl": "自ら盾になって身を挺する、責任の矢面に立つ慣用句は `pasang badan` です。"
            },
            {
                "q": "「二国間の外交関係は、50年の歴史の中で幾多の浮き沈み（栄枯盛衰）を経験してきた」の空欄に入る表現はどれか。\n「Hubungan bilateral kedua negara telah melewati berbagai ________ selama setengah abad.」",
                "choices": ["tarik ulur", "pasang surut", "buka tutup", "tutup usia"],
                "ans": "pasang surut",
                "expl": "歴史や関係性の浮き沈み、紆余曲折を表す連語は `pasang surut` です。"
            },
            {
                "q": "「注意深く耳を澄ます、聞き耳を立てて情報を集める」を意味する慣用表現はどれか。",
                "choices": ["pasang telinga", "tutup telinga", "ambil pusing", "buang waktu"],
                "ans": "pasang telinga",
                "expl": "耳を澄ませて情報に注意を払う表現は `pasang telinga` です。`tutup telinga` は聞く耳を持たない、です。"
            }
        ],
        "culture_column": {
            "title": "「Pasang Badan」に宿る指導者の美学（Ksatria）",
            "body": "インドネシアの政治文化や企業風土において、都合が悪くなると部下に責任を擦り付けて逃げる上司は最も軽蔑されます。逆に、現場の失策や摩擦に対して自ら先頭に立って盾となり、批判を一身に引き受ける姿勢はジャワの伝統的な武士道精神「ケサトリア（Ksatria / 騎士）」の美徳と重なります。`Pasang badan` という言葉には、単なる防衛を超えた深い倫理的威厳が宿っているのです。"
        }
    },
    {
        "filename": "docs/lexicon/07-verb-collocations-buang.md",
        "title": "【共起連語】語根 buang の必須コロケーション辞典：buang waktu / buang air / buang muka / buang sial",
        "root": "buang",
        "meaning": "捨てる、投げ捨てる、追放する、排泄する",
        "core_concept": "「不要になったゴミや異物を体外・圏外へ投げ捨てる」基本動詞から、「貴重な時間を浪費する」「見て見ぬふりをして顔を背ける」「生理的排泄を行う」「厄落としをして悪運を払う」という、物質・時間・人間関係・呪術的領域にまたがる多様な連語を生み出します。",
        "table_rows": [
            ("buang waktu", "時間を捨てる", "時間を無駄にする、時間を浪費する", "日常/一般", "Jangan buang waktu untuk memikirkan hal-hal negatif yang tidak bisa kamu kendalikan."),
            ("buang air", "水を捨てる", "トイレに行く、用を足す（小水・大便の排泄）", "生理/生活", "Di mana toilet umum terdekat? Saya sudah tidak tahan ingin buang air kecil."),
            ("buang muka", "顔を捨てる", "顔を背ける、無視する、見向きもしない", "心理/態度", "Ketika kami berpapasan di lorong kantor, dia malah buang muka seolah tidak kenal."),
            ("buang sial", "不運・厄を捨てる", "厄落としをする、不運を祓う、気分転換をする", "伝統/信仰", "Masyarakat mengadakan ritual mandi kembang di laut untuk buang sial."),
            ("buang uang", "お金を捨てる", "お金をドブに捨てる、無駄遣い・浪費する", "経済/口語", "Membeli barang mewah tiruan yang cepat rusak itu sama saja dengan buang uang."),
            ("buang sampah", "ゴミを捨てる", "ゴミを投棄する、ゴミ出しをする", "環境/日常", "Warga dilarang keras membuang sampah sembarangan di aliran sungai."),
            ("buang hajat", "用・必要を捨てる", "大便を排泄する、用を足す（改まった表現）", "丁寧/衛生", "Pemerintah membangun fasilitas sanitasi layak agar warga tidak buang hajat sembarangan.")
        ],
        "details": [
            {
                "term": "buang waktu (menyia-nyiakan waktu)",
                "trans": "時間を浪費する、無駄骨を折る",
                "nuance": "人生の限りある時間やプロジェクトの納期を、無意味な議論や怠惰で消費してしまうことを戒める定番の共起表現です。",
                "ex_id": "Membantah orang yang keras kepala di media sosial hanya akan buang waktu dan energi secara sia-sia.",
                "ex_kana": "ムンバンター オラン ヤン クラス クパラ ディ メディア ソシアル ハニャ アカン ブアン ワクトゥ ダン エネルギ スチャラ シアシエ",
                "ex_ja": "SNS上で頑固な人と議論しても、時間とエネルギーを無駄にするだけです。",
                "note": "`buang-buang waktu` と畳語にして浪費感を強調することもあります。"
            },
            {
                "term": "buang air kecil / besar (buang air)",
                "trans": "小水（おしっこ）/ 大便（うんち）をする、用を足す",
                "nuance": "排泄行為を直接的な下品な言葉で呼ばず、水（air）を使って清浄にする東南アジアの水洗習慣に根ざした上品な生理的表現です。",
                "ex_id": "Anak kecil itu minta izin kepada gurunya untuk buang air kecil ke kamar mandi.",
                "ex_kana": "アナッ クチル イトゥ ミンタ イジン クパダ グルニャ ウントゥッ ブアン アイル クチル ケ カマル マンディ",
                "ex_ja": "その幼い子どもは、トイレに小用（おしっこ）を足しに行く許可を先生に求めました。",
                "note": "省略して単に `buang air`（用を足す）とも言います。"
            },
            {
                "term": "buang muka (berpaling / pura-pura acuh)",
                "trans": "顔を背ける、あからさまに無視する",
                "nuance": "怒り、嫌悪、気まずさから、相手と視線を合わせないよう意図的に顔の向きを逸らす冷淡な身体的態度を描写します。",
                "ex_id": "Sejak perselisihan mengenai warisan itu mencuat, kedua saudara kandung itu selalu buang muka bila berpapasan.",
                "ex_kana": "スジャッ プルスリシハン ムンゲナイ ワリサン イトゥ ムンチュアット、クドゥア サウダラ カンドゥン イトゥ スラル ブアン ムカ ビラ ブルパパサン",
                "ex_ja": "遺産相続をめぐる争いが表面化して以来、その実の兄弟はすれ違っても常に顔を背け合っています。",
                "note": "軽蔑や絶縁の心理的シグナルです。"
            },
            {
                "term": "buang sial (meruwat / tolak bala)",
                "trans": "厄落としをする、悪運を祓う",
                "nuance": "事故、病気、失業など度重なる不幸に見舞われた際、髪を切ったり海で沐浴したりして負のエネルギーを浄化する伝統的儀礼に由来する文化語彙です。",
                "ex_id": "Setelah sembuh dari sakit berkepanjangan, ia memotong rambutnya sebagai simbol buang sial.",
                "ex_kana": "ステラ スンブー ダリ サキット ブルクパンジャンガン、イア ムモトン ランブットニャ スバガイ シンボル ブアン シアル",
                "ex_ja": "長引く病気から回復した後、彼は厄落とし（悪運祓い）の象徴として髪を短く切りました。",
                "note": "ジャワの伝統的な厄除け儀礼 `ruwatan` に通じる民間概念です。"
            },
            {
                "term": "buang hajat (buang air besar secara santun)",
                "trans": "大便をする、用を足す（丁寧な言いまわし）",
                "nuance": "`hajat` は「必要・用件」を意味するアラビア語起源の語彙で、公共衛生キャンペーン等で `Jangan buang hajat sembarangan (BABS)`（野外排泄の禁止）の標語として用いられます。",
                "ex_id": "Penyediaan jamban sehat di pedesaan bertujuan mencegah kebiasaan buang hajat di sungai.",
                "ex_kana": "プニェディアアン ジャンバン セハット ディ プデサアン ブルトゥジュアン ムンチェガ クビアサアン ブアン ハジャット ディ スンガイ",
                "ex_ja": "農村部での衛生的なトイレの整備は、川での野外排泄習慣を防ぐことを目的としています。",
                "note": "保健行政・公衆衛生の公式文書における標準表現です。"
            }
        ],
        "dialogue": {
            "title": "長時間の不毛な会議とプロジェクトの見直し",
            "lines": [
                ("Bambang", "Rapat koordinasi tadi pagi berlangsung hampir empat jam tanpa menghasilkan keputusan apapun."),
                ("Yuni", "Benar-benar buang waktu dan tenaga, ya. Padahal tenggat waktu kita sudah semakin dekat."),
                ("Bambang", "Bahkan manajer divisi lain tampak buang muka saat saya meminta bantuan tim teknis mereka."),
                ("Yuni", "Mungkin mereka sedang banyak tekanan. Lebih baik kita fokus pada sumber daya yang kita miliki agar tidak buang uang percuma.")
            ],
            "trans": [
                ("バンバン", "今朝の調整会議、何の結論も出ないまま4時間近くも続いたよ。"),
                ("ユニ", "本当に時間とエネルギーの無駄遣い（buang waktu）だったわね。締切がどんどん迫っているのに。"),
                ("バンバン", "それどころか、私が技術チームの支援を要請した際、他部署のマネージャーはあからさまに顔を背けて（buang muka）無視したんだ。"),
                ("ユニ", "向こうもプレッシャーが大きいのかも。予算を無駄にドブに捨てない（buang uang）よう、自前のリソースに集中しましょう。")
            ]
        },
        "grammar_points": [
            "**meN- の有声音 b 保持**: `buang` の頭文字は有声音 `b` です。接頭辞 `meN-` が付加されると `b` は脱落せず保持され `membuang`（ムンブアン）となります（例: `membuang sampah`＝ゴミを捨てる）。",
            "**buang-buang の畳語反復**: `buang waktu` や `buang uang` は、畳語動詞 `membuang-buang waktu` や `buang-buang uang` にすることで、「無駄にダラダラと投げ捨て続けている」という無益な反復性を感情を込めて強調できます。"
        ],
        "quizzes": [
            {
                "q": "「相手と視線を合わせたくないため、意図的に顔を背けて冷淡に無視する態度」を表す成句はどれか。",
                "choices": ["buang muka", "buang waktu", "buang air", "buang sial"],
                "ans": "buang muka",
                "expl": "顔を背けて無視する慣用表現は `buang muka` です。"
            },
            {
                "q": "外出先で「おしっこをしたい（小用を足したい）」と丁寧に伝える表現として正しいものはどれか。",
                "choices": ["ingin buang air kecil", "ingin buang waktu", "ingin buang sial", "ingin buang muka"],
                "ans": "ingin buang air kecil",
                "expl": "小水・排尿の適切な表現は `buang air kecil` です。"
            },
            {
                "q": "「重なる不運や災厄を祓うため、伝統儀礼や散髪などを行って厄落としをする」を意味する表現はどれか。",
                "choices": ["buang sial", "ambil hati", "pasang badan", "buat onar"],
                "ans": "buang sial",
                "expl": "悪運や厄を落とす・祓う民間表現は `buang sial` です。"
            }
        ],
        "culture_column": {
            "title": "「Buang Sial」とインドネシアの浄化儀礼",
            "body": "インドネシアでは、大きな病気や事故から生還した際、あるいは度重なる不運に見舞われた際に「buang sial（厄落とし）」として頭髪を剃ったり、海に花を流す儀礼（larung sesaji）を行ったりする風習が広く残っています。単なる迷信にとどまらず、過去のトラウマや停滞した精神状態に明確な区切りをつけ、心機一転して前向きな日常へと再出発するための実生活に根ざした心理的セラピーとして機能しています。"
        }
    },
    {
        "filename": "docs/lexicon/08-verb-collocations-lepas.md",
        "title": "【共起連語】語根 lepas の必須コロケーション辞典：lepas tangan / lepas tanggung jawab / lepas kendali / lepas landas",
        "root": "lepas",
        "meaning": "放す、離れる、外れる、逃れる、自由になる",
        "core_concept": "「束縛されていた紐や拘束から解き放たれる」原義から、「無責任に手を引く（責任放棄する）」「感情や車輛のコントロールを失う」「飛行機が滑走路を離陸する」「監視の死角に入って見失う」という、解放と制御喪失の多面的な語彙世界を構築します。",
        "table_rows": [
            ("lepas tangan", "手を放す", "責任逃れをする、知らぬ顔をする、手を引く", "非難/慣用", "Pihak pengembang tidak boleh lepas tangan atas cacat konstruksi bangunan apartemen."),
            ("lepas kendali", "制御・手綱を放す", "制御不能になる、暴走する、自制心を失う", "事故/心理", "Mobil pick-up itu lepas kendali dan menabrak pembatas jalan akibat rem blong."),
            ("lepas landas", "滑走路を離れる", "離陸する、テイクオフする、（経済が）離陸する", "航空/経済", "Pesawat Garuda Indonesia dijadwalkan lepas landas menuju Tokyo pukul sepuluh malam."),
            ("lepas tanggung jawab", "責任を放す", "責任を放棄する、義務を免れる", "公式/法務", "Perusahaan asuransi berupaya tidak lepas tanggung jawab terhadap klaim nasabah."),
            ("lepas pandang / lepas pengawasan", "視界・監視を放す", "見失う、目を離す、監視の目が届かなくなる", "育児/警備", "Jangan pernah lepas pandang terhadap balita saat berada di area kolam renang."),
            ("lepas lelah", "疲労を放す", "疲れを癒やす、休息をとる、一服する", "日常/文芸", "Para petani duduk di gubuk pinggir sawah sambil minum teh hangat untuk melepas lelah."),
            ("lepas rindu", "恋しさを放す", "恋しさを癒やす、久しぶりの再会を楽しむ", "叙情/家族", "Momen mudik lebaran adalah kesempatan emas untuk melepas rindu dengan sanak keluarga.")
        ],
        "details": [
            {
                "term": "lepas tangan (cuci tangan / tidak bertanggung jawab)",
                "trans": "責任逃れをする、関与を放棄する",
                "nuance": "トラブルや事故が発生した際、本来責任を負うべき当事者が「自分には関係ない」と無責任に手を引く卑劣な態度を厳しく糾弾する言葉です。",
                "ex_id": "Kontraktor utama dituduh lepas tangan setelah subkontraktornya gagal membayar upah buruh.",
                "ex_kana": "コントラクトール ウタマ ディトゥドゥー ルパス タンガン ステラ サブコントラクトールニャ ガガル ムンバヤル ウパ ブルフ",
                "ex_ja": "元請け業者は、下請け業者が労働者の賃金支払いを怠った後に責任逃れをしたとして告発されました。",
                "note": "類似の身体表現に `cuci tangan`（手を洗う＝責任を回避する）があります。"
            },
            {
                "term": "lepas kendali (hilang kontrol)",
                "trans": "制御不能になる、暴走する",
                "nuance": "自動車のブレーキ故障やスリップによる物理的制御喪失から、群衆の暴徒化、激怒して自制心を失った人間の精神状態まで幅広く用いられます。",
                "ex_id": "Situasi unjuk rasa menjadi lepas kendali setelah sekelompok penyusup mulai melempari petugas dengan batu.",
                "ex_kana": "シトゥアシ ウンジュッ ラサ ムンジャディ ルパス クンダリ ステラ スケロンポッ プニュスップ ムライ ムルンパリ プトゥガス ドゥンガン バトゥ",
                "ex_ja": "潜入者グループが警官隊に向かって投石を始めた後、デモの状況は制御不能（暴走状態）に陥りました。",
                "note": "`hilang kendali` とも互換性があります。"
            },
            {
                "term": "lepas landas (take off)",
                "trans": "離陸する、テイクオフする",
                "nuance": "航空用語としての「離陸」の標準語です（対義語は `mendarat`＝着陸する）。また経済学において、発展途上国が持続的成長軌道に乗る「経済離陸期（fase lepas landas）」の比喩としても有名です。",
                "ex_id": "Karena cuaca buruk dan kabut tebal, penerbangan ditunda dan belum diizinkan lepas landas.",
                "ex_kana": "カレナ チュアチャ ブルッ ダン カブット トゥバル、プヌルバンガン ディトゥンダ ダン スブルム ディイジンカン ルパス ランダス",
                "ex_ja": "悪天候と濃霧のため、フライトは遅延となりまだ離陸を許可されていません。",
                "note": "`landas` は「滑走路（landasan）」の語根です。"
            },
            {
                "term": "lepas pandang (luput dari pandangan)",
                "trans": "目を離す、見失う、視界から外れる",
                "nuance": "ショッピングモールやプールなど、一瞬の油断で子どもや要人を見失ってしまう危機的な状況を警告する際に用いられます。",
                "ex_id": "Hanya karena lepas pandang selama beberapa detik, anak kecil itu sudah berlari ke tengah jalan.",
                "ex_kana": "ハニャ カレナ ルパス パンダン スラマ ブルブラパ デティッ、アナッ クチル イトゥ スダ ブルラリ ケ トゥンガ ジャラン",
                "ex_ja": "わずか数秒目を離した（視界から外れた）隙に、その幼い子は道路の真ん中へ駆け出していました。",
                "note": "事故防止の安全標語で頻出します。"
            },
            {
                "term": "melepas lelah / melepas rindu",
                "trans": "疲れを癒やす / 恋しさを癒やす（再会を喜ぶ）",
                "nuance": "他動詞 `melepas`（解き放つ）に感情や生理的疲労を繋げることで、「長年胸に溜め込んできた感情や疲れをすっきりと解放する」という詩的で心温まる表現になります。",
                "ex_id": "Setelah menempuh perjalanan darat selama dua hari, para pemudik akhirnya bisa melepas rindu dengan orang tua tercinta.",
                "ex_kana": "ステラ ムヌンプ プルジャラナン ダラット スラマ ドゥア ハリ、パラ プムディッ アヒルニャ ビサ ムルパス リンドゥ ドゥンガン オラン トゥア トゥルチンタ",
                "ex_ja": "2日間の陸路の旅路路程程程を経て、帰省客たちはついに愛する両親との再会を果たし、募る恋しさを癒やす（melepas rindu）ことができました。",
                "note": "帰省シーズン（Mudik）の報道や詩歌で頻繁に耳にします。"
            }
        ],
        "dialogue": {
            "title": "製品リコール問題と広報対応の危機管理",
            "lines": [
                ("Irfan", "Sari, ada laporan bahwa salah satu model sepeda motor listrik kita tiba-tiba lepas kendali di jalan tol."),
                ("Sari", "Gawat sekali! Kita tidak boleh lepas tangan dan harus segera menarik semua produk tersebut untuk investigasi."),
                ("Irfan", "Setuju. Jangan sampai masyarakat mengira manajemen lepas tanggung jawab atas keselamatan konsumen."),
                ("Sari", "Saya akan segera menyusun siaran pers agar situasi krisis ini tidak semakin lepas kendali.")
            ],
            "trans": [
                ("イルファン", "サリさん、弊社の電動バイクの1モデルが高速道路で突然制御不能（lepas kendali）になったという報告が入ったよ。"),
                ("サリ", "大変な事態です！決して知らぬ顔で責任逃れ（lepas tangan）をせず、直ちに全製品を回収して原因調査を行うべきです。"),
                ("イルファン", "同感だ。消費者の安全に対する責任を経営陣が放棄している（lepas tanggung jawab）と世間に誤解されてはならない。"),
                ("サリ", "この危機的状況がこれ以上暴走（lepas kendali）しないよう、至急プレスリリースを作成します。")
            ]
        },
        "grammar_points": [
            "**meN- 付加による無声音 l の保持**: `lepas` の頭文字は流音 `l` です。接頭辞 `meN-` が付加されると `melepas`（ムルパス）となり、子音脱落は起きません（例: `melepaskan`＝〜を解き放つ）。",
            "**他動詞構文での melepas**: `melepas lelah`（疲労を癒やす）や `melepas rindu`（恋しさを晴らす）のように目的語を解放する文脈では、文法的に正則な他動詞形 `melepas` または `melepaskan` が好まれます。"
        ],
        "quizzes": [
            {
                "q": "企業や指導者が「問題発生時に自らの非を認めず、無責任に手を引く・知らぬ顔をする」態度を批判する成句はどれか。",
                "choices": ["lepas tangan", "lepas landas", "lepas lelah", "tarik ulur"],
                "ans": "lepas tangan",
                "expl": "無責任に関与を放棄し、責任逃れをするイディオムは `lepas tangan` です。"
            },
            {
                "q": "飛行機の「離陸（テイクオフ）」を表す正しいインドネシア語はどれか。",
                "choices": ["lepas landas", "lepas kendali", "mendarat darurat", "pasang badan"],
                "ans": "lepas landas",
                "expl": "離陸は `lepas landas` です。`mendarat` は着陸、`lepas kendali` は制御不能です。"
            },
            {
                "q": "「車両がブレーキの故障により制御不能になり、ガードレールに激突した」の文脈で入る語はどれか。\n「Kendaraan itu mendadak ________ akibat rem blong dan menabrak pembatas jalan.」",
                "choices": ["lepas kendali", "lepas rindu", "buka suara", "tutup buku"],
                "ans": "lepas kendali",
                "expl": "車などのコントロールを失い制御不能になるのは `lepas kendali` です。"
            }
        ],
        "culture_column": {
            "title": "「Melepas Rindu」にみるムディック（帰省）の温もり",
            "body": "レバラン（断食明け大祭）の帰省ラッシュ「Mudik」のニュースで、アナウンサーが最も温かい口調で語るのが `melepas rindu`（募る恋しさを解き放つ）というフレーズです。首都ジャカルタの過酷な日常で孤独やプレッシャーに耐えてきた人々が、故郷の村（kampung halaman）に帰り、老いた両親の手に口づけ（sungkem）をして抱き合う瞬間、張り詰めていた心の緊張が優しく解き放たれるのです。"
        }
    },
    {
        "filename": "docs/lexicon/09-verb-collocations-jatuh.md",
        "title": "【共起連語】語根 jatuh の必須コロケーション辞典：jatuh tempo / jatuh sakit / jatuh cinta / jatuh bangun",
        "root": "jatuh",
        "meaning": "落ちる、落下する、倒れる、陥る",
        "core_concept": "「重力に従って高い所から低い所へ落下する」物理的動作から、「期限が到来して満期を迎える」「病魔に倒れる」「恋に落ちる」「事業で浮沈を繰り返す」という、不可抗力的な運命の転落や情動の深化を描く豊かな表現群を形成します。",
        "table_rows": [
            ("jatuh tempo", "期日に落ちる", "満期を迎える、支払期日が到来する、期限切れになる", "金融/商取引", "Tagihan kartu kredit ini akan jatuh tempo pada tanggal 25 bulan ini."),
            ("jatuh sakit", "病気に落ちる", "病気に倒れる、発病する、患う", "日常/健康", "Akibat kelelahan bekerja lembur tanpa istirahat, ayah akhirnya jatuh sakit."),
            ("jatuh cinta", "愛に落ちる", "恋に落ちる、一目惚れする、愛着を抱く", "恋愛/感情", "Pemuda itu langsung jatuh cinta pada pandangan pertama saat melihat senyumnya."),
            ("jatuh bangun", "倒れて起きる", "紆余曲折を経る、七転び八起き、苦闘を重ねる", "人生/起業", "Pengusaha sukses itu menceritakan bagaimana ia jatuh bangun merintis usahanya dari nol."),
            ("jatuh miskin", "貧困に落ちる", "無一文になる、没落する、極貧に喘ぐ", "社会/経済", "Banyak keluarga jatuh miskin akibat terlilit utang judi online yang tak berkesudahan."),
            ("jatuh hati", "心に落ちる", "心を奪われる、好意を寄せる、気に入る", "感情/慣用", "Sejak berkunjung ke Raja Ampat, turis asing itu langsung jatuh hati pada keindahan alamnya."),
            ("jatuh pingsan", "気絶に落ちる", "卒倒する、失神する、気を失って倒れる", "救急/医療", "Seorang peserta upacara jatuh pingsan karena berdiri terlalu lama di bawah terik matahari.")
        ],
        "details": [
            {
                "term": "jatuh tempo (tanggal batas pembayaran)",
                "trans": "支払期日が到来する、満期になる",
                "nuance": "銀行ローン、クレジットカード請求、社債、契約の満期日など、金融実務や商取引で最も厳格に遵守される締め切り日を表す専門連語です。",
                "ex_id": "Nasabah dihimbau segera melunasi angsuran sebelum tanggal jatuh tempo agar tidak terkena denda keterlambatan.",
                "ex_kana": "ナサバー ディヒムバウ スグラ フルナシ アンスラン スブルム タンガル ジャトゥ テンポ アガル ティダッ トゥルクナ デンダ クトゥルランバタン",
                "ex_ja": "顧客は、遅延損害金（延滞利息）が課されないよう期日到来日（jatuh tempo）までに速やかに分割払い債務を清算するよう呼びかけられています。",
                "note": "請求書に `Jatuh Tempo: DD/MM/YYYY` と印字されます。"
            },
            {
                "term": "jatuh sakit (terserang penyakit)",
                "trans": "病気に倒れる、体調を崩す",
                "nuance": "単に「風邪をひいている（sedang sakit）」という静止状態ではなく、過労や感染などによって「急激に健康を損なって倒れ伏す」という動的な変化を強調します。",
                "ex_id": "Setelah berhari-hari bertugas mengevakuasi korban banjir, beberapa relawan mulai jatuh sakit.",
                "ex_kana": "ステラ ブルハリハリ ブルトゥガス ムネヴァクアシ コルバン バンジール、ブルブラパ ルラワン ムライ ジャトゥ サキット",
                "ex_ja": "何日も洪水被災者の救援活動に従事した後、ボランティアの数名が病気に倒れ始めました。",
                "note": "過労死や急性疾患の文脈でよく見られます。"
            },
            {
                "term": "jatuh cinta (kasmaran / terpikat asmara)",
                "trans": "恋に落ちる、愛するようになる",
                "nuance": "英語の「fall in love」と全く同じ構造を持つ万国共通のロマンチックな表現です。`jatuh cinta pada pandangan pertama`（一目惚れする）は定番フレーズです。",
                "ex_id": "Bukan hal yang aneh jika banyak wisatawan jatuh cinta pada keramahan penduduk pulau Bali.",
                "ex_kana": "ブカン ハル ヤン アネ ジュカ バニャッ ウィサタワン ジャトゥ チンタ パダ クラマハン プンドゥドゥッ プラウ バリ",
                "ex_ja": "多くの旅行客がバリ島住民の温かいもてなしに心奪われ（恋に落ち）ても、何ら不思議ではありません。",
                "note": "人だけでなく土地や文化に対する深い愛着にも使われます。"
            },
            {
                "term": "jatuh bangun (pasang surut perjuangan)",
                "trans": "七転び八起き、幾多の挫折と奮闘を繰り返す",
                "nuance": "「倒れては起き上がる」。困難な状況で倒れそうになりながらも、決して諦めず立ち上がって夢を掴み取る人間の不屈の生き様を讃える感動的なイディオムです。",
                "ex_id": "Kisah jatuh bangun atlet difabel itu dalam meraih medali emas sungguh menginspirasi jutaan orang.",
                "ex_kana": "キサー ジャトゥ バングン アトレット ディファベル イトゥ ダラム ムライ メダリ エマス スングー ムンギンスピラシ ジュタアン オラン",
                "ex_ja": "その障がい者アスリートが金メダルを獲得するまでの七転び八起きの苦闘の物語は、何百万人もの人々に真の勇気を与えました。",
                "note": "自伝（otobiografi）や起業ストーリーの副題として極めて好まれます。"
            },
            {
                "term": "jatuh hati (menaruh simpati / cinta)",
                "trans": "心を奪われる、好意を寄せる",
                "nuance": "`jatuh cinta` が情熱的な恋愛感情であるのに対し、`jatuh hati` はより穏やかで奥深い好意、慈しみ、あるいは物や景色への深い愛着を含みます。",
                "ex_id": "Sejak pertama kali mendengarkan petikan dawai sasando, komponis itu langsung jatuh hati pada musik tradisional NTT.",
                "ex_kana": "スジャッ プルタマ カリ ムンデンガルカン プティカン ダワイ ササンド、コンポニス イトゥ ラングスン ジャトゥ ハティ パダ ムジッ トラディシオナル エヌテテ",
                "ex_ja": "ササンドの弦の爪弾きを初めて聴いた時から、その作曲家は東ヌサ・トゥンガラ（NTT）の伝統音楽に一瞬で心を奪われました。",
                "note": "文学作品や紀行文で好まれる美しい表現です。"
            }
        ],
        "dialogue": {
            "title": "起業家の苦闘とローンの返済計画",
            "lines": [
                ("Doni", "Bagaimana kabar perkembangan kedai kopimu yang baru buka tiga bulan lalu?"),
                ("Bayu", "Luar biasa berat, Don. Saya benar-benar merasakan bagaimana jatuh bangun mengelola bisnis sendiri."),
                ("Doni", "Iya, saya paham. Apalagi minggu depan cicilan modal usaha sudah mulai jatuh tempo, kan?"),
                ("Bayu", "Tepat sekali. Saya harus menjaga kesehatan jangan sampai jatuh sakit di tengah tekanan finansial ini.")
            ],
            "trans": [
                ("ドニ", "3ヶ月前にオープンしたばかりの君のカフェ、進捗はどうだい？"),
                ("バユ", "とんでもなく大変だよ、ドニ。自分で事業を切り盛りする中で七転び八起き（jatuh bangun）の苦闘をまさに実感しているところさ。"),
                ("ドニ", "ああ、分かるよ。しかも来週には創業資金融資の返済期日（jatuh tempo）が迫っているんだろう？"),
                ("バユ", "その通りなんだ。この資金的プレッシャーの中で、病気に倒れる（jatuh sakit）ことだけはないよう体調管理に気をつけなきゃ。")
            ]
        },
        "grammar_points": [
            "**自動詞としての jatuh**: `jatuh` は外力による他動詞ではなく、主語自身がその状態に転落・到達する自動詞です。したがって `meN-` 接辞は通常付かず、語根 `jatuh` のまま副詞や名詞を伴って多様な連語を構成します。",
            "**使役化 menjatuhkan**: 他動詞にして「（物を）落とす」「（政権を）倒閣・失脚させる」「（判決を）下す」と表現する場合は、使役接尾辞 `-kan` を伴って `menjatuhkan hukuman`（判決を下す）、`menjatuhkan sanksi`（制裁を科す）となります。"
        ],
        "quizzes": [
            {
                "q": "銀行の融資やクレジットカード請求の「支払期日・満期」を意味する正確な専門連語はどれか。",
                "choices": ["jatuh tempo", "jatuh bangun", "jatuh sakit", "jatuh cinta"],
                "ans": "jatuh tempo",
                "expl": "支払期日や満期到来を意味する金融用語は `jatuh tempo` です。"
            },
            {
                "q": "「苦難や挫折を幾度も経験しながら、不屈の精神で立ち上がる七転び八起きの生き様」を表す慣用句はどれか。",
                "choices": ["jatuh bangun", "pasang badan", "tarik ulur", "buang waktu"],
                "ans": "jatuh bangun",
                "expl": "幾多の苦闘と浮沈を乗り越える七転び八起きの表現は `jatuh bangun` です。"
            },
            {
                "q": "「過酷な労働環境により、多くの作業員が急激に体調を崩して病気に倒れた」を意味する動詞句はどれか。",
                "choices": ["jatuh sakit", "jatuh hati", "jatuh pingsan", "jatuh miskin"],
                "ans": "jatuh sakit",
                "expl": "発病する、病に倒れるは `jatuh sakit` です。"
            }
        ],
        "culture_column": {
            "title": "「Jatuh Bangun」とダンドゥットの名曲",
            "body": "インドネシアの大衆歌謡ダンドゥット（Dangdut）に、メガ・ムスティカが歌って大ヒットした不朽の名曲『Jatuh Bangun』があります。「Jatuh bangun aku mengejarmu...（あなたを追いかけて私は転び、起き上がり…）」と歌われるこのフレーズは、恋愛の哀歓のみならず、激動の現代社会をたくましく泥臭く生き抜く庶民（rakyat jelata）の人生讃歌として、世代を超えて熱狂的に愛唱されています。"
        }
    },
    {
        "filename": "docs/lexicon/10-verb-collocations-naik.md",
        "title": "【共起連語】語根 naik の必須コロケーション辞典：naik daun / naik pangkat / naik darah / naik banding",
        "root": "naik",
        "meaning": "上がる、登る、乗る、増える、昇進する",
        "core_concept": "「物理的に低い位置から高い位置へ上昇する、乗り物に乗る」動作から、「人気や運気が急上昇する」「役職が昇進する」「激怒して血圧が上がる」「判決を不服として上訴・控訴する」という、栄達・怒り・法的手続きの上昇メタファーを形成します。",
        "table_rows": [
            ("naik daun", "葉に登る", "人気絶頂になる、時の人となる、売れっ子になる", "芸能/流行", "Band indie asal Bandung itu sedang naik daun di kalangan anak muda."),
            ("naik pangkat", "位・階級に登る", "昇進する、昇格する、階級が上がる", "人事/軍警察", "Setelah bertugas dengan penuh dedikasi, perwira itu resmi naik pangkat menjadi jenderal."),
            ("naik darah / naik pitam", "血・胆汁が上がる", "激怒する、血圧が上がる、頭に血がのぼる", "感情/心理", "Sikap pelaku yang arogan membuat hakim dan jaksa di pengadilan naik pitam."),
            ("naik banding", "控訴に登る", "控訴する、上級審へ不服申し立てを行う", "法務/司法", "Kuasa hukum terdakwa menyatakan akan mengajukan naik banding atas vonis tersebut."),
            ("naik gaji", "給与が上がる", "昇給する、ベースアップする", "労働/経済", "Para buruh menggelar demonstrasi damai menuntut kenaikan upah minimum tahun depan."),
            ("naik kelas", "学年・等級に登る", "進級する、格上げされる、ステージが一段上がる", "教育/ビジネス", "Program pelatihan ini dirancang agar UMKM lokal bisa naik kelas menjadi eksportir global."),
            ("naik haji", "巡礼に登る", "メッカ大巡礼（ハッジ）を果たす", "宗教/文化", "Kakek menabung selama dua puluh tahun agar bisa berangkat naik haji ke tanah suci.")
        ],
        "details": [
            {
                "term": "naik daun (populer / tenar)",
                "trans": "人気絶頂である、時の人になる、ブレイクする",
                "nuance": "芸能人、アーティスト、新興企業などが急速に世間の注目と熱烈な支持を集め、名声を極めている輝かしい状態を表す極めてポピュラーな慣用句です。",
                "ex_id": "Aktor muda berbakat itu kini sedang naik daun setelah film terbarunya menembus box office.",
                "ex_kana": "アクトール ムダ ブルバカット イトゥ キニ スダン ナイッ ダウン ステラ フィルム トゥルバルニャ ムヌンブス ボックス オフィス",
                "ex_ja": "その才能ある若手俳優は、主演した最新映画が興行記録を塗り替えたことで、現在人気絶頂（ブレイク中）です。",
                "note": "語源は「緑の若葉が高く伸びゆく生命力」に由来します。"
            },
            {
                "term": "naik pangkat (promosi jabatan)",
                "trans": "昇進する、昇格する、階級が上がる",
                "nuance": "公務員、軍隊、警察、民間企業における階級や役職が上位に引き上げられる公式人事イベントです。",
                "ex_id": "Selamat atas keberhasilan Anda yang baru saja naik pangkat menjadi manajer operasional.",
                "ex_kana": "スラマット アタス クブルハシラン アンダ ヤン バル サジャ ナイッ パンカット ムンジャディ マナジェール オペラシオナル",
                "ex_ja": "業務統括マネージャーへのご昇進、心よりお祝い申し上げます。",
                "note": "名詞形は `kenaikan pangkat`（昇進・昇格）です。"
            },
            {
                "term": "naik darah / naik pitam (sangat marah / murka)",
                "trans": "激怒する、頭に血がのぼる",
                "nuance": "不正義、侮辱、嘘などを目の当たりにして怒りが頂点に達し、顔が紅潮するほどの激しい憤りを表します。`naik pitam` はさらに文学的・強烈な表現です。",
                "ex_id": "Mendengar fitnah keji yang ditujukan kepada keluarganya, pria penyabar itu pun akhirnya naik darah.",
                "ex_kana": "ムンデンガル フィトナー クジ ヤン ディトゥジュカン クパダ クルアルガニャ、プリア プニャバール イトゥ プン アヒルニャ ナイッ ダラー",
                "ex_ja": "家族に向けられた卑劣な中傷を聞き、普段は温厚なその男もついに頭に血がのぼり（激怒し）ました。",
                "note": "感情抑制の限界を超えた状態を描写します。"
            },
            {
                "term": "naik banding (mengajukan banding)",
                "trans": "控訴する、上訴する",
                "nuance": "第一審（地方裁判所 Pengadilan Negeri）の判決に不服がある当事者が、高等裁判所（Pengadilan Tinggi）に対して再審理を求める司法用語です。",
                "ex_id": "Merasa vonis hakim terlalu berat dan tidak adil, terdakwa memutuskan untuk segera naik banding.",
                "ex_kana": "ムラサ ヴォニス ハキム トゥルラル ブラット ダン ティダッ アディル、トゥルダクワ ムムトゥスカン ウントゥッ スグラ ナイッ バンディン",
                "ex_ja": "裁判官の言い渡した判決が重すぎ不当であると感じ、被告人は直ちに控訴する（naik banding）ことを決定しました。",
                "note": "最高裁判所（Mahkamah Agung）へ持ち込む場合は `kasasi`（上告）となります。"
            },
            {
                "term": "naik kelas (meningkat levelnya)",
                "trans": "進級する / （事業等の）ステージが一段上がる",
                "nuance": "学校で学年が上がる原義から、政府主導の「零細企業（UMKM）の近代化・海外展開プログラム」のキャッチコピー「UMKM Naik Kelas」として国中で定着した成長キーワードです。",
                "ex_id": "Digitalisasi sistem pembayaran QRIS terbukti membantu ribuan pedagang tradisional naik kelas.",
                "ex_kana": "ディジタリサシ システム プンバヤラン クリス トゥルブクティ ムンバントゥ リブアン プダガン トラディシオナル ナイッ クラス",
                "ex_ja": "QRISによるデジタル決済システムの導入は、何千もの伝統的商人たちの事業ステージを一段引き上げる（naik kelas）手助けとなったことが証明されました。",
                "note": "能力や地位のステップアップをポジティブに称える表現です。"
            }
        ],
        "dialogue": {
            "title": "若手起業家のブレイクと事業拡大の歓び",
            "lines": [
                ("Tono", "Wah, selamat ya! Brand kopi lokal buatanmu kabarnya sedang naik daun di Jakarta."),
                ("Eka", "Terima kasih banyak, Mas Tono. Berkat adopsi teknologi dan kemitraan petani, usaha kami akhirnya bisa naik kelas."),
                ("Tono", "Luar biasa. Manajer produksimu yang bekerja keras layak dipertimbangkan untuk naik pangkat, tuh."),
                ("Eka", "Pasti, Mas. Kesejahteraan tim adalah prioritas utama agar tidak ada yang merasa kecewa atau naik darah karena beban kerja.")
            ],
            "trans": [
                ("トノ", "おお、おめでとう！君が立ち上げたローカルコーヒーのブランド、ジャカルタで今や人気絶頂（naik daun）らしいじゃないか。"),
                ("エカ", "トノさん、本当にありがとうございます。テクノロジーの導入と農家さんとの提携のおかげで、私たちのビジネスもようやく一段上のステージへ進む（naik kelas）ことができました。"),
                ("トノ", "素晴らしい。現場で奮闘してくれた製造マネージャーは、昇進（naik pangkat）を検討してあげるに値するよ。"),
                ("エカ", "もちろんです。過酷な業務負荷で不満を抱いたり激怒したり（naik darah）する者が出ないよう、チームの待遇改善が最優先事項です。")
            ]
        },
        "grammar_points": [
            "**自動詞としての naik**: `naik` は自動詞であり、「乗る」「上がる」を意味します。目的語を直接取る他動詞にするには使役接尾辞 `-kan` を付加して `menaikan`（引き上げる、昇給させる、掲揚する）とします（例: `menaikkan bendera`＝国旗を掲揚する）。",
            "**名詞化 kenaikan**: 接頭辞 `ke-` と接尾辞 `-an` が付いた `kenaikan` は、「上昇・値上げ・昇進」を意味する名詞となります（例: `kenaikan harga bahan pokok`＝生活必需品の値上げ、`kenaikan pangkat`＝昇進）。"
        ],
        "quizzes": [
            {
                "q": "芸能人やアーティストが「今まさに世間で大ブレイクし、人気絶頂である」ことを表す慣用句はどれか。",
                "choices": ["naik daun", "naik darah", "naik banding", "naik pangkat"],
                "ans": "naik daun",
                "expl": "人気絶頂、ブレイク中を意味するイディオムは `naik daun` です。"
            },
            {
                "q": "裁判の判決に不服がある被告が「高等裁判所へ控訴する」ことを意味する法務連語はどれか。",
                "choices": ["naik banding", "naik kelas", "naik darah", "pasang badan"],
                "ans": "naik banding",
                "expl": "控訴の手続きを行うことは `naik banding` と言います。"
            },
            {
                "q": "怒りが頂点に達して「頭に血がのぼる、激怒する」ことを表す身体連語はどれか。",
                "choices": ["naik darah", "naik daun", "naik kelas", "ambil alih"],
                "ans": "naik darah",
                "expl": "激怒して血圧が上がる状態は `naik darah` または `naik pitam` と表現します。"
            }
        ],
        "culture_column": {
            "title": "「Naik Daun」にみるインドネシアの植物メタファー",
            "body": "なぜ人気絶頂になることを「葉に登る（naik daun）」と呼ぶのでしょうか。伝統的な農耕社会において、若葉（pucuk daun）は最も日光を浴びて青々と輝き、生命の躍動と収穫の約束を象徴していました。その葉の頂点に立つかのように才能が開花し、社会の賞賛を浴びる姿を愛でるこの表現は、自然の息吹とともに生きるインドネシア人の温かな詩情が結晶化した名言といえます。"
        }
    }
]

def generate_markdown(art):
    # 构建最重要コロケーション表
    table_lines = [
        "| コロケーション（連語） | 直訳 | 実際の意味・用例 | 文脈・レジスター | 典型例文 |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for row in art["table_rows"]:
        table_lines.append(f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} | *{row[4]}* |")
    table_md = "\n".join(table_lines)

    # 各コロケーションの詳細解説
    details_md_list = []
    for d in art["details"]:
        d_md = f"""### {d["term"]}
- **直訳と意味**: 「**{d["trans"]}**」
- **語感と文脈解説**: {d["nuance"]}

<div class="id-example">
<div class="id-sentence"><strong>{d["ex_id"]}</strong></div>
<div class="id-pronunciation">（{d["ex_kana"]}）</div>
<div class="id-translation">「{d["ex_ja"]}」</div>
</div>

> [!NOTE]
> **語法・派生ポイント**: {d["note"]}
"""
        details_md_list.append(d_md)
    details_md = "\n".join(details_md_list)

    # 会話ダイアログ
    dlg = art["dialogue"]
    dlg_lines = []
    for l in dlg["lines"]:
        dlg_lines.append(f"**{l[0]}**: {l[1]}<br>")
    dlg_trans = []
    for t in dlg["trans"]:
        dlg_trans.append(f"- **{t[0]}**: 「{t[1]}」")
    
    dialogue_md = f"""<div class="dialogue-box">
<div class="dialogue-title">会話ダイアログ：{dlg["title"]}</div>

{"".join(dlg_lines)}
</div>

#### 日本語対訳
{"\n".join(dlg_trans)}
"""

    # 文法・語形ポイント
    gp_md = "\n".join([f"- {p}" for p in art["grammar_points"]])

    # クイズ
    quizzes_md_list = []
    for idx, q in enumerate(art["quizzes"], 1):
        choices_str = "\n".join([f"{chr(65+c_idx)}. {choice}" for c_idx, choice in enumerate(q["choices"])])
        q_md = f"""#### 問{idx}: {q["q"]}

{choices_str}

<details>
<summary>正解と解説を確認する</summary>

**正解**: 「**{q["ans"]}**」

**解説**:
{q["expl"]}
</details>
"""
        quizzes_md_list.append(q_md)
    quizzes_md = "\n".join(quizzes_md_list)

    # 文化コラム
    col = art["culture_column"]
    culture_md = f"""> [!TIP]
> **文化・語根コラム：{col["title"]}**
> 
> {col["body"]}
"""

    full_text = f"""# {art["title"]}

インドネシア語の語根 **`{art["root"]}`** は、原義として「**{art["meaning"]}**」を表します。{art["core_concept"]}

本稿では、日常会話からビジネス、司法・時事報道に至るまでネイティブスピーカーが自然に使いこなす必須の共起表現（コロケーション）を体系的に解説します。

---

## 1. 語根 `{art["root"]}` の最頻出コロケーション総覧

まずは、頻繁に用いられる主要な連語表現の全体像を把握しましょう。

{table_md}

---

## 2. 重要コロケーションの詳細解説と実践例文

それぞれの共起表現が持つ語感、文脈のニュアンス、および構文上のポイントを詳しく見ていきます。

{details_md}

---

## 3. 実践会話ダイアログ

日常や職場の現場でこれらのコロケーションがどのように自然に組み合わされて使われるか、会話の流れで確認しましょう。

{dialogue_md}

---

## 4. 文法・構文上の注意点（接辞変化と語形）

{gp_md}

---

## 5. 定着確認クイズ（全3問）

本記事で学んだ重要コロケーションの理解度をチェックしましょう。

{quizzes_md}

---

## 6. コア語根の文化的背景

{culture_md}

---

## 7. 次のステップ・関連リンク
- [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return full_text

def main():
    os.makedirs("docs/lexicon", exist_ok=True)
    for art in articles:
        content = generate_markdown(art)
        with open(art["filename"], "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {art['filename']}")

if __name__ == "__main__":
    main()
