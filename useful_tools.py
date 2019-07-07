#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Some basic utilities and use cases
# Author:       Denny Vettom
# Dependencies: PYTHON -3
#
# ----------------------------------------------------------------------------
# Name          Date            Comment                         Version
# ----------------------------------------------------------------------------
# DV            20/12/2018     Initial Version                  V 1.0
import webbrowser   #Help open a Web page in your default Browser
import random        #To generate some random data

def main():

""" Web Browser Module """
    # Simply open the UEL in Browser
    # webbrowser.open("https://www.adobe.com/")

    # Using Random method to get a random value
    # N = random.uniform(1,10)  #Random floating point numbers

""" Starting the random Module """
    N = random.randint(1,10)  #More useful as it will be intiger 
    print ("Num:", N)

    # Next is to select a randon sring from list
    Mesg = ['Hi', 'Morning', 'Evening', 'Howdy', 'Hiya']
    X = random.choice(Mesg)
    print (X, " Vettom")

    #Below option to create a list of Random value 
    Color = ['Red','Blue','Green','Yellow']
    Y = random.choices(Color,k=10)
    print(Y)

    #Shuffle value in the list itself
    random.shuffle(Color)
    print (Color)

    #Select random 2, but uniq
    Z = random.sample(Color, k=2)
    print (Z)

""" """
if __name__ == "__main__":
    main()
