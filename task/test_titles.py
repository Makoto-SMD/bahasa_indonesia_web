import os
import glob

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                # Remove leading '# ' and any quotes/formatting
                title = line[2:].strip()
                # Clean up quotes if present
                title = title.replace('"', '\\"')
                return title
    # Fallback to filename
    base = os.path.basename(file_path)
    return os.path.splitext(base)[0]

sample_dirs = ['docs/literature', 'docs/dialects', 'docs/derivations']
for d in sample_dirs:
    files = sorted(glob.glob(os.path.join(d, '*.md')))
    print(f"Sample from {d}:")
    for f in files[:3]:
        print(f"  {os.path.basename(f)} -> {get_title(f)}")
