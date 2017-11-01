import random

print ('Welcome, I am the Magical 8 Ball and I would like to share a little about your future. Do you want to learn more? Type Yes or No.')
input()
random_num = random.randint(1, 4)

if random_num == 1:
    print("You are awesome!")
elif random_num == 2:
    print("You will be really good looking when you are old")
elif random_num == 3:
    print("You will live a long life!")
elif random_num == 4:
    print("Your life span is unclear.")


#
# if Yes == "Great!"
# if No == "Good-Bye and Good Luck."
# print ('What is your name?')
# name = input ()
# print ('Hello', name)
