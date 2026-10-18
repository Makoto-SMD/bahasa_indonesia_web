"""Add articles 1011-1020 to zensical.toml nav.
"""

def update_nav_1011_1020():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_articles = """      { "10: 比較級・最上級・同等比較" = "output/10-comparison-patterns.md" },
      { "11: 等位接続詞（dan, atau, tetapi, melainkan）の論理接続" = "output/11-conjunction-coordinating.md" },
      { "12: 従属接続詞の複文組み立て" = "output/12-conjunction-subordinating.md" },
      { "13: 助数詞と数量詞の即時産出" = "output/13-classifiers-counting.md" },
      { "14: 存在表現 ada の多機能構文" = "output/14-existential-ada.md" },
      { "15: 依頼・指示・禁止の使い分け" = "output/15-imperatives-requests.md" },
      { "16: 三人称 di- 受動態の瞬間組み立て" = "output/16-passive-prefix-di.md" },
      { "17: 一人称語幹受動態の自動発話化" = "output/17-passive-stem-first-person.md" },
      { "18: 二人称語幹受動態の反射出力" = "output/18-passive-stem-second-person.md" },
      { "19: 接頭辞 meN- 他動詞の鼻音化と即時発話" = "output/19-prefix-men-transitive.md" },
      { "20: 接頭辞 meN- 自動詞と状態変化" = "output/20-prefix-men-intransitive.md" },"""

    target = """      { "10: 比較級・最上級・同等比較" = "output/10-comparison-patterns.md" },"""

    if target in content:
        new_content = content.replace(target, new_articles)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated nav with 1011-1020!")
    else:
        print("Target not found in zensical.toml")

if __name__ == "__main__":
    update_nav_1011_1020()
