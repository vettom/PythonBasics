#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating parsing of JSON. Here parsig json output by describe instance.
#  
# Author:       Denny Vettom
# Dependencies: PYTHON 3

    # Print Colored text on Terminal
def Err(Var): print("\033[1;41m \033[93m  {} \033[00m \n" .format(Var))  # Yellow on Red
def Warn(Var): print("\033[1;44m \033[93m  {} \033[00m \n" .format(Var)) # Yellow on Black
def Info(Var): print("\033[1;44m \033[32m  {} \033[00m \n" .format(Var)) # Green on Black
def R(Var): print("\033[1;31m{} \033[00m" .format(Var))
def Y(Var): print("\033[1;93m{} \033[00m" .format(Var))
def G(Var): print("\033[1;32m{} \033[00m" .format(Var))
def B(Var): print("\033[1;33m{} \033[00m" .format(Var))
def R1(Var): print("\033[1;41m  \033[97m{} \033[00m" .format(Var))
def G1(Var): print("\033[1;42m  \033[97m{} \033[00m" .format(Var))
def B1(Var): print("\033[1;44m  \033[97m{} \033[00m" .format(Var))
            
def main():
    # Here I have saved aws descrive_instances outut JSON. For complex tasks check Aws-Boto3 scripts
    Err("This is Error")

if __name__ == "__main__":
    main ()