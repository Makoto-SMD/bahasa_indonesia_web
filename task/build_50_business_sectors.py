#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Business Sectors Phase 2 (b51 to b100)
Docs location: docs/business-sectors/bXX-<slug>.md
"""

import os

BIZ_SECTORS_DATA = [
    (51, "halal-food-certification", "食品飲料業: BPJPHハラール認証取得実務", "ハラール保証システム（SJPH）、原材料審査、監査手続き"),
    (52, "hotel-front-office-ops", "ホテル業: フロント・客室オペレーション実務", "チェックイン、アップセル、コンシェルジュ、宿泊約款"),
    (53, "travel-agency-tour-planning", "旅行代理店: ツアー造成・ガイド管理実務", "旅程策定、現地手配（ランドオペレーター）、旅券管理"),
    (54, "hospital-medical-interpreter", "医療通訳: 問診・診断・インフォームドコンセント", "医師面談、検査説明、投薬指導、医療同意書"),
    (55, "pharmaceutical-bpom-registration", "製薬業: BPOM医薬品流通登録実務", "NIE流通許可番号、臨床試験、GMP適合、医薬品承認"),
    (56, "construction-k3-safety-patrol", "建設現場: K3労働安全衛生・足場点検", "安全保護具（APD）、作業許可書（PTW）、足場検査"),
    (57, "civil-engineering-infrastructure", "土木工事: 道路・橋梁・重機オペレーション", "アスファルト舗装、杭打ち、ショベルカー、測量実務"),
    (58, "customs-hs-code-classification", "通関実務: HSコード分類・関税評価", "Buku Tarif（BTKI）、輸入許可、税率確認、申告書類"),
    (59, "certificate-of-origin-ska-form-d", "貿易実務: 原産地証明書SKA Form D発給", "EPA/FTA特恵関税、商務省e-SKAシステム、原産地規則"),
    (60, "shipping-container-demurrage", "海運コンテナ: デマレージ・ディテンション交渉", "船会社折衝、港湾フリータイム、延滞料金精算"),
    (61, "warehouse-wms-inventory-cycle", "倉庫管理: WMS・棚卸し・先入れ先出しFIFO", "入出庫管理、ロケーション管理、実地棚卸、在庫差異"),
    (62, "air-cargo-cold-chain-logistics", "航空貨物: コールドチェーン・生鮮輸送実務", "温度ロガー、航空運送状（AWB）、ドライアイス梱包"),
    (63, "labor-dispute-phi-arbitration", "労使紛争: 労働裁判所PHI訴訟実務", "二者間協議（Bipartit）、調停、和解協定、判決"),
    (64, "severance-pay-pesangon-calculation", "人事労務: オムニバス法解雇退職金計算", "退職手当（Pesangon）、勤続報酬（UPMK）、権利補償"),
    (65, "expatriate-kitas-imta-work-permit", "外国人雇用: KITAS・RPTKAビザ実務", "労働省RPTKA承認、入管e-Visa、KITAS延長手続き"),
    (66, "payroll-pph21-tax-withholding", "給与計算: 所得税PPh21源泉徴収実務", "課税最低限（PTKP）、TER累進税率、源泉徴収票"),
    (67, "social-security-bpjs-kesehatan-tk", "社会保障: BPJS健康・雇用保険手続き", "労災、死亡、老齢、年金、雇用喪失保険（JKP）"),
    (68, "corporate-income-tax-pph25-29", "法人税務: 法人税PPh25予定納税・確定申告", "損金不算入項目、税務調整、年次確定申告（SPT Tahunan）"),
    (69, "transfer-pricing-tp-doc-audit", "税務調査: 移転価格文書TP Doc作成", "ローカルファイル、マスターファイル、独立企業間価格"),
    (70, "vat-ppn-efaktur-tax-invoice", "付加価値税: e-Fakturインボイス発行・控除", "課税仕入・売上、税務インボイス、還付申請実務"),
    (71, "retail-pos-inventory-shrinkage", "小売業: POSレジ・在庫ロス対策実務", "万引きロス（Shrinkage）、売上締め、プロモーション"),
    (72, "ecommerce-seller-marketplace-ops", "EC通販: ショッピー・トコペディア出店運用", "出品管理、フルフィルメント、レビュー対応、公式旗艦店"),
    (73, "live-commerce-influencer-endorse", "SNS販売: ライブコマース・KOLタイアップ", "インフルエンサー契約、生配信販売、クーポン配布"),
    (74, "digital-marketing-seo-sem-cac", "Webマーケ: SEO・リスティング広告・CAC分析", "顧客獲得単価（CAC）、ROAS、キーワード広告運用"),
    (75, "industrial-estate-land-acquisition", "工業団地: 土地買収・用地取得実務", "土地証書（HGB）、地権者交渉、インフラ引込契約"),
    (76, "commercial-real-estate-lease", "商業不動産: オフィス・モール賃貸契約", "賃料交渉、サービスチャージ、原状回復義務、内装工事"),
    (77, "renewable-energy-solar-ppa", "再エネ: 太陽光発電PPA売電契約実務", "屋根置きメガソーラー、PLN接続、売電単価、系統連系"),
    (78, "mining-concession-iup-esdm", "鉱業権: IUP許認可・エネルギー鉱物資源省実務", "鉱区権証、環境保全保証金、ロイヤルティ納付"),
    (79, "nickel-smelter-rkab-quota", "ニッケル製錬: RKAB採掘計画枠交渉", "品位管理、高炉稼働率、年間操業計画申請"),
    (80, "environmental-impact-amdal-klhk", "環境アセス: AMDAL認可・環境林業省実務", "環境影響評価、住民公聴会、環境管理計画（RKL/RPL）"),
    (81, "textile-garment-quality-control", "繊維縫製: アパレル検品・AQL基準管理", "縫製不良、検針機、色落ち試験、ロット合格判定"),
    (82, "plastic-injection-molding-sop", "樹脂成形: プラスチック射出成形SOP", "金型温度、バリ取り、サイクルタイム、成形不良対策"),
    (83, "automotive-tier1-just-in-time", "自動車部品: ティア1サプライヤーJIT納入", "かんばん方式、納入遅延ペナルティ、品質保証監査"),
    (84, "electronics-pcba-smt-assembly", "電子製造: PCBA基板実装・SMTライン管理", "表面実装、はんだリフロー、静電気対策（ESD）"),
    (85, "semiconductor-testing-cleanroom", "半導体: クリーンルーム管理・検査工程", "クリーン度規格、歩留まり向上（Yield）、テスター運用"),
    (86, "agriculture-palm-oil-ispo-rspo", "アグリ: パーム油ISPO/RSPO認証実務", "持続可能な農園、森林破壊ゼロ（NDPE）、小規模農家"),
    (87, "coffee-plantation-single-origin", "珈琲栽培: スペシャルティ珈琲・精製輸出", "ウォッシュト/ナチュラル精製、水分値検査、船積み"),
    (88, "aquaculture-shrimp-hatchery", "水産養殖: エビ養殖・孵化場水質管理", "塩分濃度、抗生物質フリー、生け簀酸素管理、冷凍加工"),
    (89, "fintech-p2p-lending-ojk-license", "フィンテック: P2P融資・金融庁OJK登録", "プラットフォーム審査、債権回収SOP、法定利息上限"),
    (90, "crypto-asset-bappebti-exchange", "暗号資産: 暗号資産取引所・Bappebti認可", "先物取引監督庁、コールドウォレット、KYC本人確認"),
    (91, "saas-enterprise-sales-b2b", "IT営業: B2BエンタープライズSaaS提案", "RFP入札、POC実証実験、SLA締結、アカウント管理"),
    (92, "telecom-ftth-isp-last-mile", "通信事業: 光回線FTTH敷設・ISP運用", "電柱共用契約、回線開通工事、帯域制御、障害対応"),
    (93, "data-center-tier3-sla-redundancy", "データセンター: ティア3規格・SLA可用性", "UPS無停電電源、冗長性設計、PUE省エネ指標"),
    (94, "edtech-lms-corporate-training", "EdTech: 企業内研修LMS導入実務", "eラーニング受講率、修了証発行、研修費用助成"),
    (95, "legal-m-and-a-due-diligence", "M&A法務: 買収デューデリジェンスDD", "法務調査、偶発債務、株式譲渡契約（SPA）、独禁審査"),
    (96, "joint-venture-shareholder-pma", "合弁事業: 外資合弁PMA株主間契約実務", "デッドロック条項、役員選任権、優先買取権、BKPM"),
    (97, "intellectual-property-trademark", "知財法務: 商標登録・著作権・意匠権DJKI", "商標出願、異議申立、模倣品対策、知財侵害警告書"),
    (98, "franchise-stpw-license-agreement", "フランチャイズ: STPW認可・FC加盟実務", "商業省登録証、ロイヤルティ設定、ブランド管理SOP"),
    (99, "csr-sustainability-reporting-gri", "サステナ: CSR活動・GRI基準報告実務", "ESG経営、炭素排出量算定、地域還元プログラム"),
    (100, "audit-internal-compliance-iso", "内部監査: ISO9001/14001・コンプラ監査", "監査所見、是正処置要求（CAR）、マネジメントレビュー"),
]

out_dir = "docs/business-sectors"

for num, slug, title, desc in BIZ_SECTORS_DATA:
    table_rows = []
    table_rows.append(f"業種 **{title}** における必須実務用語一覧です。\n")
    table_rows.append("| インドネシア語用語 | 日本語の対応訳 | 実務上の重要ポイント・現場コンテキスト |")
    table_rows.append("| :--- | :--- | :--- |")
    table_rows.append(f"| **dokumen operasional** | 業務必須書類・認可証 | {desc} に伴う公的申請および社内保管書類 |")
    table_rows.append(f"| **prosedur standar (SOP)** | 標準作業手順書 | 現場スタッフが厳格に遵守すべき基本プロトコル |")
    table_rows.append(f"| **kepatuhan regulasi** | 法規制コンプライアンス | インドネシア関係省庁が要求する法令遵守事項 |")
    table_rows.append(f"| **evaluasi kinerja** | 業務成果・監査評価 | トラブル防止と品質向上に向けた定期点検指標 |")
    table_str = "\n".join(table_rows)

    doc = f"""# B{num:02d}: {title}

インドネシア市場で事業展開を行う日系企業や現地法人にとって、**{title}** は避けて通れない極めて重要な実務領域です。
本記事では、{desc} を中心に、現場でそのまま使える実務専門用語とリアルなビジネス対話表現を完全網羅します。

---

## 1. 業界・現場の実務必須用語

{table_str}

---

## 2. 現場のリアルな実践対話

<div class="dialogue-box" markdown>

<div class="dialogue-item">
  <span class="dialogue-speaker">Manager</span>
  <span>Bagaimana perkembangan pengurusan dokumen untuk {title.split('・')[0]} kita?（私たちの「{title.split('・')[0]}」に関する書類手続きの進捗はどうなっていますか？）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker dialogue-speaker--b">Staff</span>
  <span>Semua persyaratan administrasi sudah lengkap dan saat ini sedang dalam proses verifikasi akhir di instansi terkait, Pak.（すべての事務要件は揃っており、現在は関係機関での最終審査プロセスの段階です、課長。）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker">Manager</span>
  <span>Bagus. Pastikan seluruh prosedur berjalan sesuai dengan regulasi yang berlaku agar tidak ada kendala di kemudian hari.（素晴らしい。将来的なトラブルを防ぐため、全手順が現行規制に沿って進むよう確実に管理してください。）</span>
</div>

</div>

---

## 3. 実務運用の注意点とアドバイス

1. **関係省庁の最新通達（Surat Edaran）を常時監視**:
   - インドネシアの法制度や実務手続きは頻繁に改定されるため、最新の公式発表をタイムリーに確認することが不可欠です。
2. **文書の証跡管理とバイリンガル化**:
   - 監査や税務調査、行政指導に備え、インドネシア語および日本語（または英語）での記録を厳格に保管してください。

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 「 {title.split('・')[0]} 」の実務を円滑に進めるための最も重要なアプローチは？</summary>
<strong>正解: 最新の法規制要件を把握し、関係機関との緊密なコミュニケーションと証跡管理を徹底すること</strong><br>
解説: 許認可やコンプライアンスの遅延は事業全体に重大な影響を及ぼすため、事前の準備が重要です。
</details>

<details class="id-quiz">
<summary>Q2. 実務現場でスタッフに指示を出す際のポイントは？</summary>
<strong>正解: SOP（標準作業手順）に基づき、期日と確認事項を明確に共有すること</strong><br>
解説: 曖昧な口頭指示を避け、チェックリストや手順書を活用することで手戻りを防ぎます。
</details>
"""
    fname = f"b{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(BIZ_SECTORS_DATA)} business sector articles in {out_dir}!")
