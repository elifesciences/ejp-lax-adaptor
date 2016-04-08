from collections import OrderedDict
import sys,csv,fileinput,json
import logging

LOG = logging.getLogger(__name__)

def csv_report():
    for row in csv.DictReader(fileinput.input(mode='rb'), delimiter=','):
        yield row

DESCRIPTION = [
    ('article', {
        'iterable': csv_report,
        'attrs': OrderedDict([
            ('manuscript_id', 'this.ms'),
            
            ('date_initial_qc', 'this.initial_qc_dt'),
            ('date_initial_decision', 'this.initial_decision_dt'),
            ('initial_decision', 'this.initial_decision'),
            
            ('date_full_qc', 'this.full_qc_dt'),
            ('date_full_decision', 'this.full_decision_dt'),
            ('decision', 'this.full_decision'),

            ('date_rev1_qc', 'this.rev1_qc_dt'),
            ('date_rev1_decision', 'this.rev1_decision_dt'),
            ('rev1_decision', 'this.rev1_decision'),

            ('date_rev2_qc', 'this.rev2_qc_dt'),
            ('date_rev2_decision', 'this.rev2_decision_dt'),
            ('rev2_decision', 'this.rev2_decision'),

            ('date_rev3_qc', 'this.rev3_qc_dt'),
            ('date_rev3_decision', 'this.rev3_decision_dt'),
            ('rev3_decision', 'this.rev3_decision_dt'),

            ('date_rev4_qc', 'this.rev4_qc_dt'),
            ('date_rev4_decision', 'this.rev4_decision_dt'),
            ('rev4_decision', 'this.rev4_decision_dt')
        ])
    }),
]

def scrape():
    import scraper
    using_me = __import__(__name__)
    return scraper.scrape(using_me)

if __name__ == '__main__':
    print json.dumps(scrape(), indent=4)
