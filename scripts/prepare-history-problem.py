"""Extract reviewable sources from the authorized English edition; never overwrite translations."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
    ('preface', 7, 11, '序言', 1),
    ('intro', 13, 32, '导论', 2),
    ('ch1', 32, 60, '第一章 跨国分隔，1945—1964年', 3),
    ('ch2', 60, 86, '第二章 跨国互动的增长，1965—1988年', 4),
    ('ch3', 86, 114, '第三章 道歉与谴责，1989—1996年', 5),
    ('ch4', 114, 141, '第四章 民族主义与世界主义的共存，1997—2015年', 6),
    ('ch5', 141, 167, '第五章 东京审判的遗产', 7),
    ('ch6', 167, 190, '第六章 历史学家在历史问题中的作用', 8),
    ('conclusion', 190, 211, '结论', 9),
]

def lines(page):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            if 50 <= line['bbox'][1] < 605:
                yield line

def normalize(text):
    return text.replace('\u00ad', '').replace('\u00a0', ' ').replace('\ufb01', 'fi').replace('\ufb02', 'fl')

def extract(pdf, destination):
    document = pymupdf.open(pdf)
    if len(document) != 293 or 'The History' not in str(document.metadata.get('title')):
        raise ValueError('Expected the 293-page open-access edition of The History Problem')
    destination.mkdir(parents=True, exist_ok=True)
    manifest = {'source': 'https://www.loc.gov/item/2019666840/', 'sha256': hashlib.sha256(Path(pdf).read_bytes()).hexdigest(), 'pdfPages': len(document), 'sections': []}
    for key, start, end, title, chapter in SECTIONS:
        output = []
        refs = []
        for page_index in range(start, end):
            printed = str(page_index - 12) if page_index >= 13 else ['vii', 'viii', 'ix', 'x'][page_index - 7]
            output.append(f'\n[[P:{printed}]]\n')
            for line in lines(document[page_index]):
                parts = []
                for span in line['spans']:
                    text = normalize(span['text'])
                    if span['size'] < 8 and re.fullmatch(r'\d+', text.strip()):
                        number = int(text)
                        refs.append(number)
                        text = f'[[N:{key}:{number}]]'
                    parts.append(text)
                output.append(''.join(parts))
        content = '\n'.join(output) + '\n'
        (destination / f'{key}.txt').write_text(content, encoding='utf-8')
        manifest['sections'].append({'key': key, 'title': title, 'chapter': chapter, 'pdfStart': start + 1, 'pdfEnd': end, 'referenceNumbers': refs, 'sourceWords': len(content.split())})

    notes = {key: [] for key, *_ in SECTIONS if key != 'preface'}
    key = 'intro'
    current = None
    for page_index in range(211, 259):
        for line in lines(document[page_index]):
            text = normalize(''.join(span['text'] for span in line['spans'])).strip()
            if text in ('Notes', 'Introduction', 'Conclusion'):
                if text == 'Conclusion':
                    key, current = 'conclusion', None
                continue
            heading = re.match(r'Chapter\s+(\d):', text)
            if heading:
                key, current = f'ch{heading[1]}', None
                continue
            match = re.match(r'^(\d{1,3})\s+(.+)', text)
            if match and line['bbox'][0] < 70:
                current = {'number': int(match[1]), 'printedPage': page_index - 12, 'text': match[2]}
                notes[key].append(current)
            elif current is not None:
                current['text'] += '\n' + text
    for key, entries in notes.items():
        output = '\n\n'.join(f"[[D:{key}:{note['number']}]]\n[Original note page {note['printedPage']}]\n{note['text']}" for note in entries) + '\n'
        (destination / f'notes-{key}.txt').write_text(output, encoding='utf-8')
        section = next(s for s in manifest['sections'] if s['key'] == key)
        section['noteCount'] = len(entries)
        expected = list(range(1, len(entries) + 1))
        if [n['number'] for n in entries] != expected or sorted(section['referenceNumbers']) != expected:
            raise ValueError(f"Nonconsecutive notes/references in {key}: notes={[n['number'] for n in entries]}, refs={section['referenceNumbers']}")
    for key, start, end in [('bibliography', 259, 283), ('index', 283, 292), ('author', 292, 293)]:
        output = []
        for page_index in range(start, end):
            output.append(f'\n[[P:{page_index - 12}]]\n')
            output.extend(normalize(''.join(s['text'] for s in line['spans'])) for line in lines(document[page_index]))
        (destination / f'{key}.txt').write_text('\n'.join(output) + '\n', encoding='utf-8')
    (destination / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(manifest, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT / 'tmp' / 'pdfs' / 'history-problem')
    args = parser.parse_args()
    extract(args.pdf, args.output)
