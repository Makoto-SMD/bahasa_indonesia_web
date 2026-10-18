# B27: インコタームズ（FOB, CIF, DDP等）と貿易リスク移転の明確化

国際貿易取引において、売主（Penjual / Shipper）と買主（Pembeli / Consignee）の間で費用負担（Cost）、危険負担・滅失リスク移転（Risk / Peralihan Tanggung Jawab）、および通関責任の境界を明確にする国際商業会議所（ICC）の統一規則が**インコタームズ（Incoterms / Ketentuan Perdagangan Internasional）**です。

インドネシアとの輸出入取引では、海上輸送特有の**FOB（本船甲板渡し）**や**CIF（運賃保険料込み渡し）**、航空便や複合輸送に適した**FCA（運送人渡し）**や**CIP（運送費保険料込み渡し）**、そして買い手側の手間を極小化する**DDP（関税込持込渡し）**が広く用いられます。

しかし、港湾でのコンテナ落下、海上荒天による濡れ損、輸入通関トラブルが発生した際、どちらが責任を負うかで法的な紛争（Sengketa Dagang）に発展することが珍しくありません。本記事では、各インコタームズ条件の定義、リスク移転の瞬間、海上保険（Asuransi Kargo）、契約書記載の留意点に関する実務インドネシア語を体系的に解説します。

---

## 1. インコタームズ・リスク分担に関する重要語彙

| インドネシア語 / 略語 | 日本語対応 | 現場での定義・実務メモ |
| :--- | :--- | :--- |
| **Incoterms (Ketentuan Dagang Internasional)** | インコタームズ規則 | 国際商業会議所が定めた貿易取引条件の国際標準ルール（最新版: Incoterms 2020） |
| **Peralihan Risiko (Transfer of Risk)** | 危険負担の移転（リスク移転） | 貨物の破損・滅失リスクが売主から買主に切り替わる法的な瞬間 |
| **Beban Biaya (Cost Allocation)** | 費用負担の境界 | 運賃、保険料、荷役費、通関手数料、関税をどちらが支払うかの取り決め |
| **FOB (Free on Board / Bebas di Atas Kapal)** | 本船甲板渡し (FOB) | 船積み港で貨物が本船上に置かれた時点でリスクが買主へ移転（海上専用） |
| **CIF (Cost, Insurance, and Freight)** | 運賃保険料込み渡し (CIF) | 売主が運賃と保険を手配するが、リスクは積出港の本船積載時に買主へ移転 |
| **CFR (Cost and Freight)** | 運賃込み渡し (CFR / C&F) | 売主が仕向港までの運賃を支払うが、保険は買主負担、リスクは積出港で移転 |
| **FCA (Free Carrier / Bebas Pengangkut)** | 運送人渡し (FCA) | 売主の施設または指定場所で指定運送人に引き渡した時点でリスク移転（コンテナ・航空便推奨） |
| **DDP (Delivered Duty Paid / Diserahkan Bea Masuk Dibayar)** | 関税込持込渡し (DDP) | 売主が輸入通関・関税支払いまで全て行い、買主の指定倉庫まで届ける条件 |
| **DAP (Delivered at Place)** | 仕向地持込渡し (DAP) | 売主が指定場所まで輸送するが、輸入通関と関税納付は買主が行う条件 |
| **Klaim Asuransi Marin (Marine Cargo Claim)** | 海上貨物保険金請求 | 輸送中の水濡れ、破損、全損事故に対して保険会社へ損害賠償を請求する手続き |
| **Kerusakan Kargo (Cargo Damage / Loss)** | 貨物損傷・滅失 | 輸送中の衝撃、浸水、結露（Sweat Damage）、盗難等による商品価値の損失 |

---

## 2. 現場実践対話 (Percakapan Praktis Incoterms)

### 場面1: 日本側本社との調達契約条件（FOB vs CIF）の切り替え協議

ジャカルタ現地法人の購買担当者が、日本本社からの原材料調達において、為替変動と海上保険の補償範囲を考慮して契約条件をFOBからCIFに変更する交渉を行う場面です。

:::id-example
**Procurement Manager (Ardi)**: Selamat pagi, Pak Kenji. Kami ingin mengevaluasi syarat pengiriman barang (trade terms) untuk pembelian komponen dari pabrik Jepang ke Jakarta. Selama ini kita menggunakan skema FOB Port of Kobe.  
**Managing Director (Kenji)**: Selamat pagi, Ardi. Mengapa kamu mengusulkan evaluasi? Apakah ada kendala operasional dengan skema FOB?  
**Procurement Manager (Ardi)**: Dengan skema FOB, kantor kami di Jakarta harus mengurus pemesanan kapal dan membayar premi asuransi pengangkutan laut sendiri menggunakan mata uang dolar AS. Karena rupiah sedang melemah terhadap dolar, biaya logistik lokal kita menjadi sangat fluktuatif dan sulit diprediksi.  
**Managing Director (Kenji)**: Apa alternatif yang kamu usulkan?  
**Procurement Manager (Ardi)**: Kami mengusulkan beralih ke skema CIF Tanjung Priok Port (Incoterms 2020). Kantor pusat di Jepang memiliki kontrak volume global (*global volume contract*) dengan perusahaan pelayaran raksasa, sehingga tarif tambang laut dan premi asuransi yang didapat kantor pusat jauh lebih murah 20 persen daripada tarif yang bisa kami dapatkan di Jakarta.  
**Managing Director (Kenji)**: Poin yang sangat tepat dari sisi efisiensi biaya grup. Ingat bahwa pada skema CIF, meskipun kantor pusat yang membayar tambang dan asuransi, peralihan risiko tetap terjadi di atas kapal di Pelabuhan Kobe. Jadi jika ada barang rusak di laut, klaim asuransi tetap diurus oleh pihak penerima di Jakarta.  
**Procurement Manager (Ardi)**: Betul sekali, Pak. Polis asuransi kargo (Marine Cargo Policy) akan diterbitkan atas nama perusahaan kami di Jakarta, dengan klausul pertanggungan Institute Cargo Clauses (A) yang mencakup segala risiko (All Risks).
:::

- **fluktuatif**: 変動が激しい、不安定な
- **kontrak volume global**: グローバル包括大口契約
- **Institute Cargo Clauses (A) / All Risks**: 協会貨物約款(A)・全危険担保特約
- **polis asuransi kargo**: 貨物保険証券

---

### 場面2: DDP（関税込渡し）契約における現地通関トラブルと責任追及

海外サプライヤーから「DDP Jakarta」で購入した精密測定器が、サプライヤー側の輸入ライセンス（PI）不備で空港税関で足止めされ、責任境界を確認する場面です。

:::id-example
**Project Engineer (Ardi)**: Halo Mr. David dari perwakilan vendor di Singapura. Kami menerima laporan dari Bea Cukai Bandara Soekarno-Hatta bahwa mesin kalibrasi yang kami pesan tertahan karena tidak ada Surat Persetujuan Impor (PI).  
**Vendor Representative (David)**: Halo Mr. Ardi. Tim forwarder kami di Jakarta sedang mencoba mengurusnya. Apakah perusahaan Anda bisa membantu meminjamkan izin NIB impor Anda untuk mengeluarkan barang tersebut?  
**Project Engineer (Ardi)**: Mohon maaf, Mr. David. Perjanjian kontrak jual beli kita nomor PO-88 adalah murni bersyarat **DDP Tempat Pabrik Cikarang (Incoterms 2020)**.  
**Vendor Representative (David)**: Kami tahu, tetapi regulasi impor di Indonesia sangat rumit dan sering berubah mendadak.  
**Project Engineer (Ardi)**: Menurut aturan DDP, seluruh tanggung jawab pengurusan izin impor, pembayaran bea masuk, pajak impor, risiko kepabeanan, dan biaya penumpukan di bandara (*storage fee*) berada seratus persen di pundak penjual. Pihak pembeli sama sekali tidak berkewajiban menanggung risiko atau meminjamkan izin korporat kami.  
**Vendor Representative (David)**: Kami memahami posisi hukum Anda. Kami mohon maaf atas kelalaian agen forwarder lokal kami.  
**Project Engineer (Ardi)**: Jika barang ini tidak tiba di pabrik kami sebelum hari Jumat, kami akan memberlakukan klausul denda keterlambatan (*liquidated damages*) sebesar satu persen per hari keterlambatan sesuai pasal 12 kontrak.
:::

- **Bandara Soekarno-Hatta**: スカルノ・ハッタ国際空港（ジャカルタの主要国際空港）
- **di pundak penjual**: 売主の双肩（売主の100%全責任）にある
- **biaya penumpukan (storage fee / demurrage)**: 貨物保管料・留置料
- **ganti rugi keterlambatan (liquidated damages)**: 履行遅滞違約金・遅延賠償金

---

## 3. インコタームズ実務で頻出する実務構文集

### 契約書記載・条件合意

- **Harga barang disepakati sebesar sepuluh ribu dolar AS dengan syarat FOB Pelabuhan Tokyo.**  
  （商品価格はFOB東京港条件にて1万米ドルと合意されました。）
- **Sebutkan versi Incoterms secara tegas dalam kontrak, misalnya: "CIF Jakarta (Incoterms 2020)".**  
  （契約書には「CIF Jakarta (Incoterms 2020)」のようにインコタームズの版数を明確に記載してください。）
- **Peralihan risiko atas kerusakan barang terjadi pada saat barang diserahkan kepada pengangkut pertama.**  
  （商品の損傷に関する危険負担の移転は、最初の運送人に商品が引き渡された時点で発生します。）

### 保険金請求・免責確認

- **Segera ajukan pemberitahuan klaim resmi (Notice of Claim) kepada perusahaan asuransi dalam waktu 48 jam.**  
  （48時間以内に保険会社へ正式な損害通知書（Notice of Claim）を提出してください。）
- **Lampirkan Berita Acara Kerusakan (Survey Report) yang diterbitkan oleh surveyor independen.**  
  （独立検査機関（サーベイヤー）が発行した損傷検査報告書を添付してください。）

---

> [!IMPORTANT]
> **DDP条件を安易に受託・発注するリスク**  
> 「DDP（関税込持込渡し）」は買い手にとって最も楽な条件ですが、外国の売り手にとっては「現地に法人や正規輸入ライセンス（NIB/API）がないと税関申告が通らない」という致命的な落とし穴があります。現地通関資格を持たない外国企業と取引する場合は、通関リスクを切り離した**DAP（仕向地持込渡し・通関買主負担）**を選択するのが国際実務上の安全策です。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 海上輸送条件において、売主が運賃と保険料を仕向港まで支払うが、貨物の滅失リスク自体は積出港の本船積載時に買主へ移転するインコタームズ条件は？</summary>

1. CIF (Cost, Insurance, and Freight)  
2. EXW (Ex Works)  
3. DDP (Delivered Duty Paid)  

**正解: 1**  
**解説**: CIF条件は売主が運賃・保険料を負担しますが、危険負担（Risk）は「積出港の本船積載時」に買主へ移転します。
</details>

<details class="id-quiz">
<summary>Q2. インコタームズの中で、売主が仕向国での輸入通関手続きや関税の納付まで全責任を負い、指定場所まで届ける最も売主負担の重い条件は？</summary>

1. DDP (Delivered Duty Paid)  
2. FOB (Free on Board)  
3. FCA (Free Carrier)  

**正解: 1**  
**解説**: 売主が輸入関税・諸税を含めて全てを負担して届ける条件は「DDP（関税込持込渡し）」です。
</details>
