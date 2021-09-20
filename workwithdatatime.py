#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Basic Data and time tasks.
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    print (" ------- This is Main Function ")
#Printing Date and time
    today = date.today()
    print ("Date is " + str(today))
    print (date.today())
    print (today.day, today.month, today.year)

#WOrking with time
    print (datetime.now())
    print (datetime.time(datetime.now()))
    

if __name__ == "__main__":
    main ()