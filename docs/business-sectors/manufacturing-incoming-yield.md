# B07: 原材料受入検査（Incoming Inspection）と歩留まり（Yield）管理

製造原価の低減と最終製品の品質保証において、サプライヤーから納入される資材を水際でチェックする**原材料受入検査（Incoming Quality Control: IQC / Pemeriksaan Bahan Baku Masuk）**と、投入した原材料がどれだけ良品として完成したかを示す**歩留まり率（Yield / Tingkat Hasil Guna）**は最重要管理指標です。

万一、粗悪な原材料が受入検査をすり抜けてラインに投入されると、大量の仕掛品不良や金型破損、ライン停止を引き起こし、工場に甚大な損失をもたらします。

本記事では、抜取検査基準（AQL: Acceptable Quality Level）、検査成績書（CoA: Certificate of Analysis）の照合、歩留まり悪化時の原因究明、サプライヤーへの受入拒否（Reject）通知に関する実務インドネシア語を体系的に解説します。

---

## 1. 受入検査・歩留まり管理に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **IQC (Incoming Quality Control)** | 受入品質検査 | サプライヤーから工場に届いた原材料・部品を検査する工程 |
| **pemeriksaan penerimaan barang** | 資材受入検査 | 納品伝票との照合、外観・寸法・材質の受入検査 |
| **CoA (Certificate of Analysis)** | 検査成績書・成分分析表 | ロットごとにメーカーが保証する化学成分や物性の測定証明書 |
| **tingkat hasil guna (Yield / Rendemen)** | 歩留まり率（イールド） | 投入原料に対して最終的に得られた良品の割合（歩留まり） |
| **pengambilan sampel (sampling)** | 抜取サンプリング | 全数ではなく、ロットから統計的に一定数を抜き取って検査する手法 |
| **AQL (Acceptable Quality Level)** | 合格品質水準 | 抜取検査において許容される最大の不良率基準（例: AQL 0.65） |
| **penolakan barang (Reject / Return)** | 返品・受入拒否 | 基準を満たさず不合格となったロットを納入業者へ突き返すこと |
| **penyimpangan spesifikasi (deviation)** | 規格外れ・仕様逸脱 | 図面や発注書に指定された公差・数値を外れている状態 |
| **kehilangan bahan (material loss / scrap)** | 材料ロス・歩留まり損失 | 切削粉、端材、スプルー・ランナーなど製造工程で生じる材料の削りかす |
| **klaim pemasok (supplier claim)** | サプライヤー求償・クレーム | 不良部品による損害や選別費用を納入元へ請求すること |
| **persetujuan khusus (concession / derosiasi)** | 特採（特別採用） | 性能上影響がない微小な規格外れを、設計・品証の特別承認で使うこと |

---

## 2. 現場実践対話 (Percakapan Praktis IQC)

### 場面1: 納入樹脂ペレットの含水率異常と受入拒否（Reject）

受入検査担当者（Staff IQC）が納入されたプラスチック成形用原料の分析を行い、水分率が基準を超えているため受入拒否を上司に上申する場面です。

:::id-example
**Staff IQC**: Pak Supervisor, kami baru saja menyelesaikan pengujian sampel dari 20 karung biji plastik resin ABS yang dikirim PT Cahaya Polymer.  
**Supervisor IQC**: Bagaimana hasilnya? Apakah data pengujian sesuai dengan Certificate of Analysis (CoA) yang mereka lampirkan?  
**Staff IQC**: Di CoA tertulis kadar air (moisture content) 0,02 persen, tetapi hasil uji laboratorium kami menggunakan moisture analyzer menunjukkan angka 0,15 persen!  
**Supervisor IQC**: Angka itu hampir delapan kali lipat dari batas toleransi kita. Jika bahan sebasah ini dimasukkan ke mesin injeksi, produk akhir pasti akan mengalami cacat gelembung udara (silver streak).  
**Staff IQC**: Betul, Pak. Selain itu, kami melihat ada beberapa karung yang sobek dan terkena percikan air hujan saat pengangkutan truk mereka.  
**Supervisor IQC**: Tolong terbitkan Surat Penolakan Bahan Baku (Reject Notice) sekarang juga. Beri tanda segel merah pada seluruh palet tersebut dan instruksikan bagian gudang untuk meminta vendor segera menarik barangnya hari ini dan mengirimkan barang pengganti.
:::

- **biji plastik resin**: プラスチック樹脂ペレット
- **moisture analyzer**: 水分計・加熱乾燥式水分測定器
- **cacat gelembung udara (silver streak)**: シルバーストリーク（成形品の銀条・気泡痕）
- **Surat Penolakan Bahan Baku**: 原材料受入拒否通知書

---

### 場面2: プレス加工ラインにおける歩留まり率悪化の検討会

生産技術エンジニアと工場長が、鋼板打ち抜きラインの歩留まり率が88%から82%へ低下した原因と、レイアウト（ネスティング）改善を議論する場面です。

:::id-example
**Manajer Pabrik**: Kenapa tingkat hasil guna (yield) untuk pemotongan lembaran baja bulan ini merosot sampai 82 persen? Kita kehilangan banyak bahan mentah menjadi rongsokan (scrap).  
**Insinyur**: Kami telah melakukan audit pada pola pemotongan (nesting) di mesin laser cutting, Pak.  
**Manajer Pabrik**: Apa yang kalian temukan? Apakah jarak antar-komponen terlalu lebar?  
**Insinyur**: Benar, Pak. Karena ada perubahan sedikit pada sudut tekukan komponen, programmer menambah margin jarak antar-potongan dari 5 mm menjadi 12 mm untuk menghindari panas berlebih.  
**Manajer Pabrik**: Jarak 12 mm itu terlalu boros! Bahan baku baja gulungan (coil) harganya sedang melambung tinggi di pasar internasional.  
**Insinyur**: Kami sudah mendesain ulang tata letak pola potong dengan optimasi perangkat lunak CAD/CAM baru. Margin bisa ditekan kembali menjadi 6 mm dengan menerapkan pendinginan gas nitrogen.  
**Manajer Pabrik**: Berapa proyeksi pemulihan yield-nya?  
**Insinyur**: Dengan pola baru ini, yield akan pulih kembali ke 89,5 persen, dan kita bisa menghemat sekitar 40 juta rupiah per bulan dari pengurangan limbah besi.
:::

- **merosot**: 急激に下がる、低落する
- **rongsokan (scrap)**: クズ鉄、スクラップ
- **pola pemotongan (nesting)**: 板取りパターン（ネスティング）
- **baja gulungan (coil)**: コイル鋼板

---

## 3. 受入検査・歩留まり改善で頻出する実務構文集

### 検査・受入合否判定

- **Lakukan pengambilan sampel secara acak berdasarkan tabel standar AQL.**  
  （AQL規格表に基づいて無作為（ランダム）サンプリングを実施してください。）
- **Batch ini tidak lolos uji kekerasan material (hardness test).**  
  （このバッチは材料硬度試験に不合格となりました。）
- **Apakah kita bisa mengajukan izin konsesi (special concession) untuk cacat warna ini?**  
  （この色ムラについて特別採用（コンセッション・特採）の申請を行うことはできますか？）

### 歩留まり・ロス改善

- **Tingkat rendemen proses pencetakan harus mencapai minimal sembilan puluh persen.**  
  （成形プロセスの歩留まり率は最低でも90パーセントに達しなければなりません。）
- **Kurangi pemborosan bahan baku dengan memanfaatkan sisa potongan lembaran logam.**  
  （金属板の端材を再利用して、原材料のムダを削減してください。）

---

> [!TIP]
> **特採（Concession / Derogasi）の運用規律**  
> 納期が迫っているからといって現場判断で安易に特採を通すと、後工程で重大な不良を引き起こす原因になります。特採を認める場合は、必ず「品質保証責任者の書面承認」を取り、対象ロット番号を生産履歴（トラッカビリティ）に記録しておくルールを厳守しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. サプライヤーが納入ロットごとに添付する、化学成分や物性の品質保証データを記載した証明書（検査成績書）の略称は？</summary>

1. CoA (Certificate of Analysis)  
2. B/L (Bill of Lading)  
3. SOP (Standard Operating Procedure)  

**正解: 1**  
**解説**: 検査成績書・成分分析証明書は英語の略称「CoA（Certificate of Analysis）」として広く用いられます。
</details>

<details class="id-quiz">
<summary>Q2. 投入した総原材料に対して、最終的に得られた良品製品の割合（歩留まり率）を表す用語はどれでしょう？</summary>

1. Tingkat hasil guna / Yield  
2. Waktu siklus (Cycle time)  
3. Biaya lembur (Overtime cost)  

**正解: 1**  
**解説**: 歩留まり率は「Yield」またはインドネシア語で「tingkat hasil guna / rendemen」と呼ばれます。
</details>
