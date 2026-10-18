"""Writer Script: Articles 1001 - 1010 for docs/output/
"""

articles_data = [
    {
        "slug": "01-svo-word-order",
        "title": "【瞬間作文】基本語順（SVO）と名詞修飾（DM則）の即時産出",
        "intro": "インドネシア語の骨格は「SVO語順」と「後置修飾（DMの法則）」です。日本語の「SOV（主語・目的語・動詞）」および「前置修飾」の発想を頭の中で瞬時に反転させ、1秒以内に文を口から出す反射神経を鍛えます。",
        "rules": [
            ("SVOの原則", "主語（S）＋ 動詞（V）＋ 目的語（O）の順。英語と同様の語順ですが、be動詞が不要なため、名詞・形容詞を直接置くだけで述語になります。"),
            ("DMの法則（Hukum D-M）", "Diterangkan（修飾される主名詞）が先、Menerangkan（説明する語）が後。「赤い車」は mobil merah、「私の本」は buku saya、「新しい家」は rumah baru となります。")
        ],
        "drill": [
            ("私はコーヒーを飲みます。", "Saya minum kopi.", "サヤ ミヌム コピ", "S(Saya) + V(minum) + O(kopi) の基本SVO構文。"),
            ("彼は熱いお茶を飲みます。", "Dia minum teh panas.", "ディア ミヌム テ パナス", "teh（お茶）＋ panas（熱い）の後置修飾。"),
            ("私たちは新しい車を買いました。", "Kami membeli mobil baru.", "カミ ムンブリ モビル バル", "mobil（車）＋ baru（新しい）。"),
            ("私の友達はジャカルタに住んでいます。", "Teman saya tinggal di Jakarta.", "トゥマン サヤ ティンガル ディ ジャカルタ", "teman saya（私の友達）が主語。"),
            ("あの大きな家は私のものです。", "Rumah besar itu milik saya.", "ルマ ブサール イトゥ ミリッ サヤ", "rumah besar itu（あの大きな家）＋ milik saya（私のもの）。"),
            ("彼女はインドネシア語の小説を読んでいます。", "Dia membaca novel bahasa Indonesia.", "ディア ムンバチャ ノフェル バハサ インドネシア", "novel（小説）を後置修飾で具体化。"),
            ("私の母は美味しいナシゴレンを作ります。", "Ibu saya memasak nasi goreng enak.", "イブ サヤ ムマサッ ナシ ゴレン エナッ", "nasi goreng enak（美味しいナシゴレン）。"),
            ("父は毎朝黒い靴を履きます。", "Ayah memakai sepatu hitam setiap pagi.", "アヤ メマカイ スパトゥ ヒタム スティアプ パギ", "sepatu hitam（黒い靴）。"),
            ("この小さなオフィスには3台のパソコンがあります。", "Kantor kecil ini memiliki tiga komputer.", "カントール クチル イニ メミリキ ティガ コンピューテル", "kantor kecil ini（この小さなオフィス）。"),
            ("先生は厚い辞書を持っています。", "Guru membawa kamus tebal.", "グル ムンバワ カムス トゥバル", "kamus tebal（厚い辞書）。"),
            ("私は昨日とても甘いマンゴーを食べました。", "Saya kemarin makan mangga sangat manis.", "サヤ クマリン マカン マンガ サンガット マニス", "mangga sangat manis（とても甘いマンゴー）。"),
            ("私の兄は新しいバイクを洗っています。", "Kakak saya mencuci motor baru.", "カカッ サヤ ムンチュチ モトル バル", "motor baru（新しいバイク）。"),
            ("彼らは白いシャツを着ています。", "Mereka memakai kemeja putih.", "ムレカ メマカイ クメジャ プティ", "kemeja putih（白いシャツ）。"),
            ("私の妹は青いドレスが好きです。", "Adik saya suka gaun biru.", "アディッ サヤ スカ ガウン ビル", "gaun biru（青いドレス）。"),
            ("あの高いビルは国立銀行です。", "Gedung tinggi itu bank nasional.", "グドゥン ティンギ イトゥ バンク ナシオナル", "gedung tinggi itu（あの高いビル）。be動詞不要。")
        ],
        "quiz": [
            ("「私の白い猫」の正しいインドネシア語順は？", ["kucing putih saya", "saya putih kucing", "putih kucing saya", "kucing saya putih"], 1),
            ("「私は甘い紅茶を飲む」をSVOで組み立てると？", ["Saya minum teh manis.", "Saya teh manis minum.", "Minum saya teh manis.", "Teh manis saya minum."], 1),
            ("「あの古い車」の正しい表現は？", ["mobil tua itu", "tua mobil itu", "itu mobil tua", "mobil itu tua"], 1)
        ]
    },
    {
        "slug": "02-negation-tidak-bukan",
        "title": "【瞬間作文】否定詞 tidak と bukan の反射的使い分け",
        "intro": "日本語の「〜ない / 〜ではない」に対して、インドネシア語は述語の品詞によって厳密に使い分けます。動詞・形容詞は「tidak」、名詞・代名詞・前置詞句は「bukan」です。迷わず0.5秒で選ぶ反射回路を構築します。",
        "rules": [
            ("tidak ＋ 動詞 / 形容詞", "動作や状態を否定します。tidak makan（食べない）、tidak mahal（高くない）、tidak bisa（できない）。"),
            ("bukan ＋ 名詞 / 代名詞 / 指示詞", "「AではなくBである」という本質・属性を否定します。bukan guru（教師ではない）、bukan saya（私ではない）、bukan ini（これではない）。")
        ],
        "drill": [
            ("私は学生ではありません。", "Saya bukan mahasiswa.", "サヤ ブカン マハシスワ", "名詞 mahasiswa の否定は bukan。"),
            ("この料理は辛くありません。", "Makanan ini tidak pedas.", "マカナン イニ ティダッ プダス", "形容詞 pedas の否定は tidak。"),
            ("彼はコーヒーを飲みません。", "Dia tidak minum kopi.", "ディア ティダッ ミヌム コピ", "動詞 minum の否定は tidak。"),
            ("それは私のバッグではありません。", "Itu bukan tas saya.", "イトゥ ブカン タス サヤ", "名詞句 tas saya の否定は bukan。"),
            ("私たちは急いでいません。", "Kami tidak buru-buru.", "カミ ティダッ ブルブル", "形容詞的状態の否定は tidak。"),
            ("これは私の車ではなく、上司の車です。", "Ini bukan mobil saya, melainkan mobil bos.", "イニ ブカン モビル サヤ ムラインカン モビル ボス", "「〜ではなく」の対比否定 bukan ... melainkan。"),
            ("私は魚が好きではありません。", "Saya tidak suka ikan.", "サヤ ティダッ スカ イカン", "感情動詞 suka の否定は tidak。"),
            ("彼女は日本人ではありません、韓国人です。", "Dia bukan orang Jepang, melainkan orang Korea.", "ディア ブカン オラン ジュパン ムラインカン オラン コレア", "国籍名詞の否定は bukan。"),
            ("そのホテルは高くありませんでした。", "Hotel itu tidak mahal.", "ホテル イトゥ ティダッ マハル", "形容詞 mahal の否定は tidak。"),
            ("電話したのは私ではありません。", "Bukan saya yang menelepon.", "ブカン サヤ ヤン ムネレポン", "人称代名詞 saya の否定は bukan。"),
            ("今日は雨が降っていません。", "Hari ini tidak hujan.", "ハリ イニ ティダッ フジャン", "天候・動詞の状態否定は tidak。"),
            ("それは解決策ではありません。", "Itu bukan jalan keluar.", "イトゥ ブカン ジャラン クルアール", "名詞句 jalan keluar の否定は bukan。"),
            ("私はまだお腹が空いていません。", "Saya belum lapar.", "サヤ ブロン ラパル", "「まだ〜ない」は belum を使用（tidak の派生）。"),
            ("彼らは敵ではありません、味方です。", "Mereka bukan musuh, melainkan kawan.", "ムレカ ブカン ムスフ ムラインカン カワン", "名詞 musuh の否定は bukan。"),
            ("私はその決定に同意しません。", "Saya tidak setuju dengan keputusan itu.", "サヤ ティダッ スツジュ ドゥンガン クプトゥサン イトゥ", "動詞 setuju の否定は tidak。")
        ],
        "quiz": [
            ("「私は先生ではありません」の空欄に入るのは？ Saya ___ guru.", ["bukan", "tidak", "belum", "jangan"], 1),
            ("「このスープは美味しくない」の空欄に入るのは？ Sup ini ___ enak.", ["tidak", "bukan", "jangan", "tanpa"], 1),
            ("「これではなくあれです」の正しい構文は？", ["Bukan ini, melainkan itu.", "Tidak ini, melainkan itu.", "Jangan ini, melainkan itu.", "Belum ini, melainkan itu."], 1)
        ]
    },
    {
        "slug": "03-pronouns-kinship",
        "title": "【瞬間作文】親称代名詞（Anda, Bapak, Ibu, Mas, Mbak）の適切な使い分け",
        "intro": "インドネシア語には英語の「you」に当たる単純な単一語がありません。相手の社会的地位、年齢、性別、親密さに応じて敬称・親称を自然に切り替える必要があります。失礼にならず、かつ親密な距離感を瞬時に選択するドリルです。",
        "rules": [
            ("Bapak / Ibu（最上級の敬意・公の場）", "成人男性には Bapak（Pak）、成人女性には Ibu（Bu）。目上、顧客、上司、公式な場での標準二人称。"),
            ("Mas / Mbak（親密な同世代・サービス店）", "ジャワ発祥で全国に定着。若い男性・同世代には Mas、若い女性には Mbak。カフェ、屋台、同僚間での必須呼称。"),
            ("Anda（公的・距離のある改まった二人称）", "広告、アナウンス、初対面の距離を置いた場。日常会話で多用すると冷たい印象を与えるので注意。")
        ],
        "drill": [
            ("（上司の男性に）部長、書類をお持ちしました。", "Pak, saya membawa dokumennya.", "パッ サヤ ムンバワ ドクメンニャ", "目上男性への呼びかけは Pak。"),
            ("（年配の女性店員に）お母さん、これいくらですか？", "Bu, berapa harganya ini?", "ブ ブラパ ハルガニャ イニ", "成人・年配女性への敬称は Bu。"),
            ("（カフェの若い男性店員に）お兄さん、アイスコーヒーを1つお願いします。", "Mas, minta es kopi satu ya.", "マス ミンタ エス コピ サトゥ ヤ", "若い男性店員には Mas。"),
            ("（コンビニの女性店員に）お姉さん、袋は要りません。", "Mbak, tidak perlu kantong plastik.", "ムバッ ティダッ プルル カントン プラスティッ", "若い女性店員には Mbak。"),
            ("（お客様へ）お客様はどちらへ行かれますか？", "Bapak mau pergi ke mana?", "バパッ マウ プルギ ク マナ", "男性客へは Anda ではなく Bapak を主語にする。"),
            ("（同僚の年上男性に）先輩、一緒に昼食に行きませんか？", "Mas, mau makan siang bersama?", "マス マウ マカン シアン ブルサマ", "親しい年上男性同僚への呼びかけ。"),
            ("（公式アンケートで）あなたのメールアドレスを入力してください。", "Silakan masukkan alamat email Anda.", "シラカン マスッカン アラマット イーメール アンダ", "公的文書・UIでは Anda を使用。"),
            ("（タクシードライバーに）運転手さん、右に曲がってください。", "Pak, tolong belok kanan.", "パッ トロン ベロッ カナン", "ドライバーへの丁寧な呼びかけは Pak。"),
            ("（友達同士で）君は明日暇？", "Kamu besok senggang?", "カム ベソッ スンガン", "対等な親しい友人には kamu を使用。"),
            ("（先生に質問）先生、この意味を教えていただけますか？", "Pak guru, boleh jelaskan arti ini?", "パッ グル ボレ ジュラスカン アルティ イニ", "教師への呼びかけは Pak guru / Bu guru。"),
            ("（屋台の若い男性に）お兄さん、サンバルは少なめで。", "Mas, sambalnya sedikit saja ya.", "マス サンバルニャ スディキッ サジャ ヤ", "親しみやすく要求を伝える Mas。"),
            ("（ホテルの女性スタッフに）すみません、チェックアウトをお願いします。", "Mbak, mau check-out ya.", "ムバッ マウ チェックアウト ヤ", "受付の女性への親切な呼びかけ Mbak。"),
            ("（医師への相談）先生、昨日から熱があります。", "Dokter, saya demam sejak kemarin.", "ドクテル サヤ ドマム スジャッ クマリン", "医師には Dokter と直接呼びかける。"),
            ("（親しいグループで）みんな、準備できた？", "Teman-teman, sudah siap?", "トゥマントゥマン スダ シアップ", "複数への親しみある呼びかけ teman-teman。"),
            ("（目上の女性へのお礼）奥様、誠にありがとうございました。", "Terima kasih banyak, Ibu.", "トゥリマ カシ バニャッ イブ", "目上女性への敬意ある結び。")
        ],
        "quiz": [
            ("カフェで20代の男性店員を呼ぶ際の最も自然な呼称は？", ["Mas", "Anda", "Kamu", "Tuan"], 1),
            ("商談相手の40代男性社長に「あなた」と呼びかける自然な表現は？", ["Bapak", "Anda", "Kamu", "Saudara"], 1),
            ("女性の同僚（年上・同世代）への親しみやすい呼びかけは？", ["Mbak", "Nyonya", "Ibu guru", "Nona"], 1)
        ]
    },
    {
        "slug": "04-demonstratives-ini-itu",
        "title": "【瞬間作文】指示詞 ini / itu と場所表現（di sini / ke sana）の瞬発力",
        "intro": "近称「ini（これ・この）」と遠称「itu（あれ・それ・あの・その）」、および場所前置詞「di / ke / dari」と組み合わさる場所副詞（sini, situ, sana）の反射的出力ドリルです。",
        "rules": [
            ("ini と itu の位置", "名詞を修飾する場合は必ず名詞の「後ろ」に置きます（mobil ini, rumah itu）。単独で主語になる場合は文頭に置きます（Ini buku saya）。"),
            ("場所表現の3階層", "sini（ここ・話し手の領域）、situ（そこ・聞き手の領域）、sana（あそこ・双方から離れた遠い領域）。前置詞 di（〜で）、ke（〜へ）、dari（〜から）と合体します。")
        ],
        "drill": [
            ("これは私のパスポートです。", "Ini paspor saya.", "イニ パスポル サヤ", "Ini を主語にした名詞述語文。"),
            ("あの建物は病院です。", "Gedung itu rumah sakit.", "グドゥン イトゥ ルマ サキッ", "gedung itu（あの建物）＋ rumah sakit（病院）。"),
            ("ここでお待ちください。", "Tolong tunggu di sini.", "トロン トゥング ディ シニ", "di sini（ここで）。"),
            ("あそこへ行きましょう。", "Ayo kita pergi ke sana.", "アヨ キタ プルギ ク サナ", "ke sana（あそこへ）。"),
            ("あなたはどこから来ましたか？", "Anda datang dari mana?", "アンダ ダタン ダリ マナ", "dari mana（どこから）。"),
            ("この席は空いていますか？", "Kursi ini kosong?", "クルシ イニ コソン", "kursi ini（この席）。"),
            ("あの人は誰ですか？", "Siapa orang itu?", "シアパ オラン イトゥ", "orang itu（あの人）。"),
            ("私の家はあそこにあります。", "Rumah saya ada di sana.", "ルマ サヤ アダ ディ サナ", "ada di sana（あそこにある）。"),
            ("荷物をそこに置いてください。", "Tolong taruh barangnya di situ.", "トロン タルー バランニャ ディ シトゥ", "di situ（聞き手の近くのそこに）。"),
            ("彼はさっきここから出て行きました。", "Dia tadi keluar dari sini.", "ディア タディ クルアール ダリ シニ", "dari sini（ここから）。"),
            ("この新しいホテルはとても快適です。", "Hotel baru ini sangat nyaman.", "ホテル バル イニ サンガット ニャマン", "hotel baru ini（この新しいホテル）。"),
            ("その問題はもう解決しました。", "Masalah itu sudah selesai.", "マサラ イトゥ スダ スルサイ", "masalah itu（その問題）。"),
            ("ここから空港までどれくらいかかりますか？", "Berapa lama dari sini ke bandara?", "ブラパ ラマ ダリ シニ ク バンダラ", "dari sini ke bandara（ここから空港まで）。"),
            ("あれは私の注文した料理ではありません。", "Itu bukan makanan pesanan saya.", "イトゥ ブカン マカナン プサナン サヤ", "Itu を主語にした否定。"),
            ("ここには誰もいません。", "Tidak ada siapa-siapa di sini.", "ティダッ アダ シアパシアパ ディ シニ", "di sini（ここに）。")
        ],
        "quiz": [
            ("「この赤いペン」の正しい語順は？", ["pulpen merah ini", "ini pulpen merah", "merah pulpen ini", "pulpen ini merah"], 1),
            ("「あそこへ行く」を表す前置詞句は？", ["ke sana", "di sana", "dari sana", "ke sini"], 1),
            ("「そこ（聞き手の近く）に置いて」の表現は？", ["di situ", "di sini", "di mana", "ke sana"], 1)
        ]
    },
    {
        "slug": "05-question-words-5w1h",
        "title": "【瞬間作文】疑問詞（apa, siapa, di mana, kapan, kenapa, bagaimana）の即座疑問文",
        "intro": "疑問詞を使った問いかけはコミュニケーションの起点です。語順（文頭に置くか文末に置くか）と助詞 -kah によるフォーマル化の即時判断をトレーニングします。",
        "rules": [
            ("基本疑問詞 6選", "apa（何）、siapa（誰）、di mana（どこ）、kapan（いつ）、kenapa / mengapa（なぜ）、bagaimana（どうやって・どんな）。"),
            ("語順の柔軟性", "日常会話では疑問詞を文末に置くことも非常に自然です（Mau makan apa? / Tinggal di mana?）。文頭に置く場合は焦点化されます。")
        ],
        "drill": [
            ("これは何ですか？", "Ini apa? / Apa ini?", "イニ アパ / アパ イニ", "最も基本的な疑問文。"),
            ("あの人は誰ですか？", "Siapa orang itu?", "シアパ オラン イトゥ", "人物を尋ねる siapa。"),
            ("トイレはどこにありますか？", "Di mana toiletnya?", "ディ マナ トイレットニャ", "場所を尋ねる di mana。"),
            ("会議はいつ始まりますか？", "Kapan rapatnya dimulai?", "カパン ラパットニャ ディムライ", "時を尋ねる kapan。"),
            ("なぜ今日遅刻したのですか？", "Kenapa kamu terlambat hari ini?", "クナパ カム トゥルランバット ハリ イニ", "理由を尋ねる kenapa。"),
            ("駅へはどうやって行けばいいですか？", "Bagaimana cara pergi ke stasiun?", "バガイマナ チャラ プルギ ク スタシウン", "方法を尋ねる bagaimana cara。"),
            ("お名前は何とおっしゃいますか？", "Siapa nama Anda?", "シアパ ナマ アンダ", "名前を尋ねる時は apa ではなく siapa を使う点に注意！"),
            ("今何時ですか？", "Jam berapa sekarang?", "ジャム ブラパ スカラン", "時刻を尋ねる jam berapa。"),
            ("この服はいくらですか？", "Berapa harga baju ini?", "ブラパ ハルガ バジュ イニ", "数量・金額を尋ねる berapa。"),
            ("何人家族ですか？", "Berapa orang dalam keluarga Anda?", "ブラパ オラン ダラム クルアルガ アンダ", "人数を尋ねる berapa orang。"),
            ("どちらが好きですか、お茶かコーヒーか？", "Yang mana yang Anda suka, teh atau kopi?", "ヤン マナ ヤン アンダ スカ テ アタウ コピ", "選択肢を尋ねる yang mana。"),
            ("どうしてインドネシア語を勉強しているのですか？", "Mengapa Anda belajar bahasa Indonesia?", "ムンガパ アンダ ブラジャール バハサ インドネシア", "丁寧・標準的な「なぜ」mengapa。"),
            ("バリ島の天気はどうですか？", "Bagaimana cuaca di Bali?", "バガイマナ チュアチャ ディ バリ", "状態・様子を尋ねる bagaimana。"),
            ("何を探しているのですか？", "Sedang mencari apa?", "スダン マンチャリ アパ", "目的語を尋ねる文末の apa。"),
            ("誰と一緒にここに来ましたか？", "Dengan siapa Anda datang ke sini?", "ドゥンガン シアパ アンダ ダタン ク シニ", "同伴を尋ねる dengan siapa。")
        ],
        "quiz": [
            ("「お名前は何ですか？」の正しいインドネシア語は？", ["Siapa nama Anda?", "Apa nama Anda?", "Di mana nama Anda?", "Bagaimana nama Anda?"], 1),
            ("「どうやってそこに行きますか？」の疑問詞は？", ["Bagaimana", "Kapan", "Kenapa", "Berapa"], 1),
            ("「どちら（どれ）が好きですか？」の疑問詞句は？", ["Yang mana", "Di mana", "Ke mana", "Dari mana"], 1)
        ]
    },
    {
        "slug": "06-aspect-markers",
        "title": "【瞬間作文】アスペクト副詞（sudah, belum, sedang, akan, pernah）の反射文生成",
        "intro": "インドネシア語には動詞の活用（過去形・現在形・未来形）がありません。その代わりにアスペクト副詞を動詞の直前に置くことで、完了・未完了・進行・未来・経験を表現します。1秒で正確な副詞を差し込むドリルです。",
        "rules": [
            ("sudah（完了・すでに）", "動作が完了している、または状態が実現していることを示します（Sudah makan）。"),
            ("belum（未完了・まだ〜ない）", "否定 tidak と違い、「今後する予定だが現時点ではまだ」という前向きな未完了を示します（Belum makan）。"),
            ("sedang / lagi（進行・〜しているところ）", "動作が今まさに行われている最中であることを示します。口語では lagi。"),
            ("akan / mau（未来・〜する予定/つもり）", "将来の予定や意志を示します。口語では mau が多用されます。"),
            ("pernah / tidak pernah（経験・〜したことがある/ない）", "過去の経験の有無を示します。")
        ],
        "drill": [
            ("私はもう昼食を食べました。", "Saya sudah makan siang.", "サヤ スダ マカン シアン", "完了 sudah。"),
            ("彼はまだ宿題を終えていません。", "Dia belum menyelesaikan PR-nya.", "ディア ブロン ムンユルサイカン ペーエルニャ", "未完了 belum。"),
            ("母は今台所で料理をしています。", "Ibu sedang memasak di dapur.", "イブ スダン ムマサッ ディ ダプール", "進行 sedang。"),
            ("私たちは来週バリ島へ行きます。", "Kami akan pergi ke Bali minggu depan.", "カミ アカン プルギ ク バリ ミング ドゥパン", "未来 akan。"),
            ("あなたは日本に行ったことがありますか？", "Apakah Anda pernah pergi ke Jepang?", "アカパ アンダ プルナ プルギ ク ジュパン", "経験 pernah。"),
            ("私は一度もドリアンを食べたことがありません。", "Saya belum pernah makan durian.", "サヤ ブロン プルナ マカン ドゥリアン", "未経験 belum pernah。"),
            ("社長はもうオフィスに着きましたか？", "Apakah bos sudah tiba di kantor?", "アカパ ボス スダ ティバ ディ カントール", "到着完了の確認 sudah tiba。"),
            ("雨が降り始めています（今降っている）。", "Hujan sedang turun.", "フジャン スダン トゥルン", "天候の進行 sedang turun。"),
            ("私は明日新しいパソコンを買うつもりです。", "Saya mau membeli komputer baru besok.", "サヤ マウ ムンブリ コンピューテル バル ベソッ", "意志・未来 mau。"),
            ("彼らはまだ契約書にサインしていません。", "Mereka belum menandatangani kontrak.", "ムレカ ブロン ムナンダタンガニ コントラッ", "未完了 belum。"),
            ("私は今、運転中です。", "Saya sedang menyetir sekarang.", "サヤ スダン ムニョティル スカラン", "行動の最中 sedang menyetir。"),
            ("会議は間もなく始まります。", "Rapat akan segera dimulai.", "ラパット アカン スグラ ディムライ", "即座の未来 akan segera。"),
            ("以前このレストランに来たことがあります。", "Saya pernah datang ke restoran ini sebelumnya.", "サヤ プルナ ダタン ク レストラン イニ スブルムニャ", "過去の経験 pernah datang。"),
            ("彼らはまだ会議室にいます。", "Mereka masih ada di ruang rapat.", "ムレカ マシ アダ ディ ルアン ラパット", "継続 masih（まだ〜の状態が続いている）。"),
            ("薬をもう飲みましたか？", "Sudah minum obat?", "スダ ミヌム オバット", "日常会話の素早い確認 sudah。")
        ],
        "quiz": [
            ("「まだ食べていません」に対する自然な返答は？", ["Belum.", "Tidak.", "Bukan.", "Jangan."], 1),
            ("「今〜している最中」を表す副詞は？", ["sedang", "sudah", "akan", "pernah"], 1),
            ("「〜したことがある」を表す経験の副詞は？", ["pernah", "sudah", "akan", "masih"], 1)
        ]
    },
    {
        "slug": "07-basic-prepositions",
        "title": "【瞬間作文】前置詞（di, ke, dari, pada, kepada）の場所・方向マッピング",
        "intro": "場所と移動を表す基本前置詞は「di（静止・場所）」「ke（方向・目的地）」「dari（起点・出所）」の3本柱です。これに人物や時間を対象とする「pada」「kepada」を加えた正確な使い分けを反射化します。",
        "rules": [
            ("空間の3大前置詞", "di Jakarta（ジャカルタで）、ke kantor（オフィスへ）、dari stasiun（駅から）。"),
            ("pada vs kepada の厳格な使い分け", "pada は「時（pada jam 9）」または「物・機関（pada dokumen）」に接続。kepada は「人への伝達・送付（surat kepada Bapak）」に接続します。")
        ],
        "drill": [
            ("父は今オフィスにいます。", "Ayah sekarang ada di kantor.", "アヤ スカラン アダ ディ カントール", "静止・存在の場所 di kantor。"),
            ("私たちは明日空港へ行きます。", "Kami besok pergi ke bandara.", "カミ ベソッ プルギ ク バンダラ", "移動の目的地 ke bandara。"),
            ("彼はスラバヤから戻ってきました。", "Dia kembali dari Surabaya.", "ディア クンバリ ダリ スラバヤ", "出発点・起点 dari Surabaya。"),
            ("会議は午前9時に始まります。", "Rapat dimulai pada pukul sembilan pagi.", "ラパット ディムライ パダ プクル スンビラン パギ", "時間の起点 pada pukul 9。"),
            ("この手紙を社長にお渡しください。", "Tolong berikan surat ini kepada direktur.", "トロン ブリカン スラット イニ クパダ ディレクトゥール", "人への受け渡し kepada direktur。"),
            ("机の上に鍵があります。", "Ada kunci di atas meja.", "アダ クンチ ディ アタス メジャ", "位置名詞と結合 di atas（〜の上に）。"),
            ("猫が車の下に隠れました。", "Kucing bersembunyi di bawah mobil.", "クチン ブルスンブニ ディ バワ モビル", "位置名詞 di bawah（〜の下に）。"),
            ("彼は部屋の中に入りました。", "Dia masuk ke dalam kamar.", "ディア マスッ ク ダラム カマール", "内部への移動 ke dalam（〜の中へ）。"),
            ("彼らは教室から出て行きました。", "Mereka keluar dari ruang kelas.", "ムレカ クルアール ダリ ルアン クラス", "内部からの移動 dari luar/dalam。"),
            ("彼女はスーパーの前で待っています。", "Dia menunggu di depan supermarket.", "ディア ムヌング ディ ドゥパン スーパーマーケット", "位置名詞 di depan（〜の前に）。"),
            ("銀行は郵便局の後ろにあります。", "Bank ada di belakang kantor pos.", "バンク アダ ディ ブラカン カントール ポス", "位置名詞 di belakang（〜の後ろに）。"),
            ("私の家は薬局の隣にあります。", "Rumah saya ada di sebelah apotek.", "ルマ サヤ アダ ディ スブラ アポテック", "位置名詞 di sebelah（〜の隣に）。"),
            ("この小包は日本から届きました。", "Paket ini tiba dari Jepang.", "パケット イニ ティバ ダリ ジュパン", "出所 dari Jepang。"),
            ("ご質問は受付窓口へお尋ねください。", "Silakan ajukan pertanyaan kepada bagian resepsionis.", "シラカン アジュカン プルタニャアン クパダ バギアン レセプシオニス", "人・窓口への問い合わせ kepada。"),
            ("私たちは夜に散歩するのが好きです。", "Kami suka jalan-jalan pada malam hari.", "カミ スカ ジャランジャラン パダ マラム ハリ", "時間帯の標示 pada malam hari。")
        ],
        "quiz": [
            ("人に対して手紙を送る際の「〜へ」は？ kirim surat ___ Ibu.", ["kepada", "ke", "pada", "di"], 1),
            ("「午前8時に」を表す前置詞は？ ___ pukul 08.00", ["pada", "di", "ke", "kepada"], 1),
            ("「駅へ行く」を表す前置詞は？ pergi ___ stasiun", ["ke", "di", "dari", "pada"], 1)
        ]
    },
    {
        "slug": "08-abstract-prepositions",
        "title": "【瞬間作文】抽象前置詞（untuk, bagi, demi, tentang, menurut）の文脈適用",
        "intro": "単なる場所移動にとどまらず、目的・対象・観点・根拠などの論理関係を構築する抽象前置詞のパターンドリルです。論文やビジネス実務で必須の思考ツールを瞬時に口から出せるようにします。",
        "rules": [
            ("untuk vs bagi（目的と対象）", "untuk は「〜のための（目的・用途）」、bagi は「〜にとって（評価の対象者）」を明快に区別します。"),
            ("demi（献身・理由）", "「〜のために（国のため、正義のため、子供の未来のため）」という崇高な目的や大義名分。"),
            ("tentang vs menurut（話題と情報源）", "tentang は「〜について（話題）」、menurut は「〜によれば（観点・情報源）」を表します。")
        ],
        "drill": [
            ("これはあなたのためのプレゼントです。", "Ini hadiah untuk Anda.", "イニ ハディア ウントゥッ アンダ", "用途・受領者 untuk Anda。"),
            ("外国人にとって、インドネシア料理は時に辛すぎます。", "Bagi orang asing, makanan Indonesia terkadang terlalu pedas.", "バギ オラン アシン マカナン インドネシア トゥルカダン トゥルラル プダス", "評価対象者 Bagi orang asing。"),
            ("私たちは家族の未来のために一生懸命働きます。", "Kami bekerja keras demi masa depan keluarga.", "カミ ブケルジャ クラス ドミ マサ ドゥパン クルアルガ", "崇高な目的・献身 demi masa depan。"),
            ("私たちは新しいプロジェクトについて議論しました。", "Kami berdiskusi tentang proyek baru.", "カミ ブルディスクシ トゥンタン プロイェッ バル", "話題・テーマ tentang proyek baru。"),
            ("天気予報によれば、午後は大雨です。", "Menurut ramalan cuaca, sore ini hujan lebat.", "ムヌルット ラマラン チュアチャ ソレ イニ フジャン ルバット", "情報源 Menurut ramalan cuaca。"),
            ("私の意見では、この提案は非常に優れています。", "Menurut pendapat saya, usulan ini sangat bagus.", "ムヌルット プンダパット サヤ ウスラン イニ サンガット バグス", "自分の見解 Menurut pendapat saya。"),
            ("健康のために毎朝ジョギングをしています。", "Saya joging setiap pagi demi kesehatan.", "サヤ ジョギング スティアプ パギ ドミ クセハタン", "健康維持の大義 demi kesehatan。"),
            ("子供たちにとって、睡眠は極めて重要です。", "Bagi anak-anak, tidur sangatlah penting.", "バギ アナッアナッ ティドゥール サンガトラ ポンティン", "対象者 Bagi anak-anak。"),
            ("この部屋は会議のために使われます。", "Ruangan ini digunakan untuk rapat.", "ルアンガン イニ ディグナカン ウントゥッ ラパット", "用途 untuk rapat。"),
            ("その小説は愛と裏切りについての物語です。", "Novel itu bercerita tentang cinta dan pengkhianatan.", "ノフェル イトゥ ブルチュリタ トゥンタン チンタ ダン プンキアナタン", "主題 tentang cinta。"),
            ("法律によれば、すべての国民は平等です。", "Menurut hukum, semua warga negara setara.", "ムヌルット フクム スムア ワルガ ネガラ スタラ", "法規根拠 Menurut hukum。"),
            ("祖国のために命を捧げた英雄たち。", "Pahlawan yang berkorban demi tanah air.", "パフラワン ヤン ブルコルバン ドミ タナ アイル", "国への献身 demi tanah air。"),
            ("私にとって、あなたの笑顔が一番の幸せです。", "Bagi saya, senyuman Anda adalah kebahagiaan terbesar.", "バギ サヤ スニュマン アンダ アダラ クバハギアアン トゥルブサール", "私にとって Bagi saya。"),
            ("社長は会社の業績について報告しました。", "Direktur melaporkan tentang kinerja perusahaan.", "ディレクトゥール ムラポルカン トゥンタン キネルジャ プルサハアン", "報告対象 tentang kinerja。"),
            ("時間通りに到着するために、早く出発しましょう。", "Mari berangkat lebih awal untuk tiba tepat waktu.", "マリ ブルランカット ルビ アワル ウントゥッ ティバ トゥパット ワクトゥ", "目的節 untuk tiba。")
        ],
        "quiz": [
            ("「〜によれば（情報源）」を表す前置詞は？", ["menurut", "tentang", "untuk", "bagi"], 1),
            ("「私にとって（評価）」を表す最も自然な語句は？", ["Bagi saya", "Demi saya", "Tentang saya", "Untuk saya"], 1),
            ("「国のために（大義名分）」を表す前置詞は？ ___ tanah air", ["demi", "tentang", "menurut", "bagi"], 1)
        ]
    },
    {
        "slug": "09-auxiliary-verbs",
        "title": "【瞬間作文】助動詞（harus, boleh, bisa, mau, ingin）のニュアンス即座出力",
        "intro": "義務（harus）、許可（boleh）、可能（bisa / dapat）、意志（mau）、願望（ingin）の助動詞は、文の意図やトーンを決定づける最重要パーツです。相手への丁寧さや強制力の強弱を意識しながら瞬時に発話します。",
        "rules": [
            ("harus（義務・〜しなければならない）", "強い義務や必要性。否定の tidak harus は「〜しなくてもよい（不必要）」、禁止の「〜してはならない」は tidak boleh / jangan です。"),
            ("bisa vs dapat（可能と許可・状況）", "bisa は口語でも頻出の一般的可能、dapat は公的な場での獲得・可能。"),
            ("mau vs ingin（意志と願望）", "mau は「〜するつもり/〜する（具体的意志）」、ingin は「〜したい（心の中の願望・控えめな希望）」。")
        ],
        "drill": [
            ("私たちは今日この仕事を終わらせなければなりません。", "Kita harus menyelesaikan pekerjaan ini hari ini.", "キタ ハルス ムンユルサイカン プケルジャアン イニ ハリ イニ", "強い義務 harus。"),
            ("ここに入ってもいいですか？", "Boleh saya masuk ke sini?", "ボレ サヤ マスッ ク シニ", "許可を求める Boleh saya..."),
            ("ここでタバコを吸ってはいけません。", "Tidak boleh merokok di sini.", "ティダッ ボレ ムロコッ ディ シニ", "禁止（不許可）tidak boleh。"),
            ("あなたはインドネシア語を話せますか？", "Apakah Anda bisa berbicara bahasa Indonesia?", "アカパ アンダ ビサ ブルビチャラ バハサ インドネシア", "能力可能 bisa。"),
            ("私は熱い紅茶が飲みたいです。", "Saya ingin minum teh hangat.", "サヤ インギン ミヌム テ ハンガット", "丁寧な願望 ingin。"),
            ("彼は明日パーティーに来るつもりです。", "Dia mau datang ke pesta besok.", "ディア マウ ダタン ク ペスタ ベソッ", "具体的意志 mau。"),
            ("質問してもよろしいですか？", "Boleh saya bertanya?", "ボレ サヤ ブルタニャ", "丁寧な質問許可 Boleh saya bertanya?"),
            ("急ぐ必要はありません（急がなくてもよい）。", "Anda tidak harus buru-buru.", "アンダ ティダッ ハルス ブルブル", "義務の免除 tidak harus。"),
            ("私たちは困難を克服することができます。", "Kita dapat mengatasi kesulitan ini.", "キタ ダパット ムンガタシ クスリタン イニ", "格調高い可能 dapat。"),
            ("私はいつかバリ島に住みたいです。", "Saya ingin tinggal di Bali suatu hari nanti.", "サヤ インギン ティンガル ディ バリ スアトゥ ハリ ナンティ", "将来の夢・願望 ingin。"),
            ("パスポートを必ず持ってこなければなりません。", "Anda harus membawa paspor.", "アンダ ハルス ムンバワ パスポル", "必須の義務 harus membawa。"),
            ("試着してもいいですか？", "Boleh saya coba?", "ボレ サヤ チョバ", "買い物の定番フレーズ Boleh saya coba?"),
            ("私は辛い食べ物が食べられません。", "Saya tidak bisa makan makanan pedas.", "サヤ ティダッ ビサ マカン マカナン プダス", "不可能性 tidak bisa。"),
            ("社長とお話ししたいのですが。", "Saya ingin berbicara dengan direktur.", "サヤ インギン ブルビチャラ ドゥンガン ディレクトゥール", "ビジネスの丁寧な申し出 ingin。"),
            ("今日はお手伝いできません。", "Saya tidak dapat membantu hari ini.", "サヤ ティダッ ダパット ムンバントゥ ハリ イニ", "丁寧な辞退 tidak dapat。")
        ],
        "quiz": [
            ("「〜してはならない（禁止）」を表す助動詞句は？", ["tidak boleh", "tidak harus", "tidak bisa", "tidak mau"], 1),
            ("「試着してもいいですか？」の丁寧な切り出しは？", ["Boleh saya coba?", "Harus saya coba?", "Mau saya coba?", "Pasti saya coba?"], 1),
            ("「〜する必要はない（不必要）」を表すのは？", ["tidak harus", "jangan", "tidak boleh", "dilarang"], 1)
        ]
    },
    {
        "slug": "10-comparison-patterns",
        "title": "【瞬間作文】比較級・最上級・同等比較（lebih, paling, ter-, sama...dengan）",
        "intro": "物事の性質や度合いを比べる表現は、日常会話や商談で頻出します。「lebih（より〜）」「paling / ter-（最も〜）」「sama ... dengan（〜と同じくらい）」の基本型を即座に組み立てるドリルです。",
        "rules": [
            ("比較級: lebih ＋ 形容詞 ＋ daripada", "「A lebih besar daripada B（AはBより大きい）」。daripada は dari と略されることもあります。"),
            ("最上級: paling ＋ 形容詞 / ter- ＋ 形容詞", "paling murah / termurah（最も安い）、paling tinggi / tertinggi（最も高い）。"),
            ("同等比較: sama ＋ 形容詞 ＋ nya ＋ dengan / se- ＋ 形容詞", "sama tingginya dengan dia（彼と同じ高さ）、setinggi dia（彼と同じ高さ）。")
        ],
        "drill": [
            ("このホテルはあのホテルより新しいです。", "Hotel ini lebih baru daripada hotel itu.", "ホテル イニ ルビ バル ダリパダ ホテル イトゥ", "比較級 lebih baru daripada。"),
            ("私の兄は私より背が高いです。", "Kakak saya lebih tinggi daripada saya.", "カカッ サヤ ルビ ティンギ ダリパダ サヤ", "背が高い比較 lebih tinggi。"),
            ("これは店の中で一番安い商品です。", "Ini produk paling murah di toko.", "イニ プロドゥッ パリン ムラ ディ トコ", "最上級 paling murah。"),
            ("彼はクラスで一番頭が良い学生です。", "Dia siswa terpintar di kelas.", "ディア シスワ トゥルピンタル ディ クラス", "接頭辞 ter- による最上級 terpintar。"),
            ("私の部屋の広さはあなたの部屋と同じです。", "Kamar saya sama luasnya dengan kamar Anda.", "カマール サヤ サマ ルアスニャ ドゥンガン カマール アンダ", "同等比較 sama luasnya dengan。"),
            ("飛行機は電車よりもずっと速いです。", "Pesawat jauh lebih cepat daripada kereta.", "プサワット ジャウ ルビ チパット ダリパダ クレタ", "差の強調 jauh lebih cepat（ずっと速い）。"),
            ("インドネシア語は日本語ほど難しくありません。", "Bahasa Indonesia tidak sesulit bahasa Jepang.", "バハサ インドネシア ティダッ ススリット バハサ ジュパン", "同等否定 tidak sesulit（〜ほど難しくない）。"),
            ("これが市場で最も新鮮な魚です。", "Ini ikan tersegar di pasar.", "イニ イカン トゥルスガル ディ パサール", "最上級 tersegar。"),
            ("今日の気温は昨日より涼しいです。", "Suhu hari ini lebih sejuk daripada kemarin.", "スフ ハリ イニ ルビ スジュッ ダリパダ クマリン", "比較級 lebih sejuk。"),
            ("彼の成績は私と同じくらい良いです。", "Nilainya sebaik nilai saya.", "ニライニャ スバイッ ニライ サヤ", "接頭辞 se- による同等比較 sebaik。"),
            ("ジャカルタはバンドンより暑いです。", "Jakarta lebih panas daripada Bandung.", "ジャカルタ ルビ パナス ダリパダ バンドン", "気候の比較 lebih panas。"),
            ("健康は富よりも貴重です。", "Kesehatan lebih berharga daripada kekayaan.", "クセハタン ルビ ブルハルガ ダリパダ クカヤアン", "抽象概念の比較 lebih berharga。"),
            ("世界で最も高い山はエベレストです。", "Gunung tertinggi di dunia adalah Everest.", "グヌン トゥルティンギ ディ ドゥニア アダラ エベレスト", "最上級 gunung tertinggi。"),
            ("この道はあの道と同じくらい混んでいます。", "Jalan ini sama macetnya dengan jalan itu.", "ジャラン イニ サマ マチェットニャ ドゥンガン ジャラン イトゥ", "渋滞の同等比較 sama macetnya。"),
            ("最も重要なことは諦めないことです。", "Hal yang terpenting adalah tidak menyerah.", "ハル ヤン トゥルポンティン アダラ ティダッ ムニェラ", "最上級の強調 hal yang terpenting。")
        ],
        "quiz": [
            ("「AはBより大きい」の正しい構文は？", ["A lebih besar daripada B.", "A paling besar daripada B.", "A sama besar daripada B.", "A ter-besar daripada B."], 1),
            ("「一番安い」を表す単語は？", ["termurah", "se-murah", "lebih murah", "sama murah"], 1),
            ("「彼と同じくらい背が高い」を表す同等比較は？", ["setinggi dia", "lebih tinggi dia", "paling tinggi dia", "daripada tinggi dia"], 1)
        ]
    }
]

import os

for a in articles_data:
    filepath = os.path.join("docs/output", f"{a['slug']}.md")
    
    lines = []
    lines.append(f"# {a['title']}\n")
    lines.append(f"{a['intro']}\n")
    lines.append("## 1. 産出メカニズムと文法公式\n")
    for r_title, r_desc in a['rules']:
        lines.append(f"### {r_title}")
        lines.append(f"{r_desc}\n")
    
    lines.append("## 2. 瞬間口頭作文トレーニング（15本ノック）\n")
    lines.append("> [!TIP]")
    lines.append("> **トレーニング手順**: 日本語の文を見て、**1〜2秒以内**に声に出してインドネシア語を発話してください。その後、正解の文と解説を確認して口頭で3回リピートします。\n")
    
    for idx, (jp, id_sent, kana, exp) in enumerate(a['drill'], 1):
        lines.append(f"### 第{idx}問")
        lines.append(f"**日本語**: 「**{jp}**」\n")
        lines.append('<div class="id-example" markdown>\n')
        lines.append(f'<div class="id-sentence">\n{id_sent}\n</div>')
        lines.append(f'<div class="id-reading">\n{kana}\n</div>')
        lines.append(f'<div class="id-meaning">\n{jp}\n</div>')
        lines.append('</div>\n')
        lines.append(f"- **構造解説**: {exp}\n")
        lines.append("---\n")
        
    lines.append("## 3. 理解度チェッククイズ\n")
    for q_idx, (q_text, opts, ans_idx) in enumerate(a['quiz'], 1):
        lines.append(f"**Q{q_idx}. {q_text}**\n")
        for opt_idx, opt in enumerate(opts, 1):
            mark = " (正解)" if opt_idx == ans_idx else ""
            lines.append(f"- {opt_idx}. {opt}{mark}")
        lines.append("")
        
    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filepath}")

print("All 10 articles generated successfully.")
