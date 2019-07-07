#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating accessing JSON data from URL and processing.
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#

import json
import ssl #For managing SSL certificate and ingnore errors


import urllib.request



def ParseJson(Data):
    print ("Parse")


def main():
    #Ignore Certificate validation error 
    ssl._create_default_https_context = ssl._create_unverified_context
    
    URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    URLOpen = urllib.request.urlopen(URL)
    UrlData = URLOpen.read()
    # Load data in to JSON Dictionary Object
    JSON = json.loads(UrlData)

    # Now have data in json format and need to process. There are 2 sections to it, Metadata which is list
    #  Features which is Array. Will have to Loop through Array to get data
    # First getting data from Metadata section. Using get function puts None value if object is missing. 
    # also get can be used to provide alternative value when missing object
    API = JSON.get('metadata').get('api', "Not_Found")
    Status = JSON.get('metadata').get('Wrong', "Not_Found") #Wrong object to demonstrate get function.
    print (API,"Status :", Status)
    
    # Now Loop through the Features Array
    for X in JSON["features"]:
        Mag = X.get("properties").get("mag")
        Place =  X.get("properties").get("place")
        print ("Magnitude :", Mag, "at place ", Place)

if __name__ == "__main__":
    main ()