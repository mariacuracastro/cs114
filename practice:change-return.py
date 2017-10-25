print('Thank you for using our kick ass Super Change Converter! How much change do you want to convert? Enter a number < 100.')
initial_balance = int(input())
num_quarters = initial_balance // 25
run_total = initial_balance - (num_quarters * 25)
num_dimes = run_total // 10
run_total = run_total - (num_dimes * 10)
num_nickels = run_total // 5
run_total = run_total - (num_nickels * 5)
num_pennies = run_total // 1
run_total = run_total - (num_pennies * 1)
print ('Here is your change:')
print('Quarters =', num_quarters)
print('Dimes =', num_dimes)
print ('Nickels =', num_nickels)
print ('Pennies =', num_pennies)
print ('Grab your money from the change bin')
print('This completes your change return for the amount you gave us of', initial_balance)
print('Your new change total is', run_total)





#cost =
# new_balance = (inital - cost)
# cents_quarters =
# print('Your total quarters = ' , )
# cents_dimes =
# print('Your total dimes = ' , )
# cents_nickels =
# print('Your total nickels = ' , )
# cents_pennies =
# print('Your total pennies = ' , )
