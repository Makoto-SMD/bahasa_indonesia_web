import ast

with open('task/write_batch_1361_1370.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Execute code to get articles
locs = {}
code_to_run = text[:text.find('def generate_markdown')]
exec(code_to_run, locs)
articles = locs.get('articles', [])

for idx, a in enumerate(articles):
    root = a.get('root')
    for m_idx, row in enumerate(a.get('matrix', [])):
        if len(row) != 5:
            print(f"Article {idx} ({root}) matrix[{m_idx}] len={len(row)}: {row}")
    for d_idx, row in enumerate(a.get('details', [])):
        if len(row) != 7:
            print(f"Article {idx} ({root}) details[{d_idx}] len={len(row)}: {row}")
print("Check completed.")
