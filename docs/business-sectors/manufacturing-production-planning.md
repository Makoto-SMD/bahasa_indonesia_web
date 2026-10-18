# B03: 生産計画（Rencana Produksi）とラインタクトタイム管理

製造業の現地工場において、納期遵守（On-Time Delivery: OTD）とコスト削減を達成するためには、綿密な生産計画（**Rencana Produksi**）と製造ラインのタクトタイム（Takt Time）・サイクルタイム（Cycle Time）管理が欠かせません。

日系工場では、需要予測や顧客からの内示注文（forecast）に基づき、月次・週次・日次の計画を立て、現場の稼働率（OEE）やボトルネック工程（bottleneck）の解消に取り組みます。本記事では、生産管理（PPIC: Production Planning and Inventory Control）担当者と製造現場リーダーが交わす実践的な生産進捗管理のインドネシア語を体系的に解説します。

---

## 1. 生産計画・タクトタイムに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **PPIC (Production Planning & Inventory Control)** | 生産管理・在庫管理 | 生産計画の策定と原材料・製品在庫を統括する部門 |
| **rencana produksi bulanan / harian** | 月次 / 日次生産計画 | 受注・需要予測に基づいて日々の生産目標数を定めた計画 |
| **takt time (waktu ketukan)** | タクトタイム | 顧客の購入ペースに合わせて製品1個を製造すべき目標時間 |
| **cycle time (waktu siklus)** | サイクルタイム | 作業者が1個の工程を完了させるのに実際に要する正味時間 |
| **target kapasitas (output per jam)** | 目標生産能力（毎時生産数） | 1時間あたり、または1シフトあたりに達成すべき目標個数 |
| **titik kemacetan (bottleneck)** | ボトルネック工程 | 全工程の中で最も処理時間が長く、全体の生産能力を制約する工程 |
| **efisiensi lini (line balancing)** | ラインバランス効率 | 各工程間の作業時間のばらつきを平準化し、手待ちをなくす指標 |
| **OEE (Overall Equipment Effectiveness)** | 設備総合効率 | 稼働率・性能・良品率を総合した設備の実質稼働効率指標 |
| **waktu henti mesin (downtime / kerugian)** | 設備停止時間（ダウンタイム） | 故障・段取り替え・材料切れ等による計画外のライン停止ロス |
| **waktu pergantian cetakan (changeover / dandori)** | 段取り替え時間 | 金型や治具、品種を切り替えるのに要するセットアップ時間 |
| **kejar target (catch-up / lembur)** | 挽回生産（遅れ回復） | 計画未達分を取り戻すために残業やライン速度を上げて追いつくこと |

---

## 2. 現場実践対話 (Percakapan Praktis Produksi)

### 場面1: 日次生産進捗の未達原因分析とボトルネック対策

夕方の進捗確認ミーティングで、生産管理マネジメントが現場スーパーバイザーに対し、当日の目標個数に対するショート（未達）の理由と対策を問う場面です。

:::id-example
**Manajer PPIC**: Selamat sore, Pak Arif. Bagaimana status pencapaian target produksi Line A hari ini?  
**Supervisor**: Selamat sore, Pak. Sampai pukul empat sore ini, kita baru mencapai 850 unit dari target harian 1.000 unit, jadi masih ada kekurangan 150 unit.  
**Manajer PPIC**: Apa penyebab utama dari selisih (gap) 150 unit tersebut? Apakah ada kerusakan mesin yang signifikan?  
**Supervisor**: Ada *downtime* sekitar 45 menit di Stasiun 4 karena masalah sensor pemotong hidrolik yang macet. Selain itu, Stasiun 2 menjadi *bottleneck* karena operator baru belum terbiasa dengan prosedur penyolderan kabel.  
**Manajer PPIC**: Siklus waktu (cycle time) di Stasiun 2 saat ini berapa detik?  
**Supervisor**: Cycle time aktualnya 48 detik, sedangkan *takt time* yang ditentukan adalah 40 detik. Jadi jalur produksi sering tertahan di sana.  
**Manajer PPIC**: Besok pagi, tolong tempatkan operator senior untuk mendampingi operator baru tersebut, atau seimbangkan beban kerja dengan memindahkan satu langkah kerja ke Stasiun 3.  
**Supervisor**: Baik, Pak. Malam ini kami juga akan menjalankan kerja lembur selama satu jam bersama tim inti untuk menutup kekurangan 150 unit agar pengiriman ke pelanggan lusa tidak tertunda.
:::

- **kekurangan (gap / short)**: 不足、差分
- **waktu henti (downtime)**: 機械停止時間
- **tertahan**: 滞る、引っかかる
- **mendampingi**: 伴走指導する、付き添う

---

### 場面2: 金型段取り替え（Changeover）時間の短縮化カイゼン

多品種少量生産に対応するため、金型交換の段取り時間を30分から15分以内に短縮するSMED（Single-Minute Exchange of Die）の取り組みについて議論する場面です。

:::id-example
**Supervisor**: Pak Manajer, kami telah menganalisis rekaman video proses pergantian cetakan (*dandori*) pada mesin cetak plastik nomor 5.  
**Manajer**: Bagus sekali. Apa temuan terbesar kalian mengenai pemborosan waktu selama pergantian model?  
**Supervisor**: Kami menemukan bahwa teknisi menghabiskan waktu hampir sepuluh menit hanya untuk mencari baut penjepit dan kunci pas khusus di lemari perkakas.  
**Manajer**: Itu adalah contoh klasik *persiapan internal* yang seharusnya bisa dijadikan *persiapan eksternal*.  
**Supervisor**: Tepat sekali, Pak. Kami merancang gerobak dorong khusus (troli setup) yang sudah berisi semua baut, selang pendingin, dan cetakan berikutnya sebelum mesin berhenti.  
**Manajer**: Ide yang sangat cerdas. Dengan begitu, begitu mesin berhenti, cetakan lama langsung dicopot dan cetakan baru siap dinaikkan. Berapa target penghematan waktunya?  
**Supervisor**: Kami yakin bisa memangkas waktu *changeover* dari 32 menit menjadi hanya 12 menit.
:::

- **persiapan internal / eksternal**: 内段取り（機械停止中に行う作業）/ 外段取り（機械稼働中に行う事前準備）
- **troli setup**: 段取り専用台車
- **memangkas waktu**: 時間を大幅に削る・削減する

---

## 3. 生産管理・進捗報告で頻出する実務構文集

### 計画策定・目標指示

- **Target produksi bulan ini ditingkatkan sebesar sepuluh persen dari bulan lalu.**  
  （今月の生産目標は前月比で10パーセント引き上げられました。）
- **Lini perakitan harus beroperasi dengan efisiensi minimal sembilan puluh lima persen.**  
  （組立ラインは最低でも95パーセントの効率で稼働しなければなりません。）
- **Waktu siklus aktual tidak boleh melebihi batas waktu ketukan (takt time).**  
  （実測サイクルタイムはタクトタイムの上限を超えてはなりません。）

### 遅延報告・挽回措置

- **Terjadi keterlambatan pasokan komponen dari pemasok lokal sebanyak dua ratus buah.**  
  （現地サプライヤーからの部品供給に200個の納入遅れが発生しています。）
- **Kita perlu menambah shift malam untuk mengejar pesanan mendesak akhir pekan ini.**  
  （今週末の緊急注文に追いつくため、夜勤シフトを追加する必要があります。）

---

> [!IMPORTANT]
> **ボトルネック改善の基本思想**  
> 「ボトルネック以外の工程をいくら速くしても全体の生産量は増えない（非ボトルネックの過剰在庫が増えるだけ）」というTOC（制約条件の理論）の考え方を現地の現場リーダーに共有することが極めて重要です。余計な仕掛品を作らせず、ボトルネック工程の停止時間をゼロにする支援体制を作りましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 顧客の購入需要ペースに合わせて製品1個を製造すべき「目標時間（タクトタイム）」に相当する概念はどれでしょう？</summary>

1. Lead Time  
2. Takt Time  
3. Overtime  

**正解: 2**  
**解説**: タクトタイム（Takt Time）は稼働可能時間を顧客の必要数量で割って算出する目標ペース時間です。
</details>

<details class="id-quiz">
<summary>Q2. 工場全体の生産能力を制約し、全体のペースを決定づけてしまっている最も遅い工程を何と呼ぶでしょう？</summary>

1. Titik kemacetan (Bottleneck)  
2. Jalur cepat (Fast track)  
3. Bahan penolong (Auxiliary material)  

**正解: 1**  
**解説**: ボトルネック（titik kemacetan）は、ライン全体の最大スループットを制限する工程です。
</details>
