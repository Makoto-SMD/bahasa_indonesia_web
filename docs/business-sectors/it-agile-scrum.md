# B12: アジャイル・スクラム開発の実践（スプリント計画と朝会）

インドネシアのIT・ソフトウェア開発の現場では、変化の激しい市場環境に迅速に対応するため、**アジャイル（Agile）**および**スクラム（Scrum）**フレームワークがデファクトスタンダードとなっています。

現地エンジニア（Software Engineer, QA, UI/UX Designer）と協働する際、スプリント計画（**Sprint Planning**）、毎朝15分のスタンドアップミーティング（**Daily Standup / Daily Scrum**）、スプリントレビュー（Sprint Review）、ふりかえり（**Sprint Retrospective**）などのスクラムイベントが日常的に回されます。

本記事では、ユーザーストーリー（User Story）、ストーリーポイント見積もり（Story Points Estimation）、進捗管理（Kanban / Jira）、障害（Blocker / Impediment）共有に関する実務インドネシア語を体系的に解説します。

---

## 1. アジャイル・スクラムに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Sprint (Siklus Kerja)** | スプリント | 1週間〜2週間単位の固定された反復開発期間 |
| **Daily Standup / Scrum Pagi** | デイリースタンドアップ（朝会） | 毎朝15分間、3つの質問（昨日・今日・障害）を共有する同期ミーティング |
| **Cerita Pengguna (User Story)** | ユーザーストーリー | 「[役割]として、[目的]のために、[機能]が欲しい」という利用者視点の要求単位 |
| **Poin Cerita (Story Points)** | ストーリーポイント | タスクの規模・難易度・不確実性をフィボナッチ数（1, 2, 3, 5, 8）等で見積もる単位 |
| **Tumpukan Tugas (Product Backlog)** | プロダクトバックログ | プロダクトに必要な全機能・改善項目・バグ修正の優先順位付き一覧 |
| **Backlog Sprint** | スプリントバックログ | 現在のスプリント期間内にチームが完成させるとコミットしたタスク群 |
| **Hambatan / Kendala (Blocker / Impediment)** | ブロッカー・障害要因 | 開発作業を妨げ、他者の支援や解決を必要としている課題 |
| **Definisi Selesai (Definition of Done - DoD)** | 完成の定義 (DoD) | コードレビュー完了、自動テスト通過、ステージング検証等、タスク完了の絶対条件 |
| **Papan Kanban (Kanban Board)** | カンバンボード | To Do, In Progress, In Review, Done など進捗状態を可視化するボード（Jira等） |
| **Retrospeksi Sprint (Sprint Retrospective)** | スプリントふりかえり | 開発プロセス・人間関係・ツールの良かった点（KPT: Keep/Problem/Try）を反省する場 |
| **Kecepatan Tim (Team Velocity)** | チームベロシティ | チームが1スプリントあたりに完了できるストーリーポイントの平均消化速度 |

---

## 2. 現場実践対話 (Percakapan Praktis Scrum)

### 場面1: 毎朝のデイリースタンドアップ（Daily Standup）

スクラムマスター（Scrum Master）が進行し、バックエンドエンジニアとフロントエンドエンジニアがJiraボードを見ながら進捗とブロッカーを報告する場面です。

:::id-example
**Scrum Master**: Selamat pagi tim! Mari kita mulai daily standup untuk hari ke-5 Sprint 14. Silakan mulai dari Mas Rio untuk modul backend.  
**Backend Engineer (Rio)**: Pagi semuanya. Kemarin saya sudah menyelesaikan endpoint API untuk pendaftaran akun pengguna baru dan unit test-nya sudah lolos 100 persen. Kartu Jira sudah saya pindahkan ke kolom *In Review*.  
**Scrum Master**: Mantap, Rio. Apa rencana kamu untuk hari ini?  
**Backend Engineer (Rio)**: Hari ini saya akan mulai mengerjakan integrasi webhook notifikasi SMS OTP.  
**Scrum Master**: Apakah ada hambatan (*blocker*) yang menghalangi pekerjaanmu?  
**Backend Engineer (Rio)**: Ada sedikit kendala, akun sandbox dari penyedia SMS gateway pihak ketiga kredensialnya belum aktif. Saya butuh bantuan tim DevOps untuk meminta token akses yang valid ke vendor.  
**Scrum Master**: Baik, saya akan hubungi tim DevOps segera setelah standup ini selesai agar kamu tidak tertahan. Sekarang lanjut ke Mbak Dewi dari frontend.  
**Frontend Engineer (Dewi)**: Kemarin saya menyelesaikan slicing tampilan halaman checkout. Hari ini fokus menghubungkan halaman tersebut dengan API keranjang belanja. Tidak ada blocker dari sisi saya.
:::

- **slicing tampilan**: デザインカンプ（Figma）をHTML/CSS/コンポーネントにコード化（スライス）する作業
- **akun sandbox**: テスト環境アカウント
- **tertahan**: 足止めを食らう、作業がストップする

---

### 場面2: スプリント計画（Sprint Planning）でのストーリーポイント見積もり

プロダクトオーナー（PO）から提示されたタスクについて、開発チームがポーカー見積もりを行い、ポイント数を議論する場面です。

:::id-example
**Product Owner (PO)**: Tiket berikutnya adalah US-102: "Pencarian Produk Berdasarkan Gambar (Image Search AI)". Kriteria penerimaan sudah saya lampirkan di kartu Jira.  
**Scrum Master**: Ayo tim pengembang, mari kita hitung estimasi *story points* menggunakan kartu planning poker. Satu, dua, tiga, buka kartu!  
**Scrum Master**: Wah, ada perbedaan cukup jauh: Mas Rio memberi 3 poin, tapi Mas Kevin memberi 8 poin. Kevin, bisa jelaskan mengapa menurutmu tiket ini bernilai 8 poin?  
**Senior Engineer (Kevin)**: Menurut saya kompleksitasnya sangat tinggi. Kita harus mengintegrasikan model machine learning eksternal, menangani latensi respons gambar beresolusi tinggi, dan membuat caching pintar di Redis. Risiko ketidakpastiannya besar.  
**Backend Engineer (Rio)**: Hmm, setelah mendengar penjelasan Kevin mengenai caching dan latensi, saya setuju. Sebelumnya saya hanya berpikir kita tinggal memanggil API pihak ketiga yang sudah siap pakai.  
**Scrum Master**: Apakah semua sepakat kita tetapkan tiket ini menjadi 8 poin?  
**Tim Pengembang**: Sepakat! 8 poin.  
**PO**: Jika tiket ini 8 poin, total beban sprint ini sudah mencapai 45 poin, melampaui rata-rata *velocity* tim kita yang berada di 40 poin. Saya akan pindahkan tiket laporan analitik ke sprint berikutnya agar tim tidak kewalahan.
:::

- **planning poker**: プランニングポーカー（見積もり手法）
- **latensi respons**: レスポンス遅延・レイテンシ
- **kewalahan**: 圧倒される、手一杯でパンクする

---

## 3. スクラム開発で頻出する実務構文集

### 朝会・進捗共有のフレーズ

- **Kemarin saya fokus menyelesaikan perbaikan kutu (bug fixing) pada fitur keranjang.**  
  （昨日はカート機能のバグ修正に集中して取り組みました。）
- **Tugas ini masih berstatus "Dalam Pengerjaan" (In Progress) karena menunggu persetujuan PR.**  
  （このタスクはプルリクエスト（PR）の承認待ちのため、まだ進行中ステータスです。）
- **Tolong tarik kartu Jira ini ke kolom pengujian (Ready for QA).**  
  （このJiraチケットをQAテスト待ちカラムへ移動してください。）

### ふりかえり・改善のフレーズ

- **Pada sesi Retrospektif, apa yang perlu kita pertahankan (Keep) dan apa yang perlu diubah (Change)?**  
  （ふりかえりセッションにおいて、私たちが継続すべきこと、改善すべきことは何ですか？）
- **Komunikasi antar-tim jauh lebih lancar setelah kita membuat kanal Slack khusus proyek ini.**  
  （本プロジェクト専用のSlackチャンネルを開設したことで、チーム間の連携が格段にスムーズになりました。）

---

> [!TIP]
> **インドネシア人エンジニアとの朝会の工夫**  
> インドネシアの文化では「上司や同僚に困っていることを言い出しにくい（segan / malu）」と感じる若手エンジニアが珍しくありません。デイリースタンドアップでは「進捗が遅れていること」を叱責するのではなく、「何がブロッカー（障害）か」「チームとしてどう手助けできるか」を問いかける心理的安全性を醸成することが大切です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. アジャイル開発において、毎朝チームが集まり「昨日やったこと・今日やること・障害」を手短に共有する15分程度のミーティングは？</summary>

1. Daily Standup (Scrum Pagi)  
2. RUPS (Rapat Pemegang Saham)  
3. Audit Pajak Tahunan  

**正解: 1**  
**解説**: 毎朝の立ち会いは「Daily Standup」または「Daily Scrum」と呼ばれます。
</details>

<details class="id-quiz">
<summary>Q2. スクラム開発で作業を妨げ、他者の助けや解決を必要としている障害・課題を表す用語は？</summary>

1. Blocker / Hambatan  
2. Velocity  
3. Milestone  

**正解: 1**  
**解説**: 作業を阻害する障害や課題は「Blocker（Hambatan / Kendala）」と呼ばれます。
</details>
