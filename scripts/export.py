"""Regenerate data/glossary.csv and data/glossary.jsonl from data/glossary.json,
then refresh the JSON-LD in index.html.  Usage: python3 scripts/export.py"""
import json, csv, pathlib, subprocess, sys
root = pathlib.Path(__file__).resolve().parent.parent
terms = json.loads((root/'data/glossary.json').read_text(encoding='utf-8'))['terms']
with open(root/'data/glossary.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(terms[0].keys())); w.writeheader(); w.writerows(terms)
with open(root/'data/glossary.jsonl', 'w', encoding='utf-8') as f:
    for t in terms: f.write(json.dumps(t, ensure_ascii=False) + '\n')
print(f'{len(terms)} terms exported')
subprocess.run([sys.executable, str(root/'scripts/build_site.py')], check=True)
