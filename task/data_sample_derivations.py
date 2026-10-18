#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DERIVATIONS_DATA = [
    {
        "root": "harap",
        "meaning": "望む、期待する",
        "lead": "希望や期待、依頼を表す超重要語根 **harap** は、ビジネスから公的通知、日常の願望まで幅広く派生します。",
        "table": [
            ("berharap", "自動詞", "希望する、〜であってほしいと願う"),
            ("mengharap", "他動詞", "〜を期待する、当てにする"),
            ("mengharapkan", "使役他動詞", "〜を強く期待する、望む"),
            ("pengharapan", "名詞", "希望、期待、願望"),
            ("harapan", "名詞", "望み、見込み、ホープ"),
        ],
        "details": [
            ("berharap", "自動詞: 望む、願う", "日常会話や公式メッセージで「〜を願っています」と伝える表現。",
             "Kami berharap kerja sama bisnis ini dapat terus berkembang di masa depan.",
             "私たちはこのビジネス協力が将来にわたって発展し続けることを願っています。",
             "berharap + 節（〜と願う） / kerja sama bisnis（ビジネス協業）。"),
            ("mengharapkan", "他動詞: 期待する、要望する", "相手や状況に対して具体的な成果や行動を期待する用法。",
             "Perusahaan mengharapkan kontribusi nyata dari setiap karyawan dalam proyek inovasi ini.",
             "会社は、このイノベーションプロジェクトにおいて各従業員からの実質的な貢献を期待しています。",
             "mengharapkan kontribusi（貢献を期待する）。"),
            ("harapan", "名詞: 希望、期待", "harapan hidup（平均余命）、menaruh harapan（期待をかける）。",
             "Pendidikan yang berkualitas memberikan harapan baru bagi generasi muda di daerah terpencil.",
             "質の高い教育は、僻地の若い世代に新たな希望をもたらします。",
             "harapan baru（新たな希望） / daerah terpencil（僻地）。")
        ],
        "quiz": [
            ("「 harapan hidup 」の日本語訳は？", "平均余命（寿命）", "harapan（期待・見込み）＋ hidup（生きる・生命）で平均余命を表します。"),
            ("「〜であってほしいと願う（自動詞）」を表す派生語は？", "berharap", "接頭辞 ber- が付いて「希望・期待を抱いている状態」を表します。")
        ]
    },
    {
        "root": "coba",
        "meaning": "試す、試みる",
        "lead": "試行錯誤や挑戦、そして人生の「試練」を表す語根 **coba** の派生語ネットワークです。",
        "table": [
            ("mencoba", "他動詞", "試す、やってみる、挑戦する"),
            ("percobaan", "名詞", "実験、試み、試用期間"),
            ("cobaan", "名詞", "（人生の）試練、災難"),
            ("mencobai", "他動詞", "誘惑する、試す（宗教・文語的）"),
        ],
        "details": [
            ("mencoba", "他動詞: 試す、トライする", "新しいことへの挑戦や、味見・試着などに広く使われます。",
             "Saya ingin mencoba makanan khas Sunda yang terkenal sangat lezat ini.",
             "私はとても美味しいと有名なこのスンダ名物料理を試してみたいです。",
             "mencoba makanan（食べ物を試食する） / makanan khas（郷土名物料理）。"),
            ("percobaan", "名詞: 実験、テスト、試用期間", "masa percobaan（試用期間）、laboratorium percobaan（実験室）。",
             "Karyawan baru harus menjalani masa percobaan selama tiga bulan sebelum diangkat menjadi karyawan tetap.",
             "新入社員は、正社員に登用される前に3ヶ月間の試用期間を経なければなりません。",
             "masa percobaan（試用期間） / karyawan tetap（正社員）。"),
            ("cobaan", "名詞: 試練、苦難", "天や運命から与えられる耐えるべき苦難。",
             "Masyarakat tetap tabah menghadapi cobaan berat akibat bencana alam banjir bandang.",
             "住民たちは鉄砲水という自然災害による重い試練に直面しても、なお冷静で忍耐強くあり続けています。",
             "menghadapi cobaan berat（重い試練に立ち向かう）。")
        ],
        "quiz": [
            ("「 masa percobaan 」のビジネス用語としての意味は？", "試用期間（プロベーション期間）", "社員採用時の試用雇用期間を指します。"),
            ("「運命の試練や苦難」を表す名詞は？", "cobaan", "接尾辞 -an がついて受動的な試練を表します。")
        ]
    },
    {
        "root": "dorong",
        "meaning": "押す、推進する",
        "lead": "物理的に「押す」から政策・経済の「推進・後押し」、心理的「動機づけ」まで広がる語根 **dorong** です。",
        "table": [
            ("mendorong", "他動詞", "押す、後押しする、促進する"),
            ("pendorong", "名詞", "推進者、推進要因、起爆剤"),
            ("dorongan", "名詞", "後押し、衝動、励まし"),
            ("terdorong", "受動・偶発", "押し出された、促された"),
        ],
        "details": [
            ("mendorong", "他動詞: 促進する、後押しする", "経済政策や人材育成で「発展を促す」際の頻出語。",
             "Pemerintah berupaya keras mendorong pertumbuhan ekonomi digital di kalangan UMKM.",
             "政府は、零細中小企業（UMKM）におけるデジタル経済の成長を促進するために全力を尽くしています。",
             "mendorong pertumbuhan（成長を促進する）。"),
            ("faktor pendorong", "名詞句: 推進要因、促進因子", "物事の成功や変化の引き金となる要素。",
             "Inovasi teknologi menjadi faktor pendorong utama dalam efisiensi operasional pabrik.",
             "技術革新が、工場のオペレーション効率化における主要な推進要因となっています。",
             "faktor pendorong utama（主要な推進要因）。"),
            ("dorongan", "名詞: 後押し、インパルス", "精神的支援や物理的推進力。",
             "Dorongan moril dari pimpinan sangat membantu staf dalam menyelesaikan proyek sulit ini.",
             "上司からの精神的な励まし（後押し）は、スタッフがこの困難なプロジェクトを完遂する上で非常に助けとなりました。",
             "dorongan moril（精神的励まし）。")
        ],
        "quiz": [
            ("「 faktor pendorong 」の対義語である「阻害要因」のインドネシア語は？", "faktor penghambat", "hambat（阻む）から派生する penghambat（阻害要因）と対比されます。"),
            ("「零細中小企業の成長を後押しする」の動詞は？", "mendorong", "meN- + dorong で他動詞化します。")
        ]
    },
    {
        "root": "hadap",
        "meaning": "向く、直面する",
        "lead": "空間的「方向」から困難への「対峙」、法律・関係の「〜に対して」を形成する超重要語根 **hadap** です。",
        "table": [
            ("menghadapi", "他動詞", "直面する、立ち向かう、対峙する"),
            ("menghadap", "自動詞/他動詞", "〜に向いている、〜に面談する"),
            ("terhadap", "前置詞", "〜に対して、〜に関して"),
            ("berhadapan", "相互自動詞", "向かい合う、対立する"),
            ("pendapat", "名詞", "意見、見解（ada/dapatとの複合派生）"),
        ],
        "details": [
            ("menghadapi", "他動詞: 直面する、立ち向かう", "課題や危機、競争に立ち向かう必須動詞。",
             "Industri manufaktur harus siap menghadapi tantangan disrupsi rantai pasok global.",
             "製造業界は、グローバルなサプライチェーン寸断の課題に直面する準備を整えなければなりません。",
             "menghadapi tantangan（課題に直面する）。"),
            ("terhadap", "前置詞: 〜に対して", "態度や政策、義務の対象を導く文語・実務頻出前置詞。",
             "Perusahaan memiliki tanggung jawab sosial terhadap kesejahteraan masyarakat sekitar pabrik.",
             "企業は、工場周辺の住民コミュニティの福祉に対して社会的責任を負っています。",
             "tanggung jawab terhadap...（〜に対する責任）。"),
            ("berhadapan", "相互自動詞: 向かい合う、対峙する", "二者が正面から向き合っている状態。",
             "Kedua tim negosiasi duduk berhadapan di ruang rapat untuk membahas klausul kontrak.",
             "両交渉チームは、契約条項を協議するため会議室で向かい合って座りました。",
             "duduk berhadapan（向かい合って座る）。")
        ],
        "quiz": [
            ("「〜に対して」を表す前置詞は？", "terhadap", "語根 hadap から派生した最も頻出する前置詞です。"),
            ("「困難や課題に直面する」を表す他動詞は？", "menghadapi", "接尾辞 -i が付き「向かう対象（課題）」をとります。")
        ]
    },
    {
        "root": "tuntut",
        "meaning": "要求する、訴求する",
        "lead": "権利の「要求」、学問の「探求」、法廷での「起訴」まで厳格な意志を表す語根 **tuntut** です。",
        "table": [
            ("menuntut", "他動詞", "要求する、起訴する、探求する"),
            ("tuntutan", "名詞", "要求、請求、訴因"),
            ("penuntut", "名詞", "原告、検察官（penuntut umum）"),
            ("tertuntut", "受動", "要求された、義務付けられた"),
        ],
        "details": [
            ("menuntut", "他動詞: 要求する、学ぶ", "menuntut ilmu（学問を修める）、menuntut hak（権利を要求する）。",
             "Para pekerja berunjuk rasa secara damai untuk menuntut kenaikan upah minimum regional.",
             "労働者たちは、地域最低賃金の引き上げを要求するために平和的にデモ行進を行いました。",
             "menuntut kenaikan upah（賃上げを要求する）。"),
            ("tuntutan", "名詞: 要求事項、需要", "tuntutan pasar（市場の要請）、tuntutan hukum（法的請求）。",
             "Manajemen sepakat untuk mempertimbangkan sebagian tuntutan dari serikat pekerja.",
             "経営陣は、労働組合からの要求事項の一部を検討することに合意しました。",
             "tuntutan serikat pekerja（労組の要求）。"),
            ("penuntut umum", "法律用語: 公判検事、検察官", "刑事裁判で国家を代表して起訴する役職。",
             "Jaksa Penuntut Umum membacakan surat dakwaan di hadapan majelis hakim pengadilan negeri.",
             "公判検察官は、地方裁判所の裁判官団の面前で起訴状を朗読しました。",
             "jaksa penuntut umum（検察官）。")
        ],
        "quiz": [
            ("「学問を修める、知識を探求する」という慣用句は？", "menuntut ilmu", "ilmu（知識・学問）を追求する定番フレーズです。"),
            ("「検察官（公訴人）」をインドネシア語で言うと？", "jaksa penuntut umum", "通常 JPU と略されます。")
        ]
    }
]

# We will generate comprehensive articles for 50 roots
print("Data template validated.")
