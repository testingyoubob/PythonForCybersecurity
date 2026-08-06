#!/usr/bin/env python3
# Sample script that writes to a file
# By 

#Open file for writing - f is used. 
# firstName = input("What is your name ")
# f = open ("test.txt", "w")

# #write to file
# f.write(firstName + ", Nice to meet you")

# #close the files. 
# f.close()
# print("file closed")
# #Want to take a look inside before closing for good
# f = open("test.txt", "r")
# print(f.read())
# f.close()
def readFile():
    print("What you wrote.")
    test = open("testfile.txt", "r")
    print(test.read())
    test.close()
    print("file closed")


#open the file    
test_file = open("testfile.txt", "w")

#Write lines to the file
test_file.write("Hello Bob\n")
test_file.write("My Name is Ed\n")
test_file.write("I like turtles\n")

#close the file
test_file.close()
readFile()

