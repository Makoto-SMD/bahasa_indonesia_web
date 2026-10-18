# B41: 法人所得税（PPh Badan）確定申告と源泉徴収税（PPh 21/23/4(2)）実務

インドネシアで法人事業（PT PMA等）を営む企業にとって、財務省税務総局（**Direktorat Jenderal Pajak - DJP**）が管轄する税制へのコンプライアンスは、税務調査（Audit Pajak / Pemeriksaan Pajak）に伴う追徴課税（SKP）や重加算金を防ぐための最重要財務実務です。

企業は年次で**法人所得税確定申告書（SPT Tahunan PPh Badan: Formulir 1771）**を提出するだけでなく、毎月の月次申告として、個人所得税源泉徴収（**PPh Pasal 21**）、サービス対価・レンタル料等の源泉徴収（**PPh Pasal 23**）、土地建物賃貸や建設業等の最終分離課税（**PPh Pasal 4 ayat 2**）、および翌年度法人税の前払予納（**PPh Pasal 25**）を遅滞なく処理しなければなりません。

本記事では、損金算入・不算入（Koreksi Fiskal Positif/Negatif）、源泉徴収票（Bukti Potong）、オンライン納税（e-Billing / DJP Online）、税務調査通知（SP2）に関する実務インドネシア語を体系的に解説します。

---

## 1. 税務申告・源泉徴収に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **PPh Badan (Pajak Penghasilan Badan)** | 法人所得税 | 企業の課税所得に対して課される税金（現行基本税率：22%） |
| **SPT Tahunan PPh Badan (Formulir 1771)** | 年次法人税確定申告書 | 事業年度終了後4ヶ月以内（通常4月末日まで）に提出する年次申告書 |
| **SPT Masa (Monthly Tax Return)** | 月次税務申告書 | 毎月10日〜20日の法定納付・申告期限に提出する源泉税等の月次申告 |
| **PPh Pasal 21 (Withholding on Salary)** | 所得税第21条（給与源泉税） | 給与、手当、賞与、退職金など個人への対価から天引きする所得税 |
| **PPh Pasal 23 (Withholding on Services)** | 所得税第23条（サービス源泉税） | コンサルティング、修理、保守、配当、利息等（原則2%〜15%）の源泉徴収 |
| **PPh Pasal 4 ayat 2 (Final Tax)** | 所得税第4条第2項（最終分離課税） | 土地建物の賃貸料（10%）や建設サービス売上等に対する確定課税 |
| **Koreksi Fiskal Positif / Negatif** | 税務調整（損金不算入 / 益金不算入） | 企業会計上の利益を税務上の課税所得へ変換するための加算・減算調整 |
| **Bukti Potong (Bupot / e-Bupot)** | 源泉徴収票・控除証明書 | 税金を天引きした側が受取側に交付する納税証明（電子申告システムで発行） |
| **Surat Tagihan Pajak (STP) / SKPKB** | 納税告知書 / 不足税額更正決定書 | 税務署が遅延利息や税務調査による追徴税額を命じる公的決定通知 |
| **Kode Billing Pajak (e-Billing)** | 電子納税番号（ビリングコード） | 銀行窓口やオンラインバンキングで国税を納付するための15桁の納付番号 |

---

## 2. 現場実践対話 (Percakapan Praktis Pajak Korporasi)

### 場面1: 外部コンサルタント費用に対するサービス源泉税（PPh 23）の処理協議

財務経理マネージャーと経理スタッフが、現地ITコンサルティング会社から届いた請求書（Invoice）に対し、源泉徴収票（e-Bupot）の発行と差引支払額を確認する場面です。

:::id-example
**Finance Manager (Hendra)**: Selamat pagi, Siti. Apakah faktur tagihan (invoice) dari PT Solusi Digital untuk jasa pemeliharaan server bulan lalu sudah diproses?  
**Staf Pajak (Siti)**: Selamat pagi, Pak Hendra. Total nilai jasanya adalah 100 juta rupiah di luar PPN. Kami sedang menyiapkan pemotongan PPh Pasal 23.  
**Finance Manager (Hendra)**: Berapa tarif pajak PPh Pasal 23 yang berlaku untuk jasa teknik dan manajemen teknologi informasi?  
**Staf Pajak (Siti)**: Tarif standarnya adalah dua persen, asalkan vendor memiliki Nomor Pokok Wajib Pajak (NPWP) yang valid. Jadi kami memotong 2 juta rupiah, dan jumlah bersih yang kita transfer ke rekening vendor adalah 98 juta rupiah ditambah PPN 11 persen (11 juta rupiah).  
**Finance Manager (Hendra)**: Apakah NPWP mereka sudah diverifikasi di sistem DJP Online?  
**Staf Pajak (Siti)**: Sudah valid, Pak. Bukti Pemotongan Elektronik (e-Bupot Unifikasi) sudah saya terbitkan di portal DJP Online dan kode billing pembayaran pajak sebesar dua juta rupiah sudah siap dibayarkan sebelum batas waktu tanggal sepuluh bulan depan.  
**Finance Manager (Hendra)**: Bagus sekali. Segera kirimkan salinan file PDF bukti potong tersebut ke bagian keuangan vendor agar mereka dapat mengkreditkannya sebagai kredit pajak PPh Badan mereka di akhir tahun.
:::

- **jasa pemeliharaan server**: サーバー保守サービス
- **PPh Pasal 23**: サービス取引に対する源泉所得税（原則2%）
- **e-Bupot Unifikasi**: 統合電子源泉徴収票発行システム
- **kredit pajak (tax credit)**: 税額控除（前払税金として確定申告で相殺控除すること）

---

### 場面2: 年次法人税申告（Form 1771）に向けた損金不算入（Koreksi Fiskal）の検証

公認会計士・税務顧問（Konsultan Pajak）と日系現地法人の財務ディレクターが、交際接待費や役員福利厚生費の税務調整（Koreksi Fiskal Positif）を精査する場面です。

:::id-example
**Konsultan Pajak (Budi)**: Selamat siang, Pak Tanaka. Dalam penyusunan draf SPT Tahunan PPh Badan 1771 tahun buku ini, laba bersih komersial menurut pembukuan adalah 10 miliar rupiah. Namun kita perlu melakukan koreksi fiskal positif sekitar 1,2 miliar rupiah.  
**Finance Director (Tanaka)**: Mengapa angka koreksi fiskal positifnya cukup besar, Pak Budi? Akun biaya apa saja yang tidak dapat diakui secara pajak (*non-deductible expense*)?  
**Konsultan Pajak (Budi)**: Pos terbesar berasal dari biaya hiburan dan representasi (entertainment expense) sebesar 600 juta rupiah yang tidak dilengkapi dengan Daftar Nominatif resmi sesuai Peraturan Menteri Keuangan.  
**Finance Director (Tanaka)**: Apa syarat dari Daftar Nominatif tersebut?  
**Konsultan Pajak (Budi)**: Harus ada rincian nama tamu, jabatan, nama perusahaan relasi bisnis, jenis hiburan, dan tanda terima yang jelas. Tanpa daftar nominatif yang dilampirkan ke SPT, pemeriksa pajak akan otomatis mendiskualifikasi biaya tersebut dari biaya pengurang penghasilan bruto.  
**Finance Director (Tanaka)**: Poin yang sangat penting. Pos biaya kedua apa yang terkena koreksi?  
**Konsultan Pajak (Budi)**: Pos kedua adalah tunjangan fasilitas natura (biaya sewa apartemen dan mobil untuk ekspatriat Jepang) yang belum dihitung sebagai objek PPh 21 karyawan.  
**Finance Director (Tanaka)**: Baik, kami akan kumpulkan seluruh bukti daftar nominatif yang ada agar nilai koreksi fiskal bisa ditekan secara legal sebelum SPT 1771 kita laporkan secara elektronik pada tanggal 30 April.
:::

- **laba bersih komersial**: 企業会計上の税引前当期純利益
- **koreksi fiskal positif**: 損金不算入調整（課税所得を加算する調整）
- **Daftar Nominatif**: 交際費明細書（税務上の損金算入に必須の法定付属書類）
- **fasilitas natura (benefit in kind)**: 現物給与・フリンジベネフィット（社宅・社用車等）

---

## 3. 税務申告実務で頻出する実務構文集

### 申告・納付期限のフレーズ

- **Batas waktu pelaporan SPT Tahunan PPh Badan adalah paling lambat empat bulan setelah akhir tahun pajak.**  
  （年次法人税確定申告書（SPT 1771）の提出期限は事業年度終了後最長4ヶ月以内です。）
- **Setorkan pajak penghasilan yang dipotong sebelum tanggal sepuluh bulan berikutnya.**  
  （源泉徴収した所得税は翌月10日までに国庫へ納付してください。）
- **Buat kode e-billing melalui portal resmi DJP Online untuk pembayaran PPh Pasal 25.**  
  （法人税前払予納（PPh 25）の納付のため、DJP Onlineポータルでビリングコードを生成してください。）

### 税務調査・更正のフレーズ

- **Surat Perintah Pemeriksaan Pajak (SP2) telah diterbitkan oleh Kantor Pelayanan Pajak (KPP).**  
  （税務署（KPP）より税務調査実施通知書（SP2）が発行されました。）
- **Siapkan seluruh buku besar (General Ledger), rekening koran bank, dan faktur pajak pendukung.**  
  （総勘定元帳、銀行残高証明・入出金明細、裏付け税務インボイスをすべて準備してください。）

---

> [!IMPORTANT]
> **交際費の「Daftar Nominatif」がないと全額損金否認**  
> インドネシア税法では、取引先との接待・会食費用（Entertainment Expense）を税務上の損金（Deductible Expense）として認めてもらうためには、**確定申告時に「Daftar Nominatif（交際相手の氏名・会社・役職・日付・場所・目的を記載したリスト）」の添付が絶対条件**となります。これがないと税務調査で100%全額否認され、22%の法人税追徴金と延滞利息が発生するため、領収書ごとの詳細記録を徹底しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 企業が提出する年次法人所得税確定申告書の公式フォーム番号（申告書名称）はどれでしょう？</summary>

1. Formulir 1771 (SPT Tahunan PPh Badan)  
2. Formulir 1770  
3. Formulir PPh 21  

**正解: 1**  
**解説**: 法人の年次確定申告書は「Formulir 1771（SPT Tahunan PPh Badan）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 会計上の費用であっても、税務上の損金として認められない項目を加算調整することを何と呼ぶでしょう？</summary>

1. Koreksi Fiskal Positif  
2. Koreksi Fiskal Negatif  
3. Amortisasi  

**正解: 1**  
**解説**: 税務上の課税所得を増やす（損金不算入とする）税務調整を「Koreksi Fiskal Positif」と呼びます。
</details>
