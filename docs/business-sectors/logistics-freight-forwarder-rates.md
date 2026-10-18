# B26: 物流フォワーダーとの運賃交渉とコンテナ不足・スペース確保

地政学的リスク（スエズ運河・紅海情勢や海峡封鎖）や世界的な荷動きの変動に伴い、海上運賃（**Tarif Uang Tambang / Ocean Freight Rate**）の急騰や空コンテナの供給不足（**Kelangkaan Kontainer / Container Shortage**）は、企業の国際サプライチェーンを揺るがす重大な経営リスクです。

日系企業のロジスティクス調達担当者は、複数の国際貨物利用運送事業者（**Freight Forwarder / Ekspedisi Muatan Kapal Laut - EMKL**）との間で、スポット運賃（Spot Rate）と長期契約運賃（Contract Rate）の比較交渉、割増料（サーチャージ: BAF, CAF, PSS, LSS 等）の査定、およびピークシーズンにおける船腹スペース枠（Alokasi Ruang Kapal）の確保を行わなければなりません。

本記事では、相見積もり（RFQ: Request for Quotation）、運賃明細の精査、空バン確保、緊急時の航空便（Air Freight）振替判断に関する実務インドネシア語を体系的に解説します。

---

## 1. 運賃交渉・コンテナ確保に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Tarif Tambang Laut (Ocean Freight Rate)** | 海上運賃レート | 港から港へのコンテナ海上輸送基本料金（20ft / 40ft 単位） |
| **Biaya Tambahan (Surcharge)** | 割増料金（サーチャージ） | 燃料割増（BAF）、為替割増（CAF）、ピーク期割増（PSS）、低硫黄燃料割増（LSS）等 |
| **THC (Biaya Penanganan di Terminal)** | ターミナル荷役料 (THC) | Terminal Handling Charge（港湾ターミナルでのコンテナ積み降ろし費用） |
| **Kelangkaan Kontainer (Container Shortage)** | コンテナ不足 | デポ（Depot）に荷積み用の健全な空コンテナ（Empty Container）が枯渇する状態 |
| **Alokasi Ruang Kapal (Space Allocation)** | 船腹スペース枠 | 船会社が特定フォワーダーや大口荷主に割り当てる確約積載スペース枠 |
| **Permintaan Penawaran Harga (RFQ)** | 見積依頼書 (RFQ) | 年間輸送量を示して複数フォワーダーに最安値とサービス水準を競わせる入札 |
| **Tarif Kontrak Jangka Panjang (Contract Rate)** | 長期契約運賃 | 6ヶ月〜1年単位で固定単価を合意する大口安定運賃（変動リスクを抑制） |
| **Tarif Pasar Spot (Spot Rate)** | スポット運賃 | 需給バランスにより週単位・航海便単位で上下する直前購入市場運賃 |
| **Depo Kontainer (Container Depot)** | コンテナデポ | 空コンテナの保管、清掃、修理、引き渡しを行う施設 |
| **Pengalihan ke Angkutan Udara (Air Shift)** | 航空便への緊急振替 | 船便の遅延で工場ライン停止の危機がある際、高額でも航空貨物に切り替える判断 |
| **Kontainer Layak Muat (Cargo-Worthy / Seaworthy)** | 積載適格コンテナ | 床板の穴、錆、水漏れがなく安全に海上輸送できる合格状態のコンテナ |

---

## 2. 現場実践対話 (Percakapan Praktis Negosiasi Logistik)

### 場面1: ピークシーズンにおける運賃値上げとコンテナスペース確保交渉

サプライチェーンマネージャーが大手フォワーダーの営業担当者に対し、クリスマス・年末商戦に向けた中国・日本からの輸入コンテナ枠確保とサーチャージ抑制を交渉する場面です。

:::id-example
**SCM Manager (Irfan)**: Selamat siang, Pak Robert. Kami menerima surat edaran kenaikan tarif pengapalan (General Rate Increase - GRI) untuk rute Asia Timur ke Jakarta sebesar 500 dolar AS per kontainer 40 kaki mulai bulan depan.  
**Forwarder Account Manager (Robert)**: Selamat siang, Pak Irfan. Kenaikan GRI tersebut tidak dapat kami hindari karena saat ini kapasitas kapal dari Shanghai dan Tokyo ke Jakarta terisi penuh lebih dari 95 persen menjelang musim puncak belanja akhir tahun.  
**SCM Manager (Irfan)**: Kami memahami dinamika pasar spot, Pak Robert. Namun, perusahaan kami menjamin volume pengiriman rutin sebanyak 30 kontainer setiap bulan sampai akhir tahun. Sebagai imbalan atas komitmen volume tersebut, kami meminta tarif khusus yang kompetitif dan jaminan alokasi ruang (*space guarantee*).  
**Forwarder Account Manager (Robert)**: Jika ada jaminan komitmen 30 kontainer per bulan, kami bisa berikan potongan harga: kenaikan GRI kita pangkas menjadi 250 dolar saja, dan biaya Peak Season Surcharge (PSS) kita bebaskan.  
**SCM Manager (Irfan)**: Itu tawaran yang jauh lebih masuk akal. Syarat kedua kami adalah: jangan sampai ada kontainer kami yang terkena penundaan muat (*rolled-over*) ke kapal berikutnya di pelabuhan transit Singapura.  
**Forwarder Account Manager (Robert)**: Kami setuju, Pak. Kami akan menandatangani *Service Contract* dengan klausul prioritas pemuatan tanpa *roll-over* untuk seluruh kontainer PT Anda.
:::

- **kenaikan tarif umum (General Rate Increase - GRI)**: 一斉基本運賃値上げ
- **musim puncak belanja (peak season)**: 繁忙期・最盛期
- **penundaan muat (rolled-over / roll-over)**: 積み残し（船腹満杯により次便へ強制延期されること）
- **komitmen volume**: 荷主の月間最低出荷数量コミットメント

---

### 場面2: コンテナデポでの空バン不足と品質不良トラブル対応

輸出用の空コンテナを引き取りに行ったトレーラー運転手から、デポに使えるコンテナがないと連絡があり、フォワーダーへ代替手配を緊急要請する場面です。

:::id-example
**Logistics Supervisor (Irfan)**: Halo Pak Robert, supir truk kontainer kami baru saja melapor dari Depo Kontainer Marunda. Pihak depo mengatakan bahwa stok kontainer 20 kaki standar sedang kosong (*out of stock*)!  
**Forwarder (Robert)**: Waduh, masa tidak ada sama sekali, Pak? Menurut sistem inventaris pelayaran tadi pagi masih ada alokasi lima unit.  
**Logistics Supervisor (Irfan)**: Supir kami mengecek sendiri: unit yang tersisa di sana lantainya berlubang, baunya menyengat bekas bahan kimia, dan pintunya bengkok sehingga tidak kedap air (*not seaworthy*). Kami tidak bisa memuat produk kain garmen ekspor berkualitas tinggi ke dalam kontainer kotor seperti itu!  
**Forwarder (Robert)**: Jangan terima unit tersebut, Pak! Itu sangat berisiko merusak barang kain Anda akibat jamur atau rembesan air laut.  
**Logistics Supervisor (Irfan)**: Pabrik kami di Karawang harus selesai stuffing sore ini sebelum jam lima untuk mengejar closing time kapal besok malam di Tanjung Priok. Apa solusinya?  
**Forwarder (Robert)**: Tenang, Pak Irfan. Saya akan segera menghubungi depo rekanan kami yang lain di Cakung untuk mengalihkan surat perintah pengambilan kontainer kosong (*Equipment Interchange Receipt - EIR*). Mereka memiliki kontainer bersih kelas A (*food-grade / cargo-worthy*). Supir Anda bisa langsung meluncur ke sana sekarang.
:::

- **depo kontainer**: コンテナデポ（空コンテナ置き場）
- **kedap air (water-tight / seaworthy)**: 防水性がある、耐航性がある
- **rembesan air laut**: 海水の浸水・にじみ
- **surat pengambilan kontainer kosong (EIR / DO Empty)**: 空コンテナ引取指図書

---

## 3. 物流運賃・スペース確保で頻出する実務構文集

### 相見積もり・価格交渉

- **Mohon kirimkan penawaran harga lengkap (All-In Rate) termasuk biaya THC dan dokumen.**  
  （THCや書類作成費用を含むコミコミのオールイン運賃見積もりを送ってください。）
- **Berapa masa berlaku tarif penawaran ini (rate validity)?**  
  （この提示運賃の有効期限（レートバリディティ）はいつまでですか？）
- **Kami meminta pembebasan biaya penyesuaian bahan bakar (Bunker Adjustment Factor - BAF).**  
  （燃料油価格調整サーチャージ（BAF）の免除を要求します。）

### コンテナ手配・トラブル対応

- **Kondisi kontainer wajib bersih, kering, tidak berbau, dan bebas dari paku tajam.**  
  （コンテナ内部は清潔で乾燥し、無臭で、鋭利な釘などの突起がない状態でなければなりません。）
- **Kargo ini sangat mendesak, apakah ada opsi pengalihan sebagian ke kargo udara?**  
  （この貨物は非常に緊急を要します。一部を航空貨物へ振り替える選択肢はありますか？）

---

> [!TIP]
> **「All-In Rate（総額運賃）」と「隠れサーチャージ」の確認**  
> 海上運賃がいくら安く見えても、後から「Lift-On/Lift-Off料」「CIC（コンテナ不均衡料金）」「洗浄料（Washing Fee）」「書類発行料（Doc Fee）」など多数のローカルサーチャージが加算され、結果的に高額になるトラブルが多発します。必ず見積取得時に「現地港湾費用を含むAll-In総額」で比較検討しましょう。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 船便のスペースが満杯となり、予約していた貨物が予定船に積み込めず次便へ回されてしまう現象を表す海運用語は？</summary>

1. Rolled-over (Penundaan Muat)  
2. Turn-over  
3. Make-over  

**正解: 1**  
**解説**: スペース不足により船会社都合で貨物が次便へ回されることを「Roll-over（積み残し）」と呼びます。
</details>

<details class="id-quiz">
<summary>Q2. 港湾ターミナルにおいて、船と陸地との間でコンテナを積み降ろし・横持ちする際に発生する基本荷役料の略称は？</summary>

1. THC (Terminal Handling Charge)  
2. ATM  
3. OJK  

**正解: 1**  
**解説**: 港湾ターミナル荷役費用は世界共通で「THC（Terminal Handling Charge）」と呼ばれます。
</details>
