#!/bin/bash
# wrapper around the conversion from article csv to json and into lax

set -e # everything must succeed

if [ ! -d /opt/elife-reporting/ ]; then
    # elife-reporting not installed, quit early
    exit 0
fi;

report="/opt/elife-reporting/paper_history$(date "+%Y_%m_%d").csv"
if [ ! -e "$report" ]; then
    echo "$report not found. cannot scrape it."
    exit 1
fi

cd /opt/ejp-lax-adaptor/

. ./install.sh

# scrape the report into json
python ./src/ejp_scraper.py $report > /tmp/ejp-report.json

# import into lax
cd /srv/lax/
./load-ejp-json.sh /tmp/ejp-report.json --just-do-it
