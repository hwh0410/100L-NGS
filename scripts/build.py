"""Render the reviewed Markdown report into dependency-free static HTML."""
from pathlib import Path
import html, re
root=Path(__file__).resolve().parent.parent
text=(root/'ANALYSIS.md').read_text()
def inline(s):
    s=html.escape(s)
    s=re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)',r'<a href="\2" target="_blank" rel="noopener noreferrer">\1 ↗</a>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return s
sections=[]
for block in text.split('\n## ')[1:]:
    title,body=block.split('\n',1)
    out=[];lines=body.strip().splitlines(); i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip(): i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip('|').split('|')]);i+=1
            head='<thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead>'
            table='<tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in rows[2:])+'</tbody>'
            out.append('<div class="table-wrap"><table>'+head+table+'</table></div>')
        else:
            para=[line];i+=1
            while i<len(lines) and lines[i].strip() and not lines[i].startswith('|'):
                para.append(lines[i]);i+=1
            out.append('<p>'+inline(' '.join(para))+'</p>')
    sections.append('<details class="report-section"><summary>'+inline(title)+'</summary><div class="report-body">'+''.join(out)+'</div></details>')
template=(root/'index.template.html').read_text()
(root/'index.html').write_text(template.replace('<!--REPORT-->','\n'.join(sections)))
print('Built',len(sections),'report sections')
