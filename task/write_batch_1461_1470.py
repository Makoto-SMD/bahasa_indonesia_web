# -*- coding: utf-8 -*-
"""
セクション35 第2バッチ (1461-1470) 記事生成スクリプト
【表現技法】プロの翻訳・通訳・高度表現テクニック
ビジネスメール・契約書法務・財務IR・M&A・トランスクリエーション
"""

import os

articles = [
    {
        "filename": "11-business-email-translation-templates.md",
        "title": "1461. 【実務翻訳】日イビジネスメール翻訳の定型パターンと敬語表現の等価性",
        "level": "実務翻訳者・日系企業ビジネスパーソン（CEFR B2〜C1）",
        "intro": "日系企業とインドネシア企業との日々の業務連絡において、最も頻繁に発生するのがビジネスメールの翻訳です。日本語特有の謙譲・尊敬・配慮表現（「お世話になっております」「ご査収ください」「恐縮ですが」）を、インドネシア語のビジネス敬語体系（Dengan hormat, mohon berkenan, terima kasih atas kerja sama）へ等価的に変換する定型パターンを徹底網羅します。",
        "theory": [
            ("ビジネスメールの標準構造と対照表現",
             "1. **件名（Subjek）**: \n"
             "   - 「〜に関するお問い合わせ」 → Pertanyaan mengenai...\n"
             "   - 「お見積書送付の件」 → Pengiriman Surat Penawaran Harga (Quotation)\n"
             "   - 「【至急】ご確認のお願い」 → [MENDESAK] Permohonan Konfirmasi...\n"
             "2. **冒頭の宛名と挨拶**: \n"
             "   - \"Yth. Bapak/Ibu [氏名],\" + \"Semoga email ini menemui Bapak/Ibu dalam keadaan sehat dan sukses.\"\n"
             "3. **本文の導入・依頼・添付**: \n"
             "   - 「〜についてご連絡差し上げました」 → Bersama email ini, kami ingin menyampaikan bahwa...\n"
             "   - 「添付ファイルをご査収ください」 → Terlampir kami sampaikan dokumen... Mohon untuk diperiksa.\n"
             "   - 「ご多忙中恐縮ですが」 → Di tengah kesibukan Bapak/Ibu, kami mohon...\n"
             "4. **結語と署名**: \n"
             "   - \"Demikian kami sampaikan. Atas perhatian dan kerja samanya, kami ucapkan terima kasih.\" + \"Salam hormat,\"")
        ],
        "problems": [
            {
                "q": "【ビジネスメール翻訳問題】次の日本文のインドネシア語メール訳として最もプロフェッショナルで自然なものはどれか？\n「お忙しいところ恐れ入りますが、来週月曜日までに本件に関するご意見をいただけますと幸甚に存じます。」",
                "options": [
                    "A. Di sela-sela kesibukan Bapak/Ibu, kami akan sangat menghargai apabila kami dapat menerima tanggapan mengenai hal ini paling lambat hari Senin depan.",
                    "B. Bapak sibuk tapi tolong kasih komentar soal ini sampai Senin depan ya.",
                    "C. Walaupun Anda sibuk sekali, kami mau dengar suara Anda sebelum hari Senin.",
                    "D. Mohon beri pendapat hal ini pada hari Senin depan karena Bapak/Ibu tidak ada waktu."
                ],
                "ans": "A. Di sela-sela kesibukan Bapak/Ibu, kami akan sangat menghargai apabila kami dapat menerima tanggapan mengenai hal ini paling lambat hari Senin depan.",
                "expl": "「お忙しいところ（Di sela-sela kesibukan Bapak/Ibu）」「〜していただけますと幸甚に存じます（kami akan sangat menghargai apabila...）」「ご意見・ご回答（tanggapan）」という格調高いビジネス語彙を完璧に配置したAが模範です。"
            }
        ],
        "table": [
            ("Di sela-sela kesibukan Bapak/Ibu", "ご多忙中恐縮ではございますが"),
            ("Mohon berkenan untuk...", "何卒〜していただけますようお願い申し上げます"),
            ("Terlampir kami sampaikan...", "添付の通り〜をお送りいたします（ご査収ください）"),
            ("Surat Penawaran Harga (SPH)", "見積書・オファーシート（Quotation）"),
            ("Salam hormat,", "敬具・よろしくお願い申し上げます（メール末尾）"),
            ("tanggapan segera", "迅速なご回答・ご返答")
        ],
        "pro_tip": "インドネシアのビジネスメールでは、冒頭に相手の健康と成功を祈る一言（Semoga Bapak/Ibu senantiasa sehat）を添えるのが、良好な関係構築における最重要マナーです。"
    },
    {
        "filename": "12-contract-translation-whereas-clause.md",
        "title": "1462. 【契約書翻訳】契約書翻訳の基本構造：頭書・前文・合意条項の定型表現",
        "level": "実務翻訳者・法務担当者（CEFR C1〜C2）",
        "intro": "英米法およびオランダ法理の影響を色濃く残すインドネシアの契約書（Perjanjian / Kontrak）は、厳格な定型構造（頭書・当事者表示・前文Whereas条項・合意条項・末文）を持ちます。契約書の法的一貫性を担保し、誤訳による法的リスクを排除するための構造的翻訳セオリーを伝授します。",
        "theory": [
            ("インドネシア語契約書の標準5大骨格と定型句",
             "1. **標題（Judul Kontrak）**: PERJANJIAN KERJA SAMA / PERJANJIAN SEWA MENYEWA。\n"
             "2. **当事者表示（Komparisi）**: \n"
             "   - \"Perjanjian ini dibuat pada hari ini, [日付], oleh dan antara: 1. [社名], ..., selanjutnya disebut sebagai **Pihak Pertama**; dan 2. ..., selanjutnya disebut sebagai **Pihak Kedua**.\"\n"
             "3. **前文・背景（Premis / Konsiderans / Whereas Clauses）**: \n"
             "   - \"MENIMBANG BAHWA: (a) Pihak Pertama adalah perseroan terbatas yang bergerak di bidang...; (b) Pihak Kedua bermaksud untuk...; MAKA, OLEH KARENA ITU, kedua belah pihak sepakat...\"\n"
             "4. **合意事項（Batang Tubuh）**: Pasal 1 (Definisi), Pasal 2 (Ruang Lingkup), Pasal 3 (Hak dan Kewajiban)。\n"
             "5. **末文・署名（Penutup Kontrak）**: \n"
             "   - \"Demikianlah Perjanjian ini dibuat dalam rangkap 2 (dua), bermeterai cukup dan masing-masing mempunyai kekuatan hukum yang sama.\"")
        ],
        "problems": [
            {
                "q": "【契約書前文翻訳問題】契約書前文の結び定型句「よって、本契約に定める相互の約束および合意を約因として、両当事者は以下の通り合意する。」の公式インドネシア語定訳はどれか？",
                "options": [
                    "A. MAKA, OLEH KARENA ITU, dengan mempertimbangkan kesepakatan dan janji-janji timbal balik yang termaktub di sini, Para Pihak sepakat sebagai berikut:",
                    "B. Jadi sekarang kedua pihak mau janji bersama dan setuju hal-hal di bawah ini ya:",
                    "C. Karena itu orang-orang ini membuat perjanjian baru seperti yang tertulis berikut ini:",
                    "D. Maka dari itu kedua orang tersebut telah setuju isi surat ini dari nomor satu sampai selesai:"
                ],
                "ans": "A. MAKA, OLEH KARENA ITU, dengan mempertimbangkan kesepakatan dan janji-janji timbal balik yang termaktub di sini, Para Pihak sepakat sebagai berikut:",
                "expl": "英米契約書の「NOW, THEREFORE,...」に相当するインドネシア法務公用文の厳格な定型句はAの「MAKA, OLEH KARENA ITU, ... Para Pihak sepakat sebagai berikut:」です。"
            }
        ],
        "table": [
            ("oleh dan antara", "〜により、〜の間で（当事者表示）"),
            ("selanjutnya disebut sebagai...", "以下「〜」という（略称定義）"),
            ("Para Pihak", "両当事者（The Parties）"),
            ("bermeterai cukup", "十分な金額の印紙を貼付した（印紙税法準拠）"),
            ("kekuatan hukum yang sama", "同一の法的効力（equal legal force）"),
            ("rangkap dua", "2通作成（in duplicate）")
        ],
        "pro_tip": "インドネシア契約書の末文にある「bermeterai cukup（印紙添付）」は、裁判証拠能力を担保するインドネシア印紙税法（Undang-Undang Bea Meterai）上の必須要件です。"
    },
    {
        "filename": "13-contract-translation-confidentiality.md",
        "title": "1463. 【契約書翻訳】秘密保持契約（NDA）の条文対訳と専門用語解説",
        "level": "実務翻訳者・法務担当者（CEFR C1〜C2）",
        "intro": "提携交渉やM&A、共同研究の端緒で必ず締結される「秘密保持契約（Non-Disclosure Agreement: NDA / Perjanjian Kerahasiaan）」。秘密情報の定義、開示の例外事由、受領当事者の善管注意義務、残存条項などの最重要条文を日英イ対照で精密に解説します。",
        "theory": [
            ("秘密保持契約（NDA）の4大必須条項と専門定訳",
             "1. **秘密情報の定義（Definisi Informasi Rahasia）**: \n"
             "   - segala informasi teknis, finansial, operasional, atau bisnis yang diungkapkan baik secara lisan, tertulis, maupun elektronik.\n"
             "2. **秘密情報の例外（Pengecualian Informasi）**: \n"
             "   - 公知の情報（sudah menjadi domain publik）、開示前から保有していた情報（sudah diketahui secara sah sebelumnya）、独自に開発した情報（dikembangkan secara independen）。\n"
             "3. **開示先と管理義務（Kewajiban Menjaga Kerahasiaan）**: \n"
             "   - 必要最小限の開示（basis kebutuhan untuk mengetahui / need-to-know basis）、善良な管理者の注意義務（derajat kehati-hatian yang wajar）。\n"
             "4. **契約終了後の返還・破棄（Pengembalian dan Pemusnahan）**: \n"
             "   - すべての原本・複製物の返還（mengembalikan seluruh salinan dokumen）または破棄の証明（sertifikat pemusnahan）。")
        ],
        "problems": [
            {
                "q": "【NDA条文翻訳演習】「受領当事者は、秘密情報を自己の秘密情報と同等の注意義務をもって厳重に管理しなければならない。」の最も正確なインドネシア語訳はどれか？",
                "options": [
                    "A. Pihak Penerima wajib menjaga kerahasiaan Informasi Rahasia dengan derajat kehati-hatian yang sama seperti yang digunakannya untuk melindungi informasi rahasianya sendiri.",
                    "B. Pihak yang menerima harus hati-hati simpan rahasia sama seperti rahasia dia sendiri.",
                    "C. Penerima informasi wajib pegang rahasia itu biar tidak hilang seperti barangnya sendiri.",
                    "D. Pihak kedua dilarang kasih lihat rahasia pihak pertama kepada orang lain sama sekali."
                ],
                "ans": "A. Pihak Penerima wajib menjaga kerahasiaan Informasi Rahasia dengan derajat kehati-hatian yang sama seperti yang digunakannya untuk melindungi informasi rahasianya sendiri.",
                "expl": "「Pihak Penerima（受領当事者）」「wajib menjaga kerahasiaan（秘密を保持する義務を負う）」「derajat kehati-hatian（注意義務の程度・Standard of Care）」という法務契約書の定型表現を満たすのはAです。"
            }
        ],
        "table": [
            ("Pihak Pengungkap", "開示当事者（Disclosing Party）"),
            ("Pihak Penerima", "受領当事者（Receiving Party）"),
            ("derajat kehati-hatian yang wajar", "相当な注意義務（reasonable degree of care）"),
            ("domain publik", "パブリックドメイン・公知の情報"),
            ("basis kebutuhan untuk mengetahui", "知る必要性に基づく開示（need-to-know basis）"),
            ("klausul keberlanjutan", "残存条項（survival clause）")
        ],
        "pro_tip": "NDA翻訳では「Pihak Pengungkap（開示側）」と「Pihak Penerima（受領側）」の主語を取り違えると致命的な法務トラブルになります。代名詞の関係性を徹底追跡してください。"
    },
    {
        "filename": "14-contract-translation-employment.md",
        "title": "1464. 【契約書翻訳】雇用契約書・就業規則の条文対訳と労働法規語彙",
        "level": "実務翻訳者・人事労務担当者（CEFR C1〜C2）",
        "intro": "インドネシア雇用創出法（UU Cipta Kerja）および労働法（UU Ketenagakerjaan）に基づく「有期雇用契約（PKWT）」「無期雇用契約（PKWTT）」「就業規則（Peraturan Perusahaan: PP）」「解雇（PHK）」「退職手当（Pesangon）」の法規用語と翻訳定型句を完全解説します。",
        "theory": [
            ("労働法規の重要概念と契約書条文",
             "1. **雇用形態の区分**: \n"
             "   - **PKWT** (Perjanjian Kerja Waktu Tertentu): 有期雇用契約（試用期間の設置は法律上禁止）。\n"
             "   - **PKWTT** (Perjanjian Kerja Waktu Tidak Tertentu): 無期・正社員雇用契約（最大3ヶ月の試用期間: masa percobaan 可）。\n"
             "2. **賃金・手当の体系**: \n"
             "   - 基本給（upah pokok）、固定手当（tunjangan tetap）、変動手当（tunjangan tidak tetap）、宗教大祭手当（THR: Tunjangan Hari Raya Keagamaan）。\n"
             "3. **契約終了と解雇（PHK）に伴う補償金**: \n"
             "   - 解雇予告手当・退職金（uang pesangon: UP）、勤続報奨金（uang penghargaan masa kerja: UPMK）、権利補償金（uang penggantian hak: UPH）、有期雇用満了補償金（uang kompensasi PKWT）。")
        ],
        "problems": [
            {
                "q": "【労務条文翻訳問題】「会社は、社員が就業規則に定める重大な規律違反を犯した場合、書面による事前の警告なしに即時解雇することができる。」の法的に正確な訳はどれか？",
                "options": [
                    "A. Perusahaan berhak melakukan Pemutusan Hubungan Kerja (PHK) secara serta-merta tanpa surat peringatan terlebih dahulu apabila Karyawan terbukti melakukan pelanggaran berat sebagaimana diatur dalam Peraturan Perusahaan.",
                    "B. Kantor boleh pecat karyawan langsung tanpa surat peringatan kalau orang itu nakal sekali.",
                    "C. Perusahaan bisa keluarkan pegawai cepat-cepat jika ada kesalahan besar menurut aturan kantor.",
                    "D. Majikan dapat memberhentikan buruh seketika tanpa peringatan jika dia bikin ribut besar."
                ],
                "ans": "A. Perusahaan berhak melakukan Pemutusan Hubungan Kerja (PHK) secara serta-merta tanpa surat peringatan terlebih dahulu apabila Karyawan terbukti melakukan pelanggaran berat sebagaimana diatur dalam Peraturan Perusahaan.",
                "expl": "「Pemutusan Hubungan Kerja (PHK)（雇用関係の終了/解雇）」「secara serta-merta（即時に）」「surat peringatan（警告書）」「pelanggaran berat（重大な違反）」「Peraturan Perusahaan（就業規則）」という労働法の厳格な専門用語に合致しているのはAのみです。"
            }
        ],
        "table": [
            ("Perjanjian Kerja Waktu Tertentu (PKWT)", "有期雇用契約（契約社員）"),
            ("Perjanjian Kerja Waktu Tidak Tertentu (PKWTT)", "無期雇用契約（正社員）"),
            ("Tunjangan Hari Raya (THR)", "宗教大祭手当（ボーナス手当）"),
            ("uang pesangon", "退職手当・解雇補償金（severance pay）"),
            ("uang penghargaan masa kerja", "勤続功労報奨金（service pay）"),
            ("masa percobaan", "試用期間（最大3ヶ月）")
        ],
        "pro_tip": "「PHK」は単なるクビ（pemecatan）ではなく、自己都合退職、定年退職、契約満了、懲戒解雇を含む「雇用関係終了全般」を指す包括的な法律概念です。"
    },
    {
        "filename": "15-contract-translation-sales-agency.md",
        "title": "1465. 【契約書翻訳】売買基本契約・販売代理店契約の条文対訳",
        "level": "実務翻訳者・国際法務担当者（CEFR C1〜C2）",
        "intro": "日イ二国間貿易や現地販売網構築で締結される「売買基本契約（Master Sales Agreement: Perjanjian Jual Beli）」および「総販売代理店契約（Sole Distributor Agreement: Perjanjian Distributor Tunggal）」。インコタームズ（Incoterms）、危険負担の移転、独占権（Hak Eksklusif）、品質保証条項の定訳ルールを解説します。",
        "theory": [
            ("販売・代理店契約の重要条項と対訳",
             "1. **引渡条件と危険負担の移転（Pengiriman dan Peralihan Risiko）**: \n"
             "   - \"Penyerahan Barang dilakukan berdasarkan ketentuan FOB Pelabuhan Tanjung Priok (Incoterms 2020), di mana risiko kerusakan atau kehilangan barang beralih dari Penjual kepada Pembeli pada saat barang melewati pagar kapal.\"\n"
             "2. **独占販売権（Hak Eksklusif）**: \n"
             "   - 指定地域（Wilayah Tertentu）、最小購入目標（Target Pembelian Minimum / Minimum Purchase Target）。\n"
             "3. **瑕疵担保責任・品質保証（Jaminan Kualitas dan Klaim Cacat）**: \n"
             "   - 隠れたる瑕疵（cacat tersembunyi）、検査期間（periode pemeriksaan）。\n"
             "4. **不可抗力条項（Keadaan Kahar / Force Majeure）**: \n"
             "   - 地震、津波、暴動、政府規制による義務免除。")
        ],
        "problems": [
            {
                "q": "【売買契約翻訳問題】「買主は、商品受領後7営業日以内に検査を実施し、隠れたる瑕疵を発見した場合は直ちに売主に書面で通知しなければならない。」の的確なインドネシア語訳はどれか？",
                "options": [
                    "A. Pembeli wajib melakukan pemeriksaan dalam jangka waktu 7 hari kerja setelah penerimaan Barang dan segera memberitahukan secara tertulis kepada Penjual apabila ditemukan adanya cacat tersembunyi.",
                    "B. Pembeli harus cek barang 7 hari kerja setelah barang datang dan kasih surat ke Penjual kalau barangnya rusak sembunyi.",
                    "C. Pembeli mesti periksa barang dalam 7 hari dan bilang pada penjual jika ada cacat yang tidak kelihatan.",
                    "D. Kalau ada cacat tersembunyi, Pembeli menulis surat kepada Penjual setelah periksa selama 7 hari."
                ],
                "ans": "A. Pembeli wajib melakukan pemeriksaan dalam jangka waktu 7 hari kerja setelah penerimaan Barang dan segera memberitahukan secara tertulis kepada Penjual apabila ditemukan adanya cacat tersembunyi.",
                "expl": "「jangka waktu 7 hari kerja（7営業日の期間）」「penerimaan Barang（商品の受領）」「memberitahukan secara tertulis（書面により通知する）」「cacat tersembunyi（隠れたる瑕疵）」という商取引約款の定型訳が整ったAが正解です。"
            }
        ],
        "table": [
            ("Distributor Tunggal", "総代理店・独占販売代理店（Sole Distributor）"),
            ("peralihan risiko", "危険負担の移転（transfer of risk）"),
            ("cacat tersembunyi", "隠れたる瑕疵・潜在的欠陥（latent defects）"),
            ("keadaan kahar", "不可抗力（Force Majeure）"),
            ("target pembelian minimum", "最低購入保証数量・ノルマ"),
            ("ganti rugi wanprestasi", "債務不履行損害賠償")
        ],
        "pro_tip": "契約書中の「瑕疵（欠陥）」は単なる rusak ではなく、「cacat」を用います。特に隠れた欠陥は「cacat tersembunyi」が確立された民法上の法務用語です。"
    },
    {
        "filename": "16-legal-memorandum-translation.md",
        "title": "1466. 【法務翻訳】法務意見書（Legal Opinion）の翻訳：論理展開と格調の維持",
        "level": "実務翻訳者・渉外弁護士・パラリーガル（CEFR C1〜C2）",
        "intro": "大手法律事務所がクライアント向けに起草する「法務意見書（Legal Opinion / Pendapat Hukum）」は、事実関係の整理、関係法令の解釈、法的リスクの分析、および推奨アクションを論理整合性高く提示する最高峰の法的文書です。その格調高い論理展開（IRAC手法）を崩さずに翻訳する技術を解説します。",
        "theory": [
            ("法務意見書（Pendapat Hukum）のIRAC構造と定型表現",
             "1. **事実関係（Fakta-Fakta Hukum / Facts）**: \n"
             "   - \"Berdasarkan kronologi yang disampaikan oleh Klien...\"（クライアントより提示された経緯に基づき…）\n"
             "2. **争点・論点（Isu Hukum / Issues）**: \n"
             "   - \"Isu hukum utama yang perlu dianalisis adalah apakah transaksi tersebut melanggar ketentuan...\"（分析すべき主たる法的論点は〜であるか否かである）\n"
             "3. **法的根拠と分析（Dasar Hukum & Analisis / Rules & Analysis）**: \n"
             "   - 関連法令の条項引用（Merujuk pada Pasal...）、最高裁判所判例（Yurisprudensi Mahkamah Agung）。\n"
             "4. **結論と助言（Kesimpulan & Rekomendasi / Conclusion）**: \n"
             "   - \"Dapat disimpulkan bahwa risiko kepatuhan hukum relatif rendah, sepanjang Klien memenuhi kewajiban...\"（〜を満たす限りにおいて、コンプライアンスリスクは比較的軽微であると結論づけられる）")
        ],
        "problems": [
            {
                "q": "【法務意見書翻訳問題】「現行法に照らし、本取引が独占禁止法上の不当な取引制限に該当するリスクは極めて低いと判断される。」の最も格調高いインドネシア語訳はどれか？",
                "options": [
                    "A. Berdasarkan hukum yang berlaku, kami berpendapat bahwa risiko transaksi ini dikualifikasikan sebagai praktik monopoli yang dilarang adalah sangat kecil.",
                    "B. Menurut hukum sekarang, transaksi ini tidak ada risiko monopoli sama sekali.",
                    "C. Hukum melihat bahwa bisnis ini tidak mungkin salah aturan monopoli dagang.",
                    "D. Sesuai undang-undang, kami rasa bahaya transaksi ini jadi monopoli itu rendah banget."
                ],
                "ans": "A. Berdasarkan hukum yang berlaku, kami berpendapat bahwa risiko transaksi ini dikualifikasikan sebagai praktik monopoli yang dilarang adalah sangat kecil.",
                "expl": "「kami berpendapat bahwa...（〜と判断/意見する）」「dikualifikasikan sebagai...（〜として法的に位置づけられる/該当する）」「praktik monopoli yang dilarang（禁止される独占的慣行）」という法律事務所の正式な意見書文体が整っているAが正解です。"
            }
        ],
        "table": [
            ("pendapat hukum", "法務意見書・法的見解（Legal Opinion）"),
            ("kronologi fakta", "事実の時系列・経緯"),
            ("yurisprudensi", "最高裁判所判例・判例法（case law）"),
            ("dikualifikasikan sebagai...", "〜として法的に位置づけられる・該当する"),
            ("mitigasi risiko hukum", "法的リスクの軽減・回避措置"),
            ("sepanjang memenuhi...", "〜を満たす限りにおいて（条件制限）")
        ],
        "pro_tip": "法務意見書の翻訳では、「断定的な表現（Pasti melanggar）」を避け、「kami berpandangan bahwa（〜という見解をとる）」「berpotensi ditafsirkan sebagai（〜と解釈される潜在的リスクがある）」という慎重な留保表現（hedging）を正確に訳出することが鉄則です。"
    },
    {
        "filename": "17-financial-statement-translation.md",
        "title": "1467. 【財務翻訳】財務諸表（貸借対照表・損益計算書）の用語対訳と注記の翻訳",
        "level": "実務翻訳者・公認会計士・経理財務担当（CEFR C1〜C2）",
        "intro": "インドネシア会計基準（PSAK / SAK: Standar Akuntansi Keuangan）および国際財務報告基準（IFRS）に完全準拠した「財政状態計算書（Neraca / Laporan Posisi Keuangan）」「包括利益計算書（Laporan Laba Rugi dan Penghasilan Komprehensif Lain）」、および会計方針注記（Catatan atas Laporan Keuangan）の財務対訳を体系的に解説します。",
        "theory": [
            ("財務諸表主要科目の日英イ対照表",
             "1. **資産の部（Aset / Assets）**: \n"
             "   - 流動資産（Aset Lancar）: 現金及び現金同等物（Kas dan Setara Kas）、売掛金（Piutang Usaha）、棚卸資産（Persediaan）。\n"
             "   - 非流動資産（Aset Tidak Lancar）: 有形固定資産（Aset Tetap）、減価償却累計額（Akumulasi Penyusutan）、のれん（Goodwill）。\n"
             "2. **負債及び純資産の部（Liabilitas & Ekuitas / Liabilities & Equity）**: \n"
             "   - 流動負債（Liabilitas Jangka Pendek）: 買掛金（Utang Usaha）、短期借入金（Pinjaman Jangka Pendek）。\n"
             "   - 固定負債（Liabilitas Jangka Panjang）: 社債（Obligasi）、退職給付引当金（Liabilitas Imbalan Kerja）。\n"
             "   - 資本（Ekuitas）: 資本金（Modal Saham）、利益剰余金（Saldo Laba / Retained Earnings）。\n"
             "3. **損益計算書科目（Laba Rugi）**: \n"
             "   - 売上高（Pendapatan / Penjualan Bersih）、売上原価（Beban Pokok Pendapatan）、売上総利益（Laba Bruto）、営業利益（Laba Usaha / Operasional）、当期純利益（Laba Bersih Tahun Berjalan）。")
        ],
        "problems": [
            {
                "q": "【財務諸表対訳問題】インドネシアの決算書における「Beban Pokok Pendapatan」に相当する日本の会計用語はどれか？",
                "options": ["A. 売上原価（Cost of Goods Sold）", "B. 販管費（Selling & Administrative Expenses）", "C. 営業外費用（Non-operating Expenses）", "D. 特別損失（Extraordinary Loss）"],
                "ans": "A. 売上原価（Cost of Goods Sold）",
                "expl": "「Beban Pokok Pendapatan」または「Beban Pokok Penjualan」は、商品やサービスの提供に直接かかった原価である「売上原価（Cost of Sales / COGS）」の正式な会計基準用語です。"
            }
        ],
        "table": [
            ("Laporan Posisi Keuangan", "財政状態計算書・貸借対照表（Balance Sheet）"),
            ("Laporan Laba Rugi", "損益計算書（Income Statement）"),
            ("piutang usaha", "売掛金・受取手形（Accounts Receivable）"),
            ("utang usaha", "買掛金・支払手形（Accounts Payable）"),
            ("beban pokok pendapatan", "売上原価（Cost of Sales）"),
            ("laba bersih tahun berjalan", "当期純利益（Net Profit for the Year）")
        ],
        "pro_tip": "インドネシアの最新会計基準（PSAK）では、「Neraca」という呼称よりも「Laporan Posisi Keuangan（財政状態計算書）」というIFRS直訳の正式名称が有価証券報告書で義務付けられています。"
    },
    {
        "filename": "18-investor-relations-ir-translation.md",
        "title": "1468. 【IR翻訳】決算説明会資料・アニュアルレポートの翻訳：投資家向け洗練表現",
        "level": "実務翻訳者・IR広報担当者（CEFR C1〜C2）",
        "intro": "機関投資家やアナリストを対象とする「アニュアルレポート（Laporan Tahunan）」や「決算説明プレゼン資料（Materi Paparan Publik）」は、客観的な財務数値だけでなく、企業の成長ストーリー、ESG（環境・社会・ガバナンス）への取り組み、および将来展望を格調高くアピールする洗練された言語運用が要求されます。",
        "theory": [
            ("IR・経営メッセージの頻出構文と定訳",
             "1. **業績ハイライト（Sorotan Kinerja）**: \n"
             "   - 前年同期比15%増（tumbuh 15 persen secara tahunan / YoY: Year-on-Year）。\n"
             "   - 過去最高益を達成（membukukan rekor laba bersih tertinggi sepanjang sejarah）。\n"
             "2. **コーポレート・ガバナンスとESG**: \n"
             "   - 企業統治の原則（Tata Kelola Perusahaan yang Baik: GCG - Transparansi, Akuntabilitas, Responsibilitas, Independensi, Kewajaran）。\n"
             "   - 脱炭素化への道筋（peta jalan dekarbonisasi / transisi menuju net zero emission）。\n"
             "3. **将来展望と経営陣の抱負（Prospek Usaha & Pandangan Manajemen）**: \n"
             "   - 逆風を乗り越えて強靭な成長を実現する（mengatasi tantangan dan mempertahankan pertumbuhan yang resilien）。")
        ],
        "problems": [
            {
                "q": "【IR経営メッセージ翻訳問題】「当社は厳しい市場環境にもかかわらず、過去最高の売上高と営業利益を達成いたしました。」の最も洗練された投資家向けインドネシア語訳はどれか？",
                "options": [
                    "A. Kendati menghadapi lingkungan pasar yang penuh tantangan, Perusahaan berhasil membukukan rekor pendapatan dan laba usaha tertinggi sepanjang sejarah.",
                    "B. Walaupun pasar susah sekali, perusahaan kami dapat untung paling banyak dalam sejarah.",
                    "C. Di depan pasar yang tidak enak, kami berhasil bikin uang banyak sekali dibanding tahun lalu.",
                    "D. Biar kata ekonomi lagi macet, perusahaan kita untungnya meloncat rekor."
                ],
                "ans": "A. Kendati menghadapi lingkungan pasar yang penuh tantangan, Perusahaan berhasil membukukan rekor pendapatan dan laba usaha tertinggi sepanjang sejarah.",
                "expl": "「Kendati menghadapi... yang penuh tantangan（厳しい環境にもかかわらず）」「membukukan rekor... tertinggi sepanjang sejarah（過去最高記録を計上・達成した）」というIR報告書の洗練された語彙が完璧です。"
            }
        ],
        "table": [
            ("membukukan rekor laba", "過去最高益を計上・達成する"),
            ("secara tahunan (YoY)", "前年同期比で（Year-on-Year）"),
            ("Tata Kelola Perusahaan yang Baik (GCG)", "コーポレートガバナンス（Good Corporate Governance）"),
            ("pertumbuhan yang resilien", "強靭な成長・レジリエントな拡大"),
            ("peta jalan dekarbonisasi", "脱炭素化ロードマップ"),
            ("paparan publik (public expose)", "機関投資家向け決算説明会")
        ],
        "pro_tip": "財務数値の「計上する・記録する」には、単なる mencatat ではなく、会計用語の「membukukan（帳簿に計上する）」を用いるとプロのIR翻訳に仕上がります。"
    },
    {
        "filename": "19-m-and-a-due-diligence-translation.md",
        "title": "1469. 【M&A翻訳】M&Aデューデリジェンス報告書の翻訳：リスク評価と企業価値算定",
        "level": "実務翻訳者・投資銀行・M&Aアドバイザリー（CEFR C1〜C2）",
        "intro": "クロスボーダーM&A（企業の合併・買収）において、買収対象会社の買収監査を行う「デューデリジェンス報告書（Laporan Uji Tuntas: Legal, Financial, Tax DD）」。偶発債務（kewajiban kontinjensi）、許認可の継続性（keberlanjutan perizinan）、チェンジオブコントロール条項（perubahan kendali）など、高度な専門リスク評価文言の翻訳技術を詳述します。",
        "theory": [
            ("M&Aデューデリジェンス報告書の最重要キーワード",
             "1. **法務DD（Uji Tuntas Hukum: LDD）の頻出リスク**: \n"
             "   - 許認可の不備・失効（ketidakpatuhan / kedaluwarsanya izin usaha）。\n"
             "   - 経営権変更条項（klausul perubahan pengendalian / Change of Control: CoC）による契約解除リスク。\n"
             "   - 係争中の訴訟・潜在的訴訟リスク（perkara litigasi yang sedang berjalan / potensi sengketa hukum）。\n"
             "2. **財務・税務DD（FDD & TDD）の頻出論点**: \n"
             "   - 簿外債務・偶発債務（liabilitas tidak tercatat / liabilitas kontinjensi）。\n"
             "   - 未納税額および追徴課税リスク（surat ketetapan pajak kurang bayar: SKPKB）。\n"
             "   - EBITDAの正常化調整（normalisasi EBITDA）。")
        ],
        "problems": [
            {
                "q": "【M&A法務DD翻訳演習】「対象会社が保有する主要な鉱山採掘許可（IUP）は、環境アセスメント（AMDAL）の更新義務不履行により、行政処分による取消リスクを孕んでいる。」の的確なインドネシア語訳はどれか？",
                "options": [
                    "A. Izin Usaha Pertambangan (IUP) utama milik Perusahaan Target rentan terhadap risiko pencabutan administratif akibat kelalaian dalam memperbarui AMDAL.",
                    "B. Izin tambang perusahaan itu bisa dicabut oleh pemerintah karena AMDAL belum diurus.",
                    "C. Perusahaan target punya izin tambang yang bahaya dibatalkan gara-gara lupa bikin AMDAL baru.",
                    "D. Izin IUP yang penting milik target akan hilang sebab aturan AMDAL tidak jalan lancar."
                ],
                "ans": "A. Izin Usaha Pertambangan (IUP) utama milik Perusahaan Target rentan terhadap risiko pencabutan administratif akibat kelalaian dalam memperbarui AMDAL.",
                "expl": "「Perusahaan Target（買収対象会社）」「rentan terhadap risiko...（〜のリスクに対して脆弱である・孕んでいる）」「pencabutan administratif（行政処分による取消）」「kelalaian memperbarui AMDAL（環境アセスメント更新義務の懈怠・不履行）」というDDレポートの厳密な法務定訳を満たしています。"
            }
        ],
        "table": [
            ("uji tuntas (due diligence)", "デューデリジェンス・買収監査"),
            ("perusahaan target", "買収対象会社（Target Company）"),
            ("liabilitas kontinjensi", "偶発債務（contingent liabilities）"),
            ("perubahan kendali (Change of Control)", "経営権の変更・支配権移転"),
            ("pencabutan izin", "許認可の取消・剥奪"),
            ("kelalaian administratif", "行政手続上の不作為・懈怠")
        ],
        "pro_tip": "DD報告書における「Red Flag（致命的リスク）」の訳出では、リスクの程度（Tinggi, Sedang, Rendah）と法的根拠法令を明確に紐付けて訳出することが、ディール担当者の迅速な判断を助けます。"
    },
    {
        "filename": "20-marketing-copywriting-transcreation.md",
        "title": "1470. 【マーケティング翻訳】広告・キャッチコピーのトランスクリエーション：心に響く現地化",
        "level": "クリエイティブ翻訳者・マーケター（CEFR B2〜C1）",
        "intro": "製品のキャッチコピー、CMスローガン、SNSマーケティング文案を直訳すると、意味は通じても「現地の消費者の感情にまったく刺さらない死んだ言葉」になります。言葉を機械的に翻訳するのではなく、文化的背景、感情のトリガー、音の心地よさを再構築するクリエイティブ翻訳手法『トランスクリエーション（Transkreasi）』の真髄を伝授します。",
        "theory": [
            ("トランスクリエーション（Transkreasi）の3大黄金原則",
             "1. **感情のコア（Emotional Core）を掴み、言葉を捨てる**: \n"
             "   - 日本語の文字面を直訳するのではなく、「消費者にどんな感情（安心、優越感、ワクワク、温かさ）を抱かせたいのか」を特定する。\n"
             "2. **音の響きとリズム感（Rima & Aliterasi）の創出**: \n"
             "   - インドネシア語では、語尾の母音の一致（韻: rima）や頭韻（aliterasi）がキャッチコピーの浸透力を決定的に左右する。\n"
             "3. **文化的価値観（Nilai Budaya）への適合**: \n"
             "   - 個人の自己実現よりも「家族との絆（keluarga）」「団らん（kebersamaan）」「祝福（berkah）」を訴求する文脈が強い共感を呼ぶ。")
        ],
        "problems": [
            {
                "q": "【キャッチコピートランスクリエーション問題】日本の自動車メーカーのファミリー向けSUVのキャッチコピー「家族の笑顔を、もっと遠くへ。」を、インドネシアの消費者の心に最も響くようトランスクリエーション（クリエイティブ現地化）したものはどれか？",
                "options": [
                    "A. \"Merajut Kebersamaan, Menjelajah Lebih Jauh.\"（家族の団らんを紡ぎ、さらに遠くへ旅立とう）",
                    "B. \"Membawa senyum keluarga pergi ke tempat yang lebih jauh.\"（直訳：家族の笑顔をより遠い場所へ持っていく）",
                    "C. \"Mobil ini bikin seluruh anggota keluarga tersenyum sampai jauh.\"（口語直訳：この車は家族全員を遠くまで笑顔にさせる）",
                    "D. \"Senyuman keluarga dipindahkan dengan jarak jauh oleh mobil ini.\"（受動直訳：家族の笑顔がこの車で長距離移動される）"
                ],
                "ans": "A. \"Merajut Kebersamaan, Menjelajah Lebih Jauh.\"（家族の団らんを紡ぎ、さらに遠くへ旅立とう）",
                "expl": "B, C, Dは日本語の直訳で極めて不自然ですが、Aはインドネシア人が最も愛する「kebersamaan（団らん・絆）」を「merajut（紡ぐ・織りなす）」と美しく表現し、頭韻（Merajut... Menjelajah...）を効かせた見事なトランスクリエーションです。"
            }
        ],
        "table": [
            ("transkreasi", "トランスクリエーション（創造的翻訳・クリエイティブ現地化）"),
            ("merajut kebersamaan", "家族の団らん・絆を紡ぎ出す（定番の感動コピー）"),
            ("rima dan ritme", "韻律とリズム（広告コピーの生命線）"),
            ("daya pikat emosional", "感情的な訴求力・アピール度"),
            ("slogan iklan", "広告スローガン・キャッチコピー"),
            ("relevansi budaya", "文化的関連性・現地適合性")
        ],
        "pro_tip": "マーケティング翻訳では、クライアントに対して「直訳」と「トランスクリエーション案（現地での受容理由の解説付）」を複数提示するのが、一流のプロ翻訳者の仕事術です。"
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

<div class="category-badge">プロフェッショナル実務翻訳</div>

# {a['title']}

<div class="article-meta">
  <span class="meta-item"><i class="fas fa-clock"></i> 読了目安: 15分</span>
  <span class="meta-item"><i class="fas fa-graduation-cap"></i> 対象レベル: {a['level']}</span>
</div>

---

## 1. 実務領域の課題と背景

{a['intro']}

---

## 2. プロの翻訳ストラテジー・対比フレームワーク

{theory_content}
---

## 3. 実戦翻訳比較演習

実務の現場で通用する正確無比なプロの訳文を練り上げる実戦演習です。選択肢を吟味して解答した後、アコーディオンを開いて論理的解説を確認してください。

{problem_items}
---

## 4. 重要専門用語・条文対比テーブル

本講のテーマに関連する重要専門用語・公用表現一覧です。

{table_header}{table_rows}
---

## 5. プロ翻訳者の着眼点・ワンポイントアドバイス

> [!TIP]
> **実務翻訳の現場で役立つワンポイント・アドバイス**:
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
