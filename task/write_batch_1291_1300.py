# -*- coding: utf-8 -*-
"""
Generate Section 31 Batch 5 Articles (1291-1300):
- 1291: docs/lexicon/41-adjective-collocations-sangat.md
- 1292: docs/lexicon/42-adjective-collocations-mutlak.md
- 1293: docs/lexicon/43-frequency-adverbs-collocations.md
- 1294: docs/lexicon/44-prepositional-chunks-collocations.md
- 1295: docs/lexicon/45-discourse-markers-connectors.md
- 1296: docs/lexicon/46-idiomatic-pairs-synonyms.md
- 1297: docs/lexicon/47-antonymic-pairs-balance.md
- 1298: docs/lexicon/48-rhyming-collocations-sound.md
- 1299: docs/lexicon/49-contemporary-slang-collocations.md
- 1300: docs/lexicon/50-comprehensive-collocation-mastery.md
"""

import os

articles_1_to_9 = [
    {
        "filename": "docs/lexicon/41-adjective-collocations-sangat.md",
        "title": "強調副詞と形容詞の自然な組み合わせ（sangat, amat, sungguh, luar biasa）",
        "category_badge": "構文・副詞連語",
        "lead": "インドネシア語で「とても〜」「非常に〜」と程度を強調する際、sangat, amat, sungguh, luar biasa, bukan main など複数の強調副詞が存在します。文脈（フォーマル・文学的・日常会話）や後ろに続く形容詞によって自然な共起パターンが異なり、適切な組み合わせを使いこなすことで文章の表現力と格調が一気に向上します。",
        "table_headers": ["強調表現", "代表的共起形容詞", "意味・ニュアンス", "使用レジスター"],
        "table_rows": [
            ["sangat", "luas, penting, indah, membantu", "客観的・標準的な「非常に、とても」", "公的文書・日常全般"],
            ["amat", "sangat, mahal, disayangkan, luas", "極めて高い度合い（格式高い・情緒的）", "文学・演説・報道"],
            ["sungguh", "menakjubkan, disayangkan, beruntung", "話し手の主観的実感「真に、心から」", "感想・エッセイ・スピーチ"],
            ["luar biasa", "indah, cerdas, rumit, berani", "常軌を逸した素晴らしさ・並外れた度合い", "会話・口語・賛辞"],
            ["bukan main", "senangnya, takutnya, marahnya", "名詞化形容詞（-nya）を伴い「並大抵ではない」", "感情表現・口語"]
        ],
        "collocations": [
            {
                "phrase": "sangat penting",
                "meaning": "極めて重要である",
                "grammar": "客観的な重要性を述べる最も基本的かつ公的なコロケーション。論文やビジネス文書で頻出。",
                "ex_id": "Keamanan data merupakan hal yang sangat penting dalam era transformasi digital.",
                "ex_kana": "ケアマナン データ メルパカン ハル ヤン サンガット プンティン ダラム エラ トランスフォルマシ デジタル",
                "ex_ja": "データのセキュリティは、デジタルトランスフォーメーションの時代において「**極めて重要**」な事項です。"
            },
            {
                "phrase": "amat sangat",
                "meaning": "この上なく、何よりも深く",
                "grammar": "amat と sangat を重ねた最上級の強調表現。公式な謝罪や深い謝意を表す際に用いられる。",
                "ex_id": "Kami amat sangat berterima kasih atas bantuan yang telah Bapak berikan.",
                "ex_kana": "カミ アマット サンガット ブルテリマ カシ アタス バントゥアン ヤン トゥラ バパッ ブリカン",
                "ex_ja": "皆様から賜りましたご支援に対し、「**この上なく深く**」感謝申し上げます。"
            },
            {
                "phrase": "sungguh menakjubkan",
                "meaning": "真に目を見張るほど素晴らしい",
                "grammar": "話し手の心からの感動や驚嘆を表す。風景や芸術作品、偉業を称える際に多用される。",
                "ex_id": "Pemandangan matahari terbit di puncak Gunung Bromo sungguh menakjubkan.",
                "ex_kana": "ペマンダンガン マタハリ トゥルビット ディ プンチャッ グヌン ブロモ スングー メナジュプカン",
                "ex_ja": "ブロモ山頂から望む日の出の光景は、「**真に息をのむほど素晴らしい**」ものでした。"
            },
            {
                "phrase": "luar biasa indah",
                "meaning": "並外れて美しい",
                "grammar": "通常の形容詞の前に置かれ、並外れたレベルであることを生き生きと描写する。",
                "ex_id": "Taman karang bawah laut di Raja Ampat memiliki panorama yang luar biasa indah.",
                "ex_kana": "タマン カラン バワー ラウト ディ ラジャ アンパット メミリキ パノラマ ヤン ルアル ビアサ インダー",
                "ex_ja": "ラジャ・アンパットの海底サンゴ園は、「**並外れて美しい**」パノラマを有しています。"
            }
        ],
        "dialogue": {
            "speaker_a": "Budi",
            "speaker_b": "Dewi",
            "text_a": "Bagaimana hasil presentasi proyek energi bersih di hadapan dewan direksi kemarin?",
            "text_b": "Luar biasa sukses! Dewan direksi sungguh terkesan dengan analisis efisiensi biaya yang sangat terperinci.",
            "trans_a": "昨日の取締役会の前でのクリーンエネルギー事業のプレゼン結果はどうだった？",
            "trans_b": "「**並外れて大成功**」だったよ！取締役会は「**極めて詳細な**」費用対効果分析に「**心から感銘を受けて**」いたね。"
        },
        "points": [
            "強調副詞の位置: sangat, amat, sungguh は原則として形容詞の前に置かれます（sangat indah）。一方 sekali は必ず形容詞の後ろに置かれます（indah sekali）。両方を同時に使うこと（×sangat indah sekali）は標準語法規範（Tata Bahasa Baku）では過剰重複（pleonasme）とされ、正式な作文では避けるべきです。",
            "amat と sangat の重ね合わせ: `amat sangat` は許容される強調重複として、深い謝意や重大な遺憾を述べる格式高いスピーチで好まれます。",
            "口語での banget: 日常会話では強調副詞に代わって形容詞の後ろに `banget`（ジャカルタ口語由来）を置く形（mahal banget, bagus banget）が圧倒的に自然です。"
        ],
        "quiz": [
            {
                "question": "次の文の空欄に入る最も自然で格式高い客観的強調表現はどれですか？「Informasi ini (...) penting untuk kelangsungan proyek.」",
                "options": ["A. sangat", "B. sekali", "C. banget", "D. amat sekali"],
                "answer": "A. sangat",
                "explanation": "形容詞の前置修飾として客観的・標準的な強調を行うのは「**sangat**」です。sekali や banget は形容詞の後ろに置かれます。"
            },
            {
                "question": "「心から遺憾に思う、極めて残念だ」を格調高く表現する共起コロケーションはどれですか？",
                "options": ["A. sungguh disayangkan", "B. indah sekali", "C. luar biasa murah", "D. sangat selesai"],
                "answer": "A. sungguh disayangkan",
                "explanation": "話し手の心からの残念な気持ちを格調高く述べるには「**sungguh disayangkan**」が最も適しています。"
            },
            {
                "question": "「bukan main」の自然な語法として正しい組み合わせはどれですか？",
                "options": ["A. Bukan main marahnya ia mendengar kabar palsu itu.", "B. Ia bukan main mahal membeli mobil.", "C. Gedung itu bukan main tinggi sekali.", "D. Mereka bukan main makan bersama."],
                "answer": "A. Bukan main marahnya ia mendengar kabar palsu itu.",
                "explanation": "「bukan main」は後ろに形容詞＋nya（marahnya, senangnya, sibuknya）を伴って「その怒りよう（嬉しさ・忙しさ）は並大抵ではなかった」という感嘆・強調構文を作ります。"
            }
        ],
        "column_title": "語法コラム：インドネシア語の多様な感嘆・強調表現",
        "column_text": "インドネシア語には、形容詞そのものを語尾重複させる強調法（panas-panas「熱々のうちに」）や、接頭辞 se- と接尾辞 -nya を組み合わせた最上級構文（secepat-cepatnya「可及的速やかに」）、さらにはスラングの「maha-」「super」「gila-gilaan」など多彩な強調のグラデーションが存在します。公の場でのスピーチでは「amat sangat berterima kasih」、論文では「sangat signifikan」、日常会話では「seru banget」と、TPOに合わせて強調のパレットを使い分けることが上級話者への第一歩です。"
    },
    {
        "filename": "docs/lexicon/42-adjective-collocations-mutlak.md",
        "title": "絶対・確定を表す共起表現（syarat mutlak, menang mutlak, rahasia umum）",
        "category_badge": "確定・限定連語",
        "lead": "「絶対条件」「圧倒的勝利」「公然の秘密」など、日本語でも確定性や絶対性を表す熟語が決まっているように、インドネシア語にも mutlak, umum, nyata, pasti などの形容詞が特定の名詞と強固に結びつくコロケーションが存在します。これらを正確に用いることで、主張の説得力と論理的厳密性が格段に高まります。",
        "table_headers": ["確定連語", "構成要素", "直訳と実務訳", "代表的使用場面"],
        "table_rows": [
            ["syarat mutlak", "syarat (条件) + mutlak (絶対の)", "絶対条件・必須要件", "法務・人事・入試"],
            ["menang mutlak", "menang (勝つ) + mutlak (絶対の)", "圧勝する・完全勝利", "選挙・裁判・競技"],
            ["rahasia umum", "rahasia (秘密) + umum (一般的な)", "公然の秘密（皆が知っていること）", "政治報道・世論・雑談"],
            ["bukti nyata", "bukti (証拠) + nyata (明白な)", "明白な証拠・動かぬ証拠", "司法・科学・事実確認"],
            ["keputusan final", "keputusan (決定) + final (最終の)", "最終決定・不可逆の判決", "法廷・組織運営"]
        ],
        "collocations": [
            {
                "phrase": "syarat mutlak",
                "meaning": "絶対条件、必須要件",
                "grammar": "妥協の余地がない必須資格や要件を定義する際に用いられる。",
                "ex_id": "Integritas moral merupakan syarat mutlak bagi calon pemimpin institusi penegak hukum.",
                "ex_kana": "インテグリタス モラル メルパカン シャラット ムトラッ バギ チャロン プミンピン インスティトゥシ プヌガッ フクム",
                "ex_ja": "道徳的廉潔さは、法執行機関のリーダー候補者にとって「**絶対条件**」です。"
            },
            {
                "phrase": "menang mutlak",
                "meaning": "圧倒的勝利を収める、完全勝利する",
                "grammar": "選挙や法廷闘争、スポーツにおいて相手を完全に圧倒して勝利した状況を修飾する。",
                "ex_id": "Pasangan calon nomor urut satu berhasil menang mutlak dalam pemilihan kepala daerah.",
                "ex_kana": "パサンガン チャロン ノモール ウルット サトゥ ブルハシル ムナン ムトラッ ダラム プミリハン クパラ ダエラ",
                "ex_ja": "候補者ペア第1番は、地方首長選挙において「**圧倒的勝利**」を収めました。"
            },
            {
                "phrase": "rahasia umum",
                "meaning": "公然の秘密",
                "grammar": "建前上は隠されているが、実際には社会の誰もが知っている事実を指すイディオム的連語。",
                "ex_id": "Praktik pungutan liar di instansi tersebut sudah lama menjadi rahasia umum.",
                "ex_kana": "プラクティッ プングタン リアル ディ インスタンシ トゥルスブット スダー ラマ ムンジャディ ラハシア ウムム",
                "ex_ja": "その機関における違法な徴収（裏金搾取）の実態は、とっくの昔から「**公然の秘密**」になっています。"
            },
            {
                "phrase": "bukti nyata",
                "meaning": "動かぬ証拠、明白な事実の証拠",
                "grammar": "抽象的な議論ではなく、現実に目に見える成果や痕跡を指して主張を裏付ける際に多用される。",
                "ex_id": "Peningkatan ekspor manufaktur adalah bukti nyata dari keberhasilan program hilirisasi.",
                "ex_kana": "プニンカタン エクスポール マヌファクトゥール アダラ ブクティ ニャタ ダリ クブルハシラン プログラム ヒリリサシ",
                "ex_ja": "製造業の輸出増加は、川下産業化プログラムの成功を示す「**動かぬ証拠**」です。"
            }
        ],
        "dialogue": {
            "speaker_a": "Hendra",
            "speaker_b": "Rina",
            "text_a": "Apakah merger kedua bank raksasa itu benar-benar akan terlaksana bulan depan?",
            "text_b": "Iya, persetujuan OJK adalah syarat mutlak, dan sekarang sudah ada keputusan final dari regulator.",
            "trans_a": "あの巨大銀行2行の合併は本当に出来月実施されるの？",
            "trans_b": "ええ、金融庁（OJK）の承認が「**絶対条件**」だったんだけど、監督当局からすでに「**最終決定**」が出たのよ。"
        },
        "points": [
            "mutlak の意味領域: mutlak はアラビア語由来（muṭlaq）で「制約のない、無条件の、絶対の」を意味します。hak mutlak（絶対的権利・専決事項）、mayoritas mutlak（絶対多数）など、揺るぎない確固たる事象を修飾します。",
            "nyata と jelas の違い: jelas は「明瞭で見えやすい、分かりやすい」という認知の容易さを指しますが、nyata は「架空ではなく現実に存在する、実体としての」明白さを意味します。したがって「実証的な証拠」には bukti nyata が選ばれます。",
            "pasti と final: pasti は「確実な（推測や予定の確実さ）」を指し、final は「これ以上の変更・議論が許されない最終結論」を指します。"
        ],
        "quiz": [
            {
                "question": "「求職者にとって英語の流暢さは必須の絶対条件である」の空欄に入る語はどれですか？「Kemampuan bahasa Inggris adalah (...) mutlak bagi pelamar.」",
                "options": ["A. syarat", "B. bukti", "C. rahasia", "D. keputusan"],
                "answer": "A. syarat",
                "explanation": "「絶対条件」は「**syarat mutlak**」という確立されたコロケーションです。"
            },
            {
                "question": "「誰もが知っている公然の秘密」を意味するインドネシア語の連語はどれですか？",
                "options": ["A. rahasia umum", "B. rahasia mutlak", "C. bukti tertutup", "D. kabar burung"],
                "answer": "A. rahasia umum",
                "explanation": "建前は秘密だが実際には一般に知れ渡っていることを「**rahasia umum**」と言います。"
            },
            {
                "question": "「選挙で圧倒的勝利を収める」という共起表現として正しいものはどれですか？",
                "options": ["A. menang mutlak", "B. juara umum", "C. sukses cepat", "D. unggul rahasia"],
                "answer": "A. menang mutlak",
                "explanation": "圧倒的・絶対的な大差をつけて勝つことは「**menang mutlak**」と表現します。"
            }
        ],
        "column_title": "時事コラム：インドネシア憲法における「Hak Mutlak（絶対権）」の変遷",
        "column_text": "スカルノ〜スハルト時代には大統領の権限は極めて強大で、内閣の任免や非常大権はまさに「hak mutlak（絶対的専権）」と見なされていました。しかし1998年の民主化改革（Reformasi）に伴う4次にわたる憲法改正により、大統領権限には国会（DPR）の承認や司法裁判所（MK）の違憲審査というチェック＆バランスが課され、真の意味での「mutlak（無制限）」な権力は制度上解体されました。言葉のコロケーションの背景には、国の政治史の歩みが色濃く反映されています。"
    },
    {
        "filename": "docs/lexicon/43-frequency-adverbs-collocations.md",
        "title": "頻度副詞の自然な共起位置（selalu hadir, sering kali terjadi, jarang terlihat）",
        "category_badge": "副詞連語",
        "lead": "selalu（いつも）、sering（しばしば）、kadang-kadang / kadang kala（時々）、jarang（めったに〜ない）などの頻度副詞は、動詞や形容詞と結びついて習慣や傾向を生き生きと描写します。インドネシア語特有の「sering kali」「kadang kala」などの語調を整えるイディオム的連語や、副詞の語順感覚を身につけることで、自然なテンポの会話や正確なレポート作成が可能になります。",
        "table_headers": ["頻度副詞連語", "頻度度合い", "共起動詞・表現", "意味"],
        "table_rows": [
            ["selalu siap", "100% (常時)", "membantu, melayani, siaga", "常に準備ができている、常時対応可能"],
            ["sering kali terjadi", "70-80% (高頻度)", "bencana, kesalahan, kesalahpahaman", "しばしば発生する、頻繁に起きる"],
            ["kadang kala", "30-50% (中頻度)", "muncul, lupa, merasa ragu", "時折、時として〜することがある"],
            ["jarang sekali terlihat", "5-10% (低頻度)", "ditemui, dipakai, berbicara", "めったに見られない、極めて稀である"],
            ["tidak pernah absen", "0%の否定 / 100%出席", "mengikuti rapat, menyapa", "決して欠席しない、必ず出席する"]
        ],
        "collocations": [
            {
                "phrase": "sering kali terjadi",
                "meaning": "しばしば発生する、頻繁に起きる",
                "grammar": "sering の後ろに kali（回数）を添えて語調を滑らかにし、客観的な事象の発生頻度を述べる定番表現。",
                "ex_id": "Kemacetan parah sering kali terjadi di jalur utama saat libur panjang akhir pekan.",
                "ex_kana": "クマチェタン パラー スリン カリ トゥルジャディ ディ ジャルール ウタマ サアット リブール パンジャン アキール プカン",
                "ex_ja": "大型連休の週末には、幹線道路で深刻な渋滞が「**頻繁に発生します**」。"
            },
            {
                "phrase": "selalu hadir",
                "meaning": "常に立ち会う、いつもその場にいる",
                "grammar": "忠実さや不可欠な存在感を表す。物理的な出席だけでなく精神的な寄り添いにも使われる。",
                "ex_id": "Pemerintah berjanji untuk selalu hadir di tengah masyarakat yang tertimpa musibah.",
                "ex_kana": "プムリンター ブルジャンジ ウントゥッ スラル ハディール ディ トゥンガ マシャラカット ヤン トゥルティンパ ムシバー",
                "ex_ja": "政府は、被災した市民のただ中に「**常に寄り添い続ける**」ことを約束しました。"
            },
            {
                "phrase": "jarang sekali ditemui",
                "meaning": "めったにお目にかかれない、極めて稀少である",
                "grammar": "jarang に sekali を重ねて稀少性を強調し、受動態 ditemui や terlihat と共起する。",
                "ex_id": "Spesies anggrek langka ini sekarang sudah jarang sekali ditemui di alam liar.",
                "ex_kana": "スペシエス アングレッ ランカ イニ スカラン スダー ジャラン スカリ ディトムイ ディ アラム リアル",
                "ex_ja": "この希少なランの野生種は、現在では自然環境下で「**めったにお目にかかれません**」。"
            },
            {
                "phrase": "kadang kala muncul",
                "meaning": "時折姿を現す、ふと生じる",
                "grammar": "定期的な周期ではなく、不規則に時々思い出したように発生する心理状態や現象を描写する。",
                "ex_id": "Rasa rindu pada kampung halaman kadang kala muncul saat malam sunyi.",
                "ex_kana": "ラサ リンドゥ パダ カンプン ハラマン カダン カラ ムンチュル サアット マラム スニ",
                "ex_ja": "故郷への恋しさは、静まり返った夜に「**時折ふと湧き上がります**」。"
            }
        ],
        "dialogue": {
            "speaker_a": "Aris",
            "speaker_b": "Fajar",
            "text_a": "Mengapa server aplikasi kita tadi malam sempat tidak bisa diakses pengguna?",
            "text_b": "Gangguan koneksi semacam ini memang jarang sekali terjadi, tetapi tim IT selalu siaga memperbaikinya.",
            "trans_a": "昨夜どうしてアプリのサーバーが一時的にアクセス不能になったの？",
            "trans_b": "この手の接続障害は「**めったに起こらない**」ことなんだけど、ITチームが「**常に待機して**」復旧作業にあたったよ。"
        },
        "points": [
            "語順のルール: 頻度副詞は基本的に「主語の後、動詞述語の前（S + Adv + V）」に配置されます（Dia sering datang）。ただし文頭に置いて文全体を修飾することも自然です（Sering kali dia datang）。",
            "sering kali と kadang kala: 単なる sering や kadang よりも、音節の語調が整うため書き言葉やアナウンスで極めて頻繁に愛用されます。",
            "jarang の否定（tidak jarang）: tidak jarang（めったにないわけではない＝「少なからず〜である」「しばしば〜だ」）は、控えめな肯定を表現する高度な文体です。"
        ],
        "quiz": [
            {
                "question": "「雨季には停電が頻繁に発生する」という文の空欄に入る最も自然な連語はどれですか？「Pemadaman listrik (...) saat musim hujan lebat.」",
                "options": ["A. sering kali terjadi", "B. selalu tidak pernah", "C. jarang sekali cepat", "D. kadang amat"],
                "answer": "A. sering kali terjadi",
                "explanation": "事象が頻繁に生じることを客観的に述べる定型コロケーションは「**sering kali terjadi**」です。"
            },
            {
                "question": "「tidak jarang」の意味として最も適切なものはどれですか？",
                "options": ["A. 少なからず〜である（しばしばある）", "B. 完全に一度もない", "C. めったに見つからない", "D. まれにしか食べない"],
                "answer": "A. 少なからず〜である（しばしばある）",
                "explanation": "tidak jarang は二重否定のニュアンスで「めったにないとは言えない＝少なからずある、しばしばある」を意味します。"
            },
            {
                "question": "「常時24時間警戒態勢にある」を表す表現はどれですか？",
                "options": ["A. selalu siaga 24 jam", "B. jarang siaga 24 jam", "C. kadang kala tidur", "D. sering kali libur"],
                "answer": "A. selalu siaga 24 jam",
                "explanation": "常に待機・警戒している状態は「**selalu siaga**」と表現します。"
            }
        ],
        "column_title": "語法コラム：インドネシア語の時間感覚と「Kadang-kadang vs Kadang kala」",
        "column_text": "口語では重複形の「kadang-kadang」が最も親しまれていますが、公的な報道や格調高い文章ではサンスクリット語由来の語根 kala（時、時代）を添えた「kadang kala」が好まれます。同様に「pada suatu ketika（ある時）」「sewaktu-waktu（いつでも、不意に）」など、時を表す語彙には多様な格調のグラデーションがあります。時間を大らかに捉える南国の風土の中で、頻度のニュアンスを繊細に言語化する知恵が息づいています。"
    },
    {
        "filename": "docs/lexicon/44-prepositional-chunks-collocations.md",
        "title": "前置詞句の定型チャンク（sehubungan dengan, berkaitan dengan, dalam rangka）",
        "category_badge": "機能語チャンク連語",
        "lead": "公用文、ビジネスレター、学術論文、公的アナウンスにおいて、前置詞句の定型チャンクは論理展開の骨格をなす極めて重要な表現です。sehubungan dengan（〜に関連して）、dalam rangka（〜の趣旨・枠組みで）、berdasarkan pada（〜に基づいて）などを塊（チャンク）としてマスターすることで、途切れのない滑らかでプロフェッショナルなインドネシア語が書けるようになります。",
        "table_headers": ["定型前置詞句", "直訳と語構成", "実務・機能的日本語訳", "代表的使用文脈"],
        "table_rows": [
            ["sehubungan dengan", "hubung (繋ぐ) + dengan", "〜に関連して、〜につき", "ビジネス書簡・公式通達の冒頭"],
            ["berkaitan dengan", "kait (引っ掛ける) + dengan", "〜に関わり、〜に関する", "法務条項・報告書・議題提示"],
            ["dalam rangka", "dalam (内) + rangka (骨組み)", "〜の一環として、〜を目的として", "行事・記念式典・政策執行"],
            ["berdasarkan pada", "dasar (基礎) + pada", "〜に基づいて、〜を根拠として", "法令引用・データ分析・判決"],
            ["sesuai dengan", "sesuai (適合) + dengan", "〜に従って、〜の通りに", "契約遵守・仕様書・規則照合"]
        ],
        "collocations": [
            {
                "phrase": "sehubungan dengan surat Anda",
                "meaning": "貴書に関連して、貴簡につき",
                "grammar": "ビジネス書簡の冒頭で相手からのレターや問い合わせに言及する際の絶対的定番チャンク。",
                "ex_id": "Sehubungan dengan surat penawaran Anda tertanggal 10 Oktober, kami ingin mengajukan klarifikasi.",
                "ex_kana": "スフブンガン ドゥンガン スラット プナワラン アンダ トゥルタンガル スプル オクトベール カミ インギン ムンガジュカン クラリフィカシ",
                "ex_ja": "10月10日付の貴社お見積書「**に関連いたしまして**」、明確化をお願い申し上げたく存じます。"
            },
            {
                "phrase": "dalam rangka memperingati",
                "meaning": "〜を記念する一環として",
                "grammar": "独立記念日や創立記念行事、キャンペーンの主旨を説明する際の定型表現。",
                "ex_id": "Perusahaan menyelenggarakan donor darah massal dalam rangka memperingati hari ulang tahun ke-50.",
                "ex_kana": "プルサハアン ムニェレンガラカン ドノール ダラー マッサル ダラム ランカ ムムプリンガティ ハリ ウラン タフン ク-リマプルー",
                "ex_ja": "会社は、創立50周年「**を記念する一環として**」大規模な集団献血を実施しました。"
            },
            {
                "phrase": "berdasarkan data statistik",
                "meaning": "統計データに基づいて",
                "grammar": "客観的な根拠を提示する際に用いられる。pada は省略されて berdasarkan data となることも多い。",
                "ex_id": "Berdasarkan data statistik resmi, angka kemiskinan ekstrem terus mengalami penurunan signifikan.",
                "ex_kana": "ブルダサルカン データ スタティスティッ レスミ アンカ クミスキナン エクストレム トゥルス ムンガラミ プヌルナン シグニフィカン",
                "ex_ja": "公的統計データ「**に基づくと**」、極度の貧困率は大幅な減少傾向を維持しています。"
            },
            {
                "phrase": "sesuai dengan ketentuan hukum",
                "meaning": "法的規定に従って、法令に則り",
                "grammar": "規則や契約への適合性を証明する法務文言。",
                "ex_id": "Seluruh prosedur audit internal telah dilaksanakan sesuai dengan ketentuan hukum yang berlaku.",
                "ex_kana": "スルルー プロセドゥール オーディット インテルナル トゥラ ディラクサナカン ススアイ ドゥンガン クトゥントゥアン フクム ヤン ブルラク",
                "ex_ja": "すべての内部監査手続きは、現行の法的規定「**に従って**」執行されました。"
            }
        ],
        "dialogue": {
            "speaker_a": "Sekretaris",
            "speaker_b": "Direktur",
            "text_a": "Bapak Direktur, ada draf surat balasan untuk kementerian perindustrian.",
            "text_b": "Pastikan kalimat pembukanya menggunakan 'sehubungan dengan surat undangan rapat' agar formal dan santun.",
            "trans_a": "社長、工業省宛ての返信書簡のドラフトができました。",
            "trans_b": "礼儀正しく公式な響きにするため、冒頭は『会議への招集状「**に関連して**」』という定型チャンクを確実に使ってくれ。"
        },
        "points": [
            "前置詞の選択ミスに注意: `berdasarkan` の後ろに `dengan` を置くのは誤りで、正しくは `berdasarkan pada` または単に `berdasarkan (名詞)` です。逆に `sehubungan` や `berkaitan` の後ろは必ず `dengan` です。",
            "文頭での副詞句機能: これらのチャンクは文頭に置かれてコンテクストを規定し、カンマ（,）で区切って主節へとつなげるのが標準的な公用文のフォーマットです。",
            "terkait (dengan) の普及: 現代のニュース報道や口頭のビジネスでは、sehubungan dengan の簡略形として `terkait (dengan) ...` が爆発的に多用されています。"
        ],
        "quiz": [
            {
                "question": "「創業記念日を祝う趣旨で（一環として）」を表す最も適切な定型チャンクはどれですか？",
                "options": ["A. dalam rangka merayakan", "B. sehubungan pada perayaan", "C. berdasarkan dengan ulang tahun", "D. sesuai pada rangka"],
                "answer": "A. dalam rangka merayakan",
                "explanation": "行事や趣旨の一環を表す定型前置詞句は「**dalam rangka**」です。"
            },
            {
                "question": "前置詞の組み合わせとして文法的に誤っているものはどれですか？",
                "options": ["A. berdasarkan dengan bukti", "B. sehubungan dengan surat", "C. berkaitan dengan masalah", "D. sesuai dengan aturan"],
                "answer": "A. berdasarkan dengan bukti",
                "explanation": "berdasarkan の後ろに dengan を置くのは誤りです。正しくは「**berdasarkan (pada) bukti**」です。"
            },
            {
                "question": "ビジネスレターの冒頭で「〜の件に関しまして」と前置きする最も標準的な表現はどれですか？",
                "options": ["A. Sehubungan dengan hal tersebut,", "B. Kadang kala hal tersebut,", "C. Sering kali pada surat,", "D. Bukan main hal itu,"],
                "answer": "A. Sehubungan dengan hal tersebut,",
                "explanation": "「その件に関連いたしまして」と書簡を切り出す標準的な公用句は「**Sehubungan dengan hal tersebut**」です。"
            }
        ],
        "column_title": "実務コラム：インドネシア公式文書（Surat Dinas）の黄金フォーマット",
        "column_text": "省庁や大企業が発行する公用文書（Surat Dinas）は、ほぼ例外なく「Sehubungan dengan surat...（〜の書簡に関連して）」「Menindaklanjuti keputusan...（〜の決定を受けて）」という前置詞チャンクから本題に入ります。これらは儀礼的な前置きであると同時に、法的な文書間の参照関係を明確にする機能を持っています。この定型句を反射的に繰り出せるようになることが、インドネシアのビジネス社会でプロフェッショナルとして認知される登竜門です。"
    },
    {
        "filename": "docs/lexicon/45-discourse-markers-connectors.md",
        "title": "談話標識・論理マーカー（oleh karena itu, selain daripada itu, di sisi lain）",
        "category_badge": "論理接続連語",
        "lead": "文と文、段落と段落を論理的につなぐ接続表現（談話標識：Discourse Markers）は、明晰で説得力のあるスピーチや論説文を書くための必須ツールです。oleh karena itu（したがって）、selain itu / selain daripada itu（さらに、それに加えて）、di sisi lain（その一方で）などの共起フレーズを自在に操ることで、読者を迷わせない洗練された論理展開が実現します。",
        "table_headers": ["論理マーカー", "論理関係", "機能・日本語訳", "配置ルール"],
        "table_rows": [
            ["oleh karena itu", "因果関係（順接）", "したがって、それゆえに", "文頭（直後にカンマ）"],
            ["dengan demikian", "帰結・結論", "このようにして、これにより", "文頭・まとめの段落"],
            ["selain itu", "追加・付加", "さらに、それに加えて", "文頭（直後にカンマ）"],
            ["di sisi lain", "対比・視点の転換", "その一方で、他方では", "文頭または主語の直後"],
            ["walaupun demikian", "譲歩・逆接", "それにもかかわらず", "文頭（直後にカンマ）"]
        ],
        "collocations": [
            {
                "phrase": "oleh karena itu",
                "meaning": "したがって、それゆえに",
                "grammar": "前文で述べられた原因・根拠を受け、論理的必然として導かれる結果や行動を述べる最重要接続副詞句。",
                "ex_id": "Biaya produksi meningkat drastis. Oleh karena itu, kita perlu meninjau ulang strategi efisiensi.",
                "ex_kana": "ビヤヤ プロドゥクシ ムニンカット ドラスティス オレー カレナ イトゥ キタ プルル ムニンジャウ ウラン ストラテギ エフィシエンシ",
                "ex_ja": "生産コストが急増しました。「**したがって**」、我々は効率化戦略を再検証する必要があります。"
            },
            {
                "phrase": "di sisi lain",
                "meaning": "その一方で、他方では",
                "grammar": "一つの事象に対する別の側面や、相反する利害関係者を対比的に論じる際に用いられる。",
                "ex_id": "Otomasi pabrik mempercepat produksi. Di sisi lain, hal ini berpotensi memicu pengurangan tenaga kerja.",
                "ex_kana": "オトマシ パブリッ ムムプルチュパット プロドゥクシ ディ シシ ライン ハル イニ ブルポテンシ ミミチュ プングランガン トゥナガ クルジャ",
                "ex_ja": "工場の自動化は生産を加速させます。「**その一方で**」、これは雇用の削減を引き起こすリスクを孕んでいます。"
            },
            {
                "phrase": "selain daripada itu",
                "meaning": "それに加えて、さらにその上",
                "grammar": "selain itu の格調高い形式。演説や論文で新たな論拠を追加提示する際に効果的。",
                "ex_id": "Produk ini hemat energi. Selain daripada itu, materialnya ramah lingkungan dan dapat didaur ulang.",
                "ex_kana": "プロダッ イニ ヘマット エネルギ スライン ダリパダ イトゥ マテリアルニャ ラマー リングンガン ダン ダパット ディダウル ウラン",
                "ex_ja": "本製品は省エネ設計です。「**それに加えて**」、素材は環境に優しくリサイクル可能です。"
            },
            {
                "phrase": "walaupun demikian",
                "meaning": "それにもかかわらず、そうではあるが",
                "grammar": "前述の困難や障害を認めつつも、それを乗り越えて行動を貫く強い意志や逆接的事実を示す。",
                "ex_id": "Kondisi pasar sedang lesu. Walaupun demikian, target pertumbuhan jangka panjang perusahaan tetap optimis.",
                "ex_kana": "コンディシ パサール スダン レス ワラウプン ドゥミキアン ターゲット プルトゥムブハン ジャンカ パンジャン プルサハアン トゥタップ オプティミス",
                "ex_ja": "市場環境は低迷しています。「**それにもかかわらず**」、当社の長期成長目標は依然として強気です。"
            }
        ],
        "dialogue": {
            "speaker_a": "Dian",
            "speaker_b": "Hadi",
            "text_a": "Apakah Anda setuju kita langsung meluncurkan produk ini bulan depan?",
            "text_b": "Fitur aplikasinya sudah siap. Oleh karena itu peluncuran bisa dilakukan, tetapi di sisi lain tim pemasaran harus bergerak lebih agresif.",
            "trans_a": "来月直ちにこの製品を市場投入することに賛成ですか？",
            "trans_b": "アプリの機能はすでに準備完了しています。「**したがって**」ローンチは可能ですが、「**その一方で**」マーケティングチームはより積極的に動く必要があります。"
        },
        "points": [
            "文頭のカンマの厳格な配置: インドネシア語の正書法（EYD）において、文頭に置かれる談話標識（Oleh karena itu, Selain itu, Namun, Di sisi lain, など）の直後には、原則として必ずカンマ（,）を打つことが義務付けられています。",
            "oleh karena itu と karena itu: karena itu も日常的によく使われますが、公式文書や学術論文では前置詞 oleh を伴った `oleh karena itu` が最も格調高い規範表現とみなされます。",
            "di satu sisi ... di sisi lain: 「一面においては〜、他面においては〜」という対比構造を作る場合、英語の on the one hand ... on the other hand に倣って `di satu pihak/sisi ... di pihak/sisi lain` が多用されます。"
        ],
        "quiz": [
            {
                "question": "前述の原因を受けて「したがって、それゆえに」と結論を導く最も格調高い文頭接続表現はどれですか？",
                "options": ["A. Oleh karena itu,", "B. Kadang kala,", "C. Amat sangat,", "D. Dalam rangka,"],
                "answer": "A. Oleh karena itu,",
                "explanation": "原因から必然的結果を導く標準的な論理接続句は「**Oleh karena itu,**」です。"
            },
            {
                "question": "対立する別の側面や利害を提示する「その一方で」に相当する談話標識はどれですか？",
                "options": ["A. Di sisi lain,", "B. Sesuai dengan,", "C. Sehubungan dengan,", "D. Amat mahal,"],
                "answer": "A. Di sisi lain,",
                "explanation": "別の角度・対比的視点を導入するマーカーは「**Di sisi lain,**」です。"
            },
            {
                "question": "インドネシア語の正書法（EYD）における「Oleh karena itu」の記述ルールとして正しいものはどれですか？",
                "options": ["A. 文頭に置いた直後に必ずカンマ（,）を置く", "B. 常に大文字だけで書く", "C. 文末にしか置くことができない", "D. 前置詞句なので動詞の後に置く"],
                "answer": "A. 文頭に置いた直後に必ずカンマ（,）を置く",
                "explanation": "文頭の談話標識・文頭接続副詞句の直後には、正書法上カンマ（,）を置くことが明確に規定されています。"
            }
        ],
        "column_title": "文章術コラム：ロジカルライティングを支える接続表現の威力",
        "column_text": "中級者の作文が「文と文がブツブツ途切れる箇条書き」に見えてしまう最大の原因は、文頭の談話標識の不足にあります。前文の主張を「Dengan demikian,（これにより）」と締めくくったり、「Namun demikian,（そうではあるが）」と深みを加えたりするだけで、文章は一気に知的なプロのレポートへと変貌します。談話標識を適切に散りばめることは、読者に対する親切な「論理の道路標識」を設置することに他なりません。"
    },
    {
        "filename": "docs/lexicon/46-idiomatic-pairs-synonyms.md",
        "title": "類語の重ね合わせによる強調（hancur lebur, cerdik pandai, kaya raya, aman sentosa）",
        "category_badge": "類語重複連語",
        "lead": "インドネシア語には、似た意味を持つ2つの単語を並置して意味を劇的に強めたり、詩的・格調高い響きを生み出したりする「類語ペア（Kata Majemuk Semantis / Pasangan Sinonim）」が豊富に存在します。hancur lebur（木っ端微塵）、kaya raya（大富豪）、cerdik pandai（博学多才）などの表現は、単なる形容詞単独では出せない圧倒的な迫力と文化的色彩を文章にもたらします。",
        "table_headers": ["類語重複連語", "構成単語", "意味", "ニュアンス・使われ方"],
        "table_rows": [
            ["hancur lebur", "hancur (砕ける) + lebur (融解する)", "木っ端微塵、完膚なきまでに崩壊", "敗北・破壊・失恋の徹底的強調"],
            ["kaya raya", "kaya (富裕) + raya (広大・偉大)", "大富豪、巨万の富を持つ", "莫大な財産・繁栄の描写"],
            ["cerdik pandai", "cerdik (機知に富む) + pandai (利発な)", "知識人、有識者、博学才知", "社会のインテリ層・指導層への言及"],
            ["aman sentosa", "aman (安全な) + sentosa (安寧な)", "天下泰平、平穏無事、安寧", "国家の平和・祈願・格調高い祝辞"],
            ["sunyi senyap", "sunyi (静かな) + senyap (音のない)", "静寂そのもの、シーンと静まり返った", "夜の静けさ・廃墟・不気味な沈黙"]
        ],
        "collocations": [
            {
                "phrase": "hancur lebur",
                "meaning": "木っ端微塵になる、徹底的に粉砕される",
                "grammar": "物理的な粉砕だけでなく、希望や夢、軍隊の完全な壊滅を劇的に描写する。",
                "ex_id": "Harapan tim tamu untuk melaju ke babak final hancur lebur setelah kebobolan lima gol.",
                "ex_kana": "ハラパン ティム タム ウントゥッ ムラジュ ク ババッ フィナル ハンチュール ルブール ストゥラー クボボラン リマ ゴル",
                "ex_ja": "アウェーチームの決勝進出の希望は、5失点を喫したことで「**木っ端微塵に砕け散りました**」。"
            },
            {
                "phrase": "kaya raya",
                "meaning": "大富豪である、巨万の富を築く",
                "grammar": "単に「お金持ち（kaya）」と言うよりも、桁外れの資産家であることを強調する定番の表現。",
                "ex_id": "Meskipun kini telah menjadi pengusaha yang kaya raya, ia tetap hidup sederhana.",
                "ex_kana": "メスキプン キニ トゥラ ムンジャディ プングサハ ヤン カヤ ラヤ イア トゥタップ ヒドゥップ スデルハナ",
                "ex_ja": "今や「**巨万の富を誇る大富豪**」の実業家になったにもかかわらず、彼は質素な暮らしを続けています。"
            },
            {
                "phrase": "cerdik pandai",
                "meaning": "有識者、博学多才な知識人層",
                "grammar": "名詞として機能し、伝統的な村落や現代社会における「知識人・オピニオンリーダー」を総称する。",
                "ex_id": "Pemerintah mengundang kalangan cerdik pandai dari berbagai universitas untuk merumuskan kebijakan.",
                "ex_kana": "プムリンター ムニンドゥン カランガン チュルディッ パンダイ ダリ ブルバガイ ウニヴェルシタス ウントゥッ メルムスカン クビジャカン",
                "ex_ja": "政府は政策を立案するため、諸大学から「**有識者・知識人層**」を招聘しました。"
            },
            {
                "phrase": "aman sentosa",
                "meaning": "平穏無事、安寧秩序が保たれた",
                "grammar": "国家や社会が外敵や内乱、災害の脅威から免れて平和に繁栄している理想的状態を寿ぐ表現。",
                "ex_id": "Semoga bangsa Indonesia senantiasa hidup dalam suasana rukun, aman, dan sentosa.",
                "ex_kana": "スモガ バンサ インドネシア スナンティアサ ヒドゥップ ダラム スアサナ ルクン アマン ダン セントサ",
                "ex_ja": "インドネシア国民が常に和合し、「**平穏無事で安寧な**」環境の中で生きていけますように。"
            }
        ],
        "dialogue": {
            "speaker_a": "Wawan",
            "speaker_b": "Tuti",
            "text_a": "Desa tempat kakekmu tinggal rasanya damai sekali ya?",
            "text_b": "Benar. Malam hari di sana sunyi senyap tanpa suara bising kendaraan, masyarakatnya hidup aman sentosa.",
            "trans_a": "君のおじいさんが住んでいる村は、本当に平和な感じがするね？",
            "trans_b": "そうなの。夜は車の騒音も一切なくて「**静寂そのもの**」だし、人々は「**平穏無事に安寧な**」暮らしを送っているわ。"
        },
        "points": [
            "意味の相乗効果: 単語をただ並べるのではなく、同系統の語彙を重ね合わせることで「これ以上ない完全な度合い」を達成します（kasih sayang「愛情」、lemah lembut「物腰柔らかで優しい」）。",
            "文化・文学的響き: 類語ペアはインドネシアの伝統的文学（Pantun や Hikayat）や大統領の演説で好まれ、聴衆の情緒に強く訴えかける美的なリズムを持ちます。",
            "語順の固定性: これらのペアは語順が決まっており、`lebur hancur` や `raya kaya` と逆転させて使うことはできません。"
        ],
        "quiz": [
            {
                "question": "「桁外れの大富豪」を意味する類語重ね合わせ表現はどれですか？",
                "options": ["A. kaya raya", "B. kaya mahal", "C. uang banyak", "D. kaya sentosa"],
                "answer": "A. kaya raya",
                "explanation": "大富豪・巨万の富を表す確立されたペアは「**kaya raya**」です。"
            },
            {
                "question": "「完全な静寂、静まり返った様子」を表す類語表現はどれですか？",
                "options": ["A. sunyi senyap", "B. hancur lebur", "C. cerdik pandai", "D. aman sentosa"],
                "answer": "A. sunyi senyap",
                "explanation": "物音ひとつしない完全な静けさは「**sunyi senyap**」と表現します。"
            },
            {
                "question": "「cerdik pandai」が指す人物層として最も適切なものはどれですか？",
                "options": ["A. 知識人、有識者", "B. 運動選手", "C. 警察官", "D. 旅人"],
                "answer": "A. 知識人、有識者",
                "explanation": "機知（cerdik）と聡明さ（pandai）を兼ね備えた「**有識者・インテリ層**」を指します。"
            }
        ],
        "column_title": "文学コラム：マレー・インドネシア語の美意識が生んだ「対語法」",
        "column_text": "マレー語・インドネシア語には、古来より口承文学（パントゥン）のリズムを整えるために、2つの同義語や関連語を対にして語る詩的伝統があります。この言語習慣が現代の標準インドネシア語にも色濃く受け継がれており、「hancur lebur」「kering kerontang（カラカラに乾ききった）」「gelap gulita（漆黒の闇）」などの表現となって日常の報道や会話を彩っています。単語をペアで覚えることは、言語の根底にあるリズム感を体得することなのです。"
    },
    {
        "filename": "docs/lexicon/47-antonymic-pairs-balance.md",
        "title": "対義語の対比による表現（suka duka, jual beli, pasang surut, maju mundur）",
        "category_badge": "対義対比連語",
        "lead": "互いに反対の意味を持つ単語を組み合わせ、物事の全体像や変化のダイナミズムを包括的に表現する「対義語ペア（Kata Majemuk Antonim）」は、インドネシア語の極めて特徴的な表現法です。suka duka（喜びと悲しみ＝人生の機微）、jual beli（売買＝取引）、pasang surut（潮の満ち引き＝盛衰）、maju mundur（進退・躊躇）などを学ぶことで、物事を多角的に捉える表現力が身につきます。",
        "table_headers": ["対義語ペア", "構成単語", "意味・比喩的用法", "使用文脈"],
        "table_rows": [
            ["suka duka", "suka (喜び) + duka (悲しみ)", "苦楽、喜びと悲しみ、人生の機微", "人間関係・回想録・スピーチ"],
            ["jual beli", "jual (売る) + beli (買う)", "売買、取引、商売全般", "商業・法務・商取引"],
            ["pasang surut", "pasang (満潮) + surut (引き潮)", "浮き沈み、盛衰、曲折", "歴史・人間関係・景気動向"],
            ["maju mundur", "maju (前進) + mundur (後退)", "進退、行きつ戻りつ、ためらい", "意思決定・心理描写・軍事"],
            ["bolak-balik", "balik (裏返す/戻る) の反復", "行ったり来たり、堂々巡り、頻繁に", "移動・議論・日常行動"]
        ],
        "collocations": [
            {
                "phrase": "suka duka perjuangan",
                "meaning": "闘い（歩み）の苦楽、喜びと悲しみ",
                "grammar": "共に困難を乗り越えてきた仲間との歴史や、事業立ち上げの苦労を情緒豊かに回想する。",
                "ex_id": "Mereka telah melewati berbagai suka duka bersama selama membangun bisnis rintisan ini.",
                "ex_kana": "ムレカ トゥラ ムレワティ ブルバガイ スカ ドゥカ ブルサマ スラマ ムンバングン ビスニス リンティサン イニ",
                "ex_ja": "彼らはこのスタートアップ事業を立ち上げる間、様々な「**苦楽**」を共に乗り越えてきました。"
            },
            {
                "phrase": "pasang surut hubungan",
                "meaning": "関係の浮き沈み、紆余曲折",
                "grammar": "潮の干満のメタファーを人間関係や国家間の外交関係の好不調に適用した表現。",
                "ex_id": "Meskipun mengalami pasang surut, hubungan bilateral kedua negara tetap terjaga dengan harmonis.",
                "ex_kana": "メスキプン ムンガラミ パサン スルット フブンガン ビラテラル クドゥア ネガラ トゥタップ トゥルジャガ ドゥンガン ハルモニス",
                "ex_ja": "「**紆余曲折（浮き沈み）**」を経ながらも、両国間の二国間関係は調和を保ち続けています。"
            },
            {
                "phrase": "akad jual beli",
                "meaning": "売買契約、取引の約定",
                "grammar": "不動産や車などの正式な商取引契約を指す法務・実務コロケーション。",
                "ex_id": "Penandatanganan akta jual beli tanah dilakukan di hadapan Pejabat Pembuat Akta Tanah (PPAT).",
                "ex_kana": "プナンダタンガナン アクタ ジュアル ブリ タナー ディラクカン ディ ハダパン プジャバット プムブアット アクタ タナー",
                "ex_ja": "土地の「**売買証書**」への署名は、土地公証人（PPAT）の面前で執り行われました。"
            },
            {
                "phrase": "maju mundur mengambil keputusan",
                "meaning": "決定を下すのをためらう、二の足を踏む",
                "grammar": "前進するか後退するか迷い、決断できずに逡巡する心理状態を表す。",
                "ex_id": "Jangan maju mundur lagi, peluang investasi emas seperti ini tidak akan datang dua kali.",
                "ex_kana": "ジャンガン マジュ ムンドゥール ラギ プルアン インヴェスタシ エマス スプルティ イニ ティダッ アカン ダタン ドゥア カリ",
                "ex_ja": "もう「**二の足を踏む（ためらう）**」のはやめなさい。このような絶好の投資機会は二度と巡ってきません。"
            }
        ],
        "dialogue": {
            "speaker_a": "Arman",
            "speaker_b": "Lilis",
            "text_a": "Selamat atas ulang tahun pernikahan perak kalian yang ke-25!",
            "text_b": "Terima kasih banyak. Selama seperempat abad ini, kami telah berbagi suka duka dalam mengarungi bahtera rumah tangga.",
            "trans_a": "結婚25周年の銀婚式、本当におめでとう！",
            "trans_b": "どうもありがとう。この四半世紀の間、私たちは家庭という舟を漕ぎながら、様々な「**苦楽**」を共にしてきたわ。"
        },
        "points": [
            "包括的総称概念の創出: 対義語を2つ並べることで、単なる2つの要素の足し算ではなく、「その両極を含む事象の全体」を指す包括的名詞が生まれます（tua muda「老若男女」、besar kecil「大小問わず」）。",
            "比喩への発展: 潮の干満（pasang surut）が「人生やビジネスの浮き沈み」に、前進と後退（maju mundur）が「決断の躊躇」に発展するように、直観的な空間・自然認知が抽象概念の表現へと拡張されています。",
            "語順の不変性: 日本語の「売買」が「買売」にならないのと同様に、インドネシア語でも `jual beli` で固定されており、`beli jual` とは言いません。"
        ],
        "quiz": [
            {
                "question": "「人生の苦楽（喜びと悲しみ）を共にする」を意味する対義語連語はどれですか？",
                "options": ["A. suka duka", "B. jual beli", "C. maju mundur", "D. kaya raya"],
                "answer": "A. suka duka",
                "explanation": "苦楽・喜びと悲しみを表す定型対義語ペアは「**suka duka**」です。"
            },
            {
                "question": "「両国の外交関係の浮き沈み（曲折）」を表す潮のメタファー表現はどれですか？",
                "options": ["A. pasang surut", "B. air laut", "C. bolak-balik", "D. hancur lebur"],
                "answer": "A. pasang surut",
                "explanation": "満潮（pasang）と引き潮（surut）から転じて盛衰・浮き沈みを表すのは「**pasang surut**」です。"
            },
            {
                "question": "「maju mundur」が比喩的に表す心理・行動状態はどれですか？",
                "options": ["A. 決断をためらう、二の足を踏む", "B. 急激に成長する", "C. 全速力で走る", "D. 完全に諦める"],
                "answer": "A. 決断をためらう、二の足を踏む",
                "explanation": "進むか戻るか迷うことから「**決断をためらう、躊躇する**」ことを意味します。"
            }
        ],
        "column_title": "文化コラム：インドネシア語における「老若男女」と二項対立の調和",
        "column_text": "インドネシア語では「老若男女」を表現する際、四字熟語ではなく「tua muda, pria wanita（老いも若きも、男も女も）」と対義語を連続して並べる手法をとります。同様に「siang malam（昼夜を問わず）」「luar dalam（表裏、内外）」など、世界を対立する2つの要素の調和・全体性として捉える思考パターンが、言語の対義語ペアの構造に深く息づいています。"
    },
    {
        "filename": "docs/lexicon/48-rhyming-collocations-sound.md",
        "title": "頭韻・脚韻を踏むリズミカルな連語（seluk beluk, hiruk pikuk, compang camping）",
        "category_badge": "音韻リズミカル連語",
        "lead": "インドネシア語の魅力の真骨頂とも言えるのが、頭韻（Alliteration）や脚韻（Rhyme）を踏んでリズミカルに響く「韻律連語・畳語（Kata Ulang Berubah Bunyi / Reduplikasi Fonologis）」です。seluk beluk（詳細・内情）、hiruk pikuk（喧騒・大騒ぎ）、compang camping（ボロボロの）、ramah tamah（親切・もてなし）など、音の快感とともに鮮烈な情景を想起させる表現をマスターしましょう。",
        "table_headers": ["韻律連語", "音韻パターン", "直観的意味", "使用場面・例文脈"],
        "table_rows": [
            ["seluk beluk", "脚韻 (-uk) + 頭韻 (s/b)", "詳細、裏事情、込み入った事情", "専門知識・調査・業界の内情"],
            ["hiruk pikuk", "脚韻 (-uk) + 変化子音 (h/p)", "喧騒、狂騒、大都会の雑踏", "都市生活・駅・市場の活気描写"],
            ["compang camping", "頭韻 (c-) + 脚韻 (-ang/-ing)", "ボロボロの、つぎはぎだらけの", "衣服の破れ・貧困・荒廃の描写"],
            ["porak poranda", "頭韻 (p-r-) + 脚韻 (-nda)", "壊滅した、滅茶苦茶になった", "災害被災地・戦争・敗戦の惨状"],
            ["ramah tamah", "頭韻 (r/t) + 脚韻 (-ah)", "親しみやすい、温かいもてなし", "懇親会・接客・国民性"]
        ],
        "collocations": [
            {
                "phrase": "seluk beluk dunia usaha",
                "meaning": "ビジネス界の詳細な内情、裏事情",
                "grammar": "表面的には見えない複雑に入り組んだ構造やノウハウを熟知している文脈で用いられる。",
                "ex_id": "Sebagai konsultan senior, ia sangat memahami seluk beluk hukum perpajakan di Indonesia.",
                "ex_kana": "スバガイ コンスルタン セニオール イア サンガット ムマハミ スルッ ブルッ フクム プルパジャカン ディ インドネシア",
                "ex_ja": "シニアコンサルタントとして、彼はインドネシアの税法の「**詳細な裏事情・機微**」を極めて深く理解しています。"
            },
            {
                "phrase": "hiruk pikuk perkotaan",
                "meaning": "都会の喧騒、大都市の喧騒と活気",
                "grammar": "人々が行き交い車がクラクションを鳴らす大都会の喧騒を情緒豊かに描く。",
                "ex_id": "Banyak warga Jakarta memilih berlibur ke desa untuk melepas penat dari hiruk pikuk ibu kota.",
                "ex_kana": "バニャッ ワルガ ジャカルタ ミリ ブルリブール ク デサ ウントゥッ ムレパス プナット ダリ ヒルッ ピクッ イブ コタ",
                "ex_ja": "多くのジャカルタ市民は、首都の「**喧騒**」から疲労を癒すために地方の村へ休暇に出かけることを選びます。"
            },
            {
                "phrase": "porak poranda akibat gempa",
                "meaning": "地震によって滅茶苦茶に壊滅した",
                "grammar": "秩序ある建物や街並みが一瞬にして粉々に破壊された痛ましい光景を描写する。",
                "ex_id": "Ratusan rumah warga porak poranda setelah diterjang angin puting beliung tadi sore.",
                "ex_kana": "ラトゥサン ルマー ワルガ ポラッ ポランダ ストゥラー ディトゥルジャン アンギン プティン ブリウン タディ ソレ",
                "ex_ja": "夕方の竜巻の直撃を受け、何百棟もの民家が「**滅茶苦茶に壊滅しました**」。"
            },
            {
                "phrase": "acara ramah tamah",
                "meaning": "懇親会、歓談の集い",
                "grammar": "公式な会議や式典の後に設けられる、飲食を伴うカジュアルな親睦セッションを指す名詞句。",
                "ex_id": "Setelah seminar kenegaraan selesai, para delegasi menghadiri acara ramah tamah di aula utama.",
                "ex_kana": "ストゥラー セミナール クネガラアン スレサイ パラ デレガシ ムンハディリ アチャラ ラマー タマー ディ アウラ ウタマ",
                "ex_ja": "国家セミナーの終了後、代表使節団は大ホールでの「**懇親会**」に出席しました。"
            }
        ],
        "dialogue": {
            "speaker_a": "Bayu",
            "speaker_b": "Nita",
            "text_a": "Kenapa kamu lebih suka bekerja di kota kecil daripada di Jakarta?",
            "text_b": "Aku tidak tahan dengan hiruk pikuk dan kemacetannya. Di sini warganya ramah tamah dan suasananya tenang.",
            "trans_a": "どうしてジャカルタじゃなくて地方の小さな街で働くのが好きなの？",
            "trans_b": "ジャカルタの「**喧騒**」と渋滞に耐えられなくてね。ここなら住民は「**温かく親切**」だし、空気も落ち着いているよ。"
        },
        "points": [
            "母音交替（Ablaut）と子音交替: インドネシア語の畳語には、母音を変えるもの（bolak-balik, kelap-kelip「チカチカ点滅する」）や子音を変えるもの（sayur-mayur「各種野菜」、lauk-pauk「各種おかず」）があり、語彙全体を総称・強調する機能があります。",
            "公用文での定着: ramah tamah や seluk beluk、porak poranda などは決してくだけた俗語ではなく、大統領スピーチや裁判文書、大手紙の社説でも日常的に使われる正統な標準語彙です。",
            "発音のリズム感: 語末の閉音節（-uk, -ah, -da 等）を歯切れよく発音することで、生き生きとしたネイティブらしい語感が生まれます。"
        ],
        "quiz": [
            {
                "question": "「ある分野の複雑に入り組んだ内情や裏事情」を意味する韻律連語はどれですか？",
                "options": ["A. seluk beluk", "B. hiruk pikuk", "C. ramah tamah", "D. suka duka"],
                "answer": "A. seluk beluk",
                "explanation": "事情の詳細や裏事情・からくりを表す表現は「**seluk beluk**」です。"
            },
            {
                "question": "「都会の喧騒」を意味する自然なコロケーションはどれですか？",
                "options": ["A. hiruk pikuk perkotaan", "B. seluk beluk jalan", "C. compang camping kota", "D. porak poranda mobil"],
                "answer": "A. hiruk pikuk perkotaan",
                "explanation": "大都市のざわめきや喧騒を描写する定型連語は「**hiruk pikuk perkotaan**」です。"
            },
            {
                "question": "公式会議の後に催される「懇親会・親睦レセプション」を指す表現はどれですか？",
                "options": ["A. acara ramah tamah", "B. acara hancur lebur", "C. acara porak poranda", "D. acara pasang surut"],
                "answer": "A. acara ramah tamah",
                "explanation": "歓談や親睦を深める集いは「**acara ramah tamah**」と呼ばれます。"
            }
        ],
        "column_title": "音韻コラム：オノマトペから文学へ昇華したインドネシア語の響き",
        "column_text": "オーストロネシア語族に属するインドネシア語は、古来より母音の響きや音の反復に対して非常に繊細な美意識を持っています。「hiruk pikuk」の響きには人々の雑踏のざわめきが、「porak poranda」には物が砕け散る破壊の衝撃が音響的に織り込まれています。語根の論理的な派生体系とともに、こうした豊かな擬音的・韻律的語彙群がインドネシア語を世界で最も表現力豊かな言語の一つに押し上げているのです。"
    },
    {
        "filename": "docs/lexicon/49-contemporary-slang-collocations.md",
        "title": "現代スラングの頻出コロケーション（gagal fokus, curi perhatian, cari gara-gara）",
        "category_badge": "現代流行・口語連語",
        "lead": "SNS（TikTok, Instagram, X）や若者の雑談、メディアのエンタメ記事で毎日飛び交う現代口語・スラングコロケーション。gagal fokus（略して kepo / salfok: 本筋から脱線して別のものに気を取られる）、curi perhatian（注目を奪う・バズる）、cari gara-gara（余計な波風を立てる・ケンカを売る）、panjat sosial（略して pansos: 売名行為・知名度狙い）など、生きた現代文化を象徴する必須コロケーションを徹底解剖します。",
        "table_headers": ["流行コロケーション", "短縮・スラング形", "直訳と実用訳", "典型的な使用場面"],
        "table_rows": [
            ["gagal fokus", "salfok", "焦点化に失敗＝他所に目を奪われる", "SNSコメント・写真の背景へのツッコミ"],
            ["curi perhatian", "curi pandang / viral", "視線を盗む＝人々の注目を一気に集める", "ファッション・新商品・バズ動画"],
            ["cari gara-gara", "cari ribut", "原因を探す＝わざと揉め事を起こす", "口論・無謀な行動への警告・批判"],
            ["panjat sosial", "pansos", "社会的地位を登る＝有名人を利用した売名", "ネット炎上・インフルエンサー批判"],
            ["banting tulang", "kerja lembur / kerja rodi", "骨を叩きつける＝身を粉にして猛烈に働く", "日常の苦労・家族を養う美談"]
        ],
        "collocations": [
            {
                "phrase": "bikin netizen salfok (gagal fokus)",
                "meaning": "ネットユーザーの視線を他所に奪わせる、脇役に注目させる",
                "grammar": "bikin（〜させる）と組み合わされ、メインの被写体ではなく背景の珍妙なものにネット民が沸き立つ現象を指すネット用語。",
                "ex_id": "Foto wisuda artis itu bikin netizen salfok karena ada kucing tidur di belakangnya.",
                "ex_kana": "フォト ウィスダ アルティス イトゥ ビキン ネティズン サルフォッ カレナ アダ クチン ティドゥール ディ ブラカンニャ",
                "ex_ja": "そのタレントの卒業写真は、背後に猫が寝ていたせいで「**ネット民の視線を完全に奪いました（脇役に注目させました）**」。"
            },
            {
                "phrase": "berhasil mencuri perhatian",
                "meaning": "見事に人々の注目・関心を独占する",
                "grammar": "展示会やフェスティバル、SNS上で圧倒的な存在感を放って話題をさらう際に好まれる表現。",
                "ex_id": "Kostum tradisional kontingen Indonesia berhasil mencuri perhatian penonton dalam festival budaya dunia.",
                "ex_kana": "コストゥム トラディシオナル コンティンゲン インドネシア ブルハシル ムンチュリ プルハティアン プノントン ダラム フェスティバル ブダヤ ドゥニア",
                "ex_ja": "インドネシア選手団の伝統衣装は、世界文化フェスティバルで「**見事に観客の注目を独占しました**」。"
            },
            {
                "phrase": "sengaja cari gara-gara",
                "meaning": "わざと喧嘩を吹っかける、故意にトラブルを起こす",
                "grammar": "gara-gara（元凶、災いの種）を自ら探しに行く＝「余計な問題を起こす」という批判的慣用表現。",
                "ex_id": "Jangan komentari unggahan provokatif itu, dia cuma sengaja cari gara-gara untuk menaikkan pengikut.",
                "ex_kana": "ジャンガン コメンタリ ウングラハン プロヴォカティフ イトゥ ディア チュマ スンガジャ チャリ ガラ-ガラ ウントゥッ ムナイッカン プンイクトゥ",
                "ex_ja": "あの挑発的な投稿にコメントしちゃダメだよ。彼はフォロワーを増やすために「**わざと波風を立てている（炎上を狙っている）**」だけだから。"
            },
            {
                "phrase": "dituduh pansos (panjat sosial)",
                "meaning": "売名行為（知名度目当て）だと非難される",
                "grammar": "panjat（木などに登る）と sosial（社会的）を掛け合わせた造語で、インフルエンサー社会を風刺する現代語。",
                "ex_id": "Selebgram baru itu dituduh pansos setelah sering membuat konten kontroversial bersama artis ternama.",
                "ex_kana": "セレブグラム バル イトゥ ディトゥドゥー パンソス ストゥラー スリン ムンブアット コンテン コントロヴェルシアル ブルサマ アルティス トゥルナマ",
                "ex_ja": "その新人インスタグラマーは、有名タレントと度々物議を醸すコンテンツを作ったことで「**売名行為（pansos）**」だと非難されました。"
            }
        ],
        "dialogue": {
            "speaker_a": "Citra",
            "speaker_b": "Rangga",
            "text_a": "Kamu sudah lihat video wawancara menteri yang viral tadi pagi?",
            "text_b": "Sudah! Tapi netizen malah salfok sama ekspresi ajudan di belakang menteri yang menahan tawa.",
            "trans_a": "今朝バズった大臣のインタビュー動画、もう見た？",
            "trans_b": "見た見た！でもネット民は大臣の話そっちのけで、後ろで笑いをこらえている副官の表情に「**完全に目を奪われて（salfokして）**」たよね。"
        },
        "points": [
            "頭文字合成語（Akronim）の爆発的人気: salfok（salah fokus / gagal fokus）、pansos（panjat sosial）、mager（malas gerak: 動きたくない・億劫だ）など、コロケーションを2音節に縮約する造語法はジャカルタ若者言葉の最大の特徴です。",
            "メディアのネット記事（Clickbait）での多用: 大手ニュースサイト（Detik, Kompas, Tribun）の芸能・トレンド面でも、「Mencuri Perhatian」「Bikin Salfok」といった口語コロケーションが見出しに日常的に踊ります。",
            "TPOの使い分け: 友人同士の会話やチャットでは抜群の親近感を生みますが、正式なビジネス会議や学術論文では口語短縮形（salfok, pansos）は使用せず、標準語表現（teralihkan fokusnya, mencari popularitas）に言い換えるのがマナーです。"
        ],
        "quiz": [
            {
                "question": "SNS上で「メインの話題ではなく、別の些細な点に気を取られてしまう（焦点がズレる）」ことを表す口語スラングはどれですか？",
                "options": ["A. salfok (gagal fokus)", "B. pansos (panjat sosial)", "C. mager (malas gerak)", "D. baper (bawa perasaan)"],
                "answer": "A. salfok (gagal fokus)",
                "explanation": "salah fokus / gagal fokus の略で、脇役に目を奪われることを「**salfok**」と言います。"
            },
            {
                "question": "「有名人にすり寄って自らの知名度を上げようとする売名行為」を指す造語コロケーションはどれですか？",
                "options": ["A. panjat sosial (pansos)", "B. curi perhatian", "C. cari gara-gara", "D. banting tulang"],
                "answer": "A. panjat sosial (pansos)",
                "explanation": "社会的階段を強引によじ登るイメージから「**panjat sosial (pansos)**」と呼ばれます。"
            },
            {
                "question": "「わざとトラブルや揉め事を引き起こす」ことを意味する日常コロケーションはどれですか？",
                "options": ["A. cari gara-gara", "B. curi perhatian", "C. gagal fokus", "D. bolak-balik"],
                "answer": "A. cari gara-gara",
                "explanation": "余計な波風やトラブルの種を自ら蒔きに行くことを「**cari gara-gara**」と表現します。"
            }
        ],
        "column_title": "社会コラム：インドネシアのSNS熱とネットスラングの超速進化",
        "column_text": "世界有数のSNS大国であるインドネシアでは、Twitter（X）やTikTokで数時間の間に新たなスラング・コロケーションが生まれ、翌日には全国民の共通語になるほどの圧倒的な伝播スピードを持っています。その根底には、お互いをからかい合い（bercanda）、ユーモアを共有して絆を深めるインドネシア社会独特の「Nongkrong（仲間とのだべり）」文化があります。生きたスラングコロケーションを理解することは、現代インドネシア人のリアルタイムの感情と同期することなのです。"
    }
]

def generate_standard_article(data):
    md = f"""# {data['title']}

<div class="article-meta">
  <span class="category-badge">{data['category_badge']}</span>
  <span class="read-time">読了目安: 12分</span>
  <span class="level-badge">中上級〜上級</span>
</div>

## はじめに

{data['lead']}

---

## 1. 最重要コロケーション総覧

| {data['table_headers'][0]} | {data['table_headers'][1]} | {data['table_headers'][2]} | {data['table_headers'][3]} |
| :--- | :--- | :--- | :--- |
"""
    for row in data['table_rows']:
        md += f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} |\n"

    md += """
---

## 2. 詳細解説と実践例文カード

ネイティブスピーカーが実際のコミュニケーションや公的文書で頻繁に用いる重要フレーズを、構造解説と共にご紹介します。

"""
    for i, item in enumerate(data['collocations'], 1):
        md += f"""### ({i}) {item['phrase']}

> **意味**: {item['meaning']}  
> **解説**: {item['grammar']}

<div class="id-example">
  <div class="id-text">"{item['ex_id']}"</div>
  <div class="kana-text">{item['ex_kana']}</div>
  <div class="ja-text">{item['ex_ja']}</div>
</div>

"""

    d = data['dialogue']
    md += f"""---

## 3. 実践会話ダイアログ（会話での自然な使われ方）

実際の会話の中でこれらのコロケーションがどのように生き生きと機能するか、以下のダイアログで確認しましょう。

<div class="dialogue-box">
  <div class="dialogue-line speaker-a">
    <div class="speaker-name">{d['speaker_a']}:</div>
    <div class="speech-text">"{d['text_a']}"</div>
    <div class="speech-trans">{d['trans_a']}</div>
  </div>
  <div class="dialogue-line speaker-b">
    <div class="speaker-name">{d['speaker_b']}:</div>
    <div class="speech-text">"{d['text_b']}"</div>
    <div class="speech-trans">{d['trans_b']}</div>
  </div>
</div>

---

## 4. 構文・文法・レジスター上の注意点

"""
    for pt in data['points']:
        md += f"- **ポイント**: {pt}\n"

    md += """
---

## 5. 定着確認クイズ（全3問）

理解度を測るための3択クイズです。最も自然な組み合わせを選んでください。

"""
    for q_idx, q in enumerate(data['quiz'], 1):
        md += f"""### 第{q_idx}問: {q['question']}

"""
        for opt in q['options']:
            md += f"- {opt}\n"
        md += f"""
??? note "解説・正解を確認する"
    **正解**: 「**{q['answer']}**」
    
    **解説**: {q['explanation']}

"""

    md += f"""---

## 6. {data['column_title']}

{data['column_text']}

---

## 7. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return md

# Special 1300 article: Comprehensive Collocation Mastery Test (50 Questions)
def generate_article_1300():
    md = """# 総合コロケーション検定：ネイティブらしい共起連語マスター50問テスト

<div class="article-meta">
  <span class="category-badge">総合検定・総集編</span>
  <span class="read-time">所要時間: 45〜60分</span>
  <span class="level-badge">B2〜C2（中上級〜最上級）</span>
</div>

## はじめに：セクション31総集編へようこそ！

本記事は、「**最頻出コア語根＆コロケーション辞典（第1251記事〜第1300記事）**」の学習成果を総合的に測定・定着させるための**50問完全マスター検定テスト**です。

単語を単体で暗記する学習から脱却し、**「ネイティブがどの単語とどの単語を組み合わせて自然な文を紡ぎ出すか」**という共起ネットワーク（Collocation Network）の習熟度を、以下の5大分野（各10問）から徹底的に試します。

1. **第1部：動詞コア語根コロケーション（問1〜問10）** - ambil, buang, jatuh, naik, tahan, jalan 等
2. **第2部：身体名詞メタファー連語（問11〜問20）** - hati, kepala, mata, tangan, kaki, mulut 等
3. **第3部：ビジネス・経済・法務専門連語（問21〜問30）** - 契約、財務、人事、マクロ経済、法廷 等
4. **第4部：社会時事・先端IT・環境連語（問31〜問40）** - 選挙、外交、サイバー、AI、伝統儀礼 等
5. **第5部：構文・機能語・イディオム・現代スラング（問41〜問50）** - 談話標識、類語対比、韻律、salfok 等

---

## 🎯 模擬テストの受け方
- 制限時間は約50分（1問あたり1分）。
- ノートやメモ用紙を用意し、ご自身の解答（A/B/C/D）を記録してください。
- 全問解答後、各問題のアコーディオンを開いて正解と詳細解説を確認し、巻末の採点基準表で現在の実力を診断しましょう。

---

## 第1部：動詞コア語根コロケーション（問1〜問10）

### 問1. 「彼は他人のビジネスの成功を自分の手柄にした」の空欄に入る語根 ambil の連語は？
「Ia berusaha (...) atas keberhasilan proyek tim tersebut.」
- A. ambil bagian
- B. ambil alih
- C. ambil pusing
- D. ambil muka

??? note "正解と解説"
    **正解**: 「**B. ambil alih**」
    
    **解説**: 「手柄や支配権、主導権を奪い取る、買収・接収する」は「**ambil alih**」です（ambil bagian は「参加する」、ambil pusing は「気にかける」）。

### 問2. 「無駄な時間を浪費してはならない」の自然な連語は？
「Jangan (...) untuk hal-hal sepele yang tidak produktif.」
- A. buang muka
- B. buang waktu
- C. buang air
- D. buang langkah

??? note "正解と解説"
    **正解**: 「**B. buang waktu**」
    
    **解説**: 時間を無駄遣いする・浪費することは「**buang waktu**」と言います。

### 問3. 「請求書の支払期日が来週月曜日に到来する」の「期日が来る」は？
「Tagihan listrik ini akan (...) pada hari Senin depan.」
- A. jatuh tempo
- B. jatuh cinta
- C. jatuh sakit
- D. jatuh miskin

??? note "正解と解説"
    **正解**: 「**A. jatuh tempo**」
    
    **解説**: 支払期日や満期が到来することは「**jatuh tempo**」です。

### 問4. 「その新進気鋭の若手俳優は今まさに人気急上昇中だ」の表現は？
「Aktor muda berbakat itu sedang (...) di dunia perfilman.」
- A. naik darah
- B. naik daun
- C. naik pangkat
- D. naik banding

??? note "正解と解説"
    **正解**: 「**B. naik daun**」
    
    **解説**: 人気や運気が急上昇して脚光を浴びている状態を「**naik daun**」と表現します。

### 問5. 「危機的状況を見かねて、政府がついに直接介入・自ら行動に乗り出した」は？
「Pemerintah akhirnya (...) untuk menstabilkan harga beras.」
- A. turun harga
- B. turun ranjang
- C. turun tangan
- D. turun minum

??? note "正解と解説"
    **正解**: 「**C. turun tangan**」
    
    **解説**: 問題解決のために自ら現場へ乗り出す・介入することは「**turun tangan**」です。

### 問6. 「逆境や厳しい試練にもへこたれない強い忍耐力がある」を表す連語は？
「Mental pengusaha harus (...), tidak boleh mudah menyerah.」
- A. tahan banting
- B. tahan lama
- C. tahan air
- D. tahan lapar

??? note "正解と解説"
    **正解**: 「**A. tahan banting**」
    
    **解説**: 叩かれてもへこたれないタフな精神・耐久力を「**tahan banting**」と言います。

### 問7. 「オリンピック水泳競技で世界新記録が打ち立てられた」の「記録更新」は？
「Perenang muda itu berhasil (...) dunia di nomor 100 meter.」
- A. pecah belah
- B. pecah rekor
- C. pecah tangis
- D. pecah kongsi

??? note "正解と解説"
    **正解**: 「**B. pecah rekor**」
    
    **解説**: 新記録を樹立する・記録を破ることは「**pecah rekor**」です。

### 問8. 「打開策を見つけるため、彼らは懸命に知恵を絞った」の表現は？
「Tim kreatif harus (...) untuk menciptakan konsep iklan baru.」
- A. putar haluan
- B. putar otak
- C. putar lidah
- D. putar balik

??? note "正解と解説"
    **正解**: 「**B. putar otak**」
    
    **解説**: 懸命に考えを巡らせて知恵を絞ることは「**putar otak**」と言います。

### 問9. 「交渉が難航し、双方は歩み寄って妥協案（中間点）を見出した」の連語は？
「Kedua belah pihak akhirnya sepakat mengambil (...) damai.」
- A. jalan buntu
- B. jalan pintas
- C. jalan tengah
- D. jalan keluar

??? note "正解と解説"
    **正解**: 「**C. jalan tengah**」
    
    **解説**: 両者の主張の折衷案・妥協点を見出すことは「**jalan tengah**」です。

### 問10. 「短絡的な近道を選んで不正を行ってはならない」の「近道・安易な手段」は？
「Jangan mengambil (...) yang melanggar hukum demi keuntungan instan.」
- A. jalan keluar
- B. jalan pintas
- C. jalan buntu
- D. jalan raya

??? note "正解と解説"
    **正解**: 「**B. jalan pintas**」
    
    **解説**: 物理的な近道だけでなく、安易な抜け道・短絡策を「**jalan pintas**」と呼びます。

---

## 第2部：身体名詞メタファー連語（問11〜問20）

### 問11. 「成功しても傲慢にならず、常に謙虚でありなさい」の「謙虚な」は？
「Meskipun sudah sukses besar, ia tetap (...).」
- A. besar hati
- B. rendah hati
- C. patah hati
- D. keras hati

??? note "正解と解説"
    **正解**: 「**B. rendah hati**」
    
    **解説**: 謙虚・謙遜は「**rendah hati**」です（besar hati は「誇らしい」、keras hati は「頑固な」）。

### 問12. 「少し褒められただけで天狗になる（うぬぼれる）な」の表現は？
「Jangan jadi orang yang (...) hanya karena mendapat pujian.」
- A. kepala dingin
- B. cuci kepala
- C. keras kepala
- D. besar kepala

??? note "正解と解説"
    **正解**: 「**D. besar kepala**」
    
    **解説**: うぬぼれて傲慢になる・天狗になることは「**besar kepala**」です。

### 問13. 「激しい怒りでカッとなる・逆上する」を表す身体連語は？
「Mendengar fitnah keji itu, ayahnya langsung (...).」
- A. naik darah
- B. darah dingin
- C. darah daging
- D. darah biru

??? note "正解と解説"
    **正解**: 「**A. naik darah**」
    
    **解説**: 血圧が上がって激怒することは「**naik darah**」です。

### 問14. 「事件の真相を口外せず、徹底して口を閉ざす」の連語は？
「Saksi kunci itu memilih (...) demi keselamatan keluarganya.」
- A. mulut manis
- B. banyak mulut
- C. buah mulut
- D. tutup mulut

??? note "正解と解説"
    **正解**: 「**D. tutup mulut**」
    
    **解説**: 秘密を守り沈黙を貫くことは「**tutup mulut**」です。

### 問15. 「批判されても平気で恥と思わない（面の皮が厚い・恥知らず）」は？
「Koruptor itu memang (...) karena masih bisa tersenyum di depan kamera.」
- A. muka masam
- B. cari muka
- C. tebal muka
- D. uang muka

??? note "正解と解説"
    **正解**: 「**C. tebal muka**」
    
    **解説**: 恥知らずで面の皮が厚いことは「**tebal muka**」と言います。

### 問16. 「上司に媚びを売って点数を稼ごうとする」の連語は？
「Karyawan itu suka (...) di hadapan manajer baru.」
- A. cari muka
- B. tebal muka
- C. muka masam
- D. uang muka

??? note "正解と解説"
    **正解**: 「**A. cari muka**」
    
    **解説**: 他人の前で良い顔をして気に入られようとすることは「**cari muka**」です。

### 問17. 「人の忠告を右の耳から左の耳へと聞き流す」の表現は？
「Nasihat gurunya hanya (...) dan keluar telinga kiri.」
- A. tebal telinga
- B. merah telinga
- C. masuk telinga kanan
- D. pasang telinga

??? note "正解と解説"
    **正解**: 「**C. masuk telinga kanan**」
    
    **解説**: 「**masuk telinga kanan, keluar telinga kiri**」で忠告を聞き流す定型表現です。

### 問18. 「社長の最も信頼する右腕・懐刀」を表す身体連語は？
「Ia telah lama menjadi (...) direktur utama dalam mengelola perusahaan.」
- A. tangan kanan
- B. cuci tangan
- C. campur tangan
- D. angkat tangan

??? note "正解と解説"
    **正解**: 「**A. tangan kanan**」
    
    **解説**: 腹心の部下・最も頼りになる補佐役は「**tangan kanan**」です。

### 問19. 「責任を放棄して知らぬ顔を決め込む（責任回避する）」は？
「Pejabat itu berusaha (...) dari skandal korupsi yang terjadi di dinasnya.」
- A. lepas tangan / cuci tangan
- B. angkat tangan
- C. tangan kanan
- D. campur tangan

??? note "正解と解説"
    **正解**: 「**A. lepas tangan / cuci tangan**」
    
    **解説**: 責任から逃れて手を洗う・放棄することは「**cuci tangan**」または「**lepas tangan**」です。

### 問20. 「歩道や路端で営業する露店・屋台商人」を指す歴史的身体連語は？
「Pedagang (...) sering memenuhi trotoar di kawasan pasar malam.」
- A. kaki lima
- B. kaki tangan
- C. angkat kaki
- D. cuci kaki

??? note "正解と解説"
    **正解**: 「**A. kaki lima**」
    
    **解説**: 5フィート歩道令に由来する屋台・露店商人は「**pedagang kaki lima (PKL)**」です。

---

## 第3部：ビジネス・経済・法務専門連語（問21〜問30）

### 問21. 「正式な業務提携契約書を締結・調印する」の動詞連語は？
「Kedua pimpinan korporasi telah resmi (...) kerja sama strategis.」
- A. menandatangani kontrak
- B. membatalkan klausul
- C. memperpanjang masa
- D. mengajukan gugatan

??? note "正解と解説"
    **正解**: 「**A. menandatangani kontrak**」
    
    **解説**: 契約書に署名調印することは「**menandatangani kontrak**」です。

### 問22. 「長時間のタフな商談の末、ついに合意に達した」の連語は？
「Setelah negosiasi alot, para pihak akhirnya berhasil (...).」
- A. menekan biaya
- B. mencapai kesepakatan
- C. mengajukan penawaran
- D. membatalkan klausul

??? note "正解と解説"
    **正解**: 「**B. mencapai kesepakatan**」
    
    **解説**: 合意に到達する・妥結することは「**mencapai kesepakatan**」です。

### 問23. 「健全な企業運営のため、日々の現金の出納状況（キャッシュフロー）を管理する」は？
「Manajer keuangan harus memantau kelancaran (...) setiap hari.」
- A. laporan laba rugi
- B. arus kas
- C. suku bunga
- D. suntikan modal

??? note "正解と解説"
    **正解**: 「**B. arus kas**」
    
    **解説**: キャッシュフロー（現金の流れ）は「**arus kas**」と言います。

### 問24. 「業績不振に伴い、会社は何十人もの従業員の解雇（整理解雇）に踏み切った」の専門略語連語は？
「Manajemen terpaksa melakukan (...) terhadap 50 karyawan pabrik.」
- A. perekrutan karyawan
- B. evaluasi kinerja
- C. pemutusan hubungan kerja (PHK)
- D. jenjang karier

??? note "正解と解説"
    **正解**: 「**C. pemutusan hubungan kerja (PHK)**」
    
    **解説**: 労働契約の解除・解雇は「**pemutusan hubungan kerja (PHK)**」です。

### 問25. 「新製品の投入により、自社の国内市場占有率（マーケットシェア）を拡大する」は？
「Perusahaan menargetkan perluasan (...) hingga mencapai 35 persen.」
- A. pangsa pasar
- B. target konsumen
- C. citra merek
- D. kampanye promosi

??? note "正解と解説"
    **正解**: 「**A. pangsa pasar**」
    
    **解説**: 市場シェア・占有率は「**pangsa pasar**」と言います。

### 問26. 「中央銀行は急激なインフレ率の上昇を抑えるため利上げを実施した」の「インフレ率」は？
「Bank sentral berusaha menekan (...) yang melonjak tinggi.」
- A. pertumbuhan ekonomi
- B. laju inflasi
- C. daya beli
- D. pendapatan per kapita

??? note "正解と解説"
    **正解**: 「**B. laju inflasi**」
    
    **解説**: インフレの進行速度・インフレ率は「**laju inflasi**」です。

### 問27. 「物価高騰が庶民の購買力を著しく低下させている」の「購買力」は？
「Kenaikan harga pangan menurunkan (...) masyarakat lapisan bawah.」
- A. daya beli
- B. nilai tukar
- C. cadangan devisa
- D. utang luar negeri

??? note "正解と解説"
    **正解**: 「**A. daya beli**」
    
    **解説**: 購買力は「**daya beli (masyarakat)**」と言います。

### 問28. 「弁護士を通じて地方裁判所に民事訴訟を提起する」の訴訟提起は？
「Penggugat berencana (...) ke Pengadilan Negeri Jakarta Pusat.」
- A. vonis hakim
- B. saksi kunci
- C. mengajukan gugatan
- D. bukti otentik

??? note "正解と解説"
    **正解**: 「**C. mengajukan gugatan**」
    
    **解説**: 訴訟を起こす・提訴することは「**mengajukan gugatan**」です。

### 問29. 「裁判官による有罪判決が被告人に言い渡された」の判決は？
「Terdakwa tertunduk lesu saat mendengarkan (...) yang dibacakan di persidangan.」
- A. saksi kunci
- B. vonis hakim
- C. bukti otentik
- D. hak pilih

??? note "正解と解説"
    **正解**: 「**B. vonis hakim**」
    
    **解説**: 裁判官が下す判決・宣告は「**vonis hakim**」です。

### 問30. 「法廷で改ざんの余地がない真正な公的証拠書類を提示する」の「真正な証拠」は？
「Jaksa penuntut umum melampirkan (...) berupa akta notaris asli.」
- A. saksi ahli
- B. bukti otentik
- C. gugatan hukum
- D. vonis bebas

??? note "正解と解説"
    **正解**: 「**B. bukti otentik**」
    
    **解説**: 公証人証書等の真正な証拠は「**bukti otentik**」と呼ばれます。

---

## 第4部：社会時事・先端IT・環境連語（問31〜問40）

### 問31. 「インドネシアでは5年ごとに大統領および国会議員を選出する総選挙が実施される」の「総選挙」は？
「Pesta demokrasi rakyat Indonesia diwujudkan melalui (...).」
- A. kampanye akbar
- B. pemilihan umum (Pemilu)
- C. perolehan suara
- D. hak pilih

??? note "正解と解説"
    **正解**: 「**B. pemilihan umum (Pemilu)**」
    
    **解説**: 総選挙は「**pemilihan umum (Pemilu)**」です。

### 問32. 「二国間の友好親善および経済協力を深める」の「二国間関係」は？
「Kunjungan kenegaraan ini bertujuan mempererat (...) kedua negara sahabat.」
- A. nota kesepahaman
- B. hubungan bilateral
- C. hak pilih
- D. duta besar

??? note "正解と解説"
    **正解**: 「**B. hubungan bilateral**」
    
    **解説**: 二国間関係は「**hubungan bilateral**」と言います。

### 問33. 「両国首脳の立ち会いのもと、覚書（MOU）の調印が行われた」の「覚書」は？
「Penandatanganan (...) bidang energi terbarukan disaksikan oleh kedua kepala negara.」
- A. nota kesepahaman (MoU)
- B. hubungan multilateral
- C. pemilihan umum
- D. kampanye akbar

??? note "正解と解説"
    **正解**: 「**A. nota kesepahaman (MoU)**」
    
    **解説**: 覚書（MOU）はインドネシア語で「**nota kesepahaman**」と定訳されています。

### 問34. 「地球温暖化の影響により、極地の氷床融解が加速している」の「地球温暖化」は？
「Dampak (...) semakin nyata dengan terjadinya cuaca ekstrem di berbagai belahan bumi.」
- A. pemanasan global
- B. energi terbarukan
- C. emisi karbon
- D. deforestasi hutan

??? note "正解と解説"
    **正解**: 「**A. pemanasan global**」
    
    **解説**: 地球温暖化は「**pemanasan global**」です。

### 問35. 「化石燃料から太陽光や風力などの再生可能エネルギーへの転換」の「再生可能エネルギー」は？
「Pemerintah mendorong transisi menuju pemanfaatan (...).」
- A. emisi karbon
- B. energi terbarukan
- C. pemanasan global
- D. bahan bakar fosil

??? note "正解と解説"
    **正解**: 「**B. energi terbarukan**」
    
    **解説**: 再生可能エネルギーは「**energi terbarukan**」と言います。

### 問36. 「不正アクセスや情報漏洩を防ぐため、サイバーセキュリティを強化する」は？
「Lembaga keuangan wajib meningkatkan sistem (...) dari serangan peretas.」
- A. kecerdasan buatan
- B. keamanan siber
- C. komputasi awan
- D. basis data

??? note "正解と解説"
    **正解**: 「**B. keamanan siber**」
    
    **解説**: サイバーセキュリティは「**keamanan siber**」です。

### 問37. 「深層学習を用いた人工知能技術が産業のあらゆる分野を変革している」の「人工知能」は？
「Penerapan teknologi (...) membuka peluang efisiensi otomatisasi kerja.」
- A. komputasi awan
- B. kecerdasan buatan (AI)
- C. basis data
- D. keamanan siber

??? note "正解と解説"
    **正解**: 「**B. kecerdasan buatan (AI)**」
    
    **解説**: 人工知能（AI）は「**kecerdasan buatan**」と言います。

### 問38. 「患者は医師の処方箋に従って正しく薬を服用しなければならない」の「医師の処方箋」は？
「Obat keras ini hanya dapat dibeli di apotek dengan menggunakan (...).」
- A. resep dokter
- B. tekanan darah
- C. rawat inap
- D. efek samping

??? note "正解と解説"
    **正解**: 「**A. resep dokter**」
    
    **解説**: 医師の処方箋は「**resep dokter**」です。

### 問39. 「学術論文において仮説の真偽を統計的手法で検証する」の「仮説検定」は？
「Peneliti melakukan (...) untuk membuktikan korelasi antarvariabel.」
- A. kerangka berpikir
- B. uji hipotesis
- C. metodologi penelitian
- D. tinjauan pustaka

??? note "正解と解説"
    **正解**: 「**B. uji hipotesis**」
    
    **解説**: 仮説の検証・仮説検定は「**uji hipotesis**」です。

### 問40. 「先祖代々受け継がれてきた尊い遺産・伝統文化」を表す連語は？
「Batik dan wayang kulit merupakan (...) yang wajib kita lestarikan bersama.」
- A. upacara adat
- B. warisan leluhur
- C. norma masyarakat
- D. nilai luhur

??? note "正解と解説"
    **正解**: 「**B. warisan leluhur**」
    
    **解説**: 先祖から継承された遺産・伝統遺産は「**warisan leluhur**」と表現します。

---

## 第5部：構文・機能語・イディオム・現代スラング（問41〜問50）

### 問41. 「この上なく深く感謝する」を表す最も格調高い強調の組み合わせは？
「Kami (...) berterima kasih atas bantuan dan kerja sama Anda.」
- A. amat sangat
- B. sangat sekali
- C. bukan main
- D. sungguh sekali

??? note "正解と解説"
    **正解**: 「**A. amat sangat**」
    
    **解説**: 重ね合わせ強調として公の場で正統に認められているのは「**amat sangat**」です（sangat sekali は重複過剰とみなされる）。

### 問42. 「採用試験において実務経験は応募者の必須の絶対条件である」の「絶対条件」は？
「Pengalaman kerja minimal tiga tahun adalah (...) bagi posisi ini.」
- A. bukti nyata
- B. rahasia umum
- C. syarat mutlak
- D. keputusan final

??? note "正解と解説"
    **正解**: 「**C. syarat mutlak**」
    
    **解説**: 必須要件・絶対条件は「**syarat mutlak**」です。

### 問43. 「雨季には大雨による洪水被害がしばしば発生する」の客観的頻度連語は？
「Banjir bandang (...) saat puncak musim penghujan di wilayah dataran rendah.」
- A. selalu siap
- B. sering kali terjadi
- C. jarang sekali terlihat
- D. kadang kala tidur

??? note "正解と解説"
    **正解**: 「**B. sering kali terjadi**」
    
    **解説**: 頻繁に発生することは「**sering kali terjadi**」と表現します。

### 問44. 「10月1日付の貴簡に関しまして、ご報告申し上げます」の公式書簡冒頭チャンクは？
「(...) surat Anda tertanggal 1 Oktober, kami ingin menyampaikan laporan perkembangan.」
- A. Berdasarkan dengan
- B. Dalam rangka pada
- C. Sehubungan dengan
- D. Sesuai pada

??? note "正解と解説"
    **正解**: 「**C. Sehubungan dengan**」
    
    **解説**: 書簡や通達の冒頭で「〜に関連して」と切り出す定型句は「**Sehubungan dengan**」です。

### 問45. 「原材料費が高騰した。したがって我々は販売価格を改定せざるを得ない」の文頭論理マーカーは？
「Biaya bahan baku naik tajam. (...), kita terpaksa menyesuaikan harga jual produk.」
- A. Oleh karena itu
- B. Di sisi lain
- C. Selain daripada itu
- D. Walaupun demikian

??? note "正解と解説"
    **正解**: 「**A. Oleh karena itu**」
    
    **解説**: 前述の原因から必然的結果を導く「したがって」は「**Oleh karena itu**」です。

### 問46. 「不屈の努力の末、彼は一代で巨万の富を築く大富豪となった」の類語重複表現は？
「Dari seorang pedagang asongan, kini ia sukses menjadi konglomerat yang (...).」
- A. cerdik pandai
- B. kaya raya
- C. hancur lebur
- D. aman sentosa

??? note "正解と解説"
    **正解**: 「**B. kaya raya**」
    
    **解説**: 莫大な財産を誇る大富豪は「**kaya raya**」と言います。

### 問47. 「夫婦として長い歳月を共に歩み、人生の苦楽を分かち合ってきた」の対義語ペアは？
「Mereka berjanji untuk saling setia dan berbagi (...) dalam mengarungi kehidupan.」
- A. suka duka
- B. jual beli
- C. pasang surut
- D. maju mundur

??? note "正解と解説"
    **正解**: 「**A. suka duka**」
    
    **解説**: 喜びと悲しみ・人生の苦楽を表す確立されたペアは「**suka duka**」です。

### 問48. 「この複雑な業界の裏事情・からくりを熟知している専門家」の韻律連語は？
「Ia mengetahui dengan persis (...) sistem birokrasi pemerintahan daerah.」
- A. hiruk pikuk
- B. seluk beluk
- C. compang camping
- D. porak poranda

??? note "正解と解説"
    **正解**: 「**B. seluk beluk**」
    
    **解説**: 入り組んだ詳細や裏事情は「**seluk beluk**」と表現します。

### 問49. 「メインの被写体ではなく背景の猫にネット民が目を奪われる」の現代ネット口語は？
「Video tersebut viral dan bikin netizen (...) karena ada penampakan aneh di latar belakang.」
- A. pansos
- B. salfok (gagal fokus)
- C. mager
- D. baper

??? note "正解と解説"
    **正解**: 「**B. salfok (gagal fokus)**」
    
    **解説**: 本筋と違う部分に視線や注意を奪われることは「**salfok (gagal fokus)**」と言います。

### 問50. 「有名人との関係を誇示して自らの知名度を上げようとする売名行為」の現代流行語は？
「Tindakan pemuda itu dianggap warganet sekadar (...) demi mendapat banyak pengikut.」
- A. cari gara-gara
- B. curi perhatian
- C. panjat sosial (pansos)
- D. banting tulang

??? note "正解と解説"
    **正解**: 「**C. panjat sosial (pansos)**」
    
    **解説**: インフルエンサー界隈でフォロワー稼ぎ・売名を狙う行為は「**panjat sosial (pansos)**」と呼ばれます。

---

## 📊 総合スコア採点基準表とレベル判定

あなたの正解数を数えて、以下の実力判定表と照らし合わせてみてください。

| 正解数 | 認定レベル | コロケーション運用力判定とアドバイス |
| :--- | :--- | :--- |
| **45〜50問** | **マスター級 (C2 / ネイティブ同等)** | **完璧な語彙共起感覚！** ビジネス、司法、時事から現代スラングに至るまで、ネイティブスピーカーと寸分違わぬ自然な単語選択ができています。通訳・翻訳のプロフェッショナルとして即戦力の実力です。 |
| **38〜44問** | **上級 (C1 / 最上位ビジネス)** | **卓越した表現力！** 大半の重要コロケーションが身についており、格調高い論文や公式スピーチも自在にこなせます。微妙な前置詞チャンクや専門語彙の精度をさらに磨きましょう。 |
| **30〜37問** | **中上級 (B2 / 業務遂行可能)** | **堅実な語彙力！** 基本的な動詞や身体表現、日常ビジネスの連語は十分に理解できています。時事専門語や現代スラングの短縮形への理解を深めることで、一皮剥けた流暢さが手に入ります。 |
| **20〜29問** | **中級 (B1 / 学習途上)** | **着実な基礎力！** 単語の意味は知っていても「どの単語と結びつくか」で迷いが生じる段階です。セクション31の第1251〜1290記事の例文カードを音読し、塊（チャンク）で口ずさむ習慣をつけましょう。 |
| **19問以下** | **初中級 (A2〜B1未満)** | **伸び代たっぷり！** 単語の単体暗記から「2語以上のセットで覚える」アプローチへと学習法をシフトする絶好のチャンスです。本辞典を最初からゆっくり復習してください。 |

---

## 祝・セクション31「最頻出コア語根＆コロケーション辞典」完結！

全50記事にわたる長大なコロケーションの旅、大変お疲れ様でした！  
単語の丸暗記を脱し、**「語と語の有機的な結びつき（コロケーション）」**をマスターしたあなたのインドネシア語は、不自然な「直訳調の不協和音」から解放され、現地の人々の心に自然にすっと届く**生きた本物のインドネシア語**へと劇的な進化を遂げました。

次なる**セクション32「【長文読解】インドネシア現代社会・トレンド深層読解（全50記事）」**では、このコロケーション辞典で培った強力な語彙ネットワークを武器に、EV革命、TikTok Shop、デジタル金融、ハラール産業など、現代インドネシアの最前線を走るリアルな長文記事の深層読解へと進出します！

---

## 関連リンク

- [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return md

def main():
    os.makedirs("docs/lexicon", exist_ok=True)
    
    # Generate 1291-1299
    for data in articles_1_to_9:
        content = generate_standard_article(data)
        with open(data["filename"], "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {data['filename']}")
        
    # Generate 1300
    c1300 = generate_article_1300()
    f1300 = "docs/lexicon/50-comprehensive-collocation-mastery.md"
    with open(f1300, "w", encoding="utf-8") as f:
        f.write(c1300)
    print(f"[OK] Generated: {f1300}")

if __name__ == "__main__":
    main()
