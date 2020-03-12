# Data-types 

# Words, characters, cannot be operated on, can only be concatenated.
word = "I am a string" # string, strings are always inside of quotes

# Numbers - Can be operated on (+, -, *, /, %) % is called "modulo"
number = 5             # Integer, for whole number
number_2 = 7.5         # Float

# Boolean, Yes or no
switch = False         # Bool, True or False

# Basic Operators
Test1 = 6
Test2 = 2.5
Test3 = 3

# Addition/Subtraction
addition = Test1 + Test2 # Datatype ?? Float
subtract = Test1 - Test2 # Datatype ?? Float

# Multiplication / division
mult = Test1 * Test2 # Datatype ?? Float (float * Int gives float)
mult2 = Test1 * Test3 # Datatype ?? Int (Int * Int gives integer)
div = Test1 / Test3 # Datatype ?? float (all division returns a float)
divInt = Test1 // Test3 # // keeps value as Int

# Modulo (%)
mod = 5 % 2 # Returns the remainder

# convert datatypes
convertedNum = int(4.9) # converts to Int, drops the decimal from a float, ALWAYS ROUNDS DOWN
convertedFloat = float("6.353574976") # converts to Float
convertString = str(convertedFloat) # converts to string

# Concatenation - Combining of strings

string1 = "Goodbye"
string2 = "US Dollar"

fullWord = string1 + " " + string2

print(fullWord)