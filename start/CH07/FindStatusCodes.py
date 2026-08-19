#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By 
import re 

#prompt for file to analyze 

log_file = input("What's the file to analyze ")
#open file

with open(log_file, "r") as f:
    sample_logs = f.readlines()

status_pattern = r'\s(\d{3})\s'
statusdict = {}

#find match and store in dictionary 
for line in sample_logs:
    #search for pattern, and if found move forward 
    m = re.search(status_pattern, line)
    if m:
        client = m.group()
        #Put access frequency in dictionary 
        if client in statusdict.keys():
            statusdict[client] += 1
        else:
            statusdict[client] = 1

        #Sort by most frequently accessed 
for w in sorted(statusdict, key=statusdict.get, reverse=False):
    print(w, statusdict[w])

