#!/bin/bash
# wrapper around the conversion from article csv to json and into lax

set -e # everything must succeed

if [ ! -d /opt/elife-reporting/ ]; then
    # elife-reporting not installed, quit early
    exit 0
fi;

. ./install.sh

# scrape the report into json
cd /opt/ejp-lax-adaptor/
report="/opt/elife-reporting/paper_history$(date "+%Y_%m_%d").csv"
python ./src/ejp_scraper.py $report > /tmp/ejp-report.json

# import into lax
cd /srv/lax/
./load-ejp-json.sh /tmp/ejp-report.json --just-do-it
