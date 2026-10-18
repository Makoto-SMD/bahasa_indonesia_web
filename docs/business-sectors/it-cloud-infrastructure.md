# B14: クラウドインフラ（AWS/GCP）の保守運用とセキュリティ要件

現代のエンタープライズシステムやWebアプリケーションにおいて、Amazon Web Services (AWS) や Google Cloud (GCP) 等のパブリッククラウド、およびコンテナ技術（Docker / Kubernetes）を活用したインフラ運用（**DevOps / SRE: Site Reliability Engineering**）は中核的な専門領域です。

インドネシアでは、個人情報保護法（**UU PDP: Undang-Undang Perlindungan Data Pribadi**）の施行や政府機関のデータ主権規制（データセンターの国内立地要件など）に伴い、クラウドのセキュリティ構成（IAM権限管理、データ暗号化、ファイアウォール設定）と耐障害性（高可用性・オートスケーリング）が厳格に問われます。

本記事では、クラウドアーキテクチャ設計、IaC（Infrastructure as Code）、リソース監視、バックアップおよび災害復旧（DR: Disaster Recovery）に関する実務インドネシア語を体系的に解説します。

---

## 1. クラウドインフラ・DevOps に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **komputasi awan (Cloud Computing)** | クラウドコンピューティング | サーバー、ストレージ、ネットワークをオンデマンドで利用する技術 |
| **penyedia cloud (Cloud Provider)** | クラウドプロバイダー | AWS, Google Cloud (GCP), Microsoft Azure, Alibaba Cloud 等 |
| **pusat data lokal (Local Data Center)** | 国内データセンター | インドネシア国内リージョン（例: AWS Jakarta Region ap-southeast-3） |
| **skalabilitas otomatis (Auto-Scaling)** | オートスケーリング | トラフィック増減に応じて仮想サーバーやポッド数を自動で拡縮する仕組み |
| **ketersediaan tinggi (High Availability - HA)** | 高可用性 (HA) | 複数アベイラビリティゾーン（Multi-AZ）に冗長配置し、単一障害点を防ぐ構成 |
| **pemuat beban (Load Balancer - ALB/NLB)** | ロードバランサー（負荷分散装置） | 外部からの大量トラフィックを複数の健全なサーバーインスタンスに分散する装置 |
| **Infrastruktur sebagai Kode (IaC)** | Infrastructure as Code (IaC) | Terraform や CloudFormation を用いてインフラ構成をコードで管理・自動構築する手法 |
| **pencadangan dan pemulihan (Backup & Recovery)** | バックアップと復旧 | データベーススナップショットの定期取得と災害復旧手順（RTO / RPO） |
| **UU PDP (Perlindungan Data Pribadi)** | 個人情報保護法 | インドネシア版GDPR。個人データの国内処理・暗号化・漏洩防止を義務付け |
| **manajemen akses identitas (IAM)** | IDアクセス管理 (IAM) | 最小権限の原則（Least Privilege）に基づき、ユーザーやサービスのアカウント権限を制御 |
| **pemantauan dan pencatatan (Monitoring & Logging)** | 監視とログ収集 | Prometheus, Grafana, CloudWatch, Datadog 等によるCPU・メモリ・エラー監視 |

---

## 2. 現場実践対話 (Percakapan Praktis Cloud DevOps)

### 場面1: インドネシア個人情報保護法（UU PDP）に準拠したクラウド設計協議

日系フィンテック企業のリードエンジニアとDevOpsスペシャリストが、金融庁（OJK）やUU PDPの規制要件を満たすインフラ構成を設計する場面です。

:::id-example
**Lead Architect**: Selamat siang, Farhan. Menjelang audit kepatuhan OJK dan implementasi penuh UU PDP, bagaimana kesiapan arsitektur cloud kita di AWS?  
**DevOps Engineer (Farhan)**: Selamat siang, Pak. Secara kepatuhan residensi data (data residency), seluruh kluster database primer kita sudah berada di AWS Region Jakarta (ap-southeast-3), jadi tidak ada data sensitif nasabah yang keluar dari wilayah hukum Indonesia.  
**Lead Architect**: Bagus. Bagaimana dengan standar enkripsi data saat diam (at-rest) dan saat transit (in-transit)?  
**DevOps Engineer (Farhan)**: Untuk data saat transit, semua komunikasi menggunakan protokol TLS 1.3 dengan sertifikat SSL yang diperbarui otomatis. Untuk data saat diam di database RDS dan penyimpanan S3, kami menggunakan enkripsi AES-256 dengan kunci yang dikelola di AWS KMS (Key Management Service).  
**Lead Architect**: Apakah prinsip hak akses terkecil (*principle of least privilege*) sudah diterapkan pada konfigurasi IAM?  
**DevOps Engineer (Farhan)**: Sudah, Pak. Tidak ada akun pengguna yang memiliki akses *AdministratorAccess* secara langsung. Semua akses produksi wajib melalui peran (IAM Role) sementara dengan autentikasi multi-faktor (MFA) dan akses SSH langsung ke server telah ditutup, digantikan dengan AWS Systems Manager Session Manager.
:::

- **residensi data (data residency)**: データの所在国・保存場所規制
- **data sensitif nasabah**: 顧客の機密個人情報
- **enkripsi saat diam / transit**: 保管時暗号化（at-rest） / 通信時暗号化（in-transit）
- **hak akses terkecil**: 最小権限の原則

---

### 場面2: トラフィック急増時のオートスケーリングと高負荷アラート対応

セールイベント中にWebサーバーのCPU使用率が85%を超え、オートスケーリング設定の確認とリレーショナルデータベース（RDS）の接続数枯渇を防ぐ場面です。

:::id-example
**Site Reliability Engineer (SRE)**: Pak Farhan, ada lonjakan trafik 5 kali lipat karena promosi kilat (flash sale) baru saja dimulai. Penggunaan CPU pada kluster Kubernetes pods melonjak ke 88 persen!  
**DevOps Lead (Farhan)**: Apakah kebijakan HPA (Horizontal Pod Autoscaler) sudah memicu penambahan pod otomatis?  
**SRE**: Ya, HPA sudah bekerja dengan baik, jumlah pod meningkat otomatis dari 10 pod menjadi 35 pod dalam waktu dua menit. Beban CPU mulai melandai kembali ke 60 persen.  
**DevOps Lead (Farhan)**: Bagus. Namun, periksa juga jumlah koneksi ke database Aurora PostgreSQL utama kita. Penambahan pod yang drastis bisa membuat *connection pool* database habis.  
**SRE**: Betul sekali, Pak. Jumlah koneksi aktif saat ini sudah mencapai 850 dari batas maksimum 1.000.  
**DevOps Lead (Farhan)**: Segera aktifkan RDS Proxy untuk mengelola dan membagikan ulang koneksi (connection pooling) agar database tidak mengalami kemacetan (*bottleneck*) atau kehabisan memori.  
**SRE**: Siap, konfigurasi RDS Proxy sedang saya aktifkan melalui Terraform sekarang juga.
:::

- **promosi kilat (flash sale)**: タイムセール、フラッシュセール
- **melandai**: 緩やかになる、落ち着く
- **koneksi habis**: コネクション枯渇
- **kebijakan HPA**: 水平ポッド自動スケーラーのポリシー

---

## 3. クラウド運用・DevOpsで頻出する実務構文集

### インフラ構築・IaCのフレーズ

- **Semua perubahan konfigurasi infrastruktur wajib dilakukan melalui kode Terraform (IaC).**  
  （すべてのインフラ構成変更はTerraformコード（IaC）を通じて行わなければなりません。）
- **Kluster database ini harus dikonfigurasikan dengan replika baca (read replica) multi-zona.**  
  （このデータベースクラスタはマルチAZのリードレプリカを備えて構成する必要があります。）
- **Berapa target RTO (Recovery Time Objective) jika terjadi pemadaman pusat data regional?**  
  （リージョンデータセンターの大規模停止が発生した場合の目標復旧時間（RTO）はどれくらいですか？）

### 監視・アラートのフレーズ

- **Atur ambang batas peringatan CPU pada delapan puluh persen di dasbor Grafana.**  
  （GrafanaダッシュボードでCPU警告のしきい値を80パーセントに設定してください。）
- **Lakukan pencadangan basis data harian otomatis setiap pukul dua dini hari.**  
  （毎日午前2時に自動日次データベースバックアップを実行してください。）

---

> [!IMPORTANT]
> **インドネシア個人情報保護法（UU PDP）の厳格化**  
> 2022年に制定され完全適用されたインドネシア個人情報保護法（UU No. 27/2022）では、個人情報漏洩が発生した場合、企業に対して**年間売上高の最大2%に達する過料（denda administratif）**や刑事罰が科されます。クラウド上で氏名、NIK（住民登録番号）、顔写真、財務データを扱う際は、暗号化とアクセスログの厳格な保管が必須です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. トラフィックの急増・急減に応じて、仮想サーバーやコンテナの数を自動的に増減させるクラウド機能を何と呼ぶでしょう？</summary>

1. Skalabilitas Otomatis (Auto-Scaling)  
2. Backup Manual  
3. Surat Jalan  

**正解: 1**  
**解説**: 自動的にサーバーリソースを拡縮する仕組みは「Auto-Scaling（Skalabilitas Otomatis）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. インフラ環境の構築や変更を、クラウド画面の手動クリックではなくコード（定義ファイル）で管理・自動化する開発手法は？</summary>

1. Infrastruktur sebagai Kode (IaC)  
2. Proof of Concept (PoC)  
3. Key Performance Indicator (KPI)  

**正解: 1**  
**解説**: コードでインフラを管理・再現可能にする手法は「Infrastructure as Code (IaC)」と呼ばれます。
</details>
