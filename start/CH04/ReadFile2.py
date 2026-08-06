#mj
#Old way
# #open file for reading
# ip_file = open("ips.txt", "r")

# #Read the contents of the file and print to screen 

# ip_address = ip_file.read()
# print(ip_address)

# #Close the file 
# ip_file.close()

#Using the with and try method 

try:
    with open("ips.txt", "r", encoding="utf-8") as ip_files:
        ip_addresses = ip_files.read()
        print(ip_addresses)
except FileNotFoundError:
    print("Error: 'ips.txt ' Was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
