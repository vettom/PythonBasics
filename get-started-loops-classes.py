#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Basic python operation like loops, conditions, classes etc.
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#
class myclass1():
    def method1(self):
        print("My class1 method1 ")

    def method2(self, someString):
        print ("Myclass1 method 2 " + someString)

class myclass2(myclass1):
    def method1(self):
        print("_________________")
        myclass1.method1(self)
        print("My class2 method1 ")

    def method2(self, someString):
        print ("Myclass2 method 2 " + someString)


def main():
    print ("Main Area print")
    c1 = myclass1()
    c1.method1()
    c1.method2("This is for Method2")
    c2 = myclass2()
    c2.method1()
    c2.method2("-----C2 Method2")

#FUNCTIONS

# def func1(ARG): 
#     print ("Func1 " + ARG )


# def func2(ARG1, ARG2):
#     # print("Func2") 
#     print(ARG1 , ARG2)
#     return ARG1 + ARG2

# def func_cube(X):   #Accepts value of x and return value 
#     return X*X*X

#Performing Power by setting a default value as well as over riding the value

# def power(num, x=3): #Definig default value for variable
#     result=1
#     for i in range(x):
#         result = result * num
#     return result


#Function accepting multiple arguments. Variable Arguments has to be the last.
# def multiadd(*args):
#     result=0
#     for x in args:
#         result = result + x
#     return result



#**** Conditional structure

x, y = 200, 20
if (x < y):
    result="X less than Y"
elif(x > y):
    result="X greater than Y"
else:
    result="X and Y are same"
print(result)

#Print conditional in single line
result="X is greate than y" if(x > y) else "Y greater tha X"
print(result)


# **** LOOPS

#While loop
# x=1
# while (x < 5):
#     print (x)
#     x= x+1

# For loop 
#Simple loop
# for x in range(1 ,6):
#     print (x)
#     x = x + 1

# Days = ["Mon", "Tue", "Wed"]
# for d in Days:
#     print(d)

# Use Break and continue
# for x in range(1 ,6):
#     if (x == 4): 
#         break
#     print (x)
#     x = x + 1


# Use continue to print odd numbers
# for x in range(1,9):
#     if (x % 2 != 0): 
#         continue
#     print (x)
#     x = x + 1

#Enumeate function used to get item numner. starts 0
# names = ["denny", "jenn", "freya", "maia"]
# for i,d in enumerate(names):
#     print (i,d)

if __name__ == "__main__":
    main ()

    # func1("argument")
    # print(func2)
    # func2(2, 4) # Pass 2 values to Func2 and prints what ever defined not the return value
    # print (func2(2, 4)) # Prints functions as well as the return value
    # print (func_cube(3))

#Printing powr Line 20
    # print(power(3))
    # print(power(x=2, num=3))  # Possible to over ride and specify in any order


#Passing variable numner of arguments 
# print(multiadd(2,4,5,1))


