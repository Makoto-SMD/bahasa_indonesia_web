# B49: 為替リスクヘッジ（Hedging）と中央銀行（BI）外為規制実務

新興国通貨であるインドネシア・ルピア（IDR）は、米国の金利政策、世界的な資源価格、新興国市場の資金フローによって為替変動（Volatilitas Kurs）が激しくなりやすい特性を持っています。

現地で巨額の外貨建て原材料輸入や日本親会社からの外貨借入（Utang Luar Negeri / ULN）を抱える日系企業にとって、為替変動リスクを回避する**ヘッジ取引（Lindung Nilai / Hedging）**と、**インドネシア中央銀行（Bank Indonesia - BI）**が定める厳格な外為規制の遵守は財務管理の生命線です。

中央銀行規則（PBI: Peraturan Bank Indonesia）では、**「インドネシア国内取引におけるルピア使用義務（Kewajiban Penggunaan Rupiah）」**、一定額以上の外貨購入時における**基礎的取引（Underlying Transaction）書類の提出義務**、および民間非銀行企業の外貨債務に対する**ヘッジ比率・流動性比率の規制（Rasio Lindung Nilai & KPP）**が課されています。本記事では、為替先渡取引（Forward）、為替スワップ（Swap）、中銀への対外債務報告（Laporan ULN）に関する実務インドネシア語を体系的に解説します。

---

## 1. 為替ヘッジ・中央銀行外為規制に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Lindung Nilai (Hedging)** | 為替ヘッジ（リスク回避取引） | 為替レートの急激な変動損失を防ぐため、将来の交換レートをあらかじめ固定・約定する金融取引 |
| **Transaksi Forward / Swap** | 先渡為替取引 (Forward) / 為替スワップ (Swap) | 将来の特定日に決めたレートで受渡を行う取引 / 直物と先物を組み合わせて資金を融通する取引 |
| **Kewajiban Penggunaan Rupiah (UU No. 7/2011)** | ルピア使用義務法 | インドネシア領土内で行われる現金・非現金の全国内取引においてルピア決済を強制する法律 |
| **Transaksi yang Mendasari (Underlying Transaction)** | 基礎的取引（アンダーライング取引） | 投機目的の外貨買いを防ぐため、商業インボイスや借入契約書など実需の証明書類を提示する規則 |
| **Bank Indonesia (BI)** | インドネシア中央銀行 | ルピア通貨の安定、金融システム規制、外為マクロプルーデンス政策を統括する独立中央銀行 |
| **Utang Luar Negeri (ULN / Foreign Debt)** | 対外債務（外貨借入金） | 非居住者（日本の親会社や海外銀行）から調達した外貨建ての中長期借入金 |
| **Rasio Lindung Nilai (Hedging Ratio)** | 最低ヘッジ比率規制 | 満期6ヶ月以内の対外外貨純債務に対し、最低20%以上のヘッジ取引を義務付ける中銀規制 |
| **Rasio Kecukupan Likuiditas (KPP / Liquidity Ratio)** | 外貨流動性充足比率 | 満期3ヶ月以内の外貨支払債務に対し、最低70%の外貨流動資産の保有を義務付ける規制 |
| **Laporan ULN dan KPP (BI Reporting)** | 対外債務・健全性比率報告書 | 毎月オンライン（sistem Si-MOLEK / BI-ETR）で中央銀行へ提出する借入・ヘッジ実績報告 |
| **DHE (Devisa Hasil Ekspor)** | 輸出代金外貨留保規制 | 天然資源（SDA）輸出企業が獲得した外貨代金を国内銀行へ最低3ヶ月間留保させる義務 |

---

## 2. 現場実践対話 (Percakapan Praktis Lindung Nilai Valas)

### 場面1: ドル建て機械輸入に対する銀行との為替予約（Forward Contract）締結

日系製造業の財務マネージャー（Treasury Manager）が、提携外資系銀行のディーラーと、3ヶ月後に決済予定の輸入代金200万米ドルの為替先渡契約（Forward）を約定する場面です。

:::id-example
**Treasury Manager (Irfan)**: Halo Pak Budi dari Corporate Treasury Bank BTMU. Perusahaan kami memiliki kewajiban pembayaran tagihan impor mesin pabrik sebesar 2 juta dolar AS yang akan jatuh tempo dalam waktu 90 hari ke depan (tanggal 25 Januari 2027).  
**Bank FX Dealer (Budi)**: Halo Pak Irfan. Melihat tren penguatan dolar AS akhir-akhir ini, melakukan lindung nilai (*hedging*) dengan kontrak forward sangat kami sarankan untuk mengunci biaya produksi Anda. Berapa kurs spot pasar saat ini yang ingin Anda jadikan acuan?  
**Treasury Manager (Irfan)**: Kurs spot saat ini berada di level 15.600 rupiah per dolar AS. Berapa kuotasi kurs forward 3 bulan (*3-month forward rate*) yang bisa bank tawarkan kepada kami?  
**Bank FX Dealer (Budi)**: Berdasarkan selisih suku bunga pasar uang rupiah dan dolar AS, kami dapat memberikan kuotasi forward 90 hari di level 15.750 rupiah per dolar AS.  
**Treasury Manager (Irfan)**: Kurs tersebut masuk dalam batas toleransi anggaran biaya kami. Kami sepakat untuk mengunci kurs di 15.750 untuk nominal 2 juta dolar AS.  
**Bank FX Dealer (Budi)**: Baik, kesepakatan (*deal*) telah tercatat. Sebagai syarat kepatuhan Peraturan Bank Indonesia (PBI) mengenai transaksi valuta asing terhadap rupiah, mohon segera unggah dokumen yang mendasari (*underlying document*) berupa salinan Commercial Invoice, Kontrak Pembelian Mesin, dan Formulir PIB ke portal perbankan kami sebelum pukul empat sore ini.  
**Treasury Manager (Irfan)**: Seluruh dokumen pendukung asli sudah kami siapkan dan akan kami unggah dalam waktu tiga puluh menit ke depan.
:::

- **jatuh tempo**: 満期を迎える、支払期日が到来する
- **mengunci biaya (lock-in cost)**: コストを固定・ロックする
- **kuotasi kurs forward**: 先渡為替レートの提示（クオート）
- **dokumen yang mendasari (underlying documents)**: 実需裏付け書類

---

### 場面2: 親会社からの親子ローンに対する中央銀行（BI）対外債務（ULN）報告実務

日本親会社から設備投資資金として500万米ドルの低利融資（Intra-Group Loan）を受けた現地法人が、中銀規則に基づき月次報告書（Laporan ULN）をオンライン提出する場面です。

:::id-example
**Finance Director (Tanaka)**: Bu Sari, pinjaman modal pemegang saham (*shareholder loan*) sebesar lima juta dolar AS dari Tokyo sudah masuk ke rekening giro khusus kita di Bank Mandiri minggu lalu. Apakah tim Anda sudah melaporkannya ke Bank Indonesia?  
**Treasury Specialist (Sari)**: Sedang kami proses pelaporannya, Pak Tanaka. Menurut Peraturan Bank Indonesia, setiap penandatanganan perjanjian Utang Luar Negeri (ULN) baru wajib dilaporkan ke sistem Bank Indonesia paling lambat tanggal 15 bulan berikutnya setelah penandatanganan kontrak pinjaman.  
**Finance Director (Tanaka)**: Apa saja parameter rasio kepatuhan yang harus kita penuhi dalam laporan tersebut?  
**Treasury Specialist (Sari)**: Kita harus memenuhi dua rasio kehati-hatian (*prudential principles*):  
1. **Rasio Kecukupan Likuiditas**: Kita wajib membuktikan memiliki aset valas lancar minimal 70 persen untuk menutup utang yang jatuh tempo dalam 3 bulan.  
2. **Peringkat Utang (Credit Rating)**: Karena pinjaman ini murni dari induk perusahaan (parent loan) dan bukan dari bank komersial pihak ketiga, kita dibebaskan dari kewajiban memiliki rating kredit independen.  
**Finance Director (Tanaka)**: Bagus sekali. Jangan sampai kita terlambat mengirimkan laporan bulanan ini, karena keterlambatan lapor dikenakan denda administratif harian dari Bank Indonesia.  
**Treasury Specialist (Sari)**: Siap, Pak. Semua berkas kontrak pinjaman dan bukti konfirmasi penarikan dana (*drawdown confirmation*) sudah selesai diinput ke sistem pelaporan online BI hari ini.
:::

- **pinjaman pemegang saham (shareholder loan)**: 株主ローン・親子間融資
- **rasio kehati-hatian (prudential principles)**: 健全性原則比率
- **penarikan dana (drawdown)**: 融資の実行・資金引き出し
- **denda administratif harian**: 日割りの行政過料・遅延ペナルティ

---

## 3. 外為・為替管理で頻出する実務構文集

### ルピア決済・法令遵守

- **Setiap transaksi yang dilakukan di wilayah Negara Kesatuan Republik Indonesia wajib menggunakan Rupiah.**  
  （インドネシア共和国領域内で行われるすべての取引はルピアを使用する義務があります。）
- **Pembelian valuta asing terhadap Rupiah di atas seratus ribu dolar AS per bulan wajib memiliki dokumen underlying.**  
  （月間10万米ドルを超える対ルピア外貨購入には基礎的実需書類（Underlying）の提出が義務付けられます。）
- **Klausul harga dalam kontrak sewa kantor di Jakarta tidak boleh dicantumkan dalam mata uang asing.**  
  （ジャカルタのオフィス賃貸契約における価格条項は外貨建てで記載してはなりません。）

### ヘッジ・対外債務報告

- **Perusahaan wajib melakukan transaksi lindung nilai untuk memitigasi risiko kerugian selisih kurs.**  
  （企業は為替差損リスクを軽減するため、ヘッジ取引を行う義務があります。）
- **Laporan penarikan Utang Luar Negeri (ULN) wajib disampaikan secara berkala melalui sistem Bank Indonesia.**  
  （対外借入金（ULN）の実行報告は中央銀行のシステムを通じて定期提出しなければなりません。）

---

> [!IMPORTANT]
> **「ルピア使用義務法（UU Mata Uang）」の絶対原則**  
> インドネシア国内の企業間取引（国内仕入、国内運賃、家賃、給与等）において、**米ドル等の外貨建てで契約書を作成したり、外貨決済を行うことは法律違反（UU No. 7/2011）**となります。違反企業には最高2億ルピアの罰金や刑事罰、銀行口座凍結が科されるため、国内の支払いはすべてルピア建てに一本化する体制を厳守しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 為替レートの急激な変動による損失を未然に防ぐため、将来の交換レートを固定する金融取引（ヘッジ）を表すインドネシア語は？</summary>

1. Lindung Nilai (Hedging)  
2. Surat Peringatan  
3. Beli Putus  

**正解: 1**  
**解説**: 為替ヘッジ取引はインドネシア語で「Lindung Nilai（英語: Hedging）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 投機目的の外貨買いを防止するため、外貨購入時に銀行へ提示が義務付けられる「商業インボイス等の実需証明」を表す用語は？</summary>

1. Transaksi yang Mendasari (Underlying Transaction)  
2. Transaksi Spekulasi  
3. Tiket Pesawat  

**正解: 1**  
**解説**: 外貨購入の正当な商業的実需を証明する取引は「Transaksi yang Mendasari（Underlying Transaction）」と呼ばれます。
</details>
