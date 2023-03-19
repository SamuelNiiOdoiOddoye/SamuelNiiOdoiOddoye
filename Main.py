import random
# Create A Password Generator.
# Prompt the user to enter the desirednumber of digits, letters and symbols wanted in the password.
# Based on the user input, randomly select digits, letters and symbols respectively and store them in variables and then concatenate them into a new string
# Display the generated password.

# This part of the code is supposed to take in the desired number of letters, symbols and numbers
Desired_Number_Of_Digits = int(input("What is the desired number of digits to be used: "))
Desired_Number_Of_Letters = int(input("What is the desired number of Letters to be used: "))
Desired_Number_Of_Symbols = int(input("What is the desired number of Symbols to be used: "))

# a string variable to hold the alphabets
Alphabet = 'ABCDEFFGHIJKLMNOPQRSTUVWXYZ'

# a string variable to hold special characters
Special_Characters = '~`!@#$%^&*()_-+=/*-+\|][}{:;"/?><.,'

# Variables to hold the password generated so far, variables to hold the number of characters printed
Password_So_Far =""
Password_Digit = ""
Password_Symbol = ""
Password_Letter = ""
Digit_Generated = 0
Letter_Generated = 0
Symbols_Generated = 0


# An if condition to control  the number of digits generated and to save them in Password_So_Far
while Digit_Generated < Desired_Number_Of_Digits :
    Random_Digit = random.randint(0,9)
    Password_Digit += str(Random_Digit)
    Digit_Generated += 1


# An if condition to control  the number of letters generated and to save them in Password_So_Far
while Letter_Generated < Desired_Number_Of_Letters :
    Random_Letter = random.choice(Alphabet)
    Password_Letter += Random_Letter
    Letter_Generated += 1


# An if condition to control the number of special characters generated and to save then in Password_So_Far
while Symbols_Generated < Desired_Number_Of_Symbols :
    Random_Special_Characters = random.choice(Special_Characters)
    Password_Symbol += str(Random_Special_Characters)
    Symbols_Generated += 1

# This part contains how the password generated so far should be shuffled and printed out
Password_So_Far = str(Password_Digit)+ str(Password_Symbol) + str(Password_Letter)
print("Your password is: ", Password_So_Far)