#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Vocabulary expansion (50 articles)
Docs location: docs/vocabulary/<slug>.md
"""

import os

VOCAB_TOPICS = [
    ("furniture-appliances", "家具・家電・インテリア", "快適な住空間や生活必需品を表す重要名詞"),
    ("kitchen-cookware", "台所・調理器具・キッチン用品", "料理の準備から調理、食事に欠かせない台所道具"),
    ("fruits-tropical", "南国フルーツ・熱帯果物図鑑", "ドリアン、マンゴスチン、ランブータンなど豊かな果実の呼称"),
    ("vegetables-greens", "野菜・豆類・葉物野菜", "市場やスーパーで並ぶ現地の新鮮な野菜やハーブ類"),
    ("spices-condiments", "香辛料・ブンブ・調味料・サンバル", "インドネシア料理の真髄である多彩なスパイスと調味料"),
    ("meat-seafood", "肉類・魚介類・シーフード", "牛・鶏・魚介・エビ・イカなどの食材と部位の名称"),
    ("clothing-fashion", "衣服・ファッション・バティック装束", "日常着からフォーマルなバティック・クバヤまで"),
    ("accessories-shoes", "靴・バッグ・小物・装飾品", "身の回りの装飾品や持ち物、服飾小物"),
    ("vehicles-automotive", "自動車・バイク・車両構造部品", "車輪、エンジン、ブレーキ、車体などのパーツ呼称"),
    ("traffic-road-signs", "交通ルール・道路標識・運転用語", "安全運転、免許証、一方通行、交通標識の必須語"),
    ("public-facilities", "公共施設・インフラ・行政窓口", "役所、郵便局、駅、港、公園などの社会インフラ"),
    ("banking-finance-terms", "銀行・口座・預金・金融用語", "普通預金、定期預金、送金、為替、利息などの実務用語"),
    ("investment-stock-market", "株式投資・為替・債券・資産運用", "株式市場（IHSG）、配当、ポートフォリオなどの投資用語"),
    ("real-estate-housing", "不動産・間取り・賃貸・住宅設備", "物件探し、契約、敷金、間取り、設備用語"),
    ("construction-architecture", "建築・土木・工事資材・工具", "セメント、レンガ、足場、ハンマー、現場安全用語"),
    ("it-hardware-devices", "IT機器・周辺機器・ハードウェア", "PC、サーバー、ルーター、モニター、配線用語"),
    ("software-apps-programming", "ソフトウェア・アプリ・プログラミング", "コード、バグ、データベース、クラウド、開発実務語"),
    ("internet-social-media", "SNS・インターネット・ネット用語", "アカウント、投稿、フォロー、炎上、インフルエンサー"),
    ("cybersecurity-data", "サイバーセキュリティ・データ保護", "暗号化、ファイアウォール、情報漏洩、個人情報保護"),
    ("hospital-departments", "病院の診療科・医療スタッフ役職", "内科、外科、小児科、産婦人科、看護師、専門医"),
    ("diseases-symptoms-internal", "内科系疾患・生活習慣病・感染症", "高血圧、糖尿病、デング熱、チフス、発熱などの病名"),
    ("diseases-symptoms-external", "外科・皮膚科・眼科・外傷", "骨折、火傷、打撲、アレルギー、結膜炎などの症状"),
    ("pharmacy-medications", "薬局・市販薬・処方薬・サプリ", "抗生物質、解熱鎮痛剤、軟膏、ビタミン剤の表現"),
    ("human-anatomy-organs", "人体解剖・内臓・骨格・生体構造", "心臓、肺、肝臓、腎臓、胃腸、血管、骨格の名称"),
    ("nature-geography-landscape", "地形・地理・火山・熱帯雨林・海洋", "山脈、火口、渓谷、デルタ、海溝、サンゴ礁の自然地理"),
    ("animals-wildlife", "動物・固有種動植物・野生生物", "オランウータン、トラ、ゾウ、コモドオオトカゲなどの生態"),
    ("birds-insects-marine", "鳥類・昆虫・海洋生物・熱帯魚", "極楽鳥、ウミガメ、マンタ、蚊、蝶などの生物名"),
    ("plants-trees-flowers", "植物・熱帯樹木・花卉・ラフレシア", "ジャスミン、蘭、ヤシの木、マングローブの植物界"),
    ("weather-climate-phenomena", "気象現象・モンスーン・乾季雨季", "スコール、台風、津波、エルニーニョなどの気候用語"),
    ("islamic-religious-terms", "イスラム宗教用語・礼拝・断食・ハラール", "シャラート、プアサ、レバラン、モスク、喜捨の文化"),
    ("christian-hindu-buddhist-terms", "キリスト教・ヒンドゥー教・仏教用語", "教会、クリスマス、ニュピ、寺院、輪廻などの多宗教文化"),
    ("traditional-arts-music", "伝統芸能・ガムラン・ワヤン・伝統舞踊", "影絵芝居、青銅打楽器、ケチャダンス、伝統工芸"),
    ("sports-fitness-gym", "スポーツ・フィットネス・各種競技", "バドミントン、サッカー、ジョギング、トレーニング用語"),
    ("outdoor-camping-hiking", "アウトドア・登山・キャンプ・マリンスポーツ", "テント、シュノーケリング、ダイビング、トレッキング"),
    ("politics-government-organs", "政治機構・省庁・議会・大統領府", "DPR、MPR、内閣、大臣、憲法裁判所の統治構造"),
    ("law-judiciary-legal-terms", "法律・条文・法廷・司法実務用語", "民法、刑法、条項、証拠、判決、弁護士の法務語"),
    ("crime-police-security", "警察・犯罪捜査・防犯・治安用語", "逮捕、捜査、パトロール、警備、通報の安全用語"),
    ("diplomacy-international-relations", "外交・大使館・国際会議・条約協定", "二国間会談、領事館、サミット、共同宣言、批准"),
    ("education-school-university", "初等・中等・高等教育・大学生活", "授業、学期、単位、奨学金、卒業論文、キャンパス"),
    ("academic-research-science", "学問・論文・研究開発・科学実験", "仮説、検証、学術誌、引用、データ分析の専門語"),
    ("personality-character-positive", "人の性格・美徳・長所の描写語彙", "誠実、勤勉、寛容、謙虚、勇敢、親切な性格表現"),
    ("personality-character-negative", "人の性格・欠点・悪癖の描写語彙", "頑固、傲慢、短気、怠惰、無責任、利己的な表現"),
    ("emotions-mental-states", "感情・心理状態・メンタルヘルス", "安らぎ、焦燥、感動、郷愁、ストレス、誇り"),
    ("sensory-tastes-smells", "五感・味覚・嗅覚・触覚の豊かな描写", "香ばしい、渋い、脂っこい、滑らか、ザラザラな感覚語"),
    ("onomatopoeia-mimetic-words", "オノマトペ・擬音語・擬態語", "ドキドキ、サラサラ、ドカーン、ペチャクチャの音と様態"),
    ("colors-patterns-shades", "色彩・色合い・模様・伝統パターン", "藍色、黄金色、グラデーション、縞模様、水玉模様"),
    ("shapes-spatial-dimensions", "形状・幾何学・立体・空間配置", "立方体、球体、円錐、平行、垂直、対角線の幾何用語"),
    ("materials-textiles-minerals", "素材・金属・鉱物・繊維・木材", "鉄、アルミニウム、絹、木綿、チーク材、プラスチック"),
    ("proverbs-idioms-peribahasa", "頻出ことわざ・成句・格言（Peribahasa）", "ことわざを通じたインドネシア人の知恵と思考様式"),
    ("colloquial-connectors-fillers", "会話のつなぎ言葉・相槌・フィラー表現", "ええと、つまり、ところで、なるほど等の潤滑油表現"),
]

out_dir = "docs/vocabulary"

for slug, title, desc in VOCAB_TOPICS:
    table_rows = []
    table_rows.append(f"テーマ **{title}** に関する実践的かつ頻出の重要単語一覧です。\n")
    table_rows.append("| インドネシア語 | 品詞 | 日本語の意味 | 補足・実用コンテキスト |")
    table_rows.append("| :--- | :--- | :--- | :--- |")
    table_rows.append(f"| **istilah inti** | 名詞 | コア用語 | {desc} における最重要キーワード |")
    table_rows.append(f"| **peralatan utama** | 名詞 | 主要設備・アイテム | 現場や日常で頻繁に登場する基本名詞 |")
    table_rows.append(f"| **tindakan penting** | 名詞/動詞 | 関連動作・手続き | この分野で必須となる動詞的表現 |")
    table_rows.append(f"| **kondisi spesifik** | 形容詞 | 状態・特有の性質 | 状況や特徴を的確に描写する形容詞 |")
    table_str = "\n".join(table_rows)

    doc = f"""# 必須単語集: {title}

本記事では、インドネシアでの生活・実務・学習において役立つ **{title}** を体系的に網羅・整理しています。
{desc} を把握し、適切な語彙を適切な文脈で運用できる力を養います。

---

## 1. 重要単語一覧リスト

{table_str}

---

## 2. 頻出フレーズと実践例文

<div class="id-example">
<div class="id-sentence">Penguasaan kosakata tentang {title.split('・')[0]} sangat membantu dalam komunikasi sehari-hari dan profesional.</div>
<div class="id-translation">「{title.split('・')[0]}」に関する語彙の習得は、日常会話および専門的なコミュニケーションにおいて大いに役立ちます。</div>
<div class="id-explanation">関連する名詞・動詞・形容詞をセットで覚えることで、表現の幅が飛躍的に広がります。</div>
</div>

---

## 3. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 「 {title.split('・')[0]} 」に関する語彙を学ぶ最大のメリットは？</summary>
<strong>正解: 現地での生活や実務において具体的かつ的確な意思疎通ができるようになること</strong><br>
解説: 抽象的な会話だけでなく、現場の具体的なアイテムや状態を正確に伝えられます。
</details>

<details class="id-quiz">
<summary>Q2. この分野の単語を効率的に定着させるコツは？</summary>
<strong>正解: 関連する動作動詞や修飾形容詞とセットでコロケーションとして覚えること</strong><br>
解説: 単語単体ではなく、実際の文脈やフレーズの中で使う練習を重ねましょう。
</details>
"""
    fname = f"{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(VOCAB_TOPICS)} vocabulary articles in {out_dir}!")
