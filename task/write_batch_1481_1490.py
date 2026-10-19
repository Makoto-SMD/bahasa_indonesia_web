# -*- coding: utf-8 -*-
"""
セクション35 第4バッチ (1481-1490) 記事生成スクリプト
【表現技法】プロの翻訳・通訳・高度表現テクニック
会議通訳・アクティブリスニング・視訳・危機管理・ウィスパリング・RSI・現場通訳
"""

import os

articles = [
    {
        "filename": "31-interpreting-active-listening.md",
        "title": "1481. 【通訳技術】通訳者のためのアクティブリスニング：文の終わりを待たずに意味を予測する",
        "level": "プロ通訳者・会議通訳志望者（CEFR C1〜C2）",
        "intro": "通訳者における「聴く（Mendengarkan）」という行為は、一般の受動的リスニングとは根本的に異なります。話し手が次に何を言おうとしているのか、構文の骨格、談話標識（Signpost words）、イントネーションから瞬時に後続展開を予測（Prediksi Makna）しながら聴く『アクティブリスニング（Mendengarkan Aktif）』の認知プロセスを解明します。",
        "theory": [
            ("プロ通訳者の3大予測トリガー",
             "1. **文頭接続詞による論理予測**: \n"
             "   - \"Kendati demikian,...\" を聴いた瞬間 → 「前文を否定・制限する自論が来る」と予測。\n"
             "   - \"Bukan hanya...\" を聴いた瞬間 → 「必ず melainkan juga が後ろに控えている」と構文を予測。\n"
             "2. **述語動詞の項構造（Valency）からの予測**: \n"
             "   - \"Pemerintah mewajibkan...\" を聴いた瞬間 → 「［誰に］［何をすることを］という2つの補語が必ず来る」と予測して待ち構える。\n"
             "3. **プロソディ（韻律・声のトーン）の知覚**: \n"
             "   - 声のピッチが上がって一呼吸置いた時 → 「次の重要なポイントや具体例が提示される」と察知する。")
        ],
        "problems": [
            {
                "q": "【通訳予測演習】話者が「Sehubungan dengan fluktuasi nilai tukar yang kian tajam, dewan direksi memandang perlu untuk...」と発話した。通訳者が瞬時に予測すべき後続の動詞句の方向性として最も自然なものはどれか？",
                "options": [
                    "A. 為替リスクを回避・ヘッジするための緊急対策（mitigasi risiko / lindung nilai）。",
                    "B. 工場の従業員全員にボーナスを一律支給する決定。",
                    "C. 来年度の新入社員採用人数を倍増させる計画。",
                    "D. 社屋の壁のペンキを塗り直すスケジュール。"
                ],
                "ans": "A. 為替リスクを回避・ヘッジするための緊急対策（mitigasi risiko / lindung nilai）。",
                "expl": "「為替相場の激しい変動に鑑み（Sehubungan dengan fluktuasi nilai tukar...）」＋「取締役会は〜が必要であると判断した（dewan direksi memandang perlu untuk...）」というビジネス文脈から、直後に来るのは「為替ヘッジ（lindung nilai / hedging）」や「リスク軽減策（mitigasi risiko）」であると0.1秒で先回り予測するのがプロのリスニングです。"
            }
        ],
        "table": [
            ("prediksi makna", "意味の予測・先回り知覚（anticipation）"),
            ("mendengarkan aktif", "アクティブリスニング・能動的傾聴"),
            ("penanda wacana", "談話標識・論理マーカー（Signpost words）"),
            ("lindung nilai (hedging)", "為替ヘッジ・リスク回避取引"),
            ("fluktuasi nilai tukar", "為替レートの乱高下・変動"),
            ("beban kognitif", "認知負荷（Cognitive Load）")
        ],
        "pro_tip": "話し手の言葉を「1語ずつ受動的に待つ」のではなく、「次に来るはずの単語を心の中で先回りして迎えに行く」感覚を持つと、通訳時の脳の疲労が激減します。"
    },
    {
        "filename": "32-interpreting-reformulation-skills.md",
        "title": "1482. 【通訳技術】通訳におけるリフォーミュレーション：直訳の呪縛を解き放つ要約・再構成",
        "level": "プロ通訳者・会議通訳志望者（CEFR C1〜C2）",
        "intro": "通訳現場で最も初学者が陥る罠が「話し手の言葉を一語一句直訳しようとして文末で破綻する現象」です。プロの通訳者は、原発話の言語的殻を脱ぎ捨て（脱言語化）、その核となるメッセージ（Message Core）を保ったまま、訳出先言語の自然な構文へと柔軟に再構成（Reformulasi）します。その具体的再構成メソッドを伝授します。",
        "theory": [
            ("リフォーミュレーション（再構成）の3大テクニック",
             "1. **長大な複文のスライシング（Slicing / Chunking）**: \n"
             "   - 長い1つの文を、関係詞や接続詞の切れ目で「2つまたは3つの短い独立文」に切断して訳出する。\n"
             "2. **名詞句の動詞化・動詞句の名詞化（Transposisi）**: \n"
             "   - 日: 「コスト削減の実現に向けた取り組みの強化が必要である。」\n"
             "   - イ: \"Kita harus memangkas biaya secara agresif.\"（名詞の羅列を簡潔なS-V-Oに変換）。\n"
             "3. **冗長表現のシェイプアップ（Pruning / Trimming）**: \n"
             "   - 「〜というふうに思われるところでございますが」のような日本語の挨拶クッションを削ぎ落とし、核（esensi）だけをストレートに届ける。")
        ],
        "problems": [
            {
                "q": "【リフォーミュレーション演習】日本の役員が「えー、当工場の生産効率の抜本的改善を図るべく、最新鋭の自動化ロボットアームの導入を決定いたしました次第であります。」と発話した。通訳として最も切れ味鋭いインドネシア語訳出はどれか？",
                "options": [
                    "A. \"Kami memutuskan untuk memasang lengan robot otomatis tercanggih demi mendongkrak efisiensi pabrik secara drastis.\"",
                    "B. \"Eh... untuk gambar perbaikan efisiensi produksi pabrik kami, maka ada keputusan pasang robot yang baru sekali menurut ceritanya.\"",
                    "C. \"Pabrik kita mau bikin bagus efisiensi jadi pimpinan sudah setuju beli tangan robot otomatis sekarang.\"",
                    "D. \"Karena kami ingin coba efisiensi, maka robot yang paling baru diputuskan masuk ke dalam pabrik ini.\""
                ],
                "ans": "A. \"Kami memutuskan untuk memasang lengan robot otomatis tercanggih demi mendongkrak efisiensi pabrik secara drastis.\"",
                "expl": "日本語の冗長な文末表現を削ぎ落とし、「Kami memutuskan untuk memasang...（〜の導入を決定した）」＋「demi mendongkrak efisiensi...（効率を劇的に押し上げるため）」と力強いS-V-Oに再構成したAがプロフェッショナルな訳出です。"
            }
        ],
        "table": [
            ("reformulasi kalimat", "文の再構成・リフォーミュレーション"),
            ("mendongkrak efisiensi", "効率を大幅に引き上げる・押し上げる"),
            ("lengan robot otomatis", "自動化ロボットアーム"),
            ("pemenggalan kalimat (slicing)", "長文の文分割・スライシング"),
            ("esensi pesan", "メッセージの核心・本質"),
            ("deverbalisasi", "脱言語化（意味の純粋概念化）")
        ],
        "pro_tip": "通訳の目的は「単語の変換」ではなく「話し手の意図が聞き手に100%誤解なく伝わること」です。言葉に忠実であるより、メッセージの意図に忠実であってください。"
    },
    {
        "filename": "33-interpreting-memory-retention.md",
        "title": "1483. 【通訳技術】通訳者の短期記憶トレーニング：シャドーイングとリプロダクション",
        "level": "プロ通訳者・上級学習者（CEFR B2〜C2）",
        "intro": "逐次通訳で話者が30秒〜1分間話している間、ノートを取りつつ内容を脳内に保持するためには強靭な「短期記憶・作業記憶（Working Memory）」が必須です。脳の認知的キャパシティを劇的に拡張し、記憶の脱落（Memory Loss）を防ぐための『プロ式シャドーイング』と『リプロダクション（再生演習）』の科学的トレーニング法を公開します。",
        "theory": [
            ("記憶保持力を鍛える3段階エクスサイズ",
             "1. **プロディレイ・シャドーイング（Delayed Shadowing）**: \n"
             "   - 音声の直後ではなく、あえて「3〜4語遅れ（2〜3秒遅れ）」で音声を影のように追唱する。常に数語分の音声を脳内バッファに溜める負荷をかける。\n"
             "2. **キーファクト・リプロダクション（Fact Reproduction）**: \n"
             "   - メモを取らずに2〜3文のインドネシア語ニュースを聴き、主語、動詞、数字、固有名詞の事実関係だけを即座に同じ言語（インドネシア語）で復元して発話する。\n"
             "3. **イメージ・マッピング法（Mental Visualization）**: \n"
             "   - 単語を文字列として覚えるのではなく、話者の語るストーリーを頭の中で「動画・絵」として映画のスクリーンに映し出すように記憶する。")
        ],
        "problems": [
            {
                "q": "【リテンション・数字保持問題】音声で「Kuartal lalu, volume ekspor nikel olahan mencapai 450 ribu ton senilai 1,2 miliar dolar AS, naik 15 persen dibanding tahun sebelumnya.」と流れた。保持すべき中核ファクトの組み合わせとして最も正確なものはどれか？",
                "options": [
                    "A. ニッケル加工品輸出: 45万トン / 12億米ドル / 15%増",
                    "B. ニッケル鉱石輸出: 450万トン / 120億米ドル / 50%増",
                    "C. 銅加工品輸出: 4万5千トン / 1.2兆ルピア / 15%減",
                    "D. 原油輸出: 45万バレル / 12億ドル / 1.5%増"
                ],
                "ans": "A. ニッケル加工品輸出: 45万トン / 12億米ドル / 15%増",
                "expl": "450 ribu ton（45万トン）、1,2 miliar dolar AS（12億ドル）、naik 15 persen（15%増）という重要数値を正確に保持できているのはAです。"
            }
        ],
        "table": [
            ("retensi memori", "記憶の保持・リテンション"),
            ("shadowing berjarak (delayed)", "ディレイ・シャドーイング（数語遅れの追唱）"),
            ("reproduksi teks", "テキストの再現・リプロダクション"),
            ("visualisasi mental", "頭の中での情景映像化（メンタルイメージ）"),
            ("kapasitas memori kerja", "作業記憶（ワーキングメモリ）容量"),
            ("nikel olahan", "ニッケル加工品（スメルター精錬品）")
        ],
        "pro_tip": "数字が連続して登場した時は、頭で覚えようとせず、右手でノートに即座にアラビア数字だけを縦に書き殴ってください。数字はメモに任せ、脳は論理の追跡に専念させるのが鉄則です。"
    },
    {
        "filename": "34-interpreting-sight-translation.md",
        "title": "1484. 【通訳技術】サイトトランスレーション（視訳）訓練法：頭から瞬時に日本語化する技術",
        "level": "プロ通訳者・会議通訳志望者（CEFR C1〜C2）",
        "intro": "サイトトランスレーション（視訳: Sight Translation）とは、目の前の外国語文書を目で追いながら、後戻りせず先頭から流れるような母国語へ瞬時に口頭訳出する技術です。同時通訳の基礎体力を養う最強のトレーニング法であり、国際会議の配布資料や契約書をその場で読み聞かせる実務現場で必須となる視訳の極意を解説します。",
        "theory": [
            ("サイトトランスレーションを可能にする3大チャンキング技法",
             "1. **左から右への順送り訳出（Linear Translation）**: \n"
             "   - 返り読み（後戻り）は絶対禁止。意味のまとまり（チャンク: 3〜5語）ごとに区切り、「〜であり、〜のために、〜となった」と順送りに日本語を繋ぐ。\n"
             "2. **関係代名詞 yang の「主語化・継続用法」処理**: \n"
             "   - yang を見たら後ろから修飾せず、「〜である。そしてその〜は…」と前の名詞をもう一度受けて文を展開する。\n"
             "3. **スラッシュ・リーディングの自動化**: \n"
             "   - [Pemerintah RI / telah menandatangani kesepakatan / dengan pihak investor // yang berkomitmen / untuk menanamkan modal sebesar 10 triliun rupiah.]")
        ],
        "problems": [
            {
                "q": "【視訳チャンキング演習】次の文を先頭から順送りに視訳した日本語として、返り読みを排した最も自然でテンポの良い口頭訳出はどれか？\n\"Kementerian ESDM meluncurkan program transisi energi / yang bertujuan mengurangi emisi karbon / sekaligus menciptakan lapangan kerja hijau / bagi generasi muda di daerah perdesaan.\"",
                "options": [
                    "A. 「エネルギー鉱物資源省はエネルギー転換プログラムを開始しました。／このプログラムは炭素排出量の削減を目指すとともに、／地方の若者たちに向けた、／環境に優しいグリーンな雇用を創出するものです。」",
                    "B. 「地方の若者のグリーンな雇用を作りながら炭素を減らすことを目指すエネルギー転換プログラムをエネルギー省が始めた。」",
                    "C. 「若者のために仕事を作って炭素も減らす目的のプログラムが地方でエネルギー省から出された。」",
                    "D. 「エネルギー省はプログラムをやったが、これは炭素を減らす若者の仕事である。」"
                ],
                "ans": "A. 「エネルギー鉱物資源省はエネルギー転換プログラムを開始しました。／このプログラムは炭素排出量の削減を目指すとともに、／地方の若者たちに向けた、／環境に優しいグリーンな雇用を創出するものです。」",
                "expl": "文を4つのスラッシュで区切り、前の文から流れるように順送りに訳出しているAがサイトトランスレーションの完璧な模範です。Bのように文末から返り読みすると同時通訳のスピードに追いつけません。"
            }
        ],
        "table": [
            ("terjemahan sekilas (sight translation)", "サイトトランスレーション・視訳"),
            ("pemenggalan frasa (chunking)", "フレーズの区切り・チャンキング"),
            ("alur berpikir linear", "直線的思考フロー・順送り思考"),
            ("lapangan kerja hijau", "グリーンジョブ・環境関連雇用"),
            ("emisi karbon", "炭素排出量（二酸化炭素排出）"),
            ("Kementerian ESDM", "エネルギー鉱物資源省")
        ],
        "pro_tip": "視訳の練習をする際は、自分の訳出音声を録音し、「えー」「あのー」という言い淀みがなく、ニュースアナウンサーのように滑らかに日本語が流れているかを確認してください。"
    },
    {
        "filename": "35-interpreting-crisis-management.md",
        "title": "1485. 【通訳技術】通訳現場のトラブル対処法：聞き逃し・専門用語不明時のスマートリカバリー",
        "level": "プロ通訳者・実務通訳者（CEFR C1〜C2）",
        "intro": "どれほど経験を積んだプロ通訳者であっても、「音響トラブルで声が聞き取れなかった」「未知の専門略語が登場した」「早口すぎて数字を取りこぼした」という危機的状況は必ず発生します。パニックに陥ってフリーズすることなく、エレガントに聞き返し（Klarifikasi）、文脈から安全にリカバリーするプロの危機管理プロトコルを伝授します。",
        "theory": [
            ("通訳現場のトラブル別リカバリー・プロトコル",
             "1. **完全に聞き取れなかった時（音声不良・雑音） → 即座の丁寧な確認**: \n"
             "   - 会議を止めずにスマートに促す: \"Mohon maaf, suara Bapak sempat terputus. Bisakah diulangi angka terakhir?\"（恐れ入ります、少々お声が途切れました。最後の数字をもう一度お願いできますでしょうか？）\n"
             "2. **未知の専門用語・略語が登場した時 → 概念的パラフレーズ**: \n"
             "   - 単語を捏造せず、前後の文脈から「〜に関する制度／〜の装置」と上位概念（kategori umum）で安全に着地させる。\n"
             "3. **自分が言い間違えた時 → 堂々とした即時訂正**: \n"
             "   - 取り乱さず、落ち着いたトーンで「Maksud saya, 15 triliun rupiah.（失礼いたしました、15兆ルピアでございます）」と訂正して進める。")
        ],
        "problems": [
            {
                "q": "【現場トラブルシミュレーション】大臣のスピーチ中、会場のマイクが一瞬ハウリングを起こし、肝心な政策目標の年号（tahun target）が聞き取れなかった。通訳者として取るべき最も適切な行動はどれか？",
                "options": [
                    "A. 発言終了直後、礼儀正しく「Mohon izin Bapak Menteri, untuk tahun target program tersebut tadi tertutup dengung mikrofon, apakah tahun 2030?」と事実確認を行い、正確な年号を訳出する。",
                    "B. 聞こえなかったふりをして、年号の部分を完全に省いて通訳を終わらせる。",
                    "C. 自分の勘で「おそらく2030年だろう」と推測してそのまま通訳する。",
                    "D. その場でマイクを叩いて音響スタッフに向かって怒鳴る。"
                ],
                "ans": "A. 発言終了直後、礼儀正しく「Mohon izin Bapak Menteri, untuk tahun target program tersebut tadi tertutup dengung mikrofon, apakah tahun 2030?」と事実確認を行い、正確な年号を訳出する。",
                "expl": "数字や年号の誤訳・捏造は政策決定において致命的です。音響トラブルという客観的理由を添えて礼儀正しく確認を求めるAが、クライアントから最も信頼されるプロの立ち振る舞いです。"
            }
        ],
        "table": [
            ("manajemen krisis", "危機管理・トラブルシューティング"),
            ("klarifikasi yang santun", "礼儀正しい確認・聞き返し"),
            ("suara terputus", "音声の途切れ・通信障害"),
            ("dengung mikrofon", "マイクのハウリング・異音"),
            ("koreksi mandiri", "自己訂正（Self-correction）"),
            ("kategori umum", "上位概念・包括的カテゴリー")
        ],
        "pro_tip": "通訳者が最も嫌われるのは「聞き取れなかったのに適当にでっち上げる（mengarang-ngarang）」ことです。堂々と1回確認できる通訳者こそが本物のプロフェッショナルです。"
    },
    {
        "filename": "36-interpreting-whispering-techniques.md",
        "title": "1486. 【通訳技術】ウィスパリング通訳の作法：小声で明瞭に伝える発声と距離感",
        "level": "プロ通訳者・ビジネスアテンド通訳（CEFR C1〜C2）",
        "intro": "専用ブースや音響設備のない役員会議、工場視察、法廷、ディナーの席で、特定クライアントの耳元で小声で同時通訳を行う「ウィスパリング（Chuchotage / Bisik-bisik）」。会議の進行を妨げず、クライアントの耳を疲れさせず、かつ自分自身の声帯を守るためのポジショニング、無声音発声、距離感の作法を解説します。",
        "theory": [
            ("ウィスパリング通訳の3大プロフェッショナル作法",
             "1. **適切な物理的ポジショニング（Duduk / Berdiri）**: \n"
             "   - クライアントの斜め後方45度、耳から30〜40cmの距離が黄金位置。真正面から話しかけたり、耳元に息を吹きかけるのは厳禁。\n"
             "2. **無声音を主体とした腹式発声（Vokal Tanpa Desah）**: \n"
             "   - 単なる「ヒソヒソ声（息混じり声）」は摩擦音が強く耳障りで喉を痛める。声帯をあまり振動させず、子音の輪郭（アーティキュレーション）を口先で明瞭に発音する。\n"
             "3. **パナガイド（携帯型送信機）の活用**: \n"
             "   - 聞き手が2名以上の場合は、ピンマイクと小型送信機（Infoport / Panaguide）を用いて通常の静かな声で発話する。")
        ],
        "problems": [
            {
                "q": "【ウィスパリング作法問題】重要顧客の隣でウィスパリング通訳を行う際、マナーおよび身体技法として最も適切なものはどれか？",
                "options": [
                    "A. クライアントの利き耳側の斜め後ろに位置取り、息が直接耳にかからないよう配慮しつつ、子音を明瞭に発音して静かに語りかける。",
                    "B. 相手の耳に口を密着させて、できる限り大きな息を吹き込みながらヒソヒソ声で話す。",
                    "C. 会議室の全員に聞こえるように、通常のプレゼンテーションと同じ大声で話す。",
                    "D. クライアントの前に立ちふさがって、相手の視界を遮りながら通訳する。"
                ],
                "ans": "A. クライアントの利き耳側の斜め後ろに位置取り、息が直接耳にかからないよう配慮しつつ、子音を明瞭に発音して静かに語りかける。",
                "expl": "クライアントのパーソナルスペースを尊重し、息を吹きかけず、子音の明瞭度を高めて疲労を与えないAがウィスパリングの基本作法です。"
            }
        ],
        "table": [
            ("chuchotage (bisik-bisik)", "ウィスパリング通訳・耳元通訳"),
            ("artikulasi konsonan", "子音の調音・明瞭な発音"),
            ("sudut 45 derajat", "斜め45度の位置取り"),
            ("perangkat pemancar nirkabel", "ワイヤレス送信機（パナガイド）"),
            ("kelelahan pita suara", "声帯の疲労"),
            ("ruang pribadi (personal space)", "パーソナルスペース・適切な対人距離")
        ],
        "pro_tip": "ウィスパリングを長時間（30分以上）1人で続けると、通常の発声よりも急速に喉が渇き疲弊します。常温の水を手元に用意し、小まめに喉を潤してください。"
    },
    {
        "filename": "37-interpreting-remote-rsi-mastery.md",
        "title": "1487. 【通訳技術】リモート同時通訳（RSI）の留意点：音響環境・チャット連携・交代ルール",
        "level": "プロ通訳者・会議通訳者（CEFR C1〜C2）",
        "intro": "パンデミック以降、国際会議の標準となった「リモート同時通訳（Remote Simultaneous Interpreting: RSI / Zoom, Kudo, Interprefy）」。現場ブースとは異なる特有の課題（音声のレイテンシ、急な回線切断、パートナーとの非対面連携）を克服し、自宅やリモートハブから完璧なパフォーマンスを発揮するためのRSIプロトコルを体系化します。",
        "theory": [
            ("RSI成功のための3大インフラ＆連携ルール",
             "1. **絶対的な有線接続と機材環境（Infrastruktur Hardwire）**: \n"
             "   - Wi-Fiは厳禁。LANケーブル直結の光回線、単一指向性コンデンサーマイク、密閉型モニターヘッドホンが必須要件。\n"
             "2. **裏チャット（Backchannel）によるパートナー連携**: \n"
             "   - WhatsAppやSlackに通訳ペア専用の裏チャンネルを開設。\n"
             "   - 数字、固有名詞、略語の瞬時共有（例: 「IKN=Nusantara」「$12M=120億ドル」とパートナーが即座に打ち込んで助け合う）。\n"
             "3. **交代プロトコル（Handover Rule）**: \n"
             "   - 15〜20分ごとの厳格な交代。交代の2分前に「2 menit lagi siap?」「OK, siap di slide berikutnya」と合図し、発話の句切れでスムーズにマイク権限をバトンタッチする。")
        ],
        "problems": [
            {
                "q": "【RSI連携問題】自分がZoom同時通訳を担当中、パートナーが裏チャットに「BI-Rate 6,25% (naik 25 bps)」と打ち込んでくれた。この時、自分が取るべき最もプロフェッショナルな対応はどれか？",
                "options": [
                    "A. チャット画面を一瞥して数字を確認し、音声通訳の中で「インドネシア銀行は政策金利を0.25%引き上げ、6.25%としました」と滑らかに訳出に反映させる。",
                    "B. 通訳を中断して「チャットありがとう！」とマイクに向かって叫ぶ。",
                    "C. パートナーのチャットを無視して、自分の聞き取った不確かな数字を話す。",
                    "D. Zoomの全体チャットに「パートナーからメモが来ました」と書き込む。"
                ],
                "ans": "A. チャット画面を一瞥して数字を確認し、音声通訳の中で「インドネシア銀行は政策金利を0.25%引き上げ、6.25%としました」と滑らかに訳出に反映させる。",
                "expl": "同時通訳はペア（2名）によるチーム戦です。パートナーがアシストしてくれた重要数字を即座に視覚で拾い、何事もなかったかのように滑らかに発話に組み込むAが最高峰のチームプレイです。"
            }
        ],
        "table": [
            ("Remote Simultaneous Interpreting (RSI)", "リモート同時通訳（遠隔同通）"),
            ("saluran komunikasi cadangan (backchannel)", "裏連絡チャット（WhatsApp等）"),
            ("pergantian giliran (handover)", "通訳交代（通常15〜20分間隔）"),
            ("latensi audio", "音声遅延・レイテンシ"),
            ("koneksi kabel LAN (hardwire)", "有線LAN接続"),
            ("mikrofon kondensor terarah", "単一指向性マイク")
        ],
        "pro_tip": "RSIでは、自分がマイクオフ（Mute）の時こそがパートナーへの貢献のチャンスです。登場した固有名詞や数字を裏チャットに即座にタイピングして相方をサポートしてください。"
    },
    {
        "filename": "38-interpreting-business-negotiation.md",
        "title": "1488. 【通訳技術】タフな価格交渉・紛争解決の場での通訳：中立性と信頼感の演出",
        "level": "実務通訳者・ビジネス交渉担当（CEFR C1〜C2）",
        "intro": "M&Aの価格交渉、納期の遅延補償、合弁解消の泥沼交渉など、双方が感情的になり鋭い対立が生じる修羅場のビジネス交渉。通訳者が一方の感情に引きずられたり、勝手な意訳を挟むと交渉は一瞬で決裂します。絶対的な中立性（Netralitas）を保ち、場の緊張を沈静化させて合意へ導くプロの通訳技法を学びます。",
        "theory": [
            ("タフネゴシエーションにおける通訳者の3大行動規範",
             "1. **感情のデトックスとトーンの適正化（Detoksifikasi Emosi）**: \n"
             "   - 日本側の役員が激昂して「ふざけるな！そんな条件飲めるわけがないだろう！」と言った時、そのまま怒鳴り返さず、\"Pihak kami menegaskan bahwa persyaratan tersebut sama sekali tidak dapat kami terima.\" と極めて冷静かつ断固とした公式トーンで訳出する。\n"
             "2. **絶対的中立の身体言語（Bahasa Tubuh Netral）**: \n"
             "   - どちらか一方の当事者だけに顔を向けたり、頷き続けたりしない。両陣営の中心に位置し、公平な視線配分（Eye Contact）を保つ。\n"
             "3. **個人的意見の表明の完全封殺**: \n"
             "   - クライアントから「どう思います？」と小声で聞かれても、「通訳者の職責として、ご助言は差し控えさせていただきます」と中立の立場を崩さない。")
        ],
        "problems": [
            {
                "q": "【交渉通訳演習】インドネシア側の交渉相手が早口で激しく不満を述べ立てている。通訳者としての最適な対応はどれか？",
                "options": [
                    "A. 相手の興奮に巻き込まれず、冷静に相手の目を見て要点をメモし、相手の主張する論拠と条件を客観的・論理的な日本語で淡々と日本側に伝える。",
                    "B. 相手を睨みつけて「落ち着いて話してください！」と怒鳴りつける。",
                    "C. 日本側に「相手がなんか怒ってますけど無視していいです」と勝手に要約する。",
                    "D. 怖くなって泣き出し、部屋から逃げ出す。"
                ],
                "ans": "A. 相手の興奮に巻き込まれず、冷静に相手の目を見て要点をメモし、相手の主張する論拠と条件を客観的・論理的な日本語で淡々と日本側に伝える。",
                "expl": "交渉現場で最も求められるのは通訳者の「揺るぎない冷静沈着さ（Ketenangan）」です。感情を濾過し、主張の骨格だけを客観的に伝えるAがプロの鑑です。"
            }
        ],
        "table": [
            ("netralitas mutlak", "絶対的中立性（Absolute Neutrality）"),
            ("negosiasi alot", "タフな交渉・難航する協議"),
            ("detoksifikasi emosi", "感情の解毒・トーンの沈静化"),
            ("titik temu (kompromi)", "妥協点・着地点（Common Ground）"),
            ("bahasa tubuh yang tenang", "落ち着いたボディーランゲージ"),
            ("kerahasiaan tingkat tinggi", "高度な守秘義務")
        ],
        "pro_tip": "緊迫した交渉の場では、通訳者の声のトーン（低めで安定したピッチ）が、両陣営のヒートアップした感情をクールダウンさせる心理的アンカーになります。"
    },
    {
        "filename": "39-interpreting-factory-site-visit.md",
        "title": "1489. 【通訳技術】工場見学・製造現場での通訳：騒音対策・安全配慮と工程用語",
        "level": "実務通訳者・製造業アテンド（CEFR B2〜C1）",
        "intro": "自動車工場、製鉄所、食品加工ラインなどの現場アテンド通訳は、会議室とは全く異なる過酷な環境（機械の爆音、粉塵、熱気、危険区域）で行われます。安全第一の立ち回り（K3準拠）、騒音下で声を届ける発声法、および製造ライン特有の工程用語の通訳ノウハウを徹底解説します。",
        "theory": [
            ("製造現場通訳の3大必須ルール",
             "1. **安全最優先の所作（K3 / Safety First）**: \n"
             "   - ヘルメット、安全靴、保護メガネの着用。\n"
             "   - 黄色の安全通路（jalur pejalan kaki hijau/kuning）から絶対にはみ出さない。稼働中の機械やフォークリフトに背を向けない。\n"
             "2. **騒音下での通訳技法（Voice Projection）**: \n"
             "   - 大声で叫ぶと声が枯れる。無線ガイドシステム（Tour Guide System）の活用、または耳元で低音を響かせて話す。\n"
             "3. **製造現場の頻出カイゼン用語**: \n"
             "   - 歩留まり（yield / rasio hasil baik）、チョコ停（chocotei / berhenti singkat）、ポカヨケ（poka-yoke / pencegah kesalahan）、段取り替え（pergantian cetakan/alat）。")
        ],
        "problems": [
            {
                "q": "【現場通訳問題】工場長が「プレス工程でのチョコ停を削減するため、金型の段取り替え時間を半減させるカイゼン活動を進めています。」と説明した。的確な通訳訳出はどれか？",
                "options": [
                    "A. \"Untuk mengurangi henti singkat (chocotei) pada proses pengepresan, kami menjalankan aktivitas kaizen untuk memangkas separuh waktu pergantian cetakan (dies).\"",
                    "B. \"Biar mesin tidak berhenti makan cokelat, kami ganti cetakan besi cepat-cepat dua kali.\"",
                    "C. \"Pabrik press mau kurangi macet kecil jadi kita perbaiki waktu bikin ganti barang.\"",
                    "D. \"Supaya proses tekan jalan terus, waktu ganti alat dibikin pendek lima puluh persen.\""
                ],
                "ans": "A. \"Untuk mengurangi henti singkat (chocotei) pada proses pengepresan, kami menjalankan aktivitas kaizen untuk memangkas separuh waktu pergantian cetakan (dies).\"",
                "expl": "「チョコ停（henti singkat / chocotei）」「プレス工程（proses pengepresan）」「金型の段取り替え（pergantian cetakan / dies）」「半減させる（memangkas separuh waktu）」という製造業の専門用語が的確に反映されているAが正解です。"
            }
        ],
        "table": [
            ("proses pengepresan", "プレス工程（Stamping / Pressing）"),
            ("pergantian cetakan (dies)", "金型交換・段取り替え"),
            ("henti singkat (chocotei)", "チョコ停（短時間の設備停止）"),
            ("rasio hasil baik (yield)", "歩留まり・良品率"),
            ("jalur keselamatan", "安全通路（歩行者専用レーン）"),
            ("alat pelindung diri (APD)", "個人用保護具（ヘルメット・安全靴）")
        ],
        "pro_tip": "工場見学では、通訳者が夢中になってメモを取るあまりフォークリフトの進路に立ち入ってしまう事故が最も危険です。現場ではメモ帳を閉じ、周囲の安全に五感を研ぎ澄ましてください。"
    },
    {
        "filename": "40-interpreting-medical-escort.md",
        "title": "1490. 【通訳技術】医療通訳・患者アテンド：問診票・インフォームドコンセントと心理ケア",
        "level": "医療通訳者・国際病院アテンド（CEFR C1〜C2）",
        "intro": "インドネシア人患者の日本での高度医療受診、または在留邦人の現地総合病院（Siloam, Pondok Indah, Medistra等）受診を支援する「医療通訳（Penerjemahan Medis）」。問診票の記入、病状の聴取、医師からのインフォームド・コンセント（説明と同意）、および不安を抱える患者への心理的ケアの作法を伝授します。",
        "theory": [
            ("医療通訳の3大プロフェッショナル原則",
             "1. **解剖学・症状表現の精密な聴取（Anamnesis）**: \n"
             "   - 痛みの性質の識別: ズキズキ（nyeri berdenyut）、キリキリ・差し込む痛み（nyeri melilit）、チクチク（nyeri menusuk）、重苦しい痛み（pegal / linu）。\n"
             "2. **インフォームド・コンセントの完全性（Informed Consent）**: \n"
             "   - 手術のリスク、合併症（komplikasi）、代替治療法（terapi alternatif）を過不足なく患者に母国語で理解させ、自由意思に基づく同意書への署名を支援する。\n"
             "3. **感情的共感と医療倫理の調和**: \n"
             "   - 不安がる患者の心に寄り添いつつも、勝手な医学的判断や気休めの予断（「大丈夫ですよ、すぐ治ります」等）は口にしない。")
        ],
        "problems": [
            {
                "q": "【医療問診通訳問題】患者が「昨日の夜から、胃がキリキリと差し込むように痛んで、冷や汗が出ます。」と訴えた。医師への正確なインドネシア語訳出（または現地医師への説明）はどれか？",
                "options": [
                    "A. \"Sejak kemarin malam, perut bagian atas saya terasa nyeri melilit yang tajam dan disertai keringat dingin.\"",
                    "B. \"Perut saya sakit sekali kemarin malam dan ada air keluar dari kulit saya.\"",
                    "C. \"Tadi malam perut saya rusak seperti dipotong dan badan saya dingin sekali.\"",
                    "D. \"Lambung saya menangis sejak semalam dan keluar keringat es banyak.\""
                ],
                "ans": "A. \"Sejak kemarin malam, perut bagian atas saya terasa nyeri melilit yang tajam dan disertai keringat dingin.\"",
                "expl": "「キリキリ差し込む痛み」を「nyeri melilit yang tajam（内臓が捻れるような鋭い痛み）」と正確に医学表現化し、「冷や汗（keringat dingin）」を適切に結びつけたAが医療通訳の模範です。"
            }
        ],
        "table": [
            ("nyeri melilit", "キリキリ・差し込むような腹痛（colicky pain）"),
            ("nyeri berdenyut", "ズキズキする脈打つ痛み（throbbing pain）"),
            ("keringat dingin", "冷や汗（cold sweat）"),
            ("persetujuan tindakan medis (Informed Consent)", "インフォームドコンセント・侵襲的医療行為への同意"),
            ("komplikasi pasca-operasi", "術後合併症"),
            ("riwayat alergi obat", "薬物アレルギー歴")
        ],
        "pro_tip": "医療通訳では、患者が医師の前で遠慮して症状を控えめに言ってしまう傾向があります。患者の「実は…」という微細な呟きを絶対に聞き漏らさず医師に伝えることが命を救います。"
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
description: "プロの翻訳・通訳・高度表現テクニック。{a['title']}の実務分析、通訳ストラテジー、実戦比較演習まで徹底指導。"
---

<div class="category-badge">実践通訳技術・プロトコル</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 専門領域の課題と認知プロセス

{a['intro']}

---

## 2. プロ通訳者の思考法・トレーニングフレームワーク

{theory_content}
---

## 3. 実戦通訳シミュレーション演習

実務の現場で直面するリアルな対話・スピーチを完璧に通訳する実戦演習です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要通訳用語・状況対応テーブル

本講のテーマに関連する重要通訳用語・現場対応表現一覧です。

{table_header}{table_rows}
---

## 5. プロ通訳者の着眼点・ワンポイントアドバイス

> [!TIP]
> **通訳現場で役立つワンポイント・アドバイス**:
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
