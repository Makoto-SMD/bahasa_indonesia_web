# -*- coding: utf-8 -*-
"""
セクション34 第3バッチ (1421-1430) 記事生成スクリプト
【資格演習】検定・UKBI直前実戦模試＆徹底解説
UKBI記述・スピーキング＆完全実戦模試（検定B級・A級・UKBI Unggul）
"""

import os

articles = [
    {
        "filename": "21-ukbi-seksi-4-writing-academic.md",
        "title": "1421. 【UKBI第4セクション】記述式（Menulis）：学術論文アブストラクト執筆",
        "level": "UKBI Seksi IV（Peringkat Unggul〜Istimewa / CEFR C1〜C2）",
        "intro": "UKBI（Uji Kemahiran Berbahasa Indonesia）第4セクション（Seksi IV: Menulis）は、上級学習者・研究者・専門職向けに実施される本格的な記述試験です。提示された学術データ・研究背景を15〜20分程度で整理し、100〜150語程度の洗練された学術論文要旨（Abstrak）を起草する能力が厳格に評価されます。客観的な文体、標準語法（bahasa baku）、明確な論理構成が不可欠です。",
        "theory": [
            ("学術要旨（Abstrak）の標準的4大構成要素（IMRaD枠組み）",
             "1. **背景と目的（Latar Belakang & Tujuan）**: 研究課題の提起と研究目的。「Penelitian ini bertujuan untuk menganalisis...（本研究は〜を分析することを目的とする）」\n"
             "2. **研究手法（Metode Penelitian）**: 調査対象、標本数、分析手法。「Pendekatan kualitatif dengan metode analisis konten digunakan untuk...（〜のためコンテンツ分析法を用いた質的アプローチを採用した）」\n"
             "3. **研究結果（Hasil Penelitian）**: 主な発見事実。「Hasil penelitian menunjukkan bahwa terdapat korelasi signifikan antara...（研究結果は〜の間に有意な相関があることを示している）」\n"
             "4. **結論と示唆（Kesimpulan & Implikasi）**: 結論と提言。「Dapat disimpulkan bahwa... sehingga direkomendasikan...（〜と結論づけられ、したがって〜が推奨される）」"),
            ("学術記述における文体（Laras Ilmiah）の鉄則",
             "- **受動構文の積極活用**: 「Penulis meneliti...」のような一人称主語を避け、「Penelitian ini dilakukan untuk...」「Data dikumpulkan melalui...」と客観化する。\n"
             "- **縮約・口語表現の完全排除**: tak/nggak → **tidak**、udah → **sudah**、karna → **karena**、banget → **sangat**。\n"
             "- **フォーマルな論理接続詞**: selain itu, oleh karena itu, sehubungan dengan hal tersebut, kendati demikian。")
        ],
        "problems": [
            {
                "q": "【UKBI記述想定課題】次の研究要約文の冒頭文として、学術論文の文体（laras bahasa ilmiah）として最も適切なものはどれか？",
                "options": [
                    "A. Penelitian ini bertujuan untuk menginvestigasi dampak digitalisasi perbankan terhadap inklusi keuangan masyarakat perdesaan.",
                    "B. Saya mau meneliti tentang pengaruh digitalisasi bank biar masyarakat desa bisa ikut menikmati keuangan modern.",
                    "C. Tulisan ini bertujuan agar supaya kita tahu gimana efek aplikasi bank di kampung-kampung saat ini.",
                    "D. Artikel ini dibikin untuk membuktikan kalau digitalisasi bank itu penting banget bagi orang desa."
                ],
                "ans": "A. Penelitian ini bertujuan untuk menginvestigasi dampak digitalisasi perbankan terhadap inklusi keuangan masyarakat perdesaan.",
                "expl": "学術アブストラクトでは客観的な受動構文や三人称表現を用い、格調高い語彙（menginvestigasi, dampak, inklusi keuangan, masyarakat perdesaan）を用います。B, C, Dは口語表現（mau, biar, gimana, kampung-kampung, dibikin, penting banget）が含まれ不適当です。"
            },
            {
                "q": "学術論文の要旨において「〜であることが判明した」という研究結果を報告する表現として最も標準的なものはどれか？",
                "options": [
                    "A. Temuan empiris mengindikasikan bahwa regulasi tersebut efektif meredam inflasi daerah.",
                    "B. Ternyata aturan itu manjur buat nurunin inflasi di daerah-daerah.",
                    "C. Rupanya peraturan tadi sungguh ampuh bikin inflasi jadi rendah.",
                    "D. Kita ketahui bersama bahwasanya peraturan itu berhasil sekali."
                ],
                "ans": "A. Temuan empiris mengindikasikan bahwa regulasi tersebut efektif meredam inflasi daerah.",
                "expl": "学術的報告では「Temuan empiris mengindikasikan bahwa...（実証的知見は〜を示唆している）」という客観・精密な学術語彙が求められます。"
            }
        ],
        "table": [
            ("Penelitian ini bertujuan untuk...", "本研究は〜を目的とする（研究目的提示）"),
            ("Data dikumpulkan melalui...", "データは〜を通じて収集された（手法提示）"),
            ("Temuan penelitian mengindikasikan...", "研究知見は〜を示唆している（結果報告）"),
            ("Berdasarkan hasil temuan tersebut...", "それらの知見に基づき（考察導入）"),
            ("Dapat disimpulkan bahwa...", "〜であると結論づけることができる（結論提示）"),
            ("implikasi praktis dan teoritis", "実践的および理論的示唆")
        ],
        "pro_tip": "UKBI Menulisでは語数不足や語数超過（制限±10%以内）が減点対象となります。段落を分けず1パラグラフでアブストラクトを完結させ、IMRaDの各要素を1〜2文ずつテンポよくまとめる訓練を積みましょう。"
    },
    {
        "filename": "22-ukbi-seksi-4-writing-argument.md",
        "title": "1422. 【UKBI第4セクション】記述式（Menulis）：賛否両論の意見論述文",
        "level": "UKBI Seksi IV（Peringkat Unggul〜Istimewa / CEFR C1〜C2）",
        "intro": "UKBI記述試験（Seksi IV）のもう一つの頻出パターンが「現代社会の論争的トピック（isu kontroversial）に対する意見論述文（Esai Argumentatif）」です。人工知能の労働市場への影響、再生可能エネルギー移行のコスト、リモートワークの是非などのテーマに対し、自らの立場を明確にしつつ、対立する意見（kontra-argumen）にも配慮した説得力ある構成が求められます。",
        "theory": [
            ("説得力ある意見論述文（Esai Argumentatif）の段落展開",
             "1. **導入部（Pendahuluan）**: トピックの現代的意義（kontekstualisasi）を提示し、自己の明確な主張（tesis）を打ち出す。\n"
             "2. **論拠の提示（Argumen Pendukung）**: 根拠、事実データ、具体例（bukti empiris）を挙げて主張を裏付ける。\n"
             "3. **反対意見への言及と反論（Sanggahan / Counter-argument）**: 反対派の視点に「確かに〜という側面はある（Kendati demikian / Memang benar bahwa...）」と一定の理解を示した上で、自説の優位性を論証する。\n"
             "4. **結論（Penutup）**: 主張の再確認（reafirmasi）と今後の展望・提言を述べる。"),
            ("論述文で必須の論理マーカー（Penanda Hubungan Wacana）",
             "- **対比・譲歩**: kendati demikian（それにもかかわらず）、di satu sisi... di sisi lain...（一方では…他方では…）、sungguhpun demikian（そうではあるが）。\n"
             "- **因果関係**: sebagai konsekuensinya（結果として）、oleh karenanya（それゆえに）、berimplikasi pada（〜に影響を及ぼす）。\n"
             "- **補足・強調**: terlebih lagi（さらに言えば）、bahkan lebih jauh lagi（さらに進んで）、perlu digarisbawahi bahwa（強調すべき点は〜）。")
        ],
        "problems": [
            {
                "q": "【論述構成問題】「新首都移転（Pemindahan Ibu Kota）」の経済的影響に関する論述文において、反対派の懸念に配慮しつつ自説を展開する譲歩構文として最も格調高いものはどれか？",
                "options": [
                    "A. Kendati membebani anggaran belanja negara dalam jangka pendek, pemindahan ibu kota berpotensi mengakselerasi pemerataan pembangunan antarwilayah.",
                    "B. Walaupun mahal banget biayanya sekarang, tapi ibu kota baru bikin daerah luar Jawa jadi maju juga kok.",
                    "C. Biar kata duit negara habis banyak, pokoknya kita harus pindah biar nggak numpuk di Jakarta terus.",
                    "D. Memang sih biayanya sangat besar, namun menurut hemat saya ya sudahlah tidak apa-apa demi masa depan."
                ],
                "ans": "A. Kendati membebani anggaran belanja negara dalam jangka pendek, pemindahan ibu kota berpotensi mengakselerasi pemerataan pembangunan antarwilayah.",
                "expl": "Aは「Kendati 〜, ... berpotensi mengakselerasi...」という極めてフォーマルかつ論理的な構文で対比を表現しています。他選択肢は口語表現や俗語が混入しています。"
            },
            {
                "q": "論述文の結論部分で自らの主張を再確認する表現として最も適切なものはどれか？",
                "options": [
                    "A. Berdasarkan elaborasi argumen di atas, dapat ditegaskan kembali bahwa mitigasi risiko iklim merupakan imperatif moral dan ekonomi.",
                    "B. Jadi begitu saja tulisan saya, pokoknya kalian harus setuju dengan apa yang saya bilang di atas.",
                    "C. Dari omongan tadi, jelas sekali kalau masalah iklim itu gawat banget dan harus segera diberesin.",
                    "D. Sekian dan terima kasih, semoga para pembaca paham maksud saya tentang iklim."
                ],
                "ans": "A. Berdasarkan elaborasi argumen di atas, dapat ditegaskan kembali bahwa mitigasi risiko iklim merupakan imperatif moral dan ekonomi.",
                "expl": "「elaborasi argumen（議論の詳述）」「ditegaskan kembali（再確認・強調される）」「imperatif moral dan ekonomi（道徳的・経済的至上命題）」といった高度な論述語彙が適切に用いられています。"
            }
        ],
        "table": [
            ("isu kontroversial", "論争的トピック・議論の的となる問題"),
            ("bukti empiris", "実証的根拠・証拠"),
            ("mengakselerasi", "加速させる（mempercepatの学術語）"),
            ("pemerataan pembangunan", "開発の公平・均等な配分"),
            ("kendati demikian", "それにもかかわらず・そうではあるが"),
            ("imperatif", "至上命令・不可欠な要件")
        ],
        "pro_tip": "UKBIの意見論述では、感情論（saya merasa, saya benci など）は大幅減点です。「データや事実が示している通り（Sebagaimana ditunjukkan oleh data）」と第三者的な客観性を保つことがPeringkat Unggul（優等）獲得の絶対条件です。"
    },
    {
        "filename": "23-ukbi-seksi-5-speaking-presentation.md",
        "title": "1423. 【UKBI第5セクション】口頭表現（Berbicara）：3分間プレゼンテーション",
        "level": "UKBI Seksi V（Peringkat Unggul〜Istimewa / CEFR C1〜C2）",
        "intro": "UKBI第5セクション（Seksi V: Berbicara）は、コンピュータの録音システムを通じて受験者の口頭発信能力（kemahiran berbicara）を評価する口述試験です。画面上に提示された図表・社会問題に関する課題に対し、1分間の準備時間の後、3分間で論理的かつ流暢なプレゼンテーションを行うことが求められます。発音の明瞭さ、文法の正確性、時間配分の管理が鍵を握ります。",
        "theory": [
            ("3分間プレゼンテーションの黄金タイムテーブル（180秒配分）",
             "1. **導入・挨拶と主題提示（0:00〜0:30）**: 審査員への挨拶、発表テーマの宣言、発表の骨子（アウトライン）の提示。\n"
             "2. **第1の論点・現状分析（0:30〜1:10）**: 課題の背景と具体的なデータ・現状の説明。\n"
             "3. **第2の論点・解決策・展望（1:10〜2:10）**: 具体的対策の提言、利点と想定される課題への対策。\n"
             "4. **まとめ・結び（2:10〜2:45）**: メインメッセージの要約と結びの言葉（2分45秒〜2分55秒の間で着地するのが理想的）。"),
            ("プレゼンテーションで即戦力となる定型フレーズ集",
             "- **発表開始**: \"Selamat pagi/siang. Pada kesempatan yang berharga ini, saya hendak memaparkan topik krusial mengenai...\"\n"
             "- **構成説明**: \"Pemaparan ini saya bagi menjadi tiga bagian utama, yaitu...\"\n"
             "- **話題転換**: \"Beralih ke poin berikutnya, mari kita telaah aspek...\"\n"
             "- **強調・着目**: \"Hal yang patut mendapat perhatian khusus di sini adalah...\"\n"
             "- **結び**: \"Demikianlah pemaparan singkat dari saya, semoga memberikan wawasan baru. Terima kasih atas perhatian Anda.\"")
        ],
        "problems": [
            {
                "q": "【口頭表現シミュレーション】提示された棒グラフ「インドネシアにおける電子決済の普及率推移」を説明する口頭プレゼンの冒頭導入として、最もプロフェッショナルな発話はどれか？",
                "options": [
                    "A. \"Berdasarkan diagram batang yang tersaji di layar, terlihat lonjakan eksponensial dalam adopsi transaksi nontunai selama lima tahun terakhir.\"",
                    "B. \"Lihatlah gambar di layar ini, transaksinya naik banyak sekali dalam lima tahun belakangan ini lho.\"",
                    "C. \"Ini ada grafik bagus yang mau saya omongin, intinya orang Indonesia sekarang suka pakai HP buat bayar-bayar.\"",
                    "D. \"Bagan ini menunjukkan kalau pembayaran digital itu sangat ramai sekali dan keren abis pembahasannya.\""
                ],
                "ans": "A. \"Berdasarkan diagram batang yang tersaji di layar, terlihat lonjakan eksponensial dalam adopsi transaksi nontunai selama lima tahun terakhir.\"",
                "expl": "「diagram batang yang tersaji（画面に提示された棒グラフ）」「lonjakan eksponensial（指数関数的急増）」「adopsi transaksi nontunai（キャッシュレス決済の導入・採用）」など、高度な語彙と明快な文法が完璧です。"
            },
            {
                "q": "プレゼンテーションの結びにおいて、時間通りに格調高く発表を締めくくる発話はどれか？",
                "options": [
                    "A. \"Sebagai konklusi, transformasi digital merupakan keniscayaan yang menuntut kesiapan regulasi dan literasi masyarakat. Sekian dan terima kasih.\"",
                    "B. \"Waktunya sudah mau habis nih, jadi ya udahlah sampai sini aja dulu omongan saya, terima kasih.\"",
                    "C. \"Begitulah kira-kira yang bisa saya sampaikan, maaf kalau banyak salah kata ya, dadah.\"",
                    "D. \"Saya rasa cukup ya, saya bingung mau ngomong apa lagi, makasih semuanya.\""
                ],
                "ans": "A. \"Sebagai konklusi, transformasi digital merupakan keniscayaan yang menuntut kesiapan regulasi dan literasi masyarakat. Sekian dan terima kasih.\"",
                "expl": "「Sebagai konklusi（結論として）」「keniscayaan（必然・避けて通れないこと）」を用いて簡潔かつ力強く締めくくっています。"
            }
        ],
        "table": [
            ("memaparkan topik", "テーマを説明・詳述する"),
            ("diagram batang", "棒グラフ（diagram garis=折れ線グラフ, diagram lingkaran=円グラフ）"),
            ("lonjakan eksponensial", "指数関数的急増・爆発的増加"),
            ("transaksi nontunai", "非現金取引・キャッシュレス決済"),
            ("keniscayaan", "必然性・避けられない運命・確実なこと"),
            ("literasi digital", "デジタルリテラシー・情報活用能力")
        ],
        "pro_tip": "録音中は「えーっと」「anu...」「nganu...」などの無意味なフィラーをできるだけ抑制し、沈黙が怖くても1秒息を整えてから標準的な論理接続詞（Selanjutnya, Sementara itu）を発話する癖をつけてください。"
    },
    {
        "filename": "24-ukbi-seksi-5-speaking-rebuttal.md",
        "title": "1424. 【UKBI第5セクション】口頭表現（Berbicara）：質問への即座の論理的応答",
        "level": "UKBI Seksi V（Peringkat Unggul〜Istimewa / CEFR C1〜C2）",
        "intro": "UKBI第5セクションの高度な課題の一つに、提示された質疑・反論・疑問点に対する即座の応答テストがあります。相手の質問の趣旨を的確に捉え、礼儀正しさを保ちながら、論理的に自説の根拠を補強して反駁（rebuttal / klarifikasi）する技術が求められます。感情的にならず、事実と論理でスマートに応答する高度なスピーキング運用能力を磨きます。",
        "theory": [
            ("反論・質疑応答における「3段論法応答モデル」",
             "1. **相手への敬意と質問の受け止め（Apresiasi & Klarifikasi）**: 質問の鋭さを認め、論点を明確化する。「Terima kasih atas pertanyaan kritis yang Anda ajukan mengenai...（〜に関する鋭いご質問に感謝いたします）」\n"
             "2. **譲歩と境界線の画定（Konsesi & Batasan）**: 相手の懸念に一定の合理性を認めつつ、例外や適用範囲を限定する。「Kekhawatiran tersebut memang sangat beralasan, namun perlu dicatat bahwa...（そのご懸念は極めてもっともですが、留意すべき点は〜）」\n"
             "3. **反論と解決策の提示（Sanggahan & Solusi）**: 事実データや代替策を提示して懸念を解消する。「Fakta di lapangan menunjukkan bahwa sistem mitigasi yang ada mampu meminimalisasi risiko tersebut secara signifikan.」"),
            ("質疑応答で品格を保つスマート表現",
             "- **質問を言い換えて時間稼ぎ**: \"Terkait dengan poin yang Anda singgung perihal...\"（あなたが言及された〜に関する論点についてですが）\n"
             "- **誤解の穏やかな訂正**: \"Perkenankan saya meluruskan satu hal penting di sini...\"（ここで一点、重要な点について誤解を解かせていただきたく存じます）\n"
             "- **多面的な視点の導入**: \"Jika kita meninjaunya dari sudut pandang yang lebih holistik...\"（より包括的な視点から検討いたしますと）")
        ],
        "problems": [
            {
                "q": "【即答シミュレーション】「再生可能エネルギーへの急進的な移行は、電力供給の不安定化を招くのではないか？」という質問に対し、反論しつつ自説を堅持する応答として最も知性的なものはどれか？",
                "options": [
                    "A. \"Kekhawatiran mengenai stabilitas pasokan sangatlah berdasar. Namun demikian, integrasi teknologi smart grid dan sistem penyimpanan baterai modern terbukti mampu menjaga keandalan jaringan secara optimal.\"",
                    "B. \"Pendapat Anda salah besar. Pokoknya energi terbarukan itu paling bagus dan tidak mungkin bikin mati lampu.\"",
                    "C. \"Nggak usah khawatir soal itu, zaman sekarang teknologi udah canggih banget jadi pasti aman-aman aja kok.\"",
                    "D. \"Kenapa Anda pesimis sekali? Di Eropa saja bisa jalan lancar, masa kita tidak bisa?\""
                ],
                "ans": "A. \"Kekhawatiran mengenai stabilitas pasokan sangatlah berdasar. Namun demikian, integrasi teknologi smart grid dan sistem penyimpanan baterai modern terbukti mampu menjaga keandalan jaringan secara optimal.\"",
                "expl": "Aは相手の懸念を「sangatlah berdasar（極めてもっともである）」と受け止めた上で、「Namun demikian（しかしながら）」と繋ぎ、「smart grid」「sistem penyimpanan baterai」という具体的技術による解決策を論理的に提示しています。"
            },
            {
                "q": "相手の発言に含まれる事実誤認を礼儀正しく正す（meluruskan）口頭表現として最も適切なものはどれか？",
                "options": [
                    "A. \"Perkenankan saya mengklarifikasi bahwa data yang kami gunakan adalah data sensus resmi terkini, bukan estimasi kasar.\"",
                    "B. \"Anda keliru dan tidak membaca data dengan teliti, tolong jangan asal menuduh ya.\"",
                    "C. \"Data Anda ngawur, data saya yang paling benar dan tidak terbantahkan sama sekali.\"",
                    "D. \"Bukan begitu dong, Anda ini sepertinya salah paham banget sama apa yang saya omongin tadi.\""
                ],
                "ans": "A. \"Perkenankan saya mengklarifikasi bahwa data yang kami gunakan adalah data sensus resmi terkini, bukan estimasi kasar.\"",
                "expl": "「Perkenankan saya mengklarifikasi...（〜であることを説明・明確にさせていただきたく存じます）」は公式の場や口述試験において極めて高い評価を受ける丁寧かつ格調高い表現です。"
            }
        ],
        "table": [
            ("pertanyaan kritis", "批判的・本質的な質問・鋭い質問"),
            ("kekhawatiran yang berdasar", "根拠のある懸念・もっともな心配"),
            ("perkenankan saya...", "私に〜させてください（極めて丁寧な前置き）"),
            ("mengklarifikasi", "明確にする・誤解を解く・釈明する"),
            ("stabilitas pasokan", "供給の安定性"),
            ("secara holistik", "包括的・全体論的に")
        ],
        "pro_tip": "反論課題では、相手を否定して論破しようとするとスピーキングの「礼節・対人配慮性（kesantunan berbahasa）」で減点されます。必ず「相手の意見に一理ある」とクッションを置いてから自論を展開してください。"
    },
    {
        "filename": "25-mock-exam-inken-b-01.md",
        "title": "1425. 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第1回",
        "level": "技能検定B級（CEFR B2 / 中上級ビジネスレベル）",
        "intro": "インドネシア語技能検定B級の筆記試験（文法・語彙・読解・翻訳）を忠実に再現した完全オリジナル想定問題集の第1回です。B級特有の「派生語の精密な使い分け」「複文構造の把握」「ビジネス・社会時事記事の読解」を本番と同じ緊迫感の中で解き、弱点を徹底的に補強します。",
        "theory": [
            ("検定B級 筆記試験の出題傾向と時間配分（80分）",
             "1. **大問1: 語彙・短文空所補充（15分）**: 語根からの派生語（meN-, di-, ber-, peN-, -an, ke--an, meN--kan, meN--i）の正確な識別。\n"
             "2. **大問2: 誤文訂正・文法識別（15分）**: 前置詞の誤用、アスペクト副詞、受動態の語順エラーを発見する能力。\n"
             "3. **大問3: 長文読解（25分）**: 300〜400語程度の経済・環境・社会記事。段落要旨、指示語の指す内容、文脈推論。\n"
             "4. **大問4: 日イ・イ日短文翻訳（25分）**: ビジネスメールや業務報告文の正確な相互翻訳。直訳を排した自然な構文。")
        ],
        "problems": [
            {
                "q": "【大問1: 接辞空所補充】次の文の空所に入れるのに最も適切な語はどれか？\n\"Pemerintah daerah berupaya keras untuk [______] potensi pariwisata bahari demi meningkatkan taraf hidup masyarakat pesisir.\"",
                "options": ["A. memanfaatkan", "B. pemanfaatan", "C. termanfaatkan", "D. berfaedah"],
                "ans": "A. memanfaatkan",
                "expl": "「untuk」の直後には目的語（potensi pariwisata bahari）を取る他動詞が必要です。語根 faedah / manfaat から派生する「memanfaatkan（〜を活用する・利用する）」が文法・文脈ともに正解です。"
            },
            {
                "q": "【大問2: 文法・前置詞識別】次の文の空所に入れる前置詞として最も適切なものはどれか？\n\"Keputusan dewan direksi tersebut diambil berlandaskan [______] hasil audit investigatif yang dilakukan oleh konsultan independen.\"",
                "options": ["A. pada", "B. atas", "C. kepada", "D. tentang"],
                "ans": "A. pada",
                "expl": "動詞「berlandaskan（〜に基づいている）」は前置詞「pada」と共起して「berlandaskan pada...（〜を基礎・根拠として）」の慣用句を形成します（berdasarkan pada / atas との混同に注意）。"
            },
            {
                "q": "【大問3: 読解空所補充】\n\"Tingkat inflasi yang terkendali memberikan ruang bagi bank sentral untuk melonggarkan kebijakan moneter. Hal ini diharapkan dapat [______] pertumbuhan ekonomi yang sempat melambat akibat gejolak pasar global.\"\n空所に入る最適な語はどれか？",
                "options": ["A. menstimulasi", "B. distimulasi", "C. stimulasi", "D. terstimulasi"],
                "ans": "A. menstimulasi",
                "expl": "助動詞「dapat」の後で目的語「pertumbuhan ekonomi」を取る能動他動詞形「menstimulasi（〜を刺激する・促進する）」が入ります。"
            }
        ],
        "table": [
            ("memanfaatkan potensi", "潜在能力・ポテンシャルを活用する"),
            ("berlandaskan pada", "〜に基づいている・〜を基盤とする"),
            ("kebijakan moneter", "金融政策（monetary policy）"),
            ("menstimulasi pertumbuhan", "成長を刺激・促進する"),
            ("gejolak pasar", "市場の動揺・乱高下"),
            ("taraf hidup", "生活水準")
        ],
        "pro_tip": "B級では「berlandaskan pada」「bergantung pada」「terdiri atas/dari」などの『動詞＋特定前置詞のコロケーション』が頻繁に狙われます。単語単体ではなく句としてインプットしてください。"
    },
    {
        "filename": "26-mock-exam-inken-b-02.md",
        "title": "1426. 【実戦模試】インドネシア語技能検定 B級 完全想定問題 第2回",
        "level": "技能検定B級（CEFR B2 / 中上級ビジネスレベル）",
        "intro": "インドネシア語技能検定B級の完全想定問題集第2回です。今回は特に受験生が苦戦する「使役（meN--kan）と適用・反復（meN--i）の識別」「受動態構文（di- vs 倒置受動態）の書き換え」、および「契約・取引におけるビジネス読解」に焦点を当てた実戦演習を実施します。",
        "theory": [
            ("B級突破のための文法急所チェック",
             "1. **meN--kan vs meN--i の対立**: \n"
             "   - memanaskan air（水を温める：対象を熱い状態にする＝使役）\n"
             "   - memanasi sup（スープを温め直す：対象に熱を加える＝場所・適用）\n"
             "   - menugasi dia（彼に任務を課す：人を目的語にとる meN--i）\n"
             "   - menugaskan pekerjaan kepadanya（彼に仕事を割り当てる：物を目的語にとる meN--kan）\n"
             "2. **三人称被動態と一人称・二人称被動態の厳格な区別**:\n"
             "   - 正: Surat itu **sudah saya baca** kemarin.\n"
             "   - 誤: Surat itu sudah dibaca oleh saya kemarin.（B級では減点対象）")
        ],
        "problems": [
            {
                "q": "【meN--kan / meN--i の識別問題】次の文の空所に入る正しい動詞の組み合わせはどれか？\n\"Direktur utama [______] sekretarisnya untuk mengatur jadwal pertemuan, kemudian beliau [______] tugas baru tersebut kepadanya.\"",
                "options": [
                    "A. menugasi / membebankan",
                    "B. menugaskan / membebani",
                    "C. ditugasi / membebankan",
                    "D. bertugas / berbeban"
                ],
                "ans": "A. menugasi / membebankan",
                "expl": "人を直接の目的語とする場合は「menugasi sekretarisnya（秘書に命じる）」となり、任務や重荷を相手に課す場合は「membebankan tugas（仕事を負わせる）」となります。したがってAが正解です。"
            },
            {
                "q": "【語順・受動態識別問題】「当社はこの提案を慎重に検討いたしました」をインドネシア語にする際、最も自然で適切なB級標準文はどれか？",
                "options": [
                    "A. Proposal ini telah kami pertimbangkan secara saksama.",
                    "B. Proposal ini telah dipertimbangkan oleh kami secara saksama.",
                    "C. Proposal ini kami telah mempertimbangkan secara saksama.",
                    "D. Kami telah dipertimbangkan oleh proposal ini secara saksama."
                ],
                "ans": "A. Proposal ini telah kami pertimbangkan secara saksama.",
                "expl": "一人称複数「kami」が動作主となる受動文では、助動詞（telah）＋代名詞（kami）＋語根動詞（pertimbangkan）という前置代名詞受動構文（Pasif Persona）にするのが鉄則です。Bの「di-... oleh kami」は不自然と見なされます。"
            },
            {
                "q": "【ビジネス長文読解】\n\"Pihak Pertama berhak memutuskan kontrak secara sepihak apabila Pihak Kedua terbukti melakukan wanprestasi yang tidak diperbaiki dalam tenggat waktu 14 hari kalender kerja.\"\nこの文の「wanprestasi」の意味として最も正確なものはどれか？",
                "options": [
                    "A. 債務不履行・契約違反（default / breach of contract）",
                    "B. 不正会計・粉飾決算（fraudulent accounting）",
                    "C. 破産宣告・会社更生（bankruptcy declaration）",
                    "D. 機密漏洩・スパイ行為（leak of confidential info）"
                ],
                "ans": "A. 債務不履行・契約違反（default / breach of contract）",
                "expl": "「wanprestasi」はオランダ法（wanprestatie）に由来する法律・契約上の重要専門用語で、「債務不履行（契約上の義務を履行しないこと）」を意味します。"
            }
        ],
        "table": [
            ("menugasi bawahan", "部下に任務を命じる（対象は人）"),
            ("menugaskan proyek", "プロジェクトを任せる（対象は仕事・事象）"),
            ("secara saksama", "綿密に・慎重に（dengan cermat/teliti）"),
            ("wanprestasi", "債務不履行・契約不履行"),
            ("memutuskan sepihak", "一方的に契約を解除・破棄する"),
            ("tenggat waktu", "猶予期間・期限（deadline/grace period）")
        ],
        "pro_tip": "「wanprestasi（債務不履行）」「itikat baik（信義誠実）」「force majeure / keadaan kahar（不可抗力）」など、ビジネス契約書の頻出法律用語はB級・A級で合否を分ける超頻出語です。"
    },
    {
        "filename": "27-mock-exam-inken-a-01.md",
        "title": "1427. 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第1回",
        "level": "技能検定A級（CEFR C1 / 最上級専門・翻訳通訳レベル）",
        "intro": "インドネシア語技能検定A級（合格率10%前後の最難関）の筆記試験をターゲットにした完全想定模試第1回です。A級では、単なる文法知識を超えた「文脈の微細なニュアンスの解釈」「高度な社説・論説文の速読と批判的把握」「格調高い日本語・インドネシア語の双方向翻訳」が課されます。",
        "theory": [
            ("検定A級で問われる3大高度スキル",
             "1. **文脈に応じた接辞の微差識別**: ber-kan, peN--an vs per--an, ke--an（抽象名詞と受動的状態の区別）。\n"
             "2. **重層的な複文・関係節の解体**: 主語と述語の間に長い修飾節（yang... serta... di mana...）が挟まれた複雑な公用文を瞬時に主幹と枝葉に分解する力。\n"
             "3. **格調高き定訳の運用**: 日イ翻訳における「〜を余儀なくされる」「〜の是非を問う」「〜に鑑み」などの慣用表現を定型インドネシア語へ的確に変換する瞬発力。")
        ],
        "problems": [
            {
                "q": "【A級語根・派生語問題】次の文の空所に入る語として最も文脈および語法上適切なものはどれか？\n\"Ketiadaan regulasi yang komprehensif disinyalir menjadi [______] suburnya praktik kartel di industri telekomunikasi.\"",
                "options": ["A. biang keladi", "B. kambing hitam", "C. batu loncatan", "D. ujung tombak"],
                "ans": "A. biang keladi",
                "expl": "文脈は「包括的な規制の欠如が、通信業界におけるカルテル慣行が蔓延する【元凶・主因】になっていると目されている」です。「biang keladi」は悪事や混乱の「元凶・張本人」を意味する成句です（kambing hitam=身代わり/スケープゴート, batu loncatan=踏み台, ujung tombak=先陣/急先鋒）。"
            },
            {
                "q": "【A級文法・構文把握問題】次の文の中で、文法的に誤り（grammatical error）を含む下線部（[A]〜[D]）はどれか？\n\"Menteri Keuangan menegaskan [A: bahwasanya] defisit anggaran [B: berhasil ditekan] menjadi 2,3 persen, [C: di mana] angka tersebut [D: mencerminkan] disiplin fiskal yang kokoh.\"",
                "options": ["A", "B", "C", "D"],
                "ans": "C",
                "expl": "標準インドネシア語（bahasa baku）において、「di mana」を英語の関係副詞「where」のように関係代名詞・継続用法として用いることは規範文法上誤りとされます。「sehingga」「yang mana（口語）」ではなく、「yang」や独立した文に改めるべき悪文です。"
            },
            {
                "q": "【日イ翻訳高度課題】次の日本文のインドネシア語訳として最も格調高いものはどれか？\n「原油価格の急激な下落に直面し、政府はエネルギー補助金の削減を余儀なくされた。」",
                "options": [
                    "A. Berhadapan dengan anjloknya harga minyak mentah, pemerintah terpaksa memangkas subsidi energi.",
                    "B. Di depan harga minyak mentah turun, pemerintah dipaksa potong subsidi energi.",
                    "C. Karena harga minyak jatuh cepat, maka pemerintah harus bikin sedikit subsidi energi.",
                    "D. Melihat minyak mentah yang jatuh sekali, pemerintah tidak punya pilihan selain menghabiskan subsidi energi."
                ],
                "ans": "A. Berhadapan dengan anjloknya harga minyak mentah, pemerintah terpaksa memangkas subsidi energi.",
                "expl": "「anjloknya harga minyak mentah（原油価格の急落）」「terpaksa memangkas subsidi energi（補助金削減を余儀なくされた）」という格調高い経済公用文の語彙が的確に選ばれています。"
            }
        ],
        "table": [
            ("disinyalir menjadi...", "〜の兆候・元凶であると目されている"),
            ("biang keladi", "諸悪の根源・元凶・張本人"),
            ("kambing hitam", "スケープゴート・身代わり・濡れ衣を着せられた人"),
            ("anjloknya harga", "価格の急落・暴落（menukik / merosot）"),
            ("memangkas subsidi", "補助金を削減する・削る"),
            ("disiplin fiskal", "財政規律")
        ],
        "pro_tip": "A級の誤文訂正では「di mana を使った誤った関係節」「mengenyampingkan などの接辞綴りミス（正: mengesampingkan）」「berulang kali などの二重表現（重複表現: pleonasme）」が三大頻出トラップです。"
    },
    {
        "filename": "28-mock-exam-inken-a-02.md",
        "title": "1428. 【実戦模試】インドネシア語技能検定 A級 完全想定問題 第2回",
        "level": "技能検定A級（CEFR C1 / 最上級専門・翻訳通訳レベル）",
        "intro": "インドネシア語技能検定A級完全想定模試の第2回です。今回は、政治・安全保障・地政学・憲法判断といった国家レベルの重厚なテーマを扱い、高度な語彙力（kosakata tingkat tinggi）、熟語（ungkapan idiomatikal）、および複雑な倒置・複文読解を演習します。",
        "theory": [
            ("A級合格を決定づける高度政治・外交語彙群",
             "1. **地政学・安全保障**: kedaulatan wilayah（領土主権）、zona ekonomi eksklusif（排他的経済水域：ZEE）、ketahanan nasional（国家強靭性）、senjata pemusnah massal（大量破壊兵器）。\n"
             "2. **憲法・司法**: uji materiil（違憲審査・違憲立法審査）、mahkamah konstitusi（憲法裁判所）、kepastian hukum（法的確実性）、keadilan substantif（実質的正義）。\n"
             "3. **国際交渉**: pakta non-agresi（不可侵条約）、resolusi dewan keamanan（安保理決議）、gencatan senjata（停戦協定）、kebuntuan diplomatik（外交的行き詰まり・デッドロック）。")
        ],
        "problems": [
            {
                "q": "【高度時事・語彙選択問題】\n\"Mahkamah Konstitusi mengabulkan sebagian permohonan [______] terhadap pasal kontroversial dalam Undang-Undang Ketenagakerjaan tersebut.\"\n空所に入る法廷用語として最も適切なものはどれか？",
                "options": ["A. uji materiil", "B. uji petik", "C. uji nyali", "D. uji coba"],
                "ans": "A. uji materiil",
                "expl": "憲法裁判所（Mahkamah Konstitusi）が法律条文の憲法適合性を審査する司法手続きは「uji materiil（違憲審査・実質的審査）」です（uji petik=無作為抽出検査, uji nyali=度胸試し, uji coba=試運転/実験）。"
            },
            {
                "q": "【外交・成句把握問題】「外交交渉が行き詰まりに直面した」を表す成句（ungkapan）として最も適切なものはどれか？",
                "options": [
                    "A. Perundingan diplomatik menemui jalan buntu.",
                    "B. Perundingan diplomatik menabrak pagar beton.",
                    "C. Perundingan diplomatik kehabisan minyak tanah.",
                    "D. Perundingan diplomatik masuk ke lubang semut."
                ],
                "ans": "A. Perundingan diplomatik menemui jalan buntu.",
                "expl": "交渉や議論が膠着状態・デッドロックに陥ることは「menemui jalan buntu（暗礁に乗り上げる・行き詰まる）」と表現します。"
            },
            {
                "q": "【イ日翻訳問題】\n\"Langkah de-eskalasi militer di wilayah perbatasan mendesak dilakukan guna mengeliminasi potensi gesekan bersenjata yang dapat menyulut instabilitas kawasan.\"\n最も格調高い日本語訳はどれか？",
                "options": [
                    "A. 地域の不安定化を招きかねない武力衝突の火種を排除するため、国境地帯における軍事的緊張緩和措置の実施が急務となっている。",
                    "B. 国境での軍隊の緊張を減らすステップは、地域の不安定に火をつける武器の擦れ合いを無くすために早くやるべきだ。",
                    "C. 地域が不安定になる恐れがある武器の摩擦を消す目的で、国境の軍事デエスカレーションを急いでやらないといけない。",
                    "D. 国境の軍隊を減らす動きは急がれており、そうしないと地域の安定が燃えてしまう可能性がある。"
                ],
                "ans": "A. 地域の不安定化を招きかねない武力衝突の火種を排除するため、国境地帯における軍事的緊張緩和措置の実施が急務となっている。",
                "expl": "「de-eskalasi（緊張緩和）」「mengeliminasi potensi gesekan bersenjata（武力衝突の潜在的摩擦・火種を排除する）」「menyulut instabilitas（不安定化に火をつける・招く）」「mendesak dilakukan（実施が急務である）」の定訳が完璧に反映されています。"
            }
        ],
        "table": [
            ("uji materiil", "違憲立法審査・実質的審査（judicial review）"),
            ("menemui jalan buntu", "行き詰まる・暗礁に乗り上げる（deadlock）"),
            ("de-eskalasi militer", "軍事的緊張緩和（de-escalation）"),
            ("gesekan bersenjata", "武力衝突・小競り合い・軍事的摩擦"),
            ("menyulut instabilitas", "不安定化を引き起こす・火をつける"),
            ("mendesak dilakukan", "実施が急務である・強く求められる")
        ],
        "pro_tip": "A級では、新聞の国際面や社説に登場する「menyulut（点火する→引き起こす）」「meredam（弱める・鎮静化する）」「mengganjal（突っかえ棒をする→妨害する）」といった比喩的動詞の習得が不可欠です。"
    },
    {
        "filename": "29-mock-exam-ukbi-unggul-01.md",
        "title": "1429. 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第1回",
        "level": "UKBI Peringkat Unggul（スコア 578〜640 / CEFR C1）",
        "intro": "インドネシア国家公認語学試験「UKBI（Uji Kemahiran Berbahasa Indonesia）」において、専門職・大学院進学・高度人材に要求される上位等級「Peringkat Unggul（優等）」をターゲットにした総合模擬問題です。聴解・読解・文法（EYD第5版基準）の実戦的複合問題で即応力を鍛えます。",
        "theory": [
            ("UKBI Peringkat Unggul 到達の要件",
             "1. **Seksi I (聴解 - Mendengarkan)**: 会話の背後にある暗黙の意図（makna tersirat）、話者の感情・アイロニーの正確な識別。\n"
             "2. **Seksi II (文法構造 - Merespons Kaidah)**: EYD第5版に基づく大文字・小文字、複合語の分かち書き、借用語（kata serapan）の正確な綴り。\n"
             "3. **Seksi III (読解 - Membaca)**: 複雑な社会統計図表、学術エッセイの多層的な論理関係の迅速な把握。")
        ],
        "problems": [
            {
                "q": "【UKBI Seksi II 文法正書法】EYD第5版に照らし、正書法上完全に正しい文はどれか？",
                "options": [
                    "A. Kerja sama bilateral tersebut ditandatangani pascaterbitnya peraturan pemerintah.",
                    "B. Kerjasama bilateral tersebut ditandatangani pasca terbitnya peraturan pemerintah.",
                    "C. Kerja-sama bilateral tersebut ditanda tangani pasca-terbitnya peraturan pemerintah.",
                    "D. Kerjasama bilateral tersebut di tandatangani pascaterbitnya peraturan pemerintah."
                ],
                "ans": "A. Kerja sama bilateral tersebut ditandatangani pascaterbitnya peraturan pemerintah.",
                "expl": "1. 「kerja sama」は原則として分かち書きします（複合名詞）。2. 接頭辞「pasca-」は結合要素（bentuk terikat）なので次に来る単語とスペースなしで直結します（pascaterbitnya）。3. 接頭辞と接尾辞が同時に付く場合は直結（ditandatangani）、片方のみなら分かち書き（tanda tangani）となります。これらを満たすのはAのみです。"
            },
            {
                "q": "【UKBI Seksi III 読解論理推論】\n「Pada era revolusi industri 4.0, otomatisasi bukan lagi sebuah pilihan pelengkap, melainkan prasyarat mutlak bagi keberlanjutan korporasi. Kendati demikian, human touch dalam layanan pelanggan tetap menjadi diferensiator utama yang tak tergantikan oleh kecerdasan buatan.」\nこの文章の筆者の主張として最も合致するものはどれか？",
                "options": [
                    "A. 企業の存続には自動化が不可欠であるが、人工知能が代替できない人間味のある顧客対応こそが決定的な差別化要因である。",
                    "B. 自動化は補足的な選択肢に過ぎないため、企業は人工知能の導入を控えて人的サービスの向上に集中すべきである。",
                    "C. 人工知能の発展により顧客サービスにおける人間味は完全に不要となり、全面的な自動化こそが唯一の差別化である。",
                    "D. 自動化と人間味のあるサービスは相反する概念であり、どちらか一方を選択しなければ企業の存続は危うい。"
                ],
                "ans": "A. 企業の存続には自動化が不可欠であるが、人工知能が代替できない人間味のある顧客対応こそが決定的な差別化要因である。",
                "expl": "「bukan lagi pilihan pelengkap, melainkan prasyarat mutlak（補足ではなく絶対的必須条件）」＋「Kendati demikian（しかしながら）」＋「human touch... tetap menjadi diferensiator utama（人間味が主要な差別化要因）」という二項対立の総合がAと完全に合致しています。"
            }
        ],
        "table": [
            ("pascaterbitnya", "〜の発表・発効後（pasca-は直結）"),
            ("kerja sama", "協力・提携（原則として2語に分ける）"),
            ("ditandatangani", "署名される（di-と-iが両方付くため1語に直結）"),
            ("prasyarat mutlak", "絶対的必須条件・不可欠な前提"),
            ("diferensiator utama", "主要な差別化要因"),
            ("keberlanjutan korporasi", "企業の持続可能性")
        ],
        "pro_tip": "UKBIの文法問題（Seksi II）では「pasca-」「antar-」「multi-」「sub-」などの束縛形式（bentuk terikat）が後続語と直結するかどうかを問う問題が必ず出題されます。"
    },
    {
        "filename": "30-mock-exam-ukbi-unggul-02.md",
        "title": "1430. 【実戦模試】UKBI Peringkat Unggul（優等）模擬問題 第2回",
        "level": "UKBI Peringkat Unggul（スコア 578〜640 / CEFR C1）",
        "intro": "UKBI Peringkat Unggul（優等）模擬問題集の第2回です。本稿では、高度なインドネシア語の語形成（morfologi bahasa Indonesia）、外来語の適応ルール（penyerapan kata asing）、および公用報告書・学術論文の批評的読解力を総合的に検証します。",
        "theory": [
            ("外来語の適応規則（Penyerapan Istilah Asing EYD 5）",
             "1. **-tion → -si**: communication → komunikasi, inflation → inflasi, corruption → korupsi。\n"
             "2. **-ty → -tas**: university → universitas, quality → kualitas, authority → otoritas。\n"
             "3. **-ic / -ical → -ik / -is**: economic → ekonomik (sistemik) / ekonomis (hemat), critic → kritik, critical → kritis。\n"
             "4. **-c- / -k- の置換**: coordination → koordinasi, chocolate → cokelat, standard → standar。")
        ],
        "problems": [
            {
                "q": "【外来語綴り・正書法】次の文の中で、外来語のインドネシア語表記（kata serapan）がすべて正しく記述されているものはどれか？",
                "options": [
                    "A. Perusahaan tersebut membutuhkan standardisasi sistem manajemen mutu yang berfokus pada efektivitas dan efisiensi.",
                    "B. Perusahaan tersebut membutuhkan standarisasi sistem manajemen mutu yang berfokus pada efektifitas dan efisiensi.",
                    "C. Perusahaan tersebut membutuhkan standardisasi sistim manajemen mutu yang berfokus pada efektifitas dan efisiensi.",
                    "D. Perusahaan tersebut membutuhkan standarisasi sistem managemen kwalitas yang berfokus pada efektivitas dan efisiensi."
                ],
                "ans": "A. Perusahaan tersebut membutuhkan standardisasi sistem manajemen mutu yang berfokus pada efektivitas dan efisiensi.",
                "expl": "1. standardisation → **standardisasi**（「d」が残る例外。standarisasiは不可）。2. system → **sistem**（sistimは不可）。3. management → **manajemen**（managemenは不可）。4. effectiveness → **efektivitas**（efektifitasは不可）。5. efficiency → **efisiensi**。正しく揃っているのはAのみです。"
            },
            {
                "q": "【読解・文脈換言問題】\n「Upaya revitalisasi kearifan lokal di tengah arus deras modernisasi bukan semata-mata romantisme masa lalu, melainkan manifestasi dari upaya memperkokoh ketahanan budaya bangsa.」\nこの文における「bukan semata-mata romantisme masa lalu」の真意として最も適切なものはどれか？",
                "options": [
                    "A. 単に過去を美化して懐かしむだけの感傷的な行動ではないということ。",
                    "B. 昔の恋愛物語を再現して現代に蘇らせる活動ではないということ。",
                    "C. 歴史的な遺跡を観光地として売り出す商業的意図ではないということ。",
                    "D. 現代文明を完全に否定して古代の生活様式に戻る運動ではないということ。"
                ],
                "ans": "A. 単に過去を美化して懐かしむだけの感傷的な行動ではないということ。",
                "expl": "「romantisme masa lalu（過去のロマン主義・感傷）」に否定の「bukan semata-mata（単に〜ではない）」が付いており、「単に昔を懐かしみ美化する感傷ではない」という意味になります。"
            }
        ],
        "table": [
            ("standardisasi", "標準化・規格化（standarisasiは誤り）"),
            ("efektivitas", "有効性・実効性（efektifitasは誤り）"),
            ("sistem", "システム・体系（sistimは誤り）"),
            ("kearifan lokal", "地域の伝統的知恵・土着の叡智"),
            ("manifestasi", "現れ・具現化・明示"),
            ("ketahanan budaya", "文化的強靭性・文化レジリエンス")
        ],
        "pro_tip": "UKBI Seksi IIで最も多くの受験者が引っかかるのが「standardisasi（正）vs standarisasi（誤）」「efektivitas（正）vs efektifitas（誤）」の綴りです。語幹の末尾文字の規則を徹底的に頭に叩き込んでください。"
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
    table_header = "| 項目・表現 | 解説・ニュアンス・共起表現 |\n| :--- | :--- |\n"
    if a["table"] and len(a["table"][0]) == 4:
        table_header = "| 表現A | 意味・用法 | 表現B | 意味・用法 |\n| :--- | :--- | :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} | **{row[2]}** | {row[3]} |\n"
    elif a["table"] and len(a["table"][0]) == 3:
        table_header = "| 区分・ランク | 点数・表現 | 特徴・解説 |\n| :--- | :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | **{row[1]}** | {row[2]} |\n"
    else:
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "インドネシア語技能検定・UKBI対策シリーズ。{a['title']}の出題傾向、解法セオリー、実戦想定問題、詳細解説まで徹底指導。"
---

<div class="category-badge">検定・UKBI実戦対策</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 試験の傾向と出題意図

{a['intro']}

---

## 2. 攻略フレームワーク・解法セオリー

{theory_content}
---

## 3. 実戦想定問題と詳細解説

本番試験と同等レベルのオリジナル想定問題です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要語彙・構文対比テーブル

本セクションのテーマに関連する最重要語彙・成句の対比一覧です。

{table_header}{table_rows}
---

## 5. 合格者の着眼点・プロのアドバイス

> [!TIP]
> **合格のためのワンポイント・アドバイス**:
> {a['pro_tip']}

---

## 6. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "exam-advanced")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
