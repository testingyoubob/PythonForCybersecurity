#!/usr/bin/env python3
# Port scanner example 
# Use 'pip3 install python-nmap' to install modules
# Use 'sudo apt -y install nmap' to install nmapccc
# By mj 


import nmap
#Identify targetaddress
target_address="192.168.0.10"
#Identify startandstopportforthescan
port_start=1
port_end=100

#Createthescannerobject
scanner=nmap.PortScanner()

print("Scanning{0}".format(target_address))
#Loopthrougheachport andscan
for port in range(port_start,port_end+1):
    result=scanner.scan(target_address,str(port))
    port_status=result['scan'][target_address]['tcp'][port]['state']
    print("\tPort:{0}is{1}".format(port,port_status))
