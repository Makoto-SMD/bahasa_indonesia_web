# B45: 公認会計士監査（Audit KAP）対応と監査調書実務

インドネシア会社法（UU No. 40/2007）において、一定規模以上の法人（資産・売上500億ルピア超の企業、外資系PT PMA、銀行融資債務者等）には、独立した公認会計士事務所（**KAP: Kantor Akuntan Publik**）による年次財務諸表の**外部監査（Audit Eksternal / Audit Keuangan Independen）**を受けることが義務付けられています。

四半期・年度末の決算期において、監査人（Auditor Eksternal）は実査・立会（Stock Opname / Cash Count）、取引残高確認書（Konfirmasi Piutang/Utang/Bank）、経営者確認書（Surat Representasi Manajemen）、および監査証拠（Bukti Audit）の提出を要求します。

目標は、財務諸表が適正に表示されていることを証明する「**無限定適正意見（Opini Wajar Tanpa Pengecualian - WTP / Unqualified Opinion）**」を獲得することです。本記事では、監査スケジュール（Interim & Year-End Audit）、PBCリスト（Provided by Client）、監査修正仕訳（Management Letter / Adjustment Entry）に関する実務インドネシア語を体系的に解説します。

---

## 1. 会計士監査・監査意見に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **KAP (Kantor Akuntan Publik)** | 公認会計士事務所 | 財務諸表監査を実施し、独立監査人報告書を発行する有資格監査法人（Big 4等） |
| **Opini Audit (Audit Opinion)** | 監査意見 | 監査人が下す評価（無限定適正、限定付適正、不適正、意見不表明） |
| **Wajar Tanpa Pengecualian (WTP)** | 無限定適正意見 (Unqualified) | 財務諸表が会計基準（SAK）に準拠して重要な虚偽表示なく適正に作成されている最高評価 |
| **Wajar Dengan Pengecualian (WDP)** | 限定付適正意見 (Qualified) | 一部の項目に重要な疑義・範囲制限があるものの、全体としては概ね適正な意見 |
| **Tidak Memberikan Pendapat (Disclaimer)** | 意見不表明 (Disclaimer of Opinion) | 監査証拠が著しく不足し、意見を述べる基礎が得られなかった場合の最悪判定 |
| **Daftar PBC (Prepared by Client List)** | 監査依頼資料リスト (PBC List) | 監査人から会社側へ事前に提示される提出必須帳票・証憑類の一覧リスト |
| **Surat Representasi Manajemen (MRL)** | 経営者確認書 (Management Representation) | 経営陣が「全取引を隠蔽なく誠実に開示した」ことを監査人に対して宣誓署名する書面 |
| **Surat Konfirmasi Eksternal (Confirmation Letter)** | 残高確認書（残高証明照会） | 銀行、売掛先、買掛先、弁護士へ直接送付し、残高や係争案件の有無を第三者検証する手続き |
| **Surat Manajemen (Management Letter)** | 改善提案書（マネジメントレター） | 監査人が発見した社内内部統制の弱点や業務改善提案を経営陣にフィードバックする報告書 |
| **Salah Saji Material (Material Misstatement)** | 重要性の基準値を超える虚偽表示 | 財務諸表利用者の経済的意思決定に影響を与えるレベルの重大な数値誤りや脱税・隠蔽 |

---

## 2. 現場実践対話 (Percakapan Praktis Audit KAP)

### 場面1: 年末監査キックオフと監査依頼資料（PBC List）のスケジュール合意

KAP（Big 4会計事務所）の監査シニアマネージャーと日系企業の財務部長が、年次外部監査のタイムラインとPBC資料の提出期限を合意する場面です。

:::id-example
**Lead Auditor KAP (Yosef)**: Selamat pagi, Pak Hendra. Senang bisa bertemu kembali untuk memulai penugasan audit laporan keuangan tahun buku 2026.  
**Accounting Manager (Hendra)**: Selamat pagi, Pak Yosef. Kami siap bekerja sama untuk memastikan proses audit tahun ini berjalan lancar dan tepat waktu sebelum Rapat Umum Pemegang Saham (RUPS) bulan April.  
**Lead Auditor KAP (Yosef)**: Kami telah mengirimkan daftar *Prepared by Client (PBC List)* yang berisi 45 dokumen utama, termasuk Neraca Saldo (*Trial Balance*), rekonsiliasi bank, daftar aset tetap, dan jadwal amortisasi. Kapan tim Anda bisa menyerahkan seluruh berkas tersebut?  
**Accounting Manager (Hendra)**: Seluruh berkas PBC reguler akan kami unggah ke portal data room terenkripsi paling lambat tanggal 15 Januari, setelah proses tutup buku tahunan (annual closing) kami selesai.  
**Lead Auditor KAP (Yosef)**: Bagus sekali. Mengenai konfirmasi eksternal, kami meminta daftar kontak resmi untuk 20 pelanggan dengan saldo piutang terbesar, 10 pemasok utama, serta seluruh rekening bank aktif perusahaan agar tim kami dapat mengirimkan formulir konfirmasi saldo langsung minggu ini.  
**Accounting Manager (Hendra)**: Daftar kontak konfirmasi sudah kami siapkan lengkap dengan surat kuasa persetujuan otorisasi dari direksi.  
**Lead Auditor KAP (Yosef)**: Satu hal lagi: tim kami akan mengirimkan dua auditor lapangan untuk menyaksikan langsung proses penghitungan fisik persediaan (*Stock Opname witness*) di gudang Cikarang pada tanggal 31 Desember.  
**Accounting Manager (Hendra)**: Jadwal stock opname sudah kami tetapkan dan APD untuk tim auditor Anda sudah kami sediakan di pos keamanan pabrik.
:::

- **Neraca Saldo (Trial Balance)**: 合計残高試算表
- **tutup buku tahunan (annual closing)**: 年次本決算
- **Stock Opname witness**: 棚卸立会い（監査人が現物カウントを監督・サンプリングする作業）
- **portal data room terenkripsi**: 暗号化データルームポータル

---

### 場面2: 固定資産の減損損失（Impairment）と監査修正仕訳（Audit Adjustment）の協議

監査人が旧式生産設備の価値下落について「減損会計（Impairment）」の修正仕訳を求め、CFOと適用基準を議論する場面です。

:::id-example
**Audit Partner (Yosef)**: Pak Hendra dan Ibu CFO, dari hasil pengujian substansial atas akun Aset Tetap, kami menemukan bahwa Mesin Cetak nomor 8 di lini lama sudah menganggur (*idle*) selama lebih dari satu tahun dan nilai pasarnya merosot tajam.  
**CFO (Ibu Melati)**: Mesin tersebut memang jarang digunakan, tetapi kami masih menyimpannya sebagai kapasitas cadangan darurat jika mesin baru rusak.  
**Audit Partner (Yosef)**: Menurut Standar Akuntansi Keuangan (PSAK 48 tentang Penurunan Nilai Aset), mesin yang menganggur dan mengalami keusangan teknologi harus diuji nilai yang dapat dipulihkan (*recoverable amount*). Kami mengestimasi adanya indikasi penurunan nilai (impairment) sebesar 1,5 miliar rupiah.  
**CFO (Ibu Melati)**: Apakah penurunan nilai ini harus dicatat sebagai beban kerugian langsung di laporan laba rugi tahun berjalan?  
**Audit Partner (Yosef)**: Ya, kami mengusulkan Jurnal Penyesuaian Audit (*Audit Adjustment Entry*) untuk mendebit Beban Penurunan Nilai Aset dan mengkredit Akumulasi Penurunan Nilai Aset Tetap sebesar 1,5 miliar rupiah.  
**CFO (Ibu Melati)**: Jika kami menolak memposting jurnal penyesuaian ini, apa konsekuensinya terhadap Laporan Auditor Independen?  
**Audit Partner (Yosef)**: Karena angka 1,5 miliar rupiah tersebut melampaui batas ambang materialitas (*materiality threshold*) kami, maka kami terpaksa menerbitkan opini *Wajar Dengan Pengecualian (Qualified Opinion)*. Namun jika manajemen setuju memposting penyesuaian ini, kami dapat memberikan opini terbaik yaitu *Wajar Tanpa Pengecualian (Unqualified Opinion / WTP)*.  
**CFO (Ibu Melati)**: Integritas dan reputasi laporan keuangan kami kepada pemegang saham dan bank kreditor adalah prioritas utama. Kami setuju untuk memposting jurnal penyesuaian penurunan nilai tersebut agar opini WTP dapat dipertahankan.
:::

- **menganggur (idle assets)**: 遊休資産
- **penurunan nilai aset (impairment loss)**: 資産の減損損失
- **ambang batas materialitas (materiality threshold)**: 重要性の基準値（マテリアリティ）
- **Laporan Auditor Independen**: 独立監査人報告書

---

## 3. 会計士監査業務で頻出する実務構文集

### 監査依頼・資料提出

- **Harap lengkapi lembar rekonsiliasi antara rekening koran bank dan buku besar kas.**  
  （銀行預金残高証明書と総勘定元帳の銀行勘定調整表を作成・完備してください。）
- **Auditor independen meminta surat konfirmasi hukum dari konsultan hukum eksternal perusahaan.**  
  （独立監査人は会社の外部法律顧問からの法律確認書（係争事件の有無）を求めています。）
- **Surat Representasi Manajemen wajib ditandatangani oleh Direktur Utama dan Direktur Keuangan.**  
  （経営者確認書は代表取締役および財務取締役の自筆署名が必須です。）

### 監査意見・報告書のフレーズ

- **Laporan keuangan konsolidasian menyajikan secara wajar, dalam semua hal yang material.**  
  （連結財務諸表は、すべての重要な点において適正に表示されています（WTPの定型句）。）
- **Surat Manajemen (Management Letter) memuat temuan mengenai kelemahan pengendalian internal penerimaan kas.**  
  （マネジメントレターには現金受取に関する内部統制の弱点についての指摘事項が記載されています。）

---

> [!IMPORTANT]
> **「WTP（無限定適正意見）」を逃すビジネスリスク**  
> インドネシアにおいて、監査意見が限定付（WDP）や意見不表明（Disclaimer）になると、**銀行融資の即時引き揚げ・金利引き上げ（Loan Default）**、**投資調整庁（BKPM/OSS）のライセンス更新停止**、および親会社への連結決算報告拒否など、企業の信用失墜に直結します。監査人からの指摘には速やかに根拠証憑を提示し、必要に応じて適正な修正仕訳を受け入れる柔軟性が求められます。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 独立監査人が財務諸表に対して発行する「重要な虚偽表示がなく、適正に作成されている」ことを認める最高評価の監査意見は？</summary>

1. Wajar Tanpa Pengecualian (WTP / Unqualified Opinion)  
2. Wajar Dengan Pengecualian (WDP)  
3. Tidak Memberikan Pendapat  

**正解: 1**  
**解説**: 最も適正で優良な監査意見は「WTP（Wajar Tanpa Pengecualian / Unqualified Opinion）」です。
</details>

<details class="id-quiz">
<summary>Q2. 監査人が社内の内部統制（Internal Control）の不備や改善点を経営陣にアドバイスするために発行する報告書は？</summary>

1. Surat Manajemen (Management Letter)  
2. Surat Peringatan  
3. Surat Jalan  

**正解: 1**  
**解説**: 内部統制の改善提案書は「Management Letter（Surat Manajemen）」と呼ばれます。
</details>
