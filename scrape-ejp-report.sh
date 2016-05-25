#!/bin/bash
set -e
source install.sh 2&> /dev/null
python ./src/ejp_scraper.py "$@"
