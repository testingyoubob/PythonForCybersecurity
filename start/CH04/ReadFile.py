#!/usr/bin/env python3
# Sample script that reads from a file
# By 

# f = open("test.txt", "r")
# read = f.read()
# print(read)
# f.close()

# get the current file
import os 
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

#create the file path 

file_path = os.path.join(script_dir, "test.txt")
#open files for reading by using the 'r' 

f = open(file_path, "r")

#read contents to fhe file 
file_content = f.read()
print(file_content) 

f.close()   
