#!/usr/bin/env python3
# Third example of pinging from Python
# By mj

import platform 
import os 

ip_prefix = "192.168.0." 

current_os = platform.system().lower()
#determine the current os
for final_octel in range(254):
    #assign IP to pint to a variable 
    #adding 1 to final_octel because loop starts at 0 
    ip = ip_prefix + str(final_octel + 1)
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else: 
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

#Execute command and capture exit code 
exit_code = os.system(ping_cmd)
if exit_code == 0:
    print("{0} is online".format(ip))

            