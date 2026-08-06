# Create a script that prompts the user for a number and a divisor.
# In the script, create a function named is_divisible, and pass in the number and divisor as parameters.
# The function should then return true or false if the number was cleanly divisible (i.e. no remainders).
# The script reports if the number was divisible

def is_divisible(num, div):
    return num % div == 0 


number = int(input("What is the number: "))
divisor = int(input("What is the divisor: "))

if(is_divisible(number, divisor)):
    print(number , " is divisible by ",  divisor)
else:
    print( number, "is NOT divisible by " , divisor)


