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
# Below defining Subparse with dest allow specifying action based on task selected.
Psub = P.add_subparsers(title="Required arguments", dest="Task")

# Defining positional arguments
# Note: You can use any name to define sub parse. I define based on command to make it clearer for arguments. for eg you can use ARG for all if you want.
Status = Psub.add_parser("status")
Status.add_argument('--object1', required=True, help='Must provide object1')
Status.add_argument('--option1', help='Optional Argument')


List = Psub.add_parser("list")
List.add_argument('--object2', required=True, help='Must provide object2')
List.add_argument('--option2', help='Optional Argument')

args = P.parse_args()

# Below line to test for Optional argument and print help
try: status | List
except: P.print_help()

# For defining action based of input. When defining Sub, dest is defined which can be used to identify argument value
if args.Task == 'status':
    print("Status selected")
elif args.Task == 'list':
    print("List selected")