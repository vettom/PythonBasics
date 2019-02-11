#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Simple error handling methods.
# 
# Author:       Denny Vettom
# Dependencies: PYTHON 3


def main():
    # Use try block for simple error check and message if failed
    print ("Section 1. Print error if any statement in try section fails")
    print("--------------------------")
    try:
        print(VAR) #Will fail as VAR not defined.
    except:
        print ("Failed to complete all tasks")

    
    print ("\nSection 2. Handling based on error message")
    print("--------------------------")

    try:
        print(VAR) #Will fail as VAR not defined.
    except NameError:
        print ("Variable Variable not defined")
    except:
        print ("Error for all other errors")

    """
    Below section most useful as there can be multiple errors in try section, this will print out which exception cause the failure without printing detailed information.
    """
    print ("\nSection 3. Print first faied error exception only")
    print("--------------------------")

    try:
        C = "Something"
        # print(VAR) #Will fail as VAR not defined.
        f = open('test.txt') #This will fail, but above command failure will result in exception before this
    except Exception as ERR:
        print (ERR)

    # Below example is testing a condition and creating own exception. You can pass raise any exception you like for th except to handle    
    print ("\nSection 4. Creating own exception")
    print("--------------------------")
    try:
        X = "Test"
        if X is "Test":
            raise Exception   #Can define what type of exception to raise.
    except:
        print ("Exception raised")

if __name__ == "__main__":
    main ()