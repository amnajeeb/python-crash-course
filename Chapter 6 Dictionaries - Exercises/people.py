# Exercise p.115

# 6-7

athlete_0 = {}

athlete_0['first'] = 'mariano'
athlete_0['last'] = 'rivera'
athlete_0['age'] = 32
athlete_0['city'] = 'new york'

athlete_1 = {}

athlete_1['first'] = 'mike'
athlete_1['last'] = 'trout'
athlete_1['age'] = 26
athlete_1['city'] = 'anaheim'

athlete_2 = {}

athlete_2['first'] = 'clayton'
athlete_2['last'] = 'kershaw'
athlete_2['age'] = 29
athlete_2['city'] = 'los angeles'

athletes = [athlete_0, athlete_1, athlete_2]

print(athletes)

for athlete in athletes:
    full_name = athlete['first'].title() + ' ' + athlete['last'].title()
    print(full_name)
    print('\t' + 'Age: ' + str(athlete['age']))
    print('\t' + 'City: ' + athlete['city'].title())

# 6-8

ronnie = {
    'name': 'ronnie',
    'animal type': 'cat',
    'owner name': 'ada'
    }

milou = {
    'name': 'milou',
    'animal type': 'dog',
    'owner name': 'tintin'
    }

mamba = {
    'name': 'mamba',
    'animal type': 'snake',
    'owner name': 'david'
    }

pets = [ronnie, milou, mamba]

for pet in pets:
    print(pet['name'].title() + ' is a ' + pet['animal type'] +
          ', and belongs to ' + pet['owner name'].title() + '.')

# 6.9

favorite_places = {
    'amir': ['anchorage', 'yangshuo'],
    'erika': ['cape town', 'paris', 'hanoi'],
    'jenny': ['alaska'],
    'ralph': ['buenos aires']
    }

for names, places in sorted(favorite_places.items()):
    if len(places) > 1:
        print(names.title() + '\'s favorite places are:')
        for place in places:
            print('\t' + place.title())
    else:
        print(names.title() + ' likes only one place:')
        for place in places:
            print('\t' + place.title())

print('\n...')
# 6.10

fav_numbers = {}

fav_numbers['julie'] = [4, 44]
fav_numbers['oscar'] = [42, 24]
fav_numbers['amelia'] = [13, 7]
fav_numbers['emily'] = [9, 99]

for names, numbers in fav_numbers.items():
    print(names.title() + "\'s favorite numbers are:")
    for number in numbers:
        print('\t' + str(number))

# 6.11

cities = {
    'paris': {
        'country': 'france',
        'population': 12,
        'sport': 'football',
        },
    'new york': {
        'country': 'united states',
        'population': 17,
        'sport': 'basketball',
        },
    'tokyo': {
        'country': 'japan',
        'population': 30,
        'sport': 'baseball',
        },
}

for city, info in cities.items():
    print(city.title() + ' is the capital of ' + info['country'].title() +
          ', it has roughly ' + str(info['population']) +
          ' million inhabitants, and its people\'s favorite sport is ' +
          info['sport'].title() + '.')

users = {
    'mj23': {
        'first': 'michael',
        'last': 'jordan',
        'location': 'chicago',
        },
    'lbj23': {
        'first': 'lebron',
        'last': 'james',
        'location': 'los angeles',
        }
    }
