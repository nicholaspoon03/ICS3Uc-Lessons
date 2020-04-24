# Lists 

# Lists are just another data-type
# A list is a collection of other pieces of data



# for numbers, index 0 = 1, index 1 = 2, index 2 = 4, index 3 = 7
numbers = [1, 2, 1, 7, 9, 22, 43, 55]

# Use index value's to access individual items of a list.
# An index is a position on your list
# Index's start at position 0.

# Each position in a list is numbered from 0 to however many items are in the list.

# List Methods
# append method - adds an element to the end of your list

words = ["one", "two", "three"]

# add the string "four" to words
words.append("four")


# Count method - takes in a value as an argument, and returns how many times the item appears in the list
print(numbers.count(1))

# For more list methods, see: https://www.w3schools.com/python/python_ref_list.asp


# For loop
# A loop is a segment of code that will repeat over a certain number of times
# In a for loop, the segment of code repeats for each item inside of a list.

for item in words:
    if item == "one":
        print(item)
    else: 
        print("wrong")

nums = [1, 35, 20, 2, 10, 15, 50, 12]

for item in nums:
    if item > 15:
        print(item)