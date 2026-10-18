# B23: 国際輸送ブッキング・船荷証券（B/L）と原産地証明書（SKA）

日本とインドネシア間、またはASEAN・世界各国のサプライチェーンを結ぶ国際物流において、海上コンテナ輸送（**Pengangkutan Laut / Ocean Freight**）および航空貨物輸送（**Pengangkutan Udara / Air Freight**）の手配実務は貿易実務の根幹を成します。

船会社（Shipping Line）やフォワーダーとのブッキング（Pemesanan Ruang Kapal）、有価証券としての**船荷証券（B/L: Bill of Lading）**の権利移転、航空貨物運送状（**Air Waybill: AWB**）、そして関税免除・減税を受けるための**特恵原産地証明書（SKA: Surat Keterangan Asal / Certificate of Origin）**の取り扱いには、1つの誤記載も許されない厳密さが要求されます。

本記事では、コンテナ船ブッキング（FCL / LCL）、航海スケジュール（ETA / ETD）、B/Lの種類（Original B/L vs Surrender B/L / Telex Release）、原産地規則（Rules of Origin）に関する実務インドネシア語を体系的に解説します。

---

## 1. 国際輸送・船積み書類に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Konosemen / B/L (Bill of Lading)** | 船荷証券 (B/L) | 海上輸送において船会社が発行する貨物の受取証・運送契約書・引換証券 |
| **AWB (Air Waybill)** | 航空貨物運送状 (AWB) | 航空輸送において航空会社が発行する運送状（流通性・有価証券性はない） |
| **SKA (Surat Keterangan Asal / COO)** | 原産地証明書 (COO) | 貨物が特定国で生産されたことを政府・商工会議所が証明する書類 |
| **Form IJEPA / Form D / Form AK** | EPA・FTA特恵原産地証明書様式 | 日イEPA（IJEPA）、ASEAN自由貿易（Form D）、ASEAN-韓国（Form AK）等 |
| **FCL (Muatan Kontainer Penuh)** | フルコンテナ積載 (FCL) | 1本のコンテナ（20フィート/40フィート）を1荷主が貸し切る輸送形態 |
| **LCL (Muatan Kurang dari Kontainer)** | コンテナ未満混載 (LCL) | 少量貨物を他の荷主の荷物と一緒に1本のコンテナに相積みする形態 |
| **ETD / ETA (Estimasi Waktu Berangkat / Tiba)** | 出港予定日 (ETD) / 入港予定日 (ETA) | Estimated Time of Departure / Estimated Time of Arrival |
| **Surrender B/L / Rilis Telex (Telex Release)** | サレンダーB/L / 元地回収 | 原本B/Lを荷送地で回収し、電信通知によって揚げ地で即時引き渡す方式 |
| **Manifes Kargo (Cargo Manifest)** | 積荷目録（マニフェスト） | 船舶や航空機に積載された全貨物の明細一覧表（税関へ提出） |
| **Pemberitahuan Kedatangan Kargo (Arrival Notice)** | 貨物到着案内 (Arrival Notice) | 船会社やフォワーダーが貨物到着前に荷受人（Consignee）へ送る通知書 |
| **DO (Surat Perintah Penyerahan Barang / Delivery Order)** | 荷渡指図書 (Delivery Order) | B/Lと引き換えに船会社が発行し、港湾ターミナルから貨物を引き取る書類 |

---

## 2. 現場実践対話 (Percakapan Praktis Ekspedisi Internasional)

### 場面1: 海上コンテナ船のブッキングとTelex Release（元地回収）の手配

日系機械メーカーの輸出入担当者が、国際貨物フォワーダーに対し、横浜港からタンジュンプリオク港（ジャカルタ）行きの40フィートコンテナのスペース予約と迅速なB/Lリリースを依頼する場面です。

:::id-example
**Logistics Officer (Hendra)**: Selamat pagi, Ibu Siska dari Global Freight Logistics. Kami ingin memesan ruang kapal (booking kontainer) untuk pengiriman mesin cetak dari Pelabuhan Yokohama ke Pelabuhan Tanjung Priok, Jakarta.  
**Freight Forwarder (Siska)**: Selamat pagi, Pak Hendra. Berapa volume kargonya dan jenis kontainer apa yang dibutuhkan?  
**Logistics Officer (Hendra)**: Kami membutuhkan satu kontainer 40 kaki *High Cube* (40' HC) muatan penuh (FCL). Berat kotor kargo sekitar 18 ton.  
**Freight Forwarder (Siska)**: Untuk jadwal pelayaran tercepat minggu depan, ada kapal Ocean Network Express (ONE) dengan ETD Yokohama tanggal 24 Oktober dan perkiraan waktu tiba (ETA) di Jakarta tanggal 2 November, waktu tempuh sekitar 9 hari langsung tanpa transit.  
**Logistics Officer (Hendra)**: Jadwal tersebut sangat ideal untuk lini produksi kami. Mengenai dokumen pengapalan, karena waktu tempuh laut cukup singkat, kami meminta penerbitan *Surrender B/L* atau *Telex Release* agar kami tidak perlu menunggu kurir berkas asli dari Tokyo.  
**Freight Forwarder (Siska)**: Baik, Pak. Setelah pihak pengirim (shipper) di Jepang menyerahkan B/L asli ke kantor kami di Tokyo dan membayar biaya pengapalan (freight charge), kantor kami di Jakarta akan langsung menerima konfirmasi rilis telex secara elektronik.
:::

- **kontainer 40 kaki High Cube**: 40フィート背高コンテナ（通常より約30cm背の高いコンテナ）
- **berat kotor (gross weight)**: 総重量（風袋込み重量）
- **tanpa transit (direct voyage)**: 直行便（トランジットなし）
- **pihak pengirim (shipper)**: 荷送人（シッパー）

---

### 場面2: 特恵原産地証明書（Form IJEPA）の記載不備と緊急差替え手続き

ジャカルタ税関の審査で、日本から届いたForm IJEPAのインボイス番号と実インボイスの日付に食い違いが見つかり、フォワーダーと至急修正を協議する場面です。

:::id-example
**Import Coordinator (Hendra)**: Ibu Siska, kami baru saja mendapat pemberitahuan dari pemeriksa dokumen Bea Cukai bahwa Surat Keterangan Asal (Form IJEPA) kami ditolak untuk mendapatkan tarif preferensi 0 persen!  
**Freight Forwarder (Siska)**: Mengapa ditolak, Pak Hendra? Apakah ada kesalahan pada kriteria asal barang (Origin Criterion)?  
**Import Coordinator (Hendra)**: Bukan pada kriteria CTC (Change in Tariff Classification), melainkan pada Kolom 10: nomor faktur komersial yang tertulis di lembar IJEPA tercetak `INV-2026-08`, sedangkan faktur asli yang diajukan ke PIB bertanggal revisi dengan nomor `INV-2026-08-REV1`.  
**Freight Forwarder (Siska)**: Ah, petugas Bea Cukai di Tanjung Priok memang sangat ketat mengenai perbedaan nomor sekecil apa pun antara invoice dan Form IJEPA.  
**Import Coordinator (Hendra)**: Jika IJEPA ini gugur, kami harus membayar bea masuk umum sebesar 10 persen atau sekitar 80 juta rupiah! Bisakah kita meminta Kamar Dagang dan Industri Jepang (JCCI) menerbitkan SKA pengganti bertanda *ISSUED RETROACTIVELY* secara ekspres?  
**Freight Forwarder (Siska)**: Tentu bisa, Pak. Kami akan segera berkoordinasi dengan agen kami di Tokyo untuk mengajukan penerbitan ulang sertifikat pengganti ke JCCI hari ini juga. Sementara itu, kami akan ajukan penjaminan tarif sementara ke Bea Cukai agar kontainer tidak terkena biaya inap (*demurrage*).
:::

- **tarif preferensi**: 特恵関税率（EPAによる優遇税率）
- **Change in Tariff Classification (CTC)**: 関税分類変更基準（原産地規則の判定要件）
- **ISSUED RETROACTIVELY**: 遡及発行（出港後に原産地証明書が発行された旨の法定スタンプ）
- **Kamar Dagang dan Industri Jepang (JCCI)**: 日本商工会議所

---

## 3. 国際輸送・船積みで頻出する実務構文集

### ブッキング・運航スケジュールのフレーズ

- **Konfirmasikan tanggal batas akhir penutupan kargo (Closing Time) di dermaga.**  
  （埠頭での貨物搬入締め切り時間（Cut-off / Closing Time）を確認してください。）
- **Apakah kapal ini mengalami keterlambatan jadwal (delay) akibat cuaca buruk di Laut Cina Selatan?**  
  （この船は南シナ海の悪天候により航海遅延が発生していますか？）
- **Segera bayar biaya tambang laut (ocean freight) agar Delivery Order (DO) dapat diterbitkan.**  
  （荷渡指図書（DO）を発行してもらうため、直ちに海上運賃を支払ってください。）

### 書類照合・原産地証明のフレーズ

- **Data pada Konosemen (B/L) harus cocok seratus persen dengan Packing List dan Faktur Komersial.**  
  （B/L上のデータはパッキングリストおよびコマーシャルインボイスと100パーセント一致しなければなりません。）
- **Form IJEPA elektronik (e-Form) kini dapat diverifikasi secara daring melalui sistem pertukaran data bilateral.**  
  （電子的Form IJEPA（e-Form）は二国間データ交換システムを通じてオンラインで検証可能です。）

---

> [!TIP]
> **Surrender B/L（元地回収）利用時のリスク管理**  
> 近海航路（日本〜インドネシア間：航海日数約8〜10日）では、原本B/Lの郵送遅延による港湾滞船料の発生を防ぐため、サレンダーB/Lが広く使われます。ただし、売買代金の全額回収前に荷送人がサレンダー手続きをしてしまうと、バイヤーが未払いのまま貨物を引き取れてしまうリスクがあるため、信用状（L/C）取引か全額前払い（T/T in Advance）かによって使い分ける必要があります。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 海上輸送において、船会社が貨物受領・運送契約を証明し、貨物の引取証券となる最重要貿易書類は？</summary>

1. B/L (Bill of Lading / Konosemen)  
2. Surat Izin Mengemudi (SIM)  
3. Faktur Pajak  

**正解: 1**  
**解説**: 船荷証券は英語で「Bill of Lading（B/L）」、インドネシア語で「Konosemen」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 日イEPA等の自由貿易協定に基づき、輸入関税の免税や特恵税率の適用を受けるために提出する書類は？</summary>

1. SKA (Surat Keterangan Asal / Certificate of Origin)  
2. NPWP  
3. UMR  

**正解: 1**  
**解説**: 原産地証明書は「SKA（Surat Keterangan Asal / COO）」と呼ばれ、Form IJEPAなどが該当します。
</details>
