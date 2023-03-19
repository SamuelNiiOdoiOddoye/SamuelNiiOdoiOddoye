# A python Project to calculate the love levels among two straight individuals using their names

loveArray = ['l', 'o', 'v','e']
true = ['t', 'r', 'u', 'e']

userInput = input("What's your name? ")
charInput1 = list(userInput)


userInput2 = input("What's your lover's name? ")
charInput2 = list(userInput2)


count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(0, userInput.__len__()):
    for j in range(0, true.__len__()):
        if true[j] == charInput1[i]:
            count1 = count1 + 1

for i in range(0, userInput2.__len__()):
    for j in range(0, true.__len__()):
        if true[j] == charInput2[i]:
            count2 = count2 + 1


for i in range (0, userInput.__len__()):
    for j in range (0, loveArray.__len__()):
        if loveArray[j] == charInput1[i]:
            count3 = count3 + 1

for i in range(0, userInput.__len__()):
    for j in range(0, loveArray.__len__()):
        if loveArray[j] == charInput2[i]:
            count4 = count4 +1


trueScore = count1 + count2
loveScore = count3 + count4
trueLove = "{0}{1}".format(str(trueScore), str(loveScore))
finalScore = int(trueLove)
print(finalScore)

if finalScore < 40:
    print("You are not compatible but you may have a chance")
elif finalScore == 50:
      print("You're compatible. Good Luck")
else:
    print("OH MY GOD YOU'RE THE PERFECT MATCH FOR EACH OTHER")
