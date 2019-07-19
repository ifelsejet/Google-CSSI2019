import random

theRandomNumber = str(random.randint(0,10))
#print(theRandomNumber)
count = 0;
userInput = ""
isNotGuessed = True
numOfLives = 5

while(isNotGuessed and numOfLives >= 0):
    print("Guess the number")
    print("You have " + str(numOfLives) + " lives")
    userInput = raw_input();
    count = count + 1
    numOfLives = numOfLives - 1
    if(userInput == theRandomNumber):
        print("Congrats! You got it in " + str(count) + " tries!")
        isNotGuessed = False
    elif(numOfLives == 0):
        print("You Lose!, Try Again!")
        break

#print(userInput)
#print(str(count))
