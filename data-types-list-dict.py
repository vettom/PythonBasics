#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Pythin data types and processing. Lists, Tuple, Dictionary
# Author:       Denny Vettom
# Dependencies: PYTHON 3

LIST = [ 1,2,3,4 ]  #Lists are represented in []. Values can be added, removed or change

TUPLE = (1,2,3,4)   # Like a list represented in (). Values in Tuple cannot be changed

DICT = { 'A': 1, 'B': 2, 'C': 'Cat'}  # Set of key value created with {} This is unordered. 

SET = { 1, 2, 5, 5}   # Is collection of unordered list of unique values


# Working with List

X = ['Cat', 'Dog', 'Pig', 'Cow', 'Sheep', 'Duck','Dove']

# Pring 2nd Item. Index starts at 0, so item index is 1
print(f'Second Item = {X[1]}')
# Print elementes from 1-3
print(f'Second Items 1 to 3 = {X[1:4]}')
# Print elements 0-5 with interval of 2
print(f'Print Interval(step) of 2 = {X[0:7:2]}')

print('----------------')
# Get index of an item by matchin
I = X.index('Pig')
print(f'Index ID for Pig is {I}')
print('Index ID for Dog is {}' .format(X.index('Dog')))

# Adding/Append item to end
X.append('Eagle')
# Adding item to sepcific index
X.insert(2,'Puppy')
print(f'X is :{X}')
# Remove Duck
X.remove('Duck')
# Remove Item from End of list and assign
Y = X.pop()
Y = X.pop(2)
print (Y)
# Remove item 3-5
del X[2:6]
print (f'X after removal {X}')

print('----------------')

# Print Length 
print (f'Length is : {len(X)}')