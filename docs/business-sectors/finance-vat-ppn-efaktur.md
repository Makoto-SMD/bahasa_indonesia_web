# B42: 付加価値税（PPN）と電子タックスインボイス（e-Faktur）実務

インドネシアにおける間接税の主軸である**付加価値税（PPN: Pajak Pertambahan Nilai / VAT）**は、物品やサービスの国内取引および輸入に対して課される税金です（税制調和法 UU HPP により基本税率は**11%**、将来的に12%へ移行予定）。

課税事業者（**PKP: Pengusaha Kena Pajak**）として認定された企業は、売上時に**売上税額（Pajak Keluaran: 出力PPN）**を記載した公式の電子タックスインボイス（**e-Faktur**）を税務総局（DJP）のシステムから即座に発行・認証（Approval）を受けなければなりません。

また、仕入れ時に支払った**仕入税額（Pajak Masukan: 入力PPN）**との相殺控除（Pengkreditan Pajak Masukan）、月末の月次申告（**SPT Masa PPN: Formulir 1111**）、そして過大納付が発生した際の**税務還付（Restitusi PPN）**請求と税務調査リスクへの対応が求められます。本記事では、NSFP（税務番号割当）、e-Fakturデスクトップ/Web版操作、相殺・還付手続に関する実務インドネシア語を体系的に解説します。

---

## 1. 付加価値税（PPN）・e-Fakturに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **PPN (Pajak Pertambahan Nilai / VAT)** | 付加価値税 (PPN / 消費税) | 課税物品（BKP）や課税サービス（JKP）の取引に課される間接税（現行11%） |
| **PKP (Pengusaha Kena Pajak)** | 課税事業者 (PKP) | 年間売上高が48億ルピアを超え、税務署からPPN徴収・発行を認可された事業者 |
| **Faktur Pajak Elektronik (e-Faktur)** | 電子タックスインボイス (e-Faktur) | DJPの公式暗号化システムで発行・承認（QRコード付）される公式税務請求書 |
| **Pajak Keluaran (Output VAT)** | 売上税額（出力PPN） | PKPが自社製品・サービスを顧客へ販売した際に徴収するPPN |
| **Pajak Masukan (Input VAT)** | 仕入税額（入力PPN） | 原材料購入や外部サービス利用時にサプライヤーへ支払ったPPN |
| **Pengkreditan Pajak Masukan** | 仕入税額控除 | 納付すべき売上税額から、支払った仕入税額を差し引いて差額を納税する仕組み |
| **NSFP (Nomor Seri Faktur Pajak)** | インボイス連番（NSFP） | 税務署からオンラインで事前に割り当てを受ける16桁の公式請求書番号 |
| **Restitusi PPN (VAT Refund)** | PPN還付（仕入税額還付請求） | 仕入税額が売上税額を上回り、超過納税分を国庫から現金還付してもらう手続き |
| **SPT Masa PPN (Formulir 1111)** | PPN月次確定申告書 | 翌月末日までに提出する月次の付加価値税申告書 |
| **BKP / JKP (Barang / Jasa Kena Pajak)** | 課税物品 / 課税サービス | 法律で非課税指定（非課税生活必需品等）されていない課税対象商品・役務 |

---

## 2. 現場実践対話 (Percakapan Praktis Administrasi PPN)

### 場面1: 顧客向けe-Faktur（電子タックスインボイス）の発行遅延と税務ペナルティ防止

経理スタッフが営業部からの売上報告を受け、税務署のe-FakturシステムでNSFPを紐付けて即座に承認（Approval Success）を取得する場面です。

:::id-example
**Supervisor Pajak (Dewi)**: Selamat pagi, Reza. Apakah faktur komersial (*commercial invoice*) untuk pengiriman 500 unit mesin ke PT Indotama Sukses tanggal 15 Oktober kemarin sudah dibuatkan e-Faktur-nya?  
**Staf Pajak (Reza)**: Selamat pagi, Bu Dewi. Saya baru saja mengimpor data fakturnya ke aplikasi e-Faktur versi 4.0. Namun, ada sedikit kendala karena Nomor Seri Faktur Pajak (NSFP) dari jatah kuota bulan ini sudah habis.  
**Supervisor Pajak (Dewi)**: Waduh, segera minta tambahan alokasi NSFP baru melalui portal e-Nofa DJP sekarang juga! Ingat ketentuan terbaru: Faktur Pajak wajib diunggah (*upload*) dan mendapatkan persetujuan (*approval*) dari server DJP paling lambat tanggal 15 bulan berikutnya!  
**Staf Pajak (Reza)**: Baik Bu, permohonan online jatah NSFP baru sudah saya ajukan via e-Nofa dan langsung disetujui sebanyak 100 nomor baru.  
**Supervisor Pajak (Dewi)**: Bagus. Pastikan Nama, Alamat, dan NPWP pembeli (atau NIK jika pembeli perorangan) sudah cocok seratus persen dengan data master DJP agar statusnya tidak *Reject* saat diunggah.  
**Staf Pajak (Reza)**: Data pembeli sudah tervalidasi, Bu. Saya klik *Upload Faktur* sekarang... Statusnya langsung berubah menjadi *Approval Sukses*. PDF faktur pajak resmi lengkap dengan barcode QR sudah bisa diunduh dan kami kirimkan ke pelanggan bersama kuitansi tagihan.
:::

- **portal e-Nofa**: 税務総局のインボイス番号（NSFP）電子割当申請ポータル
- **Approval Sukses**: 税務署サーバーによる公式承認完了
- **NPWP / NIK pembeli**: 買主の納税者番号（法人はNPWP、個人は身分証番号NIK）
- **Reject saat diunggah**: アップロード時のエラー却下

---

### 場面2: 輸出企業における多額の仕入税額超過とPPN還付（Restitusi）の税務調査判断

輸出比率が80%を超える保税工場の日系CFOと税務アドバイザーが、売上税額0%（輸出免税）による仕入税額超過（Lebih Bayar）の還付申請と税務調査リスクを検討する場面です。

:::id-example
**CFO (Yamamoto)**: Pak Konsultan, karena produk kita hampir seluruhnya diekspor ke Jepang dan Eropa dengan tarif PPN ekspor 0 persen, saldo Pajak Masukan (仕入PPN) kita bulan ini mengalami Lebih Bayar (overpaid) sebesar 3 miliar rupiah dari pembelian bahan baku lokal.  
**Tax Advisor (Budi)**: Selamat siang, Pak Yamamoto. Sesuai Pasal 9 ayat 4c UU PPN, pengusaha yang melakukan ekspor Barang Kena Pajak berhak mengajukan permohonan pengembalian kelebihan pembayaran pajak (*Restitusi PPN*) pada setiap Masa Pajak (setiap bulan), tanpa harus menunggu akhir tahun.  
**CFO (Yamamoto)**: Jika kita memilih opsi Restitusi (pengembalian tunai ke rekening bank perusahaan), apakah kantor pajak akan otomatis melakukan pemeriksaan pajak menyeluruh (*tax audit*)?  
**Tax Advisor (Budi)**: Ya, Pak. Sesuai prosedur standar DJP, setiap permohonan restitusi reguler wajib didahului dengan Pemeriksaan Pajak untuk menguji keabsahan faktur pajak masukan dan arus uang bank. Pemeriksa akan mengecek apakah seluruh vendor kita benar-benar menyetorkan PPN tersebut ke kas negara.  
**CFO (Yamamoto)**: Berapa lama waktu pemeriksaan restitusi tersebut?  
**Tax Advisor (Budi)**: Jangka waktu pemeriksaannya maksimal 12 bulan sejak surat permohonan diterima lengkap. Namun, jika perusahaan kita mengajukan permohonan status *Wajib Pajak Kriteria Tertentu (WP Patuh)*, kita bisa mendapatkan Pengembalian Pendahuluan (Restitusi Cepat) dalam waktu 1 bulan saja tanpa pemeriksaan di awal, melainkan hanya penelitian dokumen.  
**CFO (Yamamoto)**: Mari kita ajukan fasilitas Pengembalian Pendahuluan tersebut agar arus kas (cash flow) perusahaan tidak tertahan 3 miliar rupiah selama satu tahun di kas negara.
:::

- **PPN ekspor 0 persen**: 輸出に対する付加価値税ゼロ税率（輸出免税）
- **Lebih Bayar (LB)**: 超過納税・税額控除余剰
- **Pengembalian Pendahuluan**: 事前還付（優良納税者に対する1ヶ月以内の即時還付制度）
- **arus kas (cash flow)**: キャッシュフロー・資金繰り

---

## 3. PPN・e-Faktur実務で頻出する実務構文集

### インボイス発行・管理

- **Faktur Pajak wajib dibuat pada saat penyerahan Barang Kena Pajak atau saat penerimaan pembayaran.**  
  （タックスインボイス（Faktur Pajak）は課税物品の引渡し時、または代金受領時のいずれか早い方に作成する義務があります。）
- **Batas waktu pengunggahan e-Faktur ke server DJP adalah tanggal lima belas bulan berikutnya.**  
  （DJPサーバーへのe-Fakturアップロード期限は翌月15日です。）
- **Faktur Pajak Masukan dapat dikreditkan dalam jangka waktu paling lambat tiga bulan.**  
  （仕入税額インボイスは発行月から最長3ヶ月以内に仕入税額控除が可能です。）

### 申告・還付のフレーズ

- **Pelaporan SPT Masa PPN Formulir 1111 dilakukan paling lambat akhir bulan berikutnya.**  
  （PPN月次確定申告書（Form 1111）の提出は翌月末日までに行われます。）
- **Kelebihan Pajak Masukan dapat dikompensasikan ke masa pajak berikutnya atau dimintakan restitusi.**  
  （仕入税額の超過分は翌月へ繰り越し相殺（コンペンセーション）するか、現金還付を請求することができます。）

---

> [!IMPORTANT]
> **架空インボイス（Faktur Pajak Fiktif）と取引先確認の義務**  
> サプライヤーから受け取ったe-Fakturであっても、その業者が実体のないペーパーカンパニー（架空業者）だった場合、税務署から「仕入税額控除の全額否認＋100%の重加算税」が課されるリスクがあります。高額な新規取引先とは、必ず「相手の工場・オフィスの実地確認」「銀行口座の一致」「PKP登録証の有効性確認」を行いましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. インドネシアで税務総局（DJP）のシステムに接続して公式に発行・承認される電子タックスインボイスの名称は？</summary>

1. e-Faktur  
2. e-KTP  
3. e-Toll  

**正解: 1**  
**解説**: 付加価値税（PPN）の公式電子インボイスは「e-Faktur（Faktur Pajak Elektronik）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 輸出企業などで、支払った仕入PPNが売上PPNを上回った場合に、国庫から現金の払い戻しを受ける手続きは？</summary>

1. Restitusi PPN  
2. Denda Administrasi  
3. Amortisasi  

**正解: 1**  
**解説**: 超過納税分の現金還付請求は「Restitusi PPN（VAT Refund）」と呼ばれます。
</details>
