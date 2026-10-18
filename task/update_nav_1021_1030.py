"""Add articles 1021-1030 to zensical.toml nav.
"""

def update_nav_1021_1030():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_articles = """      { "20: 接頭辞 meN- 自動詞と状態変化" = "output/20-prefix-men-intransitive.md" },
      { "21: 接頭辞 ber- 自動詞・状態動詞の即時産出" = "output/21-prefix-ber-intransitive.md" },
      { "22: ber- と meN- の使い分け対比ドリル" = "output/22-ber-vs-men-contrast.md" },
      { "23: 接頭辞 ter- の無意識・偶発用法の瞬間作文" = "output/23-prefix-ter-accidental.md" },
      { "24: 接頭辞 ter- の可能・不可能否定" = "output/24-prefix-ter-potential.md" },
      { "25: 接頭辞 ter- の最上級表現の瞬間生成" = "output/25-prefix-ter-superlative.md" },
      { "26: 接尾辞 -kan の使役構文" = "output/26-suffix-kan-causative-base.md" },
      { "27: 接尾辞 -kan の受益構文" = "output/27-suffix-kan-benefactive.md" },
      { "28: 接尾辞 -kan の道具・対象移動構文" = "output/28-suffix-kan-instrumental.md" },
      { "29: 接尾辞 -i の場所・方向への作用構文" = "output/29-suffix-i-locative.md" },
      { "30: 接尾辞 -i の反復・複数対象構文" = "output/30-suffix-i-repetitive.md" },"""

    target = """      { "20: 接頭辞 meN- 自動詞と状態変化" = "output/20-prefix-men-intransitive.md" },"""

    if target in content:
        new_content = content.replace(target, new_articles)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated nav with 1021-1030!")
    else:
        print("Target not found in zensical.toml")

if __name__ == "__main__":
    update_nav_1021_1030()
