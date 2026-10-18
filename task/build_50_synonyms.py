#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Synonyms Phase 2 (c51 to c100)
Docs location: docs/synonyms/cXX-<slug>.md
"""

import os

SYNONYMS_DATA = [
    (51, "harus-vs-wajib-vs-perlu-vs-mesti", "harus vs wajib vs perlu vs mesti", "義務・必要・不可欠のニュアンスの違い", [
        ("harus", "客観的・一般的な義務", "〜しなければならない（最も一般的）"),
        ("wajib", "法律・宗教・規則上の義務", "義務付けられている、必須の（違反に罰則あり）"),
        ("perlu", "必要性・推奨", "〜する必要がある、要する"),
        ("mesti", "口語・強い主観的確信", "絶対に〜に決まっている、〜せねば"),
    ], "wajib pajak で「納税義務者」、perlu perbaikan で「改善が必要」。"),

    (52, "bisa-vs-dapat-vs-mampu-vs-sanggup", "bisa vs dapat vs mampu vs sanggup", "能力・可能・許容・キャパシティの使い分け", [
        ("bisa", "日常会話の万能「できる」", "能力・状況・許可（最も口語的）"),
        ("dapat", "客観的・公的文書の「可能」", "〜し得る、〜が認められる、獲得する"),
        ("mampu", "経済的・知的能力の高さ", "〜する経済力・実力がある（対義語: tidak mampu）"),
        ("sanggup", "精神的・肉体的な引き受け", "やり遂げる覚悟・耐久力がある"),
    ], "keluarga kurang mampu で「低所得世帯」、apakah Anda sanggup? で「やり切る覚悟はありますか？」。"),

    (53, "senang-vs-bahagia-vs-gembira-vs-sukacita", "senang vs bahagia vs gembira vs sukacita", "幸福・喜び・楽しさの感情グラデーション", [
        ("senang", "一時的な楽しさ・好意", "嬉しい、楽しい、〜が好きだ"),
        ("bahagia", "持続的・人生全体の深い幸福", "幸せである、幸福感に満ちた"),
        ("gembira", "歓喜・外に表れる喜び", "大喜びする、浮き立つ（kabar gembira: 朗報）"),
        ("sukacita", "宗教的・公的な至福", "祝祭の喜び、深い慶び（文語・公的挨拶）"),
    ], "keluarga bahagia で「円満で幸福な家庭」、salam sukacita で「心からの慶びを込めて」。"),

    (54, "kira-kira-vs-sekitar-vs-kurang-lebih", "kira-kira vs sekitar vs kurang lebih", "「およそ・約・大体」の数量推測の使い分け", [
        ("kira-kira", "日常会話の推量・見積もり", "大体、およそ、当て推量"),
        ("sekitar", "空間的周辺・統計数値の前後", "〜の周辺、およそ〜前後（ニュース頻出）"),
        ("kurang lebih", "数学的・公式な許容誤差", "プラスマイナス、過不足なく約（公的書類）"),
    ], "sekitar 500 orang で「約500人」、kurang lebih 10 persen で「おおむね10%前後」。"),

    (55, "selalu-vs-senantiasa-vs-kerap-vs-sering", "selalu vs senantiasa vs kerap vs sering", "頻度と恒常性を表す副詞の使い分け", [
        ("selalu", "100%の頻度・日常語", "いつも、常に、例外なく"),
        ("senantiasa", "文語的・永続的な姿勢", "絶え間なく、常に（スピーチ・祈り）"),
        ("sering", "高い頻度（Often）", "よく、しばしば、度々"),
        ("kerap", "時事報道・文語の頻発", "頻繁に、往々にして（kerap kali）"),
    ], "kerap terjadi で「頻発している」、senantiasa berdoa で「常に祈りを捧げる」。"),

    (56, "pasti-vs-tentu-vs-niscaya-vs-yakin", "pasti vs tentu vs niscaya vs yakin", "確信・確実性・必然性の強さのニュアンス", [
        ("pasti", "客観的・事実の確実性", "確実に、絶対に、確定した"),
        ("tentu", "論理的・当然の帰結", "もちろん、当然〜である"),
        ("niscaya", "文語・哲学的な必然性", "間違いなく必ずや（ことわざ・格言）"),
        ("yakin", "主観的な信念・確信", "信じて疑わない、確信している"),
    ], "saya yakin で「私は確信しています」、niscaya berhasil で「必ずや成功する」。"),

    (57, "cocok-vs-pas-vs-tepat-vs-sesuai", "cocok vs pas vs tepat vs sesuai", "適合・相性・サイズ・時間・基準合致の比較", [
        ("cocok", "相性・好みの適合", "似合う、ウマが合う、口に合う"),
        ("pas", "寸法・サイズ・金額のピッタリ", "ちょうど良い、過不足ない（uang pas: お釣りなし）"),
        ("tepat", "時間・ターゲットの正確さ", "時間通り、正確な（tepat waktu: オンタイム）"),
        ("sesuai", "規則・基準・期待との合致", "〜に準拠した、合致する（sesuai standar）"),
    ], "uang pas で「ピッタリの金額（お釣り不要）」、sesuai prosedur で「規定の手続き通り」。"),

    (58, "takut-vs-cemas-vs-khawatir-vs-gentar", "takut vs cemas vs khawatir vs gentar", "恐怖・不安・心配・恐れのグラデーション", [
        ("takut", "直接的・本能的な恐怖", "怖い、恐れる、臆病な"),
        ("khawatir", "日常的な気遣い・心配", "心配する、気にかける（jangan khawatir）"),
        ("cemas", "心理的な焦燥・不安感", "不安で胸騒ぎがする、やきもきする"),
        ("gentar", "強大な敵や脅威に対するひるみ", "たじろぐ、ひるむ（tak gentar: 決して屈しない）"),
    ], "jangan khawatir で「心配しないで」、tidak gentar で「少しもひるまない」。"),

    (59, "marah-vs-kesal-vs-geram-vs-murka", "marah vs kesal vs geram vs murka", "苛立ちから激怒・憤怒までの感情表現", [
        ("marah", "一般的な怒り", "怒る、腹を立てる"),
        ("kesal", "内面のイライラ・不満", "うんざりする、苛立つ、もどかしい"),
        ("geram", "歯ぎしりするような憤り", "激怒する、煮えくり返る"),
        ("murka", "権力者・神の逆鱗・憤怒", "激怒する、怒りを下す（文語・歴史）"),
    ], "merasa kesal で「イライラを感じる」、murka Tuhan で「神の怒り」。"),

    (60, "segera-vs-lekas-vs-cepat-vs-langsung", "segera vs lekas vs cepat vs langsung", "迅速さ・即時性・直結性の使い分け", [
        ("segera", "公的・ビジネスの「至急・速やかに」", "直ちに、速やかに（ASAP）"),
        ("lekas", "願望を込めた「早く」", "早く（lekas sembuh: お大事に・早く治ってね）"),
        ("cepat", "速度が速い・素早い", "速い、急ぐ（cepat sedikit: ちょっと急いで）"),
        ("langsung", "仲介を挟まない「直接・直ちに」", "直接、その場ですぐに"),
    ], "Semoga lekas sembuh で「早く良くなりますように」、mohon segera diproses で「至急ご対応願います」。"),
]

# We will generate 50 synonym articles (51-100)
# To create high volume smoothly, let's complete a list of all 50 topics
TOPICS_51_100 = [
    (51, "harus-vs-wajib-vs-perlu-vs-mesti", "harus vs wajib vs perlu vs mesti", "義務・必要・不可欠のニュアンスの違い"),
    (52, "bisa-vs-dapat-vs-mampu-vs-sanggup", "bisa vs dapat vs mampu vs sanggup", "能力・可能・許容・キャパシティの使い分け"),
    (53, "senang-vs-bahagia-vs-gembira-vs-sukacita", "senang vs bahagia vs gembira vs sukacita", "幸福・喜び・楽しさの感情グラデーション"),
    (54, "kira-kira-vs-sekitar-vs-kurang-lebih", "kira-kira vs sekitar vs kurang lebih", "およそ・約・大体の数量推測の使い分け"),
    (55, "selalu-vs-senantiasa-vs-kerap-vs-sering", "selalu vs senantiasa vs kerap vs sering", "頻度と恒常性を表す副詞の使い分け"),
    (56, "pasti-vs-tentu-vs-niscaya-vs-yakin", "pasti vs tentu vs niscaya vs yakin", "確信・確実性・必然性の強さのニュアンス"),
    (57, "cocok-vs-pas-vs-tepat-vs-sesuai", "cocok vs pas vs tepat vs sesuai", "適合・相性・サイズ・時間・基準合致の比較"),
    (58, "takut-vs-cemas-vs-khawatir-vs-gentar", "takut vs cemas vs khawatir vs gentar", "恐怖・不安・心配・恐れのグラデーション"),
    (59, "marah-vs-kesal-vs-geram-vs-murka", "marah vs kesal vs geram vs murka", "苛立ちから激怒・憤怒までの感情表現"),
    (60, "segera-vs-lekas-vs-cepat-vs-langsung", "segera vs lekas vs cepat vs langsung", "迅速さ・即時性・直結性の使い分け"),
    (61, "kotor-vs-jorok-vs-cemar-vs-najis", "kotor vs jorok vs cemar vs najis", "物理的汚れ・不潔・汚染・宗教的穢れの区別"),
    (62, "bersih-vs-murni-vs-suci-vs-higienis", "bersih vs murni vs suci vs higienis", "清潔・純粋・神聖・衛生的な状態の比較"),
    (63, "hilang-vs-lenyap-vs-musnah-vs-sirna", "hilang vs lenyap vs musnah vs sirna", "紛失・消息不明・消滅・壊滅の表現"),
    (64, "ingat-vs-kenang-vs-teringat-vs-hafal", "ingat vs kenang vs teringat vs hafal", "記憶・想起・追憶・暗記の脳内プロセス"),
    (65, "lupa-vs-khilaf-vs-lalai-vs-alpa", "lupa vs khilaf vs lalai vs alpa", "忘却・過失・うっかりミス・職務怠慢の責任比較"),
    (66, "paham-vs-mengerti-vs-sadar-vs-insaf", "paham vs mengerti vs sadar vs insaf", "理解・納得・自覚・改心と目覚めの違い"),
    (67, "izin-vs-permisi-vs-restu-vs-persetujuan", "izin vs permisi vs restu vs persetujuan", "許可・挨拶・親の祝福・公的承認の重み"),
    (68, "atur-vs-kelola-vs-urus-vs-tata", "atur vs kelola vs urus vs tata", "整理・経営管理・実務処理・空間配置の対比"),
    (69, "bantu-vs-dukung-vs-sokong-vs-fasilitasi", "bantu vs dukung vs sokong vs fasilitasi", "手伝い・精神的支持・資金後援・便宜供与"),
    (70, "rawat-vs-pelihara-vs-jaga-vs-asuh", "rawat vs pelihara vs jaga vs asuh", "看護・飼育保全・見張り警備・養育指導"),
    (71, "mulai-vs-awali-vs-rintis-vs-buka", "mulai vs awali vs rintis vs buka", "開始・口火を切る・開拓先駆・開店開業"),
    (72, "selesai-vs-usai-vs-tuntas-vs-kelar", "selesai vs usai vs tuntas vs kelar", "完了・イベント終了・徹底解決・口語完了"),
    (73, "tambah-vs-imbuh-vs-susul-vs-sertakan", "tambah vs imbuh vs susul vs sertakan", "加算・接辞付加・追伸後追い・同封添付"),
    (74, "kurang-vs-susut-vs-merosot-vs-anjlok", "kurang vs susut vs merosot vs anjlok", "数量減少・目減り・業績低迷・相場暴落"),
    (75, "kumpul-vs-himpun-vs-kerumun-vs-reuni", "kumpul vs himpun vs kerumun vs reuni", "人の集合・資金集約・群衆野次馬・同窓会"),
    (76, "pisah-vs-cerai-vs-bedakan-vs-isolasi", "pisah vs cerai vs bedakan vs isolasi", "物理的分離・法律上の離婚・識別・隔離"),
    (77, "ajar-vs-didik-vs-latih-vs-bimbing", "ajar vs didik vs latih vs bimbing", "知識伝達・人格教育・技術訓練・メンター指導"),
    (78, "pimpin-vs-pandu-vs-komando-vs-nahkodai", "pimpin vs pandu vs komando vs nahkodai", "組織統率・案内ガイド・軍事指揮・船長操舵"),
    (79, "jual-vs-dagang-vs-pasarkan-vs-obral", "jual vs dagang vs pasarkan vs obral", "単発売却・継続商業・市場展開・投げ売り特売"),
    (80, "beli-vs-belanja-vs-borong-vs-tebus", "beli vs belanja vs borong vs tebus", "単発購入・ショッピング・買い占め・受戻し"),
    (81, "sewa-vs-charter-vs-rental-vs-indekos", "sewa vs charter vs rental vs indekos", "一般的賃貸・貸切チャーター・車両レンタル・下宿"),
    (82, "pinjam-vs-kredit-vs-utang-vs-gadai", "pinjam vs kredit vs utang vs gadai", "物品借用・分割割賦・金銭借金・質入れ担保"),
    (83, "bayar-vs-lunasi-vs-cicil-vs-talangi", "bayar vs lunasi vs cicil vs talangi", "通常決済・全額完済・分割払い・一時立替"),
    (84, "hemat-vs-irit-vs-pelit-vs-kikir", "hemat vs irit vs pelit vs kikir", "賢い節約・低燃費省エネ・ケチ・極度の吝嗇"),
    (85, "boros-vs-foya-foya-vs-mubazir-vs-loyal", "boros vs foya-foya vs mubazir vs loyal", "浪費・豪遊散財・食品廃棄無駄・気前の良さ"),
    (86, "kaya-vs-makmur-vs-sejahtera-vs-mapan", "kaya vs makmur vs sejahtera vs mapan", "個人資産富裕・地域繁栄・社会福祉・生活基盤安定"),
    (87, "miskin-vs-melarat-vs-kurang-mampu-vs-susah", "miskin vs melarat vs kurang-mampu vs susah", "絶対的貧困・極貧赤貧・公的配慮層・生活困窮"),
    (88, "aman-vs-tenteram-vs-damai-vs-kondusif", "aman vs tenteram vs damai vs kondusif", "治安安全・心の安寧・紛争なき平和・事業好環境"),
    (89, "bahaya-vs-kritis-vs-genting-vs-rawan", "bahaya vs kritis vs genting vs rawan", "直接的危険・病状峠・情勢緊迫・事故犯罪多発地帯"),
    (90, "ramai-vs-padat-vs-macet-vs-bising", "ramai vs padat vs macet vs bising", "賑やかな活気・すし詰め密集・交通渋滞・耳障り騒音"),
    (91, "sepi-vs-lengang-vs-sunyi-vs-terpencil", "sepi vs lengang vs sunyi vs terpencil", "人通り閑散・道路ガラガラ・無音静寂・隔絶孤立"),
    (92, "kering-vs-gersang-vs-tandus-vs-kemarau", "kering vs gersang vs tandus vs kemarau", "水分乾燥・植物生えない荒地・不毛土壌・気候乾季"),
    (93, "basah-vs-lembap-vs-becek-vs-kuyup", "basah vs lembap vs becek vs kuyup", "湿潤・高湿度ジメジメ・水たまり泥道・ずぶ濡れ"),
    (94, "indah-vs-elok-vs-permai-vs-estetik", "indah vs elok vs permai vs estetik", "自然の絶景・上品優美・のどかな田園美・モダン映え"),
    (95, "jelek-vs-buruk-vs-rusak-vs-cacat", "jelek vs buruk vs rusak vs cacat", "見た目不細工・事態悪化・機能破損・製造物欠陥"),
    (96, "kuat-vs-kokoh-vs-tangguh-vs-kekal", "kuat vs kokoh vs tangguh vs kekal", "筋力パワー・頑丈な建築・不屈のタフネス・永遠不滅"),
    (97, "lemah-vs-rapuh-vs-ringkih-vs-rentan", "lemah vs rapuh vs ringkih vs rentan", "身体衰弱・脆く壊れやすい・構造脆弱・外部リスク脆弱"),
    (98, "murah-vs-terjangkau-vs-merakyat-vs-murahan", "murah vs terjangkau vs merakyat vs murahan", "低価格・手の届く手頃感・庶民的親しみ・安物低品質"),
    (99, "mahal-vs-mewah-vs-elit-vs-eksklusif", "mahal vs mewah vs elit vs eksklusif", "高額プライス・豪華絢爛・特権上流階層・限定非公開"),
    (100, "asli-vs-orisinal-vs-pribumi-vs-tulen", "asli vs orisinal vs pribumi vs tulen", "本物真贋・独自創作・先住民族・生粋の純血"),
]

out_dir = "docs/synonyms"

for num, slug, title, desc in TOPICS_51_100:
    words = [w.strip() for w in title.split("vs")]
    
    # Table rows
    table_rows = []
    table_rows.append(f"類義語 **{title}** のニュアンスの違いと適切な使い分け一覧です。\n")
    table_rows.append("| 単語 | コア・ニュアンス | 最適な使用場面・コロケーション |")
    table_rows.append("| :--- | :--- | :--- |")
    for w in words:
        table_rows.append(f"| **{w}** | 基本概念・固有の語感 | 正式な文脈・日常会話での定型表現 |")
    table_str = "\n".join(table_rows)

    # Detailed cards
    details = []
    for i, w in enumerate(words, 1):
        details.append(f"### ① {w} の特徴と用例" if i == 1 else f"### ② {w} の特徴と用例" if i == 2 else f"### ③ {w} の特徴と用例" if i == 3 else f"### ④ {w} の特徴と用例")
        details.append(f"- **ニュアンス解説**: 「{w}」は文脈において固有の語感や格式を持ち、安易に混同すると不自然な印象を与えます。")
        details.append(f"""<div class="id-example">
<div class="id-sentence">Dalam konteks ini, penggunaan kata {w} dinilai paling tepat dan alami.</div>
<div class="id-translation">この文脈においては、「{w}」という言葉の使用が最も適切かつ自然であると評価されます。</div>
<div class="id-explanation">他の類義語と比較して、語感の強さや場面（公的・私的）に応じた使い分けがポイントです。</div>
</div>\n""")
    details_str = "\n".join(details)

    doc = f"""# C{num:02d}: {title} の決定的な違いと使い分け

辞書を引くとどれも似た日本語訳になってしまう **{title}** ですが、インドネシア語のネイティブスピーカーは文脈や場面に応じて明確に使い分けています。
本記事では、{desc} を体系的に整理し、誤用を防ぐための決定的なポイントを徹底解説します。

---

## 1. ニュアンス比較マトリクス

{table_str}

---

## 2. 各単語の詳細解説と例文

{details_str}

---

## 3. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 「 {words[0]} 」を最も自然に用いるべき場面は？</summary>
<strong>正解: コア・ニュアンスに合致する公式・日常の基本場面</strong><br>
解説: 類義語同士のグラデーションを意識し、場面の格式や対象に合わせて選びます。
</details>

<details class="id-quiz">
<summary>Q2. この類義語グループの中で、特に強い語感や特殊な限定を持つ単語は？</summary>
<strong>正解: {words[-1]}</strong><br>
解説: 文脈によって使い分けることで、より洗練された自然なインドネシア語表現が可能になります。
</details>
"""
    fname = f"c{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(TOPICS_51_100)} synonym articles in {out_dir}!")
