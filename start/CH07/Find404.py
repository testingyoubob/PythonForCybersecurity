#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By 

log_file = input("Which file to analyze")

#open the file 
f = open(log_file, "r")

while True:
    line = f.readline()
    if not line:
        break
    if "404" in line:
        print(line.strip())
f.close()

