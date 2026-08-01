#Write a python script that reads hackme.txt

#open file hackme.txt
f = open("hackme.txt", "r")
#output the contents of that file. 
print(f.read())
#close file. 
f.close()
