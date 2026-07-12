#ask the user the question 

ask = input("Is today a good day? (y/n)")
#logic

if (ask == "y" or ask == "Y" or ask == "yes" or ask == "Yes" or ask == "YES"):
    #loop 
    for i in range(10):
        print("Yes it is")

    
elif (ask == "n" or ask == "N" or ask == "no" or ask == "No" or ask == "NO"):
    print("It will get better")
else:
    print("Invaild input")