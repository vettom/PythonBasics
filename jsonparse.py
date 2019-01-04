#!/usr/bin/env python3
# Access JSON file from Web and process

import json
import certifi
import urllib.request



def ParseJson(Data):
    print ("Parse")


def main():
    # try:
        # Put the tasks in Try block to handle error
    # URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    # Urlopen = urllib.request.urlopen(URL)
    # Data = Urlopen.read(Urldata)
    # print (Data.getcode())
    # # except:
    # #     print ("ERROR : Failed to get data from URL")
    # #     exit()

    # # Call function to process Json format file and pass JSON as argument
    # ParseJson(Data)

    BBURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    URLOpen = urllib.request.urlopen(BBURL)
    URLRead = URLOpen.read()
    print (URLRead)

if __name__ == "__main__":
    main ()