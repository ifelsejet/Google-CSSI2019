import random


classSchedule = ["English", "Chemistry", "PE","Music","Lunch","History","Math"]
#aye it works
#for myclass in classSchedule:
    #print "My favorite class is " + myclass

length = (len(classSchedule))

for index in range(length):
    print classSchedule[index]

myFavString = 'all my favorite things'

print myFavString

for i in myFavString:
    print i

random_num = random.randint(0,4)
print random_num

while random_num > 0:
    print random_num
    random_num = random_num - 1
