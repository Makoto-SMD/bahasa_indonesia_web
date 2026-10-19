# -*- coding: utf-8 -*-
import os
import re

stories = [
    {
        "id": "1221",
        "slug": "level-3-01-ojek-online-driver",
        "title": "【Level 3 (B1)】Kisah Pengemudi Ojek Online di Ibu Kota（配車ドライバーの一日と街の息吹）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "ジャカルタのメガロポリスを疾走するオジェック・オンライン（Ojol）の日常を通じて、現代都市の機動力、スマホ配車アプリ、人情味あふれる助け合いを描く中級読解パッセージ。",
        "text": """Matahari baru saja menampakkan sinarnya di ufuk timur ketika Pak Hendra sudah mengenakan jaket hijau khasnya. Sebagai seorang mitra pengemudi ojek daring di Jakarta, hari-harinya dihabiskan untuk membelah jalanan ibu kota yang selalu padat dan dinamis. Sebelum menyalakan aplikasi di ponsel pintarnya, ia selalu menyempatkan diri memeriksa tekanan ban dan mengisi bensin kendaraannya agar perjalanan penumpang tetap aman.

Begitu aplikasi diaktifkan, bunyi denting pesanan pertama langsung berdering. Pak Hendra menerima pesanan untuk mengantarkan seorang karyawan kantor dari kawasan Tebet menuju pusat perkantoran di Jalan Sudirman. Di tengah kemacetan pagi yang mencekik, kelihaiannya meliuk-liuk di antara deretan mobil menjadi penyelamat bagi para pekerja yang berkejaran dengan waktu presensi sidik jari.

Tidak hanya mengantar penumpang, pekerjaan Pak Hendra juga mencakup pengantaran makanan dan barang. Menjelang waktu makan siang, pesanan makanan siap saji melonjak tajam. Ia harus mengantre dengan sabar di restoran favorit sambil memastikan rincian pesanan pelanggan sesuai tanpa ada yang terlewat. Meskipun cuaca terik terasa membakar kulit, senyuman ramah dan ucapan terima kasih yang tulus dari pelanggan selalu menjadi penawar lelah yang ampuh baginya.

Menjadi pengemudi ojek daring di era digital bukan sekadar mencari nafkah untuk keluarga tercinta, melainkan juga menjadi bagian penting dari denyut nadi perekonomian perkotaan. Di jalanan, Pak Hendra dan ribuan rekan seprofesinya saling tolong-menolong ketika ada yang mengalami mogok atau kecelakaan kecil. Solidaritas persaudaraan tanpa memandang suku dan agama inilah yang membuat jalanan ibu kota terasa hangat di balik kepulan asap knalpot.""",
        "paragraphs": [
            ("Matahari baru saja menampakkan sinarnya di ufuk timur ketika Pak Hendra sudah mengenakan jaket hijau khasnya. Sebagai seorang mitra pengemudi ojek daring di Jakarta, hari-harinya dihabiskan untuk membelah jalanan ibu kota yang selalu padat dan dinamis. Sebelum menyalakan aplikasi di ponsel pintarnya, ia selalu menyempatkan diri memeriksa tekanan ban dan mengisi bensin kendaraannya agar perjalanan penumpang tetap aman.",
             "太陽が東の地平線にその光を現したばかりの早朝、ヘンドラさんはすでにトレードマークの緑のジャケットを身にまとっていました。ジャカルタのオンライン配車バイク（Ojol）のパートナー運転手として、彼の日々は常に混雑しダイナミックに動く首都の街路を駆け抜けることに費やされます。スマートフォンでアプリを起動する前に、彼は乗客の道中が常に安全であるよう、タイヤの空気圧を点検しガソリンを満タンにする時間を必ず取ります。",
             "menampakkan sinar（光を現す）、mitra pengemudi（パートナー運転手）、membelah jalanan（道路を縫うように疾走する）、menyempatkan diri（わざわざ時間を取る）。"),
            ("Begitu aplikasi diaktifkan, bunyi denting pesanan pertama langsung berdering. Pak Hendra menerima pesanan untuk mengantarkan seorang karyawan kantor dari kawasan Tebet menuju pusat perkantoran di Jalan Sudirman. Di tengah kemacetan pagi yang mencekik, kelihaiannya meliuk-liuk di antara deretan mobil menjadi penyelamat bagi para pekerja yang berkejaran dengan waktu presensi sidik jari.",
             "アプリを有効化するやいなや、最初の注文を知らせるチャイムの音がすぐに鳴り響きました。ヘンドラさんは、テベット地区からスディルマン通りのオフィス街へ会社員を送り届ける注文を受けました。息が詰まるような朝の渋滞のただ中で、車の列の間を巧みにすり抜ける彼の卓越した運転技術は、指紋認証の出勤打刻時間に追われるビジネスパーソンにとっての救世主となります。",
             "begitu... langsung...（〜するやいなや、すぐに〜）、kemacetan yang mencekik（息の詰まるような渋滞）、kelihaian（卓越した腕前・器用さ）、meliuk-liuk（くねくねとすり抜ける）、presensi sidik jari（指紋認証打刻）。"),
            ("Tidak hanya mengantar penumpang, pekerjaan Pak Hendra juga mencakup pengantaran makanan dan barang. Menjelang waktu makan siang, pesanan makanan siap saji melonjak tajam. Ia harus mengantre dengan sabar di restoran favorit sambil memastikan rincian pesanan pelanggan sesuai tanpa ada yang terlewat. Meskipun cuaca terik terasa membakar kulit, senyuman ramah dan ucapan terima kasih yang tulus dari pelanggan selalu menjadi penawar lelah yang ampuh baginya.",
             "乗客を送迎するだけでなく、ヘンドラさんの仕事は料理や荷物の配達にも及びます。昼食の時間が近づくにつれ、ファストフードや出来立て料理の注文が急増します。彼は人気のレストランで根気よく順番を待ちながら、顧客の注文詳細に漏れがなく合致しているかを確認しなければなりません。肌を焼くように照りつける暑さであっても、顧客からの温かい笑顔と心からの「ありがとう」という言葉は、彼にとって常に強力な疲労回復剤となります。",
             "mencakup（〜を包括する）、melonjak tajam（急増する・跳ね上がる）、rincian pesanan（注文の詳細）、penawar lelah（疲労の特効薬・解毒剤）。"),
            ("Menjadi pengemudi ojek daring di era digital bukan sekadar mencari nafkah untuk keluarga tercinta, melainkan juga menjadi bagian penting dari denyut nadi perekonomian perkotaan. Di jalanan, Pak Hendra dan ribuan rekan seprofesinya saling tolong-menolong ketika ada yang mengalami mogok atau kecelakaan kecil. Solidaritas persaudaraan tanpa memandang suku dan agama inilah yang membuat jalanan ibu kota terasa hangat di balik kepulan asap knalpot.",
             "デジタル時代においてオンライン配車ドライバーになることは、単に愛する家族のために生計を立てるだけでなく、都市経済の鼓動の不可欠な一部となることでもあります。路上では、ヘンドラさんと何千人もの同業仲間が、故障や小さな事故に見舞われた際に互いに助け合っています。民族や宗教の違いを問わないこの同胞としての連帯感こそが、排気ガスの煙の立ち込める首都の街路に温もりをもたらしているのです。",
             "bukan sekadar... melainkan...（単に〜ではなく、むしろ〜である）、denyut nadi perekonomian（経済の鼓動）、saling tolong-menolong（互いに助け合う）、solidaritas persaudaraan（同胞の連帯感）。")
        ],
        "vocab": [
            ("mitra", "名詞", "-", "パートナー、提携先（ギグワーカーと配車プラットフォームの関係）", "Ia terdaftar sebagai mitra pengemudi aktif."),
            ("membelah", "動詞", "belah", "切り開く、（道路を）縫うように走る", "Kereta api membelah malam yang sunyi."),
            ("kelihaian", "名詞", "lihai", "巧妙さ、卓越した技能・敏捷性", "Kelihaian sopir itu melewati gang sempit."),
            ("meliuk-liuk", "動詞", "liuk", "身をくねらせる、蛇行して進む", "Motor meliuk-liuk di antara kemacetan."),
            ("mencakup", "動詞", "cakup", "包括する、及ぶ", "Tugas ini mencakup berbagai bidang kerja."),
            ("melonjak", "動詞", "lonjak", "跳ね上がる、急増する", "Harga cabai melonjak tajam saat hari raya."),
            ("rincian", "名詞", "rinci", "詳細、明細、細目", "Harap periksa rincian pembelian barang."),
            ("penawar", "名詞", "tawar", "解毒剤、緩和するもの、中和薬", "Teh hangat menjadi penawar rasa dingin."),
            ("denyut nadi", "名詞句", "denyut", "脈拍、鼓動、原動力", "Pasar tradisional adalah denyut nadi kota."),
            ("solidaritas", "名詞", "-", "連帯感、団結、結束", "Solidaritas warga desa sangat kuat.")
        ],
        "grammar_points": """1. **相関構文 `bukan sekadar... melainkan...`（単に〜だけでなく、むしろ〜である）**:
   - 事象の意義をより高次・本質的なレベルへ引き上げる構文です。
   - 例: *Bukan sekadar mencari uang, melainkan juga mengabdi.*（単にお金を稼ぐだけでなく、社会に奉仕することでもある。）
2. **無意志・受動接頭辞 `ter-` の多様な用法**:
   - *terlewat*（見落とされる、うっかり通り過ぎる）
   - *tercatat*（記録されている）
   - *terbakar*（焼かれる、燃える）
3. **即時接続詞 `begitu ... langsung ...`（〜するとすぐに〜）**:
   - 事象の連続的・即時的な発生を表します。
   - 例: *Begitu aplikasi dibuka, pesanan langsung masuk.*（アプリを開くやいなや、すぐに注文が入った。）""",
        "quizzes": [
            ("ヘンドラさんが毎朝アプリを起動する前に必ず行う安全点検は何ですか？",
             ["ヘルメットのペイントの塗り直し", "タイヤの空気圧点検とガソリンの補給", "朝食のカフェでの撮影"],
             "タイヤの空気圧点検とガソリンの補給",
             "第1段落に「...ia selalu menyempatkan diri memeriksa tekanan ban dan mengisi bensin kendaraannya...」とあります。"),
            ("朝の混雑時に会社員にとってヘンドラさんの巧みな運転が救いとなる理由は何ですか？",
             ["会社の指紋認証打刻（presensi sidik jari）の時間に間に合わせるため", "渋滞中に観光案内をしてくれるため", "無料で新聞を配布してくれるため"],
             "会社の指紋認証打刻（presensi sidik jari）の時間に間に合わせるため",
             "第2段落に「...penyelamat bagi para pekerja yang berkejaran dengan waktu presensi sidik jari.」とあります。"),
            ("過酷な路上業務の中で、ヘンドラさんにとって最も強力な「疲労回復剤（penawar lelah）」となるものは何ですか？",
             ["顧客からの高額なチップ", "顧客からの温かい笑顔と心からの感謝の言葉", "路上で飲む冷たいエナジードリンク"],
             "顧客からの温かい笑顔と心からの感謝の言葉",
             "第3段落に「...senyuman ramah dan ucapan terima kasih yang tulus dari pelanggan selalu menjadi penawar lelah yang ampuh...」とあります。")
        ],
        "culture": """### インドネシアの交通インフラを支える「Ojol（オジョル）」文化
インドネシアの都市生活に欠かせない「Ojol（Ojek Onlineの略称）」は、GojekやGrabなどの配車スーパーアプリを通じて急成長しました。
単なる移動手段（Goride/GrabBike）にとどまらず、食事配達（Gofood/GrabFood）、宅配便（Gosend）、買い物代行など、生活全般の物流を担っています。
ドライバー同士の仲間意識は非常に強く、路上でトラブルが起きると互いに助け合う「Solidaritas Ojol」は、現代ジャカルタの新たな都市互助コミュニティの象徴となっています。"""
    },
    {
        "id": "1222",
        "slug": "level-3-02-digital-wallet-revolution",
        "title": "【Level 3 (B1)】Dompet Digital dan Warung Tradisional（屋台に広がるQRIS決済革命）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "伝統的な個人商店や露店にまで浸透した国家統一QRコード「QRIS」と電子マネー。金融包摂の進展と下町の商店主の奮闘を描く中級経済・生活ストーリー。",
        "text": """Ibu Siti telah mengelola sebuah warung kelontong kecil di sudut perumahan selama lebih dari dua dekade. Dahulu, semua transaksi dilakukan secara tunai menggunakan uang koin dan kertas yang sering kali lusuh. Masalah yang kerap dihadapinya adalah kekurangan uang receh untuk kembalian pembeli, atau risiko menerima uang palsu di malam hari.

Namun, pemandangan di warungnya berubah drastis sejak cucunya membantu mendaftarkan QRIS, yaitu standar kode respons cepat nasional Indonesia. Kini, selembar kertas akrilik dengan kode cetak hitam-putih terpampang jelas di dekat toples biskuit dagangannya. Para pembeli, mulai dari pelajar sekolah hingga ibu-ibu rumah tangga, cukup mengarahkan kamera ponsel mereka untuk menyelesaikan pembayaran dalam hitungan detik.

Awalnya, Ibu Siti merasa waswas dan canggung menggunakan teknologi digital ini. Ia khawatir uang hasil keringatnya tidak masuk ke rekening atau saldo tabungannya hilang karena kejahatan siber. Akan tetapi, setelah merasakan kemudahan notifikasi suara yang mengonfirmasi transaksi secara langsung di ponsel tuanya, ketakutan itu sirna berganti rasa percaya diri.

Kehadiran dompet digital dan sistem QRIS telah mempercepat inklusi finansial hingga ke lapisan masyarakat terbawah. Warung tradisional milik Ibu Siti kini mampu bersaing dengan toko ritel modern di jalan utama. Tanpa perlu repot mencari uang kembalian dan terbebas dari ancaman uang palsu, para pedagang mikro dapat lebih fokus membesarkan usaha mereka demi masa depan keluarga.""",
        "paragraphs": [
            ("Ibu Siti telah mengelola sebuah warung kelontong kecil di sudut perumahan selama lebih dari dua dekade. Dahulu, semua transaksi dilakukan secara tunai menggunakan uang koin dan kertas yang sering kali lusuh. Masalah yang kerap dihadapinya adalah kekurangan uang receh untuk kembalian pembeli, atau risiko menerima uang palsu di malam hari.",
             "シティおばさんは、住宅街の一角にある小さな雑貨屋（ワルン）を20年以上にわたって切り盛りしてきました。以前は、すべての取引が頻繁によれよれになった硬貨や紙幣を使った現金で行われていました。彼女がしばしば直面していた問題は、客への釣り銭用の小銭の不足や、夜間に偽札を受け取ってしまうリスクでした。",
             "warung kelontong（日用雑貨屋・小規模商店）、lusuh（擦り切れた・使い古された）、uang receh（小銭）、uang palsu（偽札）。"),
            ("Namun, pemandangan di warungnya berubah drastis sejak cucunya membantu mendaftarkan QRIS, yaitu standar kode respons cepat nasional Indonesia. Kini, selembar kertas akrilik dengan kode cetak hitam-putih terpampang jelas di dekat toples biskuit dagangannya. Para pembeli, mulai dari pelajar sekolah hingga ibu-ibu rumah tangga, cukup mengarahkan kamera ponsel mereka untuk menyelesaikan pembayaran dalam hitungan detik.",
             "しかし、孫がインドネシアの国家統一クイックレスポンスコード規格である「QRIS（クリス）」の登録を手伝ってくれて以来、彼女の店の光景は劇的に変化しました。今では、白黒印刷されたコードが挟まれたアクリル板が、売り物のビスケット瓶のすぐ隣に誇らしげに掲げられています。学生から主婦に至るまで、買い手はスマートフォンのカメラを向けるだけで、わずか数秒で支払いを完了させることができます。",
             "berubah drastis（劇的に変化する）、terpampang jelas（はっきりと掲示されている）、mengarahkan kamera（カメラを向ける）、dalam hitungan detik（数秒の瞬く間に）。"),
            ("Awalnya, Ibu Siti merasa waswas dan canggung menggunakan teknologi digital ini. Ia khawatir uang hasil keringatnya tidak masuk ke rekening atau saldo tabungannya hilang karena kejahatan siber. Akan tetapi, setelah merasakan kemudahan notifikasi suara yang mengonfirmasi transaksi secara langsung di ponsel tuanya, ketakutan itu sirna berganti rasa percaya diri.",
             "当初、シティおばさんはこのデジタル技術を使うことに不安とぎこちなさを感じていました。彼女は、血と汗の結晶である売上金が銀行口座に入らないのではないか、あるいはサイバー犯罪によって預金残高が消えてしまうのではないかと心配していました。しかしながら、古い携帯電話から取引を即座に確認してくれる音声通知の便利さを実感して以降、その恐怖は消え去り、自信へと取って代わりました。",
             "waswas（不安な・心配な）、hasil keringat（汗水流して得た結晶）、kejahatan siber（サイバー犯罪）、sirna（消え去る）。"),
            ("Kehadiran dompet digital dan sistem QRIS telah mempercepat inklusi finansial hingga ke lapisan masyarakat terbawah. Warung tradisional milik Ibu Siti kini mampu bersaing dengan toko ritel modern di jalan utama. Tanpa perlu repot mencari uang kembalian dan terbebas dari ancaman uang palsu, para pedagang mikro dapat lebih fokus membesarkan usaha mereka demi masa depan keluarga.",
             "デジタルウォレットとQRISシステムの登場は、社会の最末端の層にまで金融包摂（ファイナンシャル・インクルージョン）を加速させました。シティおばさんの伝統的な個人商店は今や、大通り沿いにある近代的な小売チェーン店とも互角に競争できるようになっています。釣り銭を探す煩わしさから解放され、偽札の脅威からも守られたことで、零細商店主たちは家族の未来のために自らの事業を成長させることへより集中できるようになったのです。",
             "kehadiran（登場・存在）、inklusi finansial（金融包摂）、lapisan masyarakat terbawah（社会の最末端層）、pedagang mikro（零細商人）。")
        ],
        "vocab": [
            ("mengelola", "動詞", "kelola", "運営する、管理する、切り盛りする", "Ia mengelola warung dengan sangat rapi."),
            ("lusuh", "形容詞", "-", "擦り切れた、色褪せた、使い古された", "Uang kertas lusuh itu tetap diterima."),
            ("uang receh", "名詞句", "receh", "小銭、端数の小額通貨", "Kasir kekurangan uang receh untuk kembalian."),
            ("terpampang", "動詞（状態）", "pampang", "（目立つように）掲げられている", "Poster besar terpampang di dinding stasiun."),
            ("waswas", "形容詞", "-", "不安な、気がかりな、疑心暗鬼の", "Ibu merasa waswas menunggu anaknya pulang."),
            ("hasil keringat", "慣用表現", "keringat", "汗水流した結晶、苦労して得た対価", "Rumah ini dibangun dari hasil keringat sendiri."),
            ("sirna", "動詞・形容詞", "-", "消滅する、すっかり消え失せる", "Kabut pagi sirna disinari matahari."),
            ("inklusi finansial", "名詞句", "-", "金融包摂（誰もが金融サービスを受けられること）", "QRIS mendorong inklusi finansial masyarakat desa."),
            ("bersaing", "動詞", "saing", "競争する、競い合う", "Produk lokal harus mampu bersaing di pasar global."),
            ("pedagang mikro", "名詞句", "dagang", "零細商人、小規模事業者", "Pemerintah memberikan subsidi untuk pedagang mikro.")
        ],
        "grammar_points": """1. **時の起点と変化を表す接続詞 `sejak ...`（〜以来）**:
   - 状態の変化の転換点を明示する接続詞です。
   - 例: *Sejak cucunya mendaftarkan QRIS, transaksi menjadi mudah.*（孫がQRISを登録して以来、取引が容易になった。）
2. **転換・逆接を表す複合接続詞 `Akan tetapi ...`（しかしながら）**:
   - 形式ばった文脈や論理的文章で前述の懸念を覆す際に多用されます。
   - 例: *Awalnya sulit. Akan tetapi, lama-lama terbiasa.*（最初は難しかった。しかしながら、次第に慣れた。）
3. **範囲の広がりを表す相関表現 `mulai dari... hingga...`（〜から〜に至るまで）**:
   - 多様な主体の包括を表します。
   - 例: *Mulai dari anak-anak hingga orang dewasa.*（子供から大人に至るまで。）""",
        "quizzes": [
            ("シティおばさんが現金決済の時代に最も頻繁に困っていた問題は何ですか？",
             ["品物の賞味期限切れ", "釣り銭用の小銭（uang receh）の不足と夜間の偽札リスク", "店舗の家賃の値上げ"],
             "釣り銭用の小銭（uang receh）の不足と夜間の偽札リスク",
             "第1段落に「...kekurangan uang receh untuk kembalian pembeli, atau risiko menerima uang palsu...」とあります。"),
            ("QRISを導入する前、シティおばさんが最も抱いていた不安（waswas）は何ですか？",
             ["スマホが熱を持って壊れること", "売上金が口座に入らないことやサイバー犯罪で残高が失われること", "近所の人に自慢していると思われること"],
             "売上金が口座に入らないことやサイバー犯罪で残高が失われること",
             "第3段落に「Ia khawatir uang hasil keringatnya tidak masuk ke rekening atau saldo tabungannya hilang karena kejahatan siber.」とあります。"),
            ("QRISやデジタルウォレットの普及がインドネシア社会にもたらした大きな好影響は何ですか？",
             ["社会の最末端層にまで金融包摂（inklusi finansial）が加速したこと", "紙幣の印刷が法律で完全に禁止されたこと", "すべての露店がショッピングモールに移転したこと"],
             "社会の最末端層にまで金融包摂（inklusi finansial）が加速したこと",
             "第4段落に「Kehadiran dompet digital dan sistem QRIS telah mempercepat inklusi finansial hingga ke lapisan masyarakat terbawah.」とあります。")
        ],
        "culture": """### インドネシア中央銀行のメガヒット「QRIS（クリス）」
QRIS（Quick Response Code Indonesian Standard）は、インドネシア中央銀行（Bank Indonesia）が2019年に制定した国内統一QRコード決済規格です。
それまで各社（GoPay, OVO, Dana, ShopeePay, 各銀行）バラバラだったQRコードを1つに統合し、消費者はどの決済アプリからでも同じQRコードをスキャンして支払うことができます。
下町の屋台（Warung）や露店（Kaki lima）でも手数料が非常に安く（または無料）導入できるため、国民的なキャッシュレス化と「金融包摂（Inklusi Finansial）」の世界的成功モデルとなっています。"""
    },
    {
        "id": "1223",
        "slug": "level-3-03-mudik-homecoming-journey",
        "title": "【Level 3 (B1)】Perjalanan Mudik Lebaran Menembus Kemacetan（年に一度の帰省ラッシュの感動）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "ラマダン明けの国民的一大イベント「ムディック（Mudik）」。家族全員で乗り越える長距離ドライブ、高速道路の渋滞、そして故郷で交わす許しと再会の感動を描く。",
        "text": """Bagi masyarakat Indonesia, Lebaran bukan sekadar perayaan keagamaan biasa, melainkan momentum suci untuk menyucikan hati dan merajut kembali tali persaudaraan. Tradisi pulang kampung tahunan, atau yang lebih dikenal dengan istilah mudik, menjadi peristiwa akbar yang melibatkan puluhan juta orang yang bergerak serentak dari kota-kota besar menuju kampung halaman mereka.

Tahun ini, keluarga Pak Bambang memutuskan untuk mudik ke Solo menggunakan mobil pribadi melalui Jalan Tol Trans-Jawa. Sejak dua minggu sebelumnya, Pak Bambang telah mempersiapkan segala sesuatunya secara cermat, mulai dari servis mesin kendaraan, memastikan saldo kartu tol elektronik mencukupi, hingga membungkus oleh-oleh khas Jakarta untuk para kerabat di kampung.

Perjalanan yang biasanya memakan waktu sekitar delapan jam berubah menjadi ujian kesabaran yang sesungguhnya. Di beberapa titik rest area, antrean kendaraan mengular panjang hingga beberapa kilometer. Namun, di tengah kelelahan akibat kemacetan berjam-jam, suasana kebersamaan justru terasa begitu kental. Di dalam mobil, anak-anak bernyanyi gembira ditemani bekal ketupat dan rendang buatan sang ibu.

Ketika mobil akhirnya memasuki gapura desa saat azan magrib berkumandang, rasa letih seketika sirna. Kakek dan nenek sudah berdiri menanti di teras rumah dengan mata berbinar-binar penuh kerinduan. Tradisi sungkeman, yaitu bersujud memohon maaf lahir dan batin kepada orang tua, menjadi puncak keharuan yang mengingatkan setiap insan akan makna sejati dari sebuah keluarga.""",
        "paragraphs": [
            ("Bagi masyarakat Indonesia, Lebaran bukan sekadar perayaan keagamaan biasa, melainkan momentum suci untuk menyucikan hati dan merajut kembali tali persaudaraan. Tradisi pulang kampung tahunan, atau yang lebih dikenal dengan istilah mudik, menjadi peristiwa akbar yang melibatkan puluhan juta orang yang bergerak serentak dari kota-kota besar menuju kampung halaman mereka.",
             "インドネシアの人々にとって、レバラン（断食明け大祭）は単なる通常の宗教的祝祭にとどまらず、心を清め、血縁の絆を再び結び直すための神聖な好機です。「ムディック（mudik）」という言葉で親しまれている年に一度の帰省の伝統は、大都市から故郷へと何千万人もの人々が一斉に大移動する一大行事となります。",
             "momentum suci（神聖な好機）、merajut tali persaudaraan（血縁の絆を結び直す）、bergerak serentak（一斉に行動する・大移動する）。"),
            ("Tahun ini, keluarga Pak Bambang memutuskan untuk mudik ke Solo menggunakan mobil pribadi melalui Jalan Tol Trans-Jawa. Sejak dua minggu sebelumnya, Pak Bambang telah mempersiapkan segala sesuatunya secara cermat, mulai dari servis mesin kendaraan, memastikan saldo kartu tol elektronik mencukupi, hingga membungkus oleh-oleh khas Jakarta untuk para kerabat di kampung.",
             "今年、バンバンさん一家はトランス・ジャワ高速道路を通って自家用車で中ジャワ州ソロへ帰省することを決めました。2週間前からバンバンさんは、車のエンジン点検、電子高速道路カード（E-toll）の残高の十分なチャージ、田舎の親戚のためのジャカルタ名物のお土産の梱包に至るまで、あらゆる準備を入念に進めていました。",
             "Jalan Tol Trans-Jawa（ジャワ縦断高速道路）、secara cermat（入念に・入念に）、mencukupi（十分である）、oleh-oleh khas（特産のお土産）。"),
            ("Perjalanan yang biasanya memakan waktu sekitar delapan jam berubah menjadi ujian kesabaran yang sesungguhnya. Di beberapa titik rest area, antrean kendaraan mengular panjang hingga beberapa kilometer. Namun, di tengah kelelahan akibat kemacetan berjam-jam, suasana kebersamaan justru terasa begitu kental. Di dalam mobil, anak-anak bernyanyi gembira ditemani bekal ketupat dan rendang buatan sang ibu.",
             "通常は約8時間しかかからない道中が、真の忍耐の試練へと変貌しました。いくつかのサービスエリアでは、車の列が数キロメートルにわたってヘビのように長く連なりました。しかし、何時間にも及ぶ渋滞による疲労のただ中にあって、家族の一体感の雰囲気はかえって非常に色濃く感じられました。車内では、母親が作ったクトゥパット（ちまき）とルンダンのお弁当をつまみながら、子供たちが楽しそうに歌を歌っていました。",
             "ujian kesabaran（忍耐の試練）、mengular panjang（ヘビのように長く延びる）、suasana kebersamaan（家族の一体感・連帯感）。"),
            ("Ketika mobil akhirnya memasuki gapura desa saat azan magrib berkumandang, rasa letih seketika sirna. Kakek dan nenek sudah berdiri menanti di teras rumah dengan mata berbinar-binar penuh kerinduan. Tradisi sungkeman, yaitu bersujud memohon maaf lahir dan batin kepada orang tua, menjadi puncak keharuan yang mengingatkan setiap insan akan makna sejati dari sebuah keluarga.",
             "日没のマグリブのアザーンが響き渡る中、車がついに村の入口の門をくぐったとき、疲労感は一瞬にして消え去りました。祖父と祖母は、あふれんばかりの恋しさに満ちた目を輝かせながら、家のテラスに立って待っていました。両親の前に跪いて心からの許し（Mohon Maaf Lahir dan Batin）を請う「スンクマン（sungkeman）」の伝統儀礼は、家族の真の意味をすべての人に思い起こさせる感動のクライマックスとなりました。",
             "gapura desa（村の表門）、mata berbinar-binar（瞳を輝かせる）、sungkeman（両親に跪いて許しを請う伝統作法）、puncak keharuan（感動の頂点）。")
        ],
        "vocab": [
            ("merajut", "動詞", "rajut", "編む、紡ぐ、再び結び直す", "Pertemuan ini merajut kembali persahabatan lama."),
            ("serentak", "副詞", "rentak", "一斉に、同時に、足並みをそろえて", "Para siswa menjawab salam secara serentak."),
            ("cermat", "形容詞", "-", "入念な、綿密な、几帳面な", "Ia meneliti laporan itu dengan sangat cermat."),
            ("mengular", "動詞", "ular", "ヘビのように長くうねって連なる", "Antrean tiket konser mengular hingga luar gedung."),
            ("kental", "形容詞", "-", "濃い、（関係や雰囲気が）親密な・濃厚な", "Hubungan kekeluargaan mereka sangat kental."),
            ("bekal", "名詞", "-", "弁当、旅の準備金・糧", "Ibu menyiapkan bekal nasi bungkus untuk perjalanan."),
            ("gapura", "名詞", "-", "門、アーチ状の入口", "Gapura selamat datang menyambut para pemudik."),
            ("berbinar-binar", "形容詞・動詞", "binar", "（瞳や表情が）喜びに輝く", "Matanya berbinar-binar melihat kado ulang tahun."),
            ("sungkeman", "名詞", "sungkem", "目上の人の膝に額をつけて敬意と許しを請う儀礼", "Acara sungkeman diwarnai isak tangis haru."),
            ("keharuan", "名詞", "haru", "感動、胸がいっぱいになる情景", "Keharuan menyelimuti pertemuan keluarga tersebut.")
        ],
        "grammar_points": """1. **使役・強調を表す動詞接尾辞 `-kan`（例: `menyatukan`, `mengingatkan`）**:
   - 語根 *ingat*（覚えている）+ *meng- -kan* = *mengingatkan*（思い出させる、思い起こさせる）。
   - 例: *Kisah ini mengingatkan kita akan kampung halaman.*（この物語は私たちに故郷を思い起こさせる。）
2. **対比・逆強調の副詞 `justru`（むしろ、かえって）**:
   - 予想とは反対にポジティブな感情や状況が際立つ際に使われます。
   - 例: *Di tengah kesulitan, mereka justru semakin kompak.*（困難の中で、彼らはかえって結束を深めた。）
3. **分詞的形容詞接頭辞 `ber-` の反復強調（`berbinar-binar`, `berjam-jam`）**:
   - *berjam-jam* = 何時間もにわたって
   - *berbinar-binar* = キラキラと輝き続けている""",
        "quizzes": [
            ("インドネシアのレバラン（断食明け大祭）における「ムディック（mudik）」の本質的な意義は何ですか？",
             ["海外旅行の割引セールを楽しむこと", "心を清め、家族・親族の絆を再び結び直すこと", "都会のオフィスに泊まり込んで仕事をすること"],
             "心を清め、家族・親族の絆を再び結び直すこと",
             "第1段落に「...momentum suci untuk menyucikan hati dan merajut kembali tali persaudaraan.」とあります。"),
            ("バンバンさんの家族が渋滞の車内で長い時間過ごす中で、家族の雰囲気が温かくなった理由は何ですか？",
             ["車内で母親特製のクトゥパットやルンダンを食べながら子供たちが歌い、一体感を感じたため", "スマホのゲームを無言でやり続けたため", "途中で車を乗り捨てて歩いたため"],
             "車内で母親特製のクトゥパットやルンダンを食べながら子供たちが歌い、一体感を感じたため",
             "第3段落に「...suasana kebersamaan justru terasa begitu kental. Di dalam mobil, anak-anak bernyanyi gembira ditemani bekal ketupat dan rendang...」とあります。"),
            ("故郷に到着した際に行われる、両親に跪いてこれまでの過ちの許しを請う伝統儀礼を何と呼びますか？",
             ["ハラール・ビ・ハラール（Halal Bihalal）", "スンクマン（Sungkeman）", "ゴトン・ロヨン（Gotong Royong）"],
             "スンクマン（Sungkeman）",
             "第4段落に「Tradisi sungkeman, yaitu bersujud memohon maaf lahir dan batin kepada orang tua...」とあります。")
        ],
        "culture": """### 世界最大級の民族大移動「Mudik（ムディック）」と「Sungkeman」
「Mudik」はジャワ語の「mulih dhisik（先に帰る）」またはマレー語の「menuju udik（上流・田舎へ向かう）」が語源とされます。
ラマダン（断食月）が終わるレバランの時期には、ジャカルタをはじめとする大都市から推定3,000万人以上が一斉に故郷へ大移動します。
実家に到着すると、最年長の両親の前に子どもたちが順番に正座・平伏して手を取り、「Mohon maaf lahir dan batin（現世と内面のすべての過ちをお許しください）」と言葉を交わす「Sungkeman（スンクマン）」が行われ、涙と笑顔で新たな一年を迎えます。"""
    },
    {
        "id": "1224",
        "slug": "level-3-04-coffee-culture-boom",
        "title": "【Level 3 (B1)】Gaya Hidup Kedai Kopi Anak Muda（若者のサードウェーブコーヒーとコワーキング文化）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "パームシュガー入りミルクコーヒー（Kopi Susu Gula Aren）のブームから始まった都市部のカフェ文化。若者のクリエイティブな働き方と国産スペシャリティコーヒーへの誇りを描く。",
        "text": """Dalam satu dekade terakhir, lanskap gaya hidup generasi muda di kota-kota besar Indonesia mengalami pergeseran yang sangat mencolok. Kedai kopi modern, atau yang akrab disebut kafe kekinian, tumbuh menjamur di setiap sudut jalan. Fenomena ini bukan semata-mata didorong oleh kebutuhan akan kafein, melainkan telah menjelma menjadi ruang sosial ketiga tempat gagasan-gagasan kreatif lahir dan berkembang biak.

Pemicu utama ledakan industri ini adalah popularitas kopi susu gula aren. Perpaduan harmonis antara seduhan kopi espresso yang pekat, susu segar yang gurih, dan manisnya sirup nira kelapa lokal berhasil memikat lidah masyarakat luas yang sebelumnya menganggap kopi sebagai minuman pahit khusus orang tua. Inovasi sederhana ini membuktikan bahwa cita rasa tradisional mampu bertransformasi menjadi produk bernilai ekonomi tinggi.

Bagi kaum muda urban, kedai kopi kini berfungsi ganda sebagai kantor alternatif untuk bekerja dari mana saja atau work from cafe. Dengan fasilitas internet berkecepatan tinggi, stopkontak di setiap meja, dan alunan musik santai, para pekerja lepas, pembuat konten digital, dan mahasiswa dapat menghabiskan waktu berjam-jam menyelesaikan proyek kolaboratif mereka. Suasana terbuka ini memicu lahirnya komunitas-komunitas kreatif yang saling menginspirasi.

Lebih dari sekadar tren gaya hidup sesaat, fenomena ini turut mengangkat harkat dan martabat para petani kopi lokal. Dari dataran tinggi Gayo di Aceh, lereng Gunung Ijen di Jawa Timur, hingga perbukitan Toraja di Sulawesi, biji kopi arabika nusantara kini dihargai sangat mahal di pasar domestik maupun internasional. Generasi muda bangga menyesap kopi asli negeri sendiri yang diproses secara etis dan berkelanjutan.""",
        "paragraphs": [
            ("Dalam satu dekade terakhir, lanskap gaya hidup generasi muda di kota-kota besar Indonesia mengalami pergeseran yang sangat mencolok. Kedai kopi modern, atau yang akrab disebut kafe kekinian, tumbuh menjamur di setiap sudut jalan. Fenomena ini bukan semata-mata didorong oleh kebutuhan akan kafein, melainkan telah menjelma menjadi ruang sosial ketiga tempat gagasan-gagasan kreatif lahir dan berkembang biak.",
             "過去10年間で、インドネシアの大都市における若者世代のライフスタイルの景観は非常に目覚ましい変遷を遂げました。親しみを込めて「最旬カフェ（kafe kekinian）」と呼ばれるモダンなコーヒーショップが、街の至る所に雨後の筍のように急増しました。この現象は単にカフェインへの欲求に後押しされただけでなく、クリエイティブな発想が生まれ育つ「第3のソーシャルスペース」へと変貌を遂げたのです。",
             "pergeseran mencolok（目覚ましい変遷・シフト）、tumbuh menjamur（雨後の筍のように急増する）、menjelma（姿を変える・変貌する）、ruang sosial ketiga（サードプレイス）。"),
            ("Pemicu utama ledakan industri ini adalah popularitas kopi susu gula aren. Perpaduan harmonis antara seduhan kopi espresso yang pekat, susu segar yang gurih, dan manisnya sirup nira kelapa lokal berhasil memikat lidah masyarakat luas yang sebelumnya menganggap kopi sebagai minuman pahit khusus orang tua. Inovasi sederhana ini membuktikan bahwa cita rasa tradisional mampu bertransformasi menjadi produk bernilai ekonomi tinggi.",
             "この業界の爆発的成長の主たる引き金となったのは、「パームシュガー入りミルクコーヒー（kopi susu gula aren）」の人気でした。濃厚なエスプレッソ抽出液、コクのある新鮮な牛乳、そして地元産ヤシ花糖シロップの甘さの調和のとれた融合は、かつてコーヒーを「年配者向けの苦い飲み物」とみなしていた幅広い大衆の舌を魅了することに成功しました。このシンプルな革新は、伝統的な風味が経済的価値の高い商品へと変貌できることを証明したのです。",
             "pemicu utama（主たる引き金）、seduhan pekat（濃厚な抽出液）、gula aren（パームシュガー・ヤシ花糖）、memikat lidah（舌を魅了する）。"),
            ("Bagi kaum muda urban, kedai kopi kini berfungsi ganda sebagai kantor alternatif untuk bekerja dari mana saja atau work from cafe. Dengan fasilitas internet berkecepatan tinggi, stopkontak di setiap meja, dan alunan musik santai, para pekerja lepas, pembuat konten digital, dan mahasiswa dapat menghabiskan waktu berjam-jam menyelesaikan proyek kolaboratif mereka. Suasana terbuka ini memicu lahirnya komunitas-komunitas kreatif yang saling menginspirasi.",
             "都会の若者たちにとって、カフェは今や「カフェで働く（WFC: work from cafe）」ための代替オフィスとして二重の機能を果たしています。高速インターネット設備、すべてのテーブルにある電源コンセント、そして心地よい音楽の調べによって、フリーランサー、デジタルコンテンツ制作者、大学生たちが何時間も過ごしながら共同プロジェクトを完遂することができます。このオープンな空間が、互いに刺激を与え合うクリエイティブ・コミュニティの誕生を促しています。",
             "berfungsi ganda（二重の機能を果たす）、stopkontak（電源コンセント）、pekerja lepas（フリーランサー）、memicu lahirnya（〜の誕生を促す）。"),
            ("Lebih dari sekadar tren gaya hidup sesaat, fenomena ini turut mengangkat harkat dan martabat para petani kopi lokal. Dari dataran tinggi Gayo di Aceh, lereng Gunung Ijen di Jawa Timur, hingga perbukitan Toraja di Sulawesi, biji kopi arabika nusantara kini dihargai sangat mahal di pasar domestik maupun internasional. Generasi muda bangga menyesap kopi asli negeri sendiri yang diproses secara etis dan berkelanjutan.",
             "単なる一過性のライフスタイルトレンドにとどまらず、この現象は地元コーヒー農家の尊厳と地位の向上にも貢献しています。アチェ州ガヨ高地、東ジャワ州イジェン山麓、スラウェシ州トラジャの丘陵地帯に至るまで、列島産のアラビカコーヒー豆は今や国内のみならず国際市場でも極めて高く評価されています。若者世代は、倫理的かつ持続可能な方法で精製された自国の本物のコーヒーを味わうことに誇りを持っています。",
             "tren sesaat（一過性の流行）、mengangkat harkat dan martabat（地位と尊厳を高める）、menyesap kopi（コーヒーをすする・味わう）、berkelanjutan（持続可能な・サステナブルな）。")
        ],
        "vocab": [
            ("menjamur", "動詞", "jamur", "雨後の筍のように急増する、急拡大する", "Kafe baru menjamur di kawasan kampus."),
            ("menjelma", "動詞", "jelma", "変貌する、化身する、生まれ変わる", "Gudang tua itu menjelma menjadi galeri seni."),
            ("pemicu", "名詞", "picu", "引き金、誘因、火付け役", "Inovasi rasa menjadi pemicu kesuksesan produk."),
            ("memikat", "動詞", "pikat", "魅了する、引きつける、虜にする", "Pemandangan danau memikat para wisatawan."),
            ("gula aren", "名詞句", "aren", "ヤシ花糖、パームシュガー（赤砂糖）", "Kopi dicampur gula aren cair terasa legit."),
            ("berfungsi ganda", "動詞句", "fungsi", "二重の役割を果たす", "Alat ini berfungsi ganda sebagai pemotong dan pembuka."),
            ("pekerja lepas", "名詞句", "lepas", "フリーランサー、自由契約労働者", "Banyak pekerja lepas bekerja di kedai kopi."),
            ("harkat dan martabat", "連語名詞", "-", "尊厳と品格、社会的地位", "Pendidikan mengangkat harkat dan martabat keluarga."),
            ("menyesap", "動詞", "sesap", "すする、ちびちび味わって飲む", "Ia menyesap kopi hangat di teras."),
            ("berkelanjutan", "形容詞", "lanjut", "持続可能な、継続的な（サステナブル）", "Pertanian ramah lingkungan harus berkelanjutan.")
        ],
        "grammar_points": """1. **接頭辞 `me-` による名詞からの動詞化（比喩表現）**:
   - *jamur*（キノコ）→ *menjamur*（キノコのように急増する）
   - *jelma*（化身）→ *menjelma*（姿を変える、変貌する）
2. **多機能接頭辞 `se-` による限定・副詞化 `semata-mata`（ただ〜だけ）**:
   - *bukan semata-mata... melainkan...*（ただ単に〜だけではなく、むしろ〜である）
3. **並列・強調を表す接続詞 `maupun`（〜もまた）**:
   - *baik A maupun B*、または *di pasar domestik maupun internasional*（国内市場においても国際市場においても）""",
        "quizzes": [
            ("インドネシアの若者の間で空前のカフェブームの火付け役（pemicu utama）となった飲み物は何ですか？",
             ["輸入された高級抹茶ラテ", "パームシュガー入りミルクコーヒー（kopi susu gula aren）", "炭酸入りエナジードリンク"],
             "パームシュガー入りミルクコーヒー（kopi susu gula aren）",
             "第2段落に「Pemicu utama ledakan industri ini adalah popularitas kopi susu gula aren.」とあります。"),
            ("若者たちにとって、現代のカフェが果たすもう一つの重要な機能（berfungsi ganda）は何ですか？",
             ["仕事や共同作業を行うための代替オフィス（work from cafe）", "深夜のダンスクラブ会場", "伝統的な昼寝の休憩所"],
             "仕事や共同作業を行うための代替オフィス（work from cafe）",
             "第3段落に「...kedai kopi kini berfungsi ganda sebagai kantor alternatif untuk bekerja dari mana saja atau work from cafe.」とあります。"),
            ("カフェブームがインドネシアの地方社会や農業にもたらしたプラスの影響は何ですか？",
             ["ガヨ、イジェン、トラジャなどの地元コーヒー農家の地位と生豆の価値が向上したこと", "すべての農地が宅地として売却されたこと", "農民が全員都会に移住したこと"],
             "ガヨ、イジェン、トラジャなどの地元コーヒー農家の地位と生豆の価値が向上したこと",
             "第4段落に「...fenomena ini turut mengangkat harkat dan martabat para petani kopi lokal.」とあります。")
        ],
        "culture": """### 「Kopi Susu Gula Aren」と第3の空間（Third Place）
インドネシアはブラジル、ベトナム、コロンビアに次ぐ世界第4位のコーヒー生産国です。
かつては粉ごとグラスに入れて上澄みをすする「Kopi Tubruk（コピ・トゥブルック）」が主流でしたが、2015年頃からエスプレッソに濃厚なミルクと赤ヤシ砂糖（Gula Aren）を加えた「Es Kopi Susu」が爆発的ヒットとなりました（Kopi KenanganやJanji Jiwaなど）。
現在では「WFC（Work From Cafe）」が完全に定着し、クリエイティブ産業を支えるインフラとなっています。"""
    },
    {
        "id": "1225",
        "slug": "level-3-05-coral-reef-conservation",
        "title": "【Level 3 (B1)】Menjaga Terumbu Karang di Bunaken（ブナケンのサンゴ礁を守る地元ダイバーの挑戦）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "北スラウェシ州ブナケン海洋国立公園。地球温暖化による白化現象とプラスチックごみに立ち向かい、人工サンゴ礁で海を蘇らせる地元青年ダイバーの海洋環境物語。",
        "text": """Taman Nasional Bunaken di Sulawesi Utara telah lama termasyhur ke seantero bumi sebagai surga keanekaragaman hayati bawah laut. Dinding karang vertikal yang spektakuler, terumbu karang warna-warni, serta ribuan spesies ikan tropis menjadi magnet yang memikat para penyelam mancanegara. Namun, di balik keindahan yang memesona itu, tersimpan ancaman nyata yang mengintai kelestarian ekosistem laut ini.

Rian, seorang pemuda lokal keturunan suku Bajo, mendedikasikan hidupnya untuk menyelamatkan laut leluhurnya. Dalam beberapa tahun terakhir, ia menyaksikan sendiri bagaimana pemanasan suhu permukaan air laut menyebabkan pemutihan karang secara massal. Karang-karang yang semula berwarna cerah berubah menjadi putih pucat menyerupai kerangka sebelum akhirnya mati membusuk dan ditumbuhi lumut beracun. Belum lagi masalah sampah plastik kiriman yang terbawa arus dari perkotaan.

Menolak untuk tinggal diam, Rian bersama komunitas penyelam lokal memprakarsai proyek restorasi terumbu karang buatan menggunakan metode biorock dan substrat jaring laba-laba. Setiap akhir pekan, mereka menyelam ke kedalaman dua puluh meter untuk menanam bibit-bibit karang baru pada rangka besi yang dialiri arus listrik bertenaga surya berkekuatan sangat rendah. Arus listrik ini mempercepat pengendapan mineral kalsium karbonat sehingga karang dapat tumbuh tiga hingga lima kali lebih cepat dibanding di alam liar.

Usaha gigih mereka yang berlangsung tanpa pamrih mulai membuahkan hasil nyata. Area bawah laut yang dulunya tandus dan mati kini kembali dipenuhi oleh tunas-tunas karang yang rimbun dan dikerumuni oleh penyu sisik serta kawanan ikan badut. Bagi Rian, menjaga kesehatan laut bukan hanya soal melestarikan panorama pariwisata, melainkan menjaga denyut kehidupan generasi mendatang yang bergantung penuh pada kemurahan alam bahari.""",
        "paragraphs": [
            ("Taman Nasional Bunaken di Sulawesi Utara telah lama termasyhur ke seantero bumi sebagai surga keanekaragaman hayati bawah laut. Dinding karang vertikal yang spektakuler, terumbu karang warna-warni, serta ribuan spesies ikan tropis menjadi magnet yang memikat para penyelam mancanegara. Namun, di balik keindahan yang memesona itu, tersimpan ancaman nyata yang mengintai kelestarian ekosistem laut ini.",
             "北スラウェシ州のブナケン国立公園は、海洋生物多様性の天国として古くから地球全体に名を轟かせてきました。目を見張るような垂直のサンゴ壁（ドロップオフ）、色とりどりのサンゴ礁、そして何千種もの熱帯魚が、外国人ダイバーを惹きつける磁石となっています。しかし、その魅惑的な美しさの裏には、この海洋生態系の持続可能性を脅かす現実の危機が潜んでいます。",
             "termasyhur ke seantero bumi（全世界に名を轟かせる）、keanekaragaman hayati（生物多様性）、mengintai（潜んで狙う・脅かす）、kelestarian ekosistem（生態系の持続可能性）。"),
            ("Rian, seorang pemuda lokal keturunan suku Bajo, mendedikasikan hidupnya untuk menyelamatkan laut leluhurnya. Dalam beberapa tahun terakhir, ia menyaksikan sendiri bagaimana pemanasan suhu permukaan air laut menyebabkan pemutihan karang secara massal. Karang-karang yang semula berwarna cerah berubah menjadi putih pucat menyerupai kerangka sebelum akhirnya mati membusuk dan ditumbuhi lumut beracun. Belum lagi masalah sampah plastik kiriman yang terbawa arus dari perkotaan.",
             "バジョ族の血を引く地元の青年リアンは、先祖代々の海を救うために自らの人生を捧げています。ここ数年、彼は海水表面温度の上昇がいかにサンゴの大規模な白化現象を引き起こしているかを自らの目で目撃してきました。元は鮮やかな色彩を誇っていたサンゴたちが、最終的に腐敗して死に、有害な藻類に覆われる前に、まるで骨格のような青白い姿へと変貌していきました。さらには、都市部から海流に乗って漂着するプラスチックごみの問題もあります。",
             "suku Bajo（海の民バジョ族）、pemutihan karang（サンゴの白化）、putih pucat（青白い・青ざめた）、sampah plastik kiriman（漂着プラスチックごみ）。"),
            ("Menolak untuk tinggal diam, Rian bersama komunitas penyelam lokal memprakarsai proyek restorasi terumbu karang buatan menggunakan metode biorock dan substrat jaring laba-laba. Setiap akhir pekan, mereka menyelam ke kedalaman dua puluh meter untuk menanam bibit-bibit karang baru pada rangka besi yang dialiri arus listrik bertenaga surya berkekuatan sangat rendah. Arus listrik ini mempercepat pengendapan mineral kalsium karbonat sehingga karang dapat tumbuh tiga hingga lima kali lebih cepat dibanding di alam liar.",
             "黙って手をこまねいていることを拒絶したリアンは、地元のダイバーコミュニティとともに、バイオロック工法とクモの巣状基盤を用いた人工サンゴ礁修復プロジェクトを発足させました。毎週末、彼らは水深20メートルの海底へと潜り、極めて微弱な太陽光発電による電流が通された鉄骨フレームに新しいサンゴの幼生を移植します。この電流は炭酸カルシウム鉱物の沈殿を促進し、その結果サンゴは自然界に比べて3倍から5倍のスピードで成長できるのです。",
             "tinggal diam（何もしないで放置する）、memprakarsai（創始する・発起する）、restorasi（修復・復元）、pengendapan mineral（鉱物の沈殿）。"),
            ("Usaha gigih mereka yang berlangsung tanpa pamrih mulai membuahkan hasil nyata. Area bawah laut yang dulunya tandus dan mati kini kembali dipenuhi oleh tunas-tunas karang yang rimbun dan dikerumuni oleh penyu sisik serta kawanan ikan badut. Bagi Rian, menjaga kesehatan laut bukan hanya soal melestarikan panorama pariwisata, melainkan menjaga denyut kehidupan generasi mendatang yang bergantung penuh pada kemurahan alam bahari.",
             "見返りを求めずに続けられた彼らの不屈の努力は、確かな実を結び始めました。かつて不毛で死に絶えていた海底エリアは今や、青々と茂るサンゴの新芽で再び満たされ、タイマイ（ウミガメ）やカクレクマノミの群れでごった返すようになりました。リアンにとって、海の健康を守ることは単に観光パノラマを維持することではなく、豊かな海洋の恵みに全面的に依存している未来の世代の生命の鼓動を守ることなのです。",
             "tanpa pamrih（見返りを求めない・私心のない）、membuahkan hasil（成果を結実させる）、tandus（不毛な・荒廃した）、kemurahan alam bahari（海洋の豊かな恵み）。")
        ],
        "vocab": [
            ("keanekaragaman hayati", "名詞句", "-", "生物多様性（バイオダイバーシティ）", "Hutan hujan kaya akan keanekaragaman hayati."),
            ("mengintai", "動詞", "intai", "（危険や敵が）潜んで窺う、脅かす", "Bahaya tanah longsor mengintai warga lereng."),
            ("mendedikasikan", "動詞", "dedikasi", "捧げる、献身する", "Dokter mendedikasikan ilmunya untuk warga miskin."),
            ("pemutihan karang", "名詞句", "putih", "サンゴの白化（水温上昇による共生藻類の喪失）", "Pemanasan global memicu pemutihan karang."),
            ("pucat", "形容詞", "-", "青白い、青ざめた、血色のない", "Wajahnya tampak pucat karena sakit."),
            ("memprakarsai", "動詞", "prakarsa", "発起する、創始する、主導する", "Pemuda desa memprakarsai bank sampah."),
            ("restorasi", "名詞", "-", "復元、再生、修復", "Restorasi terumbu karang butuh waktu bertahun-tahun."),
            ("pengendapan", "名詞", "endap", "沈殿、堆積作用", "Pengendapan lumpur menyebabkan sungai dangkal."),
            ("tanpa pamrih", "副詞句", "pamrih", "私心なく、見返りを求めずに", "Relawan bekerja tanpa pamrih menolong korban."),
            ("tandus", "形容詞", "-", "不毛な、草木の生えない、荒れ果てた", "Tanah tandus disulap menjadi kebun hijau.")
        ],
        "grammar_points": """1. **原因・結果の複文接続詞 `sehingga`（その結果〜）**:
   - 従属節に結果を導く最も標準的な接続詞です。
   - 例: *Arus listrik mempercepat pengendapan mineral sehingga karang tumbuh cepat.*（電流が鉱物沈殿を加速し、その結果サンゴが急速に成長する。）
2. **否定＋目的の副詞表現 `Menolak untuk ...`（〜することを拒否して）**:
   - 主体の強い意志を表す導入句です。
   - 例: *Menolak untuk menyerah, ia terus berjuang.*（諦めることを拒否して、彼は戦い続けた。）
3. **被覆・受身を表す接周辞 `di- -i`（例: `ditumbuhi`）**:
   - 語根 *tumbuh*（育つ・生える）+ *di- -i* = *ditumbuhi lumut*（コケに覆い生い茂られる）。""",
        "quizzes": [
            ("ブナケン国立公園の美しいサンゴ礁が現在直面している最大の自然環境的危機は何ですか？",
             ["海水温度の上昇による大規模なサンゴの白化現象（pemutihan karang）", "大型豪華客船の沈没事故", "火山灰の大量降下"],
             "海水温度の上昇による大規模なサンゴの白化現象（pemutihan karang）",
             "第2段落に「...pemanasan suhu permukaan air laut menyebabkan pemutihan karang secara massal.」とあります。"),
            ("リアンたちが行っている「バイオロック（biorock）」工法では、なぜサンゴの成長が3〜5倍速くなるのですか？",
             ["化学薬品の肥料を大量に撒いているため", "太陽光発電による微弱な電流を流し、炭酸カルシウム鉱物の沈殿を促すため", "24時間強力なLED照明で照らし続けているため"],
             "太陽光発電による微弱な電流を流し、炭酸カルシウム鉱物の沈殿を促すため",
             "第3段落に「Arus listrik ini mempercepat pengendapan mineral kalsium karbonat sehingga karang dapat tumbuh tiga hingga lima kali lebih cepat...」とあります。"),
            ("リアンにとって、海のサンゴ礁を守る活動の究極の意義は何ですか？",
             ["外国人ダイバーから高額なガイド料金をもらうこと", "海洋の恵みに依存する未来の世代の命の鼓動を守ること", "SNSで多くのフォロワーを獲得すること"],
             "海洋の恵みに依存する未来の世代の命の鼓動を守ること",
             "第4段落に「...menjaga denyut kehidupan generasi mendatang yang bergantung penuh pada kemurahan alam bahari.」とあります。")
        ],
        "culture": """### 海洋保護区の至宝「ブナケン」と海の民「Orang Bajo」
スラウェシ島マナド沖に浮かぶ「ブナケン国立公園（Taman Nasional Bunaken）」は、世界のサンゴ種の約7割が生息すると言われるコーラルトライアングルの中心地です。
主人公のルーツである「Suku Bajo（バジョ族）」は、古くから家を持たず船の上で一生を過ごし、水深数十メートルを素潜りして魚を獲る「海の民（Sea Gypsies）」として知られています。
現代では定住化が進んでいますが、彼らの海に対する深い敬畏と生態学的知恵は、先端科学と融合して海洋保全活動の最前線で活かされています。"""
    },
    {
        "id": "1226",
        "slug": "level-3-06-traditional-medicine-jamu",
        "title": "【Level 3 (B1)】Kebangkitan Jamu di Era Modern（ハーブ伝統薬ジャムーのカフェ的リバイバル）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "ユネスコ無形文化遺産に登録されたインドネシアの伝統植物生薬「ジャムー（Jamu）」。行商からスタイリッシュなモダンカフェへの進化とウェルネス価値の再発見を描く。",
        "text": """Sejak berabad-abad silam, nenek moyang bangsa Indonesia telah mewariskan khazanah kearifan lokal berupa jamu, yaitu ramuan obat herbal tradisional yang diracik dari aneka rimpang, daun, kulit kayu, dan rempah-rempah pilihan. Di masa lalu, citra jamu sangat lekat dengan sosok mbok jamu gendong, yaitu wanita paruh baya berkebaya yang berjalan kaki menjajakan botol-botol minuman jamu dalam bakul bambu yang digendong di punggungnya.

Rasa jamu yang identik dengan rasa pahit getir sering kali membuat generasi muda enggan mengonsumsinya. Mereka lebih memilih minuman bersoda atau boba modern yang manis dan trendi. Akibatnya, keberadaan minuman warisan leluhur ini sempat terpinggirkan dan hanya dinikmati oleh kalangan orang tua yang meyakini khasiatnya untuk menjaga kebugaran tubuh serta mengobati berbagai penyakit ringan.

Titik balik kebangkitan jamu terjadi ketika generasi muda terdidik mulai melihat potensi besar jamu dalam industri kebugaran dan gaya hidup sehat global. Dengan sentuhan inovasi kuliner modern, jamu kini disulap menjadi aneka minuman segar yang menggugah selera, seperti kombinasi kunyit asam bersoda, latte temulawak dengan susu gandum, hingga koktail beras kencur dingin. Kedai-kedai jamu modern dengan desain interior minimalis bermunculan di pusat perbelanjaan dan kawasan perkantoran.

Pengakuan resmi dari UNESCO yang menetapkan budaya sehat jamu sebagai Warisan Budaya Takbenda Dunia semakin mempertegas nilai penting tradisi ini. Jamu kini bukan lagi simbol keterbelakangan atau ramuan kuno yang ketinggalan zaman, melainkan kebanggaan identitas bangsa yang berhasil menembus batas waktu berkat kreativitas dan kesadaran hidup sehat masyarakat modern.""",
        "paragraphs": [
            ("Sejak berabad-abad silam, nenek moyang bangsa Indonesia telah mewariskan khazanah kearifan lokal berupa jamu, yaitu ramuan obat herbal tradisional yang diracik dari aneka rimpang, daun, kulit kayu, dan rempah-rempah pilihan. Di masa lalu, citra jamu sangat lekat dengan sosok mbok jamu gendong, yaitu wanita paruh baya berkebaya yang berjalan kaki menjajakan botol-botol minuman jamu dalam bakul bambu yang digendong di punggungnya.",
             "何世紀も昔から、インドネシア民族の祖先は、厳選された様々な根茎、葉、樹皮、スパイスから調合される伝統的な生薬ハーブ飲料である「ジャムー（jamu）」という形の地域知の宝庫を受け継いできました。過去においては、ジャムーのイメージは「ンボッ・ジャムー・ゲンドン（背負いジャムー売りのおばさん）」、すなわち背中に背負った竹籠にジャムーの瓶を何本も入れて徒歩で行商するクバヤ姿の中年女性の姿と強く結びついていました。",
             "khazanah kearifan lokal（地域知の宝庫）、meracik ramuan（生薬を調合する）、mbok jamu gendong（背負いジャムー売りのおばさん）、lekat dengan（〜と密接に結びついている）。"),
            ("Rasa jamu yang identik dengan rasa pahit getir sering kali membuat generasi muda enggan mengonsumsinya. Mereka lebih memilih minuman bersoda atau boba modern yang manis dan trendi. Akibatnya, keberadaan minuman warisan leluhur ini sempat terpinggirkan dan hanya dinikmati oleh kalangan orang tua yang meyakini khasiatnya untuk menjaga kebugaran tubuh serta mengobati berbagai penyakit ringan.",
             "苦くて渋い味と同一視されがちなジャムーの味は、しばしば若者世代が口にすることを敬遠させました。彼らは甘くてトレンディな炭酸飲料や現代的なボバ（タピオカ）ドリンクをより好みました。その結果、この先祖伝来の飲み物の存在は一時隅に追いやられ、体の健康を維持し軽い病気を治す効能を信じる年配者の層によってのみ嗜まれるようになっていました。",
             "pahit getir（苦くて渋い）、enggan mengonsumsi（口にするのを嫌がる・敬遠する）、terpinggirkan（周縁化される・追いやられる）、khasiat（薬効・効能）。"),
            ("Titik balik kebangkitan jamu terjadi ketika generasi muda terdidik mulai melihat potensi besar jamu dalam industri kebugaran dan gaya hidup sehat global. Dengan sentuhan inovasi kuliner modern, jamu kini disulap menjadi aneka minuman segar yang menggugah selera, seperti kombinasi kunyit asam bersoda, latte temulawak dengan susu gandum, hingga koktail beras kencur dingin. Kedai-kedai jamu modern dengan desain interior minimalis bermunculan di pusat perbelanjaan dan kawasan perkantoran.",
             "ジャムー復活の転換点は、高学歴の若者世代が世界のウェルネス産業と健康的なライフスタイルにおけるジャムーの莫大な可能性を見出し始めたときに訪れました。現代の料理イノベーションのタッチにより、ジャムーは今や、炭酸入りクニット・アサム（ウコンとタマリンド）、オーツミルクのテムラワク・ラテ、冷たいブラス・クンチュール・モクテルなど、食欲をそそる多彩な爽快飲料へと魔法のように生まれ変わりました。ミニマリストな内装のモダンなジャムーカフェが、ショッピングモールやオフィス街に次々と誕生しています。",
             "titik balik（転換点・ターニングポイント）、disulap menjadi（〜へ魔法のように変身する）、menggugah selera（食欲・興味をそそる）、bermunculan（次々と現れる）。"),
            ("Pengakuan resmi dari UNESCO yang menetapkan budaya sehat jamu sebagai Warisan Budaya Takbenda Dunia semakin mempertegas nilai penting tradisi ini. Jamu kini bukan lagi simbol keterbelakangan atau ramuan kuno yang ketinggalan zaman, melainkan kebanggaan identitas bangsa yang berhasil menembus batas waktu berkat kreativitas dan kesadaran hidup sehat masyarakat modern.",
             "「ジャムーの健康文化」を無形文化遺産として認定したユネスコ（UNESCO）からの公式認定は、この伝統の重要な価値をさらに際立たせました。ジャムーは今や、遅れた時代の象徴や時代遅れの古臭い生薬ではなく、現代社会の創造性と健康意識のおかげで時代の壁を突破することに成功した民族のアイデンティティの誇りとなっているのです。",
             "Warisan Budaya Takbenda（無形文化遺産）、mempertegas（明確にする・強調する）、keterbelakangan（後進性・遅れ）、menembus batas waktu（時代の壁を突破する）。")
        ],
        "vocab": [
            ("khazanah", "名詞", "-", "宝庫、財産、知の蓄積", "Indonesia memiliki khazanah budaya yang luas."),
            ("meracik", "動詞", "racik", "（薬や香辛料を）調合する、調合して作る", "Apoteker meracik obat sesuai resep dokter."),
            ("lekat", "形容詞", "-", "密着した、密接に結びついた", "Namanya lekat dengan dunia pendidikan."),
            ("pahit getir", "連語形容詞", "-", "苦くて渋い、（比喩的に）人生の辛苦", "Pahit getir kehidupan telah ia rasakan."),
            ("enggan", "助動詞・形容詞", "-", "〜したがらない、気が進まない", "Anak itu enggan minum obat yang pahit."),
            ("khasiat", "名詞", "-", "効能、薬効、優れた効き目", "Madu memiliki banyak khasiat kesehatan."),
            ("disulap", "動詞（受動）", "sulap", "手品のように変身させられる、一新される", "Lahan kosong disulap jadi taman bunga."),
            ("menggugah", "動詞", "gugah", "呼び覚ます、かき立てる、そそる", "Aroma masakan menggugah selera makan."),
            ("mempertegas", "動詞", "tegas", "より明確にする、強調する", "Bukti baru mempertegas putusan hakim."),
            ("ketinggalan zaman", "慣用表現", "tinggal", "時代遅れの、流行遅れの", "Gaya pakaian itu sudah ketinggalan zaman.")
        ],
        "grammar_points": """1. **接尾辞 `-kan` による状態からの使役動詞化（例: `terpinggirkan`, `mempertegas`）**:
   - 語根 *pinggir*（端・縁）+ *ter- -kan* = *terpinggirkan*（隅へ追いやられる・周縁化される）。
   - 語根 *tegas*（明確な）+ *memper-（拡大）* = *mempertegas*（より一層明確にする）。
2. **動詞反復による「続発・頻発」の表現 `bermunculan`**:
   - 語根 *muncul*（現れる）+ 接頭辞 *ber- -an* = 次から次へとあちこちに現れる。
   - 例: *Kafe-kafe baru bermunculan.*（新しいカフェが次々とオープンしている。）
3. **前置詞句 `berkat ...`（〜のおかげで）**:
   - ポジティブな要因を導入する構文です。
   - 例: *Berkat kerja keras, usahanya berhasil.*（努力のおかげで、彼の事業は成功した。）""",
        "quizzes": [
            ("昔ながらのジャムー売りの象徴的な行商スタイル（mbok jamu gendong）の特徴は何ですか？",
             ["クバヤを着て、背中に背負った竹籠にジャムーの瓶を入れて歩く姿", "バイクにスピーカーを積んで音楽を流す姿", "オンラインアプリでドローン配送する姿"],
             "クバヤを着て、背中に背負った竹籠にジャムーの瓶を入れて歩く姿",
             "第1段落に「...wanita paruh baya berkebaya yang berjalan kaki menjajakan botol-botol minuman jamu dalam bakul bambu yang digendong di punggungnya.」とあります。"),
            ("若者世代の間でジャムーが再び人気を獲得した工夫（イノベーション）は何ですか？",
             ["炭酸やオーツミルクと組み合わせ、お洒落なモダンカフェで提供したこと", "味を一切変えずに法律で飲用を強制したこと", "海外の人工着色料を大量に混ぜたこと"],
             "炭酸やオーツミルクと組み合わせ、お洒落なモダンカフェで提供したこと",
             "第3段落に「...disulap menjadi aneka minuman segar yang menggugah selera, seperti kombinasi kunyit asam bersoda, latte temulawak dengan susu gandum...」とあります。"),
            ("2023年にジャムーの国際的価値を決定づけた出来事は何ですか？",
             ["ユネスコ（UNESCO）の無形文化遺産への登録", "世界保健機関（WHO）による唯一の万能薬認定", "オリンピックの公式スポンサードリンク指定"],
             "ユネスコ（UNESCO）の無形文化遺産への登録",
             "第4段落に「Pengakuan resmi dari UNESCO yang menetapkan budaya sehat jamu sebagai Warisan Budaya Takbenda Dunia...」とあります。")
        ],
        "culture": """### ユネスコ無形文化遺産「Budaya Sehat Jamu」の奥深い世界
「Jamu（ジャムー）」は、ジャワ語の「Jawa（ジャワ）」と「Ngramu（調合する・集める）」に由来すると言われます。
代表的なメニューには、美肌や生理痛緩和に効くウコンとタマリンドの「Kunyit Asam」、疲労回復や食欲増進を促す「Beras Kencur（米とバンウコン）」、肝機能や免疫力を高める「Temulawak」、強烈な苦味でデトックス効果のある「Pahitan（センシンレン等）」などがあります。
2023年12月、ユネスコ無形文化遺産に正式登録され、現代インドネシアの誇り高きオーガニック・ウェルネス文化として世界中から注目されています。"""
    },
    {
        "id": "1227",
        "slug": "level-3-07-foreign-student-in-ugm",
        "title": "【Level 3 (B1)】Catatan Mahasiswa Asing di Jogja（ガジャマダ大学に留学した留学生の日記）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "ジョグジャカルタの最高峰ガジャマダ大学（UGM）に留学した日本人学生の日記。下宿（Kost）の大家さんや友人との交流、ジャワ文化の洗礼、多文化共生の学美を描く。",
        "text": """Enam bulan telah berlalu sejak aku pertama kali menginjakkan kaki di Yogyakarta untuk menempuh program pertukaran mahasiswa di Universitas Gadjah Mada (UGM). Masih terekam jelas dalam ingatanku betapa gugupnya diriku saat harus berbicara bahasa Indonesia di luar ruang kelas. Teori tata bahasa yang kupelajari di Tokyo terasa begitu kaku ketika dihadapkan dengan percakapan sehari-hari yang sarat dengan partikel santai dan dialek lokal.

Tempat tinggalku adalah sebuah kamar sewa sederhana, atau yang biasa disebut kost, di daerah Kaliurang. Ibu pemilik kost, yang biasa kupanggil Bu Endang, memperlakukanku layaknya anak kandung sendiri. Setiap kali aku jatuh sakit karena belum terbiasa dengan makanan pedas atau perubahan cuaca, beliau selalu mengantarkan semangkuk bubur ayam hangat dan segelas teh manis jahe ke kamarku. Kehangatan inilah yang meluluhkan rasa rindu pada kampung halaman.

Di kampus UGM, aku berinteraksi dengan teman-teman yang berasal dari Sabang sampai Merauke. Dalam diskusi kelompok perkuliahan, mereka selalu menyambut pendapatku dengan penuh keterbukaan, meskipun aksen bicaraku masih terbata-bata. Melalui obrolan santai di warung kopi dekat kampus, aku mulai memahami filosofi hidup masyarakat Jawa seperti alon-alon waton kelakon, yang mengajarkan pentingnya ketelitian dan keikhlasan dalam menjalani proses kehidupan tanpa tergesa-gesa.

Pengalaman hidup mandiri di kota pelajar ini bukan hanya memperluas wawasan akademisku tentang Asia Tenggara, melainkan juga membentuk kepribadianku menjadi lebih toleran dan peka terhadap perbedaan. Yogyakarta bukan lagi sekadar kota tujuan studi, melainkan telah menjadi rumah keduaku di mana rasa kekeluargaan mengalir tanpa memandang sekat kebangsaan.""",
        "paragraphs": [
            ("Enam bulan telah berlalu sejak aku pertama kali menginjakkan kaki di Yogyakarta untuk menempuh program pertukaran mahasiswa di Universitas Gadjah Mada (UGM). Masih terekam jelas dalam ingatanku betapa gugupnya diriku saat harus berbicara bahasa Indonesia di luar ruang kelas. Teori tata bahasa yang kupelajari di Tokyo terasa begitu kaku ketika dihadapkan dengan percakapan sehari-hari yang sarat dengan partikel santai dan dialek lokal.",
             "ガジャマダ大学（UGM）での交換留学プログラムに参加するために、僕が初めてジョグジャカルタに足を踏み入れてから6ヶ月が過ぎ去りました。教室の外でインドネシア語を話さなければならなかったとき、自分がどれほど緊張していたかが今でも鮮明に記憶に焼き付いています。東京で学んだ文法理論は、砕けた小辞や地元の方言に満ちた日常会話に直面したとき、あまりにも融通が利かず堅苦しく感じられました。",
             "menginjakkan kaki（足を踏み入れる）、menempuh program（プログラムを履修する）、sarat dengan（〜に満ちている）、dialek lokal（地元方言）。"),
            ("Tempat tinggalku adalah sebuah kamar sewa sederhana, atau yang biasa disebut kost, di daerah Kaliurang. Ibu pemilik kost, yang biasa kupanggil Bu Endang, memperlakukanku layaknya anak kandung sendiri. Setiap kali aku jatuh sakit karena belum terbiasa dengan makanan pedas atau perubahan cuaca, beliau selalu mengantarkan semangkuk bubur ayam hangat dan segelas teh manis jahe ke kamarku. Kehangatan inilah yang meluluhkan rasa rindu pada kampung halaman.",
             "僕の住まいは、カリウラン地区にある「コス（kost）」と呼ばれる質素な下宿部屋です。僕が普段エンダン小母さんと呼んでいる下宿の大家さんは、僕をまるで自分の実の子供のように扱ってくれました。辛い食べ物や気候の変化にまだ体が慣れずに僕が体調を崩すたびに、小母さんはいつも温かい一杯の鶏粥（ブブール・アヤム）と生姜入り甘い紅茶を部屋まで運んでくれました。この温かさこそが、故郷へのホームシックを溶かしてくれたのです。",
             "kamar sewa / kost（賃貸下宿部屋）、memperlakukan layaknya...（まるで〜のように扱う）、meluluhkan rasa rindu（恋しさ・ホームシックを溶かす）。"),
            ("Di kampus UGM, aku berinteraksi dengan teman-teman yang berasal dari Sabang sampai Merauke. Dalam diskusi kelompok perkuliahan, mereka selalu menyambut pendapatku dengan penuh keterbukaan, meskipun aksen bicaraku masih terbata-bata. Melalui obrolan santai di warung kopi dekat kampus, aku mulai memahami filosofi hidup masyarakat Jawa seperti alon-alon waton kelakon, yang mengajarkan pentingnya ketelitian dan keikhlasan dalam menjalani proses kehidupan tanpa tergesa-gesa.",
             "UGMのキャンパスでは、僕はサバンからメラウケに至る全国各地からやって来た友人たちと交流しました。講義のグループディスカッションにおいて、僕の話すアクセントがまだぎこちなく途切れ途切れであっても、彼らは常に寛容なオープンさで僕の意見を受け入れてくれました。大学近くのカフェでの気軽なおしゃべりを通じて、僕は「急がずとも着実に（alon-alon waton kelakon）」といったジャワの人々の人生哲学を理解し始めました。これは、焦ることなく人生のプロセスを歩む中での丁寧さと誠実さの尊さを教えてくれます。",
             "dari Sabang sampai Merauke（インドネシア全土の象徴表現）、terbata-bata（言葉がつかえる・ぎこちない）、alon-alon waton kelakon（ジャワの格言: 着実に進めば必ず成る）、tanpa tergesa-gesa（焦ることなく）。"),
            ("Pengalaman hidup mandiri di kota pelajar ini bukan hanya memperluas wawasan akademisku tentang Asia Tenggara, melainkan juga membentuk kepribadianku menjadi lebih toleran dan peka terhadap perbedaan. Yogyakarta bukan lagi sekadar kota tujuan studi, melainkan telah menjadi rumah keduaku di mana rasa kekeluargaan mengalir tanpa memandang sekat kebangsaan.",
             "この学術都市での一人暮らしの経験は、東南アジアに関する僕の学問的視野を広げただけでなく、僕の人格をより寛容で他者との違いに敏感なものへと形成してくれました。ジョグジャカルタはもはや単なる留学先の街ではなく、国籍の壁を越えて家族のような温かな絆が流れる僕の第2の故郷となったのです。",
             "kota pelajar（学術・学生都市）、memperluas wawasan（視野を広げる）、sekat kebangsaan（国籍の壁・境界線）。")
        ],
        "vocab": [
            ("menginjakkan", "動詞", "injak", "（足を）踏み入れる、足をつける", "Ia baru pertama kali menginjakkan kaki di pulau ini."),
            ("sarat", "形容詞", "-", "満ちた、積載いっぱいの、重層的な", "Buku sejarah itu sarat dengan pesan moral."),
            ("kost", "名詞", "-", "学生・単身者向けの下宿部屋、アパート", "Banyak mahasiswa mencari kost dekat kampus."),
            ("memperlakukan", "動詞", "laku", "〜として扱う、遇する", "Kita harus memperlakukan tamu dengan sopan."),
            ("meluluhkan", "動詞", "luluh", "溶かす、和らげる、頑なな心をほぐす", "Senyumannya meluluhkan amarah temannya."),
            ("terbata-bata", "副詞", "bata", "口ごもりながら、言葉がつかえながら", "Ia menjawab pertanyaan guru dengan terbata-bata."),
            ("filosofi", "名詞", "-", "哲学、人生観、根本理念", "Ia memegang teguh filosofi hidup sederhana."),
            ("tergesa-gesa", "副詞・形容詞", "gesa", "慌てて、焦って、性急に", "Jangan mengambil keputusan penting secara tergesa-gesa."),
            ("wawasan", "名詞", "was", "視野、見識、洞察力", "Membaca buku membuka wawasan dunia luar."),
            ("sekat", "名詞", "-", "仕切り、障壁、隔たり", "Toleransi meruntuhkan sekat perbedaan agama.")
        ],
        "grammar_points": """1. **直示的感嘆構文 `betapa ... -nya`（なんと〜なことか）**:
   - 感情や状態の強さを強調する構文です。
   - 例: *Masih terekam jelas betapa gugupnya diriku.*（自分がどれほど緊張していたかが今でも鮮明に記憶に残っている。）
2. **直面を表す受動構文 `dihadapkan dengan ...`（〜に直面させられる）**:
   - 語根 *hadap* + 接頭辞 *di- -kan*。
   - 例: *Ketika dihadapkan dengan masalah besar, tetaplah tenang.*（大きな問題に直面したとき、冷静であり続けなさい。）
3. **無意志動詞 `terekam`（記録・記憶されている）**:
   - 語根 *rekam*（録音・記録する）に無意志接頭辞 *ter-*。""",
        "quizzes": [
            ("語り手が東京で学んだインドネシア語文法を、ジョグジャカルタの日常会話で使った際に感じたギャップは何ですか？",
             ["日常会話は砕けた小辞や地元の方言に満ちており、教科書の文法があまりにも堅苦しく感じられたこと", "現地の人が全員英語しか話さなかったこと", "街の看板がすべて漢字で書かれていたこと"],
             "日常会話は砕けた小辞や地元の方言に満ちており、教科書の文法があまりにも堅苦しく感じられたこと",
             "第1段落に「Teori tata bahasa yang kupelajari di Tokyo terasa begitu kaku ketika dihadapkan dengan percakapan sehari-hari yang sarat dengan partikel santai dan dialek lokal.」とあります。"),
            ("下宿の大家であるエンダン小母さんが、語り手が病気になった際にしてくれた温かい看病は何ですか？",
             ["温かい鶏粥（ブブール・アヤム）と生姜入り紅茶を部屋まで届けてくれたこと", "すぐに病院へ入院させ面会謝絶にしたこと", "日本へ強制送還する手配をしたこと"],
             "温かい鶏粥（ブブール・アヤム）と生姜入り紅茶を部屋まで届けてくれたこと",
             "第2段落に「...beliau selalu mengantarkan semangkuk bubur ayam hangat dan segelas teh manis jahe ke kamarku.」とあります。"),
            ("友人とのおしゃべりで学んだジャワの人生哲学「alon-alon waton kelakon」が教えている大切な価値観は何ですか？",
             ["何事も焦らず、プロセスにおける丁寧さと誠実さを大切にして着実に進むこと", "誰よりも早く競争相手を蹴落として勝利すること", "何もしないで一日中寝て過ごすこと"],
             "何事も焦らず、プロセスにおける丁寧さと誠実さを大切にして着実に進むこと",
             "第3段落に「...mengajarkan pentingnya ketelitian dan keikhlasan dalam menjalani proses kehidupan tanpa tergesa-gesa.」とあります。")
        ],
        "culture": """### インドネシアの最高学府「UGM」と「Kota Pelajar」ジョグジャ
ジョグジャカルタは国内随一の「学生の街（Kota Pelajar）」と呼ばれ、インドネシア共和国初代大統領スカルノによって創設された最高峰の名門「ガジャマダ大学（Universitas Gadjah Mada: UGM）」をはじめ、100以上の高等教育機関が集まっています。
インドネシア各地（スマトラ、カリマンタン、スラウェシ、パプア等）から志の高い若者が集まり、下宿（Kost）で寝食を共にします。
生活費がジャカルタに比べて格段に安く、人々が温和で礼儀正しいため、外国人留学生にとっても最も居心地の良い留学先として絶大な人気を誇ります。"""
    },
    {
        "id": "1228",
        "slug": "level-3-08-fast-train-whoosh",
        "title": "【Level 3 (B1)】Merasakan Kereta Cepat Whoosh Jakarta-Bandung（高速鉄道ウーシュ初乗車記）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "東南アジア初の時速350km高速鉄道「Whoosh（ウーシュ）」。ジャカルタからバンドンまでの革新的モビリティと、乗客たちの興奮、近代インフラの飛躍を描く。",
        "text": """Stasiun Halim di Jakarta Timur pagi itu tampak berkilauan di bawah sorotan matahari cerah. Ratusan penumpang dari berbagai kalangan tampak antusias menanti di peron stasiun yang megah dan berstandar internasional. Hari ini adalah pengalaman pertamaku menjajal Kereta Cepat Jakarta-Bandung yang diberi nama Whoosh, moda transportasi massal modern yang menjadi tonggak sejarah baru perkeretaapian di Asia Tenggara.

Tepat saat pintu geser otomatis terbuka, aku melangkah masuk ke dalam kabin gerbong yang didesain futuristik dengan sentuhan motif batik megamendung khas Cirebon pada kursinya. Tidak lama kemudian, kereta mulai bergerak meluncur dengan akselerasi yang sangat mulus tanpa sentakan. Bahkan, koin yang kudirikan di atas ambang jendela tetap berdiri tegak tanpa bergoyang sedikit pun, membuktikan betapa stabilnya teknologi suspensi kereta ini.

Di layar digital gerbong, angka penunjuk kecepatan terus merangkak naik, menembus angka 200, 300, hingga mencapai kecepatan puncak 350 kilometer per jam. Pemandangan lanskap perkotaan, deretan perumahan, dan hamparan sawah hijau di sepanjang jalur melesat secepat kilat di balik kaca jendela. Perjalanan darat menuju Bandung yang sebelumnya kerap menelan waktu tiga hingga lima jam akibat kemacetan parah di jalan tol, kini terpangkas secara spektakuler menjadi hanya empat puluh lima menit saja.

Setibanya di Stasiun Padalarang, para penumpang saling melempar senyum kepuasan sambil mengabadikan momen berfoto di depan moncong kereta yang aerodinamis. Kehadiran Whoosh bukan sekadar memangkas jarak dan waktu tempuh antarkota, melainkan juga simbol lompatan peradaban bangsa Indonesia menuju masa depan yang lebih maju, efisien, dan terintegrasi secara modern.""",
        "paragraphs": [
            ("Stasiun Halim di Jakarta Timur pagi itu tampak berkilauan di bawah sorotan matahari cerah. Ratusan penumpang dari berbagai kalangan tampak antusias menanti di peron stasiun yang megah dan berstandar internasional. Hari ini adalah pengalaman pertamaku menjajal Kereta Cepat Jakarta-Bandung yang diberi nama Whoosh, moda transportasi massal modern yang menjadi tonggak sejarah baru perkeretaapian di Asia Tenggara.",
             "その朝、東ジャカルタのハリム駅は澄んだ日差しの下で輝いて見えました。様々な層から集まった数百人の乗客が、壮大で国際水準の駅プラットホームで熱心に待っていました。今日は、東南アジアの鉄道史における新たな歴史的節目となった最新の大量高速輸送機関である「Whoosh（ウーシュ）」と名付けられたジャカルタ・バンドン高速鉄道を僕が初めて体験する日です。",
             "berkilauan（輝いている）、menjajal（試す・体験乗車する）、tonggak sejarah（歴史的節目・マイルストーン）、perkeretaapian（鉄道事業・鉄道界）。"),
            ("Tepat saat pintu geser otomatis terbuka, aku melangkah masuk ke dalam kabin gerbong yang didesain futuristik dengan sentuhan motif batik megamendung khas Cirebon pada kursinya. Tidak lama kemudian, kereta mulai bergerak meluncur dengan akselerasi yang sangat mulus tanpa sentakan. Bahkan, koin yang kudirikan di atas ambang jendela tetap berdiri tegak tanpa bergoyang sedikit pun, membuktikan betapa stabilnya teknologi suspensi kereta ini.",
             "自動スライドドアが開いた瞬間、僕は座席にチレボン特有のメガムンドゥン（雨雲）バティック紋様のタッチが施された、未来的なデザインの客車キャビンへと足を踏み入れました。まもなく、列車は衝撃のない極めて滑らかな加速で滑るように動き始めました。それどころか、僕が窓枠の上に立てたコインは少しも揺れることなくまっすぐに立ち続け、この列車のサスペンション技術がいかに安定しているかを証明していました。",
             "pintu geser otomatis（自動引き戸・スライドドア）、motif batik megamendung（チレボンの伝統メガムンドゥン雲紋様）、akselerasi mulus（滑らかな加速）、tanpa sentakan（ガクンという衝撃なしに）。"),
            ("Di layar digital gerbong, angka penunjuk kecepatan terus merangkak naik, menembus angka 200, 300, hingga mencapai kecepatan puncak 350 kilometer per jam. Pemandangan lanskap perkotaan, deretan perumahan, dan hamparan sawah hijau di sepanjang jalur melesat secepat kilat di balik kaca jendela. Perjalanan darat menuju Bandung yang sebelumnya kerap menelan waktu tiga hingga lima jam akibat kemacetan parah di jalan tol, kini terpangkas secara spektakuler menjadi hanya empat puluh lima menit saja.",
             "車両のデジタル表示スクリーンでは、速度計の数字がぐんぐんと這い上がり、200、300の大台を突破し、最高時速350キロメートルに達しました。線路沿いの都市景観、住宅の並び、そして青々とした水田の広がりが、窓ガラスの向こう側を稲妻のような速さで駆け抜けていきました。以前は高速道路の深刻な渋滞により3時間から5時間もの時間を費やすのが常だったバンドンへの陸路の旅が、今や劇的にわずか45分へと短縮されたのです。",
             "merangkak naik（這い上がる・急上昇する）、kecepatan puncak（最高速度）、melesat secepat kilat（稲妻のように疾走する）、menelan waktu（時間を費やす・要する）、terpangkas（切り詰められる・短縮される）。"),
            ("Setibanya di Stasiun Padalarang, para penumpang saling melempar senyum kepuasan sambil mengabadikan momen berfoto di depan moncong kereta yang aerodinamis. Kehadiran Whoosh bukan sekadar memangkas jarak dan waktu tempuh antarkota, melainkan juga simbol lompatan peradaban bangsa Indonesia menuju masa depan yang lebih maju, efisien, dan terintegrasi secara modern.",
             "パダララン駅に到着すると、乗客たちは満足げな笑みを交わし合いながら、流線型の先頭車両の前で記念写真の瞬間をカメラに収めていました。ウーシュの登場は、単に都市間の距離と所要時間を短縮しただけでなく、より先進的で効率的、そして現代的に統合された未来へと向かうインドネシア民族の文明的跳躍の象徴でもあるのです。",
             "moncong kereta aerodinamis（空気力学的な流線型の列車先頭部）、waktu tempuh（所要時間）、lompatan peradaban（文明の跳躍）。")
        ],
        "vocab": [
            ("menjajal", "動詞", "jajal", "試す、試乗する、チャレンジする", "Kami ingin menjajal menu baru di restoran itu."),
            ("tonggak sejarah", "名詞句", "tonggak", "歴史的マイルストーン、金字塔、節目", "Peristiwa ini menjadi tonggak sejarah kemerdekaan."),
            ("sentakan", "名詞", "sentak", "急な揺れ、ガクンとする衝撃", "Kereta berhenti mendadak dengan sentakan kuat."),
            ("merangkak", "動詞", "rangkak", "這う、（数値が）徐々に上がっていく", "Penjualan merangkak naik setelah promosi."),
            ("melesat", "動詞", "lesat", "疾走する、弾丸のように飛び出す", "Anak panah melesat menuju sasaran."),
            ("menelan waktu", "動詞句", "telan", "（時間を）消費する、要する", "Proses perizinan menelan waktu berbulan-bulan."),
            ("terpangkas", "動詞（受動）", "pangkas", "切り詰められる、大幅に削減・短縮される", "Biaya operasional terpangkas hingga separuh."),
            ("mengabadikan", "動詞", "abadi", "永遠に残す、写真に収める、記念する", "Turis mengabadikan momen matahari terbenam."),
            ("moncong", "名詞", "-", "（動物の鼻先・機械の）突き出た先端部", "Moncong pesawat itu dicat warna perak."),
            ("lompatan", "名詞", "lompat", "跳躍、飛躍的進歩", "Teknologi ini merupakan lompatan besar bagi industri.")
        ],
        "grammar_points": """1. **時の起点・完了を表す接続詞 `Setibanya di ...`（〜に到着するとすぐに）**:
   - 語根 *tiba* + 接周辞 *se- -nya* = 到着するやいなや。
   - 例: *Setibanya di rumah, ia langsung istirahat.*（家に着くやいなや、彼はすぐに休んだ。）
2. **手段・状態を表す前置詞句 `dengan sentuhan ...`（〜のタッチ・装飾を伴って）**:
   - デザインや手法を修飾する洗練された表現です。
   - 例: *Desain modern dengan sentuhan tradisional.*（伝統のタッチが加わったモダンデザイン。）
3. **比喩的副詞句 `secepat kilat`（稲妻のように速く）**:
   - *se- + 形容詞 + 名詞*（〜と同じくらい〜）の比喩構文です。
   - 例: *seputih kapas*（綿のように白い）、*semanis madu*（蜂蜜のように甘い）。""",
        "quizzes": [
            ("ジャカルタ・バンドン高速鉄道（Whoosh）の走行中の卓越した安定性を示すエピソードは何ですか？",
             ["時速350kmで走行中も窓枠に立てたコインが倒れずに立ち続けたこと", "車内で熱いコーヒーがこぼれて火傷したこと", "乗客全員がシートベルトを締めさせられたこと"],
             "時速350kmで走行中も窓枠に立てたコインが倒れずに立ち続けたこと",
             "第2段落に「Bahkan, koin yang kudirikan di atas ambang jendela tetap berdiri tegak tanpa bergoyang sedikit pun...」とあります。"),
            ("従来は3〜5時間かかっていたジャカルタ〜バンドン間の所要時間は、Whooshによってどれほど短縮されましたか？",
             ["わずか45分へと短縮された", "2時間半へと短縮された", "15分へと短縮された"],
             "わずか45分へと短縮された",
             "第3段落に「...kini terpangkas secara spektakuler menjadi hanya empat puluh lima menit saja.」とあります。"),
            ("Whooshの客車の座席シートに施されている、インドネシアの伝統工芸にちなんだデザインは何ですか？",
             ["バリ島の彫刻柄", "チレボン特有のメガムンドゥン（Megamendung）バティック雲紋様", "パプアのアスマット族の木彫り模様"],
             "チレボン特有のメガムンドゥン（Megamendung）バティック雲紋様",
             "第2段落に「...sentuhan motif batik megamendung khas Cirebon pada kursinya.」とあります。")
        ],
        "culture": """### 東南アジア初の超高速鉄道「Whoosh（ウーシュ）」の衝撃
2023年10月に商業運行を開始した「Whoosh（Kereta Cepat Jakarta-Bandung）」は、最高営業時速350kmを誇る東南アジア初の高速鉄道です。
名称の「Whoosh」は、列車が風を切って疾走する擬音語であると同時に、「Waktu Hemat, Operasi Optimal, Sistem Hebat（時間節約・最適運用・卓越したシステム）」という国家スローガンの頭文字（アクロニム）となっています。
首都ジャカルタ（ハリム駅）と西ジャワの古都バンドンを最短30〜45分で結び、両都市圏の経済的一体化（メガロポリス化）を劇的に推進しています。"""
    },
    {
        "id": "1229",
        "slug": "level-3-09-traditional-weaving-tenun",
        "title": "【Level 3 (B1)】Jejak Benang Emas Tenun Sumba（スンバ島伝統織物に込められた母の祈り）",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "東ヌサ・トゥンガラ州スンバ島の伝統イカット織物「テヌン・スンバ（Tenun Ikat Sumba）」。天然草木染めと母から娘へ受け継がれる人生儀礼、文化遺産の継承を描く中級工芸パッセージ。",
        "text": """Di sebuah beranda rumah adat berpanggung di Desa Prailiu, Sumba Timur, dentang kayu alat tenun tradisional terdengar berirama memecah keheningan siang. Mama Maria, seorang penenun ulung berusia enam puluh tahun, duduk beralaskan tikar pandan sambil jemari tangannya yang lincah menyisipkan benang-benang pakan ke sela-sela benang lungsin. Sejak usia belia, ia telah mengabdikan hidupnya untuk merawat warisan adiluhung nenek moyang berupa kain tenun ikat khas Sumba.

Proses pembuatan selembar kain tenun ikat bukanlah pekerjaan yang bisa diselesaikan dalam hitungan pekan. Dari memintal kapas lokal menjadi benang, mengikat pola motif dengan serat gewang, hingga mencelupkannya ke dalam pewarna alami berbahan dasar akar mengkudu dan daun nila, semuanya membutuhkan kesabaran yang luar biasa. Seluruh proses ritual ini kerap memakan waktu enam bulan hingga satu tahun penuh sebelum sehelai kain bermutu tinggi siap dibentangkan.

Setiap goresan motif pada tenun ikat Sumba menyimpan filosofi spiritual yang sangat mendalam. Gambar kuda melambangkan kepemimpinan, kebangsawanan, dan keberanian para kesatria prajurit sabana. Sementara itu, motif buaya dan kura-kura merepresentasikan umur panjang dan kebijaksanaan para tetua adat. Bagi masyarakat adat Marapu, kain tenun bukan sekadar penutup raga, melainkan kain keramat yang mengiringi setiap fase daur hidup manusia, mulai dari kelahiran, upacara pernikahan, hingga pembungkus jenazah menuju alam baka.

Kini, tantangan modernisasi dan gempuran kain cetak pabrik yang murah mengancam kelangsungan hidup tradisi tenun tangan ini. Namun, harapan baru merekah ketika putri bungsu Mama Maria, yang baru saja menyelesaikan studinya di kota, memutuskan pulang kampung untuk membantu memadukan motif-motif klasik tenun Sumba dengan desain busana kontemporer. Melalui promosi digital dan pameran fesyen etnik, benang-benang magis tanah Sumba kini kembali bersinar menyapa panggung dunia.""",
        "paragraphs": [
            ("Di sebuah beranda rumah adat berpanggung di Desa Prailiu, Sumba Timur, dentang kayu alat tenun tradisional terdengar berirama memecah keheningan siang. Mama Maria, seorang penenun ulung berusia enam puluh tahun, duduk beralaskan tikar pandan sambil jemari tangannya yang lincah menyisipkan benang-benang pakan ke sela-sela benang lungsin. Sejak usia belia, ia telah mengabdikan hidupnya untuk merawat warisan adiluhung nenek moyang berupa kain tenun ikat khas Sumba.",
             "東スンバ県プライリウ村にある高床式の伝統家屋のベランダで、伝統的な機織り機の木が鳴り響くリズミカルな音が昼の静寂を破っていました。60歳の熟練織り手であるママ・マリアは、パンダナスの敷物の上に座り、その敏捷な手先で経糸（たていと）の隙間に緯糸（よこいと）を差し込んでいました。幼い頃から、彼女はスンバ特有の絣織物（テヌン・イカット）という祖先の至高の遺産を守り育てることにその生涯を捧げてきました。",
             "rumah adat berpanggung（高床式伝統家屋）、penenun ulung（熟練の機織り手）、benang pakan dan lungsin（緯糸と経糸）、warisan adiluhung（至高の崇高な遺産）。"),
            ("Proses pembuatan selembar kain tenun ikat bukanlah pekerjaan yang bisa diselesaikan dalam hitungan pekan. Dari memintal kapas lokal menjadi benang, mengikat pola motif dengan serat gewang, hingga mencelupkannya ke dalam pewarna alami berbahan dasar akar mengkudu dan daun nila, semuanya membutuhkan kesabaran yang luar biasa. Seluruh proses ritual ini kerap memakan waktu enam bulan hingga satu tahun penuh sebelum sehelai kain bermutu tinggi siap dibentangkan.",
             "1枚のイカット織物の制作プロセスは、数週間の単位で完了できるような仕事ではありません。地元産の綿花を紡いで糸にし、ゲワン椰子の繊維で文様パターンを括り（防染し）、ヤエヤマアオキ（モリンダ）の根や藍の葉を原料とする天然染料に浸す作業に至るまで、すべてが並外れた忍耐力を必要とします。高品質な布が広げられる準備が整うまで、この儀礼的プロセスの全体はしばしば丸6ヶ月から1年もの歳月を要します。",
             "memintal kapas（綿を紡ぐ）、pewarna alami（天然草木染料）、akar mengkudu（モリンダ／ノニの根・赤褐色染料）、daun nila（藍の葉・青色染料）。"),
            ("Setiap goresan motif pada tenun ikat Sumba menyimpan filosofi spiritual yang sangat mendalam. Gambar kuda melambangkan kepemimpinan, kebangsawanan, dan keberanian para kesatria prajurit sabana. Sementara itu, motif buaya dan kura-kura merepresentasikan umur panjang dan kebijaksanaan para tetua adat. Bagi masyarakat adat Marapu, kain tenun bukan sekadar penutup raga, melainkan kain keramat yang mengiringi setiap fase daur hidup manusia, mulai dari kelahiran, upacara pernikahan, hingga pembungkus jenazah menuju alam baka.",
             "スンバのイカット織物のすべての文様には、極めて深遠な精神的哲学が宿っています。馬の絵はサバンナの戦士たちのリーダーシップ、高貴さ、そして勇気を象徴しています。一方、ワニやカメのモチーフは、長寿と慣習法指導者（長老）たちの知恵を表しています。マラプ先住信仰の共同体にとって、織布は単なる肉体を覆う衣服ではなく、誕生、婚礼の儀式から、来世へと旅立つ遺体の包み布に至るまで、人間のライフサイクルの各段階に寄り添う神聖な布なのです。",
             "kebangsawanan（高貴さ・貴族性）、kesatria sabana（サバンナの戦士）、kepercayaan Marapu（スンバ島のマラプ先住信仰）、alam baka（来世・冥界）。"),
            ("Kini, tantangan modernisasi dan gempuran kain cetak pabrik yang murah mengancam kelangsungan hidup tradisi tenun tangan ini. Namun, harapan baru merekah ketika putri bungsu Mama Maria, yang baru saja menyelesaikan studinya di kota, memutuskan pulang kampung untuk membantu memadukan motif-motif klasik tenun Sumba dengan desain busana kontemporer. Melalui promosi digital dan pameran fesyen etnik, benang-benang magis tanah Sumba kini kembali bersinar menyapa panggung dunia.",
             "現在、近代化の挑戦と安価な工場製プリント布の猛攻が、この手織り伝統の存続を脅かしています。しかし、都会での学業を終えたばかりのママ・マリアの末娘が、スンバ織りの古典的モチーフと現代的なファッションデザインを融合させる手助けをするために帰郷を決意したとき、新たな希望が花開きました。デジタルプロモーションやエスニックファッション展を通じて、スンバの地の魔法の糸は今や再び輝きを放ち、世界の大舞台へと挨拶を届けているのです。",
             "gempuran kain cetak（プリント生地の猛攻）、kelangsungan hidup（存続・生き残り）、merekah（（希望やつぼみが）ほころび開く）、busana kontemporer（現代的な服飾ファッション）。")
        ],
        "vocab": [
            ("ulung", "形容詞", "-", "熟練した、百戦錬磨の、卓越した", "Ia adalah seorang pelaut ulung yang tangguh."),
            ("adiluhung", "形容詞", "-", "至高の、崇高で極めて価値の高い（文化遺産）", "Candi Borobudur adalah karya seni adiluhung."),
            ("memintal", "動詞", "pintal", "（糸を）紡ぐ、より合わせる", "Nenek memintal kapas menjadi benang halus."),
            ("kebangsawanan", "名詞", "bangsawan", "貴族階級、高貴さ、気品", "Sikapnya mencerminkan kebangsawanan sejati."),
            ("kebijaksanaan", "名詞", "bijaksana", "知恵、賢明さ、思慮深さ", "Keputusan itu diambil dengan penuh kebijaksanaan."),
            ("keramat", "形容詞", "-", "神聖な、霊験あらたかな、聖なる", "Masyarakat menjaga pohon keramat di hutan itu."),
            ("daur hidup", "名詞句", "daur", "ライフサイクル、生命の循環", "Kupu-kupu mengalami daur hidup sempurna."),
            ("alam baka", "名詞句", "baka", "来世、あの世、冥界（永遠の世界）", "Doa dipanjatkan untuk kerabat di alam baka."),
            ("gempuran", "名詞", "gempur", "猛攻、激しい打撃・圧力", "Produk impor memberi gempuran bagi pasar lokal."),
            ("merekah", "動詞", "rekah", "（花が）ほころび咲く、（夜が）明ける、（希望が）芽生える", "Bunga mawar merah merekah di musim semi.")
        ],
        "grammar_points": """1. **時の長さの概数表現 `dalam hitungan ...`（〜の単位で）**:
   - *dalam hitungan detik*（数秒で）
   - *dalam hitungan pekan*（数週間で）
   - *dalam hitungan bulan*（数ヶ月で）
2. **動名詞・受動の並列 `Dari..., ..., hingga...`（〜から〜を経て〜に至るまで）**:
   - 工程やプロセスの段階的推移を格調高く記述する構文です。
   - 例: *Dari memintal kapas, mengikat motif, hingga mencelup pewarna.*（綿を紡ぎ、文様を括り、染料に浸すに至るまで。）
3. **継続・献身を表す動詞 `mengabdikan`（捧げる）**:
   - 語根 *abdi*（仕える者・しもべ）+ 使役接尾辞 *-kan*。
   - 例: *mengabdikan hidup untuk seni*（芸術に生涯を捧げる）。""",
        "quizzes": [
            ("スンバ島の伝統イカット織物（Tenun Ikat Sumba）の1枚を完成させるのにどれくらいの期間がかかりますか？",
             ["工場で機械印刷するためわずか数分", "糸紡ぎや天然草木染めを含む儀礼工程のため6ヶ月から1年", "1週間以内"],
             "糸紡ぎや天然草木染めを含む儀礼工程のため6ヶ月から1年",
             "第2段落に「Seluruh proses ritual ini kerap memakan waktu enam bulan hingga satu tahun penuh...」とあります。"),
            ("スンバ織りのモチーフに描かれる「馬（kuda）」が象徴している意味は何ですか？",
             ["長寿と水利の知恵", "リーダーシップ、高貴さ、そしてサバンナの戦士の勇気", "大雨による豊かな稲作の収穫"],
             "リーダーシップ、高貴さ、そしてサバンナの戦士の勇気",
             "第3段落に「Gambar kuda melambangkan kepemimpinan, kebangsawanan, dan keberanian para kesatria prajurit sabana.」とあります。"),
            ("安価な工場製プリント布に対抗してスンバ織りの新たな希望となった、末娘の取り組みは何ですか？",
             ["織機の制作を中止して別の仕事を始めたこと", "スンバ織りの古典モチーフを現代ファッションと融合させ、世界へ発信したこと", "村の家をすべて取り壊したこと"],
             "スンバ織りの古典モチーフを現代ファッションと融合させ、世界へ発信したこと",
             "第4段落に「...membantu memadukan motif-motif klasik tenun Sumba dengan desain busana kontemporer. Melalui promosi digital dan pameran fesyen etnik...」とあります。")
        ],
        "culture": """### スンバ島の魂「Tenun Ikat」と土着信仰「Marapu」
東ヌサ・トゥンガラ州スンバ島（Pulau Sumba）は、独自のメガリス（巨石墓）巨石記念文化と精霊信仰「マラプ（Marapu）」が色濃く残る島です。
「Tenun Ikat（絣織物）」は女性たちによって手織りされ、青色は藍（Nila）、赤褐色はノニの根（Akar Mengkudu）などの天然草木染料のみを用いて何十回も浸染を繰り返します。
この織物は日常の衣服にとどまらず、結納品（Belis）や、死者を来世へ送り届けるための死装束として死者の周りに幾重にも巻かれるなど、魂と神霊世界をつなぐ最高神聖物とされています。"""
    },
    {
        "id": "1230",
        "slug": "level-3-10-level3-review-quiz",
        "title": "【Level 3 (B1) 総括】Dinamika Modern & Tradisi Nusantara & 総合読解診断テスト",
        "level": "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）",
        "desc": "Level 3（CEFR B1中級編）で登場した都市の機動力、フィンテック、文化リバイバル、伝統工芸、環境保全を総括する総合読解パッセージと、B1到達度判定クイズ。",
        "text": """Indonesia di abad ke-21 tengah berada di titik persimpangan sejarah yang sangat menarik, di mana laju modernisasi yang pesat berpadu secara harmonis dengan keteguhan merawat akar tradisi. Dari jalanan Jakarta yang dipenuhi oleh ribuan pengemudi ojek daring dan stasiun Whoosh yang melambangkan kecepatan peradaban, hingga ke sudut-sudut warung kelontong tradisional yang kini terintegrasi dengan kode QRIS, transformasi digital telah meresap ke dalam sendi-sendi kehidupan masyarakat hingga ke tingkat akar rumput.

Namun, di balik kegairahan menyambut kemajuan teknologi dan gaya hidup modern, bangsa ini tidak pernah kehilangan jiwanya. Fenomena kebangkitan kembali jamu tradisional di kafe-kafe kekinian, semaraknya tradisi mudik Lebaran yang menembus batas kelelahan fisik, hingga ketekunan para wanita penenun kain ikat di pelosok Sumba membuktikan bahwa tradisi bukanlah benda mati di museum, melainkan energi hidup yang terus berevolusi. Kesadaran untuk menjaga keseimbangan antara manusia, teknologi, dan alam—seperti yang diperjuangkan para pemuda penyelamat terumbu karang di Bunaken—menjadi kompas moral yang menuntun langkah nusantara menuju panggung masa depan yang gemilang.""",
        "paragraphs": [
            ("Indonesia di abad ke-21 tengah berada di titik persimpangan sejarah yang sangat menarik, di mana laju modernisasi yang pesat berpadu secara harmonis dengan keteguhan merawat akar tradisi. Dari jalanan Jakarta yang dipenuhi oleh ribuan pengemudi ojek daring dan stasiun Whoosh yang melambangkan kecepatan peradaban, hingga ke sudut-sudut warung kelontong tradisional yang kini terintegrasi dengan kode QRIS, transformasi digital telah meresap ke dalam sendi-sendi kehidupan masyarakat hingga ke tingkat akar rumput.",
             "21世紀のインドネシアは、急速な近代化の歩みが伝統の根を守り抜く不屈の強さと調和して融合する、極めて興味深い歴史の交差点の真っ只中にあります。何千人ものオンライン配車ドライバーで満たされたジャカルタの街路や、文明の速度を象徴する高速鉄道Whooshの駅から、今やQRISコードと統合された伝統的な個人商店の片隅に至るまで、デジタルトランスフォーメーションは草の根レベルにまで人々の生活の骨組みに浸透しています。",
             "titik persimpangan（交差点・分岐点）、keteguhan（堅固さ・不動の決意）、meresap ke sendi-sendi（骨組み・関節に染み渡る）、tingkat akar rumput（草の根レベル）。"),
            ("Namun, di balik kegairahan menyambut kemajuan teknologi dan gaya hidup modern, bangsa ini tidak pernah kehilangan jiwanya. Fenomena kebangkitan kembali jamu tradisional di kafe-kafe kekinian, semaraknya tradisi mudik Lebaran yang menembus batas kelelahan fisik, hingga ketekunan para wanita penenun kain ikat di pelosok Sumba membuktikan bahwa tradisi bukanlah benda mati di museum, melainkan energi hidup yang terus berevolusi. Kesadaran untuk menjaga keseimbangan antara manusia, teknologi, dan alam—seperti yang diperjuangkan para pemuda penyelamat terumbu karang di Bunaken—menjadi kompas moral yang menuntun langkah nusantara menuju panggung masa depan yang gemilang.",
             "しかし、技術的進歩と現代的なライフスタイルを歓迎する熱気の裏で、この国民は決してその魂を失っていません。最旬カフェにおける伝統生薬ジャムーの復活現象、肉体的疲労の限界を突破する熱気あふれるレバラン帰省（ムディック）の伝統、そしてスンバの僻地でイカット織物を織る女性たちの不屈の勤勉さに至るまで、これらは伝統が博物館に置かれた死せる展示物などではなく、進化し続ける生きたエネルギーであることを証明しています。ブナケンでサンゴ礁を救う青年たちが奮闘するように、人間、テクノロジー、そして自然の間の調和を保とうとする意識は、輝かしい未来の大舞台へと列島（ヌサンタラ）の歩みを導く道徳的コンパスとなっているのです。",
             "bukan benda mati di museum（博物館の死んだ物体ではない）、energi hidup yang terus berevolusi（進化し続ける生きたエネルギー）、kompas moral（道徳的コンパス）、masa depan yang gemilang（輝かしい未来）。")
        ],
        "vocab": [
            ("persimpangan", "名詞", "simpang", "交差点、辻、岐路", "Ia berdiri di persimpangan jalan kehidupan."),
            ("keteguhan", "名詞", "teguh", "堅固さ、不屈の意志、堅実さ", "Keteguhan imannya patut dicontoh."),
            ("meresap", "動詞", "resap", "染み込む、浸透する、深く染み渡る", "Air hujan meresap ke dalam tanah."),
            ("akar rumput", "名詞句", "rumput", "草の根（大衆・一般市民層）", "Dukungan datang dari masyarakat akar rumput."),
            ("kegairahan", "名詞", "gairah", "熱意、情熱、意気込み", "Kegairahan belajar anak-anak sangat tinggi."),
            ("semarak", "形容詞・名詞", "-", "華やかな、賑やかな、栄光", "Pesta rakyat berlangsung dengan sangat semarak."),
            ("pelosok", "名詞", "-", "僻地、片田舎、隅々", "Listrik kini telah masuk ke pelosok desa."),
            ("berevolusi", "動詞", "evolusi", "進化する、発展的に変化する", "Bahasa selalu berevolusi seiring zaman."),
            ("menuntun", "動詞", "tuntun", "導く、手を引いて案内する", "Orang tua menuntun langkah anak-anaknya."),
            ("gemilang", "形容詞", "-", "輝かしい、見事な、華々しい", "Ia meraih prestasi gemilang dalam kompetisi.")
        ],
        "grammar_points": """1. **総合構文 `Dari ..., hingga ke ..., [主文]`（〜から〜に至るまで〜）**:
   - 多彩な社会事象を網羅して全体像を描写する中上級の長文構文です。
2. **対比構文 `bukan ..., melainkan ...`（〜ではなく、むしろ〜である）**:
   - 概念の再定義や強調においてB1レベルで最頻出の論理構文です。
   - 例: *Bukan beban, melainkan kebanggaan.*（重荷ではなく、誇りである。）
3. **状態・関係を表す前置詞句 `di tengah titik persimpangan`（〜の交差点の真っ只中で）**:
   - 抽象的な歴史的局面を表現する格調高い比喩用法です。""",
        "quizzes": [
            ("この総括パッセージにおいて、現代インドネシアのデジタルトランスフォーメーションがどこまで浸透していると述べられていますか？",
             ["高級ホテルのスイートルームの客層だけに限定されている", "オジェックや高速鉄道から下町の個人商店のQRISまで、草の根レベル（akar rumput）にまで浸透している", "首都の一部のIT企業のみで使われている"],
             "オジェックや高速鉄道から下町の個人商店のQRISまで、草の根レベル（akar rumput）にまで浸透している",
             "第1段落に「...transformasi digital telah meresap ke dalam sendi-sendi kehidupan masyarakat hingga ke tingkat akar rumput.」とあります。"),
            ("パッセージの中で、伝統文化はどのようなものとして再定義（bukan... melainkan...）されていますか？",
             ["博物館に静置された死んだ物体ではなく、時代とともに進化し続ける生きたエネルギー（energi hidup yang terus berevolusi）である", "近代化の邪魔になるため早急に破棄すべき古い遺物である", "外国人観光客を騙すための商業的な飾りである"],
             "博物館に静置された死んだ物体ではなく、時代とともに進化し続ける生きたエネルギー（energi hidup yang terus berevolusi）である",
             "第2段落に「...membuktikan bahwa tradisi bukanlah benda mati di museum, melainkan energi hidup yang terus berevolusi.」とあります。"),
            ("ブナケンのサンゴ礁保全をはじめとする活動に見られる、インドネシアを輝かしい未来へ導く「道徳的コンパス（kompas moral）」とは何ですか？",
             ["人間、テクノロジー、そして自然の間の調和と均衡を保とうとする意識", "何よりも経済的利益を最優先して自然を開発する思想", "過去の伝統のみに固執して新しい科学技術を拒絶する姿勢"],
             "人間、テクノロジー、そして自然の間の調和と均衡を保とうとする意識",
             "第2段落に「Kesadaran untuk menjaga keseimbangan antara manusia, teknologi, dan alam... menjadi kompas moral yang menuntun langkah nusantara...」とあります。")
        ],
        "culture": """### CEFR B1レベル到達への祝詞と「Bhinneka Tunggal Ika」の現代的展開
CEFR B1レベルを修了した学習者は、インドネシア語の複文構造や受動態、中級接辞（-kan, -i, per- -an, ke- -an）を自然に読みこなし、現代社会のニュースやドキュメンタリーを大筋で理解できる「自立した言語使用者（Independent User）」の領域に到達しています。
テクノロジーの激動と古き良き伝統文化が共存するインドネシアは、まさに国家標語「Bhinneka Tunggal Ika（多様性の中の統一）」の精神を現代にアップデートし続けています。
この豊かな言語世界を土台として、続くLevel 4（B2）では、より深い社会論説やビジネス、学術的読解の世界へと羽ばたいていきましょう。"""
    }
]

def render_article(st):
    slug = st["slug"]
    title = st["title"]
    level = st.get("level", "CEFR B1（中級レベル・想定語彙数 1,200〜2,000語）")
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

<div class="level-badge" style="display:inline-block; background:#2563eb; color:white; padding:4px 12px; border-radius:20px; font-weight:bold; font-size:0.85rem; margin-bottom:1rem;">
  {level}
</div>

{desc}

---

## 📖 インドネシア語本文（Teks Bacaan）

<div class="reading-box" style="background:#f8fafc; border-left:4px solid #2563eb; padding:1.25rem 1.5rem; margin:1.5rem 0; line-height:1.9; font-size:1.05rem;">

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
  <p style="font-size:0.9rem; color:#64748b; margin-bottom:0;">💡 <strong>読解のポイント</strong>: {note}</p>
</div>
"""

    md += """---

## 📚 重要語彙・キーフレーズ10選（Kosakata Kunci）

| 単語 / フレーズ | 品詞 | 語根 | 日本語の意味 | 実践例文 |
| :--- | :--- | :--- | :--- | :--- |
"""
    for word, pos, root, meaning, eg in vocab:
        md += f"| **{word}** | {pos} | `{root}` | {meaning} | *{eg}* |\n"

    md += f"""
---

## 🛠️ 文法・構文の徹底解説（Tata Bahasa & Pola Kalimat）

{grammar_points}

---

## ✍️ 読解力チェッククイズ（Latihan Pemahaman）

本文の内容を正しく理解できているか、3つの問いで確認してみましょう。

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

## 🌿 背景知識・文化コラム（Wawasan Budaya）

{culture}

---

## 🧭 次のステップ・関連学習
- 読解で出会った未知の語彙は、単語リストだけでなく前後の文脈とともにノートに記録しましょう。
- 本文の音声を頭の中で再生しながら、左から右へ語順通りに直読直解するトレーニングを繰り返してください。
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

print("All 10 Level 3 articles created successfully!")
