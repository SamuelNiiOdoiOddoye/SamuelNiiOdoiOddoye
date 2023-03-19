from array import *
# create a method encrypt
# encrypt should : 
# - Allow user to enter 2 sets of inputs one of data type string and the other int
# - Assign the text and int data types to thier own unique variables
# Create an array within the encrypt method to hold alphabets
# scan the input to take the individual letters, skip 5 to 5 letters from the alphabet
# then print out "The encoded text is: "


# creating global variables

# creating a method called encrypt
def encrypt():
    # creating a variable of name Plain_Text to hold the user's input (data type of string)
    Plain_Text = input("Type in your desired text: ").upper()

    # creating a variable to hold the split of the variable Plain_Text
    # Plain_Text_Splitted = Plain_Text.split()

    # A character array to hold letters of the alphabet
    Alphabets = [ ' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', ]

    # creating a variable of name shift to hold the user's input (data type of int)
    shift = int(input("Type in the desired number of skips here: "))

    # a for loop to skip the letter in Plain_Text by shift
    Text_Shifted=""

    for c in Plain_Text:
        Y = ord(c) + shift
        Text_Shifted += chr(Y)

    print("The encoded text is : ", Text_Shifted)

    if shift > 25:
       shift = shift-25
       for c in Plain_Text:
           Y = ord(c) + shift
           Text_Shifted += chr(Y)







encrypt()

