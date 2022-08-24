# First accept the input string
input_string = input("Enter a string value: ")

# Echo/print the input back to the user.
print(f"Your entered: {input_string} \n_____________________________________________________________")

# Calculates the length of the string
string_length = len(input_string)

# Prints the slice/substring after removing the first and last characters.
print(f"Slice of '{input_string}' after removing first and last character: '{input_string[1:(string_length-1)]}' \n_____________________________________________________________")

# Prints the slice/substring after removing the first two characters.
print(f"Slice of '{input_string}' after removing first two characters: '{input_string[2:]}' \n_____________________________________________________________")

# Prints the slice/substring after removing the first two characters.
print(f"Slice of '{input_string}' after removing last two characters: '{input_string[:(string_length-2)]}' \n_____________________________________________________________")

# Finding middle index
middle_index = int(string_length/2)

# Prints the middle index of the string.
print(f"Middle index of '{input_string}' is: '{middle_index}' \n_____________________________________________________________")

# Printing the substring/slices based on the middle index
print(f"First half slice of '{input_string}' is: '{input_string[:middle_index]}' \nSecond half slice of '{input_string}' is: '{input_string[middle_index:]}' \n_____________________________________________________________")