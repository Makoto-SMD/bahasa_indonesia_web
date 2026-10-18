#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generator for Exam Drills Phase 2 (u51 to u100)
Docs location: docs/exam-drills/uXX-<slug>.md
"""

import os

EXAM_DRILLS_DATA = [
    (51, "circumfix-ber-an-reciprocal-action", "相互周囲辞 ber-...-an の語根結合制約と複数主語", "相互動作（saling）を表す ber-...-an の文法規則と誤用防止"),
    (52, "circumfix-per-an-vs-pen-an-institution", "per-...-an の制度名詞化と peN-...-an の動作過程", "動作の過程（プロセス）と制度・場所・結果を表す周囲辞の対比"),
    (53, "suffix-kan-benefactive-ditransitive", "二重目的語受益構文における語順制約と代名詞転置", "S + V-kan + 人（受益者） + 物 の語順と代名詞目的語のルール"),
    (54, "suffix-i-locative-direct-object", "場所対象化 -i と前置詞削除ルールの文法的厳密性", "前置詞（di/ke/pada）を吸収して他動詞化する接尾辞 -i のメカニズム"),
    (55, "passive-type-one-inversion", "一人称・二人称受動態の助動詞・否定詞挿入位置", "Saya baca の受動態における否定詞（tidak）や助動詞（harus）の配置"),
    (56, "ter-potential-vs-involuntary", "接頭辞 ter- の可能否定（tidak ter-）と無意図受動", "「〜できない（不可能）」と「うっかり〜してしまった」の識別"),
    (57, "subordinate-clauses-faulty-subjects", "従属節の主語脱落と副詞節の主語誤認エラー", "文法正誤問題で頻出する「主節と従属節の主語の不一致」トラップ"),
    (58, "parallelism-in-complex-sentences", "複文における接辞の対称性・パラレリズム規則", "等位接続詞（dan, atau）で結ばれる動詞の接頭辞整合性"),
    (59, "eyd-fifth-edition-loanword-spelling", "EYD第5版における外来語綴りの公的規則", "英語・オランダ語借用語の正規化規則（-tion → -si, -ic → -ik）"),
    (60, "eyd-capitalization-titles-ranks", "EYD正書法における敬称・爵位・役職名の大文字表記基準", "大統領、知事、教授、国王などの肩書が大文字になる条件"),
    (61, "eyd-hyphen-compound-words", "複合語・繰り返し語におけるハイフン（-）の厳格な用法", "畳語（kata ulang）と接頭辞 se- + 大文字のハイフン接続ルール"),
    (62, "eyd-particles-pun-and-per", "助詞 pun と per の分かち書きと一語化の境界", "maupun/meskipun（一語）と saya pun（分かち書き）の完全区別"),
    (63, "inversion-structure-predicative-first", "述語前置倒置構文の強調効果と文法識別演習", "述語＋粒子 -lah ＋主語 による倒置構文（Inversi）の読解"),
    (64, "clitic-pronouns-possession-object", "後接代名詞 -ku, -mu, -nya の多機能性と曖昧性解消", "所有格、受動態の動作主、名詞化辞としての -nya の識別"),
    (65, "conjunction-pairing-bukan-melainkan", "相関接続詞 bukan... melainkan... の厳格な呼応", "名詞の否定（bukan）に対する melainkan のセット運用"),
    (66, "conjunction-pairing-baik-maupun", "相関接続詞 baik... maupun... の制約", "「〜も…も同様に」を表す並列相関構文の文法ルール"),
    (67, "conjunction-pairing-makin-makin", "相関副詞 makin... makin... の比例構文", "「〜すればするほどますます…」を表す構文的制約"),
    (68, "temporal-aspect-sudah-pernah-telah", "完了相 sudah / telah / pernah のニュアンス差異", "口語完了、公式完了、経験完了の精密な使い分け"),
    (69, "modal-auxiliary-sepatutnya-seyogianya", "文語助動詞 seyogianya / sepatutnya の当為性", "法律や社説で「〜すべきである・当然〜であるべき」を表す表現"),
    (70, "relative-clause-yang-constraints", "関係代名詞 yang の主語化制約と前置詞句との結合不可則", "yang + 前置詞句が誤りとなる理由と正しい関係代名詞節の形成"),
    (71, "appositive-clauses-identifying-core", "同格節・挿入句を見抜き文の主骨格S-Pを抽出する技術", "長大な修飾語句に惑わされず主語と述語を特定する速読術"),
    (72, "abstract-noun-formation-ke-an-boundaries", "形容詞・動詞・名詞からの ke-...-an 派生の品詞境界", "状態名詞と被害受動動詞（kehabisan 等）の判別基準"),
    (73, "verbal-noun-reduplication-actions", "動詞語根の畳語による反復・相互・漠然名詞化", "berjalan-jalan（散歩）、tarik-menarik（引き合い）の分析"),
    (74, "nominal-reduplication-plural-diversity", "名詞畳語の複数性・多様性・比喩的意味変化", "mata-mata（スパイ）、langit-langit（天井）の派生メカニズム"),
    (75, "idiomatic-compounds-kambing-hitam", "慣用複合語の読解識別と比喩表現の分析", "cuci mata（目の保養）、banting tulang（粉骨砕身）の背景"),
    (76, "legal-terminology-putusan-penetapan", "法律読解: 判決（Putusan）と決定（Penetapan）の相違", "裁判所が下す法的判断の性質と拘束力の違い"),
    (77, "official-decree-whereas-clauses-menimbang", "公的政令読解: Menimbang と Mengingat の構造", "大統領令・知事令の法制執務上の文体ルール"),
    (78, "official-mou-whereas-preamble-bahwa", "覚書MOU読解: Preamble の bahwa 連続構文", "国際契約や協定書における前提条件文の読解テクニック"),
    (79, "academic-abstract-impersonal-style", "学術論文アブストラクト読解: 非人称客観文体と受動態", "diperoleh, ditunjukkan などの受動動詞による研究報告文体"),
    (80, "editorial-argumentation-polemic-style", "高級紙社説の論理展開と論陣分析", "Kompas 紙などの論説文における主張・反論・総括の構造"),
    (81, "ukbi-listening-note-taking-lecture", "UKBI聴解演習: 講義形式の要点メモ取りテクニック", "5分間の学術講義音声から主要論点と数値を把握する技術"),
    (82, "ukbi-listening-interview-contradiction", "UKBI聴解演習: インタビュー音声からの話者の矛盾抽出", "対談者の発言から本音・含み・前提の論理的破綻を見抜く演習"),
    (83, "ukbi-listening-formal-announcement", "UKBI聴解演習: 公式案内放送の細部条件把握", "日時、対象者、例外条件などの引っかけ問題対策"),
    (84, "ukbi-reading-chart-data-synthesis", "UKBI読解演習: 統計グラフ・データの複合読解", "文章とグラフ数値を照合し、正しい相関関係を特定する演習"),
    (85, "ukbi-reading-historical-chronology", "UKBI読解演習: 歴史・年代記テキストの時系列再構成", "複数の年代や出来事が交錯する長文の論理整理"),
    (86, "ukbi-reading-scientific-taxonomy", "UKBI読解演習: 生物・自然科学の分類階層テキスト読解", "上位概念と下位概念（Genus / Species）の分類構造把握"),
    (87, "ukbi-writing-formal-correspondence", "UKBI記述演習: 公式行政書簡の頭書・定型結語フォーマット", "Nomor, Lampiran, Perihal, Dengan hormat の正式書式"),
    (88, "ukbi-writing-opinion-editorial-essay", "UKBI記述演習: 起承転結を備えた論説エッセイの構成", "300〜400語で論理的に意見を展開するパラグラフ・ライティング"),
    (89, "ukbi-writing-cause-and-effect-analysis", "UKBI記述演習: 因果関係を明快に論証するレポート作成", "karena itu, berakibat pada を駆使した分析文執筆"),
    (90, "ukbi-speaking-presentation-structure", "UKBI口頭演習: プレゼンテーションの論理構成とトランジション", "開会挨拶から結論・質疑応答までのスマートなスピーチ構成"),
    (91, "advanced-adverbial-niscaya-iscaya", "上級副詞: niscaya の文脈適合性と論理導出", "「必然的に必ずや」を表す格調高い副詞の正誤判定"),
    (92, "archaic-conjunctions-alkisah-sebermula", "古典・文学接続詞: alkisah / sebermula の文体識別", "伝統物語や文学作品の読解問題対策"),
    (93, "formal-passive-adversative-kehujanan", "文語・公的文脈における被害受動 ke-...-an の見極め", "文脈上「被害」を被っているか「能力」かを見抜く判定"),
    (94, "double-prefix-memper-functions", "二重接頭辞 memper-（使役比較・状態深化）の用法厳密判定", "memperbesar（より大きくする）と membuat lebih besar の関係"),
    (95, "double-prefix-memper-kan-causative", "複合使役 memper-...-kan と memper-...-i の接尾辞選択", "memperdebatkan（議論する）と memperingati（記念する）の接尾辞制約"),
    (96, "pronoun-honorific-hierarchy-beliau", "敬称代名詞 beliau と dia の公的言及における厳格な序列", "要人や恩師への言及で必須となる敬意のレベル設定"),
    (97, "negative-conjunction-tanpa-adverbial", "前置詞 tanpa + 動詞句による付帯状況否定構文", "「〜することなしに」を表す副詞節のスマートな形成"),
    (98, "elliptical-sentences-subject-omission", "新聞見出し・公報における助動詞・主語の省略復元演習", "極度に圧縮された見出しから完全なSVO文を復元する技術"),
    (99, "register-formal-vs-informal-markers", "公的文体と口語の混入判別・リライト技術", "ビジネス文書に混入した口語語彙（bikin, nggak, cuma等）の純化"),
    (100, "grand-exam-mock-simulation-sangat-unggul", "最高難度総合模擬演習: 特A級・UKBI最高峰突破ドリル", "文法・語彙・読解・正書法を横断する最難関総合問題"),
]

out_dir = "docs/exam-drills"

for num, slug, title, desc in EXAM_DRILLS_DATA:
    doc = f"""# U{num:02d}: {title}

インドネシア語技能検定（INKEN）B級・A級・特A級および国家検定UKBI（Uji Kemahiran Berbahasa Indonesia）最上位ランク突破を目指す学習者のための演習です。
本記事では、**{desc}** に焦点を当て、難問の構造を論理的に解き明かす実践トレーニングを行います。

---

## 1. 出題傾向と文法理論の徹底整理

- **出題背景**: {desc}
- **典型的な失点要因**: 直感的な日本語訳に頼ってしまい、インドネシア語固有の統語論（語順制約・接辞境界・EYD正書法規則）を見落とすこと。
- **攻略の鍵**: 文の骨格（主語・述語・目的語）を正確に特定し、接辞の派生規則や相関接続詞の呼応ルールを厳格に適用すること。

---

## 2. 実戦演習問題 (Soal Latihan)

<div class="id-example">
  <div class="id-sentence">
    <strong>[Soal]</strong><br>
    Pilihlah bentuk kalimat yang paling baku dan memenuhi kaidah tata bahasa resmi terkait topik {title.split('・')[0]}:<br>
    (A) Kalimat yang menggunakan struktur rancu tanpa memperhatikan kaidah subjek-predikat.<br>
    (B) Kalimat yang secara tepat menerapkan kaidah tata bahasa baku dan ejaan yang disempurnakan (EYD).<br>
    (C) Kalimat dengan penggunaan imbuhan ganda yang tidak berterima dalam ragam formal.<br>
    (D) Kalimat yang mencampurkan ragam lisan informal dalam teks resmi kenegaraan.
  </div>
  <div class="id-translation">
    <strong>【問題日本語訳】</strong><br>
    「{title.split('・')[0]}」に関して、最も標準的で公的文法規約を満たしている文を1つ選びなさい。
  </div>
</div>

---

## 3. 正答と徹底解説 (Kunci Jawaban & Pembahasan)

### 正答: (B) Kalimat yang secara tepat menerapkan kaidah tata bahasa baku...

> **文法法則のコア解説**
> 
> 本問のポイントは、「**{desc}**」を正確に理解し、公的表記基準に合致しているかを見極める点にあります。
> 選択肢(B)は、主語と述語の対応関係が明瞭であり、接辞の選択および修飾語の語順が文法的に完璧です。
> 
> 一方、他の選択肢には以下のような典型的な誤りが含まれています：
> - 主節と従属節における主語の脱落・不一致
> - 口語的な語彙や表現の不適切な混入
> - 接尾辞や周囲辞の過剰・不適切な付加

---

## 4. 検定・UKBI突破のための実践アドバイス

1. **品詞と文の主骨格を常に意識する**:
   - 複雑な修飾節に惑わされず、文の「S（主語）」と「P（述語）」がどこにあるかを瞬時に見抜く練習を積んでください。
2. **EYD（最新正書法）の分かち書き基準の徹底**:
   - 助詞 `pun` や `per`、複合語の綴りなど、ケアレスミスが生じやすい表記規則を日頃から確認しましょう。

---

## 5. 理解度チェッククイズ

<details class="id-quiz">
<summary>Q1. 本演習で扱った文法テーマにおける最大の盲点は？</summary>
<strong>正解: {desc}</strong><br>
解説: 表面的な単語の意味だけでなく、構文全体の文法的一貫性を常に確認しましょう。
</details>

<details class="id-quiz">
<summary>Q2. 上級・最上級検定で確実に得点するための学習法は？</summary>
<strong>正解: 公的文書や高級紙の社説を精読し、文法規約（EYDおよび標準文法）に照らして構文解析を行うこと</strong><br>
解説: 生きた公的文体に触れ続けることで、不自然な文や誤りを瞬時に違和感として感知できるようになります。
</details>
"""
    fname = f"u{num:02d}-{slug}.md"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(doc)

print(f"Successfully generated {len(EXAM_DRILLS_DATA)} exam drill articles in {out_dir}!")
