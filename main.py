# write a function in python that accepts 2 string parameters.
# The first parameter will be a string of characters, and the second parameter will be the same string of characters,
# but they'll be in a different order and have one extra character.
# For example if the first parameter is "eueiieo" and the second is "ieoedue" then the function should return "d"

# create a function to take in two inputs of the same data type string
# shuffle the elements of the second variable and then print out the difference
def Spot_The_Difference():
    #this point of the function is to accept 2 inputs from the user
    #this is where two variables are declared and assigned to hold to the entries
    First_Entry = input("Type in your first word here: ")
    Second_Entry =input("Type in your second entry here: ")

    #creating a variable to hold the splitted elements of the First_Entry and Second_Entry
    First_Entry_Splitted = First_Entry.split()
    Second_Entry_Splitted = Second_Entry.split()
    First_Entry_Sum = 0
    Second_Entry_Sum = 0

# a for loop to change every character in First_Entry to it's ASCII equivalvent and sum up all the ASCII equivalent's
    for c in First_Entry:
        First_Entry_Sum += int(ord(c))

# a for loop to change every character in Second_Entry to it's ASCII equivalent and sum up all the ASCII equivalent's
    for c in Second_Entry:
        Second_Entry_Sum += int(ord(c))

# an if condition to subtract the sum of the second entry from the first entry if the first entry sum is greater than
# the second entry sum
    if First_Entry_Sum > Second_Entry_Sum:
        l1 = First_Entry_Sum - Second_Entry_Sum
        print(chr(l1), "is the unique entry of the two entries and is found in", First_Entry)

# an if condition to subtract the sum of the first entry from the second entry if the second entry sum is greater than
# the first entry sum
    if Second_Entry_Sum > First_Entry_Sum:
        l2 = Second_Entry_Sum - First_Entry_Sum
        print(chr(l2), "is the unique entry of the two entries and is found in", Second_Entry)

# an if condition if both entries have the same ASCII sum
    if Second_Entry_Sum == First_Entry_Sum:
        print("There is no unique character in both entries")

Spot_The_Difference()
