# B17: ITベンダー選定とSLA（サービス水準合意）交渉

インドネシアでシステム開発やITインフラ運用を外部委託（**Outsourcing / Alih Daya**）する際、信頼できる現地のITベンダー（Vendor TI / Mitra Pengembang）の選定と、厳格な**SLA（Service Level Agreement: Perjanjian Tingkat Layanan）**の締結はプロジェクトの成否と投資対効果（ROI）を左右します。

提案依頼書（**RFP: Request for Proposal**）の作成、技術力・財務健全性のスコアリング評価、稼働率保証（Uptime Guarantee）、障害復旧時間（MTTR）、そしてSLA未達時のペナルティ条項（Klausul Penalti / Kredit Layanan）をあらかじめ明確に取り決めておく必要があります。

本記事では、ITベンダー選定コンペ、相見積もり比較、契約交渉、SLAモニタリングに関する実務インドネシア語を体系的に解説します。

---

## 1. ITベンダー選定・SLA交渉に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **SLA (Perjanjian Tingkat Layanan)** | サービス水準合意 (SLA) | サービスの品質基準、目標稼働率、障害対応時間を定めた公式契約書 |
| **RFP (Permintaan Proposal Proyek)** | 提案依頼書 (RFP) | 発注側が要件や予算、選定基準を明記して複数社に提案を求める文書 |
| **Vendor TI / Mitra Alih Daya** | ITベンダー / アウトソーシング先 | 開発やインフラ保守を受託する外部パートナー企業 |
| **Uptime / Ketersediaan Layanan** | 稼働率（アップタイム） | サーバーやシステムが正常稼働している時間の割合（例: 99.9%） |
| **MTTR (Waktu Rata-rata Pemulihan)** | 平均修復時間 (MTTR) | 障害発生の通知を受けてからシステムが正常復旧するまでの所要時間 |
| **Waktu Tanggap Awal (Response Time)** | 初動応答時間 | 障害報告チケットが起票されてからエンジニアが調査を開始するまでの時間 |
| **Klausul Penalti / Denda Pelanggaran** | ペナルティ条項・違約金 | SLA目標が未達だった場合に月額利用料から差し引かれる返金・減額条項 |
| **Kredit Layanan (Service Credit)** | サービスクレジット | 稼働率未達に対する補償として次月以降の請求額から割り引かれるポイント |
| **Dukungan 24/7 (Bantuan 24 Jam 7 Hari)** | 24時間365日サポート体制 | 夜間や休日も含めた常時オンコール監視・保守体制 |
| **Hak Kekayaan Intelektual (HKI / IP)** | 知的財産権 (IP) | 開発されたソースコードや設計書の著作権がどちらに帰属するかの重要条項 |
| **Masa Garansi / Pemeliharaan (Warranty)** | 保証期間 / 無償瑕疵担保期間 | 納品検収後、無償でバグ修正に対応する期間（通常3〜6ヶ月） |

---

## 2. 現場実践対話 (Percakapan Praktis Negosiasi SLA)

### 場面1: RFPに基づくITベンダー提案書の審査とSLA条件の交渉

日系企業のIT統括マネージャー（CIO/IT Manager）が、現地の大手システム開発会社と保守契約のSLA条件（稼働率とペナルティ）を詰める場面です。

:::id-example
**IT Manager (Tanaka)**: Selamat siang, Pak Rudi. Kami telah meninjau proposal teknis dan komersial dari tim Anda untuk pemeliharaan sistem ERP kami. Portofolio Anda sangat meyakinkan.  
**Direktur Vendor (Rudi)**: Selamat siang, Pak Tanaka. Terima kasih atas kepercayaannya. Kami sangat antusias untuk menjadi mitra strategis jangka panjang perusahaan Anda.  
**IT Manager (Tanaka)**: Namun, ada beberapa poin dalam lampiran SLA draf Anda yang perlu kita negosiasikan ulang, terutama mengenai jaminan ketersediaan layanan (*uptime*). Di draf ini tertulis 99,0 persen per bulan.  
**Direktur Vendor (Rudi)**: Ya, angka 99,0 persen itu adalah paket standar korporat kami, Pak.  
**IT Manager (Tanaka)**: Bagi operasi ritel kami, toleransi henti 99,0 persen berarti sistem boleh mati lebih dari tujuh jam per bulan, dan itu tidak dapat kami terima. Kami mensyaratkan jaminan ketersediaan minimal 99,9 persen (tiga sembilan).  
**Direktur Vendor (Rudi)**: Jika dinaikkan menjadi 99,9 persen, kami harus mengalokasikan tim teknis siaga 24/7 khusus dan menyiapkan arsitektur *failover* otomatis cadangan di pusat data sekunder. Tentu ada sedikit penyesuaian pada biaya langganan bulanan.  
**IT Manager (Tanaka)**: Kami siap mempertimbangkan penyesuaian biaya wajar tersebut, asalkan klausul kredit layanan (*service credit*) juga dipertegas: jika *uptime* bulanan jatuh di bawah 99,5 persen, kami berhak mendapatkan pemotongan tagihan sebesar 20 persen.  
**Direktur Vendor (Rudi)**: Adil sekali, Pak Tanaka. Kami yakin dengan keandalan infrastruktur kami. Kami akan merevisi dokumen SLA tersebut dan menyertakan klausul kredit layanan yang disepakati.
:::

- **jangka panjang**: 長期的な
- **toleransi henti**: 許容停止時間
- **arsitektur failover otomatis**: 自動フェイルオーバー（予備系切り替え）構成
- **penyesuaian biaya wajar**: 妥当な費用の調整

---

### 場面2: 納品検収とソースコードの知的財産権（IP）帰属確認

プロジェクトの最終検収（UAT Sign-off）段階で、開発された独自のビジネスロジックの著作権とリポジトリの譲渡を確認する場面です。

:::id-example
**Legal Counsel Perusahaan**: Pak Rudi, sebelum kami menandatangani Berita Acara Serah Terima (BAST) untuk aplikasi ini, mari kita pastikan kembali ketentuan Hak Kekayaan Intelektual (HKI) dalam perjanjian kerja sama utama.  
**Direktur Vendor (Rudi)**: Tentu, Bu. Sesuai kontrak klausul nomor 8, seluruh hak cipta kode sumber (*source code*), skema basis data, dan dokumentasi API yang dibuat secara khusus (*custom-built*) untuk proyek ini beralih menjadi milik penuh perusahaan Anda.  
**Legal Counsel Perusahaan**: Sangat baik. Apakah seluruh hak akses repositori Git pribadi (GitHub/GitLab) dan kredensial akun root cloud sudah dialihkan sepenuhnya ke tim internal kami?  
**Direktur Vendor (Rudi)**: Semua kepemilikan repositori sudah kami transfer ke organisasi GitHub resmi Anda pagi ini, dan tim pengembang kami hanya memegang akses baca (*read-only*) untuk keperluan dukungan selama masa garansi 90 hari.  
**Legal Counsel Perusahaan**: Terima kasih atas profesionalismenya. Berkas BAST sudah kami sahkan, dan bagian keuangan akan memproses pembayaran termin terakhir sesuai jadwal.
:::

- **Berita Acara Serah Terima (BAST)**: 業務完了引渡書・検収証明書（インドネシアの必須公的商慣習帳票）
- **kode sumber (source code)**: ソースコード
- **beralih menjadi milik penuh**: 完全に貴社の所有に帰属する
- **pembayaran termin terakhir**: 最終分割支払金（マイルストーン最終払）

---

## 3. ベンダー選定・契約交渉で頻出する実務構文集

### ベンダー評価・条件提示

- **Kandidat vendor wajib memiliki sertifikasi keamanan informasi ISO 27001 yang masih aktif.**  
  （ベンダー候補は有効なISO 27001情報セキュリティ認証を保有していることが必須です。）
- **Berapa waktu tanggap awal (first response time) untuk tiket gangguan berkategori kritis (Severity 1)?**  
  （重大度カテゴリー1（Critical）の障害チケットに対する初動応答時間は何分ですか？）
- **Vendor tidak diperkenankan mengalihkan sebagian pekerjaan ke pihak ketiga (subkontraktor) tanpa persetujuan tertulis.**  
  （ベンダーは書面による事前承認なしに、業務の一部を第三者（再委託先）へ再委託することはできません。）

### 検収・保証対応

- **Masa garansi perbaikan bug berlaku selama enam bulan sejak tanggal penandatanganan BAST.**  
  （バグ修正の無償保証期間はBAST署名日から6ヶ月間有効とします。）
- **Laporan kinerja bulanan (SLA Monthly Report) harus diserahkan maksimal tanggal lima setiap bulannya.**  
  （月次SLAパフォーマンス報告書は毎月5日までに提出されなければなりません。）

---

> [!IMPORTANT]
> **BAST（Berita Acara Serah Terima）の法的重要性**  
> インドネシアの商取引では、納品物を受け取ったことを証明する「BAST」の締結が極めて重要な法的効力を持ちます。検収が不十分なまま安易にBASTにサインしてしまうと、「検収完了」とみなされて後から瑕疵（バグ）の無償修正を要求することが法的に困難になるため、必ず受入テスト（UAT）を完了させてから署名しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. システム運用委託契約において、稼働率や障害復旧時間などのサービス品質水準を定めた合意書の略称は？</summary>

1. SLA (Service Level Agreement)  
2. ROI (Return on Investment)  
3. BAST (Berita Acara Serah Terima)  

**正解: 1**  
**解説**: サービスの提供品質や停止時間許容度を明確に取り決める合意は「SLA」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. インドネシアでITプロジェクトの各開発フェーズや最終納品が完了した際、発注側と受注側が合意署名する公式検収書類は？</summary>

1. BAST (Berita Acara Serah Terima)  
2. Surat Kuasa  
3. Faktur Pajak  

**正解: 1**  
**解説**: 成果物の検収引渡しを証明する公式書類は「BAST（Berita Acara Serah Terima）」です。
</details>
