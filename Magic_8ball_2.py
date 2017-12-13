import random

def get_name():
    print ('Greetings! Please enter your name and you will be rewarded with your fortune')
    name = input()
    return name

def get_random_number():
    random_num = random.randint(1, 6)
    return random_num

def getFortune(random_num):
    if random_num == 1:
        return 'It is certain'
    elif random_num == 2:
        return 'It is decidedly so'
    elif random_num == 3:
        return 'Reply hazy try again'
    elif random_num == 4:
        return 'Ask again later'
    elif random_num == 5:
        return 'Concentrate and ask agin'
    elif random_num == 6:
        return 'Outlook not so good'

def make_output(name, fortune):
    msg = 'Hello, ' + name + ' your furtune is ' + fortune
    return msg

# print(greeting(name))

def main():
    name = get_name()
    random_num = get_random_number()
    fortune = getFortune(random_num)
    output = make_output(name, fortune)
    print(output)

main()
