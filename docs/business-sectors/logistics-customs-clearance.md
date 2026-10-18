# B21: 輸出入通関手続き（Kepabeanan / Bea Cukai）とHSコード分類

インドネシアで貿易、製造、流通ビジネスを展開する企業にとって、財務省関税総局（**Direktorat Jenderal Bea dan Cukai - DJBC**）が管轄する輸出入通関手続き（**Kepabeanan**）と**HSコード（Kode HS: Harmonized System）**の適正分類は、サプライチェーンの円滑性と税務コンプライアンスを左右する最重要実務です。

輸入貨物の通関ステータスは、リスク分析（Manajemen Risiko）によって**グリーンレーン（Jalur Hijau: 書類審査のみ）**、**イエローレーン（Jalur Kuning: 追加書類審査）**、**レッドレーン（Jalur Merah: 開梱現物検査）**に振り分けられます。HSコードの誤申告は追徴関税（Bea Masuk）や重加算税（Denda Administrasi）の対象となります。

本記事では、輸入申告書（PIB）、輸出申告書（PEB）、HSコードの事前照会（Inpassing）、税関検査立会いに関する実務インドネシア語を体系的に解説します。

---

## 1. 通関・税関手続きに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Kepabeanan / Bea dan Cukai** | 税関・通関実務 / 関税消費税局 | 財務省傘下で貨物の輸出入管理、関税賦課、密輸取締を行う官庁 |
| **PIB (Pemberitahuan Impor Barang)** | 輸入申告書 (PIB) | 輸入者が貨物の品目、数量、価額（CIF）、関税額を申告する公的電子文書 |
| **PEB (Pemberitahuan Ekspor Barang)** | 輸出申告書 (PEB) | 貨物を国外へ積み出す際に税関へ提出する公的電子申告書 |
| **Kode HS (Harmonized System Code)** | HSコード（統計品目番号） | 世界税関機構（WCO）に基づく商品分類番号（関税率や輸入規制の基準） |
| **Bea Masuk / Bea Keluar** | 輸入関税 / 輸出関税 | 貨物のCIF価額に対して品目ごとに課される税金 |
| **Jalur Hijau / Kuning / Merah** | グリーン / イエロー / レッドレーン | 税関審査区分：即時許可（緑）/ 書類審査（黄）/ 現物開梱検査（赤） |
| **SPPB (Surat Persetujuan Pengeluaran Barang)** | 貨物搬出許可証 (SPPB) | 税関審査と関税・諸税納付が完了し、港湾倉庫からの引き出しを認める書類 |
| **PPJK (Pengusaha Pengurusan Jasa Kepabeanan)** | 通関業者（カスタムズブローカー） | 荷主に代わってPIB作成や税関交渉を代行する有資格の通関取扱業者 |
| **INSW (Indonesia National Single Window)** | 国家シングルウィンドウ (INSW) | 輸出入の許認可、検疫、税関手続きを一括電子処理する政府ポータル |
| **Pemeriksaan Fisik Barang (Behandle)** | 税関現物検査（ベハンドゥル） | レッドレーンに指定されたコンテナを開梱し、税関検査官が実物を点検する作業 |
| **Notul (Nota Pembetulan / Surat Penetapan Tarif)** | 税関更正通知（追徴課税通知書） | 税関が品目分類（HSコード）や課税標準価格を否認し、追徴金を命じる公文書 |

---

## 2. 現場実践対話 (Percakapan Praktis Kepabeanan)

### 場面1: レッドレーン（Jalur Merah）指定と現物検査（Behandle）の立会い手配

輸入コンテナが税関のシステムで「レッドレーン（現物検査）」に指定され、日系商社のロジスティクス担当者が通関業者（PPJK）と検査立会い日程を調整する場面です。

:::id-example
**Import Manager (Bambang)**: Halo Pak Joko dari PPJK. Bagaimana status pengajuan dokumen PIB untuk tiga kontainer suku cadang mesin yang tiba di Pelabuhan Tanjung Priok kemarin?  
**Petugas PPJK (Joko)**: Selamat siang, Pak Bambang. Sistem CEISA Bea Cukai baru saja mengeluarkan respon *Surat Pemberitahuan Jalur Merah* (SPJM). Kargo Anda terkena pemeriksaan fisik.  
**Bambang**: Waduh, kenapa bisa kena jalur merah? Apakah karena ada perbedaan deskripsi barang pada *Packing List* dan Faktur Komersial (*Commercial Invoice*)?  
**Petugas PPJK (Joko)**: Bukan, Pak. Dari analisa profil risiko, ini adalah pemeriksaan acak (random check) berkala karena importir baru menggunakan kode HS ini untuk pertama kalinya.  
**Bambang**: Kapan pemeriksaan fisik (*behandle*) bisa dijadwalkan di Tempat Pemeriksaan Fisik Terpadu (TPFT) Graha Segara? Pelanggan kami di Cikarang sudah menunggu barang ini untuk perakitan minggu depan.  
**Petugas PPJK (Joko)**: Kami sudah memesan nomor antrean pemeriksaan untuk besok pagi pukul sembilan. Mohon siapkan tim teknis Anda untuk mendampingi pembukaan segel kontainer dan membawa sampel produk asli serta brosur spesifikasi teknis jika pemeriksa bea cukai meminta penjelasan detail.  
**Bambang**: Baik, saya sendiri bersama staf teknis akan hadir mendampingi Anda di dermaga besok pagi agar prosesnya cepat selesai dan SPPB segera terbit.
:::

- **Pelabuhan Tanjung Priok**: タンジュンプリオク港（ジャカルタ北部のインドネシア最大国際港湾）
- **surat pemberitahuan jalur merah (SPJM)**: レッドレーン通知書
- **pembukaan segel kontainer**: コンテナの税関シールの開錠
- **brosur spesifikasi teknis**: 技術仕様カタログ

---

### 場面2: HSコード分類の疑義に対する税関更正通知（Notul）への異議申し立て

税関から部品のHSコードの解釈違いを理由に高税率の追徴金（Notul）が通知され、法解釈と異議申し立て（Keberatan）を協議する場面です。

:::id-example
**Petugas PPJK (Joko)**: Pak Bambang, kami menerima Surat Penetapan Tarif dan/atau Nilai Pabean (SPTNP) atau biasa disebut *Notul* dari kantor Bea Cukai Tanjung Priok.  
**Bambang**: Berapa nilai penetapan tambahannya, dan apa dasar argumen pemeriksa Bea Cukai?  
**Petugas PPJK (Joko)**: Pemeriksa mengubah klasifikasi kode HS komponen kita dari bab 84 (bagian mesin dengan bea masuk 5%) menjadi bab 85 (perangkat elektronik dengan bea masuk 10%). Ada tagihan kekurangan bea masuk dan denda administrasi sebesar 45 juta rupiah.  
**Bambang**: Tapi komponen ini adalah katup mekanis murni tanpa sirkuit terpadu! Jelas-jelas ini masuk ke Pos 8481 sesuai Buku Tarif Kepabeanan Indonesia (BTKI).  
**Petugas PPJK (Joko)**: Betul, Pak. Kita memiliki dasar hukum yang sangat kuat berdasarkan Catatan Bagian XVI dan Penjelasan WCO (Explanatory Notes).  
**Bambang**: Kalau begitu, kita tidak boleh menerima penetapan sepihak ini. Segera siapkan Surat Permohonan Keberatan resmi kepada Kepala Kantor Bea Cukai dalam waktu sebelum 60 hari kerja, dan lampirkan hasil uji laboratorium independen.  
**Petugas PPJK (Joko)**: Siap, Pak. Kami akan menyusun draf argumen keberatannya hari ini dan mengurus jaminan bank (*bank guarantee*) agar barang tetap bisa dikeluarkan terlebih dahulu selama proses sengketa berjalan.
:::

- **SPTNP / Notul**: 関税更正通知書（税関による税率・評価替え処分）
- **Buku Tarif Kepabeanan Indonesia (BTKI)**: インドネシア関税率表
- **Surat Permohonan Keberatan**: 税関異議申立書
- **jaminan bank (bank guarantee)**: 銀行保証状（争訟中に貨物を仮引き取りするための保証金担保）

---

## 3. 通関・税関業務で頻出する実務構文集

### 申告・書類確認のフレーズ

- **Pastikan nilai pabean (CIF: Biaya, Asuransi, dan Tambang) dihitung secara akurat.**  
  （課税標準価格（CIF：運賃・保険料込み）が正確に算出されていることを確認してください。）
- **Berapa tarif preferensi bea masuk jika menggunakan Surat Keterangan Asal (Form IJEPA / Form AK)?**  
  （日イEPA特恵原産地証明書（Form IJEPA）を利用した場合の特恵関税率は何パーセントですか？）
- **Dokumen PIB telah divalidasi dan Surat Perintah Pembayaran Pajak (Billing DJBC) sudah terbit.**  
  （PIB申告書が検証され、税関納税告知書（ビリングコード）が発行されました。）

### トラブル・検査対応のフレーズ

- **Kontainer telah selesai diperiksa secara fisik dan tidak ditemukan ketidaksesuaian jumlah koli.**  
  （コンテナの現物検査が完了し、個数の不一致は見つかりませんでした。）
- **Surat Persetujuan Pengeluaran Barang (SPPB) sudah turun, armada truk bisa segera masuk ke dermaga.**  
  （搬出許可証（SPPB）が下りましたので、トラック部隊は直ちに埠頭に入場できます。）

---

> [!IMPORTANT]
> **日イEPA（IJEPA: Indonesia-Japan Economic Partnership Agreement）の活用**  
> 日本からインドネシアへの機械や部品の輸出では、日本商工会議所が発行するEPA特定原産地証明書（Form IJEPA）を電子提出することで、通常5〜10%の輸入関税が**0%（免税）**に軽減される品目が多数あります。ただし、インボイス上の記載（HSコード・原産国表示・船名）と1文字でも食い違いがあると税関に却下されるため、厳密な書類一致が求められます。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. インドネシアの輸入通関において、税関現物開梱検査（Behandle）が義務付けられる審査区分（レーン）はどれでしょう？</summary>

1. Jalur Hijau (Green Lane)  
2. Jalur Merah (Red Lane)  
3. Jalur Prioritas  

**正解: 2**  
**解説**: 現物検査（Pemeriksaan Fisik）が必要な区分は「Jalur Merah（レッドレーン）」です。
</details>

<details class="id-quiz">
<summary>Q2. 税関の審査・納税が完了し、港湾や保税倉庫から貨物を搬出することを正式に許可する書類の略称は？</summary>

1. SPPB (Surat Persetujuan Pengeluaran Barang)  
2. NPWP  
3. AMDAL  

**正解: 1**  
**解説**: 貨物の引き取りを許可する公的搬出許可証は「SPPB」と呼ばれます。
</details>
