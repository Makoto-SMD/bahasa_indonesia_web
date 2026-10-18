# B43: 移転価格税制（Transfer Pricing / TP Doc）と関連当事者間取引

日本本社の親会社や海外グループ子会社との間で原材料の購入、完成品の輸出、ロイヤルティ（Royalti）の支払い、役務提供（Management Service Fees）、親子間ローン（Intra-Group Loan）を行う日系多国籍企業にとって、税務当局（DJP）の最大のターゲットとなるのが**移転価格税制（Penetapan Harga Transfer / Transfer Pricing）**です。

財務大臣規則（PMK No. 213/2016 および PMK No. 172/2023）に基づき、一定規模以上の関連当事者間取引（**Transaksi Hubungan Istimewa**）を行う企業には、**独立企業間原則（Arm's Length Principle / Prinsip Kewajaran dan Kelaziman Usaha - PKKU）**に従っていることを証明する**移転価格文書（Dokumen Penentuan Harga Transfer: TP Doc）**の作成・保管が厳格に義務付けられています。

本記事では、3層構造文書（ローカルファイル、マスターファイル、国別報告書 CbCR）、移転価格算定手法（TNM法、再販売価格基準法、原価加算法等）、利益率比較分析（ベンチマーク分析）、事前確認制度（APA: Advance Pricing Agreement）に関する実務インドネシア語を体系的に解説します。

---

## 1. 移転価格税制に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Harga Transfer (Transfer Pricing - TP)** | 移転価格 | 資本関係や支配関係のあるグループ関連会社間で行われる取引価格 |
| **Hubungan Istimewa (Related Party)** | 特殊関係・関連当事者 | 株式保有25%以上、または役員兼任・実質的支配関係にある企業関係 |
| **Prinsip Kewajaran dan Kelaziman Usaha (PKKU)** | 独立企業間原則 (Arm's Length Principle) | 関連会社間取引であっても、独立した第三者間取引と同様の適正価格・利益水準で行うべき大原則 |
| **TP Doc (Dokumen Penentuan Harga Transfer)** | 移転価格文書 (TP Doc) | ローカルファイル（Dokumen Lokal）およびマスターファイル（Dokumen Induk）の総称 |
| **Dokumen Lokal (Local File)** | ローカルファイル | 現地法人の事業概要、関連当事者間取引の詳細、経済分析・利益率検証を記載した文書 |
| **Dokumen Induk (Master File)** | マスターファイル | 多国籍企業グループ全体のグローバルな組織構造、無形資産、財務活動をまとめた文書 |
| **Laporan per Negara (CbCR - Country-by-Country)** | 国別報告書 (CbCR) | 連結売上11兆ルピア超の巨大多国籍企業が提出する各国別の売上・利益・納税額一覧表 |
| **Metode TNMM (Metode Laba Bersih Transaksional)** | 取引単位営業利益法 (TNMM) | 比較可能な独立企業の営業利益率（Operating Margin / Full Cost Mark-up）と比較する最も一般的な算定手法 |
| **Studi Pembanding (Benchmarking Study)** | ベンチマーク分析・比較可能性分析 | 財務データベース（Orbis, Osiris等）から独立第三者企業を抽出し、適正利益レンジを導く分析 |
| **Rentang Kewajaran (Arm's Length Range)** | 独立企業間レンジ（四分位範囲 / IQR） | 比較可能企業の利益率の中央値を中心とする適正な範囲（第1四分位数〜第3四分位数） |
| **APA (Kesepakatan Harga Transfer / Advance Pricing Agreement)** | 事前確認制度 (APA) | 納税者と税務当局（二国間APAでは日本国税庁とDJP）があらかじめ移転価格の算定基準を合意する制度 |

---

## 2. 現場実践対話 (Percakapan Praktis Transfer Pricing)

### 場面1: 日本本社へのロイヤルティ（Royalti）支払いの経済的利益（Benefit Test）立証協議

日系製造法人の財務ディレクターと国際税務コンサルタントが、日本親会社へ支払っている売上高3%の技術ライセンス・商標使用料（Royalti）に対する税務調査防衛を検討する場面です。

:::id-example
**Tax Partner (Bambang)**: Selamat pagi, Pak Tanaka. Menjelang batas akhir penyusunan Dokumen Penentuan Harga Transfer (TP Doc) tahun ini, kami ingin membedah pos pembayaran royalti sebesar 15 miliar rupiah ke kantor pusat Anda di Tokyo.  
**Finance Director (Tanaka)**: Selamat pagi, Pak Bambang. Pembayaran royalti 3 persen tersebut didasarkan pada Perjanjian Lisensi Teknologi (*Technology Licensing Agreement*) untuk penggunaan paten dan merek dagang kami. Bukankah tarif 3 persen sudah sangat lazim di industri manufaktur otomotif?  
**Tax Partner (Bambang)**: Secara tarif mungkin wajar. Namun, sesuai Peraturan Menteri Keuangan PMK Nomor 172 Tahun 2023, pemeriksa pajak di Indonesia menerapkan pembuktian bertingkat yang sangat ketat untuk transaksi aset tak berwujud (intangible property), yaitu *Uji Keberadaan (Existence Test)* dan *Uji Manfaat Ekonomi (Economic Benefit Test)*.  
**Finance Director (Tanaka)**: Apa yang diminta pemeriksa untuk membuktikan uji manfaat ekonomi tersebut?  
**Tax Partner (Bambang)**: Pemeriksa tidak akan puas hanya dengan melihat selembar kontrak lisensi. Mereka meminta bukti dokumentasi nyata: apakah ada panduan teknis yang dikirim dari Tokyo? Berapa kali insinyur Jepang datang memberikan pelatihan ke pabrik Cikarang? Dan bagaimana merek tersebut berkontribusi terhadap kenaikan harga jual produk kita di pasar Indonesia?  
**Finance Director (Tanaka)**: Kami memiliki ratusan lembar cetak biru teknik (*blueprint*), laporan kunjungan teknis berkala, dan data riset pasar yang membuktikan bahwa pelanggan Indonesia bersedia membayar harga premium karena kepercayaan terhadap merek Jepang kami.  
**Tax Partner (Bambang)**: Luar biasa! Seluruh bukti konkret tersebut wajib kita lampirkan secara komprehensif ke dalam Dokumen Lokal (Local File). Dengan begitu, pemeriksa pajak tidak bisa mendiskualifikasi biaya royalti tersebut sebagai dividen terselubung (*hidden dividend*).
:::

- **transaksi aset tak berwujud**: 無形資産取引（特許権、商標権、ノウハウ）
- **uji manfaat ekonomi (benefit test)**: 経済的利益テスト（対価に見合う実質的便益があったかの検証）
- **cetak biru teknik (blueprint)**: 技術青写真・設計図面
- **dividen terselubung (hidden dividend)**: 認定配当・偽装配当（損金否認されて配当とみなされること）

---

### 場面2: ベンチマーク分析による営業利益率の四分位範囲（Interquartile Range）検証

現地法人の営業利益率が2.5%であり、独立第三者企業のベンチマーク調査結果と比較して適正レンジに入っているかを確認する場面です。

:::id-example
**TP Specialist (Lina)**: Pak Tanaka, kami telah menyelesaikan studi pembanding (benchmarking study) menggunakan basis data keuangan perusahaan manufaktur independen di kawasan Asia Tenggara untuk menguji metode TNMM kita.  
**Finance Director (Tanaka)**: Bagaimana posisi margin laba operasi (*operating margin*) pabrik kita tahun ini dibandingkan dengan rentang kewajaran (*arm's length range*)?  
**TP Specialist (Lina)**: Margin laba operasi aktual kita tahun ini tercatat 2,8 persen. Dari hasil pencarian terhadap 15 perusahaan pembanding independen, rentang interkuartil (Interquartile Range - IQR) berada pada angka: Kuartil Bawah (Q1) 1,9 persen, Nilai Tengah (Median) 3,1 persen, dan Kuartil Atas (Q3) 4,8 persen.  
**Finance Director (Tanaka)**: Berarti angka 2,8 persen kita berada di dalam rentang kewajaran antara Q1 dan Q3?  
**TP Specialist (Lina)**: Betul sekali, Pak. Karena berada di atas Q1 (1,9 persen), secara teknis posisi harga transfer kita telah memenuhi Prinsip Kewajaran dan Kelaziman Usaha (PKKU). DJP tidak berhak melakukan penyesuaian laba (primary adjustment) secara sepihak.  
**Finance Director (Tanaka)**: Sangat melegakan. Pastikan Ikhtisar Dokumen Penentuan Harga Transfer (Lampiran 3A/3B SPT 1771) sudah diisi lengkap dan dicentang bahwa Dokumen Lokal dan Dokumen Induk telah tersedia tepat waktu sebelum SPT dilaporkan.
:::

- **rentang interkuartil (Interquartile Range - IQR)**: 四分位範囲（下位25%〜上位25%を除外した適正中央帯）
- **penyesuaian laba sepihak (primary adjustment)**: 税務署による一方的な利益修正・所得加算処分
- **Ikhtisar Dokumen Penentuan Harga Transfer**: 移転価格文書サマリー（確定申告書の必須別表）

---

## 3. 移転価格実務で頻出する実務構文集

### 文書化義務・作成基準

- **Dokumen Lokal dan Dokumen Induk wajib tersedia paling lambat empat bulan setelah akhir tahun pajak.**  
  （ローカルファイルおよびマスターファイルは事業年度終了後最長4ヶ月以内に備え置く義務があります。）
- **Wajib Pajak wajib menyerahkan TP Doc dalam waktu maksimal satu bulan setelah diminta oleh pemeriksa pajak.**  
  （納税者は税務調査官から要求された場合、最長1ヶ月以内に移転価格文書を提出する義務があります。）
- **Transaksi dengan pihak yang memiliki hubungan istimewa wajib memenuhi prinsip kelaziman usaha.**  
  （特殊関係者との取引は独立企業間原則を満たさなければなりません。）

### 利益率分析・調査防衛

- **Metode Transaksi Laba Bersih (TNMM) dipilih sebagai metode yang paling tepat untuk menguji margin pabrikan.**  
  （製造受託者の利益率を検証するため、最も適切な手法として取引単位営業利益法（TNMM）が選定されました。）
- **Lampirkan analisis fungsional (Fungsi, Aset, dan Risiko - FAR) secara rinci dalam Dokumen Lokal.**  
  （ローカルファイル内に詳細な機能・資産・リスク分析（FAR分析）を添付してください。）

---

> [!IMPORTANT]
> **「TP Docは後から作れない（Harus Tersedia Tepat Waktu）」**  
> インドネシア税法（PMK 172/2023）では、TP Docは確定申告書の提出期限（4月末）までに**「既に完成して社内に保管されていること（Tersedia）」**が法定義務とされています。確定申告書の別表で「備え置き済み」にチェックを入れたにもかかわらず、税務調査時に提出期限（30日）以内に提出できなかった場合、**「TP Docが存在しなかった」とみなされ、莫大な無申告加算税と税務署による一方的な推計課税**が科されます。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 資本関係25%以上などのグループ関連会社間取引において、独立した第三者間と同様の適正価格で取引すべき大原則を何と呼ぶでしょう？</summary>

1. Prinsip Kewajaran dan Kelaziman Usaha (Arm's Length Principle)  
2. Prinsip Monopoli Usaha  
3. Prinsip Bagi Rata  

**正解: 1**  
**解説**: 移転価格の大原則は「独立企業間原則（Prinsip Kewajaran dan Kelaziman Usaha - PKKU / Arm's Length Principle）」です。
</details>

<details class="id-quiz">
<summary>Q2. 移転価格文書（TP Doc）の構成要素のうち、現地法人の詳細な取引や経済分析（ベンチマーク分析）を記載する文書は？</summary>

1. Dokumen Lokal (Local File)  
2. Dokumen Induk (Master File)  
3. Surat Jalan  

**正解: 1**  
**解説**: 各法人の具体的取引や利益率分析を詳述する文書は「Dokumen Lokal（ローカルファイル）」です。
</details>
