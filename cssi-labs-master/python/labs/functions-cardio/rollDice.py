import random

def roll_dice(num):
    sum = 0
    while(num > 0):
        randomNum = random.randint(1,6)
        sum = sum+ randomNum
        num = num - 1
    print(sum)



roll_dice(2)
