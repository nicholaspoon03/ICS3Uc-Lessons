#Admission Price Solution

#Guests age 2 and under are free
baby = 0

# between 3 and 12 cost 14.00
kids = 14.00

# Seniors over 65 cost 18.00
senior = 18.00

# all others pay 23.00
adult = 23.00


# Step 1: Take ages of group members from user. 
# Users can input as many people as they want.
# user inputs a blank, when they are ready to stop.

#Letters will break this as well. How can you fix this?
i = 1
allAges = []
while i > 0:
    age = input('Please enter an age for each group member. Enter blank when finished: ')
    if age.isalpha() == True:
        print("incorrect value. try again") 
        break
    if age == " ":
        break   #the keyword break ends the loop. If this is encountered, your loop finishes, but your program continues to run.

    age = int(age)
    allAges.append(age)

#At this point, we would have our data list.

# This will be the total cost
totalCost = 0

# This will be the number of each age group
babyCount = 0
kidsCount = 0
seniorCount = 0
adultCount = 0

# We will write a loop to go through each item in allAges, and it will tally age groups, and calculate total cost.

for item in allAges:
    # check age group. Use conditionals
    if item <= 2:
        # babyCount = babyCount + 1   Long way
        babyCount += 1
    elif item >= 3 and item <= 12:
        kidsCount += 1
        totalCost += kids
    elif item >= 65:
        seniorCount += 1
        totalCost += senior
    else:
        adultCount += 1
        totalCost += adult
print(allAges)
print("Total: " + str(totalCost) + " babies: " + str(babyCount) + " kids: " + str(kidsCount) + " seniors: " + str(seniorCount) + " adults: " + str(adultCount))
