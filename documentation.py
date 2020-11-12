#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : How to get documentation of functions and how to add for your functions.
# Author:       Denny Vettom
# Dependencies: Python3
#
import argparse

'''
Func() Trying some
Doc string can be added to each function and use __doc__ to pring the help

To add documentation to each function start with tripple quote and add test field. This field will be printed when __doc__ is called with function
No need to add function name, but always good to add.
Documentation of any python function can be retrieved using this method.


'''


def myFunc(Arg):
    ''' 
     myFunc()  -- > Help explaining this function
      Arg = First argument expected

    '''

# To print help for a function if it is included. 
# To add help, immediately after function start, add necessary help topic in 3 tics
print(myFunc.__doc__)

# Print help for argparse
print(argparse.__doc__)