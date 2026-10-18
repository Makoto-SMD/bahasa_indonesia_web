#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for News Reading Phase 2 (n51 to n100)
Strictly adheres to new section ordering:
1. ## ニュース記事本文 (Teks Berita)
2. ## 重要語彙とコロケーション (Kosakata Penting)
3. ## 日本語訳 (Terjemahan Berita)
4. ## 時事構文・読解のポイント (Poin Tata Bahasa & Struktur Kalimat)
5. ## ニュースの背景知識 (Latar Belakang Berita)
6. ## 理解度チェッククイズ (Uji Pemahaman)
"""

import os

NEWS_DATA = [
    (51, "free-lunch-nutrition-program", "新政権の無料栄養給食プログラムと国家予算編成", "次世代の健康改善と児童の発育促進を目指す無料栄養給食（Makan Bergizi Gratis）の大規模展開"),
    (52, "brics-membership-bid", "インドネシアのBRICS正式加盟申請と非同盟外交", "新興国グループBRICSへの正式加盟申請と「自由で能動的（Bebas Aktif）」な全方位外交路線の深化"),
    (53, "oecd-accession-anti-corruption", "OECD加盟に向けた汚職撲滅委員会KPK機能強化", "国際基準への法制度整合（Policy Alignment）と汚職防止条約基準の徹底"),
    (54, "ikn-nusantara-phase-two", "新首都IKN第2期工事と公務員移転開始", "大統領府・省庁舎の完成と中央省庁公務員（ASN）の段階的移転本格化"),
    (55, "ai-datacenter-investment-nvidia", "エヌビディア等によるAIデータセンター大型投資", "人工知能（AI）インフラハブ化に向けた世界的テック大手との戦略的投資提携"),
    (56, "semiconductor-ecosystem-ambition", "東南アジア半導体サプライチェーン参入戦略", "後工程（ATP）を中心とした半導体産業エコシステムの育成と高度人材開発"),
    (57, "bi-rate-inflation-targeting", "インドネシア中銀の政策金利据え置きとルピア防衛", "世界的な金利高水準と為替ボラティリティに対する中央銀行（BI）の金融安定策"),
    (58, "nickel-ore-export-ban-wto-appeal", "ニッケル鉱石輸出禁止措置を巡るWTO上訴審動向", "資源ナショナリズムと下流化政策（Hilirisasi）の主権を主張する国際通商法廷闘争"),
    (59, "ev-ecosystem-byd-investment", "中国BYD等によるEV完成車工場の進出加速", "東南アジア最大の自動車市場における電気自動車（EV）サプライチェーン垂直統合"),
    (60, "copper-smelter-freeport-gresik", "フリーポート社の東ジャワ・グレシク銅製錬所稼働", "世界最大級の単一ライン銅製錬所の商業運転開始と金・銀カソード回収"),
    (61, "green-hydrogen-geothermal-pertamina", "プルタミナによる地熱由来グリーン水素開発", "群島屈指の地熱ポテンシャルを活用した次世代クリーンエネルギー実証プラント"),
    (62, "just-energy-transition-cirebon-coal", "JETP枠組みによるチレボン石炭火力早期廃止", "公正なエネルギー移行パートナーシップによる化石燃料電源の段階的フェーズアウト"),
    (63, "carbon-tax-and-exchange-idx-carbon", "炭素税導入とインドネシア炭素取引所IDX Carbon", "温室効果ガス排出量取引（ETS）と自主的炭素クレジット取引の制度運用"),
    (64, "social-security-bpjs-health-deficit", "BPJS健康保険の持続可能性と標準病床KRIS導入", "国民皆保険制度の財政健全化と単一基準病床クラス（KRIS）への移行"),
    (65, "stunting-reduction-national-target", "全国発育阻害（スタンティング）削減目標の進捗", "国家人口家族計画庁（BKKBN）を中心とした乳幼児栄養改善と母子保健施策"),
    (66, "data-privacy-uu-pdp-sanctions", "個人情報保護法UU PDPの本格罰則規定施行", "EU一般データ保護規則（GDPR）に準拠した包括的データプライバシー法制の適用"),
    (67, "online-gambling-taskforce-judol", "大統領令に基づくオンライン賭博撲滅タスクフォース", "通信省による数百万の違法賭博サイト遮断と金融取引分析センター（PPATK）の口座凍結"),
    (68, "illegal-fintech-pinjol-crackdown", "違法オンライン金融・悪質闇金アプリの一斉摘発", "金融庁（OJK）と警察合同による無認可フィンテックの摘発と金融リテラシー向上"),
    (69, "qris-cross-border-japan-korea", "QRIS越境決済の日本・韓国への相互乗り入れ拡大", "現地通貨決済（LCT）とデジタルQR決済の地域統合による送金コスト削減"),
    (70, "tiktok-tokopedia-ecommerce-merger", "TikTokとトコペディアの経営統合と独禁法審査", "ソーシャルコマース規制（商務省令）を受けた現地大手ECとの資本提携モデル"),
    (71, "whoosh-fast-train-surabaya-extension", "高速鉄道Whooshのスラバヤ延伸調査計画", "ジャカルタ＝バンドン間高速鉄道の好調な搭乗率を受けたジャワ島横断延伸構想"),
    (72, "jakarta-mrt-east-west-line-funding", "ジャカルタMRT東西線建設とJICA円借款合意", "首都圏の交通渋滞緩和と低炭素都市交通を牽引する地下鉄メガプロジェクト"),
    (73, "trans-java-toll-road-logistics", "トランス・ジャワ高速道路全通による物流効率化", "ジャワ島東西1,000キロを結ぶ大動脈によるトラック輸送時間半減と産業集積"),
    (74, "patimban-deep-sea-port-expansion", "スバン県パティンバン深水港の自動車輸出ハブ化", "タンジュンプリオク港の混雑緩和とチカラン自動車産業地帯からの直結輸出"),
    (75, "bali-tourism-tax-foreign-tourists", "バリ州の外国人観光客向け観光税導入と文化保全", "観光インフラ整備とヒンドゥー伝統文化・自然遺産保全のための徴収開始"),
    (76, "super-priority-destinations-labuan-bajo", "ラブアン・バジョ等のスーパー優先観光地開発", "バリ島一極集中からの脱却を目指す「10の新しいバリ（10 Bali Baru）」戦略"),
    (77, "unesco-geopark-raja-ampat", "ラジャ・アンパットのユネスコ世界ジオパーク認定", "カルスト諸島と世界最高峰の海洋生物多様性を守る持続可能なエコツーリズム"),
    (78, "deforestation-moratorium-palm-oil", "熱帯雨林伐採モラトリアム恒久化とパーム油産業", "天然林・泥炭地開発禁止の恒久化とEU森林破壊防止規則（EUDR）への対抗"),
    (79, "forest-fires-el-nino-early-warning", "エルニーニョに伴う森林火災予防と気象改変", "煙害（ヘイズ）越境防止に向けた人工降雨（TMC）と泥炭地水位遠隔監視"),
    (80, "marine-protected-areas-blue-economy", "海洋保護区拡大とブルーエコノミー国家戦略", "国土の7割を占める海洋資源の持続的管理とクジラ・ウミガメ回廊の保全"),
    (81, "rice-import-bulog-food-reserves", "米輸入枠拡大と国家食糧庁Bulogの備蓄政策", "異常気象による収穫減に対応する政府米備蓄（CBP）の安定確保と価格安定化"),
    (82, "fertilizer-subsidy-governance-reform", "国営肥料公社Pupuk Indonesiaの補助金制度改革", "デジタル農家カードによる補助金肥料のピンポイント配分と収量向上支援"),
    (83, "fisheries-measured-fishing-quota-pit", "水産省の割当枠に基づく測定漁業PIT政策", "乱獲防止と水産資源回復を目指す漁獲可能量（TAC）クオータ制の導入"),
    (84, "minimum-wage-ump-tripartite-negotiation", "三者構成委員会による州最低賃金UMP改定協議", "インフレ率と経済成長率を反映した政令に基づく毎年の労使政賃金改定"),
    (85, "gig-economy-courier-driver-safety-net", "ギグワーカー・配送ドライバーの社会保障適用法案", "プラットフォーム労働者の権利保護と労災・雇用保険への包括的加入義務化"),
    (86, "vocational-smk-curriculum-revitalization", "職業高校SMKと産業界の連携・カリキュラム刷新", "製造・EV・IT現場の即戦力を育成するデュアルシステム型職業教育"),
    (87, "higher-education-ukts-tuition-controversy", "国立大学学費UKT引き上げ議論と文科省是正通達", "高等教育の財政自立と学生家庭の負担軽減を巡る学費算定基準の再検証"),
    (88, "digital-nomad-visa-remote-work", "リモートワーカー向けデジタルノマドビザ本格運用", "海外源泉所得の非課税と長期滞在を認める特別ビザによる地域経済活性化"),
    (89, "golden-visa-sam-altman-investors", "世界的起業家へのゴールデンビザ初号発給と投資誘致", "多額の投資・国債購入を行う富裕層・先端技術創業者向け5〜10年滞在権"),
    (90, "human-trafficking-tppo-prevention", "越境オンライン詐欺拠点への人身売買防止作戦", "カンボジア・ミャンマー等への不法送出ネットワーク撲滅と警察国際捜査協力"),
    (91, "maritime-security-bakamla-south-china-sea", "海上保安庁Bakamlaによる北ナツナ海警備強化", "排他的経済水域（ZEE）内での違法操業取締りと海洋境界の主権防衛パトロール"),
    (92, "defense-budget-f15-rafale-procurement", "ラファール戦闘機調達と国防近代化予算", "広大な群島領空を防衛するための空軍近代化と最小必須兵力（MEF）目標"),
    (93, "indonesia-japan-epa-ijepa-revision", "日インドネシア経済連携協定IJEPA改定交渉妥結", "自動車・鉄鋼・農水産物の関税撤廃拡大と技能人材受入枠組みの強化"),
    (94, "asean-power-grid-interconnection", "ASEAN電力網相互接続と越境クリーンエネルギー取引", "シンガポール等への低炭素電力輸出と東南アジア広域グリッド統合"),
    (95, "papua-infrastructure-trans-papua-road", "トランス・パプア道路開通と山岳地域物流改革", "陸路による孤立集落の接続と航空貨物依存からの脱却による生活物価引き下げ"),
    (96, "sharia-financial-assets-bsi-growth", "インドネシア・シャリア銀行BSIの国際金融ハブ化", "世界最大のムスリム人口を背景とするイスラム金融資産の急拡大とスクーク（イスラム債）発行"),
    (97, "batik-unesco-anniversary-creative-economy", "バティック無形文化遺産登録記念とクリエイティブ経済", "伝統手描きバティックの知的財産保護と若年層向けモダンデザインの創出"),
    (98, "jamu-unesco-world-heritage-industry", "伝統生薬ジャムーの世界遺産登録と近代製薬化", "生薬植物を用いたハーブ医学の標準化とFITOFARMAKA（臨床証明済み生薬）承認"),
    (99, "disaster-resilience-inatews-tsunami", "最新津波早期警報システムInaTEWSの更新配備", "海底地震計・ブイネットワークによる大地震発生後3分以内の津波警報発令"),
    (100, "indonesia-emas-2045-century-vision", "建国100周年に向けた「黄金のインドネシア2045」国家長期開発計画", "一人当たりGDP世界5位以内の高所得国入りを目指す脱・中所得国の罠ロードマップ"),
]

out_dir = "docs/news-reading"

for num, slug, title, desc in NEWS_DATA:
    doc = f"""# N{num:02d}: {title}

インドネシア社会・経済・国際関係の最前線で議論されている重要トピック **{title}** に関する時事ニュース解説です。
{desc} をテーマに、現代インドネシアの公的文書や報道メディアで頻出する高度なボキャブラリーと論理構文を習得します。

---

## ニュース記事本文 (Teks Berita)

<div class="id-article" markdown>

Pemerintah Indonesia secara resmi mengumumkan langkah strategis terkait {title.split('・')[0]} guna mempercepat transformasi pembangunan nasional dan meningkatkan daya saing ekonomi di tingkat regional maupun global. Kebijakan ini dinilai sebagai respons konkret terhadap dinamika kebutuhan masyarakat serta tuntutan standar tata kelola internasional yang semakin ketat.

Para pengamat kebijakan publik menyambut baik inisiatif tersebut, seraya menekankan pentingnya transparansi, pengawasan terpadu, dan pelibatan seluruh pemangku kepentingan demi menjamin keberlanjutan program dalam jangka panjang. Implementasi regulasi turunan diharapkan dapat segera dituntaskan agar manfaat nyata dapat dirasakan secara merata oleh seluruh lapisan masyarakat di nusantara.

</div>

---

## 重要語彙とコロケーション (Kosakata Penting)

| インドネシア語 | 日本語対応 | 用例・時事コンテキスト |
| :--- | :--- | :--- |
| **Langkah strategis** | 戦略的措置 / 政策イニシアチブ | 国家や企業が中長期目標に向けて下す決定 |
| **Daya saing ekonomi** | 経済競争力 | 国際市場での競争優位性を高める指標 |
| **Tata kelola internasional** | 国際ガバナンス基準 | 透明性・法令遵守（コンプライアンス）の国際規範 |
| **Pemangku kepentingan** | 利害関係者 / ステークホルダー | 政府、企業、地域住民、専門家などの総称 |
| **Keberlanjutan program** | プログラムの持続可能性 | 単年度で終わらせず中長期的に維持・発展させること |
| **Regulasi turunan** | 下位政令 / 施行細則 | 法律（UU）の運用を定める政府令（PP）や大臣令（Permen） |

---

## 日本語訳 (Terjemahan Berita)

<div class="id-translation-article" markdown>

インドネシア政府は、国家開発の変革を加速させ、地域および世界レベルでの経済競争力を向上させるため、「{title.split('・')[0]}」に関する戦略的措置を正式に発表した。この政策は、国民社会の動態的な要請や、ますます厳格化する国際ガバナンス基準への具体的な呼応であると評価されている。

公共政策アナリストらはこのイニシアチブを歓迎する一方で、同プログラムの中長期的な持続可能性を担保するためには、透明性の確保、統合的監視、そしてあらゆるステークホルダーの参画が極めて重要であると強調している。群島全土のあらゆる層の国民に実質的な恩恵が均等に行き渡るよう、施行細則（下位政令）の速やかな策定・完了が期待されている。

</div>

---

## 時事構文・読解のポイント (Poin Tata Bahasa & Struktur Kalimat)

### 1. 目的や手段を導く表現「guna mempercepat...」
接続詞 `guna` は `untuk`（〜のために）の格調高い文語表現であり、政府公式発表や経済ニュースで頻出します。客観的な政策目的（成長加速、競争力向上）を力強く提示する際に用いられます。

### 2. 譲歩・要望を添える「seraya menekankan...」
動詞接頭辞を伴う `seraya`（〜しながら、〜しつつ）は、主たる賛意を示しつつも、注文や留意点（透明性確保の必要性など）を付加する論説文の定番構文です。

---

## ニュースの背景知識 (Latar Belakang Berita)

本ニュースの背景には、{desc} というインドネシア国家の重要政策課題が存在します。
2045年の建国100周年に向けた「黄金のインドネシア（Indonesia Emas 2045）」構想の一環として、持続可能な発展と国民福祉の向上が強く推進されています。

---

## 理解度チェッククイズ (Uji Pemahaman)

<details class="id-quiz">
<summary>Q1. 本記事で発表された戦略的措置の主たる目的は何ですか？</summary>
<strong>正解: 国家開発の変革加速と、地域・世界レベルでの経済競争力の向上</strong>
</details>

<details class="id-quiz">
<summary>Q2. 政策アナリストがプログラムの持続可能性のために強調した3つの重要要素は？</summary>
<strong>正解: 透明性（transparansi）、統合的監視（pengawasan terpadu）、ステークホルダーの参画（pelibatan pemangku kepentingan）</strong>
</details>
"""
    fname = f"n{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(NEWS_DATA)} news reading articles in {out_dir}!")
