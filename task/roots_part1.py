#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Root Derivations Phase 2 (50 files)
Docs location: docs/derivations/root-<name>.md
Follows strict guidelines:
- Accessible markdown tables (no mermaid)
- Bold syntax inside brackets: 「**text**」
- Rich examples with .id-example
- No furigana/rubi
"""

import os

ROOTS = [
    ("harap", "望む、期待する", "希望・期待や依頼を表す最重要語根", [
        ("berharap", "自動詞", "希望する、〜であってほしいと願う"),
        ("mengharap", "他動詞", "〜を期待する、当てにする"),
        ("mengharapkan", "使役他動詞", "〜を強く期待する、要望する"),
        ("pengharapan", "名詞", "希望、期待、願望"),
        ("harapan", "名詞", "望み、期待、ホープ"),
    ], [
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
    ], [
        ("「 harapan hidup 」の日本語訳は？", "平均余命（寿命）", "harapan（期待・見込み）＋ hidup（生きる・生命）で平均余命を表します。"),
        ("「〜であってほしいと願う（自動詞）」を表す派生語は？", "berharap", "接頭辞 ber- が付いて「希望・期待を抱いている状態」を表します。")
    ]),

    ("coba", "試す、試みる", "試行錯誤や挑戦、そして人生の「試練」を表す語根", [
        ("mencoba", "他動詞", "試す、やってみる、挑戦する"),
        ("percobaan", "名詞", "実験、試み、試用期間"),
        ("cobaan", "名詞", "（人生の）試練、災難"),
        ("mencobai", "他動詞", "誘惑する、試す（宗教・文語的）"),
    ], [
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
    ], [
        ("「 masa percobaan 」のビジネス用語としての意味は？", "試用期間（プロベーション期間）", "社員採用時の試用雇用期間を指します。"),
        ("「運命の試練や苦難」を表す名詞は？", "cobaan", "接尾辞 -an がついて受動的な試練を表します。")
    ]),

    ("dorong", "押す、推進する", "物理的に「押す」から政策・経済の「推進・後押し」まで広がる語根", [
        ("mendorong", "他動詞", "押す、後押しする、促進する"),
        ("pendorong", "名詞", "推進者、推進要因、起爆剤"),
        ("dorongan", "名詞", "後押し、衝動、励まし"),
        ("terdorong", "受動・偶発", "押し出された、促された"),
    ], [
        ("mendorong", "他動詞: 促進する、後押しする", "経済政策や人材育成で「発展を促す」際の頻出語。",
         "Pemerintah berupaya keras mendorong pertumbuhan ekonomi digital di kalangan UMKM.",
         "政府は、零細中小企業（UMKM）におけるデジタル経済の成長を促進するために全力を尽くしています。",
         "mendorong pertumbuhan（成長を促進する）。"),
        ("pendorong", "名詞: 推進要因、促進因子", "faktor pendorong（推進要因）。物事の成功の引き金。",
         "Inovasi teknologi menjadi faktor pendorong utama dalam efisiensi operasional pabrik.",
         "技術革新が、工場のオペレーション効率化における主要な推進要因となっています。",
         "faktor pendorong utama（主要な推進要因）。"),
        ("dorongan", "名詞: 後押し、励まし", "精神的支援や物理的推進力。",
         "Dorongan moril dari pimpinan sangat membantu staf dalam menyelesaikan proyek sulit ini.",
         "上司からの精神的な励まし（後押し）は、スタッフがこの困難なプロジェクトを完遂する上で非常に助けとなりました。",
         "dorongan moril（精神的励まし）。")
    ], [
        ("「 faktor pendorong 」の対義語である「阻害要因」のインドネシア語は？", "faktor penghambat", "hambat（阻む）から派生する penghambat（阻害要因）と対比されます。"),
        ("「零細中小企業の成長を後押しする」の動詞は？", "mendorong", "meN- + dorong で他動詞化します。")
    ]),

    ("hadap", "向く、直面する", "空間的方向から困難への「対峙」、法律関係の「〜に対して」を形成する語根", [
        ("menghadapi", "他動詞", "直面する、立ち向かう、対峙する"),
        ("menghadap", "自動詞/他動詞", "〜に向いている、〜に面談する"),
        ("terhadap", "前置詞", "〜に対して、〜に関して"),
        ("berhadapan", "相互自動詞", "向かい合う、対立する"),
        ("pendapat", "名詞", "意見、見解（ada/dapatとの複合派生）"),
    ], [
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
    ], [
        ("「〜に対して」を表す前置詞は？", "terhadap", "語根 hadap から派生した最も頻出する前置詞です。"),
        ("「困難や課題に直面する」を表す他動詞は？", "menghadapi", "接尾辞 -i が付き「向かう対象（課題）」をとります。")
    ]),

    ("tuntut", "要求する、訴求する", "権利の要求、学問の探求、法廷での起訴まで厳格な意志を表す語根", [
        ("menuntut", "他動詞", "要求する、起訴する、探求する"),
        ("tuntutan", "名詞", "要求、請求、訴因"),
        ("penuntut", "名詞", "原告、検察官（penuntut umum）"),
        ("tertuntut", "受動", "要求された、義務付けられた"),
    ], [
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
    ], [
        ("「学問を修める、知識を探求する」という慣用句は？", "menuntut ilmu", "ilmu（知識・学問）を追求する定番フレーズです。"),
        ("「検察官（公訴人）」をインドネシア語で言うと？", "jaksa penuntut umum", "通常 JPU と略されます。")
    ]),

    ("sebar", "広める、散布する", "情報の拡散から病気の流行、製品の流通網まで「広がり」を表す語根", [
        ("menyebar", "自動詞", "広がる、拡散する、散らばる"),
        ("menyebarkan", "使役他動詞", "広める、配布する、宣伝する"),
        ("tersebar", "受動・完了", "広まった、点在している"),
        ("penyebaran", "名詞", "拡散、配布、伝播"),
        ("persebaran", "名詞", "分布、配置状況"),
    ], [
        ("menyebarkan", "使役他動詞: 拡散する、広める", "情報やチラシ、ニュースを世間に広める動詞。",
         "Masyarakat dihimbau tidak menyebarkan berita bohong atau hoaks di media sosial.",
         "市民はソーシャルメディア上で虚偽ニュース（デマ・フェイクニュース）を拡散しないよう呼びかけられています。",
         "menyebarkan hoaks（デマを拡散する）。"),
        ("persebaran", "名詞: 地理的分布", "persebaran penduduk（人口分布）。地理や統計の基本語。",
         "Pemerintah berfokus pada pemerataan persebaran penduduk melalui program pembangunan luar Jawa.",
         "政府は、ジャワ島外の開発プログラムを通じて人口分布の均等化に注力しています。",
         "persebaran penduduk（人口分布）。"),
        ("tersebar", "形容詞/受動: 各地に点在する", "全国や広範囲に散らばっている様子。",
         "Kantor cabang bank ini telah tersebar luas di seluruh kota besar di Indonesia.",
         "この銀行の支店網は、すでにインドネシア全土の主要都市に広く展開（点在）しています。",
         "tersebar luas（広く点在している）。")
    ], [
        ("「フェイクニュースを拡散する」のインドネシア語は？", "menyebarkan hoaks", "sebar の使役他動詞 menyebarkan を使います。"),
        ("「人口分布」を表す名詞句は？", "persebaran penduduk", "per-...-an により地理的配置・広がりを表します。")
    ]),

    ("tentu", "定まる、確実な", "方針の決定から法的規則、確信の表現まで日常・実務に不可欠な語根", [
        ("menentukan", "他動詞", "決定する、定める、左右する"),
        ("tertentu", "形容詞的受動", "特定の、一定の"),
        ("ketentuan", "名詞", "規定、条項、条件"),
        ("penentuan", "名詞", "決定プロセス、策定"),
        ("tentunya", "副詞", "もちろん、当然のことながら"),
    ], [
        ("menentukan", "他動詞: 決定する、左右する", "方針や価格、合否を定める必須語。",
         "Kualitas pelayanan dan reputasi merek sangat menentukan loyalitas pelanggan.",
         "サービスの質とブランドの評判は、顧客のロイヤルティを大きく左右（決定）します。",
         "menentukan loyalitas（忠誠度を左右する）。"),
        ("ketentuan", "名詞: 規定、規約、条件", "ketentuan hukum（法的規定）、syarat dan ketentuan（利用規約）。",
         "Semua pihak wajib mematuhi ketentuan yang tercantum dalam perjanjian kerja bersama.",
         "すべての当事者は、労働協約に記載されている諸規定を遵守する義務があります。",
         "mematuhi ketentuan（規定を遵守する）。"),
        ("tertentu", "形容詞: 特定の", "pada waktu tertentu（特定の時間に）、kelompok tertentu（特定のグループ）。",
         "Fasilitas pembebasan bea masuk hanya diberikan untuk impor mesin industri tertentu.",
         "輸入関税の免除措置は、特定の産業機械の輸入に対してのみ付与されます。",
         "industri tertentu（特定の産業）。")
    ], [
        ("「利用規約」をインドネシア語で言うと？", "syarat dan ketentuan", "Webサイトや契約で必ず目にする定番表現（Terms & Conditions）です。"),
        ("「特定の条件」を表す表現は？", "syarat tertentu", "ter- + tentu で「定められた・特定の」を意味します。")
    ]),

    ("tuju", "向かう、意図する", "物理的な移動の目的地から、人生の目標、合意（同意）まで幅広く派生する語根", [
        ("menuju", "他動詞/前置詞", "〜に向かう、〜を目指す"),
        ("bertujuan", "自動詞", "〜を目的とする、目指している"),
        ("tujuan", "名詞", "目的、目標、目的地"),
        ("setuju", "形容詞/動詞", "同意する、賛成する"),
        ("persetujuan", "名詞", "合意、承認、許可"),
    ], [
        ("tujuan", "名詞: 目的、目標", "tujuan wisata（観光地）、tujuan utama（主目的）。",
         "Tujuan utama dari transformasi digital ini adalah meningkatkan efisiensi dan kepuasan pelanggan.",
         "このデジタルトランスフォーメーションの主たる目的は、効率性と顧客満足度を高めることです。",
         "tujuan utama（主たる目的）。"),
        ("menuju", "動詞: 〜へ向かう", "kereta menuju Bandung（バンドン行き列車）。",
         "Indonesia melangkah mantap menuju status negara maju pada tahun 2045.",
         "インドネシアは、2045年に向け先進国の地位を目指して力強く歩みを進めています。",
         "menuju status negara maju（先進国の地位へ向かう）。"),
        ("persetujuan", "名詞: 承認、合意書", "surat persetujuan（承諾書）、meminta persetujuan（承認を求める）。",
         "Proyek pembangunan pabrik baru masih menunggu persetujuan analisis dampak lingkungan.",
         "新工場建設計画は、今なお環境影響評価（AMDAL）の承認を待っている状態です。",
         "menunggu persetujuan（承認を待つ）。")
    ], [
        ("「同意する、賛成する」の最も一般的な日常語は？", "setuju", "se-（同一の）＋ tuju（向く先・意図）で「同じ方向を向く＝同意する」となります。"),
        ("「目的地」を表す名詞句は？", "tempat tujuan", "tujuan 単体でも「目的・目的地」を表します。")
    ]),

    ("tolak", "拒否する、退ける", "提案の拒絶から出発点、押し返す動作までを表す語根", [
        ("menolak", "他動詞", "拒否する、断る、却下する"),
        ("penolakan", "名詞", "拒絶、却下、否認"),
        ("tertolak", "受動", "却下された、断られた"),
        ("bertolak", "自動詞", "（船や旅が）出発する、〜を出発点とする"),
        ("bertolak belakang", "熟語", "正反対である、矛盾する"),
    ], [
        ("menolak", "他動詞: 断る、拒否する", "ビジネスでの申し出辞退や提案の却下。",
         "Manajemen terpaksa menolak proposal kerja sama tersebut karena tidak sesuai dengan visi perusahaan.",
         "経営陣は、会社のビジョンに合致しないため、その提携提案を断らざるを得ませんでした。",
         "menolak proposal（提案を断る）。"),
        ("penolakan", "名詞: 拒絶、不承認通知", "surat penolakan（却下通知書）。",
         "Alasan penolakan visa harus disampaikan secara transparan kepada pemohon.",
         "ビザ却下の理由は、申請者に対して透明性をもって説明されなければなりません。",
         "alasan penolakan（却下の理由）。"),
        ("bertolak belakang", "成句: 正反対である", "意見や性格が180度異なる様子。",
         "Kebijakan baru ini dinilai bertolak belakang dengan komitmen pelestarian hutan tropis.",
         "この新政策は、熱帯雨林保全のコミットメントと正反対（矛盾している）と評価されています。",
         "bertolak belakang dengan...（〜と正反対である）。")
    ], [
        ("「正反対である、矛盾する」を表す重要成句は？", "bertolak belakang", "背中（belakang）を向け合って出発することから「正反対」を意味します。"),
        ("「提案を拒絶・却下する」の動詞は？", "menolak", "meN- + tolak で「拒否する」となります。")
    ]),

    ("tanggung", "責任を負う、引き受ける", "義務や責任、費用の負担、保証を語る上で欠かせない語根", [
        ("menanggung", "他動詞", "負担する、被る、保証する"),
        ("tanggung jawab", "熟語名詞", "責任、責務"),
        ("bertanggung jawab", "複合動詞", "責任を負う、担当する"),
        ("pertanggungjawaban", "名詞", "説明責任、決算報告、責任追及"),
        ("tanggungan", "名詞", "扶養家族、借金などの負担"),
    ], [
        ("bertanggung jawab", "動詞: 責任を持つ", "役職や職責を説明する際の最頻出表現。",
         "Manajer operasional bertanggung jawab penuh atas kelancaran proses produksi harian.",
         "オペレーションマネージャーは、日々の生産プロセスの円滑な進行に対して全責任を負っています。",
         "bertanggung jawab atas...（〜に対して責任を負う）。"),
        ("menanggung", "他動詞: 負担する、保証する", "menanggung biaya（費用を負担する）、menanggung kerugian（損失を被る）。",
         "Pihak asuransi akan menanggung seluruh biaya pengobatan rawat inap karyawan.",
         "保険会社が、従業員の入院治療費全額を負担（補償）します。",
         "menanggung biaya（費用を負担する）。"),
        ("pertanggungjawaban", "名詞: 説明責任、報告書", "laporan pertanggungjawaban（業務・決算報告書、通称LPJ）。",
         "Ketua panitia harus menyampaikan laporan pertanggungjawaban dalam rapat evaluasi akhir.",
         "委員会代表は、最終評価ミーティングにおいて活動・決算報告（LPJ）を提出しなければなりません。",
         "laporan pertanggungjawaban（LPJ：活動報告・説明責任書）。")
    ], [
        ("インドネシアの組織で頻出する「LPJ（活動・決算報告書）」のフルスペルは？", "Laporan Pertanggungjawaban", "組織運営やイベントで必須の公式報告書です。"),
        ("「費用を負担する」をインドネシア語で言うと？", "menanggung biaya", "menanggung が「引き受ける・負担する」を表します。")
    ])
]

print(f"Loaded {len(ROOTS)} primary root definitions.")
