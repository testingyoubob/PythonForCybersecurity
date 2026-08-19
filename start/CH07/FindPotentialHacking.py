#!/usr/bin/env python3
# Script that scans web server logs for possible hacking
# Use RegEx to find and report on common hacking types
# Based on https://www.cgisecurity.com/fingerprinting-port80-attacks-a-look-into-web-server-and-web-application-attack-signatures-part-two.html
# By 
#Import 

import re 
#Prompt

log_file = input("What file to analyze ")

#Open 
with open(log_file, "r") as f:
    sample_logs = f.readlines()

#Setup regex patterns 
find_wildcard_uri_pattern=r'\"(\S+)\s(\S*\*\S*)\s*(\S+)\"'
find_backtick_uri_pattern=r'\"(\S+)\s(\S*`\S*)\s*(\S+)\"'
find_code_uri_pattern=r']\s\"(\S+)\s(\S*[\^\[\]#{}\"]\S*)\s*(\S+)\"'
find_css_uri_pattern=r']\s\"(\S+)\s(\S*[\(\)]\S*)\s*(\S+)\"'
find_foldertraversal_uri_pattern=r']\s\"(\S+)\s(\S*///\S*)\s*(\S+)\"'

for line in sample_logs:
    m = re.search(find_wildcard_uri_pattern, line)
    if m:
        print("Possible attack: Wildcard in URL")
        print("\t{0}".format(line.strip()))
    m = re.search(find_backtick_uri_pattern, line)
    if m:
        print("Possible attack: Backtick (`) in URI")
        print(f"\t{line.strip()}")

    m = re.search(find_code_uri_pattern, line)
    if m:
        print("Possible attack: Code in URI")
        print(f"\t{line.strip()}")

    m = re.search(find_css_uri_pattern, line)
    if m:
        print("Possible attack: Potential CSS in URI")
        print(f"\t{line.strip()}")

    m = re.search(find_foldertraversal_uri_pattern, line)
    if m:
        print("Possible attack: Folder Traversal in URI")
        print(f"\t{line.strip()}")
    