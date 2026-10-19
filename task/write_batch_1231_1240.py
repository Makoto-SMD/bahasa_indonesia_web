# -*- coding: utf-8 -*-
import os
import re

stories = [
    {
        "id": "1231",
        "slug": "level-4-01-new-capital-nusantara",
        "title": "【Level 4 (B2)】Membangun Kota Masa Depan IKN Nusantara（森林新首都ヌサンタラ建設の光と影）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "ジャカルタの過密・地盤沈下を背景に東カリマンタン州で進む新首都IKNヌサンタラ建設。スマート・フォレストシティ構想、先住慣習権の尊重、環境保全との調和を問う本格論説パッセージ。",
        "text": """Pemindahan ibu kota negara dari Jakarta ke Ibu Kota Nusantara (IKN) di Kabupaten Penajam Paser Utara, Kalimantan Timur, merupakan salah satu keputusan geopolitik dan tata ruang paling monumental dalam sejarah modern Indonesia. Selama berpuluh-puluh tahun, Jakarta telah memikul beban demografis dan ekologis yang melampaui daya dukungnya. Ancaman penurunan muka tanah yang masif, kemacetan lalu lintas kronis yang menelan kerugian ekonomi triliunan rupiah setiap tahunnya, serta sentralisasi kekayaan yang berpusat di Pulau Jawa semata, mendasari urgensi transformasi spasial yang berkeadilan sosial ini.

Pemerintah merancang IKN bukan sekadar sebagai relokasi pusat birokrasi pemerintahan, melainkan sebagai manifesto peradaban baru berkonsep kota hutan pintar (smart forest city). Dalam cetak biru pembangunannya, lebih dari tujuh puluh persen kawasan dirancang tetap menjadi ruang terbuka hijau yang didominasi oleh reboisasi hutan hujan tropis. Sistem transportasi massal berbasis energi listrik otonom, pemanfaatan energi baru terbarukan bertenaga surya dan hidro, serta penerapan konstruksi hijau netral karbon digadang-gadang sebagai komitmen konkret Indonesia dalam mitigasi krisis iklim global.

Kendatipun demikian, mega proyek dengan estimasi anggaran ratusan triliun rupiah ini menuai diskursus publik yang sangat dinamis dan kritis. Para pemerhati lingkungan mengingatkan risiko fragmentasi habitat satwa endemik seperti orangutan dan bekantan akibat pembukaan koridor infrastruktur jalan tol dan bendungan. Di samping itu, pengakuan serta perlindungan terhadap hak ulayat masyarakat adat suku Balik dan Paser setempat menjadi ujian sesungguhnya bagi komitmen inklusivitas pemerintah, agar pembangunan tidak mengulang paradigma lama yang mengorbankan kaum marjinal demi kilau modernitas.

Keberhasilan IKN pada akhirnya tidak semata diukur dari kemegahan istana garuda atau kecanggihan gedung pencakar langitnya, melainkan dari sejauh mana kota ini mampu mewujudkan visi Indonesia-sentris yang meratakan kesejahteraan antarpulau. Mewujudkan kota masa depan yang berkelanjutan menuntut tata kelola yang transparan, partisipasi publik yang bermakna, dan keberanian etis untuk menyeimbangkan akselerasi pertumbuhan ekonomi dengan kelestarian alam hayati nusantara.""",
        "paragraphs": [
            ("Pemindahan ibu kota negara dari Jakarta ke Ibu Kota Nusantara (IKN) di Kabupaten Penajam Paser Utara, Kalimantan Timur, merupakan salah satu keputusan geopolitik dan tata ruang paling monumental dalam sejarah modern Indonesia. Selama berpuluh-puluh tahun, Jakarta telah memikul beban demografis dan ekologis yang melampaui daya dukungnya. Ancaman penurunan muka tanah yang masif, kemacetan lalu lintas kronis yang menelan kerugian ekonomi triliunan rupiah setiap tahunnya, serta sentralisasi kekayaan yang berpusat di Pulau Jawa semata, mendasari urgensi transformasi spasial yang berkeadilan sosial ini.",
             "ジャカルタから東カリマンタン州北プナジャム・パセール県に位置する新首都ヌサンタラ（IKN）への遷都は、インドネシア近現代史において最も記念碑的な地政学的・国土空間計画上の決断の一つです。数十年にわたり、ジャカルタはその環境収容力を超える人口動態的および生態学的重荷を背負い続けてきました。大規模な地盤沈下の脅威、毎年数兆ルピアの経済損失を生み出す慢性的な交通渋滞、そしてもっぱらジャワ島のみに集中する富の一極集中が、この社会正義に適った空間的変革の緊急性を根底から支えています。",
             "keputusan monumental（記念碑的決断）、daya dukung（環境収容力）、penurunan muka tanah（地盤沈下）、transformasi spasial berkeadilan sosial（社会的正義に適った空間変革）。"),
            ("Pemerintah merancang IKN bukan sekadar sebagai relokasi pusat birokrasi pemerintahan, melainkan sebagai manifesto peradaban baru berkonsep kota hutan pintar (smart forest city). Dalam cetak biru pembangunannya, lebih dari tujuh puluh persen kawasan dirancang tetap menjadi ruang terbuka hijau yang didominasi oleh reboisasi hutan hujan tropis. Sistem transportasi massal berbasis energi listrik otonom, pemanfaatan energi baru terbarukan bertenaga surya dan hidro, serta penerapan konstruksi hijau netral karbon digadang-gadang sebagai komitmen konkret Indonesia dalam mitigasi krisis iklim global.",
             "政府はIKNを単なる政府官僚機構の中枢移転としてではなく、「スマート・フォレストシティ（森林スマート都市）」構想を掲げた新たな文明宣言（マニフェスト）として設計しています。その建設基本計画（ブループリント）では、全域の70%以上が熱帯雨林の植林再生活動によって占められる緑地オープンスペースとして維持されるよう設計されています。自動運転型電気エネルギーによる大量公共交通システム、太陽光や水力を活用した新再生可能エネルギーの利用、そしてカーボンニュートラルなグリーン建築の導入は、地球規模の気候危機緩和におけるインドネシアの具体的コミットメントとして大々的に喧伝されています。",
             "manifesto peradaban（文明のマニフェスト）、cetak biru（基本計画・設計図）、ruang terbuka hijau（緑地空間）、energi baru terbarukan（新再生可能エネルギー）、digadang-gadang（大いに期待・喧伝されている）。"),
            ("Kendatipun demikian, mega proyek dengan estimasi anggaran ratusan triliun rupiah ini menuai diskursus publik yang sangat dinamis dan kritis. Para pemerhati lingkungan mengingatkan risiko fragmentasi habitat satwa endemik seperti orangutan dan bekantan akibat pembukaan koridor infrastruktur jalan tol dan bendungan. Di samping itu, pengakuan serta perlindungan terhadap hak ulayat masyarakat adat suku Balik dan Paser setempat menjadi ujian sesungguhnya bagi komitmen inklusivitas pemerintah, agar pembangunan tidak mengulang paradigma lama yang mengorbankan kaum marjinal demi kilau modernitas.",
             "それにもかかわらず、数百兆ルピアの概算予算を伴うこの巨大メガプロジェクトは、極めてダイナミックで批判的な公的議論（言説）を巻き起こしています。環境保護活動家らは、高速道路やダムといったインフラ回廊の開削に伴うオランウータンやテングザルなどの固有動物の生息地分断化リスクに警鐘を鳴らしています。それに加えて、地元のバリック族やパセール族などの先住慣習法共同体の慣習的土地権（hak ulayat）の承認と保護は、開発が近代性の眩い輝きのために社会的弱者を犠牲にする古いパラダイムを繰り返さないための、政府の包摂性への本物の試練となっています。",
             "kendatipun demikian（それにもかかわらず）、menuai diskursus publik（公的議論を巻き起こす）、fragmentasi habitat（生息地の分断化）、hak ulayat（先住慣習的土地所有権）、kaum marjinal（社会的周縁層・弱者）。"),
            ("Keberhasilan IKN pada akhirnya tidak semata diukur dari kemegahan istana garuda atau kecanggihan gedung pencakar langitnya, melainkan dari sejauh mana kota ini mampu mewujudkan visi Indonesia-sentris yang meratakan kesejahteraan antarpulau. Mewujudkan kota masa depan yang berkelanjutan menuntut tata kelola yang transparan, partisipasi publik yang bermakna, dan keberanian etis untuk menyeimbangkan akselerasi pertumbuhan ekonomi dengan kelestarian alam hayati nusantara.",
             "IKNの成功は、最終的にはガルーダ大統領宮殿の壮麗さや超高層ビルの先端技術によってのみ測られるのではなく、この都市が島嶼間の福祉と富を均等化する「インドネシア中心主義」のビジョンをどれほど体現できるかによって測られます。持続可能な未来都市を実現することは、透明性の高いガバナンス、実質的な市民参加、そして経済成長の加速と列島の豊かな自然生態系の保全とを均衡させる倫理的勇気を強く求めているのです。",
             "tidak semata diukur dari...（〜によってのみ測られるのではない）、visi Indonesia-sentris（全インドネシア中心主義・脱ジャワ中心）、partisipasi publik bermakna（実質的・有意義な市民参加）、keberanian etis（倫理的勇気）。")
        ],
        "vocab": [
            ("geopolitik", "名詞", "-", "地政学、地政学的要因", "Pemindahan ibu kota adalah keputusan geopolitik besar."),
            ("monumental", "形容詞", "-", "記念碑的な、歴史に残る極めて重大な", "Karya arsitektur itu sangat monumental."),
            ("daya dukung", "名詞句", "dukung", "環境収容力、支持力", "Jumlah penduduk melebihi daya dukung lingkungan."),
            ("manifesto", "名詞", "-", "宣言、声明文、マニフェスト", "Buku itu merupakan manifesto peradaban hijau."),
            ("cetak biru", "名詞句", "-", "青写真、基本計画、ブループリント", "Pemerintah merilis cetak biru pembangunan 20 tahun."),
            ("digadang-gadang", "動詞（受動・反復）", "gadang", "大いに期待される、喧伝される", "Proyek ini digadang-gadang jadi penggerak ekonomi."),
            ("kendatipun demikian", "接続表現", "-", "それにもかかわらず、そうではあるが", "Kendatipun demikian, kita harus tetap waspada."),
            ("diskursus", "名詞", "-", "言説、公的議論、ディスクール", "Topik ini memicu diskursus hangat di media sosial."),
            ("hak ulayat", "名詞句", "-", "慣習法共同体の土地用益権・先住権", "Hak ulayat masyarakat adat dijamin konstitusi."),
            ("tata kelola", "名詞句", "kelola", "統治、ガバナンス、管理体制", "Tata kelola keuangan negara harus transparan.")
        ],
        "grammar_points": """1. **重層的論理接続表現 `Kendatipun demikian, ...`（それにもかかわらず）**:
   - 前述の壮大な構想やメリットを認めつつ、直後に批判的検証やリスクを対置するB2レベルの必須論述表現です。
2. **抽象名詞化の極致 `peN-...-an`（例: `pemindahan`, `penurunan`, `pemanfaatan`）**:
   - 動詞の動作そのものを格調高い政策概念として客観化します。
   - *pindah* → *pemindahan*（移転・遷都）
   - *turun* → *penurunan muka tanah*（地盤沈下）
3. **範囲・程度を規定する構文 `sejauh mana ... mampu ...`（〜がどれほど〜できるか）**:
   - 評価基準や達成度を検証する論説文特有の構文です。
   - 例: *Tergantung pada sejauh mana kita mampu beradaptasi.*（我々がどれほど適応できるかにかかっている。）""",
        "quizzes": [
            ("ジャカルタから新首都（IKN）への移転を決定づけた根本的な危機（urgensi）は何ですか？",
             ["ジャカルタの寒冷化と豪雪", "地盤沈下の脅威、巨額の渋滞損失、およびジャワ島への極端な富の一極集中", "ジャカルタの人口が激減して過疎化したこと"],
             "地盤沈下の脅威、巨額の渋滞損失、およびジャワ島への極端な富の一極集中",
             "第1段落に「Ancaman penurunan muka tanah yang masif, kemacetan lalu lintas kronis yang menelan kerugian ekonomi triliunan rupiah... serta sentralisasi kekayaan yang berpusat di Pulau Jawa...」とあります。"),
            ("新首都IKNの都市計画ブループリントにおいて、全体の何パーセント以上が緑地空間（ruang terbuka hijau）として設計されていますか？",
             ["30パーセント", "50パーセント", "70パーセント以上"],
             "70パーセント以上",
             "第2段落に「...lebih dari tujuh puluh persen kawasan dirancang tetap menjadi ruang terbuka hijau yang didominasi oleh reboisasi hutan hujan tropis.」とあります。"),
            ("IKN建設に伴って環境保護団体や有識者が強く懸念している社会的・環境的リスクは何ですか？",
             ["野生動物（オランウータン等）の生息地分断と、先住民族（バリック族・パセール族等）の慣習権（hak ulayat）の保護", "建物のペンキの色が派手すぎること", "外国人観光客が全員車を運転すること"],
             "野生動物（オランウータン等）の生息地分断と、先住民族（バリック族・パセール族等）の慣習権（hak ulayat）の保護",
             "第3段落に「Para pemerhati lingkungan mengingatkan risiko fragmentasi habitat satwa endemik... perlindungan terhadap hak ulayat masyarakat adat suku Balik dan Paser...」とあります。")
        ],
        "culture": """### 森林都市構想「IKN Nusantara」と「Indonesia-sentris」の理念
インドネシアは長年、国土面積のわずか7%に過ぎないジャワ島に総人口の約56%とGDPの約58%が偏重する「Jawa-sentris（ジャワ一極集中）」の構造的課題を抱えてきました。
新首都「IKN Nusantara」は、地理的中心に近い東カリマンタン州に拠点を移すことで、東部インドネシアの振興と「Indonesia-sentris（全インドネシア均等発展）」を実現する国家戦略です。
大統領宮殿は国章である霊鳥ガルーダが翼を広げた荘厳な意匠で設計され、自然環境とデジタルインフラが融合する未来都市のショーケースを目指しています。"""
    },
    {
        "id": "1232",
        "slug": "level-4-02-nickel-downstreaming-economy",
        "title": "【Level 4 (B2)】Hilirisasi Nikel dan Transisi Energi Global（ニッケル下流化政策とEVバッテリーの覇権）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "未加工鉱石の輸出禁止から始まった資源ナショナリズムと「下流化（Hilirisasi）」の成果。EV電池産業のグローバルサプライチェーンと環境負荷のジレンマを読み解く。",
        "text": """Dalam kurun waktu beberapa tahun terakhir, kebijakan hilirisasi komoditas tambang, khususnya bijih nikel, telah mereposisi status Indonesia dalam rantai pasok global secara drastis. Keputusan berani pemerintah untuk melarang total ekspor bijih nikel mentah sejak awal tahun 2020 sempat memicu gelombang penolakan keras dari negara-negara maju, bahkan berujung pada gugatan sengketa dagang di Organisasi Perdagangan Dunia (WTO). Namun, keteguhan Indonesia untuk tidak lagi sekadar menjadi eksportir bahan mentah berharga murah telah membuahkan lonjakan nilai tambah ekonomi yang luar biasa.

Melalui kewajiban pembangunan fasilitas pemurnian atau smelter di dalam negeri, ekspor produk turunan nikel seperti feronikel, nikel matte, dan Mixed Hydroxide Precipitate (MHP) melonjak hingga puluhan kali lipat. Kawasan industri terpadu berskala raksasa dibangun di Morowali, Sulawesi Tengah, dan Weda Bay di Halmahera Tengah. Indonesia berhasil memikat investasi asing bernilai ratusan triliun rupiah untuk membangun ekosistem terintegrasi hulu-ke-hilir, mulai dari penambangan, peleburan, perakitan sel baterai kendaraan listrik (electric vehicle/EV), hingga manufaktur mobil listrik.

Kendati mendatangkan pundi-pundi devisa negara dan menciptakan puluhan ribu lapangan kerja, akselerasi hilirisasi nikel tidak lepas dari paradoks lingkungan yang mencemaskan. Proses peleburan nikel berkadar rendah menuntut pasokan energi listrik yang masif, yang hingga kini sebagian besar masih ditopang oleh pembangkit listrik tenaga uap (PLTU) batu bara mandiri. Ironi ini menjadi sorotan tajam di panggung internasional: upaya memproduksi komponen hijau demi transisi energi bersih dunia justru menyisakan jejak karbon yang tinggi dan ancaman limbah tailing di perairan pesisir nusantara.

Oleh sebab itu, babak lanjutan dari hilirisasi nikel harus bertransformasi menuju standar keberlanjutan yang lebih ketat, atau yang kerap diistilahkan sebagai green nickel. Pemerintah dan pelaku industri dituntut untuk segera mempercepat transisi energi hijau di kawasan industri, memperbaiki tata kelola keselamatan kerja, serta menjamin bahwa keuntungan devisa yang melimpah terdistribusi secara adil demi mengangkat derajat kesejahteraan masyarakat lingkar tambang yang selama ini menanggung dampak ekologis secara langsung.""",
        "paragraphs": [
            ("Dalam kurun waktu beberapa tahun terakhir, kebijakan hilirisasi komoditas tambang, khususnya bijih nikel, telah mereposisi status Indonesia dalam rantai pasok global secara drastis. Keputusan berani pemerintah untuk melarang total ekspor bijih nikel mentah sejak awal tahun 2020 sempat memicu gelombang penolakan keras dari negara-negara maju, bahkan berujung pada gugatan sengketa dagang di Organisasi Perdagangan Dunia (WTO). Namun, keteguhan Indonesia untuk tidak lagi sekadar menjadi eksportir bahan mentah berharga murah telah membuahkan lonjakan nilai tambah ekonomi yang luar biasa.",
             "ここ数年の間、鉱物資源、特にニッケル鉱石の下流化（ヒリリサシ／高付加価値化加工）政策は、世界サプライチェーンにおけるインドネシアの地位を劇的に再配置しました。2020年初頭から未加工のニッケル原鉱石の輸出を全面禁止するという政府の果敢な決断は、先進諸国からの激しい反発の波を引き起こし、世界貿易機関（WTO）における貿易紛争提訴にまで発展しました。しかし、安価な原材料の単なる輸出国にとどまることを拒絶したインドネシアの確固たる決意は、並外れた経済的高付加価値の急増を結実させました。",
             "hilirisasi（下流化・加工高付加価値化）、mereposisi（再配置する）、gugatan sengketa dagang（貿易紛争提訴）、lonjakan nilai tambah（付加価値の急増）。"),
            ("Melalui kewajiban pembangunan fasilitas pemurnian atau smelter di dalam negeri, ekspor produk turunan nikel seperti feronikel, nikel matte, dan Mixed Hydroxide Precipitate (MHP) melonjak hingga puluhan kali lipat. Kawasan industri terpadu berskala raksasa dibangun di Morowali, Sulawesi Tengah, dan Weda Bay di Halmahera Tengah. Indonesia berhasil memikat investasi asing bernilai ratusan triliun rupiah untuk membangun ekosistem terintegrasi hulu-ke-hilir, mulai dari penambangan, peleburan, perakitan sel baterai kendaraan listrik (electric vehicle/EV), hingga manufaktur mobil listrik.",
             "国内での製錬所（スメルター）建設の義務付けを通じて、フェロニッケル、ニッケルマット、混合水酸化沈殿物（MHP）などのニッケル派生加工品の輸出は何十倍にも跳ね上がりました。中央スラウェシ州モロワリや中央ハルマヘラ県ウェダベイに巨大な統合工業団地が建設されました。インドネシアは、採掘、製錬、電気自動車（EV）向けバッテリーセルの組み立て、電気自動車自体の製造に至るまで、上流から下流まで統合されたエコシステムを構築するために、数百兆ルピアに上る外国直接投資を惹きつけることに成功したのです。",
             "smelter（精錬所）、produk turunan（派生商品・加工品）、hulu-ke-hilir（上流から下流まで・包括的一貫体制）、manufaktur mobil listrik（電気自動車製造）。"),
            ("Kendati mendatangkan pundi-pundi devisa negara dan menciptakan puluhan ribu lapangan kerja, akselerasi hilirisasi nikel tidak lepas dari paradoks lingkungan yang mencemaskan. Proses peleburan nikel berkadar rendah menuntut pasokan energi listrik yang masif, yang hingga kini sebagian besar masih ditopang oleh pembangkit listrik tenaga uap (PLTU) batu bara mandiri. Ironi ini menjadi sorotan tajam di panggung internasional: upaya memproduksi komponen hijau demi transisi energi bersih dunia justru menyisakan jejak karbon yang tinggi dan ancaman limbah tailing di perairan pesisir nusantara.",
             "多額の外貨収入をもたらし数万人の雇用を創出したにもかかわらず、ニッケル下流化の加速は憂慮すべき環境的パラドックスと切り離せません。低品位ニッケルの製錬プロセスは膨大な電力供給を必要とし、その電力の大部分は今なお自家発電型の石炭火力発電所（PLTU）に依存しています。この皮肉（アイロニー）は国際舞台で厳しい監視の的となっています。世界のクリーンエネルギー転換のための「グリーン部品」を生産する試みが、むしろ高い二酸化炭素排出フットプリントと列島沿岸海域での鉱滓（テーリング）廃棄物脅威を残しているのです。",
             "pundi-pundi devisa（巨額の外貨資金）、PLTU batu bara mandiri（自家消費型石炭火力発電所）、transisi energi bersih（クリーンエネルギー転換）、jejak karbon（カーボンフットプリント）。"),
            ("Oleh sebab itu, babak lanjutan dari hilirisasi nikel harus bertransformasi menuju standar keberlanjutan yang lebih ketat, atau yang kerap diistilahkan sebagai green nickel. Pemerintah dan pelaku industri dituntut untuk segera mempercepat transisi energi hijau di kawasan industri, memperbaiki tata kelola keselamatan kerja, serta menjamin bahwa keuntungan devisa yang melimpah terdistribusi secara adil demi mengangkat derajat kesejahteraan masyarakat lingkar tambang yang selama ini menanggung dampak ekologis secara langsung.",
             "それゆえに、ニッケル下流化の次のステージは、しばしば「グリーン・ニッケル」と称される、より厳格な持続可能性基準へと転換しなければなりません。政府および業界関係者は、工業地帯におけるグリーンエネルギー転換の迅速な加速、労働安全衛生ガバナンスの是正、そしてこれまで生態学的打撃を直接被ってきた鉱山周辺住民の福祉水準を向上させるために、潤沢な外貨利益が公正に分配されることを保証することを強く求められています。",
             "green nickel（環境適合型グリーンニッケル）、masyarakat lingkar tambang（鉱山周辺コミュニティ）、menanggung dampak ekologis（環境的影響を背負う）。")
        ],
        "vocab": [
            ("hilirisasi", "名詞", "hilir", "下流化、加工による高付加価値化政策", "Hilirisasi mineral meningkatkan pendapatan negara."),
            ("komoditas", "名詞", "-", "商品、一次産品、コモディティ", "Kelapa sawit adalah komoditas ekspor utama."),
            ("sengketa", "名詞", "-", "紛争、係争、対立", "Kedua negara menyelesaikan sengketa perbatasan."),
            ("pemurnian", "名詞", "murni", "精製、純化、製錬プロセス", "Proses pemurnian emas butuh teknologi tinggi."),
            ("terpadu", "形容詞", "padu", "統合された、集約された、一体型の", "Kawasan industri terpadu dilengkapi pelabuhan."),
            ("devisa", "名詞", "-", "外貨、外国為替準備金", "Sektor pariwisata menyumbang devisa besar."),
            ("mencemaskan", "動詞", "cemas", "心配させる、懸念を抱かせる", "Kenaikan harga beras mencemaskan warga."),
            ("limbah", "名詞", "-", "廃棄物、排水、公害ゴミ", "Pabrik dilarang membuang limbah ke sungai."),
            ("tata kelola", "名詞句", "kelola", "ガバナンス、管理運営体制", "Tata kelola tambang harus berorientasi lingkungan."),
            ("derajat", "名詞", "-", "度合い、階層、地位・尊厳", "Pendidikan mengangkat derajat hidup keluarga.")
        ],
        "grammar_points": """1. **原因・結果の形式接続詞 `Oleh sebab itu, ...`（それゆえに）**:
   - 前段落での論理的展開や問題提起を受け、最終的な提言や結論を導く格調高い接続詞です。
2. **要求・責務を表す受動構文 `dituntut untuk ...`（〜することを求められている）**:
   - 語根 *tuntut*（要求する）+ *di- -kan*。
   - 例: *Pelaku usaha dituntut untuk mematuhi regulasi.*（事業者は規制を遵守することを求められている。）
3. **対比構文 `Alih-alih ..., justru ...`（〜する代わりに、むしろ〜）**:
   - 意図とは逆の結果が生じるアイロニーを表現する際の中上級構文です。""",
        "quizzes": [
            ("インドネシア政府が2020年から断行した、世界的な波紋を呼んだ貿易政策は何ですか？",
             ["完成車輸入の全面禁止", "未加工ニッケル原鉱石（bijih nikel mentah）の輸出全面禁止", "全国の鉱山の国営化と外国人追放"],
             "未加工ニッケル原鉱石（bijih nikel mentah）の輸出全面禁止",
             "第1段落に「Keputusan berani pemerintah untuk melarang total ekspor bijih nikel mentah sejak awal tahun 2020...」とあります。"),
            ("ニッケル下流化政策によってモロワリやウェダベイなどの工業団地が構築を目指している包括体制は何ですか？",
             ["採掘から製錬、EVバッテリーセル組み立て、電気自動車製造に至る上流から下流まで（hulu-ke-hilir）の一貫エコシステム", "石炭の輸出専門ターミナル", "海外からの使用済み家電製品のリサイクル解体工場"],
             "採掘から製錬、EVバッテリーセル組み立て、電気自動車製造に至る上流から下流まで（hulu-ke-hilir）の一貫エコシステム",
             "第2段落に「...membangun ekosistem terintegrasi hulu-ke-hilir, mulai dari penambangan, peleburan, perakitan sel baterai... hingga manufaktur mobil listrik.」とあります。"),
            ("ニッケル製錬の加速が国際社会から環境面で指摘されている「皮肉（ironi）」とは何ですか？",
             ["世界のクリーンエネルギー転換のためのEV部品製造が、製錬所の石炭火力発電所（PLTU）依存により高いCO2を排出していること", "ニッケルが軽すぎて船に積めないこと", "電気自動車の普及でガソリンスタンドが喜んでいること"],
             "世界のクリーンエネルギー転換のためのEV部品製造が、製錬所の石炭火力発電所（PLTU）依存により高いCO2を排出していること",
             "第3段落に「...upaya memproduksi komponen hijau demi transisi energi bersih dunia justru menyisakan jejak karbon yang tinggi...」とあります。")
        ],
        "culture": """### 資源ナショナリズムと「Hilirisasi（下流化）」戦略
インドネシアは世界のニッケル埋蔵量の約20〜25%（世界第1位）を有しています。
かつてはオランダ植民地時代以来、未加工の原鉱石を安価で輸出し、高価な工業製品を逆輸入する「原材料供給国」の地位に甘んじていました。
ジョコ・ウィドド政権下で推進された「Hilirisasi」は、国内での製錬（スメルター）を義務付け、EV（電気自動車）時代のグローバル・サプライチェーンの要衝を握る歴史的転換点となりました。現在は銅、ボーキサイト、スズなど他の重要鉱物へも下流化が拡大されています。"""
    },
    {
        "id": "1233",
        "slug": "level-4-03-wayang-philosophy-modern",
        "title": "【Level 4 (B2)】Filsafat Wayang Kulit dalam Dinamika Demokrasi（影絵劇の善悪葛藤と現代政治思想）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "ユネスコ無形文化遺産「ワヤン・クリ（Wayang Kulit）」。マハーバーラタの善悪相克、道化師プノカワの社会批判、そして現代インドネシアの民主主義と政治対話を読み解く文化哲学論説。",
        "text": """Bagi masyarakat Jawa pada khususnya dan bangsa Indonesia pada umumnya, pertunjukan wayang kulit purwa bukan sekadar seni pertunjukan teatrikal tradisional pengisi malam perayaan, melainkan ensiklopedia falsafah hidup yang sarat dengan diskursus moral, etika kekuasaan, dan psikologi kemanusiaan. Dalam rentang waktu semalam suntuk di bawah pendar lampu blencong, sang dalang menggerakkan lembaran-lembaran kulit kerbau pipih yang diukir rumit, memproyeksikan bayang-bayang dinamis di atas layar kelir putih yang merefleksikan panggung kehidupan alam fana.

Inti dari epik agung Mahabarata yang dipentaskan dalam lakon Baratayuda berkisar pada konflik abadi antara keluarga Pandawa yang dipandang sebagai representasi kebajikan moral, melawan keluarga Kurawa yang kerap diidentikkan dengan watak angkara murka dan keserakahan. Namun, falsafah wayang menolak polarisasi hitam-putih yang simplistis. Tokoh kesatria agung seperti Karna, yang berdiri di pihak Kurawa demi membalas budi dan mempertahankan kehormatan sumpah setianya, memperlihatkan dilema eksistensial yang tragis. Wayang mengajarkan bahwa kebaikan dan keburukan sesungguhnya bersemayam dalam diri setiap insan, dan batas antara keduanya kerap kali kabur dalam pusaran realitas politik.

Dimensi paling revolusioner dalam wayang terletak pada kehadiran Punokawan, yaitu empat serangkai punakawan pengabdi yang dipimpin oleh Semar bersama anak-anaknya: Gareng, Petruk, dan Bagong. Meskipun secara strata sosial mereka digambarkan sebagai rakyat jelata yang berwajah jenaka dan cacat fisik, Semar sesungguhnya adalah manifestasi dewa tertinggi, Batara Ismaya, yang turun ke bumi untuk mendampingi para kesatria. Melalui segmen adegan goro-goro, Punokawan menggunakan humor satir dan lelucon rakyat untuk melontarkan kritik sosial yang tajam terhadap kezaliman para penguasa, sebuah bentuk kontrol demokrasi organik yang telah berakar ratusan tahun sebelum konsep demokrasi modern diadopsi.

Di era kontemporer, kearifan wayang tetap menjadi rujukan filosofis yang sangat relevan dalam membaca dinamika perpolitikan nasional. Para elite politik sering kali menggunakan metafora lakon wayang untuk menyampaikan pesan diplomasi yang bernuansa tinggi, menghindari konfrontasi verbal yang vulgar, serta mencari konsensus damai di balik layar. Dengan memahami filsafat wayang, kita tidak hanya mengapresiasi keindahan estetika warisan adiluhung UNESCO, melainkan juga menyingkap kode-kode kultural yang membentuk pola pikir, etika kepemimpinan, dan kesadaran kolektif bangsa Indonesia.""",
        "paragraphs": [
            ("Bagi masyarakat Jawa pada khususnya dan bangsa Indonesia pada umumnya, pertunjukan wayang kulit purwa bukan sekadar seni pertunjukan teatrikal tradisional pengisi malam perayaan, melainkan ensiklopedia falsafah hidup yang sarat dengan diskursus moral, etika kekuasaan, dan psikologi kemanusiaan. Dalam rentang waktu semalam suntuk di bawah pendar lampu blencong, sang dalang menggerakkan lembaran-lembaran kulit kerbau pipih yang diukir rumit, memproyeksikan bayang-bayang dinamis di atas layar kelir putih yang merefleksikan panggung kehidupan alam fana.",
             "特にジャワ社会、そして広くインドネシア国民にとって、伝統的なワヤン・クリット・プルウォ（影絵芝居）の上演は、祝祭の夜を彩る単なる伝統的な劇場型芸能にとどまらず、道徳的言説、権力の倫理、そして人間心理に満ちた「人生哲学の百科事典」です。ブレンチョンと呼ばれる伝統ココナッツオイルランプの淡い光の下で一晩中繰り広げられる時間の中で、ダラン（人形遣い）は緻密に彫刻された薄い水牛の革人形を動かし、現世（滅びゆく世界）の人生の大舞台を反映する白い布スクリーン（クリール）の上に躍動する影を投影します。",
             "falsafah hidup（人生哲学）、semalam suntuk（一晩中）、sang dalang（ダラン・影絵人形遣い）、alam fana（儚い現世・有限の世界）。"),
            ("Inti dari epik agung Mahabarata yang dipentaskan dalam lakon Baratayuda berkisar pada konflik abadi antara keluarga Pandawa yang dipandang sebagai representasi kebajikan moral, melawan keluarga Kurawa yang kerap diidentikkan dengan watak angkara murka dan keserakahan. Namun, falsafah wayang menolak polarisasi hitam-putih yang simplistis. Tokoh kesatria agung seperti Karna, yang berdiri di pihak Kurawa demi membalas budi dan mempertahankan kehormatan sumpah setianya, memperlihatkan dilema eksistensial yang tragis. Wayang mengajarkan bahwa kebaikan dan keburukan sesungguhnya bersemayam dalam diri setiap insan, dan batas antara keduanya kerap kali kabur dalam pusaran realitas politik.",
             "バラタユダ大戦の演目で演じられる叙事詩『マハーバーラタ』の核心は、道徳的徳の表象とみなされるパンダワ家と、強欲や激しい邪悪さと同一視されがちなクラワ家との間の永遠の葛藤をめぐって展開します。しかしながら、ワヤンの哲学は単純化された白黒二元論の分極化を拒絶します。恩義に報い、忠誠の誓いの名誉を守るためにクラワ側に立つ大戦士カルナのような登場人物は、悲劇的な実存的ジレンマを見せつけます。ワヤンは、善と悪が本来あらゆる人間の内面に宿っており、両者の境界線は政治的現実の渦の中ではしばしば曖昧であることを教えています。",
             "kebajikan moral（道徳的徳）、angkara murka（激しい怒りと邪悪）、polarisasi hitam-putih（白黒二元論）、dilema eksistensial（実存的ジレンマ）。"),
            ("Dimensi paling revolusioner dalam wayang terletak pada kehadiran Punokawan, yaitu empat serangkai punakawan pengabdi yang dipimpin oleh Semar bersama anak-anaknya: Gareng, Petruk, dan Bagong. Meskipun secara strata sosial mereka digambarkan sebagai rakyat jelata yang berwajah jenaka dan cacat fisik, Semar sesungguhnya adalah manifestasi dewa tertinggi, Batara Ismaya, yang turun ke bumi untuk mendampingi para kesatria. Melalui segmen adegan goro-goro, Punokawan menggunakan humor satir dan lelucon rakyat untuk melontarkan kritik sosial yang tajam terhadap kezaliman para penguasa, sebuah bentuk kontrol demokrasi organik yang telah berakar ratusan tahun sebelum konsep demokrasi modern diadopsi.",
             "ワヤンにおける最も革命的な次元は、セマルを筆頭にその子どもたちであるガレン、ペトルック、バゴンからなる4人組の従者「プノカワ（Punokawan）」の存在にあります。社会的階層において彼らは滑稽な顔立ちと身体的特徴を持つ庶民として描かれていますが、セマルは本来、戦士たちに寄り添うために地上へ降臨した最高神バタラ・イスマヤの顕現（化身）なのです。「ゴロゴロ（goro-goro: 天地混乱）」の場面を通じて、プノカワは風刺ユーモアと民衆の冗談を用いて支配者たちの不正や専横に対する痛烈な社会批判を浴びせます。これは、近代的な民主主義の概念が導入される数百年前から根付いていた有機的民主主義コントロールの形態なのです。",
             "Punokawan（道化師・従者の4人組）、rakyat jelata（庶民・一般大衆）、adegan goro-goro（天地動乱・風刺の幕間）、satir（風刺・サタイア）。"),
            ("Di era kontemporer, kearifan wayang tetap menjadi rujukan filosofis yang sangat relevan dalam membaca dinamika perpolitikan nasional. Para elite politik sering kali menggunakan metafora lakon wayang untuk menyampaikan pesan diplomasi yang bernuansa tinggi, menghindari konfrontasi verbal yang vulgar, serta mencari konsensus damai di balik layar. Dengan memahami filsafat wayang, kita tidak hanya mengapresiasi keindahan estetika warisan adiluhung UNESCO, melainkan juga menyingkap kode-kode kultural yang membentuk pola pikir, etika kepemimpinan, dan kesadaran kolektif bangsa Indonesia.",
             "現代においても、ワヤンの知恵は国家の政治力学を読み解く上で極めて示唆に富む哲学的参照点であり続けています。政治エリートたちはしばしばワヤンの演目のメタファーを用いて、高度な含みを持たせた外交メッセージを伝え、下品な直接的言葉の衝突を避け、水面下で平和的な合意（コンセンサス）を模索します。ワヤンの哲学を理解することによって、私たちはユネスコ無形文化遺産の美的至高性を称賛するだけでなく、インドネシア民族の思考様式、指導者倫理、そして集合的無意識を形成している文化的コードを解き明かすことができるのです。",
             "rujukan filosofis（哲学的参照点）、pesan bernuansa tinggi（高尚なニュアンスのメッセージ）、konsensus damai（平和的合意）、kode kultural（文化的コード）。")
        ],
        "vocab": [
            ("ensiklopedia", "名詞", "-", "百科事典、知の全体系", "Kamus ini adalah ensiklopedia bahasa daerah."),
            ("alam fana", "名詞句", "fana", "儚い現世、滅びゆく有限の世界", "Kita hidup sementara di alam fana ini."),
            ("kebajikan", "名詞", "kebajikan", "徳、善行、高潔さ", "Kebajikan hati mengalahkan kejahatan."),
            ("angkara murka", "連語名詞", "-", "激しい邪悪、狂暴な悪意、貪欲", "Raja yang angkara murka akhirnya runtuh."),
            ("polarisasi", "名詞", "-", "二極化、分極化", "Pemilu memicu polarisasi di kalangan masyarakat."),
            ("jelata", "形容詞・名詞", "-", "平民の、庶民の（rakyat jelata）", "Pemimpin itu sangat dekat dengan rakyat jelata."),
            ("satir", "名詞", "-", "風刺、皮肉を込めた批判", "Kartun editorial itu berisi satir politik tajam."),
            ("merujuk", "動詞", "rujuk", "参照する、言及する、典拠とする", "Penulis merujuk pada undang-undang yang berlaku."),
            ("konfrontasi", "名詞", "-", "対決、衝突、対立", "Diplomasi mencegah terjadinya konfrontasi militer."),
            ("menyingkap", "動詞", "singkap", "覆いを取る、解き明かす、暴露する", "Penyelidikan berhasil menyingkap fakta tersembunyi.")
        ],
        "grammar_points": """1. **範囲・属性を表す限定構文 `pada khususnya dan ... pada umumnya`（特に〜、広く一般に〜）**:
   - 議論の適用対象を特殊から一般へと広げる格調高い前置詞構文です。
   - 例: *Bagi generasi muda pada khususnya dan bangsa pada umumnya.*（特に若者世代、そして広く国民全体にとって。）
2. **否定＋形容詞句 `menolak polarisasi yang simplistis`（単純化された二極論を拒絶する）**:
   - 複眼的な学術・評論的論述を展開する際の典型的な語彙選択です。
3. **継続・全体性の表現 `semalam suntuk`（一晩中）**:
   - 時間の完全な持続を表す慣用副詞句です。""",
        "quizzes": [
            ("ジャワの伝統影絵芝居「ワヤン・クリ（Wayang Kulit）」が人生哲学の百科事典と呼ばれる理由は何ですか？",
             ["単なる夜の娯楽にとどまらず、道徳的言説、権力の倫理、人間心理の葛藤が重層的に描かれているため", "文字が読めない子供に算数を教えるための劇だから", "外国の演劇をそのまま翻訳しただけだから"],
             "単なる夜の娯楽にとどまらず、道徳的言説、権力の倫理、人間心理の葛藤が重層的に描かれているため",
             "第1段落に「...bukan sekadar seni pertunjukan teatrikal tradisional pengisi malam perayaan, melainkan ensiklopedia falsafah hidup yang sarat dengan diskursus moral, etika kekuasaan, dan psikologi kemanusiaan.」とあります。"),
            ("ワヤンに登場する道化師「プノカワ（Punokawan）」のリーダーであるセマル（Semar）の真の正体は何ですか？",
             ["王宮を追い出された泥棒", "戦士たちに寄り添うために地上へ降臨した最高神（Batara Ismaya）の顕現", "外国からやってきた商人"],
             "戦士たちに寄り添うために地上へ降臨した最高神（Batara Ismaya）の顕現",
             "第3段落に「...Semar sesungguhnya adalah manifestasi dewa tertinggi, Batara Ismaya, yang turun ke bumi untuk mendampingi para kesatria.」とあります。"),
            ("現代の政治家やエリートがワヤンの演目のメタファー（比喩）を多用する主な理由は何ですか？",
             ["相手を罵倒して喧嘩を売るため", "高尚な含みを持たせて下品な直接衝突を避け、水面下で平和的合意（コンセンサス）を模索するため", "国民にワヤン人形を買わせるため"],
             "高尚な含みを持たせて下品な直接衝突を避け、水面下で平和的合意（コンセンサス）を模索するため",
             "第4段落に「...menyampaikan pesan diplomasi yang bernuansa tinggi, menghindari konfrontasi verbal yang vulgar, serta mencari konsensus damai di balik layar.」とあります。")
        ],
        "culture": """### ユネスコ無形文化遺産「Wayang Kulit」とジャワの深層心理
2003年、ユネスコは「ワヤン・クリット人形劇」を「人類の口承及び無形遺産の傑作」に宣言しました。
人形遣い「Dalang（ダラン）」は単なる操り手ではなく、語り部、歌手、ガムラン合奏団の指揮者、道徳の教師、そして時に神霊を降ろす呪術的司祭としての役割を一人でこなします。
白黒で割り切れない複雑な人間関係や、「Alus（高雅・洗練）」と「Kasar（粗野・直情）」の均衡を尊ぶ美意識は、インドネシアの政治的リーダーシップや日常の対人関係（Toleransi）の根底に今なお息づいています。"""
    },
    {
        "id": "1234",
        "slug": "level-4-04-startup-bubble-burst",
        "title": "【Level 4 (B2)】Musim Dingin Startup dan Matangnya Ekosistem Digital（テックバブル崩壊と堅実経営への転換）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "巨額の資金燃焼（Bakar Uang）とユニコーン誕生に沸いた東南アジアのデジタル経済。世界的金融引き締めによる「テック・ウィンター」を経て、収益性と堅実経営へと成熟する転換期を分析。",
        "text": """Sepanjang dekade 2010-an, ekosistem ekonomi digital Indonesia melesat bagai meteor, mencuri perhatian para pemodal ventura global. Didorong oleh penetrasi telepon pintar yang masif dan populasi usia muda yang melek teknologi, lahir sejumlah perusahaan rintisan berstatus unicorn bahkan decacorn yang mendisrupsi sektor transportasi, niaga elektronik, perjalanan, hingga teknologi finansial. Pada masa kejayaan tersebut, narasi pertumbuhan pengguna menjadi satu-satunya mantra keramat, memicu fenomena bakar uang gila-gilaan berupa promo diskon besar-besaran demi mengunci pangsa pasar dominan.

Namun, pesta likuiditas modal ventura yang berlimpah itu terhenti secara mendadak ketika lanskap makroekonomi global berbalik arah. Kenaikan suku bunga acuan bank sentral Amerika Serikat yang agresif untuk menjinakkan inflasi pascapandemi memicu arus modal keluar dari pasar negara berkembang. Fenomena yang dikenal luas sebagai musim dingin perusahaan rintisan (tech winter) ini menyapu kawasan Asia Tenggara. Akses permodalan mengering seketika, valuasi perusahaan yang melambung tinggi dikoreksi secara tajam, dan gelombang pemutusan hubungan kerja (PHK) massal terpaksa diambil demi memperpanjang napas operasional perusahaan.

Kendatipun terasa pahit dan mengguncang ribuan talenta digital, krisis likuiditas ini sesungguhnya menjadi katalis penting bagi proses pendewasaan ekosistem digital nasional. Alih-alih mengejar pertumbuhan pengguna yang semu tanpa perhitungan biaya, para pendiri startup kini beralih fokus secara radikal pada perbaikan ekonomi unit (unit economics) dan pencapaian profitabilitas yang berkelanjutan. Model bisnis yang rapuh dan hanya bertumpu pada subsidi investor tersingkir dari gelanggang kompetisi secara seleksi alamiah.

Transformasi struktural ini membuktikan bahwa ekonomi digital Indonesia tengah berevolusi dari fase euforia menuju fase kematangan. Startup generasi baru kini lahir dengan mentalitas yang jauh lebih tangguh, berfokus memecahkan masalah riil di sektor-sektor esensial seperti logistik rantai pasok agrikultur, teknologi kesehatan preventif, dan digitalisasi usaha mikro di daerah terpencil. Masa depan digital nusantara tidak lagi ditentukan oleh seberapa deras modal asing yang dibakar, melainkan seberapa kokoh nilai fundamental yang mampu diciptakan bagi masyarakat luas.""",
        "paragraphs": [
            ("Sepanjang dekade 2010-an, ekosistem ekonomi digital Indonesia melesat bagai meteor, mencuri perhatian para pemodal ventura global. Didorong oleh penetrasi telepon pintar yang masif dan populasi usia muda yang melek teknologi, lahir sejumlah perusahaan rintisan berstatus unicorn bahkan decacorn yang mendisrupsi sektor transportasi, niaga elektronik, perjalanan, hingga teknologi finansial. Pada masa kejayaan tersebut, narasi pertumbuhan pengguna menjadi satu-satunya mantra keramat, memicu fenomena bakar uang gila-gilaan berupa promo diskon besar-besaran demi mengunci pangsa pasar dominan.",
             "2010年代を通じて、インドネシアのデジタル経済エコシステムは流星のように疾走し、世界のベンチャーキャピタル投資家たちの注目を奪い去りました。スマートフォンの爆発的普及とテクノロジーに精通した若年人口に後押しされ、交通、電子商取引（EC）、旅行、そしてフィンテック業界を破壊的創造（ディスラプト）するユニコーンやデカコーン企業が次々と誕生しました。その栄光の時代には、ユーザー数の拡大という物語が唯一無二の神聖な呪文となり、圧倒的な市場シェアを囲い込むための大幅な割引プロモーションという途方もない「資金燃焼（キャッシュバーン／bakar uang）」現象を引き起こしました。",
             "melesat bagai meteor（流星のように急成長する）、pemodal ventura（ベンチャーキャピタル）、melek teknologi（テクノロジーリテラシーのある）、mendisrupsi（ディスラプトする・破壊的革新を起こす）、bakar uang（キャッシュバーン・資金燃焼）。"),
            ("Namun, pesta likuiditas modal ventura yang berlimpah itu terhenti secara mendadak ketika lanskap makroekonomi global berbalik arah. Kenaikan suku bunga acuan bank sentral Amerika Serikat yang agresif untuk menjinakkan inflasi pascapandemi memicu arus modal keluar dari pasar negara berkembang. Fenomena yang dikenal luas sebagai musim dingin perusahaan rintisan (tech winter) ini menyapu kawasan Asia Tenggara. Akses permodalan mengering seketika, valuasi perusahaan yang melambung tinggi dikoreksi secara tajam, dan gelombang pemutusan hubungan kerja (PHK) massal terpaksa diambil demi memperpanjang napas operasional perusahaan.",
             "しかし、潤沢なベンチャーキャピタルの流動性の宴は、世界のマクロ経済情勢が反転した瞬間に突如として幕を閉じました。パンデミック後のインフレを鎮静化するための米連邦準備制度理事会（FRB）による積極的な政策金利引き上げは、新興国市場からの資本流出を引き起こしました。「テック・ウィンター（スタートアップの冬）」として広く知られるこの現象は、東南アジア全域を吹き荒れました。資金調達へのアクセスは一瞬で枯渇し、吊り上がっていた企業評価額（バリュエーション）は急激に下方修正され、企業の事業継続期間を延ばすために大規模な人員削減（PHK）の嵐が余儀なくされたのです。",
             "pesta likuiditas（流動性の宴）、suku bunga acuan（政策金利）、tech winter（テック・ウィンター・IT不況）、pemutusan hubungan kerja / PHK（解雇・人員削減）。"),
            ("Kendatipun terasa pahit dan mengguncang ribuan talenta digital, krisis likuiditas ini sesungguhnya menjadi katalis penting bagi proses pendewasaan ekosistem digital nasional. Alih-alih mengejar pertumbuhan pengguna yang semu tanpa perhitungan biaya, para pendiri startup kini beralih fokus secara radikal pada perbaikan ekonomi unit (unit economics) dan pencapaian profitabilitas yang berkelanjutan. Model bisnis yang rapuh dan hanya bertumpu pada subsidi investor tersingkir dari gelanggang kompetisi secara seleksi alamiah.",
             "何千人ものデジタル人材に打撃を与え苦渋に満ちたものであったにもかかわらず、この流動性危機は、実際には国のデジタルエコシステムの成熟プロセスにとって極めて重要な触媒となりました。コスト計算を度外視した見せかけのユーザー獲得を追う代わりに、スタートアップの創業者たちは今やユニットエコノミクスの改善と持続可能な収益性（プロフィタビリティ）の達成へと抜本的に舵を切りました。脆弱で投資家の補助金だけに依存していたビジネスモデルは、自然淘汰によって競争のリングから姿を消したのです。",
             "katalis pendewasaan（成熟への触媒）、alih-alih（〜する代わりに）、ekonomi unit（ユニットエコノミクス・単位当たり採算）、seleksi alamiah（自然淘汰）。"),
            ("Transformasi struktural ini membuktikan bahwa ekonomi digital Indonesia tengah berevolusi dari fase euforia menuju fase kematangan. Startup generasi baru kini lahir dengan mentalitas yang jauh lebih tangguh, berfokus memecahkan masalah riil di sektor-sektor esensial seperti logistik rantai pasok agrikultur, teknologi kesehatan preventif, dan digitalisasi usaha mikro di daerah terpencil. Masa depan digital nusantara tidak lagi ditentukan oleh seberapa deras modal asing yang dibakar, melainkan seberapa kokoh nilai fundamental yang mampu diciptakan bagi masyarakat luas.",
             "この構造的変革は、インドネシアのデジタル経済が熱狂（ユーフォリア）のフェーズから成熟のフェーズへと進化を遂げつつあることを証明しています。新世代のスタートアップは、農業サプライチェーン物流、予防医療テクノロジー、僻地の零細事業者デジタル化といった本質的セクターにおける現実の課題解決にフォーカスした、遥かに強靭なメンタリティを持って誕生しています。列島のデジタルの未来は、どれほど多くの外資を燃やしたかではなく、社会全体のためにどれほど強固なファンダメンタルズ（本質的価値）を創出できたかによって決定づけられるのです。",
             "fase euforia menuju kematangan（熱狂から成熟へのフェーズ）、sektor esensial（不可欠な基幹部門）、nilai fundamental（本質的価値・ファンダメンタルズ）。")
        ],
        "vocab": [
            ("melesat", "動詞", "lesat", "急上昇する、猛スピードで飛ぶ", "Ekonomi digital melesat pesat."),
            ("pemodal", "名詞", "modal", "投資家、出資者", "Pemodal menanamkan dana pada teknologi hijau."),
            ("disrupsi", "名詞", "-", "破壊的変革、ディスラプション", "Teknologi AI membawa disrupsi di dunia kerja."),
            ("likuiditas", "名詞", "-", "流動性、資金の流通性", "Bank menjaga likuiditas agar tetap stabil."),
            ("menjinakkan", "動詞", "jinak", "手なずける、鎮める、抑制する", "Pemerintah berupaya menjinakkan laju inflasi."),
            ("katalis", "名詞", "-", "触媒、変化を促す刺激", "Pandemi menjadi katalis transformasi digital."),
            ("semu", "形容詞", "-", "見せかけの、偽りの、実態のない", "Kemenangan semu itu tidak bertahan lama."),
            ("profitabilitas", "名詞", "-", "収益性、プロフィタビリティ", "Perusahaan fokus pada profitabilitas jangka panjang."),
            ("tersingkir", "動詞（受動）", "singkir", "排除される、脱落する、締め出される", "Tim itu tersingkir dari babak semifinal."),
            ("euforia", "名詞", "-", "熱狂、陶酔感、高揚感", "Euforia kemenangan menyelimuti seluruh stadion.")
        ],
        "grammar_points": """1. **代替・転換を表す接続詞 `Alih-alih ..., justru / malah ...`（〜する代わりに）**:
   - 誤った行動や旧来の慣習を否定し、真に取るべき行動を対置する論理構文です。
   - 例: *Alih-alih mengeluh, ia justru bekerja lebih keras.*（不平を言う代わりに、彼はむしろ一層懸命に働いた。）
2. **比喩的副詞表現 `melesat bagai meteor`（流星のように急伸する）**:
   - 驚異的な速度を文学的・修辞的に描写する格調高い比喩です。
3. **推移・変化を表す前置詞句 `dari fase ... menuju fase ...`（〜のフェーズから〜のフェーズへ）**:
   - 発展段階の移行を明確に提示する分析的表現です。""",
        "quizzes": [
            ("2010年代のインドネシア・スタートアップ業界で圧倒的市場シェアを獲得するために行われていた「bakar uang」とはどのような現象ですか？",
             ["文字通りオフィスで紙幣を焼却する儀式", "巨額の割引やプロモーションに投資家の資金を大量投入する資金燃焼（キャッシュバーン）競争", "偽札を処分するための法律"],
             "巨額の割引やプロモーションに投資家の資金を大量投入する資金燃焼（キャッシュバーン）競争",
             "第1段落に「...memicu fenomena bakar uang gila-gilaan berupa promo diskon besar-besaran demi mengunci pangsa pasar dominan.」とあります。"),
            ("東南アジア全域を襲った「テック・ウィンター（Tech Winter）」の主たる引き金となった世界経済の要因は何ですか？",
             ["インフレ抑制のための米連邦準備制度による積極的な政策金利引き上げと新興国からの資本流出", "スマートフォンの生産が世界中で中止されたこと", "海底光ケーブルの断線事故"],
             "インフレ抑制のための米連邦準備制度による積極的な政策金利引き上げと新興国からの資本流出",
             "第2段落に「Kenaikan suku bunga acuan bank sentral Amerika Serikat yang agresif untuk menjinakkan inflasi pascapandemi memicu arus modal keluar dari pasar negara berkembang.」とあります。"),
            ("テック・ウィンターを経て新世代のスタートアップが最も重視するようになった経営方針は何ですか？",
             ["見せかけのユーザー数ではなく、ユニットエコノミクス（単位当たり採算）の改善と持続可能な収益性の確立", "さらに多額の外国資金を燃やすこと", "すべての事業を海外へ売却すること"],
             "見せかけのユーザー数ではなく、ユニットエコノミクス（単位当たり採算）の改善と持続可能な収益性の確立",
             "第3段落に「...beralih fokus secara radikal pada perbaikan ekonomi unit (unit economics) dan pencapaian profitabilitas yang berkelanjutan.」とあります。")
        ],
        "culture": """### 東南アジアのデジタル大国と「Tech Winter」の教訓
インドネシアは、Gojek（配車・スーパーアプリ）、Tokopedia（EC）、Bukalapak（EC）、Traveloka（オンライン旅行）、OVO（決済）、J&T Express（物流）など、東南アジアで最も多くのユニコーン企業を輩出してきました。
しかし2022年以降の世界的「Tech Winter」により、単なるGMV（流通取引総額）の拡大から、確固たるEBITDA（営業利益）の創出へと経営パラダイムが劇的にシフトしました。
この淘汰を経て、現在では農業（Agritech）や医療、気候変動テクノロジー（Climatetech）など、国家の構造的課題に直結する骨太なスタートアップが次々と台頭しています。"""
    },
    {
        "id": "1235",
        "slug": "level-4-05-peatland-restoration",
        "title": "【Level 4 (B2)】Restorasi Lahan Gambut Demi Bumi yang Lestari（泥炭湿原再生と炭素クレジットの最前線）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "火災による煙害（Haze）と温室効果ガスの大量排出をもたらした泥炭湿原の乾燥化。3R戦略（再湿地化・植生再生・地域生計向上）と国際炭素市場の挑戦を描く環境科学論説。",
        "text": """Lahan gambut tropis Indonesia, yang terbentang luas di wilayah Sumatra, Kalimantan, dan Papua, merupakan salah satu ekosistem paling krusial sekaligus rentan di muka bumi. Terbentuk dari timbunan sisa-sisa vegetasi purba yang membusuk secara parsial di lingkungan kedap udara selama ribuan tahun, kubah-kubah gambut ini menyimpan cadangan karbon terestrial raksasa. Keberadaannya berfungsi sebagai spons hidrologis raksasa yang menyerap limpasan air hujan di musim basah dan melepaskannya secara perlahan di musim kemarau, menjaga keseimbangan mikroklimat pulau-pulau nusantara.

Malapetaka ekologis bermula ketika proyek-proyek drainase masif di masa lalu membuka kanal-kanal buatan sedalam beberapa meter untuk mengeringkan rawa gambut demi ekspansi perkebunan monokultur skala besar. Pengeringan air menyebabkan lapisan gambut teroksidasi, menyusut, dan kehilangan kelembapan alaminya hingga menjadi bahan bakar yang sangat mudah tersulut api. Pada puncak musim kemarau panjang yang dipicu oleh anomali iklim El Niño, kebakaran hutan dan lahan (karhutla) bawah tanah membakar lapisan gambut sedalam beberapa meter, melepaskan miliaran ton karbon dioksida ke atmosfer serta memicu kabut asap lintas batas (transboundary haze) yang melumpuhkan aktivitas ekonomi dan meracuni jutaan paru-paru manusia di Asia Tenggara.

Menyikapi krisis berkepanjangan ini, dibentuklah Badan Restorasi Gambut dan Mangrove (BRGM) dengan mandat melaksanakan strategi terpadu yang dikenal sebagai pendekatan 3R: Rewetting (pembasahan kembali), Revegetation (penanaman kembali vegetasi asli), dan Revitalization (revitalisasi mata pencaharian masyarakat lokal). Rewetting diwujudkan dengan menyekat ribuan kanal pengering menggunakan bendungan kayu dan timbunan tanah agar tinggi muka air tanah kembali mendekati permukaan. Bersamaan dengan itu, bibit pohon endemik seperti ramin, jelutung, dan belangeran ditanam untuk merehabilitasi tutupan tajuk hutan yang rusak.

Kunci keberlanjutan dari seluruh ikhtiar restorasi ini bertumpu pada dimensi sosial-ekonomi. Tanpa menghadirkan alternatif penghasilan yang layak bagi masyarakat pedesaan yang hidup di sekitar kubah gambut, godaan untuk membakar lahan demi pembukaan kebun akan terus berulang. Oleh karena itu, pengembangan paludikultur—yaitu budi daya komoditas bernilai ekonomi tinggi di lahan basah tanpa mengeringkan air, seperti sagu, nanas rawa, dan perikanan air tawar—kini digabungkan dengan skema pasar karbon internasional. Menjaga gambut tetap basah bukan lagi beban pengeluaran, melainkan investasi hijau yang mampu mendatangkan dividen ekologis dan finansial demi masa depan bumi.""",
        "paragraphs": [
            ("Lahan gambut tropis Indonesia, yang terbentang luas di wilayah Sumatra, Kalimantan, dan Papua, merupakan salah satu ekosistem paling krusial sekaligus rentan di muka bumi. Terbentuk dari timbunan sisa-sisa vegetasi purba yang membusuk secara parsial di lingkungan kedap udara selama ribuan tahun, kubah-kubah gambut ini menyimpan cadangan karbon terestrial raksasa. Keberadaannya berfungsi sebagai spons hidrologis raksasa yang menyerap limpasan air hujan di musim basah dan melepaskannya secara perlahan di musim kemarau, menjaga keseimbangan mikroklimat pulau-pulau nusantara.",
             "スマトラ、カリマンタン、パプア地域に広大に広がるインドネシアの熱帯泥炭湿原（Lahan Gambut）は、地球上で最も決定的に重要であると同時に最も脆弱な生態系の一つです。数千年にわたり空気が遮断された嫌気的環境で部分的に腐敗した古代の植物遺骸の堆積物から形成されたこれらの泥炭ドームは、莫大な陸上炭素貯留量を蓄えています。その存在は巨大な水文学的スポンジとして機能し、雨季には雨水の流出を吸収し、乾季にはそれをゆっくりと放出することで、列島諸島の微気候の均衡を維持しています。",
             "lahan gambut tropis（熱帯泥炭湿原）、kedap udara（空気が遮断された・嫌気性の）、kubah gambut（泥炭ドーム）、spons hidrologis（水文学的スポンジ・保水緩衝体）。"),
            ("Malapetaka ekologis bermula ketika proyek-proyek drainase masif di masa lalu membuka kanal-kanal buatan sedalam beberapa meter untuk mengeringkan rawa gambut demi ekspansi perkebunan monokultur skala besar. Pengeringan air menyebabkan lapisan gambut teroksidasi, menyusut, dan kehilangan kelembapan alaminya hingga menjadi bahan bakar yang sangat mudah tersulut api. Pada puncak musim kemarau panjang yang dipicu oleh anomali iklim El Niño, kebakaran hutan dan lahan (karhutla) bawah tanah membakar lapisan gambut sedalam beberapa meter, melepaskan miliaran ton karbon dioksida ke atmosfer serta memicu kabut asap lintas batas (transboundary haze) yang melumpuhkan aktivitas ekonomi dan meracuni jutaan paru-paru manusia di Asia Tenggara.",
             "生態学的災厄は、過去の大規模排水事業が大規模モノカルチャー農園の拡大のために泥炭湿原を乾燥させようと深さ数メートルの人工水路（運河）を開削したときに始まりました。水の排水は泥炭層を酸化・収縮させ、その自然な湿潤性を失わせて極めて引火しやすい燃料へと変貌させました。エルニーニョ気候変動によって引き起こされた長期乾季のピーク時には、地下深部での森林・泥炭火災（Karhutla）が数メートルの深さまで泥炭層を焼き尽くし、大気中に数十億トンの二酸化炭素を放出するとともに、東南アジアの経済活動を麻痺させ何百万もの人々の肺を毒する越境煙害（ヘイズ）を引き起こしたのです。",
             "malapetaka ekologis（生態学的惨事）、drainase masif（大規模排水・水抜き）、mudah tersulut api（極めて引火しやすい）、kebakaran hutan dan lahan / karhutla（森林泥炭火災）、kabut asap lintas batas（越境煙害ヘイズ）。"),
            ("Menyikapi krisis berkepanjangan ini, dibentuklah Badan Restorasi Gambut dan Mangrove (BRGM) dengan mandat melaksanakan strategi terpadu yang dikenal sebagai pendekatan 3R: Rewetting (pembasahan kembali), Revegetation (penanaman kembali vegetasi asli), dan Revitalization (revitalisasi mata pencaharian masyarakat lokal). Rewetting diwujudkan dengan menyekat ribuan kanal pengering menggunakan bendungan kayu dan timbunan tanah agar tinggi muka air tanah kembali mendekati permukaan. Bersamaan dengan itu, bibit pohon endemik seperti ramin, jelutung, dan belangeran ditanam untuk merehabilitasi tutupan tajuk hutan yang rusak.",
             "この長期化する危機に対処するため、「泥炭・マングローブ再生庁（BRGM）」が設立され、「3Rアプローチ」として知られる統合戦略を実行する任務が課されました。すなわち、Rewetting（再湿潤化）、Revegetation（在来植生の再植林）、そしてRevitalization（地元住民の生計再生）です。再湿潤化は、地下水位が再び地表近くに戻るよう、木製ダムや土嚢を用いて何千もの排水水路を遮断（キャナル・ブロッキング）することによって具現化されました。それと並行して、破壊された森林の樹冠被覆を修復するために、ラミン、ジェルツン、ブランゲランといった固有種の苗木が植樹されました。",
             "Badan Restorasi Gambut（泥炭再生庁・BRGM）、pendekatan 3R（3Rアプローチ）、menyekat kanal（水路を遮断する）、tutupan tajuk hutan（林冠被覆）。"),
            ("Kunci keberlanjutan dari seluruh ikhtiar restorasi ini bertumpu pada dimensi sosial-ekonomi. Tanpa menghadirkan alternatif penghasilan yang layak bagi masyarakat pedesaan yang hidup di sekitar kubah gambut, godaan untuk membakar lahan demi pembukaan kebun akan terus berulang. Oleh karena itu, pengembangan paludikultur—yaitu budi daya komoditas bernilai ekonomi tinggi di lahan basah tanpa mengeringkan air, seperti sagu, nanas rawa, dan perikanan air tawar—kini digabungkan dengan skema pasar karbon internasional. Menjaga gambut tetap basah bukan lagi beban pengeluaran, melainkan investasi hijau yang mampu mendatangkan dividen ekologis dan finansial demi masa depan bumi.",
             "この再生のあらゆる取り組みの持続可能性の鍵は、社会経済的側面に依拠しています。泥炭ドームの周辺に暮らす農村社会に対して適切な代替所得手段を提示しなければ、農地開墾のために火を放つ誘惑は何度も繰り返されることになります。それゆえに、水を抜くことなく湿地でサゴヤシ、湿地パイナップル、淡水養殖といった経済的価値の高い作物を栽培する「パルディカルチャー（湿地農業）」の開発が、現在では国際炭素市場スキームと統合されています。泥炭地を湿潤に保つことはもはや経費の重荷ではなく、地球の未来のために環境的・金融的配当をもたらしうるグリーン投資となっているのです。",
             "bertumpu pada...（〜に依拠する・かかっている）、paludikultur（パルディカルチャー・湿原保全型農業）、pasar karbon internasional（国際炭素取引市場）、dividen ekologis（生態学的配当）。")
        ],
        "vocab": [
            ("rentan", "形容詞", "-", "脆弱な、影響を受けやすい、傷つきやすい", "Kawasan pesisir rentan terhadap abrasi air laut."),
            ("malapetaka", "名詞", "-", "災厄、大惨事、破滅", "Kekeringan panjang membawa malapetaka bagi petani."),
            ("tersulut", "動詞（受動）", "sulut", "点火される、火がつく、燃え上がる", "Rumput kering tersulut puntung rokok."),
            ("anomali", "名詞", "-", "異常、変則、アノマリー", "Anomali cuaca menyebabkan hujan di musim kemarau."),
            ("mandat", "名詞", "-", "委任、命令、任務の付与", "Lembaga ini menerima mandat menjaga kelestarian."),
            ("menyekat", "動詞", "sekat", "遮断する、堰き止める、仕切る", "Warga menyekat saluran air untuk mencegah banjir."),
            ("rehabilitasi", "名詞", "-", "修復、再生、リハビリテーション", "Rehabilitasi hutan mangrove terus dilakukan."),
            ("ikhtiar", "名詞", "-", "努力、試み、尽力", "Segala ikhtiar dilakukan untuk memadamkan api."),
            ("budi daya", "名詞句", "-", "栽培、養殖、育成", "Budi daya ikan air tawar menguntungkan."),
            ("dividen", "名詞", "-", "配当、利益の分配", "Investasi hijau memberikan dividen jangka panjang.")
        ],
        "grammar_points": """1. **分詞構文による成因説明 `Terbentuk dari ...`（〜から形成され）**:
   - 文頭に過去分詞（受動態）を置き、主語の起源や属性を簡潔かつ重厚に記述する学術構文です。
   - 例: *Terbentuk dari endapan ribuan tahun, tanah ini sangat subur.*（数千年の堆積から形成され、この土壌は極めて肥沃である。）
2. **否定＋動名詞節 `tanpa mengeringkan air`（水を抜くことなく）**:
   - 手段や条件の否定を表す前置詞構文です。
   - 例: *Bercocok tanam tanpa merusak alam.*（自然を破壊することなく農耕を行う。）
3. **対比構文 `bukan lagi beban pengeluaran, melainkan investasi`（もはや支出の負担ではなく、投資である）**:
   - 概念の根本的転換（パラダイムシフト）を強調する論説表現です。""",
        "quizzes": [
            ("インドネシアの熱帯泥炭湿原（Lahan Gambut）が持つ地球環境上の決定的な役割は何ですか？",
             ["砂漠化を促進して観光客を呼ぶこと", "莫大な陸上炭素を貯留し、巨大なスポンジとして雨水流出を調節して気候均衡を保つこと", "塩分を吸収して海水を真水に変えること"],
             "莫大な陸上炭素を貯留し、巨大なスポンジとして雨水流出を調節して気候均衡を保つこと",
             "第1段落に「...kubah-kubah gambut ini menyimpan cadangan karbon terestrial raksasa. Keberadaannya berfungsi sebagai spons hidrologis raksasa...」とあります。"),
            ("過去に泥炭地で頻発した大規模な森林火災（Karhutla）と越境煙害（Haze）の根本原因は何でしたか？",
             ["宇宙からの隕石の落下", "大規模農園拡大のために人工水路を開削して泥炭地を乾燥させ、極めて燃えやすい状態にしたこと", "川の魚が多すぎたこと"],
             "大規模農園拡大のために人工水路を開削して泥炭地を乾燥させ、極めて燃えやすい状態にしたこと",
             "第2段落に「...proyek-proyek drainase masif... membuka kanal-kanal buatan... untuk mengeringkan rawa gambut... kehilangan kelembapan alaminya hingga menjadi bahan bakar yang sangat mudah tersulut api.」とあります。"),
            ("泥炭地を乾燥させることなく、湿潤な状態のままサゴヤシや湿地作物を栽培して住民の生計を支える農業手法を何と呼びますか？",
             ["水耕栽培（Hydroponics）", "パルディカルチャー（Paludikultur）", "焼畑農業（Ladang Berpindah）"],
             "パルディカルチャー（Paludikultur）",
             "第4段落に「...pengembangan paludikultur—yaitu budi daya komoditas bernilai ekonomi tinggi di lahan basah tanpa mengeringkan air, seperti sagu...」とあります。")
        ],
        "culture": """### 「Lahan Gambut」と越境煙害（Haze）対策の最前線
インドネシアには世界最大規模（約1,300〜1,500万ヘクタール）の熱帯泥炭湿原が存在します。
1990年代のメガ・ライス・プロジェクト（100万ヘクタール水田開発計画）などで無数の排水運河が掘削された結果、乾燥化した泥炭が自然発火し、シンガポールやマレーシアまで覆う「Haze（ヘイズ）」公害が国際問題となりました。
現在では泥炭再生庁（BRGM）による「水路遮断（Canal Blocking）」と「湿原保全型農業（Paludiculture）」が進められ、世界最大の炭素吸収源（カーボンシンク）として国連や国際炭素市場から巨額の環境投資が集まっています。"""
    },
    {
        "id": "1236",
        "slug": "level-4-06-halal-lifestyle-industry",
        "title": "【Level 4 (B2)】Transformasi Industri Halal Indonesia di Kancah Global（世界をリードするハラール経済圏）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "人口2億3,000万人のムスリム市場を背景に、単なる宗教的義務から一大グローバル産業へ進化したハラール経済。シャリア金融、モデストファッション、ハラール化粧品の革新を追う。",
        "text": """Dengan populasi muslim terbesar di dunia yang melampaui dua ratus tiga puluh juta jiwa, Indonesia telah lama dipandang sebagai pasar konsumen produk halal yang paling menggiurkan bagi korporasi multinasional. Namun, dalam lanskap ekonomi global kontemporer, Indonesia tidak lagi berpuas diri menjadi sekadar pasar sasaran konsumtif. Melalui visi strategis Masterplan Ekonomi Syariah Indonesia, bangsa ini tengah bertransformasi secara agresif menjadi produsen utama dan pusat gravitasi ekonomi halal dunia, membalikkan arus perdagangan dari impor menuju kepemimpinan rantai nilai global.

Evolusi konsep halal di masyarakat modern telah meluas jauh melampaui batasan ritual keagamaan tradisional yang semata-mata mengatur kehalalan penyembelihan daging dan ketiadaan unsur babi atau alkohol. Halal kini telah bermetamorfosis menjadi sinonim dari gaya hidup holistik (halal lifestyle) yang mengedepankan prinsip kebersihan prima, keselamatan biologis, keberlanjutan lingkungan, dan keadilan etis dalam rantai pasok. Nilai-nilai universal thoyyib (kebaikan dan kualitas unggul) ini memikat konsumen lintas agama dan bangsa yang mengutamakan kesehatan dan integritas produk yang mereka konsumsi.

Di sektor industri manufaktur, akselerasi ini tercermin nyata dalam dominasi kosmetik halal lokal yang memadukan riset bioteknologi modern dengan bahan-bahan alami bebas kekejaman hewani (cruelty-free). Produk kosmetik dan perawatan kulit buatan anak negeri kini merajai pangsa pasar domestik dan diekspor hingga ke Timur Tengah dan Afrika. Sementara itu, di panggung mode, tren busana santun (modest fashion) karya perancang Indonesia berhasil menembus pekan mode bergengsi di Paris, London, dan New York, membuktikan bahwa identitas keagamaan mampu berpadu selaras dengan estetika adibusana kelas dunia.

Penguatan ekosistem riil ini diakselerasi oleh konsolidasi sektor keuangan syariah melalui merger bank-bank syariah milik negara menjadi Bank Syariah Indonesia (BSI), yang kini masuk dalam jajaran bank berkapitalisasi pasar terbesar di tanah air. Dengan kewajiban sertifikasi halal nasional yang terintegrasi secara digital melalui Badan Penyelenggara Jaminan Produk Halal (BPJPH), Indonesia memantapkan langkahnya bukan hanya sebagai penonton, melainkan sebagai penentu standar dan poros peradaban ekonomi syariah global yang inklusif dan berkelanjutan.""",
        "paragraphs": [
            ("Dengan populasi muslim terbesar di dunia yang melampaui dua ratus tiga puluh juta jiwa, Indonesia telah lama dipandang sebagai pasar konsumen produk halal yang paling menggiurkan bagi korporasi multinasional. Namun, dalam lanskap ekonomi global kontemporer, Indonesia tidak lagi berpuas diri menjadi sekadar pasar sasaran konsumtif. Melalui visi strategis Masterplan Ekonomi Syariah Indonesia, bangsa ini tengah bertransformasi secara agresif menjadi produsen utama dan pusat gravitasi ekonomi halal dunia, membalikkan arus perdagangan dari impor menuju kepemimpinan rantai nilai global.",
             "2億3,000万人を超える世界最大のイスラム教徒人口を擁するインドネシアは、多国籍企業にとって最も魅力的なハラール製品の消費者市場として長年見なされてきました。しかし、現代のグローバル経済の景観において、インドネシアはもはや単なる消費の標的市場であり続けることに甘んじてはいません。「インドネシア・シャリア経済マスタープラン」の戦略的ビジョンを通じて、この国は主要な生産国、そして世界のハラール経済の重力の中心へと攻撃的に変貌を遂げつつあり、輸入依存からグローバル・バリューチェーンのリーダーシップへと貿易の流れを逆転させています。",
             "populasi muslim terbesar（世界最大のイスラム教徒人口）、pasar menggiurkan（魅力的な市場）、pusat gravitasi（重力の中心・ハブ）、kepemimpinan rantai nilai（バリューチェーンの主導権）。"),
            ("Evolusi konsep halal di masyarakat modern telah meluas jauh melampaui batasan ritual keagamaan tradisional yang semata-mata mengatur kehalalan penyembelihan daging dan ketiadaan unsur babi atau alkohol. Halal kini telah bermetamorfosis menjadi sinonim dari gaya hidup holistik (halal lifestyle) yang mengedepankan prinsip kebersihan prima, keselamatan biologis, keberlanjutan lingkungan, dan keadilan etis dalam rantai pasok. Nilai-nilai universal thoyyib (kebaikan dan kualitas unggul) ini memikat konsumen lintas agama dan bangsa yang mengutamakan kesehatan dan integritas produk yang mereka konsumsi.",
             "現代社会におけるハラールの概念の進化は、肉の屠殺の適法性や豚・アルコール成分の不在を単に規定する伝統的な宗教儀礼の境界をはるかに超えて拡大しました。ハラールは今や、最高度の衛生原則、生物学的安全性、環境の持続可能性、そしてサプライチェーンにおける倫理的公正さを前面に打ち出した「全人的ライフスタイル（halal lifestyle）」の同義語へと変貌を遂げました。「トイーブ（善性と卓越した品質）」というこの普遍的価値は、自らが消費する製品の健康と完全性を重視する、宗教や国境を越えた消費者たちを魅了しています。",
             "gaya hidup holistik（ホリスティック・包括的ライフスタイル）、kebersihan prima（卓越した衛生度）、keadilan etis（倫理的公正さ）、nilai-nilai thoyyib（善良で高品質な価値）。"),
            ("Di sektor industri manufaktur, akselerasi ini tercermin nyata dalam dominasi kosmetik halal lokal yang memadukan riset bioteknologi modern dengan bahan-bahan alami bebas kekejaman hewani (cruelty-free). Produk kosmetik dan perawatan kulit buatan anak negeri kini merajai pangsa pasar domestik dan diekspor hingga ke Timur Tengah dan Afrika. Sementara itu, di panggung mode, tren busana santun (modest fashion) karya perancang Indonesia berhasil menembus pekan mode bergengsi di Paris, London, dan New York, membuktikan bahwa identitas keagamaan mampu berpadu selaras dengan estetika adibusana kelas dunia.",
             "製造業セクターにおいて、この加速は、現代のバイオテクノロジー研究と動物実験を行わない天然原料（クルエルティフリー）を融合させた国産ハラール化粧品の覇権に顕著に反映されています。国産の化粧品やスキンケア製品は今や国内市場シェアを席巻し、中東やアフリカへも輸出されています。一方、ファッション界では、インドネシア人デザイナーによる「モデスト・ファッション（控えめでお洒落なイスラム服飾）」のトレンドがパリ、ロンドン、ニューヨークの名門ファッションウィークに進出を果たし、宗教的アイデンティティが世界水準のオートクチュール美学と見事に調和できることを証明しました。",
             "bebas kekejaman hewani / cruelty-free（動物実験なし）、merajai pangsa pasar（市場シェアを席巻する）、busana santun / modest fashion（控えめで上品なイスラムファッション）、adibusana（オートクチュール・高級服飾）。"),
            ("Penguatan ekosistem riil ini diakselerasi oleh konsolidasi sektor keuangan syariah melalui merger bank-bank syariah milik negara menjadi Bank Syariah Indonesia (BSI), yang kini masuk dalam jajaran bank berkapitalisasi pasar terbesar di tanah air. Dengan kewajiban sertifikasi halal nasional yang terintegrasi secara digital melalui Badan Penyelenggara Jaminan Produk Halal (BPJPH), Indonesia memantapkan langkahnya bukan hanya sebagai penonton, melainkan sebagai penentu standar dan poros peradaban ekonomi syariah global yang inklusif dan berkelanjutan.",
             "この実体経済エコシステムの強化は、国営イスラム銀行各行の統合による「バンク・シャリア・インドネシア（BSI）」への合併を通じて加速され、同銀行は今や国内最大手時価総額の銀行グループの一角に食い込んでいます。ハラール製品保証機関（BPJPH）を通じてデジタル統合された国家ハラール認証の義務化とともに、インドネシアは単なる観客としてではなく、包摂的で持続可能な世界のシャリア経済文明の基準設定者（スタンダードセッター）および主軸としての足取りを確固たるものにしています。",
             "keuangan syariah（イスラム金融）、konsolidasi（統合・再編）、penentu standar（基準設定者・スタンダードセッター）、poros peradaban（文明の主軸）。")
        ],
        "vocab": [
            ("menggiurkan", "動詞", "giur", "魅了する、食欲や食指をそそる", "Peluang bisnis itu sangat menggiurkan."),
            ("konsumtif", "形容詞", "-", "消費的な、浪費しがちな", "Gaya hidup konsumtif harus dikurangi."),
            ("bermetamorfosis", "動詞", "metamorfosis", "変態する、脱皮して変貌を遂げる", "Ulat bermetamorfosis menjadi kupu-kupu."),
            ("holistik", "形容詞", "-", "包括的な、全人的な、全体論的な", "Pendekatan holistik dibutuhkan dalam kesehatan."),
            ("mengedepankan", "動詞", "depan", "優先する、前面に押し出す、重視する", "Musyawarah mengedepankan mufakat bersama."),
            ("merajai", "動詞", "raja", "支配する、王座に君臨する、席巻する", "Ponsel pintar lokal merajai pasar dalam negeri."),
            ("adibusana", "名詞", "busana", "高級衣装、オートクチュール", "Gaun adibusana itu dirancang desainer ternama."),
            ("poros", "名詞", "-", "軸、旋回軸、要衝", "Selat Malaka adalah poros perdagangan maritim."),
            ("inklusif", "形容詞", "-", "包摂的な、あらゆる層を受け入れる", "Pendidikan inklusif menyambut siswa berkebutuhan khusus."),
            ("konsolidasi", "名詞", "-", "統合、連帯強化、地盤固め", "Konsolidasi perbankan memperkuat permodalan.")
        ],
        "grammar_points": """1. **派生接頭辞 `ber-` による外来語動詞化（例: `bermetamorfosis`, `bertransformasi`）**:
   - ギリシャ・ラテン起源の学術借用語に *ber-* を冠し、主体的な自己変革を表します。
2. **連語的表現 `tidak lagi berpuas diri menjadi ...`（もはや〜であることに甘んじない）**:
   - 現状打破と野心的な成長戦略を宣言する格調高い評論表現です。
3. **対比構文 `bukan hanya sebagai penonton, melainkan sebagai penentu standar`（単なる観客ではなく、基準設定者として）**:
   - 国際的地位の向上を力強くアピールする構文です。""",
        "quizzes": [
            ("現代のインドネシアにおいて、「ハラール（Halal）」の概念はどのように進化（bermetamorfosis）しましたか？",
             ["単なる肉の屠殺方法や豚肉・酒の禁止を超え、衛生、安全性、環境持続性、倫理的公正さを重んじるライフスタイルへと進化した", "宗教の信者以外には購入を禁止する閉鎖的なルールになった", "すべての料理に唐辛子を入れることと同義になった"],
             "単なる肉の屠殺方法や豚肉・酒の禁止を超え、衛生、安全性、環境持続性、倫理的公正さを重んじるライフスタイルへと進化した",
             "第2段落に「Halal kini telah bermetamorfosis menjadi sinonim dari gaya hidup holistik (halal lifestyle) yang mengedepankan prinsip kebersihan prima, keselamatan biologis, keberlanjutan lingkungan, dan keadilan etis...」とあります。"),
            ("インドネシアのモデスト・ファッション（busana santun）が達成した国際的な快挙は何ですか？",
             ["パリ、ロンドン、ニューヨークの名門ファッションウィークに進出し、高い評価を得たこと", "海外の服をすべて輸入禁止にしたこと", "全員に同じ制服を着せる法律を作ったこと"],
             "パリ、ロンドン、ニューヨークの名門ファッションウィークに進出し、高い評価を得たこと",
             "第3段落に「...tren busana santun (modest fashion) karya perancang Indonesia berhasil menembus pekan mode bergengsi di Paris, London, dan New York...」とあります。"),
            ("国営シャリア銀行各行が合併して誕生した、インドネシア最大のイスラム金融機関は何ですか？",
             ["Bank Sentral Asia", "Bank Syariah Indonesia (BSI)", "Bank Pasar Tradisional"],
             "Bank Syariah Indonesia (BSI)",
             "第4段落に「...melalui merger bank-bank syariah milik negara menjadi Bank Syariah Indonesia (BSI)...」とあります。")
        ],
        "culture": """### 「Halal Lifestyle」と「Halal & Thoyyib」の哲学
コーランにおいてハラール（合法）は常に「Thoyyib（善良で清潔、質が高い）」という概念と対で語られます（Halalan Thayyiban）。
インドネシアでは2014年制定の「ハラール製品保証法（UU JPH）」に基づき、食品・飲料のみならず医薬品、化粧品、日用品に至るまで認証制度が義務化されました。
「Wardah（ワルダ）」などのコスメブランドは「ハラール×天然成分×クルエルティフリー」を打ち出して外資系巨頭を凌駕し、ムスリム女性の自己実現とグローバルな美の基準を再定義しています。"""
    },
    {
        "id": "1237",
        "slug": "level-4-07-borobudur-conservation-tourism",
        "title": "【Level 4 (B2)】Dilema Konservasi dan Pariwisata di Candi Borobudur（ボロブドゥール遺跡の保全とマスツーリズムの相克）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "8〜9世紀に建立された世界最大の仏教遺跡ボロブドゥール。過剰観光（オーバーツーリズム）による石材摩耗・地盤沈下と、保全規制に対する地域経済の反発。持続可能な文化観光の解を探る。",
        "text": """Berdiri megah di atas bukit di Lembah Kedu, Jawa Tengah, Candi Borobudur merupakan mahakarya arsitektur batu andesit terbesar di dunia yang dibangun oleh wangsa Syailendra pada abad kedelapan. Lebih dari dua ribu panel relief yang dipahat dengan detail mengagumkan serta ratusan stupa berterawang membentang membentuk mandala kosmik raksasa, merepresentasikan tingkatan spiritual manusia dari alam hasrat jasmani (Kamadhatu), alam wujud tanpa nafsu (Rupadhatu), hingga alam kekosongan mutlak (Arupadhatu). Sebagai salah satu warisan dunia UNESCO, Borobudur bukan hanya magnet pariwisata premier Indonesia, melainkan juga tempat peribadatan suci bagi umat Buddha dari seluruh penjuru dunia.

Akan tetapi, popularitas global yang luar biasa tersebut bagaikan pisau bermata dua. Ledakan pariwisata massal (mass tourism) selama beberapa dekade terakhir telah memberikan tekanan fisik yang sangat berat bagi struktur monumen kuno tersebut. Jutaan pasang alas kaki pengunjung yang menaiki tangga candi setiap tahunnya telah mengikis batu andesit purba sedalam beberapa sentimeter. Belum lagi perilaku vandalisme segelintir wisatawan yang menduduki stupa, membuang sampah permen karet di sela-sela relief, serta beban getaran struktural berlebih yang mempercepat keausan dan penurunan stabilitas struktur candi.

Menyadari ancaman degradasi yang tak tergantikan ini, pemerintah dan Balai Konservasi Borobudur mengambil langkah berani namun kontroversial untuk membatasi kuota pengunjung yang diizinkan naik ke atas struktur candi secara drastis, yakni hanya seribu dua ratus orang per hari. Setiap pengunjung yang naik diwajibkan mengenakan upanat, yaitu sandal khusus berbahan anyaman daun pandan dan spons alami yang dirancang tidak merusak permukaan batu. Selain itu, wacana kenaikan tarif tiket naik candi sempat memicu resistensi sengit dari para pelaku usaha wisata lokal, pemandu wisata, dan pedagang suvenir yang mengkhawatirkan penurunan omzet pendapatan mereka.

Dilema antara konservasi cagar budaya dan eksploitasi ekonomi pariwisata menuntut perubahan paradigma yang fundamental. Borobudur tidak boleh terus-menerus diperlakukan sekadar sebagai objek wisata swafoto yang dieksploitasi tanpa batas, melainkan sebagai pusat studi spiritualitas, sejarah, dan peradaban yang harus dihormati. Melalui integrasi pariwisata berkualitas dengan pengembangan desa-desa wisata (balkondes) di kawasan penyangga sekitar candi, kesejahteraan ekonomi masyarakat lokal dapat tetap tumbuh tanpa harus mengorbankan kelestarian batu-batu suci yang telah bertahan menembus seribu tahun sejarah.""",
        "paragraphs": [
            ("Berdiri megah di atas bukit di Lembah Kedu, Jawa Tengah, Candi Borobudur merupakan mahakarya arsitektur batu andesit terbesar di dunia yang dibangun oleh wangsa Syailendra pada abad kedelapan. Lebih dari dua ribu panel relief yang dipahat dengan detail mengagumkan serta ratusan stupa berterawang membentang membentuk mandala kosmik raksasa, merepresentasikan tingkatan spiritual manusia dari alam hasrat jasmani (Kamadhatu), alam wujud tanpa nafsu (Rupadhatu), hingga alam kekosongan mutlak (Arupadhatu). Sebagai salah satu warisan dunia UNESCO, Borobudur bukan hanya magnet pariwisata premier Indonesia, melainkan juga tempat peribadatan suci bagi umat Buddha dari seluruh penjuru dunia.",
             "中ジャワ州ケドゥ盆地の丘の上に壮大に聳えるボロブドゥール寺院は、8世紀にシャイレーンドラ王朝によって建立された世界最大の安山岩建築の最高傑作です。息を呑むような細密さで彫刻された2,000面以上の浮彫（レリーフ）パネルと、幾百もの格子状透かし彫りストゥーパ（仏塔）が広大な宇宙曼荼羅を形成し、肉体的欲望の世界（カーマダートゥ／欲界）、欲望を脱した物質の世界（ルーパダートゥ／色界）、そして絶対的空無の世界（アルーパダートゥ／無色界）に至る人間の精神的段階を象徴しています。ユネスコ世界遺産の一つとして、ボロブドゥールはインドネシア随一の観光マグネットであるだけでなく、世界中の仏教徒にとっての神聖な祈りの場でもあります。",
             "Lembah Kedu（ケドゥ盆地）、wangsa Syailendra（シャイレーンドラ朝）、stupa berterawang（格子状透かし彫り仏塔）、mandala kosmik（宇宙曼荼羅）。"),
            ("Akan tetapi, popularitas global yang luar biasa tersebut bagaikan pisau bermata dua. Ledakan pariwisata massal (mass tourism) selama beberapa dekade terakhir telah memberikan tekanan fisik yang sangat berat bagi struktur monumen kuno tersebut. Jutaan pasang alas kaki pengunjung yang menaiki tangga candi setiap tahunnya telah mengikis batu andesit purba sedalam beberapa sentimeter. Belum lagi perilaku vandalisme segelintir wisatawan yang menduduki stupa, membuang sampah permen karet di sela-sela relief, serta beban getaran struktural berlebih yang mempercepat keausan dan penurunan stabilitas struktur candi.",
             "しかしながら、その並外れた世界的人気は「両刃の剣」でもあります。過去数十年にわたるマスツーリズムの爆発的増加は、この古代記念碑の構造に対して極めて過酷な物理的圧力を課してきました。毎年寺院の階段を上る数百万人もの観光客の履物は、古代の安山岩を数センチメートルの深さにまで削り摩耗させてきました。さらには、ストゥーパの上に座り込んだり、レリーフの隙間にガムのゴミを捨てたりする一部観光客のヴァンダリズム（文化財破壊行為）や、寺院の摩耗と安定性の低下を加速させる過剰な構造的振動負荷も重なっています。",
             "pisau bermata dua（両刃の剣）、pariwisata massal / mass tourism（過剰観光・マスツーリズム）、mengikis batu（石を摩耗させる・削る）、keausan struktural（構造的摩耗・劣化）。"),
            ("Menyadari ancaman degradasi yang tak tergantikan ini, pemerintah dan Balai Konservasi Borobudur mengambil langkah berani namun kontroversial untuk membatasi kuota pengunjung yang diizinkan naik ke atas struktur candi secara drastis, yakni hanya seribu dua ratus orang per hari. Setiap pengunjung yang naik diwajibkan mengenakan upanat, yaitu sandal khusus berbahan anyaman daun pandan dan spons alami yang dirancang tidak merusak permukaan batu. Selain itu, wacana kenaikan tarif tiket naik candi sempat memicu resistensi sengit dari para pelaku usaha wisata lokal, pemandu wisata, dan pedagang suvenir yang mengkhawatirkan penurunan omzet pendapatan mereka.",
             "取り返しのつかないこの劣化の危機を認識した政府とボロブドゥール保全庁は、寺院の構造物の上に登壇できる入場者定員（クオータ）を1日わずか1,200人へと劇的に制限するという、果敢ながらも議論を呼ぶ措置を講じました。登壇するすべての参拝者・観光客は、石の表面を傷つけないよう設計された、パンダナスの葉の編み込みと天然スポンジを素材とする特製サンダル「ウパナット（upanat）」の着用が義務付けられました。さらに、登壇チケット料金の値上げ議論は、売上減少を懸念する地元の観光事業者、ツアーガイド、土産物商人らからの激しい抵抗を巻き起こしました。",
             "Balai Konservasi Borobudur（ボロブドゥール保全庁）、kuota pengunjung（入場者定員・クオータ）、sandal upanat（寺院保全用特製サンダル）、resistensi sengit（激しい抵抗・反発）。"),
            ("Dilema antara konservasi cagar budaya dan eksploitasi ekonomi pariwisata menuntut perubahan paradigma yang fundamental. Borobudur tidak boleh terus-menerus diperlakukan sekadar sebagai objek wisata swafoto yang dieksploitasi tanpa batas, melainkan sebagai pusat studi spiritualitas, sejarah, dan peradaban yang harus dihormati. Melalui integrasi pariwisata berkualitas dengan pengembangan desa-desa wisata (balkondes) di kawasan penyangga sekitar candi, kesejahteraan ekonomi masyarakat lokal dapat tetap tumbuh tanpa harus mengorbankan kelestarian batu-batu suci yang telah bertahan menembus seribu tahun sejarah.",
             "文化財の保全と観光による経済的搾取との間のジレンマは、根本的なパラダイムシフトを要求しています。ボロブドゥールは、際限なく搾取される単なるセルフィー（自撮り）観光地として扱われ続けてはならず、敬意を持って対峙されるべき精神性、歴史、そして文明の研究拠点として位置づけられなければなりません。高品質な質の高い観光と、寺院周辺の緩衝地帯における観光村（バルコンデス／Balkondes）の開発との統合を通じて、1,000年の歴史を耐え抜いてきた神聖な石々の持続可能性を犠牲にすることなく、地元住民の経済的福祉を持続的に成長させることができるのです。",
             "cagar budaya（文化財・保護記念物）、perubahan paradigma fundamental（根本的パラダイムシフト）、objek wisata swafoto（自撮り用観光対象）、kawasan penyangga（緩衝地帯・バッファーゾーン）。")
        ],
        "vocab": [
            ("mahakarya", "名詞", "karya", "最高傑作、マスターピース", "Lukisan itu adalah mahakarya sang pelukis."),
            ("berterawang", "形容詞", "terawang", "透かし彫りの、穴あき細工の", "Stupa berterawang melindungi patung Buddha."),
            ("mengikis", "動詞", "kikis", "削る、摩耗させる、徐々に削り取る", "Ombak mengikis tebing karang pantai."),
            ("vandalisme", "名詞", "-", "公共物・文化財破壊行為", "Aksi vandalisme merusak fasilitas umum."),
            ("keausan", "名詞", "aus", "摩耗、すり減り、損耗", "Keausan ban mobil membahayakan pengemudi."),
            ("degradasi", "名詞", "-", "劣化、低下、環境破壊", "Degradasi hutan memicu bencana banjir."),
            ("kontroversial", "形容詞", "-", "議論を呼ぶ、物議を醸す", "Pernyataan itu menuai tanggapan kontroversial."),
            ("resistensi", "名詞", "-", "抵抗、反発、耐性", "Warga menunjukkan resistensi terhadap kebijakan baru."),
            ("swafoto", "名詞", "foto", "自撮り、セルフィー", "Banyak turis antre mengambil swafoto."),
            ("penyangga", "名詞", "sangga", "緩衝材、支え、バッファー", "Hutan lindung berfungsi sebagai penyangga air.")
        ],
        "grammar_points": """1. **比喩的対比構文 `bagaikan pisau bermata dua`（両刃の剣のような）**:
   - メリットと深刻なデメリットが表裏一体であることを鮮烈に例える表現です。
2. **否定＋許可の受動構文 `diizinkan naik`（登壇を許可される）**:
   - 語根 *izin* + 接頭辞 *di- -kan*。
   - 例: *Hanya mereka yang memiliki izin yang boleh masuk.*（許可を持つ者だけが入場を許される。）
3. **継続・義務の禁止構文 `tidak boleh terus-menerus diperlakukan ...`（〜として扱われ続けてはならない）**:
   - 批判的論説で強い政策是正を求める際に多用される文型です。""",
        "quizzes": [
            ("世界遺産ボロブドゥール寺院の安山岩が近年深刻に摩耗（mengikis）した主たる物理的原因は何ですか？",
             ["寺院の周りでの大規模な花火大会", "毎年階段を上る数百万人の参拝者・観光客の履物による摩擦と過剰な振動負荷", "強い海風による塩害"],
             "毎年階段を上る数百万人の参拝者・観光客の履物による摩擦と過剰な振動負荷",
             "第2段落に「Jutaan pasang alas kaki pengunjung yang menaiki tangga candi setiap tahunnya telah mengikis batu andesit purba sedalam beberapa sentimeter.」とあります。"),
            ("石材の摩耗を防ぐために、現在寺院に登壇する参拝者全員に着用が義務付けられている履物の名称は何ですか？",
             ["ハイヒール", "パンダナスの葉と天然スポンジで作られた特製サンダル「ウパナット（upanat）」", "鉄製の安全靴"],
             "パンダナスの葉と天然スポンジで作られた特製サンダル「ウパナット（upanat）」",
             "第3段落に「Setiap pengunjung yang naik diwajibkan mengenakan upanat, yaitu sandal khusus berbahan anyaman daun pandan dan spons alami...」とあります。"),
            ("ボロブドゥール寺院の過剰観光（オーバーツーリズム）を解消し、周辺地域を潤すために進められている共生策は何ですか？",
             ["寺院を解体して別の場所へ移築すること", "自撮り観光地としての過剰搾取をやめ、周辺の緩衝地帯（観光村バルコンデス等）と統合した質の高い文化観光へ転換すること", "寺院を一般人立ち入り禁止にして永久封鎖すること"],
             "自撮り観光地としての過剰搾取をやめ、周辺の緩衝地帯（観光村バルコンデス等）と統合した質の高い文化観光へ転換すること",
             "第4段落に「Melalui integrasi pariwisata berkualitas dengan pengembangan desa-desa wisata (balkondes) di kawasan penyangga sekitar candi...」とあります。")
        ],
        "culture": """### 「Candi Borobudur」の精神世界と「Balkondes」構想
ボロブドゥールは、下の階層から上へと時計回りに回廊を巡ることで、俗世の欲望（Kamadhatu）から形ある世界（Rupadhatu）、そして悟りと解脱の境地である無色界（Arupadhatu）へと至る立体的な巡礼路となっています。
寺院本体への過剰な集中を防ぐため、周辺の20の村落には「Balkondes（Balai Ekonomi Desa: 村落経済交流所）」が整備され、伝統農村のホームステイ、陶芸・農業体験、地元オーガニック料理を提供することで、寺院保全と地域経済の共生（分散型ツーリズム）が図られています。"""
    },
    {
        "id": "1238",
        "slug": "level-4-08-education-inequality-islands",
        "title": "【Level 4 (B2)】Menjembatani Kesenjangan Pendidikan di Wilayah 3T（辺境島嶼地域の教育格差に挑む若手教師たち）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "辺境・最遠・後進地域（Wilayah 3T: Terdepan, Terluar, Tertinggal）における深刻な教育格差。電気やネットのない絶海の孤島で教鞭を執る青年教師たちの献身と、デジタル衛星通信による教育の公平性の追求。",
        "text": """Sebagai negara kepulauan terbesar di dunia dengan lebih dari tujuh belas ribu pulau, Indonesia menghadapi tantangan geografis yang luar biasa dalam mendistribusikan keadilan sosial, terutama dalam pemenuhan hak mendasar atas pendidikan berkualitas. Di balik kegemilangan sekolah-sekolah berstandar internasional dan megahnya gedung universitas di kota-kota metropolitan Pulau Jawa, tersimpan jurang kesenjangan yang menganga di wilayah-wilayah 3T (terdepan, terluar, dan tertinggal) yang tersebar di tapal batas nusantara, mulai dari pulau-pulau kecil di Maluku, pedalaman Papua, hingga perbatasan Kalimantan.

Di daerah-daerah terpencil tersebut, realitas pendidikan sering kali berada pada titik nadir. Banyak ruang kelas berdinding papan yang lapuk dengan atap seng yang bocor ketika musim hujan tiba. Ketiadaan aliran listrik dari jaringan negara serta nihilnya sinyal telekomunikasi memutus akses para guru dan siswa dari arus informasi dan bahan ajar modern. Lebih memprihatinkan lagi, keterbatasan jumlah guru berstatus pegawai negeri sipil kerap memaksa satu orang guru mengajar tiga kelas sekaligus secara bergantian, diperparah oleh tingginya angka putus sekolah akibat desakan ekonomi keluarga nelayan dan petani subsisten.

Menjawab panggilan kemanusiaan ini, lahirlah berbagai inisiatif gerakan pengajar muda, seperti program Indonesia Mengajar dan program afirmasi pendidik dari kementerian. Ribuan lulusan sarjana terbaik dari universitas-universitas ternama dengan sukarela meninggalkan kenyamanan karier korporat di ibu kota demi mengabdi selama setahun penuh di pelosok nusantara. Mereka menyeberangi lautan ganas dengan perahu kayu kecil dan menempuh jalan setapak berlumpur demi menyalakan lentera harapan di mata anak-anak bangsa yang selama ini terlupakan.

Di era transformasi digital saat ini, ikhtiar para pendidik militan tersebut mulai diperkuat oleh terobosan infrastruktur telekomunikasi berbasis satelit orbit rendah dan proyek Palapa Ring. Pemasangan panel surya dan terminal internet satelit di sekolah-sekolah pedalaman mulai membuka cakrawala baru, memungkinkan anak-anak di pulau terluar mengakses ensiklopedia digital dan berinteraksi secara virtual dengan teman-teman sebaya mereka di ibu kota. Menjembatani jurang pendidikan di wilayah 3T bukan semata soal menyamaratakan kurikulum atau membagikan gawai, melainkan ikhtiar menepati janji kemerdekaan untuk mencerdaskan seluruh kehidupan bangsa tanpa ada seorang anak pun yang tertinggal di belakang.""",
        "paragraphs": [
            ("Sebagai negara kepulauan terbesar di dunia dengan lebih dari tujuh belas ribu pulau, Indonesia menghadapi tantangan geografis yang luar biasa dalam mendistribusikan keadilan sosial, terutama dalam pemenuhan hak mendasar atas pendidikan berkualitas. Di balik kegemilangan sekolah-sekolah berstandar internasional dan megahnya gedung universitas di kota-kota metropolitan Pulau Jawa, tersimpan jurang kesenjangan yang menganga di wilayah-wilayah 3T (terdepan, terluar, dan tertinggal) yang tersebar di tapal batas nusantara, mulai dari pulau-pulau kecil di Maluku, pedalaman Papua, hingga perbatasan Kalimantan.",
             "1万7,000以上の島々を抱える世界最大の島嶼国家として、インドネシアは社会正義を分配する上で、とりわけ質の高い教育を受ける基本的権利の充足において並外れた地理的挑戦に直面しています。ジャワ島のメトロポリタン都市における国際水準校の輝かしさや壮麗な大学校舎の裏側には、マルク諸島の小島、パプアの内陸部、カリマンタンの国境地帯に至るまで、列島の境界線に広がる「3T地域（最前線・最遠・後進地域）」にぽっかりと口を開けた深刻な格差の断絶（jurang kesenjangan）が潜んでいます。",
             "negara kepulauan terbesar（世界最大の島嶼国家）、jurang kesenjangan menganga（ぽっかり口を開けた格差の深い溝）、wilayah 3T（最前線・最果て・後進地域）、tapal batas（国境地帯・境界）。"),
            ("Di daerah-daerah terpencil tersebut, realitas pendidikan sering kali berada pada titik nadir. Banyak ruang kelas berdinding papan yang lapuk dengan atap seng yang bocor ketika musim hujan tiba. Ketiadaan aliran listrik dari jaringan negara serta nihilnya sinyal telekomunikasi memutus akses para guru dan siswa dari arus informasi dan bahan ajar modern. Lebih memprihatinkan lagi, keterbatasan jumlah guru berstatus pegawai negeri sipil kerap memaksa satu orang guru mengajar tiga kelas sekaligus secara bergantian, diperparah oleh tingginya angka putus sekolah akibat desakan ekonomi keluarga nelayan dan petani subsisten.",
             "それらの遠隔地において、教育の実態はしばしばどん底の「最悪の状態（どん底・天底）」にあります。多くの教室は板壁が朽ち果て、雨季が来るとトタン屋根から雨漏りがします。国家電力網からの電力供給の不在、そして電気通信シグナルの皆無は、教師や生徒たちが最新の情報や現代的教材の潮流にアクセスすることを遮断しています。さらに憂慮すべきことに、公務員教師の不足はしばしば1人の教師が3つの学級を同時に交代で教えることを余儀なくさせ、漁師や自給自足農家の家庭の経済的逼迫による高い中退率によってさらに深刻化しています。",
             "titik nadir（どん底・天底・最悪の状態）、lapuk（朽ち果てた・腐食した）、nihil（ゼロ・皆無）、angka putus sekolah（中退率）、petani subsisten（自給自足的農民）。"),
            ("Menjawab panggilan kemanusiaan ini, lahirlah berbagai inisiatif gerakan pengajar muda, seperti program Indonesia Mengajar dan program afirmasi pendidik dari kementerian. Ribuan lulusan sarjana terbaik dari universitas-universitas ternama dengan sukarela meninggalkan kenyamanan karier korporat di ibu kota demi mengabdi selama setahun penuh di pelosok nusantara. Mereka menyeberangi lautan ganas dengan perahu kayu kecil dan menempuh jalan setapak berlumpur demi menyalakan lentera harapan di mata anak-anak bangsa yang selama ini terlupakan.",
             "この人道的な呼びかけに応えて、「インドネシア・ムンガジャール（Indonesia Mengajar）」や省庁による教員アファーマティブ・プログラムなど、青年教師運動の様々なイニシアチブが誕生しました。名門大学を卒業した優秀な学士たちの幾千人もの若者が、列島の僻地で丸1年間奉仕するために、首都での快適な企業キャリアを自発的に捨て去りました。彼らは、これまで見捨てられていた国家の子どもたちの瞳の中に希望のランタン（灯火）を灯すために、小さな木造小舟で荒れ狂う海を渡り、ぬかるんだ獣道を歩み抜いたのです。",
             "panggilan kemanusiaan（人道的な呼びかけ・使命感）、sukarela（自発的に・進んで）、lautan ganas（荒れ狂う海）、menyalakan lentera harapan（希望の灯火を灯す）。"),
            ("Di era transformasi digital saat ini, ikhtiar para pendidik militan tersebut mulai diperkuat oleh terobosan infrastruktur telekomunikasi berbasis satelit orbit rendah dan proyek Palapa Ring. Pemasangan panel surya dan terminal internet satelit di sekolah-sekolah pedalaman mulai membuka cakrawala baru, memungkinkan anak-anak di pulau terluar mengakses ensiklopedia digital dan berinteraksi secara virtual dengan teman-teman sebaya mereka di ibu kota. Menjembatani jurang pendidikan di wilayah 3T bukan semata soal menyamaratakan kurikulum atau membagikan gawai, melainkan ikhtiar menepati janji kemerdekaan untuk mencerdaskan seluruh kehidupan bangsa tanpa ada seorang anak pun yang tertinggal di belakang.",
             "現在のデジタルトランスフォーメーション時代において、これら熱血教師たちの奮闘は、低軌道衛星やパラパ・リング計画に基づく電気通信インフラの突破口によって補強され始めています。奥地の学校におけるソーラーパネルと衛星インターネット端末の設置は新たな地平を開き始め、最果ての島の子どもたちがデジタル百科事典にアクセスし、首都の同世代の友人たちとバーチャルに交流することを可能にしています。3T地域の教育格差に橋を架けることは、単にカリキュラムを一律に揃えたり端末を配ったりすることではなく、誰一人として取り残されることなく全国家の生活を知的に向上させるという「独立の誓約」を果たすための崇高な試みなのです。",
             "pendidik militan（熱血で不屈の教育者）、proyek Palapa Ring（国家光ファイバー通信網パラパ・リング）、membuka cakrawala baru（新たな地平を開く）、mencerdaskan kehidupan bangsa（国民生活を知的に向上させる・憲法前文の誓い）。")
        ],
        "vocab": [
            ("kesenjangan", "名詞", "senjang", "格差、不均衡、乖離", "Kesenjangan ekonomi memicu ketegangan sosial."),
            ("menganga", "動詞", "nganga", "（傷口や裂け目が）大きく口を開ける", "Jurang yang dalam menganga di tepi tebing."),
            ("nadir", "名詞", "-", "最悪のどん底、天底（zenithの対義語）", "Prestasinya anjlok ke titik nadir."),
            ("lapuk", "形容詞", "-", "腐食した、朽ちた、脆くなった", "Jembatan kayu itu sudah lapuk dimakan usia."),
            ("nihil", "形容詞", "-", "皆無の、ゼロの、空無の", "Hasil tes menunjukkan hasil nihil."),
            ("afirmasi", "名詞", "-", "積極的是正措置、アファーマティブ、肯定", "Kebijakan afirmasi membantu siswa dari daerah tertinggal."),
            ("lentera", "名詞", "-", "ランタン、灯火、提灯", "Lentera minyak menerangi malam yang gelap."),
            ("cakrawala", "名詞", "-", "地平線、視野、見識", "Membaca buku membuka cakrawala berpikir."),
            ("sebaya", "形容詞・名詞", "baya", "同年代の、同い年の", "Anak itu senang bermain dengan teman sebaya."),
            ("mencerdaskan", "動詞", "cerdas", "賢くする、知的向上をもたらす", "Pendidikan bertujuan mencerdaskan generasi penerus.")
        ],
        "grammar_points": """1. **比喩的対比表現 `Di balik kegemilangan ..., tersimpan ...`（〜の輝きの裏に、〜が潜んでいる）**:
   - 表層の華やかさと構造的な闇・格差を対比させる定番の論説構文です。
2. **使役＋受動の複合構文 `kerap memaksa ... mengajar`（しばしば〜に教えることを強制する）**:
   - 厳しい構造的制約を記述する客観的構文です。
3. **目的を表す格調高い接続構文 `demi menyalakan lentera harapan`（希望の灯火を灯すために）**:
   - 崇高な使命や献身を文学的に表現する名文句です。""",
        "quizzes": [
            ("インドネシアの教育政策において「Wilayah 3T」が指している地域の定義は何ですか？",
             ["高級住宅地・工業団地・商業地区", "最前線（Terdepan）・最遠（Terluar）・後進遅延地域（Tertinggal）の辺境境界地域", "首都ジャカルタの3つの主要行政区"],
             "最前線（Terdepan）・最遠（Terluar）・後進遅延地域（Tertinggal）の辺境境界地域",
             "第1段落に「...wilayah-wilayah 3T (terdepan, terluar, dan tertinggal) yang tersebar di tapal batas nusantara...」とあります。"),
            ("名門大学を卒業した優秀な若者たちが1年間僻地で教育ボランティアを行う運動（Indonesia Mengajar等）の目的は何ですか？",
             ["都会のキャリアを捨てて、見捨てられていた子どもたちの瞳に希望の灯火を灯すため", "僻地で金鉱を発見して大金持ちになるため", "都会のオフィスが満員で居場所がなかったため"],
             "都会のキャリアを捨てて、見捨てられていた子どもたちの瞳に希望の灯火を灯すため",
             "第3段落に「...sukarela meninggalkan kenyamanan karier korporat di ibu kota demi mengabdi selama setahun penuh... demi menyalakan lentera harapan di mata anak-anak bangsa...」とあります。"),
            ("辺境地域の学校にソーラーパネルや衛星インターネットを配備して教育格差を埋める究極の意義は何ですか？",
             ["誰一人取り残されることなく全人民の生活を知的に向上させるという「建国独立の誓い」を果たすこと", "すべての教科書を英語だけに統一すること", "子どもたちにゲームをさせること"],
             "誰一人取り残されることなく全人民の生活を知的に向上させるという「建国独立の誓い」を果たすこと",
             "第4段落に「...ikhtiar menepati janji kemerdekaan untuk mencerdaskan seluruh kehidupan bangsa tanpa ada seorang anak pun yang tertinggal di belakang.」とあります。")
        ],
        "culture": """### 「Wilayah 3T」と青年指導者たち「Indonesia Mengajar」
インドネシア共和国憲法前文（UUD 1945）には、「国民生活を知的に向上させる（mencerdaskan kehidupan bangsa）」ことが国家の至上命題として刻まれています。
しかし、東西5,000kmにわたる島嶼地形ゆえに、3T地域（国境島嶼や山岳僻地）では長年、電力・通信・教員不足が深刻でした。
2010年にアニス・バスウェダン（元教育文化相）らによって創設された「Indonesia Mengajar（インドネシア・ムンガジャール）」は、選抜されたエリート大卒生（Pengajar Muda）を1年間無給に近い手当で僻地に派遣する社会運動として国民的共感を呼び、国家の教育インフラ整備を大いに加速させました。"""
    },
    {
        "id": "1239",
        "slug": "level-4-09-traditional-law-adat",
        "title": "【Level 4 (B2)】Kedaulatan Hutan Adat dan Pengakuan Hak Masyarakat（慣習法共同体と森林主権を巡る司法闘争）",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "憲法裁判所判決（Putusan MK No. 35/2012）が認めた「慣習林は国有林ではない」という歴史的転換。プランテーション開発と先住慣習法住民（Masyarakat Adat）の土地主権を巡る法思想論説。",
        "text": """Sejak era kolonial Hindia Belanda hingga beberapa dekade pascakemerdekaan, paradigma pengelolaan sumber daya alam di Indonesia sangat didominasi oleh doktrin hak menguasai negara (domeinverklaring). Negara memosisikan diri sebagai pemilik tunggal seluruh kawasan hutan yang belum terbebani hak milik pribadi perorangan. Melalui klaim sepihak ini, ratusan juta hektare kawasan hutan adat yang telah dikelola secara turun-temurun oleh masyarakat hukum adat dipatok sepihak sebagai hutan negara, yang kemudian diobral melalui izin konsesi konsesi hak pengusahaan hutan dan perkebunan monokultur skala masif kepada korporasi besar.

Akibat dari rezim hukum yang tidak adil tersebut, masyarakat adat yang telah mendiami hutan leluhur selama berabad-abad mendadak diperlakukan layaknya perambah liar di tanah tumpah darah mereka sendiri. Kriminalisasi terhadap para tetua adat yang memungut hasil hutan atau mempertahankan wilayah ulayat dari gusuran alat berat sering kali memicu konflik agraria berdarah. Kearifan lokal dalam menjaga ekosistem hutan—seperti sistem perladangan bergilir ramah lingkungan, hukum adat pantangan menebang pohon keramat, dan zonasi perlindungan mata air—terabaikan oleh logika eksploitasi kapitalistik jangka pendek.

Titik balik historis dalam perjuangan keadilan agraria ini meletus ketika Aliansi Masyarakat Adat Nusantara (AMAN) mengajukan uji materi Undang-Undang Kehutanan ke Mahkamah Konstitusi. Melalui Putusan MK Nomor 35/PUU-X/2012 yang sangat monumental, Mahkamah Konstitusi secara tegas memutuskan bahwa hutan adat adalah hutan yang berada dalam wilayah masyarakat hukum adat, dan bukan lagi merupakan hutan negara. Putusan yudisial ini meruntuhkan dominasi penguasaan mutlak negara atas hutan leluhur, serta mengembalikan kedaulatan masyarakat adat atas tanah, air, dan sumber daya alam warisan moyang mereka.

Meskipun demikian, perjalanan dari pengakuan hukum di atas kertas menuju implementasi nyata di lapangan masih berliku dan sarat tantangan birokratis. Proses penetapan hutan adat masih menuntut peraturan daerah yang kerap tersandera kepentingan politik dan bisnis lokal. Mengawal kedaulatan hutan adat bukan sekadar membela hak asasi kaum marjinal, melainkan ikhtiar krusial dalam menyelamatkan sisa-sisa benteng terakhir keanekaragaman hayati nusantara. Terbukti secara ilmiah di seluruh dunia, hutan yang dikelola secara otonom oleh masyarakat adat memiliki laju deforestasi yang jauh lebih rendah dibanding kawasan konservasi negara.""",
        "paragraphs": [
            ("Sejak era kolonial Hindia Belanda hingga beberapa dekade pascakemerdekaan, paradigma pengelolaan sumber daya alam di Indonesia sangat didominasi oleh doktrin hak menguasai negara (domeinverklaring). Negara memosisikan diri sebagai pemilik tunggal seluruh kawasan hutan yang belum terbebani hak milik pribadi perorangan. Melalui klaim sepihak ini, ratusan juta hektare kawasan hutan adat yang telah dikelola secara turun-temurun oleh masyarakat hukum adat dipatok sepihak sebagai hutan negara, yang kemudian diobral melalui izin konsesi konsesi hak pengusahaan hutan dan perkebunan monokultur skala masif kepada korporasi besar.",
             "オランダ領東インド植民地時代から独立後の数十年に至るまで、インドネシアの天然資源管理パラダイムは国家支配権ドクトリン（ドメイン宣言・国家無主地帰属主義）に強く支配されてきました。国家は、個人の私的所有権が設定されていないすべての森林地域の「単独の所有者」として自らを位置づけました。この一方的な主張を通じて、慣習法共同体によって代々管理されてきた何億ヘクタールもの慣習林（Hutan Adat）が一方的に「国有林」として指定され、巨大企業への森林伐採権コンセッションや大規模モノカルチャー農園の操業許可として安価に払い下げられていったのです。",
             "doktrin hak menguasai negara（国家支配権ドクトリン）、masyarakat hukum adat（慣習法共同体）、dipatok sepihak（一方的に杭を打たれる・指定される）、izin konsesi（コンセッション操業権）。"),
            ("Akibat dari rezim hukum yang tidak adil tersebut, masyarakat adat yang telah mendiami hutan leluhur selama berabad-abad mendadak diperlakukan layaknya perambah liar di tanah tumpah darah mereka sendiri. Kriminalisasi terhadap para tetua adat yang memungut hasil hutan atau mempertahankan wilayah ulayat dari gusuran alat berat sering kali memicu konflik agraria berdarah. Kearifan lokal dalam menjaga ekosistem hutan—seperti sistem perladangan bergilir ramah lingkungan, hukum adat pantangan menebang pohon keramat, dan zonasi perlindungan mata air—terabaikan oleh logika eksploitasi kapitalistik jangka pendek.",
             "その不当な法体制の結果として、何世紀にもわたり先祖伝来の森に定住してきた先住慣習民たちは、自らの生誕の地において突如として不法侵入者（密伐採者）であるかのように扱われることになりました。林産物を採取したり、重機の強制立ち退きから先住慣習地（ウラヤット）を守ろうとした慣習指導者（長老）たちへの犯罪者扱い（クリミナライゼーション）は、しばしば流血の農地紛争を引き起こしました。環境共生型の循環型焼畑システム、神聖な樹木の伐採を禁じる慣習法上の禁忌、水源保護のゾーニングといった、森林生態系を守る地域知は、短期的な資本主義的搾取の論理によって打ち捨てられていたのです。",
             "rezim hukum（法体制・レジーム）、perambah liar（不法侵入者・密伐採者）、tanah tumpah darah（生誕の地・祖国）、kriminalisasi（犯罪者扱い・刑事罰化）、pantangan（禁忌・タブー）。"),
            ("Titik balik historis dalam perjuangan keadilan agraria ini meletus ketika Aliansi Masyarakat Adat Nusantara (AMAN) mengajukan uji materi Undang-Undang Kehutanan ke Mahkamah Konstitusi. Melalui Putusan MK Nomor 35/PUU-X/2012 yang sangat monumental, Mahkamah Konstitusi secara tegas memutuskan bahwa hutan adat adalah hutan yang berada dalam wilayah masyarakat hukum adat, dan bukan lagi merupakan hutan negara. Putusan yudisial ini meruntuhkan dominasi penguasaan mutlak negara atas hutan leluhur, serta mengembalikan kedaulatan masyarakat adat atas tanah, air, dan sumber daya alam warisan moyang mereka.",
             "この土地正義闘争における歴史的転換点は、列島先住民族同盟（AMAN）が森林法（UU Kehutanan）の違憲審査（Judicial Review）を憲法裁判所に申し立てたときに勃発しました。極めて記念碑的な「憲法裁判所判決第35号（Putusan MK No. 35/PUU-X/2012）」を通じて、憲法裁判所は「慣習林とは慣習法共同体の領域内に存在する森林であり、もはや国有林ではない」と断固として判決を下しました。この司法判決は、先祖伝来の森林に対する国家の絶対的支配の優位性を崩壊させ、先祖伝来の土地、水、天然資源に対する慣習民の主権を取り戻したのです。",
             "Aliansi Masyarakat Adat Nusantara / AMAN（列島先住民族同盟）、uji materi（違憲審査・法適合性審査）、Putusan MK No. 35/2012（憲法裁判所第35号判決）、meruntuhkan dominasi（支配の優位を崩壊させる）。"),
            ("Meskipun demikian, perjalanan dari pengakuan hukum di atas kertas menuju implementasi nyata di lapangan masih berliku dan sarat tantangan birokratis. Proses penetapan hutan adat masih menuntut peraturan daerah yang kerap tersandera kepentingan politik dan bisnis lokal. Mengawal kedaulatan hutan adat bukan sekadar membela hak asasi kaum marjinal, melainkan ikhtiar krusial dalam menyelamatkan sisa-sisa benteng terakhir keanekaragaman hayati nusantara. Terbukti secara ilmiah di seluruh dunia, hutan yang dikelola secara otonom oleh masyarakat adat memiliki laju deforestasi yang jauh lebih rendah dibanding kawasan konservasi negara.",
             "それにもかかわらず、紙の上の法的承認から現場での実際の履行に至る道筋は依然として曲がりくねり、官僚的手続きの困難に満ちています。慣習林の公式認定手続きは、地域政治や地元ビジネスの利害によってしばしば人質に取られる地方条例（Perda）を要求しています。慣習林の主権を守り抜くことは、単に社会的弱者の基本的人権を擁護するだけでなく、列島の生物多様性の最後の砦の残骸を救うための極めて重要な試みなのです。世界中の科学的調査で実証されているように、先住慣習民によって自治管理されている森林は、国家が管理する自然保護区よりも森林減少率（デフォレステーション率）が遥かに低いのです。",
             "di atas kertas（机上の・紙の上の）、tersandera kepentingan（利害関係に人質に取られる）、benteng terakhir keanekaragaman hayati（生物多様性の最後の砦）、laju deforestasi（森林減少率）。")
        ],
        "vocab": [
            ("sepihak", "副詞・形容詞", "pihak", "一方的な、片側だけの", "Keputusan sepihak merugikan pihak lain."),
            ("perambah", "名詞", "rambah", "侵入者、密伐採者、開拓者", "Polisi menangkap perambah hutan lindung."),
            ("kriminalisasi", "名詞", "-", "不当な犯罪者扱い、刑事罰化", "Aktivis menolak kriminalisasi warga adat."),
            ("gusuran", "名詞", "gusur", "強制立ち退き、地上げ、撤去", "Warga menolak gusuran tanpa ganti rugi."),
            ("pantangan", "名詞", "pantang", "禁忌、タブー、戒め", "Ada pantangan menangkap ikan di danau itu."),
            ("uji materi", "名詞句", "uji", "司法審査、違憲審査（judicial review）", "LSM mengajukan uji materi undang-undang baru."),
            ("yudisial", "形容詞", "-", "司法の、裁判に関する", "Putusan yudisial itu bersifat mengikat."),
            ("kedaulatan", "名詞", "daulat", "主権、統治権、独立性", "Negara menjaga kedaulatan wilayah perbatasan."),
            ("tersandera", "動詞（受動）", "sandera", "人質に取られる、拘束される", "Rancangan perda tersandera lobi politik."),
            ("deforestasi", "名詞", "-", "森林伐採、森林減少", "Deforestasi mengancam habitat satwa langka.")
        ],
        "grammar_points": """1. **時の推移・起点と終点 `Sejak era ... hingga beberapa dekade ...`（〜の時代から〜に至るまで）**:
   - 歴史的経緯を巨視的に概観する学術的導入構文です。
2. **比喩表現 `layaknya perambah liar di tanah tumpah darah mereka sendiri`（自らの生誕の地で密伐採者であるかのように）**:
   - 不条理な境遇を感情と論理の双方で読者に訴えかける格調高い比喩です。
3. **客観的論拠の提示 `Terbukti secara ilmiah di seluruh dunia, ...`（世界中で科学的に実証されているように）**:
   - 結論部分で主張の説得力を最大化する言説マーカーです。""",
        "quizzes": [
            ("過去の国家ドクトリン（Domeinverklaring等）によって先住慣習民が受けた最も不当な仕打ちは何ですか？",
             ["何世代も住み続けた先祖伝来の森が一方的に「国有林」とみなされ、不法侵入者のように扱われたこと", "オランダ語を全員が話すことを強制されたこと", "木造住宅をすべて石造りに建て替えさせられたこと"],
             "何世代も住み続けた先祖伝来の森が一方的に「国有林」とみなされ、不法侵入者のように扱われたこと",
             "第2段落に「...masyarakat adat yang telah mendiami hutan leluhur selama berabad-abad mendadak diperlakukan layaknya perambah liar di tanah tumpah darah mereka sendiri.」とあります。"),
            ("2012年の歴史的な憲法裁判所判決（Putusan MK No. 35/2012）が決定づけた根本的な法的変更は何ですか？",
             ["慣習林は国有林ではなく、慣習法共同体の領域に属する森林であると認めたこと", "すべての森林の伐採を国家が直轄すること", "慣習民を全員都市部に移住させること"],
             "慣習林は国有林ではなく、慣習法共同体の領域に属する森林であると認めたこと",
             "第3段落に「...Mahkamah Konstitusi secara tegas memutuskan bahwa hutan adat adalah hutan yang berada dalam wilayah masyarakat hukum adat, dan bukan lagi merupakan hutan negara.」とあります。"),
            ("先住慣習民による森林の自治管理が世界中の科学的調査で高く評価されている理由は何ですか？",
             ["木をすべて切り倒して更地にするのが早いため", "国家が管理する自然保護区よりも森林減少率（laju deforestasi）が遥かに低いことが実証されているため", "紙パルプを大量生産できるため"],
             "国家が管理する自然保護区よりも森林減少率（laju deforestasi）が遥かに低いことが実証されているため",
             "第4段落に「...hutan yang dikelola secara otonom oleh masyarakat adat memiliki laju deforestasi yang jauh lebih rendah dibanding kawasan konservasi negara.」とあります。")
        ],
        "culture": """### 「Hutan Adat」と「Masyarakat Adat」の復権
インドネシアには、バドゥイ（Baduy）、ダヤック（Dayak）、ダニ（Dani）、メンタワイ（Mentawai）、トラジャ（Toraja）など、何百もの「Masyarakat Hukum Adat（慣習法共同体）」が存在します。
植民地時代からスハルト開発独裁期にかけては、国有林としてパーム油プランテーションや鉱山開発に強引に明け渡され、多くの紛争が生じました。
2012年の画期的な「MK 35判決」以降、地方条例（Perda）制定を通じて慣習林の返還が進められており、先住民族の伝統知（Indigenous Knowledge）による持続可能な自然保護が世界的なモデルとして再評価されています。"""
    },
    {
        "id": "1240",
        "slug": "level-4-10-level4-review-quiz",
        "title": "【Level 4 (B2)】Tantangan Abad 21 Menuju Indonesia Emas 2045 & 総合読解診断テスト",
        "level": "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）",
        "desc": "建国100周年を迎える2045年の「黄金のインドネシア（Indonesia Emas 2045）」。人口ボーナス、中進国の罠の打破、脱炭素・グリーン経済、多文化包摂を総括する高度な論説パッセージとB2総合診断テスト。",
        "text": """Ketika fajar abad kedua puluh satu merekah semakin benderang, bangsa Indonesia tengah melangkah di atas jembatan krusial menuju momentum satu abad kemerdekaannya pada tahun 2045. Visi megah bertajuk Indonesia Emas 2045 memproyeksikan transformasi tanah air menjadi salah satu dari lima kekuatan ekonomi terbesar di dunia, dengan pendapatan per kapita yang sejajar dengan negara-negara maju dan tingkat kemiskinan yang mendekati nol persen. Namun, jalan menuju puncak peradaban tersebut bukanlah hamparan karpet merah yang mulus, melainkan gelanggang uji kelayakan yang sarat dengan dialektika antara peluang emas dan tantangan struktural yang mahaberat.

Peluang terbesar Indonesia bersumber pada jendela bonus demografi, di mana proporsi penduduk usia produktif mencapai puncaknya hingga mendominasi lebih dari enam puluh persen total populasi. Jika modalitas sumber daya manusia yang melimpah ini dibekali dengan kompetensi sains dan teknologi mutakhir, etos kerja profesional, serta karakter kebangsaan yang kokoh, niscaya Indonesia mampu melompat keluar dari perangkap pendapatan menengah (middle-income trap). Sebaliknya, apabila sistem pendidikan gagal mengimbangi laju disrupsi kecerdasan buatan dan otomatisasi global, ledakan angkatan kerja ini justru berpotensi berubah menjadi bom waktu pengangguran massal dan kerawanan sosial.

Secara bersamaan, transformasi ekonomi Indonesia dituntut untuk berlayar menembus gelombang transisi hijau global. Sebagaimana tercermin dalam kebijakan hilirisasi mineral kritis, pembangunan ibu kota hijau Nusantara, restorasi ekosistem gambut, hingga penguatan industri halal dan ekonomi sirkular, paradigma pembangunan tidak lagi mentoleransi pertumbuhan ekstraktif yang rakus dan merusak daya lentur bumi. Kedaulatan energi baru terbarukan serta perlindungan terhadap hak-hak masyarakat adat atas hutan leluhur menjadi prasyarat mutlak agar kemakmuran material tidak dibayar dengan kepunahan ekologis.

Pada akhirnya, pilar penyangga paling hakiki dari Indonesia Emas adalah keteguhan merawat rajutan kebinekaan dan demokrasi yang berkeadaban. Di tengah godaan polarisasi identitas dan arus disinformasi digital, kearifan lokal seperti filosofi wayang dan semangat gotong royong harus tetap menjadi jangkar nurani bangsa. Dengan memadukan kecerdasan akal budi, kemajuan teknologi, keberanian mengambil keputusan geopolitik, dan kepekaan sosial terhadap kaum marjinal, nusantara akan mampu membuktikan kepada dunia bahwa modernitas dan tradisi bukanlah dua kutub yang saling meniadakan, melainkan simfoni agung yang mengantarkan Indonesia menuju takhta kejayaan abadi.""",
        "paragraphs": [
            ("Ketika fajar abad kedua puluh satu merekah semakin benderang, bangsa Indonesia tengah melangkah di atas jembatan krusial menuju momentum satu abad kemerdekaannya pada tahun 2045. Visi megah bertajuk Indonesia Emas 2045 memproyeksikan transformasi tanah air menjadi salah satu dari lima kekuatan ekonomi terbesar di dunia, dengan pendapatan per kapita yang sejajar dengan negara-negara maju dan tingkat kemiskinan yang mendekati nol persen. Namun, jalan menuju puncak peradaban tersebut bukanlah hamparan karpet merah yang mulus, melainkan gelanggang uji kelayakan yang sarat dengan dialektika antara peluang emas dan tantangan struktural yang mahaberat.",
             "21世紀の夜明けがますます眩しく輝き始める中、インドネシア民族は2045年の独立100周年の記念すべきモメンタムへ向かう極めて重要な架け橋の上を歩んでいます。「インドネシア黄金期2045（Indonesia Emas 2045）」と銘打たれた壮大なビジョンは、先進国と肩を並べる一人当たり国民所得とほぼゼロパーセントの貧困率を達成し、祖国を世界5大経済大国の一つへと変革することを予測しています。しかし、その文明の頂点へと至る道は平坦な赤い絨毯の広がりなどではなく、黄金の好機と極めて重い構造的挑戦との間の弁証法に満ちた適合性の試練のリングなのです。",
             "Indonesia Emas 2045（インドネシア黄金期2045）、lima kekuatan ekonomi terbesar（世界5大経済大国）、hamparan karpet merah（平坦なレッドカーペット）、uji kelayakan（適合性・妥当性の試練）、dialektika（弁証法）。"),
            ("Peluang terbesar Indonesia bersumber pada jendela bonus demografi, di mana proporsi penduduk usia produktif mencapai puncaknya hingga mendominasi lebih dari enam puluh persen total populasi. Jika modalitas sumber daya manusia yang melimpah ini dibekali dengan kompetensi sains dan teknologi mutakhir, etos kerja profesional, serta karakter kebangsaan yang kokoh, niscaya Indonesia mampu melompat keluar dari perangkap pendapatan menengah (middle-income trap). Sebaliknya, apabila sistem pendidikan gagal mengimbangi laju disrupsi kecerdasan buatan dan otomatisasi global, ledakan angkatan kerja ini justru berpotensi berubah menjadi bom waktu pengangguran massal dan kerawanan sosial.",
             "インドネシアにとっての最大の好機は、生産年齢人口の割合がピークに達して総人口の60%以上を占める「人口ボーナスの窓」に源泉があります。もしこの潤沢な人的資源の潜在力が、最先端の科学技術能力、専門的労働倫理、そして強固な国民的品格を備えるならば、インドネシアは間違いなく「中進国の罠（middle-income trap）」から飛び出すことができるでしょう。逆に、教育システムが人工知能（AI）や世界的な自動化のディスラプションの速度に追いつけなければ、この労働力人口の爆発はむしろ大量失業と社会的不安の時限爆弾へと変わる恐れがあるのです。",
             "bonus demografi（人口ボーナス）、perangkap pendapatan menengah / middle-income trap（中進国の罠）、laju disrupsi AI（人工知能による破壊的変化の速度）、kerawanan sosial（社会的不安・脆弱性）。"),
            ("Secara bersamaan, transformasi ekonomi Indonesia dituntut untuk berlayar menembus gelombang transisi hijau global. Sebagaimana tercermin dalam kebijakan hilirisasi mineral kritis, pembangunan ibu kota hijau Nusantara, restorasi ekosistem gambut, hingga penguatan industri halal dan ekonomi sirkular, paradigma pembangunan tidak lagi mentoleransi pertumbuhan ekstraktif yang rakus dan merusak daya lentur bumi. Kedaulatan energi baru terbarukan serta perlindungan terhadap hak-hak masyarakat adat atas hutan leluhur menjadi prasyarat mutlak agar kemakmuran material tidak dibayar dengan kepunahan ekologis.",
             "同時に、インドネシアの経済変革は、地球規模のグリーン転換の波を乗り越えて航行することを求められています。重要鉱物の下流化政策、グリーン首都ヌサンタラの建設、泥炭湿原生態系の再生、そしてハラール産業やサーキュラーエコノミーの強化に反映されているように、開発パラダイムはもはや地球の回復力を破壊する貪欲で収奪的な成長を容認しません。新再生可能エネルギーの主権、および先祖伝来の森に対する先住慣習民の権利保護は、物質的繁栄が生態学的絶滅という代償を払って購われないための絶対的前提条件なのです。",
             "transisi hijau global（地球規模のグリーン転換）、pertumbuhan ekstraktif（資源収奪的成長）、daya lentur bumi（地球の回復力・レジリエンス）、kepunahan ekologis（生態学的絶滅）。"),
            ("Pada akhirnya, pilar penyangga paling hakiki dari Indonesia Emas adalah keteguhan merawat rajutan kebinekaan dan demokrasi yang berkeadaban. Di tengah godaan polarisasi identitas dan arus disinformasi digital, kearifan lokal seperti filosofi wayang dan semangat gotong royong harus tetap menjadi jangkar nurani bangsa. Dengan memadukan kecerdasan akal budi, kemajuan teknologi, keberanian mengambil keputusan geopolitik, dan kepekaan sosial terhadap kaum marjinal, nusantara akan mampu membuktikan kepada dunia bahwa modernitas dan tradisi bukanlah dua kutub yang saling meniadakan, melainkan simfoni agung yang mengantarkan Indonesia menuju takhta kejayaan abadi.",
             "結局のところ、「インドネシア黄金期」の最も本質的な支柱は、多様性の織物と文明化された民主主義を守り育てる不屈の決意にあります。アイデンティティの分極化の誘惑やデジタル偽情報の潮流のただ中にあっても、ワヤンの哲学やゴトン・ロヨン（相互扶助）の精神といった地域知は、国家の良心の錨であり続けなければなりません。理性の知性、科学技術の進歩、地政学的決断を下す勇気、そして社会的弱者への社会的感受性を融合させることで、列島は近代性と伝統が互いを排除し合う二極などではなく、インドネシアを永遠の栄光の王座へと導く壮大なシンフォニーであることを世界に証明できるはずです。",
             "rajutan kebinekaan（多様性の織り成し）、jangkar nurani（良心の錨）、kecerdasan akal budi（理性の知性）、simfoni agung（壮大なるシンフォニー）。")
        ],
        "vocab": [
            ("benderang", "形容詞", "-", "燦然と輝く、明るい、明瞭な", "Lampu kristal bersinar benderang."),
            ("dialektika", "名詞", "-", "弁証法、対立と止揚の力学", "Dialektika sejarah mendorong perubahan zaman."),
            ("modalitas", "名詞", "-", "潜在能力、形態、資源的基盤", "Bonus demografi adalah modalitas pembangunan."),
            ("niscaya", "副詞", "-", "必ず、間違いなく、必然的に", "Kerja keras niscaya membuahkan keberhasilan."),
            ("kerawanan", "名詞", "rawan", "脆弱性、危機的状況、不安状態", "Krisis pangan memicu kerawanan sosial."),
            ("ekstraktif", "形容詞", "-", "採取的な、収奪的な（資源採掘型）", "Ekonomi ekstraktif merusak kelestarian alam."),
            ("prasyarat", "名詞", "syarat", "前提条件、必須条件", "Stabilitas politik adalah prasyarat investasi."),
            ("berkeadaban", "形容詞", "adab", "文明的な、礼儀と道徳を備えた", "Demokrasi berkeadaban menjunjung hak asasi."),
            ("jangkar", "名詞", "-", "錨（アンカー）、精神の支え", "Agama menjadi jangkar hidup manusia."),
            ("simfoni", "名詞", "-", "交響曲、調和のとれた融合", "Perbedaan bersatu dalam simfoni harmoni.")
        ],
        "grammar_points": """1. **確信・必然を表す文語副詞 `niscaya ...`（間違いなく〜、必ずや〜）**:
   - 条件節（*jika...*）の帰結部で確実な未来を力強く宣言する格式高い副詞です。
   - 例: *Jika kita bersatu, niscaya kita menang.*（我々が団結すれば、必ずや勝利する。）
2. **目的・予防の否定接続表現 `agar ... tidak dibayar dengan ...`（〜で購われないように）**:
   - 代償の大きさに警鐘を鳴らす修辞的論説文型です。
3. **総合相関構文 `bukanlah dua kutub yang saling meniadakan, melainkan ...`（互いに打ち消し合う二極ではなく、むしろ〜である）**:
   - 二項対立を超克する高度な哲学的結論を導く最高峰の構文です。""",
        "quizzes": [
            ("国家ビジョン「Indonesia Emas 2045」が目標として掲げているインドネシアの将来像は何ですか？",
             ["人口を半分に減らして自給自足に戻ること", "独立100周年に世界5大経済大国の一角となり、一人当たり所得で先進国と並び貧困率ゼロに近づくこと", "首都を海外に移転すること"],
             "独立100周年に世界5大経済大国の一角となり、一人当たり所得で先進国と並び貧困率ゼロに近づくこと",
             "第1段落に「Visi megah bertajuk Indonesia Emas 2045 memproyeksikan transformasi tanah air menjadi salah satu dari lima kekuatan ekonomi terbesar di dunia, dengan pendapatan per kapita yang sejajar dengan negara-negara maju...」とあります。"),
            ("インドネシアが「中進国の罠（middle-income trap）」を打破するための最大の好機（modalitas）とされているものは何ですか？",
             ["生産年齢人口が60%以上を占める人口ボーナスの窓（bonus demografi）", "外国からの無制限の借款", "すべての工場の機械を停止すること"],
             "生産年齢人口が60%以上を占める人口ボーナスの窓（bonus demografi）",
             "第2段落に「Peluang terbesar Indonesia bersumber pada jendela bonus demografi, di mana proporsi penduduk usia produktif mencapai puncaknya hingga mendominasi lebih dari enam puluh persen...」とあります。"),
            ("パッセージの結論において、近代化（modernitas）と伝統（tradisi）の関係はどのように総括されていますか？",
             ["互いに排斥・打ち消し合う二極ではなく、インドネシアを真の繁栄へと導く壮大な交響曲（simfoni agung）である", "近代化のためにはすべての伝統文化を早急に破壊すべきである", "伝統を守るために一切のデジタル技術を禁止すべきである"],
             "互いに排斥・打ち消し合う二極ではなく、インドネシアを真の繁栄へと導く壮大な交響曲（simfoni agung）である",
             "第4段落に「...modernitas dan tradisi bukanlah dua kutub yang saling meniadakan, melainkan simfoni agung yang mengantarkan Indonesia menuju takhta kejayaan abadi.」とあります。")
        ],
        "culture": """### 「Indonesia Emas 2045」とCEFR B2レベルの達成
1945年8月17日の独立宣言から100年目を迎える2045年に向け、インドネシアは「主権を有し、先進的で持続可能な国家（Negara Nusantara Berdaulat, Maju, dan Berkelanjutan）」を目指す長期開発計画（RPJPN 2025-2045）を推進しています。
CEFR B2（中上級）を修了した学習者は、抽象的な法政策、経済マクロ指標、地政学的リスク、環境持続性、文化人類学的考察を重層的に読み解く高度なリテラシーを獲得しています。
続くLevel 5（C1/C2最上級編）では、国家白書、学術論文、古典文学、そして最高峰の論説読解へと進み、インドネシア語の深遠なマスターを目指します。"""
    }
]

def render_article(st):
    slug = st["slug"]
    title = st["title"]
    level = st.get("level", "CEFR B2（中上級レベル・想定語彙数 2,500〜4,000語）")
    desc = st["desc"]
    text = st["text"]
    paragraphs = st["paragraphs"]
    vocab = st["vocab"]
    grammar_points = st["grammar_points"]
    quizzes = st["quizzes"]
    culture = st["culture"]

    # Build markdown
    md = f"""---
title: "{title}"
description: "{desc}"
---

# {title}

<div class="level-badge" style="display:inline-block; background:#1e40af; color:white; padding:4px 12px; border-radius:20px; font-weight:bold; font-size:0.85rem; margin-bottom:1rem;">
  {level}
</div>

{desc}

---

## 📖 インドネシア語本文（Teks Bacaan）

<div class="reading-box" style="background:#f8fafc; border-left:4px solid #1e40af; padding:1.25rem 1.5rem; margin:1.5rem 0; line-height:1.9; font-size:1.05rem;">

{text}

</div>

---

## 🔍 段落ごとの対訳と読解着眼点（Analisis Paragraf）

"""
    for i, (orig, trans, note) in enumerate(paragraphs, 1):
        md += f"""### 第{i}段落
<div class="paragraph-analysis" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1rem 1.25rem; margin-bottom:1.25rem;">
  <p style="font-weight:600; color:#1e293b; margin-bottom:0.5rem; line-height:1.7;">{orig}</p>
  <p style="color:#334155; margin-bottom:0.5rem; line-height:1.7;"><strong>日本語訳</strong>: {trans}</p>
  <p style="font-size:0.9rem; color:#64748b; margin-bottom:0;">💡 <strong>論理・構文のポイント</strong>: {note}</p>
</div>
"""

    md += """---

## 📚 重要学術・論説語彙10選（Kosakata Kunci & Akademik）

| 単語 / 表現 | 品詞 | 語根 | 日本語の意味 | 実践用例 |
| :--- | :--- | :--- | :--- | :--- |
"""
    for word, pos, root, meaning, eg in vocab:
        md += f"| **{word}** | {pos} | `{root}` | {meaning} | *{eg}* |\n"

    md += f"""
---

## 🛠️ 文法・論説構文の徹底解説（Tata Bahasa & Struktur Wacana）

{grammar_points}

---

## ✍️ 読解力チェッククイズ（Latihan Pemahaman Kritis）

論説の内容や筆者の論理展開を正しく読み解けているか、3つの問いで確認してみましょう。

"""
    for q_idx, (q_text, choices, answer, explanation) in enumerate(quizzes, 1):
        md += f"""### 問{q_idx}: {q_text}

"""
        for c in choices:
            md += f"- [ ] {c}\n"
        md += f"""
??? success "正解と解説を確認する"
    **正解**: 「**{answer}**」

    **解説**:
    {explanation}

"""

    md += f"""---

## 🌿 背景知識・社会文化コラム（Wawasan Kontekstual）

{culture}

---

## 🧭 次のステップ・関連学習
- 本文で用いられている重層的な接続表現（*kendatipun demikian*, *alih-alih*, *niscaya* 等）の文脈機能をノートに整理しましょう。
- 政策論説や学術記事の読解を通じて、客観的・論理的な思考フレームワークを強化してください。
- 関連リンク: [総合サイトマップ](../sitemap.md) | [トップページ](../index.md)
"""
    return md

output_dir = r"c:\Users\Makoto\Projects\bahasa_indonesia\docs\graded-reading"
os.makedirs(output_dir, exist_ok=True)

for st in stories:
    slug = st["slug"]
    filepath = os.path.join(output_dir, f"{slug}.md")
    content = render_article(st)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {filepath}")

print("All 10 Level 4 articles created successfully!")
