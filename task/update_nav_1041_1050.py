"""Add articles 1041-1050 to zensical.toml nav.
"""

def update_nav_1041_1050():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_articles = """      { "40: 重複語の強調・度合い表現" = "output/40-reduplication-intensity.md" },
      { "41: 関係詞 yang による長文修飾と焦点化構文" = "output/41-complex-relative-yang.md" },
      { "42: 名詞節を導く bahwa 構文の瞬間展開" = "output/42-nominal-clause-bahwa.md" },
      { "43: 譲歩節による複文構築" = "output/43-concessive-meskipun.md" },
      { "44: 条件節・仮定法の瞬時産出" = "output/44-conditional-jika-seandainya.md" },
      { "45: 目的節による論理的表現の瞬間生成" = "output/45-purpose-agar-supaya.md" },
      { "46: 結果節の即時産出" = "output/46-result-sehingga-makanya.md" },
      { "47: 様態副詞・確信度の反射産出" = "output/47-modal-adv-mungkin-pasti.md" },
      { "48: 発話を和らげるクッション言葉" = "output/48-polite-honorific-softener.md" },
      { "49: 定型チャンクの反射発話" = "output/49-idiomatic-fixed-chunks.md" },
      { "50: 総合スピード作文テスト：実戦会話50本連続ノック" = "output/50-comprehensive-rapid-drill.md" },"""

    target = """      { "40: 重複語の強調・度合い表現" = "output/40-reduplication-intensity.md" },"""

    if target in content:
        new_content = content.replace(target, new_articles)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated nav with 1041-1050!")
    else:
        print("Target not found in zensical.toml")

if __name__ == "__main__":
    update_nav_1041_1050()
