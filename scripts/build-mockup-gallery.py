"""Build the mock-up catalogue from the images documented in README.md."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / 'README.md').read_text()

class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'img':
            src = values.get('src', '')
            assert (ROOT / src).is_file(), src
            self.images.append({'src': src, 'alt': values.get('alt', ''),
                                'device': 'mobile' if 'mobile-' in src else 'web'})

def images(section):
    parser = Images()
    parser.feed(section)
    return parser.images

landing = text.split('### 6.3.2. Landing Page Mock-up', 1)[1].split('## 6.4.', 1)[0]
items = [{'id': 'L01', 'title': 'Landing pública', 'category': 'landing',
          'description': 'Presentación de Talki, beneficios, pasos de uso y planes.',
          'images': images(landing)}]
section = text.split('### 6.4.3. Applications Mock-ups', 1)[1].split('### 6.4.4.', 1)[0]
headings = list(re.finditer(r'^#{4,5} (.+)$', section, re.M))
state_index = 0
for i, match in enumerate(headings):
    title = match.group(1)
    body = section[match.end():headings[i+1].start() if i+1 < len(headings) else len(section)]
    pics = images(body)
    if not pics:
        continue
    category = 'states' if match.group(0).startswith('#####') else 'app'
    if ': ' in title:
        code, title = title.split(': ', 1)
    elif category == 'states':
        state_index += 1
        code = f'E{state_index:02}'
    else:
        code = 'R02'
    paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]
    description = re.sub(r'\*\*([^*]+)\*\*', r'\1', paragraphs[0])
    items.append({'id': code, 'title': title, 'category': category,
                  'description': description, 'images': pics})
assert len(items) == 26, f'Unexpected number of screens: {len(items)}'
assert sum(len(x['images']) for x in items) == 51
assert len({pic['src'] for item in items for pic in item['images']}) == 51
out = ROOT / 'assets/ux/gallery/screens.js'
out.write_text('window.TALKI_MOCKUPS = ' + json.dumps(items, ensure_ascii=False, indent=2) + ';\n')
print('Catalogue generated: 26 screens, 51 images; every source exists.')
