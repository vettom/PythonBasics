#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : How to use Argparse to process user input
# 
# Author:       Denny Vettom
# Dependencies: PYTHON 3

import argparse


# Use argparse to accept and validate user input
# Below line description displayed when user run -h for help
argparser = argparse.ArgumentParser(description='Text to display when -H option used for', epilog='Text to display under help section')
# Below demonstration of optional smaller argumen. Also defining it as required value
argparser.add_argument('-a', '--action', help='Instance action to be performed list/status/', required=True)
# Below option acceps profile argument and if not provided defaults to value "default"
argparser.add_argument('--profile', default="default", help='If no profile provided, assumes default')
# Optional argument and no default. If not argument it will be set to None type. Note, variable is fined but value is None type.
argparser.add_argument('--region', help='Provide region as argument')
# Below argument accepts 1 or more inputs and stores in a list.
argparser.add_argument('--elb', nargs='+', help='Name/s of Aws ELB seperated by space')
# Positional argument that is compulsary if defined. Be careful if mix with nargs, positional must be before multi args.
argparser.add_argument('vpc', help="A positional argument if defined must be profided")



args = argparser.parse_args()
print("")
# Below variable check generally works, but in argparse case variable set to type None, so cannot be used
try: args.region
except: print ("region Not defined")

# Use if statement to check if Region is defined or not
if args.region is None:  # None is type NULl in Python not a value in variable.
    print("Regions is defined as None")
    # If required variable not defined, print help and exit.
    argparser.print_help()
    exit()

# Processing Variable examples
print ("Action is:", args.action, ":: Profile:", args.profile,":: Region is :", args.region, ":: VPC is:", args.vpc)

# Processing the list received for ELB
if args.elb is not None:
    for X in args.elb:
        print ("ELB:", X)

