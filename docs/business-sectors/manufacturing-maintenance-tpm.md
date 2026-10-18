# B05: 生産設備の定期保守点検（Maintenance）と突発故障対応（TPM・予防保全）

製造ラインの安定稼働は、保全部門（**Departemen Maintenance / Perawatan Mesin**）の技術力と計画的な保全活動によって支えられています。

設備が突発停止（**kerusakan mendadak / breakdown**）すると、生産ライン全体がストップし、納期遅延や多大な損害が発生します。そのため、日系製造業では事後保全（Corrective Maintenance）から、計画的な予防保全（**Preventive Maintenance: PM**）や全社的設備保全（**TPM: Total Productive Maintenance**）、自主保全（Autonomous Maintenance）への移行が徹底されます。

本記事では、日常点検、定期オーバーホール、予備部品（Spare Parts）管理、突発故障発生時のトラブルシューティングに関する実務インドネシア語を体系的に解説します。

---

## 1. 設備保全・メンテナンスに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **perawatan preventif (Preventive Maintenance - PM)** | 予防保全 | 故障を未然に防ぐため、定期的な点検・給油・部品交換を行う保全 |
| **perawatan korektif (Corrective Maintenance)** | 事後保全 | 設備が故障・機能停止した後に修理・復旧させる活動 |
| **pemeliharaan mandiri (Autonomous Maintenance / Jishu Hozen)** | 自主保全 | オペレーター自身が日常点検、清掃・給油、小異変の発見を行う活動 |
| **kerusakan mendadak (breakdown / failure)** | 突発故障・ブレークダウン | 予期せぬ機器の停止や機能喪失 |
| **pembongkaran total (overhaul)** | オーバーホール・全分解点検 | 機械を完全に分解・洗浄・摩耗部品交換し、初期性能に戻す作業 |
| **suku cadang (spare part)** | 予備部品・スペアパーツ | ベアリング、ベルト、Oリング、ヒューズ等、交換用の常備部品 |
| **pelumasan / oli / gemuk (grease)** | 給油・潤滑 / オイル / グリース | 摺動部の摩耗や摩擦熱を防ぐための潤滑剤充填 |
| **getaran abnormal / kebisingan** | 異常振動 / 異音 | ベアリングのガタつきや偏心を示す故障予兆シグナル |
| **kebocoran oli / udara (air leak)** | 油漏れ / エアー漏れ | 配管継ぎ手やパッキンの劣化による圧力損失・油圧低下 |
| **MTBF (Mean Time Between Failures)** | 平均故障間隔 | 設備が故障してから次の故障が発生するまでの平均稼働時間 |
| **MTTR (Mean Time To Repair)** | 平均修復時間 | 故障発生から修理完了・運転再開までに要する平均修復時間 |
| **daftar periksa harian (checklist)** | 日常点検チェックシート | 始業前・終業時に作業員が点検項目をチェックする帳票 |

---

## 2. 現場実践対話 (Percakapan Praktis Maintenance)

### 場面1: 稼働中モーターの異音・発熱発見と緊急停止措置

ライン巡回中の保全技術者（Teknisi Maintenance）が、コンベア駆動モーターからの異常振動と異音に気づき、現場リーダーへ連絡する場面です。

:::id-example
**Teknisi**: Pak Leader, tolong hentikan konveyor jalur 1 sebentar. Saya mendeteksi bunyi dengung yang tidak wajar dan getaran kasar pada motor penggerak utama.  
**Leader**: Ada masalah apa, Mas? Apakah bantalannya (bearing) yang rusak?  
**Teknisi**: Tepat sekali, suaranya terdengar seperti gesekan logam berat. Saya juga baru mengecek suhu rumahan motor dengan termometer inframerah, suhunya sudah mencapai 90 derajat Celsius, jauh di atas batas aman 60 derajat!  
**Leader**: Kalau motor ini terbakar di tengah jalan, seluruh perakitan bisa lumpuh setengah hari. Berapa lama waktu yang dibutuhkan untuk mengganti bantalannya?  
**Teknisi**: Kami memiliki stok bantalan cadangan ukuran standar di gudang suku cadang. Jika kita ganti sekarang, butuh waktu sekitar 40 menit.  
**Leader**: Baik, segera ambil suku cadangnya. Saya akan alihkan operator untuk melakukan pembersihan 5R sambil menunggu jalur siap kembali.
:::

- **bunyi dengung**: うなり音、異音（humming noise）
- **bantalan (bearing)**: ベアリング、軸受
- **termometer inframerah**: 赤外線温度計
- **lumpuh**: 麻痺する、ストップする

---

### 場面2: 月次予防保全（PM）計画と予備品在庫の確認

保全部門のマネージャーが技術者に対し、週末に実施予定の大型プレス機械の予防保全項目とパッキン類の在庫手配を確認する場面です。

:::id-example
**Manajer**: Bagaimana kesiapan tim kita untuk jadwal perawatan preventif (PM) bulanan hari Sabtu besok?  
**Supervisor Maintenance**: Rencana kerja sudah matang, Pak. Kita akan melakukan overhaul pompa hidrolik, penggantian oli filter, dan kalibrasi sensor tekanan pada Mesin Press 4 dan 5.  
**Manajer**: Apakah semua suku cadang kritis sudah tersedia? Terutama seal karet silinder dan oli pelumas khusus ISO VG 46?  
**Supervisor Maintenance**: Semua suku cadang sudah kami terima dari pemasok kemarin sore. Minyak pelumas dan filter juga sudah siap di dekat mesin.  
**Manajer**: Pastikan teknisi mematuhi prosedur keselamatan kerja saat membuka jalur pipa bertekanan tinggi. Jangan lupa buang sisa tekanan hidrolik sebelum membuka baut!  
**Supervisor Maintenance**: Siap, Pak. Form Izin Kerja Berbahaya (Permit to Work) sudah ditandatangani dan prosedur LOTO akan dipasang penuh.
:::

- **kalibrasi sensor**: センサーの校正・キャリブレーション
- **seal karet silinder**: シリンダーゴムパッキン・オイルシール
- **pipa bertekanan tinggi**: 高圧配管
- **Izin Kerja Berbahaya (Permit to Work)**: 危険作業許可証

---

## 3. 保全業務で頻出する指示・報告フレーズ集

### 点検・診断のフレーズ

- **Lakukan pengecekan level oli mesin sebelum menyalakan daya.**  
  （電源を入れる前に、機械のオイルレベル点検を行ってください。）
- **Tekanan udara kompresor turun drastis, periksa apakah ada selang yang bocor.**  
  （コンプレッサーのエアー圧力が急低下しています。ホースの破れやエアー漏れがないか調べてください。）
- **Kencangkan kembali baut-baut penahan yang longgar akibat getaran mesin.**  
  （機械の振動によって緩んだ固定ボルトを増し締めしてください。）

### 予防保全・予備品管理

- **Kuras dan ganti oli transmisi ini setiap enam bulan sekali.**  
  （このトランスミッションオイルは6ヶ月ごとに全量抜き取って交換してください。）
- **Jumlah stok minimum untuk sabuk V-belt ini harus dijaga sebanyak lima buah.**  
  （このVベルトの最低予備在庫数は5本を維持しなければなりません。）

---

> [!IMPORTANT]
> **「清掃は点検なり（Membersihkan adalah Memeriksa）」**  
> 自主保全（Jishu Hozen）の核心は、オペレーター自身が自分の使う機械を雑巾で拭くことにあります。手で機械を拭くことで、「ボルトの緩み」「油のにじみ」「異常な熱」「かすかな異音」など、重大故障につながる初期の微欠陥（cacat mikro）を五感で察知できるようになります。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 機械が故障する前に、定期的な点検や部品交換を行ってトラブルを未然に防ぐ保全方式はどれでしょう？</summary>

1. Perawatan Korektif (Breakdown Maintenance)  
2. Perawatan Preventif (Preventive Maintenance)  
3. Perbaikan Darurat  

**正解: 2**  
**解説**: 計画的にトラブルを未然防止する保守点検手法を「予防保全（Perawatan Preventif）」と呼びます。
</details>

<details class="id-quiz">
<summary>Q2. 工場の機械修理に必要なベアリングやベルトなどの「予備交換部品」を指すインドネシア語は？</summary>

1. Bahan mentah  
2. Suku cadang  
3. Alat tulis  

**正解: 2**  
**解説**: 予備部品・交換パーツはインドネシア語で「suku cadang（または spare part）」と呼ばれます。
</details>
