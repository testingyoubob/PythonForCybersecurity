#!/usr/bin/env python3
# Fourth example of pinging from Python
# By mj

import platform
import os 

def ping_host(ip):
    #Determine the current OS
    current_os = platform.system().lower()
    if current_os == "windows":
        #Build our ping command for Windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    #Build our command for other OS
    else:   
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    #Execute command and capture exit code 
    exit_code = os.system(ping_cmd)
    return exit_code

#Define the prefix to begin pinging 
ip_prefix = "192.168.0."

#loop from 0 - 254
for final_octet in range(254):
    #assign IP to ping to a variable 
    #adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet + 1)

    #Call ping_host funcation and capture the return value 
    exit_code = ping_host(ip)

    #Print results to consoles only if successful 
    if exit_code == 0:
        print("{0} is online".format(ip))

    
