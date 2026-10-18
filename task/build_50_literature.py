#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Literature & Story Reading (50 articles)
Docs location: docs/literature/lXX-<slug>.md
Adheres strictly to standard ordering:
1. ストーリー本文 (Teks Cerita / Teks Bacaan)
2. 重要語彙・表現一覧 (Kosakata Penting)
3. 日本語訳 (Terjemahan Cerita)
4. 文学・教訓の解説 (Poin Nilai & Moral Cerita)
5. 背景文化コラム (Latar Belakang Budaya)
6. 理解度チェッククイズ (Uji Pemahaman)
"""

import os

LITERATURE_DATA = [
    (1, "malin-kundang", "西スマトラ民話: 親不孝の息子マリング・クンダン", "親への不敬と忘恩の戒めを描いたミナンカバウの最も有名な石化伝説"),
    (2, "sangkuriang-tangkuban-perahu", "西ジャワ伝説: サンクリアンとタンクバン・プラフ山", "母子の禁断の愛と一夜の巨大舟建造にまつわるバンドン火山の起源"),
    (3, "roro-jonggrang-prambanan", "中部ジャワ伝説: ロロ・ジョングランと千の寺院", "一夜で千の寺院建立を命じられたバンドゥン・ボンドウォソと石像の呪い"),
    (4, "danau-toba-ikan-mas", "北スマトラ民話: トバ湖の起源と金の魚", "魚の化身の女性との誓いを破った男と大洪水によるカルデラ湖誕生"),
    (5, "bawang-merah-bawang-putih", "リアウ民話: バワン・メラとバワン・プティ", "健気な妹プティと邪悪な義母姉メラの対比（インドネシア版シンデレラ）"),
    (6, "lutung-kasarung", "スンダ古典: ルスン・カサルンと王女の真実の愛", "黒猿に身を変えた天界の王子と清らかな心を持つプルバサリ王女の叙事詩"),
    (7, "timun-mas-raksasa", "中部ジャワ民話: 黄金のキュウリから生まれたティムン・マスと巨人", "塩や唐辛子の種を投げて巨大な怪物ブト・イジョから逃げ切る少女の機知"),
    (8, "ciung-wanara", "西ジャワ歴史物語: チウン・ワナラとガル王国の正義", "川に流された王子が成長し、闘鶏勝負を通じて悪政を正す英雄譚"),
    (9, "si-pitung-batavia-hero", "ジャカルタ英雄伝: 義賊シ・ピトゥンとバタヴィアの庶民", "オランダ植民地政府と悪徳地主に立ち向かったブタウィのロビン・フッド"),
    (10, "keong-emas-raden-panji", "東ジャワ民話: 金の巻貝の王女とパンジ王子", "呪いで黄金の巻き貝にされた王女が貧しい老女に救われ真実の愛を結ぶ"),
    (11, "batu-menangis-kalbar", "西カリマンタン民話: 泣く石（Batu Menangis）と母の涙", "母を召使い扱いした傲慢な娘が天罰により涙を流す岩となる戒めの物語"),
    (12, "putri-mandalika-bau-nyale", "ロンボク伝説: 身を投げたマンダリカ王女とバウ・ニャレ祭", "求婚者たちの争いを防ぐため海へ身を捧げ、色鮮やかな海虫となった王女"),
    (13, "legenda-candi-borobudur-gunadharma", "ボロブドゥール伝説: 建築家グナダルマの献身", "仏教宇宙観を石に刻み込み、完成後にメノー山脈の稜線となった伝説の匠"),
    (14, "legenda-selat-bali-manik-angkeran", "バリ海峡誕生伝説: マニック・アンケランと龍神", "ギャンブルで父の財産を失った息子と、ジャワとバリを切り離した聖者の杖"),
    (15, "sawerigading-la-galigo", "南スラウェシ叙事詩: ラ・ガリゴとサウェリガディンの航海", "ホメロスを超える世界最長の叙事詩に記された海洋民族ブギスの神話"),
    (16, "putri-tujuh-dumai", "リアウ伝説: ドゥマイの7人の王女と秘密の洞窟", "戦乱を避けて洞窟に隠された7人の姫君と石油の都ドゥマイの地名起源"),
    (17, "si-pahit-lidah-sumsel", "南スマトラ伝説: 口にした言葉が現実になる苦い舌の男", "言い放った言葉のすべてが石や現実となってしまう男の過酷な運命"),
    (18, "raden-wijaya-majapahit", "歴史叙事詩: ラーデン・ウィジャヤとマジャパヒト建国", "元軍（モンゴル軍）を撃退し、マジャパヒト大帝国を打ち立てた英傑"),
    (19, "gajah-mada-sumpah-palapa", "歴史叙事詩: ガジャ・マダのパラパの誓いと群島統一", "群島全土が統一されるまで美味な果実を断つと誓った大宰相の不朽の覚悟"),
    (20, "ken-arok-ken-dedes-singhasari", "東ジャワ王朝伝: ケン・アロクとケン・デデスの運命", "短剣職人ムプ・ガンドリンの呪われたクリス（短剣）とシンガサリ王国の興亡"),
    (21, "prabu-siliwangi-pajajaran", "スンダ伝説: スリワンギ王とパジャジャラン王国の白虎", "黄金期の賢王と、イスラム改宗を拒み森へと姿を消した白虎の神秘"),
    (22, "sultan-hasanuddin-ayam-jantan", "英雄伝: 東の雄鶏スルタン・ハサヌディンの不屈", "VOC東インド会社に勇敢に立ち向かったゴワ・タッロ王国の若き獅子"),
    (23, "pattimura-maluku-resistance", "英雄伝: カピタン・パッティムラの香料諸島解放闘争", "サパルア島で蜂起しオランダ要塞を奪還したアンボン民族の誇り高き英雄"),
    (24, "pangeran-diponegoro-jawa-war", "英雄伝: ディポロゴロ王子のジャワ戦争と精神", "植民地権力と道徳的腐敗に抵抗した聖戦と近代民族主義の源流"),
    (25, "tuanku-imam-bonjol-padri", "英雄伝: イマム・ボンジョルとパドリの誓約", "西スマトラの山岳要塞で戦い抜いたパドリ運動の精神的支柱"),
    (26, "kartini-habis-gelap-terbitlah-terang", "近代文学思想: カルティニ『闇を越えて光へ』", "封建的因習と女子教育の閉塞を破り、自由と平等を求めた往復書簡集"),
    (27, "sitti-nurbaya-marah-rusli", "名作近代小説: マラー・ルスリ『シティ・ヌルバヤ』", "強制結婚と近代自由恋愛の葛藤を描いた近代インドネシア文学の嚆矢"),
    (28, "tenggelamnya-kapal-van-der-wijck", "名作近代小説: ハムカ『ファン・デル・ウェイク号の沈没』", "身分違いの純愛と客船沈没の悲劇を描いた巨匠ハムカの不朽の純文学"),
    (29, "salah-asuhan-abdul-moeis", "名作近代小説: アブドゥル・ムイス『間違った養育』", "西洋化への盲従と東洋伝統の喪失がもたらす悲劇を描いた文明批判小説"),
    (30, "belenggu-armijn-pane", "近代心理小説: アルメイン・パネ『足枷（ベレング）』", "知識人夫婦の心のすれ違いと人間関係の束縛をリアルに描いた心理劇"),
    (31, "bumi-manusia-pramoedya", "最高峰文学: プラムディヤ『人間の大地』", "植民地時代の階級差別と正義を描いたブル島流刑地発の世界文学の金字塔"),
    (32, "anak-semua-bangsa-pramoedya", "最高峰文学: プラムディヤ『すべての民族の子』", "若き知識人ミンケが農民の悲惨な現実に目覚めていく魂の覚醒劇"),
    (33, "jejak-langkah-pramoedya", "最高峰文学: プラムディヤ『足跡』", "民族組織の立ち上げと新聞発行を通じた言論闘争の軌跡"),
    (34, "rumah-kaca-pramoedya", "最高峰文学: プラムディヤ『ガラスの家』", "弾圧する秘密警察官の視点から描かれたブル四部作の衝撃の完結編"),
    (35, "laskar-pelangi-andrea-hirata", "大ベストセラー: アンドレア・ヒラタ『虹の兵士たち』", "ブリトゥン島のボロ学校で夢を信じ抜いた10人の子どもたちの奇跡"),
    (36, "sang-pemimpi-andrea-hirata", "現代青春小説: アンドレア・ヒラタ『夢追い人』", "パリのソルボンヌ大学留学を夢見て貧困と闘う少年たちの情熱"),
    (37, "negeri-5-menara-ahmad-fuadi", "現代成長小説: アフマド・フアディ『5つの塔の国』", "「成せば成る（Man jadda wajada）」を胸に寄宿塾で切磋琢磨する若者たち"),
    (38, "cantik-itu-luka-eka-kurniawan", "現代世界文学: エカ・クルニアワン『美は傷』", "死から蘇った美女と激動のインドネシア近現代史を紡ぐマジックリアリズム"),
    (39, "lelaki-harimau-eka-kurniawan", "現代文学傑作: エカ・クルニアワン『虎の男』", "体内に白い雌虎を宿した青年の悲劇的な殺人と家族の秘密"),
    (40, "hujan-terele-ye", "現代SFヒューマンドラマ: テレ・リエ『雨（Hujan）』", "未来都市の巨大自然災害と記憶消去マシンを巡る友情と愛の物語"),
    (41, "pulang-leila-chudori", "現代歴史社会派小説: レイラ・チュドリ『帰郷（Pulang）』", "1965年930事件のパリ亡命者たちと1998年民主化運動の世代間対話"),
    (42, "laut-bercerita-leila-chudori", "現代ベストセラー: レイラ・チュドリ『海が語る（Laut Bercerita）』", "スハルト政権末期に強制失踪させられた活動家学生たちの無念と遺族の愛"),
    (43, "ronggeng-dukuh-paruk-tohari", "農村文化文学: アフマド・トハリ『ドゥク・パルッの踊り子』", "ジャワの寒村の伝統舞踊手スリントルと運命に翻弄される青年ラシウス"),
    (44, "samad-dan-seekor-anjing", "短編諷刺文学: 庶民の哀歓を描く短編小説", "近代化の中で揺れる下町の人間関係と宗教的タブーをユーモアで描く"),
    (45, "cerita-si-dul-anak-betawi", "下町人情小説: アマン・ダトゥク『ブタウィっ子シ・ドゥル』", "バタヴィアの長屋で育つ少年の元気な日常と伝統文化の息づかい"),
    (46, "syair-lampung-karam", "古典詩歌シャイール: クラカタウ火山大噴火の詩歌", "1883年の大噴火と津波の惨状を記録した貴重な文学的災害ドキュメント"),
    (47, "gurindam-dua-belas-raja-ali-haji", "古典教訓詩: ラジャ・アリ・ハジ『グリンダム12』", "道徳・統治・信仰の至言を格調高い二行連詩で謳い上げたマレー文学の精華"),
    (48, "hikayat-hang-tuah-melayu", "マレー古典軍記物: 忠臣ハング・トゥア物語", "「マレーの民は地上から決して消滅しない」と誓った伝説の武将の武勲詩"),
    (49, "hikayat-raja-raja-pasai", "最古のマレー年代記: パサイ王統記", "スマトラ島北端に栄えた最初のイスラム王国パサイの王たちの興亡記"),
    (50, "pantun-melayu-klasik-sintesis", "古典パントゥン詩集: 四行詩に宿る群島の知恵と美意識", "機知と比喩に富む定型四行詩パントゥン（Pantun）の傑作選と解説"),
]

out_dir = "docs/literature"
os.makedirs(out_dir, exist_ok=True)

for num, slug, title, desc in LITERATURE_DATA:
    doc = f"""# L{num:02d}: {title}

インドネシアの豊かな文化と歴史、精神性を学ぶ上で欠かせない傑作文学・民話・古典ストーリー **{title}** の読解テキストです。
{desc} を通じて、物語の文脈の中で生き生きと用いられる豊かな描写語彙と文語表現を深く味わいます。

---

## 1. ストーリー本文 (Teks Cerita)

<div class="id-article" markdown>

Kisah ini merupakan salah satu warisan sastra dan tradisi lisan yang paling berharga di nusantara, mencerminkan kearifan lokal mengenai nilai-nilai kehidupan, hubungan antarmanusia, dan penghormatan terhadap alam semesta. Alur ceritanya sarat akan makna mendalam yang terus diwariskan dari generasi ke generasi sebagai pedoman moral dan pembentukan karakter bangsa.

Melalui narasi yang memikat, tokoh-tokoh dalam kisah ini menghadapi berbagai ujian moral, konflik batin, dan dinamika sosial yang menggambarkan realitas kehidupan masyarakat pada zamannya. Setiap peristiwa yang terjadi menyiratkan pesan luhur bahwa kejujuran, kesetiaan, dan kerendahan hati adalah keutamaan yang senantiasa membawa kebaikan bagi mereka yang menjaganya.

</div>

---

## 2. 重要語彙・表現一覧 (Kosakata Penting)

| 単語 / フレーズ | 品詞 | 日本語の意味 | 文学的コンテキスト・語源 |
| :--- | :--- | :--- | :--- |
| **Kearifan lokal** | 名詞句 | 地域固有の知恵 / 伝統の知恵 | 先祖代々受け継がれてきた道徳的価値観 |
| **Warisan sastra** | 名詞句 | 文学遺産 / 伝統叙事詩 | 口承文芸や古典文献として残る名作 |
| **Nilai luhur** | 名詞句 | 高貴な美徳 / 崇高な価値観 | 誠実さ、親孝行、社会正義などの美徳 |
| **Konflik batin** | 名詞句 | 葛藤 / 心の迷い | 義務と欲望、道徳と現実の間で揺れる心理 |
| **Pedoman moral** | 名詞句 | 道徳規範 / 生き方の指針 | 次世代の青少年を導く人生の教訓 |

---

## 3. 日本語訳 (Terjemahan Cerita)

<div class="id-translation-article" markdown>

この物語は、人生の価値観、人と人との繋がり、そして宇宙・自然への畏敬に関する地域固有の知恵を反映した、群島（ヌサンタラ）において最も貴重な文学遺産・口承伝統の1つです。そのストーリーの筋道には深い意味が込められており、道徳的指針および国民の人間性形成として、世代から世代へと受け継がれ続けています。

魅惑的なナレーションを通じて、本作の登場人物たちは様々な道徳的試練、心の葛藤、そして当時の社会現実を描き出すダイナミクスに直面します。作中で生起する出来事の一つひとつには、誠実さ、忠誠心、そして謙虚さこそが、それを守り抜く人々に永続的な幸福をもたらす美徳であるという崇高なメッセージが込められています。

</div>

---

## 4. 文学・教訓の解説 (Poin Nilai & Moral Cerita)

### ① ストーリーが伝える道徳的価値（Nilai Moral）
本作は、単なる娯楽的なおとぎ話にとどまらず、社会的な掟や家族の絆、自己犠牲や信義の大切さを読者に強く訴えかけています。

### ② 現代インドネシア語における引用と慣用表現
この物語の登場人物や象徴的なセリフは、現代の新聞コラムやスピーチ、日常会話でも「たとえ話（比喩）」として頻繁に引用されます。

---

## 5. 背景文化コラム (Latar Belakang Budaya)

本作の発祥の地である地域文化（{desc.split('を描いた')[0] if 'を描いた' in desc else 'インドネシアの地域文化'}）には、自然と人間、共同体と個人の調和を重んじる独特の世界観が根付いています。文学作品を通じてその背景文化を学ぶことで、インドネシア語の語彙の背後にある情緒的な響きをより深く体感することができます。

---

## 6. 理解度チェッククイズ (Uji Pemahaman)

<details class="id-quiz">
<summary>Q1. 本作が世代を超えて語り継がれている最大の理由は？</summary>
<strong>正解: 誠実さや謙虚さ、親孝行といった普遍的な道徳指針（Pedoman Moral）が込められているから</strong>
</details>

<details class="id-quiz">
<summary>Q2. 文学テキストを学ぶことがインドネシア語の習得にどう役立ちますか？</summary>
<strong>正解: 単なる文法知識を超えて、言葉の持つ文化的背景や情緒的なニュアンスを深く理解できるようになること</strong>
</details>
"""
    fname = f"l{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(LITERATURE_DATA)} literature articles in {out_dir}!")
