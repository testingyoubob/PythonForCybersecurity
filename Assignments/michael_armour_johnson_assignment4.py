# reate a script that asks:

# What is your name
# What is your favorite color
# What was your first pet's name
# What is your mother's maiden name
# What elementary school did you attend
# Once the information is collected, the script should save it to a file called "hackme.txt"

name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What is your pet's name? ")
parent = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

#open the file 
f = open("hackme.txt", "w")
#write the file
f.write(name)
f.write(color)
f.write(pet)
f.write(parent)
f.write(school) 
#Close the file 
f.close()

