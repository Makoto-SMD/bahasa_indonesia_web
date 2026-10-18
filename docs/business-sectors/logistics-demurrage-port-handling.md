# B28: 港湾滞船料（Demurrage / Detention）防止と港湾手続き

インドネシアへの海上貨物輸入において、企業を悩ませる最大の想定外コストが、港湾ターミナルや船会社から請求される高額な超過料金である**デマレージ（Demurrage: 港内コンテナ超過保管料）**と**ディテンション（Detention: 港外コンテナ延滞料）**です。

タンジュンプリオク港（Jakarta）やタンジュンペラ港（Surabaya）等の主要港湾では、貨物が船から陸揚げされた後、一定の無料保管期間（**Masa Bebas / Free Time**: 通常3〜7日間）が与えられます。しかし、輸入ライセンス不備や税関検査（Jalur Merah）、輸入申告書（PIB）の修正等でこの期間を過ぎると、累進的な超過料金が日割りで課され、数千万円規模の莫大なペナルティに膨らむことがあります。

本記事では、フリータイム（Free Time）の延長交渉、港湾ヤード保管料（Storage Fee）、空コンテナ返却（Return of Empty Container）、港湾手続きのボトルネック回避に関する実務インドネシア語を体系的に解説します。

---

## 1. 港湾滞船料・延滞料に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Demurrage (Biaya Keterlambatan Pengambilan)** | デマレージ（港内延滞料） | 港湾ターミナル敷地内からコンテナを搬出せず放置したことに対する超過料金 |
| **Detention (Biaya Keterlambatan Pengembalian)** | ディテンション（港外延滞料） | 港から搬出した実入りコンテナを荷降ろし後、指定デポへ空返却するまでの遅延料 |
| **Waktu Bebas Denda (Free Time)** | フリータイム（無料猶予期間） | デマレージやディテンションが発生せずにコンテナを保管・利用できる猶予日数 |
| **Biaya Penumpukan Pelabuhan (Storage Fee)** | 港湾ヤード保管料 | 港湾公社（Pelindo / JICT / Koja等）がヤードの占有面積・日数に対して課す保管料 |
| **Pengembalian Kontainer Kosong (Empty Return)** | 空コンテナ返却 | 荷降ろし完了後、清掃して船会社指定の空コンテナデポへ返納する作業 |
| **Pelindo (PT Pelabuhan Indonesia)** | インドネシア港湾公社 (Pelindo) | インドネシア国内の主要商業港湾を統合管理・運営する巨大国営企業 |
| **Kuitansi Jaminan Kontainer (Container Deposit)** | コンテナ保証金（デポジット） | 空バン返却時の破損や遅延に備えて輸入者が船会社に一時預け入れる敷金 |
| **Surat Pengantar Pengembalian (EIR Inbound)** | 空コンテナ返却伝票 (EIR) | デポが空コンテナの返却を受け取り、損傷の有無を記録する公式伝票 |
| **Dwelling Time (Waktu Inap Kargo)** | 貨物滞留時間（ドウェリングタイム） | 船からコンテナが降ろされてから税関許可を得て港外へゲートアウトするまでの総日数 |
| **Kongesti Pelabuhan (Port Congestion)** | 港湾混雑・バース待ち | 入港船の殺到やシステム障害により荷役・搬出が麻痺する状態 |

---

## 2. 現場実践対話 (Percakapan Praktis Demurrage & Detention)

### 場面1: 船会社（Shipping Line）への事前フリータイム（Free Time）延長交渉

日系化学メーカーの物流マネージャーが、ジャカルタ税関での化学品検査（Jalur Merah）の遅延リスクに備え、船会社の営業担当者に対しフリータイムを14日間に延長する特約（Special Agreement）を交渉する場面です。

:::id-example
**Logistics Manager (Surya)**: Selamat pagi, Ibu Diana dari Maersk Line. Kami sedang merencanakan pengiriman rutin 20 kontainer bahan kimia khusus dari Tokyo ke Tanjung Priok bulan depan.  
**Shipping Line Rep (Diana)**: Selamat pagi, Pak Surya. Senang sekali mendengar rencana volume tersebut. Apa yang bisa kami bantu untuk kelancaran pengapalannya?  
**Logistics Manager (Surya)**: Karena kargo bahan kimia kami sering kali memerlukan uji laboratorium kepabeanan yang memakan waktu cukup lama, standar masa bebas (*free time*) kombinasi 7 hari yang Anda tawarkan terlalu berisiko terkena biaya *Demurrage*.  
**Shipping Line Rep (Diana)**: Berapa hari masa bebas yang Anda butuhkan untuk profil kargo tersebut?  
**Logistics Manager (Surya)**: Kami mengajukan permohonan fasilitas *Combined Demurrage and Detention Free Time* selama 14 hari di pelabuhan tujuan Jakarta.  
**Shipping Line Rep (Diana)**: Jika perusahaan Anda berkomitmen untuk memesan seluruh 20 kontainer tersebut pada kapal kami, kami bisa menyetujui perpanjangan *free time* menjadi 14 hari kerja. Kami akan masukkan kode persetujuan khusus (*Special Deal ID*) tersebut ke dalam pemesanan (*booking confirmation*) Anda.  
**Logistics Manager (Surya)**: Sangat bagus. Pastikan kode tersebut juga tercantum jelas di lembar konfirmasi B/L dan manifes kedatangan (*Arrival Notice*) agar staf operasional kami di Tanjung Priok tidak ditagih demurrage otomatis oleh sistem kasir Pelindo.
:::

- **uji laboratorium kepabeanan**: 税関化学分析試験
- **Combined Demurrage and Detention**: デマレージ・ディテンション合算フリータイム
- **kode persetujuan khusus (Special Deal ID)**: 特約割引コード
- **sistem kasir Pelindo**: 港湾公社の自動料金支払い窓口システム

---

### 場面2: コンテナ破損（Damage）に伴うディテンション課金トラブルの解決

工場で荷降ろしを終えて空コンテナをデポに返納した際、デポの検査員が床板の油汚れを理由に受領を拒否し、ディテンションの日数カウントが止まらないトラブルを解決する場面です。

:::id-example
**Transport Coordinator (Surya)**: Halo Pak Mandor Depo Marunda, supir trailer kami melaporkan bahwa Anda menolak menerbitkan surat penerimaan kontainer kosong (EIR) untuk kontainer nomor MSKU-88712. Mengapa?  
**Mandor Depo**: Selamat siang, Pak. Kami tidak bisa menerima kontainer ini karena ada noda oli hitam di lantai kayu bagian dalam dan bau menyengat. Harus dibersihkan secara kimia (*chemical washing*) terlebih dahulu oleh pihak penyewa.  
**Transport Coordinator (Surya)**: Tolong diperiksa catatan EIR saat pengambilan kontainer kosong di Pelabuhan Yokohama, Jepang! Di lembar EIR awal sudah tercatat jelas kondisi *remark: existing oil stain on inner floor*. Noda oli itu sudah ada sejak dari Jepang sebelum kami memuat barang mesin kami yang bersih!  
**Mandor Depo**: Coba saya lihat salinan lembar EIR awalnya... Ah, betul, di sini ada stempel dan tanda tangan surveyor Yokohama mengenai noda tersebut.  
**Transport Coordinator (Surya)**: Jadi ini bukan kerusakan atau pencemaran yang disebabkan oleh kami. Tolong segera terbitkan bukti pengembalian (EIR Inbound) sekarang juga per jam dua siang ini agar argo denda *Detention* dari pelayaran otomatis berhenti hari ini!  
**Mandor Depo**: Baik, Pak. Kami mengakui bukti catatan awal tersebut. Saya akan terbitkan lembar tanda terima kontainer kosong tanpa klaim biaya perbaikan (*clean return*).
:::

- **noda oli hitam**: 黒い油シミ・油汚れ
- **chemical washing**: 薬品洗浄
- **EIR awal (initial EIR / outgate EIR)**: 貸出時のコンテナ状態点検票
- **argo denda (fine counter)**: 延滞金メーター・日割りペナルティ計算

---

## 3. 港湾手続き・延滞防止で頻出する実務構文集

### フリータイム管理のフレーズ

- **Berapa hari sisa waktu bebas denda (free time) sebelum kontainer ini dikenakan demurrage?**  
  （このコンテナにデマレージが課されるまで、無料保管期間（フリータイム）の残りは何日ですか？）
- **Argo biaya detention dihitung per hari kalender, termasuk hari Sabtu, Minggu, dan libur nasional.**  
  （ディテンション延滞料は土日祝日を含むカレンダー日ベースで日割り計算されます。）
- **Lakukan pembayaran tarif penumpukan pelabuhan secara elektronik melalui portal autodebit.**  
  （港湾保管料の支払いは口座自動引き落としポータルを通じて電子的に行ってください。）

### 迅速搬出・返却のフレーズ

- **Segera kembalikan kontainer kosong ke depo yang ditunjuk sebelum pukul lima sore.**  
  （午後5時までに指定デポへ空コンテナを速やかに返却してください。）
- **Ajukan permohonan pemeriksaan jalur merah di luar jam kerja (lembur) untuk memangkas dwelling time.**  
  （港湾滞留時間を短縮するため、時間外（残業枠）でのレッドレーン検査申請を行ってください。）

---

> [!IMPORTANT]
> **インドネシア港湾の「累進デマレージ（Tarif Progresif）」の恐怖**  
> インドネシアの港湾ターミナルでは、滞留を解消させるために**保管日数が長くなるほど1日あたりの単価が2倍、3倍へと跳ね上がる累進課金制（Tarif Progresif）**が採用されています。税関手続きが難航して1ヶ月放置されると、コンテナの中身の貨物価格を上回る保管料が請求される「荷捨て（Abandonment）」の事態に陥るため、日々のフリータイム残日数管理は厳格に行いましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 港湾ターミナルからコンテナを搬出せず、無料保管期間（Free Time）を超えてヤード内に放置した場合に課される超過保管料は？</summary>

1. Demurrage (Biaya Keterlambatan Pengambilan)  
2. Uang Lembur  
3. Uang Tip Supir  

**正解: 1**  
**解説**: 港内ヤードにコンテナを引き取らず長居させたことに対する延滞料は「Demurrage（デマレージ）」です。
</details>

<details class="id-quiz">
<summary>Q2. 工場での荷降ろし後、指定されたデポへ空コンテナを返却するのが遅れた場合に船会社から課される延滞料は？</summary>

1. Detention (Biaya Keterlambatan Pengembalian)  
2. Asuransi Jiwa  
3. Pajak Pertambahan Nilai  

**正解: 1**  
**解説**: 港外に持ち出した空コンテナの返納遅延に対するペナルティは「Detention（ディテンション）」です。
</details>
