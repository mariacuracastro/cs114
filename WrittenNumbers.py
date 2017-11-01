print('Written Numbers Converter')

print('Enter number')
num = int(input())

tens = num // 10
ones = num % 10

print('You entered:' + str(num))
print('The first digit is: ' + str(tens))
print('The second digit is: ' + str(ones))

if tens == 1:
    string_number = 'one'
elif tens == 2:
    string_number = 'two'
elif tens == 3:
    string_number = 'three'
elif tens == 4:
    string_number = 'four'
elif tens == 5:
    string_number = 'five'
elif tens == 6:
    string_number = 'six'
elif tens == 7:
    string_number = 'seven'
elif tens == 8:
    string_number = 'eight'
elif tens == 9:
    string_number = 'nine'

if ones == 1:
    string_number = 'eleven'
elif ones == 2:
    string_number = 'twelve'
elif ones == 3:
    string_number = 'thirteen'
elif ones == 4:
    string_number = 'fourteen'
elif ones == 5:
    string_number = 'fifteen'
elif ones == 6:
    string_number = 'sixteen'
elif ones == 7:
    string_number = 'seventeen'
elif ones == 8:
    string_number = 'eighteen'
elif ones == 9:
    string_number = 'nineteen'


print(string_number)



# elif 2 = 'two':
#     print("two")
# elif 3 = 'three':
#     print("three")
