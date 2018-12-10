#!/bin/bash
set -e # everything must succeed.
rm -rf venv/
if [ ! -e venv3/bin/activate ]; then
    rm -rf venv3/
    python -m venv venv3
fi
source venv3/bin/activate
pip install -r requirements.lock
