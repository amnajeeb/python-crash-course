# Nesting, p.109

alien_0 = {
    'color': 'green',
    'points': 5
    }

alien_1 = {
    'color': 'yellow',
    'points': 10
    }

alien_2 = {
    'color': 'red',
    'points': 15
    }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# How to create 30 green aliens automatically

# Empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# Code above: for each alien_number in the range of 30:
# set dictionary 'new_alien' with specific characteristics and append each
# new_alien to the (empty) list of aliens

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Code above: we limit the range of list of aliens to 5 with [:5], so that the
# print operation is limited to this range.

# Show how many aliens have been created
print('Total number of aliens:' + str(len(aliens)))

# Changing the color of 3 aliens in aliens dictionary
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens to check the changes

for alien in aliens[:5]:
    print(alien)
print('...')

# IMPORTANT REMINDER: ln.57, the range ends one unit before the stated range.
# [:5] ends at 4, knowing that the range starts at 0.


for alien in aliens[3:6]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:8]:
    print(alien)
print('...')
