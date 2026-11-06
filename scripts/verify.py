"""Check data integrity, headline calculations and local page assets."""
import csv,json,math
from pathlib import Path
from html.parser import HTMLParser
root=Path(__file__).resolve().parent.parent
d=json.loads((root/'data/community.json').read_text()); a=d['audit']; ranks=d['ranks']
assert a['total_reads']==62557 and a['asvs']==521
for k,rows in ranks.items():
    assert sum(r['reads'] for r in rows)==62557,k
    assert sum(r['asvs'] for r in rows)==521,k
with (root/'data/asv.csv').open(encoding='utf-8-sig',newline='') as f:asvs=list(csv.DictReader(f))
n=[int(r['An-100L-0929']) for r in asvs]; total=sum(n)
assert total==62557 and len(n)==521
assert abs(-sum(x/total*math.log2(x/total) for x in n)-a['shannon_bits'])<1e-12
arch=[r for r in ranks['Genus'] if r['domain']=='Archaea']
assert sum(r['reads'] for r in arch)==2108
assert next(r for r in arch if r['name']=='Methanosarcina')['reads']==1603
assert round(1603/2108*100,2)==76.04
assert round(6678/62557*100,2)==10.68
assert round(20528/62557*100,2)==32.81
class Links(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.links=[]
    def handle_starttag(self,tag,attrs):
        at=dict(attrs)
        if 'id' in at:assert at['id'] not in self.ids;self.ids.add(at['id'])
        for k in ('href','src'):
            if k in at:self.links.append(at[k])
s=Links(); s.feed((root/'index.html').read_text())
for link in s.links:
    if link.startswith('#'):assert link[1:] in s.ids,link
    elif not link.startswith('https://'):assert (root/link).is_file(),link
assert '<!--REPORT-->' not in (root/'index.html').read_text()
assert (root/'index.html').read_text().count('class="report-section"')==10
print('PASS: source totals, ASV diversity, headline ratios, all local assets and report sections.')
