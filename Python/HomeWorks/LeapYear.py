# Function to return a valid input as year
def getValidInputYear() -> int:
    inputInvalid = True

    # Checks for valid input and keeps asking until the input is valid.
    while inputInvalid:
        userInput = input(f"Enter an Year: ")
        if userInput.isdigit():
            inputInvalid = False
            return int(userInput)

        print("Please enter a valid input! \n")


# Receives the year to check as a Keyboard input.
yearToCheck = getValidInputYear()

print(f"Checking if {yearToCheck} is a Leap Year")

# First checks whether the year is divisible by 4, then it is divi
if yearToCheck % 4 != 0:
    print(f"{yearToCheck} is not a leap year as it is not divisible by 4.")
# Otherwise, if the year is divisible by 100 alone but not by 400 then it is not a leap year
# Divisible 100 means it is a Century year.
elif yearToCheck % 100 == 0 and yearToCheck % 400 != 0:
    print(f"{yearToCheck} is not a leap year as it is divisible by 100 but not divisible by 400.")
# In other cases, it will be a leap year as it would either of the following:
# Divisible by 4 and not divisible by 100
# OR
# Divisible by 400
else:
    print(f"{yearToCheck} is a leap year as it is divisible by 4 but not by 100 or 400.")