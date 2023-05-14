#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install colr
python3 typethis.py
deactivate
