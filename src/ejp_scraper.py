from datetime import datetime
from collections import OrderedDict
import sys,csv,fileinput,json
import logging
from scraper.utils import fattrs

LOG = logging.getLogger(__name__)

def csv_report():
    for row in csv.DictReader(fileinput.input(mode='rb'), delimiter=','):
        yield row

def todt(ymdstr):
    if not ymdstr.strip():
        return None
    return datetime.strptime(ymdstr, "%Y-%m-%d")

@fattrs('this as row')
def debug(row):
    print 'debug:',row

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

@fattrs('this.type as mstype')
def paper_type(mstype):
    types = { 
        'RA': 'Research article',
        'SR': 'Registered report',
        'AV': 'Short report',
        'RR': 'Research advance',
        'TR': 'Replication study',
        'RS': 'Tools and resources',
    }
    assert mstype in types.keys(), "unknown paper type %r" % mstype
    return mstype

@fattrs('this.ms as msid')
def msid(msid):
    int(msid)
    return msid

DESCRIPTION = [
    ('article', {
        'iterable': csv_report,
        'attrs': OrderedDict([
            #('debug', 'debug'),
        
            ('manuscript_id', 'msid'),

            ('ejp_type', 'paper_type'),
            
            ('date_initial_qc', ('this.initial_qc_dt', None, todt)),
            ('date_initial_decision', ('this.initial_decision_dt', None, todt)),
            ('initial_decision', ('this.initial_decision', None, tfield)),
            
            ('date_full_qc', ('this.full_qc_dt', None, todt)),
            ('date_full_decision', ('this.full_decision_dt', None, todt)),
            ('decision', ('this.full_decision', None, tfield)),

            ('date_rev1_qc', ('this.rev1_qc_dt', None, todt)),
            ('date_rev1_decision', ('this.rev1_decision_dt', None, todt)),
            ('rev1_decision', ('this.rev1_decision', None, tfield)),

            ('date_rev2_qc', ('this.rev2_qc_dt', None, todt)),
            ('date_rev2_decision', ('this.rev2_decision_dt', None, todt)),
            ('rev2_decision', ('this.rev2_decision', None, tfield)),

            ('date_rev3_qc', ('this.rev3_qc_dt', None, todt)),
            ('date_rev3_decision', ('this.rev3_decision_dt', None, todt)),
            ('rev3_decision', ('this.rev3_decision', None, tfield)),

            ('date_rev4_qc', ('this.rev4_qc_dt', None, todt)),
            ('date_rev4_decision', ('this.rev4_decision_dt', None, todt)),
            ('rev4_decision', ('this.rev4_decision', None, tfield)),
        ])
    }),
]

def scrape():
    import scraper
    using_me = __import__(__name__)
    return scraper.scrape(using_me)

def customserializations(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type %r not serializable" % type(obj))

if __name__ == '__main__':
    print json.dumps(scrape()[0]['article'], indent=4, default=customserializations)
