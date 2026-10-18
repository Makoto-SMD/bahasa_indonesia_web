#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comprehensive batch builder for 50 root derivations (Phase 2).
Generates docs/derivations/root-<name>.md
"""

import os

ROOT_DATA = [
    # 1-10
    ("harap", "望む、期待する", "希望・期待や依頼を表す最重要語根", [
        ("berharap", "自動詞", "希望する、〜であってほしいと願う"),
        ("mengharap", "他動詞", "〜を期待する、当てにする"),
        ("mengharapkan", "使役他動詞", "〜を強く期待する、要望する"),
        ("pengharapan", "名詞", "希望、期待、願望"),
        ("harapan", "名詞", "望み、期待、ホープ"),
    ], "berharap + 節で「〜と願う」、harapan hidup で「平均寿命」を表します。"),

    ("coba", "試す、試みる", "試行錯誤や挑戦、そして人生の試練を表す語根", [
        ("mencoba", "他動詞", "試す、やってみる、挑戦する"),
        ("percobaan", "名詞", "実験、試み、試用期間"),
        ("cobaan", "名詞", "（人生の）試練、災難"),
        ("mencobai", "他動詞", "誘惑する、試す（宗教・文語的）"),
    ], "mencoba は挑戦・味見・試着に万能。masa percobaan で入社後の「試用期間」です。"),

    ("dorong", "押す、推進する", "物理的に押す動作から政策・経済の推進・後押しまで広がる語根", [
        ("mendorong", "他動詞", "押す、後押しする、促進する"),
        ("pendorong", "名詞", "推進者、推進要因、起爆剤"),
        ("dorongan", "名詞", "後押し、衝動、励まし"),
        ("terdorong", "受動・偶発", "押し出された、促された"),
    ], "faktor pendorong で「推進要因」、mendorong pertumbuhan ekonomi で「経済成長を後押しする」。"),

    ("hadap", "向く、直面する", "空間的方向から困難への対峙、法律関係の対象を形成する語根", [
        ("menghadapi", "他動詞", "直面する、立ち向かう、対峙する"),
        ("menghadap", "自動詞/他動詞", "〜に向いている、〜に面談する"),
        ("terhadap", "前置詞", "〜に対して、〜に関して"),
        ("berhadapan", "相互自動詞", "向かい合う、対立する"),
    ], "terhadap は「〜に対して」の最重要前置詞。menghadapi tantangan で「課題に直面する」。"),

    ("tuntut", "要求する、訴求する", "権利の要求、学問の探求、法廷での起訴まで厳格な意志を表す語根", [
        ("menuntut", "他動詞", "要求する、起訴する、探求する"),
        ("tuntutan", "名詞", "要求、請求、訴因"),
        ("penuntut", "名詞", "原告、検察官（penuntut umum）"),
        ("tertuntut", "受動", "要求された、義務付けられた"),
    ], "menuntut ilmu で「学問を修める」、tuntutan pasar で「市場の要請」を表します。"),

    ("sebar", "広める、散布する", "情報の拡散から病気の流行、製品の流通網まで広がりを表す語根", [
        ("menyebar", "自動詞", "広がる、拡散する、散らばる"),
        ("menyebarkan", "使役他動詞", "広める、配布する、宣伝する"),
        ("tersebar", "受動・完了", "広まった、点在している"),
        ("penyebaran", "名詞", "拡散、配布、伝播"),
        ("persebaran", "名詞", "分布、配置状況"),
    ], "menyebarkan hoaks で「デマを拡散する」、persebaran penduduk で「人口分布」。"),

    ("tentu", "定まる、確実な", "方針の決定から法的規則、確信の表現まで日常・実務に不可欠な語根", [
        ("menentukan", "他動詞", "決定する、定める、左右する"),
        ("tertentu", "形容詞的受動", "特定の、一定の"),
        ("ketentuan", "名詞", "規定、条項、条件"),
        ("penentuan", "名詞", "決定プロセス、策定"),
        ("tentunya", "副詞", "もちろん、当然のことながら"),
    ], "syarat dan ketentuan で「利用規約」、menentukan masa depan で「将来を決定する」。"),

    ("tuju", "向かう、意図する", "物理的な移動の目的地から、人生の目標、合意まで幅広く派生する語根", [
        ("menuju", "他動詞/前置詞", "〜に向かう、〜を目指す"),
        ("bertujuan", "自動詞", "〜を目的とする、目指している"),
        ("tujuan", "名詞", "目的、目標、目的地"),
        ("setuju", "形容詞/動詞", "同意する、賛成する"),
        ("persetujuan", "名詞", "合意、承認、許可"),
    ], "setuju（同意する）は se- + tuju（同じ方向を向く）の成り立ち。surat persetujuan で「承諾書」。"),

    ("tolak", "拒否する、退ける", "提案の拒絶から出発点、押し返す動作までを表す語根", [
        ("menolak", "他動詞", "拒否する、断る、却下する"),
        ("penolakan", "名詞", "拒絶、却下、否認"),
        ("tertolak", "受動", "却下された、断られた"),
        ("bertolak", "自動詞", "出発する、〜を出発点とする"),
        ("bertolak belakang", "熟語", "正反対である、矛盾する"),
    ], "menolak tawaran で「申し出を断る」、bertolak belakang で「正反対・矛盾する」。"),

    ("tanggung", "責任を負う、引き受ける", "義務や責任、費用の負担、保証を語る上で欠かせない語根", [
        ("menanggung", "他動詞", "負担する、被る、保証する"),
        ("tanggung jawab", "熟語名詞", "責任、責務"),
        ("bertanggung jawab", "複合動詞", "責任を負う、担当する"),
        ("pertanggungjawaban", "名詞", "説明責任、決算報告（LPJ）"),
        ("tanggungan", "名詞", "扶養家族、負担"),
    ], "menanggung biaya で「費用を負担する」、LPJ（Laporan Pertanggungjawaban）は必修実務用語。"),

    # 11-20
    ("tarik", "引く、引きつける", "物理的な牽引から預金の引き出し、関心や魅力の喚起までを表す語根", [
        ("menarik", "他動詞/形容詞", "引く、引き出す、興味深い・魅力的な"),
        ("tertarik", "形容詞/受動", "興味がある、引きつけられた"),
        ("ketertarikan", "名詞", "関心、興味、好意"),
        ("penarikan", "名詞", "引き出し、回収、撤退"),
    ], "menarik uang di ATM で「預金引き出し」、sangat menarik で「とても興味深い」。"),

    ("susun", "組み立てる、構成する", "計画の策定、文章の作成、組織の階層化を意味する語根", [
        ("menyusun", "他動詞", "組み立てる、作成する、計画する"),
        ("tersusun", "受動・完了", "構成されている、配置された"),
        ("susunan", "名詞", "構成、配列、編成"),
        ("penyusun", "名詞", "執筆者、編成者、構成要素"),
    ], "menyusun rencana で「計画を立てる」、susunan kabinet で「内閣の組閣・名簿」。"),

    ("nilai", "評価する、値する", "金銭的価値から人事評価、倫理的価値観まで広く扱う語根", [
        ("menilai", "他動詞", "評価する、採点する、鑑定する"),
        ("penilaian", "名詞", "評価、査定、アセスメント"),
        ("bernilai", "自動詞/形容詞", "価値がある、貴重な"),
        ("nilai", "名詞", "価値、点数、価格"),
    ], "penilaian kinerja で「人事業績評価」、bernilai tinggi で「高価値の」。"),

    ("ukur", "測定する、測る", "寸法・重量の計測から基準、成果の定量的把握を表す語根", [
        ("mengukur", "他動詞", "測定する、測る、評価する"),
        ("pengukuran", "名詞", "測定、計測、測量"),
        ("ukuran", "名詞", "サイズ、寸法、基準"),
        ("terukur", "形容詞", "測定可能な、定量化された"),
    ], "mengukur suhu で「体温を測る」、hasil yang terukur で「測定可能な定量的成果」。"),

    ("milik", "所有する、財産", "個人・法人の所有権から財産、国家主権までを論じる重要語根", [
        ("memiliki", "他動詞", "持っている、所有する、具備する"),
        ("kepemilikan", "名詞", "所有権、株式保有比率"),
        ("pemilik", "名詞", "オーナー、所有者、持ち主"),
        ("milik", "名詞", "所有物、〜のもの"),
    ], "memiliki izin で「許可を保持している」、pemilik saham で「株主」。"),

    ("pegang", "握る、保持する", "手で掴む動作から職務の担当、理念の堅持を表す語根", [
        ("memegang", "他動詞", "握る、持つ、担当する"),
        ("berpegang", "自動詞", "固執する、拠って立つ（〜pada）"),
        ("pegangan", "名詞", "手すり、よりどころ、マニュアル"),
        ("pemegang", "名詞", "保持者、所持人、ホルダー"),
    ], "pemegang saham で「株主（シェアホルダー）」、memegang peranan で「役割を担う」。"),

    ("ganti", "交換する、交代する", "部品の交換、シフト交代、損失の補償・賠償を表す語根", [
        ("mengganti", "他動詞", "交換する、代える、弁償する"),
        ("berganti", "自動詞", "変わる、交代する、着替える"),
        ("pergantian", "名詞", "交代、交代期、更迭"),
        ("ganti rugi", "熟語名詞", "損害賠償、補償金"),
    ], "ganti rugi で「損害賠償」、pergantian pimpinan で「リーダーの交代」。"),

    ("bagi", "分配する、共有する", "分割やシェア、前置詞としての「〜にとって」を導く多機能語根", [
        ("membagi", "他動詞", "分ける、分割する、割り算する"),
        ("berbagi", "自動詞", "分かち合う、シェアする"),
        ("pembagian", "名詞", "分配、配分、区分"),
        ("sebagian", "名詞/副詞", "一部、大半の（sebagian besar）"),
    ], "bagi saya で「私にとって」、berbagi pengalaman で「経験を共有する」。"),

    ("kait", "関連づける、連動する", "フックにかける物理動作から制度・事件の因果関係を表す語根", [
        ("mengaitkan", "他動詞", "結びつける、関連づける"),
        ("terkait", "形容詞/受動", "関連する、関係のある"),
        ("keterkaitan", "名詞", "相互連動性、因果関係"),
        ("kaitan", "名詞", "つながり、フック"),
    ], "pihak terkait で「関係者・関係機関」、isu terkait で「関連する課題」。"),

    ("dasar", "基礎、根拠", "物事の土台から法的前提、基本方針を築く超重要語根", [
        ("mendasari", "他動詞", "〜の基礎となる、根底にある"),
        ("berdasarkan", "前置詞/自動詞", "〜に基づいて、〜に準拠して"),
        ("dasar", "名詞", "基礎、土台、底"),
        ("dasar-dasar", "名詞", "基礎知識、入門"),
    ], "berdasarkan data で「データに基づいて」、hukum dasar で「基本法（憲法）」。"),

    # 21-30
    ("nyata", "明確な、表明する", "事実の宣言、声明、現実の具現化を表す語根", [
        ("menyatakan", "他動詞", "表明する、述べる、宣言する"),
        ("pernyataan", "名詞", "声明、発言、言明"),
        ("ternyata", "副詞/自発", "実は〜だと判明する、なんと"),
        ("kenyataan", "名詞", "現実、事実、真相"),
    ], "pernyataan resmi で「公式声明」、ternyata benar で「実は本当だった」。"),

    ("adil", "公平な、正義", "司法制度、裁判所、平等の理念を語る法学・社会の中心語根", [
        ("mengadili", "他動詞", "裁判する、裁く、審理する"),
        ("keadilan", "名詞", "正義、公平さ、公正"),
        ("pengadilan", "名詞", "裁判所、法廷"),
        ("peradilan", "名詞", "司法制度、裁判手続き"),
    ], "pengadilan negeri で「地方裁判所」、keadilan sosial で「社会正義」。"),

    ("hubung", "繋ぐ、連絡する", "通信、交通網、人間関係、国際協調の基盤をなす語根", [
        ("menghubungkan", "他動詞", "つなぐ、連結する、連絡する"),
        ("berhubungan", "自動詞", "関係がある、連絡を取り合う"),
        ("hubungan", "名詞", "関係、交際、コネクション"),
        ("perhubungan", "名詞", "運輸、通信、交通行政"),
    ], "Kementerian Perhubungan で「運輸省」、hubungan bilateral で「二国間関係」。"),

    ("diri", "立つ、自己", "起立の動作から会社の設立、自己自身を表す語根", [
        ("berdiri", "自動詞", "立つ、設立される"),
        ("mendirikan", "他動詞", "設立する、創設する、建てる"),
        ("pendirian", "名詞", "設立、見解、信念"),
        ("terdiri dari", "熟語", "〜から構成される"),
    ], "mendirikan perusahaan で「会社を設立する」、terdiri dari 5 bab で「5章から成る」。"),

    ("bina", "育成する、構築する", "人材育成、国家建設、組織の指導教育を表す語根", [
        ("membina", "他動詞", "育成する、指導する、構築する"),
        ("pembinaan", "名詞", "育成、指導、能力開発"),
        ("pembina", "名詞", "指導員、育成者、顧問"),
        ("terbina", "受動", "育成された、構築された"),
    ], "membina hubungan で「良好な関係を築く」、pembinaan karier で「キャリア育成」。"),

    ("ajak", "誘う、促す", "共同行動の呼びかけ、提案、キャンペーンを表す語根", [
        ("mengajak", "他動詞", "誘う、促す、呼びかける"),
        ("ajakan", "名詞", "誘い、呼びかけ、勧誘"),
        ("diajak", "受動", "誘われる、招待される"),
    ], "mengajak kerja sama で「協力を呼びかける」、ajakan boikot で「不買運動の呼びかけ」。"),

    ("serah", "引き渡す、委ねる", "業務の引き継ぎ、提出、運命への降伏・帰依を表す語根", [
        ("menyerahkan", "他動詞", "引き渡す、提出する、委ねる"),
        ("penyerahan", "名詞", "引き渡し、納品、移譲"),
        ("pasrah / berserah", "自動詞", "身を任せる、成り行きに任せる"),
        ("terserah", "慣用表現", "お任せします、あなた次第です"),
    ], "Terserah Anda で「あなたにお任せします」、menyerahkan laporan で「報告書を提出する」。"),

    ("banding", "比較する、匹敵する", "優劣の比較、控訴（司法）、比率を表す語根", [
        ("membandingkan", "他動詞", "比較する、対比させる"),
        ("perbandingan", "名詞", "比較、比率、プロポーション"),
        ("sebanding", "形容詞", "見合っている、匹敵する"),
        ("banding", "名詞", "上訴、控訴（裁判）"),
    ], "mengajukan banding で「控訴する」、sebanding dengan harga で「価格に見合っている」。"),

    ("tambah", "加える、増加する", "数量の増加、残業、補足情報を表す語根", [
        ("menambah", "他動詞", "増やす、付け足す、加える"),
        ("bertambah", "自動詞", "増える、増加する"),
        ("tambahan", "名詞/形容詞", "追加、補足、付加的な"),
        ("penambahan", "名詞", "追加、増強、加算"),
    ], "biaya tambahan で「追加費用」、jam kerja tambahan で「残業時間」。"),

    ("kurang", "減らす、欠ける", "数量の減少、不足、否定辞（あまり〜ない）を表す語根", [
        ("mengurangi", "他動詞", "減らす、削減する、引き算する"),
        ("berkurang", "自動詞", "減る、減少する、衰退する"),
        ("kekurangan", "名詞", "不足、欠点、短所"),
        ("pengurangan", "名詞", "削減、減税、マイナス"),
    ], "mengurangi limbah で「廃棄物を削減する」、kekurangan modal で「資本不足」。"),

    # 31-40
    ("hitung", "計算する、数える", "見積もり、会計計算、統計的算定を表す語根", [
        ("menghitung", "他動詞", "数える、計算する、算出する"),
        ("perhitungan", "名詞", "計算、見積もり、打算"),
        ("terhitung", "受動/副詞", "〜付で（日付）、計算に入る"),
        ("berhitung", "自動詞", "算数をする、暗算する"),
    ], "perhitungan matang で「綿密な計算」、terhitung sejak hari ini で「本日付で」。"),

    ("pilih", "選ぶ、選択する", "購買の選択、意思決定、国政選挙を表す語根", [
        ("memilih", "他動詞", "選ぶ、選択する、投票する"),
        ("pilihan", "名詞/形容詞", "選択肢、チョイス、特選の"),
        ("pemilihan", "名詞", "選挙、選考、セレクション"),
        ("terpilih", "受動", "選ばれた、当選した"),
    ], "pemilihan umum (pemilu) で「総選挙」、banyak pilihan で「選択肢が多い」。"),

    ("kuat", "強化する、強固な", "筋力・強度から経済・法的効力の強化を表す語根", [
        ("memperkuat", "使役他動詞", "強化する、補強する、固める"),
        ("kekuatan", "名詞", "力、強さ、勢力"),
        ("menguat", "自動詞", "強まる、（通貨が）上昇する"),
        ("terkuat", "最上級", "最も強い、最強の"),
    ], "nilai rupiah menguat で「ルピア相場が上昇する」、memperkuat sinergi で「連携を強化する」。"),

    ("lemah", "弱める、衰退", "身体の衰弱から通貨安、論理の弱点を表す語根", [
        ("melemahkan", "使役他動詞", "弱める、骨抜きにする"),
        ("kelemahan", "名詞", "弱点、短所、脆さ"),
        ("melemah", "自動詞", "弱まる、（相場が）下落する"),
        ("pelemahan", "名詞", "下落、弱体化"),
    ], "kelemahan sistem で「システムの弱点」、daya beli melemah で「購買力が弱まる」。"),

    ("tingkat", "向上させる、段階", "建物の階数からスキル向上、進歩のステップを表す語根", [
        ("meningkatkan", "使役他動詞", "高める、向上させる、改善する"),
        ("peningkatan", "名詞", "向上、改善、増大"),
        ("meningkat", "自動詞", "上昇する、増大する"),
        ("bertingkat", "形容詞", "多層の、段階的な"),
    ], "meningkatkan efisiensi で「効率を高める」、peningkatan mutu で「品質向上」。"),

    ("turun", "低下する、降りる", "階段を降りる動作から価格の下落、子孫への継承を表す語根", [
        ("menurunkan", "使役他動詞", "下げる、降ろす、軽減する"),
        ("penurunan", "名詞", "下落、低下、減少"),
        ("menurun", "自動詞", "低下する、落ち込む"),
        ("keturunan", "名詞", "子孫、血統、〜系（keturunan Jepang）"),
    ], "penurunan harga で「値下げ」、turun minum で「ハーフタイム（スポーツ）」。"),

    ("naik", "上昇する、乗る", "乗り物に乗る動作から価格上昇、役職の昇進を表す語根", [
        ("menaikkan", "使役他動詞", "上げる、引き上げる、積載する"),
        ("kenaikan", "名詞", "上昇、引き上げ、昇進"),
        ("menaiki", "他動詞", "〜に乗る、登る"),
        ("naik kelas", "熟語", "進級する、ランクアップする"),
    ], "kenaikan gaji で「昇給」、naik pangkat で「昇進する」。"),

    ("luas", "拡大する、広大な", "面積の広さから事業のスケールアップ、視野の拡大を表す語根", [
        ("memperluas", "使役他動詞", "広げる、拡大する、拡張する"),
        ("perluasan", "名詞", "拡大、拡張、増床"),
        ("meluas", "自動詞", "広がる、蔓延する"),
        ("keluasan", "名詞", "広さ、自由裁量、寛容さ"),
    ], "memperluas jaringan で「ネットワークを広げる」、perluasan pasar で「市場開拓・拡張」。"),

    ("sempit", "狭める、窮屈な", "空間の狭小から時間的切迫、視野の狭さを表す語根", [
        ("menyempit", "自動詞", "狭くなる、縮小する"),
        ("mempersempit", "使役他動詞", "狭める、絞り込む"),
        ("penyempitan", "名詞", "狭窄、絞り込み、縮小"),
        ("kesempitan", "名詞/形容詞", "窮屈さ、狭さ、切迫"),
    ], "mempersempit peluang で「機会を狭める」、penyempitan pembuluh darah で「血管狭窄」。"),

    ("panjang", "延長する、長い", "物理的長さからビザや契約の更新・期間延長を表す語根", [
        ("memperpanjang", "使役他動詞", "延長する、更新する"),
        ("perpanjangan", "名詞", "延長、更新手続き"),
        ("berkepanjangan", "形容詞", "長引く、長期にわたる"),
        ("sepanjang", "前置詞/副詞", "〜に沿って、〜の間じゅう"),
    ], "perpanjangan KITAS で「就労ビザ更新」、krisis berkepanjangan で「長期化する危機」。"),

    # 41-50
    ("singkat", "要約する、簡潔な", "時間の短さから文章の要約、略語の形成を表す語根", [
        ("menyingkat", "他動詞", "短縮する、要約する、略す"),
        ("singkatan", "名詞", "略語、頭文字（略称）"),
        ("penyingkatan", "名詞", "要約、短縮"),
        ("mempersingkat", "使役他動詞", "（時間を）縮める、手短にする"),
    ], "singkatan umum で「一般的な略語」、mempersingkat waktu で「時間を節約・短縮する」。"),

    ("jelas", "説明する、明確な", "視覚のクリアさから状況の説明、疑惑の解明を表す語根", [
        ("menjelaskan", "他動詞", "説明する、解説する、明らかにする"),
        ("penjelasan", "名詞", "説明、解説、注釈"),
        ("memperjelas", "使役他動詞", "より明確にする、鮮明にする"),
        ("kejelasan", "名詞", "明確さ、明瞭性"),
    ], "meminta penjelasan で「説明を求める」、memberikan kejelasan で「明確な指針を出す」。"),

    ("kabur", "曖昧にする、逃亡する", "視界のぼやけから意図的な論点ずらし、容疑者の逃亡を表す語根", [
        ("mengaburkan", "使役他動詞", "曇らせる、曖昧にする、ぼやかす"),
        ("pengaburan", "名詞", "隠蔽、曖昧化、論点ずらし"),
        ("kabur", "自動詞/形容詞", "逃げる、ぼやけた、かすかな"),
    ], "mengaburkan fakta で「事実を曖昧にする・隠蔽する」、tahanan kabur で「囚人が脱走した」。"),

    ("lengkap", "補完する、完全な", "書類の不備解消から設備完備、フルセットの提供を表す語根", [
        ("melengkapi", "他動詞", "完備する、補完する、添付する"),
        ("dilengkapi", "受動", "〜が備え付けられている"),
        ("perlengkapan", "名詞", "装備、備品、アメニティ"),
        ("kelengkapan", "名詞", "書類の具備、完全性"),
    ], "fasilitas lengkap で「充実した設備」、kelengkapan berkas で「提出書類の完備」。"),

    ("rusak", "破壊する、損害", "機械の故障から自然環境の破壊、人間関係の破綻を表す語根", [
        ("merusak", "他動詞", "壊す、損なう、荒らす"),
        ("kerusakan", "名詞", "故障、損害、破損"),
        ("perusak", "名詞", "破壊者、害虫、攪乱要因"),
    ], "kerusakan mesin で「機械故障」、merusak lingkungan で「環境を破壊する」。"),

    ("baik", "改善する、善意", "道徳的良さから設備の修理、関係の改善・修復を表す語根", [
        ("memperbaiki", "使役他動詞", "修理する、改善する、直す"),
        ("perbaikan", "名詞", "改善、修理、改修工事"),
        ("kebaikan", "名詞", "善意、親切、長所"),
        ("sebaiknya", "副詞", "〜したほうがよい（提案）"),
    ], "memperbaiki kesalahan で「誤りを正す」、perbaikan jalan で「道路補修工事」。"),

    ("buruk", "悪化する、悪い", "品質の悪さから治安・病状・景気の悪化を表す語根", [
        ("memburuk", "自動詞", "悪化する、下り坂になる"),
        ("memperburuk", "使役他動詞", "さらに悪化させる、追い討ちをかける"),
        ("keburukan", "名詞", "短所、欠陥、悪事"),
        ("perburukan", "名詞", "悪化プロセス、病状悪化"),
    ], "kondisi memburuk で「容態が悪化する」、memperburuk situasi で「事態をさらに悪化させる」。"),

    ("mati", "停止する、死亡", "生命の死から電気・機械のスイッチ停止、麻痺を表す語根", [
        ("mematikan", "使役他動詞", "消す、電源を切る、殺傷する"),
        ("kematian", "名詞", "死亡、死期、致死"),
        ("mati rasa", "熟語", "無感覚になる、麻痺する"),
        ("pematian", "名詞", "シャットダウン、消去"),
    ], "mematikan lampu で「電気を消す」、angka kematian で「死亡率」。"),

    ("sadar", "自覚する、意識", "気絶からの意識回復から社会的責任の自覚、コンプライアンスを表す語根", [
        ("menyadari", "他動詞", "気付く、自覚する、認識する"),
        ("kesadaran", "名詞", "意識、自覚、コンシャスネス"),
        ("tersadar", "受動/自発", "ふと我に返る、目が覚める"),
        ("penyadaran", "名詞", "啓発、意識改革"),
    ], "kesadaran hukum で「遵法意識」、menyadari kesalahan で「過ちに気付く」。"),

    ("lupa", "忘れる、忘却", "記憶の喪失から約束のうっかり失念、恩知らずを表す語根", [
        ("melupakan", "他動詞", "忘れる、水に流す、度外視する"),
        ("kelupaan", "口語名詞/自発", "うっかり忘れる、失念"),
        ("terlupakan", "受動・可能", "忘れ去られた、見落とされた"),
        ("pelupa", "名詞/形容詞", "忘れっぽい人、健忘"),
    ], "jangan lupa で「忘れないで」、sulit dilupakan で「忘れ難い」。")
]

def generate_article(item):
    root, meaning, desc, table, usage_note = item
    
    # Derivations summary string
    deriv_names = ", ".join([f"**{row[0]}**" for row in table])
    
    table_rows = []
    table_rows.append(f"語根 **{root}**（意味: {meaning}）から派生する主要な単語一覧です。\n")
    table_rows.append("| 派生語 | 品詞・分類 | 主な日本語の意味・ニュアンス |")
    table_rows.append("| :--- | :--- | :--- |")
    for w, pos, m in table:
        table_rows.append(f"| **{w}** | {pos} | {m} |")
    table_content = "\n".join(table_rows)

    # Detailed cards
    details_content = []
    for i, (w, pos, m) in enumerate(table[:3], 1):
        details_content.append(f"### ① {w}（{pos}: {m}）" if i == 1 else f"### ② {w}（{pos}: {m}）" if i == 2 else f"### ③ {w}（{pos}: {m}）")
        details_content.append(f"- **ポイント**: {usage_note}")
        details_content.append(f"""<div class="id-example">
<div class="id-sentence">Penggunaan kata {w} sangat penting dalam konteks formal dan praktis sehari-hari.</div>
<div class="id-translation">「{w}」という単語の使用は、公式な場面および日常の実践的な文脈において極めて重要です。</div>
<div class="id-explanation">語根「**{root}**」の派生語として、文脈に応じて正確に使い分けることが求められます。</div>
</div>\n""")
        
    details_str = "\n".join(details_content)
    
    q1_q = f"「 {table[0][0]} 」の品詞と主な日本語の意味は？"
    q1_a = f"{table[0][1]}（{table[0][2]}）"
    q2_q = f"語根「 {root} 」から派生した名詞の代表例は？"
    q2_a = f"{table[-1][0]}（{table[-1][2]}）"

    content = f"""# 語根 {root} の全派生語図鑑（{deriv_names}）

インドネシア語の重要語根 **{root}（{meaning}）** は、{desc}。
日常会話からビジネス実務、公的文書、検定試験で必須となる派生語を体系的に完全整理します。

---

## 1. 語根 {root} からの派生語ファミリー

{table_content}

---

## 2. 各派生語の詳細解説と例文

{details_str}

---

## 3. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. {q1_q}</summary>
<strong>正解: {q1_a}</strong><br>
解説: 接辞の変化規則を理解することで、語根から語義を論理的に推測できます。
</details>

<details class="id-quiz">
<summary>Q2. {q2_q}</summary>
<strong>正解: {q2_a}</strong><br>
解説: 接尾辞や周囲辞の働きにより、動詞や形容詞から抽象名詞や事象名詞が形成されます。
</details>
"""
    return content

out_dir = "docs/derivations"
created = 0

for item in ROOT_DATA:
    root = item[0]
    filename = f"root-{root}.md"
    fpath = os.path.join(out_dir, filename)
    article_text = generate_article(item)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(article_text)
    created += 1

print(f"Successfully generated {created} root derivation articles in {out_dir}!")
