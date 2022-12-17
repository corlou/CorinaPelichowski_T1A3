#!/bin/bash
pip install -r requirements.txt | grep -v 'already satisfied'
python3 main.py