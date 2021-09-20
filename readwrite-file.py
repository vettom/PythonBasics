#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating  different actions while reading file including filtering column
# Author:       Denny Vettom
# Dependencies: PYTHON 3


def main():
	print (" ------- This is Main Function ")

	# Open a file for writing and create it if it does not exists
	# F = open("testfile.txt", "w+")  # + sign will create file if not exist
	# Apend data to file
	# F = open("testfile.txt", "a")  # Apend
	# Read data in file
	F = open("testfile.txt", "r")  # Open file in read mode
	# # Write some lines
	# for i in range(10):
	# 	F.write("This is line No: " + str(i) + "\r\n")
    
    #Read entire file
	# if F.mode == 'r':
	# 	CONTENT=F.read()
	# 	print(CONTENT)
	# Close file once done

	# Read content line by line
	LINES = F.readlines()
	for X in LINES:
		print(X) #Print entire line
		Var = X.split() #Split line so can filter column
		NUM = Var[3] #Get 3rd Column
		Count = Var[4]
		print (NUM, Count)
	F.close()
if __name__ == "__main__":
	main ()