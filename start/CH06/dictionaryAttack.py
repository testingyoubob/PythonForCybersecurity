#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By mj 

import crypt 

def test_password(hashed_password, algorithm_salt, plaintext_password):
    #Using the provided alogorith/salt and Plaintext password, create a hash
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    #Compare hashed_Password with the just created hash 
    if hashed_password == crypted_password:
        return True
    return False

def read_dictionary(dictionary_file):
    #Open provided dictionary file 
    #and read contents into vaiable 
    f = open(dictionary_file, "r")
    message = f.read()  
    return message 

#Load dictionary file and prompt for hash and alogorithm/salt 
password_dictionary = read_dictionary("top10.text")
hashed_password = input("What is the hased password? ")
algorithm_salt = input("What is the algorithm and salt ")

#For each password in dictionary file, 
#test against hashed_password 
for password in password_dictionary.splitlines():
    result = test_password(hashed_password, algorithm_salt, password)
    if result:
        #if a mathc is found, print it and quit
        print("Match found: {0}".format(password))
        break 

    