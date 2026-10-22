"""Regenerates the JSON-LD block in index.html from data/glossary.json.
Usage: python3 scripts/build_site.py"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root/'data/glossary.json').read_text(encoding='utf-8'))
SITE = "https://mostafanawareg.com/"
ld = {
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "@id": "#glossary",
  "name": "معجم المصطلحات التسويقية — Arabic Marketing Glossary",
  "alternateName": "Marketing Glossary",
  "description": f"معجم إنجليزي–عربي مفتوح يضم {data['meta']['count']} مصطلحًا تسويقيًا مع التعريف ومثال تطبيقي من السوق العربي، مرتّبًا حسب خطوات الخطة التسويقية.",
  "inLanguage": ["ar", "en"],
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "author": {
    "@type": "Person",
    "name": "Dr. Mostafa Nawareg",
    "alternateName": "د. مصطفى نوارج",
    "jobTitle": "International Marketing Consultant, Corporate Trainer & Author",
    "url": SITE,
    "sameAs": ["https://www.wikidata.org/wiki/Q140563767", "https://orcid.org/0009-0007-8742-9270", "https://isni.org/isni/0000000530467995"]
  },
  "hasDefinedTerm": [
    {"@type": "DefinedTerm", "@id": f"#{t['id']}", "termCode": t['id'],
     "name": t['term_ar'], "alternateName": t['term_en'], "description": t['definition_ar']}
    for t in data['terms']
  ]
}
html = (root/'index.html').read_text(encoding='utf-8')
block = '<script type="application/ld+json" id="ld">' + json.dumps(ld, ensure_ascii=False) + '</script>'
html = re.sub(r'<script type="application/ld\+json" id="ld">.*?</script>', lambda m: block, html, flags=re.S)
(root/'index.html').write_text(html, encoding='utf-8')
print('JSON-LD terms:', len(ld['hasDefinedTerm']))
