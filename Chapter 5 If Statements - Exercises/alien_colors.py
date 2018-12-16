# Exercise p.88

alien_color = 'green'

if alien_color == 'green':
    print('You\'ve just earned 5 points!')

# 5.3


alien_color = 'red'

if alien_color == 'green':
    print('\nYou\'ve just earned 5 points!')

if alien_color != 'green':
    print('\nYou\'ve just earned 10 points!')

#


alien_color = 'green'

if alien_color == 'green':
    print('\nYou\'ve just earned 5 points!')
else:
    print('\nYou\'ve just earned 10 points!')


# 5.4


alien_color = 'green'

if alien_color == 'green':
    print('\nYou\'ve just earned 5 points!')
elif alien_color == 'yellow':
    print('\nYou\'ve just earned 10 points!')
else:
    print('\nYou\'ve just earned 15 points!')

alien_color = 'yellow'

if alien_color == 'green':
    print('\nYou\'ve just earned 5 points!')
elif alien_color == 'yellow':
    print('\nYou\'ve just earned 10 points!')
else:
    print('\nYou\'ve just earned 15 points!')

alien_color = 'blue'

if alien_color == 'green':
    print('\nYou\'ve just earned 5 points!')
elif alien_color == 'yellow':
    print('\nYou\'ve just earned 10 points!')
else:
    print('\nYou\'ve just earned 15 points!')


# 5.6


age = 1

if age < 2:
    print('\nYou\'re a baby.')
elif (age >= 2) and (age < 4):
    print('\nYou\'re a toddler.')
elif (age >= 4) and (age < 13):
    print('\nYou\'re a kid.')
elif (age >= 13) and (age < 20):
    print('\nYou\'re a teenager.')
elif (age >= 20) and (age < 65):
    print('\nYou\'re an adult.')
elif age >= 65:
    print('\nYou\'re an elder.')

#


age = 4

if age < 2:
    status = 'baby'
    article = 'a'
elif (age >= 2) and (age < 4):
    status = 'toddler'
    article = 'a'
elif (age >= 4) and (age < 13):
    status = 'kid'
    article = 'a'
elif (age >= 13) and (age < 20):
    status = 'teenager'
    article = 'a'
elif (age >= 20) and (age < 65):
    status = 'adult'
    article = 'an'
elif age >= 65:
    status = 'elder'
    article = 'an'


print('\nYou\'re ' + article + ' ' + status + '.')


# 5.7


fruits = ['grapes', 'strawberries', 'oranges', 'apples']

if 'grapes' in fruits:
    print('\nWe have grapes in our basket.')
if 'oranges' in fruits:
    print('\nWe have oranges in our basket.')
if 'mangoes' in fruits:
    print('\nWe have mangoes in our basket.')


#


favorite_fruits = fruits[0:3]  # Copying the list and selecting first 3 items.

if 'grapes' in favorite_fruits:
    print('\nYou really like grapes!')
if 'apples' in favorite_fruits:
    print('\nYou really like apples!')
if 'raspberries' in favorite_fruits:
    print('\nYou really like raspberries!')
if 'strawberries' in favorite_fruits:
    print('\nYou really like strawberries!')
if 'oranges' in favorite_fruits:
    print('\nYou really like oranges!')
