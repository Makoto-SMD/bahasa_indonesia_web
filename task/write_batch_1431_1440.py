# -*- coding: utf-8 -*-
"""
セクション34 第4バッチ (1431-1440) 記事生成スクリプト
【資格演習】検定・UKBI直前実戦模試＆徹底解説
難問空所補充・誤文訂正・速読・特殊語彙・正書法EYD5特訓
"""

import os

articles = [
    {
        "filename": "31-cloze-test-grammar-advanced-01.md",
        "title": "1431. 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選 Vol. 1",
        "level": "技能検定B級〜A級 / UKBI Madya〜Unggul（CEFR B2〜C1）",
        "intro": "検定試験やUKBIの文法セクションにおいて、配点が高くかつ受験者の正答率が最も割れるのが「高度な空所補充問題（Cloze Test）」です。特に、接辞の微細な意味変化（使役・適用・相互・反復）、動詞と特定前置詞の結合（コロケーション）、文脈に応じた論理接続詞の選択は合否を決定づけます。本稿では実践的演習を通じて確固たる解答力を構築します。",
        "theory": [
            ("接辞補充の瞬時判別アルゴリズム",
             "1. **文構造（S-V-O）と目的語の性質の特定**: \n"
             "   - 後続の名詞が「場所・相手（人）」→ **meN--i**（例: mendatangi lokasi, melengkapi berkas）。\n"
             "   - 後続の名詞が「移動する物体・結果生じる状態」→ **meN--kan**（例: mendatangkan barang, menyampaikan pesan）。\n"
             "2. **自動詞か他動詞かの判別**: \n"
             "   - 目的語を取らない状態・動作 → **ber-**（例: bergerak, berkembang）。\n"
             "   - 受動的・偶発的完了状態 → **ter-**（例: terkejut, terlaksana）。")
        ],
        "problems": [
            {
                "q": "【空所補充問題 1】次の文の空所に入る最適な動詞はどれか？\n\"Gubernur terpilih berjanji akan [______] seluruh aspirasi masyarakat tanpa membeda-bedakan latar belakang politik.\"",
                "options": ["A. mengakomodasi", "B. mengakomodasikan", "C. mengakomodir", "D. terakomodasi"],
                "ans": "A. mengakomodasi",
                "expl": "語根 akomodasi（適応・収容）に meN- が付いた他動詞形は「mengakomodasi（〜を受け入れる・配慮する・収容する）」が標準形（kata baku）です。「mengakomodir」はオランダ語由来の非標準形（tidak baku）、「mengakomodasikan」は不要な接尾辞が付加された冗長形です。"
            },
            {
                "q": "【空所補充問題 2】次の文の空所に入る適切な前置詞はどれか？\n\"Pihak manajemen menyampaikan permohonan maaf [______] ketidaknyamanan yang dialami para penumpang akibat penundaan penerbangan.\"",
                "options": ["A. atas", "B. pada", "C. kepada", "D. dari"],
                "ans": "A. atas",
                "expl": "「permohonan maaf atas...（〜に対する謝罪）」「terima kasih atas...（〜に対する感謝）」のように、感謝や陳謝の対象・理由には前置詞「atas」を用います。"
            }
        ],
        "table": [
            ("mengakomodasi aspirasi", "要望・願いを受け入れる・汲み取る"),
            ("permohonan maaf atas...", "〜に対するお詫び・謝罪"),
            ("menanggapi keluhan", "苦情・クレームに対応する（menanggapiはmeN--i）"),
            ("melimpahkan wewenang", "権限を委譲する・委託する（melimpahkanはmeN--kan）"),
            ("berorientasi pada...", "〜を志向する・〜本位の（padaと結合）"),
            ("terlepas dari...", "〜は別として・〜にかかわらず（dariと結合）")
        ],
        "pro_tip": "空所補充では、空所の直後にある「前置詞」や「目的語名詞」を手がかりにするのが鉄則です。例えば「pada」があれば「berdasarkan / berlandaskan / bergantung」が最有力候補となります。"
    },
    {
        "filename": "32-cloze-test-grammar-advanced-02.md",
        "title": "1432. 【難問空所補充】接辞・前置詞・接続詞の精密補充ドリル 30選 Vol. 2",
        "level": "技能検定B級〜A級 / UKBI Madya〜Unggul（CEFR B2〜C1）",
        "intro": "難問空所補充ドリル第2弾では、論理的思考力を試す「相関接続詞（Konjungsi Korelatif）」「譲歩・因果の複文マーカー」、および「名詞化接辞（peN--an vs per--an）」の厳格な使い分けをマスターします。上級文脈で文章の筋道を正確に辿る技術を鍛えます。",
        "theory": [
            ("相関接続詞（Konjungsi Korelatif）の絶対的ペアリング",
             "- **baik... maupun...**: AもBも（両方肯定）。※baik... atau... は誤り。\n"
             "- **tidak hanya... tetapi juga...** (または **bukan hanya... melainkan juga...**): 〜だけでなく〜も。\n"
             "- **bukan... melainkan...**: 〜ではなくて〜（名詞否定の対比）。\n"
             "- **tidak... tetapi...**: 〜ではなくて〜（動詞・形容詞否定の対比）。\n"
             "- **sedemikian rupa... sehingga...**: 〜のようなやり方で、その結果〜。")
        ],
        "problems": [
            {
                "q": "【相関接続詞補充】次の文の空所に入る正しい接続詞のペアはどれか？\n\"Program beasiswa ini terbuka [______] mahasiswa berprestasi [______] peneliti muda dari seluruh pelosok tanah air.\"",
                "options": [
                    "A. baik / maupun",
                    "B. baik / atau",
                    "C. bukan / tetapi",
                    "D. antara / dan juga"
                ],
                "ans": "A. baik / maupun",
                "expl": "「baik A maupun B（AであれBであれ両方）」が規範文法における唯一正しい相関ペアです。日常会話で頻出する「baik... atau...」は検定・UKBIでは文法エラーとして厳格に排除されます。"
            },
            {
                "q": "【名詞化接辞の識別】次の文の空所に入る適切な派生名詞はどれか？\n\"[______] wilayah perbatasan menjadi prioritas utama kabinet kerja dalam rangka memperkuat kedaulatan negara.\"",
                "options": ["A. Pembangunan", "B. Perkembangan", "C. Membangun", "D. Bangunan"],
                "ans": "A. Pembangunan",
                "expl": "主語の位置にあり、「地域を開発・建設すること（他動詞的プロセス）」を指すため、動作主体・作為の名詞化である「pembangunan（開発・建設）」が正解です（perkembangan=発展・成長、bangunan=建物/建造物）。"
            }
        ],
        "table": [
            ("baik... maupun...", "〜も〜も（両者肯定）"),
            ("bukan hanya... melainkan juga...", "〜のみならず〜もまた"),
            ("sedemikian rupa sehingga...", "〜なように…その結果…"),
            ("pembangunan infrastruktur", "インフラ開発・整備（作為のプロセス）"),
            ("perkembangan teknologi", "テクノロジーの発展・進歩（自然な推移）"),
            ("perselisihan perdata", "民事紛争（相互関係の名詞化）")
        ],
        "pro_tip": "「peN--an」は他動詞（meN-）に対応し「〜すること（開発、配分、破壊）」を意味するのに対し、「per--an」は自動詞（ber-）に対応し「状態・相互関係・場所（発展、紛争、拠点）」を意味します。"
    },
    {
        "filename": "33-error-identification-mastery-01.md",
        "title": "1433. 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問 Vol. 1",
        "level": "技能検定A級 / UKBI Unggul（CEFR C1）",
        "intro": "誤文訂正（Error Identification / Pembetulan Kalimat Rusak）は、文法規則の完全な内在化を求める検定上級・UKBIの最難関関門です。一見すると自然に読める文の中に巧妙に潜む「疑似関係詞の誤用」「重複表現（Pleonasme）」「前置詞の二重使用」を瞬時に暴く眼力を養成します。",
        "theory": [
            ("上級者が引っかかる三大文法トラップ Vol. 1",
             "1. **関係代名詞 di mana / yang mana の誤用**: 英語の where / which を直訳した「..., di mana hal itu...」はインドネシア語正用法では完全な誤謬。主節と独立させるか「yang」「sehingga」で結ぶ。\n"
             "2. **重複表現（Pleonasme）の冗長エラー**:\n"
             "   - 誤: agar supaya → 正: **agar** または **supaya**\n"
             "   - 誤: adalah merupakan → 正: **adalah** または **merupakan**\n"
             "   - 誤: demi untuk → 正: **demi** または **untuk**\n"
             "   - 誤: saling tolong-menolong → 正: **saling menolong** または **tolong-menolong**\n"
             "3. **前置詞の二重配置**: selain daripada itu → 正: **selain itu**。")
        ],
        "problems": [
            {
                "q": "【誤文箇所指摘問題】次の文の中で、規範文法上誤り（tidak baku）を含む部分はどれか？\n\"Pendidikan karakter [A: adalah merupakan] fondasi fundamental [B: dalam rangka] membentuk generasi penerus bangsa [C: yang berintegritas tinggi] [D: serta berdaya saing].\"",
                "options": ["A", "B", "C", "D"],
                "ans": "A",
                "expl": "「adalah」と「merupakan」はどちらも同一の述語連結語（kopula）であり、重ねて使う「adalah merupakan」は典型的な重複表現（pleonasme）の誤用です。「adalah」または「merupakan」のどちらか一方のみを用いなければなりません。"
            },
            {
                "q": "次の文の中で、誤りのない完全に文法的な文はどれか？",
                "options": [
                    "A. Kita harus saling bantu-membantu dalam menyelesaikan krisis ini.",
                    "B. Kita harus saling membantu dalam menyelesaikan krisis ini.",
                    "C. Demi untuk kesejahteraan rakyat, proyek ini harus diselesaikan.",
                    "D. Para hadirin sekalian dipersilakan masuk ke dalam ruangan."
                ],
                "ans": "B. Kita harus saling membantu dalam menyelesaikan krisis ini.",
                "expl": "Aは「saling」と重複形「bantu-membantu」の二重使用、Cは「demi untuk」の重複、Dは「para hadirin sekalian（複数の三重表現）」および「masuk ke dalam（入る＋中へ）」の重複エラーです。唯一正しいのはBです。"
            }
        ],
        "table": [
            ("adalah merupakan", "誤謬重複（正: adalah / merupakan）"),
            ("demi untuk", "誤謬重複（正: demi / untuk）"),
            ("agar supaya", "誤謬重複（正: agar / supaya）"),
            ("saling tolong-menolong", "誤謬重複（正: saling menolong）"),
            ("sangat indah sekali", "誤謬重複（正: sangat indah / indah sekali）"),
            ("para hadirin sekalian", "誤謬重複（正: hadirin / para hadirin）")
        ],
        "pro_tip": "問題文に「adalah merupakan」「agar supaya」「saling...-an」が見えたら、0.1秒で重複エラー（Pleonasme）を疑ってください。試験作成者が好んで仕掛ける定番中の定番トラップです。"
    },
    {
        "filename": "34-error-identification-mastery-02.md",
        "title": "1434. 【誤文訂正マスター】ハイレベル文法エラー発見特訓 30問 Vol. 2",
        "level": "技能検定A級 / UKBI Unggul（CEFR C1）",
        "intro": "誤文訂正ドリル第2弾では、より構造的・統語的な難所である「主語欠落文（Kalimat Tanpa Subjek）」「従属節の孤立（Anak Kalimat Menggantung）」「受動態における人称代名詞の語順破壊」にメスを入れます。複雑な公用文の骨格を正確に見抜く訓練です。",
        "theory": [
            ("上級者が引っかかる構造トラップ Vol. 2",
             "1. **前置詞による主語の埋没（Subjek Terhalang Preposisi）**:\n"
             "   - 誤: **Dalam rapat itu** memutuskan untuk membatalkan proyek.\n"
             "   - 正: **Rapat itu** memutuskan... または **Dalam rapat itu diputuskan** untuk...\n"
             "   ※文頭の前置詞句（Keterangan）のせいで、能動他動詞「memutuskan」の主語が存在しない破綻文。\n"
             "2. **従属節のみで独立した破綻文**:\n"
             "   - 誤: Meskipun inflasi menurun drastis. Tetapi daya beli masyarakat belum pulih.\n"
             "   - 正: Meskipun inflasi menurun drastis, daya beli masyarakat belum pulih.\n"
             "3. **一人称受動態の助動詞配置エラー**:\n"
             "   - 誤: Laporan itu sudah dikerjakan oleh saya.（口語・非標準）\n"
             "   - 正: Laporan itu **sudah saya kerjakan**.")
        ],
        "problems": [
            {
                "q": "【主語欠落エラー問題】次の文の中で、文法的に正しい完全文（kalimat efektif）はどれか？",
                "options": [
                    "A. Melalui penelitian ini diharapkan dapat memberikan kontribusi nyata bagi pengembangan energi terbarukan.",
                    "B. Penelitian ini diharapkan dapat memberikan kontribusi nyata bagi pengembangan energi terbarukan.",
                    "C. Untuk para peserta seminar dimohon segera memasuki auditorium.",
                    "D. Bagi yang kehilangan dompet dapat mengambilnya di pos keamanan."
                ],
                "ans": "B. Penelitian ini diharapkan dapat memberikan kontribusi nyata bagi pengembangan energi terbarukan.",
                "expl": "Aは文頭に「Melalui」が付いているため副詞句となり主語が存在しません（主語欠落文）。Cも「Untuk」が主語を隠しており誤り、Dも「Bagi」により主語が欠けています。正しく名詞主語（Penelitian ini）から始まっているBのみが完全文です。"
            },
            {
                "q": "【受動態語順エラー】「この提案書は私たちが昨日精査いたしました」の正しい公用文受動態はどれか？",
                "options": [
                    "A. Proposal ini kami kemarin telaah secara cermat.",
                    "B. Proposal ini kemarin telah kami telaah secara cermat.",
                    "C. Proposal ini ditelaah oleh kami kemarin secara cermat.",
                    "D. Kemarin proposal ini kami telah menelaah secara cermat."
                ],
                "ans": "B. Proposal ini kemarin telah kami telaah secara cermat.",
                "expl": "前置代名詞受動文では、助動詞（telah）の直後に代名詞（kami）が密着し、その直後に語根動詞（telaah）が来ます（telah kami telaah）。時を表す副詞（kemarin）は助動詞の前に置くのが正統です。"
            }
        ],
        "table": [
            ("kalimat tanpa subjek", "主語欠落文（前置詞で主語が消えた悪文）"),
            ("kalimat efektif", "有効文（簡潔で文法的に完璧な規範文）"),
            ("anak kalimat menggantung", "主節を伴わず孤立した従属節"),
            ("pasif persona", "人称代名詞受動構文（代名詞＋語根）"),
            ("telah kami telaah", "私たちが精査した（正統な前置受動態）"),
            ("memberikan kontribusi", "貢献を果たす・寄与する")
        ],
        "pro_tip": "文頭が「Dengan...」「Dalam...」「Melalui...」「Berdasarkan...」で始まっている文を見たら、コンマの後にきちんとした『名詞の主語』があるかを必ず確認してください。主語がなくいきなり動詞が来ている文は100%主語欠落エラーです。"
    },
    {
        "filename": "35-reading-speed-comprehension-01.md",
        "title": "1435. 【速読演習】制限時間内での長文斜め読みと設問照合テクニック Vol. 1",
        "level": "技能検定B級〜A級 / UKBI Seksi III（CEFR B2〜C1）",
        "intro": "検定試験やUKBI読解セクション（Seksi III）の最大の難敵は「時間切れ」です。長大な学術・社会長文を最初から最後まで一語一句日本語に翻訳しながら読んでいては合格点を取ることは不可能です。設問を起点とし、キーワードをアンカーにして本文中を瞬時にスキャンする『スキミング＆スキャニング速読法』を体得します。",
        "theory": [
            ("情報照合の高速3ステップ手順",
             "1. **設問と選択肢の先読み（Pre-reading）**: パッセージを読む前に必ず設問のキーワード（数字、人名、固有地名、特異な名詞）を頭にインプットする。\n"
             "2. **段落の頭尾確認（Skimming）**: 各パラグラフの第1文（トピックセンテンス）と最終文だけを拾い読みし、文章全体の「論理マップ」を15秒で把握する。\n"
             "3. **アンカー検索とピンポイント照合（Scanning）**: 設問のキーワードを発見したら、その前後の2文（文脈）だけを精読し、選択肢の言い換え（paraphrase）を特定する。")
        ],
        "problems": [
            {
                "q": "【速読スキャニング演習】次の文章を素早くスキャンし、設問に答えよ。\n\n\"Kementerian Energi dan Sumber Daya Mineral (ESDM) menargetkan bauran energi baru terbarukan (EBT) mencapai 23 persen pada 2025. Namun, hingga akhir semester pertama 2024, realisasinya baru menyentuh angka 13,8 persen. Tantangan utama lambatnya penetrasi ini antara lain tingginya biaya investasi awal untuk pembangkit listrik tenaga surya (PLTS) atap, belum memadainya infrastruktur transmisi pintar, serta negosiasi tarif jual-beli listrik dengan PLN yang kerap memakan waktu panjang.\"\n\n問: 本文において、EBT（再生可能エネルギー）普及の遅れをもたらす主因として明示されていないものはどれか？",
                "options": [
                    "A. 屋根型太陽光発電の初期投資コストの高さ",
                    "B. スマート送電インフラの未整備",
                    "C. 国内における石炭埋蔵量の枯渇",
                    "D. PLN（国営電力会社）との電力売買価格交渉の長期化"
                ],
                "ans": "C. 国内における石炭埋蔵量の枯渇",
                "expl": "本文中の「Tantangan utama lambatnya penetrasi ini antara lain...」以降をスキャンすると、A（biaya investasi awal PLTS atap）、B（infrastruktur transmisi pintar）、D（negosiasi tarif... memakan waktu panjang）は明記されていますが、C（石炭枯渇）については一切言及されていません。"
            }
        ],
        "table": [
            ("bauran energi", "エネルギーミックス・電源構成比率"),
            ("energi baru terbarukan (EBT)", "新・再生可能エネルギー"),
            ("penetrasi pasar", "市場浸透・普及率"),
            ("biaya investasi awal", "初期投資費用（イニシャルコスト）"),
            ("infrastruktur transmisi", "送電網インフラ"),
            ("negosiasi tarif", "料金・価格交渉")
        ],
        "pro_tip": "「本文で言及されていないものを選べ（yang tidak disebutkan）」という否定設問では、本文中の箇条書き的列挙表現（antara lain, seperti, meliputi）に直行してアンカーを打つのが最速解法です。"
    },
    {
        "filename": "36-reading-speed-comprehension-02.md",
        "title": "1436. 【速読演習】制限時間内での長文斜め読みと設問照合テクニック Vol. 2",
        "level": "技能検定B級〜A級 / UKBI Seksi III（CEFR B2〜C1）",
        "intro": "速読演習第2弾では、事実確認問題にとどまらず「筆者の主観的態度（sikap penulis）」「文章の主眼・トーン（nada tulisan）」「言外の意図（makna tersirat）」を高速で見極める高度な推論テクニックを伝授します。論理標識（Signpost words）を追跡することで、文脈の急旋回を察知します。",
        "theory": [
            ("論理標識（Signpost Words）によるトーンの察知",
             "- **逆接・転換（Shift）**: namun, kendati demikian, alih-alih, alangkah naifnya。→ *ここから筆者の本音が語られる！*\n"
             "- **強調・着目（Focus）**: ironisnya, patut disayangkan, fakta tak terbantahkan bahwa。→ *筆者の強い感情・批判的視点！*\n"
             "- **結論・提言（Claim）**: oleh sebab itu, sudah saatnya, tiada jalan lain selain。→ *文章の主眼（Tesis）！*")
        ],
        "problems": [
            {
                "q": "【筆者の態度推論演習】次の文章を読み、設問に答えよ。\n\n\"Pemberian bantuan sosial secara masif menjelang perhelatan pemilu kerap diklaim sebagai bentuk kepedulian negara terhadap kaum marjinal. Namun, alih-alih memberdayakan ekonomi rakyat secara berkelanjutan, kebijakan populis jangka pendek ini justru berpotensi membudayakan ketergantungan dan menggerogoti ketahanan fiskal negara dalam jangka panjang.\"\n\n問: この文章における筆者の社会支援（bansos）政策に対する姿勢・態度はどのようなものか？",
                "options": [
                    "A. 貧困層の生活向上に直結するとして全面的な賛意を示している。",
                    "B. 短期的ポピュリズムであり、財政と国民の自立を損ねるとして極めて批判的である。",
                    "C. 選挙前の政策としてはやむを得ない措置であると一定の理解を示している。",
                    "D. 社会支援の内容を現金給付から現物支給に切り替えるべきだと提言している。"
                ],
                "ans": "B. 短期的ポピュリズムであり、財政と国民の自立を損ねるとして極めて批判的である。",
                "expl": "「Namun, alih-alih memberdayakan...（〜を自立させるどころか）」「kebijakan populis jangka pendek（短期的ポピュリスト政策）」「membudayakan ketergantungan（依存を定着させる）」「menggerogoti ketahanan fiskal（国家財政を蝕む）」という極めて批判的な語彙連鎖から、Bが明白な正解です。"
            }
        ],
        "table": [
            ("alih-alih...", "〜どころか・〜する代わりに"),
            ("kebijakan populis", "ポピュリズム政策・大衆迎合策"),
            ("memberdayakan", "エンパワーする・自立させる"),
            ("menggerogoti", "蝕む・侵食する・少しずつ損なう"),
            ("ketahanan fiskal", "財政健全性・財政耐力"),
            ("sikap kritis", "批判的な態度・姿勢")
        ],
        "pro_tip": "「alih-alih（〜どころか）」「menggerogoti（蝕む）」などのマイナス感情を帯びた動詞（Loaded words）は、筆者の批判的スタンスを特定するための決定打になります。"
    },
    {
        "filename": "37-formal-affixation-traps.md",
        "title": "1437. 検定で狙われる「不規則鼻音化・特殊接辞」の落とし穴完全網羅",
        "level": "技能検定B級〜A級 / UKBI Seksi II（CEFR B2〜C1）",
        "intro": "インドネシア語の接頭辞 meN- および peN- における鼻音化規則（K-P-S-Tの脱落）は学習初期に習得しますが、検定上級やUKBIでは『規則が適用されない外来子音結合語』や『特殊な二重子音語』が出題され、多くの受験生が足をすくわれます。例外パターンを完全網羅して失点をゼロにします。",
        "theory": [
            ("K-P-S-Tが「脱落しない」外来借用語の二重子音（Kluster Konsonan）",
             "語根の先頭が「子音＋子音（kluster）」で始まる外来語は、K-P-S-Tであっても**脱落せず**そのまま残る！\n"
             "- **k-**: kritik → **mengkritik** (×mengritik), kristal → **mengkristal**, konfirmasi → **mengonfirmasi** (単一子音扱いで脱落)。\n"
             "- **p-**: produksi → **memproduksi** (×memroduksi), proses → **memproses**, protes → **memprotes**。\n"
             "- **s-**: skala → **mengkala / menskalakan**, steril → **mensterilkan**, stabil → **menstabilkan**。\n"
             "- **t-**: traksi → **mentraksi**, transfer → **mentransfer** (×menransfer)。"),
            ("1音節語根（Monosilabel）の特殊鼻音化（menge- / penge-）",
             "- bom → **mengebom** / **pengeboman**\n"
             "- cat → **mengecat** / **pengecatan**\n"
             "- cek → **mengecek** / **pengecekan**\n"
             "- las → **mengelas** / **pengelasan**\n"
             "- klik → **mengeklik** / **pengeklikan**")
        ],
        "problems": [
            {
                "q": "【不規則鼻音化正誤問題】次の選択肢の中で、EYD第5版基準で綴りが完全に正しい動詞はどれか？",
                "options": [
                    "A. Perusahaan itu berencana memroduksi massal kendaraan listrik tahun depan.",
                    "B. Perusahaan itu berencana memproduksi massal kendaraan listrik tahun depan.",
                    "C. Tim auditor sedang mengevaluasikan laporan keuangan tahunan.",
                    "D. Pihak bank telah menransfer dana kompensasi ke rekening korban."
                ],
                "ans": "B. Perusahaan itu berencana memproduksi massal kendaraan listrik tahun depan.",
                "expl": "語根「produksi」は語頭が二重子音「pr-」であるため、pは脱落せず「memproduksi」となります（Aは誤り）。Dの「transfer」も「tr-」のため脱落せず「mentransfer」が正解です。Cは「mengevaluasi」が標準形です。"
            },
            {
                "q": "語根「sertifikasi（認証・資格付与）」に接辞 meN--kan が付いた正しい派生語はどれか？",
                "options": [
                    "A. menyertifikasikan",
                    "B. mensertifikasikan",
                    "C. mengsertifikasikan",
                    "D. besertifikasi"
                ],
                "ans": "A. menyertifikasikan",
                "expl": "語根「sertifikasi」の頭文字「s」の後ろは母音「e」であり二重子音ではありません。したがって通常規則通り s は脱落して ny に鼻音化し、「menyertifikasikan」となります。"
            }
        ],
        "table": [
            ("memproduksi", "生産する（pr-のためpは脱落しない）"),
            ("memproses", "処理する・加工する（pr-のためpは脱落しない）"),
            ("mengkritik", "批判する（kr-のためkは脱落しない）"),
            ("mentransfer", "振り込む・移転する（tr-のためtは脱落しない）"),
            ("mengeklik", "クリックする（1音節語のため menge-）"),
            ("menyertifikasikan", "認証する（se-は単一子音＋母音なのでs脱落）")
        ],
        "pro_tip": "「memproduksi」「mengkritik」「mentransfer」は毎年必ずどこかの試験で問われます。「子音＋r/l（kluster）で始まる語は脱落しない」と暗記してください。"
    },
    {
        "filename": "38-archaic-classical-terms-in-exams.md",
        "title": "1438. 上級試験に登場する文語・古典由来語彙（syahdan, alkisah, bahwasanya）",
        "level": "技能検定A級〜特A級 / UKBI Seksi III（CEFR C1〜C2）",
        "intro": "検定最上級（A級・特A級）の読解問題やUKBI最上位バンドでは、マレー古典文学（Hikayat）の抜粋や、伝統的な文語・古風表現（kata arkais / klasik）が突如として登場します。「syahdan」「alkisah」「sebermula」などの物語導入語や「bahwasanya」「nan」などの古典的接続詞の用法を知っておくことで、慌てず冷静に対処できます。",
        "theory": [
            ("古典マレー語由来の頻出接続詞・談話標識（Penanda Wacana Klasik）",
             "1. **物語の開始**: \n"
             "   - **Alkisah / Tersebutlah perkataan**: 物語の始まり。「昔々、あるところに…」\n"
             "   - **Sebermula**: 物語の端緒。「そもそも、事の起こりは…」\n"
             "2. **話題の転換・継続**: \n"
             "   - **Syahdan / Hatta**: 話題の転換。「さて、それから…」「一方で…」\n"
             "   - **Kalakian**: 時間の経過。「その後、やがて…」\n"
             "3. **文語的強調・関係詞**: \n"
             "   - **Bahwasanya**: 「〜であるということは誠に…」「実に〜である（bahwaの強調古語）」\n"
             "   - **Nan**: 文語的「yang」。「gadis nan rupawan（美しき乙女）」")
        ],
        "problems": [
            {
                "q": "【古典文語読解問題】次の古典物語の冒頭文における「Hatta」の意味・役割として最も適切なものはどれか？\n\"Hatta beberapa lamanya baginda bersemayam di atas takhta, maka datanglah seorang saudagar kaya membawa persembahan yang tiada bertara.\"",
                "options": [
                    "A. 時間の経過や場面の転換を表す「さて、それから／やがて」",
                    "B. 理由や原因を表す「〜のせいで／〜のために」",
                    "C. 否定を表す「決して〜ない／〜はずがない」",
                    "D. 比較を表す「〜と同じくらい／〜に匹敵する」"
                ],
                "ans": "A. 時間の経過や場面の転換を表す「さて、それから／やがて」",
                "expl": "古典文学で多用される「Hatta」は、アラビア語・ペルシア語影響下で発達した古典マレー語の談話標識で、「さて／それから／やがて（maka kemudian）」という場面転換・時間経過を示します。"
            },
            {
                "q": "現代の公用文や憲法前文などでも用いられる文語表現「bahwasanya」と同義の標準現代語はどれか？",
                "options": ["A. sesungguhnya bahwa", "B. barangkali jika", "C. seandainya bila", "D. meskipun demikian"],
                "ans": "A. sesungguhnya bahwa",
                "expl": "「Bahwasanya」はアラビア語借用語に由来し、インドネシア憲法（UUD 1945）の冒頭文（\"Bahwa sesungguhnya kemerdekaan itu...\"）などに見られる通り、「sesungguhnya bahwa（真に〜であることには）」という意味を持ちます。"
            }
        ],
        "table": [
            ("Alkisah", "物語の始まり・むかしむかし（once upon a time）"),
            ("Hatta / Syahdan", "さて・それから・一方（meanwhile / then）"),
            ("Sebermula", "そもそも・事の起こりは（in the beginning）"),
            ("Kalakian", "その後・やがて（thereafter）"),
            ("Bahwasanya", "まことに〜である（verily / truly that）"),
            ("Nan", "〜なる・〜である（yangの文語・詩的表現）")
        ],
        "pro_tip": "古典テキストが出題された場合、HattaやSyahdanなどの接続語は「場面の区切り」に過ぎないため、これらに惑わされず直後の動詞と主語に焦点を当てることが正解への近道です。"
    },
    {
        "filename": "39-acronyms-abbreviations-mastery.md",
        "title": "1439. 検定必須！政治・社会・経済の公式略語・頭字語200選",
        "level": "技能検定B級〜特A級 / UKBI全等級（CEFR B1〜C2）",
        "intro": "インドネシアの新聞・ニュース・公文書は世界有数の「略語・頭字語（Akronim & Singkatan）大国」です。検定読解やリスニングでこれらを知らないと、文脈全体の意味を見失う致命的な原因になります。国家機関、経済・法律、治安、社会運動の重要アクロニムを完全体系化して習得します。",
        "theory": [
            ("アクロニム（Akronim）と略語（Singkatan）の構造分類",
             "1. **国家・政治・司法**: \n"
             "   - **KPK** (Komisi Pemberantasan Korupsi): 汚職撲滅委員会\n"
             "   - **MK** (Mahkamah Konstitusi) / **MA** (Mahkamah Agung): 憲法裁判所 / 最高裁判所\n"
             "   - **DPR** (Dewan Perwakilan Rakyat): 国民協議会・国会\n"
             "   - **IKN** (Ibu Kota Nusantara): 新首都ヌサンタラ\n"
             "2. **経済・金融・公的企業**: \n"
             "   - **BUMN** (Badan Usaha Milik Negara): 国営企業\n"
             "   - **APBN** (Anggaran Pendapatan dan Belanja Negara): 国家歳入歳出予算\n"
             "   - **OJK** (Otoritas Jasa Keuangan): 金融活動監督庁\n"
             "   - **BI** (Bank Indonesia): インドネシア中央銀行\n"
             "3. **法律・警察・捜査実務**: \n"
             "   - **OTT** (Operasi Tangkap Tangan): 現行犯逮捕作戦（KPKなどが実施）\n"
             "   - **KUHP** (Kitab Undang-Undang Hukum Pidana): 刑法典\n"
             "   - **SP3** (Surat Perintah Penghentian Penyidikan): 捜査打ち切り命令書")
        ],
        "problems": [
            {
                "q": "【略語識別問題】インドネシアのニュースで頻出する「KPK menggelar OTT terhadap kepala daerah」という見出しの「OTT」が意味する活動として最も正確なものはどれか？",
                "options": [
                    "A. 現行犯逮捕・おとり捜査作戦（Operasi Tangkap Tangan）",
                    "B. 財務諸表の公開監査手続き（Operasi Transparansi Tahunan）",
                    "C. 地方首長の臨時弾劾裁判（Otoritas Tindak Tuntutan）",
                    "D. 資産公開制度の点検（Operasi Tinjauan Terbuka）"
                ],
                "ans": "A. 現行犯逮捕・おとり捜査作戦（Operasi Tangkap Tangan）",
                "expl": "「OTT」は「Operasi Tangkap Tangan（現行犯逮捕捜査）」の略で、汚職撲滅委員会（KPK）や警察が贈収賄の現場を押さえて即座に拘束する強制捜査を指します。"
            },
            {
                "q": "金融・経済ニュースで登場する「OJK」の正式名称と役割の組み合わせとして正しいものはどれか？",
                "options": [
                    "A. Otoritas Jasa Keuangan（銀行・金融機関を監督する公的機関）",
                    "B. Organisasi Jaringan Kerja（全国労働組合ネットワーク）",
                    "C. Operasi Jaminan Komoditas（一次産品価格保証機構）",
                    "D. Otoritas Jalan tol dan Konstruksi（高速道路建設公社）"
                ],
                "ans": "A. Otoritas Jasa Keuangan（銀行・金融機関を監督する公的機関）",
                "expl": "「OJK」は「Otoritas Jasa Keuangan（金融サービス庁／金融活動監督庁）」で、日本の金融庁に相当する独立監督機関です。"
            }
        ],
        "table": [
            ("BUMN", "Badan Usaha Milik Negara（国営企業）"),
            ("APBN", "Anggaran Pendapatan dan Belanja Negara（国家予算）"),
            ("OTT", "Operasi Tangkap Tangan（現行犯逮捕作戦）"),
            ("KPK", "Komisi Pemberantasan Korupsi（汚職撲滅委員会）"),
            ("IKN", "Ibu Kota Nusantara（新首都ヌサンタラ）"),
            ("OJK", "Otoritas Jasa Keuangan（金融活動監督庁）")
        ],
        "pro_tip": "略語は大文字だけで綴られるもの（DPR, KPK, BUMN）と、単語のように発音されるアクロニム（Bappenas, Puskesmas, Tilang）があります。後者は頭文字のみ大文字または小文字表記になる点も正書法上重要です。"
    },
    {
        "filename": "40-punctuation-eyd-mechanics.md",
        "title": "1440. EYD第5版に基づく句読点（コンマ、セミコロン、コロン）の正確な用法",
        "level": "技能検定B級〜特A級 / UKBI Seksi II（CEFR B2〜C2）",
        "intro": "UKBI第2セクション（Seksi II）および技能検定の上級筆記において、高得点者と一般受験者を分かつ決定打が「句読点記号（Tanda Baca）の正確な用法」です。コンマ（tanda koma）、セミコロン（tanda titik koma）、コロン（tanda titik dua）、ハイフン（tanda hubung）の公式レギュレーション（EYD Edisi V）を完全マスターします。",
        "theory": [
            ("EYD第5版における句読点の厳格ルール",
             "1. **コンマ（, / tanda koma）の必須配置**: \n"
             "   - **文頭副詞句の後**: \"Pada tahun 2024**,** pemerintah meluncurkan...\"\n"
             "   - **逆接接続詞の前**: \"..., **tetapi**...\" \"..., **melainkan**...\" \"..., **sedangkan**...\"\n"
             "   - **文頭接続詞の後**: \"Oleh karena itu**,**...\" \"Selain itu**,**...\" \"Namun**,**...\"\n"
             "   - **並列要素の最終項の前（オックスフォード・コンマ）**: \"buku, pensil**,** dan penghapus\" (×buku, pensil dan penghapus)。\n"
             "2. **コロン（: / tanda titik dua）の用法**: \n"
             "   - 直前に完全な文（klausa lengkap）がある場合のみ列挙に使用可能。\n"
             "   - 正: Kami memerlukan alat tulis**: yaitu** buku dan pena. (×Kami memerlukan: buku dan pena)\n"
             "3. **セミコロン（; / tanda titik koma）の用法**: \n"
             "   - 接続詞を用いずに等位節を接続する（Hari sudah malam; anak-anak masih belajar）。\n"
             "   - 箇条書きの各項目の末尾。")
        ],
        "problems": [
            {
                "q": "【EYD句読点正誤問題】EYD第5版の基準に照らし、句読点の用法が完全に正しい文はどれか？",
                "options": [
                    "A. Ibu membeli beras, minyak goreng, dan telur di pasar tradisional.",
                    "B. Ibu membeli beras, minyak goreng dan telur di pasar tradisional.",
                    "C. Ibu membeli: beras, minyak goreng, dan telur di pasar tradisional.",
                    "D. Ibu membeli beras, minyak goreng, dan telur, di pasar tradisional."
                ],
                "ans": "A. Ibu membeli beras, minyak goreng, dan telur di pasar tradisional.",
                "expl": "インドネシア語の正書法（EYD V）では、3つ以上の要素を並列する際、最後の「dan」の前にも必ずコンマを打たなければなりません（rincian tiga unsur atau lebih）。したがってAが正解です（Bはコンマ欠落、Cは完全な節の前にコロンを置いているため誤り）。"
            },
            {
                "q": "文頭の談話接続詞（konjungsi antarkalimat）の後ろの句読点として正しいものはどれか？",
                "options": [
                    "A. Namun demikian, kita tidak boleh berpuas diri.",
                    "B. Namun demikian kita tidak boleh berpuas diri.",
                    "C. Namun, demikian kita tidak boleh berpuas diri.",
                    "D. Namun demikian; kita tidak boleh berpuas diri."
                ],
                "ans": "A. Namun demikian, kita tidak boleh berpuas diri.",
                "expl": "「Namun demikian」「Oleh karena itu」「Akan tetapi」などの文頭接続詞の直後には、必ずコンマ（,）を打たなければなりません。"
            }
        ],
        "table": [
            ("tanda koma (,)", "コンマ（並列の最終dan前、文頭副詞後、tetapi前）"),
            ("tanda titik koma (;)", "セミコロン（接続詞なしの等位節接続、箇条書き）"),
            ("tanda titik dua (:)", "コロン（完全文に後続する詳細列挙、対話劇）"),
            ("tanda hubung (-)", "ハイフン（重複語、接辞と大文字の結合 se-Indonesia）"),
            ("tanda pisah (—)", "ダッシュ（挿入句・思考の飛躍）"),
            ("tanda petik (”...”)", "二重引用符（直接話法、論文タイトル）")
        ],
        "pro_tip": "UKBIの文法問題では「danの前のコンマ抜け」「Namunの後のコンマ抜け」「動詞の直後にコロンを置くエラー（Kami menjual: buku...）」が頻出3大句読点トラップです。"
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
        table_header = "| 区分・ランク | 点数・表現 | 特徴・解説 |\n| :--- | :--- |\n"
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
