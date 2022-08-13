def subtract(a,b):
  return (a-b)

a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))

c = subtract(a,b)

if c < 0:
    c = c * -1

print("The absolute of (" + str(a) + " - " + str(b) + ") is: "+ str(c))