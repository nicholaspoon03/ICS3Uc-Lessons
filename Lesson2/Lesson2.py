import math

# Inputs

# obtaining length and width as input
length = input("Enter a length in meters: ")
width = input("Enter a width in meters: ")

# converting length/width to int
length = int(length)
width = int(width)

# caluclate perimeter
perimeter = length * 2 + width * 2

# covnert to string
perimeter = str(perimeter)

# concatenation
print("The perimeter is: " + perimeter + " meters")

# using sqrt from math library

square = input("Please enter a number to root: ")
square = float(square)

root = math.sqrt(square)

print(root)


#Boolean Operators
bool1 = False
bool2 = True
bool3 = False

# Three boolean Operators: and or not
# and operator: returns true if and only if both sides of the "and" are true
andTest = True and bool2
print(andTest)

# OR operator: returns true if one or both sides of it are true
orTest = bool1 or bool2
print(orTest)

# NOT operator: flips true to false, and false to true
notTest = not bool3

# Combining boolean operators

# order of boolean operations: NOT first, AND second, OR last
orderTest = not bool1 or bool3 and bool2
print(orderTest)