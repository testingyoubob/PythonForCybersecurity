# #open file
# ip_file = open("ips.txt", "r")

# #Read the file

# ip_address = ip_file.read()
# #OutPut file
# print(ip_address)

with open("ips.txt", "r") as ip_file:
    print(ip_file.read())



