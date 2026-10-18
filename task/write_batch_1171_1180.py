# -*- coding: utf-8 -*-
import os
import re

os.makedirs("docs/strategies", exist_ok=True)

articles_data = [
    {
        "slug": "21-saying-no-diplomatically",
        "title": "【戦略会話】角を立てない拒絶：「前向きに検討しますが、現時点では困難です」の外交辞令",
        "intro": "インドネシア文化（特にジャワ的社会規範）において、「Tidak bisa!（無理です！）」と直接的に拒絶することは相手のメンツ（muka）を潰すタブーとされます。「Kami pertimbangkan dulu...（まず検討させていただきます）」「Untuk saat ini agak berat...（現時点では少々厳しく…）」など、角を立てずに礼儀正しく断る外交辞令ストラテジーを体得します。",
        "pairs": [
            ("Akan kami pertimbangkan terlebih dahulu.", "Dipikir-pikir dulu ya...", "保留・前向き検討の建前"),
            ("Untuk saat ini agak sulit bagi kami.", "Kayaknya agak berat deh buat skrg.", "現時点での困難提示"),
            ("Jadwal kami sudah terisi penuh.", "Jadwalnya udah padet bgt nih.", "多忙を理由にした辞退"),
            ("Mohon maaf belum berjodoh saat ini.", "Belum jodoh kali ya kali ini.", "文化的な縁の表現")
        ],
        "drill": [
            ("【ビジネス】大変魅力的なご提案ですが、現時点での導入は予算上困難でございます。（Penawaran menarik, namun anggaran saat ini belum memungkinkan.）", "Tawaran ini sangat menarik, namun mengingat alokasi anggaran tahun ini sudah terkunci, untuk saat ini belum memungkinkan bagi kami.", "タワラン イニ サンガット ムナリッ、ナムン ムニンガット アロカスィ アンガラン タフン イニ スダ トゥルクンチ、ウントゥッ サアット イニ ブルム ムンムンキンカン バギ カミ", "公式な丁寧な辞退。"),
            ("【日常会話】誘ってくれて嬉しいけど、今日は先約があって行けないんだ。（Makasih udah diajak, tapi hari ini udah ada janji lain.）", "Wah makasih banyak ya udah diajak! Tapi sori bgt, kebetulan hari ini udah ada janji sama keluarga nih.", "ワ マカスィ バニャッ ヤ ウダ ディアンジャッ！ タピ ソリ バンゲット、クブトゥラン ハリ イニ ウダ アダ ジャンジ サマ クルアルガ ニ", "友人からの誘いの上手な断り。"),
            ("【借金申し入れ】申し訳ないけど、今月は出費が重なってお金に余裕がないんだ。（Sori bgt, bulan ini pengeluaran lagi jebol.）", "Duh sori bgt ya bro, bukannya gak mau bantu, tapi bulan ini pengeluaran gue lagi boncos parah buat biaya rumah sakit.", "ドゥ ソリ バンゲット ヤ ブロ、ブカンニャ ガッ マウ バントゥ、タピ ブラン イニ プングルアラン グエ ラギ ボンチョス パラ ブアット ビアヤ ルマ サキット", "金銭貸借の角を立てない拒否。"),
            ("【納期短縮】品質を担保するため、これ以上の納期前倒しは困難です。（Sulit memajukan tenggat demi menjaga mutu.）", "Demi menjaga standar kualitas yang prima, kami khawatir hasil kerja tidak maksimal apabila jadwal dimajukan lebih awal.", "ドゥミ ムンジャガ スタンダール クアリタス ヤン プリマ、カミ カワティール ハシル クルジャ ティダッ マクスィマル アパビラ ジャドワル ディマジュカン ルビ アワル", "品質理由の納期拒否。"),
            ("【追加値引き】これ以上の値引きは原価割れしてしまうため致しかねます。（Diskon lebih lanjut berada di bawah modal dasar.）", "Angka ini sudah harga modal tanpa margin keuntungan lagi bagi kami, mohon pengertiannya ya Bapak.", "アンカ イニ スダ ハルガ モダル タンパ マルジン クウントゥンガン ラギ バギ カミ、モホン プンゲルティアンニャ ヤ バパッ", "原価限界の提示。"),
            ("【残業要請】今日は家庭の事情があり、どうしても定時で退社せねばなりません。（Hari ini ada urusan keluarga mendesak.）", "Mohon maaf sekali Pak, kebetulan malam ini ada agenda keluarga yang tidak dapat diwakilkan, saya cicil tugasnya besok pagi ya.", "モホン マアフ スカリ パッ、クブトゥラン マラム イニ アダ アジェンダ クルアルガ ヤン ティダッ ダパット ディワキルカン、サヤ チチル トゥガスニャ ベソッ パギ ヤ", "残業の丁寧な辞退。"),
            ("【商品勧誘】今は必要ありませんので、また機会がございましたら。（Belum butuh saat ini, nanti kalau butuh saya kontak.）", "Terima kasih informasinya mbak, untuk saat ini kami belum membutuhkan produk tersebut, nanti jika ada keperluan kami hubungi ya.", "トゥリマ カシ インフォルマスィニャ ムバッ、ウントゥッ サアット イニ カミ ブルム ムムルルカン プロドゥッ トゥルスブット、ナンティ ジカ アダ クプルルアン カミ フブンギ ヤ", "セールス電話の撃退。"),
            ("【飲酒の勧め】ドクターストップでお酒が飲めない体質なんです。（Sedang tidak boleh minum alkohol oleh dokter.）", "Aduh mohon maaf sekali, lambung saya lagi dalam perawatan dokter jadi dipantang minum alkohol sama sekali nih.", "アドゥ モホン マアフ スカリ、ランブン サヤ ラギ ダラム プラワタン ドクテール ジャディ ディパンタン ミヌム アルコール サマ スカリ ニ", "健康理由の飲酒辞退。"),
            ("【無理な依頼】私の権限の範囲を超えておりますので、対応いたしかねます。（Di luar wewenang dan kapasitas saya.）", "Perkara tersebut berada di luar wewenang kapasitas jabatan saya, mohon koordinasikan langsung ke bagian legal ya.", "プルカラ トゥルスブット ブラダ ディ ルアル ウェウェナン カパスィタス ジャバタン サヤ、モホン コオルディナスィカン ランスン ク バギアン レガル ヤ", "権限外の明確化。"),
            ("【ヘッドハンティング】現職でのプロジェクトが道半ばのため、転職は考えておりません。（Masih berkomitmen menuntaskan proyek saat ini.）", "Terima kasih atas tawarannya yang terhormat; saat ini saya masih berkomitmen penuh menyelesaikan amanah proyek di institusi saya.", "トゥリマ カシ アタス タワランニャ ヤン トゥルホルマット；サアット イニ サヤ マスィ ブルコミットメン プヌ ムニュレサイカン アマナ プロイェッ ディ インスティトゥスィ サヤ", "転職の辞退。"),
            ("【相乗り拒否】急いで直行せねばならず、遠回りは難しいです。（Harus buru-buru langsung ke tujuan.）", "Sori bgt bro gak bisa bareng, gue mesti langsung tancap gas ngejar waktu ke bandara, takut ketinggalan pesawat.", "ソリ バンゲット ブロ ガッ ビサ バレン、グエ ムスティ ランスン タンチャップ ガス ンゲジャール ワクトゥ ク バンダラ、タクット クティンガラン プサワット", "便乗依頼の断り。"),
            ("【寄付の要請】今月はすでに予算枠を使い切ってしまいました。（Alokasi donasi bulan ini sudah terserap penuh.）", "Mohon maaf proposalnya kami terima, namun pos alokasi donasi sosial kami untuk bulan berjalan sudah habis terserap.", "モホン マアフ プロポサルニャ カミ トゥリマ、ナムン ポス アロカスィ ドナスィ ソスィアル カミ ウントゥッ ブラン ブルジャラン スダ ハビス トゥルスラッ", "寄付の角を立てない辞退。"),
            ("【社内昇進辞退】今は現場の実務で経験を積みたいと考えております。（Ingin fokus memperdalam pengalaman teknis lapangan.）", "Terima kasih atas kepercayaan manajemen; namun saat ini saya merasa perlu memperdalam kematangan teknis sebelum menduduki jabatan struktural.", "トゥリマ カシ アタス クプルチャヤアン マナジェメン；ナムン サアット イニ サヤ ムラサ プル ムンプルダラム クマタンガン テクニス スブルム ムンドゥドゥキ ジャバタン ストルクトゥラル", "役職打診の辞退。"),
            ("【私生活への介入】プライベートな領域ですので、回答は控えさせていただきます。（Ini ranah pribadi yang ingin saya simpan sendiri.）", "Hehe itu ranah privasi saya ya kak, mending kita bahas topik lain yang lebih seru yuk!", "ヘヘ イトゥ ラナ プリヴァスィ サヤ ヤ カッ、メンディン キタ バハス トピック ライン ヤン ルビ スル ユッ", "詮索の上手なかわし。"),
            ("【総括】断り方の上手な者こそが、生涯の人間関係を守り抜く。（Seni menolak dengan santun adalah pelindung persahabatan sejati.）", "Tolak tawarannya dengan elegan, tapi pelihara rasa hormat dan martabat manusianya!", "トラッ タワランニャ ドゥンガン エレガン、タピ プリハラ ラサ ホルマット ダン マルタバット マヌスィアニャ", "断り方の神髄。")
        ],
        "quiz": [
            ("インドネシアで相手のメンツを潰さずに提案を断る際、最も一般的な前置きは？", ["Akan kami pertimbangkan terlebih dahulu / Untuk saat ini agak sulit...", "Pasti saya tolak mentah-mentah!", "Tidak sudi saya bekerjasama!", "Pergi sana kamu!"], 1),
            ("友人からの誘いを断る際、関係を悪化させないための最も重要なマナーは？", ["誘ってくれたことへの感謝（Makasih udah diajak）を述べてから理由を添える", "既読無視して放置する", "怒ってブロックする", "悪口を言いふらす"], 1),
            ("ビジネスの価格交渉で値引きを断る際、「原価限界（これ以上は赤字）」を理由にするメリットは？", ["私利私欲ではなく客観的なビジネスの限界として相手が納得しやすいから", "相手を脅迫できるから", "法律で決まっているから", "相手が泣いて謝るから"], 1)
        ]
    },
    {
        "slug": "22-addressing-awkward-topics",
        "title": "【戦略会話】気まずい話題の切り出し：納期遅延・金銭・ミスの報告を申し訳なさそうに切り出す",
        "intro": "言いにくいこと（納期の遅延、作業ミス、貸したお金の催促、契約の不備）を伝える際、前置きなしに直球で切り出すと相手の防衛本能を刺激し、怒りや摩擦を生みます。「Sebenarnya agak berat menyampaikannya...（実は申し上げにくいのですが…）」「Ada hal yang perlu kami luruskan...（修正が必要な点がありまして…）」と、心理的クッションを置いてスマートに切り出す技術を訓練します。",
        "pairs": [
            ("Sebenarnya ada hal yang agak berat untuk disampaikan...", "Sebenernya agak gak enak nih ngomongnya...", "切り出しクッション"),
            ("Terkait kendala yang tidak kami duga...", "Ada kendala tak terduga nih...", "不測の事態の前置き"),
            ("Mohon maaf bila hal ini menimbulkan ketidaknyamanan.", "Sori ya kalo bikin gak nyaman.", "事前のお詫び"),
            ("Boleh minta waktu empat mata sebentar?", "Bisa ngobrol berdua bentar gak?", "個別相談の打診")
        ],
        "drill": [
            ("【ビジネス】実は申し上げにくいのですが、納期が2日ほど遅れる見込みです。（Sebenarnya agak berat menyampaikan, tapi jadwal tampaknya mundur dua hari.）", "Sebenarnya agak berat bagi kami menyampaikan hal ini, namun akibat kendala teknis tak terduga, penyelesaian draf tampaknya mundur dua hari.", "スブヌルニャ アガッ ブラット バギ カミ ムンニャムパイカン ハル イニ、ナムン アキバット クンダラ テクニス タッ トゥルドゥガ、プニュレサイアン ドラフ タンパッニャ ムンドゥール ドゥア ハリ", "納期遅延の切り出し。"),
            ("【日常会話】ちょっと言いにくいんだけど、この前のお金返してもらえる？（Agak gak enak ngomongnya, tapi bisa balikin uang kemarin?）", "Bro sebenernya agak gak enak nih nagihnya, tapi uang yang lu pinjem kemarin bisa ditransfer sekarang gak? Soalnya gue lagi butuh mendesak.", "ブロ スブヌルニャ アガッ ガッ エナッ ニ ナギニャ、タピ ウアン ヤン ル ピンジェム クマレン ビサ ディトランスファー スカラン ガッ？ ソアルニャ グエ ラギ ブトゥ ムンデザッ", "借金の切り出し。"),
            ("【ミス報告】私の不手際により、計算ミスが発生してしまいました。（Terjadi kelalaian perhitungan dari pihak saya.）", "Mohon maaf Bapak, dengan penuh rasa tanggung jawab saya ingin melaporkan bahwa terjadi selisih angka dalam pembukuan kemarin.", "モホン マアフ バパッ、ドゥンガン プヌ ラサ タングン ジャワブ サヤ インギン ムンラポルカン バフワ トゥルジャディ スリスィ アンカ ダラム プンブクアン クマレン", "ミスの自己申告。"),
            ("【契約の不備】契約書に記載されていない追加費用が発生しそうです。（Tampaknya timbul biaya tambahan di luar klausul.）", "Ada satu klausul teknis di lapangan yang perlu kita bicarakan bersama, berhubung muncul potensi biaya logistik tambahan.", "アダ サトゥ クラウスル テクニス ディ ラパンガン ヤン プル キタ ビチャラカン ブルサマ、ブルフブン ムンチュル ポテンスィ ビアヤ ロギスティック タンバハン", "追加費用の相談。"),
            ("【別れの切り出し】私たちの将来について、真剣に話し合いたいことがあります。（Ada hal serius tentang masa depan kita yang perlu dibicarakan.）", "Bisa kita luangkan waktu bicara berdua akhir pekan ini? Ada hal penting terkait kelanjutan hubungan kita yang ingin saya sampaikan.", "ビサ キタ ルアンカン ワクトゥ ビチャラ ブルドゥア アキール プカン イニ？ アダ ハル プンティン トゥルカイット クランジュタン フブンガン キタ ヤン インギン サヤ サンパイカン", "関係見直しの切り出し。"),
            ("【同僚の悪癖】体臭や口臭について、プライドを傷つけずにそっと伝える。（Menegur aroma tubuh secara sangat berhati-hati empat mata.）", "Bro ngobrol empat mata yuk di luar bentar... lu lagi gak bawa permen ya? Nih gue ada stok permen mint segar, cobain deh.", "ブロ ンオブロル エンパット マタ ユッ ディ ルアル ブンタル... ル ラギ ガッ バワ プルメンド ヤ？ ニ グエ アダ ストック プルメン ミント スガール、チョバイン デ", "デリケートな衛生面の配慮。"),
            ("【退職の申し出】部長、本日は今後のキャリアについてご相談がございます。（Pak, mohon waktu untuk mendiskusikan rencana karier saya.）", "Selamat siang Bapak, apabila Bapak memiliki waktu luang hari ini, ada hal krusial terkait masa depan karier saya yang ingin saya konsultasikan.", "スラマット スィアン バパッ、アパビラ バパッ ムミリキ ワクトゥ ルアン ハリ イニ、アダ ハル クルシアル トゥルカイット マサ ドゥパン カリエル サヤ ヤン インギン サヤ コンスルタスィカン", "退職・転職の相談切り出し。"),
            ("【評価の不満】人事評価のフィードバックについて、詳細をお伺いしてもよろしいですか。（Boleh meminta penjelasan detail atas hasil evaluasi kinerja?）", "Mohon izin Bapak, terkait hasil rapor evaluasi semester ini, bolehkah saya meminta arahan agar memahami bagian mana yang perlu saya genjot?", "モホン イジン バパッ、トゥルカイット ハシル ラポール エヴァルアスィ スメステル イニ、ボレカ サヤ ミンタ アラハン アガル ムンパハミ バギアン マナ ヤン プル サヤ ゲンジョット", "人事評価の質問切り出し。"),
            ("【病状の告白】実は持病があり、激しい運動や残業ができない状態です。（Sebenarnya saya memiliki riwayat penyakit kronis.）", "Sebagai bentuk keterbukaan, saya ingin menginformasikan bahwa saya memiliki riwayat asma yang memerlukan pantauan medis khusus.", "スバガイ ブントゥッ クトゥルブカアン、サヤ インギン ムンインフォルマスィカン バフワ サヤ ムミリキ リワヤット アスマ ヤン ムムルルカン パントウアン メディス カス", "健康状態の告白。"),
            ("【企画の却下】大変素晴らしい発想ですが、現段階での採用は見送らせてください。（Gagasan yang sangat cemerlang, namun implementasinya ditangguhkan.）", "Konsep yang teman-teman buat sungguh luar biasa; namun dengan mempertimbangkan prioritas korporasi saat ini, kami putuskan untuk menyimpan ide ini sebagai tabungan masa depan.", "コンセプ ヤン トゥムン トゥムン ブアット スング ルアル ビアサ；ナムン ドゥンガン ムムプルティンバンカン プリオリタス コルポラスィ サアット イニ、カミ プトゥスカン ウントゥッ ムンユンパン イデ イニ スバガイ タブンガン マサ ドゥパン", "企画却下の優しい切り出し。"),
            ("【不倫・密告】職場のコンプライアンスに関わる重大な事実を目撃してしまいました。（Saya menyaksikan pelanggaran etika serius di divisi kita.）", "Izin bicara sangat tertutup Pak... ini terkait integritas dan kode etik tim yang saya amati secara langsung di lantai kerja.", "イジン ビチャラ サンガット トゥルトゥップ パッ... イニ トゥルカイット インテグリタス ダン コデ エティカ ティム ヤン サヤ アマティ スチャラ ランスン ディ ランタイ クルジャ", "内部通報の切り出し。"),
            ("【値上げの告知】原材料費の高騰に伴い、来月より価格改定をお願いせざるを得ません。（Terpaksa menyesuaikan harga akibat lonjakan biaya bahan baku.）", "Surat edaran ini sungguh berat kami terbitkan, namun lonjakan biaya impor bahan baku memaksa kami melakukan penyesuaian tarif sebesar 5%.", "スラット エダラン イニ スング ブラット カミ トゥルビットカン、ナムン ロンジャカン ビアヤ インポール バハン バク ムマクサ カミ ムラクカン プニュスアイアン タリフ スブサール リマ パーセン", "価格改定の切り出し。"),
            ("【友人のミス指摘】あなたの言っている数字、1桁間違っているよ。（Angka yang lu sebut tadi kelebihan satu nol lho.）", "Bro jangan tersinggung ya, tapi data yang lu tunjukin di depan klien tadi kayaknya kelebihan satu angka nol deh, buruan ralat!", "ブロ ジャンガン トゥルスィングン ヤ、タピ データ ヤン ル チュンジュッキン ディ ドゥパン クライエン タディ カヤッニャ クリビハン サトゥ アンカ ノル デ、ブルアン ララット", "友人のミスを庇う切り出し。"),
            ("【家族への相談】実は会社を辞めたいと思っているんだ。（Sebenarnya aku berniat mengajukan pengunduran diri dari kantor.）", "Sayang, ada hal besar yang pengen aku obrolin malam ini soal kebahagiaan dan beban kerja aku di kantor selama ini.", "サヤン、アダ ハル ブサール ヤン ペンゲン アク ンオブロリン マラム イニ ソアル クバハギアアン ダン ブバン クルジャ アク ディ カントール スラマ イニ", "家族への重大相談。"),
            ("【総括】言いにくい真実を誠実に切り出せる者こそ、真のリーダーである。（Keberanian menyampaikan kabar pahit dengan kelembutan adalah mahkota integritas.）", "Jangan menunda kabar buruk: buka dengan empati, paparkan fakta dengan tenang, dan tawarkan jalan keluar!", "ジャンガン ムヌンダ カバル ブルック：ブカ ドゥンガン エンパティ、パパルカン ファクタ ドゥンガン トゥナン、ダン タワルカン ジャラン クルアル", "気まずい話題の哲学。")
        ],
        "quiz": [
            ("相手に言いにくい重大な話題を切り出す際、最も適切なクッション言葉は？", ["Sebenarnya agak berat / tidak enak menyampaikan hal ini...", "Hei kamu bodoh!", "Dengarkan saya sekarang juga!", "Tertawalah bersamaku!"], 1),
            ("デリケートな問題（身だしなみやプライベートなミス）を指摘する際のマナーとして鉄則なのは？", ["他人のいない場所で1対1（bicara empat mata）で伝えること", "全員の前で大声でバカにすること", "SNSで拡散して晒すこと", "黙って陰口を叩くこと"], 1),
            ("納期遅延やミスを報告する際、相手の怒りを最小限に抑えるための必須要素は？", ["ミスの事実だけでなく、具体的な打開策や新しい完了見込み日程をセットで提示すること", "すべて他人のせいにして逃げること", "泣き真似をして同情を引くこと", "会社を無断欠勤すること"], 1)
        ]
    },
    {
        "slug": "23-humor-easing-tension",
        "title": "【戦略会話】ユーモアで場を和らげる：失敗やミスをした時に笑顔で雰囲気をほぐす一言",
        "intro": "インドネシア社会はユーモア（Guyonan / Candaan）を愛する文化です。ミスを犯したり気まずい空気が流れた時、深刻になりすぎてフリーズするのではなく、自虐や機転の利いた一言でクスッと笑わせ、場の緊張を一瞬でほぐす「ユーモア・サバイバル術」を習得します。",
        "pairs": [
            ("Maklum ya, maklum faktor usia...", "Faktor 'U' nih bro, maklum ya!", "自虐ネタ（年齢・疲労）"),
            ("Untung kopinya belum tumpah...", "Untung bukan gue yang jatoh!", "不幸中の幸いジョーク"),
            ("Namanya juga manusia, tempatnya salah...", "Manusiawi lah ya, bukan robot!", "人間らしさへの帰着"),
            ("Jangan tegang-tegang amat, senyum dikit napa!", "Tegang amat, kayak mau ujian!", "緊張緩和の声かけ")
        ],
        "drill": [
            ("【言い間違い自虐】すみません、舌がまだ朝ご飯を消化していないようです！（Lidah saya belum sarapan nih.）", "Waduh mohon maaf lidah saya agak keseleo barusan, maklum kopinya belum nendang nih pagi-pagi!", "ワドゥ モホン マアフ リダ サヤ アガッ クスレオ バルサン、マクルム コピニャ ブルム ネンダン ニ パギ パギ", "言い間違いを笑いに変える。"),
            ("【物忘れ】年齢のせいですね、若さの有効期限が切れたみたいです。（Faktor usia nih, garansi mudanya sudah habis.）", "Aduh faktor 'U' (umur) nih bro, ram memori di kepala gue mendadak minta upgrade!", "アドゥ ファクトール 'ウー'（ウムール）ニ ブロ、ラム メモリ ディ クパラ グエ ムンダダッ ミンタ アップグレード", "ど忘れの自虐ジョーク。"),
            ("【書類落下】おっと、書類が私より先に床に挨拶したがっています！（Dokumennya pengen sungkem ke lantai duluan.）", "Waduh, kertas-kertasnya buru-buru pengen sujud syukur ke lantai nih saking semangatnya!", "ワドゥ、クルタス クルタスニャ ブルブル ペンゲン スジュッド シュクール ク ランタイ ニ サキン スマンガットニャ", "書類を落とした時のジョーク。"),
            ("【会議の沈黙】皆さん緊張しすぎですよ、処刑台じゃないんですから！（Tegang amat, bukan ruang pengadilan kok!）", "Santai aja rekan-rekan, kok tegang bgt mukanya kayak mau disuntik imunisasi massal!", "サンタイ アジャ ルカン ルカン、コッ トゥガン バンゲット ムカニャ カヤッ マウ ディスンティッ イムニサスィ マッサル", "重い空気の打破。"),
            ("【道迷い】目的地が恥ずかしがって隠れてるみたいですね！（Tampaknya gedungnya lagi main petak umpet.）", "Gedung kantornya kayaknya lagi malu-malu kucing nih pak sopir, suka bgt main petak umpet sama kita!", "グドゥン カントールニャ カヤッニャ ラギ マル マル クチン ニ パッ ソピール、スカ バンゲット マイン プタッ ウムペット サマ キタ", "迷子時の和ませ。"),
            ("【お腹の音】お腹が発言権を主張して鳴っちゃいました！（Perut saya ikut bersuara minta jatah makan siang.）", "Aduh maaf suara keroncongan tadi, cacing di perut saya ikut interupsi minta jatah makan siang!", "アドゥ マアフ スアラ クロンチョンガン タディ、チャチン ディ プルット サヤ イクット インテルプスィ ミンタ ジャタ マカン スィアン", "お腹の鳴りへの対処。"),
            ("【転倒自虐】地面の品質検査をしてただけですよ！（Lagi ngecek kualitas ubin lantai kok!）", "Gak apa-apa guys, gak luka kok, tadi cuma mau ngecek seberapa kokoh keramik lantainya aja!", "ガッ アパ アパ ガイズ、ガッ ルカ コッ、タディ チュマ マウ ンゲチェック スブラパ ココ クラミック ランタイニャ アジャ", "転んだ時のジョーク。"),
            ("【計算ミス】算数の先生に謝らなきゃいけませんね。（Mesti minta maaf ke guru matematika SD nih.）", "Aduh saya mesti sungkem minta maaf ke guru matematika SD saya nih, kalkulatornya salah pencet!", "アドゥ サヤ ムスティ スンケム ミンタ マアフ ク グル マテマティカ エスデー サヤ ニ、カルクラトールニャ サラ ペンチェット", "計算ミスの笑い転換。"),
            ("【食べこぼし】服も美味しそうなカレーを味わいたかったみたいです。（Baju saya juga pengen ikutan makan kare.）", "Duh bajunya iri nih, pengen ikutan icip saus rendang yang sedap ini!", "ドゥ バジュニャ イリ ニ、ペンゲン イクタン イチップ サウス ルンダン ヤン スダップ イニ", "服に汁を飛ばした時。"),
            ("【名前ど忘れ】かっこよすぎて名前を見とれて忘れちゃいました！（Saking terpesonanya sampe lupa nama.）", "Saking terpukaunya saya sama gaya keren Bapak, sampe memorinya nge-blank sesaat lupa nama!", "サキン トゥルプカウニャ サヤ サマ ガヤ クレン バパッ、サンペ メモリニャ ンゲブランク スサアット ルパ ナマ", "名前忘れの褒め殺しジョーク。"),
            ("【雨天中止】雨の神様が私たちに休めと言ってるんですね。（Dewa hujan menyuruh kita istirahat dulu sejenak.）", "Hujan berkah nih, semesta kayaknya kompak nyuruh kita santai ngopi dulu daripada macet-macetan di jalan.", "フジャン ブルカ ニ、スムスタ カヤッニャ コンパック ニュル キタ サンタイ ンオピ ドゥル ダルィパダ マチェット マチェッタン ディ ジャラン", "雨天中止のポジティブ転換。"),
            ("【長引く会議】皆さんのお腹が空く前に早くまとめましょう！（Sebelum ada yang pingsan kelaparan, mari kita bungkus!）", "Sebelum aroma nasi padang tercium di ruangan ini, yuk kita sepakati kesimpulannya sekarang!", "スブルム アロマ ナスィ パダン トゥルチウム ディ ルアンガン イニ、ユッ キタ スパカティ クスィンプルアンニャ スカラン", "会議の軽妙な締め。"),
            ("【プレゼン機材トラブル】パソコンも金曜日で早く週末休みに入りたいみたいです。（Laptopnya pengen cepet-cepet weekend-an.）", "Laptop saya tampaknya udah kena sindrom 'butuh liburan' nih pak, mendadak ngambek gak mau nyala!", "ラップトップ サヤ タンパッニャ ウダ クナ スィンドロム 'ブトゥ リブラン' ニ パッ、ムンダダッ ンガンベック ガッ マウ ニャラ", "機材トラブルの和ませ。"),
            ("【失敗後の励まし】大丈夫、死ぬわけじゃないし世界はまだ回ってる！（Tenang, kiamat belum tiba, dunia masih berputar!）", "Santai bro, hal kayak gini mah kerikil kecil, bumi masih muter dan kita masih bisa ketawa!", "サンタイ ブロ、ハル カヤッ ブギニ マ クリキル クチル、ブミ マスィ ムテル ダン キタ マスィ ビサ クタワ", "同僚への温かい励まし。"),
            ("【総括】笑いは人と人を結ぶ最短距離の魔法である。（Senyuman dan tawa adalah jembatan terpendek antara dua manusia.）", "Tertawakan ketidaksempurnaan diri sendiri: orang yang pandai mencairkan suasana akan selalu dicintai!", "トゥルタワカン クティダッスンプルナアン ディリ スンディリ：オラン ヤン パンダイ ムンチャイルカン スアサナ アカン スラル ディチンタイ", "ユーモアの真理。")
        ],
        "quiz": [
            ("ミスや物忘れをした際、年齢のせいにして笑い飛ばすインドネシアの定番自虐スラングは？", ["Faktor 'U' (Umur) nih...", "Faktor 'X'...", "Faktor cuaca...", "Faktor uang..."], 1),
            ("会議が重苦しく沈黙している時、「皆さん緊張しすぎですよ！」と和ませる表現は？", ["Tegang amat mukanya, santai aja napa!", "Semuanya harus dihukum!", "Saya benci kalian semua!", "Kalian tidak berguna!"], 1),
            ("対話において適切なユーモア（Guyonan）を使う最大のコミュニケーション上の利点は？", ["場の緊張（tensi）を一瞬でほぐし、心理的安全性と親近感を高めること", "相手を馬鹿にして優越感に浸ること", "真面目な仕事を放棄すること", "全員を怒らせること"], 1)
        ]
    },
    {
        "slug": "24-apologizing-with-solutions",
        "title": "【戦略会話】謝罪＋代替案の提示：ただ頭を下げるだけでなく、次の打開策をセットで提案する",
        "intro": "ビジネスでもプライベートでも、ただ「Maaf, saya salah（すみません、私が悪かったです）」と平謝りするだけでは信頼を失います。成熟した大人のコミュニケーションでは、「謝罪＋原因の簡潔な説明＋具体的代替案（Plan B）の提示」をセットで行うことで、ピンチを信頼強化のチャンスに変えます。",
        "pairs": [
            ("Sebagai gantinya, kami tawarkan...", "Sebagai gantinya, gimana kalo...", "代替案の提示フレーム"),
            ("Kami bertanggung jawab penuh untuk...", "Gue yang tanggung jawab beresin...", "責任の引き受け"),
            ("Langkah korektif yang kami siapkan adalah...", "Solusinya gini ya...", "改善アクションの差"),
            ("Apakah opsi solusi ini dapat diterima?", "Opsi ini oke gak buat lu?", "代替案の合意確認")
        ],
        "drill": [
            ("【ビジネス】納品遅延を深くお詫び申し上げます。代替として一部製品を本日先行納品いたします。（Mohon maaf atas keterlambatan, sebagai gantinya kami kirimkan sebagian hari ini.）", "Kami memohon maaf atas penundaan ini; sebagai solusi langsung, 30% produk akan kami kirimkan hari ini menggunakan kurir instan dengan biaya penuh kami.", "カミ ムモホン マアフ アタス プヌンダアン イニ；スバガイ ソルスィ ランスン、ティガプル パーセン プロドゥッ アカン カミ キリムカン ハリ イニ ムングナカン クーリエ インスタン ドゥンガン ビアヤ プヌ カミ", "分割先行納品の提案。"),
            ("【日常約束】待ち合わせに遅れて本当にごめん！今日のランチは私が奢るね！（Sori bgt telat, makan siang hari ini gue yang traktir ya!）", "Aduh sori bgt ya bro gue ngaret 20 menit gara-gara macet parah! Sebagai gantinya, ngopi sama makan siang hari ini gue yang bayarin semua!", "アドゥ ソリ バンゲット ヤ ブロ グエ ンガレット ドゥアプル ムニット ガラガラ マチェット パラ！ スバガイ ガンティニャ、ンオピ サマ マカン スィアン ハリ イニ グエ ヤン バヤリン スムア", "奢りによる即座リペア。"),
            ("【欠品対応】ご注文の青色が在庫切れでした。代わりに上位モデルの黒色を同価格でいかがですか？（Warna biru habis, bagaimana bila diganti hitam spek lebih tinggi dengan harga sama?）", "Mohon maaf warna biru sedang kosong; sebagai kompensasi, kami tawarkan unit warna hitam dengan spesifikasi lebih tinggi tanpa tambahan biaya.", "モホン マアフ ワルナ ビル スダン コソン；スバガイ コンペンサスィ、カミ タワルカン ユニット ワルナ ヒタム ドゥンガン スペスィフィカスィ ルビ ティンギ タンパ タンバハン ビアヤ", "アップグレード提案。"),
            ("【データ喪失】バックアップから昨日の状態まで復旧可能です。（Bisa dipulihkan dari data cadangan kemarin.）", "Kami sangat menyesalkan hilangnya berkas tadi; tim IT kami bergerak cepat dan dapat memulihkan 95% data dari cadangan kemarin malam.", "カミ サンガット ムニュサルカン ヒランニャ ブルカス タディ；ティム アイティー カミ ブルグラッ チパット ダン ダパット ムムリカン ソンビランプル リマ パーセン データ ダリ チャダンガン クマレン マラム", "リカバリー作業の提示。"),
            ("【日程再調整】明日の会議は出張と重なりました。金曜日の午前に変更願えますでしょうか？（Rapat besok bentrok, bisakah digeser ke Jumat pagi?）", "Mohon maaf sekali agenda besok bertabrakan dengan inspeksi mendadak; apakah memungkinkan bila jadwal pertemuan kita geser ke Jumat pagi pukul 09.00?", "モホン マアフ スカリ アジェンダ ベソッ ブルタブラカン ドゥンガン インスペクスィ ムンダダッ；アパカ ムンムンキンカン ビラ ジャドワル プルトゥムアン キタ ゲセル ク ジュマアット パギ プクル ソンビラン", "確実な代替日時の提示。"),
            ("【料理間違い】注文と違う料理をお出ししてしまいました。すぐ作り直す間、こちらを無料でお召し上がりください。（Salah hidang, silakan nikmati hidangan pembuka ini gratis sembari kami buatkan yang baru.）", "Mohon maaf atas kekeliruan hidangan ini; kami buatkan steak baru sekarang, dan sup jamur ini silakan dinikmati secara cuma-cuma sebagai permohonan maaf kami.", "モホン マアフ アタス ククリルーアン ヒダンガン イニ；カミ ブアットカン ステーキ バル スカラン、ダン スップ ジャムール イニ スィラカン ディニクマティ スチャラ チュマチュマ スバガイ プルモホナン マアフ カミ", "無料前菜の提供。"),
            ("【ホテル騒音】隣室の工事でご迷惑をおかけしております。静かな最上階スイートへ無償アップグレードいたします。（Pindah ke kamar suite lantai atas yang tenang tanpa biaya.）", "Kami mohon maaf atas ketidaknyamanan suara renovasi; kami telah menyiapkan kamar suite di lantai tertinggi yang tenang untuk perpindahan Bapak sekarang.", "カミ モホン マアフ アタス クティダッニャマナン スアラ レノヴァスィ；カミ トゥラ スィアプカン カマール スイート ディ ランタイ トゥルティンギ ヤン トゥナン ウントゥッ プルピンダハン バパッ スカラン", "スイートへの無償変更。"),
            ("【誤送金】口座番号を間違えて振り込んでしまいました。即座に自腹で立て替えて正規口座に送金します。（Saya talangi dulu dana pribadinya sekarang.）", "Terjadi salah transfer ke rekening pihak lain; agar operasional tidak terganggu, saya talangi dulu dari rekening pribadi saya detik ini juga.", "トゥルジャディ サラ トランスファー ク ルケニング ピハッ ライン；アガル オペラシオナル ティダッ トゥルガング、サヤ タランギ ドゥル ダリ ルケニング プリバディ サヤ ドゥティッ イニ ジュガ", "個人立替による即時解決。"),
            ("【破損事故】お借りしたカメラを落としてしまいました。全額修理費を負担するか、同等新品を購入いたします。（Saya tanggung biaya reparasi penuh atau beli baru.）", "Aduh gue minta maaf sebesar-besarnya kamera lu jatuh lecet; gue siap tanggung seratus persen biaya servis resmi, atau gue ganti unit baru yang setara.", "アドゥ グエ ミンタ マアフ スブサール ブサールニャ カメラ ル ジャトゥ レチェット；グエ スィアップ タングン スラトゥス パーセン ビアヤ サーヴィス レスミ、アタウ グエ ガンティ ユニット バル ヤン スタラ", "完全弁償の申し出。"),
            ("【資料不備】グラフの一部が未完成でした。本日20時までに完全版を再送いたします。（Laporan versi final lengkap dikirimkan sebelum pukul 20.00.）", "Mohon maaf bagan analisisnya belum lengkap tercantum; kami lemburkan tim analis untuk mengirimkan versi revisi paripurna sebelum pukul delapan malam ini.", "モホン マアフ バガン アナリスィスニャ ブルム ルンカップ トゥルチャントゥム；カミ レンブールカン ティム アナリス ウントゥッ ムンキリムカン ヴェルスィ レヴィスィ パリプルナ スブルム プクル ドラパン マラム イニ", "当日夜の修正版提出。"),
            ("【車内清掃】タクシー車内に飲み物をこぼしてしまいました。洗車・クリーニング代をお支払いします。（Saya bayar biaya cuci salon mobilnya pak.）", "Aduh maaf sekali pak minumannya tumpah di jok mobil; saya tambahkan uang lima ratus ribu ya untuk biaya salon cuci joknya hari ini.", "アドゥ マアフ スカリ パッ ミヌマンニャ トゥムパ ディ ジョッ モビル；サヤ タンバカン ウアン リマ ラトゥス リブ ヤ ウントゥッ ビアヤサロン チュチ ジョックニャ ハリ イニ", "清掃代金の自発的上乗せ。"),
            ("【参加辞退の埋め合わせ】今回のイベントには参加できませんが、協賛金として支援させていただきます。（Tidak bisa hadir langsung, namun kami dukung lewat sponsor.）", "Mohon maaf kami tidak dapat hadir secara fisik di seminar tersebut; namun sebagai bentuk dukungan penuh, kami salurkan dana sponsor senilai 10 juta rupiah.", "モホン マアフ カミ ティダッ ダパット ハディール スチャラ フィスィッ ディ セミナール トゥルスブット；ナムン スバガイ ブントゥッ ドゥクンガン プヌ、カミ サルールカン ダナ スポンサー スニライ スプル ジュタ ルピア", "協賛による支援。"),
            ("【フライト遅延】機材トラブルで4時間遅延いたします。ミールクーポンと空港ラウンジをご利用いただけます。（Kupon makan dan akses lounge bandara gratis selama menunggu.）", "Penerbangan tertunda empat jam demi keselamatan teknis; seluruh penumpang berhak mendapatkan kupon makan senilai 150 ribu beserta akses ruang tunggu eksekutif.", "プヌルバンガン トゥルトゥンダ エンパット ジャム ドゥミ クスラマタン テクニス；スルルー プヌンパン ブルハッ ムンダパットカン クポン マカン スニライ スラトゥス リマプル リブ ブルスルタ アクセス ルアン トゥング エクセクティフ", "空港待機の補償。"),
            ("【作業遅延の挽回】週末に休日出勤して月曜朝には必ず間に合わせます。（Kami lembur akhir pekan agar tuntas Senin pagi.）", "Keterlambatan fase satu akan kami tebus dengan pengerjaan lembur akhir pekan, sehingga pada hari Senin pukul 08.00 pagi target utama tetap terkejar.", "クトゥルランバタン ファセ サトゥ アカン カミ テブス ドゥンガン プンクルジャアン レンブール アキール プカン、スヒンガ パダ ハリ スニン プクル ドラパン パギ ターゲット ウタマ トゥタップ トゥルケジャール", "休日出勤による挽回確約。"),
            ("【総括】失敗の後の身の処し方こそが、人間の真価を証明する。（Cara seseorang merespons kesalahannya adalah cermin sejati karakternya.）", "Minta maaf itu kewajiban moral; membawa solusi konkret adalah keahlian profesional!", "ミンタ マアフ イトゥ クワジバン モラル；ムンバワ ソルスィ コンクレット アダラ クアリアン プロフェシオナル", "謝罪と解決策の原則。")
        ],
        "quiz": [
            ("ミスやトラブルで謝罪する際、相手の信頼を失わないプロフェッショナルの鉄則は？", ["謝罪の言葉とともに、具体的で現実的な代替案・解決策（solusi konkret）を提示すること", "ただ何十回も頭を下げて泣き続けること", "責任を部下や外部のせいにして自分は逃げること", "問題が発覚しないよう隠蔽すること"], 1),
            ("遅刻や不手際のお詫びとして「その代わりに（Sebagai gantinya...）」と申し出る表現の意味は？", ["代替として・その埋め合わせとして", "何の関係もなく", "勝手に決めたこととして", "忘れたことにして"], 1),
            ("欠陥商品やサービス不備に対して「上位モデルへの無償交換（upgrade）」を提示するビジネス的意図は？", ["顧客の不満を感動・満足に変え、将来的なロイヤルカスタマーとして維持するため", "会社のお金をわざと減らすため", "在庫処分のため", "店員が早く帰りたいから"], 1)
        ]
    },
    {
        "slug": "25-asking-for-urgent-help",
        "title": "【戦略会話】緊急SOS救助要請：盗難・スリ・事故・急病の現場で周囲の助けを即座に呼ぶ",
        "intro": "海外滞在中に最も命に関わるのが、スリ・強盗、交通事故、急病、火災などの緊急事態（situasi darurat）です。パニックに陥って声が出なくなるのを防ぎ、「Tolong!（助けて！）」「Maling!（泥棒！）」「Panggil ambulans!（救急車を呼んで！）」など、最短の音節で周囲の人々を動員し救助を勝ち取るサバイバル命令文を訓練します。",
        "pairs": [
            ("Tolong panggilkan polisi / ambulans!", "Panggil polisi / ambulans cepet!", "緊急通報の要請"),
            ("Telah terjadi kecelakaan / pencopetan!", "Ada copet / tabrakan tuh!", "事件・事故の叫び"),
            ("Saya membutuhkan pertolongan medis segera.", "Butuh dokter cepet, gak kuat!", "医療救護の要請"),
            ("Tolong amankan pelaku ini!", "Tangkap tuh orang, maling!", "犯人逮捕の叫び")
        ],
        "drill": [
            ("【強盗・泥棒】泥棒！泥棒！あの男を捕まえて！（Maling! Maling! Tangkap orang itu!）", "Tolong! Maling! Maling! Tangkap pria berbaju hitam yang lari ke sana!", "トロン！ マリン！ マリン！ タンカップ プリア ブルバジュ ヒタム ヤン ラリ ク サナ", "街頭での泥棒叫喚（Maling）。"),
            ("【スリ被害】財布をすられました！誰か警察を呼んで！（Dompet saya dicopet! Tolong panggil polisi!）", "Copet! Dompet saya baru saja dicopet di dalam busway! Tolong hubungi petugas keamanan sekarang!", "チョペット！ ドンペット サヤ バル サジャ ディチョペット ディ ダラム バスウェイ！ トロン フブンギ プツガス クアマナン スカラン", "公共交通でのスリ被害。"),
            ("【急病・失神】誰か助けて！人が倒れて意識がありません！（Tolong! Ada orang pingsan tidak sadarkan diri!）", "Tolong! Ada orang jatuh pingsan dan tidak sadarkan diri! Siapa saja tolong panggilkan ambulans cepat!", "トロン！ アダ オラン ジャトゥ ピンサン ダン ティダッ サダルカン ディリ！ スィアパ サジャ トロン パンギルカン アンブランス チパット", "意識不明者への救護要請。"),
            ("【交通事故】車に跳ねられました！救急車を呼んでください！（Ada korban tertabrak mobil! Tolong panggil ambulans!）", "Tolong ada kecelakaan tabrak lari di sini! Korbannya berdarah banyak, cepat telepon ambulans 118!", "トロン アダ クチュラカアン タブラッ ラリ ディ スィニ！ コルバンニャ ブルダラ バニャッ、チパット テレポン アンブランス サトゥ サトゥ ドラパン", "ひき逃げ・重傷事故通報。"),
            ("【火災】火事だ！火事だ！全員外へ避難して！（Kebakaran! Kebakaran! Tolong evakuasi ke luar!）", "Kebakaran! Ada api besar dari lantai dua! Cepat evakuasi keluar gedung lewat tangga darurat!", "クバカラン！ アダ アピ ブサール ダリ ランタイ ドゥア！ チパット エヴァクアスィ クルアル グドゥン レワット タンガ ダルラット", "火災発生の避難叫喚。"),
            ("【呼吸困難】息が苦しいです、酸素マスクか医師をお願いします。（Saya sesak napas berat, tolong panggil dokter.）", "Dada saya sakit sekali... sesak napas... tolong carikan dokter atau bawa saya ke IGD rumah sakit terdekat...", "ダダ サヤ サキット スカリ... スサッ ナパス... トロン チャリカン ドクテール アタウ バワ サヤ ク イーゲーデー ルマ サキット トゥルデカット", "自覚症状のSOS。"),
            ("【迷子保護】小さな子どもが親とはぐれて泣いています。（Ada anak kecil terpisah dari orang tuanya.）", "Tolong satpam, anak kecil ini tersesat dan menangis sendirian, boleh umumkan lewat pengeras suara mall?", "トロン サットパム、アナッ クチル イニ トゥルセサット ダン ムナンギス スンディリアン、ボレ ウムムカン レワット プンゲラス スアラ モール", "迷子の館内放送要請。"),
            ("【パスポート紛失】パスポートと全財産を盗まれてしまいました。（Paspor dan seluruh uang saya hilang dicuri.）", "Pak polisi, tas ransel saya berisi paspor dan dompet dicuri orang, saya butuh surat keterangan kehilangan untuk kedutaan.", "パッ ポリシスィ、タス ランセル サヤ ブルイスィ パスポール ダン ドンペット ディチュリ オラン、サヤ ブトゥ スラット クトゥランガン クヒランガン ウントゥッ クドゥタアン", "警察署での被害届。"),
            ("【アレルギーショック】エビアレルギーでアナフィラキシーが起きています。（Saya kena syok anafilaksis alergi udang.）", "Tolong saya alergi udang parah, tenggorokan saya bengkak gak bisa napas, tolong suntikan epinefrin sekarang!", "トロン サヤ アレルギ ウダン パラ、トゥンゴロカン サヤ ブンカッ ガッ ビサ ナパス、トロン スンティカン エピネフリン スカラン", "アレルギーの緊急申告。"),
            ("【暴行・脅迫】助けて！知らない男たちに絡まれています！（Tolong! Saya sedang diancam oleh preman!）", "Tolong! Jangan mendekat! Pergi kalian! Tolong warga sekitar, ada orang berniat jahat mau memeras saya!", "トロン！ ジャンガン ムンドゥカット！ プルギ カリアン！ トロン ワルガ スキタール、アダ オラン ブルニアット ジャハット マウ ムムラス サヤ", "恐喝・チンピラへの威嚇。"),
            ("【水難事故】人が川で溺れています！浮き輪を投げて！（Ada orang tenggelam di sungai! Lempar pelampung!）", "Tolong ada yang hanyut tenggelam di sana! Cepat lemparkan tali atau ban pelampung ke arahnya!", "トロン アダ ヤン ハニュット トゥンゲラム ディ サナ！ チパット レンパルカン タリ アタウ バン プラムプン ク アラニャ", "溺水事故の救助。"),
            ("【車内閉じ込め】車のドアが開かなくなりました、助けて！（Pintu mobil terkunci macet dari dalam!）", "Tolong kami terjebak di dalam mobil, handle pintunya patah dan hawanya sangat panas, tolong buka dari luar!", "トロン カミ トゥルジェバッ ディ ダラム モビル、ハンドル ピントゥニャ パタ ダン ハワニャ サンガット パナス、トロン ブカ ダリ ルアル", "閉じ込め脱出要請。"),
            ("【熱中症】熱中症で目眩がします、水と涼しい場所をください。（Kena heatstroke pusing berat, butuh air dan tempat sejuk.）", "Kepala saya berputar hebat karena kepanasan... tolong beri saya air putih dingin dan tempat teduh...", "プパラ サヤ ブルプタール ヘバット カレナ クパナサン... トロン ブリ サヤ アイル プティ ディンギン ダン トゥムパット トゥドゥ", "熱中症の救護。"),
            ("【日本大使館連絡】日本大使館の緊急連絡先に電話を繋いでください。（Tolong hubungi nomor darurat Kedutaan Besar Jepang.）", "Mohon bantuan petugas untuk menghubungi nomor darurat Kedutaan Besar Jepang di Jakarta segera.", "モホン バントゥアン プツガス ウントゥッ ムンフブンギ ノモール ダルラット クドゥタアン ブサール ジュパン ディ ジャカルタ スグラ", "大使館連絡要請。"),
            ("【総括】恥を捨てて大声で叫ぶこと。それが生死を分ける唯一の防壁である。（Buang rasa gengsi: suara lantang di saat darurat adalah penyelamat nyawa!）", "Jangan berbisik saat bahaya mengancam: teriakkan 'TOLONG' dan 'MALING' sekuat tenaga!", "ジャンガン ブルビスィッ サアット バハヤ ムンアンチャム：トゥリアッカン 'トロン' ダン 'マリン' スクアット トゥナガ", "緊急SOSの鉄則。")
        ],
        "quiz": [
            ("街頭でスリや泥棒を発見した際、周囲の市民を一瞬で動員して犯人を捕まえさせる叫び言葉は？", ["Maling! / Copet!", "Halo apa kabar!", "Selamat makan!", "Terima kasih banyak!"], 1),
            ("急病人や負傷者が発生した際、救急車を呼ぶための正確な指示フレーズは？", ["Tolong panggilkan ambulans sekarang!", "Tolong belikan es krim!", "Tolong nyalakan televisi!", "Tolong tutup jendelanya!"], 1),
            ("緊急事態（盗難・事故・急病）において、最も生存率を高める初期行動は？", ["躊躇や恥じらいを捨て、大声で周囲に助け（Tolong!）を求め、具体的に警察や病院への連絡を指示すること", "隅っこで小さくなって一人で泣くこと", "SNSに愚痴を投稿して待つこと", "諦めて寝ること"], 1)
        ]
    },
    {
        "slug": "26-getting-lost-directions",
        "title": "【戦略会話】道迷いサバイバル：現在地を特定し、目的地への行き方を道行く人から引き出す",
        "intro": "スマートフォンの充電が切れたりGPSが狂ったりして見知らぬ街で迷子になった際、地元の人に声をかけて現在地を把握し、安全に目的地へ辿り着くための「道迷いサバイバル技術」を学びます。「Saya tersesat（道に迷いました）」「Patokannya apa ya?（目印は何ですか？）」など、的確な道案内を引き出す質問術を訓練します。",
        "pairs": [
            ("Mohon maaf, saya tersesat.", "Nyasar nih mas, numpang tanya.", "道迷い申告"),
            ("Bagaimana cara menuju ke...?", "Arah ke... lewat mana ya?", "経路質問の差"),
            ("Apa patokan yang paling mudah?", "Patokannya apa ya biar gampang?", "目印・ランドマーク確認"),
            ("Apakah tempat tersebut bisa ditempuh jalan kaki?", "Bisa jalan kaki apa mesti naek ojek?", "移動手段の確認")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、道に迷ってしまいました。このビルへはどう行けばよろしいでしょうか？（Permisi, saya tersesat. Bagaimana menuju gedung ini?）", "Permisi Bapak, mohon maaf saya tersesat; bagaimanakah rute termudah menuju Menara Astra dari titik ini?", "プルミスィ バパッ、モホン マアフ サヤ トゥルセサット；バガイマナカ ルテ トゥルムダ ムヌジュ メナラ アストラ ダリ ティティッ イニ", "公式な道案内質問。"),
            ("【日常会話】すみません、完全に道に迷っちゃいました！（Punten kang, nyasar parah nih gue!）", "Punten mang, numpang tanya, nyasar nih saya, arah ke Stasiun Bandung lewat mana ya beloknya?", "プンテン マン、ヌンパンタニャ、ニャサール ニ サヤ、アラ ク スタスィウン バンドン レワット マナ ヤ ベロッニャ", "街角での親密な道尋ね。"),
            ("【現在地確認】ここは地図で見るとどのあたりになりますか？（Di peta ini letaknya di sebelah mana ya?）", "Boleh tolong tunjukkan di layar Google Maps ini, posisi kita sekarang persisnya ada di jalan apa ya mas?", "ボレ トロン チュンジュッカン ディ レイヤー グーグルマップス イニ、ポスィスィ キタ スカラン プルスィスニャ アダ ディ ジャラン アパ ヤ マス", "地図上での現在地特定。"),
            ("【目印・ランドマーク】一番わかりやすい目印は何ですか？（Apa patokan gedung paling mudah dikenali?）", "Patokan paling gampang apa ya mas biar saya gak kelewatan? Ada plang pom bensin atau minimarket?", "パトカン パリン ガンパン アパ ヤ マス ビアル サヤ ガッ クレワタン？ アダ プラン ポム ベンスィン アタウ ミニマーケット", "目印（patokan）の確認。"),
            ("【徒歩かバイクか】ここから歩いて行けますか、それともオジェックに乗るべきですか？（Bisa jalan kaki atau harus naik ojek?）", "Kira-kira kalau jalan kaki kejauhan gak ya? Atau mending saya pesan ojol motor aja?", "キラ キラ カロ ジャラン カキ クジャウハン ガッ ヤ？ アタウ メンディン サヤ プサン オジョル モトール アジャ", "移動手段の判断質問。"),
            ("【交差点の指示】次の信号を右ですか、それとも左ですか？（Di lampu merah depan belok kanan atau kiri?）", "Pas ketemu lampu merah di depan itu saya ambil belok kanan atau lurus terus ya pak?", "パス クトゥム ランプ メラ ディ ドゥパン イトゥ サヤ アンビル ベロッ カナン アタウ ルルス トゥルス ヤ パッ", "交差点での分岐確認。"),
            ("【反対車線警告】反対側の道路を歩かないと渡れませんか？（Harus menyeberang ke sisi jalan sebelah?）", "Lokasinya ada di seberang jalan ya? JPO (jembatan penyeberangan orang) terdekatnya ada di mana?", "ロカスィニャ アダ ディ スブラン ジャラン ヤ？ ジェーペーオー（歩道橋）トゥルデカットニャ アダ ディ マナ", "道路横断の確認。"),
            ("【通り過ぎ防止】もし大きなモスクが見えたら行き過ぎですか？（Kalau sudah lewat masjid besar berarti kelewat ya?）", "Kalau saya sudah melihat ada masjid kubah hijau besar, itu artinya saya sudah kelewat jauh ya mas?", "カロ サヤ スダ ムリハット アダ マスジッド クバ ヒジャウ ブサール、イトゥ アルティニャ サヤ スダ クレワット ジャウ ヤ マス", "行き過ぎの目印。"),
            ("【所要時間】歩いて大体何分くらいかかりますか？（Kira-kira berapa menit jalan kaki dari sini?）", "Jalan santai kira-kira makan waktu berapa menit ya pak sampai ke gerbang masuk utamanya?", "ジャラン サンタイ キラ キラ マカン ワクトゥ ブラパ ムニット ヤ パッ サンパイ クゲルバン マスッ ウタマニャ", "所要時間の見積もり。"),
            ("【治安確認】この裏路地を夜間に歩いて通っても安全ですか？（Apakah aman lewat gang kecil ini saat malam?）", "Lewat gang tikus ini aman gak ya buat pejalan kaki malam-malam, atau mending muter lewat jalan raya besar?", "レワット ガン ティクス イニ アマン ガッ ヤ ブアット プジャラン カキ マラム マラム、アタウ メンディン ムテル レワット ジャラン ラヤ ブサール", "夜間の安全性確認。"),
            ("【案内のお願い】すみません、方向音痴なので近くまで案内してもらえませんか？（Boleh tolong antarkan sampai dekat sana?）", "Aduh saya buta arah bgt nih mas, kalau gak merepotkan boleh tolong diantar sampai perempatan depan?", "アドゥ サヤ ブタ アラ バンゲット ニ マス、カロ ガッ ムレポットカン ボレ トロン ディアンタール サンパイ プルムパタン ドゥパン", "方向音痴の引率依頼。"),
            ("【駅・バス停の改札】改札口や乗り場はどこから入ればいいですか？（Pintu masuk peron keretanya lewat mana?）", "Pintu masuk 'tap-in' kartu untuk naik KRL arah Jakarta Kota lewat tangga sebelah mana ya pak satpam?", "ピントゥ マスッ 'タップイン' カルトゥ ウントゥッ ナイッ カーエルエル アラ ジャカルタ コタ レワット タンガ スブラ マナ ヤ パッ サットパム", "駅構内の動線確認。"),
            ("【スマホの充電切れ】携帯の充電が切れてしまって道が調べられません。（Baterai HP saya mati total, tidak bisa cek peta.）", "Baterai ponsel saya mati total nih mas, boleh pinjam charger atau numpang tanya letak halte TransJakarta terdekat?", "バテライ ポンセル サヤ マティ トータル ニ マス、ボレ ピンジャム チャージャー アタウ ヌンパンタニャ ルタック ハルテ トランスジャカルタ トゥルデカット", "充電切れの申告。"),
            ("【タクシー運転手への指示】運転手さん、この住所までナビを見ながら行けますか？（Pak sopir, bisa antar ke alamat ini pakai Google Maps?）", "Pak sopir, ini alamat tujuan saya di aplikasi, tolong ikuti rute jalan tol yang paling cepat ya.", "パッ ソピール、イニ アラマット トゥジュアン サヤ ディ アプリカスィ、トロン イクティ ルテ ジャラン トル ヤン パリン チパット ヤ", "ドライバーへの指示。"),
            ("【総括】口に言葉を持つ者は、決して世界で迷子にならない。（Malu bertanya sesat di jalan; berani bertanya selamat sampai tujuan!）", "Peribahasa Indonesia paling legendaris: 'Malu bertanya sesat di jalan!' Jangan gengsi bertanya!", "ペリバハサ インドネシア パリン レジェンダリス：'マル ブルタニャ スサット ディ ジャラン！' ジャンガン ゲンシ ブルタニャ", "道案内の名言。")
        ],
        "quiz": [
            ("道に迷って人に尋ねる時の最も有名なインドネシアのことわざ「Malu bertanya sesat di jalan」の意味は？", ["尋ねるのを恥ずかしがると道に迷う（聞くは一時の恥、聞かぬは一生の恥）", "道を聞くとお金を取られる", "走れば必ず目的地に着く", "地図を見れば誰でも分かる"], 1),
            ("道案内をしてもらう際、「一番わかりやすい目印・ランドマークは何ですか？」と尋ねる語「patokan」の意味は？", ["目印・基準・ランドマーク", "靴のサイズ", "料理の味", "警察署の電話番号"], 1),
            ("裏路地を通る際、治安が不安な時に「この道を通っても安全ですか？」と確認する表現は？", ["Apakah aman lewat jalan ini?", "Apakah jalan ini sangat mahal?", "Apakah jalan ini terbuat dari kue?", "Berapa banyak mobil di sini?"], 1)
        ]
    },
    {
        "slug": "27-food-allergy-restrictions",
        "title": "【戦略会話】食事制限・アレルギー：宗教規定（ハラル）・食物アレルギー・苦手食材を確実に伝える",
        "intro": "世界最大のムスリム人口を抱えるインドネシアでは、ハラル（Halal: イスラム法で許された食品）とハラム（Haram: 豚肉やアルコールなど禁止された食品）の峻別が日常的に極めて重要です。また、エビ・カニ、ナッツ、グルテンなどのアレルギーやベジタリアン宣言を、命に関わる誤解なく確実に店員へ伝えるフレーズを学びます。",
        "pairs": [
            ("Makanan ini mengandung babi atau alkohol?", "Ada babinya gak mas?", "豚・酒の含有確認"),
            ("Saya memiliki alergi parah terhadap...", "Saya alergi berat sama...", "アレルギーの申告"),
            ("Tolong jangan pakai...", "Jangan pake... ya, tolong pisahkan.", "特定食材の抜き・別皿依頼"),
            ("Apakah minyak yang digunakan halal?", "Minyak gorengnya pake minyak apa mas?", "調理油の確認")
        ],
        "drill": [
            ("【宗教規定】この料理には豚肉やラード（豚油）は一切使われていませんか？（Apakah hidangan ini bebas dari daging babi dan minyak babi?）", "Mohon maaf memastikan, apakah menu ini seratus persen bebas dari daging babi, minyak babi (lard), maupun mirin?", "モホン マアフ ムマスティカン、アパカ メニュー イニ スラトゥス パーセン ベバス ダリ ダギン バビ、ミニャッ バビ（ラード）、マウプン ミリン", "ハラル性の厳密確認。"),
            ("【甲殻類アレルギー】私はエビとカニに激しいアレルギーがあります。（Saya punya alergi sangat parah terhadap udang dan kepiting.）", "Tolong dicatat ya mas, saya punya alergi maut sama udang dan kepiting, sedikit pun jangan sampai kecampur ya!", "トロン ディチャタット ヤ マス、サヤ プニャ アレルギ マウト サマ ウダン ダン クピティン、スディキット プン ジャンガン サンパイ クチャンプール ヤ", "甲殻類アレルギーの警告。"),
            ("【ピーナッツアレルギー】ソースにピーナッツやナッツ類が入っていますか？（Apakah sausnya mengandung kacang tanah?）", "Bumbunya pakai campuran kacang tanah gak ya? Saya ada alergi kacang parah, bisa sesak napas.", "ブムブニャ パケ チャンプラン カチャン タナ ガッ ヤ？ サヤ アダ アレルギ カチャン パラ、ビサ スサッ ナパス", "ナッツアレルギーの確認。"),
            ("【化学調味料抜き】グルタミン酸ナトリウム（MSG/味の素）を入れずに調理してください。（Tolong masak tanpa menggunakan MSG / micin.）", "Bisa tolong minta dibuatkan tanpa micin atau penyedap rasa sama sekali? Cukup garam dan lada saja.", "ビサ トロン ミンタ ディブアットカン タンパ ミチン アタウ プニュダップ ラサ サマ スカリ？ チュクップ ガラム ダン ラダ サジャ", "MSG抜きの依頼。"),
            ("【辛さゼロ要請】辛いものが全く食べられません、唐辛子は一本も入れないでください！（Tidak bisa makan pedas sama sekali, tanpa cabai ya!）", "Tolong jangan pakai cabai sama sekali ya mas, nol cabai, perut saya gak kuat pedas nanti sakit.", "トロン ジャンガン パケ チャバイ サマ スカリ ヤ マス、ノル チャバイ、プルット サヤ ガッ クアット プダス ナンティ サキット", "唐辛子完全抜きの念押し。"),
            ("【ベジタリアン】肉や魚、卵を一切使わない精進料理はありますか？（Ada menu vegetarian tanpa daging, ikan, dan telur?）", "Apakah tersedia pilihan menu vegetarian murni yang tidak menggunakan daging, kaldu hewani, maupun telur?", "アパカ トゥルスディア ピリハン メニュー ヴェゲタリアン ムルニ ヤン ティダッ ムングナカン ダギン、カルドゥ ヘワニ、マウプン トゥルール", "純粋ベジタリアン食の確認。"),
            ("【乳製品アレルギー】牛乳やチーズなどの乳製品は含まれていますか？（Apakah ada kandungan susu atau olahan susu?）", "Minuman atau kuah ini ada campuran susu sapi atau krimernya gak ya? Saya lactose intolerant.", "ミヌマン アタウ クア イニ アダ チャンプラン スス サピ アタウ クリーマーニャ ガッ ヤ？ サヤ ラクトース イントレラント", "乳糖不耐症・乳製品確認。"),
            ("【パクチー抜き】香草（パクチー/コリアンダーの葉）が苦手なので抜いてください。（Tolong jangan pakai daun ketumbar ya.）", "Mas, tolong jangan ditaburi daun ketumbar (wansui) di atas mangkoknya ya, saya kurang suka aromanya.", "マス、トロン ジャンガン ディタブリン ダウン クツンバール（ワンスイ）ディ アタス マンコックニャ ヤ、サヤ クラン スカ アロマニャ", "パクチー（daun ketumbar）抜き。"),
            ("【調理器具の共用】豚肉を切った同じ包丁やまな板を使わないでいただけますか？（Tolong gunakan pisau dan talenan terpisah.）", "Untuk menjaga kehalalan, tolong gunakan pisau dan papan talenan yang terpisah dari pemotongan daging babi ya.", "ウントゥッ ムンジャガ クハララン、トロン グナカン ピサウ ダン パパン タレナン ヤン トゥルピサ ダリ プモトンガン ダギン バビ ヤ", "調理器具のクロスコンタミ防止。"),
            ("【生水・氷への警戒】飲み物の氷は沸騰させた安全な水で作られていますか？（Apakah es batunya dibuat dari air matang?）", "Es batu di minumannya ini dari air matang yang ada lubang bulatnya (es kristal) kan ya mas?", "エス バトゥ ディ ミヌマンニャ イニ ダリ アイル マタン ヤン アダ ルバン ブラットニャ（エス クリスタル）カン ヤ マス", "氷の衛生度確認（es kristal）。"),
            ("【アルコール調味料】料理酒やみりんなどの酒類は使っていますか？（Apakah menggunakan mirin atau arak masak?）", "Saus marinasinya ada campuran arak masak, mirin, atau alkohol gak ya koki?", "サウス マリナスィニャ アダ チャンプラン アラッ マサッ、ミリン、アタウ アルコール ガッ ヤ コキ", "料理酒・みりんの確認。"),
            ("【グルテンフリー】小麦粉を使わずに米粉で作った麺はありますか？（Ada mie dari tepung beras bebas gluten?）", "Apakah mie ini terbuat dari tepung beras (bihun/kwetiau) atau mengandung terigu gandum?", "アパカ ミエ イニ トゥルブアット ダリ トゥプン ブラス（ビフン/クエティアウ）アタウ ムンガンドゥン トリグ ガンドゥム", "グルテンフリー（小麦粉回避）。"),
            ("【別皿提供】ソースを上からかけずに、小皿に分けて添えてもらえますか？（Sausnya dipisah di piring kecil ya.）", "Saus sambalnya tolong jangan langsung disiram ke atas ayamnya ya mas, dipisah aja di mangkok kecil.", "サウス サンバルニャ トロン ジャンガン ランスン ディスィラム ク アタス アヤムニャ ヤ マス、ディピサ アジャ ディ マンコック クチル", "ソース別皿（dipisah）の指定。"),
            ("【ドクターストップ】医者から塩分を控えるように言われています。（Harus membatasi asupan garam atas saran dokter.）", "Tolong masakannya jangan terlalu asin ya koki, tekanan darah saya lagi tinggi atas anjuran dokter.", "トロン マサカンニャ ジャンガン トゥルラル アスィン ヤ コキ、トゥカナン ダラ サヤ ラギ ティンギ アタス アンジュラン ドクテール", "減塩の依頼。"),
            ("【総括】食の安全と信念を伝えることは、自分の身体を守る神聖な権利である。（Menjaga asupan tubuh adalah hak dasar kesehatan dan keyakinan.）", "Jangan malu menegaskan pantangan makanan: jelaskan secara spesifik agar makan dengan tenang dan bahagia!", "ジャンガン マル ムヌガスカン パンタンガン マカナン：ジュラスカン スチャラ スペスィフィッ アガル マカン ドゥンガン トゥナン ダン バハギア", "食事制限の哲学。")
        ],
        "quiz": [
            ("イスラム法で許された食品（Halal）と禁止された食品（Haram）のうち、最も厳重に確認すべき豚肉のインドネシア語は？", ["babi", "ayam", "sapi", "kambing"], 1),
            ("東南アジアの食堂で、氷でお腹を壊さないために「穴の空いた製氷機の安全な氷（es kristal）」か確認する表現は？", ["Es batunya dibuat dari air matang kan ya?", "Es batunya sangat dingin ya?", "Berapa harga es batunya?", "Saya mau beli kulkas"], 1),
            ("唐辛子（cabai）の辛さに極端に弱い日本人が、屋台で「辛さゼロ（唐辛子を一切入れないで）」と念押しするキーワードは？", ["nol cabai / tanpa cabai sama sekali", "tambah cabai sepuluh", "sambal yang banyak", "pedas level lima"], 1)
        ]
    },
    {
        "slug": "28-hotel-room-issue",
        "title": "【戦略会話】ホテル設備トラブル：エアコン故障・お湯が出ない・異臭時の部屋変更交渉術",
        "intro": "ホテルの客室に入った直後、エアコンが効かない、シャワーからお湯が出ない、排水溝から異臭がする、Wi-Fiが繋がらないなどの設備トラブルに直面した際、我慢して泣き寝入りしてはいけません。フロントに冷静かつ断固として状況を伝え、修理スタッフの手配や部屋変更（Pindah kamar）を勝ち取る交渉術を学びます。",
        "pairs": [
            ("AC di kamar tidak dingin sama sekali.", "AC-nya rusak mas, panas bgt!", "エアコン故障の訴え"),
            ("Air panas di kamar mandi tidak menyala.", "Air panasnya gak keluar sama sekali.", "温水不具合の訴え"),
            ("Bolehkah kami meminta pindah kamar?", "Bisa tolong pindah kamar aja gak?", "部屋変更の要求"),
            ("Tolong kirimkan staf teknisi sekarang.", "Kirim teknisi ke kamar skrg ya.", "修理スタッフの派遣要請")
        ],
        "drill": [
            ("【エアコン故障】客室のエアコンが全く冷えず、部屋の中が蒸し風呂状態です。（AC kamar tidak dingin, sangat gerah.）", "Selamat malam resepsionis, AC di kamar 302 tidak dingin sama sekali dan hanya mengeluarkan angin panas, mohon ditindaklanjuti.", "スラマット マラム ルセプスィオニス、エーチェー ディ カマール ティガラトゥス ドゥア ティダッ ディンギン サマ スカリ ダン ハニャ ムンゲルアルカン アンギン パナス、モホン ディティンダッ ランジュティ", "エアコン不調のクレーム。"),
            ("【お湯が出ない】シャワーの給湯器が動いておらず、水しか出ません。（Air shower dingin semua, tidak ada air panas.）", "Mohon maaf, air panas di kamar mandi sama sekali tidak berfungsi, hanya mengalir air dingin seperti es.", "モホン マアフ、アイル パナス ディ カマール マンディ サマ スカリ ティダッ ブルフングスィ、ハニャ ムンアリル アイル ディンギン スプルティ エス", "温水不作動のクレーム。"),
            ("【部屋変更要求】修理に時間がかかるのであれば、別の部屋へ変更していただけますか？（Boleh tolong pindahkan ke kamar lain?）", "Jika perbaikan teknis memakan waktu lebih dari 15 menit, kami mohon untuk dipindahkan ke kamar lain yang setara.", "ジカ プルバイカン テクニス ムマカン ワクトゥ ルビ ダリ リマブラス ムニット、カミ モホン ウントゥッ ディピンダカン ク カマール ライン ヤン スタラ", "部屋変更（pindah kamar）の要求。"),
            ("【異臭トラブル】排水溝から下水の酷い悪臭が上がってきて耐えられません。（Ada bau busuk menyengat dari saluran pembuangan air.）", "Ada bau limbah yang sangat menyengat dari lubang saluran air kamar mandi, ini sangat mengganggu pernapasan kami.", "アダ バウ リンバ ヤン サンガット ムニェンガット ダリ ルバン サルールアン アイル カマール マンディ、イニ サンガット ムンガング プルナパサン カミ", "悪臭トラブルの申告。"),
            ("【清掃不備】シーツに汚れが残っており、前の宿泊客のゴミがゴミ箱に残っています。（Sprei bernoda kotor dan sampah belum dibuang.）", "Sprei tempat tidur tampak kotor bernoda dan tong sampah belum dikosongkan oleh staf kebersihan, mohon diganti baru.", "スプレイ トゥムパット ティドゥール タンパッ コトール ブルノダ ダン トン サンパ ブルム ディコソンカン オレ スタッフ クブルスィハン、モホン ディガンティ バル", "清掃不備の抗議。"),
            ("【隣室の騒音】隣の部屋の宿泊客が大音量で音楽を流していて眠れません。（Kamar sebelah sangat bising memutar musik kencang.）", "Tamu di kamar sebelah berisik sekali memutar musik tengah malam, mohon pihak keamanan menegur mereka sekarang.", "タム ディ カマール スブラ ブルスィッ スカリ ムムタール ムスィック トゥンガ マラム、モホン ピハッ クアマナン ムヌグール ムレカ スカラン", "騒音への警備員派遣要請。"),
            ("【Wi-Fi不通】部屋の中でWi-Fiの電波が拾えず、仕事になりません。（Koneksi Wi-Fi di kamar tidak terdeteksi sama sekali.）", "Sinyal Wi-Fi hotel tidak sampai ke sudut kamar kami, padahal saya harus menghadiri konferensi daring malam ini.", "スィニャル ワイファイ ホテル ティダッ サンパイ ク スドゥット カマール カミ、パダハル サヤ ハルス ムンハディリ コンフェレンスィ ダーリン マラム イニ", "ネット接続不良の訴え。"),
            ("【鍵の不具合】カードキーをかざしてもドアのロックが解除されません。（Kartu kunci tidak bisa membuka pintu kamar.）", "Kartu kunci kamar kami tidak merespons sensor pintu sama sekali, mohon dibantu aktivasi ulang di resepsionis.", "カルトゥ クンチ カマール カミ ティダッ ムレスポン センサー ピントゥ サマ スカリ、モホン ディバントゥ アクティヴァスィ ウラン ディ ルセプスィオニス", "カードキー磁気不良。"),
            ("【水漏れ】洗面台の蛇口から水がポタポタ漏れて止まりません。（Keran wastafel bocor menetes terus-menerus.）", "Pipa di bawah wastafel bocor dan menggenangi lantai kamar mandi, tolong kirimkan staf teknisi sebelum meluap.", "ピパ ディ バワ ワスタフェル ボチョール ダン ムンゲナンギ ランタイ カマール マンディ、トロン キリムカン スタッフ テクニス スブルム ムルアップ", "水漏れ修理要請。"),
            ("【備品不足】タオルとトイレットペーパーが置かれていません。（Tidak ada handuk dan tisu toilet di kamar.）", "Di kamar belum disediakan handuk mandi dan tisu toilet, tolong antarkan dua set handuk bersih ke kamar sekarang ya.", "ディ カマール ブルム ディスディアカン ハンドゥッ マンディ ダン ティス トイレット、トロン アンタルカン ドゥア セット ハンドゥッ ブルスィ ク カマール スカラン ヤ", "アメニティ補充要請。"),
            ("【冷蔵庫故障】ミニ冷蔵庫の電源が入っておらず、飲み物が冷えません。（Kulkas mini mati tidak berfungsi.）", "Kulkas mini di kamar tidak menyala, tolong diperiksa colokannya agar obat saya bisa disimpan di suhu dingin.", "クルカス ミニ ディ カマール ティダッ ムニャラ、トロン ディプルリクサ チョロカンニャ アガル オバット サヤ ビサ ディスィンパン ディ スフ ディンギン", "冷蔵庫故障の申告。"),
            ("【虫の発生】ベッドの上に虫（南京虫/アリ）がいます、即刻部屋を変えてください！（Ada kutu/semut di kasur, tolong ganti kamar segera!）", "Saya menemukan banyak kutu kasur (bed bugs) di balik bantal, ini tidak higienis sama sekali, saya minta ganti kamar detik ini juga!", "サヤ ムヌムカン バニャッ クトゥ カスール（ベッドバグス）ディ バリッ バンタル、イニ ティダッ ヒギエニス サマ スカリ、サヤ ミンタ ガンティ カマール ドゥティッ イニ ジュガ", "害虫による緊急部屋変更。"),
            ("【同等グレードの確認】変更先の部屋も同じキングサイズベッドと窓付きですか？（Kamar pengganti juga tipe king bed dan ada jendela kan?）", "Kamar penggantinya tetap tipe Deluxe dengan ranjang King size dan jendela luar kan ya, bukan tipe yang lebih rendah?", "カマール プンガンティニャ トゥタップ ティペ デラックス ドゥンガン ランジャン キング サイズ ダン ジェンデラ ルアル カン ヤ、ブカン ティペ ヤン ルビ ルンダ", "ダウングレード防止確認。"),
            ("【お詫びサービス】これだけ待たされたのですから、レイトチェックアウトを無料にしてください。（Tolong beri kompensasi late check-out gratis.）", "Karena kami sudah terganggu istirahatnya selama dua jam, apakah pihak hotel berkenan memberikan 'late check-out' gratis besok?", "カレナ カミ スダ トゥルガング イスティラハットニャ スラマ ドゥア ジャム、アパカ ピハッ ホテル ブルクナン ムンブリカン 'レイト チェックアウト' グラティス ベソッ", "レイトチェックアウトの補償要求。"),
            ("【総括】宿泊客として当然の権利を、毅然と礼儀正しく主張せよ。（Menuntut kenyamanan hotel adalah hak konsumen yang berdaulat.）", "Jangan menderita dalam diam: laporkan kerusakan kamar dengan detail, minta kepastian waktu, atau tuntut ganti kamar seketika!", "ジャンガン ムンデリタ ダラム ディアム：ラポルカン クルサカン カマール ドゥンガン ディテイル、ミンタ クパスティアン ワクトゥ、アタウ トゥントゥット ガンティ カマール スクティカ", "ホテルサバイバルの掟。")
        ],
        "quiz": [
            ("ホテルの部屋の設備が壊れていて、別の部屋に変えてほしいと要求する際の最重要フレーズは？", ["Bolehkah kami meminta pindah kamar? (Bisa pindah kamar?)", "Saya mau tidur di lobi", "Tolong tutup hotel ini", "Berapa harga gedung ini?"], 1),
            ("エアコンが冷えず、生温い風しか出ない状態をフロントに説明する表現は？", ["AC tidak dingin sama sekali, hanya keluar angin panas", "AC-nya sangat dingin seperti kutub utara", "Saya suka sekali dengan udaranya", "Tolong matikan semua lampu"], 1),
            ("シャワーのお湯が出ない時、「お湯（air panas）」の反対で水しか出ないことを表す単語は？", ["hanya mengalir air dingin", "air sirup", "air kelapa", "air teh manis"], 1)
        ]
    },
    {
        "slug": "29-airport-transit-trouble",
        "title": "【戦略会話】空港・フライトトラブル：ロストバゲージ・乗り遅れ・遅延時の航空会社カウンター交渉",
        "intro": "海外旅行や出張で最もパニックに陥りやすいのが空港（Bandara）でのトラブルです。預け荷物が出てこない（Lost baggage）、乗り継ぎ便の遅延で接続便に乗り遅れた（Missed connection）、フライトが急遽欠航した際の航空会社カウンターでの補償・振替便交渉サバイバル術を体得します。",
        "pairs": [
            ("Bagasi saya tidak keluar di konveyor.", "Koper saya hilang / belum keluar nih!", "ロストバゲージの申告"),
            ("Penerbangan tertunda sehingga saya tertinggal transit.", "Ketinggalan pesawat lanjutan gara-gara delay!", "乗り継ぎ失敗の訴え"),
            ("Mohon aturkan penerbangan pengganti berikutnya.", "Bisa carikan penerbangan berikutnya?", "振替便の手配要求"),
            ("Apakah disediakan kompensasi hotel dan makanan?", "Dapet hotel sama makan gratis kan?", "補償・宿泊・食事の要求")
        ],
        "drill": [
            ("【ロストバゲージ申告】ターンテーブルが止まりましたが、私のスーツケースが出てきませんでした。（Semua bagasi sudah selesai, tapi koper saya tidak ada.）", "Selamat malam petugas, seluruh bagasi dari penerbangan GA-875 sudah selesai keluar, namun koper perak saya belum tampak di korsel bagasi.", "スラマット マラム プツガス、スルルー バガスィ ダリ プヌルバンガン ジーエー ハチラパンリマ スダ スルサイ クルアル、ナムン コペル ペラッ サヤ ブルム タンパッ ディ コルセル バガスィ", "ロストバゲージの公式申告。"),
            ("【荷物引換証提示】これが私の手荷物引換証（バゲージタグ）の半券です。（Ini nomor bukti klaim bagasi saya.）", "Ini lembar tanda terima bagasi (baggage claim tag) saya yang tertempel di paspor, atas nama Takeshi.", "イニ ルンバール サンダ トゥリマ バガスィ（バゲッジ クレーム タグ）サヤ ヤン トゥルテンペル ディ パスポール、アタス ナマ タケシ", "タグ半券の提示。"),
            ("【外見の特徴説明】黒い大型スーツケースで、赤いリボンを目印に結んでいます。（Koper hitam besar dengan pita merah di pegangannya.）", "Bentuknya koper hardcase besar warna hitam merk Samsonite, dengan pita merah terang terikat di pegangan atasnya.", "ブントゥッニャ コペル ハードケース ブサール ワルナ ヒタム メルク サムソナイト、ドゥンガン ピタ メラ トゥラン トゥリカット ディ プガンガン アタスニャ", "荷物の外見描写。"),
            ("【滞在先への配送要求】見つかり次第、滞在先ホテルまで無料で届けてください。（Tolong antarkan langsung ke hotel bila ditemukan.）", "Begitu kopernya terlacak, mohon segera dikirimkan langsung ke Hotel Kempinski Jakarta tempat saya menginap tanpa biaya tambahan.", "ブギトゥ コペルニャ トゥルラチャッ、モホン スグラ ディキリムカン ランスン ク ホテル ケンピンスキ ジャカルタ トゥムパット サヤ ムンインアップ タンパ ビアヤ タンバハン", "ホテル配送の手配。"),
            ("【緊急必需品手当】着替えと洗面用具を買うための緊急補償金（アメニティキット）は出ますか？（Apakah ada uang kompensasi darurat untuk beli baju ganti?）", "Karena seluruh baju saya ada di dalam koper tersebut, apakah pihak maskapai menyediakan 'overnight allowance' atau 'emergency kit'?", "カレナ スルルー バジュ サヤ アダ ディ ダラム コペル トゥルスブット、アパカ ピハッ マスカパイ ムンニュスディアカン 'オーバーナイト アラワンス' アタウ 'エマージェンシー キット'", "アメニティ補償の要求。"),
            ("【乗り遅れ訴え】貴社の初便が遅延したため、乗り継ぎ便に乗り遅れてしまいました！（Ketinggalan pesawat transit akibat penerbangan pertama delay!）", "Penerbangan pertama kami mengalami keterlambatan dua jam, akibatnya kami ketinggalan pesawat lanjutan ke Denpasar!", "プヌルバンガン プルタマ カミ ムンガラミ クトゥルランバタン ドゥア ジャム、アキバットニャ カミ クティンガラン プサワット ランジュタン ク デンパサール", "接続便乗り遅れの抗議。"),
            ("【振替便の要求】本日中の他社便を含め、最速の振替便を手配してください。（Tolong carikan penerbangan paling awal, termasuk maskapai lain.）", "Mohon bantu carikan penerbangan berikutnya hari ini juga, kami tidak keberatan dipindahkan ke maskapai mitra lain.", "モホン バントゥ チャリカン プヌルバンガン ブルイクットニャ ハリ イニ ジュガ、カミ ティダッ クブラタン ディピンダカン ク マスカパイ ミトラ ライン", "振替便（re-routing）の手配。"),
            ("【宿泊ホテル補償】明日の朝便になる場合、今夜のホテルと送迎バスを用意してください。（Sediakan kamar hotel dan transportasi bila harus terbang besok.）", "Apabila penerbangan pengganti baru tersedia besok pagi, mohon sediakan akomodasi hotel di dekat bandara beserta antar-jemputnya.", "アパビラ プヌルバンガン プンガンティ バル トゥルスディア ベソッ パギ、モホン スディアカン アコモダスィ ホテル ディ ドゥクット バンダラ ブルスルタ アンタルジュンポットニャ", "欠航宿泊の手配。"),
            ("【遅延証明書】保険会社に提出するための公式遅延証明書を発行してください。（Mohon terbitkan surat keterangan keterlambatan penerbangan.）", "Kami memerlukan surat keterangan resmi (delay certificate) yang mencantumkan durasi keterlambatan untuk klaim asuransi perjalanan.", "カミ ムムルルカン スラット クトゥランガン レスミ（ディレイ サーティフィケート）ヤン ムンチャントゥムカン ドゥラスィ クトゥルランバタン ウントゥッ クレイム アスランスィ プルジャラナン", "遅延証明書の発行。"),
            ("【オーバーブッキング】予約確定済みなのに席がないとはどういうことですか？（Kenapa tidak ada kursi padahal tiket sudah konfirmasi?）", "Tiket kami sudah berstatus 'confirmed' sejak dua minggu lalu, mengapa di counter check-in dibilang kursinya overbooked?", "ティケット カミ スダ ブルスタトゥス 'コンファームド' スジャッ ドゥアミング ラル、ムンアパ ディ カウンター チェックイン ディビラン クルスィニャ オーバーブックト", "オーバーブッキングへの抗議。"),
            ("【搭乗口変更】搭乗ゲートが急に変更されたアナウンスを聞き逃しました。（Gerbang keberangkatan mendadak berpindah.）", "Apakah pintu boarding untuk penerbangan ke Tokyo pindah ke gerbang 8? Informasi di layar monitor tampaknya berubah.", "アパカ ピントゥ ボーディング ウントゥッ プヌルバンガン ク トウキョウ ピンダ ク ゲルバン ドラパン？ インフォルマスィ ディ レイヤー モニター タンパッニャ ブルバ", "ゲート変更の確認。"),
            ("【重量超過の交渉】お土産の箱が1キロオーバーしていますが、大目に見てもらえませんか？（Kelebihan satu kilo, boleh tolong diberi toleransi?）", "Kelebihan bagasinya hanya satu kilogram saja nih mbak, isinya oleh-oleh keripik ringan, apakah boleh diberi toleransi kebijaksanaan?", "クリビハン バガスィニャ ハニャ サトゥ キログラム サジャ ニ ムバッ、イスィニャ オレ オレ クリピック リンガン、アパカ ボレ ディブリ トレランスィ クビジャクサナアン", "荷物重量オーバーの交渉。"),
            ("【座席変更】足元の広い非常口座席に変更することは可能ですか？（Bisa pindah ke kursi dekat pintu darurat yang lebih luas?）", "Apakah kursi di baris 'emergency exit' dengan ruang kaki lebih lega masih tersedia untuk kami pilih?", "アパカ クルスィ ディ バリス 'エマージェンシー エグジット' ドゥンガン ルアン カキ ルビ レガ マスィ トゥルスディア ウントゥッ カミ ピリ", "足元広め座席のリクエスト。"),
            ("【車椅子手配】同行者が足を痛めており、搭乗口まで車椅子の手配をお願いできますか？（Bisa tolong siapkan kursi roda sampai ke dalam pesawat?）", "Rekan saya baru saja terkilir kakinya, mohon bantuan kursi roda beserta petugas pengantar hingga masuk ke kabin pesawat.", "ルカン サヤ バル サジャ トゥルキリル カキニャ、モホン バントゥアン クルスィ ロダ ブルスルタ プツガス プンガンタール ヒンガ マスッ ク カビン プサワット", "車椅子アシスタンスの手配。"),
            ("【総括】空港での混乱を制するのは、チケットの控えと毅然とした権利主張である。（Penguasa bandara adalah yang memegang bukti dan bersikap lugas tanpa ragu!）", "Pegang boarding pass Anda, catat nama petugas counter, dan tuntut hak kompensasi secara terhormat!", "プガン ボーディング パス アンダ、チャタット ナマ プツガス カウンター、ダン トゥントゥット ハッ コンペンサスィ スチャラ トゥルホルマット", "空港交渉の真理。")
        ],
        "quiz": [
            ("空港の荷物受け取りターンテーブルからスーツケースが出てこない（ロストバゲージ）時の申告表現は？", ["Koper / bagasi saya tidak keluar di korsel bagasi", "Saya mau beli koper baru", "Koper saya sangat bagus", "Pesawatnya sangat besar"], 1),
            ("乗り継ぎ（transit）に失敗した際、航空会社に「別の最速の振替便を手配してほしい」と要求する表現は？", ["Mohon bantu carikan penerbangan pengganti berikutnya", "Saya mau pulang jalan kaki", "Tolong bakar pesawatnya", "Saya mau tidur di landasan"], 1),
            ("手荷物預け入れ時に搭乗券の裏に貼られる、荷物捜索に不可欠な半券シールの正式名称は？", ["Baggage claim tag (bukti nomor bagasi)", "Paspor", "Visa", "Brosur wisata"], 1)
        ]
    }
]

# 1171-1179の生成
for a in articles_data:
    filepath = os.path.join("docs/strategies", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. 戦略的キラーフレーズ対比表（公式・ビジネス ⇄ 日常会話 ⇄ 緊急サバイバル）\n")
    lines.append("| No | 公式・ビジネス表現 | 日常・カジュアル口語 | 状況・ニュアンス |")
    lines.append("|---|---|---|---|")
    for idx, (baku, gaul, meaning) in enumerate(a['pairs'], 1):
        lines.append(f"| {idx} | `{baku}` | **{gaul}** | {meaning} |")
    lines.append("")
    
    lines.append("## 2. サバイバル戦略・交渉心理のメカニズム\n")
    lines.append("海外や異文化の現場において、予期せぬトラブルや摩擦は避けられません。しかし、適切な言語ストラテジー（意味交渉、クッション言葉、ユーモア、代替案提示、毅然とした権利主張）を用いることで、トラブルは相手との絆を深める最高の機会へと転換されます。\n")
    
    drill_len = len(a['drill'])
    lines.append(f"## 3. 場面別サバイバル・プラクティス（{drill_len}問ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 提示されたシチュエーションと日本語を見て、1〜2秒以内に口頭で適切なサバイバルフレーズを声に出してください。\n")
    
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

# 1180: 総合サバイバル対話シミュレーション（30番勝負＆判定）の生成
f30_path = "docs/strategies/30-comprehensive-survival-test.md"
drill30_data = [
    ("【聞き返し】周囲が騒がしくて聞き取れませんでした、もう一度お願いします。（Suasana bising, boleh diulang kembali?）", "Mohon maaf Bapak, dikarenakan ruangan agak bising, apakah berkenan diulang sekali lagi?", "モホン マアフ バパッ、ディカレナカン ルアンガン アガッ ビスィン、アパカ ブルクナン ディウラン スカリ ラギ", "聞き返しストラテジー。"),
    ("【理解確認】つまり、来週金曜日が提出期限ということで合っていますか？（Berarti batas pengumpulannya Jumat depan kan ya?）", "Jika pemahaman saya tepat, tenggat waktu penyerahan berkasnya adalah Jumat pekan depan kan ya?", "ジカ プマハマン サヤ トゥパット、トゥンガット ワクトゥ プニュラハン ブルカスニャ アダラ ジュマアット プカン ドゥパン カン ヤ", "理解確認チェック。"),
    ("【相手の理解確認】ここまでの私の説明で、分かりにくい点はありますか？（Sampai di sini apakah penjelasan saya cukup jelas?）", "Sampai di titik ini, apakah poin penjelasan kami cukup jelas dan dapat dipahami dengan baik?", "サンパイ ディ ティティッ イニ、アパカ ポイン プンジュラサン カミ チュクップ ジュラス ダン ダパット ディパハムイ ドゥンガン バイッ", "相手の理解度確認。"),
    ("【スピード減速】少し早口すぎるので、ゆっくり話していただけますか？（Kecepatan bicaranya agak terlalu cepat, boleh lebih pelan?）", "Mohon maaf temponya agak terlalu cepat, apakah berkenan berbicara sedikit lebih perlahan?", "モホン マアフ テンポニャ アガッ トゥルラル チパット、アパカ ブルクナン ブルビチャラ スディキット ルビ プルラハン", "速度減速要請。"),
    ("【音量アップ】声が小さくて聞こえないので、もう少し声を張ってください。（Tolong berbicara lebih lantang karena suara kecil.）", "Suaranya agak sayup-sayup terdengar, boleh tolong berbicara lebih lantang sedikit ya mas?", "スアラニャ アガッ サユップ サユップ トゥルドゥンガル、ボレ トロン ブルビチャラ ルビ ランタン スディキット ヤ マス", "音量要請。"),
    ("【迂回：モノ】紙をパチンと留めるホッチキスを貸してください。（Pinjam alat penjepit kertas kawat kecil dong.）", "Boleh pinjam alat kecil dari besi yang fungsinya buat nyatuin lembaran kertas pake kawat (staples)?", "ボレ ピンジャム アラット クチル ダリ ブスィ ヤン フングスィニャ ブアット ニャトゥイン ルンバラン クルタス パケ カワット（ステープルズ）", "ホッチキスの迂回。"),
    ("【迂回：動作】歩いていて石につまずいて転びそうになりました。（Kaki tersandung batu saat berjalan.）", "Tadi pas lagi jalan gak sengaja kakinya nabrak batu di trotoar terus hampir jatuh tersungkur.", "タディ パス ラギ ジャラン ガッ スンガジャ カキニャ ナブラッ バトゥ ディ トロトアール トゥルス ハンピール ジャトゥ トゥルスンクール", "つまずくの動作迂回。"),
    ("【迂回：概念】物価がどんどん上がってお金の価値が下がるインフレ現象。（Fenomena harga naik dan nilai uang turun.）", "Kondisi ekonomi di mana harga barang-barang kebutuhan pokok melonjak terus jadi nilai uang makin menyusut.", "コンディスィ エコノミ ディ マナ ハルガ バラン バラン クブトゥハン ポコッ ムロンジャッ トゥルス ジャディ ニライ ウアン マキン ムニュスット", "インフレの概念迂回。"),
    ("【フィラー】ええと、なんて言うかさ、要するにこういうこと！（Gimana ya ngomongnya, intinya tuh gini!）", "Gimana ya bilangnya... pokoknya mah intinya balik lagi ke persiapan kita dari awal bro!", "ギマナ ヤ ビランニャ... ポコッニャ マ インティニャ バリッ ラギ ク プルスィアパン キタ ダリ アワル ブロ", "沈黙回避フィラー。"),
    ("【自己修正】あ、違った！5万じゃなくて50万ルピアでした！（Eh bukan deng, bukan lima puluh ribu tapi lima ratus ribu!）", "Eh salah sebut gue barusan, bukan lima puluh ribu, tapi lima ratus ribu maksudnya!", "エ サラ スブット グエ バルサン、ブカン リマプル リブ、タピ リマ ラトゥス リブ マクスッドニャ", "金額の即座リペア。"),
    ("【パラフレーズ】別の言葉で言えば、初期投資が回収できたということですね？（Dengan kata lain, modal awal sudah kembali utuh?）", "Dengan kata lain, posisi keuangan kita sudah mencapai titik impas (BEP) kan ya pak?", "ドゥンガン カタ ライン、ポスィスィ クウアンガン キタ スダ ムンチャパイ ティティッ インパス（ビーイーピー）カン ヤ パッ", "専門用語の平易言い換え。"),
    ("【スペル確認】「Takahashi」の綴りは T-A-K-A-H-A-S-H-I です。（Ejaan nama saya adalah Té-Ah-Kah-Ah-Hah-Ah-Es-Hah-I.）", "Nama saya dieja: Té - Ah - Kah - Ah - Hah - Ah - Es - Hah - I, semuanya huruf kecil ya.", "ナマ サヤ ディエジャ：テー - アー - カー - アー - ハー - アー - エス - ハー - イ、スムアニャ フルフ クチル ヤ", "アルファベット綴り確認。"),
    ("【電波障害】電波が悪くて声が途切れています、かけ直します。（Sinyal jelek suara putus-putus, saya telepon balik ya.）", "Sinyalnya kurang stabil dan suara Bapak terputus-putus, izin saya tutup dan hubungi kembali ya.", "スィニャルニャ クラン スタビル ダン スアラ バパッ トゥルプトゥス プトゥス、イジン サヤ トゥトゥップ ダン フブンギ クンバリ ヤ", "通話不良時の掛け直し。"),
    ("【オンライン会議】マイクがミュートになっていますよ！（Mikrofon Anda masih dalam posisi bisu / mute.）", "Mohon maaf Bapak pembicara, tampaknya mikrofon Bapak masih dalam posisi bisu (mute).", "モホン マアフ バパッ プンビチャラ、タンパッニャ マイクロフォン バパッ マスィ ダラム ポスィスィ ビス（ミュート）", "ミュート解除要請。"),
    ("【割り込み】一言だけ重要なデータを補足させてください。（Boleh izin menyela untuk menambah satu data penting?）", "Mohon izin pimpinan menyela sejenak, perkenankan saya menambahkan satu data krusial terkait angka ini.", "モホン イジン ピンピナン ムニュラ スジュナッ、プルクナンカン サヤ ムナンバカン サトゥ データ クルシアル トゥルカイット アンカ イニ", "丁寧な割り込み。"),
    ("【本題復帰】話が逸れてしまいました、元の議題に戻りましょう。（Tadi agak melebar, mari kembali ke topik utama.）", "Pembahasan tadi sudah agak melebar, sekarang mari kita kembali fokus pada agenda utama rapat.", "プンバハサン タディ スダ アガッ ムルバール、スカラン マリ キタ クンバリ フォーカス パダ アジェンダ ウタマ ラパット", "脱線からの復帰。"),
    ("【単語質問】その単語はどういう意味ですか？例文を教えて！（Apa artinya kata itu? Bisa kasih contohnya?）", "Boleh tahu apa arti istilah gaul tersebut mas? Bagaimana contoh penggunaannya dalam kalimat?", "ボレ タウ アパ アルティ イスティラ ガウル トゥルスブット マス？ バガイマナ チョント プングナアンニャ ダラム カリマット", "未知語の質問。"),
    ("【文化説明】「稟議（Ringi）」とは下から上へとハンコを回す決裁制度です。（Ringi adalah sistem persetujuan berjenjang dari bawah ke atas.）", "Ringi itu sistem persetujuan proposal dari staf bawah yang diedarkan ke semua jajaran atasan untuk distempel resmi.", "リンギ イトゥ スィステム プルス トゥジュアン プロポサル ダリ スタッフ バワ ヤン ディエダルカン ク スムア ジャジャラン アタサン ウントゥッ ディステンペル レスミ", "日本文化概念の説明。"),
    ("【価格限界】当社の予算上限は1億ルピアで頭打ちです。（Plafon anggaran kami mentok di angka seratus juta.）", "Plafon anggaran yang disetujui direksi kami mentok di angka seratus juta rupiah, tidak bisa ditambah lagi.", "プラフォン アンガラン ヤン ディストゥジュイ ディレクスィ カミ ムントッ ディ アンカ スラトゥス ジュタ ルピア、ティダッ ビサ ディタンバ ラギ", "予算限界の提示。"),
    ("【苦情対応】ご不快な思いをおかけし申し訳ありません、事実を詳しくお聞かせください。（Mohon maaf atas ketidaknyamanan ini, boleh ceritakan kronologinya?）", "Kami mohon maaf sedalam-dalamnya atas kejadian ini; perkenankan kami mendengarkan kronologi peristiwanya secara utuh.", "カミ モホン マアフ スダラム ダラムニャ アタス クジャディアン イニ；プルクナンカン カミ ムンドゥンガルカン クロノロギ プリスティワニャ スチャラ ウトゥ", "苦情の傾聴初期対応。"),
    ("【丁寧な拒絶】大変魅力的なお話ですが、現時点での参加は困難です。（Penawaran menarik, namun untuk saat ini belum memungkinkan.）", "Penawaran ini sangat terhormat, namun dengan pertimbangan beban kerja saat ini, kami belum dapat berpartisipasi.", "プナワラン イニ サンガット トゥルホルマット、ナムン ドゥンガン プルティンバンガン ブバン クルジャ サアット イニ、カミ ブルム ダパット ブルパルティスィパシ", "角を立てない辞退。"),
    ("【気まずい話題】言いにくいのですが、納期が2日ほど遅れる見込みです。（Agak berat menyampaikan, tapi jadwal mundur dua hari.）", "Sebenarnya agak berat bagi kami menyampaikan hal ini, namun akibat kendala teknis, target penyelesaian tampaknya mundur dua hari.", "スブヌルニャ アガッ ブラット バギ カミ ムンニャムパイカン ハル イニ、ナムン アキバット クンダラ テクニス、ターゲット プニュレサイアン タンパッニャ ムンドゥール ドゥア ハリ", "納期遅延の切り出し。"),
    ("【ユーモア】年齢のせいですね、頭のメモリが一時フリーズしました！（Faktor umur nih, memori kepala mendadak nge-blank!）", "Waduh faktor 'U' nih bro, memori di kepala mendadak nge-blank saking banyaknya yang dipikirin!", "ワドゥ ファクトール 'ウー' ニ ブロ、メモリ ディ クパラ ムンダダッ ンゲブランク サキン バニャッニャ ヤン ディピキリン", "物忘れのユーモア。"),
    ("【謝罪＋代替案】遅延を深くお詫びします、先行して30%を本日納品します。（Mohon maaf atas keterlambatan, sebagai solusinya 30% kami kirim hari ini.）", "Kami memohon maaf atas keterlambatan ini; sebagai langkah solusi, 30% produk kami kirimkan hari ini menggunakan kurir instan.", "カミ ムモホン マアフ アタス クトゥルランバタン イニ；スバガイ ランカ ソルスィ、ティガプル パーセン プロドゥッ カミ キリムカン ハリ イニ ムングナカン クーリエ インスタン", "謝罪と代替案の提示。"),
    ("【緊急SOS】泥棒！泥棒！あの走っている男を捕まえて！（Tolong! Maling! Maling! Tangkap orang itu!）", "Tolong! Maling! Maling! Tangkap pria berbaju hitam yang lari ke arah jalan raya itu!", "トロン！ マリン！ マリン！ タンカップ プリア ブルバジュ ヒタム ヤン ラリ ク アラ ジャラン ラヤ イトゥ", "泥棒の緊急救助要請。"),
    ("【道迷い】道に迷いました、一番わかりやすい目印は何ですか？（Saya tersesat, apa patokan yang paling mudah?）", "Permisi mas, saya tersesat; patokan gedung paling mudah untuk menuju stasiun kereta apa ya di depan?", "プルミスィ マス、サヤ トゥルセサット；パトカン グドゥン パリン ムダ ウントゥッ ムヌジュ スタスィウン クレタ アパ ヤ ディ ドゥパン", "目印の質問。"),
    ("【食事制限】私はエビアレルギーです、唐辛子も一切入れないでください。（Saya alergi udang dan tidak bisa makan cabai sama sekali.）", "Tolong dicatat ya mas, saya punya alergi maut sama udang dan sama sekali tidak bisa makan cabai (nol cabai).", "トロン ディチャタット ヤ マス、サヤ プニャ アレルギ マウト サマ ウダン ダン サマ スカリ ティダッ ビサ マカン チャバイ（ノル チャバイ）", "アレルギーと辛さ制限。"),
    ("【ホテル設備】エアコンが冷えず熱風しか出ません、部屋を変えてください。（AC tidak dingin hanya keluar angin panas, tolong ganti kamar.）", "AC kamar kami tidak dingin sama sekali dan hanya keluar angin panas, mohon kami dipindahkan ke kamar lain sekarang.", "エーチェー カマール カミ ティダッ ディンギン サマ スカリ ダン ハニャ クルアル アンギン パナス、モホン カミ ディピンダカン ク カマール ライン スカラン", "ホテル部屋変更の交渉。"),
    ("【空港トラブル】荷物が出てきません、見つかり次第ホテルへ届けてください。（Koper saya tidak keluar, tolong antarkan ke hotel bila ditemukan.）", "Koper saya tidak kunjung keluar di korsel bagasi; ini nomor klaimnya, mohon segera dikirimkan ke hotel saya bila terlacak.", "コペル サヤ ティダッ クンジュン クルアル ディ コルセル バガスィ；イニ ノモール クレイムニャ、モホン スグラ ディキリムカン ク ホテル サヤ ビラ トゥルラチャッ", "ロストバゲージの交渉。"),
    ("【総括】トラブルを恐れず、対話の力で世界を切り拓け。（Hadapi tantangan komunikasi dengan ketenangan dan strategi unggul!）", "Kuasai seni negosiasi makna: bahasa bukan sekadar hafalan aturan, melainkan jembatan hidup penyambung harapan!", "クアサイ スニ ネゴスィアスィ マクナ：バハサ ブカン スカダール ハファラン アトゥラン、ムラインカン ジュンバタン ヒドゥップ プニャンブン ハラパン", "サバイバル対話の到達点。")
]

lines30 = []
lines30.append("# 【戦略会話総括】総合サバイバル対話シミュレーション30番勝負＆判定クリニック\n")
lines30.append("セクション28で学んだ「聞き返し、理解確認、相手の理解度確認、スピード減速、音量反復、迂回表現（モノ・動作・概念）、沈黙回避フィラー、自己修正リペア、パラフレーズ再陳述、アルファベット綴り確認、電話電波障害、オンライン会議トラブル、丁寧な割り込み、本題復帰、未知語質問、日本文化概念説明、予算限界提示、苦情初期対応、角を立てない拒絶、気まずい話題切り出し、ユーモア、謝罪＋代替案、緊急SOS、道迷い、アレルギー食事制限、ホテル設備、空港トラブル」の全29領域を総括する、30問の完全現場即応サバイバル・シミュレーションです。\n")

lines30.append("## 1. サバイバル対話力・判定基準\n")
lines30.append("| スコア（正答数） | レベル称号 | 診断結果と現場サバイバル能力 |")
lines30.append("|---|---|---|")
lines30.append("| **28 〜 30 問** | **自律サバイバルマスター (Survivor Elite)** | いかなる緊急事態・交渉・設備トラブルにも即座に言語化して主導権を確保できる。 |")
lines30.append("| **22 〜 27 問** | **上級現場適応者 (Advanced Pragmatist)** | 日常的なトラブルや交渉、聞き返しを落ち着いて処理できる頼もしい実務力。 |")
lines30.append("| **15 〜 21 問** | **中級サバイバー (Intermediate)** | 基本的な言い換えや質問はできるが、パニック時に言葉が詰まる傾向がある。 |")
lines30.append("| **0 〜 14 問** | **要支援トラベラー (Novice Needs-Assistance)** | 語彙のド忘れやトラブルに直面した際に黙り込みやすく、積極的な意味交渉の訓練が必要。 |")
lines30.append("")

lines30.append("## 2. 30問総合サバイバル対話シミュレーション\n")
lines30.append("> [!IMPORTANT]")
lines30.append("> **シミュレーション・ルール**: 現場のトラブル状況を想定し、1〜2秒以内に声に出して即座に切り返しフレーズを発話してください。\n")

for idx, (prompt, target_sent, kana, exp) in enumerate(drill30_data, 1):
    m = re.match(r'^(【.+?】)(.+?)（(.+?)）$', prompt)
    if m:
        tag, jp, orig = m.group(1), m.group(2), m.group(3)
        lines30.append(f"### 第{idx}問: {tag}「**{jp}**」（{orig}）\n")
    else:
        lines30.append(f"### 第{idx}問: 「**{prompt}**」\n")
    lines30.append('<div class="id-example">')
    lines30.append(f'<div class="id-sentence"><strong>{target_sent}</strong></div>')
    lines30.append(f'<div class="id-pronunciation">発音: {kana}</div>')
    lines30.append(f'<div class="id-translation">解説: {exp}</div>')
    lines30.append('</div>\n')

lines30.append("## 3. セクション28修了チェッククイズ\n")
quiz30 = [
    ("第二言語習得（SLA）における「意味交渉（Negotiation of Meaning）」の最大の目的は？", ["コミュニケーションの破綻を防ぎ、相手と互いの理解をすり合わせて協働すること", "文法テストで満点を取ること", "相手を言葉で言い負かすこと", "沈黙して相手が察するのを待つこと"], 1),
    ("単語をど忘れした際、道具の用途や外見、動作プロセスを説明して伝える戦略を何と呼ぶ？", ["迂回表現（Circumlocution）", "完全沈黙（Silent Period）", "暴言（Swearing）", "直訳（Literal Translation）"], 1),
    ("トラブルやクレームが発生した際、相手との信頼を強化する最も優れた大人の対応方法は？", ["真摯な心情共感＋謝罪に加えて、具体的で現実的な代替案（solusi / Plan B）をセットで提案すること", "すべてを相手や環境のせいにして言い訳すること", "警察を呼んで威嚇すること", "電話を切って連絡を絶つこと"], 1)
]

for q_idx, (q_text, opts, ans_idx) in enumerate(quiz30, 1):
    lines30.append(f"### 問{q_idx}: {q_text}\n")
    for o_idx, opt in enumerate(opts, 1):
        mark = " (正解)" if o_idx == ans_idx else ""
        lines30.append(f"- [{ 'x' if o_idx == ans_idx else ' ' }] {o_idx}. {opt}{mark}")
    lines30.append("")

with open(f30_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines30))
print(f"Generated: {f30_path}")

print("Batch 1171-1180 generated successfully. Section 28 completed!")
