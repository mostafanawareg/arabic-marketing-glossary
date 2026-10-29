<div dir="rtl">

# معجم المصطلحات التسويقية — Arabic Marketing Glossary

**375 مصطلحًا تسويقيًا (إنجليزي ← عربي)، لكل مصطلح تعريف ومثال تطبيقي من السوق العربي، مرتّبة حسب خطوات الخطة التسويقية.**

إعداد: **د. مصطفى نوارج** — استشاري تسويق دولي، مدرّب شركات ومؤلف · [mostafanawareg.com](https://mostafanawareg.com/)

🔎 **ابحث في المعجم مباشرة:** افتح صفحة المشروع على GitHub Pages (`index.html`).

</div>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Terms](https://img.shields.io/badge/terms-375-F18F01)
![Languages](https://img.shields.io/badge/lang-Arabic%20%7C%20English-1a1a2e)

---

## English

An open, structured **English ↔ Arabic marketing glossary**: 375 terms, each with an Arabic definition and a real-world example drawn from Arab markets (KSA, UAE, Egypt and beyond). Terms follow the logical order of a marketing plan, from market analysis to international marketing.

Useful for:

- **Arabic NLP & LLM work**: terminology alignment, glossary-constrained translation, RAG grounding, evaluation sets
- **Translators & localisation teams**: consistent Arabic equivalents for marketing vocabulary
- **Students, trainers & marketers**: a searchable reference with practical examples
- **App builders**: drop-in data for tooltips, quizzes, flashcards and chatbots

### Data

| File | Format | Notes |
|---|---|---|
| [`data/glossary.json`](data/glossary.json) | JSON | `{ meta, terms[] }`, includes chapter list |
| [`data/glossary.csv`](data/glossary.csv) | CSV (UTF-8 with BOM) | Opens correctly in Excel |
| [`data/glossary.jsonl`](data/glossary.jsonl) | JSON Lines | One term per line, handy for ML pipelines |

Each term:

```json
{
  "id": "MG-122",
  "chapter": 2,
  "chapter_ar": "التسويق الاستراتيجي",
  "chapter_en": "Strategic Marketing",
  "code": "3.2.3.3",
  "term_en": "Less for Less (L4L)",
  "term_ar": "أقل مقابل أقل",
  "definition_ar": "تقديم منتج أساسي بأقل سعر ممكن.",
  "example_ar": "علامات القيمة الأساسية المخفضة في \"كارفور\" و\"بنده\" ...",
  "parent_id": "MG-119"
}
```

- `id`: stable identifier (`MG-001` … `MG-375`); safe to link to (`index.html#MG-122`)
- `code`: the term's position in the book's outline, numbered within its chapter
- `parent_id`: the broader term this one belongs to (builds a taxonomy tree), or `null`

### Chapters

| # | Arabic | English | Terms |
|---|---|---|---|
| 1 | نظام المعلومات التسويقية | Marketing Information System | 48 |
| 2 | التسويق الاستراتيجي | Strategic Marketing | 84 |
| 3 | التسويق التكتيكي | Tactical Marketing (Marketing Mix) | 171 |
| 4 | استراتيجيات التسويق | Marketing Strategies | 37 |
| 5 | التسويق الدولي | International Marketing | 35 |

### Quick start

```python
import json
terms = json.load(open("data/glossary.json", encoding="utf-8"))["terms"]
lookup = {t["term_en"].lower(): t["term_ar"] for t in terms}
print(lookup["market segmentation"])  # تجزئة السوق
```

```js
const { terms } = await (await fetch("data/glossary.json")).json();
```

### Source

The data is extracted from the book **«معجم المصطلحات التسويقية» (Marketing Glossary)** by Dr. Mostafa Nawareg. The full book is available as an ebook: **[mostafanawareg.com/books](https://mostafanawareg.com/books/)**.

### License & attribution

Released under **[CC BY 4.0](LICENSE)**. You may use, adapt and redistribute it, including commercially, **as long as you credit the author**:

> Nawareg, M. *Arabic Marketing Glossary (معجم المصطلحات التسويقية)*. https://mostafanawareg.com/ — CC BY 4.0

See [`CITATION.cff`](CITATION.cff) for academic citation (GitHub's “Cite this repository” button uses it).

### Contributing

Spotted a typo, a better Arabic equivalent, or an outdated example? Open an issue or a pull request. Please edit `data/glossary.json`, then run `python3 scripts/export.py` to regenerate the CSV, JSONL and page metadata.

---

<div dir="rtl">

## بالعربي

معجم مفتوح ومنظَّم للمصطلحات التسويقية، يضم **375 مصطلحًا**. لكل مصطلح:

- المصطلح بالإنجليزي والعربي
- تعريف واضح
- مثال تطبيقي من السوق العربي

المصطلحات مرتّبة حسب خطوات الخطة التسويقية: نظام المعلومات التسويقية، ثم التسويق الاستراتيجي، ثم المزيج التسويقي، ثم استراتيجيات التسويق، ثم التسويق الدولي.

**لمن هذا المعجم؟**

- طلاب التسويق والباحثون
- المدرّبون والمترجمون
- فرق التسويق
- مطوّرو تطبيقات الذكاء الاصطناعي العربية

**الترخيص:** CC BY 4.0. الاستخدام والتعديل وإعادة النشر مسموحة، حتى للأغراض التجارية، **بشرط ذكر المصدر**: د. مصطفى نوارج، mostafanawareg.com.

**ساهم:** لو عندك تصحيح أو مقابل عربي أدق، افتح Issue أو Pull Request.

⭐ إذا أفادك المعجم، ادعمه بنجمة ليصل إلى غيرك.

**روابط:**

- [الموقع الرسمي](https://mostafanawareg.com/)
- [الكتاب كاملًا: معجم المصطلحات التسويقية](https://mostafanawareg.com/books/)
- [أدوات Marketing Planner AI المجانية](https://marketingplannerai.mostafanawareg.com/)
- [Wikidata](https://www.wikidata.org/wiki/Q140563767)
- [ORCID](https://orcid.org/0009-0007-8742-9270)

</div>
