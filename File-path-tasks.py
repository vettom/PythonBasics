#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Working with File path, test conditions etc
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#

import os
from os  import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print (" ------- This is Main Function ")

    # Print OS name
    print(os.name)
    # #  Check if item exists
    print ("Item exists : " + str(path.exists("testfile.txt")))
    # # check if it is file or directory
    # print ("It is file : " + str(path.isfile("testfile.txt")))
    # print ("It is DIr : " + str(path.isdir("testfile.txt")))

    # Get path
    print("Items path : " + str(path.realpath("testfile.txt")) )
    DD=str(path.realpath("testfile.txt"))
    print(DD)
    # # strip out path from filename
    # print("Path and Name : " + str(path.split(path.realpath("testfile.txt"))))


    # Get modification time
    # T = time.ctime(path.getmtime("testfile.txt"))
    # print (T)

    # print(datetime.datetime.fromtimestamp(path.getmtime("testfile.txt")))

    # Calculate how long it was modified.

    TD = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("testfile.txt"))

    print( str(TD) + " time since modified")
    print ("OR, " + str(TD.total_seconds()) + " Seconds")
if __name__ == "__main__":
    main ()