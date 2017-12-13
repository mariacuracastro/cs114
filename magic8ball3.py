print ('Greetings! Please enter your name and you will be rewarded with your fortune')
name = input()

import random

FortuneList = [
'You are gonna do great',
'Load up on caffeine',
'Get some extra rest',
'You got this'
]

def myRandomFortune(FortuneList):
    random_num = random.randint(0,3)
    print(FortuneList[random_num])

myRandomFortune(FortuneList)


# get random number
#
# use random number to pull fortune from list

# FortuneList = len(fortune) >= 4

# fortune1 = [fortune[0]]
# fortune2 = [fortune[1:2]]
# fortune3 = [fortune[2:3]]
# fortune4 = [fortune[3:4]]
