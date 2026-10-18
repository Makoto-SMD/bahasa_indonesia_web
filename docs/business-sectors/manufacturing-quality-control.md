# B04: 不良品（Barang Cacat）の原因分析と再発防止（QC・なぜなぜ分析・ポカヨケ）

製造業において、品質管理（**QC: Quality Control / QA: Quality Assurance**）は顧客の信頼と企業の収益性を直結する生命線です。不良品（**barang cacat / produk reject**）が発生した際、単に不良品を廃棄・手直し（rework）するだけでは根本解決になりません。

日系工場では、「なぜなぜ5回分析（Analisis 5 Why）」、QC7つ道具（フィッシュボーン図・パレート図等）、そして人為的ミスを物理的に防ぐ「ポカヨケ（Poka-Yoke）」の導入が日常的に行われます。本記事では、不良発生時の流出防止（containment）、真因追究（root cause analysis）、恒久対策（corrective action）の実践インドネシア語を体系的に学びます。

---

## 1. 品質管理・不良対策に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **barang cacat / produk reject** | 不良品・リジェクト品 | 寸法、外観、機能が図面や基準値を満たさない不適合品 |
| **tingkat cacat (defect rate / PPM)** | 不良率 (PPM) | 生産総数に対する不良個数の割合（百万分率など） |
| **pengerjaan ulang (rework)** | 手直し・リワーク | 規格外品を加工や修正によって合格品基準に戻す作業 |
| **pemusnahan / scrap** | 廃棄・スクラップ | 手直し不能で再利用できず破棄処分される不良品 |
| **analisis akar masalah (Root Cause Analysis)** | 根本原因分析 | 表層的な現象ではなく、不具合を招いた本質的根本要因を突き止めること |
| **analisis 5 Mengapa (5 Whys Analysis)** | なぜなぜ5回分析 | 「なぜ」を5回繰り返して真の真因に到達する手法 |
| **diagram tulang ikan (Fishbone / Ishikawa)** | フィッシュボーン図（特性要因図） | 4M（Man, Machine, Material, Method）の観点から要因を整理する図 |
| **poka-yoke (pencegah kesalahan)** | ポカヨケ（フールプルーフ） | 逆向きセットや部品入れ忘れ時に機械が作動しない物理的仕組み |
| **tindakan penahanan (containment action)** | 流出防止応急措置 | 不良の疑いがあるロットを直ちに隔離・全数選別する初期対応 |
| **tindakan perbaikan dan pencegahan (CAPA)** | 是正措置および予防措置 | 再発を恒久的に防ぐための手順書改訂や治具改善などの恒久対策 |
| **inspeksi visual / pemeriksaan dimensi** | 目視検査 / 寸法測定 | 傷・バリ・異物混入の確認やノギス・マイクロメーターによる測定 |

---

## 2. 現場実践対話 (Percakapan Praktis Kualitas)

### 場面1: 出荷前検査での傷・寸法不良発覚と緊急隔離対応

品質管理スーパーバイザー（QC Supervisor）が完成品検査でキズ不良の急増を発見し、該当ロットの出荷保留と緊急全数選別を指示する場面です。

:::id-example
**Staff QC**: Pak Supervisor, kami menemukan lonjakan cacat goresan (scratch) dan penyok halus pada casing luar produk model X di stasiun inspeksi akhir.  
**Supervisor QC**: Berapa banyak unit yang terpengaruh, dan berapa persentase tingkat cacatnya saat ini?  
**Staff QC**: Dari 500 unit yang diperiksa pada lot pagi ini, ditemukan 35 unit tergores. Tingkat cacatnya mencapai tujuh persen, jauh melampaui batas toleransi 0,5 persen!  
**Supervisor QC**: Ini sangat kritis! Segera keluarkan instruksi *Hold Lot* (penahanan lot). Jangan biarkan satu kotak pun dimuat ke dalam truk pengiriman ke pelanggan.  
**Staff QC**: Siap, Pak. Semua palet dari Lot 1018A sudah kami tempeli label kuning *Tahanan Kualitas* dan dipindahkan ke area karantina.  
**Supervisor QC**: Bagus. Bentuk tim sortir khusus sekarang juga untuk melakukan inspeksi seratus persen (100% sorting) terhadap stok yang ada di gudang barang jadi.
:::

- **lonjakan (spike / surge)**: 急増、跳ね上がり
- **penyok halus**: 微小なへこみ・打痕
- **penahanan lot (lot hold)**: ロット保留、出荷停止
- **inspeksi seratus persen**: 全数検査、選別作業

---

### 場面2: 「なぜなぜ分析（5 Why）」による真因追究とポカヨケ設計

なぜ金型へのワーク逆向きセットが発生したのか、現場リーダーとエンジニアが「5 Why」を深掘りしてポカヨケ治具を導入する場面です。

:::id-example
**Manajer QC**: Mengapa komponen ini bisa terpotong dalam posisi terbalik di Mesin Press 3?  
**Leader Produksi**: (Why 1) Karena operator meletakkan lembaran logam secara terbalik di dalam cetakan.  
**Manajer QC**: Mengapa operator bisa meletakkannya terbalik?  
**Leader Produksi**: (Why 2) Karena bentuk sisi kiri dan kanan komponen ini hampir simetris dan sangat mirip secara visual.  
**Manajer QC**: Mengapa operator tidak memeriksa lubang penunjuk (guide hole) sebelum menekan tombol start?  
**Leader Produksi**: (Why 3) Karena penerangan di stasiun tersebut agak redup dan operator merasa lelah di akhir shift.  
**Manajer QC**: Mengapa kita mengandalkan kehati-hatian manusia pada bentuk yang rentan salah seperti itu? Mengapa tidak ada mekanisme *Poka-Yoke*?  
**Leader Produksi**: (Why 4) Karena cetakan lama ini memang tidak dilengkapi pin pemandu fisik (locator pin) asimetris.  
**Manajer QC**: Baik! Akar masalahnya adalah ketiadaan pencegah kesalahan fisik. Solusinya bukan sekadar memperingatkan operator, melainkan memodifikasi cetakan dengan memasang pin penahan sehingga komponen tidak bisa masuk jika posisinya terbalik.  
**Leader Produksi**: Sangat setuju, Pak. Tim perkakas (tooling) akan memasang pin tersebut sore ini juga agar mustahil terjadi kesalahan serupa.
:::

- **posisi terbalik**: 逆向き、裏返し
- **hampir simetris**: ほぼ左右対称
- **pin pemandu (locator pin)**: 位置決めピン
- **akar masalah**: 根本原因（root cause）

---

## 3. 品質管理で頻出する指示・報告フレーズ集

### 是正要求・流出防止

- **Segera lakukan isolasi terhadap seluruh barang yang diproduksi kemarin.**  
  （昨日生産されたすべての製品を直ちに隔離してください。）
- **Buat laporan ketidaksesuaian produk (Non-Conformance Report / NCR).**  
  （不適合品報告書（NCR）を作成してください。）
- **Cari tahu faktor penyebab utama berdasarkan prinsip 4M: Manusia, Mesin, Material, dan Metode.**  
  （4M（人、機械、材料、方法）の原則に基づいて主因を突き止めてください。）

### 恒久対策・標準化

- **Modifikasi cetakan ini dengan mekanisme poka-yoke untuk mencegah salah pasang.**  
  （誤組み付けを防止するため、この金型にポカヨケ機構を追加改造してください。）
- **Perbarui Standar Operasional Prosedur (SOP) dan lakukan pelatihan ulang untuk semua operator.**  
  （標準作業手順書（SOP）を改訂し、全作業員に対して再教育を実施してください。）

---

> [!TIP]
> **「人のせい」にしない品質管理**  
> 不良が発生した際、初心者の管理者は「作業員の不注意（kelalaian operator）」を原因にして注意・叱責で終わらせがちです。しかし日系工場の真の強みは「人間は誰でもミスをする」という前提に立ち、ミスが物理的に不可能な治具（Poka-Yoke）や自動検査センサーを構築することにあります。現地スタッフにもこの哲学を教え込みましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 作業員の不注意や疲労による誤組み付けを、物理的・機械的な仕組みで未然に防止する設計手法はどれでしょう？</summary>

1. Poka-yoke  
2. Overtime  
3. FIFO  

**正解: 1**  
**解説**: 日本発祥で世界標準用語となった「ポカヨケ（poka-yoke）」は、エラー防止・フールプルーフの代名詞です。
</details>

<details class="id-quiz">
<summary>Q2. 不良品が発生した際、問題の真因に到達するために質問を繰り返す手法を何と呼ぶでしょう？</summary>

1. Analisis 5 Mengapa (5 Whys Analysis)  
2. Analisis SWOT  
3. Analisis Biaya  

**正解: 1**  
**解説**: 「Mengapa（なぜ）」を繰り返して表層的要因から根本原因を突き止めるのが「なぜなぜ分析」です。
</details>
