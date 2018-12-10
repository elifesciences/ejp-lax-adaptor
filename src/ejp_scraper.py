from datetime import datetime
from collections import OrderedDict
import csv, fileinput, json
from et3.extract import path as p
from et3.render import render

def todt(ymdstr):
    if not ymdstr.strip():
        return None
    return datetime.strptime(ymdstr, "%Y-%m-%d")

mapping = dict([
    ('RJI', 'Reject Initial Submission'),
    ('RJF', 'Reject Full Submission'),
    ('RVF', 'Revise Full Submission'),
    ('AF', 'Accept Full Submission'),
    ('EF', 'Encourage Full Submission'),
    ('SW', 'Simple Withdraw')
])
mapping_rev = {v:k for k, v in mapping.items()}
    
def tfield(val):
    val = str(val).strip()
    if not val:
        return None
    assert val in mapping.values(), "unknown decision type %r" % val
    return mapping_rev[val]

def paper_type(mstype):
    # these labels aren't actually used
    # the value is passed through so long as it exists in map
    types = { 
        'RA': 'Research article',
        'AV': 'Short report',
        'RR': 'Research advance',
        'SR': 'Registered report',
        'TR': 'Tools and resources',
        'RE': 'Research exchange', # deprecated in favour of SC
        'SC': 'Scientific Correspondence',
        'RS': 'Replication study',
        'RC': 'Research communication',
    }
    assert mstype in types.keys(), "unknown paper type %r" % mstype
    return mstype

DESCRIPTION = OrderedDict([
    ('manuscript_id', [p('ms'), int, str]), # yes, str->int->str, I know.

    ('ejp_type', [p('type'), paper_type]),
    
    ('date_initial_qc', [p('initial_qc_dt', None), todt]),
    ('date_initial_decision', [p('initial_decision_dt', None), todt]),
    ('initial_decision', [p('initial_decision', None), tfield]),
    
    ('date_full_qc', [p('full_qc_dt', None), todt]),
    ('date_full_decision', [p('full_decision_dt', None), todt]),
    ('decision', [p('full_decision', None), tfield]),

    ('date_rev1_qc', [p('rev1_qc_dt', None), todt]),
    ('date_rev1_decision', [p('rev1_decision_dt', None), todt]),
    ('rev1_decision', [p('rev1_decision', None), tfield]),

    ('date_rev2_qc', [p('rev2_qc_dt', None), todt]),
    ('date_rev2_decision', [p('rev2_decision_dt', None), todt]),
    ('rev2_decision', [p('rev2_decision', None), tfield]),

    ('date_rev3_qc', [p('rev3_qc_dt', None), todt]),
    ('date_rev3_decision', [p('rev3_decision_dt', None), todt]),
    ('rev3_decision', [p('rev3_decision', None), tfield]),

    ('date_rev4_qc', [p('rev4_qc_dt', None), todt]),
    ('date_rev4_decision', [p('rev4_decision_dt', None), todt]),
    ('rev4_decision', [p('rev4_decision', None), tfield]),
])

def scrape(fh):
    return render(DESCRIPTION, csv.DictReader(fh))

def customserializations(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type %r not serializable" % type(obj))

def main(fh):
    data = list(scrape(fh))
    return json.dumps(data, indent=4, default=customserializations)

if __name__ == '__main__':
    print(main(fileinput.input(mode='r')))
