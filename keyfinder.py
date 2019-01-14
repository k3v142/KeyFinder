#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os.path
import argparse


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('-k', '--key', help='Key to find', type=str)
parser.add_argument('-i', '--input', help='Input file')
parser.add_argument('-o', '--output', help='Output file (optional)')

description = r"""
 _   __          ______ _           _
| | / /          |  ___(_)         | |
| |/ /  ___ _   _| |_   _ _ __   __| | ___ _ __
|    \ / _ \ | | |  _| | | '_ \ / _` |/ _ \ '__|
| |\  \  __/ |_| | |   | | | | | (_| |  __/ |
\_| \_/\___|\__, \_|   |_|_| |_|\__,_|\___|_|
             __/ |
            |___/

Tool to find every value in JSON file by key
https://github.com/k3v142/KeyFinder
-------------------------------------------------------------------------------
"""
print(description)
args = parser.parse_args()

KEY = args.key
INPUT = args.input
OUTPUT = args.output

if KEY is None:
    raise ValueError("No key given")
if INPUT is None:
    raise ValueError("No input given")
if OUTPUT is not None:
    sys.stdout = open(OUTPUT, 'w')

def get_values(key, d):
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(d[key], dict):
                get_values(key, d[key])
            elif key == KEY:
                print(d[KEY])
    elif isinstance(d, list):
        for item in d:
            get_values(key, item)

if os.path.isfile(INPUT):
    with open(INPUT, 'r') as f:
        try:
            d = json.load(f)
        except Exception as e:
            print('Bad JSON file. {}'.format(str(e)))
            exit(1)
    get_values(KEY, d)
