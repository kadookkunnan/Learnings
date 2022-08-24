# Function to return a valid input as integer
def getValidInput() -> int:
    inputInvalid = True

    # Checks for valid input and keeps asking until the input is valid.
    while inputInvalid:
        userInput = input(f"Enter a number (preferably less than 10): ")
        if userInput.isdigit():
            inputInvalid = False
            return int(userInput)

        print("Please enter a valid input! \n")


# First accept the first input string
first_string = input("Enter a string value: ")

# Echo/print the input back to the user.
print(f"Your first string value is: {first_string} \n_________________________________")

# Accept the second string input
second_string = input("Enter another string value: ")

# Echo/print the second input back to the user.
print(f"Your second string value is: {second_string} \n__________________________________")

# Accept the number for printing
num_times = getValidInput()

# Echo/print the number back to the user.
print(f"You entered number: {num_times} \n__________________________________")

# Printing the results as per the operation
print(f"{first_string} + {second_string} is {first_string+second_string} \n__________________________________")
print(f"{first_string} * {num_times} is {first_string * num_times} \n__________________________________")
print(f"{second_string} * {num_times} is {second_string * num_times} \n__________________________________")