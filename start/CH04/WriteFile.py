#!/usr/bin/env python3
# Sample script that writes to a file
# By 

#Open file for writing - f is used. 
firstName = input("What is your name ")
f = open ("test.txt", "w")

#write to file
f.write(firstName + ", Nice to meet you")

#close the files. 
f.close()
print("file closed")
#Want to take a look inside before closing for good
f = open("test.txt", "r")
print(f.read())
f.close()
