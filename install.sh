#!/bin/bash
set -e # everything must succeed.
. mkvenv.sh
source venv/bin/activate
pip install -r requirements.lock
