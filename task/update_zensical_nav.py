"""Update zensical.toml with new SLA section in nav.
"""

def update_zensical_nav():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_section_block = """  { "SLA実践演習・自動化" = [
    { "瞬間口頭作文＆パターンプラクティス" = [
      { "01: 基本語順（SVO）と名詞修飾（DM則）の即時産出" = "output/01-svo-word-order.md" },
      { "02: 否定詞 tidak と bukan の反射的使い分け" = "output/02-negation-tidak-bukan.md" },
      { "03: 親称代名詞の適切な使い分け" = "output/03-pronouns-kinship.md" },
      { "04: 指示詞 ini / itu と場所表現の瞬発力" = "output/04-demonstratives-ini-itu.md" },
      { "05: 疑問詞（5W1H）の即座疑問文" = "output/05-question-words-5w1h.md" },
      { "06: アスペクト副詞の反射文生成" = "output/06-aspect-markers.md" },
      { "07: 前置詞の場所・方向マッピング" = "output/07-basic-prepositions.md" },
      { "08: 抽象前置詞の文脈適用" = "output/08-abstract-prepositions.md" },
      { "09: 助動詞のニュアンス即座出力" = "output/09-auxiliary-verbs.md" },
      { "10: 比較級・最上級・同等比較" = "output/10-comparison-patterns.md" },
    ] },
  ] },
]"""

    target_ending = "    ] },\n  ] },\n]"
    if target_ending in content:
        new_content = content.replace(target_ending, "    ] },\n  ] },\n" + new_section_block)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("zensical.toml successfully updated!")
    else:
        print("Could not find target_ending in zensical.toml")

if __name__ == "__main__":
    update_zensical_nav()
