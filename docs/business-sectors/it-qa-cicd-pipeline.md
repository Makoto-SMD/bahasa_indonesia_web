# B20: テスト自動化・コードレビュー・CI/CDパイプライン

高品質なソフトウェアを迅速かつ安定してリリースし続けるため、現代の開発チームでは**テスト自動化（Otomatisasi Pengujian）**、GitHub/GitLab での**コードレビュー（Tinjauan Kode / Code Review）**、そして**CI/CDパイプライン（Integrasi dan Penerapan Berkelanjutan）**の構築が不可欠な標準プラクティスです。

現地ソフトウェアエンジニアやQAエンジニアとの日々の開発において、プルリクエスト（Pull Request: PR）の指摘作法、単体テスト（Unit Test）のカバレッジ基準、静的解析ツール（SonarQube / Linter）によるコード品質検証、ステージングおよび本番環境への自動デプロイワークフローをスムーズに運用する必要があります。

本記事では、PRレビューでの建設的フィードバック、エンドツーエンド（E2E）自動テスト（Playwright / Cypress）、カナリアリリース（Canary Release）、パイプライン障害のトラブルシューティングに関する実務インドネシア語を体系的に解説します。

---

## 1. CI/CD・QA自動化・コードレビューに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **CI/CD (Integrasi & Pengiriman Berkelanjutan)** | CI/CD | コードの変更を自動でビルド・テスト・デプロイする自動化パイプライン |
| **Tinjauan Kode (Code Review)** | コードレビュー | 他の開発者が書いたコードの品質、可読性、セキュリティ、設計を検証する作業 |
| **Permintaan Tarik (Pull Request - PR / MR)** | プルリクエスト (PR) | 自分の作成した機能ブランチを主ブランチ（main）へマージ（統合）するための申請 |
| **Uji Unit / Uji Integrasi (Unit / Integration Test)** | 単体テスト / 結合テスト | 個別の関数・モジュールの動作検証 / モジュール同士の連携動作検証 |
| **Uji Ujung-ke-Ujung (End-to-End Test - E2E)** | E2Eテスト（総合自動テスト） | 実際のブラウザやアプリ上でユーザーの一連の操作動線を自動シミュレーションするテスト |
| **Cakupan Pengujian (Test Coverage)** | テストカバレッジ（網羅率） | 全コードベースのうち、自動テストによって実行・検証されたコード行の割合（%） |
| **Analisis Kode Statis (Static Code Analysis)** | 静的コード解析 | コードを実行せずに潜在的バグ、セキュリティ脆弱性、コードスメルを自動検知するツール |
| **Penerapan Bertahap (Canary / Blue-Green Deployment)** | カナリアリリース / ブルーグリーンデプロイ | 全ユーザーではなく一部（5%〜10%）のユーザーに新版を先行公開してリスクを抑える手法 |
| **Pipa yang Rusak (Broken Pipeline / Build Failure)** | パイプライン障害（ビルド落ち） | 自動テストの失敗や構文エラーによりCI/CDプロセスが途中で停止する状態 |
| **Penggabungan Cabang (Branch Merging)** | ブランチのマージ | レビューとテストを通過したコードを本流ブランチへ結合すること |
| **Pembersihan Kode (Refactoring)** | リファクタリング | 外部から見た動作を変えずに、内部コードの可読性や保守性を向上させる書き換え |

---

## 2. 現場実践対話 (Percakapan Praktis CI/CD & Review)

### 場面1: GitHub上でのプルリクエスト（PR）のコードレビュー議論

シニアエンジニアがジュニアエンジニアの書いたプルリクエストに対し、クエリのN+1問題とセキュリティ上の懸念について建設的なフィードバックを行う場面です。

:::id-example
**Senior Engineer (Bayu)**: Halo Adit, saya sudah meninjau Pull Request (PR) kamu nomor 156 untuk fitur riwayat transaksi pelanggan.  
**Junior Engineer (Adit)**: Halo Mas Bayu, terima kasih sudah direview! Apakah ada catatan perbaikan?  
**Senior Engineer (Bayu)**: Secara keseluruhan kodenya bersih dan mudah dibaca. Namun, ada dua hal yang perlu kamu perbaiki sebelum saya bisa memberikan *Approval* (persetujuan).  
**Junior Engineer (Adit)**: Poin apa saja itu, Mas?  
**Senior Engineer (Bayu)**: Pertama, di berkas `TransactionController.java` baris 45, ada masalah *Kueri N+1* saat mengambil data nama toko. Dalam perulangan for-loop, kamu memanggil database satu per satu. Tolong gunakan teknik *eager loading* dengan `JOIN FETCH` agar kueri dieksekusi sekali saja. Jika datanya ribuan, performa database bisa jebol.  
**Junior Engineer (Adit)**: Ah, betul sekali! Saya tidak menyadari hal itu. Saya akan ubah menjadi join fetch sekarang. Poin keduanya apa, Mas?  
**Senior Engineer (Bayu)**: Poin kedua mengenai sanitasi input pada parameter pencarian kata kunci untuk mencegah potensi SQL Injection. Tolong pastikan kamu menggunakan *Prepared Statements* atau ORM bawaan.  
**Junior Engineer (Adit)**: Siap, Mas Bayu! Saya akan commit perubahan perbaikannya siang ini dan meminta review ulang.
:::

- **kueri N+1**: N+1問題（ループ内でSQLを大量発行してしまうアンチパターン）
- **eager loading**: 一括先行読み込み
- **performa jebol**: 性能が崩壊する、耐えきれなくなる
- **sanitasi input**: 入力値のサニタイズ・無害化

---

### 場面2: CI/CDパイプラインのテスト失敗と本番自動デプロイの保護

ブランチマージ時にGitHub Actionsパイプラインが赤（ビルドエラー）になり、品質ゲート（Quality Gate）によって本番環境への不正リリースが自動阻止される場面です。

:::id-example
**DevOps Engineer**: Mas Bayu,パイプライン CI/CD untuk repositori pembayaran baru saja memicu tanda merah (*build failed*) pada langkah *Job E2E Testing*.  
**Senior Engineer (Bayu)**: Bagus sistem proteksi kita bekerja. Apa yang menyebabkan pengujian E2E gagal?  
**DevOps Engineer**: Dari laporan Cypress, ada kegagalan asersi (*assertion error*) pada skenario pembayaran dompet digital: tombol 'Konfirmasi Pembayaran' tidak dapat diklik karena tertutup oleh komponen pop-up promosi baru.  
**Senior Engineer (Bayu)**: Ini bukti nyata mengapa pengujian otomatis dan *Quality Gate* di pipeline CI/CD sangat berharga. Jika perubahan ini langsung lolos ke produksi tanpa pengujian otomatis, ribuan pengguna tidak akan bisa membayar hari ini.  
**DevOps Engineer**: Betul sekali. Cabang *main* kita dilindungi oleh aturan proteksi (*branch protection rule*), jadi penggabungan (merge) otomatis diblokir sampai semua tes lulus 100 persen.  
**Senior Engineer (Bayu)**: Tolong beri tahu pengembang yang membuat perubahan tersebut untuk memperbaiki selektor tombol di komponen frontend dan menjalankan tes Cypress lokal sebelum mendorong (*push*) kembali kodenya.
:::

- **kegagalan asersi (assertion error)**: アサーションエラー（テスト期待値の不一致）
- **aturan proteksi cabang (branch protection rule)**: ブランチ保護ルール（マージ制限設定）
- **mendorong kode (push code)**: リモートリポジトリへコードをプッシュする

---

## 3. CI/CD・QA業務で頻出する実務構文集

### コードレビュー・フィードバック

- **Tolong tambahkan pengujian unit (unit test) untuk menangani kasus batas (edge cases).**  
  （境界値・例外ケース（エッジケース）を処理するための単体テストを追加してください。）
- **Cakupan tes (test coverage) pada modul ini harus mencapai ambang batas minimal delapan puluh persen.**  
  （このモジュールのテスト網羅率は最低80パーセントのしきい値に達しなければなりません。）
- **Kode ini terlihat redundan, tolong lakukan pembersihan kode (refactoring) menggunakan pola desain standar.**  
  （このコードは冗長に見えます。標準的なデザインパターンを用いてリファクタリングしてください。）

### デプロイ・パイプライン管理

- **Penerapan bertahap (canary deployment) telah diarahkan ke sepuluh persen lalu lintas pengguna.**  
  （カナリアリリースが全ユーザートラフィックの10パーセントに対して適用されました。）
- **Jika ada lonjakan tingkat kesalahan (error rate) di atas satu persen, sistem akan otomatis melakukan rollback.**  
  （エラー率が1パーセントを超えて急増した場合、システムは自動的にロールバックを実行します。）

---

> [!TIP]
> **「NIT（微細な指摘）」と「BLOCKER（必須修正）」の区別**  
> コードレビューで細かいインデントや命名の好みにまで厳しく注文をつけて承認を渋ると、開発速度が著しく低下し人間関係も摩擦が起きます。「必須のバグ・セキュリティ修正（Blocker）」と「好みの範疇・提案（Nit / Suggestion）」を明確にラベル分けしてレビューする文化を共有しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. コードを主ブランチ（main）へ統合する前に、他メンバーが品質やセキュリティを検証する作業を何と呼ぶでしょう？</summary>

1. Tinjauan Kode (Code Review)  
2. Surat Peringatan  
3. Wawancara Kerja  

**正解: 1**  
**解説**: 他の開発者が書いたコードを検証・承認する作業は「Code Review（Tinjauan Kode）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 新バージョンのソフトウェアを全ユーザーに一斉公開せず、数パーセントの一部ユーザーに先行公開して安全性を確かめるリリース手法は？</summary>

1. Penerapan Bertahap (Canary Deployment)  
2. Big Bang Deployment  
3. Manual Release  

**正解: 1**  
**解説**: 一部トラフィックに先行配信してリスクを最小化する手法を「カナリアリリース（Penerapan Bertahap / Canary）」と呼びます。
</details>
