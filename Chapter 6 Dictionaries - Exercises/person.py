# Exercise p.102

# 6.1

athlete_0 = {}

athlete_0['first_name'] = 'mariano'
athlete_0['last_name'] = 'rivera'
athlete_0['age'] = 32
athlete_0['city'] = 'panama city'

print(athlete_0['first_name'])
print(athlete_0['last_name'])
print(athlete_0['age'])
print(athlete_0['city'])

# 6.2

fav_numbers = {}

fav_numbers['julie'] = 4
fav_numbers['oscar'] = 42
fav_numbers['amelia'] = 13
fav_numbers['emily'] = 7

print('Hi I\'m Julie and my favorite number is ' + str(fav_numbers['julie']) +
      '.')
print('Hi I\'m Oscar and my favorite number is ' + str(fav_numbers['oscar']) +
      '.')
print('Hi I\'m Amelia and my favorite number is ' +
      str(fav_numbers['amelia']) + '.')
print('Hi I\'m Emily and my favorite number is ' + str(fav_numbers['emily']) +
      '.')

# 6.3

glossary = {}

glossary['list'] = 'range of number'
glossary['tuple'] = 'immutable list'
glossary['statement'] = 'checks condition of interest'
glossary['integer'] = 'other name for number in programming'

print(glossary)

for item in glossary:
    print('\n' + item.title() + ':')  # this prints the key.
    print(glossary[item].capitalize() + '.')  # this prints the value.
