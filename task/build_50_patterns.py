#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Patterns Phase 2 (p51 to p100)
Docs location: docs/patterns/pXX-<slug>.md
"""

import os

PATTERNS_DATA = [
    (51, "bagaimana-kalau-suggestions", "提案構文: Bagaimana kalau...", "〜してみてはどうですか？ / 〜したらどう？"),
    (52, "sebaiknya-recommendations", "推奨構文: Sebaiknya...", "〜した方が良いです / 〜するのが賢明です"),
    (53, "ada-baiknya-jika-advice", "助言構文: Ada baiknya jika...", "〜しておいた方が無難です / 〜するのも一案です"),
    (54, "walaupun-begitu-concession", "譲歩構文: Walaupun begitu...", "そうは言っても / それにもかかわらず"),
    (55, "biar-bagaimanapun-resolution", "覚悟構文: Biar bagaimanapun...", "いずれにしても / どんな場合でも"),
    (56, "gara-gara-negative-cause", "原因構文: Gara-gara...", "〜のせいで / 〜が原因で（悪い結果）"),
    (57, "berkat-positive-cause", "恩恵構文: Berkat...", "〜のおかげで / 〜の恩恵により（良い結果）"),
    (58, "akibat-dari-consequence", "因果構文: Akibat dari...", "〜の結果として / 〜の影響に伴い"),
    (59, "daripada-preference", "選好構文: Daripada... lebih baik...", "〜するくらいなら…した方がマシだ"),
    (60, "alih-alih-instead-of", "対照構文: Alih-alih...", "〜する代わりにむしろ… / 〜どころか"),
    (61, "rupanya-discovery", "発見構文: Rupanya...", "どうやら〜らしい / 見てみれば実は…"),
    (62, "tampaknya-speculation", "推測構文: Tampaknya...", "〜のように見える / 〜のようだ"),
    (63, "bisa-jadi-possibility", "可能構文: Bisa jadi...", "〜ということもあり得る / ひょっとすると…"),
    (64, "katanya-hearsay", "伝聞構文: Katanya...", "〜という話だ / 〜らしいよ"),
    (65, "menurut-kabar-news-hearsay", "報道構文: Menurut kabar...", "ニュースの報じるところによると"),
    (66, "konon-legend-rumor", "古伝構文: Konon...", "言い伝えによれば / 昔から〜と伝えられる"),
    (67, "mumpung-taking-opportunity", "好機構文: Mumpung...", "せっかく〜の機会だから / 今のうちに"),
    (68, "kebetulan-coincidence", "偶然構文: Kebetulan...", "ちょうど偶然にも / たまたま〜だった"),
    (69, "pantas-saja-comprehension", "納得構文: Pantas saja...", "どおりで〜なわけだ！ / 納得がいった"),
    (70, "wajar-kalau-natural-result", "当然構文: Wajar kalau...", "〜なのももっともだ / 当然のことだ"),
    (71, "jangan-sampai-prevention", "予防構文: Jangan sampai...", "決して〜にならないように / 〜しては困る"),
    (72, "untung-saja-relief", "安堵構文: Untung saja...", "幸いにも〜で済んだ / 助かったことに"),
    (73, "nyaris-near-miss", "危機回避構文: Nyaris...", "もう少しで〜するところだった（ヒヤリハット）"),
    (74, "sayang-sekali-regret", "遺憾構文: Sayang sekali...", "誠に残念ながら / もったいないことに"),
    (75, "bukan-main-admiration", "感嘆構文: Bukan main...", "とんでもなく〜だ / 並大抵ではない"),
    (76, "makin-lama-makin-progressive", "漸増構文: Makin lama makin...", "時間が経つにつれてますます…"),
    (77, "sedikit-demi-sedikit-stepwise", "着実構文: Sedikit demi sedikit...", "一歩一歩少しずつ / 着実に"),
    (78, "mau-tidak-mau-inevitability", "不可避構文: Mau tidak mau...", "好むと好まざるとにかかわらず / 必然的に"),
    (79, "bukan-karena-melainkan-contrast", "対比構文: Bukan karena... melainkan...", "〜だからではなく、むしろ…だからだ"),
    (80, "seperti-halnya-analogy", "比喩構文: Seperti halnya...", "あたかも〜であるのと同様に"),
    (81, "jangankan-apatah-lagi-extreme", "極端例示構文: Jangankan... apatah lagi...", "〜はおろか…でさえも"),
    (82, "sedemikian-rupa-sehingga-manner", "様態構文: Sedemikian rupa sehingga...", "〜なようなやり方で…になるよう"),
    (83, "atas-dasar-legal-ground", "根拠構文: Atas dasar...", "〜の原則・根拠に基づいて"),
    (84, "dalam-rangka-purpose-framework", "枠組構文: Dalam rangka...", "〜の一環として / 〜を目的として"),
    (85, "sehubungan-dengan-formal-reference", "公的言及構文: Sehubungan dengan...", "〜に関連して / 〜につき（公式書簡）"),
    (86, "mengingat-bahwa-considering", "熟慮構文: Mengingat bahwa...", "〜という事実を鑑みると / 〜を考慮し"),
    (87, "menimbang-bahwa-decree", "決定構文: Menimbang bahwa...", "〜という点を考慮した結果（Menimbang）"),
    (88, "sepanjang-yang-saya-tahu-knowledge", "見聞構文: Sepanjang yang saya tahu...", "私の知る限りにおいては"),
    (89, "sejauh-ini-up-to-now", "進捗構文: Sejauh ini...", "これまでのところは / 現在の段階では"),
    (90, "pada-dasarnya-fundamentally", "本質構文: Pada dasarnya...", "基本的には / 根本的な部分では"),
    (91, "dengan-kata-lain-rephrasing", "換言構文: Dengan kata lain...", "換言すれば / 別の言い方をすれば"),
    (92, "terlepas-dari-regardless", "分離構文: Terlepas dari...", "〜はさておき / 〜に関わらず"),
    (93, "di-satu-sisi-di-sisi-lain-two-sides", "両面構文: Di satu sisi..., di sisi lain...", "一方で…、しかし他方では…"),
    (94, "oleh-karena-itu-logical-conclusion", "帰結構文: Oleh karena itu...", "したがって / それゆえに"),
    (95, "dengan-demikian-summary-consequence", "総括構文: Dengan demikian...", "これにより / 以上のことから"),
    (96, "singkat-kata-in-short", "要約構文: Singkat kata...", "要するに / 手短に言えば"),
    (97, "pada-akhirnya-in-the-end", "着地点構文: Pada akhirnya...", "最終的には / 究極的には"),
    (98, "perlu-ditegaskan-bahwa-emphasis", "強調構文: Perlu ditegaskan bahwa...", "〜という点は強調しておく必要があります"),
    (99, "tidak-bisa-dipungkiri-undeniable", "不可抗力構文: Tidak bisa dipungkiri bahwa...", "〜であることは否定できません"),
    (100, "semoga-sukses-dan-lancar-wishes", "祝福構文: Semoga sukses dan lancar...", "ご成功と順調な進展をお祈り申し上げます"),
]

out_dir = "docs/patterns"

for num, slug, title, desc in PATTERNS_DATA:
    pat_name = title.split(":")[1].strip() if ":" in title else title
    doc = f"""# P{num:02d}: {title}

会話や文章作成において、単語を入れ替えるだけで無限に実用的な表現を生み出せる万能構文が **{pat_name}** です。
本記事では、「{desc}」というニュアンスを的確に伝える構文テンプレートと例文を徹底解説します。

---

## 1. 構文パターン構造と解説

### 基本フォーマット
```text
{pat_name} + [節 / 名詞句 / 状況]
```

- **コア機能**: {desc}
- **使用場面**: 日常会話からビジネス交渉、公的文書、メール連絡まで幅広く活用されます。
- **ポイント**: 文頭に置くことで、発言全体のトーンや話者の意図（提案、譲歩、因果、推測など）を相手に瞬時に伝えることができます。

---

## 2. 実践パターン例文集

### 例文①: 基本的な使い方
<div class="id-example">
<div class="id-sentence">{pat_name} kita mendiskusikan hal ini secara langsung dalam rapat besok pagi?</div>
<div class="id-translation">明日の朝の会議で、この件について直接話し合ってみてはいかがでしょうか？</div>
<div class="id-explanation">構文「**{pat_name}**」を用いることで、相手に角を立てずスムーズにメッセージを伝えます。</div>
</div>

### 例文②: ビジネス実務での応用
<div class="id-example">
<div class="id-sentence">{pat_name} seluruh tim tetap mematuhi SOP demi menjaga kualitas dan keselamatan kerja.</div>
<div class="id-translation">品質と安全衛生を守るため、チーム全員がSOPを遵守し続けることが求められます。</div>
<div class="id-explanation">重要事項の徹底や方針の共有において、説得力を持たせる用法です。</div>
</div>

---

## 3. 入れ替え練習ドリル

以下の空欄にご自身の状況に合った語句を当てはめて発話練習をしてみましょう。

1. **{pat_name}** [ kondisi saat ini ] ...
2. **{pat_name}** [ rencana masa depan ] ...

---

## 4. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 構文「 {pat_name} 」が果たす主なコミュニケーション上の役割は？</summary>
<strong>正解: {desc}</strong><br>
解説: 状況に応じた構文テンプレートを活用することで、自然で洗練されたインドネシア語表現が可能になります。
</details>

<details class="id-quiz">
<summary>Q2. この構文を実際の会話で効果的に使うコツは？</summary>
<strong>正解: 文頭で明瞭に発音し、その後に続く具体的な提案や事実とスムーズに繋げること</strong><br>
解説: 接続表現が明確であれば、聞き手も文脈を即座に理解できます。
</details>
"""
    fname = f"p{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(PATTERNS_DATA)} pattern articles in {out_dir}!")
