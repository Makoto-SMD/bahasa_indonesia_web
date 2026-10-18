"""Add Clinic section to zensical.toml nav.
"""

def update_nav_clinic_part1():
    with open("zensical.toml", "r", encoding="utf-8") as f:
        content = f.read()

    new_section = """    { "日本人特有の不自然な表現・矯正クリニック" = [
      { "01: 「〜した＝sudah」の呪縛！過去テンスとアスペクト完了の混同" = "clinic/01-sudah-tense-overuse.md" },
      { "02: 「〜てあげる/もらう」を memberi で直訳しない！" = "clinic/02-memberi-giving-receiving.md" },
      { "03: 無生物主語の壁！「この薬を飲めば治る」の表現法" = "clinic/03-inanimate-subject-avoidance.md" },
      { "04: 日本語の受身「〜される」の過剰直訳を排す" = "clinic/04-passive-voice-overuse.md" },
      { "05: 「〜しておく」の直訳ミスを防ぐ（siapkan, biarkan, dulu）" = "clinic/05-te-oku-preparatory.md" },
      { "06: 「〜てしまう（後悔・完了）」の直訳ミス" = "clinic/06-te-shimau-regret-accident.md" },
      { "07: 「遠慮・遠回しな断り」が招く誤解と温かい断り方" = "clinic/07-indirect-politeness-clash.md" },
      { "08: 「持っている/ある」の混乱（Ada vs Punya vs Memiliki）" = "clinic/08-ada-punya-confusion.md" },
      { "09: 「できる」の使い分けミス（mampu vs bisa vs dapat）" = "clinic/09-bisa-dapat-mampu-misuse.md" },
      { "10: 「〜するつもり/〜だろう」の mau と akan の混同矯正" = "clinic/10-mau-akan-distinction.md" },
    ] },"""

    target = """      { "50: 総合スピード作文テスト：実戦会話50本連続ノック" = "output/50-comprehensive-rapid-drill.md" },
    ] },"""

    replacement = """      { "50: 総合スピード作文テスト：実戦会話50本連続ノック" = "output/50-comprehensive-rapid-drill.md" },
    ] },
""" + new_section

    if target in content:
        new_content = content.replace(target, replacement)
        with open("zensical.toml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated nav with clinic part 1!")
    else:
        print("Target not found in zensical.toml")

if __name__ == "__main__":
    update_nav_clinic_part1()
