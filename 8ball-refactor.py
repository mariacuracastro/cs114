def get_number():
    num = int(input('A number between 1 and 99: '))
    return num

def get_tens_inwords(num):
    tens = num // 10
    tens_word = ''
    
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word

def get_ones_inwords(num):
    ones = num % 10
    
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    else:
        ones_word = ''
    
    return ones_word

def make_output(num, tens_word, ones_word):
    tens = num // 10
    ones = num % 10
    
    
    if int(num) >= 100:
        output = 'not valid'
    elif int(num) <= 0:
        output = 'not valid'
    elif tens == 0:
        output = ones_word
    elif tens == 1:
        if ones == 1:
            output = 'eleven'
        elif ones == 2:
            output = 'twelve'
        elif ones == 3:
            output = 'thirteen'
        else:
            output = ones_word + 'teen'
    else:
        output = tens_word + '-' + ones_word
    
    msg = 'Your number is, ' + output
    return msg

def main():
    num = get_number()
    tens_inwords = get_tens_inwords(num)
    ones_inwords = get_ones_inwords(num)
    output = make_output(num, tens_inwords, ones_inwords)
    print(output)

main()

