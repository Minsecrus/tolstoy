"""Verify all index items and source-line markers in the export's Pandoc AST.

This check parses existing Markdown and writes only QA JSON, never a PDF/TeX.
Run check-representation-theory-index.mjs first to refresh the exact reading bodies.
"""
import importlib.util
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'tmp/pdfs/representation-theory-index-qa'
spec = importlib.util.spec_from_file_location('representation_export', ROOT / 'scripts/export-representation-theory-pdf.py')
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


def text(node):
    if isinstance(node, list):
        return ''.join(text(value) for value in node)
    if not isinstance(node, dict):
        return ''
    kind = node.get('t')
    if kind == 'Str':
        return node['c']
    if kind in ['Space','SoftBreak','LineBreak']:
        return ' '
    if kind == 'Math':
        return '$' + node['c'][1] + '$'
    if kind in ['BulletList','RawInline','RawBlock']:
        return ''
    return ''.join(text(value) for value in node.values())


def collect(bullet_list, records, parent=None, depth=0):
    for item in bullet_list['c']:
        index = len(records)
        own = [block for block in item if block.get('t') != 'BulletList']
        raw = []
        def markers(node):
            if isinstance(node, list):
                for value in node: markers(value)
            elif isinstance(node, dict):
                if node.get('t') == 'RawInline':
                    raw.extend(re.findall(r'\\source(begin|end)\{(\d+)\}', node['c'][1]))
                else:
                    for value in node.values(): markers(value)
        markers(own)
        records.append({'depth':depth,'parent':parent,'text':text(own).strip(),'sourceMarkers':raw})
        for block in item:
            if block.get('t') == 'BulletList':
                collect(block,records,index,depth+1)


reports = []
def compact(value):
    # Pandoc's smart prose punctuation may turn ASCII apostrophes/quotes into
    # their typographic glyphs; it does not alter the index term or any math.
    return re.sub(r'\s+','',value.translate(str.maketrans({'‘':"'",'’':"'",'“':'"','”':'"'})))

for language in ('zh','en'):
    section = json.loads((WORK / f'reading-index-{language}.json').read_text(encoding='utf8'))
    expected,stack=[],[]
    for page in section['pages']:
        source = (ROOT / f"source/representation-theory/{language}/pdf-{page['pdfPage']:04d}.md").read_text(encoding='utf8')
        for line in source.splitlines():
            bullet = re.match(r'^([ \t]*)[-+*][ \t]+(.*)$',line)
            if not bullet: continue
            depth = len(bullet[1].expandtabs(4)) // 2
            assert depth == 0 or len(stack) >= depth, (language,page['pdfPage'],'missing source parent')
            expected.append({'sourcePdfPage':page['pdfPage'],'depth':depth,'parent':stack[depth-1] if depth else None,'text':bullet[2]})
            stack = stack[:depth] + [len(expected)-1]
    joined = None
    for page in section['pages']:
        blocks = json.loads(subprocess.run(['pandoc','-f','markdown-fancy_lists','-t','json'],input=page['body'],
                            text=True,encoding='utf8',stdout=subprocess.PIPE,check=True).stdout)['blocks']
        assert len(blocks)==1 and blocks[0]['t']=='BulletList', (language,page['pdfPage'],'source not a single index list')
        exporter.attach_boundary(blocks,page['pdfPage'])
        exporter.attach_boundary(blocks,page['pdfPage'],end=True)
        if joined is None:
            joined = blocks[0]
        else:
            exporter.merge_index_page(joined,blocks[0],page['body'])
    actual=[]
    collect(joined,actual)
    assert len(actual)==len(expected) and len(expected)>0, (language,len(actual),len(expected))
    for index,(saved,source) in enumerate(zip(actual,expected)):
        assert saved['depth']==source['depth'] and saved['parent']==source['parent'],(language,index,saved,source)
        assert compact(saved['text'])==compact(source['text']),(language,index,saved,source)
    source_markers={}
    for index,item in enumerate(actual):
        for kind,number in item['sourceMarkers']:
            assert (kind,number) not in source_markers,(language,kind,number,'duplicated source marker')
            source_markers[(kind,number)]=index
    boundaries=[]
    for page in section['pages']:
        number=page['pdfPage']
        indexes=[index for index,item in enumerate(expected) if item['sourcePdfPage']==number]
        assert source_markers[('begin',str(number))]==indexes[0] and source_markers[('end',str(number))]==indexes[-1],(language,number,'source markers left their original actual item lines')
        first=expected[indexes[0]]
        boundaries.append({'sourcePdfPage':number,'firstItem':indexes[0],'depth':first['depth'],
                           'parent':expected[first['parent']]['text'] if first['parent'] is not None else None})
    assert len(source_markers)==2 * len(section['pages'])
    (WORK/f'index-{language}.ast.json').write_text(json.dumps(joined,ensure_ascii=False,indent=2),encoding='utf8')
    reports.append({'language':language,'entryCount':len(actual),'allDepthsParentsAndTextsVerified':True,
                    'allActualLineSourceMarkersVerified':True,'boundaries':boundaries})
(WORK/'ast-validation.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(reports,ensure_ascii=True))
