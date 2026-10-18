import os
import re
import shutil

# Restore from original backup
shutil.copyfile('zensical.toml.bak', 'zensical.toml')

def clean_nav_title(title):
    title = re.sub(r'\*\*(.*?)\*\*', r'\1', title)
    title = re.sub(r'\*(.*?)\*', r'\1', title)
    title = re.sub(r'`(.*?)`', r'\1', title)
    title = title.replace('"', "'")
    return title.strip()

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                return clean_nav_title(line[2:])
    base = os.path.basename(file_path)
    return clean_nav_title(os.path.splitext(base)[0])

with open('zensical.toml', 'r', encoding='utf-8') as f:
    orig_content = f.read()

referenced_files = set(re.findall(r'\"([^\"]+\.md)\"', orig_content))

def get_unreferenced_sorted(directory):
    files = []
    dir_path = os.path.join('docs', directory)
    for f in os.listdir(dir_path):
        if f.endswith('.md'):
            rel = f"{directory}/{f}".replace('\\', '/')
            if rel not in referenced_files:
                files.append(rel)
    files.sort()
    return files

with open('zensical.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    
    # 1. derivations: after root-terima.md
    if 'derivations/root-terima.md' in line:
        unref = get_unreferenced_sorted('derivations')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 2. vocabulary: after travel-tourism.md
    elif 'vocabulary/travel-tourism.md' in line:
        unref = get_unreferenced_sorted('vocabulary')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 3. synonyms: after c50-rusak-vs-hancur-vs-punah-vs-binasa.md
    elif 'synonyms/c50-rusak-vs-hancur-vs-punah-vs-binasa.md' in line:
        unref = get_unreferenced_sorted('synonyms')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 4. situations: after charity-zakat.md
    elif 'situations/charity-zakat.md' in line:
        unref = get_unreferenced_sorted('situations')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 5. patterns: after conclusions-projections.md
    elif 'patterns/conclusions-projections.md' in line:
        unref = get_unreferenced_sorted('patterns')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 6. business-sectors: after finance-internal-audit-compliance.md
    elif 'business-sectors/finance-internal-audit-compliance.md' in line:
        unref = get_unreferenced_sorted('business-sectors')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 7. news-reading: after n50-disaster-resilience-inatews-early-warning.md
    elif 'news-reading/n50-disaster-resilience-inatews-early-warning.md' in line:
        unref = get_unreferenced_sorted('news-reading')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')

    # 8. exam-drills: after u50-exam-idioms-compound-expressions.md
    elif 'exam-drills/u50-exam-idioms-compound-expressions.md' in line:
        unref = get_unreferenced_sorted('exam-drills')
        for f in unref:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')
        # Add literature section directly following exam-drills
        new_lines.append('    { "古典・民話・名作文学読解" = [\n')
        lit_files = get_unreferenced_sorted('literature')
        for f in lit_files:
            full_path = os.path.join('docs', f)
            title = get_title(full_path)
            new_lines.append(f'      {{ "{title}" = "{f}" }},\n')
        new_lines.append('    ] },\n')

# Write updated content
with open('zensical.toml', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Inject dialects block after social-connections
with open('zensical.toml', 'r', encoding='utf-8') as f:
    cur = f.read()

target_str = '      { "スモールトーク（Basa-basi）と笑顔" = "slang-culture/social-connections.md" },\n    ] },'

dialect_block = target_str + '\n    { "地方言語・方言カルチャー事典" = [\n'
dia_files = get_unreferenced_sorted('dialects')
for f in dia_files:
    full_path = os.path.join('docs', f)
    title = get_title(full_path)
    dialect_block += f'      {{ "{title}" = "{f}" }},\n'
dialect_block += '    ] },'

if target_str in cur:
    cur = cur.replace(target_str, dialect_block, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(cur)
    print("Successfully injected dialects block!")
else:
    print("Warning: target_str not found for dialects!")

print("Nav update completed.")
