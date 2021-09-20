#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating Time formatting and tme calculation.
# Author:       Denny Vettom
# Dependencies: PYTHON 3

import time
from datetime import datetime


def main():
    # Record start time
    StartTime = time.time()
    print (" ------- This is Main Function ")
    now = datetime.now()
    # %y %Y - Year, %a/%A -Weekday, %b/%B - Month, %d - Day of month
    print(now.strftime("Today is : %a, %d, %B, %Y"))  # Today is : Sat, 05, January, 2019

    # %c - Locale's date and time, %x Local date, %X - Local time
    print(now.strftime("Local date and time : %c")) # Local date and time : Sat Jan  5 10:46:43 2019
    print(now.strftime("Local date : %x"))  #Local date : 01/05/19
    print(now.strftime("Local time : %X")) #  Local time : 10:46:43

#  Time Formatting : %I/%H -12/24 hour, %M - Minute, %S -Second, %p - Loals AM/PM
    print(now.strftime("Current time : %I:%M:%S %p")) # Current time : 10:46:43 AM
    print(now.strftime("Current time : %H:%M"))  # Current time : 10:46

    # Adding a sleep to delay
    print ("Sleeping 5 seconds")
    time.sleep(5)

    print ("Total time taken =", time.time() - StartTime)


if __name__ == "__main__":
    main ()
