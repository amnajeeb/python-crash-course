# if-elif-else statement, p.85
age = 17

if age < 4:
    print('Your admission is free.')
elif age < 18:  # no need for age >= 4 as it is covered by ln.5.
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')


# More concise way of doing things.
age = 3

if age < 4:
    price = 0
elif age < 18:  # no need for age >= 4 as it is covered by ln.5.
    price = 5
else:
    price = 10

print('\nYour admission cost is $' + str(price) + '.')
# the str() method turns the cost into a string (i.e. into text)


# Using multiple elif statements
age = 2

if age < 4:
    division = 'third'
elif age < 12:
    division = 'second'
elif age < 18:
    division = 'first'
else:
    division = 'veteran'

print('\nYou will play in the ' + str(division.lower()) + ' division.')


# Not using else statements at the end, but another elif to test for a final
# condition.
age = 19

if age < 4:
    division = 'third'
elif age < 12:
    division = 'second'
elif age < 18:
    division = 'first'
elif age >= 18:
    division = 'veteran'

print('\nYou will play in the ' + str(division.lower()) + ' division.')
