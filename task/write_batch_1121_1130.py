# -*- coding: utf-8 -*-
import os
import re

articles_data = [
    {
        "slug": "21-slang-contraction-habits",
        "title": "【二重言語】短縮造語（Akronim Gaul）の形成ルール：mager, baper, pansos, bucin, curcol",
        "intro": "インドネシアの若者カルチャーは、2つの単語を合体させて2音節のキャッチーな短縮語（Akronim）を作る天才です。「mager（malas gerak = めんどくさい）」「baper（bawa perasaan = 感情的になる）」「bucin（budak cinta = 恋の奴隷）」など、日常会話に溶け込む必須造語を完全マスターします。",
        "pairs": [
            ("malas bergerak (動くのが億劫だ)", "mager", "ダラダラしたい、面倒くさい"),
            ("bawa perasaan (感情を挟みすぎる)", "baper", "真に受ける、傷つきやすい"),
            ("panjat sosial (社会的知名度を狙う)", "pansos", "SNSで売名・知名度狙い"),
            ("curhat colongan (隙を見て愚痴る)", "curcol", "どさくさ紛れの身の上相談")
        ],
        "drill": [
            ("【Baku→Gaul】外出するのが億劫です。（Saya malas bergerak untuk keluar rumah.）", "Lagi mager bgt nih mau keluar.", "ラギ マゲル バンゲット ニ マウ クルアル", "mager ⇄ malas bergerak。"),
            ("【Gaul→Baku】そんなに真に受けないで。（Jangan baper dong, cuma guyon.）", "Mohon jangan memasukkan lelucon ini ke dalam hati.", "モホン ジャンガン ムマスッカン ルルチョン イニ ク ダラム ハティ", "baper ⇄ bawa perasaan。"),
            ("【Baku→Gaul】彼女は恋に盲目になっている。（Dia sangat diperbudak oleh cinta.）", "Dia bucin parah sama cowoknya.", "ディア ブチン パラ サマ チョウォッニャ", "bucin ⇄ budak cinta。"),
            ("【Gaul→Baku】どさくさに紛れて愚痴っちゃった。（Malah curcol gue jadinya.）", "Akhirnya saya justru menceritakan masalah pribadi secara tidak sengaja.", "アキールニャ サヤ ジュストゥル ムンチュリタカン マサラ プリバディ スチャラ ティダッ スンガジャ", "curcol ⇄ curhat colongan。"),
            ("【Baku→Gaul】ただの売名行為だよ。（Hanya tindakan untuk panjat sosial.）", "Cuma pansos doang tuh orang.", "チュマ パンソス ドアン トゥ オラン", "pansos ⇄ panjat sosial。"),
            ("【Gaul→Baku】暇でやることがない。（Lagi gabut nih, nggak ada kerjaan.）", "Saya sedang memiliki banyak waktu luang tanpa ada kegiatan.", "サヤ スダン ムミリキ バニャッ ワクトゥ ルアン タンパ アダ クギアタン", "gabut ⇄ gaji buta / tidak ada kegiatan。"),
            ("【Baku→Gaul】見せびらかさないで。（Jangan suka pamer barang mahal.）", "Jangan suka flexing dong di medsos.", "ジャンガン スカ フレクシング ドン ディ メドソス", "flexing ⇄ pamer。"),
            ("【Gaul→Baku】あいつ、本当にケチだな。（Pelit bgt tuh orang, pelici.）", "Orang tersebut sangat kikir sekali.", "オラン トゥルスブット サンガット キキル スカリ", "pelit ⇄ kikir。"),
            ("【Baku→Gaul】恥ずかしくてたまらない。（Merasa sangat malu sekali.）", "Cringe bgt liat kelakuannya.", "クリンジ バンゲット リアット クラクアンニャ", "cringe ⇄ malu melihatnya。"),
            ("【Gaul→Baku】かっこつけすぎだよ。（Jangan sok jaim deh lu!）", "Jangan terlalu berusaha menjaga citra diri secara berlebihan.", "ジャンガン トゥルラル ブルウサハ メンジャガ チトラ ディリ スチャラ ブルレビハン", "jaim ⇄ jaga image。"),
            ("【Baku→Gaul】気分屋で困る。（Sifatnya berubah-ubah mengikuti suasana hati.）", "Moodyan bgt orangnya.", "ムーディアン バンゲット オランニャ", "moody ⇄ berubah-ubah。"),
            ("【Gaul→Baku】彼、本当にイケメン！（Cakep bgt cowoknya, cogan!）", "Pria tersebut memiliki paras yang sangat tampan.", "プリア トゥルスブット ムミリキ パラス ヤン サンガット タンパン", "cogan ⇄ cowok ganteng。"),
            ("【Baku→Gaul】美女に目がない。（Sangat tertarik pada wanita cantik.）", "Suka liat cewek cici cecan.", "スカ リアット チェウェッ チチ チェチャン", "cecan ⇄ cewek cantik。"),
            ("【Gaul→Baku】もうこれ以上我慢できない。（Udah ilfeel gue sama dia.）", "Saya sudah kehilangan rasa simpati dan rasa hormat.", "サヤ スダ クヒランガン ラサ スィンパティ ダン ラサ ホルマット", "ilfeel ⇄ hilang feeling。"),
            ("【Baku→Gaul】ただの口先だけ。（Hanya pandai berbicara tanpa tindakan.）", "Omdo doang dia mah, nggak ada bukti.", "オムド ドアン ディア マ、ンガッ アダ ブクティ", "omdo ⇄ omong doang。")
        ],
        "quiz": [
            ("若者スラング「mager」の元の2つの単語は？", ["malas gerak (動くのが面倒)", "makan burger", "malam gelap", "main gitar"], 1),
            ("冗談を言われた人が真に受けてムッとした時に「Jangan ...」と言う語は？", ["baper (bawa perasaan)", "mager", "pansos", "bucin"], 1),
            ("「口先だけで行動が伴わない（ビッグマウス）」を表すスラングは？", ["omdo (omong doang)", "baper", "gabut", "curcol"], 1)
        ]
    },
    {
        "slug": "22-work-formal-email-to-wa",
        "title": "【二重言語】ビジネス文書 ⇄ 社内チャット変換：メール文体を同僚向けSlack/WAに変換",
        "intro": "インドネシアの職場では、顧客や経営陣宛ての「公式ビジネスメール（Bahasa Baku）」と、同僚同士の「社内チャット（Slack / WhatsApp）」で劇的なコードスイッチングが行われます。同じ案件をいかに適切にレジスター変換するかを訓練します。",
        "pairs": [
            ("Dengan hormat, mohon konfirmasi.", "Pagi bro/sis, minta konfirmasinya ya.", "確認依頼のレジスター差"),
            ("Dokumen terlampir untuk diperiksa.", "Ini file-nya ya, tolong dicek.", "添付ファイル共有の差"),
            ("Terima kasih atas kerja samanya.", "Tengkyu bgt bantuannya ya!", "感謝の表現差"),
            ("Mohon maaf atas keterlambatan ini.", "Sori bgt baru sempet bales ya.", "返信遅延の詫びの差")
        ],
        "drill": [
            ("【Email→Chat】添付の報告書をご確認ください。（Mohon periksa laporan terlampir.）", "Pagi mas, ini laporannya ya, tolong dicek.", "パギ マス、イニ ラポランニャ ヤ、トロン ディチェッ", "チャット添付共有。"),
            ("【Chat→Email】了解、すぐやるね！（Sip, meluncur skrg!）", "Baik, akan segera saya tindak lanjuti.", "バイッ、アカン スグラ サヤ ティンダッ ランジュティ", "公式承諾。"),
            ("【Email→Chat】会議の時間を変更可能でしょうか？（Apakah jadwal rapat dapat diundur?）", "Bro, bisa geser jam rapatnya dikit nggak?", "ブロ、ビサ グセル ジャム ラパットニャ ディキット ンガッ", "チャット時間変更打診。"),
            ("【Chat→Email】ごめん、返信遅れた！（Sori bgt baru bales, td lg meeting.）", "Mohon maaf atas keterlambatan dalam membalas pesan ini.", "モホン マアフ アタス クトゥルランバタン ダラム ムンバレス プサン イニ", "公式遅延謝罪。"),
            ("【Email→Chat】ご確認のほど何卒よろしくお願い申し上げます。（Demikian kami sampaikan, terima kasih.）", "Tengkyu bgt ya atas bantuannya!", "テンキュー バンゲット ヤ アタス バントゥアンニャ", "チャット感謝締め。"),
            ("【Chat→Email】企画書、これでOK？（Proposalnya udah oke kan ya?）", "Apakah draf proposal tersebut telah sesuai dengan arahan?", "アパカ ドラフ プロポサル トゥルスブット トゥラ ススアイ ドゥンガン アラハン", "公式提案書確認。"),
            ("【Email→Chat】後ほど詳細をご連絡いたします。（Rincian akan kami informasikan lebih lanjut.）", "Ntar gue kabarin detailnya lagi ya.", "エンタール グエ カバリン ディテイルニャ ラギ ヤ", "チャット連絡予告。"),
            ("【Chat→Email】クライアントからOK出たよ！（Klien udah acc nih!）", "Pihak klien telah memberikan persetujuan resmi.", "ピハッ クライエン トゥラ ムンブリカン プルス トゥジュアン レスミ", "acc ⇄ persetujuan。"),
            ("【Email→Chat】本件についてご相談がございます。（Ada hal yang perlu kami diskusikan.）", "Bisa minta waktunya bentar? Mau ngobrolin ini.", "ビサ ミンタ ワクトゥニャ ブンタル？ マウ ンオブロリン イニ", "チャット相談打診。"),
            ("【Chat→Email】修正完了しました。（Udah direvisi ya, monggo dicek.）", "Revisi dokumen telah selesai kami lakukan.", "レヴィスィ ドクメン トゥラ スルサイ カミ ラクカン", "公式改訂完了報告。"),
            ("【Email→Chat】至急ご返信いただけますと幸いです。（Mohon tanggapan sesegera mungkin.）", "Ditunggu kabarnya ya bro secepatnya.", "ディトゥング カバルニャ ヤ ブロ スチパットニャ", "チャット急ぎ催促。"),
            ("【Chat→Email】体調不良で休みます。（Izin sakit ya hari ini, demam.）", "Dengan hormat, saya mengajukan izin tidak masuk karena sakit.", "ドゥンガン ホルマット、サヤ ムンガジュカン イジン ティダッ マスッ カレナ サキッ", "公式病欠届。"),
            ("【Email→Chat】請求書を送付いたします。（Bersama ini kami lampirkan faktur tagihan.）", "Ini invoicenya ya mas, tolong diproses.", "イニ インヴォイスニャ ヤ マス、トロン ディプロセス", "チャット請求書送付。"),
            ("【Chat→Email】リンク共有します。（Ini link gdrive-nya ya.）", "Berikut kami sampaikan tautan dokumen terkait.", "ブルイクット カミ サンパイカン タウタン ドクメン トゥルカイット", "公式リンク共有。"),
            ("【Email→Chat】良い週末をお過ごしください。（Selamat berakhir pekan.）", "Happy weekend semuanya!", "ハッピー ウィークエンド スムアニャ", "チャット週末挨拶。")
        ],
        "quiz": [
            ("社内チャット（Slack/WA）で同僚に添付ファイルを送る時の最も自然な挨拶は？", ["Ini file-nya ya, tolong dicek bro/sis.", "Dengan hormat kami lampirkan berkas.", "Kepada Yang Terhormat Saudara.", "Bersama surat ini kami haturkan."], 1),
            ("クライアントが承認を出したことを社内チャットで「acc（アクセプト）」と言うが、元の語は？", ["acc (dari kata Belanda: akkoord / accept)", "account", "accident", "accelerate"], 1),
            ("同僚宛てのチャットで「Tengkyu bgt ya!」を公式メールに直す表現は？", ["Terima kasih banyak atas kerja sama dan bantuan Bapak/Ibu.", "Makasih bnyk bro.", "Sip tengkyu.", "Sama-sama dong."], 1)
        ]
    },
    {
        "slug": "23-boss-report-formal-to-oral",
        "title": "【二重言語】上司への口頭進捗報告：かしこまりすぎず失礼にならない敬語ブレンド術",
        "intro": "インドネシアの上司（Bapak / Ibu）への口頭報告は、格式ばった公文書の言葉そのままではぎこちなく、かといって友人言葉（Gaul）を使うと不敬になります。「敬称（Pak / Bu）＋丁寧な口語構文」の黄金バランスを身につけます。",
        "pairs": [
            ("Laporan telah selesai saya buat.", "Laporannya sudah beres saya buat, Pak.", "完了報告のブレンド"),
            ("Klien telah menyetujui kontrak.", "Kliennya sudah setuju dengan kontraknya, Bu.", "進捗報告のブレンド"),
            ("Ada sedikit kendala dalam proyek.", "Mohon maaf Pak, ada sedikit kendala di lapangan.", "トラブル報告の配慮"),
            ("Apakah saya boleh meminta persetujuan?", "Bolehkah saya minta tanda tangan Bapak?", "承認依頼の丁寧口頭")
        ],
        "drill": [
            ("【報告】進捗報告：資料の準備が完了しました。（資料完成報告）", "Pak, bahan presentasinya sudah siap semua.", "パッ、バハン プレゼンタスィニャ スダ スィアップ スムア", "上司への口頭報告 Sudah siap Pak。"),
            ("【相談】お時間を少しいただけますでしょうか？（相談打診）", "Mohon maaf Pak, apakah boleh saya minta waktunya sebentar?", "モホン マアフ パッ、アパカ ボレ サヤ ミンタ ワクトゥニャ スブンタル", "丁寧な時間依頼。"),
            ("【報告】クライアントから返信をいただきました。（進捗）", "Bu, tadi pihak klien sudah memberikan konfirmasi.", "ブ、タディ ピハッ クライエン スダ ムンブリカン コンフィルマスィ", "確認報告。"),
            ("【トラブル】少し問題が発生してしまいました。（問題報告）", "Mohon maaf Pak, ada sedikit masalah pada sistem, tapi sedang kami atasi.", "モホン マアフ パッ、アダ スディキット マサラ パダ スィステム、タピ スダン カミ アタスィ", "対策込みの報告。"),
            ("【依頼】こちらにサインをいただけますでしょうか。（署名依頼）", "Mohon tanda tangan Bapak di lembar persetujuan ini.", "モホン タンダ タンガン バパッ ディ ルンバール プルス トゥジュアン イニ", "丁寧な署名依頼。"),
            ("【報告】予定通り完了いたしました。（定刻完了）", "Pekerjaannya sudah selesai tepat waktu sesuai arahan Bapak.", "プクルジャアンニャ スダ スルサイ トゥパット ワクトゥ ススアイ アラハン バパッ", "指示遵守のアピール。"),
            ("【確認】明日の集合時間はこちらでよろしいですか？（時間確認）", "Untuk pertemuan besok jam sembilan pagi ya, Bu?", "ウントゥッ プルトゥムアン ブソッ ジャム スムビラン パギ ヤ、ブ", "確認の口頭トーン。"),
            ("【報告】現場の視察を終えてオフィスに戻りました。（帰社報告）", "Pak, saya sudah kembali ke kantor setelah survei lapangan.", "パッ、サヤ スダ クンバリ ク カントール ストゥラ スルヴェイ ラパンガン", "帰社報告 kembali ke kantor。"),
            ("【提案】こちらの代替案はいかがでしょうか？（提案打診）", "Bagaimana jika kita gunakan opsi cadangan ini, Pak?", "バガイマナ ジカ キタ グナカン オプスィ チャダンガン イニ、パッ", "控えめな代替案提案。"),
            ("【報告】予算の範囲内に収まりました。（経費報告）", "Biayanya masih masuk dalam anggaran yang disetujui, Bu.", "ビアヤニャ マシ マスッ ダラム アンガラン ヤン ディス トゥジュイ、ブ", "予算遵守報告。"),
            ("【感謝】ご指導いただき誠にありがとうございました。（謝意）", "Terima kasih banyak atas bimbingan dan arahan Bapak.", "トゥリマ カスィ バニャッ アタス ビムビンガン ダン アラハン バパッ", "上司への心からの感謝。"),
            ("【確認】この件は進めてよろしいでしょうか？（GOサイン確認）", "Apakah proyek ini bisa kita mulai jalankan, Pak?", "アパカ プロイェッ イニ ビサ キタ ムライ ジャランカン、パッ", "実行許可確認。"),
            ("【報告】売上が先月比で15%増加しました。（実績報告）", "Penjualan bulan ini naik 15 persen dibanding bulan lalu, Bu.", "プンジュアラン ブラン イニ ナイス リマブラス プルセン ディバンディン ブラン ラル、ブ", "実績口頭報告。"),
            ("【欠勤連絡】発熱のため本日はお休みをいただけますでしょうか。（病欠口頭）", "Pak, mohon izin saya tidak masuk hari ini karena demam tinggi.", "パッ、モホン イジン サヤ ティダッ マスッ ハリ イニ カレナ ドゥマム ティンギ", "丁寧な口頭病欠。"),
            ("【報告】至急の案件に対応完了いたしました。（緊急対応報告）", "Tugas mendadak tadi sudah berhasil kami selesaikan, Pak.", "トゥガス ムンダダッ タディ スダ ブルハスィル カミ スレサイカン、パッ", "緊急案件解決報告。")
        ],
        "quiz": [
            ("男性の上司に口頭で完了報告をする時の最も自然な切り出しは？", ["Pak, laporannya sudah beres saya buat ya.", "Bro, udah kelar nih.", "Gue udah selesai kerjaan.", "Woi bos, liat nih."], 1),
            ("上司への提案で「〜はいかがでしょうか？」と柔らかく尋ねる表現は？", ["Bagaimana menurut arahan Bapak jika...", "Lu harus setuju ya Pak.", "Pasti Bapak mau ini.", "Wajib Bapak terima."], 1),
            ("上司に書類の確認・承認をお願いする際の敬語表現は？", ["Mohon kesediaan Bapak untuk memeriksa draf ini.", "Tolong periksa cepat ya Pak.", "Bawain tanda tangan lu dong.", "Cek ini cepetan."], 1)
        ]
    },
    {
        "slug": "24-customer-cs-chat-register",
        "title": "【二重言語】カスタマーサポート接客：Kak / Min 呼びと親切な敬語チャット表現",
        "intro": "Tokopedia, Shopee, Grabなどの現代インドネシアのオンライン接客では、堅苦しい「Bapak / Ibu」ではなく、親しみと敬意を両立させた「Kak（お兄さん・お姉さん）」や「Min（管理者・Admin）」という独特のチャット敬語が標準です。その作法をマスターします。",
        "pairs": [
            ("Pelanggan yang terhormat", "Halo Kak!", "呼びかけ（親愛なるお客様 ⇄ お客様/Kak）"),
            ("Admin yang bertugas", "Halo Min / Mimin", "顧客から店舗への呼びかけ（Min/Mimin）"),
            ("Barang siap dikirim hari ini.", "Pesanan ready stock ya Kak, siap kirim!", "在庫・発送案内"),
            ("Mohon maaf atas ketidaknyamanan ini.", "Mohon maaf bgt ya Kak atas kendalanya.", "トラブルへのお詫び")
        ],
        "drill": [
            ("【CS対応】こんにちは！何かお手伝いできることはありますか？（挨拶）", "Halo Kak, ada yang bisa dibantu hari ini?", "ハロ カッ、アダ ヤン ビサ ディバントゥ ハリ イニ", "定番挨拶 Halo Kak。"),
            ("【顧客質問】この商品、在庫はまだありますか？（在庫確認）", "Halo Min, apakah produk ini masih ready stock?", "ハロ ミン、アパカ プロドゥッ イニ マシ レディー ストック", "Admin への質問 Halo Min。"),
            ("【CS案内】はい、在庫ございますのですぐに発送可能です。（在庫有）", "Iya Kak, barangnya ready ya, bisa langsung diorder.", "イヤ カッ、バランニャ レディー ヤ、ビサ ランスン ディオルデル", "購入案内 ready stock。"),
            ("【CS案内】ご注文の品は現在配送中です。（配送中）", "Paketnya sedang dalam proses pengiriman oleh kurir ya Kak.", "パケットニャ スダン ダラム プロセス プンギリマン オレ クリル ヤ カッ", "配送状況案内。"),
            ("【CS詫び】配送の遅れについて心よりお詫び申し上げます。（遅延詫び）", "Mohon maaf banget atas keterlambatan pengirimannya ya Kak.", "モホン マアフ バンゲット アタス クトゥルランバタン プンギリマンニャ ヤ カッ", "丁寧かつ親切な謝罪。"),
            ("【顧客質問】色の変更はまだ間に合いますか？（変更希望）", "Min, bisa ganti warna sebelum dikirim nggak ya?", "ミン、ビサ ガンティ ワルナ スブルム ディキリム ンガッ ヤ", "変更希望の打診。"),
            ("【CS対応】承知いたしました、ご希望のカラーに変更いたしますね。（変更受諾）", "Baik Kak, sudah kami ubah warnanya sesuai permintaan ya.", "バイッ カッ、スダ カミ ウバ ワルナニャ ススアイ プルミンタアン ヤ", "柔軟な対応。"),
            ("【CS確認】送付先のご住所にお間違いはございませんか？（住所確認）", "Mohon pastikan kembali alamat pengirimannya sudah benar ya Kak.", "モホン パスティカン クンバリ アラマット プンギリマンニャ スダ ブナル ヤ カッ", "住所再確認。"),
            ("【CS案内】商品は丁寧にプチプチで梱包いたします。（梱包案内）", "Tenang aja Kak, paket akan kami kemas aman dengan bubble wrap tebal.", "トゥナン アジャ カッ、パケット アカン カミ クマス アマン ドゥンガン バブル ラップ トゥバル", "安心感の提供。"),
            ("【顧客感謝】丁寧なご対応ありがとうございました！（顧客謝意）", "Terima kasih banyak ya Min, responnya cepet banget!", "トゥリマ カスィ バニャッ ヤ ミン、レスポンニャ チペット バンゲット", "神対応への感謝。"),
            ("【CS結び】商品がお手元に届くまで少々お待ちください。（結び）", "Ditunggu paketnya tiba dengan selamat ya Kak, have a nice day!", "ディトゥング パケットニャ ティバ ドゥンガン スラマット ヤ カッ、ハヴ ア ナイス デイ", "好印象な締め。"),
            ("【CS案内】レビューで星5つをいただけますと幸いです。（評価依頼）", "Jika puas dengan layanan kami, jangan lupa bintang 5-nya ya Kak.", "ジカ プアス ドゥンガン ラヤナン カミ、ジャンガン ルパ ビンタン リマニャ ヤ カッ", "評価リクエスト。"),
            ("【CS確認】領収書を同封いたしました。（領収書案内）", "Struk pembelian sudah kami masukkan ke dalam paket ya Kak.", "ストルッ プムブリアン スダ カミ マスッカン ク ダラム パケット ヤ カッ", "レシート同封。"),
            ("【CS案内】返金手続きが完了いたしました。（返金完了）", "Proses pengembalian dana sudah berhasil diproses ya Kak.", "プロセス プンガンバリアン ダナ スダ ブルハスィル ディプロセス ヤ カッ", "返金処理報告。"),
            ("【CS結び】またのご利用を心よりお待ちしております。（再訪願い）", "Terima kasih sudah berbelanja di toko kami, ditunggu next ordernya!", "トゥリマ カスィ スダ ブルブランジャ ディ トコ カミ、ディトゥング ネクスト オルダーニャ", "リピート促進。")
        ],
        "quiz": [
            ("インドネシアのEC（Tokopedia/Shopee等）の接客で顧客に対する標準的な親愛呼称は？", ["Kak (Kakak)", "Bapak/Ibu saja", "Tuan", "Saudara"], 1),
            ("顧客が店舗のチャット管理者（カスタマー担当）を呼ぶ定番の愛称は？", ["Min / Mimin (Admin)", "Bos", "Pak", "Guru"], 1),
            ("「商品は在庫がありますのですぐ発送できます」を伝えるEC接客英語混じりの表現は？", ["Barangnya ready ya Kak, siap kirim!", "Barangnya ada di lemari.", "Barang tidak mati.", "Barang hidup Kak."], 1)
        ]
    },
    {
        "slug": "25-sns-instagram-tiktok-slang",
        "title": "【二重言語】SNSコメント欄の解読：IG・TikTok・Xで飛び交う最新ミームと略語",
        "intro": "インドネシアは世界屈指のソーシャルメディア大国です。Instagram, TikTok, X（旧Twitter）のコメント欄には、日々新しいネットスラング（Bahasa Netizen）が誕生しています。スピル（spill）、FYP、サルのように笑うスラングなど、最新のネットミームを解読します。",
        "pairs": [
            ("spill (暴露する、詳細を明かす)", "Spill dong rahasianya!", "「詳細教えて！」「秘密をバラして！」"),
            ("FYP (For You Page)", "Masuk FYP nih kontennya!", "TikTokのおすすめに乗る（バズる）"),
            ("relate (激しく共感する)", "Relate bgt sumpah!", "「めっちゃ共感する、分かりすぎる」"),
            ("salfok (salah fokus)", "Salfok sama kucing di belakang.", "「後ろの猫に目が行って草（視点がズレる）」")
        ],
        "drill": [
            ("【SNS】このコスメの詳細教えて！（暴露・情報要求）", "Spill nama produknya dong Kak!", "スピル ナマ プロドゥッニャ ドン カッ", "情報要求 Spill dong。"),
            ("【SNS】この動画、分かりすぎて超共感！（激しい共感）", "Relate banget sumpah sama ceritanya!", "リレート バンゲット スンパ サマ チュリタニャ", "共感 Relate bgt。"),
            ("【SNS】後ろに映ってる人に目がいっちゃった。（視点の逸脱）", "Salfok sama orang yang lewat di belakang wkwk.", "サルフォッ サマ オラン ヤン ルワット ディ ブラカン", "salah fokus ⇄ salfok。"),
            ("【SNS】動画がバズってお勧めページに乗った！（バズる）", "Kontennya masuk FYP sampe jutaan views!", "コンテンニャ マスッ エフワイピー サンパイ ジュタアン ヴィューズ", "masuk FYP。"),
            ("【SNS】ビジュアルが完璧すぎて神！（ビジュアル絶賛）", "Visualnya nggak ada obat, cakep pol!", "ヴィスアルニャ ンガッ アダ オバット、チャカップ ポル", "nggak ada obat = 薬がない（最高）。"),
            ("【SNS】面白すぎてお腹が痛い！（大爆笑）", "Ngakak guling-guling liat videonya wkwkwk.", "ンガカッ グリングリン リアット ヴィデオニャ", "ngakak = 爆笑。"),
            ("【SNS】どこのブランドか教えて！（リンク要求）", "Spill link tokonya dong min, mau beli!", "スピル リンク トコニャ ドン ミン、マウ ブリ", "Spill link。"),
            ("【SNS】炎上しちゃってコメント欄が荒れてる。（炎上）", "Videonya kena rujak netizen di kolom komentar.", "ヴィデオニャ クナ ルジャッ ネティゼン ディ コロム コメンタール", "kena rujak = 叩かれる・炎上。"),
            ("【SNS】可愛すぎて無理！（萌え死ぬ）", "Lucu bgt tolong, nggak kuat liatnya!", "ルチュ バンゲット トロン、ンガッ クアット リアットニャ", "nggak kuat = 耐えられない（可愛すぎ）。"),
            ("【SNS】この組み合わせ、優勝！（最高のマリアージュ）", "Kombinasi ini valid no debat!", "コンビナスィ イニ ヴァリッド ノー デバット", "valid no debat = 確定・優勝。"),
            ("【SNS】美しすぎて眩しい！（美貌絶賛）", "Cantik bgt MasyaAllah, glowing parah!", "チャンティッ バンゲット マシャアッラー、グローウィング パラ", "glowing parah = 超ツヤ肌。"),
            ("【SNS】噂の真相を早く教えて！（ゴシップ要求）", "Ditunggu spill kelanjutannya part 2!", "ディトゥング スピル クランジュタンニャ パート トゥー", "part 2 希望。"),
            ("【SNS】思わず保存しちゃった。（ブックマーク）", "Auto save konten ini buat referensi.", "オート セーヴ コンテン イニ ブアット レフェレンスィ", "auto save。"),
            ("【SNS】コメント欄で大喜利が始まってる。（ネット民のユーモア）", "Komen-komen netizen emang nggak pernah gagal bikin ketawa.", "コメンコメン ネティゼン エマン ンガッ プルナ ガガル ビキン クタワ", "笑いを外さない。"),
            ("【SNS】ただただ尊い。（感嘆）", "Definisi bahagia yang sesungguhnya.", "デフィニスィ バハギア ヤン ススングフニャ", "definisi = 〜の定義（尊い）。")
        ],
        "quiz": [
            ("SNSで「商品名やブランド、秘密を教えて！」とおねだりするスラング動詞は？", ["Spill dong!", "Share dong!", "Delete dong!", "Block dong!"], 1),
            ("「動画の主旨とは別の背景の面白いものに目が行く」を表す略語は？", ["salfok (salah fokus)", "mager", "baper", "pansos"], 1),
            ("ネット民が「反論の余地がないほど最高・確定！」と同意するフレーズは？", ["Valid no debat!", "Kagak tahu!", "Mungkin bisa!", "Bukan deh!"], 1)
        ]
    },
    {
        "slug": "26-ordering-cafe-restaurant",
        "title": "【二重言語】飲食店・カフェの注文：教科書調（Saya ingin memesan...）⇄ こなれた口語",
        "intro": "カフェやワルン（屋台）で店員に「Saya ingin memesan secangkir kopi」と注文すると、丁寧すぎて相手が恐縮してしまいます。街角の飲食店で最も自然に注文を通すためのスマートな口語表現（Mba, pesen es teh satu ya）をマスターします。",
        "pairs": [
            ("Saya ingin memesan makanan.", "Mas / Mba, mau pesen dong.", "注文したい時の声かけ"),
            ("Tolong berikan es teh manis satu.", "Es teh manisnya satu ya.", "注文の品数コール"),
            ("Berapa total harga semuanya?", "Berapa semuanya, Mas?", "会計尋ね"),
            ("Bolehkah saya minta bon?", "Minta bill-nya dong Mba.", "お会計・レシート依頼")
        ],
        "drill": [
            ("【声かけ】すみません、注文いいですか？（店員への呼びかけ）", "Mas / Mba, mau pesen dong!", "マス / ムバ、マウ プセン ドン", "飲食店での呼びかけ mau pesen dong。"),
            ("【注文】アイススイートティーを1つ、ホットブラックコーヒーを1つ。（注文）", "Es teh manis satu, sama kopi hitam panas satu ya.", "エステ マニス サトゥ、サマ コピ ヒタム パナス サトゥ ヤ", "品数と ya。"),
            ("【要望】砂糖は少なめでお願いします。（甘さ控えめ）", "Gulanya dikit aja ya, less sugar.", "グラニャ ディキット アジャ ヤ、レス シュガー", "甘さ控えめ gulanya dikit aja。"),
            ("【要望】辛くしないでください。（唐辛子抜き）", "Jangan pedes ya Mas, cabenya dikit aja.", "ジャンガン プデス ヤ マス、チャベニャ ディキット アジャ", "辛さ控えめ jangan pedes ya。"),
            ("【店内/持帰】ここで食べます。（店内飲食）", "Makan di sini ya.", "マカン ディ スィニ ヤ", "店内飲食 makan di sini。"),
            ("【持帰】持ち帰りでお願いします。（テイクアウト）", "Dibungkus aja ya Mas.", "ディブンクス アジャ ヤ マス", "テイクアウト dibungkus。"),
            ("【質問】おすすめメニューは何ですか？（人気メニュー）", "Yang paling favorit di sini menu apa ya?", "ヤン パリン ファヴォリット ディ スィニ メニュー アパ ヤ", "おすすめ尋ね favorit menu。"),
            ("【要望】氷抜きでお願いします。（氷なし）", "Nggak pake es ya, tanpa es batu.", "ンガッ パケ エス ヤ、タンパ エス バトゥ", "氷なし nggak pake es。"),
            ("【会計】お会計お願いします。（伝票依頼）", "Mas, minta bill-nya dong / mau bayar.", "マス、ミンタ ビルニャ ドン / マウ バヤル", "会計 minta bill。"),
            ("【支払い】QRIS（QR決済）で払えますか？（電子マネー決済）", "Bisa bayar pake QRIS nggak?", "ビサ バヤル パケ キュリス ンガッ", "QR決済 pake QRIS。"),
            ("【追加】ご飯をもう一杯おかわり！（ライス追加）", "Nasi putihnya nambah satu porsi lagi ya!", "ナスィ プティニャ ナンバ サトゥ ポルスィ ラギ ヤ", "おかわり nambah satu。"),
            ("【要望】別々の会計にできますか？（個別会計）", "Bisa pisah bill nggak Mas?", "ビサ ピサ ビル ンガッ マス", "別会計 pisah bill。"),
            ("【確認】まだ注文した料理が来ていません。（催促）", "Mba, makanannya belom dateng ya dari tadi?", "ムバ、マカナンニャ ブロム ダテン ヤ ダリ タディ", "料理催促 belom dateng ya。"),
            ("【会計】全部でおいくらですか？（合計金額）", "Berapa semuanya Mas totalnya?", "ブラパ スムアニャ マス トタルニャ", "合計金額尋ね。"),
            ("【感謝】ごちそうさまでした、美味しかったです！（退店時）", "Makasih Mas, enak bgt makanannya!", "マカスィ マス、エナッ バンゲット マカナンニャ", "美味しかった感謝。")
        ],
        "quiz": [
            ("ワルンやカフェでテイクアウト（持ち帰り）をお願いする定番単語は？", ["dibungkus", "dibuang", "dimakan", "ditaruh"], 1),
            ("ドリンクの「氷抜き」をお願いする自然な口語表現は？", ["nggak pake es", "tanpa air dingin", "esnya buang", "tidak ada kutub"], 1),
            ("料理をもう一皿「おかわり・追加」する時の動詞は？", ["nambah satu lagi", "kurang satu lagi", "hilang satu lagi", "habis satu lagi"], 1)
        ]
    },
    {
        "slug": "27-taxi-ojol-ride-hailing",
        "title": "【二重言語】タクシー・配車アプリの会話：GoCar/Grabドライバーとの自然なナビ指示",
        "intro": "Gojek, Grab, Bluebird などの車やバイクに乗る際、ドライバー（Pak Sopir / Bang Ojol）との意思疎通は100%口語で行われます。「左折してください」「ロビー前で降ろしてください」など、安全かつ的確に指示を伝える会話パターンを体得します。",
        "pairs": [
            ("Tolong belok ke kiri.", "Kiri depan ya Bang.", "左折指示（前のところで左ね）"),
            ("Saya sudah berada di lobi.", "Saya udah di lobi ya Pak.", "ピックアップ場所の連絡"),
            ("Tolong turunkan saya di sini.", "Turun di sini aja Pak, pas.", "降車指示（ここで降ろして）"),
            ("Lewat jalan tol saja.", "Lewat tol aja ya Pak biar cepet.", "ルート指定（高速使ってね）")
        ],
        "drill": [
            ("【位置連絡】ロビーの柱の前にいます。（ピックアップ位置）", "Pak, saya tunggu di depan lobi dekat tiang ya.", "パッ、サヤ トゥング ディ ドゥパン ロビ ドゥカット ティアン ヤ", "ピックアップ詳細連絡。"),
            ("【ルート指示】高速道路を通ってください。（高速利用）", "Lewat jalan tol aja ya Pak biar nggak kena macet.", "ルワット ジャラン トル アジャ ヤ パッ ビアル ンガッ クナ マチェット", "高速利用指示 lewat tol aja。"),
            ("【方向指示】次の交差点を右折してください。（右折）", "Depan belok kanan ya Bang.", "ドゥパン ベロッ カナン ヤ バン", "右折指示 belok kanan。"),
            ("【方向指示】そのまま真っ直ぐ進んでください。（直進）", "Lurus terus aja Pak ikuti jalan utama.", "ルルス トゥルス アジャ パッ イクティ ジャラン ウタマ", "直進指示 lurus terus。"),
            ("【停車指示】あの赤い門の前で停めてください。（停車位置）", "Berhenti di depan gerbang merah itu ya Pak.", "ブルヘンティ ディ ドゥパン グルバン メラ イトゥ ヤ パッ", "目印停車 gerbang merah。"),
            ("【エアコン調整】冷房をもう少し強くしてもらえますか？（冷房）", "Pak, AC-nya boleh tolong digedein dikit?", "パッ、アーセーニャ ボレ トロン ディグデイン ディキット", "冷房強め AC digedein。"),
            ("【チャット確認】ドライバーさん、今どのあたりですか？（現在地確認）", "Pak, posisinya udah di mana ya sekarang?", "パッ、ポスィスィニャ ウダ ディ マナ ヤ スカラン", "現在地尋ね posisinya di mana。"),
            ("【降車】ここで降ります、お釣りは取っておいてください。（降車＆チップ）", "Turun di sini aja Pak, kembaliannya ambil aja.", "トゥルン ディ スィニ アジャ パッ、クンバリアンニャ アンビル アジャ", "チップ kembaliannya ambil aja。"),
            ("【スピード】急がなくて大丈夫ですよ、安全運転で。（安全配慮）", "Nggak usah buru-buru Pak, santai aja.", "ンガッ ウサ ブルブル パッ、サンタイ アジャ", "安全運転促し santai aja。"),
            ("【確認】この道、合っていますか？（ルート確認）", "Pak, jalannya bener lewat sini ya?", "パッ、ジャランニャ ブネル ルワット スィニ ヤ", "ルート確認。"),
            ("【停車指示】少し手前で降ろしてください。（手前停車）", "Sebelum jembatan turunin di kiri ya Bang.", "スブルム ジュンバタン トゥルニン ディ キリ ヤ バン", "手前降車 turunin di kiri。"),
            ("【支払い】高速代は現金でお支払いしますね。（高速代清算）", "Uang tolnya saya bayar tunai ya Pak.", "ウアン トルニャ サヤ バヤル トゥナイ ヤ パッ", "高速代現金 uang tol tunai。"),
            ("【Uターン】あそこでUターンしてください。（Uターン）", "Putar balik di depan putaran itu ya Pak.", "プタール バリッ ディ ドゥパン プタラン イトゥ ヤ パッ", "Uターン putar balik。"),
            ("【オジェック乗車】ヘルメットを貸してください。（バイクヘルメット）", "Helmnya ada Bang? Tolong pinjam ya.", "ヘルムニャ アダ バン？ トロン ピンジャム ヤ", "ヘルメット借用。"),
            ("【感謝】安全運転ありがとうございました！（降車挨拶）", "Makasih banyak ya Pak, hati-hati di jalan!", "マカスィ バニャッ ヤ パッ、ハティハティ ディ ジャラン", "感謝と送り出し。")
        ],
        "quiz": [
            ("タクシーや車内で「高速道路を使ってください」と頼む自然な表現は？", ["Lewat tol aja ya Pak.", "Pergi tol silakan Bapak.", "Jalan tol ambil cepat.", "Mobil naik tol saja."], 1),
            ("バイクタクシー（オジョル）の男性ドライバーに対する親しみのある呼びかけは？", ["Bang (Abang)", "Bapak Direktur", "Tuan", "Adik kecil"], 1),
            ("「お釣りは取っておいてください（チップ）」と言う時の定番フレーズは？", ["Kembaliannya ambil aja ya Pak.", "Uang ini hilang untuk Anda.", "Tidak mau uang kembali.", "Beri hadiah kembalian."], 1)
        ]
    },
    {
        "slug": "28-market-bargaining-tpo",
        "title": "【二重言語】伝統市場・露店の値引き交渉：角を立てずに距離を縮めるGaul交渉術",
        "intro": "パサール（伝統市場）やお土産屋での値段交渉は、単なる金額の叩き合いではなく「人間味のあるコミュニケーションの場」です。尊大にならず、親近感（Bisa kurang dikit nggak bu?）を演出して笑顔で値引きを引き出す交渉術を学びます。",
        "pairs": [
            ("Berapa harganya ini?", "Berapaan nih Bu satu kilonya?", "値段尋ね（キロいくら？）"),
            ("Apakah harganya bisa ditawar?", "Bisa kurang dikit nggak, Bang?", "値引き可能かの打診"),
            ("Harganya terlalu mahal.", "Mahal amat ya, nggak dapet murah?", "高すぎるよ〜（親しい不満）"),
            ("Kalau saya beli dua, dapat diskon?", "Kalo ambil dua dapet berapa nih?", "まとめ買い交渉")
        ],
        "drill": [
            ("【価格尋ね】おばちゃん、このマンゴー1キロいくら？（値段尋ね）", "Bu, mangga ini sekilo berapaan?", "ブ、マンガ イニ スキロ ブラパアン", "パサールでの値段尋ね berapaan。"),
            ("【値引き打診】もう少し安くならない？（値引き打診）", "Bisa kurang dikit nggak nih harganya?", "ビサ クラン ディキット ンガッ ニ ハルガニャ", "値引き Bisa kurang dikit nggak?。"),
            ("【親しい不満】え〜高いよ！まけてよ〜（甘え交渉）", "Aduh mahal amat ya, kurangin dong Bu!", "アドゥ マハル アマット ヤ、クランイン ドン ブ", "kurangin dong!。"),
            ("【まとめ買い】2個買うからオマケして！（複数買い）", "Kalo gue ambil dua biji, dapet diskon kan ya?", "カロ グエ アンビル ドゥア ビジ、ダペット ディスコン カン ヤ", "まとめ買い ambil dua。"),
            ("【予算提示】5万ルピアにしてくれたら今すぐ買う！（指値交渉）", "Pas lima puluh ribu boleh nggak? Langsung bungkus deh.", "パス リマ プル リブ ボレ ンガッ？ ランスン ブンクス デ", "即決提示 Langsung bungkus deh。"),
            ("【品質確認】これ、新鮮だよね？（鮮度確認）", "Masih seger-seger kan sayurnya Bu?", "マシ スグルスグル カン サユルニャ ブ", "新鮮確認 seger kan。"),
            ("【立ち去り作戦】うーん、じゃあ他のお店も見てみるね。（駆け引き）", "Ya udah deh, saya liat-liat toko sebelah dulu ya.", "ヤ ウダ デ、サヤ リアットリアット トコ スブラ ドゥル ヤ", "立ち去り戦術。"),
            ("【呼び戻し】お客さん、特別にその値段でいいよ！（妥協成立）", "Ya udah deh Mas, khusus buat Mas saya kasih harga segitu.", "ヤ ウダ デ マス、クスス ブアット マス サヤ カスィ ハルガ スギトゥ", "店側の譲歩 harga segitu。"),
            ("【追加要求】唐辛子をちょっとオマケで付けて！（オマケおねだり）", "Minta bonus cabe rawitnya dikit dong Bu!", "ミンタ ボヌス チャベ ラウィットニャ ディキット ドン ブ", "オマケ要求 bonus cabe。"),
            ("【常連アピール】私、いつもここで買ってる常連だよ！（関係性アピール）", "Saya kan langganan di sini Bu, masa nggak dapet murah.", "サヤ カン ランガナン ディ スィニ ブ、マサ ンガッ ダペット ムラ", "常連 langganan。"),
            ("【甘さ確認】このパパイヤ、甘い？（味の保証）", "Pepayanya manis nggak nih? Kalo nggak manis boleh balikin ya.", "プパヤニャ マニス ンガッ ニ？ カロ ンガッ マニス ボレ バリキン ヤ", "甘さ保証 manis nggak。"),
            ("【硬さ確認】アボカド、今日すぐ食べられるやつある？（食べ頃）", "Alpukat yang udah mateng buat dimakan hari ini ada Bu?", "アルプカット ヤン ウダ マテン ブアット ディマカン ハリ イニ アダ ブ", "完熟 udah mateng。"),
            ("【試食】味見してもいい？（試食許可）", "Boleh icip-icip dikit dulu nggak?", "ボレ イチップイチップ ディキット ドゥル ンガッ", "味見 icip-icip。"),
            ("【支払い】細かいお札がなくて、10万札でもいい？（高額紙幣）", "Ada kembalian nggak Bu? Duitnya merah seratus ribu nih.", "アダ クンバリアン ンガッ ブ？ ドゥイットニャ メラ スラトゥス リブ ニ", "duit merah = 10万ルピア札。"),
            ("【感謝】おばちゃん、ありがとう！また来るね。（再訪約束）", "Makasih ya Bu, besok-besok saya mampir lagi!", "マカスィ ヤ ブ、ブソッブソッ サヤ マンピル ラギ", "関係構築 mampir lagi。")
        ],
        "quiz": [
            ("伝統市場で「少し値引きしてもらえませんか？」と笑顔で尋ねる最も定番のフレーズは？", ["Bisa kurang dikit nggak Bu?", "Harus kurangi harga!", "Saya minta diskon mutlak.", "Berapa potongan wajib?"], 1),
            ("「常連客」を意味するインドネシア語は？", ["langganan", "tamu baru", "penjual", "kasir"], 1),
            ("果物やスナックを「ちょっと味見してもいい？」と可愛らしく聞く語は？", ["Boleh icip-icip dikit?", "Boleh telan habis?", "Boleh bawa pulang?", "Boleh buang dikit?"], 1)
        ]
    },
    {
        "slug": "29-phone-call-switching",
        "title": "【二重言語】電話応対のコードスイッチング：公式代表電話 ⇄ 同僚・内線電話",
        "intro": "相手の顔が見えない電話では、最初の名乗りとレジスターの選択が極めて重要です。社外の顧客に対する「公式代表電話（Halo, selamat pagi, dengan PT...）」と、社内の内線や親しい同僚の携帯への電話（Halo bro, lagi di mana?）を瞬時に切り替えます。",
        "pairs": [
            ("Halo, selamat pagi, PT ABC, dengan Budi.", "Halo bro, ada apa nih?", "名乗りのレジスター差"),
            ("Bolehkah saya berbicara dengan Bapak Direktur?", "Pak Bambang-nya ada nggak ya?", "取次ぎ依頼の差"),
            ("Mohon tunggu sebentar, saya sambungkan.", "Bentar ya, gue panggilin orangnya.", "保留・呼出しの差"),
            ("Apakah ada pesan yang ingin disampaikan?", "Mau titip pesen apa nih?", "伝言預かりの差")
        ],
        "drill": [
            ("【公式受電】お電話ありがとうございます、ABC社でございます。（代表受電）", "Selamat pagi, PT ABC, dengan Budi, ada yang bisa dibantu?", "スラマット パギ、ペーテー アーベーセー、ドゥンガン ブディ、アダ ヤン ビサ ディバントゥ", "代表電話名乗り。"),
            ("【同僚受電】もしもし、どうしたの？（内線同僚）", "Halo bro, kenapa? Ada urusan apa nih?", "ハロ ブロ、クナパ？ アダ ウルサン アパ ニ", "フランクな内線 Halo bro。"),
            ("【公式取次】営業部の山田様にお繋ぎいただけますでしょうか。（取次依頼）", "Bolehkah saya disambungkan dengan Bapak Yamada dari bagian pemasaran?", "ボレカ サヤ ディサンブンカン ドゥンガン パッ ヤマダ ダリ バギアン プマサラン", "公式取次依頼。"),
            ("【内線取次】ちょっと待ってて、彼を呼んでくるから。（内線保留）", "Tunggu bentar ya bro, orangnya lagi di toilet, ntar gue panggilin.", "トゥング ブンタル ヤ ブロ、オランニャ ラギ ディ トイレット、エンタール グエ パンギリン", "口語保留 panggilin。"),
            ("【公式不在】あいにく外出中でございます、伝言を承りましょうか？（不在案内）", "Mohon maaf beliau sedang berada di luar kantor, apakah ada pesan?", "モホン マアフ ベリアウ スダン ブルアダ ディ ルアル カントール、アパカ アダ プサン", "不在案内と伝言。"),
            ("【内線伝言】戻ったら電話くれるように伝えて。（内線伝言）", "Titip pesen ya, suruh dia telpon balik ke gue kalo udah nyampe.", "ティティップ プセン ヤ、スルー ディア テルポン バリッ ク グエ カロ ウダ ニャンペ", "telpon balik = 折り返し。"),
            ("【音声不良】申し訳ございません、お電話が少し遠いようです。（音声トラブル）", "Mohon maaf suaranya agak putus-putus, bisa diulangi?", "モホン マアフ スアラニャ アガッ プトゥスプトゥス、ビサ ディウランギ", "途切れ putus-putus。"),
            ("【口語電波】電波悪い！後で掛け直すね！（電波不良）", "Sinyalnya jelek parah nih! Ntar gue telpon lagi ya!", "スィニャルニャ ジュレッ パラ ニ！ エンタール グエ テルポン ラギ ヤ", "sinyal jelek ⇄ 電波不良。"),
            ("【公式折返】先ほどお電話をいただいた件で折り返しました。（公式折返し）", "Saya menghubungi kembali sehubungan dengan panggilan telepon tadi.", "サヤ ムンフブンギ クンバリ スフブンガン ドゥンガン パンギラン テレポン タディ", "折り返し電話 sehubungan。"),
            ("【内線急ぎ】緊急の件だからすぐ確認して！（至急）", "Urgent nih bro, buruan cek email ya!", "ウルジェント ニ ブロ、ブルアン チェッ イーメール ヤ", "urgent nih。"),
            ("【間違い電話】恐れ入りますが、番号をお間違いではないでしょうか？（誤発信）", "Mohon maaf, sepertinya Anda salah sambung nomor telepon.", "モホン マアフ、スペルティニャ アンダ サラ サンブン ノモール テレポン", "間違い電話 salah sambung。"),
            ("【口語切電】じゃあね、また後で！（通話終了）", "Oke deh, yuk ntar ketemu! Bye!", "オケ デ、ユッ エンタール クトゥム！ バイ", "通話終了 Oke deh。"),
            ("【公式終話】お電話いただきありがとうございました、失礼いたします。（公式切電）", "Terima kasih telah menghubungi kami, selamat siang.", "トゥリマ カスィ トゥラ ムンフブンギ カミ、スラマット スィアン", "代表電話終了。"),
            ("【内線着信】誰から電話？（着信尋ね）", "Dari siapa tuh telponnya tadi?", "ダリ スィアパ トゥ テルポンニャ タディ", "誰から dari siapa。"),
            ("【不在着信】着信残ってたけど、何かあった？（折り返し尋ね）", "Tadi ada missed call dari lu, ada apa ya?", "タディ アダ ミスド コール ダリ ル、アダ アパ ヤ", "missed call。")
        ],
        "quiz": [
            ("公式な代表電話を受電した際の最も標準的な第一声は？", ["Selamat pagi, PT [Nama Perusahaan], dengan [Nama], ada yang bisa dibantu?", "Halo bro, ada urusan apa nih?", "Woi siapa nih yang nelpon?", "Halo apaan ya?"], 1),
            ("電話が「間違い電話ですよ」と丁寧に伝える決まり文句は？", ["Mohon maaf, sepertinya salah sambung.", "Salah nomor lu!", "Jangan telpon ke sini!", "Bukan rumah ini."], 1),
            ("電波が悪くて「声が途切れています」と伝えるフレーズは？", ["Suaranya agak putus-putus.", "Suaranya patah-patah.", "Suaranya rusak total.", "Suaranya mati."], 1)
        ]
    },
    {
        "slug": "30-small-talk-weekend-gossip",
        "title": "【二重言語】週末の雑談・ウワサ話：距離を一気に縮める完全Gaulリラックスモード",
        "intro": "同僚や友人とカフェでくつろぎ、週末の出来事や最新のゴシップ（gosip）、恋愛事情を語り合う時は、教科書的文法をすべて脱ぎ捨てた「完全Gaulモード」が炸裂します。心の壁を完全に取り払い、ネイティブと本音で笑い合える表現を身につけます。",
        "pairs": [
            ("Bagaimana akhir pekan Anda?", "Gimana weekend lu kemarin? Seru nggak?", "週末どうだった？"),
            ("Apakah ada kabar terbaru?", "Ada gosip panas apa nih sekarang?", "最新ゴシップある？"),
            ("Saya merasa sangat lelah.", "Capek parah gue, pengen healing.", "めっちゃ疲れた、癒されたい"),
            ("Itu adalah hal yang sangat menarik.", "Gokil bgt sih ceritanya!", "マジでヤバい（最高に面白い）")
        ],
        "drill": [
            ("【雑談】週末どこか遊びに行った？（週末の過ごし方）", "Kemaren pas weekend jalan ke mana aja lu?", "クマリン パス ウィークエンド ジャラン ク マナ アジャ ル", "週末の行動尋ね。"),
            ("【雑談】ずっと家でダラダラ寝てただけだよ。（家で休養）", "Cuma mager rebahan doang di kosan, santai abis.", "チュマ マゲル ルバハン ドアン ディ コサン、サンタイ アビス", "ダラダラ過ごす mager rebahan。"),
            ("【ウワサ】ねえねえ、あの二人が付き合ってるって聞いた？（ゴシップ）", "Eh lu tahu nggak, denger-denger mereka jadian lho!", "エ ル タフ ンガッ、ドゥンゲルドゥンゲル ムレカ ジャディアン ロ", "付き合い始めた jadian。"),
            ("【驚き】マジで？！全然知らなかった！（驚愕）", "Sumpah demi apa?! Gue nggak nyangka sama sekali!", "スンパ デミ アパ？！ グエ ンガッ ニャンカ サマ スカリ", "驚きのリアクション Sumpah demi apa?!。"),
            ("【癒し】最近仕事忙しすぎて、マジで癒し旅行行きたい。（ヒーリング）", "Kerjaan numpuk parah, butuh healing ke Bali nih.", "クルジャアン ヌンプッ パラ、ブトゥ ヒーリング ク バリ ニ", "癒し butuh healing。"),
            ("【恋愛】彼氏/彼女と喧嘩しちゃった。（恋愛トラブル）", "Lagi berantem gue sama ayang semalem.", "ラギ ブランテム グエ サマ アヤン スマレム", "恋人 ayang (sayang)。"),
            ("【共感】分かる〜、私も同じ経験あるよ。（共感）", "Iya bgt, gue juga pernah ngerasain hal yang sama persis.", "イヤ バンゲット、グエ ジュガ プルナ ンゲラサイン ハル ヤン サマ プルスィス", "激しい共感 Iya bgt。"),
            ("【買い物】衝動買いして金欠になっちゃった。（散財）", "Kalap belanja online, dompet langsung kering kerontang.", "カラップ ブランジャ オンライン、ドンペット ランスン クリン クロンタン", "金欠 dompet kering。"),
            ("【カフェ】ここのコーヒー、マジで美味しくて当たりだね！（カフェ絶賛）", "Kopinya enak bgt no debat, tempatnya juga aesthetic parah.", "コピニャ エナッ バンゲット ノー デバット、トゥンパットニャ ジュガ エステティック パラ", "aesthetic parah = 超エモい。"),
            ("【映画】あの新作映画、もう見た？超おすすめだよ。（映画談義）", "Udah nonton film barunya belom? Wajib tonton sih parah!", "ウダ ノントン フィルム バルニャ ブロム？ ワジッブ トントン スィ パラ", "必見 wajib tonton。"),
            ("【ツッコミ】お前、盛りすぎでしょ！（大げさツッコミ）", "Lebay lu ah, jangan lebay gitu napa!", "ルバイ ル ア、ジャンガン ルバイ ギトゥ ナパ", "大げさ lebay。"),
            ("【愚痴】あの上司、気難しくて疲れるわ。（上司への本音）", "Bos gue rewel bgt akhir-akhir ini, capek ati gue.", "ボス グエ レウェル バンゲット アキールアキール イニ、チャペッ アティ グエ", "気難しい rewel, capek ati。"),
            ("【計画】来週みんなでBBQしようぜ！（仲間内計画）", "Minggu depan kita bakar-bakar daging yuk bareng anak-anak!", "ミング ドゥパン キタ バカルバカル ダギン ユッ バレン アナッアナッ", "BBQ bakar-bakar。"),
            ("【安心】心配すんな、俺がついてる！（友情）", "Santai aja bro, ada gue ini, aman terkendali.", "サンタイ アジャ ブロ、アダ グエ イニ、アマン トゥルクンダリ", "万事快調 aman terkendali。"),
            ("【締め】楽しかった！また集まろうね！（雑談の別れ）", "Seru bgt ngobrol hari ini, ntar nongkrong lagi ya guys!", "スル バンゲット ンオブロル ハリ イニ、エンタール ノンクロン ラギ ヤ ガイズ", "また集まろう nongkrong lagi ya。")
        ],
        "quiz": [
            ("恋人同士が「正式に付き合い始めた」ことを表す定番の口語動詞は？", ["jadian", "nikahan", "temanan", "putusan"], 1),
            ("疲れた若者が「自然や旅行で癒されたい、リフレッシュしたい」と言う時の流行語は？", ["butuh healing", "butuh obat", "butuh rumah sakit", "butuh lari"], 1),
            ("大げさに振る舞ったり、話を盛りすぎる人をからかうスラング形容詞は？", ["lebay", "mager", "baper", "omdo"], 1)
        ]
    }
]

for a in articles_data:
    filepath = os.path.join("docs/diglossia", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. コードスイッチング対比表（公式標準表現 ⇄ 口語・スラング）\n")
    lines.append("| No | 公式標準表現 (Bahasa Baku) | 口語・スラング (Bahasa Gaul) | 意味・ニュアンス |")
    lines.append("|---|---|---|---|")
    for idx, (baku, gaul, meaning) in enumerate(a['pairs'], 1):
        lines.append(f"| {idx} | `{baku}` | **{gaul}** | {meaning} |")
    lines.append("")
    
    lines.append("## 2. 構文・文脈心理メカニズム\n")
    lines.append("公式標準語の文法構造が、口語においてどのように短縮・脱落・母音変容（音韻融合）を起こしているかを理解することで、リスニングの「聞き取れない壁」を突破し、自然な発話が可能になります。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 双方向コード変換ドリル（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語と提示された文を見て、指定されたレジスター（Baku → Gaul または Gaul → Baku）へ1〜2秒以内に口頭で言い換えてください。\n")
    
    for idx, (prompt, target_sent, kana, exp) in enumerate(a['drill'], 1):
        m = re.match(r'^(【.+?】)(.+?)（(.+?)）$', prompt)
        if m:
            tag, jp, orig = m.group(1), m.group(2), m.group(3)
            lines.append(f"### 第{idx}問: {tag}「**{jp}**」（{orig}）\n")
        else:
            lines.append(f"### 第{idx}問: 「**{prompt}**」\n")
        lines.append('<div class="id-example">')
        lines.append(f'<div class="id-sentence"><strong>{target_sent}</strong></div>')
        lines.append(f'<div class="id-pronunciation">発音: {kana}</div>')
        lines.append(f'<div class="id-translation">解説: {exp}</div>')
        lines.append('</div>\n')
    
    lines.append("## 4. 理解度チェッククイズ\n")
    for q_idx, (q_text, opts, ans_idx) in enumerate(a['quiz'], 1):
        lines.append(f"### 問{q_idx}: {q_text}\n")
        for o_idx, opt in enumerate(opts, 1):
            mark = " (正解)" if o_idx == ans_idx else ""
            lines.append(f"- [{ 'x' if o_idx == ans_idx else ' ' }] {o_idx}. {opt}{mark}")
        lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated: {filepath}")

print("Batch 1121-1130 generated successfully.")
