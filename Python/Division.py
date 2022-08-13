# Divides the given number and returns the result.
def division(a,b):
  return (a/b)

# Accepting inputs from Keyboard.
a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))

if a < 0:       # Only positive number is acceptable.
    print("Please enter a positive first number")

elif b == 0:    # We should divide only if the second number is not 0.
    print("Division by 0 is undefined!")    
elif b < 0:     # Only positive number is acceptable.
    print("Please enter a positive second number")
else:           # All good to go with the Division
    c = division(a,b)