# Conditionals

#IF statement
userVal = input("Please enter a number: ")
userVal = int(userVal)
num1 = 15

# Only ONE of the following conditions well ever execute.
# basic If
if userVal > 15:
    print("value is over 15")
# else if
elif userVal < 5:
    print("value is very small")
# Else - no condition, this is what triggers if none of the above conditions are met
else:
    print("value is under 15") 

#Comparative Operators
# >, <, >=, <=, ==
# > - greater than
# < - less than
# >= - greater than or equal to
# <= - less than or equal to
# == - equal to

compare1 = 13 == 12 # Datatype of compare1 is a Bool
print(compare1)