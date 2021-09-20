#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Common tasks with Dictionary
# Author:       Denny Vettom
# Dependencies: PYTHON 3

D1 = [{
    'name': 'John',
    'age': 20
}, {
    'name': 'Bob',
    'age': 15
}, {
    'name': 'Charles',
    'age': 30
}]


# Sort Dictionary by key value Name
Out1 = sorted(D1, key=lambda k: k['name'])
Out2 = sorted(D1, key=lambda k: k['age'])
print(Out1)
print(Out2)

# Reverse order
Out3 = sorted(D1, key=lambda k: k['name'], reverse=True)
print(Out3)

# Creating a list of disctionaries
List=[]

X = {
    "Name" : "John",
    "Age" : 24
}
List.append(X)
X = {
    "Name" : "Tom",
    "Age" : 55
}
List.append(X) 
print(List)