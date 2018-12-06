# Exercises p.82

accepted_cars = ['suzuki', 'nissan', 'toyota', 'mitsubishi', 'honda']
registered_car = 'subaru'

if registered_car in accepted_cars:
    print('You are eligible to partipate in the race.')
else:
    print('You are not eligible to partipate in the race.')

registered_car2 = 'nissan'

if registered_car2 in accepted_cars:
    print('\nYou are eligible to partipate in the race.')
else:
    print('\nYou are not eligible to partipate in the race.')


# Another method
teams = 'Yankees'

if teams == 'Orioles':
    print('\nYou can buy tickets for the game.')
else:
    print('\nYou can not buy tickets at the moment.')


# Another method
age = 16
country = ' FRANCE  '
country = country.lower().strip()

if (age >= 18) and (country == 'france'):
    print('\nYou are eligible to enter the competition.')
else:
    print('\nYou are not eligible.')


# Another method
game_buyers = ['frank1', 'alic3', 'gamerzZz', 'footief4n', 'fcb85']
username = ' frank1  '
username = username.lower().strip()

if username in game_buyers:
    print('\nYou can find your Steam code below.')
else:
    print('\nYou have not purchased this game.')


# Another method
banned_users = ['ronald0', 'r33c3', 'theg33k4U', 'ananananas', '3w4n']
login_username = ' r33c3  '       # Will trigger 'You've been banned'.
login_username = login_username.lower().strip()

if login_username not in banned_users:
    print('\nWelcome back '+ login_username +'!')
else:
    print('\nYou\'ve been banned.')
