#!/usr/bin/env bash
set -e

echo $'\nConfiguring virtual environment...'
python3 -m venv .venv > /dev/null
.venv/bin/python -m pip install --upgrade pip > /dev/null
.venv/bin/python -m pip install -r requirements.txt > /dev/null

exec .venv/bin/python main.py