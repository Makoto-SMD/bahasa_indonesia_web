# -*- coding: utf-8 -*-
import os
import re

articles = [
    {
        "id": "1191",
        "slug": "11-vowel-reduction-elision",
        "title": "【弱音化と音韻脱落】早口の日常会話で消える母音・子音の法則",
        "desc": "ネイティブが早口で話す際に生じる音韻脱落（Elision）と弱音化（Reduction）。教科書通りの音を探しても聞き取れない現象の完全解剖。",
        "theory": """### 1. 「音韻脱落（Elision）」と「弱音化（Reduction）」とは？
初心者がネイティブの日常会話を聞いて「知っている単語のはずなのに全く聞き取れない」と感じる最大の原因は、**早口の会話で特定の音節や子音・母音源が物理的に脱落（Elision）したり、弱く曖昧な音へ縮約（Reduction）される現象**にあります。

これは「だらしのない崩れた発音」ではなく、人間が最小の筋肉エネルギーで最大の情報を伝達しようとする音声学的な自然法則（調音の経済性）です。

### 2. インドネシア語の代表的な音韻脱落パターン
1. **語頭音節・母音の脱落（Aphaeresis）**:
   - *sudah* [su-dah] → **'dah** [dah]（スダ → ダー）
   - *belum* [bə-lum] → **'lom** [lom] または **'lum**
   - *tidak* [ti-daʔ] → **'gak** [gaʔ]
   - *saja* [sa-dʒa] → **'ja** [dʒa]
   - *seperti* [sə-pər-ti] → **'kayak** [ka-yaʔ]（語彙置換を伴う）
2. **語中母音・子音の脱落（Syncope）**:
   - *tetapi* [tə-ta-pi] → **tapi** [ta-pi]（語頭の te- が完全に消滅）
   - *bagaimana* [ba-gai-ma-na] → **gimana** [gi-ma-na]（ba- が消え、gai が gi へ縮約）
   - *kalau* [ka-lau̯] → **kalo** [ka-lo]（二重母音 au が単母音 o へ融合）
3. **h 音の脱落（語頭・語中・語末）**:
   - *lihat* [li-hat] → **liat** [li-yat]
   - *tahu* [ta-hu] → **tau** [ta-wu]
   - *bohong* [bo-hoŋ] → **boong** [bo-woŋ]""",
        "drills": [
            ("【sudah の脱落】「もうご飯食べたよ、お腹いっぱい（'dah makan）」",
             "'Dah makan tadi, sekarang udah kenyang banget.",
             "ダー マカン タディ、スカラン ウダ クニャン バンゲッ。",
             "sudah の su- が消え、'dah [dah] と単音節でリズミカルに発音される。"),
            ("【belum の弱音化】「まだだよ、まだ連絡が来ていない（'lom ada kabar）」",
             "'Lom, belom ada kabar sama sekali dari mereka.",
             "ロム、ブロン アダ カバル サマ スカリ ダリ ムレカ。",
             "belum の e が曖昧母音のまま縮まり、語末が 'lom と丸め込まれる。"),
            ("【tidak の脱落】「いや、全然平気だよ（'gak apa-apa）」",
             "'Gak apa-apa kok, santai aja ya.",
             "ガッ アパパ コッ、サンタイ アジャ ヤ。",
             "tidak が nggak になり、さらに頭が落ちて 'gak [gaʔ] と声門閉鎖音で一瞬で終わる。"),
            ("【saja の脱落】「これだけでいいよ、他にはいらない（ini 'ja）」",
             "Pilih yang ini 'ja, gak usah yang aneh-aneh.",
             "ピリ ヤン イニジャ、ガッ ウサ ヤン アネアネ。",
             "saja の sa- が落ちて前の単語とくっつき、ini 'ja [i-ni-dʒa] とリンキング。"),
            ("【tetapi → tapi】「行きたいんだけど、お金がないんだ（tapi gak ada uang）」",
             "Pengen ikut jalan-jalan, tapi lagi gak megang duit.",
             "ペンゲン イクッ ジャランジャラン、タピ ラギ ガッ ムガン ドゥイッ。",
             "tetapi の te- が完全に脱落した tapi は、口語の標準形となっている。"),
            ("【bagaimana → gimana】「昨日の試験、どうだった？（gimana kemarin?）」",
             "Gimana ujiannya kemarin? Lancar kan?",
             "ギマナ ウジアンニャ クマリン？ ランチャル カン？",
             "bagaimana の ba- が消え、二重母音 gai が gi に縮約されて gimana [gi-ma-na]。"),
            ("【kalau → kalo】「もし雨が降ったら、家にいよう（kalo ujan）」",
             "Kalo ujan deres, mendingan kita di rumah aja.",
             "カロ ウジャン ドゥレス、メンディンガン キタ ディ ルマ アジャ。",
             "kalau の au が o に融合して kalo。hujan の h も脱落して ujan。"),
            ("【h 音の脱落: lihat】「ちょっとあれ見てごらんよ！（coba liat deh）」",
             "Coba liat deh ke sana, ada pemandangan bagus banget.",
             "チョバ リヤッ デッ ク サナ、アダ プマンダンガン バグス バンゲッ。",
             "lihat の h が落ちて liat [li-yat]。y の渡り音が自然に滑り込む。"),
            ("【h 音の脱落: tahu】「知ってるよ、彼が来ないこと（gue udah tau）」",
             "Gue udah tau kok dari kemarin soal masalah itu.",
             "グエ ウダ タウ コッ ダリ クマリン ソアル マサラ イトゥ。",
             "tahu の h が落ちて tau [ta-wu]。豆腐の tahu と区別して発音。"),
            ("【h 音の脱落: bohong】「嘘つくなよ、本当のことを言って（jangan boong）」",
             "Jangan boong dong, jujur aja sama kita.",
             "ジャンガン ボオン ドン、ジュジュル アジャ サマ キタ。",
             "bohong の h が落ちて boong [bo-oŋ]。母音が連続して滑らかに流れる。"),
            ("【h 音の脱落: habis】「お金がもうなくなっちゃった（duwit abis）」",
             "Duit bulanan gue udah abis buat bayar kosan.",
             "ドゥイッ ブラナン グエ ウダ アビス ブアッ バヤル コサン。",
             "habis の語頭 h が脱落して abis。uang も duit へ口語置換。"),
            ("【h 音の脱落: hujan】「外は土砂降りの雨だよ（ujan gede）」",
             "Di luar lagi ujan gede, neduh dulu yuk.",
             "ディ ルアル ラギ ウジャン グデ、ヌドゥ ドゥル ユッ。",
             "hujan の h が落ちて ujan。besar もジャワ語由来の gede に短縮。"),
            ("【複合脱落】「どうして知ってるの？（kok bisa tau?）」",
             "Lho, kok kamu bisa tau sih? Padahal gak ada yang ngasih tau.",
             "ロ、コッ カム ビサ タウ シ？ パダハル ガカダ ヤン ンガシ タウ。",
             "tahu → tau, tidak ada → gak ada, memberi tahu → ngasih tau と脱落が連鎖する。"),
            ("【複合脱落】「もういいよ、気にしないで（'dah gak usah dipikirin）」",
             "'Dah, gak usah terlalu dipikirin, bawa santai aja.",
             "ダー、ガッ ウサ トゥルラル ディピキリン、バワ サンタイ アジャ。",
             "sudah → 'dah, tidak usah → gak usah, saja → aja と極限まで短縮。"),
            ("【総仕上げ】「もう知ってるよ（'dah tau）、どうして彼が来ないのか（gimana dia gak dateng）」",
             "Gue 'dah tau gimana ceritanya kenapa dia gak bisa dateng hari ini.",
             "グエ ダー タウ ギマナ チェリタニャ クナパ ディア ガッ ビサ ダテン ハリ イニ。",
             "sudah('dah), tahu(tau), bagaimana(gimana), datang(dateng) の全脱落形を流暢に操る。")
        ],
        "quizzes": [
            ("日常の早口会話で「sudah」が「'dah」に短縮される現象を音声学で何と呼ぶか？",
             ["語頭音脱落（Aphaeresis / Elision）", "強勢移動（Stress Shift）", "二重母音化（Diphthongization）"],
             "語頭音脱落（Aphaeresis / Elision）",
             "語頭の音節や母音が高速発話の中で省略される現象を語頭音脱落（Elision/Aphaeresis）と呼びます。"),
            ("単語「lihat」や「tahu」が口語で「liat」「tau」と発音される主な要因は？",
             ["語中の無声声門摩擦音 [h] が脱落し、母音間に渡り音が生じるため", "インドネシア語の正書法が改定されたため", "地方方言の文法規則による強制"],
             "語中の無声声門摩擦音 [h] が脱落し、母音間に渡り音が生じるため",
             "母音に挟まれた h は摩擦が弱まりやすく、日常会話では極めて高頻度で脱落します。"),
            ("「bagaimana」が「gimana」になる変化に含まれる2つの音韻プロセスは？",
             ["語頭音節 ba- の脱落と、二重母音 -ai- の単母音 -i- への短縮", "鼻音化と巻き舌化", "語末子音の無声化と長音化"],
             "語頭音節 ba- の脱落と、二重母音 -ai- の単母音 -i- への短縮",
             "ba- が脱落し、さらに gai が gi へと母音融合・短縮を起こして gimana となっています。")
        ]
    },
    {
        "id": "1192",
        "slug": "12-loanword-phonology",
        "title": "【外来語の借用音韻】オランダ語・アラビア語・英語由来単語の発音ルール",
        "desc": "数百年に及ぶ歴史の中でオランダ語・アラビア語・英語から流入した外来語の調音体系。標準正音（EYD）と口語借用音のリアルな響き。",
        "theory": """### 1. インドネシア語の多層的な外来語（Kata Serapan）
インドネシア語の語彙の約30〜40%は外来語です。歴史的な接触により、言語ごとに特徴的な音韻体系を持ち込みました。
1. **オランダ語由来（350年の植民地時代）**:
   - 日常生活・機械・医療・法制度の基本語彙に深く浸透。
   - 例: *knalpot*（マフラー [knal-pɔt]）, *handuk*（タオル [han-dʊk]）, *kamar*（部屋 [ka-mar]）, *kantor*（事務所 [kan-tɔr]）, *bengkel*（修理工場 [bɛŋ-kəl]）。
2. **アラビア語由来（イスラム伝来と宗教・倫理・思考）**:
   - 特有の喉音（咽頭音・喉頭音）がインドネシア語化。
   - *kh* [x/h]: *khabar* → *kabar*, *khusus* [xu-sus/hu-sus]（特殊）
   - *sy* [ʃ]: *syarat* [ʃa-rat]（条件）, *syukur* [ʃu-kur]（感謝）
   - *z* [z]: *zaman* [za-man]（時代）, *izin* [i-zin]（許可）
3. **英語由来（近現代の科学技術・ビジネス・国際用語）**:
   - スペルと発音の規則的な適応ルール（EYD）。
   - -tion → **-si**: *activity* → *aktivitas*, *condition* → *kondisi*
   - -ty → **-tas**: *quality* → *kualitas*, *facility* → *fasilitas*
   - -c- → **-k-**: *factor* → *faktor*, *practical* → *praktis*

### 2. 「f / v」が「p」になる現地調音のメカニズム
インドネシア語の土着言語（特にジャワ語やスンダ語）には元来「f」や「v」の音素（唇歯摩擦音）が存在しませんでした。
そのため、高齢者や大衆会話では外来語の f/v が無声両唇破裂音 [p] に置換される現象が頻繁に見られます。
- *foto* → **poto**
- *aktif* → **aktip**
- *telepon* → **telpon**
現代の教育を受けた層や標準語（Baku）ではクリアに [f] を発音しますが、この二重性を知ることで聞き取り能力が飛躍します。""",
        "drills": [
            ("【オランダ語借用】「車のマフラー（knalpot）を修理工場（bengkel）で直す」",
             "Knalpot mobil saya bocor dan harus diperbaiki di bengkel resmi.",
             "クナルポッ モビル サヤ ボチョル ダン ハルス ディプルバイキ ディ ベンケル レスミ。",
             "knalpot, bengkel はオランダ語由来。k-n の結合を母音なしで調音する。"),
            ("【オランダ語借用】「シャワーを浴びてからタオル（handuk）で体を拭く」",
             "Setelah mandi, jangan lupa memakai handuk yang bersih.",
             "ス トゥラ マンディ、ジャンガン ルパ ムマカイ ハンドゥッ ヤン ブルシ。",
             "handuk（オランダ語 handdoek）の語末 k は声門閉鎖で止める。"),
            ("【オランダ語借用】「オフィスの部屋（kamar di kantor）を清掃する」",
             "Petugas sedang membersihkan kamar kerja di kantor pusat.",
             "プトゥガス スダン ムンブルシカン カマル クルジャ ディ カントル プサッ。",
             "kamar（kamer）、kantor（kantoor）の語末 r をしっかり響かせる。"),
            ("【アラビア語借用: kh】「この部屋は特別（khusus）なお客様専用です」",
             "Ruangan ini dirancang khusus untuk menyambut tamu kehormatan.",
             "ルアンガン イニ ディランチャン クスス（フスス） ウントゥッ ムニャンブッ タム クホルマタン。",
             "khusus の kh は喉の奥を摩擦させる無声軟口蓋摩擦音 [x] または [h]。"),
            ("【アラビア語借用: sy】「どんな状況でも感謝（bersyukur）の心を忘れない」",
             "Kita harus selalu bersyukur atas nikmat kesehatan yang diberikan.",
             "キタ ハルス スラル ブルシュクル アタス ニッマッ クセハタン ヤン ディブルィカン。",
             "bersyukur, nikmat の sy は日本語の「シュ」に近い無声後部歯茎摩擦音 [ʃ]。"),
            ("【アラビア語借用: z】「時代の変化（perubahan zaman）に適応する」",
             "Perusahaan harus mampu beradaptasi dengan perkembangan zaman.",
             "プルサハアン ハルス マンプ ブルアダプタシ ドゥンガン プルクンバンガン ザマン。",
             "zaman を「ジャマン」と破裂させず、濁った摩擦音 [z] で上品に調音する。"),
            ("【アラビア語借用: izin】「上司に休暇の許可（izin cuti）を申請する」",
             "Saya sudah mengajukan surat izin cuti kepada atasan.",
             "サヤ スダ ムンガジュカン スラッ イジン（イジン/イズィン） チュティ クパダ アタサン。",
             "izin は口語では ijin と発音されがちだが、標準音は [i-zin]。"),
            ("【英語借用: -si】「最新の状況（kondisi terbaru）を確認する」",
             "Mari kita pantau kondisi pasar secara berkala.",
             "マリ キタ パンタウ コンディシ パサル スチャラ ブルカラ。",
             "kondisi（condition）の -si は明瞭な [si]。口を横に引く。"),
            ("【英語借用: -tas】「製品の品質（kualitas produk）を最優先にする」",
             "Kualitas adalah faktor terpenting dalam menjaga kepercayaan pelanggan.",
             "クアリタス アダラ ファクトル トゥルペンティン ダラム メンジャガ クプルチャヤアン プランガン。",
             "kualitas（quality）, faktor（factor）の語末子音 s, r を正確に止める。"),
            ("【英語借用: -tif】「効率的（efektif）かつ生産的（produktif）な働き方」",
             "Kita harus bekerja secara efektif dan produktif.",
             "キタ ハルス ブルクルジャ スチャラ エフェクティフ ダン プロドゥクティフ。",
             "efektif, produktif の語末 f は上歯で下唇を軽く噛んで息を抜く。"),
            ("【f vs p の対比】「写真を撮る（foto vs poto）」",
             "Silakan ambil foto pemandangan ini dengan kamera ponsel Anda.",
             "シラカン アンビル フォト（ポト） プマンダンガン イニ ドゥンガン カメラ ポンセル アンダ。",
             "標準音 foto [fo-to] と大衆音 poto [po-to] の違いを意識して発声。"),
            ("【英語借用: risiko】「高いリスク（risiko tinggi）を慎重に回避する」",
             "Investasi saham memiliki risiko kerugian yang cukup tinggi.",
             "インヴェスタシ サハム ムミリキ リシコ（レスィコ） クルギアン ヤン チュクッ ティンギ。",
             "risk はインドネシア語正書法で risiko（公式）または resiko（口語）。"),
            ("【英語借用: teknologi】「最先端のデジタル技術（teknologi digital）」",
             "Perkembangan teknologi digital membawa perubahan besar bagi masyarakat.",
             "プルクンバンガン テクノロジ ディジタール ムンバワ プルバハン ブサール バギ マシャラカッ。",
             "teknologi の k-n は母音を挟まず [tɛk-no-lo-gi]。"),
            ("【オランダ語借用: gratis】「このサービスは完全に無料（gratis）です」",
             "Pemerintah menyediakan layanan konsultasi kesehatan secara gratis.",
             "プムリンタ ムニュディアカン ラヤナン コンスルタシ クセハタン スチャラ グラティス。",
             "gratis の gr- は巻き舌で一気に弾き、語末 s を息で締める。"),
            ("【総仕上げ】「オフィス（kantor）で特別（khusus）なプロジェクトの品質（kualitas）とリスク（risiko）を分析する」",
             "Di kantor, kami menganalisis kualitas dan risiko proyek khusus ini.",
             "ディ カントル、カミ ムンアナリシス クアリタス ダン リシコ プロイェッ クスス イニ。",
             "オランダ語（kantor）、英語（kualitas, risiko）、アラビア語（khusus）の重層的外来語を完璧に吹き分ける。")
        ],
        "quizzes": [
            ("オランダ語由来の単語「knalpot（マフラー）」を発音する際の注意点は？",
             ["k と n の間に母音 u を入れて「クナルポット」と発音する", "k と n を母音なしで直結させ、語末 t は無開放で止める", "k を発音せずに「ナルポット」と言う"],
             "k と n を母音なしで直結させ、語末 t は無開放で止める",
             "オランダ語借用語の語頭子音結合 kn- は母音を挟まず、語末 t も破裂させずに止めます。"),
            ("英語の語尾「-tion」（condition, communication）はインドネシア語化するとどう変化するか？",
             ["-syong になる", "-si（kondisi, komunikasi）になる", "-tian になる"],
             "「-si（kondisi, komunikasi）」になる",
             "英語の -tion はオランダ語 -tie を経由してインドネシア語では -si と表記・調音されます。"),
            ("地方の大衆会話で「foto」が「poto」、「aktif」が「aktip」と発音される言語学的背景は？",
             ["伝統的な地域言語（ジャワ語・スンダ語等）に f の音素が存在せず、近縁の p で代用されてきた歴史があるため", "単に活字の印刷ミスが定着したため", "若者言葉としての意図的なスラング"],
             "伝統的な地域言語（ジャワ語・スンダ語等）に f の音素が存在せず、近縁の p で代用されてきた歴史があるため",
             "土着言語の音素目録に f/v がなかったため、最も調音位置が近い両唇破裂音 p に置換される音韻適応が生じました。")
        ]
    },
    {
        "id": "1193",
        "slug": "13-ai-voice-recognition-training",
        "title": "【AI音声認識特訓】Siri / Google音声入力に100%通じるクリアな調音法",
        "desc": "スマホの音声入力やAIアシスタントを誤認識させない音響工学的スピーキング。母音の均一化・閉鎖音の保持・語頭アタックの技術。",
        "theory": """### 1. AI音声認識エンジン（ASR）は人間の耳とどう違うか？
人間は会話の中で、文脈や表情、事前の知識から「多少発音が崩れていても推測して補正」してくれます。
しかし、**Siri、Google音声入力、ChatGPT Voice などの自動音声認識（ASR: Automatic Speech Recognition）は、音響モデル（周波数スペクトログラム）と音素確率のみを厳格に照合**します。

日本人の発音がAIに弾かれる（誤認識される）3大原因：
1. **母音の無声化・挿入**: 勝手に足した「u」や「o」を別の単語として認識する。
2. **語末閉鎖音の破裂欠落**: *tidak* の声門閉鎖が甘く、単なる「tida...」と判定される。
3. **語頭アタックの弱さ**: 息の立ち上がりが遅く、最初の子音（p, t, k, b, d, g）が検知されない。

### 2. AIに100%通じる「3大音響工学的ルール」
- **ルール1: 語頭子音の鋭いアタック（Clear Attack）**:
  - 発声の最初の1ミリ秒でしっかり圧力をかけ、子音の破裂・摩擦を機械のマイクに明瞭に届ける。
- **ルール2: 母音の長さを等間隔に保つ（Isometric Vowels）**:
  - 日本語のように「だぁー」「ねぇー」と母音をだらしなく引き延ばさない。インドネシア語の短母音を均一の長さでキビキビと発声する。
- **ルール3: 語末の音を完全に切る（Abrupt Cut-off）**:
  - 声門閉鎖 [ʔ] や無開放閉鎖音 [p̚, t̚] をピタッと止め、無音区間（Silence）をマイクに認識させる。""",
        "drills": [
            ("【AI入力・検索】「ジャカルタの今日の天気を教えて（cuaca Jakarta hari ini）」",
             "Bagaimana ramalan cuaca di Jakarta hari ini?",
             "バガイマナ ラマラン チュアチャ ディ ジャカルタ ハリ イニ？",
             "cuaca の c [tʃ] を鋭く立ち上げ、hari ini の母音を均等な長さで刻む。"),
            ("【AI入力・道案内】「一番近いガソリンスタンドはどこですか？（pom bensin terdekat）」",
             "Tunjukkan jalan menuju pom bensin terdekat dari sini.",
             "トゥンジュッカン ジャラン ムヌジュ ポム ベンシン トゥル ドゥカッ ダリ シニ。",
             "terdekat の語末 t をピタッと止める。pom bensin はクリアに唇を破裂させる。"),
            ("【AI入力・リマインダー】「明日の朝7時にアラームを設定して（setel alarm jam tujuh）」",
             "Setel alarm untuk besok pagi pada jam tujuh tepat.",
             "セテル アラルム ウントゥッ ベソッ パギ パダ ジャム トゥジュ トゥパッ。",
             "tujuh の語末 h と tepat の語末 t を正確に吹き分け、AIの誤入力を防ぐ。"),
            ("【AI入力・翻訳】「この文章を日本語に翻訳してください（terjemahkan kalimat ini）」",
             "Tolong terjemahkan kalimat ini ke dalam bahasa Jepang.",
             "トロン トゥルジェマカン カリマッ イニ ク ダラム バハサ ジェパン。",
             "kalimat の t を落とさず止め、bahasa Jepang の p を明瞭に弾く。"),
            ("【AI入力・電話発信】「田中さんに電話をかけて（telepon Tanaka）」",
             "Tolong panggil nomor telepon Bapak Tanaka sekarang.",
             "トロン パンギル ノモル テレポン バパッ タナカ スカラン。",
             "panggil の p と Bapak の k を鋭く立たせる。"),
            ("【AI入力・音楽再生】「インドネシアのポップスを再生して（putar lagu pop Indonesia）」",
             "Putar lagu pop Indonesia terbaru di Spotify.",
             "プタル ラグ ポップ インドネシア トゥルバル ディ スポティファイ。",
             "putar の語末 r を軽く振動させ、pop の p を唇で止める。"),
            ("【AI入力・メモ】「牛乳と卵を買うとメモして（catat beli susu dan telur）」",
             "Catat di daftar belanja: beli susu segar dan telur ayam.",
             "チャタッ ディ ダフタル ブランジャ: ブリ スス スガル ダン トゥルル アヤム。",
             "catat の語末 t を声門で閉じる。telur の r を曖昧にしない。"),
            ("【AI入力・質問】「インドネシアの独立記念日はいつですか？（hari kemerdekaan）」",
             "Kapan hari kemerdekaan Republik Indonesia dirayakan?",
             "カパン ハリ クムルデカアン レプブリッ インドネシア ディラヤカン？",
             "kemerdekaan の double a を等間隔で明瞭に発音する。"),
            ("【AI入力・通貨換算】「10万ルピアは日本円でいくらですか？（seratus ribu rupiah）」",
             "Berapa nilai seratus ribu rupiah jika dikonversi ke yen?",
             "ブラパ ニライ スラトゥス リブ ルピア ジカ ディコンヴェルシ ク エン？",
             "seratus の s をしっかり摩擦させ、rupiah の p をクリアに発声。"),
            ("【AI入力・メッセージ】「5分遅れますとメッセージを送って（terlambat lima menit）」",
             "Kirim pesan ke bos bahwa saya akan terlambat lima menit.",
             "キリム プサン ク ボス バワ サヤ アカン トゥルラムバッ リマ ムニッ。",
             "terlambat と menit の両方の語末 t を正確に止める。"),
            ("【AI入力・スケジュール】「明日の午後3時に会議を登録して（rapat jam tiga）」",
             "Jadwalkan rapat evaluasi proyek besok sore jam tiga.",
             "ジャドワルカン ラパッ エヴァルアシ プロイェッ ベソッ ソレ ジャム ティガ。",
             "jadwalkan の dw をスムーズに繋ぎ、rapat の t を遮断する。"),
            ("【AI入力・レストラン予約】「今夜7時に4名で予約できますか？（reservasi empat orang）」",
             "Buat reservasi meja untuk empat orang nanti malam jam tujuh.",
             "ブアッ レセルヴァシ メジャ ウントゥッ エンパッ オラン ナンティ マラム ジャム トゥジュ。",
             "empat の t と orang の ng をノイズなく入力する。"),
            ("【AI入力・タクシー手配】「スカルノハッタ空港まで車を呼んで（pesan taksi ke bandara）」",
             "Pesan taksi sekarang menuju Bandara Internasional Soekarno-Hatta.",
             "プサン タクシ スカラン ムヌジュ バンダラ インテルナシオナル スカルノ ハッタ。",
             "taksi の k-s 結合を母音なしでシャープに発音。"),
            ("【AI入力・ニュース要約】「今日の主要ニュースを要約して（ringkas berita hari ini）」",
             "Tolong ringkas berita utama nasional hari ini dalam tiga poin.",
             "トロン リングカス ブリタ ウタマ ナシオナル ハリ イニ ダラム ティガ ポイン。",
             "ringkas の ng と s を高精度で調音。"),
            ("【総仕上げ】「今日のスケジュール（jadwal hari ini）を確認し、田中さんに会議が3時（jam tiga）からだと伝えて（sampaikan rapat）」",
             "Cek jadwal saya hari ini, lalu kirim pesan bahwa rapat dimulai jam tiga.",
             "チェッ ジャドワル サヤ ハリ イニ、ラル キリム プサン バワ ラパッ ディムライ ジャム ティガ。",
             "AIの音声認識ログを見ながら、1単語も誤認識されずに100%テキスト化されるまで練習する。")
        ],
        "quizzes": [
            ("スマホの音声認識（Siri / Google）が日本人のインドネシア語を誤認識する最大の要因は？",
             ["話すスピードがネイティブより速すぎること", "子音の後に余計な母音を足したり、語末閉鎖音が弱く音響モデルと一致しないこと", "声のトーンが高すぎること"],
             "子音の後に余計な母音を足したり、語末閉鎖音が弱く音響モデルと一致しないこと",
             "AIは音響特徴量（周波数パターン）を音素辞書と照合するため、母音挿入や閉鎖音の崩れがあると即座に別単語と判定されます。"),
            ("AI音声認識に対して最も認識率が高くなる母音の発声法は？",
             ["日本語のように語尾をだらしなく引き延ばして発音する", "母音の長さをキビキビと等間隔に保ち、余計な長音化を避ける", "母音をできる限り小さな声でささやく"],
             "母音の長さをキビキビと等間隔に保ち、余計な長音化を避ける",
             "短母音の均一な持続時間は音節の境界を明瞭にし、AIが単語を正確に切り出すのを助けます。"),
            ("単語の頭（語頭子音）を発音する際のAI対策として有効なテクニックは？",
             ["最初の1ミリ秒で圧力をかけて鋭く立ち上げる（Clear Attack）", "喉に力を入れずに息を吐くだけにする", "語頭を完全に省略して2番目の音節から発音する"],
             "最初の1ミリ秒で圧力をかけて鋭く立ち上げる（Clear Attack）",
             "語頭の破裂や摩擦のエネルギーが明瞭であるほど、機械学習モデルは先頭音素を確信を持って特定できます。")
        ]
    },
    {
        "id": "1194",
        "slug": "14-tongue-twisters-speed-drill",
        "title": "【早口言葉（Lidah Terbelit）】舌の回転速度を上げる伝統的アナウンサー訓練法",
        "desc": "インドネシアの放送局アナウンサーが実際に用いる早口言葉（Pembelit Lidah）。舌の可動域と筋力を限界まで鍛え上げる特訓。",
        "theory": """### 1. なぜ早口言葉（Pembelit Lidah）が効果的なのか？
早口言葉（Bahasa Indonesia: *Pembelit Lidah* または *Tongue Twister*）は、**類似した調音位置を持つ音素（k/t, r/l, s/c, b/p）が交互に高速で出現する人工的な音声ドリル**です。

調音器官（舌・唇）の筋肉は、普段使い慣れていない動きを高速で要求されると、脳からの運動指令と筋肉の収縮が追いつかずに「舌がもつれる（Lidah Terbelit）」現象を起こします。
早口言葉を毎日3分間トレーニングすることで：
1. **舌先の瞬発力と可動域が劇的に向上する**。
2. **調音位置の切り替え（前舌 ↔ 後舌 ↔ 唇）の神経回路が強化される**。
3. **通常の日常会話が「スローモーション」のように感じられるようになる**。

### 2. インドネシアの伝統的・代表的早口言葉
- **k-k-k の閉鎖連打**:
  - *Kuku kaki kakek-kakekku kaku-kaku.*（私の祖父たちの足の爪は硬い）
- **r-l の舌先弾き分け**:
  - *Ular melingkar-lingkar di atas pagar bundar.*（蛇が丸いフェンスの上でとぐろを巻いている）
- **k-k 困惑系**:
  - *Kakak kok kikuk-kikuk?*（お兄さん/お姉さんはなぜそんなにおどおどしているの？）""",
        "drills": [
            ("【早口言葉1: 初級】「私の祖父の足の爪は硬い（Kuku kaki kakek）」",
             "Kuku kaki kakek-kakekku kaku-kaku.",
             "クク カキ カケッカケック カクカク。",
             "k と u/a/i の組み合わせが連続する。語末 k の声門閉鎖を崩さず3回連続で唱える。"),
            ("【早口言葉2: 初級】「なぜお兄さんはそんなにおどおどしているの？（Kakak kok kikuk）」",
             "Kakak kok kikuk-kikuk, kakek kok batuk-batuk?",
             "カカッ コッ キクッキクッ、カケッ コッ バトゥッバトゥッ？",
             "kikuk の声門閉鎖と batuk の t-k 移行をリズミカルに跳ねさせる。"),
            ("【早口言葉3: 中級】「蛇が丸いフェンスの上でとぐろを巻いている（Ular melingkar）」",
             "Ular melingkar-lingkar di atas pagar bundar.",
             "ウラル ムリンカルリンカル ディ アタス パガル ブンダル。",
             "l（側面音）と r（巻き舌ふるえ音）が交互に激しく入れ替わる最高峰のドリル。"),
            ("【早口言葉4: 中級】「青いペンシル、丸い円（Pensil biru）」",
             "Satu biru, dua biru, tiga biru, empat biru, lima biru...",
             "サトゥ ビル、ドゥア ビル、ティガ ビル、エンパッ ビル、リマ ビル...",
             "biru の r と各数字の語末子音（t, m）を1秒に2回のペースで加速。"),
            ("【早口言葉5: 上級】「丸い丸い大豆の揚げ煎餅（Roti bulat）」",
             "Roti bolu bulat-bulat, bola bulu bulat-bulat.",
             "ロティ ボル ブラッブラッ、ボラ ブル ブラッブラッ。",
             "b, l, r, t の音素が目まぐるしく入れ替わる。唇と舌先のコンビネーション。"),
            ("【早口言葉6: 難関】「ワニとトカゲの競争（Buaya biawak）」",
             "Buaya, biawak, buaya, biawak, buaya, biawak...",
             "ブアヤ、ビアワッ、ブアヤ、ビアワッ、ブアヤ、ビアワッ...",
             "二重母音・渡り音 ua と ia、語末声門閉鎖 k を超高速で往復する。"),
            ("【早口言葉7: 難関】「頭を洗うシャンプー（Keramas）」",
             "Kucing kurus keramas di atas kardus karatan.",
             "クチン クルス クラマス ディ アタス カルドゥス カラタン。",
             "ku- kur- ker- kar- と k+r の母音バリエーションを正確に撃ち抜く。"),
            ("【早口言葉8: 応用】「市場のスイカ（Semangka segar）」",
             "Semangka segar sangat manis, semangka manis sangat segar.",
             "スマンカ スガル サンガッ マニス、スマンカ マニス サンガッ スガル。",
             "s, ng, r, m の鼻音と摩擦音の連続スイッチング。"),
            ("【早口言葉9: 応用】「赤い豆と青い豆（Kacang merah）」",
             "Kacang merah, kacang putih, kacang hijau, kacang tanah.",
             "カチャン メラ、カチャン プティ、カチャン ヒジャウ、カチャン タナ。",
             "c [tʃ] の破擦音と語末 h の息抜けを均一に保ちながら速度を上げる。"),
            ("【早口言葉10: 最難関】「道端のココナッツの木（Kelapa di tepi jalan）」",
             "Kelapa diparut, kelapa dipipit, kelapa diparut, kelapa dipipit.",
             "クラパ ディパルッ、クラパ ディピピッ、クラパ ディパルッ、クラパ ディピピッ。",
             "diparut（r-t）と dipipit（p-t）の調音位置の微細な差異を舌先に叩き込む。"),
            ("【スピード変化練習】「Kuku kaki kakek を低速から最高速へ」",
             "Kuku kaki kakekku kaku... Kuku kaki kakekku kaku... Kuku kaki kakek-kakekku kaku-kaku!",
             "クク カキ カケック カク...（徐々にスピードを上げ、息継ぎなしで一気に最高速へ）",
             "メトロノームに合わせてテンポを 60 → 90 → 120 → 160 BPM と引き上げる。"),
            ("【舌先集中ドリル】「Pagar kawat（針金フェンス）」",
             "Pagar kawat berkarat ditarik erat-erat.",
             "パガル カワッ ブルカラッ ディタリッ エラッエラッ。",
             "r と t の語末連打。舌先が疲れてもフォームを崩さない。"),
            ("【唇集中ドリル】「Bibir bengkak（唇が腫れる）」",
             "Bibir bapa bengkak kena batu bata.",
             "ビビル バパ ベンカッ クナ バトゥ バタ。",
             "b と p の両唇音の連続。唇を力強く弾き合わせる。"),
            ("【喉奥集中ドリル】「Katak lompat（カエルが跳ぶ）」",
             "Katak lompat di kotak-kotak dekat kolam katak.",
             "カタッ ロンパッ ディ コタッコタッ ドゥカッ コラム カタッ。",
             "k-t, t-k の入れ替えで喉と舌先の連動性を極限まで高める。"),
            ("【総合超絶技巧】「Kuku kaki kakek + Ular melingkar 2連撃」",
             "Kuku kaki kakek-kakekku kaku-kaku, ular melingkar di atas pagar bundar!",
             "クク カキ カケッカケック カクカク、ウラル ムリンカル ディ アタス パガル ブンダル！",
             "インドネシア語の2大早口言葉をノーミス・一息で完全制覇する。")
        ],
        "quizzes": [
            ("インドネシア語の代表的早口言葉「Kuku kaki kakek-kakekku kaku-kaku」の日本語の意味は？",
             ["私の祖父たちの足の爪は硬い", "おじいさんが川で足を洗っている", "鶏の足がフェンスに引っかかった"],
             "私の祖父たちの足の爪は硬い",
             "kuku（爪）、kaki（足）、kakek（祖父）、kaku（硬い・凝る）という k 音の単語を連ねた定番の早口言葉です。"),
            ("早口言葉「Ular melingkar-lingkar di atas pagar bundar」が訓練する主な調音能力は？",
             ["鼻濁音 ng と ny の聞き分け", "側面音 l と歯茎ふるえ音（巻き舌）r の高速切り替え", "母音 e のテーリングとプルペッの区別"],
             "側面音 l と歯茎ふるえ音（巻き舌）r の高速切り替え",
             "u-lar, me-ling-kar, pa-gar, bun-dar と l と r が交互に出現し、舌先の運動パターンを鍛えます。"),
            ("早口言葉の練習において、舌がもつれたときの最も効果的なトレーニング法は？",
             ["もつれたまま適当にごまかして最後まで走り抜ける", "一度テンポを落として超スローで調音位置を確認し、そこから徐々に速度を上げる", "大声で叫んで勢いで突破する"],
             "一度テンポを落として超スローで調音位置を確認し、そこから徐々に速度を上げる",
             "筋肉の記憶（Muscle Memory）を正しく構築するためには、正確な調音位置を低速で神経に刷り込んでから加速するのが科学的です。")
        ]
    },
    {
        "id": "1195",
        "slug": "15-variable-speed-shadowing",
        "title": "【プロソディ・速度可変訓練】0.8倍速から1.5倍速まで自在に操るシャドーイング",
        "desc": "再生速度を自在にコントロールして脳の音声処理能力を拡張する。0.8倍速の精密調音から1.5倍速の超速脳内デコーディングまで。",
        "theory": """### 1. 「速度可変シャドーイング（Variable-Speed Shadowing）」のメカニズム
語学学習において、常に一定の速度（1.0倍速）だけで練習していると、脳の音韻処理能力が頭打ちになります。
速度を意図的に変化させることで、以下の異なる認知能力を鍛え分けることができます。

1. **0.8倍速: 精密調音モード（Precision Articulation）**:
   - 舌の位置、唇の形、声門閉鎖のタイミング、曖昧母音の脱力など、**普段のスピードでは見落としがちな細部のフォームを完璧に矯正**する。
2. **1.0倍速: 自然プロソディモード（Natural Cadence）**:
   - ネイティブの自然なリズム、息継ぎの場所、イントネーションの波を身体に同調させる。
3. **1.2倍速: リアル会話追従モード（Real-World Fluency）**:
   - 若者の早口、ジャカルタのストリート会話、白熱した議論のスピードに耳と口を慣らす。
4. **1.5倍速: 超速ハイパードライブモード（High-Load Decoding）**:
   - 脳のワーキングメモリに極限の負荷をかける。1.5倍速を経験した後に1.0倍速に戻すと、**まるで周囲がスローモーションのようにクリアに聞き取れる「インターバル効果」**が得られる。""",
        "drills": [
            ("【0.8倍速・精密調音】「私たちは持続可能な開発目標に向けて努力しています」",
             "Kami berkomitmen untuk mendukung pembangunan berkelanjutan demi masa depan.",
             "カミ ブルコミットメン ウントゥッ ムンドゥクン プンバングナン ブルクランジュタン デミ マサ ドゥパン。",
             "0.8倍速で ber-komitmen, pem-bangunan, ber-kelanjutan の各音節を解剖学的に正確に発声。"),
            ("【1.0倍速・標準速度】「私たちは持続可能な開発目標に向けて努力しています」",
             "Kami berkomitmen untuk mendukung pembangunan berkelanjutan demi masa depan.",
             "カミ ブルコミットメン ウントゥッ ムンドゥクン プンバングナン ブルクランジュタン デミ マサ ドゥパン。",
             "1.0倍速で滑らかなリンキングと、文末 masa depan への穏やかな下降調を再現。"),
            ("【1.2倍速・実戦速度】「私たちは持続可能な開発目標に向けて努力しています」",
             "Kami berkomitmen untuk mendukung pembangunan berkelanjutan demi masa depan.",
             "カミ ブルコミットメン ウントゥッ ムンドゥクン プンバングナン ブルクランジュタン デミ マサ ドゥパン。",
             "1.2倍速で息継ぎを最小限にし、リズムを崩さずに一息で畳み掛ける。"),
            ("【1.5倍速・超速追唱】「私たちは持続可能な開発目標に向けて努力しています」",
             "Kami berkomitmen untuk mendukung pembangunan berkelanjutan demi masa depan.",
             "カミ ブルコミットメン ウントゥッ ムンドゥクン プンバングナン ブルクランジュタン デミ マサ ドゥパン。",
             "1.5倍速で脳内デコードをフル回転。口がもつれても音の輪郭を追い続ける。"),
            ("【0.8倍速・日常短文】「もし時間があれば、一緒に美味しいコーヒーを飲みに行こう」",
             "Kalau kamu ada waktu senggang, ayo kita pergi ngopi bareng.",
             "カラウ カム アダ ワクトゥ スンガン、アヨ キタ プルギ ンゴピ バレン。",
             "kalau の二重母音、waktu の k 閉鎖、ngopi の語頭 ng をスローモーションで確認。"),
            ("【1.2倍速・日常短文】「もし時間があれば、一緒に美味しいコーヒーを飲みに行こう」",
             "Kalau kamu ada waktu senggang, ayo kita pergi ngopi bareng.",
             "カラウ カム アダ ワクトゥ スンガン、アヨ キタ プルギ ンゴピ バレン。",
             "口語の軽快なテンポで、kalau kamu ada を一塊のチャンクとして飛ばす。"),
            ("【1.5倍速・日常短文】「もし時間があれば、一緒に美味しいコーヒーを飲みに行こう」",
             "Kalau kamu ada waktu senggang, ayo kita pergi ngopi bareng.",
             "カラウ カム アダ ワクトゥ スンガン、アヨ キタ プルギ ンゴピ バレン。",
             "瞬時に発音器官を動かし、0.5秒以内に全フレーズを言い終える。"),
            ("【0.8倍速・ビジネス】「本日の議題について、皆様のご意見を率直にお聞かせください」",
             "Terkait agenda hari ini, kami sangat mengharapkan masukan terbuka dari Bapak dan Ibu.",
             "トゥルカイッ アゲンダ ハリ イニ、カミ サンガッ ムンハラプカン マスカン トゥルブカ ダリ バパッ ダン イブ。",
             "Bapak dan Ibu の敬称、mengharapkan の接尾辞 -kan の調音位置を丁寧に固定。"),
            ("【1.2倍速・ビジネス】「本日の議題について、皆様のご意見を率直にお聞かせください」",
             "Terkait agenda hari ini, kami sangat mengharapkan masukan terbuka dari Bapak dan Ibu.",
             "トゥルカイッ アゲンダ ハリ イニ、カミ サンガッ ムンハラプカン マスカン トゥルブカ ダリ バパッ ダン イブ。",
             "ビジネスミーティングのテンポの良い司会進行のリズムで発声。"),
            ("【0.8倍速・長文解説】「経済成長と環境保全のバランスを取ることは容易ではありません」",
             "Menyeimbangkan pertumbuhan ekonomi dengan pelestarian lingkungan bukanlah tugas yang mudah.",
             "ムニェインバンカン プルトゥムブハン エコノミ ドゥンガン プレスタリアン リングンガン ブカンラ トゥガス ヤン ムダ。",
             "menyeimbangkan の ny と ng、lingkungan の連続鼻音を正確に分解調音。"),
            ("【1.2倍速・長文解説】「経済成長と環境保全のバランスを取ることは容易ではありません」",
             "Menyeimbangkan pertumbuhan ekonomi dengan pelestarian lingkungan bukanlah tugas yang mudah.",
             "ムニェインバンカン プルトゥムブハン エコノミ ドゥンガン プレスタリアン リングンガン ブカンラ トゥガス ヤン ムダ。",
             "ニュースキャスターの標準的な報道速度で淀みなく一気に読む。"),
            ("【1.5倍速・長文解説】「経済成長と環境保全のバランスを取ることは容易ではありません」",
             "Menyeimbangkan pertumbuhan ekonomi dengan pelestarian lingkungan bukanlah tugas yang mudah.",
             "ムニェインバンカン プルトゥムブハン エコノミ ドゥンガン プレスタリアン リングンガン ブカンラ トゥガス ヤン ムダ。",
             "高負荷をかけ、耳に入った音声を脳内で即座に調音コマンドに変換する。"),
            ("【速度落差の体験】「1.5倍速直後に1.0倍速へ戻す（インターバル効果）」",
             "Belajar bahasa Indonesia dengan tekun pasti akan membuahkan hasil yang manis.",
             "ブラジャル バハサ インドネシア ドゥンガン トゥクン パスティ アカン ムンブアカン ハシル ヤン マニス。",
             "1.5倍速の直後に通常速度で読むと、驚くほど口がスムーズに動き、余裕が生まれることを体感。"),
            ("【総合・早口追従】「時間がありませんので、要点だけ手短にお伝えします」",
             "Karena waktu sangat terbatas, saya akan menyampaikan poin-poin intinya saja.",
             "カルナ ワクトゥ サンガッ トゥルバタス、サヤ アカン ムニャンパイカン ポインポイン インティニャ サジャ。",
             "早口でテキパキと要約するビジネスマンのスピード感を体現。"),
            ("【総仕上げ・フルスピード変奏曲】「0.8倍速 → 1.0倍速 → 1.2倍速 → 1.5倍速」",
             "Kecepatan berbicara bukanlah tujuan utama, melainkan kejelasan pesan yang kita sampaikan.",
             "クチパタン ブルビチャラ ブカンラ トゥジュアン ウタマ、ムラインカン クジュラサン プサン ヤン キタ スラカン。",
             "1つの文章を4段階の速度で自在にコントロールし、速度可変の適応力を完成させる。")
        ],
        "quizzes": [
            ("シャドーイングを0.8倍速の低速で行う最大の目的は何か？",
             ["単語の意味をゆっくり日本語に訳すため", "普段の速度では見落としがちな舌の位置や閉鎖音の精密なフォームを点検・矯正するため", "単に疲れた時の休憩のため"],
             "普段の速度では見落としがちな舌の位置や閉鎖音の精密なフォームを点検・矯正するため",
             "低速練習は、調音器官の解剖学的なフォームを正確にチェックし、悪癖を取り除くための精密調音モードです。"),
            ("1.5倍速の高速シャドーイングを行った後に得られる「インターバル効果」とは？",
             ["頭痛がして発音できなくなること", "通常の1.0倍速に戻した際に、相手の声がスローモーションのように遅く感じられ、余裕を持って発話できるようになること", "単語のスペルを忘れてしまうこと"],
             "通常の1.0倍速に戻した際に、相手の声がスローモーションのように遅く感じられ、余裕を持って発話できるようになること",
             "脳の音韻ワーキングメモリに高負荷をかけた後、通常速度に戻すと知覚的な余裕（Headroom）が劇的に拡大します。"),
            ("高速シャドーイング（1.2〜1.5倍速）を行う際、最も意識すべきポイントは？",
             ["すべての単語を日本語に逐語訳しながら発音する", "息継ぎを最小化し、単語をブツ切りにせずチャンク（意味の塊）として滑らかに繋ぐ", "大声を出して音声をかき消す"],
             "息継ぎを最小化し、単語をブツ切りにせずチャンク（意味の塊）として滑らかに繋ぐ",
             "高速発話では個々の単語を区切る暇がないため、リンキングを活用してチャンク単位で流れるように発声します。")
        ]
    },
    {
        "id": "1196",
        "slug": "16-emotional-pitch-inflection",
        "title": "【感情とピッチ高低差】怒り・喜び・皮肉・親愛を伝える音調コントロール",
        "desc": "文法や単語が同じでも、ピッチ（音高）と音調曲線（インフレクション）で感情が180度変わる。感情表現プロソディの極意。",
        "theory": """### 1. 「感情プロソディ（Emotional Prosody）」とは？
人間が言葉を交わす際、伝達される情報の半分以上は「言葉そのものの意味（Verbal）」ではなく、「**声のトーン・ピッチの高さ・音の強弱・話す速度（Vocal / Prosodic）**」によって決まります。

インドネシア語は、感情がピッチ曲線（ピッチインフレクション: Pitch Inflection）に極めてダイレクトに反映される言語です。
特に以下の感情パラメータを使い分ける必要があります。

### 2. 4大感情の音響プロファイル
1. **喜び・賞賛・感激（Joy & Admiration）**:
   - **高音域（High Pitch）**、全体に波打つようなメロディ、語尾の母音や感嘆詞（*wah*, *hebat ya*）が明るく伸びる。
2. **怒り・抗議・不満（Anger & Frustration）**:
   - **低〜中音域の硬い音（Tense Voice）**、急激なスタッカート（音が途切れる）、語末閉鎖音（k, t, p）が強く叩きつけられるように閉じる。
3. **親愛・甘え・懇願（Affection & Pleading）**:
   - **中高音域の柔らかい音（Soft & Breathy）**、語尾の小詞（*dong*, *sih*, *ya*）を猫なで声のように少し持ち上げて滑らかに抜く。
4. **皮肉・からかい・疑念（Sarcasm & Doubt）**:
   - **不自然に平坦な低音から、最後の1音節だけを極端に跳ね上げる（Flat then Sharp Rise）**。
   - 例: *Masa iya?*（まさか〜？ [語尾の ya を高く強調]）""",
        "drills": [
            ("【喜び・感激】「うわあ、信じられない！本当に合格したの？！おめでとう！」",
             "Wah, luar biasa sekali! Kamu beneran lulus?! Selamat ya!",
             "ワァ（高音・歓喜）、ルアル ビアサ スカリ！ カム ブネラン ルルス？！ スラマッ ヤ！",
             "Wah でピッチを一気に最高点に上げ、笑顔の表情筋を使って明るく響かせる。"),
            ("【喜び・感激】「この料理、言葉が出ないくらい美味しい！」",
             "Ya ampun, makanan ini enak banget! Bikin nagih rasanya!",
             "ヤ アンプン、マカナン イニ エナッ バンゲッ！ ビキン ナギ ラサニャ！",
             "Ya ampun を高めのピッチで弾ませ、enak banget に熱狂的なトーンを込める。"),
            ("【怒り・抗議】「ふざけないでくれ！何度同じミスを繰り返せば気が済むんだ！」",
             "Jangan main-main ya! Sudah berapa kali kamu mengulangi kesalahan yang sama?!",
             "ジャンガン マインマイン ヤ！（低音・鋭い） スダ ブラパ カリ カム ムングランギ クサラハン ヤン サマ？！",
             "声のトーンを低く落とし、Jangan main-main の各音節を硬く叩きつけるように発音。"),
            ("【怒り・抗議】「いい加減にして！私の話を全然聞いてないじゃない！」",
             "Cukup ya! Dari tadi kamu sama sekali tidak mendengarkan penjelasan saya!",
             "チュクッ ヤ！（急激な閉鎖） ダリ タディ カム サマ スカリ ティダッ ムンデンガルカン プンジェラサン サヤ！",
             "Cukup の語末 p を強く噛み締め、語尾 ya を冷たく切り落とす。"),
            ("【親愛・甘え】「ねえ、お願いだから手伝ってよ、頼むから〜（tolong dong）」",
             "Ayo dong, tolongin aku sebentar aja... Kamu kan baik hati.",
             "アヨ ドン〜（甘えた高音）、トロンギン アク スブンタル アジャ... カム カン バイク ハティ。",
             "dong と aja の語尾を優しく引き延ばし、相手の懐に入るような柔らかいトーン。"),
            ("【親愛・甘え】「怒らないでよ、ちょっと冗談言っただけじゃん〜」",
             "Jangan ngambek dong sayang, aku cuma bercanda sedikit kok.",
             "ジャンガン ンガムベッ ドン サヤン〜、アク チュマ ブルチャンダ スディキッ コッ。",
             "ngambek dong を丸みのあるメロディで包み込み、kok を優しく添える。"),
            ("【皮肉・疑念】「へえー、そうなの？ずいぶん偉くなったもんだね」",
             "Oh ya? Hebat banget ya kamu sekarang, sudah sombong ya.",
             "オ ヤ〜？（平坦から語尾跳ね上げ） ヘバッ バンゲッ ヤ カム スカラン、スダ ソンボン ヤ。",
             "Oh ya? を不自然にフラットに保ち、Hebat banget で冷笑的なピッチを乗せる。"),
            ("【皮肉・疑念】「本当かなあ？また口先だけの約束じゃないの？」",
             "Masa iya sih? Jangan-jangan cuma janji manis di bibir doang.",
             "マサ イヤ シ〜？（疑念のピッチ揺れ） ジャンガンジャンガン チュマ ジャンジ マニス ディ ビビル ドアン。",
             "Masa iya sih の語尾を少し歪めるように持ち上げ、信じていないニュアンスを出す。"),
            ("【困惑・躊躇】「うーん、どう言ったらいいか…ちょっと難しいですね」",
             "Aduh, gimana ya ngomongnya... Agak sulit sih kalau kondisinya begini.",
             "アドゥー、ギマナ ヤ ンゴモンニャ...（迷いの揺れ） アガッ スリッ シ カロウ コンディシニャ ブギニ。",
             "Aduh と gimana ya のピッチを定まらずに漂わせ、判断に迷う心理を表現。"),
            ("【困惑・躊躇】「本当に申し訳ないんですが、私にはどうすることもできなくて…」",
             "Duh, maaf banget ya, sepertinya aku bener-bener gak bisa bantu apa-apa.",
             "ドゥッ、マアフ バンゲッ ヤ... スプルティニャ アク ブネルブネル ガッ ビサ バントゥ アパアパ。",
             "トーンを全体的に暗く沈ませ、申し訳なさを声の息漏れ（Breathy Voice）で伝える。"),
            ("【失望・落胆】「あーあ、あんなに頑張ったのに、全部無駄になっちゃった…」",
             "Yah, padahal kita sudah berusaha sekuat tenaga, tapi sia-sia jadinya.",
             "ヤー（深いため息）、パダハル キタ スダ ブルサハ スクアッ トゥナガ、タピ シアシ ア ジャディニャ。",
             "Yah で重いため息をつき、文末に向かって音程を完全に底まで落とす。"),
            ("【激励・鼓舞】「大丈夫！君なら絶対にできる！自分を信じて！」",
             "Tenang saja! Kamu pasti bisa melewati ini semua! Percaya pada dirimu sendiri!",
             "トゥナン サジャ！（力強い中音） カム パスティ ビサ ムルワティ イニ スムア！ プルチャヤ パダ ディリム スンディリ！",
             "Tenang saja と pasti bisa に前向きなエネルギーを込め、リズムを力強く前進させる。"),
            ("【驚愕・恐怖】「えっ？！本当ですか？！警察を呼んでください！」",
             "Hah?! Yang bener?! Cepat panggil polisi sekarang juga!",
             "ハッ？！（息を吸い込むような高音） ヤン ブネル？！ チパッ パンギル ポリシ スカラン ジュガ！",
             "Hah で息を呑み、短く切迫したリズムで叫ぶように調音。"),
            ("【穏やかな愛情】「いつもそばにいてくれて、本当にありがとう」",
             "Terima kasih ya sudah selalu setia mendampingi aku selama ini.",
             "トゥリマ カシ ヤ（温かい低中音） スダ スラル スティア ムンダンピンギ アク スラマ イニ。",
             "ゆっくりとした呼吸で、一語一語を抱きしめるように温かいピッチで発声。"),
            ("【感情の落差演習】「怒り ⤓ から一転して歓喜 ↗ へ」",
             "Tadi aku marah banget sama kamu! Tapi karena kamu bawa martabak manis, aku maafkan deh!",
             "タディ アク マラ バンゲッ（低く怒る）！ タピ カルナ カム バワ マルタバッ マニス、アク マアフカン デッ（一気に笑顔と高音）！",
             "1つの発話の中で怒りの重低音と、許しの明るい高音をドラマチックに切り替える。")
        ],
        "quizzes": [
            ("インドネシア語で「怒り」や「不満」を伝える際、音響プロファイル（声のトーン）はどう変化するか？",
             ["声のトーンが高くなり、甘えたように語尾が伸びる", "声のトーンが低く硬くなり、スタッカートのように語末子音が鋭く途切れる", "全く抑揚のない平坦な機械音になる"],
             "声のトーンが低く硬くなり、スタッカートのように語末子音が鋭く途切れる",
             "怒りや抗議は、低いピッチ、緊張した筋肉（Tense Voice）、鋭い閉鎖音の遮断によって表現されます。"),
            ("相手にお願いや甘え（dong, ya）を伝えるときの自然なイントネーションは？",
             ["怒鳴るように語尾を強く叩きつける", "柔らかい中高音域で、語尾の小詞を猫なで声のように滑らかに持ち上げて抜く", "ボソボソと聞き取れない声でつぶやく"],
             "柔らかい中高音域で、語尾の小詞を猫なで声のように滑らかに持ち上げて抜く",
             "親愛や懇願は、柔らかい息遣いと語尾の上昇〜滑音によって相手の心理的警戒を解く効果があります。"),
            ("「Masa iya sih?（まさか〜？）」を皮肉や疑念を込めて発音する際のピッチの特徴は？",
             ["最初から最後まで完全に高い音で歌うように発音する", "全体を不自然に平坦な低音に保ち、最後の音節（sih）だけを極端に跳ね上げる", "急激に下降させて終わる"],
             "全体を不自然に平坦な低音に保ち、最後の音節（sih）だけを極端に跳ね上げる",
             "皮肉（Sarcasm）特有のトーンは、フラットな低音と最後の鋭い跳ね上げの不協和音によって生み出されます。")
        ]
    },
    {
        "id": "1197",
        "slug": "17-drama-dialogue-overlapping",
        "title": "【映画・ドラマのセリフ完全完コピ】息遣い・間（ま）・ため息まで真似るオーバーラッピング",
        "desc": "シャドーイングの最終進化形「オーバーラッピング（Overlapping）」。映像作品の俳優と完全にタイミングを重ね、身体性ごと完コピする極意。",
        "theory": """### 1. 「オーバーラッピング（Overlapping）」とは？
シャドーイングが「音声を0.5〜1秒遅れて追いかける」のに対し、**オーバーラッピングは「音声と全く同時に、0ミリ秒のズレもなく完全に重ねて発声する訓練法」**です。

スクリプトと音声を完全に把握した状態で、**俳優の口の動き、息を吸う音（Inhalation）、息を吐くため息（Sigh）、言葉と言葉の間の沈黙（Pause）、語尾の消え入り方までミリ秒単位で完全に同期**させます。

### 2. なぜ映画・ドラマのセリフ完コピが最強なのか？
1. **「身体性（Embodiment）」の獲得**:
   - 言語は頭の中の抽象概念ではなく、表情筋、呼吸、身振り手振りと連動した「身体運動」です。役になりきることで、ネイティブの身体性を直接インストールできます。
2. **間（ま）と相槌のマスター**:
   - 会話の生命線である「沈黙の間」「相槌（*hmm*, *he-eh*, *ya ampun*, *astaga*）」の自然なタイミングが身体に染み込みます。
3. **レジスター（社会言語的場面）への即応**:
   - 恋人同士の囁き、家族の口喧嘩、オフィスの緊張した対話など、教科書では学べない生々しいリアリティを習得できます。""",
        "drills": [
            ("【恋愛ドラマ・別れ話】「もう無理だよ。君と一緒にいても、お互いに傷つけ合うだけだ」",
             "Udah gak bisa lagi, Rin. Kalau kita terus paksain kayak gini, kita cuma bakal saling nyakitin.",
             "ウダ ガッ ビサ ラギ、リン。（重い息） カロウ キタ トゥルス パクサイン カヤッ ギニ、キタ チュマ バカル サリン ニャキティン。",
             "名前（Rin）を呼んだ後の0.5秒の沈黙、ため息混じりの udah gak bisa を完全に同期させる。"),
            ("【恋愛ドラマ・引き止め】「行かないで！お願い、私の話を聞いて！全部私の誤解だったの！」",
             "Jangan pergi dulu! Dengerin aku dulu sebentar! Itu semua cuma salah paham, Rangga!",
             "ジャンガン プルギ ドゥル！（悲痛な叫び） ドゥンゲリン アク ドゥル スブンタル！ イトゥ スムア チュマ サラ パハム、ランガ！",
             "息を吸い込むタイミングと、Rangga! の前の切迫した叫びを俳優のピッチと完璧に重ねる。"),
            ("【家族ドラマ・親子の口論】「お父さんはいつだってそう！私の気持ちなんて一度も考えてくれたことないじゃない！」",
             "Papa tuh selalu begitu! Dari dulu Papa gak pernah sekalipun mikirin perasaan aku!",
             "パパ トゥ スラル ブギトゥ！（激高） ダリ ドゥル パパ ガッ プルナ スカリプン ミキリン プラサアン アク！",
             "Papa tuh の tuh に怒りを乗せ、mikirin perasaan aku で声の震えまで再現。"),
            ("【家族ドラマ・父親の説教】「お前のためを思って言ってるんだ！社会はそんなに甘くないんだぞ！」",
             "Papa ngomong begini demi kebaikan kamu sendiri! Kamu pikir cari uang di luar sana gampang?!",
             "パパ ンゴモン ブギニ デミ クバイカン カム スンディリ！ カム ピキル チャリ ウアン ディ ルアル サナ ガンパン？！",
             "重厚な父親のバリトンボイスを意識し、demi kebaikan kamu を厳格に響かせる。"),
            ("【オフィスドラマ・裏切り】「信じていたのに…まさか君が競合他社にデータを流していたなんて」",
             "Padahal saya percaya banget sama kamu... Gak nyangka, kamu tega jual data rahasia itu ke kompetitor.",
             "パダハル サヤ プルチャヤ バンゲッ サマ カム...（絶句） ガッ ニャンカ、カム トゥガ ジュアル データ ラハシア イトゥ ク コンペティトル。",
             "sama kamu... の後の1秒間の絶句（無音）の緊張感を完全に再現する。"),
            ("【オフィスドラマ・弁明】「違います、部長！罠なんです！私を陥れようとする誰かの仕業です！」",
             "Bukan begitu, Pak! Sumpah, ini semua jebakan! Ada orang yang sengaja mau jatuhin saya!",
             "ブカン ブギトゥ、パッ！（必死の弁明） スンパ、イニ スムア ジェバカン！ アダ オラン ヤン スンガジャ マウ ジャトゥヒン サヤ！",
             "Sumpah の s を強く吐き出し、jebakan の語末声門閉鎖をタイトに止める。"),
            ("【友情ドラマ・励まし】「大丈夫だよ。俺たちがついてるじゃん。何があってもお前は一人じゃない」",
             "Santai aja, bro. Kan ada kita-kita di sini. Apapun yang terjadi, lu gak bakal sendirian kok.",
             "サンタイ アジャ、ブロ。（肩を叩く間） カン アダ キタキタ ディ シニ。アパプン ヤン トゥルジャディ、ル ガッ バカル スンディリアン コッ。",
             "bro の後の温かいポーズ、kita-kita のリズミカルな連打を一体化させる。"),
            ("【ホラードラマ・恐怖】「しーっ！静かにして…あそこのドアの向こうに、誰か立ってる…」",
             "Ssst! Diem dulu sebentar... Di balik pintu itu, kayaknya ada orang yang lagi berdiri...",
             "ススト！（ささやき声） ディエム ドゥル スブンタル... ディ バリッ ピントゥ イトゥ、カヤッニャ アダ オラン ヤン ラギ ブルディリ...",
             "完全なささやき声（Whisper Voice）で、息遣いだけで緊迫感を表現する。"),
            ("【コメディドラマ・呆れ】「おいおい、また財布忘れたのかよ？これで今週3回目だぞ！」",
             "Aduh ampun deh! Lu ketinggalan dompet lagi?! Ini udah ketiga kalinya minggu ini, Bambang!",
             "アドゥ アンプン デッ！（手で頭を抱える） ル クティンガラン ドンペッ ラギ？！ イニ ウダ クティガ カリニャ ミング イニ、バンバン！",
             "Aduh ampun deh の大袈裟なジェスチャーと呆れ返ったトーンを同期。"),
            ("【刑事ドラマ・尋問】「白状しろ！事件の夜、8時にどこで誰といたんだ？！」",
             "Jawab yang jujur! Malam itu jam delapan, kamu lagi di mana dan sama siapa?!",
             "ジャワッ ヤン ジュジュル！（机を叩く勢い） マラム イトゥ ジャム ドゥラパン、カム ラギ ディ マナ ダン サマ シアパ？！",
             "Jawab の b を強く抑え込み、sama siapa?! で威嚇するように語尾を突き刺す。"),
            ("【感動ドラマ・感謝】「先生、先生に出会えなかったら、今の私はここにいませんでした」",
             "Ibu Guru... Kalau bukan karena bimbingan Ibu, saya gak akan pernah bisa sampai di titik ini.",
             "イブ グル...（涙ぐむ声） カロウ ブカン カルナ ビンビンガン イブ、サヤ ガカカン プルナ ビサ サンパイ ディ ティティッ イニ。",
             "涙声の微妙なかすれ（Vocal Fry）や息の震えまで完璧にトレースする。"),
            ("【日常ドラマ・噂話】「ねえねえ、聞いた？隣の部署の課長、今月で会社辞めるらしいよ！」",
             "Eh, lu udah denger belum? Katanya manajer divisi sebelah mau resign akhir bulan ini lho!",
             "エッ、ル ウダ デンゲル ブルム？（身を乗り出す） カタニャ マナジェル ディヴィシ スブラ マウ レサイン アキル ブラン イニ ロ！",
             "Eh の呼びかけの鋭さと、lho の噂話特有の弾むイントネーションを模倣。"),
            ("【カフェでの世間話】「本当にジャカルタの渋滞は頭がおかしくなりそうだよ、毎日2時間だよ？」",
             "Gila ya, macetnya Jakarta tuh bener-bener bikin stres! Masa tiap hari harus tua di jalan dua jam?",
             "ギラ ヤ、（深い溜め息） マチェッニャ ジャカルタ トゥ ブネルブネル ビキン ストレス！ マサ スティアッ ハリ ハルス トゥア ディ ジャラン ドゥア ジャム？",
             "Gila ya の後の首を振る仕草と、tua di jalan（道で歳をとる）の皮肉なユーモアを同期。"),
            ("【謝罪と和解】「ごめん、本当に私が悪かった。もう二度とあなたを傷つけないから」",
             "Maafin aku ya, aku bener-bener nyesel. Aku janji gak bakal bikin kamu kecewa lagi.",
             "マアフィン アク ヤ、アク ブネルブネル ニェセル。（目を合わせる） アク ジャンジ ガッ バカル ビキン カム クチェワ ラギ。",
             "nyesel の切実な後悔の響きを感情込めてオーバーラップ。"),
            ("【総仕上げ・フルシーン対話オーバーラッピング】「2人の登場人物の掛け合いを1人で交互に完璧同期」",
             "A: 'Kamu mau ke mana?!' / B: 'Bukan urusan kamu lagi!' / A: 'Tolong dengerin aku sekali ini aja!'",
             "A:「カム マウ ク マナ？！」 / B:「ブカン ウルサン カム ラギ！」 / A:「トロン ドゥンゲリン アク スカリ イニ アジャ！」",
             "AとBの全く異なる感情とキャラクターの声を、0ミリ秒のタイムラグで完コピする。")
        ],
        "quizzes": [
            ("「オーバーラッピング（Overlapping）」と「シャドーイング（Shadowing）」の根本的な違いは？",
             ["オーバーラッピングは音声を聞かずに文字だけを読むこと", "シャドーイングは0.5〜1秒遅れて追唱するが、オーバーラッピングは音声と完全に同時（0秒差）に重ねて発声すること", "オーバーラッピングは歌を歌うこと"],
             "シャドーイングは0.5〜1秒遅れて追唱するが、オーバーラッピングは音声と完全に同時（0秒差）に重ねて発声すること",
             "オーバーラッピングは音声と寸分違わず完全に同時に発声するため、タイミング、ポーズ、息遣いの完全な同期が要求されます。"),
            ("映画やドラマのセリフをオーバーラッピングする最大の学習効果は？",
             ["文字のスペルを覚えられること", "言葉の意味だけでなく、息遣い・間（ま）・表情・感情といった「身体性」ごとネイティブの会話力を獲得できること", "字幕の翻訳ミスを発見できること"],
             "言葉の意味だけでなく、息遣い・間（ま）・表情・感情といった「身体性」ごとネイティブの会話力を獲得できること",
             "言語のノンバーバル（非言語的）なプロソディや息のコントロールを身体で覚える究極の体得メソッドです。"),
            ("オーバーラッピングを成功させるための必須ステップは？",
             ["初めて聞く音声をいきなりぶっつけ本番で重ねる", "スクリプトの精読とリスニングを事前に行い、セリフの抑揚とポーズの場所を完全に頭に入れてから重ねる", "音声を消して字幕だけを見て話す"],
             "スクリプトの精読とリスニングを事前に行い、セリフの抑揚とポーズの場所を完全に頭に入れてから重ねる",
             "完全同期を達成するためには、セリフの内容、リズム、ポーズの位置を事前に把握しておく準備が必要です。")
        ]
    },
    {
        "id": "1198",
        "slug": "18-formal-news-broadcasting-cadence",
        "title": "【ニュース・アナウンスの格調高い発話】国家儀式・式典・報道番組のプロソディ",
        "desc": "国営放送（TVRI/RRI）のキャスターや国家式典の司会に見られる、格調高く威厳ある公的スピーチの韻律（Cadence）とポーズ法。",
        "theory": """### 1. 公的・格調高い発話（Bahasa Indonesia Formal / Baku）の美学
街角口語（Gaul）が「音の短縮・融合・脱落」を極めるのに対し、**国家儀式、式典司会（MC）、ニュース報道、学術スピーチで求められるのは「一音節も崩さない完全な正音（EYD 標準発音）」と「威厳あるリズム（Cadence: カデンツ）」**です。

インドネシアの公的スピーチは、独特の朗々とした節回し（リズム・ポーズ・ピッチ）を持ちます。

### 2. 公式スピーチの3大プロソディ規則
1. **厳格な音節分解と接辞の完全調音**:
   - 口語のように *meN-* や *-kan* を省略することは一切許されません。
   - *memberikan* [məm-bə-ri-kan], *keberlanjutan* [kə-bər-lan-dʒu-tan] を一音節ずつ端正に調音します。
2. **計算されたポーズ（Jeda: 息継ぎと沈黙の配置）**:
   - 主部（Subjek）、述部（Predikat）、補部（Keterangan）の境界に明確な0.5秒のポーズ（Jeda）を置き、聴衆に情報の構造を提示します。
   - 例: *Presiden Republik Indonesia / didampingi para menteri / telah meresmikan proyek Whoosh.*
3. **カデンツ（Cadence: 句末の荘重な下降音調）**:
   - 節の終わりではピッチを保ち（休止音調 ↗）、文末では重厚かつ威厳を持って深い下降音調（↘）で着地します。""",
        "drills": [
            ("【ニュース冒頭挨拶】「皆様、こんばんは。TVRI夜の報道番組をお伝えいたします」",
             "Selamat malam pemirsa, inilah Warta Malam TVRI edisi hari ini bersama saya.",
             "スラマッ マラム プミルサ、インイラ ワルタ マラム テヴェエルイ エディシ ハリ イニ ブルサマ サヤ。",
             "pemirsa の後に堂々たるポーズを置き、inilah Warta Malam を格調高く切り出す。"),
            ("【国家式典・開会】「ただいまより、インドネシア共和国独立記念式典を執り行います」",
             "Upacara Peringatan Hari Ulang Tahun Kemerdekaan Republik Indonesia, dimulai.",
             "ウパチャラ プリンガタン ハリ ウラン タフン クムルデカアン レプブリッ インドネシア、ディムライ。",
             "インドネシア共和国の威厳を込め、dimulai の前のポーズで全聴衆の耳を集中させる。"),
            ("【首脳会談報道】「両国の首脳は、二国間経済協力の強化について合意に達しました」",
             "Kedua kepala negara / telah menyepakati penguatan kerja sama bilateral / di bidang ekonomi.",
             "クドゥア クパラ ネガラ / トゥラ ムニェパカティ プングアタン クルジャ サマ ビラテラル / ディ ビダン エコノミ。",
             "スラッシュ（/）の場所で0.5秒の的確なポーズを置き、大統領スピーチの威厳を再現。"),
            ("【経済ニュース】「中央銀行は、インフレ抑制のため政策金利の維持を決定いたしました」",
             "Bank Indonesia / memutuskan untuk mempertahankan suku bunga acuan / demi stabilitas moneter.",
             "バン インドネシア / ムムトゥスカン ウントゥッ ムムプルタハンカン スク ブンガ アチュアン / デミ スタビリタス モネテル。",
             "Bank Indonesia の後に明確な間を作り、stabilitas moneter で低音着地。"),
            ("【交通開通報道】「ジャカルタ・バンドン高速鉄道は、本日より本格的な商業運行を開始いたします」",
             "Kereta Cepat Jakarta-Bandung / secara resmi / mulai beroperasi secara komersial / pada hari ini.",
             "クレタ チパッ ジャカルタ バンドン / スチャラ レスミ / ムライ ブルオペラシ スチャラ コメルシアル / パダ ハリ イニ。",
             "beroperasi secara komersial の外来語を滑らかかつ厳格に調音。"),
            ("【環境サミット】「地球温暖化の脅威に対処するため、国際社会の結束が求められています」",
             "Solidaritas komunitas internasional / sangat dibutuhkan / untuk mengatasi ancaman perubahan iklim global.",
             "ソリダリタス コムニタス インテルナシオナル / サンガッ ディブトゥカン / ウントゥッ ムンガタシ アンチャマン プルバハン イクリム グローバル。",
             "格調高い学術・政治語彙の母音を一つ一つクリアに響かせる。"),
            ("【追悼スピーチ】「故人の国家に対する偉大なる貢献に、心より敬意と哀悼の意を表します」",
             "Kami menyampaikan belasungkawa yang sedalam-dalamnya / atas dedikasi almarhum bagi bangsa dan negara.",
             "カミ ムニャンパイカン ブラスングカワ ヤン スダラムダラムニャ / アタス デディカシ アルマルフム バギ バンサ ダン ネガラ。",
             "深い敬意と哀悼を込め、トーンを低く厳粛に保って発声。"),
            ("【公式ウェルカム】「インドネシアへようこそ。皆様のご滞在が実り多きものとなりますよう」",
             "Selamat datang di Indonesia, semoga kunjungan Anda / membawa manfaat yang sebesar-besarnya.",
             "スラマッ ダタン ディ インドネシア、スモガ クンジュンガン アンダ / ムンバワ マンファアッ ヤン スブサルブサルニャ。",
             "温かみの中にも国家の気品を感じさせる堂々としたウェルカムスピーチ。"),
            ("【ニュース締めくくり】「以上、本日のニュースをお伝えいたしました。ご視聴ありがとうございました」",
             "Demikian Warta Malam edisi hari ini, terima kasih atas perhatian Anda, dan sampai jumpa.",
             "ドゥミキアン ワルタ マラム エディシ ハリ イニ、トゥリマ カシ アタス プルハティアン アンダ、ダン サンパイ ジュンパ。",
             "Demikian を格調高く切り落とし、sampai jumpa で爽やかに下降して締めくくる。"),
            ("【緊急災害速報】「気象庁は、沿岸部の住民に対し津波警報を発令いたしました」",
             "Badan Meteorologi / mengeluarkan peringatan dini tsunami / bagi masyarakat di pesisir pantai.",
             "バダン メテオロロギ / ムングルアルカン プリンガタン ディニ ツナミ / バギ マシャラカッ ディ プシシル パンタイ。",
             "緊迫感を保ちつつ、パニックを防ぐ冷静沈着なアナウンスメント・プロソディ。"),
            ("【議会・国会演説】「国民の福祉向上に向けた法案を、本日ここに提案いたします」",
             "Dengan ini, kami mengajukan rancangan undang-undang / demi meningkatkan kesejahteraan rakyat.",
             "ドゥンガン イニ、カミ ムンガジュカン ランチャンガン ウンダンウンダン / デミ ムニンカッカン クセジャフテラアン ラッヤッ。",
             "kesejahteraan rakyat の語幹・周囲辞を格調高く力強く響かせる。"),
            ("【学術シンポジウム】「研究結果から、AI技術が産業構造を根本から変革することが示されました」",
             "Hasil penelitian menunjukkan / bahwa kecerdasan buatan / akan merevolusi struktur industri secara fundamental.",
             "ハシル プネリティアン ムヌンジュッカン / バワ クチュルダサン ブアタン / アカン ムレヴォルシ ストルクトゥル インドゥストリ スチャラ フンダメンタル。",
             "学術的権威を支える無駄のない洗練されたプロソディ。"),
            ("【スポーツ実況・公式】「選手団の皆様の健闘と、フェアプレーの精神を期待いたします」",
             "Mari kita junjung tinggi sportivitas / dan semangat persaudaraan / dalam kompetisi ini.",
             "マリ キタ ジュンジュン ティンギ スポルティヴィタス / ダン スマンガッ プルスウダラアン / ダラム コンペティシ イニ。",
             "sportivitas と persaudaraan に情熱と規律を込めて朗々とアナウンス。"),
            ("【航空機内アナウンス】「当機はまもなくスカルノハッタ国際空港に着陸いたします」",
             "Para penumpang yang terhormat, pesawat kita / akan segera mendarat / di Bandara Internasional Soekarno-Hatta.",
             "パラ プヌンパン ヤン トゥルホルマッ、プサワッ キタ / アカン スゲラ ムンダラッ / ディ バンダラ インテルナシオナル スカルノ ハッタ。",
             "機内アナウンス特有の穏やかで洗練された語り口。"),
            ("【総仕上げ・大統領就任演説風】「多様性の中の統一を胸に、私たちは共に栄光ある未来へと歩みを進めます」",
             "Dengan semboyan Bhinneka Tunggal Ika, / marilah kita melangkah bersama / menuju masa depan Indonesia yang gemilang!",
             "ドゥンガン スンボヤン ビンネカ トゥンガル イカ、 / マリラ キタ ムランカ ブルサマ / ムヌジュ マサ ドゥパン インドネシア ヤン グミラン！",
             "国家の最高リーダーになりきり、歴史を動かす壮大なスケールと完璧な正音カデンツで読み切る。")
        ],
        "quizzes": [
            ("ニュース報道や国家式典（公的スピーチ）において、口語と最も対照的な発音の特徴は何か？",
             ["音を極端に短縮し、スラングを多用する", "接頭辞 meN- や語末子音を一音節も崩さず、EYD標準発音の正音で厳格に調音する", "早口でささやくように話す"],
             "接頭辞 meN- や語末子音を一音節も崩さず、EYD標準発音の正音で厳格に調音する",
             "公的スピーチ（Bahasa Baku）では、省略や音韻脱落を徹底的に排除し、正書法に則った完全な形態素を発声します。"),
            ("アナウンサーや式典司会が文中に意図的に配置する「Jeda（ポーズ）」の主目的は？",
             ["単に息が切れたから休むため", "文の構造（主部・述部・条件節）を明瞭にし、聴衆が情報を正確に理解できるようにするため", "時間を稼いで番組を長くするため"],
             "文の構造（主部・述部・条件節）を明瞭にし、聴衆が情報を正確に理解できるようにするため",
             "適切なポーズ（Jeda）は文法構造を可視化し、荘重な品格と分かりやすさを聴衆に提供します。"),
            ("公的スピーチの文末における音調（カデンツ: Cadence）の基本パターンは？",
             ["疑問文のように語尾を高く跳ね上げる", "平坦なまま音声をフェードアウトさせる", "重厚かつ威厳を持って深い下降音調（↘）で確実に着地する"],
             "重厚かつ威厳を持って深い下降音調（↘）で確実に着地する",
             "文の完結性と国家・組織としての決定事項の重みを示すため、威厳ある下降調（Falling Cadence）で着地します。")
        ]
    },
    {
        "id": "1199",
        "slug": "19-interpreter-simultaneous-shadowing",
        "title": "【通訳者の先取りシャドーイング】2秒遅れで追唱しながら意味を把握する高度訓練",
        "desc": "プロの同時通訳者が養成訓練で実践する「ラギング・シャドーイング（Lag Shadowing）」。音韻模倣と意味理解を完全両立させる究極の認知的負荷トレーニング。",
        "theory": """### 1. 「ラギング・シャドーイング（Lag Shadowing）」とは？
初心者のシャドーイングは「音を真似るだけで精一杯で、意味が全く頭に入っていない」状態に陥りがちです。

プロの同時通訳者が行う**「ラギング・シャドーイング（タイムラグ追唱）」は、スピーカーから意図的に「2〜3秒（1〜2文節）」遅れて発声**します。
この時、脳の中では以下の2つの猛烈な認知的処理が並行して実行されます。
1. **耳からの新しい音声情報の知覚とワーキングメモリへの保持（Input Buffer）**。
2. **2秒前に記憶した音声の調音運動の実行 ＋ その意味内容の瞬時イメージ化（Output Execution & Conceptualization）**。

### 2. 認知的二重負荷（Cognitive Dual-Task）の克服法
- **ステップ1: キーワードの視覚化（Mental Imagery）**:
  - 音声を追唱しながら、単語を「日本語の文字」ではなく「映像・情景・コンセプト」として脳裏に描く。
- **ステップ2: 予測（Anticipation）能力の覚醒**:
  - 主語と動詞が聞こえた瞬間に、次にどのような前置詞や目的語が来るかを先回りして推測する。
- **ステップ3: カウント・バック（数字引き算）との併用**:
  - 超上級者は、シャドーイングをしながら指で100から3ずつ引いていくなど、音韻自動化が本物かどうかをテストします。""",
        "drills": [
            ("【2秒遅れ追唱・基礎】「インドネシア政府は、新首都ヌサンタラの建設を加速させています」",
             "Pemerintah Indonesia sedang mempercepat pembangunan Ibu Kota Nusantara di Kalimantan Timur.",
             "プムリンタ インドネシア スダン ムムプルチパッ プンバングナン イブ コタ ヌサンタラ ディ カリマンタン ティムール。",
             "音声が mempercepat まで進んだところで Pemerintah Indonesia と発声を開始する。"),
            ("【2秒遅れ追唱・基礎】「このプロジェクトは、ジャワ島への一極集中を是正することを目的としています」",
             "Proyek ini bertujuan untuk mengatasi kesenjangan ekonomi dan mengurangi beban Pulau Jawa.",
             "プロイェッ イニ ブルトゥジュアン ウントゥッ ムンガタシ クスンジャンガン エコノミ ダン ムングランギ ブバン プラウ ジャワ。",
             "音声から常に2〜3単語遅れをキープし、遅れの距離を一定に保つ。"),
            ("【イメージ化トレーニング】「緑豊かな熱帯雨林の中に、スマートで持続可能な都市が誕生します」",
             "Sebuah kota pintar dan berkelanjutan akan lahir di tengah hutan hujan tropis yang asri.",
             "スブア コタ ピンタル ダン ブルクランジュタン アカン ラヒル ディ トゥンガ フタン フジャン トロピス ヤン アスリ。",
             "発声しながら、頭の中に「緑の森の中に建つ近代都市」の映像を鮮明にイメージする。"),
            ("【複文のラギング】「海外からの投資を呼び込むため、様々な税制優遇措置が用意されています」",
             "Guna menarik minat investor asing, berbagai insentif perpajakan telah disiapkan secara matang.",
             "グナ ムナリッ ミナッ インヴェストル アシン、ブルバガイ インセンティフ プルパジャカン トゥラ ディシヤプカン スチャラ マタン。",
             "Guna menarik で目的を予測し、主節の insentif を遅れて追唱する。"),
            ("【国際会議スピーチ】「本日のシンポジウムにご参加いただいた皆様に、心より感謝申し上げます」",
             "Saya ingin menyampaikan apresiasi setinggi-tingginya kepada seluruh peserta simposium hari ini.",
             "サヤ インギン ムニャンパイカン アプレシアシ スティンギティンギニャ クパダ スルルフ プスルタ シンポジウム ハリ イニ。",
             "apresiasi setinggi-tingginya の定型チャンクを頭のメモリにプールしながら追う。"),
            ("【数値データの処理】「昨年の貿易額は前年比15%増加し、過去最高を記録しました」",
             "Nilai perdagangan tahun lalu meningkat sebesar lima belas persen, mencatat rekor tertinggi.",
             "ニライ プルダガンガン タフン ラル ムニンカッ スブサル リマ ブラス プルセン、ムンチャタッ レコル トゥルティンギ。",
             "数字（lima belas persen）を聞き逃さずにメモリに保持し、正確に遅れて発声。"),
            ("【外交交渉の文脈】「双方は、地域平和と安定の維持に向けた協力を再確認いたしました」",
             "Kedua belah pihak menegaskan kembali komitmen bersama untuk menjaga perdamaian kawasan.",
             "クドゥア ブラッ ピハッ ムヌガスカン クンバリ コミットメン ブルサマ ウントゥッ メンジャガ プルダマイアン カワサン。",
             "外交辞令の格調高い表現を2単語遅れで噛まずに追唱。"),
            ("【技術トレンド】「人工知能の急速な発展は、労働市場に大きな地殻変動をもたらしています」",
             "Pesatnya perkembangan kecerdasan buatan membawa pergeseran besar dalam pasar tenaga kerja.",
             "プサッニャ プルクンバンガン クチュルダサン ブアタン ムンバワ プルゲセラン ブサール ダラム パサル トゥナガ クルジャ。",
             "pergeseran besar（大きな地殻変動）の概念を頭で把握しながら口を動かす。"),
            ("【医療・公衆衛生】「予防接種プログラムの普及により、感染症の発生率は劇的に低下しました」",
             "Berkat perluasan program vaksinasi, tingkat penularan penyakit menurun secara drastis.",
             "ブルカッ プルルアサン プログラム ヴァクシナシ、ティンカッ プヌララン プニャキッ ムヌルン スチャラ ドラスティス。",
             "Berkat... menurun（〜のおかげで低下した）の因果関係を把握する。"),
            ("【環境・エネルギー】「再生可能エネルギーへの移行は、もはや待ったなしの世界的課題です」",
             "Transisi menuju energi baru dan terbarukan kini menjadi agenda global yang sangat mendesak.",
             "トランシシ ムヌジュ エネルギ バル ダン トゥルバルカン キニ ムンジャディ アゲンダ グローバル ヤン サンガッ ムンデサッ。",
             "mendesak（緊急の）の危機感を共有しながら追唱。"),
            ("【3秒遅れ・高負荷】「長文を3秒遅れでキープしながら、意味の要約を意識する」",
             "Meskipun tantangan yang dihadapi sangat kompleks, semangat kolaborasi antarnegara tetap menjadi kunci utama.",
             "ムスキプン タンタンガン ヤン ディハダピ サンガッ コンプレクス、スマンガッ コラボラシ アンタルネガラ トゥタップ ムンジャディ クンチ ウタマ。",
             "Meskipun（譲歩）の節が終わる頃に発声を開始し、主節の結論までメモリを保持する。"),
            ("【通訳者特訓・脱落防止】「固有名詞と年号が連続する文章の先取り」",
             "Pada tahun 1945, para pendiri bangsa merumuskan Pancasila sebagai dasar negara Indonesia.",
             "パダ タフン セリブ スンビラン ラトゥス エンパッ プルフ リマ、パラ プンディリ バンサ ムルムスカン パンチャシラ スバガイ ダサル ネガラ インドネシア。",
             "年号（1945）と固有名詞（Pancasila）を確実にワーキングメモリに格納。"),
            ("【通訳者特訓・話者の感情追従】「失望から決意へ変化するスピーチの追唱」",
             "Kita tidak boleh menyerah sekarang, kegagalan ini harus menjadi cambuk untuk bangkit lebih kuat.",
             "キタ ティダッ ボレ ムニェラ スカラン、クガガラン イニ ハルス ムンジャディ チャムブッ ウントゥッ バンキッ ルビ クアッ。",
             "話者の感情の起伏を2秒遅れでそのまま声に乗せる。"),
            ("【通訳者特訓・即時要約】「聞きながら要点を日本語で一言でまとめる訓練」",
             "Efisiensi logistik maritim menjadi prioritas utama demi menurunkan disparitas harga antarwilayah.",
             "エフィシエンシ ロギスティッ マリティム ムンジャディ プオリタス ウタマ デミ ムヌルンカン ディスパリタス ハルガ アンタルウィラヤ。",
             "追唱終了直後に「海洋物流の効率化による地域格差是正」と即座に日本語で要約できるか確認。"),
            ("【総合・プロ通訳実戦演習】「3分間の基調講演をノンストップ・ラギング追唱」",
             "Perubahan iklim, revolusi digital, dan dinamika geopolitik menuntut kepemimpinan global yang adaptif dan inklusif.",
             "プルバハン イクリム、レヴォルシ ディジタール、ダン ディナミカ ゲオポリティッ ムヌントゥッ クプミンピナン グローバル ヤン アダプティフ ダン インクルシフ。",
             "3秒のタイムラグを完全に維持したまま、意味を100%把握して最後まで完走する。")
        ],
        "quizzes": [
            ("プロの通訳者が実践する「ラギング・シャドーイング（Lag Shadowing）」の最大の特徴は？",
             ["音声を1音節も遅れずに完全に同時に発音する", "音声から意図的に2〜3秒（1〜2文節）遅れて追唱し、ワーキングメモリと意味理解を同時稼働させる", "音声を録音して翌日聞くこと"],
             "音声から意図的に2〜3秒（1〜2文節）遅れて追唱し、ワーキングメモリと意味理解を同時稼働させる",
             "耳からの新規インプット保持と、少し前の記憶のアウトプットを同時並行で行うことで、認知的マルチタスク能力を鍛えます。"),
            ("シャドーイング中に「音の真似だけで意味が頭に入らない」状態を打破するコツは？",
             ["日本語の字幕を全画面に表示する", "言葉を逐語訳するのではなく、情景やコンセプトを映像として脳裏に描く（Mental Imagery）", "目を閉じて何も考えないようにする"],
             "言葉を逐語訳するのではなく、情景やコンセプトを映像として脳裏に描く（Mental Imagery）",
             "翻訳を介さず「言葉 → 情景イメージ」へ直結させることで、ワーキングメモリの消費を抑えながら意味理解を両立できます。"),
            ("ラギング・シャドーイング中に主語と動詞が聞こえた瞬間に通訳者が無意識に行っている認知活動は？",
             ["次にどのような前置詞、目的語、結論が来るかを先回りして推測する（Anticipation）", "昨日食べた夕食のことを思い出す", "スマートフォンの通知をチェックする"],
             "次にどのような前置詞、目的語、結論が来るかを先回りして推測する（Anticipation）",
             "高度な言語処理では、文脈と文法規則から後続の展開を予測（Anticipation）することで、脳の負荷を劇的に軽減しています。")
        ]
    },
    {
        "id": "1200",
        "slug": "20-phonology-mastery-diagnostic",
        "title": "【音韻総合診断テスト】発音・アクセント・イントネーションの総合実力測定20番勝負",
        "desc": "セクション29の全20テーマを集大成した音韻実力測定テスト。母音・子音・強勢・抑揚・脱落・プロソディの弱点を完全にあぶり出す20問。",
        "theory": """### 1. セクション29「音韻・発音・シャドーイング特訓」の総括
本セクションでは、全20記事を通じて日本人学習者が直面する音韻の壁を科学的に解剖し、調音筋肉を鍛え上げてきました。
- **基礎編（1181〜1190）**: シャドーイング原理、母音e（テーリング vs プルペッ）、巻き舌r、語末k声門閉鎖、鼻音ng/ny、二重母音・滑音、リンキング、後から2番目の音節アクセント、ピッチイントネーション、脱カタカナ発音。
- **応用編（1191〜1200）**: 弱音化・音韻脱落、外来語借用音韻、AI音声認識対策、早口言葉、速度可変プロソディ、感情ピッチ、ドラマ対話オーバーラッピング、報道カデンツ、通訳ラギングシャドーイング。

### 2. 総合診断テストの受検プロトコル
本記事の20問診断テストでは、各問題に「**音韻ターゲット**」が設定されています。
以下の手順でセルフ診断を行ってください。
1. **録音の準備**: スマートフォンのボイスメモや録音アプリを起動する。
2. **初見発声**: スクリプトを見ながら、自然なスピードで1回で録音する。
3. **客観的評価**: 録音を聞き返し、解説のチェックポイント（母音の質、子音の閉鎖、ピッチの抑揚）と照合して合否を判定する。""",
        "drills": [
            ("【第1問: 母音 e の識別】「朝礼（apel [e]）で美味しいリンゴ（apel [ə]）の話を聞いた」",
             "Saat apel pagi di kantor, pimpinan membagikan buah apel segar.",
             "サアッ アペル パギ ディ カントル、ピンピナン ムンバギカン ブア アプル スガル。",
             "apel [e]（テーリング）と apel [ə]（プルペッ）の口の形と緊張感を完璧に区別できているか。"),
            ("【第2問: 巻き舌 r のふるえ音】「家（rumah）が壊れて（rusak）、修理（reparasi）する」",
             "Rumah tua itu rusak parah dan membutuhkan reparasi segera.",
             "ルマ トゥア イトゥ ルサッ パラ ダン ムンブトゥカン レパラシ スゲラ。",
             "語頭の r（rumah, rusak, reparasi）で舌先を2〜3回しっかり振動させられているか。"),
            ("【第3問: 語末 k の声門閉鎖】「お父さん（Bapak）、このスープ（bakso）はちっとも辛くありません（tidak）」",
             "Bapak, bakso hangat ini rasanya enak dan tidak terlalu pedas.",
             "バパッ、バッソ ハンガッ イニ ラサニャ エナッ ダン ティダッ トゥルラル プダス。",
             "Bapak, bakso, enak, tidak の語末で「ク」と母音を出さず、喉をピタッと閉鎖して音を止められているか。"),
            ("【第4問: 語頭鼻音 ng】「昨夜遅くまで起きていたので、すごく眠い（ngantuk）」",
             "Saya sangat ngantuk karena semalam menonton film sampai larut.",
             "サヤ サンガッ ンガントゥッ カルナ スマラム ムノントン フィルム サンパイ ラルッ。",
             "ngantuk の頭を「ガ」と破裂させず、鼻腔共鳴「ンガ」で滑らかに立ち上げられているか。"),
            ("【第5問: 硬口蓋鼻音 ny】「部屋に蚊（nyamuk）が多くて、快適（nyaman）に眠れない」",
             "Banyak nyamuk di kamar ini sehingga saya tidak bisa tidur dengan nyaman.",
             "バニャッ ニャムッ ディ カマル イニ スヒンガ サヤ ティダッ ビサ ティドゥル ドゥンガン ニャマン。",
             "nyamuk, banyak, nyaman で舌の中央を上あごに広く押し当てて調音できているか。"),
            ("【第6問: 二重母音 vs 母音連続】「浜辺でリラックス（santai）したい（mau）」",
             "Kalau ada waktu senggang, saya mau duduk santai di pantai.",
             "カラウ アダ ワクトゥ スンガン、サヤ マウ ドゥドゥッ サンタイ ディ パンタイ。",
             "santai, pantai（二重母音・1拍）と mau（母音連続・2拍）のリズム差を再現できているか。"),
            ("【第7問: リンキング（連音）】「何もないよ、ヒヨコ（anak ayam）がいただけで（tidak ada apa-apa）」",
             "Tidak ada apa-apa kok, cuma seekor anak ayam yang lewat.",
             "ティダカダ アパパ コッ、チュマ スエコル アナカヤム ヤン ルワッ。",
             "tidak ada [ti-da-ka-da]、anak ayam [a-na-ka-yam] の単語境界が滑らかに結合しているか。"),
            ("【第8問: アクセント移動】「開ける（buka）→ 開けてあげる（bukakan）」",
             "Tolong buka pintu itu, lalu bukakan juga pintu gerbangnya.",
             "トロン ブカ ピントゥ イトゥ、ラル ブカカン ジュガ ピントゥ グルバンニャ。",
             "buka（BU-ka）から bukakan（bu-KA-kan）へと強勢が後ろへシフトしているか。"),
            ("【第9問: 疑問詞疑問文の抑揚】「いつ（kapan）そのプロジェクトは始まりますか？」",
             "Kapan proyek renovasi gedung ini akan dimulai?",
             "カパン（高） プロイェッ レノヴァシ グドゥン イニ アカン ディムライ（下降 ↘）？",
             "Kapan を最も高く際立たせ、文末に向かって滑らかに下降調（Falling）で着地しているか。"),
            ("【第10問: Yes/No疑問文の抑揚】「明日の朝礼に出席されますか？」",
             "Apakah Bapak akan hadir dalam apel pagi besok?",
             "アパカ バパッ アカン ハディル ダラム アペル パギ ベソッ？ ↗",
             "文末の besok をキュッと高めのピッチ（Rising）に跳ね上げて疑問を示せているか。"),
            ("【第11問: 脱カタカナ発音】「ホテル（hotel）の近くの銀行（bank）で実践的な（praktis）話をする」",
             "Di dekat hotel, kami membahas strategi praktis di bank.",
             "ディ ドゥカッ ホテル、カミ ムンバハス ストラテギ プラクティス ディ バンク。",
             "hotel, bank, praktis, strategi の子音に余計な母音「u」「o」を挿入していないか。"),
            ("【第12問: 語頭音脱落】「もうご飯食べたよ（'dah makan）、知ってるよ（'dah tau）」",
             "Gue 'dah makan dan 'dah tau masalah itu dari kemarin.",
             "グエ ダー マカン ダン ダー タウ マサラ イトゥ ダリ クマリン。",
             "sudah → 'dah, tahu → tau と日常口語の音韻脱落を淀みなく操れているか。"),
            ("【第13問: オランダ語借用】「車のマフラー（knalpot）を修理工場（bengkel）に持っていく」",
             "Knalpot mobil ini patah dan harus dibawa ke bengkel resmi.",
             "クナルポッ モビル イニ パタ ダン ハルス ディバワ ク ベンケル レスミ。",
             "knalpot の kn- 結合、語末 t 閉鎖、bengkel の l 閉鎖が正確か。"),
            ("【第14問: アラビア語借用】「どんな時代（zaman）でも感謝（bersyukur）の気持ちを忘れない」",
             "Dalam zaman apa pun, kita harus selalu bersyukur kepada Tuhan.",
             "ダラム ザマン アパ プン、キタ ハルス スラル ブルシュクル クパダ トゥハン。",
             "zaman の [z] と bersyukur の [ʃ]（sy）を正しく調音できているか。"),
            ("【第15問: AI音声認識対策】「明日の朝7時にアラームを設定して」",
             "Setel alarm untuk besok pagi pada jam tujuh tepat.",
             "セテル アラルム ウントゥッ ベソッ パギ パダ ジャム トゥジュ トゥパッ。",
             "スマホの音声入力（Siri / Google）に向かって話し、1文字も誤変換されずに入力されるか。"),
            ("【第16問: 早口言葉の俊敏性】「Kuku kaki kakek-kakekku kaku-kaku」",
             "Kuku kaki kakek-kakekku kaku-kaku.",
             "クク カキ カケッカケック カクカク。",
             "舌をもつれさせずに、等間隔のハイテンポで3回連続発声できるか。"),
            ("【第17問: 早口言葉の l/r 交代】「Ular melingkar-lingkar di atas pagar bundar」",
             "Ular melingkar-lingkar di atas pagar bundar.",
             "ウラル ムリンカルリンカル ディ アタス パガル ブンダル。",
             "u-lar, me-ling-kar, pa-gar, bun-dar の l と r を混同せずに弾き分けられるか。"),
            ("【第18問: 感情プロソディ（怒り）】「ふざけるな！何度言ったらわかるんだ！」",
             "Jangan main-main ya! Sudah berapa kali saya bilang sama kamu?!",
             "ジャンガン マインマイン ヤ！（重低音・鋭いスタッカート） スダ ブラパ カリ サヤ ビラン サマ カム？！",
             "低いピッチと硬い筋肉の緊張を声に乗せ、迫力ある怒りの音調を表現できているか。"),
            ("【第19問: 公式報道カデンツ】「両国の首脳は、二国間協力の強化について合意に達しました」",
             "Kedua kepala negara / telah menyepakati penguatan kerja sama bilateral / di bidang ekonomi.",
             "クドゥア クパラ ネガラ / トゥラ ムニェパカティ プングアタン クルジャ サマ ビラテラル / ディ ビダン エコノミ。",
             "計算されたポーズ（Jeda）と、文末の威厳ある重厚な下降音調（Cadence）を再現できているか。"),
            ("【第20問: 先取りラギング追唱】「2秒遅れで追唱しながら意味を100%把握する」",
             "Transisi energi baru dan terbarukan / kini menjadi agenda global yang sangat mendesak / demi masa depan bumi.",
             "トランシシ エネルギ バル ダン トゥルバルカン / キニ ムンジャディ アゲンダ グローバル ヤン サンガッ ムンデサッ / デミ マサ ドゥパン ブミ。",
             "音声から意図的に2秒遅れて追唱し、かつ「地球の未来に向けたエネルギー転換の緊急性」を脳裏で鮮明に把握できているか。")
        ],
        "quizzes": [
            ("音韻診断テストで「Tidak ada apa-apa」を発音した際、最も高得点となる調音は？",
             ["「ティダック・アダ・アパ・アパ」と4つの単語を完全に区切る", "「ティダカダ・アパパ [ti-da-ka-da-pa-pa]」と連音化して滑らかに一息で繋ぐ", "「ティダ・アパ」と短縮する"],
             "「ティダカダ・アパパ [ti-da-ka-da-pa-pa]」と連音化して滑らかに一息で繋ぐ",
             "語末子音と語頭母音の自然なリンキング（連音）は、ネイティブ特有の流暢なリズムの決定的証拠です。"),
            ("「Kapan Anda berangkat?（いつ出発しますか？）」の正しい文末イントネーションは？",
             ["Yes/No 疑問文のように語尾を高く跳ね上げる（Rising）", "疑問詞 Kapan を最も高く発音し、文末に向かって下降する（Falling）", "平坦な音程を維持する"],
             "疑問詞 Kapan を最も高く発音し、文末に向かって下降する（Falling）",
             "5W1H の疑問詞疑問文は疑問詞がフォーカスされるため、文末は平叙文と同様に下降調（Falling）となります。"),
            ("シャドーイングや発音特訓の成果を長期的に維持するための最も効果的な習慣は？",
             ["週に1回だけ5時間猛特訓する", "毎日5〜10分間、スマホの録音アプリやAI音声認識を使って自分の声を客観的にフィードバックする", "声を出さずに参考書を黙読する"],
             "毎日5〜10分間、スマホの録音アプリやAI音声認識を使って自分の声を客観的にフィードバックする",
             "調音運動は筋肉トレーニングであるため、毎日の短時間反復と客観的録音チェックの習慣化が最も確実に脳と筋肉に定着します。")
        ]
    }
]

output_dir = "docs/phonology"
os.makedirs(output_dir, exist_ok=True)

for art in articles:
    filename = f"{art['slug']}.md"
    filepath = os.path.join(output_dir, filename)
    
    lines = []
    lines.append(f"# {art['title']}")
    lines.append("")
    lines.append(f"> [!NOTE]")
    lines.append(f"> **本記事のねらい**: {art['desc']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. 音韻理論と科学的メカニズム")
    lines.append("")
    lines.append(art["theory"])
    lines.append("")
    lines.append("---")
    lines.append("")
    drill_count = len(art["drills"])
    lines.append(f"## 2. 実践調音・シャドーイング集中ドリル{drill_count}選")
    lines.append("")
    lines.append("以下の例文を、解説の発音ポイントを意識しながら、**音声知覚から調音運動へ直結させる反復シャドーイング（3〜5回）**を行ってください。")
    lines.append("")
    
    for idx, drill in enumerate(art["drills"], 1):
        prompt, indon, kana, tips = drill
        m = re.match(r'^(【.+?】)(.+?)$', prompt)
        if m:
            tag = m.group(1)
            jp = m.group(2)
            header_prompt = f"{tag}「**{jp}**」"
        else:
            header_prompt = f"「**{prompt}**」"
            
        lines.append(f"### 第{idx}問: {header_prompt}")
        lines.append("")
        lines.append('<div class="id-example">')
        lines.append("")
        lines.append(f"**インドネシア語正音**: `{indon}`")
        lines.append("")
        lines.append(f"**カタカナ調音ガイド**: `{kana}`")
        lines.append("")
        lines.append(f"**調音・プロソディの極意**: {tips}")
        lines.append("")
        lines.append("</div>")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## 3. 理解度チェッククイズ")
    lines.append("")
    lines.append("本記事で学んだ音韻知識と調音運動の理解度を確認しましょう。")
    lines.append("")
    
    for q_idx, quiz in enumerate(art["quizzes"], 1):
        q_text, options, correct, explanation = quiz
        lines.append(f"### クイズ第{q_idx}問: {q_text}")
        lines.append("")
        for opt in options:
            lines.append(f"- [ ] {opt}")
        lines.append("")
        lines.append("<details>")
        lines.append(f"<summary>正解と解説を確認する</summary>")
        lines.append("")
        # Safe bracket formatting in correct answer:
        m_ans = re.match(r'^(「.+?」)(.+?)$', correct)
        if m_ans:
            c_tag = m_ans.group(1)
            c_rest = m_ans.group(2)
            lines.append(f"**正解**: {c_tag}**{c_rest}**")
        else:
            lines.append(f"**正解**: **{correct}**")
        lines.append("")
        lines.append(f"**解説**: {explanation}")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## 4. 学習のまとめと次へのステップ")
    lines.append("")
    lines.append("音韻の習得は「頭で理解すること」以上に、「**調音器官（舌・唇・声帯・鼻腔）の筋肉トレーニング**」です。")
    lines.append("スマートフォンの録音機能を使って自分の発声を録音し、ネイティブの模範音声と聞き比べることで、音韻の歪みを客観的に修正していきましょう。")
    lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated {filepath}")

print("All 10 articles written successfully.")
