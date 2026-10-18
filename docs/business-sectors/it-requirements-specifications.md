# B11: ITシステム開発の要件定義（Definisi Kebutuhan）と仕様書レビュー

東南アジアのデジタル経済を牽引するインドネシアでは、スタートアップ（Unicorn企業等）の隆盛だけでなく、日系企業の現地法人やオフショア開発拠点、社内システム刷新において、現地ITエンジニアやプロダクトマネージャー（PM）との協働が急増しています。

システム開発プロジェクトの成否を分ける最大の要因は、上流工程である**要件定義（Definisi Kebutuhan / Requirement Engineering）**と仕様書（Spesifikasi Kebutuhan Perangkat Lunak / PRD）の合意形成です。文化や言語の違いから起こる「認識のズレ（mispersepsi）」を防ぐためには、明確で論理的なインドネシア語による要件定義書の作成とレビューが不可欠です。

本記事では、機能要件・非機能要件の定義、ユースケースシナリオ、スコープ外（Out of Scope）の明確化、仕様変更（Change Request）交渉に関する実務インドネシア語を体系的に解説します。

---

## 1. 要件定義・仕様設計に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **definisi kebutuhan (requirement definition)** | 要件定義 | 開発すべきシステムの機能・目的・制約条件を言語化するプロセス |
| **kebutuhan fungsional (Functional Requirement)** | 機能要件 | ログイン、決済、在庫検索などシステムが提供すべき具体的な機能 |
| **kebutuhan non-fungsional (Non-Functional)** | 非機能要件 | レスポンス速度、同時接続数、セキュリティ基準、稼働率（可用性）等 |
| **dokumen PRD / SRS** | 製品要件定義書 / ソフトウェア要件仕様書 | Product Requirement Document / Software Requirements Specification |
| **ruang lingkup proyek (Project Scope)** | プロジェクトのスコープ（対象範囲） | 今回の開発フェーズで実装する範囲と責任境界 |
| **di luar ruang lingkup (Out of Scope)** | スコープ外（対象外） | コストや納期の都合上、次回フェーズへ見送る機能・要件 |
| **permintaan perubahan (Change Request - CR)** | 仕様変更要求 (CR) | 開発着手後に顧客や事業部門から出される追加・変更の要望 |
| **alur pengguna (user flow / use case)** | ユーザーフロー / ユースケース | ユーザーが画面上で目的を達成するまでの一連の操作動線シナリオ |
| **kriteria penerimaan (Acceptance Criteria - AC)** | 受入基準（完了条件） | 機能が正しく完成したとみなすための客観的な合格判定基準 |
| **kelayakan teknis (technical feasibility)** | 技術的実現可能性 | 既存の技術スタックや予算・期間内で実装が可能かどうかの検証 |
| **pembengkakan lingkup (scope creep)** | スコープ肥大化（スコープクリープ） | 統制なく追加要求が膨らみ、納期や予算が破綻するリスク現象 |

---

## 2. 現場実践対話 (Percakapan Praktis Spesifikasi IT)

### 場面1: プロダクトマネージャー（PM）と顧客間での機能要件・非機能要件の合意

日系ECアプリの刷新プロジェクトで、プロダクトマネージャーが現地クライアントと決済機能の受入基準および同時アクセスの非機能要件を確認する場面です。

:::id-example
**Product Manager (PM)**: Selamat pagi, Ibu Maya. Mari kita tinjau dokumen PRD untuk modul pembayaran gerbang (payment gateway) versi 2.0.  
**Klien**: Selamat pagi, Pak Kenji. Kami sudah membaca drafnya, terutama pada bagian integrasi dompet digital (e-wallet) dan QRIS.  
**PM**: Baik. Mengenai kebutuhan fungsional, apakah kriteria penerimaan (Acceptance Criteria) sudah cukup jelas? Transaksi harus otomatis dibatalkan jika pengguna tidak membayar dalam waktu 15 menit.  
**Klien**: Ya, itu sudah sesuai alur bisnis kami. Namun, bagaimana dengan kebutuhan non-fungsional untuk lonjakan trafik saat kampanye tanggal kembar seperti Promo 12.12?  
**PM**: Kami menetapkan target performa: sistem harus mampu menangani hingga 10.000 transaksi bersamaan (concurrent transactions) dengan waktu respon API di bawah 500 milidetik.  
**Klien**: Sangat bagus. Tolong pastikan juga kepatuhan terhadap standar keamanan PCI-DSS agar data kartu kredit pengguna aman dari kebocoran.  
**PM**: Tentu saja, arsitektur kami menggunakan enkripsi ujung-ke-ujung (end-to-end encryption) dan data kartu tidak disimpan di server lokal kita.
:::

- **gerbang pembayaran (payment gateway)**: 決済ゲートウェイ
- **dompet digital (e-wallet)**: 電子ウォレット（GoPay, OVO, Dana 等）
- **transaksi bersamaan (concurrent transactions)**: 同時トランザクション
- **enkripsi ujung-ke-ujung**: エンドツーエンド暗号化

---

### 場面2: 開発途中の仕様変更要求（Change Request）への対応交渉

開発スプリントの途中で、クライアントから新たな多言語切り替え機能の追加要望が出され、納期と追加費用のトレードオフを協議する場面です。

:::id-example
**Klien**: Pak Kenji, dewan direksi kami mendadak meminta agar fitur multi-bahasa (Inggris, Indonesia, dan Mandarin) dimasukkan ke dalam peluncuran MVP bulan depan.  
**PM**: Ibu Maya, fitur multi-bahasa tersebut saat ini berada di luar ruang lingkup (out of scope) untuk rilis Fase 1 sesuai kesepakatan awal.  
**Klien**: Apakah tidak bisa diselipkan di sprint yang sedang berjalan saat ini?  
**PM**: Jika kita memaksakan penambahan fitur ini sekarang, kita menghadapi risiko pembengkakan lingkup (*scope creep*). Tim pengembang harus merombak struktur database dan API, yang akan menunda tanggal peluncuran sedikitnya tiga minggu.  
**Klien**: Waduh, tanggal peluncuran tidak boleh mundur karena promosi pemasaran sudah dijadwalkan.  
**PM**: Sebagai solusinya, kami sarankan merilis MVP tepat waktu dengan bahasa Indonesia dan Inggris terlebih dahulu, lalu menerbitkan Formulir Permintaan Perubahan (Change Request) resmi untuk memasukkan bahasa Mandarin pada Fase 1.5 dua minggu setelah peluncuran.  
**Klien**: Saran yang sangat masuk akal. Kami setujui rencana tersebut agar jadwal rilis utama tetap aman.
:::

- **peluncuran MVP (Minimum Viable Product)**: 実用最小限の製品のリリース
- **merombak struktur**: 構造を一から作り変える、全面改修する
- **menunda tanggal peluncuran**: リリース日を延期する

---

## 3. 要件定義・仕様レビューで頻出する実務構文集

### 要件の明文化・確認

- **Fitur ini wajib memiliki mekanisme verifikasi dua langkah (Two-Factor Authentication / 2FA).**  
  （この機能には2要素認証（2FA）の仕組みが必須要件として含まれます。）
- **Tingkat ketersediaan sistem (system availability) ditargetkan minimal 99,9 persen per tahun.**  
  （システムの年間稼働率（可用性）は最低99.9パーセントを目標とします。）
- **Bagaimana alur alternatif jika koneksi internet pengguna terputus saat proses sinkronisasi data?**  
  （データ同期処理中にユーザーのネット接続が切断された場合の代替フローはどうなっていますか？）

### スコープ管理・変更交渉

- **Permintaan penambahan fitur analitik ini akan kami catat sebagai backlog untuk rilis berikutnya.**  
  （この分析機能の追加要望は、次回リリースのためのバックログとして記録しておきます。）
- **Setiap perubahan spesifikasi setelah tahap penandatanganan akan dikenakan biaya tambahan.**  
  （仕様合意の署名フェーズ以降の仕様変更には追加費用が発生します。）

---

> [!IMPORTANT]
> **仕様書の「暗黙の了解（Asumsi）」を徹底排除する**  
> 日本では「言わなくても普通はこう作るだろう」という暗黙の期待が通用しますが、多言語・多国籍のITチームでは通用しません。画面遷移、エラーメッセージの内容、権限ロール（Admin, User, Viewer）、タイムアウト秒数に至るまで、仕様書（PRD）にすべて明文化（tersurat）して合意を取りましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. システム開発において、決済やログインなどシステムが提供すべき具体的機能を指す用語はどれでしょう？</summary>

1. Kebutuhan Fungsional (Functional Requirement)  
2. Kebutuhan Non-fungsional  
3. Anggaran Belanja  

**正解: 1**  
**解説**: システムの機能そのものを定義する要件は「kebutuhan fungsional（機能要件）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 当初の開発合意範囲外（Out of Scope）の要望が無秩序に追加され、納期や予算が圧迫される現象を表すIT専門用語は？</summary>

1. Scope creep (pembengkakan lingkup)  
2. Unit testing  
3. Refactoring  

**正解: 1**  
**解説**: 管理されずに開発範囲が膨れ上がるリスク現象を「スコープクリープ（scope creep / pembengkakan lingkup）」と呼びます。
</details>
