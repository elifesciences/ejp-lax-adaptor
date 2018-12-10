#!/bin/bash
./install.sh
source venv3/bin/activate
PYTHONPATH=src pytest -vv
