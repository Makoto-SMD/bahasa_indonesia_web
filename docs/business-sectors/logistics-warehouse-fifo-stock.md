# B25: 倉庫入出庫管理・棚卸差異（Stock Opname）と先入れ先出し（FIFO）

物流センターや工場併設倉庫（**Gudang Logistik / Pergudangan**）において、入庫・保管・ピッキング・出庫のオペレーション精度は、欠品（Stockout）や過剰在庫、製品の品質劣化を防ぐための要です。

特に食品、医薬品、化学品、ゴム・樹脂製品など消費期限や使用可能期間（Shelf-Life）がある資材では、**先入れ先出し（FIFO: First In First Out / Masuk Pertama Keluar Pertama）**の徹底が必須です。また、定期的な実地棚卸（**Stock Opname / Inventarisasi Fisik**）を実施し、帳簿在庫（Book Stock）と実在庫（Physical Stock）の**在庫差異（Selisih Stok / Variansi）**の発生原因を調査・是正する手順が確立されていなければなりません。

本記事では、倉庫管理システム（WMS）、バーコードピッキング、ロケーション管理、棚卸差異の調査と帳簿調整に関する実務インドネシア語を体系的に解説します。

---

## 1. 倉庫管理・棚卸に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Gudang / Pergudangan (Warehouse / WMS)** | 倉庫 / 倉庫管理システム | 物資の受入、保管、管理、出荷を担う拠点および情報システム |
| **Stock Opname (SO / Inventarisasi Fisik)** | 実地棚卸（ストックオプネーム） | 倉庫内の全在庫を実際に数え上げて帳簿残高と照合する作業 |
| **FIFO (Masuk Pertama, Keluar Pertama)** | 先入れ先出し (FIFO) | 先に入庫した古いロットから優先的に出庫・使用する原則 |
| **Selisih Stok (Inventory Discrepancy / Variance)** | 在庫差異（棚卸差異） | 帳簿上の在庫数と実際に倉庫にあった現品数との食い違い |
| **Kartu Stok / Sistem Barcode** | 在庫カード / バーコードスキャン | 各パレットや棚に備え付けられた入出庫履歴札および電子読み取り |
| **Penerimaan Barang (Inbound / Receiving)** | 入庫・荷受け | 運送会社から荷物を受け取り、納品伝票と現品を照合・登録する工程 |
| **Pengeluaran Barang (Outbound / Dispatch)** | 出庫・出荷 | 出荷指示書（Delivery Order）に基づき検品・梱包・トラック積み込みする工程 |
| **Pengambilan Barang (Picking / Packing)** | ピッキング・梱包 | 保管棚（Racking）から指定品番・数量を取り出して仕分け・箱詰めする作業 |
| **Alamat Rak / Lokasi Penyimpanan (Bin Location)** | 棚番・ロケーション番号 | 倉庫内のどの列、どの棚、どの段にあるかを特定する住所コード |
| **Barang Rusak / Kedaluwarsa (Damaged / Expired)** | 破損品・期限切れ品 | 輸送・荷役中の落下破損、湿気による劣化、使用期限が切れた不良品 |
| **Penyesuaian Saldo (Stock Adjustment)** | 在庫調整・帳簿修正 | 棚卸差異の承認後、会計システムの在庫残高を実在庫数に合わせる処理 |

---

## 2. 現場実践対話 (Percakapan Praktis Pergudangan)

### 場面1: 倉庫内での先入れ先出し（FIFO）違反の発見と再配置指示

倉庫スーパーバイザーが原材料保管エリアを巡回し、作業員が手前に置かれた新しいロットを先に出荷しようとしているのを発見して指導する場面です。

:::id-example
**Supervisor Gudang (Hasan)**: Tunggu sebentar, Mas Doni! Tolong hentikan proses pemuatan palet lembaran karet ini ke forklift.  
**Operator Forklift (Doni)**: Ada apa, Pak Hasan? Ini barang yang diminta oleh departemen produksi untuk pesanan siang ini.  
**Supervisor Gudang (Hasan)**: Coba lihat label barcode pada palet yang kamu ambil. Ini adalah Lot B-10 yang baru masuk kemarin sore, sedangkan di rak bagian belakang masih ada lima palet Lot B-02 yang masuk dua minggu lalu!  
**Operator Forklift (Doni)**: Maaf, Pak. Palet Lot B-10 ini posisinya berada di paling depan lorong, jadi lebih mudah diambil tanpa harus memindahkan tumpukan lain.  
**Supervisor Gudang (Hasan)**: Memang lebih cepat untukmu, tetapi bahan kimia karet memiliki masa simpan (*shelf-life*) maksimum tiga bulan. Jika kita melanggar prinsip FIFO, bahan lama di belakang akan mengeras, kedaluwarsa, dan tidak bisa dipakai lagi oleh pabrik!  
**Operator Forklift (Doni)**: Saya paham sekarang, Pak. Saya salah karena mencari jalan pintas.  
**Supervisor Gudang (Hasan)**: Turunkan kembali palet baru ini. Gunakan sistem *gravity flow rack* kita dengan benar: masukkan barang baru dari sisi belakang rak, dan ambil barang keluar hanya dari sisi depan rak agar rotasi stok otomatis berjalan.
:::

- **prinsip FIFO**: 先入れ先出しの原則
- **shelf-life (masa simpan)**: 有効保管期間・シェルフライフ
- **gravity flow rack**: 先入れ先出し専用の傾斜ローラースルーラック
- **mencari jalan pintas**: 近道（安易な手抜き）をする

---

### 場面2: 月末実地棚卸（Stock Opname）での在庫差異調査と原因特定

月末の全数棚卸が終了し、倉庫責任者と会計監査担当者が高額電子部品の差異（マイナス5個）の原因を調査する場面です。

:::id-example
**Akuntan Biaya (Rina)**: Pak Hasan, hasil rekapitulasi Stock Opname (SO) akhir kuartal ketiga menunjukkan adanya selisih minus lima buah pada komponen sensor optik IC-990.  
**Supervisor Gudang (Hasan)**: Komponen itu harganya cukup mahal, sekitar dua juta rupiah per unit. Selisih totalnya sepuluh juta rupiah. Apakah sudah dihitung ulang secara manual (*recheck*)?  
**Akuntan Biaya (Rina)**: Kami sudah menghitung fisik sebanyak tiga kali dengan dua petugas berbeda, hasilnya tetap 195 unit, sementara saldo buku sistem SAP tercatat 200 unit.  
**Supervisor Gudang (Hasan)**: Mari kita periksa log riwayat pergerakan barang (*goods movement log*) di sistem WMS selama dua minggu terakhir.  
**Akuntan Biaya (Rina)**: Lihat transaksi tanggal 18 September: ada permintaan darurat dari tim perbaikan lini untuk lima unit, tetapi status dokumen *Surat Bukti Pengeluaran Barang* (Material Issue Note) belum ditandatangani oleh pemohon.  
**Supervisor Gudang (Hasan)**: Nah, ini dia akar masalahnya! Operator shift malam menyerahkan barang fisik ke teknisi saat darurat mesin mati, tetapi lupa mencatat konfirmasi serah terima di komputer. Jadi ini bukan kehilangan fisik atau pencurian, melainkan keterlambatan pembukuan administrasi.  
**Akuntan Biaya (Rina)**: Syukurlah barangnya jelas keberadaannya. Tolong selesaikan dokumen pengeluarannya hari ini agar kami bisa mencocokkan saldo buku dan tidak perlu membuat jurnal kerugian selisih persediaan.
:::

- **rekapitulasi Stock Opname**: 実地棚卸集計表
- **log pergerakan barang (goods movement log)**: 入出庫移動ログ
- **keterlambatan pembukuan administrasi**: 事務入力の遅延（未記帳）
- **jurnal kerugian selisih**: 棚卸減耗損・棚卸差異損失仕訳

---

## 3. 倉庫業務で頻出する実務構文集

### 入出庫・ロケーション管理

- **Pastikan setiap palet ditempatkan tepat di alamat rak (bin location) yang sesuai.**  
  （各パレットが指定された棚番ロケーションに正確に配置されていることを確認してください。）
- **Pindai barcode pada Surat Jalan sebelum mengeluarkan barang dari pintu dok pemuatan.**  
  （積込ドック扉から荷物を搬出する前に、納品書のバーコードをスキャンしてください。）
- **Lakukan inspeksi visual terhadap kemasan kardus yang penyok atau basah sebelum menerima kargo.**  
  （貨物を受け取る前に、箱のへこみや水濡れがないか目視点検を実施してください。）

### 棚卸・在庫調査

- **Seluruh aktivitas penerimaan dan pengeluaran barang dihentikan sementara selama Stock Opname.**  
  （実地棚卸の実施中は、すべての入出庫作業を一時停止します。）
- **Batas toleransi selisih persediaan untuk barang bernilai tinggi adalah nol persen.**  
  （高額品目の在庫差異許容基準はゼロパーセントです。）

---

> [!TIP]
> **「サイクルカウント（Cycle Counting）」による日常棚卸**  
> 年に1〜2回の大型棚卸（Stock Opname）だけでは、ズレが発生した直後に原因を突き止めることが困難です。日系倉庫では、毎日特定エリアや高回転品目（Aランク品）を小分けにして日常点検する「サイクルカウント」を導入し、帳簿精度（Inventory Record Accuracy: IRA）を99.8%以上に保つ運用が定石です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 倉庫に保管されている実際の物品数をすべて数え上げ、帳簿在庫と照合する棚卸作業を表すインドネシアのビジネス用語は？</summary>

1. Stock Opname  
2. Surat Peringatan  
3. Uji Coba  

**正解: 1**  
**解説**: 実地棚卸はインドネシアの商業・製造現場で一般に「Stock Opname（ストックオプネーム）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 入庫日の古いロットから優先的に出庫し、長期保管による品質劣化や期限切れを防ぐ原則は？</summary>

1. FIFO (Masuk Pertama, Keluar Pertama)  
2. LIFO (Last In First Out)  
3. Random Picking  

**正解: 1**  
**解説**: 先入れ先出しは「FIFO（First In First Out / Masuk Pertama Keluar Pertama）」と呼ばれます。
</details>
