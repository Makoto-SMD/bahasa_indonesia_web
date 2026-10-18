import re
import os

with open('zensical.toml', 'r', encoding='utf-8') as f:
    toml_text = f.read()

# Parse nav entries
# In zensical.toml, nav structure is roughly:
# nav = [
#   { "Group" = [
#     { "Section" = [
#       { "Title" = "path.md" },
#     ] },
#   ] },
# ]

# We can parse the sections and their items:
lines = toml_text.splitlines()

# Let's inspect all section names
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
    
    # Section match: { "Section Name" = [
    # Top group match: { "Top Group" = [ (usually 2 spaces indent)
    # Section match: 4 spaces indent:     { "Section Name" = [
    sec_match = re.match(r'^\s{4}\{\s*"([^"]+)"\s*=\s*\[', line)
    if sec_match:
        if current_section and current_items:
            sections.append((current_section, current_items))
        current_section = sec_match.group(1)
        current_items = []
        continue
    
    # Item match: 6 spaces indent:       { "Title" = "path.md" },
    item_match = re.match(r'^\s*\{\s*"([^"]+)"\s*=\s*"([^"]+\.md)"\s*\}', line)
    if item_match:
        title = item_match.group(1)
        path = item_match.group(2)
        if current_section:
            current_items.append((title, path))

if current_section and current_items:
    sections.append((current_section, current_items))

print(f"Parsed {len(sections)} sections:")
total_articles = 0
for name, items in sections:
    print(f"  {name}: {len(items)} articles")
    total_articles += len(items)
print(f"Total articles in nav: {total_articles}")
