# importing libraries
from curses.ascii import isdigit

# Function to add two variables and get the result.
def add(a,b):
    return (a + b)

# Function to subtract two variables and get the result.
def subtract(a,b):
    return (a - b)

# Function to multiply two variables and get the result.
def multiply(a,b):
    return (a * b)

# Function to divide two variables and get the result.
def divide(a,b):
    return (a / b)

# Function to get remainder (%) two variables and get the result.
def remainder(a,b):
    return (a % b)

# Function to get quotient (//) two variables and get the result.
def quotient(a,b):
    return (a // b)

# Function to get square of a number.
def square(a):
    return (a * a)

# Function to return a valid calculator option
def getValidOption() -> int:
    optionInvalid = True

    # Showing the input options to the user.
    print("\nChoose an option from the following: \n\n (1) Add (+) \n (2) Subtract (-) \n (3) Multiply (*) \n (4) Divide (/) \n (5) Find Remainder (%) \n (6) Find Quotiend (//) \n (7) Find Square of a number (**) \n")

    # we need to accept an option by the user as input (needs to be a valid option)
    while optionInvalid:
        userOption = input("Select an option: ")
        if userOption.isdigit():
            option = int(userOption)
        
            if (option > 0 and option < 8):
                optionInvalid = False
                return option
        
        print("Please enter a valid option!")

# Function to return a valid input as integer
def getValidInput(choice = "the") -> int:
    inputInvalid = True
    
    # Checks for valid input and keeps asking until the input is valid.
    while inputInvalid:
        userInput = input(f"Enter {choice} number: ")
        if userInput.isdigit():
            inputInvalid = False
            return int(userInput)
        
        print("Please enter a valid input! \n")

def calculator():
    option = getValidOption()
    
    num1 = 0
    num2 = 0
    result = 0

    if (option >= 1 and option <= 6):
        num1 = getValidInput("first")
        num2 = getValidInput("second")

        if (option == 1):       # Add operation
            result = add(num1, num2)
        elif (option == 2):     # Subtract operation
            result = subtract(num1, num2)
        elif (option == 3):     # Multiply operation
            result = multiply(num1, num2)
        else:     
            while (num2 == 0):
                print("Please enter another number as division by 0 is not allowed!")
                num2 = getValidInput("second")
                if (num2 != 0):
                    break
            if (option == 4):   # Divide operation        
                result = divide(num1, num2)
            elif (option == 5): # Remainder operation
                result = remainder(num1, num2)
            else:               # Quotient operation
                result = quotient(num1, num2)
    else:
        num1 = getValidInput()
        result = square(num1)

    print(f"Output is: {result}")


# Calling the calculator method for execution
multipleCalculation = True
while multipleCalculation:
    calculator()

    choice = input("\nWould you like to do another calculation? \n\nEnter 'y' or 'yes' to do again \nEnter anything else to quit \n\n Do again?? : ").lower()

    if (choice == "y" or choice == "yes"):
        continue
    else:
        break

    





