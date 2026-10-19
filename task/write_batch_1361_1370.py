# -*- coding: utf-8 -*-
"""
セクション33 第2バッチ (1361-1370) 記事生成スクリプト
【語彙拡張】語根別派生語マスター図鑑 第2弾
"""

import os

articles = [{'filename': '111-root-tambah.md',
  'title': '1361. 語根 tambah の全派生語図鑑（menambah, bertambah, tambahan, penambahan）',
  'root': 'tambah',
  'core_meaning': '増える、増やす、添加する、付け加える、お代わり',
  'explanation': '語根 tambah '
                 'は、既存の数量や程度に新たな要素を「加える・増大させる」というコアを持ちます。自発的な増加（bertambah）から人為的な追加・補足（menambah）、追加料金や付加価値（tambahan）、制度的増員・増額（penambahan）まで、数量・進歩・拡大を語る最頻出語根です。',
  'matrix': [('menambah',
              'meN-',
              '他動詞',
              '増やす、付け加える、増大させる',
              'Pemerintah berencana menambah anggaran pendidikan tahun depan.'),
             ('ditambah', 'di-', '受動態動詞・接続詞', '加えられる、〜に加えて（plus）', 'Tiga ditambah lima sama dengan delapan.'),
             ('bertambah', 'ber-', '自動詞', '増える、増大する、ますます〜になる', 'Jumlah penduduk kota bertambah pesat setiap tahun.'),
             ('tambahan', '-an', '名詞・形容詞', '追加、付加、おまけ、追加の', 'Karyawan lembur berhak menerima upah tambahan.'),
             ('penambahan',
              'peN- -an',
              '名詞',
              '追加作業、増員、増額プロセス',
              'Penambahan fasilitas laboratorium disambut gembira para mahasiswa.'),
             ('pertambahan',
              'per- -an',
              '名詞',
              '増加現象、自然増、増大の度合い',
              'Pertambahan penduduk alami dipengaruhi oleh angka kelahiran.'),
             ('tambah-tambah',
              'kata ulang',
              '副詞',
              'ますます、輪をかけて、なおさら',
              'Hujan deras disertai angin kencang membuat suasana tambah dingin.')],
  'details': [('menambah',
               '他動詞',
               'ムナンバハ',
               '主語が外的な対象に対して数量や価値を「人為的に加える・増やす」動作です。',
               'menambah wawasan（見識を広げる）, menambah modal（資本を増強する）, menambah daya listrik（契約電力を増設する）',
               'Membaca buku setiap hari dapat menambah perbendaharaan kata asing kita.',
               '毎日読書することは、私たちの外国語の語彙を増やすことができる。'),
              ('bertambah',
               '自動詞',
               'ブルナンバハ',
               '対象そのものが自発的・自然に「増える、より〜の度合いを増す」状態変化を表します。',
               'bertambah usia（歳を重ねる）, bertambah parah（悪化する）, bertambah kaya（ますます裕福になる）',
               'Seiring bertambahnya usia, kita harus semakin bijak menjaga kesehatan.',
               '年齢を重ねるにつれて、私たちは健康管理により賢明にならなければならない。'),
              ('tambahan',
               '名詞・形容詞',
               'タンバハン',
               '本来のものに加えて与えられる「おまけ、付加物、追加手当」を指します。',
               'biaya tambahan（追加料金・チャージ）, nilai tambahan（付加価値）, tugas tambahan（追加課題）',
               'Apakah ada biaya tambahan untuk pengiriman paket pada akhir pekan?',
               '週末の荷物配送には追加料金が発生しますか？'),
              ('penambahan',
               '名詞',
               'プナンバハン',
               '設備や人員、予算などを人為的に「付け加える作業・増員・増設のプロセス」を指します。',
               'penambahan rute bus（バス路線の増設）, penambahan kuota（定員の増枠）, penambahan pegawai（職員の増員）',
               'Manajemen menyetujui penambahan lima staf baru di divisi pemasaran.',
               '経営陣はマーケティング部門における5名の新規スタッフ増員を承認した。')],
  'dialogue': {'title': 'レストランでの料理の追加注文とサービスの確認',
               'lines': [('Rian', 'Pelayan, bolehkah kami menambah satu porsi nasi putih lagi?'),
                         ('Pelayan', 'Tentu, Pak. Apakah ada tambahan menu minuman atau lauk lainnya?'),
                         ('Rian', 'Cukup nasi saja. Suasananya nyaman sekali, membuat selera makan bertambah.'),
                         ('Pelayan',
                          'Terima kasih, Pak. Kami memang sedang melakukan penambahan kapasitas ruangan demi '
                          'kenyamanan pelanggan.')]},
  'grammar_point': '### menambah（他動詞）vs bertambah（自動詞）の決定的な違い\n'
                   '\n'
                   '語根 tambah の派生で最も厳格に区別すべき構文ルールです：\n'
                   '- **menambah**（他動詞）：目的語を取る。「〜を増やす、追加する」。\n'
                   '  - 例: *Perusahaan **menambah** modal.*（会社は資本を増やした。）\n'
                   '- **bertambah**（自動詞）：目的語を取らない。「〜が増える、ますます…になる」。\n'
                   '  - 例: *Modal perusahaan **bertambah**.*（会社の資本が増えた。）\n'
                   '  - 例: *Sakitnya **bertambah** parah.*（病状がますます悪化した。）\n'
                   '\n'
                   '「形容詞 + bertambah」または「bertambah + 形容詞（bertambah tinggi, bertambah mahal）」で「ますます〜になる」という比較級の深化を表します。',
  'quiz': [{'q': "Manakah kalimat yang menggunakan kata 'bertambah' secara benar?",
            'options': ['Saya ingin bertambah gaji karyawan bulan depan.',
                        'Jumlah wisatawan mancanegara bertambah secara signifikan tahun ini.',
                        'Pemerintah bertambah kuota subsidi bahan bakar.',
                        'Tolong bertambah garam pada sup yang tawar ini.'],
            'ans': 'Jumlah wisatawan mancanegara bertambah secara signifikan tahun ini.',
            'exp': '観光客数が自然に「増える」という自動詞用法なので bertambah が正解です。'},
           {'q': "Istilah yang tepat untuk menyebut '追加料金（Extra Charge）' adalah...",
            'options': ['biaya bertambah', 'biaya tambahan', 'biaya penambahan', 'biaya pertambahan'],
            'ans': 'biaya tambahan',
            'exp': '「追加の、付加的な」という修飾語は tambahan を用い、biaya tambahan と言います。'},
           {'q': "Lengkapi kalimat: 'Seiring ... usia, kondisi fisik manusia akan mengalami penurunan alami.'",
            'options': ['menambahnya', 'bertambahnya', 'tambahannya', 'tertambahnya'],
            'ans': 'bertambahnya',
            'exp': '「年齢が増える・重なるにつれて」という成句は「Seiring bertambahnya usia」です。'}],
  'column': '### 語源コラム：食堂の定番フレーズ「Nambah Nasi（ご飯お代わり！）」\n'
            '\n'
            'インドネシアの定食屋（Warung Nasi）やパダン料理店で、客たちが笑顔で叫ぶ決まり文句が「Mas, nambah nasi satu lagi!（お兄さん、ご飯もう一杯お代わり！）」です。\n'
            '\n'
            '口語では接頭辞 meN- が脱落して「Nambah（追加する・お代わりする）」と短縮されます。サンバルや濃厚なカレーソースが美味しすぎてご飯が止まらない時、「Nambah '
            'terus（何度もおかわりする）」することは、料理人に対する最高の賛辞とみなされます。'},
 {'filename': '112-root-kurang.md',
  'title': '1362. 語根 kurang の全派生語図鑑（mengurangi, berkurang, kekurangan, pengurangan）',
  'root': 'kurang',
  'core_meaning': '減る、減らす、不足する、欠点、あまり〜でない（控えめ否定）',
  'explanation': '語根 kurang '
                 'は、数量や基準に対して「足りない、減退する、控える」というコアを持ちます。引き算やコスト削減（mengurangi）、自然な減少（berkurang）、欠乏や栄養失調（kekurangan '
                 'gizi）、そして「あまり美味しくない（kurang enak）」といった丁寧な控えめ否定（オブラート表現）まで、極めて重要な語根です。',
  'matrix': [('mengurangi',
              'meN- -i',
              '他動詞',
              '減らす、削減する、控える、割り引く',
              'Kita harus mengurangi konsumsi gula demi kesehatan jantung.'),
             ('dikurangi', 'di- -i', '受動態動詞・接続詞', '減らされる、〜を引いて（minus）', 'Sepuluh dikurangi empat sama dengan enam.'),
             ('berkurang', 'ber-', '自動詞', '減る、減少する、衰える、和らぐ', 'Rasa sakit di kakinya berangsur-angsur mulai berkurang.'),
             ('kekurangan',
              'ke- -an',
              '名詞・状態動詞',
              '不足、欠乏、欠点、〜が不足している',
              'Banyak balita di daerah terpencil mengalami kekurangan gizi.'),
             ('pengurangan',
              'peN- -an',
              '名詞',
              '削減、減量、縮小プロセス、引き算',
              'Pengurangan subsidi energi memicu kenaikan harga bahan pokok.'),
             ('sekurang-kurangnya',
              'se- -nya',
              '副詞',
              '少なくとも、最低限（setidaknya）',
              'Tidurlah sekurang-kurangnya tujuh jam setiap malam.'),
             ('kurang lebih',
              'frasa',
              '成句副詞',
              'およそ、約、大体（kira-kira）',
              'Jarak dari sini ke bandara kurang lebih lima belas kilometer.')],
  'details': [('mengurangi',
               '他動詞',
               'ムングランギ',
               '主語が数量、負荷、リスク、支出を人為的に「減らす・削減する」動作です。',
               'mengurangi sampah plastik（プラスチックゴミを削減する）, mengurangi stres（ストレスを緩和する）, mengurangi kecepatan（速度を落とす）',
               'Pemerintah mendorong warga untuk mengurangi penggunaan kantong plastik.',
               '政府は市民に対してレジ袋の使用を削減するよう奨励している。'),
              ('berkurang',
               '自動詞',
               'ブルクラン',
               '他からの使役ではなく、数量や痛みの強度が「自然に減少する・引いていく」動作です。',
               'daya tahan berkurang（持久力が衰える）, nafsu makan berkurang（食欲が減退する）, debit air berkurang（水量が減る）',
               'Setelah meminum obat penurun panas, suhu tubuhnya mulai berkurang.',
               '解熱剤を服用した後、彼の体温は下がり始めた。'),
              ('kekurangan',
               '名詞・動詞',
               'ククランガン',
               '必要なものが「不足している状態（欠乏）」、または人の「弱点・短所」を指します。',
               'kekurangan air bersih（きれいな水の不足）, kekurangan modal（資金不足）, kelebihan dan kekurangan（長所と短所）',
               'Setiap manusia memiliki kelebihan dan kekurangan masing-masing.',
               'すべての人間は各自の長所と短所を持っている。'),
              ('pengurangan',
               '名詞',
               'プングランガン',
               '予算や人員、二酸化炭素排出量などを能動的に「削減する計画・作業プロセス」を指します。',
               'pengurangan emisi karbon（炭素排出削減）, pengurangan biaya operasional（運営コスト削減）, pengurangan staf（人員削減）',
               'Target pengurangan emisi gas rumah kaca telah ditetapkan dalam dokumen iklim.',
               '温室効果ガスの排出削減目標が気候変動文書の中で定められた。')],
  'dialogue': {'title': 'オフィスの経費削減と業務効率化ミーティング',
               'lines': [('Budi',
                          'Manajemen meminta kita untuk mencari cara mengurangi pengeluaran operasional bulan depan.'),
                         ('Linda', 'Apakah pengurangan anggaran ini akan berdampak pada kualitas layanan kita, Pak?'),
                         ('Budi',
                          'Kita usahakan tidak. Kekurangan staf bisa diatasi dengan otomatisasi sistem komputer.'),
                         ('Linda',
                          'Baik, Pak. Jika sistem berjalan lancar, beban kerja manual kita pasti akan berkurang '
                          'drastis.')]},
  'grammar_point': '### クッション言葉としての「kurang + 形容詞」（控えめ否定）\n'
                   '\n'
                   'インドネシア社会では、直接的に不快感や否定を表明するのを避ける「Halus（上品・控えめ）」の文化があります。そこで **tidak の代わりに kurang を使うテクニック** '
                   'が極めて多用されます：\n'
                   '- *Masakan ini tidak enak.*（この料理はまずい。）→ ❌ 露骨すぎて角が立つ\n'
                   '- *Masakan ini **kurang** enak.*（この料理はちょっと味が物足りない。）→ ⭕ ソフトで丁寧な表現\n'
                   '- *Saya **kurang** paham.*（あまりよく理解できていません＝わからない）\n'
                   '- *Harganya **kurang** cocok.*（お値段が少々折り合いません＝高すぎる）',
  'quiz': [{'q': "Bagaimana cara menolak tawaran harga secara sopan menggunakan kata 'kurang'?",
            'options': ['Harganya tidak boleh sama sekali!',
                        'Maaf, harganya kurang cocok dengan anggaran saya.',
                        'Saya kekurangan uang selamanya.',
                        'Tolong kurangi seluruh barang toko ini.'],
            'ans': 'Maaf, harganya kurang cocok dengan anggaran saya.',
            'exp': 'kurang cocok は「少々合わない（高すぎる）」と角を立てずに伝える丁寧なビジネス表現です。'},
           {'q': "Kata yang tepat untuk mendeskripsikan '長所と短所' adalah...",
            'options': ['pertambahan dan pengurangan',
                        'kelebihan dan kekurangan',
                        'mengurangi dan menambah',
                        'kurang lebih'],
            'ans': 'kelebihan dan kekurangan',
            'exp': '長所と短所（メリット・デメリット）は「kelebihan dan kekurangan」と表現します。'},
           {'q': "Frasa 'kurang lebih' memiliki makna yang sepadan dengan...",
            'options': ['persis sama', 'kira-kira / sekitar', 'tidak pernah', 'sangat jauh'],
            'ans': 'kira-kira / sekitar',
            'exp': 'kurang lebih は「およそ、約（approximately）」を意味します。'}],
  'column': '### 語源コラム：値切り交渉の魔法「Boleh kurang?（まけてくれる？）」\n'
            '\n'
            '伝統市場（Pasar Tradisional）や路面店で買い物をする際、インドネシア語学習者が最初に覚える最も役立つフレーズが「Boleh kurang, Pak?（おじさん、少し安くしてくれる？）」です。\n'
            '\n'
            '「Harga pas（定価）」と書かれていない限り、店主は「Kurang sedikit '
            'boleh（少しなら引いてあげるよ）」と笑顔で応じてくれます。単なる値切りではなく、売り手と買い手が言葉を交わし、親近感（Keakraban）を育む伝統市場のコミュニケーションの基本です。'},
 {'filename': '113-root-bagi.md',
  'title': '1363. 語根 bagi の全派生語図鑑（membagi, berbagi, pembagian, sebagian）',
  'root': 'bagi',
  'core_meaning': '分ける、分配する、共有する、〜にとって、割り算',
  'explanation': '語根 bagi '
                 'は、一つの全体を切り分けて複数に「配分する、シェアする」というコアと、視点を提示する「〜にとって（for/to）」という前置詞の二大機能性を持ちます。富の分配（pembagian）や助け合いの分かち合い（berbagi）、部分集合（sebagian '
                 'besar）まで、社会連帯の精神を支える語根です。',
  'matrix': [('membagi', 'meN-', '他動詞', '分ける、分配する、分類する、割る', 'Ibu membagi kue bolu menjadi delapan potong sama besar.'),
             ('dibagi', 'di-', '受動態動詞・接続詞', '分けられる、〜で割って（divided by）', 'Dua belas dibagi tiga sama dengan empat.'),
             ('berbagi',
              'ber-',
              '自動詞',
              '分かち合う、共有する、施しをする',
              'Komunitas relawan gemar berbagi makanan kepada warga miskin.'),
             ('pembagian',
              'peN- -an',
              '名詞',
              '分配、配給、区分、割り算',
              'Pembagian bantuan sosial berlangsung tertib di kantor kelurahan.'),
             ('sebagian',
              'se- -an',
              '名詞・副詞',
              '一部、部分的に、〜のうち一部',
              'Sebagian besar karyawan memilih bekerja dari rumah hari ini.'),
             ('bagian', '-an', '名詞', '部分、部署、部門、割当分', 'Saya bekerja di bagian hubungan masyarakat dan pemasaran.'),
             ('bagaimanapun',
              'frasa',
              '複合接続詞',
              'どうであれ、いずれにせよ、どんなに〜でも',
              'Bagaimanapun sulitnya situasi ini, kita tidak boleh menyerah.')],
  'details': [('membagi',
               '他動詞',
               'ムンバギ',
               '全体を複数の断片やグループに「人為的に区分・配分する」動作です。',
               'membagi waktu（時間をやりくりする）, membagi tugas（役割分担する）, membagi rata（均等に分ける）',
               'Ketua kelompok membagi tugas penelitian kepada setiap anggota secara adil.',
               'リーダーは各メンバーに研究課題を公平に役割分担した。'),
              ('berbagi',
               '自動詞',
               'ブルバギ',
               '自分の持っている食べ物、知識、幸せを他者と「分かち合う、シェアする」という温かい行為を表します。',
               'berbagi pengalaman（経験を分かち合う）, berbagi rezeki（恵みを分かち合う）, berbagi layar（画面共有する）',
               'Indahnya berbagi terasa saat kita melihat senyum anak-anak panti asuhan.',
               '孤児院の子どもたちの笑顔を見たとき、分かち合うことの素晴らしさが実感される。'),
              ('sebagian',
               '名詞・副詞',
               'スバギアン',
               '全体の中の「一部分」を指します。「sebagian besar（大部分）」は論説文の超重要表現です。',
               'sebagian besar（大部分）, sebagian kecil（ごく一部）, untuk sebagian orang（一部の人々にとっては）',
               'Sebagian besar lahan di pulau tersebut masih berupa hutan lindung alami.',
               'その島の土地の大部分は依然として天然の保護林のままである。'),
              ('bagian',
               '名詞',
               'バギアン',
               '物の一部、組織の「課・部門」、または自分の取り分（シェア）を指します。',
               'bagian keuangan（財務課）, bagian dari sejarah（歴史の一部）, mengambil bagian（参加する）',
               'Generasi muda harus mengambil bagian aktif dalam pembangunan bangsa.',
               '若者世代は国家建設において能動的な役割を担わなければならない。')],
  'dialogue': {'title': '社会貢献活動での食糧配給とボランティアの役割分担',
               'lines': [('Dewi', 'Bagaimana kita akan membagi paket sembako ini kepada warga yang membutuhkan?'),
                         ('Rizky', 'Kita bagi menjadi tiga tim lapangan agar proses pembagian berjalan cepat.'),
                         ('Dewi',
                          'Ide bagus. Senang sekali melihat masyarakat saling berbagi di masa sulit seperti ini.'),
                         ('Rizky',
                          'Benar, sebagian besar donasi ini terkumpul dari para dermawan muda di media sosial.')]},
  'grammar_point': '### 前置詞 bagi（〜にとって）の用法\n'
                   '\n'
                   '語根 bagi は単体で**「〜にとって（for / to / as for）」**という視点提示の前置詞として日常・論説で多用されます：\n'
                   '- *Bagi saya, keluarga adalah segalanya.*（私にとって、家族がすべてです。）\n'
                   '- *Bahasa Indonesia sangat penting bagi masa depan karier Anda.*（インドネシア語はあなたの将来のキャリアにとって極めて重要です。）\n'
                   '同義語に **untuk** や **menurut** がありますが、客観的な価値や影響を提示する際には **bagi** が最も格調高く自然です。',
  'quiz': [{'q': "Frasa yang paling tepat untuk menerjemahkan '大部分の人々（The majority of people）' adalah...",
            'options': ['sebagian kecil orang', 'sebagian besar orang', 'pembagian orang', 'berbagi orang'],
            'ans': 'sebagian besar orang',
            'exp': '大部分・過半数は「sebagian besar」と表現します。'},
           {'q': "Lengkapi kalimat: '... saya, kejujuran adalah nilai moral yang paling utama.'",
            'options': ['Membagi', 'Bagi', 'Bagian', 'Dibagi'],
            'ans': 'Bagi',
            'exp': '「私にとって（as for me）」という前置詞句は「Bagi saya」となります。'},
           {'q': "Fitur 'Screen Sharing' pada aplikasi Zoom dalam bahasa Indonesia diterjemahkan sebagai...",
            'options': ['membagi layar', 'berbagi layar', 'pembagian layar', 'bagian layar'],
            'ans': 'berbagi layar',
            'exp': '画面共有（Share screen）は「berbagi layar」と言います。'}],
  'column': '### 語源コラム：ラマダン（断食月）の美徳「Indahnya Berbagi（分かち合いの美）」\n'
            '\n'
            'イスラム教の断食月（ラマダン）になると、テレビや街頭広告で一斉に掲げられるスローガンが「Indahnya Berbagi（分かち合いの素晴らしさ）」です。\n'
            '\n'
            '夕暮れの断食明け（Buka Puasa）の時刻が近づくと、路上ではボランティアや一般市民が道行く人々に無料の甘い軽食や飲料水（Takjil '
            'Gratis）を配り歩きます。自らの富を独り占めせず、恵まれない人々と喜びを分かち合う「Berbagi」の精神は、インドネシア社会の強固な社会的紐帯（ソーシャル・キャピタル）そのものです。'},
 {'filename': '114-root-gabung.md',
  'title': '1364. 語根 gabung の全派生語図鑑（menggabungkan, bergabung, penggabungan, gabungan）',
  'root': 'gabung',
  'core_meaning': '結合する、合流する、合併する、グループに加わる',
  'explanation': '語根 gabung '
                 'は、バラバラに存在していた複数の要素を「一つに結び合わせる、集団に合流する」というコアを持ちます。企業合併・M&A（penggabungan/merger）からコミュニティへの参加（bergabung）、複数の機能の統合（menggabungkan）まで、アライアンスやシナジーを語る重要語根です。',
  'matrix': [('menggabungkan',
              'meN- -kan',
              '他動詞',
              '結びつける、結合・統合する、合併させる',
              'Perancang busana menggabungkan motif batik dengan gaya modern.'),
             ('digabungkan',
              'di- -kan',
              '受動態動詞',
              '統合される、併合される、結合される',
              'Dua kementerian strategis digabungkan menjadi satu badan baru.'),
             ('bergabung',
              'ber-',
              '自動詞',
              '加わる、参加する、合流する、加盟する',
              'Indonesia resmi menyatakan minatnya untuk bergabung dengan OECD.'),
             ('gabungan',
              '-an',
              '名詞・形容詞',
              '連合、結合体、合同の、複合的な',
              'Pasukan gabungan TNI dan Polri menggelar operasi pengamanan.'),
             ('penggabungan',
              'peN- -an',
              '名詞',
              '合併、併合、統合プロセス (Merger)',
              'Penggabungan bank-bank syariah BUMN melahirkan BSI.'),
             ('tergabung',
              'ter-',
              '状態動詞',
              '所属している、組み込まれている',
              'Ribuan pengemudi ojol tergabung dalam serikat pekerja mandiri.'),
             ('bergabung bersama',
              'frasa',
              '成句',
              '〜とともに合流・参加する',
              'Mari bergabung bersama kami membangun komunitas literasi digital.')],
  'details': [('menggabungkan',
               '他動詞',
               'ムンガブンカン',
               '異なる2つ以上の要素、技術、アイデアを融合させて一つの新しいものを生み出す動作です。',
               'menggabungkan tradisi dan modernitas（伝統と現代性を融合する）, menggabungkan data（データを統合する）',
               'Chef itu mahir menggabungkan rempah lokal dengan teknik kuliner Prancis.',
               'そのシェフは地元のスパイスとフランス料理の技法を融合させることに長けている。'),
              ('bergabung',
               '自動詞',
               'ブルガブン',
               '主語が既存の組織、クラブ、国連などの国際連盟に「自らメンバーとして加わる・加盟する」動作です。',
               'bergabung dengan tim（チームに加わる）, bergabung dalam komunitas（コミュニティに参加する）',
               'Selamat datang kepada para kolega baru yang baru saja bergabung di kantor ini.',
               'このオフィスに新しく加わった新しい同僚の皆さん、ようこそ。'),
              ('gabungan',
               '名詞・形容詞',
               'ガブンガン',
               '複数の機関や力が一つに結集した「合同体、連合組織」を指します。',
               'tim gabungan（合同捜査・対策チーム）, kekuatan gabungan（連合戦力）, operasi gabungan（合同作戦）',
               'Tim gabungan SAR dan relawan terus menyisir lokasi bencana tanah longsor.',
               '捜索救助隊（SAR）とボランティアの合同チームは地滑り被災現場を捜索し続けている。'),
              ('penggabungan',
               '名詞',
               'プンガブンガン',
               '企業や省庁、銀行などが制度的・法的に一つになる「合併・統合手続き（Merger）」を指します。',
               'penggabungan usaha (merger)（企業合併）, penggabungan sekolah（学校統廃合）',
               'Rencana penggabungan dua maskapai penerbangan nasional telah disetujui pemerintah.',
               '2つの国営航空会社の合併計画は政府によって承認された。')],
  'dialogue': {'title': '新しいスタートアップコミュニティへの参加と技術統合',
               'lines': [('Dimas',
                          'Apakah aplikasi baru kalian berhasil menggabungkan fitur e-commerce dan media sosial?'),
                         ('Nita',
                          'Iya, Dimas. Kami merancangnya agar ramah pengguna. Mau bergabung menjadi penguji coba '
                          'beta?'),
                         ('Dimas',
                          'Tentu saja! Saya sangat antusias bergabung dengan komunitas pengembang inovatif seperti '
                          'ini.'),
                         ('Nita',
                          'Terima kasih. Kami adalah tim gabungan dari berbagai talenta muda di Asia Tenggara.')]},
  'grammar_point': '### bergabung dengan vs bergabung dalam の前置詞の使い分け\n'
                   '\n'
                   '動詞 bergabung に続く前置詞には微妙なニュアンスの違いがあります：\n'
                   '- **bergabung dengan...**: 「〜（人や組織）に合流する、〜と一緒に加わる（join with）」。\n'
                   '  - 例: *Dia bergabung **dengan** tim riset kami.*（彼は私たちの研究チームに加わった。）\n'
                   '- **bergabung dalam...**: 「〜（枠組み、活動、プロジェクト、組織）の中に所属・参画する（participate in）」。\n'
                   '  - 例: *Indonesia bergabung **dalam** organisasi internasional.*（インドネシアは国際機関に加盟している。）',
  'quiz': [{'q': 'Istilah bahasa Indonesia untuk operasi militer atau SAR yang dilakukan bersama oleh beberapa '
                 'instansi adalah...',
            'options': ['operasi pembagian', 'operasi gabungan', 'operasi penggabung', 'operasi bergabung'],
            'ans': 'operasi gabungan',
            'exp': '複数機関による合同作戦・合同チームは「operasi gabungan / tim gabungan」と言います。'},
           {'q': "Lengkapi kalimat: 'Selamat datang, silakan ... dengan grup diskusi kami di WhatsApp.'",
            'options': ['menggabungkan', 'bergabung', 'penggabungan', 'gabungan'],
            'ans': 'bergabung',
            'exp': '「グループに加わる・参加する」という自動詞命令形なので「bergabung」が正解です。'},
           {'q': 'Proses peleburan dua perusahaan menjadi satu entitas bisnis dalam hukum ekonomi disebut...',
            'options': ['pemisahan usaha', 'penggabungan usaha (merger)', 'pembagian saham', 'pengurangan aset'],
            'ans': 'penggabungan usaha (merger)',
            'exp': '企業の合併（M&A）は公式に「penggabungan usaha」と呼ばれます。'}],
  'column': '### 語源コラム：国営銀行メガマージャー「Bank Mandiri」と「BSI」の誕生劇\n'
            '\n'
            'インドネシアの金融史において、語根 gabung（penggabungan）の金字塔となったのが、1998年のアジア通貨危機後に誕生した「Bank Mandiri」です。破綻寸前だった国営4行（Bank '
            'Bumi Daya, BDN, Bank Ekspor Impor, Bapindo）を統合合併し、国内最大級のメガバンクへと再編しました。\n'
            '\n'
            'さらに2021年には、国営3行のイスラム金融部門が統合され「Bank Syariah Indonesia '
            '(BSI)」が発足しました。「Gabung」は、危機の時代にバラバラの資源を結集して世界と渡り合う強大な力（Sinergi Nasional）を生み出す魔法の言葉なのです。'},
 {'filename': '115-root-kumpul.md',
  'title': '1365. 語根 kumpul の全派生語図鑑（mengumpulkan, berkumpul, perkumpulan, kumpulan）',
  'root': 'kumpul',
  'core_meaning': '集まる、集める、収集する、蓄積する、結集する',
  'explanation': '語根 kumpul は、散らばっていた人や物が一つの場所に「寄り集まる、集積する」というコアを持ちます。家族の団欒（kumpul keluarga）からデータの収集（mengumpulkan '
                 'data）、文芸作品集（kumpulan puisi）、同好会や結社（perkumpulan）まで、コミュニティと集積を象徴する語根です。',
  'matrix': [('mengumpulkan',
              'meN- -kan',
              '他動詞',
              '集める、収集・集約する、募金する',
              'Relawan mengumpulkan donasi pakaian layak pakai bagi pengungsi.'),
             ('dikumpulkan',
              'di- -kan',
              '受動態動詞',
              '集められる、収集される、蓄積される',
              'Sampah anorganik dikumpulkan di bank sampah setiap minggu.'),
             ('berkumpul',
              'ber-',
              '自動詞',
              '集まる、集合する、会合する',
              'Warga desa berkumpul di balai pertemuan untuk bermusyawarah.'),
             ('kumpulan', '-an', '名詞', '集まり、作品集、コレクション、群れ', 'Buku ini memuat kumpulan esai budaya karya penulis muda.'),
             ('perkumpulan',
              'per- -an',
              '名詞',
              '結社、協会、組合、団体、寄り合い',
              'Perkumpulan petani tebu menuntut transparansi harga lelang gula.'),
             ('pengumpulan',
              'peN- -an',
              '名詞',
              '収集作業、集計・データ採取プロセス',
              'Metode pengumpulan data dilakukan melalui wawancara mendalam.'),
             ('terkumpul',
              'ter-',
              '状態動詞',
              '集まった、蓄積された、集約済みである',
              'Dana bantuan yang terkumpul telah disalurkan secara transparan.')],
  'details': [('mengumpulkan',
               '他動詞',
               'ムングンプルカン',
               'お金、ゴミ、情報、人を一つの場所に能動的に「集める・取りまとめる」動作です。',
               'mengumpulkan bukti（証拠を集める）, mengumpulkan tugas（宿題を提出する・集める）, mengumpulkan uang（貯金する・募金する）',
               'Para detektif bekerja siang malam untuk mengumpulkan bukti kejahatan.',
               '刑事たちは犯罪の証拠を収集するために日夜働いた。'),
              ('berkumpul',
               '自動詞',
               'ブルクンプル',
               '人々が自然にまたは約束して「一箇所に集まる・団欒する」動作です。',
               'berkumpul bersama keluarga（家族と一緒に集まる・団欒する）, tempat berkumpul（集合場所・溜まり場）',
               'Keluarga besar kami selalu berkumpul di rumah kakek saat hari raya Idulfitri.',
               '私たちの大家族はレバラン（断食明け大祭）の際、常に祖父の家に集まる。'),
              ('kumpulan',
               '名詞',
               'クンプルラン',
               '詩や短編小説、論文などがまとめられた「〜集・アンソロジー」、または物の集合体を指します。',
               'kumpulan puisi（詩集）, kumpulan cerpen（短編集）, kumpulan dokumen（書類集・ファイル）',
               'Kumpulan cerpen karangan Pramoedya Ananta Toer telah diterjemahkan ke bahasa Jepang.',
               'プラムディヤ・アナンタ・トゥール作の短編集は日本語に翻訳されている。'),
              ('perkumpulan',
               '名詞',
               'プルクンプルラン',
               '共通の目的や趣味を持った人々の「組織・結社・協会（法人格を持つ団体）」を指します。',
               'perkumpulan advokat（弁護士会）, perkumpulan bulu tangkis（バドミントンクラブ）, perkumpulan adat（慣習団体）',
               'Pemerintah memberikan pengesahan hukum bagi perkumpulan nirlaba tersebut.',
               '政府はその非営利社団法人に対して法的な公認を与えた。')],
  'dialogue': {'title': '大学の同窓会とチャリティ基金の設立',
               'lines': [('Fandi', 'Kapan alumni angkatan kita akan berkumpul lagi untuk reuni akbar?'),
                         ('Ratna',
                          'Bulan depan di kampus. Selain silaturahmi, kita berencana mengumpulkan dana beasiswa.'),
                         ('Fandi', 'Luar biasa! Berapa target donasi yang ingin dikumpulkan oleh panitia?'),
                         ('Ratna',
                          'Sekitar seratus juta rupiah. Nanti perkumpulan alumni kita akan mengelolanya secara '
                          'profesional.')]},
  'grammar_point': '### kumpul-kumpul（だべり・気楽な集まり）の文化\n'
                   '\n'
                   '日常会話で非常によく使われるのが、重複語 **kumpul-kumpul** です：\n'
                   '- フォーマルな会議（rapat）や公式行事とは異なり、カフェや路地の屋台で友達同士が「特に用事もなく集まって雑談する・だべる」という温かい親睦行動を指します。\n'
                   '- 例: *Malam minggu ini kita kumpul-kumpul di mana?*（今週の土曜の夜、どこで集まってだべる？）\n'
                   '人と人のつながりを何より重んじるインドネシア文化を象徴する語彙です。',
  'quiz': [{'q': "Istilah bahasa Indonesia untuk '短編集（Short story collection）' adalah...",
            'options': ['perkumpulan cerpen', 'kumpulan cerpen', 'mengumpulkan cerpen', 'pengumpulan cerpen'],
            'ans': 'kumpulan cerpen',
            'exp': '文学の短編集や作品集は「kumpulan cerpen（cerita pendek）」と言います。'},
           {'q': "Lengkapi kalimat: 'Para siswa diminta untuk ... lembar jawaban ujian kepada pengawas.'",
            'options': ['berkumpul', 'mengumpulkan', 'perkumpulan', 'terkumpul'],
            'ans': 'mengumpulkan',
            'exp': '答案用紙を試験官に「集める・提出する」という他動詞なので mengumpulkan が適切です。'},
           {'q': "Apa arti dari 'perkumpulan alumni'?",
            'options': ['Gedung sekolah lama',
                        'Organisasi atau ikatan wadah berkumpulnya para lulusan',
                        'Ujian kelulusan akhir',
                        'Buku tahunan sekolah'],
            'ans': 'Organisasi atau ikatan wadah berkumpulnya para lulusan',
            'exp': 'perkumpulan alumni は卒業生の同窓会・同窓生組織を意味します。'}],
  'column': '### 語源コラム：ジャワの哲学「Mangan Ora Mangan Sing Penting Kumpul」\n'
            '\n'
            'ジャワ社会に古くから伝わる最も有名なことわざの一つが、「Mangan ora mangan sing penting kumpul（食えようが食えまいが、集まっていることが何より大切だ）」です。\n'
            '\n'
            '貧しく食べ物が十分にない時代であっても、家族や村の仲間たちが一箇所に寄り添い、お互いの顔を見つめ合って肩を寄せ合っていれば、どんな苦難も乗り越えられるという集団主義の情愛を表しています。現代の都市化の中でも、週末になると親族一同が狭い居間にぎゅうぎゅう詰めで「Kumpul '
            'Keluarga」を楽しむ光景に、この精神が息づいています。'},
 {'filename': '116-root-pisah.md',
  'title': '1366. 語根 pisah の全派生語図鑑（memisahkan, berpisah, pemisahan, terpisah）',
  'root': 'pisah',
  'core_meaning': '分かれる、分ける、隔離する、分離する、別離・別れ',
  'explanation': '語根 pisah は、一つにくっついていたものや一緒にいた人々を「切り離す、隔離する、別れを告げる」という分離のコアを持ちます。ゴミの分別（memisahkan '
                 'sampah）から愛する人との別離（perpisahan）、三権分立（pemisahan kekuasaan）、地理的な孤立（terpisah jarak）まで、空間的・感情的な距離を描写します。',
  'matrix': [('memisahkan',
              'meN- -kan',
              '他動詞',
              '分ける、引き離す、分別する、隔離する',
              'Petugas memisahkan sampah organik dari sampah plastik.'),
             ('dipisahkan',
              'di- -kan',
              '受動態動詞',
              '分けられる、隔離される、引き離される',
              'Bayi yang baru lahir tidak boleh dipisahkan dari ibunya.'),
             ('berpisah',
              'ber-',
              '自動詞',
              '別れる、離れ離れになる、離婚する',
              'Sahabat karib itu berpisah di bandara dengan penuh haru.'),
             ('perpisahan',
              'per- -an',
              '名詞',
              '別れ、別離、送別会、卒業式',
              'Acara perpisahan sekolah diwarnai isak tangis para siswa.'),
             ('pemisahan',
              'peN- -an',
              '名詞',
              '分離、分別、分割作業、分離独立',
              'Doktrin pemisahan kekuasaan (Trias Politica) menjadi pilar demokrasi.'),
             ('terpisah',
              'ter-',
              '形容詞・状態動詞',
              '離れた、別々の、隔てられた',
              'Keluarga itu tinggal terpisah di dua benua yang berbeda.'),
             ('pemisah',
              'peN-',
              '名詞',
              '仕切り、境界線、隔離帯、分かつもの',
              'Sungai besar itu menjadi pemisah alami antara kedua wilayah.')],
  'details': [('memisahkan',
               '他動詞',
               'ムミサハカン',
               '喧嘩を仲裁して引き離す、物質を分別・抽出する、境界を設けて切り離す動作です。',
               'memisahkan fakta dan opini（事実と意見を分ける）, memisahkan sampah（ゴミを分別する）, memisahkan pertengkaran（喧嘩を止める）',
               'Guru segera melerai dan memisahkan dua siswa yang sedang berkelahi.',
               '教師はすぐに仲裁に入り、喧嘩していた2人の生徒を引き離した。'),
              ('berpisah',
               '自動詞',
               'ブルピサハ',
               '旅立ちや転勤、関係の破綻によって、人がお互いに「別れる・離れ離れになる」動作です。',
               'berpisah selamanya（永遠に別れる・死別する）, berpisah jalan（別々の道を歩む）, berat untuk berpisah（別れが辛い）',
               'Setelah sepuluh tahun bersama, pasangan selebriti itu memutuskan untuk berpisah secara baik-baik.',
               '10年間の結婚生活の後、その有名人カップルは円満に別れる（離婚する）ことを決意した。'),
              ('perpisahan',
               '名詞',
               'プルピサハン',
               '人生の節目における「別れ、送別会、お別れ会」という感情的なイベントや状態を指します。',
               'pesta perpisahan（送別パーティー）, ucapan perpisahan（別れの言葉）, lagu perpisahan（別れの歌）',
               "Lagu 'Kemesraan' kerap dinyanyikan bersama pada akhir malam perpisahan.",
               '送別会の夜のフィナーレには、しばしば名曲『ケメスラアン（親密さ）』が合唱される。'),
              ('terpisah',
               '形容詞・状態動詞',
               'トルピサハ',
               '物理的・空間的に「離れ離れになっている、別個に存在する」状態を表します。',
               'secara terpisah（別個に・個別に）, terpisah oleh samudera（大海によって隔てられた）',
               'Penagihan biaya listrik dan air kini dilakukan secara terpisah melalui tagihan mandiri.',
               '電気代と水道代の請求は現在、独立した請求書を通じて別個に行われている。')],
  'dialogue': {'title': '高校の卒業送別会と未来への旅立ちの約束',
               'lines': [('Adit', 'Tidak terasa ya, malam ini adalah acara perpisahan sekolah kita.'),
                         ('Nadia', 'Iya, Adit. Sangat berat rasanya harus berpisah dengan teman-teman sekelas.'),
                         ('Adit',
                          'Meskipun nanti kita tinggal terpisah di kota-kota yang berbeda, kita harus tetap menjaga '
                          'komunikasi.'),
                         ('Nadia', 'Pasti! Jarak tidak akan pernah bisa memisahkan persahabatan kita.')]},
  'grammar_point': '### pemisahan（能動的作業）vs perpisahan（情緒的別れ）の使い分け\n'
                   '\n'
                   '語根 pisah の接辞対比は、学習者が非常に間違えやすいポイントです：\n'
                   '- **pemisahan**（peN- -an）：人為的な「分離・分別・分割・隔離」という制度的・物理的作業。\n'
                   '  - 例: *pemisahan sampah*（ゴミ分別）, *pemisahan kekuasaan*（三権分立）\n'
                   '- **perpisahan**（per- -an）：人と人の「別離・旅立ち・送別会」という情緒的イベント。\n'
                   '  - 例: *acara perpisahan*（送別会）, *ciuman perpisahan*（別れのキス）\n'
                   '\n'
                   '「三権分立」を perpisahan kekuasaan と言ってしまうと「権力同士の悲しいお別れ会」になってしまうので注意しましょう。',
  'quiz': [{'q': "Istilah hukum tata negara untuk konsep '三権分立（Separation of Powers）' adalah...",
            'options': ['perpisahan kekuasaan', 'pemisahan kekuasaan', 'berpisah kekuasaan', 'terpisah kekuasaan'],
            'ans': 'pemisahan kekuasaan',
            'exp': '政治学・憲法における三権分立は「pemisahan kekuasaan（Trias Politica）」と言います。'},
           {'q': 'Pesta atau acara yang digelar untuk melepas rekan kerja yang pindah kantor disebut...',
            'options': ['acara pemisahan', 'acara perpisahan', 'acara terpisah', 'acara memisahkan'],
            'ans': 'acara perpisahan',
            'exp': '同僚や友人を送り出す送別会・お別れ会は「acara perpisahan」です。'},
           {'q': "Lengkapi kalimat: 'Tagihan kamar dan makanan di hotel ini dihitung secara ...'",
            'options': ['memisahkan', 'terpisah', 'perpisahan', 'pemisah'],
            'ans': 'terpisah',
            'exp': '「別々に、個別に（separately）」という副詞的用法は「secara terpisah」を用います。'}],
  'column': '### 語源コラム：送別会の国民的定番ソング『Kemesraan』の涙\n'
            '\n'
            'インドネシアで送別会（Perpisahan）やキャンプの夜、大学の卒業合宿の最後に必ず全員で肩を組んで歌われる名曲が、イワン・ファルス（Iwan Fals）らが歌った『Kemesraan（親密さ）』です。\n'
            '\n'
            '「Kemesraan ini janganlah cepat '
            'berlalu...（この温かい親密さよ、どうか早く過ぎ去らないでおくれ...）」という切ないサビは、これから別々の街や島へと「Berpisah」していく友への惜別の情を歌い上げています。島々が海で隔てられているからこそ、インドネシア人にとって「別れ」と「再会（Reuni）」は人生で最も感情が高まる瞬間なのです。'},
 {'filename': '117-root-tarik.md',
  'title': '1367. 語根 tarik の全派生語図鑑（menarik, tertarik, ketertarikan, penarikan）',
  'root': 'tarik',
  'core_meaning': '引く、引っ張る、引き出す、惹きつける、興味深い、撤退する',
  'explanation': '語根 tarik は、対象を手元へ「引く・引っ張る」という物理的動作から、銀行口座から預金を「引き出す（tarik tunai）」、心をグッと惹きつける「魅力（daya '
                 'tarik）」や「興味深い（menarik）」、そして軍隊や資金の「引き揚げ・撤退（penarikan）」へと重層的に展開する超重要語根です。',
  'matrix': [('menarik',
              'meN-',
              '他動詞・形容詞',
              '引く、引き出す、惹きつける、面白い・興味深い',
              'Cerita rakyat ini memiliki alur kisah yang sangat menarik.'),
             ('ditarik',
              'di-',
              '受動態動詞',
              '引かれる、回収される、撤退させられる',
              'Produk makanan cacat itu ditarik dari peredaran pasar.'),
             ('tertarik',
              'ter-',
              '状態動詞・形容詞',
              '興味がある、惹きつけられた、魅了された',
              'Banyak investor asing tertarik menanamkan modal di sektor EV.'),
             ('ketertarikan',
              'ke- -an',
              '名詞',
              '関心、興味、惹かれる気持ち',
              'Ketertarikan anak muda terhadap musik indie kian meningkat.'),
             ('penarikan',
              'peN- -an',
              '名詞',
              '出金、引き出し、回収、軍隊撤退プロセス',
              'Penarikan uang tunai dapat dilakukan di seluruh mesin ATM.'),
             ('tarikan',
              '-an',
              '名詞',
              '引っ張り、加速度・吹き上がり、魅力の強さ',
              'Tarikan mesin motor matik ini terasa sangat responsif dan bertenaga.'),
             ('daya tarik',
              'frasa',
              '複合名詞',
              '魅力、アピール力、引力',
              'Keindahan alam bawah laut menjadi daya tarik utama wisata Bali.')],
  'details': [('menarik',
               '他動詞・形容詞',
               'ムナリック',
               'ロープを引っ張る物理動作のほか、形容詞として「面白い、魅力的だ（interesting / attractive）」を表す超頻出語です。',
               'menarik napas（深呼吸する）, cerita yang menarik（面白い話）, menarik perhatian（注目を集める）',
               'Penampilan tarian kontemporer itu sukses menarik perhatian ribuan penonton.',
               'その現代舞踊のパフォーマンスは何千人もの観客の注目を惹きつけることに成功した。'),
              ('tertarik',
               '形容詞・状態動詞',
               'トルタリック',
               '主語が何かの魅力に心奪われ、「〜に興味・関心を持っている（interested in）」状態を表します。',
               'tertarik untuk belajar（学ぶことに興味がある）, tertarik pada seni（芸術に関心がある）',
               'Saya sangat tertarik untuk mempelajari sejarah peradaban kerajaan kuno di Jawa.',
               '私はジャワの古代王国の文明史を学ぶことに極めて強い興味を持っています。'),
              ('penarikan',
               '名詞',
               'プナリカン',
               'ATMでの出金（penarikan tunai）、市場からの商品回収（penarikan produk/recall）、軍隊の撤収を指します。',
               'penarikan tunai（現金引き出し）, penarikan pasukan（軍隊の撤収）, batas penarikan harian（1日の出金限度額）',
               'Biaya penarikan dana antarbank telah disesuaikan dengan regulasi baru.',
               '銀行間出金手数料は新規則に合わせて調整された。'),
              ('daya tarik',
               '名詞句',
               'ダヤ タリック',
               '観光地、商品、人物が持っている「人を惹きつけるパワー・魅力」そのものを指します。',
               'daya tarik wisata（観光の魅力）, memiliki daya tarik tersendiri（独自の魅力を持つ）',
               'Keramahan penduduk lokal menjadi daya tarik utama yang membuat turis betah.',
               '地元住民の温かい人柄は、観光客を居心地良くさせる最大の魅力となっている。')],
  'dialogue': {'title': '銀行ATMでの現金引き出しと新しい投資信託の相談',
               'lines': [('Hadi', 'Apakah Anda tahu lokasi mesin ATM terdekat untuk penarikan uang tunai?'),
                         ('Ria',
                          'Ada di lobi depan, Pak. Ngomong-ngomong, brosur investasi reksa dana di meja Anda tampak '
                          'sangat menarik.'),
                         ('Hadi', 'Iya, saya memang sedang tertarik untuk berinvestasi di instrumen hijau.'),
                         ('Ria',
                          'Pilihan yang bagus! Instrumen tersebut memiliki daya tarik berupa dividen yang stabil.')]},
  'grammar_point': '### menarik（面白い・魅力的）vs tertarik（興味がある）の主語の使い分け\n'
                   '\n'
                   "英語の 'interesting' と 'interested' の対比と全く同じ構造です：\n"
                   '- **menarik**（-ing）: 物や出来事が主語。「人を惹きつける性質がある」。\n'
                   '  - 例: *Buku ini sangat **menarik**.*（この本はとても面白い。）\n'
                   '- **tertarik**（-ed）: 人が主語。「〜に興味・関心をそそられている」。\n'
                   '  - 例: *Saya **tertarik** pada buku ini.*（私はこの本に興味があります。）\n'
                   '\n'
                   '*Saya menarik* と言うと「私は魅力的な人間です」という自慢になってしまうので、「私は興味があります」と言いたい時は必ず **Saya tertarik** と言いましょう。',
  'quiz': [{'q': "Bagaimana cara mengatakan '私はインドネシアの歴史に興味があります' secara tepat?",
            'options': ['Saya menarik sejarah Indonesia.',
                        'Saya tertarik dengan sejarah Indonesia.',
                        'Sejarah Indonesia tertarik saya.',
                        'Penarikan saya pada sejarah Indonesia.'],
            'ans': 'Saya tertarik dengan sejarah Indonesia.',
            'exp': '人が主語で「〜に関心がある」ときは「Saya tertarik dengan / pada...」を用います。'},
           {'q': 'Fitur di mesin ATM untuk mengambil uang tunai bertuliskan...',
            'options': ['Penarikan Tunai', 'Ditarik Tunai', 'Menarik Tunai', 'Tarikan Tunai'],
            'ans': 'Penarikan Tunai',
            'exp': 'ATMの現金引き出しボタンには「Penarikan Tunai（Cash Withdrawal）」と表示されます。'},
           {'q': "Ungkapan 'menarik napas panjang' memiliki arti...",
            'options': ['Menahan napas di dalam air',
                        'Menghela atau menghirup napas dalam-dalam',
                        'Berhenti bernapas',
                        'Berbicara sangat cepat'],
            'ans': 'Menghela atau menghirup napas dalam-dalam',
            'exp': 'menarik napas panjang は「深く息を吸い込む、深呼吸する、ため息をつく」という意味です。'}],
  'column': '### 語源コラム：独立記念日の伝統綱引き競技「Tarik Tambang」\n'
            '\n'
            '8月17日のインドネシア独立記念日（Hari Kemerdekaan）になると、国中の広場や路地裏で爆笑と歓声とともに開催される伝統競技が「Tarik Tambang（綱引き）」です。\n'
            '\n'
            '太いヤシ繊維のロープ（Tambang）を町内対抗の二チームが泥まみれになって全力で「Tarik! '
            'Tarik!（引け！引け！）」と引き合います。個人技ではなく、チーム全員の呼吸（Irama）と踏ん張り（Pijakan '
            'Kaki）が一致した瞬間に勝利が訪れるこの競技は、独立闘争を勝ち抜いた国民の助け合いと団結のメタファーとして今も深く愛されています。'},
 {'filename': '118-root-dorong.md',
  'title': '1368. 語根 dorong の全派生語図鑑（mendorong, dorongan, pendorong, terdorong）',
  'root': 'dorong',
  'core_meaning': '押す、押し出す、推進する、後押しする、動機づける、駆り立てる',
  'explanation': '語根 dorong は、物体に力を加えて前方へ「押す」という物理動作から、政策を力強く「推進する（mendorong '
                 'kebijakan）」、人の背中を「後押しする・励ます」、心の内面から湧き出る「衝動・動機（dorongan）」まで、前進するエネルギーの源泉を表現する語根です。',
  'matrix': [('mendorong',
              'meN-',
              '他動詞',
              '押す、推進する、促進する、動機づける',
              'Pemerintah terus mendorong pertumbuhan industri kreatif lokal.'),
             ('didorong',
              'di-',
              '受動態動詞',
              '押される、推進される、促される',
              'Perekonomian nasional didorong oleh konsumsi domestik yang kuat.'),
             ('dorongan', '-an', '名詞', '推進力、後押し、刺激、衝動、激励', 'Dorongan moral dari keluarga menjadi kunci kesuksesannya.'),
             ('pendorong',
              'peN-',
              '名詞',
              '推進役、動機、起爆剤、推進力となる要素',
              'Ekspor komoditas unggulan menjadi faktor pendorong ekonomi.'),
             ('terdorong',
              'ter-',
              '状態動詞',
              '駆り立てられた、思わず促された、押された',
              'Dia terdorong untuk membantu setelah melihat penderitaan korban.'),
             ('gerobak dorong',
              'frasa',
              '名詞句',
              '手押し車、屋台カート',
              'Pedagang bakso keliling menjajakan dagangannya dengan gerobak dorong.'),
             ('mendorong maju',
              'frasa',
              '動詞句',
              '前進させる、躍進を後押しする',
              'Inovasi teknologi mendorong maju peradaban manusia.')],
  'details': [('mendorong',
               '他動詞',
               'ムンドロン',
               '故障した車を押す物理動作から、経済成長を促進する、人をやる気にさせる際に多用されます。',
               'mendorong pertumbuhan ekonomi（経済成長を後押しする）, mendorong inovasi（イノベーションを促す）, mendorong mobil（車を押す）',
               'Bank sentral menurunkan suku bunga untuk mendorong penyaluran kredit perbankan.',
               '中央銀行は銀行融資を促進するために政策金利を引き下げた。'),
              ('dorongan',
               '名詞',
               'ドロンガン',
               '物理的な推進力のほか、心の内側から突き動かす「衝動」や周囲からの「後押し・励まし」を指します。',
               'dorongan moral（道徳的・精神的後押し）, dorongan batin（内面からの衝動）, faktor dorongan（プッシュ要因）',
               'Berkat dorongan semangat dari orang tua, ia berhasil meraih gelar doktor.',
               '両親からの精神的な励ましのおかげで、彼は博士号を取得することに成功した。'),
              ('pendorong',
               '名詞',
               'プンドロン',
               '成長や変化を力強く牽引する「主たる推進力、アクセル役、駆動力」を指す論説用語です。',
               'faktor pendorong（推進要因・促進因子）, motor pendorong（推進モーター・原動力）',
               'Sektor konsumsi rumah tangga tetap menjadi pendorong utama ekonomi kuartal ini.',
               '家計消費部門は今四半期も依然として経済の主要な推進役であり続けている。'),
              ('terdorong',
               '形容詞・状態動詞',
               'トルドロン',
               '義務感や慈悲心、情熱によって「内面から思わず突き動かされた、駆り立てられた」状態を表します。',
               'terdorong oleh rasa iba（同情心に駆り立てられて）, terdorong oleh ambisi（野心に動かされて）',
               'Banyak dokter muda terdorong untuk mengabdi di pelosok daerah terpencil.',
               '多くの若い医師たちが、遠隔僻地で奉仕活動を行いたいという思いに駆り立てられた。')],
  'dialogue': {'title': '若手起業家へのスタートアップ助成金とメンターシップ',
               'lines': [('Arif',
                          'Bagaimana program inkubasi bisnis ini dapat mendorong pertumbuhan usaha rintisan kita?'),
                         ('Maya',
                          'Program ini memberikan mentoring intensif dan dorongan modal awal yang sangat kita '
                          'butuhkan.'),
                         ('Arif',
                          'Luar biasa. Apa faktor pendorong utama yang membuatmu berani mendirikan startup ini?'),
                         ('Maya',
                          'Saya terdorong oleh keinginan kuat untuk menyelesaikan masalah logistik di desa-desa '
                          'terpencil.')]},
  'grammar_point': '### 成句 faktor pendorong（推進要因）vs faktor penarik（誘引要因）\n'
                   '\n'
                   '経済学、地理学、社会学の人口移動論などでペアとして頻出する専門コロケーションです：\n'
                   '- **faktor pendorong (push factors)**: 貧困、災害、失業など、人を元の場所から「押し出す」要因。\n'
                   '- **faktor penarik (pull factors)**: 高賃金、充実した教育、娯楽など、人を都市へ「引きつける（語根 tarik）」要因。\n'
                   '\n'
                   'インドネシア語の学術論説において、dorong と tarik が見事な対比の概念ペアを形成しています。',
  'quiz': [{'q': "Kata mana yang paling tepat untuk melengkapi: 'Inovasi digital menjadi faktor ... utama industri "
                 "kreatif.'?",
            'options': ['dorongan', 'pendorong', 'terdorong', 'mendorongkan'],
            'ans': 'pendorong',
            'exp': '名詞を修飾して「推進要因」とする定型フレーズは「faktor pendorong」です。'},
           {'q': "Lengkapi kalimat: 'Melihat anak itu menangis kelaparan, hatinya ... untuk membelikan makanan.'",
            'options': ['mendorong', 'terdorong', 'pendorong', 'dorongan'],
            'ans': 'terdorong',
            'exp': '同情心によって「思わず心が突き動かされた」という受け身・自発状態なので terdorong が適切です。'},
           {'q': "Lawan kata atau pasangan konsep dari 'faktor pendorong' dalam teori migrasi adalah...",
            'options': ['faktor penarik', 'faktor pembagi', 'faktor pemisah', 'faktor pelepas'],
            'ans': 'faktor penarik',
            'exp': 'プッシュ要因（faktor pendorong）と対になるプル要因は「faktor penarik」です。'}],
  'column': '### 語源コラム：教育の父キ・ハジャル・デワンタラの金言「Tut Wuri Handayani」\n'
            '\n'
            'インドネシア教育文化省の公式ロゴマークに刻まれている国是の教育標語が、古代ジャワ語の金言「Tut Wuri Handayani」です。現代インドネシア語に訳すと「Dari belakang memberikan '
            'dorongan（後ろから後押し・支援を与える）」という意味です。\n'
            '\n'
            '指導者や教師は、常に前で偉そうに引っ張るのではなく、時には先頭に立ち（Ing ngarsa sung tulada）、時には真ん中で共に汗を流し（Ing madya mangun '
            'karsa）、そして最後方から生徒たちの自立を優しく力強く後押しする（Tut wuri '
            'handayani）存在であるべきだという、インドネシアの尊い教育精神の核心がこの「Dorongan（後押し）」に込められています。'},
 {'filename': '119-root-angkat.md',
  'title': '1369. 語根 angkat の全派生語図鑑（mengangkat, pengangkatan, angkatan, terangkat）',
  'root': 'angkat',
  'core_meaning': '持ち上げる、引き上げる、任命する、世代、軍隊、出発する',
  'explanation': '語根 angkat は、重いものを下から上へ「持ち上げる、引き上げる」という物理動作から、人を重職に「登用・任命する（mengangkat '
                 'pejabat）」、電話の受話器を「取る（mengangkat telepon）」、同世代の集団（angkatan）、そして国を守る軍隊（Angkatan '
                 'Bersenjata/TNI）へと雄大に意味を展開する重要語根です。',
  'matrix': [('mengangkat',
              'meN-',
              '他動詞',
              '持ち上げる、任命する、取り上げる、引き受ける',
              'Presiden resmi mengangkat duta besar baru untuk Jepang.'),
             ('diangkat',
              'di-',
              '受動態動詞',
              '持ち上げられる、任命・登用される、養子にされる',
              'Dia diangkat menjadi anak asuh oleh keluarga dermawan itu.'),
             ('angkatan',
              '-an',
              '名詞',
              '軍隊・軍種、同窓・同期、世代、文学世代',
              'Angkatan Bersenjata Republik Indonesia siap menjaga kedaulatan.'),
             ('pengangkatan',
              'peN- -an',
              '名詞',
              '任命、登用、引き上げ作業、就任式',
              'Proses pengangkatan pegawai negeri sipil dilakukan melalui seleksi ketat.'),
             ('berangkat',
              'ber-',
              '自動詞',
              '出発する、旅立つ、〜を起点とする',
              'Kereta cepat Whoosh berangkat dari Stasiun Halim tepat pukul delapan.'),
             ('terangkat',
              'ter-',
              '形容詞・状態動詞',
              '持ち上げられた、名誉が回復した、向上した',
              'Derajat keluarganya terangkat berkat kesuksesan sang anak.'),
             ('angkat bicara',
              'frasa',
              '成句',
              '口を開く、公に発言する、声を上げる',
              'Tokoh masyarakat akhirnya angkat bicara mengenai kasus korupsi tersebut.')],
  'details': [('mengangkat',
               '他動詞',
               'ムナンカット',
               '荷物を持ち上げる動作のほか、官職に任命する（mengangkat menteri）、議題を取り上げる（mengangkat tema）際に使われます。',
               'mengangkat beban（荷物を持ち上げる）, mengangkat tema budaya（文化テーマを取り上げる）, mengangkat tangan（挙手する）',
               'Para jurnalis mengangkat isu krisis lingkungan dalam laporan investigasi mereka.',
               'ジャーナリストたちは調査報道の中で環境危機の問題を取り上げた。'),
              ('angkatan',
               '名詞',
               'アンカタン',
               '軍隊の軍種（陸・海・空軍）や、学校の「〜期生・同期（angkatan 2024）」、文学史の「〜年代派」を指します。',
               'Angkatan Darat (TNI AD)（陸軍）, Angkatan Laut (TNI AL)（海軍）, teman seangkatan（同期生）',
               'Budi bertemu kembali dengan teman-teman seangkatan saat reuni akbar kampus.',
               'ブディは大学の大同窓会で同期の友人たちと再会した。'),
              ('berangkat',
               '自動詞',
               'ブランカット',
               '乗り物や人が「出発する・旅立つ」基本動詞です。比喩的に「〜を原点とする（berangkat dari...）」としても使われます。',
               'jam keberangkatan（出発時刻）, berangkat kerja（出勤する）, berangkat dari niat baik（善意から出発する）',
               'Pesawat kami dijadwalkan berangkat menuju Denpasar sore hari.',
               '私たちの飛行機は夕方にデンパサールへ向けて出発する予定です。'),
              ('angkat tangan',
               '成句',
               'アンカット タンガン',
               '文字通りの「挙手する」動作と、比喩的な「降参する、お手上げだ（give up）」の二重の意味を持ちます。',
               'angkat tangan（手を挙げる / 降伏・お手上げになる）, angkat kaki（立ち退く・逃げ出す）, angkat topi（脱帽する・敬意を表す）',
               'Dokter sudah angkat tangan menghadapi komplikasi penyakit yang amat parah itu.',
               '医師はその極めて深刻な病気の合併症にお手上げ状態となった（匙を投げた）。')],
  'dialogue': {'title': '新役員の就任式典と同期の出世の祝福',
               'lines': [('Hendra', 'Selamat atas pengangkatanmu sebagai direktur operasional baru!'),
                         ('Wahyu',
                          'Terima kasih banyak, Hendra. Tanggung jawab ini sangat berat, tapi saya siap mengangkat '
                          'performa perusahaan.'),
                         ('Hendra',
                          'Kami sangat bangga. Kamu adalah alumni angkatan 2010 pertama yang menjadi direksi.'),
                         ('Wahyu',
                          'Ini semua berkat dukungan kalian. Besok pagi saya harus berangkat ke kantor cabang luar '
                          'kota.')]},
  'grammar_point': '### 成句 angkat bicara（公に口を開く、声を上げる）\n'
                   '\n'
                   '報道やニュース論説で日常的に見かける格調高い慣用句です：\n'
                   '- これまで沈黙を守っていた要人や被害者が「公の場で発言する、沈黙を破って声を上げる（speak up / voice opinion）」ことを意味します。\n'
                   '- 例: *Presiden akhirnya **angkat bicara** menanggapi isu kenaikan pajak.*（大統領は増税問題に対応してついに口を開いた。）\n'
                   '反対に沈黙を守ることは **tutup mulut** と表現されます。',
  'quiz': [{'q': "Apa arti dari frasa 'teman seangkatan'?",
            'options': ['Teman yang suka mengangkat barang',
                        'Teman satu angkatan / teman satu tahun kelulusan/masuk (peers)',
                        'Anggota tentara aktif',
                        'Supir bus antarprovinsi'],
            'ans': 'Teman satu angkatan / teman satu tahun kelulusan/masuk (peers)',
            'exp': 'teman seangkatan は「同期生・同じ学年・期（peers）」を意味します。'},
           {'q': 'Upacara resmi untuk meresmikan pejabat baru pada posisinya disebut...',
            'options': ['pemberangkatan pejabat', 'pengangkatan pejabat', 'angkatan pejabat', 'terangkatnya pejabat'],
            'ans': 'pengangkatan pejabat',
            'exp': '高官や役員の任命・就任は「pengangkatan pejabat」と言います。'},
           {'q': "Ungkapan 'angkat tangan' dalam situasi sulit memiliki makna...",
            'options': ['Merayakan kemenangan',
                        'Menyerah / mengaku kalah (surrender/give up)',
                        'Memanggil taksi di jalan',
                        'Menari bersama teman'],
            'ans': 'Menyerah / mengaku kalah (surrender/give up)',
            'exp': 'angkat tangan は「降参する、お手上げである、匙を投げる」という意味の成句です。'}],
  'column': '### 語源コラム：インドネシア文学史を刻む「Angkatan 45（45年派）」\n'
            '\n'
            'インドネシアの文化・思想史において、「Angkatan」という単語は世代ごとの文学運動を指す記念碑的な言葉です。\n'
            '\n'
            '特に詩人チェアリル・アンワル（Chairil Anwar）らが牽引した「Angkatan '
            '45（1945年派）」は、植民地時代の伝統的な韻律や装飾的文体をかなぐり捨て、独立の戦火の中で生の叫びを叩きつける近代インドネシア文学の爆発を生み出しました。「Aku ini binatang jalang '
            'dari kumpulannya terbuang（我は群れを追われた野良犬）」という彼の詩句は、新しい時代を持ち上げ（mengangkat）、切り拓く若者の熱情を象徴しています。'},
 {'filename': '120-root-turun.md',
  'title': '1370. 語根 turun の全派生語図鑑（menurunkan, penurunan, keturunan, menurun）',
  'root': 'turun',
  'core_meaning': '下りる、下落する、低下する、引き下げる、子孫・世襲・伝統',
  'explanation': '語根 turun '
                 'は、高所から低所へ「下りる、降下する」という基本動作から、物価や気温の「下落・低下（penurunan）」、病状の悪化（menurun）、そして先祖から子孫へと受け継がれる「血統・遺伝（keturunan）」や「代々の伝統（turun-temurun）」まで、極めて豊饒な多義性を持つ語根です。',
  'matrix': [('menurunkan',
              'meN- -kan',
              '他動詞',
              '降ろす、引き下げる、低下させる、継承させる',
              'Pemerintah berupaya menurunkan harga beras di pasar.'),
             ('diturunkan',
              'di- -kan',
              '受動態動詞',
              '降ろされる、引き下げられる、啓示される',
              'Kitab suci diturunkan sebagai petunjuk hidup umat manusia.'),
             ('menurun',
              'meN-',
              '自動詞・形容詞',
              '下がる、減少・低下する、坂を下る、遺伝する',
              'Kondisi kesehatan pasien berangsur-angsur menurun hari ini.'),
             ('penurunan',
              'peN- -an',
              '名詞',
              '低下、減少、下落、下り坂',
              'Penurunan angka kemiskinan menjadi prioritas utama pembangunan.'),
             ('keturunan',
              'ke- -an',
              '名詞',
              '子孫、血統、家系、遺伝',
              'Dia merupakan keturunan langsung dari pahlawan nasional Pangeran Diponegoro.'),
             ('turun-temurun',
              'kata ulang',
              '形容詞・副詞',
              '代々、世々、先祖代々受け継がれた',
              'Resep ramuan jamu ini diwariskan secara turun-temurun.'),
             ('turun tangan',
              'frasa',
              '成句',
              '自ら介入する、直接手を差し伸べる',
              'Presiden turun tangan langsung menyelesaikan sengketa agraria warga.')],
  'details': [('menurunkan',
               '他動詞',
               'ムヌルンカン',
               '車から荷物や人を降ろす動作のほか、物価を引き下げる、旗を降納する際に使われます。',
               'menurunkan harga（値下げする）, menurunkan berat badan（体重を落とす）, menurunkan bendera（国旗を降納する）',
               'Dokter menyarankan pasien berolahraga untuk menurunkan kadar kolesterol jahat.',
               '医師は悪玉コレステロール値を下げるために患者に運動を勧めた。'),
              ('menurun',
               '自動詞・形容詞',
               'ムヌルン',
               '品質や健康状態、成績などが他動的ではなく「悪化する・下がる」、または坂道が下っている状態です。',
               'prestasi menurun（成績が落ちる）, jalanan menurun（下り坂）, sifat yang menurun（遺伝した性質）',
               'Tekanan darah penderita hipertensi itu mulai menurun setelah istirahat cukup.',
               '高血圧患者の血圧は、十分な休息を取った後に下がり始めた。'),
              ('penurunan',
               '名詞',
               'プヌルンガン',
               '数値や比率の「低下・減少現象」、または坂道の「下り坂部分」を指します。',
               'penurunan suku bunga（利下げ）, penurunan muka tanah（地盤沈下）, penurunan omzet（売上減少）',
               'Penurunan angka stunting pada balita menunjukkan kemajuan program kesehatan.',
               '幼児の発育阻害（低身長）率の低下は、保健プログラムの進展を示している。'),
              ('keturunan',
               '名詞',
               'クトゥルナン',
               '生物学的な「子孫、血統、家系」を指し、多民族社会のインドネシアでルーツを語る頻出語です。',
               'keturunan Tionghoa（中華系インドネシア人）, garis keturunan ibu（母系血統）, tidak memiliki keturunan（子どもがいない）',
               'Masyarakat keturunan Arab telah berbaur harmonis selama berabad-abad di pesisir Jawa.',
               'アラブ系の人々はジャワ沿岸で何世紀にもわたり調和して溶け込んできた。')],
  'dialogue': {'title': 'インフレ抑制と物価引き下げに向けた市場介入',
               'lines': [('Bambang',
                          'Bagaimana langkah pemerintah untuk menurunkan harga kebutuhan pokok menjelang lebaran?'),
                         ('Kartika',
                          'Kementerian Perdagangan menggelar operasi pasar murah guna mendorong penurunan harga beras '
                          'dan minyak goreng.'),
                         ('Bambang', 'Apakah upaya tersebut berhasil? Tampaknya daya beli masyarakat sempat menurun.'),
                         ('Kartika',
                          'Syukurlah, harga mulai stabil kembali sehingga tradisi belanja turun-temurun warga tetap '
                          'berjalan semarak.')]},
  'grammar_point': '### 成句 turun tangan（自ら介入する）の重み\n'
                   '\n'
                   '語根 turun を用いた最重要成句が **turun tangan（自ら手を下す、直接介入する、救いの手を差し伸べる）** です：\n'
                   '- リーダーや高官が、部下に任せきりにせず「自ら現場に足を運んで問題を解決する（intervene directly）」という能動的で称賛される姿勢を表します。\n'
                   '- 例: *Menteri Keuangan **turun tangan** mengatasi keluhan wajib '
                   'pajak.*（財務大臣は納税者の苦情を解決するため自ら乗り出した。）\n'
                   'これと対比されるのが、前述の **lepas tangan（無責任に手を引く・責任逃れする）** です。',
  'quiz': [{'q': "Apa arti dari frasa 'diwariskan secara turun-temurun'?",
            'options': ['Dijual dengan harga murah di pasar loak',
                        'Diwariskan dari generasi ke generasi / secara turun-temurun',
                        'Dibuang ke sungai karena sudah rusak',
                        'Dilarang digunakan oleh pemerintah'],
            'ans': 'Diwariskan dari generasi ke generasi / secara turun-temurun',
            'exp': 'turun-temurun は「代々、先祖代々、世代から世代へ（generation to generation）」という意味です。'},
           {'q': "Lengkapi kalimat: 'Pemerintah berjanji akan ... tarif listrik untuk pelanggan industri kecil.'",
            'options': ['menurunkan', 'penurunan', 'keturunan', 'turun-temurun'],
            'ans': 'menurunkan',
            'exp': '「電気料金を引き下げる」という他動詞なので menurunkan が正解です。'},
           {'q': 'Sikap pejabat yang terjun langsung ke lapangan membantu masyarakat yang kesulitan disebut...',
            'options': ['turun tangan', 'lepas tangan', 'tangan dingin', 'panjang tangan'],
            'ans': 'turun tangan',
            'exp': '自ら現場に介入して手を差し伸べるリーダーシップは「turun tangan」と呼びます。'}],
  'column': '### 語源コラム：天から降る恵みの雨「Turun Hujan」と神の啓示「Turun Wahyu」\n'
            '\n'
            'インドネシア語において、雨が降ることは「Hujan turun」または「Turun hujan」と表現されます。\n'
            '\n'
            '熱帯の灼熱の大地にとって、天から水が降り注ぐことは生きとし生けるものへの最大の神の恩寵（Berkah）です。また、イスラム教において聖典コーランが預言者ムハンマドに初めて啓示された夜の記念日は「Nuzulul '
            'Quran（コーラン降臨祭）」と呼ばれ、インドネシア語では「Malam turunnya '
            'Al-Quran」と表現されます。「Turun」という言葉には、天の高い場所から人間界へと注がれる神聖な恵みや啓示の響きが込められているのです。'}]

def generate_markdown(a):
    md = []
    md.append(f"# {a['title']}\n")
    md.append(f'<span class="badge badge-derivations">語根派生語</span> <span class="badge badge-vocabulary">語彙拡張</span> <span class="badge badge-intermediate">中級文法</span>\n')
    md.append(f"- **対象語根**: `{a['root']}`")
    md.append(f"- **コアの意味**: {a['core_meaning']}")
    md.append(f"- **CEFRレベル**: A2-B2 (初中級〜中上級)")
    md.append(f"- **読了目安**: 12分\n")
    md.append("---\n")
    
    md.append("## 語根のコアミーニングと概念展開\n")
    md.append(f"{a['explanation']}\n")
    
    md.append("## 派生語一覧マトリックス\n")
    md.append("| 派生語 | 接辞パターン | 品詞 | 日本語義 | 基本例文 |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for word, aff, pos, meaning, ex in a["matrix"]:
        md.append(f"| **{word}** | `{aff}` | {pos} | {meaning} | {ex} |")
    md.append("\n")
    
    md.append("## 主要派生語の精密解説と例文カード\n")
    for word, pos, kana, desc, coloc, id_ex, ja_ex in a["details"]:
        md.append(f"### {word}（{pos}）\n")
        md.append(f"**カタカナ発音**: {kana}  \n")
        md.append(f"**語法とニュアンス**: {desc}  \n")
        md.append(f"**重要コロケーション**: `{coloc}`\n")
        md.append(f'<div class="id-example">\n')
        md.append(f"**インドネシア語例文**: {id_ex}  \n")
        md.append(f"**日本語訳**: {ja_ex}\n")
        md.append("</div>\n")
    
    md.append("## 実践会話ダイアログ（Dialogue）\n")
    md.append(f"**シチュエーション**: {a['dialogue']['title']}\n")
    md.append('<div class="dialogue-box">\n')
    for speaker, line in a["dialogue"]["lines"]:
        md.append(f"**{speaker}**: \"{line}\"  \n")
    md.append("</div>\n")
    
    md.append("## 接辞の使い分け・文法比較のポイント\n")
    md.append(f"{a['grammar_point']}\n")
    
    md.append("## 定着確認チェッククイズ（3問）\n")
    for i, q in enumerate(a["quiz"], 1):
        md.append(f"**Q{i}. {q['q']}**\n")
        for opt in q["options"]:
            md.append(f"- {opt}")
        md.append("\n")
        md.append(f'<details>\n<summary>正解と解説を見る</summary>\n<div class="answer-box">\n')
        md.append(f"**正解**: 「**{q['ans']}**」\n")
        md.append(f"**解説**: {q['exp']}\n")
        md.append("</div>\n</details>\n")
    
    md.append("## 語源・文化コラム\n")
    md.append(f"{a['column']}\n")
    
    md.append("---\n")
    md.append("## 次の学習ステップ・関連リンク\n")
    md.append("- [総合サイトマップ](../sitemap.md)")
    md.append("- [トップページ](../index.md)\n")
    
    return "\n".join(md)

def main():
    target_dir = os.path.join("docs", "derivations-2")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        fpath = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {fpath}")

if __name__ == "__main__":
    main()

