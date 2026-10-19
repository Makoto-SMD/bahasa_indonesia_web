# -*- coding: utf-8 -*-
"""
セクション34 第5バッチ (1441-1450) 記事生成スクリプト
【資格演習】検定・UKBI直前実戦模試＆徹底解説
専門翻訳・面接・試験戦略・最高峰Istimewa/特A級＆究極の実戦模試
"""

import os

articles = [
    {
        "filename": "41-translation-clinic-business-letters.md",
        "title": "1441. 【翻訳演習】公式ビジネスレター・案内状の日イ相互翻訳",
        "level": "技能検定B級〜A級（CEFR B2〜C1）",
        "intro": "インドネシアとのビジネス現場や検定筆記試験で不可欠となるのが「公式ビジネスレター（Surat Resmi）」および「式典案内状（Surat Undangan）」の高度な翻訳能力です。日本の儀礼的な時候の挨拶や謙譲表現を、インドネシア語の標準公用レター定型構文へと論理的・格式高く変換する技法を徹底解説します。",
        "theory": [
            ("公式書簡（Surat Resmi）の構成要素と対比表現",
             "1. **発信者情報・頭書き**: Nomor（文書番号）, Lampiran（添付書類）, Hal/Perihal（件名）。\n"
             "2. **宛名（Alamat Surat）**: \"Yth. Bapak/Ibu [役職名], PT [社名]\" (Yth. = Yang Terhormat)。\n"
             "3. **前文・挨拶（Salam Pembuka）**: \"Dengan hormat,\"（謹啓・拝啓に相当）。\n"
             "4. **導入定型句（Pembuka Surat）**: \n"
             "   - 「平素は格別のご高配を賜り…」 → \"Sehubungan dengan hubungan kerja sama yang telah terjalin baik selama ini...\"\n"
             "   - 「〜についてご案内申し上げます」 → \"Bersama surat ini, kami bermaksud mengundang Bapak/Ibu dalam acara...\"\n"
             "5. **結語・感謝（Penutup Surat）**: \"Demikian surat undangan ini kami sampaikan. Atas perhatian dan kerja sama Bapak/Ibu, kami ucapkan terima kasih.\"")
        ],
        "problems": [
            {
                "q": "【日イ翻訳想定問題】\n次の日本文の公式ビジネスレターとしてのインドネシア語訳として最も格式高く適切なものはどれか？\n「貴社のますますのご発展を心よりお祈り申し上げます。」",
                "options": [
                    "A. Semoga perusahaan Bapak/Ibu semakin maju dan sukses di masa depan.",
                    "B. Kami berharap semoga PT Anda untung banyak terus.",
                    "C. Perusahaan Anda harus semakin besar setiap hari ya.",
                    "D. Kami mendoakan biar bisnis Bapak makin ramai selalu."
                ],
                "ans": "A. Semoga perusahaan Bapak/Ibu semakin maju dan sukses di masa depan.",
                "expl": "公式書簡では「Bapak/Ibu」を用いて敬意を示し、「semakin maju dan sukses di masa depan（将来にわたり益々発展し成功を収める）」と表現するのが格式高い定型句です。他選択肢は口語（banyak terus, ya, biar, makin ramai）が含まれ不適切です。"
            },
            {
                "q": "【イ日翻訳問題】\n\"Dengan ini kami mengonfirmasi bahwa seluruh pesanan telah dikirimkan sesuai dengan spesifikasi yang disepakati.\"\n最も自然なビジネス日本語訳はどれか？",
                "options": [
                    "A. これにより、全注文が合意された仕様に従って発送されたことを確認します。",
                    "B. 本状をもちまして、ご注文いただいた全商品が合意の仕様通りに発送完了いたしました旨、ご報告申し上げます。",
                    "C. これで注文が全部決められたスペック通りに送られたと確かめました。",
                    "D. この手紙で、全部の荷物が仕様通りに送られたことを証明します。"
                ],
                "ans": "B. 本状をもちまして、ご注文いただいた全商品が合意の仕様通りに発送完了いたしました旨、ご報告申し上げます。",
                "expl": "「Dengan ini（本状をもちまして）」「kami mengonfirmasi bahwa...（〜の旨、ご報告/確認申し上げます）」「sesuai dengan spesifikasi yang disepakati（合意された仕様通りに）」という日本の商慣習に即した敬語表現への意訳が模範です。"
            }
        ],
        "table": [
            ("Dengan hormat,", "拝啓・謹啓（公式レター冒頭の挨拶）"),
            ("Yang Terhormat (Yth.)", "〜様・〜殿（宛名への尊称）"),
            ("Hal / Perihal", "件名・表題（Subject）"),
            ("terjalin baik", "良好に構築・維持されている（協力関係）"),
            ("konfirmasi penerimaan", "受領確認（acknowledgement of receipt）"),
            ("Atas perhatian dan kerja sama...", "ご高配とご協力に感謝申し上げます（結語）")
        ],
        "pro_tip": "インドネシアのビジネス書簡では、「Bapak/Ibu」などの人称敬称を省略しないこと、受動態を基調とした客観的文体を維持することがプロフェッショナルな印象を与える決め手です。"
    },
    {
        "filename": "42-translation-clinic-economic-reports.md",
        "title": "1442. 【翻訳演習】中央銀行レポート・経済白書の日イ相互翻訳",
        "level": "技能検定A級〜特A級（CEFR C1〜C2）",
        "intro": "インドネシア中央銀行（Bank Indonesia）の金融政策報告書や財務省の経済白書（Nota Keuangan）は、高度な経済マクロ用語、指標分析、政策意図が凝縮されたテキストです。検定A級・特A級の翻訳大問で頻出する「金融引き締め・緩和」「為替相場防衛」「インフレ圧力」「経常収支」の精密翻訳を伝授します。",
        "theory": [
            ("マクロ経済・中央銀行レポートの頻出構文と定訳",
             "1. **金融政策スタンス**: \n"
             "   - 利上げ（menaikkan suku bunga acuan） ⇔ 利下げ（menurunkan suku bunga acuan）\n"
             "   - 金融引き締め（pengetatan moneter） ⇔ 金融緩和（pelonggaran moneter）\n"
             "2. **インフレ・物価動向**: \n"
             "   - インフレ圧力（tekanan inflasi）、物価安定（stabilitas harga）、購買力（daya beli）。\n"
             "3. **国際収支・為替市場**: \n"
             "   - 為替介入（intervensi pasar valas）、外貨準備高（cadangan devisa）、経常収支赤字/黒字（defisit/surplus transaksi berjalan）。")
        ],
        "problems": [
            {
                "q": "【経済翻訳演習】次の文の最も的確な日本語訳はどれか？\n\"Bank Indonesia memutuskan untuk mempertahankan BI-Rate sebesar 6,00 persen guna memastikan inflasi tetap terkendali dalam sasaran dan mendukung stabilitas nilai tukar rupiah di tengah ketidakpastian pasar keuangan global.\"",
                "options": [
                    "A. インドネシア銀行は、インフレ率が目標値内に抑制されていることを確実にし、世界的な金融市場の不確実性の中でルピア相場の安定を支援するため、政策金利（BIレート）を6.00パーセントに据え置くことを決定した。",
                    "B. 中央銀行は、インフレが目標通りに行くようにするため、また世界の金融が不安定な中でルピアを守るために、金利を6%のままにしておくことに決めた。",
                    "C. インドネシアの中央銀行はインフレを抑え込み、ルピア為替レートを安定させる目的で、BI金利を6%で持ち続ける判断を下した。",
                    "D. 世界金融の不透明感に対処してルピアを安定化させ、インフレを目標に入れるため、中銀は6%のレートを保つことを確定させた。"
                ],
                "ans": "A. インドネシア銀行は、インフレ率が目標値内に抑制されていることを確実にし、世界的な金融市場の不確実性の中でルピア相場の安定を支援するため、政策金利（BIレート）を6.00パーセントに据え置くことを決定した。",
                "expl": "「mempertahankan... sebesar 6,00 persen（〜を6.00%に据え置く）」「suku bunga acuan / BI-Rate（政策金利）」「sasaran inflasi（インフレ目標）」「stabilitas nilai tukar rupiah（ルピア相場の安定）」という経済公用語の厳格な定訳を完全に網羅しているのはAのみです。"
            }
        ],
        "table": [
            ("suku bunga acuan", "政策金利・基準金利（benchmark interest rate）"),
            ("mempertahankan suku bunga", "金利を据え置く（maintain interest rate）"),
            ("cadangan devisa", "外貨準備高（foreign exchange reserves）"),
            ("transaksi berjalan", "経常収支（current account）"),
            ("ketidakpastian pasar global", "世界市場の不確実性・不透明感"),
            ("daya beli masyarakat", "国民の購買力（purchasing power）")
        ],
        "pro_tip": "経済ニュースで「mempertahankan」は「維持する」だけでなく、金利文脈では「据え置く」と訳出するのが経済翻訳の業界基準です。"
    },
    {
        "filename": "43-translation-clinic-legal-notices.md",
        "title": "1443. 【翻訳演習】法務通知・コンプライアンス規程の日イ相互翻訳",
        "level": "技能検定A級〜特A級（CEFR C1〜C2）",
        "intro": "日系企業の現地法人運営やM&A、労務管理において極めて需要が高いのが「社内コンプライアンス規程（Kode Etik & Kepatuhan）」および「法的警告・契約解除通知（Surat Peringatan & Somasi）」の翻訳です。オランダ法理に基づくインドネシアの法務語彙と、日本企業の統治基準を齟齬なく繋ぐ高度な翻訳技法を学びます。",
        "theory": [
            ("法務・コンプライアンスの重要概念と定訳",
             "1. **秘密保持と利益相反**: \n"
             "   - 秘密保持義務（kewajiban menjaga kerahasiaan）、利益相反（benturan kepentingan / konflik kepentingan）。\n"
             "2. **贈収賄・腐敗防止**: \n"
             "   - 贈収賄（penyuapan）、便宜供与・キックバック（uang pelicin / gratifikasi）。\n"
             "3. **警告書と法的措置**: \n"
             "   - 催告書・督促状（somasi / surat peringatan）、損害賠償請求（tuntutan ganti rugi）、契約の解除（pemutusan perjanjian）。")
        ],
        "problems": [
            {
                "q": "【法務翻訳問題】次の条文の最も適切な日本語訳はどれか？\n\"Karyawan dilarang keras menerima hadiah, komisi, atau gratifikasi dalam bentuk apa pun dari pihak ketiga yang memiliki hubungan bisnis dengan Perusahaan guna menghindari potensi benturan kepentingan.\"",
                "options": [
                    "A. 従業員は、潜在的な利益相反を回避するため、会社と取引関係にある第三者からいかなる形態であれ贈物、手数料、または便宜供与を受け取ることを固く禁じられる。",
                    "B. 社員は、利益の衝突を避ける目的で、会社のビジネス相手からプレゼントやお金をもらうことは絶対に禁止されている。",
                    "C. 従業員が会社と関係のある人からお礼やリベートをもらうと利益相反になるので、どんな形でも受け取ってはいけない。",
                    "D. 会社の利益衝突を防ぐため、取引先からの贈り物やキックバックを従業員が受け取ることは一切禁止とする。"
                ],
                "ans": "A. 従業員は、潜在的な利益相反を回避するため、会社と取引関係にある第三者からいかなる形態であれ贈物、手数料、または便宜供与を受け取ることを固く禁じられる。",
                "expl": "「dilarang keras（固く禁じられる）」「gratifikasi（便宜供与/不正報酬）」「pihak ketiga yang memiliki hubungan bisnis（取引関係にある第三者）」「benturan kepentingan（利益相反）」という就業規則・法務規程の厳格な定訳を満たすのはAです。"
            }
        ],
        "table": [
            ("gratifikasi", "便宜供与・不正な謝礼・金品（bribery/kickback）"),
            ("benturan kepentingan", "利益相反（conflict of interest）"),
            ("uang pelicin", "便宜供与金・潤滑油（facilitation payment）"),
            ("ganti rugi", "損害賠償・損失補償（compensation/damages）"),
            ("surat peringatan (SP)", "始末書・懲戒警告書（warning letter）"),
            ("somasi", "法的催告書・内容証明郵便（legal notice/subpoena）")
        ],
        "pro_tip": "法務文書で「gratifikasi」は単なるプレゼントではなく、汚職防止法上の「公職者や取引先への不正な便益供与」を指す重い法概念です。文脈に応じて「便宜供与」と訳出してください。"
    },
    {
        "filename": "44-listening-comprehension-traps.md",
        "title": "1444. リスニング試験で引っかかりやすい同音異義語・似た発音の対策",
        "level": "技能検定B級〜A級 / UKBI Seksi I（CEFR B2〜C1）",
        "intro": "リスニング試験（Mendengarkan）で受験者が最も失点しやすいのが「類似音の聞き間違い（Minimal Pairs）」および「文脈による多義語の取り違え」です。子音の有声/無声（p/b, t/d, k/g）、母音の曖昧音（pepet vs taling）、音節の転置（kelapa vs kepala）など、出題者が仕掛ける聴解トラップを論理的に解体します。",
        "theory": [
            ("試験で頻出する紛らわしい類似音ペア（Minimal Pairs）",
             "1. **p vs b**: \n"
             "   - **pangsa** (シェア・配分) ⇔ **bangsa** (民族・国家)\n"
             "   - **pola** (パターン・様式) ⇔ **bola** (ボール・球)\n"
             "2. **k vs g**: \n"
             "   - **kanti** (仲間) ⇔ **ganti** (交代・交代する)\n"
             "   - **kala** (時・時代) ⇔ **gala** (樹脂・最高の)\n"
             "3. **母音曖昧音（e pepet /ə/ vs e taling /e/）の識別**: \n"
             "   - **perang** (/pəraŋ/ = 戦争) ⇔ **perang** (/peraŋ/ = 赤茶色の・ブロンドの)\n"
             "   - **serang** (/səraŋ/ = 攻撃する) ⇔ **Serang** (バンテン州のセラン市)\n"
             "4. **音節の転置・アナグラム型トラップ**: \n"
             "   - **kelapa** (ココナッツ) ⇔ **kepala** (頭・首長)\n"
             "   - **sahabat** (親友) ⇔ **syahadat** (信仰告白)")
        ],
        "problems": [
            {
                "q": "【聴解類似音判別問題】音声で「Perusahaan kami berhasil memperluas [______] pasar domestik hingga 35 persen.」と流れた。文脈上正しい単語はどちらか？",
                "options": [
                    "A. pangsa（市場シェア）",
                    "B. bangsa（民族・国家）",
                    "C. mangsa（獲物・犠牲者）",
                    "D. mangga（マンゴー）"
                ],
                "ans": "A. pangsa（市場シェア）",
                "expl": "「pangsa pasar」は「市場シェア（market share）」の定型ビジネスコロケーションです。発音が極めて近い「bangsa pasar」という表現は存在しません。"
            }
        ],
        "table": [
            ("pangsa pasar", "市場シェア（bangsa pasarではない）"),
            ("kepala kantor", "事務所長・支店長（kelapaではない）"),
            ("perang harga", "価格戦争・値下げ合戦（/pəraŋ/）"),
            ("rambut perang", "赤茶色の髪・金髪（/peraŋ/）"),
            ("ganti rugi", "損害賠償（kanti rugiではない）"),
            ("baku tembak", "銃撃戦（buku tembakではない）")
        ],
        "pro_tip": "リスニングでは、単語単体の音を判別しようとするのではなく「pasar と共起しているから pangsa」「rugi と共起しているから ganti」という『コロケーション（連語関係）』で自動判定するのが最も確実です。"
    },
    {
        "filename": "45-interview-speaking-strategies.md",
        "title": "1445. 面接・スピーキング試験で沈黙を作らず高得点を獲得するテクニック",
        "level": "技能検定A級・特A級二次試験 / UKBI Seksi V（CEFR C1〜C2）",
        "intro": "面接試験やUKBI口述試験（Seksi V）で最も致命的な減点となるのが「3秒以上の完全な沈黙（dead air）」です。質問を即座に咀嚼し、時間を稼ぎながら思考をまとめ、論理的かつ流暢に発話を展開するための『スマート・フィラー』『パラフレーズ技術』『自己訂正の技術』をマスターします。",
        "theory": [
            ("沈黙をゼロにする3大プロフェッショナル技術",
             "1. **知的フィラーによる時間稼ぎ（5秒の猶予獲得）**: \n"
             "   - \"Pertanyaan yang sangat menarik sekaligus mendasar...\"（極めて興味深く本質的なご質問です…）\n"
             "   - \"Jika kita mencermati dinamika persoalan tersebut...\"（その問題の力学を注意深く見つめてみますと…）\n"
             "2. **質問のオウム返し・敷衍（Paraphrasing）**: \n"
             "   - 相手の質問を自分の言葉で整理して発話する。「Terkait dengan apa yang Anda tanyakan mengenai dampak inflasi...」\n"
             "3. **自然で優雅な自己訂正（Self-Correction）**: \n"
             "   - 言い間違えた時に「あ、違った」と言わず、\"Maksud saya...\" または \"Atau lebih tepatnya...\"（あるいはより正確に言えば…）とスムーズに言い直す。")
        ],
        "problems": [
            {
                "q": "【面接応答問題】面接官から「インドネシアの少子高齢化への懸念についてどう考えるか」と不意を突かれた際、即座に知的に発話を始めるフレーズとして最も優れているものはどれか？",
                "options": [
                    "A. \"Terkait dengan transisi demografi yang Anda singgung, hal ini sesungguhnya menghadirkan paradoks antara bonus demografi dan kesiapan sistem jaminan sosial.\"",
                    "B. \"Aduh... tunggu sebentar ya pak, saya belum pernah mikirin soal itu sama sekali.\"",
                    "C. \"Anu... apa ya namanya... ya pokoknya orang tua makin banyak itu gawat sih.\"",
                    "D. \"Saya tidak tahu banyak tentang hal itu, bisakah ganti pertanyaan lain saja?\""
                ],
                "ans": "A. \"Terkait with transisi demografi yang Anda singgung, hal this sesungguhnya menghadirkan paradoks antara bonus demografi dan kesiapan sistem jaminan sosial.\"",
                "expl": "Aは「Terkait dengan... yang Anda singgung（あなたが言及された〜に関して）」と受けて時間を稼ぎつつ、「transisi demografi（人口転換）」「bonus demografi（人口ボーナス）」「paradoks（逆説）」という高度な概念を用いて論理的に切り込んでいます。"
            }
        ],
        "table": [
            ("transisi demografi", "人口動態の転換・人口転換"),
            ("bonus demografi", "人口ボーナス期"),
            ("atau lebih tepatnya...", "あるいはより正確に言えば…（自己訂正）"),
            ("pertanyaan mendasar", "本質的・根本的な質問"),
            ("jika kita cermati...", "注意深く観察・検討してみますと…"),
            ("paradoks", "パラドックス・逆説")
        ],
        "pro_tip": "口頭試験で最も評価されるのは「完璧な暗記スピーチ」ではなく「不意の質問に対して知的な態度と言語運用力で柔軟に対応できるアドリブ能力」です。"
    },
    {
        "filename": "46-exam-time-management-skills.md",
        "title": "1446. 検定本番で時間が足りなくなる人のための時間配分ストラテジー",
        "level": "技能検定B級〜特A級 / UKBI全等級（CEFR B1〜C2）",
        "intro": "「知識はあるのに、大問の最後で時間が足りなくなって大量失点した…」これは検定受験者が最も多く直面する悲劇です。本番80分〜90分の試験時間を1分単位でコントロールし、最大の得点効率（ROI）を生み出す『タイムマネジメント・プロトコル』を確立します。",
        "theory": [
            ("検定B級・A級の推奨タイムマネジメント表（80分試験）",
             "1. **大問1（接辞・短文補充 15問）**: 12分（1問45秒以内。迷ったら印をつけて次へ）。\n"
             "2. **大問2（誤文訂正・短文文法 10問）**: 15分（1問90秒。主語と述語の骨格を素早く走査）。\n"
             "3. **大問3（長文読解 3〜4題）**: 25分（設問先読み→スキャニングで1題6〜7分）。\n"
             "4. **大問4（日イ・イ日翻訳）**: 20分（下書きを短くし、公用構文で一気に清書）。\n"
             "5. **見直し＆マーク確認**: 8分（マークずれ、名前・受験番号の確認、保留問題の最終回答）。")
        ],
        "problems": [
            {
                "q": "【試験戦略シミュレーション】長文読解の第3問で、1つの難問に3分以上悩んでしまっている。試験戦略上、最も取るべき行動はどれか？",
                "options": [
                    "A. その設問に仮のマーク（最も可能性の高い選択肢）をつけ、問題用紙に大きく印をつけて即座に次の設問へ進む。",
                    "B. 答えが見つかるまで本文を最初からもう一度すべて精読し直す。",
                    "C. 翻訳問題の時間を削って、この長文問題にさらに5分追加する。",
                    "D. 試験官に質問して設問の意味が正しいか確認する。"
                ],
                "ans": "A. その設問に仮のマーク（最も可能性の高い選択肢）をつけ、問題用紙に大きく印をつけて即座に次の設問へ進む。",
                "expl": "試験における最大のタブーは「1問の難問への固執」です。配点は他の平易な設問と同じであることが多いため、仮マークをして即座に次へ進み、全問解き終えた後の「見直し時間（残り8分）」で戻るのが鉄則です。"
            }
        ],
        "table": [
            ("alokasi waktu", "時間配分（time allocation）"),
            ("lembar jawaban", "解答用紙・マークシート"),
            ("pemeriksaan ulang", "見直し・再点検（review）"),
            ("pertanyaan jebakan", "トラップ設問・引っかけ問題"),
            ("efisiensi pengerjaan", "解答効率・処理スピード"),
            ("manajemen stres", "ストレスコントロール・冷静さの維持")
        ],
        "pro_tip": "「分からない問題にぶつかったら1分で損切りする」というルールを事前に体に刷り込んでおくことが、時間不足を防ぐ唯一の特効薬です。"
    },
    {
        "filename": "47-psychological-prep-exam-day.md",
        "title": "1447. 試験当日のメンタルコントロールと直前1時間の最終チェックリスト",
        "level": "技能検定B級〜特A級 / UKBI全等級（全受験者対象）",
        "intro": "数ヶ月に及ぶ学習の成果を本番の数時間で100%発揮できるかどうかは、当日のメンタルコントロールと直前のルーティンにかかっています。極度の緊張による頭の真っ白化（Brain Freeze）を防ぐ心理調整法と、試験開始直前に目を通すべき「超重要チートシート」をまとめました。",
        "theory": [
            ("試験開始60分前の黄金ルーティン",
             "1. **60分前: 会場到着と環境順応**: トイレを済ませ、座席の位置、空調（冷房対策の上着必須）、時計の視認性を確認。\n"
             "2. **45分前: 脳のインドネシア語モードへの切り替え**: 日本語の思考を止め、短いインドネシア語ニュース記事を1本音読して耳と目を慣らす。\n"
             "3. **30分前: 最終チートシートの点検**: 不規則鼻音化（memproduksi, mengkritik）、EYD句読点、接続詞（baik... maupun...）の確認。\n"
             "4. **15分前: 呼吸法とマインドフルネス**: 参考書を閉じ、4秒吸って7秒止め8秒吐く深呼吸（4-7-8呼吸法）で自律神経を安定させる。")
        ],
        "problems": [
            {
                "q": "【直前チェック問題】試験開始直前に頭の中で復習すべき「二重子音で鼻音化脱落しない語」の組み合わせとして正しいものはどれか？",
                "options": [
                    "A. memproduksi, mengkritik, mentransfer",
                    "B. memroduksi, mengritik, menransfer",
                    "C. mentransaksikan, memromosikan, mengoleksi",
                    "D. mengecek, mengecat, mengebom"
                ],
                "ans": "A. memproduksi, mengkritik, mentransfer",
                "expl": "語頭が二重子音（pr-, kr-, tr-）の外来語は、p, k, t が脱落せずそのまま残るため、memproduksi, mengkritik, mentransfer が正解です。"
            }
        ],
        "table": [
            ("ketenangan mental", "精神の平静・落ち着き"),
            ("kedinginan ruang ujian", "試験室の冷え（冷房対策）"),
            ("pemanasan otak", "脳のウォーミングアップ"),
            ("pernapasan dalam", "深呼吸・呼吸法"),
            ("konsentrasi penuh", "完全な集中状態（フロー状態）"),
            ("lembar jawaban komputer (LJK)", "コンピュータ用マークシート")
        ],
        "pro_tip": "インドネシア国内や日本の試験会場では、冷房が異常に強く効いているケースが多々あります。防寒着（パーカーやカーディガン）を1枚必ず持参してください。"
    },
    {
        "filename": "48-ukbi-istimewa-masterclass.md",
        "title": "1448. 最高峰 UKBI Istimewa（特等）を目指すための超絶技巧研究",
        "level": "UKBI 最高等級 Peringkat Istimewa（スコア 726〜800 / CEFR C2+）",
        "intro": "UKBIの頂点に君臨する「Peringkat Istimewa（特等）」は、インドネシア人の国語学者・文学者・最高裁判事でも容易には到達できないとされる神話的等級です。726点以上のスコアを獲得するために要求される、古今東西の語彙体系、超絶的な文法・正書法精度、および高度な批評的読解力の深奥を探求します。",
        "theory": [
            ("Peringkat Istimewa 到達の3大極限要件",
             "1. **KBBI（大辞典）深層語彙の完全制覇**: サンスクリット語、アラビア語、オランダ語起源の文語・哲学・法律語彙（niskala, pragmatis, paripurna, diskresi, akuntabilitas）。\n"
             "2. **統語論（Sintaksis）の絶対的無欠性**: 複文の多層修飾関係、倒置構文（Inversi）、焦点化（Pemfokusan）の完璧な解読。\n"
             "3. **言説分析（Analisis Wacana）能力**: テキストの背後にあるイデオロギー、執筆者の社会的立場、メタファー（隠喩）の多重層構造の完全な理解。")
        ],
        "problems": [
            {
                "q": "【最上級語彙問題】「目に見えない・抽象的な・形而上の概念」を意味するサンスクリット由来の学術語彙はどれか？",
                "options": ["A. niskala", "B. sakala", "C. niscaya", "D. nirwana"],
                "ans": "A. niskala",
                "expl": "「niskala」は古代サンスクリットおよび古ジャワ語に由来し、哲学・文学において「形而上の・目に見えない（abstrak / tidak berwujud）」を意味します（sakala=目に見える/具象の、niscaya=確実に、nirwana=涅槃/解脱）。"
            }
        ],
        "table": [
            ("niskala", "形而上の・無形の・抽象的な（intangible / metaphysical）"),
            ("paripurna", "完全無欠の・全体を網羅した（sidang paripurna=本会議）"),
            ("diskresi", "裁量権・自由裁量（discretion）"),
            ("kemaslahatan umat", "大衆・社会全体の福利・公益"),
            ("kemahiran paripurna", "完全無欠な言語習熟度（Istimewaの定義）"),
            ("makna kontekstual", "文脈的・状況的意味")
        ],
        "pro_tip": "Istimewaを目指すレベルでは、単に文法書を読むのではなく、Tempo誌のコラム（Catatan Pinggir）や学術誌（Jurnal Bahasa dan Sastra）の論文を日常的に精読することが必須です。"
    },
    {
        "filename": "49-inken-special-a-hall-of-fame.md",
        "title": "1449. 技能検定 特A級合格者の学習法とノート作成術の徹底分析",
        "level": "技能検定特A級（日本国内最難関語学資格）",
        "intro": "合格率わずか数パーセント、年間合格者が数名にとどまるインドネシア語技能検定の最高峰「特A級」。この栄誉殿堂（Hall of Fame）に名を刻んだ歴代合格者たちが実践していた門外不出の学習法、語根派生語マッピングノート作成術、および通訳ラギング訓練プロトコルを徹底公開します。",
        "theory": [
            ("特A級合格者が実践する3大学習プロトコル",
             "1. **KOMPAS社説の3色ボールペン分析法**: \n"
             "   - 青: 新出の派生語・成句（Kata Majemuk）。\n"
             "   - 赤: 法律・経済・政治の公式定型構文（Struktur Baku）。\n"
             "   - 緑: 筆者のトーン・論理標識（Penanda Wacana）。\n"
             "2. **語根マッピング・ノート術（Buku Sakti Kata Dasar）**: \n"
             "   - 1つの語根（例: sangkut）から派生する全形式（menyangkut, bersangkut-paut, tersangkut, penyangkut, sangkutan）を用例と共に1ページに集約。\n"
             "3. **毎日のラジオニュース即時要約（Shadowing & Lagging）**: \n"
             "   - BBC Indonesia や VOA Indonesia の音声を聴き、3語遅れで要約を発話する通訳訓練法。")
        ],
        "problems": [
            {
                "q": "【特A級合格者レベル演習】語根「sangkut」の派生語の中で「〜に関連する・〜についてである」を意味する他動詞はどれか？",
                "options": ["A. menyangkut", "B. tersangkut", "C. persangkutan", "D. bersangkutan"],
                "ans": "A. menyangkut",
                "expl": "「menyangkut masa depan bangsa（国家の未来に関連する/関わる）」のように、他動詞「menyangkut」は「mengenai / berkaitan dengan」と同義の重要語です。"
            }
        ],
        "table": [
            ("menyangkut", "〜に関連する・関わる（mengenai/perihal）"),
            ("tersangkut perkara", "事件に巻き込まれる・連座する"),
            ("bersangkut paut", "密接に関連している・利害関係がある"),
            ("pihak yang bersangkutan", "関係当事者・関係者"),
            ("shadowing", "シャドーイング（音声を影のように追って発音）"),
            ("lagging", "ラギング（通訳で数秒遅れて意味を再構築する技術）")
        ],
        "pro_tip": "特A級の壁を突破する鍵は「単語帳での暗記」を卒業し、「生きた時事テキストの中で語根のネットワークを広げる」学習へのシフトです。"
    },
    {
        "filename": "50-comprehensive-grand-mock-exam.md",
        "title": "1450. グランドフィナーレ：全形式統合型インドネシア語究極の実戦模試",
        "level": "技能検定B級〜特A級 / UKBI全等級（セクション34総括・実力判定）",
        "intro": "セクション34「【資格演習】検定・UKBI直前実戦模試＆徹底解説」の集大成となるグランドフィナーレです。語彙・接辞・正書法・読解・翻訳のすべての出題形式を網羅した『究極の実戦模試（全問解答・詳細論理解説付）』で、あなたの現在の総合実力を完全判定します！",
        "theory": [
            ("究極の実戦模試 構成と目標スコア",
             "1. **第1問: 語根・派生語・鼻音化判定（文法力）**\n"
             "2. **第2問: EYD第5版正書法・句読点・重複排除（正書法力）**\n"
             "3. **第3問: 政治・経済時事社説の論理読解（読解力）**\n"
             "4. **第4問: 格調高き日イ公用文翻訳（総合運用力）**\n\n"
             "※全問正解＝技能検定A級〜特A級 / UKBI Unggul〜Istimewa合格水準！")
        ],
        "problems": [
            {
                "q": "【第1問: 派生語】次の文の空所に入る正しい動詞はどれか？\n\"Pemerintah bertekad [______] birokrasi perizinan guna menarik minat investor asing.\"",
                "options": ["A. merestrukturisasi", "B. merestrukturisasikan", "C. menrestrukturisasi", "D. berstrukturisasi"],
                "ans": "A. merestrukturisasi",
                "expl": "外来語「restrukturisasi」に接頭辞 meN- が付く場合、r はそのまま残り「merestrukturisasi（〜を再編・構造改革する）」が標準形です。"
            },
            {
                "q": "【第2問: 正書法EYD 5】次の文の中で正書法上完全に正しいものはどれか？",
                "options": [
                    "A. Perjanjian kerja sama tersebut telah ditandatangani pascakonferensi pers.",
                    "B. Perjanjian kerjasama tersebut telah di tanda tangani pasca konferensi pers.",
                    "C. Perjanjian kerja-sama tersebut telah ditanda-tangani pasca-konferensi pers.",
                    "D. Perjanjian kerjasama tersebut telah ditandatangani pasca konferensi pers."
                ],
                "ans": "A. Perjanjian kerja sama tersebut telah ditandatangani pascakonferensi pers.",
                "expl": "「kerja sama（分かち書き）」「ditandatangani（接頭辞と接尾辞両方で直結）」「pascakonferensi（pasca-は直結）」のすべての基準を完全に満たしているのはAのみです。"
            },
            {
                "q": "【第3問: 読解】\n「Hukum tidak boleh tumpul ke atas dan tajam ke bawah, melainkan harus tegak lurus tanpa pandang bulu.」\nこの成句が主張している法の精神は何か？",
                "options": [
                    "A. 法は権力者や富裕層には甘く庶民に厳しいものであってはならず、何人に対しても公平平等に適用されるべきである。",
                    "B. 法律の条文は時代に合わせて常に削ったり尖らせたりして改定しなければならない。",
                    "C. 裁判官は下級裁判所での判決を尊重し、上級審での介入を避けるべきである。",
                    "D. 犯罪を取り締まる際は、まず一般庶民の刑罰を軽くして富裕層のみを処罰すべきである。"
                ],
                "ans": "A. 法は権力者や富裕層には甘く庶民に厳しいものであってはならず、何人に対しても公平平等に適用されるべきである。",
                "expl": "「tumpul ke atas, tajam ke bawah（上には鈍く、下には鋭い）」という司法批判の慣用句を否定し、「tegak lurus tanpa pandang bulu（誰に対しても差別なく直立＝公平である）」と述べているため、Aが完璧な正解です。"
            },
            {
                "q": "【第4問: 翻訳】「当社は持続可能な社会の実現に向けて、環境負荷の低減に努めてまいります。」の最も格調高いインドネシア語訳はどれか？",
                "options": [
                    "A. Perusahaan kami berkomitmen untuk mereduksi dampak lingkungan demi mewujudkan masyarakat yang berkelanjutan.",
                    "B. Perusahaan kami mau bikin dampak lingkungan jadi sedikit biar masyarakat terus berjalan.",
                    "C. Kami mencoba mengurangi efek lingkungan agar supaya masyarakat ada keberlanjutan.",
                    "D. Perusahaan kita berjanji untuk turunkan dampak alam demi masa depan yang aman."
                ],
                "ans": "A. Perusahaan kami berkomitmen untuk mereduksi dampak lingkungan demi mewujudkan masyarakat yang berkelanjutan.",
                "expl": "「berkomitmen untuk...（〜に努める・コミットする）」「mereduksi dampak lingkungan（環境負荷を低減する）」「mewujudkan masyarakat yang berkelanjutan（持続可能な社会を実現する）」という企業の公式サステナビリティ宣言の定訳が完璧です。"
            }
        ],
        "table": [
            ("merestrukturisasi", "再構築する・構造改革する（restrukturisasi）"),
            ("tumpul ke atas, tajam ke bawah", "権力者には甘く、庶民には厳しい（悪しき司法の比喩）"),
            ("tanpa pandang bulu", "えこひいきなく・差別なく・誰に対しても公平に"),
            ("mereduksi dampak", "悪影響・負荷を低減する（mengurangi）"),
            ("masyarakat berkelanjutan", "持続可能な社会（sustainable society）"),
            ("komitmen korporasi", "企業のコミットメント・確固たる約束")
        ],
        "pro_tip": "セクション34（全50記事）を読破・マスターしたあなたは、技能検定B級・A級はもちろん、最高峰特A級やUKBI最上位バンドを突破できる十分な知見と論理力を身につけました。自信を持って本番に臨んでください！"
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
    table_header = "| 項目・表現 | 解説・ニュアンス・共起表現 |\n| :--- | :--- |\n"
    if a["table"] and len(a["table"][0]) == 4:
        table_header = "| 表現A | 意味・用法 | 表現B | 意味・用法 |\n| :--- | :--- | :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} | **{row[2]}** | {row[3]} |\n"
    elif a["table"] and len(a["table"][0]) == 3:
        table_header = "| 区分・ランク | 点数・表現 | 特徴・解説 |\n| :--- | :--- |\n"
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | **{row[1]}** | {row[2]} |\n"
    else:
        for row in a["table"]:
            table_rows += f"| **{row[0]}** | {row[1]} |\n"

    md = f"""---
title: "{a['title']}"
description: "インドネシア語技能検定・UKBI対策シリーズ。{a['title']}の出題傾向、解法セオリー、実戦想定問題、詳細解説まで徹底指導。"
---

<div class="category-badge">検定・UKBI実戦対策</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 試験の傾向と出題意図

{a['intro']}

---

## 2. 攻略フレームワーク・解法セオリー

{theory_content}
---

## 3. 実戦想定問題と詳細解説

本番試験と同等レベルのオリジナル想定問題です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要語彙・構文対比テーブル

本セクションのテーマに関連する最重要語彙・成句の対比一覧です。

{table_header}{table_rows}
---

## 5. 合格者の着眼点・プロのアドバイス

> [!TIP]
> **合格のためのワンポイント・アドバイス**:
> {a['pro_tip']}

---

## 6. 次のステップ・関連リンク

- [総合サイトマップ](../sitemap.md)
- [トップページ](../index.md)
"""
    return md

def main():
    target_dir = os.path.join("docs", "exam-advanced")
    os.makedirs(target_dir, exist_ok=True)
    
    for a in articles:
        file_path = os.path.join(target_dir, a["filename"])
        content = generate_markdown(a)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
