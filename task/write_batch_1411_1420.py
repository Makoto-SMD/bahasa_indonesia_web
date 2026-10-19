# -*- coding: utf-8 -*-
"""
セクション34 第2バッチ (1411-1420) 記事生成スクリプト
【資格演習】検定・UKBI直前実戦模試＆徹底解説
特A級対策・UKBIリスニング・正書法EYD5・学術読解
"""

import os

articles = [
    {
        "filename": "11-inken-special-a-legal-treaty.md",
        "title": "1411. 【技能検定特A級対策】国際条約・法律条文の翻訳：格調高き定型表現の処理",
        "level": "技能検定特A級（CEFR C2 / プロフェッショナル翻訳者）",
        "intro": "インドネシア語技能検定の最高峰「特A級」において、合否を分ける最難関課題が『国際条約・二国間協定・インドネシア法律条文（Undang-Undang）』の高度な翻訳です。オランダ法理に由来する厳格な法令構文、特有のプレアンブル定型句（Menimbang, Mengingat, Menetapkan）、および絶対的な法的精度を保証する定訳ルールを徹底解説します。",
        "theory": [
            ("法律条文（Undang-Undang）の構造と定型表現",
             "1. **前文・考慮事項（Menimbang）**: 法律制定の社会的・経済的背景。「〜を考慮して（Considering that...）」の定訳。\n"
             "2. **根拠法令（Mengingat）**: 憲法第5条や上位法の明記。「〜に鑑み、〜に基づき（In view of...）」の定訳。\n"
             "3. **決定宣言（MEMUTUSKAN / Menetapkan）**: 「以下のように制定・決定する（HAS DECIDED / To enact...）」の定型句。\n"
             "4. **条・項・号の呼称体系**: Pasal（第〜条）、ayat（第〜項）、huruf（〜号/アルファベット）、angka（〜号/数字）。"),
            ("条約・契約書における義務・禁止・権利の助動詞",
             "- **義務（shall）**: **wajib** または **harus**。契約当事者の法的作為義務を明示。\n"
             "- **禁止（shall not）**: **dilarang** または **tidak boleh**。不作為義務の明示。\n"
             "- **権利・裁量（may）**: **berhak** または **dapat**。作為権能の付与。\n"
             "- **失効・無効（null and void）**: **batal demi hukum**（法律上当然無効）。"),
            ("二国間投資協定（BIT）等の頻出フレーズ",
             "- **Perlakuan yang Adil dan Merata**: 公平かつ衡平な待遇（Fair and Equitable Treatment: FET）。\n"
             "- **Klausul Bangsa yang Paling Diuntungkan**: 最恵国待遇条項（Most-Favoured-Nation Clause: MFN）。\n"
             "- **Penyelesaian Sengketa**: 紛争解決（Dispute Settlement）。")
        ],
        "problems": [
            {
                "q": "【条文翻訳想定問題】次の条文の日本語訳として最も法的に正確なものはどれか？\n\n\"Perjanjian ini mulai berlaku pada tanggal pertukaran instrumen ratifikasi dan tetap berlaku untuk jangka waktu sepuluh tahun, kecuali salah satu Pihak memberitahukan secara tertulis niatnya untuk mengakhiri Perjanjian ini enam bulan sebelum berakhirnya masa berlaku tersebut.\"",
                "options": [
                    "A. 本協定は批准書の交換の日に効力を生じ、一方の当事国が効力期間の満了の6箇月前に本協定を終了させる意図を書面により通告しない限り、10年の期間効力を有する。",
                    "B. この契約は批准書を交換した日から有効になり、10年間ずっと効力があるが、どちらかが終わらせたいと手紙で6ヶ月前に言えば別である。",
                    "C. 批准書の交換が行われた日をもって本条約は開始し、10年間の間は効力を保つが、片方の国がやめたい意向を6ヶ月前に書けば終了する。",
                    "D. 本合意は批准書類がやり取りされた日付から発効し、いずれかの国が6ヶ月以内に終了通知を出さない場合、永久に10年有効である。"
                ],
                "ans": "A. 本協定は批准書の交換の日に効力を生じ、一方の当事国が効力期間の満了の6箇月前に本協定を終了させる意図を書面により通告しない限り、10年の期間効力を有する。",
                "expl": "「mulai berlaku（効力を生ずる/発効する）」「instrumen ratifikasi（批准書）」「tetap berlaku untuk jangka waktu...（〜の期間効力を有する）」「memberitahukan secara tertulis（書面により通告する）」という日本の条約公用文の厳格な定型表現に完全に一致しているのはAのみです。"
            },
            {
                "q": "インドネシアの法律条文において「法律上当然に無効である（null and void by operation of law）」を意味する法廷用語はどれか？",
                "options": ["A. batal demi hukum", "B. dibatalkan hakim", "C. tidak sah perdata", "D. kadaluwarsa hukum"],
                "ans": "A. batal demi hukum",
                "expl": "オランダ法（van rechtswege nietig）に由来する法廷ラテン語・法学用語の定訳は「batal demi hukum（法律上当然無効）」です。"
            }
        ],
        "table": [
            ("Menimbang", "〜を考慮して（法律の考慮事項・前文）"),
            ("Mengingat", "〜に鑑み（根拠法令の明記）"),
            ("Menetapkan", "以下を制定する・定める（決定事項）"),
            ("batal demi hukum", "法律上当然無効（null and void）"),
            ("sengketa penanaman modal", "投資紛争（investment dispute）"),
            ("ganti rugi yang memadai", "十分かつ妥当な補償（adequate compensation）")
        ],
        "pro_tip": "特A級の条文翻訳では、日常会話的な意訳は減点対象となります。「shall＝〜するものとする」「may＝〜することができる」「Pihak＝当事国/当事者」といった公用文の統語規則を死守してください。"
    },
    {
        "filename": "12-inken-special-a-simultaneous.md",
        "title": "1412. 【技能検定特A級対策】通訳・即時要約の技術：情報の取捨選択と瞬発力",
        "level": "技能検定特A級（CEFR C2 / 国際会議通訳）",
        "intro": "特A級二次試験（口頭試験）では、高速で読み上げられる公式スピーチや記者会見の音声を聴き、即座に要点を抽出して正確な日本語またはインドネシア語で再現する「逐次通訳・即時要約・ラギング（Lagging）」の技術が試されます。情報処理のキャパシティを超えないためのノートテイキングとデカプリング技法を伝授します。",
        "theory": [
            ("プロ通訳者の情報処理3大ステップ",
             "1. **聴解と脱言語化（Deverbalization）**: 単語の一言一句に囚われず、話者の「思考・メッセージの骨格」を頭の中に映像・概念として保持する。\n"
             "2. **スマート・ノートテイキング（Note-taking）**: 主語（S）、矢印（原因→結果）、数字、固有名詞のみをシンボル化して瞬時にメモする。\n"
             "3. **先頭からの構文再構築（Chunking / Lagging）**: 後戻りして修飾せず、前から句ごとに「〜であり、〜のため、〜となった」と順送りに訳出する。"),
            ("数字・単位の瞬時変換テクニック",
             "- **1 juta** ＝ 100万（百万）\n"
             "- **10 juta** ＝ 1,000万（一千万）\n"
             "- **100 juta** ＝ 1億（一億）\n"
             "- **1 miliar** ＝ 10億（十億）\n"
             "- **10 miliar** ＝ 100億（百億）\n"
             "- **1 triliun** ＝ 1兆（一兆）")
        ],
        "problems": [
            {
                "q": "【即時通訳・数字変換問題】\nインドネシア側首脳が「Realisasi investasi asing kuartal ini menembus angka 150 triliun rupiah, melonjak 18 persen dibanding periode yang sama tahun lalu.」と発言した。最も正確な通訳訳出はどれか？",
                "options": [
                    "A. 今期の外国投資実行額は150兆ルピアを突破し、前年同期比で18パーセントの急増となりました。",
                    "B. 今期の海外投資額は1500億ルピアに達し、去年の同じ時期に比べて18パーセント伸びました。",
                    "C. 今期の外国直接投資は15兆ルピアを超え、前年に比べて18パーセント上がりました。",
                    "D. 今期の投資受け入れ額は150億ルピアとなり、去年同期比で18パーセント増えました。"
                ],
                "ans": "A. 今期の外国投資実行額は150兆ルピアを突破し、前年同期比で18パーセントの急増となりました。",
                "expl": "「150 triliun rupiah」は日本語で「150兆ルピア」です。melonjak は単なる増加（naik）ではなく「急増・跳ね上がった」ニュアンスを持ち、Realisasi investasi は「投資実行額」の定訳です。"
            }
        ],
        "table": [
            ("1 juta", "100万（百万）"),
            ("100 juta", "1億（一億）"),
            ("1 miliar", "10億（十億）"),
            ("100 miliar", "1,000億（一千億）"),
            ("1 triliun", "1兆（一兆）"),
            ("100 triliun", "100兆（百兆）")
        ],
        "pro_tip": "通訳現場で最も失点しやすいのが「数字の桁の混乱」です。「1 miliar ＝ 10億」「1 triliun ＝ 1兆」の2大アンカーを呪文のように暗記し、0.5秒で変換できるように自動化してください。"
    },
    {
        "filename": "13-ukbi-overview-scoring-bands.md",
        "title": "1413. 【UKBI能力評価試験】試験構成・評価基準（Peringkat）とスコアアップ戦略",
        "level": "UKBI能力評価試験（Peringkat Unggul〜Istimewa / CEFR B2〜C2）",
        "intro": "インドネシア共和国教育文化研究技術省・言語育成開発局（Badan Bahasa）が主催する国家公認のインドネシア語能力検定「UKBI（Uji Kemahiran Berbahasa Indonesia）」。外国人専門職の就労ビザ取得や大学院進学、国費留学生選考で必須となる本試験の全体構成と、最上位ランク（Unggul / Istimewa）を奪取するための総合戦略を解説します。",
        "theory": [
            ("UKBIの試験構成（5つのセクション）",
             "1. **Seksi I: Mendengarkan（リスニング・聴解）**: 40問（日常会話、アナウンス、学術講義、インタビュー）。音声は1回のみ再生。\n"
             "2. **Seksi II: Merespons Kaidah（文法規則・正書法）**: 25問（EYD第5版、接辞、語彙、助詞、構文の正誤選択）。\n"
             "3. **Seksi III: Membaca（リーディング・読解）**: 40問（図表、案内文、学術論文、論説、文学作品）。\n"
             "4. **Seksi IV: Menulis（記述・エッセイ）**: パケット選択式（学術要約・論述）。\n"
             "5. **Seksi V: Berbicara（スピーキング・口頭発表）**: テーマ別プレゼンテーション。"),
            ("UKBI評価ランク（Peringkat）とスコア対比",
             "- **Istimewa（特級・最高峰）**: 725〜800点（母語話者の学者・プロ通訳水準 / CEFR C2）\n"
             "- **Sangat Unggul（最優等）**: 641〜724点（高度な学術・政策・報道の完全運用 / CEFR C1）\n"
             "- **Unggul（優等）**: 578〜640点（大学院教育・専門職就労に十分な水準 / CEFR B2）\n"
             "- **Madya（中等）**: 482〜577点（一般的なビジネス・日常実務 / CEFR B1）\n"
             "- **Semenjana（初等）**: 405〜481点（日常サバイバル会話 / CEFR A2）")
        ],
        "problems": [
            {
                "q": "UKBI試験において、外国人専門職や大学院進学で標準的に求められる「Peringkat Unggul（優等）」の獲得に必要なスコア範囲はどれか？",
                "options": ["A. 405〜481点", "B. 482〜577点", "C. 578〜640点", "D. 725〜800点"],
                "ans": "C. 578〜640点",
                "expl": "UKBIの「Peringkat Unggul」は578〜640点です。482〜577点はMadya、641〜724点はSangat Unggul、725点以上が最高位のIstimewaです。"
            }
        ],
        "table": [
            ("Istimewa", "725〜800点", "CEFR C2（最高特級・完全な学術・言語運用力）"),
            ("Sangat Unggul", "641〜724点", "CEFR C1（最優等・政策立案・高度ジャーナリズム）"),
            ("Unggul", "578〜640点", "CEFR B2（優等・大学院進学・高度専門職ビザ要件）"),
            ("Madya", "482〜577点", "CEFR B1（中等・ビジネス実務・現場マネジメント）"),
            ("Semenjana", "405〜481点", "CEFR A2（初等・基礎的日常業務）")
        ],
        "pro_tip": "UKBIのリスニング（Seksi I）は音声が1回しか流れません。問題文と選択肢を音声が始まる前の数秒間で先読み（スキャニング）する反射神経が勝負を分けます。"
    },
    {
        "filename": "14-ukbi-seksi-1-listening-social.md",
        "title": "1414. 【UKBI第1セクション】リスニング攻略：日常会話・インタビューの聞き取り",
        "level": "UKBI Seksi I（CEFR B1〜B2）",
        "intro": "UKBIの第1セクション（Mendengarkan）前半では、公共交通機関のアナウンス、職場の同僚間の打ち合わせ、ラジオインタビューなどが出題されます。自然な発話スピード、地域のアクセント（ジャワ訛り、スンダ訛り等）、および間投詞や口語短縮形が混入する会話から、話者の意図（tujuan）、時間・場所、トラブルの核心を即座に聞き分けるテクニックを解説します。",
        "theory": [
            ("Seksi I 前半の3大頻出シチュエーション",
             "1. **公共交通・インフラ・気象アナウンス**: 列車の遅延理由、搭乗口の変更、豪雨や強風による運行見合わせ。\n"
             "2. **オフィス・業務調整の対話**: 会議の日程繰り上げ（dimajukan）、資料の差し替え、予算配分の修正。\n"
             "3. **ラジオ・ポッドキャストの専門家インタビュー**: 健康管理、伝統食の保存、若手起業家の成功体験。"),
            ("聞き取りの重要アンカーワード",
             "- **逆接・転換**: tetapi, namun, sayangnya, padahal（話者の本音・真のトラブルはここ以降に来る）。\n"
             "- **時間・条件**: ditunda（延期）, dialihkan（振り替え）, dibatalkan（中止）。")
        ],
        "problems": [
            {
                "q": "【リスニング音声スクリプト想定問題】\n(Suara Petugas Stasiun): \"Perhatian para penumpang Kereta Api Argo Parahyangan tujuan Bandung. Sehubungan dengan adanya perbaikan bantalan rel di km 45, keberangkatan kereta yang semula dijadwalkan pukul 14.15 terpaksa kami tunda selama tiga puluh menit. Kami mohon maaf atas ketidaknyamanan ini.\"\n\n**設問: Kapan Kereta Api Argo Parahyangan diperkirakan berangkat?**",
                "options": ["A. Pukul 14.15", "B. Pukul 14.30", "C. Pukul 14.45", "D. Pukul 15.15"],
                "ans": "C. Pukul 14.45",
                "expl": "当初の出発予定は14時15分（14.15）で、線路改修のため30分延期（ditunda selama tiga puluh menit）されたため、実際の出発予定時刻は14時45分（14.45）となります。"
            }
        ],
        "table": [
            ("sehubungan dengan", "〜に関連して・〜のため（理由提示）"),
            ("perbaikan rel", "線路の改修・保守工事"),
            ("ditunda", "延期される・見合わされる"),
            ("dialihkan", "迂回・振り替えされる"),
            ("peron keberangkatan", "出発ホーム")
        ],
        "pro_tip": "数字や時刻の聞き取り問題では、問題用紙の余白に数字をメモしながら、足し算（遅延時間）や引き算の計算を頭の中で瞬時に行ってください。"
    },
    {
        "filename": "15-ukbi-seksi-1-listening-academic.md",
        "title": "1415. 【UKBI第1セクション】リスニング攻略：学術講義・公式スピーチの論理把握",
        "level": "UKBI Seksi I（CEFR C1 / 上級〜最上級）",
        "intro": "UKBI Seksi I の後半（Dialog / Monolog Panjang）では、大学の学術シンポジウム、大臣の公式演説、環境学・地質学・文化人類学の本格的モノローグが長文で流れます。学術専門用語（terminologi ilmiah）を的確にキャッチし、論理の因果関係（sebab-akibat）とスピーカーの結論を把握するハイレベル・リスニング戦略を伝授します。",
        "theory": [
            ("学術モノローグの論理展開パターン",
             "1. **現象の提示（Fenomena）**: 地球温暖化、生物多様性の喪失、伝統言語の消滅危機の現状。\n"
             "2. **科学的メカニズム（Mekanisme Ilmiah）**: 温室効果ガス排出、泥炭地の乾燥、若年層の都市移動。\n"
             "3. **研究成果・実証データ（Temuan Riset）**: 大学や研究機関（BRIN等）による最新の調査数値。\n"
             "4. **提言・政策的結論（Rekomendasi Kebijakan）**: 国際協力、規制強化、持続可能な代替案。")
        ],
        "problems": [
            {
                "q": "【学術モノローグ音声スクリプト想定問題】\n(Suara Pembicara): \"Lahan gambut tropis di Kalimantan menyimpan cadangan karbon raksasa yang krusial bagi stabilitas iklim bumi. Sayangnya, praktik pengeringan gambut melalui pembuatan kanal untuk perkebunan monokultur telah menyebabkan subsidensi tanah dan memicu kerentanan kebakaran hebat saat musim El Nino. Riset kami membuktikan bahwa restorasi hidrologis melalui penyekatan kanal (canal blocking) mampu menaikkan kembali muka air tanah dan menekan emisi karbon hingga enam puluh persen.\"\n\n**設問: Apa solusi teknis yang direkomendasikan pembicara untuk merestorasi lahan gambut?**",
                "options": [
                    "A. Memperluas pembuatan kanal irigasi untuk perkebunan kelapa sawit.",
                    "B. Melakukan penyekatan kanal guna menaikkan muka air tanah.",
                    "C. Mengeringkan lahan gambut secara permanen sebelum musim El Nino.",
                    "D. Mengganti seluruh vegetasi hutan gambut dengan tanaman semusim."
                ],
                "ans": "B. Melakukan penyekatan kanal guna menaikkan muka air tanah.",
                "expl": "スピーカーは「restorasi hidrologis melalui penyekatan kanal (canal blocking) mampu menaikkan kembali muka air tanah（水路の堰き止めによる水文学的再生が地下水位を回復させる）」と明言しているため、Bが正解です。"
            }
        ],
        "table": [
            ("cadangan karbon", "炭素貯留量・カーボンストック"),
            ("subsidensi tanah", "地盤沈下"),
            ("penyekatan kanal", "水路の堰き止め（canal blocking）"),
            ("muka air tanah", "地下水位"),
            ("kerentanan kebakaran", "火災脆弱性・火災リスク")
        ],
        "pro_tip": "学術リスニングでは、「Riset kami membuktikan bahwa...（私たちの研究は〜を証明した）」というフレーズの直後に、設問の正解となる結論が必ず提示されます。"
    },
    {
        "filename": "16-ukbi-seksi-2-grammar-mechanics.md",
        "title": "1416. 【UKBI第2セクション】文法・正書法（EYD第5版）完全対応ドリル",
        "level": "UKBI Seksi II（CEFR B2〜C1）",
        "intro": "UKBIの第2セクション（Merespons Kaidah）は、インドネシア語の正書法ガイドライン『EYD第5版（Ejaan Bahasa Indonesia yang Disempurnakan Edisi V）』の規則、助詞の分かち書き、句読点（約物）、大文字表記、外来語綴りを正確に識別する文法テストです。受験者が最も失点しやすい急所を網羅ドリル形式で特訓します。",
        "theory": [
            ("EYD第5版の最重要チェックポイント",
             "1. **助詞 pun の分かち書きと一語化**: 原則として前単語と分かち書きする（例: apa pun, saya pun）。ただし慣用的に一語化される12語（adapun, andaikanpun, ataupun, bagaimanapun, biarpun, kalaupun, kendatipun, maupun, meskipun, sekalipun, sungguhpun, walaupun）は一語で書く。\n"
             "2. **助詞 per の分かち書き**: 「〜ごとに（tiap-tiap）」「〜から（mulai）」「〜につき（demi）」を意味する per は分かち書き（例: per orang, per 1 Januari）。分数接頭辞の per-（perenam＝6分の1）のみ一語。\n"
             "3. **大文字表記の基準**: 国名・民族名・言語名は頭文字大文字（bangsa Indonesia, bahasa Jepang）。しかし派生語化された場合は小文字（keindonesiaan, diindonesiakan）。\n"
             "4. **ハイフン（-）の必須用法**: アルファベットと数字（ke-5）、小文字と大文字（se-Indonesia, ber-KTP）、神への接尾詞（hamba-Mu）はハイフンで繋ぐ。")
        ],
        "problems": [
            {
                "q": "次の文のうち、EYD第5版の正書法に照らして完全に正しい文はどれか？",
                "options": [
                    "A. Bagaimanapun sulit nya situasi ekonomi, kita tidak boleh berputus asa.",
                    "B. Bagaimanapun sulitnya situasi ekonomi, kita tidak boleh berputus asa.",
                    "C. Bagaimana pun sulitnya situasi ekonomi, kita tidak boleh berputus asa.",
                    "D. Bagaimanapun sulitnya situasi ekonomi, kita tidak boleh ber-putus asa."
                ],
                "ans": "B. Bagaimanapun sulitnya situasi ekonomi, kita tidak boleh berputus asa.",
                "expl": "bagaimanapun は慣用的に一語化される12語の1つなので一語で綴ります。代名詞接語 -nya は前の単語に密着して書くため「sulitnya」が正しく、Bが完全な正解です。"
            },
            {
                "q": "次のうち、助詞「per」の使い方が正しいものはどれか？",
                "options": [
                    "A. Harga tiket masuk museum dinaikkan menjadi sepuluh ribu rupiah perorang.",
                    "B. Harga tiket masuk museum dinaikkan menjadi sepuluh ribu rupiah per orang.",
                    "C. Harga tiket masuk museum dinaikkan menjadi sepuluh ribu rupiah per-orang.",
                    "D. Harga tiket masuk museum dinaikkan menjadi sepuluh ribu rupiah pero rang."
                ],
                "ans": "B. Harga tiket masuk museum dinaikkan menjadi sepuluh ribu rupiah per orang.",
                "expl": "「1人につき・1人ごとに（tiap-tiap orang）」を表す助詞 per は、後続の名詞と分かち書きして「per orang」と書くのがEYD規則です。"
            }
        ],
        "table": [
            ("一語化される pun", "bagaimanapun, meskipun, walaupun, maupun, ataupun, biarpun"),
            ("分かち書きする pun", "siapa pun, apa pun, satu kali pun, malam pun"),
            ("分かち書きする per", "per orang, per kilogram, per 1 April"),
            ("ハイフン接続", "ke-77, se-Jawa Barat, mem-PHK, hamba-Mu"),
            ("小文字化される派生語", "mengindonesiakan kata asing, kejawa-jawaan")
        ],
        "pro_tip": "EYD問題で迷ったら、「pun は基本バラバラ（分かち書き）、12語だけ合体」と覚えておけば、9割の問題を瞬殺できます。"
    },
    {
        "filename": "17-ukbi-seksi-2-word-formation.md",
        "title": "1417. 【UKBI第2セクション】接辞・造語法・派生語の正誤判定トレーニング",
        "level": "UKBI Seksi II（CEFR B2〜C1）",
        "intro": "UKBI Seksi II において文法知識の深さが最も露骨に試されるのが、接頭辞・接尾辞・周囲辞の音韻変化規則（morfofonemik）および外来語の借用接尾辞（-isasi, -itas, -al）の正誤判定です。大辞典KBBI（Kamus Besar Bahasa Indonesia）の基準に準拠した正当な造語法を体系化します。",
        "theory": [
            ("音韻同化・鼻音化の厳格ルール（meN- / peN-）",
             "1. **K-P-S-Tの脱落規則**: 語根の頭文字が k, p, s, t で、第2母音が母音の場合、頭文字は鼻音化して脱落する（例: tulis → menulis, kirim → mengirim, sapu → menyapu, potong → memotong）。\n"
             "2. **脱落の例外（二重子音クラスタ）**: 語根頭文字が二重子音（kr, pr, sk, st, tr等）の外来語の場合、脱落しない（例: kritik → mengkritik, proses → memproses, transfer → mentransfer）。\n"
             "3. **二重接頭辞 memper- の注意点**: memper- の後ろに形容詞が来る場合、接尾辞 -kan を重ねてはならない（誤: memperbesarkan → 正: memperbesar）。")
        ],
        "problems": [
            {
                "q": "次の動詞表現のうち、KBBIおよびEYD第5版の造語規則に照らして「誤っているもの（不適切な重複）」はどれか？",
                "options": ["A. memperbesar", "B. memperluas", "C. mempercepatkan", "D. memperindah"],
                "ans": "C. mempercepatkan",
                "expl": "二重接頭辞 memper- に形容詞（cepat）が付く場合、それ自体で「〜をより速くする（比較使役）」意味を持つため、使役接尾辞 -kan を重ねて「mempercepatkan」とするのは文法的な重複誤用（pleonasme）です。正しくは「mempercepat」または「mencepatkan」です。"
            },
            {
                "q": "外来語語根「konfirmasi（確認）」に接頭辞 meN- と接尾辞 -kan が結合した正しい表記はどれか？",
                "options": ["A. mengonfirmasikan", "B. mengkonfirmasikan", "C. menkonfirmasi", "D. mekonfirmasikan"],
                "ans": "A. mengonfirmasikan",
                "expl": "語根 konfirmasi の頭文字 k の後ろは母音 o であるため、K-P-S-T脱落規則（鼻音化 ng への置換）が適用され、「mengonfirmasikan」となるのが公的標準語法（Bahasa Baku）です。"
            }
        ],
        "table": [
            ("memper- + 形容詞（正）", "memperbesar, memperluas, memperdalam, memperjelas"),
            ("memper- + 形容詞 + -kan（誤）", "memperbesarkan, memperluaskan, memperdalamkan"),
            ("外来語 k 脱落（正）", "mengonfirmasi, mengoordinasi, mengonsumsi"),
            ("外来語 二重子音維持（正）", "mempromosikan, mengkritik, mentransfer, memprogram"),
            ("名詞借用接尾辞", "-isasi（globalisasi）, -itas（aktivitas）, -isme（patriotisme）")
        ],
        "pro_tip": "日常のニュースや口語では「mengkonfirmasi」「memperbaiki」などの誤用や混同が散見されますが、UKBIの正書法試験ではKBBIに厳格に準拠して「mengonfirmasi」が正解となります。"
    },
    {
        "filename": "18-ukbi-seksi-3-reading-charts-tables.md",
        "title": "1418. 【UKBI第3セクション】図表・インフォグラフィックス読み取り読解法",
        "level": "UKBI Seksi III（CEFR B2〜C1）",
        "intro": "UKBIの第3セクション（Membaca）で必ず出題されるのが、棒グラフ、折れ線グラフ、円グラフ、統計表、およびインフォグラフィックス（infografik）の複合読解問題です。数値を素早く対比し、最大の伸び率（lonjakan tertinggi）や減少傾向（tren penurunan）を客観的に読み取る解法テクニックを伝授します。",
        "theory": [
            ("図表読解の3大チェックポイント",
             "1. **タイトルと単位（Judul dan Satuan）**: 縦軸・横軸の単位が persen（％）なのか jiwa（人）なのか rupiah（ルピア）なのかを最初に見る。\n"
             "2. **極値の確認（Nilai Ekstrem）**: 最も高い数値（tertinggi / puncak）と最も低い数値（terendah / titik nadir）を特定する。\n"
             "3. **トレンドの推移（Arah Tren）**: berfluktuasi（変動している）, stagnan（横ばい）, konsisten meningkat（一貫して上昇）などの動詞・形容詞の選択肢を見極める。")
        ],
        "problems": [
            {
                "q": "【統計表想定読解】\n[Tabel: Tingkat Inflasi Tahunan Indonesia (2020-2023)]\n- Tahun 2020: 1,68%\n- Tahun 2021: 1,87%\n- Tahun 2022: 5,51%\n- Tahun 2023: 2,61%\n\n**設問: Berdasarkan data tabel di atas, pernyataan manakah yang paling akurat?**",
                "options": [
                    "A. Laju inflasi Indonesia selalu mengalami kenaikan konsisten setiap tahun.",
                    "B. Puncak inflasi tertinggi terjadi pada tahun 2022 sebelum melandai kembali pada tahun 2023.",
                    "C. Tingkat inflasi pada tahun 2023 merupakan yang terendah dalam empat tahun terakhir.",
                    "D. Inflasi tahun 2021 meningkat lebih dari tiga kali lipat dibanding tahun 2020."
                ],
                "ans": "B. Puncak inflasi tertinggi terjadi pada tahun 2022 sebelum melandai kembali pada tahun 2023.",
                "expl": "2022年に5.51%という最高値（puncak tertinggi）を記録し、2023年には2.61%へと沈静化・下降（melandai）しているため、Bが完全にデータと一致する正解です。"
            }
        ],
        "table": [
            ("melandai", "（急上昇の後に）緩やかになる・落ち着く"),
            ("berfluktuasi", "激しく上下に変動する"),
            ("stagnan", "停滞している・横ばいである"),
            ("titik puncak", "最高点・ピーク"),
            ("titik terendah", "最下点・底（nadir）"),
            ("lonjakan signifikan", "顕著な急増・跳ね上がり")
        ],
        "pro_tip": "グラフ問題では、本文を見ずに「selalu（常に）」「semua（すべて）」といった全称命題の選択肢をまず疑い、具体的な数値対比を行っている選択肢を優先的に検証してください。"
    },
    {
        "filename": "19-ukbi-seksi-3-reading-scientific.md",
        "title": "1419. 【UKBI第3セクション】自然科学・テクノロジー学術論文の読解演習",
        "level": "UKBI Seksi III（CEFR C1〜C2）",
        "intro": "UKBI最上位ランク（Sangat Unggul / Istimewa）を狙う上で最大の関門となるのが、自然科学、再生可能エネルギー、バイオテクノロジー、海洋生態系に関する査読付き学術論文（Jurnal Ilmiah）の長文読解です。高度な専門述語（jargon ilmiah）と緻密な論理因果関係を解き明かす読解法を解説します。",
        "theory": [
            ("学術論文（Jurnal Ilmiah）の定型構造（IMRAD）",
             "1. **Pendahuluan（Introduction）**: 研究背景、先行研究の限界、本研究のリサーチクエスチョン。\n"
             "2. **Metode Penelitian（Methods）**: 実験手法、サンプリング、データ解析アルゴリズム。\n"
             "3. **Hasil dan Pembahasan（Results & Discussion）**: 実証データの提示、統計的有意性、科学的メカニズムの解釈。\n"
             "4. **Kesimpulan（Conclusion）**: 研究の学術的貢献と今後の研究課題。")
        ],
        "problems": [
            {
                "q": "【論文読解想定問題】\n\"Hasil analisis spektroskopi menunjukkan bahwa nanopartikel perak yang disintesis menggunakan ekstrak daun sirih merah memiliki aktivitas antibakteri yang signifikan terhadap Staphylococcus aureus. Mekanisme penghambatan tersebut berkaitan erat dengan kemampuan nanopartikel menembus dinding sel bakteri, merusak integritas membran selular, dan menginduksi stres oksidatif intraseluler yang berujung pada lisis sel.\"\n\n**設問: Bagaimana nanopartikel perak daun sirih merah menyebabkan kematian sel bakteri?**",
                "options": [
                    "A. Dengan memperkuat ketebalan dinding sel bakteri dari serangan luar.",
                    "B. Melalui perusakan membran sel dan induksi stres oksidatif yang melisiskan sel.",
                    "C. Mengubah bakteri menjadi organisme yang bermanfaat bagi inang.",
                    "D. Menghentikan proses sintesis nanopartikel di dalam laboratorium."
                ],
                "ans": "B. Melalui perusakan membran sel dan induksi stres oksidatif yang melisiskan sel.",
                "expl": "本文に「merusak integritas membran selular, dan menginduksi stres oksidatif intraseluler yang berujung pada lisis sel（細胞膜の完全性を破壊し、細胞融解に至る細胞内酸化ストレスを誘導する）」と明記されているため、Bが科学的に完全に合致する正解です。"
            }
        ],
        "table": [
            ("sintesis nanopartikel", "ナノ粒子の合成"),
            ("aktivitas antibakteri", "抗菌活性"),
            ("stres oksidatif", "酸化ストレス"),
            ("lisis sel", "溶菌・細胞融解"),
            ("signifikan secara statistik", "統計的に有意な")
        ],
        "pro_tip": "難解な自然科学論文の読解では、未知の専門用語にパニックにならず、「A menyebabkan B yang berujung pada C（AがBを引き起こし、それがCという結果に至る）」という因果関係の矢印だけを追跡してください。"
    },
    {
        "filename": "20-ukbi-seksi-3-reading-literature.md",
        "title": "1420. 【UKBI第3セクション】現代文学・エッセイの行間を読む高度読解",
        "level": "UKBI Seksi III（CEFR C1〜C2）",
        "intro": "UKBI Seksi III の最終盤に登場するのが、インドネシアの現代作家（プラムディヤ、セノ・グミラ・アジダルマ、アユ・ウタミ等）の短編小説や文芸エッセイからの抜粋です。比喩表現（metafora）、暗示（makna tersirat）、登場人物の心理的葛藤を正確に読み解く文芸的読解力を養成します。",
        "theory": [
            ("文芸テキスト読解の3つの着眼点",
             "1. **比喩・メタファーの解読**: 「langit mendung di matanya（彼の目に宿る曇り空＝悲哀・絶望）」「menelan ludah kepahitan（苦渋の唾を飲み込む＝無念さを耐える）」。\n"
             "2. **語り手の視点（Sudut Pandang）**: 一人称視点（aku/saya）による主観的告白か、三人称全知視点（dia/nama tokoh）か。\n"
             "3. **暗示された主題（Tema Tersirat）**: 文字通りの筋書きの裏に隠された「社会的不平等、権力への批判、実存的孤独」のメッセージを捉える。")
        ],
        "problems": [
            {
                "q": "【文学テキスト抜粋想定問題】\n\"Pak Karto menatap sepetak sawah warisan leluhurnya yang kini telah dipagari seng keliling oleh alat-alat berat pengembang kawasan industri. Debu semen telah menggantikan harum tanah basah yang selama puluhan tahun menjadi napas hidupnya. Di tangannya, cangkul tua itu terasa begitu berat—bukan karena beban besinya, melainkan karena ia tahu, esok hari tak ada lagi sejengkal tanah pun yang menunggunya untuk dicangkul.\"\n\n**設問: Apa makna tersirat dari kalimat 'cangkul tua itu terasa begitu berat' pada kutipan cerpen di atas?**",
                "options": [
                    "A. Cangkul tersebut terbuat dari jenis logam besi yang sangat padat dan baru dibeli.",
                    "B. Pak Karto sedang menderita penyakit fisik parah sehingga tangannya melemah.",
                    "C. Perasaan duka mendalam dan keputusasaan karena kehilangan tanah garapan untuk selamanya.",
                    "D. Keinginan Pak Karto untuk segera menjual cangkulnya ke pabrik daur ulang semen."
                ],
                "ans": "C. Perasaan duka mendalam dan keputusasaan karena kehilangan tanah garapan untuk selamanya.",
                "expl": "直後の「bukan karena beban besinya, melainkan karena ia tahu, esok hari tak ada lagi sejengkal tanah pun yang menunggunya（鉄の重さゆえではなく、明日には耕す土地が一寸も残されていないと悟ったからだ）」から明らかなように、鍬の重さは先祖代々の農地を失った深い悲痛と絶望の心理的メタファーであるため、Cが正解です。"
            }
        ],
        "table": [
            ("makna tersurat", "文字通りの明示的な意味"),
            ("makna tersirat", "行間に隠された暗示的・象徴的意味"),
            ("latar suasana", "情景・雰囲気の背景描写"),
            ("sudut pandang persona", "語り手の視点（人称）"),
            ("resolusi konflik", "葛藤・紛争の結末・解決")
        ],
        "pro_tip": "文学読解の設問で「makna tersirat（暗示された意味）」を問われた場合、物理的・字面通りの説明をしている選択肢（AやBなど）は真っ先に消去し、心理描写や社会的テーマに踏み込んだ選択肢を選んでください。"
    }
]

def generate_markdown(a):
    theory_content = ""
    for title, desc in a["theory"]:
        theory_content += f"""### {title}
{desc}

"""

    problem_items = ""
    for idx, p in enumerate(a["problems"], 1):
        opts_str = "\n".join([f"- {opt}" for opt in p["options"]])
        problem_items += f"""#### 第{idx}問
{p['q']}

{opts_str}

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
