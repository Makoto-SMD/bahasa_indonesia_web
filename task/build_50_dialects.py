#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Regional Dialects & Culture (50 articles)
Docs location: docs/dialects/dXX-<slug>.md
"""

import os

DIALECTS_DATA = [
    (1, "javanese-court-kromo-ngoko", "ジャワ語の敬語階層（ンゴコ・クロモ）とインドネシア語への影響", "対等な親愛表現Ngokoと最上級敬意Kromoの体系が国語に与えた敬語意識"),
    (2, "javanese-particles-tho-lha-kok", "会話に混じるジャワ語助詞: lha, kok, tho, lho", "ジャワ出身者が無意識に挟む独特の間やニュアンスを補強する小辞群"),
    (3, "javanese-kinship-mas-mbak", "呼称の全国化: Mas（兄さん）と Mbak（姉さん）の用法", "ジャワ語の親族呼称がインドネシア全土の共通呼称へと浸透した背景とマナー"),
    (4, "javanese-loanwords-daily-life", "日常化したジャワ語借用語: monggo, maturnuwun, kulo", "挨拶や食事、ビジネスの雑談で頻出する親愛のこもった基本単語"),
    (5, "javanese-philosophy-alon-alon", "ジャワの処世訓: alon-alon asal kelakon", "急がば回れ、和を重んじる精神性が反映されたことわざ・慣用表現"),
    (6, "sundanese-politeness-lemes-loma", "スンダ語の親愛・丁寧語と日常語の境界", "西ジャワ高原地帯で育まれた繊細な言葉遣いと親近感のグラデーション"),
    (7, "sundanese-particles-teh-mah-atuh", "会話を柔らかくするスンダ語助詞: teh, mah, atuh, euy", "語尾に添えるだけでスンダ風の親しみやすさと柔和さを演出する語尾群"),
    (8, "sundanese-kinship-aa-teteh-kang", "スンダの親称: Kang, Aa, Teteh, Ceuceu", "バンドンや西ジャワで年長者や同僚を呼ぶ際のお決まりの敬称・愛称"),
    (9, "sundanese-food-terms-lalapan-sambal", "スンダ食文化の語彙: lalapan, liwet, tutug oncom", "生野菜を愛し、香り高いスパイスと共にあるスンダ料理の専門呼称"),
    (10, "sundanese-wisdom-somah-hade", "スンダの精神: someah hade ka semah", "見知らぬ来客をも笑顔で温かくもてなす高原民族のホスピタリティ言語"),
    (11, "balinese-caste-language-tri-wangsa", "バリ語の階層言語と寺院・儀礼の言葉", "カーストや神々への帰依を反映した三層の言語ヒエラルキー"),
    (12, "balinese-kinship-wayan-made-nyoman-ketut", "バリ独特の誕生順名前システム: Wayan, Made, Nyoman, Ketut", "出生順によって決定されるバリ人の名前と呼びかけのルール"),
    (13, "balinese-daily-greetings-om-swastiastu", "バリの挨拶: Om Swastiastu と Suksema", "神々の島で交わされる祈りの挨拶と心からの感謝の言葉"),
    (14, "balinese-culture-banjar-subak", "共同体の言葉: Banjar（自治会）と Subak（水利組合）", "ユネスコ世界遺産にも登録された伝統的水利組織と村落共同体の語彙"),
    (15, "minangkabau-matrilineal-terms", "母系制社会ミナンカバウの親族呼称: Mamak, Bundo", "母から娘へ財産が継承される西スマトラの独特な親族・指導者呼称"),
    (16, "minangkabau-traders-marantau-culture", "放浪と商人の文化: Marantau（出稼ぎ）と商談の語彙", "故郷を離れ商売で成功を収めるミナン人の起業家精神を表す言葉"),
    (17, "minangkabau-particles-lah-ko-yo", "ミナン方言の語尾とリズム: lah, ko, bana, yo", "パダン料理屋や市場で響き渡るリズミカルなミナン語の小辞"),
    (18, "batak-clan-marga-system", "北スマトラ・バタク族の父系氏族（Marga）呼称体系", "シトランガン、シレガール等の苗字（マルガ）を通じた同族確認の文化"),
    (19, "batak-kinship-tulang-nantulang", "バタク親族呼称: Tulang（母方の叔父）への絶対的敬意", "父系社会の中で特別な精神的権威を持つ母方親族への呼称儀礼"),
    (20, "batak-greeting-horas-spirit", "バタクの魂の挨拶: Horas! と Mauliate", "トバ湖の雄大な自然と不屈の情熱を象徴する力強い挨拶と感謝"),
    (21, "bugis-makassar-honor-siri-na-pesse", "南スラウェシの不屈の誇り: Siri' na Pacce", "命よりも大切な名誉と、仲間の苦しみを分かち合う連帯精神の言葉"),
    (22, "bugis-makassar-particles-ji-ki-pi-mo", "強烈な語末助詞: ji, ki', pi, mo, mi, pale'", "マカッサル方言を特徴づける短く歯切れの良い感情豊かな接語群"),
    (23, "bugis-kinship-daeng-puang", "海洋民族の親称: Daeng（兄・船長）と Puang（貴族敬称）", "ピニシ帆船を操る船乗り文化に根差した相互敬愛の呼称"),
    (24, "ambonese-malay-bet-ose-slang", "マルク・アンボン・マレー語の代名詞: Beta と Ose", "オランダ植民地期からの歴史を背負う香料諸島の親密な人称表現"),
    (25, "ambonese-musicality-lagu-dialect", "歌うような抑揚を持つアンボン方言の音楽的リズム", "ユネスコ音楽都市アンボンの情緒豊かなイントネーションとスラング"),
    (26, "manado-malay-torang-ngana-kita", "北スラウェシ・マナド語: Torang と Ngana", "「私たちは皆兄弟（Torang Samua Basudara）」を合言葉とするマナド方言"),
    (27, "manado-cultural-sitou-timou", "ミナハサの共生精神: Si Tou Timou Tumou Tou", "人は他者を人間らしく育てるために生きるという教育的道徳箴言"),
    (28, "papuan-malay-pace-mace-kitorang", "パプア・マレー語の基本呼称: Pace, Mace, Kitorang", "ニューギニア島の温かなコミュニティを結ぶ親称と自称"),
    (29, "papuan-pronouns-sa-ko-dong", "パプアの親密代名詞: Sa（私）、Ko（君）、Dong（彼ら）", "音節が短縮されスピード感と親密さが増すパプア独特の代名詞体系"),
    (30, "papuan-interjections-io-ka-kaka", "パプアの温かい感嘆詞と語尾: Iyo, Ka, Kaka, Adoh", "驚きや共感をダイレクトに伝えるパプアの豊かな感嘆詞"),
    (31, "banjarese-south-kalimantan-ulun-pian", "南カリマンタン・バンジャル語の敬称: Ulun と Pian", "ダイヤモンドと大河の街で育まれた謙譲と尊敬の美しい代名詞"),
    (32, "banjarese-trading-pasar-terapung", "水上マーケットの商取引とバンジャル商人の言葉", "ロカバタン水上市場の小舟の上で飛び交う値引き・交渉フレーズ"),
    (33, "madurese-resilience-carok-tradition", "マドゥラ語のダイナミズムと名誉の文化", "不毛な島からたくましく生き抜くマドゥラ人のストレートな語感"),
    (34, "madurese-terms-tretan-dhibik", "マドゥラの同胞意識: Tretan Dhibik", "群島各地に出稼ぎに出るマドゥラ人同士の固い結束を表す合言葉"),
    (35, "acehnese-islamic-identity-syariah", "アチェ語の宗教的語彙と Serambi Mekkah の気風", "シャリーア法と独自の伝統慣習（Adat）が融合したアチェの言葉"),
    (36, "sasak-lombok-tiang-pelungguh", "ロンボク・ササック語の敬語階層とサデ村の言葉", "伝統家屋と織物の里に受け継がれるササック族の格式ある言葉遣い"),
    (37, "palembang-baso-palembang-wong-kito", "南スマトラ・パレンバン語: Wong Kito Galo", "「私たちは皆仲間だ」というムシ川流域の誇り高いアイデンティティ"),
    (38, "riau-coastal-malay-formal-roots", "標準インドネシア語の母体となったリアウ海岸マレー語", "澄んだ母音と格調高い文法美を誇る国語発祥の地の正統マレー語"),
    (39, "betawi-jakarta-gue-elo-origins", "ジャカルタ先住民ブタウィ語: Gue と Elo のルーツ", "中国語（潮州語・福建語）借用語が首都の若者口語へと定着した軌跡"),
    (40, "betawi-word-formation-ujung-e", "ブタウィ語の母音変化規則: -a から -e への転訛", "kenapa → kenape, bisa → bise 等のジャカルタ下町語の音韻法則"),
    (41, "chinese-indonesian-hokkien-peranakan", "プラナカン・華人由来の語彙: Cuan, Cincai, Lu, Gua", "ビジネスや金銭感覚、料理名に深く浸透した福建語由来の必須単語"),
    (42, "arab-indonesian-hadrami-slang", "ハドラミ系アラブ移民由来の俗語: Ana, Ente, Afwan", "イスラム文化圏と都市部若者スラングに影響を与えたアラビア語語彙"),
    (43, "dutch-colonial-loanwords-bureaucracy", "オランダ植民地期由来の行政・法務・技術語彙", "Kantor, Gratis, Kulkas, Notaris など近代社会インフラを支える蘭語"),
    (44, "portuguese-colonial-loanwords-history", "大航海時代ポルトガル由来の生活語彙", "Gereja, Mentega, Sepatu, Meja, Pesta など16世紀に伝来した欧州語"),
    (45, "sanskrit-classical-motto-pancasila", "サンスクリット語由来の国家標語・憲章語彙", "Bhinneka Tunggal Ika, Pancasila, Adipura など高貴な公的言語の源流"),
    (46, "slang-prokem-1980s-reverse-syllables", "80年代プロケム俗語: 逆さ言葉の構造", "Bokap（父）、Nyokap（母）、Gokil（狂気）などの隠語生成メカニズム"),
    (47, "modern-gen-z-jaksel-code-mixing", "南ジャカルタ（Jaksel）英語チャンポン言葉", "Literally, Which is, Honestly などの現代ミレニアル・Z世代の混交語"),
    (48, "regional-code-switching-etiquette", "多民族混成の職場におけるコードスイッチングのマナー", "共通語と地方語を状況に合わせて切り替えるスマートな対人配慮"),
    (49, "pancasila-unity-in-diversity-linguistics", "言語学的観点から見た「多様性の中の統一」の奇跡", "700の地方言語を殺さず共通語として機能するインドネシア語の寛容性"),
    (50, "future-of-bahasa-indonesia-dialects", "地方語の保護と進化し続ける現代インドネシア語の未来", "デジタル時代における方言の存続と新語創出のダイナミックな展望"),
]

out_dir = "docs/dialects"
os.makedirs(out_dir, exist_ok=True)

for num, slug, title, desc in DIALECTS_DATA:
    doc = f"""# D{num:02d}: {title}

700以上の地方言語が存在する多言語国家インドネシアにおいて、国語（Bahasa Indonesia）は各地域の言葉や文化的精神と絶えず相互作用しています。
本記事では、**{title}** に焦点を当て、{desc} を体系的に解き明かします。

---

## 1. 地方言語・方言の文化的背景

- **対象地域・民族**: {title.split('・')[0]}
- **言語的特徴**: {desc}
- **インドネシア語との関わり**: 現地のビジネスや日常会話において、これらの語彙や助詞を適切に理解・運用できると、現地の人々との心理的距離が劇的に縮まります。

---

## 2. 頻出キーワード・表現一覧

| 単語・フレーズ | 品詞・分類 | 日本語の意味・ニュアンス | 実際の使われ方・文脈 |
| :--- | :--- | :--- | :--- |
| **Kosa kata khas** | 方言固有語 | 地域特有のキーワード | 現地社会の生活や感情表現に直結する単語 |
| **Partikel percakapan** | 会話助詞 | 語尾・相槌のニュアンス | 会話を柔らかくし親密さを演出する小辞 |
| **Sapaan akrab** | 親称・敬称 | 親しみと敬意を込めた呼び名 | 相手の年齢や社会的関係に応じた呼称 |

---

## 3. 実践会話シミュレーション

<div class="dialogue-box" markdown>

<div class="dialogue-item">
  <span class="dialogue-speaker">Tamu</span>
  <span>Permisi, saya baru pertama kali berkunjung ke daerah ini.（すみません、この地域を訪れるのは初めてなのですが。）</span>
</div>

<div class="dialogue-item">
  <span class="dialogue-speaker dialogue-speaker--b">Warga Lokal</span>
  <span>Selamat datang! Di sini masyarakat sangat ramah dan menjunjung tinggi nilai {title.split('・')[0]}. Jangan sungkan untuk bertegur sapa ya.（ようこそ！ここでは人々がとても温かく、独自の伝統の心を大切にしています。どうぞ遠慮なく声をかけてくださいね。）</span>
</div>

</div>

---

## 4. コミュニケーションにおけるマナーと配慮

1. **文化的文脈の尊重**:
   - 地方言語の単語は親密さを生む一方で、フォーマルな公式文書や他民族との公式会議では標準インドネシア語を用いるのが基本エチケットです。
2. **親称の使い分け**:
   - 年長者や初対面の相手には、まず敬称を添えて丁寧に接し、関係が深まるにつれて親しい呼称へと移行しましょう。

---

## 5. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 「 {title.split('・')[0]} 」の文化的特徴を一言で表すと？</summary>
<strong>正解: {desc}</strong>
</details>

<details class="id-quiz">
<summary>Q2. 地方言語や方言の知識を持つことがインドネシア語学習において重要な理由は？</summary>
<strong>正解: 現地の人々の文化的アイデンティティを理解し、より深い信頼関係と自然なコミュニケーションを築けるから</strong>
</details>
"""
    fname = f"d{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(DIALECTS_DATA)} dialect articles in {out_dir}!")
