from pathlib import Path

for path_str in ['backend/app/data/schemes_central.py', 'backend/app/data/schemes_karnataka.py']:
    p = Path(path_str)
    if p.exists():
        text = p.read_text(encoding='utf-8')
        count = text.count('contains_any')
        if count > 0:
            text = text.replace('"contains_any"', '"any_of"').replace("'contains_any'", "'any_of'")
            p.write_text(text, encoding='utf-8')
            print(f'Replaced {count} occurrences of contains_any with any_of in {p}')

