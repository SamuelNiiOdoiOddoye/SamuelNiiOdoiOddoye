# take a message from the user
# convert the input into characters only
# display the ascii equivalence of the characters onto the console

# this is the point of the code where the user inputs his ir hr message into the console
# the variable User_Input_1 holds the message the user inputs into the console to be encrypted
User_Input_1 = input("Type in Your desired message here: ")

#this part of the code holds words in the sentence
# a variable l1 is to hold the words
l1 = User_Input_1.split()

# a for loop to populate an array of data type character with the message the user inputs into the console
# c in the for loop below represents every character in the variable User_Input_1
# This portion was originally meant to present every letter in a word
# but in the case of the user input being a sentence it still prints all individual characters
for c in User_Input_1:
   Y = print(ord(c))


# an attempt to save the characters into a variable and then print out the characters
# Ask the user if he wants to print the original word or sentence
# a variable User_Response to hold user answer
# declare an if....else statement for if the user wants to or to not print his original entry

print(l1)
print(User_Input_1)