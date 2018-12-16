# Exercise p.93

# 5.8

usernames = ['john24', 'admin', 'fr4nk', '3m1ly', 'jack1', 'emmA']

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello ' + username + ', would you like to see a status'
                  ' report?')
        else:
            print('Hello ' + username + ', thanks for logging in again.')
else:
    print('We need to find some users!')

# 5.10

current_users = ['john24', 'admin', 'FRANK', '3m1ly', 'wayneee', 'emmA']
current_users_lower = [current_user.lower() for current_user in current_users]
new_users = ['r4lph', 'jennif3r', 'erikkk', 'frank', 'm0lly', 'wayneee']

for new_user in new_users:
    if new_user in current_users_lower:
        print('The username ' + new_user + ' is not available, please '
              'pick a new one.')
    else:
        print('The username ' + new_user + ' is available.')

# To ensure that the comparison in ln.24 is case insensitive, I had to create
# a new variable called current_users_lower, which is current_users variable
# with a loop to turn each item within current_users into lowercase (see ln.
# 20).

# 5.11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + 'th')
