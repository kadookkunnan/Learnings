# Function to return a valid input as number
def getValidInputNumber(message) -> int:
    inputInvalid = True

    # Checks for valid input and keeps asking until the input is valid.
    while inputInvalid:
        userInput = input(f"{message}: ")
        if userInput.isdigit():
            inputInvalid = False
            return int(userInput)

        print("Please enter a valid input! \n")

# Accept the starting number as input.
starting_number = getValidInputNumber("Please enter the starting number")

# Echo/Print the number back to the user.
print(f"The starting number you have entered is: {starting_number}")

# Accept the number of iterations as input.
num_iterations = getValidInputNumber("Please enter the number of iterations")

# Echo/Print the number back to the user.
print(f"The number of iterations you have entered is: {starting_number}")

# Calculating the even number near to the starting_number.
nearest_even_number = starting_number
if starting_number % 2 != 0:
    nearest_even_number = starting_number + 1

# Priting the num_iterations number of even numbers - Using for loop.
print(f"The even numbers starting from {starting_number} are:")
i = 0
for i in range(0,num_iterations):
    print(f"{nearest_even_number}")
    nearest_even_number += 2

"""
# PLEASE REMEMBER TO COMMENT FOR_LOOP BEFORE UNCOMMENTING THIS TO GET IT WORKING CORRECTLY
# Priting the num_iterations number of even numbers - Using while loop
i = 0
while i < num_iterations:
    print(f"{nearest_even_number}")
    nearest_even_number += 2
    i += 1
"""