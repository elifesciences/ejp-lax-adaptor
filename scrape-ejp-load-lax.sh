#!/bin/bash
# wrapper around the conversion from article csv to json and into lax

set -e # everything must succeed

. ./install.sh

# scrape the report into json
cd /opt/ejp-lax-adaptor/
report="/opt/elife-reporting/paper_history$(date "+%Y_%m_%d").csv"
./.scrape-ejp.sh $report > /tmp/ejp-report.json

# import into lax
cd /srv/lax/
./load-ejp-json.sh /tmp/ejp-report.json --just-do-it
