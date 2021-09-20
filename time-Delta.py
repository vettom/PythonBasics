#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating working with time delta.
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
import datetime
import time


def main():
    # Starttime = time.strftime('%Y-%m-%dT%H:%M:%S %Z')   
    # VAR = "Some information"
    # print (Starttime, VAR + " This is comment" + VAR)
    # print (" ------- This is Main Function ")

    # Basic time delta print
    # print(timedelta(days=365, hours=5, minutes=12))

    # # Print todays date
    Yday = '2020-04-05 10:58:49.281262'
    now = datetime.datetime.now()
    print("Today is :" + str(now))

    Diff = datetime.datetime.strptime(now) - datetime.datetime.strptime(Yday)
    print (Diff)

    # Print todays date year from now
    # print("Year Today=" + str(now + timedelta(days=365)))

    # Create time data to use more than one argument
    # print ("In 2 days and 5 Weeks it will be : " +
    #     str(now + timedelta(days=2, weeks=5)))

    # Time in the past
    # print("Last week this time : "
    #     + str(now - timedelta(days=3, weeks=5)))

    # Time in past with formatting
    # Otime=datetime.now() - timedelta(days=3)
    # Ftime=Otime.strftime("%A %B %d, %Y")
    # print("Time in past : " + Ftime)

# How many days until specific date
    Today = date.today()
    Xday = date(Today.year, 12, 25)  # Sets this year and date
    # print (Today.day, Today.month)
    # print date(Today.year, 1, Today.month)
    # Use comparission to see it it has already passed this years date
    if (Xday < Today):
        print("Date passed %d days ago" % ((Today - Xday).days))
        # Now to find next years date, set year as next
        Xday = Xday.replace(year=Today.year + 1)

        # Now calculate the number of dates
    TimetoXmas = Xday - Today
    print ("Next Xmas is ", TimetoXmas.days, " days")


if __name__ == "__main__":
    main()
