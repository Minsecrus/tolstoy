from pathlib import Path
import hashlib, html, json, re, sys
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2:
    raise SystemExit('用法：python scripts/import-qiu-miaojin.py <PDF路径>')
pdf_path = Path(sys.argv[1])
source_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
assert source_hash == '74ff48648d5610a8a12cddf9b8dc66c0e32f06c1fd6e1d922df2ed78e729af46', '来源 PDF 校验值与所用版本不符'
doc = pymupdf.open(pdf_path)
assert len(doc) == 400, '来源 PDF 页数与所用版本不符'

crocodile = [(12,'第一手记'),(37,'第二手记'),(62,'第三手记'),(84,'第四手记'),(104,'第五手记'),(128,'第六手记'),(152,'第七手记'),(178,'第八手记')]
letters = [(244,'见证','见证（开篇）'),(247,'第一书','第一书'),(252,'第二书','第二书'),(255,'第三书','第三书'),(265,'第四书','第四书'),(267,'第六书','第六书'),(273,'第七书','第七书'),(281,'第八书','第八书'),(286,'第九书','第九书'),(295,'第十书','第十书'),(303,'第十七书','第十七书（五月十八日）'),(306,'第五书','第五书'),(312,'第十一书','第十一书'),(321,'第十二书','第十二书'),(327,'第十三书','第十三书'),(334,'第十四书','第十四书'),(338,'第十五书','第十五书'),(342,'第十六书','第十六书'),(351,'第十七书','第十七书（六月十一日）'),(355,'第十八书','第十八书'),(356,'第十九书','第十九书'),(370,'第二十书','第二十书'),(375,'见证','见证（结尾）')]

def lines_on(page_no):
    lines = []
    for block in doc[page_no - 1].get_text('dict')['blocks']:
        if block['type'] != 0:
            continue
        for line in block['lines']:
            s = ''.join(span['text'] for span in line['spans']).strip()
            if s:
                lines.append((s, *line['bbox']))
    return lines

def safe(s):
    return html.escape(s, quote=False).replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')

def join_line(a, b):
    # A wrapped Latin phrase needs its word separator; Chinese wraps without one.
    return a + (' ' if re.search(r'[A-Za-z]$', a) and re.match(r'[A-Za-z]', b) else '') + b

def prose(start, end, title, numbers=False):
    result, current = [], ''
    prev = None
    def flush():
        nonlocal current
        if current:
            result.append(safe(current))
            current = ''
    for page_no in range(start, end + 1):
        for j, (s,x,y,right,bottom) in enumerate(lines_on(page_no)):
            if page_no == start and j == 0:
                assert s == title, (page_no,s,title)
                continue
            if numbers and re.fullmatch(r'\d+', s) and x > 450:
                flush(); result.append('## ' + s); prev = None; continue
            if s == '* * *':
                flush(); result.append('---'); prev = None; continue
            if not current:
                current = s
            else:
                # Text is usually indented 30 points on the first line. Embedded
                # quotations can have a different left margin, so compare the
                # preceding line as well as its right edge and vertical gap.
                px, py, pr, pb, pp = prev
                same_page = pp == page_no
                new_paragraph = ((x > px + 18 and x < 250) or
                                 (same_page and y - py > 31) or
                                 (pr < 510 and x >= px - 2))
                if new_paragraph:
                    flush(); current = s
                else:
                    current = join_line(current, s)
            prev = (x,y,right,bottom,page_no)
    flush()
    return '\n\n'.join(result)

def preliminaries():
    # Dedication and two epigraphs are part of the work, not publisher matter.
    p = [x[0] for x in lines_on(241)]
    assert len(p)==5
    q = [x[0] for x in lines_on(242)]
    assert len(q)==19
    french = ' '.join(q[:10]).replace(' —— ', ' —— ')
    chinese = ''.join(q[11:18])
    return '\n\n'.join([safe(''.join(p[:3])), safe(''.join(p[3:])), safe(french), safe(q[10]), safe(chinese), safe(q[18])])

def final_witness():
    seq = [x[0] for p in (375,376) for x in lines_on(p)]
    assert seq[0] == '见证'
    return '  \n'.join(safe(s) for s in seq[1:])

volumes = [(96,'鳄鱼手记',[(a, (crocodile[i+1][0]-1 if i+1 < len(crocodile) else 207),t,t) for i,(a,t) in enumerate(crocodile)]),
           (97,'蒙马特遗书',[(241,242,'献词','献词')] + [(a, (letters[i+1][0]-1 if i+1 < len(letters) else 376),t,label) for i,(a,t,label) in enumerate(letters)])]
sidebars=[]; catalog=[]; characters=0
for vol,book,chapters in volumes:
    directory=ROOT / f'docs/library/volume-{vol}'
    directory.mkdir(parents=True,exist_ok=True)
    pages=[]
    for i,(start,end,title,label) in enumerate(chapters,1):
        if start==241: body=preliminaries()
        elif start==375: body=final_witness()
        else: body=prose(start,end,title,numbers=(vol==96))
        assert body.strip()
        characters += len(re.sub(r'\s','',html.unescape(body)))
        link=f'/library/volume-{vol}/chapter-{i:03}'
        content='\n'.join(['---',f'title: {json.dumps(title,ensure_ascii=False)}',f'description: {json.dumps(book+" · "+label,ensure_ascii=False)}','---','',f'<p class="reading-meta"><a href="/library/volume-{vol}/">{book}</a></p>','',f'# {title}','','',body,''])
        (directory/f'chapter-{i:03}.md').write_text(content,encoding='utf-8',newline='\n')
        pages.append({'text':label,'link':link})
    index=['---',f'title: {json.dumps(book,ensure_ascii=False)}',f'description: {json.dumps("邱妙津作品",ensure_ascii=False)}','---','',f'# {book}','','邱妙津 著。','',f'[开始阅读 →]({pages[0]["link"]})','','## 目录','']
    index += [f'- [{p["text"]}]({p["link"]})' for p in pages]
    (directory/'index.md').write_text('\n'.join(index)+'\n',encoding='utf-8',newline='\n')
    sidebars.append({'text':book,'collapsed':True,'items':[{'text':'本卷首页','link':f'/library/volume-{vol}/'}]+pages})
    catalog.append({'title':book,'fullTitle':book,'volumeLabel':'新增卷','author':'邱妙津','link':f'/library/volume-{vol}/','firstPage':pages[0]['link'],'pageCount':len(pages)})
stats={'volumeCount':2,'pageCount':sum(x['pageCount'] for x in catalog),'characterCount':characters}
module='// Generated by scripts/import-qiu-miaojin.py.\n'
for name,value in [('qiuMiaojinLibrarySidebar',sidebars),('qiuMiaojinLibraryCatalog',catalog),('qiuMiaojinLibraryStats',stats)]:
    module += 'export const '+name+' = '+json.dumps(value,ensure_ascii=False,indent=2)+'\n\n'
(ROOT/'docs/.vitepress/library.qiu-miaojin.mjs').write_text(module,encoding='utf-8',newline='\n')
print('SHA-256:',source_hash)
print('生成',stats)
