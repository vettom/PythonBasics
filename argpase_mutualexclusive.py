#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : some advanced option like mutual exclusive, choices, Sub parse.
# 
# Author:       Denny Vettom
# Dependencies: PYTHON 3


'''
In this example explaining 2 use cases of mutually exclusive arguments option.
1. arg1 and 2 used for confirming particular action, does not accept arguments. If specified it returns true and with required option it is mandatory at least one of the provided
2. Here arga and B are required argument and only oneof it should be entered. Argument a ca  accept multiple values

Use case for 1 : When an action must be specified like list, update, delete etc
case 2 : when multiple ways of processing, like accept input as argument or filename or list etc. Only one will be valid at any time.

'''

import argparse

EPILOG = "example for §mutually_exclusive_group"
# Use argparse to accept and validate user input
# Description and additional text in epilog.
argparser = argparse.ArgumentParser(description='Text to display when -H option used for', prog='Parse', epilog=EPILOG)

# Create mutually exclusively group that returns True
group = argparser.add_mutually_exclusive_group(required=True)
# Arg1 and 2 are mutually exclusive and at least one must be provided. "Store_tru" stores Boolian
group.add_argument('--arg1', action="store_true", help='Exclusive argument group')
group.add_argument('--arg2', action="store_true", help='Exclusive argument group')


# Arga abd b are mutually exclusive and one of the much provided with a value.
groupa = argparser.add_mutually_exclusive_group(required=True)
groupa.add_argument('--arga', nargs='+', help='Exclusive argument group')
groupa.add_argument('--argb', help='Exclusive argument group')
# Working with Sub Parser
args = argparser.parse_args()


# Printing selection


print ("Arg1 = '{}', Arg2 = '{}' " .format(args.arg1, args.arg2))

print ("Arga = '{}', Argb = '{}' " .format(args.arga, args.argb))

# example ./argpase_mutualexclusive.py --arg2  --arga one two