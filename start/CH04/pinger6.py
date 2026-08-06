#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By mj

#import necessary models
import platform
import os
from datetime import datetime

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("pinger.log", "a")
    f.write(message)
    f.close()   

def ping_host(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        #Build our ping command for Windows 
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:   
        #Other OS's 
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
        #Execute command and capture exit code 
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    #Create empty list object 
    lines = []
    #Open file and read line-by-line 
    f = open("ips.txt", "r")
    for line in f:
        #Use strip() to remove spaces and carriage returns 
        line = line.strip() 
        lines.append(line)
    return lines

#read IPs from file 
write_log("ips.txt")
ip_addresses = import_addresses()
write_log("Import {0} IPs".format(len(ip_addresses)))

for ip in ip_addresses:
    #Call ping_host function and capture the return value 
    exit_code = ping_host(ip)   
    #Print results to console only if successful 
    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0}".format(ip))
    else:
        write_log("{0} is offline".format(ip))




