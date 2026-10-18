"""Add articles 1031-1040 to zensical.toml nav.
"""

def update_nav_1031_1040():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_articles = """      { "30: 接尾辞 -i の反復・複数対象構文" = "output/30-suffix-i-repetitive.md" },
      { "31: 接尾辞 -kan と -i の対比瞬間産出" = "output/31-suffix-kan-vs-i-contrast.md" },
      { "32: 周囲辞 ke-...-an の名詞化の瞬間生成" = "output/32-circumfix-ke-an-noun.md" },
      { "33: 周囲辞 ke-...-an の被災・不本意受動" = "output/33-circumfix-ke-an-adversative.md" },
      { "34: 周囲辞 ke-...-an の過度形容詞用法" = "output/34-circumfix-ke-an-excessive.md" },
      { "35: 周囲辞 peN-...-an の動作・過程名詞化" = "output/35-circumfix-pen-an-process.md" },
      { "36: 周囲辞 per-...-an の状態・集約名詞化" = "output/36-circumfix-per-an-result.md" },
      { "37: peN-...-an と per-...-an の使い分け対比ドリル" = "output/37-pen-an-vs-per-an-contrast.md" },
      { "38: 重複語の複数・多様性表現" = "output/38-reduplication-plural.md" },
      { "39: 重複語の相互行為表現" = "output/39-reduplication-reciprocal.md" },
      { "40: 重複語の強調・度合い表現" = "output/40-reduplication-intensity.md" },"""

    target = """      { "30: 接尾辞 -i の反復・複数対象構文" = "output/30-suffix-i-repetitive.md" },"""

    if target in content:
        new_content = content.replace(target, new_articles)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated nav with 1031-1040!")
    else:
        print("Target not found in zensical.toml")

if __name__ == "__main__":
    update_nav_1031_1040()
