#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating parsing of JSON. Here parsig json output by describe instance.
#  For more detailed AWS scripts check https://github.com/vettom/Aws-Boto3
# Author:       Denny Vettom
# Dependencies: PYTHON 3
import json
import urllib
import urllib.request

def processjson(data):
    TheJSON = json.loads(data) 
    for X in TheJSON["Reservations"]:
        for Y in X["Instances"]:
            IP= Y.get("PublicIpAddress")
            VPC=Y.get("VpcId")

            # Some data can be key:Value pair. Loop trough and get value for matching Key
            for T in Y["Tags"]:
                if T["Key"] == 'Name':
                    HOST = T['Value']

            print (IP, VPC, HOST)

            
def main():
    # Here I have saved aws descrive_instances outut JSON. For complex tasks check Aws-Boto3 scripts
    URL = "http://localhost/json/eu-west-2.json"
    UrlDataOpen = urllib.request.urlopen(URL)
    UrlData = UrlDataOpen.read()

    processjson(UrlData)


if __name__ == "__main__":
    main ()