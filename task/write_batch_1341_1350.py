# -*- coding: utf-8 -*-
"""
セクション32 第5バッチ (1341-1350) 記事生成スクリプト
【長文読解】インドネシア現代社会・トレンド深層読解（セクション32完結）
"""

import os

articles = [
    {
        "filename": "41-craft-beer-wine-bali.md",
        "title": "41. 熱帯ワインとクラフトビールの挑戦：厳しい酒税下で育まれるバリ島醸造文化",
        "category": "長文読解・食文化・産業経済",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "世界最大のイスラム教徒人口を抱えるインドネシアでは、酒類に対する高率の物品税（Cukai）や厳しい流通規制が存在します。しかし、ヒンドゥー文化が根付き外国人観光客が集うバリ島では、熱帯の気候に適したブドウ品種の改良や地場産ハーブを用いたクラフトビールなど、独自のクラフト醸造文化が開花しています。",
        "passage": """Sebagai negara dengan populasi Muslim terbesar di dunia, Republik Indonesia menerapkan regulasi yang sangat ketat dan tarif cukai yang amat tinggi terhadap peredaran minuman beralkohol. Peraturan Menteri Perdagangan membatasi jalur distribusi minuman keras hanya pada hotel berbintang, restoran berizin khusus, dan kawasan pariwisata internasional. Di tengah lanskap regulasi yang restriktif ini, Pulau Dewata Bali tampil sebagai episentrum anomali sekaligus laboratorium kreatif bagi berkembangnya industri minuman fermentasi lokal yang mandiri dan berdaya saing.

Salah satu terobosan paling fenomenal adalah keberhasilan industri anggur lokal, seperti Hatten Wines dan Sababay Winery, dalam mematahkan mitos bahwa tanaman anggur (Vitis vinifera) tidak dapat menghasilkan wine berkualitas tinggi di iklim tropis. Dengan memanfaatkan iklim mikro pesisir Bali utara di Buleleng yang kering dan berangin, para petani lokal bermitra dengan pembuat anggur (winemaker) internasional untuk membudidayakan varietas Probel dan Alphonse Lavallée. Menariknya, ketiadaan musim dingin di khatulistiwa memungkinkan panen anggur berlangsung sepanjang tahun (evergreen cycle), menghasilkan karakter rasa yang segar dan unik yang kini menyabet berbagai penghargaan di panggung internasional.

Seiring dengan gelombang selera konsumen generasi baru, industri bir kerajinan (craft beer) lokal juga mengalami lonjakan popularitas yang luar biasa di Bali. Produsen mikro seperti Kura Kura Beer, Black Sand Brewery, dan Island Brewing meracik bir artisanal dengan menginfus bahan-bahan botani asli Nusantara, mulai dari kopi Kintamani, jeruk nipis, jahe, hingga rempah-rempah tropis lainnya. Kehadiran produk-produk ini menawarkan diferensiasi yang kuat di tengah dominasi merek bir industri raksasa yang telah bercokol puluhan tahun.

Keberhasilan produsen minuman fermentasi di Bali membuktikan bahwa batasan regulasi fiskal justru memicu lahirnya inovasi berbasis substitusi impor bernilai tambah tinggi. Dengan menggabungkan teknologi modern, kemitraan agrikultur bersama petani lokal, serta narasi budaya pariwisata yang otentik, Bali berhasil menempatkan dirinya sebagai salah satu destinasi gastronomi beralkohol paling unik dan disegani di kawasan Asia Tenggara.""",
        "vocab": [
            ("tarif cukai", "名詞句", "物品税率、酒税率", "Pemerintah menaikkan tarif cukai untuk menekan konsumsi alkohol."),
            ("regulasi restriktif", "名詞句", "制限的・厳格な規制", "Industri beroperasi di tengah regulasi restriktif yang berlapis."),
            ("industri minuman fermentasi", "名詞句", "発酵飲料産業（ワイン・ビール等）", "Industri minuman fermentasi lokal menyerap ratusan tenaga kerja."),
            ("mematahkan mitos", "成句動詞", "神話・先入観を打破する", "Keberhasilan mereka berhasil mematahkan mitos yang telah lama beredar."),
            ("panen sepanjang tahun", "名詞句", "通年収穫 (evergreen cycle)", "Iklim tropis memungkinkan panen sepanjang tahun tanpa henti."),
            ("menyabet penghargaan", "動詞句 (口語的文語)", "賞を総なめにする、勝ち取る", "Produk lokal menyabet berbagai penghargaan bergengsi tingkat dunia."),
            ("bir kerajinan", "名詞句", "クラフトビール (craft beer)", "Tren bir kerajinan mulai digemari kalangan menengah perkotaan."),
            ("diferensiasi yang kuat", "名詞句", "強力な差別化", "Bahan botani lokal memberikan diferensiasi yang kuat pada cita rasa."),
            ("substitusi impor", "名詞句 (経済用語)", "輸入代替", "Produksi dalam negeri diarahkan untuk mendukung substitusi impor."),
            ("destinasi gastronomi", "名詞句", "美食観光の目的地", "Bali bertransformasi menjadi destinasi gastronomi kelas dunia.")
        ],
        "paragraphs": [
            ("Sebagai negara dengan populasi Muslim terbesar di dunia, Republik Indonesia menerapkan regulasi yang sangat ketat dan tarif cukai yang amat tinggi terhadap peredaran minuman beralkohol. Peraturan Menteri Perdagangan membatasi jalur distribusi minuman keras hanya pada hotel berbintang, restoran berizin khusus, dan kawasan pariwisata internasional. Di tengah lanskap regulasi yang restriktif ini, Pulau Dewata Bali tampil sebagai episentrum anomali sekaligus laboratorium kreatif bagi berkembangnya industri minuman fermentasi lokal yang mandiri dan berdaya saing.",
             "世界最大のイスラム教徒人口を抱える国家として、インドネシア共和国は酒類の流通に対して極めて厳格な規制と非常に高率な物品税（酒税）を適用している。商業省令は酒類の流通ルートを星付きホテル、特別営業許可を持つレストラン、国際観光特区のみに制限している。この厳格な規制環境の只中で、「神々の島」バリは例外的な震源地であると同時に、自立的で競争力ある地場発酵飲料産業の発展に向けた創造的実験場として立ち現れている。",
             "同格前置詞句「Sebagai negara dengan populasi...」、対比の前置詞句「Di tengah lanskap regulasi yang restriktif ini, ...」、成句的表現「tampil sebagai episentrum anomali sekaligus laboratorium kreatif（例外の中心かつ創造的実験室として姿を現す）」。"),
            ("Salah satu terobosan paling fenomenal adalah keberhasilan industri anggur lokal dalam mematahkan mitos bahwa tanaman anggur tidak dapat menghasilkan wine berkualitas tinggi di iklim tropis. Dengan memanfaatkan iklim mikro pesisir Bali utara di Buleleng yang kering dan berangin, para petani lokal bermitra dengan pembuat anggur internasional untuk membudidayakan varietas Probel dan Alphonse Lavallée. Menariknya, ketiadaan musim dingin di khatulistiwa memungkinkan panen anggur berlangsung sepanjang tahun, menghasilkan karakter rasa yang segar dan unik yang kini menyabet berbagai penghargaan di panggung internasional.",
             "最も目覚ましいブレークスルーの一つは、熱帯気候ではブドウ樹が高品質なワインを生み出せないという神話を地場ワイン産業が打ち破った成功である。乾燥し風通しの良いブレレン県北バリ沿岸の微気候（マイクロクライメット）を活用し、地元農家は国際的な醸造家と提携してプロベル種やアルフォンス・ラヴァレ種を栽培している。興味深いことに、赤道直下に冬がないことはブドウの通年収穫を可能にし、国際舞台で数々の賞を勝ち取る新鮮でユニークな味わいの個性を生み出している。",
             "関係名詞節「mematahkan mitos bahwa...」、手段の前置詞句「Dengan memanfaatkan iklim mikro...」、接続詞的副詞「Menariknya（興味深いことに）」、使役構文「memungkinkan panen anggur berlangsung...（収穫が持続することを可能にする）」。"),
            ("Seiring dengan gelombang selera konsumen generasi baru, industri bir kerajinan lokal juga mengalami lonjakan popularitas yang luar biasa di Bali. Produsen mikro seperti Kura Kura Beer, Black Sand Brewery, dan Island Brewing meracik bir artisanal dengan menginfus bahan-bahan botani asli Nusantara, mulai dari kopi Kintamani, jeruk nipis, jahe, hingga rempah-rempah tropis lainnya. Kehadiran produk-produk ini menawarkan diferensiasi yang kuat di tengah dominasi merek bir industri raksasa yang telah bercokol puluhan tahun.",
             "新世代消費者の嗜好の波に伴い、クラフトビール（手造りビール）産業もバリ島で並外れた人気の急上昇を経験している。クラ・クラ・ビール、ブラック・サンド・ブルワリー、アイランド・ブリューイングといったマイクロブルワリーは、キンタマーニ・コーヒー、ライム、生姜からその他の熱帯スパイスに至るまで、群島本来のボタニカル素材をインフューズ（浸漬抽出）して職人技のビールを調合している。これらの製品の登場は、数十年にわたり居座ってきた巨大産業ビールブランドの支配の中で強力な差別化を提供している。",
             "前置詞句「Seiring dengan gelombang selera...」、手段を表す分詞構文「dengan menginfus bahan-bahan botani...」、関係代名詞「yang telah bercokol puluhan tahun（数十年間居座り続けてきた）」。"),
            ("Keberhasilan produsen minuman fermentasi di Bali membuktikan bahwa batasan regulasi fiskal justru memicu lahirnya inovasi berbasis substitusi impor bernilai tambah tinggi. Dengan menggabungkan teknologi modern, kemitraan agrikultur bersama petani lokal, serta narasi budaya pariwisata yang otentik, Bali berhasil menempatkan dirinya sebagai salah satu destinasi gastronomi beralkohol paling unik dan disegani di kawasan Asia Tenggara.",
             "バリ島の発酵飲料メーカーの成功は、財政的規制の制約がむしろ高付加価値な輸入代替に基づくイノベーションの誕生を刺激したことを証明している。最新技術、地元農家との農業パートナーシップ、そして本物の観光文化ナラティブを融合させることで、バリ島は東南アジア地域で最もユニークかつ一目置かれるアルコール・ガストロノミーの目的地として自らを位置づけることに成功した。",
             "名詞節「membuktikan bahwa batasan... justru memicu...」、再帰代名詞を用いた動詞句「berhasil menempatkan dirinya sebagai...（自らを〜として位置づけることに成功した）」、形容詞連鎖「paling unik dan disegani（最もユニークかつ尊敬される）」。")
        ],
        "grammar": [
            ("成句 mematahkan mitos（神話を打破する、先入観を覆す）", "語根 patah（折れる）に使役接頭辞 meN- が付いた mematahkan（へし折る）と mitos（神話・誤った通念）が結合した表現。「従来の固定観念を科学的・実証的に打破する」という論説の定番成句です。"),
            ("動詞 bercokol（居座る、根を張って動かない）", "元々は動物や鳥が巣にうずくまる動作を指しますが、市場や政治で「巨大企業や既得権益が長期間にわたって地位を独占し続けている」状態をやや批判的・対比的に描写する際に使われます。"),
            ("副詞 justru（かえって、むしろ、まさに）", "一般的な予想（規制が産業を衰退させる）に反して、「むしろ規制があったからこそ輸入代替イノベーションが促進された」という逆説的因果関係を鮮やかに示す論理接続詞です。")
        ],
        "quiz": [
            {
                "q": "Di kawasan manakah perkebunan anggur di Bali yang memanfaatkan iklim mikro kering dan berangin?",
                "options": ["Ubud, Gianyar", "Buleleng, Bali Utara", "Kuta, Badung", "Nusa Dua, Bali Selatan"],
                "ans": "Buleleng, Bali Utara",
                "exp": "第2段落に「Dengan memanfaatkan iklim mikro pesisir Bali utara di Buleleng yang kering dan berangin」と明記されています。"
            },
            {
                "q": "Apa keunikan siklus panen anggur di iklim tropis khatulistiwa menurut teks?",
                "options": ["Hanya bisa dipanen lima tahun sekali", "Dapat dipanen sepanjang tahun (evergreen cycle)", "Harus dipanen saat musim salju buatan", "Hanya tumbuh di dalam gua bawah tanah"],
                "ans": "Dapat dipanen sepanjang tahun (evergreen cycle)",
                "exp": "第2段落後半に「ketiadaan musim dingin di khatulistiwa memungkinkan panen anggur berlangsung sepanjang tahun (evergreen cycle)」とあります。"
            },
            {
                "q": "Bahan botani asli Nusantara apa saja yang diinfus ke dalam bir kerajinan lokal di Bali?",
                "options": ["Keju dan gandum Eropa", "Kopi Kintamani, jeruk nipis, jahe, dan rempah tropis", "Susu sapi dan teh hijau Jepang", "Minyak kelapa sawit murni"],
                "ans": "Kopi Kintamani, jeruk nipis, jahe, dan rempah tropis",
                "exp": "第3段落に「menginfus bahan-bahan botani asli Nusantara, mulai dari kopi Kintamani, jeruk nipis, jahe, hingga rempah-rempah tropis lainnya」と記載されています。"
            }
        ],
        "column": """### 深層コラム：神事のお神酒「アラック（Arak）」とバリ州知事令第1号

バリ島における酒類は、単なる娯楽飲料にとどまらず、ヒンドゥー教の浄化儀礼「ブタ・ヤドニャ（Bhuta Yadnya）」において大地の精霊に捧げる神聖な供物「テタブハン（Tetabuhan）」としての重要な宗教的役割を持っています。

特にヤシの花蜜や米を発酵蒸留した伝統蒸留酒「Arak Bali」は、かつて密造酒として取り締まりの対象になりがちでした。しかし2020年、バリ州知事は「バリ伝統発酵蒸留酒の管理に関する知事令2020年第1号」を制定し、アラックの製造・品質基準・ブランド化を公式に合法化・奨励しました。現在では、メキシコのテキーラや日本の日本酒のように、アラックを国際的スピリッツとして確立させる産官学の取り組みが加速しています。"""
    },
    {
        "filename": "42-cross-border-digital-payment.md",
        "title": "42. ASEAN域内QR決済相互接続：シンガポール・タイ・マレーシアと自国通貨で直接決済",
        "category": "長文読解・フィンテック・国際金融",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "インドネシア中央銀行（BI）が主導する即時QRコード決済システム「QRIS」は、国内の普及にとどまらず、タイ、マレーシア、シンガポールとの相互接続を実現しました。米ドルを介さず自国通貨間で即時両替・決済する「Local Currency Transaction (LCT)」の革新と、ASEAN経済共同体のデジタル統合の未来を読み解きます。",
        "passage": """Integrasi ekonomi di kawasan Perhimpunan Bangsa-Bangsa Asia Tenggara (ASEAN) mencapai tonggak sejarah baru melalui implementasi interkoneksi pembayaran lintas batas (cross-border payment) berbasis Quick Response Code Indonesian Standard (QRIS). Diinisiasi oleh Bank Indonesia (BI) bersama bank sentral negara-negara tetangga, inisiatif ini memungkinkan wisatawan dan pelaku usaha mikro untuk melakukan transaksi keuangan internasional semudah memindai kode QR di kasir, langsung menggunakan aplikasi pembayaran dari negara asal masing-masing.

Skema pembayaran lintas batas ini telah beroperasi secara penuh antara Indonesia dengan Thailand, Malaysia, dan Singapura. Sebagai contoh, pelancong Indonesia yang berkunjung ke Bangkok atau Kuala Lumpur kini dapat langsung memindai kode QR PromptPay atau DuitNow menggunakan dompet digital domestik seperti GoPay, OVO, atau aplikasi mobile banking nasional tanpa perlu menukarkan uang tunai fisik ke valuta asing terlebih dahulu. Sebaliknya, turis dari negara-negara mitra dapat memindai barcode QRIS di jutaan pedagang kaki lima hingga pusat perbelanjaan di Tanah Air.

Aspek paling revolusioner dari arsitektur pembayaran ini adalah penerapan mekanisme Transaksi Mata Uang Lokal (Local Currency Transaction/LCT). Selama beberapa dekade, transaksi perdagangan dan pariwisata internasional di kawasan ini selalu bergantung pada dolar Amerika Serikat (USD) sebagai mata uang perantara (invoicing currency), yang memicu biaya konversi ganda serta ketergantungan likuiditas terhadap sistem keuangan global. Dengan skema LCT, rupiah langsung dikonversikan secara real-time ke baht, ringgit, atau dolar Singapura berdasarkan kurs kuotasi langsung antara bank-bank mitra (Appointed Cross Currency Dealer/ACCD).

Keberhasilan konektivitas QR regional ini tidak hanya memangkas biaya transaksi bagi konsumen dan mengikis dominasi jaringan kartu kredit global, melainkan juga mempercepat digitalisasi sektor UMKM yang menjadi tulang punggung perekonomian kawasan. ASEAN kini dipandang sebagai pelopor global dalam interoperabilitas sistem pembayaran lintas batas, membuktikan bahwa integrasi ekonomi regional dapat diwujudkan secara nyata tanpa harus membentuk mata uang tunggal seperti kawasan Euro.""",
        "vocab": [
            ("tonggak sejarah", "名詞句", "歴史の金字塔、画期的マイルストーン", "Kesepakatan ini menjadi tonggak sejarah kerja sama moneter ASEAN."),
            ("pembayaran lintas batas", "名詞句", "越境決済 (Cross-border Payment)", "Sistem pembayaran lintas batas mempermudah arus wisatawan."),
            ("mata uang perantara", "名詞句", "媒介通貨 (intermediary / invoicing currency)", "Ketergantungan pada mata uang perantara meningkatkan risiko kurs."),
            ("biaya konversi ganda", "名詞句", "二重為替手数料", "Skema LCT menghapus biaya konversi ganda yang membebani nasabah."),
            ("kurs kuotasi langsung", "名詞句", "直接為替レート", "Transaksi diselesaikan dengan kurs kuotasi langsung rupiah-ringgit."),
            ("memangkas biaya transaksi", "動詞句", "取引コストを大幅に削減する", "Inovasi digital terbukti mampu memangkas biaya transaksi UMKM."),
            ("mengikis dominasi", "動詞句", "支配的地位を削ぎ落とす・弱める", "Jaringan QR lokal mulai mengikis dominasi kartu kredit asing."),
            ("interoperabilitas", "名詞", "相互運用性 (Interoperability)", "Interoperabilitas sistem perbankan regional meningkatkan efisiensi."),
            ("mata uang tunggal", "名詞句", "単一通貨 (Single Currency)", "ASEAN memilih integrasi digital tanpa mengadopsi mata uang tunggal."),
            ("arsitektur pembayaran", "名詞句", "決済アーキテクチャ・決済基盤構造", "BI merancang arsitektur pembayaran modern yang berdaulat.")
        ],
        "paragraphs": [
            ("Integrasi ekonomi di kawasan ASEAN mencapai tonggak sejarah baru melalui implementasi interkoneksi pembayaran lintas batas berbasis QRIS. Diinisiasi oleh Bank Indonesia bersama bank sentral negara-negara tetangga, inisiatif ini memungkinkan wisatawan dan pelaku usaha mikro untuk melakukan transaksi keuangan internasional semudah memindai kode QR di kasir, langsung menggunakan aplikasi pembayaran dari negara asal masing-masing.",
             "ASEAN地域における経済統合は、QRISを基盤とする越境決済相互接続の実装を通じて新たな歴史的マイルストーンに到達した。インドネシア中央銀行（BI）が近隣諸国の中央銀行とともに主導したこのイニシアチブは、旅行者や零細事業者が、各々の母国の決済アプリを直接使用してレジのQRコードをスキャンするのと同じ手軽さで国際金融取引を行うことを可能にしている。",
             "受動態分詞節「Diinisiasi oleh...（〜によって開始され）」、使役構文「memungkinkan wisatawan... untuk melakukan...（旅行者が〜を行うことを可能にする）」、比較表現「semudah memindai kode QR（QRコードをスキャンするのと同じくらい容易に）」。"),
            ("Skema pembayaran lintas batas ini telah beroperasi secara penuh antara Indonesia dengan Thailand, Malaysia, dan Singapura. Pelancong Indonesia yang berkunjung ke Bangkok atau Kuala Lumpur kini dapat langsung memindai kode QR PromptPay atau DuitNow menggunakan dompet digital domestik tanpa perlu menukarkan uang tunai fisik ke valuta asing terlebih dahulu. Sebaliknya, turis dari negara-negara mitra dapat memindai barcode QRIS di jutaan pedagang kaki lima di Tanah Air.",
             "この越境決済スキームは、インドネシアとタイ、マレーシア、シンガポールとの間で完全稼働している。バンコクやクアラルンプールを訪れるインドネシア人旅行者は、事前に現金を外貨へ両替する必要なく、国内の電子ウォレットを使って現地のPromptPayやDuitNowのQRコードを直接スキャンできる。逆に、提携国からの観光客も国内の何百万もの屋台からショッピングモールに至るまでQRISのバーコードをスキャンできる。",
             "副詞句「secara penuh（完全に）」、前置詞句「tanpa perlu menukarkan... terlebih dahulu（あらかじめ両替する必要なく）」、対比接続詞「Sebaliknya（逆に、これに対して）」。"),
            ("Aspek paling revolusioner dari arsitektur pembayaran ini adalah penerapan mekanisme Transaksi Mata Uang Lokal (LCT). Selama beberapa dekade, transaksi internasional di kawasan ini selalu bergantung pada dolar AS sebagai mata uang perantara, yang memicu biaya konversi ganda serta ketergantungan likuiditas. Dengan skema LCT, rupiah langsung dikonversikan secara real-time ke baht, ringgit, atau dolar Singapura berdasarkan kurs kuotasi langsung antara bank-bank mitra (ACCD).",
             "この決済アーキテクチャの最も革命的な側面は、自国通貨取引（LCT）メカニズムの適用である。過去数十年間にわたり、この地域の国際取引は媒介通貨としての米ドルに常に依存しており、これが二重為替手数料や流動性依存を引き起こしていた。LCTスキームにより、ルピアは指定適格クロス・カレンシー・ディーラー（ACCD）銀行間の直接為替レートに基づき、タイ・バーツ、マレーシア・リンギット、シンガポール・ドルへリアルタイムで直接両替される。",
             "関係代名詞「yang memicu biaya konversi...」、前置詞句「berdasarkan kurs kuotasi langsung（直接相場レートに基づいて）」、受動構文「langsung dikonversikan secara real-time（リアルタイムで直接両替される）」。"),
            ("Keberhasilan konektivitas QR regional ini tidak hanya memangkas biaya transaksi bagi konsumen dan mengikis dominasi jaringan kartu kredit global, melainkan juga mempercepat digitalisasi sektor UMKM. ASEAN kini dipandang sebagai pelopor global dalam interoperabilitas sistem pembayaran lintas batas, membuktikan bahwa integrasi ekonomi regional dapat diwujudkan secara nyata tanpa harus membentuk mata uang tunggal seperti kawasan Euro.",
             "この地域QR接続の成功は、消費者にとっての取引手数料を削減しグローバルなクレジットカード網の支配力を削ぎ落とすだけでなく、地域の経済の屋台骨である零細・中小企業（UMKM）セクターのデジタル化を加速させている。ASEANは現在、越境決済システムの相互運用性における世界的な先駆者と見なされており、ユーロ圏のような単一通貨を創設せずとも、地域経済統合が目に見える形で実現できることを証明している。",
             "相関接続詞「tidak hanya memangkas... melainkan juga mempercepat...」、比喩的動詞「mengikis dominasi（支配力を削ぎ落とす）」、条件否定構文「tanpa harus membentuk mata uang tunggal（単一通貨を形成することなく）」。")
        ],
        "grammar": [
            ("成句 tonggak sejarah（歴史の節目、金字塔、画期的マイルストーン）", "tonggak（杭・柱）と sejarah（歴史）が結合した表現。重要な国際条約の調印や画期的技術の導入など、歴史を大きく前に進める出来事を形容する格調高い成句です。"),
            ("金融成句 Local Currency Transaction (LCT) とその統語", "インドネシア語では「Transaksi Mata Uang Lokal」と訳されます。以前は Local Currency Settlement (LCS) と呼ばれていましたが、決済（Settlement）だけでなく投資や送金を含む包括的取引（Transaction）へと枠組みが拡大改称されました。"),
            ("動詞 mengikis（削ぎ落とす、徐々に減退させる）の比喩的用法", "土壌浸食（erosi）の動作を表す語根 kikis に接頭辞 meN- が付いた動詞。「mengikis dominasi（独占的支配を突き崩す）」、「mengikis kemiskinan（貧困を徐々に根絶する）」など、強固な対象を少しずつ減衰させる比喩として多用されます。")
        ],
        "quiz": [
            {
                "q": "Sistem kode QR nasional milik negara mana saja yang telah terhubung penuh dengan QRIS Indonesia?",
                "options": ["Jepang, Korea Selatan, dan Tiongkok", "Thailand (PromptPay), Malaysia (DuitNow), dan Singapura (NETS)", "Inggris, Prancis, dan Jerman", "Australia dan Selandia Baru"],
                "ans": "Thailand (PromptPay), Malaysia (DuitNow), dan Singapura (NETS)",
                "exp": "第2段落に「antara Indonesia dengan Thailand, Malaysia, dan Singapura. Pelancong... memindai kode QR PromptPay atau DuitNow」と記載されています。"
            },
            {
                "q": "Apa manfaat utama dari penerapan mekanisme Local Currency Transaction (LCT)?",
                "options": ["Mewajibkan semua orang menggunakan uang kertas dolar AS", "Menghapus ketergantungan pada dolar AS dan menghilangkan biaya konversi ganda", "Menghapus seluruh pajak penjualan di toko bebas bea", "Membuat seluruh bank swasta ditutup oleh pemerintah"],
                "ans": "Menghapus ketergantungan pada dolar AS dan menghilangkan biaya konversi ganda",
                "exp": "第3段落に「bergantung pada dolar AS sebagai mata uang perantara... Dengan skema LCT, rupiah langsung dikonversikan secara real-time」とあります。"
            },
            {
                "q": "Pelajaran apa yang ditunjukkan integrasi pembayaran ASEAN dibandingkan dengan Uni Eropa?",
                "options": ["ASEAN harus segera mencetak uang kertas bersama", "Integrasi ekonomi dapat diwujudkan secara nyata tanpa membentuk mata uang tunggal", "ASEAN gagal mengadopsi teknologi digital perbankan", "Uni Eropa tidak memiliki sistem pembayaran kartu kredit"],
                "ans": "Integrasi ekonomi dapat diwujudkan secara nyata tanpa membentuk mata uang tunggal",
                "exp": "最終段落末尾に「membuktikan bahwa integrasi ekonomi regional dapat diwujudkan secara nyata tanpa harus membentuk mata uang tunggal seperti kawasan Euro」と明記されています。"
            }
        ],
        "column": """### 深層コラム：屋台（Kaki Lima）が外貨を稼ぐ日：QRIS普及率4,000万店舗の衝撃

かつて東南アジアの旅行といえば、空港や街路の両替商（Money Changer）で現地の紙幣を手に入れ、小銭の計算に頭を悩ませるのが当たり前でした。

しかしインドネシア中銀が2019年に導入した「QRIS」は、わずか数年で4,000万以上の加盟店（その9割以上が零細屋台・個人商店）に普及しました。今日では、ジャカルタの路上でバクソ（肉団子スープ）を売る屋台や、バリ島のビーチでココナッツを売るおばちゃんのQRコードを、シンガポールやマレーシアの観光客が自国のスマホアプリで「ピッ」と読み取るだけで、手数料ほぼゼロで自国通貨即時決済が完了します。国家主導のデジタルインフラが草の根の庶民経済を世界経済へ直結させた、世界で最も成功したフィンテック事例の一つです。"""
    },
    {
        "filename": "43-elderly-care-demographic-shift.md",
        "title": "43. 超高齢社会の足音：若年人口ボーナスの終了を見据えた介護保険と高齢者ケア制度",
        "category": "長文読解・人口問題・社会保障",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "豊富な若年労働人口を誇り「人口ボーナス（Bonus Demografi）」の真っ只中にあるインドネシアですが、2035〜2040年頃には急速な少子高齢化の波が到来すると予測されています。伝統的な「家族扶養（孝行）」の限界、未整備な公的介護保険（Long-Term Care）、そして持続可能な社会保障制度改革の最前線を検証します。",
        "passage": """Secara demografis, Indonesia saat ini sedang menikmati periode emas yang dikenal sebagai 'bonus demografi', di mana proporsi penduduk usia produktif (15–64 tahun) mencapai lebih dari dua pertiga dari total populasi nasional. Struktur demografi yang sangat menguntungkan ini menjadi pendorong utama pertumbuhan ekonomi dan daya tarik investasi manufaktur. Namun, di balik narasi optimisme tersebut, para pakar demografi memperingatkan bahwa jendela peluang ini akan segera menutup sekitar tahun 2035 hingga 2040, ketika laju penuaan penduduk (aging population) melonjak secara eksponensial.

Indonesia diproyeksikan akan bertransisi dari masyarakat menua (aging society) menjadi masyarakat tua (aged society) dalam kurun waktu yang jauh lebih singkat dibandingkan negara-negara maju di Eropa atau Jepang. Fenomena 'menjadi tua sebelum menjadi kaya' (getting old before getting rich) menjadi ancaman nyata yang membayangi masa depan bangsa. Sementara negara-negara maju memiliki waktu puluhan tahun untuk membangun jaring pengaman sosial dan dana pensiun yang mapan sebelum proporsi lansia membengkak, Indonesia menghadapi risiko keterbatasan kapasitas fiskal dan rendahnya cakupan perlindungan hari tua.

Tantangan paling genting terletak pada runtuhnya model pengasuhan lansia tradisional yang selama berabad-abad bertumpu pada institusi keluarga besar (filial piety). Perubahan struktur sosial perkotaan, migrasi pemuda ke kota-kota besar, menyusutnya ukuran keluarga inti, serta meningkatnya partisipasi perempuan dalam angkatan kerja formal membuat tugas merawat orang tua renta di rumah tidak lagi mudah dipertahankan. Konsekuensinya, fenomena 'generasi roti lapis' (sandwich generation) yang terhimpit beban ganda membiayai anak sekaligus merawat orang tua semakin merebak di kalangan kelas pekerja urban.

Hingga saat ini, sistem jaminan sosial nasional (BPJS Kesehatan dan BPJS Ketenagakerjaan) belum memiliki skema khusus untuk Perawatan Jangka Panjang (Long-Term Care/LTC) bagi lansia yang mengalami disabilitas fungsional. Merespons bom waktu demografis ini, pemerintah dan masyarakat sipil mulai merancang integrasi layanan perawatan lansia berbasis komunitas (community-based elderly care), pemberdayaan kader posyandu lansia di tingkat rukun tetangga, serta reformasi skema pensiun wajib guna memastikan kehidupan hari tua yang bermartabat bagi seluruh warga negara.""",
        "vocab": [
            ("bonus demografi", "名詞句", "人口ボーナス", "Pemanfaatan bonus demografi harus diimbangi penciptaan lapangan kerja."),
            ("jendela peluang", "名詞句", "好機の窓 (window of opportunity)", "Jendela peluang bonus demografi akan tertutup dalam dua dekade."),
            ("laju penuaan penduduk", "名詞句", "高齢化の進展速度", "Laju penuaan penduduk menuntut kesiapan sistem kesehatan."),
            ("jaring pengaman sosial", "名詞句", "社会安全網 (Social Safety Net)", "Jaring pengaman sosial harus diperluas untuk mencakup warga lansia."),
            ("keterbatasan kapasitas fiskal", "名詞句", "財政余力の限界", "Keterbatasan kapasitas fiskal menghambat subsidi pensiun universal."),
            ("runtuhnya model pengasuhan", "名詞句", "扶養・介護モデルの崩壊", "Urbanisasi memicu runtuhnya model pengasuhan lansia tradisional."),
            ("institusi keluarga besar", "名詞句", "拡大家族制度", "Nilai-nilai dalam institusi keluarga besar mulai mengalami pergeseran."),
            ("disabilitas fungsional", "名詞句", "機能的障害・要介護状態", "Lansia dengan disabilitas fungsional membutuhkan asisten perawat."),
            ("bom waktu demografis", "名詞句", "人口動態の時限爆弾", "Pemerintah harus bersiap menghadapi bom waktu demografis."),
            ("kehidupan hari tua bermartabat", "名詞句", "尊厳ある老後生活", "Negara wajib menjamin kehidupan hari tua yang bermartabat bagi pensiunan.")
        ],
        "paragraphs": [
            ("Secara demografis, Indonesia saat ini sedang menikmati periode emas yang dikenal sebagai 'bonus demografi', di mana proporsi penduduk usia produktif mencapai lebih dari dua pertiga dari total populasi nasional. Struktur demografi yang sangat menguntungkan ini menjadi pendorong utama pertumbuhan ekonomi. Namun, para pakar demografi memperingatkan bahwa jendela peluang ini akan segera menutup sekitar tahun 2035 hingga 2040, ketika laju penuaan penduduk melonjak secara eksponensial.",
             "人口動態的に、インドネシアは現在「人口ボーナス」として知られる黄金期を謳歌しており、生産年齢人口（15〜64歳）の割合が国家総人口の3分の2以上に達している。この極めて有利な人口構成は、経済成長の主要な牽引役となっている。しかし人口動態の専門家たちは、高齢化の進展速度が指数関数的に跳ね上がる2035年から2040年頃には、この好機の窓がまもなく閉じるだろうと警鐘を鳴らしている。",
             "副詞句「Secara demografis（人口学的に）」、関係副詞「di mana proporsi... mencapai...」、比喩表現「jendela peluang akan menutup（好機の窓が閉じる）」、時間副詞節「ketika laju penuaan penduduk melonjak...」。"),
            ("Indonesia diproyeksikan akan bertransisi dari masyarakat menua menjadi masyarakat tua dalam kurun waktu yang jauh lebih singkat dibandingkan negara-negara maju di Eropa atau Jepang. Fenomena 'menjadi tua sebelum menjadi kaya' menjadi ancaman nyata yang membayangi masa depan bangsa. Sementara negara-negara maju memiliki waktu puluhan tahun untuk membangun jaring pengaman sosial sebelum proporsi lansia membengkak, Indonesia menghadapi risiko keterbatasan kapasitas fiskal.",
             "インドネシアは、ヨーロッパの先進諸国や日本と比較して遥かに短い期間で「高齢化社会」から「高齢社会」へと移行すると予測されている。「豊かになる前に老いる（getting old before getting rich）」という現象は、国家の未来に影を落とす現実の脅威となっている。先進諸国が高齢者比率の膨張に先立って社会安全網を構築するために数十年の時間を持っていたのに対し、インドネシアは財政余力の限界というリスクに直面している。",
             "受動態述語「diproyeksikan akan bertransisi（移行すると予測される）」、対比接続詞「Sementara...（〜である一方）」、比喩表現「membayangi masa depan bangsa（国家の未来に暗雲を投げかける）」。"),
            ("Tantangan paling genting terletak pada runtuhnya model pengasuhan lansia tradisional yang selama berabad-abad bertumpu pada institusi keluarga besar. Perubahan struktur sosial perkotaan, migrasi pemuda ke kota-kota besar, menyusutnya ukuran keluarga inti, serta meningkatnya partisipasi perempuan dalam angkatan kerja formal membuat tugas merawat orang tua renta di rumah tidak lagi mudah dipertahankan. Konsekuensinya, fenomena 'generasi roti lapis' semakin merebak di kalangan kelas pekerja urban.",
             "最も差し迫った課題は、何世紀にもわたり拡大家族の制度に依存してきた伝統的な高齢者扶養・介護モデルの崩壊にある。都市の社会構造の変化、大都市への若者の移住、核家族サイズの縮小、そしてフォーマル労働力への女性の社会進出の増加は、老親を自宅で介護する役割を維持することをもはや困難にしている。その結果として、子どもの養育費と親の介護負担に二重に挟まれる『サンドイッチ世代』現象が、都市の労働者層の間でますます蔓延している。",
             "最上級形容詞句「Tantangan paling genting terletak pada...」、名詞列挙主語「Perubahan struktur..., migrasi..., menyusutnya..., serta meningkatnya...」、使役動詞「membuat tugas merawat... tidak lagi mudah dipertahankan（維持を容易でなくさせている）」。"),
            ("Hingga saat ini, sistem jaminan sosial nasional belum memiliki skema khusus untuk Perawatan Jangka Panjang (LTC) bagi lansia yang mengalami disabilitas fungsional. Merespons bom waktu demografis ini, pemerintah dan masyarakat sipil mulai merancang integrasi layanan perawatan lansia berbasis komunitas, pemberdayaan kader posyandu lansia di tingkat RT, serta reformasi skema pensiun wajib guna memastikan kehidupan hari tua yang bermartabat bagi seluruh warga negara.",
             "現在に至るまで、国民社会保障制度（BPJS健康および雇用）には、身体的・機能的障害を抱える高齢者のための長期介護（LTC）に特化した公的スキームが存在していない。この人口動態の時限爆弾に対応し、政府と市民社会は、地域コミュニティ密着型の高齢者ケアサービスの統合、住民組織（RT）レベルでの高齢者保健ポスト（Posyandu Lansia）幹部の育成、そして全市民の尊厳ある老後生活を保障するための義務的年金制度の改革を計画し始めている。",
             "現在完了否定「belum memiliki skema khusus...」、分詞節「Merespons bom waktu demografis ini, ...（この人口時限爆弾に応答して）」、目的接続詞「guna memastikan kehidupan hari tua yang bermartabat（尊厳ある老後生活を確実にするため）」。")
        ],
        "grammar": [
            ("成句 bom waktu demografis（人口動態の時限爆弾）", "爆発（社会崩壊・財政破綻）までの猶予期間が刻一刻と迫る深刻な社会構造問題を、時限爆弾（bom waktu）に喩えたジャーナリズム・論説表現です。"),
            ("動詞 menyusut（縮む、収縮する）の派生名詞化 menyusutnya", "語根 susut（減少する、縮小する）に接尾辞 -nya が付き、「核家族の規模が縮小していること」という動名詞的意味を形成します。"),
            ("比喩成句 menjadi tua sebelum menjadi kaya", "英語の 'getting old before getting rich' の直訳。人口ボーナス期に十分な資本蓄積と社会保障インフラを確立できないまま少子高齢化に突入する新興国の最大の構造的罠を指します。")
        ],
        "quiz": [
            {
                "q": "Kapan jendela peluang 'bonus demografi' di Indonesia diproyeksikan akan menutup?",
                "options": ["Tahun 2025", "Sekitar tahun 2035 hingga 2040", "Tahun 2075", "Tahun 2100"],
                "ans": "Sekitar tahun 2035 hingga 2040",
                "exp": "第1段落末尾に「jendela peluang ini akan segera menutup sekitar tahun 2035 hingga 2040」と明記されています。"
            },
            {
                "q": "Apa arti dari istilah 'generasi roti lapis' (sandwich generation) dalam konteks teks?",
                "options": ["Generasi yang gemar mengonsumsi makanan cepat saji", "Pekerja yang terhimpit beban membiayai anak sekaligus merawat orang tua lansia", "Generasi yang membuka usaha toko roti modern", "Anak-anak yang hidup mandiri tanpa orang tua"],
                "ans": "Pekerja yang terhimpit beban membiayai anak sekaligus merawat orang tua lansia",
                "exp": "第3段落に「terhimpit beban ganda membiayai anak sekaligus merawat orang tua semakin merebak di kalangan kelas pekerja urban」と説明されています。"
            },
            {
                "q": "Skema perawatan apa yang belum dimiliki oleh BPJS Kesehatan untuk lansia dengan keterbatasan fisik?",
                "options": ["Imunisasi balita", "Perawatan Jangka Panjang (Long-Term Care/LTC)", "Operasi katarak", "Pemeriksaan tensi darah gratis"],
                "ans": "Perawatan Jangka Panjang (Long-Term Care/LTC)",
                "exp": "第4段落冒頭に「belum memiliki skema khusus untuk Perawatan Jangka Panjang (Long-Term Care/LTC) bagi lansia yang mengalami disabilitas fungsional」と明記されています。"
            }
        ],
        "column": """### 深層コラム：インドネシアの草の根セーフティネット「ポスヤンドゥ・ランシア（Posyandu Lansia）」

インドネシアの地域社会には、乳幼児健診を行う「Posyandu（統合保健ポスト）」の仕組みを高齢者向けに応用した「Posyandu Lansia」が全国の村や町内会（RT/RW）に根付いています。

月1回、地域の公民館や住民の庭先に近所の高齢者たちが集まり、ボランティアの女性幹部（Kader Kesehatan）が血圧測定、血糖値・尿酸値チェック、健康体操（Senam Lansia）を実施します。公的な特別養護老人ホームが極めて限られる中、近隣住民同士が顔を合わせ、安否確認や孤独死防止を担うこの草の根システムは、世界が直面する超高齢化時代におけるコミュニティ主導型見守りモデルとして世界保健機関（WHO）からも高く評価されています。"""
    },
    {
        "filename": "44-preservation-oral-traditions.md",
        "title": "44. 消滅の危機に瀕する口承文芸と少数言語：消えゆく先住民族の叙事詩を記録する",
        "category": "長文読解・言語文化・人類学",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "世界第2位となる718もの地方言語（Bahasa Daerah）が存在する言語大国インドネシア。しかし急速な近代化や都市化、標準インドネシア語の普及に伴い、文字を持たず長老たちの口頭記憶だけで受け継がれてきた数多の先住言語や口承叙事詩（Tradisi Lisan）が、かつてない絶滅の危機に瀕しています。",
        "passage": """Dengan 718 bahasa daerah yang teridentifikasi secara ilmiah dari Sabang sampai Merauke, Indonesia dinobatkan sebagai salah satu laboratorium linguistik paling kaya dan paling kompleks di muka bumi. Sebagian besar dari khazanah bahasa ini terkonsentrasi di wilayah timur Nusantara, khususnya di Kepulauan Maluku dan Pulau Papua. Namun, di balik keanekaragaman yang menakjubkan tersebut, Badan Pengembangan dan Pembinaan Bahasa memperingatkan bahwa puluhan bahasa daerah kini berstatus punah, kritis, atau terancam punah seiring menyusutnya jumlah penutur jati (native speakers) usia muda.

Kerapuhan terbesar dialami oleh tradisi lisan (oral tradition), yakni khazanah kesastraan dan pengetahuan adat yang tidak pernah ditranskripsikan ke dalam aksara tulisan. Epik kepahlawanan kuno, nyanyian ritual pertanian, mantra penyembuhan tradisional, hingga silsilah hukum tanah adat selama berabad-abad hanya disimpan dalam ingatan para penutur sepuh (maestro tradisi). Contoh tragis adalah tradisi pelantunan epos 'La Galigo' di Sulawesi Selatan atau seni bertutur 'Didong' di Dataran Tinggi Gayo, di mana generasi pelantun ahli yang mampu mengingat ribuan bait puitis kini dapat dihitung dengan jari.

Ketika seorang maestro tradisi lisan wafat tanpa sempat mewariskan hafalannya kepada generasi penerus, maka satu peradaban pengetahuan ekologis dan filosofis musnah untuk selamanya. Fenomena ini kerap dianalogikan dengan pepatah Afrika: 'Setiap kali seorang tetua meninggal, itu sama seperti sebuah perpustakaan yang terbakar habis'. Tekanan homogenisasi budaya pop global, pergeseran bahasa pengantar di sekolah menjadi bahasa Indonesia baku, serta keengganan generasi muda mempelajari bahasa leluhur mempercepat proses kepunahan linguistik ini.

Menyadari urgensi eksistensial ini, gerakan revitalisasi bahasa dan dokumentasi digital mulai digalakkan secara masif oleh pemerintah, akademisi, dan komunitas adat. Peneliti linguistik menjelajahi pedalaman pulau-pulau terpencil untuk merekam audio visual pelantunan tradisi lisan beresolusi tinggi, mentranskripsikannya ke dalam format ortografi fonetik, serta menyusun kamus digital dwibahasa. Melalui integrasi kurikulum muatan lokal di sekolah dasar dan pemanfaatan media sosial oleh pemuda adat, asa untuk melestarikan memori kolektif bangsa tetap dinyalakan.""",
        "vocab": [
            ("khazanah linguistik", "名詞句", "言語の宝庫、言語資産", "Khazanah linguistik Papua menyimpan misteri asal-usul migrasi manusia."),
            ("penutur jati", "名詞句 (言語学用語)", "母語話者 (native speaker)", "Jumlah penutur jati bahasa daerah di Maluku kian menyusut."),
            ("tradisi lisan", "名詞句", "口承文芸、口承伝統 (Oral Tradition)", "Tradisi lisan diwariskan dari mulut ke mulut tanpa naskah tertulis."),
            ("penutur sepuh", "名詞句", "長老の話者、古老の語り部", "Hanya tersisa sedikit penutur sepuh yang menguasai epos kuno."),
            ("dihitung dengan jari", "成句動詞", "指折り数えるほど極めて少ない", "Jumlah maestro penenun tradisional kini dapat dihitung dengan jari."),
            ("homogenisasi budaya", "名詞句", "文化の画一化・均質化", "Globalisasi membawa dampak berupa homogenisasi budaya generasi muda."),
            ("urgensi eksistensial", "名詞句", "実存的・死活的な緊急性", "Kepunahan bahasa adalah urgensi eksistensial yang mengancam identitas."),
            ("transkripsi fonetik", "名詞句", "音声表記による転写", "Peneliti melakukan transkripsi fonetik terhadap nyanyian adat."),
            ("kurikulum muatan lokal", "名詞句 (教育用語)", "地域独自カリキュラム (Mulok)", "Bahasa daerah diajarkan kembali melalui kurikulum muatan lokal."),
            ("memori kolektif bangsa", "名詞句", "国民の集合的記憶", "Pelestarian tradisi lisan menjaga memori kolektif bangsa dari kepunahan.")
        ],
        "paragraphs": [
            ("Dengan 718 bahasa daerah yang teridentifikasi secara ilmiah dari Sabang sampai Merauke, Indonesia dinobatkan sebagai salah satu laboratorium linguistik paling kaya di muka bumi. Sebagian besar dari khazanah bahasa ini terkonsentrasi di wilayah timur Nusantara, khususnya di Maluku dan Papua. Namun, Badan Pengembangan dan Pembinaan Bahasa memperingatkan bahwa puluhan bahasa daerah kini berstatus punah, kritis, atau terancam punah seiring menyusutnya penutur jati usia muda.",
             "サバンからメラウケに至るまで科学的に特定された718もの地方言語を擁し、インドネシアは地球上で最も豊かで複雑な言語学的実験室の一つとして称されている。この言語資産の大部分は群島東部地域、特にマルク諸島やパプア島に集中している。しかし言語育成開発機構は、若年層の母語話者の減少に伴い、現在数十の地方言語が絶滅、危機的、あるいは絶滅危惧のステータスにあると警告している。",
             "前置詞句「Dengan 718 bahasa daerah yang teridentifikasi...」、受動構文「dinobatkan sebagai...（〜と称される）」、名詞化従属節「seiring menyusutnya jumlah penutur jati...（母語話者の減少に伴い）」。"),
            ("Kerapuhan terbesar dialami oleh tradisi lisan, yakni khazanah kesastraan dan pengetahuan adat yang tidak pernah ditranskripsikan ke dalam aksara tulisan. Epik kepahlawanan kuno, nyanyian ritual pertanian, hingga silsilah hukum tanah adat selama berabad-abad hanya disimpan dalam ingatan para penutur sepuh. Contoh tragis adalah epos 'La Galigo' di Sulawesi Selatan atau seni 'Didong' di Gayo, di mana pelantun ahli yang mampu mengingat ribuan bait kini dapat dihitung dengan jari.",
             "最大の脆弱性は、文字表記へと書き起こされたことのない文学的資産および慣習的知識である「口承伝統（Tradisi Lisan）」によって被られている。古代の英雄叙事詩、農業儀礼の歌、慣習土地法の系図に至るまでが、何世紀もの間、古老の語り部たちの記憶の中にのみ保存されてきた。悲劇的な例は南スラウェシの叙事詩『ラ・ガリゴ』やガヨ高地の口承芸術『ディドン』であり、何千もの詩節を記憶できる熟練の歌い手はいまや指で数えられるほどしか残っていない。",
             "同格の標識「yakni（すなわち）」、受動構文「hanya disimpan dalam ingatan...（記憶の中にのみ保管されている）」、慣用句「dapat dihitung dengan jari（指折り数えるほど少ない）」。"),
            ("Ketika seorang maestro tradisi lisan wafat tanpa sempat mewariskan hafalannya kepada generasi penerus, maka satu peradaban pengetahuan ekologis dan filosofis musnah untuk selamanya. Fenomena ini kerap dianalogikan dengan pepatah: 'Setiap kali seorang tetua meninggal, itu sama seperti sebuah perpustakaan yang terbakar habis'. Tekanan homogenisasi budaya pop global dan pergeseran bahasa pengantar di sekolah mempercepat proses kepunahan linguistik ini.",
             "ある口承伝統のマエストロが、その暗記記憶を後継世代に継承する暇もなく逝去した時、一つの生態学的・哲学的知識の文明が永遠に消滅する。この現象はしばしば『一人の長老が亡くなるたび、一つの図書館が全焼するのと同じである』というアフリカの諺に喩えられる。世界的なポップカルチャーの均質化圧力や学校の教授言語の標準語化が、この言語学的絶滅プロセスを加速させている。",
             "条件複文「Ketika... wafat tanpa sempat..., maka... musnah untuk selamanya」、受動表現「kerap dianalogikan dengan pepatah...（〜の諺でしばしば類比される）」、名詞連鎖「Tekanan homogenisasi..., pergeseran bahasa... mempercepat...」。"),
            ("Menyadari urgensi eksistensial ini, gerakan revitalisasi bahasa dan dokumentasi digital mulai digalakkan secara masif oleh pemerintah, akademisi, dan komunitas adat. Peneliti linguistik menjelajahi pedalaman pulau-pulau terpencil untuk merekam audio visual pelantunan tradisi lisan, mentranskripsikannya ke dalam format ortografi fonetik, serta menyusun kamus digital dwibahasa. Melalui kurikulum muatan lokal dan pemanfaatan media sosial oleh pemuda adat, asa untuk melestarikan memori kolektif bangsa tetap dinyalakan.",
             "この実存的危機を自覚し、言語復興運動とデジタルドキュメンテーションが政府、研究機関、先住コミュニティによって大規模に推進され始めている。言語学者たちは遠隔の島々の奥地を探訪して口承伝統の歌唱を高解像度で視聴覚記録し、それを表音文字の表記形式へ書き起こし、二言語デジタル辞書を編纂している。学校教育における地域独自カリキュラム（ムオタン・ロカル）の統合と先住青年によるSNS活用を通じ、国民の集合的記憶を継承する希望の火は灯され続けている。",
             "動名詞節「Menyadari urgensi eksistensial ini, ...」、並列動詞「merekam..., mentranskripsikannya..., serta menyusun...」、比喩的結語「asa untuk melestarikan... tetap dinyalakan（希望の火は灯され続けている）」。")
        ],
        "grammar": [
            ("成句 dapat dihitung dengan jari（指折り数えるほど少ない）", "文字通り「指で数えられる」という意味で、数量が極めて希少であることを強調する慣用句。伝統工芸の継承者や絶滅危惧言語の話者を語る際の頻出表現です。"),
            ("動詞句 tanpa sempat（〜する暇・猶予もなく）", "sempat（機会がある、都合がつく）に否定の tanpa が付いた表現。「tanpa sempat mewariskan（引き継ぐ間もなく）」のように、突発的な事態によって重要な行為が果たされなかった無念さを表します。"),
            ("名詞 asa（希望、光）の文語表現", "日常語の harapan と同義ですが、詩的・文学的な格調を持つ単語。「asa tetap dinyalakan（希望の火は灯され続ける）」のように、困難に屈しない不屈の精神を表す比喩句として用いられます。")
        ],
        "quiz": [
            {
                "q": "Berapa jumlah bahasa daerah yang teridentifikasi di Indonesia menurut teks?",
                "options": ["120 bahasa", "350 bahasa", "718 bahasa", "1.500 bahasa"],
                "ans": "718 bahasa",
                "exp": "第1段落冒頭に「Dengan 718 bahasa daerah yang teridentifikasi secara ilmiah」と明記されています。"
            },
            {
                "q": "Di wilayah manakah konsentrasi bahasa daerah paling tinggi di Indonesia?",
                "options": ["Pulau Jawa dan Bali", "Pulau Sumatra dan Bangka", "Kepulauan Maluku dan Pulau Papua", "Kalimantan Tengah dan Barat"],
                "ans": "Kepulauan Maluku dan Pulau Papua",
                "exp": "第1段落に「Sebagian besar dari khazanah bahasa ini terkonsentrasi di wilayah timur Nusantara, khususnya di Kepulauan Maluku dan Pulau Papua」とあります。"
            },
            {
                "q": "Apa nama epos kesastraan lisan agung yang berasal dari Sulawesi Selatan?",
                "options": ["Didong", "La Galigo", "Mahabharata", "Panji Semirang"],
                "ans": "La Galigo",
                "exp": "第2段落に「tradisi pelantunan epos 'La Galigo' di Sulawesi Selatan」と記載されています。"
            }
        ],
        "column": """### 深層コラム：世界最長の叙事詩『ラ・ガリゴ（I La Galigo）』と聖なる語り部「ビッス」

ブギス族に伝わる神話叙事詩『I La Galigo』は、全編約30万行に及び、ホメロスの『イリアス』や古代インドの『マハーバーラタ』を遥かに凌ぐ「世界最長の文学叙事詩」としてユネスコの世界の記憶（Memory of the World）に登録されています。

この壮大な物語は、かつて両性具有の聖職者「Bissu（ビッス）」や語り部たちによって、独特の節回しで何日もかけて朗唱されていました。しかし第二次世界大戦後のイスラム厳格派反乱（DI/TII）による迫害や近代化の中で伝承者が激減しました。現在、オランダのライデン大学図書館に保管された手記の解読とともに、現地の若者たちによるデジタル朗唱アーカイブ化プロジェクトが急ピッチで進められています。"""
    },
    {
        "filename": "45-water-security-sanitation.md",
        "title": "45. 安全な飲料水へのアクセス向上：都市水道普及率向上と雨水再利用技術",
        "category": "長文読解・環境インフラ・公衆衛生",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "豊かな降水量に恵まれた熱帯の国でありながら、インドネシアの大都市や離島部では安全な上水道（Air Bersih）へのアクセスが長年の重大課題です。過剰な地下水汲み上げによるジャカルタの地盤沈下危機を背景に、公設上水道（PAM）の配管網拡張、民間BOT方式の浄水場建設、そして雨水貯留・再利用技術の普及が進んでいます。",
        "passage": """Secara geografis dan klimatologis, Indonesia dianugerahi curah hujan tropis yang sangat melimpah, menjadikannya salah satu negara dengan cadangan air tawar terbarukan terbesar di Asia Tenggara. Kendati demikian, kelimpahan anugerah alam ini berbanding terbalik dengan ketersediaan akses terhadap air minum yang aman dan layak bagi masyarakat. Di berbagai kawasan metropolitan dan perkotaan padat penduduk, cakupan jaringan pipa air bersih perpipaan (Perusahaan Air Minum/PAM) rata-rata masih berada di bawah angka 40 persen, memaksa sebagian besar warga bergantung pada air tanah dan air minum kemasan isi ulang galon.

Dampak paling katastropik dari defisit infrastruktur air perpipaan ini tampak nyata di ibu kota Jakarta. Ketiadaan akses air pipa selama puluhan tahun mendorong maraknya penyedotan air tanah secara ilegal dan tak terkendali melalui sumur-sumur bor dalam oleh permukiman, gedung pencakar langit, dan kompleks industri. Akibatnya, permukaan tanah di Jakarta Utara ambles (land subsidence) hingga belasan sentimeter per tahun, mempercepat ancaman tenggelamnya kota di bawah permukaan laut pasang. Menghentikan penyedotan air tanah secara total hanya mungkin dilakukan apabila pemerintah mampu menyediakan 100 persen cakupan air perpipaan.

Guna mengatasi darurat ketahanan air ini, pemerintah pusat meluncurkan Proyek Strategis Nasional (PSN) berupa pembangunan sejumlah Sistem Penyediaan Air Minum (SPAM) regional berkapasitas raksasa, seperti SPAM Karian-Serpong, SPAM Jatiluhur I, dan SPAM Umbulan di Jawa Timur. Proyek-proyek ini mengolah air baku dari waduk-waduk raksasa menggunakan teknologi sedimentasi dan filtrasi ozon modern sebelum didistribusikan melalui pipa transmisi bertekanan tinggi melintasi batas-batas administratif antardaerah.

Di tingkat komunitas dan rumah tangga, paradigma baru pengelolaan air mandiri mulai tumbuh subur melalui gerakan 'Pemanenan Air Hujan' (Rainwater Harvesting). Alih-alih membiarkan air hujan terbuang sia-sia menjadi limpasan permukaan yang memicu banjir genangan, warga diedukasi untuk memasang instalasi talang penyaring, tandon penampung higienis, serta sumur resapan biopori. Melalui perpaduan mega-proyek infrastruktur perpipaan dan aksi konservasi air desentralistis di tingkat akar rumput, Indonesia menatap masa depan ketahanan air yang berkeadilan dan berkelanjutan.""",
        "vocab": [
            ("cadangan air tawar", "名詞句", "淡水資源埋蔵量", "Cadangan air tawar melimpah harus dikelola secara bijaksana."),
            ("berbanding terbalik", "成句動詞", "正反対である、反比例する", "Kelimpahan sumber daya berbanding terbalik dengan kualitas akses."),
            ("air minum perpipaan", "名詞句", "上水道飲料水 (Piped Water)", "Pemerintah menargetkan 100 persen akses air minum perpipaan."),
            ("penyedotan air tanah", "名詞句", "地下水汲み上げ・揚水", "Penyedotan air tanah berlebihan memicu penurunan muka tanah."),
            ("ambles", "動詞・形容詞 (ジャワ語借用)", "（地面が）沈下する、陥没する", "Tanah di pesisir utara ambles hingga 10 sentimeter per tahun."),
            ("ketahanan air", "名詞句", "水安全保障 (Water Security)", "Ketahanan air merupakan prasyarat mutlak kedaulatan pangan."),
            ("air baku", "名詞句", "浄水原水 (Raw Water)", "Waduk Jatiluhur menyuplai air baku bagi pabrik pengolahan."),
            ("limpasan permukaan", "名詞句", "地表流出水 (Surface Runoff)", "Betonisasi kota meningkatkan volume limpasan permukaan yang memicu banjir."),
            ("pemanenan air hujan", "名詞句", "雨水貯留・利用 (Rainwater Harvesting)", "Teknik pemanenan air hujan menjadi solusi hemat di musim hujan."),
            ("sumur resapan biopori", "名詞句", "バイオポア浸透井戸", "Pembuatan sumur resapan biopori membantu mengisi kembali air tanah.")
        ],
        "paragraphs": [
            ("Secara geografis, Indonesia dianugerahi curah hujan tropis yang sangat melimpah, menjadikannya salah satu negara dengan cadangan air tawar terbesar di Asia Tenggara. Kendati demikian, kelimpahan anugerah alam ini berbanding terbalik dengan ketersediaan akses terhadap air minum yang aman. Di kawasan perkotaan padat penduduk, cakupan jaringan pipa air bersih (PAM) rata-rata masih berada di bawah angka 40 persen, memaksa sebagian besar warga bergantung pada air tanah dan air kemasan galon.",
             "地理的に、インドネシアは極めて豊富な熱帯降水量に恵まれており、東南アジアで最大の再生可能淡水埋蔵量を誇る国家の一つとなっている。それにもかかわらず、この自然の豊かな恵みは、市民にとっての安全で適切な飲料水へのアクセス可能性とは正反対の状況にある。人口密度の高い都市地域において、公設上水道（PAM）の配管網普及率は平均して依然として40%未満にとどまり、大多数の住民が地下水やガロンボトルの詰め替え飲料水に依存せざるを得ない状況を生んでいる。",
             "受動態述語「dianugerahi curah hujan...（降水量に恵まれている）」、分詞節「menjadikannya salah satu negara...（それを〜な国家の一つにしている）」、成句「berbanding terbalik dengan...（〜と正反対・反比例である）」。"),
            ("Dampak paling katastropik dari defisit infrastruktur air perpipaan ini tampak nyata di ibu kota Jakarta. Ketiadaan akses air pipa mendorong maraknya penyedotan air tanah secara ilegal melalui sumur bor dalam oleh permukiman dan gedung perkantoran. Akibatnya, permukaan tanah di Jakarta Utara ambles hingga belasan sentimeter per tahun, mempercepat ancaman tenggelamnya kota di bawah permukaan laut. Menghentikan penyedotan air tanah secara total hanya mungkin dilakukan apabila pemerintah mampu menyediakan 100 persen cakupan air perpipaan.",
             "配管水道インフラの不足がもたらす最も壊滅的な影響は、首都ジャカルタにおいて明白に現れている。水道アクセスの欠如は、住宅地やオフィスビルによる深井戸を通じた不法かつ野放図な地下水汲み上げの横行を促した。その結果、北ジャカルタの地表面は年間十数センチメートルも沈下し、高潮の海面下に都市が沈没する脅威を加速させている。地下水の汲み上げを完全に停止させることは、政府が100%の上水道普及率を提供できた場合にのみ可能となる。",
             "最上級形容詞句「Dampak paling katastropik dari...」、原因結果の接続「Akibatnya, permukaan tanah ambles...」、限定条件構文「hanya mungkin dilakukan apabila...（〜の場合にのみ実行可能である）」。"),
            ("Guna mengatasi darurat ketahanan air ini, pemerintah pusat meluncurkan Proyek Strategis Nasional (PSN) berupa pembangunan sejumlah Sistem Penyediaan Air Minum (SPAM) regional berkapasitas raksasa, seperti SPAM Karian-Serpong dan SPAM Jatiluhur I. Proyek-proyek ini mengolah air baku dari waduk-waduk raksasa menggunakan teknologi filtrasi modern sebelum didistribusikan melalui pipa transmisi bertekanan tinggi melintasi batas-batas administratif antardaerah.",
             "この水安全保障の緊急事態を克服するため、中央政府はカリアン・セルポンSPAMやジャティルフール第1SPAMのような、巨大容量の広域上水道供給システム（SPAM）の建設という国家戦略プロジェクト（PSN）を展開している。これらのプロジェクトは、高圧送水管を通じて地域間の行政境界を越えて配水される前に、最新のオゾン濾過・沈殿技術を用いて巨大ダム湖からの原水を浄水処理している。",
             "目的前置詞「Guna mengatasi darurat ketahanan air ini, ...」、同格表現「berupa pembangunan sejumlah...」、時間接続詞「sebelum didistribusikan melalui pipa...（パイプを通じて配水される前に）」。"),
            ("Di tingkat komunitas dan rumah tangga, paradigma baru pengelolaan air mandiri mulai tumbuh subur melalui gerakan 'Pemanenan Air Hujan'. Alih-alih membiarkan air hujan terbuang sia-sia menjadi limpasan permukaan yang memicu banjir genangan, warga diedukasi untuk memasang instalasi talang penyaring, tandon penampung higienis, serta sumur resapan biopori. Melalui perpaduan mega-proyek perpipaan dan konservasi air desentralistis di tingkat akar rumput, Indonesia menatap masa depan ketahanan air yang berkelanjutan.",
             "コミュニティや世帯レベルでは、「雨水収穫（レインウォーター・ハーベスティング）」運動を通じた自主的な水管理の新たなパラダイムが豊かに育ち始めている。雨水を無駄に浸水冠水を促す地表流出水として流してしまう代わりに、住民はフィルター付き雨樋、衛生的な貯水タンク、そしてバイオポア浸透井戸を設置するよう啓発されている。大規模な配管インフラプロジェクトと草の根レベルの分散型水保全の融合を通じて、インドネシアは持続可能な水安全保障の未来を見据えている。",
             "比喩動詞句「mulai tumbuh subur（豊かに育ち始めている）」、代替前置詞句「Alih-alih membiarkan air hujan terbuang sia-sia...（雨水を無駄に捨てる代わりに）」、結語「menatap masa depan yang berkelanjutan（持続可能な未来を見据える）」。")
        ],
        "grammar": [
            ("成句 berbanding terbalik dengan（〜と反比例する、真逆である）", "数学用語の「反比例（inversely proportional）」から転じた論説表現。恵まれた条件と実際の不十分な実態の不条理なギャップを強調する際に使われます。"),
            ("動詞 ambles（地面が沈む、地盤沈下する）の語源", "ジャワ語 ambles（すっぽり沈む）からインドネシア語（KBBI）の標準語彙に取り入れられた動詞。学術用語 penurunan muka tanah（地盤沈下）の口語・報道表現として完全に定着しています。"),
            ("環境工学複合語 sumur resapan biopori（バイオポア浸透井戸）", "ボゴール農科大学（IPB）のカミル・スブランディ教授が考案した土壌浸透穴。直径10cm深さ1mの穴を有機物で満たし、ミミズなどの生物（bio）の活動で微細な穴（pori）を作らせて雨水の地下浸透を劇的に促すインドネシア発祥のエコ技術です。")
        ],
        "quiz": [
            {
                "q": "Berapa rata-rata cakupan jaringan air perpipaan (PAM) di perkotaan Indonesia menurut teks?",
                "options": ["Di atas 90 persen", "Sekitar 75 persen", "Di bawah 40 persen", "Nol persen sama sekali"],
                "ans": "Di bawah 40 persen",
                "exp": "第1段落に「cakupan jaringan pipa air bersih perpipaan (PAM) rata-rata masih berada di bawah angka 40 persen」と記載されています。"
            },
            {
                "q": "Apa dampak katastropik utama dari penyedotan air tanah ilegal di Jakarta Utara?",
                "options": ["Terjadinya gempa bumi vulkanik", "Penurunan permukaan tanah (ambles) belasan sentimeter per tahun", "Air laut berubah menjadi air tawar", "Kekeringan total tanpa ada hujan"],
                "ans": "Penurunan permukaan tanah (ambles) belasan sentimeter per tahun",
                "exp": "第2段落に「permukaan tanah di Jakarta Utara ambles hingga belasan sentimeter per tahun, mempercepat ancaman tenggelamnya kota」とあります。"
            },
            {
                "q": "Teknik konservasi air mandiri apa yang diajarkan kepada warga di tingkat rumah tangga?",
                "options": ["Pengeboran air tanah sedalam 500 meter", "Pemanenan air hujan (Rainwater Harvesting) dan sumur biopori", "Pengeringan seluruh danau alami", "Pembangunan pabrik plastik kemasan"],
                "ans": "Pemanenan air hujan (Rainwater Harvesting) dan sumur biopori",
                "exp": "最終段落に「gerakan 'Pemanenan Air Hujan'... memasang instalasi talang penyaring, tandon penampung higienis, serta sumur resapan biopori」と明記されています。"
            }
        ],
        "column": """### 深層コラム：インドネシア庶民の生命線「ガロン水（Air Galon）」ビジネスの光と影

インドネシアの都市生活で最も身近な家庭用品が、青い19リットルの大型ポリカーボネート容器「Air Galon」です。Aqua（ダノン）をはじめとする大手ブランドや、近所の「Depot Air Minum Isi Ulang（詰め替えスタンド）」のガロン水が、水道を飲めない全世帯の飲用水需要を一手に引き受けています。

しかし、週に数個の重いガロン水を買い運ぶ家計負担に加え、使い捨てペットボトル以上のプラスチック容器循環コストや、微細なマイクロプラスチック混入、BPA（ビスフェノールA）の健康リスクをめぐる論争も激化しています。政府が公設上水道（PAM）の蛇口直結飲料化（Tap Water）を急ぐ背景には、市民をこの「ガロン水依存のコスト」から解放するという公衆衛生上の大義があるのです。"""
    },
    {
        "filename": "46-creative-economy-lokananta.md",
        "title": "46. 国営音楽スタジオ「ロカナタ」の劇的復活：歴史的音源アーカイブと文化観光複合施設",
        "category": "長文読解・音楽遺産・クリエイティブ経済",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "1956年、スカルノ大統領の命により中部ジャワ・ソロ（スラカルタ）に設立されたインドネシア初の国営音楽録音会社「Lokananta（ロカナタ）」。デジタル時代の波に乗り遅れて荒廃していたこの音楽の聖地が、国営企業省主導の大規模リノベーションにより、歴史的音源アーカイブ、最新スタジオ、ライブハウスを備えた文化観光複合施設として劇的な復活を遂げました。",
        "passage": """Di belantika sejarah musik Indonesia, nama 'Lokananta' memiliki kedudukan yang sangat sakral layaknya Studio Abbey Road di Inggris. Didirikan pada 29 Oktober 1956 di Kota Surakarta (Solo) atas inisiatif Direktur Jenderal Radio Republik Indonesia (RRI) Maladi dan didukung penuh oleh Presiden pertama Sukarno, Lokananta memegang mandat kebudayaan yang monumental: memproduksi piringan hitam (vinyl) untuk menyiarkan rekaman gending gamelan, musik keroncong, serta pidato-pidato kenegaraan ke stasiun-stasiun radio di seluruh pelosok tanah air. Di studio inilah, master rekaman proklamasi kemerdekaan yang dibacakan Bung Karno serta lagu kebangsaan 'Indonesia Raya' versi tiga stanza pertama kali digandakan.

Namun, memasuki era disrupsi digital dan kaset pita bajakan pada akhir abad ke-20, kejayaan Lokananta meredup drastis. Pabrik piringan hitam berhenti beroperasi, ribuan master tape bersejarah terbengkalai dalam ruangan berdebu tanpa pendingin udara yang memadai, dan kompleks seluas tiga hektare tersebut nyaris menjadi museum usang yang mati suri. Kondisi memprihatinkan ini memicu jeritan keprihatinan dari kalangan musisi, sejarawan, dan pecinta musik Nusantara yang menyaksikan warisan ingatan auditif bangsa berada di ambang kemusnahan fisik.

Titik balik penyelamatan aset bersejarah ini terwujud pada tahun 2022, ketika Kementerian Badan Usaha Milik Negara (BUMN) melalui PT Danareksa dan PT Perusahaan Pengelola Aset (PPA) meluncurkan proyek revitalisasi total. Tanpa mengubah keaslian fasad arsitektur art deco peninggalan era Sukarno, Lokananta disulap menjadi 'Lokananta Reloaded': sebuah ekosistem kreatif multifungsi yang memadukan museum musik modern interaktif, galeri seni, studio rekaman berteknologi analog-digital termutakhir, amfiteater terbuka untuk konser musik, serta area kuliner UMKM lokal.

Aspek paling bernilai dari revitalisasi ini adalah penyelamatan lebih dari 50.000 keping piringan hitam dan 5.600 master pita magnetik melalui proses restorasi fisik dan digitalisasi audio beresolusi tinggi. Lokananta baru kini menjadi magnet wisata edukasi budaya yang memikat ribuan anak muda setiap bulannya. Keberhasilan ini menjadi cetak biru (blueprint) inspiratif bagi revitalisasi aset-aset cagar budaya negara lainnya, membuktikan bahwa sejarah kebangsaan dapat dihidupkan kembali sebagai motor penggerak ekonomi kreatif kontemporer.""",
        "vocab": [
            ("belantika musik", "名詞句", "音楽業界、音楽界の舞台", "Lokananta mencatatkan sejarah emas di belantika musik nasional."),
            ("piringan hitam", "名詞句", "アナログレコード盤 (vinyl record)", "Koleksi piringan hitam kuno dirawat dalam arsip berpendingin."),
            ("gending gamelan", "名詞句", "ガムラン合奏曲", "Gending gamelan Jawa pertama kali direkam di studio ini."),
            ("mati suri", "成句形容詞", "仮死状態の、休眠して活動停止した", "Perusahaan rekaman tersebut sempat mati suri selama puluhan tahun."),
            ("ingatan auditif bangsa", "名詞句", "国民の聴覚的記憶・音の遺産", "Pita rekaman menyimpan ingatan auditif bangsa yang tak ternilai."),
            ("di ambang kemusnahan", "成句前置詞句", "絶滅・消滅の危機に瀕して", "Warisan sejarah berada di ambang kemusnahan akibat penelantaran."),
            ("fasad arsitektur art deco", "名詞句", "アール・デコ様式の建築正面外観", "Fasad arsitektur art deco gedung dipertahankan keasliannya."),
            ("disulap menjadi", "動詞句 (受動)", "魔法のように〜へと生まれ変わる", "Gudang tua disulap menjadi ruang konser megah."),
            ("pita magnetik", "名詞句", "磁気テープ (Magnetic Tape)", "Ribuan rol pita magnetik menjalani proses restorasi digital."),
            ("cetak biru inspiratif", "名詞句", "示唆に富む青写真 (Inspiring Blueprint)", "Proyek ini menjadi cetak biru inspiratif bagi revitalisasi cagar budaya.")
        ],
        "paragraphs": [
            ("Di belantika sejarah musik Indonesia, nama 'Lokananta' memiliki kedudukan yang sangat sakral layaknya Studio Abbey Road di Inggris. Didirikan pada tahun 1956 di Surakarta atas inisiatif Maladi dan didukung penuh oleh Presiden Sukarno, Lokananta memegang mandat kebudayaan yang monumental: memproduksi piringan hitam untuk menyiarkan rekaman gending gamelan dan pidato kenegaraan ke stasiun-stasiun radio di seluruh pelosok. Di studio inilah, master rekaman proklamasi kemerdekaan serta lagu kebangsaan 'Indonesia Raya' versi tiga stanza pertama kali digandakan.",
             "インドネシア音楽史の舞台において、『Lokananta（ロカナタ）』の名は英国のアビー・ロード・スタジオのように極めて神聖な地位を占めている。1956年、国営ラジオ（RRI）総裁マラディの主導とスカルノ初代大統領の全面支援によってスラカルタ（ソロ）に設立されたロカナタは、ガムラン合奏曲の録音や国家元首の演説を全国津々浦々のラジオ局へ届けるためのアナログレコードを制作するという記念碑的な文化マンデートを担った。このスタジオでこそ、ブン・カルノによって朗読された独立宣言のマスター音源や、国歌『インドネシア・ラヤ』の3スタンザ完全版が初めて複製されたのである。",
             "比況副詞「layaknya Studio Abbey Road...」、受動過去分詞節「Didirikan pada... didukung penuh oleh...」、強調倒置構文「Di studio inilah, ... pertama kali digandakan（まさにこのスタジオで初めて複製された）」。"),
            ("Namun, memasuki era disrupsi digital dan kaset bajakan pada akhir abad ke-20, kejayaan Lokananta meredup drastis. Pabrik piringan hitam berhenti beroperasi, ribuan master tape bersejarah terbengkalai dalam ruangan berdebu tanpa pendingin udara, dan kompleks seluas tiga hektare tersebut nyaris menjadi museum usang yang mati suri. Kondisi memprihatinkan ini memicu keprihatinan dari kalangan musisi yang menyaksikan warisan ingatan auditif bangsa berada di ambang kemusnahan.",
             "しかし、20世紀末の海賊版カセットテープやデジタルディスラプションの時代に入ると、ロカナタの栄光は急速に色褪せた。レコード工場は操業を停止し、何千本もの歴史的マスターテープは適切な空調もない埃まみれの部屋に放置され、広さ3ヘクタールの複合施設は仮死状態の古びた博物館へと成り果てようとしていた。この痛ましい状況は、国民の聴覚的記憶の遺産が物理的消滅の危機に瀕するのを目撃した音楽家たちの切実な懸念を呼び起こした。",
             "時制分詞節「memasuki era disrupsi digital...」、動詞「meredup drastis（劇的に衰退する）」、成句「mati suri（仮死状態）」、「berada di ambang kemusnahan（消滅の瀬戸際にある）」。"),
            ("Titik balik penyelamatan aset bersejarah ini terwujud pada tahun 2022, ketika Kementerian BUMN meluncurkan proyek revitalisasi total. Tanpa mengubah keaslian fasad arsitektur art deco peninggalan era Sukarno, Lokananta disulap menjadi 'Lokananta Reloaded': sebuah ekosistem kreatif multifungsi yang memadukan museum musik modern interaktif, galeri seni, studio rekaman analog-digital termutakhir, amfiteater konser terbuka, serta area kuliner UMKM lokal.",
             "この歴史的資産の救済の転換点は、国営企業（BUMN）省が全面的な再生プロジェクトを開始した2022年に結実した。スカルノ時代の遺産であるアール・デコ建築ファサードの真正性を損なうことなく、ロカナタは『ロカナタ・リローデッド』へと華麗に変貌を遂げた。インタラクティブな現代音楽博物館、アートギャラリー、最先端のアナログ・デジタル録音スタジオ、野外コンサート円形劇場、そして地元の零細・飲食（UMKM）エリアを融合させた多機能クリエイティブエコシステムである。",
             "関係副詞「ketika Kementerian BUMN meluncurkan...」、前置詞句「Tanpa mengubah keaslian fasad...」、比喩動詞「disulap menjadi（〜へと魔法のように変貌させられた）」。"),
            ("Aspek paling bernilai dari revitalisasi ini adalah penyelamatan lebih dari 50.000 keping piringan hitam dan 5.600 master pita magnetik melalui proses restorasi fisik dan digitalisasi audio beresolusi tinggi. Lokananta baru kini menjadi magnet wisata edukasi budaya yang memikat ribuan anak muda setiap bulannya. Keberhasilan ini menjadi cetak biru inspiratif bagi revitalisasi aset cagar budaya negara lainnya, membuktikan bahwa sejarah kebangsaan dapat dihidupkan kembali sebagai motor penggerak ekonomi kreatif kontemporer.",
             "この再活性化の最も価値ある側面は、物理的修復とハイレゾ音声デジタル化プロセスを通じた、5万枚以上のレコード盤と5,600本のマスター磁気テープの救出である。新生ロカナタは現在、毎月何千人もの若者を魅了する文化教育観光のマグネット（求心力）となっている。この成功は、国の他の歴史文化遺産資産の再生にとっても示唆に富む青写真となっており、国家の歴史が現代クリエイティブ経済の牽引エンジンとして蘇り得ることを証明している。",
             "名詞句主語「Aspek paling bernilai dari revitalisasi ini adalah...」、比喩表現「menjadi magnet wisata（観光のマグネットとなる）」、「motor penggerak ekonomi kreatif（創造経済の推進原動力）」。")
        ],
        "grammar": [
            ("動詞 disulap menjadi（〜へ魔法のように姿を変える、一変する）", "語根 sulap（手品・奇術・マジック）に受動態接頭辞 di- が付いた表現。ボロボロの廃墟や古い倉庫が、見違えるほど現代的で華麗な施設へと劇的改修された際によく用いられるジャーナリズム用語です。"),
            ("成句 mati suri（仮死状態、休眠状態）", "suri は「仮死、死んだふり」を意味し、完全に消滅したわけではないが生命活動を停止している状態を表します。企業、事業、文化施設が長期休眠していた文脈を活写します。"),
            ("比喩成句 cetak biru（青写真、マスタープラン、設計図）", "オランダ語 blauwdruk / 英語 blueprint の直訳借用。今後の国家プロジェクトや都市開発の規範となる「成功モデル」を指す定番の論説語彙です。")
        ],
        "quiz": [
            {
                "q": "Di kota manakah studio rekaman bersejarah Lokananta berada?",
                "options": ["Jakarta", "Surabaya", "Surakarta (Solo)", "Bandung"],
                "ans": "Surakarta (Solo)",
                "exp": "第1段落に「Didirikan pada 29 Oktober 1956 di Kota Surakarta (Solo)」と明記されています。"
            },
            {
                "q": "Dokumen rekaman suara bersejarah apa yang pertama kali digandakan di Studio Lokananta?",
                "options": ["Pidato Ratu Belanda Wilhelmina", "Teks Proklamasi Bung Karno dan Indonesia Raya 3 stanza", "Deklarasi KTT Non-Blok pertama", "Siaran radio pertama BBC London"],
                "ans": "Teks Proklamasi Bung Karno dan Indonesia Raya 3 stanza",
                "exp": "第1段落末尾に「master rekaman proklamasi kemerdekaan yang dibacakan Bung Karno serta lagu kebangsaan 'Indonesia Raya' versi tiga stanza pertama kali digandakan」とあります。"
            },
            {
                "q": "Berapa banyak koleksi piringan hitam yang diselamatkan melalui proses restorasi dan digitalisasi di Lokananta?",
                "options": ["Sekitar 500 keping", "Lebih dari 50.000 keping", "1.000 keping", "Tepat 100 keping"],
                "ans": "Lebih dari 50.000 keping",
                "exp": "第4段落冒頭に「penyelamatan lebih dari 50.000 keping piringan hitam dan 5.600 master pita magnetik」と明記されています。"
            }
        ],
        "column": """### 深層コラム：ジャワ神話の「天上の音楽」から名付けられたロカナタ

「Lokananta」という雅な名前は、ジャワの古典影絵芝居（ワヤン）やヒンドゥー神話に登場する「スラリーロカ（天界・神々の世界）で奏でられる音色の美しいガムラン」を意味します。

スカルノ大統領は、欧米のポップスに国土が席巻されることを警戒し、「文化的主体性（Kepribadian di Bidang Kebudayaan / Trisakti）」を確立するために、各地の伝統ガムランやクロンチョンを最高峰の音質でレコードに刻み、国営ラジオを通じて全土に鳴り響かせることを国家の使命と位置づけました。新生ロカナタには、かつてウォルドルフ・アスター劇場でも使われたドイツ製真空管ミキサーや貴重なマイクロフォンが現在も大切に保存されています。"""
    },
    {
        "filename": "47-wildlife-trafficking-crackdown.md",
        "title": "47. 野生生物違法取引との戦い：センザンコウとオランウータンを密猟から救出する",
        "category": "長文読解・環境保護・生物多様性",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "地球上で最も豊かな生物多様性を誇る熱帯雨林を有するインドネシアは、残念ながら国際的な野生動物違法取引（Illegal Wildlife Trade）の供給地・中継地としても狙われてきました。絶滅危惧種センザンコウの鱗密輸やオランウータンの密猟に対し、環境林業省（KLHK）と警察による摘発、DNA追跡、そして森への野生復帰プロジェクトが進展しています。",
        "passage": """Sebagai salah satu negara megabiodiversitas terkemuka di dunia, Indonesia menjadi habitat bagi ratusan ribu spesies flora dan fauna endemik yang tidak dapat ditemukan di belahan bumi mana pun. Hutan hujan tropis Sumatra, Kalimantan, Sulawesi, hingga Papua menjadi benteng pertahanan terakhir bagi mamalia langka seperti orangutan, badak sumatra, harimau sumatra, dan trenggiling (pangolin). Namun, anugerah keanekaragaman hayati ini menghadapi ancaman eksistensial yang sangat destruktif dari kejahatan terorganisasi perdagangan satwa liar ilegal lintas negara bernilai triliunan rupiah.

Salah satu mamalia yang paling menderita akibat perburuan liar adalah trenggiling sunda (Manis javanica). Sisik trenggiling yang terbuat dari zat keratin diburu secara masif untuk diselundupkan ke pasar internasional, di mana sisik tersebut dihargai sangat mahal sebagai bahan baku obat tradisional dan bahan baku sintesis narkotika. Sindikat kejahatan transnasional menggunakan jalur tikus pelabuhan ilegal di pesisir Sumatra untuk menyelundupkan berton-ton sisik trenggiling beku. Sementara itu, bayi-bayi orangutan kerap ditangkap secara kejam di kawasan deforestasi perkebunan dengan membunuh induknya terlebih dahulu, untuk kemudian dijual di pasar gelap sebagai hewan peliharaan eksotis kaum elite.

Merespons darurat konservasi ini, Direktorat Jenderal Penegakan Hukum Kementerian Lingkungan Hidup dan Kehutanan (Gakkum KLHK) bersama Kepolisian Republik Indonesia memperketat operasi intelijen siber dan pengawasan perbatasan. Pendekatan investigasi ilmiah (forensik satwa liar) mulai diterapkan, di mana analisis DNA digunakan untuk mengidentifikasi asal geografis satwa yang disita sehingga mempermudah pemetaan jaringan mafia penyelundup. Selain hukuman penjara yang diperberat berdasarkan Undang-Undang Konservasi Sumber Daya Alam Hayati, penegak hukum juga mulai menerapkan pasal Tindak Pidana Pencucian Uang (TPPU) untuk memiskinkan para cukong pengendali sindikat.

Penyelamatan fisik satwa sitaan hanyalah langkah awal dari proses pemulihan yang panjang dan kompleks. Lembaga-lembaga konservasi nirlaba seperti Borneo Orangutan Survival Foundation (BOSF) mengoperasikan pusat rehabilitasi khusus untuk melatih kembali insting liar orangutan sitaan di 'Sekolah Hutan' selama bertahun-tahun sebelum mereka siap dilepasliarkan ke habitat alaminya. Keberhasilan pelestarian satwa langka ini pada akhirnya menuntut komitmen kolektif global untuk memutus rantai permintaan pasar dan memberdayakan komunitas tepi hutan sebagai garda terdepan pelindung ekosistem.""",
        "vocab": [
            ("megabiodiversitas", "名詞", "メガ生物多様性 (Megabiodiversity)", "Indonesia masuk dalam jajaran tiga besar negara megabiodiversitas dunia."),
            ("benteng pertahanan terakhir", "名詞句", "最後の防衛砦", "Taman nasional menjadi benteng pertahanan terakhir bagi harimau sumatra."),
            ("perdagangan satwa liar", "名詞句", "野生動物違法取引 (Wildlife Trafficking)", "Perdagangan satwa liar ilegal merupakan kejahatan transnasional serius."),
            ("jalur tikus pelabuhan", "名詞句", "密輸用の抜け道ルート・非公式港", "Penyelundup memanfaatkan jalur tikus untuk menghindari patroli bea cukai."),
            ("forensik satwa liar", "名詞句", "野生動物法医学 (Wildlife Forensics)", "Forensik satwa liar menggunakan uji DNA untuk melacak asal populasi."),
            ("memiskinkan para cukong", "動詞句", "黒幕ボス（チュコン）の全財産を剥奪する", "Penerapan pasal TPPU bertujuan memiskinkan para cukong kejahatan."),
            ("satwa sitaan", "名詞句", "差し押さえ・押収された動物", "Satwa sitaan dibawa ke pusat rehabilitasi untuk karantina medis."),
            ("sekolah hutan", "名詞句", "森の学校（オランウータン野生復帰訓練施設）", "Bayi orangutan diajari memanjat dan mencari makan di sekolah hutan."),
            ("dilepasliarkan", "他動詞 (受動)", "自然の野生へ再放流・復帰される", "Puluhan orangutan berhasil dilepasliarkan ke hutan lindung."),
            ("memutus rantai permintaan", "動詞句", "需要の連鎖を断ち切る", "Kampanye global diperlukan untuk memutus rantai permintaan cula dan sisik.")
        ],
        "paragraphs": [
            ("Sebagai salah satu negara megabiodiversitas di dunia, Indonesia menjadi habitat bagi ratusan ribu spesies flora dan fauna endemik. Hutan hujan tropis Sumatra, Kalimantan, hingga Papua menjadi benteng pertahanan terakhir bagi mamalia langka seperti orangutan, badak, harimau, dan trenggiling. Namun, anugerah ini menghadapi ancaman eksistensial dari kejahatan terorganisasi perdagangan satwa liar ilegal lintas negara bernilai triliunan rupiah.",
             "世界有数のメガ生物多様性国家として、インドネシアは何十万種もの固有動植物種の生息地となっている。スマトラ、カリマンタン、パプアに至る熱帯雨林は、オランウータン、スマトラサイ、スマトラトラ、センザンコウといった希少哺乳類の最後の砦である。しかし、この恵みは数兆ルピア規模に上る国際的な野生動物違法取引という組織犯罪からの実存的脅威に直面している。",
             "同格前置詞句「Sebagai salah satu negara...」、比喩表現「benteng pertahanan terakhir（最後の防衛砦）」、名詞句「kejahatan terorganisasi perdagangan satwa liar lintas negara（国境を越えた組織的野生動物取引犯罪）」。"),
            ("Salah satu mamalia yang paling menderita akibat perburuan liar adalah trenggiling sunda. Sisik trenggiling diburu secara masif untuk diselundupkan ke pasar internasional, di mana sisik tersebut dihargai sangat mahal sebagai bahan baku obat tradisional. Sindikat kejahatan menggunakan jalur tikus pelabuhan ilegal di pesisir Sumatra. Sementara itu, bayi-bayi orangutan kerap ditangkap secara kejam di kawasan deforestasi perkebunan dengan membunuh induknya terlebih dahulu, untuk kemudian dijual di pasar gelap sebagai hewan peliharaan eksotis.",
             "密猟によって最も苦しんでいる哺乳類の一つがスンダセンザンコウである。センザンコウの鱗は伝統薬の原料として極めて高値で取引される国際市場へ密輸するため、大規模に乱獲されている。犯罪シンジケートはスマトラ沿岸の非公式な密輸ルート（ネズミの抜け道）を利用している。一方、農園開発に伴う森林伐採現場では、まず母親を殺害した上でオランウータンの赤ん坊を残酷に捕獲し、エキゾチックペットとして闇市場で売り捌いている。",
             "受動構文連鎖「diburu secara masif untuk diselundupkan...」、関係副詞「di mana sisik tersebut dihargai...」、手段節「dengan membunuh induknya terlebih dahulu（まず母親を殺した上で）」。"),
            ("Merespons darurat konservasi ini, Gakkum KLHK bersama Kepolisian memperketat operasi intelijen siber dan pengawasan perbatasan. Pendekatan investigasi ilmiah mulai diterapkan, di mana analisis DNA digunakan untuk mengidentifikasi asal geografis satwa yang disita. Selain hukuman penjara yang diperberat, penegak hukum juga mulai menerapkan pasal Tindak Pidana Pencucian Uang (TPPU) untuk memiskinkan para cukong pengendali sindikat.",
             "この保全緊急事態に応じ、環境林業省法執行総局（Gakkum KLHK）は警察とともにサイバーインテリジェンス作戦と国境監視を強化している。押収された動物の地理的起源を特定するためにDNA分析が用いられるなど、科学的捜査（野生動物法医学）アプローチが導入され始めている。重罰化された禁錮刑に加え、法執行機関はシンジケートを裏で操る黒幕ボス（チュコン）の財産を剥奪するため、資金洗浄罪（マネーロンダリング／TPPU）条項の適用も開始した。",
             "分詞構文「Merespons darurat konservasi ini, ...」、司法表現「menerapkan pasal TPPU（マネロン条項を適用する）」、使役構文「untuk memiskinkan para cukong（黒幕の財産を剥奪して無一文にするため）」。"),
            ("Penyelamatan fisik satwa sitaan hanyalah langkah awal dari proses pemulihan yang panjang dan kompleks. Lembaga konservasi nirlaba seperti BOSF mengoperasikan pusat rehabilitasi khusus untuk melatih kembali insting liar orangutan sitaan di 'Sekolah Hutan' selama bertahun-tahun sebelum mereka siap dilepasliarkan ke habitat alaminya. Keberhasilan pelestarian satwa langka ini pada akhirnya menuntut komitmen kolektif global untuk memutus rantai permintaan pasar dan memberdayakan komunitas tepi hutan.",
             "押収動物の物理的救出は、長く複雑な回復プロセスの第一歩に過ぎない。BOSFのような民間保全団体は、押収されたオランウータンが本来の生息地へ再放流される準備が整うまで、何年にもわたって『森の学校』で野生の本能を再訓練するための専門リハビリセンターを運営している。希少動物の保全の成功は、最終的には市場の需要連鎖を断ち切り、森林周辺の地域社会をエコシステムの最前線の保護者としてエンパワーするというグローバルな協調的コミットメントを要求している。",
             "制限表現「hanyalah langkah awal dari...（〜の初歩の一歩に過ぎない）」、目的の時間接続詞「sebelum mereka siap dilepasliarkan（野生復帰の準備が整う前に）」、結語「menuntut komitmen kolektif global（グローバルな共同の責務を要求する）」。")
        ],
        "grammar": [
            ("俗語・経済用語 cukong（黒幕資本家、シンジケートの親玉）", "福建方言（主公）に由来する借用名詞。違法伐採、密輸、密猟などの現場実行犯の背後にいて、巨額の資金を動かし利益を吸い上げる黒幕・実力者を指します。"),
            ("動詞 memiskinkan（貧困化させる、全財産を没収する）", "語根 miskin（貧しい）に使役接頭辞 meN- と接尾辞 -kan が付いた派生動詞。刑法において犯罪収益をすべて没収して「無一文にする」というマネーロンダリング捜査の強力な方針を表します。"),
            ("成句 jalur tikus（ネズミの道、密輸用の非公式裏ルート）", "正規の税関や出入国審査が存在しない、海岸線や国境密林の細い抜け道を指す定型表現。密輸や不法越境の報道で不可欠な語彙です。")
        ],
        "quiz": [
            {
                "q": "Mengapa sisik trenggiling sunda sangat diburu di pasar gelap internasional?",
                "options": ["Sebagai bahan bakar pesawat terbang", "Sebagai bahan baku obat tradisional dan sintesis narkotika", "Untuk perhiasan emas murni", "Sebagai pengganti pakan ternak"],
                "ans": "Sebagai bahan baku obat tradisional dan sintesis narkotika",
                "exp": "第2段落に「dihargai sangat mahal sebagai bahan baku obat tradisional dan bahan baku sintesis narkotika」と記載されています。"
            },
            {
                "q": "Undang-Undang apa yang mulai diterapkan penegak hukum untuk memiskinkan cukong satwa liar?",
                "options": ["Undang-Undang Lalu Lintas", "Tindak Pidana Pencucian Uang (TPPU)", "Undang-Undang Hak Cipta", "Peraturan Pajak Pertambahan Nilai"],
                "ans": "Tindak Pidana Pencucian Uang (TPPU)",
                "exp": "第3段落末尾に「menerapkan pasal Tindak Pidana Pencucian Uang (TPPU) untuk memiskinkan para cukong」と明記されています。"
            },
            {
                "q": "Di manakah bayi orangutan sitaan diajari memanjat dan mencari makan sebelum dilepasliarkan?",
                "options": ["Sekolah Hutan", "Laboratorium universitas", "Kebun binatang perkotaan", "Kandang sirkus"],
                "ans": "Sekolah Hutan",
                "exp": "第4段落に「melatih kembali insting liar orangutan sitaan di 'Sekolah Hutan' selama bertahun-tahun」とあります。"
            }
        ],
        "column": """### 深層コラム：オランウータンを森へ還す「森の学校（Sekolah Hutan）」の感動の日々

親を密猟者に殺され、人間の家で鎖に繋がれて育った幼いオランウータンは、自力で木に登ることも、どの果実が食べられるかも知りません。

カリマンタンのニョアル・メンテン（Nyaru Menteng）にある「BOSF」のリハビリセンターでは、代用母（Babysitter）と呼ばれる人間のスタッフが、赤ちゃんオランウータンを抱いて森へ連れ出し、木登りや巣作り（Bikin Sarang）、毒のある植物の見分け方を毎朝手取り足取り教えます。8年から10年もの長い「就学」を経て、人間への依存を完全に断ち切り、無事にヘリコプターで手つかずの原生保護林へ放獣される瞬間は、インドネシアの保全関係者が最も涙する奇跡の光景です。"""
    },
    {
        "filename": "48-disability-rights-accessibility.md",
        "title": "48. 障害者権利条約とバリアフリー化：車椅子対応歩道と障害者雇用クォータ制の進展",
        "category": "長文読解・人権・共生社会",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "障害者権利条約の批准と2016年障害者法（UU Nomor 8 Tahun 2016）の制定以降、インドネシアでは障害者を「慈善・憐れみの対象」から「権利の主体」と捉えるパラダイムシフトが起きています。大都市における点字ブロックや車椅子スロープの整備、企業に対する法定雇用率（クォータ制）の義務付けなど、共生社会（Masyarakat Inklusif）への挑戦を追います。",
        "passage": """Selama berdekade-dekade, diskursus seputar penyandang disabilitas di Indonesia terkungkung dalam paradigma karitatif (charity-based approach) yang memandang kaum difabel semata-mata sebagai objek belas kasihan dan penerima santunan sosial pasif. Namun, ratifikasi Konvensi PBB tentang Hak-Hak Penyandang Disabilitas (CRPD) serta disahkannya Undang-Undang Nomor 8 Tahun 2016 tentang Penyandang Disabilitas menandai revolusi paradigma fundamental menuju pendekatan berbasis hak asasi manusia (human rights-based approach). Negara kini secara tegas mengakui penyandang disabilitas sebagai warga negara setara yang berhak atas kemandirian, partisipasi penuh, dan aksesibilitas tanpa diskriminasi.

Manifestasi fisik dari komitmen ini tampak pada revitalisasi ruang publik di kota-kota besar. Di Jakarta, Solo, dan Surabaya, proyek pelebaran trotoar ramah pedestrian mulai dilengkapi dengan ubin pemandu bertekstur (guiding blocks) bagi tunanetra, jalur landai (ramp) dengan kemiringan standar bagi pengguna kursi roda, serta elevator khusus di jembatan penyeberangan orang (JPO) terintegrasi halte TransJakarta dan stasiun MRT. Transportasi publik modern dirancang dengan lantai rendah (low deck) dan area kursi roda yang aman demi menjamin mobilitas mandiri bagi semua warga tanpa terkecuali.

Di ranah ketenagakerjaan, UU No. 8/2016 menetapkan kebijakan kuota ketenagakerjaan yang bersifat mengikat: instansi pemerintah, BUMN, dan BUMD wajib mempekerjakan paling sedikit 2 persen penyandang disabilitas dari jumlah pegawai, sedangkan perusahaan swasta diwajibkan memenuhi kuota minimal 1 persen. Untuk mendorong kepatuhan korporasi, pemerintah bersama berbagai organisasi advokasi disabilitas mendirikan Unit Layanan Disabilitas (ULD) Ketenagakerjaan guna memfasilitasi pelatihan vokasional, pemetaan kecocokan kerja, serta penyediaan fasilitas akomodasi yang layak di tempat kerja.

Kendati kemajuan regulasi dan infrastruktur fisik patut diapresiasi, tantangan terbesar masih berakar pada stigma kultural dan rendahnya penegakan sanksi hukum. Di banyak daerah luar perkotaan, fasilitas pendidikan inklusif masih sangat terbatas dan trotoar berubin pemandu kerap kali diokupasi oleh pedagang kaki lima atau dijadikan tempat parkir liar sepeda motor. Mewujudkan Indonesia yang benar-benar inklusif menuntut penghapusan hambatan arsitektural sekaligus dekonstruksi prasangka sosial yang membatasi potensi kaum difabel.""",
        "vocab": [
            ("paradigma karitatif", "名詞句", "慈善・憐れみパラダイム (Charity Approach)", "Kita harus beralih dari paradigma karitatif menuju pemenuhan hak asasi."),
            ("penyandang disabilitas", "名詞句 (公式呼称)", "障害者（disabilitas / difabel）", "Hak-hak penyandang disabilitas dijamin setara dalam undang-undang."),
            ("ubin pemandu bertekstur", "名詞句", "視覚障害者誘導用点字ブロック (Guiding Blocks)", "Ubin pemandu kuning dipasang di sepanjang trotoar utama."),
            ("jalur landai ramah kursi roda", "名詞句", "車椅子用スロープ通路 (Ramp)", "Gedung perkantoran wajib menyediakan jalur landai ramah kursi roda."),
            ("akomodasi yang layak", "名詞句 (人権法用語)", "合理的配慮 (Reasonable Accommodation)", "Perusahaan wajib memberikan akomodasi yang layak bagi staf difabel."),
            ("kuota ketenagakerjaan wajib", "名詞句", "法定雇用クォータ制", "BUMN wajib memenuhi kuota ketenagakerjaan difabel minimal 2 persen."),
            ("unit layanan disabilitas", "名詞句 (行政組織)", "障害者就労支援ユニット (ULD)", "ULD memfasilitasi pelatihan keterampilan vokasional inklusif."),
            ("diokupasi secara liar", "動詞句 (受動)", "不法に占拠・不法占有される", "Fasilitas pejalan kaki kerap diokupasi secara liar oleh pedagang."),
            ("dekonstruksi prasangka sosial", "名詞句", "社会的偏見の解体・脱構築", "Diperlukan edukasi publik untuk dekonstruksi prasangka sosial."),
            ("masyarakat inklusif", "名詞句", "共生社会、インクルーシブ社会", "Pembangunan berkelanjutan mensyaratkan terciptanya masyarakat inklusif.")
        ],
        "paragraphs": [
            ("Selama berdekade-dekade, diskursus seputar penyandang disabilitas di Indonesia terkungkung dalam paradigma karitatif yang memandang kaum difabel semata-mata sebagai objek belas kasihan. Namun, disahkannya UU No. 8 Tahun 2016 menandai revolusi paradigma fundamental menuju pendekatan berbasis hak asasi manusia. Negara kini secara tegas mengakui penyandang disabilitas sebagai warga negara setara yang berhak atas kemandirian, partisipasi penuh, dan aksesibilitas tanpa diskriminasi.",
             "何十年もの間、インドネシアにおける障害者をめぐる言説は、障害者を単に憐れみと同情の対象、受動的な社会扶助の受給者と見なす慈善パラダイムに閉じ込められていた。しかし2016年法律第8号の制定は、人権アプローチへの根本的なパラダイム革命を記した。国家はいまや、障害者を自立、完全な社会参加、そして無差別のアクセシビリティを享受する権利を持つ対等な国民として明確に認めている。",
             "受動態動詞「terkungkung dalam...（〜に閉じ込められている）」、前置詞句「menandai revolusi... menuju...（〜への革命を画する）」、権利を表す成句「berhak atas kemandirian（自立に対する権利を有する）」。"),
            ("Manifestasi fisik dari komitmen ini tampak pada revitalisasi ruang publik di kota-kota besar. Di Jakarta, Solo, dan Surabaya, pelebaran trotoar mulai dilengkapi dengan ubin pemandu bagi tunanetra, jalur landai ramah kursi roda, serta elevator khusus di jembatan penyeberangan terintegrasi. Transportasi publik modern dirancang dengan lantai rendah dan area kursi roda yang aman demi menjamin mobilitas mandiri bagi semua warga tanpa terkecuali.",
             "このコミットメントの物理的具現化は、大都市における公共空間の再整備に顕著に現れている。ジャカルタ、ソロ、スラバヤにおいて、歩道の拡幅工事は視覚障害者用点字ブロック、車椅子スロープ、バス停や駅直結歩道橋のエレベーターの完備を伴い始めている。最新の公共交通機関は、例外なくすべての市民の自立した移動を保障するため、低床（ノンステップ）設計と安全な車椅子スペースを備えて設計されている。",
             "名詞句主語「Manifestasi fisik dari komitmen ini...」、並列構文「mulai dilengkapi dengan ubin pemandu..., jalur landai..., serta elevator khusus...」、成句副詞「tanpa terkecuali（例外なく）」。"),
            ("Di ranah ketenagakerjaan, UU No. 8/2016 menetapkan kebijakan kuota ketenagakerjaan yang mengikat: instansi pemerintah dan BUMN wajib mempekerjakan paling sedikit 2 persen penyandang disabilitas, sedangkan perusahaan swasta diwajibkan memenuhi kuota minimal 1 persen. Pemerintah bersama organisasi advokasi mendirikan Unit Layanan Disabilitas Ketenagakerjaan guna memfasilitasi pelatihan vokasional dan pemetaan kecocokan kerja.",
             "雇用の領域において、2016年法第8号は拘束力ある雇用クォータ政策を定めている：政府機関および国営企業（BUMN）は従業員総数の最低2%以上の障害者を雇用することが義務付けられ、民間企業には最低1%のクォータ達成が義務付けられている。企業の遵守を促進するため、政府は権利擁護団体とともに障害者就労支援ユニット（ULD）を設立し、職業訓練や適職マッチングを支援している。",
             "関係詞節「kebijakan kuota yang mengikat（拘束力のある割当政策）」、対比接続詞「sedangkan perusahaan swasta...（一方民間企業は）」、目的接続詞「guna memfasilitasi...（〜を円滑化するために）」。"),
            ("Kendati kemajuan regulasi dan infrastruktur fisik patut diapresiasi, tantangan terbesar masih berakar pada stigma kultural dan rendahnya penegakan sanksi. Di banyak daerah, fasilitas pendidikan inklusif masih sangat terbatas dan trotoar berubin pemandu kerap diokupasi oleh pedagang kaki lima atau parkir liar. Mewujudkan Indonesia yang benar-benar inklusif menuntut penghapusan hambatan arsitektural sekaligus dekonstruksi prasangka sosial yang membatasi potensi kaum difabel.",
             "法制度や物理インフラの進歩は評価に値するものの、最大の課題は依然として文化的な偏見や法的制裁の執行力の弱さに根ざしている。地方の多くの地域ではインクルーシブ教育施設は未だ極めて限定的であり、点字ブロック付きの歩道はしばしば露店商に占拠されたりバイクの違法駐車スペースと化している。真に包摂的なインドネシアを実現することは、物理的・建築的バリアの撤廃と同時に、障害者の可能性を制限する社会的偏見の脱構築を要求している。",
             "譲歩構文「Kendati kemajuan... patut diapresiasi, tantangan terbesar masih berakar pada...」、受動態「kerap diokupasi oleh pedagang...」、結語の対比「penghapusan hambatan arsitektural sekaligus dekonstruksi prasangka sosial」。")
        ],
        "grammar": [
            ("受動動詞 terkungkung（閉じ込められている、束縛されている）", "語根 kungkung（首かせ・足かせ、囲い）に接頭辞 ter- が付き、自らの意志ではなく長年の慣習や誤った通念に「がんじがらめに縛り付けられている状態」を表します。"),
            ("法的権利用語 akomodasi yang layak（合理的配慮）", "国際的な障害者権利条約（CRPD）における 'Reasonable Accommodation' のインドネシア法公式訳。過度な負担を課さない範囲で障害者の権利行使を保障する環境調整を指します。"),
            ("新語・造語 difabel（ディファベル：異なる能力を持つ人々）", "英語の 'Differently Abled People' に由来するインドネシア発の呼称。cacad（障害・欠損）という侮蔑的表現を退け、尊厳と多様な能力を肯定する用語として学術・メディアで広く愛用されています。")
        ],
        "quiz": [
            {
                "q": "Berapa persentase kuota wajib mempekerjakan penyandang disabilitas bagi instansi pemerintah dan BUMN menurut UU No. 8/2016?",
                "options": ["Paling sedikit 1 persen", "Paling sedikit 2 persen", "Paling sedikit 5 persen", "Paling sedikit 10 persen"],
                "ans": "Paling sedikit 2 persen",
                "exp": "第3段落に「instansi pemerintah, BUMN, dan BUMD wajib mempekerjakan paling sedikit 2 persen penyandang disabilitas」と明記されています。"
            },
            {
                "q": "Apa nama fasilitas pedestrian di trotoar yang berfungsi memandu tuna netra?",
                "options": ["Ramp kursi roda", "Guiding blocks (ubin pemandu bertekstur)", "Zebra cross", "Underpass"],
                "ans": "Guiding blocks (ubin pemandu bertekstur)",
                "exp": "第2段落に「dilengkapi dengan ubin pemandu bertekstur (guiding blocks) bagi tunanetra」とあります。"
            },
            {
                "q": "Apa kepanjangan dari konsep 'difabel' dalam kesetaraan hak disabilitas?",
                "options": ["Different Abilities People", "Digital Fashion Label", "Direct Finance Balance", "Disaster Family Relief"],
                "ans": "Different Abilities People",
                "exp": "文法解説および第1段落にあるように、difabel は Differently Abled（異なる能力・特性を持つ人々）に由来する肯定的呼称です。"
            }
        ],
        "column": """### 深層コラム：スルタンの街ジョグジャカルタと車椅子活動家の挑戦

インドネシアにおいて、障害当事者運動の先進地として知られるのが古都ジョグジャカルタです。

1990年代から活動する「CIQAL」や「Dria Manunggal」といった草の根当事者団体は、行政と徹底的に対話し、王宮周辺の歩道スロープ設置や公立学校の統合教育をリードしてきました。また、車椅子ユーザーの女性たちが起業した手織りバティック工房や、ろう者が手話で接客するカフェ「Kopi Tuli（Fingertalk）」など、当事者が施しの客体から経済の担い手へと社会を能動的に変えていく実践が、インドネシア全土のロールモデルとなっています。"""
    },
    {
        "filename": "49-indonesian-gastro-tourism.md",
        "title": "49. 郷土料理探訪の旅：ストリートフードからミシュラン星獲得店まで巡る美食観光",
        "category": "長文読解・食文化・観光立国",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "スパイス諸島（Kepulauan Rempah）の歴史を背負うインドネシア料理は、CNNの「世界一美味しい料理」に選ばれたルンダンをはじめ、世界的な注目を集めています。伝統的なストリートフード（Kakilima）の屋台巡りから、気鋭のシェフによるファインダイニングの再解釈まで、美食を目的に旅する「ガストロノミー・ツーリズム（Wisata Gastronomi）」の熱気と文化戦略を解読します。",
        "passage": """Pariwisata Indonesia kini tengah mengalami metamorfosis mendalam dari model pariwisata pemandangan konvensional (sightseeing tourism) menuju pariwisata berbasis pengalaman otentik (experiential tourism). Di garda terdepan pergeseran tren ini, wisata kuliner dan gastronomi telah menjelma menjadi daya tarik magnetis yang mampu menggerakkan jutaan pelancong domestik maupun mancanegara. Dengan kekayaan ribuan resep pusaka yang diwariskan oleh ratusan suku bangsa serta ketersediaan rempah-rempah tropis yang tiada duanya, Indonesia menawarkan petualangan rasa yang sarat akan narasi historis dan filosofis.

Puncak pengakuan global terhadap cita rasa Nusantara tercermin dari terpilihnya hidangan khas Minangkabau, 'Rendang', sebagai salah satu makanan terlezat di dunia dalam berbagai survei internasional. Namun, daya pikat gastronomi Indonesia tidak hanya berhenti pada hidangan-hidangan ikonik seperti rendang, sate, dan nasi goreng. Dari gurihnya sup konro khas Makassar, segarnya kuah asam pedas ikan kuah kuning khas Maluku, hingga pedas manisnya sambal matah Bali, setiap daerah memiliki kekhasan 'terroir' geografis dan teknik pengolahan tradisional yang sangat distingtif.

Dalam beberapa tahun terakhir, panggung gastronomi nasional semakin diperkaya oleh keberanian para juru masak muda (chef) berbintang yang membawa hidangan jalanan dan resep desa ke tingkat santap mewah (fine dining). Restoran-restoran avant-garde di Bali dan Jakarta, seperti Locavore NXT dan Nusa Gastronomy, menerapkan filosofi 'hyper-local': menggunakan 100 persen bahan musiman dari petani lokal, mengadopsi teknik fermentasi kuno nusantara, serta menyajikan setiap piring bagaikan karya seni visual yang menceritakan riwayat rempah-rempah Nusantara kepada para tamu internasional.

Pengembangan wisata gastronomi kini diposisikan oleh Kementerian Pariwisata dan Ekonomi Kreatif sebagai pilar diplomasi budaya dan pengungkit ekonomi inklusif. Penyelenggaraan festival kuliner bertaraf internasional seperti Ubud Food Festival, standarisasi sertifikasi higienitas warung kaki lima, serta integrasi rute jalur rempah (Spice Route Trails) ke dalam paket wisata terbukti ampuh mendongkrak pendapatan pelaku UMKM pangan lokal sembari merawat kedaulatan warisan kuliner leluhur.""",
        "vocab": [
            ("metamorfosis mendalam", "名詞句", "深層のメタモルフォーシス（劇的変容）", "Industri pariwisata mengalami metamorfosis mendalam pascapandemi."),
            ("pariwisata berbasis pengalaman", "名詞句", "体験型観光 (Experiential Tourism)", "Pelancong kini lebih memilih pariwisata berbasis pengalaman budaya."),
            ("resep pusaka", "名詞句", "祖先伝来の秘伝レシピ", "Resep pusaka keluarga Minang dijaga kemurniannya secara turun-temurun."),
            ("cita rasa Nusantara", "名詞句", "群島の伝統の味・風味", "Kekayaan rempah membentuk cita rasa Nusantara yang kompleks."),
            ("kekhasan terroir", "名詞句 (食文化用語)", "地理的環境が生むテロワール特有の風味", "Kopi dan rempah memiliki kekhasan terroir di setiap lereng pulau."),
            ("santap mewah", "名詞句", "高級ダイニング (Fine Dining)", "Chef menyajikan interpretasi baru masakan desa ke meja santap mewah."),
            ("filosofi hyper-local", "名詞句", "超地域密着哲学（完全地産地消）", "Restoran mengusung filosofi hyper-local tanpa bahan pangan impor."),
            ("pengungkit ekonomi", "名詞句", "経済の牽引レバー・起爆剤", "Wisata gastronomi terbukti menjadi pengungkit ekonomi desa."),
            ("jalur rempah", "名詞句", "スパイス街道 (Spice Route)", "Napak tilas jalur rempah membuka wawasan sejarah perdagangan dunia."),
            ("merawat kedaulatan kuliner", "動詞句", "食の主権・伝統の尊厳を守り育てる", "Generasi muda berkewajiban merawat kedaulatan kuliner Nusantara.")
        ],
        "paragraphs": [
            ("Pariwisata Indonesia kini tengah mengalami metamorfosis mendalam dari model pariwisata pemandangan konvensional menuju pariwisata berbasis pengalaman otentik. Di garda terdepan pergeseran tren ini, wisata kuliner dan gastronomi telah menjelma menjadi daya tarik magnetis yang mampu menggerakkan jutaan pelancong. Dengan kekayaan ribuan resep pusaka serta ketersediaan rempah-rempah tropis yang tiada duanya, Indonesia menawarkan petualangan rasa yang sarat akan narasi historis dan filosofis.",
             "インドネシアの観光は今、従来の景色眺望型観光モデルから本物の体験型観光への深い変容（メタモルフォーシス）を経験している。このトレンドシフトの最前線において、食とガストロノミーの観光は、国内外の何百万人もの旅行者を動かす磁力的な魅力へと変貌を遂げた。何百もの民族によって受け継がれてきた数千の秘伝レシピと唯一無二の熱帯スパイスに恵まれ、インドネシアは歴史的・哲学的な物語に満ちた味覚の冒険を提供している。",
             "現在進行の様相「kini tengah mengalami...」、対比の前置詞句「dari model konvensional menuju...」、最前線を表す成句「Di garda terdepan...」、形容詞句「sarat akan narasi historis（歴史的ナラティブに満ち満ちた）」。"),
            ("Puncak pengakuan global terhadap cita rasa Nusantara tercermin dari terpilihnya hidangan Minangkabau, 'Rendang', sebagai salah satu makanan terlezat di dunia dalam berbagai survei internasional. Namun, daya pikat gastronomi Indonesia tidak hanya berhenti pada hidangan ikonik saja. Dari gurihnya sup konro Makassar, segarnya ikan kuah kuning Maluku, hingga pedas manisnya sambal matah Bali, setiap daerah memiliki kekhasan terroir geografis dan teknik pengolahan tradisional yang sangat distingtif.",
             "群島の味覚に対する世界的な評価の頂点は、ミナンカバウ地方の名物料理『ルンダン』が各種の国際調査で世界一美味しい料理の一つに選ばれたことに反映されている。しかし、インドネシアの美食の魅力は単に象徴的な定番料理だけに留まらない。マカッサルの濃厚なコンロ・スープの旨味、マルクの爽やかなイカン・クア・クニンの酸味と辛味、バリ島のサンバル・マタの甘辛さに至るまで、各地域が極めて際立った地理的テロワールの独自性と伝統調理法を備えている。",
             "受動名詞節「Puncak pengakuan... tercermin dari terpilihnya...」、相関否定「tidak hanya berhenti pada...」、名詞の並列描写「Dari gurihnya..., segarnya..., hingga pedas manisnya...」。"),
            ("Dalam beberapa tahun terakhir, panggung gastronomi nasional semakin diperkaya oleh keberanian para juru masak muda yang membawa hidangan jalanan dan resep desa ke tingkat santap mewah (fine dining). Restoran-restoran avant-garde di Bali dan Jakarta menerapkan filosofi 'hyper-local': menggunakan 100 persen bahan musiman dari petani lokal, mengadopsi teknik fermentasi kuno, serta menyajikan setiap piring bagaikan karya seni visual yang menceritakan riwayat rempah Nusantara.",
             "過去数年において、国内のガストロノミー界は、ストリートフードや農村のレシピを高級ダイニング（ファインダイニング）の高みへと引き上げる気鋭の若きシェフたちの挑戦によって一層豊かになっている。バリやジャカルタのアヴァンギャルドなレストランは、地元農家からの100%旬の食材を使用し、群島の古代の発酵技術を採用し、すべての一皿をスパイス街道の歴史を語る視覚的芸術作品のように提供する『ハイパーローカル（超地産地消）』哲学を実践している。",
             "受動態述語「semakin diperkaya oleh...（〜によってますます豊かにされている）」、コロンを用いた詳細展開「menerapkan filosofi: ...」、比況接続詞「bagaikan karya seni visual（あたかも視覚的芸術作品のように）」。"),
            ("Pengembangan wisata gastronomi kini diposisikan oleh Kemenparekraf sebagai pilar diplomasi budaya dan pengungkit ekonomi inklusif. Penyelenggaraan festival kuliner bertaraf internasional seperti Ubud Food Festival, standarisasi sertifikasi higienitas warung kaki lima, serta integrasi rute jalur rempah ke dalam paket wisata terbukti ampuh mendongkrak pendapatan UMKM sembari merawat kedaulatan warisan kuliner leluhur.",
             "ガストロノミー観光の推進は、観光・創造経済省によって文化外交の柱および包摂的経済の起爆レバーとして位置づけられている。ウブド・フード・フェスティバルのような国際規格の食の祭典の開催、屋台の衛生認証の標準化、そして観光ツアーへのスパイス街道ルートの統合は、先祖伝来の食の遺産の尊厳を守りつつ、地元の食品UMKMの収入を大幅に引き上げる上で絶大な威力を発揮している。",
             "受動態「kini diposisikan sebagai...（今や〜として位置づけられている）」、名詞列挙主語「Penyelenggaraan festival..., standarisasi..., serta integrasi...」、効果を称える成句述語「terbukti ampuh mendongkrak pendapatan...（収入を押し上げるのに絶大な効果を証明している）」。")
        ],
        "grammar": [
            ("接尾辞 -nya を伴う味覚形容詞の名詞化（gurihnya, segarnya）", "形容詞 gurih（旨味がある・香ばしい）、segar（爽やか・新鮮）に -nya が付き、「旨味の深さ」「爽快さ」という抽象名詞を形成する文語表現。五感に訴える食の論説文で多用されます。"),
            ("形容詞 sarat akan（〜で満ち満ちている、〜がぎっしり詰まった）", "sarat は元々「船や車に荷物が満載された」状態を表しますが、比喩的に「sarat akan narasi historis（歴史的物語に満ち溢れている）」のように抽象的内容の豊潤さを表します。"),
            ("成句 pengungkit ekonomi（経済の起爆剤、テコ、推進レバー）", "道具のテコ（ungkit）から派生した名詞 pengungkit。「経済を力強くテコの原理で持ち上げる起爆要因」という意味で、政策文書の定番語彙です。")
        ],
        "quiz": [
            {
                "q": "Hidangan khas daerah manakah 'Rendang' yang terpilih sebagai salah satu makanan terlezat di dunia?",
                "options": ["Sunda, Jawa Barat", "Minangkabau, Sumatra Barat", "Batak, Sumatra Utara", "Dayak, Kalimantan"],
                "ans": "Minangkabau, Sumatra Barat",
                "exp": "第2段落に「terpilihnya hidangan khas Minangkabau, 'Rendang', sebagai salah satu makanan terlezat di dunia」と明記されています。"
            },
            {
                "q": "Apa arti dari filosofi 'hyper-local' yang diterapkan restoran avant-garde menurut teks?",
                "options": ["Mengimpor semua bumbu mahal dari Eropa", "Menggunakan 100 persen bahan pangan musiman dari petani lokal tanpa bahan impor", "Menjual makanan hanya melalui aplikasi pesan antar online", "Menghapus semua menu tradisional dan menggantinya dengan burger"],
                "ans": "Menggunakan 100 persen bahan pangan musiman dari petani lokal tanpa bahan impor",
                "exp": "第3段落に「menerapkan filosofi 'hyper-local': menggunakan 100 persen bahan musiman dari petani lokal, mengadopsi teknik fermentasi kuno」とあります。"
            },
            {
                "q": "Festival kuliner bertaraf internasional apa yang disebutkan diselenggarakan di Bali?",
                "options": ["Jakarta Fashion Week", "Ubud Food Festival", "Pesta Kesenian Bali", "Solo Keroncong Festival"],
                "ans": "Ubud Food Festival",
                "exp": "最終段落に「festival kuliner bertaraf internasional seperti Ubud Food Festival」と記載されています。"
            }
        ],
        "column": """### 深層コラム：世界一の旨味の秘密「ルンダン」の哲学的四要素

ミナンカバウ社会において、ルンダンを煮込む行為は単なる料理ではなく、社会哲学の具現化とされています。ルンダンを構成する4つの基本材料には、それぞれ社会の役割が象徴されています：

1. **Daging（牛肉）**：社会全体を導くリーダーや部族長（Niniak Mamak）。
2. **Kelapa / Santan（ココナッツミルク）**：社会を豊かに潤す知識人・学者層（Cadiak Pandai）。
3. **Lada / Cabe（唐辛子）**：社会の規律を厳しく正す宗教指導者（Alim Ulama）。
4. **Pemasak / Bumbu（スパイス群）**：これら全体を調和させ結びつける一般社会・共同体（Keseluruhan Masyarakat）。

薪の火で焦がさぬよう何時間も根気強く木べらで混ぜ続けるプロセスは、人間が怒りや我欲を抑え、忍耐（Sabar）を培う精神修行そのものなのです。"""
    },
    {
        "filename": "50-vision-indonesia-emas-2045.md",
        "title": "50. 「黄金のインドネシア2045（Indonesia Emas 2045）」：建国100年に向けた先進国入りのシナリオ",
        "category": "長文読解・国家戦略・未来予測",
        "cefr": "CEFR B2-C1 (中上級〜上級)",
        "intro": "2045年の独立100周年に向けて、インドネシアが国家の総力を挙げて掲げるメガビジョン「Indonesia Emas 2045」。中所得国の罠（Middle Income Trap）を脱出し、世界トップ5の経済大国・高所得先進国入りを果たすための国家長期開発計画（RPJPN 2025-2045）の青写真、人材育成、グリーン産業革命、そして地政学的挑戦を包括的に総括読解します。",
        "passage": """Tepat satu abad pasca-Proklamasi Kemerdekaan 17 Agustus 1945, Republik Indonesia membidik lompatan peradaban terbesar dalam sejarah modernnya melalui visi megah 'Indonesia Emas 2045'. Dokumen Rencana Pembangunan Jangka Panjang Nasional (RPJPN) 2025–2045 yang dirumuskan oleh Kementerian PPN/Bappenas menetapkan target ambisius namun terukur: mentransformasikan Indonesia dari negara berpendapatan menengah-atas (upper-middle income) menjadi negara maju berpendapatan tinggi (high-income country) dengan Produk Domestik Bruto (PDB) nominal yang menembus jajaran lima besar kekuatan ekonomi dunia.

Peta jalan menuju status negara maju tersebut bertumpu pada lima pilar transformasi fundamental. Pilar pertama adalah transformasi ekonomi melalui hilirisasi industri bernilai tambah tinggi berbasis sumber daya alam hayati dan mineral, percepatan transisi energi hijau terbarukan, serta digitalisasi menyeluruh di semua sektor produktif. Indonesia bertekad melepaskan diri secara permanen dari kutukan pengekspor bahan mentah menuju produsen komponen teknologi tinggi global. Pilar kedua dan ketiga menekankan pada transformasi sosial dan tata kelola: mencetak sumber daya manusia (SDM) unggul berpendidikan sains-teknologi tinggi yang sehat bebas stunting, serta mereformasi birokrasi pemerintahan menjadi institusi yang bersih, transparan, dan berintegritas hukum mutlak.

Kendati visi tersebut memancarkan harapan masa depan yang gemilang, jalan menuju Indonesia Emas tidaklah bebas dari jebakan struktural. Tantangan paling krusial adalah ancaman perangkap pendapatan menengah (middle-income trap) yang kerap menjerat negara-negara berkembang ketika pertumbuhan produktivitas gagal mengimbangi kenaikan upah. Selain itu, menyempitnya jendela demografi emas pada dekade 2030-an menuntut pemerintah untuk bergerak cepat meningkatkan kualitas sistem pendidikan vokasi dan riset universitas agar jutaan angkatan kerja muda tidak terperangkap dalam sektor informal yang berpenghasilan rendah.

Menatap tahun 2045, Indonesia tidak hanya dituntut untuk menjadi raksasa ekonomi, melainkan juga mercusuar demokrasi yang berkeadilan sosial, berwawasan lingkungan lestari, dan memainkan kepemimpinan geopolitik bebas-aktif yang bermartabat di panggung global. Keberhasilan merealisasikan visi Indonesia Emas pada akhirnya bertumpu pada konsistensi kepemimpinan lintas generasi dan persatuan nasional yang teguh berlandaskan Pancasila dan Bhinneka Tunggal Ika.""",
        "vocab": [
            ("lompatan peradaban", "名詞句", "文明の飛躍、歴史的大跳躍", "Indonesia Emas adalah lompatan peradaban menuju negara maju."),
            ("negara berpendapatan tinggi", "名詞句 (世界銀行定義)", "高所得国、先進国 (High-income Country)", "Target 2045 adalah mencapai status negara berpendapatan tinggi."),
            ("lima besar kekuatan ekonomi", "名詞句", "世界5大経済大国", "PDB Indonesia diproyeksikan menembus lima besar kekuatan ekonomi."),
            ("hilirisasi bernilai tambah", "名詞句", "高付加価値下流化産業化 (Downstreaming)", "Hilirisasi bernilai tambah menjadi mesin utama pertumbuhan PDB."),
            ("perangkap pendapatan menengah", "名詞句 (経済学用語)", "中所得国の罠 (Middle-Income Trap)", "Banyak negara gagal keluar dari perangkap pendapatan menengah."),
            ("bebas stunting", "形容詞句", "発育阻害（低身長症）ゼロの", "Pencegahan gizi buruk menciptakan generasi emas yang bebas stunting."),
            ("integritas hukum mutlak", "名詞句", "絶対的な法の完全性・清廉性", "Kepastian investasi menuntut kepastian integritas hukum mutlak."),
            ("sektor informal", "名詞句", "非公式セクター、インフォーマル雇用", "Pemerintah berupaya memindahkan pekerja informal ke sektor formal."),
            ("mercusuar demokrasi", "名詞句", "民主主義の灯台・導きの光", "Indonesia bertekad menjadi mercusuar demokrasi di kawasan Asia."),
            ("konsistensi lintas generasi", "名詞句", "世代を超えた政策の一貫性", "Pembangunan jangka panjang membutuhkan konsistensi lintas generasi.")
        ],
        "paragraphs": [
            ("Tepat satu abad pasca-Proklamasi Kemerdekaan, Republik Indonesia membidik lompatan peradaban terbesar dalam sejarah modernnya melalui visi megah 'Indonesia Emas 2045'. Dokumen RPJPN 2025–2045 menetapkan target ambisius namun terukur: mentransformasikan Indonesia dari negara berpendapatan menengah-atas menjadi negara maju berpendapatan tinggi dengan Produk Domestik Bruto (PDB) nominal yang menembus jajaran lima besar kekuatan ekonomi dunia.",
             "1945年8月17日の独立宣言からちょうど1世紀を経て、インドネシア共和国は壮大なビジョン『黄金のインドネシア2045』を通じて、その近代史における最大の文明的跳躍を狙っている。国家開発計画省（Bappenas）によって策定された国家長期開発計画（RPJPN 2025-2045）文書は、野心的かつ測定可能な目標を定めている：名目国内総生産（GDP）で世界5大経済大国の一角に食い込み、インドネシアを高中所得国から高所得の先進国へと変革することである。",
             "時制表現「Tepat satu abad pasca-Proklamasi...」、比喩動詞「membidik lompatan peradaban（文明の跳躍に照準を合わせる）」、使役動詞句「mentransformasikan Indonesia dari... menjadi...（インドネシアを〜から…へと変革する）」。"),
            ("Peta jalan menuju status negara maju tersebut bertumpu pada lima pilar transformasi fundamental. Pilar pertama adalah transformasi ekonomi melalui hilirisasi industri bernilai tambah tinggi, percepatan transisi energi hijau, serta digitalisasi menyeluruh. Indonesia bertekad melepaskan diri dari kutukan pengekspor bahan mentah. Pilar kedua dan ketiga menekankan pada transformasi sosial dan tata kelola: mencetak SDM unggul berpendidikan sains tinggi yang bebas stunting, serta mereformasi birokrasi menjadi institusi yang transparan dan berintegritas hukum.",
             "先進国の地位へ向かうロードマップは、5つの根本的な変革の柱に基づいている。第1の柱は、高付加価値な産業下流化、グリーンエネルギー移行の加速、あらゆる分野のデジタル化を通じた経済変革である。インドネシアは原料輸出国という呪縛から恒久的に脱却することを決意している。第2・第3の柱は社会と統治の変革を強調する：発育阻害（スタンティング）のない健康で高度な科学技術教育を受けた優れた人材（SDM）を育成し、官僚機構を透明で絶対的な法的清廉性を備えた組織へと改革することである。",
             "動詞句「bertumpu pada lima pilar transformasi...（5つの変革の柱に基づく）」、比喩表現「melepaskan diri dari kutukan pengekspor bahan mentah（原料輸出国の呪縛から脱却する）」、動詞句「mencetak SDM unggul（優れた人材を輩出する）」。"),
            ("Kendati visi tersebut memancarkan harapan masa depan yang gemilang, jalan menuju Indonesia Emas tidaklah bebas dari jebakan struktural. Tantangan paling krusial adalah ancaman perangkap pendapatan menengah (middle-income trap) yang kerap menjerat negara-negara berkembang. Selain itu, menyempitnya jendela demografi emas pada dekade 2030-an menuntut pemerintah untuk bergerak cepat meningkatkan kualitas pendidikan vokasi agar jutaan angkatan kerja muda tidak terperangkap dalam sektor informal.",
             "このビジョンが輝かしい未来の希望を放っているにもかかわらず、黄金のインドネシアへの道は構造的な罠と無縁ではない。最も極めて重要な課題は、途上国をしばしば捕らえる「中所得国の罠（Middle-Income Trap）」の脅威である。さらに、2030年代における人口ボーナスの好機の窓の狭まりは、何百万人もの若い労働力が低所得のインフォーマルセクターに閉じ込められないよう、職業教育や大学研究の質を向上させるため迅速に行動することを政府に要求している。",
             "譲歩構文「Kendati visi tersebut memancarkan..., jalan menuju... tidaklah bebas dari...（〜であるものの、…と無縁ではない）」、関係詞節「yang kerap menjerat negara berkembang（途上国をしばしば罠にかける）」、動名詞主語「menyempitnya jendela demografi emas... menuntut...（人口ボーナスの狭まりが〜を要求する）」。"),
            ("Menatap tahun 2045, Indonesia tidak hanya dituntut untuk menjadi raksasa ekonomi, melainkan juga mercusuar demokrasi yang berkeadilan sosial, berwawasan lingkungan lestari, dan memainkan kepemimpinan geopolitik bebas-aktif yang bermartabat di panggung global. Keberhasilan merealisasikan visi Indonesia Emas pada akhirnya bertumpu pada konsistensi kepemimpinan lintas generasi dan persatuan nasional yang teguh berlandaskan Pancasila dan Bhinneka Tunggal Ika.",
             "2045年を見据え、インドネシアは単に経済の巨人となることだけでなく、社会正義に満ち、持続可能な環境観を備え、世界の舞台で品格ある「自由・能動（Bebas-Aktif）」の地政学的リーダーシップを発揮する民主主義の灯台となることを求められている。黄金のインドネシアというビジョンを実現できるかどうかの成功は、最終的には世代を超えたリーダーシップの一貫性と、パンチャシラおよび多様性の中の統一（Bhinneka Tunggal Ika）に固く根ざした国民的連帯にかかっている。",
             "未来志向の分詞節「Menatap tahun 2045, ...」、相関構文「tidak hanya dituntut untuk menjadi..., melainkan juga mercusuar demokrasi...」、格調高い結語「persatuan nasional yang teguh berlandaskan Pancasila dan Bhinneka Tunggal Ika（パンチャシラと多様性の統一に固く根ざした国民的連帯）」。")
        ],
        "grammar": [
            ("成句 lompatan peradaban（文明の跳躍、飛躍的発展）", "lompat（跳ぶ）の名詞派生語 lompatan と peradaban（文明）が結合した壮大な国家論説表現。小幅な漸進的改善ではなく、国家のステージを根本から一段引き上げる大飛躍を指します。"),
            ("比喩表現 kutukan pengekspor bahan mentah（原料輸出国の呪縛）", "資源の呪い（Resource Curse）の文脈で用いられる語彙。自国の豊かな鉱物・農産物を未加工のまま安価で輸出し、他国の高付加価値工業製品を高値で買い戻す植民地型経済構造の脱却意志を象徴します。"),
            ("比喩成句 mercusuar demokrasi（民主主義の灯台、道標）", "mercusuar（灯台）を用いた国家比喩。暗闇の海を照らす光のように、多民族・多宗教の巨大国家でありながら民主主義と寛容を両立させる模範国となる誇りを表します。")
        ],
        "quiz": [
            {
                "q": "Tahun berapakah yang menjadi target pencapaian visi 'Indonesia Emas' bertepatan dengan satu abad kemerdekaan?",
                "options": ["Tahun 2030", "Tahun 2045", "Tahun 2050", "Tahun 2100"],
                "ans": "Tahun 2045",
                "exp": "第1段落冒頭に「Tepat satu abad pasca-Proklamasi Kemerdekaan 17 Agustus 1945... melalui visi megah 'Indonesia Emas 2045'」と明記されています。"
            },
            {
                "q": "Apa ancaman struktural utama yang kerap menjerat negara berkembang menurut teks?",
                "options": ["Kekurangan cadangan minyak bumi", "Perangkap pendapatan menengah (middle-income trap)", "Turunnya jumlah wisatawan mancanegara", "Terlalu banyaknya universitas negeri"],
                "ans": "Perangkap pendapatan menengah (middle-income trap)",
                "exp": "第3段落に「ancaman perangkap pendapatan menengah (middle-income trap) yang kerap menjerat negara-negara berkembang」と明記されています。"
            },
            {
                "q": "Dua semboyan/falsafah kebangsaan apa yang menjadi fondasi persatuan nasional Indonesia menuju 2045?",
                "options": ["Devide et Impera dan VOC", "Pancasila dan Bhinneka Tunggal Ika", "Trisakti dan Manifesto Politik", "Sumpah Palapa dan Piagam Jakarta"],
                "ans": "Pancasila dan Bhinneka Tunggal Ika",
                "exp": "最終文に「persatuan nasional yang teguh berlandaskan Pancasila dan Bhinneka Tunggal Ika」と記載されています。"
            }
        ],
        "column": """### 深層コラム：セクション32完結記念：群島の記憶と未来を結ぶ旅

全50記事にわたる「インドネシア現代社会・トレンド深層読解（Contemporary Reading）」は、EVニッケル下流化革命から始まり、TikTok規制、新首都IKN、地熱エネルギー、映画・インディーズ音楽、食文化・ジェンダー、海洋主権、宇宙衛星、eスポーツ、火山共生、そして「黄金のインドネシア2045」国家ビジョンに至るまで、今まさに躍動する2億8千万人の大国の光と影、伝統と革新のドラマを活写してきました。

インドネシア語を学ぶということは、単に単語や文法を覚えることにとどまりません。17,000の島々を跨ぐ多様性の哲学、自然との共生、苦難の歴史を乗り越えて前を向く人々の温かい魂（Jiwa Nusantara）と対話することです。この50本の深層読解を読破した学習者は、すでに現地の一流論説を読み解き、現地の知識人と対等に議論できる最高峰の知的教養と言語運用力をその手にしています。"""
    }
]

def generate_markdown(a):
    md = []
    md.append(f"# {a['title']}\n")
    md.append(f'<span class="badge badge-reading">長文読解</span> <span class="badge badge-society">現代社会</span> <span class="badge badge-advanced">時事深層</span>\n')
    md.append(f"- **読了目安**: 15分")
    md.append(f"- **レベル**: {a['cefr']}")
    md.append(f"- **テーマ領域**: {a['category']}\n")
    md.append("---\n")
    
    md.append("## 導入と背景\n")
    md.append(f"{a['intro']}\n")
    
    md.append("## 本文：Reading Passage\n")
    md.append(f"{a['passage']}\n")
    
    md.append("## 重要語彙・専門用語・コロケーション\n")
    md.append("| 語彙・表現 | 品詞・分類 | 日本語義 | 例文・共起表現 |")
    md.append("| :--- | :--- | :--- | :--- |")
    for term, pos, meaning, ex in a["vocab"]:
        md.append(f"| **{term}** | {pos} | {meaning} | {ex} |")
    md.append("\n")
    
    md.append("## 段落別対訳・日本語全訳\n")
    for i, (orig, trans, logic) in enumerate(a["paragraphs"], 1):
        md.append(f"### 第{i}段落\n")
        md.append(f"> {orig}\n")
        md.append(f"**【日本語訳】**  \n{trans}\n")
        md.append(f"**【論理構造と読解着眼点】**  \n{logic}\n")
    
    md.append("## 文法・論理構造の深層解説\n")
    for title, exp in a["grammar"]:
        md.append(f"### {title}\n")
        md.append(f"{exp}\n")
    
    md.append("## 読解理解度チェック（3問）\n")
    for i, q in enumerate(a["quiz"], 1):
        md.append(f"**Q{i}. {q['q']}**\n")
        for opt in q["options"]:
            md.append(f"- {opt}")
        md.append("\n")
        md.append(f'<details>\n<summary>正解と解説を見る</summary>\n<div class="answer-box">\n')
        md.append(f"**正解**: 「**{q['ans']}**」\n")
        md.append(f"**解説**: {q['exp']}\n")
        md.append("</div>\n</details>\n")
    
    md.append("## 現地事情・深層背景コラム\n")
    md.append(f"{a['column']}\n")
    
    md.append("---\n")
    md.append("## 次の学習ステップ・関連リンク\n")
    md.append("- [総合サイトマップ](../sitemap.md)")
    md.append("- [トップページ](../index.md)\n")
    
    return "\n".join(md)

def main():
    target_dir = os.path.join("docs", "contemporary")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        fpath = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {fpath}")

if __name__ == "__main__":
    main()
