import math as m
# a python program for intro to the use of functions in python
# the main aim of the app is to take 5 numbers from the user, use a function to sum them up and return the value

# declaration of the five variables to hold the user input
a, b, c, d, e = input("Type in the next number: ").split()

def power1():
    z = int(a) + int(b) + int(c) + int(d) + int(e)
    print(z)


def power2():
    z =   int(a) + int(b) + int(c) + int(d) + int(e)
    z = m.sqrt(z)
    return z

print("This is the sum of the 5 numbers using the power1 function: ")
power1()
print("The squareroot of the sum is: " , m.sqrt(power1)+power1())

print("This is the sum of the 5 numbers using the power2 function: ")
print(power2())