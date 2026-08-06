# Update the Conditional / Loop script
# Create a function named send_message
# Move the looping "Yeah it is" code to the function
# Update the conditional statement to call the function
# Define the send_message function containing the loop

def send_message():
    # Example loop repeating "Yeah it is" 3 times
    for _ in range(3):
        print("Yeah it is")

# Example condition variable
statment = True

# Conditional statement calling the function
if statment:
    send_message()
else:
    print("Statment is false.")