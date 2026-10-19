# -*- coding: utf-8 -*-
with open('zensical.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_idx = -1
for i, line in enumerate(lines):
    if 'contemporary/30-heritage-railway-revival.md' in line:
        target_idx = i
        break

assert target_idx != -1, "Target line not found"

new_articles = [
    '      { "ナトゥナ諸島の海洋主権と排他的経済水域（EEZ）防衛：国連海洋法条約に基づく海洋安保" = "contemporary/31-maritime-defense-natuna.md" },\n',
    '      { "国家研究イノベーション庁（BRIN）と通信衛星SATRIA-1：離島遠隔地を結ぶデジタルインフラ" = "contemporary/32-space-agency-brin-satellites.md" },\n',
    '      { "モバイルレジェンド（MLBB）熱狂と急拡大するeスポーツ産業：競技スポーツ化と若者文化" = "contemporary/33-esports-gaming-phenomenon.md" },\n',
    '      { "世界へ羽ばたくインドネシアのウェブトゥーン作家群：縦スクロール漫画のグローバルIP革命" = "contemporary/34-comic-webtoon-creators.md" },\n',
    '      { "地場スキンケア・コスメブランド（Scarlett, Somethinc）の躍進：熱帯処方とD2C戦略" = "contemporary/35-local-cosmetics-skincare.md" },\n',
    '      { "都市部若者のマイホーム断念危機と公的住宅ローン（KPR）改革：TOD型垂直集合住宅の挑戦" = "contemporary/36-housing-affordability-crisis.md" },\n',
    '      { "公共交通統合システム「JakLingko」と都市モビリティ革命：アンコット近代化と定額運賃" = "contemporary/37-public-transport-integration-jaklingko.md" },\n',
    '      { "泥炭地再生機構（BRGM）と森林泥炭火災（ヘイズ）の根絶挑戦：3Rアプローチと湿潤農業" = "contemporary/38-peatland-restoration-fires.md" },\n',
    '      { "土着信仰（Penghayat Kepercayaan）の復権と身分証（KTP）明記：憲法裁判所判決と市民権の平等" = "contemporary/39-indigenous-faith-recognition.md" },
    '      { "活火山と共生する島々：メラピ防災地域ネットワークと伝承：科学観測と住民自治無線の融合" = "contemporary/40-volcano-disaster-resilience.md" },\n',
]

lines[target_idx+1:target_idx+1] = new_articles

with open('zensical.toml', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated zensical.toml successfully.")
