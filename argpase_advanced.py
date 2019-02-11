#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : some advanced option like mutual exclusive, choices, Sub parse.
# 
# Author:       Denny Vettom
# Dependencies: PYTHON 3

import argparse

EPILOG = "This is text displayed at botom of -h result"
# Use argparse to accept and validate user input
# Description and additional text in epilog.
argparser = argparse.ArgumentParser(description='Text to display when -H option used for', prog='Parse', epilog=EPILOG)
# Below define positioal arguments and acceptable values
argparser.add_argument('action', choices=['list', 'status'], help='Instance action to be performed list/status/')
# Create mutually exclusively group
group = argparser.add_mutually_exclusive_group()
# Arg1 and 2 are mutually exclusive
group.add_argument('--arg1', action="store_true", help='Exclusive argument group')
group.add_argument('--arg2', action="store_true", help='Exclusive argument group')

# Working with Sub Parser
subparser = argparser.add_subparsers()
parser_A = subparser.add_parser("clone")
parser_A.add_argument("--host", action="store_true", help='Additional Arg X')

args = argparser.parse_args()

