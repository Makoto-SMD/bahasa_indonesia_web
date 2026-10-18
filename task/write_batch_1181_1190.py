# -*- coding: utf-8 -*-
import os
import re

articles = [
    {
        "id": "1181",
        "slug": "01-shadowing-mastery-guide",
        "title": "インドネシア語シャドーイング完全マニュアル：耳と口を直結させる科学的訓練法",
        "desc": "音声知覚と調音運動を直結させ、ネイティブのスピード・イントネーション・リズムを脳と筋肉に刷り込む科学的シャドーイング訓練法の全貌。",
        "theory": """### 1. なぜシャドーイングがインドネシア語習得に不可欠なのか？
第二言語習得論（SLA）において、リスニングとスピーキングは別個の能力ではなく、**「音声知覚（Phonological Decoding）」と「調音運動（Articulatory Execution）」が高度に同期した単一のループ（音韻ループ: Phonological Loop）**として機能します。

日本人がインドネシア語を話す際、「頭の中で作文してから口に出す」プロセスを踏んでいると、会話のスピードに追いつけません。シャドーイングは、流れてくる音声を1〜2音節遅れて影（シャドー）のように追いかけて発声することで、**意味理解の介在を一時的にバイパスし、調音器官（舌・唇・声帯）の筋肉に直接インドネシア語特有のプロソディ（韻律・リズム・抑揚）を自動化**させます。

### 2. 科学的4ステップ・シャドーイング訓練法
1. **ステップ1: リスニング（音の知覚と音素の特定）**:
   - スクリプトを見ずに音声を集中して聴き、音の強弱、息継ぎの場所、単語の連結（リンキング）を把握する。
2. **ステップ2: マンブリング（口パク・微小発声）**:
   - 音声に合わせて、口の中でつぶやくようにボソボソと音を真似る。調音器官の準備運動。
3. **ステップ3: パラレルリーディング（テキストを目で追いながらの同期発声）**:
   - スクリプトを見ながら、音声と全く同じスピード・イントネーションで同時に発音する。スペルと発音の乖離を埋める。
4. **ステップ4: フルシャドーイング（スクリプトなし・完全追唱）**:
   - スクリプトを見ずに、耳から入る音だけを頼りに0.5〜1秒遅れで忠実に発声する。感情やジェスチャーも模倣する。""",
        "drills": [
            ("【基礎・挨拶】「こんにちは、お元気ですか？お会いできて嬉しいです」",
             "Halo, apa kabar? Senang sekali bisa bertemu dengan Anda.",
             "ハロー、アパ カバール？ スナン スカリ ビサ ブルトゥム ドゥンガン アンダ。",
             "語末の r（kabar）を軽く震わせ、senang sekali のリズムを弾ませて発声する。"),
            ("【基礎・自己紹介】「私は東京から来た田中です。ジャカルタに住んで3ヶ月になります」",
             "Saya Tanaka dari Tokyo. Saya sudah tinggal di Jakarta selama tiga bulan.",
             "サヤ タナカ ダリ トーキョー。サヤ スダ ティンガル ディ ジャカルタ スラマ ティガ ブラン。",
             "dari Tokyo と di Jakarta の前置詞で音を途切れさせず、一息で滑らかに流す。"),
            ("【基礎・感謝】「温かいおもてなしをいただき、心より感謝申し上げます」",
             "Terima kasih banyak atas sambutan hangat yang diberikan.",
             "トゥリマ カシ バニャッ アタス サンブタン ハンガッ ヤン ディブルィカン。",
             "hangat と diberikan の語末子音 t, n を明瞭に止め、母音を勝手に付け足さない。"),
            ("【日常・注文】「アイスコーヒーを甘さ控えめで、持ち帰りでお願いします」",
             "Tolong es kopi susu, gulanya sedikit saja, dibungkus ya.",
             "トロン エス コピ スス、グラニャ スディキッ サジャ、ディブンクス ヤ。",
             "dibungkus ya の語尾に親しみやすい上昇調のニュアンスを込める。"),
            ("【日常・買い物】「このバティックのシャツを試着してもよろしいですか？」",
             "Boleh saya coba kemeja batik ini di kamar pas?",
             "ボレ サヤ チョバ クメジャ バティッ イニ ディ カマル パス？",
             "boleh saya coba を一息で発音し、ini の後でわずかに息を整える。"),
            ("【日常・タクシー】「次の交差点を右に曲がって、ガソリンスタンドの前で止めてください」",
             "Tolong belok kanan di perempatan depan, lalu berhenti di depan pom bensin.",
             "トロン ベロッ カナン ディ プルンパタン ドゥパン、ラル ブルヘンティ ディ ドゥパン ポム ベンシン。",
             "perempatan のアクセントは pa（後ろから2番目）に置く。"),
            ("【ビジネス・挨拶】「本日の会議にご参加いただき、誠にありがとうございます」",
             "Terima kasih atas kehadiran Bapak dan Ibu dalam rapat hari ini.",
             "トゥリマ カシ アタス クハディラン バパッ ダン イブ ダラム ラパッ ハリ イニ。",
             "Bapak dan Ibu は敬意を込めてクリアに調音し、rapat の t は声門閉鎖で止める。"),
            ("【ビジネス・進捗】「プロジェクトの進捗は計画通り順調に進んでおります」",
             "Kemajuan proyek berjalan dengan lancar sesuai dengan rencana awal.",
             "クマジュアン プロイェッ ブルジャラン ドゥンガン ランチャル ススアイ ドゥンガン レンチャナ アワル。",
             "lancar の r をしっかり響かせ、sesuai dengan で音を滑らかに繋ぐ。"),
            ("【ビジネス・質問】「この提案について、皆様のご意見をお聞かせいただけますか？」",
             "Apakah ada tanggapan atau masukan terkait proposal ini?",
             "アパカ アダ タンガパン アタウ マスカン トゥルカイッ プロポサル イニ？",
             "tanggapan の ng と proposal の l を正確に調音する。"),
            ("【感情・共感】「そのお気持ち、本当によく分かります。大変でしたね」",
             "Saya sangat mengerti perasaan Anda. Pasti berat sekali ya.",
             "サヤ サンガッ ムンゲルティ プラサアン アンダ。パスティ ブルアッ スカリ ヤ。",
             "perasaan の double a を長めに維持し、pasti berat sekali に感情を込める。"),
            ("【感情・驚き】「まさかそんなことが起きるなんて、信じられません！」",
             "Wah, tidak disangka hal seperti itu bisa terjadi!",
             "ワァ、ティダッ ディサンカ ハル スプルティ イトゥ ビサ トゥルジャディ！",
             "Wah でピッチを一気に上げ、bisa terjadi で落ち着かせる。"),
            ("【長文・説明】「インドネシアは多様な民族と文化が共生する魅力的な国です」",
             "Indonesia adalah negara kepulauan yang kaya akan keragaman budaya dan suku bangsa.",
             "インドネシア アダラ ネガラ クプラウアン ヤン カヤ アカン クラガマン ブダヤ ダン スク バンサ。",
             "negara kepulauan の母音連続を淀みなく発音する。"),
            ("【長文・意見】「相互理解を深めるためには、相手の文化を尊重する姿勢が何より重要です」",
             "Untuk mempererat saling pengertian, sikap menghormati budaya lain adalah kunci utama.",
             "ウントゥッ ムムプルエラッ サリン プンゲルティアン、シカッ ムンホルマティ ブダヤ ライン アダラ クンチ ウタマ。",
             "mempererat の二重 r を力強く震わせる。"),
            ("【長文・交渉】「双方にとって最適な解決策を見出すため、柔軟に議論を重ねましょう」",
             "Mari kita berdiskusi secara terbuka agar dapat menemukan solusi terbaik bagi kedua belah pihak.",
             "マリ キタ ブルディスクシ スチャラ トゥルブカ アガル ダパッ ムヌムカン ソルシ トゥルバイッ バギ クドゥア ブラッ ピハッ。",
             "berdiskusi secara terbuka をリズムに乗せて軽やかに発声する。"),
            ("【総合・総仕上げ】「言葉を学ぶことは、新しい世界への扉を開く素晴らしい冒険です」",
             "Belajar bahasa baru bukan hanya menghafal kata, tetapi juga membuka jendela menuju dunia baru.",
             "ブラジャル バハサ バル ブカン ハニャ ムンハファル カタ、トゥタピ ジュガ ムンブカ ジェンデラ ムヌジュ ドゥニア バル。",
             "but... also（bukan hanya... tetapi juga）の対比リズムを意識して完璧にシャドーイングする。")
        ],
        "quizzes": [
            ("シャドーイング訓練において最も重要な原則はどれか？",
             ["音声を完全に聞き取ってから、ゆっくり日本語に訳して発音する", "音声を0.5〜1秒遅れで追いかけ、イントネーションやリズムごと身体で模倣する", "スクリプトを最初から最後まで黙読して文法解析を行う"],
             "音声を0.5〜1秒遅れで追いかけ、イントネーションやリズムごと身体で模倣する",
             "シャドーイングは意味処理に頼りすぎず、耳からの音声を即座に調音器官で再現する自動化トレーニングです。"),
            ("シャドーイングの第2ステップである「マンブリング（mumbling）」の主目的は？",
             ["大声を出して周囲の人に聞かせること", "スクリプトの単語をノートに書き写すこと", "口の中でつぶやきながら、調音器官の筋肉を準備運動させること"],
             "口の中でつぶやきながら、調音器官の筋肉を準備運動させること",
             "マンブリングは負荷を抑えつつ、音声のスピードと調音の動きを合わせる準備段階です。"),
            ("シャドーイング中に単語の意味が分からなくなったときの最善の対処法は？",
             ["音声を一時停止し、辞書を引いて意味を調べる", "発声を止めずに音の真似を継続し、後からスクリプトで意味を確認する", "その日の練習を打ち切る"],
             "発声を止めずに音の真似を継続し、後からスクリプトで意味を確認する",
             "シャドーイングの最中は「音韻ループを止めない」ことが最優先です。意味確認は前後のステップで行います。")
        ]
    },
    {
        "id": "1182",
        "slug": "02-vowel-e-taling-pepet-drill",
        "title": "【母音 e 徹底攻略】[e]（テーリング）と [ə]（プルペッ）を聞き分け・発音し分ける50ペア",
        "desc": "同じ「e」の文字でありながら全く異なる2つの母音 [e] と [ə] の完全識別法。意味の違いを生むミニマルペアと調音の極意。",
        "theory": """### 1. インドネシア語の「e」には2種類の音がある
インドネシア語のアルファベット表記では、以下の2つの異なる母音が同じ「e」という文字で書かれます。
1. **e taling（テーリング） [e] または [ɛ]**:
   - 日本語の「エ」に近い。唇をやや左右に引いて、はっきりと発音する。
   - 例: *sore*（夕方 [so-re]）, *meja*（机 [me-dʒa]）, *bebek*（アヒル [be-bɛk]）。
2. **e pepet（プルペッ） [ə]（シュワー・曖昧母音）**:
   - 口を半開きにして完全に力を抜き、喉の奥から「ウ」と「ア」の中間のような音を短く弱く出す。
   - 例: *selamat*（無事 [sə-la-mat]）, *teman*（友達 [tə-man]）, *besar*（大きい [bə-sar]）。

### 2. 母音の混同が意味の致命的な違いを生む「ミニマルペア」
- **apel**:
  - `[a-pəl]`（プルペッ） = リンゴ（果物）
  - `[a-pel]`（テーリング） = 朝礼、点呼、集合
- **perang**:
  - `[pə-raŋ]`（プルペッ） = 戦争
  - `[pe-raŋ]`（テーリング） = 茶髪、金髪、明るい茶色
- **tahu**: （※語中の母音省略に関わるが、kemerdekaan などの接辞内の e はほぼすべてプルペッ）""",
        "drills": [
            ("【ミニマルペア対比】「リンゴ（apel [ə]）を買って、朝礼（apel [e]）に参加する」",
             "Saya membeli buah apel sebelum mengikuti apel pagi di kantor.",
             "サヤ ムンブリ ブア アプル スブルム ムンギクティ アペル パギ ディ カントール。",
             "1つ目の apel は口の力を抜いた [ə]、2つ目の apel は口を横に引いた明瞭な [e]。"),
            ("【ミニマルペア対比】「茶髪（perang [e]）の兵士が戦争（perang [ə]）に反対する」",
             "Tentara berambut perang itu menolak adanya perang.",
             "トゥンタラ ブラムブッ ペラン イトゥ ムノラッ アダニャ プラン。",
             "髪の色の perang は口を引く [e]、戦争の perang は喉の力を抜く [ə]。"),
            ("【テーリング [e] 単語】「アヒル（bebek [e]）が机（meja [e]）の下に隠れている」",
             "Bebek itu bersembunyi di bawah meja.",
             "ベベッ イトゥ ブルスンブニ ディ バワ メジャ。",
             "bebek と meja の e は日本語の「エ」と同じように口を横に引いて発音。"),
            ("【プルペッ [ə] 単語】「友人と一緒に（teman [ə]）大きな（besar [ə]）家を見る」",
             "Saya bersama teman melihat rumah yang sangat besar.",
             "サヤ ブルサマ トゥマン ムリハッ ルマ ヤン サンガッ ブサール。",
             "teman, besar, bersama の e はすべて力を抜いた曖昧母音 [ə]。"),
            ("【混在文】「夕方（sore [e]）、彼らは冷たい（sejuk [ə]）風を感じた」",
             "Pada sore hari, mereka merasakan angin yang sejuk.",
             "パダ ソレ ハリ、ムレカ ムラサカン アンギン ヤン スジュッ。",
             "sore と mereka の e はテーリング、sejuk の e はプルペッ。"),
            ("【テーリング [e]】「試験（tes [e]）の前に、美味しいケーキ（kue [e]）を食べる」",
             "Sebelum tes dimulai, kami makan kue yang enak.",
             "スブルム テス ディムライ、カミ マカン クエ ヤン エナッ。",
             "tes, kue, enak の e はすべてクリアなテーリング [e]。"),
            ("【プルペッ [ə]】「正しい（benar [ə]）答えを慎重に（cermat [ə]）選ぶ」",
             "Pilihlah jawaban yang benar secara cermat.",
             "ピリラ ジャワバン ヤン ブナル スチャラ チュルマッ。",
             "benar と cermat の e は音節の核として弱く曖昧に調音。"),
            ("【接頭辞 meN- / ber-】「勉強を続け（belajar [ə]）、本を読む（membaca [ə]）」",
             "Kita harus rajin belajar dan gemar membaca buku.",
             "キタ ハルス ラジン ブラジャル ダン グマル ムンバチャ ブク。",
             "接頭辞 ber-（be-）や meN-（mem-）の e は100% プルペッ [ə]。"),
            ("【テーリング [e]】「赤い（merah [e]）シャツを着た店員（sales [e]）」",
             "Petugas sales itu memakai kemeja merah yang mencolok.",
             "プトゥガス セレス イトゥ ムマカイ クメジャ メラ ヤン ムンチョロッ。",
             "merah の e はテーリング。petugas と kemeja の最初の e はプルペッ。"),
            ("【プルペッ [ə]】「9月（September）の初めに（pertama [ə]）出発する」",
             "Kami berangkat pada minggu pertama bulan September.",
             "カミ ブランカッ パダ ミング プルタマ ブラン セプテンベル。",
             "berangkat, pertama の e はプルペッ。September は [səp-tɛm-bər]。"),
            ("【同一単語内の混在】「インドネシア（Indonesia [e]）の独立（kemerdekaan [ə]）」",
             "Rakyat Indonesia merayakan hari kemerdekaan dengan gembira.",
             "ラッヤッ インドネシア ムラヤカン ハリ クムルデカアン ドゥンガン グンビラ。",
             "Indonesia の e はテーリング [e]、kemerdekaan の ke-, mer- はプルペッ [ə]。"),
            ("【注意単語】「カブトムシ（kumbang）とペニス・スラングではなく、カブトムシの仲間（kepik [ə]）」",
             "Petani menemukan kepik kecil di dedaunan.",
             "プタニ ムヌムカン クピッ クチル ディ ドゥダウナン。",
             "kepik の e はプルペッ。曖昧母音として弱く発声する。"),
            ("【外来語のテーリング】「現代のトレンド（tren [e]）とモデル（model [e]）」",
             "Model pakaian ini mengikuti tren mode terbaru.",
             "モデル パカイアン イニ ムンギクティ トレン モデ トゥルバル。",
             "欧米借用語の e は大半がテーリング [e]（tren, mode, model, hotel）。"),
            ("【数詞のプルペッ】「1（satu）、4（empat [ə]）、6（enam [ə]）、9（sembilan [ə]）」",
             "Nomor teleponnya mengandung angka empat, enam, dan sembilan.",
             "ノモル テレポンニャ ムンガンドゥン アンカ エンパッ、エナム、ダン スンビラン。",
             "empat, enam, sembilan, seratus, seribu の e はすべてプルペッ [ə]。"),
            ("【総仕上げ】「夕暮れ時（sore [e]）、大きな（besar [ə]）机（meja [e]）の上で美味しい（enak [e]）リンゴ（apel [ə]）を食べる」",
             "Di sore hari, saya makan apel enak di atas meja besar.",
             "ディ ソレ ハリ、サヤ マカン アプル エナッ ディ アタス メジャ ブサール。",
             "1文の中で [e] と [ə] が交互に出現しても、口の開きと緊張感を瞬時に切り替える。")
        ],
        "quizzes": [
            ("単語「apel」で、朝礼・点呼を意味する場合の「e」の発音は？",
             ["口の力を抜いた曖昧母音 [ə]（プルペッ）", "口を左右に引いてはっきり出す母音 [e]（テーリング）", "日本語の「イ」と同じ音"],
             "口を左右に引いてはっきり出す母音 [e]（テーリング）",
             "朝礼の apel は [a-pel]（テーリング）、果物のリンゴは [a-pəl]（プルペッ）と発音し分けます。"),
            ("動詞接頭辞「meN-」や「ber-」に含まれる母音「e」の正確な発音は？",
             ["常にテーリング [e]（日本語のエ）", "常にプルペッ [ə]（喉の力を抜いた曖昧母音）", "単語によって完全に自由"],
             "常にプルペッ [ə]（喉の力を抜いた曖昧母音）",
             "文法的な接辞（me-, ber-, ter-, per-, se-, ke-）の e は例外なくすべてプルペッ [ə] です。"),
            ("欧米からの外来語（hotel, televisi, tren など）の「e」の傾向は？",
             ["大半がプルペッ [ə] に変化する", "大半がテーリング [e] として発音される", "すべて母音が脱落して発音されない"],
             "大半がテーリング [e] として発音される",
             "近代の外来語は元の言語の発音を保ち、テーリング [e] で発音されるのが一般的です。")
        ]
    },
    {
        "id": "1183",
        "slug": "03-rolled-r-tongue-training",
        "title": "【巻き舌 r 完全克服】舌先を震わせるステップバイステップ調音トレーニング",
        "desc": "日本人が最も苦手とする歯茎ふるえ音（巻き舌の r）の解剖学的メカニズム。呼気圧と舌先の脱力による完全マスター手順。",
        "theory": """### 1. 巻き舌「r」の正体は「歯茎ふるえ音（Alveolar Trill [r]）」
日本語のラ行は、舌先で上あごを1回だけ弾く「弾き音（Tap/Flap [ɾ]）」です。
これに対し、インドネシア語の標準的な「r」は、**舌先を上の前歯の付け根（歯茎硬口蓋）に軽く当て、肺からの呼気（息）を押し出すことで、舌先が旗のようにバタバタと連続して振動する「ふるえ音（Trill [r]）」**です。

### 2. なぜ日本人は巻き舌ができないのか？
1. **舌先に力が入りすぎている**: 舌を固く緊張させると、息の力で振動しません。舌先は完全に脱力する必要があります。
2. **呼気（息の勢い）が足りない**: 振動を起こすためには、強い息の圧力が必要です。
3. **調音位置が後ろすぎる**: 英語の「r」のように舌を口の奥に巻き込むと、物理的に振動しません。

### 3. ステップバイステップ・トレーニング法
- **ステップ1: 「札幌ラーメン」メソッド**:
  - 日本語で「さっぽろ・らーめん」を「さっぽッらーめん」と発音し、促音（ッ）で呼気圧を溜めた直後に舌先を弾く感覚を掴む。
- **ステップ2: 「トゥルルル」息吐き練習**:
  - 「t」または「d」の音から始めて「tra... dra...」と息を吹き出す。舌先と歯茎の間に隙間を作り、呼気で風を起こす。
- **ステップ3: 語頭・語中・語末の段階的練習**:
  - 語中（murah, terima）→ 語頭（rumah, rusak）→ 語末（besar, belajar）の順に難易度が上がります。語末の r は軽く1〜2回振動させて息を抜きます。""",
        "drills": [
            ("【促音からの導入】「車（truk）と列車（kereta）が走る」",
             "Truk besar dan kereta api melintas dengan cepat.",
             "トゥルッ ブサール ダン クレタ アピ ムリンタス ドゥンガン チパッ。",
             "truk の tr- は舌先を振動させやすい起点。舌先を上の歯茎にセットして息を弾く。"),
            ("【語中 r】「どうもありがとうございます（terima kasih）」",
             "Terima kasih banyak atas bantuan Anda.",
             "トゥリマ カシ バニャッ アタス バントゥアン アンダ。",
             "terima の -ri- で舌先を2〜3回パラパラと振動させる。日本語の「リ」で済ませない。"),
            ("【語中 r】「安くて（murah）美味しい料理」",
             "Makanan ini sangat murah dan rasanya lezat.",
             "マカナン イニ サンガッ ムラ ダン ラサニャ ルザッ。",
             "murah の -ra- で母音 u から滑らかに舌先を振動位置へ運ぶ。"),
            ("【語頭 r】「私の家（rumah）は駅の近くにあります」",
             "Rumah saya berada di dekat stasiun.",
             "ルマ サヤ ブルアダ ディ ドゥカッ スタシウン。",
             "語頭の r は発声の瞬間に舌先を振動させる。呼気圧を強めに押し出す。"),
            ("【語頭 r】「車が故障して（rusak）、修理が必要です」",
             "Mobil saya rusak dan perlu segera diperbaiki.",
             "モビル サヤ ルサッ ダン プルル スゲラ ディプルバイキ。",
             "rusak と diperbaiki の r をしっかり鳴らし、クリアに発話する。"),
            ("【語頭 r】「豊かな（ramah）笑顔と親切な人々」",
             "Masyarakat di sini sangat ramah terhadap pendatang.",
             "マシャラカッ ディ シニ サンガッ ラマ トゥルハダッ プンダタン。",
             "ramah の r を明るく響かせ、親しみやすさを表現する。"),
            ("【二重 r・連続】「互いに（saling）愛し合う（merawat）」",
             "Kita harus merawat lingkungan secara bersama-sama.",
             "キタ ハルス ムラワッ リングンガン スチャラ ブルサマサマ。",
             "merawat と bersama の r をそれぞれ正確に調音する。"),
            ("【語末 r】「大きい（besar）部屋と新しい机」",
             "Kamar tidur ini cukup besar dan sangat bersih.",
             "カマル ティドゥル イニ チュクッ ブサール ダン サンガッ ブルシ。",
             "kamar, tidur, besar の語末 r は、音を消さずに舌先を軽く1〜2回震わせて止める。"),
            ("【語末 r】「毎日一生懸命勉強する（belajar）」",
             "Setiap hari saya rajin belajar bahasa Indonesia.",
             "スティアッ ハリ サヤ ラジン ブラジャル バハサ インドネシア。",
             "belajar の -jar の語末で息を吸い込まず、呼気とともに振動を残す。"),
            ("【語末 r】「外で（di luar）冷たい水を飲む」",
             "Jangan berdiri di luar saat hujan air turun lebat.",
             "ジャンガン ブルディリ ディ ルアル サアッ フジャン アイル トゥルン ルバッ。",
             "luar と air の語末 r を日本語の長音「ー」にしない（「ルアー」「アイ」にならないよう注意）。"),
            ("【接頭辞 ber-】「話す（berbicara）練習をする」",
             "Saya sedang latihan berbicara di depan umum.",
             "サヤ スダン ラティハン ブルビチャラ ディ ドゥパン ウムム。",
             "berbicara には ber- と -bicara の2つの r がある。軽快に舌を動かす。"),
            ("【接頭辞 ter-】「一番美しい（terindah）景色」",
             "Ini adalah pemandangan terindah yang pernah saya lihat.",
             "イニ アダラ プマンダンガン トゥルインダ ヤン プルナ サヤ リハッ。",
             "terindah と pernah の r を明瞭に発音し、リズムを引き締める。"),
            ("【難関・子音結合】「実践的（praktis）なプログラム（program）」",
             "Program pelatihan ini dirancang sangat praktis.",
             "プログラム プラティハン イニ ディランチャン サンガッ プラクティス。",
             "pr- の結合は、唇を閉じて p を破裂させた直後に舌先を振動させる。"),
            ("【難関・重畳語】「サラサラと流れる川の水（gemercik）」",
             "Suara gemercik air sungai terdengar sangat merdu.",
             "スアラ グムルチッ アイル スンガイ トゥルデンガル サンガッ ムルドゥ。",
             "gemercik, terdengar, merdu と連続する r を淀みなくコントロールする。"),
            ("【総仕上げ】「赤髪の（rambut merah）店員が、美味しいパン（roti）を勧めてくれた」",
             "Pria berambut merah itu merekomendasikan roti yang gurih dan renyah.",
             "プリア ブラムブッ メラ イトゥ ムレコメンダシカン ロティ ヤン グリ ダン ルニャ。",
             "rambut, merah, merekomendasikan, roti, gurih, renyah の全 r を完璧なふるえ音で再現する。")
        ],
        "quizzes": [
            ("インドネシア語の標準的な「r」の調音法として正しいものはどれか？",
             ["英語のように舌を口の奥深くに巻き込んで発音する", "舌先を上の歯茎に当て、呼気で振動させる（ふるえ音）", "日本語のラ行のように舌先で上あごを軽く1回だけ弾く"],
             "舌先を上の歯茎に当て、呼気で振動させる（ふるえ音）",
             "インドネシア語の r は歯茎ふるえ音（Trill）であり、呼気の圧力で舌先を振動させます。"),
            ("巻き舌の r を練習する際、舌先の力の入れ方として適切なのは？",
             ["舌全体に限界まで力を込めて硬くする", "舌先を完全に脱力させ、息の圧力で動くようにする", "舌を前歯で強く挟んで固定する"],
             "舌先を完全に脱力させ、息の圧力で動くようにする",
             "筋肉が緊張していると振動が起きません。舌先をリラックスさせ、息の勢いで旗をはためかせるイメージです。"),
            ("単語末尾の「r」（besar, kamar など）を日本人が発音する際の最も多いミスは？",
             ["語末の r を発音せず、単なる日本語の長音「ベサー」「カマー」にしてしまう", "語末の r の後に余計な母音「ル」を強く付けて「ベサル」「カマル」にしてしまう", "上記の両方とも典型的な母語干渉のミスである"],
             "上記の両方とも典型的な母語干渉のミスである",
             "長音化（脱落）も母音 u の挿入も日本語の干渉です。舌先を1〜2回振動させて息を止めるのが自然です。")
        ]
    },
    {
        "id": "1184",
        "slug": "04-glottal-stop-k-mastery",
        "title": "【語末 k の声門閉鎖音】「バソッ」と音を止める喉の使い方の完全マスター",
        "desc": "語末の「k」は破裂させず声門をピタッと閉じる。日本人の「ク」母音挿入を撲滅し、ネイティブ度を一気に引き上げる調音法。",
        "theory": """### 1. 語末「k」は「声門閉鎖音（Glottal Stop [ʔ]）」
日本語話者が最も犯しやすい発音ミスの筆頭が、語末の子音「k」の後に勝手に母音「u」を足して「ク」と発音してしまう現象です（カタカナ英語・カタカナ発音）。
- 誤: *tidak* を「ティダック」
- 誤: *enak* を「エナック」
- 誤: *masuk* を「マスク」

インドネシア語において、**音節末・語末の「k」は息を外に破裂させません（無開放閉鎖音）**。それどころか、事実上**「喉仏の奥（声門）をキュッと急激に閉じて音を遮断する声門閉鎖音（IPA: [ʔ]）」**として発音されます。
日本語の「あっ！」と驚いたときや、促音「バッ」「サッ」の詰まる感覚と全く同じです。

### 2. 語頭・語中・語末での「k」の振る舞い
1. **語頭・母音の前（kita, kopi）**: 通常の無声軟口蓋破裂音 [k]（息を吐いて「カ行」）。
2. **語末（tidak, bapak）**: 声門閉鎖音 [ʔ]（喉を閉じて音を止める）。
3. **語末「k」に母音から始まる接尾辞がついた場合**:
   - *masuk* [ma-suʔ] ＋ *-an* → *masukan* [ma-su-kan]（再び通常の [k] に戻る）。""",
        "drills": [
            ("【基本・否定】「いいえ、私はまだお腹が空いていません（tidak）」",
             "Tidak, saya belum merasa lapar.",
             "ティダッ、サヤ ブルム ムラサ ラパル。",
             "tidak は「ティダック」ではなく「ティダッ！」。喉を瞬時に閉じて音を切る。"),
            ("【基本・味覚】「このスープは本当に美味しいですね（enak）」",
             "Sup ini rasanya sungguh sangat enak sekali.",
             "スッ イニ ラサニャ スング サンガッ エナッ スカリ。",
             "enak は「エナック」ではなく「エナッ」。喉で音を捕まえる。"),
            ("【基本・敬称】「その書類は部長（bapak）にお渡ししました」",
             "Dokumen itu sudah saya serahkan kepada Bapak Direktur.",
             "ドクメン イトゥ スダ サヤ スラカン クパダ バパッ ディレク トゥル。",
             "Bapak は「バパック」ではなく「バパッ」。敬意を込めて端正に止める。"),
            ("【料理・名物】「屋台で温かい肉団子スープ（bakso）を食べる」",
             "Kami menikmati semangkuk bakso hangat di pinggir jalan.",
             "カミ ムニンマティ スマンクッ バッソ ハンガッ ディ ピンギル ジャラン。",
             "bakso の k は次の s の直前で喉を詰まらせる（「バッソ」）。semangkuk も同様。"),
            ("【日常・動作】「どうぞ部屋の中にお入りください（masuk）」",
             "Silakan masuk ke dalam ruangan ber-AC ini.",
             "シラカン マスッ ク ダラム ルアンガン ブルエーセー イニ。",
             "masuk はマスク（masker）と混同しないよう、末尾を「マスッ」と止める。"),
            ("【日常・状態】「服が雨でびしょ濡れ（basah kuyup）で寒気がする」",
             "Pakaian saya basah kuyup karena terkena hujan lebat.",
             "パカイアン サヤ バサ クユッ カルナ トゥルケナ フジャン ルバッ。",
             "kuyup の p も同様に唇を閉じて開かない無開放音。"),
            ("【対比練習】「子供（anak）が小さなバッグ（tas kecil）を持っている」",
             "Anak kecil itu membawa tas yang sangat lucu.",
             "アナッ クチル イトゥ ムンバワ タス ヤン サンガッ ルチュ。",
             "anak は「アナック」ではなく「アナッ」。母音 u の挿入を徹底排除。"),
            ("【数詞・語末 k】「たくさんの（banyak）人々が集まっている」",
             "Ada banyak orang yang berkumpul di lapangan.",
             "アダ バニャッ オラン ヤン ブルクンプル ディ ラパンガン。",
             "banyak は「バニャック」ではなく「バニャッ」。"),
            ("【感情・衝撃】「その知らせを聞いてとても驚いた（kaget）」",
             "Saya sangat kaget mendengar kabar mengejutkan tersebut.",
             "サヤ サンガッ カゲッ ムンデンガル カバル ムンジュトゥカン トゥルセブッ。",
             "kaget と mengejutkan の語末 t, n も母音を付けずにタイトに止める。"),
            ("【派生語での変化】「入る（masuk [ʔ]）→ 意見・インプット（masukan [k]）」",
             "Setelah masuk ke ruangan, kami menyampaikan masukan kepada tim.",
             "ス トゥラ マスッ ク ルアンガン、カミ ムンニャンパイカン マスカン クパダ ティム。",
             "masuk は「マスッ」、masukan は接尾辞が付いて「マスカン」と k が復活する。"),
            ("【派生語での変化】「座る（duduk [ʔ]）→ 住民（penduduk [k]）」",
             "Silakan duduk di sini bersama para penduduk desa.",
             "シラカン ドゥドゥッ ディ シニ ブルサマ パラ プンドゥドゥッ デサ。",
             "duduk は「ドゥドゥッ」、penduduk も語末なので「プンドゥドゥッ」。"),
            ("【名詞・場所】「私たちは古いお寺（kuil）と市場（pasar）を訪れた」",
             "Kami berkunjung ke tempat bersejarah yang sangat unik.",
             "カミ ブルクンジュン ク トゥムパッ ブルスジャラ ヤン サンガッ ウニッ。",
             "unik は「ユニーク」ではなく「ウニッ」。喉を止める。"),
            ("【会話チャンク】「ちょっと待ってください（tunggu sebentar [ʔ] なし / tunggu kok）」",
             "Tunggu sebentar, saya akan cek dokumennya dulu.",
             "トゥング スブンタル、サヤ アカン チェッ ドクメンニャ ドゥル。",
             "cek は「チェック」ではなく「チェッ！」。"),
            ("【複合文】「子供たち（anak-anak）が公園で元気に遊んでいる」",
             "Anak-anak sedang asyik bermain bola di taman.",
             "アナッ アナッ スダン アシッ ブルマイン ボラ ディ タマン。",
             "anak-anak は「アナッカナッ」とリンキングするか「アナッ・アナッ」と止める。asyik も「アシッ」。"),
            ("【総仕上げ】「お父さん（Bapak）、このスープ（bakso）は本当に美味しくて（enak）、ちっとも（tidak）辛くありません」",
             "Bapak, bakso ini rasanya sangat enak dan tidak pedas sama sekali.",
             "バパッ、バッソ イニ ラサニャ サンガッ エナッ ダン ティダッ プダス サマ スカリ。",
             "Bapak, bakso, enak, tidak の4大 k 声門閉鎖音を連続して完璧にコントロールする。")
        ],
        "quizzes": [
            ("インドネシア語の語末にある「k」（tidak, enak など）の調音法として正しいものは？",
             ["英語のように息を強く破裂させて「クッ」と発音する", "日本語の「ク」のように母音 u をはっきり発音する", "息を外に破裂させず、喉の奥（声門）を急激に閉じて音を止める"],
             "息を外に破裂させず、喉の奥（声門）を急激に閉じて音を止める",
             "語末の k は声門閉鎖音 [ʔ] であり、日本語の促音「ッ」のように喉を閉じて音を遮断します。"),
            ("単語「masuk [ma-suʔ]」に接尾辞「-an」が付いて「masukan」になった場合、k の音はどうなるか？",
             ["依然として声門閉鎖音のまま発音される", "母音 a と結合し、通常の破裂音 [k]（カ行の音）として発音される", "k の音が完全に消えて発音されなくなる"],
             "母音 a と結合し、通常の破裂音 [k]（カ行の音）として発音される",
             "後ろに母音接尾辞が来ると、k は音節頭子音となり、通常の [ka] として明瞭に発音されます。"),
            ("日本人が「tidak」を発音する際、最もネイティブらしさを損なう不自然な発音は？",
             ["「ティダッ」と語末を短く止める", "「ティダック」と語末に「ク」を足してしまう", "「ティダ」と子音を完全に抜かす"],
             "「ティダック」と語末に「ク」を足してしまう",
             "日本語には子音単独で終わる音節（閉音節）が「ん」「っ」以外にないため、無意識に母音 u を足してしまうのが最大の癖です。")
        ]
    },
    {
        "id": "1185",
        "slug": "05-nasal-clusters-ng-ny",
        "title": "【鼻音 ng と ny】日本人最大の弱点「鼻濁音」の正確な調音位置と練習法",
        "desc": "語頭に来ると発音できなくなる [ŋ]（ng）と、舌の中央を使う [ɲ]（ny）の解剖学的攻略。鼻腔共鳴を自在に操る特訓法。",
        "theory": """### 1. 日本人がつまずく2大鼻音「ng」と「ny」
日本語にも「ん」という鼻音がありますが、インドネシア語には独立した音素として以下の2つの鼻音が存在します。
1. **軟口蓋鼻音 [ŋ]（表記: ng）**:
   - 舌の奥（後舌面）を上あごの奥の柔らかい部分（軟口蓋）にピタッと密着させ、口からの息を完全に塞いだ状態で、**鼻から「ンー」と息を抜きながら母音を出す**。
   - 日本語の「漫画（まんが）」の「ん」や、東京方言の鼻濁音「が（nga）」の音。
   - **難所**: 語頭に来る単語（*ngantuk*, *ngopi*, *nggak*）が日本人は極めて苦手。
2. **硬口蓋鼻音 [ɲ]（表記: ny）**:
   - 舌先ではなく、**舌の中央（前舌面）を上あごの硬い部分（硬口蓋）に広くベタッと押し当てて、鼻から息を抜く音**。
   - 日本語の「ニャ・ニュ・ニョ」に極めて近いが、より舌の接触面積が広い。
   - 例: *nyamuk*（蚊 [ɲa-muk]）, *nyanyi*（歌う [ɲa-ɲi]）, *banyak*（多い [ba-ɲak]）。

### 2. 語頭「ng」を一瞬で発音できるようになる裏ワザ
語頭の「ng」が言えない人は、**直前に小さな「ん」を頭の中で思い浮かべてから発音する**と成功します。
- *ngantuk* → 「（ン）ガントゥッ」
- *ngopi* → 「（ン）ゴピ」
- *nggak* → 「（ン）ガッ」""",
        "drills": [
            ("【語頭 ng】「昨夜遅くまで起きていたので、とても眠い（ngantuk）」",
             "Saya sangat ngantuk karena semalam tidur larut.",
             "サヤ サンガッ ンガントゥッ カルナ スマラム ティドゥル ラルッ。",
             "ngantuk の頭の ng は鼻腔に息を通し、「ンガ」と滑らかに立ち上げる。"),
            ("【語頭 ng】「仕事の合間に、ちょっとカフェでコーヒーを飲もう（ngopi）」",
             "Yuk, kita istirahat sebentar sambil ngopi santai.",
             "ユッ、キタ イスティラハッ スブンタル サンビル ンゴピ サンタイ。",
             "ngopi は口語の超頻出語。鼻濁音でリラックスして発声する。"),
            ("【語頭 ng】「いや、全然大丈夫だよ、気にしないで（nggak apa-apa）」",
             "Nggak apa-apa kok, santai saja, tidak usah dipikirkan.",
             "ンガッ アパパ コッ、サンタイ サジャ、ティダッ ウサ ディピキルカン。",
             "nggak は鼻から息を抜いて「ンガッ」と語末を閉じる。"),
            ("【語中 ng】「なぜ（mengapa）そんな悲しい顔をしているの？」",
             "Mengapa Anda tampak begitu sedih hari ini?",
             "ムンガパ アンダ タンパッ ブギトゥ スディ ハリ イニ？",
             "mengapa の me-ngapa は、me と nga の間で舌の奥を持ち上げる。"),
            ("【語中 ng】「彼らは新しい計画について話し合っている（mengobrol）」",
             "Mereka sedang asyik mengobrol di ruang tamu.",
             "ムレカ スダン アシッ ムンゴブロル ディ ルアン タム。",
             "mengobrol の ng-o で鼻腔共鳴を途切れさせない。"),
            ("【語末 ng】「広い部屋（ruang）で静かに待つ」",
             "Silakan menunggu di ruang tunggu yang sudah disediakan.",
             "シラカン ムヌング ディ ルアン トゥング ヤン スダ ディスディアカン。",
             "ruang, tunggu の連続する ng を意識して鼻に抜く。"),
            ("【語末 ng】「今夜（malam ini）、美しい星空を見上げる（bintang）」",
             "Malam ini langit cerah dan penuh dengan bintang.",
             "マラム イニ ランギッ チュラ ダン プヌ ドゥンガン ビンタン。",
             "bintang の ng は、日本語の「ン」のように口を閉じず、口を開けたまま鼻から抜く。"),
            ("【ny の調音】「部屋の中に蚊（nyamuk）がたくさん入ってきた」",
             "Banyak nyamuk yang masuk ke dalam kamar tidur.",
             "バニャッ ニャムッ ヤン マスッ ク ダラム カマル ティドゥル。",
             "banyak と nyamuk の ny は舌の中央をしっかり上あごに押し当てる。"),
            ("【ny の連続】「彼女はステージの上で美しい歌を歌っている（menyanyi）」",
             "Dia sangat pandai menyanyi lagu daerah.",
             "ディア サンガッ パンダイ ムニャニ ラグ ダエラ。",
             "menyanyi の me-nya-nyi は舌の甲をペタペタと動かしてリズミカルに調音。"),
            ("【ny の日常語】「とても快適で（nyaman）リラックスできるホテル」",
             "Suasana di hotel ini terasa sangat nyaman dan damai.",
             "スアサナ ディ ホテル イニ トゥラサ サンガッ ニャマン ダン ダマイ。",
             "nyaman は「ニャマン」。鼻に響く心地よい音を意識する。"),
            ("【ny の日常語】「本物（nyata）の証拠を提示してください」",
             "Kami membutuhkan bukti yang nyata dan terverifikasi.",
             "カミ ムンブトゥカン ブクティ ヤン ニャタ ダン トゥルヴェリフィカシ。",
             "nyata は日本語の「ニャタ」。口を大きく開けすぎない。"),
            ("【ng と ny の同居】「歌を歌うこと（menyanyi）と話すこと（ngobrol）」",
             "Hobi saya adalah menyanyi lagu pop dan mengobrol bersama teman.",
             "ホビ サヤ アダラ ムニャニ ラグ ポップ ダン ムンゴブロル ブルサマ トゥマン。",
             "menyanyi（ny）と mengobrol（ng）の調音位置の移動をスムーズに行う。"),
            ("【動詞接頭辞 meN- + g】「聞く（mendengar）、覚える（mengingat）」",
             "Saya berusaha mengingat semua materi yang telah diajarkan.",
             "サヤ ブルサハ ムンインガッ スムア マテリ ヤン トゥラ ディアラカン。",
             "mengingat の -ngi- は舌の奥を持ち上げて「ムン・イ・ンガッ」。"),
            ("【動詞接頭辞 meN- + s】「料理を調理する（memasak）、探す（mencari）」",
             "Ibu sedang menyiapkan sarapan sehat di dapur.",
             "イブ スダン ムニヤプカン サラパン セハッ ディ ダプル。",
             "menyiapkan の nyi は meN- + siap から派生した音。"),
            ("【総仕上げ】「多くの蚊（banyak nyamuk）が飛んでいるので、歌う（menyanyi）のをやめてコーヒーを飲む（ngopi）」",
             "Karena banyak nyamuk, kami berhenti menyanyi dan memilih untuk ngopi santai.",
             "カルナ バニャッ ニャムッ、カミ ブルヘンティ ムニャニ ダン ムミリ ウントゥッ ンゴピ サンタイ。",
             "banyak, nyamuk, menyanyi（ny）と ngopi（ng）の対比を完璧にこなす。")
        ],
        "quizzes": [
            ("インドネシア語の「ng」（軟口蓋鼻音 [ŋ]）を発音する際の舌の位置は？",
             ["舌先を上の前歯の裏に強く当てる", "舌の中央を上あごの硬い部分（硬口蓋）に広く押し当てる", "舌の奥（後舌面）を喉の奥の柔らかい部分（軟口蓋）に密着させ、鼻から息を抜く"],
             "舌の奥（後舌面）を喉の奥の柔らかい部分（軟口蓋）に密着させ、鼻から息を抜く",
             "ng は軟口蓋鼻音であり、舌の奥を持ち上げて口の通路を塞ぎ、鼻腔から音を響かせます。"),
            ("語頭の「ng」（ngantuk, ngopi など）が苦手な日本人がスムーズに発音するためのコツは？",
             ["息を止めて「ガ」「ゴ」と力強く破裂させる", "直前に小さな「ん」を頭の中で思い浮かべ、鼻から息を通しながら母音を出す", "ng を完全に無視して「アントゥッ」「オピ」と言う"],
             "直前に小さな「ん」を頭の中で思い浮かべ、鼻から息を通しながら母音を出す",
             "日本語の「ん」の口構え（舌の奥を上げる）から滑らかに母音へ移行すると、自然な語頭 ng になります。"),
            ("「ny」（nyamuk, banyak など）の調音法として最も近い日本語の音は？",
             ["マ行（マ・ミ・ム・メ・モ）", "ニャ行（ニャ・ニュ・ニョ）", "ラ行（ラ・リ・ル・レ・ロ）"],
             "ニャ行（ニャ・ニュ・ニョ）",
             "ny は硬口蓋鼻音 [ɲ] であり、日本語の「ニャ・ニュ・ニョ」と調音位置がほぼ同一です。")
        ]
    },
    {
        "id": "1186",
        "slug": "06-diphthongs-glides",
        "title": "【二重母音と滑音】ai, au, oi のスムーズな移行と w, y の渡り音",
        "desc": "二重母音（diftong: ai, au, oi）と単なる母音連続（vokal berurutan）の決定的差異。渡り音（glide）を活かした滑らかな発声。",
        "theory": """### 1. 「二重母音（Diftong）」とは何か？
インドネシア語正書法（EYD）において、公式に二重母音（diftong）として定義されているのは **ai, au, oi, ei** の4つです。
- **二重母音の特徴**:
  - **1つの音節（1拍）**の中で、第1母音から第2母音へ向かって滑らかに音色を変化させる（滑音: Glide）。
  - 例: *pan-dai*（賢い [pan-dai̯]）, *pu-lau*（島 [pu-lau̯]）, *am-boi*（まあ！ [am-boi̯]）。

### 2. 二重母音（Diftong）vs 母音連続（Vokal Berurutan）の識別
ここが学習者の最大の盲点です。同じ文字の並びでも、**二重母音ではなく「2つの独立した音節」として分かれる単語**が存在します。
- **二重母音（1音節）**:
  - *santai* → `[san-tai̯]`（2音節）
  - *kalau* → `[ka-lau̯]`（2音節）
- **母音連続（2音節に分かれる）**:
  - *kain* → `[ka-in]`（2音節・布）
  - *mau* → `[ma-u]`（2音節・〜したい）
  - *daun* → `[da-un]`（2音節・葉）
  - *laut* → `[la-ut]`（2音節・海）

### 3. 渡り音（Glide）w と y の自然な発生
母音が連続するとき、ネイティブの口の中では自然に滑音（w または y）が渡り音として挿入されます。
- *dia* → `[di-ya]`（微小な y が渡る）
- *dua* → `[du-wa]`（微小な w が渡る）
- *semua* → `[se-mu-wa]`""",
        "drills": [
            ("【二重母音 ai】「カフェのテラスでリラックスして（santai）過ごす」",
             "Kami duduk santai sambil menikmati udara sore.",
             "カミ ドゥドゥッ サンタイ サンビル ムニンマティ ウダラ ソレ。",
             "santai の -tai は1音節。日本語の「サン・タ・イ」と3拍に区切らず「サンタイ」と滑らせる。"),
            ("【母音連続 a-i】「市場で伝統的なバティックの布（kain）を買う」",
             "Ibu membeli kain batik tradisional bermotif indah.",
             "イブ ムンブリ カイン バティッ トラディシオナル ブルモティフ インダ。",
             "kain は ka-in と2音節に分かれる。ka と in の境目を意識する。"),
            ("【二重母音 au】「バリ島は世界的に有名な美しい島（pulau）です」",
             "Pulau Bali adalah salah satu destinasi wisata terpopuler di dunia.",
             "プラウ バリ アダラ サラ サトゥ デスティナシ ウィサタ トゥルポプレル ディ ドゥニア。",
             "pulau の -lau は1拍で「プラウ」。口をすぼめながら au を流す。"),
            ("【母音連続 a-u】「私たちは新しいプロジェクトを始めたい（mau）」",
             "Kami mau memulai proyek kerja sama ini secepatnya.",
             "カミ マウ ムムライ プロイェッ クルジャ サマ イニ スチパッニャ。",
             "mau は ma-u と2音節。短くても「マ・ウ」の拍を感じさせる。"),
            ("【母音連続 a-u】「風に揺れる緑の木の葉（daun）」",
             "Dedaunan hijau bergoyang tertiup angin sepoi-sepoi.",
             "ドゥダウナン ヒジャウ ブルゴヤン トゥルティウッ アンギン スポイ スポイ。",
             "daun は da-un、sepoi-sepoi は二重母音 -poi（1音節）。"),
            ("【母音連続 a-u】「青く澄んだ海（laut）を眺める」",
             "Dari atas bukit, kami bisa memandang luasnya laut biru.",
             "ダリ アタス ブキッ、カミ ビサ ムマンダン ルアスニャ ラウッ ビル。",
             "laut は la-ut と2拍。語末 t は声門・舌先でしっかり止める。"),
            ("【渡り音 y の挿入】「彼（dia）は明日ジャカルタへ出発する」",
             "Dia akan berangkat ke Jakarta besok pagi.",
             "ディア（ディヤ） アカン ブランカッ ク ジャカルタ ベソッ パギ。",
             "dia の i と a の間に自然な [j]（yの音）が渡ることで「ディヤ」と滑らかになる。"),
            ("【渡り音 w の挿入】「2つ（dua）の選択肢を慎重に比較する」",
             "Ada dua pilihan yang harus kita pertimbangkan dengan matang.",
             "アダ ドゥア（ドゥワ） ピリハン ヤン ハルス キタ プルティンバンカン ドゥンガン マタン。",
             "dua の u と a の間に自然な [w] が渡り「ドゥワ」と聞こえる。"),
            ("【渡り音 w の挿入】「すべての（semua）メンバーが集まった」",
             "Semua anggota tim telah hadir di ruang pertemuan.",
             "スムア（スムワ） アンゴタ ティム トゥラ ハディル ディ ルアン プルトゥムアン。",
             "semua は se-mu-wa と滑らかに移行させる。"),
            ("【二重母音 oi】「そよ風が心地よく吹いている（sepoi-sepoi）」",
             "Angin sepoi-sepoi berhembus menyejukkan suasana pantai.",
             "アンギン スポイ スポイ ブルヘンブス ムニェジュッカン スアサナ パンタイ。",
             "sepoi-sepoi の -poi は典型的な二重母音。パンタイ（pantai）の -tai も二重母音。"),
            ("【二重母音 ai】「彼女は様々な外国語を操る賢い（pandai）女性だ」",
             "Gadis yang pandai itu menguasai berbagai bahasa asing.",
             "ガディス ヤン パンダイ イトゥ ムングアサイ ブルバガイ バハサ アシン。",
             "pandai, menguasai, berbagai に現れる -ai を流暢に繋ぐ。"),
            ("【母音連続 u-a】「私たちは広い（luas）庭のある家に住んでいる」",
             "Rumah itu memiliki halaman yang sangat luas dan asri.",
             "ルマ イトゥ ムミリキ ハラマン ヤン サンガッ ルアス（ルワス） ダン アスリ。",
             "luas は lu-as。w の滑音を自然に介在させる。"),
            ("【二重母音 au】「もし（kalau）時間があれば、一緒に行きましょう」",
             "Kalau ada waktu luang, mari kita pergi bersama.",
             "カラウ アダ ワクトゥ ルアン、マリ キタ プルギ ブルサマ。",
             "kalau の -lau は一拍で発音。「カ・ラ・ウ」と伸ばさない。"),
            ("【二重母音 ei】「彼は測量技師（survei）として働いている」",
             "Tim sedang melakukan survei lapangan di lokasi proyek.",
             "ティム スダン ムラクカン スルヴェイ ラパンガン ディ ロカシ プロイェッ。",
             "survei の -vei は二重母音 ei [ei̯]。"),
            ("【総仕上げ】「もし（kalau）天気が良ければ、島（pulau）へ行って浜辺でリラックス（santai）したい（mau）」",
             "Kalau cuaca cerah, kami mau pergi ke pulau dan duduk santai di pantai.",
             "カラウ チュアチャ チュラ、カミ マウ プルギ ク プラウ ダン ドゥドゥッ サンタイ ディ パンタイ。",
             "二重母音（kalau, pulau, santai, pantai）と母音連続（mau）の拍感覚を完全に区別して発話する。")
        ],
        "quizzes": [
            ("単語「santai」の「-ai」と「kain」の「-ai-」の違いとして正しいものは？",
             ["どちらも全く同じ2音節の母音連続である", "santai の ai は1音節の二重母音（diftong）だが、kain は ka-in と2音節に分かれる", "kain の方が二重母音で、santai は3音節である"],
             "santai の ai は1音節の二重母音（diftong）だが、kain は ka-in と2音節に分かれる",
             "santai は [san-tai̯]（2音節）ですが、kain は [ka-in]（2音節・母音連続）であり、音節の区切れが異なります。"),
            ("単語「dia」や「dua」を発音する際、母音の間に自然に生じる音（渡り音）は？",
             ["それぞれ [k] と [t] の破裂音が挟まる", "dia には [y]、dua には [w] の滑らかな渡り音（Glide）が生じる", "母音の間に声門閉鎖音 [ʔ] が入って音が途切れる"],
             "dia には [y]、dua には [w] の滑らかな渡り音（Glide）が生じる",
             "狭母音（i, u）から広母音（a）へ移行する際、自然に半母音的滑音（y, w）が渡り音として介在します。"),
            ("二重母音（diftong）を発音する際の基本的なリズム感覚は？",
             ["日本語のように「ア・イ」「ア・ウ」と2拍に均等に分けて発音する", "1拍（1音節）の中で第1母音から第2母音へ滑らかに音色を移行させる", "第2母音だけを極端に長く伸ばして発音する"],
             "1拍（1音節）の中で第1母音から第2母音へ滑らかに音色を移行させる",
             "二重母音は1つの音節核を成すため、1拍の長さの中で滑らかに音を変えます。")
        ]
    },
    {
        "id": "1187",
        "slug": "07-linking-liaison",
        "title": "【連音（リンキング）】単語境界で音がつながるネイティブの自然なリエゾン",
        "desc": "単語と単語の境界で音が滑らかに連結する「リンキング」。ロボットのようなぶつ切り発音を脱し、流暢なリズムを獲得する。",
        "theory": """### 1. 「リンキング（連音・Liaison）」とは？
日本語は「1文字＝1拍」のモーラ言語であるため、日本人は単語と単語の間で無意識に音を区切り（「Saya / makan / nasi」）、ロボットのようにぶつ切りの発音になりがちです。

一方、インドネシア語のネイティブスピーカーは、**前の単語の語末子音と、次の単語の語頭母音を一体化させて滑らかに発音（リンキング: Linking）**します。
- 表記: *anak ayam*（ヒヨコ）
- 個別発音: [a-nak] ＋ [a-yam]
- 実際のリンキング発音: **[a-na-ka-yam]**（アナカヤム）

### 2. インドネシア語の主要なリンキング・パターン
1. **子音 ＋ 母音（C + V）の結合**:
   - *tidak ada* → **[ti-da-ka-da]**（ティダカダ）
   - *sudah enak* → **[su-da-he-nak]**（スダヘナッ）
   - *makan apel* → **[ma-ka-na-pəl]**（マカナプル）
2. **母音 ＋ 母音（V + V）の滑音結合**:
   - *ada apa* → **[a-da-pa]** または **[a-da-wa-pa]**（アダパ／アダワパ）
   - *ke mana saja* → 一息で流れるように発音
3. **語末 k 声門閉鎖 ＋ 母音**:
   - 声門閉鎖音 [ʔ] が解除され、軽やかな [k] として次の母音と結びつく現象。""",
        "drills": [
            ("【C + V リンキング】「何もない、問題ない（tidak ada）」",
             "Tidak ada masalah yang perlu dikhawatirkan sama sekali.",
             "ティダカダ マサラ ヤン プルル ディカワティルカン サマ スカリ。",
             "tidak ada は「ティダッ・アダ」と切らず、[ti-da-ka-da]（ティダカダ）と一息で繋ぐ。"),
            ("【C + V リンキング】「どういたしまして、問題ありません（tidak apa-apa）」",
             "Sama-sama, tidak apa-apa, jangan sungkan ya.",
             "サマサマ、ティダカパパ、ジャンガン スンカン ヤ。",
             "tidak apa-apa は [ti-da-ka-pa-pa]（ティダカパパ）と軽やかに連音させる。"),
            ("【C + V リンキング】「ヒヨコ（anak ayam）が庭を歩いている」",
             "Anak ayam itu berjalan mengikuti induknya di halaman.",
             "アナカヤム イトゥ ブルジャラン ムンギクティ イン ドゥッニャ ディ ハラマン。",
             "anak ayam は [a-na-ka-yam] と発音し、ak-ay の境界を完全に融合させる。"),
            ("【C + V リンキング】「リンゴを食べる（makan apel）」",
             "Setiap pagi saya selalu makan apel segar untuk sarapan.",
             "スティアッ パギ サヤ スラル マカナプル スガル ウントゥッ サラパン。",
             "makan apel は [ma-ka-na-pəl]（マカナプル）と連音する。"),
            ("【C + V リンキング】「もう十分に美味しい（sudah enak）」",
             "Sup ini sudah enak, tidak perlu ditambah garam lagi.",
             "スッ イニ スダヘナッ、ティダカダ プルル ディタンバ ガラム ラギ。",
             "sudah enak は [su-da-he-naʔ] と h の息を次の e に乗せる。"),
            ("【C + V リンキング】「水を飲む（minum air）」",
             "Jangan lupa minum air putih yang cukup setiap hari.",
             "ジャンガン ルパ ミヌマイル プティ ヤン チュクッ スティアッ ハリ。",
             "minum air は [mi-nu-ma-yir]（ミヌマイル）と m を繋げる。"),
            ("【V + V リンキング】「どうしたの？何かあった？（ada apa）」",
             "Ada apa denganmu? Mengapa wajahmu terlihat pucat?",
             "アダパ ドゥンガンム？ ムンガパ ワジャフム トゥルリハッ プチャッ？",
             "ada apa は [a-da-pa] と縮約されるか、滑らかに連結して発声。"),
            ("【C + V リンキング】「一冊の本（sebuah buku / satu orang）」",
             "Hanya ada satu orang yang datang tepat waktu.",
             "ハニャ アダ サトゥオラン（サトゥウォラン） ヤン ダタン トゥパッ ワクトゥ。",
             "satu orang は [sa-tu-wo-raŋ] と渡り音 w を挟んで流す。"),
            ("【前置詞のリンキング】「家の中で（di dalam rumah）」",
             "Anak-anak sedang bermain di dalam rumah.",
             "アナカニャッ スダン ブルマイン ディダラム ルマ。",
             "di dalam は [di-da-lam] と1単語のように一体化させて発音。"),
            ("【否定詞のリンキング】「まだ起きていない（belum bangun / belum ada）」",
             "Belum ada kabar terbaru mengenai keputusan tersebut.",
             "ブルマダ カバル トゥルバル ムンゲナイ クプトゥサン トゥルセブッ。",
             "belum ada は [bə-lu-ma-da]（ブルマダ）と連結。"),
            ("【前置詞のリンキング】「彼から（dari dia）」",
             "Saya baru saja menerima pesan singkat dari dia.",
             "サヤ バル サジャ ムヌリマ プサン シンカッ ダリディア。",
             "dari dia は [da-ri-di-ya] と淀みなく繋げる。"),
            ("【C + V リンキング】「もっと多い（lebih banyak / lebih enak）」",
             "Makanan di restoran ini jauh lebih enak daripada yang kemarin.",
             "マカナン ディ レストラン イニ ジャウ ルビヘナッ ダリパダ ヤン クマリン。",
             "lebih enak は [lə-bi-he-naʔ] と連結。"),
            ("【C + V リンキング】「本を開く（buka pintu / masuk angin）」",
             "Badan saya terasa tidak enak, sepertinya saya masuk angin.",
             "バダン サヤ トゥラサ ティダケナッ、スプルティニャ サヤ マスカンギン。",
             "masuk angin は [ma-su-ka-ŋin]（マスカンギン）の連結が定着している。"),
            ("【長文リンキング】「もし時間があれば、どうぞここに来てください」",
             "Kalau ada waktu, silakan mampir ke kantor kami kapan saja.",
             "カラワダ ワクトゥ、シラカン マンピル ク カントル カミ カパン サジャ。",
             "Kalau ada は [ka-law-a-da]、kapan saja は [ka-pan-sa-ja]。"),
            ("【総仕上げ】「何もない（tidak ada）、ヒヨコ（anak ayam）がリンゴを食べた（makan apel）だけだ」",
             "Tidak ada apa-apa, hanya seekor anak ayam yang sedang makan apel.",
             "ティダカダ アパパ、ハニャ スエコル アナカヤム ヤン スダン マカナプル。",
             "tidak ada, apa-apa, seekor, anak ayam, makan apel の全リンキングを一息で美しく繋ぐ。")
        ],
        "quizzes": [
            ("フレーズ「tidak ada」をネイティブが自然な速度で発音した時の音は？",
             ["「ティダック・アダ」と完全に単語の間を区切る", "「ティダカダ [ti-da-ka-da]」のように語末の k が次の a と連結する", "「ティダ・ダ」と k が完全に脱落して消える"],
             "「ティダカダ [ti-da-ka-da]」のように語末の k が次の a と連結する",
             "語末子音と次の語頭母音が連結（リンキング）し、[ti-da-ka-da] と滑らかに一体化します。"),
            ("「masuk angin（風邪をひく）」が日常会話で「マスカンギン」と聞こえる理由は？",
             ["masuk の語末 k と angin の語頭 a がリンキングして [ka] の音節を作るため", "インドネシア人が masuk の発音を間違えているため", "angin の a が脱落して k と ng が結合するため"],
             "masuk の語末 k と angin の語頭 a がリンキングして [ka] の音節を作るため",
             "典型的な子音＋母音のリンキングであり、[ma-su-ka-ngin] と1つの複合語のように発音されます。"),
            ("リンキングを意識して発音する最大のメリットは何か？",
             ["文法的なミスを減らすことができる", "日本語特有のぶつ切り発音を脱し、流暢で自然なスピーチリズムを獲得できる", "単語の文字数を減らして書くことができる"],
             "日本語特有のぶつ切り発音を脱し、流暢で自然なスピーチリズムを獲得できる",
             "リンキングにより発声の息の流れが持続し、ネイティブ特有の滑らかなメロディが生まれます。")
        ]
    },
    {
        "id": "1188",
        "slug": "08-penultimate-stress-rule",
        "title": "【語幹アクセントと接辞】接辞が付いても動かない原則後から2番目の音節ルール",
        "desc": "インドネシア語の強勢アクセントの絶対法則「最後から2番目の音節（Penultimate Syllable）」。接辞付加によるアクセント移動の完全体系。",
        "theory": """### 1. インドネシア語の基本強勢ルール
インドネシア語には、英語のような強い高低・強弱アクセント（Stress Accent）や、日本語のような高低ピッチアクセントはありません。
しかし、**「単語の最後から2番目の音節（Penultimate Syllable: 後ろから2番目）」に、穏やかな強勢（やや高く、やや長めに発声）が置かれる**という極めて規則的な法則が存在します。

- *ru-mah* → **ru**-mah
- *ma-kan* → **ma**-kan
- *In-do-ne-sia* → In-do-**ne**-sia
- *ja-kar-ta* → ja-**kar**-ta

### 2. 例外規則: 最後から2番目の音節が「プルペッ [ə]」の場合
最後から2番目の音節の母音がプルペッ（曖昧母音 [ə]）である場合、この音節は弱いため強勢を支えられず、**強勢は「最後の音節（Ultimate Syllable）」へシフト**します。
- *be-sar* → be-**sar**（サールに強勢）
- *ce-pat* → ce-**pat**（パットに強勢）
- *se-nang* → se-**nang**（ナンに強勢）

### 3. 接尾辞が付くと強勢位置がシフトする！
接頭辞（meN-, ber-, di-）が付いても音節の後ろの数は変わらないため強勢位置は動きませんが、**接尾辞（-an, -kan, -i）が付くと音節が増えるため、強勢が後ろへ移動します**。
- *bu-ka*（開ける）: **bu**-ka
  - ＋ *-kan* → *bu-ka-kan*: bu-**ka**-kan（強勢が ka へ移動！）
- *ja-lan*（道・歩く）: **ja**-lan
  - ＋ *per-...-an* → *per-ja-la-nan*: per-ja-**la**-nan（強勢が la へ移動！）""",
        "drills": [
            ("【基本2音節】「本（BU-ku）を読む」",
             "Saya membaca buku cerita yang menarik.",
             "サヤ ムンバチャ ブク チェリタ ヤン ムナリッ。",
             "buku の強勢は bu。bu をわずかに高く、穏やかに伸ばす。"),
            ("【基本3音節】「学校（se-KO-lah）へ行く」",
             "Anak-anak berangkat ke sekolah setiap pagi.",
             "アナカニャッ ブランカッ ク スコラ スティアッ パギ。",
             "sekolah の強勢は後ろから2番目の ko。se-KO-lah。"),
            ("【プルペッ例外】「大きな（be-SAR）家を見る」",
             "Rumah itu sangat besar dan megah.",
             "ルマ イトゥ サンガッ ブサール ダン ムガ。",
             "besar の be は [ə] なので強勢を持てず、後ろの sar にアクセントが移る。"),
            ("【プルペッ例外】「素早く（ce-PAT）走る」",
             "Kereta cepat Whoosh melaju dengan kecepatan tinggi.",
             "クレタ チパッ ウーシュ ムラジュ ドゥンガン クチパタン ティンギ。",
             "cepat の ce は [ə] なので pat に強勢。kecepatan になると pa にシフト。"),
            ("【接頭辞の付加】「本を読む（mem-BA-ca）」",
             "Dia sangat gemar membaca buku sejarah.",
             "ディア サンガッ グマル ムンバチャ ブク スジャラ。",
             "mem-ba-ca の強勢は後ろから2番目の ba。接頭辞 mem- は強勢に影響しない。"),
            ("【接尾辞 -an のシフト】「食べ物（ma-ka-nan: ma-KA-nan）」",
             "Makanan khas daerah ini sangat lezat dan gurih.",
             "マカナン カス ダエラ イニ サンガッ ルザッ ダン グリ。",
             "makan（MA-kan）に -an が付いて makanan（ma-KA-nan）と ka に移動。"),
            ("【接尾辞 -kan のシフト】「説明する（men-je-las-kan: men-je-LAS-kan）」",
             "Dosen itu menjelaskan teori ekonomi secara rinci.",
             "ドセン イトゥ ムンジェラスカン テオリ エコノミ スチャラ リンチ。",
             "jelas（je-LAS）＋ -kan → menjelaskan（men-je-LAS-kan）と las に強勢。"),
            ("【接尾辞 -i のシフト】「愛する（men-cin-ta-i: men-cin-TA-i）」",
             "Kita harus mencintai tanah air kita Indonesia.",
             "キタ ハルス ムンチンタイ タナ アイル キタ インドネシア。",
             "cinta（CIN-ta）＋ -i → mencintai（men-cin-TA-i）と ta に強勢。"),
            ("【周囲辞 per-...-an】「旅・道のり（per-ja-la-nan: per-ja-LA-nan）」",
             "Perjalanan menuju puncak gunung memakan waktu lima jam.",
             "プルジャラナン ムヌジュ プンチャッ グヌン ムマカン ワクトゥ リマ ジャム。",
             "jalan（JA-lan）から perjalanan（per-ja-LA-nan）へシフト。"),
            ("【周囲辞 ke-...-an】「成功（ke-ber-ha-si-lan: ke-ber-ha-SI-lan）」",
             "Kerja keras adalah kunci keberhasilan dalam karier.",
             "クルジャ クラス アダラ クンチ クブルハシラン ダラム カリエル。",
             "hasil（HA-sil）から keberhasilan（ke-ber-ha-SI-lan）へシフト。"),
            ("【地名のアクセント】「ジャカルタ（ja-KAR-ta）、スラバヤ（su-ra-BA-ya）」",
             "Penerbangan dari Jakarta menuju Surabaya memakan waktu satu jam.",
             "プネルバンガン ダリ ジャカルタ ムヌジュ スラバヤ ムマカン ワクトゥ サトゥ ジャム。",
             "ja-KAR-ta, su-ra-BA-ya ともに後ろから2番目の音節を自然に立てる。"),
            ("【4音節以上の語】「大学（u-ni-ver-si-tas: u-ni-ver-SI-tas）」",
             "Dia kuliah di salah satu universitas terkemuka di Bandung.",
             "ディア クリア ディ サラ サトゥ ユニヴェルシタス トゥルケムカ ディ バンドン。",
             "後ろから数えて2番目の si に強勢を置く。"),
            ("【接尾辞付きの対比】「開ける（bu-ka）→ ドアを開けてあげる（bu-ka-kan）」",
             "Tolong buka pintunya, lalu bukakan juga jendelanya.",
             "トロン ブカ ピントゥニャ、ラル ブカカン ジュガ ジェンデラニャ。",
             "buka（BU-ka）と bukakan（bu-KA-kan）の強勢移動を対比して発声。"),
            ("【複合名詞のアクセント】「rumah sakit（病院: ru-mah SA-kit）」",
             "Ambulans itu segera melaju kencang menuju rumah sakit.",
             "アンブランス イトゥ スゲラ ムラジュ クンチャン ムヌジュ ルマ サキッ。",
             "複合語では後ろの単語（sakit）の第2音節（sa）が主強勢となる。"),
            ("【総仕上げ】「旅行（per-ja-LA-nan）の成功（ke-ber-ha-SI-lan）を祈り、食事（ma-KA-nan）を楽しむ」",
             "Semoga perjalanan Anda menyenangkan, dan nikmatilah makanan enak ini.",
             "スモガ プルジャラナン アンダ ムニュナンカン、ダン ニクマティラ マカナン エナッ イニ。",
             "per-ja-LA-nan, me-nye-NANG-kan, ma-KA-nan の語幹シフト規則を完璧に再現する。")
        ],
        "quizzes": [
            ("インドネシア語の単語において、原則として強勢（アクセント）が置かれる位置は？",
             ["常に単語の最初の音節（第1音節）", "原則として最後から2番目の音節（後ろから2番目）", "常に単語の最後の音節"],
             "原則として最後から2番目の音節（後ろから2番目）",
             "インドネシア語は最後から2番目の音節（Penultimate Syllable）に穏やかな強勢を置くのが基本ルールです。"),
            ("単語「besar」や「cepat」のように、最後から2番目の母音がプルペッ [ə] の場合、強勢はどうなるか？",
             ["プルペッの音節に極端に強いアクセントを置く", "強勢が最後の音節（-sar, -pat）へシフトする", "単語全体のアクセントが完全に消失する"],
             "強勢が最後の音節（-sar, -pat）へシフトする",
             "プルペッ（曖昧母音）は音として弱いため強勢を支えられず、最後の音節へ強勢が移動します。"),
            ("単語「makan」に接尾辞「-an」が付いて「makanan」になった場合、強勢の位置はどう変化するか？",
             ["ma に留まったまま変わらない", "音節が増えたため、後ろから2番目となる ka に強勢が移動する", "最後の音節 nan に移動する"],
             "音節が増えたため、後ろから2番目となる ka に強勢が移動する",
             "接尾辞が付くと全体の音節数が増えるため、「最後から2番目」のルールに従って強勢が後ろへ1音節シフトします。")
        ]
    },
    {
        "id": "1189",
        "slug": "09-sentence-intonation-pitch",
        "title": "【文全体の抑揚（イントネーション）】疑問文・平叙文・命令文のピッチパターン",
        "desc": "感情や意図を正確に伝えるインドネシア語のプロソディ（抑揚・ピッチ）。平叙文・疑問文・命令文・強調の音調カーブをマスターする。",
        "theory": """### 1. インドネシア語の文イントネーション体系
イントネーション（文全体の音の高低パターンの変化）は、文の種類（平叙文・疑問文・命令文）や、話者の感情（親愛・疑念・怒り・丁寧）を決定づける極めて重要な要素です。

### 2. 3大基本パターンのピッチカーブ
1. **平叙文（Declarative: 下降調 ↘）**:
   - 文頭から中盤にかけて中位のピッチを保ち、**文末の最後の強勢音節でわずかに上昇した後、急激に下降**して終わる（Falling Intonation）。
   - 例: *Saya mau makan nasi goreng.*（中位 → 低下降 ↘）
2. **疑問文（Interrogative）**:
   - **Yes/No 疑問文（apa/apakah 文・助詞文: 上昇調 ↗）**:
     - 文末に向かってピッチが高くなり、語尾をキュッと上げて終わる（Rising Intonation）。
     - 例: *Bapak sudah makan?* ↗, *Mau ikut tidak?* ↗
   - **疑問詞疑問文（5W1H: 疑問詞高調 → 文末下降調 ↘）**:
     - 疑問詞（kapan, di mana, siapa）が最も高いピッチで発音され、**文末に向かって下降**する（英語と同様）。
     - 例: ***Kapan* Anda berangkat ke Bali?** ↘（Kapan が最高音、Bali は下降）
3. **命令文・依頼文（Imperative: 水平調 → 急降下 ⤓）**:
   - 力強いピッチで水平に保たれ、文末でピタッと切れるように急降下する。
   - 丁寧な依頼（tolong, silakan）は、中盤に穏やかな波を作り、語尾に *ya* を添えてわずかに上げる。""",
        "drills": [
            ("【平叙文・下降調 ↘】「私は明日ジャカルタへ行きます」",
             "Saya akan pergi ke Jakarta besok pagi.",
             "サヤ アカン プルギ ク ジャカルタ ベソッ パギ ↘",
             "besok でわずかに音を立て、pagi の gi で静かに下降して息を吐き終える。"),
            ("【Yes/No疑問文・上昇調 ↗】「あなたはもうお昼ご飯を食べましたか？」",
             "Apakah Anda sudah makan siang?",
             "アパカ アンダ スダ マカン シアン？ ↗",
             "siang の -ang をキュッと高めのピッチに引き上げて疑問の意図を明確にする。"),
            ("【疑問詞疑問文・頭高下降調 ↘】「どこでそのチケットを買いましたか？」",
             "Di mana Anda membeli tiket pesawat itu?",
             "ディ マナ（高） アンダ ムンブリ ティケッ プサワッ イトゥ？ ↘",
             "Di mana を最も高く強く発音し、tiket pesawat itu は滑らかにピッチを落とす。"),
            ("【疑問詞疑問文・頭高下降調 ↘】「いつ会議が始まりますか？」",
             "Kapan rapat koordinasi ini akan dimulai?",
             "カパン（高） ラパッ コオルディナシ イニ アカン ディムライ？ ↘",
             "Kapan を高く際立たせ、語尾 dimulai は平叙文のように下降させる。"),
            ("【命令・禁止文・急降下 ⤓】「ここでタバコを吸わないでください！」",
             "Dilarang merokok di area ini!",
             "ディララン ムロコッ ディ エリア イニ！ ⤓",
             "Dilarang を力強く切り出し、ini でピタッと落として断定的な意思を示す。"),
            ("【丁寧な依頼・波状調 〜↗】「窓を開けていただけますか？」",
             "Tolong bukakan jendelanya sebentar ya.",
             "トロン ブカカン ジェンデラニャ スブンタル ヤ 〜↗",
             "Tolong を柔らかく発声し、語尾の ya を優しく上げて親愛の情を添える。"),
            ("【確認疑問文・kan ↗】「明日も来るよね？」",
             "Besok kamu datang lagi, kan?",
             "ベソッ カム ダタン ラギ、カン？ ↗",
             "kan の直前で一瞬息を整え、kan を高めのピッチで弾ませる。"),
            ("【確認疑問文・ya ↗】「忘れないでね、いい？」",
             "Jangan lupa tugasnya ya.",
             "ジャンガン ルパ トゥガスニャ ヤ？ ↗",
             "ya に甘えや念押しのトーンを乗せて上げる。"),
            ("【感嘆文・高低差 ↗↘】「わあ、なんて綺麗な景色なんでしょう！」",
             "Wah, indah sekali pemandangan di sini!",
             "ワァ（最高音）、インダ スカリ プマンダンガン ディ シニ！ ↘",
             "Wah で一気に音域の最高点に達し、感情の余韻を伴って下降する。"),
            ("【対比平叙文・二部構成 ↗/↘】「彼は来ましたが、彼女は来ませんでした」",
             "Dia sudah datang, tetapi temannya belum tiba.",
             "ディア スダ ダタン（↗ 休止）、トゥタピ トゥマンニャ ブルム ティバ（↘）",
             "datang で音をわずかに上げて文が続くことを示し、tiba で完結の下降をする。"),
            ("【選択疑問文・二重調 ↗/↘】「お茶にしますか、それともコーヒーにしますか？」",
             "Anda mau minum teh atau minum kopi?",
             "アンダ マウ ミヌム テ（↗）、アタウ ミヌム コピ（↘）？",
             "teh でピッチを上げ、最後の選択肢 kopi で下降させる（A or B の定番リズム）。"),
            ("【疑念・不審の疑問文 ↗↗】「本当に？信じられない」",
             "Masa sih? Yang benar?",
             "マサ シ？ ↗ ヤン ブナル？ ↗",
             "語尾の sih と benar を連続して高ピッチに跳ね上げる。"),
            ("【条件文の抑揚 ↗/↘】「もし雨が降ったら、私たちは出かけません」",
             "Jika hujan turun deras, kita tidak akan pergi.",
             "ジカ フジャン トゥルン ドゥラス（↗ 休止）、キタ ティダカカン プルギ（↘）",
             "条件節の末尾（deras）を軽く持ち上げ、主節でしっかりと着地する。"),
            ("【丁寧な断り・クッション調 ↘〜】「申し訳ありませんが、今は時間がありません」",
             "Maaf sekali, saat ini saya sedang tidak ada waktu.",
             "マアフ スカリ（低〜中）、サアッ イニ サヤ スダン ティダカダ ワクトゥ（低下降 ↘）",
             "申し訳なさを表すため、ピッチ全体を低めに設定してフラットに落ち着かせる。"),
            ("【総仕上げ】「お父さん、明日の朝食は何にしますか（疑問詞 ↘）？ナシゴレンにしますか（Yes/No ↗）？」",
             "Bapak, besok pagi mau sarapan apa? Mau dibuatkan nasi goreng?",
             "バパッ、ベソッ パギ マウ サラパン アパ（↘）？ マウ ディブアッカン ナシ ゴレン（↗）？",
             "疑問詞の末尾下降と、Yes/No疑問文の末尾上昇を1つの発話内で鮮やかに演じ分ける。")
        ],
        "quizzes": [
            ("疑問詞（kapan, di mana, siapa など）を用いた疑問文の文末イントネーションは？",
             ["平叙文と同様に、文末に向かって下降する（Falling）", "Yes/No 疑問文と同様に、文末を高く跳ね上げる（Rising）", "最初から最後まで完全に一定の音程を維持する"],
             "平叙文と同様に、文末に向かって下降する（Falling）",
             "疑問詞疑問文は疑問詞自体が強調されるため、文末は平叙文と同様に下降調（Falling）となります。"),
            ("「Apakah Anda sudah makan?」のような Yes/No 疑問文の文末ピッチはどうなるか？",
             ["急激に低く落とす", "文末に向かってピッチを高く引き上げる（Rising）", "ささやき声にする"],
             "文末に向かってピッチを高く引き上げる（Rising）",
             "Yes/No 疑問文は、聞き手に可否の判断を求めるため、文末を上昇調（Rising）にして疑問の意図を示します。"),
            ("接続詞「tetapi（しかし）」で繋がれる複文の前半節の文末はどう発音すべきか？",
             ["完全に文が終わったように急降下させる", "わずかにピッチを上げて（または維持して）文が継続することを示す", "息を止めて無音の時間を5秒間作る"],
             "わずかにピッチを上げて（または維持して）文が継続することを示す",
             "文がまだ続く場合（休止境界）、ピッチをわずかに保つか上げることで「まだ話が終わっていない」合図を送ります。")
        ]
    },
    {
        "id": "1190",
        "slug": "10-eliminating-katakana-bias",
        "title": "【脱カタカナ発音】日本人が無意識に子音の後に母音を挿入してしまう癖の完全矯正",
        "desc": "日本語の「子音＋母音（CV構造）」の呪縛を断ち切る。語末子音や子音結合（CC）に余計な母音 [u] や [o] を足さない調音筋肉の作り方。",
        "theory": """### 1. なぜ日本人はカタカナ発音になってしまうのか？
日本語の音節構造は、ほぼすべてが「子音＋母音（Consonant + Vowel: CV）」で構成されています（例: か ka, さ sa, と to）。子音だけで終わる「閉音節（CVC）」は「ん」と促音「っ」以外に存在しません。

このため、日本人は子音で終わる単語や子音が連続する単語を見たとき、**無意識に脳が「勝手な母音（主に [u] や [o]）」を補正して発音してしまう「母音挿入バイアス（Vowel Epenthesis）」**を抱えています。
- *film* を「フィルム（fi-lu-mu: 3音節）」にしてしまう（実際は 1音節 `[fɪlm]`）。
- *pos* を「ポスト（po-su-to）」にしてしまう。
- *bank* を「バンク（bang-ku）」にしてしまう。

### 2. インドネシア語の豊富な子音連続と語末子音
インドネシア語には、語末に立つ多種多様な子音（-p, -t, -k, -m, -n, -ng, -s, -r, -l, -h）や、外来語に由来する子音結合（str-, pr-, kl-, sp-）が多数存在します。
これらに母音を足すと、**音節数が倍増し、現地人には全く別の単語や呪文のように聞こえてしまいます**。

### 3. 脱カタカナの鉄則
1. **語末子音で息を止める**:
   - 語末の -t, -p, -k は息を破裂させず、調音位置でピタッと閉鎖して終わる。
2. **語末の -s は「スッ」と息の摩擦音だけで終わる**:
   - 母音 u を足して「ス（su）」にしない。唇を丸めず、歯の間から「s---」と息だけを漏らす。
3. **子音結合（pr-, tr-）は一息で弾く**:
   - *praktis* を「プラクティス（pu-ra-ku-ti-su: 5音節）」ではなく、「prak-tis（2音節）」として発音する。""",
        "drills": [
            ("【語末 s の摩擦音】「美味しいご飯（nasi）、美味しいジュース（jus）」",
             "Tolong segelas jus jeruk dingin tanpa gula.",
             "トロン スグラス ジュス（sの息だけ） ジェルッ ディンギン タンパ グラ。",
             "jus は「ジュース」と伸ばさず、jus [dʒus] で s の息をスーッと出して止める。"),
            ("【語末 s の摩擦音】「熱い紅茶（teh panas）」",
             "Saya ingin minum secangkir teh panas.",
             "サヤ インギン ミヌム スチャンキル テ パナス（sの息だけ）。",
             "panas は「パナス（su）」ではなく、na の後に s の摩擦音だけを添える。"),
            ("【子音結合 pr-】「この方法は非常に実践的（praktis）です」",
             "Metode pembelajaran ini terbukti sangat praktis.",
             "メトデ プンブラジャラン イニ トゥルブクティ サンガッ プラクティス。",
             "praktis は「プ・ラ・ク・ティ・ス」ではなく、[prak-tis] の2音節。"),
            ("【子音結合 str-】「会社の戦略（strategi）を見直す」",
             "Kita perlu menyusun strategi pemasaran yang baru.",
             "キタ プルル ムニュスン ストラテギ（stra-te-gi） プマサラン ヤン バル。",
             "strategi を「ス・ト・ラ・テ・ギ」と5拍にせず、stra- を1音節で一気に発音。"),
            ("【語末 l の閉鎖】「ホテルのロビー（lobi hotel）で待ち合わせる」",
             "Mari kita bertemu di lobi hotel pada jam dua siang.",
             "マリ キタ ブルトゥム ディ ロビ ホテル（lで舌を歯茎につけて止める）。",
             "hotel は「ホテル（ru）」ではなく、語末 l で舌先を上の歯茎につけて音を止める。"),
            ("【語末 l の閉鎖】「高価な（mahal）宝石」",
             "Barang antik ini harganya sangat mahal.",
             "バラン アンティッ イニ ハルガニャ サンガッ マハル（lで止める）。",
             "mahal を「マハル（ru）」と母音で終わらせない。"),
            ("【外来語の閉音節】「映画（film）を見に行く」",
             "Malam minggu ini kami berencana menonton film di bioskop.",
             "マラム ミング イニ カミ ブルンチャナ ムノントン フィルム（film） ディ ビオスコップ。",
             "film は「フィ・ル・ム」の3拍ではなく、film の1音節。l から m への速やかな移行。"),
            ("【外来語の閉音節】「銀行（bank）でお金を下ろす」",
             "Saya harus pergi ke bank untuk mengambil uang tunai.",
             "サヤ ハルス プルギ ク バンク（bank） ウントゥッ ムンガンビル ウアン トゥナイ。",
             "bank を「バンク（bang-ku）」にしない。語末 k を閉じて終わる。"),
            ("【語末 h の呼気】「まだ（masih）雨が降っている」",
             "Di luar masih hujan deras dan berangin kencang.",
             "ディ ルアル マシッ（hの息抜け） フジャン ドゥラス ダン ブルアンギン クンチャン。",
             "masih は「マシ」ではなく、最後に喉から「ハー」と息をわずかに抜く。"),
            ("【語末 h の呼気】「きれいな（bersih）水を使う」",
             "Gunakan air yang bersih untuk mencuci sayuran.",
             "グナカン アイル ヤン ブルシッ（hの息抜け） ウントゥッ ムンチュチ サユラン。",
             "bersih を日本語の「ベルシ」で終わらせず、末尾の気流（無声声門摩擦音）を感じさせる。"),
            ("【子音結合 kl-】「エアコン（AC / pendingin ruangan / klub）」",
             "Dia menjadi anggota klub olahraga di kampusnya.",
             "ディア ムンジャディ アンゴタ クラブ（klub） オラフラガ ディ カンプスニャ。",
             "klub を「ク・ラ・ブ」と発音せず、kl- を同時に調音して短く発声。"),
            ("【語末 t の無開放】「夜遅く（larut malam）まで働く」",
             "Jangan bekerja sampai larut malam, jaga kesehatan.",
             "ジャンガン ブルクルジャ サンパイ ラルッ（tで止める） マラム、ジャガ クセハタン。",
             "larut は「ラルト（to）」ではなく、舌先を歯茎につけて息を遮断する。"),
            ("【語末 p の無開放】「屋根（atap）の修理をする」",
             "Pekerja sedang memperbaiki atap rumah yang bocor.",
             "プクルジャ スダン ムンプルバイキ アタッ（pで口を閉じる） ルマ ヤン ボチョル。",
             "atap は「アタップ（pu）」ではなく、唇を閉じて音を止める。"),
            ("【カタカナ vs ネイティブ比較】「ポスト（pos）、カード（kartu）、手紙（surat）」",
             "Saya mengirim surat dan kartu pos melalui kantor pos.",
             "サヤ ムンギリム スラッ ダン カルトゥ ポス（s息） ムラルイ カントル ポス。",
             "kantor pos を「カン・トル・ポ・ス・ト」とせず、kan-tor pos と引き締める。"),
            ("【総仕上げ】「ホテル（hotel）の近くの銀行（bank）で、実践的な（praktis）戦略（strategi）について映画（film）を見ながら話す」",
             "Di dekat hotel, kami membahas strategi praktis di bank sambil menonton film.",
             "ディ ドゥカッ ホテル、カミ ムンバハス ストラテギ プラクティス ディ バンク サンビル ムノントン フィルム。",
             "カタカナ化しやすい全単語（hotel, strategi, praktis, bank, film）から余計な母音を完璧に削ぎ落とす。")
        ],
        "quizzes": [
            ("日本人が「film」を「フィルム（fi-lu-mu）」のように発音してしまう言語学的理由は？",
             ["インドネシア語の正式な発音ルールがそう指定しているから", "日本語の母語干渉により、子音の後に無意識に母音を補正・挿入してしまうため", "film という単語が元々3音節の単語だから"],
             "日本語の母語干渉により、子音の後に無意識に母音を補正・挿入してしまうため",
             "日本語のCV（子音＋母音）構造の癖により、子音単独の音節に母音（uやo）を足してしまう母語干渉（Epenthesis）です。"),
            ("単語「jus」や「panas」の語末にある「-s」の自然な発音法は？",
             ["日本語の「ス」のように母音 u を唇を丸めて発音する", "母音を一切含めず、歯の間から「s---」と息の摩擦音だけを出して終わる", "s を完全に発音せず省略する"],
             "母音を一切含めず、歯の間から「s---」と息の摩擦音だけを出して終わる",
             "語末の s は無声歯茎摩擦音であり、母音 u を足さずに息の摩擦音だけで抜くのが自然です。"),
            ("「praktis」をネイティブのように流暢に発音するための音節感覚は？",
             ["「プ・ラ・ク・ティ・ス」の5音節（5拍）", "「prak-tis」の2音節（2拍）", "「プ・ラク・ティス」の3音節"],
             "「prak-tis」の2音節（2拍）",
             "子音結合 pr- と語末 -s を母音なしで調音することで、自然な2音節 [prak-tis] として引き締まります。")
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
    lines.append("## 2. 実践調音・シャドーイング集中ドリル15選")
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
