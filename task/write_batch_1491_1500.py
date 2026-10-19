# -*- coding: utf-8 -*-
"""
セクション35 第5バッチ (1491-1500) 記事生成スクリプト
【表現技法】プロの翻訳・通訳・高度表現テクニック
高度文体論・修辞学・AIポストエディット・QA用語集・倫理・大団円翻訳批評
全1,500記事 完結記念バッチ！
"""

import os

articles = [
    {
        "filename": "41-stylistics-formal-academic-register.md",
        "title": "1491. 高度文体論：公式報告書・論文における端正な学術的文体の構築",
        "level": "プロ翻訳者・研究者・文体論専攻（CEFR C1〜C2）",
        "intro": "最高峰のインドネシア語文章に共通するのは、単なる文法的正しさ（gramatikal）を超えた「格調ある学術的文体（Register Formal / Laras Ilmiah）」の統一感です。主観の完全な排除、緻密な名詞化構文（Nominalisasi）、論理的一貫性を保つ結束性（Kohesi dan Koherensi）により、知性と権威を感じさせる文章を構築する技術を解き明かします。",
        "theory": [
            ("端正な学術文体を創出する3大技法",
             "1. **名詞化構文（Nominalisasi）による凝縮**: \n"
             "   - 動詞の連続文を格調高い名詞句に圧縮する。\n"
             "   - 俗文: \"Ketika pemerintah menaikkan harga BBM, masyarakat menjadi resah...\"\n"
             "   - 端正文: \"**Kenaikan harga BBM memicu keresahan sosio-ekonomi masyarakat.**\"\n"
             "2. **三人称・客観的受動構文の徹底**: \n"
             "   - 「Kami berpendapat」を排し、「**Berdasarkan data empiris di atas, dapat diargumentasikan bahwa...**」と学術的距離を置く。\n"
             "3. **精密な抽象接続語（Penanda Transisi Akademik）の活用**: \n"
             "   - 補足: *Lebih lanjut*, *Sejalan dengan premis tersebut*.\n"
             "   - 対比: *Sebaliknya*, *Dalam konteks yang kontras*.\n"
             "   - 帰結: *Konsekuensinya*, *Dengan demikian*.")
        ],
        "problems": [
            {
                "q": "【学術文体推敲問題】「政府が税金を上げたので、国民は怒ってデモをやった。」という平易な文章を、最高峰の社会科学論文の文体へリライトしたものとして最も適切なものはどれか？",
                "options": [
                    "A. Kebijakan penyesuaian tarif pajak oleh pemerintah memantik gelombang demonstrasi penolakan dari masyarakat luas.",
                    "B. Kenaikan pajak pemerintah bikin masyarakat marah-marah lalu jalan di jalanan demo.",
                    "C. Rakyat sangat marah sekali karena pajak dinaikkan presiden lalu demonstrasi ramai.",
                    "D. Lantaran pajak naik tinggi, orang-orang pada kumpul demo protes aturan tadi."
                ],
                "ans": "A. Kebijakan penyesuaian tarif pajak oleh pemerintah memantik gelombang demonstrasi penolakan dari masyarakat luas.",
                "expl": "「Kebijakan penyesuaian tarif pajak（税率調整政策）」「memantik gelombang demonstrasi（デモの波を点火・誘発した）」という名詞化と高度学術語彙で端正にまとめられたAが最高峰の学術文体です。"
            }
        ],
        "table": [
            ("memantik gelombang penolakan", "反発・拒絶の波を誘発する・点火する"),
            ("keresahan sosio-ekonomi", "社会経済的不安・動揺"),
            ("dapat diargumentasikan bahwa...", "〜であると論証・主張することができる"),
            ("sejalan dengan premis tersebut", "その前提と軌を一にして・整合して"),
            ("nominalisasi", "名詞化（動詞を抽象名詞句へ圧縮する技法）"),
            ("kohesi dan koherensi", "文章の結束性と首尾一貫性")
        ],
        "pro_tip": "知的な文章を書く秘訣は「動詞でダラダラ繋がず、名詞句でスパッと切る（名詞化）」ことです。これにより文章の密度が2倍になり、説得力が飛躍的に高まります。"
    },
    {
        "filename": "42-stylistics-persuasive-rhetoric.md",
        "title": "1492. 高度文体論：説得力と扇情性を高める修辞的レトリック（反復・対句・誇張）",
        "level": "スピーチライター・広報責任者（CEFR C1〜C2）",
        "intro": "人の心を揺さぶり、大衆を行動へと駆り立てる言葉には、計算し尽くされた「修辞的レトリック（Gaya Bahasa / Majas Retorika）」が組み込まれています。スカルノ大統領の伝説的演説から現代のトップリーダーのスピーチまで、反復（Anafora）、対句（Antitesis）、頭韻（Aliterasi）を駆使したインドネシア語の美しき雄弁術を伝授します。",
        "theory": [
            ("リーダーが愛用する3大修辞技法",
             "1. **文頭反復（Anafora）による感情の昂揚**: \n"
             "   - 同じ単語を行頭で畳み掛ける。\n"
             "   - \"**Bukan untuk** kepentingan pribadi, **bukan untuk** golongan tertentu, **melainkan untuk** kejayaan seluruh rakyat Indonesia!\"\n"
             "2. **対立概念の対比（Antitesis）による鮮烈なコントラスト**: \n"
             "   - 対義語を左右に配置して主題を際立たせる。\n"
             "   - \"Jangan tanyakan apa yang **diberikan bangsa kepadamu**, tanyakanlah apa yang telah **kamu baktikan bagi bangsamu**.\"\n"
             "3. **三部構成（Tricolon / Aturan Tiga）の心地よいリズム**: \n"
             "   - 3つの要素をテンポよく並べる。「Bekerja keras, berpikir cerdas, berintegritas tuntas.」")
        ],
        "problems": [
            {
                "q": "【修辞技法演習】次の格調高いスピーチの一節で用いられている主な修辞技法（Gaya Bahasa）はどれか？\n\"Kita tidak boleh gentar menghadapi badai, kita tidak boleh mundur selangkah pun, kita tidak boleh menyerah pada takdir!\"",
                "options": [
                    "A. Anafora（文頭反復技法：Kita tidak boleh...の畳み掛け）",
                    "B. Litotes（謙遜・過小評価技法）",
                    "C. Pleonasme（不要な重複表現技法）",
                    "D. Eufemisme（婉曲オブラート表現技法）"
                ],
                "ans": "A. Anafora（文頭反復技法：Kita tidak boleh...の畳み掛け）",
                "expl": "同一の句「Kita tidak boleh（私たちは決して〜してはならない）」を3回連続して文頭に配置し、聴衆の決意と情熱を鼓舞する古典的修辞技法「Anafora（アナフォラ・首句反復）」です。"
            }
        ],
        "table": [
            ("Anafora", "首句反復（文頭に同一語句を繰り返す修辞）"),
            ("Antitesis", "対句法・対照法（対立概念を対比させる修辞）"),
            ("Tricolon", "三部構成法（3つの要素でリズムを作る技法）"),
            ("majas penegas", "強調修辞技法（説得力を高めるレトリック）"),
            ("menggentarkan hati", "心を揺さぶる・畏怖させる"),
            ("retorika persuasif", "説得的修辞学（Persuasive Rhetoric）")
        ],
        "pro_tip": "プレゼンテーションや演説の結びでは、「3拍子（Tricolon）」でキーワードを提示すると、聴衆の耳に最も心地よく残り、スタンディングオベーションを引き出すことができます。"
    },
    {
        "filename": "43-stylistics-irony-satire-humor.md",
        "title": "1493. 高度文体論：アイロニーと風刺の解読と産出：行間に潜むユーモアのニュアンス",
        "level": "文芸批評家・上級ジャーナリスト（CEFR C1〜C2）",
        "intro": "インドネシアの言論・文学・SNS空間において、最も知的な破壊力を持つのが「反語（Ironi）」「風刺（Satire）」「ブラックユーモア（Sarkasme）」です。表面上は褒めているようで実は強烈な社会批判が込められた行間のニュアンス（Makna Tersirat）を解読し、自らも洗練されたエスプリを生み出す高等技法を考察します。",
        "theory": [
            ("アイロニー・風刺の3段階グラデーション",
             "1. **優雅な皮肉（Ironi）**: \n"
             "   - 言葉の表面と真意が真逆。上品な嘲笑。\n"
             "   - \"Bagus sekali kinerjamu, sampai-sampai kantor kita rugi miliaran rupiah.\"（実に素晴らしい仕事ぶりだ、おかげで我が社は数十億の赤字だよ）。\n"
             "2. **辛辣な嘲罵（Sarkasme）**: \n"
             "   - 容赦のない直接的なトゲ。\n"
             "   - \"Apakah otakmu tertinggal di rumah saat menghadiri rapat penting ini?\"\n"
             "3. **知的社会風刺（Satire）**: \n"
             "   - コメディや寓話、比喩を通じて権力や社会の矛盾を突く。\n"
             "   - 「Koruptor kita memang paling dermawan, membagikan uang rakyat kepada sanak saudaranya sendiri.」")
        ],
        "problems": [
            {
                "q": "【行間読解演習】政治コラムに「Wakil rakyat kita sangat rajin berkunjung ke luar negeri untuk studi banding, saking rajinnya hingga lupa mengesahkan rancangan undang-undang yang dinanti rakyat.」とある。筆者の真意はどれか？",
                "options": [
                    "A. 国会議員が海外視察にかまけて法案審議を放棄していることを、反語（Ironi）を用いて痛烈に批判している。",
                    "B. 国会議員の勤勉な海外研修の成果を純粋に賞賛し、国民に感謝を呼びかけている。",
                    "C. 海外視察の予算が不足しているため、法案審議を優先すべきだと提言している。",
                    "D. 国民が法案を待っていないため、議員が海外に避難したという事実を報告している。"
                ],
                "ans": "A. 国会議員が海外視察にかまけて法案審議を放棄していることを、反語（Ironi）を用いて痛烈に批判している。",
                "expl": "「saking rajinnya（あまりに勤勉すぎて）」という褒め言葉の形を借りて、「国民が待望する法案の成立を忘れている」という職務怠慢を鋭く風刺（Satire / Ironi）しています。"
            }
        ],
        "table": [
            ("makna tersirat", "言外の意味・行間に隠されたニュアンス"),
            ("studi banding", "視察研修・比較研究（時に「税金旅行」の隠語）"),
            ("satire politik", "政治風刺"),
            ("humor intelektual", "知的なユーモア・エスプリ"),
            ("majas sindiran", "風刺・皮肉修辞技法"),
            ("berlidah tajam", "毒舌の・言葉が鋭い")
        ],
        "pro_tip": "インドネシアの知識層（Tempo誌など）の記事を読む際は、「Bagus」「Hebat」「Luar biasa」が文脈の中で『真逆の皮肉』として使われていないか常に警戒する審美眼が必要です。"
    },
    {
        "filename": "44-stylistics-euphemism-taboo.md",
        "title": "1494. 高度文体論：婉曲表現（Eufemisme）の美学：死・病・金銭・失敗を品良く語る",
        "level": "外交官・広報責任者・上級学習者（CEFR C1〜C2）",
        "intro": "インドネシア社会は「調和（Kerukunan）」と「礼節（Kesantunan）」を至上命題とする高コンテキスト文化です。死、病気、貧困、解雇、身体障害などの重い現実を、角を立てず品格を保ってオブラートに包む『婉曲表現（Eufemisme）』は、大人のインドネシア語の教養の証です。その精緻な語彙体系をマスターします。",
        "theory": [
            ("領域別・公用婉曲表現（Eufemisme）の対照表",
             "1. **死（Kematian）**: \n"
             "   - mati / tewas（粗野） → **meninggal dunia** / **berpulang ke rahmatullah**（召される） / **tutup usia**（天寿を全うする）。\n"
             "2. **貧困・困窮（Kemiskinan）**: \n"
             "   - orang miskin（直截） → **masyarakat prasejahtera**（前福祉層） / **keluarga kurang mampu**。\n"
             "3. **身体的ハンディキャップ（Disabilitas）**: \n"
             "   - buta（盲目） → **tunanetra** / tuli（聾） → **tunarungu** / cacat（障害） → **penyandang disabilitas**。\n"
             "4. **解雇・失業（PHK）**: \n"
             "   - dipecat（クビ） → **dirumahkan**（自宅待機） / **diberhentikan dengan hormat**（依願退職）。\n"
             "5. **物価・料金の値上げ**: \n"
             "   - kenaikan harga → **penyesuaian tarif**（料金の適正化・調整）。")
        ],
        "problems": [
            {
                "q": "【婉曲表現選択問題】公的プレスリリースにおいて「当社は業績悪化に伴い、やむを得ず貧困家庭の従業員を解雇した」を、最も品格高く人権と社会規範に配慮してリライトしたものはどれか？",
                "options": [
                    "A. Sehubungan dengan rasionalisasi bisnis, Perusahaan terpaksa melakukan perampingan organisasi terhadap sebagian karyawan dari kelompok masyarakat kurang mampu.",
                    "B. Karena toko mau bangkrut, kami pecat orang-orang miskin yang kerja di sini.",
                    "C. Perusahaan memberhentikan orang cacat dan orang susah sebab tidak ada uang gaji.",
                    "D. Lantaran rugi banyak, majikan buang buruh-buruh yang tidak punya uang makan."
                ],
                "ans": "A. Sehubungan dengan rasionalisasi bisnis, Perusahaan terpaksa melakukan perampingan organisasi terhadap sebagian karyawan dari kelompok masyarakat kurang mampu.",
                "expl": "「業績悪化 → rasionalisasi bisnis」「解雇 → perampingan organisasi（組織のスリム化）」「貧困層 → masyarakat kurang mampu」という最高水準の公用婉曲表現でまとめられたAが模範です。"
            }
        ],
        "table": [
            ("tutup usia / berpulang", "逝去する・他界する（死の婉曲）"),
            ("masyarakat prasejahtera", "生活困窮層・低所得層（貧困の婉曲）"),
            ("penyandang disabilitas", "障がい者（身体の婉曲）"),
            ("penyesuaian tarif", "料金・価格の改定・調整（値上げの婉曲）"),
            ("perampingan organisasi", "組織再編・人員適正化（解雇の婉曲）"),
            ("kesantunan berbahasa", "言語的礼節・ポライトネス（Politeness）")
        ],
        "pro_tip": "インドネシアの公文書で「penyesuaian tarif（料金調整）」と書かれていたら、100%「値上げ（kenaikan tarif）」を意味します。社会的反発を和らげる行政の定番Eufemismeです。"
    },
    {
        "filename": "45-stylistics-archaisms-court-style.md",
        "title": "1495. 高度文体論：古風・宮廷風文体の活用：格調ある歴史的重みの付与",
        "level": "文芸翻訳者・歴史・古典研究者（CEFR C1〜C2）",
        "intro": "歴史小説、宮廷劇、叙事詩、伝統儀礼のスピーチでは、現代標準語だけでは醸し出せない「歴史の重厚感と王者の威厳」を表現するために、宮廷語（Bahasa Keraton）や古風語（Kata Arkais）が巧みに用いられます。ジョグジャカルタやソロの王室伝統、古代マタラム・マジャパヒトの息吹を現代文に吹き込む文体技法を学びます。",
        "theory": [
            ("宮廷風文体（Bahasa Istana / Keraton）の重要語彙群",
             "1. **王と王族の行為**: \n"
             "   - 王の命令（titah / sabda baginda） ⇔ 臣下の伺い（sembah hamba）。\n"
             "   - 王の怒り（murka） ⇔ 王の慈悲（kurnia / karunia）。\n"
             "   - 滞在・御座す（bersemayam di atas takhta）。\n"
             "   - 巡幸・行幸（berangkat / mangkat: 王の崩御）。\n"
             "2. **古風な人称体系**: \n"
             "   - 臣下が王に対する一人称: **Patek / Hamba / Sahaya**（僕・臣）。\n"
             "   - 王に対する二人称: **Tuanku / Duli Tuanku**（陛下・主上）。\n"
             "3. **文語的装飾詞（Partikel Arkais）**: \n"
             "   - gerangan（一体〜であろうか: \"Siapakah gerangan orang itu?\"）。\n"
             "   - alangkah（なんと〜であろうか）。")
        ],
        "problems": [
            {
                "q": "【宮廷語翻訳演習】歴史劇のセリフ「王様、臣下の申し上げますことを何卒お聞き届けください。」の最も格調高い宮廷語訳はどれか？",
                "options": [
                    "A. \"Ampun Tuanku, perkenankanlah hamba menyampaikan sembah puji ke hadapan Duli Baginda.\"",
                    "B. \"Halo Raja, tolong dengar omongan saya ya, ini penting banget.\"",
                    "C. \"Hei bos besar, saya mau bicara tolong dengarkan baik-baik ya.\"",
                    "D. \"Tuan Presiden, kami minta waktu bicara sebentar di depan Anda.\""
                ],
                "ans": "A. \"Ampun Tuanku, perkenankanlah hamba menyampaikan sembah puji ke hadapan Duli Baginda.\"",
                "expl": "「Ampun Tuanku（陛下、ご容赦を）」「hamba（臣）」「sembah（拝謁の言葉）」「Duli Baginda（主上）」という完全な宮廷語（Bahasa Istana）の語彙体系に合致しているのはAのみです。"
            }
        ],
        "table": [
            ("titah baginda", "王の仰せ・勅命・詔（Royal Decree）"),
            ("mangkat", "王が崩御する（王族の死）"),
            ("bersemayam", "王座に御座す・鎮座する"),
            ("murka", "王が激怒する・怒り狂う"),
            ("hamba / patek", "臣・下僕（王に対する一人称）"),
            ("siapakah gerangan...", "一体誰であろうか（文語的疑問）")
        ],
        "pro_tip": "日常会話で「mangkat（崩御）」や「titah（勅命）」を使うと滑稽ですが、歴史物や伝統文化行事の通訳・翻訳では、これらを正確に用いることで作品の品格が一瞬で跳ね上がります。"
    },
    {
        "filename": "46-ai-translation-post-editing-mtpe.md",
        "title": "1496. AI翻訳時代における機械翻訳ポストエディット（MTPE）の実践",
        "level": "プロ翻訳者・ランゲージスペシャリスト（CEFR C1〜C2）",
        "intro": "ChatGPTやDeepLなどのニューラル機械翻訳（NMT）や生成AIが普及した現代、プロ翻訳者に最も求められているのはゼロからの翻訳ではなく「AI生成訳文の誤謬を瞬時に見抜き、完璧な公用文へ磨き上げるポストエディット（MTPE: Machine Translation Post-Editing）」能力です。AIの典型的弱点（ハルシネーション、用語の不統一、文化的不適合）を外科手術のように修正する技術を確立します。",
        "theory": [
            ("ライトPE（Light PE） vs フルPE（Full PE）の基準",
             "1. **ライトPE（Light Post-Editing）**: \n"
             "   - 社内情報把握目的。文法エラーと致命的誤訳（Mistranslation）のみを修正し、文体の洗練度は追求しない。\n"
             "2. **フルPE（Full Post-Editing）**: \n"
             "   - 出版・契約・公式開示用。人手翻訳（Human Translation）と同等の完全無欠な品質を保証する。\n"
             "3. **AI翻訳が最も引き起こしやすい3大トラップ**: \n"
             "   - **用語のブレ（Inconsistency）**: 同一文書内で「董事長」が Direktur と Presiden Komisaris に揺れる。\n"
             "   - **受動態の乱用**: 日本語の「〜された」を直訳して di- を不自然に連発する。\n"
             "   - **幻覚（Hallucination）**: 原文にない数字や否定語（tidak）を勝手に出力・欠落させる。")
        ],
        "problems": [
            {
                "q": "【MTPE実践演習】\n原文: 「本協定は、双方の署名の日から効力を発する。」\nAIの初期出力: *\"Perjanjian ini mulai berlaku dari hari penandatanganan kedua belah pihak.\"*\nプロ翻訳者としてフルPE（最高品質修正）を施した訳文はどれか？",
                "options": [
                    "A. \"Perjanjian ini mulai berlaku pada tanggal ditandatanganinya oleh Para Pihak.\"",
                    "B. \"Perjanjian ini jalan terus dari tanggal kedua orang tanda tangan bersama.\"",
                    "C. \"Surat ini sah mulai hari ketika dua pihak menulis nama mereka.\"",
                    "D. \"Perjanjian ini aktif sejak hari ditandatangani oleh semuanya.\""
                ],
                "ans": "A. \"Perjanjian ini mulai berlaku pada tanggal ditandatanganinya oleh Para Pihak.\"",
                "expl": "AIの拙い直訳（dari hari... kedua belah pihak）を、契約書公用文の厳格な定型句「pada tanggal ditandatanganinya oleh Para Pihak（両当事者により署名された日をもって発効する）」へ完璧にブラッシュアップしたAが模範的なフルPEです。"
            }
        ],
        "table": [
            ("Machine Translation Post-Editing (MTPE)", "機械翻訳ポストエディット"),
            ("Light Post-Editing (LPE)", "ライト・ポストエディット（最低限の誤り修正）"),
            ("Full Post-Editing (FPE)", "フル・ポストエディット（人手翻訳同等品質化）"),
            ("halusinasi AI", "AIのハルシネーション（もっともらしい事実無根の出力）"),
            ("inkonsistensi terminologi", "用語の不統一・表記揺れ"),
            ("kelancaran bahasa (fluency)", "訳文の流暢さ・自然さ")
        ],
        "pro_tip": "MTPE作業で最も重要なのは「数字の照合（Number Check）」です。AIは文脈が流暢であればあるほど、数字（桁や日付）のすり替わりに気づきにくいため、数字だけを目視で徹底突合してください。"
    },
    {
        "filename": "47-translation-quality-assurance-qa.md",
        "title": "1497. プロの翻訳チェック・品質保証（QA）手順とチェックリスト",
        "level": "翻訳チェッカー・プロジェクトマネージャー（CEFR C1〜C2）",
        "intro": "プロフェッショナルな翻訳会社（LSP: Language Service Provider）や多国籍企業において、翻訳成果物を納品・公開する前に実施される厳格な「品質保証プロセス（QA: Quality Assurance）」。タイポ、訳抜け、数字ミス、フォント不一致などのヒューマンエラーをゼロにする多層防御チェックリストを体系化します。",
        "theory": [
            ("プロ翻訳QAの5大ステップ・プロトコル",
             "1. **第1層: 訳抜け・欠落チェック（Completeness Check）**: \n"
             "   - 段落、箇条書き、図表のキャプション、ヘッダー・フッターに訳抜けがないか原文と対照。\n"
             "2. **第2層: 数字・固有名詞・記号の機械的突合（Fact-checking）**: \n"
             "   - 100%の数字突合（桁数、コンマとピリオドの正書法: 1.000 vs 1,000）。\n"
             "3. **第3層: 用語集（Glossary）適合性検証**: \n"
             "   - クライアント指定用語（Klien-mandated terms）が厳密に守られているか。\n"
             "4. **第4層: バイリンガル校正（Bilingual Editing）**: \n"
             "   - 意味の歪み、主客の取り違え、不自然な訳読の是正。\n"
             "5. **第5層: モノリンガル素読み（Monolingual Proofreading）**: \n"
             "   - 原文を見ずに訳文だけを通読し、母国語として完璧に自然か検証する。")
        ],
        "problems": [
            {
                "q": "【QA検証問題】インドネシア語の契約書を校正中、財務金額「Rp 10.000.000,00」という記載を見つけた。インドネシアの正書法（EYD 5）および会計基準に照らし、この表記の正誤判定として正しいものはどれか？",
                "options": [
                    "A. 正しい。インドネシア語では千の位の区切りにピリオド（.）を用い、小数点以下にコンマ（,）を用いる。",
                    "B. 誤り。英語や日本語と同様に、千の位はコンマ（,）で区切り、小数はピリオド（.）にすべきである。",
                    "C. 誤り。ルピア記号（Rp）の後ろに必ずスペースを空けなければならない。",
                    "D. 誤り。数字の後ろに「Rupiah」と文字で書かないと法律上無効である。"
                ],
                "ans": "A. 正しい。インドネシア語では千の位の区切りにピリオド（.）を用い、小数点以下にコンマ（,）を用いる。",
                "expl": "インドネシア語（EYD 5）では、オランダ式・大陸欧州式に従い、3桁区切りにピリオド「.」を用い、小数の区切りにコンマ「,」を用います（例: 10.000.000,00＝一千万ルピア）。英米式と逆であるため、QAチェッカーの最重要点検ポイントです。"
            }
        ],
        "table": [
            ("penjaminan mutu (QA)", "品質保証（Quality Assurance）"),
            ("penyuntingan dwibahasa", "二言語対訳校正（Bilingual Editing）"),
            ("uji keterbacaan (proofreading)", "素読み校正・通読チェック"),
            ("titik ribuan dan koma desimal", "千の位のピリオドと小数点のコンマ（正書法）"),
            ("omisi / bagian terlewat", "訳抜け・脱落（Omission）"),
            ("daftar istilah wajib (mandatory glossary)", "必須用語集")
        ],
        "pro_tip": "数字のピリオドとコンマの反転（1.500 = 千五百 / 1,5 = 一点五）は、日本人翻訳者が最もミスしやすい罠です。納品前の数字検索マクロで必ず一括抽出チェックを行ってください。"
    },
    {
        "filename": "48-building-personal-termbase-glossary.md",
        "title": "1498. 通訳・翻訳者のための個人用語集（Termbase）構築とCATツール活用",
        "level": "プロ翻訳者・通訳者・情報アーキテクト（CEFR C1〜C2）",
        "intro": "プロ翻訳者・通訳者の最大の知的資産（Intellectual Asset）は、長年の実務経験を通じて蓄積された「個人用語集（Personal Termbase / Glosarium Pribadi）」と「翻訳メモリ（Translation Memory: TM）」です。Trados, memoQ, Phrase などのCATツール（翻訳支援ツール）を自在に操り、検索スピード0.1秒の用語データベースを構築・保守する技術を解説します。",
        "theory": [
            ("プロの用語集（Termbase）データ構造設計",
             "1. **最小必須フィールド設計**: \n"
             "   - `Term ID`: 一意の識別子。\n"
             "   - `Japanese`: 原語（例: 債務不履行）。\n"
             "   - `Indonesian`: 確定定訳（例: wanprestasi）。\n"
             "   - `English`: 英語対照（例: default / breach of contract）。\n"
             "   - `Domain`: 分野（例: Hukum Kontrak）。\n"
             "   - `Context / Example`: 実際の条文用例。\n"
             "   - `Forbidden Term`: 使用禁止語（例: tidak boleh memakai 'cidra janji' dalam kontrak ini）。\n"
             "2. **同義語のランク付け**: \n"
             "   - 優先語（Preferred Term）と許容語（Admitted Term）を明確に区別して登録する。\n"
             "3. **通訳現場での瞬時検索環境**: \n"
             "   - タブレットやサブPCでのインクリメンタルサーチ（1文字打つごとに候補が絞り込まれるツール）の構築。")
        ],
        "problems": [
            {
                "q": "【用語集管理問題】多人数で翻訳プロジェクトを進める際、用語集（Termbase）に「禁止用語（Forbidden Term）」フィールドを設ける主たる目的はどれか？",
                "options": [
                    "A. 直訳や日常会話的な不適切な表現、またはクライアントが明確に拒絶した旧訳語の混入を機械的・組織的に防ぐため。",
                    "B. 翻訳者のタイピング速度を測定するため。",
                    "C. 辞書の項目数を減らしてファイルサイズを小さくするため。",
                    "D. 翻訳料金の計算を自動化するため。"
                ],
                "ans": "A. 直訳や日常会話的な不適切な表現、またはクライアントが明確に拒絶した旧訳語の混入を機械的・組織的に防ぐため。",
                "expl": "「禁止用語（Forbidden Term / Blacklist）」を指定することで、CATツールが誤用を自動検出し、クライアント指定に反する不適切訳語の混入を未然に遮断します。"
            }
        ],
        "table": [
            ("pangkalan istilah (termbase)", "用語ベース・用語集データベース"),
            ("memori terjemahan (Translation Memory: TM)", "翻訳メモリ（過去訳文の対訳DB）"),
            ("istilah pilihan (preferred term)", "優先用語・推奨訳語"),
            ("istilah terlarang (forbidden term)", "禁止用語・使用禁止訳語"),
            ("alat CAT (Computer-Assisted Translation)", "翻訳支援ツール（Trados, memoQ等）"),
            ("pencarian inkremental", "インクリメンタル検索（逐次絞り込み検索）")
        ],
        "pro_tip": "用語集は「単語＋訳語」のペアだけで登録してはいけません。必ず「前後3語のコロケーション（共起動詞・前置詞）」と「分野タグ」をセットで登録して初めて、現場で即戦力になります。"
    },
    {
        "filename": "49-professional-code-of-ethics-interpreter.md",
        "title": "1499. 通訳者・翻訳者の国際職業倫理規定：守秘義務と専門的誠実さ",
        "level": "プロ通訳者・実務翻訳者・AIIC/HPI会員（全言語専門家対象）",
        "intro": "言語の職人である通訳者・翻訳者が、多国籍企業、国家機関、裁判所から絶対的な信頼を勝ち得るための根幹にあるのが「職業倫理規定（Kode Etik Profesi / Code of Professional Ethics）」です。国際会議通訳者連盟（AIIC）やインドネシア翻訳者協会（HPI: Himpunan Penerjemah Indonesia）の国際基準に準拠した、守秘義務、利益相反の回避、中立性の倫理を学びます。",
        "theory": [
            ("国際通訳・翻訳者の4大倫理義務（AIIC / HPI 基準）",
             "1. **絶対的守秘義務（Kerahasiaan Mutlak）**: \n"
             "   - 業務上知り得た機密情報（M&A情報、未公開決算、個人情報）は、契約終了後も生涯にわたり第三者への漏洩・自己の利益利用を固く禁じる（インサイダー取引の厳禁）。\n"
             "2. **忠実性と正確性（Fidelitas & Akurasi）**: \n"
             "   - 自己の思想・信条・好悪を差し挟まず、原発話者の意図、ニュアンス、感情のトーンを忠実に母国語へ再現する。\n"
             "3. **能力の限界の開示（Kompetensi Profesional）**: \n"
             "   - 自己の能力や準備時間を超える専門外の案件は、無責任に引き受けず辞退するか、事前の専門資料開示を誠実に要求する。\n"
             "4. **利益相反の回避と中立性（Netralitas & Konflik Kepentingan）**: \n"
             "   - 紛争当事者の双方と利害関係がある場合は即座に開示し、中立な第三者としての立場を死守する。")
        ],
        "problems": [
            {
                "q": "【職業倫理ケーススタディ】通訳中、ある上場企業の未発表M&A交渉を担当した通訳者が、会議終了後に知人に「あの会社、近々買収されるから株を買っておいた方がいいよ」と漏らした。この行為の倫理的・法的判断として正しいものはどれか？",
                "options": [
                    "A. 職業倫理規定における絶対的守秘義務に明白に違反するだけでなく、金融商品取引法上のインサイダー取引（insider trading）として刑事罰の対象となる重大な違法行為である。",
                    "B. 知人に親切で教えただけなので、金銭を受け取っていなければ倫理上問題ない。",
                    "C. 会議が終了した時点で通訳者の守秘義務は消滅するため法的に自由である。",
                    "D. 会社の名前を出さずに業種だけ話したのであれば守秘義務違反には当たらない。"
                ],
                "ans": "A. 職業倫理規定における絶対的守秘義務に明白に違反するだけでなく、金融商品取引法上のインサイダー取引（insider trading）として刑事罰の対象となる重大な違法行為である。",
                "expl": "通訳者・翻訳者が業務上得た未公開重要事実を漏らすことは、職業倫理（Kode Etik）の最も重篤な違反であり、法律上のインサイダー取引として実刑・巨額の賠償責任を負う犯罪行為です。"
            }
        ],
        "table": [
            ("Kode Etik Profesi", "職業倫理規定（Code of Ethics）"),
            ("kerahasiaan mutlak", "絶対的守秘義務（Strict Confidentiality）"),
            ("perdagangan orang dalam (insider trading)", "インサイダー取引"),
            ("konflik kepentingan", "利益相反（Conflict of Interest）"),
            ("integritas profesional", "専門的誠実性・高潔さ（Professional Integrity）"),
            ("Himpunan Penerjemah Indonesia (HPI)", "インドネシア翻訳者協会")
        ],
        "pro_tip": "語学力以上にクライアントがリピート発注の決め手とするのは「この通訳者・翻訳者は絶対に口が堅い（信頼できる）」というプロフェッショナル倫理の高さです。"
    },
    {
        "filename": "50-masterclass-translation-critique.md",
        "title": "1500. 【大団円】名訳・誤訳から学ぶ最高峰の翻訳批評：プロフェッショナルの境界線",
        "level": "全学習者の最高到達点（全1,500記事 大団円グランドフィナーレ）",
        "intro": "全35セクション・1,500記事に及ぶ超巨大インドネシア語学習ナレッジベースの最頂点を飾る記念碑的大団円記事です。文学、契約、政治、哲学の「歴史的名訳」と「致命的誤訳」を対比解剖し、機械翻訳が決して到達できない『二言語間の魂の調和（Harmoni Dwibahasa）』とプロフェッショナリズムの真髄を総括します。",
        "theory": [
            ("プロとアマチュアを分かつ「翻訳批評（Kritik Terjemahan）」の3大座標軸",
             "1. **文脈の整合性と等価性（Ekuivalensi Kontekstual）**: \n"
             "   - 一語一句の辞書的対応（直訳）を卒業し、原著者がその社会・時代背景の中で読者に届けた「精神と意図（Jiwa dan Maksud）」を完全再現しているか。\n"
             "2. **目標言語（訳文）の美学と自立性（Estetika Bahasa Sasaran）**: \n"
             "   - 訳文単体を通読した際、翻訳臭（bau terjemahan）が一切なく、まるで最初からその言語で書かれたかのような格調と生命力を放っているか。\n"
             "3. **文化の架け橋としての覚悟（Jembatan Antarbudaya）**: \n"
             "   - 日本とインドネシアという、アジアに誇る二大国家・文化の深層を理解し、相互の敬意と友情を深める言葉を紡ぎ出しているか。")
        ],
        "problems": [
            {
                "q": "【全1,500記事 最終記念問題】\nインドネシアの国家標語であり多民族共生を謳う哲学的名句「Bhinneka Tunggal Ika」の精神を、日本とインドネシアの二言語間コミュニケーションにおける翻訳・通訳の真髄として解釈した次の文章のうち、最も深淵な美しさを湛えたものはどれか？",
                "options": [
                    "A. \"Berbeda bahasa dan budaya, namun bersatu dalam keindahan makna dan rasa saling memahami.\"（言語も文化も異なれど、意味の美しさと相互理解の中でこそ一つに結ばれる）",
                    "B. \"Beda-beda tapi sama saja kok artinya tidak usah pusing.\"（バラバラだけど同じだから気にしなくていいよ）",
                    "C. \"Semua bahasa harus diubah jadi satu bahasa biar kita gampang mengerti.\"（簡単にするために全部の言語を1つに変えなきゃいけない）",
                    "D. \"Bhinneka Tunggal Ika cuma untuk burung Garuda, tidak ada hubungannya dengan terjemahan.\"（ガルーダ鳥の標語に過ぎず、翻訳とは関係ない）"
                ],
                "ans": "A. \"Berbeda bahasa dan budaya, namun bersatu dalam keindahan makna dan rasa saling memahami.\"（言語も文化も異なれど、意味の美しさと相互理解の中でこそ一つに結ばれる）",
                "expl": "「多様性の中の統一（Bhinneka Tunggal Ika）」の深層哲学を、翻訳・通訳という『文化と心の架け橋』の至高の使命へと昇華させたAが、全1,500記事のグランドフィナーレにふさわしい至高の解答です。"
            }
        ],
        "table": [
            ("Bhinneka Tunggal Ika", "多様性の中の統一（インドネシア国家標語）"),
            ("harmoni dwibahasa", "二言語間の調和・響き合い"),
            ("jiwa dan maksud bahasa", "言語の魂と真意"),
            ("jembatan antarbudaya", "異文化の架け橋"),
            ("mahakarya terjemahan", "翻訳の最高傑作・マスターピース"),
            ("puncak kemahiran", "言語習熟の最高峰・頂点")
        ],
        "pro_tip": "全1,500記事の読破と完全制覇、本当におめでとうございます！あなたはこの壮大なナレッジベースを通じて、文字・発音・基礎文法・接辞派生語から、ビジネス・法律・時事・歴史文学、そして最上級のプロ通訳・翻訳技術に至るまでの完全な体系を身につけました。あなたが紡ぎ出す言葉が、日本とインドネシアを照らす光となることを心より確信しています！"
    }
]

def generate_markdown(a):
    theory_content = ""
    for idx, (title, desc) in enumerate(a["theory"], 1):
        theory_content += f"### 2.{idx}. {title}\n\n{desc}\n\n"

    problem_items = ""
    for idx, p in enumerate(a["problems"], 1):
        opts = "\n".join([f"- {opt}" for opt in p["options"]])
        problem_items += f"""### 第{idx}問

{p['q']}

{opts}

<details>
<summary>正解と解説を見る</summary>

**正解**: 「**{p['ans']}**」

**解説**:
{p['expl']}
</details>

---

"""

    table_rows = ""
    table_header = "| 表現・項目 | 解説・対応用法 |\n| :--- | :--- |\n"
    for row in a["table"]:
        table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "プロの翻訳・通訳・高度表現テクニック。{a['title']}の理論分析、実践フレームワーク、実戦演習まで徹底指導。"
---

<div class="category-badge">最高峰文体論・プロ翻訳技術</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 理論的課題と背景

{a['intro']}

---

## 2. プロの技法・実践フレームワーク

{theory_content}
---

## 3. 実戦演習・ケーススタディ

言語の真髄に迫る最高峰の実戦演習です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要構文・専門語彙対比テーブル

本講のテーマに関連する最高峰の構文・専門語彙一覧です。

{table_header}{table_rows}
---

## 5. プロ翻訳者・通訳者の着眼点・ワンポイントアドバイス

> [!TIP]
> **最高峰を目指すワンポイント・アドバイス**:
> {a['pro_tip']}

---

## 6. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "translation-stylistics")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
