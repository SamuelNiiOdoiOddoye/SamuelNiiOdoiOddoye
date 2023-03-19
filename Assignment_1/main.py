# a python program to print out the prime numbers between 2 and 31

# print("The Numbers between -1 and 31 are : ")
newlist = [30]
for x in range(2, 31):
    for y in range(2, x) :
        if x % y == 0:

            print( y , " is not a prime number")
    else:
        print(x , " is a prime number")
