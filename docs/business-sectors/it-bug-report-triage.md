# B13: バグ報告・障害トリアージ（Bug Report）と緊急パッチ対応（Hotfix）

Webサービスやモバイルアプリの本番運用（Production）において、バグ（Bug / Kutu Sistem）やサービス障害（Insiden / Pemadaman Layanan）の発生は避けられません。

重要なのは、バグを発見した際の的確な**バグ報告書（Laporan Bug）**の起票、影響度に応じた優先順位付け（**Triase / Severity Level**）、そして本番環境への安全かつ迅速な**緊急パッチ適用（Hotfix / Tambalan Darurat）**のプロセスです。

本記事では、再現手順（Langkah Reproduksi）、期待される動作と実際の動作の比較、障害重大度分類（P0〜P3 / Critical to Minor）、ポストモーテム（Post-Mortem / Laporan Pasca Insiden）に関する実務インドネシア語を体系的に解説します。

---

## 1. バグ報告・障害トリアージに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **laporan bug (Bug Report / Tiket Cacat)** | バグ報告書 | 不具合の現象、環境、再現手順、ログを整理して報告するチケット |
| **triase bug (Bug Triage)** | バグトリアージ | 報告されたバグの重大度とビジネス影響を評価し、修正順序を決める会議 |
| **tingkat keparahan (Severity Level)** | 重大度（シビラティ） | システム機能への技術的破壊度（P0/Critical, P1/Major, P2/Minor, P3/Trivial） |
| **prioritas perbaikan (Priority)** | 修正優先度 | ビジネス上の緊急度（High, Medium, Low） |
| **langkah reproduksi (Steps to Reproduce - STR)** | 再現手順 | 不具合を100%確実に再現させるためのステップバイステップの操作手順 |
| **perilaku yang diharapkan (Expected Behavior)** | 期待される動作 | 仕様書通りに正しく動いた場合の想定動作 |
| **perilaku aktual (Actual Behavior)** | 実際の動作 | 現実に発生してしまっているエラーや画面クラッシュなどの不具合動作 |
| **lingkungan sistem (Environment)** | 発生環境 | Production, Staging, Dev、OSバージョン（iOS 17, Android 14等）、端末種別 |
| **hotfix / tambalan darurat** | ホットフィックス・緊急パッチ | 定期リリースを待たずに本番環境へ即座にデプロイする緊急修正プログラム |
| **penurunan layanan (service degradation / outage)** | サービス低下 / サービス停止 | サーバー高負荷による遅延、または全機能停止（ダウン） |
| **analisis pasca-insiden (Post-Mortem / RCA)** | 障害事後検証・ポストモーテム | 障害復旧後、根本原因、対応タイムライン、再発防止策をまとめる公式文書 |

---

## 2. 現場実践対話 (Percakapan Praktis Penanganan Bug)

### 場面1: 本番環境での重大障害（P0 Critical Bug）発覚と緊急トリアージ

深夜に本番環境の決済処理で全件エラー（HTTP 500）が発生し、オンコール担当エンジニアとエンジニアリングマネージャーが緊急通話（War Room）でトリアージを行う場面です。

:::id-example
**QA Lead**: Halo Pak Anton, mohon maaf mengganggu malam-malam. Ada insiden kritis (Severity P0) di lingkungan produksi sejak 15 menit lalu!  
**Engineering Manager (Anton)**: Apa yang terjadi? Fitur mana yang terdampak?  
**QA Lead**: Semua transaksi pembayaran kartu kredit dan QRIS gagal total dan mengembalikan kode status HTTP 500 Internal Server Error. Angka kegagalan mencapai 100 persen!  
**Anton**: Ini sangat darurat. Dampak finansialnya sangat fatal. Segera aktifkan kanal War Room di Slack dan hubungi tim inti backend dan devops.  
**Backend Engineer**: Halo Pak, saya sudah memeriksa log server di Datadog. Penyebabnya adalah galat *NullPointerException* pada layanan gateway pembayaran setelah rilis versi 3.4.1 tadi malam. Parameter mata uang (currency) bernilai null.  
**Anton**: Apakah kita bisa melakukan *rollback* (kembali ke versi sebelumnya) dengan cepat, atau kita buatkan *hotfix*?  
**Backend Engineer**: Proses rollback image kontainer di Kubernetes butuh waktu 10 menit. Sementara saya sedang menyiapkan satu baris kode perbaikan hotfix untuk validasi fallback nilai mata uang.  
**Anton**: Lakukan rollback sekarang juga ke versi 3.4.0 agar pengguna bisa bertransaksi kembali segera! Setelah sistem stabil, baru kita uji hotfix tersebut di staging secara matang.
:::

- **gagal total**: 全滅、完全な失敗
- **war room**: 緊急対策オンライン会議・招集部屋
- **galat (error / bug)**: エラー（インドネシア語の正式技術語）
- **kembali ke versi sebelumnya (rollback)**: ロールバック（直前の安定版に戻すこと）

---

### 場面2: QAエンジニアによる的確なバグ報告チケットの作成と共有

QA担当者がステージング環境で発見したカート金額計算の端数処理バグについて、再現手順と証拠動画を添えてエンジニアに報告する場面です。

:::id-example
**QA Engineer**: Halo Budi, saya baru saja menugaskan (assign) tiket bug BUG-405 untukmu di Jira dengan prioritas *High*.  
**Frontend Engineer (Budi)**: Halo Sari. Mengenai apa bug tersebut?  
**QA Engineer**: Ada masalah pembulatan diskon (rounding error) di keranjang belanja saat pengguna menerapkan voucher diskon 15 persen. Total tagihan menjadi minus dua rupiah jika ada produk dengan harga ganjil.  
**Budi**: Apakah langkah reproduksinya (steps to reproduce) sudah kamu tulis lengkap di deskripsi?  
**QA Engineer**: Sudah sangat detail. Ada 4 langkah mulai dari menambahkan barang A ke keranjang, memasukkan kode kupon 'HEMAT15', hingga tombol bayar ditekan. Saya juga sudah melampirkan rekaman layar (screen recording) dan tangkapan payload respons jaringan dari inspect element browser.  
**Budi**: Terima kasih banyak, Sari! Laporan bug yang lengkap seperti ini sangat memudahkan saya untuk langsung mereproduksinya di lingkungan lokal tanpa harus bertanya bolak-balik. Saya akan telusuri fungsi perhitungannya sekarang.
:::

- **pembulatan (rounding)**: 四捨五入・端数処理
- **harga ganjil**: 奇数価格
- **rekaman layar**: 画面録画（スクリーンレコード）
- **bertanya bolak-balik**: 何度も質問を行ったり来たりする

---

## 3. バグ対応・インシデント管理で頻出する実務構文集

### バグ報告・再現確認

- **Bug ini hanya terjadi pada perangkat Android dengan versi sistem operasi di bawah 11.**  
  （このバグはOSバージョン11未満のAndroid端末でのみ発生します。）
- **Lampirkan berkas log sistem dan tangkapan layar konsol (console screenshot).**  
  （システムログファイルとコンソールのスクリーンショットを添付してください。）
- **Apakah Anda dapat mereproduksi kesalahan ini secara konsisten seratus persen?**  
  （このエラーを100パーセント確実に再現させることができますか？）

### 修正完了・ポストモーテム

- **Hotfix telah berhasil diterapkan di produksi dan metrik pemantauan menunjukkan status hijau normal.**  
  （ホットフィックスは本番環境に正常適用され、監視メトリクスは正常（緑）を示しています。）
- **Kita harus menjadwalkan rapat Post-Mortem besok untuk mencegah insiden serupa di masa depan.**  
  （将来の類似障害を防止するため、明日ポストモーテム会議を設定しなければなりません。）

---

> [!TIP]
> **「Blameless Post-Mortem（個人を責めない障害反省会）」の徹底**  
> 障害が発生した際に「誰がバグを書いたのか」を作業者個人の責任にして糾弾すると、チームはバグを隠蔽するようになり、組織の信頼性が崩壊します。「なぜテストで見抜けなかったのか」「なぜCI/CDパイプラインが止まらなかったのか」という**仕組み・プロセスの欠陥（kegagalan sistem/proses）**に焦点を当てて議論しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. バグ報告書において、開発者が手元で同じエラーを確実に発生させるための「操作手順」を表す用語は？</summary>

1. Langkah Reproduksi (Steps to Reproduce)  
2. Rancangan Anggaran Biaya  
3. Jadwal Cuti Tahunan  

**正解: 1**  
**解説**: バグを再現するための具体的な一連の手順は「Langkah Reproduksi（Steps to Reproduce）」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. 本番環境で重大な障害が発生した際、定期リリースサイクルを待たずに即時デプロイされる緊急修正プログラムは？</summary>

1. Hotfix (Tambalan Darurat)  
2. Sprint Planning  
3. Standup Meeting  

**正解: 1**  
**解説**: 緊急の致命的バグを本番環境で即時修正するパッチは「Hotfix」と呼ばれます。
</details>
