#!/bin/bash
./install.sh
source venv/bin/activate
PYTHONPATH=src pytest -vv
