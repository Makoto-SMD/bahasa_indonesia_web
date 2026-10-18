import re
import os

with open('zensical.toml', 'r', encoding='utf-8') as f:
    toml_text = f.read()

lines = toml_text.splitlines()

sections = []
current_section = None
current_items = []

in_nav = False
for line in lines:
    line_s = line.strip()
    if line_s == 'nav = [':
        in_nav = True
        continue
    if in_nav and line_s == ']':
        break
    if not in_nav:
        continue
    
    sec_match = re.match(r'^\s{4}\{\s*"([^"]+)"\s*=\s*\[', line)
    if sec_match:
        if current_section and current_items:
            sections.append((current_section, current_items))
        current_section = sec_match.group(1)
        current_items = []
        continue
    
    item_match = re.match(r'^\s*\{\s*"([^"]+)"\s*=\s*"([^"]+\.md)"\s*\}', line)
    if item_match:
        title = item_match.group(1)
        path = item_match.group(2)
        if current_section:
            current_items.append((title, path))

if current_section and current_items:
    sections.append((current_section, current_items))

# Build Markdown for sitemap.md
out = []
out.append("---")
out.append("icon: lucide/map")
out.append("title: 総合サイトマップ・全コンテンツ目録")
out.append("---")
out.append("")
out.append("# 総合サイトマップ・全コンテンツ目録")
out.append("### Peta Situs Lengkap & Indeks Pembelajaran Bahasa Indonesia")
out.append("")
out.append("当ナレッジベースに収録されている**全1,000記事**の体系的完全目録です。")
out.append("初心者から最上級者・実務エキスパートまで、目的やレベルに合わせて体系的に学習を進められます。")
out.append("")
out.append("> [!TIP]")
out.append("> **お探しのコンテンツの探し方**:")
out.append("> - 上部の検索窓（ショートカット: <kbd>S</kbd> または <kbd>/</kbd>）からキーワードで瞬時に記事を検索できます。")
out.append("> - 下記の「**目的別・レベル別おすすめ学習ルート**」から、ご自身の目標に合わせた最短コースを選択できます。")
out.append("> - 各ジャンルの目次から気になるトピックへ直接ジャンプできます。")
out.append("")
out.append("---")
out.append("")
out.append("## 🎯 目的別・レベル別おすすめ学習ルート")
out.append("")
out.append('<div class="grid cards" markdown>')
out.append("")
out.append("-   :lucide-compass: **【入門・初級】ゼロから始める基礎力養成コース**")
out.append("")
out.append("    ---")
out.append("")
out.append("    文字と発音（8記事） → 基本文法（16記事） → 日常会話（20記事） → 基本接辞（meN-, di-, ber-）")
out.append("    ローマ字読みの感覚からSVO語順、基本挨拶まで最短2〜3週間で土台を完成させます。")
out.append("    [:octicons-arrow-right-24: 文字と発音から始める](pronunciation/alphabet-vowels.md)")
out.append("")
out.append("-   :lucide-plane: **【旅行・生活】インドネシア現地サバイバルコース**")
out.append("")
out.append("    ---")
out.append("")
out.append("    日常会話（20記事） → 実践対話・トラブル解決（100記事） → 万能パターンドリル（100記事） → スラング・口語（8記事）")
out.append("    Grab配車、屋台注文、アパート修理、病院受診など、現地で即座に役立つ実践口頭フレーズを網羅。")
out.append("    [:octicons-arrow-right-24: 日常会話を見る](conversation/greetings.md)")
out.append("")
out.append("-   :lucide-briefcase: **【ビジネス・赴任】実務交渉・マネジメント特化コース**")
out.append("")
out.append("    ---")
out.append("")
out.append("    ビジネス基礎（10記事） → 業界別実務（製造・IT・物流・金融・法務・農業・鉱業等：100記事） → パターンドリル")
out.append("    朝礼、KPI評価、解雇・就業規則、税務通関、監査など、インドネシア人部下・取引先との協働に必須の実務語彙。")
out.append("    [:octicons-arrow-right-24: ビジネス基礎を見る](business/office-greetings.md)")
out.append("")
out.append("-   :lucide-award: **【検定・資格】検定合格・UKBI突破コース**")
out.append("")
out.append("    ---")
out.append("")
out.append("    接辞完全攻略（16記事） → 語根別派生語（100記事） → 検定・UKBI突破演習（100記事） → 類義語徹底比較（100記事）")
out.append("    インドネシア語技能検定（C級〜特A級）や国家検定UKBIの最頻出ポイント、倒置、正書法（EYD）、接辞制約を制覇。")
out.append("    [:octicons-arrow-right-24: 検定突破演習を見る](exam-drills/u01-affixes-kan-vs-i-distinction.md)")
out.append("")
out.append("-   :lucide-newspaper: **【中上級読解】時事・論説・古典教養深掘りコース**")
out.append("")
out.append("    ---")
out.append("")
out.append("    長文読解（10記事） → 時事ニュース読解（100記事） → 古典・民話・名作文学（50記事） → 地方言語・方言（50記事） → 地理文化（40記事）")
out.append("    新首都IKNや経済改革から民話マク・カラン・ジャワ語・スンダ語文化まで、社会を深く理解するための総合教養。")
out.append("    [:octicons-arrow-right-24: 時事ニュース読解を見る](news-reading/n01-ikn-infrastructure-investment.md)")
out.append("")
out.append("</div>")
out.append("")
out.append("---")
out.append("")
out.append("## 📑 全セクション一覧ナビゲーション")
out.append("")

for idx, (sec_name, items) in enumerate(sections, start=1):
    out.append(f"{idx}. [{sec_name}](#sec-{idx:02d})（全{len(items)}記事）")

out.append("")
out.append("---")
out.append("")

for idx, (sec_name, items) in enumerate(sections, start=1):
    out.append(f"### {idx}. {sec_name} {{: #sec-{idx:02d} }}")
    out.append(f"全{len(items)}記事を収録しています。")
    out.append("")
    for title, path in items:
        out.append(f"- [{title}]({path})")
    out.append("")

with open('docs/sitemap.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("Successfully regenerated docs/sitemap.md with all 1,000 articles!")
