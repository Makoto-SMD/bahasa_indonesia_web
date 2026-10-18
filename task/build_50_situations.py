#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Situations Phase 2 (s51 to s100)
Docs location: docs/situations/sXX-<slug>.md
"""

import os

SITUATIONS_DATA = [
    (51, "passport-loss-consulate", "パスポート紛失と領事館渡航書発行手続き", "盗難・紛失届、警察証明（Surat Kehilangan）、帰国用渡航書申請"),
    (52, "traffic-accident-police-report", "交通事故・物損事故と警察現場見分", "接触事故、過失割合、示談交渉、警察調書作成実務"),
    (53, "credit-card-fraud-bank-block", "クレジットカード不正利用と銀行カード停止", "不正請求異議申立、カード利用停止、再発行手続き"),
    (54, "plumbing-pipe-leak-emergency", "水道管破裂・水漏れと配管工tukang ledeng修理", "止水栓、階下への水漏れ、配管交換、工賃交渉"),
    (55, "house-moving-damaged-cargo", "引っ越しトラブル・荷物破損クレーム交渉", "家財道具運搬、傷・破損確認、運送業者への補償請求"),
    (56, "school-parent-teacher-conference", "学校の三者面談と学習・進路相談", "成績表確認、学校生活、語学サポート、保護者会面談"),
    (57, "pet-vet-vaccination-emergency", "ペットの急病・動物病院での受診とワクチン接種", "下痢・嘔吐症状説明、血液検査、入院手続き、狂犬病予防"),
    (58, "flight-cancellation-airline-desk", "フライト急遽欠航と空港カウンターでの振替交渉", "悪天候欠航、代替便手配、ホテル宿泊補償、ミールバウチャー"),
    (59, "dengue-hospital-admission", "デング熱発症と総合病院での緊急入院手続き", "高熱・血小板減少、入院保証金（Deposit）、個室希望"),
    (60, "driving-license-sim-renewal", "運転免許証SIM更新と警察署Satpasでの手続き", "適性検査、視力検査、指紋登録、SIM-A/SIM-C発行"),
    (61, "laptop-repair-it-mall-service", "ノートPC故障とITモールでの修理・部品交換", "液晶割れ、SSD交換、データ復旧見積もり、修理保証"),
    (62, "apartment-deposit-return-dispute", "アパート退去時の敷金返還トラブル・原状回復", "敷金（Deposit）返金遅延、経年劣化論争、修理控除精算"),
    (63, "dry-cleaning-clothing-ruined", "高級衣料クリーニング事故と賠償交渉", "色落ち、縮み、シミ残り、クリーニング店責任追及"),
    (64, "internet-wifi-disruption-isp", "光回線Wi-Fi障害とプロバイダへの技術者派遣要請", "モデム赤ランプ点滅、光ファイバー断線、回線復旧依頼"),
    (65, "lost-baggage-airport-lost-found", "ロストバゲージ・手荷物紛失と空港遺失物届", "荷物未着、手荷物引換証（Baggage Tag）、配送先指定"),
    (66, "food-poisoning-clinic-prescription", "食中毒・激しい腹痛と近隣クリニック受診", "脱水症状、点滴投与、経口補水塩（Oralit）、整腸剤処方"),
    (67, "car-battery-flat-roadside-help", "車のバッテリー上がりとロードサービス要請", "エンジン不始動、ジャンピングスタート、レッカー移動"),
    (68, "neighborhood-security-rt-rw-dues", "町内会RT/RWへの転入挨拶と警備費・ゴミ収集費納付", "住民票登録（Lapor Pak RT）、月次治安警備費、ゴミ回収"),
    (69, "motorcycle-tire-puncture-tambal", "バイクのパンクと街角パンク修理屋Tambal Ban", "釘踏みパンク、チューブ補修、空気圧点検、修理代金支払い"),
    (70, "bank-atm-card-swallowed", "ATMにキャッシュカードが吸い込まれた際の緊急対応", "ATM画面フリーズ、コールセンター通報、カード無効化"),
    (71, "gas-cylinder-leak-lpg-safety", "家庭用プロパンガスLPGのガス漏れ点検と交換", "ガス臭、レギュレーターゴムパッキン劣化、ボンベ交換"),
    (72, "electric-token-meter-trip-pln", "電気トークン切れ・ブレーカー落ちとPLN緊急通報", "プリペイド電気番号、トークン番号入力、容量不足相談"),
    (73, "maid-helper-hiring-interview", "住み込みお手伝いさんPembantuの雇用面談と就業条件", "掃除・洗濯・料理スキル、給与手当、帰省休暇条件"),
    (74, "private-driver-probation-rules", "専属運転手Sopirの採用試用期間と走行マナー指示", "安全運転、洗車・ガソリン管理、時間厳守、残業手当"),
    (75, "online-food-delivery-wrong-order", "GrabFood/GoFoodの誤配送・商品不足クレーム", "別注文受領、アプリ返金申請、ドライバー再配送連絡"),
    (76, "courier-package-stolen-porch", "置き配荷物の盗難・行方不明と配送業者追跡調査", "配達完了通知、受取サイン相違、防犯カメラ確認要請"),
    (77, "dentist-toothache-filling-root", "歯の激痛・虫歯治療と歯科クリニックでの神経処置", "麻酔処置、レントゲン撮影、詰め物脱落、根管治療"),
    (78, "eye-clinic-prescription-glasses", "視力低下・眼鏡処方箋と眼鏡店での度数測定", "乱視・近視度数検査、ブルーライトカット、フレーム選定"),
    (79, "gym-membership-cancellation", "フィットネスジムの解約手続きと違約金交渉", "自動引き落とし停止、退会届提出、会員証返却"),
    (80, "hotel-noisy-neighbors-room-change", "ホテルの隣室騒音クレームと部屋替え要請", "夜間パーティー騒音、フロント苦情、静かな別部屋へ移動"),
    (81, "car-rental-breakdown-highway", "レンタカーの高速道路上でのエンストと代車要請", "オーバーヒート、三角停止板設置、代車至急配送要請"),
    (82, "immigration-overstay-fine", "うっかりオーバーステイと入国管理局での罰金納付", "滞在期限超過、1日100万ルピア罰金、出国許可手続き"),
    (83, "police-scam-extortion-defense", "悪質な不当要求に対する冷静な法的自衛", "交通違反言いがかり、正式反則切符（Slip Biru）要求"),
    (84, "stray-dog-bite-rabies-shot", "野良犬・動物咬傷と狂犬病ワクチン緊急接種", "傷口流水洗浄、破傷風注射、狂犬病血清（SAR）投与"),
    (85, "shopping-mall-lost-child", "大型ショッピングモールでの迷子捜索と館内放送依頼", "子供の服装・特徴説明、警備室連絡、館内迷子放送"),
    (86, "tax-office-npwp-registration", "税務署KPPでの個人納税者番号NPWP登録手続き", "パスポート・KITAS提示、オンラインNPWP登録、納税窓口"),
    (87, "embassy-marriage-registration", "国際結婚の婚姻届・出生証明書と領事館手続き", "公的独身証明書、婚姻証明書（Buku Nikah）、領事認証"),
    (88, "customs-airport-tax-on-goods", "空港税関での高額電子機器・酒類課税と申告手続き", "携帯品申告書（e-CD）、500ドル免税枠超過、IMEI登録"),
    (89, "hotel-wedding-reception-booking", "ホテル宴会場での結婚式・パーティー会場下見と見積", "バンケット収容人数、ケータリング試食、音響設備確認"),
    (90, "golf-caddie-booking-tips", "ゴルフ場でのキャディー予約・コース案内とチップ習慣", "ティーオフ時間、キャディフィー、パッティングライン指示"),
    (91, "scuba-diving-equipment-safety", "スキューバダイビング機材チェックと安全ブリーフィング", "残圧計確認、レギュレーター点検、バディ確認、減圧停止"),
    (92, "surfing-lesson-wave-rules", "バリ島サーフィンスクールでの波乗りレッスンとルール", "テイクオフ姿勢、パドリング、前乗り禁止（ドロップイン）"),
    (93, "tailor-batik-shirt-fitting", "オーダーメイドバティックシャツの採寸と仕立て直し", "肩幅・胸囲採寸、裏地（Furing）指定、袖丈直し"),
    (94, "house-cleaning-service-maid", "専門ハウスクリーニング業者へのエアコン・水回り清掃依頼", "エアコン高圧洗浄、ガス補充、浴室水垢・カビ除去"),
    (95, "pest-control-termites-fumigation", "シロアリ・害虫駆除業者への燻蒸消毒見積もり", "木造部食害検査、土壌バリア処理、定期燻蒸保証"),
    (96, "water-purifier-filter-change", "浄水器フィルター交換と飲料水水質検査依頼", "逆浸透膜（RO）膜交換、TDS総溶解固形分測定、水漏れ点検"),
    (97, "car-insurance-claim-survey", "自動車事故保険金請求と損害鑑定サーベイヤー立ち会い", "事故状況説明、修理見積書、免責金額（Own Damage）支払い"),
    (98, "notary-ppat-contract-signing", "公証人役場Notarisでの契約書・公正証書署名実務", "定款認証、宣誓陳述、公証人手数料、印紙貼付（Meterai）"),
    (99, "money-changer-counterfeit-check", "両替所での偽札警戒・大口両替レート交渉", "紙幣シワ・破れ検査、ホログラム確認、電卓レート提示"),
    (100, "farewell-party-speech-colleagues", "現地同僚・スタッフへの送別会での感謝のスピーチ", "任期満了帰任、長年のサポート感謝、今後の友情の誓い"),
]

out_dir = "docs/situations"

for num, slug, title, desc in SITUATIONS_DATA:
    doc = f"""# S{num:02d}: {title}

インドネシア滞在・生活・ビジネスにおいて、突発的なトラブルや専門的な現場対応が求められる代表的場面が **{title}** です。
本記事では、{desc} を中心に、感情的にならず冷静かつ論理的に意思疎通を図るための実践対話と必須構文を完全整理します。

---

## 1. シチュエーション概要と対話のポイント

- **状況設定**: {desc}
- **重要ゴール**: 相手の言い分を正確に聞き取り、こちらの要求や権利を法規・ルールに即して明確に主張する。
- **留意事項**: インドネシア社会では、大声で怒鳴る行為は事態を悪化させます。丁寧な敬称（Pak / Bu）を保ちつつ、事実関係と証拠（Bukti）を提示することが解決への最短ルートです。

---

## 2. 現場の実践リアル対話 (Percakapan Nyata)

<div class="dialogue-box" markdown>

<div class="dialogue-item">
  <span class="dialogue-speaker">Warga / Tamu</span>
  <span>Selamat pagi Pak, mohon maaf mengganggu. Saya ingin menanyakan terkait penanganan {title.split('・')[0]} ini.（おはようございます、お忙しいところ恐れ入ります。この「{title.split('・')[0]}」への対応に関して伺いたいのですが。）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker dialogue-speaker--b">Petugas / Pihak</span>
  <span>Baik Pak, silakan duduk terlebih dahulu. Bisa tolong dijelaskan kronologi kejadian dan dokumen pendukung yang Anda miliki?（承知いたしました。どうぞまずはお座りください。事の経緯と、お持ちの関連書類・証拠をご説明いただけますか？）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker">Warga / Tamu</span>
  <span>Tentu. Ini seluruh bukti dan catatan kronologinya. Kami berharap masalah ini bisa diselesaikan secara adil sesuai prosedur yang berlaku.（もちろんです。こちらがすべての証拠と経緯のメモです。規定の手順に沿って、この問題が公平に解決されることを望んでおります。）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker dialogue-speaker--b">Petugas / Pihak</span>
  <span>Terima kasih atas kelengkapan datanya. Kami akan segera memproses laporan ini dan memberikan pembaruan dalam waktu 24 jam.（詳細なデータを揃えていただきありがとうございます。直ちに報告書を処理し、24時間以内に進捗をご連絡いたします。）</span>
</div>

</div>

---

## 3. この場面で役立つ重要フレーズ集

| インドネシア語フレーズ | 日本語の意味 | 使用場面・ニュアンス |
| :--- | :--- | :--- |
| **Mohon bantuannya untuk mengecek...** | 〜を確認するのを手伝ってください | 状況の調査・確認を丁重に依頼する |
| **Berdasarkan bukti yang ada...** | 存在する証拠に基づきますと… | 客観的事実を提示して交渉する |
| **Berapa lama estimasi prosesnya?** | 手続きの所要見込み時間はどれくらいですか？ | 完了までの期日・目安を確認する |
| **Apakah ada tanda terima resminya?** | 公式な受領書・控えはありますか？ | 証拠書類を確実に受け取る |

---

## 4. トラブル解決のための実践アドバイス

1. **すべてのやり取りをテキスト（WhatsApp等）で記録**:
   - 口頭での約束は忘れられるリスクがあるため、決定事項や金額、期日はメッセージに残して確認を取りましょう。
2. **公式な領収書（Kwitansi / Tanda Terima）の受領**:
   - 費用を支払う際は、受領印や署名のある正規の領収書を必ず発行してもらいましょう。

---

## 5. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. トラブル発生時に最も優先すべき行動は？</summary>
<strong>正解: 冷静さを保ち、発生経緯（クロノロジー）と客観的証拠を整理して記録すること</strong><br>
解説: 感情的にならず、事実関係を時系列で論理的に説明することが信頼と迅速な対応につながります。
</details>

<details class="id-quiz">
<summary>Q2. 相手に期日や所要時間の目安を尋ねる適切な表現は？</summary>
<strong>正解: Berapa lama estimasi waktu yang dibutuhkan?</strong><br>
解説: estimasi（見積もり・見込み）を用いて、所要期間を明確に確認します。
</details>
"""
    fname = f"s{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(SITUATIONS_DATA)} situation articles in {out_dir}!")
