# First accept the first input string
first_string = input("Enter a string value: ")

# Echo/print the input back to the user.
print(f"Your entered: {first_string} \n______________________________________________")

# Printing the first character.
print(f"First character in '{first_string}' is: '{first_string[0]}' \n______________________________________________")

# Printing the last character.
print(f"Last character in '{first_string}' is: '{first_string[-1]}' \n______________________________________________")

# Finds the length of the string.
string_length = len(first_string);

# Printing the length of the string.
print(f"Length of string '{first_string}' is: {string_length} \n______________________________________________")

# Printing the middle index
middle_index = int(string_length/2)
print(f"Middle index is: {middle_index} \n______________________________________________")

# Printing the middle characters accordingly.
if string_length % 2 == 0:
    print(f"Middle characters in '{first_string}' are: '{first_string[(middle_index - 1)]}' and '{first_string[middle_index]}'")
else:
    print(
        f"Middle character in '{first_string}' is: '{first_string[middle_index]}'")
