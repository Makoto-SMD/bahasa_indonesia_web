# -*- coding: utf-8 -*-
import os
import re

os.makedirs("docs/strategies", exist_ok=True)

articles_data = [
    {
        "slug": "01-clarification-request",
        "title": "【戦略会話】聞き返し技術：相手を不快にさせず自然に聞き直す意味交渉フレーズ",
        "intro": "第二言語習得論（SLA）における「意味交渉（Negotiation of Meaning）」の最も基本的な方略が「聞き返し（Clarification Request）」です。聞き取れなかった時に黙り込んだり曖昧に笑ってやり過ごすのではなく、相手に不快感を与えず堂々と聞き直すフレーズを身につけます。",
        "pairs": [
            ("Mohon maaf, boleh diulang kembali?", "Sori, bisa diulang gak barusan?", "反復要請のレジスター差"),
            ("Bagian mana yang kurang jelas?", "Maksudnya gimana ya tadi?", "要点確認のレジスター差"),
            ("Saya kurang dapat menangkap poin terakhir.", "Gak nangkep gue barusan, apa tadi?", "聞き逃し申告のレジスター差"),
            ("Mohon perjelas maksud dari istilah tersebut.", "Maksud kata itu apaan sih?", "語句確認のレジスター差")
        ],
        "drill": [
            ("【ビジネス】申し訳ありません、もう一度繰り返していただけますか？（Mohon maaf, boleh diulang kembali?）", "Mohon maaf Bapak, apakah bisa diulang sekali lagi?", "モホン マアフ バパッ、アパカ ビサ ディウラン スカリ ラギ", "公式で丁寧な反復要請。"),
            ("【日常会話】ごめん、もう一回言ってくれる？（Sori, bisa diulang lagi gak?）", "Sori bro, gak kedengeran barusan, bisa ulang gak?", "ソリ ブロ、ガッ クドゥンゲラン バルサン、ビサ ウラン ガッ", "友人同士の気軽な聞き返し。"),
            ("【会議】最後の部分がうまく聞き取れませんでした。（Saya kurang dapat menangkap bagian terakhir.）", "Bagian terakhir tadi kurang jelas bagi kami, mohon diperjelas.", "バギアン トゥラキール タディ クラン ジュラス バギ カミ、モホン ディプルジュラス", "特定の聞き逃し箇所の指定。"),
            ("【電話】電波が悪くて途切れました。（Suaranya putus-putus karena sinyal buruk.）", "Suara Bapak terputus-putus, bisa tolong diulang poin utamanya?", "スアラ バパッ トゥルプトゥス プトゥス、ビサ トロン ディウラン ポイン ウタマニャ", "通信不良時の聞き返し。"),
            ("【店頭】すみません、最後の単語は何とおっしゃいましたか？（Kata terakhirnya apa tadi ya?）", "Punten mbak, kata yang terakhir tadi apa ya namanya?", "プンテン ムバッ、カタ ヤン トゥラキール タディ アパ ヤ ナマニャ", "聞き慣れない語句への質問。"),
            ("【同僚】え、何て？聞こえなかった！（Hah, apaan? Gak denger gue barusan!）", "Hah gimana tadi? Lagi ribut bgt nih di sini, gak kedengeran!", "ハ ギマナ タディ？ ラギ リブット バンゲット ニ ディ スィニ、ガッ クドゥンゲラン", "騒音下での自然な聞き返し。"),
            ("【商談】今の条件について再度ご確認させてください。（Boleh konfirmasi ulang mengenai syarat tadi?）", "Perkenankan kami mengonfirmasi ulang klausul yang baru saja disebutkan.", "プルクナンカン カミ ムンオンフィルムアスィ ウラン クラウスル ヤン バル サジャ ディスブットカン", "条件の再確認。"),
            ("【雑談】早すぎてついていけなかった！（Cepet bgt ngomongnya, ketinggalan gue!）", "Wah kecepetan bro ngomongnya, pelan-pelan dikit napa!", "ワ クチプタン ブロ ンオモンニャ、プラン プラン ディキット ナパ", "発話速度へのツッコミ。"),
            ("【講義】先生、そのスライドの要点をもう一度お願いします。（Pak, boleh minta poin penting dari slide ini?）", "Mohon izin Pak dosen, apakah poin pada salindia ini dapat dijelaskan ulang?", "モホン イジン パッ ドセン、アパカ ポイン パダ サリンディア イニ ダパット ディジュラスカン ウラン", "大学講義・セミナーでの質問。"),
            ("【カフェ】トッピングの種類をもう一度教えてもらえますか？（Boleh sebutkan pilihan topping-nya lagi?）", "Mas, pilihan rasanya tadi apa aja ya? Lupa saya.", "マス、ピリハン ラサニャ タディ アパ アジャ ヤ？ ルパ サヤ", "選択肢の再提示依頼。"),
            ("【上司報告】恐れ入ります、修正箇所はどこになりますでしょうか？（Mohon maaf, bagian mana yang perlu direvisi?）", "Mohon arahan Bapak, bagian manakah yang secara spesifik perlu kami perbaiki?", "モホン アラハン バパッ、バギアン マナカ ヤン スチャラ スペスィフィッ プル カミ プルバイキ", "修正指示の明確化。"),
            ("【タクシー】どこで曲がるとおっしゃいましたか？（Tadi suruh belok di mana ya pak?）", "Pak sopir, tadi belok kirinya setelah lampu merah atau sebelum?", "パッ ソピール、タディ ベロッ キリニャ ストゥラ ランプ メラ アタウ スブルム", "道案内の詳細確認。"),
            ("【チャット】今のメッセージの意味がよく分かりませんでした。（Maksud pesan tadi kurang saya pahami.）", "Sori, maksud pesan yang barusan itu gimana ya konteksnya?", "ソリ、マクスッド プサン ヤン バルサン イトゥ ギマナ ヤ コンテクスニャ", "テキストチャットの意図確認。"),
            ("【病院】薬を飲むタイミングをもう一度確認させてください。（Kapan waktu minum obat ini sekali lagi?）", "Dok, diminumnya sebelum atau sesudah makan tadi ya? Mohon dipastikan.", "ドッ、ディミヌムニャ スブルム アタウ ススダ マカン タディ ヤ？ モホン ディパスティカン", "医療指示の確実な聞き返し。"),
            ("【総括】聞き返すことは恥ではなく、誠実な対話の証である。（Meminta klarifikasi adalah bukti tanggung jawab komunikasi.）", "Jangan takut minta ulang, daripada salah paham malah berabe!", "ジャンガン タクット ミンタ ウラン、ダルィパダ サラ パハム マラ ブラベ", "意味交渉のマインドセット。")
        ],
        "quiz": [
            ("ビジネスや公の場で相手の話を聞き直す際、最も丁寧で適切な前置きは？", ["Mohon maaf, apakah boleh diulang kembali?", "Apaan sih lu ngomong apa!", "Hah? Gak jelas bgt!", "Bodo amat lah!"], 1),
            ("周囲がうるさくて相手の声が聞こえなかった時に、同僚にカジュアルに聞き直すフレーズは？", ["Sori, gak kedengeran barusan, gimana tadi?", "Saya menolak usulan Anda.", "Silakan keluar dari ruangan.", "Selamat jalan kawan."], 1),
            ("意味交渉（Negotiation of Meaning）において、聞き取れなかった時に最も避けるべき態度は？", ["聞き取れたふりをして曖昧に頷き、誤ったまま放置すること", "笑顔でもう一度言ってほしいと頼むこと", "どの部分が分からなかったかを具体的に伝えること", "メモを取りながら確認すること"], 1)
        ]
    },
    {
        "slug": "02-confirmation-check",
        "title": "【戦略会話】理解確認チェック：「〜ということですか？」と自分の理解を確かめる技術",
        "intro": "相手の発言を聞いた後、「つまりAではなくBということですね」「私の理解が正しければ…」と自分の解釈を言語化して相手にぶつける手法が「理解確認（Confirmation Check）」です。ミスコミュニケーションを未然に防ぐ最強の防波堤となります。",
        "pairs": [
            ("Apakah maksud Saudara adalah...?", "Maksud lu tuh kayak gini ya?", "理解確認のレジスター差"),
            ("Jika tidak salah memahami, artinya...", "Kalo gak salah nangkep, intinya...", "前置きクッションの差"),
            ("Mohon koreksi apabila pemahaman saya keliru.", "Bener gak pemahaman gue?", "訂正要請の差"),
            ("Secara garis besar dapat disimpulkan bahwa...", "Pokoknya intinya begini kan?", "要約確認の差")
        ],
        "drill": [
            ("【ビジネス】私の理解が正しければ、納期は来週金曜日ですね？（Kalau tidak salah paham, batas waktunya Jumat depan ya?）", "Jika pemahaman kami tepat, tenggat waktunya adalah hari Jumat depan, betul?", "ジカ プマハマン カミ トゥパット、トゥンガット ワクトゥニャ アダラ ハリ ジュマアット ドゥパン、ブトゥル", "納期の確認チェック。"),
            ("【日常会話】つまり、彼は今日来られないってこと？（Maksudnya dia gak bisa dateng hari ini?）", "Berarti dia gak jadi dateng nih hari ini, gitu kan maksud lu?", "ブラルティ ディア ガッ ジャディ ダトゥン ニ ハリ イニ、ギトゥ カン マクスッド ル", "友人との状況確認。"),
            ("【会議】要するに、予算を再検討する必要があるということでしょうか。（Intinya anggaran perlu ditinjau ulang?）", "Apakah dapat diartikan bahwa rencana anggaran ini harus kami revisi?", "アパカ ダパット ディアルティカン バフワ レンチャナ アンガラン イニ ハルス カミ レヴィスィ", "論点の確認チェック。"),
            ("【指示確認】この書類を全員にメールで共有すればいいのですね？（Tinggal kirim email dokumen ini ke semua orang ya?）", "Cukup dikirimkan melalui pos-el ke seluruh peserta rapat, betul begitu?", "チュクップ ディキリムカン ムラルイ ポスエル ク スルルー プスルタ ラパット、ブトゥル ブギトゥ", "タスク内容の確認。"),
            ("【価格確認】この金額には税金が含まれているということですか？（Apakah harga ini sudah termasuk pajak?）", "Harga ini sudah 'all-in' termasuk PPN dan ongkir kan ya?", "ハルガ イニ スダ オール イン トゥルマスッ ペーペーエン ダン オンキル カン ヤ", "内税・送料の確認。"),
            ("【道案内】この交差点を右に曲がる、で合っていますか？（Belok kanan di perempatan ini kan ya?）", "Berarti pas perempatan depan ini saya ambil jalur kanan ya pak?", "ブラルティ パス プルムパタン ドゥパン イニ サヤ アンビル ジャルール カナン ヤ パッ", "進行方向の確認。"),
            ("【待ち合わせ】明日の朝9時にロビー集合で間違いないですね？（Besok kumpul jam 9 pagi di lobi ya?）", "Kita fix kumpul jam 9 pagi di lobi hotel kan, gak ada perubahan?", "キタ フィックス クンプル ジャム ソンビラン パギ ディ ロビ ホテル カン、ガッ アダ プルバハン", "集合時間・場所の確認。"),
            ("【トラブル】注文した商品が在庫切れということでしょうか？（Barang yang dipesan sedang habis stok ya?）", "Maksud mbak barangnya lagi kosong dan harus nunggu restock?", "マクスッド ムバッ バランニャ ラギ コソン ダン ハルス ヌング リストック", "欠品状況の確認。"),
            ("【交渉】もし20個買うなら、10%割引になるのですね？（Kalau beli 20 dapat diskon 10% ya?）", "Kalo saya ambil 20 pcs, fix dapet potongan 10% kan ya mas?", "カロ サヤ アンビル ドゥアプル ピーシーズ、フィックス ダペット ポトンガン スプル パーセン カン ヤ マス", "割引条件の確認。"),
            ("【社内】私が先にクライアントへ電話すればよろしいですか？（Saya yang telepon klien lebih dulu ya?）", "Apakah sebaiknya saya yang menginisiasi kontak pertama dengan pihak klien?", "アパカ スバイッニャ サヤ ヤン ムンイニスィアスィ コンタク プルタマ ドゥンガン ピハッ クライエン", "担当役割の確認。"),
            ("【文脈解釈】怒っているのではなく、疲れているだけなのですね？（Bukan marah, cuma capek aja kan?）", "Lu lagi kecapekan aja kan bro, bukan kesel sama kita-kita?", "ル ラギ クチャペカン アジャ カン ブロ、ブカン クセル サマ キタ キタ", "心理状態の確認。"),
            ("【スケジュール】月曜日の会議は中止ではなく延期ですね？（Rapat Senin diundur, bukan dibatalkan ya?）", "Agendanya hanya dijadwalkan ulang dan bukan dibatalkan secara permanen kan?", "アジェンダニャ ハニャ ディジャドワルカン ウラン ダン ブカン ディバタルカン スチャラ プルマネン カン", "延期と中止の区別確認。"),
            ("【料理注文】唐辛子は一切入れないということでよろしいですか？（Sama sekali tidak pakai cabai kan?）", "Benar-benar tanpa cabai sama sekali ya mas, perut saya sensitif.", "ブナル ブナル タンパ チャバイ サマ スカリ ヤ マス、プルット サヤ スンスィティフ", "辛さ抜きの念押し確認。"),
            ("【手続】この用紙にサインするだけで手続き完了ですか？（Tinggal tanda tangan formulir ini saja ya?）", "Apakah proses administrasi ini selesai cukup dengan membubuhkan tanda tangan?", "アパカ プロセス アドミニストラスィ イニ スルサイ チュクップ ドゥンガン ムンブブーカン タンダ タンガン", "手続完了条件の確認。"),
            ("【総括】自分の言葉で言い直すことこそが最強の確認術である。（Menyatakan ulang dengan kata sendiri adalah kunci pemahaman.）", "Pastikan dengan kata-kata sendiri, biar gak ada miskomunikasi di kemudian hari!", "パスティカン ドゥンガン カタ カタ スンディリ、ビアル ガッ アダ ミスコムニカスィ ディ クムディアン ハリ", "確認チェックの哲学。")
        ],
        "quiz": [
            ("相手の話を要約して「つまり〜ということですね？」と確認する定番の接続詞・前置きは？", ["Berarti maksudnya...", "Padahal...", "Meskipun...", "Kecuali..."], 1),
            ("自分の理解が正しいかを丁寧に相手に尋ねる表現「Betul begitu?」の同義表現は？", ["Apakah demikian?", "Siapa Anda?", "Ke mana saja?", "Berapa harganya?"], 1),
            ("ビジネスの契約や条件交渉で、口頭の約束を「fix（確定）」と念押し確認する主な目的は？", ["認識のズレ（miskomunikasi）を防ぎ言質を固めるため", "相手を怒らせるため", "時間を浪費するため", "文法を誇示するため"], 1)
        ]
    },
    {
        "slug": "03-comprehension-check",
        "title": "【戦略会話】相手への理解確認：「伝わっていますか？大丈夫ですか？」と反応を引き出す",
        "intro": "自分が話している途中で、相手が本当に理解してついてきているかを確かめる方略が「相手への理解確認（Comprehension Check）」です。「Sampai di sini jelas?（ここまで分かりましたか？）」「Paham maksud saya?（私の言いたいこと伝わってますか？）」を適切なタイミングで挟むことで、一方通行の独白を防ぎます。",
        "pairs": [
            ("Apakah penjelasan saya cukup jelas?", "Jelas gak penjelasan gue?", "理解確認のレジスター差"),
            ("Sampai di sini apakah ada pertanyaan?", "Ada yang mau ditanyain dulu gak?", "質疑受付の差"),
            ("Apakah instruksi ini dapat dipahami?", "Kira-kira kebayang gak tugasnya?", "イメージ共有の差"),
            ("Mohon konfirmasi bila ada hal yang membingungkan.", "Kalo bingung langsung bilang ya!", "疑問点の申告促し")
        ],
        "drill": [
            ("【ビジネス】ここまでの説明でご不明な点はございますでしょうか？（Apakah ada hal yang kurang jelas sejauh ini?）", "Sampai di titik ini, apakah pemaparan kami cukup jelas dan dapat dipahami?", "サンパイ ディ ティティッ イニ、アパカ プマパラン カミ チュクップ ジュラス ダン ダパット ディパハムイ", "公式プレゼンの理解確認。"),
            ("【日常会話】私の言いたいこと、伝わってる？（Nangkep gak maksud gue?）", "Nangkep kan ya arah pembicaraan gue barusan?", "ナンカップ カン ヤ アラ プンビチャラアン グエ バルサン", "友人同士の共感確認。"),
            ("【指示出し】具体的な作業イメージは湧きましたか？（Kira-kira sudah kebayang belum langkah kerjanya?）", "Sudah terbayang jelas kan ya apa yang harus dieksekusi pertama kali?", "スダ トゥルバヤン ジュラス カン ヤ アパ ヤン ハルス ディエクセクスィ プルタマ カリ", "タスクイメージの確認。"),
            ("【研修】質問があればいつでも遠慮なく遮ってください。（Jangan ragu untuk memotong jika ada pertanyaan.）", "Kalo ada bagian yang bikin bingung, langsung interupsi aja ya, jangan sungkan!", "カロ アダ バギアン ヤン ビキン ビングン、ランスン インテルプスィ アジャ ヤ、ジャンガン スンカン", "質問歓迎のスタンス。"),
            ("【会議】このペースで進めても大丈夫ですか？（Apakah tempo pemaparan ini sudah sesuai?）", "Gimana kecepatannya, gak terlalu ngebut kan ya penjelasannya?", "ギマナ クチパタンニャ、ガッ トゥルラル ンゲブット カン ヤ プンジュラサンニャ", "進行ペースの確認。"),
            ("【商談】ご提案内容にご納得いただけましたでしょうか。（Apakah Saudara merasa cocok dengan penawaran ini?）", "Kira-kira penawaran skema ini sudah sesuai dengan ekspektasi pihak Bapak?", "キラ キラ プナワラン スケマ イニ スダ ススアイ ドゥンガン エクスペクタスィ ピハッ バパッ", "納得度の確認。"),
            ("【電話】私の声はきちんとクリアに届いていますか？（Apakah suara saya terdengar jelas di sana?）", "Suara saya cukup terdengar jernih kan ya di seberang sana?", "スアラ サヤ チュクップ トゥルドゥンガル ジュルニ カン ヤ ディ スブラン サナ", "通話音声の届き具合確認。"),
            ("【教育】次のトピックに進んでもよろしいでしょうか？（Boleh kita lanjut ke materi selanjutnya?）", "Kalo poin ini udah clear, kita bisa lanjut ke modul berikutnya ya?", "カロ ポイン イニ ウダ クリア、キタ ビサ ランジュット ク モドゥル ブルイクットニャ ヤ", "段階移行の確認。"),
            ("【トラブル対応】こちらの謝罪と対応策を受け入れていただけますか？（Apakah solusi ini dapat diterima?）", "Apakah langkah mitigasi ini sudah menjawab kekhawatiran yang ada?", "アパカ ランカ ミティガスィ イニ スダ メンジャワブ クカワティラン ヤン アダ", "合意形成の確認。"),
            ("【同僚】ちょっと説明がごちゃごちゃしちゃったけど大丈夫？（Agak berantakan ya ngomongnya, ngerti kan?）", "Sori kalo rada muter-muter, tapi lu dapet kan intinya?", "ソリ カロ ラダ ムテル ムテル、タピ ル ダペット カン インティニャ", "自己反省を交えた確認。"),
            ("【病院】この薬の用法・用量はご理解いただけましたか？（Sudah paham aturan pakai obat ini?）", "Aturan dosisnya sudah cukup dimengerti ya Bapak/Ibu?", "アトゥラン ドスィスニャ スダ チュクップ ディムンゲルティ ヤ バパッ/イブ", "服薬指導の確認。"),
            ("【観光案内】集合場所の位置関係は把握できましたか？（Sudah tahu persis letak titik kumpulnya?）", "Patokan gedungnya sudah jelas kan ya, biar nanti gak nyasar?", "パトカン グドゥンニャ スダ ジュラス カン ヤ、ビアル ナンティ ガッ ニャサール", "迷子防止の確認。"),
            ("【技術説明】専門用語が多くて分かりにくかったですか？（Apakah terlalu banyak istilah teknis?）", "Bahasa teknisnya terlalu rumit gak? Perlu saya analogikan lebih simpel?", "バハサ テクニスニャ トゥルラル ルミット ガッ？ プル サヤ アナロギカン ルビ スィンペル", "平易化の打診。"),
            ("【雑談】共感してくれる？（Relate gak sama pengalaman gue tadi?）", "Pernah ngalamin hal yang sama gak lu? relate bgt kan?", "プルナ ンガラミン ハル ヤン サマ ガッ ル？ レレート バンゲット カン", "共感体験の引き出し。"),
            ("【総括】対話とはピンポン玉のラリーである。（Komunikasi sejati adalah permainan lempar tangkap bola.）", "Jangan terus bicara satu arah; cek pemahaman lawan bicara secara berkala!", "ジャンガン トゥルス ビチャラ サトゥ アラ；チェック プマハマン ラワン ビチャラ スチャラ ブルカラ", "双方向性の原則。")
        ],
        "quiz": [
            ("相手に「ここまで分かりましたか？説明はクリアですか？」と尋ねる最も代表的な表現は？", ["Sampai di sini apakah cukup jelas?", "Berapa umur Anda?", "Mau makan apa?", "Kapan Anda pergi?"], 1),
            ("若者や同僚の間で「言いたいこと分かった？頭に入った？」と親密に確認する俗語は？", ["Nangkep kan maksud gue?", "Tidur kan lu?", "Jatuh kan lu?", "Kenyang kan lu?"], 1),
            ("プレゼンや説明の途中で定期的に理解確認（Comprehension Check）を入れる最大の利点は？", ["相手の置き去りを防ぎ、疑問点をその場で解消できること", "話す時間を引き延ばせること", "自分の知識を誇示できること", "相手を試して優位に立つこと"], 1)
        ]
    },
    {
        "slug": "04-speed-control-pause",
        "title": "【戦略会話】スピード減速要請：ネイティブのマシンガントークを自然にスローダウンさせる",
        "intro": "インドネシア人の日常会話はリズムが速く、音節が融合して流れるように話されるため、初・中級者は圧倒されがちです。気後れせずに相手の会話スピードをコントロールし、「少しゆっくり話してください」とスマートに伝える減速ストラテジーを学びます。",
        "pairs": [
            ("Mohon berbicara sedikit lebih perlahan.", "Bisa pelan-pelan dikit gak ngomongnya?", "減速要請のレジスター差"),
            ("Saya masih dalam tahap belajar.", "Maklum ya, masih tahap belajar nih.", "学習者ステータスの提示"),
            ("Tempo bicaranya agak terlalu cepat.", "Ngebut bgt bro ngomongnya, kalem dikit!", "速度指摘のレジスター差"),
            ("Tolong beri jeda sejenak.", "Bentar-bentar, jeda dikit napa!", "一時停止の要請")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、もう少しゆっくりお話しいただけますでしょうか。（Mohon maaf, bolehkah berbicara sedikit lebih perlahan?）", "Mohon maaf Bapak, apakah berkenan berbicara dengan tempo sedikit lebih perlahan?", "モホン マアフ バパッ、アパカ ブルクナン ブルビチャラ ドゥンガン テンポ スディキット ルビ プルラハン", "公式な減速要請。"),
            ("【日常会話】ちょっと早すぎるよ！もっとゆっくり話して。（Kecepetan bro, pelan-pelan dong!）", "Wah ngebut bgt ngomongnya kayak kereta cepat, santai dikit napa!", "ワ ンゲブット バンゲット ンオモンニャ カヤッ クレタ チパット、サンタイ ディキット ナパ", "ユーモアを交えた減速要請。"),
            ("【学習者提示】まだインドネシア語を勉強中なので、手加減してください。（Saya masih belajar, tolong maklum ya.）", "Maklum ya kak, saya masih pemula belajar bahasa Indonesia, jangan ngebut-ngebut.", "マクルム ヤ カッ、サヤ マスィ プムラ ブラジャール バハサ インドネシア、ジャンガン ンゲブット ンゲブット", "相手の配慮を引き出す。"),
            ("【電話】電話口だと聞き取りにくいので、ゆっくりお願いします。（Lewat telepon agak susah, pelan-pelan ya.）", "Melalui sambungan telepon suaranya agak berdengung, mohon berbicara lebih lambat.", "ムラルイ サンブンガン テレポン スアラニャ アガッ ブルドゥングン、モホン ブルビチャラ ルビ ランバット", "電話での速度調整。"),
            ("【数字・金額】数字の桁が多いので、一桁ずつゆっくり言ってもらえますか？（Boleh sebutkan angkanya perlahan satu per satu?）", "Bisa tolong sebutkan nominal uangnya satu per satu dengan pelan?", "ビサ トロン スブットカン ノミナル ウアンニャ サトゥ プル サトゥ ドゥンガン プラン", "数字の聞き取り。"),
            ("【住所案内】メモを取るので、少し間を置きながら教えてください。（Mau saya catat, tolong pelan-pelan ya.）", "Saya sambil mencatat alamatnya, tolong kasih jeda sedikit ya mas.", "サヤ サンビル ムンチャタット アラマットニャ、トロン カスィ ジェダ スディキット ヤ マス", "メモ取りのための減速。"),
            ("【道案内】右折か左折か、もう一度ゆっくり教えて！（Belok mana tadi, pelan-pelan dong!）", "Bentar pak, tadi instruksinya apa? Belok kiri terus apa lagi?", "ブンタル パッ、タディ インストルクスィニャ アパ？ ベロッ キリ トゥルス アパ ラギ", "道順の再整理。"),
            ("【会議】議論のスピードに追いつけません。（Saya agak kewalahan mengikuti ritme diskusi.）", "Mohon izin, dinamika diskusinya sangat cepat, boleh kami mencerna poin ini dulu?", "モホン イジン、ディナミカ ディスクスィニャ サンガット チパット、ボレ カミ ムンチェルナ ポイン イニ ドゥル", "会議での発言権行使。"),
            ("【店頭】早口でメニューを言われても分かりません。（Jangan cepat-cepat sebut menunya.）", "Mbak, jangan buru-buru, saya baca menunya pelan-pelan dulu ya.", "ムバッ、ジャンガン ブルブル、サヤ バチャ メニューニャ プラン プラン ドゥル ヤ", "焦らされ防止。"),
            ("【チャット口頭通話】一呼吸置いて話しましょう。（Tarik napas dulu bro, santai.）", "Tarik napas dulu napa bro, jangan kayak dikejar setan gitu ngomongnya!", "タリッ ナパス ドゥル ナパ ブロ、ジャンガン カヤッ ディクジャール セタン ギトゥ ンオモンニャ", "落ち着きを促す。"),
            ("【タクシー】運転手さん、ちょっと待って、今どこですか？（Pak sopir, sebentar, ini kita di mana?）", "Pelan-pelan pak nyetirnya sambil kasih tahu ini udah nyampe daerah mana.", "プラン プラン パッ ニェティルニャ サンビル カスィ タウ イニ ウダ ニャンペ ダエラ マナ", "運転ペースの調整。"),
            ("【講義】先生、板書が追いつかないので少しお待ちください。（Tunggu sebentar Pak, belum selesai mencatat.）", "Mohon waktu sejenak Pak dosen, kami belum selesai merangkum rumus tersebut.", "モホン ワクトゥ スジュナッ パッ ドセン、カミ ブルム スルサイ ムランクム ルムス トゥルスブット", "板書待ち要請。"),
            ("【スラング頻出】普通の言葉でゆっくり話してくれる？（Bisa pakai kata biasa dan pelan-pelan?）", "Jangan banyak istilah gaul dong, pake kata biasa aja dan pelan-pelan.", "ジャンガン バニャッ イスティラ ガウル ドン、パケ カタ ビアサ アジャ ダン プラン プラン", "スラング抑制。"),
            ("【ビジネス確認】契約条件なので、一文ずつ精査させてください。（Mari kita bedah satu per satu secara teliti.）", "Mengingat ini dokumen legal, mari kita baca klausulnya perlahan kata demi kata.", "ムニンガット イニ ドクメン レガル、マリ キタ バチャ クラウスルニャ プルラハン カタ ドゥミ カタ", "厳密確認。"),
            ("【総括】会話の主導権を握る者が、最も適切な速度を支配する。（Penguasa dialog adalah yang mampu mengatur tempo percakapan.）", "Mengatur ritme bicara bukan tanda kelemahan, tapi strategi diplomasi tingkat tinggi!", "ムンアトゥル リトメ ビチャラ ブカン サンダ クルマハン、タピ ストラテギ ディプロマスィ ティンカット ティンギ", "スピードコントロールの極意。")
        ],
        "quiz": [
            ("相手に「もう少しゆっくり話してください」と上品かつ丁寧にお願いするフレーズは？", ["Bolehkah berbicara sedikit lebih perlahan?", "Jangan banyak bicara lu!", "Tutup mulutmu sekarang!", "Pergi dari sini cepat!"], 1),
            ("自分が学習者であることを伝えて「大目に見てね・手加減してね」と前置きする定番語は？", ["Maklum ya...", "Hebat ya...", "Bodo amat ya...", "Marah ya..."], 1),
            ("相手がマシンガントークで早口すぎる時、「落ち着いて、焦らないで」と促す口語表現は？", ["Santai aja, tarik napas dulu...", "Lari lebih kencang...", "Makan yang banyak...", "Beli mobil baru..."], 1)
        ]
    },
    {
        "slug": "05-volume-repetition-ask",
        "title": "【戦略会話】音量・反復要請：「もう少し大きな声でもう一度」を角を立てずにお願いする",
        "intro": "カフェや街頭、工場などの騒音下では、声が小さかったり篭っていたりして聞き取れない事態が頻発します。「もう少し大きな声で話してもらえますか？」「最後の一言だけもう一度！」と、相手の機嫌を損ねずに音量アップや部分反復を促す技術を訓練します。",
        "pairs": [
            ("Mohon berbicara lebih lantang.", "Kencengan dikit suaranya bro!", "音量要請のレジスター差"),
            ("Suara di sini agak bising.", "Rame bgt di sini, gak kedengeran.", "周囲の騒音理由付け"),
            ("Boleh ulang satu kalimat terakhir?", "Kalimat terakhir tadi apa?", "部分反復要請の差"),
            ("Mohon dekatkan mikrofonnya.", "Deketin mik-nya dong!", "マイク・通話機器への要請")
        ],
        "drill": [
            ("【ビジネス】恐れ入ります、周囲が騒がしいため少し大きなお声でお願いできますでしょうか。（Mohon berbicara sedikit lebih keras karena suasana agak bising.）", "Mohon maaf Bapak, dikarenakan ruangan agak bising, apakah berkenan berbicara lebih lantang?", "モホン マアフ バパッ、ディカレナカン ルアンガン アガッ ビスィン、アパカ ブルクナン ブルビチャラ ルビ ランタン", "公式な音量アップ要請。"),
            ("【日常会話】声が小さくて聞こえないよ、もっと大きな声で！（Kencengan dikit suaranya bro, gak kedengeran!）", "Suara lu kecil amat kayak semut, kencengan dikit napa bro!", "スアラ ル クチル アマット カヤッ スムット、クンチュンガン ディキット ナパ ブロ", "友人同士の音量ツッコミ。"),
            ("【オンライン会議】マイクを少し口元に近づけていただけますか？（Boleh dekatkan mikrofonnya ke mulut?）", "Mohon maaf suaranya agak tenggelam, boleh tolong dekatkan mikrofonnya?", "モホン マアフ スアラニャ アガッ トゥンゲラム、ボレ トロン ドゥカッカン マイクロフォンニャ", "マイク位置の調整。"),
            ("【電話】受話器の音量を最大にしても聞き取りにくいです。（Sudah volume maksimal tapi masih kecil suaranya.）", "Volume gawai saya sudah maksimal, tapi suara Bapak masih sayup-sayup terdengar.", "ヴォリューム ガワイ サヤ スダ マクスィマル、タピ スアラ バパッ マスィ サユップ サユップ トゥルドゥンガル", "機器音量の限界申告。"),
            ("【レストラン】音楽の音が大きいので、もう一度メニューをお願いします。（Suara musiknya keras, boleh ulang menunya?）", "Mas, backsound musiknya kenceng bgt nih, boleh sebutin sekali lagi menunya?", "マス、バックサウンド ムスィックニャ クンチェン バンゲット ニ、ボレ スブッティン スカリ ラギ メニューニャ", "BGM騒音への対処。"),
            ("【部分反復】最後の金額の部分だけもう一度おっしゃってください。（Bagian nominal terakhirnya saja yang diulang ya.）", "Hanya bagian nominal biayanya saja yang perlu diulang, selebihnya sudah jelas.", "ハニャ バギアン ノミナル ビアヤニャ サジャ ヤン プル ディウラン、スレビフニャ スダ ジュラス", "部分特定リピート。"),
            ("【工場現場】機械の音がうるさいので、耳元で話してください。（Suara mesin berisik, boleh bicara di dekat telinga?）", "Bising sekali suara mesin di sini pak, tolong agak mendekat saat berbicara ya.", "ビスィン スカリ スアラ ムスィン ディ スィニ パッ、トロン アガッ ムンドゥカット サアット ブルビチャラ ヤ", "工場現場での会話。"),
            ("【窓口】アクリル板越しで声が篭って聞こえます。（Suaranya terhalang sekat akrilik.）", "Tertutup kaca pembatas nih mbak, boleh agak dikeraskan suaranya?", "トゥルトゥップ カチャ プンバタス ニ ムバッ、ボレ アガッ ディクラスカン スアラニャ", "遮蔽板越しの要請。"),
            ("【雑談】秘密の話だからって小声すぎ！（Pelan amat bisik-bisiknya, gak dapet gue!）", "Gak usah bisik-bisik amat kali, gak ada orang lain kok di sini!", "ガッ ウサ ビスィッ ビスィッ アマット カリ、ガッ アダ オラン ライン コッ ディ スィニ", "過度の小声へのツッコミ。"),
            ("【講義】マイクのスイッチが入っていないようです。（Sepertinya mikrofonnya belum menyala.）", "Mohon maaf Pak dosen, tampaknya sakelar mikrofon belum dinyalakan.", "モホン マアフ パッ ドセン、タンパッニャ サクラル マイクロフォン ブルム ディニャラカン", "マイク電源指摘。"),
            ("【タクシー】車の走行音で道案内が聞こえませんでした。（Suara ban mobil berisik, boleh ulang arah jalannya?）", "Tadi belok kanannya di depan ruko warna apa ya pak? Suara jalanannya ramai.", "タディ ベロッ カナンニャ ディ ドゥパン ルコ ワルナ アパ ヤ パッ？ スアラ ジャラナンニャ ラマイ", "ロードノイズへの対処。"),
            ("【復唱依頼】念には念を入れて、もう一度同じ言葉を復唱願えますか？（Boleh lafalkan sekali lagi persis seperti tadi?）", "Boleh minta tolong dieja atau dilafalkan persis seperti tadi sekali lagi?", "ボレ ミンタ トロン ディエジャ アタウ ディラファルカン プルスィス スプルティ タディ スカリ ラギ", "完全復唱要請。"),
            ("【オンライン】エコーがかかってハウリングしています。（Suaranya bergema dan terjadi feedback.）", "Ada suara gema feedback nih, mohon peserta lain mute mikrofonnya sejenak.", "アダ スアラ グマ フィードバック ニ、モホン プスルタ ライン ミュート マイクロフォンニャ スジュナッ", "ハウリング対処。"),
            ("【同僚】後ろの席で電話してる人がうるさくて聞こえない。（Orang di belakang berisik bgt nelponnya.）", "Sebelah gue lagi heboh nelpon nih bro, bisa ngomong lebih tegas dan jelas?", "スブラ グエ ラギ ヘボー ネルポン ニ ブロ、ビサ ンオモン ルビ トゥガス ダン ジュラス", "同僚への音量要請。"),
            ("【総括】環境のせいにして頼むのが最も角の立たない大人の知恵である。（Menjadikan situasi lingkungan sebagai alasan adalah etika diplomasi.）", "Katakan 'ruangannya bising', bukan 'suara Anda jelek'!", "カタカン 'ルアンガンニャ ビスィン'、ブカン 'スアラ アンダ ジュレック'", "角を立てない配慮。")
        ],
        "quiz": [
            ("相手に「もう少し声を張って、大きな声で話してください」と丁寧に頼む語彙は？", ["berbicara lebih lantang / keras", "berbisik perlahan", "menangis tersedu", "diam seribu bahasa"], 1),
            ("相手の声の小ささを責めるのではなく、角を立てずに聞き直すベストな理由は？", ["周囲の環境が騒がしいせいにする（ruangan agak bising）", "相手の滑舌が悪いせいにする", "相手が嫌いだからだと言う", "自分の耳が遠いせいにして怒る"], 1),
            ("オンライン通話で声が篭っている時に「マイクを口元に近づけて」と頼むフレーズは？", ["Tolong dekatkan mikrofonnya ke mulut ya", "Tolong lempar mikrofonnya", "Tolong matikan laptopnya", "Tolong beli komputer baru"], 1)
        ]
    },
    {
        "slug": "06-circumlocution-objects",
        "title": "【戦略会話】迂回表現（モノ編）：単語をど忘れした時に「ほら、あの〜するための道具」と伝える",
        "intro": "外国語で話す際、すべての名詞を知っている必要はありません。単語がパッと出てこない時に、「alat untuk...（〜するための道具）」「bentuknya kayak...（形は〜みたいで）」「fungsinya buat...（機能は〜用で）」と外見や用途から説明して相手に単語を当てさせる「迂回表現（Circumlocution）」の極意を学びます。",
        "pairs": [
            ("Alat yang digunakan untuk... (〜するための道具)", "Barang yang fungsinya buat...", "用途説明のフレーム"),
            ("Bentuknya menyerupai... (形は〜に似ている)", "Bentuknya mirip kayak...", "形状説明のフレーム"),
            ("Terbuat dari bahan... (〜の素材で作られている)", "Bahannya dari semacem...", "素材説明のフレーム"),
            ("Benda yang biasa ada di... (普段〜にあるもの)", "Barang yang suka nongol di...", "場所・文脈説明のフレーム")
        ],
        "drill": [
            ("【ホッチキス】ほら、紙を針でパチンと留める道具だよ。（Alat untuk menyatukan kertas pakai kawat kecil.）", "Itu lho, alat yang dipencet buat nyatuin lembaran kertas pake kawat!", "イトゥ ロ、アラット ヤン ディペンチェット ブアット ニャトゥイン ルンバラン クルタス パケ カワット", "stapler (staples) の迂回説明。"),
            ("【爪切り】爪をパチパチ切るための小さな刃物。（Alat kecil untuk memotong kuku jari.）", "Barang kecil dari besi yang biasa dipake buat motong kuku, apa tuh namanya?", "バラン クチル ダリ ブスィ ヤン ビアサ ディパケ ブアット モトン クク、アパ トゥ ナマニャ", "pemotong kuku / gunting kuku の迂回。"),
            ("【栓抜き】ビンの王冠のフタを開ける金具。（Benda logam untuk membuka tutup botol kaca.）", "Alat dari besi buat ngebuka tutup botol kaca minuman yang keras itu lho.", "アラット ダリ ブスィ ブアット ンゲブカ トゥトゥップ ボトル カチャ ミヌマン ヤン クラス イトゥ ロ", "pembuka botol の迂回。"),
            ("【アイロン】熱で服のシワをピンと伸ばす家電。（Alat elektronik panas untuk merapikan pakaian kusut.）", "Barang elektronik yang panas buat ngilangin kusut di baju biar rapi.", "バラン エレクトロニック ヤン パナス ブアット ンギランイン クスット ディ バジュ ビアル ラピ", "setrika の迂回。"),
            ("【じょうろ】花や植物にシャワーみたいに水をあげる容器。（Wadah penyiram tanaman dengan corong semprot.）", "Wadah plastik bertangkai yang ada lubang-lubang kecilnya buat nyiram bunga.", "ワダ プラスティック ブルタンカイ ヤン アダ ルバン ルバン クチルニャ ブアット ニラム ブンガ", "gembor / penyiram tanaman の迂回。"),
            ("【延長コード】コンセントの穴を遠くまで伸ばす長いケーブル。（Kabel panjang dengan beberapa lubang colokan listrik.）", "Kabel panjang yang ada banyak lubang stopkontaknya buat colokan charger.", "カベル パンジャン ヤン アダ バニャッ ルバン ストップコンタクニャ ブアット チョロカン チャージャー", "kabel colokan / kabel rol の迂回。"),
            ("【体温計】熱があるかどうか脇に挟んで測る器具。（Alat untuk mengukur suhu tubuh saat demam.）", "Alat kecil yang dijepit di ketiak buat ngecek suhu badan pas lagi sakit.", "アラット クチル ヤン ディジュピット ディ クティアッ ブアット ンゲチェック スフ バダン パス ラギ サキット", "termometer の迂回。"),
            ("【耳かき】耳の中のゴミを掃除する小さな棒。（Benda tipis panjang untuk membersihkan kotoran telinga.）", "Alat dari bambu atau besi yang ujungnya kayak sendok kecil buat bersihin kuping.", "アラット ダリ バンブ アタウ ブスィ ヤン ウジュンニャ カヤッ スンドッ クチル ブアット ブルスィヒン クピン", "korek kuping の迂回。"),
            ("【ハンガー】服を掛けてクローゼットに吊るす三角の道具。（Alat segitiga untuk menggantung baju di lemari.）", "Benda bentuk segitiga dari kawat atau plastik buat gantung baju.", "ブンダ ブントゥッ スギティガ ダリ カワット アタウ プラスティック ブアット ガントゥン バジュ", "gantungan baju (hanger) の迂回。"),
            ("【虫除けスプレー】蚊に刺されないように肌に吹きかける液体。（Cairan semprot untuk mencegah gigitan nyamuk.）", "Lotion atau semprotan yang baunya khas biar gak digigit nyamuk pas tidur.", "ロスィオン アタウ スンプロタン ヤン バウニャ カス ビアル ガッ ディギギット ニャムッ パス ティドゥール", "obat nyamuk / autan の迂回。"),
            ("【消しゴム】鉛筆で書いた文字をこすって消すゴム。（Karet untuk menghapus coretan pensil di kertas.）", "Benda kenyal kecil buat ngehapus tulisan pensil yang salah di buku.", "ブンダ クニャル クチル ブアット ンゲハプス トゥリスアン ペンスィル ヤン サラ ディ ブク", "penghapus の迂回。"),
            ("【絆創膏】小さな切り傷にペタッと貼る医療用テープ。（Plester kecil berperekat untuk menutup luka ringan.）", "Plester obat kecil yang ditempel di jari kalo pas kena iris pisau.", "プレステル オバット クチル ヤン ディトゥンペル ディ ジャリ カロ パス クナ イリス ピサウ", "plester luka (Hansaplast) の迂回。"),
            ("【爪楊枝】歯の隙間に挟まった食べカスを取る細い木。（Kayu runcing kecil untuk membersihkan sisa makanan di gigi.）", "Tusuk kayu kecil yang biasa ada di meja makan buat bersihin sela-sela gigi.", "トゥスッ カユ クチル ヤン ビアサ アダ ディ メジャ マカン ブアット ブルスィヒン スラ スラ ギギ", "tusuk gigi の迂回。"),
            ("【雨ガッパ】バイクに乗る時に着るビニールの合羽。（Jas dari bahan tahan air saat mengendarai motor di kala hujan.）", "Baju plastik panjang tahan air yang suka dipake pengendara motor pas ujan gede.", "バジュ プラスティック パンジャン タハン アイル ヤン スカ ディパケ プンゲンダラ モトール パス ウジャン グデ", "jas hujan の迂回。"),
            ("【総括】名詞を知らなくても、機能と外見を言えれば世界中どこでも通じる。（Menjelaskan fungsi adalah esensi komunikasi manusiawi.）", "Lupa nama bendanya? Jelaskan fungsinya, bentuknya, bahannya: lawan bicara pasti paham!", "ルパ ナマ ブンダニャ？ ジュラスカン フングスィニャ、ブントゥッニャ、バハンニャ：ラワン ビチャラ パスティ パハム", "モノ迂回の原則。")
        ],
        "quiz": [
            ("名前が出てこない道具を説明する時の万能フレーズ「〜するための道具」のインドネシア語は？", ["alat untuk / barang yang fungsinya buat...", "makanan yang rasanya enak...", "orang yang bekerja di...", "tempat yang letaknya di..."], 1),
            ("形が似ていることを伝える時の定番表現「bentuknya menyerupai / mirip kayak...」の日本語の意味は？", ["形は〜に似ている", "価格は〜より安い", "色は〜より明るい", "重さは〜より重い"], 1),
            ("爪切り（gunting kuku）を迂回表現で説明する場合、最も的確な特徴描写は？", ["alat kecil dari besi buat motong kuku jari", "kendaraan roda dua buat jalan jauh", "makanan manis dari cokelat", "kertas tipis untuk menggambar"], 1)
        ]
    },
    {
        "slug": "07-circumlocution-actions",
        "title": "【戦略会話】迂回表現（動作編）：動詞が出てこない時に平易な語彙を組み合わせて説明する",
        "intro": "「うがいをする」「見せびらかす」「盗み聞きする」「つまずく」など、特定の高度な動詞がパッと出ない時でも、基本動詞（bikin, buat, ambil, jalan, lihat）と状況描写を組み合わせれば100%意図を伝えることができます。動詞のド忘れをスマートに切り抜ける迂回術を体得します。",
        "pairs": [
            ("Melakukan gerakan... (〜という動きをする)", "Bikin gerakan kayak gini...", "動作模倣のフレーム"),
            ("Proses dari kondisi A menjadi B (AからBへの変化)", "Dari yang tadinya... terus jadi...", "状態変化のフレーム"),
            ("Sama artinya dengan... (〜と同じ意味の動作)", "Mirip kayak kata... tapi lebih...", "類義動詞の微調整"),
            ("Apa istilah untuk tindakan... (〜する行為は何て言う？)", "Kalo orang lagi... itu istilahnya apa ya?", "語彙逆引き質問")
        ],
        "drill": [
            ("【うがいをする】水で喉をガラガラ洗う動作。（Kumur-kumur di tenggorokan pakai air.）", "Itu lho, bersihin tenggorokan pake air sambil ngeluarin suara 'glogok-glogok'!", "イトゥ ロ、ブルスィヒン トゥンゴロカン パケ アイル サンビル ンゲルアルカン スアラ グロゴッ グロゴッ", "kumur / berkumur の迂回説明。"),
            ("【つまずく】歩いていて石に足が引っかかって転びそうになる。（Kaki tersandung batu saat berjalan.）", "Lagi jalan terus kakinya gak sengaja nabrak batu dan hampir jatuh tersungkur.", "ラギ ジャラン トゥルス カキニャ ガッ スンガジャ ナブラッ バトゥ ダン ハンピール ジャトゥ トゥルスンクール", "tersandung の迂回。"),
            ("【見せびらかす】自慢したくて高価なものをわざと人に見せる。（Pamer barang mahal biar dipuji.）", "Sengaja nunjuk-nunjukin barang mewah ke orang biar dibilang kaya dan keren.", "スンガジャ ヌンジュッ ヌンジュッキン バラン ムワ ク オラン ビアル ディビラン カヤ ダン クレン", "pamer / flexing の迂回。"),
            ("【盗み聞きする】他人の会話をこっそり隠れて聞く。（Mendengarkan obrolan orang secara sembunyi-sembunyi.）", "Diem-diem masang kuping dengerin omongan orang lain tanpa izin.", "ディエム ディエム マサン クピン ドゥンゲルイン オモンガン オラン ライン タンパ イジン", "menguping の迂回。"),
            ("【あくびをする】眠い時に口を大きく開けて息を吸い込む。（Membuka mulut lebar-lebar saat mengantuk.）", "Membuka mulut gede-gede sambil narik napas dalem gara-gara ngantuk berat.", "ムンブカ ムルット グデ グデ サンビル ナリッ ナパス ダラム ガラガラ ンアントゥッ ブラット", "menguap の迂回。"),
            ("【しゃっくりが出る】横隔膜がピクピクして変な音が出る。（Tersentak-sentak mengeluarkan bunyi dari dada.）", "Kondisi di mana dada tersentak-sentak ngeluarin bunyi cegukan tanpa bisa ditahan.", "コンディスィ ディ マナ ダダ トゥルスンタッ スンタッ ンゲルアルイン ブニ チュグカン タンパ ビサ ディタハン", "cegukan の迂回。"),
            ("【くすぐる】相手を笑わせるために脇腹や足の裏をコチョコチョする。（Menyentuh bagian sensitif agar tertawa geli.）", "Menyentuh pinggang atau telapak kaki orang pake jari biar dia ketawa kegelian.", "ムニュントゥ ピンガン アタウ トゥラパッ カキ オラン パケ ジャリ ビアル ディア クタワ クグリアン", "menggelitik の迂回。"),
            ("【値切る】提示された価格を安くしてくれと交渉する。（Minta potongan harga saat berbelanja.）", "Minta ke penjual biar harganya diturunin lebih murah dari harga pasaran.", "ミンタ ク プンジュアル ビアル ハルガニャ ディトゥルニン ルビ ムラ ダリ ハルガ パサラン", "menawar の迂回。"),
            ("【割り込む】並んでいる列の前に横入りする。（Menyelak antrean orang yang sudah rapi.）", "Tiba-tiba masuk ke barisan orang tanpa mau antre dari belakang.", "ティバ ティバ マスッ ク バリスアン オラン タンパ マウ アントレ ダリ ブラカン", "menyerobot / menyela の迂回。"),
            ("【居眠り運転をする】車を運転中にウトウト寝てしまう。（Tertidur sesaat saat mengemudikan kendaraan.）", "Mata merem beberapa detik pas lagi nyetir mobil karena capek banget.", "マタ ムレム ブルブラパ ドゥティッ パス ラギ ニェティル モビル カレナ チャペ バンゲット", "microsleep / tertidur saat nyetir の迂回。"),
            ("【ため息をつく】疲れたり悩んだりして深く息を吐き出す。（Menghembuskan napas berat tanda lelah atau kecewa.）", "Buang napas kenceng-kenceng lewat mulut pas lagi pusing mikirin masalah.", "ブアン ナパス クンチェン クンチェン レワット ムルット パス ラギ プスィン ミキリン マサラ", "menghela napas の迂回。"),
            ("【腕組みをする】両腕を胸の前で交差させるポーズ。（Menyilangkan kedua tangan di depan dada.）", "Posisi melipat kedua tangan di depan dada pas lagi mikir atau ngeliatin orang.", "ポスィスィ ムリパット クドゥア タンガン ディ ドゥパン ダダ パス ラギ ミキール アタウ ンゲリアティン オラン", "bersedekap の迂回。"),
            ("【つまみ食いをする】料理ができる前に手でこっそり少し食べる。（Mencicipi makanan secara sembunyi sebelum matang.）", "Nyomot makanan sedikit pake jari sebelum hidangan resmi disajikan di meja.", "ニョモット マカナン スディキット パケ ジャリ スブルム ヒダンガン レスミ ディサジカン ディ メジャ", "mencuri makan / nyomot の迂回。"),
            ("【二度寝する】一度起きたのにまたベッドに入って眠る。（Tidur kembali setelah sempat terbangun.）", "Udah bangun subuh terus malah merem dan tidur nyenyak lagi sampe siang.", "ウダ バングン スブ トゥルス マラ ムレム ダン ティドゥール ニエニャッ ラギ サンペ スィアン", "tidur lagi の迂回。"),
            ("【総括】動詞の直訳を諦めた瞬間、自由な表現力が覚醒する。（Fleksibilitas verbal adalah tanda kematangan linguistik.）", "Jangan mentok di satu kata; urai tindakannya menjadi kalimat sederhana!", "ジャンガン ムントッ ディ サトゥ カタ；ウライ ティンダカンニャ ムンジャディ カリマット スデルハナ", "動作迂回の極意。")
        ],
        "quiz": [
            ("喉を水でガラガラ洗う「うがいをする」の動詞が出ない時、最もわかりやすい迂回説明は？", ["bersihin tenggorokan pake air sambil bunyi 'glogok-glogok'", "lari kencang di lapangan", "membaca buku tebal di kamar", "membeli baju di toko"], 1),
            ("「列に横入りする・割り込む」を平易な言葉で説明する表現は？", ["tiba-tiba masuk barisan tanpa antre dari belakang", "memberi uang kepada pengemis", "berenang di sungai yang dalam", "menutup pintu secara perlahan"], 1),
            ("動詞をド忘れした時の対処法として、SLA理論で推奨される戦略は？", ["具体的な動作プロセスや前後の状態変化を分解して易しい言葉で描写する", "黙り込んで相手が察するのを待つ", "日本語の動詞をそのまま大声で叫ぶ", "会話を諦めてその場を立ち去る"], 1)
        ]
    },
    {
        "slug": "08-circumlocution-concepts",
        "title": "【戦略会話】迂回表現（概念編）：抽象名詞や専門用語を具体例とメタファーで切り抜ける",
        "intro": "「インフレ」「持続可能性」「既得権益」「自己肯定感」などの抽象概念や専門用語は、辞書的な難解語（inflasi, keberlanjutan, hak istimewa, kepercayaan diri）を暗記していなくても、具体例や日常のたとえ話（メタファー）を用いて説明することで相手に確実に伝えることができます。",
        "pairs": [
            ("Situasi di mana hal ini terjadi... (これが起きる状況)", "Kondisi pas orang ngerasa...", "状況描写のフレーム"),
            ("Bisa diibaratkan seperti... (〜のように例えられる)", "Bisa diumpamain kayak...", "メタファー・比喩のフレーム"),
            ("Dampaknya membuat... (その結果〜になる)", "Efeknya bikin keadaan jadi...", "結果・影響説明のフレーム"),
            ("Konsep yang berhubungan dengan... (〜に関する概念)", "Konsep yang nyangkut soal...", "関連領域のフレーム")
        ],
        "drill": [
            ("【インフレ】物価がどんどん上がってお金の価値が下がる現象。（Kondisi saat harga barang naik dan nilai uang turun.）", "Fenomena di mana harga-harga barang kebutuhan naik terus, jadi uang sejuta sekarang cuma dapet dikit.", "フェノメナ ディ マナ ハルガ ハルガ バラン クブトゥハン ナイッ トゥルス、ジャディ ウアン スジュタ スカラン チュマ ダペット ディキット", "inflasi の概念迂回。"),
            ("【サステナビリティ（持続可能性）】将来の世代のために環境や資源を使い尽くさない配慮。（Menjaga alam agar generasi masa depan tetap bisa hidup layak.）", "Prinsip hidup di mana kita pake sumber daya bumi secukupnya aja, biar anak cucu kita tetep punya masa depan.", "プリンスィプ ヒドゥップ ディ マナ キタ パケ スンベル ダヤ ブミ スチュクップニャ アジャ、ビアル アナッ チュチュ キタ トゥタップ プニャ マサ ドゥパン", "keberlanjutan (sustainability) の迂回。"),
            ("【自己肯定感】自分には価値があり、ありのままで素晴らしいと思える感情。（Rasa percaya bahwa diri sendiri berharga apa adanya.）", "Perasaan dalam hati bahwa diri kita ini berharga, layak dicintai, dan gak gampang minder sama orang lain.", "プラサアン ダラム ハティ バフワ ディリ キタ イニ ブルハルガ、ラヤッ ディチンタイ、ダン ガッ ガンパン ミンデル サマ オラン ライン", "self-esteem / rasa percaya diri の迂回。"),
            ("【既得権益】昔から権力を持つ一部の人々が独占している都合の良い特権。（Keuntungan istimewa yang dipertahankan kelompok berkuasa.）", "Hak-hak enak yang udah dinikmati sama orang-orang lama berkuasa, dan mereka gak mau bagi ke orang baru.", "ハッ ハッ エナッ ヤン ウダ ディニクマティ サマ オラン オラン ラマ ブルクアサ、ダン ムレカ ガッ マウ バギ ク オラン バル", "vested interest の迂回。"),
            ("【過労死】激しすぎる労働のストレスと疲労によって突然命を落とすこと。（Kematian mendadak akibat beban kerja yang terlalu ekstrem.）", "Istilah buat orang yang meninggal tiba-tiba kena serangan jantung karena kerja lembur gila-gilaan tanpa istirahat.", "イスティラ ブアット オラン ヤン ムニンガル ティバ ティバ クナ サランガン ジャンツン カレナ クルジャ レンブール ギラギラアン タンパ イスティラハット", "karoshi / mati karena kelelahan kerja の迂回。"),
            ("【デジャブ（既視感）】初めて訪れた場所なのに、過去に見たことがあるように錯覚する感覚。（Perasaan aneh seolah pernah mengalami momen ini sebelumnya.）", "Sensasi unik pas kita ngerasa momen atau tempat ini udah pernah kita lewatin di masa lalu, padahal baru pertama kali.", "センサスィ ユニッ パス キタ ンゲラサ モメン アタウ トゥムパット イニ ウダ プルナ キタ レワティン ディ マサ ラル、パダハル バル プルタマ カリ", "deja vu の迂回。"),
            ("【共感力（エンパシー）】他人の痛みや感情を自分のことのように感じ取る能力。（Kemampuan merasakan apa yang dirasakan oleh orang lain.）", "Kemampuan hati kita buat bener-bener ngerasain kesedihan atau penderitaan orang lain, bukan cuma kasihan doang.", "クマンプアン ハティ キタ ブアット ブナル ブナル ンゲラサイン クスディハン アタウ プンデリタアン オラン ライン、ブカン チュマ カスィハン ドアン", "empati の迂回。"),
            ("【コンプライアンス（法令遵守）】企業がルールや法律、社会的倫理を厳格に守って活動すること。（Kepatuhan perusahaan terhadap seluruh aturan hukum yang berlaku.）", "Komitmen perusahaan buat taat sama aturan hukum dan etika, gak boleh nyogok atau ngelanggar SOP.", "コミットメン プルサハアン ブアット タアット サマ アトゥラン フクム ダン エティカ、ガッ ボレ ニョゴッ アタウ ンゲランガル エスオーピー", "kepatuhan hukum / compliance の迂回。"),
            ("【ワークライフバランス】仕事の責任とプライベートな生活の充実が調和している状態。（Keseimbangan antara tanggung jawab kerja dan kebahagiaan hidup.）", "Kondisi ideal di mana kerjaan kantor tuntas, tapi kita tetep punya waktu berkualitas buat keluarga, hobi, dan istirahat.", "コンディスィ イデアル ディ マナ クルジャアン カントール トゥンタス、タピ キタ トゥタップ プニャ ワクトゥ ブルクアリタス ブアット クルアルガ、ホビ、ダン イスティラハット", "work-life balance の迂回。"),
            ("【先入観（プレジェディス）】事実を確かめる前に、決めつけで他人を判断してしまう偏見。（Penilaian negatif yang tergesa-gesa tanpa mengetahui fakta sebenarnya.）", "Sikap yang udah ngecap buruk atau menilai seseorang secara sepihak sebelum bener-bener kenal orangnya.", "スィカップ ヤン ウダ ンゲチャップ ブルック アタウ ムニライ ススオラン スチャラ スピハッ スブルム ブナル ブナル クナル オランニャ", "prasangka / prasangka buruk の迂回。"),
            ("【シナジー（相乗効果）】2つの要素が組み合わさることで、1＋1が3以上になる効果。（Hasil gabungan yang jauh lebih besar daripada berjalan sendiri-sendiri.）", "Efek kolaborasi di mana pas dua pihak gabung, hasilnya berlipat ganda, bukan cuma satu tambah satu jadi dua.", "エフェッ コラボラスィ ディ マナ パス ドゥア ピハッ ガブン、ハシルニャ ブルリパット ガンダ、ブカン チュマ サトゥ タンバ サトゥ ジャディ ドゥア", "sinergi の迂回。"),
            ("【ボトルネック】全体の進行を遅らせている最大の詰まり・障害箇所。（Bagian proses yang paling menghambat laju keseluruhan sistem.）", "Titik paling macet di dalam proses kerja yang bikin seluruh bagian lainnya ikutan mandek nungguin.", "ティティッ パリン マチェット ディ ダラム プロセス クルジャ ヤン ビキン スルルー バギアン ラインニャ イクタン マンデッ ヌングイン", "faktor penghambat / bottleneck の迂回。"),
            ("【マインドセット】物事の捉え方や判断を決定づけている根本的な思考の枠組み。（Pola pikir mendasar yang membentuk cara pandang seseorang.）", "Kerangka pola pikir di dalam kepala kita yang nentuin gimana cara kita bereaksi terhadap setiap kegagalan atau peluang.", "クランカ ポラ ピキール ディ ダラム クパラ キタ ヤン ネントゥイン ギマナ チャラ キタ ブレアクスィ トゥルハダップ スティアップ クガガラン アタウ プルアン", "pola pikir / mindset の迂回。"),
            ("【アルゴリズム】コンピューターが問題を解決するために従う計算手順。（Urutan langkah sistematis untuk menyelesaikan masalah data.）", "Rumus langkah demi langkah yang dipake komputer buat nentuin video mana yang muncul di beranda media sosial kita.", "ルムス ランカ ドゥミ ランカ ヤン ディパケ コンピューター ブアット ネントゥイン ヴィデオ マナ ヤン ムンチュル ディ ブランダ メディア ソスィアル キタ", "algoritma の迂回。"),
            ("【総括】抽象概念を平易な言葉に翻訳できる人間こそが、最高の知性の持ち主である。（Menjelaskan hal rumit dengan sederhana adalah puncak kepintaran.）", "Bisa menjelaskan konsep berat dengan bahasa sehari-hari adalah bukti pemahaman yang paling mendalam!", "ビサ ムンジュラスカン コンセプ ブラット ドゥンガン バハサ スハリ ハリ アダラ ブクティ プマハマン ヤン パリン ムンダラム", "概念迂回の哲学。")
        ],
        "quiz": [
            ("物価が上がり通貨の価値が落ちる「インフレ」を具体例で説明する場合、最も分かりやすい表現は？", ["harga barang naik terus, jadi uang sejuta sekarang cuma dapat sedikit", "semua orang belajar bahasa asing di sekolah", "hujan turun sangat deras kemarin malam", "mobil berjalan cepat di jalan tol"], 1),
            ("抽象的な専門用語を説明する際、「〜のように例えられる」と比喩を導入する表現は？", ["Bisa diibaratkan / diumpamakan seperti...", "Sama sekali tidak ada hubungannya...", "Harganya sangat murah...", "Siapa nama penulis buku ini..."], 1),
            ("全体の進行を滞らせている「ボトルネック（障害箇所）」の的確な比喩的説明は？", ["titik paling macet yang bikin seluruh proses ikutan mandek", "kunci untuk membuka pintu rumah", "hadiah ulang tahun dari teman", "makanan penutup setelah makan malam"], 1)
        ]
    },
    {
        "slug": "09-time-buying-fillers",
        "title": "【戦略会話】沈黙回避フィラー：発話権を維持し「ええと、つまり…」と時間を稼ぐ戦略",
        "intro": "外国語で話している際、言いたい単語や構文を頭の中で組み立てている間の「不自然な沈黙（awkward silence）」は、会話が途切れたり相手に発話権を奪われたりする最大の要因です。「Anu...」「Gini lho...」「Maksud saya...」などのフィラーを効果的に配置し、発話権（floor）をキープしながら思考時間を稼ぐ技術を習得します。",
        "pairs": [
            ("Bagaimana menjelaskannya ya...", "Gimana ya ngomongnya...", "思考時間の確保"),
            ("Hal yang ingin saya garis bawahi adalah...", "Intinya tuh gini sebenernya...", "要点整理のフィラー"),
            ("Sebentar, saya sedang memikirkannya...", "Bentar-bentar, apa tuh namanya...", "記憶想起のフィラー"),
            ("Dapat dikatakan bahwa...", "Bisa dibilang kayak...", "曖昧化・クッションのフィラー")
        ],
        "drill": [
            ("【ビジネス】少し考えを整理させてください。（Perkenankan saya merapikan poin pemikiran sejenak.）", "Mohon waktu beberapa detik ya, saya coba rangkai poin utamanya dulu.", "モホン ワクトゥ ブルブラパ ドゥティッ ヤ、サヤ チョバ ランカイ ポイン ウタマニャ ドゥル", "公式な思考時間要求。"),
            ("【日常会話】なんて言うかさ、要するにこういうこと！（Gimana ya ngomongnya, intinya tuh gini lho!）", "Gimana ya bilangnya... pokoknya mah intinya tuh gak sesimpel itu bro!", "ギマナ ヤ ビランニャ... ポコッニャ マ インティニャ トゥ ガッ ススィンペル イトゥ ブロ", "日常の思考つなぎ。"),
            ("【会議】言わば、一種のパイロット事業のようなものです。（Bisa dibilang ini semacam proyek percontohan.）", "Bisa dibilang kayak... semacem uji coba awal gitu lho, paham kan?", "ビサ ディビラン カヤッ... スマチェム ウジ チョバ アワル ギトゥ ロ、パハム カン", "類推フィラー。"),
            ("【同僚】あの件、ええと何だっけ？（Soal yang itu... apa tuh namanya?）", "Soal proyek yang kemarin... aduh bentar, apa ya namanya tuh, kok mendadak amnesia!", "ソアル プロイェッ ヤン クマレン... アドゥ ブンタル、アパ ヤ ナマニャ トゥ、コッ ムンダダッ アムネスィア", "物忘れフィラー。"),
            ("【意見表明】私の感覚から言えばですね。（Kalo menurut feeling gue ya...）", "Kalo dari kacamata gue pribadi sih... kayaknya ada langkah yang miss deh.", "カロ ダリ カチャマタ グエ プリバディ スィ... カヤッニャ アダ ランカ ヤン ミス デ", "私見挿入フィラー。"),
            ("【困惑】どう説明したらいいか難しいのですが。（Agak sulit mendeskripsikannya secara tepat.）", "Agak tricky sih ngejelasinnya, tapi bayangin aja skenario kayak gini...", "アガッ トリッキー スィ ンゲジュラスィンニャ、タピ バヤンイン アジャ スケナリオ カヤッ ブギニ", "難易度提示フィラー。"),
            ("【電話】ちょっと待って、今手元に資料を探してるから。（Bentar ya, lagi buka file-nya nih.）", "Tunggu bentar ya pak... ini filenya lagi loading... nah ini dia datanya!", "トゥング ブンタル ヤ パッ... イニ ファイルニャ ラギ ローディング... ナ イニ ディア データニャ", "実況型フィラー。"),
            ("【質問への即答回避】興味深い質問ですね。（Pertanyaan yang sangat menarik untuk dibedah.）", "Pertanyaan yang sangat bagus nih... begini ya kalau kita bedah dari akar masalahnya...", "プルタニャアン ヤン サンガット バグス ニ... ブギニ ヤ カロ キタ ブダ ダリ アカール マサラニャ", "質問褒めフィラー。"),
            ("【言いよどみ】あのー、名前なんだっけあの人。（Anu... siapa ya nama beliau?）", "Anu... itu tuh yang waktu rapat duduk di sebelah direktur, siapa tuh namanya?", "アヌ... イトゥ トゥ ヤン ワクトゥ ラパット ドゥドゥッ ディ スブラ ディレクトゥール、スィアパ トゥ ナマニャ", "「Anu」の自然な活用。"),
            ("【結論の前置き】つまり、一言で言うとですね。（Kalau diringkas dalam satu kalimat...）", "Jadi gini gampangnya... ujung-ujungnya kita tetep butuh tambahan orang.", "ジャディ ギニ ガンパンニャ... ウジュン ウジュンニャ キタ トゥタップ ブトゥ タンバハン オラン", "結論導入フィラー。"),
            ("【記憶の再確認】私の記憶が確かならば。（Sejauh ingatan saya...）", "Kalo gak salah inget sih ya... kejadiannya pas sebelum libur lebaran kemarin deh.", "カロ ガッ サラ インゲット スィ ヤ... クジャディアンニャ パス スブルム リブール ルバラン クマレン デ", "記憶確認フィラー。"),
            ("【沈黙阻止】まだ話すから割り込まないでね。（Gue belum selesai ngomong ya, jangan dipotong.）", "Tunggu-tunggu, belom kelar nih poinnya, dengerin dulu bentar ya bro!", "トゥング トゥング、ブロム クラル ニ ポインニャ、ドゥンゲルイン ドゥル ブンタル ヤ ブロ", "発話権キープ。"),
            ("【感情の整理】正直に告白するとね。（Sejujurnya kalau boleh buka-bukaan...）", "Jujurly ya... gue sendiri waktu pertama kali denger isu ini agak shock juga sih.", "ジュジュルリー ヤ... グエ スンディリ ワクトゥ プルタマ カリ ドゥンゲル イス イニ アガッ ショック ジュガ スィ", "心情告白フィラー。"),
            ("【話題の着地】まあ、大体そんな感じです！（Kurang lebih semacam itu gambarannya!）", "Yaaah... kira-kira gambarannya kayak gitu lah ya, gak jauh beda kok.", "ヤー... キラ キラ ガンバランニャ カヤッ ギトゥ ラ ヤ、ガッ ジャウ ベダ コッ", "着地フィラー。"),
            ("【総括】沈黙するな、繋げ！フィラーは考える脳のBGMである。（Filler adalah jembatan emas saat otak sedang memproses data.）", "Gunakan filler untuk mengulur waktu secara elegan tanpa kehilangan panggung bicara!", "グナカン フィラー ウントゥッ ムンウルール ワクトゥ スチャラ エレガン タンパ クヒランガン パングン ビチャラ", "フィラーの黄金律。")
        ],
        "quiz": [
            ("言いたいことを考えている間、沈黙を埋めて発話権を維持するインドネシア語の定番フィラーは？", ["Gimana ya ngomongnya... / Jadi gini lho...", "Selamat pagi semuanya!", "Tolong jangan ganggu saya!", "Berapa nomor telepon Anda?"], 1),
            ("相手からの鋭い質問に対し、時間を稼ぎながら威厳を保つスマートな切り返しは？", ["Pertanyaan yang sangat bagus dan menarik nih...", "Saya tidak mau menjawab!", "Pertanyaan Anda sangat bodoh!", "Saya mau pulang sekarang!"], 1),
            ("不自然な沈黙（awkward silence）が会話にもたらす最大のデメリットは？", ["相手に会話終了と誤解されたり、発話の主導権を奪われたりすること", "話すスピードが速くなりすぎること", "文法が正しくなりすぎること", "相手が怒り狂って暴れ出すこと"], 1)
        ]
    },
    {
        "slug": "10-self-correction-repair",
        "title": "【戦略会話】自己修正（リペア）：言い間違えた瞬間に「いや、違った、〜です」と軌道修正する",
        "intro": "会話の中で単語や数字、文法を言い間違えてしまった時、最も重要なのは「パニックにならず、その場ですぐに自然な軌道修正（Self-Correction / Repair）を入れること」です。「Eh bukan, maksud saya...（あ、違った、私の意図は…）」「Maksudnya...（つまり…）」など、ネイティブも日常的に使うリペア技術を習得します。",
        "pairs": [
            ("Maksud saya bukan A, melainkan B.", "Eh bukan A deng, maksudnya B!", "訂正・置換のレジスター差"),
            ("Mohon maaf, ralat sedikit mengenai...", "Ralat-ralat, tadi salah sebut!", "公式訂正 ⇄ カジュアル訂正"),
            ("Biar saya luruskan kekeliruan tadi.", "Gue lurusin dulu ya biar gak salah paham.", "誤解解消の宣言"),
            ("Maksudnya bukan begitu, tapi...", "Bukan gitu maksud gue, tapi...", "意図の修正")
        ],
        "drill": [
            ("【ビジネス】失礼いたしました、来週ではなく再来週の月曜日でした。（Mohon maaf, maksud saya bukan pekan depan, melainkan dua pekan lagi.）", "Mohon maaf ralat sedikit Bapak, maksud kami bukan pekan depan, melainkan tanggal 25.", "モホン マアフ ララット スディキット バパッ、マクスッド カミ ブカン プカン ドゥパン、ムラインカン タンガル ドゥアプル リマ", "公式な日付訂正（ralat）。"),
            ("【日常会話】あ、違った！5万ルピアじゃなくて50万だった。（Eh bukan deng, bukan lima puluh ribu, tapi lima ratus ribu!）", "Eh salah sebut gue! Bukan gocap, tapi gopek deng maksudnya!", "エ サラ スブット グエ！ ブカン ゴチャップ、タピ ゴペッ デン マクスッドニャ", "金額の口語自己修正。"),
            ("【会議】前言を撤回させてください、調査の結果データが異なっていました。（Perkenankan kami meralat pernyataan sebelumnya.）", "Izin meralat paparan barusan, setelah diverifikasi ulang, angkanya mencapai 15%.", "イジン ムララット パパラン バルサン、ストゥラ ディヴェリフィカスィ ウラン、アンカニャ ムンチャパイ リマブラス パーセン", "会議でのデータ訂正。"),
            ("【人名】あ、失礼しました、スハルトさんではなくスサントさんでした。（Eh maaf, bukan Pak Suharto, tapi Pak Susanto.）", "Eh keliru sebut nama, maksud saya Pak Susanto dari divisi keuangan, bukan Pak Suharto.", "エ クリルー スブット ナマ、マクスッド サヤ パッ スサント ダリ ディヴィスィ クウアンガン、ブカン パッ スハルト", "人名の即座リペア。"),
            ("【時間】朝の9時じゃなくて夜の9時です！（Bukan jam 9 pagi, tapi jam 9 malam!）", "Eh bukan jam 9 pagi deng, jam 21.00 malam maksudnya, kebalik tadi!", "エ ブカン ジャム ソンビラン パギ デン、ジャム ドゥアプル サトゥ マラム マクスッドニャ、クバリッ タディ", "昼夜の取り違え修正。"),
            ("【場所】西ジャカルタではなく南ジャカルタの支店でした。（Bukan cabang Jakarta Barat, melainkan Jakarta Selatan.）", "Ralat lokasi ya guys, acaranya bukan di Jakbar, tapi di Jaksel!", "ララット ロカスィ ヤ ガイズ、アチャラニャ ブカン ディ ジャッバール、タピ ディ ジャッセル", "場所のチャットリペア。"),
            ("【意図の修正】責めているわけじゃないよ、ただ心配なだけ。（Gue bukan nyalahin lu ya, maksudnya cuma khawatir doang.）", "Bukan maksud gue mau nyalahin lu ya bro, cuma pengen mastiin aja biar aman.", "ブカン マクスッド グエ マウ ニャライン ル ヤ ブロ、チュマ ペンゲン マスティイン アジャ ビアル アマン", "感情・ニュアンスの修正。"),
            ("【否定の訂正】行かないんじゃなくて、少し遅れて行きます。（Bukan tidak mau datang, tapi datang terlambat sedikit.）", "Eh bukan gak mau ikut ya, tapi gue nyusul agak siangan, gitu lho maksudnya.", "エ ブカン ガッ マウ イクット ヤ、タピ グエ ニュスル アガッ スィアンガン、ギトゥ ロ マクスッドニャ", "参加条件の修正。"),
            ("【単語の言い直し】大きいというより、むしろ重いと言った方が正確です。（Bukan besar, lebih tepatnya berat.）", "Bukan gede sih barangnya, lebih pas dibilang berat banget ya.", "ブカン グデ スィ バランニャ、ルビ パス ディビラン ブラット バンゲット ヤ", "語彙の精度向上リペア。"),
            ("【電話】番号を一桁間違えました。（Salah sebut satu digit nomornya barusan.）", "Aduh ralat satu digit terakhir ya pak, bukan angka 8 tapi angka 9.", "アドゥ ララット サトゥ ディジット トゥラキール ヤ パッ、ブカン アンカ ドラパン タピ アンカ ソンビラン", "電話番号の修正。"),
            ("【約束】キャンセルではなく、日時の変更をお願いしたいのです。（Bukan membatalkan, tapi menjadwalkan ulang.）", "Maksud kami bukan membatalkan kerja sama, melainkan menjadwalkan ulang pertemuan.", "マクスッド カミ ブカン ムムバタルカン クルジャ サマ、ムラインカン ムンジャドワルカン ウラン プルトゥムアン", "契約意図の修正。"),
            ("【事実誤認】私の勘違いでした、彼女は既婚者ではありません。（Saya salah sangka, ternyata beliau belum menikah.）", "Eh salah info gue barusan, ternyata dia masih single, sori-sori!", "エ サラ インフォ グエ バルサン、トゥルニャタ ディア マスィ シングル、ソリ ソリ", "勘違いの訂正。"),
            ("【方向】右じゃなくて左に曲がってください！（Eh bukan kanan pak, belok kiri!）", "Eh salah belok kiri pak di depan warung itu, aduh maaf kecele tadi!", "エ サラ ベロッ キリ パッ ディ ドゥパン ワルン イトゥ、アドゥ マアフ クチェレ タディ", "進行方向の緊急リペア。"),
            ("【数量】2個じゃなくて2箱でした！（Bukan 2 buah, tapi 2 dus!）", "Eh bukan dua biji mbak, dua kardus besar maksud saya, tolong diganti ya.", "エ ブカン ドゥア ビジ ムバッ、ドゥア カルドゥス ブサール マクスッド サヤ、トロン ディガンティ ヤ", "数量単位の修正。"),
            ("【総括】言い間違いを恐れるな。瞬時にリペアできる者こそが真の流暢な話者である。（Kemampuan meralat seketika adalah ciri penutur mahir.）", "Salah ucap itu wajar bagi manusiawi; yang penting sigap meralatnya tanpa panik!", "サラ ウチャップ イトゥ ワジャール バギ マヌスィアウィ；ヤン プンティン スィガップ ムララットニャ タンパ パニック", "自己修正の極意。")
        ],
        "quiz": [
            ("公式な場やビジネスで、直前の言い間違いを「少し訂正させてください」と述べる専門語は？", ["Ralat sedikit...", "Marah sedikit...", "Tidur sedikit...", "Makan sedikit..."], 1),
            ("口語で「あ、違った！そうじゃなくて〜だった！」と咄嗟に言い直す時に挟む間投詞は？", ["Eh bukan... deng, maksudnya...", "Pasti benar...", "Tidak mungkin salah...", "Harus begitu..."], 1),
            ("会話中の自己修正（Self-Correction）において最も重要なマインドセットは？", ["パニックにならず、その場ですぐに自然な訂正フレーズを挟んで軌道修正すること", "言い間違えたことを隠すために沈黙すること", "怒り出して他人のせいにすること", "二度と会話しないと誓うこと"], 1)
        ]
    }
]

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
    
    lines.append("## 2. 意味交渉（Negotiation of Meaning）のメカニズム\n")
    lines.append("第二言語習得論（SLA）におけるインターアクション仮説（Long）が示す通り、コミュニケーションの破綻を修復し、相手と意味をすり合わせる「意味交渉」のプロセスこそが、言語能力を飛躍的に高める最大の触媒です。\n")
    
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

print("Batch 1151-1160 generated successfully.")
