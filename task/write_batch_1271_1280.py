# -*- coding: utf-8 -*-
"""
Batch generation script for Section 31: Collocations Batch 3 (Articles 1271-1280)
Directory: docs/lexicon/
"""

import os

articles = [
    {
        "filename": "docs/lexicon/21-noun-collocations-mulut.md",
        "title": "【共起連語】身体名詞 mulut の連語辞典：mulut manis / tutup mulut / banyak mulut / buah mulut",
        "root": "mulut",
        "meaning": "口、開口部、発話器官、弁舌",
        "core_concept": "食物を取り入れ言葉を紡ぎ出す「口」から、「口先だけの甘い言葉」「秘密を固く守る沈黙」「おしゃべりで口数が多い軽薄さ」「世間の噂の的」という、言葉の真偽・社交・秘密・世評のメタファーを構成します。",
        "table_rows": [
            ("mulut manis", "甘い口", "口がうまい、口先だけの甘言、愛想の良い言葉", "人間関係/批判", "Jangan mudah teperdaya oleh mulut manis tenaga pemasar yang menawarkan keuntungan instan."),
            ("tutup mulut", "口を閉じる", "口をつぐむ、沈黙を守る、口封じする", "司法/事件", "Saksi kunci itu bersikeras tutup mulut karena takut akan keselamatan keluarganya."),
            ("banyak mulut", "多い口", "おしゃべりな、口数が多い、余計な口出しをする", "性格/短所", "Karyawan baru itu terlalu banyak mulut sehingga tidak disukai oleh rekan-rekan seniornya."),
            ("buah mulut", "口の果実", "世間の噂の的、話題の種、語り草", "世評/メディア", "Keberhasilan pemuda desa menciptakan turbin angin mandiri menjadi buah mulut warga kota."),
            ("mulut besar", "大きい口", "大言壮語する、ホラ吹き、ビッグマウス", "非難/性格", "Dia terkenal bermulut besar tetapi kenyataannya tidak memiliki bukti prestasi apapun."),
            ("adu mulut", "口を戦わせる", "口論する、激しく言い争う、口げんかする", "対立/日常", "Dua pengemudi yang saling bersenggolan di jalan tol terlibat adu mulut sengit."),
            ("mulut buaya", "ワニの口", "虎口、危険な状況（lepas dari mulut harimau jatuh ke mulut buaya）", "ことわざ/危機", "Kebijakan utang baru itu ibarat meloloskan diri dari mulut harimau lalu masuk ke mulut buaya.")
        ],
        "details": [
            {
                "term": "mulut manis (pandai merayu tapi tidak tulus)",
                "trans": "口がうまい、口先だけの甘言、美辞麗句",
                "nuance": "表面上は耳に心地よいお世辞や甘い約束を並べ立てるものの、内心では誠意がなく欺瞞を秘めている人物の言動を警戒する表現です。",
                "ex_id": "Waspadalah terhadap penipuan investasi yang menjanjikan keuntungan ratusan persen dengan mulut manis.",
                "ex_kana": "ワスパダラー トゥルハダップ プニプアン インヴェスタシ ヤン ムンジャンジカン クウントゥンガン ラトゥサン パーセン ドゥンガン ムルット マニス",
                "ex_ja": "口先だけの甘言（mulut manis）で数百パーセントの利益を約束する投資詐欺に十分警戒しなさい。",
                "note": "警戒・教訓の文脈で多用されます。"
            },
            {
                "term": "buah mulut (buah bibir / topik pembicaraan)",
                "trans": "世間の噂の的、話題の種、人々の語り草",
                "nuance": "街角やSNS、職場で誰もが口端に上らせているホットな話題を指します（同義語: `buah bibir`）。ポジティブな快挙にもスキャンダルにも使われます。",
                "ex_id": "Inovasi mobil listrik buatan mahasiswa ITS Surabaya seketika menjadi buah mulut di media nasional.",
                "ex_kana": "イノヴァシ モビル リストリッ ブアタン マハシスワ イーテーエス スラバヤ スケティカ ムンジャディ ブア ムルット ディ メディア ナシオナル",
                "ex_ja": "スラバヤITS工科大学の学生たちが制作した電気自動車の技術革新は、瞬く間に全国メディアで話題の的（buah mulut）となりました。",
                "note": "「Buah bibir（唇の果実）」と全く同じ意味で互換します。"
            },
            {
                "term": "adu mulut (bertengkar hebat secara verbal)",
                "trans": "激しく口論する、口げんかをする",
                "nuance": "物理的な殴り合い（adu fisik / adu jotos）に至る前段階として、互いに激しい言葉を浴びせ合って罵倒し合う状態を描写します。",
                "ex_id": "Rapat warga sempat memanas dan diwarnai adu mulut perihal alokasi dana bantuan sosial.",
                "ex_kana": "ラパット ワルガ スムパット ムマナス ダン ディワルナイ アドゥ ムルット プリアル アロカシ ダナ バントゥアン ソシアル",
                "ex_ja": "住民集会は紛糾し、社会保障給付金の配分をめぐって激しい口論（adu mulut）が交わされました。",
                "note": "ニュース報道のトラブル記事で定番です。"
            },
            {
                "term": "mulut besar (pembual / suka sesumbar)",
                "trans": "大言壮語する、ホラ吹き、ビッグマウス",
                "nuance": "実行力や実力が伴っていないにもかかわらず、大口を叩いて大言壮語する人物の性格的欠陥を批判する成句です。",
                "ex_id": "Jangan dengarkan janjinya yang muluk-muluk, dia itu cuma orang mulut besar yang tidak punya modal.",
                "ex_kana": "ジャンガン デンガルカン ジャンジニャ ヤン ムルックムルック、ディア イトゥ チュマ オラン ムルット ブサール ヤン ティダッ プニャ モダル",
                "ex_ja": "彼の誇大な約束など真に受けるな、資本も持たないただの大口叩き（mulut besar）にすぎないのだから。",
                "note": "英語の「big mouth」と同義です。"
            },
            {
                "term": "banyak mulut (cerewet / suka mencampuri urusan)",
                "trans": "おしゃべりな、口数が多い、余計な口出しをする",
                "nuance": "単に陽気でおしゃべりというより、「余計なことまで口出しして他人を不快にさせる出しゃばり」への非難の含みがあります。",
                "ex_id": "Orang yang terlalu banyak mulut di tempat kerja sering kali tidak disukai karena membocorkan rahasia rekan.",
                "ex_kana": "オラン ヤン トゥルラル バニャッ ムルット ディ トゥムパット クルジャ スリン カリ ティダッ ディスカイ カレナ ムンボチョルカン ラハシア ルカン",
                "ex_ja": "職場で口数が多すぎる（banyak mulut）おしゃべりな人間は、同僚の秘密を漏らしたりするため嫌われがちです。",
                "note": "自制心を欠く軽薄さを戒める表現です。"
            }
        ],
        "dialogue": {
            "title": "怪しい投資話の勧誘と先輩の警告",
            "lines": [
                ("Fajar", "Bang, tadi ada agen asuransi investasi yang menawarkan bunga 15 persen per bulan. Menarik sekali!"),
                ("Bang Hendra", "Hati-hati, Fajar! Jangan gampang kena bujuk rayu mulut manis agen seperti itu."),
                ("Fajar", "Tapi kantor cabangnya besar dan sekarang sedang jadi buah mulut di mana-mana, Bang."),
                ("Bang Hendra", "Banyak mulut besar yang akhirnya ditangkap polisi karena skema ponzi. Jangan sampai kamu menyesal nanti.")
            ],
            "trans": [
                ("ファジャール", "先輩、さっき月利15％を謳う投資保険の営業マンが来たんですよ。ものすごく魅力的です！"),
                ("ヘンドラ先輩", "気をつけろ、ファジャール！あんな業者の口先だけの甘言（mulut manis）に簡単に乗せられるんじゃない。"),
                ("ファジャール", "でも支店も立派で、いま至る所で話題の的（buah mulut）になっていますよ。"),
                ("ヘンドラ先輩", "ポンジ・スキームで最後は警察に御用となった大口叩き（mulut besar）なんて山ほどいるぞ。後で後悔するなよ。")
            ]
        },
        "grammar_points": [
            "**接尾辞 -an による mulut-mulutan**: `mulut` は身体器官ですが、`bermulut besar`（大口を叩く）、`bermulut manis`（口がうまい）のように接頭辞 `ber-` を伴って「〜な口を持つ（性格・態度）」という叙述形容詞句を形成します。",
            "**ことわざ Lepas dari mulut harimau...**: 「トラの口を逃れてワニの口に落ちる（一難去ってまた一難）」ということわざは、`mulut` が捕食・死の象徴として使われる古典的名句です。"
        ],
        "quizzes": [
            {
                "q": "「内心では誠意がないのに、口先だけで都合のよい美辞麗句やお世辞を並べる態度」を表す成句はどれか。",
                "choices": ["mulut manis", "mulut besar", "banyak mulut", "tutup mulut"],
                "ans": "mulut manis",
                "expl": "口先だけの甘言、口がうまい態度は `mulut manis` です。"
            },
            {
                "q": "「新技術やスキャンダルなどが、世間の人々の間で広く噂の的・話題の種になること」を意味する表現はどれか。",
                "choices": ["buah mulut", "buah tangan", "buah hati", "buah pena"],
                "ans": "buah mulut",
                "expl": "話題の種、噂の的は `buah mulut`（または `buah bibir`）です。"
            },
            {
                "q": "「道路上での接触事故をきっかけに、当事者同士が激しい口喧嘩・口論を交わすこと」を表す連語はどれか。",
                "choices": ["adu mulut", "tutup mulut", "ambil alih", "cuci tangan"],
                "ans": "adu mulut",
                "expl": "激しい口論・口げんかは `adu mulut` です。"
            }
        ],
        "culture_column": {
            "title": "「Mulutmu Harimaumu」にみるインドネシアの言霊思想",
            "body": "インドネシアで最も有名なことわざの一つに「Mulutmu harimaumu yang akan menerkam kepalamu（お前の口は、お前自身の頭を噛み砕くトラである）」があります。軽率な一言や不誠実な嘘、陰口が、最終的には自分自身の身を滅ぼす猛獣となって襲いかかるという教訓です。日本の一言居士や「口は災いの元」と同様、言葉の持つ呪力（kesaktian kata）に対する畏敬と慎重さが強調されています。"
        }
    },
    {
        "filename": "docs/lexicon/22-noun-collocations-telinga.md",
        "title": "【共起連語】身体名詞 telinga の連語辞典：tebal telinga / merah telinga / pasang telinga / masuk telinga kanan",
        "root": "telinga",
        "meaning": "耳、聴覚、情報受容、聞き役",
        "core_concept": "音や声を受け止める感覚器官「耳」から、「批判や罵声を平気で聞き流す面の皮の厚さ」「屈辱的な言葉に激怒して耳が赤くなること」「聞き耳を立てて集中する」「右の耳から入って左の耳から抜ける（馬耳東風）」という、批判耐性・屈辱・情報収集・聞き流しのメタファーを展開します。",
        "table_rows": [
            ("tebal telinga", "厚い耳", "面の皮が厚い、批判に動じない、悪口を平気で聞き流す", "性格/批判", "Sebagai pejabat publik, ia harus tebal telinga menghadapi cemoohan netizen di media sosial."),
            ("merah telinga", "赤い耳", "激怒する、侮辱に屈辱を感じてかっとなる", "感情/怒り", "Merah telinga sang manajer mendengar kata-kata kasar yang dilontarkan oleh klien."),
            ("pasang telinga", "耳を据える", "耳を澄ます、聞き耳を立てる、情報収集に努める", "注意/日常", "Warga desa pasang telinga baik-baik mendengarkan instruksi peringatan dini tsunami."),
            ("masuk telinga kanan keluar telinga kiri", "右耳から入って左耳から出る", "右から左へ聞き流す、馬耳東風、全く身につかない", "教育/戒め", "Nasihat orang tua itu cuma masuk telinga kanan keluar telinga kiri bagi remaja pembangkang."),
            ("sakit telinga", "耳が痛い", "聞くに耐えない悪口、耳障りな騒音、耳の痛み", "感覚/心理", "Sakit telinga rasanya mendengar fitnah murahan yang terus diulang-ulang di televisi."),
            ("telinga tipis", "薄い耳", "怒りっぽい、悪口を真に受けてすぐ怒る、傷つきやすい", "性格/短所", "Jangan terlalu telinga tipis jika ingin berkarier di dunia politik yang keras."),
            ("daun telinga", "耳の葉", "耳介、耳たぶ、耳の外側の軟骨部", "解剖/身体", "Dokter memeriksa adanya pembengkakan pada daun telinga pasien akibat infeksi.")
        ],
        "details": [
            {
                "term": "tebal telinga (kebal terhadap celaan / muka tebal)",
                "trans": "批判を平気で聞き流す、面の皮が厚い、へこたれない",
                "nuance": "中傷や厳しい批判、ブーイングを浴びせられても、全く気に留めず平然としている鈍感力やふてぶてしさを指します。政治家には必須の資質とも言われます。",
                "ex_id": "Politisi kawakan itu sudah sangat tebal telinga terhadap segala tudingan miring dari kubu oposisi.",
                "ex_kana": "ポリティシ カワカン イトゥ スダ サンガット トゥバル トゥリンガ トゥルハダップ スガラ トゥディンガン ミリン ダリ クブ オポスィシ",
                "ex_ja": "その老獪な政治家は、野党陣営からのあらゆる邪推や非難に対して極めて厚い耳（tebal telinga / 驚異的な鈍感力）を持っています。",
                "note": "批判耐性の高さを表す両義的な表現です。"
            },
            {
                "term": "merah telinga (sangat marah karena tersinggung)",
                "trans": "屈辱で激怒する、耳まで真っ赤になって怒る",
                "nuance": "人格や自尊心を傷つけられる侮辱やからかいを受け、血圧が急上昇して耳がカーッと熱くなるほどの怒りを描写します。",
                "ex_id": "Mendengar ayahnya dihina di depan umum, merah telinganya dan ia nyaris melayangkan pukulan.",
                "ex_kana": "ムンデンガル アヤフニャ ディヒナ ディ ドゥパン ウムム、メラ トゥリンガニャ ダン イア ニャリス ムラヤンカン プクラン",
                "ex_ja": "父親が人前で侮辱されるのを聞き、彼は耳まで真っ赤になって激怒し（merah telinga）、あやうく殴りかかるところでした。",
                "note": "生理的反応と感情が直結した慣用表現です。"
            },
            {
                "term": "masuk telinga kanan keluar telinga kiri",
                "trans": "右の耳から入って左の耳から抜ける、馬耳東風",
                "nuance": "教師や親の貴重な忠告や教訓を、その場では聞いているふりをしながら全く記憶にも留めず聞き流してしまう軽薄さを戒める定番の成句です。",
                "ex_id": "Semua teguran mengenai keselamatan kerja tampaknya cuma masuk telinga kanan keluar telinga kiri bagi pekerja tambang itu.",
                "ex_kana": "スムア トゥグラン ムンゲナイ クスラマタン クルジャ タンパックニャ チュマ マスッ トゥリンガ カナン クルアル トゥリンガ キリ バギ プクルジャ タンバン イトゥ",
                "ex_ja": "労働安全に関するすべての注意喚起は、その鉱山作業員にとっては単に右の耳から入って左の耳から抜ける（馬耳東風）だけのようでした。",
                "note": "日本の「馬の耳に念仏」「右から左へ聞き流す」と完全一致します。"
            },
            {
                "term": "telinga tipis (mudah tersinggung dan marah)",
                "trans": "すぐに怒る、悪口を真に受けてカッとなる、怒りっぽい",
                "nuance": "`tebal telinga`（厚い耳＝鈍感力）の対義語で、他人の些細な批判やからかいに敏感に反応し、すぐに腹を立ててしまう心の狭さを指します。",
                "ex_id": "Sebagai pimpinan organisasi, kamu jangan telinga tipis saat menerima kritik dari anggota muda.",
                "ex_kana": "スバガイ ピンピナン オルガニサシ、カム ジャンガン トゥリンガ ティピス サアット ムヌリマ クリティック ダリ アンゴタ ムダ",
                "ex_ja": "組織のリーダーとして、若いメンバーからの批判を受け止める際にすぐにカッとなって怒る（telinga tipis）な。",
                "note": "器の小ささを指摘する表現です。"
            },
            {
                "term": "pasang telinga (mendengarkan dengan sangat seksama)",
                "trans": "聞き耳を立てる、全集中して聴取する",
                "nuance": "重要な発表や機密情報を逃すまいと、周囲の雑音を遮断して耳を傾ける意図的動作です。",
                "ex_id": "Para investor pasang telinga menanti pidato gubernur bank sentral mengenai arah suku bunga acuan.",
                "ex_kana": "パラ インヴェストール パサン トゥリンガ ムナンティ ピダト グブルヌル バンク セントラル ムンゲナイ アラー スク ブンガ アチュアン",
                "ex_ja": "投資家たちは政策金利の方向性に関する中央銀行総裁の演説を待って、固唾を呑んで聞き耳を立て（pasang telinga）ました。",
                "note": "情報の重要性を強調する表現です。"
            }
        ],
        "dialogue": {
            "title": "SNSの炎上批判と政治家のメンタル",
            "lines": [
                ("Surya", "Pak, serangan warganet terhadap pernyataan Bapak kemarin di televisi sangat gencar dan kasar."),
                ("Pak Anggota Dewan", "Biar saja, Surya. Kalau mau jadi wakil rakyat, kita harus tebal telinga menghadapi hujatan publik."),
                ("Surya", "Tapi beberapa staf fraksi mulai merah telinga dan ingin membalas komentar mereka secara agresif."),
                ("Pak Anggota Dewan", "Jangan terpancing! Menjadi telinga tipis di media sosial hanya akan merusak reputasi partai kita.")
            ],
            "trans": [
                ("スーリャ", "先生、昨日のテレビでの先生のご発言に対するネットユーザーのバッシングは極めて猛烈で過激です。"),
                ("議員先生", "放っておきなさい、スーリャ君。国民の代表になろうとするなら、大衆の罵声に対して厚い耳（tebal telinga / 批判耐性）を持たねばならんよ。"),
                ("スーリャ", "しかし会派のスタッフ数名が激怒して（merah telinga）、攻撃的にコメントをやり返そうとしています。"),
                ("議員先生", "挑発に乗るな！SNSですぐカッとなる怒りっぽい態度（telinga tipis）を取れば、我が党の評判を損なうだけだ。")
            ]
        },
        "grammar_points": [
            "**tebal vs tipis の対立体系**: \n- `tebal telinga`（耳が厚い ＝ 批判を気にしない鈍感力） vs `telinga tipis`（耳が薄い ＝ すぐ傷つき怒る狭量さ）\n- `tebal muka`（面の皮が厚い ＝ 恥知らず） vs `tipis muka`（恥ずかしがり屋）\n身体の「厚さ（tebal）」と「薄さ（tipis）」が精神的耐性の比喩として見事に対立しています。",
            "**空間移動の比喩 masuk ... keluar ...**: `masuk telinga kanan keluar telinga kiri` は、前置詞句が対句構造となって「情報が素通りして一切定着しない無意味さ」をリズミカルに表現しています。"
        ],
        "quizzes": [
            {
                "q": "「大衆からの批判や悪口を平気で受け流し、動じない面の皮の厚さ・鈍感力」を表す身体連語はどれか。",
                "choices": ["tebal telinga", "telinga tipis", "merah telinga", "pasang telinga"],
                "ans": "tebal telinga",
                "expl": "批判に動じない厚い耳・鈍感力は `tebal telinga` です。"
            },
            {
                "q": "「親や上司の忠告をその場で聞き流し、全く身につかない馬耳東風の状態」を表す成句はどれか。",
                "choices": ["masuk telinga kanan keluar telinga kiri", "pasang telinga baik-baik", "tutup telinga rapat-rapat", "merah telinga mendengarnya"],
                "ans": "masuk telinga kanan keluar telinga kiri",
                "expl": "右から左へ聞き流す・馬耳東風は `masuk telinga kanan keluar telinga kiri` です。"
            },
            {
                "q": "「侮辱やからかいを浴びせられて激怒し、耳まで真っ赤になって怒る」を表す表現はどれか。",
                "choices": ["merah telinga", "daun telinga", "tebal telinga", "sakit telinga"],
                "ans": "merah telinga",
                "expl": "激怒して耳を赤くするのは `merah telinga` です。"
            }
        ],
        "culture_column": {
            "title": "「Telinga」にみるジャワ宮廷の忍耐美学（Tepa Selira）",
            "body": "ジャワの伝統的な人間教育において、他者の挑発的な発言に対して即座に激怒（merah telinga）することは未熟さ（durung Jawa＝まだ真のジャワ人ではない）の証とみなされます。自制心（ngempet）を発揮し、他者の立場を察しながら穏やかに聞き流す（tebal telinga）ことこそが高貴な人間（priyayi）の証とされました。耳の表現には、東南アジアの調和を重んじる精神修養の伝統が息づいています。"
        }
    },
    {
        "filename": "docs/lexicon/23-noun-collocations-hidung.md",
        "title": "【共起連語】身体名詞 hidung の連語辞典：hidung belang / batang hidung / mencium bau / menarik hidung",
        "root": "hidung",
        "meaning": "鼻、嗅覚、顔の突起、存在の象徴",
        "core_concept": "顔の中央に突き出た呼吸・嗅覚器官「鼻」から、「女性関係にだらしない女たらし」「本人の姿・顔立ち（鼻柱）」「不正や危機の異変を嗅ぎつける」「牛のように言いなりに引きずり回される」という、色情・存在感・鋭敏な察知・盲従のユニークなメタファーを形成します。",
        "table_rows": [
            ("hidung belang", "斑点の鼻", "女たらし、好色漢、浮気男、スケベ", "俗語/風俗", "Wanita itu memperingatkan adiknya agar menjauhi pria hidung belang di klub malam."),
            ("batang hidung", "鼻の柱", "鼻筋、（比喩で）本人の姿、顔立ち（tak tampak batang hidungnya）", "日常/慣用", "Sudah ditunggu berjam-jam di kantor, batang hidungnya belum juga kelihatan."),
            ("mencium bau busuk", "腐った臭いを嗅ぐ", "不正・悪事の気配を嗅ぎつける、疑念を抱く", "事件/司法", "KPK mulai mencium bau busuk adanya suap dalam proyek pengadaan pengadaan alat kesehatan."),
            ("menarik hidung", "鼻を引っ張る", "言いなりにする、牛のように意のままに操る", "支配/比喩", "Rakyat tidak mau lagi ditarik hidungnya oleh politisi korup yang menebar janji palsu."),
            ("mancung hidung", "高い鼻", "鼻が高い、西洋風のすっと通った鼻筋", "容姿/美", "Banyak orang mengagumi paras artis blesteran itu karena memiliki hidung yang mancung."),
            ("hidung pesek", "低い鼻", "団子鼻、鼻が低い（親しみ・愛嬌の身体特徴）", "容姿/口語", "Meskipun memiliki hidung pesek, senyumannya yang manis membuat semua orang menyukainya."),
            ("hidung belang kelas kakap", "巨大スナッパー級の斑点鼻", "大物の悪名高き女たらし、常習的プレイボーイ", "俗語/強調", "Aparat kepolisian menggerebek mucikari yang sering melayani pria hidung belang kelas kakap.")
        ],
        "details": [
            {
                "term": "hidung belang (pria hidung belang / buaya darat)",
                "trans": "女たらし、浮気男、好色漢、プレイボーイ",
                "nuance": "女性を騙したり買春を繰り返したりする不誠実な男性を軽蔑して呼ぶ、インドネシア語で最も有名な俗語的イディオムです（同義語: `buaya darat`＝陸のワニ）。",
                "ex_id": "Korban penipuan asmara itu baru menyadari bahwa tunangannya adalah seorang hidung belang berkantong tebal.",
                "ex_kana": "コルバン プニプアン アスマラ イトゥ バル ムニャダリ バフワ トゥナンガンニャ アダラー スオラン ヒドゥン ブラン ブルカントン トゥバル",
                "ex_ja": "その結婚詐欺の被害者は、自らの婚約者が金回りの良い札付きの女たらし（hidung belang）であったことにようやく気づきました。",
                "note": "オランダ植民地時代のバタヴィアの故事に由来します。"
            },
            {
                "term": "batang hidung (tampak batang hidungnya)",
                "trans": "本人の姿、本人の顔（通例否定形で「姿を見せない」）",
                "nuance": "顔の中で最も目立つ「鼻筋（batang hidung）」を人間の存在の象徴（換喩 / metonymy）とし、「約束の時間になっても影も形も見当たらない」という苛立ちを表現します。",
                "ex_id": "Rapat sudah dimulai sejak setengah jam lalu, tetapi batang hidung manajer proyek belum juga tampak.",
                "ex_kana": "ラパット スダ ディムライ スジャッ ストゥンガ ジャム ラル、トゥタピ バタン ヒドゥンニャ マナジェール プロイェッ スブルム ジュガ タンパック",
                "ex_ja": "会議は30分前から始まっているのに、プロジェクトマネージャーの姿（batang hidung）はまだどこにも見当たりません。",
                "note": "`belum tampak batang hidungnya`（姿を現さない）という否定定型句です。"
            },
            {
                "term": "mencium bau busuk / bau amis",
                "trans": "不正や悪事のきな臭い気配を嗅ぎつける",
                "nuance": "公的機関やジャーナリストが、表向きは正常に見える入札や政策決定の裏に潜む汚職（korupsi）や贈収賄の兆候を鋭く察知する場面で用いられます。",
                "ex_id": "Wartawan investigasi mulai mencium bau busuk aliran dana mencurigakan ke rekening rekening keluarga pejabat.",
                "ex_kana": "ワルタワン インヴェスティガシ ムライ ムンチウム バウ ブスッ アリラン ダナ ムンチュリガカン ケ ルクニン クルアルガ プジャバット",
                "ex_ja": "調査報道記者は、高官家族の口座への不審な資金流出というきな臭い不正の臭い（mencium bau busuk）を嗅ぎつけ始めました。",
                "note": "汚職報道の超定番比喩です。"
            },
            {
                "term": "ditarik hidungnya (seperti kerbau dicocok hidungnya)",
                "trans": "鼻面を引き回される、言いなりになって盲従する",
                "nuance": "鼻輪（keluan）を通された水牛（kerbau）が農夫の引く綱のままにおとなしく従うことわざ（Bagai kerbau dicocok hidung）に由来し、主体性を失って操られている人間を皮肉ります。",
                "ex_id": "Jangan mau ditarik hidungmu oleh kelompok kepentingan yang hanya memanfaatkan kepolosanmu.",
                "ex_kana": "ジャンガン マウ ディタリッ ヒドゥンム オレ クロンポッ クプンティンガン ヤン ハニャ ムマンファアトカン クポロサンム",
                "ex_ja": "君の純真さを利用しているだけの利害集団に、鼻面を引き回される（ditarik hidung）ような真似はするな。",
                "note": "ことわざに直結する比喩です。"
            },
            {
                "term": "hidung mancung vs hidung pesek",
                "trans": "鼻が高い（すっと通った鼻） vs 団子鼻（低い鼻）",
                "nuance": "身体的特徴の描写として日常会話で極めて頻繁に使われます。西洋人や中東系混血のすっと通った鼻を `mancung`、東南アジア土着の愛らしい丸い鼻を `pesek` と呼びます。",
                "ex_id": "Banyak gadis remaja mendambakan hidung mancung seperti para bintang drama Korea.",
                "ex_kana": "バニャッ ガディス ルマジャ ムンダムバカン ヒドゥン マンチュン スプルティ パラ ビンタン ドラマ コレア",
                "ex_ja": "多くの若い女性たちが、韓国ドラマのスターのような高くすっと通った鼻筋（hidung mancung）に憧れています。",
                "note": "日常の容姿描写の基本対照ペアです。"
            }
        ],
        "dialogue": {
            "title": "遅刻した取引先の担当者と不正の噂",
            "lines": [
                ("Adit", "Pak, vendor penyedia server kita belum juga kelihatan batang hidungnya padahal sudah jam sepuluh."),
                ("Pak Harun", "Aneh sekali. Padahal hari ini jadwal penandatanganan berita acara serah terima barang."),
                ("Adit", "Saya dengar dari divisi audit, mereka mulai mencium bau busuk pemalsuan spesifikasi perangkat keras."),
                ("Pak Harun", "Waduh! Pantas saja dia sengaja menghindar dan tidak berani menampakkan batang hidungnya di sini.")
            ],
            "trans": [
                ("アディット", "部長、サーバー納入ベンダーの担当者、もう10時だというのに姿（batang hidung）すら見えませんよ。"),
                ("ハルン部長", "おかしいな。今日は検収引き渡し書の調印予定日だというのに。"),
                ("アディット", "監査部門から聞いたのですが、ハードウェアスペックの偽装というきな臭い不正の臭い（mencium bau busuk）を嗅ぎつけ始めているそうです。"),
                ("ハルン部長", "なんと！道理であいつが意図的に逃げ回って、ここに姿を現そうと（menampakkan batang hidungnya）しないわけだ。")
            ]
        },
        "grammar_points": [
            "**換喩（Metonymy）としての batang hidung**: 部分をもって全体（人間そのもの）を表す修辞技法です。通常、否定詞 `belum` や `tidak` を伴って `belum tampak batang hidungnya`（まだ姿を見せない）という固定チャンクとして用いられます。",
            "**hidung belang の歴史的語源**: 17世紀のオランダ領バタヴィアで、総督ヤン・ピーテルスゾーン・クーンが寝取られ姦通事件を起こした士官ピーター・コルテホーファーの鼻に炭で「まだら模様（belang）」を塗って公衆の面前で晒し者にした史実に由来すると言われています。"
        ],
        "quizzes": [
            {
                "q": "「女性関係にだらしなく、言葉巧みに女性を口説いて騙す浮気男・女たらし」を意味する有名な俗語表現はどれか。",
                "choices": ["hidung belang", "batang hidung", "kaki tangan", "tangan kanan"],
                "ans": "hidung belang",
                "expl": "女たらし、浮気男は `hidung belang`（または `buaya darat`）です。"
            },
            {
                "q": "「待ち合わせの時間になっても、本人の姿や顔が一向に見当たらない」ことを表す定番の身体連語はどれか。",
                "choices": ["belum kelihatan batang hidungnya", "sudah mencium bau busuk", "ditarik hidungnya", "memutar balik lidah"],
                "ans": "belum kelihatan batang hidungnya",
                "expl": "姿を現さない・顔を見せないは `belum kelihatan batang hidungnya` です。"
            },
            {
                "q": "捜査機関や記者が「入札や事業の裏に潜む不正・汚職のきな臭い気配を察知する」を表す表現はどれか。",
                "choices": ["mencium bau busuk", "menarik hidung", "membuat onar", "tutup usia"],
                "ans": "mencium bau busuk",
                "expl": "不正の気配を嗅ぎつけるは `mencium bau busuk` です。"
            }
        ],
        "culture_column": {
            "title": "「Bagai Kerbau Dicocok Hidung」と民衆の自立",
            "body": "水田を耕す温順な水牛の鼻に穴を開けて縄を通す「cocok hidung」。どんなに巨躯を誇る水牛であっても、鼻の急所を握られれば子どもの力でも自在に誘導されてしまいます。この光景から生まれたことわざ `Bagai kerbau dicocok hidung`（鼻輪を通された水牛のよう）は、植民地支配や権力者のプロパガンダに唯々諾々と盲従する無知への深い警鐘として、インドネシアの独立運動期から民衆を覚醒させる合言葉として語り継がれています。"
        }
    },
    {
        "filename": "docs/lexicon/24-noun-collocations-muka.md",
        "title": "【共起連語】身体名詞 muka の連語辞典：muka masam / cari muka / tebal muka / uang muka / buang muka",
        "root": "muka",
        "meaning": "顔、前面、表情、世間体、面目",
        "core_concept": "他者と対峙する人体の正面「顔」から、「不機嫌で酸っぱい仏頂面」「上司に取り入って点数を稼ぐ（顔を探す）」「恥知らずな面の皮の厚さ」「売買契約の手付金・頭金」「顔を背ける無視」という、表情心理・出世欲・羞恥心・商取引の多面的な連語世界を形成します。",
        "table_rows": [
            ("muka masam", "酸っぱい顔", "不機嫌な顔、仏頂面、むっとした表情", "表情/感情", "Pelayan restoran itu ditegur manajer karena melayani pelanggan dengan muka masam."),
            ("cari muka", "顔を探す", "ゴマをする、点数稼ぎをする、上司に取り入る", "職場/批判", "Karyawan penjilat itu suka cari muka di depan direksi saat ada acara kantor."),
            ("tebal muka", "厚い顔", "恥知らずな、厚かましい、面の皮が厚い", "道徳/非難", "Koruptor itu masih tebal muka tersenyum di depan kamera wartawan tanpa rasa bersalah."),
            ("uang muka (DP)", "前のお金", "頭金、手付金、内金（Down Payment）", "金融/商取引", "Pembelian rumah subsidi ini memerlukan uang muka sebesar sepuluh persen dari total harga."),
            ("buang muka", "顔を捨てる", "顔を背ける、知らぬふりをする、無視する", "態度/冷淡", "Ketika berpapasan di koridor kampus, mantan pacarnya malah buang muka."),
            ("buka muka", "顔を開く", "素顔をさらす、正体を明かす、ベールを脱ぐ", "比喩/暴露", "Akhirnya peretas anonim yang meresahkan itu dipaksa buka muka di hadapan penyidik."),
            ("jaga muka", "顔を守る", "面目を保つ、メンツを立てる、恥をかかないようにする", "社交/名誉", "Tuan rumah berusaha sebaik mungkin menyajikan hidangan lezat demi menjaga muka keluarga.")
        ],
        "details": [
            {
                "term": "cari muka (menjilat atasan demi keuntungan pribadi)",
                "trans": "点数稼ぎをする、ゴマをする、上司に取り入る",
                "nuance": "実質的な仕事の成果ではなく、上司や権力者の前でだけ熱心に働いているふりをしたり、過剰なお世辞を言って自らの昇進や評価を上げようとする卑しい態度を痛烈に批判する言葉です。",
                "ex_id": "Jangan cuma rajin saat ada bos lewat, rekan-rekanmu tahu kalau kamu cuma sedang cari muka.",
                "ex_kana": "ジャンガン チュマ ラジン サアット アダ ボス レワット、ルカンルカンム タフ カロウ カム チュマ スダン チャリ ムカ",
                "ex_ja": "上司が通りかかった時だけ熱心に振る舞うな、君が単に点数稼ぎ（cari muka）をしていることなど同僚たちはお見通しだ。",
                "note": "職場での最も軽蔑される行動の一つです。"
            },
            {
                "term": "muka masam (wajah cemberut tidak ramah)",
                "trans": "仏頂面、不機嫌な表情、不満げな顔つき",
                "nuance": "`masam` は「酸っぱい」を意味し、レモンをかじった時のような歪んだ不機嫌な顔つきを描写します。接客業や対人マナーで厳禁とされる態度です。",
                "ex_id": "Meskipun merasa lelah setelah bekerja seharian, jangan sampai menyambut tamu dengan muka masam.",
                "ex_kana": "ムスキプン ムラサ レラー ステラ ブルクルジャ スハリアン、ジャンガン サンパイ ムニャムブット タム ドゥンガン ムカ マサム",
                "ex_ja": "一日中働いて疲れているとしても、仏頂面（muka masam）でお客様を迎えるようなことがあってはなりません。",
                "note": "接客研修の禁止事項として頻出します。"
            },
            {
                "term": "tebal muka (tidak tahu malu / muka tembok)",
                "trans": "恥知らずな、厚かましい、面の皮が厚い",
                "nuance": "悪事や失態を犯して世間から糾弾されているにもかかわらず、平然と振る舞い反省の色を見せない不届き者を非難します（同義語: `muka tembok`＝壁の顔/鉄面皮）。",
                "ex_id": "Sudah tertangkap basah mencuri anggaran desa, terdakwa masih tebal muka membantah semua bukti.",
                "ex_kana": "スダ トゥルタンカップ バサー ムンチュリ アンガラン デサ、トゥルダクワ マシー トゥバル ムカ ムンバンター スムア ブクティ",
                "ex_ja": "村の予算横領で現行犯逮捕されたにもかかわらず、被告人は面の皮厚く（tebal muka）すべての証拠を否認し続けています。",
                "note": "道徳的破廉恥さを糾弾する表現です。"
            },
            {
                "term": "uang muka (down payment / DP)",
                "trans": "頭金、手付金、内金",
                "nuance": "不動産購入、自動車ローン、工事請負契約などにおいて、契約締結時に前払いで支払う初期費用を指す標準商用用語です。日常では英語の頭文字 `DP`（デー・ペー）とも呼ばれます。",
                "ex_id": "Calon pembeli wajib membayar uang muka sebesar dua puluh persen saat penandatanganan perjanjian jual beli.",
                "ex_kana": "チャロン プムベリ ワジブ ムンバヤル ウアン ムカ スブサール ドゥアプル パーセン サアット プナンダタンガナン プルジャンジアン ジュアル ベリ",
                "ex_ja": "購入希望者は、売買契約の調印時に20％の頭金（uang muka）を支払わなければなりません。",
                "note": "ビジネス・商取引の必須重要語彙です。"
            },
            {
                "term": "jaga muka (menjaga gengsi / kehormatan)",
                "trans": "メンツを保つ、面目を保つ、世間体を守る",
                "nuance": "東洋社会特有の「メンツ（gengsi / kehormatan）」を傷つけないよう、儀礼やもてなし、身だしなみに細心の配慮を払う文化的行動です。",
                "ex_id": "Demi menjaga muka keluarga besar di hadapan besan, resepsi pernikahan itu digelar secara megah.",
                "ex_kana": "デミ ムンジャガ ムカ クルアルガ ブサール ディ ハダパン ベサン、レセプスィ プルニカハン イトゥ ディゲラール スチャラ ムガー",
                "ex_ja": "嫁ぎ先の親族の前で一族のメンツを保つ（jaga muka）ため、その結婚披露宴は盛大に執り行われました。",
                "note": "社交文化の核心概念です。"
            }
        ],
        "dialogue": {
            "title": "マイホーム購入の頭金と職場の人間関係",
            "lines": [
                ("Ilham", "Wah, saya dengar kamu baru saja membayar uang muka untuk rumah baru di BSD?"),
                ("Riko", "Iya, Alhamdulillah, tabungan lima tahun akhirnya cukup untuk bayar uang muka 15 persen."),
                ("Ilham", "Hebat! Jangan seperti si Doni ya, kerjanya cuma cari muka di depan bos tapi kinerjanya nol besar."),
                ("Riko", "Ah, biarkan saja. Saya lebih memilih fokus bekerja jujur demi menjaga muka keluarga daripada cari muka begitu.")
            ],
            "trans": [
                ("イルハム", "おお、BSDの新築住宅の頭金（uang muka）を支払ったらしいじゃないか？"),
                ("リコ", "ええ、おかげさまで。5年間の貯金がようやく15％の頭金を払うのに十分な額になりました。"),
                ("イルハム", "素晴らしい！ドニのようになってはいけないよ。あいつはボスの前で点数稼ぎ（cari muka）ばかりして、実績はゼロだからね。"),
                ("リコ", "まあ、放っておきましょう。そんな点数稼ぎをするより、家族のメンツを守る（menjaga muka）ために誠実に働くことを選びますよ。")
            ]
        },
        "grammar_points": [
            "**muka と wajah の使い分け**: 解剖学的・中立的な「顔立ち」は `wajah`（美しい顔: `wajah cantik`）が好まれます。一方、成句や慣用表現（cari muka, tebal muka, uang muka, buang muka）では圧倒的に語根 `muka` が用いられます。",
            "**前置詞としての di muka**: `muka` は「前面」を意味するため、文語の前置詞句 `di muka umum`（公衆の面前で）、`ke muka`（前方へ）としてフォーマルな文章で多用されます。"
        ],
        "quizzes": [
            {
                "q": "「実質的な実力ではなく、上司の前でだけ熱心に振る舞って点数稼ぎをする・取り入る」を意味する成句はどれか。",
                "choices": ["cari muka", "tebal muka", "buang muka", "jaga muka"],
                "ans": "cari muka",
                "expl": "上司にゴマすりをして点数稼ぎをする行為は `cari muka` です。"
            },
            {
                "q": "不動産や自動車などの高額商品の売買契約時に支払う「頭金・手付金」の正式なインドネシア語はどれか。",
                "choices": ["uang muka", "uang tutup mulut", "uang receh", "uang pelicin"],
                "ans": "uang muka",
                "expl": "頭金・手付金は `uang muka`（通称 DP）です。"
            },
            {
                "q": "「公衆や親族の前で一族のメンツや世間体を保つ・恥をかかないようにする」を表す表現はどれか。",
                "choices": ["jaga muka", "buka muka", "muka masam", "buang muka"],
                "ans": "jaga muka",
                "expl": "メンツや面目を保つことは `jaga muka` です。"
            }
        ],
        "culture_column": {
            "title": "「Cari Muka」とインドネシアの職場ポリティクス",
            "body": "上下関係やパトロン・クライアント関係が色濃く残るインドネシアの伝統的組織において、上司（Bapak）の機嫌を伺って寵愛を得ようとする `cari muka`（顔を探す）は、実力主義（meritokrasi）を阻害する悪弊としてしばしば風刺されます。現代のスタートアップや多国籍企業では、透明なKPI評価制度を導入して「顔色伺い」を排除し、具体的な成果で評価する職場改革が進められています。"
        }
    },
    {
        "filename": "docs/lexicon/25-noun-collocations-darah.md",
        "title": "【共起連語】身体名詞 darah の連語辞典：darah daging / darah dingin / darah biru / naik darah / darah muda",
        "root": "darah",
        "meaning": "血、血液、血統、情熱、激情",
        "core_concept": "血管を巡る赤い生命の液体「血」から、「実の我が子・血肉を分けた肉親」「冷酷非情な性格」「王侯貴族の高貴な血統」「頭に血がのぼる激怒」「血気盛んな若者」という、血縁・性格・階層・情動の強烈なメタファーを構成します。",
        "table_rows": [
            ("darah daging", "血と肉", "実の子、実子、血を分けた我が子、血肉", "家族/情愛", "Bagaimanapun nakalnya anak itu, ia tetaplah darah daging saya sendiri."),
            ("darah dingin", "冷たい血", "冷酷非情な、冷徹な、平然と残虐なことをする（pembunuh berdarah dingin）", "事件/心理", "Pelaku melakukan aksi keji tersebut dengan darah dingin tanpa menunjukkan penyesalan."),
            ("darah biru", "青い血", "貴族の血筋、名門の家柄、王族の血統", "階層/歴史", "Meskipun merupakan keturunan darah biru Keraton Surakarta, ia tetap hidup sederhana."),
            ("naik darah", "血が上がる", "激怒する、血圧が上がる、頭に血がのぼる", "感情/怒り", "Sikap arogan sopir truk yang ugal-ugalan membuat warga sekitar naik darah."),
            ("darah muda", "若い血", "若者、青年期、血気盛んな若気の至り", "大衆文化/情熱", "Darah muda memang penuh semangat dan idealisme, namun perlu diimbangi kebijaksanaan."),
            ("donor darah", "血の寄付", "献血、輸血のための血液提供", "医療/福祉", "Palang Merah Indonesia mengadakan bakti sosial donor darah massal di kampus."),
            ("tekanan darah", "血の圧力", "血圧（tekanan darah tinggi: 高血圧）", "医療/健康", "Dokter menyarankan pasien mengurangi konsumsi garam demi menjaga tekanan darah tetap normal.")
        ],
        "details": [
            {
                "term": "darah daging (anak kandung sendiri)",
                "trans": "実の子、血を分けた我が子、骨肉",
                "nuance": "自らの体から生まれた実の子どもに対する断ち切れない深い愛情を表す最も情緒的な言葉です。どんな過ちを犯した子であっても見捨てられない親心の文脈で感動を呼びます。",
                "ex_id": "Seorang ibu rela mengorbankan nyawanya demi melindungi darah dagingnya dari marabahaya.",
                "ex_kana": "スオラン イブ ルラ ムンゴルバンカン ニャワニャ デミ ムルインドゥンギ ダラー ダギンニャ ダリ マラバハヤ",
                "ex_ja": "母親は、自らの血を分けた我が子（darah daging）を危険から守るためなら命を投げ出すことも厭いません。",
                "note": "親子の情愛を描く最高峰の表現です。"
            },
            {
                "term": "darah dingin (berdarah dingin / kejam tanpa empati)",
                "trans": "冷酷非情な、平然と悪事を犯す、冷血な",
                "nuance": "一切の罪悪感や同情心を持たず、計算ずくで残虐な犯行を実行する犯罪者を描写する成句です（例: `pembunuh berdarah dingin`＝冷酷な殺人鬼）。",
                "ex_id": "Penyidik kepolisian menggambarkan tersangka sebagai sosok berdarah dingin yang merencanakan aksinya berbulan-bulan.",
                "ex_kana": "プニェディッ クポリシアン ムンガンバルカン トゥルサンカ スバガイ ソソッ ブルダラー ディンギン ヤン ムレンチャナカン アクシニャ ブルブランブラン",
                "ex_ja": "警察の捜査官は、その容疑者を何ヶ月も前から犯行を計画していた冷血な（berdarah dingin）人物として描写しました。",
                "note": "接頭辞 `ber-` を伴う `berdarah dingin` の形で多用されます。"
            },
            {
                "term": "darah biru (bangsawan / priyayi keningratan)",
                "trans": "貴族の血筋、青い血、名門王族の末裔",
                "nuance": "ヨーロッパの「blue blood」と同様、ジャワの王宮（Keraton）や群島の伝統首長層（Bangsawan）の家系に生まれた血統的高貴さを指します。",
                "ex_id": "Tradisi perkawinan di masa lampau sangat ketat menjaga agar kaum darah biru tidak menikah dengan rakyat jelata.",
                "ex_kana": "トラディシ プルカウィナン ディ マサ ランパウ サンガット クタット ムンジャガ アガル カウム ダラー ビル ティダッ ムニカ ドゥンガン ラクヤット ジュラタ",
                "ex_ja": "過去の婚姻慣習においては、青い血を引く貴族階層（darah biru）が平民と結婚しないよう極めて厳格に統制されていました。",
                "note": "歴史・文化小説で頻出します。"
            },
            {
                "term": "darah muda (jiwa muda yang bergejolak)",
                "trans": "血気盛んな若者、若気の至り、青年の情熱",
                "nuance": "恐れを知らない理想主義、情熱、そして時に無謀な無鉄砲さを併せ持つ青春期の心理状態を親しみを込めて表現します。",
                "ex_id": "Wajar jika darah muda suka mencoba hal-hal baru dan menantang status quo.",
                "ex_kana": "ワジャル ジュカ ダラー ムダ スカ ムンチョバ ハルハル バル ダン ムナンタン ステイタス クオ",
                "ex_ja": "血気盛んな若い世代（darah muda）が新しい物事に挑戦し、現状（ステータスクオ）に挑もうとするのは当然のことです。",
                "note": "ダンドゥットの帝王ロマ・イラマの大ヒット曲の題名でも有名です。"
            },
            {
                "term": "naik darah (naik pitam / tersulut amarah)",
                "trans": "頭に血がのぼる、激怒する",
                "nuance": "血圧が急上昇して怒りがコントロールできなくなる状態を描く身体連語です（前述の動詞 `naik` の項でも解説）。",
                "ex_id": "Melihat anaknya diperlakukan tidak adil di sekolah, sang ayah langsung naik darah mendatangi kepala sekolah.",
                "ex_kana": "ムリハット アナッニャ ディプルラクカン ティダッ アディル ディ スコラ、サン アヤ ラングスン ナイッ ダラー ムンダタンギ クパラ スコラ",
                "ex_ja": "学校で我が子が不当な扱いを受けたのを見て、父親は激怒して頭に血をのぼらせ（naik darah）、直ちに校長のもとへ乗り込みました。",
                "note": "怒りの激情を表す定番表現です。"
            }
        ],
        "dialogue": {
            "title": "非行に走る息子と親子の血の絆",
            "lines": [
                ("Pak Danu", "Saya benar-benar naik darah mendengar anak saya terlibat tawuran antarpelajar kemarin."),
                ("Ibu Danu", "Sabar, Pak. Dia masih darah muda, emosinya masih labil dan mudah terpengaruh teman sebaya."),
                ("Pak Danu", "Tapi tindakannya sudah membahayakan nyawa orang lain! Apakah kita harus lapor polisi?"),
                ("Ibu Danu", "Bagaimanapun kesalahannya, dia adalah darah daging kita sendiri. Mari kita bimbing dia dengan kasih sayang terlebih dahulu.")
            ],
            "trans": [
                ("ダヌさん", "昨日うちの息子が生徒間の乱闘騒ぎ（タウラン）に巻き込まれたと聞いて、本当に激怒した（naik darah）よ。"),
                ("ダヌ夫人", "落ち着いて、お父さん。あの子はまだ血気盛んな若者（darah muda）だし、感情も不安定で同級生の影響を受けやすいのよ。"),
                ("ダヌさん", "しかし他人の命を危険に晒す行為だぞ！警察に通報すべきだろうか？"),
                ("ダヌ夫人", "どんな過ちを犯したとしても、あの子は私たちの血を分けた我が子（darah daging）です。まずは親の深い愛情で導いてあげましょう。")
            ]
        },
        "grammar_points": [
            "**複合名詞 darah daging の情緒性**: `darah`（血）と `daging`（肉）が並置された `darah daging` は、日本語の「血肉」「骨肉」と全く同じ発想であり、法的な実子（anak kandung）という客観的事実を超えた深い情愛を想起させます。",
            "**接頭辞 ber- による berdarah**: `berdarah dingin`（冷酷な）、`berdarah biru`（貴族の血を引く）、`berdarah campuran`（混血の）のように、`berdarah` は血統や性質の修飾句を豊かに作ります。"
        ],
        "quizzes": [
            {
                "q": "親が「どんなに非行に走っても、この子は自分の血を分けた実の我が子だ」と愛情を込めて表現する成句はどれか。",
                "choices": ["darah daging", "darah dingin", "darah biru", "darah muda"],
                "ans": "darah daging",
                "expl": "血を分けた実の子、我が子は `darah daging` です。"
            },
            {
                "q": "「伝統的な王宮や貴族の家系に生まれた名門の血統・青い血」を表す言葉はどれか。",
                "choices": ["darah biru", "darah putih", "darah daging", "darah dingin"],
                "ans": "darah biru",
                "expl": "貴族・王族の血筋は `darah biru`（青い血）です。"
            },
            {
                "q": "一切の同情や罪悪感を持たずに「冷酷非情に悪事を働く冷血な人物」を表す連語はどれか。",
                "choices": ["berdarah dingin", "berdarah panas", "berdarah biru", "berdarah muda"],
                "ans": "berdarah dingin",
                "expl": "冷酷非情なは `berdarah dingin`（冷たい血を持つ）です。"
            }
        ],
        "culture_column": {
            "title": "ロマ・イラマと名曲『Darah Muda』の社会変革",
            "body": "インドネシア音楽のレジェンド、ダンドゥットの帝王ロマ・イラマ（Rhoma Irama）が1970年代に発表した代表曲『Darah Muda（若い血）』。「Darah muda darahnya para remaja, yang selalu merasa gagah...（若い血、それは常に勇ましく誇らしげな青年たちの血…）」と歌われるこの楽曲は、スハルト強権体制下でエネルギーを持て余していた何千万人もの青年の心を捉え、青春の熱気と倫理的自覚を呼び覚ます社会現象となりました。"
        }
    },
    {
        "filename": "docs/lexicon/26-business-collocations-contract.md",
        "title": "【共起連語】ビジネス契約の必須コロケーション辞典：menandatangani kontrak / membatalkan klausul / wanprestasi",
        "root": "kontrak",
        "meaning": "契約、協定、法的合意、約款",
        "core_concept": "法的な権利義務を規定する商取引の根幹「契約（Kontrak / Perjanjian）」において、契約締結、条項の変更・破棄、債務不履行、有効期間延長など、実務で1日たりとも欠かせない法務コロケーションを体系化します。",
        "table_rows": [
            ("menandatangani kontrak", "契約に署名する", "契約を締結する、調印する", "法務/公式", "Kedua direktur utama resmi menandatangani kontrak kerja sama senilai lima puluh miliar rupiah."),
            ("membatalkan klausul", "条項を取り消す", "契約条項を破棄・無効化する、特約を削除する", "法務/交渉", "Pihak pembeli meminta agar pasal mengenai denda sepihak tersebut dibatalkan."),
            ("wanprestasi", "債務不履行", "契約違反、債務不履行、約束不履行（オランダ語由来法学用語）", "民法/係争", "Penggugat menuduh pihak tergugat telah melakukan tindakan wanprestasi atas perjanjian pasokan."),
            ("memperpanjang masa berlaku", "効力期間を延ばす", "契約期間を延長する、更新する", "行政/実務", "Kedua belah pihak sepakat memperpanjang masa berlaku nota kesepahaman hingga tahun depan."),
            ("memutus kontrak sepihak", "一方的に契約を切る", "契約を一方的に破棄・解除する", "係争/労働", "Karyawan dapat mengajukan gugatan ke pengadilan jika perusahaan memutus kontrak secara sepihak."),
            ("klausul kerahasiaan", "秘密条項", "秘密保持条項（NDA条項）、機密保持約款", "コンプラ/法務", "Setiap karyawan baru diwajibkan mematuhi klausul kerahasiaan data internal perusahaan."),
            ("ganti rugi", "損害を替える", "損害賠償、賠償金（ganti rugi materiil）", "司法/補償", "Pelanggar hak paten diwajibkan membayar uang ganti rugi sebesar kerugian nyata yang diderita.")
        ],
        "details": [
            {
                "term": "menandatangani kontrak (teken kontrak / eksekusi perjanjian)",
                "trans": "契約を締結する、契約書に調印・署名する",
                "nuance": "長時間の商談やデューデリジェンスの集大成として、法的拘束力のある契約書面（kontrak payung / perjanjian kerja）に代表者が署名押印する公式行為です。",
                "ex_id": "Setelah melalui uji tuntas selama tiga bulan, konsorsium BUMN resmi menandatangani kontrak pembangunan pelabuhan baru.",
                "ex_kana": "ステラ ムラルイ ウジ トゥンタス スラマ ティガ ブラン、コンソルシウム ベウエムエン レスミ ムナンダタンガニ コントラッ プムバングナン プラブハン バル",
                "ex_ja": "3ヶ月間のデューデリジェンスを経て、国営企業コンソーシアムは新港湾建設の契約を正式に締結（menandatangani kontrak）しました。",
                "note": "口語では `teken kontrak`（オランダ語 teekenen 由来）とも言われます。"
            },
            {
                "term": "melakukan wanprestasi (cedera janji / ingkar janji hukum)",
                "trans": "債務不履行（契約違反）を犯す",
                "nuance": "オランダ法由来の民法典（KUHPerdata）第1243条に基づく厳格な法律用語で、期日遅延、不完全履行、履行不能などにより契約上の義務を果たさない不法行為を指します。",
                "ex_id": "Jika kontraktor terlambat menyelesaikan proyek lebih dari tiga puluh hari, mereka dianggap melakukan wanprestasi.",
                "ex_kana": "ジュカ コントラクトール トゥルランバット ムニェレサイカン プロイェッ レビ ダリ ティガプル ハリ、ムレカ ディアンガップ ムラクカン ワンプレスタシ",
                "ex_ja": "もし請負業者が30日以上プロジェクトの完了を遅延させた場合、債務不履行（wanprestasi）を犯したものとみなされます。",
                "note": "損害賠償請求訴訟の基礎となる重要語彙です。"
            },
            {
                "term": "memperpanjang masa berlaku kontrak",
                "trans": "契約の有効期間を延長・更新する",
                "nuance": "賃貸借契約、保守運用契約、業務委託契約の期限到来に際し、双方の合意に基づいて契約効力をさらに一定期間存続させる定型実務です。",
                "ex_id": "Manajemen memutuskan untuk memperpanjang masa berlaku kontrak kerja para tenaga ahli asing.",
                "ex_kana": "マナジェメン ムムトゥスカン ウントゥッ ムムプルパンジャン マサ ブルラク コントラッ クルジャ パラ トゥナガ アーリ アシン",
                "ex_ja": "経営陣は、外国人専門家たちの雇用契約の有効期間を延長（memperpanjang masa berlaku）することを決定しました。",
                "note": "自動更新条項は `perpanjangan otomatis` と呼ばれます。"
            },
            {
                "term": "memutus kontrak secara sepihak",
                "trans": "契約を一方的に解除・破棄する",
                "nuance": "相手方の同意や正当な契約解除事由（syarat batal）なしに、一方の当事者が一方的に契約関係を打ち切る重大な契約違反行為です。",
                "ex_id": "Tindakan pengembang yang memutus kontrak secara sepihak telah merugikan puluhan investor ruko.",
                "ex_kana": "ティンダカン プンゲムバン ヤン ムムトゥス コントラッ スチャラ スピハッ トゥラー メルギカン プルフアン インヴェストール ルコ",
                "ex_ja": "契約を一方的に解除（memutus kontrak sepihak）した開発業者の行為は、数十人ものショップハウス投資家に多大な損害を与えました。",
                "note": "労働契約破棄の場合は不当解雇（PHK sepihak）問題となります。"
            },
            {
                "term": "klausul kerahasiaan (Non-Disclosure Agreement / NDA)",
                "trans": "秘密保持条項、機密情報保持約款",
                "nuance": "提携交渉やM&A、雇用契約において、企業秘密、技術ノウハウ、顧客データが第三者に漏洩するのを防ぐ必須の法的防護壁です。",
                "ex_id": "Pelanggaran terhadap klausul kerahasiaan ini dapat dituntut secara pidana maupun perdata ganti rugi.",
                "ex_kana": "プランガラン トゥルハダップ クラウスル クラハシアアン イニ ダパット ディトゥントゥット スチャラ ピダナ マウプン プルダタ ガンティ ルギ",
                "ex_ja": "この秘密保持条項（klausul kerahasiaan）に対する違反は、刑事責任のみならず民事上の損害賠償を請求される可能性があります。",
                "note": "現代ビジネスの全契約に必須の標準条項です。"
            }
        ],
        "dialogue": {
            "title": "海外企業との独占販売契約の最終調整",
            "lines": [
                ("Legal", "Pak Daniel, draf akhir perjanjian distribusi eksklusif dengan mitra Jepang sudah siap."),
                ("Pak Daniel", "Bagus. Bagaimana dengan klausul kerahasiaan dan penyelesaian sengketa hukumnya?"),
                ("Legal", "Semua sudah disesuaikan. Ada klausul tegas bahwa jika ada pihak yang wanprestasi, perkara akan diselesaikan di BANI."),
                ("Pak Daniel", "Sempurna. Hubungi mereka agar kita bisa menjadwalkan acara penandatanganan kontrak minggu depan.")
            ],
            "trans": [
                ("法務担当", "ダニエル社長、日本側パートナーとの独占販売代理店契約の最終ドラフトが準備できました。"),
                ("ダニエル社長", "ご苦労さま。秘密保持条項（klausul kerahasiaan）と法的分争解決条項はどうなっているかね？"),
                ("法務担当", "すべて調整済みです。いずれかの当事者が債務不履行（wanprestasi）に陥った場合、BANI（インドネシア仲裁委員会）で解決する旨の厳格な条項を設けてあります。"),
                ("ダニエル社長", "完璧だ。来週正式に契約調印（penandatanganan kontrak）の日程を設定できるよう、先方に連絡してくれ。")
            ]
        },
        "grammar_points": [
            "**wanprestasi の法学的性格**: オランダ語の `wanprestatie`（不履行）に由来する借用語で、現代インドネシア法学において英語の `breach of contract` や `default` に相当する唯一の公的専門用語として不可侵の地位を確立しています。",
            "**両分接辞 menandatangani**: `tanda tangan`（署名）に動詞接頭辞 `meN-` と接尾辞 `-i` が付くと、分かち書きが解消されて `menandatangani`（署名する）という1語の他動詞になります（名詞形: `penandatanganan`＝調印）。"
        ],
        "quizzes": [
            {
                "q": "契約上の義務（支払や納品など）を果たさず、不履行・契約違反となる事態を指すオランダ法由来の正確な法律専門用語はどれか。",
                "choices": ["wanprestasi", "force majeure", "ganti rugi", "ad-hoc"],
                "ans": "wanprestasi",
                "expl": "債務不履行・契約違反を表す法学用語は `wanprestasi` です。"
            },
            {
                "q": "「双方の代表者が合意に達し、契約書に正式に署名・調印して契約を締結する」を表す動詞句はどれか。",
                "choices": ["menandatangani kontrak", "membatalkan klausul", "memutus kontrak sepihak", "melakukan wanprestasi"],
                "ans": "menandatangani kontrak",
                "expl": "契約を締結・調印することは `menandatangani kontrak` です。"
            },
            {
                "q": "企業機密や独自ノウハウの外部流出を厳格に禁じる「秘密保持条項」の正式名称はどれか。",
                "choices": ["klausul kerahasiaan", "klausul arbitrase", "klausul wanprestasi", "klausul ganti rugi"],
                "ans": "klausul kerahasiaan",
                "expl": "秘密保持条項（NDA条項）は `klausul kerahasiaan` です。"
            }
        ],
        "culture_column": {
            "title": "「Materai」とインドネシアの印紙文化",
            "body": "インドネシアで契約書面を作成する際、絶対に忘れてはならないのが公的印紙「マテライ（Materai）」の貼付です。現在は10,000ルピア印紙（Materai Sepuluh Ribu）または電子印紙（e-Meterai）が義務付けられており、これに署名（tanda tangan）がまたがるようにサインすることで初めて法廷での公的証拠能力が担保されます。デジタル化が進む現代でも、印紙の有無は契約実務の最重要チェック項目です。"
        }
    },
    {
        "filename": "docs/lexicon/27-business-collocations-negotiation.md",
        "title": "【共起連語】ビジネス商談の必須コロケーション辞典：mencapai kesepakatan / mengajukan penawaran / menekan biaya",
        "root": "negosiasi",
        "meaning": "交渉、商談、価格折衝、妥協の模索",
        "core_concept": "利益の最大化と強固なパートナーシップの構築を目指す「ビジネス商談（Negosiasi Bisnis）」において、見積提示、コスト圧縮、合意形成、競争力強化など、現場を動かす最重要のアクション連語を網羅します。",
        "table_rows": [
            ("mencapai kesepakatan", "合意に到達する", "合意に達する、妥結する、商談をまとめる", "ビジネス/公式", "Setelah perundingan yang alot, kedua pihak akhirnya mencapai kesepakatan harga."),
            ("mengajukan penawaran", "オファーを提出する", "見積書を提出する、提案を行う、買収提案を出す", "営業/商用", "Vendor teknologi mengajukan penawaran harga khusus untuk pengadaan skala besar."),
            ("menekan biaya", "費用を押し下げる", "コストを圧縮する、経費削減する、出費を抑える", "経営/財務", "Perusahaan berupaya keras menekan biaya operasional tanpa mengurangi kualitas layanan."),
            ("meningkatkan daya saing", "競争力を高める", "競争力を強化する、市場競争優位を築く", "戦略/政策", "Penerapan otomatisasi pabrik bertujuan meningkatkan daya saing produk lokal di kancah global."),
            ("memberikan konsesi", "譲歩を与える", "譲歩する、妥協に応じる、特権を付与する", "外交/通商", "Pemerintah bersedia memberikan konsesi tarif pajak kepada investor yang membangun smelter."),
            ("menjajaki peluang", "機会を踏査する", "可能性・協業の機会を探る、打診する", "事業開発", "Delegasi bisnis berkunjung ke Jakarta untuk menjajaki peluang investasi sektor energi hijau."),
            ("titik temu", "出会う点", "合意点、妥協の着地点、共通項", "調停/折衝", "Mediator berusaha keras mencari titik temu antara tuntutan serikat buruh dan kemampuan asosiasi.")
        ],
        "details": [
            {
                "term": "mencapai kesepakatan (deal / mencapai mufakat)",
                "trans": "合意に達する、商談を妥結させる、ディールをまとめる",
                "nuance": "双方が提示した条件の隔たりを粘り強い交渉で埋め、最終的に双方が納得する合意（kesepakatan）に漕ぎ着ける商談のクライマックスです。",
                "ex_id": "Kedua korporasi telekomunikasi berhasil mencapai kesepakatan merger setelah negosiasi intensif selama setahun.",
                "ex_kana": "クドゥア コルポラシ テレコムニカシ ブルハシル ムンチャパイ クセパカタン メルゲル ステラ ネゴシアシ インテンシフ スラマ サトゥ タフン",
                "ex_ja": "両通信大手企業は、1年間にわたる集中的な交渉を経て、合併の合意に達し（mencapai kesepakatan）ました。",
                "note": "`mufakat`（伝統的合意）にも通じる重要目標です。"
            },
            {
                "term": "mengajukan penawaran harga (memberikan quotation)",
                "trans": "見積書（オファー）を提出する、価格提案を行う",
                "nuance": "入札（tender）や相見積もり（bidding）において、自社の提案書（proposal）および価格見積書（quotation）を正式に提出する営業の初動アクションです。",
                "ex_id": "Kami telah mengajukan penawaran harga yang sangat kompetitif untuk proyek pengadaan armada logistik.",
                "ex_kana": "カミ トゥラー ムンガジュカン プナワラン ハルガ ヤン サンガット コンペティティフ ウントゥッ プロイェッ プンガダアン アルマダ ロギスティック",
                "ex_ja": "弊社は物流フリート調達プロジェクトに対し、極めて競争力の高い価格見積もりを提出（mengajukan penawaran）いたしました。",
                "note": "名詞 `surat penawaran`（見積提案書）と共起します。"
            },
            {
                "term": "menekan biaya operasional (efisiensi anggaran)",
                "trans": "運営コストを圧縮する、経費削減を図る",
                "nuance": "不況期や利益率改善のために、無駄なプロセスを省き、支出を限界まで抑え込む企業の経営努力を指します。",
                "ex_id": "Digitalisasi alur dokumen berhasil menekan biaya operasional kantor hingga tiga puluh persen.",
                "ex_kana": "ディジタリサシ アルル ドクメン ブルハシル ムヌカン ビアヤ オペラシオナル カントール ヒンガ ティガプル パーセン",
                "ex_ja": "文書ワークフローのデジタル化により、オフィスの運営コストを最大30％圧縮する（menekan biaya）ことに成功しました。",
                "note": "動詞 `menekan`（押す・圧縮する）が鍵となります。"
            },
            {
                "term": "mencari titik temu (menemukan kompromi)",
                "trans": "合意点（妥協点）を探る、着地点を見出す",
                "nuance": "価格や納期、責任範囲で双方が対立している際、双方が面目を保ちつつ実利を分け合える落としどころを模索する交渉技術です。",
                "ex_id": "Setelah perdebatan sengit mengenai royalti, para perunding akhirnya menemukan titik temu yang adil.",
                "ex_kana": "ステラ プルデバタン スンギット ムンゲナイ ロヤルティ、パラ プルンディン アヒルニャ ムヌムカン ティティッ トゥム ヤン アディル",
                "ex_ja": "ロイヤルティをめぐる激しい議論の末、交渉者たちはついに公正な合意の着地点（titik temu）を見出しました。",
                "note": "`titik temu`（接点・共通の着地点）は頻出名詞句です。"
            },
            {
                "term": "meningkatkan daya saing produk",
                "trans": "製品の市場競争力を高める",
                "nuance": "価格競争力、品質、ブランド認知度、アフターサービスを総合的に強化し、国内外のライバル企業に競り勝つ優位性を確立する戦略用語です。",
                "ex_id": "Investasi dalam riset dan pengembangan (R&D) adalah kunci utama untuk meningkatkan daya saing manufaktur.",
                "ex_kana": "インヴェスタシ ダラム リセット ダン プンゲムバンガン アダラー クンチ ウタマ ウントゥッ ムニンカットカン ダヤ サイン マヌファクトゥル",
                "ex_ja": "研究開発（R&D）への投資こそが、製造業の競争力を高める（meningkatkan daya saing）ための最大の鍵です。",
                "note": "経済白書や中期経営計画の必須スローガンです。"
            }
        ],
        "dialogue": {
            "title": "大口クライアントとの価格折衝と妥結",
            "lines": [
                ("Sales Lead", "Pak, klien meminta diskon 15 persen untuk pesanan 10.000 unit panel surya."),
                ("Direktur", "Diskon sebesar itu bisa memangkas margin kita terlalu dalam. Apakah kita bisa menekan biaya logistik?"),
                ("Sales Lead", "Bisa, Pak, jika mereka bersedia mengambil barang langsung dari pelabuhan utama."),
                ("Direktur", "Bagus. Ajukan penawaran baru itu sebagai titik temu agar kita segera mencapai kesepakatan akhir.")
            ],
            "trans": [
                ("営業主任", "社長、クライアントが太陽光パネル1万台の発注に対して15％の値引きを要求してきています。"),
                ("取締役", "それほどの値引きでは弊社のマージンが削られすぎる。物流コストを圧縮（menekan biaya）できないかね？"),
                ("営業主任", "可能です、社長。先方が主要港から直接引き取る条件を受け入れてくれれば。"),
                ("取締役", "よし。その新たな提案（ajukan penawaran）を着地点（titik temu）として提示し、速やかに最終合意に達する（mencapai kesepakatan）よう進めたまえ。")
            ]
        },
        "grammar_points": [
            "**動詞 tekan の使役・圧縮メタファー**: 語根 `tekan`（押す）に `meN-` が付いた `menekan` は、「物理的にボタンを押す」から「コストを圧縮する（menekan biaya）」「インフレを抑制する（menekan inflasi）」「相手に圧力をかける（menekan pihak lawan）」へと発展します。",
            "**名詞 daya saing の構造**: `daya`（力・エネルギー）＋ `saing`（競争する）＝「競争力」。`daya beli`（購買力）、`daya tahan`（耐久力）など、`daya` は能力・ポテンシャルを表す高度な複合名詞を量産します。"
        ],
        "quizzes": [
            {
                "q": "「双方の粘り強い交渉の結果、最終的な契約合意・妥結に達する」を表す最も自然なビジネス連語はどれか。",
                "choices": ["mencapai kesepakatan", "menemui jalan buntu", "mengambil alih kuasa", "membatalkan klausul"],
                "ans": "mencapai kesepakatan",
                "expl": "合意に達する、妥結するは `mencapai kesepakatan` です。"
            },
            {
                "q": "「自社の製品提案書や価格見積書を正式に顧客へ提出・提示する」を表す動詞句はどれか。",
                "choices": ["mengajukan penawaran", "menekan biaya", "menarik kesimpulan", "memutus kontrak"],
                "ans": "mengajukan penawaran",
                "expl": "見積書やオファーを提出するは `mengajukan penawaran` です。"
            },
            {
                "q": "対立する交渉双方が互いに妥協して見出す「合意の着地点・落としどころ」を意味する名詞句はどれか。",
                "choices": ["titik temu", "jalan buntu", "garis batas", "mata rantai"],
                "ans": "titik temu",
                "expl": "合意の着地点、落としどころは `titik temu` です。"
            }
        ],
        "culture_column": {
            "title": "「Musyawarah Mufakat」にみるインドネシア的交渉術",
            "body": "欧米的な「勝ち負け（Zero-sum game）」を競うディベート交渉と異なり、インドネシアの商談や協議では伝統的な「ムシャワラ・ムファカット（Musyawarah untuk Mufakat / 熟議による全会一致の合意形成）」が重視されます。相手を論破して窮地に追い込むのではなく、互いのメンツ（gengsi）を立てながら双方が笑顔で握手できる「Titik Temu（着地点）」をじっくりと時間をかけて探ることが、長期的な信頼（kepercayaan）を築く王道とされています。"
        }
    },
    {
        "filename": "docs/lexicon/28-business-collocations-finance.md",
        "title": "【共起連語】ビジネス財務の必須コロケーション辞典：laporan laba rugi / arus kas / suntikan modal / suku bunga",
        "root": "keuangan",
        "meaning": "財務、金融、資金繰り、会計、資本",
        "core_concept": "企業の生命線である「財務・ファイナンス（Keuangan）」において、損益計算書、キャッシュフロー管理、資本注入、政策金利変動、配当分配など、CFOや経理担当者・投資家が駆使する必須の財務コロケーションを体系化します。",
        "table_rows": [
            ("laporan laba rugi", "損益報告書", "損益計算書（P/L）、損益計算リポート", "財務/会計", "Laporan laba rugi kuartal ketiga menunjukkan pertumbuhan laba bersih sebesar dua digit."),
            ("arus kas (cash flow)", "現金の流れ", "キャッシュフロー、資金繰り、現金の出納状況", "経営/資金", "Perusahaan harus menjaga arus kas operasional tetap positif demi kelancaran produksi."),
            ("suntikan modal", "資本の注射", "増資、資本注入、追加出資（capital injection）", "投資/M&A", "Startup logistik tersebut berhasil mendapatkan suntikan modal ventura dari investor global."),
            ("suku bunga acuan", "基準の利子", "政策金利、基準金利（BI-Rate）", "中央銀行/マクロ", "Bank Indonesia memutuskan mempertahankan suku bunga acuan guna mengendalikan laju inflasi."),
            ("membagikan dividen", "配当を配る", "株主配当を支払う、配当金を分配する", "株式/IR", "Rapat Umum Pemegang Saham (RUPS) menyetujui pembagian dividen tunai tahun buku 2025."),
            ("neraca keuangan", "財務の天秤", "貸借対照表（バランスシート / B/S）", "会計/監査", "Auditor independen memeriksa neraca keuangan perusahaan untuk memastikan kepatuhan standar akuntansi."),
            ("likuiditas perbankan", "銀行の流動性", "銀行流動性、金融市場の資金余力", "金融/信用", "Bank sentral menjaga kecukupan likuiditas perbankan untuk mendukung penyaluran kredit usaha.")
        ],
        "details": [
            {
                "term": "laporan laba rugi (income statement / profit and loss)",
                "trans": "損益計算書（P/L）、収益費用報告書",
                "nuance": "一定期間（四半期や通期）における企業の売上高（pendapatan）、売上原価（HPP）、販管費、純利益（laba bersih）をまとめた財務諸表の最重要書類です。",
                "ex_id": "Berdasarkan laporan laba rugi konsolidasian, pendapatan perseroan naik berkat lonjakan penjualan ekspor.",
                "ex_kana": "ブルダサルカン ラポラン ラバ ルギ コンソリダシアン、プンダパタン プルセロアン ナイッ ブルカッ ロンジャカン プンジュアラン エクスポール",
                "ex_ja": "連結損益計算書（laporan laba rugi）に基づくと、同社の売上高は輸出販売の急増により増加しました。",
                "note": "会計実務の必須財務諸表です。"
            },
            {
                "term": "arus kas operasional (operating cash flow)",
                "trans": "営業キャッシュフロー、日々の資金繰り",
                "nuance": "帳簿上の黒字（laba akuntansi）であっても、実際に手元に入出金される現金の流れ（arus kas）が枯渇すれば黒字倒産（kebangkrutan）に至るため、経営者が最も神経を尖らせる指標です。",
                "ex_id": "Keterlambatan pembayaran dari distributor ritel mulai mengganggu kelancaran arus kas internal perusahaan.",
                "ex_kana": "クトゥルランバタン プンバヤラン ダリ ディストリブトール リテル ムライ ムンガング クランチャラン アルス カス インテルナル プルサハアン",
                "ex_ja": "小売ディストリビューターからの支払遅延が、社内のキャッシュフロー（arus kas）の円滑な循環を妨げ始めています。",
                "note": "`arus kas negatif`（キャッシュフロー赤字）は経営危機シグナルです。"
            },
            {
                "term": "suntikan modal (injeksi modal / penambahan ekuitas)",
                "trans": "資本注入、増資、ベンチャー出資",
                "nuance": "「資本の注射（suntikan）」という医療メタファーを用い、資金難に陥った企業を救済する公的資金注入や、急成長スタートアップへの巨額VC投資を描写します。",
                "ex_id": "Pemerintah menyetujui suntikan modal negara (PMN) kepada BUMN karya guna menyelesaikan jalan tol strategis.",
                "ex_kana": "プムリンター ムニュトゥジュイ スンティカン モダル ネガラ クパダ ベウエムエン カルヤ グナ ムニェレサイカン ジャラン トル ストラテギス",
                "ex_ja": "政府は戦略的高速道路を完成させるため、インフラ国営企業への国家資本注入（PMN / suntikan modal）を承認しました。",
                "note": "`Penyertaan Modal Negara (PMN)` は公的経済ニュースで頻出します。"
            },
            {
                "term": "suku bunga acuan Bank Indonesia (BI-Rate)",
                "trans": "インドネシア中央銀行の政策金利（基準金利）",
                "nuance": "インドネシア銀行（BI）が毎月の金融政策決定会合（RDG）で設定する、民間銀行の預金金利や住宅ローン金利の指標となる最高レベルのマクロ経済変数です。",
                "ex_id": "Kenaikan suku bunga acuan diperkirakan akan menaikkan beban bunga pinjaman kepemilikan rumah (KPR).",
                "ex_kana": "クナイカン スク ブンガ アチュアン ディプルキラカン アカン ムナイッカン ブバン ブンガ ピンジャマン クプミリカン ルマー",
                "ex_ja": "政策金利（suku bunga acuan）の引き上げは、住宅ローン（KPR）の金利負担を増加させると予想されています。",
                "note": "為替・住宅・株式市場に直結する指標です。"
            },
            {
                "term": "membagikan dividen (distribusi dividen pemegang saham)",
                "trans": "株主配当を支払う、配当金を分配する",
                "nuance": "上場企業（emiten）が年間事業活動で得た純利益の一部を、株主総会（RUPS）の決議を経て株主に還元する公式IRイベントです。",
                "ex_id": "Bank pelat merah tersebut mengumumkan rencana membagikan dividen jumbo dengan payout ratio mencapai delapan puluh persen.",
                "ex_kana": "バンク プラット メラー トゥルスブット ムンウムムカン レンチャナ ムムバギカン ディヴィデン ジュムボ ドゥンガン ペイアウト ラシオ ムンチャパイ ドゥラパンプル パーセン",
                "ex_ja": "その大手国営銀行は、配当性向80％に達する巨額の株主配当を支払う（membagikan dividen）計画を発表しました。",
                "note": "`dividen interim`（中間配当）、`dividen tunai`（現金配当）と共起します。"
            }
        ],
        "dialogue": {
            "title": "取締役会での四半期財務報告と増資計画",
            "lines": [
                ("CFO", "Bapak Direktur Utama, laporan laba rugi kuartal ini mencatatkan perbaikan margin operasional sebesar lima persen."),
                ("Dirut", "Bagus sekali. Namun bagaimana dengan arus kas kita setelah ekspansi pabrik baru di Jawa Tengah?"),
                ("CFO", "Arus kas sempat tertekan, namun kita sudah mendapatkan komitmen suntikan modal dari investor institusi."),
                ("Dirut", "Syukurlah. Dengan likuiditas yang terjaga, kita tetap bisa membagikan dividen stabil kepada para pemegang saham.")
            ],
            "trans": [
                ("CFO", "代表取締役社長、今四半期の損益計算書（laporan laba rugi）は営業利益率の5％改善を記録しました。"),
                ("社長", "大変結構だ。しかし中部ジャワの新工場拡張後の弊社のキャッシュフロー（arus kas）はどうなっているかね？"),
                ("CFO", "資金繰りは一時圧迫されましたが、機関投資家からの増資受入れ（suntikan modal）の確約を取り付けました。"),
                ("社長", "安心したよ。手元流動性が維持されれば、株主への安定した配当支払い（membagikan dividen）も継続できるね。")
            ]
        },
        "grammar_points": [
            "**suku bunga の多機能性**: `bunga` は「花」ですが、金融文脈では「利子・利息」を意味します。`suku bunga`（利率・金利）、`bunga pinjaman`（借入金利）、`beban bunga`（支払利息）など、借入・預金のあらゆる場面で共起します。",
            "**laba rugi の対比並置**: `laba`（利益）と `rugi`（損失）が並置された `laba rugi` は、損益計算書（Income Statement）の公的会計名称として定着しています。"
        ],
        "quizzes": [
            {
                "q": "企業の売上高、費用、純利益の推移を一覧表示する「損益計算書（P/L）」の正式なインドネシア語はどれか。",
                "choices": ["laporan laba rugi", "neraca keuangan", "laporan arus kas", "laporan ekuitas"],
                "ans": "laporan laba rugi",
                "expl": "損益計算書は `laporan laba rugi` です。`neraca keuangan` は貸借対照表です。"
            },
            {
                "q": "スタートアップの資金調達や赤字企業への「資本注入・増資（Capital injection）」を表す比喩的連語はどれか。",
                "choices": ["suntikan modal", "arus kas", "suku bunga", "uang muka"],
                "ans": "suntikan modal",
                "expl": "資本注入・増資は `suntikan modal`（資本の注射）と言います。"
            },
            {
                "q": "中央銀行が金融引き締めやインフレ抑制のために決定する「政策金利・基準金利」はどれか。",
                "choices": ["suku bunga acuan", "arus kas bebas", "dividen tunai", "nilai tukar riil"],
                "ans": "suku bunga acuan",
                "expl": "政策金利・基準金利は `suku bunga acuan` です。"
            }
        ],
        "culture_column": {
            "title": "「RUPS」とインドネシア企業の株主総会文化",
            "body": "インドネシアの上場企業において、年次株主総会「RUPS（Rapat Umum Pemegang Saham）」は一大イベントです。単なる業績報告にとどまらず、配当（dividen）の分配や役員人事、将来の投資計画が承認されます。特に配当性向（dividend payout ratio）が高く設定される傾向があるインドネシア株式市場（IDX）において、株主還元への期待は極めて高く、経営陣の手腕が最も厳格に問われる場となります。"
        }
    },
    {
        "filename": "docs/lexicon/29-business-collocations-hr.md",
        "title": "【共起連語】ビジネス人事の必須コロケーション辞典：perekrutan karyawan / PHK / evaluasi kinerja / jenjang karier",
        "root": "kepegawaian",
        "meaning": "人事、労務管理、雇用、キャリア、労使関係",
        "core_concept": "人材の獲得から育成・評価・退職に至る「人事労務管理（Manajemen SDM / HR）」において、採用募集、人員削減（PHK）、業績人事評価、キャリアパス形成、最低賃金など、組織を統治する必須のHRコロケーションを整理します。",
        "table_rows": [
            ("perekrutan karyawan", "従業員の採用", "社員採用、人材募集、リクルーティング", "人事/実務", "Proses perekrutan karyawan baru kini beralih sepenuhnya ke platform digital."),
            ("pemutusan hubungan kerja (PHK)", "労働関係の切断", "解雇、人員削減、リストラ、レイオフ", "労務/法律", "Gelombang pemutusan hubungan kerja di industri tekstil memicu kekhawatiran para buruh."),
            ("evaluasi kinerja", "業績の評価", "人事考課、パフォーマンス評価、業績査定", "組織/人事", "Setiap akhir tahun, perusahaan mengadakan evaluasi kinerja karyawan berbasis KPI."),
            ("jenjang karier", "キャリアの階段", "キャリアパス、昇進昇格の道筋、キャリア形成", "キャリア/育成", "Kandidat berbakat cenderung memilih perusahaan yang menawarkan jenjang karier jelas."),
            ("surat peringatan (SP)", "警告の手紙", "警告書、始末書勧告、懲戒通告書（SP 1, SP 2, SP 3）", "規律/法務", "Manajemen melayangkan surat peringatan pertama kepada staf yang sering mangkir kerja."),
            ("uang pesangon", "手切れのお金", "退職金、解雇手当、法定補償金", "労働法/金銭", "Perusahaan wajib membayarkan uang pesangon sesuai ketentuan Undang-Undang Cipta Kerja."),
            ("upah minimum regional (UMR / UMP)", "地域最低賃金", "地域別最低賃金（UMP: 州最低賃金、UMK: 市郡最低賃金）", "政策/労使", "Pemerintah provinsi resmi mengumumkan kenaikan upah minimum regional untuk tahun depan.")
        ],
        "details": [
            {
                "term": "pemutusan hubungan kerja / PHK (layoff / terminasi)",
                "trans": "解雇、人員削減、リストラ、雇用契約解除",
                "nuance": "雇用主と労働者の間の雇用契約を終了させる法的手続きであり、現代インドネシア社会で最も社会的関心が高くデリケートな人事・社会問題のキーワードです。",
                "ex_id": "Badai ekonomi global memaksa beberapa perusahaan rintisan melakukan efisiensi berupa PHK massal.",
                "ex_kana": "バダイ エコノミ グロバル ムマクサ ブルブラパ プルサハアン リンティサン ムラクカン エフィシエンシ ブルパ ペー・ハー・カー マッサル",
                "ex_ja": "世界的な経済の逆風は、複数のスタートアップ企業に集団解雇（PHK massal）という形での効率化を余儀なくさせました。",
                "note": "日常会話や報道では略称 `PHK`（ペー・ハー・カー）が完全に定着しています。"
            },
            {
                "term": "evaluasi kinerja tahunan (performance appraisal)",
                "trans": "人事評価、年間業績考課、パフォーマンス査定",
                "nuance": "KPI（Key Performance Indicator）やOKRに基づき、社員の年間目標達成度、リーダーシップ、行動特性を多角的に採点して昇給やボーナスに反映させる実務です。",
                "ex_id": "Hasil evaluasi kinerja ini akan menentukan kelayakan kenaikan gaji dan promosi jabatan setiap staf.",
                "ex_kana": "ハシル エヴァルアシ キネルジャ イニ アカン ムヌントゥカン クラヤカン クナイカン ガジ ダン プロモシ ジャバタン スティアップ スタフ",
                "ex_ja": "この人事評価（evaluasi kinerja）の結果が、各スタッフの昇給および役職昇進の適格性を決定します。",
                "note": "名詞 `kinerja`（パフォーマンス・業績）と共起します。"
            },
            {
                "term": "jenjang karier yang jelas (career progression)",
                "trans": "明確なキャリアパス、ステップアップの道筋",
                "nuance": "優秀な若手人材を採用・リテンション（定着）する上で、将来どのような役職や専門職へ成長・昇進できるかの透明な階梯を示します。",
                "ex_id": "Generasi milenial sangat memprioritaskan lingkungan kerja yang menyediakan jenjang karier yang transparan.",
                "ex_kana": "ゲネラシ ミレニアル サンガット ムムリオリティスカン リングクンガン クルジャ ヤン ムニェディアカン ジュンジャン カリエル ヤン トランスパラン",
                "ex_ja": "ミレニアル世代は、透明性の高いキャリアパス（jenjang karier）を提供する職場環境を強く優先視しています。",
                "note": "`jenjang` は「階段・階梯」を意味します。"
            },
            {
                "term": "surat peringatan / SP (warning letter)",
                "trans": "警告書、戒告処分（SP 1, SP 2, SP 3）",
                "nuance": "規律違反や業務怠慢を犯した社員に対し、会社が段階的に発行する公式懲戒文書です。法定制度に基づき、通常 SP3 で解雇（PHK）の要件が成立します。",
                "ex_id": "Karyawan yang melanggar kode etik perusahaan telah dijatuhi surat peringatan kedua secara tertulis.",
                "ex_kana": "カルヤワン ヤン ムランガル コデ エティッ プルサハアン トゥラー ディジャトゥヒ スラット プリンガタン クドゥア スチャラ トゥルトゥリス",
                "ex_ja": "会社の行動規範に違反した従業員に対し、書面による第2次警告書（surat peringatan kedua / SP 2）が言い渡されました。",
                "note": "労務管理の必須懲戒プロセスです。"
            },
            {
                "term": "uang pesangon (severance pay)",
                "trans": "退職手当、解雇補償金、法定退職金",
                "nuance": "定年退職や解雇時に、労働法規（UU Ketenagakerjaan / Cipta Kerja）の基準に従って勤続年数に応じて支払われる法定補償金です。",
                "ex_id": "Serikat pekerja menggelar demonstrasi menuntut pembayaran uang pesangon penuh bagi buruh yang terdampak relokasi pabrik.",
                "ex_kana": "スリカット プクルジャ ムンゲラール デモンストラシ ムヌントゥット プンバヤラン ウアン プサンゴン プヌー バギ ブルフ ヤン トゥルダンパック レロカシ パブリック",
                "ex_ja": "労働組合は、工場の移転の影響を受けた労働者に対し、満額の退職補償金（uang pesangon）を支払うよう求めてデモを実施しました。",
                "note": "労使紛争の最大の争点となる金銭項目です。"
            }
        ],
        "dialogue": {
            "title": "年度末の人事考課とキャリア面談",
            "lines": [
                ("HR Manager", "Budi, selamat! Berdasarkan hasil evaluasi kinerja tahun ini, skormu melampaui target KPI."),
                ("Budi", "Terima kasih, Bu. Saya sangat bersyukur atas dukungan tim dan bimbingan manajemen."),
                ("HR Manager", "Perusahaan ingin menawarkan promosi ke posisi manajerial sebagai bagian dari jenjang kariermu."),
                ("Budi", "Ini kehormatan besar, Bu. Saya siap mengemban tanggung jawab baru ini dengan sebaik-baiknya.")
            ],
            "trans": [
                ("人事マネージャー", "ブディさん、おめでとう！今年の人事評価（evaluasi kinerja）の結果に基づき、君のスコアはKPI目標を上回ったわ。"),
                ("ブディ", "ありがとうございます、マネージャー。チームの支えと経営陣のご指導に心から感謝いたします。"),
                ("人事マネージャー", "会社としては、君のキャリアパス（jenjang karier）の一環として管理職ポジションへの昇進を打診したいと考えているの。"),
                ("ブディ", "大変光栄です。この新たな責任を全力で果たせるよう全力を尽くします。")
            ]
        },
        "grammar_points": [
            "**略語 PHK の動詞化**: 名詞 `pemutusan hubungan kerja` は略称 `PHK` と呼ばれますが、日常会話やニュースでは受動態接頭辞 `di-` を付けて `di-PHK`（解雇される）、能動態 `mem-PHK`（解雇する）と動詞化して極めて頻繁に発話されます。",
            "**rekut から perekrutan への派生**: 外来語の語根 `rekut`（リクルート）に名詞化の周囲辞 `pe-...-an` が付加されて `perekrutan`（採用・登用プロセス）となります。"
        ],
        "quizzes": [
            {
                "q": "企業による従業員の解雇、リストラ、雇用契約解除を指すインドネシア語の正式名称および頻出略称はどれか。",
                "choices": ["pemutusan hubungan kerja (PHK)", "evaluasi kinerja (EK)", "jenjang karier (JK)", "surat peringatan (SP)"],
                "ans": "pemutusan hubungan kerja (PHK)",
                "expl": "解雇・人員削減は `pemutusan hubungan kerja`（略称 PHK）です。"
            },
            {
                "q": "社員の年間目標達成度や行動を客観的に査定する「人事考課・業績評価」を表す専門用語はどれか。",
                "choices": ["evaluasi kinerja", "uang pesangon", "perekrutan karyawan", "klausul kerahasiaan"],
                "ans": "evaluasi kinerja",
                "expl": "業績評価・人事考課は `evaluasi kinerja` です。"
            },
            {
                "q": "規律違反を犯した社員に対して会社から段階的に発行される「公式警告書」の略称はどれか。",
                "choices": ["SP (Surat Peringatan)", "DP (Down Payment)", "UMR (Upah Minimum Regional)", "PKL (Pedagang Kaki Lima)"],
                "ans": "SP (Surat Peringatan)",
                "expl": "警告書・始末書通告は `SP`（Surat Peringatan）です。"
            }
        ],
        "culture_column": {
            "title": "「Keluarga Besar」の企業理念と解雇（PHK）の重み",
            "body": "インドネシアの多くの企業において、会社組織は単なる契約関係を超えて「大家族（Keluarga Besar）」の温かい絆として捉えられます。そのため、リストラや解雇（PHK）は単なるコスト削減ではなく「家族の一員を切り捨てる悲劇」として受け止められ、経営者には手厚い退職金（uang pesangon）の支給や丁寧な説明対話が倫理的に強く求められます。この家族主義的な温もりこそが、インドネシアの労使関係の根底にある文化的特色です。"
        }
    },
    {
        "filename": "docs/lexicon/30-business-collocations-marketing.md",
        "title": "【共起連語】ビジネス販促・マーケティングの必須コロケーション辞典：pangsa pasar / target konsumen / kampanye promosi",
        "root": "pemasaran",
        "meaning": "マーケティング、販促、市場占有、ブランド、顧客維持",
        "core_concept": "顧客の心を掴み売上を飛躍させる「マーケティング＆プロモーション（Pemasaran & Promosi）」において、市場シェア拡大、ターゲット顧客層の特定、販促キャンペーン、ブランドイメージ構築、顧客維持率など、マーケター必携の共起表現を網羅します。",
        "table_rows": [
            ("pangsa pasar (market share)", "市場の分け前", "市場シェア、マーケットシェア、市場占有率", "戦略/市場", "Platform e-commerce lokal berhasil menguasai lima puluh persen pangsa pasar nasional."),
            ("target konsumen", "消費者の標的", "ターゲット顧客層、対象顧客、ターゲット層", "企画/顧客", "Produk kosmetik alami ini dirancang khusus untuk target konsumen wanita urban usia muda."),
            ("kampanye promosi", "販促の軍事行動", "プロモーションキャンペーン、販促キャンペーン", "広告/宣伝", "Perusahaan meluncurkan kampanye promosi besar-besaran menjelang pesta belanja tanggal kembar."),
            ("citra merek (brand image)", "ブランドのイメージ", "ブランドイメージ、ブランドの好感度・企業像", "ブランディング", "Kolaborasi dengan atlet berprestasi sukses mendongkrak citra merek produk minuman berenergi."),
            ("retensi pelanggan", "顧客の保持", "顧客維持、リピート率向上、既存顧客の定着", "CRM/顧客", "Program loyalitas poin reward terbukti efektif meningkatkan angka retensi pelanggan."),
            ("menembus pasar global", "世界市場を貫く", "グローバル市場に進出する、海外市場を開拓する", "貿易/成長", "Kopi arabika asal Gayo berhasil menembus pasar global hingga ke Amerika dan Eropa."),
            ("pemasaran digital (digital marketing)", "デジタルのマーケティング", "デジタルマーケティング、ネット集客、Webマーケ", "IT/マーケ", "Biaya pemasaran digital dinilai jauh lebih efisien dan terukur dibanding iklan televisi konvensional.")
        ],
        "details": [
            {
                "term": "pangsa pasar (market share)",
                "trans": "市場シェア、マーケットシェア、市場占有率",
                "nuance": "特定産業やカテゴリーにおいて、自社製品やサービスが占める売上や販売数量のパーセンテージを表す事業戦略の基本指標です。",
                "ex_id": "Melalui strategi diferensiasi harga, merek ponsel pintar baru itu mampu merebut pangsa pasar dari pesaing lama.",
                "ex_kana": "ムラルイ ストラテギ ディフェレンシアシ ハルガ、メレック ポンセル ピンタル バル イトゥ マムプ ムルブット パンサ パサール ダリ プサイン ラマ",
                "ex_ja": "価格差別化戦略を通じて、その新しいスマートフォンブランドは旧来の競合他社から市場シェア（pangsa pasar）を奪取することに成功しました。",
                "note": "`menguasai pangsa pasar`（市場シェアを制覇する）と共起します。"
            },
            {
                "term": "target konsumen (target audiens / pasar sasaran)",
                "trans": "ターゲット顧客層、対象消費者、ターゲット層",
                "nuance": "年齢、性別、収入、居住地域、ライフスタイル（demografi & psikografi）に基づいて精密に定義された、商品やサービスの想定購入者群です。",
                "ex_id": "Identifikasi target konsumen yang tepat adalah langkah krusial sebelum merumuskan strategi konten di media sosial.",
                "ex_kana": "イデンティフィカシ ターゲット コンスメン ヤン トゥパット アダラー ランカ クルシアル スブルム ムルムスカン ストラテギ コンテン ディ メディア ソシアル",
                "ex_ja": "適切なターゲット顧客層（target konsumen）の特定は、SNSでのコンテンツ戦略を策定する前の極めて重要なステップです。",
                "note": "`menjangkau target konsumen`（ターゲット層にリーチする）と頻出します。"
            },
            {
                "term": "kampanye promosi besar-besaran (mega campaign)",
                "trans": "大々的な販促プロモーションキャンペーン",
                "nuance": "新製品発売時やダブルデー商戦（Hari Belanja Online Nasional / Harbolnas）に、広告宣伝、インフルエンサー起用、割引クーポンを総動員して展開する集中マーケティングです。",
                "ex_id": "Aplikasi pesan-antar makanan menggelar kampanye promosi besar-besaran dengan diskon ongkos kirim cuma-cuma.",
                "ex_kana": "アプリカシ プサンアンタル マカナン ムンゲラール カンパニェ プロモシ ブサールブサーラン ドゥンガン ディスコン オンコス キリム チュマチュマ",
                "ex_ja": "フードデリバリーアプリは、送料無料割引を掲げた大々的なプロモーションキャンペーン（kampanye promosi）を展開しました。",
                "note": "消費を刺激するイベントの定型表現です。"
            },
            {
                "term": "citra merek (brand image & perception)",
                "trans": "ブランドイメージ、企業・ブランドの評判",
                "nuance": "消費者がそのブランド名を聞いた時に心に抱く品質、信頼性、格調、親しみやすさなどの心理的印象を指します。",
                "ex_id": "Isu pencemaran lingkungan yang viral di media sosial dapat merusak citra merek yang dibangun puluhan tahun.",
                "ex_kana": "イス プンチェマラン リングクンガン ヤン ヴィラル ディ メディア ソシアル ダパット メルサッ チトラ メレック ヤン ディバングン プルフアン タフン",
                "ex_ja": "SNSで拡散した環境汚染問題は、何十年もかけて構築されたブランドイメージ（citra merek）を一瞬で傷つけかねません。",
                "note": "`membangun citra merek`（ブランドイメージを構築する）と共起します。"
            },
            {
                "term": "retensi pelanggan (customer retention)",
                "trans": "顧客維持率、既存顧客の定着化、リピート購入",
                "nuance": "新規顧客の獲得（akuisisi pelanggan）だけでなく、既存の顧客が継続して利用し続けてくれる関係性を維持するCRMの重要指標です。",
                "ex_id": "Biaya untuk menjaga retensi pelanggan terbukti jauh lebih murah daripada mencari pelanggan baru.",
                "ex_kana": "ビアヤ ウントゥッ ムンジャガ レテンシ プランガン トゥルブクティ ジャウ レビ ムラー ダリパダ ムンチャリ プランガン バル",
                "ex_ja": "既存顧客を維持する（retensi pelanggan）ためのコストは、新規顧客を開拓するよりも遥かに安上がりであることが証明されています。",
                "note": "サブスクリプションやECビジネスの必須指標です。"
            }
        ],
        "dialogue": {
            "title": "新製品の発売戦略と市場シェア拡大",
            "lines": [
                ("Marketing Lead", "Pak, prototipe minuman teh hijau organik kita siap diluncurkan ke pasar bulan depan."),
                ("CMO", "Bagus. Bagaimana dengan target konsumen dan saluran promosinya?"),
                ("Marketing Lead", "Target konsumen kita adalah kalangan pekerja muda yang peduli kesehatan, dipromosikan lewat pemasaran digital."),
                ("CMO", "Rancang kampanye promosi yang kreatif untuk membangun citra merek premium agar kita lekas merebut pangsa pasar.")
            ],
            "trans": [
                ("マーケティング主任", "部長、弊社のオーガニック緑茶飲料の試作品、来月市場に投入する準備が整いました。"),
                ("CMO（最高マーケティング責任者）", "素晴らしい。ターゲット顧客層（target konsumen）と販促チャネルはどうなっているかね？"),
                ("マーケティング主任", "想定ターゲットは健康志向の若いビジネスパーソン層で、デジタルマーケティングを通じてプロモーションを展開します。"),
                ("CMO", "一気に市場シェア（pangsa pasar）を奪取できるよう、プレミアムなブランドイメージ（citra merek）を築く創造的な販促キャンペーン（kampanye promosi）を設計してくれ。")
            ]
        },
        "grammar_points": [
            "**pangsa の語源と展開**: `pangsa` は本来ドリアンなどの果実の「房（ふさ）・区分け」を意味します。そこから市場の全体パイを切り分けた「分け前・シェア（pangsa pasar）」という見事な経済メタファーへと発展しました。",
            "**citra の多角的用法**: サンスクリット語由来の `citra`（像・イメージ）は、`citra merek`（ブランドイメージ）、`citra satelit`（衛星写真画像）、`pencitraan`（政治家のイメージ作り）など、視覚的・心理的イメージの表現として幅広く定着しています。"
        ],
        "quizzes": [
            {
                "q": "企業や製品が市場全体の中で占める「市場占有率・マーケットシェア」を表す正確な専門語はどれか。",
                "choices": ["pangsa pasar", "target konsumen", "citra merek", "arus kas"],
                "ans": "pangsa pasar",
                "expl": "市場シェア・市場占有率は `pangsa pasar` です。"
            },
            {
                "q": "製品開発や広告戦略において「自社商品を購入してくれる想定購入者・対象顧客層」を意味する用語はどれか。",
                "choices": ["target konsumen", "kaki tangan", "uang pesangon", "badan hukum"],
                "ans": "target konsumen",
                "expl": "ターゲット顧客層は `target konsumen`（または `target audiens`）です。"
            },
            {
                "q": "消費者が企業や商品に対して抱く心理的印象や好感度を表す「ブランドイメージ」のインドネシア語はどれか。",
                "choices": ["citra merek", "mata rantai", "banyak mulut", "tebal muka"],
                "ans": "citra merek",
                "expl": "ブランドイメージは `citra merek` です。"
            }
        ],
        "culture_column": {
            "title": "「Harbolnas」とダブルデーメガセール熱狂社会",
            "body": "インドネシアのEコマース市場において、毎月のゾロ目の日（9.9、10.10、11.11）や12月12日の「全国オンラインショッピングの日（Harbolnas: Hari Belanja Online Nasional）」は、国中が熱狂する最大の消費フェスティバルです。大手プラットフォームが何十億ルピアもの巨額予算を投じて展開する `kampanye promosi besar-besaran`（大々的販促キャンペーン）は、単なる安売りを超え、真夜中のカウントダウンライブ配信やゲーム機能を取り入れた東南アジア特有の「ショッパーテインメント（Shoppertainment）」文化を創出しています。"
        }
    }
]

def generate_markdown(art):
    table_lines = [
        "| コロケーション（連語） | 直訳 | 実際の意味・用例 | 文脈・レジスター | 典型例文 |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for row in art["table_rows"]:
        table_lines.append(f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} | *{row[4]}* |")
    table_md = "\n".join(table_lines)

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

    gp_md = "\n".join([f"- {p}" for p in art["grammar_points"]])

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

    col = art["culture_column"]
    culture_md = f"""> [!TIP]
> **文化・ビジネスコラム：{col["title"]}**
> 
> {col["body"]}
"""

    full_text = f"""# {art["title"]}

インドネシア語における **`{art["root"]}`** は、原義として「**{art["meaning"]}**」を表します。{art["core_concept"]}

本稿では、日常会話から実務ビジネス、法務・経営戦略に至るまでネイティブスピーカーが自然に使いこなす必須の共起表現（コロケーション）を体系的に解説します。

---

## 1. `{art["root"]}` の最頻出コロケーション総覧

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

## 6. コア概念の文化的・ビジネス的背景

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
