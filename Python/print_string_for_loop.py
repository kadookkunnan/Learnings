# First accept the input string
input_string = input("Enter a string value: ")

# Echo/print the input back to the user.
print(f"Your entered: <{input_string}> \n______________________________________________")

# Get the length of the string.
string_length = len(input_string)

# Print the statement to print the letters
print(f"Printing the characters of <{input_string}>\n")

# Printing the characters in normal order
for i in input_string:
    print(i)

# Print the statement to print the letters in reverse
print(f"\nPrinting the characters of <{input_string}> in reverse\n")

# Printing the characters in reverse order
for j in range((string_length-1), -1, -1):
    print(input_string[j])

# This logic also works.
#for k in range(1, string_length+1):
 #   print(input_string[(-1 * k)])