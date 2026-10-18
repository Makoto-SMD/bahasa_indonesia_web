# B18: サイバーセキュリティインシデント対応と情報漏洩対策

東南アジアにおけるサイバー攻撃の激化と、インドネシア**国家暗号サイバー庁（BSSN: Badan Siber dan Sandi Negara）**および**個人情報保護法（UU PDP）**の施行に伴い、企業のサイバーセキュリティ管理（**Keamanan Siber**）は経営陣の最重要責務となっています。

ランサムウェア（Ransomware）によるデータ暗号化、フィッシング詐欺（Phishing）、不正アクセス（Akses Tidak Sah）、個人情報の流出（Kebocoran Data Pribadi）が発生した際、被害の拡大を防ぐ初動対応（Containment）、原因調査（Forensik Digital）、および監督当局（BSSN / Kominfo / OJK）への**72時間以内の公式通報義務**が存在します。

本記事では、CSIRT（Incident Response Team）の組織、セキュリティパトロール、脆弱性診断（Penetration Testing）、情報漏洩インシデント発生時の緊急対応に関する実務インドネシア語を体系的に解説します。

---

## 1. サイバーセキュリティに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Keamanan Siber (Cybersecurity)** | サイバーセキュリティ | ネットワーク、サーバー、端末、データを不正攻撃から保護する技術・体制 |
| **Insiden Keamanan (Security Incident)** | セキュリティインシデント | 不正アクセス、マルウェア感染、情報漏洩などのセキュリティ事故 |
| **Kebocoran Data Pribadi (Data Breach)** | 個人情報漏洩・データ侵害 | 顧客や従業員の機密個人データが外部に流出・公開されてしまう事象 |
| **Peretasan / Peretas (Hacking / Hacker)** | ハッキング / ハッカー（攻撃者） | システムの脆弱性を突いて不正侵入する行為およびその主体 |
| **Perangkat Pemeras (Ransomware)** | ランサムウェア（身代金型ウイルス） | データを暗号化して人質に取り、復号キーと引き換えに金銭を要求するマルウェア |
| **Rekayasa Sosial / Phishing (Social Engineering)** | ソーシャルエンジニアリング / フィッシング | 偽メールや偽サイトでパスワードや二要素認証コードを騙し取る手法 |
| **Uji Penetrasi (Penetration Testing / Pentest)** | 脆弱性侵入テスト（ペンテスト） | 疑似攻撃を行ってシステムの弱点やセキュリティホールを事前に洗い出す検査 |
| **CSIRT (Tim Tanggap Insiden Keamanan Siber)** | CSIRT（インシデント対応チーム） | 攻撃発生時に緊急対応・調査・封じ込めを指揮する専門対応組織 |
| **BSSN (Badan Siber dan Sandi Negara)** | 国家暗号サイバー庁 | インドネシア政府のサイバーセキュリティ政策・規制を統括する最高機関 |
| **Karantina Jaringan (Network Isolation / Containment)** | ネットワーク隔離 | 感染端末や侵害サーバーを社内LANから物理的・論理的に切り離す初動措置 |
| **Analisis Forensik Digital (Digital Forensics)** | デジタルフォレンジック調査 | ログやメモリダンプを解析し、侵入経路や改ざん履歴の証拠保全を行う調査 |

---

## 2. 現場実践対話 (Percakapan Praktis Tanggap Insiden)

### 場面1: ランサムウェア感染の検知と緊急ネットワーク隔離（Containment）

セキュリティ監視センター（SOC）のオペレーターが、経理部PCからランサムウェア特有の通信異常を検知し、CISO（最高情報セキュリティ責任者）へ緊急報告する場面です。

:::id-example
**SOC Analyst**: Lapor Pak CISO! Sistem EDR (Endpoint Detection and Response) kami baru saja mendeteksi enkripsi massal file di dua komputer departemen keuangan, dan muncul pesan tebusan (ransom note)!  
**CISO**: Ini darurat tingkat satu! Segera lakukan isolasi jaringan (network quarantine) terhadap kedua workstation tersebut sekarang juga! Cabut kabel LAN dan putuskan koneksi Wi-Fi-nya!  
**SOC Analyst**: Perintah isolasi via konsol EDR sudah berhasil dieksekusi dalam hitungan detik, Pak. Komputer sudah terputus total dari jaringan lokal kita.  
**CISO**: Apakah ada tanda-tanda pergerakan lateral (*lateral movement*) ke server penyimpanan bersama (NAS) atau pengendali domain (Domain Controller)?  
**SOC Analyst**: Kami sedang menyaring log lalu lintas jaringan. Beruntung, sistem firewall internal berhasil memblokir upaya koneksi mencurigakan ke port 445 (SMB) pada server utama.  
**CISO**: Bagus sekali. Amankan salinan citra memori (*memory dump*) dan log kejadian untuk tim forensik digital. Jangan sekali-kali mematikan daya komputer yang terinfeksi secara paksa agar bukti digital di RAM tidak hilang!
:::

- **pesan tebusan (ransom note)**: 身代金要求画面・脅迫メッセージ
- **isolasi jaringan (network quarantine)**: ネットワーク隔離
- **pergerakan lateral (lateral movement)**: 攻撃者のラテラルムーブメント（社内横展開・感染拡大）
- **salinan citra memori (memory dump)**: メモリダンプ（揮発性メモリの証拠保全）

---

### 場面2: 個人情報漏洩疑いと法的義務に基づく監督機関（BSSN / Kominfo）への報告

顧客データベースの一部がダークウェブのフォーラムで売りに出されているとの通報を受け、法務チームとCISOがUU PDPに基づく72時間通報手順を確認する場面です。

:::id-example
**Legal Manager**: Pak CISO, kami menerima laporan dari intelijen ancaman siber bahwa ada sampel 5.000 data pengguna kita yang diposting di forum peretas gelap (dark web).  
**CISO**: Kami telah memvalidasi sampel tersebut dengan database internal. Format nomor telepon dan alamat email cocok dengan data lama dari server pengujian pihak ketiga yang salah konfigurasi tahun lalu.  
**Legal Manager**: Menurut Pasal 46 Undang-Undang Perlindungan Data Pribadi (UU PDP), pengendali data pribadi wajib menyampaikan pemberitahuan tertulis kepada lembaga pengawas (Kominfo/BSSN) dan subjek data pribadi paling lambat 3 x 24 jam (72 jam) sejak terjadinya kegagalan perlindungan data.  
**CISO**: Tim forensik kami sedang merampungkan Laporan Kronologi Insiden Awal. Informasi apa saja yang wajib disertakan dalam surat pemberitahuan tersebut?  
**Legal Manager**: Surat wajib memuat: jenis data pribadi yang terungkap, waktu terjadinya insiden, dampak potensial bagi nasabah, serta langkah mitigasi dan saluran kontak darurat (hotline) yang dapat dihubungi.  
**CISO**: Baik, draf laporan teknis mitigasi akan selesai sore ini. Kita harus bersikap transparan dan patuh hukum untuk meminimalkan sanksi administratif dan menjaga reputasi publik perusahaan.
:::

- **forum peretas gelap (dark web)**: ダークウェブのハッカーフォーラム
- **salah konfigurasi**: 設定ミス（misconfiguration）
- **subjek data pribadi**: 個人情報主体（ユーザー・本人）
- **langkah mitigasi**: 被害軽減策・緩和措置

---

## 3. セキュリティ管理で頻出する実務構文集

### 予防・日常運用のフレーズ

- **Semua karyawan wajib mengganti kata sandi secara berkala dan mengaktifkan MFA.**  
  （全従業員は定期的なパスワード変更と多要素認証（MFA）の有効化が義務付けられています。）
- **Jangan pernah mengklik tautan atau mengunduh lampiran dari email yang mencurigakan.**  
  （不審なメールのリンクをクリックしたり、添付ファイルをダウンロードしたりしないでください。）
- **Lakukan penambalan kerentanan (vulnerability patching) pada sistem operasi server setiap minggu.**  
  （毎週サーバーOSのセキュリティパッチ適用（脆弱性修正）を実施してください。）

### 事故対応・通報のフレーズ

- **Cabut perangkat yang terinfeksi dari jaringan lokal sesegera mungkin.**  
  （感染したデバイスを直ちにローカルネットワークから切り離してください。）
- **Pemberitahuan resmi mengenai kebocoran data wajib disampaikan dalam batas waktu 72 jam.**  
  （データ漏洩に関する正式通知は72時間の制限時間内に提出されなければなりません。）

---

> [!IMPORTANT]
> **UU PDP（個人情報保護法）第46条の「72時間ルール」**  
> インドネシアで個人データ侵害（Kegagalan Perlindungan Data Pribadi）が発生した場合、**発覚から最長72時間以内（paling lambat 3 x 24 jam）**に監督当局および影響を受けるユーザー全員に対して書面通知を行うことが法律で義務付けられています。隠蔽（menutupi insiden）は最大の罰則対象となるため、迅速な事実把握と公表体制が不可欠です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. データを暗号化して人質に取り、復号キーと引き換えに身代金を要求する悪意あるマルウェアを何と呼ぶでしょう？</summary>

1. Perangkat Pemeras (Ransomware)  
2. Antivirus  
3. Firewall  

**正解: 1**  
**解説**: 身代金を要求する脅迫型マルウェアは「Ransomware（Perangkat Pemeras）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. インドネシア個人情報保護法（UU PDP）において、個人データの漏洩事故が発生した際に監督官庁へ通知すべき法定制限時間は？</summary>

1. Paling lambat 72 jam (3 x 24 jam)  
2. Satu bulan  
3. Tidak ada batas waktu  

**正解: 1**  
**解説**: UU PDP第46条により、インシデント認知から最長「72時間（3×24時間）以内」に書面通知を行う義務があります。
</details>
