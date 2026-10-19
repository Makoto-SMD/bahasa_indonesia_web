# -*- coding: utf-8 -*-
"""
セクション35 第1バッチ (1451-1460) 記事生成スクリプト
【表現技法】プロの翻訳・通訳・高度表現テクニック
日イ翻訳の根本原理・構文転換・対照言語学的アプローチ
"""

import os

articles = [
    {
        "filename": "01-jp-id-translation-core-principles.md",
        "title": "1451. 【翻訳技法】日イ翻訳の根本原理：日本語の主語省略とインドネシア語の主語復元",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語は「話題優勢言語（Topic-prominent Language）」であり、文脈から明らかな主語や行為者を徹底的に省略する特徴を持ちます。一方、インドネシア語は英語と同様に「主語・述語の明確な結合（S-V構造）」を厳格に要求する言語です。日本語の文をそのまま直訳すると主語欠落の不自然な悪文（kalimat pincang）になるため、文脈から適切な主語（kami, kita, perusahaan, pemerintah など）を特定・復元するプロの翻訳技法を解説します。",
        "theory": [
            ("主語復元（Restorasi Subjek）の判断基準",
             "1. **発信者の視点（一人称復元）**: \n"
             "   - 日: 「検討の上、明日までにご連絡いたします。」\n"
             "   - 誤: *Akan menghubungi sampai besok setelah mempertimbangkan.\n"
             "   - 正: **Kami akan menghubungi Anda** paling lambat besok setelah mempertimbangkannya.\n"
             "2. **包括的共同体（包括的一人称 kita の活用）**: \n"
             "   - 日: 「地球環境を守るために、省エネに取り組む必要があります。」\n"
             "   - 正: **Kita perlu** melakukan penghematan energi demi menjaga kelestarian lingkungan bumi.\n"
             "3. **組織・制度・一般主体（Institusi / Pelaku Umum）**: \n"
             "   - 日: 「申請書は窓口で受理されます。」\n"
             "   - 正: **Petugas loket akan menerima** berkas permohonan tersebut (または Berkas permohonan **diterima di loket**).")
        ],
        "problems": [
            {
                "q": "【主語復元翻訳問題】次の日本文のビジネスインドネシア語訳として最も自然で文法的に完全なものはどれか？\n「来週水曜日までに修正版の図面を再提出していただけますと幸甚に存じます。」",
                "options": [
                    "A. Kami sangat menghargai apabila Anda dapat menyerahkan kembali revisi gambar rancangan paling lambat hari Rabu depan.",
                    "B. Sangat bahagia kalau bisa kirim lagi gambar revisi sampai hari Rabu depan.",
                    "C. Jika menyerahkan revisi gambar hari Rabu depan, maka merasa sangat senang.",
                    "D. Tolong ya gambar revisinya dikirim balik Rabu depan biar kita senang."
                ],
                "ans": "A. Kami sangat menghargai apabila Anda dapat menyerahkan kembali revisi gambar rancangan paling lambat hari Rabu depan.",
                "expl": "日本語で省略されている「私たち（Kami）」と「あなた（Anda）」の主語を明確に復元し、公式ビジネス定型句「Kami sangat menghargai apabila Anda dapat...（〜していただけますと幸いです）」に落とし込んだAが完璧な名訳です。"
            },
            {
                "q": "「本件についてご不明な点がございましたら、いつでもお問い合わせください。」の自然なインドネシア語訳はどれか？",
                "options": [
                    "A. Apabila Anda memiliki pertanyaan terkait hal ini, jangan ragu untuk menghubungi kami kapan saja.",
                    "B. Kalau ada tidak jelas soal ini, kontak saja kapan pun.",
                    "C. Jika bingung tentang hal ini, silakan tanya terus.",
                    "D. Menghubungi kami kapan saja apabila tidak paham hal ini."
                ],
                "ans": "A. Apabila Anda memiliki pertanyaan terkait hal ini, jangan ragu untuk menghubungi kami kapan saja.",
                "expl": "主語「Anda」と「kami」を補い、「jangan ragu untuk menghubungi kami（ご遠慮なくお問い合わせください）」というビジネスの定型表現を用いたAが模範です。"
            }
        ],
        "table": [
            ("Kami sangat menghargai...", "〜していただけますと幸甚です（主語Kamiを復元）"),
            ("Jangan ragu untuk...", "ご遠慮なく〜してください（敬意を込めた依頼）"),
            ("kalimat pincang", "主語欠落などの不完全文・破綻文"),
            ("restorasi subjek", "主語の復元・明示化"),
            ("paling lambat...", "遅くとも〜までに（by no later than）"),
            ("berkas permohonan", "申請書類一式")
        ],
        "pro_tip": "日本語を訳す際は、まず「誰が誰に対して述べているのか」を行為者マップとして整理し、インドネシア語文の先頭（S）に据える癖をつけるだけで翻訳品質が劇的に向上します。"
    },
    {
        "filename": "02-handling-japanese-wa-and-ga.md",
        "title": "1452. 【翻訳技法】日本語の「は」と「が」の処理：主題提示 vs 焦点化 yang",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語学習者が最も悩む「助詞の『は』と『が』の違い」は、翻訳者にとっても極めて繊細な問題です。「は」は既知の主題提示（Topic）や対比を表し、「が」は新情報の導入や排他的焦点（Focus）を表します。インドネシア語では、この機能差を「語順」「強調小詞 -lah」「焦点化関係詞 yang」を用いて見事に再現することができます。",
        "theory": [
            ("「は」と「が」の対照言語学的マッピング",
             "1. **主題の「は」（Topic）→ 通常の文頭主語、または Adapun / Mengenai...**:\n"
             "   - 「私は田中です。」 → Saya Tanaka.\n"
             "   - 「この計画については、慎重な検討が必要です。」 → **Mengenai / Adapun rencana ini**, diperlukan pertimbangan cermat.\n"
             "2. **焦点・排他指定の「が」（Exhaustive Focus）→ 焦点化「yang」または「-lah」**:\n"
             "   - 「田中さん**が**行きます（他の誰でもなく田中さんこそが）。」 → **Tanaka-lah yang akan pergi**.\n"
             "   - 「誰が責任者ですか？ 私**が**責任者です。」 → Siapa penanggung jawabnya? — **Saya-lah penanggung jawabnya**.\n"
             "3. **現象描写の「が」（Neutral Description）→ 無標識文または倒置構文**:\n"
             "   - 「雨が降ってきた。」 → Hujan mulai turun (または Turunlah hujan).")
        ],
        "problems": [
            {
                "q": "【焦点化翻訳問題】「彼こそが、この難事件を解決した真の英雄である。」という排他的強調（〜が…した）のニュアンスを最も鮮やかに表現したインドネシア語訳はどれか？",
                "options": [
                    "A. Dialah pahlawan sejati yang berhasil memecahkan kasus pelik ini.",
                    "B. Dia adalah pahlawan sejati dan kasus ini selesai.",
                    "C. Dia pahlawan betul karena perkara ini dia bikin beres.",
                    "D. Kalau dia itu pahlawan yang bisa selesaikan kasus sulit."
                ],
                "ans": "A. Dialah pahlawan sejati yang berhasil memecahkan kasus pelik ini.",
                "expl": "排他的焦点「彼こそが…である」を表現するため、強調小詞「-lah」を代名詞に結合させた「Dialah... yang...」構文を用いたAが完璧です。"
            },
            {
                "q": "「品質は優れているが、価格が極めて高い。」という対比（は）と新情報（が）の組み合わせの的確な訳はどれか？",
                "options": [
                    "A. Kualitasnya memang unggul, tetapi harganya sangat mahal.",
                    "B. Kualitas bagus tapi uangnya banyak sekali.",
                    "C. Memang kualitas tinggi, namun biaya mahal sekali lho.",
                    "D. Soal kualitas ya oke, harga sih tinggi banget."
                ],
                "ans": "A. Kualitasnya memang unggul, tetapi harganya sangat mahal.",
                "expl": "主題対比の「〜は…だが」を「Kualitasnya memang unggul, tetapi harganya...」と格調高い標準語で再現しているAが正解です。"
            }
        ],
        "table": [
            ("Dialah yang...", "彼こそが〜した（排他的焦点の yang / -lah）"),
            ("Mengenai hal tersebut...", "その件につきましては（主題提示の「は」）"),
            ("Adapun rinciannya...", "なお、その詳細につきましては（話題展開）"),
            ("kasus pelik", "難事件・複雑で解決が困難な問題"),
            ("pahlawan sejati", "真の英雄"),
            ("kualitas unggul", "優れた品質・卓越したクオリティ")
        ],
        "pro_tip": "「AがBをした」という排他的指定（他ではなくAだ）を訳出する際は、「A-lah yang melakukan B」という公式を用いると、ネイティブのプロ翻訳者と同じ切れ味の文章になります。"
    },
    {
        "filename": "03-abstract-noun-nominalization.md",
        "title": "1453. 【翻訳技法】日本語の接尾辞型抽象名詞（〜性、〜化、〜感）のインドネシア語変換",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語のビジネス・学術文章には「安全性、可能性、利便性（〜性）」「デジタル化、都市化、合法化（〜化）」「危機感、連帯感、清潔感（〜感）」といった漢字の接尾辞による抽象名詞が頻出します。これらを機械的に直訳するのではなく、インドネシア語の造語接辞体系（ke--an, peN--an, rasa/nuansa）と的確に結びつける変換技術を体系化します。",
        "theory": [
            ("3大抽象接尾辞のインドネシア語対応パターン",
             "1. **「〜性」（性質・状態・可能性） → ke--an または -itas**:\n"
             "   - 安全性 → **keamanan**\n"
             "   - 可能性 → **kemungkinan**\n"
             "   - 柔軟性 → **fleksibilitas** / **kelenturan**\n"
             "   - 実現可能性（フィージビリティ） → **kelayakan**\n"
             "2. **「〜化」（プロセス・変革・作為） → peN--an または -isasi**:\n"
             "   - デジタル化 → **digitalisasi**\n"
             "   - 効率化 → **pengefisienan** / **peningkatan efisiensi**\n"
             "   - 義務化 → **kewajiban** / **penjadikan wajib**\n"
             "3. **「〜感」（感覚・感情・雰囲気） → rasa / nuansa / sensasi**:\n"
             "   - 危機感 → **rasa krisis** / **urgensi**\n"
             "   - 連帯感 → **rasa solidaritas**\n"
             "   - 達成感 → **rasa pencapaian** / **kepuasan tersendiri**\n"
             "   - 清潔感 → **kesan bersih** / **kebersihan**")
        ],
        "problems": [
            {
                "q": "【抽象名詞翻訳問題】「我が社は業務プロセスの合理化を通じて、コスト競争力の強化を図る。」の自然なインドネシア語訳はどれか？",
                "options": [
                    "A. Perusahaan kami berupaya memperkuat daya saing biaya melalui rasionalisasi proses operasional.",
                    "B. Perusahaan kita mau bikin kuat kompetisi harga lewat rasional operasional.",
                    "C. Kami mencoba memperbesar menang biaya dari jalan merasionalkan proses.",
                    "D. Perusahaan mau menguatkan lomba harga melalui pembikinan proses yang masuk akal."
                ],
                "ans": "A. Perusahaan kami berupaya memperkuat daya saing biaya melalui rasionalisasi proses operasional.",
                "expl": "「合理化 → rasionalisasi」「競争力 → daya saing」「強化を図る → berupaya memperkuat」という学術・経営語彙が的確に選ばれているAが正解です。"
            },
            {
                "q": "「リーダーは組織全体に危機感を共有させることが求められる。」の「危機感」の訳語として最も適切なものはどれか？",
                "options": ["A. rasa urgensi / kesadaran krisis", "B. rasa bahaya akut", "C. perasaan takut rugi", "D. nuansa celaka"],
                "ans": "A. rasa urgensi / kesadaran krisis",
                "expl": "ビジネス・組織論における「危機感（事態が急迫しているという認識）」は「rasa urgensi（切迫感）」または「kesan/kesadaran akan krisis」と表現するのがプロの定訳です。"
            }
        ],
        "table": [
            ("rasionalisasi proses", "プロセスの合理化（〜化）"),
            ("daya saing", "競争力（〜力）"),
            ("kelayakan proyek", "プロジェクトの実現可能性（フィージビリティ：〜性）"),
            ("rasa solidaritas", "連帯感（〜感）"),
            ("transparansi", "透明性（akuntabilitas=説明責任）"),
            ("efektivitas", "有効性・実効性")
        ],
        "pro_tip": "「〜化」を訳す際、単に「-isasi」を多用するのではなく、動詞句に開いて「peningkatan kualitas（品質向上＝高度化）」のように名詞句として具体化すると、より自然なインドネシア語になります。"
    },
    {
        "filename": "04-passive-to-active-transformation.md",
        "title": "1454. 【翻訳技法】日本語の受動態を自然なインドネシア語能動態 meN- に変換する定石",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語では「雨に降られた（迷惑受動）」「親に褒められた」「新型モデルが発表された」のように受動態が日常的・自動的に多用されます。しかし、これをそのままインドネシア語の di- 受動態に直訳すると、主客が不自然に歪んだり、文脈の力動性が失われる原因になります。特に日本語特有の「間接受動態」を自然な能動構文（meN-）へ構造転換するプロの技術を伝授します。",
        "theory": [
            ("日本語受動態の3大分類とインドネシア語への転換法",
             "1. **直接受動態（動作主が明確） → 能動態 meN- への転換（主客入れ替え）**:\n"
             "   - 日: 「社長は全社員から深く尊敬されている。」\n"
             "   - 直訳: *Direktur dihormati secara mendalam oleh semua karyawan.\n"
             "   - 名訳: **Seluruh karyawan sangat menghormati direktur utama**.\n"
             "2. **迷惑受動態・間接受動態（被害のニュアンス） → 状況描写・能動文への転換**:\n"
             "   - 日: 「昨日、雨に降られてずぶ濡れになった。」\n"
             "   - 直訳: *Saya dihujani kemarin... (不自然)\n"
             "   - 名訳: **Kemarin saya kehujanan hingga basah kuyup** (ke--an 偶発受動または能動).\n"
             "   - 日: 「隣の人に夜遅くまで騒がれて眠れなかった。」\n"
             "   - 名訳: **Suara bising tetangga hingga larut malam membuat saya tidak bisa tidur**.\n"
             "3. **自発・可能の受動態（〜と思われる／〜と見られる） → 三人称能動または客観副詞**:\n"
             "   - 日: 「景気は回復傾向にあると考えられる。」\n"
             "   - 名訳: **Perekonomian dinilai sedang berada dalam tren pemulihan**.")
        ],
        "problems": [
            {
                "q": "【受動態転換演習】「この新製品は多くの消費者に愛されている。」を最も生き生きとした自然なインドネシア語に訳したものはどれか？",
                "options": [
                    "A. Produk baru ini sangat dicintai oleh banyak konsumen.",
                    "B. Banyak konsumen sangat menyukai dan menggemari produk baru ini.",
                    "C. Produk ini ada rasa cinta dari banyak pembeli.",
                    "D. Banyak konsumen dibuat cinta oleh produk baru ini."
                ],
                "ans": "B. Banyak konsumen sangat menyukai dan menggemari produk baru ini.",
                "expl": "A（dicintai oleh...）も文法的に間違いではありませんが、人間を主語に据えて「Banyak konsumen sangat menyukai/menggemari...（多くの消費者が〜を愛好している）」と能動態に転換したBの方が、はるかに自然で力強い商業文になります。"
            }
        ],
        "table": [
            ("basah kuyup", "ずぶ濡れ・びしょ濡れ"),
            ("kehujanan", "雨に降られる（ke--an 偶発・被害）"),
            ("suara bising", "騒音・騒がしい音"),
            ("hingga larut malam", "夜遅くまで・深夜に至るまで"),
            ("menggemari produk", "製品を好む・愛用する"),
            ("tren pemulihan", "回復基調・持ち直しの傾向")
        ],
        "pro_tip": "「AがBによって〜される」という日本語を見たら、一度「BがAを〜する」と頭の中で能動態にひっくり返してみてください。大半のケースでその方が格段に読みやすいインドネシア語になります。"
    },
    {
        "filename": "05-active-to-passive-transformation.md",
        "title": "1455. 【翻訳技法】インドネシア語の被動構文を自然な日本語能動文に変換する定石",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "前講とは逆に、イ日翻訳（インドネシア語→日本語）において頻出する落とし穴が「インドネシア語の受動態（di- および前置代名詞受動態）の直訳癖」です。インドネシア語では客観的事実や公用報告において受動態が極めて好まれますが、日本語で「〜された」「〜によって行われた」を連発すると、極めて拙劣な翻訳調の悪文になります。自然な日本語の能動文へ変換するノウハウを解説します。",
        "theory": [
            ("イ日翻訳における脱・受動態化テクニック",
             "1. **前置代名詞受動構文（Pasif Persona） → 日本語能動態**:\n"
             "   - イ: \"Rencana ini **telah kami diskusikan** dengan pihak mitra.\"\n"
             "   - 拙訳: 「この計画は、私たちによって提携先と議論された。」\n"
             "   - 名訳: 「当社は、本計画について提携先と協議を重ねてまいりました。」\n"
             "2. **三人称受動構文（di-...） → 日本語の名詞述語・能動文**:\n"
             "   - イ: \"Pembangunan jembatan tersebut **diselesaikan** dalam waktu enam bulan.\"\n"
             "   - 拙訳: 「その橋の建設は6ヶ月の時間の中で完了された。」\n"
             "   - 名訳: 「同橋の建設工事は、わずか6ヶ月で完了しました。」\n"
             "3. **指示・要請の受動態（Diharapkan... / Dimohon...） → 丁寧な依頼能動文**:\n"
             "   - イ: \"Pengunjung **dilarang merokok** di area ini.\"\n"
             "   - 拙訳: 「来場者はこのエリアでタバコを吸うことを禁じられる。」\n"
             "   - 名訳: 「当エリア内での喫煙はご遠慮ください。」")
        ],
        "problems": [
            {
                "q": "【イ日受動態転換問題】\n\"Laporan pertanggungjawaban tahunan telah disetujui oleh seluruh pemegang saham dalam Rapat Umum Pemegang Saham (RUPS).\"\n最もプロフェッショナルで自然な日本語ビジネス訳はどれか？",
                "options": [
                    "A. 年次報告書は定時株主総会において全株主によって承認された。",
                    "B. 定時株主総会（RUPS）において、全株主が年次活動報告書を満場一致で承認いたしました。",
                    "C. 株主総会の中で全株主が年次報告書を承認した状態になった。",
                    "D. 年次責任報告書が株主総会で株主たちからオッケーをもらった。"
                ],
                "ans": "B. 定時株主総会（RUPS）において、全株主が年次活動報告書を満場一致で承認いたしました。",
                "expl": "受動態直訳の「全株主によって承認された」を排し、「全株主が〜を承認いたしました」と自然な能動文に再構成しているBがプロの実務翻訳基準を満たしています。"
            }
        ],
        "table": [
            ("Rapat Umum Pemegang Saham (RUPS)", "定時株主総会（Annual General Meeting of Shareholders）"),
            ("laporan pertanggungjawaban", "業務報告書・活動報告書・決算報告"),
            ("disetujui secara aklamasi", "満場一致で承認される"),
            ("pihak mitra", "提携先・パートナー企業"),
            ("dimohon dengan hormat", "何卒〜していただきますようお願い申し上げます"),
            ("dilarang keras", "固くお断りいたします・厳禁")
        ],
        "pro_tip": "日本語の公用文やビジネス報告では、「誰が何を承認した」「誰が何を決定した」という能動の骨格が最も明快で信頼感を与えます。受動態の「〜された」は可能な限り削ぎ落としましょう。"
    },
    {
        "filename": "06-modality-translation-hazuda-wake.md",
        "title": "1456. 【翻訳技法】日本語モダリティ「〜はずだ・〜わけだ・〜に違いない」の的確な訳出",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語の文末に現れるモダリティ（話し手の認識・判断）は、文脈によって極めて精緻な意味のグラデーションを持ちます。「〜はずだ（論理的当然・期待）」「〜わけだ（納得・必然の帰結）」「〜に違いない（強い推量・確信）」を、インドネシア語の助動詞・副詞（seharusnya, sudah sewajarnya, pasti, tentulah）へと過不足なく訳し分ける技術を学びます。",
        "theory": [
            ("日本語モダリティのインドネシア語対応チャート",
             "1. **「〜はずだ」（客観的根拠に基づく当然の期待・予定）**:\n"
             "   - 「書類は昨日届いたはずです。」 → Berkas itu **seharusnya sudah tiba** kemarin.\n"
             "   - 「彼は来ないはずがない（絶対に来る）。」 → Tidak mungkin dia tidak datang / **Pasti dia datang**.\n"
             "2. **「〜わけだ」（理由を知って納得する・論理的帰結）**:\n"
             "   - 「なるほど、それで電車が遅れたわけだ。」 → Pantas saja / **Wajarlah kalau keretanya terlambat**.\n"
             "   - 「つまり、契約は無効というわけですね。」 → Jadi artinya, perjanjian ini batal demi hukum.\n"
             "3. **「〜に違いない」（話し手の主観的な強い確信）**:\n"
             "   - 「この戦略は必ず成功するに違いない。」 → Strategi ini **pasti / niscaya akan berhasil**.\n"
             "   - 「犯人は内部の事情に詳しい人物に違いない。」 → Pelakunya **tentulah orang yang sangat memahami** seluk-beluk internal.")
        ],
        "problems": [
            {
                "q": "【モダリティ翻訳問題】「昨夜から激しい雨が降り続いていたのだから、川が氾濫したのも当然のわけだ。」のニュアンスを最も見事に再現したインドネシア語訳はどれか？",
                "options": [
                    "A. Mengingat hujan lebat mengguyur sejak tadi malam, sangatlah wajar jika sungai meluap.",
                    "B. Karena hujan deras kemarin malam, sungainya harus banjir.",
                    "C. Tadi malam hujan banyak, jadi sungai banjir itu harusnya begitu.",
                    "D. Kalau hujan lebat semalam, maka sungai meluap adalah pasti."
                ],
                "ans": "A. Mengingat hujan lebat mengguyur sejak tadi malam, sangatlah wajar jika sungai meluap.",
                "expl": "「〜なのだから（Mengingat...）」「当然のわけだ（sangatlah wajar jika...）」という納得・因果帰結のモダリティが格調高く表現されています。"
            }
        ],
        "table": [
            ("seharusnya sudah...", "〜したはずだ（当然の期待）"),
            ("pantas saja / wajarlah kalau...", "〜なのも納得のわけだ・道理だ"),
            ("tentulah...", "〜に違いない（強い推量・確信）"),
            ("niscaya...", "確実に〜する・必ずや〜となる（文語的確信）"),
            ("meluap", "氾濫する・あふれ出る（河川）"),
            ("seluk-beluk internal", "内部の事情・詳細な内情")
        ],
        "pro_tip": "「はずだ」を訳す際、単に pasti（確信）とするのではなく、期待や規範が未達である文脈では「seharusnya（〜すべき／〜のはず）」を用いるのが重要な識別ポイントです。"
    },
    {
        "filename": "07-benefactive-translation-kureru-morau.md",
        "title": "1457. 【翻訳技法】「〜てくれる・〜てもらう」受益表現の翻訳ストラテジー",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語の対人コミュニケーションの中核を成すのが「〜てくれる」「〜てあげる」「〜てもらう」という『授受・受益表現（Benefactive）』です。インドネシア語には日本語のような精緻な受益動詞体系が存在しないため、直訳しようとして「memberi」を乱用すると極めて幼稚な文になります。前置詞（untuk, bagi）、助動詞（bersedia, sudi）、あるいは受動態を活用して恩恵ニュアンスをエレガントに訳出する技法を習得します。",
        "theory": [
            ("受益表現のプロフェッショナル翻訳3大パターン",
             "1. **「〜てくれる」（相手の好意による行為） → bersedia / dengan senang hati / sudi**:\n"
             "   - 日: 「専門家が親切にアドバイスをしてくれた。」\n"
             "   - 直訳: *Ahli memberi nasihat untuk saya secara baik. (稚拙)\n"
             "   - 名訳: **Pakar tersebut bermurah hati memberikan masukan berharga kepada kami**.\n"
             "2. **「〜てもらう」（依頼して恩恵を受ける） → meminta / memohon / bantuan**:\n"
             "   - 日: 「弁護士に契約書を確認してもらった。」\n"
             "   - 直訳: *Saya dapat konfirmasi kontrak dari pengacara. (誤謬)\n"
             "   - 名訳: **Kami meminta pengacara untuk menelaah draf perjanjian tersebut** (または Draf perjanjian telah **ditelaah oleh pengacara kami**).\n"
             "3. **「〜てあげる」（相手への親切） → 動詞 + untuk / demi**:\n"
             "   - 日: 「同僚の仕事を手伝ってあげた。」\n"
             "   - 名訳: **Saya membantu rekan kerja menyelesaikan tugasnya** (untuk dia は不要).")
        ],
        "problems": [
            {
                "q": "【受益表現翻訳問題】「現地のパートナー企業が、工場用地の選定を快く手伝ってくれた。」の自然で洗練されたインドネシア語訳はどれか？",
                "options": [
                    "A. Mitra lokal dengan senang hati membantu kami dalam memilih lokasi lahan pabrik.",
                    "B. Teman lokal memberi tolong pada kita buat pilih tanah pabrik secara senang.",
                    "C. Perusahaan partner kasih bantuan kepada saya untuk cari tanah pabrik.",
                    "D. Kami dapat tolong dari teman lokal untuk pemilihan tanah pabrik."
                ],
                "ans": "A. Mitra lokal dengan senang hati membantu kami dalam memilih lokasi lahan pabrik.",
                "expl": "「快く〜してくれた」を「dengan senang hati membantu kami（喜んで私たちを助けてくれた）」と品格ある語彙で再現したAが正解です。"
            }
        ],
        "table": [
            ("dengan senang hati", "快く・喜んで（with pleasure）"),
            ("bermurah hati", "寛大にも・親切にも〜してくれる"),
            ("menelaah draf", "草案を精査・吟味する"),
            ("lahan pabrik", "工場用地・敷地"),
            ("masukan berharga", "貴重な意見・有益なアドバイス"),
            ("rekan kerja", "同僚・仕事仲間")
        ],
        "pro_tip": "インドネシア語では、動詞そのもの（membantu, mendukung, mendampingi）に既に「支援・恩恵」の意味が含まれているため、無理に「memberi」を重ねる必要はありません。"
    },
    {
        "filename": "08-causative-translation-saseru.md",
        "title": "1458. 【翻訳技法】日本語の使役「〜させる」と接辞 -kan/-i のニュアンス適合性",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語の使役助動詞「〜させる」には、「強制（〜させる）」「放任・許可（〜させておく／〜させてあげる）」「原因・誘発（〜という状態に至らせる）」という全く異なる意味合いが含まれます。インドネシア語でこれらをすべて「menyuruh」や「membuat」で訳すと重大なニュアンスの誤解を招きます。使役接辞（-kan）と使役動詞（membiarkan, menyuruh, mendorong, memicu）の精密な適合性を分析します。",
        "theory": [
            ("「〜させる」の4大ニュアンスと訳し分け",
             "1. **状態変化の使役（対象を〜な状態にする） → 接尾辞 -kan**:\n"
             "   - 「部屋を暖かくさせる（暖める）」 → **menghangatkan** ruangan.\n"
             "   - 「作業を容易にさせる（容易にする）」 → **memudahkan** pekerjaan.\n"
             "2. **強制・命令の使役（人に〜することを命じる） → menyuruh / mewajibkan / memerintahkan**:\n"
             "   - 「部下にレポートを再提出させた。」 → **memerintahkan / meminta bawahan** untuk menyerahkan ulang laporan.\n"
             "3. **許可・放任の使役（〜したいようにさせる） → membiarkan / mengizinkan**:\n"
             "   - 「子供たちを自由に遊ばせておく。」 → **membiarkan** anak-anak bermain dengan bebas.\n"
             "4. **原因・心理的誘発の使役（〜という感情を抱かせる） → membuat / memicu / membuahkan**:\n"
             "   - 「その決定は市民に失望をもたらさせた（失望させた）。」 → Keputusan tersebut **membuat masyarakat kecewa** (または **memicu kekecewaan publik**).")
        ],
        "problems": [
            {
                "q": "【使役識別演習】「政府の急な方針転換が、市場に混乱を生じさせた。」の翻訳として最も格調高いものはどれか？",
                "options": [
                    "A. Perubahan kebijakan pemerintah yang mendadak memicu kekacauan pasar.",
                    "B. Pemerintah ganti aturan cepat bikin pasar jadi bingung.",
                    "C. Kebijakan pemerintah suruh pasar bikin ribut.",
                    "D. Perubahan aturan membiarkan pasar jadi kacau balau."
                ],
                "ans": "A. Perubahan kebijakan pemerintah yang mendadak memicu kekacauan pasar.",
                "expl": "原因・誘発の使役「〜を生じさせた・引き起こした」には、動詞「memicu（引き金を引く→引き起こす）」または「menimbulkan」を用いるAが完璧な経済公用文です。"
            }
        ],
        "table": [
            ("memicu kekacauan", "混乱を引き起こす・生じさせる（誘発）"),
            ("memudahkan proses", "プロセスを円滑化・容易にする（状態化 -kan）"),
            ("mengizinkan akses", "アクセスを許可する・認めさせる（許可）"),
            ("mewajibkan karyawan", "従業員に義務付ける（強制）"),
            ("membiarkan berkembang", "自然に発展させる・放任する（放任）"),
            ("kekecewaan publik", "世論・市民の失望")
        ],
        "pro_tip": "学術論文やビジネス報告では、「membuat（作る）」という汎用動詞を避け、「mendorong（促進させる）」「memicu（引き起こす）」「mengakibatkan（結果を生じさせる）」などの因果動詞を使うと文章の格調が一気に跳ね上がります。"
    },
    {
        "filename": "09-inanimate-subject-translation.md",
        "title": "1459. 【翻訳技法】無生物主語構文の処理法：主客転換と因果関係の再構成",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "インドネシア語や英語の学術・報道記事では「Penelitian ini membuktikan...（この研究は〜を証明している）」「Kecelakaan tersebut menewaskan...（その事故は〜人を死に至らしめた）」といった無生物主語構文（Inanimate Subject）が頻出します。しかし、日本語では事物を主語として人間のような動作をさせる表現は不自然です。日本語への翻訳において主客転換（因果構文・手段構文への変換）を行うプロの技法を学びます。",
        "theory": [
            ("無生物主語の日本語への構造転換 3大パターン",
             "1. **「研究・調査が〜を示している」 → 「〜によると／〜を通じて判明した」**:\n"
             "   - イ: \"Survei ini mengindikasikan bahwa kepuasan pelanggan menurun.\"\n"
             "   - 拙訳: 「この調査は、顧客満足度が低下していることを示している。」\n"
             "   - 名訳: 「**今回の調査結果によると**、顧客満足度の低下が明らかになりました。」\n"
             "2. **「事故・災害が〜を死亡させた」 → 「〜により、〜人が死亡した」**:\n"
             "   - イ: \"Bencana tanah longsor tersebut menewaskan lima warga.\"\n"
             "   - 拙訳: 「その土砂崩れ災害は5人の住民を死亡させた。」\n"
             "   - 名訳: 「**同土砂崩れ災害により**、住民5名が命を落としました。」\n"
             "3. **「テクノロジーが〜を可能にする」 → 「〜のおかげで、〜できるようになった」**:\n"
             "   - イ: \"Aplikasi ini memungkinkan pengguna untuk mentransfer uang secara instan.\"\n"
             "   - 拙訳: 「このアプリはユーザーが瞬時に送金することを可能にする。」\n"
             "   - 名訳: 「**本アプリを利用することで**、利用者は即時送金が可能となります。」")
        ],
        "problems": [
            {
                "q": "【無生物主語の転換問題】\n\"Laporan Bank Dunia memperingatkan bahwa kenaikan suku bunga global akan memperlambat pertumbuhan ekonomi negara berkembang.\"\n最も自然な日本語の報道文はどれか？",
                "options": [
                    "A. 世界銀行の報告書は、世界的な金利上昇が途上国の経済成長を減速させると警告している。",
                    "B. 世界銀行が発表した最新報告書によると、世界的な金利上昇に伴い、途上国の経済成長が減速する恐れがあると警鐘を鳴らしています。",
                    "C. 世界銀行の書類は、世界の金利が上がって途上国の成長が遅くなると注意した。",
                    "D. 世界銀行レポートは途上国の成長遅延を世界金利上昇によって警告させた。"
                ],
                "ans": "B. 世界銀行が発表した最新報告書によると、世界的な金利上昇に伴い、途上国の経済成長が減速する恐れがあると警鐘を鳴らしています。",
                "expl": "「報告書によると（手段・根拠）」＋「金利上昇に伴い（原因）」＋「減速する恐れがあると警鐘を鳴らしている（客観報道）」と見事に日本語の報道文体へ再構成されているBが卓越した名訳です。"
            }
        ],
        "table": [
            ("memungkinkan pengguna", "利用者が〜できるようにする（可能構文）"),
            ("menewaskan korban", "犠牲者の命を奪う・死に至らしめる"),
            ("memperingatkan bahwa...", "〜であると警告を発する・警鐘を鳴らす"),
            ("tanah longsor", "土砂崩れ・地すべり"),
            ("memperlambat pertumbuhan", "成長を減速・鈍化させる"),
            ("negara berkembang", "発展途上国・新興国")
        ],
        "pro_tip": "無生物主語の文を見たら、主語を「〜によって」「〜のおかげで」「〜によると」という副詞句（原因・理由・手段）に置き換えるだけで、日本語の文章の硬さが一瞬で消え去ります。"
    },
    {
        "filename": "10-onomatopoeia-translation-techniques.md",
        "title": "1460. 【翻訳技法】日本語オノマトペ・擬音語擬態語のインドネシア語描写技法",
        "level": "実務翻訳者・上級学習者（CEFR B2〜C1）",
        "intro": "日本語には4,000語以上ものオノマトペ（擬音語・擬態語）が存在し、感情、触覚、動作の機微を鮮やかに表現します（ドキドキ、キラキラ、サクサク、イライラなど）。インドネシア語には同等の一対一対応語が存在しないことが多いため、プロの翻訳者は「具体的な動詞」「副詞的描写句」「比喩表現」を駆使して情景を生き生きと描き出します。オノマトペ翻訳の極意を伝授します。",
        "theory": [
            ("日本語オノマトペのインドネシア語パラフレーズ技術",
             "1. **感情・心理オノマトペ**: \n"
             "   - 「ドキドキする（緊張・不安）」 → **berdebar-debar** / jantung berdegup kencang\n"
             "   - 「イライラする」 → **kesal** / merasa jengkel / naik darah\n"
             "   - 「ワクワクする」 → **sangat bersemangat** / tak sabar menantikan\n"
             "   - 「ホッとする」 → **merasa lega**\n"
             "2. **状態・質感オノマトペ**: \n"
             "   - 「キラキラ輝く」 → **berkilauan** / gemerlap\n"
             "   - 「サクサクした食感」 → tekstur yang **renyah** (krispi)\n"
             "   - 「モチモチした食感」 → tekstur yang **kenyal**\n"
             "   - 「ツルツルした肌」 → kulit yang **halus mulus**\n"
             "3. **動作・進捗オノマトペ**: \n"
             "   - 「仕事がサクサク進む」 → pekerjaan **berjalan lancar tanpa hambatan**\n"
             "   - 「ウロウロ歩き回る」 → **berjalan mondar-mandir** tanpa tujuan")
        ],
        "problems": [
            {
                "q": "【オノマトペ翻訳問題】「面接の順番を待つ間、心臓がドキドキして手が汗でびっしょりになった。」の最も文学的・情景描写として優れたインドネシア語訳はどれか？",
                "options": [
                    "A. Saat menunggu giliran wawancara, jantung saya berdegup kencang dan telapak tangan saya basah oleh keringat.",
                    "B. Waktu tunggu giliran wawancara, hati saya doki-doki dan tangan penuh air.",
                    "C. Pas antre wawancara, jantung saya bunyi keras sekali dan tangan saya basah kuyup.",
                    "D. Ketika nunggu wawancara, saya berdebar dan tangan keluar banyak keringat."
                ],
                "ans": "A. Saat menunggu giliran wawancara, jantung saya berdegup kencang dan telapak tangan saya basah oleh keringat.",
                "expl": "「ドキドキする → jantung berdegup kencang」「びっしょり → basah oleh keringat」と、オノマトペの感覚を生理的・身体的描写へ精密に翻訳しているAが正解です。"
            }
        ],
        "table": [
            ("jantung berdegup kencang", "心臓がドキドキ・激しく鼓動する"),
            ("merasa lega", "ホッとする・胸をなでおろす"),
            ("renyah / krispi", "サクサク・カリカリした（食感）"),
            ("kenyal", "モチモチ・弾力のある（食感）"),
            ("halus mulus", "ツルツル・スベスベした（肌触り）"),
            ("mondar-mandir", "ウロウロ・行ったり来たりする")
        ],
        "pro_tip": "オノマトペを訳すときは、「音」を訳そうとせず、「その時、身体や心や物がどんな状態にあるのか」という『現象の本質』にフォーカスして描写語を選ぶのがプロのコツです。"
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
    table_header = "| 日本語表現・概念 | インドネシア語対応表現 | ニュアンス・用法解説 |\n| :--- | :--- | :--- |\n"
    for row in a["table"]:
        table_rows += f"| **{row[0]}** | **{row[1]}** | {row[1]} |\n" if len(row) == 2 else f"| **{row[0]}** | {row[1]} |\n"

    # Fix table format for 2 items
    table_rows = ""
    table_header = "| 表現・項目 | 解説・対応用法 |\n| :--- | :--- |\n"
    for row in a["table"]:
        table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "プロの翻訳・通訳・高度表現テクニック。{a['title']}の言語対照分析、プロの翻訳ストラテジー、実戦比較演習まで徹底指導。"
---

<div class="category-badge">プロフェッショナル翻訳・表現技法</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 言語対照分析と翻訳の課題

{a['intro']}

---

## 2. プロの翻訳ストラテジー・変換フレームワーク

{theory_content}
---

## 3. 実戦翻訳比較演習

直訳の不自然さを解消し、プロの自然な訳文へ昇華させる実戦演習です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要構文・表現対比テーブル

本講のテーマに関連する重要構文・定型表現一覧です。

{table_header}{table_rows}
---

## 5. プロ翻訳者の着眼点・ワンポイントアドバイス

> [!TIP]
> **名訳を生み出すワンポイント・アドバイス**:
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
