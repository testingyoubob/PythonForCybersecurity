#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most frequent users
# By 
import re

log_file = input("Which file to analyze? ")

#open file
with open(log_file, "r") as f:
    sample_logs = f.readlines()

    #Setup regex pattern and empty dictionary 
    client_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
    clientdict = {}

    for line in sample_logs:
        m = re.match(client_pattern,line)
        if m:
            client = m.group()
            #put access frequency in dictionary 
            if client in clientdict.keys():
                clientdict[client] += 1
            else:
                clientdict[client] = 1


for w in sorted(clientdict, key=clientdict.get, reverse=False):
    print(w, clientdict[w])
    