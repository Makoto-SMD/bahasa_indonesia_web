# B15: API連携・データベース設計とデータ移行（Data Migration）

企業の基幹システム刷新やモバイルアプリ開発、外部パートナー（金融機関、決済代行、物流API等）とのサービス接続において、**API連携（Integrasi API）**と**データベース設計（Desain Basis Data）**、そして旧システムからの**データ移行（Migrasi Data）**は極めて難易度の高い重要領域です。

インドネシアでは、国営決済ネットワーク（SNAP: Standar Nasional Open API Pembayaran）や政府の統合データ政策（Satu Data Indonesia）の推進により、RESTful API や GraphQL を用いた標準化連携が急速に進んでいます。

本記事では、API仕様書（Swagger / OpenAPI）、スキーマ設計（ERD）、正規化（Normalisasi）、インデックス最適化、ダウンタイムを最小化するデータ移行戦略（ETL処理・ロールバック計画）に関する実務インドネシア語を体系的に解説します。

---

## 1. API連携・データベース・データ移行に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Integrasi API (API Integration)** | API連携 | 異なるシステム間でデータや機能を送受信し、連動させる仕組み |
| **RESTful API / Titik Akhir (Endpoint)** | RESTful API / エンドポイント | HTTPメソッド（GET, POST, PUT, DELETE）でアクセスする接続先URL |
| **Pembatasan Laju (Rate Limiting)** | レートリミット（流量制限） | APIサーバーへの過負荷を防ぐため、単位時間あたりのリクエスト数を制限する設定 |
| **Skema Basis Data (Database Schema / ERD)** | データベーススキーマ / ER図 | テーブル構造、カラム属性、主キー・外部キーのリレーション定義 |
| **Kunci Utama / Kunci Asing (PK / FK)** | 主キー (Primary Key) / 外部キー (Foreign Key) | レコードの一意性特定およびテーブル間の参照整合性を保証するキー |
| **Indeks dan Pengoptimalan Kueri (Indexing)** | インデックスとクエリ最適化 | 検索パフォーマンスを高めるための索引設定とSQL実行計画のチューニング |
| **Migrasi Data (Data Migration)** | データ移行 | 旧システム（Legacy）から新データベースへデータを変換・移し替える作業 |
| **Proses ETL (Ekstraksi, Transformasi, Pemuatan)** | ETL処理 | データの抽出（Extract）、変換・クレンジング（Transform）、格納（Load） |
| **Pembersihan Data (Data Cleansing)** | データクレンジング | 重複、欠損値、不正フォーマットのデータを修正・除外する前処理 |
| **Waktu Henti Sistem (System Downtime)** | システム停止時間（メンテナンス時間） | データ切り替え（Cutover）のためにサービスを一時停止する時間枠 |
| **Rencana Pemulihan (Rollback Plan)** | 切り戻し計画（ロールバック計画） | 移行作業で重大トラブルが発生した際、旧環境へ安全に戻す手順 |

---

## 2. 現場実践対話 (Percakapan Praktis Data & API)

### 場面1: 銀行決済API（SNAP規格）の連携仕様と署名検証の実装協議

フィンテックアプリ開発チームのバックエンドエンジニアと外部パートナー銀行の技術担当者が、インドネシア中央銀行の標準オープンAPI仕様（SNAP）に基づく認証とWebhookを協議する場面です。

:::id-example
**Lead Backend**: Selamat siang, Pak Dani. Kami sedang mengimplementasikan integrasi API Virtual Account berdasarkan standar SNAP Bank Indonesia dengan sistem perbankan Anda.  
**Bank Tech Lead (Dani)**: Selamat siang, Pak Anton. Senang mendengar perkembangannya. Apakah Anda sudah berhasil menghasilkan Tanda Tangan Digital (Digital Signature) menggunakan algoritma SHA-256 with RSA?  
**Lead Backend**: Kami sudah berhasil menghasilkan signature untuk pengujian di sandbox. Namun, kami ingin mengonfirmasi spesifikasi header otorisasi saat pemanggilan token akses B2B.  
**Bank Tech Lead (Dani)**: Format header wajib menyertakan X-TIMESTAMP dalam format ISO 8601, X-CLIENT-KEY, dan X-SIGNATURE. Jika ada selisih waktu lebih dari lima menit antara server Anda dan server kami, permintaan akan otomatis ditolak dengan galat HTTP 401 Unauthorized demi alasan keamanan.  
**Lead Backend**: Dipahami, kami sudah menyinkronkan waktu server kami dengan server NTP global. Bagaimana dengan mekanisme panggilan balik (*webhook/callback*) saat nasabah berhasil membayar tagihan?  
**Bank Tech Lead (Dani)**: Server kami akan mengirimkan HTTP POST ke endpoint callback Anda. Jika server Anda tidak mengembalikan status 200 OK dalam 5 detik, sistem kami akan mencoba mengirim ulang (*retry*) secara otomatis sebanyak tiga kali dengan jeda eksponensial.
:::

- **tanda tangan digital (digital signature)**: デジタル署名
- **selisih waktu**: 時間のズレ、タイムスタンプの乖離
- **jeda eksponensial (exponential backoff)**: 指数関数的リトライ待機時間
- **panggilan balik (webhook / callback)**: コールバック通知

---

### 場面2: 500万件の旧顧客データの新DB移行とインデックス設計

レガシーなMySQLデータベースから新クラウドPostgreSQLデータベースへの夜間移行作業について、データエンジニアとDBAが手順を確認する場面です。

:::id-example
**Data Engineer**: Pak DBA, skrip ETL untuk migrasi lima juta baris data pelanggan lama dari MySQL ke PostgreSQL sudah selesai kami uji coba di lingkungan staging.  
**Database Administrator (DBA)**: Berapa lama waktu yang dibutuhkan untuk menyelesaikan seluruh proses ekstraksi dan pemuatan (loading) data tersebut?  
**Data Engineer**: Pada uji coba pertama, butuh waktu hampir empat jam. Itu terlalu lama dan melebihi jendela waktu henti (maintenance window) yang hanya dialokasikan dua jam pada hari Minggu malam.  
**Database Administrator (DBA)**: Apa yang menyebabkan proses impor berjalan lambat?  
**Data Engineer**: Karena seluruh indeks dan konstrain kunci asing (*foreign keys*) masih aktif selama proses impor data massal (bulk insert).  
**Database Administrator (DBA)**: Betul sekali. Strategi standarnya adalah: jatuhkan (drop) semua indeks sekunder dan nonaktifkan pengecekan foreign key terlebih dahulu sebelum impor massal dimulai. Setelah semua data termuat, baru kita buat ulang indeksnya secara paralel.  
**Data Engineer**: Ide bagus! Kami juga akan membagi data menjadi batch berukuran 10.000 baris menggunakan pipeline multi-threading.  
**Database Administrator (DBA)**: Dengan cara itu, waktu migrasi seharusnya bisa dipangkas menjadi di bawah 45 menit, sehingga kita punya sisa waktu 75 menit untuk verifikasi rekonsiliasi data dan rencana *rollback* darurat jika terjadi anomali.
:::

- **jendela waktu henti (maintenance window)**: メンテナンス停止時間枠
- **impor data massal (bulk insert)**: 一括大量データインポート
- **indeks sekunder**: セカンダリインデックス
- **rekonsiliasi data**: データの照合・整合性チェック

---

## 3. API・DB設計で頻出する実務構文集

### API設計・仕様書のフレーズ

- **Dokumentasi API ini harus mematuhi standar OpenAPI versi 3.0 (Swagger).**  
  （このAPIドキュメントはOpenAPIバージョン3.0（Swagger）標準に準拠しなければなりません。）
- **Terapkan mekanisme pembatasan laju (rate limiting) maksimal 100 permintaan per menit per alamat IP.**  
  （IPアドレスあたり毎分最大100リクエストのレートリミットを適用してください。）
- **Gunakan format respons JSON standar dengan menyertakan kode status, pesan, dan data payload.**  
  （ステータスコード、メッセージ、データペイロードを含む標準JSONレスポンス形式を使用してください。）

### データベース設計・移行のフレーズ

- **Tabel transaksi ini harus memiliki indeks gabungan (composite index) pada kolom tanggal dan ID pengguna.**  
  （この取引テーブルには日付カラムとユーザーIDカラムの複合インデックスを設定する必要があります。）
- **Pastikan tidak ada data yang hilang atau terduplikasi setelah proses migrasi data selesai.**  
  （データ移行プロセスの完了後、データの欠落や重複が一切ないことを確認してください。）

---

> [!TIP]
> **ゼロダウンタイムデータ移行（Zero-Downtime Migration）のトレンド**  
> 近年の24時間365日稼働サービスでは、長時間のメンテナンス停止が許されません。旧DBから新DBへリアルタイムで変更データを差分レプリケーション（CDC: Change Data Capture）し、デュアルライト（新旧両方への書き込み）を経て無停止でDNSを切り替える手法が、インドネシアの先端テック企業でも主流になっています。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. データベース設計において、テーブル内の各レコード（行）を一意に識別するための最も基本的なキーはどれでしょう？</summary>

1. Kunci Utama (Primary Key)  
2. Kunci Pas (Spanner)  
3. Kata Sandi (Password)  

**正解: 1**  
**解説**: 各行を一意に特定するための識別子は「主キー（Primary Key / Kunci Utama）」です。
</details>

<details class="id-quiz">
<summary>Q2. 大規模なデータ移行において、データ抽出（Extract）、変換（Transform）、格納（Load）を一連で行うプロセスの略称は？</summary>

1. ETL  
2. OTD  
3. APD  

**正解: 1**  
**解説**: データの抽出・変換・読み込み処理を総称して「ETL（Extract, Transform, Load）」と呼びます。
</details>
