# Exercises 5-2, p.82

# Equality
age = 17

if age == 17:
    print('You\'re eligible to play in that category.')
else:
    print('You do not have the eligible age to play in that category.')


# Inequality + lower() function
country = ' Venezuela  '
country = country.lower().strip()

if country != 'united states':
    print('\nThis content is blocked in your country.')
else:
    print('\nVideo loading.')


# Greater than + Less than
age = 24

if age >= 18 and age <= 23:    # Age 24 should trigger negative response.
    print('\nYou can play soccer in the Olympics.')
else:
    print('\nYou are not elegible to play soccer in the Olympics.')


# Item in list or not
# In
ale_teams = ['Blue Jays', 'Orioles', 'Rays', 'Red Sox', 'Yankees']
team = 'Rangers'

if team in ale_teams:
    print('\nThe ' + team + ' play in the AL East.')  # True statement
else:
    print('\nThe ' + team + ' do not play in the AL East.')  # False statement

# Not In
if team not in ale_teams:
    print('\nThe ' + team + ' play in another division.')  # True statement
else:
    print('\nThe ' + team + ' play in the AL East.')  # False statement
