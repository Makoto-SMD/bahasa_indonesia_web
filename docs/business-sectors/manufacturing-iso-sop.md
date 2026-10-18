# B06: ISO 9001/14001 監査対応と標準作業手順書（SOP）の遵守

インドネシアの製造工場において、グローバルサプライチェーンへの参入や大手顧客との取引維持に不可欠なのが、品質マネジメントシステム（**ISO 9001**）および環境マネジメントシステム（**ISO 14001**）の認証取得と維持です。

外部審査機関によるサーベイランス審査や、社内の内部品質監査（Internal Quality Audit）、顧客監査（Audit Pelanggan）では、現場作業員が**標準作業手順書（SOP: Standar Operasional Prosedur）**通りに作業を行っているか、計測機器の校正（Kalibrasi）が切れていないか、不適合（Temuan Ketidaksesuaian / Non-Conformity）に対する是正処置要求（CAR）が適切にクローズされているかが厳格にチェックされます。

本記事では、監査準備、現場質問対応、不適合是正に関する実務インドネシア語を体系的に解説します。

---

## 1. ISO 監査・SOP に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **SOP (Standar Operasional Prosedur)** | 標準作業手順書 | 作業の目的、順序、安全上の注意、使用工具を定めた公認文書 |
| **Instruksi Kerja (Work Instruction - WI)** | 作業指示書・作業標準 | SOPよりさらに具体的で、ステーションごとに掲示される手元手順書 |
| **Audit Internal / Audit Eksternal** | 内部監査 / 外部審査 | 自社監査員による定期チェック / 認証機関（TUV, SGS等）による公式審査 |
| **temuan ketidaksesuaian (Non-Conformity - NC)** | 不適合（指摘事項） | ISO規格や自社規程、SOPの要求事項を満たしていない状態 |
| **ketidaksesuaian mayor / minor** | 重大な不適合 / 軽微な不適合 | システム全体の崩壊につながる欠陥 / 孤立した手続き上の軽微な不備 |
| **rekomendasi perbaikan (Opportunity for Improvement)** | 観察事項・改善の機会 (OFI) | 不適合ではないが、将来の不具合を防ぐために改善が推奨される事項 |
| **Tindakan Korektif (Corrective Action Request - CAR)** | 是正処置要求 (CAR) | 不適合の根本原因を特定し、再発防止策を講じて報告する公的プロセス |
| **pengendalian dokumen (Document Control)** | 文書管理 | 手順書の版数（revision number）、承認印、旧版回収を管理する仕組み |
| **kedaluwarsa dokumen (obsolete document)** | 旧版・無効文書 | 改訂によって効力を失った文書（現場に残ると重大不適合になる） |
| **bukti objektif (objective evidence)** | 客観的証拠 | 記録帳票、写真、データログなど、監査員に提示する検証可能な事実 |
| **kalibrasi alat ukur (tool calibration)** | 計測器の校正 | ノギス、トルクレンチ等の精度を国家標準に照らして定期検証する手続き |

---

## 2. 現場実践対話 (Percakapan Praktis Audit ISO)

### 場面1: 監査員による現場オペレーターへのヒアリング

外部ISO審査員（Auditor）が組立ラインの作業員に対し、手順書の所在と測定機器の校正ステッカーを確認する場面です。

:::id-example
**Auditor**: Selamat siang. Boleh saya tahu nama Anda dan tugas apa yang sedang Anda kerjakan di stasiun ini?  
**Operator**: Selamat siang, Pak. Nama saya Rian, saya bertugas melakukan pengetatan baut penyangga dengan kunci torsi (torque wrench).  
**Auditor**: Baik, Mas Rian. Bagaimana Anda tahu nilai torsi yang tepat untuk baut ini? Apakah ada panduan tertulisnya?  
**Operator**: Ya, ada, Pak. Di depan saya terpasang Instruksi Kerja (IK) nomor IK-ASM-04 rev 3. Di situ tertulis nilai torsi standarnya adalah 25 Newton-meter plus minus satu.  
**Auditor**: Bagus sekali. Boleh saya periksa kunci torsi yang sedang Anda gunakan?  
**Operator**: Silakan, Pak.  
**Auditor**: Saya lihat stiker kalibrasi di gagang kunci torsi ini: tanggal kalibrasi terakhir bulan lalu dan masa berlaku berikutnya adalah bulan Mei tahun depan. Dokumen dan alat Anda sesuai standar. Terima kasih atas kerja samanya.
:::

- **kunci torsi (torque wrench)**: トルクレンチ
- **pengetatan baut**: ボルトの締め付け
- **stiker kalibrasi**: 校正ステッカー・校正済証
- **masa berlaku**: 有効期限

---

### 場面2: 内部監査での旧版文書（Obsolete Document）放置の指摘

内部品質監査員（Lead Auditor）が資材受入セクションで、改訂前の旧版チェックシートが現場で使われている不適合を発見する場面です。

:::id-example
**Auditor**: Pak Hendra, saya perhatikan formulir pengecekan bahan baku yang digunakan operator hari ini masih menggunakan Formulir Revisi 1.  
**Supervisor**: Iya, betul, Pak. Kami masih menghabiskan sisa lembaran fotokopi formulir yang lama agar tidak mubazir.  
**Auditor**: Ini temuan ketidaksesuaian kategori *minor* dalam ISO 9001 klausul pengendalian informasi terdokumentasi. Sejak dua minggu lalu, Formulir Revisi 2 sudah diterbitkan dengan penambahan kolom pemeriksaan kadar air.  
**Supervisor**: Ah, saya minta maaf, Pak. Kami tidak menyadari hal tersebut berdampak pada sistem kepatuhan mutu.  
**Auditor**: Jika operator tidak mengisi kolom kadar air, bahan baku yang lembap bisa lolos ke proses pencampuran. Saya akan terbitkan Lembar Tindakan Korektif (CAR). Mohon semua formulir lama segera ditarik dan dimusnahkan hari ini juga.  
**Supervisor**: Baik, Pak. Kami akan segera menarik semua berkas revisi lama dan mencetak revisi terbaru, serta membuat laporan tindakan perbaikan.
:::

- **mubazir**: もったいない、無駄遣い（日常口語）
- **pengendalian informasi terdokumentasi**: 文書化された情報の管理
- **kadar air**: 水分率・含水率
- **ditarik dan dimusnahkan**: 回収および破棄処分される

---

## 3. ISO 監査で即座に使える応答・指示フレーズ集

### 監査対応のフレーズ

- **Semua catatan produksi diarsipkan rapi selama minimal tiga tahun sesuai prosedur.**  
  （すべての製造記録は手順書に基づき最低3年間きちんと保管されています。）
- **Bisa tolong tunjukkan bukti verifikasi harian timbangan digital ini?**  
  （この電子天秤の日常点検・日常校正の確認記録を見せていただけますか？）
- **Kami telah meninjau kembali Analisis Risiko (Risk Assessment) untuk proses pencampuran bahan kimia.**  
  （化学薬品の混合プロセスに関するリスクアセスメントを再検討・更新しました。）

### 是正処置（CAR）対応のフレーズ

- **Kami telah menyelesaikan tindakan perbaikan dan menutup temuan audit tersebut tepat waktu.**  
  （私たちは是正措置を完了し、指摘事項のCARを期限内にクローズしました。）
- **Lakukan sosialisasi perubahan SOP ini kepada seluruh pekerja di shift satu dan shift dua.**  
  （このSOP変更を第1シフトおよび第2シフトの全作業員に周知徹底してください。）

---

> [!IMPORTANT]
> **ISO監査で現場作業員が回答する際の鉄則**  
> 監査員から質問された現場スタッフが「よくわからないので適当に答える」ことは厳禁です。「自分の作業標準（IK/SOP）がどこにあるか」「誰に報告するか」を教え込み、わからない場合は「手順書を確認します（Saya akan periksa instruksi kerja terlebih dahulu）」と答えるよう教育することが合格への近道です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 改訂によって新バージョンが発行された後に現場に残っている「無効な旧版文書」を指す表現はどれでしょう？</summary>

1. Dokumen kedaluwarsa / obsolete  
2. Dokumen resmi  
3. Bukti transaksi  

**正解: 1**  
**解説**: 旧版の文書が現場に残って使用されると、古い規格や誤った数値で作業が行われる恐れがあるため「dokumen kedaluwarsa（廃止文書）」として回収・破棄が義務付けられます。
</details>

<details class="id-quiz">
<summary>Q2. ISO監査で不適合が指摘された際に発行され、原因究明と再発防止策を報告する文書の略称は？</summary>

1. CAR (Corrective Action Request)  
2. PO (Purchase Order)  
3. B/L (Bill of Lading)  

**正解: 1**  
**解説**: 是正処置要求書は「CAR（Corrective Action Request）」と呼ばれ、期限内に原因と対策を報告・承認を受ける必要があります。
</details>
