import re

with open('zensical.toml.bak', 'r', encoding='utf-8') as f:
    text = f.read()

for cat in ['derivations', 'vocabulary', 'synonyms', 'situations', 'patterns', 'business-sectors', 'news-reading', 'exam-drills', 'geography-culture', 'slang-culture']:
    matches = re.findall(rf'{cat}/[^\"]+', text)
    if matches:
        print(f"{cat}: last 2 files = {matches[-2:]}")
    else:
        print(f"{cat}: no matches")
