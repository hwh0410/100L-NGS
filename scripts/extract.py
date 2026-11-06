"""Rebuild derived data from the supplied FullTable workbooks. Read-only; requires openpyxl."""
import argparse, csv, json, math, hashlib
from pathlib import Path
import openpyxl

def extract(source, output):
    output.mkdir(parents=True, exist_ok=True)
    w = openpyxl.load_workbook(source / 'FullTable_abs_abun.xlsx', read_only=True, data_only=True)
    ranks = {}
    for s in w:
        s.reset_dimensions() # Vendor workbook dimensions incorrectly report A1.
        rows = list(s.values)
        records = [dict(zip(rows[0], row)) for row in rows[1:]]
        ranks[s.title] = records
    sample = 'An-100L-0929'
    total = sum(r[sample] for r in ranks['ASV'])
    assert total == 62557 and len(ranks['ASV']) == 521
    rel = openpyxl.load_workbook(source / 'FullTable_rel_abun.xlsx', read_only=True, data_only=True)
    max_error = 0
    for rank, records in ranks.items():
        assert sum(r[sample] for r in records) == total, rank
        s = rel[rank]; s.reset_dimensions(); rows = list(s.values)
        rr = [dict(zip(rows[0], row)) for row in rows[1:]]
        key = 'ID' if rank == 'ASV' else 'Processed_Taxonomy'
        lookup = {r[key]: r[sample] for r in rr}
        for r in records:
            max_error = max(max_error, abs(r[sample]/total - lookup[r[key]]))
        with (output / (rank.lower()+'.csv')).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(records[0])+['percent_total'])
            writer.writeheader()
            for r in records: writer.writerow({**r, 'percent_total': 100*r[sample]/total})
    assert max_error < 1e-10, max_error
    asvs = ranks['ASV']
    arch = sum(r[sample] for r in asvs if r['Domain']=='d__Archaea')
    summaries = {}
    for rank in ['Domain','Phylum','Class','Order','Family','Genus','Species']:
        groups = {}
        for r in asvs:
            name = r[rank]
            entry = groups.setdefault(name, {'name':name[3:], 'reads':0,'asvs':0, 'domain':r['Domain'][3:], 'phylum':r['Phylum'][3:], 'family':r['Family'][3:]})
            entry['reads'] += r[sample]; entry['asvs'] += 1
        summaries[rank] = sorted(groups.values(), key=lambda x:-x['reads'])
    p = [r[sample]/total for r in asvs]
    singles = sum(r[sample]==1 for r in asvs); doubles = sum(r[sample]==2 for r in asvs)
    audit = {'sample':sample,'total_reads':total,'input_pairs':72114,'retention_percent':100*total/72114,
       'asvs':len(asvs),'archaea_reads':arch,'archaea_percent':100*arch/total,
       'shannon_bits':-sum(x*math.log2(x) for x in p),'gini_simpson':1-sum(x*x for x in p),
       'chao1_bias_corrected':len(asvs)+singles*(singles-1)/(2*(doubles+1)),
       'unresolved_genus_reads':sum(r[sample] for r in asvs if 'UNCLASSIFIED' in r['Genus'] or 'Incertae_Sedis' in r['Genus']),
       'max_relative_table_error':max_error,
       'source_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [source/'FullTable_abs_abun.xlsx',source/'FullTable_rel_abun.xlsx']}}
    payload = {'audit':audit,'ranks':summaries}
    (output/'community.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    (output.parent/'data.js').write_text('window.NGS_DATA = '+json.dumps(payload, ensure_ascii=False)+';\n')
    (output/'audit.json').write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('source',type=Path); parser.add_argument('--output',type=Path,default=Path('data'))
    args=parser.parse_args(); extract(args.source,args.output)
