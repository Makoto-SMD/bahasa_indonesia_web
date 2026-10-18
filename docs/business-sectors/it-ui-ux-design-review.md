# B16: UI/UXデザインのレビューとユーザビリティテスト（Usability Testing）

スマートフォンの普及率が急激に高まり、モバイルファースト（Mobile-First）が徹底されているインドネシア市場において、ユーザーインターフェース（**UI: Antarmuka Pengguna**）とユーザー体験（**UX: Pengalaman Pengguna**）の最適化は、サービスの成否やコンバージョン率（Tingkat Konversi）を決定づける最重要ファクターです。

Figma や Adobe XD を用いたワイヤーフレーム（Kerangka Gambar）や高精度プロトタイプ（Prototipe High-Fidelity）のデザインレビュー、デザインシステム（Sistem Desain）の統一、そして実際の現地エンドユーザーを招いた**ユーザビリティテスト（Uji Kegunaan / Usability Testing）**では、ローカル文化特有の視覚的好みやデジタルリテラシーへの深い配慮が求められます。

本記事では、デザインレビュー会議、アクセシビリティ評価、A/Bテスト、ヒューリスティック評価に関する実務インドネシア語を体系的に解説します。

---

## 1. UI/UXデザイン・ユーザビリティに関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Antarmuka Pengguna (UI)** | ユーザーインターフェース (UI) | ボタン、色彩、タイポグラフィ、レイアウト等の視覚的画面要素 |
| **Pengalaman Pengguna (UX)** | ユーザーエクスペリエンス (UX) | サービス利用時における使いやすさ、感情、満足度、ストレスの総体 |
| **Kerangka Kawat (Wireframe)** | ワイヤーフレーム | 色や装飾を排除し、画面の骨組みと情報配置を簡易的に示した設計図 |
| **Prototipe Interaktif (Prototype)** | インタラクティブプロトタイプ | Figma等でボタンを押すと画面遷移する、実際に操作可能な試作モデル |
| **Sistem Desain (Design System)** | デザインシステム | カラーパレット、余白ルール、アイコン、共通UIコンポーネントの規約集 |
| **Uji Kegunaan (Usability Testing - UT)** | ユーザビリティテスト | 被験者に特定のタスクを実行させ、つまずき（Pain Point）を観察・分析する調査 |
| **Titik Hambatan Pengguna (Pain Point)** | ペインポイント（ユーザーの課題） | 操作中にユーザーが迷ったり、不快感や離脱を覚える問題箇所 |
| **Tingkat Konversi (Conversion Rate)** | コンバージョン率 (CVR) | 閲覧者が購入や会員登録などの目標行動に到達した割合 |
| **Tingkat Rasio Pantulan (Bounce Rate)** | 直帰率 / 離脱率 (Drop-off Rate) | アプリ起動直後や購入手続きの途中で離脱してしまうユーザーの比率 |
| **Aksesibilitas Desain (Accessibility)** | デザインアクセシビリティ | 視覚障害や高齢者でも見やすいコントラスト比、文字サイズ、音声対応 |
| **Pengujian A/B (A/B Testing)** | A/Bテスト | 2種類以上の画面デザインをランダムに配信し、クリック率や購入率を比較する手法 |

---

## 2. 現場実践対話 (Percakapan Praktis Desain UI/UX)

### 場面1: Figmaを用いたプロダクトデザインレビュー会議

UI/UXリードデザイナーがプロダクトマネージャー（PM）およびフロントエンドエンジニアに対し、新決済画面のデザインプロトタイプを提示してフィードバックを求める場面です。

:::id-example
**UI/UX Designer (Reza)**: Selamat pagi rekan-rekan. Hari ini saya ingin mempresentasikan prototipe interaktif di Figma untuk alur checkout yang telah disederhanakan.  
**Product Manager (Maya)**: Selamat pagi, Reza. Mari kita lihat. Apa perubahan terbesar dibandingkan dengan versi aplikasi yang ada saat ini?  
**UI/UX Designer (Reza)**: Kami memangkas jumlah langkah checkout dari empat layar menjadi proses satu layar (*one-page checkout*). Pilihan metode pembayaran utama seperti QRIS, GoPay, dan Transfer Bank BCA kami letakkan di posisi teratas dengan tombol *radio button* berukuran besar yang mudah ditekan jempol tangan satu (*thumb-friendly*).  
**Frontend Engineer (Budi)**: Dari segi teknis, tampilannya sangat bersih. Namun, saya perhatikan ukuran font pada rincian biaya pengiriman dan asuransi hanya 10 piksel dengan warna abu-abu muda.  
**UI/UX Designer (Reza)**: Ah, terima kasih atas masukannya, Budi. Menurut pedoman aksesibilitas Web (WCAG), rasio kontras warna tersebut memang terlalu rendah dan mungkin sulit dibaca oleh pengguna dengan layar smartphone kelas menengah di bawah terik sinar matahari.  
**Product Manager (Maya)**: Betul sekali. Di Indonesia, banyak pengguna memakai smartphone berlayar resolusi rendah di luar ruangan. Tolong naikkan kontrasnya menjadi abu-abu gelap dan ubah ukuran font minimal 12 piksel agar teks tetap jelas terbaca.  
**UI/UX Designer (Reza)**: Siap, Mbak Maya. Saya akan sesuaikan token warnanya di pustaka sistem desain kita siang ini.
:::

- **alur checkout**: チェックアウト動線・購入決済フロー
- **ramah jempol (thumb-friendly)**: 親指で片手操作しやすい
- **smartphone kelas menengah**: ミドルレンジ・低価格帯スマートフォン
- **di bawah terik sinar matahari**: 強い日差しの下で

---

### 場面2: ユーザビリティテスト（UT）の観察とペインポイントの特定

UXリサーチャーが現地モニター（被験者）にアプリを使ってもらい、マジックミラー越しの部屋でチームと観察しながらボトルネックを分析する場面です。

:::id-example
**UX Researcher (Lina)**: Sekarang pengguna ketiga kita, Mas Danang, sedang mencoba menyelesaikan skenario: "Cari hotel di Yogyakarta dengan fasilitas kolam renang dan lakukan pemesanan sampai ke pemilihan metode bayar."  
**Product Manager (Maya)**: Coba perhatikan gerak-gerik jarinya di layar rekaman. Dia tampak ragu-ragu di halaman daftar hotel.  
**UX Researcher (Lina)**: Ya, dia sudah mengetuk (tap) ikon filter tiga kali, tetapi tidak menyadari bahwa tombol "Terapkan Filter" tersembunyi di bawah lipatan layar (*below the fold*) karena terhalang oleh *floating banner* promosi.  
**Product Manager (Maya)**: Ini adalah *pain point* kritis! Tiga dari empat pengguna yang kita uji hari ini mengalami kebingungan yang sama persis di titik tersebut. Mereka mengira filternya otomatis aktif tanpa harus menekan tombol terapkan.  
**UX Researcher (Lina)**: Tepat sekali. Rekomendasi perbaikan saya adalah: buat tombol "Terapkan Filter" menempel permanen di bagian bawah layar (*sticky bottom bar*) dengan indikator jumlah filter aktif yang mencolok.  
**Product Manager (Maya)**: Sangat setuju. Perubahan ini akan segera kita masukkan ke dalam *backlog* prioritas tinggi untuk sprint mendatang sebelum kita meluncurkan kampanye liburan akhir tahun.
:::

- **ragu-ragu**: 迷っている、躊躇している
- **di bawah lipatan layar (below the fold)**: スクロールしないと見えない領域
- **tombol menempel permanen (sticky bar)**: 画面下部に固定されるバー
- **kebingungan yang sama persis**: まったく同一の混乱・つまずき

---

## 3. UI/UX業務で頻出する実務構文集

### デザイン評価・フィードバック

- **Tata letak (layout) halaman ini terlalu padat, tolong berikan ruang kosong (white space) yang cukup.**  
  （このページのレイアウトは過密すぎます。十分な余白（ホワイトスペース）を設けてください。）
- **Hierarki visual judul dan sub-judul harus diperjelas agar alur pembacaan lebih alami.**  
  （視線誘導が自然になるよう、タイトルとサブタイトルの視覚的ヒエラルキーを明確にしてください。）
- **Gunakan komponen standar dari sistem desain kita untuk menjaga konsistensi antarmuka.**  
  （画面の一貫性を保つため、社内デザインシステムの標準コンポーネントを使用してください。）

### ユーザー調査・テスト分析

- **Pengguna membutuhkan waktu rata-rata tiga menit lebih lama untuk menemukan menu pengaturan.**  
  （ユーザーが設定メニューを見つけるのに、平均して3分以上余計に時間がかかっています。）
- **Hasil uji A/B menunjukkan bahwa tombol Call to Action (CTA) berwarna hijau meningkatkan konversi sebesar lima belas persen.**  
  （A/Bテストの結果、緑色のCTAボタンがコンバージョンを15パーセント向上させることが実証されました。）

---

> [!TIP]
> **インドネシア市場におけるUI/UXの国民的特性**  
> インドネシアの消費者は、テキストだらけのシンプルなデザインよりも、**親しみやすいイラストや鮮やかなバナー、ゲーミフィケーション（ポイントやガチャ）、チャット相談ボタン（WhatsApp連携）**が目立つインターフェースを好む傾向があります。「情報過多にせず、かつ楽しげで信頼感のあるビジュアル（ramah dan terpercaya）」のバランスが重要です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 実際のユーザーに特定の操作を依頼し、迷ったり困ったりする問題点（ペインポイント）を抽出する調査手法は？</summary>

1. Uji Kegunaan (Usability Testing)  
2. Uji Emisi Kendaraan  
3. Uji Beban Server  

**正解: 1**  
**解説**: 使いやすさの検証と課題抽出をユーザー観察によって行う手法を「ユーザビリティテスト（Uji Kegunaan）」と呼びます。
</details>

<details class="id-quiz">
<summary>Q2. 操作中にユーザーがストレスや不便、離脱を感じる具体的な問題箇所を表すUX専門用語は？</summary>

1. Titik Hambatan (Pain Point)  
2. Poin Pelanggaran (Penalty Point)  
3. Poin Loyalitas (Loyalty Point)  

**正解: 1**  
**解説**: ユーザー体験上の障害や課題・不満点は「Pain Point（Titik Hambatan / Masalah）」と呼ばれます。
</details>
