# Chapter 5, 'Checking for inequality', p.78

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# Above: the if statement is asking if requested_topping is NOT equal to
# 'anchovies', then the string 'Hold the anchovies!' should be printed.
# Because the requested_topping variable is set as 'mushrooms' (thus not
# 'anchovies'), the string 'Hold the anchovies!' is printed.

mo_number = 42

question = 'What was Mariano Rivera\'s jersey number?'
print(question)

answer = 24

if answer != 42:
    print('\nThis is not the correct answer. Please try again!')


# Same as above but comparing answer to Rivera's number using the variables
if answer != mo_number:
    print('\nThis is not the correct answer. Please try again!')
else:
    print('\nWell done!')


# Numerical comparisons:
age = 18

if age >= 16:
    print('You can purchase that game.')
else:
    print('You\'re too young to purchase that game.')


# Checking multiple conditions using and.
age = 19
country = ' Canada  '
country = country.lower().strip()

if (age >= 18) and (country == 'united states'):
    print('You are eligible to play in the League.')
else:
    print('You are not eligible to play in the League.')


# Checking if value is in list with 'in'.
usernames = ['john', 'julie', 'emily', 'ian']
proposed_username = 'irene'

if proposed_username in usernames:
    print('\nThis username is already taken.')
else:
    print('\nThis username is availabe!')


# Checking if value is NOT in list with 'not in'.
banned_usernames = ['john17', 'julie8', '3mily', 'ian77']
login_username = 'irene17'

if login_username not in banned_usernames:
    print('\nWelcome back to our forums!')
else:
    print('\nYou have been banned from our forums.')
