#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose :  Using subparse to accept optional argument and have its own custom arguments
# 
# Author:       Denny Vettom
# Dependencies: PYTHON 3

import argparse

EPILOG = "Positional argument is required, run argument -h for help with positional argument"

P = argparse.ArgumentParser(description='Text to display when -H option used for', prog='Parse', epilog=EPILOG)
P.add_argument('--option', help="Optional common argument.")
Psub = P.add_subparsers()

Arg1 = Psub.add_parser("status")
Arg1.add_argument('--object1', required=True, help='Must provide object1')
Arg1.add_argument('--option1', help='Optional Argument')


Arg2 = Psub.add_parser("list")
Arg2.add_argument('--object2', required=True, help='Must provide object2')
Arg2.add_argument('--option2', help='Optional Argument')

args = P.parse_args()

# Below line to test for Optional argument and print help
try: status | List
except: P.print_help()