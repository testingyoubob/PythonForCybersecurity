#!/usr/bin/env python3
# Script that hashes a password
# By #!/usr/bin/env python3
# Script that hashes a password with provided salt
# By mj THIS is the Windows and Linux Version 

# #Imported Python Modules (This only works on Linux)
# import crypt 

# #Prompt user for plain-text password 
# plain_pass = input("What is the password? ")

# #print out hash 

# print("MD5  :{0}".format(crypt.crypt(plain_pass, "$1$")))
# print("Blowfish  :{0}".format(crypt.crypt(plain_pass, "$2a$")))
# print("eksblowfish  :{0}".format(crypt.crypt(plain_pass, "$2y$")))
# print("SHA-256  :{0}".format(crypt.crypt(plain_pass, "$5$")))
# print("SHA-512  :{0}".format(crypt.crypt(plain_pass, "$6$")))

from passlib.hash import md5_crypt, bcrypt, sha256_crypt, sha512_crypt

# Prompt user for plain-text password 
plain_pass = input("What is the password? ")

# print out hash 

print("MD5  :{0}".format(md5_crypt.hash(plain_pass)))
print("Blowfish  :{0}".format(bcrypt.hash(plain_pass)))
print("eksblowfish  :{0}".format(bcrypt.hash(plain_pass)))
print("SHA-256  :{0}".format(sha256_crypt.hash(plain_pass)))
print("SHA-512  :{0}".format(sha512_crypt.hash(plain_pass)))
