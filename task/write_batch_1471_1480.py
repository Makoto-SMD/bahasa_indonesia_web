# -*- coding: utf-8 -*-
"""
セクション35 第3バッチ (1471-1480) 記事生成スクリプト
【表現技法】プロの翻訳・通訳・高度表現テクニック
技術・IT・医療・特許・外交・文学・報道・通訳ノートテイキング
"""

import os

articles = [
    {
        "filename": "21-technical-manual-translation-safety.md",
        "title": "1471. 【産業翻訳】機械操作マニュアル・安全衛生規程の正確かつ明瞭な翻訳",
        "level": "産業技術翻訳者・製造業現場管理者（CEFR B2〜C1）",
        "intro": "自動車・重機・電子機器の操作説明書（Buku Panduan Pengoperasian）や労働安全衛生（K3: Keselamatan dan Kesehatan Kerja）マニュアルは、作業員の生命と工場の安全に直結する最高度の明瞭性（Kejelasan）が求められます。曖昧な指示や誤解を生む表現を排除し、誰が読んでも直感的に理解できる命令構文（Kalimat Perintah Baku）の翻訳技法を解説します。",
        "theory": [
            ("安全警告表示の4段階国際規格とインドネシア語定訳",
             "1. **【危険】BAHAYA (DANGER)**: 回避しないと死亡または重傷を招く切迫した危険。「Matikan sumber listrik utama sebelum membuka penutup mesin!（機械カバーを開ける前に主電源を切れ！）」\n"
             "2. **【警告】PERINGATAN (WARNING)**: 死亡または重傷を招くおそれがある潜在的危険。「Gunakan kacamata pelindung saat mengoperasikan mesin gerinda!（グラインダー操作時は保護メガネを着用せよ！）」\n"
             "3. **【注意】PERHATIAN (CAUTION)**: 軽傷または物的損害を招くおそれがある危険。「Jangan menyentuh bagian ini selama mesin beroperasi karena suhu tinggi!」\n"
             "4. **【注記・指示】CATATAN (NOTICE)**: 操作上の重要な補足・製品寿命延長のための指示。"),
            ("マニュアル翻訳の文体ルール",
             "- 動詞原形または受動態で簡潔に記述する（Pastikan... / Tekan tombol... / Bersihkan filter...）。\n"
             "- 「〜してください」を機械的に「Tolong...」と訳さず、公用指示語「Harap...」「Pastikan...」を用いる。")
        ],
        "problems": [
            {
                "q": "【安全マニュアル翻訳問題】「可燃性ガスの漏洩を防ぐため、バルブが完全に閉じていることを必ず確認してください。」の最も正確な産業マニュアル訳はどれか？",
                "options": [
                    "A. Pastikan katup tertutup rapat guna mencegah kebocoran gas yang mudah terbakar.",
                    "B. Tolong cek keran tutup rapat biar gas tidak keluar dan kebakaran.",
                    "C. Harap Anda melihat katup sudah mati supaya gas yang gampang api tidak lepas.",
                    "D. Harus yakin kalau pintu gas tertutup agar tidak ada gas meledak."
                ],
                "ans": "A. Pastikan katup tertutup rapat guna mencegah kebocoran gas yang mudah terbakar.",
                "expl": "「必ず確認せよ（Pastikan...）」「バルブが完全に閉じている（katup tertutup rapat）」「可燃性ガスの漏洩を防ぐため（guna mencegah kebocoran gas yang mudah terbakar）」という技術マニュアルの標準定型句を満たすのはAです。"
            }
        ],
        "table": [
            ("Pastikan...", "〜であることを確実に確認せよ（Make sure that...）"),
            ("katup tertutup rapat", "バルブが完全に密閉されている"),
            ("mudah terbakar", "可燃性の・引火しやすい（flammable）"),
            ("Alat Pelindung Diri (APD)", "個人防護具（PPE: ヘルメット・安全靴・メガネ等）"),
            ("Keselamatan dan Kesehatan Kerja (K3)", "労働安全衛生（Occupational Health & Safety）"),
            ("matikan sumber listrik", "主電源を遮断せよ・電源を切れ")
        ],
        "pro_tip": "技術マニュアルの指示文では、「Anda」や「Kita」などの主語を一切入れず、動詞から直接始める（Pastikan / Tekan / Hubungkan）のが世界の技術文書標準です。"
    },
    {
        "filename": "22-it-localization-ui-strings.md",
        "title": "1472. 【IT翻訳】ITソフトウェア・UI文字列のローカライズ：文字数制限と直感性",
        "level": "ITローカライザー・プロダクトデザイナー（CEFR B2〜C1）",
        "intro": "スマートフォンアプリやWebサービスのUI（User Interface）ローカライゼーションでは、「ボタン幅の制限」「画面の視認性」「用語の一貫性」が極めて厳格に求められます。日本語の短い漢字（例:「保存」「設定」「削除」）を、文字数が長くなりがちなインドネシア語へと直感的かつコンパクトに落とし込むプロのローカライズ技術を体系化します。",
        "theory": [
            ("主要UIアクション文字列の標準定訳と文字数最適化",
             "1. **基本アクションボタン**: \n"
             "   - 保存: **Simpan** (×Menyimpan)\n"
             "   - キャンセル・戻る: **Batal** / **Kembali**\n"
             "   - 削除: **Hapus** (×Menghapus)\n"
             "   - 設定: **Pengaturan** (×Setelan: Google系はSetelanだが一般はPengaturan)\n"
             "   - 編集: **Edit** / **Ubah**\n"
             "2. **状態・トグル・通知**: \n"
             "   - 有効 / 無効: **Aktif** / **Nonaktif**\n"
             "   - 成功しました: **Berhasil** (例: Profil berhasil diperbarui)\n"
             "   - 失敗しました: **Gagal** (例: Gagal memuat data)\n"
             "3. **プレースホルダーとエラーメッセージ**: \n"
             "   - 「メールアドレスを入力」: Masukkan alamat email\n"
             "   - 「必須項目です」: Bidang ini wajib diisi")
        ],
        "problems": [
            {
                "q": "【UIローカライズ演習】モバイルアプリのポップアップダイアログ「このアカウントを完全に削除しますか？この操作は取り消せません。」のUI文案として最も直感的で洗練されたものはどれか？",
                "options": [
                    "A. Hapus akun ini secara permanen? Tindakan ini tidak dapat dibatalkan.",
                    "B. Apakah Anda mau menghapus akun ini selamanya? Ini tidak bisa kembali lagi ya.",
                    "C. Mau buang akun ini sekarang? Nanti tidak bisa dibikin balik lho.",
                    "D. Apakah betul-betul ingin menghapuskan akun? Kalau sudah hapus selesai."
                ],
                "ans": "A. Hapus akun ini secara permanen? Tindakan ini tidak dapat dibatalkan.",
                "expl": "「Hapus akun... secara permanen?（アカウントを恒久的に削除しますか？）」「Tindakan ini tidak dapat dibatalkan（この操作は取り消せません）」というグローバルIT企業の標準的UIローカライズ基準に完全に合致しているのはAです。"
            }
        ],
        "table": [
            ("Simpan", "保存（Save）"),
            ("Batal", "キャンセル（Cancel）"),
            ("Hapus secara permanen", "完全に削除（Delete permanently）"),
            ("Pengaturan", "設定（Settings）"),
            ("Wajib diisi", "必須（Required field）"),
            ("Gagal memuat data", "データの読み込みに失敗しました")
        ],
        "pro_tip": "ボタンなどのラベルには、接頭辞 meN- を付けた動詞（Menyimpan, Menghapus）ではなく、語根動詞（Simpan, Hapus）を用いるのがUIローカライズの鉄則です。"
    },
    {
        "filename": "23-medical-pharmaceutical-translation.md",
        "title": "1473. 【メディカル翻訳】治験プロトコル・医薬品添付文書の翻訳：厳密な学術性と安全性",
        "level": "医薬翻訳者・臨床開発モニター・薬剤師（CEFR C1〜C2）",
        "intro": "治験総括報告書（Clinical Study Report）や医薬品添付文書（Brosur Obat / Informasi Produk untuk Pasien）は、人命に関わるため一切の誤訳や曖昧さが許されない最難関の専門翻訳分野です。インドネシア食品医薬品監督庁（BPOM）の規制基準に準拠した用量用法、副作用、禁忌事項の精密翻訳を解説します。",
        "theory": [
            ("医薬品添付文書の標準構成とBPOM公用語彙",
             "1. **適応症・効能効果（Indikasi）**: \n"
             "   - 用于治疗...（〜の治療に用いる） → Diindikasikan untuk pengobatan...\n"
             "2. **用法・用量（Posologi dan Cara Pemberian）**: \n"
             "   - 食前服用（diminum sebelum makan） ⇔ 食後服用（diminum sesudah makan）。\n"
             "   - 1日3回1錠ずつ（tiga kali sehari, satu tablet）。\n"
             "3. **禁忌（Kontraindikasi）**: \n"
             "   - 本剤の成分に対し過敏症の既往歴がある患者（pasien dengan riwayat hipersensitivitas terhadap zat aktif...）。\n"
             "4. **副作用・有害事象（Efek Samping / Kejadian yang Tidak Diinginkan）**: \n"
             "   - 悪心（mual）、眩暈（pusing）、肝機能障害（gangguan fungsi hati）。\n"
             "5. **使用上の注意・相互作用（Peringatan dan Perhatian / Interaksi Obat）**。")
        ],
        "problems": [
            {
                "q": "【医薬添付文書翻訳問題】「重篤な腎機能障害のある患者には本剤を投与してはならない（禁忌）。」の最も厳密な医薬インドネシア語訳はどれか？",
                "options": [
                    "A. Obat ini dikontraindikasikan pada pasien dengan gangguan fungsi ginjal berat.",
                    "B. Orang sakit ginjal parah dilarang minum obat ini.",
                    "C. Pasien yang ginjalnya rusak jangan dikasih obat ini sama sekali.",
                    "D. Obat ini tidak boleh untuk orang yang ada masalah berat pada ginjal."
                ],
                "ans": "A. Obat ini dikontraindikasikan pada pasien dengan gangguan fungsi ginjal berat.",
                "expl": "医学公用文では「〜には禁忌である」を「dikontraindikasikan pada pasien dengan...」と表現し、「重篤な腎機能障害」を「gangguan fungsi ginjal berat」と厳密に定訳するAが正解です。"
            }
        ],
        "table": [
            ("dikontraindikasikan", "禁忌である（contraindicated）"),
            ("gangguan fungsi ginjal", "腎機能障害（renal impairment）"),
            ("riwayat hipersensitivitas", "過敏症の既往歴（history of hypersensitivity）"),
            ("uji klinis fase III", "第III相臨床試験（Phase 3 Clinical Trial）"),
            ("efek samping yang merugikan", "有害な副作用（adverse drug reaction）"),
            ("Badan POM (BPOM)", "食品医薬品監督庁（インドネシアのFDA）")
        ],
        "pro_tip": "医療用語では、日常会話的な sakit ではなく、医学専門用語の「gangguan fungsi（機能障害）」「kerusakan（器質的損傷）」を厳格に使い分けることが求められます。"
    },
    {
        "filename": "24-patent-specification-translation.md",
        "title": "1474. 【特許翻訳】特許明細書・請求の範囲（Claims）の翻訳：権利範囲の明確化",
        "level": "特許翻訳者・弁理士・知財担当者（CEFR C1〜C2）",
        "intro": "特許権の排他的独占範囲を決定する「特許請求の範囲（Klaim Paten）」および「特許明細書（Deskripsi Paten）」。特許庁（DJKI: Direktorat Jenderal Kekayaan Intelektual）における審査を円滑に通過し、侵害訴訟に耐えうる権利範囲を構築するための特許特有の構文規則を徹底指南します。",
        "theory": [
            ("特許請求の範囲（Klaim）の2大構造ルール",
             "1. **前提部と特徴部の二段構成（Klaim Dua Bagian）**: \n"
             "   - 「［発明の名称］であって、…において、…を特徴とする［発明の名称］。」\n"
             "   - 公式構文: \"Suatu [発明名], yang meliputi: [構成要素A]; dan [構成要素B], **yang dicirikan oleh** [特徴的構成要素C].\"\n"
             "2. **オープンエンド（包括的記載） vs クローズド（限定記載）**: \n"
             "   - 「〜を備える・含む（comprising）」 → **meliputi** / **mencakup** (他の要素の追加を排除しない包括的権利).\n"
             "   - 「〜からなる（consisting of）」 → **terdiri atas** (記載された要素のみに限定).\n"
             "3. **単一センテンス原則**: \n"
             "   - どんなに長く複雑な請求項であっても、冒頭から末尾のピリオドまで「1つの文（satu kalimat utuh）」として統語的破綻なく完結させる。")
        ],
        "problems": [
            {
                "q": "【特許クレーム翻訳問題】「第1電極と、第2電極と、前記第1電極と第2電極の間に配置された固体電解質層と、を備える全固体電池。」の特許インドネシア語訳として最も適切なものはどれか？",
                "options": [
                    "A. Suatu baterai semua-padat (all-solid-state battery), yang meliputi: elektroda pertama; elektroda kedua; dan suatu lapisan elektrolit padat yang ditempatkan di antara elektroda pertama dan elektroda kedua tersebut.",
                    "B. Baterai padat yang punya elektroda nomor satu dan nomor dua serta ada lapisan elektrolit di tengah-tengahnya.",
                    "C. Sebuah baterai serba padat yang isinya elektroda pertama, elektroda kedua, dan elektrolit padat.",
                    "D. Baterai padat total yang dibuat dari elektroda kesatu dan kedua bersama lapisan elektrolit."
                ],
                "ans": "A. Suatu baterai semua-padat (all-solid-state battery), yang meliputi: elektroda pertama; elektroda kedua; dan suatu lapisan elektrolit padat yang ditempatkan di antara elektroda pertama dan elektroda kedua tersebut.",
                "expl": "特許の包括的記載「Suatu..., yang meliputi: ...; dan ... tersebut（前記〜）」という知的財産実務の厳格なクレーム構文を満たしているのはAのみです。"
            }
        ],
        "table": [
            ("Klaim Mandiri", "独立請求項（Independent Claim）"),
            ("Klaim Turunan", "従属請求項（Dependent Claim）"),
            ("yang dicirikan oleh...", "〜を特徴とする（characterized in that / characterized by）"),
            ("meliputi", "〜を備える・含む（comprising: 包括的記載）"),
            ("kebaruan dan langkah inventif", "新規性および進歩性（Novelty & Inventive Step）"),
            ("DJKI", "知的所有権総局（インドネシア特許庁）")
        ],
        "pro_tip": "特許翻訳では、前出の構成要素を指す「前記〜（the said...）」に対して「... tersebut」を必ず付着させ、先行詞との同一性を法的に明確化することが絶対不可欠です。"
    },
    {
        "filename": "25-diplomatic-speech-translation.md",
        "title": "1475. 【外交翻訳】首脳会談・国際会議スピーチの翻訳：儀礼的威厳と修辞技法",
        "level": "外交通訳・国際公務員・スピーチライター（CEFR C1〜C2）",
        "intro": "国家首脳のスピーチ、国連総会演説、ASEAN首脳会議における基調発言は、国家の尊厳と外交メッセージが凝縮された言説です。格式高き外交儀礼（Protokoler Diplomatik）、国際協調の修辞技法（Retorika Kerja Sama Internasional）、および平和と繁栄を希求する格調高い公用語法を伝授します。",
        "theory": [
            ("外交スピーチの3大必須レトリック",
             "1. **議長・列席首脳への儀礼的敬意（Apresiasi Protokoler）**: \n"
             "   - \"Yang Mulia para Pemimpin Negara Anggota ASEAN, Yang Terhormat Bapak Sekretaris Jenderal...\"\n"
             "2. **歴史的絆と共通のビジョン（Ikatan Historis & Visi Bersama）**: \n"
             "   - 「半世紀にわたる友好の歴史」 → persahabatan yang telah teruji oleh waktu selama setengah abad.\n"
             "   - 「自由で開かれた国際秩序の維持」 → menjaga tatanan internasional yang bebas dan terbuka berdasarkan supremasi hukum.\n"
             "3. **決意と連帯の呼びかけ（Komitmen & Seruan Solidaritas）**: \n"
             "   - \"Mari kita bergandengan tangan, melangkah maju bersama demi mewujudkan perdamaian abadi dan kemakmuran bersama.\"")
        ],
        "problems": [
            {
                "q": "【外交演説翻訳問題】首脳演説における「法の支配に基づく、自由で開かれた包摂的な地域秩序を構築するため、手を携えて前進しようではありませんか。」の格調高いインドネシア語訳はどれか？",
                "options": [
                    "A. \"Marilah kita bergandengan tangan untuk melangkah maju bersama dalam membangun tatanan kawasan yang bebas, terbuka, dan inklusif berdasarkan supremasi hukum.\"",
                    "B. \"Ayo kita pegang tangan sama-sama biar kawasan kita jadi bebas, buka, dan ada hukum yang kuat.\"",
                    "C. \"Mari kita jalan bareng-bareng untuk bikin daerah kita jadi bebas dan ramai menurut hukum.\"",
                    "D. \"Kita harus gabung tangan agar suasana kawasan menjadi terbuka luas dan patuh aturan.\""
                ],
                "ans": "A. \"Marilah kita bergandengan tangan untuk melangkah maju bersama dalam membangun tatanan kawasan yang bebas, terbuka, dan inklusif berdasarkan supremasi hukum.\"",
                "expl": "「bergandengan tangan（手を携えて）」「tatanan kawasan（地域秩序）」「inklusif（包摂的な）」「supremasi hukum（法の支配/法の至上）」という国際外交文書の標準格式を満たすAが名訳です。"
            }
        ],
        "table": [
            ("Yang Mulia (YM)", "閣下・殿下（Excellency / Majesty）"),
            ("supremasi hukum", "法の支配（Rule of Law）"),
            ("tatanan internasional yang inklusif", "包摂的な国際秩序"),
            ("bergandengan tangan", "手を携えて・団結して"),
            ("perdamaian abadi dan keadilan sosial", "恒久平和と社会正義（UUD1945の格調句）"),
            ("kemitraan strategis komprehensif", "包括的戦略的パートナーシップ")
        ],
        "pro_tip": "外交スピーチでは、インドネシア憲法前文（Pembukaan UUD 1945）にある名句「perdamaian abadi（恒久平和）」などの政治的共鳴語を適切に織り込むと、聴衆の心に深く刺さります。"
    },
    {
        "filename": "26-literary-translation-dialogue-style.md",
        "title": "1476. 【文学翻訳】登場人物の階層・人柄を表現する文体選択と語末詞",
        "level": "文芸翻訳者・文学研究者（CEFR C1〜C2）",
        "intro": "小説や戯曲、映画字幕の翻訳において、全登場人物が均一な標準語で話していては文学としての生命が失われます。ジャカルタ方言（Bahasa Gaul）、ジャワ語的語末小詞（dong, sih, kan, ya, kok, lho）、社会階層（kelas sosial）、世代差、親疎関係を反映したリアルで味わい深いセリフの訳出技法を分析します。",
        "theory": [
            ("セリフ翻訳における3大人称・語末詞の使い分け",
             "1. **親密な友人・若者同士（Bahasa Gaul Jakarta）**: \n"
             "   - 人称: **gue - lu**\n"
             "   - 語末詞: **dong**（念押し・甘え: \"Bantuin dong!\"）、**deh**（諦め・促し: \"Udah deh!\"）、**nih**（強調: \"Gue lagi sibuk nih.\"）。\n"
             "2. **庶民・家庭・目下への愛情（Akrab & Hangat）**: \n"
             "   - 人称: **aku - kamu** / 呼称（Mas, Mbak, Pak, Bu, Nak）。\n"
             "   - 語末詞: **kok**（反論・驚き: \"Kok gitu?\"）、**lho**（注意喚起: \"Hati-hati lho.\"）。\n"
             "3. **格式高い知識人・貴族・公の場（Baku & Santun）**: \n"
             "   - 人称: **saya - Anda / Tuan / Nyonya**\n"
             "   - 語末詞を一切排し、標準的な語彙と受動態で格調高く話す。")
        ],
        "problems": [
            {
                "q": "【セリフ翻訳演習】下町の親しみやすい若者が親友に対して「おいおい、そんなに怒るなよ。冗談だってば！」と軽く宥めるセリフの翻訳として最も自然なものはどれか？",
                "options": [
                    "A. \"Yah, jangan marah gitu dong, Bro. Gue cuma bercanda kali!\"",
                    "B. \"Wahai sahabatku, janganlah Anda murka, sesungguhnya saya hanya bergurau.\"",
                    "C. \"Tolong Anda tidak boleh marah sangat banyak, perkataan saya tadi palsu.\"",
                    "D. \"Jangan ada kemarahan dalam hati Anda, saya bermaksud membuat lelucon saja.\""
                ],
                "ans": "A. \"Yah, jangan marah gitu dong, Bro. Gue cuma bercanda kali!\"",
                "expl": "都会の若者同士の自然な会話（gitu dong, Bro, gue, cuma bercanda kali）を完璧に再現しているのはAです。他選択肢は直訳または文語的すぎてセリフとして完全に死んでいます。"
            }
        ],
        "table": [
            ("dong", "〜だよ／〜してよ（促し・当然・甘え）"),
            ("deh", "〜してよ／もう〜だ（促し・納得・諦念）"),
            ("sih", "〜だけどね／一体〜（含み・疑問）"),
            ("kok", "なぜ・どうして（意外・反論）"),
            ("lho", "〜なんだよ・〜だよ（注意喚起・驚き）"),
            ("cuma bercanda kali", "冗談に決まってんだろ")
        ],
        "pro_tip": "字幕翻訳では文字数制限が厳しいため、「語末詞1文字（dong/sih/deh）」で登場人物の性格や感情の機微を瞬時に伝える技術が最も重宝されます。"
    },
    {
        "filename": "27-literary-translation-metaphor-culture.md",
        "title": "1477. 【文化翻訳】比喩・文化的暗号の翻訳：注釈をつけずに文脈で溶け込ませる職人技",
        "level": "文芸翻訳者・上級学習者（CEFR C1〜C2）",
        "intro": "「秋の日は釣瓶落とし」「清水の舞台から飛び降りる」のような文化固有の比喩を、欄外注釈（footnote）だらけにしては読書の没入感を破壊してしまいます。異文化のメタファーを、インドネシアの読者が自然に追体験できるように文脈内で溶け込ませる『文化的脱中心化・現地化（Domestikasi vs Foreignisasi）』の職人技を解説します。",
        "theory": [
            ("文化的メタファー処理の3大翻訳アプローチ",
             "1. **機能的等価物への置換（Functional Equivalence）**: \n"
             "   - 日: 「カエルの子はカエル」 → イ: **Air cucuran atap jatuhnya ke pelimbahan juga**（または Buah jatuh tidak jauh dari pohonnya: 親の血を引く）。\n"
             "   - 日: 「喉元過ぎれば熱さを忘れる」 → イ: **Habis manis sepah dibuang**（用が済めば捨てられる）。\n"
             "2. **文脈内での解きほぐし・語義の埋め込み（Textual Integration）**: \n"
             "   - 注釈をつけず、比喩の持つ感情・意味を本文の中に自然に補いながら描写する。\n"
             "3. **異国情緒の保持（Foreignizing with Context Clues）**: \n"
             "   - 文化固有の単語（Tatami, Yukata, Wayang）をそのまま残しつつ、前後の動詞や形容詞で読者にその質感や役割を直感させる。")
        ],
        "problems": [
            {
                "q": "【ことわざ・比喩翻訳問題】「彼は一度の失敗に懲りて、すっかり臆病になってしまった（羹に懲りて膾を吹く）。」のインドネシア語の等価的ことわざとして最も適切なものはどれか？",
                "options": [
                    "A. Sekali terantuk, dua kali tengadah.（一度つまずけば、二度目は上を向いて注意する）",
                    "B. Bagai air di daun talas.（里芋の葉の上の水滴のように定まらない）",
                    "C. Bagai kerakap tumbuh di batu.（岩の上に生える植物のように悲惨な境遇）",
                    "D. Ada udang di balik batu.（岩の裏にエビがいる＝下心がある）"
                ],
                "ans": "A. Sekali terantuk, dua kali tengadah.（一度つまずけば、二度目は上を向いて注意する）",
                "expl": "「一度痛い目に遭ったことで過剰に警戒する」という教訓の等価的なインドネシアのことわざは「Sekali terantuk, dua kali tengadah（一度つまずいたら、次は用心深くなる）」です。"
            }
        ],
        "table": [
            ("sekali terantuk, dua kali tengadah", "一度の失敗に懲りて用心深くなる"),
            ("buah jatuh tidak jauh dari pohonnya", "蛙の子は蛙・親の血は争えない"),
            ("ada udang di balik batu", "下心がある・裏がある"),
            ("bagai air di daun talas", "優柔不断・意見が定まらない"),
            ("domestikasi", "自文化化（読者に馴染む表現に置き換える技法）"),
            ("foreignisasi", "異文化化（現地の文化色をそのまま残す技法）")
        ],
        "pro_tip": "翻訳文学で最も読者を興ざめさせるのは「※注：日本の伝統的な〜」という頻繁な訳注です。名訳とは、文脈そのものの中に注釈の意味が自然に溶け込んでいる訳文を指します。"
    },
    {
        "filename": "28-news-journalism-translation-tempo.md",
        "title": "1478. 【報道翻訳】報道・時事ニュースの翻訳：見出しの切れ味と事実伝達のスピード感",
        "level": "国際通信社特派員・ニュース翻訳者（CEFR C1〜C2）",
        "intro": "通信社（ロイター、ブルームバーグ、アンタラ通信）や新聞社におけるニュース翻訳は、「1分1秒を争う速報性（Kecepatan）」と「1文字の誤りも許されない正確性（Akurasi）」の極限のバランスです。読者の目を一瞬で捉える見出し（Judul Berita）の作成術と、5W1Hを凝縮したリード文（Lead）の高速翻訳技術を伝授します。",
        "theory": [
            ("ニュース翻訳の2大鉄則",
             "1. **見出し（Headline）の動詞短縮とインパクト**: \n"
             "   - 受動態の di- よりも、力強い能動他動詞（meN- の省略形や語根）を好む。\n"
             "   - 例: 「中央銀行が利上げを発表」 → **BI Kerek Suku Bunga Acuan Jadi 6%**（menaikkanではなく俗語的・躍動的なkerekを使用）。\n"
             "   - 例: 「政府が汚職根絶を誓約」 → **Pemerintah Bidik Transformasi Total Birokrasi**。\n"
             "2. **逆ピラミッド構造（Inverted Pyramid）の死守**: \n"
             "   - 最も重要な事実（結論・数字）を第1パラグラフ（Lead）の先頭に配置し、背景情報は後ろの段落へと流し込む。")
        ],
        "problems": [
            {
                "q": "【ニュース見出し翻訳問題】「インドネシア新首都ヌサンタラへの大統領府移転、インフラ未整備により延期へ」というニュースの見出しとして、最も切れ味鋭いジャーナリスティックなインドネシア語はどれか？",
                "options": [
                    "A. Infrastruktur Belum Rampung, Pemindahan Kantor Presiden ke IKN Resmi Ditunda",
                    "B. Kantor Presiden belum mau pindah ke IKN karena masih banyak bangunan rusak",
                    "C. Ada berita bahwa perpindahan ibu kota ke IKN batal sebab belum selesai",
                    "D. Gedung belum jadi maka Presiden tidak jadi pergi ke kota baru tahun ini"
                ],
                "ans": "A. Infrastruktur Belum Rampung, Pemindahan Kantor Presiden ke IKN Resmi Ditunda",
                "expl": "「Infrastruktur Belum Rampung（インフラ未整備・未完了）」を前置して理由を端的に示し、「Pemindahan... Resmi Ditunda（移転が正式延期）」と結論を力強く打ち出したAがプロの新聞見出しそのものです。"
            }
        ],
        "table": [
            ("kerek suku bunga", "金利を引き上げる（ニュース見出しの定番躍動動詞）"),
            ("belum rampung", "未完の・工事中である（belum selesaiの見出し語）"),
            ("resmi ditunda", "正式に延期された"),
            ("membidik target", "目標を照準に定める・狙う"),
            ("tumbuh melesat", "急成長する・爆発的に伸びる"),
            ("kantor berita", "通信社（news agency）")
        ],
        "pro_tip": "インドネシアの経済新聞（Bisnis Indonesia, Kontan）の見出しでは、menaikkanのかわりに「kerek（滑車で巻き上げる）」、menurunkanのかわりに「pangkas（刈り込む）」などの躍動感ある比喩動詞が好まれます。"
    },
    {
        "filename": "29-academic-paper-abstract-translation.md",
        "title": "1479. 【学術翻訳】学術論文アブストラクトの翻訳：国際学術水準の格調高き論述体",
        "level": "大学院生・研究者・学術翻訳者（CEFR C1〜C2）",
        "intro": "国際学術誌（Scopus / SINTA 1・2収録誌）に採択されるための論文アブストラクト（Abstrak Makalah Ilmiah）翻訳では、学術文体（Laras Ilmiah）の厳格な統語規則が課されます。研究背景、問題提起、方法論、発見事実、示唆を、受動構文と標準学術ターミノロジーを用いて無駄なく凝縮する技法を指南します。",
        "theory": [
            ("学術アブストラクトの定型フレームワークと統語構文",
             "1. **研究目的（Tujuan Penelitian）**: \n"
             "   - \"Penelitian ini bertujuan untuk menginvestigasi secara komprehensif korelasi antara...\"\n"
             "2. **方法論（Metodologi）**: \n"
             "   - \"Dengan mengadopsi pendekatan kuantitatif, data dikumpulkan melalui survei terhadap 500 responden...\"\n"
             "3. **実証的知見（Temuan Empiris）**: \n"
             "   - \"Hasil analisis regresi mengindikasikan bahwa variabel X berpengaruh positif dan signifikan terhadap variabel Y (p < 0,01).\"\n"
             "4. **学術的・実践的示唆（Implikasi Teoretis & Praktis）**: \n"
             "   - \"Temuan ini memberikan kontribusi teoretis bagi literatur mengenai... sekaligus menawarkan rekomendasi strategis bagi...\"")
        ],
        "problems": [
            {
                "q": "【論文要旨翻訳演習】「本研究の実証結果は、持続可能なサプライチェーン管理が企業の財務パフォーマンスに有意なプラスの影響を及ぼすことを示唆している。」の国際学術水準のインドネシア語訳はどれか？",
                "options": [
                    "A. Hasil empiris penelitian ini mengindikasikan bahwa manajemen rantai pasok berkelanjutan berpengaruh positif dan signifikan terhadap kinerja keuangan perusahaan.",
                    "B. Dari hasil riset ini kita tahu kalau rantai pasok hijau bikin untung uang kantor naik banyak.",
                    "C. Temuan kami memperlihatkan bahwa cara kerja suplai yang awet membawa hasil manis bagi finansial.",
                    "D. Data membuktikan kalau manajemen suplai bagus pasti perusahaannya jadi kaya raya."
                ],
                "ans": "A. Hasil empiris penelitian ini mengindikasikan bahwa manajemen rantai pasok berkelanjutan berpengaruh positif dan signifikan terhadap kinerja keuangan perusahaan.",
                "expl": "「Hasil empiris penelitian ini mengindikasikan bahwa...（実証結果は〜を示唆している）」「manajemen rantai pasok berkelanjutan（持続可能なサプライチェーン管理）」「berpengaruh positif dan signifikan（有意な正の影響を及ぼす）」という完全な学術公用語を満たすAが正解です。"
            }
        ],
        "table": [
            ("temuan empiris", "実証的知見・研究成果（empirical findings）"),
            ("berpengaruh positif dan signifikan", "有意な正の影響を及ぼす（統計分析用語）"),
            ("analisis regresi linear", "線形回帰分析（linear regression analysis）"),
            ("kontribusi teoretis", "理論的貢献"),
            ("menginvestigasi korelasi", "相関関係を調査・解明する"),
            ("implikasi praktis", "実践的示唆・政策提言")
        ],
        "pro_tip": "論文要旨では「Saya meneliti（私は研究した）」のような一人称を排し、「Penelitian ini dilakukan untuk...（本研究は〜のために実施された）」と客観構文を徹底することが査読通過の絶対条件です。"
    },
    {
        "filename": "30-interpreting-note-taking-technique.md",
        "title": "1480. 【通訳技術】逐次通訳のノートテイキング技術：シンボル記号と情報配置の工夫",
        "level": "プロ通訳者・会議通訳志望者（CEFR C1〜C2）",
        "intro": "プロの逐次通訳者（Penerjemah Lisan Konsekutif）が話者の長大なスピーチを完璧に再現できる秘密は、「速記（Shorthand）」ではなく「概念のシンボル化と情報配置（Note-taking Technique）」にあります。言語に依存せず、矢印・記号・縦書き配置を駆使して脳のワーキングメモリを解放するプロのノートテイキング術を公開します。",
        "theory": [
            ("通訳ノートテイキングの3大原則（ロザンの7原則準拠）",
             "1. **脱言語化とシンボル化（Deverbalization & Symbols）**: \n"
             "   - 言葉ではなく概念を記号化する。\n"
             "   - 国: インドネシア＝**RI**, 日本＝**Jap/JP**, アメリカ＝**US**。\n"
             "   - 動き: 増加＝**↑**, 減少＝**↓**, 因果・発展＝**→**, 比較・対比＝**≠**。\n"
             "   - 概念: 経済＝**$**, 会議・合意＝**OK / ◯**, 課題・問題＝**? / !**。\n"
             "2. **縦書き階段配置（Verticality & Stacking）**: \n"
             "   - 横に長く書かず、主語（S）→ 述語（V）→ 目的語（O）を上から下へ階段状に配置し、一瞥で構造を把握する。\n"
             "3. **接続関係の左端配置（Shift & Margin）**: \n"
             "   - しかし（But）、ゆえに（So）、また（+）などの論理接続詞はノートの左マージンに大きく記す。")
        ],
        "problems": [
            {
                "q": "【通訳メモ解読問題】通訳者のノートに次のように縦書きでメモされていた。\n[But] RI $ ↑ \n      → inflasi ↑ \n      → BI: Rate ↑\nこのメモが表す発言内容として最も忠実な日本語訳出はどれか？",
                "options": [
                    "A. しかしながら、インドネシア経済の成長に伴いインフレ圧力が高まったため、中央銀行は利上げに踏み切りました。",
                    "B. でもインドネシアのお金が増えたので、みんな買い物をして中銀が怒りました。",
                    "C. インドネシアの景気が悪くなってインフレが止まったため、金利は下がりました。",
                    "D. しかし中央銀行はインフレを恐れて経済成長を止めるために金利を据え置きました。"
                ],
                "ans": "A. しかしながら、インドネシア経済の成長に伴いインフレ圧力が高まったため、中央銀行は利上げに踏み切りました。",
                "expl": "[But]（しかしながら）＋ RI $ ↑（インドネシア経済の成長）＋ → inflasi ↑（その結果インフレ上昇）＋ → BI: Rate ↑（中銀が政策金利引き上げ）という論理連鎖を正確に日本語化したAが正解です。"
            }
        ],
        "table": [
            ("deverbalisasi", "脱言語化（言葉を概念・映像に変えて保持する）"),
            ("penataan vertikal", "縦方向配置（主語・動詞・目的語の階段配置）"),
            ("memori jangka pendek", "短期記憶・作業記憶（Working Memory）"),
            ("penerjemahan konsekutif", "逐次通訳（Consecutive Interpreting）"),
            ("penerjemahan simultan", "同時通訳（Simultaneous Interpreting）"),
            ("simbol universal", "普遍的シンボル記号（矢印、不等号、通貨記号）")
        ],
        "pro_tip": "通訳ノートは「綺麗に書く」のではなく「自分の頭の中にある記憶を呼び戻すためのトリガー」に過ぎません。発言終了後0.5秒で訳出し始めるための配置を極めましょう。"
    }
]

def generate_markdown(a):
    theory_content = ""
    for idx, (title, desc) in enumerate(a["theory"], 1):
        theory_content += f"### 2.{idx}. {title}\n\n{desc}\n\n"

    problem_items = ""
    for idx, p in enumerate(a["problems"], 1):
        opts = "\n".join([f"- {opt}" for opt in p["options"]])
        problem_items += f"""### 第{idx}問

{p['q']}

{opts}

<details>
<summary>正解と解説を見る</summary>

**正解**: 「**{p['ans']}**」

**解説**:
{p['expl']}
</details>

---

"""

    table_rows = ""
    table_header = "| 表現・項目 | 解説・対応用法 |\n| :--- | :--- |\n"
    for row in a["table"]:
        table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "プロの翻訳・通訳・高度表現テクニック。{a['title']}の実務分析、翻訳ストラテジー、実戦比較演習まで徹底指導。"
---

<div class="category-badge">高度翻訳・通訳技術</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 専門領域の課題と背景

{a['intro']}

---

## 2. プロの翻訳・通訳ストラテジー

{theory_content}
---

## 3. 実戦翻訳・通訳比較演習

実務の現場で通用する正確無比なプロの訳文・訳出を練り上げる実戦演習です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要専門用語・構文対比テーブル

本講のテーマに関連する重要専門用語・公用表現一覧です。

{table_header}{table_rows}
---

## 5. プロ翻訳者・通訳者の着眼点・ワンポイントアドバイス

> [!TIP]
> **実務現場で役立つワンポイント・アドバイス**:
> {a['pro_tip']}

---

## 6. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "translation-stylistics")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
